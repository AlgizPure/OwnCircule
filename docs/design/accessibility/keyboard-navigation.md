# KEYBOARD NAVIGATION

**Version:** 1.0

---

## ⌨️ WHY KEYBOARD NAVIGATION?

**Users who rely on keyboard:**
- Motor disabilities
- Power users (faster)
- Blind users (with screen reader)

**All functionality must work with keyboard only.**

---

## 🔑 KEY INTERACTIONS

### Tab

**Navigate forward**
- Moves focus to next interactive element
- Order: Top → Bottom, Left → Right

```html
<button>First</button>
<button>Second</button>
<button>Third</button>
```

**Tab order:** First → Second → Third

---

### Shift + Tab

**Navigate backward**
- Moves to previous element

---

### Enter / Space

**Activate element**
- Enter: Buttons, links
- Space: Buttons, checkboxes

```html
<button>Click Me</button>  ← Enter or Space activates
```

---

### Escape

**Close or cancel**
- Close modals
- Dismiss tooltips
- Cancel operations

---

### Arrow Keys

**Navigate within component**
- Tabs: Left/Right arrows
- Dropdown: Up/Down arrows
- Sliders: Left/Right arrows

---

## ✅ REQUIREMENTS

### 1. All Interactive Elements Focusable

```html
✅ <button>Click</button>
✅ <a href="/">Link</a>
✅ <input type="text">

❌ <div onclick="...">Click</div>  ← Not focusable!
```

**Use semantic HTML!**

---

### 2. Visible Focus Indicator

```css
/* Good: Visible focus */
button:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

/* Bad: No focus */
button:focus {
  outline: none;  ← NEVER DO THIS!
}
```

**CRITICAL: Focus must be visible!**

---

### 3. Logical Tab Order

```html
<!-- Good: Natural order -->
<form>
  <input name="first">   ← Tab 1
  <input name="second">  ← Tab 2
  <button>Submit</button> ← Tab 3
</form>

<!-- Bad: Using tabindex -->
<div tabindex="3">...</div>  ← Don't manipulate order!
```

**Let natural DOM order dictate tab order.**

---

### 4. Focus Management

**Modal opens:**
```javascript
// Move focus to modal
modal.focus();

// Trap focus inside modal
trapFocus(modal);
```

**Modal closes:**
```javascript
// Return focus to trigger
trigger.focus();
```

---

### 5. Skip Links

```html
<a href="#main" class="skip-link">
  Skip to main content
</a>

<nav>...</nav>

<main id="main">
  Content...
</main>
```

**Helps keyboard users skip navigation**

---

## 🧪 TESTING

### Manual Test

1. **Hide your mouse**
2. **Tab through page**
   - Can you reach all interactive elements?
   - Is focus visible?
   - Is order logical?
3. **Try each interaction**
   - Enter/Space to activate
   - Escape to close
   - Arrows for navigation

---

### Common Issues

**❌ Can't reach element:**
- Not focusable (div instead of button)
- Display: none or visibility: hidden

**❌ Focus not visible:**
- outline: none without alternative
- Insufficient contrast

**❌ Focus trapped:**
- Modal without escape mechanism
- Can't Tab out

**❌ Wrong tab order:**
- CSS positioning (visual != DOM order)
- tabindex manipulation

---

## ✅ CHECKLIST

- [ ] All interactive elements focusable
- [ ] Focus indicator visible (2px, high contrast)
- [ ] Tab order logical (follows visual order)
- [ ] Enter/Space activates elements
- [ ] Escape closes modals/menus
- [ ] Focus management in modals
- [ ] Skip links for main content
- [ ] No keyboard traps

---

**If it works with mouse, it must work with keyboard.** ⌨️

