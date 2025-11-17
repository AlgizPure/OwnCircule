# Module 3: Transactions & Purchase History - Requirements

**Module ID:** MOD-03
**Total Functions:** 12
**Priority:** P0 (Critical - MVP)
**Dependencies:** Backend Transaction API, CRM Integrations (Module 8)
**Tech Stack:** React Native 0.81, Redux Toolkit, PostgreSQL 16.11, ClickHouse 25.8 LTS

---

## 📋 Module Overview

Transaction module tracks all member purchases across partner businesses, provides purchase history with filtering/search, and generates analytics visualizations. Transactions are synchronized from CRM systems (YCLIENTS, Iiko, 1С) and displayed in mobile app with bonus accrual details.

**Key Features:**
- Manual transaction creation (QR scan or ID entry)
- Automatic CRM synchronization
- Purchase history with filters (business, category, date)
- Transaction search
- Detailed transaction cards
- CSV/PDF export
- Monthly spending statistics
- Top-3 favorite categories analysis

---

## User Story 3.1: Manual Transaction Creation
**As a** business staff member
**I want to** manually create a transaction by QR scan or member ID
**So that** bonuses are applied even if CRM sync fails

**Acceptance Criteria:**
```gherkin
Scenario: Create transaction via QR scan
  Given I am business staff with tablet app
  When I scan member QR code
  And I enter transaction amount: 5000₽
  And I select transaction type: "Purchase"
  Then transaction is created instantly
  And member receives 5% bonuses (250₽ for Insider)
  And member sees push notification "Начислено 250₽ бонусов"

Scenario: Create transaction via ID entry
  Given I cannot scan QR code (damaged/no camera)
  When I manually enter member ID: "ABC-123456"
  And I enter amount and type
  Then transaction is validated and created
```

**Technical Requirements:**
- Transaction endpoint: `POST /api/v1/transactions/create`
- Validate member exists before creating transaction
- Calculate bonus percentage based on member status tier
- Support offline mode with sync queue

---

## User Story 3.2: Automatic CRM Synchronization
**As a** platform
**I want to** automatically sync transactions from business CRM systems
**So that** members don't need manual bonus accrual

**Acceptance Criteria:**
```gherkin
Scenario: Sync from YCLIENTS (Миндаль salon)
  Given Миндаль uses YCLIENTS CRM
  When a member completes a purchase in YCLIENTS
  Then within 5 minutes, the transaction appears in platform database
  And bonuses are auto-accrued to member's account
  And member receives push notification

Scenario: Duplicate detection
  Given a transaction was already synced (external_id="YCLIENTS-12345")
  When sync runs again and finds same external_id
  Then the transaction is skipped (no duplicate created)
  And sync log records "Duplicate skipped"
```

**Technical Requirements:**
- Celery Beat task runs every 5 minutes
- Fetch new transactions from all CRM APIs (YCLIENTS, Iiko, 1С, AMO CRM, Renovatio)
- Match member by phone number (CRM customer phone → platform user phone)
- Store external_id (CRM transaction ID) to prevent duplicates
- Log sync errors for admin review

---

## User Story 3.3: View Purchase History
**As a** member
**I want to** see all my purchases in chronological order
**So that** I can track my spending

**Acceptance Criteria:**
```gherkin
Scenario: View transaction list
  Given I have 25 transactions
  When I tap Profile → "История покупок"
  Then I see transactions sorted by date (newest first)
  And each transaction shows:
    - Business logo and name
    - Date and time (e.g., "17 ноября 2025, 14:35")
    - Amount paid: 5,000₽
    - Bonuses earned: +250₽ (or bonuses spent: -500₽)
  And I see infinite scroll pagination (20 transactions per page)

Scenario: Empty state
  Given I have 0 transactions (new member)
  When I view purchase history
  Then I see empty state: "Ваши покупки появятся здесь"
  And I see button "Найти бизнесы" → takes to Business Catalog
```

---

