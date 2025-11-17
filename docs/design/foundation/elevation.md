# Elevation System

## Overview

The elevation system creates visual depth and hierarchy through carefully calibrated shadows. Inspired by premium design principles (Tiffany & Co aesthetic), our elevation system uses soft, subtle shadows that suggest luxury without overwhelming the interface.

Elevation indicates importance, interactivity, and spatial relationships. Our approach emphasizes understated elegance with layered, diffused shadows rather than harsh or pronounced effects.

## Specifications

### Elevation Levels

We define 5 elevation levels, from baseline (no shadow) to premium (pronounced depth):

| Level | Name | Z-Index | Use Case |
|-------|------|---------|----------|
| 0 | Baseline | 0 | Flat surfaces, backgrounds |
| 1 | Raised | 1 | Cards, components above baseline |
| 2 | Floating | 2 | Modals, popovers, menus |
| 3 | Modal | 3 | Primary modals, important overlays |
| 4 | Overlay | 4 | Full-screen overlays, dialogs |

### Shadow Specifications

Each elevation level uses a multi-layer shadow technique for depth:

#### Elevation 0 (Baseline)
```
No shadow
Z-Index: 0
```

#### Elevation 1 (Raised)
- **Soft Shadow** (ambient): 0px 2px 4px rgba(0, 0, 0, 0.08)
- **Mid Shadow** (penumbra): 0px 4px 8px rgba(0, 0, 0, 0.04)
- Z-Index: 1

#### Elevation 2 (Floating)
- **Soft Shadow**: 0px 4px 8px rgba(0, 0, 0, 0.10)
- **Mid Shadow**: 0px 8px 16px rgba(0, 0, 0, 0.06)
- **Deep Shadow** (umbra): 0px 2px 1px rgba(0, 0, 0, 0.04)
- Z-Index: 2

#### Elevation 3 (Modal)
- **Soft Shadow**: 0px 6px 12px rgba(0, 0, 0, 0.12)
- **Mid Shadow**: 0px 12px 24px rgba(0, 0, 0, 0.08)
- **Deep Shadow**: 0px 4px 2px rgba(0, 0, 0, 0.06)
- Z-Index: 3

#### Elevation 4 (Overlay)
- **Soft Shadow**: 0px 8px 16px rgba(0, 0, 0, 0.15)
- **Mid Shadow**: 0px 16px 32px rgba(0, 0, 0, 0.10)
- **Deep Shadow**: 0px 6px 4px rgba(0, 0, 0, 0.08)
- Z-Index: 4

### Color Considerations

All shadows use black (rgba(0, 0, 0, x)) with varying opacity levels:
- Soft/ambient layer: Lower opacity (4-8%)
- Mid layer: Medium opacity (6-10%)
- Deep layer: Higher opacity (4-8%)

This creates subtle, premium shadows that don't overwhelm the interface or interfere with Tiffany Blue brand colors.

## Usage Guidelines

### Elevation 1 (Raised) - For Cards

Use for:
- Card components in lists
- Subtle component elevation
- Items that are slightly interactive
- Secondary content containers

**Example**: Loyalty rewards cards, transaction items, product cards

```
Box shadow: 0px 2px 4px rgba(0, 0, 0, 0.08), 0px 4px 8px rgba(0, 0, 0, 0.04)
```

### Elevation 2 (Floating) - For Interactive Components

Use for:
- Floating action buttons
- Dropdown menus
- Tooltips
- Popovers
- Navigation drawers
- Filter panels

**Example**: Category menu, filter options, product details menu

```
Box shadow: 0px 4px 8px rgba(0, 0, 0, 0.10), 0px 8px 16px rgba(0, 0, 0, 0.06), 0px 2px 1px rgba(0, 0, 0, 0.04)
```

### Elevation 3 (Modal) - For Modals

Use for:
- Modal dialogs
- Confirmation sheets
- Action sheets
- Bottom sheets with primary actions
- Important overlays that need strong focus

**Example**: Checkout confirmation, reward redemption modal, profile settings

```
Box shadow: 0px 6px 12px rgba(0, 0, 0, 0.12), 0px 12px 24px rgba(0, 0, 0, 0.08), 0px 4px 2px rgba(0, 0, 0, 0.06)
```

### Elevation 4 (Overlay) - For Full-Screen Overlays

