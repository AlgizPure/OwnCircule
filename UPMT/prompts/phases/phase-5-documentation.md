# PHASE 5: DOCUMENTATION GENERATION

**Время выполнения:** 2-4 часа (автономно)

**Назначение:** Генерация ВСЕЙ проектной документации

**⚠️ САМАЯ БОЛЬШАЯ ФАЗА - КРИТИЧНО ВАЖНА**

---

## 📖 КОНТЕКСТ ПЕРЕД PHASE 5

**⚠️ ОБЯЗАТЕЛЬНО ПРОЧИТАЙ:**

**⚠️ КРИТИЧНО: Обработка больших файлов**

**Используй `safe_read_file()` из адаптера для автоматической обработки больших файлов.**

**Алгоритм:**
1. Для каждого файла вызывай `safe_read_file(file_path)`
2. Если файл большой (>256KB или >25000 токенов) - функция автоматически прочитает по частям
3. Объедини все части перед анализом

**Файлы для чтения:**
- `synthesized-project-data.md` → `safe_read_file("synthesized-project-data.md")`
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md` → `safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")` (может быть очень большим)
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md` → `safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")`
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml` → `safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")`

**⚠️ ВАЖНО:** 
- НЕ ПРОПУСКАЙ файлы из-за размера
- Функция автоматически обработает большие файлы
- Детали алгоритма см. в `cli-adapter.md` / `web-adapter.md`

---

## 📋 ТРЕБОВАНИЯ К QUALITY STANDARDS

### ⚠️ КРИТИЧНО: Каждый requirements file ДОЛЖЕН быть ДЕТАЛЬНЫМ!

**Минимальные требования:**
- ✅ Минимум **100 строк** на файл (для модуля с 4+ функциями)
- ✅ Детальные **user stories** для КАЖДОЙ функции (формат: As a... I want... So that...)
- ✅ **Acceptance criteria** в формате Given/When/Then (минимум 2-3 на функцию)
- ✅ **Technical requirements** (API endpoints, database, services)
- ✅ **UI behavior** описание (layout, interactions, states)
- ✅ **Error handling** scenarios
- ✅ **Dependencies** список

**❌ ЗАПРЕЩЕНО создавать файлы-заглушки:**
- ❌ Файлы с текстом "See extracted_features.md" или "For detailed acceptance criteria, see..."
- ❌ Ссылки вместо полного контента
- ❌ Файлы короче 50 строк
- ❌ Только headers без деталей

**⚡ ПРАВИЛО:** Если файл короче 50 строк → это ОШИБКА! Переделай с полным контентом.

---

## 📝 REQUIREMENTS FILE TEMPLATE

**Используй этот формат для КАЖДОГО requirements file:**

```markdown
# [Module Name] Requirements

**Module ID:** Module X
**Total Functions:** Y
**Priority:** CRITICAL/IMPORTANT/NICE-TO-HAVE
**Status:** Not Started
**Dependencies:** [List module dependencies]

---

## Overview

[2-3 paragraphs describing module purpose, scope, and value proposition]

**Key Capabilities:**
- [Capability 1 - what this module enables]
- [Capability 2]
- [Capability 3]

**Integration Points:**
- [Other modules this integrates with]

---

## Function X.1: [Function Name]

### User Story
**As a** [specific user type/role]  
**I want to** [specific action/capability]  
**So that** [clear business value/benefit]

### Acceptance Criteria

**Scenario 1: [Primary happy path name]**
- **Given** [initial context/preconditions]
- **When** [user action/system trigger]
- **Then** [expected outcome/behavior]
- **And** [additional verification points]

**Scenario 2: [Alternative/edge case]**
- **Given** [different context]
- **When** [action]
- **Then** [expected behavior]

**Scenario 3: [Error handling case]**
- **Given** [error condition]
- **When** [action that triggers error]
- **Then** [proper error handling behavior]

### Technical Requirements

**Frontend:**
- Component: [Component name, e.g., `ProjectDashboard.tsx`]
- Location: [File path, e.g., `app/dashboard/page.tsx`]
- State management: [Zustand store/actions needed]
- UI Framework: [shadcn/ui components or custom]

**Backend:**
- API Endpoint: [`METHOD /api/path`]
- Database: [Tables/entities involved]
- Service Layer: [Service functions needed]
- External APIs: [If any third-party integrations]

**Authentication/Authorization:**
- Required: [Yes/No]
- Permissions: [Specific permissions/roles needed]

### API Specification (if applicable)

**Endpoint:** `[METHOD] /api/resource/path`

**Request:**
```typescript
interface RequestBody {
  field1: string;
  field2: number;
  // ... other fields
}
```

**Response (Success 200):**
```typescript
interface ResponseBody {
  success: true;
  data: {
    // response structure
  };
}
```

**Response (Error 4xx/5xx):**
```typescript
interface ErrorResponse {
  success: false;
  error: {
    code: string;
    message: string;
  };
}
```

**Status Codes:**
- 200: Success
- 400: Bad request (validation error)
- 401: Unauthorized
- 403: Forbidden
- 404: Resource not found
- 500: Internal server error

### UI Behavior

**Layout:**
- [Describe screen/page layout]
- [Component placement and hierarchy]

**User Interactions:**
1. [What happens when user does X]
2. [What happens when user does Y]
3. [Form submissions, button clicks, etc.]

**UI States:**
- **Loading:** [How loading state is displayed]
- **Success:** [Success feedback to user]
- **Error:** [Error state UI and messaging]
- **Empty:** [Empty state when no data]

**Responsive Behavior:**
- [Mobile/tablet/desktop considerations]

### Error Handling

**Validation Errors:**
- [Invalid input scenario 1] → User sees: "[Error message]"
- [Invalid input scenario 2] → User sees: "[Error message]"

**System Errors:**
- [Network error] → User sees: "[Error message]" + [Retry mechanism]
- [API failure] → User sees: "[Error message]" + [Fallback behavior]

**Recovery:**
- [How user can recover from errors]

### Edge Cases

- [Edge case 1: unusual but valid scenario] → [Expected behavior]
- [Edge case 2] → [Expected behavior]
- [Edge case 3] → [Expected behavior]

### Dependencies

**Requires (must be implemented first):**
- Module X: [Specific functionality needed]
- Service Y: [Specific service/API]

**Blocks (other features waiting for this):**
- Function Z.1: [Why it needs this function]

**External Dependencies:**
- [Third-party services, if any]

### Testing Considerations

**Unit Tests:**
- [Test case 1: what to unit test]
- [Test case 2]

**Integration Tests:**
- [Integration scenario 1: testing multiple components together]
- [Integration scenario 2]

**E2E Tests:**
- [User flow 1: complete user journey]
- [User flow 2]

---

## Function X.2: [Next Function Name]

[Repeat exact same detailed format for EVERY function in the module]

---

[Continue for ALL functions...]

---

## Module-Level Requirements

### Performance Requirements
- [Metric 1: e.g., Page load time < 2s]
- [Metric 2: e.g., API response time < 500ms]
- [Metric 3: e.g., Concurrent users supported]

### Security Requirements
- [Security consideration 1]
- [Security consideration 2]
- [Data protection measures]

### Accessibility Requirements
- [WCAG 2.1 Level AA compliance]
- [Keyboard navigation support]
- [Screen reader compatibility]

### Browser/Platform Support
- [Chrome/Edge 111+, Firefox 128+, Safari 16.4+]
- [Mobile: iOS 16+, Android 12+]

---

## Implementation Notes

**Recommended Implementation Order:**
1. Function X.1: [Name] (foundation - implement first)
2. Function X.2: [Name] (builds on X.1)
3. Function X.3: [Name] (dependent on X.1 + X.2)
4. Function X.4: [Name] (final integration)

**Estimated Effort:**
- Function X.1: [8-12 hours / 5-8 story points]
- Function X.2: [4-6 hours / 3-5 story points]
- Function X.3: [6-8 hours / 5-8 story points]
- Function X.4: [4-6 hours / 3-5 story points]
- **Total Module Estimate:** [22-32 hours / 16-26 story points]

**Technical Risks & Mitigation:**
- **Risk 1:** [Description of potential technical challenge]  
  **Mitigation:** [How to address this risk]
- **Risk 2:** [Description]  
  **Mitigation:** [Approach]

**Dependencies on External Factors:**
- [External API availability, third-party service limitations, etc.]

---

## Related Documentation

- [Architecture Overview](../core/04_ARCHITECTURE.md)
- [Backend Documentation](../backend/00_BACKEND_OVERVIEW.md)
- [API Specifications](../backend/api/00_API_OVERVIEW.md)
- [Related Module Requirements](./related_module_requirements.md)

---

**Last Updated:** [Date]  
**Author:** Bootstrap PHASE 5  
**Status:** Ready for Development
```

