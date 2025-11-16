# 🎯 DEV ORCHESTRATOR

**Версия:** 1.0.0  
**Дата:** 2025-11-15  
**Роль:** Главный контроллер development итераций

---

## 📋 ЧТО ЭТО

Этот файл - **главный оркестратор** для post-bootstrap разработки. Он:
- Управляет циклом dev итераций
- Интегрируется с Project Rules
- Обеспечивает checkpoint систему
- Гарантирует качество кода
- Синхронизирует code ↔ docs

---

## 🔄 DEV ITERATION ЦИКЛ

```
┌──────────────────────────────────────────────────────────┐
│                  ITERATION START                          │
└──────────────────────────────────────────────────────────┘
                          ↓
╔══════════════════════════════════════════════════════════╗
║  1️⃣  READ CONTEXT                                         ║
╚══════════════════════════════════════════════════════════╝

📖 Прочитай необходимые файлы:
   - docs/requirements/[module]_requirements.md (для текущей задачи)
   - .context/state.md (текущее состояние)
   - docs/progress/sprint_current.md (текущие задачи)
   - docs/progress/backlog.md (запланированные задачи)

                          ↓
╔══════════════════════════════════════════════════════════╗
║  2️⃣  SELECT TASK                                          ║
╚══════════════════════════════════════════════════════════╝

🎯 Выбери задачу из:
   Option A: Из sprint_current.md (приоритет!)
   Option B: Из backlog.md (если спринт пуст)
   Option C: От пользователя (если задача не в списках)

📝 Формат задачи:
   - Module: [название модуля]
   - Feature: [название фичи]
   - Description: [детальное описание]
   - Acceptance Criteria: [критерии готовности]
   - Priority: [P0/P1/P2]

                          ↓
╔══════════════════════════════════════════════════════════╗
║  3️⃣  PLAN IMPLEMENTATION                                  ║
╚══════════════════════════════════════════════════════════╝

🗺️ Создай технический план:
   1. Какие файлы нужно создать/изменить
   2. Какие зависимости нужны (npm install)
   3. Какие docs нужно обновить (Project Rules!)
   4. Какие тесты нужны
   5. Estimated time

💬 Покажи план пользователю и дождись подтверждения

                          ↓
╔══════════════════════════════════════════════════════════╗
║  4️⃣  WRITE CODE                                           ║
╚══════════════════════════════════════════════════════════╝

💻 Пиши код следуя:
   ✅ Tech Stack из docs/core/03_TECH_STACK.md
   ✅ Architecture из docs/core/04_ARCHITECTURE.md
   ✅ Code Quality Checklist (UPMT/ClaudeCode_web_dev/rules/)
   ✅ TypeScript strict mode
   ✅ Комментарии для сложных участков
   ✅ Error handling

⚠️ КРИТИЧНО: Следуй Project Rules!
   Если изменяешь code → обнови связанные docs автоматически

                          ↓
╔══════════════════════════════════════════════════════════╗
║  5️⃣  UPDATE DOCS (если нужно)                            ║
╚══════════════════════════════════════════════════════════╝

📚 Проверь триггеры Project Rules (All_Project_rules.md):

RULE_XX может требовать обновления:
   - docs/core/04_ARCHITECTURE.md (если изменилась структура)
   - docs/requirements/[module].md (если добавлена фича)
   - docs/backend/api/*.md (если изменились endpoints)
   - .context/decisions.md (если принято решение)
   - .context/insights.md (если обнаружен важный инсайт)

🎯 Действие:
   1. Определи какие правила сработали
   2. Обнови соответствующие файлы
   3. Уведоми: "✅ RULE_XX: обновлены [файлы]"

                          ↓
╔══════════════════════════════════════════════════════════╗
║  6️⃣  TEST                                                 ║
╚══════════════════════════════════════════════════════════╝

🧪 Тестирование (manual или automated):

Manual Test:
   - Запусти dev server (если нужно)
   - Проверь функциональность вручную
   - Проверь edge cases

Automated Test:
   - Запусти существующие тесты: npm test
   - Добавь новые тесты (если нужно)
   - Проверь coverage

✅ Результат: PASSED или FAILED
❌ Если FAILED → вернись к step 4 (fix code)

                          ↓
╔══════════════════════════════════════════════════════════╗
║  7️⃣  COMMIT + PUSH                                        ║
╚══════════════════════════════════════════════════════════╝

💾 Git workflow:

```bash
# Stage changes
git add [files]

# Commit with semantic message
git commit -m "type(scope): description

- Detail 1
- Detail 2

Closes #123"

