# Module 10: Superadmin Ecosystem Panel - Requirements

**Module ID:** MOD-10
**Total Functions:** 18
**Priority:** P1 (Important - MVP)
**Dependencies:** All modules (platform-wide administration)
**Tech Stack:** React 18 (web admin), FastAPI 0.121.2, PostgreSQL 16.11, ClickHouse 25.8 LTS

---

## 📋 Module Overview

Superadmin panel provides platform-wide administration for ecosystem management: add/edit businesses, manage users, moderate content (event proposals, comments), monitor system analytics (NSM, revenue, Win-Win matrix), and configure platform settings. Accessible only to superadmin role.

**Key Subsystems:**
- 10.1 Business Management (5 functions): Add, edit, deactivate businesses, configure CRM
- 10.2 User Management (4 functions): View, search, change status, ban/unban
- 10.3 Content Moderation (4 functions): Approve/reject cross-promo, events, comments
- 10.4 System Analytics (5 functions): Dashboard, Win-Win matrix, cohort analysis, budget monitoring

---

## 10.1 Business Management (5 functions)

### User Story 10.1.1: Add New Partner Business
**As a** superadmin
**I want to** add new partner businesses to the ecosystem
**So that** members have more options

**Acceptance Criteria:**
```gherkin
Scenario: Add business via admin panel
  Given I am logged in as superadmin
  When I go to Admin Panel → "Businesses" → "Add New"
  Then I see form with fields:
    - Business name (required)
    - Category (dropdown: Красота, Косметология, Стоматология, etc.)
    - Description (rich text editor)
    - Logo upload (JPG/PNG, max 2MB)
    - Address, phone, website
    - Operating hours
    - Base cashback rate (5-10%)
    - CRM type (dropdown: YCLIENTS, Iiko, 1С, AMO CRM, Renovatio, CSV, None)
    - Is medical business (checkbox - врачебная тайна)
  And I fill fields and click "Create Business"
  Then business is created with status="pending_activation"
  And I see "Business added successfully"
```

**Technical Requirements:**
- API endpoint: `POST /api/v1/admin/businesses`
- Image upload to Yandex Object Storage
- Default cashback rate: 5% (Insider tier)
- New business starts inactive until superadmin activates

---

### User Story 10.1.2: Edit Business Details
**As a** superadmin
**I want to** edit existing business information
**So that** data stays current

**Acceptance Criteria:**
```gherkin
Scenario: Edit business
  Given I am on Businesses list
  When I click "Edit" on Миндаль
  Then I see edit form pre-filled with current data
  And I can modify any field
  And I click "Save Changes"
  Then business is updated
  And changes reflect immediately in mobile app (after cache refresh)
```

---

### User Story 10.1.3: Deactivate/Activate Business
**As a** superadmin
**I want to** deactivate businesses that left the ecosystem
**So that** they no longer appear in app

**Acceptance Criteria:**
```gherkin
Scenario: Deactivate business
  Given business "Миндаль" is active
  When I click "Deactivate"
  Then business.status changes to "inactive"
  And business no longer appears in mobile app catalog
  And existing transactions remain (archived)

Scenario: Reactivate business
  Given business is inactive
  When I click "Activate"
  Then business returns to active state
  And appears in app again
```

---

### User Story 10.1.4-10.1.5: Configure CRM Integration & View Stats
**As a** superadmin
**I want to** configure CRM integrations for businesses
**So that** transactions sync automatically

**Acceptance Criteria:**
```gherkin
Scenario: Set up CRM integration
  Given I am editing business "Миндаль"
  When I select CRM type: "YCLIENTS"
  And I enter API credentials (or delegate to business owner)
  And I click "Test Connection"
  Then connection is tested
  And if successful: "✅ Integration configured"

Scenario: View business statistics
  Given I am on business details page
  When I scroll to "Statistics" section
  Then I see:
    - Total members who purchased: 245
    - Total transactions: 1,230
    - Total revenue: 5,450,000₽
    - Ecosystem revenue share: 15%
    - Average transaction: 4,430₽
    - Last 30 days activity chart
```

---

## 10.2 User Management (4 functions)

### User Story 10.2.1-10.2.2: View and Search Users
**As a** superadmin
**I want to** view all users and search by filters
**So that** I can manage the member base

**Acceptance Criteria:**
```gherkin
Scenario: View users list
  Given I am on Admin Panel → "Users"
  When page loads
  Then I see table with columns:
    - Name, Phone, Email
    - Status (Insider/VIP/Elite/Inner Circle)
    - Total spent (12 months)
    - Categories visited
    - Registration date
    - Actions (View, Edit, Ban)
  And I see pagination (50 users per page)

Scenario: Search users
  Given I want to find specific user
  When I enter search query: "Мария"
  Or I filter by status: "VIP"
  Or I filter by registration date: "Last 30 days"
  Then results are filtered accordingly
```

---

### User Story 10.2.3: Manually Change User Status
**As a** superadmin
**I want to** manually override user status
**So that** I can grant Inner Circle status or fix errors

