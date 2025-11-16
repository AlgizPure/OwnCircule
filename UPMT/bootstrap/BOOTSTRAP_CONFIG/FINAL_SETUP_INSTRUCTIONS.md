# FINAL SETUP INSTRUCTIONS

**Статус:** Bootstrap завершён ✅  
**Версия:** 1.0.2  
**Дата:** [будет заполнено Claude Code автоматически]

---

## ✅ ЧТО СОЗДАНО

[Claude Code автоматически заполнит этот раздел после завершения bootstrap]

**Пример:**
- 52 файла
- 150+ страниц документации
- 10 модулей специфицированы
- 75 функциональных требований
- Tech stack верифицирован ({CURRENT_MONTH_YEAR})

---

## 🎯 СЛЕДУЮЩИЕ ШАГИ

После завершения bootstrap нужно настроить AI ассистентов для правильной работы системы.

**Критически важно выполнить ВСЕ шаги ниже!**

---

## 🔧 НАСТРОЙКА CURSOR (ОБЯЗАТЕЛЬНО)

### Шаг 1: Копирование .cursorrules в корень проекта

Cursor автоматически читает `.cursorrules` из **корня проекта**.

**Проверь наличие файла:**

```bash
# Должен существовать
ls -la UPMT/structure-templates/AI_INSTRUCTIONS/.cursorrules.template
```

**Скопируй в корень проекта:**

```bash
# Из корня проекта
cp UPMT/structure-templates/AI_INSTRUCTIONS/.cursorrules.template .cursorrules

# Проверь
ls -la .cursorrules

# Добавь в git
git add .cursorrules
git commit -m "Add: Cursor project rules"
```

**Важно:** Файл ДОЛЖЕН быть в корне, не в подпапке!

---

### Шаг 2: Настройка Cursor Project Settings

1. **Открой проект в Cursor**
   ```bash
   cursor .
   ```

2. **Открой Settings**
   - Нажми `Cmd+,` (Mac) или `Ctrl+,` (Windows/Linux)
   - Или: `Cmd/Ctrl + Shift + P` → "Preferences: Open Settings"

3. **Перейди на вкладку "Features"**

4. **Включи следующие опции:**
   - ✅ **"Use .cursorrules"** - читать правила из файла
   - ✅ **"Include project context in AI requests"** - включать контекст проекта
   - ✅ **"Auto-update context"** - автообновление контекста

5. **Сохрани настройки**

---

### Шаг 3: Добавление дополнительных Project Rules (ВАЖНО!)

Эти правила критически важны для работы с файлами из новой UPMT структуры.

**Как добавить:**

1. Открой Cursor Settings
2. Найди секцию **"Rules"** или **"Project Rules"**
3. Нажми **"Edit in settings.json"** или **"Add Project Rules"**

**Добавь следующие правила:**

