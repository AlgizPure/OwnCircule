# MODAL

**Component:** Modal (Dialog)  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Modals are overlay windows that require user interaction before returning to main content.

**Use sparingly!** Modals interrupt workflow.

---

## 🏗️ ANATOMY

```
━━━━━━━━━━━━━━━━━━━━━━━━━━  ← Backdrop (overlay)
┃  ┌─────────────────────┐
┃  │ Title          [X]  │  ← Header
┃  ├─────────────────────┤
┃  │                     │
┃  │ Content             │  ← Body
┃  │                     │
┃  ├─────────────────────┤
┃  │ [Cancel]  [Confirm] │  ← Footer
┃  └─────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Elements:**
1. **Backdrop** - semi-transparent overlay
2. **Modal container** - white box
3. **Header** - title + close button
4. **Body** - content
5. **Footer** - actions (optional)

---

## 🎨 VARIANTS

### Standard Modal

```html
<div class="modal-backdrop">
  <div class="modal">
    <div class="modal-header">
      <h2>Modal Title</h2>
      <button class="close-btn" aria-label="Close">×</button>
    </div>
    <div class="modal-body">
      Content here...
    </div>
    <div class="modal-footer">
      <button class="btn-secondary">Cancel</button>
      <button class="btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

---

### Confirmation Modal

```html
<div class="modal modal-sm">
  <h2>Delete Account?</h2>
  <p>This action cannot be undone.</p>
  <div class="modal-footer">
    <button class="btn-secondary">Cancel</button>
    <button class="btn-destructive">Delete</button>
  </div>
</div>
```

---

### Form Modal

```html
<div class="modal">
  <h2>Create New Project</h2>
  <form>
    <input type="text" placeholder="Project name" />
    <textarea placeholder="Description"></textarea>
    <div class="modal-footer">
      <button type="button" class="btn-secondary">Cancel</button>
      <button type="submit" class="btn-primary">Create</button>
    </div>
  </form>
</div>
```

---

## 📏 SIZES

### Small

```yaml
Width: 400px
Usage: Confirmations, alerts
```

---

### Medium (Default)

```yaml
Width: 600px
Usage: Forms, standard content
```

---

### Large

```yaml
Width: 800px
Usage: Complex forms, rich content
```

---

### Full Screen

```yaml
Width: 90vw
Height: 90vh
Usage: Rich editors, complex workflows
```

---

## 🎯 BEHAVIOR

### Opening

```yaml
Animation: Scale in + fade in (300ms)
Focus: First focusable element
Scroll: Body scroll locked
```

---

### Closing

**Can close via:**
- Close button (X)
- Cancel button
- Escape key
- Click backdrop (optional)

```yaml
Animation: Scale out + fade out (200ms)
Focus: Return to trigger element
Scroll: Body scroll unlocked
```

---

## ♿ ACCESSIBILITY

### Focus Management

```html
<div 
  role="dialog" 
  aria-labelledby="modal-title"
  aria-modal="true"
>
  <h2 id="modal-title">Modal Title</h2>
  <!-- Content -->
</div>
```

**CRITICAL:**
- Focus trap (Tab loops within modal)
- Escape to close
- Return focus on close

---

### ARIA

```html
<div 
  role="dialog"
  aria-labelledby="title"
  aria-describedby="description"
  aria-modal="true"
>
  <h2 id="title">Title</h2>
  <p id="description">Description</p>
</div>
```

---

## 🎯 USAGE GUIDELINES

**When to use:**
- ✅ Critical decisions (delete, confirm)
- ✅ Urgent information (errors, warnings)
- ✅ Short forms (create, edit)
- ✅ Task completion required

**When NOT to use:**
- ❌ Non-critical info (use toast instead)
- ❌ Long forms (use dedicated page)
- ❌ Too frequent (annoying)
- ❌ Navigation (use page routing)

---

## 🔧 CSS

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: var(--z-floating);
}

.modal {
  background: white;
  border-radius: 12px;
  width: 600px;
  max-width: 90vw;
  max-height: 90vh;
  overflow: auto;
  box-shadow: var(--shadow-3);
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

---

**Modals interrupt. Use wisely.** 🪟

