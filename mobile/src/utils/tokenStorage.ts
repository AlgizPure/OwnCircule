/**
 * Token Storage Utility
 * Manages secure storage of JWT tokens using AsyncStorage
 */

import AsyncStorage from '@react-native-async-storage/async-storage';

const STORAGE_KEYS = {
  ACCESS_TOKEN: '@svoy_krug:access_token',
  REFRESH_TOKEN: '@svoy_krug:refresh_token',
  USER_DATA: '@svoy_krug:user_data',
} as const;

export interface StoredTokens {
  accessToken: string;
  refreshToken: string;
}

export interface StoredUser {
  id: number;
  phone: string;
  firstName: string;
  lastName: string;
  email?: string;
  role: 'member' | 'business_admin' | 'super_admin';
  statusTier: 'insider' | 'vip' | 'elite' | 'inner_circle';
  totalSpend: number;
  bonusBalance: number;
  isVerified: boolean;
}

class TokenStorage {
  /**
   * Save access and refresh tokens
   */
  async saveTokens(accessToken: string, refreshToken: string): Promise<void> {
    try {
      await AsyncStorage.multiSet([
        [STORAGE_KEYS.ACCESS_TOKEN, accessToken],
        [STORAGE_KEYS.REFRESH_TOKEN, refreshToken],
      ]);
    } catch (error) {
      console.error('Error saving tokens:', error);
      throw new Error('Failed to save authentication tokens');
    }
  }

  /**
   * Get access token
   */
  async getAccessToken(): Promise<string | null> {
    try {
      return await AsyncStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN);
    } catch (error) {
      console.error('Error getting access token:', error);
      return null;
    }
  }

  /**
   * Get refresh token
   */
  async getRefreshToken(): Promise<string | null> {
    try {
      return await AsyncStorage.getItem(STORAGE_KEYS.REFRESH_TOKEN);
    } catch (error) {
      console.error('Error getting refresh token:', error);
      return null;
    }
  }

  /**
   * Get both tokens
   */
  async getTokens(): Promise<StoredTokens | null> {
    try {
      const values = await AsyncStorage.multiGet([
        STORAGE_KEYS.ACCESS_TOKEN,
        STORAGE_KEYS.REFRESH_TOKEN,
      ]);

      const accessToken = values[0][1];
      const refreshToken = values[1][1];

      if (!accessToken || !refreshToken) {
        return null;
      }

      return { accessToken, refreshToken };
    } catch (error) {
      console.error('Error getting tokens:', error);
      return null;
    }
  }

  /**
   * Clear all tokens
   */
  async clearTokens(): Promise<void> {
    try {
      await AsyncStorage.multiRemove([
        STORAGE_KEYS.ACCESS_TOKEN,
        STORAGE_KEYS.REFRESH_TOKEN,
      ]);
    } catch (error) {
      console.error('Error clearing tokens:', error);
    }
  }

  /**
   * Save user data
   */
  async saveUser(user: StoredUser): Promise<void> {
    try {
      await AsyncStorage.setItem(STORAGE_KEYS.USER_DATA, JSON.stringify(user));
    } catch (error) {
      console.error('Error saving user data:', error);
      throw new Error('Failed to save user data');
    }
  }

  /**
   * Get user data
   */
  async getUser(): Promise<StoredUser | null> {
    try {
      const userData = await AsyncStorage.getItem(STORAGE_KEYS.USER_DATA);
      return userData ? JSON.parse(userData) : null;
    } catch (error) {
      console.error('Error getting user data:', error);
      return null;
    }
  }

  /**
   * Clear user data
   */
  async clearUser(): Promise<void> {
    try {
      await AsyncStorage.removeItem(STORAGE_KEYS.USER_DATA);
    } catch (error) {
      console.error('Error clearing user data:', error);
    }
  }

  /**
   * Clear all stored data (tokens + user)
   */
  async clearAll(): Promise<void> {
    try {
      await AsyncStorage.multiRemove([
        STORAGE_KEYS.ACCESS_TOKEN,
        STORAGE_KEYS.REFRESH_TOKEN,
        STORAGE_KEYS.USER_DATA,
      ]);
    } catch (error) {
      console.error('Error clearing all data:', error);
    }
  }

  /**
   * Check if user is authenticated (has valid tokens)
   */
  async isAuthenticated(): Promise<boolean> {
    const tokens = await this.getTokens();
    return tokens !== null;
  }
}

export default new TokenStorage();
