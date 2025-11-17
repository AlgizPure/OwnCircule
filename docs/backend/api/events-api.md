# Events API

**Base URL:** `/api/v1/events`  
**Version:** 1.0  
**Auth Required:** Yes

---

## GET /events

**Purpose:** List events with filters

**Query Params:**
- `status`: `upcoming` | `completed` | `proposals`
- `type`: `open` | `paid` | `elite_only`
- `registered`: `true` | `false`
- `page`: 1
- `limit`: 20

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "title": "Мастер-класс по макияжу",
      "description": "Дневной макияж от профессионала",
      "date": "2025-12-10T18:00:00Z",
      "location": "Skinerica, ул. Ленина 5",
      "maxParticipants": 20,
      "currentParticipants": 15,
      "minStatusTier": "Insider",
      "eventType": "open",
      "coverImageUrl": "/events/makeup-masterclass.jpg",
      "isRegistered": false
    }
  ],
  "pagination": {
    "page": 1,
    "total": 12
  }
}
```

---

## POST /events

**Purpose:** Create event proposal (VIP+)

**Request:**
```json
{
  "title": "Дегустация вина",
  "description": "Знакомство с винами Италии",
  "date": "2025-12-20T19:00:00Z",
  "location": "Лисичкино",
  "maxParticipants": 15,
  "minStatusTier": "VIP",
  "eventType": "paid",
  "price": 2000.00
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "Дегустация вина",
    "status": "proposed",
    "votingEndsAt": "2025-11-24T23:59:59Z",
    "createdAt": "2025-11-17T15:00:00Z"
  }
}
```

---

## POST /events/:id/register

**Purpose:** Register for event

**Request:**
```json
{
  "plusOne": false,
  "dietaryRestrictions": "Вегетарианка"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "registrationId": "uuid",
    "status": "registered",
    "qrCode": "https://api.svoykrug.ru/qr/event-checkin/uuid"
  }
}
```

---

## POST /events/:id/vote

**Purpose:** Vote on event proposal

**Request:**
```json
{
  "vote": "yes"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "voteWeight": 2.0,
    "currentResults": {
      "votesFor": 15,
      "votesAgainst": 3,
      "approvalPercentage": 83.3
    }
  }
}
```

---

**Navigation:** [← Loyalty API](./loyalty-api.md) | [Businesses API →](./businesses-api.md)
