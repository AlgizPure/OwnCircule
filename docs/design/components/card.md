# Card Component

## Overview

The Card component is a flexible container for displaying grouped information and content. It serves as a foundational layout element used throughout OwnCircule for presenting partners, events, user status, and other content sections. Cards use soft rounded corners and subtle shadows to create a sophisticated, elevated appearance.

**Primary Use Cases:**
- Partner profiles and listings
- Event information and booking
- User status displays
- Content containers for related information groups
- Wallet and transaction history

## Anatomy

The Card component consists of the following visual parts:

```
┌────────────────────────────┐
│ ▶ Image/Icon (optional)    │
│                            │
├────────────────────────────┤
│ H3 Title                   │
│ Body Text Description      │
│                            │
│ Meta Information            │
├────────────────────────────┤
│ Button(s) or Action        │
└────────────────────────────┘
```

### Key Elements:
- **Container**: Rounded rectangle with subtle shadow
- **Header**: Optional image or icon area
- **Content**: Title, description, and metadata
- **Footer**: Optional action buttons or controls
- **Dividers**: Subtle separators between sections
- **Spacing**: Consistent 16px padding throughout

## Variants

### 1. Standard Card
- **Background**: White with subtle shadow
- **Border Radius**: 16px
- **Usage**: Default card style for most content
- **Shadow**: `shadowColor: #000, opacity: 0.08, radius: 8px`

### 2. Elevated Card
- **Background**: White with more pronounced shadow
- **Border Radius**: 16px
- **Usage**: Featured content, primary focus items
- **Shadow**: `shadowColor: #000, opacity: 0.12, radius: 12px`

