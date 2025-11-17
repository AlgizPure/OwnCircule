# Module 7: Business Analytics - Requirements

**Module ID:** MOD-07
**Total Functions:** 25
**Priority:** P1 (Important - v1.5)
**Dependencies:** Module 3 (Transactions), Module 5 (Cross-Promo), ClickHouse
**Tech Stack:** React (web admin), FastAPI 0.121.2, ClickHouse 25.8 LTS, Chart.js

---

## 📋 Module Overview

Business Analytics provides enterprise-grade insights for partner businesses: revenue tracking, customer acquisition sources, cross-business flows, RFM segmentation, and churn prediction. Democratizes analytics typically requiring 500K+ custom development.

**Key Subsystems:**
- 7.1 General Statistics (8 functions): Revenue, transactions, customers, trends
- 7.2 Customer Acquisition Sources (4 functions): Where customers come from (cross-promo tracking)
- 7.3 Customer Outflow (3 functions): Where customers go after your business
- 7.4 RFM Segmentation (5 functions): Auto-segment customers (Champions, At-Risk, Lost)
- 7.5 Churn Prediction (5 functions): Identify at-risk customers, retention campaigns

---

## 7.1 General Statistics (8 functions)

### User Story 7.1.1-7.1.8: Dashboard & Trends
**As a** business owner
**I want to** see key metrics at a glance
**So that** I monitor business health

**Acceptance Criteria:**
```gherkin
Scenario: View main dashboard
  Given I log in to Business Admin Panel
  When I open Analytics Dashboard
  Then I see KPIs:
    - Total revenue (30 days): 450,000₽ (↑ 12% vs last 30 days)
    - Ecosystem revenue: 135,000₽ (30% of total - from members)
    - Total transactions: 102 (↑ 8%)
    - Unique customers: 85 (↑ 15%)
    - New vs returning: 25 new (29%) / 60 returning (71%)
    - Avg transaction: 4,410₽ (↓ 3%)
  And charts:
    - Revenue trend (daily, 30 days)
    - Customer split pie chart (new vs returning)

Scenario: Ecosystem revenue share
  Given I want to see ecosystem impact
  When I view "Ecosystem vs Direct"
  Then I see:
    - Direct revenue (non-members): 315,000₽ (70%)
    - Ecosystem revenue (members): 135,000₽ (30%)
    - Insight: "Ecosystem members have 2.5x higher avg transaction"

Scenario: Revenue comparison
  Given I want to compare periods
  When I select "Compare: Last month vs This month"
  Then I see side-by-side:
    - Last month: 400,000₽
    - This month: 450,000₽
    - Change: +50,000₽ (+12.5%)
  And I see insight: "Growth driven by 15% more customers"

Scenario: Revenue chart
  Given I want to see trends
  When I view "Revenue by Day"
  Then I see line chart (30 days)
  And I can switch to: Week / Month / Year views

Scenario: Export data
  Given I want to analyze externally
  When I click "Export to Excel"
  Then CSV file is generated with:
    - Date, Revenue, Transactions, Customers, Avg Transaction
  And file is downloaded

Scenario: Date range selection
  Given I want custom period
  When I select "Custom Range" → Nov 1-15
  Then all metrics recalculate for that period
```

---

## 7.2 Customer Acquisition Sources (4 functions)

### User Story 7.2.1-7.2.4: Source Attribution & Recommendations
**As a** business owner
**I want to** know where my customers come from
**So that** I invest in best acquisition channels

