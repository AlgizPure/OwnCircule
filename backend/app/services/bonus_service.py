"""
Bonus Service
Business logic for bonus accrual, redemption, and status tier upgrades

See: docs/requirements/module-02-loyalty-system.md
"""

import logging
from datetime import datetime
from typing import Optional, Dict, Any
from sqlalchemy import select, func, and_, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.bonus import Bonus, BonusType, BonusStatus
from app.models.user import User, StatusTier
from app.models.transaction import Transaction, TransactionStatus
from app.models.user_category import UserCategory


logger = logging.getLogger(__name__)


# Cashback rates by status tier
CASHBACK_RATES = {
    StatusTier.INSIDER: 0.05,      # 5%
    StatusTier.VIP: 0.07,          # 7%
    StatusTier.ELITE: 0.10,        # 10%
    StatusTier.INNER_CIRCLE: 0.15, # 15%
}

# Status tier upgrade thresholds (total_spend in rubles)
TIER_THRESHOLDS = {
    StatusTier.VIP: 50_000,        # 50K₽
    StatusTier.ELITE: 150_000,     # 150K₽
    StatusTier.INNER_CIRCLE: 300_000,  # 300K₽
}

# First purchase in category multiplier
FIRST_PURCHASE_MULTIPLIER = 1.5


