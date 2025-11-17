# Users API

**Base URL:** `/api/v1/users`  
**Version:** 1.0  
**Auth Required:** Yes

---

## GET /users/me

**Purpose:** Get current user profile

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "phone": "+79991234567",
    "firstName": "Анна",
    "lastName": "Иванова",
    "email": "anna@example.com",
    "statusTier": "VIP",
    "totalSpent": 45000.00,
    "categoriesVisited": 4,
    "influenceWeight": 2.0,
    "badges": ["pioneer", "friend_of_club"],
    "referralCode": "ANNA2024",
    "createdAt": "2025-01-15T10:00:00Z"
  }
}
```

---

## PATCH /users/me

**Purpose:** Update user profile

**Request:**
```json
{
  "firstName": "Анна",
  "email": "anna.new@example.com",
  "bio": "Любитель красоты и здоровья",
  "notificationSettings": {
    "push": true,
    "email": true,
    "sms": false
  }
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "firstName": "Анна",
    "email": "anna.new@example.com",
    "updatedAt": "2025-11-17T14:30:00Z"
  }
}
```

---

## GET /users/me/stats

**Purpose:** Get user statistics

**Response (200):**
```json
{
  "success": true,
  "data": {
    "totalTransactions": 23,
    "totalSpent": 45000.00,
    "categoriesVisited": 4,
    "eventsAttended": 5,
    "referralsCount": 3,
    "bonusBalance": 2500.00
  }
}
```

---

## GET /users/me/referrals

**Purpose:** List users referred by current user

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "firstName": "Мария",
      "lastName": "Петрова",
      "statusTier": "Insider",
      "joinedAt": "2025-10-01T10:00:00Z",
      "firstPurchaseCompleted": true
    }
  ]
}
```

---

**Navigation:** [← Auth API](./auth-api.md) | [Loyalty API →](./loyalty-api.md)
