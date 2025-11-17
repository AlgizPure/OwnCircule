# Status Badge Component

## Overview

The Status Badge component displays user status, achievement levels, and point accumulation in a visually distinctive format. It features soft pink coloring (#E8B4BC), a circular flower icon, and typographic hierarchy for clear information display. Status badges are typically used in user profiles, cards, and wallet displays to show membership tier, loyalty status, and collected points.

**Primary Use Cases:**
- Displaying user membership tiers (Bronze, Silver, Gold)
- Showing achievement status and levels
- Presenting loyalty point balances
- Indicating special membership status
- Visual status indicators in cards and profiles

## Anatomy

The Status Badge component consists of the following visual parts:

```
┌─────────────────────────┐
│  ◉ Flower Icon         │ ← Circular Icon (24x24px)
├─────────────────────────┤
│  Бронза                 │ ← Status Label
│  500 Points             │ ← Points/Value (secondary)
├─────────────────────────┤
│ [Background]            │
└─────────────────────────┘
```

### Key Elements:
- **Background**: Soft pink (#E8B4BC) or tinted color
- **Icon**: Circular flower or achievement icon (24x24px)
- **Status Label**: Tier name (Бронза, Серебро, Золото)
- **Value Display**: Points, percentage, or secondary text
- **Border Radius**: 16px for soft, rounded appearance
- **Shadow**: Subtle shadow for elevation

## Variants

### 1. Bronze Status Badge
- **Background**: Soft pink (#E8B4BC)
- **Icon**: Bronze-toned flower/achievement icon
- **Label**: "Бронза" (Bronze)
- **Value**: Point count (e.g., "500 Points")
- **Usage**: Entry-level membership tier

### 2. Silver Status Badge
- **Background**: Light silver-gray (#D3D3D3) or lighter variant
- **Icon**: Silver-toned flower/achievement icon
- **Label**: "Серебро" (Silver)
- **Value**: Point count (e.g., "1500 Points")
- **Usage**: Mid-level membership tier

### 3. Gold Status Badge
- **Background**: Champagne Gold (#D4AF37) at reduced opacity
- **Icon**: Gold-toned flower/achievement icon
- **Label**: "Золото" (Gold)
- **Value**: Point count (e.g., "5000+ Points")
- **Usage**: Premium membership tier

### 4. Compact Badge
- **Size**: 120x120px (smaller version)
- **Icon Only**: Circular icon without text background
- **Usage**: Avatar overlays, small displays
- **Position**: Top-right of cards or avatars

### 5. Progress Badge
- **Background**: Gradient fill indicating progress
- **Ring**: Circular progress indicator
- **Label**: Current level and progress percentage
- **Usage**: Level progression display

### 6. Achievement Badge
- **Background**: Distinct color per achievement type
- **Icon**: Achievement-specific symbol
- **Label**: Achievement name
- **Usage**: Milestone and accomplishment display

## States

### Default State
- Full opacity background
- Icon clearly visible
- Text readable
- No animation

### Hover State
- Shadow elevation increases
- Slight scale transform (1.05)
- Cursor indicates interactivity

### Active/Selected State
- Border highlight (2px Tiffany Blue #0ABAB5)
- Shadow elevation increases
- Background opacity slightly increased

### Disabled State
- Background opacity: 50%
- Text opacity: 60%
- Icon opacity: 60%
- No interactive response

### Upgrade Available State
- Animated pulse effect
- Highlight color
- Badge indicator showing upgrade path
- Optional glow effect

### Locked State
- Reduced opacity (40%)
- Lock icon overlay
- "Locked" or requirement text
- Grayed appearance

## Props/API

```typescript
interface StatusBadgeProps {
  // Content
  status: 'bronze' | 'silver' | 'gold' | 'achievement';
  label: string;
  points?: number;
  icon?: React.ReactNode;
  
  // Display
  variant?: 'full' | 'compact' | 'progress' | 'achievement';
  size?: 'small' | 'medium' | 'large'; // default: 'medium'
  
  // Progress
  currentLevel?: number;
  maxLevel?: number;
  progressPercentage?: number;
  
  // State
  disabled?: boolean; // default: false
  locked?: boolean; // default: false
  upgradeAvailable?: boolean; // default: false
  
  // Interaction
  onPress?: () => void;
  
  // Styling
  backgroundColor?: string;
  textColor?: string;
  variant?: 'default' | 'animated';
  
  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;
  
  // Styling overrides
  style?: StyleProp<ViewStyle>;
  labelStyle?: StyleProp<TextStyle>;
}
```

## Spacing & Sizing

### Container Dimensions

#### Small Badge
- **Width**: 100px
- **Height**: 100px
- **Border Radius**: 12px
- **Padding**: 12px

#### Medium Badge (Default)
- **Width**: 140px
- **Height**: 140px
- **Border Radius**: 16px
- **Padding**: 16px

#### Large Badge
- **Width**: 180px
- **Height**: 180px
- **Border Radius**: 16px
- **Padding**: 20px

### Icon Sizing
- **Small Badge Icon**: 20x20px
- **Medium Badge Icon**: 24x24px
- **Large Badge Icon**: 32x32px

### Text Sizing
- **Status Label Font**: 16px/600
- **Points/Value Font**: 12px/400
- **Compact Badge Font**: 14px/600

### Spacing
- **Icon to Label**: 8px
- **Label to Points**: 4px
- **Content Padding**: 16px (all sides)

### Compact Variant
- **Diameter**: 56px (small), 72px (medium), 88px (large)
- **Icon Only**: No text background

## Accessibility

### Touch Target
- Minimum 44x44px tap area per WCAG 2.1
- Full badge dimensions provide adequate hit area
- Circular badges: 72px+ diameter for mobile

### Contrast Ratio
- Label on pink background: 3.8:1 (meets WCAG AA for large text)
- Points text: 4.2:1
- Icon color: High contrast (icon-specific)

### Screen Reader Support
```typescript
<TouchableOpacity
  accessible={true}
  accessibilityLabel={`${label} badge`}
  accessibilityHint={`Status level ${status} with ${points} points`}
  accessibilityRole="button"
/>
```

### Color Independence
- Status conveyed through text label, not color alone
- Icon provides additional visual distinction
- Tier level clearly labeled (not reliant on color)

### Keyboard Navigation
- Focusable if interactive (onPress provided)
- Activatable with Enter key
- Clear focus indicator (2px outline)

## Implementation

### React Native Example

```typescript
import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';

type StatusType = 'bronze' | 'silver' | 'gold' | 'achievement';

interface StatusBadgeProps {
  status: StatusType;
  label: string;
  points?: number;
  icon?: React.ReactNode;
  size?: 'small' | 'medium' | 'large';
  variant?: 'full' | 'compact';
  locked?: boolean;
  disabled?: boolean;
  onPress?: () => void;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({
  status,
  label,
  points,
  icon,
  size = 'medium',
  variant = 'full',
  locked = false,
  disabled = false,
  onPress,
}) => {
  const styles = getStyles(status, size, variant);

  const statusColors = {
    bronze: '#E8B4BC',
    silver: '#D3D3D3',
    gold: '#D4AF37',
    achievement: '#F5B6D9',
  };

  return (
    <TouchableOpacity
      style={[
        styles.container,
        { backgroundColor: statusColors[status] },
        disabled && styles.disabled,
        locked && styles.locked,
      ]}
      onPress={onPress}
      disabled={disabled || locked}
      accessible={true}
      accessibilityLabel={`${label} badge`}
      accessibilityHint={`Status level with ${points || 0} points`}
      accessibilityRole={onPress ? 'button' : 'image'}
    >
      {variant === 'full' ? (
        <View style={styles.content}>
          {icon && <View style={styles.iconContainer}>{icon}</View>}
          <Text style={styles.label}>{label}</Text>
          {points !== undefined && (
            <Text style={styles.points}>{points} Points</Text>
          )}
        </View>
      ) : (
        <View style={styles.compactContent}>
          {icon && <View style={styles.compactIcon}>{icon}</View>}
        </View>
      )}

      {locked && (
        <View style={styles.lockOverlay}>
          <Text style={styles.lockIcon}>🔒</Text>
        </View>
      )}
    </TouchableOpacity>
  );
};

const getStyles = (status: StatusType, size: string, variant: string) => {
  const sizeConfig = {
    small: { width: 100, height: 100, padding: 12, borderRadius: 12 },
    medium: { width: 140, height: 140, padding: 16, borderRadius: 16 },
    large: { width: 180, height: 180, padding: 20, borderRadius: 16 },
  };

  const config = sizeConfig[size as keyof typeof sizeConfig];

  return StyleSheet.create({
    container: {
      ...config,
      justifyContent: 'center',
      alignItems: 'center',
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.1,
      shadowRadius: 8,
      elevation: 3,
    },
    disabled: {
      opacity: 0.5,
    },
    locked: {
      opacity: 0.6,
    },
    content: {
      alignItems: 'center',
      justifyContent: 'center',
      gap: 8,
    },
    compactContent: {
      alignItems: 'center',
      justifyContent: 'center',
    },
    iconContainer: {
      width: size === 'small' ? 20 : size === 'large' ? 32 : 24,
      height: size === 'small' ? 20 : size === 'large' ? 32 : 24,
    },
    compactIcon: {
      width: size === 'small' ? 28 : size === 'large' ? 40 : 32,
      height: size === 'small' ? 28 : size === 'large' ? 40 : 32,
    },
    label: {
      fontSize: 16,
      fontWeight: '600',
      color: '#2A2D34',
      textAlign: 'center',
    },
    points: {
      fontSize: 12,
      fontWeight: '400',
      color: '#666666',
      textAlign: 'center',
    },
    lockOverlay: {
      position: 'absolute',
      width: '100%',
      height: '100%',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: 'rgba(0, 0, 0, 0.2)',
    },
    lockIcon: {
      fontSize: 24,
    },
  });
};
```

## Usage Guidelines

### Do's
- Use consistent badge sizes within a section
- Clearly label status levels (Бронза, Серебро, Золото)
- Show point totals to motivate engagement
- Use distinct colors for each tier
- Include appropriate icons for visual distinction
- Position badges prominently in profile/wallet
- Update badges when users achieve new levels

### Don'ts
- Don't stack multiple badges without spacing
- Don't use badges for status that isn't related to tiers/achievements
- Don't hide tier information (always label)
- Don't use only color to distinguish tiers
- Don't make badges too small (< 100px width)
- Don't display outdated achievement information
- Avoid changing badge appearance randomly

## Related Components

- [Card](/docs/design/components/card.md) - Badges often displayed in status cards
- [Button](/docs/design/components/button.md) - Links to tier upgrade information
- [Bottom Navigation](/docs/design/components/bottom-navigation.md) - Wallet tab shows badges
- [QR Code Display](/docs/design/components/qr-code-display.md) - Often displayed together with status badge
