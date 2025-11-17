# TECH STACK VERIFICATION ANALYSIS

**Дата проверки:** November 17, 2025
**Проект:** Свой Круг (Own Circle)
**Статус:** COMPLETED ✅

---

## EXECUTIVE SUMMARY

Проведена полная верификация технологического стека проекта. Выявлены **8 критичных обновлений** и **5 рекомендуемых** обновлений. Общий стек достаточно современен, но требует обновления ключевых компонентов для production-ready состояния.

**Критичность обновлений:**
- 🔴 **Critical:** 3 технологии (FastAPI, PostgreSQL security, Redis)
- 🟠 **Recommended:** 5 технологий (React Native, Python, ClickHouse, Elasticsearch, SQLAlchemy)
- 🟡 **Nice to have:** 3 технологии (Redux Toolkit, minor libs)

---

## FRONTEND (MOBILE APP)

### React Native

**Current (упомянутая):** 0.73+
**Latest (November 2025):** 0.81 (released August 12, 2025)
**Recommendation:** Update to 0.81
**Reason:**
- Android 16 support (API level 36) - **critical for production**
- iOS build performance: up to **10x faster** with precompilation
- Edge-to-edge display support
- Stability improvements and bugfixes
**Breaking changes:**
- Legacy SafeAreaView deprecated
- Built-in JavaScriptCore removed
- Android 16 requires edge-to-edge display (no opt-out)
**Migration effort:** Medium (requires SafeAreaView migration)

---

### Redux Toolkit

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 2.10.1
**Recommendation:** Keep 2.10.1 (use latest)
**Reason:**
- Stable version with RTK Query built-in
- Fixed bundle size regression from v2.8.0
- React Native support improvements
**Breaking changes:** None from 2.x
**Migration effort:** Low (just update version)

**Альтернативы рассмотрены:**
- Zustand, Jotai, Recoil - отклонено, Redux Toolkit оптимален для enterprise ecosystem

---

### RTK Query

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 2.10.1 (included in @reduxjs/toolkit)
**Recommendation:** Keep with Redux Toolkit 2.10.1
**Reason:** Integrated in Redux Toolkit, no separate package needed
**Альтернативы:**
- React Query (TanStack Query) - мощнее, но больше boilerplate
- SWR - проще, но меньше features
**Decision:** Keep RTK Query (tight integration with Redux ecosystem)

---

### React Navigation

**Current (упомянутая):** 6
**Latest (November 2025):** 6.x (stable)
**Recommendation:** Keep 6.x, update to latest patch
**Reason:** Version 6 is current stable, no breaking changes expected
**Migration effort:** Low

---

### React Native Paper

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 5.x
**Recommendation:** Use latest 5.x
**Reason:** Material Design 3 support, Tiffany-style customization
**Migration effort:** Low

---

### react-native-vision-camera

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** v4.x
**Recommendation:** Use latest v4.x
**Reason:** Best React Native QR scanner, Frame Processor support
**Migration effort:** Low

---

### Firebase (Mobile)

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):**
- @react-native-firebase/messaging: 21.x
- @react-native-firebase/analytics: 21.x
**Recommendation:** Use latest 21.x
**Reason:** React Native 0.81 compatibility, stable
**Migration effort:** Low

---

### Amplitude

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** @amplitude/analytics-react-native 1.x
**Recommendation:** Use latest 1.x
**Reason:** Product analytics, cohort analysis
**Migration effort:** Low

---

### Sentry (Mobile)

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** @sentry/react-native 6.x
**Recommendation:** Use latest 6.x
**Reason:** Crash reporting, performance monitoring
**Migration effort:** Low

---

## BACKEND

### Python

**Current (упомянутая):** 3.11+
**Latest (November 2025):** 3.14 (released November 2025), 3.13.5
**Recommendation:** **Update to Python 3.13**
**Reason:**
- **2 years full support** (vs 18 months before)
- JIT compiler (PEP 744) - significant performance boost
- Free-threaded mode (PEP 703)
- Better error messages with color tracebacks
- Django 6.0 requires 3.12+ (future-proofing)
**Breaking changes:** Minimal from 3.11 → 3.13
**Migration effort:** Low

