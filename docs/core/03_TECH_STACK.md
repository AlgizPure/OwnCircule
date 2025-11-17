# Свой Круг - Tech Stack

**Created:** 2025-11-17
**Version:** 1.0 (November 2025 Verified)
**Status:** Approved for Production

---

## 📋 Stack Overview

This document describes the complete technology stack for Свой Круг, verified for November 2025 compatibility through PHASE 3 Tech Verification. All versions have been validated against latest stable releases, security advisories, and community adoption.

**Key Principles:**
- **Modern & Stable:** Use latest LTS/stable versions (verified Nov 2025)
- **Russian Federation Compliance:** Cloud providers and data storage in RF
- **Production-Ready:** Proven technologies with strong community support
- **Mobile-First:** React Native for iOS/Android from single codebase
- **API-Driven:** RESTful APIs with OpenAPI documentation

---

## 📱 Frontend (Mobile App)

### Core Framework
- **React Native 0.81** (Nov 2025 stable)
  - Why: Cross-platform iOS/Android, 80%+ code reuse, active community
  - Alternatives considered: Flutter (rejected: weaker ecosystem for Russian market)
  - Update from: 0.73 → 0.81 (PHASE 3 recommendation)

- **TypeScript 5.7.x**
  - Why: Type safety, better IDE support, fewer runtime errors
  - Strict mode enabled for maximum safety

### State Management
- **Redux Toolkit 2.10.1** (latest Nov 2025)
  - Why: Standard for complex state, devtools, persistence
  - Update from: 2.0 → 2.10.1 (PHASE 3 CRITICAL)
  - RTK Query for API caching and synchronization

### Navigation
- **React Navigation 6.x**
  - Why: De-facto standard for RN navigation, flexible, well-documented
  - Stack, tab, and drawer navigators for multi-level navigation

