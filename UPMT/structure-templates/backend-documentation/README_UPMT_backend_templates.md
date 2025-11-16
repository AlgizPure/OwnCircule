# Backend Documentation Templates

**Version:** 2.1  
**Last Updated:** 2025-11-11  
**Purpose:** Templates for backend documentation generation during UPMT bootstrap

---

## 📋 OVERVIEW

This directory contains **reusable templates** for backend documentation. These templates are used by Claude Code during the bootstrap process (PHASE 5.7) to generate backend documentation for your project.

**Key Concept:** These are TEMPLATES, not project-specific documentation. They contain placeholders and examples that Claude Code fills in based on:
1. Raw data analysis
2. Tech stack detection
3. Intelligent inference (when raw data is incomplete)

---

## 📄 AVAILABLE TEMPLATES

### 1. _ENTITY_TEMPLATE.md

**Purpose:** Document database entities (tables/models)

**Use When:** Claude Code detects or infers entities from:
- Database schema mentions in raw data
- Tech stack (e.g., PostgreSQL)
- Project type (e.g., web app → likely has users, projects)

**Covers:**
- Database schema
- TypeScript types
- Relationships (ERD diagrams)
- API endpoints
- Frontend mapping
- Permissions & validation

**Example Output:** `docs/backend/entities/user.md`

---

### 2. _API_ENDPOINT_TEMPLATE.md

**Purpose:** Document API endpoints

**Use When:** Claude Code detects or infers API structure from:
- Backend framework (e.g., Express, Fastify)
- RESTful mentions in raw data
- Standard CRUD operations for detected entities

**Covers:**
- Request/response formats
- Authentication & authorization
- Validation rules
- Error handling
- Usage examples (cURL, TypeScript, React)

**Example Output:** `docs/backend/api/users-api.md`

---

### 3. _SERVICE_TEMPLATE.md

**Purpose:** Document backend services/modules

**Use When:** Claude Code detects or infers service architecture from:
- Modular backend structure
- Business logic separation
- Microservices mentions

**Covers:**
- Service purpose & responsibilities
- Dependencies
- Data models
- Business logic & rules
- Events & state machines
- Performance & monitoring

**Example Output:** `docs/backend/services/auth-service.md`

---

### 4. _ADR_TEMPLATE.md

**Purpose:** Architecture Decision Records

**Use When:** Claude Code identifies architectural decisions from:
- Tech stack choices
- Raw data discussions
- Best practices for detected stack

**Covers:**
- Decision context
- Alternatives considered
- Consequences
- Implementation plan
- Validation criteria

**Example Output:** `docs/adr/001-use-postgresql.md`

---

### 5. _RELATIONSHIPS_MATRIX_TEMPLATE.md

**Purpose:** Comprehensive relationship mapping between all backend components

**Use When:** Claude Code needs to document:
- Entity relationships (ERD)
- Entity ↔ API mappings
- Entity ↔ Service mappings
- Service dependencies
- Module architecture

**Covers:**
- Entity-to-Entity relationships matrix
- Entity ↔ API endpoints matrix
- Entity ↔ Services matrix
- Services ↔ API endpoints matrix
- Module ↔ Components matrix
- Multiple Mermaid diagrams (ERD, flow diagrams, dependency graphs)
- Quick reference dependency tables

**Example Output:** `docs/backend/relationships_matrix.md`

**Key Feature:** Visual maps showing ALL connections between backend components for quick architecture understanding.

---

## 🎯 HOW TEMPLATES ARE USED

### During Bootstrap (PHASE 5.7):

```
PHASE 5.7: BACKEND DOCUMENTATION GENERATION

1. ANALYZE:
   - Raw data mentions backend?
   - Tech stack includes backend framework?
   - Project type suggests backend?

2. DECIDE:
   IF (raw_data_has_backend):
       Generate from raw data
   ELSE IF (tech_stack_suggests_backend):
       Intelligent inference
   ELSE:
       Skip backend docs

3. GENERATE:
   - Copy template
   - Fill placeholders with:
     * Raw data findings
     * Inferred structure
     * Best practices for stack
   - Save to project docs/

4. VALIDATE:
   - All placeholders filled?
   - Mermaid diagrams valid?
   - Cross-references correct?
```

---

## 📂 GENERATED STRUCTURE

When Claude Code generates backend documentation, it creates:

```
docs/
├── backend/
│   ├── 00_BACKEND_OVERVIEW.md           # Overview (generated)
│   ├── entities/
│   │   ├── 00_ENTITY_CATALOG.md         # Catalog with ERD (generated)
│   │   ├── user.md                      # From _ENTITY_TEMPLATE
│   │   ├── project.md                   # From _ENTITY_TEMPLATE
│   │   └── task.md                      # From _ENTITY_TEMPLATE
│   ├── api/
│   │   ├── 00_API_OVERVIEW.md           # Overview (generated)
│   │   ├── users-api.md                 # From _API_ENDPOINT_TEMPLATE
│   │   └── projects-api.md              # From _API_ENDPOINT_TEMPLATE
│   ├── services/
│   │   ├── 00_SERVICES_CATALOG.md       # Catalog (generated)
│   │   └── auth-service.md              # From _SERVICE_TEMPLATE
│   ├── database/
│       ├── 00_DATABASE_SCHEMA.md        # Complete schema (generated)
│       └── relationships.md             # ERD diagrams (generated)
│   └── relationships_matrix.md         # Comprehensive relationships map (from template)
│
└── adr/
    ├── 00_ADR_INDEX.md                  # Index (generated)
    ├── 001-use-postgresql.md            # From _ADR_TEMPLATE
    └── 002-modular-monolith.md          # From _ADR_TEMPLATE
```

---

## 🧠 INTELLIGENT INFERENCE

**When raw data lacks backend details, Claude Code infers based on:**

### Project Type Inference:

| Project Type | Likely Entities | Likely Services |
|--------------|-----------------|-----------------|
| Task Manager | User, Project, Task, Comment | Auth, Tasks, Notifications |
| E-commerce | User, Product, Order, Cart | Auth, Catalog, Orders, Payments |
| Social Network | User, Post, Comment, Like | Auth, Posts, Feed, Messaging |
| Blog Platform | User, Article, Comment, Tag | Auth, Content, Comments, Search |

### Tech Stack Inference:

| Tech Stack | Documentation Strategy |
|------------|----------------------|
| **PostgreSQL** → Relational entities, ERD diagrams, migrations | Full entity & DB docs |
| **MongoDB** → Document models, no ERD | Entity docs without strict schema |
| **Express** → RESTful API, middleware, routes | Standard REST API docs |
| **Fastify** → Plugin-based, validation schemas | Schema-driven API docs |
| **NestJS** → Module-based, decorators, DI | Service-oriented docs |

### Best Practices Integration:

Claude Code automatically includes modern best practices:
- JWT authentication (if auth mentioned)
- Rate limiting
- Soft deletes
- Audit trails
- API versioning
- Error handling patterns

---

## 📖 EXAMPLES

See `examples/` directory for condensed examples showing:
- **entity-example.md** - Simplified entity documentation
- **api-example.md** - Simplified API endpoint
- **service-example.md** - Simplified service
- **adr-example.md** - Simplified ADR

These examples show the minimal viable documentation (vs full templates).

---

## ✅ VALIDATION CHECKLIST

When Claude Code generates documentation, it validates:

- [ ] All placeholders `[PLACEHOLDER]` replaced
- [ ] Mermaid diagrams render correctly
- [ ] Cross-references point to existing files
- [ ] Examples are project-specific (not template examples)
- [ ] Tech stack matches project
- [ ] No contradictions with raw data

---

## 🔄 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 2.1 | 2025-11-11 | Created backend templates for hybrid approach |
| 2.0 | 2025-11-10 | UPMT v2.0 release |

---

## 📚 RELATED DOCUMENTATION

- [UPMT Master Reference](../AI_INSTRUCTIONS/UPMT.md)
- [Bootstrap Process](../../bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_START_PROMPT.md)
- [All Project Rules](../AI_INSTRUCTIONS/All_Project_rules.md)
- [Relationships Matrix Template](_RELATIONSHIPS_MATRIX_TEMPLATE.md) - Comprehensive relationship mapping

**Generated Files Reference:**
- `docs/backend/relationships_matrix.md` - Visual maps of all backend component relationships
- `docs/backend/entities/00_ENTITY_CATALOG.md` - Entity catalog with ERD
- `docs/backend/api/00_API_OVERVIEW.md` - API design overview
- `docs/backend/services/00_SERVICES_CATALOG.md` - Services catalog

---

**Note:** These templates are part of UPMT template system. They live in `UPMT/structure-templates/` and are copied to project `docs/` during bootstrap.

