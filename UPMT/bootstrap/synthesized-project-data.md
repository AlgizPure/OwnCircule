# SYNTHESIZED PROJECT DATA

**Дата:** 2025-11-17
**Статус:** Ready for documentation generation
**Проект:** Свой Круг (Own Circle)

---

## PROJECT OVERVIEW

**Название:** Свой Круг (Own Circle)
**Тип:** Mobile App (iOS + Android) + Web Backend
**Версия:** MVP (v1.0)

**Описание:** Женский премиум клуб с кросс-промо между бизнесами. Закрытая экосистема лояльности для женщин 30-50 лет с доходом 80K+ рублей/месяц.

**Проблема:**
Клиенты премиум-сегмента (beauty, wellness, гастрономия) тратят 15-30K₽/месяц, но не получают значимых бонусов за лояльность. Бизнесы конкурируют за одну и ту же аудиторию, вместо того чтобы сотрудничать. Нет мотивации пробовать новые категории услуг.

**Ценность (Value Proposition):**
- **Для клиентов:** Кешбэк 5-10%, кросс-промо между бизнесами разных категорий, эксклюзивные мероприятия, премиум-статусы, экономия до 30K₽/год
- **Для бизнесов:** Новые клиенты через кросс-промо, RFM-аналитика, прогноз оттока, win-win цепочки, доступ к премиум аудитории

**Целевая аудитория:**
- **Primary:** Женщины 30-50 лет, доход 80K+/месяц, траты на бьюти/wellness 15-30K/месяц
- **Secondary:** Собственники премиум бизнесов (бьюти, wellness, гастрономия)
- **Segments:**
  - Постоянные клиенты 5 стартовых партнёров (Skinerica, Лисичкино, Стим Центр, Миндаль, Миллениум)
  - Предприниматели женщины
  - Руководители среднего и высшего звена
- **Initial User Base:** 200+ регистраций к концу MVP, 50 бета-тестеров

**Geo:** Russia (Москва, старт)

---

## FEATURES & MODULES

**Всего функций:** 325
**Всего модулей:** 15
**Тип проекта:** New project (greenfield)

### Модули (по приоритету):

**🔴 CRITICAL (MVP Sprint 1-6):**

**1. Мобильное приложение (Frontend)** - 68 функций
- **Описание:** Клиентское React Native приложение для iOS и Android
- **Приоритет:** Critical
- **Статус:** New (to be developed)
- **Подмодули:**
  - 1.1 Аутентификация и Onboarding (12 функций) - SMS-код, регистрация, валидация
  - 1.2 Главный экран (Home) (10) - Статус, QR-кнопка, gamification ring, акции
  - 1.3 QR-Кошелек (8) - Генерация QR, баланс бонусов, Apple Wallet/Google Pay
  - 1.4 Профиль пользователя (12) - Профиль, статистика, настройки
  - 1.5 Мероприятия (Events Hub) (14) - Фильтры, регистрация, детали
  - 1.6 Конструктор мероприятий (VIP/Elite) (8) - Создание предложений
  - 1.7 Каталог бизнесов (4) - Список партнеров, детали, записаться

**2. Система лояльности** - 45 функций
- **Описание:** Бонусная программа, статусы (Insider/VIP/Elite/Inner Circle), купоны
- **Приоритет:** Critical
- **Статус:** New
- **Подмодули:**
  - 2.1 Бонусная система (15) - Начисление, списание, множители, сгорание
  - 2.2 Система статусов (12) - Автоматический расчет статуса, прогресс
  - 2.3 Купоны и промо (18) - 5 типов купонов (скидка, бонусы, кросс-промо, пакет, подарок)

**3. Транзакции и история покупок** - 12 функций
- **Описание:** Управление покупками, история, синхронизация с CRM
- **Приоритет:** Critical
- **Статус:** New

