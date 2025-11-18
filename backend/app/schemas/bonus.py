"""
Bonus Schemas
Pydantic models for bonus API endpoints

See: docs/requirements/module-02-loyalty-system.md
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


# ===================================================================
# Request Schemas
# ===================================================================
class BonusRedeemRequest(BaseModel):
    """
    Redeem bonuses request

    Endpoint: POST /api/v1/bonuses/redeem
    """
    amount: float = Field(..., description="Bonus amount to redeem", gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "amount": 500.0
            }
        }


# ===================================================================
# Response Schemas
# ===================================================================
class BonusRead(BaseModel):
    """
    Bonus response schema

    Returned by:
    - GET /api/v1/bonuses/
    - POST /api/v1/bonuses/redeem
    """
    id: int
    user_id: int
    transaction_id: Optional[int]
    amount: float
    type: str
    status: str
    expires_at: Optional[datetime]
    description: Optional[str]
    multiplier: float
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True


class BonusHistoryResponse(BaseModel):
    """
    Bonus history response

    Returned by: GET /api/v1/bonuses/
    """
    bonuses: list[BonusRead]
    total: int
    page: int
    per_page: int


class BonusBalanceResponse(BaseModel):
    """
    Bonus balance response

    Returned by: GET /api/v1/bonuses/balance
    """
    balance: float
    currency: str = "₽"

    class Config:
        json_schema_extra = {
            "example": {
                "balance": 1250.50,
                "currency": "₽"
            }
        }


class BonusRedeemResponse(BaseModel):
    """
    Bonus redemption response

    Returned by: POST /api/v1/bonuses/redeem
    """
    bonus: BonusRead
    new_balance: float
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "bonus": {
                    "id": 123,
                    "user_id": 1,
                    "amount": -500.0,
                    "type": "redemption"
                },
                "new_balance": 750.50,
                "message": "Бонусы успешно списаны"
            }
        }