# Push to remote
git push
```

📝 Commit message types:
   - feat: Новая фича
   - fix: Исправление бага
   - docs: Обновление документации
   - refactor: Рефакторинг кода
   - test: Добавление тестов
   - chore: Техническая работа

                          ↓
╔══════════════════════════════════════════════════════════╗
║  8️⃣  CREATE CHECKPOINT                                    ║
╚══════════════════════════════════════════════════════════╝

💾 Сохрани checkpoint в `.dev/checkpoints/latest.json`:

```python
save_checkpoint_dev(
    type="development_session",
    current_task={
        "module": "Authentication",
        "feature": "GitHub OAuth Login",
        "status": "in_progress" or "completed",
        "file": "src/auth/github-oauth.ts",
        "line": 145,
        "description": "..."
    },
    completed_today=[
        "Created OAuth route handler",
        "Implemented token exchange"
    ],
    next_actions=[
        "Add unit tests",
        "Update API documentation"
    ],
    files_modified=[...],
    commits=[...],
    stats={...}
)
```

📄 Checkpoint format: См. `checkpoints/dev-checkpoint-system.md`

                          ↓
╔══════════════════════════════════════════════════════════╗
║  9️⃣  WRITE ITERATION REPORT                              ║
╚══════════════════════════════════════════════════════════╝

📝 Добавь iteration report в session log:

Файл: `.dev/logs/session-YYYYMMDD-HHMMSS.md`

Содержание:
   - Task completed: [название]
   - Files changed: [список]
   - Code snippets: [ключевые фрагменты]
   - Tests: [результаты]
   - Time spent: [HH:MM]
   - Commits: [hashes]

Template: `logging/iteration-report-template.md`

                          ↓
╔══════════════════════════════════════════════════════════╗
║  🔟 UPDATE PROGRESS                                       ║
╚══════════════════════════════════════════════════════════╝

📊 Обнови прогресс файлы:

1. `docs/progress/modules_status.md`:
   ```markdown
   | Auth | 🔄 IN PROGRESS | 45% → 60% | 2025-11-15 |
   ```

2. `docs/progress/sprint_current.md`:
   ```markdown
   - [x] Task: Implement OAuth flow ✅ 2025-11-15
   ```

3. `.context/state.md`:
   ```markdown
   **Last Updated:** 2025-11-15 15:30

   **Current Focus:** Authentication module (60% complete)
   ```

                          ↓
╔══════════════════════════════════════════════════════════╗
║  ✅ ITERATION COMPLETE                                    ║
╚══════════════════════════════════════════════════════════╝

🎉 Итерация завершена! Готов к:

Option A: NEXT ITERATION
   ↻ Вернись к step 1 (Read Context)
   ↻ Выбери следующую задачу
   ↻ Повтори цикл

Option B: HANDOFF TO ANOTHER AGENT
   📤 Создай handoff report (см. ниже)
   📤 Сохрани в `.dev/handoff/`
   📤 Завершай сессию

Option C: SESSION END
   🛑 Финализируй session log
   🛑 Final checkpoint
   🛑 Commit logs
   🛑 Завершай сессию
```

---

## 🛡️ RESUME FROM CHECKPOINT

**Когда использовать:** Recovery после зависания или продолжение прерванной сессии

### Алгоритм:

```
1️⃣  READ CHECKPOINT
    Прочитай: `.dev/checkpoints/latest.json`

2️⃣  VALIDATE CHECKPOINT
    - Проверь возраст (<24 часа)
    - Проверь наличие файлов из checkpoint
    - Проверь Git history (commit существует?)

3️⃣  LOAD CONTEXT
    Прочитай все файлы из checkpoint:
    - Текущий файл разработки
    - Связанные docs
    - Project context (.context/*, docs/progress/*)

4️⃣  SHOW STATUS REPORT
    Выведи пользователю:
    ```
    📍 ВОССТАНОВЛЕНИЕ С CHECKPOINT

    Последняя сессия:
    - Дата: {timestamp}
    - Задача: {current_task.feature}
    - Прогресс: {current_task.status}

    ✅ Завершено:
    - {completed[0]}
    - {completed[1]}

    🔄 Осталось:
    - {next_actions[0]}
    - {next_actions[1]}

    Продолжить? (yes/no)
    ```

5️⃣  CONTINUE FROM LAST POINT
    Если yes:
    - Перейди к step где остановился
    - Если task "in_progress" → step 4 (Write Code)
    - Если task "completed" → step 2 (Select Task)

6️⃣  CREATE NEW CHECKPOINT
    После первой завершенной итерации:
    - Обнови latest.json
    - Подтверди recovery успешен
```

---

## 📤 HANDOFF TO ANOTHER AGENT

**Когда создавать:** Перед завершением сессии если задачи незавершены

### Handoff Report Template:

Файл: `.dev/handoff/handoff-to-[cursor|cli]-YYYYMMDD.md`

