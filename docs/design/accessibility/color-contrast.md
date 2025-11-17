# COLOR CONTRAST
## Ensuring Text Readability for All Users

**Version:** 2.0
**Last Updated:** November 2025
**WCAG Criteria:** 1.4.3 Contrast (Minimum)
**Target:** 4.5:1 for normal text, 3:1 for large text

---

## 🎨 WHY CONTRAST MATTERS

**Low contrast = hard to read for:**
- Low vision users (20% of users over 50)
- Color blind users (8% of men, 0.5% of women)
- Users in bright sunlight (outdoor reading)
- Older users (presbyopia)
- Everyone on bad screens

**15% of population has vision impairment.**

---

## 📊 WCAG CONTRAST REQUIREMENTS

### Normal Text (< 18px)

```
✅ AA Level (our target): 4.5:1 minimum
✅ AAA Level (enhanced): 7:1
```

### Large Text (≥ 18px or ≥ 14px bold)

```
✅ AA Level (our target): 3:1 minimum
✅ AAA Level (enhanced): 4.5:1
```

### UI Components & Borders

```
✅ 3:1 minimum (icons, buttons, focus indicators)
```

---

## 🔍 TESTING CONTRAST

### Tools

**Online:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Most accurate
- [Contrast Ratio](https://contrast-ratio.com/) - Simple & visual

**Design:**
- Stark (Figma plugin)
- Figma accessibility panel

**Browser:**
- axe DevTools
- Chrome DevTools (Inspect > Accessibility > Contrast)

### How to Test

```
1. Get hex colors of text & background
2. Input into WebAIM checker
3. Check both AA and AAA
4. Document results
5. Use 4.5:1 minimum (AA)
```

---

## ✅ GOOD CONTRAST COMBINATIONS

### Dark Text on Light Backgrounds

```
✅ Gray-900 (#212121) on White: 19.6:1 (excellent)
✅ Gray-800 (#424242) on White: 12.6:1 (excellent)
✅ Gray-700 (#616161) on White: 8.9:1 (excellent)
✅ Gray-600 (#757575) on White: 6.2:1 (excellent)
✅ Gray-500 (#9E9E9E) on White: 4.6:1 (pass AA)
⚠️ Gray-400 (#BDBDBD) on White: 2.9:1 (fail)
```

**Recommendation:** Use Gray-600 or darker for text on white

### Light Text on Dark Backgrounds

```
✅ White (#FFFFFF) on Gray-900: 19.6:1 (excellent)
✅ Gray-100 (#F5F5F5) on Gray-900: 17.5:1 (excellent)
✅ Gray-50 (#FAFAFA) on Gray-900: 20.1:1 (excellent)
```

### Brand Colors on White

```
✅ Primary Blue (#2196F3) on White: 4.8:1 (pass)
✅ Error Red (#EF5350) on White: 5.1:1 (pass)
⚠️ Success Green (#66BB6A) on White: 3.2:1 (fail - too light)
⚠️ Warning Orange (#FFA726) on White: 2.1:1 (fail - too light)
```

### White Text on Brand Colors

```
✅ White on Primary-500: 4.8:1 (pass)
✅ White on Primary-700: 7.2:1 (excellent)
✅ White on Error-500: 5.1:1 (pass)
⚠️ White on Success-500: 3.2:1 (fail)
⚠️ White on Warning-500: 2.1:1 (fail)
```

---

## ⚠️ COMMON MISTAKES

```
1. ❌ Light gray text on white
   Gray-300 on White: 1.9:1 (FAIL)

2. ❌ Light text on light background
   Gray-100 on White: 1.1:1 (FAIL)

3. ❌ Colored text too light
   Light blue on white (fail)

4. ❌ Placeholder text too light
   Should be 4.5:1 even for placeholders

5. ❌ Focus indicators insufficient contrast
   Light gray border on white: only 2:1 (fail)

6. ❌ Disabled state text too light
   Should still meet 4.5:1 or clearly disabled
```

---

## 🎨 COLOR BLINDNESS

### Types

```
Protanopia (Red-blind):  ~1% of men
- Confuses red/green
- Sees red as dark
- Sees green as yellow

Deuteranopia (Green-blind): ~1% of men
- Confuses red/green
- Sees differently than protanopia
- Sees red as orange

Tritanopia (Blue-yellow blind): Rare
- Confuses blue/yellow
- Confuses red/pink
```

### Testing

```
DO:
✅ Use Stark plugin (color blindness mode)
✅ Use Color Oracle (desktop simulator)
✅ Test with simulator during design
✅ Don't rely on color alone

DON'T:
❌ Assume everyone sees colors normally
❌ Use red/green to distinguish (bad for 8% of men)
❌ Rely solely on color (use icons + color)
```

### Design Pattern

```
❌ WRONG: "Required fields in red"
✅ RIGHT: "Required fields marked with * AND red"

Visual cues:
- Icon (required *, error X, success ✓)
- Color (red, green, etc)
- Text ("Required", "Error", "Success")
```

---

## 📱 REACT NATIVE CONTRAST IMPLEMENTATION

```javascript
// Define color tokens with contrast in mind
const colors = {
  // Grays for text
  text: {
    primary: '#212121',      // Gray-900 (19.6:1 on white)
    secondary: '#616161',    // Gray-700 (8.9:1 on white)
    disabled: '#BDBDBD',     // Gray-400 (use sparingly)
  },
  background: {
    light: '#FFFFFF',
    dark: '#212121',
  },
  // Brand colors (ensure proper contrast)
  primary: {
    500: '#2196F3',          // 4.8:1 on white ✅
    700: '#1565C0',          // Higher contrast
  },
  error: {
    500: '#EF5350',          // 5.1:1 on white ✅
    700: '#C62828',          // Higher contrast
  },
  success: {
    500: '#66BB6A',          // 3.2:1 on white ❌ (too light)
    700: '#2E7D32',          // 10.2:1 on white ✅ (use this)
  },
  warning: {
    500: '#FFA726',          // 2.1:1 on white ❌ (too light)
    700: '#E65100',          // 10.5:1 on white ✅ (use this)
  },
};

// ✅ GOOD: Sufficient contrast
<Text style={{ color: colors.text.primary }}>
  Primary text on white
</Text>

// ❌ BAD: Insufficient contrast
<Text style={{ color: colors.text.disabled }}>
  Disabled text on white  (only 2.9:1)
</Text>

// ✅ GOOD: Sufficient contrast for interactive states
<TouchableOpacity
  style={[
    styles.button,
    disabled && styles.buttonDisabled,
  ]}
>
  <Text style={styles.buttonText}>Action</Text>
</TouchableOpacity>

// Styles
const styles = StyleSheet.create({
  button: {
    backgroundColor: colors.primary[700],  // Dark enough
    paddingVertical: 12,
    borderRadius: 8,
  },
  buttonDisabled: {
    backgroundColor: colors.background.light,
    borderWidth: 1,
    borderColor: colors.text.secondary,
  },
  buttonText: {
    color: '#FFFFFF',                      // White on dark blue
    fontSize: 16,
    fontWeight: '600',
  },
});
```

---

## 🌓 DARK MODE CONTRAST

If your app supports dark mode:

```javascript
// Dark mode text should also meet 4.5:1
const darkModeColors = {
  text: {
    primary: '#FFFFFF',          // White
    secondary: '#E0E0E0',        // Light gray
  },
  background: {
    dark: '#121212',
  },
};

// ✅ GOOD: White on dark background
<Text style={{ color: '#FFFFFF' }}>  // 19.6:1 on #121212
  Primary text
</Text>

// ✅ GOOD: Light gray on dark
<Text style={{ color: '#E0E0E0' }}>  // 10.9:1 on #121212
  Secondary text
</Text>

// ❌ BAD: Light gray on slightly lighter background
<Text style={{ color: '#E0E0E0' }}>  // Only 1.3:1
  Text on #C0C0C0 background
</Text>
```

---

## 📋 SVOY KRUG CONTRAST STANDARDS

### Text

```
✅ Primary text (headings, body): Gray-900 (#212121)
✅ Secondary text: Gray-700 (#616161)
✅ Helper text: Gray-600 (#757575)
⚠️ Disabled text: Gray-600 (with disabled state styling)
```

### Interactive States

```
✅ Primary button: Brand Blue (4.8:1 white text)
✅ Error: Error Red (5.1:1 white text)
✅ Success: Dark Green (10.2:1)
✅ Warning: Dark Orange (10.5:1)
```

### Focus Indicators

```
✅ Focus outline: 3:1 minimum contrast with background
✅ Width: 2-3px minimum
✅ Color: High contrast (black on light, white on dark)
```

---

## ✅ CONTRAST CHECKLIST

Before launch:

- [ ] All text meets 4.5:1 (normal) or 3:1 (large)
- [ ] Focus indicators meet 3:1
- [ ] Button text on button background: 4.5:1
- [ ] Tested with WebAIM Contrast Checker
- [ ] Tested with Color Oracle (color blindness)
- [ ] Dark mode (if supported) also passes
- [ ] Placeholder text meets contrast
- [ ] Disabled state clear (styling + text)
- [ ] Form errors have color + icon/text
- [ ] Links distinguishable (not color alone)

---

**Good contrast is the foundation of accessible design.** 🎨

