# FIGMA MAKE PROMPT: ПРИНЦИПЫ ФОРМИРОВАНИЯ

**Версия:** 1.0  
**Дата:** 2025-11-16  
**Для:** UPMT Bootstrap Automation

---

## 📖 ВВЕДЕНИЕ

Этот документ описывает принципы и best practices для автоматической генерации промптов Figma Make из UPMT Raw Data.

**Цель:** Создавать промпты которые дают:
- ✅ Высококачественные визуальные прототипы
- ✅ Полное покрытие всех модулей проекта
- ✅ Консистентность дизайна
- ✅ Интерактивность и юзабилити

---

## 🎯 ПРИНЦИП 1: СПЕЦИФИЧНОСТЬ > АБСТРАКЦИЯ

### ❌ ПЛОХО (абстрактно):
```
"Make it look modern and clean"
"Use nice colors"
"Professional interface"
```

### ✅ ХОРОШО (конкретно):
```
"Primary color: #2563eb (blue) for trust, used in main CTAs and navigation"
"Typography: Inter 16px/24px for body text, weight 400"
"Spacing: 8px base grid system (16px, 24px, 32px, 48px)"
"Border radius: 8px for cards, 4px for inputs"
"Shadows: 0 1px 3px rgba(0,0,0,0.12) for default elevation"
```

### ПРАВИЛО:
- Всегда используй HEX коды вместо названий цветов
- Всегда используй px/rem вместо "large/small"
- Всегда называй конкретные шрифты вместо "modern font"
- Всегда указывай numbers: "3 columns", "5 items per page"

---

## 🎯 ПРИНЦИП 2: ПОЛНОТА ПОКРЫТИЯ

### ЧТО НУЖНО ПОКРЫТЬ:

**✅ Все модули из modules_list.md:**
```python
# Проверка покрытия
modules_in_source = get_modules_from_list()
modules_in_prompt = extract_modules_from_prompt()

missing = set(modules_in_source) - set(modules_in_prompt)
if missing:
    raise ValidationError(f"Missing modules: {missing}")
```

**✅ Все ключевые функции:**
- Минимум top 3 функции для каждого must-have модуля
- Минимум top 1 функция для should-have модулей
- UI elements для каждой функции

**✅ Все critical user flows:**
- Happy path для core functionality
- Error handling flows
- Empty states
- Success confirmations

### МЕТРИКА ПОКРЫТИЯ:

```python
coverage_score = (
    (documented_modules / total_modules) * 0.4 +
    (documented_functions / total_functions) * 0.3 +
    (documented_screens / estimated_screens) * 0.2 +
    (documented_flows / critical_flows) * 0.1
)

# Target: > 0.85 (85% coverage)
```

---

## 🎯 ПРИНЦИП 3: КОНТЕКСТНАЯ СВЯЗНОСТЬ

### Модули → Screens → Components СВЯЗАНЫ:

```
Module: "Project Management"
    ↓ (has functions)
Function: "Create new project"
    ↓ (requires screen)
Screen: "Create Project Form"
    ↓ (uses components)
Components: [Form, Input, Button, DatePicker]
    ↓ (have states)
States: [Empty, Filling, Validating, Success, Error]
```

### ❌ ПЛОХО (disconnected):
```
"Make a form"
"Add buttons"
"Show projects"
```

### ✅ ХОРОШО (connected):
```
"For the 'Create Project' function in Project Management module:
1. Create form screen with:
   - Project name input (text, required, 3-50 chars)
   - Description textarea (optional, max 500 chars)
   - Tags multi-select (from predefined list)
   - Deadline datepicker (optional, future dates only)
   - Submit button (primary, disabled until valid)

2. On submit success → redirect to Project Detail view
3. On error → show inline validation below fields"
```

### ПРАВИЛО:
Каждая описанная UI часть должна быть связана с:
- Модулем (какой module)
- Функцией (какая user action)
- User flow (откуда пришли, куда идём)

---

## 🎯 ПРИНЦИП 4: INTELLIGENT INFERENCE

### ЧТО ИНФЕРИТЬ АВТОМАТИЧЕСКИ:

#### 4.1: UI Components из Functions

**Patterns:**