### UI Components
- **React Native Paper 5.x**
  - Why: Material Design 3, Tiffany-style theming, accessibility built-in
  - Custom theme: Tiffany blue (#0ABAB5), premium aesthetic

### Camera & QR
- **react-native-vision-camera 4.x**
  - Why: High-performance camera access, QR scanning, modern architecture
  - Alternatives: react-native-camera (deprecated)

### Notifications
- **Firebase Cloud Messaging (FCM)**
  - Why: Free, reliable, iOS + Android support, rich notifications
  - @react-native-firebase/messaging wrapper

### Analytics & Monitoring
- **Firebase Analytics** - User behavior tracking
- **Amplitude** - Product analytics, funnels, retention
- **Sentry** - Crash reporting, error tracking

---

## 🔧 Backend

### Language & Framework
- **Python 3.13** (latest stable Nov 2025)
  - Why: Fast development, rich ecosystem, ML/analytics libraries
  - Update from: 3.11 → 3.13 (PHASE 3 CRITICAL - performance improvements)

- **FastAPI 0.121.2** (latest Nov 2025)
  - Why: High performance, async support, auto OpenAPI docs, type hints
  - Update from: 0.104 → 0.121.2 (PHASE 3 CRITICAL - security & features)

### API & Documentation
- **OpenAPI 3.0** (Swagger UI)
  - Why: Auto-generated from FastAPI code, interactive testing, client generation
  - Endpoint: `/docs` (Swagger), `/redoc` (ReDoc)

### Authentication
- **PyJWT 2.9.x** (latest Nov 2025)
  - Why: Standard JWT implementation, RS256 support
  - Access tokens (15 min) + Refresh tokens (30 days)

### Task Queue
- **Celery 5.4.x** (latest Nov 2025)
  - Why: Async task processing (notifications, analytics, integrations)
  - Update from: 5.3 → 5.4.x (PHASE 3 RECOMMENDED)
  - Beat scheduler for periodic tasks (RFM calculation, churn prediction)

### ORM & Database
- **SQLAlchemy 2.0.44** (latest Nov 2025)
  - Why: Powerful ORM, async support, migration tools (Alembic)
  - Update from: 2.0 → 2.0.44 (PHASE 3 CRITICAL - async improvements)

### HTTP Client
- **httpx 0.28.x** (latest Nov 2025)
  - Why: Modern async HTTP client for CRM integrations
  - Update from: 0.24 → 0.28.x (PHASE 3 RECOMMENDED)

---

## 🗄️ Databases & Storage

### Primary Database
- **PostgreSQL 16.11** (latest stable Nov 2025)
  - Why: ACID compliance, JSONB support, battle-tested for transactions
  - Update from: 15 → 16.11 (PHASE 3 RECOMMENDED - performance)
  - Extensions: pgcrypto (encryption), pg_trgm (full-text search)

### Analytics Database
- **ClickHouse 25.8 LTS** (latest LTS Nov 2025)
  - Why: Columnar storage, 100x faster analytics queries than PostgreSQL
  - Update from: 23 → 25.8 LTS (PHASE 3 RECOMMENDED - LTS stability)
  - Use cases: RFM segmentation, Win-Win analytics, churn prediction

### Cache & Session Store
- **Redis 8.2** (latest stable Nov 2025)
  - Why: In-memory cache, session storage, Celery broker
  - Update from: 7 → 8.2 (PHASE 3 CRITICAL - major performance upgrade)
  - Redis Insight for monitoring

### Search Engine
- **Elasticsearch 9.3.0** (latest Nov 2025)
  - Why: Full-text search for businesses, events, transactions
  - Update from: 8 → 9.3.0 (PHASE 3 RECOMMENDED - new features)

---

## ☁️ Infrastructure & DevOps

### Cloud Provider
- **Yandex Cloud** (primary)
  - Why: Russian data residency (152-ФЗ compliance), low latency, ruble billing
  - Services: Compute Cloud (VMs), Managed PostgreSQL, Object Storage
- **VK Cloud** (backup/failover)
  - Why: Geographic redundancy, Russian jurisdiction

### Containerization
- **Docker 27.x** (latest Nov 2025)
  - Why: Consistent environments, easy deployment, microservices-ready
  - Docker Compose for local development
  - Update from: 24.x → 27.x (PHASE 3 RECOMMENDED)

### CI/CD
- **GitHub Actions**
  - Why: Native GitHub integration, free for public repos, flexible workflows
  - Pipelines: lint → test → build → deploy (staging/production)

### Monitoring & Logging
- **Prometheus 3.3.0** (latest Nov 2025)
  - Why: Metrics collection, time-series DB, alerting
  - Update from: 2.x → 3.3.0 (PHASE 3 CRITICAL - major upgrade)

- **Grafana 11.5.0** (latest Nov 2025)
  - Why: Metrics visualization, dashboards, alerts
  - Update from: 10.x → 11.5.0 (PHASE 3 RECOMMENDED)

- **Loki 3.3.0** (latest Nov 2025)
  - Why: Log aggregation, Grafana integration
  - Update from: 2.x → 3.3.0 (PHASE 3 RECOMMENDED)

- **Sentry**
  - Why: Error tracking for backend + frontend, release tracking

### Object Storage
- **Yandex Object Storage** (S3-compatible)
  - Why: Images, event photos, user avatars, backups
  - CDN for fast content delivery

---

## 🔌 External Integrations

### CRM Systems
1. **YCLIENTS REST API** - Миндаль (салон красоты)
2. **Iiko API** - Лисичкино (гастромаркет)
3. **1С REST API** - Skinerica, Лисичкино
4. **Bitrix24 REST API** - Skinerica
5. **AMO CRM API** - Стим Центр (стоматология)
6. **МИС Renovatio API** - Миллениум (медцентр)
7. **CSV Upload** - Fallback for any system

### Payment Gateways
- **ЮKassa** (primary)
  - Why: Russian bank support, low fees, well-documented
- **CloudPayments** (backup)
  - Why: Alternative for redundancy, international cards

### SMS & Communications
- **SMS.ru API** (primary)
  - Why: Reliable delivery, competitive pricing, Russian phone support
- **SMSC.ru API** (backup)
  - Why: Failover, bulk pricing

### Push Notifications
- **Firebase Cloud Messaging (FCM)**
  - Why: Free, reliable, iOS + Android, rich notifications

---

## 📦 Development Tools

### Package Managers
- **npm / yarn** - Frontend dependencies
- **pip / poetry** - Backend dependencies

### Code Quality
- **ESLint + Prettier** - Frontend linting/formatting
- **Ruff 0.8.x** - Python linting (fast, modern)
- **mypy** - Python type checking

### Testing
- **Jest + React Native Testing Library** - Frontend unit tests
- **pytest + pytest-asyncio** - Backend unit tests
- **Playwright** - E2E testing for web admin panel

---

## 🔒 Security & Compliance

### Data Protection
- **152-ФЗ Compliance** - Russian personal data law
- **HTTPS/TLS 1.3** - All API traffic encrypted
- **At-rest encryption** - PostgreSQL transparent data encryption
- **Врачебная тайна** - Medical data isolation (Module 13)

### Authentication
- **JWT (RS256)** - Asymmetric tokens for security
- **SMS OTP** - Two-factor authentication
- **Rate limiting** - 5 requests/min for auth endpoints

---

## 🔄 Migration Effort (from Initial Stack)

**Estimated effort:** 2-3 weeks across Sprint 1-3

**Critical updates:**
1. Python 3.11 → 3.13 (2 days - testing, compatibility checks)
2. FastAPI 0.104 → 0.121.2 (1 day - breaking changes review)
3. Redux Toolkit 2.0 → 2.10.1 (3 days - migration guide)
4. SQLAlchemy async improvements (2 days - refactor queries)
5. Redis 7 → 8.2 (1 day - configuration updates)
6. Prometheus 2.x → 3.3.0 (2 days - major version upgrade)

---

## 🔄 Related Documentation

- [Architecture](./04_ARCHITECTURE.md) - System design and data models
- [Module Requirements](../requirements/) - Detailed module specifications
- [PHASE 3 Verification](../../UPMT/bootstrap/verification/tech-stack-analysis.md) - Full verification analysis

---

**Last Updated:** 2025-11-17
**Owner:** Engineering Team
**Status:** Approved for Development
