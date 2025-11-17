# Typography

**Last Updated:** 2025-11-17
**Status:** ✅ Defined for React Native cross-platform

---

## Overview

Typography for Свой Круг balances **elegance and readability** using system fonts optimized for each platform. Our type scale ensures visual hierarchy while maintaining premium feel.

---

## Font Families

### iOS (Primary)
```
Primary: SF Pro Display (headings, display)
Secondary: SF Pro Text (body, UI elements)
```

**Why SF Pro:**
- Native to iOS, optimal rendering
- Excellent legibility at all sizes
- Professional, modern aesthetic  
- Multiple weights available (300-700)
- Designed for Retina displays

### Android (Primary)
```
Primary: Roboto (all uses)
Weights: Light (300), Regular (400), Medium (500), Bold (700)
```

**Why Roboto:**
- Native to Android Material Design
- Clean, geometric letterforms
- Excellent cross-platform consistency
- Wide character set (Cyrillic support)

### Web Fallback
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
             'Oxygen', 'Ubuntu', 'Cantarell', 'Helvetica Neue', sans-serif;
```

---

## Type Scale

### Display (34px / 700)
**Usage:** Hero sections, onboarding, major announcements

```
Font Size: 34px (2.125rem)
Line Height: 40px (1.18)
Font Weight: 700 (Bold)
Letter Spacing: -0.5px
```

**Example:**
```
Добро пожаловать  
в Свой Круг!
```

**Accessibility:** ✅ High contrast required (4.5:1 minimum)

---

### H1 (28px / 700)
**Usage:** Screen titles, page headers

```
Font Size: 28px (1.75rem)
Line Height: 34px (1.21)
Font Weight: 700 (Bold)
Letter Spacing: -0.3px
```

**Example:**
```
Партнёры
```

**Accessibility:** ✅ Meets WCAG AA for large text (3:1 minimum contrast)

---

### H2 (22px / 600)
**Usage:** Section headers, card titles

```
Font Size: 22px (1.375rem)
Line Height: 28px (1.27)
Font Weight: 600 (Semibold)
Letter Spacing: 0px
```

**Example:**
```
События клуба
```

---

### H3 (18px / 600)
**Usage:** Card titles, list headers, sub-sections

```
Font Size: 18px (1.125rem)
Line Height: 24px (1.33)
Font Weight: 600 (Semibold)
Letter Spacing: 0px
```

**Example:**
```
Женский вечер
```

**Accessibility:** ✅ Passes AA for large text

---

### Body Large (16px / 400)
**Usage:** Primary content, important descriptions

```
Font Size: 16px (1rem)
Line Height: 24px (1.5)
Font Weight: 400 (Regular)
Letter Spacing: 0px
```

**Example:**
```
Получайте бонусы во всех партнёрских  
заведениях и обменивайте на привилегии
```

**Accessibility:** ✅ Optimal reading size for mobile

---

### Body (14px / 400)
**Usage:** Secondary content, descriptions, list items

```
Font Size: 14px (0.875rem)
Line Height: 20px (1.43)
Font Weight: 400 (Regular)
Letter Spacing: 0px
```

**Example:**
```
Бонус 100 баллов при покупке от 500₽
```

**Accessibility:** ⚠️ Requires 4.5:1 contrast (normal text)

---

### Caption (12px / 400)
**Usage:** Metadata, labels, timestamps, helper text

```
Font Size: 12px (0.75rem)
Line Height: 16px (1.33)
Font Weight: 400 (Regular)
Letter Spacing: 0.3px
```

**Example:**
```
До VIP осталось 650₽
25 мая - 19:00
```

**Accessibility:** ⚠️ Use sparingly, ensure high contrast (7:1 recommended)

---

## Font Weights

### Available Weights

**SF Pro (iOS):**
- Light: 300
- Regular: 400
- Medium: 500
- Semibold: 600
- Bold: 700

**Roboto (Android):**
- Light: 300
- Regular: 400
- Medium: 500
- Bold: 700

### Weight Usage Guidelines

| Weight | Usage |
|--------|-------|
| 300 (Light) | Reserved for display/hero text only |
| 400 (Regular) | Body text, descriptions, default |
| 500 (Medium) | Subtle emphasis, button labels |
| 600 (Semibold) | Headings, important labels |
| 700 (Bold) | Strong emphasis, CTA buttons, titles |

---

## Line Height

**Base Ratio:** 1.5 for body text (optimal readability)

**Adjustments:**
- Display/Headlines: 1.2-1.3 (tighter for visual impact)
- Body text: 1.4-1.5 (comfortable reading)
- Captions/small text: 1.3-1.4 (compact)

**Minimum:** Never below 1.2 (accessibility requirement)

---

## Letter Spacing

**Guidelines:**
- Display/Large Headings: Slightly negative (-0.3px to -0.5px) for optical balance
- Body Text: 0px (default)
- Captions/Small Text: Slightly positive (+0.3px) for legibility
- ALL CAPS: +0.5px to +1px (always increase for readability)

---

## Usage Examples

### Screen Title Pattern
```
H1 (28px/700): Партнёры
Body (14px/400): Выбирайте из 5 премиальных заведений
```

### Card Pattern
```
H3 (18px/600): Гастромаркет
Caption (12px/400): Бонус 100 баллов при покупке от 500₽
```

### Status Display Pattern
```
Caption (12px/400): Уровень
H2 (22px/600): 320
Caption (12px/400): баллов
```

---

## Accessibility Guidelines

### WCAG 2.1 Level AA Compliance

**Minimum Contrast Ratios:**
- **Normal text (< 18px):** 4.5:1
- **Large text (≥ 18px or ≥ 14px bold):** 3:1

**Font Size Recommendations:**
- ✅ **Minimum for body text:** 14px (mobile), 16px (preferred)
- ✅ **Minimum for captions:** 12px (use sparingly)
- ❌ **Avoid:** Text smaller than 12px

**Line Height Requirements:**
- Minimum 1.5 for body text (WCAG Success Criterion 1.4.12)
- Minimum 1.2 for headings

**Text Spacing:**
Users must be able to adjust:
- Line height to at least 1.5x font size
- Paragraph spacing to at least 2x font size
- Letter spacing to at least 0.12x font size
- Word spacing to at least 0.16x font size

### Color Combinations (with Typography)

**Approved Combinations:**
- ✅ Charcoal (#2A2D34) on White: 14.8:1
- ✅ Charcoal on Champagne Beige (#F5F1E8): 13.2:1
- ✅ Taupe (#8B7355) on White: 4.6:1 (AA pass)
- ✅ Taupe on Champagne Beige: 4.1:1 (AA pass for 18px+)

**Not Approved:**
- ❌ Champagne Gold on White: 3.2:1 (fails for normal text)
- ❌ Gray 400 on Champagne Beige: < 3:1

---

## Responsive Typography

### Mobile (320px - 428px)
**Use defined scale as-is**
- Display: 34px
- H1: 28px
- Body: 14-16px

### Tablet (429px - 1024px)
**Optional scale up +2px:**
- Display: 36px
- H1: 30px
- Body: 16-18px

### Desktop (1025px+)
**Optional scale up +4px:**
- Display: 38px
- H1: 32px
- Body: 18px

**Note:** For MVP (mobile-first), stick to base scale

---

## Implementation

### React Native (StyleSheet)
```javascript
const typography = {
  display: {
    fontSize: 34,
    lineHeight: 40,
    fontWeight: '700',
    letterSpacing: -0.5,
  },
  h1: {
    fontSize: 28,
    lineHeight: 34,
    fontWeight: '700',
    letterSpacing: -0.3,
  },
  body: {
    fontSize: 14,
    lineHeight: 20,
    fontWeight: '400',
    letterSpacing: 0,
  },
};
```

### CSS (Web)
```css
:root {
  --font-display-size: 34px;
  --font-display-line-height: 40px;
  --font-display-weight: 700;
  
  --font-h1-size: 28px;
  --font-h1-line-height: 34px;
  --font-h1-weight: 700;
  
  --font-body-size: 14px;
  --font-body-line-height: 20px;
  --font-body-weight: 400;
}
```

---

## Design Tokens

See: `resources/design-tokens.json`

```json
{
  "typography": {
    "fontFamily": {
      "ios": "SF Pro Display",
      "android": "Roboto",
      "web": "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    },
    "fontSize": {
      "display": "34px",
      "h1": "28px",
      "h2": "22px",
      "h3": "18px",
      "bodyLarge": "16px",
      "body": "14px",
      "caption": "12px"
    },
    "fontWeight": {
      "light": "300",
      "regular": "400",
      "medium": "500",
      "semibold": "600",
      "bold": "700"
    }
  }
}
```

---

**Related:**
- [Colors](colors.md) - Color usage with typography
- [Spacing](spacing.md) - Text spacing guidelines
- [Accessibility](../accessibility/overview.md) - Typography accessibility

**Cyrillic Support:** ✅ All fonts fully support Russian language
