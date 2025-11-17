# Module 2: Loyalty System - Requirements

**Module ID:** MOD-02
**Total Functions:** 45
**Priority:** P0 (Critical - MVP)
**Dependencies:** Module 3 (Transactions), Module 8 (CRM Integrations)
**Tech Stack:** Python 3.13, FastAPI 0.121.2, PostgreSQL 16.11, Redis 8.2, Celery 5.4.x

---

## 📋 Module Overview

Loyalty system is the core value proposition of Свой Круг: unified bonuses (5-10% cashback), status tiers (Insider/VIP/Elite/Inner Circle), coupons/promotions, and cross-business incentives. Members earn bonuses on every purchase, redeem at any partner, and progress through status tiers for increased benefits.

**Key Subsystems:**
- 2.1 Bonus System (15 functions): Accrual, redemption, expiry, multipliers, history, gifting
- 2.2 Status System (12 functions): Tier calculation, progress tracking, upgrade notifications, privileges
- 2.3 Coupons & Promotions (18 functions): Activation, redemption, types (discount/bonus/cross-promo/bundle/gift), expiry

---

## 2.1 Bonus System (15 functions)

### User Story 2.1.1: Automatic Bonus Accrual
**As a** member
**I want to** receive bonuses automatically after purchases
**So that** I don't need to manually request accrual

**Acceptance Criteria:**
```gherkin
Scenario: Insider tier (5% cashback)
  Given I am Insider status
  When I complete a 10,000₽ purchase at Миндаль
  Then I receive 500₽ bonuses (5% of 10K)
  And I see push notification "Начислено 500₽ бонусов!"
  And bonus appears in my balance within 1 minute

Scenario: VIP tier (7% cashback)
  Given I am VIP status
  When I complete same 10,000₽ purchase
  Then I receive 700₽ bonuses (7% of 10K)

Scenario: Elite tier (10% cashback)
  Given I am Elite status
  When I complete same 10,000₽ purchase
  Then I receive 1,000₽ bonuses (10% of 10K)
```

**Technical Requirements:**
- Celery task after transaction: `accrue_bonus(user_id, transaction_id, amount)`
- Bonus calculation: `bonus = amount * cashback_rate[user.status_tier]`
- Update `bonuses` table atomically (PostgreSQL transaction)
- Send push notification via Module 12

---

### User Story 2.1.2: First Purchase in New Category Multiplier (1.5x)
**As a** member
**I want to** earn 1.5x bonuses on first purchase in a new category
**So that** I am incentivized to explore the ecosystem

**Acceptance Criteria:**
```gherkin
Scenario: First purchase in Beauty category
  Given I am VIP (7% cashback) and never purchased in Beauty
  When I buy at Миндаль (Beauty) for 10,000₽
  Then I receive 1,050₽ bonuses (7% × 1.5 = 10.5%)
  And I see message "Бонус за новую категорию! +50% бонусов"

Scenario: Subsequent purchases in same category
  Given I already purchased in Beauty
  When I buy at Миндаль again
  Then I receive standard 7% (no multiplier)
```

**Technical Requirements:**
- Track categories visited: `user_categories` table
  ```sql
  user_categories (
    user_id UUID REFERENCES users(id),
    category VARCHAR(50),
    first_purchase_at TIMESTAMP,
    PRIMARY KEY (user_id, category)
  )
  ```
- Check category novelty before accrual: `if category not in user.visited_categories: apply 1.5x multiplier`

---

### User Story 2.1.3: Business-Specific Multipliers (2x/3x)
**As a** member
**I want to** earn bonus multipliers during special promotions
**So that** I maximize my bonuses

**Acceptance Criteria:**
```gherkin
Scenario: Double bonus promotion
  Given Миндаль runs "Двойные бонусы" promotion
  When I purchase 10,000₽ at Миндаль (VIP 7% → 14%)
  Then I receive 1,400₽ bonuses (7% × 2)
  And I see "Активна акция: Двойные бонусы!"

Scenario: Triple bonus promotion
  Given Skinerica runs "Тройные бонусы" promotion
  When I purchase 5,000₽ at Skinerica (Elite 10% → 30%)
  Then I receive 1,500₽ bonuses (10% × 3)
```

