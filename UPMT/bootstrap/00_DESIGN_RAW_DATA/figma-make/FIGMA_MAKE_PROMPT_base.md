# PROJECT: Свой Круг (Own Circle)

## CONTEXT & PURPOSE

**What we're building:**
Свой Круг — это премиум женский клуб с кросс-промо между бизнесами. Закрытая экосистема лояльности для женщин 30-50 лет с доходом 80K+ рублей/месяц в Москве. Объединяет бизнесы категорий: косметология, стоматология, салоны красоты, медцентры, гастромаркеты.

**Target users:**
- **Primary:** Женщины 30-50 лет, доход 80K+/месяц, траты на бьюти/wellness 15-30K/месяц
- **Secondary:** Собственники премиум бизнесов (красота, здоровье, гастрономия)
- **Persona:** Анна, 38 лет, руководитель отдела, посещает косметолога 2 раза/месяц, салон 1 раз/неделю, ищет выгоды и эксклюзивность

**Core value:**
- Unified Loyalty: Один клуб вместо 10+ разрозненных программ лояльности
- Smart Cross-Promo: Покупка в бизнесе A → автоматический купон в бизнес B
- Status & Rewards: Insider → VIP → Elite → Inner Circle с растущим кешбэком (5% → 10%)
- Premium Community: Закрытые мероприятия только для VIP+ участниц

**Type:**
Mobile app (iOS + Android) + Web admin panels

---

## VISUAL DIRECTION

### Style & Mood
Luxury premium women's club meets modern fintech elegance. Inspired by Tiffany & Co aesthetics combined with sleek app UI like Revolut/N26.

- **Feel:** Luxurious, exclusive, elegant, yet approachable
- **Inspiration:** Tiffany & Co (jewelry luxury), Hermès app (premium), Revolut (modern fintech), Linear (clean UI)
- **Aesthetic:** Clean, sophisticated, with touches of luxury (subtle gradients, refined animations, premium feel)

### Color Strategy
**Primary:** #0ABAB5 (Tiffany Blue) - Brand identity, primary actions, status indicators
**Secondary:** #2A2D34 (Charcoal) - Text, headers, professional contrast
**Accent:** #E6C9A8 (Champagne Gold) - Premium touches, highlights, VIP features

**Semantic:**
- Success: #10B981 (emerald green) - Confirmations, positive states, bonuses accrued
- Warning: #F59E0B (amber) - Cautions, pending actions, expiring bonuses
- Error: #EF4444 (red) - Errors, destructive actions, failed transactions
- Info: #3B82F6 (blue) - Helpful information, tips, new features

**Neutrals:**
- Background: #FFFFFF (pure white) - Main background
- Surface: #F9FAFB (light gray) - Cards, elevated surfaces
- Text Primary: #111827 (near black) - Main text
- Text Secondary: #6B7280 (gray) - Secondary text, labels
- Border: #E5E7EB (light gray) - Dividers, borders

**Status Tier Colors:**
- Insider: #94A3B8 (slate gray) - Entry level
- VIP: #A855F7 (purple) - Premium tier
- Elite: #E6C9A8 (champagne gold) - Top tier
- Inner Circle: #0ABAB5 (tiffany blue) - Exclusive invitation-only

### Typography
**Primary Font:** SF Pro Display (iOS) / Roboto (Android) - For headings and emphasis
**Body Font:** SF Pro Text (iOS) / Roboto (Android) - For readable text
**Mono Font:** SF Mono - For codes, transaction IDs

**Scale:**
- Display: 34px / 700 (semibold) - Hero titles
- H1: 28px / 700 - Screen titles
- H2: 22px / 600 - Section headers
- H3: 18px / 600 - Card titles
- Body: 16px / 400 - Primary text
- Small: 14px / 400 - Secondary text
- Caption: 12px / 400 - Labels, hints

### Spacing System
Based on 8px base unit:
- xs: 4px (0.5x)
- sm: 8px (1x)
- md: 16px (2x)
- lg: 24px (3x)
- xl: 32px (4x)
- 2xl: 48px (6x)

