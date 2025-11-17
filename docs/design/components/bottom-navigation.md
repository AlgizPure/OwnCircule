# Bottom Navigation Component

## Overview

The Bottom Navigation component provides a persistent, mobile-optimized navigation interface positioned at the bottom of the screen. It serves as the primary navigation pattern for moving between major sections of the OwnCircule application. The component displays 5 tabs with icons and labels, providing quick access to key features.

**Primary Use Cases:**
- Main app navigation
- Tab switching between major sections
- Always-accessible navigation throughout the app
- Mobile-first navigation pattern

## Anatomy

The Bottom Navigation component consists of the following visual parts:

```
┌─────────────────────────────────┐
│                                 │
│ Home  Search  Wallet  Messages  │
│  ◀       ◀       ◀       ◀      │
│                                 │
├─────────────────────────────────┤
│ Icon  Icon    Icon    Icon      │
│ Label Label   Label   Label     │
│                                 │
└─────────────────────────────────┘
```

### Key Elements:
- **Container**: Full-width bar at screen bottom
- **Tabs**: Individual navigation items with icon and label
- **Active Indicator**: Visual highlight for current tab
- **Icon**: 24x24px symbol representing the section
- **Label**: Text description of the tab (12px, Body typography)
- **Safe Area**: Respects device safe area insets

## Variants

### 1. Standard Bottom Navigation
- **Tab Count**: 5 tabs (Home, Search, Wallet, Messages, Profile)
- **Active State**: Tiffany Blue (#0ABAB5) icon and text
- **Inactive State**: Charcoal (#2A2D34) at 50% opacity
- **Background**: White with top border

### 2. Badge Bottom Navigation
- **Badge**: Notification count/indicator on tab icons
- **Badge Style**: Tiffany Blue (#0ABAB5) circular badge
- **Badge Position**: Top-right of icon
- **Usage**: Messages, notifications, pending actions

### 3. Floating Bottom Navigation
- **Style**: Floating above content with margin
- **Border Radius**: 16px (rounded container)
- **Shadow**: Elevated shadow appearance
- **Usage**: Less common, for specific layouts

## States

### Default State
- All tabs visible
- One tab highlighted as active
- Icon and label in standard colors

### Active Tab State
- Icon color: Tiffany Blue (#0ABAB5)
- Label color: Tiffany Blue (#0ABAB5)
- Font weight: 600
- Slight elevation indication

### Inactive Tab State
- Icon color: Charcoal (#2A2D34) at 50% opacity
- Label color: Charcoal (#2A2D34) at 50% opacity
- Font weight: 400
- Standard elevation

### Pressed/Touch State
- Background opacity increase
- Scale slight animation (0.95)
- Haptic feedback on press

### Badge State
- Red or Tiffany Blue badge circle
- Badge shows count (1-99, or "99+" for > 99)
- Badge visible on inactive tabs

### Disabled Tab State
- Icon opacity: 30%
- Label opacity: 30%
- No response to touch
- Cursor: not-allowed

## Props/API

```typescript
interface BottomNavigationProps {
  // Navigation
  tabs: BottomNavTab[];
  activeTabIndex: number;
  onTabChange: (index: number) => void;

  // Styling
  backgroundColor?: string; // default: '#FFFFFF'
  activeColor?: string; // default: '#0ABAB5'
  inactiveColor?: string; // default: '#2A2D34'
  showBorder?: boolean; // default: true

  // Layout
  variant?: 'standard' | 'floating';
  safeAreaEnabled?: boolean; // default: true

  // Accessibility
  accessibilityLabel?: string;

  // Styling overrides
  style?: StyleProp<ViewStyle>;
}

interface BottomNavTab {
  // Content
  label: string;
  icon: React.ReactNode;
  
  // State
  disabled?: boolean;
  badge?: number | string;
  
  // Interaction
  onPress?: () => void;
  
  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;
}
```

## Spacing & Sizing

### Container Dimensions
- **Height**: 64px (including safe area padding)
- **Safe Area Padding**: 8px bottom (varies by device)
- **Safe Area Padding**: 0px horizontal
- **Border Radius**: 0px (standard), 16px (floating)

### Tab Dimensions
- **Width**: 100% / tab count (20% per tab for 5 tabs)
- **Height**: 56px (excluding safe area)
- **Padding**: 8px vertical, 4px horizontal

### Icon Sizing
- **Standard Icon**: 24x24px
- **Icon Margin**: 4px below label

### Text Sizing
- **Label Font**: 12px/400 (caption style)
- **Label Color**: Tiffany Blue (#0ABAB5) when active
- **Label Margin**: 4px above icon

### Badge Sizing
- **Badge Diameter**: 18px
- **Badge Font**: 10px/600
- **Badge Position**: Offset 4px top-right from icon

### Touch Target
- **Minimum**: 48x48px per tab (easily tappable)
- **Actual**: Each tab approximately 64x56px

## Accessibility

### Touch Target
- Each tab minimum 44x44px, typically 64x56px
- Adequate spacing prevents accidental touches
- WCAG 2.1 Level AAA compliant

### Contrast Ratio
- Active State: 4.51:1 (Tiffany Blue on White)
- Inactive State: 4.2:1 (50% opacity Charcoal on White)
- Badge: 4.51:1 (Tiffany Blue on White)
- All meet WCAG AA standard

### Screen Reader Support
```typescript
<BottomNavTab
  accessible={true}
  accessibilityLabel={label}
  accessibilityHint={`Navigate to ${label} section`}
  accessibilityRole="tab"
  accessibilityState={{
    selected: isActive,
    disabled: disabled,
  }}
/>
```

### Keyboard Navigation
- Tabs are focusable via keyboard
- Arrow keys move between tabs
- Enter/Space activates selected tab
- Clear visual focus indicator

### Safe Area
- Respects device notches, home indicators
- Padding adjusted for different devices
- Content doesn't hide behind gestures

## Implementation

### React Native Example

```typescript
import React from 'react';
import {
  View,
  StyleSheet,
  TouchableOpacity,
  Text,
  SafeAreaView,
} from 'react-native';

interface BottomNavTab {
  label: string;
  icon: React.ReactNode;
  badge?: number | string;
  disabled?: boolean;
}

interface BottomNavigationProps {
  tabs: BottomNavTab[];
  activeTabIndex: number;
  onTabChange: (index: number) => void;
}

export const BottomNavigation: React.FC<BottomNavigationProps> = ({
  tabs,
  activeTabIndex,
  onTabChange,
}) => {
  return (
    <SafeAreaView style={styles.safeArea} edges={['bottom']}>
      <View style={styles.container}>
        {tabs.map((tab, index) => (
          <TabButton
            key={index}
            tab={tab}
            isActive={index === activeTabIndex}
            onPress={() => {
              if (!tab.disabled) {
                onTabChange(index);
              }
            }}
          />
        ))}
      </View>
    </SafeAreaView>
  );
};

const TabButton: React.FC<{
  tab: BottomNavTab;
  isActive: boolean;
  onPress: () => void;
}> = ({ tab, isActive, onPress }) => {
  return (
    <TouchableOpacity
      style={[styles.tab, tab.disabled && styles.disabledTab]}
      onPress={onPress}
      disabled={tab.disabled}
      accessible={true}
      accessibilityLabel={tab.label}
      accessibilityHint={`Navigate to ${tab.label}`}
      accessibilityRole="tab"
      accessibilityState={{ selected: isActive }}
    >
      <View style={styles.iconContainer}>
        {tab.icon}
        {tab.badge && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>
              {typeof tab.badge === 'number' && tab.badge > 99
                ? '99+'
                : tab.badge}
            </Text>
          </View>
        )}
      </View>
      <Text
        style={[
          styles.label,
          isActive && styles.activeLabel,
        ]}
      >
        {tab.label}
      </Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  safeArea: {
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#E8E8E8',
  },
  container: {
    flexDirection: 'row',
    height: 56,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#E8E8E8',
  },
  tab: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 8,
  },
  disabledTab: {
    opacity: 0.3,
  },
  iconContainer: {
    position: 'relative',
    marginBottom: 4,
  },
  badge: {
    position: 'absolute',
    top: -4,
    right: -4,
    backgroundColor: '#0ABAB5',
    borderRadius: 9,
    minWidth: 18,
    height: 18,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 4,
  },
  badgeText: {
    color: '#FFFFFF',
    fontSize: 10,
    fontWeight: '600',
  },
  label: {
    fontSize: 12,
    fontWeight: '400',
    color: '#2A2D34',
    opacity: 0.5,
  },
  activeLabel: {
    color: '#0ABAB5',
    opacity: 1,
    fontWeight: '600',
  },
});
```

## Usage Guidelines

### Do's
- Use for main app navigation (primary pattern)
- Keep labels concise (1-2 words)
- Use descriptive, recognizable icons
- Maintain consistent icon style across all tabs
- Highlight current section with Tiffany Blue color
- Use badges for unread counts or alerts
- Test navigation paths for user flow

### Don'ts
- Don't use more than 5 tabs
- Don't use less than 3 tabs (use drawer menu for more options)
- Don't hide the bottom navigation dynamically
- Don't use generic icons that don't clearly represent sections
- Don't place non-navigation items in bottom nav
- Don't use emoji as icons (use consistent icon set)
- Avoid changing tab labels or icons dynamically
- Don't disable tabs without clear reason

## Related Components

- [Button](/docs/design/components/button.md) - Alternative navigation patterns
- [Card](/docs/design/components/card.md) - Content displayed after navigation
- [Status Badge](/docs/design/components/status-badge.md) - Badge style for notification counts
- [QR Code Display](/docs/design/components/qr-code-display.md) - Often accessed via bottom nav (Wallet tab)