**Technical Requirements:**
- Store multipliers in `promotions` table:
  ```sql
  promotions (
    id UUID PRIMARY KEY,
    business_id UUID REFERENCES businesses(id),
    multiplier DECIMAL(3,2),  -- 2.00, 3.00
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
  )
  ```
- Check active promotions before accrual: `SELECT multiplier FROM promotions WHERE business_id=X AND NOW() BETWEEN start_date AND end_date`

---

### User Story 2.1.4: View Bonus Balance
**As a** member
**I want to** see my current bonus balance
**So that** I know how much I can spend

**Acceptance Criteria:**
```gherkin
Scenario: View balance on Home screen
  Given I have 7,250₽ bonuses
  When I open Home screen
  Then I see bonus balance: "7,250₽"
  And I see balance inside gamification ring

Scenario: Balance breakdown
  Given I tap on bonus balance
  Then I see modal with:
    - Available: 7,250₽
    - Pending (from recent purchases): 500₽
    - Total earned (lifetime): 25,000₽
    - Total spent (lifetime): 17,750₽
```

**Technical Requirements:**
- Cache balance in Redis with 5-minute TTL: `bonus:balance:{user_id}`
- Query PostgreSQL for precise balance:
  ```sql
  SELECT SUM(CASE WHEN type='earned' THEN amount ELSE -amount END) as balance
  FROM bonus_transactions
  WHERE user_id = :user_id
  ```

---

### User Story 2.1.5: Bonus Transaction History
**As a** member
**I want to** see all my bonus accruals and redemptions
**So that** I can audit my bonus activity

**Acceptance Criteria:**
```gherkin
Scenario: View bonus history
  Given I tap Profile → "Бонусы и купоны" → "История бонусов"
  When history loads
  Then I see chronological list of bonus transactions:
    - "+500₽ - Покупка в Миндаль - 17 ноября 2025"
    - "-200₽ - Списаны при покупке в Лисичкино - 15 ноября 2025"
    - "+1,000₽ - Реферальный бонус - 10 ноября 2025"

Scenario: Filter history
  Given I am on bonus history screen
  When I select filter "Earned" (only accruals)
  Then I see only "+500₽", "+1,000₽" transactions
```

---

### User Story 2.1.6-2.1.7: Bonus Expiry Warnings
**As a** member
**I want to** receive warnings about expiring bonuses
**So that** I don't lose unused bonuses

**Acceptance Criteria:**
```gherkin
Scenario: 7-day expiry warning
  Given I have 500₽ bonuses expiring in 7 days
  When expiry date approaches
  Then I receive push notification "500₽ бонусов сгорят через 7 дней!"
  And I see warning banner on Home screen

Scenario: Bonus expiry policy (future enhancement)
  Given platform implements 12-month expiry
  When bonuses are >12 months old
  Then they are marked as expired
  And balance is reduced accordingly
  Note: MVP has NO expiry (bonuses never expire while account active)
```

**Technical Requirements:**
- Celery Beat task runs daily: `check_expiring_bonuses()`
- Query bonuses expiring in 7 days: `WHERE expires_at <= NOW() + INTERVAL '7 days'`
- Send push notifications via Module 12

---

### User Story 2.1.8: Auto-Apply Bonuses at Checkout
**As a** member
**I want to** automatically apply bonuses when purchasing
**So that** I don't need to manually redeem

**Acceptance Criteria:**
```gherkin
Scenario: Auto-redeem bonuses
  Given I have 1,000₽ bonuses and I purchase 5,000₽ at Лисичкино
  When checkout occurs (QR scan)
  Then bonuses are auto-applied (if I enabled auto-redeem in settings)
  And I pay 4,000₽ cash + 1,000₽ bonuses
  And I earn new bonuses on 4,000₽ only (not on bonus-paid portion)

Scenario: Manual redemption
  Given I disabled auto-redeem
  When checkout occurs
  Then business staff asks "Использовать бонусы?"
  And I confirm how much to redeem (up to my balance or purchase amount)
```

