/**
 * Authentication API Service
 * Handles all authentication-related API calls
 */

import apiClient from './apiClient';
import tokenStorage from '../utils/tokenStorage';

// ===================================================================
// Request/Response Types
// ===================================================================

export interface SendOTPRequest {
  phone: string;
}

export interface SendOTPResponse {
  message: string;
  phone: string;
  expires_in: number;
}

export interface VerifyOTPRequest {
  phone: string;
  code: string;
}

export interface VerifyOTPResponse {
  message: string;
  phone: string;
}

export interface RegisterRequest {
  phone: string;
  password: string;
  first_name: string;
  last_name: string;
}

export interface LoginRequest {
  phone: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
}

export interface LogoutResponse {
  message: string;
}

// ===================================================================
// Auth Service
// ===================================================================

class AuthService {
  /**
   * Send OTP code to phone number
   */
  async sendOTP(phone: string): Promise<SendOTPResponse> {
    const response = await apiClient.post<SendOTPResponse>('/auth/send-otp', {
      phone,
    });
    return response.data;
  }

  /**
   * Verify OTP code
   */
  async verifyOTP(phone: string, code: string): Promise<VerifyOTPResponse> {
    const response = await apiClient.post<VerifyOTPResponse>('/auth/verify-otp', {
      phone,
      code,
    });
    return response.data;
  }

  /**
   * Register new user
   * Returns tokens and automatically saves them
   */
  async register(data: RegisterRequest): Promise<TokenResponse> {
    const response = await apiClient.post<TokenResponse>('/auth/register', data);
    const tokens = response.data;

    // Save tokens to storage
    await tokenStorage.saveTokens(tokens.access_token, tokens.refresh_token);

    return tokens;
  }

  /**
   * Login user
   * Returns tokens and automatically saves them
   */
  async login(phone: string, password: string): Promise<TokenResponse> {
    const response = await apiClient.post<TokenResponse>('/auth/login', {
      phone,
      password,
    });
    const tokens = response.data;

    // Save tokens to storage
    await tokenStorage.saveTokens(tokens.access_token, tokens.refresh_token);

    return tokens;
  }

  /**
   * Refresh access token
   * Called automatically by apiClient interceptor on 401 errors
   */
  async refreshToken(refreshToken: string): Promise<TokenResponse> {
    const response = await apiClient.post<TokenResponse>('/auth/refresh', {
      refresh_token: refreshToken,
    });
    const tokens = response.data;

    // Save new tokens to storage
    await tokenStorage.saveTokens(tokens.access_token, tokens.refresh_token);

    return tokens;
  }

  /**
   * Logout user
   * Revokes refresh token on backend and clears local storage
   */
  async logout(): Promise<void> {
    try {
      const refreshToken = await tokenStorage.getRefreshToken();

      if (refreshToken) {
        // Call logout endpoint to revoke refresh token on backend
        await apiClient.post<LogoutResponse>('/auth/logout', {
          refresh_token: refreshToken,
        });
      }
    } catch (error) {
      // Even if logout fails, clear local tokens
      console.error('[Logout Error]', error);
    } finally {
      // Always clear local storage
      await tokenStorage.clearAll();
    }
  }

  /**
   * Check if user is authenticated
   */
  async isAuthenticated(): Promise<boolean> {
    return tokenStorage.isAuthenticated();
  }

  /**
   * Get stored tokens
   */
  async getStoredTokens() {
    return tokenStorage.getTokens();
  }
}

export default new AuthService();
