# BUTTON

**Component:** Button  
**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be customized during bootstrap

---

## 📋 OVERVIEW

Buttons trigger actions and events.

**Purpose:**
- Primary actions (save, submit, confirm)
- Secondary actions (cancel, back)
- Navigation (next, previous)

**Key principle:** Button должна четко communicat что произойдет при клике.

---

## 🏗️ ANATOMY

```
┌─────────────────────────┐
│  [Icon]  Label  [Icon]  │  ← Button (clickable area)
└─────────────────────────┘
   ↑       ↑        ↑
  Leading  Text   Trailing
  Icon             Icon
```

**Elements:**
1. **Container** - background, border, padding
2. **Label** - text content (required)
3. **Icon** (optional) - leading or trailing
4. **Loading indicator** (state) - replaces content when loading

---

## 🎨 VARIANTS

### 1. Primary (Filled)

**Purpose:** Main call-to-action

**Visual:**
- Background: `primary-500`
- Text: `white`
- Border: none
- Hover: `primary-600`

**Usage:**
- Save, Submit, Create, Confirm
- ONE primary button per screen/section
- Most important action

```html
<button class="btn-primary">
  Save Changes
</button>
```

---

### 2. Secondary (Outlined)

**Purpose:** Secondary actions

**Visual:**
- Background: transparent
- Text: `primary-500`
- Border: `1px solid primary-500`
- Hover: `background: primary-50`

**Usage:**
- Cancel, Back, Skip
- Less emphasis than primary
- Alternative actions

```html
<button class="btn-secondary">
  Cancel
</button>
```

---

### 3. Ghost (Text Only)

**Purpose:** Tertiary actions, minimal emphasis

**Visual:**
- Background: transparent
- Text: `gray-700`
- Border: none
- Hover: `background: gray-100`

**Usage:**
- Learn more, View details
- Least visual weight
- Non-critical actions

```html
<button class="btn-ghost">
  Learn More
</button>
```

---

### 4. Destructive (Danger)

**Purpose:** Destructive actions

**Visual:**
- Background: `error-500`
- Text: `white`
- Border: none
- Hover: `error-600`

**Usage:**
- Delete, Remove, Discard
- Always require confirmation
- Use sparingly

```html
<button class="btn-destructive">
  Delete Account
</button>
```

---

## 📏 SIZES

### Small

```yaml
Height: 32px
Padding: 8px 16px
Font size: 14px
Icon size: 16px
Gap: 8px
```

**Usage:** Compact UIs, tables, cards

---

### Medium (Default)

```yaml
Height: 40px
Padding: 12px 24px
Font size: 16px
Icon size: 20px
Gap: 8px
```

**Usage:** Most common size, forms, modals

---

### Large

```yaml
Height: 48px
Padding: 16px 32px
Font size: 18px
Icon size: 24px
Gap: 8px
```

**Usage:** Hero CTAs, marketing pages, high emphasis

---

## 🎭 STATES

### Default (Rest)

Normal appearance, ready for interaction.

---

### Hover

```yaml
Primary: background → primary-600
Secondary: background → primary-50
Ghost: background → gray-100
Destructive: background → error-600

Cursor: pointer
Transition: 100ms ease-out
```

---

### Active (Pressed)

```yaml
Transform: translateY(1px)
Opacity: 0.9
Duration: 100ms
```

Provides tactile feedback.

---

### Focus

```yaml
Outline: 2px solid primary-500
Outline offset: 2px
```

**CRITICAL for accessibility!**

---

### Disabled

```yaml
Background: gray-200
Text: gray-400
Cursor: not-allowed
Opacity: 0.6
```

**Never use disabled for unavailable actions** - hide instead or explain why disabled.

---

### Loading

```yaml
Cursor: wait
Content: Hidden (or semi-transparent)
Spinner: Visible (center or replace icon)
```

```html
<button class="btn-primary loading">
  <spinner /> Loading...
</button>
```

---

## 🎯 USAGE GUIDELINES

### Button Hierarchy

**One screen should have:**
- ✅ 1 Primary button (main action)
- ✅ 0-2 Secondary buttons (alternatives)
- ✅ 0-3 Ghost buttons (tertiary)

**Example (Form):**
```
[Save Changes]  ← Primary
[Cancel]        ← Secondary
```

**Example (Modal):**
```
[Delete]  [Cancel]  ← Destructive + Secondary
```

---

### Button Labels

**Do's:**
- ✅ Clear action verbs: "Save", "Delete", "Create"
- ✅ Specific: "Save Changes" not "OK"
- ✅ Short: 1-3 words
- ✅ Sentence case: "Save changes" not "SAVE CHANGES"

**Don'ts:**
- ❌ Generic: "Submit", "OK", "Yes"
- ❌ Ambiguous: "Continue" (continue what?)
- ❌ Too long: "Click here to save your changes"
- ❌ ALL CAPS (unless brand)

---

### Button Icons

**When to add:**
- ✅ Adds clarity (Save → Save icon)
- ✅ Common actions (Search, Download, Delete)
- ✅ Recognizable icon

