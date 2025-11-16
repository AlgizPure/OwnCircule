# ADR-XXX: [Short Title of Decision]

**Date:** YYYY-MM-DD  
**Status:** Proposed | Accepted | Superseded | Deprecated | Rejected  
**Author:** Team Name / Person Name  
**Deciders:** List of people involved in decision

---

## Context

**What is the issue we're facing? What factors are driving this decision?**

Describe the context and problem statement. Include:
- Current situation
- Why this decision is needed
- Constraints (technical, business, timeline, budget)
- Stakeholders affected
- Related decisions or requirements

Be specific about:
- What assumptions are we making?
- What requirements must be met?
- What is the current pain point?

---

## Decision

**What are we going to do?**

State the decision clearly and concisely. Use declarative language:
- "We will use PostgreSQL for the primary database"
- "We will adopt a microservices architecture"
- "We will implement JWT-based authentication"

Include:
- High-level approach
- Key components or technologies chosen
- Implementation timeline (if applicable)

---

## Alternatives Considered

**What other options did we evaluate?**

List alternative solutions considered and why they were not chosen:

### Alternative 1: [Name]

**Description:** Brief description of the alternative

**Pros:**
- Advantage 1
- Advantage 2

**Cons:**
- Disadvantage 1
- Disadvantage 2

**Why Not Chosen:** Specific reason for rejection

---

### Alternative 2: [Name]

**Description:** ...

**Pros:**
- ...

**Cons:**
- ...

**Why Not Chosen:** ...

---

## Consequences

**What are the outcomes of this decision?**

Document both positive and negative consequences:

### Positive Consequences

- **Benefit 1:** Explanation
- **Benefit 2:** Explanation
- **Benefit 3:** Explanation

### Negative Consequences

- **Trade-off 1:** Explanation and mitigation plan
- **Trade-off 2:** Explanation and mitigation plan
- **Risk 1:** Potential risk and how we'll monitor it

### Impact Assessment

| Area | Impact | Severity |
|------|--------|----------|
| Performance | Improves query speed | High |
| Cost | Increases hosting cost | Low |
| Developer Experience | Requires learning curve | Medium |
| Maintenance | Reduces complexity | High |

---

## Implementation

**How will this decision be implemented?**

Optional section if implementation details are relevant:

### Steps

1. Step one
2. Step two
3. Step three

### Timeline

- **Week 1:** Task A
- **Week 2:** Task B
- **Week 3:** Task C

### Dependencies

- Requires completion of [ADR-XXX]
- Depends on infrastructure team approval

---

## Validation

**How will we know if this decision was successful?**

Define success criteria and metrics:

### Success Criteria

- [ ] Criteria 1 (e.g., "99.9% uptime achieved")
- [ ] Criteria 2 (e.g., "Response time < 200ms")
- [ ] Criteria 3 (e.g., "No data loss incidents")

### Metrics to Track

- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

### Review Date

- **Review on:** YYYY-MM-DD (6 months after implementation)
- **Responsible:** Team/Person name

---

## Related Decisions

- Supersedes: [ADR-XXX: Previous Decision](XXX-old-decision.md)
- Related to: [ADR-XXX: Related Decision](XXX-related-decision.md)
- Depends on: [ADR-XXX: Foundation Decision](XXX-foundation.md)

---

## References

**Links and resources that informed this decision:**

- [Technical documentation](https://example.com/docs)
- [Benchmark results](https://example.com/benchmark)
- [Industry best practices](https://example.com/best-practices)
- [Team discussion thread](https://slack.com/thread/12345)

---

## Notes

**Additional context, caveats, or future considerations:**

- Note 1
- Note 2
- Future consideration 1

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial draft | Author Name |
| YYYY-MM-DD | Updated after team review | Author Name |
| YYYY-MM-DD | Status changed to Accepted | Team Lead |

---

**Navigation:** [← ADR Index](00_ADR_INDEX.md)

