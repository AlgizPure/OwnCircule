# Module 12: Notifications & Communications - Requirements

**Module ID:** MOD-12
**Total Functions:** 18
**Priority:** P0 (Critical - MVP)
**Dependencies:** All modules (cross-cutting communication layer)
**Tech Stack:** Firebase Cloud Messaging, SendGrid/Mailgun, SMS.ru, Python 3.13, Celery 5.4.x

---

## 📋 Module Overview

Notification system delivers real-time updates via push, email, and SMS channels. Handles bonus accruals, status upgrades, new coupons/offers, expiring coupons, event registrations/reminders, voting results. Members control notification preferences and quiet hours.

**Key Subsystems:**
- 12.1 Push Notifications (8 functions): Bonuses, status, coupons, events, voting
- 12.2 Email Notifications (5 functions): Welcome, weekly digest, status upgrade, event tickets, thank-you
- 12.3 SMS Notifications (3 functions): OTP codes, critical alerts, event reminders
- 12.4 Notification Settings (2 functions): Subscription management, quiet hours

---

## 12.1 Push Notifications (8 functions)

### User Story 12.1.1: Bonus Accrual Push
**As a** member
**I want to** receive instant push when bonuses are earned
**So that** I know my purchase was processed

**Acceptance Criteria:**
```gherkin
Scenario: Standard bonus accrual
  Given I completed 10,000₽ purchase at Миндаль (VIP 7%)
  When bonuses are accrued (700₽)
  Then I receive push within 1 minute:
    Title: "Начислено 700₽ бонусов!"
    Body: "За покупку в Миндаль. Новый баланс: 5,700₽"
  And I can tap push to open bonus history

Scenario: Multiplier applied
  Given I earned 1.5x multiplier (first purchase in category)
  When push is sent
  Then body includes: "Бонус за новую категорию! +150₽ extra"
```

**Technical Requirements:**
- FCM (Firebase Cloud Messaging) for iOS + Android
- Celery task after bonus accrual: `send_push_notification(user_id, title, body, data)`
- Deep link to bonus history: `svoykrug://profile/bonuses`

---

### User Story 12.1.2: Status Upgrade Push
**As a** member
**I want to** be notified when my status upgrades
**So that** I celebrate the achievement

**Acceptance Criteria:**
```gherkin
Scenario: VIP upgrade
  Given I just crossed VIP threshold
  When status recalculation runs (daily)
  Then I receive push:
    Title: "Поздравляем! Вы теперь VIP!"
    Body: "Теперь 7% кешбэк и приоритетная регистрация на мероприятия"
  And I see fullscreen animation when I tap push

Scenario: Elite upgrade
  Given I upgraded to Elite
  Then push includes confetti emoji: "🎉 Вы достигли Elite статуса!"
```

---

### User Story 12.1.3-12.1.4: Coupon Push Notifications
**As a** member
**I want to** be notified about new coupons and expiring ones
**So that** I don't miss offers

**Acceptance Criteria:**
```gherkin
Scenario: New coupon received
  Given cross-promo chain triggered coupon for Миндаль
  When coupon is generated
  Then I receive push:
    Title: "Новый купон: 20% скидка в Миндаль!"
    Body: "Действует 30 дней. Активируйте в разделе 'Купоны'"
  And I can tap to open coupon details

Scenario: Expiring coupon reminder (24 hours)
  Given I have coupon expiring in 24 hours
  When reminder task runs
  Then I receive push:
    Title: "Купон сгорает через 24 часа!"
    Body: "20% скидка в Миндаль. Успейте использовать!"
  And push has high priority (iOS critical alert, Android high importance)
```

---

### User Story 12.1.5-12.1.6: Event Push Notifications
**As a** member
**I want to** receive event confirmations and reminders
**So that** I don't miss events I registered for