```markdown
# 🤝 HANDOFF REPORT - [TARGET AGENT]

**From:** Claude Code Web
**To:** [Cursor AI / CLI Agent]
**Date:** 2025-11-15 16:30
**Session ID:** dev-web-20251115-143000

---

## 📍 CURRENT STATE

**Current Task:**
- Module: Authentication
- Feature: GitHub OAuth Login
- Status: 70% complete
- File: src/auth/github-oauth.ts (line 145)

**What's Done:**
1. ✅ Created OAuth routes
2. ✅ Implemented token exchange
3. ✅ Added error handling

**What Remains:**
1. ⏳ Complete callback handler (30% left)
2. ⏳ Add unit tests
3. ⏳ Update API documentation

---

## 💾 FILES TO WORK WITH

**Code:**
- `src/auth/github-oauth.ts` (main file, 70% done)
- `src/auth/types.ts` (types defined)
- `src/lib/oauth-client.ts` (helper functions)

**Docs to Update:**
- `docs/backend/api/auth-endpoints.md` (after completing)
- `docs/requirements/authentication.md` (mark as done)

---

## 🎯 NEXT ACTIONS

**Priority 1:**
```typescript
// Complete callback handler in github-oauth.ts line 145:
export async function handleCallback(code: string) {
  // TODO: Add user creation/login logic
  // TODO: Add session management
  // TODO: Add redirect to dashboard
}
```

**Priority 2:**
- Add unit tests for OAuth flow
- Test with real GitHub OAuth app

**Priority 3:**
- Update API docs with new endpoint

---

## 💾 IMPORTANT CONTEXT

**GitHub OAuth Setup:**
- OAuth App created in GitHub Settings
- Client ID: stored in .env
- Client Secret: stored in .env
- Callback URL: http://localhost:3000/api/auth/callback/github

**Dependencies Installed:**
- @auth/core@0.18.0
- next-auth@5.0.0-beta.4

**Tech Stack:**
- Next.js 14 App Router
- TypeScript 5.3+
- Prisma for database

---

## 🚨 BLOCKERS

[Если есть блокеры, опиши детально]

---

## 📚 RESOURCES

**Related Docs:**
- docs/core/03_TECH_STACK.md - Tech stack details
- docs/core/04_ARCHITECTURE.md - Auth architecture
- docs/requirements/authentication.md - Full requirements

**Related Code:**
- src/auth/ - Auth module
- src/lib/ - Helper libraries

---

## 💾 CHECKPOINT

Checkpoint saved: `.dev/checkpoints/latest.json`

**Last commit:**
```
a1b2c3d feat(auth): implement GitHub OAuth token exchange
```

**Stats:**
- Files changed: 3
- Lines added: 187
- Lines deleted: 23
- Time spent: 2h 15min

---

## ✅ HOW TO CONTINUE

**For Cursor AI:**
```
1. Открой проект в Cursor
2. Прочитай этот handoff report
3. Прочитай .dev/checkpoints/latest.json
4. Открой src/auth/github-oauth.ts (line 145)
5. Продолжай разработку с callback handler
```

**For CLI Agent:**
```
1. cd [project_directory]
2. Read .dev/handoff/handoff-to-cli-YYYYMMDD.md
3. Read .dev/checkpoints/latest.json
4. Open src/auth/github-oauth.ts
5. Continue development
```

---

**Handoff Ready:** ✅  
**Agent can start:** Immediately  
**Estimated time to complete:** ~1-2 hours
```

---

## 📊 CHECKPOINT JSON FORMAT

**Полный формат:** См. `checkpoints/dev-checkpoint-system.md`

**Краткий пример:**

```json
{
  "type": "development_session",
  "session_id": "dev-web-20251115-143000",
  "timestamp": "2025-11-15T14:30:00Z",
  "mode": "WEB_GITHUB",
  
  "current_task": {
    "module": "Authentication",
    "feature": "GitHub OAuth Login",
    "status": "in_progress",
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
    "a1b2c3d: feat(auth): implement GitHub OAuth token exchange"
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

## ✅ BEST PRACTICES

**Для эффективной разработки:**

1. **Маленькие итерации:**
   - 1 итерация = 1 feature/fix
   - ~30-60 минут на итерацию
   - Commit после каждой итерации

2. **Checkpoint часто:**
   - После каждого commit
   - Каждые 30 минут (если есть изменения)
   - Перед началом новой задачи

3. **Следуй Project Rules:**
   - Автоматически обновляй docs
   - Синхронизируй code ↔ docs
   - Уведомляй о сработавших правилах

4. **Quality First:**
   - Code Quality Checklist
   - Tests перед commit
   - Comments для сложных участков

5. **Logging обязателен:**
   - Session log для каждой сессии
   - Iteration reports для каждой итерации
   - Handoff reports при передаче

---

**Версия:** 1.0.0  
**Последнее обновление:** 2025-11-15  
**Готов к использованию:** ✅

