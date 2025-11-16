# INPUT

**Component:** Input  
**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template

---

## 📋 OVERVIEW

Text input fields allow users to enter text data.

**Types:**
- Text (default)
- Email, Password, Number, Tel, URL
- Textarea (multi-line)
- Search

---

## 🏗️ ANATOMY

```
Label *                    ← Label (required = *)
┌──────────────────────────┐
│ [Icon] Placeholder text  │  ← Input field
└──────────────────────────┘
Helper text or error       ← Helper/Error message
```

**Elements:**
1. **Label** - describes input (required)
2. **Input field** - text entry area
3. **Placeholder** - hint text (optional)
4. **Icon** - leading or trailing (optional)
5. **Helper text** - guidance or error

---

## 🎨 VARIANTS

### Text Input (Default)

```html
<div class="input-group">
  <label for="name">Full Name *</label>
  <input 
    id="name" 
    type="text" 
    placeholder="Enter your name"
    required
  />
  <span class="helper-text">As it appears on your ID</span>
</div>
```

---

### Email Input

```html
<input 
  type="email" 
  placeholder="name@example.com"
  autocomplete="email"
/>
```

**Includes:** Email validation, keyboard type on mobile

---

### Password Input

```html
<div class="input-wrapper">
  <input 
    type="password" 
    placeholder="••••••••"
  />
  <button type="button" aria-label="Show password">
    <icon name="eye" />
  </button>
</div>
```

**Features:**
- Toggle visibility (eye icon)
- Password strength indicator (if needed)
- Autocomplete="current-password"

---

### Number Input

```html
<input 
  type="number" 
  min="0" 
  max="100"
  step="1"
/>
```

---

### Search Input

```html
<div class="search-input">
  <icon name="search" />
  <input 
    type="search" 
    placeholder="Search..."
  />
</div>
```

---

### Textarea

```html
<textarea 
  rows="4"
  placeholder="Enter description..."
></textarea>
```

**For:** Multi-line text, descriptions, comments

---

## 📏 SIZES

### Small

```yaml
Height: 32px
Padding: 8px 12px
Font size: 14px
```

---

### Medium (Default)

```yaml
Height: 40px
Padding: 12px 16px
Font size: 16px
```

---

### Large

```yaml
Height: 48px
Padding: 16px 20px
Font size: 18px
```

---

## 🎭 STATES

### Default

```yaml
Background: white
Border: 1px solid gray-300
Text: gray-900
Placeholder: gray-400
```

---

### Focus

```yaml
Border: 2px solid primary-500
Box-shadow: 0 0 0 3px primary-50
```

**CRITICAL for accessibility!**

---

### Error

```yaml
Border: 2px solid error-500
Background: error-50
Icon: error icon (trailing)
Message: Error text below (error-600)
```

```html
<div class="input-group error">
  <label for="email">Email *</label>
  <input 
    id="email" 
    type="email"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <span id="email-error" class="error-text">
    Please enter a valid email
  </span>
</div>
```

---

### Success

```yaml
Border: 1px solid success-500
Icon: check icon (trailing)
Message: Success text (success-600)
```

---

### Disabled

```yaml
Background: gray-100
Border: gray-200
Text: gray-400
Cursor: not-allowed
```

**Avoid if possible** - explain instead.

---

## 🎯 USAGE GUIDELINES

### Labels

**Do's:**
- ✅ Always include label
- ✅ Clear and concise
- ✅ Sentence case
- ✅ Mark required fields (*)

**Don'ts:**
- ❌ No label (placeholder is NOT label)
- ❌ Vague labels ("Input")
- ❌ ALL CAPS

```html
<!-- Good -->
<label for="email">Email Address *</label>

<!-- Bad -->
<input placeholder="Email" /> <!-- No label! -->
```

---

### Placeholders

**Use for:**
- ✅ Format examples ("name@example.com")
- ✅ Hints ("Search by name or ID")

**Don't use for:**
- ❌ Primary instructions (use label + helper)
- ❌ Required info

---

### Helper Text

```html
<span class="helper-text">
  We'll never share your email
</span>
```

**When to use:**
- Format requirements ("Use 8+ characters")
- Privacy notes ("We'll never share...")
- Examples

---

### Validation

**Real-time validation:**
- ✅ After user leaves field (onBlur)
- ✅ On submit
- ❌ NOT while typing (annoying)

**Error messages:**
- Specific ("Email must include @")
- Helpful ("Use format: name@example.com")
- NOT generic ("Invalid input")

---

## ♿ ACCESSIBILITY

### Label Association

```html
<!-- Correct -->
<label for="email">Email</label>
<input id="email" type="email" />

<!-- Also correct -->
<label>
  Email
  <input type="email" />
</label>
```

---

### Required Fields

```html
<input 
  required
  aria-required="true"
/>
```

---

### Error States

```html
<input 
  aria-invalid="true"
  aria-describedby="error-message"
/>
<span id="error-message">Error text</span>
```

---

### Autocomplete

```html
<input 
  type="email"
  autocomplete="email"
/>
```

**Helps:** Autofill, password managers

---

## 🔧 IMPLEMENTATION

### CSS

```css
.input {
  width: 100%;
  height: 40px;
  padding: 12px 16px;
  
  background: white;
  border: 1px solid var(--gray-300);
  border-radius: 6px;
  
  font-size: 16px;
  color: var(--gray-900);
  
  transition: all 200ms ease-out;
}

.input::placeholder {
  color: var(--gray-400);
}

.input:focus {
  outline: none;
  border: 2px solid var(--primary-500);
  box-shadow: 0 0 0 3px var(--primary-50);
}

.input.error {
  border-color: var(--error-500);
  background: var(--error-50);
}

.input:disabled {
  background: var(--gray-100);
  border-color: var(--gray-200);
  color: var(--gray-400);
  cursor: not-allowed;
}
```

---

### React Component

```jsx
const Input = ({
  label,
  type = 'text',
  placeholder,
  helperText,
  error,
  icon,
  required,
  ...props
}) => {
  return (
    <div className="input-group">
      <label>
        {label} {required && '*'}
      </label>
      <div className="input-wrapper">
        {icon && <Icon name={icon} />}
        <input
          type={type}
          placeholder={placeholder}
          aria-invalid={!!error}
          required={required}
          {...props}
        />
      </div>
      {error && <span className="error-text">{error}</span>}
      {!error && helperText && <span className="helper-text">{helperText}</span>}
    </div>
  );
};
```

---

## ✅ CHECKLIST

- [ ] Label present and associated
- [ ] Required indicator if needed (*)
- [ ] Appropriate input type
- [ ] Placeholder helpful (format/example)
- [ ] Helper text for guidance
- [ ] Error messages specific
- [ ] Focus state visible
- [ ] Autocomplete attribute
- [ ] Keyboard accessible

---

**Inputs are critical to forms. Make them easy.** ⌨️

