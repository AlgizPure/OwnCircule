# Businesses API

**Base URL:** `/api/v1/businesses`  
**Version:** 1.0  
**Auth Required:** Yes

---

## GET /businesses

**Purpose:** List all partner businesses

**Query Params:**
- `category`: `beauty` | `cosmetology` | `dental` | `medical` | `gastronomy`
- `city`: `Екатеринбург`
- `search`: Text search
- `page`: 1
- `limit`: 20

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "name": "Skinerica",
      "category": "cosmetology",
      "description": "Центр косметологии",
      "logoUrl": "/logos/skinerica.png",
      "cashbackPercent": 7.0,
      "address": "ул. Ленина 5",
      "city": "Екатеринбург",
      "phone": "+73432345678",
      "coordinates": {
        "lat": 56.838,
        "lon": 60.605
      },
      "rating": 4.8,
      "reviewsCount": 124
    }
  ],
  "pagination": {
    "page": 1,
    "total": 5
  }
}
```

---

## GET /businesses/:id

**Purpose:** Get business details

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "Skinerica",
    "category": "cosmetology",
    "description": "Центр косметологии полного цикла",
    "logoUrl": "/logos/skinerica.png",
    "cashbackPercent": 7.0,
    "acceptsBonusPayment": true,
    "address": "ул. Ленина 5",
    "phone": "+73432345678",
    "email": "info@skinerica.ru",
    "website": "https://skinerica.ru",
    "workingHours": {
      "mon-fri": "09:00-21:00",
      "sat": "10:00-18:00",
      "sun": "Closed"
    },
    "services": [
      "Чистка лица",
      "Массаж",
      "Инъекции"
    ],
    "currentOffers": 3
  }
}
```

---

## GET /businesses/:id/offers

**Purpose:** Get active offers from business

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "title": "Скидка 20% на чистку лица",
      "description": "Для новых клиентов",
      "discountType": "percent",
      "discountValue": 20.0,
      "minPurchaseAmount": 3000.00,
      "expiresAt": "2025-12-31T23:59:59Z"
    }
  ]
}
```

---

**Navigation:** [← Events API](./events-api.md) | [Services Catalog →](../services/00_SERVICES_CATALOG.md)
