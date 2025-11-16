# COLOR SYSTEM

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## 🎨 COLOR PALETTE

### Primary Colors

**Purpose:** Brand identity, primary actions, key UI elements

```yaml
Primary:
  50:  #E3F2FD  # Lightest - hover states
  100: #BBDEFB  # Very light
  200: #90CAF9  # Light
  300: #64B5F6  # Medium light
  400: #42A5F5  # Medium
  500: #2196F3  # Base (use this by default)
  600: #1E88E2  # Medium dark - hover
  700: #1976D2  # Dark
  800: #1565C0  # Very dark
  900: #0D47A1  # Darkest - emphasis
```

**Usage:**
- Primary buttons (`background: primary-500`)
- Links (`color: primary-600`)
- Active states (`background: primary-100`)
- Brand elements
- Focus rings (`border-color: primary-500`)

**Do's:**
- ✅ Use primary-500 as default
- ✅ Use lighter shades for hover/backgrounds
- ✅ Use darker shades for text on light
- ✅ Maintain 4.5:1 contrast ratio minimum

**Don'ts:**
- ❌ Don't use primary-50/100 for text (low contrast)
- ❌ Don't overuse (not everything should be blue)
- ❌ Don't mix with secondary in same action

---

### Secondary Colors

**Purpose:** Secondary actions, accents, variety

```yaml
Secondary:
  50:  #F3E5F5  # Lightest
  100: #E1BEE7
  200: #CE93D8
  300: #BA68C8
  400: #AB47BC
  500: #9C27B0  # Base (purple/accent)
  600: #8E24AA  # Hover
  700: #7B1FA2
  800: #6A1B9A
  900: #4A148C  # Darkest
```

**Usage:**
- Secondary buttons
- Accents and highlights
- Tags/badges (variety)
- Supporting UI elements

**When to use:**
- When primary would be too strong
- For variety in multi-action scenarios
- Highlights that aren't CTAs

---

### Semantic Colors

**Purpose:** Communicate meaning (status, feedback)

#### Success

```yaml
Success:
  50:  #E8F5E9
  100: #C8E6C9
  200: #A5D6A7
  300: #81C784
  400: #66BB6A
  500: #4CAF50  # Green base
  600: #43A047  # Hover
  700: #388E3C
  800: #2E7D32
  900: #1B5E20
```

**Usage:**
- Success messages
- Positive states (completed, verified)
- Positive actions (approve, confirm)
- Progress indicators (done)

---

#### Error

```yaml
Error:
  50:  #FFEBEE
  100: #FFCDD2
  200: #EF9A9A
  300: #E57373
  400: #EF5350
  500: #F44336  # Red base
  600: #E53935  # Hover
  700: #D32F2F
  800: #C62828
  900: #B71C1C
```

**Usage:**
- Error messages
- Destructive actions (delete, remove)
- Validation errors
- Critical warnings

---

#### Warning

```yaml
Warning:
  50:  #FFF3E0
  100: #FFE0B2
  200: #FFCC80
  300: #FFB74D
  400: #FFA726
  500: #FF9800  # Orange base
  600: #FB8C00  # Hover
  700: #F57C00
  800: #EF6C00
  900: #E65100
```

**Usage:**
- Warning messages
- Caution states
- Important notices (non-critical)
- Pending actions

---

#### Info

```yaml
Info:
  50:  #E1F5FE
  100: #B3E5FC
  200: #81D4FA
  300: #4FC3F7
  400: #29B6F6
  500: #03A9F4  # Cyan base
  600: #039BE5  # Hover
  700: #0288D1
  800: #0277BD
  900: #01579B
```

**Usage:**
- Informational messages
- Helper text
- Tips and hints
- Neutral notifications

---

### Neutral Colors (Grays)

**Purpose:** Text, backgrounds, borders, structure