**⚡ EXPECTED FILE LENGTH:**
- Module with 4 functions: **200-300 lines**
- Module with 10 functions: **400-600 lines**
- Module with 20+ functions: **800-1200 lines**

**⚡ Минимальная длина: 100 строк** (для модуля с 4+ функциями)

---

## 📝 CORE DOCUMENTATION TEMPLATES

**⚠️ КРИТИЧНО: Используй эти templates для создания core docs!**

Каждый core документ ДОЛЖЕН быть детальным и информативным, НЕ просто header'ы!

---

### Template 1: 00_PROJECT_ESSENCE.md

**Minimum: 50 lines**

```markdown
# [Project Name] - Project Essence

**Created:** [Date]  
**Version:** 1.0  
**Status:** Active

---

## 🎯 Vision

[2-3 параграфа описывающих главное видение проекта]

**What we're building:**
[Чёткое определение что строится]

**Why it matters:**
[Почему это важно]

**Long-term impact:**
[Какое влияние окажет проект в долгосрочной перспективе]

---

## 🔍 Problem Statement

### The Problem

[Детальное описание проблемы которую решает проект - 2-3 параграфа]

**Current pain points:**
- **Pain point 1:** [Description] → Impact: [quantified if possible]
- **Pain point 2:** [Description] → Impact: [quantified if possible]
- **Pain point 3:** [Description] → Impact: [quantified if possible]

**Who experiences this problem:**
- [User group 1]: [How they experience it]
- [User group 2]: [How they experience it]
- [User group 3]: [How they experience it]

**Cost of not solving:**
- [Financial cost / time cost / opportunity cost]
- [User frustration / churn]
- [Business impact]

---

## 💡 Solution

### Our Approach

[2-3 параграфа описывающих решение]

**Core solution pillars:**

1. **[Pillar 1 Name]**
   - What: [What this pillar provides]
   - How: [How it works]
   - Why: [Why this approach]

2. **[Pillar 2 Name]**
   - What: [Description]
   - How: [Mechanism]
   - Why: [Rationale]

3. **[Pillar 3 Name]**
   - What: [Description]
   - How: [Mechanism]
   - Why: [Rationale]

**Key differentiators:**
- [What makes this solution unique]
- [Advantages over alternatives]
- [Innovation elements]

---

## 🎁 Value Proposition

### For [Primary User Type]

**Value delivered:**
- [Value 1]: [Specific benefit]
- [Value 2]: [Specific benefit]
- [Value 3]: [Specific benefit]

**Metrics of success:**
- [Metric 1]: [Target] (e.g., "Reduce time by 50%")
- [Metric 2]: [Target]
- [Metric 3]: [Target]

### For [Secondary User Type]

**Value delivered:**
- [Value 1]: [Benefit]
- [Value 2]: [Benefit]

**Success metrics:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]

---

## 👥 Target Audience

### Primary Persona: [Name]

**Demographics:**
- Role: [Job title]
- Experience level: [Junior/Mid/Senior]
- Team size: [If relevant]
- Industry: [If relevant]

**Goals:**
- [Goal 1]
- [Goal 2]
- [Goal 3]

**Pain points:**
- [Pain 1 specific to this persona]
- [Pain 2]
- [Pain 3]

**Tech proficiency:**
- [Level of technical knowledge]
- [Tools they currently use]

**Quote:**
> "[A typical quote from this persona about their needs/frustrations]"

### Secondary Persona: [Name]

[Repeat same structure]

---

## 🌟 Success Criteria

**Launch criteria (MVP):**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**6-month success:**
- [Metric 1]: [Target value]
- [Metric 2]: [Target value]
- [Metric 3]: [Target value]

**1-year vision:**
- [Goal 1]
- [Goal 2]
- [Goal 3]

---

## 🔄 Related Documentation

- [PRD](./01_PRD.md) - Product requirements
- [Roadmap](./02_ROADMAP.md) - Timeline and milestones
- [Architecture](./04_ARCHITECTURE.md) - Technical architecture

---

**Last Updated:** [Date]  
**Owner:** [Team/Person]
```

**Expected length:** 50-80 lines minimum

---

### Template 2: 01_PRD.md

**Minimum: 200 lines** (самый большой документ!)

```markdown
# [Project Name] - Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** [Date]  
**Status:** Draft/Approved  
**Owner:** [Team/Person]

---

## 📋 Document Overview

### Purpose

[Paragraph explaining purpose of this PRD]

### Scope

**In scope:**
- [Feature area 1]
- [Feature area 2]
- [Feature area 3]

**Out of scope:**
- [What's NOT included]
- [Future considerations]

---

## 🎯 Product Vision & Goals

### Vision Statement

[1-2 sentences capturing product vision]

### Strategic Goals

1. **[Goal 1]**
   - Objective: [Clear objective]
   - Key Results:
     - [KR 1]
     - [KR 2]
   - Timeline: [When]

2. **[Goal 2]**
   - Objective: [Objective]
   - Key Results:
     - [KR 1]
     - [KR 2]
   - Timeline: [When]

3. **[Goal 3]**
   - Objective: [Objective]
   - Key Results:
     - [KR 1]
   - Timeline: [When]

---

## 👥 User Personas & Needs

### Primary User: [Persona Name]

**Needs:**
- [Need 1]: [Why]
- [Need 2]: [Why]
- [Need 3]: [Why]

**Current workflow:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Desired workflow:**
1. [Improved step 1]
2. [Improved step 2]
3. [Improved step 3]

---

## 🏗️ Feature Overview

### Feature Breakdown by Module

[FOR EACH MODULE из modules_list.md создай детальную секцию]

---

#### Module 1: [Module Name]

**Priority:** CRITICAL/IMPORTANT/NICE-TO-HAVE  
**Status:** [Planning/In Progress/Done]  
**Owner:** [Team/Person]

**Purpose:**
[2-3 sentences describing module purpose]

**Key Features:**

##### Feature 1.1: [Feature Name]

**Description:**
[2-3 sentences describing feature]

**User benefit:**
[What value this provides to user]

**Acceptance criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Dependencies:**
- [Dependency 1]
- [Dependency 2]

**Effort estimate:** [Small/Medium/Large] ([Story points if applicable])

**Priority:** Must-have / Should-have / Nice-to-have

---

##### Feature 1.2: [Feature Name]

[Repeat same structure for ALL features in module]

---

[CONTINUE FOR ALL MODULES - это сделает документ 200+ строк]

---

## 🔄 User Flows

### Primary User Flow: [Flow Name]

**Trigger:** [What starts this flow]

**Steps:**
1. User [action 1]
   - System [response 1]
   - Expected outcome: [Outcome 1]

2. User [action 2]
   - System [response 2]
   - Expected outcome: [Outcome 2]

3. User [action 3]
   - System [response 3]
   - Expected outcome: [Outcome 3]

**Success criteria:**
- [What defines success]

**Edge cases:**
- [Edge case 1] → [How handled]
- [Edge case 2] → [How handled]

---

## 📊 Success Metrics

### Product Metrics

**Engagement:**
- [Metric 1]: [Current baseline] → [Target]
- [Metric 2]: [Baseline] → [Target]

**Performance:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]

**Business:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]

### How we'll measure:
- [Tool/method 1]
- [Tool/method 2]

---

## 🚫 Non-Functional Requirements

### Performance

- [Requirement 1, e.g., "Page load < 2s"]
- [Requirement 2, e.g., "API response < 500ms"]
- [Requirement 3, e.g., "Support 1000 concurrent users"]

### Security

- [Security requirement 1]
- [Security requirement 2]
- [Security requirement 3]

### Scalability

- [Scalability requirement 1]
- [Scalability requirement 2]

### Accessibility

- [WCAG 2.1 Level AA compliance]
- [Keyboard navigation]
- [Screen reader support]

### Browser/Platform Support

- **Desktop:** Chrome 111+, Firefox 128+, Safari 16.4+, Edge 111+
- **Mobile:** iOS 16+, Android 12+
- **Responsive:** Support viewports from 320px to 4K

---

## ⚠️ Constraints & Assumptions

### Technical Constraints

- [Constraint 1]
- [Constraint 2]

### Business Constraints

- [Constraint 1]
- [Constraint 2]

### Assumptions

- [Assumption 1]
- [Assumption 2]

---

## 🔄 Future Considerations

### Phase 2 Features

- [Feature idea 1]
- [Feature idea 2]

### Long-term Vision

- [Vision element 1]
- [Vision element 2]

---

## 📚 Related Documentation

- [Project Essence](./00_PROJECT_ESSENCE.md)
- [Roadmap](./02_ROADMAP.md)
- [Tech Stack](./03_TECH_STACK.md)
- [Architecture](./04_ARCHITECTURE.md)
- [Module Requirements](../requirements/)

---

**Approval:**
- [ ] Product Owner: _______________
- [ ] Tech Lead: _______________
- [ ] Design Lead: _______________

**Last Updated:** [Date]
```

