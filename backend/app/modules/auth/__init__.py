"""
Auth Module
Authentication endpoints (register, login, refresh, logout)
"""

from app.modules.auth.routes import router

__all__ = ["router"]
