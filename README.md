# Свой Круг (Own Circle)

> **Россия's first premium women's loyalty ecosystem**
>
> Unified loyalty program connecting premium businesses in Moscow through cross-promotion chains, bonuses, and exclusive community events.

## 🎯 What is Свой Круг?

Свой Круг is a premium loyalty ecosystem that solves the problem of fragmented loyalty programs for affluent women in Moscow. Instead of managing 10+ individual loyalty cards with minimal benefits, members get:

- **Unified Bonuses:** 5-10% cashback across all partner businesses (beauty, wellness, gastronomy, medicine)
- **Smart Cross-Promotion:** Purchase at salon A → automatic 500₽ coupon at restaurant B
- **Status Tiers:** Insider → VIP → Elite → Inner Circle (based on total spend)
- **Exclusive Events:** Masterclasses, tastings, wellness workshops for VIP+ members

**Target Users:** Women 30-50, 80K+ monthly income, premium service consumers
**Initial Partners:** 5 businesses (Skinerica, Лисичкино, Стим Центр, Миндаль, Миллениум)
**MVP Launch:** 12 weeks (6 sprints), target 200+ members

## 🚀 Quick Start

### For Developers

**Prerequisites:**
- Python 3.13+
- Node.js 20+ (for mobile development)
- Docker & Docker Compose
- PostgreSQL 16.11, Redis 8.2

**Setup:**
```bash
# 1. Clone repository
git clone https://github.com/AlgizPure/OwnCircule.git
cd OwnCircule

# 2. Set up backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head

# 3. Set up mobile app
cd ../mobile
npm install
npx pod-install  # iOS only

# 4. Run development servers
docker-compose up -d  # Start PostgreSQL, Redis, ClickHouse
cd backend && uvicorn main:app --reload  # Backend on :8000
cd mobile && npm start  # Mobile on :8081
```

**Documentation:**
- 📚 Project Docs: `docs/core/`
- 📋 Module Requirements: `docs/requirements/`
- 📊 Progress Tracking: `docs/progress/`
- 💭 Context: `.context/state.md`

## 📁 Project Structure

```
OwnCircule/
├── docs/                       # 📚 Project Documentation
│   ├── core/                   # Core documents (6 files)
│   │   ├── 00_PROJECT_ESSENCE.md  # Vision, problem, solution
│   │   ├── 01_PRD.md              # Product requirements
│   │   ├── 02_ROADMAP.md          # 12-week MVP roadmap
│   │   ├── 03_TECH_STACK.md       # Verified tech stack
│   │   ├── 04_ARCHITECTURE.md     # System design
│   │   └── 05_GLOSSARY.md         # Project terminology
│   │
│   ├── requirements/           # Module Requirements (15 files)
│   │   ├── module-01-mobile-app.md       # 68 functions
│   │   ├── module-02-loyalty-system.md   # 45 functions
│   │   ├── module-03-transactions.md     # 12 functions
│   │   ├── module-04-events.md           # 28 functions
│   │   ├── module-05-cross-promo.md      # 22 functions (CORE)
│   │   ├── module-08-crm-integrations.md # 20 functions
│   │   ├── module-13-security.md         # 8 functions (152-ФЗ)
│   │   └── ...                           # 8 more modules
│   │
│   └── progress/               # Progress Tracking (3 files)
│       ├── modules_status.md   # Module development status
│       ├── sprint_current.md   # Current sprint details
│       └── backlog.md          # Product backlog (325 functions)
│
├── .context/                   # 💭 Project Context (4 files)
│   ├── state.md                # Current state, priorities, blockers
│   ├── decisions.md            # 15 architectural decisions
│   ├── insights.md             # 18 key insights
│   └── changes_log.md          # Complete change timeline
│
├── .upmt/                      # UPMT Metadata
│   └── metadata.yaml           # Project metadata (auto-filled)
│
├── backend/                    # 🐍 Backend (FastAPI + Python 3.13)
│   ├── app/                    # Application code
│   │   ├── modules/            # 15 domain modules
│   │   │   ├── loyalty/        # Module 2: Bonuses, status tiers
│   │   │   ├── transactions/   # Module 3: Transaction history
│   │   │   ├── cross_promo/    # Module 5: Cross-promo chains
│   │   │   ├── crm/            # Module 8: CRM integrations
│   │   │   └── ...
│   │   ├── core/               # Shared utilities
│   │   └── main.py             # FastAPI application
│   ├── alembic/                # Database migrations
│   ├── tests/                  # pytest tests
│   └── requirements.txt        # Python dependencies
│
├── mobile/                     # 📱 Mobile App (React Native 0.81)
│   ├── src/
│   │   ├── screens/            # App screens
│   │   ├── components/         # Reusable components
│   │   ├── store/              # Redux Toolkit + RTK Query
│   │   ├── navigation/         # React Navigation 6
│   │   └── utils/
│   ├── ios/                    # iOS native code
│   ├── android/                # Android native code
│   └── package.json
│
├── .cursorrules                # AI development guidelines
├── docker-compose.yml          # Local development stack
└── README.md                   # This file
```

