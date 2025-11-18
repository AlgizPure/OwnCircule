/**
 * Auth Slice
 * Manages authentication state (tokens, login status)
 */

import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import type { RootState } from '../index';
import authService from '../../services/authService';
import userService from '../../services/userService';
import { setUser, clearUser } from './userSlice';

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

const initialState: AuthState = {
  accessToken: null,
  refreshToken: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,
};

// ===================================================================
// Async Thunks
// ===================================================================

/**
 * Send OTP code
 */
export const sendOTP = createAsyncThunk(
  'auth/sendOTP',
  async (phone: string, { rejectWithValue }) => {
    try {
      const response = await authService.sendOTP(phone);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to send OTP');
    }
  }
);

/**
 * Verify OTP code
 */
export const verifyOTP = createAsyncThunk(
  'auth/verifyOTP',
  async ({ phone, code }: { phone: string; code: string }, { rejectWithValue }) => {
    try {
      const response = await authService.verifyOTP(phone, code);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Invalid OTP code');
    }
  }
);

/**
 * Register new user
 */
export const register = createAsyncThunk(
  'auth/register',
  async (
    data: { phone: string; password: string; firstName: string; lastName: string },
    { dispatch, rejectWithValue }
  ) => {
    try {
      const tokens = await authService.register({
        phone: data.phone,
        password: data.password,
        first_name: data.firstName,
        last_name: data.lastName,
      });

      // Fetch user profile after registration
      // Extract user ID from token (simplified - should decode JWT)
      // For now, we'll fetch using /users/me endpoint (to be implemented)
      // TODO: Implement /users/me endpoint or decode JWT to get user ID

      return tokens;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Registration failed');
    }
  }
);

/**
 * Login user
 */
export const login = createAsyncThunk(
  'auth/login',
  async (
    { phone, password }: { phone: string; password: string },
    { dispatch, rejectWithValue }
  ) => {
    try {
      const tokens = await authService.login(phone, password);

      // Fetch user profile after login
      // TODO: Implement /users/me endpoint or decode JWT to get user ID

      return tokens;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Login failed');
    }
  }
);

/**
 * Logout user
 */
export const logout = createAsyncThunk('auth/logout', async (_, { dispatch }) => {
  await authService.logout();
  dispatch(clearUser());
});

// ===================================================================
// Slice
// ===================================================================

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setTokens: (
      state,
      action: PayloadAction<{ accessToken: string; refreshToken: string }>
    ) => {
      state.accessToken = action.payload.accessToken;
      state.refreshToken = action.payload.refreshToken;
      state.isAuthenticated = true;
      state.error = null;
    },
    clearTokens: (state) => {
      state.accessToken = null;
      state.refreshToken = null;
      state.isAuthenticated = false;
      state.error = null;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Send OTP
    builder
      .addCase(sendOTP.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(sendOTP.fulfilled, (state) => {
        state.isLoading = false;
      })
      .addCase(sendOTP.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Verify OTP
    builder
      .addCase(verifyOTP.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(verifyOTP.fulfilled, (state) => {
        state.isLoading = false;
      })
      .addCase(verifyOTP.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Register
    builder
      .addCase(register.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.isLoading = false;
        state.accessToken = action.payload.access_token;
        state.refreshToken = action.payload.refresh_token;
        state.isAuthenticated = true;
      })
      .addCase(register.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Login
    builder
      .addCase(login.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.isLoading = false;
        state.accessToken = action.payload.access_token;
        state.refreshToken = action.payload.refresh_token;
        state.isAuthenticated = true;
      })
      .addCase(login.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Logout
    builder
      .addCase(logout.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(logout.fulfilled, (state) => {
        state.isLoading = false;
        state.accessToken = null;
        state.refreshToken = null;
        state.isAuthenticated = false;
        state.error = null;
      });
  },
});

export const { setTokens, clearTokens, setLoading, clearError } = authSlice.actions;

// Selectors
export const selectAuth = (state: RootState) => state.auth;
export const selectIsAuthenticated = (state: RootState) => state.auth.isAuthenticated;
export const selectAccessToken = (state: RootState) => state.auth.accessToken;
export const selectAuthLoading = (state: RootState) => state.auth.isLoading;
export const selectAuthError = (state: RootState) => state.auth.error;

export default authSlice.reducer;
