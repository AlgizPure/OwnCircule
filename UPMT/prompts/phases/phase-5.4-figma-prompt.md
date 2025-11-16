# PHASE 5.4: FIGMA MAKE PROMPT (DUAL PROMPTING: CLAUDE WEB → FIGMA MAKE)

**Время выполнения:**
- Автоматическая часть (локально): 10-15 минут
- Claude Web (GitHub + Web search): 10-20 минут (user action)
- Figma Make работа (user): 2-3 часа (НЕ внутри этой фазы, но готовится здесь)

**Назначение:**
1. Автоматически сгенерировать базовый промт для Figma Make из UPMT Raw Data
2. Использовать двойной промптинг через Claude Sonnet 4.5 Web для улучшения промта
3. Подготовить все необходимые промты (global + per-module + iterations) для Figma Make
4. Обеспечить экспорт результатов как Design Raw Data для PHASE 5.5

**⚠️ УСЛОВНАЯ ФАЗА** - выполняется только если пользователь выбрал YES на вопрос о Figma Make

---

## 📖 КОНТЕКСТ ПЕРЕД PHASE 5.4

**⚠️ ОБЯЗАТЕЛЬНО ПРОЧИТАЙ:**

**Файлы для чтения:**
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/PROJECT_ESSENCE.md`
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md`
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md`
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml`
- `synthesized-project-data.md`
- `verification/final-tech-stack.md` (если есть)
- `UPMT/prompts/templates/figma-make-prompt-template.md` (шаблон)
- `UPMT/docs/FIGMA_MAKE_PRINCIPLES.md` (принципы качества)

**Выход этой фазы:**
- `FIGMA_MAKE_PROMPT_base.md` (локально сгенерированный)
- `global_prompt.md` (улучшенный Claude Web)
- `module_prompts/{module}.md` (per-module промты)
- `iterations/{module}_steps.md` (итерационные промты)

Эти файлы используются в Figma Make для генерации MVP прототипа.

---

## 📋 ИНСТРУКЦИИ

### ⚡ ШАГ 0: ПРОВЕРКА УСЛОВИЙ

**Спросить пользователя:**

```markdown
🎨 DESIGN PROTOTYPE GENERATION

Хочешь сгенерировать визуальный прототип интерфейса через Figma Make (AI)?

**Что это даёт:**
- ✅ Автоматический MVP интерфейс за 2-3 часа (вместо 2-3 недель)
- ✅ Интерактивный кликабельный прототип
- ✅ Все модули визуализированы
- ✅ Рабочий код как стартовая точка
- ✅ Design Raw Data для PHASE 5.5

**Что нужно:**
- Figma аккаунт (Professional план $16/мес для Figma Make)
- 2-3 часа на итерации в Figma Make
- Доступ к GitHub репозиторию (для Claude Web)

**Выбери:**
1. ✅ YES - Сгенерировать промпт для Figma Make (рекомендуется)
2. ⏭️ NO - Пропустить, создать дизайн позже
```

**ЕСЛИ YES:**
- ✅ Продолжай PHASE 5.4

**ЕСЛИ NO:**
- ⏭️ SKIP → Переход к PHASE 5.5 (или пропуск если нет design data)
- **Checkpoint PHASE 5.4 НЕ создаётся**

---

### ШАГ 1: СБОР ДАННЫХ ДЛЯ ПРОМПТА (5 минут)

**1.1: Прочитай источники:**

```python
# Основные источники
project_essence = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/PROJECT_ESSENCE.md")
extracted_features = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")
modules_list = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")
metadata = read_yaml("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")
tech_stack = read_file("verification/final-tech-stack.md")  # если есть
synthesis = read_file("synthesized-project-data.md")

# Опциональные
if exists("UPMT/bootstrap/00_DESIGN_RAW_DATA/design-metadata.yaml"):
    design_metadata = read_yaml("UPMT/bootstrap/00_DESIGN_RAW_DATA/design-metadata.yaml")
```

**1.2: Извлеки ключевые данные:**

