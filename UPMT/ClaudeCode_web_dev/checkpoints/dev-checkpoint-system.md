# Dev Checkpoint System

**Версия:** 1.0.0  
**Для:** Development sessions

---

## JSON Format

**Полный формат checkpoint:**

```json
{
  "type": "development_session",
  "session_id": "dev-web-20251115-143000",
  "timestamp": "2025-11-15T14:30:00Z",
  "mode": "WEB_GITHUB" or "CLI",
  
  "current_task": {
    "module": "Authentication",
    "feature": "GitHub OAuth Login",
    "status": "in_progress" or "completed",
    "file": "src/auth/github-oauth.ts",
    "line": 145,
    "description": "Implementing callback handler"
  },
  
  "completed_today": [
    "Created OAuth route handler",
    "Implemented token exchange",
    "Added error handling"
  ],
  
  "next_actions": [
    "Complete callback handler (50% done)",
    "Add unit tests",
    "Update API documentation"
  ],
  
  "files_modified": [
    "src/auth/github-oauth.ts",
    "docs/backend/api/auth-endpoints.md"
  ],
  
  "commits": [
    "a1b2c3d: feat(auth): implement GitHub OAuth token exchange",
    "e4f5g6h: docs(api): update auth endpoints documentation"
  ],
  
  "stats": {
    "files_changed": 2,
    "lines_added": 187,
    "lines_deleted": 23,
    "commits_today": 2,
    "elapsed_time": "02:15:30"
  },
  
  "context_for_next_session": {
    "what_was_done": "Implemented 70% of GitHub OAuth flow",
    "what_remains": "Callback handler completion + tests",
    "blockers": [],
    "notes": "OAuth app credentials configured in .env"
  }
}
```

---

## Checkpoint Points

**Checkpoint создается автоматически:**

1. ✅ После каждой завершенной итерации
2. ✅ После каждого commit
3. ✅ По таймеру (каждые 30 минут, если есть изменения)
4. ✅ Перед началом новой задачи

---

## File Location

**CLI Mode:**
```
.dev/checkpoints/latest.json
```

**Web Mode (GitHub):**
```
.dev/checkpoints/latest.json (через GitHub API)
```

---

## Functions

См. `dev-checkpoint-functions.md` для Python функций

