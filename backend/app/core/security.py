"""
Security Utilities
JWT tokens, password hashing, OTP hashing, encryption

See: docs/adr/ADR-004-jwt-authentication.md
"""

import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings


# ===================================================================
# Password Hashing (bcrypt)
# ===================================================================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash password using bcrypt (12 rounds)

    Args:
        password: Plain text password

    Returns:
        Hashed password string

    Security:
        - bcrypt with 12 rounds (configurable via PASSWORD_HASH_ROUNDS)
        - Salted automatically by bcrypt
    """
    return pwd_context.hash(password, rounds=settings.PASSWORD_HASH_ROUNDS)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password against hash

    Args:
        plain_password: Plain text password from user input
        hashed_password: Hashed password from database

    Returns:
        True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


# ===================================================================
# Token Hashing (SHA-256)
# ===================================================================
def hash_token(token: str) -> str:
    """
    Hash token using SHA-256 for storage in database

    Used for:
    - Refresh tokens (stored in tokens table)
    - OTP codes (stored in otp_codes table)

    Args:
        token: Plain token string

    Returns:
        SHA-256 hex digest (64 characters)

    Security:
        - SHA-256 (one-way hash)
        - Tokens stored as hash in DB (not plain text)
        - If DB compromised, tokens cannot be recovered
    """
    return hashlib.sha256(token.encode()).hexdigest()


def verify_token_hash(plain_token: str, token_hash: str) -> bool:
    """
    Verify token against stored hash

    Args:
        plain_token: Plain token from user/client
        token_hash: SHA-256 hash from database

    Returns:
        True if token matches hash, False otherwise
    """
    return hash_token(plain_token) == token_hash


# ===================================================================
# JWT Token Generation (RS256)
# ===================================================================
# NOTE: For RS256, we need RSA key pair (private + public keys)
# For development, we'll use HS256 temporarily until keys are generated
# Production MUST use RS256 with proper key management
# ===================================================================

# TODO: Generate RSA key pair for production
# For now, use HS256 for simplicity in development
# Command to generate keys:
#   openssl genrsa -out private_key.pem 2048
#   openssl rsa -in private_key.pem -pubout -out public_key.pem
ALGORITHM = "HS256"  # TODO: Change to RS256 in production with proper keys


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create JWT access token

    Args:
        data: Payload data (user_id, role, etc.)
        expires_delta: Optional custom expiration time

    Returns:
        JWT token string

    Token Structure:
        {
            "sub": user_id (subject),
            "role": user_role,
            "exp": expiration_timestamp,
            "iat": issued_at_timestamp,
            "type": "access"
        }

    Expiration:
        - Default: 15 minutes
        - Configurable via JWT_ACCESS_TOKEN_EXPIRE_MINUTES

    Security:
        - Short expiration (15 min) for access tokens
        - Stateless (not stored in DB)
        - Signature verified on each request
    """
    to_encode = data.copy()

    # Set expiration
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    # Add standard claims
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "access"
    })

    # Encode token
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create JWT refresh token

    Args:
        data: Payload data (user_id)
        expires_delta: Optional custom expiration time

    Returns:
        JWT token string

    Token Structure:
        {
            "sub": user_id (subject),
            "exp": expiration_timestamp,
            "iat": issued_at_timestamp,
            "type": "refresh",
            "jti": unique_token_id (for rotation tracking)
        }

    Expiration:
        - Default: 7 days
        - Configurable via JWT_REFRESH_TOKEN_EXPIRE_DAYS

    Security:
        - Longer expiration (7 days) for refresh tokens
        - Stored in DB (hashed) for revocation
        - One-time use (rotation on refresh)
        - Includes jti (JWT ID) for tracking
    """
    to_encode = data.copy()

    # Set expiration
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS)

    # Generate unique token ID (jti) for tracking
    jti = secrets.token_urlsafe(32)

    # Add standard claims
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "refresh",
        "jti": jti
    })

    # Encode token
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Dict[str, Any]:
    """
    Decode and validate JWT token

    Args:
        token: JWT token string

    Returns:
        Decoded payload dict

    Raises:
        JWTError: If token is invalid, expired, or tampered

    Validation:
        - Signature verification
        - Expiration check
        - Token structure validation
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise JWTError(f"Invalid token: {str(e)}")


def verify_access_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify access token and return payload

    Args:
        token: JWT access token

    Returns:
        Payload dict if valid, None if invalid

    Checks:
        - Token signature
        - Token expiration
        - Token type is "access"
    """
    try:
        payload = decode_token(token)

        # Check token type
        if payload.get("type") != "access":
            return None

        return payload
    except JWTError:
        return None


def verify_refresh_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify refresh token and return payload

    Args:
        token: JWT refresh token

    Returns:
        Payload dict if valid, None if invalid

    Checks:
        - Token signature
        - Token expiration
        - Token type is "refresh"

    Note:
        This only validates JWT structure.
        Additional checks required:
        - Check token not revoked in DB
        - Check token not already used (rotation)
    """
    try:
        payload = decode_token(token)

        # Check token type
        if payload.get("type") != "refresh":
            return None

        return payload
    except JWTError:
        return None


# ===================================================================
# OTP Code Generation
# ===================================================================
def generate_otp_code(length: int = 6) -> str:
    """
    Generate random OTP code

    Args:
        length: Number of digits (default 6)

    Returns:
        OTP code string (e.g., "123456")

    Security:
        - Uses secrets module (cryptographically secure)
        - Range: 000000 to 999999 for 6 digits
    """
    # Generate random number in range [0, 10^length)
    otp = secrets.randbelow(10 ** length)

    # Format with leading zeros
    return str(otp).zfill(length)


# ===================================================================
# Utilities
# ===================================================================
def get_password_hash(password: str) -> str:
    """
    Alias for hash_password (backward compatibility)
    """
    return hash_password(password)