### Other Foundations
**Border Radius:**
- Small: 8px (inputs, small cards, tags)
- Medium: 12px (cards, modals, buttons)
- Large: 20px (hero sections, prominent cards)
- Full: 9999px (pills, avatars, status badges)

**Shadows:**
- Subtle: 0 1px 2px rgba(0,0,0,0.05)
- Default: 0 4px 6px rgba(0,0,0,0.1)
- Emphasis: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)

**Transitions:**
- Fast: 150ms (hovers, micro-interactions)
- Base: 300ms (standard animations, modals)
- Slow: 500ms (page transitions, complex animations)

---

## APPLICATION STRUCTURE

### Core Modules & Screens

#### MODULE 1: Mobile App (Frontend)
**Purpose:** Primary user interface for club members
**Priority:** must_have

**User Actions in this module:**

**1.1 Authentication & Onboarding (12 functions)**
- Экран приветствия с видео-презентацией клуба (30 сек, skippable)
- Слайды с преимуществами клуба (3 слайда with smooth swipe)
- Регистрация по телефону с SMS-подтверждением (Russian +7 format)
- Ввод персональных данных (имя, фамилия, email, дата рождения, город)
- Валидация полей в реальном времени (red/green indicators)
- Ввод реферального кода при регистрации (optional, highlighted if present)
- Согласие на обработку персональных данных (152-ФЗ compliance, checkbox)
- Вход по телефону + SMS-код (OTP 6 digits)
- Вход по FaceID/TouchID (biometric, after first setup)

**Screens needed:**
1. **Welcome Screen** - Video introduction to club
   - Layout: Full-screen video with overlay text
   - Key elements: Brand logo, video player, "Skip" button (top-right), "Get Started" CTA
   - Actions: Watch video, Skip, Start registration

2. **Benefits Carousel** - 3 slides explaining value
   - Layout: Swipeable cards with illustrations
   - Key elements: Illustration, headline, description, progress dots, "Next"/"Skip"
   - Actions: Swipe through slides, Skip to registration

3. **Phone Registration** - Enter phone number
   - Layout: Centered form
   - Key elements: Large phone input (Russian mask +7 XXX XXX-XX-XX), "Send Code" button
   - Actions: Enter phone, Request SMS code

4. **SMS Verification** - Enter OTP code
   - Layout: Centered with large OTP inputs (6 digits)
   - Key elements: 6 digit boxes, "Resend code" link, countdown timer (5 minutes)
   - Actions: Enter code, Resend if expired

5. **Profile Setup** - Complete profile information
   - Layout: Vertical form with sections
   - Key elements: Avatar upload, Name/Email/Birthdate fields, City selector, Submit button
   - Actions: Fill form, Upload photo, Submit

6. **Consent Screens** - 152-ФЗ compliance
   - Layout: Legal text with checkbox
   - Key elements: Text scroll view, checkboxes for each consent, "I Agree" button
   - Actions: Read, Accept, Proceed

**UI Components required:**
- Text Input (with Russian phone mask, real-time validation)
- Button (Primary CTA style with Tiffany Blue)
- OTP Input (6 large boxes, auto-focus next)
- Image Upload (avatar with crop functionality)
- Checkbox (styled, Material Design 3)
- Video Player (with play/pause, skip controls)

**1.2 Home Screen (10 functions)**
- Отображение аватара пользователя и уровня статуса (top left, with tier badge)
- Кнопка уведомлений с badge (top right, unread count)
- Быстрый доступ к QR-коду (prominent card, center-top)
- Кольцо прогресса (Gamification Ring) - визуализация статуса (circular progress bar)
- Процент выполнения до следующего статуса (e.g., "75% to VIP")
- Анимация при достижении нового статуса (confetti, badge animation)
- Карусель текущих акций и активных бонусов (horizontal scroll cards)
- Таймер сгорания купонов/бонусов (countdown, red if <3 days)
- AI-рекомендации "Попробуйте новое" (personalized suggestions)
- Карточки ближайших мероприятий (dates, registration status)

**Screens needed:**
1. **Home Dashboard** - Central hub
   - Layout: Scrollable vertical stack
   - Key elements: Status card (QR + ring), promo carousel, events section, recommendations
   - Actions: View QR, Browse promos, Register for event, Tap recommendations

**UI Components required:**
- Status Card (avatar, tier badge, circular progress ring, QR access button)
- Carousel (horizontal scrollable cards with snap-to-grid)
- Countdown Timer (visual countdown with color changes)
- Notification Bell (with badge indicator)
- Recommendation Cards (AI-powered suggestions with images)

**1.3 QR Wallet (8 functions)**
- Генерация и отображение уникального QR-кода (large, centered, animated generation)
- Отображение уникального ID участницы (below QR, monospace font)
- Визуальный бейдж статуса (Insider/VIP/Elite/Inner Circle - colored banner)
- Крупное отображение баланса бонусов (prominent, Tiffany Blue color)
- Автоматическое увеличение яркости экрана до 100% (on screen open)
- Режим "Экран не гаснет" (keep screen awake while QR open)
- Поворот QR-кода для удобства сканирования (rotate button)
- Интеграция с Apple Wallet / Google Pay (add to wallet button)

**Screens needed:**
1. **QR Code Screen** - Full-screen QR display
   - Layout: Centered QR with white background for scanning
   - Key elements: Large QR code (300x300px), Member ID, Tier badge, Bonus balance, "Add to Wallet" button
   - Actions: Show QR, Rotate, Add to wallet, Close

**UI Components required:**
- QR Code Generator (dynamic, with member ID encoding)
- Tier Badge (colored banner with tier name and icon)
- Balance Display (large numbers with currency symbol)
- Action Buttons (Rotate, Add to Wallet, Close)

**1.4 User Profile (12 functions)**
- Просмотр и редактирование профиля (avatar, name, data)
- Загрузка аватара пользователя (photo picker, crop, upload)
- Отображение текущего статуса с визуальным бейджем (tier card)
- Отображение уровня влияния (voting weight for Elite users)
- Статистика профиля (purchases, categories, bonuses, events attended)
- Просмотр истории всех покупок (transaction list with filters)
- Просмотр активных бонусов и купонов (tabbed view)
- Реферальная программа - генерация ссылки (share link, QR code)
- Настройки уведомлений (push/email/sms toggles)
- Настройки приватности и безопасности (data visibility controls)
- Смена пароля и 2FA (security settings)
- Удаление аккаунта (danger zone, confirmation modal)

**Screens needed:**
1. **Profile View** - User profile overview
   - Layout: Header (avatar, name, tier) + scrollable content sections
   - Key elements: Avatar, Name, Tier badge, Stats cards (4x), Action buttons
   - Actions: Edit profile, View stats, Access settings

2. **Edit Profile** - Modify profile data
   - Layout: Form with sections (Personal, Contact, Preferences)
   - Key elements: Input fields, Save button, Cancel button
   - Actions: Edit fields, Save changes, Cancel

3. **Transaction History** - All purchases
   - Layout: List view with filters
   - Key elements: Filter chips, transaction cards (date, business, amount, bonuses), pagination
   - Actions: Filter by date/business, View transaction details

4. **Bonuses & Coupons** - Active rewards
   - Layout: Tabbed view (Bonuses / Coupons)
   - Key elements: Tab bar, reward cards (amount, expiry, terms), redeem button
   - Actions: Switch tabs, View details, Redeem

5. **Settings** - Account settings
   - Layout: Grouped list
   - Key elements: Toggle switches (notifications), navigation items (Privacy, Security), Danger zone (Delete)
   - Actions: Toggle settings, Navigate to sub-screens, Delete account (with confirmation)

**UI Components required:**
- Avatar Upload (with camera/gallery picker, crop tool)
- Stats Cards (4 metrics: purchases, categories, bonuses, events)
- Transaction Card (business logo, date, amount, bonuses earned/redeemed)
- Coupon Card (amount, business, expiry countdown, QR code)
- Toggle Switch (styled for iOS/Android)
- Tabs (for Bonuses/Coupons view)
- Confirmation Modal (for destructive actions like delete account)

