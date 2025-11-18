"""
Transaction API Tests
Test transaction endpoints (create, get, list, update, cancel, stats)

Run with: pytest tests/test_transaction_api.py -v
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from app.models.user import User, UserRole, StatusTier
from app.models.business import Business
from app.core.security import hash_password


@pytest.mark.asyncio
class TestTransactionAPI:
    """Test suite for Transaction API endpoints"""

    # ===================================================================
    # Create Transaction Tests
    # ===================================================================
    async def test_create_transaction_success(self, client: AsyncClient, db_session: AsyncSession):
        """Test creating transaction successfully"""
        # Create user
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
            is_verified=True
        )
        db_session.add(user)

        # Create business
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

        # Create transaction (as admin)
        # Note: For testing, we'll simulate admin access
        response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": user.id,
                "business_id": business.id,
                "amount": 10000.0,
                "type": "purchase",
                "description": "Test purchase"
            }
        )

        assert response.status_code == 201
        data = response.json()

        assert data["user_id"] == user.id
        assert data["business_id"] == business.id
        assert data["amount"] == 10000.0
        assert data["type"] == "purchase"
        assert data["status"] == "pending"
        assert data["category"] == "Beauty"

    async def test_create_transaction_invalid_amount(self, client: AsyncClient):
        """Test creating transaction with invalid amount"""
        response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": 1,
                "business_id": 1,
                "amount": -100.0,  # Negative amount
                "type": "purchase"
            }
        )

        assert response.status_code == 422  # Validation error

    async def test_create_transaction_nonexistent_user(self, client: AsyncClient, db_session: AsyncSession):
        """Test creating transaction for nonexistent user"""
        business = Business(
            name="Test Business",
            slug="test",
            category="Beauty",
            is_active=True
        )
        db_session.add(business)
        await db_session.commit()
        await db_session.refresh(business)

        response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": 99999,  # Doesn't exist
                "business_id": business.id,
                "amount": 1000.0,
                "type": "purchase"
            }
        )

        assert response.status_code == 400
        assert "not found" in response.json()["detail"].lower()

    # ===================================================================
    # Get Transaction Tests
    # ===================================================================
    async def test_get_transaction_by_id(self, client: AsyncClient, db_session: AsyncSession):
        """Test getting transaction by ID"""
        # Setup user and business
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
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

        # Create transaction
        create_response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": user.id,
                "business_id": business.id,
                "amount": 5000.0,
                "type": "purchase"
            }
        )
        transaction_id = create_response.json()["id"]

        # Get transaction
        response = await client.get(f"/api/v1/transactions/{transaction_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == transaction_id
        assert data["amount"] == 5000.0

    async def test_get_transaction_not_found(self, client: AsyncClient):
        """Test getting nonexistent transaction"""
        response = await client.get("/api/v1/transactions/99999")

        assert response.status_code == 404

    # ===================================================================
    # List Transactions Tests
    # ===================================================================
    async def test_list_transactions(self, client: AsyncClient, db_session: AsyncSession):
        """Test listing transactions with pagination"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
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

        # Create 3 transactions
        for i in range(3):
            await client.post(
                "/api/v1/transactions/",
                json={
                    "user_id": user.id,
                    "business_id": business.id,
                    "amount": 1000.0 * (i + 1),
                    "type": "purchase"
                }
            )

        # List transactions
        response = await client.get("/api/v1/transactions/")

        assert response.status_code == 200
        data = response.json()

        assert data["total"] >= 3
        assert len(data["transactions"]) >= 3
        assert data["page"] == 1

    # ===================================================================
    # Update Transaction Tests
    # ===================================================================
    async def test_update_transaction_status(self, client: AsyncClient, db_session: AsyncSession):
        """Test updating transaction status"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
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

        # Create transaction
        create_response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": user.id,
                "business_id": business.id,
                "amount": 2000.0,
                "type": "purchase"
            }
        )
        transaction_id = create_response.json()["id"]

        # Update status
        response = await client.patch(
            f"/api/v1/transactions/{transaction_id}",
            json={"status": "completed"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "completed"
        assert data["completed_at"] is not None

    # ===================================================================
    # Cancel Transaction Tests
    # ===================================================================
    async def test_cancel_transaction(self, client: AsyncClient, db_session: AsyncSession):
        """Test cancelling transaction"""
        # Setup
        user = User(
            phone="+79991234567",
            password_hash=hash_password("Test123"),
            first_name="Анна",
            last_name="Иванова",
            status_tier=StatusTier.INSIDER,
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

        # Create transaction
        create_response = await client.post(
            "/api/v1/transactions/",
            json={
                "user_id": user.id,
                "business_id": business.id,
                "amount": 3000.0,
                "type": "purchase"
            }
        )
        transaction_id = create_response.json()["id"]

        # Cancel transaction
        response = await client.delete(f"/api/v1/transactions/{transaction_id}")

        assert response.status_code == 204

        # Verify cancelled
        get_response = await client.get(f"/api/v1/transactions/{transaction_id}")
        assert get_response.json()["status"] == "cancelled"

    # ===================================================================
    # Statistics Tests
    # ===================================================================
    async def test_get_transaction_stats(self, client: AsyncClient, db_session: AsyncSession):
        """Test getting transaction statistics"""
        # This test would require authentication setup
        # Placeholder for now
        pass
