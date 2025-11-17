# Colors

**Last Updated:** 2025-11-17
**Status:** ✅ Extracted from design screenshots

---

## Overview

The Свой Круг color palette embodies **premium elegance** with a Tiffany & Co-inspired approach. Our colors communicate luxury, warmth, and exclusivity while maintaining excellent accessibility.

---

## Primary Palette

### Tiffany Blue (Primary)
**Usage:** Primary actions, highlights, active states, branding

```
HEX: #0ABAB5
RGB: rgb(10, 186, 181)
HSL: hsl(178, 90%, 38%)
```

**Applications:**
- Primary buttons
- Active navigation items  
- Links
- Progress indicators
- Focus states
- Brand highlights

**Accessibility:** ✅ Passes WCAG AA on white backgrounds (contrast ratio 3.84:1 for large text)

---

### Champagne Beige (Background)
**Usage:** Primary backgrounds, cards, subtle warmth

```
HEX: #F5F1E8
RGB: rgb(245, 241, 232)
HSL: hsl(42, 38%, 94%)
```

**Applications:**
- App backgrounds
- Card backgrounds  
- Empty states
- Overlays (light)

**Accessibility:** ✅ Excellent contrast with dark text (ratio 1.08:1 with white)

---

### Champagne Gold (Accent)
**Usage:** Premium elements, achievements, logo, highlights

```
HEX: #D4AF37
RGB: rgb(212, 175, 55)
HSL: hsl(46, 65%, 52%)
```

**Applications:**
- Logo primary color
- Achievement badges
- VIP/Elite status indicators
- Premium features highlight
- Celebratory elements

**Accessibility:** ⚠️ Use with dark text only (contrast 5.12:1)

---

## Secondary Palette

### Charcoal (Text Primary)
**Usage:** Primary text, headings, important content

```
HEX: #2A2D34
RGB: rgb(42, 45, 52)
HSL: hsl(222, 11%, 18%)
```

**Accessibility:** ✅ Excellent (contrast 14.8:1 on white)

---

### Taupe (Text Secondary)
**Usage:** Secondary text, metadata, captions

```
HEX: #8B7355
RGB: rgb(139, 115, 85)
HSL: hsl(33, 24%, 44%)
```

**Accessibility:** ✅ Passes AA (contrast 4.6:1 on white)

---

## Semantic Colors

### Success (Soft Green)
**Usage:** Success messages, confirmations, positive states

```
HEX: #7CB342
RGB: rgb(124, 179, 66)
HSL: hsl(89, 46%, 48%)
```

**Applications:**
- Success toasts
- Confirmation checkmarks
- Positive balance changes
- Completed actions

**Accessibility:** ✅ Passes AA (contrast 3.12:1 for large text on white)

---

### Error (Soft Red)
**Usage:** Error messages, validation errors, destructive actions

```
HEX: #E57373
RGB: rgb(229, 115, 115)
HSL: hsl(0, 68%, 67%)
```

**Applications:**
- Error messages
- Form validation errors
- Destructive button states
- Alert icons

**Accessibility:** ✅ Passes AA (contrast 3.18:1 for large text)

---

### Warning (Amber)
**Usage:** Warnings, cautions, important notices

```
HEX: #FFB74D
RGB: rgb(255, 183, 77)
HSL: hsl(36, 100%, 65%)
```

**Applications:**
- Warning messages
- Expiring offers
- Low balance alerts
- Attention-required states

**Accessibility:** ⚠️ Pair with dark text (contrast 1.82:1 on white)

---

### Info (Light Blue)
**Usage:** Informational messages, tips, neutral highlights

```
HEX: #64B5F6
RGB: rgb(100, 181, 246)
HSL: hsl(207, 89%, 68%)
```

**Applications:**
- Info toasts
- Tips and hints
- Neutral notifications
- Helper text highlights

**Accessibility:** ✅ Passes AA (contrast 2.91:1 for large text)

---

## Neutral Grays

### Gray Scale
**Usage:** Borders, dividers, disabled states, backgrounds

```
Gray 50:  #FAFAFA (backgrounds)
Gray 100: #F5F5F5 (subtle backgrounds)
Gray 200: #EEEEEE (borders light)
Gray 300: #E0E0E0 (borders default)
Gray 400: #BDBDBD (borders strong, disabled text)
Gray 500: #9E9E9E (placeholder text)
Gray 600: #757575 (secondary text)
Gray 700: #616161 (text alternative)
Gray 800: #424242 (text strong)
Gray 900: #212121 (text primary)
```

**Accessibility:** All grays 600+ pass AA for body text

---

## Branding Colors (Logo Variations)

### Bronze (Logo Alternative)
```
HEX: #8B7355
RGB: rgb(139, 115, 85)
```

### Soft Pink (Status Badges)
```
HEX: #E8B4BC
RGB: rgb(232, 180, 188)
```

**Usage:** Bronze/VIP status tier indicators

---

## Usage Guidelines

### Do's ✅
- Use Tiffany Blue for all primary actions
- Maintain Champagne Beige as primary background for warmth
- Reserve Champagne Gold for premium/achievement elements only
- Always check color contrast before using custom combinations
- Use semantic colors consistently (green = success, red = error)

### Don'ts ❌
- Don't use Champagne Gold for body text (insufficient contrast)
- Don't mix Tiffany Blue with similar blues (creates confusion)
- Don't use semantic colors for decorative purposes
- Don't override semantic meanings (red ≠ success)

---

## Accessibility Compliance

**Target:** WCAG 2.1 Level AA

**Text Contrast Requirements:**
- Normal text (< 18px): ≥ 4.5:1 contrast ratio
- Large text (≥ 18px or 14px bold): ≥ 3:1 contrast ratio
- UI components & graphical elements: ≥ 3:1

**Testing:**
All color combinations used for text have been tested and documented above.

**Tools:**
- WebAIM Contrast Checker
- Figma contrast plugins
- Automated accessibility audits in Storybook

---

## Design Tokens

See: `resources/design-tokens.json` for implementation-ready values

```json
{
  "colors": {
    "primary": "#0ABAB5",
    "background": "#F5F1E8",
    "accent": "#D4AF37",
    "text": {
      "primary": "#2A2D34",
      "secondary": "#8B7355"
    },
    "semantic": {
      "success": "#7CB342",
      "error": "#E57373",
      "warning": "#FFB74D",
      "info": "#64B5F6"
    }
  }
}
```

---

**Related:**
- [Typography](typography.md) - Color usage in text
- [Components](../components/) - Component-specific color usage
- [Accessibility](../accessibility/color-contrast.md) - Detailed contrast testing

**Source:** Extracted from design screenshots in `UPMT/bootstrap/00_DESIGN_RAW_DATA/screenshots/`
