# PHASE 5.4: FIGMA MAKE PROMPT GENERATION (OPTIONAL)

**Время выполнения:** 20-30 минут (автономно)

**Назначение:** Автоматическая генерация промпта для Figma Make из UPMT Raw Data

**⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ**

---

## ⚡ ШАГ 0: ПРОВЕРКА УСЛОВИЙ

**Спросить пользователя:**

```markdown
🎨 DESIGN PROTOTYPE GENERATION

Хочешь сгенерировать визуальный прототип интерфейса через Figma Make?

**Что это даёт:**
- ✅ Автоматический MVP интерфейс за 2-3 часа
- ✅ Интерактивный кликабельный прототип
- ✅ Все модули визуализированы
- ✅ Рабочий код как стартовая точка
- ✅ Design Raw Data для PHASE 5.5

**Что нужно:**
- Figma аккаунт (Professional план $16/мес для Figma Make)
- 2-3 часа на итерации в Figma Make

**Выбери:**
1. ✅ YES - Сгенерировать промпт для Figma Make (рекомендуется)
2. ⏭️ NO - Пропустить, создать дизайн позже
```

**ЕСЛИ YES:**
- ✅ Продолжай PHASE 5.4

**ЕСЛИ NO:**
- ⏭️ SKIP → Переход к PHASE 5.5 (или пропуск если нет design data)

---

## 📋 ИНСТРУКЦИИ (если продолжаем)

### ШАГ 1: Сбор данных для промпта (5 минут)

**1.1: Прочитай источники:**

```python
# Основные источники
project_essence = read_file("docs/core/00_PROJECT_ESSENCE.md")
extracted_features = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")
modules_list = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")
metadata = read_yaml("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")
tech_stack = read_file("verification/final-tech-stack.md")
synthesis = read_file("synthesized-project-data.md")

# Опциональные
if exists("UPMT/bootstrap/00_DESIGN_RAW_DATA/design-metadata.yaml"):
    design_metadata = read_yaml("UPMT/bootstrap/00_DESIGN_RAW_DATA/design-metadata.yaml")
```

**1.2: Извлеки ключевые данные:**

```python
prompt_data = {
    "project": {
        "name": metadata["project_name"],
        "description": project_essence["description"],
        "type": metadata["project_type"],
        "target_audience": project_essence["target_audience"],
        "unique_value": project_essence["unique_value_proposition"]
    },
    "design": {
        "style": metadata.get("design_preferences", {}).get("style", "modern, clean"),
        "colors": metadata.get("design_preferences", {}).get("colors", {}),
        "typography": metadata.get("design_preferences", {}).get("typography", {}),
        "inspiration": metadata.get("design_preferences", {}).get("inspiration", [])
    },
    "modules": parse_modules(modules_list, extracted_features),
    "tech_stack": parse_tech_stack(tech_stack),
    "navigation": infer_navigation_from_modules(modules_list)
}
```

---

### ШАГ 2: Генерация промпта (10-15 минут)

**2.1: Используй шаблон**

Прочитай шаблон:
```python
template = read_file("UPMT/prompts/templates/figma-make-prompt-template.md")
```

**2.2: Заполни переменные**

Замени все `{{переменные}}` реальными данными:

```python
def fill_template(template, data):
    # PROJECT CONTEXT
    template = template.replace("{{project_name}}", data["project"]["name"])
    template = template.replace("{{project_description}}", data["project"]["description"])
    template = template.replace("{{target_audience}}", data["project"]["target_audience"])
    template = template.replace("{{unique_value_proposition}}", data["project"]["unique_value"])
    template = template.replace("{{project_type}}", data["project"]["type"])
    
    # VISUAL DIRECTION
    template = template.replace("{{visual_style_description}}", data["design"]["style"])
    template = template.replace("{{primary_color_hex}}", data["design"]["colors"].get("primary", "#2563eb"))
    template = template.replace("{{secondary_color_hex}}", data["design"]["colors"].get("secondary", "#7c3aed"))
    
    # MODULES SECTION
    modules_content = generate_modules_section(data["modules"])
    template = template.replace("{{modules_section}}", modules_content)
    
    # NAVIGATION
    navigation_content = generate_navigation_section(data["navigation"])
    template = template.replace("{{navigation_section}}", navigation_content)
    
    # Продолжай для всех переменных...
    
    return template
```