**Acceptance Criteria:**
```gherkin
Scenario: View customer sources
  Given I go to Analytics → "Customer Sources"
  When I view source breakdown
  Then I see list:
    1. Skinerica → 25 customers (29%) - 112,500₽ revenue
    2. Direct (non-ecosystem) → 20 customers (24%)
    3. Лисичкино → 15 customers (18%)
    4. Referrals → 10 customers (12%)
    5. Other → 15 customers (18%)

Scenario: Source revenue
  Given I want to see source profitability
  When I view "Revenue by Source"
  Then I see:
    - Skinerica: 112,500₽ (25 customers × 4,500₽ avg)
    - Conversion rate: 45% (25 of 55 Skinerica customers tried us)
  And I see insight: "Skinerica is your best source (45% conversion)"

Scenario: Conversion rates
  Given I want to optimize cross-promo
  When I view "Source Conversion Rates"
  Then I see funnel:
    - Coupons issued: 55
    - Coupons activated: 40 (73%)
    - Coupons redeemed: 25 (45% of issued, 63% of activated)

Scenario: Recommendations
  Given system analyzes sources
  When I view "Recommendations"
  Then I see:
    - "Strengthen partnership with Skinerica (45% conversion)"
    - "Improve conversion from Лисичкино (currently 28%)"
    - "Consider new cross-promo with Миллениум (high potential)"
```

---

## 7.3 Customer Outflow (3 functions)

### User Story 7.3.1-7.3.3: Destination Analysis
**As a** business owner
**I want to** know where customers go after my business
**So that** I create return-loop cross-promos

**Acceptance Criteria:**
```gherkin
Scenario: View customer destinations
  Given I go to Analytics → "Customer Outflow"
  When I view where customers go
  Then I see:
    1. Лисичкино → 30 customers (35% of my customers tried them)
    2. Миллениум → 20 customers (24%)
    3. Стим Центр → 15 customers (18%)

Scenario: Destination conversion
  Given I want to measure outflow
  When I view conversion rates
  Then I see:
    - Миндаль → Лисичкино: 35% conversion
    - Time to cross: Avg 8 days
    - Revenue at Лисичкино: 150,000₽ (30 customers × 5K)

Scenario: Return-loop opportunities
  Given I want customers to return
  When I view "Potential Return Chains"
  Then I see suggestions:
    - "Create chain: Лисичкино → Миндаль (bring customers back)"
    - "30 customers went to Лисичкино - 10 haven't returned in 30 days"
```

---

## 7.4 RFM Segmentation (5 functions)

### User Story 7.4.1-7.4.5: Auto-Segmentation
**As a** business owner
**I want to** segment customers by behavior
**So that** I target them effectively

**Acceptance Criteria:**
```gherkin
Scenario: View RFM segments
  Given I go to Analytics → "Customer Segments"
  When I view RFM analysis
  Then I see segments:
    - Champions (R5F5M5): 15 customers - High value, frequent, recent
    - Loyal (R4F4M4): 20 customers - Regular customers
    - At Risk (R2F4M4): 10 customers - Haven't visited recently
    - Lost (R1F5M5): 5 customers - Used to be champions, now gone
    - New (R5F1M1): 25 customers - Recent first purchase
  
Scenario: Segment characteristics
  Given I click on "Champions" segment
  When I view details
  Then I see:
    - Size: 15 customers (18% of total)
    - Avg Recency: 5 days (very recent)
    - Avg Frequency: 8 purchases (high)
    - Avg Monetary: 45,000₽ total (high spend)
    - LTV: 55,000₽ predicted
    - Retention: 95%

Scenario: Segment recommendations
  Given I view "At Risk" segment
  When I see recommendations
  Then I see:
    - "Send 20% discount to win back these 10 customers"
    - "Expected recovery: 6 customers (60% return rate)"
    - "Cost: 12,000₽ discount / Benefit: 60,000₽ revenue"

Scenario: Export segments
  Given I want to run email campaign
  When I click "Export Champions" → CSV
  Then I get file with:
    - Name, Phone, Email, Last purchase date, Total spent

Scenario: RFM score explanation
  Given I want to understand scoring
  When I view "What is RFM?"
  Then I see:
    - Recency: Days since last purchase (1-5 scale)
    - Frequency: Number of purchases (1-5 scale)
    - Monetary: Total spent (1-5 scale)
    - R5F5M5 = Best customers (recent, frequent, high-spend)
```

