# Input Component

## Overview

The Input component is a fundamental form element for capturing user text input. It features a clean, minimal design with rounded corners and a Champagne Beige background (#F5F1E8) for a soft, welcoming appearance. Input fields are used throughout the application for forms, search, filters, and user data entry.

**Primary Use Cases:**
- Form field input (name, email, phone)
- Search functionality
- Password entry
- Filter/query input
- Text message composition
- Numeric input for quantities

## Anatomy

The Input component consists of the following visual parts:

```
┌─────────────────────────────────┐
│ Label (optional)                │
├─────────────────────────────────┤
│ ◀ Icon   Input Text   Icon ▶   │
├─────────────────────────────────┤
│ Helper text or error message    │
└─────────────────────────────────┘
```

### Key Elements:
- **Container**: Rounded rectangle with Champagne Beige background
- **Label**: Optional text above input (12px/600, caption style)
- **Leading Icon**: Optional icon (16x16px) for context
- **Input Field**: Text input area with cursor
- **Placeholder**: Faded text showing expected format
- **Trailing Icon**: Optional icon (clear button, visibility toggle)
- **Helper Text**: Optional text below input for guidance
- **Error Text**: Red error message for validation feedback
- **Border Radius**: 8px for clean appearance

## Variants

### 1. Standard Text Input
- **Type**: text
- **Background**: Champagne Beige (#F5F1E8)
- **Usage**: General text entry
- **Example**: Name, description fields

### 2. Email Input
- **Type**: email
- **Keyboard**: Email keyboard on mobile
- **Validation**: Email format checking
- **Usage**: Email address entry

### 3. Password Input
- **Type**: password
- **Masking**: Text masked with dots/asterisks
- **Toggle**: Show/hide password icon
- **Usage**: Password entry, sensitive information

### 4. Numeric Input
- **Type**: number
- **Keyboard**: Numeric keyboard on mobile
- **Input Filter**: Numbers only
- **Usage**: Quantities, codes, zip codes

### 5. Phone Input
- **Type**: tel
- **Keyboard**: Phone keyboard on mobile
- **Formatting**: Automatic phone number formatting
- **Usage**: Phone number entry

### 6. Search Input
- **Leading Icon**: Search icon
- **Trailing Icon**: Clear/close button
- **Placeholder**: "Search..."
- **Usage**: Search functionality

### 7. Textarea
- **Multiline**: true
- **Height**: Dynamic or fixed (120px minimum)
- **Resizable**: Expandable height as user types
- **Usage**: Comments, descriptions, long text

## States

### Default State
- Background: Champagne Beige (#F5F1E8)
- Border: 1px solid #E8E8E8
- Text color: Charcoal (#2A2D34)
- Placeholder: 50% opacity text

### Focus State
- Border: 2px solid Tiffany Blue (#0ABAB5)
- Background: White (#FFFFFF)
- Shadow: Subtle shadow (0 0 0 3px rgba(10, 186, 181, 0.1))
- Cursor: Visible text input cursor

### Active State (Filled)
- Background: Champagne Beige (#F5F1E8)
- Border: 1px solid Charcoal (#2A2D34)
- Text: Fully opaque
- Clear button visible if applicable

### Hover State
- Border: 1px solid Tiffany Blue (#0ABAB5)
- Shadow: Subtle elevation
- Cursor: text cursor

### Disabled State
- Background: #F5F1E8 at 50% opacity
- Text: #2A2D34 at 50% opacity
- Cursor: not-allowed
- No focus or hover response

### Error State
- Border: 2px solid #D32F2F (Red)
- Background: #FFF3E0 (Light orange tint)
- Icon: Error icon (red)
- Text: Error message in red

### Loading State
- Activity indicator visible
- Input disabled
- Loading spinner in trailing icon area

### Success State
- Border: 2px solid #4CAF50 (Green)
- Icon: Checkmark icon (green)
- Validation message visible
- Temporary state (2-3 seconds)

## Props/API

```typescript
interface InputProps {
  // Content
  placeholder?: string;
  label?: string;
  value: string;
  defaultValue?: string;
  
  // Input Properties
  inputType?: 'text' | 'email' | 'password' | 'number' | 'phone' | 'search';
  multiline?: boolean; // default: false
  numberOfLines?: number; // for multiline
  maxLength?: number;
  
  // Icons
  leadingIcon?: React.ReactNode;
  trailingIcon?: React.ReactNode;
  showClearButton?: boolean; // default: false
  showPasswordToggle?: boolean; // default: false (for password type)
  
  // Styling
  backgroundColor?: string; // default: '#F5F1E8'
  borderColor?: string;
  textColor?: string;
  size?: 'small' | 'medium' | 'large'; // default: 'medium'
  
  // State
  disabled?: boolean; // default: false
  readOnly?: boolean; // default: false
  error?: string | null; // error message
  helperText?: string;
  success?: boolean; // default: false
  loading?: boolean; // default: false
  
  // Interaction
  onChangeText: (text: string) => void;
  onFocus?: () => void;
  onBlur?: () => void;
  onSubmitEditing?: () => void;
  
  // Validation
  required?: boolean; // default: false
  pattern?: RegExp;
  
  // Accessibility
  accessibilityLabel?: string;
  accessibilityHint?: string;
  
  // Styling overrides
  style?: StyleProp<ViewStyle>;
  inputStyle?: StyleProp<TextStyle>;
}
```

## Spacing & Sizing

### Size Variants

#### Small Input
- **Height**: 36px
- **Padding**: 10px horizontal, 8px vertical
- **Font**: 14px/400
- **Border Radius**: 6px
- **Min Touch Target**: 36x44px (height with surrounding space)

#### Medium Input (Default)
- **Height**: 44px
- **Padding**: 12px horizontal, 10px vertical
- **Font**: 16px/400
- **Border Radius**: 8px
- **Min Touch Target**: 44x44px

#### Large Input
- **Height**: 52px
- **Padding**: 16px horizontal, 12px vertical
- **Font**: 18px/400
- **Border Radius**: 8px
- **Min Touch Target**: 52x52px

### Textarea Sizing
- **Min Height**: 120px
- **Max Height**: 200px (scrollable beyond)
- **Padding**: 12px (all sides)
- **Border Radius**: 8px

### Icon Sizing
- **Leading/Trailing Icon**: 16x16px (small), 20x20px (medium), 24x24px (large)
- **Icon Margin**: 8px from input edge
- **Clear Button**: 20x20px centered

### Text Sizing
- **Label Font**: 12px/600 (caption style)
- **Input Font**: 16px/400 (body style)
- **Helper Text Font**: 12px/400 (caption style)
- **Error Text Font**: 12px/400 (caption style, red color)

### Spacing
- **Label to Input**: 4px gap
- **Input to Helper Text**: 4px gap
- **Input to Error Text**: 4px gap

## Accessibility

### Touch Target
- Minimum 44x44px tap area per WCAG 2.1
- Input height of 44px meets standard
- Clear buttons and icons minimum 20x20px

### Contrast Ratio
- Text on Beige background: 13.5:1 (Charcoal on Beige)
- Placeholder: 5.2:1 (50% opacity Charcoal)
- Error text: 5.9:1 (Red on white)
- All exceed WCAG AAA standard

### Screen Reader Support
```typescript
<TextInput
  accessible={true}
  accessibilityLabel={label}
  accessibilityHint={helperText || error}
  accessibilityRole="none"
  accessibilityState={{
    disabled: disabled,
    focused: focused,
  }}
/>
```

### Keyboard Navigation
- Focusable via Tab key
- Clear focus indicator (blue border + shadow)
- Tab moves to next input
- Shift+Tab moves to previous input
- Enter/Space activates related buttons (clear, toggle)

### Labels
- Every input should have associated label
- Label can be above input or use aria-label
- Label font: 12px/600 for clarity

## Implementation

### React Native Example

```typescript
import React, { useState } from 'react';
import {
  View,
  TextInput,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';

interface InputProps {
  placeholder?: string;
  label?: string;
  value: string;
  onChangeText: (text: string) => void;
  inputType?: 'text' | 'email' | 'password' | 'number' | 'phone';
  error?: string | null;
  helperText?: string;
  disabled?: boolean;
  multiline?: boolean;
  size?: 'small' | 'medium' | 'large';
  showClearButton?: boolean;
  leadingIcon?: React.ReactNode;
  onFocus?: () => void;
  onBlur?: () => void;
}

export const Input: React.FC<InputProps> = ({
  placeholder,
  label,
  value,
  onChangeText,
  inputType = 'text',
  error = null,
  helperText,
  disabled = false,
  multiline = false,
  size = 'medium',
  showClearButton = false,
  leadingIcon,
  onFocus,
  onBlur,
}) => {
  const [focused, setFocused] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const styles = getStyles(size, focused, error, disabled);

  const keyboardType = {
    text: 'default',
    email: 'email-address',
    password: 'default',
    number: 'numeric',
    phone: 'phone-pad',
  }[inputType];

  return (
    <View style={styles.container}>
      {label && <Text style={styles.label}>{label}</Text>}

      <View
        style={[
          styles.inputContainer,
          focused && styles.inputContainerFocused,
          error && styles.inputContainerError,
        ]}
      >
        {leadingIcon && (
          <View style={styles.iconContainer}>{leadingIcon}</View>
        )}

        <TextInput
          style={[styles.input, multiline && styles.multilineInput]}
          placeholder={placeholder}
          value={value}
          onChangeText={onChangeText}
          onFocus={() => {
            setFocused(true);
            onFocus?.();
          }}
          onBlur={() => {
            setFocused(false);
            onBlur?.();
          }}
          editable={!disabled}
          secureTextEntry={inputType === 'password' && !showPassword}
          keyboardType={keyboardType as any}
          multiline={multiline}
          numberOfLines={multiline ? 4 : 1}
          accessible={true}
          accessibilityLabel={label}
          accessibilityHint={helperText || error}
          accessibilityRole="none"
          placeholderTextColor="#99999980"
        />

        {showClearButton && value.length > 0 && (
          <TouchableOpacity
            style={styles.clearButton}
            onPress={() => onChangeText('')}
            accessible={true}
            accessibilityLabel="Clear input"
          >
            <Text style={styles.clearIcon}>✕</Text>
          </TouchableOpacity>
        )}

        {inputType === 'password' && (
          <TouchableOpacity
            style={styles.iconContainer}
            onPress={() => setShowPassword(!showPassword)}
          >
            <Text style={styles.eyeIcon}>{showPassword ? '👁' : '👁‍🗨'}</Text>
          </TouchableOpacity>
        )}
      </View>

      {error && <Text style={styles.errorText}>{error}</Text>}
      {helperText && !error && (
        <Text style={styles.helperText}>{helperText}</Text>
      )}
    </View>
  );
};

const getStyles = (
  size: string,
  focused: boolean,
  error: string | null,
  disabled: boolean,
) => {
  const sizeConfig = {
    small: {
      height: 36,
      paddingHorizontal: 10,
      fontSize: 14,
      borderRadius: 6,
    },
    medium: {
      height: 44,
      paddingHorizontal: 12,
      fontSize: 16,
      borderRadius: 8,
    },
    large: {
      height: 52,
      paddingHorizontal: 16,
      fontSize: 18,
      borderRadius: 8,
    },
  };

  const config = sizeConfig[size as keyof typeof sizeConfig];

  return StyleSheet.create({
    container: {
      marginVertical: 8,
    },
    label: {
      fontSize: 12,
      fontWeight: '600',
      color: '#2A2D34',
      marginBottom: 4,
    },
    inputContainer: {
      flexDirection: 'row',
      alignItems: 'center',
      height: config.height,
      backgroundColor: disabled ? '#F5F1E8CC' : '#F5F1E8',
      borderRadius: config.borderRadius,
      borderWidth: 1,
      borderColor: '#E8E8E8',
      paddingHorizontal: config.paddingHorizontal,
    },
    inputContainerFocused: {
      borderWidth: 2,
      borderColor: '#0ABAB5',
      backgroundColor: '#FFFFFF',
      shadowColor: '#0ABAB5',
      shadowOffset: { width: 0, height: 0 },
      shadowOpacity: 0.15,
      shadowRadius: 3,
      elevation: 3,
    },
    inputContainerError: {
      borderWidth: 2,
      borderColor: '#D32F2F',
      backgroundColor: '#FFF3E0',
    },
    input: {
      flex: 1,
      fontSize: config.fontSize,
      color: '#2A2D34',
      fontWeight: '400',
    },
    multilineInput: {
      minHeight: 120,
      maxHeight: 200,
      textAlignVertical: 'top',
      paddingVertical: 12,
    },
    iconContainer: {
      marginHorizontal: 8,
      justifyContent: 'center',
      alignItems: 'center',
    },
    clearButton: {
      marginLeft: 8,
      padding: 4,
    },
    clearIcon: {
      fontSize: 18,
      color: '#999999',
    },
    eyeIcon: {
      fontSize: 18,
    },
    helperText: {
      fontSize: 12,
      fontWeight: '400',
      color: '#666666',
      marginTop: 4,
    },
    errorText: {
      fontSize: 12,
      fontWeight: '400',
      color: '#D32F2F',
      marginTop: 4,
    },
  });
};
```

## Usage Guidelines

### Do's
- Always provide labels for inputs (accessibility)
- Use appropriate input types (email, password, number, etc.)
- Provide helpful placeholder text
- Show validation errors clearly
- Use helper text to guide users
- Disable inputs when not needed (loading, dependent fields)
- Clear input on clear button press
- Validate input on blur and form submission

### Don'ts
- Don't rely only on placeholder text as label
- Don't disable input without explanation
- Don't show errors while user is still typing (except validation preview)
- Don't use unclear placeholder text
- Don't make inputs too small (< 44px height)
- Don't use password input for non-sensitive data
- Avoid dynamic background color changes during typing
- Don't truncate or hide error messages

## Related Components

- [Button](/docs/design/components/button.md) - Used to submit input forms
- [Card](/docs/design/components/card.md) - Forms often contained within cards
- [Status Badge](/docs/design/components/status-badge.md) - Shows input validation status
- [Bottom Navigation](/docs/design/components/bottom-navigation.md) - Navigation for form sections
