# Sprint 2: Loyalty System & Mobile Integration

**Sprint:** Sprint 2
**Sprint Goal:** Implement core loyalty features (transactions, bonuses) and integrate mobile app with backend
**Dates:** 2025-11-18 → 2025-12-01 (2 weeks)
**Team Capacity:** 21 story points
**Status:** Planning

---

## 📊 Sprint Overview

| Metric | Value |
|--------|-------|
| **Committed Story Points** | 21 |
| **Completed Story Points** | 0 |
| **In Progress** | 0 tasks |
| **Blocked** | 0 tasks |
| **Sprint Progress** | 0% |
| **Days Remaining** | 14 days |

---

## 🎯 Sprint Goal

**Sprint 2 Core Loyalty:**
Implement transaction tracking, automatic bonus accrual, and integrate mobile app with backend API. Enable full authentication flow (SMS OTP) and display real transaction/bonus data in mobile app.

---

## 📋 Sprint Backlog

### Task 1: Transaction System Backend (5 pts) - Priority: P0
**Owner:** Backend Team
**Status:** Not Started
**Dependencies:** Sprint 1 (Backend API Framework ✅, Auth System ✅)

**Tasks:**
- [ ] Create Transaction model (user_id, business_id, amount, type, bonus_amount, status, created_at)
- [ ] Create Alembic migration for transactions table
- [ ] Implement Transaction CRUD service (create, get, list, update, cancel)
- [ ] Create Transaction API endpoints:
  - POST /api/v1/transactions/ - Create manual transaction
  - GET /api/v1/transactions/{id} - Get transaction by ID
  - GET /api/v1/transactions/ - List user transactions (paginated, filtered)
  - GET /api/v1/transactions/stats - Get spending statistics
- [ ] Add transaction validation (amount > 0, business exists, user exists)
- [ ] Write 10 test cases for Transaction API

**Acceptance Criteria:**
- Transactions can be created manually (QR scan simulation)
- Transactions are linked to user and business
- Transaction history is queryable with filters (date, business, category)
- Spending statistics API ready (total, by month, by category)
- 10 tests passing

**Module Reference:** docs/requirements/module-03-transactions.md (Functions 3.1-3.4)

---

### Task 2: Bonus System Backend (8 pts) - Priority: P0
**Owner:** Backend Team
**Status:** Not Started
**Dependencies:** Task 1 (Transaction System ✅)

**Tasks:**
- [ ] Create Bonus model (user_id, transaction_id, amount, type, status, expires_at)
- [ ] Create Alembic migration for bonuses table
- [ ] Implement automatic bonus accrual logic:
  - Celery task: `accrue_bonus(transaction_id)`
  - Calculate bonus % based on status tier (Insider: 5%, VIP: 7%, Elite: 10%, Inner Circle: 15%)
  - First purchase in category: 1.5x multiplier
  - Update user.bonus_balance atomically
- [ ] Implement bonus redemption logic:
  - POST /api/v1/bonuses/redeem
  - Validate sufficient balance
  - Deduct bonuses, create redemption record
- [ ] Create Bonus API endpoints:
  - GET /api/v1/bonuses/ - Get user bonus history
  - GET /api/v1/bonuses/balance - Get current balance
  - POST /api/v1/bonuses/redeem - Redeem bonuses
- [ ] Implement status tier upgrade logic:
  - Check total_spend thresholds: VIP (50K), Elite (150K), Inner Circle (300K)
  - Auto-upgrade user status_tier
  - Send upgrade notification (Module 12 stub)
- [ ] Write 12 test cases for Bonus API

**Acceptance Criteria:**
- Bonuses accrued automatically after transaction creation (5-15% based on tier)
- First purchase in new category gets 1.5x multiplier
- Bonuses can be redeemed (balance deducted)
- Status tier auto-upgrades based on total_spend
- Bonus history queryable
- 12 tests passing

**Module Reference:** docs/requirements/module-02-loyalty-system.md (Functions 2.1.1-2.1.6, 2.2.1-2.2.4)

---

### Task 3: Mobile Backend Integration (5 pts) - Priority: P0
**Owner:** Mobile Team
**Status:** Not Started
**Dependencies:** Sprint 1 (Auth API ✅, Mobile Shell ✅)

**Tasks:**
- [ ] Create API client (axios):
  - Base URL configuration
  - Request/response interceptors
  - Token injection (Authorization: Bearer {accessToken})
  - Automatic token refresh on 401
  - Error handling (network errors, API errors)
- [ ] Integrate SMS OTP flow:
  - Implement sendOTP screen (call POST /auth/send-otp)
  - Implement VerifyOTP screen (call POST /auth/verify-otp)
  - Implement Register screen (call POST /auth/register)
  - Store tokens in Redux + MMKV (persistent storage)
