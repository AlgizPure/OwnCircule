"""
UserCategory Model
Tracks which categories user has purchased in (for first purchase multiplier)

See: docs/requirements/module-02-loyalty-system.md (Function 2.1.2)
"""

from datetime import datetime
from sqlalchemy import String, Float, DateTime, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class UserCategory(Base):
    """
    UserCategory Entity - Category Purchase Tracking

    Tracks which categories user has made purchases in.
    Used for first purchase in category multiplier (1.5x bonus).

    Flow:
    1. Transaction created in category X
    2. Check if user has purchased in category X before
    3. If not: Create UserCategory record, apply 1.5x multiplier
    4. If yes: No multiplier

    Example:
        User makes first purchase at Миндаль (Beauty category)
        → UserCategory created: user_id=1, category="Beauty"
        → Bonus multiplier: 1.5x (7% * 1.5 = 10.5% for VIP)

    See full spec: docs/requirements/module-02-loyalty-system.md
    """

    __tablename__ = "user_categories"
    __table_args__ = (
        UniqueConstraint('user_id', 'category', name='uq_user_category'),
    )

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Foreign Key
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="User ID"
    )

    # Category
    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
        comment="Business category (Beauty, Fitness, Wellness, etc.)"
    )

    # First Purchase Info
    first_purchase_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        comment="Timestamp of first purchase in this category"
    )

    first_transaction_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("transactions.id", ondelete="SET NULL"),
        comment="ID of first transaction in this category"
    )

    # Stats
    total_purchases: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
        comment="Total number of purchases in this category"
    )

    total_spent: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False,
        comment="Total amount spent in this category"
    )

    # Timestamps
    last_purchase_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        comment="Timestamp of most recent purchase in this category"
    )

    def __repr__(self) -> str:
        return f"<UserCategory(user_id={self.user_id}, category={self.category}, purchases={self.total_purchases})>"
