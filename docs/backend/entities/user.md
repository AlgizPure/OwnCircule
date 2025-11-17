# User Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Authentication & User Management

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | User |
| **Database Table** | `users` |
| **Module** | Auth, Loyalty, Profile |
| **Type** | Core |
| **Frontend Components** | ProfileScreen, QRWallet, HomeScreen |
| **Primary Key** | `id` (uuid) |

### Description

User entity represents a member of the Свой Круг loyalty ecosystem. It stores authentication credentials, profile information, loyalty status, and serves as the central entity connecting transactions, bonuses, events, and referrals.

### Purpose

**Business Purpose:**
Enable member registration, track loyalty status (Insider/VIP/Elite/Inner Circle), manage bonus balances, and personalize user experience across 5 business categories.

**Technical Purpose:**
Central authentication entity, owner reference for all user-generated content, join table anchor for many-to-many relationships (events, businesses, referrals).

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE users (
  -- Primary Key
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Authentication
  phone                 VARCHAR(15) NOT NULL UNIQUE,
  phone_verified_at     TIMESTAMP WITH TIME ZONE,
  password_hash         VARCHAR(255),  -- Optional, for future web access
  
  -- Profile
  first_name            VARCHAR(100) NOT NULL,
  last_name             VARCHAR(100) NOT NULL,
  email                 VARCHAR(255) UNIQUE,
  email_verified_at     TIMESTAMP WITH TIME ZONE,
  date_of_birth         DATE,
  city                  VARCHAR(100),
  avatar_url            VARCHAR(500),
  bio                   TEXT,
  
  -- Loyalty Status
  status_tier           VARCHAR(20) DEFAULT 'Insider' 
                        CHECK (status_tier IN ('Insider', 'VIP', 'Elite', 'Inner Circle')),
  total_spent           DECIMAL(12,2) DEFAULT 0.00,
  categories_visited    SMALLINT DEFAULT 0,
  influence_weight      DECIMAL(3,1) DEFAULT 1.0,  -- Voting weight
  
  -- Gamification
  badges                JSONB DEFAULT '[]',  -- ["pioneer", "friend_of_club", "collector"]
  referral_code         VARCHAR(10) UNIQUE,
  referred_by_id        UUID REFERENCES users(id) ON DELETE SET NULL,
  
  -- Preferences
  notification_settings JSONB DEFAULT '{"push": true, "email": true, "sms": false}',
  marketing_consent     BOOLEAN DEFAULT false,
  
  -- Account Status
  is_active             BOOLEAN DEFAULT true,
  is_banned             BOOLEAN DEFAULT false,
  ban_reason            TEXT,
  
  -- Metadata
  last_login_at         TIMESTAMP WITH TIME ZONE,
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  deleted_at            TIMESTAMP WITH TIME ZONE DEFAULT NULL
);

-- Indexes
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_email ON users(email) WHERE email IS NOT NULL;
CREATE INDEX idx_users_status_tier ON users(status_tier);
CREATE INDEX idx_users_referral_code ON users(referral_code);
CREATE INDEX idx_users_referred_by ON users(referred_by_id);
CREATE INDEX idx_users_created_at ON users(created_at DESC);

-- Trigger for updated_at
CREATE TRIGGER update_users_updated_at
  BEFORE UPDATE ON users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

---

### TypeScript Type

```typescript
/**
 * User entity representing a member of Свой Круг
 */
interface User {
  // Primary Key
  id: string; // UUID
  
  // Authentication
  phone: string;
  phoneVerifiedAt?: Date;
  
  // Profile
  firstName: string;
  lastName: string;
  email?: string;
  emailVerifiedAt?: Date;
  dateOfBirth?: Date;
  city?: string;
  avatarUrl?: string;
  bio?: string;
  
  // Loyalty Status
  statusTier: 'Insider' | 'VIP' | 'Elite' | 'Inner Circle';
  totalSpent: number;
  categoriesVisited: number;
  influenceWeight: number;
  
  // Gamification
  badges: string[];
  referralCode: string;
  referredBy?: User;
  
  // Preferences
  notificationSettings: {
    push: boolean;
    email: boolean;
    sms: boolean;
  };
  marketingConsent: boolean;
  
  // Account Status
  isActive: boolean;
  isBanned: boolean;
  banReason?: string;
  
  // Metadata
  lastLoginAt?: Date;
  createdAt: Date;
  updatedAt: Date;
  deletedAt?: Date | null;
}

interface UserCreate {
  phone: string;
  firstName: string;
  lastName: string;
  email?: string;
  dateOfBirth?: Date;
  city?: string;
  referralCode?: string; // Code used to join
  marketingConsent?: boolean;
}

interface UserUpdate {
  firstName?: string;
  lastName?: string;
  email?: string;
  dateOfBirth?: Date;
  city?: string;
  avatarUrl?: string;
  bio?: string;
  notificationSettings?: {
    push?: boolean;
    email?: boolean;
    sms?: boolean;
  };
}
```

