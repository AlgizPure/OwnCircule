# Event Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module:** Event Management

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | Event |
| **Database Table** | `events` |
| **Module** | Events Hub |
| **Type** | Core |
| **Primary Key** | `id` (uuid) |

### Description

Event entity represents a community event (masterclass, networking, closed gathering). Can be created by platform or proposed by VIP/Elite members with voting.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE events (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Basic Info
  title                 VARCHAR(255) NOT NULL,
  description           TEXT,
  cover_image_url       VARCHAR(500),
  
  -- Schedule
  date                  TIMESTAMP WITH TIME ZONE NOT NULL,
  duration_minutes      INT DEFAULT 120,
  location              VARCHAR(255),
  location_type         VARCHAR(20) CHECK (location_type IN ('offline', 'online', 'hybrid')),
  online_link           VARCHAR(500),
  
  -- Capacity
  max_participants      INT,
  current_participants  INT DEFAULT 0,
  waitlist_enabled      BOOLEAN DEFAULT true,
  
  -- Access Control
  min_status_tier       VARCHAR(20) DEFAULT 'Insider'
                        CHECK (min_status_tier IN ('Insider', 'VIP', 'Elite', 'Inner Circle')),
  event_type            VARCHAR(20) DEFAULT 'open'
                        CHECK (event_type IN ('open', 'paid', 'elite_only')),
  price                 DECIMAL(10,2) DEFAULT 0.00,
  
  -- Proposal & Voting
  created_by_id         UUID NOT NULL REFERENCES users(id),
  is_proposal           BOOLEAN DEFAULT false,
  voting_enabled        BOOLEAN DEFAULT false,
  votes_for             INT DEFAULT 0,
  votes_against         INT DEFAULT 0,
  voting_ends_at        TIMESTAMP WITH TIME ZONE,
  
  -- Status
  status                VARCHAR(20) DEFAULT 'draft'
                        CHECK (status IN ('draft', 'proposed', 'approved', 'published', 'in_progress', 'completed', 'cancelled')),
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  published_at          TIMESTAMP WITH TIME ZONE,
  cancelled_at          TIMESTAMP WITH TIME ZONE
);

-- Indexes
CREATE INDEX idx_events_date ON events(date) WHERE status = 'published';
CREATE INDEX idx_events_status ON events(status);
CREATE INDEX idx_events_creator ON events(created_by_id);
CREATE INDEX idx_events_voting ON events(voting_ends_at) WHERE voting_enabled = true;
```

---

### TypeScript Type

```typescript
interface Event {
  id: string;
  
  title: string;
  description?: string;
  coverImageUrl?: string;
  
  date: Date;
  durationMinutes: number;
  location?: string;
  locationType: 'offline' | 'online' | 'hybrid';
  onlineLink?: string;
  
  maxParticipants?: number;
  currentParticipants: number;
  waitlistEnabled: boolean;
  
  minStatusTier: 'Insider' | 'VIP' | 'Elite' | 'Inner Circle';
  eventType: 'open' | 'paid' | 'elite_only';
  price: number;
  
  createdById: string;
  isProposal: boolean;
  votingEnabled: boolean;
  votesFor: number;
  votesAgainst: number;
  votingEndsAt?: Date;
  
  status: string;
  
  createdAt: Date;
  updatedAt: Date;
}
```

---

## 🌐 API ENDPOINTS

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/v1/events` | List events | Member |
| POST | `/api/v1/events` | Create event proposal | VIP+ |
| GET | `/api/v1/events/:id` | Get event details | Member |
| POST | `/api/v1/events/:id/register` | Register for event | Member |
| POST | `/api/v1/events/:id/vote` | Vote on proposal | Member |

**Detailed Documentation:** [Events API](../api/events-api.md)

---

## 📝 BUSINESS RULES

1. **Weighted Voting** - Vote weight based on status (Insider:1, VIP:2, Elite:3, Inner:5)
2. **Approval Threshold** - 60% positive votes for approval
3. **Capacity Management** - Auto-waitlist when full
4. **Budget Allocation** - Funded from 2% of all purchases

---

**Navigation:** [← Coupon Entity](./coupon.md) | [Event Registration Entity →](./event-registration.md)
