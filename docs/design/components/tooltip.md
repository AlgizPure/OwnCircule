# TOOLTIP

**Component:** Tooltip  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Tooltips provide short contextual information on hover or focus.

**Use for:**
- Explaining icon buttons
- Providing additional context
- Showing keyboard shortcuts

**Don't use for:**
- Critical information (might be missed)
- Long text (use modal or help text)
- Mobile (no hover state)

---

## 🏗️ ANATOMY

```
           ┌─────────────┐
[Button]   │  Tooltip    │  ← Tooltip content
           │  text here  │
           └──────▼──────┘
              ↑
            Arrow (optional)
```

---

## 🎨 VARIANTS

### Basic Tooltip

```html
<button 
  data-tooltip="Save changes"
  aria-label="Save changes"
>
  <icon name="save" />
</button>
```

---

### With Arrow

```html
<div class="tooltip tooltip-top">
  This is a tooltip
  <div class="tooltip-arrow"></div>
</div>
```

---

## 📏 POSITIONING

### Top (Default)

```yaml
Position: Above element
Arrow: Points down
```

---

### Bottom

```yaml
Position: Below element
Arrow: Points up
```

---

### Left / Right

```yaml
Position: Side of element
Arrow: Points to element
```

**Auto-position:** Flip if would overflow viewport

---

## 🎭 BEHAVIOR

### Show

```yaml
Trigger: Hover or focus
Delay: 300ms (prevent flashing)
Animation: Fade in (200ms)
```

---

### Hide

```yaml
Trigger: Mouse leave or blur
Delay: 0ms (immediate)
Animation: Fade out (100ms)
```

---

## ♿ ACCESSIBILITY

### Don't Rely on Tooltips

**Critical info should be visible!**

```html
<!-- Bad: critical info in tooltip -->
<button data-tooltip="This will delete everything">
  Delete
</button>

<!-- Good: clear label -->
<button>Delete All Items</button>
```

---

### ARIA

```html
<button 
  aria-label="Save changes"
  aria-describedby="save-tooltip"
>
  <icon name="save" />
</button>
<div id="save-tooltip" role="tooltip">
  Save changes (Cmd+S)
</div>
```

---

### Keyboard

- Tooltip should appear on focus
- Escape key should dismiss
- Should work without mouse

---

## 🎯 USAGE

**Do's:**
- ✅ Brief (1-2 lines max)
- ✅ Supplement visible info
- ✅ Explain icon buttons
- ✅ Show keyboard shortcuts

**Don'ts:**
- ❌ Critical information
- ❌ Long paragraphs
- ❌ Required for understanding
- ❌ On mobile (no hover!)

---

## 🔧 CSS

```css
.tooltip {
  position: absolute;
  
  background: var(--gray-900);
  color: white;
  
  padding: 8px 12px;
  border-radius: 6px;
  
  font-size: 14px;
  white-space: nowrap;
  
  pointer-events: none;
  z-index: var(--z-floating);
  
  opacity: 0;
  transition: opacity 200ms ease-out;
}

.tooltip.show {
  opacity: 1;
}

.tooltip-arrow {
  position: absolute;
  width: 8px;
  height: 8px;
  background: var(--gray-900);
  transform: rotate(45deg);
}
```

---

## 📱 MOBILE CONSIDERATIONS

**Problem:** No hover on mobile!

**Solutions:**
- Don't rely on tooltips
- Use visible labels instead
- Show on long-press (if needed)
- Provide help section

---

## 💡 ALTERNATIVES

**Instead of tooltip, consider:**

**Help Icon + Modal:**
```html
<button aria-label="Help">
  <icon name="help" />
</button>
<!-- Opens modal with full explanation -->
```

**Helper Text (Always Visible):**
```html
<label>Password</label>
<input type="password" />
<span class="helper-text">
  Must be 8+ characters
</span>
```

**Disclosure Widget:**
```html
<details>
  <summary>Why do we need this?</summary>
  <p>Detailed explanation here...</p>
</details>
```

---

**Tooltips enhance. They don't replace.** 💬

