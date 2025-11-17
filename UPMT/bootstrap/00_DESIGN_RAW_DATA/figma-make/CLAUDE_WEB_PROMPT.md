# CLAUDE WEB PROMPT: Улучшение Figma Make Промптов

Ты — Senior UX Architect + Design Systems Engineer.

**Цель:** На основе UPMT данных и кода проекта подготовить НАБОР промптов для Figma Make, чтобы получить качественный MVP-прототип для проекта "Свой Круг".

## Контекст проекта

- **Репозиторий:** https://github.com/AlgizPure/OwnCircule
- **Ветка:** claude/upmt-start-1-3-01NzbZsT7jYrAdgQsXszWpS4

## Важные файлы для чтения

**ОБЯЗАТЕЛЬНО прочитай ВСЕ следующие файлы из репозитория:**

1. **Raw Data & Analysis:**
   - `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md` (325 функций)
   - `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md` (15 модулей)
   - `.upmt/metadata.yaml` (метаданные проекта)

2. **Design Raw Data:**
   - `UPMT/bootstrap/00_DESIGN_RAW_DATA/screenshots/` (13 скриншотов дизайна)
   - `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT_base.md` (базовый промпт)

3. **Core Documentation:**
   - `docs/core/00_PROJECT_ESSENCE.md` (видение проекта)
   - `docs/core/01_PRD.md` (требования)
   - `docs/core/04_ARCHITECTURE.md` (архитектура)
   - `docs/core/05_GLOSSARY.md` (терминология)

4. **Module Requirements (выборочно, топ-5 модулей):**
   - `docs/requirements/module-01-mobile-app.md` (68 функций)
   - `docs/requirements/module-02-loyalty-system.md` (45 функций)
   - `docs/requirements/module-04-events.md` (28 функций)
   - `docs/requirements/module-05-cross-promo.md` (22 функции)
   - `docs/requirements/module-13-security.md` (8 функций)

5. **Tech Stack & Principles:**
   - `docs/core/03_TECH_STACK.md` (verified tech stack)
   - `.cursorrules` (development guidelines)

## Твои задачи

### TASK 1: Прочитай и проанализируй

1. Прочитай ВСЕ файлы выше через GitHub API
2. Изучи 13 скриншотов дизайна в `00_DESIGN_RAW_DATA/screenshots/`
3. Проанализируй базовый промпт `FIGMA_MAKE_PROMPT_base.md`

### TASK 2: Создай УЛУЧШЕННЫЙ GLOBAL PROMPT

На основе базового промпта создай улучшенную версию с:

**Требования к качеству:**
- ✅ **Специфичность:** Все цвета в HEX, все размеры в px, конкретные шрифты (не "красивый шрифт", а "SF Pro Display 28px/700")
- ✅ **Полнота:** Все 15 модулей из modules_list.md покрыты, все ключевые функции учтены
- ✅ **Структура:** От контекста → визуала → структуры → компонентов → flows → a11y → responsive
- ✅ **Связность:** Четкая связь module → screen → component → function
- ✅ **Умные выводы:** Автоматически определяй UI паттерны из описаний функций (например, "создать X" = форма + кнопка Save)
- ✅ **Визуальные референсы:** Используй данные из 13 скриншотов для уточнения color palette, typography, spacing

**Структура GLOBAL PROMPT:**
```markdown
# PROJECT: Свой Круг (Own Circle)

## CONTEXT & PURPOSE
[Refined from base prompt + PROJECT_ESSENCE.md]

## VISUAL DIRECTION
[Enhanced with specific HEX codes from screenshots, precise typography scale]

### Color Palette (from design screenshots)
- Primary: #XXXXXX (Tiffany Blue from screenshot analysis)
- Secondary: #XXXXXX (Charcoal from screenshots)
- Accent: #XXXXXX (Champagne Gold)
- [Extract exact colors from 13 screenshots]

### Typography (precise scale)
- Display: XXpx / XXX weight - [actual font name]
- H1-H3: [exact sizes and weights]
- Body: [exact sizes]

## APPLICATION STRUCTURE
[All 15 modules with detailed screens]

### MODULE 1: Mobile App
[Enhanced from base + module-01-mobile-app.md with all 68 functions]

### MODULE 2: Loyalty System
[From module-02-loyalty-system.md with all 45 functions]

[... остальные модули ...]

## KEY COMPONENTS
[Complete component library with variants, states, specs]

## USER FLOWS
[All critical flows with step-by-step screen transitions]

## RESPONSIVE & ACCESSIBILITY
[Detailed breakpoints, a11y requirements]

## BRAND & AESTHETICS
[Refined brand voice, illustration style from screenshots]
```

