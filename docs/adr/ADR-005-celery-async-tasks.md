# ADR-005: Celery for Async Task Queue

**Date:** 2025-11-17  
**Status:** ✅ Accepted  
**Author:** Backend Team

---

## Context

Background tasks needed:
- CRM transaction sync (every 5 min)
- Bonus expiration checks (daily)
- RFM segmentation (daily)
- Email/SMS notifications
- Analytics aggregations

Requirements:
- Reliable task execution
- Scheduled tasks (cron-like)
- Retry logic
- Task monitoring

---

## Decision

**We will use Celery 5.4+ with Redis broker.**

Components:
- **Celery Worker:** Execute async tasks
- **Celery Beat:** Schedule periodic tasks
- **Redis:** Message broker + result backend

---

## Alternatives Considered

### Alternative 1: FastAPI Background Tasks

**Why Not Chosen:** 
- No persistence (lost on restart)
- No scheduling
- No retry logic
- Not suitable for long-running tasks

### Alternative 2: RQ (Redis Queue)

**Why Not Chosen:**
- Less mature than Celery
- Limited scheduling features
- Smaller ecosystem

### Alternative 3: Cloud Functions (Serverless)

**Why Not Chosen:**
- Cold start latency
- More expensive for frequent tasks
- Harder to debug locally

---

## Consequences

**Positive:**
- Reliable task execution with retries
- Flexible scheduling (Celery Beat)
- Rich monitoring (Flower UI)
- Proven at scale

**Negative:**
- Additional infrastructure (Celery workers)
- More complex deployment
- Resource overhead

---

## Implementation

```python
# celery_app.py
app = Celery('svoy_krug', broker='redis://localhost:6379/0')

@app.task(bind=True, max_retries=3)
def sync_crm_transactions(self, business_id):
    try:
        # Sync logic
        pass
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

# Scheduled tasks
app.conf.beat_schedule = {
    'sync-transactions-every-5-min': {
        'task': 'sync_crm_transactions',
        'schedule': timedelta(minutes=5),
    },
}
```

---

**Navigation:** [← ADR-004](./ADR-004-jwt-authentication.md) | [Backend Overview →](../backend/00_BACKEND_OVERVIEW.md)
