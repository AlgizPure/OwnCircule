"""
Application Configuration
Loads environment variables and provides centralized settings
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Environment
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    DEBUG: bool = Field(default=True, env="DEBUG")
    
    # Database (PostgreSQL)
    DATABASE_URL: PostgresDsn = Field(
        default="postgresql+asyncpg://postgres:postgres_dev_password@localhost:5432/owncircle_dev",
        env="DATABASE_URL"
    )
    DATABASE_POOL_SIZE: int = Field(default=20, env="DATABASE_POOL_SIZE")
    DATABASE_MAX_OVERFLOW: int = Field(default=0, env="DATABASE_MAX_OVERFLOW")
    
    # Redis
    REDIS_URL: RedisDsn = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    REDIS_CACHE_TTL: int = Field(default=300, env="REDIS_CACHE_TTL")
    
    # ClickHouse (Analytics)
    CLICKHOUSE_HOST: str = Field(default="localhost", env="CLICKHOUSE_HOST")
    CLICKHOUSE_PORT: int = Field(default=9000, env="CLICKHOUSE_PORT")
    CLICKHOUSE_USER: str = Field(default="clickhouse", env="CLICKHOUSE_USER")
    CLICKHOUSE_PASSWORD: str = Field(default="clickhouse_dev_password", env="CLICKHOUSE_PASSWORD")
    CLICKHOUSE_DATABASE: str = Field(default="analytics", env="CLICKHOUSE_DATABASE")
    
    # JWT Authentication
    JWT_SECRET_KEY: str = Field(default="dev-secret-change-in-production", env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field(default="RS256", env="JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=15, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, env="JWT_REFRESH_TOKEN_EXPIRE_DAYS")
    
    # SMS Gateway
    SMS_RU_API_KEY: str = Field(default="", env="SMS_RU_API_KEY")
    SMS_OTP_EXPIRE_MINUTES: int = Field(default=5, env="SMS_OTP_EXPIRE_MINUTES")
    
    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:19000", "http://localhost:19006"],
        env="CORS_ORIGINS"
    )
    
    # Security
    AES_ENCRYPTION_KEY: str = Field(default="dev-aes-key-change-in-production", env="AES_ENCRYPTION_KEY")
    PASSWORD_HASH_ROUNDS: int = Field(default=12, env="PASSWORD_HASH_ROUNDS")
    
    # Yandex Cloud (Production)
    YANDEX_CLOUD_ACCESS_KEY: str = Field(default="", env="YANDEX_CLOUD_ACCESS_KEY")
    YANDEX_CLOUD_SECRET_KEY: str = Field(default="", env="YANDEX_CLOUD_SECRET_KEY")
    YANDEX_CLOUD_BUCKET: str = Field(default="owncircle-media", env="YANDEX_CLOUD_BUCKET")
    
    # Sentry (Error Tracking)
    SENTRY_DSN: str = Field(default="", env="SENTRY_DSN")
    
    # Celery
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/1", env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/2", env="CELERY_RESULT_BACKEND")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()
