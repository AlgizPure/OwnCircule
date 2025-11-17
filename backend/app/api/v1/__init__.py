"""
API v1 Router
Aggregates all API endpoints
"""

from fastapi import APIRouter

# Import module routers
from app.modules.users.routes import router as users_router

# Create main API router
api_router = APIRouter()

# Include module routers
api_router.include_router(users_router, prefix="/users", tags=["Users"])

# Health check endpoint
@api_router.get("/ping", tags=["System"])
async def ping():
    """Ping endpoint for testing API connectivity"""
    return {"message": "pong", "status": "ok"}