**Acceptance Criteria:**
```gherkin
Scenario: Grant Inner Circle status
  Given user is Elite but I want to grant Inner Circle
  When I click "Edit" → "Change Status" → "Inner Circle"
  And I enter reason: "Top contributor, invited by founder"
  Then user.status changes to "Inner Circle"
  And status_history records manual change
  And user receives push notification
```

---

### User Story 10.2.4: Ban/Unban User
**As a** superadmin
**I want to** ban users who violate terms
**So that** they can't access the platform

**Acceptance Criteria:**
```gherkin
Scenario: Ban user
  Given user violated terms of service
  When I click "Ban User"
  And I enter reason: "Fraudulent activity"
  Then user.is_banned = TRUE
  And user is logged out immediately (JWT invalidated)
  And user cannot log in (receives error: "Account suspended")

Scenario: Unban user
  Given user was banned
  When I click "Unban User"
  Then user.is_banned = FALSE
  And user can log in again
```

---

## 10.3 Content Moderation (4 functions)

### User Story 10.3.1-10.3.2: Moderate Cross-Promo & Bundles
**As a** superadmin
**I want to** approve/reject cross-promo proposals
**So that** only quality offers go live

**Acceptance Criteria:**
```gherkin
Scenario: Approve cross-promo chain
  Given business A proposed chain "Buy at A → 20% off at B"
  And business B approved
  When I review proposal in "Pending Cross-Promos"
  And I click "Approve"
  Then cross_promo.status = "approved"
  And chain goes live immediately
  And both businesses receive notification

Scenario: Reject cross-promo
  Given proposal has unrealistic discount (90% off)
  When I click "Reject"
  And I enter reason: "Discount too high, not sustainable"
  Then proposal is rejected
  And proposer receives notification with reason
```

---

### User Story 10.3.3: Moderate Event Proposals
**As a** superadmin
**I want to** approve/reject member event proposals
**So that** only suitable events are funded

**Acceptance Criteria:**
```gherkin
Scenario: Approve event proposal
  Given VIP member proposed "Wine Tasting Evening"
  And voting ended with 75% approval
  When I review proposal
  And I check budget availability (VIP category has funds)
  And I click "Approve & Allocate Budget"
  Then event.status = "approved"
  And budget is allocated from VIP category
  And proposer receives notification: "Your event is approved!"
  And event appears in Events Hub

Scenario: Reject event proposal
  Given proposal is inappropriate or budget insufficient
  When I click "Reject"
  And I enter reason
  Then proposer receives notification with feedback
```

---

### User Story 10.3.4: Moderate Comments & Reviews
**As a** superadmin
**I want to** moderate user comments on events/businesses
**So that** content stays appropriate

**Acceptance Criteria:**
```gherkin
Scenario: Review flagged comment
  Given user flagged comment as inappropriate
  When I view "Flagged Content" queue
  Then I see comment with context
  And I can:
    - Approve (no action needed)
    - Delete (removes comment)
    - Ban user (if severe violation)

Scenario: Delete inappropriate comment
  Given comment contains offensive language
  When I click "Delete Comment"
  Then comment is removed from platform
  And commenter receives warning notification
```

---

## 10.4 System Analytics (5 functions)

### User Story 10.4.1: Ecosystem Dashboard
**As a** superadmin
**I want to** see high-level ecosystem metrics
**So that** I monitor platform health

**Acceptance Criteria:**
```gherkin
Scenario: View main dashboard
  Given I log in as superadmin
  When I open dashboard
  Then I see KPIs:
    - Total members: 2,450 (↑ 12% from last month)
    - Active members (30 days): 1,850 (76%)
    - North Star Metric (NSM): 23% (% with 2+ categories in 60 days)
    - Total GMV (30 days): 45,000,000₽
    - Ecosystem commission (if applicable): 450,000₽
    - Partner businesses: 15
    - Events this month: 12
    - Cohort retention (Month 3): 65%
  And I see charts:
    - Monthly GMV trend (12 months)
    - Member growth (12 months)
    - NSM trend (12 months)
```

**Technical Requirements:**
- Query ClickHouse for aggregated metrics (fast OLAP queries)
- Cache dashboard data for 15 minutes (Redis)
- Export dashboard as PDF for board meetings

---

### User Story 10.4.2: Win-Win Matrix (All Businesses)
**As a** superadmin
**I want to** see Win-Win matrix for entire ecosystem
**So that** I identify best cross-promo opportunities

