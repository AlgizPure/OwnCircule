# Module 4: Events Hub & Management - Requirements

**Module ID:** MOD-04
**Total Functions:** 28
**Priority:** P0 (Critical - MVP)
**Dependencies:** Module 1 (Mobile App), Module 15 (Events Budget), Module 12 (Notifications)
**Tech Stack:** React Native 0.81, PostgreSQL 16.11, Firebase Cloud Messaging, Celery 5.4.x

---

## 📋 Module Overview

Events Hub is the community engagement platform where members discover exclusive events (wellness workshops, beauty masterclasses, networking dinners), register, attend, and vote on proposals. VIP/Elite members can propose new events via constructor with weighted voting. Events are funded from ecosystem budget (Module 15).

**Key Subsystems:**
- 4.1 Event Management (10 functions): Create, edit, publish, cancel events
- 4.2 Registration & Attendance (8 functions): Register, waitlist, QR tickets, check-in
- 4.3 Voting & Constructor (10 functions): Propose events, vote, weighted results

---

## 4.1 Event Management (10 functions)

### User Story 4.1.1-4.1.3: Create Event
**As a** platform administrator or business
**I want to** create new events
**So that** members can attend

**Acceptance Criteria:**
```gherkin
Scenario: Create event (admin panel)
  Given I am logged in as admin
  When I go to Events → "Create Event"
  Then I fill form:
    - Title (required, max 100 chars)
    - Description (required, rich text)
    - Cover image upload (16:9 ratio, max 5MB)
    - Date & time (datetime picker)
    - Location (address + map pin)
    - Max participants (number)
    - Min status tier (Insider/VIP/Elite/Inner Circle)
    - Format (Free/Paid/Closed)
    - Budget allocated (₽, from events fund)
  And I click "Save Draft" or "Publish Now"
  Then event is created with status="draft" or "published"

Scenario: Add event program
  Given I am creating event
  When I click "Add Program"
  Then I see time-slot editor:
    - 19:00-19:30: Welcome drinks
    - 19:30-20:30: Masterclass
    - 20:30-21:00: Q&A
  And I can add/remove/reorder slots

Scenario: Add speakers
  Given event is workshop-type
  When I add speakers
  Then I upload:
    - Speaker photo
    - Name, title, bio (max 500 chars)
  And speakers appear on event detail page
```

---

### User Story 4.1.4-4.1.6: Edit & Configure Event
**As a** event creator
**I want to** edit event details before publication
**So that** information is accurate

**Acceptance Criteria:**
```gherkin
Scenario: Edit draft event
  Given event is in draft status
  When I edit any field
  Then changes are saved
  And event remains draft until I publish

Scenario: Set min status tier
  Given event is VIP-only
  When I set "Min Status" = VIP
  Then only VIP/Elite/Inner Circle members can register
  And Insider members see "VIP+ only" badge

Scenario: Set max participants
  Given event has limited capacity
  When I set "Max Participants" = 20
  Then registration closes after 20 people
  And 21st person is added to waitlist
```

---

### User Story 4.1.7-4.1.10: Publish, Cancel, Archive Events
**As a** event creator
**I want to** manage event lifecycle
**So that** events are properly communicated

**Acceptance Criteria:**
```gherkin
Scenario: Publish event
  Given event is in draft
  When I click "Publish Event"
  Then event.status = "published"
  And event appears in Events Hub immediately
  And push notifications sent to target audience
    (e.g., if VIP event → notify all VIP+ members)

Scenario: Cancel event
  Given event is published with registrations
  When I click "Cancel Event"
  And I enter cancellation reason
  Then event.status = "cancelled"
  And all registered users receive:
    - Push notification
    - SMS (critical alert)
    - Email with apology + reason
  And registrations are refunded (if paid event)

Scenario: Archive completed event
  Given event date has passed
  When event auto-archives (Celery task runs next day)
  Then event.status = "completed"
  And event moves to "Past Events" section
  And thank-you emails sent to attendees
```

---

## 4.2 Registration & Attendance (8 functions)

### User Story 4.2.1-4.2.2: Register for Event
**As a** member
**I want to** register for events
**So that** I can attend

**Acceptance Criteria:**
```gherkin
Scenario: Register for free event
  Given I view event "Мастер-класс по макияжу"
  And event has 5 spots remaining
  When I tap "Зарегистрироваться"
  Then I see confirmation dialog
  And I tap "Confirm"
  Then registration is created
  And I receive push "Вы зарегистрированы!"
  And I receive email with QR ticket
  And spots remaining = 4

Scenario: Register with +1 guest
  Given event allows guests
  When I register
  Then I see toggle "Взять +1 гостя?"
  And I enable it and enter guest: Name, Phone
  Then 2 spots are reserved (not 1)
  And both QR tickets are generated
```