## User Story 3.4-3.6: Filter Transactions
**As a** member
**I want to** filter my purchases by business, category, or date
**So that** I find specific transactions quickly

**Acceptance Criteria:**
```gherkin
Scenario: Filter by business
  Given I have transactions at 3 businesses
  When I select filter "Бизнес" → "Миндаль"
  Then I see only 5 transactions from Миндаль
  And other businesses are hidden

Scenario: Filter by category
  Given I have transactions in Beauty (10) and Gastronomy (5)
  When I select filter "Категория" → "Красота"
  Then I see only 10 Beauty transactions
  
Scenario: Filter by date range
  Given I have transactions spanning 3 months
  When I select "Период" → "Ноябрь 2025"
  Then I see only November transactions (8 transactions)
  And I can see total spent in November: 45,000₽
```

**Technical Requirements:**
- Use Redux Toolkit `createSlice` for filter state
- Backend API: `GET /api/v1/transactions?business_id=X&category=Y&from_date=Z&to_date=W`
- Cache filtered results for 5 minutes (RTK Query)

---

## User Story 3.7: Search Transactions
**As a** member
**I want to** search transactions by amount or description
**So that** I find a specific purchase

**Acceptance Criteria:**
```gherkin
Scenario: Search by amount
  Given I have 25 transactions
  When I enter search query "5000"
  Then I see all transactions with amount containing "5000"
  And results are highlighted (e.g., "5000₽", "15000₽")

Scenario: Search by business name
  Given I have transactions at Миндаль and Skinerica
  When I enter "Минд"
  Then I see transactions from "Миндаль" (autocomplete)
  
Scenario: No results
  Given I search for "9999999"
  When no transactions match
  Then I see "Ничего не найдено. Попробуйте другой запрос"
```

---

## User Story 3.8: Transaction Details
**As a** member
**I want to** see full transaction details
**So that** I understand what bonuses were applied

**Acceptance Criteria:**
```gherkin
Scenario: View transaction card
  Given I tap on a transaction from list
  When the detail modal opens
  Then I see:
    - Business name, logo, category
    - Date and time (full timestamp)
    - Amount paid: 5,000₽
    - Bonuses earned: +350₽ (7% VIP rate)
    - Bonuses spent: -500₽ (if any were redeemed)
    - Net amount: 4,500₽
    - Transaction ID for support reference
  And I see "Сообщить о проблеме" button → contact support
```

---

## User Story 3.9: Link Transaction to Coupon
**As a** member
**I want to** see which coupon was used in a transaction
**So that** I understand the discount applied

**Acceptance Criteria:**
```gherkin
Scenario: Transaction with coupon
  Given I used a "20% discount" coupon at Миндаль
  When I view transaction details
  Then I see "Использован купон: Скидка 20% на услуги"
  And I see original price: 5,000₽
  And I see discount: -1,000₽
  And I see final price: 4,000₽
  And I see bonuses earned on discounted price: +280₽ (7% of 4000)

Scenario: Transaction without coupon
  Given no coupon was used
  When I view transaction details
  Then I do not see coupon section
```

---

## User Story 3.10: Export Transaction History
**As a** member
**I want to** export my purchase history to CSV or PDF
**So that** I can use it for personal budgeting or taxes

**Acceptance Criteria:**
```gherkin
Scenario: Export to CSV
  Given I am on transaction history screen
  When I tap "···" menu → "Экспорт" → "CSV"
  Then I see dialog "Экспортировать за какой период?"
  And I select "Весь период" or custom date range
  Then CSV file is generated and downloaded
  And CSV contains: date, business, category, amount, bonuses_earned, bonuses_spent

Scenario: Export to PDF
  Given I select "PDF" format
  When export completes
  Then I receive PDF with:
    - Header: "История покупок - Свой Круг"
    - Member name and ID
    - Date range
    - Table of transactions
    - Footer: Total spent, total bonuses earned
```

**Technical Requirements:**
- Backend endpoint: `POST /api/v1/transactions/export` (returns file URL)
- Use Celery task for large exports (>1000 transactions)
- Store export files in Yandex Object Storage
- Send download link via push notification when ready

