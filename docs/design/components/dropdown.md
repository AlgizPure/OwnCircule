# DROPDOWN

**Component:** Dropdown (Select)  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Dropdowns allow users to select one option from a list.

---

## 🎨 VARIANTS

### Select Dropdown

```html
<div class="select-wrapper">
  <label for="country">Country</label>
  <select id="country">
    <option value="">Select country</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="ca">Canada</option>
  </select>
</div>
```

---

### Custom Dropdown

```html
<div class="dropdown">
  <button class="dropdown-trigger">
    Select Option
    <icon name="chevron-down" />
  </button>
  <div class="dropdown-menu">
    <button class="dropdown-item">Option 1</button>
    <button class="dropdown-item">Option 2</button>
    <button class="dropdown-item">Option 3</button>
  </div>
</div>
```

---

### Multi-Select

```html
<div class="multiselect">
  <div class="selected-items">
    <span class="tag">Option 1 <button>×</button></span>
    <span class="tag">Option 2 <button>×</button></span>
  </div>
  <button class="dropdown-trigger">Add more...</button>
  <div class="dropdown-menu">
    <label><input type="checkbox" /> Option 3</label>
    <label><input type="checkbox" /> Option 4</label>
  </div>
</div>
```

---

### Search Dropdown

```html
<div class="dropdown">
  <input 
    type="text" 
    placeholder="Search..."
    class="dropdown-search"
  />
  <div class="dropdown-menu">
    <!-- Filtered results -->
  </div>
</div>
```

---

## 🎭 STATES

### Closed (Default)

```yaml
Trigger: Normal button appearance
Menu: Hidden
Icon: Chevron down
```

---

### Open

```yaml
Trigger: Active appearance
Menu: Visible (below trigger)
Icon: Chevron up
Focus: First menu item
```

---

### Selected

```yaml
Trigger text: Shows selected value
Item: Check icon or highlight
```

---

## 🎯 BEHAVIOR

### Opening

```yaml
Click trigger → Open menu
Focus first item
Arrow keys navigate
```

---

### Selecting

```yaml
Click item → Select
Close menu
Update trigger text
Emit change event
```

---

### Closing

```yaml
Click outside → Close
Escape key → Close
Select item → Close (single-select)
```

---

## ♿ ACCESSIBILITY

### Native Select

```html
<label for="option">Choose option</label>
<select id="option">
  <option>Option 1</option>
</select>
```

**Preferred:** Native select is accessible by default!

---

### Custom Dropdown

```html
<button 
  aria-haspopup="listbox"
  aria-expanded="false"
>
  Select
</button>
<ul role="listbox">
  <li role="option">Option 1</li>
</ul>
```

**Required:**
- Keyboard navigation (Arrow keys, Enter, Escape)
- ARIA roles
- Focus management

---

## 🎯 USAGE

**When to use:**
- ✅ 5+ options (below 5 → radio buttons)
- ✅ Single selection
- ✅ Space constrained

**When NOT to use:**
- ❌ < 5 options (use radio buttons)
- ❌ Critical info (dropdowns hide options)

---

## 🔧 CSS

```css
.dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  margin-top: 4px;
  
  background: white;
  border: 1px solid var(--gray-200);
  border-radius: 6px;
  box-shadow: var(--shadow-2);
  
  max-height: 300px;
  overflow-y: auto;
  
  z-index: var(--z-elevated);
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: 12px 16px;
  text-align: left;
  border: none;
  background: white;
}

.dropdown-item:hover {
  background: var(--gray-100);
}
```

---

**Dropdowns save space. Use wisely.** ▼

