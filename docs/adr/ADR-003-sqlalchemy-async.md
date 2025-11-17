# ADR-003: SQLAlchemy 2.0 Async ORM

**Date:** 2025-11-17  
**Status:** ✅ Accepted  
**Author:** Backend Team

---

## Context

FastAPI supports async/await for high-concurrency workloads. We need an ORM that:
- Supports async database operations
- Integrates with FastAPI
- Provides type safety
- Handles complex relationships

---

## Decision

**We will use SQLAlchemy 2.0.44 with asyncpg driver.**

Key features:
- Native async/await support
- Type-safe queries
- Relationship management
- Alembic migrations

---

## Alternatives Considered

### Alternative 1: Django ORM

**Why Not Chosen:** Synchronous by default, tight Django coupling

### Alternative 2: Tortoise ORM

**Why Not Chosen:** Smaller ecosystem, less mature than SQLAlchemy

---

## Consequences

**Positive:**
- Async queries don't block event loop
- Type-safe models with mypy
- Mature ecosystem (20+ years)

**Negative:**
- Learning curve for async patterns
- More verbose than Django ORM

---

**Navigation:** [← ADR-002](./ADR-002-database-architecture.md) | [ADR-004 →](./ADR-004-jwt-authentication.md)
