# 📚 DEV SYSTEM - DOCUMENTATION

**Версия:** 1.0.0  
**Дата:** 2025-11-15  
**Для:** Post-Bootstrap Development в Claude Code Web

---

## 🎯 ЧТО ЭТО

**UPMT Dev System** - это система для продолжения разработки ПОСЛЕ завершения bootstrap.

**Решает:**
- ✅ Продолжение работы по готовой документации
- ✅ Автоматическое логирование всех действий
- ✅ Recovery после зависания Claude Code Web
- ✅ Передача контекста между агентами (Web → Cursor → CLI)
- ✅ Синхронизация code ↔ docs

---

## 📦 СТРУКТУРА СИСТЕМЫ

```
UPMT/ClaudeCode_web_dev/
├── START_DEV_SESSION.md          # 🚀 ГЛАВНЫЙ ENTRY POINT
├── dev-orchestrator.md           # 🎯 Контроллер итераций
├── README_DEV_SYSTEM.md          # 📚 Эта документация
│
├── adapters/                      # 🔧 Адаптеры для разных сред
│   ├── web-dev-adapter.md         # Web (GitHub API)
│   └── cli-dev-adapter.md         # CLI (локальная работа)
│
├── workflows/                     # 🔄 Рабочие процессы
│   ├── feature-workflow.md        # Новые фичи
│   ├── bugfix-workflow.md         # Исправления
│   ├── refactor-workflow.md       # Рефакторинг
│   └── docs-update-workflow.md    # Обновление docs
│
├── checkpoints/                   # 💾 Система checkpoint
│   ├── dev-checkpoint-system.md   # Документация
│   └── dev-checkpoint-functions.md # Python функции
│
├── recovery/                      # 🛡️ Recovery система
│   ├── DEV_RECOVERY_PROTOCOL.md   # Главный протокол
│   └── recovery-scenarios.md      # Сценарии восстановления
│
├── logging/                       # 📝 Система логирования
│   ├── session-log-template.md    # Template session log
│   ├── iteration-report-template.md # Template iteration report
│   └── handoff-report-template.md  # Template handoff report
│
└── rules/                         # 📋 Правила разработки
    ├── dev-rules.md               # Правила для dev
    └── code-quality-checklist.md  # Чеклист качества
```

---

## 🚀 БЫСТРЫЙ СТАРТ

### 1. Проверь что Bootstrap завершен

```bash
# Должны существовать:
✅ BOOTSTRAP_REPORT.md
✅ docs/core/
✅ docs/requirements/
✅ .context/
✅ docs/progress/
```

### 2. Запусти Dev Session

**В Claude Code Web введи:**

```
Прочитай и выполни: UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
```

### 3. Следуй инструкциям

Claude автоматически:
1. Проверит recovery checkpoint
2. Загрузит контекст проекта
3. Предложит выбрать workflow
4. Начнет итерационную разработку

---

## 🔄 WORKFLOWS

### Feature Development

**Когда:** Разработка новой фичи

**Workflow:**
```
1. Read requirements
2. Plan implementation
3. Write code
4. Update docs
5. Test
6. Commit + Checkpoint
```

**Детали:** `workflows/feature-workflow.md`

---

### Bug Fix

**Когда:** Исправление бага

**Workflow:**
```
1. Reproduce bug
2. Identify root cause
3. Fix code
4. Test fix
5. Commit + Checkpoint
```

**Детали:** `workflows/bugfix-workflow.md`

---

### Refactoring

**Когда:** Улучшение структуры кода

**Workflow:**
```
1. Identify code smell
2. Plan refactoring
3. Refactor incrementally
4. Test continuously
5. Commit after each step
```

**Детали:** `workflows/refactor-workflow.md`

---

### Documentation Update

**Когда:** Обновление документации

**Workflow:**
```
1. Identify outdated docs
2. Update docs
3. Sync with code
4. Commit
```

**Детали:** `workflows/docs-update-workflow.md`

---

## 💾 CHECKPOINT СИСТЕМА

### Автоматические сохранения

**Checkpoint создается:**
- ✅ После каждой завершенной итерации
- ✅ После каждого commit
- ✅ По таймеру (каждые 30 минут)
- ✅ Перед началом новой задачи

**Формат:**
```json
{
  "type": "development_session",
  "current_task": {...},
  "completed_today": [...],
  "next_actions": [...],
  "files_modified": [...],
  "commits": [...]
}
```

**Файл:** `.dev/checkpoints/latest.json`

**Документация:** `checkpoints/dev-checkpoint-system.md`

---

## 🛡️ RECOVERY PROTOCOL

### Когда использовать

Claude Code Web зависла и нужно восстановить сессию.

### Быстрый recovery

**В новой сессии Claude Code Web:**

```
🛡️ DEV RECOVERY MODE

Предыдущая сессия прервана. Восстанавливаю.

Прочитай: UPMT/ClaudeCode_web_dev/recovery/DEV_RECOVERY_PROTOCOL.md

Выполни: СЦЕНАРИЙ A (Dev Session Recovery)
```

### Что произойдет

1. Claude прочитает checkpoint
2. Покажет статус восстановления
3. Спросит подтверждение
4. Продолжит с прерванной точки

**Документация:** `recovery/DEV_RECOVERY_PROTOCOL.md`

---

## 📝 LOGGING СИСТЕМА

### Session Logs

**Файл:** `.dev/logs/session-YYYYMMDD-HHMMSS.md`

**Содержит:**
- Session info
- Completed tasks
- In-progress tasks
- Commits
- Stats

**Template:** `logging/session-log-template.md`

---

### Iteration Reports

**Добавляется в session log**

**Содержит:**
- Task details
- Code snippets
- Files changed
- Tests results
- Time spent

**Template:** `logging/iteration-report-template.md`

---

### Handoff Reports

**Файл:** `.dev/handoff/handoff-to-[agent]-YYYYMMDD.md`

**Для:** Передачи контекста другому агенту

**Содержит:**
- Current state
- What's done
- What remains
- How to continue
- Important context

**Template:** `logging/handoff-report-template.md`

---

## 🤝 AGENT HANDOFF

### Передача Cursor AI

**Создай handoff report:**
```
1. Complete current task или pause
2. Create checkpoint
3. Generate handoff report
4. Save to .dev/handoff/
5. Commit
```

**Cursor получит:**
- Полный контекст
- Точное место где остановился
- Инструкции как продолжить

---

### Передача CLI Agent

**Аналогично Cursor:**
- Handoff report
- Checkpoint
- Инструкции для CLI

---

## 📋 RULES & QUALITY

### Dev Rules

**Файл:** `rules/dev-rules.md`

**Правила:**
- Code style guidelines
- Best practices
- Error handling patterns
- Testing requirements

---

### Code Quality Checklist

**Файл:** `rules/code-quality-checklist.md`

**Проверяется перед commit:**
- ✅ TypeScript strict mode
- ✅ No console.log в production
- ✅ Error handling
- ✅ Comments для сложного кода
- ✅ Tests pass
- ✅ Docs updated

---

## 📊 INTEGRATION С UPMT

### Project Rules Integration

Dev System интегрирован с **Project Rules** (`All_Project_rules.md`):

**При изменении code:**
- ✅ Автоматическое обновление docs
- ✅ Синхронизация требований
- ✅ Update progress tracking
- ✅ Log changes в .context/

---

### Bootstrap → Development Flow

```
BOOTSTRAP (UPMT/START.md)
    ↓
    ↓ Создает: docs/, .context/, metadata
    ↓
    ↓ Выход: BOOTSTRAP_REPORT.md
    ↓
    ↓
DEVELOPMENT (ClaudeCode_web_dev/)
    ↓
    ↓ Использует: docs/, requirements/
    ↓
    ↓ Создает: src/, app/, components/
    ↓
    ↓ Обновляет: docs/, .context/, progress/
    ↓
    ↓ Логирует: .dev/logs/, .dev/checkpoints/
    ↓
    ↓
PRODUCTION (Ready Code)
```

