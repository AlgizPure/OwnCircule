# Database Migrations

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Tool:** Alembic 1.14+

---

## 🔄 MIGRATION WORKFLOW

### Alembic Setup

**Directory Structure:**
```
alembic/
├── versions/
│   ├── 001_initial_schema.py
│   ├── 002_add_referral_codes.py
│   └── 003_add_cross_promo_chains.py
├── env.py
└── script.py.mako
```

---

## 📝 CREATING MIGRATIONS

### Auto-Generate Migration

```bash
# Generate migration from model changes
alembic revision --autogenerate -m "Add new table: notifications"

# Review generated migration
# Edit: alembic/versions/004_add_notifications.py
```

### Manual Migration Template

```python
"""Add notifications table

Revision ID: 004_add_notifications
Revises: 003_add_cross_promo_chains
Create Date: 2025-11-17 10:30:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

revision = '004_add_notifications'
down_revision = '003_add_cross_promo_chains'

def upgrade():
    op.create_table(
        'notifications',
        sa.Column('id', UUID, primary_key=True),
        sa.Column('user_id', UUID, sa.ForeignKey('users.id')),
        sa.Column('channel', sa.String(20), nullable=False),
        sa.Column('body', sa.Text, nullable=False),
        sa.Column('status', sa.String(20), default='pending'),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now())
    )
    
    op.create_index('idx_notifications_user', 'notifications', ['user_id'])

def downgrade():
    op.drop_table('notifications')
```

---

## 🚀 RUNNING MIGRATIONS

### Development
```bash
# Apply all pending migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Show current revision
alembic current
```

### Production
```bash
# Dry run (show SQL without executing)
alembic upgrade head --sql > migration.sql
# Review migration.sql, then apply manually

# Or run with backup
pg_dump -Fc svoy_krug > backup.dump
alembic upgrade head
```

---

## 📋 MIGRATION CHECKLIST

Before deploying migration:

- [ ] Test on local database
- [ ] Test on staging database
- [ ] Review generated SQL
- [ ] Check for breaking changes
- [ ] Verify indexes are created
- [ ] Test rollback (downgrade)
- [ ] Create database backup
- [ ] Update entity documentation
- [ ] Notify team of schema changes

---

## 🔙 ROLLBACK STRATEGY

### Safe Rollback (< 24 hours)
```bash
alembic downgrade -1
```

### Emergency Restore
```bash
pg_restore -d svoy_krug backup.dump
```

---

**Navigation:** [← Relationships](./relationships.md) | [ADR Index →](../../adr/00_ADR_INDEX.md)
