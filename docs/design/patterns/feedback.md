# FEEDBACK PATTERNS

**Version:** 1.0

---

## 💬 PATTERNS

### Toast Notifications

```
┌──────────────────────┐
│ ✓ Saved successfully │  ← Auto-dismiss (3s)
└──────────────────────┘
```

**Use for:**
- Success confirmation
- Non-critical info
- Auto-dismiss

**Position:** Top-right or bottom-center

---

### Alerts

```
┌─────────────────────────────┐
│ ⚠ Warning: Action required  │
│ [Dismiss]                   │
└─────────────────────────────┘
```

**Use for:**
- Important notices
- Warnings
- Stays until dismissed

**Position:** Top of content area

---

### Inline Errors

```
Email *
[invalid@___]
✗ Please enter a valid email
```

**Use for:**
- Form validation
- Input-specific errors
- Real-time feedback

---

### Loading States

```
[●●●   ] Loading...
```

**Types:**
- Spinner (indeterminate)
- Progress bar (determinate)
- Skeleton (content loading)

**Always show loading for > 200ms**

---

### Empty States

```
┌─────────────────┐
│   [Illustration]│
│                 │
│ No items yet    │
│ [Create First]  │
└─────────────────┘
```

**Include:**
- Illustration or icon
- Explanation
- Clear CTA

---

**Give feedback instantly and clearly.** 💬

