"""
User Model
See: docs/backend/entities/user.md
"""

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.core.database import Base


class UserRole(str, enum.Enum):
    """User roles for RBAC"""
    MEMBER = "member"           # Regular club member
    BUSINESS_ADMIN = "business_admin"  # Business owner/admin
    SUPER_ADMIN = "super_admin"  # System administrator


class StatusTier(str, enum.Enum):
    """Membership status tiers"""
    INSIDER = "insider"      # 0-50K spend
    VIP = "vip"             # 50K-150K spend
    ELITE = "elite"         # 150K-300K spend
    INNER_CIRCLE = "inner_circle"  # 300K+ spend


class User(Base):
    """
    User Entity - Club Members
    
    Represents a member of the Svoy Krug loyalty ecosystem.
    Links to transactions, bonuses, events, and business relationships.
    
    Security:
    - Password hashed with bcrypt (12 rounds)
    - Phone number is unique identifier
    - Created/updated timestamps for audit trail
    
    See full spec: docs/backend/entities/user.md
    """
    
    __tablename__ = "users"
    
    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    # Authentication
    phone: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
    # Profile
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), unique=True, index=True)
    
    # Role & Status
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        default=UserRole.MEMBER,
        nullable=False
    )
    status_tier: Mapped[StatusTier] = mapped_column(
        Enum(StatusTier, name="status_tier"),
        default=StatusTier.INSIDER,
        nullable=False
    )
    
    # Loyalty Metrics
    total_spend: Mapped[float] = mapped_column(default=0.0, nullable=False)
    bonus_balance: Mapped[int] = mapped_column(default=0, nullable=False)
    
    # Flags
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, phone={self.phone}, name={self.first_name} {self.last_name})>"
