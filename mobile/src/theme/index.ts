/**
 * Theme System
 * Centralized design tokens for Svoy Krug mobile app
 *
 * Imported from docs/design/resources/design-tokens.json
 */

export { colors } from './colors';
export { typography } from './typography';
export { spacing } from './spacing';
export { borderRadius } from './borderRadius';
export { shadows } from './shadows';

export const theme = {
  colors: require('./colors').colors,
  typography: require('./typography').typography,
  spacing: require('./spacing').spacing,
  borderRadius: require('./borderRadius').borderRadius,
  shadows: require('./shadows').shadows,
} as const;

export type Theme = typeof theme;