```python
prompt_data = {
    "project": {
        "name": metadata.get("project_name", "Project"),
        "description": extract_section(project_essence, "Описание") or "",
        "type": metadata.get("project_type", "web app"),
        "target_audience": extract_section(project_essence, "Целевая аудитория") or "",
        "unique_value": extract_section(project_essence, "Ценность") or ""
    },
    "design": metadata.get("design_preferences", {}),
    "modules": parse_modules(modules_list, extracted_features),
    "tech_stack": parse_tech_stack(tech_stack) if tech_stack else {},
    "navigation": infer_navigation_from_modules(modules_list)
}
```

**1.3: Парсинг модулей и функций:**

```python
def parse_modules(modules_md, features_md):
    """Парсинг модулей из modules_list.md и связывание с функциями из extracted_features.md"""
    modules = []
    current = None
    
    for line in modules_md.splitlines():
        if line.strip().startswith(("-", "*")) or re.match(r'^\s*\d+\.', line):
            name = re.sub(r'^[\s\-\*\d\.\)]+', '', line.strip()).strip()
            current = {"name": name, "description": "", "priority": "must_have", "functions": []}
            modules.append(current)
    
    # Связывание функций с модулями
    for line in features_md.splitlines():
        if line.strip().startswith("- "):
            raw = line.strip()[2:]
            if ":" in raw:
                mod_name, desc = raw.split(":", 1)
                mod_name = mod_name.strip()
                desc = desc.strip()
                for m in modules:
                    if m["name"].lower() in mod_name.lower():
                        m["functions"].append({"id": None, "description": desc})
                        break
    
    return modules

modules_data = parse_modules(modules_list, extracted_features)
```

---

### ШАГ 2: ЛОКАЛЬНАЯ ГЕНЕРАЦИЯ БАЗОВОГО ПРОМПТА (5.4A) (10-15 минут)

**2.1: Прочитай шаблон:**

```python
template = read_file("UPMT/prompts/templates/figma-make-prompt-template.md")
```

**2.2: Заполни переменные:**

