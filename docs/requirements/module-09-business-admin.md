# Module 9: Business Admin Panel - Requirements

**Module ID:** MOD-09
**Total Functions:** 22
**Priority:** P1 (Important - MVP)
**Dependencies:** Module 3 (Transactions), Module 6 (Offers), Module 7 (Analytics)
**Tech Stack:** React 18 (web), FastAPI 0.121.2, PostgreSQL 16.11

---

## 📋 Module Overview

Business Admin Panel is the web dashboard for partner business owners to manage customers, transactions, offers, and view analytics. Provides self-service tools for daily operations without requiring superadmin intervention.

**Key Subsystems:**
- 9.1 Customer Management (6 functions): View, search, filter customers
- 9.2 Transaction Management (5 functions): Manual entry, edit, refund, export
- 9.3 Analytics & Reports (6 functions): Dashboard, revenue, sources, RFM, churn
- 9.4 Offer Management (5 functions): Create, edit, pause, analytics

---

## 9.1 Customer Management (6 functions)

### User Story 9.1.1-9.1.6: View & Search Customers
**As a** business owner
**I want to** see all my customers
**So that** I understand my customer base

**Acceptance Criteria:**
```gherkin
Scenario: View customer list
  Given I log in to Business Admin Panel
  When I go to "Customers"
  Then I see table with columns:
    - Name, Phone, Email
    - Status (Insider/VIP/Elite/Inner Circle)
    - Last visit date
    - Total spent at my business
    - Visits count
  And I see pagination (50 customers per page)
  And I see total: "85 customers"

Scenario: Search by name
  Given I want to find customer
  When I enter "Мария" in search box
  Then I see 3 results matching "Мария"
  And results are highlighted

Scenario: Search by phone
  Given I enter "+7 999 123-45-67"
  Then I see customer with that phone
  And I see their full details

Scenario: Filter by status
  Given I want to see VIP customers
  When I select filter "Status: VIP"
  Then I see only VIP customers (18 of 85)

Scenario: Filter by last visit
  Given I want to see recent customers
  When I select "Last 7 days"
  Then I see customers who visited in last week (25 customers)

Scenario: View customer details
  Given I click on customer "Анна К."
  When detail modal opens
  Then I see:
    - Full profile (name, phone, email, status)
    - Transaction history at my business (12 purchases)
    - Total spent: 54,000₽
    - Avg transaction: 4,500₽
    - Last visit: 5 days ago
    - Favorite services: Стрижка, Окрашивание
  And I can click "View in Ecosystem" to see full ecosystem activity (if permissions allow)

Scenario: Export customer list
  Given I want to run marketing campaign
  When I click "Export" → "CSV"
  Then I download file with:
    - Name, Phone, Email, Status, Last Visit, Total Spent, Visits
```

---

## 9.2 Transaction Management (5 functions)

### User Story 9.2.1-9.2.5: Manual Transaction Entry & Management
**As a** business staff
**I want to** manually enter transactions
**So that** bonuses are applied even if CRM sync fails

**Acceptance Criteria:**
```gherkin
Scenario: Manual transaction entry (QR scan)
  Given customer shows QR code at checkout
  When I scan QR code with tablet
  Then I see customer name + status (e.g., "Анна К. - VIP")
  And I enter amount: 5,000₽
  And I click "Create Transaction"
  Then transaction is created
  And bonuses are accrued (7% for VIP = 350₽)
  And customer receives push notification

Scenario: Manual transaction entry (ID input)
  Given customer doesn't have QR code
  When I enter Member ID: "ABC-123456"
  And I enter amount
  Then transaction is created same as QR scan

Scenario: Edit transaction before confirmation
  Given I entered transaction with wrong amount
  When I change amount from 5,000₽ to 4,500₽
  And I click "Update"
  Then transaction is updated
  And bonus calculation is recalculated

Scenario: Refund transaction
  Given customer returns item
  When I find transaction in list
  And I click "Refund"
  And I enter refund reason
  Then transaction.type = "refund"
  And bonuses are deducted from customer balance
  And customer receives notification: "Возврат обработан, списано 350₽ бонусов"

Scenario: View all transactions
  Given I go to "Transactions"
  When I view list
  Then I see all transactions at my business:
    - Date, Customer, Amount, Bonuses Accrued/Redeemed
  And I can filter by date range

Scenario: Export transactions
  Given I want accounting report
  When I click "Export" → "Excel"
  Then I download file with all transactions (date, customer, amount, bonuses)
```

---

## 9.3 Analytics & Reports (6 functions)

### User Story 9.3.1-9.3.6: Business Analytics Dashboard
**As a** business owner
**I want to** see analytics about my business
**So that** I make data-driven decisions

