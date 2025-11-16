Создай визуальную таблицу статуса всех модулей проекта:

# MODULES STATUS DASHBOARD

**Last Updated:** [date]  
**Overall Progress:** XX%

| Module | Priority | Status | Progress | Owner | Target Date | Notes |
|--------|----------|--------|----------|-------|-------------|-------|
| Auth | Must | In Dev | ███████░░░ 70% | Name | 2025-MM-DD | Login works, OAuth pending |
| Profile | Must | Not Started | ░░░░░░░░░░ 0% | Name | 2025-MM-DD | Blocked by Auth |
| Dashboard | Should | Planning | ██░░░░░░░░ 20% | Name | 2025-MM-DD | Design ready |
| ... | ... | ... | ... | ... | ... | ... |

## STATUS LEGEND
- 🔴 Not Started
- 🟡 Planning
- 🟢 In Development
- 🔵 Testing
- ✅ Completed
- ⚠️ Blocked

## COMPLETION BY PHASE
**MVP (Phase 0):** XX% complete
- Auth: 70%
- Profile: 0%
Average: XX%

**Phase 1:** XX% complete
- Dashboard: 20%
Average: XX%

## RECENT UPDATES
- [Date]: Module X reached 50% completion
- [Date]: Module Y unblocked, started development

---
UPDATE THIS FILE WEEKLY or when module status changes significantly


---

## 🤖 ПРОМПТЫ ДЛЯ AI АССИСТЕНТОВ

### **Cursor - .cursorrules**

**Создать:** `AI_INSTRUCTIONS/.cursorrules`


# PROJECT RULES FOR CURSOR AI

You are working on: [Project Name]
Project Type: [Web App / Mobile App / API / etc.]
Stack: [list from TECH_STACK.md]

## MANDATORY CHECKS BEFORE ANY CODE CHANGE:
1. Read /CONTEXT_MEMORY/state.md to understand current state
2. Read relevant /MODULES_REQUIREMENTS/[module]_requirements.md
3. Check /PROJECT_CORE/04_ARCHITECTURE.md for architectural decisions

## CODE STANDARDS:
- Language: [JavaScript/TypeScript/Python/etc.]
- Style Guide: [Airbnb/Google/etc.]
- File Naming: [camelCase/kebab-case/etc.]
- Component Structure: [pattern]

## BEFORE IMPLEMENTING:
If user request conflicts with requirements:
1. STOP
2. Say: "This conflicts with [module]_requirements.md section [X]. Should we update requirements first?"
3. Wait for approval

## AFTER IMPLEMENTING:
1. Update /CONTEXT_MEMORY/state.md "LAST COMPLETED" section
2. If made architectural decision → update /CONTEXT_MEMORY/decisions.md
3. Suggest updating module progress in /PROGRESS_TRACKING/modules_status.md

## RESPONSE FORMAT:
