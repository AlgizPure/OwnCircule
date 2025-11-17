"""
Auth Service - Authentication Business Logic
Registration, login, OTP verification, token management

See: docs/backend/services/auth-service.md
     docs/adr/ADR-004-jwt-authentication.md
"""

import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User, StatusTier
from app.models.token import Token, OTPCode
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
    hash_token,
    verify_token_hash,
    generate_otp_code
)
from app.core.config import settings
from app.services.sms_service import get_sms_service


logger = logging.getLogger(__name__)


class AuthService:
    """Service layer for authentication operations"""

    # ===================================================================
    # OTP Operations
    # ===================================================================
    @staticmethod
    async def send_otp(db: AsyncSession, phone: str) -> Dict[str, Any]:
        """
        Send OTP code to phone number

        Args:
            db: Database session
            phone: Phone number in format +7XXXXXXXXXX

        Returns:
            Dict with success status and message

        Flow:
            1. Check rate limiting (max 5 OTP codes per phone per hour)
            2. Generate 6-digit OTP code
            3. Hash code with SHA-256
            4. Store hash in database with 5-minute expiration
            5. Send code via SMS.ru API

        Raises:
            ValueError: If rate limit exceeded
        """

        # ===================================================================
        # Rate Limiting: Max 5 OTP codes per phone per hour
        # ===================================================================
        one_hour_ago = datetime.utcnow() - timedelta(hours=1)

        result = await db.execute(
            select(OTPCode)
            .where(
                and_(
                    OTPCode.phone == phone,
                    OTPCode.created_at >= one_hour_ago
                )
            )
        )
        recent_otps = result.scalars().all()

        if len(recent_otps) >= 5:
            logger.warning(f"OTP rate limit exceeded for phone {phone}")
            raise ValueError(
                "Превышен лимит запросов кода. "
                "Попробуйте через час."
            )

        # ===================================================================
        # Generate OTP Code
        # ===================================================================
        code = generate_otp_code(length=6)
        code_hash = hash_token(code)

        # ===================================================================
        # Store OTP in Database
        # ===================================================================
        expires_at = datetime.utcnow() + timedelta(minutes=settings.SMS_OTP_EXPIRE_MINUTES)

        otp_record = OTPCode(
            phone=phone,
            code_hash=code_hash,
            expires_at=expires_at,
            is_used=False,
            attempts=0
        )

        db.add(otp_record)
        await db.commit()
        await db.refresh(otp_record)

        # ===================================================================
        # Send SMS via SMS.ru API
        # ===================================================================
        sms_service = get_sms_service()
        sms_result = await sms_service.send_otp(phone, code)

        # Update OTP record with SMS status
        if sms_result["success"]:
            otp_record.sms_status = "sent"
            otp_record.sms_id = sms_result.get("sms_id")
            logger.info(f"OTP sent to {phone}, SMS ID: {sms_result.get('sms_id')}")
        else:
            otp_record.sms_status = "failed"
            logger.error(f"Failed to send OTP to {phone}: {sms_result['status_text']}")

        await db.commit()

        # Return result
        if not sms_result["success"]:
            raise ValueError(f"Failed to send SMS: {sms_result['status_text']}")

        return {
            "success": True,
            "message": f"OTP code sent to {phone}",
            "expires_in": settings.SMS_OTP_EXPIRE_MINUTES * 60  # seconds
        }

    @staticmethod
    async def verify_otp(db: AsyncSession, phone: str, code: str) -> bool:
        """
        Verify OTP code

        Args:
            db: Database session
            phone: Phone number
            code: 6-digit OTP code from SMS

        Returns:
            True if OTP is valid, False otherwise

        Validation:
            - Code matches hash
            - Not expired (5 minutes)
            - Not already used
            - Attempts < 3

        Side Effects:
            - Increments attempt counter on failure
            - Marks OTP as used on success
        """

        # ===================================================================
        # Find most recent OTP for this phone
        # ===================================================================
        result = await db.execute(
            select(OTPCode)
            .where(OTPCode.phone == phone)
            .order_by(OTPCode.created_at.desc())
            .limit(1)
        )
        otp_record = result.scalar_one_or_none()

        # No OTP found
        if not otp_record:
            logger.warning(f"No OTP found for phone {phone}")
            return False

        # ===================================================================
        # Validation Checks
        # ===================================================================

        # Check if OTP is expired
        if datetime.utcnow() > otp_record.expires_at:
            logger.warning(f"OTP expired for phone {phone}")
            return False

        # Check if OTP is already used
        if otp_record.is_used:
            logger.warning(f"OTP already used for phone {phone}")
            return False

        # Check attempts limit
        if otp_record.attempts >= 3:
            logger.warning(f"OTP max attempts exceeded for phone {phone}")
            return False

        # ===================================================================
        # Verify Code Hash
        # ===================================================================
        if verify_token_hash(code, otp_record.code_hash):
            # Success - mark OTP as used
            otp_record.is_used = True
            otp_record.used_at = datetime.utcnow()
            await db.commit()

            logger.info(f"OTP verified successfully for phone {phone}")
            return True
        else:
            # Failure - increment attempt counter
            otp_record.attempts += 1
            await db.commit()

            logger.warning(
                f"Invalid OTP code for phone {phone} "
                f"(attempt {otp_record.attempts}/3)"
            )
            return False

    # ===================================================================
    # Registration
    # ===================================================================
    @staticmethod
    async def register(
        db: AsyncSession,
        phone: str,
        password: str,
        first_name: str,
        last_name: str
    ) -> Dict[str, Any]:
        """
        Register new user

        Args:
            db: Database session
            phone: Phone number (must be OTP-verified)
            password: User password
            first_name: First name
            last_name: Last name

        Returns:
            Dict with access_token, refresh_token, user_id

        Flow:
            1. Check phone is OTP-verified (has used OTP code)
            2. Check user doesn't already exist
            3. Create user with hashed password
            4. Generate JWT tokens
            5. Store refresh token in database

        Raises:
            ValueError: If phone not verified or user already exists
        """

        # ===================================================================
        # Check OTP Verification
        # ===================================================================
        result = await db.execute(
            select(OTPCode)
            .where(
                and_(
                    OTPCode.phone == phone,
                    OTPCode.is_used == True
                )
            )
            .order_by(OTPCode.used_at.desc())
            .limit(1)
        )
        verified_otp = result.scalar_one_or_none()

        if not verified_otp:
            raise ValueError("Phone number not verified. Please verify OTP first.")

        # Check OTP was verified recently (within 10 minutes)
        if verified_otp.used_at:
            time_since_verification = datetime.utcnow() - verified_otp.used_at
            if time_since_verification > timedelta(minutes=10):
                raise ValueError("OTP verification expired. Please request new code.")

        # ===================================================================
        # Check User Doesn't Exist
        # ===================================================================
        result = await db.execute(select(User).where(User.phone == phone))
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise ValueError(f"User with phone {phone} already exists")

        # ===================================================================
        # Create User
        # ===================================================================
        user = User(
            phone=phone,
            password_hash=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            status_tier=StatusTier.INSIDER,
            is_active=True,
            is_verified=True  # Phone verified via OTP
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        logger.info(f"User registered successfully: {user.id} ({phone})")

        # ===================================================================
        # Generate Tokens
        # ===================================================================
        tokens = await AuthService._create_tokens(db, user)

        return {
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "token_type": "bearer",
            "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "user_id": user.id
        }

    # ===================================================================
    # Login
    # ===================================================================
    @staticmethod
    async def login(db: AsyncSession, phone: str, password: str) -> Dict[str, Any]:
        """
        Authenticate user and generate tokens

        Args:
            db: Database session
            phone: Phone number
            password: User password

        Returns:
            Dict with access_token, refresh_token, user_id

        Flow:
            1. Find user by phone
            2. Verify password
            3. Generate JWT tokens
            4. Store refresh token in database
            5. Update last_login_at

        Raises:
            ValueError: If credentials invalid or user inactive
        """

        # ===================================================================
        # Find User
        # ===================================================================
        result = await db.execute(select(User).where(User.phone == phone))
        user = result.scalar_one_or_none()

        if not user:
            logger.warning(f"Login failed: user not found ({phone})")
            raise ValueError("Неверный телефон или пароль")

        # ===================================================================
        # Check User Active
        # ===================================================================
        if not user.is_active:
            logger.warning(f"Login failed: user inactive ({phone})")
            raise ValueError("Аккаунт деактивирован")

        # ===================================================================
        # Verify Password
        # ===================================================================
        if not verify_password(password, user.password_hash):
            logger.warning(f"Login failed: invalid password ({phone})")
            raise ValueError("Неверный телефон или пароль")

        # ===================================================================
        # Update Last Login
        # ===================================================================
        user.last_login_at = datetime.utcnow()
        await db.commit()

        logger.info(f"User logged in successfully: {user.id} ({phone})")

        # ===================================================================
        # Generate Tokens
        # ===================================================================
        tokens = await AuthService._create_tokens(db, user)

        return {
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "token_type": "bearer",
            "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "user_id": user.id
        }

    # ===================================================================
    # Token Refresh
    # ===================================================================
    @staticmethod
    async def refresh_tokens(db: AsyncSession, refresh_token: str) -> Dict[str, Any]:
        """
        Refresh access token using refresh token

        Args:
            db: Database session
            refresh_token: JWT refresh token

        Returns:
            Dict with new access_token, refresh_token

        Flow:
            1. Validate refresh token JWT signature
            2. Check token not revoked in database
            3. Revoke old refresh token
            4. Generate new token pair
            5. Store new refresh token

        Token Rotation:
            - Old refresh token is revoked (one-time use)
            - New refresh token issued
            - Prevents replay attacks

        Raises:
            ValueError: If token invalid, expired, or revoked
        """

        # ===================================================================
        # Validate JWT
        # ===================================================================
        payload = verify_refresh_token(refresh_token)
        if not payload:
            raise ValueError("Invalid refresh token")

        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("Invalid token payload")

        # ===================================================================
        # Check Token Not Revoked in Database
        # ===================================================================
        token_hash = hash_token(refresh_token)

        result = await db.execute(
            select(Token).where(Token.token_hash == token_hash)
        )
        token_record = result.scalar_one_or_none()

        if not token_record:
            logger.warning(f"Refresh token not found in database (user {user_id})")
            raise ValueError("Invalid refresh token")

        if token_record.is_revoked:
            logger.warning(f"Refresh token already revoked (user {user_id})")
            raise ValueError("Refresh token revoked")

        if datetime.utcnow() > token_record.expires_at:
            logger.warning(f"Refresh token expired (user {user_id})")
            raise ValueError("Refresh token expired")

        # ===================================================================
        # Get User
        # ===================================================================
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user or not user.is_active:
            raise ValueError("User not found or inactive")

        # ===================================================================
        # Revoke Old Refresh Token (Token Rotation)
        # ===================================================================
        token_record.is_revoked = True
        token_record.revoked_at = datetime.utcnow()
        await db.commit()

        logger.info(f"Refresh token rotated for user {user_id}")

        # ===================================================================
        # Generate New Tokens
        # ===================================================================
        tokens = await AuthService._create_tokens(db, user)

        return {
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "token_type": "bearer",
            "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }

    # ===================================================================
    # Logout
    # ===================================================================
    @staticmethod
    async def logout(db: AsyncSession, refresh_token: str) -> bool:
        """
        Logout user by revoking refresh token

        Args:
            db: Database session
            refresh_token: JWT refresh token to revoke

        Returns:
            True if token revoked, False if not found

        Note:
            - Access tokens cannot be revoked (stateless)
            - Access tokens expire in 15 minutes
            - Revoking refresh token prevents getting new access tokens
        """

        token_hash = hash_token(refresh_token)

        result = await db.execute(
            select(Token).where(Token.token_hash == token_hash)
        )
        token_record = result.scalar_one_or_none()

        if not token_record:
            logger.warning("Logout: refresh token not found")
            return False

        if token_record.is_revoked:
            logger.info("Logout: token already revoked")
            return True

        # Revoke token
        token_record.is_revoked = True
        token_record.revoked_at = datetime.utcnow()
        await db.commit()

        logger.info(f"User logged out (user_id: {token_record.user_id})")
        return True

    # ===================================================================
    # Helper: Create Token Pair
    # ===================================================================
    @staticmethod
    async def _create_tokens(db: AsyncSession, user: User) -> Dict[str, str]:
        """
        Generate access + refresh token pair and store refresh token

        Args:
            db: Database session
            user: User instance

        Returns:
            Dict with access_token and refresh_token
        """

        # Generate access token (15 min)
        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "role": user.role.value,
                "status_tier": user.status_tier.value
            }
        )

        # Generate refresh token (7 days)
        refresh_token = create_refresh_token(
            data={"sub": str(user.id)}
        )

        # Store refresh token in database (hashed)
        expires_at = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS)

        token_record = Token(
            user_id=user.id,
            token_hash=hash_token(refresh_token),
            expires_at=expires_at,
            is_revoked=False
        )

        db.add(token_record)
        await db.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