```python
INFERENCE_RULES = {
    # Patterns → Components
    "create": ["Form", "Button (primary)", "Input fields"],
    "list": ["Table/Grid", "Search", "Filter", "Pagination"],
    "view": ["Detail Panel", "Header", "Action Buttons"],
    "edit": ["Form (pre-filled)", "Button (save)", "Button (cancel)"],
    "delete": ["Confirm Modal", "Button (destructive)"],
    "search": ["Search Input", "Results List", "Filter sidebar"],
    "filter": ["Dropdown", "Checkbox group", "Apply button"],
    "sort": ["Sort controls", "Column headers (clickable)"],
    "export": ["Export button", "Format selector", "Download modal"],
    "import": ["File upload", "Progress bar", "Validation feedback"],
    "share": ["Share modal", "Permission selector", "Copy link"],
    "comment": ["Comment form", "Comment list", "Reply threading"],
    "like": ["Like button", "Counter", "User list modal"],
    "notify": ["Bell icon", "Notification dropdown", "Badge counter"],
}
```

**Пример:**

```python
function = "Allow user to create and publish blog post"

# Inference:
components = infer_components(function)
# Returns:
# - Form (title, content, tags, category)
# - Rich Text Editor (for content)
# - Tag selector (multi-select)
# - Category dropdown
# - Image uploader (featured image)
# - Button (Save Draft) - secondary
# - Button (Publish) - primary
# - Preview modal
```

#### 4.2: Screens из Function Patterns

```python
SCREEN_PATTERNS = {
    "CRUD": [
        "List View (all items)",
        "Detail View (single item)",
        "Create Form",
        "Edit Form"
    ],
    "Workflow": [
        "Step 1 Screen",
        "Step 2 Screen",
        "...",
        "Review Screen",
        "Confirmation Screen"
    ],
    "Dashboard": [
        "Overview Dashboard",
        "Analytics View",
        "Quick Actions Panel"
    ]
}
```

#### 4.3: User Flows из Module Structure

```python
def infer_user_flow(module, functions):
    # CRUD pattern
    if has_create(functions) and has_read(functions):
        return [
            "Start: Landing page",
            "Action: Click 'Create New'",
            "Screen: Create form",
            "Action: Fill & Submit",
            "Screen: Detail view (new item)",
            "Success: Item created confirmation"
        ]
    
    # Workflow pattern
    if is_multi_step(functions):
        steps = identify_steps(functions)
        return create_sequential_flow(steps)
```

### ПРАВИЛО INFERENCE:
- Если паттерн распознан → использовать inference
- Если не уверен → добавить обе опции с пометкой "or"
- Всегда можно уточнить дополнительными промптами

---

## 🎯 ПРИНЦИП 5: PROGRESSIVE DETAIL

### Структура промпта: От общего к детальному

```
Level 1: Context (что строим, для кого, зачем)
    ↓
Level 2: Visual Direction (цвета, типография, стиль)
    ↓
Level 3: Structure (модули, навигация, flows)
    ↓
Level 4: Components (конкретные UI элементы)
    ↓
Level 5: States & Interactions (hover, focus, animations)
    ↓
Level 6: Edge Cases (empty states, errors, loading)
```

### ❌ ПЛОХО (всё в одной куче):
```
"Make dashboard with projects list, forms for creating, 
use blue color, navigation sidebar, buttons should have 
shadows and hover effects, also add empty states..."
```

### ✅ ХОРОШО (структурированно):
```
## VISUAL DIRECTION
[Complete section with colors, typography...]

## APPLICATION STRUCTURE
### Dashboard Module
[Complete module description...]

## KEY COMPONENTS
### Buttons
[All button variants, states, usage...]

## INTERACTION PATTERNS
### Hover States
[All hover behaviors...]
```

### ПРАВИЛО:
- Каждая секция полная и законченная
- Секции логически упорядочены
- Можно читать секцию отдельно и понимать

---

## 🎯 ПРИНЦИП 6: ACCESSIBILITY BY DEFAULT

### Включать accessibility в каждую секцию:

**Colors:**
```
Primary: #2563eb
- Contrast ratio with white: 4.56:1 ✅ (WCAG AA)
- Use for text on light backgrounds
```

**Components:**
```
Button:
- Min height: 44px (touch target)
- Focus ring: 2px solid #3b82f6 (always visible)
- ARIA label: descriptive text
```

**Interactions:**
```
Modal:
- Focus trap: yes
- Escape key: closes modal
- ARIA role: dialog
- Focus management: first interactive element
```

### ПРАВИЛО:
Для каждого interactive element указывай:
- Touch target size (min 44x44px)
- Focus behavior
- Keyboard support
- Screen reader labels

---

## 🎯 ПРИНЦИП 7: RESPONSIVE AWARENESS

### Desktop-first → Mobile adaptation

