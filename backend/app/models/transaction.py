"""
Transaction Model
Tracks member purchases across partner businesses

See: docs/requirements/module-03-transactions.md
"""

from datetime import datetime
from sqlalchemy import String, Float, DateTime, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from app.core.database import Base


class TransactionType(str, enum.Enum):
    """Transaction types"""
    PURCHASE = "purchase"           # Regular purchase
    BONUS_REDEMPTION = "bonus_redemption"  # Paid with bonuses
    REFUND = "refund"              # Purchase refund
    ADJUSTMENT = "adjustment"       # Manual adjustment


class TransactionStatus(str, enum.Enum):
    """Transaction statuses"""
    PENDING = "pending"             # Created, awaiting confirmation
    COMPLETED = "completed"         # Confirmed and processed
    CANCELLED = "cancelled"         # Cancelled/refunded
    FAILED = "failed"              # Processing failed


class Transaction(Base):
    """
    Transaction Entity - Member Purchases

    Tracks all purchases across partner businesses.
    Links to users, businesses, and bonus accruals.

    Flow:
    1. Business creates transaction (POST /transactions/)
    2. Transaction created with status=PENDING
    3. Celery task validates and processes transaction
    4. Status updated to COMPLETED
    5. Bonus accrued (linked via bonus.transaction_id)

    See full spec: docs/requirements/module-03-transactions.md
    """

    __tablename__ = "transactions"

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Member who made the purchase"
    )

    business_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Business where purchase was made"
    )

    # Transaction Data
    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        comment="Transaction amount in rubles"
    )

    bonus_amount: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False,
        comment="Bonus amount accrued for this transaction"
    )

    bonus_redeemed: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False,
        comment="Bonus amount redeemed in this transaction"
    )

    # Type & Status
    type: Mapped[TransactionType] = mapped_column(
        Enum(TransactionType, name="transaction_type"),
        default=TransactionType.PURCHASE,
        nullable=False,
        index=True
    )

    status: Mapped[TransactionStatus] = mapped_column(
        Enum(TransactionStatus, name="transaction_status"),
        default=TransactionStatus.PENDING,
        nullable=False,
        index=True
    )

    # Business Category (denormalized for analytics)
    category: Mapped[str | None] = mapped_column(
        String(100),
        index=True,
        comment="Business category (Beauty, Fitness, Wellness, etc.)"
    )

    # Optional Metadata
    description: Mapped[str | None] = mapped_column(
        Text,
        comment="Transaction description or notes"
    )

    receipt_number: Mapped[str | None] = mapped_column(
        String(100),
        comment="Receipt number from POS/CRM system"
    )

    external_id: Mapped[str | None] = mapped_column(
        String(255),
        index=True,
        comment="ID from external CRM system (YCLIENTS, Iiko, 1C)"
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Transaction creation timestamp"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Timestamp when transaction was completed"
    )

    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Timestamp when transaction was cancelled"
    )

    # Relationships
    # user: Mapped["User"] = relationship("User", back_populates="transactions")
    # business: Mapped["Business"] = relationship("Business", back_populates="transactions")
    # bonuses: Mapped[list["Bonus"]] = relationship("Bonus", back_populates="transaction")

    def __repr__(self) -> str:
        return f"<Transaction(id={self.id}, user_id={self.user_id}, amount={self.amount}₽, status={self.status.value})>"
