# Current Sprint Status - Свой Круг

**Sprint:** Sprint 1 (Foundation & Infrastructure)
**Sprint Goal:** Establish backend foundation, authentication, and mobile app shell
**Dates:** 2025-11-17 → 2025-11-30 (2 weeks)
**Team Capacity:** 20 story points (Bootstrap AI-assisted development)

---

## 📊 Sprint Overview

| Metric | Value |
|--------|-------|
| **Committed Story Points** | 20 |
| **Completed Story Points** | 7 |
| **In Progress** | 0 tasks |
| **Blocked** | 0 tasks |
| **Sprint Progress** | 35% (Infrastructure + Backend API complete) |
| **Days Remaining** | 14 days |

---

## 🎯 Sprint Goal

**Sprint 1 Foundation:**
Set up development infrastructure, create backend API framework with authentication, and initialize mobile app shell. Establish CI/CD pipeline and development workflows.

---

## 📋 Sprint Backlog

### ⏳ Not Started (2 tasks, 13 pts)

#### 2. JWT Authentication System (8 pts) - Priority: P0
**Owner:** Backend Team
**Status:** Not Started
**Dependencies:** Backend API Framework
**Tasks:**
- [ ] Implement RS256 JWT token signing (ADR-004)
- [ ] Create access token (15 min) + refresh token (7 days) flow
- [ ] Add token blacklist table for logout
- [ ] Implement SMS OTP integration (SMS.ru API)
- [ ] Create auth endpoints: /register, /login, /refresh, /logout
- [ ] Add password hashing (bcrypt)
- [ ] Create middleware for protected routes

**Acceptance Criteria:**
- Users can register with phone +7 XXX XXX-XX-XX
- SMS OTP code sent and verified
- JWT tokens generated and validated
- Refresh token rotation works
- Logout blacklists tokens
- Protected routes return 401 for invalid tokens

**Module Reference:** docs/requirements/module-01-mobile-app.md (Functions 1.1.3-1.1.5)

---

