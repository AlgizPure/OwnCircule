/**
 * Color Tokens
 * Imported from docs/design/resources/design-tokens.json
 */

export const colors = {
  // Primary Colors
  primary: {
    tiffanyBlue: '#0ABAB5',
    champagneBeige: '#F5F1E8',
    champagneGold: '#D4AF37',
  },

  // Secondary Colors
  secondary: {
    charcoal: '#2A2D34',
    taupe: '#8B7355',
    bronze: '#8B7355',
    softPink: '#E8B4BC',
  },

  // Semantic Colors
  semantic: {
    success: '#7CB342',
    error: '#E57373',
    warning: '#FFB74D',
    info: '#64B5F6',
  },

  // Grays
  grays: {
    50: '#FAFAFA',
    100: '#F5F5F5',
    200: '#EEEEEE',
    300: '#E0E0E0',
    400: '#BDBDBD',
    500: '#9E9E9E',
    600: '#757575',
    700: '#616161',
    800: '#424242',
    900: '#212121',
  },

  // Text Colors
  text: {
    primary: '#2A2D34',
    secondary: '#8B7355',
    disabled: '#BDBDBD',
    onPrimary: '#FFFFFF',
    onAccent: '#2A2D34',
  },

  // Background Colors
  background: {
    default: '#FFFFFF',
    secondary: '#F5F1E8',
    tertiary: '#FAFAFA',
  },

  // Border Colors
  border: {
    light: '#EEEEEE',
    default: '#E0E0E0',
    strong: '#BDBDBD',
  },
} as const;

export type Colors = typeof colors;