**Technical Requirements:**
- User setting: `auto_redeem_bonuses BOOLEAN DEFAULT FALSE`
- Redemption logic in transaction creation:
  ```python
  if user.auto_redeem_bonuses and user.bonus_balance > 0:
      redeem_amount = min(user.bonus_balance, transaction.amount)
      transaction.bonus_redeemed = redeem_amount
      transaction.amount_paid = transaction.amount - redeem_amount
  ```

---

### User Story 2.1.9-2.1.10: Bonus Transfer (Gift)
**As a** member
**I want to** transfer bonuses to another member
**So that** I can gift bonuses to friends

**Acceptance Criteria:**
```gherkin
Scenario: Gift bonuses
  Given I have 5,000₽ bonuses
  When I go to Profile → "Подарить бонусы"
  And I enter recipient phone: +7 999 123-45-67
  And I enter amount: 1,000₽
  Then bonuses are transferred to recipient
  And I see confirmation "1,000₽ отправлено Марии П."
  And recipient receives push "Вы получили подарок 1,000₽ от Анны К.!"

Scenario: Transfer limits
  Given I try to transfer more than my balance
  When I enter 10,000₽ (but I only have 5,000₽)
  Then I see error "Недостаточно бонусов. Доступно: 5,000₽"
  
  Given platform enforces daily transfer limit
  When I try to transfer 10,000₽ in one day (limit: 5,000₽/day)
  Then I see error "Превышен дневной лимит переводов (5,000₽)"
```

**Technical Requirements:**
- Bonus transfer table:
  ```sql
  bonus_transfers (
    id UUID PRIMARY KEY,
    sender_user_id UUID REFERENCES users(id),
    recipient_user_id UUID REFERENCES users(id),
    amount DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT NOW()
  )
  ```
- Daily transfer limit enforced: `SELECT SUM(amount) FROM bonus_transfers WHERE sender_user_id=X AND created_at >= NOW() - INTERVAL '24 hours'`

---

### User Story 2.1.11-2.1.13: Bonus Rewards (Birthday, Events, Referrals)
**As a** member
**I want to** earn bonus rewards for special occasions
**So that** I feel valued by the ecosystem

**Acceptance Criteria:**
```gherkin
Scenario: Birthday bonuses
  Given my birthdate is November 17
  When November 17 arrives
  Then I receive 1,000₽ birthday bonuses
  And I see push "С днём рождения! Подарок от Свой Круг: 1,000₽ бонусов"

Scenario: Event participation bonuses
  Given I attended a VIP event
  When event ends and I was marked as attended
  Then I receive 500₽ bonuses as thank-you
  And I see "Спасибо за участие! +500₽ бонусов"

Scenario: Referral bonuses
  Given my friend registered using my referral code
  When she completes registration
  Then I receive 1,000₽ referral bonuses (Module 11)
```

**Technical Requirements:**
- Celery Beat task runs daily: `send_birthday_bonuses()`
- Query users with birthdays today: `SELECT * FROM users WHERE EXTRACT(MONTH FROM birthdate) = :month AND EXTRACT(DAY FROM birthdate) = :day`
- Award bonuses via: `award_bonus(user_id, amount=1000, reason='birthday')`

---

### User Story 2.1.14-2.1.15: Bonus Validation & Notifications
**As a** member
**I want to** receive notifications for all bonus activity
**So that** I am always informed

**Acceptance Criteria:**
```gherkin
Scenario: Minimum balance check for redemption
  Given I have 50₽ bonuses and I try to redeem at checkout
  When minimum redemption is 100₽
  Then I see error "Минимальная сумма списания: 100₽"
  And redemption is blocked until I have 100₽+

Scenario: Bonus accrual notification
  Given I completed a purchase
  When bonuses are accrued
  Then I receive push notification within 1 minute
  And notification shows: amount, business name, multipliers applied

Scenario: Bonus redemption notification
  Given I redeemed 500₽ bonuses
  When transaction completes
  Then I receive push "Списано 500₽ бонусов в Лисичкино"
  And I see new balance
```

