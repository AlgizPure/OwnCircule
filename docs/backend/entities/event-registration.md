# Event Registration Entity

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** ✅ Implemented  
**Module** Event Management

---

## 📊 OVERVIEW

| Property | Value |
|----------|-------|
| **Entity Name** | EventRegistration |
| **Database Table** | `event_registrations` |
| **Module** | Events Hub |
| **Type** | Core |
| **Primary Key** | `id` (uuid) |

### Description

EventRegistration entity represents a user's RSVP to an event. Tracks registration status, check-in, dietary restrictions, and +1 guest allowance.

---

## 🏗️ STRUCTURE

### Database Schema

```sql
CREATE TABLE event_registrations (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- References
  event_id              UUID NOT NULL REFERENCES events(id),
  user_id               UUID NOT NULL REFERENCES users(id),
  
  -- Registration Details
  status                VARCHAR(20) DEFAULT 'registered'
                        CHECK (status IN ('registered', 'waitlist', 'cancelled', 'attended', 'no_show')),
  plus_one              BOOLEAN DEFAULT false,
  plus_one_name         VARCHAR(200),
  dietary_restrictions  TEXT,
  
  -- Check-in
  checked_in            BOOLEAN DEFAULT false,
  checked_in_at         TIMESTAMP WITH TIME ZONE,
  qr_code               VARCHAR(100) UNIQUE,  -- QR code for check-in
  
  -- Metadata
  created_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  cancelled_at          TIMESTAMP WITH TIME ZONE
);

-- Indexes
CREATE INDEX idx_event_registrations_event ON event_registrations(event_id, status);
CREATE INDEX idx_event_registrations_user ON event_registrations(user_id, created_at DESC);
CREATE UNIQUE INDEX idx_event_registrations_unique ON event_registrations(event_id, user_id) WHERE status != 'cancelled';
```

---

### TypeScript Type

```typescript
interface EventRegistration {
  id: string;
  eventId: string;
  userId: string;
  
  status: 'registered' | 'waitlist' | 'cancelled' | 'attended' | 'no_show';
  plusOne: boolean;
  plusOneName?: string;
  dietaryRestrictions?: string;
  
  checkedIn: boolean;
  checkedInAt?: Date;
  qrCode: string;
  
  createdAt: Date;
  cancelledAt?: Date;
}
```

---

## 📝 BUSINESS RULES

1. **Unique Registration** - User can register once per event
2. **Waitlist Logic** - Auto-promoted when spot available
3. **QR Check-in** - Generate unique QR code on registration
4. **Cancellation Window** - Can cancel up to 24h before event

---

**Navigation:** [← Event Entity](./event.md) | [Cross Promo Chain Entity →](./cross-promo-chain.md)
