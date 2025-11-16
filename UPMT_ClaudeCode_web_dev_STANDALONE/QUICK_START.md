# ⚡ БЫСТРЫЙ СТАРТ

## 🎯 КОПИРОВАНИЕ В ПРОЕКТ

### Windows (PowerShell):

```powershell
# 1. Перейди в папку standalone
cd UPMT_ClaudeCode_web_dev_STANDALONE

# 2. Скопируй в целевой проект
Copy-Item -Path "UPMT\ClaudeCode_web_dev" -Destination "[путь-к-проекту]\UPMT\" -Recurse -Force
```

### Linux/Mac (Bash):

```bash
# 1. Перейди в папку standalone
cd UPMT_ClaudeCode_web_dev_STANDALONE

# 2. Скопируй в целевой проект
cp -r UPMT/ClaudeCode_web_dev [путь-к-проекту]/UPMT/
```

---

## ✅ ПРОВЕРКА

После копирования проверь:

```bash
# Должен существовать:
[проект]/UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
```

---

## 🚀 ЗАПУСК

В Claude Code Web (в вашем проекте):

```
Прочитай и выполни: UPMT/ClaudeCode_web_dev/START_DEV_SESSION.md
```

---

**Полная инструкция:** См. `README_COPY_INSTRUCTIONS.md`