---

## 2.2 Status System (12 functions)

### User Story 2.2.1: Automatic Status Calculation
**As a** member
**I want to** have my status calculated automatically based on spending and categories
**So that** I don't need to track manually

**Acceptance Criteria:**
```gherkin
Scenario: Status calculation formula
  Given status is calculated using:
    - Total spend (last 12 months)
    - Categories visited (last 12 months)
  When I have 35,000₽ spent + 3 categories
  Then my status is VIP (≥30,000₽ + ≥3 categories)

Scenario: Recalculation frequency
  Given status is recalculated daily at midnight
  When a new day starts
  Then Celery task recalculates all user statuses
  And users who upgraded receive push notifications
```

**Technical Requirements:**
- Celery Beat task runs daily: `recalculate_all_statuses()`
- Status calculation query:
  ```sql
  SELECT
    user_id,
    SUM(amount) as total_spent,
    COUNT(DISTINCT category) as categories_count
  FROM transactions
  WHERE created_at >= NOW() - INTERVAL '12 months'
  GROUP BY user_id
  ```
- Apply status rules:
  - Insider: 1 purchase
  - VIP: ≥30,000₽ + ≥3 categories
  - Elite: ≥100,000₽ + ≥5 categories OR top 1% spenders
  - Inner Circle: ≥200,000₽ OR invitation-only

---

### User Story 2.2.2-2.2.5: Status Tiers (Insider/VIP/Elite/Inner Circle)
**As a** member
**I want to** understand each status tier requirements
**So that** I know how to upgrade

**Acceptance Criteria:**
```gherkin
Scenario: Insider status (entry level)
  Given I just registered and completed first purchase
  When my status is calculated
  Then I am assigned "Insider" status
  And I receive 5% cashback on all purchases

Scenario: VIP status
  Given I spent 30,000₽+ across 3+ categories in last 12 months
  When status is recalculated
  Then I am upgraded to "VIP"
  And I now receive 7% cashback
  And I unlock priority event registration

Scenario: Elite status
  Given I spent 100,000₽+ across 5+ categories in last 12 months
  OR I am in top 1% of spenders (regardless of categories)
  When status is recalculated
  Then I am upgraded to "Elite"
  And I now receive 10% cashback
  And I unlock event constructor and weighted voting (3x vote weight)

Scenario: Inner Circle status
  Given I spent 200,000₽+ in last 12 months
  OR I received invitation from superadmin
  When status is granted
  Then I become "Inner Circle" (highest tier)
  And I receive 10% cashback + ambassador recognition
```

---

### User Story 2.2.6-2.2.7: Status Progress Visualization
**As a** member
**I want to** see my progress toward next status tier
**So that** I am motivated to increase spending

**Acceptance Criteria:**
```gherkin
Scenario: View progress ring
  Given I am Insider with 15,000₽ spent and 2 categories visited
  When I view Home screen
  Then I see progress ring showing:
    - Spending: 50% (15K of 30K needed for VIP)
    - Categories: 67% (2 of 3 needed for VIP)
    - Overall: 58% (average of both)

Scenario: Progress tooltip
  Given I tap on progress ring
  When tooltip opens
  Then I see "Осталось 15,000₽ и 1 категория до VIP"
  And I see breakdown:
    - Текущие траты: 15,000₽ / 30,000₽
    - Категории: 2 / 3 (Красота, Гастрономия)
    - Рекомендация: "Попробуйте категорию Здоровье"
```

---

### User Story 2.2.8-2.2.9: Status Upgrade Notifications
**As a** member
**I want to** be notified when my status upgrades
**So that** I celebrate the achievement

**Acceptance Criteria:**
```gherkin
Scenario: VIP upgrade notification
  Given I just crossed VIP threshold (30K + 3 categories)
  When daily status recalculation runs
  Then I receive push "Поздравляем! Вы теперь VIP!"
  And I see fullscreen animation with confetti when I open app
  And I see list of new VIP benefits:
    - 7% cashback (up from 5%)
    - Priority event registration
    - Access to VIP-only events

Scenario: Elite upgrade notification
  Given I upgraded to Elite
  When I open app
  Then animation is more elaborate (golden confetti, fanfare sound)
  And I see "Вы достигли Elite статуса - топ-1% участниц!"
```