- [ ] Integrate Login flow:
  - Call POST /auth/login
  - Handle success (store tokens, navigate to Main)
  - Handle errors (show error messages)
- [ ] Implement token refresh:
  - Auto-refresh when access token expires
  - Use refresh token from storage
  - Update tokens in Redux + MMKV
- [ ] Implement logout:
  - Call POST /auth/logout
  - Clear tokens from Redux + MMKV
  - Navigate to Welcome screen
- [ ] Add loading states and error handling to all API calls

**Acceptance Criteria:**
- SMS OTP flow works end-to-end (send → verify → register → login)
- Tokens stored persistently (survive app restart)
- Token auto-refresh works (401 → refresh → retry)
- Logout clears tokens and navigates to Welcome
- Error messages shown to user (network errors, API errors)
- Loading spinners during API calls

**Module Reference:** docs/requirements/module-01-mobile-app.md (Functions 1.1.3-1.1.5, 1.2.1)

---

### Task 4: Mobile Transaction & Bonus UI (3 pts) - Priority: P0
**Owner:** Mobile Team
**Status:** Not Started
**Dependencies:** Task 1 ✅, Task 2 ✅, Task 3 ✅

**Tasks:**
- [ ] Create TransactionHistoryScreen:
  - Fetch transactions from GET /api/v1/transactions/
  - Display as scrollable list (date, business, amount, bonus)
  - Pull-to-refresh
  - Infinite scroll (pagination)
  - Filters: date range, business, category
- [ ] Create TransactionDetailScreen:
  - Fetch transaction details from GET /api/v1/transactions/{id}
  - Display full transaction info (business, amount, bonus accrued, date, receipt)
- [ ] Update HomeScreen to show real data:
  - Fetch user profile from GET /api/v1/users/{id}
  - Fetch bonus balance from GET /api/v1/bonuses/balance
  - Display actual bonus_balance and total_spend
  - Show spending statistics (monthly, by category)
- [ ] Add BonusHistoryScreen (in Main tabs):
  - Fetch bonus history from GET /api/v1/bonuses/
  - Display accruals and redemptions
  - Show expiring bonuses warning

**Acceptance Criteria:**
- Transaction history loads and displays real backend data
- Transaction detail screen shows full info
- Home screen shows real balance and stats
- Bonus history screen shows accrual/redemption records
- Pull-to-refresh works on all list screens
- Pagination works (load more on scroll)
- Filters work (date, business, category)

**Module Reference:** docs/requirements/module-01-mobile-app.md (Functions 1.4.1-1.4.4), module-03-transactions.md (Functions 3.3-3.5)

---

## 📈 Sprint Burndown

```
Day 1:  21 pts remaining
Day 2:  TBD
Day 3:  TBD
...
```

**Status:** Planning Phase

---

## 🚧 Blockers & Risks

### Current Blockers
- None

### Identified Risks
1. **SMS.ru API Integration**
   - Impact: Need API key for production SMS sending
   - Mitigation: Use MockSMSService for Sprint 2, add real integration in Sprint 3
   - Owner: Backend Team
   - Status: 🟡 Medium Priority

2. **Celery Worker Setup**
   - Impact: Async bonus accrual requires Celery
   - Mitigation: Add Celery container to docker-compose
   - Owner: Backend Team
   - Status: 🟡 Medium Priority

3. **Mobile Testing Devices**
   - Impact: Need iOS/Android devices for testing
   - Mitigation: Use simulators/emulators for Sprint 2
   - Owner: Mobile Team
   - Status: 🟢 Low Priority

---

## 📝 Sprint Ceremonies

### Sprint Planning
- **Date:** 2025-11-18
- **Duration:** 2 hours
- **Outcome:** Sprint backlog finalized (21 pts committed)

### Daily Standup
- **Time:** Daily at 10:00 AM Moscow time
- **Duration:** 15 minutes
- **Format:** What done yesterday / What doing today / Blockers

### Sprint Review
- **Date:** 2025-12-01 (End of Week 2)
- **Duration:** 1 hour
- **Demo:** Transaction creation, bonus accrual, mobile app with real data

### Sprint Retrospective
- **Date:** 2025-12-01 (End of Week 2)
- **Duration:** 45 minutes
- **Outcome:** Action items for Sprint 3

---

## 🎯 Sprint 2 Success Metrics

- [ ] Transaction API implemented (5 endpoints)
- [ ] Bonus accrual works automatically (Celery task)
- [ ] Status tier auto-upgrade works (VIP at 50K spend)
- [ ] Mobile app integrated with backend (SMS OTP flow complete)
- [ ] Mobile app shows real transaction/bonus data
- [ ] All tests passing (22+ test cases total)
- [ ] No critical bugs
- [ ] Code review completed

---

**Last Updated:** 2025-11-18
**Status:** Planning
**Next Update:** Sprint 2 Day 1