```python
def fill_template(template, data):
    """Заполнение шаблона реальными данными"""
    # PROJECT CONTEXT
    template = template.replace("{{project_name}}", data["project"]["name"])
    template = template.replace("{{project_description}}", data["project"]["description"])
    template = template.replace("{{target_audience}}", data["project"]["target_audience"])
    template = template.replace("{{unique_value_proposition}}", data["project"]["unique_value"])
    template = template.replace("{{project_type}}", data["project"]["type"])
    
    # VISUAL DIRECTION
    colors = data["design"].get("colors") or get_color_palette(data["project"]["type"], data["design"])
    typography = data["design"].get("typography") or get_typography_system(data["design"].get("style", "modern"))
    
    template = template.replace("{{visual_style_description}}", data["design"].get("style", "modern, clean"))
    template = template.replace("{{primary_color_hex}}", colors.get("primary", "#2563eb"))
    template = template.replace("{{secondary_color_hex}}", colors.get("secondary", "#7c3aed"))
    template = template.replace("{{accent_color_hex}}", colors.get("accent", "#10b981"))
    
    # MODULES SECTION
    modules_content = generate_modules_section(data["modules"])
    template = template.replace("{{modules_section}}", modules_content)
    
    # NAVIGATION
    navigation_content = generate_navigation_section(data["navigation"])
    template = template.replace("{{navigation_section}}", navigation_content)
    
    # Продолжай для всех переменных из шаблона...
    
    return template

def get_color_palette(project_type, design_prefs):
    """Умные дефолты для цветов по типу проекта"""
    presets = {
        "saas": {"primary": "#2563eb", "secondary": "#7c3aed", "accent": "#10b981"},
        "e-commerce": {"primary": "#ea580c", "secondary": "#dc2626", "accent": "#16a34a"},
        "dashboard": {"primary": "#0891b2", "secondary": "#6366f1", "accent": "#f59e0b"}
    }
    return presets.get(project_type, presets["saas"])

def get_typography_system(style):
    """Умные дефолты для типографики"""
    systems = {
        "modern": {"primary": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
        "elegant": {"primary": "Playfair Display", "body": "Source Sans Pro", "mono": "Fira Code"},
        "playful": {"primary": "Nunito", "body": "Nunito", "mono": "Space Mono"}
    }
    return systems.get(style, systems["modern"])

def generate_modules_section(modules):
    """Генерация секции модулей для промпта"""
    output = ""
    for module in modules:
        output += f"""
#### MODULE: {module["name"]}
**Purpose:** {module.get("description", "")}
**Priority:** {module.get("priority", "must_have")}

**User Actions in this module:**
"""
        for func in module.get("functions", [])[:8]:  # Top 8 функций
            output += f"""
- {func.get("id", "N/A")}: {func.get("description", "")}
  - Input: {infer_input(func)}
  - Output: {infer_output(func)}
  - Trigger: {infer_trigger(func)}
"""
        
        # Инференс UI компонентов из функций
        screens = infer_screens_from_functions(module.get("functions", []))
        components = infer_components_from_functions(module.get("functions", []))
        
        output += f"""
**Screens needed:**
"""
        for idx, screen in enumerate(screens, 1):
            output += f"""
{idx}. **{screen["name"]}** - {screen["purpose"]}
   - Layout: {screen["layout"]}
   - Key elements: {", ".join(screen["elements"])}
   - Actions: {", ".join(screen["actions"])}
"""
        
        output += f"""
**UI Components required:**
"""
        for comp in components:
            output += f"- {comp['name']} ({comp['usage']})\n"
        
        output += "\n---\n"
    return output

def infer_components_from_functions(functions):
    """Автоматический вывод UI компонентов из функций (по принципам из FIGMA_MAKE_PRINCIPLES.md)"""
    components = set()
    INFERENCE_RULES = {
        "create": [("Form", "data input"), ("Button", "create action")],
        "list": [("Table", "data display"), ("Card", "item preview"), ("Search Input", "filtering")],
        "search": [("Search Input", "filtering"), ("Results List", "display")],
        "delete": [("Confirm Modal", "destructive action"), ("Button", "delete action")],
        "edit": [("Form", "data editing"), ("Button", "save action")],
        "filter": [("Dropdown", "filter options"), ("Checkbox group", "multi-select")]
    }
    
    for func in functions:
        desc = func.get("description", "").lower()
        for pattern, comps in INFERENCE_RULES.items():
            if pattern in desc:
                components.update(comps)
    
    return [{"name": name, "usage": usage} for name, usage in components]

def infer_screens_from_functions(functions):
    """Вывод необходимых экранов из функций"""
    screens = []
    descs = [f.get("description", "").lower() for f in functions]
    
    has_list = any("list" in d or "view all" in d for d in descs)
    has_create = any("create" in d or "add" in d for d in descs)
    has_detail = any("view" in d or "detail" in d for d in descs)
    has_edit = any("edit" in d or "update" in d for d in descs)
    
    if has_list:
        screens.append({
            "name": "List View",
            "purpose": "Display all items",
            "layout": "table/grid",
            "elements": ["search bar", "filter controls", "data table/cards", "pagination"],
            "actions": ["create new", "view details", "bulk actions"]
        })
    
    if has_create or has_edit:
        screens.append({
            "name": "Create/Edit Form",
            "purpose": "Add or modify items",
            "layout": "centered form",
            "elements": ["input fields", "validation messages", "submit button"],
            "actions": ["save", "cancel", "save & continue"]
        })
    
    if has_detail:
        screens.append({
            "name": "Detail View",
            "purpose": "Show full item information",
            "layout": "detail panel",
            "elements": ["header", "content sections", "action buttons", "related data"],
            "actions": ["edit", "delete", "share", "export"]
        })
    
    return screens

def infer_navigation_from_modules(modules):
    """Вывод навигационной структуры"""
    primary_modules = [m for m in modules if m.get("priority") == "must_have"]
    secondary_modules = [m for m in modules if m.get("priority") != "must_have"]
    
    return {
        "type": "sidebar" if len(primary_modules) > 4 else "top_nav",
        "primary": primary_modules,
        "secondary": secondary_modules
    }

def generate_navigation_section(nav):
    """Генерация секции навигации"""
    output = f"""
**Primary Navigation:**
{nav["type"]}

**Navigation Items:**
"""
    for module in nav["primary"]:
        output += f"- {module['name']} → {module['name']} List View\n"
    
    if nav["secondary"]:
        output += "\n**Secondary Navigation:**\n"
        for module in nav["secondary"]:
            output += f"- {module['name']}\n"
    
    return output

filled_base_prompt = fill_template(template, prompt_data)
```

