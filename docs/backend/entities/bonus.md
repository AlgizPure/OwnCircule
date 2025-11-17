# Bonus Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Loyalty System

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | Bonus |
| **Database Table** | `bonuses` |
| **Module** | Loyalty |
| **Type** | Core |
| **Primary Key** | `id` (uuid) |

### Description

Bonus entity represents a user's loyalty points balance. One-to-one relationship with User. Tracks earned, spent, and available points with expiration logic.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE bonuses (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL UNIQUE REFERENCES users(id),
  
  -- Balances
  balance               DECIMAL(10,2) DEFAULT 0.00 CHECK (balance >= 0),
  pending_balance       DECIMAL(10,2) DEFAULT 0.00,  -- Not yet available
  lifetime_earned       DECIMAL(12,2) DEFAULT 0.00,
  lifetime_spent        DECIMAL(12,2) DEFAULT 0.00,
  lifetime_expired      DECIMAL(12,2) DEFAULT 0.00,
  
  -- Expiration
  expires_at            TIMESTAMP WITH TIME ZONE,  -- Oldest bonus expiry
  
  -- Metadata
  last_accrual_at       TIMESTAMP WITH TIME ZONE,
  last_redemption_at    TIMESTAMP WITH TIME ZONE,
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_bonuses_user ON bonuses(user_id);
CREATE INDEX idx_bonuses_expires ON bonuses(expires_at) WHERE expires_at IS NOT NULL;
```

---

### TypeScript Type

```typescript
interface Bonus {
  id: string;
  userId: string;
  
  balance: number;
  pendingBalance: number;
  lifetimeEarned: number;
  lifetimeSpent: number;
  lifetimeExpired: number;
  
  expiresAt?: Date;
  lastAccrualAt?: Date;
  lastRedemptionAt?: Date;
  
  createdAt: Date;
  updatedAt: Date;
}
```

---

## 🌐 API ENDPOINTS

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/v1/loyalty/balance` | Get bonus balance | Member |
| GET | `/api/v1/loyalty/history` | Bonus transaction history | Member |

**Detailed Documentation:** [Loyalty API](../api/loyalty-api.md)

---

## 📝 BUSINESS RULES

1. **Expiration Policy** - Bonuses expire after 90 days
2. **Warning Notification** - Alert 7 days before expiry
3. **FIFO Redemption** - Oldest bonuses used first
4. **Minimum Redemption** - 100₽ minimum to redeem

---

**Navigation:** [← Transaction Entity](./transaction.md) | [Coupon Entity →](./coupon.md)
