"""
FastAPI Main Application Entry Point
Svoy Krug - Premium Women's Loyalty Ecosystem
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1 import api_router

# Setup logging
setup_logging()

# Initialize FastAPI app
app = FastAPI(
    title="Svoy Krug API",
    description="Premium Women's Loyalty Ecosystem Backend",
    version="1.0.0",
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
    default_response_class=ORJSONResponse,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for load balancers and monitoring
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0"
    }


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint
    """
    return {
        "message": "Svoy Krug API",
        "version": "1.0.0",
        "docs": "/api/docs" if settings.DEBUG else "Documentation disabled in production"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info"
    )
