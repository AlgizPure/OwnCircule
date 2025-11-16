# PROJECT CHANGES LOG

**Purpose:** Track all significant changes to project scope, requirements, or approach  
**Use:** Quick reference of "what changed and why"

---

## 📝 CHANGE ENTRY TEMPLATE

## [Date]: [Change Title]

**Type:** Feature Add / Feature Remove / Feature Change / Scope Change / Tech Change / Process Change  
**Impact:** LOW / MEDIUM / HIGH / CRITICAL  
**Status:** Proposed / Approved / Implemented / Rolled Back

### What Changed

[Clear description of the change]

### Why

[Rationale for the change]

### Impact

**Affected:**
- [Module/Feature 1]
- [Module/Feature 2]

**Timeline Impact:** [None / +X days / -X days]

**Documentation Updated:**
- [ ] PRD
- [ ] ROADMAP
- [ ] Requirements
- [ ] Other: [specify]

### Related

- Decision: DEC-XXX
- Requirements: [module]_requirements.md
- Discussion: [link]

---

## 📚 CHANGES HISTORY

### 2025-11-08: Added Avatar Upload Feature

**Type:** Feature Add  
**Impact:** MEDIUM  
**Status:** Implemented

#### What Changed

Added avatar upload functionality to user profiles.
Users can now upload profile pictures (JPEG/PNG, max 5MB).

#### Why

User research showed profile pictures increase engagement by 40%.
Top feature request from beta users (15/20 requested).

#### Impact

**Affected:**
- Auth module (avatar field added)
- Profile module (upload UI)
- Storage (AWS S3 integration)

**Timeline Impact:** None (was in backlog, pulled into MVP)

**Documentation Updated:**
- [x] PRD v1.8 (added FR-PROF-005)
- [x] ROADMAP v1.5 (added to MVP)
- [x] profile_requirements.md v1.2
- [x] TECH_STACK.md (AWS S3 added)

#### Related

- Decision: DEC-008 (AWS S3 for storage)
- Requirements: profile_requirements.md FR-PROF-005
- User Research: `/research/beta-feedback-2025-11.md`

---

### 2025-11-05: Removed Social Login from MVP

**Type:** Feature Remove  
**Impact:** MEDIUM  
**Status:** Approved

#### What Changed

Moved Social Login (Google/Facebook OAuth) from MVP to Phase 1.
MVP will ship with email/password authentication only.

#### Why

Timeline pressure - team behind schedule.
Social login saves 5-7 days of development.
Email/password sufficient for MVP validation.

#### Impact

**Affected:**
- Auth module (scope reduced)
- Onboarding flow (simpler)

**Timeline Impact:** -5 days (MVP back on track)

**Documentation Updated:**
- [x] PRD v1.7 (moved to Phase 1)
- [x] ROADMAP v1.4 (Phase 1 updated)
- [x] auth_requirements.md v1.1.1 (marked deferred)

#### Related

- Decision: DEC-002 (Defer Social Login)
- Discussion: Team meeting 2025-11-04
- Stakeholder approval: Email from PM

---

### 2025-11-03: Changed Database from MongoDB to PostgreSQL

**Type:** Tech Change  
**Impact:** HIGH  
**Status:** Implemented

#### What Changed

Switched from MongoDB to PostgreSQL as primary database.
All schemas redesigned for relational model.

#### Why

**Original plan:** MongoDB (flexible schema)
**Reality:** Our data is highly relational (users → teams → tasks)
**MongoDB issues:** 
- Complex joins difficult
- Data consistency challenges
- Team more familiar with SQL

**PostgreSQL benefits:**
- Perfect fit for relational data
- ACID compliance
- JSON support (flexibility when needed)
- Better tooling

#### Impact

**Affected:**
- All backend code (data layer rewrite)
- Deployment (PostgreSQL instead of MongoDB)
- Development setup

**Timeline Impact:** +3 days (one-time migration)

**Documentation Updated:**
- [x] PRD v1.6 (data model updated)
- [x] TECH_STACK.md v1.2 (PostgreSQL section)
- [x] ARCHITECTURE.md v1.3 (data layer)
- [x] All requirement files (data schemas)

#### Related

- Decision: DEC-001 (PostgreSQL choice)
- Architecture: ARCHITECTURE.md section on Data Layer
- Migration: `/database/migration-plan.md`

---

### 2025-11-01: Scope Increased - Analytics Module Added

**Type:** Feature Add / Scope Change  
**Impact:** HIGH  
**Status:** Approved

#### What Changed

Added Analytics module to MVP scope.
Features:
- Task completion metrics
- Team productivity dashboard
- Time tracking insights

Originally planned for Phase 1, moved to MVP.

#### Why

**Stakeholder request:** CEO wants data for investor demo.
**Business need:** Analytics differentiator vs competitors.
**User feedback:** Beta users asking "where are my stats?"

#### Impact

**Affected:**
- NEW: Analytics module
- Tasks module (time tracking integration)
- Dashboard (analytics widgets)

**Timeline Impact:** +10 days (MVP timeline extended)

**Documentation Updated:**
- [x] PRD v1.5 (Analytics section added)
- [x] ROADMAP v1.3 (MVP timeline adjusted)
- [x] analytics_requirements.md (NEW FILE)
- [x] modules_status.md (new module)

#### Related

- Decision: DEC-015 (Add Analytics to MVP)
- Requirements: analytics_requirements.md
- Stakeholder email: CEO request 2025-10-28

---

## 📊 CHANGE STATISTICS

**Total Changes:** [X]

**By Type:**
- Feature Add: [X]
- Feature Remove: [X]
- Feature Change: [X]
- Scope Change: [X]
- Tech Change: [X]
- Process Change: [X]

**By Impact:**
- Critical: [X]
- High: [X]
- Medium: [X]
- Low: [X]

**Timeline Impact:**
- Delays: [X] changes (+Y days total)
- Savings: [X] changes (-Y days total)
- Net: [+/- Y days]

---

## 💡 CHANGE MANAGEMENT TIPS

**When to Log a Change:**
- ✅ Feature added/removed/modified
- ✅ Scope changes (timeline, budget, team)
- ✅ Technology switches
- ✅ Major process changes
- ❌ Bug fixes (use git commits)
- ❌ Minor tweaks (use git commits)

**Good Change Entries:**
- State WHAT changed clearly
- Explain WHY (context matters)
- Document IMPACT (affected areas)
- Update relevant docs
- Link to decisions/discussions

**After Logging Change:**
1. Update affected documentation
2. Log decision (if applicable)
3. Communicate to team
4. Update project tracking

---

**Keep This Log Current!** It's invaluable for retrospectives and audits. 📝

