"""
Authentication Dependencies
JWT middleware for protecting routes

Usage:
    from app.core.auth import get_current_user

    @router.get("/protected")
    async def protected_route(current_user: User = Depends(get_current_user)):
        return {"user_id": current_user.id}

See: docs/adr/ADR-004-jwt-authentication.md
"""

from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.security import verify_access_token
from app.models.user import User


# Bearer token authentication scheme
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """
    Get current authenticated user from JWT token

    Args:
        credentials: HTTP Authorization header with Bearer token
        db: Database session

    Returns:
        Current User instance

    Raises:
        HTTPException: 401 if token invalid or user not found

    Usage:
        @router.get("/profile")
        async def get_profile(user: User = Depends(get_current_user)):
            return {"user_id": user.id}
    """

    # Extract token from Authorization header
    token = credentials.credentials

    # Validate token and extract payload
    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Extract user ID from token payload
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get user from database
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Check user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Get current active user (alias for get_current_user)

    Usage:
        @router.get("/profile")
        async def get_profile(user: User = Depends(get_current_active_user)):
            return {"user_id": user.id}
    """
    return current_user


def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False)),
    db: AsyncSession = Depends(get_db)
) -> Optional[User]:
    """
    Get current user (optional - returns None if no token)

    Used for endpoints that work for both authenticated and anonymous users.

    Args:
        credentials: Optional HTTP Authorization header
        db: Database session

    Returns:
        User instance if authenticated, None otherwise

    Usage:
        @router.get("/content")
        async def get_content(user: Optional[User] = Depends(get_current_user_optional)):
            if user:
                # Personalized content for authenticated user
                return {"message": f"Hello, {user.first_name}!"}
            else:
                # Generic content for anonymous user
                return {"message": "Hello, guest!"}
    """

    if not credentials:
        return None

    try:
        token = credentials.credentials
        payload = verify_access_token(token)

        if not payload:
            return None

        user_id = payload.get("sub")
        if not user_id:
            return None

        result = db.execute(select(User).where(User.id == int(user_id)))
        user = result.scalar_one_or_none()

        if not user or not user.is_active:
            return None

        return user

    except Exception:
        return None


# ===================================================================
# Role-Based Access Control (RBAC) Dependencies
# ===================================================================
def require_role(allowed_roles: list[str]):
    """
    Dependency factory for role-based access control

    Args:
        allowed_roles: List of allowed roles (e.g., ["member", "business_admin", "super_admin"])

    Returns:
        Dependency function

    Usage:
        @router.post("/admin/users")
        async def admin_endpoint(
            user: User = Depends(require_role(["super_admin"]))
        ):
            return {"message": "Admin access granted"}
    """

    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        """Check if user has required role"""
        if current_user.role.value not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required role: {', '.join(allowed_roles)}"
            )
        return current_user

    return role_checker


def require_super_admin(current_user: User = Depends(get_current_user)) -> User:
    """
    Require super admin role

    Usage:
        @router.delete("/admin/users/{user_id}")
        async def delete_user(
            user_id: int,
            admin: User = Depends(require_super_admin)
        ):
            # Only super admins can access this
            ...
    """
    if current_user.role.value != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super admin access required"
        )
    return current_user


def require_business_admin(current_user: User = Depends(get_current_user)) -> User:
    """
    Require business admin or super admin role

    Usage:
        @router.patch("/businesses/{business_id}")
        async def update_business(
            business_id: int,
            admin: User = Depends(require_business_admin)
        ):
            # Business admins and super admins can access this
            ...
    """
    allowed_roles = ["business_admin", "super_admin"]
    if current_user.role.value not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Business admin access required"
        )
    return current_user
