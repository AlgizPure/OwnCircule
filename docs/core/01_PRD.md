# Свой Круг - Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Approved  
**Owner:** Product Team

---

## 📋 Document Overview

### Purpose

This Product Requirements Document (PRD) defines the complete feature set, user flows, and technical requirements for Свой Круг MVP (v1.0). It serves as the authoritative source for development teams, designers, and QA to understand what needs to be built, why it matters, and how success will be measured.

### Scope

**In scope (MVP - 12 weeks):**
- Mobile app (iOS + Android) with core loyalty features
- Backend API with 2 CRM integrations (YCLIENTS, Iiko)
- QR wallet for bonus accrual and redemption
- Status system (Insider/VIP/Elite/Inner Circle)
- Basic cross-promo chains (A→B)
- Admin panels for businesses and super

admin
- Transaction history and analytics foundation
- 5 initial partner businesses

**Out of scope (Post-MVP v1.5/v2.0):**
- Referral program (v1.5)
- Push notifications system (v1.5)
- Event constructor with voting (v2.0)
- AI recommendations engine (v2.0)
- Social feed (v2.0)
- Payment gateway integration (v2.0)
- Additional CRM integrations beyond YCLIENTS + Iiko

---

## 🎯 Product Vision & Goals

### Vision Statement

Create Russia's first premium women's loyalty ecosystem where every purchase unlocks value across an entire network of curated businesses, transforming isolated transactions into an interconnected community of trusted brands and engaged clients.

### Strategic Goals

1. **Client Acquisition & Engagement (Primary)**
   - Objective: Achieve 200+ registered users by end of MVP (Week 12)
   - Key Results:
     - 50 beta testers active by Week 10
     - 150 public registrations in Weeks 11-12
     - 10% cross-purchase rate (2+ businesses in 60 days)
   - Timeline: Weeks 1-12 (MVP)

2. **Business Partner Network (Primary)**
   - Objective: Onboard and integrate 5 premium partner businesses
   - Key Results:
     - All 5 partners confirmed and contracts signed by Week 2
     - 2 CRM integrations (YCLIENTS + Iiko) live by Week 6
     - CSV uploader operational for 3 remaining partners by Week 8
   - Timeline: Weeks 1-8

3. **Technical Foundation (Primary)**
   - Objective: Build scalable, performant platform ready for 500+ users in v1.5
   - Key Results:
     - API response time <100ms (p95)
     - App load time <2s
     - 0 critical bugs in production
     - 99%+ integration sync success rate
   - Timeline: Continuous through MVP

4. **Cross-Promo Mechanics (Secondary)**
   - Objective: Validate that cross-business promotions drive new client discovery
   - Key Results:
     - 3-5 A→B cross-promo chains active
     - 30%+ conversion rate on cross-promo coupons
     - Measure Win-Win matrix for top 3 business pairs
   - Timeline: Weeks 7-12

---

## 👥 User Personas & Needs

### Primary User: Premium Women Client (Ekaterina, 38)

**Needs:**
- **Unified rewards:** One app, one QR code, one balance across all businesses (vs. 8 separate apps currently)
- **Visible status:** Clear recognition as VIP/Elite client with tangible benefits (priority booking, exclusive events)
- **Curated discovery:** Trustworthy recommendations for new premium services within ecosystem

**Current workflow (frustrating):**
1. Visit Business A → Ask "Do you have a loyalty program?" → Download separate app
2. Forget to show loyalty card at checkout → Miss 500₽ bonuses
3. 2 months later → Remember app → Find bonuses expired
4. Repeat for Businesses B, C, D, E (5-8 different apps/cards)

**Desired workflow (with Свой Круг):**
1. One-time registration → QR wallet added to Apple Wallet
2. Checkout at any partner → Show QR → Automatic 5-10% cashback
3. Receive notification: "Spent 5,000₽ at Skinerica → Get 20% off at Лисичкино!"
4. Try new business with confidence (ecosystem member status = quality signal)

---

### Secondary User: Premium Business Owner (Dmitry, owner of Миндаль salon)

**Needs:**
- **Low-cost client acquisition:** Get qualified new clients through cross-promo (vs. 10K₽ CAC on Instagram ads)
- **Churn prevention:** Automated alerts when VIP clients haven't visited in 45 days
- **Data insights:** RFM segmentation and actionable recommendations (vs. raw CRM data)

**Current workflow:**
1. Spend 300K₽/month on Instagram/Google ads → 30-50 new bookings
2. Convert only 15% to repeat clients (85% one-timers)
3. Manually call clients who ghosted → Too late, they already switched salons
4. Run random discounts hoping to fill slow periods
5. Export data to Excel for basic reporting

**Desired workflow:**
1. Receive 20-30 new clients/month via cross-promo (cost: 2-3K₽ bonus expense each)
2. Automated alert: "5 VIP clients at risk → Send 15% return offer"
3. Dashboard shows: Champions (15%), Loyal (30%), At Risk (20%), Lost (10%)
4. Collaborate with Stim Center + Skinerica on package deal targeting VIP+ clients
5. Real-time analytics: CAC, LTV, retention rate, cross-promo ROI

---

## 🏗️ Feature Overview

### Feature Breakdown by Module

---

#### Module 1: Mobile App (Frontend) - 68 Functions

**Priority:** CRITICAL  
**Status:** MVP Sprint 1-4  
**Owner:** Frontend Team

**Purpose:**
React Native mobile app (iOS + Android) providing client-facing interface for registration, QR wallet, transaction history, business catalog, status progression, and event discovery.

**Key Features:**

##### Feature 1.1: Authentication & Onboarding

**Description:**
Phone number-based registration with SMS verification, creating frictionless signup flow optimized for mobile. Includes welcome video (30s) explaining Свой Круг value proposition and 3-slide benefit showcase.

**User benefit:**
New members can join in <60 seconds without email/password complexity, immediately understanding what they gain from membership.

**Acceptance criteria:**
- [ ] Phone input validates Russian mobile format (+7 XXX XXX-XX-XX)
- [ ] SMS code arrives within 30 seconds, expires after 5 minutes
- [ ] Welcome video autoplays on first app open (skippable after 5s)
- [ ] User completes profile (name, email, birthday) before accessing app
- [ ] Referral code input (optional) tracked for future rewards

**Dependencies:**
- SMS.ru API integration for code delivery
- Firebase Analytics to track signup funnel drop-off

**Effort estimate:** Medium (8-12 hours / 5-8 story points)

**Priority:** Must-have (MVP Week 1-2)

---

##### Feature 1.2: QR Wallet

**Description:**
Digital wallet displaying unique QR code for each member, along with bonus balance, status badge (Insider/VIP/Elite/Inner Circle), and user ID. QR code shown in large format optimized for business POS scanning.

**User benefit:**
One QR code replaces 5-8 separate loyalty cards, bonus accrual is automatic and instant, never forget card at checkout again.

**Acceptance criteria:**
- [ ] QR code generates unique identifier (UUID) per user
- [ ] Screen brightness auto-increases to 100% when wallet opened
- [ ] "Keep screen on" prevents auto-lock while QR displayed
- [ ] Bonus balance updates in real-time (<5s after transaction scanned)
- [ ] Status badge visually distinct (color-coded: blue/purple/gold/platinum)
- [ ] Add to Apple Wallet / Google Pay integration functional

**Dependencies:**
- Backend API: `POST /api/transactions` (when business scans QR)
- Backend API: `GET /api/users/me/balance`

**Effort estimate:** Medium (10-14 hours / 8-13 story points)

**Priority:** Must-have (MVP Week 2-3)

---

##### Feature 1.3: Transaction History

**Description:**
Complete history of all purchases across all partner businesses, filterable by business, category, date range. Each transaction shows business name, amount spent, bonuses earned, date/time.

**User benefit:**
Full transparency on all purchases and bonus accruals, ability to dispute incorrect transactions, track spending patterns.

**Acceptance criteria:**
- [ ] Displays last 100 transactions by default (infinite scroll for more)
- [ ] Filter by business (dropdown with all 5 partners)
- [ ] Filter by date range (last 7/30/90 days or custom range)
- [ ] Each transaction shows: business logo, name, amount, bonuses earned, timestamp
- [ ] Tapping transaction opens detail modal (receipt data if available)
- [ ] "Export to PDF" generates downloadable transaction report

**Dependencies:**
- Backend API: `GET /api/transactions?user_id=X&filters=Y`

**Effort estimate:** Small (6-8 hours / 5 story points)

**Priority:** Must-have (MVP Week 3-4)

---

##### Feature 1.4: Business Catalog

**Description:**
Scrollable catalog of all 5 partner businesses with category tags (Beauty, Health, Food, Wellness), ratings (if available), current active offers, and deep links to booking.

**User benefit:**
Discover new businesses within ecosystem, see which ones have active promotions, one-tap to book services.