**2.3: Генерация модулей секции**

Для каждого модуля из `modules_list.md`:

```python
def generate_modules_section(modules):
    output = ""
    
    for module in modules:
        output += f"""
#### MODULE: {module["name"]}
**Purpose:** {module["description"]}
**Priority:** {module["priority"]}

**User Actions in this module:**
"""
        # Извлеки функции этого модуля из extracted_features
        functions = get_functions_for_module(module["name"])
        
        for func in functions:
            output += f"""
- {func["id"]}: {func["description"]}
  - Input: {infer_input(func)}
  - Output: {infer_output(func)}
  - Trigger: {infer_trigger(func)}
"""
        
        # Инференс UI компонентов из функций
        screens = infer_screens_from_functions(functions)
        components = infer_components_from_functions(functions)
        
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
```

**2.4: Intelligent Inference**

Используй smart логику для вывода деталей:

```python
def infer_components_from_functions(functions):
    """Автоматический вывод UI компонентов из функций"""
    components = set()
    
    for func in functions:
        desc = func["description"].lower()
        
        # Инференс на основе ключевых слов
        if "create" in desc or "add" in desc:
            components.add(("Button", "create action"))
            components.add(("Form", "data input"))
        
        if "list" in desc or "view all" in desc:
            components.add(("Table", "data display"))
            components.add(("Card", "item preview"))
        
        if "search" in desc:
            components.add(("Search Input", "filtering"))
        
        if "delete" in desc:
            components.add(("Confirm Modal", "destructive action"))
        
        if "edit" in desc or "update" in desc:
            components.add(("Form", "data editing"))
            components.add(("Button", "save action"))
        
        if "filter" in desc:
            components.add(("Dropdown", "filter options"))
        
        # Продолжай для других паттернов...
    
    return [{"name": name, "usage": usage} for name, usage in components]

def infer_screens_from_functions(functions):
    """Вывод необходимых экранов из функций"""
    screens = []
    
    # Анализируй паттерны функций
    has_list = any("list" in f["description"].lower() for f in functions)
    has_create = any("create" in f["description"].lower() for f in functions)
    has_detail = any("view" in f["description"].lower() for f in functions)
    has_edit = any("edit" in f["description"].lower() for f in functions)
    
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
    # Основные модули → primary navigation
    primary_modules = [m for m in modules if m.get("priority") == "must_have"]
    
    # Вторичные → secondary/dropdown
    secondary_modules = [m for m in modules if m.get("priority") != "must_have"]
    
    return {
        "type": "sidebar" if len(primary_modules) > 4 else "top_nav",
        "primary": primary_modules,
        "secondary": secondary_modules
    }
```

---

### ШАГ 3: Дополнительные секции (5 минут)

**3.1: Color Strategy**

Если цвета не заданы в metadata, используй умные дефолты:

```python
def get_color_palette(project_type, design_prefs):
    """Подбор цветовой палитры по типу проекта"""
    
    presets = {
        "saas": {
            "primary": "#2563eb",  # Blue - trustworthy
            "secondary": "#7c3aed",  # Purple - innovative
            "accent": "#10b981"  # Green - success
        },
        "e-commerce": {
            "primary": "#ea580c",  # Orange - energetic
            "secondary": "#dc2626",  # Red - urgent
            "accent": "#16a34a"  # Green - deals
        },
        "dashboard": {
            "primary": "#0891b2",  # Cyan - analytical
            "secondary": "#6366f1",  # Indigo - data
            "accent": "#f59e0b"  # Amber - highlight
        }
        # ... другие presets
    }
    
    return presets.get(project_type, presets["saas"])
```

