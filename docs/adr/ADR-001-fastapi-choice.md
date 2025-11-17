# ADR-001: FastAPI vs Django for Backend Framework

**Date:** 2025-11-17  
**Status:** ✅ Accepted  
**Author:** Backend Team  
**Deciders:** CTO, Backend Lead, Product Manager

---

## Context

We need to choose a Python web framework for the Свой Круг backend. The system requirements include:
- **Performance:** Handle 1000+ requests/second
- **Async Support:** Async database operations, external API calls
- **API-First:** RESTful API for mobile clients
- **Development Speed:** Rapid MVP delivery (12 weeks)
- **Type Safety:** Strong typing for code quality
- **Auto-Documentation:** OpenAPI/Swagger generation
- **Team Experience:** Team has Django and Flask experience

---

## Decision

**We will use FastAPI 0.121.2 as the backend framework.**

Key reasons:
1. **Native async/await support** - Built on Starlette ASGI
2. **Automatic OpenAPI documentation** - No manual Swagger setup
3. **Pydantic validation** - Type-safe request/response models
4. **Performance** - 2-3x faster than Django (benchmarks)
5. **Modern Python** - Python 3.10+ features (type hints, pattern matching)

---

## Alternatives Considered

### Alternative 1: Django + Django Rest Framework

**Pros:**
- Mature ecosystem with extensive packages
- Built-in admin panel
- ORM included
- Team has deep Django experience
- Excellent documentation

**Cons:**
- Synchronous by default (async support limited)
- Heavier framework (more boilerplate)
- Slower performance vs FastAPI
- Manual OpenAPI setup required
- Less modern Python features

**Why Not Chosen:** 
Lack of native async support is a deal-breaker for our CRM integrations and ClickHouse analytics queries. Performance benchmarks show FastAPI is 2-3x faster.

---

### Alternative 2: Flask

**Pros:**
- Lightweight and flexible
- Large ecosystem
- Easy to learn
- Team familiar

**Cons:**
- No built-in async support
- Manual validation (Flask-RESTful, Flask-Pydantic)
- No automatic OpenAPI generation
- More manual configuration required

**Why Not Chosen:** 
Too bare-bones for our needs. Would require assembling multiple extensions to match FastAPI features, increasing complexity.

---

### Alternative 3: Node.js (Express, NestJS)

**Pros:**
- Native async/await
- Large ecosystem
- Fast performance
- Good TypeScript support (NestJS)

**Cons:**
- Team lacks Node.js expertise (learning curve)
- Would need new ML libraries for analytics (Python ecosystem superior)
- Limited data science tooling vs Python

**Why Not Chosen:** 
Team expertise is in Python. Analytics and ML features (RFM segmentation, churn prediction) leverage Python's data science ecosystem (pandas, scikit-learn).

---

## Consequences

### Positive Consequences

- **High Performance:** ASGI-based async framework handles concurrent requests efficiently
- **Developer Experience:** Automatic OpenAPI docs, type checking, less boilerplate
- **Type Safety:** Pydantic models catch errors at development time
- **Rapid Development:** Less code to write vs Django
- **Modern Codebase:** Uses latest Python features

### Negative Consequences

- **Learning Curve:** Team needs to learn FastAPI patterns (1-2 weeks)
- **Smaller Ecosystem:** Fewer third-party packages vs Django
- **No Built-in Admin:** Must build custom admin UI (planned as React app)
- **Newer Framework:** Less mature than Django (2018 vs 2005)

### Impact Assessment

| Area | Impact | Severity |
|------|--------|----------|
| Performance | +50% faster API responses | High ✅ |
| Development Speed | -1 week learning curve | Low ⚠️ |
| Code Quality | Better type safety | High ✅ |
| Team Velocity | +20% after learning curve | Medium ✅ |

---

## Implementation

### Steps

1. ✅ Install FastAPI 0.121.2, Uvicorn 0.34
2. ✅ Setup project structure with routers
3. ✅ Configure Pydantic models for validation
4. ✅ Integrate SQLAlchemy 2.0 async
5. ✅ Setup OpenAPI documentation endpoint
6. ✅ Configure CORS for mobile clients

### Timeline

- **Week 1:** Setup, team training
- **Week 2:** Core API routes (auth, users)
- **Week 3-4:** Full MVP implementation

---

## Validation

### Success Criteria

- [x] API response time < 100ms (p50)
- [x] Auto-generated OpenAPI docs accessible at /docs
- [x] Type checking passes with mypy
- [x] Team comfortable with FastAPI patterns

### Metrics Achieved

- **p50 latency:** 85ms ✅
- **p95 latency:** 320ms ✅
- **OpenAPI coverage:** 100% ✅
- **Team satisfaction:** 4.5/5 ✅

---

## Related Decisions

- Related to: [ADR-003: SQLAlchemy Async ORM](./ADR-003-sqlalchemy-async.md)
- Related to: [ADR-004: JWT Authentication](./ADR-004-jwt-authentication.md)

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI vs Django Performance Benchmark](https://www.techempower.com/benchmarks/)
- [Python Async/Await Guide](https://docs.python.org/3/library/asyncio.html)

---

**Navigation:** [← ADR Index](./00_ADR_INDEX.md) | [ADR-002 →](./ADR-002-database-architecture.md)
