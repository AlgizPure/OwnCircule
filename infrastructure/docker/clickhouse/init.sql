-- ClickHouse Initialization Script
-- Creates analytics database and base tables for OLAP

-- Create analytics database
CREATE DATABASE IF NOT EXISTS analytics;

USE analytics;

-- Transaction Facts Table (for RFM analysis)
CREATE TABLE IF NOT EXISTS transaction_facts
(
    transaction_id UInt64,
    user_id UInt64,
    business_id UInt64,
    amount Float64,
    bonus_accrued UInt32,
    bonus_redeemed UInt32,
    transaction_date DateTime,
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(transaction_date)
ORDER BY (user_id, transaction_date)
SETTINGS index_granularity = 8192;

-- User Activity Facts (for engagement analytics)
CREATE TABLE IF NOT EXISTS user_activity_facts
(
    user_id UInt64,
    activity_type String,
    activity_date DateTime,
    metadata String,  -- JSON string
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(activity_date)
ORDER BY (user_id, activity_date)
SETTINGS index_granularity = 8192;

-- Event Participation Facts
CREATE TABLE IF NOT EXISTS event_participation_facts
(
    event_id UInt64,
    user_id UInt64,
    business_id UInt64,
    registration_date DateTime,
    attended Bool DEFAULT false,
    attended_date Nullable(DateTime),
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(registration_date)
ORDER BY (event_id, user_id)
SETTINGS index_granularity = 8192;

-- Cross-Promo Chain Facts
CREATE TABLE IF NOT EXISTS cross_promo_facts
(
    chain_id UInt64,
    user_id UInt64,
    business_id UInt64,
    step_number UInt8,
    completed Bool DEFAULT false,
    completion_date Nullable(DateTime),
    reward_value Float64,
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(created_at)
ORDER BY (chain_id, user_id, step_number)
SETTINGS index_granularity = 8192;

-- Business Performance Facts
CREATE TABLE IF NOT EXISTS business_performance_facts
(
    business_id UInt64,
    date Date,
    total_transactions UInt32,
    total_revenue Float64,
    unique_customers UInt32,
    bonus_given UInt32,
    bonus_redeemed UInt32,
    created_at DateTime DEFAULT now()
)
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(date)
ORDER BY (business_id, date)
SETTINGS index_granularity = 8192;

SELECT 'ClickHouse analytics database initialized' AS status;