**Acceptance Criteria:**
```gherkin
Scenario: Event registration confirmation
  Given I registered for "Мастер-класс по макияжу" event
  When registration succeeds
  Then I receive push:
    Title: "Вы зарегистрированы на мероприятие"
    Body: "Мастер-класс по макияжу - 20 ноября, 19:00"
  And push includes "Добавить в календарь" action

Scenario: Event reminder (24 hours)
  Given event is happening tomorrow
  When 24-hour reminder task runs
  Then I receive push:
    Title: "Завтра: Мастер-класс по макияжу"
    Body: "19:00, Миндаль, ул. Тверская 10. До встречи!"

Scenario: Event reminder (2 hours)
  Given event is happening in 2 hours
  When 2-hour reminder task runs
  Then I receive push:
    Title: "Через 2 часа: Мастер-класс по макияжу"
    Body: "Не забудьте QR-билет!"
  And push has high priority
```

---

### User Story 12.1.7-12.1.8: Voting Push Notifications
**As a** VIP/Elite member
**I want to** be notified about voting opportunities and results
**So that** I participate in community decisions

**Acceptance Criteria:**
```gherkin
Scenario: New event proposal for voting
  Given a VIP member proposed new event "Wine Tasting Evening"
  When proposal is published for voting
  Then I receive push:
    Title: "Новое предложение на голосовании"
    Body: "Wine Tasting Evening - проголосуйте за или против"
  And I can tap to view proposal details and vote

Scenario: Voting results
  Given I voted for "Wine Tasting Evening" proposal
  When voting period ends (7 days)
  Then I receive push:
    Title: "Результаты голосования: Wine Tasting Evening"
    Body: "Предложение одобрено! 75% голосов 'за'. Мероприятие запланировано."
```

---

## 12.2 Email Notifications (5 functions)

### User Story 12.2.1: Welcome Email
**As a** new member
**I want to** receive welcome email after registration
**So that** I feel welcomed and learn how to use the app

**Acceptance Criteria:**
```gherkin
Scenario: Registration welcome email
  Given I just completed registration
  When my account is created
  Then I receive email within 5 minutes:
    Subject: "Добро пожаловать в Свой Круг!"
    Body: 
      - Welcome message from founder
      - Quick start guide (5 steps)
      - Links to partner businesses
      - Download app reminder (if registered on web)
      - Support contact
```

**Technical Requirements:**
- Email provider: SendGrid or Mailgun
- HTML template: `templates/emails/welcome.html`
- Send via Celery task: `send_welcome_email(user_id, email)`
- Track email opens with pixel tracking

---

### User Story 12.2.2: Weekly Digest Email
**As a** member
**I want to** receive weekly summary of my activity
**So that** I stay engaged with the ecosystem

**Acceptance Criteria:**
```gherkin
Scenario: Weekly digest (Monday 10am)
  Given it's Monday and I have activity last week
  When weekly digest task runs
  Then I receive email:
    Subject: "Ваша неделя в Свой Круг - 10-16 ноября"
    Body:
      - Purchases this week: 2 (total 15,000₽)
      - Bonuses earned: 1,050₽
      - Bonuses spent: 500₽
      - New status progress: 65% toward VIP
      - Upcoming events: 1 registered
      - Active coupons: 3 (expires soon)
      - CTA: "Посмотреть новые предложения"

Scenario: No activity week
  Given I had no activity last week
  When digest task runs
  Then email includes:
    - "Мы скучали! Вот что нового в клубе:"
    - New partner businesses
    - Upcoming events
    - Special offers to re-engage
```

---

### User Story 12.2.3: Status Upgrade Email
**As a** member
**I want to** receive detailed email about status upgrade
**So that** I understand new privileges

**Acceptance Criteria:**
```gherkin
Scenario: VIP upgrade email
  Given I upgraded to VIP today
  When status upgrade push is sent
  Then I also receive email:
    Subject: "Поздравляем! Вы теперь VIP"
    Body:
      - Congratulations message
      - New cashback rate: 7% (up from 5%)
      - New privileges:
        * Priority event registration
        * Access to VIP-only events
        * Event constructor access
      - Roadmap to Elite status
      - CTA: "Explore VIP Benefits"
```

---

### User Story 12.2.4: Event Ticket Email
**As a** member
**I want to** receive email with event ticket
**So that** I have backup if app is unavailable

