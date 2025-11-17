# API Overview - Свой Круг

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Base URL:** `https://api.svoykrug.ru/api/v1`  
**Protocol:** HTTPS (TLS 1.3)

---

## 🎯 API DESIGN PRINCIPLES

### REST Architecture
- Resource-based URLs (`/users`, `/events`, `/transactions`)
- Standard HTTP methods (GET, POST, PATCH, DELETE)
- Stateless authentication (JWT Bearer tokens)
- JSON request/response bodies

### Versioning
- URL-based versioning (`/api/v1`)
- Deprecation warnings in headers
- Minimum 6-month support for deprecated versions

### Response Format

**Success Response:**
```json
{
  "success": true,
  "data": { /* payload */ },
  "meta": {
    "timestamp": "2025-11-17T10:30:00Z",
    "requestId": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "email": ["Invalid email format"]
    }
  },
  "meta": {
    "timestamp": "2025-11-17T10:30:00Z",
    "requestId": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

---

## 🔐 AUTHENTICATION

### JWT Bearer Tokens

**Access Token (15 min):**
```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Token Structure:**
```json
{
  "sub": "user-uuid",
  "role": "member",
  "status": "vip",
  "exp": 1700000000,
  "iat": 1699999000,
  "type": "access"
}
```

**Refresh Flow:**
```http
POST /api/v1/auth/refresh
Content-Type: application/json

{
  "refreshToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 📚 ENDPOINT GROUPS

### Authentication (Public)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/send-code` | Send SMS OTP |
| POST | `/auth/verify-code` | Verify OTP, get JWT |
| POST | `/auth/refresh` | Refresh access token |

**Detailed:** [Auth API](./auth-api.md)

---

### Users (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/me` | Get current user |
| PATCH | `/users/me` | Update profile |
| POST | `/users/me/avatar` | Upload avatar |
| GET | `/users/me/stats` | User statistics |
| GET | `/users/me/referrals` | Referred users |
| DELETE | `/users/me` | Delete account |

**Detailed:** [Users API](./users-api.md)

---

### Loyalty (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/loyalty/balance` | Bonus balance |
| GET | `/loyalty/history` | Bonus transactions |
| GET | `/loyalty/status` | Status tier info |
| GET | `/loyalty/progress` | Progress to next tier |

**Detailed:** [Loyalty API](./loyalty-api.md)

---

### Transactions (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/transactions` | Create transaction |
| GET | `/transactions` | List user transactions |
| GET | `/transactions/:id` | Get transaction |

---

### Events (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/events` | List events |
| POST | `/events` | Create event proposal |
| GET | `/events/:id` | Get event details |
| POST | `/events/:id/register` | Register for event |
| POST | `/events/:id/vote` | Vote on proposal |

**Detailed:** [Events API](./events-api.md)

---

### Businesses (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/businesses` | List businesses |
| GET | `/businesses/:id` | Get business |
| GET | `/businesses/:id/offers` | Business offers |

**Detailed:** [Businesses API](./businesses-api.md)

---

### Coupons (Authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/coupons` | List user coupons |
| POST | `/coupons/:id/activate` | Activate coupon |
| POST | `/coupons/:id/redeem` | Redeem coupon |

---

## 📊 PAGINATION

**Query Parameters:**
```
GET /api/v1/transactions?page=1&limit=20&sortBy=created_at&sortOrder=desc
```

**Response with Pagination:**
```json
{
  "success": true,
  "data": [ /* items */ ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 156,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  }
}
```

---

## ⚠️ ERROR CODES

| HTTP Status | Code | Description |
|-------------|------|-------------|
| 400 | `VALIDATION_ERROR` | Invalid input data |
| 401 | `UNAUTHORIZED` | Missing or invalid token |
| 403 | `FORBIDDEN` | Insufficient permissions |
| 404 | `NOT_FOUND` | Resource not found |
| 409 | `CONFLICT` | Duplicate resource |
| 422 | `BUSINESS_RULE_VIOLATION` | Business logic error |
| 429 | `RATE_LIMIT_EXCEEDED` | Too many requests |
| 500 | `INTERNAL_SERVER_ERROR` | Server error |

---

## 🚀 RATE LIMITING

| Endpoint Group | Limit | Window |
|----------------|-------|--------|
| **Auth** | 5 requests | 1 minute |
| **Public** | 60 requests | 1 minute |
| **Authenticated** | 1000 requests | 1 hour |
| **Business** | 5000 requests | 1 hour |

**Headers:**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1699635600
```

---

## 📝 API CONVENTIONS

### Date/Time Format
- ISO 8601: `2025-11-17T10:30:00Z`
- Timezone: UTC

### Currency
- Always in Russian Rubles (₽)
- Decimal format: `12345.67`

### Phone Numbers
- E.164 format: `+79991234567`

### UUIDs
- Version 4: `550e8400-e29b-41d4-a716-446655440000`

---

## 🔗 RELATED DOCUMENTATION

- [Auth API](./auth-api.md)
- [Users API](./users-api.md)
- [Loyalty API](./loyalty-api.md)
- [Events API](./events-api.md)
- [Businesses API](./businesses-api.md)
- [Backend Overview](../00_BACKEND_OVERVIEW.md)

---

**Last Updated:** 2025-11-17  
**Interactive Docs:** https://api.svoykrug.ru/docs