---

## 🎯 USE CASES

### Use Case 1: Daily Development

```
Day 1:
  08:00 - Start dev session (Claude Code Web)
  10:00 - 2 features completed, checkpoint
  12:00 - Lunch break, checkpoint saved

Day 1 (afternoon):
  13:00 - Resume from checkpoint
  16:00 - 1 more feature, refactoring
  17:00 - Session end, handoff report

Day 2:
  09:00 - Resume from yesterday's checkpoint
  11:00 - Continue development
```

---

### Use Case 2: Agent Switch

```
Morning (Claude Code Web):
  - Start feature implementation (50% done)
  - Checkpoint + Handoff report

Afternoon (Cursor AI):
  - Read handoff report
  - Continue feature (finish + test)
  - Deploy
```

---

### Use Case 3: Recovery After Freeze

```
Claude Code Web freezes at 15:30:
  - Session lost?

New Claude Code Web session at 15:35:
  - Read checkpoint (15:25 saved)
  - Recovery dialog
  - Continue from exact point
  - Only 5 minutes lost!
```

---

## ✅ SUCCESS CRITERIA

**Dev Session успешна когда:**

1. ✅ Checkpoint создан после каждой итерации
2. ✅ Session log содержит все действия
3. ✅ Code написан и затестирован
4. ✅ Docs обновлены (если нужно)
5. ✅ Commits сделаны с правильными сообщениями
6. ✅ Progress tracking обновлен
7. ✅ Recovery checkpoint актуален

---

## 📚 ДОПОЛНИТЕЛЬНЫЕ РЕСУРСЫ

### Основные файлы

- `START_DEV_SESSION.md` - Главный entry point
- `dev-orchestrator.md` - Контроллер итераций
- `DEV_RECOVERY_PROTOCOL.md` - Recovery guide

### Workflows

- `workflows/feature-workflow.md` - Feature development
- `workflows/bugfix-workflow.md` - Bug fixes
- `workflows/refactor-workflow.md` - Refactoring
- `workflows/docs-update-workflow.md` - Documentation

### Системы

- `checkpoints/` - Checkpoint documentation
- `logging/` - Log templates
- `recovery/` - Recovery scenarios
- `rules/` - Development rules

---

## 🆘 TROUBLESHOOTING

### Проблема: Checkpoint не создается

**Решение:**
```bash
# Проверь существование директории
ls -la .dev/checkpoints/

# Если нет, создай
mkdir -p .dev/checkpoints
```

---

### Проблема: Recovery не работает

**Решение:**
- Проверь возраст checkpoint (<24 часа)
- Проверь формат JSON (валидный?)
- Проверь существование файлов из checkpoint
- Используй СЦЕНАРИЙ B (recovery by Git history)

---

### Проблема: Handoff report неполный

**Решение:**
- Используй template: `logging/handoff-report-template.md`
- Укажи ВСЕ обязательные секции
- Добавь достаточно контекста
- Проверь что checkpoint сохранен

---

## 📞 FEEDBACK & SUPPORT

**Нашли проблему?**
- Создай issue в UPMT репо
- Опиши проблему детально
- Приложи checkpoint JSON (если есть)

**Есть предложения?**
- Открой discussion
- Опиши use case
- Предложи улучшения

---

## 📈 STATISTICS

**Dev System:**
- 📁 21 файл
- 📂 7 директорий
- 📝 ~8000 строк документации
- 🎯 4 workflows
- 🛡️ 1 recovery protocol
- 💾 Автоматические checkpoints
- 📊 Полное логирование

---

**Версия:** 1.0.0  
**Последнее обновление:** 2025-11-15  
**Статус:** ✅ Production Ready

---

**Made with ❤️ for developers using UPMT + Claude Code Web**

