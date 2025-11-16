# 📦 ИНСТРУКЦИЯ ПО КОПИРОВАНИЮ DEV SYSTEM

**Версия:** 1.0.0  
**Дата:** 2025-11-15

---

## 🎯 ЧТО ЭТО

Эта папка содержит **standalone версию** системы `ClaudeCode_web_dev` для копирования в проекты, где уже завершен bootstrap на предыдущих версиях UPMT.

---

## 📋 ЧТО ВНУТРИ

```
UPMT_ClaudeCode_web_dev_STANDALONE/
└── UPMT/
    └── ClaudeCode_web_dev/
        ├── START_DEV_SESSION.md          # 🚀 Главный entry point
        ├── dev-orchestrator.md           # Контроллер итераций
        ├── README_DEV_SYSTEM.md          # Документация
        ├── adapters/                      # Адаптеры (2 файла)
        ├── workflows/                     # Workflows (4 файла)
        ├── checkpoints/                   # Checkpoint система (2 файла)
        ├── recovery/                      # Recovery система (2 файла)
        ├── logging/                       # Templates для логов (3 файла)
        └── rules/                         # Правила разработки (2 файла)

Итого: 18 файлов в 7 папках
```

---

## 🚀 КАК ИСПОЛЬЗОВАТЬ

### Шаг 1: Скопируй папку в корень проекта

**В корне проекта (где есть `UPMT/`, `docs/`, `.context/`):**

```bash
# Скопируй всю папку UPMT из этой standalone папки
cp -r UPMT_ClaudeCode_web_dev_STANDALONE/UPMT/ClaudeCode_web_dev [path-to-project]/UPMT/
```

**Или вручную:**
1. Открой `UPMT_ClaudeCode_web_dev_STANDALONE/UPMT/ClaudeCode_web_dev/`
2. Скопируй всю папку `ClaudeCode_web_dev`
3. Вставь в `[ваш-проект]/UPMT/`

**Результат:**
```
[ваш-проект]/
├── UPMT/
│   ├── ClaudeCode_web_dev/          ← НОВАЯ ПАПКА
│   │   ├── START_DEV_SESSION.md
│   │   ├── dev-orchestrator.md
│   │   └── ...
│   ├── bootstrap/
│   ├── prompts/
│   └── ...
├── docs/
├── .context/
└── ...
```

---

### Шаг 2: Проверь зависимости (опционально)

**Для полной функциональности проверь наличие:**

```bash
# Project Rules (для автообновления docs)
UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md
```

**Если файла нет:**
- Система будет работать, но без автообновления документации
- Можно скопировать из нового UPMT template (опционально)

---

### Шаг 3: Запусти Dev Session

**В Claude Code Web (в вашем проекте):**

```
Прочитай и выполни: UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
```

---

## ✅ ПРОВЕРКА ПОСЛЕ КОПИРОВАНИЯ

**Убедись что файлы на месте:**

```bash
# Должны существовать:
✅ [ваш-проект]/UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
✅ [ваш-проект]/UPMT/ClaudeCode_web_dev/dev-orchestrator.md
✅ [ваш-проект]/UPMT/ClaudeCode_web_dev/workflows/feature-workflow.md
✅ [ваш-проект]/UPMT/ClaudeCode_web_dev/checkpoints/dev-checkpoint-system.md
✅ [ваш-проект]/UPMT/ClaudeCode_web_dev/recovery/DEV_RECOVERY_PROTOCOL.md
```

**Проверка количества файлов:**
```bash
# Должно быть 18 файлов
find [ваш-проект]/UPMT/ClaudeCode_web_dev -type f | wc -l
# Результат: 18
```

---

## 📊 СТРУКТУРА ФАЙЛОВ

### Core Files (3):
- `START_DEV_SESSION.md` - Главный entry point
- `dev-orchestrator.md` - Контроллер итераций
- `README_DEV_SYSTEM.md` - Полная документация

### Adapters (2):
- `adapters/web-dev-adapter.md` - Web mode (GitHub API)
- `adapters/cli-dev-adapter.md` - CLI mode (local FS)

### Workflows (4):
- `workflows/feature-workflow.md` - Разработка фичи
- `workflows/bugfix-workflow.md` - Исправление бага
- `workflows/refactor-workflow.md` - Рефакторинг
- `workflows/docs-update-workflow.md` - Обновление docs

### Checkpoints (2):
- `checkpoints/dev-checkpoint-system.md` - Документация
- `checkpoints/dev-checkpoint-functions.md` - Функции