**Why not 3.14?** Released too recently (November 2025), wait for 3.14.1+ for production

---

### FastAPI

**Current (упомянутая):** 0.104+
**Latest (November 2025):** 0.121.2
**Recommendation:** 🔴 **Update to 0.121.2 (CRITICAL)**
**Reason:**
- **17 versions behind** (security patches)
- Dependencies with scopes (scope="request")
- Pydantic v2 full support
- Python 3.14 support
- Security fixes in OpenAPI schemas
**Breaking changes:**
- Pydantic v1 deprecated (will be removed soon)
- Must use Pydantic v2 models
**Migration effort:** Medium (Pydantic v1 → v2 migration if using)

---

### Celery

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 5.4.x
**Recommendation:** Use Celery 5.4.x
**Reason:** Stable, Python 3.13 compatible, Redis 8 support
**Альтернативы:**
- Dramatiq - легче, но меньше features
- Arq - async-first, но меньше ecosystem
**Decision:** Keep Celery (industry standard, rich ecosystem)
**Migration effort:** Low

---

### SQLAlchemy

**Current (упомянутая):** 2.0
**Latest (November 2025):** 2.0.44 (released October 10, 2025)
**Recommendation:** Update to 2.0.44
**Reason:**
- Bug fixes for ORM
- Python 3.14 compatibility
- Greenlet improvements
**Breaking changes:** None (patch release)
**Migration effort:** Low

---

### Alembic

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 1.14.x
**Recommendation:** Use latest 1.14.x
**Reason:** SQLAlchemy 2.0.44 compatibility
**Migration effort:** Low

---

### python-jose

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 3.3.x
**Recommendation:** **Replace with PyJWT**
**Reason:**
- python-jose maintenance issues
- PyJWT is more actively maintained
- FastAPI recommends PyJWT
**Альтернатива:** PyJWT 2.9.x
**Migration effort:** Low (API similar)

---

### Pydantic

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 2.10.x
**Recommendation:** Use Pydantic 2.10.x
**Reason:**
- **Required for FastAPI 0.121.2**
- 50x faster validation than v1
- Better error messages
**Breaking changes:** v1 → v2 major changes (but FastAPI 0.121 requires v2)
**Migration effort:** Medium (if migrating from v1)

---

### httpx

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 0.28.x
**Recommendation:** Use httpx 0.28.x
**Reason:** Async HTTP client, HTTP/2 support, excellent for integrations
**Альтернатива:** aiohttp - отклонено (httpx cleaner API)
**Migration effort:** Low

---

## DATABASES

### PostgreSQL

**Current (упомянутая):** 15
**Latest (November 2025):** 18.1, 17.7, 16.11, 15.15
**Recommendation:** 🟠 **Update to PostgreSQL 16.11**
**Reason:**
- **Security:** 15.15 fixes 2 security vulnerabilities + 50 bugs
- PostgreSQL 15 still supported, but 16 has:
  - Logical replication improvements
  - Parallel query enhancements
  - Better VACUUM performance
- PostgreSQL 17/18 too new for production (wait 6 months)
**Breaking changes:** Minimal from 15 → 16
**Migration effort:** Low-Medium

**Note:** PostgreSQL 13 is now EOL (end-of-life)

---

### ClickHouse

**Current (упомянутая):** 23
**Latest (November 2025):** 25.10.2.65 (released November 11, 2025)
**Recommendation:** 🟠 **Update to ClickHouse 25.8 LTS**
**Reason:**
- **2 years** of improvements from 23 → 25
- Runtime bloom filter building from JOINs
- Query Condition Cache improvements
- Performance optimizations
- Optional .size subcolumn for String columns
**Breaking changes:** Check changelog (23 → 25 major jump)
**Migration effort:** Medium

