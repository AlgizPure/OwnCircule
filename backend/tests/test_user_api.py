"""
User API Tests
Tests for user CRUD endpoints
"""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
class TestUserAPI:
    """Test suite for User API endpoints"""
    
    async def test_create_user_success(self, client: AsyncClient):
        """Test successful user creation"""
        response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "+79991234567",
                "password": "SecurePass123",
                "first_name": "Анна",
                "last_name": "Иванова",
                "email": "anna.ivanova@example.com"
            }
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["phone"] == "+79991234567"
        assert data["first_name"] == "Анна"
        assert data["last_name"] == "Иванова"
        assert data["email"] == "anna.ivanova@example.com"
        assert data["status_tier"] == "insider"
        assert data["bonus_balance"] == 0
        assert "password" not in data
        assert "password_hash" not in data
    
    async def test_create_user_duplicate_phone(self, client: AsyncClient):
        """Test user creation with duplicate phone"""
        user_data = {
            "phone": "+79991234567",
            "password": "SecurePass123",
            "first_name": "Анна",
            "last_name": "Иванова"
        }
        
        # Create first user
        response1 = await client.post("/api/v1/users/", json=user_data)
        assert response1.status_code == 201
        
        # Try to create duplicate
        response2 = await client.post("/api/v1/users/", json=user_data)
        assert response2.status_code == 400
        assert "already exists" in response2.json()["detail"]
    
    async def test_create_user_invalid_phone(self, client: AsyncClient):
        """Test user creation with invalid phone format"""
        response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "89991234567",  # Should start with +7
                "password": "SecurePass123",
                "first_name": "Анна",
                "last_name": "Иванова"
            }
        )
        
        assert response.status_code == 422  # Validation error
    
    async def test_create_user_weak_password(self, client: AsyncClient):
        """Test user creation with weak password"""
        response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "+79991234567",
                "password": "weak",  # Too short, no uppercase, no digit
                "first_name": "Анна",
                "last_name": "Иванова"
            }
        )
        
        assert response.status_code == 422  # Validation error
    
    async def test_get_user_by_id(self, client: AsyncClient):
        """Test getting user by ID"""
        # Create user first
        create_response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "+79991234567",
                "password": "SecurePass123",
                "first_name": "Анна",
                "last_name": "Иванова"
            }
        )
        user_id = create_response.json()["id"]
        
        # Get user by ID
        response = await client.get(f"/api/v1/users/{user_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id
        assert data["phone"] == "+79991234567"
    
    async def test_get_user_not_found(self, client: AsyncClient):
        """Test getting non-existent user"""
        response = await client.get("/api/v1/users/999999")
        
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
    
    async def test_update_user(self, client: AsyncClient):
        """Test updating user profile"""
        # Create user first
        create_response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "+79991234567",
                "password": "SecurePass123",
                "first_name": "Анна",
                "last_name": "Иванова"
            }
        )
        user_id = create_response.json()["id"]
        
        # Update user
        response = await client.patch(
            f"/api/v1/users/{user_id}",
            json={
                "first_name": "Мария",
                "email": "maria@example.com"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["first_name"] == "Мария"
        assert data["last_name"] == "Иванова"  # Unchanged
        assert data["email"] == "maria@example.com"
    
    async def test_delete_user(self, client: AsyncClient):
        """Test user soft delete"""
        # Create user first
        create_response = await client.post(
            "/api/v1/users/",
            json={
                "phone": "+79991234567",
                "password": "SecurePass123",
                "first_name": "Анна",
                "last_name": "Иванова"
            }
        )
        user_id = create_response.json()["id"]
        
        # Delete user
        response = await client.delete(f"/api/v1/users/{user_id}")
        
        assert response.status_code == 204
        
        # Verify user is deactivated (still exists but is_active=False)
        get_response = await client.get(f"/api/v1/users/{user_id}")
        assert get_response.status_code == 200
        assert get_response.json()["is_active"] is False
    
    async def test_get_users_list(self, client: AsyncClient):
        """Test getting paginated users list"""
        # Create multiple users
        for i in range(3):
            await client.post(
                "/api/v1/users/",
                json={
                    "phone": f"+7999123456{i}",
                    "password": "SecurePass123",
                    "first_name": f"User{i}",
                    "last_name": "Test"
                }
            )
        
        # Get users list
        response = await client.get("/api/v1/users/?skip=0&limit=10")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["users"]) == 3
        assert data["total"] == 3
        assert data["page"] == 1
        assert data["page_size"] == 10
    
    async def test_ping_endpoint(self, client: AsyncClient):
        """Test API ping endpoint"""
        response = await client.get("/api/v1/ping")
        
        assert response.status_code == 200
        assert response.json() == {"message": "pong", "status": "ok"}
