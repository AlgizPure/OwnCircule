"""
Transaction Service
Business logic for transaction management

See: docs/requirements/module-03-transactions.md
"""

import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from sqlalchemy import select, func, and_, or_, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.transaction import Transaction, TransactionType, TransactionStatus
from app.models.user import User
from app.models.business import Business
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionFilters,
    TransactionStats,
    MonthlySpending,
    SpendingByCategory
)


logger = logging.getLogger(__name__)


class TransactionService:
    """Service layer for transaction operations"""

    @staticmethod
    async def create_transaction(
        db: AsyncSession,
        transaction_data: TransactionCreate
    ) -> Transaction:
        """
        Create a new transaction

        Args:
            db: Database session
            transaction_data: Transaction creation data

        Returns:
            Created transaction instance

        Raises:
            ValueError: If user or business doesn't exist

        Flow:
            1. Validate user and business exist
            2. Get business category for analytics
            3. Create transaction with status=PENDING
            4. Trigger bonus accrual (Celery task in Sprint 2 Task 2)
        """

        # Validate user exists
        result = await db.execute(select(User).where(User.id == transaction_data.user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise ValueError(f"User with ID {transaction_data.user_id} not found")

        if not user.is_active:
            raise ValueError(f"User {transaction_data.user_id} is inactive")

        # Validate business exists
        result = await db.execute(select(Business).where(Business.id == transaction_data.business_id))
        business = result.scalar_one_or_none()
        if not business:
            raise ValueError(f"Business with ID {transaction_data.business_id} not found")

        if not business.is_active:
            raise ValueError(f"Business {transaction_data.business_id} is inactive")

        # Create transaction
        db_transaction = Transaction(
            user_id=transaction_data.user_id,
            business_id=transaction_data.business_id,
            amount=transaction_data.amount,
            type=TransactionType(transaction_data.type),
            status=TransactionStatus.PENDING,
            category=business.category,  # Denormalize for analytics
            description=transaction_data.description,
            receipt_number=transaction_data.receipt_number,
            external_id=transaction_data.external_id,
        )

        db.add(db_transaction)
        await db.commit()
        await db.refresh(db_transaction)

        logger.info(
            f"Transaction created: ID={db_transaction.id}, "
            f"User={transaction_data.user_id}, Amount={transaction_data.amount}₽"
        )

        # TODO: Trigger bonus accrual (Celery task in Sprint 2 Task 2)
        # from app.tasks import accrue_bonus
        # accrue_bonus.delay(db_transaction.id)

        return db_transaction

    @staticmethod
    async def get_by_id(db: AsyncSession, transaction_id: int) -> Optional[Transaction]:
        """Get transaction by ID"""
        result = await db.execute(select(Transaction).where(Transaction.id == transaction_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_transaction(
        db: AsyncSession,
        transaction_id: int,
        transaction_data: TransactionUpdate
    ) -> Optional[Transaction]:
        """
        Update transaction

        Args:
            db: Database session
            transaction_id: Transaction ID
            transaction_data: Updated transaction data

        Returns:
            Updated transaction or None if not found
        """
        transaction = await TransactionService.get_by_id(db, transaction_id)
        if not transaction:
            return None

        # Update fields
        update_data = transaction_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if field == 'status' and value:
                # Update status and timestamp
                transaction.status = TransactionStatus(value)
                if value == 'completed' and not transaction.completed_at:
                    transaction.completed_at = datetime.utcnow()
                elif value == 'cancelled' and not transaction.cancelled_at:
                    transaction.cancelled_at = datetime.utcnow()
            else:
                setattr(transaction, field, value)

        await db.commit()
        await db.refresh(transaction)

        logger.info(f"Transaction updated: ID={transaction_id}")
        return transaction

    @staticmethod
    async def get_transactions(
        db: AsyncSession,
        filters: TransactionFilters
    ) -> tuple[list[Transaction], int]:
        """
        Get paginated and filtered transactions

        Args:
            db: Database session
            filters: Filter parameters

        Returns:
            Tuple of (transactions list, total count)
        """

        # Build query
        query = select(Transaction)

        # Apply filters
        conditions = []

        if filters.user_id:
            conditions.append(Transaction.user_id == filters.user_id)

        if filters.business_id:
            conditions.append(Transaction.business_id == filters.business_id)

        if filters.category:
            conditions.append(Transaction.category == filters.category)

        if filters.type:
            conditions.append(Transaction.type == filters.type)

        if filters.status:
            conditions.append(Transaction.status == filters.status)

        if filters.date_from:
            conditions.append(Transaction.created_at >= filters.date_from)

        if filters.date_to:
            conditions.append(Transaction.created_at <= filters.date_to)

        if filters.min_amount:
            conditions.append(Transaction.amount >= filters.min_amount)

        if filters.max_amount:
            conditions.append(Transaction.amount <= filters.max_amount)

        if conditions:
            query = query.where(and_(*conditions))

        # Get total count
        count_query = select(func.count()).select_from(Transaction)
        if conditions:
            count_query = count_query.where(and_(*conditions))
        result = await db.execute(count_query)
        total = result.scalar()

        # Apply sorting
        sort_column = getattr(Transaction, filters.sort_by, Transaction.created_at)
        if filters.sort_order == 'asc':
            query = query.order_by(asc(sort_column))
        else:
            query = query.order_by(desc(sort_column))

        # Apply pagination
        offset = (filters.page - 1) * filters.per_page
        query = query.offset(offset).limit(filters.per_page)

        # Execute query
        result = await db.execute(query)
        transactions = result.scalars().all()

        return transactions, total

    @staticmethod
    async def get_statistics(
        db: AsyncSession,
        user_id: int
    ) -> TransactionStats:
        """
        Get transaction statistics for user

        Args:
            db: Database session
            user_id: User ID

        Returns:
            Transaction statistics
        """

        # Overall stats
        result = await db.execute(
            select(
                func.count(Transaction.id).label('total_transactions'),
                func.sum(Transaction.amount).label('total_spending'),
                func.sum(Transaction.bonus_amount).label('total_bonuses'),
                func.avg(Transaction.amount).label('average_transaction'),
                func.max(Transaction.created_at).label('last_transaction_date'),
            )
            .where(
                and_(
                    Transaction.user_id == user_id,
                    Transaction.status == TransactionStatus.COMPLETED
                )
            )
        )
        overall = result.one()

        # Monthly spending (last 12 months)
        monthly_result = await db.execute(
            select(
                func.to_char(Transaction.created_at, 'YYYY-MM').label('month'),
                func.sum(Transaction.amount).label('total_amount'),
                func.count(Transaction.id).label('transaction_count'),
                func.avg(Transaction.amount).label('average_transaction'),
            )
            .where(
                and_(
                    Transaction.user_id == user_id,
                    Transaction.status == TransactionStatus.COMPLETED,
                    Transaction.created_at >= datetime.utcnow() - timedelta(days=365)
                )
            )
            .group_by('month')
            .order_by(desc('month'))
        )
        monthly_data = monthly_result.all()

        monthly_spending = [
            MonthlySpending(
                month=row.month,
                total_amount=float(row.total_amount or 0),
                transaction_count=row.transaction_count,
                average_transaction=float(row.average_transaction or 0)
            )
            for row in monthly_data
        ]

        # Spending by category
        category_result = await db.execute(
            select(
                Transaction.category,
                func.sum(Transaction.amount).label('total_amount'),
                func.count(Transaction.id).label('transaction_count'),
            )
            .where(
                and_(
                    Transaction.user_id == user_id,
                    Transaction.status == TransactionStatus.COMPLETED,
                    Transaction.category.isnot(None)
                )
            )
            .group_by(Transaction.category)
            .order_by(desc('total_amount'))
        )
        category_data = category_result.all()

        total_spending = float(overall.total_spending or 0)
        spending_by_category = [
            SpendingByCategory(
                category=row.category,
                total_amount=float(row.total_amount),
                transaction_count=row.transaction_count,
                percentage=round((float(row.total_amount) / total_spending * 100), 2) if total_spending > 0 else 0
            )
            for row in category_data
        ]

        top_categories = [cat.category for cat in spending_by_category[:3]]

        # This month stats
        month_start = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_result = await db.execute(
            select(
                func.count(Transaction.id).label('transactions_this_month'),
                func.sum(Transaction.amount).label('spending_this_month'),
            )
            .where(
                and_(
                    Transaction.user_id == user_id,
                    Transaction.status == TransactionStatus.COMPLETED,
                    Transaction.created_at >= month_start
                )
            )
        )
        month_data = month_result.one()

        return TransactionStats(
            total_transactions=overall.total_transactions or 0,
            total_spending=float(overall.total_spending or 0),
            total_bonuses_earned=float(overall.total_bonuses or 0),
            average_transaction=float(overall.average_transaction or 0),
            monthly_spending=monthly_spending,
            spending_by_category=spending_by_category,
            top_categories=top_categories,
            last_transaction_date=overall.last_transaction_date,
            transactions_this_month=month_data.transactions_this_month or 0,
            spending_this_month=float(month_data.spending_this_month or 0),
        )

    @staticmethod
    async def cancel_transaction(db: AsyncSession, transaction_id: int) -> bool:
        """
        Cancel transaction (soft delete)

        Args:
            db: Database session
            transaction_id: Transaction ID

        Returns:
            True if cancelled, False if not found
        """
        transaction = await TransactionService.get_by_id(db, transaction_id)
        if not transaction:
            return False

        transaction.status = TransactionStatus.CANCELLED
        transaction.cancelled_at = datetime.utcnow()

        await db.commit()

        logger.info(f"Transaction cancelled: ID={transaction_id}")

        # TODO: Reverse bonus accrual if transaction had bonuses
        return True
