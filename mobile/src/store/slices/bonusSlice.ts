/**
 * Bonus Slice
 * Manages bonus state
 */

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import type { RootState } from '../index';
import bonusService, { Bonus } from '../../services/bonusService';

interface BonusState {
  balance: number;
  bonusHistory: Bonus[];
  total: number;
  page: number;
  perPage: number;
  isLoading: boolean;
  error: string | null;
}

const initialState: BonusState = {
  balance: 0,
  bonusHistory: [],
  total: 0,
  page: 1,
  perPage: 50,
  isLoading: false,
  error: null,
};

// ===================================================================
// Async Thunks
// ===================================================================

/**
 * Fetch bonus balance
 */
export const fetchBonusBalance = createAsyncThunk(
  'bonus/fetchBalance',
  async (_, { rejectWithValue }) => {
    try {
      const balance = await bonusService.getBalance();
      return balance;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch bonus balance');
    }
  }
);

/**
 * Fetch bonus history
 */
export const fetchBonusHistory = createAsyncThunk(
  'bonus/fetchHistory',
  async ({ page = 1, perPage = 50 }: { page?: number; perPage?: number }, { rejectWithValue }) => {
    try {
      const response = await bonusService.getBonusHistory(page, perPage);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch bonus history');
    }
  }
);

/**
 * Redeem bonuses
 */
export const redeemBonuses = createAsyncThunk(
  'bonus/redeem',
  async (amount: number, { rejectWithValue }) => {
    try {
      const response = await bonusService.redeemBonuses(amount);
      return response;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to redeem bonuses');
    }
  }
);

// ===================================================================
// Slice
// ===================================================================

export const bonusSlice = createSlice({
  name: 'bonus',
  initialState,
  reducers: {
    clearBonusHistory: (state) => {
      state.bonusHistory = [];
      state.total = 0;
      state.page = 1;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Fetch balance
    builder
      .addCase(fetchBonusBalance.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchBonusBalance.fulfilled, (state, action) => {
        state.isLoading = false;
        state.balance = action.payload;
      })
      .addCase(fetchBonusBalance.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Fetch history
    builder
      .addCase(fetchBonusHistory.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchBonusHistory.fulfilled, (state, action) => {
        state.isLoading = false;
        state.bonusHistory = action.payload.bonuses;
        state.total = action.payload.total;
        state.page = action.payload.page;
        state.perPage = action.payload.perPage;
      })
      .addCase(fetchBonusHistory.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Redeem bonuses
    builder
      .addCase(redeemBonuses.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(redeemBonuses.fulfilled, (state, action) => {
        state.isLoading = false;
        state.balance = action.payload.newBalance;
        // Add the redemption to history
        state.bonusHistory.unshift(action.payload.bonus);
      })
      .addCase(redeemBonuses.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const { clearBonusHistory, clearError } = bonusSlice.actions;

// Selectors
export const selectBonusBalance = (state: RootState) => state.bonus.balance;
export const selectBonusHistory = (state: RootState) => state.bonus.bonusHistory;
export const selectBonusLoading = (state: RootState) => state.bonus.isLoading;
export const selectBonusError = (state: RootState) => state.bonus.error;
export const selectBonusPagination = (state: RootState) => ({
  page: state.bonus.page,
  perPage: state.bonus.perPage,
  total: state.bonus.total,
});

export default bonusSlice.reducer;