**8. Интеграции с CRM** - 20 функций
- **Описание:** Коннекторы к CRM систем партнёров
- **Приоритет:** Critical (MVP требует 2 интеграции)
- **Статус:** New
- **Ключевые интеграции:**
  - 1С (Skinerica, Лисичкино)
  - YCLIENTS (Миндаль) - MVP Sprint 5-6
  - Iiko (Лисичкино) - MVP Sprint 5-6
  - AMO CRM (Стим Центр)
  - МИС Renovatio (Миллениум)
  - CSV-загрузчик (fallback)

**9. Админ-панель для бизнесов** - 22 функции
- **Описание:** Панель управления для собственников бизнесов
- **Приоритет:** Critical
- **Статус:** New
- **Подмодули:**
  - 9.1 Управление клиентами (6)
  - 9.2 Управление транзакциями (5) - Ручной ввод, QR-сканирование
  - 9.3 Аналитика и отчеты (6)
  - 9.4 Управление предложениями (5)

**10. Суперадмин экосистемы** - 18 функций
- **Описание:** Административная панель для управления всей экосистемой
- **Приоритет:** Critical
- **Статус:** New

**13. Безопасность и Compliance** - 8 функций
- **Описание:** 152-ФЗ compliance, врачебная тайна, шифрование, RBAC
- **Приоритет:** Critical
- **Статус:** New

---

**🟠 IMPORTANT (MVP Sprint 3-6 + v1.5):**

**4. Мероприятия и Events Hub** - 28 функций
- **Приоритет:** Important (базовая версия в MVP, полная в v1.5)
- **Статус:** New
- **Подмодули:**
  - 4.1 Управление мероприятиями (10)
  - 4.2 Регистрация и участие (8)
  - 4.3 Голосование и конструктор (10) - v2.0 feature

**5. Кросс-промо и цепочки** - 22 функции
- **Приоритет:** Important
- **Статус:** New
- **Подмодули:**
  - 5.1 Простые цепочки A→B (8)
  - 5.2 Последовательные цепочки A→B→C (4)
  - 5.3 Циклические и веерные цепочки (4)
  - 5.4 Win-Win аналитика (6)

**6. Конструктор предложений** - 18 функций
- **Приоритет:** Important
- **Статус:** New
- **5 типов предложений:** Скидка, бонусы, кросс-промо, пакет, подарок

**7. Аналитика для бизнесов** - 25 функций
- **Приоритет:** Important
- **Статус:** New
- **Подмодули:**
  - 7.1 Общая статистика (8) - Дашборд, выручка, метрики
  - 7.2 Источники клиентов (4)
  - 7.3 Куда уходят клиенты (3)
  - 7.4 RFM-сегментация (5)
  - 7.5 Прогноз оттока (5)

**12. Уведомления и коммуникации** - 18 функций
- **Приоритет:** Important (Push в v1.5)
- **Статус:** New

---

**🟡 NICE TO HAVE (v1.5 - v2.0):**

**11. Реферальная программа** - 10 функций
- **Приоритет:** Nice to have (v1.5)
- **Статус:** New

**14. Геймификация и бейджи** - 7 функций
- **Приоритет:** Nice to have (v2.0)
- **Статус:** New

**15. Система бюджета мероприятий** - 4 функции
- **Приоритет:** Nice to have (v2.0)
- **Статус:** New

---

### Приоритетные функции (Top 20):

**🔴 CRITICAL (Sprint 1-2):**

1. **SMS-аутентификация** - Регистрация по телефону + SMS-код - Module: 1.1
2. **Профиль пользователя** - Аватар, данные, баланс бонусов - Module: 1.4
3. **QR-кошелек** - Генерация уникального QR для начисления бонусов - Module: 1.3
4. **Начисление бонусов** - Автоматическое начисление 5-10% кешбэка - Module: 2.1
5. **Система статусов** - Расчет статуса (Insider/VIP/Elite) - Module: 2.2

**🔴 CRITICAL (Sprint 3-4):**

6. **История транзакций** - Отображение всех покупок пользователя - Module: 3
7. **Ручной ввод транзакции** - Бизнес сканирует QR и вводит сумму - Module: 9.2
8. **Каталог бизнесов** - Список 5 партнёров с категориями - Module: 1.7
9. **Админ-панель для бизнесов** - Просмотр клиентов и транзакций - Module: 9
10. **Суперадмин панель** - Управление бизнесами и пользователями - Module: 10

