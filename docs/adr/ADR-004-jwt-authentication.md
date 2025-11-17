# ADR-004: JWT RS256 Authentication

**Date:** 2025-11-17  
**Status:** ✅ Accepted  
**Author:** Backend Team

---

## Context

Mobile app requires stateless authentication. Options:
- Session-based auth (server-side sessions)
- JWT tokens (stateless)
- OAuth2 with external provider

Requirements:
- Stateless (no session storage)
- Secure (industry standard)
- Mobile-friendly (offline validation)

---

## Decision

**We will use JWT tokens with RS256 (RSA asymmetric signing).**

**Token Structure:**
- Access token: 15-minute TTL
- Refresh token: 30-day TTL
- RS256 signature (public/private key pair)

---

## Alternatives Considered

### Alternative 1: Session-Based Auth

**Why Not Chosen:** Requires server-side session storage (Redis), not stateless

### Alternative 2: JWT HS256 (Symmetric)

**Why Not Chosen:** Single secret key = higher security risk if leaked. RS256 allows public key distribution for token validation.

---

## Consequences

**Positive:**
- Stateless (no session storage)
- Scalable (no shared state)
- Secure (industry standard)

**Negative:**
- Cannot revoke tokens instantly (need blacklist)
- Larger token size than sessions

---

**Navigation:** [← ADR-003](./ADR-003-sqlalchemy-async.md) | [ADR-005 →](./ADR-005-celery-async-tasks.md)