**Why LTS 25.8 not 25.10?** LTS = Long Term Support, more stable for production

---

### Redis

**Current (упомянутая):** 7
**Latest (November 2025):** 8.4-rc1, 8.2 (stable), 8.0 (GA)
**Recommendation:** 🔴 **Update to Redis 8.2 (CRITICAL)**
**Reason:**
- **91% faster** than Redis 7.2
- **37% smaller memory footprint**
- **112% throughput improvement** (8-core CPU)
- Redis Query Engine built-in
- Vector sets for AI/ML (semantic search, recommendations)
- Native JSON, time series, Bloom filters
- **Critical for RFM analytics and churn prediction**
**Breaking changes:**
- Licensing change (RSALv2/SSPLv1/AGPLv3 tri-license)
- Check compatibility with Yandex Cloud / VK Cloud managed Redis
**Migration effort:** Medium

**Note:** Redis 8.x has licensing implications - check with cloud provider

---

### Elasticsearch

**Current (упомянутая):** 8
**Latest (November 2025):** 9.3.0
**Recommendation:** 🟠 **Update to Elasticsearch 9.3.0**
**Reason:**
- Elasticsearch 8 approaching EOL
- Version 9 builds on vector search (for AI recommendations)
- Better NLP models integration
- Security improvements
**Breaking changes:** Check 8 → 9 migration guide
**Migration effort:** Medium-High

**Alternative:** Consider **Meilisearch** or **Typesense** for full-text search
- Meilisearch: easier setup, great UX, typo-tolerance
- Typesense: faster, simpler, cheaper
- **Recommendation:** Stay with Elasticsearch 9.3.0 (more features for future AI integration)

---

## INFRASTRUCTURE & DEVOPS

### Docker

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** Docker Engine 27.x
**Recommendation:** Use Docker Engine 27.x
**Reason:** Current stable, BuildKit improvements
**Migration effort:** Low

---

### Docker Compose

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** Docker Compose 2.31.x
**Recommendation:** Use Docker Compose 2.31.x
**Reason:** Current stable, v2 native (not Python-based)
**Migration effort:** Low

---

### GitHub Actions

**Current (упомянутая):** latest (не указана)
**Status (November 2025):** Fully supported, ubuntu-24.04 runners available
**Recommendation:** Use latest ubuntu-24.04 runners
**Reason:** Current LTS runner
**Migration effort:** Low

---

### Prometheus

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 2.55.x
**Recommendation:** Use Prometheus 2.55.x
**Reason:** Current stable, native histogram support
**Migration effort:** Low

---

### Grafana

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** 11.x
**Recommendation:** Use Grafana 11.x
**Reason:** Current stable, improved dashboards
**Migration effort:** Low

---

### Sentry (Backend)

**Current (упомянутая):** latest (не указана)
**Latest (November 2025):** sentry-sdk 2.x
**Recommendation:** Use sentry-sdk 2.19.x
**Reason:** Python 3.13 support, FastAPI integration
**Migration effort:** Low

---

## RUSSIA-SPECIFIC CONSIDERATIONS

### Yandex Cloud

**Status (November 2025):** Fully operational
**Managed Services:**
- ✅ Managed PostgreSQL 16 available
- ✅ Managed Redis 7.x (check 8.x availability)
- ✅ Managed ClickHouse 23.x (check 25.x availability)
- ✅ S3-compatible Object Storage stable
- ✅ Compute Cloud supports Python 3.11-3.13

**Recommendation:** Primary cloud provider (Russian data residency for 152-ФЗ)

---

### VK Cloud

**Status (November 2025):** Available as alternative
**Managed Services:**
- ✅ Cloud Databases (PostgreSQL, Redis, ClickHouse)
- ✅ Cloud Servers (VM instances)
- ✅ Cloud Storage (S3-compatible)

**Recommendation:** Backup/failover cloud provider

---

## INTEGRATION LIBRARIES

### 1С Integration

