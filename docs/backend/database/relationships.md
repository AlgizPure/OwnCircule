# Database Relationships

**Version:** 1.0  
**Last Updated:** 2025-11-17

---

## 🔗 RELATIONSHIP MATRIX

| Parent Table | Child Table | Relationship | FK Column | On Delete | Cardinality |
|--------------|-------------|--------------|-----------|-----------|-------------|
| `users` | `transactions` | Has Many | `user_id` | RESTRICT | 1:N |
| `users` | `bonuses` | Has One | `user_id` | CASCADE | 1:1 |
| `users` | `coupons` | Has Many | `user_id` | CASCADE | 1:N |
| `users` | `events` | Has Many | `created_by_id` | RESTRICT | 1:N |
| `users` | `event_registrations` | Has Many | `user_id` | CASCADE | 1:N |
| `users` | `notifications` | Has Many | `user_id` | CASCADE | 1:N |
| `users` | `users` | Self-Ref | `referred_by_id` | SET NULL | 1:N |
| `businesses` | `transactions` | Has Many | `business_id` | RESTRICT | 1:N |
| `businesses` | `coupons` | Has Many | `business_id` | CASCADE | 1:N |
| `businesses` | `crm_integrations` | Has One | `business_id` | CASCADE | 1:1 |
| `events` | `event_registrations` | Has Many | `event_id` | CASCADE | 1:N |
| `cross_promo_chains` | `coupons` | Has Many | `source_id` | CASCADE | 1:N |

---

## 📝 CASCADE BEHAVIORS

### On User Delete (Soft Delete)
- `transactions` → **RESTRICT** (cannot delete user with transactions)
- `bonuses` → **CASCADE** (delete bonus record)
- `coupons` → **CASCADE** (invalidate user coupons)
- `event_registrations` → **CASCADE** (cancel registrations)
- `notifications` → **CASCADE** (clear notification queue)

### On Business Delete
- `transactions` → **RESTRICT** (cannot delete business with transactions)
- `coupons` → **CASCADE** (invalidate business coupons)
- `crm_integrations` → **CASCADE** (remove CRM config)

### On Event Delete
- `event_registrations` → **CASCADE** (cancel all registrations)

---

## 🧪 REFERENTIAL INTEGRITY TESTS

```sql
-- Test 1: Cannot delete user with transactions
DELETE FROM users WHERE id = 'uuid';
-- Expected: ERROR - violates foreign key constraint

-- Test 2: Deleting user cascades to bonuses
DELETE FROM bonuses WHERE user_id = 'uuid';
SELECT COUNT(*) FROM bonuses WHERE user_id = 'uuid';
-- Expected: 0

-- Test 3: Self-referential integrity
SELECT referred_by_id FROM users WHERE id = 'uuid';
-- Should be NULL if referrer deleted
```

---

**Navigation:** [← Database Schema](./00_DATABASE_SCHEMA.md) | [Migrations →](./migrations.md)