Use for:
- Full-screen modals
- Authentication flows
- Critical dialogs
- Scrim layers (semi-transparent backgrounds)
- Overlays requiring maximum prominence

**Example**: Login modal, payment information dialog, critical alerts

```
Box shadow: 0px 8px 16px rgba(0, 0, 0, 0.15), 0px 16px 32px rgba(0, 0, 0, 0.10), 0px 6px 4px rgba(0, 0, 0, 0.08)
```

### Scrim (Semi-transparent Overlay)

- **Opacity**: 40% black (rgba(0, 0, 0, 0.4))
- **Z-Index**: One level below the modal
- **Animation**: Fade in/out with motion-standard timing
- **Touch Behavior**: Dismisses modal when tapped
- **Use Case**: All modals, drawers, and significant overlays

## Accessibility Considerations

### Shadow & Visibility

- Shadows should enhance, not obscure, content
- Ensure text remains readable over shadowed backgrounds
- High contrast between shadow and content background
- Avoid relying on shadow alone to convey hierarchy (use color, spacing, typography)

### Reduced Motion Preference

Users with `prefers-reduced-motion: reduce` should:
- Still see elevation differences
- Experience instant (0ms) shadow changes instead of animated
- Maintain shadow opacity but remove transition effects

**CSS Implementation**:
```css
@media (prefers-reduced-motion: reduce) {
  .elevated-component {
    transition: none !important;
    box-shadow: /* immediate shadow value */;
  }
}
```

### Color Contrast & Shadows

- Verify minimum 4.5:1 contrast ratio between text and shadowed background
- Test with various background colors (especially Champagne Beige)
- Ensure shadows don't reduce perceived contrast below WCAG AA

### Screen Reader & Semantic Meaning

- Elevation is visual only; doesn't affect screen reader announcements
- Use semantic HTML/ARIA to convey hierarchy
- Don't rely on shadow to indicate interactive vs. static elements

## Design Tokens & Code Examples

### CSS Variables

```css
--elevation-0: none;
--elevation-1: 0px 2px 4px rgba(0, 0, 0, 0.08), 0px 4px 8px rgba(0, 0, 0, 0.04);
--elevation-2: 0px 4px 8px rgba(0, 0, 0, 0.10), 0px 8px 16px rgba(0, 0, 0, 0.06), 0px 2px 1px rgba(0, 0, 0, 0.04);
--elevation-3: 0px 6px 12px rgba(0, 0, 0, 0.12), 0px 12px 24px rgba(0, 0, 0, 0.08), 0px 4px 2px rgba(0, 0, 0, 0.06);
--elevation-4: 0px 8px 16px rgba(0, 0, 0, 0.15), 0px 16px 32px rgba(0, 0, 0, 0.10), 0px 6px 4px rgba(0, 0, 0, 0.08);

--scrim-overlay: rgba(0, 0, 0, 0.4);
```

### React Native Implementation

```typescript
// tokens/elevation.ts
import { StyleSheet } from 'react-native';

export const elevation = {
  none: {
    shadowColor: 'transparent',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0,
    shadowRadius: 0,
    elevation: 0,
  },
  
  level1: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 4,
    elevation: 2,
  },
  
  level2: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.10,
    shadowRadius: 8,
    elevation: 4,
  },
  
  level3: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.12,
    shadowRadius: 12,
    elevation: 6,
  },
  
  level4: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.15,
    shadowRadius: 16,
    elevation: 8,
  },
} as const;

export type ElevationLevel = keyof typeof elevation;
```

### Card Component with Elevation

```typescript
import { View, StyleSheet } from 'react-native';
import { elevation } from './tokens/elevation';

interface CardProps {
  children: React.ReactNode;
  level?: ElevationLevel;
}

const Card: React.FC<CardProps> = ({ children, level = 'level1' }) => {
  const styles = StyleSheet.create({
    container: {
      backgroundColor: '#FFFFFF',
      borderRadius: 12,
      ...elevation[level],
    },
  });

  return <View style={styles.container}>{children}</View>;
};

export default Card;
```

### Modal Component with Scrim