**Acceptance criteria:**
- [ ] Displays all 5 partners with logo, name, 1-line description
- [ ] Category filters: All / Beauty / Health / Food / Wellness
- [ ] "Active Offer" badge if business has live cross-promo
- [ ] Tapping business opens detail page (description, services, photos, map)
- [ ] "Book Now" button deep links to YCLIENTS/Iiko booking (if integrated)
- [ ] "Get Directions" opens Google Maps navigation

**Dependencies:**
- Backend API: `GET /api/businesses`
- Backend API: `GET /api/businesses/:id/offers`

**Effort estimate:** Medium (8-10 hours / 5-8 story points)

**Priority:** Should-have (MVP Week 4-5)

---

#### Module 2: Loyalty System - 45 Functions

**Priority:** CRITICAL  
**Status:** MVP Sprint 2-4  
**Owner:** Backend Team

**Purpose:**
Core loyalty mechanics including bonus accrual (5-10% cashback), status calculation (4 tiers based on spend + category diversity), coupon management (5 types), and bonus expiration rules.

**Key Features:**

##### Feature 2.1: Bonus Accrual & Balance

**Description:**
Automatic bonus calculation upon transaction: 5% for Insider, 7% for VIP, 10% for Elite/Inner Circle. Bonuses credited to user balance within 15 minutes, usable across all partner businesses.

**User benefit:**
Immediate, transparent cashback on every purchase, higher tiers unlock better rewards, creating motivation to increase ecosystem spend.

**Acceptance criteria:**
- [ ] Transaction of 1,000₽ → Insider gets 50₽, VIP gets 70₽, Elite gets 100₽ bonuses
- [ ] Bonuses credited within 15 minutes of transaction (async Celery task)
- [ ] Balance displayed as: Available (usable now) + Pending (processing)
- [ ] 1.5x multiplier applied for first purchase in new category
- [ ] Special promotions (2x/3x bonuses) override base rate if active

**Dependencies:**
- Transaction creation API
- Celery task queue for async bonus calculation
- Redis caching for user balance (< 1ms lookup)

**Effort estimate:** Large (16-20 hours / 13 story points)

**Priority:** Must-have (MVP Week 2-3)

---

##### Feature 2.2: Status Progression System

**Description:**
Automated calculation of user status tier (Insider/VIP/Elite/Inner Circle) based on 12-month rolling window of total spend + number of unique categories purchased from.

**User benefit:**
Gamified progression path creates aspirational goals ("Only 5,000₽ more to VIP!"), rewards loyalty with tangible benefits (higher cashback, event access).

**Acceptance criteria:**
- [ ] Insider: Default status on registration + 1 purchase
- [ ] VIP: ≥30,000₽ spent + ≥3 categories (in last 12 months)
- [ ] Elite: ≥100,000₽ spent + ≥5 categories OR top 1% of users
- [ ] Inner Circle: ≥200,000₽ spent OR by platform invitation
- [ ] Status recalculated daily (Celery cron job)
- [ ] User sees progress bar: "3,500₽ to VIP" or "1 more category needed"

**Dependencies:**
- ClickHouse analytics for 12-month rolling window queries
- PostgreSQL user status table for current tier

**Effort estimate:** Large (14-18 hours / 13 story points)

**Priority:** Must-have (MVP Week 3-4)

---

##### Feature 2.3: Coupon System (5 Types)

**Description:**
Five coupon types created by businesses: (1) Simple Discount (% or fixed), (2) Bonus Cashback (2x/3x multiplier), (3) Cross-Promo (buy at A → get coupon for B), (4) Package Deal (bundle from 2-5 businesses), (5) Gift with Purchase (minimum spend → free item).

**User benefit:**
Receive personalized offers based on purchase history, discover new businesses through cross-promo, save money on packages.

**Acceptance criteria:**
- [ ] Each coupon has: title, description, type, value, valid_from, valid_until, business_id, min_purchase
- [ ] User sees "My Coupons" tab with Active / Used / Expired filters
- [ ] Tapping coupon shows: terms, expiration countdown, "Activate" button
- [ ] Activated coupon generates unique code for POS entry
- [ ] Cross-promo coupon auto-appears after trigger purchase (within 5 min)
- [ ] Expired coupons removed from "Active" tab after 24 hours

**Dependencies:**
- Backend API: `GET /api/users/me/coupons`
- Backend API: `POST /api/coupons/:id/activate`
- Celery task for cross-promo trigger detection

**Effort estimate:** Very Large (20-24 hours / 21 story points)

**Priority:** Must-have (MVP Week 4-6)

---

#### Module 3: CRM Integrations - 20 Functions

**Priority:** CRITICAL  
**Status:** MVP Sprint 5-6  
**Owner:** Backend Integration Team

**Purpose:**
Bi-directional sync with partner CRM systems (YCLIENTS for Миндаль salon, Iiko for Лисичкино gastromarket) to automatically import transactions, eliminating manual entry by businesses.

**Key Features:**

##### Feature 3.1: YCLIENTS Integration

**Description:**
Connect to YCLIENTS API (used by Миндаль beauty salon) to pull transaction data every 15 minutes, match phone numbers to Свой Круг members, create transactions with bonus accrual.

**User benefit:**
Seamless experience - client visits Миндаль, pays through YCLIENTS POS, bonuses appear in app within 15 min without any manual steps.

**Acceptance criteria:**
- [ ] API credentials (token, salon ID) configurable in admin panel
- [ ] Celery task runs every 15 min: fetch new transactions since last sync
- [ ] Match YCLIENTS phone → Свой Круг user (handle +7 vs 8 prefix variations)
- [ ] Create transaction record with: amount, business_id, timestamp, external_id
- [ ] Trigger bonus accrual Celery task
- [ ] Log sync errors (unmatched phone, API timeout) for manual review
- [ ] Admin dashboard shows: last sync time, success rate, error count

**Dependencies:**
- YCLIENTS API access (Миндаль provides credentials)
- Phone normalization utility (handle format variations)
- Duplicate detection (check external_id to avoid double-crediting)

**Effort estimate:** Very Large (24-30 hours / 21 story points)

**Priority:** Must-have (MVP Week 5-6)

---

##### Feature 3.2: Iiko Integration

**Description:**
Connect to Iiko API (restaurant management system used by Лисичкино) to sync food/beverage purchases, applying 5-10% cashback on dining experiences.

**User benefit:**
Earn bonuses on restaurant visits automatically, unlock cross-promo offers like "Spent 3,000₽ at Лисичкино → Get 15% off at Skinerica cosmetology."

**Acceptance criteria:**
- [ ] API credentials configurable per business
- [ ] Poll Iiko API every 15 min for new closed checks
- [ ] Match customer phone to Свой Круг user
- [ ] Handle partial payments (only credit full transaction when payment complete)
- [ ] Create transaction + trigger bonus accrual
- [ ] Retry failed requests (max 3 attempts with exponential backoff)
- [ ] Alert admin if sync fails for >1 hour

**Dependencies:**
- Iiko API documentation and test environment
- Лисичкино provides production credentials

**Effort estimate:** Very Large (24-30 hours / 21 story points)

**Priority:** Must-have (MVP Week 5-6)

---

##### Feature 3.3: CSV Uploader (Fallback)

**Description:**
Web-based CSV upload interface for businesses without API access (Skinerica, Стим Центр, Миллениум). Business admin uploads CSV with columns: phone, amount, date, service/item description.

**User benefit:**
All 5 partners can participate in ecosystem even if their CRM doesn't have API, ensuring complete transaction coverage.

**Acceptance criteria:**
- [ ] CSV template downloadable (columns: phone, amount, date, description)
- [ ] Upload validates: phone format, amount is numeric, date is valid
- [ ] Shows preview table before confirming import
- [ ] Batch import creates transactions (max 1000 rows per upload)
- [ ] Duplicate detection (same phone + amount + date = likely duplicate, flag for review)
- [ ] Admin sees import history (who uploaded, when, how many rows, status)

**Dependencies:**
- File upload handling (limit to 5MB, .csv only)
- Background job for large imports (Celery)

**Effort estimate:** Medium (12-16 hours / 13 story points)

**Priority:** Must-have (MVP Week 6-8)

---

#### Module 4: Admin Panels - 22 Functions (Business) + 18 Functions (Super Admin)

**Priority:** CRITICAL  
**Status:** MVP Sprint 4-8  
**Owner:** Backend + Frontend Teams

**Purpose:**
Two admin interfaces: (1) Business Admin Panel for salon/restaurant owners to view their clients, manually enter transactions, see analytics; (2) Super Admin Panel for platform team to manage all businesses, users, moderate content.

**Key Features:**

##### Feature 4.1: Business Admin - Client List

**Description:**
Business owner logs in, sees list of all Свой Круг members who have purchased from their business, with filters by status (VIP/Elite), last visit date, total spent.

**User benefit:**
Understand which ecosystem members are your clients, identify VIPs for special treatment, see who hasn't visited recently (churn risk).

