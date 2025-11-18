"""
Bonus Model
Tracks bonus points accrual and redemption

See: docs/requirements/module-02-loyalty-system.md
"""

from datetime import datetime, timedelta
from sqlalchemy import String, Float, DateTime, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from app.core.database import Base


class BonusType(str, enum.Enum):
    """Bonus types"""
    ACCRUAL = "accrual"           # Bonus accrued from purchase
    REDEMPTION = "redemption"     # Bonus redeemed (negative amount)
    EXPIRY = "expiry"             # Bonus expired (negative amount)
    ADJUSTMENT = "adjustment"     # Manual adjustment
    GIFT = "gift"                 # Gift from another user


class BonusStatus(str, enum.Enum):
    """Bonus statuses"""
    PENDING = "pending"           # Created, awaiting confirmation
    COMPLETED = "completed"       # Confirmed and added to balance
    CANCELLED = "cancelled"       # Cancelled (e.g., transaction refunded)
    EXPIRED = "expired"           # Bonus expired (not used within 1 year)


class Bonus(Base):
    """
    Bonus Entity - Loyalty Points

    Tracks bonus accrual and redemption.
    Bonuses are earned on purchases (5-15% cashback based on status tier)
    and can be redeemed at any partner business.

    Flow (Accrual):
    1. Transaction created (POST /transactions/)
    2. Celery task: accrue_bonus(transaction_id)
    3. Calculate bonus: amount * cashback_rate[user.status_tier]
    4. Check first purchase in category → multiply by 1.5x
    5. Create Bonus record with status=COMPLETED
    6. Update user.bonus_balance
    7. Send push notification

    Flow (Redemption):
    1. User pays with bonuses (POST /bonuses/redeem)
    2. Validate sufficient balance
    3. Create Bonus record with type=REDEMPTION, negative amount
    4. Update user.bonus_balance (deduct)
    5. Create transaction with bonus_redeemed field

    Expiry:
    - Bonuses expire 1 year after accrual
    - Celery task runs daily to expire old bonuses

    See full spec: docs/requirements/module-02-loyalty-system.md
    """

    __tablename__ = "bonuses"

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="User who earned/redeemed bonuses"
    )

    transaction_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("transactions.id", ondelete="SET NULL"),
        index=True,
        comment="Transaction that triggered bonus (null for manual adjustments)"
    )

    # Bonus Data
    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        comment="Bonus amount (positive for accrual, negative for redemption)"
    )

    # Type & Status
    type: Mapped[BonusType] = mapped_column(
        Enum(BonusType, name="bonus_type"),
        default=BonusType.ACCRUAL,
        nullable=False,
        index=True
    )

    status: Mapped[BonusStatus] = mapped_column(
        Enum(BonusStatus, name="bonus_status"),
        default=BonusStatus.PENDING,
        nullable=False,
        index=True
    )

    # Expiration
    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        index=True,
        comment="Bonus expiration date (1 year from accrual)"
    )

    # Metadata
    description: Mapped[str | None] = mapped_column(
        Text,
        comment="Bonus description or notes"
    )

    multiplier: Mapped[float] = mapped_column(
        Float,
        default=1.0,
        nullable=False,
        comment="Multiplier applied (e.g., 1.5 for first purchase in category)"
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Timestamp when bonus was completed"
    )

    # Relationships
    # user: Mapped["User"] = relationship("User", back_populates="bonuses")
    # transaction: Mapped["Transaction"] = relationship("Transaction", back_populates="bonuses")

    def __repr__(self) -> str:
        return f"<Bonus(id={self.id}, user_id={self.user_id}, amount={self.amount}, type={self.type.value})>"

    @staticmethod
    def calculate_expiration_date() -> datetime:
        """Calculate bonus expiration date (1 year from now)"""
        return datetime.utcnow() + timedelta(days=365)
