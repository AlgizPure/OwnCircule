# Свой Круг - System Architecture

**Created:** 2025-11-17
**Version:** 1.0
**Status:** Active

---

## 🏗️ High-Level Architecture

Свой Круг uses a **mobile-first, API-driven architecture** with a modular monolith backend and React Native frontend. The system is designed for rapid MVP development while maintaining clear boundaries for future microservices extraction if needed.

```
┌─────────────────────────────────────────────────────────────┐
│                    MOBILE CLIENTS                           │
│  ┌─────────────────────┐    ┌─────────────────────┐        │
│  │   iOS App           │    │   Android App       │        │
│  │ (React Native 0.81) │    │ (React Native 0.81) │        │
│  └─────────────────────┘    └─────────────────────┘        │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTPS/TLS 1.3
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   API GATEWAY / LOAD BALANCER               │
│                  (Yandex Application Load Balancer)         │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Auth Service │  │ Loyalty Core │  │ CRM Connector│     │
│  │  (JWT, SMS)  │  │ (Bonus/Status)│  │  (Adapters)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Transaction  │  │ Event Manager│  │ Analytics    │     │
│  │  Service     │  │              │  │ Service      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATA LAYER                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ PostgreSQL   │  │ ClickHouse   │  │ Redis        │     │
│  │ (Primary DB) │  │ (Analytics)  │  │ (Cache/Queue)│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │Elasticsearch │  │ Object Store │                        │
│  │  (Search)    │  │  (S3/Yandex) │                        │
│  └──────────────┘  └──────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                       ▲
                       │
┌──────────────────────┴──────────────────────────────────────┐
│              EXTERNAL INTEGRATIONS                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  YCLIENTS    │  │     Iiko     │  │     1С       │     │
│  │  (REST API)  │  │  (REST API)  │  │  (REST API)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   AMO CRM    │  │ МИС Renovatio│  │  ЮKassa      │     │
│  │  (REST API)  │  │  (REST API)  │  │  (Payments)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧱 Backend Architecture

### Modular Monolith Design

The backend is organized as a **modular monolith** with clear domain boundaries:

```
backend/
├── app/
│   ├── api/                    # API routes (FastAPI routers)
│   │   ├── v1/
│   │   │   ├── auth.py         # Authentication endpoints
│   │   │   ├── users.py        # User management
│   │   │   ├── loyalty.py      # Bonuses, status
│   │   │   ├── transactions.py # Transaction tracking
│   │   │   ├── events.py       # Event Hub
│   │   │   ├── businesses.py   # Business catalog
│   │   │   └── admin.py        # Admin endpoints
│   ├── core/                   # Core business logic
│   │   ├── loyalty/            # Bonus & status calculations
│   │   ├── cross_promo/        # Cross-promotion engine
│   │   ├── analytics/          # RFM, churn prediction
│   │   └── notifications/      # Push, SMS, Email
│   ├── integrations/           # External CRM connectors
│   │   ├── yclients/
│   │   ├── iiko/
│   │   ├── amo_crm/
│   │   ├── renovatio/
│   │   └── base_adapter.py     # Abstract connector
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── transaction.py
│   │   ├── bonus.py
│   │   ├── business.py
│   │   └── event.py
│   ├── schemas/                # Pydantic validation schemas
│   ├── services/               # Business logic layer
│   ├── tasks/                  # Celery async tasks
│   └── utils/                  # Shared utilities
└── main.py                     # FastAPI app entry point
```

### API Design Patterns

**RESTful Endpoints:**
- `POST /api/v1/auth/send-code` - Send SMS OTP
- `POST /api/v1/auth/verify-code` - Verify OTP, get JWT
- `GET /api/v1/users/me` - Get current user profile
- `GET /api/v1/loyalty/balance` - Get bonus balance
- `POST /api/v1/transactions/scan` - Scan QR code to process transaction
- `GET /api/v1/events` - List events with filters
- `POST /api/v1/events/{id}/register` - Register for event

**Authentication Flow:**
1. User enters phone number → `POST /auth/send-code`
2. Backend generates 6-digit code, sends via SMS.ru
3. User enters code → `POST /auth/verify-code`
4. Backend validates code, returns JWT access + refresh tokens
5. All subsequent requests include `Authorization: Bearer <access_token>`

**Response Format:**
```json
{
  "success": true,
  "data": { /* payload */ },
  "meta": {
    "timestamp": "2025-11-17T10:30:00Z",
    "request_id": "uuid-here"
  }
}
```

---

## 🗃️ Database Schema Overview

### PostgreSQL (Primary OLTP Database)

**Core Tables:**

```sql
-- Users
users (
  id UUID PRIMARY KEY,
  phone VARCHAR(15) UNIQUE NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(255),
  status_tier VARCHAR(20) DEFAULT 'Insider',
  total_spent DECIMAL(10,2) DEFAULT 0,
  categories_visited INT DEFAULT 0,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

-- Transactions
transactions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  business_id UUID REFERENCES businesses(id),
  amount DECIMAL(10,2) NOT NULL,
  bonus_accrued DECIMAL(10,2),
  bonus_redeemed DECIMAL(10,2),
  transaction_type VARCHAR(20), -- 'purchase' | 'refund'
  external_id VARCHAR(255),     -- CRM system transaction ID
  created_at TIMESTAMP
)

