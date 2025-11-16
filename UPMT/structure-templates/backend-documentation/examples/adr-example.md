# ADR-001: Use PostgreSQL (Minimal Example)

**Date:** 2025-11-10  
**Status:** Accepted

---

## Context

Need to choose primary database for project with relational data (users, projects, tasks).

---

## Decision

We will use **PostgreSQL 16** as the primary database.

---

## Alternatives Considered

**MySQL** - Good, but PostgreSQL has better JSON support  
**MongoDB** - Not suitable for relational data  
**SQLite** - Not suitable for multi-user production

---

## Consequences

**Pros:**
- ACID compliance
- Strong relational support
- JSON columns for flexibility

**Cons:**
- Slightly more complex than MySQL
- Hosting cost higher than SQLite

---

**See:** [Full Template](_ADR_TEMPLATE.md) for complete ADR structure