**Acceptance criteria:**
- [ ] Login with email + password (separate from client app auth)
- [ ] Client list shows: name, phone (masked), status badge, last purchase date, total spent (lifetime)
- [ ] Filter by status: All / VIP / Elite / Inner Circle
- [ ] Filter by recency: Visited in last 7/30/90 days or Not visited in 30+ days
- [ ] Click client → detail modal (full purchase history at this business)
- [ ] "Export to CSV" downloads client list for email campaigns

**Dependencies:**
- Backend API: `GET /api/admin/businesses/:id/clients`
- Authentication middleware (JWT for business admins)

**Effort estimate:** Medium (10-12 hours / 8 story points)

**Priority:** Must-have (MVP Week 4-5)

---

##### Feature 4.2: Business Admin - Manual Transaction Entry

**Description:**
For walk-in clients or when POS fails, business admin can manually enter transaction (scan QR or input phone number, enter amount, submit).

**User benefit:**
Ensures no client is left without bonuses due to technical issues, backup method if API sync fails.

**Acceptance criteria:**
- [ ] QR scanner activated via webcam (or phone camera if mobile admin panel)
- [ ] Alternatively, input phone number manually
- [ ] Amount field validates: must be ≥ 50₽ (minimum transaction)
- [ ] Optional: service/item description
- [ ] Submit → creates transaction, triggers bonus accrual
- [ ] Confirmation screen shows: "500₽ transaction created, client earned 50₽ bonuses"
- [ ] Transaction appears in client's history within 30 seconds

**Dependencies:**
- Backend API: `POST /api/admin/transactions`
- QR code scanning library (jsQR or react-qr-reader)

**Effort estimate:** Medium (8-12 hours / 8 story points)

**Priority:** Must-have (MVP Week 5-6)

---

##### Feature 4.3: Super Admin - Business Management

**Description:**
Platform super admin can add new businesses, edit business details (name, category, logo, contact info), activate/deactivate businesses.

**User benefit:**
Centralized control over ecosystem, easy onboarding of new partners in v1.5, ability to pause problematic businesses without code changes.

**Acceptance criteria:**
- [ ] "Add Business" form: name, category, logo upload, address, phone, email, CRM type
- [ ] Edit business details (changes reflected in client app within 5 min via cache invalidation)
- [ ] Toggle "Active" status (inactive businesses hidden from client catalog)
- [ ] "Danger Zone": Delete business (soft delete, retains transaction history)
- [ ] Audit log tracks all business changes (who, what, when)

**Dependencies:**
- Backend API: `POST /api/admin/businesses`
- Image upload to S3 (Yandex Object Storage)

**Effort estimate:** Medium (10-14 hours / 8-13 story points)

**Priority:** Must-have (MVP Week 6-8)

---

## 📊 Success Metrics

### Product Metrics

**Engagement (Client-side):**
- Active users (opened app in last 7 days): Target 60% of registered users by Week 12
- QR wallet opens per week: Target 1.5x per active user (users showing QR when shopping)
- Cross-purchase rate: 10% of users buy from 2+ businesses in first 60 days (baseline for NSM)

**Engagement (Business-side):**
- Business admin logins per week: Target 3-4x per business (checking analytics, entering transactions)
- CSV uploads per week: Target 1-2x per non-integrated business (Skinerica, Стим, Миллениум)
- Manual transactions entered: <10% of total (most should auto-sync via YCLIENTS/Iiko)

**Performance:**
- API response time: <100ms (p50), <200ms (p95), <500ms (p99)
- App load time: <2s on 4G, <1s on WiFi (p95)
- Integration sync success rate: >99% (exclude business-side outages)
- App crash rate: <1% (per session)

**Business:**
- Total GMV (gross merchandise value): Track total transaction volume through platform
- CAC for businesses (through cross-promo): Target <3,000₽ per acquired client (vs. 10K+ via ads)
- Client retention: Track 30-day, 60-day, 90-day retention cohorts

### How we'll measure:

- **Client metrics:** Firebase Analytics + Amplitude (events: screen_view, qr_opened, transaction_created, cross_promo_used)
- **Business metrics:** Admin panel usage logs (login_count, csv_upload_count, manual_transaction_count)
- **Performance:** Prometheus (API latency histograms), Sentry (error rate, crash rate), New Relic (app load time)
- **Business outcomes:** PostgreSQL queries (GMV, CAC, retention cohorts), ClickHouse (RFM, Win-Win matrix)

---

## 🚫 Non-Functional Requirements

