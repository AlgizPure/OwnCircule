# Coupon Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Loyalty & Cross-Promo

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | Coupon |
| **Database Table** | `coupons` |
| **Module:** | Loyalty, Cross-Promo |
| **Type** | Core |
| **Primary Key** | `id` (uuid) |

### Description

Coupon entity represents a discount or bonus voucher issued to a user. Can be generated from offers, cross-promo chains, or admin grants. Single-use with expiration.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE coupons (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Ownership
  user_id               UUID NOT NULL REFERENCES users(id),
  business_id           UUID NOT NULL REFERENCES businesses(id),
  
  -- Coupon Type
  discount_type         VARCHAR(20) NOT NULL
                        CHECK (discount_type IN ('percent', 'fixed', 'bonus_multiplier', 'gift')),
  discount_value        DECIMAL(10,2) NOT NULL,
  
  -- Conditions
  min_purchase_amount   DECIMAL(10,2) DEFAULT 0.00,
  max_discount_amount   DECIMAL(10,2),  -- Cap for percent discounts
  
  -- Origin
  source_type           VARCHAR(50),  -- 'offer' | 'cross_promo_chain' | 'referral' | 'birthday' | 'admin'
  source_id             UUID,  -- Reference to source entity
  
  -- Status
  is_activated          BOOLEAN DEFAULT false,
  activated_at          TIMESTAMP WITH TIME ZONE,
  redeemed_at           TIMESTAMP WITH TIME ZONE,
  expires_at            TIMESTAMP WITH TIME ZONE NOT NULL,
  
  -- Usage
  activation_code       VARCHAR(10),  -- For POS usage
  transaction_id        UUID REFERENCES transactions(id),  -- Transaction where used
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_coupons_user ON coupons(user_id, expires_at DESC);
CREATE INDEX idx_coupons_business ON coupons(business_id);
CREATE INDEX idx_coupons_expires ON coupons(expires_at) WHERE redeemed_at IS NULL;
CREATE INDEX idx_coupons_activation_code ON coupons(activation_code) WHERE activation_code IS NOT NULL;
```

---

### TypeScript Type

```typescript
interface Coupon {
  id: string;
  userId: string;
  businessId: string;
  
  discountType: 'percent' | 'fixed' | 'bonus_multiplier' | 'gift';
  discountValue: number;
  
  minPurchaseAmount: number;
  maxDiscountAmount?: number;
  
  sourceType: string;
  sourceId?: string;
  
  isActivated: boolean;
  activatedAt?: Date;
  redeemedAt?: Date;
  expiresAt: Date;
  
  activationCode?: string;
  transactionId?: string;
  
  createdAt: Date;
}
```

---

## 🌐 API ENDPOINTS

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/v1/coupons` | List user coupons | Member |
| POST | `/api/v1/coupons/:id/activate` | Activate coupon | Member |
| POST | `/api/v1/coupons/:id/redeem` | Redeem coupon | Business |

**Detailed Documentation:** [Coupons API](../api/coupons-api.md)

---

## 📝 BUSINESS RULES

1. **Single-Use** - Each coupon can only be redeemed once
2. **Activation Window** - 30 minutes after activation before expiry
3. **Expiration Notification** - Push notification 24h before expiry
4. **Auto-Apply** - Auto-applied if conditions met at checkout

---

**Navigation:** [← Bonus Entity](./bonus.md) | [Event Entity →](./event.md)
