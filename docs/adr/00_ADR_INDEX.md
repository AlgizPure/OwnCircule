# Architecture Decision Records (ADR) Index

**Project:** Свой Круг (Own Circle)  
**Last Updated:** 2025-11-17

---

## 📋 WHAT ARE ADRs?

Architecture Decision Records document important architectural decisions made during the project lifecycle. Each ADR captures:
- Context and problem statement
- Decision made
- Alternatives considered
- Consequences and trade-offs

---

## 📚 ACTIVE ADRs

| ADR | Title | Date | Status |
|-----|-------|------|--------|
| [ADR-001](./ADR-001-fastapi-choice.md) | FastAPI vs Django for Backend Framework | 2025-11-17 | ✅ Accepted |
| [ADR-002](./ADR-002-database-architecture.md) | PostgreSQL + ClickHouse Dual Database | 2025-11-17 | ✅ Accepted |
| [ADR-003](./ADR-003-sqlalchemy-async.md) | SQLAlchemy 2.0 Async ORM | 2025-11-17 | ✅ Accepted |
| [ADR-004](./ADR-004-jwt-authentication.md) | JWT RS256 Authentication | 2025-11-17 | ✅ Accepted |
| [ADR-005](./ADR-005-celery-async-tasks.md) | Celery for Async Task Queue | 2025-11-17 | ✅ Accepted |

---

## 🗂️ ADR CATEGORIES

### Backend Framework
- ADR-001: FastAPI vs Django

### Data Storage
- ADR-002: PostgreSQL + ClickHouse dual database architecture

### ORM & Data Access
- ADR-003: SQLAlchemy 2.0 async ORM

### Authentication
- ADR-004: JWT RS256 authentication

### Async Processing
- ADR-005: Celery + Redis for background tasks

---

## 📝 ADR LIFECYCLE

**Statuses:**
- **Proposed:** Under discussion
- **Accepted:** Approved and implemented
- **Superseded:** Replaced by newer ADR
- **Deprecated:** No longer recommended
- **Rejected:** Not approved

---

## 🔗 RELATED DOCUMENTATION

- [Backend Overview](../backend/00_BACKEND_OVERVIEW.md)
- [Architecture Overview](../core/04_ARCHITECTURE.md)
- [Tech Stack](../core/03_TECH_STACK.md)

---

**Last Updated:** 2025-11-17  
**Maintained By:** Backend Engineering Team