**2.3: Сохрани базовый промпт:**

```python
# Создай структуру папок
os.makedirs("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make", exist_ok=True)
os.makedirs("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/module_prompts", exist_ok=True)
os.makedirs("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/iterations", exist_ok=True)
os.makedirs("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports", exist_ok=True)
os.makedirs("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/screens", exist_ok=True)

# Сохрани базовый промпт
save_file(
    "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT_base.md",
    filled_base_prompt
)

print("✅ Базовый промпт сгенерирован: FIGMA_MAKE_PROMPT_base.md")
```

---

### ШАГ 3: DUAL PROMPTING - CLAUDE WEB (5.4B) (10-20 минут, user action)

**3.1: Подготовь промт для Claude Sonnet 4.5 Web:**

Создай файл с готовым промтом для Claude Web:

```python
claude_web_prompt = f"""
Ты — Senior UX Architect + Design Systems Engineer.

Цель: На основе UPMT данных и кода проекта подготовить НАБОР промтов для Figma Make, чтобы получить качественный MVP-прототип.

Контекст:
- Репозиторий: https://github.com/{{owner}}/{{repo}}
- Ветка: main
- Важные файлы:
  - UPMT/bootstrap/00_RAW_DATA_TEMPLATE/PROJECT_ESSENCE.md
  - UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md
  - UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md
  - UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml
  - synthesized-project-data.md
  - verification/final-tech-stack.md (если есть)
  - UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT_base.md
  - UPMT/docs/FIGMA_MAKE_PRINCIPLES.md (12 принципов качества)
  - UPMT/prompts/templates/figma-make-prompt-template.md (шаблон)

1️⃣ Прочитай ВСЕ перечисленные файлы из репозитория (и при необходимости код в src/app для лучшего контекста).

2️⃣ Применяя "12 ПРИНЦИПОВ" из FIGMA_MAKE_PRINCIPLES.md, сделай:

SECTION A: GLOBAL_PROMPT.md
- Улучшенная версия FIGMA_MAKE_PROMPT_base.md:
  - Специфичность: HEX коды, px значения, конкретные шрифты (не абстракции)
  - Полнота: все модули из modules_list.md покрыты, все ключевые функции учтены
  - Структура: от контекста → визуала → структуры → компонентов → flows → a11y → responsive
  - Validation: соответствие чеклисту качества из PRINCIPLES (опиши score и найденные issues)

SECTION B: MODULE_PROMPTS/
- Для КАЖДОГО модуля из modules_list.md:
  - отдельный промт (формат .md), включающий:
    - Purpose, Entities, User Actions (max 8 ключевых),
    - Screens (List/Detail/Create/Edit/Empty/Error),
    - Components (связанные с функциями),
    - Responsive + a11y требования,
    - Priority & notes

SECTION C: ITERATIVE_REFINEMENT/
- Для сложных или критичных модулей:
  - по 2-4 mini-промта "iteration steps", например:
    - Step 1: каркас (wireframe)
    - Step 2: визуальное оформление
    - Step 3: состояния (empty/error/loading)
    - Step 4: mobile adaptation

3️⃣ В конце дай:
- Summary: coverage (modules/functions/flows) + quality score (≥85% или нет)
- Если есть "necks": чётко перечисли

Формат ответа:
- SECTION A: GLOBAL_PROMPT.md
- SECTION B: MODULE_PROMPTS/{{module_slug}}.md
- SECTION C: ITERATIVE_REFINEMENT/{{module_slug}}_steps.md
"""

save_file(
    "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/CLAUDE_WEB_PROMPT.md",
    claude_web_prompt
)
```

