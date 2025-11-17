# Spacing System

## Overview

The spacing system defines consistent, predictable spacing values used throughout the Свой Круг design system. Based on an 8px unit grid, our spacing system ensures visual harmony, improved readability, and easier implementation across iOS and Android platforms.

This foundational element creates rhythm and balance in our interface, helping users navigate content intuitively and reducing cognitive load through consistent visual hierarchies.

## Specifications

### Spacing Units

Our spacing system is built on an 8px base unit with a geometric progression approach:

| Token | Value | Usage |
|-------|-------|-------|
| `spacing-0` | 0px | Reset/none |
| `spacing-xs` | 4px | Small gaps, internal spacing |
| `spacing-sm` | 8px | Base unit, button padding |
| `spacing-md` | 12px | Component gaps |
| `spacing-lg` | 16px | Sections, containers |
| `spacing-xl` | 24px | Major sections |
| `spacing-2xl` | 32px | Page-level spacing |
| `spacing-3xl` | 40px | Large containers |
| `spacing-4xl` | 48px | Hero sections |

### Geometric Progression

We follow an 8px base with 1.5x scaling multiplier for larger values:

```
Base: 8px
8px × 1 = 8px
8px × 1.5 = 12px
8px × 2 = 16px
8px × 3 = 24px
8px × 4 = 32px
8px × 5 = 40px
8px × 6 = 48px
```

This creates harmonious relationships between values while maintaining the 8px grid alignment.

## Usage Guidelines

### Component Padding

- **Buttons**: 8px vertical, 16px horizontal (spacing-sm, spacing-lg)
- **Input Fields**: 12px vertical, 16px horizontal (spacing-md, spacing-lg)
- **Cards**: 16px padding (spacing-lg)
- **Cell Rows**: 12px vertical, 16px horizontal (spacing-md, spacing-lg)

### Margin & Layout Spacing

- **Between Components**: 16-24px (spacing-lg to spacing-xl)
- **Between Sections**: 32-40px (spacing-2xl to spacing-3xl)
- **Section Edges**: 16px minimum (spacing-lg)
- **Top Safe Area**: 8px minimum above content
- **Bottom Safe Area**: 8px minimum below content

### Spacing Scale in Layouts

```
Body Content
├─ Top Margin: spacing-2xl (32px)
├─ Section 1
│  ├─ Padding: spacing-lg (16px)
│  └─ Child Spacing: spacing-md (12px)
├─ Gap Between Sections: spacing-xl (24px)
├─ Section 2
│  ├─ Padding: spacing-lg (16px)
│  └─ Child Spacing: spacing-md (12px)
└─ Bottom Margin: spacing-2xl (32px)
```

### Mobile-Specific Considerations

- Minimum touch target height: 44px (includes spacing-lg padding)
- Minimum touch target width: 44px
- Reduce spacing-4xl on small screens to spacing-3xl
- Use spacing-xl as minimum between tap targets
- Maintain spacing-lg horizontal padding on screen edges

### Premium Density

Our premium aesthetic benefits from generous spacing:

- Avoid spacing-0 and spacing-xs in primary UI
- Use spacing-lg as minimum for primary content
- Stack vertical spacing generously for visual breathing room
- Horizontal edges maintain spacing-lg minimum for elegance

## Accessibility Considerations

### Visual Spacing & Cognitive Load

- Adequate spacing reduces visual overwhelm
- Consistent spacing improves predictability for cognitive disabilities
- Generous spacing aids readability for low-vision users
- Clear visual hierarchy through spacing benefits dyslexic users

### Touch Target Accessibility

- All interactive elements must be minimum 44x44pt
- Minimum 8px spacing between adjacent touch targets
- Use spacing-xl (24px) for better touch accuracy
- Avoid cramped layouts that cause mis-taps

### WCAG 2.1 Compliance

- Spacing does not prevent content accessibility
- Zoom to 200% must maintain usable spacing
- Text spacing adjustments (1.5x line-height, etc.) must be supported
- No fixed spacing that breaks responsive layouts

### Color Contrast & Spacing

Adequate spacing helps users with color blindness:
- Don't rely on spacing alone to convey structure
- Combine spacing with visual separators
- Use consistent spacing patterns for recognition

## Design Tokens & Code Examples

### CSS/Design System Variables

```css
--spacing-0: 0px;
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 12px;
--spacing-lg: 16px;
--spacing-xl: 24px;
--spacing-2xl: 32px;
--spacing-3xl: 40px;
--spacing-4xl: 48px;
```

### React Native Implementation