---

### User Story 4.2.3: Dietary Restrictions
**As a** member
**I want to** specify dietary restrictions
**So that** organizers accommodate me

**Acceptance Criteria:**
```gherkin
Scenario: Add dietary restrictions
  Given event includes food/drinks
  When I register
  Then I see optional field "Dietary Restrictions"
  And I enter: "Vegetarian, no nuts"
  Then restrictions are saved
  And visible to event organizer in attendee list
```

---

### User Story 4.2.4-4.2.5: Waitlist & Cancellation
**As a** member
**I want to** join waitlist if event is full
**So that** I can attend if spot opens

**Acceptance Criteria:**
```gherkin
Scenario: Join waitlist
  Given event is full (20/20 registered)
  When I try to register
  Then I see "Event Full - Join Waitlist?"
  And I tap "Join Waitlist"
  Then I'm added to waitlist (position #1)
  And I receive notification if spot opens

Scenario: Cancel my registration
  Given I registered but can't attend
  When I tap "Отменить регистрацию"
  Then registration is cancelled
  And spot is freed for waitlist person #1
  And waitlist person receives push "Место освободилось!"
```

---

### User Story 4.2.6-4.2.7: QR Ticket & Check-in
**As a** member
**I want to** show QR ticket at entrance
**So that** I can check in to event

**Acceptance Criteria:**
```gherkin
Scenario: Generate QR ticket
  Given I registered for event
  When registration is confirmed
  Then QR ticket is generated with:
    - Event title, date, time, location
    - Member name + status badge
    - Unique ticket ID (QR code)
  And ticket is viewable in app: Events → "Мои регистрации" → Event
  And ticket is sent via email as backup

Scenario: Check-in at event
  Given I arrive at event venue
  When organizer scans my QR code
  Then check-in is recorded (timestamp, location)
  And I see "✅ Checked In"
  And attendance bonus (+500₽) is awarded after event
```

---

### User Story 4.2.8: Event Reminder Notifications
**As a** member
**I want to** receive event reminders
**So that** I don't forget

**Acceptance Criteria:**
```gherkin
Scenario: 24-hour reminder
  Given event is tomorrow at 19:00
  When it's 19:00 today (24h before)
  Then I receive push:
    Title: "Завтра: Мастер-класс по макияжу"
    Body: "19:00, Миндаль, ул. Тверская 10. Не забудьте QR-билет!"

Scenario: 2-hour reminder
  Given event starts in 2 hours
  When reminder task runs
  Then I receive push + SMS (if enabled):
    "Через 2 часа: Мастер-класс по макияжу. Адрес: Миндаль, ул. Тверская 10"
```

---

## 4.3 Voting & Constructor (10 functions)

### User Story 4.3.1: Propose Event (VIP/Elite)
**As a** VIP/Elite member
**I want to** propose new event ideas
**So that** community votes on them

**Acceptance Criteria:**
```gherkin
Scenario: Create event proposal
  Given I am VIP member
  When I go to Events Hub → "Предложить мероприятие"
  Then I fill proposal form (Module 1.6):
    - Event type (predefined or custom)
    - Title, description
    - Suggested date, location, budget
    - Program (optional)
  And I set visibility (All/VIP+/Elite)
  And I submit for voting
  Then proposal.status = "voting"
  And 7-day voting period starts
  And all eligible members receive push notification
```

---

### User Story 4.3.2-4.3.3: Vote on Proposals
**As a** member
**I want to** vote on event proposals
**So that** community decides what events happen

**Acceptance Criteria:**
```gherkin
Scenario: Cast vote
  Given I see proposal "Wine Tasting Evening"
  When I tap "Голосовать"
  Then I see voting screen:
    - Proposal details (title, description, budget)
    - Vote options: "За" (Yes) or "Против" (No)
  And I select "За"
  Then my vote is recorded
  And I see "Спасибо за голос!"

Scenario: Weighted voting
  Given I am Elite member (vote weight = 3x)
  When I vote "За"
  Then my vote counts as 3 votes
  And voting results reflect weighted count
  And I see "Ваш голос: 3x (Elite статус)"
```

**Technical Requirements:**
- Vote weights:
  - Insider: 1.0
  - VIP: 2.0
  - Elite: 3.0
  - Inner Circle: 5.0
- Voting period: 7 days from proposal submission
- Vote stored with user_id + weight for audit

---

### User Story 4.3.4-4.3.5: View Voting Results
**As a** member
**I want to** see real-time voting results
**So that** I know which proposals are winning

