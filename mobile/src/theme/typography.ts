/**
 * Typography Tokens
 * Imported from docs/design/resources/design-tokens.json
 */

import { Platform } from 'react-native';

export const typography = {
  // Font Families
  fontFamily: {
    display: Platform.select({
      ios: 'SF Pro Display',
      android: 'Roboto',
      default: 'System',
    }),
    text: Platform.select({
      ios: 'SF Pro Text',
      android: 'Roboto',
      default: 'System',
    }),
  },

  // Font Sizes
  fontSize: {
    display: 34,
    h1: 28,
    h2: 22,
    h3: 18,
    bodyLarge: 16,
    body: 14,
    caption: 12,
  },

  // Line Heights
  lineHeight: {
    display: 40,
    h1: 34,
    h2: 28,
    h3: 24,
    bodyLarge: 24,
    body: 20,
    caption: 16,
  },

  // Font Weights
  fontWeight: {
    light: '300' as const,
    regular: '400' as const,
    medium: '500' as const,
    semibold: '600' as const,
    bold: '700' as const,
  },

  // Letter Spacing
  letterSpacing: {
    display: -0.5,
    h1: -0.3,
    h2: 0,
    h3: 0,
    body: 0,
    caption: 0.3,
  },
} as const;

export type Typography = typeof typography;
