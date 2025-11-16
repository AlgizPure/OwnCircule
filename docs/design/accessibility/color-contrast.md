# COLOR CONTRAST

**Version:** 1.0

---

## 🎨 WHY CONTRAST MATTERS?

**Low contrast =** Hard to read for:
- Low vision users
- Color blind users
- Users in bright sunlight
- Older users
- Everyone!

**15% of population has vision impairment.**

---

## 📊 WCAG REQUIREMENTS

### Contrast Ratios

**Normal text (< 18px):**
- AA: **4.5:1** minimum ⭐
- AAA: 7:1

**Large text (≥18px or ≥14px bold):**
- AA: **3:1** minimum ⭐
- AAA: 4.5:1

**UI components (borders, icons):**
- **3:1** minimum

**We target AA compliance (4.5:1 for text).**

---

## ✅ TESTING COMBINATIONS

### Text on White

```
✅ Gray-900 on White: 18.2:1 (excellent)
✅ Gray-800 on White: 12.6:1 (excellent)
✅ Gray-700 on White: 8.9:1 (excellent)
✅ Gray-500 on White: 4.6:1 (pass AA)
⚠️ Gray-400 on White: 2.9:1 (fail - too light!)
```

**Use gray-500 or darker for text**

---

### Colors on White

```
✅ Primary-500 (#2196F3) on White: 4.8:1 (pass)
✅ Error-500 (#F44336) on White: 5.1:1 (pass)
⚠️ Warning-500 (#FF9800) on White: 2.1:1 (fail!)
```

**Use Warning-600+ for text on white**

---

### White on Colors

```
✅ White on Primary-500: 4.8:1 (pass)
✅ White on Primary-600: 5.6:1 (pass)
✅ White on Error-500: 5.1:1 (pass)
⚠️ White on Warning-500: 2.1:1 (fail!)
```

---

## 🔧 TOOLS

**Online:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Contrast Ratio](https://contrast-ratio.com/)

**Figma:**
- Stark plugin
- Contrast plugin

**Browser:**
- axe DevTools
- Lighthouse

---

## 🎯 BEST PRACTICES

### 1. Don't Rely on Color Alone

```
❌ Bad:
Required fields in red

✅ Good:
Required fields marked with * AND red
```

---

### 2. Test Color Blindness

**Types:**
- Protanopia (red-blind) - 1% men
- Deuteranopia (green-blind) - 1% men
- Tritanopia (blue-blind) - rare

**Tool:** Color Oracle (simulator)

---

### 3. Dark Mode

**Must also pass contrast:**
- Text on dark background: ≥4.5:1
- Use lighter text colors (gray-50, gray-100)

---

## ✅ CHECKLIST

- [ ] All text ≥ 4.5:1 contrast (< 18px)
- [ ] Large text ≥ 3:1 contrast (≥ 18px)
- [ ] UI components ≥ 3:1 contrast
- [ ] Don't rely on color alone for meaning
- [ ] Tested with contrast checker
- [ ] Color blindness tested

---

**Good contrast benefits everyone.** 🎨