class BonusService:
    """Service layer for bonus operations"""

    @staticmethod
    async def accrue_bonus(
        db: AsyncSession,
        transaction_id: int
    ) -> Optional[Bonus]:
        """
        Accrue bonus for transaction (called by Celery task)

        Args:
            db: Database session
            transaction_id: Transaction ID

        Returns:
            Created Bonus record or None if transaction not found

        Flow:
            1. Get transaction and validate
            2. Get user and check status tier
            3. Calculate bonus percentage (5-15% based on tier)
            4. Check if first purchase in category → apply 1.5x multiplier
            5. Create Bonus record
            6. Update user.bonus_balance
            7. Check if user should be upgraded to next tier

        Example:
            Transaction: 10,000₽ at Миндаль (Beauty)
            User: VIP status (7% cashback)
            First purchase in Beauty: Yes
            Calculation: 10,000 * 0.07 * 1.5 = 1,050₽ bonus
        """

        # Get transaction
        result = await db.execute(
            select(Transaction).where(Transaction.id == transaction_id)
        )
        transaction = result.scalar_one_or_none()

        if not transaction:
            logger.error(f"Transaction {transaction_id} not found for bonus accrual")
            return None

        if transaction.status != TransactionStatus.COMPLETED:
            logger.warning(f"Transaction {transaction_id} not completed, skipping bonus accrual")
            return None

        # Get user
        result = await db.execute(
            select(User).where(User.id == transaction.user_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            logger.error(f"User {transaction.user_id} not found")
            return None

        # Calculate cashback rate
        cashback_rate = CASHBACK_RATES.get(user.status_tier, 0.05)

        # Check if first purchase in category
        multiplier = 1.0
        is_first_purchase = False

        if transaction.category:
            result = await db.execute(
                select(UserCategory).where(
                    and_(
                        UserCategory.user_id == user.id,
                        UserCategory.category == transaction.category
                    )
                )
            )
            user_category = result.scalar_one_or_none()

            if not user_category:
                # First purchase in this category!
                is_first_purchase = True
                multiplier = FIRST_PURCHASE_MULTIPLIER

                # Create UserCategory record
                user_category = UserCategory(
                    user_id=user.id,
                    category=transaction.category,
                    first_purchase_at=datetime.utcnow(),
                    first_transaction_id=transaction.id,
                    total_purchases=1,
                    total_spent=transaction.amount,
                    last_purchase_at=datetime.utcnow()
                )
                db.add(user_category)

                logger.info(
                    f"First purchase in category {transaction.category} for user {user.id}, "
                    f"applying {multiplier}x multiplier"
                )
            else:
                # Update category stats
                user_category.total_purchases += 1
                user_category.total_spent += transaction.amount
                user_category.last_purchase_at = datetime.utcnow()

        # Calculate bonus amount
        bonus_amount = round(transaction.amount * cashback_rate * multiplier, 2)

        # Create bonus record
        bonus = Bonus(
            user_id=user.id,
            transaction_id=transaction.id,
            amount=bonus_amount,
            type=BonusType.ACCRUAL,
            status=BonusStatus.COMPLETED,
            multiplier=multiplier,
            description=f"Bonus from purchase at business_id={transaction.business_id}",
            expires_at=Bonus.calculate_expiration_date(),
            completed_at=datetime.utcnow()
        )

        db.add(bonus)

        # Update user bonus balance
        user.bonus_balance += bonus_amount

        # Update transaction bonus_amount
        transaction.bonus_amount = bonus_amount

        await db.commit()
        await db.refresh(bonus)

        logger.info(
            f"Bonus accrued: User={user.id}, Amount={bonus_amount}₽, "
            f"Rate={cashback_rate*100}%, Multiplier={multiplier}x, "
            f"FirstPurchase={is_first_purchase}"
        )

        # Check tier upgrade
        await BonusService.check_tier_upgrade(db, user.id)

        # TODO: Send push notification (Module 12)
        # from app.services.notification_service import send_push
        # send_push(user.id, f"Начислено {bonus_amount}₽ бонусов!")

        return bonus

    @staticmethod
    async def redeem_bonus(
        db: AsyncSession,
        user_id: int,
        amount: float
    ) -> Bonus:
        """
        Redeem bonuses (deduct from balance)

        Args:
            db: Database session
            user_id: User ID
            amount: Bonus amount to redeem

        Returns:
            Created Bonus redemption record

        Raises:
            ValueError: If insufficient balance

        Flow:
            1. Get user and check balance
            2. Validate sufficient balance
            3. Create Bonus record with type=REDEMPTION, negative amount
            4. Update user.bonus_balance (deduct)
        """

        # Get user
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            raise ValueError(f"User {user_id} not found")

        # Check balance
        if user.bonus_balance < amount:
            raise ValueError(
                f"Insufficient bonus balance. "
                f"Available: {user.bonus_balance}₽, Required: {amount}₽"
            )

        # Create redemption record (negative amount)
        bonus = Bonus(
            user_id=user.id,
            transaction_id=None,  # No linked transaction
            amount=-amount,  # Negative for redemption
            type=BonusType.REDEMPTION,
            status=BonusStatus.COMPLETED,
            description=f"Bonus redemption: {amount}₽",
            completed_at=datetime.utcnow()
        )

        db.add(bonus)

        # Update user balance
        user.bonus_balance -= amount

        await db.commit()
        await db.refresh(bonus)

        logger.info(f"Bonus redeemed: User={user_id}, Amount={amount}₽, New Balance={user.bonus_balance}₽")

        return bonus

    @staticmethod
    async def get_bonus_history(
        db: AsyncSession,
        user_id: int,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[list[Bonus], int]:
        """
        Get user bonus history

        Args:
            db: Database session
            user_id: User ID
            limit: Max records to return
            offset: Records to skip (pagination)

        Returns:
            Tuple of (bonuses list, total count)
        """

        # Get total count
        count_result = await db.execute(
            select(func.count()).select_from(Bonus).where(Bonus.user_id == user_id)
        )
        total = count_result.scalar()

        # Get bonuses
        result = await db.execute(
            select(Bonus)
            .where(Bonus.user_id == user_id)
            .order_by(desc(Bonus.created_at))
            .offset(offset)
            .limit(limit)
        )
        bonuses = result.scalars().all()

        return bonuses, total

    @staticmethod
    async def get_balance(db: AsyncSession, user_id: int) -> float:
        """
        Get user bonus balance

        Args:
            db: Database session
            user_id: User ID

        Returns:
            Current bonus balance
        """

        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            raise ValueError(f"User {user_id} not found")

        return user.bonus_balance

    @staticmethod
    async def check_tier_upgrade(db: AsyncSession, user_id: int) -> Optional[StatusTier]:
        """
        Check if user should be upgraded to next status tier

        Args:
            db: Database session
            user_id: User ID

        Returns:
            New status tier if upgraded, None otherwise

        Tiers:
            - INSIDER: 0-50K spend (default)
            - VIP: 50K-150K spend
            - ELITE: 150K-300K spend
            - INNER_CIRCLE: 300K+ spend

        Flow:
            1. Get user total_spend
            2. Check against thresholds
            3. Upgrade if threshold reached
            4. Send upgrade notification
        """

        # Get user
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            logger.error(f"User {user_id} not found")
            return None

        total_spend = user.total_spend
        current_tier = user.status_tier

        # Determine new tier
        new_tier = None

        if total_spend >= TIER_THRESHOLDS[StatusTier.INNER_CIRCLE]:
            new_tier = StatusTier.INNER_CIRCLE
        elif total_spend >= TIER_THRESHOLDS[StatusTier.ELITE]:
            new_tier = StatusTier.ELITE
        elif total_spend >= TIER_THRESHOLDS[StatusTier.VIP]:
            new_tier = StatusTier.VIP
        else:
            new_tier = StatusTier.INSIDER

        # Check if upgrade needed
        tier_order = [StatusTier.INSIDER, StatusTier.VIP, StatusTier.ELITE, StatusTier.INNER_CIRCLE]
        current_index = tier_order.index(current_tier)
        new_index = tier_order.index(new_tier)

        if new_index > current_index:
            # Upgrade!
            user.status_tier = new_tier
            await db.commit()

            logger.info(
                f"User {user_id} upgraded: {current_tier.value} → {new_tier.value} "
                f"(total_spend: {total_spend}₽)"
            )

            # TODO: Send upgrade notification (Module 12)
            # from app.services.notification_service import send_push
            # send_push(user.id, f"Поздравляем! Вы получили статус {new_tier.value.upper()}!")

            return new_tier

        return None