**🔴 CRITICAL (Sprint 5-6):**

11. **Интеграция YCLIENTS** - Синхронизация транзакций из Миндаль - Module: 8.1
12. **Интеграция Iiko** - Синхронизация транзакций из Лисичкино - Module: 8.1
13. **CSV-загрузчик** - Fallback для бизнесов без API - Module: 8.1
14. **Простые купоны** - Скидка % или фиксированная сумма - Module: 2.3
15. **Кросс-промо купоны** - Покупка в A → купон на B - Module: 2.3

**🟠 IMPORTANT (v1.5):**

16. **Push-уведомления** - О начислении бонусов, смене статуса - Module: 12.1
17. **Реферальная программа** - Генерация ссылки, награды - Module: 11
18. **Базовые мероприятия** - Создание, регистрация - Module: 4.1, 4.2
19. **RFM-сегментация** - Автоматическая сегментация клиентов - Module: 7.4
20. **Простые цепочки A→B** - Кросс-промо между бизнесами - Module: 5.1

---

## TECH STACK (Verified November 2025)

**Verification Date:** 2025-11-17
**Verification Status:** ✅ APPROVED
**Total Technologies Verified:** 31

### Frontend (Mobile App)

- **Framework:** React Native 0.81 ✅ (UPDATED from 0.73+)
  - Android 16 support, 10x faster iOS builds
- **Language:** TypeScript 5.7.x
- **State Management:** Redux Toolkit 2.10.1 (includes RTK Query)
- **Navigation:** React Navigation 6.x
- **UI Library:** React Native Paper 5.x (Material Design 3, Tiffany-style)
- **QR Scanner:** react-native-vision-camera 4.x
- **Push Notifications:** Firebase Cloud Messaging (@react-native-firebase/messaging 21.x)
- **Analytics:** Firebase Analytics 21.x + Amplitude 1.x
- **Crash Reporting:** Sentry (@sentry/react-native 6.x)
- **Biometrics:** react-native-biometrics
- **Wallet:** Apple Wallet + Google Pay integration

### Backend

- **Runtime:** Python 3.13 ✅ (UPDATED from 3.11+)
  - JIT compiler, 2-year support, performance boost
- **Framework:** FastAPI 0.121.2 ✅ (CRITICAL UPDATE from 0.104+)
  - 17 versions of security patches
- **Validation:** Pydantic 2.10.x ✅ (required for FastAPI 0.121)
- **Task Queue:** Celery 5.4.x
- **Message Broker:** Redis 8.2 (for Celery)
- **ORM:** SQLAlchemy 2.0.44 ✅ (UPDATED from 2.0)
- **Migrations:** Alembic 1.14.x
- **JWT:** PyJWT 2.9.x ✅ (REPLACED python-jose)
- **HTTP Client:** httpx 0.28.x
- **Firebase Admin:** firebase-admin 6.6.x

### Databases

- **PostgreSQL:** 16.11 ✅ (RECOMMENDED UPDATE from 15)
  - Security fixes, performance improvements
  - Purpose: Users, transactions, events, businesses, offers
  - Extensions: pgcrypto, pg_trgm, uuid-ossp

- **ClickHouse:** 25.8 LTS ✅ (RECOMMENDED UPDATE from 23)
  - 2 years of improvements
  - Purpose: Analytics, RFM segmentation, churn prediction, event logs

- **Redis:** 8.2 ✅ (CRITICAL UPDATE from 7)
  - 91% faster, 37% memory reduction
  - Purpose: Cache, sessions, Celery broker, rate limiting

- **Elasticsearch:** 9.3.0 ✅ (RECOMMENDED UPDATE from 8)
  - EOL avoidance, AI/vector search features
  - Purpose: Full-text search (businesses, events, offers)

### Infrastructure

