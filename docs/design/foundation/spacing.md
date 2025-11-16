# SPACING

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## 📐 SPACING SCALE

**Base Unit:** 4px (0.25rem)

**Scale:** Multiples of 4

```yaml
0:   0px      (0rem)      # No space
1:   4px      (0.25rem)   # Micro
2:   8px      (0.5rem)    # Tiny
3:   12px     (0.75rem)   # Small
4:   16px     (1rem)      # Base
5:   20px     (1.25rem)   # Medium-small
6:   24px     (1.5rem)    # Medium
8:   32px     (2rem)      # Large
10:  40px     (2.5rem)    # Extra large
12:  48px     (3rem)      # 2X large
16:  64px     (4rem)      # 3X large
20:  80px     (5rem)      # 4X large
24:  96px     (6rem)      # 5X large
```

**Why 4px?**
- Scales well (4, 8, 16, 32, 64...)
- Divisible (works with most grids)
- Industry standard
- Aligns with typography line heights

---

## 🎯 USAGE GUIDELINES

### Component Spacing (Internal)

```yaml
Micro (4px):
  Usage: Between icon and text in button
  Example: [Icon] 4px "Button Text"

Tiny (8px):
  Usage: Inside components (padding)
  Example: Badge padding, chip spacing

Small (12px):
  Usage: Component padding
  Example: Button padding (12px vertical)

Base (16px):
  Usage: Standard padding/margin
  Example: Card padding, input padding

Medium (24px):
  Usage: Section spacing
  Example: Between form fields

Large (32px):
  Usage: Component separation
  Example: Between cards in grid
```

### Layout Spacing (Page Level)

```yaml
Medium (24px):
  Usage: Between sections (mobile)
  
Large (32px):
  Usage: Between sections (tablet)

Extra Large (40px):
  Usage: Between sections (desktop)

2X Large (48px):
  Usage: Major sections
  
3X Large (64px):
  Usage: Page sections with emphasis
```

---

## 📱 RESPONSIVE SPACING

### Mobile (< 768px)

```yaml
Page padding: 16px
Section spacing: 24px
Component spacing: 16px
```

### Tablet (768px - 1023px)

```yaml
Page padding: 24px
Section spacing: 32px
Component spacing: 20px
```

### Desktop (≥1024px)

```yaml
Page padding: 32px
Section spacing: 48px
Component spacing: 24px
```

---

## 🏗️ COMMON PATTERNS

### Card

```css
.card {
  padding: 24px;        /* Content padding */
  margin-bottom: 16px;  /* Space between cards */
  gap: 16px;            /* Internal spacing (flex/grid) */
}
```

### Form

```css
.form-field {
  margin-bottom: 24px;  /* Between fields */
}

.input {
  padding: 12px 16px;   /* Inside input */
}

.label {
  margin-bottom: 8px;   /* Label to input */
}
```

### Button

```css
.button {
  padding: 12px 24px;   /* Vertical / Horizontal */
  gap: 8px;             /* Icon to text */
}

.button-small {
  padding: 8px 16px;
}

.button-large {
  padding: 16px 32px;
}
```

### Grid

```css
.grid {
  gap: 24px;            /* Between grid items */
}

@media (max-width: 768px) {
  .grid {
    gap: 16px;          /* Tighter on mobile */
  }
}
```

---

## 🔧 IMPLEMENTATION

### CSS Variables

```css
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;  /* 4px */
  --spacing-2: 0.5rem;   /* 8px */
  --spacing-3: 0.75rem;  /* 12px */
  --spacing-4: 1rem;     /* 16px */
  --spacing-5: 1.25rem;  /* 20px */
  --spacing-6: 1.5rem;   /* 24px */
  --spacing-8: 2rem;     /* 32px */
  --spacing-10: 2.5rem;  /* 40px */
  --spacing-12: 3rem;    /* 48px */
  --spacing-16: 4rem;    /* 64px */
  --spacing-20: 5rem;    /* 80px */
  --spacing-24: 6rem;    /* 96px */
}

/* Usage */
.card {
  padding: var(--spacing-6);  /* 24px */
  gap: var(--spacing-4);      /* 16px */
}
```

### Tailwind (Built-in)

```html
<!-- Padding -->
<div class="p-4">      <!-- 16px padding all sides -->
<div class="px-6">     <!-- 24px padding horizontal -->
<div class="py-3">     <!-- 12px padding vertical -->

<!-- Margin -->
<div class="m-4">      <!-- 16px margin all sides -->
<div class="mb-6">     <!-- 24px margin bottom -->

<!-- Gap (flexbox/grid) -->
<div class="gap-4">    <!-- 16px gap -->
<div class="gap-x-6">  <!-- 24px horizontal gap -->
```

---

## ⚖️ CONSISTENCY RULES

### Do's

- ✅ Use spacing scale values only (4, 8, 16, 24...)
- ✅ Consistent spacing = visual harmony
- ✅ Larger spacing = more emphasis
- ✅ Group related items (small spacing)
- ✅ Separate sections (large spacing)

### Don'ts

- ❌ Don't use arbitrary values (13px, 17px, 23px)
- ❌ Don't mix too many spacing values
- ❌ Don't use spacing for alignment (use flexbox/grid)
- ❌ Don't forget responsive spacing

---

## 🎨 VISUAL EXAMPLES

### Spacing Hierarchy

```
Large Section Spacing (48px)
├─ Content Block
│  ├─ Heading
│  ├─ Medium Spacing (24px)
│  ├─ Paragraph
│  ├─ Small Spacing (16px)
│  └─ Button Group
│     ├─ Button
│     ├─ Tiny Spacing (8px)
│     └─ Button
└─ Large Section Spacing (48px)
```

### Card Example

```
Card Container (padding: 24px)
├─ Header
├─ 16px spacing
├─ Content
│  ├─ Label
│  ├─ 8px spacing
│  └─ Value
├─ 24px spacing
└─ Footer (buttons with 8px gap)
```

---

## 📊 DESIGN TOKENS

See [design-tokens.json](../resources/design-tokens.json) for spacing tokens.

---

## 🔄 WHEN TO UPDATE

Update spacing when:
- Layout feels cramped or too loose
- Adding new component sizes
- Responsive adjustments needed
- Consistency issues found

**Process:**
1. Identify spacing issue
2. Update scale if needed
3. Update this file
4. Update design-tokens.json
5. Test responsive behavior
6. Update changelog

---

## ✅ CHECKLIST

- [ ] Using 4px base unit
- [ ] Spacing scale is consistent
- [ ] Responsive spacing tested
- [ ] No arbitrary values in code
- [ ] Design tokens match Figma
- [ ] Components use spacing scale

---

**Consistent spacing = Visual harmony.** 📐

