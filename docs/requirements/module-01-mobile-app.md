# Module 1: Mobile App (Frontend) - Requirements

**Module ID:** MOD-01
**Total Functions:** 68
**Priority:** P0 (Critical - MVP)
**Dependencies:** Backend Auth API, Loyalty API, Events API
**Tech Stack:** React Native 0.81, TypeScript 5.7, Redux Toolkit 2.10.1, React Navigation 6

---

## 📋 Module Overview

The mobile app is the primary user interface for Свой Круг members. It provides authentication, onboarding, QR wallet, profile management, event discovery, event creation (VIP/Elite), and business catalog. Built with React Native for cross-platform iOS/Android deployment.

**Key Subsystems:**
- 1.1 Authentication & Onboarding (12 functions)
- 1.2 Home Screen (10 functions)
- 1.3 QR Wallet (8 functions)
- 1.4 User Profile (12 functions)
- 1.5 Events Hub (14 functions)
- 1.6 Event Constructor for VIP/Elite (8 functions)
- 1.7 Business Catalog (4 functions)

---

## 1.1 Authentication & Onboarding (12 functions)

### User Story 1.1.1: Welcome Video
**As a** first-time visitor
**I want to** watch a 30-second club presentation video
**So that** I understand the value proposition before signing up

**Acceptance Criteria:**
```gherkin
Scenario: First app open shows welcome video
  Given I am opening the app for the first time
  When the app loads
  Then I see a fullscreen welcome video (30 sec, auto-play)
  And I see a "Skip" button in top-right corner (available after 5s)
  And the video is followed by onboarding slides

Scenario: Skip button functionality
  Given the welcome video is playing
  When I tap "Skip" after 5 seconds
  Then I am taken to onboarding slides immediately
  
Scenario: Video completion
  Given the welcome video is playing
  When the video completes (30 seconds)
  Then I automatically transition to onboarding slides
```

**Technical Requirements:**
- Video format: MP4, max 10MB, hosted on Yandex Object Storage CDN
- Use react-native-video library
- Preload video on app installation to avoid streaming delay
- Skip button appears at T+5s with fade-in animation

---

### User Story 1.1.2: Onboarding Slides
**As a** new user
**I want to** see 3 slides explaining club benefits
**So that** I understand what I'm joining

**Acceptance Criteria:**
```gherkin
Scenario: View onboarding slides
  Given I completed the welcome video
  When I am on onboarding flow
  Then I see 3 slides: (1) Unified bonus wallet, (2) Exclusive events, (3) Status tiers
  And I can swipe left/right to navigate
  And I see progress dots (3 dots) at the bottom
  And I see "Next" button on slides 1-2, "Get Started" on slide 3

Scenario: Complete onboarding
  Given I am on the 3rd slide
  When I tap "Get Started"
  Then I am taken to phone number registration screen
```