```typescript
import { Modal, View, StyleSheet, TouchableOpacity } from 'react-native';
import { colors } from './tokens/colors';
import { elevation } from './tokens/elevation';

interface ModalProps {
  visible: boolean;
  onDismiss: () => void;
  children: React.ReactNode;
}

const PremiumModal: React.FC<ModalProps> = ({ visible, onDismiss, children }) => {
  const styles = StyleSheet.create({
    scrim: {
      flex: 1,
      backgroundColor: 'rgba(0, 0, 0, 0.4)',
      justifyContent: 'flex-end',
    },
    content: {
      backgroundColor: colors.white,
      borderTopLeftRadius: 24,
      borderTopRightRadius: 24,
      paddingBottom: 20,
      ...elevation.level3,
    },
  });

  return (
    <Modal
      visible={visible}
      transparent
      animationType="slide"
      onRequestClose={onDismiss}
    >
      <TouchableOpacity
        style={styles.scrim}
        activeOpacity={1}
        onPress={onDismiss}
      >
        <View style={styles.content}>{children}</View>
      </TouchableOpacity>
    </Modal>
  );
};

export default PremiumModal;
```

### Shadow Composition Helper

```typescript
// utils/elevation.ts
export const composeShadow = (
  offsetY: number,
  blurRadius: number,
  opacity: number
) => ({
  shadowColor: '#000',
  shadowOffset: { width: 0, height: offsetY },
  shadowOpacity: opacity,
  shadowRadius: blurRadius,
  elevation: Math.ceil(offsetY + blurRadius / 2),
});

// Usage for custom elevation levels
const customElevation = composeShadow(
  8,    // offsetY
  16,   // blurRadius
  0.15  // opacity
);
```

## Platform-Specific Considerations

### iOS
- Use `shadowColor`, `shadowOffset`, `shadowOpacity`, `shadowRadius`
- Shadow rendering is more accurate to specification
- Supports multi-layer shadows through composition
- Better performance with blurred shadows

### Android
- Use `elevation` property (API level 21+)
- Android Material elevation differs from CSS shadows
- For precise control, consider custom shadow implementation
- Test on actual devices for shadow rendering accuracy

## Examples by Component Type

### List Item (Elevation 1)
```typescript
const listItemStyles = StyleSheet.create({
  container: {
    backgroundColor: '#FFFFFF',
    marginHorizontal: 16,
    marginVertical: 8,
    borderRadius: 12,
    padding: 16,
    ...elevation.level1,
  },
});
```

### Floating Action Button (Elevation 2)
```typescript
const fabStyles = StyleSheet.create({
  container: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: colors.tiffanyBlue,
    justifyContent: 'center',
    alignItems: 'center',
    ...elevation.level2,
  },
});
```

### Bottom Sheet Modal (Elevation 3)
```typescript
const bottomSheetStyles = StyleSheet.create({
  content: {
    backgroundColor: colors.white,
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    padding: 24,
    ...elevation.level3,
  },
});
```

### Full-Screen Modal (Elevation 4)
```typescript
const fullModalStyles = StyleSheet.create({
  content: {
    flex: 1,
    backgroundColor: colors.white,
    ...elevation.level4,
  },
});
```

## Animation & Elevation Changes

### Interactive States

When components change elevation (on press, hover, etc.):

```typescript
// State-based elevation
const [isPressed, setIsPressed] = useState(false);

const dynamicElevation = isPressed 
  ? elevation.level2 
  : elevation.level1;
```

### Animated Elevation Transitions

```typescript
import { Animated } from 'react-native';

const elevationAnim = useRef(new Animated.Value(0)).current;

const onPressIn = () => {
  Animated.timing(elevationAnim, {
    toValue: 8,
    duration: 200,
    useNativeDriver: false,
  }).start();
};

// Apply to elevation value dynamically
```

## Testing Elevation

### Visual Verification

- Print designs and verify shadow depth perception
- Test on physical devices (iOS and Android)
- Check shadows under different lighting conditions
- Verify contrast ratios with text overlays

### Accessibility Testing

- Use accessibility inspector tools
- Test with `prefers-reduced-motion: reduce`
- Verify semantic meaning isn't lost without shadows
- Screen reader testing for hierarchy perception

## Related Documentation

- [Motion System](./motion.md) - Timing for elevation changes
- [Spacing System](./spacing.md) - Spatial relationships with elevation
- [Design Tokens](../00_DESIGN_SYSTEM.md) - Complete token system
- [Color System](./color.md) - Shadow colors and contrast
- [Components](../components/README.md) - Component elevation usage
