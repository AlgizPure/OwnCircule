Создай файл: `AI_INSTRUCTIONS/UPDATE_RULES.md`


# UPDATE RULES - Правила Обновления Документов

**Version:** 1.0  
**Last Updated:** [date]  
**Purpose:** Детальная матрица когда и как обновлять документы

---

## 📋 СОДЕРЖАНИЕ

1. [Триггеры Обновлений](#триггеры-обновлений)
2. [Детальные Правила по Файлам](#детальные-правила-по-файлам)
3. [Шаблоны Обновлений](#шаблоны-обновлений)
4. [Валидация После Обновления](#валидация-после-обновления)

---

## 🎯 ТРИГГЕРЫ ОБНОВЛЕНИЙ

### Триггер A: Изменение в PROJECT_ESSENCE.md

**Когда происходит:**
- Изменилось видение продукта
- Изменилась целевая аудитория
- Изменилась core value proposition
- Добавлена/удалена ключевая фича из Must Have

**Что обновлять ОБЯЗАТЕЛЬНО:**
1. PROJECT_ESSENCE.md itself:
   actions:
     - Update version: MAJOR.MINOR → MAJOR+1.0
     - Update "Last Updated" date
     - Add CHANGELOG entry
   template: |
     ## CHANGELOG
     ### v2.0 - [date]
     - Changed vision from "[old]" to "[new]"
     - Rationale: [why change happened]
     - Impact: [what this means for product]

2. PRD.md:
   priority: CRITICAL
   sections_to_check:
     - "2. OBJECTIVES & GOALS" 
       → Must align with new ESSENCE vision
     - "3. USER PERSONAS" 
       → Update if target audience changed
     - "4. FEATURES" 
       → Add/remove features based on ESSENCE changes
   actions:
     - Update affected sections
     - Version: MINOR bump (1.5 → 1.6) or MAJOR if significant
     - Add CHANGELOG: "Aligned with PROJECT_ESSENCE v2.0"
   validation:
     - No contradictions with ESSENCE
     - All ESSENCE "Must Have" features present in PRD

3. ROADMAP.md:
   priority: HIGH
   sections_to_check:
     - "PHASES" → Reprioritize if core features changed
     - "MODULES BREAKDOWN" → Update priorities
   actions:
     - If Must Have feature added → add to MVP or Phase 1
     - If feature removed → move to Backlog or delete
     - Recalculate timelines if scope changed
     - Version: MINOR bump
     - CHANGELOG entry

4. All Module Requirements:
   priority: MEDIUM
   check_each:
     - Does module still align with new vision?
     - Are success criteria still relevant?
   actions:
     - Update "Module Overview" if needed
     - Update "Business Value" section
     - No version bump unless content changes

**Что обновлять ПО НЕОБХОДИМОСТИ:**
5. TECH_STACK.md:
   check_if:
     - New vision requires different technologies
     - Example: "Real-time collaboration" → need WebSockets
   actions:
     - Add required technologies
     - Explain why needed for new vision
     - Version: MINOR bump

6. ARCHITECTURE.md:
   check_if:
     - New features require architectural changes
   actions:
     - Update system overview
     - Add new components if needed
     - Version: MINOR or MAJOR depending on changes

---

### Триггер B: Добавление Новой Фичи

**Когда происходит:**
- User says: "Добавь функцию X"
- User says: "Я хочу чтобы пользователи могли Y"
- During brainstorming/planning

**Workflow:**
Step 1: INTAKE (Gather Information)
  questions_to_ask:
    - "Опиши фичу подробнее: что она должна делать?"
    - "Для кого эта фича? (какой user persona)"
    - "Зачем нужна? (какую проблему решает)"
    - "Когда нужна? (MVP / Phase 1 / Phase 2 / Future)"
    - "Must Have / Should Have / Nice to Have?"
  
  record_answers_to: temp_feature_description.txt

Step 2: EVALUATE (Check Feasibility)
  check_files:
    - PROJECT_ESSENCE.md: 
        question: "Соответствует ли vision?"
        if_no: WARN user, discuss
    
    - TECH_STACK.md: 
        question: "Есть ли нужные технологии?"
        if_no: "Need to add [technology]?"
    
    - ARCHITECTURE.md: 
        question: "Вписывается в архитектуру?"
        if_no: "Need architectural change?"
    
    - ROADMAP.md: 
        question: "Есть ли место в timeline?"
        if_no: WARN "MVP already full, add to Phase 1?"
  
  create_impact_report:
    template: |
      📊 FEATURE IMPACT ANALYSIS
      
      Feature: [name]
      Priority: [Must/Should/Nice]
      Phase: [MVP/P1/P2]
      
      ✅ FEASIBILITY:
      - Vision aligned: YES/NO
      - Tech available: YES/NO
      - Architecture fit: YES/NO
      - Timeline: [estimate] days
      
      ⚠️ CONCERNS:
      - [list any issues]
      
      📝 DEPENDENCIES:
      - Requires: [list]
      - Blocks: [list]
      
      Continue? (yes/no)
  
  wait_for_user_approval: true

Step 3: UPDATE DOCUMENTS (After Approval)
  
  file: PROJECT_ESSENCE.md
  condition: IF feature is core AND Must Have
  actions:
    - Add to "CORE FEATURES (MVP)" section
    - Format: "- Feature Name - brief description"
    - Version: MINOR bump (1.2 → 1.3)
    - CHANGELOG: "Added core feature: [name]"
  
  file: PRD.md
  condition: ALWAYS (for any new feature)
  actions:
    - Find last feature number (e.g., 4.8)
    - Add new section 4.9
    - Template:
        
### 4.9 [Feature Name]
        **Priority:** [Must/Should/Nice]
        **Phase:** [MVP/Phase 1/etc]
        **Effort:** [estimate]
        
        **Description:**
        [2-3 sentences explaining what and why]
        
        **User Stories:**
        
        #### US-[MODULE]-XXX: [Story Title]
        **As a** [user type]
        **I want** [action]
        **So that** [benefit]
        
        **Acceptance Criteria:**
        - [ ] Criterion 1
        - [ ] Criterion 2
        - [ ] Criterion 3
        
        **Dependencies:**
        - [list if any]
        
        **Success Criteria:**
        - [measurable outcomes]

    - Version: MINOR bump
    - CHANGELOG: "Added feature: [name] (section 4.9)"
  
  file: ROADMAP.md
  condition: ALWAYS
  actions:
    - Determine phase (from PRD Priority + User input)
    - Add to appropriate phase section:
        
### PHASE X: [Name]
        **Key Features:**
        - [ ] [Existing feature 1]
        - [ ] [Existing feature 2]
        - [ ] [NEW: Feature Name] (Priority: Must) - Status: Not Started

    - Add to MODULES BREAKDOWN table:
        
| [Feature] | Phase X | Must | 0% | Not Started | TBD | [date] | New |

    - IF adding to current phase (MVP if in MVP):
        - Recalculate completion %
        - WARN if overloading
        - Suggest timeline adjustment
    - Version: MINOR bump
    - CHANGELOG: "Added [feature] to Phase X"
  
  file: MODULES_REQUIREMENTS/[module]_requirements.md
  condition: IF new module OR addition to existing
  actions:
    if_new_module:
