# Notification Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Notification System

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | Notification |
| **Database Table** | `notifications` |
| **Module:** | Notifications |
| **Type** | Supporting |
| **Primary Key** | `id` (uuid) |

### Description

Notification entity represents a message sent to a user via push, SMS, or email. Queued for async delivery via Celery. Tracks delivery status and user interaction.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE notifications (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Recipient
  user_id               UUID NOT NULL REFERENCES users(id),
  
  -- Channel
  channel               VARCHAR(20) NOT NULL
                        CHECK (channel IN ('push', 'sms', 'email')),
  
  -- Content
  title                 VARCHAR(255),
  body                  TEXT NOT NULL,
  data                  JSONB,  -- Additional payload for deep linking
  
  -- Template
  template_name         VARCHAR(100),
  template_variables    JSONB,
  
  -- Delivery
  status                VARCHAR(20) DEFAULT 'pending'
                        CHECK (status IN ('pending', 'sent', 'delivered', 'failed', 'read')),
  sent_at               TIMESTAMP WITH TIME ZONE,
  delivered_at          TIMESTAMP WITH TIME ZONE,
  read_at               TIMESTAMP WITH TIME ZONE,
  failed_reason         TEXT,
  retry_count           INT DEFAULT 0,
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_notifications_user ON notifications(user_id, created_at DESC);
CREATE INDEX idx_notifications_status ON notifications(status) WHERE status = 'pending';
CREATE INDEX idx_notifications_channel ON notifications(channel);
```

---

### TypeScript Type

```typescript
interface Notification {
  id: string;
  userId: string;
  
  channel: 'push' | 'sms' | 'email';
  
  title?: string;
  body: string;
  data?: Record<string, any>;
  
  templateName?: string;
  templateVariables?: Record<string, any>;
  
  status: 'pending' | 'sent' | 'delivered' | 'failed' | 'read';
  sentAt?: Date;
  deliveredAt?: Date;
  readAt?: Date;
  failedReason?: string;
  retryCount: number;
  
  createdAt: Date;
}
```

---

## 📝 BUSINESS RULES

1. **Rate Limiting** - Max 10 push/day per user
2. **Quiet Hours** - No push between 23:00-08:00
3. **Retry Policy** - Max 3 retries for failed deliveries
4. **Template System** - Use templates for consistency

---

**Navigation:** [← Cross Promo Chain Entity](./cross-promo-chain.md) | [Status Tier Entity →](./status-tier.md)
