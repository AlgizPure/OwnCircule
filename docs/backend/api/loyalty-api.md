# Loyalty API

**Base URL:** `/api/v1/loyalty`  
**Version:** 1.0  
**Auth Required:** Yes

---

## GET /loyalty/balance

**Purpose:** Get user's bonus points balance

**Response (200):**
```json
{
  "success": true,
  "data": {
    "balance": 2500.00,
    "pendingBalance": 150.00,
    "lifetimeEarned": 15000.00,
    "lifetimeSpent": 12500.00,
    "expiresAt": "2026-01-15T00:00:00Z",
    "expiringAmount": 300.00
  }
}
```

---

## GET /loyalty/history

**Purpose:** Get bonus transaction history

**Query Params:**
- `type`: `earned` | `spent` | `expired`
- `page`: 1
- `limit`: 20

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "type": "earned",
      "amount": 250.00,
      "description": "Покупка в Skinerica",
      "business": {
        "id": "uuid",
        "name": "Skinerica"
      },
      "createdAt": "2025-11-10T14:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 45,
    "totalPages": 3
  }
}
```

---

## GET /loyalty/status

**Purpose:** Get current status tier information

**Response (200):**
```json
{
  "success": true,
  "data": {
    "currentTier": "VIP",
    "cashbackPercent": 7.0,
    "influenceWeight": 2.0,
    "privileges": [
      "Кешбэк 7%",
      "Предложение мероприятий",
      "Усиленное голосование (2x)"
    ],
    "progress": {
      "nextTier": "Elite",
      "spentRequired": 55000.00,
      "spentProgress": 45000.00,
      "categoriesRequired": 5,
      "categoriesProgress": 4,
      "percentComplete": 75
    }
  }
}
```

---

**Navigation:** [← Users API](./users-api.md) | [Events API →](./events-api.md)
