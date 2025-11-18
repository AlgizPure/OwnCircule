/**
 * Environment Configuration
 * Loads environment variables from .env file
 */

import { Platform } from 'react-native';

// Note: In production, use react-native-config or similar to load from .env
// For now, using defaults suitable for development

export const ENV = {
  // API Configuration
  API_BASE_URL: __DEV__
    ? Platform.select({
        ios: 'http://localhost:8000',
        android: 'http://10.0.2.2:8000', // Android emulator uses this IP for localhost
      })
    : 'https://api.svoykrug.ru',
  API_TIMEOUT: 10000, // 10 seconds

  // App Info
  APP_ENV: __DEV__ ? 'development' : 'production',
  APP_VERSION: '1.0.0',
  APP_BUILD_NUMBER: '1',

  // Feature Flags
  FEATURE_BIOMETRIC_LOGIN: true,
  FEATURE_QR_SCANNER: true,
  FEATURE_EVENTS: true,

  // Debug Settings
  DEBUG_MODE: __DEV__,
  SHOW_NETWORK_LOGS: __DEV__,

  // Cache Settings
  CACHE_EXPIRY_MINUTES: 10,
};

export default ENV;
