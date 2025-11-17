# Status Tier Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Loyalty System

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | StatusTier |
| **Database Table** | `status_tiers` |
| **Module:** | Loyalty |
| **Type** | Reference Data |
| **Primary Key** | `name` (enum) |

### Description

StatusTier entity defines loyalty tier configurations (Insider, VIP, Elite, Inner Circle). Static reference data with business rules for tier calculation.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE status_tiers (
  name                  VARCHAR(20) PRIMARY KEY
                        CHECK (name IN ('Insider', 'VIP', 'Elite', 'Inner Circle')),
  
  -- Thresholds
  min_spent             DECIMAL(12,2) NOT NULL,
  min_categories        INT NOT NULL,
  
  -- Benefits
  cashback_percent      DECIMAL(5,2) NOT NULL,
  influence_weight      DECIMAL(3,1) NOT NULL,
  can_propose_events    BOOLEAN DEFAULT false,
  can_vote              BOOLEAN DEFAULT true,
  exclusive_events      BOOLEAN DEFAULT false,
  
  -- Display
  display_name_ru       VARCHAR(100) NOT NULL,
  description           TEXT,
  badge_icon_url        VARCHAR(500),
  color_hex             VARCHAR(7),
  
  -- Order
  tier_order            INT UNIQUE NOT NULL
);

-- Seed data
INSERT INTO status_tiers VALUES
('Insider', 0, 0, 5.00, 1.0, false, true, false, 
 'Инсайдер', 'Базовый статус', '/badges/insider.svg', '#A0A0A0', 1),
('VIP', 30000, 3, 7.00, 2.0, true, true, false,
 'VIP', 'Привилегированный статус', '/badges/vip.svg', '#FFD700', 2),
('Elite', 100000, 5, 10.00, 3.0, true, true, true,
 'Элита', 'Элитный статус', '/badges/elite.svg', '#C0C0C0', 3),
('Inner Circle', 200000, 7, 12.00, 5.0, true, true, true,
 'Внутренний круг', 'Высший статус', '/badges/inner.svg', '#FFD700', 4);
```

---

### TypeScript Type

```typescript
interface StatusTier {
  name: 'Insider' | 'VIP' | 'Elite' | 'Inner Circle';
  
  minSpent: number;
  minCategories: number;
  
  cashbackPercent: number;
  influenceWeight: number;
  canProposeEvents: boolean;
  canVote: boolean;
  exclusiveEvents: boolean;
  
  displayNameRu: string;
  description?: string;
  badgeIconUrl?: string;
  colorHex?: string;
  
  tierOrder: number;
}
```

---

## 📝 BUSINESS RULES

1. **Automatic Calculation** - User status recalculated after each transaction
2. **Rolling 12-Month Window** - Spend and categories from last 12 months
3. **Manual Override** - Admin can manually set Inner Circle status

---

**Navigation:** [← Notification Entity](./notification.md) | [CRM Integration Entity →](./crm-integration.md)