```
Desktop View (Primary):
- Sidebar navigation
- 3-column layout
- Hover states
- Drag & drop

Mobile Adaptation:
- Bottom tab navigation (sidebar → tabs)
- Single column (3 columns → 1)
- Touch targets (larger, 56px)
- Swipe gestures (drag → swipe)
```

### BREAKPOINTS:

```
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px
```

### ПРАВИЛО:
Для каждого сложного layout указывай:
- Desktop version
- Mobile adaptation
- Touch-friendly alternative
- Simplified navigation

---

## 🎯 ПРИНЦИП 8: ITERABILITY

### Промпт должен быть дополняемым:

**Initial Prompt:**
```
Core modules: Dashboard, Projects, Settings
```

**Follow-up Prompts:**
```
"Add screen for Analytics module"
"Make Projects list filterable by status"
"Add dark mode variant"
"Create onboarding flow (3 steps)"
```

### СТРУКТУРА ДЛЯ ИТЕРАЦИЙ:

```markdown
## PRIORITY SCREENS (MVP)
Create these FIRST:
1. Dashboard
2. Projects List
3. Create Project Form

## FUTURE ADDITIONS
Can be added in iterations:
- Analytics module
- User management
- Advanced filters
- ...
```

### ПРАВИЛО:
- Разделяй MVP vs Future
- Priority screens детальнее остальных
- Оставляй место для расширения

---

## 🎯 ПРИНЦИП 9: BRAND CONSISTENCY

### Если есть brand data → использовать:

```python
if exists("00_DESIGN_RAW_DATA/brand/"):
    brand = read_brand_guidelines()
    
    # Apply to prompt:
    colors = brand.get("colors")
    logo = brand.get("logo")
    voice = brand.get("voice")
    illustrations = brand.get("illustrations")
```

**В промпте:**
```
## BRAND ELEMENTS

Logo:
- Placement: Top-left corner (header)
- Size: 32x32px icon + wordmark
- Versions: Full (desktop), Icon only (mobile)

Brand Colors:
- [Use exact HEX from brand guidelines]

Brand Voice:
- Tone: [from guidelines]
- Copy style: [concise|detailed|conversational]
```

### ПРАВИЛО:
Brand data > inference > defaults

---

## 🎯 ПРИНЦИП 10: VALIDATION & QUALITY

### Quality Metrics:

```python
QUALITY_CHECKS = {
    "specificity": {
        "hex_colors": "must have HEX codes",
        "px_values": "must have pixel values",
        "font_names": "must have specific fonts"
    },
    "completeness": {
        "module_coverage": "> 90%",
        "function_coverage": "> 80%",
        "flow_coverage": "> 3 critical flows"
    },
    "structure": {
        "word_count": "> 2000 words",
        "sections": "all required sections present",
        "no_placeholders": "no {{unfilled}} variables"
    },
    "consistency": {
        "color_usage": "consistent naming",
        "spacing_scale": "consistent system",
        "component_patterns": "reusable components"
    }
}
```

### Validation Process:

```python
def validate_prompt(prompt):
    scores = {
        "specificity": check_specificity(prompt),
        "completeness": check_completeness(prompt),
        "structure": check_structure(prompt),
        "consistency": check_consistency(prompt)
    }
    
    total_score = sum(scores.values()) / len(scores)
    
    if total_score < 0.8:
        return {
            "status": "NEEDS_IMPROVEMENT",
            "issues": identify_issues(scores)
        }
    
    return {"status": "PASSED", "score": total_score}
```

### ПРАВИЛО:
- Всегда запускай validation
- Score < 0.8 → improve перед отправкой
- Issues → fix приоритетно

---

## 🎯 ПРИНЦИП 11: HUMAN READABILITY

### Промпт должен быть читаемым человеком:

**❌ ПЛОХО (machine-readable only):**
```
PRIMARY_COLOR: #2563eb
SECONDARY_COLOR: #7c3aed
FONT_PRIMARY: Inter
FONT_SIZE_BASE: 16
```

**✅ ХОРОШО (human-friendly):**
```
## VISUAL DIRECTION

### Color Strategy
**Primary:** #2563eb (Trust Blue)
- Usage: Main CTAs, primary navigation, links
- Psychological impact: Trust, professionalism, stability

**Secondary:** #7c3aed (Innovation Purple)
- Usage: Secondary actions, accents, highlights
- Psychological impact: Creativity, modern, forward-thinking
```

### ПРАВИЛО:
- Используй headers и sections
- Объясняй "почему", не только "что"
- Примеры использования
- Markdown formatting для читаемости

