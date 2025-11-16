# 🛡️ DEV RECOVERY PROTOCOL

**Версия:** 1.0.0
**Для:** Восстановление dev сессий после зависания

## Проблема

Claude Code Web зависла ВО ВРЕМЯ РАЗРАБОТКИ:
- Был в процессе написания кода
- Файл частично изменен
- Commit не сделан
- Прогресс потерян?

## Recovery System

### 1. Automatic Checkpoints

Checkpoint создается:
- После каждой итерации
- После каждого commit
- Каждые 30 минут (если есть изменения)

### 2. Checkpoint Format

```json
{
  "type": "development_session",
  "current_task": {
    "module": "Auth",
    "feature": "OAuth Login",
    "status": "in_progress",
    "file": "src/auth/oauth.ts",
    "line": 145
  },
  "completed_today": [...],
  "next_actions": [...],
  "commits": [...]
}
```

## Recovery Scenarios

### СЦЕНАРИЙ A: Зависание во время dev

**Действия:**

```
1. Открой новую сессию Claude Code Web
2. Введи:

🛡️ DEV RECOVERY MODE

Прочитай: .dev/checkpoints/latest.json
Прочитай: UPMT/ClaudeCode_web_dev/recovery/DEV_RECOVERY_PROTOCOL.md

Восстанови dev сессию с checkpoint
