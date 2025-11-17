# Loyalty Service

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** Active

---

## 🎯 PURPOSE

Manages loyalty program logic including bonus calculations, status tier updates, cashback rates, and expiration handling.

**Primary Responsibilities:**
- Calculate bonus accrual on transactions
- Update user status tiers (Insider/VIP/Elite/Inner Circle)
- Handle bonus redemption and expiration
- Apply category multipliers and special rates

---

## ⚙️ KEY FUNCTIONS

### calculate_bonus()

**Purpose:** Calculate bonus points for a transaction

**Logic:**
```python
bonus = transaction.amount * cashback_rate * multiplier

# Cashback rates by status tier
cashback_rate = {
    'Insider': 0.05,   # 5%
    'VIP': 0.07,       # 7%
    'Elite': 0.10,     # 10%
    'Inner Circle': 0.12  # 12%
}

# Apply category multiplier (first purchase in category)
if is_first_in_category:
    multiplier = 1.5
else:
    multiplier = business.bonus_multiplier  # Default 1.0
```

### update_status_tier()

**Purpose:** Recalculate user status based on 12-month rolling window

**Thresholds:**
- **VIP:** ≥30,000₽ spent + ≥3 categories
- **Elite:** ≥100,000₽ spent + ≥5 categories OR Top 1%
- **Inner Circle:** ≥200,000₽ spent OR manual promotion

---

## 📝 BUSINESS RULES

1. **Bonus Expiration:** 90 days from accrual
2. **FIFO Redemption:** Oldest bonuses used first
3. **Minimum Redemption:** 100₽ minimum
4. **Warning Notification:** 7 days before expiry

---

**Navigation:** [← Auth Service](./auth-service.md) | [Cross-Promo Service →](./cross-promo-service.md)