### Recovery (2):
- `recovery/DEV_RECOVERY_PROTOCOL.md` - Recovery протокол
- `recovery/recovery-scenarios.md` - Сценарии

### Logging (3):
- `logging/session-log-template.md` - Session log template
- `logging/iteration-report-template.md` - Iteration report template
- `logging/handoff-report-template.md` - Handoff report template

### Rules (2):
- `rules/dev-rules.md` - Правила разработки
- `rules/code-quality-checklist.md` - Чеклист качества

---

## 🎯 ТРЕБОВАНИЯ К ПРОЕКТУ

**Проект должен иметь (после bootstrap):**

```bash
✅ docs/core/00_PROJECT_ESSENCE.md
✅ docs/core/01_PRD.md
✅ docs/core/03_TECH_STACK.md
✅ docs/core/04_ARCHITECTURE.md
✅ .context/state.md
✅ .context/decisions.md
✅ docs/progress/modules_status.md
✅ docs/progress/sprint_current.md
✅ .upmt/metadata.yaml
```

**Если чего-то нет:**
- Система будет работать, но с ограничениями
- Некоторые функции могут быть недоступны

---

## 🔧 БЫСТРОЕ КОПИРОВАНИЕ (PowerShell)

**Для Windows:**

```powershell
# Перейди в папку standalone
cd UPMT_ClaudeCode_web_dev_STANDALONE

# Скопируй в целевой проект
Copy-Item -Path "UPMT\ClaudeCode_web_dev" -Destination "[path-to-project]\UPMT\" -Recurse -Force
```

---

## 🔧 БЫСТРОЕ КОПИРОВАНИЕ (Bash)

**Для Linux/Mac:**

```bash
# Перейди в папку standalone
cd UPMT_ClaudeCode_web_dev_STANDALONE

# Скопируй в целевой проект
cp -r UPMT/ClaudeCode_web_dev [path-to-project]/UPMT/
```

---

## 📝 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ

### Пример 1: Копирование в проект "Brain-Rent"

```bash
# Путь к проекту
PROJECT_PATH="C:/Users/333/Documents/My projects/Brain-Rent"

# Копирование
cp -r UPMT_ClaudeCode_web_dev_STANDALONE/UPMT/ClaudeCode_web_dev "$PROJECT_PATH/UPMT/"

# Проверка
ls "$PROJECT_PATH/UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md"
# ✅ Файл существует
```

### Пример 2: Копирование в несколько проектов

```bash
# Список проектов
PROJECTS=(
  "C:/Users/333/Documents/My projects/Brain-Rent"
  "C:/Users/333/Documents/My projects/Ground-Control"
  "C:/Users/333/Documents/My projects/Another-Project"
)

# Копирование во все проекты
for project in "${PROJECTS[@]}"; do
  echo "Копирую в: $project"
  cp -r UPMT_ClaudeCode_web_dev_STANDALONE/UPMT/ClaudeCode_web_dev "$project/UPMT/"
done
```

---

## ❓ TROUBLESHOOTING

### Проблема: Файлы не копируются

**Решение:**
- Проверь права доступа к целевой папке
- Убедись что папка `UPMT/` существует в проекте
- Используй `-Force` флаг (PowerShell) или `-f` (Bash)

---

### Проблема: Структура неправильная

**Проверь:**
```bash
# Должно быть:
[проект]/UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md

# НЕ должно быть:
[проект]/ClaudeCode_web_dev/START_DEV_SESSION.md  ❌
```

---

### Проблема: Система не запускается

**Проверь:**
1. ✅ Файлы скопированы в правильную папку
2. ✅ Путь в команде правильный: `UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md`
3. ✅ Проект имеет необходимые файлы (`docs/core/`, `.context/`)

---

## 📚 ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ

**Полная документация:**
- `UPMT/ClaudeCode_web_dev/README_DEV_SYSTEM.md` - Overview системы
- `UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md` - Start here!

**Версия UPMT:**
- Dev System: v1.0.0
- Совместимость: UPMT v2.0.0+ (любая версия после bootstrap)

---

## ✅ ГОТОВО!

После копирования:

1. ✅ Файлы на месте
2. ✅ Структура правильная
3. ✅ Запусти dev session

**Команда для запуска:**

```
Прочитай и выполни: UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
```

---

**Версия:** 1.0.0  
**Дата:** 2025-11-15  
**Готово к использованию:** ✅