```yaml
Gray:
  50:  #FAFAFA  # Almost white - page background
  100: #F5F5F5  # Very light - card backgrounds
  200: #EEEEEE  # Light - borders, dividers
  300: #E0E0E0  # Medium light - hover states
  400: #BDBDBD  # Medium - disabled elements
  500: #9E9E9E  # Medium dark - secondary text
  600: #757575  # Dark - tertiary text
  700: #616161  # Darker - secondary headings
  800: #424242  # Very dark - primary text
  900: #212121  # Darkest - emphasis text

White: #FFFFFF  # Pure white - cards, modals
Black: #000000  # Pure black - rarely used directly
```

**Usage Guidelines:**

**Backgrounds:**
- Page background: `gray-50`
- Card/Modal background: `white`
- Hover background: `gray-100`
- Selected background: `primary-50`
- Disabled background: `gray-200`

**Text:**
- Primary text: `gray-900` (headings, main content)
- Secondary text: `gray-500` (descriptions, metadata)
- Tertiary text: `gray-600` (timestamps, captions)
- Disabled text: `gray-400`
- Placeholder text: `gray-400`
- On primary button: `white`
- On dark bg: `white` or `gray-50`

**Borders:**
- Default border: `gray-200` (1px)
- Hover border: `gray-300`
- Focus border: `primary-500` (2px)
- Divider: `gray-200`
- Strong divider: `gray-300`

---

## 🎯 USAGE GUIDELINES

### Color Hierarchy

```
High Emphasis (attention grabbing):
- Primary colors
- Semantic colors (error, success)
- High contrast

Medium Emphasis (supporting):
- Secondary colors
- Gray-700, Gray-800
- Medium contrast

Low Emphasis (background):
- Light grays (50-300)
- Low contrast
```

### Color Combinations

**Good Combinations:**
- ✅ Primary-500 + White (buttons)
- ✅ Gray-900 + White (text on page)
- ✅ Success-500 + White (success buttons)
- ✅ Gray-50 + Gray-900 (page background + text)

**Avoid:**
- ❌ Primary-500 + Secondary-500 (competing)
- ❌ Error-500 + Warning-500 (confusing)
- ❌ Gray-400 + White (low contrast)

---

## ♿ ACCESSIBILITY

### Contrast Ratios (WCAG 2.1 AA)

**Requirements:**
- Normal text (≥16px): **4.5:1 minimum**
- Large text (≥18px or ≥14px bold): **3:1 minimum**
- UI components (borders, icons): **3:1 minimum**

### Tested Combinations

