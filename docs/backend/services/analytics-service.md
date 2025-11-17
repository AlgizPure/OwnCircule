# Analytics Service

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** Active

---

## 🎯 PURPOSE

Provides business intelligence through RFM segmentation, churn prediction, and dashboard generation using ClickHouse analytics database.

**Primary Responsibilities:**
- Daily RFM segmentation for all users
- Churn risk prediction using ML models
- Business dashboard data aggregation
- Transaction data replication to ClickHouse

---

## ⚙️ KEY FUNCTIONS

### calculate_rfm_segments()

**Purpose:** Calculate RFM scores for user segmentation

**Logic:**
```python
# Calculate RFM metrics (last 12 months)
recency = (datetime.now() - last_transaction_date).days
frequency = count_transactions(user_id, last_12_months)
monetary = sum_transaction_amounts(user_id, last_12_months)

# Score each dimension (1-5 scale)
r_score = score_recency(recency)      # 1=long ago, 5=recent
f_score = score_frequency(frequency)   # 1=rare, 5=frequent
m_score = score_monetary(monetary)     # 1=low spend, 5=high spend

# Segment mapping
rfm_segment = f"{r_score}{f_score}{m_score}"

segments = {
    '555': 'Champions',
    '554': 'Loyal Customers',
    '155': 'At Risk',
    '111': 'Lost'
}

return segments.get(rfm_segment, 'Other')
```

### predict_churn_risk()

**Purpose:** Predict probability of customer churn

**Features:**
- Days since last purchase
- Transaction frequency trend
- Average purchase amount trend
- Engagement with promotions
- Event attendance rate

**Model:** XGBoost classifier (trained monthly)

**Output:** Churn probability 0.0-1.0

---

## 📊 CLICKHOUSE AGGREGATIONS

### Transaction Facts
```sql
-- Aggregate daily to ClickHouse
INSERT INTO transaction_facts
SELECT 
  transaction_id,
  user_id,
  business_id,
  amount,
  bonus_accrued,
  category,
  created_at
FROM transactions
WHERE created_at >= :last_sync;
```

### RFM Snapshots
```sql
-- Daily RFM calculation
INSERT INTO rfm_snapshots
SELECT 
  today() as snapshot_date,
  user_id,
  dateDiff('day', max(timestamp), today()) as recency_days,
  count(*) as frequency_count,
  sum(amount) as monetary_value,
  rfm_segment
FROM transaction_facts
WHERE timestamp >= today() - INTERVAL 12 MONTH
GROUP BY user_id;
```

---

## 📝 BUSINESS RULES

1. **RFM Update Frequency:** Daily at 02:00
2. **Churn Threshold:** >0.7 probability = high risk
3. **Dashboard Cache:** 15-minute TTL
4. **Historical Data:** 24-month retention

---

**Navigation:** [← Events Service](./events-service.md) | [Database Schema →](../database/00_DATABASE_SCHEMA.md)