**3.2: Typography**

```python
def get_typography_system(style):
    """Подбор типографики"""
    
    systems = {
        "modern": {
            "primary": "Inter",
            "body": "Inter",
            "mono": "JetBrains Mono"
        },
        "elegant": {
            "primary": "Playfair Display",
            "body": "Source Sans Pro",
            "mono": "Fira Code"
        },
        "playful": {
            "primary": "Nunito",
            "body": "Nunito",
            "mono": "Space Mono"
        }
    }
    
    return systems.get(style, systems["modern"])
```

**3.3: Spacing & Layout**

```python
def get_spacing_system():
    """8px base spacing system"""
    base = 8
    return {
        "xs": base * 0.5,
        "sm": base,
        "md": base * 2,
        "lg": base * 3,
        "xl": base * 4,
        "2xl": base * 6
    }
```

---

### ШАГ 4: Генерация User Flows (5 минут)

**Создай 3-5 ключевых user flows:**

```python
def generate_user_flows(modules):
    """Генерация примеров user flows из модулей"""
    flows = []
    
    for module in modules[:3]:  # Top 3 priority modules
        functions = get_functions_for_module(module["name"])
        
        # Определи типичный flow для этого модуля
        if has_crud_pattern(functions):
            flows.append(generate_crud_flow(module, functions))
        elif has_workflow_pattern(functions):
            flows.append(generate_workflow_flow(module, functions))
        
    return flows

def generate_crud_flow(module, functions):
    """CRUD flow: Create → View → Edit → Delete"""
    return {
        "name": f"{module['name']} Management",
        "steps": [
            {"screen": f"{module['name']} List", "action": "Click 'Create New'"},
            {"screen": "Create Form", "action": "Fill details & Submit"},
            {"screen": "Detail View", "action": "View created item"},
            {"screen": "Detail View", "action": "Click 'Edit'"},
            {"screen": "Edit Form", "action": "Update & Save"},
            {"screen": "Detail View", "action": "Confirm changes"}
        ]
    }
```

---

### ШАГ 5: Валидация промпта (3 минуты)

**Проверь качество:**

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

# Запусти валидацию
issues = validate_prompt(filled_prompt)

if issues:
    print("⚠️ PROMPT VALIDATION ISSUES:")
    for issue in issues:
        print(f"   - {issue}")
    print("\nПродолжить с этими issues? (yes/fix)")
else:
    print("✅ Prompt validation passed!")
```

---

### ШАГ 6: Сохранение промпта (2 минуты)

**Сохрани в структуру UPMT:**

```python
# Основной файл
save_file(
    "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT.md",
    filled_prompt
)

# Версионированная копия (для истории итераций)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
save_file(
    f"UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/iterations/prompt_{timestamp}.md",
    filled_prompt
)

# Также сохрани в удобное место для копирования
save_file(
    "FIGMA_MAKE_PROMPT.md",  # В корне для легкого доступа
    filled_prompt
)
```

**Создай README с инструкциями:**

```markdown
# FIGMA MAKE PROMPT - READY TO USE

## 📋 NEXT STEPS

1. **Открой Figma Make:**
   - https://www.figma.com/
   - Перейди в Figma Make (требуется Professional план)

2. **Скопируй промпт:**
   ```bash
   cat FIGMA_MAKE_PROMPT.md | pbcopy  # macOS
   cat FIGMA_MAKE_PROMPT.md | xclip   # Linux
   ```

3. **Вставь в Figma Make:**
   - New Project → Start from Prompt
   - Paste full prompt
   - Click "Generate"

4. **Итерируй:**
   - Проверь результат
   - Уточни через дополнительные промпты
   - "Add screen for X"
   - "Change color to Y"
   - "Make component Z more prominent"