**UI Requirements:**
- Tiffany blue (#0ABAB5) accent color
- Illustrations: high-quality vector graphics (SVG)
- Typography: SF Pro (iOS) / Roboto (Android), 18px body, 28px heading

---

### User Story 1.1.3: Phone Registration with SMS OTP
**As a** new user
**I want to** register using my phone number and SMS code
**So that** I can create an account securely

**Acceptance Criteria:**
```gherkin
Scenario: Enter phone number
  Given I am on registration screen
  When I enter a valid Russian phone number (+7 XXX XXX-XX-XX)
  Then the phone input validates format in real-time
  And the "Send Code" button becomes enabled
  And I tap "Send Code"
  Then I receive an SMS code within 30 seconds
  And I am taken to OTP verification screen

Scenario: Invalid phone number
  Given I am on registration screen
  When I enter an invalid phone number (e.g., 123)
  Then the input field shows red border
  And I see error message "Неверный формат номера телефона"
  And the "Send Code" button remains disabled

Scenario: SMS code verification
  Given I received SMS code and I am on OTP screen
  When I enter the 6-digit code
  Then the code auto-submits on 6th digit (no manual submit)
  And if code is correct, I proceed to personal data form
  And if code is incorrect, I see error "Неверный код. Попробуйте ещё раз" with retry option
```

**Technical Requirements:**
- SMS provider: SMS.ru API (primary), SMSC.ru (backup)
- OTP expiry: 5 minutes
- Rate limiting: Max 3 SMS per phone number per hour
- Auto-fill SMS code using iOS SMS Autofill / Android SMS Retriever API

---

### User Story 1.1.4-1.1.5: Personal Data Form with Validation
**As a** new user
**I want to** provide my personal details (name, email, birthdate, city)
**So that** my profile is complete

**Acceptance Criteria:**
```gherkin
Scenario: Fill personal data form
  Given I verified my phone number
  When I am on personal data form
  Then I see fields: First Name, Last Name, Email, Birthdate, City
  And all fields have real-time validation
  And First Name/Last Name are required
  And Email is optional but validates format if provided
  And Birthdate uses date picker (18+ age requirement)
  And City has autocomplete dropdown with Russian cities

Scenario: Real-time validation
  Given I am typing in First Name field
  When I enter non-alphabetic characters (e.g., "Anna123")
  Then I see error "Имя должно содержать только буквы"
  And the field border turns red
  And the "Continue" button is disabled until fixed

Scenario: Submit valid form
  Given I filled all required fields correctly
  When I tap "Continue"
  Then my data is saved to backend
  And I proceed to referral code screen
```

**Validation Rules:**
- First/Last Name: 2-50 chars, Cyrillic/Latin letters only
- Email: RFC 5322 format validation
- Birthdate: Must be 18+ years old
- City: Must be from predefined list (Yandex Geocoder API)

---

### User Story 1.1.6: Referral Code (Optional)
**As a** new user
**I want to** enter a referral code if invited by friend
**So that** we both receive referral bonuses

**Acceptance Criteria:**
```gherkin
Scenario: Enter referral code
  Given I am on referral code screen
  When I enter a 6-character alphanumeric code (e.g., "ABC123")
  Then the code is validated against backend
  And if valid, I see "Реферальный код применён! +500₽ бонусов"
  And I proceed to consent screen
  
Scenario: Skip referral code
  Given I am on referral code screen
  When I tap "У меня нет кода" button
  Then I proceed to consent screen without referral bonuses
```

---

### User Story 1.1.7-1.1.8: Consents (152-ФЗ Compliance)
**As a** new user
**I want to** review and accept data processing consents
**So that** my registration is legally compliant

**Acceptance Criteria:**
```gherkin
Scenario: Review consents
  Given I am on consent screen
  When the screen loads
  Then I see two checkboxes:
    1. "Согласие на обработку персональных данных (152-ФЗ)" - REQUIRED
    2. "Согласие на получение рассылок (push/email/SMS)" - OPTIONAL
  And each checkbox has "Подробнее" link to full legal text
  And I must check checkbox 1 to enable "Complete Registration" button

Scenario: Complete registration
  Given I checked "152-ФЗ" consent (checkbox 1)
  When I tap "Complete Registration"
  Then my account is created on backend
  And I receive Insider status automatically
  And I see success animation + "Добро пожаловать в Свой Круг!"
  And I am taken to the main app (Home screen)
```

---

### User Story 1.1.9: Login with SMS OTP
**As a** returning user
**I want to** log in using my phone number and SMS code
**So that** I can access my account securely

**Acceptance Criteria:**
```gherkin
Scenario: Login flow
  Given I am on login screen
  When I enter my registered phone number
  And I tap "Send Code"
  Then I receive SMS code within 30 seconds
  And I enter the 6-digit code
  Then I am logged in and see Home screen
  And my JWT access token is stored securely (iOS Keychain / Android Keystore)
```

---

### User Story 1.1.10: Biometric Login (FaceID/TouchID)
**As a** returning user
**I want to** log in using FaceID/TouchID after initial setup
**So that** I can access the app quickly

**Acceptance Criteria:**
```gherkin
Scenario: Enable biometric login
  Given I completed first login via SMS
  When I am asked "Включить вход по FaceID?"
  And I tap "Включить"
  Then biometric credentials are stored securely
  And next time I open app, I am prompted for FaceID/TouchID
  
Scenario: Biometric login success
  Given I enabled biometric login previously
  When I open the app
  And I complete FaceID/TouchID verification
  Then I am logged in immediately without SMS code
```

**Technical Requirements:**
- Use react-native-biometrics library
- Fallback to SMS login if biometric fails 3 times
- User can disable biometric in Settings

---

### User Story 1.1.11: Password Recovery
**As a** user who lost access
**I want to** recover my account using phone number
**So that** I can regain access

**Acceptance Criteria:**
```gherkin
Scenario: Forgot password flow
  Given I am on login screen
  When I tap "Забыли пароль?"
  Then I am taken to phone number entry screen
  And I enter my phone number
  And I receive SMS code
  And I verify code
  Then I am logged in and prompted to update profile if needed
```

---

### User Story 1.1.12: Auto-fill from Contacts
**As a** new user
**I want to** auto-fill my name and email from phone contacts
**So that** registration is faster

**Acceptance Criteria:**
```gherkin
Scenario: Auto-fill data
  Given I am on personal data form
  When I tap "Заполнить из контактов"
  Then I grant contacts permission (if not granted)
  And the app finds my contact info (name, email)
  And the form fields are pre-filled
  And I can still edit any field manually
```

---

## 1.2 Home Screen (10 functions)

### User Story 1.2.1-1.2.3: Header with Avatar, Status, Notifications
**As a** member
**I want to** see my avatar, status tier, and notification count
**So that** I know my current standing and have quick access to notifications

**Acceptance Criteria:**
```gherkin
Scenario: View header
  Given I am logged in
  When I open Home screen
  Then I see top header with:
    - My circular avatar (left)
    - Status badge (Insider/VIP/Elite/Inner Circle) next to name
    - Notification bell icon (right) with red badge showing unread count
    - QR code icon (right) for quick access to wallet
```

---

### User Story 1.2.4-1.2.6: Gamification Ring with Progress
**As a** member
**I want to** see my progress toward next status tier
**So that** I am motivated to increase spending and category diversity

**Acceptance Criteria:**
```gherkin
Scenario: View progress ring
  Given I am an Insider with 15,000₽ spent and 2 categories
  When I view Home screen
  Then I see a circular progress ring with:
    - Inner text "Insider" + current bonus balance
    - Progress bar showing 50% toward VIP (15K of 30K spent)
    - Tooltip "Осталось 15,000₽ и 1 категория до VIP"
  And I can tap the ring to see detailed status breakdown

Scenario: Status upgrade animation
  Given I just completed a purchase that upgraded me to VIP
  When I return to Home screen
  Then I see a fullscreen animation with confetti
  And I see message "Поздравляем! Вы теперь VIP"
  And I see new VIP benefits listed
```

---

### User Story 1.2.7-1.2.9: Active Promotions & AI Recommendations
**As a** member
**I want to** see current promotions and personalized recommendations
**So that** I discover new businesses and maximize my bonuses

**Acceptance Criteria:**
```gherkin
Scenario: View promotions carousel
  Given I have 3 active coupons
  When I scroll down on Home screen
  Then I see a horizontal carousel with:
    - My 3 active coupons with countdown timers
    - AI recommendation card "Попробуйте новое: Миндаль Салон"
    - Each card is tappable to see details

Scenario: Expiring coupon alert
  Given I have a coupon expiring in 6 hours
  When I view Home screen
  Then I see a red timer badge "Осталось 6 ч"
  And the coupon card is highlighted in orange
```

---

### User Story 1.2.10: Upcoming Events
**As a** member
**I want to** see my upcoming registered events on Home screen
**So that** I don't miss them

**Acceptance Criteria:**
```gherkin
Scenario: View upcoming events
  Given I am registered for 2 events (next week)
  When I scroll down on Home screen
  Then I see "Ближайшие мероприятия" section with 2 event cards
  And each card shows: event title, date, location, "Вы зарегистрированы" badge
  And I can tap "Все мероприятия" to go to Events Hub
```

---

## 1.3 QR Wallet (8 functions)

### User Story 1.3.1-1.3.4: QR Code Display
**As a** member
**I want to** show my QR code to business staff
**So that** they can scan it to apply my bonuses

**Acceptance Criteria:**
```gherkin
Scenario: Open QR wallet
  Given I am on Home screen
  When I tap the QR icon in header
  Then I see QR Wallet screen with:
    - Large QR code in center (300x300px)
    - My unique member ID below QR code
    - Status badge (e.g., "VIP") above QR code
    - Bonus balance in large font at top
  And the QR code is scannable by business staff

Scenario: QR code content
  Given I opened QR Wallet
  When business staff scans my QR code
  Then the QR contains: user_id, status_tier, current_timestamp
  And the data is encrypted to prevent forgery
```

---

### User Story 1.3.5-1.3.6: Screen Brightness & Keep Awake
**As a** member
**I want to** have maximum screen brightness and no auto-lock when showing QR
**So that** the code is easily scannable in any lighting

**Acceptance Criteria:**
```gherkin
Scenario: Auto-brightness adjustment
  Given I opened QR Wallet
  When the screen loads
  Then screen brightness is automatically set to 100%
  And screen auto-lock is disabled
  
Scenario: Exit QR Wallet
  Given I am viewing QR Wallet
  When I navigate back to Home screen
  Then screen brightness returns to previous level
  And auto-lock is re-enabled
```

**Technical Requirements:**
- Use react-native-brightness library for brightness control
- Use react-native-keep-awake to prevent screen sleep
- Reset settings on component unmount

---

### User Story 1.3.7-1.3.8: QR Rotation & Wallet Integration
**As a** member
**I want to** rotate the QR code and add it to Apple/Google Wallet
**So that** I can show it conveniently

**Acceptance Criteria:**
```gherkin
Scenario: Rotate QR code
  Given I am viewing QR Wallet
  When I rotate my phone to landscape orientation
  Then the QR code rotates and scales to fit screen
  
Scenario: Add to Apple/Google Wallet
  Given I am viewing QR Wallet
  When I tap "Добавить в Wallet"
  Then I see native wallet integration prompt
  And my membership card is added to Apple Wallet / Google Pay
  And the wallet card shows: QR code, status, bonus balance
```

---

## 1.4 User Profile (12 functions)

### User Story 1.4.1-1.4.2: View and Edit Profile
**As a** member
**I want to** view and update my profile information
**So that** my data is current

**Acceptance Criteria:**
```gherkin
Scenario: View profile
  Given I am logged in
  When I tap Profile tab
  Then I see my profile with:
    - Avatar (circular, 120px)
    - Full name, email, phone, city, birthdate
    - Status tier badge
    - Edit button in top-right

Scenario: Edit profile
  Given I am on Profile screen
  When I tap Edit button
  Then all fields become editable except phone
  And I can tap avatar to upload new photo (camera or gallery)
  And I can save changes
```

---

### User Story 1.4.3-1.4.5: Status Display & Statistics
**As a** member
**I want to** see my status details and purchase statistics
**So that** I understand my standing in the ecosystem

**Acceptance Criteria:**
```gherkin
Scenario: View status details
  Given I am a VIP member
  When I tap on status badge
  Then I see a modal with:
    - Current status: VIP
    - Progress to Elite: 70,000₽ more, 2 more categories
    - Benefits: 7% cashback, priority event registration
    - Comparison table of all 4 tiers

Scenario: View statistics
  Given I am on Profile screen
  When I scroll down
  Then I see "Статистика" section with:
    - Total purchases: 15
    - Categories visited: 3 (Beauty, Gastronomy, Health)
    - Total bonuses earned: 12,450₽
    - Total bonuses spent: 5,200₽
    - Events attended: 2
```

---

### User Story 1.4.6-1.4.7: Transaction History & Bonuses
**As a** member
**I want to** view my purchase history and bonus details
**So that** I can track my spending

**Acceptance Criteria:**
```gherkin
Scenario: View transaction history
  Given I am on Profile screen
  When I tap "История покупок"
  Then I see a list of all my transactions with:
    - Business name and logo
    - Date and time
    - Amount paid
    - Bonuses earned/spent
  And I can filter by date range or business
  And I can search by amount or business name

Scenario: View active bonuses
  Given I am on Profile screen
  When I tap "Бонусы и купоны"
  Then I see:
    - Current bonus balance: 7,250₽
    - Active coupons (3) with expiry dates
    - Bonus history (earned/spent) with filters
```

---

### User Story 1.4.8: Referral Program
**As a** member
**I want to** invite friends and earn referral bonuses
**So that** we both benefit

**Acceptance Criteria:**
```gherkin
Scenario: Generate referral link
  Given I am on Profile screen
  When I tap "Пригласить подругу"
  Then I see my unique referral code: ABC123
  And I see referral link: https://svoykrug.ru/ref/ABC123
  And I can share via WhatsApp/Telegram/Instagram
  
Scenario: Track referrals
  Given I invited 3 friends
  When I view referral screen
  Then I see:
    - Friends registered: 3
    - Bonuses earned from referrals: 1,500₽ (500₽ per friend)
    - Status: "Ещё 2 приглашения до VIP бейджа"
```

---

### User Story 1.4.9-1.4.12: Settings & Security
**As a** member
**I want to** manage my notification preferences and account security
**So that** I have control over my data

**Acceptance Criteria:**
```gherkin
Scenario: Notification settings
  Given I am on Profile screen
  When I tap "Настройки" → "Уведомления"
  Then I see toggles for:
    - Push notifications (new coupons, events, status upgrades)
    - Email notifications (weekly digest, promotions)
    - SMS notifications (important alerts only)
  And I can toggle each on/off individually

Scenario: Change password & 2FA
  Given I am on Settings → Security
  When I tap "Сменить пароль"
  Then I enter current password, new password (8+ chars, 1 uppercase, 1 number)
  And I can enable 2FA via SMS or authenticator app
  
Scenario: Delete account
  Given I am on Settings → Security
  When I tap "Удалить аккаунт"
  Then I see warning "Все данные будут удалены. Это действие необратимо."
  And I must confirm by entering my password
  And if confirmed, my account is permanently deleted
  And I am logged out
```

---

## 1.5 Events Hub (14 functions)

### User Story 1.5.1-1.5.3: Event Filters
**As a** member
**I want to** filter events by status, format, and date
**So that** I find relevant events quickly

**Acceptance Criteria:**
```gherkin
Scenario: Filter events by status
  Given I am on Events Hub
  When I select filter "Мои регистрации"
  Then I see only events I registered for (2 events)
  
Scenario: Filter by format
  Given I am on Events Hub
  When I select filter "Бесплатные"
  Then I see only free events (5 events)
  And paid/closed events are hidden

Scenario: Filter by date
  Given I am on Events Hub
  When I select "На этой неделе"
  Then I see only events happening within next 7 days
```

---

### User Story 1.5.4-1.5.6: Event Cards & Registration
**As a** member
**I want to** see event details and register
**So that** I can attend

**Acceptance Criteria:**
```gherkin
Scenario: View event card
  Given I am on Events Hub
  When I view an event card
  Then I see:
    - Event cover photo (16:9 ratio)
    - Event title (e.g., "Мастер-класс по макияжу")
    - Date & time (e.g., "18 ноября, 19:00")
    - Location (e.g., "Миндаль, ул. Тверская 10")
    - Seats available (e.g., "Осталось 5 из 20 мест")
    - "Зарегистрироваться" button or "Вы зарегистрированы" badge

Scenario: Register for event
  Given I am viewing an event with available seats
  When I tap "Зарегистрироваться"
  Then I am asked "Зарегистрироваться на мероприятие?"
  And I confirm
  Then I see success message "Вы зарегистрированы!"
  And button changes to "Вы зарегистрированы"
  And I receive confirmation email + push notification
```

---

### User Story 1.5.7-1.5.13: Event Details Page
**As a** member
**I want to** see full event details before registering
**So that** I make an informed decision

**Acceptance Criteria:**
```gherkin
Scenario: View event details
  Given I am on Events Hub
  When I tap an event card
  Then I see event details page with:
    - Full description (multi-paragraph)
    - Program schedule (e.g., "19:00-19:30 Welcome drinks, 19:30-20:30 Masterclass")
    - Speaker bios with photos
    - Photo gallery from past similar events (if available)
    - Participant reviews (star rating + text)
    - "Поделиться" button (share to social media)
    - "Добавить в календарь" button (Google Calendar/iCal export)

Scenario: Share event
  Given I am on event details page
  When I tap "Поделиться с подругой"
  Then I see native share sheet with event link
  And I can share via WhatsApp/Telegram/Instagram
  
Scenario: Add to calendar
  Given I am on event details page
  When I tap "Добавить в календарь"
  Then I see native calendar integration
  And event is added with: title, date, location, description
```

---

### User Story 1.5.14: Register with +1 Guest
**As a** member
**I want to** register for an event and bring a guest
**So that** I can attend with a friend

**Acceptance Criteria:**
```gherkin
Scenario: Register with guest
  Given I am viewing an event that allows guests
  When I tap "Зарегистрироваться"
  Then I see option "Взять +1 гостя?"
  And I can toggle it on/off
  And if on, I enter guest name and phone
  And I submit registration for 2 people
  Then both registrations are confirmed
  And 2 seats are reserved (not 1)
```

---

## 1.6 Event Constructor (VIP/Elite Only) - 8 functions

### User Story 1.6.1-1.6.3: Create Event Proposal
**As a** VIP/Elite member
**I want to** propose a new event idea
**So that** the community can vote on it

**Acceptance Criteria:**
```gherkin
Scenario: Access event constructor
  Given I am a VIP member
  When I go to Events Hub
  Then I see "Предложить мероприятие" button
  
Scenario: Access denied for Insider
  Given I am an Insider member
  When I go to Events Hub
  Then I do not see "Предложить мероприятие" button

Scenario: Choose event type
  Given I am creating an event proposal
  When I tap "Предложить мероприятие"
  Then I see predefined event types:
    - Wellness Workshop
    - Beauty Masterclass
    - Networking Dinner
    - Fitness Session
    - Custom (free text)
  And I select "Beauty Masterclass"
  
Scenario: Create custom event type
  Given I selected "Custom"
  When I enter event type name "Wine Tasting Evening"
  Then my custom type is saved
  And I proceed to details form
```

---

### User Story 1.6.4-1.6.6: Event Proposal Details
**As a** VIP/Elite member
**I want to** provide full event details
**So that** voters understand my proposal

**Acceptance Criteria:**
```gherkin
Scenario: Fill event details
  Given I selected event type
  When I am on details form
  Then I see fields:
    - Event title (required, max 100 chars)
    - Description (required, max 500 chars)
    - Suggested date (optional, date picker)
    - Suggested location (optional, text input)
    - Estimated budget (optional, number input with ₽ symbol)
    - Program (optional, step-by-step editor)
  And I can attach photos/videos (max 3 files, 10MB total)
  
Scenario: Create program
  Given I am filling event details
  When I tap "Создать программу"
  Then I see step editor
  And I can add steps: "19:00-19:30 Welcome drinks"
  And I can add/remove/reorder steps
```

---

### User Story 1.6.7-1.6.8: Submit Proposal & Track Voting
**As a** VIP/Elite member
**I want to** submit my proposal for community voting
**So that** it can be realized if approved

**Acceptance Criteria:**
```gherkin
Scenario: Set visibility
  Given I completed event details
  When I tap "Настройки видимости"
  Then I can choose:
    - "Все участницы" (all members can vote)
    - "VIP+" (only VIP/Elite/Inner Circle can vote)
    - "Elite" (only Elite/Inner Circle can vote)
  And I select "Все участницы"
  
Scenario: Submit proposal
  Given I filled all required fields
  When I tap "Отправить на голосование"
  Then my proposal is submitted for 7-day voting period
  And I see confirmation "Предложение отправлено на голосование!"
  And I can view it in "Мои предложения" section
  
Scenario: Track voting
  Given I submitted a proposal 3 days ago
  When I go to "Мои предложения"
  Then I see my proposal with:
    - Voting progress: 45 votes (32 за, 13 против)
    - Time remaining: 4 дня
    - Current rank: #2 of 5 proposals this month
  And I can see who voted (anonymized by status tier)
```

---

## 1.7 Business Catalog (4 functions)

### User Story 1.7.1-1.7.2: Browse Businesses
**As a** member
**I want to** browse all partner businesses
**So that** I discover new places to visit

**Acceptance Criteria:**
```gherkin
Scenario: View business catalog
  Given I am on Businesses tab
  When the screen loads
  Then I see category filters:
    - Все (5 businesses)
    - Красота (2: Миндаль, Skinerica)
    - Здоровье (2: Миллениум, Стим Центр)
    - Гастрономия (1: Лисичкино)
  And I see business cards with:
    - Business logo
    - Business name
    - Rating (5-star with review count)
    - Current active promotion (if any)

Scenario: Filter by category
  Given I am on Businesses tab
  When I select "Красота"
  Then I see only 2 businesses: Миндаль, Skinerica
```

---

### User Story 1.7.3-1.7.4: Business Details & Actions
**As a** member
**I want to** view business details and take actions
**So that** I can visit or contact them

**Acceptance Criteria:**
```gherkin
Scenario: View business details
  Given I am on Businesses tab
  When I tap "Миндаль" business card
  Then I see details page with:
    - Full description (200+ words)
    - Services offered with prices
    - Photo gallery (5-10 photos)
    - Reviews from members (star rating + text comments)
    - Address with map preview
    - Operating hours
    - Contact phone number
  
Scenario: Book appointment
  Given I am on business details page
  When I tap "Записаться"
  Then I am taken to external booking system (YCLIENTS deep link for Миндаль)
  And my member ID is pre-filled if integration supports it
  
Scenario: Get directions
  Given I am on business details page
  When I tap "Построить маршрут"
  Then I am taken to native maps app (Apple Maps / Google Maps)
  And the business address is set as destination
```

---

## 📊 Technical Requirements

### Performance
- App load time: <2 seconds (cold start)
- Screen transition: <300ms
- API response time: <500ms (p95)
- Image lazy loading for all lists
- Redux persist for offline support

### Offline Support
- Cache last 30 days of transactions locally
- Cache bonus balance (sync on app open)
- Cache QR code for offline scanning

### Analytics
- Track screen views (Firebase Analytics)
- Track button taps and conversions (Amplitude)
- Track errors and crashes (Sentry)

### Accessibility
- VoiceOver / TalkBack support for all screens
- Minimum touch target: 44x44 px
- WCAG AA contrast ratios (4.5:1 for text)

---

## 7. UI/UX REQUIREMENTS

### 7.1 Design System Reference

**Foundation:**
- **Colors:** See [docs/design/foundation/colors.md](../design/foundation/colors.md)
  - Primary: Tiffany Blue (#0ABAB5) for buttons, links, active states
  - Background: Champagne Beige (#F5F1E8) for warmth
  - Accent: Champagne Gold (#D4AF37) for achievements, VIP elements
  - Text: Charcoal (#2A2D34) primary, Taupe (#8B7355) secondary

- **Typography:** See [docs/design/foundation/typography.md](../design/foundation/typography.md)
  - SF Pro Display/Text (iOS), Roboto (Android)
  - H1: 28px/700 for screen titles
  - H3: 18px/600 for card titles
  - Body: 14px/400 for descriptions
  - Caption: 12px/400 for metadata

- **Spacing:** See [docs/design/foundation/spacing.md](../design/foundation/spacing.md)
  - Base unit: 8px
  - Component padding: 16px standard, 24px generous
  - Touch targets: Minimum 44x44px

- **Elevation:** See [docs/design/foundation/elevation.md](../design/foundation/elevation.md)
  - Cards: Level 2 (soft shadow)
  - Modals: Level 4
  - Bottom nav: Level 3

### 7.2 Components Used

**Navigation:**
- [Bottom Navigation](../design/components/bottom-navigation.md) - 5 tabs (Home, Partners, Events, Profile, QR)
- Top bar with back button and screen title

**Data Display:**
- [Card](../design/components/card.md) - Partner cards, Event cards, Status cards
- [Status Badge](../design/components/status-badge.md) - Bronze/Silver/Gold/Elite tiers
- [QR Code Display](../design/components/qr-code-display.md) - Wallet screen, expandable view

**Forms & Inputs:**
- [Input](../design/components/input.md) - Phone, Name, Email variants
- [Button](../design/components/button.md) - Primary (Tiffany Blue), Secondary, Accent (Gold)

**Other:**
- Progress indicators (onboarding dots)
- Empty states (no events, no bonuses)
- Loading skeletons
- Toast notifications

### 7.3 Screen-Specific Design Notes

**Onboarding Screens:**
- Full-screen illustrations with Champagne Beige background
- Tiffany Blue progress dots
- Typography: Display (34px) for headlines
- CTA button: Primary (Tiffany Blue), minimum 48px height

**Home Dashboard:**
- Status card at top (Champagne Beige background, Gold accents for VIP+)
- Level progress bar (Tiffany Blue fill)
- Partner carousel (horizontal scroll)
- Bottom navigation always visible

**QR Wallet:**
- White card with black QR code, centered
- "Свой Круг" branding above QR
- Points display below (H2 size, Charcoal text)
- Expandable to full-screen modal

**Events Hub:**
- Event cards with partner photos
- Date/time in Caption size (12px)
- "Записаться" button (Tiffany Blue primary)
- Filter chips at top (default/active states)

**Profile:**
- Avatar (circular, 80px diameter)
- Status badge overlay (top-right of avatar)
- Settings list (white cards with subtle shadows)
- Logout button (tertiary style, subtle)

### 7.4 Accessibility Compliance

See [docs/design/accessibility/overview.md](../design/accessibility/overview.md)

**Requirements:**
- ✅ WCAG 2.1 Level AA compliance
- ✅ VoiceOver/TalkBack screen reader support (all screens)
- ✅ Minimum touch targets: 44x44px
- ✅ Color contrast: ≥4.5:1 for text, ≥3:1 for UI components
- ✅ Keyboard navigation (focus indicators visible)
- ✅ Text scaling support (up to 200%)
- ✅ Reduced motion support (prefers-reduced-motion)

**Testing:**
- Use VoiceOver (iOS) and TalkBack (Android) for every screen
- Test with Accessibility Inspector (Xcode) / Accessibility Scanner (Android Studio)
- Validate color contrast with WebAIM Contrast Checker
- Test with actual users (accessibility testing sessions)

### 7.5 Design Assets

**Figma Files:**
- See [docs/design/resources/figma-links.md](../design/resources/figma-links.md)

**Design Screenshots:**
- Reference: `UPMT/bootstrap/00_DESIGN_RAW_DATA/screenshots/` (13 PNG files)
- Mobile app screens, UI layouts, status cards, QR wallet examples

**Design Tokens:**
- Import from `docs/design/resources/design-tokens.json`
- Use for consistent colors, typography, spacing across app

---

## 🔄 Dependencies

- **Backend APIs:**
  - `/api/v1/auth/*` - Authentication endpoints
  - `/api/v1/users/*` - User profile management
  - `/api/v1/loyalty/*` - Bonus and status data
  - `/api/v1/events/*` - Event Hub endpoints
  - `/api/v1/businesses/*` - Business catalog

- **External Services:**
  - SMS.ru API for SMS OTP
  - Yandex Object Storage for media (CDN)
  - Firebase Cloud Messaging for push notifications
  - Firebase Analytics & Amplitude for analytics
  - Sentry for crash reporting

---

## ✅ Success Criteria

- [ ] All 68 functions implemented and tested
- [ ] 0 critical bugs in production
- [ ] <2s app load time achieved
- [ ] 95%+ users complete onboarding (funnel analysis)
- [ ] 4.5+ star rating on App Store & Google Play
- [ ] <5% crash rate (measured by Sentry)

---

**Last Updated:** 2025-11-17
**Owner:** Mobile Team
**Status:** Ready for Development
