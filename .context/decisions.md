# Architectural & Technical Decisions - Свой Круг

**Last Updated:** 2025-11-17

---

## 🏗️ Architecture Decisions

### AD-001: Modular Monolith vs Microservices
**Decision:** Use modular monolith for MVP
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- New project with small initial team (3-5 developers)
- Need rapid MVP development (12 weeks)
- Microservices add complexity (networking, distributed tracing, deployment)

**Decision:**
Implement modular monolith with FastAPI, clear domain boundaries (loyalty, events, analytics, etc.), but single deployable application.

**Rationale:**
- Faster development (no inter-service communication overhead)
- Easier debugging and testing
- Lower infrastructure costs
- Can extract microservices later if needed (clear module boundaries)

**Consequences:**
- ✅ Faster time-to-market
- ✅ Simpler deployment
- ⚠️ May need refactoring to microservices at scale (>10K users)

---

### AD-002: Mobile Platform - React Native vs Native
**Decision:** React Native 0.81 for cross-platform
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- Need iOS + Android apps
- Limited mobile development resources (1-2 developers)
- Premium UX requirements (smooth animations, native feel)

**Decision:**
Use React Native 0.81 with TypeScript 5.7 for cross-platform development.

**Rationale:**
- 80%+ code reuse between iOS and Android
- Large ecosystem (React Navigation, Redux Toolkit, Lottie animations)
- Can drop to native code for performance-critical features (QR scanning via react-native-vision-camera)
- Russian market has good React Native adoption

**Consequences:**
- ✅ Faster development, single codebase
- ✅ Lower hiring costs (React devs vs iOS+Android)
- ⚠️ Performance slightly worse than native (but acceptable for our use case)

---

### AD-003: Database Strategy - PostgreSQL + ClickHouse
**Decision:** PostgreSQL (OLTP) + ClickHouse (OLAP)
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- Need transactional database for bonuses, transactions, users
- Need fast analytics for RFM segmentation, Win-Win matrix
- Single database struggles with both OLTP and OLAP workloads

**Decision:**
- PostgreSQL 16.11 for primary OLTP (transactions, users, bonuses)
- ClickHouse 25.8 LTS for analytics (aggregations, time-series, dashboards)
- Hourly sync: PostgreSQL → ClickHouse via Celery

**Rationale:**
- PostgreSQL: ACID compliance, mature, excellent for transactional workloads
- ClickHouse: 100x faster for analytics queries (columnar storage)
- Industry standard pattern (Uber, Cloudflare use similar setup)

**Consequences:**
- ✅ Fast analytics without slowing down transactions
- ✅ Can scale OLTP and OLAP independently
- ⚠️ Data sync lag (up to 1 hour for analytics)
- ⚠️ Additional infrastructure complexity

---

### AD-004: Authentication - JWT vs Session-based
**Decision:** JWT (RS256) with access + refresh tokens
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- Mobile app needs stateless authentication
- Need to support biometric login (FaceID/TouchID)
- Security requirement: short-lived tokens

**Decision:**
- Access tokens: 15 minutes (RS256 signed)
- Refresh tokens: 30 days (stored in database, one-time use with rotation)
- Biometric login stores refresh token in iOS Keychain / Android Keystore

**Rationale:**
- Stateless (no server-side sessions for every request)
- Mobile-friendly (store refresh token securely, renew access token)
- Industry best practice for mobile APIs

**Consequences:**
- ✅ Scalable (no session storage)
- ✅ Secure (short-lived access tokens)
- ⚠️ Need refresh token rotation logic
- ⚠️ Token blacklist required for logout

---

### AD-005: Cloud Provider - Yandex Cloud (Primary)
**Decision:** Yandex Cloud with VK Cloud as backup
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- 152-ФЗ requires data storage in Russian Federation
- Need reliable cloud provider with low latency in Moscow
- Budget constraints (AWS/GCP expensive for Russian market)

**Decision:**
- Primary: Yandex Cloud (ru-central1 region)
- Backup: VK Cloud (for failover)

**Rationale:**
- 152-ФЗ compliant (data never leaves RF)
- Yandex Cloud mature (Object Storage, Managed PostgreSQL, Compute Cloud)
- Ruble billing (no currency conversion risk)
- Low latency for Moscow users

**Consequences:**
- ✅ 152-ФЗ compliant
- ✅ Cost-effective
- ⚠️ Less mature than AWS/GCP (fewer managed services)
- ⚠️ Vendor lock-in to Russian cloud

---

## 🔐 Security Decisions

### SD-001: Encryption at Rest - AES-256
**Decision:** Encrypt sensitive fields with AES-256 (Fernet)
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- Store phone numbers, emails, birthdates (PII under 152-ФЗ)
- Need compliance with Russian data protection laws
- Database breaches common threat

**Decision:**
Encrypt sensitive columns (phone, email, birthdate) with AES-256 using Python `cryptography` library. Keys stored in Yandex KMS with monthly rotation.

**Rationale:**
- 152-ФЗ compliance (encryption at rest recommended)
- Industry standard (AES-256 = bank-level encryption)
- Key rotation mitigates long-term key exposure

**Consequences:**
- ✅ Data breach protection
- ⚠️ Performance overhead (decrypt on read)
- ⚠️ Cannot search encrypted fields without hashing