5. **Экспорт результата:**
   - Screens → Export as PNG → `00_DESIGN_RAW_DATA/figma-make/exports/`
   - Figma file → Share link → Add to `figma-links.md`
   - Design tokens → Extract → `design-tokens.json`

6. **Запусти PHASE 5.5:**
   - После экспорта → Continue bootstrap
   - PHASE 5.5 обработает результаты Figma Make
   - Создаст финальную design документацию

---

**Полезные команды для Figma Make:**

"Add screen showing [functionality]"
"Change primary color to [HEX]"
"Make buttons more prominent"
"Add empty state for [screen]"
"Create responsive mobile version"
"Add dark mode variant"
"Improve spacing on [screen]"
```

---

### ШАГ 7: Показать пользователю (5 минут)

```markdown
✅ PHASE 5.4 COMPLETE - FIGMA MAKE PROMPT GENERATED!

**Сгенерированный промпт:**
- Файл: `FIGMA_MAKE_PROMPT.md`
- Размер: [N] слов
- Модулей: [M]
- Screens: ~[K] (estimated)

**Валидация:**
[показать результаты валидации]

**Что включено:**
✅ Project context
✅ Visual direction (colors, typography)
✅ All [M] modules with functions
✅ Navigation structure
✅ Component requirements
✅ [N] user flows
✅ Accessibility requirements
✅ Responsive guidelines

---

**🎯 NEXT STEPS:**

1. **Прочитай промпт:**
   ```
   cat FIGMA_MAKE_PROMPT.md
   ```

2. **Скопируй в Figma Make:**
   - Открой https://www.figma.com/
   - Figma Make → New Project
   - Paste prompt → Generate

3. **Итерируй 2-3 часа:**
   - Улучшай через дополнительные промпты
   - Экспортируй результат

4. **После Figma Make:**
   - Экспорт → `00_DESIGN_RAW_DATA/figma-make/exports/`
   - Continue bootstrap → PHASE 5.5

---

**Хочешь review промпта перед использованием? (yes/no/continue)**
```

**ЕСЛИ yes:**
- Покажи первые 100 строк промпта
- "Want to see more? (yes/full/continue)"

**ЕСЛИ no ИЛИ continue:**
- Переход к следующей фазе

---

## 💾 CHECKPOINT

**⚠️ КРИТИЧНО: Checkpoint после завершения PHASE 5.4:**

**1. Сохранить JSON Checkpoint:**

```python
save_checkpoint(
    phase_number=5.4,
    phase_name="PHASE 5.4: Figma Make Prompt",
    batch=None,
    state={
        "current_action": "Figma Make prompt generated",
        "files_created": [
            "FIGMA_MAKE_PROMPT.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/FIGMA_MAKE_PROMPT.md",
            "UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/README.md"
        ],
        "word_count": word_count,
        "modules_count": len(modules),
        "validation_status": "passed" if not issues else "with_warnings"
    }
)
```

**2. Git Checkpoint:**

```bash
git add FIGMA_MAKE_PROMPT.md
git add UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 5.4 complete - Figma Make prompt generated

- Word count: [N]
- Modules: [M]
- Estimated screens: [K]
- Validation: [passed|warnings]

Ready for Figma Make prototype generation."
git push
```

**Показать итоги:**

```markdown
✅ PHASE 5.4 COMPLETE

**Figma Make Prompt:**
- ✅ Generated and validated
- ✅ Saved in multiple locations
- ✅ README with instructions

**Next Steps:**
1. Use prompt in Figma Make
2. Export results to 00_DESIGN_RAW_DATA/
3. Continue to PHASE 5.5

⏱️ PHASE 5.4 завершена за [время]
```

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
→ USER ACTION REQUIRED: Work with Figma Make
→ After export: PHASE 5.5 (Design System) OR PHASE 5.7 (Backend)
→ Прочитай README в UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/
```

---

**Made for UPMT v3.0.1**  
**Integrated into Bootstrap Process**
