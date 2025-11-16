# TYPOGRAPHY

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be filled during bootstrap

---

## 📝 TYPE SCALE

### Font Families

```yaml
Primary (UI):
  Family: Inter
  Weights: 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold)
  Usage: UI text, buttons, labels, body text
  
Secondary (Display):
  Family: Inter
  Weights: 600 (Semibold), 700 (Bold)
  Usage: Headings, hero text, marketing
  
Monospace (Code):
  Family: "JetBrains Mono" or "Fira Code"
  Weights: 400 (Regular), 500 (Medium)
  Usage: Code blocks, technical text, logs
```

**Why Inter?**
- Excellent readability at all sizes
- Variable font (flexible weights)
- Free, open-source
- Wide language support
- Designed for screens

**Alternatives:**
- Roboto, SF Pro (Apple), Segoe UI (Windows)

---

### Font Sizes

```yaml
Display (Hero):
  Size: 48px / 3rem
  Line Height: 1.1 (52.8px)
  Weight: 700 (Bold)
  Usage: Hero headings, landing pages

Heading 1 (H1):
  Size: 32px / 2rem
  Line Height: 1.2 (38.4px)
  Weight: 700 (Bold)
  Usage: Page titles, main headings

Heading 2 (H2):
  Size: 24px / 1.5rem
  Line Height: 1.3 (31.2px)
  Weight: 600 (Semibold)
  Usage: Section headings

Heading 3 (H3):
  Size: 20px / 1.25rem
  Line Height: 1.4 (28px)
  Weight: 600 (Semibold)
  Usage: Subsection headings

Heading 4 (H4):
  Size: 18px / 1.125rem
  Line Height: 1.4 (25.2px)
  Weight: 600 (Semibold)
  Usage: Card titles, component headings

Body Large:
  Size: 18px / 1.125rem
  Line Height: 1.5 (27px)
  Weight: 400 (Regular)
  Usage: Large body text, intros

Body (Default):
  Size: 16px / 1rem
  Line Height: 1.5 (24px)
  Weight: 400 (Regular)
  Usage: Main body text, descriptions

Body Small:
  Size: 14px / 0.875rem
  Line Height: 1.5 (21px)
  Weight: 400 (Regular)
  Usage: Secondary text, metadata

Caption:
  Size: 12px / 0.75rem
  Line Height: 1.5 (18px)
  Weight: 400 (Regular)
  Usage: Labels, captions, timestamps

Overline:
  Size: 12px / 0.75rem
  Line Height: 1.5 (18px)
  Weight: 600 (Semibold)
  Letter Spacing: 0.5px (uppercase)
  Usage: Labels, tags, categories
```

---

## 📏 LINE HEIGHT

```yaml
Headings:
  Line Height: 1.1 - 1.3
  Why: Tight spacing for visual impact

Body Text:
  Line Height: 1.5
  Why: Optimal readability for paragraphs

Small Text:
  Line Height: 1.5
  Why: Consistent spacing

Code/Technical:
  Line Height: 1.6
  Why: Slightly more space for readability
```

**General Rule:**
- Larger text → tighter line height
- Smaller text → looser line height
- Body text → 1.5 (golden standard)

---

## 🎯 USAGE GUIDELINES

### Hierarchy

```
Display (48px, Bold)    ← Biggest impact
    ↓
Heading 1 (32px, Bold)  ← Page level
    ↓
Heading 2 (24px, Semi)  ← Section level
    ↓
Heading 3 (20px, Semi)  ← Subsection
    ↓
Heading 4 (18px, Semi)  ← Component
    ↓
Body (16px, Regular)    ← Default content
    ↓
Small (14px, Regular)   ← Secondary
    ↓
Caption (12px, Regular) ← Least emphasis
```

### When to Use What

**Display (48px):**
- Hero sections
- Landing page headlines
- Marketing pages
- High-impact announcements

**H1 (32px):**
- Page titles (Dashboard, Settings, Profile)
- Main page headings
- Modal titles (important)

**H2 (24px):**
- Section headers (Overview, Details, Activity)
- Tab titles
- Panel headings

**H3 (20px):**
- Subsections within sections
- Sidebar headings
- Step titles in multi-step flows

**H4 (18px):**
- Card titles
- List section headers
- Table headers (important)

**Body (16px):**
- Paragraphs
- Descriptions
- List items
- Form help text

**Body Small (14px):**
- Secondary descriptions
- Metadata (author, date, status)
- Sidebar text
- Table cells

**Caption (12px):**
- Timestamps
- Labels (form labels, badges)
- Footnotes
- Helper text (minimal)

**Overline (12px, uppercase):**
- Category labels
- Section tags
- Breadcrumbs
- Status badges

---

## ⚖️ FONT WEIGHTS

```yaml
Regular (400):
  Usage: Body text, descriptions, lists
  Most common weight

Medium (500):
  Usage: Emphasis in body text, important labels
  Subtle emphasis

Semibold (600):
  Usage: Headings, buttons, important UI elements
  Strong emphasis

Bold (700):
  Usage: Hero text, H1, strong emphasis
  Maximum emphasis
```

**Guidelines:**
- Don't use too many weights (3-4 max)
- Regular (400) for body
- Semibold (600) for headings
- Bold (700) for emphasis

---

## 📱 RESPONSIVE TYPOGRAPHY

### Desktop (≥1024px)

Use base sizes as defined above.

