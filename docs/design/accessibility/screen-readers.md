# SCREEN READERS

**Version:** 1.0

---

## 🔊 WHAT ARE SCREEN READERS?

Software that reads page content aloud for blind/low-vision users.

**Popular screen readers:**
- NVDA (Windows, free)
- JAWS (Windows, commercial)
- VoiceOver (macOS/iOS, built-in)
- TalkBack (Android, built-in)

---

## 🏗️ SEMANTIC HTML

**Screen readers rely on HTML structure:**

```html
✅ Good (semantic):
<button>Save</button>
<nav>...</nav>
<h1>Title</h1>
<main>...</main>

❌ Bad (non-semantic):
<div onclick="save()">Save</div>
<div class="nav">...</div>
<div class="title">Title</div>
<div class="main">...</div>
```

**Use semantic HTML first!**

---

## 🎯 ARIA (When Needed)

**ARIA = Accessible Rich Internet Applications**

### Rules

1. **Use semantic HTML first**
2. **ARIA only when HTML insufficient**
3. **Test with screen reader**

---

### Common ARIA Attributes

**aria-label:**
```html
<button aria-label="Close modal">
  <icon name="x" />
</button>
```

**aria-labelledby:**
```html
<div role="dialog" aria-labelledby="modal-title">
  <h2 id="modal-title">Delete Project</h2>
</div>
```

**aria-describedby:**
```html
<input 
  id="email"
  aria-describedby="email-hint"
/>
<span id="email-hint">We'll never share your email</span>
```

**aria-hidden:**
```html
<icon aria-hidden="true" />  ← Decorative only
<span>Save</span>             ← Screen reader reads this
```

**aria-live:**
```html
<div aria-live="polite" aria-atomic="true">
  Status updates appear here
</div>
```

---

## ✅ BEST PRACTICES

### 1. Alt Text

```html
✅ <img src="logo.png" alt="Company Name">
✅ <img src="chart.png" alt="Sales increased 20% in Q4">
❌ <img src="logo.png" alt="">  ← Missing context
```

---

### 2. Link Text

```html
✅ <a href="...">Read privacy policy</a>
❌ <a href="...">Click here</a>
❌ <a href="...">Learn more</a>
```

**Link text must make sense out of context**

---

### 3. Form Labels

```html
✅ <label for="email">Email</label>
   <input id="email">

❌ <input placeholder="Email">  ← Placeholder not label!
```

---

### 4. Heading Hierarchy

```html
✅ <h1>Page Title</h1>
   <h2>Section</h2>
   <h3>Subsection</h3>

❌ <h1>Page Title</h1>
   <h3>Section</h3>  ← Skipped h2!
```

---

## 🧪 TESTING

### VoiceOver (Mac)

**Enable:** Cmd + F5

**Navigate:**
- VO + Right Arrow: Next
- VO + Left Arrow: Previous
- VO + Space: Activate

---

### NVDA (Windows)

**Download:** nvaccess.org

**Navigate:**
- Down Arrow: Next
- Up Arrow: Previous
- Enter: Activate

---

## ✅ CHECKLIST

- [ ] Semantic HTML used
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Buttons have accessible names
- [ ] Heading hierarchy logical
- [ ] Links descriptive
- [ ] ARIA used correctly (sparingly)
- [ ] Tested with screen reader

---

**Screen readers reveal structure. Make it meaningful.** 🔊

