"""
Auth API Endpoints
Registration, login, OTP verification, token refresh, logout

See: docs/backend/api/auth-api.md
"""

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.auth import (
    SendOTPRequest,
    VerifyOTPRequest,
    RegisterRequest,
    LoginRequest,
    RefreshTokenRequest,
    LogoutRequest,
    TokenResponse,
    OTPSentResponse,
    OTPVerifiedResponse,
    LogoutResponse
)
from app.services.auth_service import AuthService
from app.services.sms_service import SMSService


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ===================================================================
# OTP Endpoints
# ===================================================================
@router.post(
    "/send-otp",
    response_model=OTPSentResponse,
    status_code=status.HTTP_200_OK,
    summary="Send OTP code to phone",
    description="""
    Send 6-digit OTP code via SMS to phone number.

    **Rate Limiting:**
    - Max 5 OTP codes per phone per hour

    **OTP Expiration:**
    - 5 minutes

    **Flow:**
    1. User enters phone number
    2. Backend generates 6-digit code
    3. Code sent via SMS.ru API
    4. User receives SMS with code
    """
)
async def send_otp(
    request: SendOTPRequest,
    db: AsyncSession = Depends(get_db)
):
    """Send OTP code to phone number"""
    try:
        result = await AuthService.send_otp(db, request.phone)

        # Format phone for display
        formatted_phone = SMSService.format_phone_for_display(request.phone)

        return OTPSentResponse(
            message=f"OTP code sent to {formatted_phone}",
            phone=formatted_phone,
            expires_in=result["expires_in"]
        )

    except ValueError as e:
        logger.warning(f"Send OTP failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Send OTP error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка отправки кода. Попробуйте позже."
        )


@router.post(
    "/verify-otp",
    response_model=OTPVerifiedResponse,
    status_code=status.HTTP_200_OK,
    summary="Verify OTP code",
    description="""
    Verify 6-digit OTP code received via SMS.

    **Validation:**
    - Code must match SMS code
    - Code not expired (5 minutes)
    - Code not already used
    - Max 3 attempts per code

    **Flow:**
    1. User enters code from SMS
    2. Backend validates code
    3. If valid, phone number is verified
    4. User can proceed to registration
    """
)
async def verify_otp(
    request: VerifyOTPRequest,
    db: AsyncSession = Depends(get_db)
):
    """Verify OTP code"""
    try:
        is_valid = await AuthService.verify_otp(db, request.phone, request.code)

        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Неверный код или код истёк"
            )

        return OTPVerifiedResponse(
            message="Phone number verified successfully",
            phone=request.phone
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Verify OTP error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка проверки кода"
        )


# ===================================================================
# Registration Endpoint
# ===================================================================
@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register new user",
    description="""
    Register new user after OTP verification.

    **Prerequisites:**
    - Phone must be verified via OTP (call /auth/verify-otp first)

    **Password Requirements:**
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit

    **Returns:**
    - Access token (15 min expiration)
    - Refresh token (7 days expiration)

    **Flow:**
    1. User verifies phone via OTP
    2. User fills registration form (password, first_name, last_name)
    3. Backend creates user account
    4. JWT tokens issued
    5. User logged in automatically
    """
)
async def register(
    request: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    """Register new user"""
    try:
        result = await AuthService.register(
            db,
            phone=request.phone,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name
        )

        logger.info(f"User registered: {result['user_id']}")

        return TokenResponse(
            access_token=result["access_token"],
            refresh_token=result["refresh_token"],
            token_type=result["token_type"],
            expires_in=result["expires_in"]
        )

    except ValueError as e:
        logger.warning(f"Registration failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Registration error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка регистрации"
        )


# ===================================================================
# Login Endpoint
# ===================================================================
@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Login user",
    description="""
    Authenticate user with phone + password.

    **Returns:**
    - Access token (15 min expiration)
    - Refresh token (7 days expiration)

    **Flow:**
    1. User enters phone + password
    2. Backend validates credentials
    3. JWT tokens issued
    4. User logged in
    """
)
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """Login user"""
    try:
        result = await AuthService.login(
            db,
            phone=request.phone,
            password=request.password
        )

        logger.info(f"User logged in: {result['user_id']}")

        return TokenResponse(
            access_token=result["access_token"],
            refresh_token=result["refresh_token"],
            token_type=result["token_type"],
            expires_in=result["expires_in"]
        )

    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Login error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка входа"
        )


# ===================================================================
# Token Refresh Endpoint
# ===================================================================
@router.post(
    "/refresh",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Refresh access token",
    description="""
    Get new access token using refresh token.

    **Token Rotation:**
    - Old refresh token is revoked (one-time use)
    - New access + refresh token pair issued
    - Prevents replay attacks

    **Flow:**
    1. Access token expires (15 min)
    2. Client sends refresh token
    3. Backend validates refresh token
    4. New token pair issued
    5. Old refresh token revoked
    """
)
async def refresh(
    request: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db)
):
    """Refresh access token"""
    try:
        result = await AuthService.refresh_tokens(db, request.refresh_token)

        return TokenResponse(
            access_token=result["access_token"],
            refresh_token=result["refresh_token"],
            token_type=result["token_type"],
            expires_in=result["expires_in"]
        )

    except ValueError as e:
        logger.warning(f"Token refresh failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Token refresh error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка обновления токена"
        )


# ===================================================================
# Logout Endpoint
# ===================================================================
@router.post(
    "/logout",
    response_model=LogoutResponse,
    status_code=status.HTTP_200_OK,
    summary="Logout user",
    description="""
    Logout user by revoking refresh token.

    **Note:**
    - Access tokens cannot be revoked (stateless)
    - Access tokens expire in 15 minutes
    - Revoking refresh token prevents getting new access tokens

    **Flow:**
    1. User clicks "Logout"
    2. Client sends refresh token
    3. Backend revokes refresh token
    4. User logged out
    """
)
async def logout(
    request: LogoutRequest,
    db: AsyncSession = Depends(get_db)
):
    """Logout user"""
    try:
        success = await AuthService.logout(db, request.refresh_token)

        if not success:
            logger.warning("Logout: token not found")

        return LogoutResponse(message="Logged out successfully")

    except Exception as e:
        logger.exception(f"Logout error: {str(e)}")
        # Even if error, return success (token might already be revoked)
        return LogoutResponse(message="Logged out successfully")
