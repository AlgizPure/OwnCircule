"""
Business Model
See: docs/backend/entities/business.md
"""

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Business(Base):
    """
    Business Entity - Partner Businesses
    
    Represents partner businesses in the Svoy Krug ecosystem.
    Each business can have CRM integrations, offer bonuses, and host events.
    
    Initial Partners (MVP):
    1. Skinerica - Beauty salon
    2. Лисичкино - Gastromarket  
    3. Стим Центр - SPA center
    4. Миндаль - Beauty salon
    5. Миллениум - Multibrand store
    
    See full spec: docs/backend/entities/business.md
    """
    
    __tablename__ = "businesses"
    
    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    # Business Info
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(200), unique=True, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    
    # Category
    category: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    # Categories: beauty, gastro, spa, fashion, wellness
    
    # Contact
    phone: Mapped[str | None] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(255))
    website: Mapped[str | None] = mapped_column(String(500))
    
    # Address
    address: Mapped[str | None] = mapped_column(String(500))
    city: Mapped[str] = mapped_column(String(100), default="Москва", nullable=False)
    coordinates: Mapped[dict | None] = mapped_column(JSON)  # {"lat": 55.7558, "lon": 37.6173}
    
    # Bonus Configuration
    bonus_percentage: Mapped[float] = mapped_column(default=5.0, nullable=False)  # 5-10% default
    accepts_bonus_redemption: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # CRM Integration
    crm_type: Mapped[str | None] = mapped_column(String(50))  # "yclients", "iiko", "rkeeper", null
    crm_credentials: Mapped[dict | None] = mapped_column(JSON)  # Encrypted CRM API credentials
    
    # Media
    logo_url: Mapped[str | None] = mapped_column(String(500))
    cover_image_url: Mapped[str | None] = mapped_column(String(500))
    gallery_urls: Mapped[list | None] = mapped_column(JSON)  # Array of image URLs
    
    # Flags
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    
    def __repr__(self) -> str:
        return f"<Business(id={self.id}, name={self.name}, category={self.category})>"
