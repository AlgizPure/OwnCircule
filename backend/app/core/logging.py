"""
Logging Configuration
JSON structured logging for production, human-readable for development
"""

import logging
import sys
from pythonjsonlogger import jsonlogger

from app.core.config import settings


def setup_logging():
    """
    Configure application logging
    - Development: Human-readable console logging
    - Production: JSON structured logging for log aggregation
    """
    
    # Root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO if not settings.DEBUG else logging.DEBUG)
    
    # Remove existing handlers
    logger.handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    
    if settings.ENVIRONMENT == "production":
        # JSON formatter for production
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(name)s %(levelname)s %(message)s',
            rename_fields={'asctime': 'timestamp', 'levelname': 'level'}
        )
    else:
        # Human-readable formatter for development
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Silence noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    
    logger.info(f"Logging configured for {settings.ENVIRONMENT} environment")