---

## 🎯 ПРИНЦИП 12: DATA TRACEABILITY

### Каждый элемент → источник:

```python
# Tracking sources
PROMPT_DATA = {
    "project_name": {
        "value": "Ground Control",
        "source": "metadata.yaml",
        "line": 5
    },
    "primary_color": {
        "value": "#2563eb",
        "source": "metadata.yaml:design_preferences",
        "fallback": "inferred from project_type:saas"
    },
    "dashboard_module": {
        "value": "Dashboard Module",
        "source": "modules_list.md",
        "functions": "extracted_features.md lines 45-67"
    }
}
```

### В prompt можно добавить comments:

```markdown
<!-- 
SOURCE TRACKING:
- Primary color: metadata.yaml (user specified)
- Typography: Inferred from style:modern
- Dashboard screens: Inferred from functions in extracted_features.md
- Navigation: Inferred from module count (8 modules → sidebar)
-->
```

### ПРАВИЛО:
- Трекай источник каждого решения
- Разделяй: user-specified vs inferred
- Полезно для debugging

---

## 📊 CHECKLIST КАЧЕСТВЕННОГО ПРОМПТА

### Перед сохранением проверь:

**Базовые требования:**
- [ ] Размер > 2000 слов
- [ ] Все секции заполнены
- [ ] Нет {{незаполненных}} переменных
- [ ] Все модули из modules_list включены

**Specificity:**
- [ ] Есть конкретные HEX коды цветов
- [ ] Есть конкретные px значения
- [ ] Названы конкретные шрифты
- [ ] Указаны конкретные числа (columns, items, etc)

**Completeness:**
- [ ] ≥90% модулей покрыты
- [ ] ≥80% ключевых функций покрыты
- [ ] ≥3 критических user flows описаны
- [ ] Все priority screens детально описаны

**Structure:**
- [ ] Логическая последовательность секций
- [ ] От общего к детальному
- [ ] Каждая секция standalone readable

**Consistency:**
- [ ] Единая система именования
- [ ] Консистентное использование терминов
- [ ] Reusable component patterns

**Usability:**
- [ ] Accessibility требования для всех interactive elements
- [ ] Responsive adaptations указаны
- [ ] Touch targets ≥44px
- [ ] Keyboard navigation описана

**Iterability:**
- [ ] MVP vs Future разделены
- [ ] Priority ясна
- [ ] Можно дополнять

**Quality:**
- [ ] Validation passed (score ≥0.8)
- [ ] Human readable
- [ ] Traceability maintained

---

## 🚀 ИТОГОВАЯ ФОРМУЛА

```
КАЧЕСТВЕННЫЙ ПРОМПТ = 
    Специфичность (HEX, px, названия) +
    Полнота (все модули + функции) +
    Связность (module→screen→component) +
    Inference (smart conclusions) +
    Структура (progressive detail) +
    Accessibility (by default) +
    Responsive (mobile awareness) +
    Iterability (MVP + future) +
    Brand consistency +
    Validation (quality checks) +
    Readability (human-friendly) +
    Traceability (sources)
```

### Target Score: ≥85%

**Если score < 85%:**
1. Identify weak areas
2. Improve specific sections
3. Re-validate
4. Iterate until pass

---

## 📚 ПРИМЕРЫ

### Пример 1: Хороший Module Description

