# Events Service

**Version:** 1.0  
**Last Updated:** 2025-11-17  
**Status:** Active

---

## 🎯 PURPOSE

Manages community events, proposals, registrations, voting, and check-ins for the Свой Круг event hub.

**Primary Responsibilities:**
- Event creation and lifecycle management
- Member registration with capacity management
- Weighted voting system for proposals
- QR-based check-in at events

---

## ⚙️ KEY FUNCTIONS

### register_for_event()

**Purpose:** Register user for event with waitlist support

**Logic:**
```python
# Check capacity
if event.current_participants >= event.max_participants:
    if event.waitlist_enabled:
        status = 'waitlist'
    else:
        raise EventFullError()
else:
    status = 'registered'
    event.current_participants += 1

# Create registration
registration = EventRegistration(
    event_id=event.id,
    user_id=user.id,
    status=status,
    qr_code=generate_qr_code()
)

# Send confirmation
send_event_confirmation(user, event, registration)

return registration
```

### process_vote()

**Purpose:** Process weighted vote on event proposal

**Logic:**
```python
# Calculate vote weight based on status tier
vote_weights = {
    'Insider': 1.0,
    'VIP': 2.0,
    'Elite': 3.0,
    'Inner Circle': 5.0
}

weight = vote_weights[user.status_tier]

# Record vote
if vote == 'yes':
    event.votes_for += weight
else:
    event.votes_against += weight

# Check approval threshold (60%)
total_votes = event.votes_for + event.votes_against
approval_rate = event.votes_for / total_votes

if approval_rate >= 0.6 and voting_ended:
    event.status = 'approved'
    notify_creator(event, 'approved')

return VoteResult(weight=weight, current_results=event)
```

---

## 📝 BUSINESS RULES

1. **Weighted Voting:** Vote weight based on status tier
2. **Approval Threshold:** 60% positive votes
3. **Budget Allocation:** 2% of all purchases
4. **Capacity Management:** Auto-waitlist when full

---

**Navigation:** [← Cross-Promo Service](./cross-promo-service.md) | [Analytics Service →](./analytics-service.md)