**1.5 Events Hub (14 functions)**
- Фильтрация мероприятий (All/Upcoming/My Registrations tabs)
- Фильтр по формату (Free/Paid/Closed Elite chips)
- Фильтр по дате (This week/This month)
- Карточка мероприятия (photo, title, date, location, seats left)
- Отображение количества мест ("5 of 20 spots left" - urgent if <5)
- Кнопка "Зарегистрироваться" / "Registered" (state-based button)
- Детальная страница мероприятия (full description, program, speakers)
- Программа мероприятия (timeline with activities)
- Информация о спикерах (photo, bio, credentials)
- Галерея фото с прошлых мероприятий (grid of photos)
- Отзывы участников прошлых событий (reviews with ratings)
- Кнопка "Поделиться с подругой" (share link/QR)
- Добавление мероприятия в Google Calendar / iCal (calendar integration)
- Регистрация на мероприятие с опцией +1 гость (guest selector)

**Screens needed:**
1. **Events List** - Browse all events
   - Layout: Filter bar + scrollable event cards
   - Key elements: Tab bar (All/Upcoming/My), Filter chips (Format, Date), Event cards
   - Actions: Filter events, Tap card to view details

2. **Event Detail** - Full event information
   - Layout: Scrollable with hero image + content sections
   - Key elements: Hero image, Title, Date/Location/Price, Seats indicator, Register button, Program timeline, Speakers grid, Photo gallery, Reviews
   - Actions: Register, +1 guest, Share, Add to calendar, View speakers, Browse photos

**UI Components required:**
- Event Card (image, title, date, location, seats badge, price/free indicator)
- Filter Chips (active/inactive states, tap to toggle)
- Seats Indicator (progress bar or text with urgency color)
- Speaker Card (photo, name, bio, credentials)
- Timeline (event program with times and activities)
- Photo Gallery (grid with lightbox on tap)
- Review Card (avatar, name, rating stars, text)
- Share Sheet (native share for link/QR)

**1.6 Event Constructor (VIP/Elite) (8 functions)**
- Выбор типа мероприятия (predefined templates: Masterclass, Tasting, Workshop, etc.)
- Создание custom типа мероприятия (free text input)
- Ввод деталей (name, description, date, location, budget)
- Создание программы мероприятия (drag-and-drop timeline builder)
- Прикрепление фото/видео (media upload for visualization)
- Выбор видимости (All/VIP+/Elite dropdown)
- Отправка предложения на голосование (submit button)
- Просмотр статуса голосования (progress bar, vote count)

**Screens needed:**
1. **Event Type Selection** - Choose event template
   - Layout: Grid of event type cards
   - Key elements: Template cards (icon, name, description), "Custom" option
   - Actions: Select template, Create custom

2. **Event Details Form** - Fill event info
   - Layout: Multi-step form (Details → Program → Media → Visibility)
   - Key elements: Input fields, Date picker, Location selector, Budget input, "Next" button
   - Actions: Fill form, Navigate steps, Submit

3. **Program Builder** - Create event timeline
   - Layout: Drag-and-drop interface
   - Key elements: Time slots, Activity cards (draggable), "Add Activity" button
   - Actions: Add activity, Reorder activities, Set times

4. **Voting Status** - View proposal votes
   - Layout: Card with voting progress
   - Key elements: Event preview, Progress bar (Yes/No votes), Vote count, Comments
   - Actions: View results, Share proposal

**UI Components required:**
- Template Card (icon, title, description, "Select" button)
- Multi-step Form (progress indicator, step navigation)
- Date/Time Picker (native styled)
- Location Selector (map integration or dropdown)
- Media Upload (image/video picker with preview)
- Dropdown (for visibility selection)
- Drag-and-Drop List (for program timeline)
- Progress Bar (for voting visualization)

**1.7 Business Catalog (4 functions)**
- Список бизнесов-партнеров (categories: Beauty, Health, Food, Home, Services)
- Карточка бизнеса (logo, name, rating, current promos)
- Детальная страница бизнеса (description, services, prices, gallery, reviews)
- Кнопка "Записаться" (deep link to booking) и "Построить маршрут" (maps integration)

