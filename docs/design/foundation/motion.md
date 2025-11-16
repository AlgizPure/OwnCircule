# MOTION

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## ⚡ ANIMATION PRINCIPLES

**Motion serves purpose:**
- Guide attention
- Show relationships
- Provide feedback
- Communicate state

**Not decoration!**

---

## ⏱️ DURATIONS

```yaml
Fast:
  Duration: 100ms
  Usage: Hover states, button press, icon changes
  Feel: Instant, snappy
  
Medium:
  Duration: 200ms
  Usage: Dropdowns, tooltips, small transitions
  Feel: Quick, responsive
  
Normal:
  Duration: 300ms
  Usage: Modals, panels, most transitions
  Feel: Smooth, natural
  
Slow:
  Duration: 500ms
  Usage: Large panels, page transitions
  Feel: Deliberate, important
```

**Rule:** Shorter distance = faster duration

---

## 📈 EASING CURVES

```yaml
Ease-out:
  Curve: cubic-bezier(0.0, 0.0, 0.2, 1)
  Usage: Enter animations (elements appearing)
  Feel: Quick start, gentle finish
  
Ease-in:
  Curve: cubic-bezier(0.4, 0.0, 1, 1)
  Usage: Exit animations (elements disappearing)
  Feel: Slow start, quick finish
  
Ease-in-out:
  Curve: cubic-bezier(0.4, 0.0, 0.2, 1)
  Usage: Moving between states
  Feel: Smooth throughout
  
Linear:
  Curve: linear
  Usage: Continuous animations (spinners, progress)
  Feel: Constant speed
```

**Most common:** ease-out (natural feel)

---

## 🎬 ANIMATION TYPES

### Fade

```css
.fade-in {
  animation: fadeIn 200ms ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

**Usage:** Tooltips, notifications, subtle appearances

---

### Slide

```css
.slide-up {
  animation: slideUp 300ms ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Usage:** Modals, dropdowns, panels

---

### Scale

```css
.scale-in {
  animation: scaleIn 200ms ease-out;
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

**Usage:** Popovers, context menus, growing elements

---

### Rotate

```css
.spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

**Usage:** Loading spinners (continuous)

---

## 🎯 USAGE GUIDELINES

### Button Hover

```css
.button {
  transition: all 100ms ease-out;
}

.button:hover {
  background-color: var(--primary-600);
  transform: translateY(-1px);
}
```

**Fast (100ms)** for immediate feedback.

---

### Modal Enter

```css
.modal {
  animation: modalEnter 300ms ease-out;
}

@keyframes modalEnter {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

**Normal (300ms)** for clear transition.

---

### Dropdown

```css
.dropdown {
  animation: dropdownSlide 200ms ease-out;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Medium (200ms)** for quick but smooth.

---

## ⚖️ BEST PRACTICES

**Do's:**
- ✅ Use motion for feedback and guidance
- ✅ Keep animations short (< 500ms)
- ✅ Consistent durations across similar actions
- ✅ Respect prefers-reduced-motion

**Don'ts:**
- ❌ Don't animate for decoration
- ❌ Don't use slow animations (feels laggy)
- ❌ Don't animate too many things at once
- ❌ Don't ignore accessibility preferences

---

## ♿ ACCESSIBILITY

### Reduced Motion

**CRITICAL:** Respect user preference!

```css
/* Default: animations */
.element {
  transition: all 300ms ease-out;
}

/* Reduced motion: instant */
@media (prefers-reduced-motion: reduce) {
  .element {
    transition: none;
  }
}
```

**Always provide this!**

---

## 🔧 IMPLEMENTATION

### CSS Variables

```css
:root {
  --duration-fast: 100ms;
  --duration-medium: 200ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
  
  --ease-out: cubic-bezier(0.0, 0.0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0.0, 1, 1);
  --ease-in-out: cubic-bezier(0.4, 0.0, 0.2, 1);
}

.button {
  transition: all var(--duration-fast) var(--ease-out);
}
```

### Tailwind Config

```js
module.exports = {
  theme: {
    transitionDuration: {
      'fast': '100ms',
      'medium': '200ms',
      'normal': '300ms',
      'slow': '500ms',
    },
    transitionTimingFunction: {
      'ease-out': 'cubic-bezier(0.0, 0.0, 0.2, 1)',
      'ease-in': 'cubic-bezier(0.4, 0.0, 1, 1)',
      'ease-in-out': 'cubic-bezier(0.4, 0.0, 0.2, 1)',
    }
  }
}
```

---

## 📝 COMMON PATTERNS

```css
/* Hover (fast) */
transition: all 100ms ease-out;

/* Dropdown (medium) */
transition: all 200ms ease-out;

/* Modal (normal) */
transition: all 300ms ease-out;

/* Panel (slow) */
transition: all 500ms ease-out;
```

---

**Motion should feel natural, not noticed.** ⚡

