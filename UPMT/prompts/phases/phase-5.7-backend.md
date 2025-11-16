# PHASE 5.7: BACKEND DOCUMENTATION (CONDITIONAL)

**Время выполнения:** 30-90 минут (автономно)

**Назначение:** Создание backend документации (entities, API, services, database)

**⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ**

---

## ⚡ ШАГ 0: ПРОВЕРКА - SKIP или ПРОДОЛЖИТЬ?

**Проверь триггеры:**

```python
IF (raw_data_mentions_backend OR tech_stack_has_backend_framework):
    EXECUTE PHASE 5.7
ELSE:
    SKIP → ПЕРЕХОД К PHASE 6
```

**Триггеры для выполнения:**
- ✅ Raw data содержит backend спецификации (API endpoints, database schema, entities)
- ✅ Tech stack включает backend framework (Express, Fastify, NestJS, Django, etc.)
- ✅ Проект типа требует backend (web app, mobile backend, SaaS)

**ЕСЛИ НИ ОДИН ТРИГГЕР НЕ СРАБОТАЛ:**
- ⏭️ **SKIP PHASE 5.7**
- → Переход к PHASE 6

**ЕСЛИ ХОТЯ БЫ ОДИН ТРИГГЕР СРАБОТАЛ:**
- ✅ **ПРОДОЛЖАЙ PHASE 5.7**

---

## 📋 ИНСТРУКЦИИ (если продолжаем)

### ШАГ 1: Анализ Backend Data (10 минут)

**⚠️ КРИТИЧНО: Обработка больших файлов**

**Используй `safe_read_file()` из адаптера для автоматической обработки больших файлов.**

**Алгоритм:**
1. Для каждого файла вызывай `safe_read_file(file_path)`
2. Если файл большой (>256KB или >25000 токенов) - функция автоматически прочитает по частям
3. Объедини все части перед анализом

**Определи стратегию:**

| Сценарий | Источник данных | Стратегия |
|----------|-----------------|-----------|
| A) Raw data содержит backend спецификации | Чаты/документы с API, entities, database | Генерация из raw data (100% точность) |
| B) Только tech stack упоминания | Express/PostgreSQL упомянуты, детали отсутствуют | Intelligent inference |
| C) Частичные данные | Некоторые entities/API упомянуты | Гибрид: raw data + inference |

**Извлеки из raw data (если есть):**

**Файлы для чтения:**
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md` → `safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")` (может быть очень большим)
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md` → `safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")`

**⚠️ ВАЖНО:** 
- НЕ ПРОПУСКАЙ файлы из-за размера
- Функция автоматически обработает большие файлы
- Детали алгоритма см. в `cli-adapter.md` / `web-adapter.md`

**Извлеки:**
- Упоминания сущностей (User, Project, Task, etc.)
- Упоминания API endpoints
- Упоминания database tables
- Упоминания backend services
- Архитектурные решения (REST vs GraphQL, monolith vs microservices)

**Используй `extracted_features.md`:**
- Функции часто подразумевают entities
- Пример: "User can create projects" → entities: User, Project

---

### ШАГ 2: Intelligent Inference (если данных нет/мало)

**Основа для inference:**

**A) Из типа проекта:**

| Тип проекта | Предполагаемые entities | Предполагаемые services |
|-------------|------------------------|------------------------|
| Task Manager | User, Project, Task, Comment, Tag | Auth, Tasks, Notifications, Teams |
| E-commerce | User, Product, Category, Order, Cart, Payment | Auth, Catalog, Orders, Payments, Shipping |
| Social Network | User, Post, Comment, Like, Follow, Message | Auth, Posts, Feed, Messaging, Notifications |

**B) Из функций (`extracted_features.md`):**