```yaml
# Additional Cursor Project Rules for Project Management Template

## Context Files Priority

ALWAYS read FIRST before starting ANY task:
1. `.context/state.md`
2. `docs/core/99_SYSTEM_GUIDE.md`
3. Relevant module from `docs/requirements/` (based on current task)

## Auto-Update Rules After Code Changes

After ANY code change, automatically:
1. Update `.context/state.md`:
   - Section "LAST COMPLETED" with what was done
   - Section "NEXT STEPS" with what's next
   - Timestamp "Last Updated"

2. If progress was made on a module:
   - Update `docs/progress/modules_status.md`
   - Update completion percentage
   - Update status (In Dev, Testing, Complete)

3. If technical decision was made:
   - Log in `.context/decisions.md`
   - Format: DEC-XXX with full context
   - Include rationale and alternatives

## Update Rules on Milestones

When module reaches specific completion:
- **25% complete:** Review requirements, confirm scope
- **50% complete:** Update `docs/core/02_ROADMAP.md` progress section
- **75% complete:** Update `docs/core/01_PRD.md`, mark features as "In Progress"
- **100% complete:** 
  - Update `docs/core/01_PRD.md` (mark features ✅)
  - Update `docs/progress/modules_status.md` (Complete)
  - Update `.context/state.md` (move to next module)
  - Log completion in `.context/changes_log.md`

## File Change Triggers

When these files are modified:
- **PROJECT_ESSENCE.md changed** → Review and update:
  - `docs/core/01_PRD.md` (align features with vision)
  - `docs/core/02_ROADMAP.md` (align phases with goals)
  - `docs/core/03_TECH_STACK.md` (ensure tech supports vision)

- **PRD.md changed** → Review and update:
  - `docs/requirements/*.md` (sync requirements)
  - `docs/progress/modules_status.md` (new modules?)

- **TECH_STACK.md changed** → Review and update:
  - `docs/core/04_ARCHITECTURE.md` (architectural impact?)
  - `.cursorrules` (code standards section)

- **Any requirement file changed** → Notify developer:
  - "Requirements changed! Review existing code for impact."
  - List affected files based on implementation

## Requirements Reference

For EVERY code change:
- Include comment: // Implements: FR-[MODULE]-XXX
- Reference requirement file in commit message
- Check acceptance criteria before marking complete

## Documentation References

Refer to these for detailed workflows:
- `@UPMT/structure-templates/AI_INSTRUCTIONS/UPDATE_RULES.md` (update matrix)
- `@UPMT/structure-templates/AI_INSTRUCTIONS/CHANGE_SCENARIOS.md` (change handling)
- `@UPMT/structure-templates/AI_INSTRUCTIONS/WORKFLOW_GUIDE.md` (daily workflows)

## Examples

For code examples and patterns:
- `@UPMT/structure-templates/AI_INSTRUCTIONS/EXAMPLES/` (all examples)
```

**Сохрани и закрой.**

---

### Шаг 4: Проверка работы Cursor

Протестируй настройки:

1. **Открой Cursor Chat** (`Cmd/Ctrl + L`)

2. **Спроси:**
   ```
   Какой текущий статус проекта?
   ```

3. **Cursor должен:**
   - Прочитать `.context/state.md`
   - Показать текущий фокус, прогресс, следующие шаги
   - Ответить осмысленно

**Если Cursor НЕ читает файлы автоматически:**

- Перезапусти Cursor
- Проверь что `.cursorrules` в корне проекта
- Проверь что "Use .cursorrules" включено в Settings
- Проверь Project Rules добавлены

**Попробуй явно:**
```
@.context/state.md Какой текущий статус?
```

---

## 🤖 НАСТРОЙКА CLAUDE CODE CLI

Claude Code CLI автоматически использует `.clauderules`.

### Шаг 1: Проверка наличия .clauderules

```bash
# Проверь наличие
ls -la UPMT/structure-templates/AI_INSTRUCTIONS/.clauderules

# Должен быть ~297 строк (если файл существует)
wc -l UPMT/structure-templates/AI_INSTRUCTIONS/.clauderules
```

**Если файл есть** → всё готово! Claude Code автоматически его использует.

**Если файла нет** → это нормально, Claude Code работает без него (использует .cursorrules).

### Шаг 2: Проверка работы

**Запусти Claude Code:**

```bash
# Из корня проекта
claude
```

**Claude Code должен автоматически:**

1. Прочитать `.cursorrules` из корня проекта (если есть)
2. Загрузить `.context/state.md`
3. Показать приветствие с текущим контекстом:

```
📊 CLAUDE CODE - PROJECT LOADED

Project: [Название проекта]
Phase: [Текущая фаза]
Current Focus: [Из state.md]

Last Activity: [Из state.md]
Today's Plan: [Из NEXT STEPS]

System rules loaded ✓
Ready to work! 🚀

What would you like to do?
```

**Если что-то не так:**
- Проверь путь к `.cursorrules` в корне проекта
- Убедись что файл читаемый
- Перезапусти Claude Code

### Шаг 3: Нет дополнительной настройки!

Claude Code CLI **НЕ требует** дополнительных настроек.

Всё работает "из коробки" благодаря `.cursorrules` в корне проекта.

---

## 📝 ЕЖЕДНЕВНЫЙ РАБОЧИЙ ПРОЦЕСС

После настройки, вот как работать с системой:

### Утро (5 минут)

**Вариант A: Claude Code CLI**

```bash
# Запусти Claude Code
claude

# Claude автоматически покажет:
# - Текущий статус
# - Прогресс
# - План на день

# Подтверди или скорректируй план
"Да, продолжаем" или "Нет, изменить на..."
```

**Вариант B: Cursor**

```bash
# Открой проект
cursor .

# В Cursor Chat спроси:
"Какой план на сегодня?"

# Cursor прочитает state.md и ответит
```

### В течение дня (Cursor)

**Работай в Cursor с AI assistance:**

```typescript
// Cursor автоматически:
// - Читает requirements перед кодированием
// - Следует архитектуре из ARCHITECTURE.md
// - Добавляет traceability comments
// - Напоминает обновить документацию
```

**Если нужна помощь:**

```
# В Cursor Chat
@docs/requirements/auth_requirements.md
Реализуй FR-AUTH-005
```

### Конец дня (5 минут)

**Обнови state.md:**

```bash
# Через Claude Code
claude
"Обнови state.md: сегодня завершил FR-AUTH-005"

# Или через Cursor
# В Chat: "Обнови state.md с сегодняшним прогрессом"
```

**Claude/Cursor автоматически обновит:**
- LAST COMPLETED (что сделано)
- NEXT STEPS (что завтра)
- Timestamp

**Коммит:**

```bash
git add .context/state.md
git commit -m "Update: daily progress (FR-AUTH-005 completed)"
git push
```

---

## 🔄 ОБНОВЛЕНИЕ ПРАВИЛ ПРИ ИЗМЕНЕНИЯХ

### Когда обновлять .cursorrules / .clauderules

**Триггер 1: Изменилась архитектура**

```bash
# Изменил ARCHITECTURE.md?
# Обнови секцию "Architecture Patterns" в .cursorrules

# Пример: добавил микросервисы
# → Добавь в .cursorrules правила для микросервисной архитектуры
```

**Триггер 2: Добавился новый модуль**

```bash
# Создал новый модуль в docs/requirements/?
# Обнови список модулей в .cursorrules

# Добавь:
# - Название модуля
# - Ключевые требования
# - Зависимости
```

**Триггер 3: Изменился tech stack**

```bash
# Изменил TECH_STACK.md (добавил Redis)?
# Обнови:
# - .cursorrules: секция "Tech Stack"
# - .clauderules: секция "Code Standards"

# Добавь правила для нового стека:
# - Naming conventions
# - Best practices
# - Integration patterns
```

**Триггер 4: Достигнута веха (milestone)**

```bash
# Завершил MVP?
# Обнови:
# - .cursorrules: Current Phase: "MVP" → "Phase 1"
# - Adjust priorities

# Новая фаза = новые правила!
```

### Как обновлять правила

**Метод 1: Ручное редактирование**

```bash
# Открой в редакторе
cursor .cursorrules

# Отредактируй нужные секции
# Сохрани

# Коммит
git add .cursorrules
git commit -m "Update: Cursor rules for Phase 1"
git push
```

**Метод 2: Попроси Claude Code**

```bash
claude

"Обнови .cursorrules:
- Current Phase: MVP → Phase 1
- Добавь новый модуль: Analytics
- Обнови tech stack: добавлен Redis"

# Claude Code обновит файл автоматически
```

**Метод 3: Попроси Cursor**

```
# В Cursor Chat
"Обнови .cursorrules: добавь правила для работы с Redis.
Ссылайся на @docs/core/03_TECH_STACK.md"

# Cursor обновит и предложит изменения
```

---

## 📚 ДОПОЛНИТЕЛЬНЫЕ РЕСУРСЫ

После setup, изучи эти документы для глубокого понимания системы:

### Рабочие процессы

**`@UPMT/structure-templates/AI_INSTRUCTIONS/WORKFLOW_GUIDE.md`**
- Daily development workflow
- Weekly review process
- Code review workflow
- Bug fix process

### Сценарии изменений

**`@UPMT/structure-templates/AI_INSTRUCTIONS/CHANGE_SCENARIOS.md`**
- Добавление новой фичи
- Изменение существующей фичи
- Удаление фичи
- Изменение архитектуры
- Pivot проекта

### Правила обновлений

**`@UPMT/structure-templates/AI_INSTRUCTIONS/UPDATE_RULES.md`**
- Когда и как обновлять документы
- Матрица триггеров обновления
- Cascade update rules
- Validation rules

### Примеры кода

**`@UPMT/structure-templates/AI_INSTRUCTIONS/EXAMPLES/`**
- Примеры реализации фич
- Примеры code review
- Примеры requirements reference
- Примеры traceability comments

---

## ✅ ФИНАЛЬНАЯ ПРОВЕРКА

Пройдись по чеклисту, чтобы убедиться что всё настроено:

### Cursor Setup

- [ ] Файл `.cursorrules` скопирован в корень проекта
- [ ] Cursor Settings: "Use .cursorrules" включено
- [ ] Cursor Settings: "Include project context" включено
- [ ] Additional Project Rules добавлены в settings.json
- [ ] Тестовый вопрос в Cursor Chat работает (читает state.md)

### Claude Code Setup

- [ ] Файл `.cursorrules` существует в корне проекта
- [ ] Запуск `claude` показывает project loaded message
- [ ] Claude Code автоматически читает `.context/state.md`
- [ ] Claude Code понимает текущий контекст

### Documentation

- [ ] Все файлы в `docs/core/` заполнены
- [ ] `docs/requirements/` содержит спецификации
- [ ] `.context/state.md` актуален
- [ ] `docs/progress/` настроен

### Git

- [ ] Все файлы закоммичены
- [ ] `.cursorrules` в корне добавлен в git
- [ ] Создан meaningful commit message
- [ ] Запушено в remote (если нужно)

---

## 🎉 ГОТОВО! МОЖНО НАЧИНАТЬ

### Ты успешно настроил:

✅ Project Management Template структуру  
✅ AI ассистенты (Cursor + Claude Code)  
✅ Автоматическое обновление документации  
✅ Систему отслеживания прогресса  
✅ Context preservation между сессиями

### Следующие шаги:

1. **Выбери первую задачу** из `docs/progress/sprint_current.md`
2. **Открой requirements** для соответствующего модуля
3. **Попроси AI помощь**: "Реализуй FR-XXX-YYY"
4. **Разрабатывай** с AI assistance
5. **Обновляй progress** ежедневно

---

## 🆘 ПРОБЛЕМЫ?

### Cursor не читает файлы автоматически

**Решение:**
1. Перезапусти Cursor
2. Проверь `.cursorrules` в корне
3. Проверь Settings
4. Попробуй явный @mention: `@.context/state.md`

### Claude Code не показывает контекст

**Решение:**
1. Проверь наличие `.cursorrules` в корне проекта
2. Запусти из корня проекта
3. Проверь что `.context/state.md` заполнен

### AI не обновляет документацию

**Решение:**
1. Проверь Project Rules в Cursor
2. Напомни явно: "Обнови `.context/state.md` с прогрессом"
3. Проверь что `UPMT/structure-templates/AI_INSTRUCTIONS/UPDATE_RULES.md` доступен

### Нужна дополнительная помощь

- 📖 Читай WORKFLOW_GUIDE.md
- 🔍 Проверь CHANGE_SCENARIOS.md
- 💬 Задай вопрос в GitHub Discussions
- 🐛 Открой Issue на GitHub

---

**Проект готов к разработке!** 🚀

**Happy coding with AI assistance!** 🤖

---

*Примечание: Этот файл был сгенерирован автоматически Claude Code после завершения bootstrap. Если нужны изменения в setup процессе, обнови соответствующие секции выше.*

