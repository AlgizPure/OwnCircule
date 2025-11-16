# FIGMA MAKE INTEGRATION GUIDE

**Версия:** 1.0  
**Дата:** 2025-11-16  
**Статус:** Ready for Integration

---

## 📋 ОБЗОР

Интеграция Figma Make в UPMT bootstrap добавляет возможность автоматической генерации визуальных прототипов интерфейса из Raw Data.

### ЧТО ДОБАВЛЯЕТСЯ:

```
UPMT Bootstrap Flow (ДО):
PHASE 1 → PHASE 2 → PHASE 3 → PHASE 4 → PHASE 5 → PHASE 5.5 → PHASE 6 → PHASE 7 → PHASE 8

UPMT Bootstrap Flow (ПОСЛЕ):
PHASE 1 → PHASE 2 → PHASE 3 → PHASE 4 → PHASE 5 → 
→ PHASE 5.4 (NEW!) → Figma Make Work → PHASE 5.5 → PHASE 6 → PHASE 7 → PHASE 8
```

**PHASE 5.4:** Генерация промпта для Figma Make  
**User Action:** Работа с Figma Make (2-3 часа)  
**Result:** Design Raw Data для PHASE 5.5

---

## 🎯 ПРЕИМУЩЕСТВА

### Для Solo Developers:
- ✅ MVP интерфейс за 2-3 часа vs 2-3 недели дизайна
- ✅ Профессиональный вид без навыков дизайна
- ✅ Интерактивный прототип для тестирования
- ✅ Рабочий код как стартовая точка

### Для Команд:
- ✅ Быстрая визуализация для стейкхолдеров
- ✅ Единое видение интерфейса у всей команды
- ✅ Сокращение времени согласования дизайна
- ✅ Интеграция с существующим UPMT workflow

### Для Проектов:
- ✅ Полная traceability: requirements → design → code
- ✅ Контекст сохранён (не забываются функции/модули)
- ✅ Документация дизайна автоматически
- ✅ Design system готов к использованию

---

## 🏗️ АРХИТЕКТУРА РЕШЕНИЯ

### Data Flow:

```
┌─────────────────────────────────────────────────────┐
│ PHASE 1-4: Data Collection & Synthesis             │
├─────────────────────────────────────────────────────┤
│ • extracted_features.md (функции)                  │
│ • modules_list.md (модули)                         │
│ • metadata.yaml (метаданные)                       │
│ • PROJECT_SYNTHESIS.md (unified view)              │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 5.4: Prompt Generation (NEW!)                │
├─────────────────────────────────────────────────────┤
│ INPUT:                                              │
│ • All PHASE 1-4 outputs                            │
│ • Template: FIGMA_MAKE_PROMPT_TEMPLATE.md         │
│                                                      │
│ PROCESS:                                            │
│ • Smart variable replacement                       │
│ • Intelligent inference (components, screens)      │
│ • Validation (completeness, specificity)          │
│                                                      │
│ OUTPUT:                                             │
│ • FIGMA_MAKE_PROMPT.md (3000+ words)              │
│ • Instructions for user                            │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│ USER ACTION: Figma Make Work (2-3 hours)           │
├─────────────────────────────────────────────────────┤
│ 1. Copy prompt to Figma Make                       │
│ 2. Generate initial prototype                      │
│ 3. Iterate with additional prompts                 │
│ 4. Export:                                          │
│    • Screenshots of screens                        │
│    • Design tokens (JSON)                          │
│    • Figma file link                               │
│                                                      │
│ SAVE TO:                                            │
│ • 00_DESIGN_RAW_DATA/figma-make/exports/          │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 5.5: Design System Generation                │
├─────────────────────────────────────────────────────┤
│ INPUT:                                              │
│ • Figma Make exports                               │
│ • Original Raw Data (if any)                       │
│                                                      │
│ PROCESS:                                            │
│ • Analyze Figma exports                            │
│ • Extract design tokens                            │
│ • Document components                              │
│ • Create design system                             │
│                                                      │
│ OUTPUT:                                             │
│ • docs/design/ (full design documentation)         │
└─────────────────────────────────────────────────────┘
```

---

## 📁 СТРУКТУРА ФАЙЛОВ

### Новые файлы/папки:

```
UPMT/
├── prompts/
│   ├── phases/
│   │   └── phase-5.4-figma-prompt.md     # НОВАЯ ФАЗА
│   └── templates/
│       └── figma-make-prompt-template.md  # ШАБЛОН ПРОМПТА
│
└── bootstrap/
    └── 00_DESIGN_RAW_DATA/
        └── figma-make/                     # НОВАЯ ПАПКА
            ├── README.md                   # Инструкции
            ├── FIGMA_MAKE_PROMPT.md       # Сгенерированный промпт
            ├── exports/                    # Результаты Figma Make
            │   ├── screens/
            │   │   ├── 01-dashboard.png
            │   │   ├── 02-projects.png
            │   │   └── ...
            │   ├── design-tokens.json
            │   └── figma-link.md
            └── iterations/                 # История промптов
                ├── prompt_20251116_140000.md
                └── ...
```

---

## 🔧 ИНТЕГРАЦИЯ В BOOTSTRAP

### ШАГ 1: Добавить PHASE 5.4 в оркестратор

**Файл:** `UPMT/prompts/orchestrator.md`

**Найти секцию PHASE 5:**

```markdown
#### PHASE 5: DOCUMENTATION GENERATION
...
```

**Добавить ПОСЛЕ PHASE 5, ПЕРЕД PHASE 5.5:**

```markdown
#### PHASE 5.4: FIGMA MAKE PROMPT (OPTIONAL)

**Файл:** `UPMT/prompts/phases/phase-5.4-figma-prompt.md`

**⚠️ ОПЦИОНАЛЬНАЯ ФАЗА - спрашивает пользователя:**
"Хочешь сгенерировать визуальный прототип через Figma Make?"

**Если YES:**
- Генерирует промпт из Raw Data
- Сохраняет в `00_DESIGN_RAW_DATA/figma-make/`
- Инструктирует пользователя работать с Figma Make
- Ждёт экспорта результатов

**Если NO:**
- SKIP → переход к PHASE 5.5

**Выход:**
- ✅ `FIGMA_MAKE_PROMPT.md` (3000+ слов)
- ✅ Инструкции для пользователя

**User Action Required:**
Работа с Figma Make (2-3 часа) → Export в 00_DESIGN_RAW_DATA/

**Checkpoint:** Коммит после генерации промпта

```bash
git commit -m "docs(bootstrap): PHASE 5.4 complete - Figma Make prompt generated"
```

**После User Action:**
→ Переход к PHASE 5.5 (которая обработает Figma exports)
```

---

### ШАГ 2: Обновить PHASE 5.5

**Файл:** `UPMT/prompts/phases/phase-5.5-design.md`

**В ШАГ 0: ПРОВЕРКА УСЛОВИЙ добавить:**

```markdown
**0.3: Проверь наличие Figma Make exports:**

```python
if exists("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/"):
    figma_exports = list_files("UPMT/bootstrap/00_DESIGN_RAW_DATA/figma-make/exports/screens/")
    if len(figma_exports) > 0:
        print(f"✅ Found {len(figma_exports)} Figma Make exports")
        use_figma_data = True
```

**IF use_figma_data:**
- Приоритет Figma exports over other design data
- Извлечь design tokens из Figma
- Использовать screenshots как reference
```

---

### ШАГ 3: Обновить README в 00_DESIGN_RAW_DATA

**Файл:** `UPMT/bootstrap/00_DESIGN_RAW_DATA/README_UPMT_design_raw_data.md`

**Добавить секцию:**

```markdown
## 🎨 FIGMA MAKE INTEGRATION (НОВОЕ!)

### Автоматическая генерация прототипа

UPMT может автоматически создать промпт для Figma Make:

**Workflow:**
1. **Bootstrap генерирует промпт** (PHASE 5.4)
   - Из extracted_features.md
   - Из modules_list.md
   - Из metadata.yaml
   
2. **Ты работаешь с Figma Make** (2-3 часа)
   - Копируешь промпт
   - Генерируешь в Figma Make
   - Итерируешь
   
3. **Экспортируешь результат**
   - Screenshots → `figma-make/exports/screens/`
   - Design tokens → `figma-make/exports/design-tokens.json`
   - Figma link → `figma-make/exports/figma-link.md`
   
4. **Bootstrap обрабатывает** (PHASE 5.5)
   - Анализирует exports
   - Создаёт design документацию

**Преимущества:**
- MVP интерфейс за 2-3 часа
- Все модули визуализированы
- Интерактивный прототип
- Рабочий код

### Структура figma-make/

```
figma-make/
├── FIGMA_MAKE_PROMPT.md      # Сгенерированный промпт
├── README.md                  # Инструкции
├── exports/                   # Результаты Figma Make
│   ├── screens/              # PNG screenshots
│   ├── design-tokens.json    # Извлечённые tokens
│   └── figma-link.md         # Ссылка на Figma файл
└── iterations/                # История промптов
    └── prompt_*.md
