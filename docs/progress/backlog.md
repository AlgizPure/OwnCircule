# Product Backlog - Свой Круг

**Last Updated:** 2025-11-17
**Total Stories:** 325 functions across 15 modules
**Prioritization Framework:** MoSCoW (Must/Should/Could/Won't) + Sprint Assignment

---

## 📊 Backlog Overview

| Priority | User Stories | Story Points (Est.) | Target |
|----------|--------------|---------------------|--------|
| **P0 (MVP Critical)** | ~200 functions | ~350 pts | Sprint 1-6 (12 weeks) |
| **P1 (Important)** | ~90 functions | ~150 pts | v1.5 (Month 4-6) |
| **P2 (Nice-to-have)** | ~35 functions | ~60 pts | v2.0 (Month 7-12) |
| **TOTAL** | **325 functions** | **~560 pts** | **12 months** |

---

## 🎯 P0: MVP Critical (Sprint 1-6)

### Sprint 1 (Weeks 1-2): Foundation - 20 story points

#### Epic 1.1: Backend Foundation (8 pts)
- **User Story 1.1.1:** Set up FastAPI project structure (2 pts)
  - Acceptance Criteria: FastAPI app runs, health check endpoint `/health`, auto-generated OpenAPI docs
  - Dependencies: None
  - Module: Foundation

- **User Story 1.1.2:** Configure PostgreSQL database (3 pts)
  - Acceptance Criteria: PostgreSQL 16.11 running in Docker, connection pooling configured, migrations framework (Alembic) set up
  - Dependencies: 1.1.1
  - Module: Foundation

- **User Story 1.1.3:** Create base models (users, businesses, bonuses) (3 pts)
  - Acceptance Criteria: SQLAlchemy models for `users`, `businesses`, `bonuses` tables with all fields from architecture doc
  - Dependencies: 1.1.2
  - Module: Foundation

#### Epic 1.2: Authentication & Security (8 pts)
- **User Story 1.2.1:** Implement JWT authentication (Module 13) (5 pts)
  - Acceptance Criteria: RS256 token signing, 15-min access tokens, 30-day refresh tokens, token blacklist for logout
  - Dependencies: 1.1.3
  - Module: 13 (Security)
  - Related: docs/requirements/module-13-security.md:133-138

- **User Story 1.2.2:** Implement SMS OTP for login (Module 12.3.1) (3 pts)
  - Acceptance Criteria: SMS.ru integration, OTP generation, 5-min expiration, rate limiting (5 SMS per hour per phone)
  - Dependencies: 1.2.1
  - Module: 12 (Notifications)
  - Related: docs/requirements/module-12-notifications.md:119-122

#### Epic 1.3: Mobile App Shell (4 pts)
- **User Story 1.3.1:** Set up React Native project (2 pts)
  - Acceptance Criteria: React Native 0.81 project, TypeScript configured, runs on iOS + Android simulators
  - Dependencies: None
  - Module: 1 (Mobile App)

- **User Story 1.3.2:** Create basic navigation (2 pts)
  - Acceptance Criteria: React Navigation 6 configured, stack navigator with Welcome → Login → Home screens
  - Dependencies: 1.3.1
  - Module: 1 (Mobile App)

---

### Sprint 2 (Weeks 3-4): Authentication & Loyalty - 25 story points

#### Epic 2.1: User Onboarding (Module 1.1) (8 pts)
- **User Story 2.1.1:** Phone registration with SMS OTP (3 pts)
  - Acceptance Criteria: Russian phone validation (+7 XXX XXX-XX-XX), SMS code arrives <30s, code expires after 5 min
  - Dependencies: 1.2.2
  - Module: 1.1 (Authentication & Onboarding)
  - Related: docs/requirements/module-01-mobile-app.md:29

- **User Story 2.1.2:** Welcome video & onboarding slides (2 pts)
  - Acceptance Criteria: 30-second video autoplays (skippable after 5s), 3 slides explaining club benefits
  - Dependencies: 2.1.1
  - Module: 1.1

- **User Story 2.1.3:** Profile creation (3 pts)
  - Acceptance Criteria: User enters name, email, birthdate, uploads profile photo, data encrypted with AES-256
  - Dependencies: 2.1.1
  - Module: 1.1

#### Epic 2.2: Bonus System (Module 2.1) (12 pts)
- **User Story 2.2.1:** Bonus accrual on purchase (5 pts)
  - Acceptance Criteria: QR scan → transaction created → bonuses accrued based on status tier (5% Insider, 7% VIP, 10% Elite)
  - Dependencies: 1.2.1, 1.1.3
  - Module: 2.1 (Bonus System)
  - Related: docs/requirements/module-02-loyalty-system.md:46

- **User Story 2.2.2:** Bonus balance & history (4 pts)
  - Acceptance Criteria: User sees total bonus balance, transaction history with filters (all/accrual/redemption), pagination
  - Dependencies: 2.2.1
  - Module: 2.1

- **User Story 2.2.3:** Bonus redemption (3 pts)
  - Acceptance Criteria: User selects bonuses to redeem at checkout, bonuses deducted from balance, transaction recorded
  - Dependencies: 2.2.2
  - Module: 2.1

#### Epic 2.3: User Profile (Module 1.4) (5 pts)
- **User Story 2.3.1:** View & edit profile (3 pts)
  - Acceptance Criteria: User views profile (name, phone, email, status tier), can edit name/email/photo
  - Dependencies: 2.1.3
  - Module: 1.4 (User Profile)

- **User Story 2.3.2:** QR wallet (2 pts)
  - Acceptance Criteria: User sees dynamic QR code (Member ID encoded), QR refreshes every 60s, brightness boost on QR screen
  - Dependencies: 2.3.1
  - Module: 1.3 (QR Wallet)
  - Related: docs/requirements/module-01-mobile-app.md:108

---

### Sprint 3 (Weeks 5-6): CRM Integration & Status - 30 story points

#### Epic 3.1: Status System (Module 2.2) (10 pts)
- **User Story 3.1.1:** Status tier calculation (5 pts)
  - Acceptance Criteria: Celery task runs daily, calculates total_spent across all partners, assigns tier (Insider <50K, VIP 50-200K, Elite >200K)
  - Dependencies: 2.2.1
  - Module: 2.2 (Status System)
  - Related: docs/requirements/module-02-loyalty-system.md:134

- **User Story 3.1.2:** Status upgrade notifications (2 pts)
  - Acceptance Criteria: Push notification when status upgrades, modal in app shows new benefits
  - Dependencies: 3.1.1
  - Module: 2.2

- **User Story 3.1.3:** Inner Circle invitation (3 pts)
  - Acceptance Criteria: Elite users with >500K spent receive Inner Circle invitation, acceptance flow, exclusive benefits activated
  - Dependencies: 3.1.1
  - Module: 2.2

#### Epic 3.2: First CRM Integration - YCLIENTS (Module 8.1) (12 pts)
- **User Story 3.2.1:** YCLIENTS adapter implementation (8 pts)
  - Acceptance Criteria: `YCLIENTSAdapter` class, `fetch_transactions()` fetches from YCLIENTS API, `find_customer_by_phone()` searches customers, error handling + retry logic
  - Dependencies: None (standalone adapter)
  - Module: 8.1 (CRM Connectors)
  - Related: docs/requirements/module-08-crm-integrations.md:102

- **User Story 3.2.2:** Automatic transaction sync (4 pts)
  - Acceptance Criteria: Celery Beat task runs hourly, fetches new transactions from YCLIENTS, creates transactions in our DB, accrues bonuses
  - Dependencies: 3.2.1
  - Module: 8.2 (Data Synchronization)

#### Epic 3.3: Simple Cross-Promo Chains (Module 5.1) (8 pts)
- **User Story 3.3.1:** Create simple chain (A → B) (5 pts)
  - Acceptance Criteria: Superadmin creates chain "Skinerica → Миндаль", sets trigger (purchase >3000₽), sets reward (500₽ coupon at Миндаль)
  - Dependencies: 2.2.1
  - Module: 5.1 (Simple Chains)
  - Related: docs/requirements/module-05-cross-promo.md:87

- **User Story 3.3.2:** Chain trigger engine (3 pts)
  - Acceptance Criteria: After transaction at Skinerica >3000₽, Celery task triggers within 1 min, creates coupon for Миндаль, sends push notification
  - Dependencies: 3.3.1
  - Module: 5.1

---

### Sprint 4 (Weeks 7-8): Events & Coupons - 25 story points

#### Epic 4.1: Coupons & Promotions (Module 2.3) (10 pts)
- **User Story 4.1.1:** Coupon issuance (4 pts)
  - Acceptance Criteria: System creates coupon record, assigns to user, user sees coupon in "Мои купоны" tab, expiration date shown
  - Dependencies: 2.2.1
  - Module: 2.3 (Coupons & Promotions)

- **User Story 4.1.2:** Coupon redemption (4 pts)
  - Acceptance Criteria: User selects coupon at checkout, business scans QR code, coupon marked as redeemed, cannot be used again
  - Dependencies: 4.1.1
  - Module: 2.3

- **User Story 4.1.3:** Coupon expiration handling (2 pts)
  - Acceptance Criteria: Celery task runs daily at midnight, marks expired coupons, sends notification 3 days before expiration
  - Dependencies: 4.1.1
  - Module: 2.3

#### Epic 4.2: Event Management (Module 4.1) (10 pts)
- **User Story 4.2.1:** Create event (Superadmin) (5 pts)
  - Acceptance Criteria: Superadmin creates event with title, description, date, location, max attendees, eligibility (VIP+), cover photo
  - Dependencies: None
  - Module: 4.1 (Event Management)
  - Related: docs/requirements/module-04-events.md:74

- **User Story 4.2.2:** Event listing in app (3 pts)
  - Acceptance Criteria: Users see upcoming events, filter by date/status eligibility, event detail view with registration button
  - Dependencies: 4.2.1
  - Module: 4.1

- **User Story 4.2.3:** Event editing & cancellation (2 pts)
  - Acceptance Criteria: Superadmin can edit event details, cancel event (sends notifications to registered users)
  - Dependencies: 4.2.1
  - Module: 4.1

#### Epic 4.3: Second CRM Integration - Iiko (Module 8.1) (5 pts)
- **User Story 4.3.1:** Iiko adapter implementation (5 pts)
  - Acceptance Criteria: `IikoAdapter` class, fetches transactions from Iiko Cloud API, maps Iiko data to our schema
  - Dependencies: 3.2.1 (pattern established)
  - Module: 8.1

---

### Sprint 5 (Weeks 9-10): Events Registration & Analytics - 20 story points

#### Epic 5.1: Event Registration (Module 4.2) (8 pts)
- **User Story 5.1.1:** Event registration flow (4 pts)
  - Acceptance Criteria: User clicks "Зарегистрироваться", confirms attendance, receives QR ticket, capacity enforced (max attendees)
  - Dependencies: 4.2.2
  - Module: 4.2 (Registration & Attendance)

- **User Story 5.1.2:** QR ticket & check-in (4 pts)
  - Acceptance Criteria: User shows QR ticket at event, business scans with tablet, marks user as attended, prevents duplicate check-ins
  - Dependencies: 5.1.1
  - Module: 4.2

#### Epic 5.2: Win-Win Analytics (Module 5.4) (6 pts)
- **User Story 5.2.1:** Win-Win matrix calculation (6 pts)
  - Acceptance Criteria: ClickHouse query aggregates cross-promo effectiveness for all business pairs, calculates conversion rates, revenue attribution
  - Dependencies: 3.3.2
  - Module: 5.4 (Win-Win Analytics)
  - Related: docs/requirements/module-05-cross-promo.md:91

#### Epic 5.3: Superadmin Panel - Basic (Module 10) (6 pts)
- **User Story 5.3.1:** Business management (3 pts)
  - Acceptance Criteria: Superadmin views all businesses, adds new business, edits details, deactivates business
  - Dependencies: None
  - Module: 10.1 (Business Management)

- **User Story 5.3.2:** User management (3 pts)
  - Acceptance Criteria: Superadmin views all users, searches by phone/email, views user details, can ban/unban users
  - Dependencies: None
  - Module: 10.2 (User Management)

---

### Sprint 6 (Weeks 11-12): Testing & Launch - 10 story points

#### Epic 6.1: Beta Testing (5 pts)
- **User Story 6.1.1:** Beta tester onboarding (2 pts)
  - Acceptance Criteria: 50 beta testers recruited, invited via email/SMS, onboarded to app, provided feedback form
  - Dependencies: All prior epics
  - Module: Testing

- **User Story 6.1.2:** Bug fixes & polish (3 pts)
  - Acceptance Criteria: Critical bugs fixed, UI polish based on beta feedback, performance optimization
  - Dependencies: 6.1.1
  - Module: Testing

#### Epic 6.2: Production Deployment (5 pts)
- **User Story 6.2.1:** Production infrastructure setup (3 pts)
  - Acceptance Criteria: Yandex Cloud production environment, CI/CD pipeline (GitHub Actions), monitoring (Sentry, Grafana)
  - Dependencies: None
  - Module: DevOps

- **User Story 6.2.2:** Production launch (2 pts)
  - Acceptance Criteria: App submitted to App Store + Google Play, backend deployed to production, 200+ registrations achieved
  - Dependencies: 6.2.1
  - Module: DevOps

---

## 📈 P1: Important - v1.5 (Month 4-6)

### Module 6: Offer Constructor (18 functions, ~30 pts)
- Epic: Self-service offer creation for businesses
- Target: Month 4-5
- Dependencies: Module 2 (Loyalty)

### Module 7: Business Analytics (25 functions, ~40 pts)
- Epic: RFM segmentation, churn prediction, cohort analysis
- Target: Month 4-6
- Dependencies: Module 3 (Transactions), Module 8 (CRM)

### Module 9: Business Admin Panel (22 functions, ~35 pts)
- Epic: Web dashboard for business owners
- Target: Sprint 2-6 (parallel with mobile, basic version in MVP)
- Dependencies: Module 3, 6, 7

### Module 10: Superadmin Panel - Full (18 functions, ~30 pts)
- Epic: Complete platform administration
- Target: Month 4-5 (basic version in Sprint 5)
- Dependencies: All modules

### Module 11: Referral Program (10 functions, ~15 pts)
- Epic: Viral growth mechanism with Ambassador status
- Target: Month 4
- Dependencies: Module 1 (Mobile)

---

## 🎨 P2: Nice-to-have - v2.0 (Month 7-12)

### Module 14: Gamification & Badges (7 functions, ~12 pts)
- Epic: Category exploration badges, achievement system
- Target: Month 7-8
- Dependencies: Module 2 (Loyalty)

---

## 🚫 Won't Have (Out of Scope for v1.0)

- Multi-language support (Russian only for MVP)
- Cryptocurrency payments
- AI-powered recommendations (manual curation for MVP)
- White-label solution for other cities

---

## 📋 Backlog Grooming Notes

### Estimation Scale
- 1 pt = ~4 hours (simple feature)
- 2 pts = ~8 hours (moderate feature)
- 3 pts = ~12 hours (complex feature)
- 5 pts = ~20 hours (very complex feature)
- 8 pts = ~32 hours (epic, needs breakdown)

### Definition of Ready (DoR)
- [ ] User story follows format: "As a [role], I want to [action], so that [benefit]"
- [ ] Acceptance criteria defined (Given/When/Then format)
- [ ] Dependencies identified
- [ ] Story points estimated
- [ ] Technical approach discussed

### Definition of Done (DoD)
- [ ] Code written and peer-reviewed
- [ ] Unit tests written (80%+ coverage)
- [ ] Integration tests written (critical paths)
- [ ] API documentation updated
- [ ] Deployed to staging and tested
- [ ] Product Owner accepted

---

## 📊 Velocity Tracking

### Sprint 1 (Planned)
- **Committed:** 20 pts
- **Completed:** TBD
- **Velocity:** TBD

### Sprint 2 (Planned)
- **Committed:** 25 pts
- **Completed:** TBD
- **Velocity:** TBD

**Average Velocity (Target):** 20-25 pts per 2-week sprint

---

**Last Updated:** 2025-11-17
**Next Grooming Session:** Sprint 1 Planning (when team assembled)
**Backlog Health:** 🟢 Ready for Sprint 1
