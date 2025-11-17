# Module 15: Events Budget System - Requirements

**Module ID:** MOD-15
**Total Functions:** 4
**Priority:** P1 (Important - v1.5)
**Dependencies:** Module 3 (Transactions), Module 4 (Events)
**Tech Stack:** PostgreSQL 16.11, Celery, FastAPI 0.121.2

---

## 📋 Module Overview

Events budget system automatically allocates 2% of every transaction to a shared community fund for events. Budget is transparently displayed to members and distributed across event categories: Open (30%), VIP (40%), Elite (20%), Reserve (10%). Members can see budget growth in real-time and how funds are spent on events.

**Key Features:**
- Automatic 2% budget accrual from every purchase
- Budget distribution across 4 categories (Open/VIP/Elite/Reserve)
- Transparent budget dashboard for all members
- Monthly budget reports showing income and spending
- Real-time budget tracking

---

## Function C.1: Automatic Budget Formation (2% from purchases)
**As a** platform
**I want to** automatically allocate 2% of every transaction to events budget
**So that** the community has a shared fund for events

**Acceptance Criteria:**
```gherkin
Scenario: Budget accrual on purchase
  Given a member completes a 10,000₽ purchase
  When transaction is processed
  Then 200₽ (2%) is added to events budget
  And transaction bonus (5-10%) is calculated on original 10,000₽ (not affected by budget)
  And budget is visible to all members immediately

Scenario: Cumulative budget growth
  Given events budget is currently 50,000₽
  When 10 transactions totaling 100,000₽ are processed today
  Then budget increases by 2,000₽ (2% of 100K)
  And new balance is 52,000₽

Scenario: Medical transactions exemption
  Given a transaction is from medical business (врачебная тайна)
  When budget accrual is calculated
  Then 2% is still added to budget (medical data is isolated, but budget contribution is anonymous)
```

**Technical Requirements:**
- Celery task after every transaction: `accrue_event_budget(transaction_id, amount)`
- Budget table:
  ```sql
  event_budget (
    id UUID PRIMARY KEY,
    balance DECIMAL(10,2) DEFAULT 0,
    total_accrued DECIMAL(10,2) DEFAULT 0,
    total_spent DECIMAL(10,2) DEFAULT 0,
    last_updated TIMESTAMP DEFAULT NOW()
  )
  
  event_budget_transactions (
    id UUID PRIMARY KEY,
    transaction_id UUID REFERENCES transactions(id),
    amount DECIMAL(10,2) NOT NULL,
    type VARCHAR(20),  -- 'accrual' | 'spending'
    event_id UUID REFERENCES events(id) NULL,
    created_at TIMESTAMP DEFAULT NOW()
  )
  ```
- Calculate 2% of transaction amount: `budget_amount = transaction.amount * 0.02`
- Update `event_budget.balance` atomically (PostgreSQL transaction)

---

## Function C.2: Budget Distribution (Open/VIP/Elite/Reserve)
**As a** platform
**I want to** distribute budget across 4 event categories
**So that** all member tiers have fair access to events

**Acceptance Criteria:**
```gherkin
Scenario: Budget allocation percentages
  Given total events budget is 100,000₽
  When budget is viewed in dashboard
  Then I see distribution:
    - Open events (30%): 30,000₽ - Events for all members
    - VIP events (40%): 40,000₽ - Events for VIP+ members
    - Elite events (20%): 20,000₽ - Events for Elite+ members
    - Reserve (10%): 10,000₽ - Emergency fund or special initiatives

Scenario: Spending from category
  Given Open events budget is 30,000₽
  When an Open event is created with budget 5,000₽
  Then Open budget decreases to 25,000₽
  And event is marked as "funded"
  And total balance decreases to 95,000₽

Scenario: Category depletion
  Given VIP budget is 2,000₽
  When a VIP event requiring 5,000₽ is proposed
  Then event is marked "Недостаточно средств"
  And admin can approve using Reserve fund
  Or event is postponed until budget replenishes
```

**Technical Requirements:**
- Budget distribution stored in separate table:
  ```sql
  event_budget_allocation (
    category VARCHAR(20) PRIMARY KEY,  -- 'open' | 'vip' | 'elite' | 'reserve'
    percentage DECIMAL(5,2) NOT NULL,  -- 30.00, 40.00, 20.00, 10.00
    current_balance DECIMAL(10,2) DEFAULT 0,
    total_allocated DECIMAL(10,2) DEFAULT 0,
    total_spent DECIMAL(10,2) DEFAULT 0
  )
  ```
- Update all categories when budget accrues:
  ```python
  for category in ['open', 'vip', 'elite', 'reserve']:
      allocation = accrued_amount * (category.percentage / 100)
      category.current_balance += allocation
  ```

---

## Function C.3: Transparent Budget Dashboard
**As a** member
**I want to** see the current events budget and how it's used
**So that** I understand where my 2% contribution goes

