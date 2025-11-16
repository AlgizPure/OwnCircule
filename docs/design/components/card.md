# CARD

**Component:** Card  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Cards are containers for related content and actions.

---

## 🏗️ ANATOMY

```
┌─────────────────────────┐
│ Header                  │  ← Optional header
├─────────────────────────┤
│                         │
│ Content                 │  ← Main content
│                         │
├─────────────────────────┤
│ Footer / Actions        │  ← Optional footer
└─────────────────────────┘
```

---

## 🎨 VARIANTS

### Basic Card

```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content here...</p>
</div>
```

**Visual:**
- Background: white
- Border: 1px solid gray-200
- Border radius: 8px
- Padding: 24px
- Shadow: level 1

---

### Card with Header

```html
<div class="card">
  <div class="card-header">
    <h3>Title</h3>
    <button class="icon-btn">⋯</button>
  </div>
  <div class="card-content">
    Content here...
  </div>
</div>
```

---

### Card with Footer

```html
<div class="card">
  <div class="card-content">
    Content...
  </div>
  <div class="card-footer">
    <button class="btn-secondary">Cancel</button>
    <button class="btn-primary">Save</button>
  </div>
</div>
```

---

### Interactive Card

```html
<div class="card interactive" onclick="navigate()">
  <h3>Clickable Card</h3>
  <p>Entire card is clickable</p>
</div>
```

**Hover:**
- Shadow: level 2
- Transform: translateY(-2px)
- Cursor: pointer

---

## 📏 SPACING

```yaml
Padding: 24px (default)
Gap (internal): 16px
Margin (between cards): 16px
```

---

## 🎯 USAGE

**Do's:**
- ✅ Group related content
- ✅ Consistent padding (24px)
- ✅ Clear hierarchy (header → content → footer)

**Don'ts:**
- ❌ Too much content (overwhelming)
- ❌ Nested cards (confusing)
- ❌ Clickable card + clickable elements (conflict)

---

## 🔧 CSS

```css
.card {
  background: white;
  border: 1px solid var(--gray-200);
  border-radius: 8px;
  padding: 24px;
  box-shadow: var(--shadow-1);
}

.card.interactive:hover {
  box-shadow: var(--shadow-2);
  transform: translateY(-2px);
  cursor: pointer;
}
```

---

**Cards organize content visually.** 🃏