```markdown
#### MODULE: Project Management
**Purpose:** Allow users to create, organize, and track projects
**Priority:** Must-have (Core functionality)

**User Actions in this module:**

1. **PM-1: Create New Project**
   - Input: Project name (text, 3-50 chars), Description (textarea, optional)
   - Output: New project created, user redirected to project detail
   - Trigger: Click "Create Project" button on Projects List

2. **PM-2: View Project List**
   - Input: None (optional: filters, search query)
   - Output: Grid of project cards (title, progress, team, due date)
   - Trigger: Navigate to Projects page

3. **PM-3: Update Project Status**
   - Input: Select status from dropdown (Planning/Active/On Hold/Complete)
   - Output: Status updated, timeline recalculated if needed
   - Trigger: Click status badge on project card or detail view

**Screens needed:**

1. **Projects List View** - Show all user's projects
   - Layout: Grid (3 columns on desktop, 1 on mobile)
   - Key elements: 
     * Search bar (top, full-width)
     * Filter controls (sidebar left, collapsible)
     * Project cards (grid, sortable)
     * Create button (floating action, bottom-right)
     * Pagination (bottom-center, 12 projects per page)
   - Actions: Create new, Filter, Sort, Search, View details

2. **Create Project Form** - Add new project
   - Layout: Centered modal (600px width)
   - Key elements:
     * Project name input (text, required, auto-focus)
     * Description textarea (4 rows, optional)
     * Team members multi-select (async search)
     * Deadline datepicker (optional, future dates only)
     * Tags input (comma-separated, max 5)
     * Submit button (primary, disabled until valid)
     * Cancel link (secondary)
   - Actions: Submit, Cancel, Add team member

3. **Project Detail View** - Full project information
   - Layout: Full page with sidebar
   - Key elements:
     * Header (title, status badge, edit button)
     * Progress bar (visual, percentage)
     * Description section
     * Task list (embedded, top 5 recent)
     * Team members (avatars, names, roles)
     * Activity timeline (right sidebar)
     * Action menu (dropdown, top-right)
   - Actions: Edit, Archive, Share, Export, Delete

**UI Components required:**
- Card (project card with image, title, meta info)
- Form (with validation, required indicators)
- Modal (for create/edit dialogs)
- Dropdown (status selector, filters)
- Multi-select (team members, tags)
- Datepicker (deadline selection)
- Button (primary, secondary, icon)
- Badge (status indicator, color-coded)
- Progress bar (linear, percentage)
- Avatar (team member, with fallback)
- Search input (with debounce, clear button)

**Data to display:**
- Project: id, name, description, status, progress (0-100%), created_date, due_date
- Team: user_id, name, avatar_url, role
- Tasks: task_id, title, status, assignee
- Activity: timestamp, user, action, details

**States to show:**
- Empty state: "No projects yet. Create your first project to get started!" with illustration and Create button
- Loading state: Skeleton cards (3x) while fetching
- Error state: "Failed to load projects. Please try again." with Retry button
- Success state: "Project created successfully!" toast notification
```

**Что делает этот пример хорошим:**
- ✅ Детальное описание каждой функции
- ✅ Конкретные layouts и размеры
- ✅ Все состояния покрыты
- ✅ Components связаны с usage
- ✅ Data structures определены
- ✅ Actions clear and specific

---

## 🎓 ОБУЧЕНИЕ И ИТЕРАЦИЯ

### Continuous Improvement:

1. **Собирай feedback:**
   - Качество Figma Make результатов
   - Что пришлось уточнять дополнительными промптами
   - Что было упущено
   - Что работало отлично

2. **Обновляй inference patterns:**
   ```python
   # Добавляй новые patterns по мере обнаружения
   NEW_PATTERN = {
       "export data": ["Export button", "Format selector", "Progress indicator"]
   }
   ```

3. **Расширяй presets:**
   ```python
   # Добавляй новые color/typography presets
   PRESETS["fintech"] = {
       "primary": "#10b981",  # Trust green
       "secondary": "#3b82f6",  # Professional blue
       ...
   }
   ```

4. **Улучшай validation:**
   ```python
   # Добавляй новые checks
   def check_interaction_completeness(prompt):
       required_interactions = ["hover", "focus", "active", "disabled"]
       ...
   ```

### Метрики успеха:

```python
SUCCESS_METRICS = {
    "figma_generation_success_rate": "> 90%",
    "iterations_needed": "< 3",
    "user_satisfaction": "> 4.5/5",
    "coverage_accuracy": "> 85%",
    "validation_pass_rate": "> 95%"
}
```

---

## ✅ ЗАКЛЮЧЕНИЕ

Следуя этим 12 принципам, автоматически генерируемые промпты будут:

1. **Специфичными** - конкретные детали, не абстракции
2. **Полными** - все модули и функции покрыты
3. **Связными** - логическая связь между элементами
4. **Умными** - intelligent inference где нужно
5. **Структурированными** - progressive detail
6. **Доступными** - accessibility by default
7. **Адаптивными** - responsive awareness
8. **Расширяемыми** - iterability built-in
9. **Брендированными** - consistency с brand
10. **Качественными** - validated scores
11. **Читаемыми** - human-friendly format
12. **Отслеживаемыми** - data traceability

**Результат:** Высококачественные визуальные прототипы из Figma Make за 2-3 часа.

---

**Применяй эти принципы при:**
- Создании нового шаблона промпта
- Обновлении существующего шаблона
- Добавлении новых inference patterns
- Валидации сгенерированных промптов
- Debugging проблем с результатами

---

**Made for UPMT v3.0.1**  
**Figma Make Integration**  
**Date:** 2025-11-16
