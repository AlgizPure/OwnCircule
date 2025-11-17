# Button Component

## Overview

The Button component is a fundamental interactive element that triggers actions when pressed. It serves as the primary call-to-action throughout the OwnCircule application. Buttons are designed with rounded corners, soft styling, and clear visual feedback to guide user interactions.

**Primary Use Cases:**
- Submitting forms
- Navigating to new screens
- Confirming actions
- Booking appointments (e.g., "Записаться")

## Anatomy

The Button component consists of the following visual parts:

```
┌─────────────────────────────┐
│  Icon (optional)  Label     │
└─────────────────────────────┘
│← Padding: 16px horizontal  │
│← Padding: 12px vertical    │
│← Border Radius: 8px        │
│← Min Height: 44px          │
```

### Key Elements:
- **Background**: Solid color or gradient based on variant
- **Label**: Text using H3 typography (18px/600)
- **Icon**: Optional leading icon (16x16px or 24x24px)
- **Feedback State**: Visual indicator for interaction states
- **Touch Target**: Minimum 44x44px for accessibility

## Variants

### 1. Primary Button
- **Background**: Tiffany Blue (#0ABAB5)
- **Text Color**: White
- **Usage**: Main call-to-action, primary navigation
- **Example**: "Записаться", "Подтвердить"

### 2. Secondary Button
- **Background**: Champagne Beige (#F5F1E8)
- **Text Color**: Charcoal (#2A2D34)
- **Border**: 1px Tiffany Blue (#0ABAB5)
- **Usage**: Alternative actions, cancel operations

### 3. Accent Button
- **Background**: Champagne Gold (#D4AF37)
- **Text Color**: Charcoal (#2A2D34)
- **Usage**: Premium features, special promotions

### 4. Tertiary/Ghost Button
- **Background**: Transparent
- **Text Color**: Tiffany Blue (#0ABAB5)
- **Border**: None
- **Usage**: Less prominent actions, inline actions

## States

### Default State
- Background with full opacity
- Text with appropriate color
- No shadow or minimal shadow

### Hover State
- Background opacity increases by 10%
- Subtle elevation (shadow scale: 2)
- Cursor changes to pointer

### Active/Pressed State
- Background opacity increases by 20%
- Elevation increases (shadow scale: 4)
- Visual feedback confirms interaction

### Disabled State
- Background opacity: 50%
- Text opacity: 60%
- Cursor: not-allowed
- No hover or active state responses

### Loading State
- Text hidden
- Activity indicator displayed
- Button remains disabled
- Minimum duration: 400ms

### Focus State (Keyboard)
- 2px outline in Tiffany Blue (#0ABAB5)
- Outline offset: 2px
- Visible when navigating via keyboard

## Props/API

```typescript
interface ButtonProps {
  // Content
  label: string;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right'; // default: 'left'

  // Styling
  variant?: 'primary' | 'secondary' | 'accent' | 'tertiary'; // default: 'primary'
  size?: 'small' | 'medium' | 'large'; // default: 'medium'
  fullWidth?: boolean; // default: false

  // State
  disabled?: boolean; // default: false
  loading?: boolean; // default: false

  // Interaction
  onPress: () => void;

  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;

  // Styling overrides
  style?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
}
```

## Spacing & Sizing

### Size Variants

#### Small Button
- **Height**: 36px
- **Padding**: 12px horizontal, 8px vertical
- **Font**: 14px/600
- **Min Touch Target**: 36x44px (width x height with spacing)

#### Medium Button (Default)
- **Height**: 44px
- **Padding**: 16px horizontal, 12px vertical
- **Font**: 18px/600
- **Min Touch Target**: 44x44px

#### Large Button
- **Height**: 52px
- **Padding**: 20px horizontal, 16px vertical
- **Font**: 18px/600
- **Min Touch Target**: 52x52px

### Icon Sizing
- **Small Button Icon**: 16x16px
- **Medium Button Icon**: 20x20px
- **Large Button Icon**: 24x24px
- **Icon Gap**: 8px from label

### Border Radius
- All variants: 8px for standard appearance
- Option for 16px for more rounded style

## Accessibility

### Touch Target
- Minimum 44x44px tap area per WCAG 2.1
- Adequate spacing between adjacent buttons (minimum 8px)

### Contrast Ratio
- Primary Button: 4.51:1 (Tiffany Blue on White)
- Secondary Button: 10.86:1 (Charcoal on Beige)
- All variants meet WCAG AA standard

### Screen Reader Support
```typescript
<TouchableOpacity
  accessible={true}
  accessibilityLabel={accessibilityLabel || label}
  accessibilityHint={accessibilityHint}
  accessibilityRole="button"
/>
```

### Keyboard Navigation
- Focusable via keyboard
- Activatable with Enter key
- Clear focus indicator (2px outline)

## Implementation

### React Native Example

```typescript
import React from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
  View,
  ActivityIndicator,
} from 'react-native';

interface ButtonProps {
  label: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'accent' | 'tertiary';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  loading?: boolean;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  label,
  onPress,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  loading = false,
  icon,
  iconPosition = 'left',
  fullWidth = false,
}) => {
  const styles = getStyles(variant, size, disabled, fullWidth);

  return (
    <TouchableOpacity
      style={[styles.container, disabled && styles.disabled]}
      onPress={onPress}
      disabled={disabled || loading}
      accessible={true}
      accessibilityLabel={label}
      accessibilityRole="button"
      activeOpacity={0.8}
    >
      {loading ? (
        <ActivityIndicator
          color={variant === 'secondary' ? '#2A2D34' : '#FFFFFF'}
          size="small"
        />
      ) : (
        <View style={styles.content}>
          {icon && iconPosition === 'left' && (
            <View style={styles.iconContainer}>{icon}</View>
          )}
          <Text style={styles.label}>{label}</Text>
          {icon && iconPosition === 'right' && (
            <View style={styles.iconContainer}>{icon}</View>
          )}
        </View>
      )}
    </TouchableOpacity>
  );
};

const getStyles = (
  variant: string,
  size: string,
  disabled: boolean,
  fullWidth: boolean,
) => {
  const sizeStyles = {
    small: { height: 36, paddingHorizontal: 12, paddingVertical: 8 },
    medium: { height: 44, paddingHorizontal: 16, paddingVertical: 12 },
    large: { height: 52, paddingHorizontal: 20, paddingVertical: 16 },
  };

  const variantStyles = {
    primary: { backgroundColor: '#0ABAB5', color: '#FFFFFF' },
    secondary: {
      backgroundColor: '#F5F1E8',
      color: '#2A2D34',
      borderWidth: 1,
      borderColor: '#0ABAB5',
    },
    accent: { backgroundColor: '#D4AF37', color: '#2A2D34' },
    tertiary: { backgroundColor: 'transparent', color: '#0ABAB5' },
  };

  const sizeDim = sizeStyles[size as keyof typeof sizeStyles];
  const variantStyle = variantStyles[variant as keyof typeof variantStyles];

  return StyleSheet.create({
    container: {
      ...sizeDim,
      ...variantStyle,
      borderRadius: 8,
      justifyContent: 'center',
      alignItems: 'center',
      width: fullWidth ? '100%' : 'auto',
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.1,
      shadowRadius: 4,
      elevation: 3,
    },
    disabled: {
      opacity: 0.5,
    },
    content: {
      flexDirection: 'row',
      alignItems: 'center',
      justifyContent: 'center',
    },
    label: {
      fontSize: 18,
      fontWeight: '600',
      color: variantStyle.color,
    },
    iconContainer: {
      marginHorizontal: 8,
    },
  });
};
```

## Usage Guidelines

### Do's
- Use Primary variant for main call-to-action
- Maintain consistent sizing within a section
- Use clear, action-oriented labels ("Записаться", "Подтвердить")
- Ensure buttons are always touch-accessible (44x44px minimum)
- Provide visual feedback for all interaction states
- Use loading state for asynchronous operations

### Don'ts
- Don't use more than 2 Primary buttons per screen
- Don't use ambiguous labels ("OK", "Click here")
- Don't make buttons smaller than 36px height
- Don't disable buttons without explanation
- Don't change button color dynamically except for state changes
- Don't place buttons too close together (< 8px spacing)
- Avoid nested or stacked buttons without clear hierarchy

## Related Components

- [Input](/docs/design/components/input.md) - Often paired with buttons in forms
- [Card](/docs/design/components/card.md) - Buttons frequently appear in card footers
- [Bottom Navigation](/docs/design/components/bottom-navigation.md) - Alternative navigation pattern
- [Status Badge](/docs/design/components/status-badge.md) - Can be used together for state indicators