```
```

---

### ШАГ 4: Обновить алиасы сценариев

**Файлы:** `UPMT/start/1.1.md`, `1.2.md`, `1.3.md`, `1.4.md`

**Найти секцию с перечислением фаз:**

```markdown
**⚙️ Bootstrap Process (X Phases):**
1. **PHASE 1:** Analysis
2. **PHASE 2:** Interview
3. **PHASE 3:** Tech Verification
4. **PHASE 4:** Synthesis
5. **PHASE 5:** Documentation
6. **PHASE 5.5:** Design (conditional)
...
```

**Обновить на:**

```markdown
**⚙️ Bootstrap Process (11 Phases):**
1. **PHASE 1:** Analysis
2. **PHASE 2:** Interview
3. **PHASE 3:** Tech Verification
4. **PHASE 4:** Synthesis
5. **PHASE 5:** Documentation
6. **PHASE 5.4:** Figma Make Prompt (optional)     ← НОВАЯ ФАЗА
7. **PHASE 5.5:** Design (conditional)
8. **PHASE 5.7:** Backend (conditional)
9. **PHASE 6:** Setup Instructions
10. **PHASE 7:** Validation
11. **PHASE 8:** Final Report
12. **PHASE 9:** Project Cleanup (optional)
```

---

### ШАГ 5: Создать шаблон промпта

**Файл:** `UPMT/prompts/templates/figma-make-prompt-template.md`

Скопировать содержимое из `FIGMA_MAKE_PROMPT_TEMPLATE.md` (уже создан).

---

### ШАГ 6: Обновить VERSION_HISTORY.md

**Файл:** `UPMT/VERSION_HISTORY.md`

**Добавить новую версию:**

```markdown
## v2.2.2 (2025-11-16) - Figma Make Integration

**Статус:** Current  
**Тип:** MINOR RELEASE - Feature Addition

### 🎯 Цели Релиза

- **FIGMA MAKE INTEGRATION:** Автоматическая генерация визуальных прототипов
- **DESIGN AUTOMATION:** Сокращение времени на создание MVP интерфейса с 2-3 недель до 2-3 часов
- **SMART PROMPT GENERATION:** Интеллектуальная генерация промптов из Raw Data
- **SEAMLESS WORKFLOW:** Интеграция Figma Make в существующий bootstrap процесс

### 🏗️ Что Добавлено

#### 1. PHASE 5.4: Figma Make Prompt Generation
**Файл:** `UPMT/prompts/phases/phase-5.4-figma-prompt.md`

**Функциональность:**
- Автоматическая генерация промптов для Figma Make (3000+ слов)
- Smart variable replacement из UPMT Raw Data
- Intelligent inference:
  - UI компонентов из функций
  - Screens из паттернов функций
  - Navigation структуры из модулей
  - User flows из CRUD/workflow паттернов
- Валидация промпта (completeness, specificity)
- Сохранение с версионированием

#### 2. Prompt Template
**Файл:** `UPMT/prompts/templates/figma-make-prompt-template.md`

**Секции:**
- Project Context (название, описание, аудитория)
- Visual Direction (colors, typography, spacing, shadows)
- Application Structure (модули, screens, components)
- Navigation Structure (sidebar/top-nav, flows)
- Key Components (forms, data display, feedback)
- Responsive Behavior (breakpoints, adaptations)
- Interaction Patterns (hover, focus, micro-interactions)
- Accessibility Requirements (WCAG compliance)
- Technical Constraints (framework, browsers, performance)
- Special Features (dark mode, i18n, auth, onboarding)
- Priority Screens (MVP must-haves)
- Example User Flows (step-by-step)

#### 3. New Directory Structure
```
UPMT/bootstrap/00_DESIGN_RAW_DATA/
└── figma-make/              # NEW
    ├── README.md
    ├── FIGMA_MAKE_PROMPT.md
    ├── exports/
    │   ├── screens/
    │   ├── design-tokens.json
    │   └── figma-link.md
    └── iterations/
```

#### 4. Integration Docs
**Файлы:**
- `FIGMA_MAKE_INTEGRATION_GUIDE.md` - Полное руководство по интеграции
- `FIGMA_MAKE_PRINCIPLES.md` - Принципы формирования промптов
- Updated README в `00_DESIGN_RAW_DATA/`

### 📊 Statistics

**Новые файлы:**
- 1 новая фаза: phase-5.4-figma-prompt.md (~800 lines)
- 1 шаблон: figma-make-prompt-template.md (~650 lines)
- 3 guide документа (~1200 lines total)
- Обновлено 5 существующих файлов

**Функциональность:**
- Генерация промптов 3000+ слов
- Поддержка всех модулей из UPMT
- Intelligent inference из 10+ паттернов
- Валидация по 5 критериям

### 🔄 Changed

**Обновлены:**
- `UPMT/prompts/orchestrator.md` - добавлена PHASE 5.4
- `UPMT/prompts/phases/phase-5.5-design.md` - интеграция с Figma exports
- `UPMT/bootstrap/00_DESIGN_RAW_DATA/README_UPMT_design_raw_data.md` - новая секция
- Все алиасы сценариев (1.1-1.4.md) - обновлён счётчик фаз

**Bootstrap Flow:**
```
БЫЛО: PHASE 5 → PHASE 5.5 → PHASE 6
СТАЛО: PHASE 5 → PHASE 5.4 (optional) → [User Work] → PHASE 5.5 → PHASE 6
```

### 🎯 Impact

**Для Solo Developers:**
- ⏱️ Экономия 2-3 недели на дизайне MVP
- 🎨 Профессиональный интерфейс без дизайнерских навыков
- 🔗 Полный prototype для тестирования

**Для Команд:**
- 🚀 Быстрая визуализация для стейкхолдеров
- 🤝 Единое видение у всей команды
- 📋 Сокращение циклов согласования дизайна

**Для Проектов:**
- 📍 Traceability: requirements → design → code
- 💾 Контекст сохранён (0% потерь функций)
- 📚 Design documentation автоматически
- 🎨 Design system из коробки

### ✅ Backward Compatible

- Все существующие проекты работают без изменений
- PHASE 5.4 полностью optional
- Можно skip → работает как раньше

### 📝 Next Steps

1. Test на новом проекте с Figma Make
2. Собрать feedback на качество промптов
3. Расширить inference patterns
4. Добавить больше presets (color/typography)

### 🔗 Related

**Базируется на:**
- v2.2.1 - Design System Integration
- v2.2.0 - Backend Documentation System

**Использует:**
- Figma Make (2025 release)
- UPMT Raw Data structure
- Design system templates

---
```

---

## ✅ CHECKLIST ИНТЕГРАЦИИ

### Phase Files:
- [ ] Создан `UPMT/prompts/phases/phase-5.4-figma-prompt.md`
- [ ] Создан `UPMT/prompts/templates/figma-make-prompt-template.md`
- [ ] Создан `FIGMA_MAKE_INTEGRATION_GUIDE.md`

### Orchestrator:
- [ ] Добавлена PHASE 5.4 в `orchestrator.md`
- [ ] Обновлены checkpoint instructions
- [ ] Добавлен user action flow

### PHASE Updates:
- [ ] PHASE 5.5 обновлена (Figma exports detection)
- [ ] PHASE 5.5 приоритизирует Figma data

### Directory Structure:
- [ ] Создана папка `00_DESIGN_RAW_DATA/figma-make/`
- [ ] Создан README с инструкциями
- [ ] Созданы exports/ и iterations/ папки

### Documentation:
- [ ] README в 00_DESIGN_RAW_DATA обновлён
- [ ] Все алиасы сценариев обновлены (11 phases)
- [ ] VERSION_HISTORY.md обновлён (v2.2.2)

### Validation:
- [ ] Bootstrap test run с PHASE 5.4
- [ ] Проверка generation качества
- [ ] Проверка Figma Make compatibility

---

## 🧪 ТЕСТИРОВАНИЕ

### Test Scenario 1: New Project + Figma Make

```bash
# 1. Запуск bootstrap
./UPMT/start/1.1.md  # Новый проект, local

# 2. После PHASE 5, получи вопрос о Figma Make
# → Ответь YES

# 3. PHASE 5.4 сгенерирует промпт
# Проверь:
- FIGMA_MAKE_PROMPT.md создан
- Размер > 10KB
- Все модули включены
- Нет незаполненных {{variables}}

# 4. Работа с Figma Make
- Скопируй промпт
- Создай prototype в Figma Make
- Экспорт → 00_DESIGN_RAW_DATA/figma-make/exports/

# 5. Continue bootstrap
# PHASE 5.5 должна найти Figma exports

# 6. Проверь результат
- docs/design/ создана
- Design tokens извлечены из Figma
- Components задокументированы
```

### Test Scenario 2: Skip Figma Make

```bash
# 1. Запуск bootstrap
./UPMT/start/1.1.md

# 2. После PHASE 5, получи вопрос о Figma Make
# → Ответь NO

# 3. Bootstrap пропускает PHASE 5.4
# → Прямой переход к PHASE 5.5 или 6

# 4. Проверь
- PHASE 5.4 skipped (нет FIGMA_MAKE_PROMPT.md)
- Bootstrap продолжается нормально
- Всё работает как до интеграции
```

### Test Scenario 3: Existing Project + Figma Make

```bash
# 1. Запуск bootstrap на существующем проекте
./UPMT/start/1.2.md  # Existing project, local

# 2. PHASE 5.4 с Figma Make
# Промпт должен учитывать:
- Существующий код
- Текущий design из CSS
- Planned changes из Raw Data

# 3. Проверь промпт
- Секция "EXISTING STATE" заполнена
- Противоречия выделены
- Gaps указаны
```

---

## 🐛 TROUBLESHOOTING

### Проблема 1: Prompt слишком большой для Figma Make

**Симптом:** Figma Make не принимает промпт (>10000 слов)

**Решение:**
1. Сократить количество модулей в первой итерации
2. Разделить на 2 промпта: Core modules + Secondary modules
3. Использовать приоритеты: Must-have → Figma Make 1, Should-have → Figma Make 2

### Проблема 2: Недостаточно деталей в промпте

**Симптом:** Figma Make создаёт generic интерфейс

**Решение:**
1. Проверь metadata.yaml - заполнены ли design preferences
2. Добавь больше деталей в extracted_features (user actions)
3. Используй дополнительные промпты в Figma Make для уточнений

### Проблема 3: Незаполненные {{variables}}

**Симптом:** В промпте остались {{плейсхолдеры}}

**Решение:**
1. Проверь validation в PHASE 5.4
2. Вернись к PHASE 2 - заполни пропущенные metadata
3. Re-run PHASE 5.4 после заполнения

### Проблема 4: Фаза 5.5 не находит Figma exports

**Симптом:** PHASE 5.5 skips, хотя есть Figma exports

**Решение:**
1. Проверь путь: `00_DESIGN_RAW_DATA/figma-make/exports/screens/`
2. Убедись что файлы .png, не .jpg или другой формат
3. Проверь permissions на папку

---

## 📚 ДОПОЛНИТЕЛЬНЫЕ РЕСУРСЫ

### Для Пользователей:
- **Figma Make Documentation:** https://www.figma.com/ai/figma-make
- **Prompt Engineering Guide:** (ссылка на guide по написанию хороших промптов)
- **Figma Make Examples:** (community templates)

### Для Разработчиков UPMT:
- **Template Variables Reference:** список всех доступных переменных
- **Inference Patterns:** документация логики intelligent inference
- **Validation Rules:** детали валидации промпта

---

## 🎉 ГОТОВО К ИНТЕГРАЦИИ

Все файлы готовы. Следуй Checklist Integration выше для полной интеграции в UPMT.

После интеграции:
1. Test на новом проекте
2. Собери feedback
3. Iterate на template если нужно

---

**Integration Status:** ✅ READY  
**Estimated Integration Time:** 30-60 минут  
**Breaking Changes:** НЕТ (полностью backward compatible)

---

**Made for UPMT v3.0.1**  
**Author:** Integration Team  
**Date:** 2025-11-16
