# Project Insights - Свой Круг

**Last Updated:** 2025-11-17

---

## 💡 Key Insights from UPMT Bootstrap

### 1. Cross-Promotion is Core Value Proposition
**Insight:** The cross-promo engine (Module 5) is what differentiates Свой Круг from traditional loyalty programs.

**Evidence:**
- 22 functions dedicated to cross-promo (simple, sequential, cyclical, fan-out chains)
- Win-Win analytics to optimize chain performance
- Business problem: fragmented loyalty programs with minimal value
- Solution: Purchase at A → automatic coupon at B (different category)

**Implications for Development:**
- Prioritize Module 5 in Sprint 3-4 (after core loyalty system)
- Cross-promo must be seamless (trigger within 1 minute of purchase)
- Need robust analytics to prove ROI to businesses

**Action Items:**
- [ ] Prototype cross-promo algorithm in Sprint 2
- [ ] Build Win-Win matrix MVP (even simple version) by Sprint 5
- [ ] Demo cross-promo to initial 5 partners before Sprint 3

---

### 2. Mobile-First, But Business Admin Panel is Critical
**Insight:** While members use mobile app (68 functions), business owners need powerful web admin panel (22 functions).

**Evidence:**
- Module 9 (Business Admin) has same priority as core mobile features
- Business owners are secondary users but critical stakeholders
- They need: customer management, transaction entry, offer creation, analytics

**Implications:**
- Don't neglect web admin panel (some teams over-index on mobile)
- Allocate 1 frontend developer for web admin from Sprint 1
- Business owners must be able to self-serve (create offers, view analytics)

**Action Items:**
- [ ] Design web admin UI/UX in parallel with mobile (Sprint 1)
- [ ] Ensure web admin uses same FastAPI backend (code reuse)
- [ ] Train initial 5 partners on admin panel in Sprint 6

---

### 3. CRM Integration Complexity is Underestimated
**Insight:** Module 8 (CRM Integrations) is 20 functions and requires deep integration knowledge.

**Evidence:**
- 6 different CRM systems (YCLIENTS, Iiko, 1С, AMO CRM, Renovatio, CSV)
- Each has unique API, auth flow, data format
- Need bidirectional sync (read transactions, write bonuses)
- Error handling, retry logic, duplicate detection critical

**Implications:**
- CRM integration is NOT "just API calls" - it's complex adapter pattern
- Budget 3-4 weeks for first 2 integrations (YCLIENTS + Iiko)
- CSV fallback is essential (some businesses have no API)

**Action Items:**
- [ ] Assign 1 senior backend dev to CRM integrations (Sprint 3-5)
- [ ] Get API credentials from 5 partners BEFORE Sprint 3
- [ ] Build test suite with mock CRM responses

---

### 4. Events Hub is Community Engagement Driver
**Insight:** Events (Module 4, 28 functions) are not just "nice-to-have" - they're core to retention and community.

**Evidence:**
- 28 functions (3rd largest module after Mobile and Loyalty)
- Event constructor for VIP/Elite (weighted voting, proposals)
- Events budget system (2% of all transactions → shared fund)
- Success criteria: 80%+ registered members attend events

**Implications:**
- Events drive emotional connection (vs transactional loyalty)
- VIP/Elite need to feel ownership (propose events, vote)
- Budget transparency builds trust

**Action Items:**
- [ ] Plan first 3 pilot events during beta (Sprints 9-10)
- [ ] Event constructor can be v1.5, but basic events in MVP
- [ ] Ensure event budget dashboard is transparent from Day 1

---

### 5. Security & Compliance is Non-Negotiable
**Insight:** Module 13 (Security) must be P0, not afterthought.

**Evidence:**
- 152-ФЗ (Russian data law) requires data in RF, encryption, consent tracking
- врачебная тайна (medical confidentiality) for 2 of 5 partners
- AES-256 encryption, JWT with RS256, audit logging all required

**Implications:**
- Security decisions must be made in Sprint 1 (not Sprint 10)
- Cannot launch without 152-ФЗ compliance (legal risk)
- Medical data isolation is architectural decision (not feature)