**Acceptance Criteria:**
```gherkin
Scenario: View main dashboard
  Given I go to "Analytics"
  When dashboard loads
  Then I see KPIs (Module 7.1):
    - Total revenue (30 days)
    - Ecosystem revenue share
    - Total transactions
    - Unique customers
  And charts:
    - Revenue trend (30 days)
    - Customer acquisition sources

Scenario: Revenue report
  Given I want detailed revenue breakdown
  When I go to "Reports" → "Revenue"
  Then I can select period: Day / Week / Month / Year
  And I see revenue by period
  And I can export to Excel

Scenario: Customer sources report
  Given I want to see acquisition channels (Module 7.2)
  When I view "Customer Sources"
  Then I see:
    - Top sources (other businesses)
    - Conversion rates
    - Revenue by source

Scenario: Cross-promo effectiveness
  Given I want to measure cross-promo ROI (Module 7.2)
  When I view "Cross-Promo Performance"
  Then I see all chains where I'm destination:
    - Skinerica → Миндаль: 25 customers, 112,500₽ revenue
  And I see all chains where I'm source:
    - Миндаль → Лисичкино: 30 customers sent

Scenario: RFM analysis
  Given I want to segment customers (Module 7.4)
  When I view "Customer Segments"
  Then I see RFM segments:
    - Champions: 15 customers
    - At Risk: 10 customers
    - Lost: 5 customers
  And I can export segments for targeted campaigns

Scenario: Churn prediction
  Given I want to retain customers (Module 7.5)
  When I view "At-Risk Customers"
  Then I see list of customers likely to churn
  And I can send win-back offers directly
```

---

## 9.4 Offer Management (5 functions)

### User Story 9.4.1-9.4.5: Create & Manage Offers
**As a** business owner
**I want to** create and manage promotional offers
**So that** I attract customers

**Acceptance Criteria:**
```gherkin
Scenario: View all offers
  Given I go to "Offers"
  When page loads
  Then I see tabs:
    - Active (3 offers currently running)
    - Drafts (1 offer in progress)
    - Completed (5 past offers)
  And each offer shows: Title, Type, Status, Uses, Start/End dates

Scenario: Create new offer
  Given I click "Create Offer"
  When I'm redirected to Offer Constructor (Module 6)
  Then I can create any of 5 offer types
  And I configure details step-by-step
  And I publish or save draft

Scenario: Edit active offer
  Given I have active offer "20% скидка"
  When I click "Edit"
  Then I can modify:
    - End date (extend or shorten)
    - Max uses (increase limit)
    - Description
  But I cannot change discount value (would affect issued coupons)

Scenario: Pause/Resume offer
  Given offer is active
  When I click "Pause"
  Then offer.status = "paused"
  And no new coupons are issued
  And existing coupons remain valid
  When I click "Resume"
  Then offer.status = "active" again

Scenario: View offer analytics (Module 6.3)
  Given I have running offer
  When I click "Analytics"
  Then I see:
    - Views, Activations, Redemptions
    - ROI calculation
    - Usage chart over time
    - Top customers who used offer
```

---

## 📊 Technical Requirements

### Admin Panel Stack
- **Frontend:** React 18 + TypeScript + Ant Design (UI library)
- **Backend:** FastAPI endpoints under `/api/v1/business/*`
- **Authentication:** JWT with `role='business_owner'` or `business_staff`
- **RBAC:** Business owners see only their business data (enforced by business_id filter)

### API Endpoints
- `GET /api/v1/business/customers` - List customers with filters
- `GET /api/v1/business/transactions` - List transactions with filters
- `POST /api/v1/business/transactions` - Manual transaction entry
- `GET /api/v1/business/analytics/dashboard` - Dashboard KPIs
- `GET /api/v1/business/offers` - List offers
- `POST /api/v1/business/offers` - Create offer

### Performance
- Customer list load: <500ms (paginated, indexed queries)
- Dashboard load: <1 second (cached metrics)
- Transaction entry: <300ms (create + notify)

---

## 🔄 Dependencies

- **Module 3 (Transactions):** Transaction CRUD operations
- **Module 6 (Offers):** Offer constructor and management
- **Module 7 (Analytics):** Analytics dashboards and reports

---

## ✅ Success Criteria

- [ ] All 22 functions implemented
- [ ] Business owners use admin panel 3+ times per week
- [ ] Manual transaction entry completes in <30 seconds
- [ ] 80%+ of businesses create at least 1 offer per month
- [ ] Analytics dashboards drive 20% increase in data-driven decisions

---

**Last Updated:** 2025-11-17
**Owner:** Web Frontend + Backend Teams
**Status:** Important - MVP Required