**Expected length:** 200-400 lines

---

### Template 3: 02_ROADMAP.md

**Minimum: 80 lines**

```markdown
# [Project Name] - Product Roadmap

**Version:** 1.0  
**Last Updated:** [Date]  
**Timeline:** [Project start] → [Target launch]

---

## 🎯 Roadmap Overview

### Project Timeline

**Total Duration:** [X weeks/months]
**Target Launch:** [Date]

**Key Milestones:**
- **Milestone 1:** [Date] - [What's delivered]
- **Milestone 2:** [Date] - [What's delivered]
- **Milestone 3:** [Date] - [What's delivered]
- **Milestone 4:** [Date] - [What's delivered]

---

## 📅 Development Phases

### Phase 1: Foundation (Weeks 1-X)

**Duration:** [X weeks]  
**Goal:** [Clear goal for this phase]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

**Modules included:**
- **Module 1:** [Module name] - [Status]
- **Module 2:** [Module name] - [Status]
- **Module 3:** [Module name] - [Status]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

**Risks:**
- ⚠️ [Risk 1] - Mitigation: [How to address]
- ⚠️ [Risk 2] - Mitigation: [How to address]

---

### Phase 2: Core Features (Weeks X-Y)

**Duration:** [Y-X weeks]  
**Goal:** [Goal for this phase]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

**Modules included:**
- **Module 4:** [Module name] - [Priority]
- **Module 5:** [Module name] - [Priority]
- **Module 6:** [Module name] - [Priority]

**Dependencies:**
- Requires Phase 1 completion
- [Other dependency]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

### Phase 3: Integration & Polish (Weeks Y-Z)

**Duration:** [Z-Y weeks]  
**Goal:** [Goal]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Modules included:**
- **Module 7:** [Module name]
- **Module 8:** [Module name]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

### Phase 4: Testing & Launch Prep (Weeks Z-End)

**Duration:** [End-Z weeks]  
**Goal:** Production readiness

**Deliverables:**
- [ ] All critical bugs fixed
- [ ] Performance optimization complete
- [ ] Documentation finalized
- [ ] Deployment pipeline ready

**Activities:**
- Beta testing
- Load testing
- Security audit
- Launch checklist completion

---

## 🎯 Module Implementation Order

### Critical Path (Must-have for MVP)

1. **[Module Name]** - Week [X]
   - Why first: [Justification]
   - Blocks: [What depends on this]

2. **[Module Name]** - Week [Y]
   - Why second: [Justification]
   - Blocks: [What depends on this]

3. **[Module Name]** - Week [Z]
   - Why third: [Justification]

[Continue for all critical modules]

### Important (Should-have)

[List important but not critical modules]

### Nice-to-have (Post-MVP)

[List nice-to-have modules for future iterations]

---

## 📊 Progress Tracking

### Current Status

**Phase:** [Current phase name]  
**Sprint:** [Current sprint number]  
**Completion:** [X]%

**Completed:**
- ✅ [Milestone 1]
- ✅ [Milestone 2]

**In Progress:**
- 🔄 [Task 1]
- 🔄 [Task 2]

**Upcoming:**
- ⏳ [Task 3]
- ⏳ [Task 4]

---

## ⚠️ Risks & Mitigation

### High Priority Risks

1. **[Risk Name]**
   - Impact: [High/Medium/Low]
   - Probability: [High/Medium/Low]
   - Mitigation: [Strategy]
   - Owner: [Person/Team]

2. **[Risk Name]**
   - Impact: [Level]
   - Probability: [Level]
   - Mitigation: [Strategy]
   - Owner: [Person/Team]

---

## 🔄 Future Iterations

### Post-MVP (Phase 2)

**Timeline:** [Months after launch]

**Planned features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Long-term Vision (Phase 3+)

**Timeline:** [6-12 months after launch]

**Strategic initiatives:**
- [Initiative 1]
- [Initiative 2]

---

## 📚 Related Documentation

- [PRD](./01_PRD.md)
- [Module Requirements](../requirements/)
- [Progress Tracking](../progress/modules_status.md)

---

**Last Updated:** [Date]  
**Next Review:** [Date]
```

**Expected length:** 80-120 lines

---

### Template 4: 03_TECH_STACK.md

**Minimum: 80 lines**

```markdown
# [Project Name] - Technology Stack

**Version:** 1.0  
**Last Updated:** [Date]  
**Status:** Approved

---

## 📋 Stack Overview

### Tech Stack Summary

**Frontend:** [Framework + key libraries]  
**Backend:** [Framework/approach]  
**Database:** [Database system]  
**Infrastructure:** [Hosting/deployment]  
**Development:** [Key dev tools]

---

## 🎨 Frontend Stack

### Core Framework

**[Framework Name] [Version]**
- **Why chosen:** [2-3 sentences explaining rationale]
- **Key features:**
  - [Feature 1]
  - [Feature 2]
  - [Feature 3]
- **Alternatives considered:** [Alternative 1], [Alternative 2]
- **Decision rationale:** [Why this over alternatives]

### UI Framework

**[UI Library Name] [Version]**
- **Why chosen:** [Explanation]
- **Components used:**
  - [Component category 1]
  - [Component category 2]
- **Customization approach:** [How we customize]

### State Management

**[State Management Solution] [Version]**
- **Why chosen:** [Rationale - e.g., "Lightweight, TypeScript-first, devtools"]
- **Usage pattern:** [How it's used in the app]
- **Store structure:** [Brief overview]

### Styling

**[Styling Solution] [Version]**
- **Why chosen:** [Rationale]
- **Approach:** [Utility-first / CSS-in-JS / etc.]
- **Theme management:** [How themes are handled]

### Additional Frontend Libraries

**[Library 1 Name]** - [Purpose]
- Version: [X.Y.Z]
- Usage: [Where/how used]

**[Library 2 Name]** - [Purpose]
- Version: [X.Y.Z]
- Usage: [Where/how used]

[Continue for all major frontend libraries]

---

## ⚙️ Backend Stack

### Backend Framework

**[Framework Name] [Version]** or **[Approach]**
- **Why chosen:** [Rationale]
- **Architecture pattern:** [e.g., API Routes, Serverless, Microservices]
- **Key features:**
  - [Feature 1]
  - [Feature 2]

### Database

**[Database Name] [Version]**
- **Type:** [Relational/NoSQL/Graph/etc.]
- **Why chosen:** [Rationale]
- **Key features used:**
  - [Feature 1 - e.g., "Row-Level Security"]
  - [Feature 2 - e.g., "Real-time subscriptions"]
  - [Feature 3 - e.g., "Full-text search"]

**Schema approach:**
- [How schema is managed]
- [Migration strategy]

### ORM/Query Builder

**[ORM Name] [Version]** (if applicable)
- **Why chosen:** [Rationale]
- **Usage:** [How it's used]

### Authentication

**[Auth Solution] [Version]**
- **Why chosen:** [Rationale]
- **Features:**
  - [Auth method 1 - e.g., "Email/password"]
  - [Auth method 2 - e.g., "OAuth providers"]
  - [Auth method 3 - e.g., "Magic links"]

### API Layer

**Approach:** [REST / GraphQL / tRPC / etc.]
- **Why this approach:** [Rationale]
- **API versioning:** [How versions are managed]
- **Documentation:** [How API is documented]

---

## 🧪 Testing Stack

### Unit Testing

**[Testing Framework] [Version]**
- **Why chosen:** [Rationale]
- **Coverage target:** [X]%
- **Key features:** [Fast, ESM support, etc.]

### Integration Testing

**[Tool Name] [Version]**
- **Why chosen:** [Rationale]
- **Scope:** [What's tested]

### E2E Testing

**[E2E Tool] [Version]**
- **Why chosen:** [Rationale]
- **Coverage:** [Critical paths covered]

---

## 🛠️ Development Tools

### Build Tools

**[Build Tool] [Version]**
- **Why chosen:** [Fast, modern, etc.]
- **Key features:** [HMR, TypeScript, etc.]

### Package Manager

**[Package Manager] [Version]**
- **Why chosen:** [Fast, disk-efficient, etc.]
- **Workspace support:** [If monorepo]

### Type Checking

**TypeScript [Version]**
- **Strictness level:** [strict/very strict]
- **Configuration highlights:** [Key tsconfig settings]

### Code Quality

**Linting:**
- [Linter] [Version] - [Config used]

**Formatting:**
- [Formatter] [Version] - [Style guide]

**Pre-commit hooks:**
- [Tool] - [What it does]

---

## 🚀 Infrastructure & DevOps

### Hosting

**[Platform Name]**
- **Why chosen:** [Rationale]
- **Regions:** [Deployment regions]
- **Scaling:** [Auto-scaling approach]

### CI/CD

**[CI/CD Tool]**
- **Pipeline:** [Stages]
- **Deployment strategy:** [Strategy]

### Monitoring

**[Monitoring Tool]**
- **Metrics tracked:** [Key metrics]
- **Alerting:** [Alert strategy]

### Version Control

**Git + [Platform]**
- **Branching strategy:** [Strategy name]
- **Review process:** [How PRs are reviewed]

---

## 📦 Third-Party Services

### [Service Category 1]

**[Service Name]**
- **Purpose:** [What it does]
- **Plan:** [Free/Paid tier]
- **Integration:** [How it's integrated]

### [Service Category 2]

**[Service Name]**
- **Purpose:** [What it does]
- **Plan:** [Tier]
- **Integration:** [How it's integrated]

---

## 📈 Version History

### Current Versions (as of [Date])

**Frontend:**
- [Library 1]: v[X.Y.Z]
- [Library 2]: v[X.Y.Z]

**Backend:**
- [Library 1]: v[X.Y.Z]
- [Library 2]: v[X.Y.Z]

**Update policy:**
- [How often dependencies are updated]
- [Security update policy]

---

## 🔄 Future Considerations

### Planned Upgrades

- [Upgrade 1] - [Timeline]
- [Upgrade 2] - [Timeline]

### Technology Evaluation

- [Tech to evaluate] - [Why considering]

---

## 📚 Related Documentation

- [Architecture](./04_ARCHITECTURE.md)
- [Backend Documentation](../backend/00_BACKEND_OVERVIEW.md)
- [ADRs](../adr/)

---

**Last Updated:** [Date]  
**Next Review:** [Date]
```