---

### User Story 2.2.10-2.2.12: Status Privileges & Freeze
**As a** member
**I want to** see my current status privileges
**So that** I understand what I have access to

**Acceptance Criteria:**
```gherkin
Scenario: View status privileges
  Given I am VIP
  When I tap Profile → Status badge → "Привилегии"
  Then I see my VIP benefits:
    - 7% cashback on all purchases
    - Priority event registration (register 24h before Insider)
    - Access to VIP-only events
    - Ability to propose event ideas (event constructor)

Scenario: Compare status tiers
  Given I view privileges screen
  When I tap "Сравнить статусы"
  Then I see comparison table:
    | Feature | Insider | VIP | Elite | Inner Circle |
    | Cashback | 5% | 7% | 10% | 10% |
    | Event constructor | No | Yes | Yes | Yes |
    | Voting weight | 1x | 2x | 3x | 5x |

Scenario: Status freeze (illness/vacation)
  Given I am VIP and going on 2-month vacation
  When I request "Заморозить статус"
  Then my VIP status is frozen for 30 days
  And status downgrade is paused during freeze
  And I can request freeze once per 6 months
```

**Technical Requirements:**
- Status freeze table:
  ```sql
  status_freezes (
    user_id UUID REFERENCES users(id),
    frozen_at TIMESTAMP,
    unfrozen_at TIMESTAMP,
    reason TEXT
  )
  ```
- Exclude frozen periods from status calculation

---

## 2.3 Coupons & Promotions (18 functions)

### User Story 2.3.1-2.3.3: View and Filter Coupons
**As a** member
**I want to** see all my active coupons
**So that** I know what offers are available

**Acceptance Criteria:**
```gherkin
Scenario: View active coupons
  Given I have 3 active coupons
  When I tap Profile → "Бонусы и купоны" → "Купоны"
  Then I see 3 coupon cards:
    - "20% скидка в Миндаль" - expires in 5 days
    - "Двойные бонусы в Skinerica" - expires in 10 days
    - "Бесплатный кофе в Лисичкино" - expires in 2 days

Scenario: Filter by type
  Given I have discount, bonus, and gift coupons
  When I select filter "Скидки"
  Then I see only discount coupons

Scenario: Filter by business
  Given I have coupons for 3 businesses
  When I select "Миндаль"
  Then I see only Миндаль coupons
```

---

### User Story 2.3.4-2.3.6: Activate and Use Coupons
**As a** member
**I want to** activate coupons before using them
**So that** business staff can apply the discount

**Acceptance Criteria:**
```gherkin
Scenario: Activate coupon
  Given I have inactive coupon "20% скидка в Миндаль"
  When I tap "Активировать"
  Then coupon is activated for 1 hour
  And I see activation code: "ABC123"
  And I see countdown timer: "Осталось 59:45"

Scenario: Show code at checkout
  Given I activated coupon
  When I arrive at Миндаль
  Then I tell staff activation code "ABC123"
  And staff enters code in their admin panel
  And discount is applied to my purchase

Scenario: Coupon expiry during activation
  Given coupon activated for 1 hour
  When 1 hour passes
  Then coupon deactivates automatically
  And I can activate again (if still valid)
```

---

### User Story 2.3.7: View Used Coupon History
**As a** member
**I want to** see coupons I used previously
**So that** I can track my savings

**Acceptance Criteria:**
```gherkin
Scenario: View coupon history
  Given I used 10 coupons in past 3 months
  When I tap "История купонов"
  Then I see chronological list:
    - "20% скидка в Миндаль" - Used Nov 15 - Saved 1,000₽
    - "Бесплатный кофе в Лисичкино" - Used Nov 10 - Saved 350₽
  And I see total savings: "Вы сэкономили 15,450₽ за 3 месяца"
```

---

