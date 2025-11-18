"""
Transaction Schemas
Pydantic models for transaction API endpoints

See: docs/requirements/module-03-transactions.md
"""

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


# ===================================================================
# Request Schemas
# ===================================================================
class TransactionCreate(BaseModel):
    """
    Create transaction request

    Endpoint: POST /api/v1/transactions/
    """
    user_id: int = Field(..., description="Member ID", gt=0)
    business_id: int = Field(..., description="Business ID", gt=0)
    amount: float = Field(..., description="Transaction amount in rubles", gt=0)
    type: str = Field(
        default="purchase",
        description="Transaction type: purchase, bonus_redemption, refund, adjustment"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional transaction description"
    )
    receipt_number: Optional[str] = Field(
        None,
        max_length=100,
        description="Receipt number from POS system"
    )
    external_id: Optional[str] = Field(
        None,
        max_length=255,
        description="ID from external CRM system"
    )

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: float) -> float:
        """Validate amount is positive"""
        if v <= 0:
            raise ValueError('Amount must be greater than 0')
        if v > 1_000_000:
            raise ValueError('Amount cannot exceed 1,000,000₽')
        return round(v, 2)

    @field_validator('type')
    @classmethod
    def validate_type(cls, v: str) -> str:
        """Validate transaction type"""
        allowed_types = ['purchase', 'bonus_redemption', 'refund', 'adjustment']
        if v not in allowed_types:
            raise ValueError(f'Type must be one of: {", ".join(allowed_types)}')
        return v


class TransactionUpdate(BaseModel):
    """
    Update transaction request

    Endpoint: PATCH /api/v1/transactions/{id}
    """
    status: Optional[str] = Field(
        None,
        description="Transaction status: pending, completed, cancelled, failed"
    )
    description: Optional[str] = Field(None, max_length=500)
    receipt_number: Optional[str] = Field(None, max_length=100)

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        """Validate transaction status"""
        if v is None:
            return v
        allowed_statuses = ['pending', 'completed', 'cancelled', 'failed']
        if v not in allowed_statuses:
            raise ValueError(f'Status must be one of: {", ".join(allowed_statuses)}')
        return v


# ===================================================================
# Response Schemas
# ===================================================================
class TransactionRead(BaseModel):
    """
    Transaction response schema

    Returned by:
    - GET /api/v1/transactions/{id}
    - POST /api/v1/transactions/
    """
    id: int
    user_id: int
    business_id: int
    amount: float
    bonus_amount: float
    bonus_redeemed: float
    type: str
    status: str
    category: Optional[str]
    description: Optional[str]
    receipt_number: Optional[str]
    external_id: Optional[str]
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime]
    cancelled_at: Optional[datetime]

    # Computed fields (from joins)
    business_name: Optional[str] = None
    user_name: Optional[str] = None

    class Config:
        from_attributes = True


class TransactionList(BaseModel):
    """
    Paginated transaction list response

    Returned by: GET /api/v1/transactions/
    """
    transactions: list[TransactionRead]
    total: int
    page: int
    per_page: int
    total_pages: int


# ===================================================================
# Statistics Schemas
# ===================================================================
class SpendingByCategory(BaseModel):
    """Spending statistics by category"""
    category: str
    total_amount: float
    transaction_count: int
    percentage: float  # Percentage of total spending


class MonthlySpending(BaseModel):
    """Monthly spending statistics"""
    month: str  # Format: "2025-11"
    total_amount: float
    transaction_count: int
    average_transaction: float


class TransactionStats(BaseModel):
    """
    Transaction statistics response

    Returned by: GET /api/v1/transactions/stats
    """
    # Overall stats
    total_transactions: int
    total_spending: float
    total_bonuses_earned: float
    average_transaction: float

    # By period
    monthly_spending: list[MonthlySpending]

    # By category
    spending_by_category: list[SpendingByCategory]
    top_categories: list[str]  # Top 3 categories by spending

    # Recent activity
    last_transaction_date: Optional[datetime]
    transactions_this_month: int
    spending_this_month: float


# ===================================================================
# Filter Schemas
# ===================================================================
class TransactionFilters(BaseModel):
    """
    Query parameters for filtering transactions

    Used in: GET /api/v1/transactions/
    """
    user_id: Optional[int] = Field(None, description="Filter by user ID")
    business_id: Optional[int] = Field(None, description="Filter by business ID")
    category: Optional[str] = Field(None, description="Filter by category")
    type: Optional[str] = Field(None, description="Filter by transaction type")
    status: Optional[str] = Field(None, description="Filter by status")
    date_from: Optional[datetime] = Field(None, description="Filter by date (start)")
    date_to: Optional[datetime] = Field(None, description="Filter by date (end)")
    min_amount: Optional[float] = Field(None, description="Minimum transaction amount", ge=0)
    max_amount: Optional[float] = Field(None, description="Maximum transaction amount", ge=0)

    # Pagination
    page: int = Field(1, description="Page number", ge=1)
    per_page: int = Field(20, description="Items per page", ge=1, le=100)

    # Sorting
    sort_by: str = Field("created_at", description="Sort field: created_at, amount, status")
    sort_order: str = Field("desc", description="Sort order: asc, desc")
