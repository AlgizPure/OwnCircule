# Cross Promo Chain Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Cross-Promotion Engine

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | CrossPromoChain |
| **Database Table** | `cross_promo_chains` |
| **Module:** | Cross-Promo |
| **Type** | Core |
| **Primary Key** | `id` (uuid) |

### Description

CrossPromoChain entity represents a business-to-business promotion chain (A→B, A→B→C, A⇄B, A→[B,C,D]). Triggers coupon generation when user completes purchases in sequence.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE cross_promo_chains (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Chain Configuration
  name                  VARCHAR(255) NOT NULL,
  chain_type            VARCHAR(20) NOT NULL
                        CHECK (chain_type IN ('simple', 'sequential', 'cyclic', 'fan')),
  chain_steps           JSONB NOT NULL,  -- [{"business_id": "...", "min_amount": 1000}]
  
  -- Trigger Conditions
  min_purchase_amount   DECIMAL(10,2) DEFAULT 0.00,
  user_status_required  VARCHAR(20),  -- NULL = all users
  
  -- Reward Configuration
  reward_type           VARCHAR(20) CHECK (reward_type IN ('coupon', 'bonus', 'discount')),
  reward_value          DECIMAL(10,2),
  reward_business_id    UUID REFERENCES businesses(id),
  coupon_expiry_days    INT DEFAULT 30,
  
  -- Financing
  financed_by           VARCHAR(20) CHECK (financed_by IN ('source', 'target', 'platform', 'split')),
  
  -- Status & Analytics
  is_active             BOOLEAN DEFAULT true,
  approval_status       VARCHAR(20) DEFAULT 'pending'
                        CHECK (approval_status IN ('pending', 'approved', 'rejected')),
  triggers_count        INT DEFAULT 0,
  conversions_count     INT DEFAULT 0,
  conversion_rate       DECIMAL(5,2) DEFAULT 0.00,
  winwin_index          DECIMAL(3,1),  -- 1.0 to 10.0
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  approved_at           TIMESTAMP WITH TIME ZONE,
  deactivated_at        TIMESTAMP WITH TIME ZONE
);

-- Indexes
CREATE INDEX idx_cross_promo_chains_active ON cross_promo_chains(is_active) WHERE is_active = true;
CREATE INDEX idx_cross_promo_chains_type ON cross_promo_chains(chain_type);
```

---

### TypeScript Type

```typescript
interface CrossPromoChain {
  id: string;
  name: string;
  chainType: 'simple' | 'sequential' | 'cyclic' | 'fan';
  chainSteps: Array<{
    businessId: string;
    minAmount: number;
  }>;
  
  minPurchaseAmount: number;
  userStatusRequired?: string;
  
  rewardType: 'coupon' | 'bonus' | 'discount';
  rewardValue: number;
  rewardBusinessId: string;
  couponExpiryDays: number;
  
  financedBy: 'source' | 'target' | 'platform' | 'split';
  
  isActive: boolean;
  approvalStatus: 'pending' | 'approved' | 'rejected';
  triggersCount: number;
  conversionsCount: number;
  conversionRate: number;
  winwinIndex?: number;
  
  createdAt: Date;
}
```

---

## 📝 BUSINESS RULES

1. **Simple Chain (A→B):** Purchase at A triggers coupon for B
2. **Sequential (A→B→C):** Must complete in order
3. **Cyclic (A⇄B):** Mutual benefit, refreshes monthly
4. **Fan (A→[B,C,D]):** User chooses coupon destination

---

**Navigation:** [← Event Registration Entity](./event-registration.md) | [Notification Entity →](./notification.md)
