# CRM Integration Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** CRM Integration

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | CRMIntegration |
| **Database Table** | `crm_integrations` |
| **Module:** | CRM Sync |
| **Type** | Supporting |
| **Primary Key** | `id` (uuid) |

### Description

CRMIntegration entity stores sync configuration and credentials for external CRM systems (YCLIENTS, Iiko, 1C, AMO CRM, Renovatio). One-to-one with Business.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE crm_integrations (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Reference
  business_id           UUID NOT NULL UNIQUE REFERENCES businesses(id),
  
  -- CRM Type
  crm_type              VARCHAR(50) NOT NULL
                        CHECK (crm_type IN ('yclients', 'iiko', '1c', 'amo_crm', 'renovatio', 'csv')),
  
  -- Credentials (Encrypted)
  api_key               BYTEA,  -- AES-256 encrypted
  api_secret            BYTEA,
  api_url               VARCHAR(500),
  additional_config     JSONB,  -- CRM-specific settings
  
  -- Sync Configuration
  sync_enabled          BOOLEAN DEFAULT false,
  sync_interval_minutes INT DEFAULT 5,
  last_sync_at          TIMESTAMP WITH TIME ZONE,
  last_sync_status      VARCHAR(20),  -- 'success' | 'failed' | 'in_progress'
  next_sync_at          TIMESTAMP WITH TIME ZONE,
  
  -- Statistics
  total_syncs           INT DEFAULT 0,
  successful_syncs      INT DEFAULT 0,
  failed_syncs          INT DEFAULT 0,
  last_error            TEXT,
  transactions_synced   INT DEFAULT 0,
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_crm_integrations_business ON crm_integrations(business_id);
CREATE INDEX idx_crm_integrations_type ON crm_integrations(crm_type);
CREATE INDEX idx_crm_integrations_next_sync ON crm_integrations(next_sync_at) WHERE sync_enabled = true;
```

---

### TypeScript Type

```typescript
interface CRMIntegration {
  id: string;
  businessId: string;
  
  crmType: 'yclients' | 'iiko' | '1c' | 'amo_crm' | 'renovatio' | 'csv';
  
  // Credentials not exposed in API
  apiUrl?: string;
  additionalConfig?: Record<string, any>;
  
  syncEnabled: boolean;
  syncIntervalMinutes: number;
  lastSyncAt?: Date;
  lastSyncStatus?: 'success' | 'failed' | 'in_progress';
  nextSyncAt?: Date;
  
  totalSyncs: number;
  successfulSyncs: number;
  failedSyncs: number;
  lastError?: string;
  transactionsSynced: number;
  
  createdAt: Date;
  updatedAt: Date;
}
```

---

## 📝 BUSINESS RULES

1. **Credential Encryption** - All API keys encrypted with AES-256
2. **Health Checks** - Test connection before enabling sync
3. **Retry Logic** - Max 3 retries on failure with exponential backoff
4. **Duplicate Detection** - Use external_id to prevent duplicate transactions

---

**Navigation:** [← Status Tier Entity](./status-tier.md) | [API Overview →](../api/00_API_OVERVIEW.md)