**Screens needed:**
1. **Business List** - Browse partners
   - Layout: Category chips + scrollable business cards
   - Key elements: Category filter chips, Business cards (logo, name, rating, active promo badge)
   - Actions: Filter by category, Tap card for details

2. **Business Detail** - Full business info
   - Layout: Scrollable with header image + content sections
   - Key elements: Hero image, Logo, Name, Rating, Description, Services list, Price table, Photo gallery, Reviews, CTA buttons
   - Actions: Book appointment (deep link), Get directions (maps), Call, View menu/services

**UI Components required:**
- Business Card (logo, name, rating stars, promo badge, category tag)
- Category Chips (horizontal scrollable, tap to filter)
- Service List (name, description, price)
- Photo Gallery (grid with lightbox)
- Review Card (same as events)
- CTA Buttons (Book, Directions, Call)
- Maps Integration (for "Get Directions")

---

#### MODULE 2: Loyalty System
**Purpose:** Bonuses, status tiers, coupons, rewards
**Priority:** must_have

**Key Screens:**
1. **Bonus Balance** - Current bonuses
2. **Bonus History** - Accruals and redemptions
3. **Status Progress** - Tier advancement
4. **Coupons** - Active and expired coupons

**UI Components:**
- Bonus Balance Card (large number, Tiffany Blue)
- Transaction List (date, business, amount, +/- bonuses)
- Status Tier Card (tier name, progress ring, benefits list)
- Coupon Card (amount, business, expiry, QR, redeem button)

---

#### MODULE 3: Transactions
**Purpose:** Purchase history, manual entry, synchronization
**Priority:** must_have

**Key Screens:**
1. **Transaction List** - All purchases
2. **Transaction Detail** - Full transaction info
3. **Manual Entry** - Add transaction manually

**UI Components:**
- Transaction Card (business, date, amount, bonuses)
- Filter Controls (date range, business, status)
- Manual Entry Form (business selector, amount input, receipt upload)

---

## NAVIGATION STRUCTURE

**Primary Navigation:**
Bottom Tab Bar (5 tabs)

**Navigation Items:**
- Home (icon: house) → Home Dashboard
  - Badge: Notifications count
- Events (icon: calendar) → Events List
  - Badge: New events count
- QR (icon: qr-code, larger, center) → QR Code Screen (prominent)
- Catalog (icon: grid) → Business Catalog
- Profile (icon: user) → Profile View
  - Badge: Profile completion %

**User Actions Menu (Profile screen):**
- Settings → Settings screen
- Help → Help/FAQ
- Logout → Logout confirmation

**Navigation Flow Examples:**
```
[Home] → [Tap QR] → [QR Code Screen] → [Business scans QR] → [Transaction created] → [Bonus notification]
[Events] → [View Event] → [Register] → [+1 Guest] → [Submit] → [Success + Calendar add]
[Catalog] → [Select Business] → [View Details] → [Book Appointment] → [Deep link to booking system]
[Profile] → [Bonuses & Coupons] → [View Coupon] → [Show QR] → [Business scans] → [Coupon redeemed]
```

---

## KEY COMPONENTS TO CREATE

### Forms & Inputs
**Text Input:**
- Label placement: Floating (Material Design 3 style)
- Validation: Inline (green checkmark on valid, red error text on invalid)
- Error display: Below field (red text, icon)
- States: default, focus (Tiffany Blue border), filled, error (red border), disabled (gray)

**Select/Dropdown:**
- Style: Custom (styled to match brand)
- Search: Yes (for long lists like city selector)
- Multi-select: Yes (for event filters)

