# Свой Круг - Development Roadmap

**Created:** 2025-11-17
**Version:** 1.0
**Status:** Active

---

## 📅 Development Phases

### Phase 1: Foundation (Weeks 1-4)
**Duration:** 4 weeks (Sprints 1-2)
**Goal:** Establish core infrastructure and authentication
**Deliverables:**
- Backend foundation (FastAPI + PostgreSQL + Redis)
- Mobile app shell (React Native 0.81 + Redux Toolkit)
- Authentication system (SMS OTP, JWT tokens)
- User profile management
- Basic admin panel structure
- CI/CD pipeline (GitHub Actions)
- Development environment setup

**Critical Modules:**
- Module 1.1: Authentication & Onboarding (12 functions)
- Module 1.4: User Profile (12 functions)
- Backend: User management, auth APIs
- Infrastructure: Docker setup, cloud deployment

**Success Criteria:**
- [ ] Users can register and log in via SMS
- [ ] User profiles can be created and updated
- [ ] Basic API endpoints operational
- [ ] CI/CD pipeline deploys to staging

---

### Phase 2: Core Loyalty Features (Weeks 5-8)
**Duration:** 4 weeks (Sprints 3-4)
**Goal:** Implement loyalty system and transaction tracking
**Deliverables:**
- Bonus system (accrual, redemption, balance)
- Status system (Insider/VIP/Elite/Inner Circle)
- Transaction history and tracking
- QR code wallet (scanning, generation)
- Business catalog with filtering
- First CRM integration (YCLIENTS for Миндаль salon)

**Critical Modules:**
- Module 2.1: Bonus System (15 functions)
- Module 2.2: Status System (12 functions)
- Module 3: Transactions & History (12 functions)
- Module 1.3: QR Wallet (8 functions)
- Module 8.1: CRM Connectors (partial - YCLIENTS)

**Success Criteria:**
- [ ] Users earn bonuses on purchases (5-10% by status)
- [ ] Status automatically calculated from spend + categories
- [ ] QR codes work for bonus accrual/redemption
- [ ] YCLIENTS integration syncs transactions
- [ ] Transaction history displays correctly

---

### Phase 3: Integration & Cross-Promo (Weeks 9-10)
**Duration:** 2 weeks (Sprint 5)
**Goal:** Connect partner businesses and enable cross-promotion
**Deliverables:**
- Second CRM integration (Iiko for Лисичкино gastromarket)
- Simple cross-promo chains (A → B)
- Coupon system (distribution, redemption)
- Basic business analytics dashboard
- Event Hub with registration

**Critical Modules:**
- Module 5.1: Simple Cross-Promo Chains (8 functions)
- Module 2.3: Coupons & Promo (18 functions)
- Module 8.1: CRM Connectors (Iiko)
- Module 4.1: Event Management (10 functions)
- Module 7.1: Business Analytics (8 functions)

**Success Criteria:**
- [ ] 2 CRM integrations operational (YCLIENTS + Iiko)
- [ ] Cross-promo chains trigger coupons automatically
- [ ] Users can redeem coupons at partner businesses
- [ ] Events visible in app with registration
- [ ] Business owners see basic analytics

---

### Phase 4: Testing & Launch (Weeks 11-12)
**Duration:** 2 weeks (Sprint 6)
**Goal:** Beta test, fix bugs, production launch
**Deliverables:**
- Beta testing with 50 participants
- Bug fixes and performance optimization
- Push notifications system
- SMS/Email notifications
- Production deployment
- Marketing materials and onboarding

**Critical Modules:**
- Module 12: Notifications & Communications (18 functions)
- Module 13: Security & Compliance (8 functions)
- All previous modules: testing, optimization

**Success Criteria:**
- [ ] 50 beta testers complete onboarding
- [ ] 0 critical bugs in production
- [ ] <2s app load time, <100ms API response (p95)
- [ ] 200+ registrations in first 2 weeks post-launch
- [ ] 5 partner businesses confirmed and integrated

---

## 🗓️ Module Implementation Order

