# Component Documentation Index

This directory contains comprehensive documentation for OwnCircule's core UI components.

## Components

### 1. Button
**File:** `/docs/design/components/button.md`
- **Purpose:** Primary interactive element for triggering actions
- **Key Variants:** Primary, Secondary, Accent, Tertiary
- **States:** Default, Hover, Active, Disabled, Loading, Focus
- **Size Variants:** Small (36px), Medium (44px), Large (52px)
- **Primary Color:** Tiffany Blue (#0ABAB5)
- **Implementation:** React Native with TypeScript

### 2. Card
**File:** `/docs/design/components/card.md`
- **Purpose:** Flexible container for grouped information
- **Key Variants:** Standard, Elevated, Status, Partner, Event, Expandable
- **Border Radius:** 16px (soft, rounded appearance)
- **Padding:** 16px (consistent throughout)
- **Shadow:** Subtle (standard) to pronounced (elevated)
- **Usage:** Partner profiles, events, status displays, wallet content
- **Implementation:** React Native with state management for expandable cards

### 3. Bottom Navigation
**File:** `/docs/design/components/bottom-navigation.md`
- **Purpose:** Primary mobile navigation pattern
- **Tab Count:** 5 tabs (Home, Search, Wallet, Messages, Profile)
- **Container Height:** 56px + safe area padding
- **Active Indicator:** Tiffany Blue (#0ABAB5)
- **States:** Active, Inactive, Disabled, Badge (notification)
- **Badge Support:** Red/Tiffany Blue badges with count display
- **Implementation:** React Native with SafeAreaView

### 4. QR Code Display
**File:** `/docs/design/components/qr-code-display.md`
- **Purpose:** Scannable QR code presentation for wallet/membership
- **Key Variants:** Standard, Compact, Large/Featured, Branded, Floating
- **QR Code Size:** 200x200px (small), 280x280px (medium), 360x360px (large)
- **Container:** White card with 16px border radius and subtle shadow
- **Coloring:** Black (#000000) on white for optimal scannability
- **Features:** Share, Download, Expandable full-screen view
- **Implementation:** React Native with QRCode library

### 5. Status Badge
**File:** `/docs/design/components/status-badge.md`
- **Purpose:** Display user membership tiers and achievements
- **Tier System:** Bronze, Silver, Gold, Achievements
- **Badge Colors:** Soft pink (#E8B4BC), Silver-gray, Champagne Gold (#D4AF37)
- **Key Elements:** Circular icon, status label, points display
- **Sizes:** Small (100px), Medium (140px), Large (180px)
- **Icon:** Flower or achievement symbol (24-32px)
- **States:** Default, Hover, Active, Disabled, Locked, Upgrade Available
- **Implementation:** React Native with TypeScript interfaces

### 6. Input
**File:** `/docs/design/components/input.md`
- **Purpose:** Text input for forms, search, and user data entry
- **Key Variants:** Text, Email, Password, Numeric, Phone, Search, Textarea
- **Background:** Champagne Beige (#F5F1E8)
- **Border Radius:** 8px
- **Size Variants:** Small (36px), Medium (44px), Large (52px)
- **Features:** Labels, helper text, error messages, clear button, password toggle
- **States:** Default, Focus, Active, Hover, Disabled, Error, Loading, Success
- **Keyboard Support:** Automatic keyboard type selection
- **Implementation:** React Native TextInput with validation

## Color Palette

- **Primary:** Tiffany Blue (#0ABAB5)
- **Background:** Champagne Beige (#F5F1E8)
- **Accent:** Champagne Gold (#D4AF37)
- **Text:** Charcoal (#2A2D34)
- **Error:** Red (#D32F2F)
- **Success:** Green (#4CAF50)

## Typography Scale

- **H3 (Headings):** 18px/600 - Used for card titles
- **Body (Default):** 14px/400 - Descriptions and main text
- **Caption (Small):** 12px/400 - Metadata and helper text
- **Large Text:** 16-20px/600 - Prominent headings

## Spacing System (8px Grid)

- **Padding/Margins:** 4px, 8px, 12px, 16px, 20px, 24px, 32px
- **Standard Internal Padding:** 16px
- **Standard Gap Between Elements:** 8px
- **Card/Container Spacing:** 8px (margins)

## Accessibility Standards

All components meet:
- **WCAG 2.1 Level AAA** contrast requirements
- **Minimum 44x44px** touch target sizes
- **Keyboard navigation** support
- **Screen reader** compatibility with proper labels and hints
- **Focus indicators** for keyboard users

## Component Relationships

```
Button
├── Used in Card footers
├── Used in Input submission
└── Used in Navigation

Card
├── Contains Button, Input, Status Badge
├── Displays QR Code
└── Primary content container

Bottom Navigation
├── Links to major app sections
└── Often leads to card-based layouts

QR Code Display
├── Displayed in Cards
├── Associated with Status Badge
└── Accessed via Bottom Navigation (Wallet tab)

Status Badge
├── Displayed in Cards
├── Shows with QR Code in wallet
└── Updated via Button interactions

Input
├── Contained in Cards
├── Submitted via Button
└── Styled with Status Badge for validation
```

## Implementation Notes

- All components use React Native with TypeScript
- StyleSheet for performance optimization
- Accessibility features built-in
- State management integrated where needed
- Dark mode considerations included
- Safe area aware components

## Related Resources

- Brand Guidelines: `/docs/design/brand.md`
- Design System: `/docs/design/system.md`
- Spacing Guidelines: `/docs/design/spacing.md`
- Accessibility Guide: `/docs/design/accessibility.md`