**Acceptance Criteria:**
```gherkin
Scenario: Event registration ticket
  Given I registered for event
  When registration is confirmed
  Then I receive email:
    Subject: "Билет на мероприятие: Мастер-класс по макияжу"
    Body:
      - Event details (title, date, time, location)
      - QR code ticket (embedded image)
      - Program/agenda
      - Dietary restrictions reminder (if provided)
      - Add to Google Calendar / iCal link
      - Map to venue
      - Cancellation policy
```

---

### User Story 12.2.5: Post-Event Thank You Email
**As a** member
**I want to** receive thank-you email after attending event
**So that** I feel appreciated and can provide feedback

**Acceptance Criteria:**
```gherkin
Scenario: Thank you email (1 day after event)
  Given I attended event yesterday
  When post-event email task runs
  Then I receive email:
    Subject: "Спасибо за участие в мероприятии!"
    Body:
      - Thank you message
      - Event photos (gallery link)
      - Feedback form (5-star rating + comments)
      - Bonus reward: +500₽ for participation
      - Announcement of next event
```

---

## 12.3 SMS Notifications (3 functions)

### User Story 12.3.1: SMS OTP Codes
**As a** user
**I want to** receive SMS codes for authentication
**So that** I can log in securely

**Acceptance Criteria:**
```gherkin
Scenario: Login SMS code
  Given I entered phone number on login screen
  When I tap "Send Code"
  Then I receive SMS within 30 seconds:
    Body: "Ваш код для входа в Свой Круг: 123456. Код действителен 5 минут."
  And code is 6 digits, numeric only
  And code expires after 5 minutes
```

**Technical Requirements:**
- SMS provider: SMS.ru (primary), SMSC.ru (backup)
- Rate limiting: Max 3 SMS per phone per hour
- Code generation: `random.randint(100000, 999999)`
- Store code hash in Redis with 5-minute TTL

---

### User Story 12.3.2: Critical Event SMS
**As a** member
**I want to** receive SMS for critical events
**So that** I don't miss important updates

**Acceptance Criteria:**
```gherkin
Scenario: Event cancellation SMS
  Given I registered for event "Мастер-класс по макияжу"
  When event is canceled by organizer
  Then I receive SMS:
    Body: "Мероприятие 'Мастер-класс по макияжу' (20 ноября) отменено. Подробности в приложении."
  And I receive push notification simultaneously
  And I receive email with full explanation
```

---

### User Story 12.3.3: Event Reminder SMS (2 hours)
**As a** member
**I want to** receive SMS reminder 2 hours before event
**So that** I don't forget to attend

**Acceptance Criteria:**
```gherkin
Scenario: 2-hour event reminder
  Given event starts at 19:00 today
  When it's 17:00 (2 hours before)
  Then I receive SMS:
    Body: "Напоминание: Мастер-класс по макияжу начнётся в 19:00. Адрес: Миндаль, ул. Тверская 10"
  And SMS is sent only if user enabled SMS reminders in settings
```

---

## 12.4 Notification Settings (2 functions)

### User Story 12.4.1: Manage Subscriptions
**As a** member
**I want to** control which notifications I receive
**So that** I'm not overwhelmed

**Acceptance Criteria:**
```gherkin
Scenario: View notification settings
  Given I go to Profile → Settings → Notifications
  When screen loads
  Then I see toggles for:
    Push Notifications:
      - ✅ Bonus accruals
      - ✅ Status upgrades
      - ✅ New coupons
      - ✅ Expiring coupons
      - ✅ Event confirmations
      - ✅ Event reminders
      - ✅ Voting updates
    Email Notifications:
      - ✅ Weekly digest
      - ✅ Status upgrades
      - ✅ Event tickets
      - ⬜ Marketing offers
    SMS Notifications:
      - ✅ Login codes (cannot disable)
      - ✅ Critical alerts
      - ⬜ Event reminders

Scenario: Toggle notification
  Given "New coupons" push is enabled
  When I toggle it off
  Then preference is saved to backend
  And I no longer receive "New coupon" pushes
```