**Acceptance Criteria:**
```gherkin
Scenario: View Win-Win matrix
  Given I go to Analytics → "Win-Win Matrix"
  When page loads
  Then I see heatmap matrix:
    Rows: Source businesses (where customer came from)
    Columns: Destination businesses (where customer went)
    Values: Conversion rate (% of source customers who tried destination)
  And cells are color-coded:
    - Green (40%+): Strong connection
    - Yellow (20-40%): Moderate connection
    - Red (<20%): Weak connection
  And I can click cell to see details:
    - Skinerica → Миндаль: 45% conversion (120 customers)
    - Миндаль → Лисичкино: 32% conversion (85 customers)

Scenario: Identify top opportunities
  Given I view matrix
  When I click "Top Opportunities"
  Then I see recommended cross-promo chains:
    1. Skinerica ↔ Миндаль (45% mutual conversion)
    2. Миндаль ↔ Лисичкино (32% conversion)
    3. Стим Центр ↔ Миллениум (28% conversion)
```

**Technical Requirements:**
- Query ClickHouse: `SELECT source_business, dest_business, COUNT(*) / total * 100 FROM cross_purchases`
- Heatmap visualization: use D3.js or Chart.js
- Update matrix daily (Celery Beat task)

---

### User Story 10.4.3: Top Cross-Promo Chains by Conversion
**As a** superadmin
**I want to** see top-performing cross-promo chains
**So that** I promote successful patterns

**Acceptance Criteria:**
```gherkin
Scenario: View top chains
  Given I go to Analytics → "Top Cross-Promo Chains"
  When page loads
  Then I see ranked list:
    1. Skinerica → Миндаль (20% discount) - 45% conversion, 120 uses
    2. Миндаль → Лисичкино (500₽ bonuses) - 38% conversion, 95 uses
    3. Лисичкино → Skinerica (double bonuses) - 35% conversion, 80 uses
  And I see metrics for each chain:
    - Impressions (coupons generated)
    - Activation rate (coupons activated)
    - Redemption rate (coupons used)
    - ROI (revenue generated vs. discount cost)
```

---

### User Story 10.4.4: Monitor Events Budget
**As a** superadmin
**I want to** monitor events budget health
**So that** funding is sustainable

**Acceptance Criteria:**
```gherkin
Scenario: View budget dashboard
  Given I go to Analytics → "Events Budget"
  When page loads
  Then I see:
    - Total balance: 100,000₽
    - Monthly accrual rate: +25,000₽/month (2% of 1.25M GMV)
    - Monthly spending rate: -20,000₽/month (avg 4 events × 5K each)
    - Runway: 5 months at current burn rate
    - Category balances:
      * Open: 30,000₽ (30%)
      * VIP: 40,000₽ (40%)
      * Elite: 20,000₽ (20%)
      * Reserve: 10,000₽ (10%)
  And I see alerts:
    - "⚠️ Elite budget low (2 events remaining)"
    - "✅ VIP budget healthy (4+ events)"
```

---

### User Story 10.4.5: Cohort Analysis
**As a** superadmin
**I want to** analyze member cohorts
**So that** I understand retention patterns

**Acceptance Criteria:**
```gherkin
Scenario: View cohort retention table
  Given I go to Analytics → "Cohort Analysis"
  When page loads
  Then I see cohort retention table:
    | Cohort | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 |
    | Nov 2024 | 100% | 75% | 68% | 65% | 55% |
    | Dec 2024 | 100% | 78% | 70% | 67% | - |
    | Jan 2025 | 100% | 80% | 72% | - | - |
  And I see insights:
    - Average Month 3 retention: 65%
    - Best cohort: January 2025 (80% M1 retention)
    - Worst cohort: November 2024 (75% M1 retention)
    - Recommendation: "Improve onboarding to boost M1 retention"
```

**Technical Requirements:**
- Cohort defined by registration month
- Retention = % of cohort with at least 1 transaction in month N
- Query ClickHouse for cohort data (complex SQL with window functions)

---

## 📊 Technical Requirements

### Admin Panel Stack
- **Frontend:** React 18 + TypeScript + Ant Design (admin UI library)
- **Backend:** FastAPI endpoints under `/api/v1/admin/*` (RBAC enforced)
- **Database:** PostgreSQL (OLTP), ClickHouse (OLAP analytics)
- **Authentication:** JWT with `role='superadmin'` required

### RBAC Enforcement
- All admin endpoints check: `require_role('superadmin')`
- Admin actions logged in `audit_logs` table (Module 13)
- Sensitive actions (ban user, delete business) require reason + confirmation

### Performance
- Dashboard load: <1 second (cached metrics)
- Win-Win matrix: <3 seconds (ClickHouse query)
- User search: <500ms (PostgreSQL full-text search)
- Cohort analysis: <5 seconds (pre-computed daily)

---

## 🔄 Dependencies

- **All Modules:** Superadmin has access to all platform data
- **Module 13 (Security):** RBAC enforcement, audit logging
- **Module 7 (Analytics):** Win-Win matrix calculation

---

## ✅ Success Criteria

- [ ] All 18 functions implemented
- [ ] Superadmin panel accessible only to authorized users (RBAC)
- [ ] Dashboard loads in <1 second
- [ ] Win-Win matrix updates daily
- [ ] 100% of moderation actions logged (audit trail)
- [ ] Cohort analysis provides actionable insights

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Frontend Teams
**Status:** Important - MVP Required
