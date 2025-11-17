# Authentication API

**Base URL:** `/api/v1/auth`  
**Version:** 1.0  
**Last Updated:** 2025-11-17

---

## POST /auth/send-code

**Purpose:** Send SMS OTP code to user's phone

**Request:**
```json
{
  "phone": "+79991234567"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "codeId": "uuid",
    "expiresIn": 300
  }
}
```

**Errors:**
- 400: Invalid phone format
- 429: Too many attempts (5/minute limit)

---

## POST /auth/verify-code

**Purpose:** Verify OTP code and receive JWT tokens

**Request:**
```json
{
  "codeId": "uuid",
  "code": "123456"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGci...",
    "refreshToken": "eyJhbGci...",
    "expiresIn": 900,
    "user": {
      "id": "uuid",
      "phone": "+79991234567",
      "firstName": "Анна",
      "statusTier": "VIP"
    }
  }
}
```

**Errors:**
- 400: Invalid or expired code
- 404: Code ID not found

---

## POST /auth/refresh

**Purpose:** Refresh access token using refresh token

**Request:**
```json
{
  "refreshToken": "eyJhbGci..."
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGci...",
    "expiresIn": 900
  }
}
```

**Errors:**
- 401: Invalid or expired refresh token

---

**Navigation:** [← API Overview](./00_API_OVERVIEW.md) | [Users API →](./users-api.md)