## 🛠️ Tech Stack

**Verified for November 2025 compatibility** (PHASE 3 complete)

### Backend
- **Runtime:** Python 3.13 (latest stable)
- **Framework:** FastAPI 0.121.2 (async REST API)
- **Database (OLTP):** PostgreSQL 16.11 (transactions, users, bonuses)
- **Database (OLAP):** ClickHouse 25.8 LTS (analytics, RFM, Win-Win matrix)
- **Cache/Queue:** Redis 8.2 (caching, Celery task queue)
- **ORM:** SQLAlchemy 2.0.44 (async)
- **Task Queue:** Celery 5.4.x + Celery Beat (scheduled tasks)
- **Migrations:** Alembic

### Mobile (Cross-Platform)
- **Framework:** React Native 0.81
- **Language:** TypeScript 5.7 (strict mode)
- **State Management:** Redux Toolkit 2.10.1 + RTK Query
- **Navigation:** React Navigation 6
- **UI Components:** Custom (premium design)
- **Animations:** Lottie + React Native Reanimated
- **QR Scanning:** react-native-vision-camera

### Infrastructure & DevOps
- **Cloud Provider:** Yandex Cloud (ru-central1 region) - 152-ФЗ compliant
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus 3.3.0 + Grafana 11.5.0 + Loki 3.3.0
- **Error Tracking:** Sentry
- **Logging:** Structured logging (JSON format)

### Security & Compliance
- **Encryption:** AES-256 (Fernet) for sensitive data
- **Authentication:** JWT (RS256) with access + refresh tokens
- **Authorization:** RBAC (Role-Based Access Control)
- **Compliance:** 152-ФЗ (Russian personal data law), врачебная тайна (medical confidentiality)

### External Integrations
- **CRM Systems:** YCLIENTS, Iiko, 1С, AMO CRM, Renovatio, CSV fallback
- **Notifications:** Firebase Cloud Messaging (push), SendGrid (email), SMS.ru (SMS)
- **Payment Gateway:** (TBD - for v1.5)

See [`docs/core/03_TECH_STACK.md`](docs/core/03_TECH_STACK.md) for detailed rationale and version history.

## 📖 Documentation

### Core Documents
- [**Project Essence**](docs/core/00_PROJECT_ESSENCE.md) - Vision, problem statement, solution pillars, success criteria
- [**PRD (Product Requirements)**](docs/core/01_PRD.md) - Complete product requirements for all 15 modules
- [**Roadmap**](docs/core/02_ROADMAP.md) - 12-week MVP roadmap (6 sprints) + v1.5/v2.0 plans
- [**Tech Stack**](docs/core/03_TECH_STACK.md) - Verified technology stack with rationales
- [**Architecture**](docs/core/04_ARCHITECTURE.md) - System design, database schema, API structure
- [**Glossary**](docs/core/05_GLOSSARY.md) - Project-specific terminology

### Module Requirements (15 Modules, 325 Functions)
All detailed requirements are in [`docs/requirements/`](docs/requirements/):

**P0 (MVP Critical):**
- Module 1: [Mobile App](docs/requirements/module-01-mobile-app.md) (68 functions) - React Native frontend
- Module 2: [Loyalty System](docs/requirements/module-02-loyalty-system.md) (45 functions) - Bonuses, status tiers, coupons
- Module 3: [Transactions & History](docs/requirements/module-03-transactions.md) (12 functions) - Purchase tracking
- Module 4: [Events Hub & Management](docs/requirements/module-04-events.md) (28 functions) - Community events
- Module 5: [Cross-Promotion & Chains](docs/requirements/module-05-cross-promo.md) (22 functions) - **CORE VALUE PROP**
- Module 8: [CRM Integrations](docs/requirements/module-08-crm-integrations.md) (20 functions) - YCLIENTS, Iiko, 1С, etc.
- Module 12: [Notifications](docs/requirements/module-12-notifications.md) (18 functions) - Push, email, SMS
- Module 13: [Security & Compliance](docs/requirements/module-13-security.md) (8 functions) - 152-ФЗ, врачебная тайна

**P1 (Important - v1.5):**
- Module 6: [Offer Constructor](docs/requirements/module-06-offer-constructor.md) (18 functions)
- Module 7: [Business Analytics](docs/requirements/module-07-analytics.md) (25 functions)
- Module 9: [Business Admin Panel](docs/requirements/module-09-business-admin.md) (22 functions)
- Module 10: [Superadmin Panel](docs/requirements/module-10-superadmin.md) (18 functions)
- Module 11: [Referral Program](docs/requirements/module-11-referral.md) (10 functions)
- Module 15: [Events Budget System](docs/requirements/module-15-events-budget.md) (4 functions)