### Critical Path (MVP Required)
1. **Authentication & User Management** (Week 1-2)
2. **Loyalty System** (Week 3-4)
3. **Transactions & QR Wallet** (Week 5-6)
4. **CRM Integrations** (Week 7-8)
5. **Cross-Promo Chains** (Week 9-10)
6. **Notifications & Testing** (Week 11-12)

### Important (Post-MVP, v1.5 - Months 4-6)
7. **Referral Program** (Module 11)
8. **Advanced Events** (Module 4.2-4.3)
9. **Business Admin Panel** (Module 9)
10. **Win-Win Analytics** (Module 5.4)
11. **Offer Constructor** (Module 6)

### Nice-to-Have (v2.0 - Months 7-12)
12. **Event Constructor** (Module 1.6)
13. **Advanced Analytics** (Module 7.2-7.5)
14. **Gamification & Badges** (Module 14)
15. **Sequential/Cyclical Chains** (Module 5.2-5.3)

---

## 📊 Progress Tracking

**Current Status:** PHASE 5 - Documentation Generation

| Phase | Status | Progress | ETA |
|-------|--------|----------|-----|
| PHASE 1: Analysis | ✅ Complete | 100% | 2025-11-17 |
| PHASE 2: Interview | ✅ Complete | 100% | 2025-11-17 |
| PHASE 3: Tech Verification | ✅ Complete | 100% | 2025-11-17 |
| PHASE 4: Synthesis | ✅ Complete | 100% | 2025-11-17 |
| PHASE 5: Documentation | 🔄 In Progress | 40% | 2025-11-17 |
| PHASE 5.5: Design System | ⏳ Pending | 0% | TBD |
| PHASE 6: Setup Instructions | ⏳ Pending | 0% | TBD |
| PHASE 7: Validation | ⏳ Pending | 0% | TBD |
| PHASE 8: Final Report | ⏳ Pending | 0% | TBD |

---

## 🎯 Milestones

### M1: Infrastructure Ready (Week 4)
- Backend APIs operational
- Mobile app shell deployed
- Authentication working
- CI/CD pipeline live

### M2: Loyalty System Live (Week 8)
- Bonuses + status system functional
- QR wallet operational
- 2 CRM integrations complete
- First transactions tracked

### M3: Cross-Promo Active (Week 10)
- Cross-promotion chains working
- Coupon distribution automated
- Event Hub with registrations
- Business analytics dashboard

### M4: Production Launch (Week 12)
- Beta testing complete (50 users)
- All critical bugs fixed
- 200+ registrations achieved
- 5 partner businesses live

---

## ⚠️ Risks & Mitigation

### Technical Risks
1. **CRM Integration Complexity**
   - Risk: YCLIENTS/Iiko APIs may have undocumented limitations
   - Mitigation: Start integration testing in Sprint 3, build CSV fallback

2. **Performance at Scale**
   - Risk: Real-time bonus calculation may slow down at 1000+ transactions/day
   - Mitigation: Implement Redis caching, ClickHouse for analytics, load testing

3. **Mobile App Store Approval**
   - Risk: iOS/Android approval may take 1-2 weeks, delaying launch
   - Mitigation: Submit for review in Sprint 5, have TestFlight ready

### Business Risks
1. **Partner Onboarding Delays**
   - Risk: Businesses may delay providing CRM access
   - Mitigation: Sign agreements early, have manual CSV upload as backup

2. **User Adoption**
   - Risk: Target 200 registrations may not be met
   - Mitigation: Pre-launch marketing, partner promotion, referral incentives

---

## 🔄 Related Documentation

- [Project Essence](./00_PROJECT_ESSENCE.md) - Vision and problem statement
- [PRD](./01_PRD.md) - Product requirements
- [Tech Stack](./03_TECH_STACK.md) - Technology choices
- [Architecture](./04_ARCHITECTURE.md) - System design
- [Module Requirements](../requirements/) - Detailed module specs

---

**Last Updated:** 2025-11-17
**Owner:** Product Team
**Status:** Active