### User Story 2.3.8-2.3.9: Coupon Notifications
**As a** member
**I want to** receive notifications about coupons
**So that** I don't miss offers

**Acceptance Criteria:**
```gherkin
Scenario: New coupon notification
  Given I just completed purchase at Skinerica
  When cross-promo chain triggers coupon for Миндаль
  Then I receive push "Новый купон: 20% скидка в Миндаль!"
  And coupon appears in my "Купоны" list immediately

Scenario: Expiring coupon reminder
  Given I have coupon expiring in 24 hours
  When expiry time approaches
  Then I receive push "Купон сгорает через 24 часа!"
  And coupon card is highlighted in orange in app
```

---

### User Story 2.3.10-2.3.14: Coupon Types
**As a** member
**I want to** use different types of coupons
**So that** I benefit from various promotions

**Acceptance Criteria:**
```gherkin
Scenario: Simple discount coupon (% or fixed)
  Given I have "20% скидка в Миндаль" coupon
  When I purchase 5,000₽ at Миндаль
  Then I pay 4,000₽ (20% discount = 1,000₽ off)
  And I earn bonuses on 4,000₽ (discounted price)

Scenario: Cashback multiplier coupon (2x/3x bonuses)
  Given I have "Тройные бонусы в Skinerica" coupon (Elite, normally 10%)
  When I purchase 10,000₽ at Skinerica
  Then I earn 3,000₽ bonuses (10% × 3 = 30%)

Scenario: Cross-promo coupon (purchase in A → discount in B)
  Given I have "Купите в Skinerica → 500₽ бонусов в Миндаль"
  When I purchase at Skinerica
  Then 500₽ bonus coupon for Миндаль is auto-generated
  And I receive push notification

Scenario: Bundle coupon (2-5 businesses, combined discount)
  Given I have "Пакет Красота: Миндаль + Skinerica за 15,000₽"
  When I activate bundle
  Then I must visit both businesses within 30 days
  And total price is capped at 15,000₽ (vs. 20,000₽ individual)

Scenario: Gift coupon (free item/service)
  Given I have "Бесплатный кофе в Лисичкино (при покупке от 1,000₽)"
  When I purchase 1,200₽ at Лисичкино
  Then free coffee (350₽ value) is added to my order
  And I pay only 1,200₽
```

---

### User Story 2.3.15-2.3.18: Coupon Management
**As a** member
**I want to** manage my coupons effectively
**So that** I use them optimally

**Acceptance Criteria:**
```gherkin
Scenario: Find nearest location to use coupon
  Given I have coupon for business with 3 locations
  When I tap "Использовать рядом"
  Then I see map with 3 pins
  And I see nearest location: "Миндаль, ул. Тверская 10 (2 км)"

Scenario: Auto-apply coupon at checkout
  Given I have active coupon for Миндаль
  When I scan QR at Миндаль checkout
  Then coupon is auto-applied (if conditions met)
  And discount is reflected in transaction

Scenario: Cancel activated coupon
  Given I activated coupon but changed plans
  When I tap "Отменить активацию"
  Then coupon returns to inactive state
  And I can activate it later (before expiry date)

Scenario: Share coupon with friend (if transferable)
  Given I have transferable coupon
  When I tap "Поделиться"
  Then I can send coupon to friend's phone number
  And coupon moves from my account to theirs
```

---

## 📊 Technical Requirements

### Bonus System Architecture
- **Database:** PostgreSQL for ACID transactions
  ```sql
  bonuses (
    user_id UUID PRIMARY KEY REFERENCES users(id),
    balance DECIMAL(10,2) DEFAULT 0,
    lifetime_earned DECIMAL(10,2) DEFAULT 0,
    lifetime_spent DECIMAL(10,2) DEFAULT 0,
    updated_at TIMESTAMP DEFAULT NOW()
  )
  
  bonus_transactions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    amount DECIMAL(10,2),
    type VARCHAR(20),  -- 'earned' | 'redeemed' | 'gifted' | 'expired'
    transaction_id UUID REFERENCES transactions(id),
    reason TEXT,
    created_at TIMESTAMP DEFAULT NOW()
  )
  ```