**Cloud Provider:**
- **Primary:** Yandex Cloud (ru-central1 region)
  - 152-ФЗ compliance (Russian data residency)
  - Managed PostgreSQL 16, Redis 8, ClickHouse 25
  - Object Storage (S3-compatible)
- **Backup:** VK Cloud (failover/disaster recovery)

**Containers:**
- Docker Engine 27.x
- Docker Compose 2.31.x

**CI/CD:**
- GitHub Actions (ubuntu-24.04 runners)

**Monitoring:**
- Prometheus 2.55.x
- Grafana 11.x
- Sentry (sentry-sdk 2.19.x)
- Loki (log aggregation)

**Storage:**
- Yandex Object Storage (avatars, photos, logos)

**SSL/TLS:**
- Let's Encrypt + Yandex Certificate Manager

### Dev Tools

- **Python Linter/Formatter:** Ruff 0.7.x (replaces black, flake8, isort)
- **Python Type Checker:** mypy 1.13.x
- **TS/JS Linter:** ESLint 9.x
- **TS/JS Formatter:** Prettier 3.x
- **Git Hooks:** pre-commit 4.x

### Applied Updates (from PHASE 3):

**🔴 Critical (Sprint 1):**
- FastAPI: 0.104+ → 0.121.2
- Redis: 7 → 8.2
- JWT: python-jose → PyJWT 2.9.x

**🟠 Recommended (Sprint 2-3):**
- React Native: 0.73+ → 0.81
- Python: 3.11+ → 3.13
- PostgreSQL: 15 → 16.11
- ClickHouse: 23 → 25.8 LTS
- Elasticsearch: 8 → 9.3.0

**Migration Effort:** 2-3 weeks across Sprint 1-3

---

## ARCHITECTURE (High-Level)

**Pattern:** Modular Monolith (Backend) + Mobile App (Frontend)

**Frontend Architecture:**
- Feature-based structure
- Redux Toolkit for global state (user, auth, bonuses)
- RTK Query for API calls & caching
- React Navigation for screen flow
- Component-driven UI with React Native Paper

**Backend Architecture:**
- Layered Architecture (Controller → Service → Repository)
- FastAPI dependency injection
- SQLAlchemy ORM with repository pattern
- Async/await for all I/O operations
- Celery for background tasks (sync, emails, analytics)

**Planned Code Structure:**

```
backend/
├── app/
│   ├── api/             # FastAPI routers
│   ├── core/            # Config, security, auth
│   ├── db/              # Database models, migrations
│   ├── schemas/         # Pydantic models
│   ├── services/        # Business logic
│   ├── integrations/    # CRM connectors
│   └── tasks/           # Celery tasks

mobile/
├── src/
│   ├── screens/         # Screen components
│   ├── components/      # Reusable UI components
│   ├── navigation/      # React Navigation setup
│   ├── store/           # Redux slices & RTK Query
│   ├── services/        # API client
│   └── utils/           # Helpers
```

---

## TIMELINE & MILESTONES

**Estimated Duration:** 12 weeks (MVP)
**Start Date:** 2025-11-17
**Target MVP Launch:** 2026-02-09

**Milestones:**

**Phase 1: Foundation (Sprint 1-2, 4 weeks)**
- Duration: 4 weeks
- Deliverables:
  - Backend setup (FastAPI, PostgreSQL, Redis)
  - Mobile app scaffold (React Native, Redux)
  - Authentication (SMS-код, JWT)
  - User profile (registration, login, profile screen)
  - Database schema (users, bonuses, transactions)
- **Success Criteria:** Users can register and login

**Phase 2: Core Features (Sprint 3-4, 4 weeks)**
- Duration: 4 weeks
- Deliverables:
  - QR-кошелек (generation, display)
  - Bonus system (accrual, balance, history)
  - Status system (Insider/VIP/Elite calculation)
  - Transaction history
  - Admin panel for businesses (manual transaction entry)
  - Business catalog
- **Success Criteria:** Manual transactions work, bonuses accrue

