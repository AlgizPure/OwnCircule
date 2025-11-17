"""
User Pydantic Schemas
Request/Response models for User API
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator
import re

from app.models.user import UserRole, StatusTier


class UserBase(BaseModel):
    """Base User schema with common fields"""
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    """Schema for creating a new user (registration)"""
    phone: str = Field(..., pattern=r'^\+7\d{10}$', description="Phone in format +7XXXXXXXXXX")
    password: str = Field(..., min_length=8, max_length=128)
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password strength"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        return v


class UserUpdate(BaseModel):
    """Schema for updating user profile"""
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None


class UserInDB(UserBase):
    """User schema as stored in database"""
    id: int
    phone: str
    role: UserRole
    status_tier: StatusTier
    total_spend: float
    bonus_balance: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserRead(UserInDB):
    """User schema for API responses (excludes sensitive data)"""
    pass


class UserList(BaseModel):
    """Paginated list of users"""
    users: list[UserRead]
    total: int
    page: int
    page_size: int