**P2 (Nice-to-have - v2.0):**
- Module 14: [Gamification & Badges](docs/requirements/module-14-gamification.md) (7 functions)

### Progress Tracking
- [**Module Development Status**](docs/progress/modules_status.md) - Sprint-by-sprint breakdown, blockers
- [**Current Sprint**](docs/progress/sprint_current.md) - Active sprint details, daily standup format
- [**Product Backlog**](docs/progress/backlog.md) - 325 user stories prioritized across 12 months

### Context Files
- [**Project State**](.context/state.md) - Current status, priorities, blockers, next actions
- [**Architectural Decisions**](.context/decisions.md) - 15 documented decisions (AD-001 to TD-003)
- [**Key Insights**](.context/insights.md) - 18 insights from bootstrap process
- [**Change Log**](.context/changes_log.md) - Complete timeline of project evolution

## 👥 Team

**Current Status:** Pre-Development (team assembly in progress)

**Required Roles:**
- **Product Manager** (1) - Owns roadmap, prioritization, partner relations
- **Backend Developers** (2-3) - Python/FastAPI, PostgreSQL, ClickHouse, CRM integrations
- **Mobile Developer** (1-2) - React Native, TypeScript, Redux Toolkit
- **DevOps Engineer** (1) - Yandex Cloud, Docker, CI/CD, monitoring
- **QA Engineer** (1) - Manual + automated testing (pytest, Jest)

**Timeline:** Sprint 1 starts when core team (PM + 2 backend + 1 mobile) is assembled

## 📊 Project Metrics

### MVP Success Criteria (Week 12)
- [ ] 200+ registered members
- [ ] 5 partner businesses fully integrated
- [ ] 2+ CRM integrations live (YCLIENTS + Iiko minimum)
- [ ] QR wallet functional on iOS + Android
- [ ] Cross-promo chains operational (A → B triggers working)
- [ ] 0 critical bugs in production
- [ ] <2s app load time, <100ms API response (p95)

### 6-Month Targets (Post-MVP)
- [ ] 500+ active members
- [ ] 8 partner businesses
- [ ] **25% cross-purchase rate** (2+ categories in 60 days) - **North Star Metric**
- [ ] <15% monthly churn
- [ ] 3M₽ total ecosystem GMV (Gross Merchandise Value)
- [ ] NPS >50

## 🚀 Development Roadmap

### Phase 1: Foundation (Weeks 1-2) - Sprint 1
- Backend API framework (FastAPI + PostgreSQL)
- JWT authentication + SMS OTP
- Mobile app shell (React Native)
- Security foundation (AES-256 encryption, RBAC)

### Phase 2: Core Features (Weeks 3-6) - Sprints 2-3
- User onboarding + profile management
- Bonus system (accrual, redemption, balance)
- Status tiers (Insider/VIP/Elite)
- First CRM integration (YCLIENTS)
- Simple cross-promo chains (A → B)

### Phase 3: Integration & Polish (Weeks 7-10) - Sprints 4-5
- Coupons & promotions
- Event management + registration
- Second CRM integration (Iiko)
- Win-Win analytics dashboard
- Push notifications

### Phase 4: Testing & Launch (Weeks 11-12) - Sprint 6
- Beta testing with 50 users
- Bug fixes & performance optimization
- Production deployment (Yandex Cloud)
- Marketing materials & partner onboarding

**Post-MVP (v1.5 - Months 4-6):**
- Offer constructor for businesses
- Advanced analytics (RFM, churn prediction)
- Referral program
- Events budget system (2% of transactions → shared fund)

**Future (v2.0 - Months 7-12):**
- Gamification & badges
- Expansion to other cities (St. Petersburg, Kazan)

## 🤝 Contributing

**Current Status:** Closed (core team only during MVP development)

Once MVP launches, we'll open up contributions. For now, please contact the project maintainer if you're interested in joining the team.

## 📄 License

**Proprietary** - All rights reserved. This project is not open source.

© 2025 Свой Круг (Own Circle). Contact: [To be added]

---

## 📞 Contact & Support

- **Project Manager:** [To be added]
- **Technical Lead:** [To be added]
- **GitHub Issues:** For team members only
- **Documentation:** See [`docs/`](docs/) folder

---

**Project Status:** 🟢 Documentation Complete - Ready for Development

**Bootstrap Completed:** 2025-11-17 (UPMT v1.3)

**Next Milestone:** Sprint 1 Kickoff (Team Assembly Required)

---

*Created with [Universal Project Management Template (UPMT)](https://github.com/AlgizPure/project-management-template)*