**Acceptance Criteria:**
```gherkin
Scenario: View live results
  Given voting is in progress
  When I view proposal
  Then I see:
    - Total votes: 45 (32 за, 13 против)
    - Weighted votes: 102 (75 за, 27 против)
    - Approval rate: 73.5%
    - Time remaining: 4 days
  And I see progress bars (visual)

Scenario: Voting period ends
  Given 7 days have passed
  When voting closes automatically (Celery task)
  Then proposal is marked "voting_closed"
  And results are finalized
  And proposer receives notification:
    - If approved (>60%): "Ваше предложение одобрено!"
    - If rejected (<60%): "К сожалению, предложение не набрало голосов"
```

---

### User Story 4.3.6-4.3.10: Top Proposals & Approval Flow
**As a** member
**I want to** see top proposals of the month
**So that** I know what events are coming

**Acceptance Criteria:**
```gherkin
Scenario: View Top-3 proposals
  Given it's end of month with 10 proposals
  When I go to Events Hub → "Топ предложений месяца"
  Then I see Top-3 by approval rate:
    1. Wine Tasting Evening - 85% approval, 120 votes
    2. Yoga Retreat - 78% approval, 95 votes
    3. Networking Brunch - 72% approval, 80 votes
  And Top-3 are prioritized for realization

Scenario: Superadmin approves proposal
  Given proposal "Wine Tasting Evening" won voting (85%)
  When superadmin reviews in Module 10
  And checks budget availability (VIP category has 10,000₽)
  And clicks "Approve & Allocate Budget"
  Then proposal becomes real event (status="approved")
  And budget is allocated
  And event is created and published
  And proposer receives: "Ваше мероприятие одобрено и запланировано!"

Scenario: Edit proposal before voting
  Given I submitted proposal but haven't started voting
  When I edit details
  Then changes are saved
  And I can resubmit for voting

Scenario: Delete my proposal
  Given I want to withdraw proposal
  When I click "Удалить предложение"
  Then proposal is deleted
  And votes are discarded
```

---

## 📊 Technical Requirements

### Database Schema
```sql
events (
  id UUID PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  cover_image_url VARCHAR(255),
  date TIMESTAMP,
  location TEXT,
  max_participants INT,
  min_status_tier VARCHAR(20),
  format VARCHAR(20),  -- 'free' | 'paid' | 'closed'
  budget_allocated DECIMAL(10,2),
  status VARCHAR(20),  -- 'draft' | 'published' | 'cancelled' | 'completed'
  created_by UUID,
  created_at TIMESTAMP
)

event_registrations (
  id UUID PRIMARY KEY,
  event_id UUID REFERENCES events(id),
  user_id UUID REFERENCES users(id),
  guest_name VARCHAR(100) NULL,
  guest_phone VARCHAR(15) NULL,
  dietary_restrictions TEXT NULL,
  status VARCHAR(20),  -- 'registered' | 'waitlist' | 'cancelled' | 'attended'
  checked_in_at TIMESTAMP NULL,
  ticket_qr_code VARCHAR(255),
  created_at TIMESTAMP
)

event_proposals (
  id UUID PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  proposed_by UUID REFERENCES users(id),
  visibility VARCHAR(20),  -- 'all' | 'vip_plus' | 'elite'
  status VARCHAR(20),  -- 'draft' | 'voting' | 'approved' | 'rejected'
  voting_ends_at TIMESTAMP,
  created_at TIMESTAMP
)

event_votes (
  proposal_id UUID REFERENCES event_proposals(id),
  user_id UUID REFERENCES users(id),
  vote VARCHAR(10),  -- 'yes' | 'no'
  vote_weight DECIMAL(3,1),  -- 1.0, 2.0, 3.0, 5.0
  voted_at TIMESTAMP,
  PRIMARY KEY (proposal_id, user_id)
)
```

### Performance
- Event list load: <300ms
- Registration: <500ms (create + generate QR + send email)
- QR check-in: <200ms (offline-first with sync)
- Voting results: real-time updates via WebSocket or polling every 5s

---

## 🔄 Dependencies

- **Module 1 (Mobile App):** Event Hub UI, registration flow, QR tickets
- **Module 12 (Notifications):** Reminders, confirmations, voting notifications
- **Module 15 (Events Budget):** Budget allocation and spending tracking

---

## ✅ Success Criteria

- [ ] All 28 functions implemented
- [ ] Event registration completes in <1 second
- [ ] QR check-in works offline (sync when online)
- [ ] 80%+ of registered members attend events (low no-show rate)
- [ ] Voting participation: 60%+ of eligible members vote on proposals
- [ ] Top-3 proposals each month get realized

---

**Last Updated:** 2025-11-17
**Owner:** Backend + Mobile Teams
**Status:** Critical - MVP Required
