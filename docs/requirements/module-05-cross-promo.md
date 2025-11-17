# Module 5: Cross-Promotion & Chains - Requirements

**Module ID:** MOD-05
**Total Functions:** 22
**Priority:** P0 (Critical - MVP)
**Dependencies:** Module 2 (Loyalty), Module 3 (Transactions), Module 7 (Win-Win Analytics)
**Tech Stack:** Python 3.13, PostgreSQL 16.11, Celery 5.4.x, ClickHouse 25.8 LTS

---

## 📋 Module Overview

Cross-promotion engine is core to Свой Круг's value proposition: purchase at business A automatically triggers coupon/bonus at business B (different category). Includes simple chains (A→B), sequential chains (A→B→C), cyclical chains (A⇄B), fan-out chains (A→[B,C,D]), and Win-Win analytics to optimize chain performance.

**Key Subsystems:**
- 5.1 Simple Chains (8 functions): A→B triggers, configurable coupons, conversion tracking
- 5.2 Sequential Chains (4 functions): Multi-step A→B→C with progress tracking
- 5.3 Cyclical & Fan-out Chains (4 functions): A⇄B mutual, A→[B,C,D] choice
- 5.4 Win-Win Analytics (6 functions): Conversion matrix, ROI forecasting, chain recommendations

---

## 5.1 Simple Chains (8 functions)

### User Story 5.1.1-5.1.3: Create Simple Chain
**As a** business owner
**I want to** create cross-promo chain "Buy at my business → Coupon for partner"
**So that** we both get new customers

**Acceptance Criteria:**
```gherkin
Scenario: Create A→B chain
  Given I am Skinerica owner
  When I go to Admin Panel → "Cross-Promo" → "Create Chain"
  Then I fill:
    - Source: Skinerica (my business)
    - Destination: Миндаль (choose from dropdown)
    - Trigger: Min purchase 5,000₽
    - Reward: 20% discount coupon at Миндаль
    - Expiry: 30 days
    - Funding: Split 50/50 (both businesses share cost)
  And I submit proposal
  Then chain is sent to Миндаль for approval
  And I see "Waiting for Миндаль approval"

Scenario: Approve incoming chain proposal
  Given Миндаль received proposal from Skinerica
  When I review in "Pending Approvals"
  And I see estimated cost: "~5,000₽/month for 25 coupons"
  And I click "Approve"
  Then chain.status = "active"
  And chain goes live immediately
  And both businesses receive notification
```

**Technical Requirements:**
- Chain table:
  ```sql
  cross_promo_chains (
    id UUID PRIMARY KEY,
    source_business_id UUID REFERENCES businesses(id),
    dest_business_id UUID REFERENCES businesses(id),
    trigger_amount DECIMAL(10,2),
    coupon_type VARCHAR(20),  -- 'discount_percent' | 'discount_fixed' | 'bonus'
    coupon_value DECIMAL(10,2),
    expiry_days INT DEFAULT 30,
    funding_split VARCHAR(20),  -- 'source' | 'dest' | '50_50' | 'platform'
    status VARCHAR(20),  -- 'pending' | 'active' | 'paused' | 'ended'
    created_at TIMESTAMP
  )
  ```

---

### User Story 5.1.4-5.1.5: Trigger Chain & Issue Coupon
**As a** member
**I want to** receive coupons automatically after purchases
**So that** I discover new businesses

**Acceptance Criteria:**
```gherkin
Scenario: Chain triggered after purchase
  Given chain "Skinerica → Миндаль" is active
  And I completed 6,000₽ purchase at Skinerica (trigger: 5,000₽)
  When transaction is processed
  Then Celery task checks active chains from Skinerica
  And finds Миндаль chain (trigger met)
  And generates coupon: "20% скидка в Миндаль"
  And I receive push: "Новый купон: 20% скидка в Миндаль!"
  And coupon appears in my "Купоны" list

Scenario: User notification
  Given coupon was generated
  When push is sent
  Then message includes:
    - "Спасибо за покупку в Skinerica!"
    - "Получите 20% скидку в Миндаль"
    - "Действует 30 дней"
  And I can tap to view coupon details
```

---

### User Story 5.1.6: Track Chain Conversion
**As a** business owner
**I want to** see how many customers used cross-promo coupons
**So that** I measure ROI