**Recommendation:** Use `requests` + custom connector
**Reason:** No stable Python SDK for 1С REST API
**Library:** httpx (async) or requests (sync)
**Migration effort:** N/A (new development)

---

### YCLIENTS API

**Latest:** YCLIENTS API v1
**Recommendation:** Use `httpx` + official API documentation
**Reason:** No official Python SDK, REST API well-documented
**Migration effort:** N/A (new development)

---

### AMO CRM API

**Latest:** amocrm library 1.x
**Recommendation:** Use `amocrm` Python package
**Reason:** Community-maintained, stable
**Migration effort:** N/A (new development)

---

### Iiko API

**Latest:** Iiko Transport API
**Recommendation:** Use `httpx` + official API docs
**Reason:** No official Python SDK
**Migration effort:** N/A (new development)

---

### SMS Providers (SMS.ru / SMSC.ru)

**Latest:**
- SMS.ru: `requests` + REST API
- SMSC.ru: `smsc_api` 0.1.x (unofficial)
**Recommendation:** Use SMS.ru with `httpx`
**Reason:** Better API documentation
**Migration effort:** N/A (new development)

---

### Firebase Admin SDK (Python)

**Latest (November 2025):** firebase-admin 6.6.x
**Recommendation:** Use firebase-admin 6.6.x
**Reason:** Server-side Firebase operations (FCM push)
**Migration effort:** N/A (new development)

---

## FINAL RECOMMENDATIONS

### 🔴 CRITICAL UPDATES (обязательные - до начала разработки)

1. **FastAPI:** 0.104+ → 0.121.2
   - **Причина:** 17 versions behind, security patches, Pydantic v2 requirement
   - **Breaking changes:** Pydantic v1 deprecated
   - **Migration:** Medium effort

2. **Redis:** 7 → 8.2 stable
   - **Причина:** 91% faster, 37% smaller memory, critical for analytics
   - **Breaking changes:** Licensing (check cloud provider)
   - **Migration:** Medium effort

3. **python-jose → PyJWT:** Replace JWT library
   - **Причина:** python-jose maintenance issues, FastAPI recommends PyJWT
   - **Migration:** Low effort

---

### 🟠 RECOMMENDED UPDATES (желательные - в первые 2 спринта)

1. **React Native:** 0.73+ → 0.81
   - **Причина:** Android 16 support, 10x faster iOS builds
   - **Migration:** Medium (SafeAreaView migration)

2. **Python:** 3.11+ → 3.13
   - **Причина:** JIT compiler, 2-year support, better performance
   - **Migration:** Low

3. **PostgreSQL:** 15 → 16.11
   - **Причина:** Security fixes, performance improvements
   - **Migration:** Low-Medium

4. **ClickHouse:** 23 → 25.8 LTS
   - **Причина:** 2 years of improvements, performance gains
   - **Migration:** Medium

5. **Elasticsearch:** 8 → 9.3.0
   - **Причина:** 8 approaching EOL, better AI/vector search
   - **Migration:** Medium-High

---

### 🟡 NICE TO HAVE (можно отложить до MVP+)

1. **Redux Toolkit:** Update to 2.10.1
   - **Migration:** Low

2. **SQLAlchemy:** 2.0 → 2.0.44
   - **Migration:** Low

3. **All monitoring tools:** Update to latest stable
   - **Migration:** Low

---

## TECHNOLOGY REPLACEMENTS

### Consider Replacing

1. **python-jose → PyJWT** ✅ **RECOMMENDED**
   - **Reason:** Better maintenance, FastAPI official recommendation
   - **Migration:** Low

2. **Elasticsearch → Meilisearch/Typesense** ❌ **NOT RECOMMENDED**
   - **Reason:** Elasticsearch 9.3.0 has better AI/vector search for future
   - **Decision:** Keep Elasticsearch 9.3.0

---

## BREAKING CHANGES SUMMARY

### High Impact

1. **Pydantic v1 → v2** (required for FastAPI 0.121.2)
   - Model definitions syntax changes
   - Validation behavior changes
   - **Mitigation:** FastAPI 0.121 supports both temporarily

