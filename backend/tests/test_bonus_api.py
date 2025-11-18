"""
Bonus API Tests
Test bonus endpoints (balance, history, redeem, accrue)

Run with: pytest tests/test_bonus_api.py -v
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User, UserRole, StatusTier
from app.models.business import Business
from app.models.transaction import Transaction, TransactionType, TransactionStatus
from app.core.security import hash_password


@pytest.mark.asyncio
class TestBonusAPI:
    """Test suite for Bonus API endpoints"""

    # ===================================================================
    # Get Balance Tests
    # ===================================================================
    async def test_get_bonus_balance(self, client: AsyncClient, db_session: AsyncSession):
        """Test getting bonus balance"""
        # Create user with initial bonus balance
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,
            bonus_balance=1250.50,
            is_verified=True
        )
        db_session.add(user)
        await db_session.commit()

        # Get balance (requires auth - placeholder)
        # response = await client.get("/api/v1/bonuses/balance")
        # assert response.status_code == 200
        # assert response.json()["balance"] == 1250.50

    # ===================================================================
    # Bonus Accrual Tests
    # ===================================================================
    async def test_accrue_bonus_insider_tier(self, client: AsyncClient, db_session: AsyncSession):
        """Test bonus accrual for Insider tier (5% cashback)"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,  # 5% cashback
            bonus_balance=0.0,
            total_spend=0.0,
            is_verified=True
        )
        db_session.add(user)

        business = Business(
            name="Миндаль",
            slug="mindal",
            category="Beauty",
            is_active=True
        )
        db_session.add(business)
        await db_session.commit()
        await db_session.refresh(user)
        await db_session.refresh(business)

        # Create transaction
        transaction = Transaction(
            user_id=user.id,
            business_id=business.id,
            amount=10000.0,
            type=TransactionType.PURCHASE,
            status=TransactionStatus.COMPLETED,
            category="Beauty"
        )
        db_session.add(transaction)
        await db_session.commit()
        await db_session.refresh(transaction)

        # Accrue bonus (manually trigger)
        from app.services.bonus_service import BonusService
        bonus = await BonusService.accrue_bonus(db_session, transaction.id)

        assert bonus is not None
        assert bonus.amount == 500.0  # 10,000 * 5% = 500
        assert bonus.multiplier == 1.0  # No multiplier
        assert bonus.type.value == "accrual"
        assert bonus.status.value == "completed"

        # Check user balance updated
        await db_session.refresh(user)
        assert user.bonus_balance == 500.0

    async def test_accrue_bonus_vip_tier(self, client: AsyncClient, db_session: AsyncSession):
        """Test bonus accrual for VIP tier (7% cashback)"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,  # 7% cashback
            bonus_balance=0.0,
            total_spend=60000.0,  # Already VIP
            is_verified=True
        )
        db_session.add(user)

        business = Business(
            name="Миндаль",
            slug="mindal",
            category="Beauty",
            is_active=True
        )
        db_session.add(business)
        await db_session.commit()
        await db_session.refresh(user)
        await db_session.refresh(business)

        # Create transaction
        transaction = Transaction(
            user_id=user.id,
            business_id=business.id,
            amount=10000.0,
            type=TransactionType.PURCHASE,
            status=TransactionStatus.COMPLETED,
            category="Beauty"
        )
        db_session.add(transaction)
        await db_session.commit()
        await db_session.refresh(transaction)

        # Accrue bonus
        from app.services.bonus_service import BonusService
        bonus = await BonusService.accrue_bonus(db_session, transaction.id)

        assert bonus is not None
        assert bonus.amount == 700.0  # 10,000 * 7% = 700
        assert bonus.multiplier == 1.0

    async def test_accrue_bonus_first_purchase_multiplier(self, client: AsyncClient, db_session: AsyncSession):
        """Test first purchase in category multiplier (1.5x)"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,  # 7% cashback
            bonus_balance=0.0,
            total_spend=60000.0,
            is_verified=True
        )
        db_session.add(user)

        business = Business(
            name="Миндаль",
            slug="mindal",
            category="Beauty",
            is_active=True
        )
        db_session.add(business)
        await db_session.commit()
        await db_session.refresh(user)
        await db_session.refresh(business)

        # Create FIRST transaction in Beauty category
        transaction = Transaction(
            user_id=user.id,
            business_id=business.id,
            amount=10000.0,
            type=TransactionType.PURCHASE,
            status=TransactionStatus.COMPLETED,
            category="Beauty"
        )
        db_session.add(transaction)
        await db_session.commit()
        await db_session.refresh(transaction)

        # Accrue bonus
        from app.services.bonus_service import BonusService
        bonus = await BonusService.accrue_bonus(db_session, transaction.id)

        assert bonus is not None
        assert bonus.amount == 1050.0  # 10,000 * 7% * 1.5 = 1,050
        assert bonus.multiplier == 1.5  # First purchase multiplier applied!

        # Verify UserCategory created
        from app.models.user_category import UserCategory
        from sqlalchemy import select
        result = await db_session.execute(
            select(UserCategory).where(
                UserCategory.user_id == user.id,
                UserCategory.category == "Beauty"
            )
        )
        user_category = result.scalar_one_or_none()
        assert user_category is not None
        assert user_category.total_purchases == 1

    # ===================================================================
    # Bonus Redemption Tests
    # ===================================================================
    async def test_redeem_bonus_success(self, client: AsyncClient, db_session: AsyncSession):
        """Test redeeming bonuses successfully"""
        # Setup user with balance
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,
            bonus_balance=1000.0,  # Has 1000₽ bonuses
            is_verified=True
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)

        # Redeem 500₽
        from app.services.bonus_service import BonusService
        bonus = await BonusService.redeem_bonus(db_session, user.id, 500.0)

        assert bonus is not None
        assert bonus.amount == -500.0  # Negative for redemption
        assert bonus.type.value == "redemption"
        assert bonus.status.value == "completed"

        # Check balance updated
        await db_session.refresh(user)
        assert user.bonus_balance == 500.0  # 1000 - 500 = 500

    async def test_redeem_bonus_insufficient_balance(self, client: AsyncClient, db_session: AsyncSession):
        """Test redeeming bonuses with insufficient balance"""
        # Setup user with low balance
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,
            bonus_balance=100.0,  # Only 100₽
            is_verified=True
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)

        # Try to redeem 500₽ (more than balance)
        from app.services.bonus_service import BonusService
        with pytest.raises(ValueError) as exc_info:
            await BonusService.redeem_bonus(db_session, user.id, 500.0)

        assert "Insufficient" in str(exc_info.value)

    # ===================================================================
    # Status Tier Upgrade Tests
    # ===================================================================
    async def test_tier_upgrade_to_vip(self, client: AsyncClient, db_session: AsyncSession):
        """Test automatic upgrade from Insider to VIP at 50K spend"""
        # Setup user just below threshold
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
            bonus_balance=0.0,
            total_spend=49000.0,  # Just below 50K
            is_verified=True
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)

        # Check tier upgrade with 51K total spend
        user.total_spend = 51000.0
        await db_session.commit()

        from app.services.bonus_service import BonusService
        new_tier = await BonusService.check_tier_upgrade(db_session, user.id)

        assert new_tier == StatusTier.VIP
        await db_session.refresh(user)
        assert user.status_tier == StatusTier.VIP

    async def test_tier_upgrade_to_elite(self, client: AsyncClient, db_session: AsyncSession):
        """Test automatic upgrade from VIP to Elite at 150K spend"""
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.VIP,
            bonus_balance=0.0,
            total_spend=160000.0,  # Above 150K
            is_verified=True
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)

        from app.services.bonus_service import BonusService
        new_tier = await BonusService.check_tier_upgrade(db_session, user.id)

        assert new_tier == StatusTier.ELITE
        await db_session.refresh(user)
        assert user.status_tier == StatusTier.ELITE