### 3. Status Card
- **Background**: Soft pink (#E8B4BC) or Champagne Beige (#F5F1E8)
- **Border Radius**: 16px
- **Usage**: User status displays, achievements, badges
- **Shadow**: Standard shadow

### 4. Partner Card
- **Header**: Image/icon area (120x120px typical)
- **Content**: Name, description, rating/metadata
- **Footer**: Action button (e.g., "Записаться")
- **Usage**: Partner profiles, listings

### 5. Event Card
- **Header**: Event image
- **Content**: Event name, date/time, location
- **Footer**: "Подробнее" link or booking button
- **Usage**: Event information and discovery

### 6. Expandable Card
- **Indicator**: Chevron icon showing expand state
- **Content**: Collapsible additional details
- **Animation**: Smooth expand/collapse transition
- **Usage**: FAQs, feature lists, detailed information

## States

### Default State
- Full opacity background
- Subtle shadow
- All content visible
- Ready for interaction

### Hover State
- Shadow elevation increases
- Slight scale transform (1.02)
- Cursor indicates interactivity

### Active/Selected State
- Border highlight (2px Tiffany Blue #0ABAB5)
- Shadow elevation increases
- Background opacity slightly increased

### Disabled State
- Background opacity: 60%
- Content opacity: 50%
- Shadow removed or minimized
- No interactive response

### Expanded State (for expandable cards)
- Additional content visible
- Chevron icon rotated 180 degrees
- Container height increases
- Smooth animation over 300ms

### Loading State
- Skeleton placeholder in content area
- Reduced opacity for container
- No interactive response

## Props/API

```typescript
interface CardProps {
  // Layout
  variant?: 'standard' | 'elevated' | 'status' | 'partner' | 'event' | 'expandable';
  header?: React.ReactNode;
  headerImage?: string;
  headerHeight?: number; // default: 120px
  
  // Content
  title?: string;
  subtitle?: string;
  description?: string;
  children?: React.ReactNode;
  
  // Footer
  footer?: React.ReactNode;
  actions?: CardAction[];
  
  // State
  disabled?: boolean; // default: false
  selected?: boolean; // default: false
  expandable?: boolean; // default: false
  expanded?: boolean; // default: false
  onExpandChange?: (expanded: boolean) => void;
  
  // Interaction
  onPress?: () => void;
  
  // Styling
  backgroundColor?: string;
  borderRadius?: number; // default: 16
  shadowOpacity?: number;
  style?: StyleProp<ViewStyle>;
  
  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;
}

interface CardAction {
  label: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
}
```

## Spacing & Sizing

### Padding & Margins
- **Content Padding**: 16px (all sides)
- **Header-Content Gap**: 12px
- **Content-Footer Gap**: 12px
- **Action Button Gap**: 8px
- **Card Margin**: 8px (between cards in a list)

### Size Variants

#### Small Card
- **Width**: 160px (for grids/sidebars)
- **Min Height**: 120px
- **Title Font**: 14px/600
- **Description Font**: 12px/400

#### Medium Card (Default)
- **Width**: Full width or 280px (in layouts)
- **Min Height**: 200px
- **Title Font**: 18px/600
- **Description Font**: 14px/400

#### Large Card
- **Width**: Full width
- **Min Height**: 300px
- **Title Font**: 20px/600
- **Description Font**: 16px/400

### Border Radius
- All variants: 16px (soft, rounded appearance)
- Content sections: 8px for nested elements

### Image Sizing
- **Standard Header Image**: 100% width x 120px height
- **Partner Card Image**: 100% width x 160px height
- **Event Card Image**: 100% width x 180px height
- **Image Aspect Ratio**: Maintained with cover or contain

## Accessibility

### Touch Target
- Minimum 44x44px for interactive areas
- Entire card area is tappable if `onPress` is provided
- Clear focus indicator for keyboard users

### Contrast Ratio
- Title: 13.5:1 (Charcoal on White)
- Description: 7.2:1 (Charcoal on White)
- All text meets WCAG AAA standard

### Screen Reader Support
```typescript
<View
  accessible={true}
  accessibilityLabel={title}
  accessibilityHint={description}
  accessibilityRole="button"
/>
```

### Expandable Cards
- Chevron icon has `accessibilityLabel: "Expand content"`
- State change announces expanded/collapsed status
- Keyboard support with Space/Enter to toggle

## Implementation

### React Native Example

```typescript
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Image,
  Animated,
} from 'react-native';

interface CardProps {
  title: string;
  description?: string;
  headerImage?: string;
  onPress?: () => void;
  children?: React.ReactNode;
  expandable?: boolean;
  variant?: 'standard' | 'elevated' | 'status';
  disabled?: boolean;
}

export const Card: React.FC<CardProps> = ({
  title,
  description,
  headerImage,
  onPress,
  children,
  expandable = false,
  variant = 'standard',
  disabled = false,
}) => {
  const [expanded, setExpanded] = useState(false);
  const [heightAnim] = useState(new Animated.Value(0));

  const toggleExpand = () => {
    setExpanded(!expanded);
    Animated.timing(heightAnim, {
      toValue: expanded ? 0 : 200,
      duration: 300,
      useNativeDriver: false,
    }).start();
  };

  const containerStyle = [
    styles.container,
    styles[`${variant}Shadow`],
    disabled && styles.disabled,
  ];

  return (
    <TouchableOpacity
      style={containerStyle}
      onPress={onPress || (expandable ? toggleExpand : undefined)}
      disabled={disabled || !onPress}
      accessible={true}
      accessibilityLabel={title}
      accessibilityHint={description}
      accessibilityRole="button"
    >
      {headerImage && (
        <Image
          source={{ uri: headerImage }}
          style={styles.headerImage}
        />
      )}

      <View style={styles.contentContainer}>
        <Text style={styles.title}>{title}</Text>
        {description && (
          <Text style={styles.description}>{description}</Text>
        )}
      </View>

      {expandable && (
        <View style={styles.expandToggle}>
          <Text style={styles.chevron}>{expanded ? '▼' : '▶'}</Text>
        </View>
      )}

      {children}

      {expandable && expanded && (
        <Animated.View style={[styles.expandableContent, { height: heightAnim }]}>
          {children}
        </Animated.View>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    borderRadius: 16,
    backgroundColor: '#FFFFFF',
    marginVertical: 8,
    marginHorizontal: 8,
    overflow: 'hidden',
  },
  standardShadow: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 8,
    elevation: 2,
  },
  elevatedShadow: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.12,
    shadowRadius: 12,
    elevation: 4,
  },
  statusShadow: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.06,
    shadowRadius: 8,
    elevation: 2,
  },
  disabled: {
    opacity: 0.6,
  },
  headerImage: {
    width: '100%',
    height: 120,
    resizeMode: 'cover',
  },
  contentContainer: {
    padding: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#2A2D34',
    marginBottom: 8,
  },
  description: {
    fontSize: 14,
    fontWeight: '400',
    color: '#666666',
  },
  expandToggle: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    alignItems: 'flex-end',
  },
  chevron: {
    fontSize: 16,
    color: '#0ABAB5',
  },
  expandableContent: {
    overflow: 'hidden',
    paddingHorizontal: 16,
    paddingBottom: 16,
  },
});
```

## Usage Guidelines

### Do's
- Use cards to group related information
- Provide clear, descriptive titles
- Maintain consistent card sizing within a section
- Use images/icons to enhance visual hierarchy
- Include action buttons only when necessary
- Use elevation to indicate card importance
- Provide adequate spacing between cards

### Don'ts
- Don't overcrowd card content
- Don't use more than 3 action buttons per card
- Don't mix multiple card variants randomly
- Don't place cards too close together
- Don't make interactive cards visually identical to static content
- Don't use cards for simple lists of items without context
- Avoid deep nesting of cards within cards

## Related Components

- [Button](/docs/design/components/button.md) - Used in card footers and actions
- [Status Badge](/docs/design/components/status-badge.md) - Often displayed in status cards
- [Bottom Navigation](/docs/design/components/bottom-navigation.md) - Complements card-based layouts
- [Input](/docs/design/components/input.md) - Can be included in card content for forms
- [QR Code Display](/docs/design/components/qr-code-display.md) - Often placed in cards for wallet display
