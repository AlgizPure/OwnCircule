
**Response Success (200):**
{
  "result": "type"
}

**Response Error (4xx/5xx):**
{
  "error": "message"
}

[Повторить для каждого endpoint]

---

## 7. UI/UX REQUIREMENTS

### 7.1 Design System Reference

**Foundation:**
- Colors: [Link to docs/design/foundation/colors.md or specify]
- Typography: [Link to docs/design/foundation/typography.md or specify]
- Spacing: [Link to docs/design/foundation/spacing.md or standard]

**Design Files:**
- Figma: [Link to Figma file/prototype]
- Design Specs: [Link or description]

---

### 7.2 Screens & Components

#### Screen/Component: [Name]

**Purpose:** [What this screen/component does]

**Layout:**
- Structure: [Description or ASCII diagram]
- Figma: [Link to specific screen in Figma]
- Screen Documentation: [Link to docs/design/screens/[name].md if exists]

**Components Used:**
- [Component 1]: [Variant, link to docs/design/components/[name].md]
- [Component 2]: [Variant, link to docs/design/components/[name].md]
- [Component 3]: [Variant]

**User Interactions:**
- Action 1: [User does X] → [System responds Y]
- Action 2: [User does X] → [System responds Y]
- Edge case: [What happens if...]

**Form Validation (if applicable):**
- Field 1: [Rules, error messages, format]
  - Required: [Yes/No]
  - Validation: [Pattern/rules]
  - Error message: "[Specific message]"
- Field 2: [Rules]

**States:**
- Loading: [How to show]
- Empty: [Empty state design, message, CTA]
- Error: [Error handling, retry options]
- Success: [Success confirmation]

**Responsive Behavior:**
- Desktop (≥1024px): [Layout description]
- Tablet (768-1023px): [Adjustments]
- Mobile (<768px): [Mobile-optimized layout]

[Повторить для каждого UI элемента]

---

### 7.3 User Flows

**Flow: [Name]** (например, "User Sign Up Flow")

1. Entry Point: [Where user starts]
2. Step 1: [User action] → [Screen/State]
3. Step 2: [User action] → [Screen/State]
4. Exit Point: [Where flow ends]

**Alternative Flows:**
- Error path: [What if error occurs]
- Cancel path: [What if user cancels]

**Journey Map Reference:** [Link to docs/design/user-research/journey-maps.md if relevant]

---

### 7.4 Accessibility Requirements

**WCAG Compliance:** [Target level - AA recommended]

**Keyboard Navigation:**
- Tab order: [Logical flow]
- Shortcuts: [If any - e.g., Cmd+S to save]
- Focus indicators: [Must be visible]

**Screen Reader:**
- ARIA labels: [Required labels]
- Announcements: [What to announce on state changes]
- Semantic HTML: [Use semantic elements]

**Color & Contrast:**
- All text: ≥4.5:1 contrast ratio
- Interactive elements: ≥3:1 contrast
- Don't rely on color alone for meaning

**Touch Targets (Mobile):**
- Minimum size: 44x44px
- Adequate spacing between interactive elements

**Testing:**
- [ ] Keyboard accessible (all functions)
- [ ] Screen reader tested (NVDA/VoiceOver)
- [ ] Color contrast verified
- [ ] Responsive on mobile/tablet/desktop

**Reference:** [Link to docs/design/accessibility/overview.md]

---

### 7.5 Content & Microcopy

**Voice & Tone:** [Link to docs/design/content/voice-and-tone.md]

**Key Messages:**
- Page title: "[Title]"
- Primary CTA: "[Button text]"
- Helper text: "[Helpful guidance]"
- Error messages: "[Specific, actionable messages]"
- Success messages: "[Confirmation text]"

**Content Guidelines Reference:**
- Writing: [Link to docs/design/content/writing-guidelines.md]
- Errors: [Link to docs/design/content/error-messages.md]
- Microcopy: [Link to docs/design/content/microcopy.md]

---

### 7.6 Design Patterns Used

**Patterns from Design System:**
- [Pattern 1]: [Link to docs/design/patterns/[name].md]
  - Application: [How it's used in this module]
- [Pattern 2]: [Link]
  - Application: [How it's used]

**Custom Patterns (if any):**
- [Pattern name]: [Description]
  - Rationale: [Why this custom pattern]
  - Documentation: [Where documented]

---

### 7.7 User Research Insights (if applicable)

**Personas Served:**
- [Persona 1]: [Link to docs/design/user-research/personas.md]
  - Primary goal: [What they want to achieve]
- [Persona 2]: [Link]
  - Primary goal: [What they want]

**Pain Points Addressed:**
- [Pain point 1]: [Link to docs/design/user-research/pain-points.md]
  - Solution: [How this module solves it]
- [Pain point 2]: [Link]
  - Solution: [How addressed]

---

### 7.8 Design Tokens (if custom styling needed)

**Custom Colors (if any):**
```yaml
module-specific-color: #HEXCODE
```

**Custom Spacing (if any):**
```yaml
module-specific-spacing: 24px
```

**Reference:** [Link to docs/design/resources/design-tokens.json]

**Rationale:** [Why custom tokens needed vs design system]

---

## 8. INTEGRATION POINTS

### 8.1 Internal Dependencies
- Module 1: [что требуется, интерфейс]
- Module 2: [что требуется, интерфейс]

### 8.2 External Dependencies
- Service 1: [что требуется, API]
- Library 1: [версия, функции]

---

## 9. TESTING REQUIREMENTS

### 9.1 Unit Tests
- Coverage Target: [%]
- Key Test Cases: [список]

### 9.2 Integration Tests
- Test Scenarios: [список]

### 9.3 E2E Tests
- Critical User Flows: [список]

### 9.4 Performance Tests
- Load Tests: [требования]
- Stress Tests: [требования]

---

## 10. DEPLOYMENT & OPERATIONS

### 10.1 Environment Variables
- VAR1: [описание, значение по умолчанию]
- VAR2: [описание, значение по умолчанию]

### 10.2 Configuration
- Config parameters needed

### 10.3 Monitoring
- Metrics to track
- Alerts to configure

### 10.4 Logging
- What events to log
- Log levels

---

## 11. ASSUMPTIONS & CONSTRAINTS

### 11.1 Assumptions
- Assumption 1
- Assumption 2

### 11.2 Constraints
- Technical constraints
- Business constraints
- Timeline constraints

---

## 12. RISKS & MITIGATION

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Risk 1 | High | Medium | Strategy |
| Risk 2 | Medium | Low | Strategy |

---

## 13. ACCEPTANCE CRITERIA (Module-Level)

- [ ] All user stories implemented and tested
- [ ] All functional requirements met
- [ ] Non-functional requirements verified
- [ ] Documentation complete
- [ ] Code reviewed and approved
- [ ] Tests passing (unit, integration, E2E)
- [ ] Security review passed
- [ ] Performance benchmarks met

---

## 14. OPEN QUESTIONS / DECISIONS NEEDED

- [ ] Question 1: [описание] - Owner: [кто] - Due: [дата]
- [ ] Question 2: [описание] - Owner: [кто] - Due: [дата]

---

## 15. CHANGELOG

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| YYYY-MM-DD | 0.1 | Initial draft | Name |
| YYYY-MM-DD | 0.2 | Added section X | Name |

---

ИСПОЛЬЗУЙ ЭТОТ ШАБЛОН для создания требований к каждому модулю (auth, profile, dashboard и т.д.)


---

## 📝 СОЗДАНИЕ ПЕРВОГО МОДУЛЯ - ПРИМЕР

**Промпт для создания `auth_requirements.md`:**