**3.2: Покажи пользователю инструкции:**

```markdown
⏸️ PHASE 5.4B: CLAUDE WEB DUAL PROMPTING

**Твои действия:**

1. Открой claude.ai/code (Web версия, Sonnet 4.5)

2. Скопируй промт из файла:
   `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/CLAUDE_WEB_PROMPT.md`
   
   ⚠️ ВАЖНО: Замени {{owner}} и {{repo}} на реальные значения!

3. Вставь промт в Claude Web и дождись ответа

4. После ответа Claude Web сохрани файлы в репозиторий:
   - SECTION A → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md`
   - SECTION B → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/module_prompts/{module}.md` (для каждого модуля)
   - SECTION C → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/iterations/{module}_steps.md` (если есть)

5. Напиши "continue" в чат для продолжения

**⏱️ Это займёт 10-20 минут**
```

**⏸️ PAUSE** - жди "continue" от пользователя

**3.3: После "continue" - проверь наличие файлов:**

```python
# Проверка наличия файлов от Claude Web
required_files = [
    "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md"
]

module_prompts = list_files("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/module_prompts/")
if len(module_prompts) == 0:
    print("⚠️ WARNING: Module prompts не найдены. Продолжить с базовым промтом? (yes/no)")
    choice = ask_user()
    if choice == "no":
        # Повторить инструкции
        PAUSE

print(f"✅ Найдено файлов от Claude Web:")
print(f"   - global_prompt.md")
print(f"   - {len(module_prompts)} module prompts")
```

---

### ШАГ 4: ИНСТРУКЦИИ ДЛЯ FIGMA MAKE (user action)

**После завершения автоматической части PHASE 5.4, покажи пользователю:**

```markdown
✅ PHASE 5.4 COMPLETE - FIGMA MAKE PROMPTS READY!

**Сгенерированные промты:**
- ✅ FIGMA_MAKE_PROMPT_base.md (локально)
- ✅ global_prompt.md (Claude Web enhanced)
- ✅ {N} module prompts (per-module)
- ✅ {M} iteration steps (для сложных модулей)

**Валидация:**
[показать результаты валидации из ШАГ 5]

---

**🎯 NEXT STEPS: FIGMA MAKE WORK (2-3 часа)**

1. **Открой Figma Make:**
   - https://www.figma.com/
   - Figma Make → New Project (требуется Professional план)

2. **Сначала используй GLOBAL PROMPT:**
   - Скопируй: `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md`
   - Вставь в Figma Make → Generate
   - Это создаст базовую структуру и стиль

3. **Затем добавляй модули:**
   - По одному используй промты из `module_prompts/{module}.md`
   - Для сложных модулей используй итерационные шаги из `iterations/{module}_steps.md`

4. **Итерируй:**
   - "Add screen for [functionality]"
   - "Change primary color to [HEX]"
   - "Make buttons more prominent"
   - "Add empty state for [screen]"
   - "Create responsive mobile version"

5. **Экспорт результата:**
   - Screenshots (PNG) → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/screens/`
   - Design tokens (JSON) → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/design-tokens.json`
   - Figma file link → `UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/figma-link.md`

6. **После экспорта:**
   - Continue bootstrap → PHASE 5.5
   - PHASE 5.5 автоматически найдёт Figma exports и создаст design документацию

---