```
Function: "Users can register and login"
→ Entity: User (email, password_hash, name)
→ Service: Auth Service
→ API: POST /auth/register, POST /auth/login

Function: "Users can create and manage projects"
→ Entity: Project (name, description, owner_id)
→ Relationships: User ||--o{ Project
→ API: POST /projects, GET /projects, GET /projects/:id
```

**C) Из tech stack:**

| Tech Stack | Следствия |
|------------|-----------|
| PostgreSQL | Relational entities, foreign keys, migrations, ERD diagrams |
| MongoDB | Document-based entities, no strict schema |
| Express/Fastify | RESTful API, middleware, route-based structure |
| NestJS | Module-based, services, controllers, decorators |

---

### ШАГ 3: Генерация Backend Documentation (30-60 минут)

**Используй templates из:**
```
UPMT/structure-templates/backend-documentation/
```

**Создай структуру:**

```
docs/
├── backend/
│   ├── 00_BACKEND_OVERVIEW.md
│   ├── entities/
│   │   ├── 00_ENTITY_CATALOG.md
│   │   └── [entity-name].md (для каждой entity)
│   ├── api/
│   │   ├── 00_API_OVERVIEW.md
│   │   └── [resource]-api.md (для каждого resource)
│   ├── services/
│   │   ├── 00_SERVICES_CATALOG.md
│   │   └── [service-name]-service.md
│   └── database/
│       ├── 00_DATABASE_SCHEMA.md
│       └── relationships.md
│
└── adr/
    ├── 00_ADR_INDEX.md
    └── [number]-[title].md (ADRs)
```

---

### ШАГ 4: Backend Overview (5 минут)

**Создай `docs/backend/00_BACKEND_OVERVIEW.md`:**

```markdown
# Backend Architecture Overview

## Stack
- **Runtime:** [Node.js 22 / Python 3.12]
- **Framework:** [Express / Fastify / Django]
- **Database:** [PostgreSQL 16 / MongoDB 7]
- **ORM:** [Prisma / Drizzle / TypeORM]

## Architecture Pattern
[Monolith / Modular Monolith / Microservices]

## Key Entities
[List of 5-10 main entities]

## API Design
[REST / GraphQL / tRPC / Hybrid]
```

---

### ШАГ 5: Entities Documentation (20-30 минут)

**Для каждой обнаруженной/inferred entity:**

**Используй template:**
```
UPMT/structure-templates/backend-documentation/_ENTITY_TEMPLATE.md
```

**Создай:** `docs/backend/entities/[entity-name].md`

**Заполни секции:**
- Overview
- Database Schema
- TypeScript Type
- Relationships (Mermaid ERD)
- API Endpoints
- Frontend Mapping
- Permissions

**Пример inference для User entity:**

```markdown
# User Entity

## Overview
User entity represents a person who can interact with the system.

**Type:** Core  
**Module:** Authentication

## Database Schema

\```sql
CREATE TABLE users (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email             VARCHAR(255) UNIQUE NOT NULL,
  name              VARCHAR(100) NOT NULL,
  password_hash     VARCHAR(255) NOT NULL,
  avatar_url        VARCHAR(500),
  role              VARCHAR(20) DEFAULT 'user',
  is_active         BOOLEAN DEFAULT true,
  created_at        TIMESTAMP DEFAULT NOW(),
  updated_at        TIMESTAMP DEFAULT NOW()
);
\```

## Relationships

\```mermaid
erDiagram
    USER ||--o{ PROJECT : owns
    USER ||--o{ TASK : "assigned to"
    USER }o--o{ TEAM : "member of"
\```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/users/:id | Get user by ID |
| PATCH | /api/users/:id | Update user |
| DELETE | /api/users/:id | Delete user (soft) |

## Permissions

| Action | Admin | User | Guest |
|--------|-------|------|-------|
| Read own | ✅ | ✅ | ❌ |
| Update own | ✅ | ✅ | ❌ |
| Delete own | ✅ | ✅ | ❌ |
```

---

### ШАГ 6: Entity Catalog with ERD (10 минут)

