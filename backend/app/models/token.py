"""
Token and OTP Code Models
For JWT refresh tokens and SMS OTP verification

See: docs/adr/ADR-004-jwt-authentication.md
"""

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Token(Base):
    """
    Refresh Token Entity

    Stores JWT refresh tokens for user authentication.
    Access tokens are stateless (not stored in DB).
    Refresh tokens are stored for rotation and revocation.

    Security:
    - Token value is hashed (SHA-256) before storage
    - Expiration time: 7 days (configurable)
    - Can be revoked (logout, security breach)
    - One-time use with rotation

    Flow:
    1. User logs in -> Access token (15 min) + Refresh token (7 days) issued
    2. Access token expires -> Client sends refresh token
    3. Backend validates refresh token -> Issues new pair, revokes old refresh token
    4. User logs out -> Refresh token marked as revoked

    See full spec: docs/adr/ADR-004-jwt-authentication.md
    """

    __tablename__ = "tokens"

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Foreign Key to User
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # Token Data
    token_hash: Mapped[str] = mapped_column(
        String(64),  # SHA-256 hash length
        unique=True,
        index=True,
        nullable=False,
        comment="SHA-256 hash of refresh token"
    )

    # Metadata
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
        comment="Token expiration timestamp (7 days from creation)"
    )

    is_revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
        comment="True if token was revoked (logout, rotation, security)"
    )

    # Audit Fields
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Timestamp when token was revoked"
    )

    # Optional: Track device/IP for security
    device_info: Mapped[str | None] = mapped_column(
        String(255),
        comment="User-Agent or device identifier"
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(45),  # IPv6 max length
        comment="IP address where token was issued"
    )

    # Relationships
    # user: Mapped["User"] = relationship("User", back_populates="tokens")

    def __repr__(self) -> str:
        status = "revoked" if self.is_revoked else "active"
        return f"<Token(id={self.id}, user_id={self.user_id}, status={status})>"


class OTPCode(Base):
    """
    SMS OTP Code Entity

    Stores one-time passwords sent via SMS for phone verification.
    Used during registration and login (if 2FA enabled).

    Security:
    - Code is hashed (SHA-256) before storage
    - Expiration time: 5 minutes
    - Rate limiting: max 3 attempts per code
    - Rate limiting: max 5 codes per phone per hour
    - Codes are 6 digits (000000-999999)

    Flow:
    1. User enters phone number
    2. Backend generates 6-digit code, hashes it, sends via SMS.ru
    3. User enters code from SMS
    4. Backend validates code (hash match, not expired, not used, attempts < 3)
    5. Code marked as used, user verified

    Implementation:
    - SMS.ru API integration (docs/backend/services/auth-service.md)
    - Module 12.3.1: SMS OTP Integration

    See full spec: docs/requirements/module-01-mobile-app.md (Function 1.1.3)
    """

    __tablename__ = "otp_codes"

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Phone Number (not FK - user may not exist yet during registration)
    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
        comment="Phone number in format +7XXXXXXXXXX"
    )

    # OTP Data
    code_hash: Mapped[str] = mapped_column(
        String(64),  # SHA-256 hash length
        nullable=False,
        comment="SHA-256 hash of 6-digit OTP code"
    )

    # Expiration & Usage
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
        comment="OTP expiration timestamp (5 minutes from creation)"
    )

    is_used: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
        comment="True if OTP was successfully verified"
    )

    attempts: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="Number of failed verification attempts (max 3)"
    )

    # Audit Fields
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True  # Index for rate limiting queries
    )

    used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Timestamp when OTP was successfully used"
    )

    # Optional: SMS delivery tracking
    sms_status: Mapped[str | None] = mapped_column(
        String(50),
        comment="SMS delivery status from SMS.ru API"
    )

    sms_id: Mapped[str | None] = mapped_column(
        String(100),
        comment="SMS.ru message ID for tracking"
    )

    def __repr__(self) -> str:
        status = "used" if self.is_used else "active"
        return f"<OTPCode(id={self.id}, phone={self.phone}, status={status}, attempts={self.attempts})>"
