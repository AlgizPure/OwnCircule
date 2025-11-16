# ICONOGRAPHY

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## 🎨 ICON LIBRARY

**Recommended:** [Choose during bootstrap]

**Popular options:**
- **Heroicons** (Tailwind) - clean, modern, 2 styles
- **Material Icons** (Google) - comprehensive, familiar
- **Lucide** (Feather fork) - minimal, consistent
- **Phosphor** - flexible, 6 weights
- **Tabler Icons** - stroke-based, crisp

**Decision criteria:**
- Style matches design system
- Comprehensive coverage
- License (open-source)
- Format (SVG preferred)
- Maintenance (actively updated)

---

## 📏 ICON SIZES

```yaml
Micro:
  Size: 12px (0.75rem)
  Usage: Inline with caption text, tiny badges
  
Small:
  Size: 16px (1rem)
  Usage: Inline with body text, buttons, inputs
  
Medium (Default):
  Size: 20px (1.25rem)
  Usage: Navigation, toolbar, standalone icons
  
Large:
  Size: 24px (1.5rem)
  Usage: Headers, important actions, large buttons
  
Extra Large:
  Size: 32px (2rem)
  Usage: Feature icons, empty states
  
Huge:
  Size: 48px (3rem)
  Usage: Hero sections, illustrations
```

**Rule:** Icon size should match adjacent text size.

---

## 🎯 USAGE GUIDELINES

### Icon + Text

```html
<!-- Button with icon -->
<button>
  <icon size="16px" />
  <span>Button Text (16px)</span>
</button>

<!-- Icon matches text size -->
```

**Alignment:**
- Center align icon with text
- Use `gap: 8px` between icon and text

---

### Standalone Icons

```html
<!-- Icon button (no text) -->
<button aria-label="Close">
  <icon size="20px" />
</button>
```

**CRITICAL:** Always provide `aria-label` for standalone icons!

---

### Icon in Input

```html
<div class="input-wrapper">
  <icon size="16px" /> <!-- Matches input text -->
  <input type="text" placeholder="Search..." />
</div>
```

---

## 🎨 ICON STYLES

### Stroke vs Fill

**Stroke (Outline):**
- Light, minimal, modern
- Better for small sizes
- Consistent weight

**Fill (Solid):**
- Strong, bold, emphasis
- Better for large sizes
- More visual weight

**Recommendation:** Choose ONE style for consistency.

**Exception:** Use filled icons for active/selected states.

---

### Icon Weight

If using weighted icons (Phosphor, SF Symbols):

```yaml
Thin: Use for large decorative icons
Light: Use for subtle, secondary icons
Regular: Default weight (most common)
Bold: Use for emphasis, selected states
```

---

## 🎨 ICON COLORS

### Default States

```yaml
Primary Icons:
  Color: gray-900 (on light bg)
  Usage: Main navigation, important actions

Secondary Icons:
  Color: gray-500
  Usage: Secondary actions, metadata icons

Disabled Icons:
  Color: gray-400
  Usage: Disabled buttons, inactive states

On Primary:
  Color: white
  Usage: Icons on primary-colored backgrounds
```

### Interactive States

```yaml
Hover:
  Color: primary-600
  Usage: Icon buttons on hover

Active/Selected:
  Color: primary-500
  Usage: Active navigation item, selected state

Danger:
  Color: error-500
  Usage: Delete, remove actions
```

---

## 🔧 IMPLEMENTATION

### SVG Icons (Inline)

```html
<svg width="20" height="20" fill="currentColor">
  <path d="..." />
</svg>
```

**Use `currentColor`** - inherits text color!

---

### Icon Component (React Example)

```jsx
const Icon = ({ name, size = 20, color = 'currentColor' }) => {
  return (
    <svg 
      width={size} 
      height={size} 
      fill={color}
      aria-hidden="true"
    >
      <use href={`#icon-${name}`} />
    </svg>
  );
};

// Usage
<Icon name="search" size={16} />
```

---

### CSS Variables

```css
:root {
  --icon-size-sm: 16px;
  --icon-size-md: 20px;
  --icon-size-lg: 24px;
  
  --icon-color-primary: var(--gray-900);
  --icon-color-secondary: var(--gray-500);
  --icon-color-disabled: var(--gray-400);
}

.icon {
  width: var(--icon-size-md);
  height: var(--icon-size-md);
  color: var(--icon-color-primary);
}
```

---

## ⚖️ BEST PRACTICES

**Do's:**
- ✅ Consistent icon library (don't mix)
- ✅ Match icon size to text size
- ✅ Use `aria-label` for standalone icons
- ✅ Use `currentColor` for flexibility
- ✅ Optimize SVGs (remove extra attributes)

**Don'ts:**
- ❌ Don't mix icon styles (stroke + fill)
- ❌ Don't use icons without context
- ❌ Don't scale icons beyond intended sizes
- ❌ Don't forget accessibility labels

---

## ♿ ACCESSIBILITY

### Decorative Icons

```html
<!-- Icon is decorative (text provides context) -->
<button>
  <icon aria-hidden="true" />
  <span>Save</span>
</button>
```

Use `aria-hidden="true"` when text is present.

---

### Functional Icons

```html
<!-- Icon is functional (no text) -->
<button aria-label="Close modal">
  <icon />
</button>
```

Always provide `aria-label` or `aria-labelledby`.

---

### Icon Buttons

```html
<!-- Good: accessible -->
<button aria-label="Settings">
  <icon name="settings" />
</button>

<!-- Bad: screen reader can't understand -->
<button>
  <icon name="settings" />
</button>
```

---

## 📝 COMMON PATTERNS

### Navigation

```html
<nav>
  <a href="/dashboard" aria-label="Dashboard">
    <icon name="home" size="20" />
    <span>Dashboard</span>
  </a>
</nav>
```

---

### Input with Icon

```html
<div class="input-wrapper">
  <icon name="search" size="16" aria-hidden="true" />
  <input type="text" placeholder="Search..." />
</div>
```

---

### Status Icons

```html
<!-- Success -->
<div class="status-success">
  <icon name="check" color="success-500" />
  <span>Completed</span>
</div>

<!-- Error -->
<div class="status-error">
  <icon name="x" color="error-500" />
  <span>Failed</span>
</div>
```

---

## 📦 ICON SET

**To be populated during bootstrap:**

```yaml
Common Icons Needed:
  - Navigation: home, settings, user, menu, search
  - Actions: edit, delete, save, add, close
  - Status: check, x, alert, info
  - Arrows: arrow-left, arrow-right, chevron-down
  - Media: play, pause, volume
  - UI: eye, eye-off, copy, download, upload
```

---

## 🔄 WHEN TO UPDATE

Update iconography when:
- Adding new features (new icons needed)
- Consistency issues (mixing styles)
- Accessibility gaps found
- Switching icon libraries

---

**Icons communicate instantly. Use them wisely.** 🎨