**Создай `docs/backend/entities/00_ENTITY_CATALOG.md`:**

**Включи:**
1. Master Mermaid ERD со ВСЕМИ entities и relationships
2. Entity Table
3. Relationships Matrix

---

### ШАГ 7: API Documentation (10-15 минут)

**Создай `docs/backend/api/00_API_OVERVIEW.md`:**
- API design principles (REST/GraphQL)
- Authentication strategy (JWT/OAuth)
- Conventions (naming, versioning, error format)

**Для каждого resource:**
- Используй template `_API_ENDPOINT_TEMPLATE.md`
- Создай `docs/backend/api/[resource]-api.md`
- Минимум: GET, POST, PATCH, DELETE endpoints

---

### ШАГ 8: Architecture Decision Records (10 минут)

**Создай `docs/adr/` (минимум 3 ADRs):**

1. **ADR-001: Database Choice** (PostgreSQL/MongoDB/etc)
2. **ADR-002: Architecture Pattern** (Monolith/Microservices)
3. **ADR-003: Authentication** (JWT/OAuth)

**Используй template:**
```
UPMT/structure-templates/backend-documentation/_ADR_TEMPLATE.md
```

---

### ШАГ 9: Integration (5 минут)

**Обнови `docs/core/04_ARCHITECTURE.md`:**

Добавь секцию:
```markdown
## Backend Architecture

See detailed backend documentation:
- [Backend Overview](../backend/00_BACKEND_OVERVIEW.md)
- [Entity Catalog](../backend/entities/00_ENTITY_CATALOG.md)
- [API Overview](../backend/api/00_API_OVERVIEW.md)
- [Architecture Decisions](../adr/00_ADR_INDEX.md)
```

**Обнови module requirements:**

Добавь Section 8: Backend Integration в каждый `docs/requirements/[module]_requirements.md`

---

## 💾 CHECKPOINT

**⚠️ КРИТИЧНО: Checkpoint ДОЛЖЕН быть сохранен после завершения PHASE 5.7!**

**1. Сохранить JSON Checkpoint (ОБЯЗАТЕЛЬНО!):**

```python
save_checkpoint(
    phase_number=5.7,  # или 5 с маркером backend
    phase_name="PHASE 5.7: Backend Documentation",
    batch=None,
    state={
        "current_action": "Backend documentation complete",
        "files_created": [
            "docs/backend/00_BACKEND_OVERVIEW.md",
            "docs/backend/entities/*",
            "docs/backend/api/*",
            "docs/backend/services/*",
            "docs/backend/database/*",
            "docs/adr/*"
        ],
        "context_files": [
            "extracted_features.md",
            "modules_list.md",
            "PROJECT_SYNTHESIS.md",
            "docs/backend/00_BACKEND_OVERVIEW.md"
        ]
    }
)
```

**2. Git Checkpoint:**

```bash
git add docs/backend/
git add docs/adr/
git add docs/core/04_ARCHITECTURE.md # обновлённый
git add docs/requirements/ # обновлённые
git add .upmt/checkpoints/
git commit -m "docs(bootstrap): PHASE 5.7 complete - backend documented ([N] entities, [M] endpoints)"
git push
```

**Показать итоги:**

```markdown
✅ PHASE 5.7 COMPLETE

**Backend Documentation:**
- ✅ Backend overview
- ✅ Entities: [N] documented
- ✅ API endpoints: [M] documented
- ✅ ADRs: [K] created
- ✅ Mermaid ERDs included

**Strategy:** [Raw data / Intelligent inference / Hybrid]

**Next:** PHASE 6 - Final Setup Instructions

⏱️ PHASE 5.7 завершена за [время]
```

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
→ ПЕРЕХОД К PHASE 6: FINAL SETUP INSTRUCTIONS
→ Прочитай: UPMT/prompts/phases/phase-6-setup.md
```