**Buttons:**
- Primary: Filled Tiffany Blue (#0ABAB5) background, white text, medium rounded corners
- Secondary: Outlined Tiffany Blue, transparent background, Tiffany Blue text
- Tertiary: Text only, Tiffany Blue text, no background/border
- Destructive: Red (#EF4444) for delete actions
- Sizes: small (32px height), medium (44px height), large (56px height)

**Checkbox/Radio:**
- Style: Custom (Material Design 3 with Tiffany Blue accent)
- Label position: Right (for RTL-ready layouts)

**Date Picker:**
- Type: Single (for event dates), Range (for transaction history filters)
- Format: DD.MM.YYYY (Russian standard)

### Data Display
**Tables:**
- Style: Card-style (on mobile, each row is a card)
- Actions: Swipe left/right for quick actions (iOS style)
- Sorting: Yes (tap column header)
- Filtering: Yes (filter chips above table)
- Pagination: Infinite scroll (lazy load on scroll to bottom)

**Cards:**
- Layout: Vertical (stacked on mobile)
- Image: Top (with aspect ratio 16:9 for consistency)
- Actions: Bottom (buttons) or Corner (icon buttons for secondary actions)

**Lists:**
- Style: Detailed (with avatars/icons, primary + secondary text)
- Avatar/Icon: Yes (business logo, event photo, etc.)
- Secondary info: Yes (date, location, status)

### Feedback & Modals
**Toast/Notification:**
- Position: Top-center (iOS style) with slide-down animation
- Auto-dismiss: Yes (3 seconds for info, 5 seconds for errors)
- Types: success (green checkmark), error (red X), warning (yellow !), info (blue i)

**Modal/Dialog:**
- Size: Medium (80% screen width on mobile, max 600px on tablet/desktop)
- Backdrop: Dimmed (40% opacity black overlay)
- Close: X button (top-right), outside click, ESC key, swipe down (iOS style)

**Loading States:**
- Spinner: Circular progress indicator (Tiffany Blue)
- Skeleton: Yes (for cards, lists, text during loading)
- Progress bar: Yes (for long operations like photo upload)

**Empty States:**
- Illustration: Yes (custom illustrations matching brand aesthetic)
- Message: Encouraging, helpful ("No events yet. Check back soon!" vs "Empty")
- CTA: "Explore Catalog" / "Create Event" / "Invite Friends"

---

## RESPONSIVE BEHAVIOR

**Breakpoints:**
- Mobile: < 768px (primary focus)
- Tablet: 768px - 1024px (secondary)
- Desktop: > 1024px (admin panels only)

**Mobile Adaptations:**
- Navigation: Bottom tabs (5 tabs with center QR prominence)
- Tables: Cards on mobile (each row becomes a card)
- Forms: Single column, full-width inputs
- Spacing: Reduced (16px vs 24px on desktop)

**Touch Targets:**
- Minimum: 44px (Apple HIG standard)
- Spacing between: 8px minimum

---

## INTERACTION PATTERNS

### Hover States
(Desktop/tablet only - no hover on mobile)
- Links: Color change to darker Tiffany Blue
- Buttons: Slightly darker background, subtle shadow
- Cards: Lift effect (translate Y -4px) + shadow increase

### Focus States
- Color: Tiffany Blue (#0ABAB5)
- Style: Ring (2px outline with 2px offset)
- Width: 2px

### Active States
- Effect: Press down (slight scale 0.98), darker shade

### Transitions
- Property: All (for simplicity, or specific for performance)
- Duration: 150ms (fast, responsive feel)
- Easing: ease-out (natural deceleration)

### Micro-interactions
- Success: Checkmark animation (stroke draw) + confetti (for status upgrade)
- Delete: Fade out + slide left
- Add: Slide in from right + fade in
- Like: Heart pop (scale 1.2 → 1.0) + color fill

---

## ACCESSIBILITY REQUIREMENTS

**Color Contrast:**
- Target: WCAG 2.1 AA (minimum 4.5:1 for normal text, 3:1 for large text)
- Text on background: 7:1 (aim for AAA where possible)
- Interactive elements: 4.5:1 minimum

**Keyboard Navigation:**
- Tab order: Logical top-to-bottom, left-to-right flow
- Focus visible: Always (2px Tiffany Blue ring)
- Skip links: Yes (skip to main content)

**Screen Reader:**
- Alt text: All images (especially event/business photos)
- ARIA labels: All interactive elements (buttons, links, inputs)
- Semantic HTML: Proper heading hierarchy (H1 → H2 → H3)

**Motion:**
- Reduced motion: Respect `prefers-reduced-motion` (disable animations, keep functionality)
- Animations: Pausable for long animations (>5 seconds)

---

## SPECIAL FEATURES

**Authentication UI:**
- Login: Modal overlay (not full-page)
- Registration: Multi-step wizard (4 steps: Phone → SMS → Profile → Consents)
- Password reset: Not applicable (passwordless auth with SMS OTP)
- Biometric: FaceID/TouchID integration (after first SMS login)

**Onboarding:**
- Type: Video (30s intro) + Carousel (3 slides explaining benefits)
- Steps: 4 (Welcome video → Benefits slides → Phone reg → Profile setup)
- Skippable: Yes (skip video, skip benefits slides)

**Gamification:**
- Status Progress Ring: Circular progress bar showing % to next tier
- Animations: Confetti on tier upgrade, pulse on bonus accrual
- Badges: Tier badges (Insider/VIP/Elite/Inner Circle) with icons and colors

**QR Integration:**
- QR Generation: Dynamic, member ID encoded, refreshed on each screen open
- QR Scanning: react-native-vision-camera for business-side scanning
- Brightness Boost: Auto-increase screen brightness to 100% when QR screen opens
- Keep Awake: Prevent screen from sleeping while QR is displayed

**Apple Wallet / Google Pay:**
- Add to Wallet: Generate pass with QR code, tier badge, bonus balance
- Auto-update: Pass updates when bonus balance or tier changes

---

## PRIORITY SCREENS (MVP)

Create these screens FIRST for immediate testing:

1. **Home Dashboard** - Core hub
   - Shows: Status card with QR access, bonus balance, upcoming events, active promos
   - Tests: Navigation to all main sections, QR quick access, visual hierarchy

2. **QR Code Screen** - Primary value prop
   - Shows: Large scannable QR code, member ID, tier badge, bonus balance
   - Tests: QR generation, brightness boost, keep-awake functionality

3. **Phone Registration + SMS** - Entry point
   - Shows: Phone input (Russian mask), SMS OTP verification
   - Tests: Auth flow, validation, SMS integration

4. **Events List + Detail** - Community engagement
   - Shows: Upcoming events, filters, detailed event info, registration
   - Tests: Event browsing, filtering, registration flow

5. **Profile with Bonuses** - Rewards visibility
   - Shows: User profile, bonus balance, transaction history, active coupons
   - Tests: Data display, transaction list, coupon redemption

---

## BRAND ELEMENTS

**Logo:**
- Placement: Header (top-center on splash, top-left on main screens)
- Size: 120x40px (horizontal wordmark), 40x40px (icon only for favicon)
- Versions: Full logo (wordmark + icon), Icon only (for small spaces)

**Brand Voice:**
- Tone: Premium, elegant, yet warm and inclusive (not cold or pretentious)
- Messaging: Concise, empowering, aspirational ("Your circle, your benefits" vs "Loyalty program")

**Illustrations:**
- Style: Custom line art with Tiffany Blue accent color, elegant and minimalist
- Usage: Empty states (no events, no transactions), onboarding slides, error screens

---

## EXAMPLE USER FLOWS

### Flow 1: Member Registration
```
[Start: App Launch (first time)]
  ↓
[Welcome Screen: 30s video plays with "Skip" option]
  ↓ (User watches or skips)
[Benefits Carousel: 3 slides explaining value (cross-promo, bonuses, events)]
  ↓ (User swipes through or skips)
[Phone Registration: Enter +7 XXX XXX-XX-XX]
  ↓ (User enters phone, taps "Send Code")
[SMS Verification: Enter 6-digit OTP]
  ↓ (User enters code, auto-validates)
[Profile Setup: Name, email, birthdate, avatar]
  ↓ (User fills form, uploads photo)
[Consents: 152-ФЗ, marketing consents]
  ↓ (User checks boxes, taps "I Agree")
[Success: Welcome message, "Start Exploring" button]
  ↓
[Home Dashboard: User logged in, status = Insider]
```

### Flow 2: Redeem Bonus at Business
```
[Start: User at business partner location]
  ↓
[Home Dashboard: User taps QR card]
  ↓
[QR Code Screen: Large QR displayed, brightness boosted]
  ↓ (Business scans QR code)
[Transaction Created: System records purchase, accrues bonuses (5%-10% based on tier)]
  ↓
[Toast Notification: "+500₽ bonuses earned!"]
  ↓
[Home Dashboard: Bonus balance updated, transaction in history]
```

### Flow 3: Register for Event
```
[Start: Home Dashboard or Events tab]
  ↓
[Events List: Browse upcoming events, filter by Free/VIP+]
  ↓ (User taps event card)
[Event Detail: Full info, program, speakers, "Register" button]
  ↓ (User taps "Register", selects +1 guest option)
[Registration Form: Confirm attendance, add guest name if +1]
  ↓ (User submits)
[Success Modal: "You're registered!", option to add to calendar]
  ↓ (User adds to calendar)
[Events List: Event now shows "Registered" badge]
```

### Flow 4: View Transaction History
```
[Start: Profile screen]
  ↓
[Profile: User taps "Transaction History"]
  ↓
[Transaction List: All purchases with filters (date, business)]
  ↓ (User applies filter "Last 30 days")
[Filtered List: Transactions from last 30 days]
  ↓ (User taps transaction)
[Transaction Detail: Business, date, amount, bonuses earned, receipt (if uploaded)]
```

---

## NOTES & SPECIAL INSTRUCTIONS

**Important considerations:**
- **Russian Locale:** All dates in DD.MM.YYYY format, currency in RUB (₽), phone numbers in +7 XXX XXX-XX-XX format
- **152-ФЗ Compliance:** Explicit consents for data processing, ability to delete account and all data
- **Премиум Feel:** Use subtle animations, refined typography, ample whitespace - avoid cluttered/budget aesthetics
- **Mobile-First:** Design primarily for iOS/Android, responsive web is secondary (admin panels only)
- **Biometric Security:** FaceID/TouchID for quick re-authentication, but always allow SMS fallback
- **Offline Support:** Key screens (QR code, bonus balance) should work offline with cached data

**Known challenges:**
- **CRM Integration Complexity:** 6 different CRM systems (YCLIENTS, Iiko, 1С, AMO, Renovatio, CSV) - UI must handle various data formats gracefully
- **Status Tier Visual Hierarchy:** Need clear visual distinction between 4 tiers without being confusing - use color + iconography + naming
- **Event Voting Transparency:** Elite users vote with weighted votes - visualize this clearly without alienating Insider/VIP users
- **Cross-Promo Clarity:** "Purchase at A → coupon at B" flow must be immediately understandable - use clear messaging and visual cues

---

## OUTPUT REQUEST

Please create an interactive, high-fidelity prototype with:

✅ All screens for MVP modules (1.1-1.7, Module 2-3 key screens)
✅ Realistic content (Russian text, real business names: Skinerica, Лисичкино, Стим Центр, Миндаль, Миллениум)
✅ Proper navigation between screens (bottom tabs + screen-to-screen flows)
✅ Interactive states (hover on desktop, focus rings, active/pressed, disabled)
✅ Responsive layouts (mobile 375-428px width, tablet 768-1024px)
✅ Consistent design system (Tiffany Blue primary, Champagne Gold accents, SF Pro/Roboto typography)
✅ Accessibility considerations (WCAG AA contrast, focus indicators, semantic structure)

**Focus on:**
1. Premium women's club aesthetic (Tiffany & Co elegance meets modern fintech)
2. Clear user flows for core value props (QR rewards, cross-promo, events)
3. Visual hierarchy emphasizing status/bonuses/exclusivity
4. Intuitive interactions with smooth animations
5. Professional polish worthy of 80K+/month income target audience

**The prototype should feel:**
- Luxurious (premium materials, refined details)
- Exclusive (club membership vibe, not mass-market)
- Empowering (helping women get more value from their spending)
- Modern (2025 design trends, not dated)
- Trustworthy (serious about data security, professional polish)

---

**Generated by UPMT Bootstrap Process**  
**Based on:** extracted_features.md (315 functions), modules_list.md (15 modules), metadata.yaml  
**Project:** Свой Круг — Premium Women's Loyalty Ecosystem  
**Ready for Figma Make** ✨