**Output:** Сохрани как `SECTION A: GLOBAL_PROMPT.md`

### TASK 3: Создай MODULE PROMPTS (per-module)

Для КАЖДОГО из топ-6 модулей (MVP critical) создай отдельный детальный промпт:

**Модули для детализации:**
1. Module 1: Mobile App (68 functions)
2. Module 2: Loyalty System (45 functions)
3. Module 3: Transactions (12 functions)
4. Module 4: Events (28 functions)
5. Module 5: Cross-Promo (22 functions)
6. Module 13: Security (8 functions)

**Формат каждого MODULE PROMPT:**
```markdown
# MODULE: [Module Name]

## Purpose
[From requirements doc]

## User Stories (top 8-12)
- As a [role], I want to [action], so that [benefit]

## Screens
### Screen 1: [Name]
**Layout:** [description]
**Components:**
- [Component 1]: [specs]
- [Component 2]: [specs]
**States:** default, loading, error, empty, success
**Interactions:** [tap/swipe/long-press behaviors]
**Data:** [what data is displayed, format]

[Repeat for all screens in module]

## Components Required
[List all UI components needed for this module with specs]

## User Flows
[Step-by-step flows for key scenarios]

## Responsive Behavior
[Mobile → tablet → desktop adaptations]

## Accessibility
[Module-specific a11y requirements]

## Priority
[must_have/should_have/nice_to_have]

## Notes
[Special considerations, dependencies, challenges]
```

**Output:** Сохрани каждый как `SECTION B: MODULE_PROMPTS/module-0X-[slug].md`

### TASK 4: Создай ITERATIVE REFINEMENT STEPS

Для 2-3 сложных модулей (Module 1, Module 2, Module 4) создай итерационные промпты:

**Формат:**
```markdown
# MODULE X: [Name] - Iteration Steps

## Step 1: Wireframe (Structure)
Prompt for Figma Make:
"Create wireframe for [Module X] with:
- Layout structure (no colors, grayscale only)
- Spacing and hierarchy
- Component placement
- Navigation elements
Focus: Information architecture, not visual design"

## Step 2: Visual Design (Style)
Prompt for Figma Make:
"Apply visual design to wireframe from Step 1:
- Color palette (Tiffany Blue primary #0ABAB5, etc.)
- Typography (SF Pro Display/Roboto)
- Shadows, borders, radius
- Icons and illustrations
Focus: Brand consistency, premium feel"

## Step 3: States & Interactions (Behavior)
Prompt for Figma Make:
"Add all component states and interactions:
- Hover, focus, active, disabled states
- Loading skeletons
- Error messages
- Empty states
- Success animations
Focus: Complete UX coverage"

## Step 4: Mobile Adaptation (Responsive)
Prompt for Figma Make:
"Adapt design for mobile (375px-428px width):
- Bottom tabs instead of sidebar
- Cards instead of tables
- Touch targets minimum 44px
- Reduced spacing
Focus: Mobile usability, thumb-friendly"
```

**Output:** Сохрани каждый как `SECTION C: ITERATIVE_REFINEMENT/module-0X-[slug]_steps.md`

## Финальный Output

В конце дай:

### Summary:
- **Coverage:** Modules covered (X/15), Functions covered (Y/325), Flows documented (Z)
- **Quality Score:** [Calculate based on specificity, completeness, structure] - Target: ≥85%
- **Screenshot Analysis:** Colors extracted ([list HEX codes]), Typography identified ([fonts and sizes]), UI patterns found ([list patterns])

### Files Created:
- `SECTION A: GLOBAL_PROMPT.md` (improved base prompt)
- `SECTION B: MODULE_PROMPTS/module-01-mobile-app.md`
- `SECTION B: MODULE_PROMPTS/module-02-loyalty-system.md`
- `SECTION B: MODULE_PROMPTS/module-03-transactions.md`
- `SECTION B: MODULE_PROMPTS/module-04-events.md`
- `SECTION B: MODULE_PROMPTS/module-05-cross-promo.md`
- `SECTION B: MODULE_PROMPTS/module-13-security.md`
- `SECTION C: ITERATIVE_REFINEMENT/module-01-mobile-app_steps.md`
- `SECTION C: ITERATIVE_REFINEMENT/module-02-loyalty-system_steps.md`
- `SECTION C: ITERATIVE_REFINEMENT/module-04-events_steps.md`

### Issues Found (if any):
- [List any gaps, inconsistencies, or ambiguities found in source data]
- [Recommendations for improvements]

---

**Important:** Формат вывода должен быть готовым для копирования в файлы. Используй markdown headers для разделения секций.

**Start working!** Прочитай файлы и создавай промпты.
