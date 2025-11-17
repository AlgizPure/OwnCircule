# Module 14: Gamification & Badges - Requirements

**Module ID:** MOD-14
**Total Functions:** 7
**Priority:** P2 (Nice-to-have - v2.0)
**Dependencies:** Module 1 (Mobile App), Module 2 (Status System), Module 11 (Referral)
**Tech Stack:** React Native 0.81, Lottie animations, PostgreSQL 16.11

---

## 📋 Module Overview

Gamification system awards badges for achievements (category exploration, event attendance, referrals, spending milestones) to increase engagement and retention. Badges are displayed in user profiles and trigger celebratory animations when earned.

**Key Features:**
- 9 category badges (Beauty, Cosmetology, Dentistry, Medicine, Gastronomy, Floristry, Optics, Textiles, Legal Services)
- Special badges: Первопроходец (first registration), Друг клуба (3+ referrals), Тусовщица (10+ events), Коллекционер (all 9 categories), Инвестор (250K+ spent)
- Animated badge unlock with confetti/celebration
- Badge showcase in profile
- Badge rarity levels (common, rare, legendary)

---

## Function B.1: Category Badges (9 badges)
**As a** member
**I want to** earn badges for purchasing in different categories
**So that** I am incentivized to explore the ecosystem

**Acceptance Criteria:**
```gherkin
Scenario: Earn Beauty badge
  Given I have 0 purchases in Beauty category
  When I complete my first purchase at Миндаль (Beauty)
  Then I earn "Красавица" badge
  And I see fullscreen animation with badge icon + confetti
  And I see message "Новый бейдж: Красавица! Вы посетили категорию Красота"

Scenario: All 9 category badges
  The 9 categories are:
    1. Красота (Beauty) - Миндаль
    2. Косметология (Cosmetology) - Skinerica
    3. Стоматология (Dentistry) - Стим Центр
    4. Медицина (Medicine) - Миллениум
    5. Гастрономия (Gastronomy) - Лисичкино
    6. Флористика (Floristry) - Future partner
    7. Оптика (Optics) - Future partner
    8. Текстиль (Textiles) - Future partner
    9. Юридические услуги (Legal Services) - Future partner
  Each badge is earned on first purchase in that category

Scenario: View earned badges
  Given I earned 3 category badges
  When I view Profile → "Бейджи"
  Then I see 3 earned badges (colored icons)
  And I see 6 locked badges (grayscale icons with padlock)
  And I see progress: "3 из 9 категорий"
```

**Technical Requirements:**
- Badge table:
  ```sql
  badges (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),  -- 'beauty' | 'cosmetology' | ... | 'special'
    icon_url VARCHAR(255),
    rarity VARCHAR(20) DEFAULT 'common',  -- 'common' | 'rare' | 'legendary'
    description TEXT
  )
  
  user_badges (
    user_id UUID REFERENCES users(id),
    badge_id UUID REFERENCES badges(id),
    earned_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (user_id, badge_id)
  )
  ```
- Trigger badge check after every transaction: `check_category_badge(user_id, category)`

---

## Function B.2: Первопроходец Badge (Pioneer)
**As a** new member
**I want to** receive a "Pioneer" badge upon registration
**So that** I feel welcomed and special

**Acceptance Criteria:**
```gherkin
Scenario: Earn Первопроходец badge
  Given I just completed registration
  When my account is created
  Then I automatically earn "Первопроходец" badge
  And I see welcome animation: "Добро пожаловать! Вы теперь Первопроходец клуба!"
  And badge is displayed in my profile

Scenario: Badge rarity
  Given Первопроходец badge is "common" rarity
  When I view badge details
  Then I see "Редкость: Обычный"
  And I see description: "Вы одна из первых участниц Свой Круг!"
```

---

## Function B.3: Друг клуба Badge (Club Friend)
**As a** member
**I want to** earn "Club Friend" badge for 3+ referrals
**So that** I am recognized as a contributor

**Acceptance Criteria:**
```gherkin
Scenario: Earn Друг клуба badge
  Given I invited 2 friends (registered)
  When my 3rd referral completes registration
  Then I earn "Друг клуба" badge (rarity: Rare)
  And I see animation: "Поздравляем! Вы Друг клуба!"
  And I see badge in profile with "Редкость: Редкий"

Scenario: Badge linked to Ambassador status
  Given I earned Друг клуба badge
  When I view my profile
  Then I also have Ambassador status (Module 11)
  And both are displayed prominently
```

---

## Function B.4: Тусовщица Badge (Party Girl)
**As a** member
**I want to** earn "Party Girl" badge for attending 10+ events
**So that** I am recognized as active community member

**Acceptance Criteria:**
```gherkin
Scenario: Earn Тусовщица badge
  Given I attended 9 events
  When I check-in to my 10th event
  Then I earn "Тусовщица" badge (rarity: Rare)
  And I see celebration animation
  And badge is added to my profile

Scenario: Badge visibility
  Given I earned Тусовщица badge
  When other members view my profile (if social features enabled)
  Then they see my badge collection
  And they are motivated to earn badges too
```

---

## Function B.5: Коллекционер Badge (Collector)
**As a** member
**I want to** earn "Collector" badge for visiting all 9 categories
**So that** I am recognized as ecosystem explorer

**Acceptance Criteria:**
```gherkin
Scenario: Earn Коллекционер badge
  Given I have 8 category badges
  When I earn my 9th category badge
  Then I earn "Коллекционер" badge (rarity: Legendary)
  And I see epic animation with golden confetti
  And I see message "Легендарный бейдж: Коллекционер! Вы посетили все категории!"
  And I receive bonus reward: +5000₽ bonuses

Scenario: Badge rarity display
  Given Коллекционер is Legendary rarity
  When I view badge in profile
  Then badge has golden border
  And it pulses with glow animation
```

---

## Function B.6: Инвестор Badge (Investor)
**As a** member
**I want to** earn "Investor" badge for spending 250,000+ rubles
**So that** I am recognized as high-value member

**Acceptance Criteria:**
```gherkin
Scenario: Earn Инвестор badge
  Given my total lifetime spend is 245,000₽
  When I complete a purchase bringing total to 250,000₽
  Then I earn "Инвестор" badge (rarity: Legendary)
  And I see celebration animation
  And I receive bonus reward: +10,000₽ bonuses
  And badge is displayed in profile with "Редкость: Легендарный"

Scenario: Multi-tier investor badges (future)
  Given Инвестор badge is earned at 250K
  When I reach 500K spend
  Then I earn "Супер Инвестор" badge (higher tier)
  When I reach 1M spend
  Then I earn "Платиновый Инвестор" badge (ultimate tier)
```

---

## Function B.7: Badge Unlock Animation
**As a** member
**I want to** see a celebratory animation when earning badges
**So that** the achievement feels rewarding

**Acceptance Criteria:**
```gherkin
Scenario: Badge animation (common rarity)
  Given I earn a common badge (e.g., Beauty category)
  When badge is unlocked
  Then I see fullscreen modal with:
    - Badge icon animates from small to large (scale 0 → 1)
    - Confetti falls from top (pastel colors)
    - Sound effect (optional, user can disable)
    - Message: "Новый бейдж: Красавица!"
    - CTA button: "Посмотреть все бейджи"
  And animation plays for 3 seconds
  And I can tap anywhere to dismiss

Scenario: Badge animation (legendary rarity)
  Given I earn a legendary badge (e.g., Коллекционер)
  When badge is unlocked
  Then I see enhanced animation:
    - Badge rotates 360° with glow effect
    - Golden confetti + sparkles
    - Fanfare sound effect
    - Message with exclamation: "Легендарный бейдж!"
  And animation plays for 5 seconds

Scenario: Animation library
  Given animations need to be smooth
  When implementing badge animations
  Then use Lottie animations (react-native-lottie) for performance
  And preload animation JSON files on app start
```

**Technical Requirements:**
- Use `lottie-react-native` for animations
- Animation files: JSON format, hosted on CDN
- Animations:
  - `badge_common.json` - Simple confetti
  - `badge_rare.json` - Enhanced confetti + badge glow
  - `badge_legendary.json` - Golden confetti + sparkles + rotation
- Trigger animation after badge is saved to database
- Show animation on top of current screen (fullscreen modal)

---

## 📊 Technical Requirements

### Badge System Flow
1. User performs action (purchase, referral, event attendance)
2. Backend checks if action unlocks badge: `check_badge_unlock(user_id, action_type, metadata)`
3. If badge earned, insert into `user_badges` table
4. Send push notification: "Новый бейдж: {badge_name}!"
5. Next app open, show badge animation

### Badge Categories
- **Category badges (9):** Earned on first purchase in category
- **Special badges (5):** 
  - Первопроходец (registration)
  - Друг клуба (3+ referrals)
  - Тусовщица (10+ events)
  - Коллекционер (all 9 categories)
  - Инвестор (250K+ spend)

### Rarity Levels
- **Common (8):** Category badges + Первопроходец
- **Rare (2):** Друг клуба, Тусовщица
- **Legendary (2):** Коллекционер, Инвестор

### Badge Display
- Profile screen: Grid of badge icons (3 per row)
- Earned badges: Full-color icons
- Locked badges: Grayscale with padlock overlay
- Badge detail modal: Large icon, name, description, rarity, earned date

---

## 🔄 Dependencies

- **Module 1 (Mobile App):** Badge UI + animations
- **Module 2 (Loyalty):** Track spending for Инвестор badge
- **Module 4 (Events):** Track event attendance for Тусовщица badge
- **Module 11 (Referral):** Track referrals for Друг клуба badge

---

## ✅ Success Criteria

- [ ] All 14 badges implemented (9 category + 5 special)
- [ ] Badge unlock rate: 60% of members earn 3+ badges within 6 months
- [ ] Animation performance: 60 FPS on all devices
- [ ] Badge showcase increases profile views by 20%
- [ ] Коллекционер badge earned by 5% of members (category exploration goal)

---

**Last Updated:** 2025-11-17
**Owner:** Mobile + Backend Teams
**Status:** v2.0 Feature
