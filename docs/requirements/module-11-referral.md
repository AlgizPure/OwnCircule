# Module 11: Referral Program - Requirements

**Module ID:** MOD-11
**Total Functions:** 10
**Priority:** P1 (Important - v1.5)
**Dependencies:** Module 1 (Mobile App), Module 2 (Loyalty System), Module 12 (Notifications)
**Tech Stack:** React Native 0.81, PostgreSQL 16.11, Deep linking (React Navigation)

---

## 📋 Module Overview

Referral program incentivizes members to invite friends by rewarding both parties with bonuses. Members receive unique referral codes/links, track invitations, earn "Ambassador" status for 3+ referrals, and compete on monthly leaderboards. Drives viral growth with minimal CAC.

**Key Features:**
- Unique referral link & code generation
- Invitation tracking (invited count, registration status)
- Dual rewards (1000₽ bonuses each)
- Ambassador status for 3+ referrals
- "Друг клуба" badge
- Monthly leaderboard (Top-10)
- Invitation history
- Social sharing integration
- Referral analytics (conversion rate, active referrals)

---

## User Story 11.1-11.2: Generate Referral Link & Code
**As a** member
**I want to** generate my unique referral link and code
**So that** I can invite friends easily

**Acceptance Criteria:**
```gherkin
Scenario: View referral section
  Given I am logged in
  When I go to Profile → "Пригласить подругу"
  Then I see my referral details:
    - Referral code: "ABC123" (6-character alphanumeric)
    - Referral link: "https://svoykrug.ru/ref/ABC123"
    - QR code containing referral link
  And I see stats: "Вы пригласили 2 подруги"

Scenario: Copy referral code
  Given I am on referral screen
  When I tap "Скопировать код"
  Then code is copied to clipboard
  And I see toast "Код скопирован: ABC123"

Scenario: Copy referral link
  Given I am on referral screen
  When I tap "Скопировать ссылку"
  Then link is copied to clipboard
```

**Technical Requirements:**
- Generate unique 6-character code on first profile view: `generate_referral_code(user_id) -> str`
- Code format: [A-Z0-9], collision-free (check uniqueness)
- Store in `users` table: `referral_code VARCHAR(6) UNIQUE NOT NULL`
- Link format: `https://svoykrug.ru/ref/{code}` (deep link to app if installed, web landing if not)

---

## User Story 11.3: Track Invitations
**As a** member
**I want to** see how many friends I invited
**So that** I know my referral progress

**Acceptance Criteria:**
```gherkin
Scenario: View invitation count
  Given I invited 3 friends (2 registered, 1 pending)
  When I view referral screen
  Then I see:
    - "Приглашено подруг: 3"
    - "Зарегистрировались: 2"
    - "Ожидают регистрации: 1"
  And I see progress bar toward Ambassador status (3/3 = 100%)

Scenario: No invitations yet
  Given I haven't invited anyone
  When I view referral screen
  Then I see "Пригласите подруг и получите бонусы!"
  And I see CTA button "Поделиться ссылкой"
```

**Technical Requirements:**
- Track referrals in `referrals` table:
  ```sql
  referrals (
    id UUID PRIMARY KEY,
    referrer_user_id UUID REFERENCES users(id),
    referred_user_id UUID REFERENCES users(id),
    status VARCHAR(20) DEFAULT 'pending',  -- 'pending' | 'registered' | 'active'
    created_at TIMESTAMP DEFAULT NOW()
  )
  ```
- Status transitions:
  - `pending`: Friend clicked link but hasn't completed registration
  - `registered`: Friend completed registration
  - `active`: Friend made first purchase (optional future enhancement)

---

## User Story 11.4: Dual Rewards
**As a** member
**I want to** receive bonuses when my friend registers
**So that** we both benefit from the referral

**Acceptance Criteria:**
```gherkin
Scenario: Friend registers with referral code
  Given Anna invited Maria using referral code "ABC123"
  When Maria completes registration and enters "ABC123"
  Then both users receive 1000₽ bonuses
  And Anna sees push "Мария зарегистрировалась! +1000₽ бонусов"
  And Maria sees push "Приветственный бонус +1000₽ от подруги Анны"
  
Scenario: Invalid referral code
  Given Maria enters code "INVALID"
  When she submits registration
  Then she sees error "Неверный реферальный код"
  And registration continues without referral bonuses
```

**Technical Requirements:**
- Validate referral code on registration: `GET /api/v1/referrals/validate?code=ABC123`
- Apply bonuses after registration via Celery task: `apply_referral_bonuses(referrer_id, referred_id, amount=1000)`
- Store referral relationship in `referrals` table with status='registered'
- Send push notifications to both parties (Module 12)

---

## User Story 11.5-11.6: Ambassador Status & Badge
**As a** member
**I want to** earn Ambassador status for 3+ referrals
**So that** I am recognized as a top contributor

**Acceptance Criteria:**
```gherkin
Scenario: Reach Ambassador status
  Given I have 2 registered referrals
  When my 3rd referral completes registration
  Then I receive Ambassador status
  And I see push "Поздравляем! Вы стали Амбассадором клуба!"
  And I see "Друг клуба" badge in my profile
  And my profile header shows "Амбассадор" tag

Scenario: Ambassador benefits (future)
  Given I am an Ambassador
  When I view benefits screen
  Then I see special perks:
    - Priority event access
    - Exclusive Ambassador-only events
    - Additional 2% cashback on all purchases
```

**Technical Requirements:**
- Add `is_ambassador BOOLEAN DEFAULT FALSE` to `users` table
- Trigger Ambassador status check after each referral registration
- Award "Друг клуба" badge (Module 14 - Gamification)

---

## User Story 11.7: Monthly Leaderboard
**As a** member
**I want to** see top-10 referrers of the month
**So that** I am motivated to invite more friends

**Acceptance Criteria:**
```gherkin
Scenario: View leaderboard
  Given it's November 2025
  When I go to Referral screen → "Топ рефереров"
  Then I see Top-10 members with most referrals this month:
    1. Anna K. - 15 referrals
    2. Maria P. - 12 referrals
    ...
    10. Olga S. - 5 referrals
  And I see my rank: "#12 (4 referrals)"
  And I see message "Пригласите ещё 1 подругу, чтобы войти в Топ-10!"

Scenario: Top-3 rewards (optional)
  Given it's end of month
  When leaderboard is finalized
  Then Top-3 referrers receive bonus prizes:
    - 1st place: +5000₽ bonuses
    - 2nd place: +3000₽ bonuses
    - 3rd place: +2000₽ bonuses
```

**Technical Requirements:**
- Calculate monthly leaderboard via Celery task (daily refresh)
- Query: `SELECT referrer_user_id, COUNT(*) FROM referrals WHERE created_at >= '2025-11-01' AND status='registered' GROUP BY referrer_user_id ORDER BY COUNT(*) DESC LIMIT 10`
- Cache leaderboard in Redis with 24-hour TTL
- Reset leaderboard on 1st of each month

---

## User Story 11.8: Invitation History
**As a** member
**I want to** see details of friends I invited
**So that** I can track their registration status

**Acceptance Criteria:**
```gherkin
Scenario: View invitation list
  Given I invited 5 friends
  When I tap "История приглашений"
  Then I see list of invitations:
    1. Мария П. - Зарегистрировалась 15 ноября - VIP
    2. Елена К. - Зарегистрировалась 10 ноября - Insider
    3. Анна С. - Ожидает регистрации (приглашена 5 ноября)
  And I see each friend's current status tier (if registered)
  And I see bonuses earned from each referral: +1000₽

Scenario: Friend hasn't registered yet
  Given I invited a friend 7 days ago
  When I view invitation history
  Then I see "Ожидает регистрации (7 дней назад)"
  And I see "Напомнить" button → sends reminder via SMS/WhatsApp
```

---

## User Story 11.9: Share Referral Link
**As a** member
**I want to** share my referral link via social media/messengers
**So that** I reach friends easily

**Acceptance Criteria:**
```gherkin
Scenario: Share via native share sheet
  Given I am on referral screen
  When I tap "Поделиться ссылкой"
  Then I see native share sheet (iOS/Android)
  And I can share via:
    - WhatsApp (most common in Russia)
    - Telegram
    - Instagram DM
    - VKontakte
    - Copy to clipboard
  And the shared message is:
    "Привет! Присоединяйся к Свой Круг — премиум-клубу для женщин. 
     Получи 1000₽ бонусов при регистрации: https://svoykrug.ru/ref/ABC123"

Scenario: Share QR code
  Given I am on referral screen
  When I tap "Поделиться QR-кодом"
  Then I see QR code fullscreen (can be screenshot)
  And friend can scan QR to open referral link
```

**Technical Requirements:**
- Use React Native Share API: `Share.share({ message, url })`
- Deep linking: Referral link opens app if installed, web landing page otherwise
- Web landing page collects email/phone, downloads app with pre-filled referral code

---

## User Story 11.10: Referral Analytics
**As a** member
**I want to** see my referral conversion rate
**So that** I optimize my invitation strategy

**Acceptance Criteria:**
```gherkin
Scenario: View referral analytics
  Given I invited 10 friends (7 registered, 3 pending)
  When I tap "Аналитика"
  Then I see:
    - Conversion rate: 70% (7 registered / 10 invited)
    - Active referrals: 5 (made at least 1 purchase)
    - Inactive referrals: 2 (registered but no purchases)
    - Total bonuses earned: 7000₽ (7 × 1000₽)
    - Average time to registration: 2.5 days

Scenario: Identify inactive referrals
  Given I have 2 inactive referrals (registered but no purchases)
  When I view analytics
  Then I see their names + registration date
  And I see "Напомните им о бонусах!" CTA
```

---

## 📊 Technical Requirements

### Database Schema
```sql
referrals (
  id UUID PRIMARY KEY,
  referrer_user_id UUID REFERENCES users(id),
  referred_user_id UUID REFERENCES users(id) NULL,  -- NULL until registration
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW(),
  registered_at TIMESTAMP NULL,
  first_purchase_at TIMESTAMP NULL
)

CREATE INDEX idx_referrals_referrer ON referrals(referrer_user_id);
CREATE INDEX idx_referrals_status ON referrals(status);
```

### API Endpoints
- `GET /api/v1/referrals/code` - Get user's referral code
- `POST /api/v1/referrals/validate?code=ABC123` - Validate referral code
- `GET /api/v1/referrals/stats` - Referral analytics for user
- `GET /api/v1/referrals/leaderboard?month=2025-11` - Monthly Top-10
- `GET /api/v1/referrals/history` - Invitation list

### Deep Linking
- URL scheme: `svoykrug://ref/{code}`
- Fallback: `https://svoykrug.ru/ref/{code}` redirects to app store if app not installed
- Use React Navigation for deep link handling

---

## 🔄 Dependencies

- **Module 1 (Mobile App):** Referral UI screens
- **Module 2 (Loyalty System):** Bonus accrual logic
- **Module 12 (Notifications):** Push notifications for referral milestones

---

## ✅ Success Criteria

- [ ] All 10 functions implemented
- [ ] Referral link clicks: 40% conversion to registration (target)
- [ ] Average 2.5 referrals per active member
- [ ] 20% of new members arrive via referrals (vs. paid ads)
- [ ] Ambassador status achieved by 5% of members

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Mobile Teams
**Status:** Ready for v1.5 Development