**Technical Requirements:**
- RFM calculated daily via ClickHouse:
  ```sql
  SELECT
    user_id,
    NTILE(5) OVER (ORDER BY days_since_last_purchase DESC) AS recency_score,
    NTILE(5) OVER (ORDER BY purchase_count) AS frequency_score,
    NTILE(5) OVER (ORDER BY total_spent) AS monetary_score
  FROM customer_metrics
  ```

---

## 7.5 Churn Prediction (5 functions)

### User Story 7.5.1-7.5.5: Identify & Retain At-Risk Customers
**As a** business owner
**I want to** predict which customers will churn
**So that** I proactively retain them

**Acceptance Criteria:**
```gherkin
Scenario: View at-risk customers
  Given I go to Analytics → "Churn Prediction"
  When I view at-risk list
  Then I see customers with high churn probability:
    1. Anna K. - 85% churn risk - 45 days since last visit
    2. Maria P. - 75% churn risk - 35 days since last visit
    ...
  And sorted by churn risk (highest first)

Scenario: Churn probability calculation
  Given customer hasn't visited in 45 days
  When churn model runs
  Then probability calculated based on:
    - Days since last visit (primary signal)
    - Historical visit frequency (weekly → now stopped)
    - Segment (was Champions, now At Risk)
    - Ecosystem activity (still active in other businesses)
  And churn_probability = 0.85 (85%)

Scenario: Days since last visit
  Given I view at-risk customer details
  When I click on Anna K.
  Then I see:
    - Last visit: 45 days ago
    - Previous frequency: Every 14 days
    - Expected next visit: 31 days overdue
    - Insight: "Customer is likely churning"

Scenario: Retention recommendations
  Given customer has 85% churn risk
  When I view recommendations
  Then I see:
    - "Send personalized win-back offer: 30% discount"
    - "Offer expires in 7 days (creates urgency)"
    - "Expected return rate: 40%"
    - "Cost: 1,500₽ discount / Benefit: 5,000₽ revenue"

Scenario: Mass retention campaign
  Given I have 10 at-risk customers
  When I click "Send Win-Back Offers to All"
  Then bulk campaign is created:
    - 10 personalized offers generated (Module 2)
    - Push + Email sent to all 10 customers
    - Campaign tracked for effectiveness
  And I see "Campaign sent to 10 customers"
```

**Technical Requirements:**
- Churn model: Logistic regression or simple rule-based
  - Rule: If `days_since_last_visit > (avg_frequency * 2)` → at risk
  - Example: If customer visits every 14 days, after 28 days → at risk
- Calculate daily via Celery Beat task
- Store churn scores in ClickHouse for fast querying

---

## 📊 Technical Requirements

### Analytics Stack
- **OLAP Database:** ClickHouse 25.8 LTS (100x faster than PostgreSQL for analytics)
- **Visualization:** Chart.js for web admin dashboards
- **Data Pipeline:** Celery tasks sync PostgreSQL → ClickHouse hourly
- **Caching:** Redis (15-minute TTL for dashboard metrics)

### Performance
- Dashboard load: <1 second (cached metrics)
- RFM segmentation: <2 seconds (pre-computed daily)
- Churn prediction: <3 seconds (pre-computed daily)
- Export CSV: <5 seconds for 1000 customers

---

## 🔄 Dependencies

- **Module 3 (Transactions):** Source data for all analytics
- **Module 5 (Cross-Promo):** Attribution for customer sources
- **ClickHouse:** OLAP database for fast aggregations

---

## ✅ Success Criteria

- [ ] All 25 functions implemented
- [ ] RFM segmentation identifies 5+ actionable segments
- [ ] Churn prediction accuracy: 70%+ (measured after 30 days)
- [ ] Business owners use analytics 2+ times per week
- [ ] Win-back campaigns achieve 40%+ return rate

---

**Last Updated:** 2025-11-17
**Owner:** Analytics + Backend Teams
**Status:** Important - v1.5 Feature