**Acceptance Criteria:**
```gherkin
Scenario: View chain statistics
  Given I have active chain "Skinerica → Миндаль"
  When I view chain details
  Then I see metrics:
    - Coupons issued: 120
    - Coupons activated: 72 (60% activation rate)
    - Coupons redeemed: 54 (45% redemption rate)
    - New customers acquired: 54
    - Total revenue from chain: 270,000₽
    - Cost of discounts: -54,000₽ (20% × avg 5K purchase)
    - ROI: +400% (revenue / cost)
```

**Technical Requirements:**
- Track coupon lifecycle:
  - `issued_at`: When coupon was generated
  - `activated_at`: When user activated coupon
  - `redeemed_at`: When user used coupon at checkout
- Calculate conversion funnel: issued → activated → redeemed
- Store chain_id in coupons table for attribution

---

### User Story 5.1.7-5.1.8: Approve & Finance Chain
**As a** partner business
**I want to** approve chains before they go live
**So that** I control my discount budget

**Acceptance Criteria:**
```gherkin
Scenario: Funding options
  Given I'm setting up chain
  When I choose funding model
  Then I see options:
    - Source business pays 100% (Skinerica pays full discount)
    - Destination business pays 100% (Миндаль pays full discount)
    - Split 50/50 (both businesses share cost)
    - Platform subsidizes (ecosystem fund covers discount)
  And I select "Split 50/50"
  Then cost is shared equally when coupon is redeemed
```

---

## 5.2 Sequential Chains (4 functions)

### User Story 5.2.1-5.2.2: Create Multi-Step Chain
**As a** platform admin
**I want to** create sequential chains A→B→C
**So that** users explore 3+ businesses

**Acceptance Criteria:**
```gherkin
Scenario: Create 3-step chain
  Given I create chain "Skinerica → Миндаль → Лисичкино"
  When I configure:
    - Step 1: Purchase ≥5K at Skinerica → +500₽ bonus for Миндаль
    - Step 2: Purchase ≥3K at Миндаль → +300₽ bonus for Лисичкино
    - Step 3 (completion bonus): Purchase at Лисичкино → +1000₽ extra bonus
  Then chain is created with 3 steps
  And users see progress tracker in app

Scenario: Track user progress
  Given I completed Step 1 (Skinerica)
  When I view chain progress
  Then I see:
    - ✅ Step 1: Skinerica (completed)
    - 🔲 Step 2: Миндаль (active - 500₽ bonus available)
    - 🔲 Step 3: Лисичкино (locked until Step 2 complete)
  And I see "2 шага до бонуса 1,800₽!"
```

---

### User Story 5.2.3-5.2.4: Completion Bonus & Visualization
**As a** member
**I want to** earn extra bonus for completing full chain
**So that** I'm incentivized to explore all 3 businesses

**Acceptance Criteria:**
```gherkin
Scenario: Complete sequential chain
  Given I completed all 3 steps
  When I redeem final coupon at Лисичкино
  Then I receive completion bonus: +1,000₽
  And I see celebration: "Поздравляем! Вы прошли всю цепочку!"
  And I earn special badge "Исследователь"

Scenario: Chain visualization
  Given I view sequential chain in app
  When I tap "Ваш путь"
  Then I see visual path diagram:
    Skinerica ➔ Миндаль ➔ Лисичкино
    With progress indicators and rewards at each step
```

---

## 5.3 Cyclical & Fan-out Chains (4 functions)

### User Story 5.3.1-5.3.2: Cyclical Chains (A⇄B)
**As a** business owner
**I want to** create mutual cross-promo with partner
**So that** we exchange customers regularly

**Acceptance Criteria:**
```gherkin
Scenario: Create cyclical chain
  Given Skinerica and Миндаль want mutual promotion
  When I create A⇄B chain
  Then both directions are configured:
    - Skinerica → Миндаль: 15% discount
    - Миндаль → Skinerica: 15% discount
  And chain refreshes monthly (new coupons each month)

Scenario: Monthly refresh
  Given cyclical chain has been running 30 days
  When month ends
  Then new coupons are issued to active customers
  And previous coupons expire
```

---

### User Story 5.3.3-5.3.4: Fan-out Chains (A→[B,C,D])
**As a** member
**I want to** choose which coupon to receive from fan-out chain
**So that** I pick my preferred business

