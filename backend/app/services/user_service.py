"""
User Service - Business Logic Layer
CRUD operations for User entity
"""

from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from app.models.user import User, StatusTier
from app.schemas.user import UserCreate, UserUpdate


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """Service layer for User operations"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt"""
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
        """
        Create a new user
        
        Args:
            db: Database session
            user_data: User creation data
            
        Returns:
            Created user instance
            
        Raises:
            ValueError: If phone already exists
        """
        # Check if phone already exists
        existing = await UserService.get_by_phone(db, user_data.phone)
        if existing:
            raise ValueError(f"User with phone {user_data.phone} already exists")
        
        # Create user
        db_user = User(
            phone=user_data.phone,
            password_hash=UserService.hash_password(user_data.password),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            status_tier=StatusTier.INSIDER,  # Default tier
            total_spend=0.0,
            bonus_balance=0,
            is_active=True,
            is_verified=False,
        )
        
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        
        return db_user
    
    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        """Get user by ID"""
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_by_phone(db: AsyncSession, phone: str) -> Optional[User]:
        """Get user by phone number"""
        result = await db.execute(select(User).where(User.phone == phone))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> Optional[User]:
        """Get user by email"""
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update_user(
        db: AsyncSession,
        user_id: int,
        user_data: UserUpdate
    ) -> Optional[User]:
        """
        Update user profile
        
        Args:
            db: Database session
            user_id: User ID to update
            user_data: Updated user data
            
        Returns:
            Updated user or None if not found
        """
        user = await UserService.get_by_id(db, user_id)
        if not user:
            return None
        
        # Update fields
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        await db.commit()
        await db.refresh(user)
        
        return user
    
    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> bool:
        """
        Soft delete user (set is_active=False)
        
        Args:
            db: Database session
            user_id: User ID to delete
            
        Returns:
            True if deleted, False if not found
        """
        user = await UserService.get_by_id(db, user_id)
        if not user:
            return False
        
        user.is_active = False
        await db.commit()
        
        return True
    
    @staticmethod
    async def get_users(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100
    ) -> list[User]:
        """
        Get paginated list of users
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of users
        """
        result = await db.execute(
            select(User)
            .where(User.is_active == True)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