**Acceptance Criteria:**
```gherkin
Scenario: View budget overview
  Given I am on Events Hub
  When I tap "Наш общий бюджет"
  Then I see budget dashboard:
    - Total balance: 100,000₽
    - This month accrued: +25,000₽
    - This month spent: -15,000₽
    - Distribution pie chart (Open 30%, VIP 40%, Elite 20%, Reserve 10%)

Scenario: Budget breakdown
  Given I view budget dashboard
  When I scroll down
  Then I see category balances:
    - Open: 30,000₽ (осталось на 6 мероприятий по 5K каждое)
    - VIP: 40,000₽ (осталось на 4 мероприятия по 10K каждое)
    - Elite: 20,000₽ (осталось на 2 мероприятия по 10K каждое)
    - Reserve: 10,000₽

Scenario: Recent spending
  Given I view budget dashboard
  When I tap "Последние расходы"
  Then I see list of funded events:
    - "Мастер-класс по макияжу" - 5,000₽ - Open - 15 ноября
    - "VIP ужин в Лисичкино" - 10,000₽ - VIP - 10 ноября
    - "Elite wellness retreat" - 15,000₽ - Elite - 5 ноября
```

**Technical Requirements:**
- API endpoint: `GET /api/v1/events/budget/dashboard`
- Response:
  ```json
  {
    "total_balance": 100000,
    "month_accrued": 25000,
    "month_spent": 15000,
    "categories": {
      "open": {"balance": 30000, "percentage": 30},
      "vip": {"balance": 40000, "percentage": 40},
      "elite": {"balance": 20000, "percentage": 20},
      "reserve": {"balance": 10000, "percentage": 10}
    },
    "recent_spending": [
      {"event_title": "...", "amount": 5000, "category": "open", "date": "2025-11-15"}
    ]
  }
  ```
- Cache dashboard data for 15 minutes (Redis)

---

## Function C.4: Monthly Budget Report
**As a** member
**I want to** receive monthly reports on budget usage
**So that** I see the impact of community contributions

**Acceptance Criteria:**
```gherkin
Scenario: Generate monthly report
  Given it's November 30, 2025 (end of month)
  When monthly report is generated
  Then all members receive email with report:
    - Subject: "Отчёт о бюджете мероприятий - Ноябрь 2025"
    - Total accrued in November: 50,000₽ (from 2,500K transaction volume)
    - Total spent in November: 35,000₽ (7 events funded)
    - Balance growth: +15,000₽
    - Upcoming events scheduled: 3 (budget allocated)

Scenario: Annual report
  Given it's December 31, 2025 (end of year)
  When annual report is generated
  Then members receive comprehensive report:
    - Total accrued in 2025: 300,000₽
    - Total spent: 250,000₽
    - Events funded: 42
    - Members attended events: 85% (participation rate)
    - Most popular event category: VIP (60% attendance)

Scenario: Report visualization
  Given I receive monthly report email
  When I open it
  Then I see:
    - Bar chart: accrued vs spent by month
    - Pie chart: spending by category (Open/VIP/Elite)
    - Photos from top 3 events of the month
    - Testimonials from event attendees
```

**Technical Requirements:**
- Celery Beat task runs on 1st of each month: `generate_monthly_budget_report(month, year)`
- Report generated as HTML email template
- Query aggregations from `event_budget_transactions` table:
  ```sql
  SELECT 
    SUM(CASE WHEN type='accrual' THEN amount ELSE 0 END) as total_accrued,
    SUM(CASE WHEN type='spending' THEN amount ELSE 0 END) as total_spent
  FROM event_budget_transactions
  WHERE created_at >= '2025-11-01' AND created_at < '2025-12-01'
  ```
- Store generated reports in Yandex Object Storage
- Send email via SendGrid/Mailgun to all members with `marketing_consent=true`

---

## 📊 Technical Requirements

### Budget Calculation Flow
1. Transaction processed → Celery task `accrue_event_budget(transaction_id, amount)`
2. Calculate 2%: `budget_amount = amount * 0.02`
3. Update `event_budget.balance` atomically
4. Distribute across categories: Open 30%, VIP 40%, Elite 20%, Reserve 10%
5. Record in `event_budget_transactions` table with type='accrual'

### Budget Spending Flow
1. Event is approved → Check category budget availability
2. If sufficient funds, deduct from category balance
3. Record in `event_budget_transactions` with type='spending' and event_id
4. Update `event.budget_allocated = TRUE`

### Performance
- Budget accrual: <50ms per transaction (async Celery task)
- Dashboard load: <300ms (cached for 15 minutes)
- Monthly report generation: <5 minutes for 1000 members

---

## 🔄 Dependencies

- **Module 3 (Transactions):** Trigger budget accrual after every transaction
- **Module 4 (Events):** Link budget spending to events
- **Module 12 (Notifications):** Send monthly budget report emails

---

## ✅ Success Criteria

- [ ] 100% of transactions contribute 2% to budget
- [ ] Budget balance is transparent to all members
- [ ] 90%+ of events are funded from budget (not sponsor-dependent)
- [ ] Monthly reports sent on time (1st of each month)
- [ ] Budget dashboard loads in <300ms (p95)

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Analytics Teams
**Status:** Ready for v1.5 Development
