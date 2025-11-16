# All Project Rules - Проектные Правила для Всех Файлов

**Версия:** 2.0.1 (UPMT Structure)  
**Дата:** 2025-11-10  
**Назначение:** Мастер-файл всех проектных правил с обновлёнными путями для UPMT структуры

---

## 📋 КАК ИСПОЛЬЗОВАТЬ ЭТОТ ФАЙЛ

### Для пользователя:
1. **Этот файл НЕ нужно редактировать** - он справочный
2. Cursor автоматически использует эти правила при работе с проектом
3. Правила срабатывают по триггерам (см. каждое правило)
4. В начале работы правила выведут: "👀 ACTIVE: [RULE_NAME]"
5. В конце работы: "✅ [RULE_NAME]: обновлены [файлы] по триггеру [X]"

### Для Claude/Cursor:
- При начале работы с файлом → проверь его правило
- Выведи "👀 ACTIVE: [RULE_NAME]" в начале
- Следуй триггерам и действиям
- В конце выведи "✅ [RULE_NAME]: результат"

---

## 🎯 ОГЛАВЛЕНИЕ ПРАВИЛ

1. [RULE_01: metadata.yaml](#rule_01-metadatayaml)
2. [RULE_02: PROJECT_ESSENCE.md](#rule_02-project_essencemd)
3. [RULE_03: PRD.md](#rule_03-prdmd)
4. [RULE_04: ROADMAP.md](#rule_04-roadmapmd)
5. [RULE_05: TECH_STACK.md](#rule_05-tech_stackmd)
6. [RULE_06: ARCHITECTURE.md](#rule_06-architecturemd)
7. [RULE_07: module_requirements](#rule_07-module_requirements)
8. [RULE_08: state.md](#rule_08-statemd)
9. [RULE_09: decisions.md](#rule_09-decisionsmd)
10. [RULE_10: insights.md](#rule_10-insightsmd)
11. [RULE_11: changes_log.md](#rule_11-changes_logmd)
12. [RULE_12: modules_status.md](#rule_12-modules_statusmd)
13. [RULE_13: sprint_current.md](#rule_13-sprint_currentmd)
14. [RULE_14: backlog.md](#rule_14-backlogmd)
15. [RULE_15: .cursorrules](#rule_15-cursorrules)
16. [RULE_16: VERSION_HISTORY.md](#rule_16-version_historymd)
17. [RULE_17: Entity Documentation](#rule_17-entity-documentation)
18. [RULE_18: API Documentation](#rule_18-api-documentation)
19. [RULE_19: Database Schema](#rule_19-database-schema)
20. [RULE_20: ADR (Architecture Decision Records)](#rule_20-adr-architecture-decision-records)
21. [RULE_21: Testing Documentation](#rule_21-testing-documentation)
22. [RULE_22: Security Documentation](#rule_22-security-documentation)
23. [RULE_23: Services & Integrations](#rule_23-services--integrations)

---

## RULE_01: metadata.yaml

### 👀 Активация в начале
```
"👀 ACTIVE: RULE_01_METADATA - Проверяю триггеры для metadata.yaml"
```

### 📁 Файл
`.upmt/metadata.yaml`

**ИЗМЕНЕНИЕ В UPMT:** Был `00_RAW_DATA_TEMPLATE/metadata.yaml`, теперь `.upmt/metadata.yaml`

### 🎯 Назначение
Метаданные проекта, AUTO-FILLED при bootstrap, источник истины для основной информации.

### ⚡ Триггеры (когда правило срабатывает)
1. **Bootstrap PHASE 2** - AUTO-FILL режим
2. **Изменение docs/core/00_PROJECT_ESSENCE.md** (секции: vision, audience, core features)
3. **Добавление новой технологии в docs/core/03_TECH_STACK.md**
4. **Изменение названия проекта**
5. **Изменение целевой аудитории**
6. **Добавление/удаление core feature**

### 🔄 Действия при срабатывании
При любом триггере:
1. Прочитать изменённые данные
2. Обновить соответствующие поля в `.upmt/metadata.yaml`
3. Установить last_updated: текущая дата
4. Сохранить файл

### ✅ Уведомление в конце
```
"✅ RULE_01_METADATA: обновлён .upmt/metadata.yaml [fields: project.name, project.target_audience] по триггеру: PROJECT_ESSENCE изменён"
```

---

## RULE_02: PROJECT_ESSENCE.md

### 📁 Файл
`docs/core/00_PROJECT_ESSENCE.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROJECT_CORE/00_PROJECT_ESSENCE.md`

### ⚡ Триггеры
1. **Изменение vision/mission**
2. **Изменение целевой аудитории**
3. **Добавление/удаление core value**
4. **Изменение success criteria**

### 🔄 Действия при срабатывании
1. Обновить `.upmt/metadata.yaml` (RULE_01)
2. Проверить что `docs/core/01_PRD.md` aligned с новым vision
3. Залогировать изменение в `.context/decisions.md` (RULE_09)
4. Обновить `.context/state.md` (RULE_08)

### ✅ Уведомление
```
"✅ RULE_02_PROJECT_ESSENCE: обновлены [.upmt/metadata.yaml, .context/decisions.md] по триггеру: vision изменён"
```

---

## RULE_03: PRD.md

### 📁 Файл
`docs/core/01_PRD.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROJECT_CORE/01_PRD.md`

### ⚡ Триггеры
1. **Добавление новой фичи**
2. **Изменение приоритета фичи**
3. **Изменение статуса фичи**
4. **Удаление фичи**

### 🔄 Действия при срабатывании
1. Обновить `docs/progress/backlog.md` (RULE_14)
2. Если добавлена фича → создать соответствующий `docs/requirements/[module]_requirements.md` (RULE_07)
3. Обновить `docs/progress/modules_status.md` (RULE_12)
4. Залогировать в `.context/decisions.md` (RULE_09)

### ✅ Уведомление
```
"✅ RULE_03_PRD: добавлена новая фича [Feature X], созданы [docs/requirements/feature-x_requirements.md, обновлён backlog.md]"
```

---

## RULE_04: ROADMAP.md

### 📁 Файл
`docs/core/02_ROADMAP.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROJECT_CORE/02_ROADMAP.md`

### ⚡ Триггеры
1. **Изменение Phase dates**
2. **Добавление нового Milestone**
3. **Изменение статуса Phase**

### 🔄 Действия
1. Обновить `docs/progress/sprint_current.md` если текущая фаза изменена
2. Залогировать в `.context/decisions.md`

---

## RULE_05: TECH_STACK.md

### 📁 Файл
`docs/core/03_TECH_STACK.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROJECT_CORE/03_TECH_STACK.md`

### ⚡ Триггеры
1. **Добавление новой технологии**
2. **Изменение версии**
3. **Удаление технологии**

### 🔄 Действия
1. Обновить `.upmt/metadata.yaml` (секция tech_stack)
2. Обновить `.cursorrules` (RULE_15) с новыми технологиями
3. Залогировать в `.context/decisions.md`

---

## RULE_06: ARCHITECTURE.md

### 📁 Файл
`docs/core/04_ARCHITECTURE.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROJECT_CORE/04_ARCHITECTURE.md`

### ⚡ Триггеры
1. **Изменение архитектурного паттерна**
2. **Добавление нового сервиса/компонента**
3. **Изменение Data Model**

### 🔄 Действия
1. Залогировать архитектурное решение в `.context/decisions.md`
2. Обновить affected module requirements в `docs/requirements/`

---

## RULE_07: module_requirements

### 📁 Файлы
`docs/requirements/[module_name]_requirements.md`

**ИЗМЕНЕНИЕ В UPMT:** Были `02_PROJECT_STRUCTURE/MODULES_REQUIREMENTS/[module_name]_requirements.md`

### ⚡ Триггеры
1. **Добавление нового FR (Functional Requirement)**
2. **Изменение статуса FR**
3. **Добавление нового модуля**

### 🔄 Действия
1. При добавлении FR → обновить `docs/progress/backlog.md`
2. При изменении статуса → обновить `docs/progress/modules_status.md`
3. Залогировать в `.context/changes_log.md`

---

## RULE_08: state.md

### 📁 Файл
`.context/state.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/CONTEXT_MEMORY/state.md`

### ⚡ Триггеры
1. **После завершения любой задачи**
2. **Изменение Current Phase**
3. **Добавление блокера**

### 🔄 Действия
Обновить автоматически:
- LAST COMPLETED
- CURRENT FOCUS
- PROGRESS
- BLOCKERS

---

## RULE_09: decisions.md

### 📁 Файл
`.context/decisions.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/CONTEXT_MEMORY/decisions.md`

### ⚡ Триггеры
1. **Любое архитектурное решение**
2. **Выбор технологии**
3. **Изменение приоритетов**

### 🔄 Действия
Добавить новую запись с:
- Date
- Decision
- Reasoning
- Impact

---

## RULE_10: insights.md

### 📁 Файл
`.context/insights.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/CONTEXT_MEMORY/insights.md`

### ⚡ Триггеры
1. **Обнаружение паттерна в коде**
2. **Урок из ошибки**
3. **Оптимизация найдена**

---

## RULE_11: changes_log.md

### 📁 Файл
`.context/changes_log.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/CONTEXT_MEMORY/changes_log.md`

### ⚡ Триггеры
1. **Завершение фичи**
2. **Критическое изменение**

---

## RULE_12: modules_status.md

### 📁 Файл
`docs/progress/modules_status.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROGRESS_TRACKING/modules_status.md`

### ⚡ Триггеры
1. **Изменение статуса модуля**
2. **Обновление прогресса**

### 🔄 Действия
Обновить таблицу со статусами всех модулей

---

## RULE_13: sprint_current.md

### 📁 Файл
`docs/progress/sprint_current.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROGRESS_TRACKING/sprint_current.md`

### ⚡ Триггеры
1. **Начало нового спринта**
2. **Завершение задачи в спринте**

---

## RULE_14: backlog.md

### 📁 Файл
`docs/progress/backlog.md`

**ИЗМЕНЕНИЕ В UPMT:** Был `02_PROJECT_STRUCTURE/PROGRESS_TRACKING/backlog.md`

### ⚡ Триггеры
1. **Добавление задачи из PRD**
2. **Изменение приоритета**
3. **Перенос задачи в спринт**

---

## RULE_15: .cursorrules

### 📁 Файл
`.cursorrules` (в корне проекта)

### ⚡ Триггеры
1. **Изменение tech stack**
2. **Добавление нового модуля**
3. **Изменение project name**

### 🔄 Действия
Обновить AUTO-GENERATED секцию с:
- Project info
- Tech stack
- Module list
- File paths (с UPMT структурой!)

---

## RULE_16: VERSION_HISTORY.md

### 📁 Файл
`UPMT/VERSION_HISTORY.md` (в UPMT, не в проекте!)

**ИЗМЕНЕНИЕ В UPMT:** Был в корне template

### ⚡ Триггеры
1. **Изменения в UPMT системе**
2. **Major version bump**

### 🔄 Действия
Добавить запись о версии UPMT (НЕ проекта!)

---

## RULE_17: DESIGN SYSTEM SYNC

### 📁 Файлы
- `docs/design/foundation/*` - Design tokens (colors, typography, spacing, etc.)
- `docs/design/components/*.md` - Component documentation
- `docs/design/patterns/*.md` - Design patterns
- `docs/design/resources/design-tokens.json` - Machine-readable tokens
- `docs/design/resources/changelog.md` - Design system changes
- `docs/requirements/*_requirements.md` - Module requirements (section 7: UI/UX)
- `docs/design/screens/*.md` - Screen-level documentation

**NEW IN UPMT v2.2.0:** Design System integration

### ⚡ Триггеры

1. **Design Token изменен** (`docs/design/foundation/*`)
   - Color added/changed
   - Typography updated
   - Spacing adjusted
   - Elevation/motion/iconography modified

2. **Component добавлен/изменен** (`docs/design/components/*`)
   - New component created
   - Component variant added
   - Component behavior changed
   - Component deprecated

3. **UI Element добавлен в Module Requirements**
   - New screen defined in `*_requirements.md` (section 7)
   - New component needed for module
   - User flow updated

4. **Design Pattern established** (`docs/design/patterns/*`)
   - New pattern documented
   - Existing pattern updated

### 🔄 Действия

#### При изменении Design Tokens:

1. **Update design-tokens.json:**
   ```bash
   docs/design/resources/design-tokens.json
   ```
   - Sync changed token values
   - Maintain version consistency

2. **Update changelog:**
   ```bash
   docs/design/resources/changelog.md
   ```
   - Add entry with date, change description
   - Tag version if breaking change

3. **Notify team:**
   - Log in `.context/changes_log.md`
   - Tag as "DESIGN SYSTEM UPDATE"

---

#### При добавлении/изменении Component:

1. **Ensure component documented:**
   - Create/update `docs/design/components/[name].md`
   - Use `UPMT/structure-templates/_COMPONENT_TEMPLATE.md` for new components
   - Include: anatomy, variants, states, accessibility, examples

2. **Update changelog:**
   ```bash
   docs/design/resources/changelog.md
   ```
   - Document what changed (Added/Changed/Deprecated)

3. **Check dependencies:**
   - Review if other components affected
   - Update related component docs if needed

4. **Update module requirements:**
   - If component relates to specific module
   - Add reference in `docs/requirements/[module]_requirements.md` (section 7.2)

---

#### При добавлении UI Element в Module Requirements:

**Context:** Developer adds screen/component to module requirements (section 7)

1. **Check if component exists:**
   - Look in `docs/design/components/`
   - If missing → should be created first

2. **Create screen documentation** (if major screen):
   ```bash
   docs/design/screens/[module]-[screen-name].md
   ```
   - Use `docs/design/screens/_SCREEN_TEMPLATE.md`
   - Document layout, components used, flows, states

3. **Validate design consistency:**
   - Components match design system
   - Patterns from `docs/design/patterns/` reused
   - Accessibility requirements met

4. **Link design artifacts:**
   - Figma link in module requirements
   - Component links in section 7.2
   - Pattern links in section 7.6

---

#### При создании нового Design Pattern:

1. **Document pattern:**
   ```bash
   docs/design/patterns/[pattern-name].md
   ```
   - Problem it solves
   - When to use
   - Examples
   - Related components

2. **Update changelog:**
   ```bash
   docs/design/resources/changelog.md
   ```

3. **Reference in related docs:**
   - Add to `docs/design/00_DESIGN_SYSTEM.md` if major pattern
   - Link from relevant module requirements

---

### 🎯 Design System Maintenance Workflow

**When design changes:**
```
1. Update Figma (source of truth)
2. Update foundation docs (if tokens changed)
3. Update component docs (if components changed)
4. Export design-tokens.json (if needed)
5. Update changelog
6. Notify dev team (via .context/changes_log.md)
7. Update affected module requirements
```

**When new feature designed:**
```
1. Design in Figma (reuse existing components)
2. Document in module requirements (section 7)
3. Create screen docs (if major screen)
4. Reference existing patterns
5. Create new components ONLY if no existing match
   → Document with _COMPONENT_TEMPLATE.md
6. Update changelog
```

---

### ✅ Checklist for Design Changes

- [ ] Figma updated (source of truth)
- [ ] Foundation docs updated (if tokens changed)
- [ ] Component docs updated (if component changed)
- [ ] design-tokens.json exported (if changed)
- [ ] Changelog updated
- [ ] Module requirements updated (if feature-related)
- [ ] Screen docs created (if new major screen)
- [ ] Team notified via changes_log.md
- [ ] Accessibility verified (WCAG AA)

---

### 🔗 Related Files

**Design System Core:**
- `docs/design/00_DESIGN_SYSTEM.md` - Overview
- `docs/design/foundation/*` - Tokens
- `docs/design/components/*` - Components
- `docs/design/patterns/*` - Patterns
- `docs/design/resources/` - Tokens, links, changelog

**Module Integration:**
- `docs/requirements/*_requirements.md` (section 7: UI/UX)
- `docs/design/screens/*.md` - Screen docs
- `UPMT/structure-templates/_COMPONENT_TEMPLATE.md` - New component template
- `docs/design/screens/_SCREEN_TEMPLATE.md` - New screen template

**Context:**
- `.context/changes_log.md` - All changes logged here
- `.upmt/metadata.yaml` - Design info tracked

---

### 💡 Notes

**Design System = Single Source of Truth:**
- Figma is visual source of truth
- docs/design/ is documentation source of truth
- design-tokens.json is code source of truth

**When in doubt:**
- Reuse existing components > create new
- Follow existing patterns > invent new
- Document > assume

**Accessibility is NOT optional:**
- All components must meet WCAG 2.1 AA
- Test with keyboard + screen reader
- Verify contrast ratios

---

## 📝 ВАЖНО: НОВЫЕ ПУТИ В UPMT СТРУКТУРЕ

### Mapping старых путей → новых:

```
СТАРЫЕ ПУТИ (v2.0.0):
02_PROJECT_STRUCTURE/PROJECT_CORE/*.md
02_PROJECT_STRUCTURE/MODULES_REQUIREMENTS/*.md
02_PROJECT_STRUCTURE/CONTEXT_MEMORY/*.md
02_PROJECT_STRUCTURE/PROGRESS_TRACKING/*.md
00_RAW_DATA_TEMPLATE/metadata.yaml

НОВЫЕ ПУТИ (v2.0.1 UPMT):
docs/core/*.md
docs/requirements/*.md
.context/*.md
docs/progress/*.md
.upmt/metadata.yaml
```

### Template файлы перемещены в:
```
UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md (этот файл)
UPMT/structure-templates/*_TEMPLATE.md
UPMT/bootstrap/00_RAW_DATA_TEMPLATE/
UPMT/bootstrap/BOOTSTRAP_CONFIG/
```

---

## RULE_17: Entity Documentation

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если backend documentation существует.**

**Проверка:**
```
IF (docs/backend/ directory exists):
    ACTIVATE RULE_17
ELSE:
    SKIP RULE_17
```

**Создание backend docs:** Происходит в PHASE 5.7 bootstrap процесса (см. BOOTSTRAP_START_PROMPT.md)

### 📁 Файлы
- `docs/backend/entities/00_ENTITY_CATALOG.md` - Master entity list
- `docs/backend/entities/{entity_name}.md` - Individual entity docs
- `docs/backend/entities/_ENTITY_TEMPLATE.md` - Template

### ⚡ Триггеры
1. **Создание новой таблицы в database schema**
2. **Добавление нового entity/model в коде**
3. **Изменение структуры entity** (добавление/удаление полей)
4. **Изменение relationships** (foreign keys)
5. **Создание API endpoint для entity**

### 🔄 Действия при срабатывании
**При создании нового entity:**
1. Создать `docs/backend/entities/{entity_name}.md` из `_ENTITY_TEMPLATE.md`
2. Заполнить все секции (DB schema, relationships, API, frontend mapping)
3. Добавить entity в `00_ENTITY_CATALOG.md` (таблица + Mermaid ERD)
4. Обновить relationships matrix в catalog
5. Обновить `docs/backend/database/00_DATABASE_SCHEMA.md` (если нужно)

**При изменении entity:**
1. Обновить секцию "Structure" в entity.md
2. Обновить Mermaid diagram в `00_ENTITY_CATALOG.md` (если relationship изменился)
3. Проверить API endpoints documentation (RULE_18)
4. Залогировать в `.context/changes_log.md`

### ✅ Уведомление в конце
```
"✅ RULE_17_ENTITY: создан/обновлён docs/backend/entities/task.md + обновлён ENTITY_CATALOG.md по триггеру: новая таблица 'tasks' добавлена в schema"
```

---

## RULE_18: API Documentation

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если backend documentation существует.**

**Проверка:** IF (docs/backend/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/backend/api/00_API_OVERVIEW.md` - API overview
- `docs/backend/api/{resource}-api.md` - API endpoints
- `docs/backend/api/_API_ENDPOINT_TEMPLATE.md` - Template

### ⚡ Триггеры
1. **Создание нового API endpoint** (GET/POST/PATCH/DELETE)
2. **Изменение API response format**
3. **Добавление query параметров**
4. **Изменение authentication/authorization**
5. **Создание нового resource** (например, projects → projects-api.md)

### 🔄 Действия при срабатывании
**При создании нового endpoint:**
1. Добавить endpoint в соответствующий `{resource}-api.md`
2. Документировать: HTTP method, URL, auth, params, request body, response, errors
3. Добавить примеры curl/code
4. Обновить `docs/backend/resources/openapi-template.yaml`
5. Обновить `docs/backend/resources/postman-collection.json`
6. Ссылка на related entity documentation (RULE_17)

**При изменении endpoint:**
1. Обновить секцию endpoint
2. Отметить deprecated (если применимо)
3. Залогировать breaking change в `.context/changes_log.md`

### ✅ Уведомление в конце
```
"✅ RULE_18_API: обновлён docs/backend/api/tasks-api.md (добавлен endpoint POST /api/tasks/:id/assign) + обновлён openapi-template.yaml"
```

---

## RULE_19: Database Schema

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если backend documentation существует.**

**Проверка:** IF (docs/backend/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/backend/database/00_DATABASE_SCHEMA.md` - Complete schema
- `docs/backend/database/relationships.md` - ERD diagrams
- `docs/backend/database/migrations.md` - Migration docs

### ⚡ Триггеры
1. **Создание database migration** (новая таблица, изменение schema)
2. **Добавление/изменение foreign key**
3. **Создание/удаление index**
4. **Изменение column** (тип, nullable, default)
5. **Добавление constraint** (CHECK, UNIQUE)

### 🔄 Действия при срабатывании
**При migration:**
1. Обновить `00_DATABASE_SCHEMA.md` (секция Tables Reference)
2. Добавить/обновить Mermaid ERD diagram
3. Обновить `relationships.md` (если FK изменён)
4. Документировать migration в `migrations.md`
5. Обновить entity documentation (RULE_17)
6. Обновить indexes documentation (если index добавлен)

**При изменении relationships:**
1. Обновить Mermaid ERD в `relationships.md`
2. Обновить relationships matrix в entity catalog
3. Проверить cascade delete rules

### ✅ Уведомление в конце
```
"✅ RULE_19_DATABASE: обновлён 00_DATABASE_SCHEMA.md + relationships.md по триггеру: migration 20251110_add_task_assignments_table.sql"
```

---

## RULE_20: ADR (Architecture Decision Records)

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если ADR documentation существует.**

**Проверка:** IF (docs/adr/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/adr/00_ADR_INDEX.md` - ADR index
- `docs/adr/{number}-{title}.md` - Individual ADRs
- `docs/adr/_ADR_TEMPLATE.md` - Template

### ⚡ Триггеры
1. **Принятие архитектурного решения** (выбор tech stack, pattern, tool)
2. **Изменение existing ADR status** (Superseded, Deprecated)
3. **Добавление альтернативы в ADR**
4. **Review date наступила**

### 🔄 Действия при срабатывании
**При новом решении:**
1. Создать `docs/adr/{number}-{decision-title}.md` из `_ADR_TEMPLATE.md`
2. Заполнить секции: Context, Decision, Alternatives, Consequences
3. Добавить в `00_ADR_INDEX.md` (таблица Active Decisions)
4. Залогировать в `.context/decisions.md` (RULE_09)
5. Обновить related documentation (TECH_STACK, ARCHITECTURE)

**При superseding ADR:**
1. Обновить старый ADR: Status → Superseded, добавить ссылку на новый ADR
2. Переместить из Active Decisions в Superseded section в index
3. Создать новый ADR с ссылкой на старый

### ✅ Уведомление в конце
```
"✅ RULE_20_ADR: создан docs/adr/004-use-redis-cache.md + обновлён ADR_INDEX.md по триггеру: принято решение о caching strategy"
```

---

## RULE_21: Testing Documentation

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если testing documentation существует.**

**Проверка:** IF (docs/testing/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/testing/00_TESTING_STRATEGY.md` - Strategy overview
- `docs/testing/unit-testing.md` - Unit tests guide
- `docs/testing/integration-testing.md` - Integration tests
- `docs/testing/e2e-testing.md` - E2E tests
- `docs/testing/test-coverage.md` - Coverage targets

### ⚡ Триггеры
1. **Создание нового test file**
2. **Добавление нового testing tool** (Jest, Playwright, etc.)
3. **Изменение test coverage targets**
4. **Добавление critical E2E flow**
5. **Изменение testing strategy**

### 🔄 Действия при срабатывании
**При новом testing tool:**
1. Обновить `00_TESTING_STRATEGY.md` (секция Tools)
2. Создать/обновить соответствующий test guide (unit/integration/e2e)
3. Обновить `.context/changes_log.md`

**При изменении coverage:**
1. Обновить `test-coverage.md` (Coverage Targets table)
2. Обновить CI/CD pipeline docs (если thresholds changed)

**При новом E2E flow:**
1. Добавить в `e2e-testing.md` (Critical Flows list)
2. Документировать test scenario

### ✅ Уведомление в конце
```
"✅ RULE_21_TESTING: обновлён docs/testing/e2e-testing.md (добавлен flow 'Complete payment') + обновлён TESTING_STRATEGY.md"
```

---

## RULE_22: Security Documentation

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если security documentation существует.**

**Проверка:** IF (docs/security/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/security/00_SECURITY_OVERVIEW.md` - Security overview
- `docs/security/authentication.md` - Auth implementation
- `docs/security/authorization.md` - Permissions
- `docs/security/security-checklist.md` - Security checklist

### ⚡ Триггеры
1. **Изменение authentication mechanism** (JWT, OAuth, etc.)
2. **Добавление нового security control** (rate limiting, encryption)
3. **Security vulnerability discovered**
4. **Изменение permissions/roles**
5. **Security audit completed**
6. **Compliance requirement added** (GDPR, etc.)

### 🔄 Действия при срабатывании
**При изменении auth:**
1. Обновить `authentication.md`
2. Обновить related ADR (если архитектурное решение)
3. Обновить security checklist
4. Залогировать в `.context/changes_log.md` (критично!)

**При vulnerability:**
1. Документировать в `vulnerability-management.md`
2. Создать incident response entry (если применимо)
3. Обновить security checklist с new check

**При audit:**
1. Обновить `security-checklist.md` с findings
2. Документировать remediation steps

### ✅ Уведомление в конце
```
"✅ RULE_22_SECURITY: обновлён docs/security/authentication.md + security-checklist.md по триггеру: изменён JWT expiration (15min → 30min)"
```

---

## RULE_23: Services & Integrations

### ⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ

**Это правило активно ТОЛЬКО если services/integrations documentation существует.**

**Проверка:** IF (docs/backend/services/ OR docs/backend/integrations/ exists) → ACTIVATE, ELSE → SKIP

### 📁 Файлы
- `docs/backend/services/00_SERVICES_CATALOG.md` - Services catalog
- `docs/backend/services/{service}-service.md` - Service docs
- `docs/backend/integrations/00_INTEGRATIONS_MAP.md` - Integrations
- `docs/backend/integrations/{integration}.md` - Integration docs

### ⚡ Триггеры
1. **Создание нового service/module**
2. **Добавление external integration** (SendGrid, Stripe, etc.)
3. **Изменение service dependencies**
4. **Изменение service API contract**
5. **Добавление webhook/event handler**
6. **Изменение service communication pattern**

### 🔄 Действия при срабатывании
**При новом service:**
1. Создать `docs/backend/services/{service}-service.md` из `_SERVICE_TEMPLATE.md`
2. Добавить в `00_SERVICES_CATALOG.md` (Service Directory table)
3. Обновить Mermaid service dependency diagram
4. Документировать API endpoints (если есть)

**При новой integration:**
1. Создать `docs/backend/integrations/{integration}.md`
2. Добавить в `00_INTEGRATIONS_MAP.md` (Integration Catalog table)
3. Обновить Mermaid integration architecture diagram
4. Документировать: credentials location, rate limits, error handling
5. Обновить environment variables documentation

**При изменении dependencies:**
1. Обновить service dependency diagram в `00_SERVICES_CATALOG.md`
2. Проверить circular dependencies
3. Залогировать в `.context/changes_log.md`

### ✅ Уведомление в конце
```
"✅ RULE_23_SERVICES: создан docs/backend/integrations/stripe.md + обновлён INTEGRATIONS_MAP.md по триггеру: добавлена Stripe payment integration"
```

---

## 📊 СВОДКА ПО НОВЫМ ПРАВИЛАМ (17-23)

### Backend Documentation Rules

| Rule | Trigger Examples | Update Targets |
|------|------------------|----------------|
| **RULE_17** | New table, entity change | Entity docs, catalog, ERD |
| **RULE_18** | New endpoint, API change | API docs, OpenAPI, Postman |
| **RULE_19** | Migration, FK change | Schema docs, ERD, migrations |
| **RULE_20** | Architecture decision | ADR files, index, decisions.md |
| **RULE_21** | New test, coverage change | Testing docs, strategy |
| **RULE_22** | Security change, audit | Security docs, checklist |
| **RULE_23** | New service/integration | Services catalog, integration map |

### Cross-References

Backend documentation rules часто работают вместе:
- **RULE_17 + RULE_18:** Entity creation → API endpoints
- **RULE_17 + RULE_19:** Entity → Database schema
- **RULE_18 + RULE_23:** API endpoint → Service integration
- **RULE_20 + любое:** Architectural decision → Update ADR

### Automation Tips

При работе с backend:
1. **Entity-first approach:** Создали entity → автоматически триггерятся RULE_17, RULE_19
2. **API documentation:** Endpoint создан → RULE_18 обновляет 3 файла (doc, OpenAPI, Postman)
3. **Integration:** New external service → RULE_23 + security checklist (RULE_22)

---

**Все правила обновлены для UPMT структуры v2.0.1 + Backend Documentation** ✅
