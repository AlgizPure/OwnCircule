# Design System - Свой Круг (Own Circle)

**Version:** 1.0.0
**Last Updated:** 2025-11-17
**Status:** ✅ Initial Design System (from screenshot analysis)

---

## Overview

This design system defines the visual language, components, and guidelines for the Свой Круг (Own Circle) premium loyalty ecosystem. Our design embodies **elegance, exclusivity, and simplicity** - reflecting the premium nature of our women's community.

### Design Philosophy

**Core Principles:**
- **Premium & Elegant:** Inspired by Tiffany & Co's timeless luxury aesthetic
- **Warm & Inviting:** Champagne and soft tones create welcoming experiences
- **Clear & Focused:** Information hierarchy guides users effortlessly
- **Mobile-First:** Optimized for on-the-go premium lifestyle
- **Accessible:** WCAG 2.1 AA compliance for inclusive design

### Brand Identity

**Visual Inspiration:** Tiffany & Co (iconic blue + luxury feel) + Modern mobile UX (Revolut clarity, Linear speed)

**Logo:** Circular design representing unity and connection ("круг" = circle)
- Primary: Champagne Gold segmented circle
- Secondary: Tiffany Blue variations
- Tertiary: Bronze/brown natural tones

---

## Foundation

### Colors
See: [foundation/colors.md](foundation/colors.md)

**Primary Palette:**
- **Tiffany Blue** (#0ABAB5) - Primary actions, highlights, active states
- **Champagne Beige** (#F5F1E8) - Backgrounds, warmth
- **Champagne Gold** (#D4AF37) - Premium accents, logo, achievements

**Semantic Colors:**
- Success: Soft Green (#7CB342)
- Error: Soft Red (#E57373)
- Warning: Amber (#FFB74D)
- Info: Light Blue (#64B5F6)

### Typography
See: [foundation/typography.md](foundation/typography.md)

**Font Families:**
- **iOS:** SF Pro Display (headings), SF Pro Text (body)
- **Android:** Roboto (all weights)
- **Web Fallback:** -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif

**Type Scale:**
- Display: 34px / 700 (onboarding, hero sections)
- H1: 28px / 700 (screen titles)
- H2: 22px / 600 (section headers)
- H3: 18px / 600 (card titles)
- Body Large: 16px / 400 (primary content)
- Body: 14px / 400 (secondary content)
- Caption: 12px / 400 (metadata, labels)

### Spacing
See: [foundation/spacing.md](foundation/spacing.md)

**Base Unit:** 8px

**Scale:** 4px, 8px, 16px, 24px, 32px, 48px, 64px

### Elevation & Shadows
See: [foundation/elevation.md](foundation/elevation.md)

**Card Shadows:** Soft, subtle (0px 2px 8px rgba(0,0,0,0.08))

### Motion & Animation
See: [foundation/motion.md](foundation/motion.md)

**Timing:** 200ms (micro), 300ms (standard), 500ms (complex)

---

## Components

See: [components/](components/)

**Core Components:**
- Button (primary, secondary, ghost)
- Input (text, phone, search)
- Card (partner, event, status)
- Navigation (bottom tabs, top bar)
- QR Code Display
- Status Badge
- Partner Card
- Event Card
- Points Display

---

## Content Guidelines

See: [content/](content/)

**Voice & Tone:**
- Professional yet warm
- Empowering and exclusive
- Clear and concise
- Russian language with premium vocabulary

---

## Accessibility

See: [accessibility/](accessibility/)

**Target:** WCAG 2.1 Level AA Compliance

**Key Requirements:**
- Color contrast ≥ 4.5:1 for text
- Touch targets ≥ 44x44px
- Keyboard navigation support
- Screen reader optimization
- Focus indicators visible

---

## Resources

- **Figma Files:** See [resources/figma-links.md](resources/figma-links.md)
- **Design Tokens:** [resources/design-tokens.json](resources/design-tokens.json)
- **Changelog:** [resources/changelog.md](resources/changelog.md)

---

## Using This Design System

### For Designers
1. Review foundation (colors, typography, spacing)
2. Use components from library
3. Follow accessibility guidelines
4. Reference screenshots in \`UPMT/bootstrap/00_DESIGN_RAW_DATA/screenshots/\`

### For Developers
1. Import design tokens from \`resources/design-tokens.json\`
2. Implement components per specifications
3. Reference module requirements for screen-specific designs
4. Test against accessibility checklist

### For Product Managers
1. Use screen templates for feature planning
2. Reference content guidelines for copy
3. Ensure designs align with brand principles

---

## Related Documentation

- **Module Requirements:** \`docs/requirements/module-01-mobile-app.md\` (UI/UX section)
- **Architecture:** \`docs/core/04_ARCHITECTURE.md\` (Frontend structure)
- **Tech Stack:** \`docs/core/03_TECH_STACK.md\` (React Native, TypeScript)

---

**Maintained by:** Design Team
**Questions?** See docs/design/README.md or contact project leads
