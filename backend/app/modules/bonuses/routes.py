"""
Bonus API Endpoints
Get balance, history, redeem bonuses

See: docs/requirements/module-02-loyalty-system.md
"""

import logging
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.schemas.bonus import (
    BonusRead,
    BonusHistoryResponse,
    BonusBalanceResponse,
    BonusRedeemRequest,
    BonusRedeemResponse,
)
from app.services.bonus_service import BonusService


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/bonuses",
    tags=["Bonuses"]
)


# ===================================================================
# Bonus Endpoints
# ===================================================================
@router.get(
    "/balance",
    response_model=BonusBalanceResponse,
    summary="Get bonus balance",
    description="""
    Get current user's bonus balance.

    **Authorization:** Authenticated user

    **Returns:** Current bonus balance in rubles
    """
)
async def get_bonus_balance(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current bonus balance"""
    try:
        balance = await BonusService.get_balance(db, current_user.id)
        return BonusBalanceResponse(balance=balance)

    except Exception as e:
        logger.exception(f"Error getting bonus balance: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка получения баланса бонусов"
        )


@router.get(
    "/",
    response_model=BonusHistoryResponse,
    summary="Get bonus history",
    description="""
    Get user's bonus accrual and redemption history.

    **Authorization:** Authenticated user

    **Pagination:**
    - page: Page number (default: 1)
    - per_page: Items per page (default: 50, max: 100)

    **Returns:** List of bonus records (accruals, redemptions, expiries)
    """
)
async def get_bonus_history(
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get bonus history"""
    try:
        offset = (page - 1) * per_page
        bonuses, total = await BonusService.get_bonus_history(
            db,
            current_user.id,
            limit=per_page,
            offset=offset
        )

        return BonusHistoryResponse(
            bonuses=bonuses,
            total=total,
            page=page,
            per_page=per_page
        )

    except Exception as e:
        logger.exception(f"Error getting bonus history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка получения истории бонусов"
        )


@router.post(
    "/redeem",
    response_model=BonusRedeemResponse,
    summary="Redeem bonuses",
    description="""
    Redeem bonus points (pay with bonuses).

    **Authorization:** Authenticated user

    **Validation:**
    - User must have sufficient balance
    - Amount must be > 0

    **Flow:**
    1. Validate sufficient balance
    2. Create redemption record (negative amount)
    3. Deduct from user balance
    4. Return new balance

    **Note:** This endpoint deducts bonuses from balance.
    To use bonuses for payment, create a transaction with type=bonus_redemption.
    """
)
async def redeem_bonuses(
    request: BonusRedeemRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Redeem bonuses"""
    try:
        bonus = await BonusService.redeem_bonus(
            db,
            current_user.id,
            request.amount
        )

        # Get new balance
        new_balance = await BonusService.get_balance(db, current_user.id)

        return BonusRedeemResponse(
            bonus=bonus,
            new_balance=new_balance,
            message=f"Списано {request.amount}₽ бонусов. Новый баланс: {new_balance}₽"
        )

    except ValueError as e:
        logger.warning(f"Bonus redemption failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Bonus redemption error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка списания бонусов"
        )


# ===================================================================
# Admin Endpoints (for testing/manual operations)
# ===================================================================
@router.post(
    "/accrue/{transaction_id}",
    response_model=BonusRead,
    summary="Accrue bonus for transaction (Admin)",
    description="""
    Manually trigger bonus accrual for a transaction.

    **Authorization:** Business admin or super admin

    **Note:** In production, this is called automatically by Celery task.
    This endpoint is for testing/manual operations only.
    """
)
async def accrue_bonus_manual(
    transaction_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Manually accrue bonus for transaction"""
    try:
        bonus = await BonusService.accrue_bonus(db, transaction_id)

        if not bonus:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction not found or not eligible for bonus"
            )

        return bonus

    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Bonus accrual error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка начисления бонуса"
        )
