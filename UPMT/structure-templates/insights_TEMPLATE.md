# PROJECT INSIGHTS & LEARNINGS

**Purpose:** Capture learnings, patterns, and wisdom gained during development  
**Review:** Weekly to extract patterns and improve processes

---

## 💡 INSIGHT TEMPLATE
## [Date]: [Insight Title]

**Category:** Technical / Process / Team / Product  
**Trigger:** [What caused this learning?]

**What Happened:**
[Describe the situation]

**What We Learned:**
[The key insight or learning]

**Why It Matters:**
[Impact and importance]

**Action Items:**
- [ ] [How to apply this learning]
- [ ] [Process changes to make]

**Related:**
- Decisions: DEC-XXX
- Documentation: [Links]

---

## 📚 INSIGHTS COLLECTION

### 🔧 TECHNICAL INSIGHTS

#### 2025-11-08: Drizzle ORM Migration Gotcha

**Category:** Technical  
**Trigger:** Production migration failed unexpectedly

**What Happened:**

Deployed new migration to production. Migration syntax worked fine in 
development (PostgreSQL 15) but failed in production (PostgreSQL 16).
Issue: Used column name as keyword in newer version.

Error: 
```
syntax error at or near "user"
```

Cause:
Column named 'user' conflicted with reserved keyword in PG16

**What We Learned:**
- Always test migrations against same PostgreSQL version as production
- Use migration dry-run feature before production
- Avoid reserved keywords in column names
- Check PostgreSQL version compatibility in CI

**Why It Matters:**
Production downtime for 15 minutes while rolling back and fixing.

**Action Items:**
- [x] Add PG16 to CI pipeline
- [x] Create pre-deploy migration checklist
- [x] Document reserved keywords to avoid
- [ ] Set up staging environment with same PG version

**Related:**
- Decision: DEC-001 (PostgreSQL choice)
- Documentation: `/docs/MIGRATIONS.md`

---

#### 2025-11-06: Redis Caching Dramatically Improved Performance

**Category:** Technical  
**Trigger:** API response times were slow (800ms average)

**What Happened:**

Dashboard endpoint was querying database for team tasks on every request.
With 10+ users, database was bottleneck.

Before Redis:
- Dashboard load: 800ms average
- Database queries: 5-8 per request
- CPU: 60% usage

After Redis (15min TTL):
- Dashboard load: 120ms average (6.6x faster!)
- Database queries: 0-1 per request (cache hit 95%)
- CPU: 20% usage

**What We Learned:**
- Caching is critical for read-heavy endpoints
- 15min TTL good balance (freshness vs performance)
- Cache invalidation is key (clear on updates)
- Monitor cache hit rates

**Why It Matters:**
User experience dramatically improved. App feels fast now.

**Action Items:**
- [x] Add Redis caching to other hot paths
- [x] Set up cache monitoring (hit rates)
- [x] Document caching strategy
- [ ] Consider cache warming for common queries

**Related:**
- Decision: DEC-007 (Add Redis)
- Performance: `/docs/PERFORMANCE.md`

---

### 📱 PRODUCT INSIGHTS

#### 2025-11-05: Users Don't Read Onboarding

**Category:** Product / UX  
**Trigger:** User testing session revealed low onboarding completion

**What Happened:**

Built beautiful multi-step tutorial (5 screens).
Analytics showed:
- 100% see screen 1
- 40% complete screen 2
- 15% complete screen 3
- 3% finish tutorial

User interviews revealed:
- "Too long, I want to start"
- "I'll figure it out myself"
- "Skipped and forgot to come back"

**What We Learned:**

**Pattern:** Learning by doing > guided tours
**Reality:** Nobody watches tutorial videos

**Better Approach:**
- Progressive disclosure (show features when needed)
- Contextual help (tooltips on hover, not upfront)
- "Empty states" with clear CTAs
- Let users fail fast and recover

**Why It Matters:**
Onboarding is critical for retention. Bad onboarding = churn.

**Action Items:**
- [x] Removed multi-step tutorial
- [x] Added contextual tooltips (show on first use)
- [x] Designed empty states with clear actions
- [ ] A/B test: old vs new onboarding
- [ ] Track completion rates

**Quotes from Users:**
> "I just want to create a task and see what happens"
> "Too much text, I'm overwhelmed"
> "Can I skip this and come back later?"

**Related:**
- PRD: User onboarding section
- Design: Figma onboarding flow v2

---

### 👥 TEAM INSIGHTS

#### 2025-11-03: Pair Programming Caught Critical Bug

**Category:** Team / Process  
**Trigger:** Scheduled pair programming session

**What Happened:**

Developer A was implementing authentication.
Developer B joined for pair programming session.

While reviewing code together, Developer B noticed:
- Password reset tokens weren't expiring
- Security vulnerability: tokens valid forever

Developer A missed this during implementation.
Code review might have caught it, but pairing caught it BEFORE commit.

**What We Learned:**
**Two sets of eyes:** Catch bugs earlier (before PR)
**Real-time:** Faster than async code review
**Knowledge sharing:** Both developers learned

**Why It Matters:**
Critical security bug caught before reaching production.
Could have been exploited if shipped.

**Action Items:**
- [x] Schedule weekly pair programming sessions
- [x] Pair on security-critical features
- [ ] Create pairing rotation schedule
- [ ] Document pairing best practices

**Best Practices We Discovered:**
- 25min focused sessions (Pomodoro)
- Switch driver/navigator every session
- Both think out loud (verbalize reasoning)
- No judgment zone (safe to ask "stupid" questions)

**Related:**
- Process: Team workflow documentation
- Security: Security checklist

---

### 🚀 PROCESS INSIGHTS

#### 2025-11-02: Daily Standups Were Wasting Time

**Category:** Process  
**Trigger:** Team retrospective

**What Happened:**

Daily standup meetings:
- Scheduled: 15 minutes
- Actual: 35-45 minutes
- Issues:
  - People giving too much detail
  - Discussions happening (not for standup)
  - Not everyone paying attention
  - Felt like status report to manager

**What We Learned:**
**Problem:** Standup became status meeting, not sync
**Root cause:** No structure, no time limits

**New Format (strict 15min):**
1. Round-robin (2min per person max)
2. Three questions only:
   - What I shipped yesterday
   - What I'm shipping today
   - Blockers (if any)
3. Timer visible (hard stop at 15min)
4. Deeper discussions: park for later (async or separate meeting)

**Why It Matters:**
Team time is expensive. 20min saved daily = 1.5 hours/week saved.

**Action Items:**
- [x] New standup format implemented
- [x] Added visible timer
- [x] Created "parking lot" for deeper discussions
- [ ] Retrospective in 2 weeks (is it working?)

**Related:**
- Process: Team workflows
- Retrospective notes: 2025-11-02

---

## 🎯 PATTERNS & THEMES

**Emerging Patterns:**
- Caching is always worth it for read-heavy ops
- Users prefer "learning by doing" over tutorials
- Real-time collaboration (pairing) > async (review)
- Time-boxing meetings reduces waste

**Anti-Patterns to Avoid:**
- Long onboarding flows
- Meetings without structure
- Deploying without staging environment
- Using reserved keywords in naming

---

## 💡 HOW TO USE THIS FILE

**After Each Sprint:**
1. Review what went well / poorly
2. Extract learnings
3. Document using template
4. Create action items
5. Review previous insights (were actions completed?)

**Monthly Review:**
1. Look for patterns across insights
2. Update processes/guidelines
3. Share key learnings with team
4. Archive old insights (move to `/archive/insights-YYYY-MM.md`)

---

**This file is your collective wisdom. Keep it growing!** 🧠

