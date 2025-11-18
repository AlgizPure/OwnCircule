"""
Database Configuration and Session Management
PostgreSQL with SQLAlchemy async
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

from app.core.config import settings

# Create async engine
engine = create_async_engine(
    str(settings.DATABASE_URL),
    echo=settings.DEBUG,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
)

# Create async session factory
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Base class for models
class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models"""
    pass


# Dependency for FastAPI routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides async database session
    
    Usage in FastAPI routes:
    ```python
    @app.get("/users")
    async def get_users(db: AsyncSession = Depends(get_db)):
        ...
    ```
    """
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