---

### Field Descriptions

| Field | Type | Required | Description | Validation |
|-------|------|----------|-------------|------------|
| `id` | UUID | Yes (auto) | Unique identifier | UUID v4 |
| `phone` | string | Yes | Mobile phone (auth) | E.164 format, unique, max 15 chars |
| `first_name` | string | Yes | First name | Min 2, max 100 chars |
| `last_name` | string | Yes | Last name | Min 2, max 100 chars |
| `email` | string | No | Email address | Valid email, unique, max 255 chars |
| `status_tier` | enum | Yes | Loyalty status | Insider/VIP/Elite/Inner Circle |
| `total_spent` | decimal | Yes | Lifetime spend (₽) | ≥ 0, precision 12,2 |
| `categories_visited` | int | Yes | Unique categories | 0-9 (9 categories total) |
| `influence_weight` | decimal | Yes | Voting multiplier | 1.0/2.0/3.0/5.0 |
| `referral_code` | string | Yes (auto) | Unique invite code | 6-10 chars, alphanumeric |
| `referred_by_id` | UUID | No | Referrer user ID | Foreign key to users |
| `is_active` | boolean | Yes | Account active | Default: true |
| `created_at` | timestamp | Yes (auto) | Registration date | ISO 8601 |

---

## 🔗 RELATIONSHIPS

### Diagram

```mermaid
erDiagram
    USER ||--o{ TRANSACTION : "makes purchases"
    USER ||--o| BONUS : "has balance"
    USER ||--o{ EVENT : "creates proposals"
    USER ||--o{ EVENT_REGISTRATION : "registers for"
    USER ||--o{ COUPON : "receives"
    USER ||--o{ NOTIFICATION : "receives"
    USER ||--o{ USER : "refers (self-join)"
    USER }o--o{ EVENT : "votes on"
```

---

### Detailed Relationships

#### Has Many: Transactions
**Type:** One-to-Many  
**Foreign Key:** `transactions.user_id`  
**Description:** All purchase transactions made by this user across all businesses

**Example Query:**
```sql
SELECT t.*, b.name as business_name
FROM transactions t
JOIN businesses b ON t.business_id = b.id
WHERE t.user_id = $1
ORDER BY t.created_at DESC
LIMIT 20;
```

**Frontend Impact:**
- TransactionHistoryScreen displays user's purchase history
- Used in: ProfileScreen, LoyaltyDashboard

---

#### Has One: Bonus Balance
**Type:** One-to-One  
**Foreign Key:** `bonuses.user_id`  
**Description:** Current bonus points balance for this user

**Example Query:**
```sql
SELECT balance, lifetime_earned, lifetime_spent
FROM bonuses
WHERE user_id = $1;
```

**Frontend Impact:**
- HomeScreen displays bonus balance
- QRWallet shows available points
- Used in: Header, HomeScreen, QRWallet

---

#### Has Many: Event Registrations
**Type:** One-to-Many  
**Foreign Key:** `event_registrations.user_id`  
**Description:** Events the user has registered for

**Example Query:**
```sql
SELECT e.*, er.status
FROM event_registrations er
JOIN events e ON er.event_id = e.id
WHERE er.user_id = $1 AND e.date >= NOW()
ORDER BY e.date ASC;
```

**Frontend Impact:**
- EventsListScreen filters "My Events"
- HomeScreen shows upcoming registered events

---

#### Self-Join: Referrals
**Type:** One-to-Many (Self-Referential)  
**Foreign Key:** `users.referred_by_id`  
**Description:** Users invited by this user through referral code

**Example Query:**
```sql
SELECT id, first_name, last_name, created_at
FROM users
WHERE referred_by_id = $1
ORDER BY created_at DESC;
```

**Frontend Impact:**
- ReferralScreen shows list of invited friends
- ProfileScreen displays "Friend of Club" badge

---

## 🌐 API ENDPOINTS

### Summary Table

| Method | Endpoint | Description | Frontend Usage | Auth Required |
|--------|----------|-------------|----------------|---------------|
| POST | `/api/v1/auth/send-code` | Send SMS OTP | PhoneInputScreen | ❌ |
| POST | `/api/v1/auth/verify-code` | Verify OTP, get JWT | OTPVerificationScreen | ❌ |
| POST | `/api/v1/auth/refresh` | Refresh access token | Background refresh | ✅ |
| GET | `/api/v1/users/me` | Get current user | ProfileScreen, Header | ✅ |
| PATCH | `/api/v1/users/me` | Update profile | EditProfileScreen | ✅ |
| GET | `/api/v1/users/me/stats` | Get user statistics | ProfileScreen | ✅ |
| GET | `/api/v1/users/me/referrals` | List referred users | ReferralScreen | ✅ |
| POST | `/api/v1/users/me/avatar` | Upload avatar | EditProfileScreen | ✅ |