**Expected length:** 80-150 lines

---

### Template 5: 04_ARCHITECTURE.md

**Minimum: 100 lines**

```markdown
# [Project Name] - System Architecture

**Version:** 1.0  
**Date:** [Date]  
**Status:** Approved

---

## 📋 Architecture Overview

### System Description

[2-3 параграфа describing overall architecture]

**Architecture style:** [e.g., Monolithic / Microservices / Serverless / Hybrid]

**Key architectural principles:**
1. [Principle 1 - e.g., "Separation of concerns"]
2. [Principle 2 - e.g., "Modularity"]
3. [Principle 3 - e.g., "Scalability-first"]
4. [Principle 4 - e.g., "Security by design"]

---

## 🏗️ High-Level Architecture

### System Components

```
┌─────────────────────────────────────────────────┐
│                   Client Layer                   │
│  (Web Browser / Mobile App / Desktop)           │
└─────────────────────┬───────────────────────────┘
                      │
                      │ HTTPS
                      │
┌─────────────────────▼───────────────────────────┐
│              Frontend Application                │
│  - [Framework] app                              │
│  - [State management]                           │
│  - UI components                                 │
└─────────────────────┬───────────────────────────┘
                      │
                      │ API calls
                      │
┌─────────────────────▼───────────────────────────┐
│              Backend / API Layer                 │
│  - API Routes / Endpoints                       │
│  - Business logic                                │
│  - Authentication                                │
└─────────────────────┬───────────────────────────┘
                      │
                      │ Queries
                      │
┌─────────────────────▼───────────────────────────┐
│                  Database Layer                  │
│  - [Database name]                              │
│  - Schema & migrations                           │
│  - [Storage strategy]                           │
└──────────────────────────────────────────────────┘
```

---

## 🎯 Component Architecture

### Frontend Architecture

**Structure:**
```
/app                    # [Framework] app directory
├── /[route]/          # Feature-based routes
│   ├── page.tsx       # Route page
│   ├── layout.tsx     # Route layout
│   └── loading.tsx    # Loading state
├── /api/              # API routes (if applicable)
├── /components/       # Reusable components
│   ├── /ui/           # UI primitives
│   └── /features/     # Feature components
├── /lib/              # Business logic
│   ├── /stores/       # State management
│   ├── /hooks/        # Custom hooks
│   └── /utils/        # Utilities
└── /types/            # TypeScript types
```

**Key patterns:**
- **Component composition:** [How components are composed]
- **State management:** [How state flows]
- **Data fetching:** [Strategy - SSR/CSR/ISR]
- **Error boundaries:** [How errors are caught]

---

### Backend Architecture

**Structure:**
```
/api                    # API layer
├── /routes/           # Route handlers
├── /controllers/      # Business logic
├── /services/         # Service layer
├── /models/           # Data models
└── /middleware/       # Middleware functions
```

**Patterns:**
- **Layered architecture:**
  1. Route layer (HTTP handling)
  2. Controller layer (Business logic)
  3. Service layer (Complex operations)
  4. Data layer (Database access)

- **Dependency injection:** [How dependencies are injected]

---

### Database Architecture

**Schema design:**
- **Entities:** [Number] primary entities
- **Relationships:** [Relationship patterns used]
- **Indexing strategy:** [How indexes are used]

**Key tables:**

1. **[Entity 1 name]** (`table_name`)
   - Purpose: [What it stores]
   - Relationships: [Related tables]
   - Key fields: [Important columns]

2. **[Entity 2 name]** (`table_name`)
   - Purpose: [What it stores]
   - Relationships: [Related tables]
   - Key fields: [Important columns]

[Continue for key entities]

**Data access patterns:**
- [Pattern 1 - e.g., "Repository pattern"]
- [Pattern 2 - e.g., "Query builders"]

---

## 🔐 Security Architecture

### Authentication Flow

```
1. User login request → [Auth provider]
2. Token generation → JWT / Session
3. Token storage → [Where stored]
4. Request authentication → Middleware check
5. Authorization → Permission validation
```

**Authentication mechanisms:**
- [Mechanism 1 - e.g., "JWT tokens"]
- [Mechanism 2 - e.g., "Refresh tokens"]
- [Mechanism 3 - e.g., "Session management"]

### Authorization

**Permission model:**
- [How permissions are modeled]
- [Role-based / Attribute-based / etc.]

**Access control:**
- [How access is controlled]
- [Where checks happen]

### Security Measures

- **Data encryption:** [At rest / In transit]
- **Input validation:** [How validated]
- **CSRF protection:** [How protected]
- **XSS prevention:** [Prevention strategy]
- **Rate limiting:** [Limits applied]

---

## 📊 Data Flow

### Read Flow (Query)

```
User action → UI component → State manager → API call → 
Backend handler → Database query → Response → State update → 
UI re-render
```

**Optimization:**
- [Caching strategy]
- [Query optimization]

### Write Flow (Mutation)

```
User action → Form validation → API call → 
Backend validation → Database transaction → Response → 
State update → UI feedback
```

**Validation layers:**
1. Client-side: [What's validated]
2. Server-side: [What's validated]
3. Database: [Constraints]

---

## 🔄 State Management

### Global State

**Managed by:** [State management solution]

**Stores:**
- **[Store 1 name]:** [What state it manages]
- **[Store 2 name]:** [What state it manages]
- **[Store 3 name]:** [What state it manages]

**State persistence:**
- [What's persisted]
- [Where persisted - localStorage / sessionStorage]

### Server State

**Managed by:** [Data fetching library if applicable]

**Caching strategy:**
- [How server data is cached]
- [Cache invalidation strategy]

---

## 🌐 API Architecture

### API Design

**Style:** [REST / GraphQL / tRPC]

**Endpoints structure:**
```
/api/v1/
├── /auth/              # Authentication endpoints
├── /users/             # User management
├── /[resource1]/       # Resource 1 endpoints
├── /[resource2]/       # Resource 2 endpoints
└── /[resource3]/       # Resource 3 endpoints
```

**API patterns:**
- [Pattern 1 - e.g., "Resource-based URLs"]
- [Pattern 2 - e.g., "Consistent response format"]
- [Pattern 3 - e.g., "Error handling strategy"]

### API Response Format

**Success:**
```typescript
{
  success: true,
  data: { /* response data */ },
  meta?: { /* pagination, etc. */ }
}
```

**Error:**
```typescript
{
  success: false,
  error: {
    code: string,
    message: string,
    details?: any
  }
}
```

---

## 🚀 Deployment Architecture

### Infrastructure

**Hosting:** [Platform name]  
**Regions:** [Deployment regions]  
**CDN:** [CDN provider]

**Services:**
- **Frontend:** [Where hosted - e.g., "Vercel Edge Network"]
- **Backend:** [Where hosted - e.g., "Serverless functions"]
- **Database:** [Where hosted]
- **Storage:** [Storage solution]

### Scaling Strategy

**Horizontal scaling:**
- [How application scales horizontally]

**Vertical scaling:**
- [When vertical scaling is used]

**Database scaling:**
- [Read replicas / Sharding / etc.]

---

## 📈 Performance Architecture

### Frontend Performance

**Optimization strategies:**
- [Strategy 1 - e.g., "Code splitting"]
- [Strategy 2 - e.g., "Lazy loading"]
- [Strategy 3 - e.g., "Image optimization"]
- [Strategy 4 - e.g., "Caching"]

**Performance budgets:**
- First Contentful Paint: [Target]
- Largest Contentful Paint: [Target]
- Total Blocking Time: [Target]

### Backend Performance

**Optimization strategies:**
- [Strategy 1 - e.g., "Query optimization"]
- [Strategy 2 - e.g., "Caching layers"]
- [Strategy 3 - e.g., "Connection pooling"]

**Performance targets:**
- API response time: [Target]
- Database query time: [Target]

---

## 🔄 Integration Architecture

### External Integrations

**[Integration 1 Name]**
- Purpose: [What it does]
- Integration pattern: [How integrated]
- Fallback: [What happens if fails]

**[Integration 2 Name]**
- Purpose: [What it does]
- Integration pattern: [How integrated]
- Fallback: [Fallback strategy]

---

## ⚠️ Error Handling & Monitoring

### Error Handling Strategy

**Frontend errors:**
- [How client errors are caught]
- [Error boundaries usage]
- [User feedback strategy]

**Backend errors:**
- [How server errors are caught]
- [Error logging]
- [Error responses]

### Monitoring & Observability

**Metrics collected:**
- [Metric 1]
- [Metric 2]
- [Metric 3]

**Logging:**
- [What's logged]
- [Log aggregation tool]

**Alerting:**
- [Alert conditions]
- [Alert channels]

---

## 🔄 Future Architecture Evolution

### Planned Improvements

1. **[Improvement 1]**
   - Why: [Rationale]
   - Timeline: [When]

2. **[Improvement 2]**
   - Why: [Rationale]
   - Timeline: [When]

### Scalability Considerations

- [Consideration 1]
- [Consideration 2]

---

## 📚 Related Documentation

- [Tech Stack](./03_TECH_STACK.md)
- [Backend Documentation](../backend/00_BACKEND_OVERVIEW.md)
- [Database Schema](../backend/database/00_DATABASE_SCHEMA.md)
- [ADRs](../adr/)

---

**Last Updated:** [Date]  
**Reviewed by:** [Person/Team]
```