**Acceptance Criteria:**
```gherkin
Scenario: Fan-out chain triggers
  Given chain "Skinerica → [Миндаль, Лисичкино, Стим Центр]"
  When I purchase at Skinerica
  Then I receive push:
    "Выберите бонус: 20% в Миндаль, 500₽ в Лисичкино, или 15% в Стим Центр"
  And I tap push to see selection screen
  And I choose "Миндаль"
  Then 20% coupon for Миндаль is generated
  And other options expire

Scenario: UI for coupon selection
  Given I see fan-out selection screen
  When I view options
  Then I see 3 cards:
    - [Миндаль logo] 20% скидка
    - [Лисичкино logo] 500₽ бонусов
    - [Стим Центр logo] 15% скидка
  And I can tap one to select
```

---

## 5.4 Win-Win Analytics (6 functions)

### User Story 5.4.1-5.4.2: Conversion Matrix
**As a** platform admin
**I want to** see conversion rates between all business pairs
**So that** I identify best cross-promo opportunities

**Acceptance Criteria:**
```gherkin
Scenario: View Win-Win matrix
  Given I go to Analytics → "Win-Win Matrix"
  When page loads
  Then I see heatmap:
    Rows: Source businesses
    Columns: Destination businesses
    Values: % of source customers who tried destination
  And cells colored by conversion rate:
    - Green (40%+): Strong synergy
    - Yellow (20-40%): Moderate
    - Red (<20%): Weak

Scenario: Click cell for details
  Given I click Skinerica → Миндаль (45%)
  When detail modal opens
  Then I see:
    - Conversion rate: 45%
    - Customers who crossed: 120 of 267
    - Avg time to cross: 12 days
    - Cross-purchase revenue: 540,000₽
    - Recommendation: "Strong connection - increase promotion"
```

**Technical Requirements:**
- ClickHouse query for fast aggregation:
  ```sql
  SELECT
    source_business_id,
    dest_business_id,
    COUNT(DISTINCT user_id) * 100.0 / source_total AS conversion_rate
  FROM cross_purchases
  GROUP BY source_business_id, dest_business_id
  ```

---

### User Story 5.4.3-5.4.6: Win-Win Index & Chain Recommendations
**As a** platform
**I want to** calculate Win-Win index for business pairs
**So that** I recommend optimal chains

**Acceptance Criteria:**
```gherkin
Scenario: Calculate Win-Win index (1-10 scale)
  Given Skinerica ↔ Миндаль have:
    - 45% mutual conversion rate
    - High LTV customers ($250 avg)
    - Similar target demographics
  When Win-Win index is calculated
  Then score = 9/10 (excellent match)
  And recommendation: "Priority for cross-promo"

Scenario: Auto-suggest chains
  Given I'm creating new chain
  When I select source business: Skinerica
  Then system shows Top-3 destinations:
    1. Миндаль (Win-Win index: 9/10)
    2. Лисичкино (Win-Win index: 7/10)
    3. Миллениум (Win-Win index: 6/10)

Scenario: Forecast chain effectiveness
  Given I'm planning chain Skinerica → Лисичкино
  When I enter coupon details (20% discount)
  Then system forecasts:
    - Expected coupons issued: 80/month
    - Expected redemption rate: 35% (28 coupons)
    - Expected new customer revenue: 140,000₽
    - Cost of discounts: -28,000₽
    - Forecasted ROI: +400%

Scenario: Analyze existing chain
  Given chain "Миндаль → Лисичкино" has been running 3 months
  When I view detailed analytics
  Then I see:
    - Actual vs forecasted conversion: 32% vs 35% (close)
    - Customer LTV from chain: 12,500₽ avg
    - Repeat purchase rate: 60%
    - Churn rate: 15%
    - Recommendation: "Performing well - maintain"
```

---

## 📊 Technical Requirements

### Chain Processing Flow
1. Transaction created → Celery task: `check_cross_promo_chains(user_id, business_id, amount)`
2. Query active chains: `SELECT * FROM cross_promo_chains WHERE source_business_id=X AND status='active' AND trigger_amount <= Y`
3. For each matching chain → generate coupon
4. Send push notification
5. Track chain_id in coupon for analytics

### Performance
- Chain trigger check: <100ms (indexed query)
- Coupon generation: <200ms
- Win-Win matrix calculation: Daily batch job (ClickHouse)
- Matrix load time: <2 seconds

---

## 7. UI/UX REQUIREMENTS

