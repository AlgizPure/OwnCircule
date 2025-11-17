# Cross-Promo Service

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** Active

---

## 🎯 PURPOSE

Manages cross-business promotion chains and Win-Win analytics to drive customer flow between partner businesses.

**Primary Responsibilities:**
- Evaluate chain triggers on transaction completion
- Generate coupons from triggered chains
- Calculate Win-Win index for business pairs
- Recommend optimal cross-promo partnerships

---

## ⚙️ KEY FUNCTIONS

### evaluate_chain_triggers()

**Purpose:** Check if transaction triggers any cross-promo chains

**Logic:**
```python
# Find active chains where transaction.business_id is source
chains = get_active_chains(source_business=transaction.business_id)

triggered_coupons = []
for chain in chains:
    if meets_trigger_conditions(transaction, chain):
        coupon = generate_coupon(
            user=transaction.user,
            business=chain.reward_business_id,
            chain=chain
        )
        triggered_coupons.append(coupon)
        
        # Send notification
        send_notification(transaction.user, coupon)

return triggered_coupons
```

### calculate_winwin_index()

**Purpose:** Calculate mutual benefit score (1-10) for business pair

**Formula:**
```python
# Conversion rates (both directions)
conversion_a_to_b = coupon_redemptions_b / coupons_issued_b
conversion_b_to_a = coupon_redemptions_a / coupons_issued_a

# Customer LTV increase
ltv_increase_a = avg_subsequent_purchases_from_b_customers
ltv_increase_b = avg_subsequent_purchases_from_a_customers

# Win-Win Index (1-10 scale)
winwin_index = (
    (conversion_a_to_b + conversion_b_to_a) / 2 * 5 +
    (ltv_increase_a + ltv_increase_b) / baseline_ltv * 5
)
```

---

## 📝 CHAIN TYPES

1. **Simple (A→B):** Purchase at A triggers coupon for B
2. **Sequential (A→B→C):** Must complete in order
3. **Cyclic (A⇄B):** Mutual benefit, refreshes monthly
4. **Fan (A→[B,C,D]):** User chooses reward destination

---

**Navigation:** [← Loyalty Service](./loyalty-service.md) | [Events Service →](./events-service.md)
