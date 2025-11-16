# BOOTSTRAP INSTRUCTIONS FOR CLAUDE CODE

## Your Mission

Analyze all data in `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/` and bootstrap a complete project
management system following the documentation-driven approach.

## Phase 1: ANALYSIS (Autonomous - 1-2 hours)

### Task 1.1: Read Everything

Read ALL files in:
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/` - All chat transcripts
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/documents/` - All documents
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/notes/` - All notes
- `.upmt/metadata.yaml` - Context about data

### Task 1.2: Extract Information

From all sources, extract:

**HIGH CONFIDENCE (clearly stated, consistent):**
- Project vision and goals
- Target audience / user personas
- Core features (must-have)
- Key user flows
- Success metrics
- Constraints and assumptions

**MEDIUM CONFIDENCE (stated but may have variations):**
- Technology preferences
- Architecture ideas
- Nice-to-have features
- Timeline expectations

**CONTRADICTIONS FOUND:**
List all contradictions with:
- Topic: [what contradicts]
- Source A: [chat-1] says [X]
- Source B: [chat-3] says [Y]
- Dates: [when discussed]

**GAPS / MISSING INFORMATION:**
List what's missing for complete project setup:
- Tech stack decisions
- Architecture patterns
- Database choice
- Deployment strategy
- etc.

### Task 1.3: Create Analysis Report

Generate: `/analysis-report.md`

Structure:
1. Executive Summary
2. High Confidence Findings
3. Medium Confidence Findings
4. Contradictions Found (with context)
5. Information Gaps
6. Recommended Questions for User

## Phase 2: INTERVIEW (Interactive - 30-60 min)

### Task 2.1: Present Findings

Show user:
1. What you found (summary)
2. What contradicts (need resolution)
3. What's missing (need answers)

### Task 2.2: Ask Questions

Generate questions in priority order:

**CRITICAL (must answer before proceeding):**
- Contradictions that affect architecture
- Core technology decisions
- Missing must-have information

**IMPORTANT (should answer for quality):**
- Nice-to-have features prioritization
- Timeline preferences
- Team composition

**OPTIONAL (can infer if not answered):**
- Detailed preferences
- Minor technical choices

### Task 2.3: Interactive Q&A

Ask questions ONE BY ONE or in BATCHES (user preference).

Wait for answers.

Record answers to `/interview-responses.md`.

## Auto-Fill Metadata Feature

**v1.0.1+: Вам НЕ нужно вручную заполнять metadata.yaml!**

**Полное описание процесса:** см. **@AUTO_FILL_INSTRUCTIONS.md**

### Краткий обзор:

**Как работает:**
1. Claude Code читает все raw data из `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/` (chats, documents, notes)
2. Извлекает ключевую информацию автоматически
3. Задаёт 5-10 уточняющих вопросов для разрешения противоречий
4. Автоматически заполняет `.upmt/metadata.yaml`

**Что включено:**
- Интерактивный Q&A процесс
- Tech stack verification ({CURRENT_MONTH_YEAR})
- Existing code analysis (если проект уже существует)
- Рекомендации по модернизации

**Детали см:** `@AUTO_FILL_INSTRUCTIONS.md`

### Tech Stack Recommendations

Claude Code автоматически анализирует и рекомендует технологии.

**Полный процесс верификации:** см. **@tech-stack-verification.md**

**Краткий обзор:**
- Извлечение упоминаний из raw data
- Проверка актуальности ({CURRENT_MONTH_YEAR})
- Анализ fit с требованиями проекта
- Рекомендации с обоснованием
- Migration paths (если нужны обновления)

**Детали см:** `@tech-stack-verification.md`

## Phase 3: SYNTHESIS (Quick - 15 min)

Combine:
- Extracted information (high confidence)
- Resolved contradictions (from interview)
- User answers (from interview)

Create unified view: `/synthesized-project-data.md`

## Phase 4: STRUCTURE DEPLOYMENT (Autonomous - 2-4 hours)

### Task 4.1: Create Documentation Structure

Deploy full system:

```
docs/core/
  00_PROJECT_ESSENCE.md
  01_PRD.md
  02_ROADMAP.md
  03_TECH_STACK.md
  04_ARCHITECTURE.md
  99_SYSTEM_GUIDE.md

docs/requirements/
  _MODULE_TEMPLATE.md (from UPMT/structure-templates/)
  [module1]_requirements.md
  [module2]_requirements.md
  ...