**Хочешь review промтов перед использованием? (yes/no/continue)**
```

**ЕСЛИ yes:**
- Покажи первые 100 строк `global_prompt.md`
- "Want to see more? (yes/full/continue)"

**ЕСЛИ no ИЛИ continue:**
- Переход к CHECKPOINT

---

### ШАГ 5: ВАЛИДАЦИЯ ПРОМПТА (3 минуты)

**Проверь качество по принципам из FIGMA_MAKE_PRINCIPLES.md:**

```python
def validate_prompt(prompt):
    """Валидация сгенерированного промпта"""
    issues = []
    
    # Проверка 1: Все модули покрыты
    modules_in_source = get_modules_from_list()
    modules_in_prompt = extract_modules_from_prompt(prompt)
    
    missing_modules = set(modules_in_source) - set(modules_in_prompt)
    if missing_modules:
        issues.append(f"Missing modules: {', '.join(missing_modules)}")
    
    # Проверка 2: Есть ли конкретные детали (не абстракции)
    if "{{" in prompt:
        unfilled = re.findall(r'\{\{([^}]+)\}\}', prompt)
        issues.append(f"Unfilled variables: {', '.join(unfilled)}")
    
    # Проверка 3: Минимальная длина (качественный промпт ~3000+ слов)
    word_count = len(prompt.split())
    if word_count < 2000:
        issues.append(f"Prompt too short: {word_count} words (recommended: 3000+)")
    
    # Проверка 4: Наличие ключевых секций
    required_sections = [
        "## CONTEXT & PURPOSE",
        "## VISUAL DIRECTION",
        "## APPLICATION STRUCTURE",
        "## NAVIGATION STRUCTURE",
        "## KEY COMPONENTS",
        "## USER FLOWS"
    ]
    
    for section in required_sections:
        if section not in prompt:
            issues.append(f"Missing section: {section}")
    
    # Проверка 5: Специфичность (должно быть много цифр и HEX кодов)
    has_hex_colors = bool(re.search(r'#[0-9A-Fa-f]{6}', prompt))
    has_px_values = bool(re.search(r'\d+px', prompt))
    
    if not has_hex_colors:
        issues.append("No specific colors (HEX codes) found")
    if not has_px_values:
        issues.append("No specific sizing (px values) found")
    
    return issues

# Валидация базового промта
base_issues = validate_prompt(filled_base_prompt)

# Валидация global_prompt (если есть)
if exists("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md"):
    global_prompt = read_file("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md")
    global_issues = validate_prompt(global_prompt)
else:
    global_issues = ["Global prompt not generated yet (Claude Web pending)"]

# Покажи результаты
print("📊 VALIDATION RESULTS:")
print(f"\nBase Prompt:")
if base_issues:
    for issue in base_issues:
        print(f"   ⚠️ {issue}")
else:
    print("   ✅ Passed")

if global_issues and global_issues[0] != "Global prompt not generated yet":
    print(f"\nGlobal Prompt (Claude Web):")
    if global_issues:
        for issue in global_issues:
            print(f"   ⚠️ {issue}")
    else:
        print("   ✅ Passed")
```

**Правило:**
- Если word_count < 2000 или есть критические issues (непокрытые модули, незаполненные {{variables}}) → фаза НЕ считается завершённой, требуется исправление/повторная генерация.

---

### ШАГ 6: СОЗДАНИЕ README С ИНСТРУКЦИЯМИ

**Создай README для пользователя:**

```python
readme_content = """# FIGMA MAKE PROMPTS - READY TO USE

## 📋 NEXT STEPS

1. **Открой Figma Make:**
   - https://www.figma.com/
   - Перейди в Figma Make (требуется Professional план)

2. **Используй промты в правильном порядке:**
   - Сначала: `global_prompt.md` (базовая структура и стиль)
   - Затем: `module_prompts/{module}.md` (по одному модулю)
   - Для сложных: `iterations/{module}_steps.md` (итерационные шаги)

3. **Итерируй в Figma Make:**
   - Проверь результат
   - Уточни через дополнительные промпты:
     - "Add screen for X"
     - "Change color to Y"
     - "Make component Z more prominent"
     - "Add empty state for [screen]"
     - "Create responsive mobile version"

4. **Экспорт результата:**
   - Screens → Export as PNG → `exports/screens/`
   - Figma file → Share link → `exports/figma-link.md`
   - Design tokens → Extract → `exports/design-tokens.json`

5. **Запусти PHASE 5.5:**
   - После экспорта → Continue bootstrap
   - PHASE 5.5 обработает результаты Figma Make
   - Создаст финальную design документацию

---

## 📁 СТРУКТУРА ФАЙЛОВ

```
figma-make/
├── FIGMA_MAKE_PROMPT_base.md      # Базовый промт (локально сгенерированный)
├── global_prompt.md                 # Улучшенный промт (Claude Web)
├── CLAUDE_WEB_PROMPT.md            # Промт для Claude Web (reference)
├── module_prompts/                  # Per-module промты
│   ├── {module1}.md
│   ├── {module2}.md
│   └── ...
├── iterations/                      # Итерационные промты
│   ├── {module1}_steps.md
│   └── ...
└── exports/                         # Результаты Figma Make (после работы)
    ├── screens/
    ├── design-tokens.json
    └── figma-link.md
```

---

## 💡 ПРИНЦИПЫ КАЧЕСТВА

Все промты созданы по 12 принципам из `UPMT/docs/FIGMA_MAKE_PRINCIPLES.md`:

1. Специфичность (HEX, px, конкретные шрифты)
2. Полнота (все модули покрыты)
3. Связность (module → screen → component)
4. Intelligent Inference (умные выводы)
5. Progressive Detail (от общего к детальному)
6. Accessibility by Default
7. Responsive Awareness
8. Iterability (MVP + future)
9. Brand Consistency
10. Validation & Quality
11. Human Readability
12. Data Traceability

**Target Quality Score:** ≥85%

---

**Made for UPMT v3.1+**  
**Figma Make Integration v1.0**
"""