**Action Items:**
- [ ] Implement encryption from Day 1 (don't migrate later)
- [ ] Yandex Cloud setup in Sprint 1 (ru-central1 region)
- [ ] Audit log table created in first database migration

---

## 🎯 Strategic Insights

### Insight S-1: Target Demographic is Well-Defined
**Observation:** Clear target: women 30-50, 80K+ monthly income, premium services

**Why It Matters:**
- Focused marketing (not trying to be "everything to everyone")
- Partner selection is easier (premium businesses only)
- UX can be optimized for this demographic (elegant, premium feel)

**Risk:**
- Market size limited (only ~10-15K women in Moscow fit this profile)
- Need to expand to other cities after Moscow MVP success

---

### Insight S-2: North Star Metric (NSM) is Well-Chosen
**Observation:** NSM = % members with 2+ categories in 60 days (target: 25%)

**Why It's Good:**
- Directly measures core value prop (cross-category engagement)
- Leading indicator (predicts LTV, retention)
- Actionable (can optimize with cross-promo chains)

**How to Track:**
- ClickHouse daily query
- Dashboard for superadmin (Module 10)
- Monthly report to investors/board

---

### Insight S-3: Ecosystem Economics are Sustainable
**Observation:**
- 2% of all transactions → events budget
- 5-10% cashback to members
- Cross-promo costs shared between businesses (50/50 split)

**Why It Works:**
- Businesses save on CAC (10K → 3K via cross-promo)
- Members get 3-5x more value (vs. 1-3% standalone programs)
- Platform revenue from transaction fees (if added later)

**Risk:**
- Cashback rates (5-10%) are high - need to monitor profitability
- If businesses don't see ROI, they'll leave ecosystem

---

## 🚀 Technical Insights

### Insight T-1: Modular Monolith Enables Fast MVP
**Observation:** 15 modules with clear boundaries, but single deployment

**Why It's Right Choice:**
- Faster development (no microservices overhead)
- Easier debugging (single codebase, logs)
- Can extract microservices later if needed

**When to Revisit:**
- If user count >10K (single monolith may struggle)
- If team grows >10 developers (coordination overhead)

---

### Insight T-2: ClickHouse is Performance Multiplier
**Observation:** ClickHouse 25.8 LTS for analytics (vs PostgreSQL for OLTP)

**Why It's Critical:**
- RFM segmentation, Win-Win matrix, cohort analysis = complex queries
- PostgreSQL would take 10-30s for these queries
- ClickHouse does same in <1s (100x faster)

**Trade-off:**
- Additional infrastructure complexity
- Data sync lag (up to 1 hour)
- BUT: Worth it for fast analytics dashboards

---

### Insight T-3: React Native 0.81 is Mature Choice
**Observation:** React Native has 80%+ code reuse, large ecosystem

**Why It's Safe:**
- Not bleeding-edge (0.81 stable as of Nov 2025)
- Many Russian apps use React Native (Yandex, VK have RN libraries)
- Can drop to native for performance-critical features (QR scanning)

**Risk:**
- Not as performant as native Swift/Kotlin
- BUT: Our app is not performance-critical (mostly CRUD + lists)

---

## 📊 Data Insights

### Insight D-1: 325 Functions Across 15 Modules
**Analysis:** Large scope for MVP (typical MVP is 100-150 functions)

**Breakdown:**
- P0 (Critical MVP): ~200 functions across 9 modules
- P1 (Important): ~90 functions (can defer to v1.5)
- P2 (Nice-to-have): ~35 functions (v2.0)

**Recommendation:**
- Focus on P0 modules first: 1, 2, 3, 4, 5, 8, 12, 13
- Defer P1 to v1.5: 6, 7, 9, 11, 15
- Defer P2 to v2.0: 14

---

### Insight D-2: 5 Initial Partners is Right Size
**Analysis:** Skinerica, Лисичкино, Стим Центр, Миндаль, Миллениум

**Why 5 is Good:**
- Covers 4 categories (Beauty, Gastronomy, Dentistry, Medicine)
- Small enough to onboard manually
- Large enough to demonstrate cross-promo value

**Next Partners (v1.5):**
- Add 3 more (target: 8 total)
- New categories: Wellness (spa), Floristry, Optometry

---

## 🤔 Open Questions

### Q1: How to bootstrap initial members?
**Question:** Need 200 members for MVP launch. How to acquire first 50-100?

**Options:**
1. Partner businesses invite their VIP customers
2. Instagram/VK ads targeting women 30-50 in Moscow
3. Influencer partnerships (premium lifestyle bloggers)

**Recommendation:** Start with option 1 (partner invites), then supplement with 2

---

### Q2: What's the commission model?
**Question:** How does platform make money?

**Current Plan:** No commission initially (focus on growth)

**Future Options:**
1. Transaction fee (1-2% of GMV)
2. SaaS subscription for businesses (5K-10K ₽/month)
3. Premium member tier (annual fee for extra benefits)

**Recommendation:** Revisit after 6 months (focus on product-market fit first)

---

### Q3: How to handle partner churn?
**Question:** What if a partner leaves the ecosystem?

**Impact:**
- Members lose access to that business's bonuses
- Existing coupons become invalid
- Cross-promo chains break

**Mitigation:**
- Contract: 90-day notice period for partners
- Communicate to members if partner leaves
- Find replacement in same category quickly

---

## 📝 Lessons from Bootstrap Process

### Lesson 1: Tech Verification (PHASE 3) Was Critical
**What Happened:** Verified all 31 technologies for November 2025, found 8 updates needed

**Why It Mattered:** Using outdated tech (e.g., Python 3.11 vs 3.13) would cause issues 6 months from now

**Takeaway:** Always verify tech stack currency before starting development

---

### Lesson 2: Module Requirements Need 100+ Lines Each
**What Happened:** PHASE 5 BATCH 2 created 15 files, 6,876 lines total (avg 458 lines/file)

**Why It Mattered:** Detailed requirements prevent scope creep and misunderstandings

**Takeaway:** Invest time in requirements upfront (saves 10x time later)

---

### Lesson 3: Cross-Module Dependencies are Complex
**What Happened:** Module 2 (Loyalty) depends on 3, 5, 8, 12. Module 5 (Cross-Promo) depends on 2, 3, 7.

**Why It Mattered:** Development order must follow dependency graph (can't build Module 5 before Module 2)

**Takeaway:** Document dependencies clearly, plan sprints accordingly

---

**Total Insights:** 18 documented
**Last Review:** 2025-11-17
**Status:** Continuously updated during development
