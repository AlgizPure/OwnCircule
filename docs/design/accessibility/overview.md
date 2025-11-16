# ACCESSIBILITY OVERVIEW

**Version:** 1.0

---

## ♿ WHAT IS ACCESSIBILITY?

Accessibility (a11y) = **usable by everyone**

Including people with:
- Visual disabilities (blind, low vision, color blind)
- Motor disabilities (keyboard-only, tremors)
- Auditory disabilities (deaf, hard of hearing)
- Cognitive disabilities (dyslexia, ADHD)

**Not edge cases. 15% of global population.**

---

## 🎯 WCAG 2.1 COMPLIANCE

**Web Content Accessibility Guidelines**

### Levels

**Level A:** Minimum (must have)  
**Level AA:** Recommended (our goal) ⭐  
**Level AAA:** Enhanced (nice to have)

**We target WCAG 2.1 AA compliance.**

---

## 📋 FOUR PRINCIPLES (POUR)

### 1. Perceivable

**Users can perceive content**

- ✅ Text alternatives for images
- ✅ Color contrast (4.5:1 minimum)
- ✅ Captions for videos
- ✅ Don't rely on color alone

---

### 2. Operable

**Users can operate interface**

- ✅ Keyboard accessible (all functions)
- ✅ Enough time to complete tasks
- ✅ No seizure-inducing flashing
- ✅ Easy navigation

---

### 3. Understandable

**Users can understand content**

- ✅ Readable text
- ✅ Predictable behavior
- ✅ Input assistance (validation, errors)
- ✅ Clear labels

---

### 4. Robust

**Works with assistive tech**

- ✅ Valid HTML
- ✅ ARIA labels
- ✅ Screen reader compatible
- ✅ Works across browsers/devices

---

## ✅ QUICK WINS

**Easy improvements, big impact:**

1. **Use semantic HTML**
```html
<button> not <div onclick>
<nav> not <div class="nav">
<h1>, <h2> in order
```

2. **Add alt text**
```html
<img src="logo.png" alt="Company Logo">
```

3. **Ensure keyboard access**
- Tab through page
- Enter/Space to activate
- Escape to close

4. **Check color contrast**
- Text: 4.5:1 minimum
- Use tools (Stark, WebAIM)

5. **Label everything**
```html
<label for="email">Email</label>
<input id="email">
```

---

## 🔧 TOOLS

**Testing:**
- axe DevTools (Chrome extension)
- WAVE (WebAIM)
- Lighthouse (Chrome)
- Screen reader (NVDA, VoiceOver)

**Design:**
- Stark (Figma plugin)
- Color Oracle (color blindness simulator)
- Contrast checker

---

## 📚 LEARN MORE

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)

---

**Accessibility is not optional. It's essential.** ♿