save_file(
    "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/README.md",
    readme_content
)
```

---

## 💾 CHECKPOINT

**⚠️ КРИТИЧНО: Checkpoint после завершения автоматической части PHASE 5.4 (до начала реальной работы в Figma Make):**

**1. Сохранить JSON Checkpoint:**

```python
save_checkpoint(
    phase_number=5.4,
    phase_name="PHASE 5.4: Figma Make Prompt (Dual Prompting)",
    batch=None,
    state={
        "figma_make_selected": True,  # КРИТИЧНО для recovery логики
        "current_action": "Figma Make prompts generated (base + Claude Web enhanced)",
        "files_created": [
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT_base.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/global_prompt.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/CLAUDE_WEB_PROMPT.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/README.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/module_prompts/*",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/iterations/*"
        ],
        "word_count_base": len(filled_base_prompt.split()),
        "modules_count": len(modules_data),
        "validation_issues_base": base_issues,
        "validation_issues_global": global_issues if exists("global_prompt.md") else [],
        "claude_web_used": True,
        "user_action_required": "Figma Make work (2-3 hours)"
    }
)
```

**2. Git Checkpoint:**

**CLI mode:**
```bash
git add UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 5.4 complete - Figma Make prompts (base + Claude Web)

- Base prompt: [N] words
- Global prompt: [M] words (Claude Web enhanced)
- Modules: [K] module prompts
- Iterations: [L] iteration steps
- Validation: [passed|warnings]

Ready for Figma Make prototype generation."
git push
```

**Web mode (GitHub API):**
- ✅ Каждый PUT request автоматически создаёт коммит
- ✅ Commit message указывается в `-f message="..."`
- ✅ Checkpoint через `save_checkpoint_github()` создаст коммит

**Показать итоги:**

```markdown
✅ PHASE 5.4 COMPLETE

**Figma Make Prompts:**
- ✅ Base prompt generated and validated
- ✅ Claude Web prompts prepared
- ✅ Module prompts ready
- ✅ Iteration steps prepared
- ✅ README with instructions

**Next Steps:**
1. Use prompts in Figma Make (2-3 hours)
2. Export results to 00_DESIGN_RAW_DATA/figma-make/exports/
3. Continue to PHASE 5.5

⏱️ PHASE 5.4 завершена за [время]
```

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
→ USER ACTION REQUIRED: Work with Figma Make (2-3 hours)
→ After export: PHASE 5.5 (Design System) will process Figma exports
→ Прочитай README в UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/
```

---

**Made for UPMT v3.1+**  
**Figma Make Integration v1.0**  
**Dual Prompting: Local + Claude Web**

