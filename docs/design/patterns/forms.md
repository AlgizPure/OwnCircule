# FORM PATTERNS

**Version:** 1.0  
**Status:** Template

---

## 📋 COMMON PATTERNS

### Single Column Form

**Best for:** Most forms (faster completion)

```
Label
[Input]

Label
[Input]

[Submit]
```

**Why:** Natural reading flow, mobile-friendly

---

### Multi-Step Form

**Best for:** Long forms (onboarding, checkout)

```
Step 1 → Step 2 → Step 3

[Progress bar: 33%]

Current Step Fields...

[Back] [Next]
```

**Include:**
- Progress indicator
- Step labels
- Back button
- Save progress

---

### Inline Validation

```
Email *
[input@example.com___] ✓
✓ Valid email
```

**Timing:**
- Validate onBlur (after leaving field)
- Show success inline
- Show errors inline

---

### Optional vs Required

**Option 1: Mark required**
```
Name *
Email *
Phone (optional)
```

**Option 2: Mark optional (if most are required)**
```
Name
Email
Phone (optional)
```

---

### Field Groups

```
Shipping Address
├─ Street
├─ City
├─ State
└─ Zip

Billing Address
└─ [✓] Same as shipping
```

**Use fieldset for related fields**

---

**Forms should feel easy, not work.** 📝

