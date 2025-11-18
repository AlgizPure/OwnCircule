/**
 * Axios API Client
 * Configured with request/response interceptors for authentication
 */

import axios, { AxiosInstance, InternalAxiosRequestConfig, AxiosError } from 'axios';
import ENV from '../config/env';
import tokenStorage from '../utils/tokenStorage';

// Create axios instance
const apiClient: AxiosInstance = axios.create({
  baseURL: `${ENV.API_BASE_URL}/api/v1`,
  timeout: ENV.API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Track if token refresh is in progress to avoid multiple refresh requests
let isRefreshing = false;
let refreshSubscribers: ((token: string) => void)[] = [];

/**
 * Subscribe to token refresh completion
 */
function subscribeTokenRefresh(callback: (token: string) => void) {
  refreshSubscribers.push(callback);
}

/**
 * Notify all subscribers when token is refreshed
 */
function onTokenRefreshed(token: string) {
  refreshSubscribers.forEach((callback) => callback(token));
  refreshSubscribers = [];
}

/**
 * Request Interceptor
 * Injects access token into Authorization header
 */
apiClient.interceptors.request.use(
  async (config: InternalAxiosRequestConfig) => {
    // Skip token injection for auth endpoints (login, register, refresh, etc.)
    const skipTokenEndpoints = ['/auth/login', '/auth/register', '/auth/send-otp', '/auth/verify-otp'];
    const isAuthEndpoint = skipTokenEndpoints.some((endpoint) =>
      config.url?.includes(endpoint)
    );

    if (!isAuthEndpoint) {
      const accessToken = await tokenStorage.getAccessToken();
      if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
      }
    }

    // Log requests in debug mode
    if (ENV.SHOW_NETWORK_LOGS) {
      console.log(`[API Request] ${config.method?.toUpperCase()} ${config.url}`, {
        headers: config.headers,
        data: config.data,
      });
    }

    return config;
  },
  (error) => {
    console.error('[API Request Error]', error);
    return Promise.reject(error);
  }
);

/**
 * Response Interceptor
 * Handles token refresh on 401 errors
 */
apiClient.interceptors.response.use(
  (response) => {
    // Log successful responses in debug mode
    if (ENV.SHOW_NETWORK_LOGS) {
      console.log(`[API Response] ${response.config.method?.toUpperCase()} ${response.config.url}`, {
        status: response.status,
        data: response.data,
      });
    }

    return response;
  },
  async (error: AxiosError) => {
    const originalRequest = error.config as InternalAxiosRequestConfig & {
      _retry?: boolean;
    };

    // Log errors in debug mode
    if (ENV.SHOW_NETWORK_LOGS) {
      console.error('[API Response Error]', {
        url: originalRequest?.url,
        status: error.response?.status,
        data: error.response?.data,
      });
    }

    // Handle 401 Unauthorized - Token expired
    if (error.response?.status === 401 && originalRequest && !originalRequest._retry) {
      // Skip refresh for auth endpoints
      if (originalRequest.url?.includes('/auth/')) {
        return Promise.reject(error);
      }

      // If already refreshing, queue this request
      if (isRefreshing) {
        return new Promise((resolve) => {
          subscribeTokenRefresh((token: string) => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            resolve(apiClient(originalRequest));
          });
        });
      }

      // Mark as retrying
      originalRequest._retry = true;
      isRefreshing = true;

      try {
        // Get refresh token
        const refreshToken = await tokenStorage.getRefreshToken();

        if (!refreshToken) {
          // No refresh token available, user needs to login again
          await tokenStorage.clearAll();
          throw new Error('No refresh token available');
        }

        // Call refresh endpoint
        const response = await axios.post(
          `${ENV.API_BASE_URL}/api/v1/auth/refresh`,
          { refresh_token: refreshToken },
          {
            headers: { 'Content-Type': 'application/json' },
          }
        );

        const { access_token, refresh_token } = response.data;

        // Save new tokens
        await tokenStorage.saveTokens(access_token, refresh_token);

        // Update authorization header
        originalRequest.headers.Authorization = `Bearer ${access_token}`;

        // Notify all queued requests
        onTokenRefreshed(access_token);

        isRefreshing = false;

        // Retry original request
        return apiClient(originalRequest);
      } catch (refreshError) {
        // Refresh failed, clear tokens and force login
        isRefreshing = false;
        refreshSubscribers = [];
        await tokenStorage.clearAll();

        console.error('[Token Refresh Failed]', refreshError);
        return Promise.reject(refreshError);
      }
    }

    // For other errors, reject
    return Promise.reject(error);
  }
);

export default apiClient;