.context/
  state.md
  decisions.md
  insights.md
  changes_log.md

.cursorrules (in project root, copied from UPMT/structure-templates/AI_INSTRUCTIONS/.cursorrules.template)

docs/progress/
  modules_status.md
  sprint_current.md
  backlog.md
```

### Task 4.2: Fill Core Documents

Fill each document with synthesized data:

**PROJECT_ESSENCE:**
- From vision discussions
- Core value proposition
- Target audience
- Must-have features

**PRD:**
- All features mentioned in chats
- Organized by priority
- User stories from discussions
- Acceptance criteria inferred or ask user

**ROADMAP:**
- Phases based on feature complexity
- MVP scope from discussions
- Timeline if mentioned

**TECH_STACK:**
- Technologies from synthesis
- Rationale from chat context
- Alternatives considered (if discussed)

**ARCHITECTURE:**
- Pattern from synthesis
- Component structure
- Data flow
- Integration points

### Task 4.3: Create Module Requirements

For each major feature/module identified:
- Create `docs/requirements/[module]_requirements.md`
- Fill with functional requirements
- Use template structure from `UPMT/structure-templates/_MODULE_TEMPLATE.md`
- Extract details from chats
- Mark TODOs where info is missing

### Task 4.4: Set Up Context Files

**state.md:**
- Location: `.context/state.md`
- Current phase: Planning / Pre-development
- Last activity: Project bootstrapped
- Next steps: Review documentation

**decisions.md:**
- Location: `.context/decisions.md`
- All decisions from chats (with dates)
- Sources (which chat)
- Rationale (context from discussion)

**insights.md:**
- Location: `.context/insights.md`
- Learnings from chat analysis
- Common themes
- Important considerations mentioned

## Phase 5: VALIDATION & REPORT (15 min)

### Task 5.1: Self-Check

Verify:
- [ ] All contradictions resolved or flagged?
- [ ] All critical info captured?
- [ ] Documents consistent with each other?
- [ ] No broken cross-references?
- [ ] All TODOs marked clearly?

### Task 5.2: Generate Bootstrap Report

Create: `/BOOTSTRAP_REPORT.md`

Include:

**1. WHAT WAS CREATED:**
- File tree (all created files)
- Statistics (pages, features, modules)

**2. DATA SOURCES ANALYZED:**
- List of all files read
- Information extracted from each

**3. DECISIONS MADE:**
- List decisions (with sources)
- Contradictions resolved (how)
- Gaps filled (how - inferred/asked)

**4. WHAT'S READY:**
-  Core documentation complete
-  Module requirements (X modules)
-  System rules configured
-  Ready for development

**5. WHAT NEEDS REVIEW:**
- Items marked TODO (with reasons)
- Inferred decisions (need confirmation)
- Assumptions made (need validation)

**6. NEXT STEPS FOR USER:**
1. Review all core documents
2. Confirm inferred decisions
3. Fill remaining TODOs
4. Start development!

### Task 5.3: Create Review Checklist

Generate: `/REVIEW_CHECKLIST.md`

For user to review each document systematically.

### Task 5.4: Generate Final Setup Instructions

Generate: `UPMT/bootstrap/BOOTSTRAP_CONFIG/FINAL_SETUP_INSTRUCTIONS.md`

**Content:**
- Cursor project rules setup (copy .cursorrules, configure settings)
- Claude Code configuration (automatic via .clauderules)
- Additional Project Rules (for file management during updates/milestones)
- Daily workflow guide
- Rules update triggers (when to update .cursorrules/.clauderules)
- Links to resources (WORKFLOW_GUIDE.md, UPDATE_RULES.md, etc.)

**Purpose:**
User will follow these instructions to complete setup after bootstrap.

**Critical:** This file guides post-bootstrap configuration!

## Configuration

Work autonomously but:
- ASK before making major assumptions
- ASK if contradiction resolution unclear
- ASK if critical information missing
- INFORM user of progress every 30 min

Be thorough but pragmatic:
- Mark TODOs rather than block on minor details
- Infer reasonable defaults (document assumption)
- Focus on getting 80% complete - user can refine

## Success Criteria

System is ready when:
 User can read PROJECT_ESSENCE and understand project
 Developer can read PRD and start implementing
 AI assistant can read requirements and code
 Team can track progress from day 1

GO! =�
