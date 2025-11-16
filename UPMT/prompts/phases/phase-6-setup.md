# PHASE 6: FINAL SETUP INSTRUCTIONS

**Время выполнения:** 15 минут (автономно)

**Назначение:** Создание инструкций по настройке AI ассистентов

---

## 📖 КОНТЕКСТ ПЕРЕД PHASE 6

**⚠️ ОБЯЗАТЕЛЬНО ПРОЧИТАЙ:**

**⚠️ КРИТИЧНО: Обработка больших файлов**

**Используй `safe_read_file()` из адаптера для автоматической обработки больших файлов.**

**Алгоритм:**
1. Для каждого файла вызывай `safe_read_file(file_path)`
2. Если файл большой (>256KB или >25000 токенов) - функция автоматически прочитает по частям
3. Объедини все части перед анализом

**Файлы для чтения:**
- `.upmt/metadata.yaml` → `safe_read_file(".upmt/metadata.yaml")`
- `docs/core/03_TECH_STACK.md` → `safe_read_file("docs/core/03_TECH_STACK.md")`
- `.cursorrules` → `safe_read_file(".cursorrules")`

**⚠️ ВАЖНО:** 
- НЕ ПРОПУСКАЙ файлы из-за размера
- Функция автоматически обработает большие файлы
- Детали алгоритма см. в `cli-adapter.md` / `web-adapter.md`

---

## 📋 ИНСТРУКЦИИ

### ШАГ 1: Создание Setup Instructions

**Создай файл:** `UPMT/bootstrap/BOOTSTRAP_CONFIG/FINAL_SETUP_INSTRUCTIONS.md`

**Содержимое:**

```markdown
# 🎯 FINAL SETUP INSTRUCTIONS

**Проект:** [название проекта]
**Дата:** [timestamp]
**Bootstrap Status:** ✅ COMPLETE

---

## ✅ ЧТО УЖЕ СДЕЛАНО

Bootstrap процесс завершён! Создана полная документация:

**📄 Документация:**
- ✅ docs/core/ (6 файлов)
- ✅ docs/requirements/ ([N] модулей)
- ✅ docs/progress/ (3 файла)
- ✅ .context/ (4 файла)
- [Если создано] ✅ docs/design/ (design system)
- [Если создано] ✅ docs/backend/ (backend documentation)
- [Если создано] ✅ docs/adr/ (architecture decisions)

**🤖 AI Configuration:**
- ✅ .cursorrules (в корне проекта)
- ✅ .upmt/metadata.yaml

**📊 Progress Tracking:**
- ✅ modules_status.md ([M] модулей)
- ✅ backlog.md ([N] функций)
- ✅ sprint_current.md

---

## 🛠️ НАСТРОЙКА AI АССИСТЕНТОВ

### 1️⃣ Cursor AI (Рекомендуется)

**Шаг 1: Открой проект в Cursor**
```bash
cd [path/to/project]
cursor .
```

**Шаг 2: Проверь .cursorrules**
- Файл `.cursorrules` уже создан в корне проекта
- Cursor автоматически подхватит его

**Шаг 3: Добавь в Cursor Rules (Settings → Cursor Settings → Rules for AI):**

Скопируй содержимое из `UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md`

**Шаг 4: Проверь работу:**
- Открой любой файл из docs/
- Спроси Cursor: "Что это за проект?"
- Cursor должен ответить с использованием данных из .cursorrules

---

### 2️⃣ Claude Code (CLI)

**Шаг 1: Установи Claude Code CLI** (если ещё нет):
```bash
npm install -g @anthropic-ai/claude-code
```

**Шаг 2: Настрой проектные правила:**

Создай `.claude-code/project-rules.md`:
```bash
mkdir -p .claude-code
cp UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md .claude-code/project-rules.md
```

**Шаг 3: Запусти Claude Code:**
```bash
cd [path/to/project]
claude
```

**Шаг 4: Проверь работу:**
```
> Прочитай .upmt/metadata.yaml и расскажи о проекте
```

---

### 3️⃣ GitHub Copilot (опционально)

**Если используешь GitHub Copilot:**

1. Убедись что `.cursorrules` в корне проекта
2. Copilot использует те же файлы для контекста

---

## 📋 РЕКОМЕНДУЕМЫЙ WORKFLOW

### Начало работы:

**1. Проверь текущий статус:**
```bash
cat docs/progress/modules_status.md
```

**2. Выбери задачу из backlog:**
```bash
cat docs/progress/backlog.md
```

**3. Обнови спринт:**
```bash
cat docs/progress/sprint_current.md
```

**4. Спроси AI ассистента:**
```
"Какой модуль мне стоит реализовать первым?"
"Покажи требования для модуля [название]"
"Помоги спланировать implementation для [функция]"
```

---

### Во время разработки:

**AI ассистент знает:**
- ✅ Все модули проекта (из modules_list.md)
- ✅ Все функции (из extracted_features.md)
- ✅ Tech stack (из 03_TECH_STACK.md)
- ✅ Архитектуру (из 04_ARCHITECTURE.md)
- ✅ Requirements (из docs/requirements/)
- [Если создано] ✅ Design system (из docs/design/)
- [Если создано] ✅ Backend entities & API (из docs/backend/)

**Можешь спрашивать:**
```
"Как реализовать [функция] согласно requirements?"
"Какие компоненты нужны для [модуль]?"
"Покажи API endpoints для [entity]"
"Какие цвета использовать для [элемент]?"
```

---

### После завершения задачи:

**1. Обнови прогресс:**
```bash
# Обнови статус в modules_status.md
# Закрой задачу в backlog.md
# Залогируй в .context/changes_log.md
```

**2. Спроси AI:**
```
"Обнови modules_status.md - модуль [название] завершён на X%"
"Переме<br/>щи задачу [название] из backlog в completed"
"Залогируй изменения в changes_log"
```

---

## 🎯 СЛЕДУЮЩИЕ ШАГИ

### Immediate (сейчас):

1. **Настрой AI ассистента** (Cursor или Claude Code)
2. **Прочитай core documentation:**
   - `docs/core/00_PROJECT_ESSENCE.md` - суть проекта
   - `docs/core/01_PRD.md` - requirements
   - `docs/core/02_ROADMAP.md` - план развития
   - `docs/core/03_TECH_STACK.md` - технологии
   - `docs/core/04_ARCHITECTURE.md` - архитектура

3. **Выбери первый модуль:**
   - Открой `docs/progress/modules_status.md`
   - Выбери модуль с наивысшим приоритетом
   - Прочитай его requirements: `docs/requirements/[module]_requirements.md`

### Short-term (неделя 1-2):

1. **Setup development environment:**
   - Инициализируй проект (`npm init` / `python -m venv` / etc)
   - Установи зависимости из tech stack
   - Настрой linter, formatter

2. **Начни с foundation:**
   - Настрой базовую структуру проекта
   - Реализуй первый модуль (обычно Auth или Core)

3. **Используй AI для помощи:**
   ```
   "Помоги настроить [технология] согласно tech stack"
   "Сгенерируй базовую структуру для модуля [название]"
   "Покажи implementation plan для [функция]"
   ```

### Long-term (месяц 1-3):

1. **Следуй roadmap** (`docs/core/02_ROADMAP.md`)
2. **Используй sprint planning** (`docs/progress/sprint_current.md`)
3. **Обновляй прогресс** (`modules_status.md`, `backlog.md`)

---

## 📚 ПОЛЕЗНЫЕ ССЫЛКИ

**Внутренняя документация:**
- [Project Essence](../../../docs/core/00_PROJECT_ESSENCE.md)
- [PRD](../../../docs/core/01_PRD.md)
- [Roadmap](../../../docs/core/02_ROADMAP.md)
- [Tech Stack](../../../docs/core/03_TECH_STACK.md)
- [Architecture](../../../docs/core/04_ARCHITECTURE.md)
- [System Guide](../../../docs/core/99_SYSTEM_GUIDE.md)

**Progress Tracking:**
- [Modules Status](../../../docs/progress/modules_status.md)
- [Current Sprint](../../../docs/progress/sprint_current.md)
- [Backlog](../../../docs/progress/backlog.md)

**Context:**
- [State](../../../.context/state.md)
- [Decisions](../../../.context/decisions.md)
- [Insights](../../../.context/insights.md)
- [Changes Log](../../../.context/changes_log.md)

---

## 🎉 ПОЗДРАВЛЯЕМ!

Bootstrap процесс завершён! У вас есть:
- ✅ Полная документация ([N]+ файлов)
- ✅ Настроенные AI ассистенты
- ✅ Чёткий plan развития
- ✅ Систематизированные requirements ([M] модулей, [K] функций)

**Готовы к разработке!** 🚀
```

---

## 💾 CHECKPOINT

**⚠️ КРИТИЧНО: Checkpoint ДОЛЖЕН быть сохранен после завершения PHASE 6!**

**1. Сохранить JSON Checkpoint (ОБЯЗАТЕЛЬНО!):**

```python
save_checkpoint(
    phase_number=6,
    phase_name="PHASE 6: Setup Instructions",
    batch=None,
    state={
        "current_action": "Setup instructions created",
        "files_created": [
            "UPMT_FINAL_STEPS.md"
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
git add UPMT_FINAL_STEPS.md
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 6 complete - setup instructions created"
git push
```

**Показать итоги:**

```markdown
✅ PHASE 6 COMPLETE

**Setup Instructions:**
- ✅ FINAL_SETUP_INSTRUCTIONS.md created
- ✅ Cursor AI setup guide
- ✅ Claude Code CLI setup guide
- ✅ Recommended workflow
- ✅ Next steps outlined

**Next:** PHASE 7 - Validation

⏱️ PHASE 6 завершена за [время]
```

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
→ ПЕРЕХОД К PHASE 7: VALIDATION
→ Прочитай: UPMT/prompts/phases/phase-7-validation.md
```