#### 3. Mobile App Shell (5 pts) - Priority: P0
**Owner:** Mobile Team
**Status:** Not Started
**Tasks:**
- [ ] Initialize React Native 0.81 project (TypeScript)
- [ ] Configure React Navigation 6 (stack + bottom tabs)
- [ ] Set up Redux Toolkit 2.10.1 for state management
- [ ] Create design system tokens from docs/design/resources/design-tokens.json
- [ ] Implement basic screens: Welcome, Login (SMS), Home
- [ ] Add Tiffany Blue (#0ABAB5) theme
- [ ] Configure iOS + Android builds

**Acceptance Criteria:**
- App runs on iOS simulator + Android emulator
- Navigation works (stack + tabs)
- Redux store configured
- Design tokens imported
- Welcome screen shows with Tiffany Blue branding
- Login screen has phone input (no backend integration yet)

**Module Reference:** docs/requirements/module-01-mobile-app.md (Functions 1.1.1-1.1.2)

---

### 🚧 In Progress (0 tasks, 0 pts)
- Infrastructure complete, awaiting backend API implementation

---

### ✅ Done (2 tasks, 7 pts)

#### 1. Backend API Framework (5 pts) - Priority: P0 ✅
**Owner:** Backend Team
**Status:** COMPLETE
**Completed:** 2025-11-17

**Deliverables:**
- ✅ Alembic migration created (User + Business tables)
  - users table with enum types (UserRole, StatusTier)
  - businesses table with JSON fields (coordinates, CRM credentials)
  - Proper indexes for phone, email, slug, category
- ✅ Pydantic schemas:
  - UserCreate (with password validation)
  - UserUpdate, UserRead, UserInDB, UserList
  - Password strength validation (8+ chars, uppercase, lowercase, digit)
- ✅ User service layer (CRUD operations):
  - create_user, get_by_id, get_by_phone, get_by_email
  - update_user, delete_user (soft delete)
  - get_users (paginated list)
  - Password hashing with bcrypt (12 rounds)
- ✅ User API endpoints (/api/v1/users):
  - POST / - Create user (registration)
  - GET /{user_id} - Get user by ID
  - GET / - Get paginated users list
  - PATCH /{user_id} - Update user profile
  - DELETE /{user_id} - Soft delete user
- ✅ Pytest configuration:
  - pytest.ini with async support
  - conftest.py with fixtures (db_session, client)
  - SQLite in-memory test database
  - 12 test cases for User API (100% endpoint coverage)
- ✅ Database initialization:
  - PostgreSQL init.sql (extensions, timezone)
  - ClickHouse init.sql (5 analytics tables)

**Acceptance Criteria Met:**
- ✅ FastAPI server structure ready
- ✅ PostgreSQL models defined (User + Business)
- ✅ Alembic migrations setup complete
- ✅ Health check endpoint exists (/health)
- ✅ API router connected (/api/v1/users, /api/v1/ping)
- ✅ Test coverage: 12 test cases passing
- ✅ Architecture follows docs/backend/ structure

---

#### 4. Development Infrastructure (2 pts) - Priority: P0 ✅
**Owner:** DevOps / Claude
**Status:** COMPLETE
**Completed:** 2025-11-17

**Deliverables:**
- ✅ Project directory structure (backend/, mobile/, infrastructure/)
- ✅ Docker Compose configuration (PostgreSQL 16.11, Redis 8.2, ClickHouse 25.8)
- ✅ Backend Dockerfile (Python 3.13, FastAPI setup)
- ✅ Backend requirements.txt (45+ dependencies with pinned versions)
- ✅ FastAPI application structure:
  - app/main.py (entry point with CORS, health check)
  - app/core/config.py (Pydantic settings)
  - app/core/database.py (SQLAlchemy async setup)
  - app/core/logging.py (JSON logging for production)
  - app/api/v1/ (API router skeleton)
- ✅ Database models created:
  - User model (auth, profile, role, status tier)
  - Business model (partner businesses, CRM config)
- ✅ Alembic migrations setup (async support)
- ✅ Environment templates (.env.example for backend)
- ✅ .gitignore files (root, backend, mobile)
- ✅ Mobile package.json (React Native 0.81, TypeScript 5.7)
- ✅ Comprehensive setup documentation (SPRINT1_SETUP.md, 1,474 lines)

**Acceptance Criteria Met:**
- ✅ Docker Compose configuration ready (`docker-compose up` command available)
- ✅ Database models defined with SQLAlchemy
- ✅ Services configured: PostgreSQL (5432), Redis (6379), ClickHouse (9000/8123)
- ✅ Comprehensive developer guide created (SPRINT1_SETUP.md)
- ⚠️ CI/CD pipeline - Pending (not required for initial setup)
- ⚠️ Pre-commit hooks - Pending (deferred to Sprint 2)

---

## 🚦 Daily Standup Format

### Team Member 1 (Backend Lead)
**Yesterday:**
- N/A (team not assembled)

**Today:**
- N/A

**Blockers:**
- None

---

### Team Member 2 (Mobile Lead)
**Yesterday:**
- N/A (team not assembled)

**Today:**
- N/A

**Blockers:**
- None

---

## 📈 Sprint Burndown

```
Day 1:  N/A
Day 2:  N/A
Day 3:  N/A
Day 4:  N/A
Day 5:  N/A
Day 6:  N/A
Day 7:  N/A
Day 8:  N/A
Day 9:  N/A
Day 10: N/A
```

**Status:** Pre-Sprint (no burndown data)

---

## 🚧 Blockers & Risks

### Current Blockers
- **None** (documentation phase, no active development)

### Identified Risks for Sprint 1
1. **Team Hiring Delay**
   - Impact: Cannot start Sprint 1 without core team
   - Mitigation: Begin recruiting immediately
   - Owner: Product Manager
   - Status: 🔴 High Priority

2. **Yandex Cloud Setup**
   - Impact: Need infrastructure for development environment
   - Mitigation: Create account in parallel with hiring
   - Owner: DevOps Engineer
   - Status: 🟡 Medium Priority

3. **CRM API Access**
   - Impact: Cannot test integrations without credentials
   - Mitigation: Finalize partnership agreements ASAP
   - Owner: Product Manager
   - Status: 🟡 Medium Priority

---

## 📝 Sprint Retrospective (Post-Sprint)

**To be filled after Sprint 1 completes**

### What Went Well
- TBD

### What Didn't Go Well
- TBD

### Action Items
- TBD

---

## 📅 Upcoming Sprint 1 (Planned)

### Sprint 1 Goal
"Establish backend foundation, authentication, and mobile app shell"

### Planned Stories (20 story points)
1. **Backend API Framework (5 pts)**
   - Set up FastAPI project structure
   - Configure PostgreSQL database
   - Create base models (users, businesses, bonuses)

2. **JWT Authentication (8 pts)**
   - Implement RS256 token signing
   - Create access + refresh token flow
   - Add token blacklist for logout
   - Implement SMS OTP (Module 12.3.1)

3. **Mobile App Shell (5 pts)**
   - Set up React Native 0.81 project
   - Configure navigation (React Navigation 6)
   - Create basic screens (Welcome, Login, Home)

4. **Security Foundation (2 pts)**
   - Set up AES-256 encryption (Module 13)
   - Implement RBAC basics
   - Create audit log table

### Dependencies
- Yandex Cloud account created
- Team hired (2 backend, 1 mobile developer minimum)
- Development environments set up (Docker Compose)

---

## 🔄 Sprint Ceremonies

### Sprint Planning
- **Date:** TBD (when team assembled)
- **Duration:** 2 hours
- **Attendees:** Product Manager, Backend Leads, Mobile Lead, DevOps
- **Outcome:** Sprint backlog finalized, capacity committed

### Daily Standup
- **Time:** TBD (daily at 10:00 AM Moscow time recommended)
- **Duration:** 15 minutes
- **Format:** What done yesterday / What doing today / Blockers

### Sprint Review
- **Date:** End of Sprint 1 (Week 2)
- **Duration:** 1 hour
- **Attendees:** Full team + stakeholders
- **Outcome:** Demo backend API + mobile shell

### Sprint Retrospective
- **Date:** End of Sprint 1 (Week 2)
- **Duration:** 45 minutes
- **Attendees:** Development team only
- **Outcome:** Action items for Sprint 2

---

**Last Updated:** 2025-11-17
**Status:** Pre-Sprint (Awaiting Team Assembly)
**Next Update:** Sprint 1 Day 1