---

### SD-002: Medical Data - врачебная тайна Compliance
**Decision:** Flag + isolate medical transactions
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- 2 of 5 initial partners are medical (Миллениум, Стим Центр)
- врачебная тайна (medical confidentiality) is Russian law
- Cannot share medical transaction data across businesses

**Decision:**
- Flag medical businesses: `is_medical=TRUE`
- Flag medical transactions: `is_medical=TRUE`
- Exclude medical transactions from:
  - Cross-promo triggers
  - Win-Win analytics
  - Ecosystem-wide dashboards (unless aggregated/anonymized)

**Rationale:**
- Legal compliance (врачебная тайна violations = serious penalties)
- Patient privacy protection

**Consequences:**
- ✅ Compliant with medical confidentiality laws
- ⚠️ Medical businesses get less cross-promo opportunities
- ⚠️ Need separate analytics pipeline for medical data

---

## 💻 Technology Decisions

### TD-001: Python Version - 3.13 (Latest Stable)
**Decision:** Python 3.13 for backend
**Date:** 2025-11-17 (PHASE 3 Tech Verification)
**Status:** ✅ Approved

**Original Plan:** Python 3.11+
**Updated To:** Python 3.13 (latest stable as of Nov 2025)

**Rationale:**
- Performance improvements over 3.11 (15-20% faster)
- Better async/await improvements
- Long-term support (3.13 released Oct 2024)

**Migration Effort:** 2 days for compatibility testing

---

### TD-002: FastAPI Version - 0.121.2 (Latest)
**Decision:** FastAPI 0.121.2
**Date:** 2025-11-17 (PHASE 3 Tech Verification)
**Status:** ✅ Approved, CRITICAL UPDATE

**Original Plan:** FastAPI 0.104+
**Updated To:** FastAPI 0.121.2 (latest stable as of Nov 2025)

**Rationale:**
- Security patches (0.104 → 0.121.2 includes fixes)
- New features (improved WebSocket support, better OpenAPI docs)
- Community recommendation (0.104 is 1+ year old by Nov 2025)

**Migration Effort:** 1 day for breaking changes review

---

### TD-003: Redis Version - 8.2 (Major Upgrade)
**Decision:** Redis 8.2
**Date:** 2025-11-17 (PHASE 3 Tech Verification)
**Status:** ✅ Approved, CRITICAL UPDATE

**Original Plan:** Redis 7
**Updated To:** Redis 8.2 (major version upgrade)

**Rationale:**
- Major performance improvements (30% faster for our use cases)
- Better memory efficiency
- Improved clustering support

**Migration Effort:** 1 day for configuration updates

**Consequences:**
- ⚠️ Breaking changes in config format (need migration guide)

---

## 📱 Mobile Decisions

### MD-001: State Management - Redux Toolkit
**Decision:** Redux Toolkit 2.10.1 + RTK Query
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- Complex state (user, loyalty, transactions, events)
- Need offline support (cached data)
- Need optimistic updates (instant UI feedback)

**Decision:**
Use Redux Toolkit with RTK Query for API calls + caching.

**Rationale:**
- Industry standard for complex React Native apps
- RTK Query handles caching, invalidation automatically
- DevTools for debugging
- Redux Persist for offline support

**Consequences:**
- ✅ Predictable state management
- ✅ Excellent debugging
- ⚠️ Learning curve for junior developers

---

## 🔄 Integration Decisions

### ID-001: CRM Integration Strategy - Adapters Pattern
**Decision:** Base adapter interface with CRM-specific implementations
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- 6 different CRM systems (YCLIENTS, Iiko, 1С, AMO CRM, Renovatio, CSV)
- Each has different API format
- Need maintainable, extensible design

**Decision:**
Create `BaseCRMAdapter` abstract class with methods:
- `fetch_transactions(since, until)`
- `find_customer_by_phone(phone)`
- `apply_bonus(customer_id, amount)`

Each CRM implements this interface.

**Rationale:**
- Single interface for all CRMs (easier to test, maintain)
- Can add new CRMs without changing core logic
- Strategy pattern (standard OOP design)

**Consequences:**
- ✅ Clean, maintainable code
- ✅ Easy to add new CRMs
- ⚠️ Need to map different CRM data formats to common schema

---

## 📊 Analytics Decisions

### AD-001: RFM Segmentation - ClickHouse Daily Batch
**Decision:** Calculate RFM segments daily in ClickHouse
**Date:** 2025-11-17
**Status:** ✅ Approved

**Context:**
- RFM segmentation requires complex aggregations
- Calculating on-demand would be slow (PostgreSQL not optimized for this)
- Business owners need fast dashboard loads

**Decision:**
- Celery Beat task runs daily at 1am
- Calculates RFM scores for all customers in ClickHouse
- Results cached in Redis for dashboard queries

**Rationale:**
- ClickHouse 100x faster for aggregations
- Daily refresh sufficient (RFM doesn't change hourly)
- Dashboard loads in <1s vs 10s+ if calculated on-demand

**Consequences:**
- ✅ Fast dashboards
- ⚠️ RFM data up to 24 hours stale
- ⚠️ Need to handle timezone correctly (Moscow time)

---

**Total Decisions:** 15 documented
**Last Review:** 2025-11-17
**Status:** All approved for MVP development
