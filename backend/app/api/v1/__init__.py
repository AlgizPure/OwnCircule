"""
API v1 Router
Aggregates all API endpoints
"""

from fastapi import APIRouter

# Import module routers
from app.modules.users.routes import router as users_router
from app.modules.auth.routes import router as auth_router
from app.modules.transactions.routes import router as transactions_router
from app.modules.bonuses.routes import router as bonuses_router

# Create main API router
api_router = APIRouter()

# Include module routers
api_router.include_router(auth_router)  # Auth endpoints (no /auth prefix - already in router)
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(transactions_router, prefix="/transactions", tags=["Transactions"])
api_router.include_router(bonuses_router, prefix="/bonuses", tags=["Bonuses"])

# Health check endpoint
@api_router.get("/ping", tags=["System"])
async def ping():
    """Ping endpoint for testing API connectivity"""
    return {"message": "pong", "status": "ok"}