- **Cache:** Redis for bonus balance (5-min TTL)
- **Async tasks:** Celery for birthday bonuses, expiry checks

### Status System Architecture
- **Calculation frequency:** Daily at midnight (Celery Beat)
- **Rolling 12-month window:** Use PostgreSQL window functions
- **Status transition log:**
  ```sql
  status_history (
    user_id UUID REFERENCES users(id),
    old_status VARCHAR(20),
    new_status VARCHAR(20),
    changed_at TIMESTAMP DEFAULT NOW()
  )
  ```

### Coupon System Architecture
- **Coupon table:**
  ```sql
  coupons (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    business_id UUID REFERENCES businesses(id),
    type VARCHAR(20),  -- 'discount' | 'bonus_multiplier' | 'cross_promo' | 'bundle' | 'gift'
    discount_type VARCHAR(20),  -- 'percent' | 'fixed' | 'multiplier'
    discount_value DECIMAL(10,2),
    min_purchase_amount DECIMAL(10,2),
    expires_at TIMESTAMP,
    activated_at TIMESTAMP NULL,
    redeemed_at TIMESTAMP NULL,
    activation_code VARCHAR(10) NULL
  )
  ```
- **Activation flow:**
  1. User taps "Activate"
  2. Generate 6-character activation code: `generate_activation_code()`
  3. Set `activated_at = NOW()`, `activation_code = ABC123`
  4. Return code to mobile app
  5. Auto-deactivate after 1 hour if not used
- **Redemption flow:**
  1. Business staff enters activation code
  2. Backend validates code: `GET /api/v1/coupons/validate?code=ABC123`
  3. Apply discount to transaction
  4. Set `redeemed_at = NOW()`

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

**Bonus Balance Card:**
- Displays current bonus balance prominently on Home screen within gamification ring
- Large typography (22px/600) showing "7,250₽" with Tiffany Blue accent
- Tappable to reveal modal with breakdown: Available/Pending/Lifetime earned/Lifetime spent
- Card background: white with subtle shadow, border-radius 12px

**Tier Progress Visualization:**
- Circular progress ring showing overall progress toward next tier
- Inner ring: spending progress (% of 30K/100K/200K needed)
- Outer ring: category count progress (% of 3/5 categories)
- Center shows current tier name and % complete (e.g., "Insider 58%")
- Tappable for tooltip: "Осталось 15,000₽ и 1 категория до VIP"
- Uses Tiffany Blue for progress fill, light gray for background

**Coupon Cards:**
- Grid of redeemable coupons with business logo, discount description, expiry date
- "Активировать" button with countdown timer when active
- Status badge (Active/Expired/Redeemed) using semantic colors
- Swipe to reveal details: min purchase amount, T&C, shared coupon option
- Empty state: "У вас нет активных купонов. Совершите покупку!"

**Redemption Flow:**
- QR scan at checkout triggers auto-redeem (if enabled) or manual selection
- Confirmation dialog showing: bonus amount, cash amount, new balance after redemption
- Tiffany Blue "Подтвердить" button, gray "Отменить" button
- Real-time balance update after redemption

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

- **Module 3 (Transactions):** Trigger bonus accrual after each transaction
- **Module 5 (Cross-Promo):** Generate cross-promo coupons automatically
- **Module 8 (CRM Integrations):** Sync transaction data for bonus calculation
- **Module 12 (Notifications):** Send push notifications for bonuses, status upgrades, coupons

---

## ✅ Success Criteria

- [ ] All 45 functions implemented and tested
- [ ] Bonus accrual latency: <1 minute after transaction
- [ ] Status calculation: 100% accuracy with daily refresh
- [ ] Coupon activation: <500ms response time
- [ ] 0 bonus balance discrepancies (audit log validation)
- [ ] 95%+ coupon activation rate (members use coupons effectively)
- [ ] Status upgrade push notifications: 100% delivery rate

---

**Last Updated:** 2025-11-17
**Owner:** Backend Team
**Status:** Critical - MVP Required