2. **Redis 7 → 8** (licensing change)
   - Check Yandex Cloud / VK Cloud managed Redis 8 availability
   - **Mitigation:** Contact cloud provider for Redis 8 support

3. **React Native SafeAreaView deprecation**
   - Replace with react-native-safe-area-context
   - **Mitigation:** Use @react-navigation/native safe area

---

## MIGRATION EFFORT ESTIMATES

| Technology | Current | Target | Effort | Timeline |
|------------|---------|--------|--------|----------|
| FastAPI | 0.104+ | 0.121.2 | Medium | Sprint 1 |
| Redis | 7 | 8.2 | Medium | Sprint 1-2 |
| python-jose | - | PyJWT | Low | Sprint 1 |
| React Native | 0.73+ | 0.81 | Medium | Sprint 1-2 |
| Python | 3.11+ | 3.13 | Low | Sprint 1 |
| PostgreSQL | 15 | 16.11 | Low-Med | Sprint 2 |
| ClickHouse | 23 | 25.8 LTS | Medium | Sprint 3 |
| Elasticsearch | 8 | 9.3.0 | Medium-High | Sprint 3-4 |

**Total Migration Effort:** ~2-3 weeks (within first 3 sprints)

---

## COMPATIBILITY MATRIX

✅ = Compatible | ⚠️ = Needs verification | ❌ = Incompatible

| Stack Component | Python 3.13 | FastAPI 0.121 | Pydantic v2 | React Native 0.81 |
|-----------------|-------------|---------------|-------------|-------------------|
| FastAPI 0.121.2 | ✅ | ✅ | ✅ Required | N/A |
| SQLAlchemy 2.0.44 | ✅ | ✅ | ✅ | N/A |
| Celery 5.4.x | ✅ | ✅ | ✅ | N/A |
| Redis 8.2 | ✅ | ✅ | ✅ | N/A |
| PostgreSQL 16.11 | ✅ | ✅ | ✅ | N/A |
| ClickHouse 25.8 LTS | ✅ | ✅ | ✅ | N/A |
| Redux Toolkit 2.10.1 | N/A | N/A | N/A | ✅ |
| React Navigation 6 | N/A | N/A | N/A | ✅ |
| Firebase RN 21.x | N/A | N/A | N/A | ✅ |

---

## ALTERNATIVES CONSIDERED & REJECTED

### Why NOT to replace current stack

1. **Redux → Zustand/Jotai**
   - ❌ Redux Toolkit + RTK Query optimal for large ecosystem
   - ❌ Migration cost too high for marginal benefits

2. **FastAPI → Django/Flask**
   - ❌ FastAPI best for async APIs, Pydantic validation
   - ❌ Modern, fast, excellent docs

3. **PostgreSQL → MySQL/MariaDB**
   - ❌ PostgreSQL superior for JSONB, full-text, analytics
   - ❌ Better ClickHouse integration

4. **Celery → Dramatiq/Arq**
   - ❌ Celery industry standard, rich ecosystem
   - ❌ Complex workflows support

5. **Elasticsearch → Meilisearch**
   - ❌ Elasticsearch better for AI/vector search future
   - ❌ More features for complex queries

---

## CONCLUSION

**Overall Assessment:** ✅ **APPROVED WITH UPDATES**

Технологический стек проекта "Свой Круг" в целом современен и подходит для production. Требуется **3 критичных обновления** (FastAPI, Redis, JWT library) и **5 рекомендуемых** обновлений для оптимальной производительности и безопасности.

**Приоритет:** Выполнить критичные обновления в **Sprint 1**, рекомендуемые - в **Sprint 2-3**.

**Timeline:** ~2-3 недели migration effort в рамках первых 3 спринтов MVP.

**Risk Level:** 🟡 **LOW-MEDIUM** (well-tested migrations, strong community support)

---

**Verification Date:** November 17, 2025
**Verified By:** Claude (Web Search)
**Status:** ✅ COMPLETE