**When NOT to add:**
- ❌ Decorative only
- ❌ Unclear icon (confuses more than helps)
- ❌ Every button (too busy)

**Placement:**
- Leading: Action type (Save, Download)
- Trailing: Direction (Next →, External ↗)

---

### Button Groups

**Horizontal:**
```
[Secondary] [Primary]
```
- Primary на RIGHT (reading direction)
- Secondary на LEFT
- Gap: 12px

**Vertical (mobile):**
```
[Primary]      ← Full width, top
[Secondary]    ← Full width, bottom
```
- Primary сверху
- Gap: 12px

---

## ♿ ACCESSIBILITY

### Keyboard

```yaml
Tab: Focus button
Enter/Space: Activate button
Escape: Cancel (if in modal)
```

**Always ensure keyboard accessible!**

---

### Screen Readers

```html
<!-- Good: descriptive -->
<button aria-label="Delete user profile">
  <icon name="trash" />
</button>

<!-- Bad: no context -->
<button>
  <icon name="trash" />
</button>
```

**Icon-only buttons MUST have aria-label!**

---

### Focus Visible

```css
.button:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}
```

**Never remove focus outline without alternative!**

---

### Disabled State

```html
<!-- Better: explain why disabled -->
<button disabled aria-label="Save (fill required fields first)">
  Save
</button>

<!-- Even better: don't disable, show error on click -->
<button onclick="showValidationErrors()">
  Save
</button>
```

**Prefer validation errors over disabled buttons.**

---

## 🔧 IMPLEMENTATION

### CSS

```css
/* Primary Button */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  
  height: 40px;
  padding: 12px 24px;
  
  background: var(--primary-500);
  color: white;
  border: none;
  border-radius: 6px;
  
  font-size: 16px;
  font-weight: 600;
  line-height: 1;
  text-align: center;
  
  cursor: pointer;
  transition: all 100ms ease-out;
}

.btn-primary:hover {
  background: var(--primary-600);
}

.btn-primary:active {
  transform: translateY(1px);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

.btn-primary:disabled {
  background: var(--gray-200);
  color: var(--gray-400);
  cursor: not-allowed;
  opacity: 0.6;
}
```

---

### React Component

```jsx
const Button = ({ 
  children, 
  variant = 'primary',
  size = 'medium',
  icon,
  iconPosition = 'leading',
  loading = false,
  disabled = false,
  onClick,
  ...props 
}) => {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      disabled={disabled || loading}
      onClick={onClick}
      {...props}
    >
      {loading && <Spinner />}
      {!loading && icon && iconPosition === 'leading' && <Icon name={icon} />}
      {!loading && children}
      {!loading && icon && iconPosition === 'trailing' && <Icon name={icon} />}
    </button>
  );
};

// Usage
<Button variant="primary" size="medium" icon="save">
  Save Changes
</Button>
```

---

## 📝 EXAMPLES

### Form Actions

```html
<div class="form-actions">
  <button class="btn-secondary">Cancel</button>
  <button class="btn-primary">Save Changes</button>
</div>
```

---

### Modal Actions

```html
<div class="modal-actions">
  <button class="btn-secondary">Cancel</button>
  <button class="btn-destructive">Delete</button>
</div>
```

---

### Button with Icon

```html
<button class="btn-primary">
  <icon name="download" />
  Download Report
</button>
```

---

### Loading State

```html
<button class="btn-primary loading">
  <spinner />
  Saving...
</button>
```

---

### Icon Button

```html
<button class="btn-ghost" aria-label="Close">
  <icon name="x" />
</button>
```

---

## ⚠️ COMMON MISTAKES

**❌ Too many primary buttons:**
```html
<button class="btn-primary">Save</button>
<button class="btn-primary">Submit</button>  ← Which one is main?
<button class="btn-primary">Apply</button>
```

**✅ Clear hierarchy:**
```html
<button class="btn-primary">Save</button>     ← Main action
<button class="btn-secondary">Cancel</button> ← Alternative
```

---

**❌ Generic labels:**
```html
<button>OK</button>     ← OK to what?
<button>Submit</button> ← Submit what?
```

**✅ Specific labels:**
```html
<button>Save Changes</button>
<button>Create Account</button>
```

---

**❌ No focus indicator:**
```css
button:focus { outline: none; } /* Never do this! */
```

**✅ Visible focus:**
```css
button:focus-visible {
  outline: 2px solid var(--primary-500);
}
```

---

## ✅ CHECKLIST

Before using button:

- [ ] Label is clear and specific
- [ ] Correct variant (primary/secondary/ghost/destructive)
- [ ] Correct size for context
- [ ] Focus indicator visible
- [ ] Icon (if present) adds clarity
- [ ] Aria-label for icon-only buttons
- [ ] Loading state implemented (if async action)
- [ ] Disabled state justified (or avoided)

---

## 🔗 RELATED

- [Form Component](form.md) - Button in forms
- [Modal Component](modal.md) - Button in modals
- [Voice & Tone](../content/voice-and-tone.md) - Button labeling

---

**Buttons are the most common interaction. Get them right.** 🔘

