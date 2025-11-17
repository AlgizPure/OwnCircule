# Module 6: Offer Constructor - Requirements

**Module ID:** MOD-06
**Total Functions:** 18
**Priority:** P1 (Important - v1.5)
**Dependencies:** Module 2 (Loyalty), Module 5 (Cross-Promo)
**Tech Stack:** React (web admin), FastAPI 0.121.2, PostgreSQL 16.11

---

## 📋 Module Overview

Offer Constructor empowers business owners to create 5 types of promotions: discounts, bonus multipliers, cross-promo, bundle deals, and gifts. Includes step-by-step wizard, ROI forecasting, preview, approval workflow, and performance analytics.

**Key Subsystems:**
- 6.1 Offer Creation (10 functions): 5-type wizard, configuration, ROI forecast, preview
- 6.2 Approval System (4 functions): Auto-publish simple offers, partner approval for cross-promo
- 6.3 Offer Analytics (4 functions): Views, activations, redemptions, ROI calculation

---

## 6.1 Offer Creation (10 functions)

### User Story 6.1.1-6.1.3: Choose Offer Type & Configure
**As a** business owner
**I want to** create promotional offers easily
**So that** I attract customers

**Acceptance Criteria:**
```gherkin
Scenario: Choose offer type
  Given I am on Business Admin Panel → "Offers" → "Create New"
  When I see 5 offer types:
    1. Simple Discount (% or fixed amount off)
    2. Bonus Multiplier (2x/3x bonuses)
    3. Cross-Promo (trigger coupon at partner business)
    4. Bundle Deal (2-5 businesses, combined price)
    5. Gift with Purchase (free item/service)
  And I select "Simple Discount"
  Then I proceed to configuration wizard

Scenario: Configure discount offer
  Given I selected "Simple Discount"
  When I fill wizard:
    - Step 1: Discount details (20% or 1,000₽ off)
    - Step 2: Conditions (min purchase 5,000₽, new customers only)
    - Step 3: Limits (valid 30 days, max 100 uses, 1 per customer)
    - Step 4: Target audience (All members / VIP+ / Elite+)
    - Step 5: Schedule (start now / schedule for later)
  And I click "Next" through steps
  Then offer is configured

Scenario: Step-by-step wizard
  Given wizard has 5-7 steps (varies by type)
  When I complete each step
  Then I see progress indicator (Step 2 of 5)
  And I can go back to edit previous steps
  And "Next" button is disabled until required fields are filled
```

**Technical Requirements:**
- Wizard state stored in Redux (web admin) for back/forward navigation
- Offer table:
  ```sql
  offers (
    id UUID PRIMARY KEY,
    business_id UUID REFERENCES businesses(id),
    offer_type VARCHAR(20),  -- 'discount' | 'bonus_multiplier' | 'cross_promo' | 'bundle' | 'gift'
    config JSONB,  -- Type-specific configuration
    target_audience VARCHAR(20),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    max_uses INT,
    uses_per_customer INT DEFAULT 1,
    status VARCHAR(20),  -- 'draft' | 'pending_approval' | 'active' | 'paused' | 'ended'
    created_at TIMESTAMP
  )
  ```

---

### User Story 6.1.4-6.1.6: Conditions, Limits, ROI Forecast
**As a** business owner
**I want to** set conditions and see cost forecast
**So that** I control my budget

**Acceptance Criteria:**
```gherkin
Scenario: Set offer conditions
  Given I'm configuring offer
  When I set conditions:
    - Min purchase amount: 5,000₽
    - Customer type: New customers only (never purchased before)
    - Status tier: VIP+ only
  Then only customers meeting all conditions can use offer

Scenario: Set usage limits
  Given I want to limit offer usage
  When I configure limits:
    - Valid period: 30 days (expires Dec 17, 2025)
    - Max total uses: 100 coupons
    - Uses per customer: 1 (can't reuse)
  Then offer automatically ends when limits are reached

Scenario: View ROI forecast
  Given I configured 20% discount offer
  When I reach "Forecast" step
  Then I see estimated costs:
    - Expected redemptions: 80 (based on historical data)
    - Avg transaction: 5,000₽
    - Total discount cost: -80,000₽ (80 × 5K × 20%)
    - Expected revenue: 400,000₽ (80 × 5K)
    - Net revenue: +320,000₽
    - Forecasted ROI: +300%
  And I can adjust parameters to see updated forecast
```

**Technical Requirements:**
- ROI forecast uses historical redemption rates from similar offers
- Calculation: `(expected_revenue - discount_cost) / discount_cost * 100`
- If no historical data, use conservative estimate (30% redemption rate)

---

### User Story 6.1.7-6.1.10: Preview, Save Draft, Publish, Schedule
**As a** business owner
**I want to** preview offer before publishing
**So that** I ensure it looks good

