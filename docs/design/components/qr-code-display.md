# QR Code Display Component

## Overview

The QR Code Display component presents a scannable QR code within a visually polished container. It's primarily used in the wallet section to enable users to share their loyalty or membership information with partners. The component combines functional QR code generation with elegant design, featuring a white background card with rounded corners and a black QR code for optimal scannability.

**Primary Use Cases:**
- Displaying user loyalty/membership QR codes
- Wallet screen integration
- Partner verification and check-in processes
- Share-to-vendor functionality
- Contactless transactions

## Anatomy

The QR Code Display component consists of the following visual parts:

```
┌─────────────────────────────┐
│     Wallet / Profile        │ ← Header (optional)
├─────────────────────────────┤
│                             │
│    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      │
│    █ █ ▄▄▄▄ █ ▄▄▄ █        │
│    █ █ █    █ █ █ █        │
│    █ █ ▀▀▀▀ █ ▀▀▀ █        │
│    █ █▄▄▄▄▄▄█▄▄▄▄▄█        │ ← QR Code (black matrix)
│    █             █          │
│    █▄▄▄▄▄▄▄▄▄▄▄▄▄█        │
│                             │
├─────────────────────────────┤
│ USER ID or Description      │
│ Optional metadata/info      │
├─────────────────────────────┤
│   [ Share ]  [ Download ]   │ ← Action buttons (optional)
└─────────────────────────────┘
```