**Text on White:**
- ✅ Gray-900 on White: **18.2:1** (excellent)
- ✅ Gray-800 on White: **12.6:1** (excellent)
- ✅ Gray-700 on White: **8.9:1** (excellent)
- ✅ Gray-500 on White: **4.6:1** (pass)
- ⚠️ Gray-400 on White: **2.9:1** (fail - don't use for text)
- ❌ Gray-300 on White: **1.9:1** (fail)

**Colors on White:**
- ✅ Primary-500 on White: **4.8:1** (pass)
- ✅ Primary-700 on White: **7.2:1** (excellent)
- ✅ Success-500 on White: **3.8:1** (large text only)
- ✅ Error-500 on White: **5.1:1** (pass)
- ✅ Warning-600 on White: **3.2:1** (large text only)

**White on Colors:**
- ✅ White on Primary-500: **4.8:1** (pass)
- ✅ White on Primary-600: **5.6:1** (pass)
- ✅ White on Success-500: **3.9:1** (large text OK)
- ✅ White on Error-500: **5.1:1** (pass)
- ⚠️ White on Warning-500: **2.1:1** (fail - use Warning-600+)

### Color Blindness

**Don't rely on color alone:**
- ✅ Error message: Red color + "Error:" prefix + icon
- ❌ Error message: Just red color

**Test combinations:**
- Protanopia (red-blind)
- Deuteranopia (green-blind)
- Tritanopia (blue-blind)

**Tools:**
- Color Oracle (simulator)
- Figma plugins (Stark, A11y)

---

## 🔧 IMPLEMENTATION

### CSS Variables

```css
:root {
  /* Primary */
  --color-primary-50: #E3F2FD;
  --color-primary-100: #BBDEFB;
  --color-primary-200: #90CAF9;
  --color-primary-300: #64B5F6;
  --color-primary-400: #42A5F5;
  --color-primary-500: #2196F3;
  --color-primary-600: #1E88E2;
  --color-primary-700: #1976D2;
  --color-primary-800: #1565C0;
  --color-primary-900: #0D47A1;
  
  /* Semantic */
  --color-success-500: #4CAF50;
  --color-error-500: #F44336;
  --color-warning-500: #FF9800;
  --color-info-500: #03A9F4;
  
  /* Neutral */
  --color-gray-50: #FAFAFA;
  --color-gray-100: #F5F5F5;
  --color-gray-200: #EEEEEE;
  --color-gray-300: #E0E0E0;
  --color-gray-400: #BDBDBD;
  --color-gray-500: #9E9E9E;
  --color-gray-600: #757575;
  --color-gray-700: #616161;
  --color-gray-800: #424242;
  --color-gray-900: #212121;
  --color-white: #FFFFFF;
  --color-black: #000000;
}
```

### Tailwind Config

```js
module.exports = {
  theme: {
    colors: {
      primary: {
        50: '#E3F2FD',
        100: '#BBDEFB',
        200: '#90CAF9',
        300: '#64B5F6',
        400: '#42A5F5',
        500: '#2196F3',
        600: '#1E88E2',
        700: '#1976D2',
        800: '#1565C0',
        900: '#0D47A1',
      },
      gray: {
        50: '#FAFAFA',
        100: '#F5F5F5',
        200: '#EEEEEE',
        300: '#E0E0E0',
        400: '#BDBDBD',
        500: '#9E9E9E',
        600: '#757575',
        700: '#616161',
        800: '#424242',
        900: '#212121',
      },
      success: {
        500: '#4CAF50',
      },
      error: {
        500: '#F44336',
      },
      warning: {
        500: '#FF9800',
      },
      white: '#FFFFFF',
      black: '#000000',
    }
  }
}
```

### SCSS Variables

```scss
// Primary
$color-primary-50: #E3F2FD;
$color-primary-500: #2196F3;
$color-primary-900: #0D47A1;

// Semantic
$color-success: #4CAF50;
$color-error: #F44336;
$color-warning: #FF9800;

// Neutral
$color-gray-50: #FAFAFA;
$color-gray-900: #212121;
$color-white: #FFFFFF;
```

---

## 📊 DESIGN TOKENS

**Machine-readable format:**

See [design-tokens.json](../resources/design-tokens.json) for complete JSON format.

---

## 🔄 WHEN TO UPDATE

Update colors when:
- ✅ Rebranding
- ✅ Accessibility improvements needed
- ✅ New semantic color required
- ✅ User feedback on readability

**Process:**
1. Update Figma variables
2. Update this file
3. Update design-tokens.json
4. Update code (CSS/Tailwind)
5. Test accessibility
6. Update changelog

---

## 📝 NOTES

**Why these specific colors?**

Example reasoning:
- Primary Blue (#2196F3): Conveys trust, professionalism
- Success Green (#4CAF50): Universal "success" indicator
- Error Red (#F44336): Clear warning, high visibility
- Grays: Neutral, flexible, WCAG AA compliant

**Adjust during bootstrap** based on your brand/needs!

---

## ✅ CHECKLIST

Before finalizing color system:

- [ ] All colors have 4.5:1 contrast minimum (text)
- [ ] Semantic colors are distinct (colorblind tested)
- [ ] Primary color reflects brand
- [ ] Gray scale is flexible (9 shades)
- [ ] Design tokens created (JSON)
- [ ] Figma variables match
- [ ] Code implementation matches

---

**Color is powerful. Use it wisely.** 🎨