### 7.1 Design System Reference

**Foundation:**
- **Colors:** See [docs/design/foundation/colors.md](../design/foundation/colors.md)
  - Primary: Tiffany Blue (#0ABAB5) for active states, progress bars
  - Accent: Champagne Gold (#D4AF37) for VIP/Elite tier indicators
  - Status Colors: Bronze (#E8B4BC), Silver, Gold (#D4AF37)
  - Semantic: Success (#7CB342), Error (#E57373)

- **Typography:** See [docs/design/foundation/typography.md](../design/foundation/typography.md)
  - H2: 22px/600 for points display
  - H3: 18px/600 for card titles
  - Body: 14px/400 for descriptions
  - Caption: 12px/400 for metadata (expiry dates, T&C)

- **Spacing & Components:** See [docs/design/foundation/spacing.md](../design/foundation/spacing.md) and [docs/design/components/](../design/components/)

### 7.2 Components Used

- [Status Badge](../design/components/status-badge.md) - Tier indicators (Bronze/Silver/Gold/Elite)
- [Card](../design/components/card.md) - Bonus cards, coupon cards, transaction history
- [Button](../design/components/button.md) - Redeem buttons, Apply coupon buttons
- Progress bars for tier progress
- Empty states (no bonuses, no coupons)

### 7.3 Screen-Specific Design Notes

**Cross-Promo Chain Visualization:**
- Visual path diagram for sequential chains: "Skinerica ➔ Миндаль ➔ Лисичкино"
- Boxes represent businesses with logos (48x48px)
- Arrows between boxes (Tiffany Blue color, 2px stroke)
- Completed steps: checkmark (✅) with success green background
- Active step: highlighted with Tiffany Blue border
- Locked steps: grayed out with lock icon
- Below diagram: progress indicator "2 из 3 шагов выполнено" (Body: 14px/400)
- Tap business box to view details or redeem coupon

**Triggered Offer Cards (Simple & Fan-out Chains):**
- Pushed after source business purchase triggers chain
- Card layout: Business logo (top-left), offer description (center), "Accept Offer" button (right)
- For simple chain: Single offer card (e.g., "20% скидка в Миндаль")
- For fan-out chain: Multiple option cards (e.g., "Выберите бонус: 20% в Миндаль | 500₽ в Лисичкино | 15% в Стим Центр")
- Card styling: white background, shadow, border-radius 12px
- Business logo: 40x40px, rounded, top-left corner
- Offer text (H3: 18px/600): "20% скидка в Миндаль" or "500₽ бонусов"
- Subtitle (Body: 12px/400): "Действует 30 дней"

**"Accept Offer" Button:**
- Primary Tiffany Blue button, full-width within card
- Text: "Принять предложение" or "Выбрать"
- Tap triggers coupon generation and push confirmation
- For fan-out: shows selection screen with 3 option cards side-by-side (swipeable)
- After selection: "Купон активирован! Перейти в купоны?" with confirmation CTAs

**Cyclical Chain Monthly Refresh:**
- Notification when new coupons issued: "Новый месяц, новые купоны! Получите еще 15% скидку в Skinerica"
- Old coupons marked "Истекла" with expiry date
- New coupons added to coupon list with fresh expiry date

### 7.4 Accessibility

- See [docs/design/accessibility/overview.md](../design/accessibility/overview.md)
- WCAG 2.1 Level AA compliance required
- Screen reader labels for tier badges, point values, expiry dates
- Color contrast validation for all status colors

### 7.5 Design Assets

- **Design Tokens:** `docs/design/resources/design-tokens.json`
- **Screenshots:** `UPMT/bootstrap/00_DESIGN_RAW_DATA/screenshots/` (status cards, bonus displays)

---

## 🔄 Dependencies

- **Module 2 (Loyalty):** Generate coupons/bonuses
- **Module 3 (Transactions):** Trigger chains after purchases
- **Module 7 (Analytics):** Win-Win matrix calculations

---

## ✅ Success Criteria

- [ ] All 22 functions implemented
- [ ] Simple chains trigger within 1 minute of purchase
- [ ] 40%+ redemption rate for cross-promo coupons
- [ ] Win-Win matrix identifies 10+ high-conversion pairs
- [ ] Sequential chains drive 25%+ category exploration

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Analytics Teams
**Status:** Critical - MVP Core Value Prop