**Phase 3: Integrations & Launch (Sprint 5-6, 4 weeks)**
- Duration: 4 weeks
- Deliverables:
  - YCLIENTS integration (Миндаль)
  - Iiko integration (Лисичкино)
  - CSV uploader (fallback for other partners)
  - Coupon system (simple discounts, cross-promo)
  - Superadmin panel
  - Security hardening (152-ФЗ compliance)
- **Success Criteria:** 2+ integrations live, auto-sync works

**Phase 4: Beta Testing (Sprint 7-8, 2 weeks)**
- Duration: 2 weeks
- Deliverables:
  - Bug fixes from integration testing
  - Performance optimization
  - 50 beta testers onboarded
  - Monitoring setup (Prometheus, Grafana, Sentry)
- **Success Criteria:** 0 critical bugs, 50+ active users

**Phase 5: Production Launch (Sprint 9-12, 4 weeks)**
- Duration: 4 weeks
- Deliverables:
  - Production deployment (Yandex Cloud)
  - 200+ registrations
  - Marketing campaign support
  - Analytics dashboards for businesses
  - First success stories (cross-purchases)
- **Success Criteria:** 200+ users, 10%+ cross-purchase rate

**Phase 6: v1.5 Release (+3 months after MVP)**
- Duration: 3 months
- Deliverables:
  - Referral program
  - Push notifications
  - Basic events module
  - +3 new businesses
- **Success Criteria:** 500+ users, 15% cross-purchase rate

**Phase 7: v2.0 Release (+6 months after v1.5)**
- Duration: 6 months
- Deliverables:
  - Event constructor (VIP/Elite can propose events)
  - Weighted voting
  - AI recommendations
  - Social feed
  - Detailed analytics
- **Success Criteria:** 25% cross-purchase rate (NSM target)

---

## USER STORIES & USE CASES

**Primary User Stories (Top 10):**

**As a premium client, I want to:**

1. **Register quickly via phone** so that I can start earning bonuses immediately
   - Acceptance: SMS-код, 30 sec registration, auto Insider status

2. **Scan my QR-code at checkout** so that I earn cashback automatically
   - Acceptance: Business scans QR, bonuses accrue within 15 min

3. **See my bonus balance clearly** so that I know how much I can spend
   - Acceptance: Balance on home screen, history accessible

4. **Track my status progress** so that I'm motivated to reach VIP/Elite
   - Acceptance: Visual progress ring, "X₽ to VIP" hint

5. **Browse all partner businesses** so that I can discover new services
   - Acceptance: Catalog with categories, photos, ratings, location

6. **Receive cross-promo coupons** so that I try new businesses and save money
   - Acceptance: "Buy in A → get 20% off in B" notification

7. **Use bonuses to pay** so that I feel the value of the program
   - Acceptance: Bonuses deducted at checkout, transaction visible

8. **Register for events** so that I can network with other members
   - Acceptance: Event list, 1-click registration, calendar sync

9. **Invite friends via referral link** so that we both get rewards
   - Acceptance: Unique link, 1000₽ bonus each after first purchase

10. **Feel exclusive** so that I'm proud to be a member
    - Acceptance: Tiffany-style UI, Inner Circle status, VIP events

**As a business owner, I want to:**

1. **See all my customers from the ecosystem** so that I know who joined via cross-promo
   - Acceptance: Customer list, source attribution

2. **Create cross-promo offers easily** so that I attract new clients
   - Acceptance: Offer constructor, 5-7 steps, preview, publish

3. **Track ROI of my offers** so that I know what works
   - Acceptance: Views, activations, conversions, ROI% calculation

4. **Get churn alerts** so that I can win back at-risk clients
   - Acceptance: "5 clients at risk" alert, suggested actions

5. **Understand which businesses send me clients** so that I can strengthen partnerships
   - Acceptance: Win-Win matrix, top 3 sources

---

## KEY DECISIONS (from Interview - Auto-filled)

**Decision 1: Team & Resources**
- **Question:** Какая команда будет работать над проектом?
- **Answer:** [TO BE CONFIRMED]
- **Impact:** Affects timeline and skill requirements. Need: Backend (Python/FastAPI), Frontend (React Native), DevOps (Yandex Cloud), QA, Designer
- **Note:** Auto-filled with reasonable defaults in metadata.yaml