**Technical Requirements:**
- Store preferences in `user_notification_preferences` table:
  ```sql
  user_notification_preferences (
    user_id UUID PRIMARY KEY,
    push_bonus BOOLEAN DEFAULT TRUE,
    push_status BOOLEAN DEFAULT TRUE,
    push_coupons BOOLEAN DEFAULT TRUE,
    push_events BOOLEAN DEFAULT TRUE,
    email_digest BOOLEAN DEFAULT TRUE,
    email_marketing BOOLEAN DEFAULT FALSE,
    sms_events BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMP
  )
  ```
- Check preferences before sending: `if user.preferences.push_bonus: send_push(...)`

---

### User Story 12.4.2: Quiet Hours
**As a** member
**I want to** set quiet hours for push notifications
**So that** I'm not disturbed at night

**Acceptance Criteria:**
```gherkin
Scenario: Set quiet hours
  Given I go to Settings → Notifications → Quiet Hours
  When I enable quiet hours
  And I set start time: 22:00 (10pm)
  And I set end time: 08:00 (8am)
  Then push notifications are suppressed between 22:00-08:00
  And notifications are queued and delivered at 08:00

Scenario: Critical notifications bypass quiet hours
  Given I have quiet hours enabled
  When critical event occurs (e.g., event cancellation)
  Then push is sent immediately (bypasses quiet hours)
  And push has high priority/critical alert
```

**Technical Requirements:**
- Store quiet hours: `quiet_hours_start TIME`, `quiet_hours_end TIME` in preferences table
- Check before sending push:
  ```python
  current_time = datetime.now().time()
  if user.quiet_hours_start <= current_time <= user.quiet_hours_end:
      if not notification.is_critical:
          queue_for_later(notification, user.quiet_hours_end)
  ```

---

## 📊 Technical Requirements

### Push Notification Stack
- **Provider:** Firebase Cloud Messaging (FCM)
- **Delivery:** via Celery async tasks
- **Deep linking:** React Navigation deep link handlers
- **Payload format:**
  ```json
  {
    "notification": {
      "title": "Начислено 700₽ бонусов!",
      "body": "За покупку в Миндаль. Баланс: 5,700₽"
    },
    "data": {
      "type": "bonus_accrual",
      "deep_link": "svoykrug://profile/bonuses",
      "transaction_id": "uuid"
    }
  }
  ```

### Email Stack
- **Provider:** SendGrid or Mailgun
- **Templates:** HTML with Jinja2 templating
- **Tracking:** Open rate, click rate via pixel tracking
- **Unsubscribe:** All emails include one-click unsubscribe link

### SMS Stack
- **Provider:** SMS.ru (primary), SMSC.ru (backup with automatic failover)
- **Rate limiting:** 3 SMS per phone per hour (Redis counter)
- **Cost optimization:** SMS only for critical alerts (OTP, event cancellations)

### Notification Delivery Guarantees
- **Push:** Best-effort delivery (FCM handles retry)
- **Email:** Guaranteed delivery within 5 minutes (SendGrid/Mailgun SLA)
- **SMS:** 95%+ delivery rate within 30 seconds

### Performance
- Push notification latency: <1 minute from trigger event
- Email delivery: <5 minutes
- SMS delivery: <30 seconds
- Celery queue: Max 1000 notifications/second capacity

---

## 🔄 Dependencies

- **All Modules:** Notifications are triggered by events across all modules
- **Module 1 (Mobile App):** Push notification handlers, deep linking
- **Module 2 (Loyalty):** Bonus, status notifications
- **Module 4 (Events):** Event confirmations, reminders
- **Module 5 (Cross-Promo):** Coupon notifications

---

## ✅ Success Criteria

- [ ] All 18 notification types implemented
- [ ] Push delivery rate: >95% (FCM metrics)
- [ ] Email open rate: >40% (industry benchmark: 20-30%)
- [ ] SMS delivery rate: >95%
- [ ] 0 spam complaints (<0.1% unsubscribe rate)
- [ ] Notification latency: <1 minute (p95)
- [ ] Quiet hours respected: 100% compliance

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Mobile Teams
**Status:** Critical - MVP Required