```javascript
// tokens/spacing.ts
export const spacing = {
  0: 0,
  xs: 4,
  sm: 8,
  md: 12,
  lg: 16,
  xl: 24,
  '2xl': 32,
  '3xl': 40,
  '4xl': 48,
} as const;

export type SpacingToken = keyof typeof spacing;

// Usage in components
const styles = StyleSheet.create({
  container: {
    padding: spacing.lg,
    marginVertical: spacing.xl,
  },
  section: {
    marginTop: spacing['2xl'],
  },
  card: {
    padding: spacing.lg,
    marginHorizontal: spacing.lg,
    marginVertical: spacing.md,
  },
});
```

### TypeScript Helper

```typescript
// utils/spacing.ts
export const createSpacing = (
  top?: SpacingToken,
  right?: SpacingToken,
  bottom?: SpacingToken,
  left?: SpacingToken
) => {
  const t = spacing[top ?? 'md'];
  const r = spacing[right ?? 'lg'];
  const b = spacing[bottom ?? 'md'];
  const l = spacing[left ?? 'lg'];
  
  return { marginTop: t, marginRight: r, marginBottom: b, marginLeft: l };
};

// Usage
const cardMargin = createSpacing('lg', 'lg', 'xl', 'lg');
```

### Tailwind-Style Utility

```typescript
// For styled-components or similar
type Side = 'top' | 'right' | 'bottom' | 'left' | 'vertical' | 'horizontal' | 'all';

export const margin = (token: SpacingToken, side: Side = 'all') => {
  const value = spacing[token];
  
  switch (side) {
    case 'top': return { marginTop: value };
    case 'bottom': return { marginBottom: value };
    case 'right': return { marginRight: value };
    case 'left': return { marginLeft: value };
    case 'vertical': return { marginVertical: value };
    case 'horizontal': return { marginHorizontal: value };
    case 'all': return { margin: value };
  }
};
```

## Examples by Component Type

### Button Component

```typescript
const buttonStyles = StyleSheet.create({
  container: {
    paddingVertical: spacing.sm,      // 8px
    paddingHorizontal: spacing.lg,    // 16px
    borderRadius: 8,
  },
  text: {
    fontSize: 16,
  },
});
```

### Card Component

```typescript
const cardStyles = StyleSheet.create({
  container: {
    padding: spacing.lg,              // 16px all sides
    marginHorizontal: spacing.lg,     // 16px left/right
    marginVertical: spacing.md,       // 12px top/bottom
    borderRadius: 12,
  },
  title: {
    marginBottom: spacing.sm,         // 8px below title
    fontSize: 18,
  },
  content: {
    marginTop: spacing.md,            // 12px above content
  },
});
```

### List Item Component

```typescript
const listItemStyles = StyleSheet.create({
  container: {
    paddingVertical: spacing.md,      // 12px vertical
    paddingHorizontal: spacing.lg,    // 16px horizontal
    borderBottomWidth: 1,
  },
  avatar: {
    marginRight: spacing.md,          // 12px gap from avatar
  },
  text: {
    marginBottom: spacing.xs,         // 4px between lines
  },
});
```

### Modal/Dialog Component

```typescript
const modalStyles = StyleSheet.create({
  overlay: {
    padding: spacing.lg,              // 16px padding
  },
  content: {
    padding: spacing.xl,              // 24px padding
    borderRadius: 16,
  },
  header: {
    marginBottom: spacing.lg,         // 16px below header
  },
  actions: {
    marginTop: spacing.lg,            // 16px above actions
    gap: spacing.md,                  // 12px between buttons
  },
});
```

## Responsive Spacing

### Mobile (320px - 767px)

- Primary spacing: spacing-lg (16px)
- Section spacing: spacing-xl (24px)
- Edge padding: spacing-lg (16px)

### Tablet (768px - 1024px)

- Primary spacing: spacing-lg to spacing-xl (16-24px)
- Section spacing: spacing-2xl (32px)
- Edge padding: spacing-xl (24px)

### Desktop (1024px+)

- Primary spacing: spacing-xl (24px)
- Section spacing: spacing-3xl (40px)
- Edge padding: spacing-2xl (32px)

## Common Spacing Patterns

### Card Stack Pattern
```
Cards separated by: spacing-md (12px)
Card internal padding: spacing-lg (16px)
Card margin edges: spacing-lg (16px)
```

### Form Pattern
```
Field spacing: spacing-lg (16px)
Label to input: spacing-sm (8px)
Error message to field: spacing-xs (4px)
Button group gap: spacing-md (12px)
```

### Section Divider Pattern
```
Before divider: spacing-xl (24px)
After divider: spacing-xl (24px)
Divider height: spacing-xs (4px)
```

## Related Documentation

- [Elevation System](./elevation.md) - Depth and layering
- [Motion System](./motion.md) - Transitions and timing
- [Design Tokens](../00_DESIGN_SYSTEM.md) - Complete token system
- [Accessibility Guidelines](../accessibility/wcag.md) - Accessibility standards
- [Component Library](../components/README.md) - Component usage