### Key Elements:
- **Container**: Rounded card with white background (16px border radius)
- **QR Code Matrix**: Black (#000000) scannable code on white background
- **Padding**: 20px around QR code for scannability
- **Header**: Optional title/label area
- **Footer**: Optional metadata, user ID, or description
- **Actions**: Optional share and download buttons
- **Shadow**: Subtle shadow for elevation

## Variants

### 1. Standard QR Display
- **Background**: White card (#FFFFFF)
- **QR Coloring**: Black (#000000) on white
- **Size**: 280x280px (code) + padding
- **Usage**: Default wallet display

### 2. Compact QR Display
- **Background**: White card (#FFFFFF)
- **QR Coloring**: Black (#000000) on white
- **Size**: 200x200px (code) + padding
- **Usage**: Secondary displays, smaller screens

### 3. Large/Featured QR Display
- **Background**: White card (#FFFFFF)
- **QR Coloring**: Black (#000000) on white
- **Size**: 360x360px (code) + padding
- **Usage**: Primary wallet view, full screen

### 4. QR with Branding
- **Header**: Logo or partner branding area
- **QR Code**: 240x240px (slightly smaller)
- **Footer**: User ID, points, status
- **Usage**: Partner-specific QR codes

### 5. Floating QR Display
- **Position**: Floating action button style
- **Size**: Compact (240x240px)
- **Animation**: Appears on demand
- **Usage**: Quick access from any screen

## States

### Default State
- QR code fully visible and scannable
- Clear contrast between code and background
- All optional elements displayed

### Loading State
- Skeleton placeholder for QR code area
- Reduced opacity container
- Loading indicator in center

### Error State
- Error icon displayed
- Retry button visible
- Informational message
- Neutral/gray coloring

### Expanded State
- Larger QR code for full-screen view
- Darker background overlay
- Close button visible
- Share/download buttons accessible

### Downloaded/Copied State
- Brief confirmation message
- Visual feedback (checkmark icon)
- Temporary state (auto-dismisses after 2s)

### Share Active State
- Share menu visible
- Dimmed background
- Multiple platform options

## Props/API

```typescript
interface QRCodeDisplayProps {
  // Content
  qrValue: string; // The data to encode in QR code
  title?: string;
  subtitle?: string;
  userID?: string;
  
  // Sizing
  size?: 'small' | 'medium' | 'large'; // default: 'medium'
  qrCodeSize?: number; // default: 280 (in pixels)
  
  // Styling
  backgroundColor?: string; // default: '#FFFFFF'
  qrColor?: string; // default: '#000000'
  variant?: 'standard' | 'compact' | 'featured' | 'branded';
  
  // Actions
  showActions?: boolean; // default: true
  onShare?: () => void;
  onDownload?: () => void;
  
  // State
  isLoading?: boolean; // default: false
  error?: string | null;
  onRetry?: () => void;
  
  // Interaction
  expandable?: boolean; // default: true
  onExpand?: (expanded: boolean) => void;
  
  // Styling overrides
  style?: StyleProp<ViewStyle>;
  containerStyle?: StyleProp<ViewStyle>;
  
  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;
}
```

## Spacing & Sizing

### Container Dimensions

#### Small (Compact)
- **Total Width**: 240px
- **Total Height**: 280px (with actions)
- **QR Code Size**: 200x200px
- **Padding**: 20px
- **Border Radius**: 12px

#### Medium (Default)
- **Total Width**: 320px
- **Total Height**: 380px (with actions)
- **QR Code Size**: 280x280px
- **Padding**: 20px
- **Border Radius**: 16px

#### Large (Featured)
- **Total Width**: 360px (or full width - 32px)
- **Total Height**: 480px (with actions)
- **QR Code Size**: 360x360px
- **Padding**: 24px
- **Border Radius**: 16px

### Internal Spacing
- **Header to QR**: 16px gap
- **QR to Footer**: 16px gap
- **Footer to Actions**: 12px gap
- **Action Button Gap**: 8px
- **QR Code Padding**: 20px (white space around code)

### Icon/Text Sizing
- **Title Font**: 16px/600 (optional header)
- **Subtitle Font**: 14px/400 (optional)
- **User ID Font**: 12px/600 (metadata)
- **Error Text Font**: 14px/400
- **Action Button Size**: 44x44px minimum

## Accessibility

### Contrast Ratio
- QR Code: Infinite (pure black on white)
- Text on white: 7.2:1 minimum (Charcoal text)
- All elements meet WCAG AAA standard

### Touch Targets
- Entire card is tappable for expansion (44x44px minimum)
- Action buttons: 44x44px minimum
- Adequate spacing around interactive elements

### Screen Reader Support
```typescript
<View
  accessible={true}
  accessibilityLabel="QR Code for wallet or membership"
  accessibilityHint="Double tap to expand or share with partner"
  accessibilityRole="image"
>
```

### Alt Text
- QR codes should have text alternative (user ID, membership number)
- Screen reader announces: "QR code for [user identifier]"
- If expandable: "Double tap to view full screen"

### Keyboard Navigation
- Focusable via Tab key
- Expandable with Enter/Space
- Share/Download buttons accessible via keyboard
- Close button visible when expanded

### Color Independence
- QR code functionality doesn't depend on color
- High contrast (black/white) ensures scanning reliability
- Optional coloring (colored backgrounds) doesn't break scannability

## Implementation

### React Native Example

```typescript
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Share,
  ActivityIndicator,
  Modal,
} from 'react-native';
import QRCode from 'react-native-qr-code-svg';

interface QRCodeDisplayProps {
  qrValue: string;
  title?: string;
  userID?: string;
  size?: 'small' | 'medium' | 'large';
  onShare?: () => void;
  onDownload?: () => void;
  isLoading?: boolean;
  error?: string | null;
}

export const QRCodeDisplay: React.FC<QRCodeDisplayProps> = ({
  qrValue,
  title = 'Your QR Code',
  userID,
  size = 'medium',
  onShare,
  onDownload,
  isLoading = false,
  error = null,
}) => {
  const [expanded, setExpanded] = useState(false);
  const [copied, setCopied] = useState(false);

  const sizeConfig = {
    small: { qr: 200, containerWidth: 240, padding: 20 },
    medium: { qr: 280, containerWidth: 320, padding: 20 },
    large: { qr: 360, containerWidth: '100%', padding: 24 },
  };

  const config = sizeConfig[size];

  const handleShare = async () => {
    try {
      await Share.share({
        message: `Scan my QR code: ${qrValue}`,
        title: title,
      });
      onShare?.();
    } catch (error) {
      console.error('Share error:', error);
    }
  };

  const handleCopy = () => {
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (isLoading) {
    return (
      <View style={[styles.container, { width: config.containerWidth }]}>
        <ActivityIndicator size="large" color="#0ABAB5" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={[styles.container, styles.error, { width: config.containerWidth }]}>
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity style={styles.retryButton}>
          <Text style={styles.retryText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <>
      <TouchableOpacity
        style={[styles.container, { width: config.containerWidth }]}
        onPress={() => setExpanded(true)}
        accessible={true}
        accessibilityLabel="QR Code"
        accessibilityHint="Double tap to expand"
      >
        {title && <Text style={styles.title}>{title}</Text>}

        <View style={styles.qrContainer}>
          <QRCode
            value={qrValue}
            size={config.qr}
            color="#000000"
            backgroundColor="#FFFFFF"
          />
        </View>

        {userID && <Text style={styles.userId}>{userID}</Text>}

        <View style={styles.actions}>
          <TouchableOpacity
            style={styles.actionButton}
            onPress={handleShare}
            accessible={true}
            accessibilityLabel="Share QR code"
          >
            <Text style={styles.actionText}>Share</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.actionButton}
            onPress={onDownload || handleCopy}
            accessible={true}
            accessibilityLabel="Download or copy QR code"
          >
            <Text style={styles.actionText}>
              {copied ? 'Copied!' : 'Download'}
            </Text>
          </TouchableOpacity>
        </View>
      </TouchableOpacity>

      {/* Expanded View Modal */}
      <Modal
        visible={expanded}
        transparent={true}
        animationType="fade"
      >
        <View style={styles.expandedOverlay}>
          <View style={styles.expandedContainer}>
            <TouchableOpacity
              style={styles.closeButton}
              onPress={() => setExpanded(false)}
            >
              <Text style={styles.closeText}>✕</Text>
            </TouchableOpacity>

            <QRCode
              value={qrValue}
              size={360}
              color="#000000"
              backgroundColor="#FFFFFF"
            />

            {userID && <Text style={styles.expandedUserId}>{userID}</Text>}

            <View style={styles.expandedActions}>
              <TouchableOpacity
                style={styles.expandedActionButton}
                onPress={handleShare}
              >
                <Text style={styles.expandedActionText}>Share</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.expandedActionButton}
                onPress={onDownload}
              >
                <Text style={styles.expandedActionText}>Download</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  title: {
    fontSize: 16,
    fontWeight: '600',
    color: '#2A2D34',
    marginBottom: 16,
  },
  qrContainer: {
    backgroundColor: '#FFFFFF',
    padding: 8,
    borderRadius: 8,
  },
  userId: {
    fontSize: 12,
    fontWeight: '600',
    color: '#666666',
    marginTop: 16,
  },
  actions: {
    flexDirection: 'row',
    marginTop: 16,
    gap: 8,
  },
  actionButton: {
    flex: 1,
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: '#0ABAB5',
    borderRadius: 8,
    alignItems: 'center',
  },
  actionText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '600',
  },
  error: {
    justifyContent: 'center',
    backgroundColor: '#F5F1E8',
  },
  errorText: {
    color: '#D32F2F',
    fontSize: 14,
    marginBottom: 12,
    textAlign: 'center',
  },
  retryButton: {
    paddingVertical: 8,
    paddingHorizontal: 16,
    backgroundColor: '#0ABAB5',
    borderRadius: 6,
  },
  retryText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: '600',
  },
  expandedOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 16,
  },
  expandedContainer: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
    width: '100%',
  },
  closeButton: {
    position: 'absolute',
    top: 12,
    right: 12,
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#F5F1E8',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 10,
  },
  closeText: {
    fontSize: 20,
    color: '#2A2D34',
  },
  expandedUserId: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666666',
    marginTop: 20,
  },
  expandedActions: {
    flexDirection: 'row',
    marginTop: 20,
    gap: 8,
    width: '100%',
  },
  expandedActionButton: {
    flex: 1,
    paddingVertical: 12,
    backgroundColor: '#0ABAB5',
    borderRadius: 8,
    alignItems: 'center',
  },
  expandedActionText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '600',
  },
});
```

## Usage Guidelines

### Do's
- Display QR codes with sufficient padding (minimum 20px white space)
- Use black and white for maximum scannability
- Test QR codes with multiple scanner apps
- Provide alternative text or ID alongside QR
- Allow expansion for full-screen scanning
- Include share and download functionality
- Keep QR code size adequate (minimum 200x200px)

### Don'ts
- Don't add decorative elements that obscure QR code
- Don't use colored QR codes unless absolutely necessary
- Don't make QR codes smaller than 200x200px
- Don't remove white padding around code
- Don't rotate or distort QR codes
- Don't use transparent backgrounds
- Avoid placing QR codes on patterned backgrounds

## Related Components

- [Card](/docs/design/components/card.md) - QR code typically displayed in a card
- [Button](/docs/design/components/button.md) - Share/Download action buttons
- [Bottom Navigation](/docs/design/components/bottom-navigation.md) - Accessed via Wallet tab
- [Status Badge](/docs/design/components/status-badge.md) - Can show alongside user status/points