**Decision 2: Design System**
- **Question:** Есть ли готовые дизайн-материалы?
- **Answer:** 13 screenshots detected in 00_DESIGN_RAW_DATA/screenshots/
- **Impact:** PHASE 5.5 will analyze design raw data
- **Status:** Design data detected ✅

**Decision 3: Infrastructure**
- **Question:** Текущая инфраструктура (Cloud accounts, GitHub, domains)
- **Answer:** [TO BE CONFIRMED]
- **Impact:** Yandex Cloud preferred (152-ФЗ compliance), VK Cloud as backup
- **Assumptions:** GitHub Organization needed, domains to be registered

**Decision 4: CRM Access**
- **Question:** Доступы к системам партнёров (API tokens)
- **Answer:** [TO BE CONFIRMED]
- **Impact:** MVP requires YCLIENTS + Iiko integrations in Sprint 5-6
- **Fallback:** CSV-loader for partners without API access

**Decision 5: Compliance Level**
- **Question:** 152-ФЗ и врачебная тайна - уровень защиты
- **Answer:** [TO BE CONFIRMED]
- **Impact:** Affects security implementation
- **Assumptions:**
  - 152-ФЗ: Standard level (encryption, user consent, data residency)
  - Врачебная тайна: No diagnosis storage, only transaction amounts

---

## CONSTRAINTS & ASSUMPTIONS

**Constraints:**

1. **Timeline:** MVP must launch in 12 weeks (6 sprints)
2. **Budget:** ~20,300₽/month for Yandex Cloud production infrastructure
3. **Geography:** Russia-only (data residency requirement - 152-ФЗ)
4. **Initial Partners:** Limited to 5 businesses on MVP launch
5. **Integration Complexity:** Partners use different CRM systems (1С, YCLIENTS, Iiko, AMO, МИС)
6. **Technology:** Must use technologies verified for November 2025 compatibility
7. **Platform:** iOS + Android required from day 1 (React Native choice)

**Assumptions:**