**Detailed Documentation:** [Users API](../api/users-api.md)

---

### Quick Examples

#### GET /api/v1/users/me

**Request:**
```http
GET /api/v1/users/me HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
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

#### PATCH /api/v1/users/me

**Request:**
```http
PATCH /api/v1/users/me HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "firstName": "Анна",
  "email": "anna.new@example.com",
  "bio": "Любитель красоты и здоровья"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "firstName": "Анна",
    "email": "anna.new@example.com",
    "bio": "Любитель красоты и здоровья",
    "updatedAt": "2025-11-17T14:30:00Z"
  }
}
```

---

## 🔐 PERMISSIONS

### Role-Based Access Control

| Action | Member | VIP | Elite | Inner Circle | Admin |
|--------|--------|-----|-------|--------------|-------|
| **Read own** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Read others** | ⚠️ Public only | ⚠️ Public only | ⚠️ Public only | ⚠️ Public only | ✅ |
| **Update own** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Update others** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Delete own** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Delete others** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Change status** | ❌ | ❌ | ❌ | ❌ | ✅ |

### Field-Level Permissions

| Field | Member (Read) | Other Users (Read) | Admin (Read) | Notes |
|-------|---------------|-------------------|--------------|-------|
| `phone` | ✅ | ❌ | ✅ | Private |
| `email` | ✅ | ❌ | ✅ | Private |
| `firstName` | ✅ | ✅ | ✅ | Public |
| `statusTier` | ✅ | ✅ | ✅ | Public |
| `bonusBalance` | ✅ | ❌ | ✅ | Private |
| `notificationSettings` | ✅ | ❌ | ✅ | Private |

---

## ✅ VALIDATION RULES

### Creation Validation

**Required Fields:**
- `phone` - E.164 format (+79991234567)
- `firstName` - Min 2, max 100 chars, Cyrillic/Latin
- `lastName` - Min 2, max 100 chars, Cyrillic/Latin

**Optional Fields:**
- `email` - Valid email format
- `dateOfBirth` - Must be 18+ years old
- `referralCode` - Must exist in system (used during registration)

**Example:**

```python
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime

class UserCreate(BaseModel):
    phone: str = Field(..., regex=r'^\+7\d{10}$')
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr | None = None
    date_of_birth: date | None = None
    referral_code: str | None = Field(None, min_length=6, max_length=10)
    
    @validator('date_of_birth')
    def validate_age(cls, v):
        if v and (datetime.now().date() - v).days / 365 < 18:
            raise ValueError('User must be 18+ years old')
        return v
```

---

### Update Validation

All fields optional, but if provided must meet rules:

```python
class UserUpdate(BaseModel):
    first_name: str | None = Field(None, min_length=2, max_length=100)
    last_name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    bio: str | None = Field(None, max_length=500)
    notification_settings: dict | None = None
