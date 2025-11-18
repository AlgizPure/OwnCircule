"""
Transaction API Endpoints
Create, retrieve, filter transactions, and get statistics

See: docs/requirements/module-03-transactions.md
"""

import logging
import math
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from datetime import datetime

from app.core.database import get_db
from app.core.auth import get_current_user, require_business_admin
from app.models.user import User
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionRead,
    TransactionList,
    TransactionStats,
    TransactionFilters,
)
from app.services.transaction_service import TransactionService


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


# ===================================================================
# Transaction CRUD Endpoints
# ===================================================================
@router.post(
    "/",
    response_model=TransactionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create transaction",
    description="""
    Create a new transaction (manual entry or QR scan).

    **Authorization:** Business admin or super admin

    **Flow:**
    1. Business staff scans member QR code or enters ID
    2. Staff enters transaction amount and type
    3. Transaction created with status=PENDING
    4. Bonus accrued automatically (Celery task)
    5. Member receives push notification

    **Transaction Types:**
    - `purchase`: Regular purchase (default)
    - `bonus_redemption`: Paid with bonuses
    - `refund`: Purchase refund
    - `adjustment`: Manual adjustment
    """
)
async def create_transaction(
    transaction_data: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_business_admin)
):
    """Create transaction"""
    try:
        transaction = await TransactionService.create_transaction(db, transaction_data)
        return transaction

    except ValueError as e:
        logger.warning(f"Transaction creation failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Transaction creation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка создания транзакции"
        )


@router.get(
    "/{transaction_id}",
    response_model=TransactionRead,
    summary="Get transaction by ID",
    description="""
    Retrieve transaction details by ID.

    **Authorization:** User can only view own transactions (unless admin)
    """
)
async def get_transaction(
    transaction_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get transaction by ID"""
    transaction = await TransactionService.get_by_id(db, transaction_id)

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    # Authorization: user can only view own transactions
    if current_user.role.value == "member" and transaction.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    return transaction


@router.get(
    "/",
    response_model=TransactionList,
    summary="List transactions",
    description="""
    Get paginated and filtered transaction list.

    **Filters:**
    - user_id: Filter by user
    - business_id: Filter by business
    - category: Filter by category (Beauty, Fitness, etc.)
    - type: Filter by transaction type
    - status: Filter by status
    - date_from, date_to: Date range filter
    - min_amount, max_amount: Amount range filter

    **Pagination:**
    - page: Page number (default: 1)
    - per_page: Items per page (default: 20, max: 100)

    **Sorting:**
    - sort_by: Field to sort by (created_at, amount, status)
    - sort_order: asc or desc (default: desc)

    **Authorization:**
    - Members see only their own transactions
    - Business admins see transactions for their businesses
    - Super admins see all transactions
    """
)
async def list_transactions(
    user_id: Optional[int] = Query(None),
    business_id: Optional[int] = Query(None),
    category: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    date_from: Optional[datetime] = Query(None),
    date_to: Optional[datetime] = Query(None),
    min_amount: Optional[float] = Query(None),
    max_amount: Optional[float] = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    sort_by: str = Query("created_at"),
    sort_order: str = Query("desc"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List transactions"""

    # Build filters
    filters = TransactionFilters(
        user_id=user_id,
        business_id=business_id,
        category=category,
        type=type,
        status=status,
        date_from=date_from,
        date_to=date_to,
        min_amount=min_amount,
        max_amount=max_amount,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    # Authorization: members can only see own transactions
    if current_user.role.value == "member":
        filters.user_id = current_user.id

    # Get transactions
    transactions, total = await TransactionService.get_transactions(db, filters)

    # Calculate pagination
    total_pages = math.ceil(total / per_page) if total > 0 else 0

    return TransactionList(
        transactions=transactions,
        total=total,
        page=page,
        per_page=per_page,
        total_pages=total_pages,
    )


@router.patch(
    "/{transaction_id}",
    response_model=TransactionRead,
    summary="Update transaction",
    description="""
    Update transaction details (status, description, receipt number).

    **Authorization:** Business admin or super admin
    """
)
async def update_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_business_admin)
):
    """Update transaction"""
    transaction = await TransactionService.update_transaction(db, transaction_id, transaction_data)

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transaction


@router.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cancel transaction",
    description="""
    Cancel transaction (sets status to CANCELLED).

    **Authorization:** Business admin or super admin

    **Note:** Bonuses accrued for this transaction will be reversed.
    """
)
async def cancel_transaction(
    transaction_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_business_admin)
):
    """Cancel transaction"""
    success = await TransactionService.cancel_transaction(db, transaction_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return None


# ===================================================================
# Statistics Endpoint
# ===================================================================
@router.get(
    "/stats/me",
    response_model=TransactionStats,
    summary="Get my transaction statistics",
    description="""
    Get transaction statistics for current user.

    **Includes:**
    - Total transactions, spending, bonuses earned
    - Monthly spending (last 12 months)
    - Spending by category
    - Top 3 favorite categories
    - Recent activity
    """
)
async def get_my_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get transaction statistics for current user"""
    stats = await TransactionService.get_statistics(db, current_user.id)
    return stats


@router.get(
    "/stats/{user_id}",
    response_model=TransactionStats,
    summary="Get user transaction statistics",
    description="""
    Get transaction statistics for specific user.

    **Authorization:** Super admin only
    """
)
async def get_user_stats(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_business_admin)
):
    """Get transaction statistics for user"""
    stats = await TransactionService.get_statistics(db, user_id)
    return stats
