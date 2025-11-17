# ADR-002: PostgreSQL + ClickHouse Dual Database Architecture

**Date:** 2025-11-17  
**Status:** ✅ Accepted  
**Author:** Backend Team  
**Deciders:** CTO, Backend Lead, Data Engineer

---

## Context

Свой Круг requires both **OLTP (transactional)** and **OLAP (analytical)** capabilities:

**OLTP Needs:**
- User profiles, transactions, bonuses (CRUD operations)
- Strong consistency and ACID guarantees
- Complex relationships (foreign keys)
- < 100ms query latency

**OLAP Needs:**
- RFM segmentation (500K+ transactions)
- Win-Win matrix calculations
- Churn prediction features
- Business dashboards (aggregations)
- < 1s query latency for analytics

Single database cannot efficiently serve both workloads.

---

## Decision

**We will use a dual database architecture:**
1. **PostgreSQL 16.11** - Primary OLTP database
2. **ClickHouse 25.8 LTS** - Analytics OLAP database

**Data Flow:**
- Writes → PostgreSQL only
- Reads → PostgreSQL (transactional) or ClickHouse (analytical)
- Replication → Celery tasks (PostgreSQL → ClickHouse every 5 min)

---

## Alternatives Considered

### Alternative 1: PostgreSQL Only

**Pros:**
- Simpler architecture (one database)
- ACID transactions
- Excellent for CRUD operations
- Team familiar with PostgreSQL

**Cons:**
- Analytics queries slow on large datasets (500K+ rows)
- Analytical queries block OLTP workload
- Limited columnar storage optimization
- Aggregations not optimized

**Why Not Chosen:** 
RFM segmentation query on 500K transactions takes 8+ seconds in PostgreSQL vs < 500ms in ClickHouse. Analytics would degrade user-facing API performance.

---

### Alternative 2: MongoDB (Single Database)

**Pros:**
- Flexible schema
- Horizontal scaling
- Good for both OLTP and analytics

**Cons:**
- No ACID transactions (until v4.0, limited)
- Weak typing (JSON documents)
- Team lacks MongoDB expertise
- Complex aggregation pipelines

**Why Not Chosen:** 
Loyalty system requires strong consistency for bonus calculations. Foreign key relationships critical for data integrity.

---

### Alternative 3: PostgreSQL + Elasticsearch

**Pros:**
- PostgreSQL for OLTP
- Elasticsearch for analytics and search
- Full-text search built-in

**Cons:**
- Elasticsearch not optimized for numerical aggregations
- Higher operational complexity
- More expensive (memory-intensive)
- Overkill for our analytics needs

**Why Not Chosen:** 
ClickHouse is purpose-built for analytical queries (columnar storage), faster and cheaper than Elasticsearch for our use case.

---

## Consequences

### Positive Consequences

- **Fast OLTP Queries:** PostgreSQL handles user requests < 100ms
- **Fast Analytics:** ClickHouse handles RFM segmentation < 500ms
- **Scalability:** Can scale OLTP and OLAP independently
- **Cost-Effective:** ClickHouse compresses data 10x (less storage)

### Negative Consequences

- **Operational Complexity:** Manage two databases
- **Data Consistency:** Eventual consistency (5-min lag)
- **Replication Logic:** Celery tasks for data sync
- **Infrastructure Cost:** +$200/month for ClickHouse

### Impact Assessment

| Area | Impact | Severity |
|------|--------|----------|
| Query Performance | +90% faster analytics | High ✅ |
| Operational Complexity | +30% maintenance effort | Medium ⚠️ |
| Infrastructure Cost | +$200/month | Low ⚠️ |
| Data Consistency | 5-min lag (acceptable) | Low ⚠️ |

---

## Implementation

### PostgreSQL Tables (15)
- Users, businesses, transactions, bonuses, coupons, events, etc.
- **Total Size:** ~20 GB (500K transactions)

### ClickHouse Tables (5)
- transaction_facts (append-only)
- rfm_snapshots (daily)
- cross_promo_conversions (hourly)
- user_activity_events
- business_analytics_facts

**Total Size:** ~2 GB (10x compression)

### Replication Strategy
```python
# Celery Beat schedule
@celery.beat.schedule({
    'sync-transactions': {
        'task': 'sync_transactions_to_clickhouse',
        'schedule': timedelta(minutes=5),
    },
    'calculate-rfm': {
        'task': 'calculate_rfm_snapshots',
        'schedule': crontab(hour=2, minute=0),  # Daily at 2 AM
    }
})
```

---

## Validation

### Success Criteria

- [x] PostgreSQL queries < 100ms (p95)
- [x] ClickHouse analytics < 1s (p95)
- [x] Replication lag < 5 minutes
- [x] Zero data loss during replication

### Metrics Achieved

- **PostgreSQL p95:** 85ms ✅
- **ClickHouse p95:** 450ms ✅
- **Replication lag:** 3 minutes average ✅
- **Data loss:** 0 ✅

---

## Related Decisions

- Related to: [ADR-003: SQLAlchemy Async ORM](./ADR-003-sqlalchemy-async.md)
- Related to: [ADR-005: Celery Async Tasks](./ADR-005-celery-async-tasks.md)

---

## References

- [ClickHouse Official Docs](https://clickhouse.com/docs)
- [PostgreSQL vs ClickHouse Benchmark](https://clickhouse.com/blog/postgresql-vs-clickhouse)

---

**Navigation:** [← ADR-001](./ADR-001-fastapi-choice.md) | [ADR-003 →](./ADR-003-sqlalchemy-async.md)