---

## User Story 3.11: Monthly Spending Statistics
**As a** member
**I want to** see my spending trend over months
**So that** I understand my consumption patterns

**Acceptance Criteria:**
```gherkin
Scenario: View spending graph
  Given I have transactions for 6 months
  When I scroll to "Статистика" section in Profile
  Then I see bar chart with 6 bars (one per month)
  And each bar shows total spent that month
  And I see trend line (increasing/decreasing)
  And I see average monthly spend: 25,000₽
  
Scenario: Tap bar for details
  Given I see spending graph
  When I tap on November bar
  Then I see breakdown:
    - Total spent: 45,000₽
    - Transactions: 8
    - Bonuses earned: 3,150₽
    - Top category: Красота (60% of spending)
```

**Technical Requirements:**
- Use react-native-chart-kit or Victory Native for charting
- Fetch aggregated data from backend: `GET /api/v1/transactions/stats?group_by=month&months=6`
- Cache stats for 1 hour (RTK Query)

---

## User Story 3.12: Top-3 Favorite Categories
**As a** member
**I want to** see my top-3 favorite categories
**So that** I understand my preferences

**Acceptance Criteria:**
```gherkin
Scenario: View top categories
  Given I have transactions in 4 categories:
    - Красота: 60% (12 transactions)
    - Гастрономия: 25% (5 transactions)
    - Здоровье: 10% (2 transactions)
    - Флористика: 5% (1 transaction)
  When I view Profile → "Статистика"
  Then I see "Любимые категории" with Top-3:
    1. Красота (60%)
    2. Гастрономия (25%)
    3. Здоровье (10%)
  And each category has icon and percentage bar

Scenario: Less than 3 categories
  Given I only purchased in 1 category (Beauty)
  When I view favorite categories
  Then I see only 1 category
  And I see message "Попробуйте другие категории для разнообразия!"
```

---

## 📊 Technical Requirements

### Database Schema
```sql
transactions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  business_id UUID REFERENCES businesses(id),
  amount DECIMAL(10,2) NOT NULL,
  bonus_accrued DECIMAL(10,2) DEFAULT 0,
  bonus_redeemed DECIMAL(10,2) DEFAULT 0,
  transaction_type VARCHAR(20) DEFAULT 'purchase', -- 'purchase' | 'refund'
  external_id VARCHAR(255) UNIQUE,  -- CRM transaction ID
  coupon_id UUID REFERENCES coupons(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
)

CREATE INDEX idx_transactions_user_created ON transactions(user_id, created_at DESC);
CREATE INDEX idx_transactions_business ON transactions(business_id);
CREATE INDEX idx_transactions_external ON transactions(external_id);
```

### API Endpoints
- `POST /api/v1/transactions/create` - Manual transaction creation
- `GET /api/v1/transactions?user_id=X&filters=Y` - List transactions with filters
- `GET /api/v1/transactions/:id` - Transaction details
- `POST /api/v1/transactions/export` - Export transactions (CSV/PDF)
- `GET /api/v1/transactions/stats?user_id=X` - Aggregated statistics

### Performance
- Transactions list: <200ms API response time
- Pagination: 20 transactions per page (infinite scroll)
- Cache transaction list for 1 minute (RTK Query)
- Export queue: max 1000 transactions inline, >1000 use Celery task

---

## 🔄 Dependencies

- **Module 2 (Loyalty System):** Bonus calculation logic
- **Module 8 (CRM Integrations):** Automatic transaction sync
- **Backend:** PostgreSQL for OLTP, ClickHouse for analytics aggregations

---

## ✅ Success Criteria

- [ ] All 12 functions implemented and tested
- [ ] Transaction sync latency <5 minutes from CRM purchase
- [ ] 0 duplicate transactions in production
- [ ] Export completes in <30s for 1000 transactions
- [ ] Transaction list loads in <300ms (p95)

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Mobile Teams
**Status:** Ready for Development