**Expected length:** 100-200 lines

---

### Template 6: 99_SYSTEM_GUIDE.md

**Minimum: 60 lines**

```markdown
# [Project Name] - System Guide

**Version:** 1.0  
**Last Updated:** [Date]  
**Audience:** Development team, AI assistants, new contributors

---

## 📋 Overview

### What is this system?

[2-3 параграфа describing the system at high level]

### System Philosophy

**Core principles:**
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

**Design values:**
- [Value 1 - e.g., "Simplicity over complexity"]
- [Value 2 - e.g., "Explicit over implicit"]
- [Value 3 - e.g., "Developer experience first"]

---

## 🚀 Getting Started

### Prerequisites

**Required:**
- [Prerequisite 1 - e.g., "Node.js 18+"]
- [Prerequisite 2 - e.g., "Git"]
- [Prerequisite 3 - e.g., "Package manager"]

**Optional:**
- [Optional tool 1]
- [Optional tool 2]

### Initial Setup

```bash
# 1. Clone repository
git clone [repo-url]

# 2. Install dependencies
[package-manager] install

# 3. Setup environment
cp .env.example .env.local

# 4. Initialize database
[command]

# 5. Start development server
[package-manager] dev
```

**First-time setup checklist:**
- [ ] Dependencies installed
- [ ] Environment variables configured
- [ ] Database initialized
- [ ] Development server running
- [ ] Can access [http://localhost:XXXX]

---

## 📁 Project Structure

### Directory Overview

```
/
├── /app                # [Framework] application
│   ├── /[routes]/      # Application routes
│   ├── /api/           # API routes
│   └── /components/    # React components
├── /lib                # Business logic & utilities
│   ├── /stores/        # State management
│   ├── /hooks/         # Custom hooks
│   └── /utils/         # Utility functions
├── /public             # Static assets
├── /docs               # Project documentation
│   ├── /core/          # Core documentation
│   ├── /requirements/  # Feature requirements
│   └── /backend/       # Backend documentation
└── /UPMT               # Bootstrap system (can be removed)
```

**Key directories explained:**

- **`/app`**: [Explanation of what goes here]
- **`/lib`**: [Explanation of business logic organization]
- **`/docs`**: [Explanation of documentation structure]

---

## 🔧 Development Workflow

### Daily Development

**Typical workflow:**
1. Pull latest changes: `git pull`
2. Create feature branch: `git checkout -b feature/[name]`
3. Make changes
4. Run tests: `[package-manager] test`
5. Commit: `git commit -m "feat: [description]"`
6. Push: `git push`
7. Create PR

**Commit message convention:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance

### Running the Project

**Development:**
```bash
[package-manager] dev      # Start dev server
[package-manager] lint     # Run linter
[package-manager] test     # Run tests
```

**Build:**
```bash
[package-manager] build    # Production build
[package-manager] start    # Start production server
```

---

## 🧪 Testing

### Test Strategy

**Unit tests:**
- Location: Next to component/function
- Run: `[package-manager] test`
- Coverage target: [X]%

**Integration tests:**
- Location: `/__tests__/integration/`
- Run: `[package-manager] test:integration`

**E2E tests:**
- Location: `/e2e/`
- Run: `[package-manager] test:e2e`

### Writing Tests

**Example test structure:**
```typescript
describe('[Component/Function name]', () => {
  it('should [expected behavior]', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

---

## 📦 Key Modules

### Module Overview

**[Module 1 Name]**
- **Purpose:** [What it does]
- **Location:** [Where code lives]
- **Key files:** [Important files]
- **Documentation:** [Link to requirements]

**[Module 2 Name]**
- **Purpose:** [What it does]
- **Location:** [Where code lives]
- **Key files:** [Important files]
- **Documentation:** [Link to requirements]

[Continue for key modules]

---

## 🔐 Environment Variables

### Required Variables

```env
# Database
DATABASE_URL="[description]"

# Authentication
AUTH_SECRET="[description]"

# API Keys
API_KEY="[description]"
```

**Where to get values:**
- [Variable 1]: [How to obtain]
- [Variable 2]: [How to obtain]

---

## 🛠️ Common Tasks

### Adding a New Feature

1. Read requirements: `docs/requirements/[module]_requirements.md`
2. Create branch: `git checkout -b feature/[name]`
3. Implement feature following architecture patterns
4. Add tests
5. Update documentation if needed
6. Submit PR

### Debugging

**Common issues:**

**Issue:** [Common problem]
- **Cause:** [Why it happens]
- **Fix:** [How to resolve]

**Issue:** [Another problem]
- **Cause:** [Why it happens]
- **Fix:** [How to resolve]

---

## 📚 Documentation Structure

### Documentation Organization

**Core docs** (`/docs/core/`):
- Project essence, PRD, roadmap, architecture

**Requirements** (`/docs/requirements/`):
- Detailed feature requirements per module

**Backend** (`/docs/backend/`):
- Database, API, entities documentation

**ADRs** (`/docs/adr/`):
- Architecture decision records

**Progress** (`/docs/progress/`):
- Current status, sprint planning

---

## 🤖 AI Assistant Guidelines

### For AI Code Assistants (like me!)

**When working on this project:**
1. **Always read requirements first:** Check `docs/requirements/[module]_requirements.md`
2. **Follow architecture patterns:** Refer to `docs/core/04_ARCHITECTURE.md`
3. **Check tech stack:** See `docs/core/03_TECH_STACK.md` for approved technologies
4. **Maintain code style:** Follow existing patterns in codebase
5. **Write tests:** Always include tests for new features
6. **Update docs:** If you change behavior, update relevant docs

**Key files to reference:**
- `docs/core/00_PROJECT_ESSENCE.md` - Project vision
- `docs/core/01_PRD.md` - All features overview
- `docs/core/04_ARCHITECTURE.md` - Architecture patterns
- `.cursorrules` - AI-specific rules

---

## 🔄 Maintenance

### Regular Tasks

**Weekly:**
- [ ] Review open PRs
- [ ] Check for dependency updates
- [ ] Review metrics/errors

**Monthly:**
- [ ] Update dependencies
- [ ] Review and update documentation
- [ ] Security audit

---

## 📞 Getting Help

**Resources:**
- **Documentation:** Start with `/docs/core/`
- **Requirements:** Check `/docs/requirements/`
- **Architecture:** See `/docs/core/04_ARCHITECTURE.md`
- **Issues:** [Link to issue tracker]

**Questions:**
- [How to get help]
- [Team contact info]

---

## 🎯 Next Steps

**For new developers:**
1. ✅ Complete setup (see Getting Started)
2. 📖 Read [Project Essence](./00_PROJECT_ESSENCE.md)
3. 📖 Read [PRD](./01_PRD.md) for features overview
4. 🏗️ Review [Architecture](./04_ARCHITECTURE.md)
5. 🔨 Pick a task from backlog
6. 💻 Start coding!

---

**Last Updated:** [Date]  
**Maintainer:** [Person/Team]
```

**Expected length:** 60-100 lines

---

## 📋 ПОСЛЕДОВАТЕЛЬНОСТЬ СОЗДАНИЯ (СТРОГО)

### BATCH 1: Core Documentation (30-45 минут)

**Создай `docs/core/` (6 файлов):**

**⚠️ КРИТИЧНО: Используй TEMPLATES из секции "CORE DOCUMENTATION TEMPLATES" выше!**

**Для КАЖДОГО файла:**

1. **`00_PROJECT_ESSENCE.md`** (minimum 50 lines)
   - Используй Template 1 (выше)
   - Заполни из `synthesized-project-data.md`
   - Секции: Vision, Problem, Solution, Value Proposition, Target Audience, Success Criteria

2. **`01_PRD.md`** (minimum 200 lines - САМЫЙ БОЛЬШОЙ!)
   - Используй Template 2 (выше)
   - Для КАЖДОГО модуля из `modules_list.md` создай детальную секцию
   - Для КАЖДОЙ функции из `extracted_features.md` добавь feature description
   - НЕ пропускай модули! PRD ДОЛЖЕН быть 200+ строк

3. **`02_ROADMAP.md`** (minimum 80 lines)
   - Используй Template 3 (выше)
   - Заполни phases из `metadata.yaml`
   - Добавь module implementation order из `modules_list.md`

4. **`03_TECH_STACK.md`** (minimum 80 lines)
   - Используй Template 4 (выше)
   - Заполни из `final-tech-stack.md`
   - Для КАЖДОЙ технологии добавь rationale и version

5. **`04_ARCHITECTURE.md`** (minimum 100 lines)
   - Используй Template 5 (выше)
   - Заполни architecture overview
   - Добавь диаграммы и data flows

6. **`99_SYSTEM_GUIDE.md`** (minimum 60 lines)
   - Используй Template 6 (выше)
   - Setup instructions, project structure, development workflow

**⚠️ SELF-CHECK после создания:**

```python
print("\n🔍 BATCH 1 Quality Check: Core Documentation\n")

core_docs_errors = []
core_docs_requirements = {
    "docs/core/00_PROJECT_ESSENCE.md": 50,
    "docs/core/01_PRD.md": 200,  # PRD ДОЛЖЕН быть большим!
    "docs/core/02_ROADMAP.md": 80,
    "docs/core/03_TECH_STACK.md": 80,
    "docs/core/04_ARCHITECTURE.md": 100,
    "docs/core/99_SYSTEM_GUIDE.md": 60
}

for doc_file, min_lines in core_docs_requirements.items():
    if os.path.exists(doc_file):
        content = read_file(doc_file)
        line_count = len(content.split('\n'))
        
        if line_count < min_lines:
            core_docs_errors.append({
                "file": os.path.basename(doc_file),
                "issue": f"Too short: {line_count} lines (minimum {min_lines})",
                "fix": "Expand using template - add all required sections"
            })
            print(f"   ❌ {os.path.basename(doc_file)}: {line_count} lines (min {min_lines})")
        else:
            print(f"   ✅ {os.path.basename(doc_file)}: {line_count} lines")
    else:
        core_docs_errors.append({
            "file": os.path.basename(doc_file),
            "issue": "File missing"
        })
        print(f"   ❌ {os.path.basename(doc_file)}: MISSING")

if core_docs_errors:
    print(f"\n❌ CORE DOCS TOO SHORT! {len(core_docs_errors)} errors\n")
    for error in core_docs_errors:
        print(f"   - {error['file']}: {error['issue']}")
        if 'fix' in error:
            print(f"     Fix: {error['fix']}")
    
    raise ValidationError("Core documentation does not meet quality standards. "
                         "Regenerate using templates with all sections filled.")
else:
    print(f"\n✅ All core docs meet minimum standards!\n")
```

**Если проверка FAILED - перегенерируй короткие файлы с ПОЛНЫМ контентом из templates!**

**Checkpoint:**

**⚠️ КРИТИЧНО: Checkpoint ДОЛЖЕН быть сохранен после КАЖДОГО batch и после завершения PHASE 5!**

**1. Сохранить JSON Checkpoint (ОБЯЗАТЕЛЬНО!):**

```python
save_checkpoint(
    phase_number=5,
    phase_name="PHASE 5: Documentation",
    batch=1,
    state={
        "current_action": "Created core documentation files",
        "files_created": [
            "docs/core/00_PROJECT_ESSENCE.md",
            "docs/core/01_PRD.md",
            "docs/core/02_USER_STORIES.md",
            "docs/core/03_TECH_STACK.md",
            "docs/core/04_ARCHITECTURE.md",
            "docs/core/05_DEVELOPMENT_PHASES.md"
        ],
        "context_files": [
            "extracted_features.md",
            "modules_list.md",
            "metadata.yaml",
            "PROJECT_SYNTHESIS.md"
        ]
    }
)
```

**2. Git Checkpoint:**

```bash
git add docs/core/
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 5 batch 1 - core documentation"
git push
```

---

### BATCH 2: Module Requirements (ДИНАМИЧЕСКОЕ СОЗДАНИЕ)

**⚠️ КРИТИЧНО:** Читай количество модулей из `modules_list.md`, не хардкодь!

**⚠️ КРИТИЧНО: Обработка больших файлов**

**Используй `safe_read_file()` из адаптера для автоматической обработки больших файлов.**

**⚠️ КРИТИЧНО: НЕ создавай stub files!** Каждый requirements file ДОЛЖЕН быть детальным!

---

#### ШАГ 2.1: Подготовка данных

```python
# 1. Прочитай modules_list.md (может быть большим)
modules_content = safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")

# 2. Прочитай extracted_features.md (может быть ОЧЕНЬ большим)
features_content = safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")

# 3. Прочитай synthesized-project-data.md для контекста
synthesis_content = safe_read_file("synthesized-project-data.md")

# 4. Посчитай модули
TOTAL_MODULES = count_modules(modules_content)
TOTAL_FUNCTIONS = count_functions(features_content)

print(f"📊 Requirements Generation Setup:")
print(f"   Total Modules: {TOTAL_MODULES}")
print(f"   Total Functions: {TOTAL_FUNCTIONS}")
print(f"   Target: {TOTAL_MODULES} detailed requirements files\n")
```

---

#### ШАГ 2.2: Генерация requirements files

**Для КАЖДОГО модуля создай ДЕТАЛЬНЫЙ requirements file:**

```python
BATCH_SIZE = 6
BATCHES = ceil(TOTAL_MODULES / BATCH_SIZE)

for batch_num in range(1, BATCHES + 1):
    module_start = (batch_num - 1) * BATCH_SIZE + 1
    module_end = min(batch_num * BATCH_SIZE, TOTAL_MODULES)
    
    print(f"\n📦 PHASE 5 Batch {batch_num}/{BATCHES}: Modules {module_start}-{module_end}\n")
    
    for module in modules[module_start:module_end]:
        # 1. Извлеки все функции этого модуля из extracted_features.md
        module_functions = extract_functions_for_module(features_content, module.id)
        
        # 2. Извлеки module details из modules_list.md
        module_details = extract_module_details(modules_content, module.id)
        
        # 3. Для КАЖДОЙ функции создай детальный content:
        requirements_content = f"""# {module.name} Requirements

**Module ID:** Module {module.id}
**Total Functions:** {len(module_functions)}
**Priority:** {module.priority}
**Status:** Not Started
**Dependencies:** {module.dependencies}

---

## Overview

{module_details.description}

{module_details.purpose}

**Key Capabilities:**
{generate_capabilities_list(module_functions)}

**Integration Points:**
{module_details.integrations}

---
"""
        
        # 4. Для КАЖДОЙ функции добавь ПОЛНЫЙ блок (используя TEMPLATE выше!)
        for func in module_functions:
            requirements_content += generate_function_requirements(
                function=func,
                module_context=module_details,
                template=REQUIREMENTS_TEMPLATE  # Из секции выше!
            )
            # Каждая функция = 40-80 строк детальной документации
        
        # 5. Добавь Module-Level Requirements секцию
        requirements_content += generate_module_level_requirements(module_details)
        
        # 6. ПРОВЕРКА: Файл НЕ должен быть stub!
        line_count = len(requirements_content.split('\n'))
        
        if line_count < 50:
            raise Error(f"❌ Requirements file for {module.name} is TOO SHORT! "
                       f"Got {line_count} lines, minimum 50. "
                       f"You MUST create detailed user stories and acceptance criteria!")
        
        if "See extracted_features.md" in requirements_content:
            raise Error(f"❌ Requirements file for {module.name} is a STUB FILE! "
                       f"FORBIDDEN! Replace with full detailed content using template.")
        
        # 7. Сохрани файл
        file_path = f"docs/requirements/{module.slug}_requirements.md"
        write_file(file_path, requirements_content)
        
        print(f"   ✅ {module.name}: {line_count} lines, {len(module_functions)} functions")
    
    # ⚠️ КРИТИЧНО: CHECKPOINT после каждого батча (ОБЯЗАТЕЛЬНО!)
    
    # 1. Сохранить JSON Checkpoint (ОБЯЗАТЕЛЬНО!)
    save_checkpoint(
        phase_number=5,
        phase_name="PHASE 5: Documentation",
        batch=batch_num,
        state={
            "current_action": f"Generated requirements for modules {module_start}-{module_end}",
            "modules_completed": [m.name for m in modules[0:module_end]],
            "total_modules": len(modules),
            "current_module": modules[module_end].name if module_end < len(modules) else "COMPLETE",
            "files_created": [f"docs/requirements/{m.name.lower().replace(' ', '-')}.md" 
                             for m in modules[0:module_end]]
        }
    )
    
    # 2. Git checkpoint
    git add docs/requirements/
    git add .upmt/checkpoints/
    git commit -m "docs(bootstrap): PHASE 5 batch {batch_num}/{BATCHES} - modules {module_start}-{module_end}"
    git push
    
    print(f"\n✅ Batch {batch_num}/{BATCHES} complete!")
    print(f"   Remaining: {TOTAL_MODULES - module_end} modules\n")
```

**⚠️ ПОМНИ:** Каждая функция ДОЛЖНА иметь:
- User story (As a... I want... So that...)
- 2-3 acceptance criteria (Given/When/Then)
- Technical requirements (Frontend, Backend, API)
- UI behavior описание
- Error handling
- Edge cases
- Dependencies
- Testing considerations

**Это НЕ опционально!** Stub files = ПРОВАЛ PHASE 5.

---

#### ШАГ 2.3: Self-Check после генерации

**После создания ВСЕХ requirements files, выполни проверку качества:**

```python
print("\n🔍 QUALITY VERIFICATION: Requirements Files\n")

errors = []
warnings = []
stats = {
    "total_files": 0,
    "total_lines": 0,
    "min_lines": float('inf'),
    "max_lines": 0,
    "stub_files": 0,
    "missing_user_stories": 0
}

for req_file in glob("docs/requirements/*_requirements.md"):
    filename = os.path.basename(req_file)
    content = read_file(req_file)
    lines = content.split('\n')
    line_count = len(lines)
    
    stats["total_files"] += 1
    stats["total_lines"] += line_count
    stats["min_lines"] = min(stats["min_lines"], line_count)
    stats["max_lines"] = max(stats["max_lines"], line_count)
    
    # CRITICAL CHECK 1: Minimum line count
    if line_count < 50:
        errors.append({
            "file": filename,
            "severity": "CRITICAL",
            "issue": f"File too short: {line_count} lines (minimum 50)",
            "fix": "Regenerate with detailed user stories and acceptance criteria for EVERY function"
        })
    elif line_count < 100:
        warnings.append({
            "file": filename,
            "issue": f"Short file: {line_count} lines (recommended 100+)"
        })
    
    # CRITICAL CHECK 2: Stub file detection
    stub_indicators = [
        "See extracted_features.md",
        "For detailed acceptance criteria, see",
        "For complete function list"
    ]
    if any(indicator in content for indicator in stub_indicators):
        stats["stub_files"] += 1
        errors.append({
            "file": filename,
            "severity": "CRITICAL",
            "issue": "STUB FILE DETECTED (contains redirect to extracted_features.md)",
            "fix": "Replace entire content with detailed requirements using template from REQUIREMENTS FILE TEMPLATE section"
        })
    
    # CRITICAL CHECK 3: User stories presence
    function_count = content.count("## Function")
    user_story_count = content.count("### User Story")
    
    if function_count > 0 and user_story_count == 0:
        stats["missing_user_stories"] += 1
        errors.append({
            "file": filename,
            "severity": "CRITICAL",
            "issue": f"NO USER STORIES found (module has {function_count} functions)",
            "fix": "Add '### User Story' section for EVERY function with format: As a... I want... So that..."
        })
    elif user_story_count < function_count:
        warnings.append({
            "file": filename,
            "issue": f"Missing user stories for some functions ({user_story_count}/{function_count})"
        })
    
    # WARNING CHECK: Acceptance criteria presence
    ac_count = content.count("### Acceptance Criteria")
    if function_count > 0 and ac_count < function_count * 0.5:
        warnings.append({
            "file": filename,
            "issue": f"Insufficient acceptance criteria ({ac_count} criteria for {function_count} functions)"
        })
    
    # Success case
    if not any(err["file"] == filename for err in errors):
        print(f"   ✅ {filename}: {line_count} lines, {function_count} functions, {user_story_count} user stories")

# Print statistics
avg_lines = stats["total_lines"] / stats["total_files"] if stats["total_files"] > 0 else 0

print(f"\n📊 Requirements Files Statistics:")
print(f"   Total files: {stats['total_files']}")
print(f"   Total lines: {stats['total_lines']}")
print(f"   Average lines per file: {avg_lines:.0f}")
print(f"   Min lines: {stats['min_lines']}")
print(f"   Max lines: {stats['max_lines']}")

# Print results
if errors:
    print(f"\n❌ VALIDATION FAILED - {len(errors)} CRITICAL ERRORS:\n")
    for error in errors:
        print(f"   ❌ {error['file']}")
        print(f"      Severity: {error['severity']}")
        print(f"      Issue: {error['issue']}")
        print(f"      Fix: {error['fix']}\n")
    
    print(f"\n⛔ BOOTSTRAP CANNOT CONTINUE WITH STUB FILES!")
    print(f"   You MUST regenerate these files with FULL detailed content.")
    print(f"   Use the REQUIREMENTS FILE TEMPLATE from the beginning of this phase.\n")
    
    raise ValidationError(f"Requirements quality check failed: {len(errors)} critical errors. "
                         f"Stub files detected: {stats['stub_files']}. "
                         f"Missing user stories: {stats['missing_user_stories']}.")

if warnings:
    print(f"\n⚠️ {len(warnings)} WARNINGS (not blocking):\n")
    for warning in warnings:
        print(f"   ⚠️ {warning['file']}: {warning['issue']}")
    print(f"\n   Consider adding more details to improve quality.")

print(f"\n✅ REQUIREMENTS QUALITY CHECK PASSED!")
print(f"   All {stats['total_files']} files meet minimum quality standards.\n")
```

**Если проверка НЕ прошла:**
1. ❌ ОСТАНОВИСЬ
2. 🔍 Посмотри какие файлы провалили проверку
3. 🔧 Перегенерируй эти файлы с ПОЛНЫМ контентом (используя template)
4. ✅ Запусти проверку снова

**Checkpoint после успешной проверки:**
```bash
git add docs/requirements/
git commit -m "docs(bootstrap): PHASE 5 batch 2 complete - all requirements validated"
git push
```

---

### BATCH 3: Context Files (15 минут)

**Создай `.context/` (4 файла):**

1. `state.md` - НЕ template! Заполни реальными данными:
   ```markdown
   **Current Phase:** Planning (Documentation)
   **Last Activity:** Bootstrap completed PHASE 4
   **Progress:** [existing project: X% / new project: 0%]
   ```

2. `decisions.md` - Минимум 5 decision records:
   - Решения из PHASE 2 (interview)
   - Решения из PHASE 3 (tech stack updates)
   - [Если existing] Найденные architectural patterns

3. `insights.md` - Ключевые инсайты:
   - Из analysis report
   - [Если existing] Из code analysis
   
4. `changes_log.md` - Начальная запись:
   ```markdown
   # [Date] - Bootstrap Complete
   - Created full documentation ([N] файлов)
   - Extracted [M] functions, [K] modules
   - Verified tech stack ({CURRENT_MONTH_YEAR})
   ```

**Checkpoint:**
```bash
git add .context/
git commit -m "docs(bootstrap): PHASE 5 batch 3 - context files"
git push
```

---

### BATCH 4: Progress Tracking (15 минут)

**Создай `docs/progress/` (3 файла):**

1. `modules_status.md` - статус ВСЕХ модулей из modules_list.md:
   
   **New project:**
   ```markdown
   ### Module 1: [Name]
   **Status:** ❌ Not Started  
   **Progress:** 0%
   ```
   
   **Existing project:**
   ```markdown
   ### Module 1: [Name]
   **Status:** ✅ Complete / 🔄 In Progress / ❌ Not Started
   **Progress:** [X]%
   **Location:** [путь в коде]
   ```

2. `sprint_current.md` - планирование первого спринта (реальные задачи из backlog)

3. `backlog.md` - приоритизированный backlog (ВСЕ функции из extracted_features.md)

**Checkpoint:**
```bash
git add docs/progress/
git commit -m "docs(bootstrap): PHASE 5 batch 4 - progress tracking"
git push
```

---

### BATCH 5: Project Metadata & AI Rules (15 минут)

**Создай `.upmt/` и `.cursorrules`:**

1. **Скопируй metadata:**
   ```
   UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml → .upmt/metadata.yaml
   ```

2. **Создай `.cursorrules`:**
   - Прочитай `UPMT/structure-templates/AI_INSTRUCTIONS/.cursorrules.template`
   - Заполни AUTO-GENERATED секцию:
     * Project name (из metadata.yaml)
     * Tech stack (из final-tech-stack.md)
     * Modules list (из modules_list.md)
     * Current phase
     * File inventory

3. **Проверь:**
   - ✅ `.upmt/metadata.yaml` создан
   - ✅ `.cursorrules` создан в КОРНЕ проекта (не в template!)

**Checkpoint:**
```bash
git add .upmt/ .cursorrules
git commit -m "docs(bootstrap): PHASE 5 batch 5 - metadata & AI rules"
git push
```

---

### BATCH 6: Project README (10 минут)

**Обнови `/README.md`:**

Замени placeholder на полное описание проекта:
- Название проекта
- Описание (из 00_PROJECT_ESSENCE.md)
- Quick start инструкции
- Tech stack (из 03_TECH_STACK.md)
- Структура проекта
- Links to docs/

**⚠️ НЕ путай с `UPMT/README_TEMPLATE.md` (про UPMT систему)!**

**Checkpoint:**
```bash
git add README.md
git commit -m "docs(bootstrap): PHASE 5 batch 6 - project README"
git push
```

---

## 💾 FINAL CHECKPOINT

**⚠️ КРИТИЧНО: Финальный checkpoint ДОЛЖЕН быть сохранен после завершения ВСЕХ батчей PHASE 5!**

**После завершения ВСЕХ батчей:**

**1. Сохранить JSON Checkpoint (ОБЯЗАТЕЛЬНО!):**

```python
save_checkpoint(
    phase_number=5,
    phase_name="PHASE 5: Documentation",
    batch=None,  # Финальный checkpoint без номера батча
    state={
        "current_action": "PHASE 5 complete - all documentation generated",
        "files_created": [
            # Все созданные файлы
            "docs/core/*",
            "docs/requirements/*",
            ".context/*",
            "docs/progress/*",
            ".upmt/metadata.yaml",
            ".cursorrules",
            "README.md"
        ],
        "context_files": [
            "extracted_features.md",
            "modules_list.md",
            "metadata.yaml",
            "PROJECT_SYNTHESIS.md"
        ],
        "total_modules": "[N модулей]",
        "total_files": "[N файлов]"
    }
)
```

Это создаст:
- `.upmt/checkpoints/latest.json` (phase: 5, batch: None)
- `.upmt/checkpoints/phase-5.json` (архив финального состояния)

**2. Git Checkpoint:**

```bash
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 5 COMPLETE - full documentation generated" --allow-empty
git push
```

**Показать итоги:**

```markdown
✅ PHASE 5 COMPLETE

**Documentation Created:**
- ✅ docs/core/ (6 files)
- ✅ docs/requirements/ ([TOTAL_MODULES] files)
- ✅ .context/ (4 files)
- ✅ docs/progress/ (3 files)
- ✅ .upmt/metadata.yaml
- ✅ .cursorrules
- ✅ README.md

**Total Files Created:** [N]

**Module Requirements:**
- [TOTAL_MODULES] modules documented
- [TOTAL_FUNCTIONS] functions accounted for
- ✅ Completeness validation passed

**Next:** PHASE 5.5 - Design System (conditional)

⏱️ PHASE 5 завершена за [время]
```

---

## 📊 ПРОГРЕСС TRACKING

**Каждые 30 минут показывай:**

```markdown
⏱️ PHASE 5 PROGRESS UPDATE

**Current Batch:** Batch [X]/[Y]
**Progress:** [X]%

**Completed:**
- ✅ docs/core/ (6 files)
- ✅ docs/requirements/ ([N] modules)
- 🔄 Working on batch [X]...

**Remaining:**
- [ ] [REMAINING] modules
- [ ] .context/
- [ ] docs/progress/
- [ ] .cursorrules

**Checkpoint commits:** [N]
```

---

## 🚨 КРИТИЧЕСКИЕ ПРАВИЛА PHASE 5

1. **ДИНАМИЧЕСКОЕ СОЗДАНИЕ МОДУЛЕЙ**
   - НЕ хардкодь количество модулей
   - Читай из modules_list.md
   - Создавай requirements для ВСЕХ модулей

2. **CHECKPOINT ПОСЛЕ КАЖДОГО БАТЧА**
   - Не пытайся создать всё за раз
   - Коммит после каждых 6 модулей
   - Показывай прогресс

3. **ВСЕ ФУНКЦИИ ДОЛЖНЫ БЫТЬ УЧТЕНЫ**
   - Каждая функция из extracted_features → в requirements
   - Проверка полноты обязательна

4. **НЕ ОСТАВЛЯЙ TEMPLATES**
   - Все файлы заполнены реальными данными
   - state.md, decisions.md, sprint_current.md - реальное содержимое

5. **ИСПОЛЬЗУЙ АДАПТЕР**
   - CLI: `write("path", content)`
   - Web: `gh api PUT /repos/{owner}/{repo}/contents/path`

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
→ ПЕРЕХОД К PHASE 5.4: FIGMA MAKE PROMPT (optional) или PHASE 5.5: DESIGN SYSTEM (conditional)
→ Orchestrator определит следующую фазу на основе выбора пользователя и наличия данных
→ Прочитай: UPMT/prompts/phases/phase-5.4-figma-prompt.md (если выбрана PHASE 5.4)
→ Прочитай: UPMT/prompts/phases/phase-5.5-design.md (если выбрана PHASE 5.5)
```

