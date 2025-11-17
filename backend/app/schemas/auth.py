"""
Authentication Schemas
Pydantic models for auth endpoints (register, login, refresh, logout)

See: docs/backend/api/auth-api.md
     docs/adr/ADR-004-jwt-authentication.md
"""

from pydantic import BaseModel, Field, field_validator
import re


# ===================================================================
# Registration Schemas
# ===================================================================
class SendOTPRequest(BaseModel):
    """
    Request to send OTP code to phone

    Endpoint: POST /auth/send-otp
    """
    phone: str = Field(
        ...,
        description="Phone number in format +7XXXXXXXXXX",
        examples=["+79991234567"]
    )

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        """Validate Russian phone number format"""
        # Remove spaces and dashes
        phone = v.replace(" ", "").replace("-", "")

        # Check format: +7XXXXXXXXXX or 79XXXXXXXXXX
        pattern = r'^\+?7\d{10}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'Phone must be in format +7XXXXXXXXXX (e.g., +79991234567)'
            )

        # Ensure + prefix
        if not phone.startswith('+'):
            phone = '+' + phone

        return phone


class VerifyOTPRequest(BaseModel):
    """
    Request to verify OTP code

    Endpoint: POST /auth/verify-otp
    """
    phone: str = Field(
        ...,
        description="Phone number in format +7XXXXXXXXXX",
        examples=["+79991234567"]
    )
    code: str = Field(
        ...,
        description="6-digit OTP code from SMS",
        min_length=6,
        max_length=6,
        examples=["123456"]
    )

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        """Validate Russian phone number format"""
        phone = v.replace(" ", "").replace("-", "")
        pattern = r'^\+?7\d{10}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'Phone must be in format +7XXXXXXXXXX (e.g., +79991234567)'
            )
        if not phone.startswith('+'):
            phone = '+' + phone
        return phone

    @field_validator('code')
    @classmethod
    def validate_code(cls, v: str) -> str:
        """Validate OTP code is 6 digits"""
        if not v.isdigit():
            raise ValueError('OTP code must contain only digits')
        if len(v) != 6:
            raise ValueError('OTP code must be exactly 6 digits')
        return v


class RegisterRequest(BaseModel):
    """
    Registration request (after OTP verification)

    Endpoint: POST /auth/register
    """
    phone: str = Field(
        ...,
        description="Phone number in format +7XXXXXXXXXX (must be verified)",
        examples=["+79991234567"]
    )
    password: str = Field(
        ...,
        description="Password (8+ chars, uppercase, lowercase, digit)",
        min_length=8,
        max_length=128
    )
    first_name: str = Field(
        ...,
        description="First name",
        min_length=1,
        max_length=100,
        examples=["Анна"]
    )
    last_name: str = Field(
        ...,
        description="Last name",
        min_length=1,
        max_length=100,
        examples=["Иванова"]
    )

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        """Validate Russian phone number format"""
        phone = v.replace(" ", "").replace("-", "")
        pattern = r'^\+?7\d{10}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'Phone must be in format +7XXXXXXXXXX (e.g., +79991234567)'
            )
        if not phone.startswith('+'):
            phone = '+' + phone
        return phone

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Validate password strength

        Requirements:
        - At least 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        """
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')

        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')

        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')

        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')

        return v


# ===================================================================
# Login Schemas
# ===================================================================
class LoginRequest(BaseModel):
    """
    Login request with phone + password

    Endpoint: POST /auth/login
    """
    phone: str = Field(
        ...,
        description="Phone number in format +7XXXXXXXXXX",
        examples=["+79991234567"]
    )
    password: str = Field(
        ...,
        description="User password"
    )

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        """Validate Russian phone number format"""
        phone = v.replace(" ", "").replace("-", "")
        pattern = r'^\+?7\d{10}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'Phone must be in format +7XXXXXXXXXX (e.g., +79991234567)'
            )
        if not phone.startswith('+'):
            phone = '+' + phone
        return phone


# ===================================================================
# Token Schemas
# ===================================================================
class TokenResponse(BaseModel):
    """
    JWT token response

    Returned by:
    - POST /auth/register
    - POST /auth/login
    - POST /auth/refresh
    """
    access_token: str = Field(
        ...,
        description="JWT access token (15 min expiration)"
    )
    refresh_token: str = Field(
        ...,
        description="JWT refresh token (7 days expiration)"
    )
    token_type: str = Field(
        default="bearer",
        description="Token type (always 'bearer')"
    )
    expires_in: int = Field(
        ...,
        description="Access token expiration in seconds (900 = 15 min)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 900
            }
        }


class RefreshTokenRequest(BaseModel):
    """
    Refresh token request

    Endpoint: POST /auth/refresh
    """
    refresh_token: str = Field(
        ...,
        description="JWT refresh token from previous login/refresh"
    )


# ===================================================================
# Logout Schema
# ===================================================================
class LogoutRequest(BaseModel):
    """
    Logout request (revoke refresh token)

    Endpoint: POST /auth/logout
    """
    refresh_token: str = Field(
        ...,
        description="JWT refresh token to revoke"
    )


class LogoutResponse(BaseModel):
    """
    Logout response

    Endpoint: POST /auth/logout
    """
    message: str = Field(
        default="Logged out successfully",
        description="Success message"
    )


# ===================================================================
# Response Schemas
# ===================================================================
class OTPSentResponse(BaseModel):
    """
    Response after sending OTP

    Endpoint: POST /auth/send-otp
    """
    message: str = Field(
        ...,
        description="Success message",
        examples=["OTP code sent to +7 999 123-45-67"]
    )
    phone: str = Field(
        ...,
        description="Formatted phone number",
        examples=["+7 999 123-45-67"]
    )
    expires_in: int = Field(
        ...,
        description="OTP expiration in seconds (300 = 5 min)"
    )


class OTPVerifiedResponse(BaseModel):
    """
    Response after successful OTP verification

    Endpoint: POST /auth/verify-otp
    """
    message: str = Field(
        default="Phone number verified successfully",
        description="Success message"
    )
    phone: str = Field(
        ...,
        description="Verified phone number",
        examples=["+79991234567"]
    )
