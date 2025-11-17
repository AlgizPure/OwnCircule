# Iconography System

## Overview

Icons are a critical part of the Свой Круг design language. Our iconography system emphasizes clarity, elegance, and premium aesthetics aligned with the Tiffany & Co inspired visual identity. Icons serve as visual communication shortcuts, improving scannability and reducing cognitive load.

Our approach balances minimalism with distinctive personality—each icon should be instantly recognizable while maintaining visual harmony with our premium brand aesthetic.

## Specifications

### Icon Grid System

All icons are designed on a 24x24px base grid at 1x scale:

| Grid Size | Scale | Usage |
|-----------|-------|-------|
| 24x24px | 1x (100%) | Primary icons, navigation, actions |
| 32x32px | 1.33x (133%) | Larger contexts, hero sections |
| 40x40px | 1.67x (167%) | Prominent features, CTAs |
| 48x48px | 2x (200%) | Large features, onboarding |
| 16x16px | 0.67x (67%) | Compact contexts, inline |

### Design Principles

#### Stroke Weight
- **Primary**: 1.5px stroke (24x24px base)
- **Compact**: 1px stroke (16x16px)
- **Large**: 2px stroke (40x48px)

Consistency in stroke weight maintains visual cohesion across all sizes.

#### Optical Sizing
- Thin strokes optically lighter at small sizes; account for visual weight
- Thicker strokes maintain boldness at larger scales
- Negative space must be balanced across sizes

#### Rounded Corners
- **Primary corners**: 1.5px radius
- **Inner curves**: Smooth, consistent radius
- **Endpoints**: Slight rounding for premium feel (not squared)

### Icon Categories

#### Navigation Icons
- Home, Explore, Rewards, Profile, Settings
- Always visible, frequently used
- Clear, straightforward forms
- Immediate recognition priority

#### Action Icons
- Add, Edit, Delete, Save, Share, More
- Clear visual metaphors
- Directional clarity
- Distinction from navigation icons

#### Status Icons
- Success, Warning, Error, Info
- Quick comprehension required
- Often paired with color
- Accessibility-critical

#### Feature Icons
- Product categories, loyalty tiers, benefits
- Brand personality
- Distinctive character
- Context-dependent

#### Utility Icons
- Search, Filter, Sort, Close, Menu
- Essential functionality
- Minimal, efficient design
- Universal understanding

### Color Application

#### Tiffany Blue Primary (#0ABAB5)
- Default icon color
- Interactive, active states
- Primary call-to-action icons
- Navigation highlights

#### Champagne Gold (#D4AF37)
- Premium, special features
- Loyalty/rewards elements
- Premium tier indicators
- Accent and decorative

#### Neutral Gray (#757575)
- Inactive states
- Secondary actions
- Disabled states
- Supporting information

#### White (#FFFFFF)
- Icons on dark backgrounds
- Contrast on Tiffany Blue
- Premium/invert usage
- Elevation overlays

#### Status Colors
- Success: #4CAF50
- Warning: #FF9800
- Error: #F44336
- Info: #2196F3

## Design Guidelines

### Clarity & Legibility

- Icons must be instantly recognizable
- No overly complex details
- Clear negative space
- Distinguishable from other icons
- Readable at minimum 16x16px

### Visual Balance

- Center weight optically within grid
- Equal visual weight across designs
- Balanced positive/negative space
- Consistent outer dimensions
- Geometric alignment

### Consistency

- Uniform stroke weight within system
- Consistent corner radii
- Similar visual complexity
- Aligned to grid consistently
- Matching geometric language

### Accessibility

All icons require:
- Meaningful alt text when standalone
- Clear visual distinction (not color alone)
- Sufficient contrast (minimum 3:1)
- Semantic relationship to content
- Never convey critical information through icon only

### States & Variations

Each icon should support:
- **Default**: Primary state
- **Active/Selected**: Highlight state (usually filled or colored)
- **Disabled**: Reduced opacity or gray
- **Loading**: Rotatable version (if applicable)
- **Hover**: Subtle color shift on web

## Design Tokens & Code Examples

### Icon Token System

```typescript
// tokens/icons.ts
export const iconSizes = {
  xs: 16,      // Compact, inline
  sm: 24,      // Primary/default
  md: 32,      // Medium/larger
  lg: 40,      // Large/prominent
  xl: 48,      // Extra large/hero
} as const;

export const iconColors = {
  primary: '#0ABAB5',      // Tiffany Blue
  secondary: '#D4AF37',    // Champagne Gold
  neutral: '#757575',      // Gray
  white: '#FFFFFF',
  success: '#4CAF50',
  warning: '#FF9800',
  error: '#F44336',
  info: '#2196F3',
} as const;

export const iconStrokeWeights = {
  compact: 1,              // 16px size
  primary: 1.5,            // 24px size
  large: 2,                // 40-48px sizes
} as const;

export type IconSize = keyof typeof iconSizes;
export type IconColor = keyof typeof iconColors;
```

### Icon Component (React Native)

```typescript
// components/Icon.tsx
import { View, ViewStyle } from 'react-native';
import Svg, { Path, Circle, Rect } from 'react-native-svg';
import { iconSizes, iconColors } from '../tokens/icons';

interface IconProps {
  name: string;
  size?: IconSize;
  color?: IconColor;
  style?: ViewStyle;
  filled?: boolean;
  disabled?: boolean;
}

export const Icon: React.FC<IconProps> = ({
  name,
  size = 'sm',
  color = 'primary',
  style,
  filled = false,
  disabled = false,
}) => {
  const dimension = iconSizes[size];
  const fillColor = disabled ? iconColors.neutral : iconColors[color];

  return (
    <View style={[{ width: dimension, height: dimension }, style]}>
      <Svg width={dimension} height={dimension} viewBox={`0 0 24 24`}>
        {/* Dynamic icon rendering based on name */}
        {getIconPath(name, fillColor, filled)}
      </Svg>
    </View>
  );
};

// Helper to get icon paths dynamically
const getIconPath = (name: string, color: string, filled: boolean) => {
  const iconMap: Record<string, React.ReactNode> = {
    heart: (
      <Path
        d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
        fill={filled ? color : 'none'}
        stroke={color}
        strokeWidth={1.5}
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    ),
    // Add more icons...
  };

  return iconMap[name] || null;
};
```

### Icon Library Definition

```typescript
// libraries/icons/index.ts
export const ICONS = {
  // Navigation
  HOME: 'home',
  EXPLORE: 'explore',
  REWARDS: 'rewards',
  PROFILE: 'profile',
  SETTINGS: 'settings',

  // Actions
  ADD: 'add',
  EDIT: 'edit',
  DELETE: 'delete',
  SAVE: 'save',
  SHARE: 'share',
  MORE: 'more',

  // Status
  SUCCESS: 'success',
  WARNING: 'warning',
  ERROR: 'error',
  INFO: 'info',
  CHECKMARK: 'checkmark',

  // Utility
  SEARCH: 'search',
  FILTER: 'filter',
  SORT: 'sort',
  CLOSE: 'close',
  MENU: 'menu',
  BACK: 'back',
  FORWARD: 'forward',

  // Feature
  GIFT: 'gift',
  HEART: 'heart',
  STAR: 'star',
  LOCK: 'lock',
  UNLOCK: 'unlock',
  CLOCK: 'clock',
  BELL: 'bell',
} as const;

export type IconName = typeof ICONS[keyof typeof ICONS];
```

### Using Icons in Components

```typescript
// Usage examples
<Icon name={ICONS.HEART} size="sm" color="primary" />
<Icon name={ICONS.STAR} size="lg" color="secondary" filled={true} />
<Icon name={ICONS.CHECKMARK} color="success" />
<Icon name={ICONS.CLOSE} color="error" disabled={true} />
```

### SVG Icon Template

```typescript
// Consistent SVG template for all icons (24x24px base)
import Svg, { Path } from 'react-native-svg';

const HeartIcon = ({ color = '#0ABAB5', size = 24, filled = false }) => (
  <Svg width={size} height={size} viewBox="0 0 24 24">
    <Path
      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
      fill={filled ? color : 'none'}
      stroke={color}
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </Svg>
);

export default HeartIcon;
```

## Icon States & Variations

### Default State
- Primary color (#0ABAB5)
- 1.5px stroke (24px size)
- Outlined style (unless filled variant exists)

### Active/Selected State
- Same color, typically filled
- May show background highlight
- Consistent visual weight

### Disabled State
- Neutral gray (#757575)
- Reduced opacity (60-70%)
- No interactive behavior

### Loading State
- Rotating animation
- 200ms rotation timing
- Linear easing
- Continuous loop

```typescript
// Loading state example
const [rotation, setRotation] = useState(new Animated.Value(0));

useEffect(() => {
  const animation = Animated.loop(
    Animated.timing(rotation, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true,
    })
  );
  animation.start();
}, []);

const rotateInterpolate = rotation.interpolate({
  inputRange: [0, 1],
  outputRange: ['0deg', '360deg'],
});
```

## Accessibility Guidelines

### Icon + Text Pairing

When icons appear with text:
- Icon alone should not be sole conveyor of meaning
- Text provides redundancy and clarity
- Sufficient contrast between icon and background

### Icon-Only Usage

When icons appear without text:
- Must be in universally understood contexts (e.g., close button)
- Tooltip or aria-label required for clarity
- Alternative text in code comments

### Color Accessibility

- Don't rely on color alone to convey meaning
- Status icons paired with symbols (checkmark, X, !)
- Test with colorblind simulations
- Minimum 3:1 contrast ratio

### Touch Target Sizes

- Minimum 44x44pt touch area
- Icon can be 24x24px within larger target
- Padding around icon for easier interaction
- Maintain 8px minimum spacing between targets

## Platform-Specific Considerations

### iOS

- Use SF Symbols system integration
- Consistent with iOS design language
- Custom icons exported as PDF/SVG
- Weight variations (light, regular, bold)

### Android

- Follow Material Design 3 icon guidelines
- 24dp default size (aligns with 24px)
- Consistent stroke weight
- Proper safe area for interactive padding

### Web

- Export as optimized SVG
- Inline SVG for color flexibility
- Font icons as fallback (Font Awesome, etc.)
- CSS for sizing and coloring

## Icon Library Structure

```
assets/
├── icons/
│   ├── navigation/
│   │   ├── home.svg
│   │   ├── explore.svg
│   │   ├── rewards.svg
│   │   ├── profile.svg
│   │   └── settings.svg
│   ├── actions/
│   │   ├── add.svg
│   │   ├── edit.svg
│   │   ├── delete.svg
│   │   └── ...
│   ├── status/
│   │   ├── success.svg
│   │   ├── warning.svg
│   │   ├── error.svg
│   │   └── info.svg
│   └── utility/
│       ├── search.svg
│       ├── filter.svg
│       ├── close.svg
│       └── ...
└── icon-map.ts
```

## Icon Design Best Practices

### Do's
- Keep icons simple and clear
- Maintain consistent visual language
- Use geometric, balanced forms
- Test at small sizes (16-24px)
- Ensure accessibility through labels
- Document icon usage and meanings
- Version icons with design system

### Don'ts
- Don't create overly complex details
- Don't mix icon styles within system
- Don't rely on color alone
- Don't use non-standard sizes (stick to grid)
- Don't animate unnecessarily
- Don't ignore accessibility needs
- Don't forget disabled states

## Testing Icons

### Visual Verification
- Print at 16x24px sizes to verify clarity
- Compare across platforms
- Check contrast ratios
- Verify visual weight consistency

### Accessibility Testing
- Screen reader alt text
- Color contrast verification
- Keyboard navigation compatibility
- Touch target sizing

### Performance
- SVG optimization (remove unnecessary data)
- Icon loading performance
- Animation frame rates
- Memory usage for icon libraries

## Related Documentation

- [Color System](./color.md) - Icon colors and accessibility
- [Motion System](./motion.md) - Icon animations and transitions
- [Spacing System](./spacing.md) - Icon padding and touch targets
- [Accessibility Guidelines](../accessibility/wcag.md) - Icon accessibility
- [Components](../components/README.md) - Component icon usage