**Acceptance Criteria:**
```gherkin
Scenario: Preview offer in app
  Given I completed wizard
  When I click "Preview"
  Then I see how offer appears in mobile app:
    - Offer card with business logo
    - "20% скидка" headline
    - Conditions: "При покупке от 5,000₽"
    - Expiry date: "Действует до 17 декабря"
    - CTA button: "Активировать"
  And I can go back to edit if needed

Scenario: Save draft
  Given I'm midway through wizard
  When I click "Save Draft"
  Then offer is saved with status="draft"
  And I can return later to finish

Scenario: Publish immediately
  Given I completed wizard and preview
  When I click "Publish Now"
  Then offer.status = "active"
  And offer appears in mobile app immediately
  And push notifications sent to target audience

Scenario: Schedule for later
  Given I want to launch offer next week
  When I select "Schedule" and set date: Dec 20, 10:00
  Then offer is saved with start_date = Dec 20, 10:00
  And Celery task auto-publishes at scheduled time
```

---

## 6.2 Approval System (4 functions)

### User Story 6.2.1-6.2.4: Approval Workflows
**As a** platform admin
**I want to** approve certain offers before they go live
**So that** quality is maintained

**Acceptance Criteria:**
```gherkin
Scenario: Auto-publish simple offers
  Given I created "Simple Discount" or "Bonus Multiplier" offer
  When I click "Publish"
  Then offer is published immediately (no approval needed)
  And I see "Offer is now live!"

Scenario: Partner approval for cross-promo
  Given I created cross-promo "Skinerica → Миндаль"
  When I submit offer
  Then offer.status = "pending_approval"
  And Миндаль receives notification: "Skinerica хочет создать кросс-промо"
  And Миндаль can approve/reject in their admin panel

Scenario: Superadmin moderation for bundles
  Given I created bundle deal (3 businesses)
  When I submit
  Then offer requires superadmin approval
  And I see "Pending admin review"
  And superadmin reviews in Module 10

Scenario: Approval notification
  Given my cross-promo was approved by partner
  When approval happens
  Then I receive notification: "Ваше предложение одобрено!"
  And offer.status = "active"
  And offer goes live immediately
```

---

## 6.3 Offer Analytics (4 functions)

### User Story 6.3.1-6.3.4: Track Offer Performance
**As a** business owner
**I want to** see how my offers perform
**So that** I optimize future promotions

**Acceptance Criteria:**
```gherkin
Scenario: View offer metrics
  Given I have active offer "20% скидка"
  When I view offer details
  Then I see metrics:
    - Views: 1,250 (members saw offer)
    - Activations: 450 (36% activation rate)
    - Redemptions: 180 (40% redemption rate, 14.4% overall)
    - Revenue generated: 900,000₽
    - Discount cost: -180,000₽
    - Net revenue: +720,000₽
    - Actual ROI: +300%

Scenario: Calculate ROI
  Given offer has been running 15 days
  When I view ROI calculation
  Then I see:
    - Formula: (revenue - cost) / cost × 100
    - Calculation: (900K - 180K) / 180K × 100 = +300%
  And comparison to forecast: "Actual 300% vs forecast 300% (on target)"

Scenario: Usage chart over time
  Given offer has been active 30 days
  When I view "Usage Graph"
  Then I see line chart:
    - X-axis: Days (1-30)
    - Y-axis: Redemptions per day
    - Peak days highlighted (weekends had 2x redemptions)
  And I see trend: "Usage declining - consider refresh"

Scenario: Top customers
  Given offer was redeemed by 180 customers
  When I view "Top Users"
  Then I see Top-5 customers who used offer:
    1. Anna K. - VIP - 5 purchases using offer (repeat customer!)
    2. Maria P. - Elite - 3 purchases
    ...
  And I can export full list as CSV
```

**Technical Requirements:**
- Track offer interactions:
  ```sql
  offer_views (user_id, offer_id, viewed_at)
  offer_activations (user_id, offer_id, activated_at)
  offer_redemptions (user_id, offer_id, redeemed_at, transaction_id)
  ```
- Calculate metrics in real-time (or cache for 5 minutes)
- ROI = (SUM(transaction.amount) - SUM(discount)) / SUM(discount) × 100

---

## 📊 Technical Requirements

### Offer Types Configuration
1. **Simple Discount:**
   ```json
   {
     "type": "percent|fixed",
     "value": 20,
     "min_purchase": 5000
   }
   ```

2. **Bonus Multiplier:**
   ```json
   {
     "multiplier": 2.0,
     "applies_to": "all_purchases"
   }
   ```

3. **Cross-Promo:**
   ```json
   {
     "dest_business_id": "uuid",
     "trigger_amount": 5000,
     "coupon_value": 500
   }
   ```

4. **Bundle Deal:**
   ```json
   {
     "business_ids": ["uuid1", "uuid2", "uuid3"],
     "total_price": 15000,
     "individual_price": 20000
   }
   ```

5. **Gift with Purchase:**
   ```json
   {
     "min_purchase": 3000,
     "gift_item": "Бесплатный кофе",
     "gift_value": 350
   }
   ```

### Performance
- Offer creation wizard: smooth transitions (<200ms per step)
- ROI forecast calculation: <500ms
- Analytics dashboard: <1 second load time

---

## 🔄 Dependencies

- **Module 2 (Loyalty):** Apply discounts, bonus multipliers
- **Module 5 (Cross-Promo):** Create cross-promo chains

---

## ✅ Success Criteria

- [ ] All 18 functions implemented
- [ ] Business owners create 5+ offers per month on average
- [ ] ROI forecast accuracy: ±20% of actual ROI
- [ ] 80%+ of offers are profitable (positive ROI)

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Web Admin Teams
**Status:** Important - v1.5 Feature
