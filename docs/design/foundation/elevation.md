# ELEVATION

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## 🏔️ ELEVATION SYSTEM

Elevation создает depth через shadows и z-index.

### Shadow Levels

```yaml
Level 0 (Flat):
  Shadow: none
  Z-index: 0
  Usage: Page background, base elements
  
Level 1 (Raised):
  Shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
  Z-index: 100
  Usage: Cards, buttons (rest state)
  
Level 2 (Elevated):
  Shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
  Z-index: 200
  Usage: Buttons (hover), dropdowns
  
Level 3 (Floating):
  Shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)
  Z-index: 300
  Usage: Modals, popovers, tooltips
  
Level 4 (High):
  Shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)
  Z-index: 400
  Usage: Side panels, drawers
  
Level 5 (Highest):
  Shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)
  Z-index: 500
  Usage: Full-screen modals, notifications
```

---

## 🎯 USAGE GUIDELINES

### When to Use Each Level

**Level 0 (Flat):**
- Page backgrounds
- Inline elements
- No interaction

**Level 1 (Raised):**
- Cards
- Buttons (default)
- Form inputs
- Static containers

**Level 2 (Elevated):**
- Buttons (hover)
- Active states
- Dropdown menus
- Date pickers

**Level 3 (Floating):**
- Modals
- Popovers
- Tooltips
- Context menus

**Level 4 (High):**
- Sidebars
- Slide-out panels
- Drawers

**Level 5 (Highest):**
- Full overlays
- Toast notifications
- Global alerts
- Loading screens

---

## 🔧 IMPLEMENTATION

### CSS Variables

```css
:root {
  --shadow-0: none;
  --shadow-1: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  --shadow-2: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  --shadow-3: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  --shadow-4: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  --shadow-5: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
  
  --z-base: 0;
  --z-raised: 100;
  --z-elevated: 200;
  --z-floating: 300;
  --z-high: 400;
  --z-highest: 500;
}

.card {
  box-shadow: var(--shadow-1);
  z-index: var(--z-raised);
}

.modal {
  box-shadow: var(--shadow-3);
  z-index: var(--z-floating);
}
```

### Tailwind Config

```js
module.exports = {
  theme: {
    boxShadow: {
      '1': '0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)',
      '2': '0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)',
      '3': '0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)',
    },
    zIndex: {
      '0': 0,
      '100': 100,
      '200': 200,
      '300': 300,
      '400': 400,
      '500': 500,
    }
  }
}
```

---

## ⚖️ BEST PRACTICES

**Do's:**
- ✅ Use elevation to show hierarchy
- ✅ Higher elevation = more important/temporary
- ✅ Consistent shadow levels
- ✅ Subtle shadows (don't overdo)

**Don'ts:**
- ❌ Don't skip levels (1 → 4)
- ❌ Don't use too many elevated elements
- ❌ Don't use elevation for decoration
- ❌ Don't forget z-index with shadows

---

## ♿ ACCESSIBILITY

- Elevation is visual only
- Don't rely on shadows alone for meaning
- Use ARIA labels for overlays
- Ensure focus visible on elevated elements

---

**Elevation creates depth and hierarchy.** 🏔️