-- Bonuses
bonuses (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  balance DECIMAL(10,2) DEFAULT 0,
  lifetime_earned DECIMAL(10,2) DEFAULT 0,
  lifetime_spent DECIMAL(10,2) DEFAULT 0,
  updated_at TIMESTAMP
)

-- Businesses
businesses (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(50),          -- 'beauty' | 'wellness' | 'gastronomy' | 'health'
  crm_type VARCHAR(50),          -- 'yclients' | 'iiko' | '1c' | 'amo_crm'
  crm_credentials JSON,          -- Encrypted API keys
  cashback_percent DECIMAL(5,2), -- Base cashback rate
  created_at TIMESTAMP
)

-- Events
events (
  id UUID PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  date TIMESTAMP,
  location VARCHAR(255),
  max_participants INT,
  min_status_tier VARCHAR(20),  -- 'Insider' | 'VIP' | 'Elite'
  created_by UUID REFERENCES users(id),
  status VARCHAR(20),            -- 'proposed' | 'approved' | 'active' | 'completed'
  created_at TIMESTAMP
)

-- Coupons
coupons (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  business_id UUID REFERENCES businesses(id),
  discount_type VARCHAR(20),     -- 'percent' | 'fixed' | 'bonus'
  discount_value DECIMAL(10,2),
  expires_at TIMESTAMP,
  redeemed_at TIMESTAMP NULL,
  source_chain_id UUID           -- Cross-promo chain that generated this
)
```

**Indexes:**
- `idx_transactions_user_created` on (user_id, created_at DESC)
- `idx_transactions_business` on (business_id)
- `idx_coupons_user_expires` on (user_id, expires_at) WHERE redeemed_at IS NULL

### ClickHouse (Analytics OLAP Database)

**Fact Tables:**

```sql
-- Transaction facts (immutable, append-only)
transaction_facts (
  transaction_id UUID,
  user_id UUID,
  business_id UUID,
  amount Decimal64(2),
  bonus_accrued Decimal64(2),
  category String,
  timestamp DateTime
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (user_id, timestamp)

-- User RFM snapshots (daily aggregation)
rfm_snapshots (
  snapshot_date Date,
  user_id UUID,
  recency_days Int32,
  frequency_count Int32,
  monetary_value Decimal64(2),
  rfm_segment String,           -- '111' to '555'
  churn_risk_score Float32      -- 0.0 to 1.0
) ENGINE = ReplacingMergeTree(snapshot_date)
ORDER BY (user_id, snapshot_date)
```

### Redis (Cache & Queue)

**Key Patterns:**
- `session:{user_id}` - JWT session data (TTL: 30 days)
- `bonus:balance:{user_id}` - Cached bonus balance (TTL: 5 min)
- `qr:code:{code}` - QR code metadata (TTL: 5 min)
- `rate_limit:auth:{phone}` - Rate limiting for auth (TTL: 1 min)
- `celery:*` - Celery task queue

---

## 📱 Mobile App Architecture

### State Management (Redux Toolkit)

```
src/
├── store/
│   ├── slices/
│   │   ├── authSlice.ts        # User auth state
│   │   ├── userSlice.ts        # Profile, status, bonuses
│   │   ├── transactionSlice.ts # Transaction history
│   │   ├── eventSlice.ts       # Event Hub state
│   │   └── businessSlice.ts    # Business catalog
│   ├── api/                    # RTK Query API definitions
│   │   ├── authApi.ts
│   │   ├── loyaltyApi.ts
│   │   └── eventsApi.ts
│   └── store.ts                # Redux store config
```

**Global State:**
- `auth`: { isAuthenticated, accessToken, refreshToken }
- `user`: { id, phone, firstName, statusTier, bonusBalance }
- `transactions`: { items: [], pagination, filters }
- `events`: { upcoming: [], registered: [], past: [] }

### Navigation Structure

```
Root Navigator (Stack)
├── Auth Flow (if not authenticated)
│   ├── PhoneInput
│   ├── OTPVerification
│   └── Onboarding (welcome video + profile setup)
└── Main Flow (if authenticated)
    └── Tab Navigator
        ├── Home Tab (Stack)
        │   ├── HomeScreen (status card, quick actions)
        │   └── QRScannerScreen
        ├── Events Tab (Stack)
        │   ├── EventsListScreen
        │   ├── EventDetailsScreen
        │   └── EventConstructorScreen (VIP/Elite only)
        ├── Businesses Tab (Stack)
        │   ├── BusinessCatalogScreen
        │   └── BusinessDetailsScreen
        └── Profile Tab (Stack)
            ├── ProfileScreen
            ├── TransactionHistoryScreen
            ├── ReferralScreen
            └── SettingsScreen
```

---

## 🔄 Integration Architecture

### CRM Adapter Pattern

All CRM integrations implement a common `BaseCRMAdapter` interface:

```python
class BaseCRMAdapter(ABC):
    @abstractmethod
    async def fetch_transactions(
        self, 
        since: datetime, 
        until: datetime
    ) -> List[Transaction]:
        """Fetch transactions from CRM within date range."""
        pass
    
    @abstractmethod
    async def get_customer_by_phone(
        self, 
        phone: str
    ) -> Optional[Customer]:
        """Find customer in CRM by phone number."""
        pass
    
    @abstractmethod
    async def apply_bonus(
        self, 
        customer_id: str, 
        amount: Decimal
    ) -> bool:
        """Apply bonus to customer account in CRM."""
        pass
```

**Implemented Adapters:**
- `YCLIENTSAdapter` - REST API for Миндаль salon
- `IikoAdapter` - REST API for Лисичкино gastromarket
- `OneCAdapter` - REST API for Skinerica, Лисичкино
- `AMOCRMAdapter` - REST API for Стим Центр
- `RenovatioAdapter` - REST API for Миллениум medical center

**Sync Strategy:**
- Celery Beat runs sync tasks every 5 minutes
- Fetch new transactions since last sync timestamp
- Match by phone number, create/update user records
- Calculate bonuses, update balances
- Store transaction history in PostgreSQL + ClickHouse

---

## 🔐 Security Architecture

### Data Protection Layers

1. **Transport Layer:** TLS 1.3 for all API traffic
2. **Authentication:** JWT (RS256) with 15-min access tokens
3. **Authorization:** Role-based access control (RBAC)
   - User roles: `member`, `vip`, `elite`, `inner_circle`
   - Business roles: `owner`, `staff`, `viewer`
   - Admin roles: `superadmin`, `moderator`
4. **Data Encryption:** 
   - At-rest: PostgreSQL transparent data encryption
   - In-transit: TLS 1.3
   - Sensitive fields: AES-256 for CRM credentials
5. **Medical Data Isolation:** 
   - Transactions from medical businesses (Миллениум, Стим Центр) flagged with `is_medical=true`
   - Medical transactions excluded from cross-business analytics (врачебная тайна compliance)

---

## 📊 Monitoring & Observability

**Metrics Collection:**
- Prometheus scrapes `/metrics` endpoint every 15s
- Custom metrics: bonus_accrued_total, cross_promo_triggered_total, qr_scans_total

**Logging:**
- Structured JSON logs (FastAPI + python-json-logger)
- Loki aggregation with Grafana visualization
- Log levels: DEBUG (dev), INFO (staging), WARN+ (production)

**Alerting:**
- PagerDuty integration for critical alerts
- Alerts: API error rate >1%, p95 latency >500ms, database connection failures

---

## 🔄 Related Documentation

- [Tech Stack](./03_TECH_STACK.md) - Technology choices and versions
- [PRD](./01_PRD.md) - Product requirements
- [Module Requirements](../requirements/) - Detailed module specifications

---

**Last Updated:** 2025-11-17
**Owner:** Engineering Team
**Status:** Approved for Development