### Performance

- Page load: <2s on mobile (React Native app load time)
- API response: <100ms (p95) for all read endpoints, <500ms for write endpoints
- Database queries: <50ms for simple lookups, <200ms for analytics queries
- Concurrent users: Support 500 concurrent users without degradation (load test in Sprint 8)

### Security

- All data encrypted in transit (TLS 1.3)
- User passwords hashed with bcrypt (cost factor 12)
- JWT tokens: 1-hour access token, 30-day refresh token, invalidated on logout
- Rate limiting: 100 req/min per IP, 1000 req/hour per authenticated user
- PII (phone, email) encrypted at rest in PostgreSQL
- RBAC: Users can only access their own data, business admins only their business data, super admins see all
- 152-ФЗ compliance: Data stored in Russia (Yandex Cloud ru-central1), user consent on signup

### Scalability

- Horizontal scaling: Backend API stateless, can add instances behind load balancer
- Database: PostgreSQL 16 with read replicas (if needed in v1.5), ClickHouse for analytics offload
- Caching: Redis for frequently accessed data (user balance, business list, coupon counts)
- CDN: Static assets (logos, images) served via Yandex CDN (future optimization)

### Accessibility

- Mobile app: VoiceOver (iOS) and TalkBack (Android) compatibility for key flows (registration, QR wallet, transaction history)
- Minimum tap target size: 44x44 points (Apple HIG compliance)
- Color contrast: WCAG 2.1 Level AA (4.5:1 for body text, 3:1 for large text)
- Font scaling: Support iOS/Android system font size preferences

### Browser/Platform Support

- **iOS:** 14.0+ (supports iPhone 6s and newer, ~95% market coverage in Russia)
- **Android:** 10.0+ (API level 29, ~85% market coverage)
- **Admin panels (web):** Chrome 111+, Firefox 128+, Safari 16.4+, Edge 111+

---

## ⚠️ Constraints & Assumptions

### Technical Constraints

- React Native 0.81 (new architecture), may require native module adjustments
- FastAPI 0.121.2 requires Pydantic v2 (breaking change from v1)
- Redis 8.2 has licensing change (RSALv2/SSPLv1/AGPLv3) - verify Yandex Cloud support
- YCLIENTS API rate limit: 60 req/min (requires request throttling)

### Business Constraints

- 12-week MVP timeline is fixed (launch by 2026-02-09)
- 5 initial partners confirmed, no additional partners until v1.5
- Budget: ~20,300₽/month for Yandex Cloud (limits instance sizes)
- Team availability: [TO BE CONFIRMED]

### Assumptions

- All 5 partners will provide CRM API access or accept CSV uploads by Week 2
- 50 beta testers can be recruited from partners' existing client bases
- SMS delivery (SMS.ru) has <5% failure rate
- User phones are Russian mobile numbers (+7 XXX XXX-XX-XX format)
- Businesses have webcams or mobile devices for QR scanning
- Internet connectivity: App requires online connection (no offline mode in MVP)

---

## 🔄 Future Considerations

### Phase 2 Features (v1.5 - 3 months after MVP)

- Referral program: Users invite friends, both get 1,000₽ bonuses
- Push notifications: Bonus accrual alerts, cross-promo coupon arrivals, event reminders
- Basic events: Calendar, registration, QR check-in (no voting/constructor yet)
- +3 new businesses (expand from 5 → 8 partners)
- AMO CRM integration (Стим Центр), МИС Renovatio integration (Миллениум)

### Long-term Vision (v2.0 - 6 months after v1.5)

- Event constructor: VIP/Elite can propose event ideas
- Weighted voting: Status-based voting power (Insider 1x, VIP 2x, Elite 3x, Inner 5x)
- AI recommendations: Personalized business suggestions based on purchase history + RFM
- Social feed: Members share experiences, photos from events
- Marketplace: Book services directly in app (not just deep links)

---

## 📚 Related Documentation

- [Project Essence](./00_PROJECT_ESSENCE.md) - Vision and problem statement
- [Roadmap](./02_ROADMAP.md) - 12-week timeline with milestones
- [Tech Stack](./03_TECH_STACK.md) - Verified November 2025 technologies
- [Architecture](./04_ARCHITECTURE.md) - System design and data models
- [Module Requirements](../requirements/) - Detailed specs for all 15 modules

---

**Approval:**
- [ ] Product Owner: _______________
- [ ] Tech Lead: _______________
- [ ] Design Lead: _______________

**Last Updated:** 2025-11-17
