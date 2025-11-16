# FORM

**Component:** Form  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Forms collect user input through various input types.

---

## 🏗️ STRUCTURE

```html
<form>
  <div class="form-section">
    <h3>Personal Information</h3>
    
    <div class="form-field">
      <label for="name">Full Name *</label>
      <input id="name" type="text" required />
      <span class="helper-text">As appears on ID</span>
    </div>
    
    <div class="form-field">
      <label for="email">Email *</label>
      <input id="email" type="email" required />
    </div>
  </div>
  
  <div class="form-actions">
    <button type="button" class="btn-secondary">Cancel</button>
    <button type="submit" class="btn-primary">Save</button>
  </div>
</form>
```

---

## 🎯 BEST PRACTICES

### Layout

**Vertical (preferred):**
```
Label
[Input field]
Helper text

Label
[Input field]
```

**Better readability, faster completion**

---

### Required Fields

**Option 1: Mark required**
```
Full Name *
Email *
Phone (optional)
```

**Option 2: Mark optional**
```
Full Name
Email
Phone (optional)
```

**Choose ONE approach consistently**

---

### Validation

**When:**
- ✅ onBlur (after leaving field)
- ✅ onSubmit (before sending)
- ❌ NOT onChange (while typing - annoying!)

**Messages:**
- Specific: "Email must include @"
- Helpful: "Use format: name@example.com"
- Positioned: Below field (inline)

---

### Field Grouping

```html
<fieldset>
  <legend>Shipping Address</legend>
  <input name="street" />
  <input name="city" />
  <input name="zip" />
</fieldset>
```

**Groups related fields**

---

## 📏 SPACING

```yaml
Between fields: 24px
Between sections: 40px
Form padding: 24px
Label to input: 8px
Input to helper: 4px
```

---

## ♿ ACCESSIBILITY

### Labels

```html
<!-- Always associate label -->
<label for="email">Email</label>
<input id="email" type="email" />
```

---

### Required Fields

```html
<input required aria-required="true" />
```

---

### Error Messages

```html
<input 
  aria-invalid="true"
  aria-describedby="error-msg"
/>
<span id="error-msg">Error text</span>
```

---

### Autocomplete

```html
<input 
  type="email"
  autocomplete="email"
/>
```

**Helps:** Autofill, faster completion

---

## 🎯 USAGE

**Do's:**
- ✅ One column (vertical)
- ✅ Logical order
- ✅ Clear labels
- ✅ Helpful errors
- ✅ Progress indicator (multi-step)

**Don'ts:**
- ❌ Too many fields (split into steps)
- ❌ Unclear labels
- ❌ No validation feedback
- ❌ Disabled submit (show errors instead)

---

## 📱 RESPONSIVE

### Mobile

```css
.form-field {
  width: 100%;
}

.form-actions {
  flex-direction: column;
}

.form-actions button {
  width: 100%;
}
```

**Full-width fields and buttons**

---

**Forms collect data. Make them easy.** 📝

