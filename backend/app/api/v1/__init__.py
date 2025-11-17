"""
API v1 Router
Aggregates all API endpoints
"""

from fastapi import APIRouter

# Import module routers (will be created in Sprint 1)
# from app.modules.auth.routes import router as auth_router
# from app.modules.users.routes import router as users_router

# Create main API router
api_router = APIRouter()

# Include module routers
# api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users_router, prefix="/users", tags=["Users"])

# Placeholder health endpoint
@api_router.get("/ping", tags=["System"])
async def ping():
    """Ping endpoint for testing"""
    return {"message": "pong"}