1. **Team Available:** Assume team of 4-5 developers can be assembled
2. **Partner Buy-in:** 5 initial partners are committed and will provide CRM access
3. **User Adoption:** 200+ registrations achievable through partner promotion
4. **API Availability:** YCLIENTS and Iiko APIs are stable and documented
5. **Cloud Services:** Yandex Cloud supports PostgreSQL 16, Redis 8, ClickHouse 25
6. **Design:** Tiffany-style (#0ABAB5) is approved by stakeholders
7. **Payments:** Payment gateway (ЮKassa) integration postponed to v1.5+
8. **Content Moderation:** Manual moderation sufficient for MVP (50-200 users)
9. **Mobile Platforms:** iOS 14+ and Android 10+ are acceptable minimum versions
10. **Internet:** Stable internet connection required (no offline mode in MVP)

---

## RISKS & MITIGATION

**Risk 1: Integration delays with partner CRM systems**
- **Probability:** High
- **Impact:** High (blocks MVP launch)
- **Mitigation:**
  - Start integration work in Sprint 3 (not Sprint 5)
  - CSV-loader as fallback for all partners
  - Prioritize YCLIENTS + Iiko (best documented APIs)
  - Request API access from partners ASAP

**Risk 2: Low user adoption (< 200 registrations)**
- **Probability:** Medium
- **Impact:** High (MVP success criteria not met)
- **Mitigation:**
  - Partner marketing campaigns
  - Referral bonuses (1000₽ each)
  - Exclusive beta tester benefits
  - In-store QR code promotions
  - Social media campaigns (Instagram, VK)

**Risk 3: Tech stack compatibility issues**
- **Probability:** Low
- **Impact:** Medium (delays Sprint 1-2)
- **Mitigation:**
  - All tech verified for November 2025 ✅
  - Migration plan documented (2-3 weeks)
  - Critical updates in Sprint 1 (FastAPI, Redis, PyJWT)
  - Tested compatibility matrix created

**Risk 4: 152-ФЗ compliance violations**
- **Probability:** Low
- **Impact:** Critical (legal liability)
- **Mitigation:**
  - Yandex Cloud ru-central1 region (data in Russia)
  - User consent on registration
  - Encryption at rest (PostgreSQL) & in transit (HTTPS/TLS)
  - Audit logs for all PII operations
  - Legal review before production launch

**Risk 5: Performance issues at scale (200+ users)**
- **Probability:** Medium
- **Impact:** Medium (poor UX)
- **Mitigation:**
  - Redis 8.2 caching (91% faster than v7)
  - ClickHouse 25.8 for analytics (not PostgreSQL)
  - Database indexing (transactions, user_id)
  - Celery for async tasks (sync, emails)
  - Load testing in Sprint 7-8

**Risk 6: Design inconsistency / poor UI/UX**
- **Probability:** Medium
- **Impact:** Medium (affects premium positioning)
- **Mitigation:**
  - 13 design screenshots available for analysis
  - PHASE 5.5 will extract design system
  - React Native Paper (Material Design 3 base)
  - Tiffany-style theming (#0ABAB5)
  - UI/UX designer on team [TO BE CONFIRMED]

---

## DESIGN DATA STATUS

**Design Data Detected:** ✅ Yes
**Total Design Files:** 13 screenshots

**Files by Category:**
- **Screenshots:** 13 files (ChatGPT generated mockups from Nov 5, 2025)
  - Home screens, QR wallet, business catalog, events, etc.
- **Chats:** 1 example file (no actual chat logs)
- **Moodboards:** 0 files (only README)
- **Figma:** 0 files (only README)
- **Research:** 0 files (only README)
- **Brand:** 0 files (only README)

**Next Phase:** ✅ PHASE 5.5 (Design System Extraction) **WILL BE EXECUTED**

**Design Analysis Plan:**
- Extract color palette from screenshots (Tiffany blue #0ABAB5 confirmed)
- Document UI patterns (cards, buttons, navigation)
- Extract typography (fonts, sizes, weights)
- Identify component library (React Native Paper confirmed)
- Create design tokens for developers

---

## EXTERNAL INTEGRATIONS

**CRM Systems (5 partners):**

1. **1С** (Skinerica, Лисичкино)
   - Type: REST API (custom connector)
   - Library: httpx
   - Priority: Medium (CSV fallback available)

2. **YCLIENTS** (Миндаль - салон красоты)
   - Type: Official REST API
   - Library: httpx + API docs
   - Priority: **High (MVP Sprint 5-6)**

3. **Iiko** (Лисичкино - гастромаркет)
   - Type: Iiko Transport API
   - Library: httpx
   - Priority: **High (MVP Sprint 5-6)**

4. **AMO CRM** (Стим Центр - стоматология)
   - Type: REST API
   - Library: amocrm Python package
   - Priority: Medium (v1.5)

5. **МИС Renovatio** (Миллениум - медцентр)
   - Type: Custom integration (врачебная тайна compliance)
   - Library: httpx
   - Priority: Medium (v1.5)

**Payment Gateways (v1.5+):**
- ЮKassa SDK
- CloudPayments SDK (alternative)

**SMS Providers:**
- SMS.ru (primary) - httpx + REST API
- SMSC.ru (backup)

**Push & Analytics:**
- Firebase Cloud Messaging (firebase-admin SDK)
- Firebase Analytics
- Amplitude HTTP API v2

---

## PARTNERS (5 Initial Businesses)

1. **Skinerica** - Косметология
   - CRM: 1С + Bitrix24
   - Category: Beauty
   - Status: Confirmed

2. **Лисичкино** - Гастромаркет
   - CRM: Iiko + 1С
   - Category: Food
   - Status: Confirmed

3. **Стим Центр** - Стоматология
   - CRM: AMO CRM
   - Category: Health
   - Status: Confirmed

4. **Миндаль** - Салон красоты
   - CRM: YCLIENTS
   - Category: Beauty
   - Status: Confirmed

5. **Миллениум** - Медицинский центр
   - CRM: МИС Renovatio
   - Category: Health/Wellness
   - Status: Confirmed

**Expansion Plan:** +3 businesses in v1.5 (3 months after MVP)

---

## METRICS & SUCCESS CRITERIA

**North Star Metric (NSM):**
- **Metric:** % клиентов, совершивших ≥2 покупки в разных категориях за 60 дней
- **MVP Target:** 10% (baseline)
- **v1.5 Target:** 15%
- **v2.0 Target:** 25% (end of 6th month)

**KPIs:**

**User Acquisition:**
- CAC (Customer Acquisition Cost): [TO BE DEFINED]
- Registrations: 200+ by MVP end
- Beta Testers: 50 active users

**Engagement:**
- Retention Rate: [TO BE DEFINED]
- Churn Rate: < 20% monthly
- NPS (Net Promoter Score): > 50
- Cross-Purchase Rate: 25% (tied to NSM)

**Financial:**
- LTV (Lifetime Value): [TO BE DEFINED]
- Ecosystem Revenue Share: [TO BE DEFINED]
- Average cashback per user/month: [TO BE TRACKED]

**Technical:**
- API response time: < 100ms (p95)
- App crash rate: < 1%
- Integration sync success rate: > 99%

**MVP Success Criteria:**
- ✅ 200+ registrations
- ✅ 50+ active beta users
- ✅ 2+ integrations live (YCLIENTS + Iiko)
- ✅ Bonus system functional
- ✅ 0 critical bugs in production
- ✅ 10%+ users with ≥2 purchases in different categories

---

## USER STATUSES & BENEFITS

**1. Insider (базовый):**
- **Requirements:** Registration + 1 purchase
- **Benefits:** Cashback 5%, access to basic events
- **Expected:** 80% of users

**2. VIP:**
- **Requirements:** ≥30,000₽ spent + ≥3 categories
- **Benefits:** Cashback 7%, priority event registration, profile badge
- **Expected:** 15% of users

**3. Elite:**
- **Requirements:** ≥100,000₽ spent + ≥5 categories (or top 1%)
- **Benefits:** Cashback 10%, event constructor access, weighted voting (3.0x)
- **Expected:** 4% of users

**4. Inner Circle:**
- **Requirements:** By invitation only (or ≥200,000₽)
- **Benefits:** Ambassador status, exclusive events, voting weight 5.0x
- **Expected:** 1% of users

---

## NEXT STEPS

**Immediate (PHASE 5 - Documentation Generation):**
- Generate full technical documentation
- Create module requirements (15 modules)
- Setup AI rules for development
- Extract design system (PHASE 5.5)
- Create API specifications
- Database schema documentation

**Short-term (Sprint 1 - Foundation):**
- Assemble development team
- Setup GitHub Organization
- Apply critical tech stack updates (FastAPI, Redis, PyJWT)
- Setup development environment (Docker Compose)
- Backend scaffold (FastAPI + PostgreSQL)
- Mobile app scaffold (React Native + Redux)
- Authentication flow (SMS-код + JWT)

**Medium-term (Sprint 2-6 - MVP):**
- Implement 6 critical modules
- Build 2 CRM integrations (YCLIENTS, Iiko)
- Deploy to Yandex Cloud
- Onboard 50 beta testers
- Launch production (200+ users)

**Long-term (v1.5 - v2.0):**
- Scale to 500+ users
- Add 3 new businesses
- Implement AI recommendations
- Achieve 25% cross-purchase rate (NSM)
- Expand to other Russian cities

---

**Status:** ✅ READY FOR PHASE 5 (Documentation Generation)
**Next Phase:** PHASE 5 - Generate comprehensive technical documentation
**Estimated Time:** 2-4 hours (largest phase)

**Data Sources:**
- PHASE 1: extracted_features.md (325 functions), modules_list.md (15 modules)
- PHASE 2: metadata.yaml (auto-filled)
- PHASE 3: final-tech-stack.md (verified November 2025)
- Design: 13 screenshots in 00_DESIGN_RAW_DATA/screenshots/