```

---

### Business Rules Validation

1. **Unique Phone:** Phone must be unique across all users
   - Check: `SELECT COUNT(*) FROM users WHERE phone = $1`
   - Error: "Phone number already registered"

2. **Unique Email:** Email must be unique if provided
   - Check: `SELECT COUNT(*) FROM users WHERE email = $1 AND id != $2`
   - Error: "Email already in use"

3. **Referral Code Exists:** If referral code provided, must be valid
   - Check: `SELECT id FROM users WHERE referral_code = $1`
   - Error: "Invalid referral code"

4. **Age Restriction:** User must be 18+ years old
   - Check: `date_of_birth + 18 years <= NOW()`
   - Error: "Must be 18 years or older"

---

## 📝 BUSINESS RULES

### Core Business Logic

1. **Status Tier Calculation (Automated)**
   - **Description:** User status automatically updated based on 12-month rolling window
   - **Applies To:** After each transaction
   - **Implementation:** Celery daily task + post-transaction hook
   - **Calculation:**
     - **Insider:** Default (1 purchase made)
     - **VIP:** ≥30,000₽ spent + ≥3 categories
     - **Elite:** ≥100,000₽ spent + ≥5 categories OR Top 1% spenders
     - **Inner Circle:** Manual promotion by admin OR ≥200,000₽ spent

2. **Influence Weight Mapping**
   - **Description:** Voting power based on status tier
   - **Applies To:** Event voting
   - **Implementation:** `influence_weight` field
   - **Values:**
     - Insider: 1.0
     - VIP: 2.0
     - Elite: 3.0
     - Inner Circle: 5.0

3. **Referral Rewards**
   - **Description:** Both referrer and referee get 1000₽ bonus on first purchase
   - **Applies To:** User registration with referral code
   - **Implementation:** Celery task triggered after first transaction
   - **Conditions:** Referee must complete first purchase within 30 days

4. **Soft Delete**
   - **Description:** Users marked as deleted, not physically removed
   - **Applies To:** Delete operations
   - **Implementation:** Set `deleted_at = NOW()`, keep record
   - **Reason:** Preserve transaction history, audit trail, GDPR compliance

---

### Cascading Behavior

**On Delete User (Soft Delete):**
- Transactions: RETAIN (set user to "Deleted User")
- Bonuses: CASCADE (mark as deleted)
- Event Registrations: CASCADE (cancel registrations)
- Coupons: RETAIN (mark user as deleted)
- Sessions: CASCADE (revoke all tokens)
- Notifications: CASCADE (clear queue)

---

### State Machine

```mermaid
stateDiagram-v2
    [*] --> Registered: Sign up
    Registered --> Active: Phone verified
    Active --> Insider: First purchase
    Insider --> VIP: ≥30k₽ + 3 categories
    VIP --> Elite: ≥100k₽ + 5 categories
    Elite --> Inner_Circle: Admin invite or ≥200k₽
    
    Active --> Banned: Violation
    Banned --> Active: Appeal accepted
    
    Active --> Deleted: User request
    Deleted --> [*]: 90 days (GDPR)
```

---

## 🧪 TESTING

### Test File Location

`tests/entities/test_user.py`

### Key Test Scenarios

#### Unit Tests

```python
def test_user_creation_with_valid_data():
    user = User(
        phone="+79991234567",
        first_name="Анна",
        last_name="Иванова"
    )
    assert user.id is not None
    assert user.status_tier == "Insider"
    assert user.influence_weight == 1.0

def test_user_phone_validation():
    with pytest.raises(ValidationError):
        User(phone="invalid", first_name="Test", last_name="User")

def test_referral_code_generation():
    user = User(phone="+79991234567", first_name="Test", last_name="User")
    assert len(user.referral_code) >= 6
    assert user.referral_code.isalnum()

def test_status_tier_upgrade():
    user = User(phone="+79991234567", first_name="Test", last_name="User")
    user.total_spent = Decimal("35000.00")
    user.categories_visited = 3
    
    updated_tier = calculate_status_tier(user)
    assert updated_tier == "VIP"
```

#### Integration Tests

```python
async def test_user_registration_api():
    response = await client.post("/api/v1/auth/register", json={
        "phone": "+79991234567",
        "firstName": "Анна",
        "lastName": "Иванова",
        "email": "anna@example.com"
    })
    assert response.status_code == 201
    assert "id" in response.json()["data"]

async def test_duplicate_phone_registration():
    # First registration
    await create_user(phone="+79991234567")
    
    # Duplicate attempt
    response = await client.post("/api/v1/auth/register", json={
        "phone": "+79991234567",
        "firstName": "Другая",
        "lastName": "Пользователь"
    })
    assert response.status_code == 409
    assert "already registered" in response.json()["error"]["message"]
```

---

## 📚 RELATED DOCUMENTATION

### Entity Documentation
- [Bonus Entity](./bonus.md) - Loyalty points
- [Transaction Entity](./transaction.md) - Purchase records
- [Event Registration Entity](./event-registration.md) - Event RSVPs

### API Documentation
- [API Overview](../api/00_API_OVERVIEW.md)
- [Auth API](../api/auth-api.md) - Authentication endpoints
- [Users API](../api/users-api.md) - User management

### Database Documentation
- [Database Schema](../database/00_DATABASE_SCHEMA.md)
- [Relationships](../database/relationships.md)

---

## 📝 CHANGELOG

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-17 | Initial documentation | Backend Team |

---

## 💡 NOTES & CONSIDERATIONS

### Performance
- Index on `phone` for auth lookups (< 10ms)
- Index on `status_tier` for filtering (< 20ms)
- Cache user profile in Redis (TTL: 5 min)

### Security
- Phone numbers hashed in logs
- PII fields encrypted at rest (AES-256)
- Rate limiting on auth endpoints (5 attempts/min)

### Future Enhancements
- [ ] Add biometric authentication (FaceID/TouchID)
- [ ] Implement 2FA for high-value accounts
- [ ] Social auth (Google, Apple Sign-In)
- [ ] Multi-language profile support

---

**Navigation:** [← Entity Catalog](00_ENTITY_CATALOG.md) | [Bonus Entity →](./bonus.md)