### Tablet (768px - 1023px)

```yaml
Display: 40px (was 48px)
H1: 28px (was 32px)
H2: 22px (was 24px)
Body: 16px (unchanged)
```

### Mobile (< 768px)

```yaml
Display: 32px (was 48px)
H1: 24px (was 32px)
H2: 20px (was 24px)
H3: 18px (was 20px)
Body: 16px (unchanged - never go below!)
```

**Rule:** Never go below 16px for body text (readability).

---

## ♿ ACCESSIBILITY

### Minimum Sizes

- **Body text:** 16px minimum (never smaller)
- **Small text:** 14px minimum for secondary
- **Caption:** 12px OK for labels/metadata only

### Readability

**Line Length:**
- Optimal: 45-75 characters per line
- Max width: 80 characters

**Contrast:**
- Regular text (16px): 4.5:1 minimum
- Large text (18px+): 3:1 minimum

**Line Height:**
- Body text: 1.5 minimum (WCAG)
- Headings: 1.3 minimum

### Font Weight

- Don't rely on font weight alone for meaning
- Use size, color, AND weight for hierarchy

---

## 🔧 IMPLEMENTATION

### CSS

```css
/* Font Families */
--font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;

/* Font Sizes */
--font-size-display: 3rem;      /* 48px */
--font-size-h1: 2rem;           /* 32px */
--font-size-h2: 1.5rem;         /* 24px */
--font-size-h3: 1.25rem;        /* 20px */
--font-size-h4: 1.125rem;       /* 18px */
--font-size-body-lg: 1.125rem;  /* 18px */
--font-size-body: 1rem;         /* 16px */
--font-size-body-sm: 0.875rem;  /* 14px */
--font-size-caption: 0.75rem;   /* 12px */

/* Line Heights */
--line-height-tight: 1.1;
--line-height-snug: 1.3;
--line-height-normal: 1.5;
--line-height-relaxed: 1.6;

/* Font Weights */
--font-weight-regular: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;

/* Usage Classes */
.text-display {
  font-size: var(--font-size-display);
  line-height: var(--line-height-tight);
  font-weight: var(--font-weight-bold);
}

.text-h1 {
  font-size: var(--font-size-h1);
  line-height: var(--line-height-snug);
  font-weight: var(--font-weight-bold);
}

.text-body {
  font-size: var(--font-size-body);
  line-height: var(--line-height-normal);
  font-weight: var(--font-weight-regular);
}
```

### Tailwind Config

```js
module.exports = {
  theme: {
    fontFamily: {
      sans: ['Inter', 'sans-serif'],
      mono: ['JetBrains Mono', 'monospace'],
    },
    fontSize: {
      'display': ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
      'h1': ['2rem', { lineHeight: '1.2', fontWeight: '700' }],
      'h2': ['1.5rem', { lineHeight: '1.3', fontWeight: '600' }],
      'h3': ['1.25rem', { lineHeight: '1.4', fontWeight: '600' }],
      'h4': ['1.125rem', { lineHeight: '1.4', fontWeight: '600' }],
      'body-lg': ['1.125rem', { lineHeight: '1.5' }],
      'body': ['1rem', { lineHeight: '1.5' }],
      'body-sm': ['0.875rem', { lineHeight: '1.5' }],
      'caption': ['0.75rem', { lineHeight: '1.5' }],
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    }
  }
}
```

---

## 🎨 EXAMPLES

### Good Typography

```
Hero Section:
├── Display (48px, Bold): "Welcome to [Product]"
├── Body Large (18px, Regular): "Description text here with good readability"
└── Button (16px, Semibold): "Get Started"

Content Page:
├── H1 (32px, Bold): "Page Title"
├── Body (16px, Regular): "Main content paragraph with optimal line height..."
├── H2 (24px, Semibold): "Section Heading"
└── Body (16px, Regular): "Section content..."
```

### Common Mistakes

**❌ Too many sizes:**
```
48px, 36px, 30px, 28px, 24px, 20px, 18px, 16px...
(confusing, no clear hierarchy)
```

**✅ Clear scale:**
```
48px (Display), 32px (H1), 24px (H2), 20px (H3), 16px (Body)
(clear hierarchy, consistent)
```

**❌ Low contrast:**
```
Gray-400 text on White background
(contrast ratio: 2.9:1 - fails WCAG)
```

**✅ Good contrast:**
```
Gray-900 text on White background
(contrast ratio: 18.2:1 - excellent)
```

---

## 📊 DESIGN TOKENS

See [design-tokens.json](../resources/design-tokens.json) for typography tokens.

---

## 🔄 WHEN TO UPDATE

Update typography when:
- Rebranding (new fonts)
- Readability issues reported
- Adding new text styles
- Responsive adjustments needed

**Process:**
1. Update Figma text styles
2. Update this file
3. Update design-tokens.json
4. Update code (CSS/Tailwind)
5. Test responsive sizes
6. Update changelog

---

## ✅ CHECKLIST

Before finalizing typography:

- [ ] Font families loaded (web fonts)
- [ ] Type scale is consistent (clear hierarchy)
- [ ] Line heights are readable (1.5 for body)
- [ ] Contrast ratios pass WCAG (4.5:1 min)
- [ ] Responsive sizes tested
- [ ] Design tokens match Figma
- [ ] Code implementation matches

---

**Typography is the voice of your design. Make it clear.** 📝

