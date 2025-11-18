/**
 * Transaction Slice
 * Manages transaction state
 */

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import type { RootState } from '../index';
import transactionService, {
  Transaction,
  TransactionFilters,
  TransactionStats,
} from '../../services/transactionService';

interface TransactionState {
  transactions: Transaction[];
  currentTransaction: Transaction | null;
  stats: TransactionStats | null;
  total: number;
  page: number;
  perPage: number;
  totalPages: number;
  isLoading: boolean;
  error: string | null;
}

const initialState: TransactionState = {
  transactions: [],
  currentTransaction: null,
  stats: null,
  total: 0,
  page: 1,
  perPage: 20,
  totalPages: 0,
  isLoading: false,
  error: null,
};

// ===================================================================
// Async Thunks
// ===================================================================

/**
 * Fetch user's transactions
 */
export const fetchTransactions = createAsyncThunk(
  'transactions/fetchTransactions',
  async (filters?: TransactionFilters, { rejectWithValue }) => {
    try {
      const response = await transactionService.getTransactions(filters);
      return response;
    } catch (error: any) {
      return rejectWithValue(
        error.response?.data?.detail || 'Failed to fetch transactions'
      );
    }
  }
);

/**
 * Fetch transaction by ID
 */
export const fetchTransactionById = createAsyncThunk(
  'transactions/fetchTransactionById',
  async (transactionId: number, { rejectWithValue }) => {
    try {
      const transaction = await transactionService.getTransactionById(transactionId);
      return transaction;
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Transaction not found');
    }
  }
);

/**
 * Fetch transaction statistics
 */
export const fetchTransactionStats = createAsyncThunk(
  'transactions/fetchStats',
  async (_, { rejectWithValue }) => {
    try {
      const stats = await transactionService.getMyStats();
      return stats;
    } catch (error: any) {
      return rejectWithValue(
        error.response?.data?.detail || 'Failed to fetch statistics'
      );
    }
  }
);

// ===================================================================
// Slice
// ===================================================================

export const transactionSlice = createSlice({
  name: 'transactions',
  initialState,
  reducers: {
    clearTransactions: (state) => {
      state.transactions = [];
      state.total = 0;
      state.page = 1;
      state.totalPages = 0;
    },
    clearCurrentTransaction: (state) => {
      state.currentTransaction = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Fetch transactions
    builder
      .addCase(fetchTransactions.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchTransactions.fulfilled, (state, action) => {
        state.isLoading = false;
        state.transactions = action.payload.transactions;
        state.total = action.payload.total;
        state.page = action.payload.page;
        state.perPage = action.payload.perPage;
        state.totalPages = action.payload.totalPages;
      })
      .addCase(fetchTransactions.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Fetch transaction by ID
    builder
      .addCase(fetchTransactionById.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchTransactionById.fulfilled, (state, action) => {
        state.isLoading = false;
        state.currentTransaction = action.payload;
      })
      .addCase(fetchTransactionById.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Fetch stats
    builder
      .addCase(fetchTransactionStats.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchTransactionStats.fulfilled, (state, action) => {
        state.isLoading = false;
        state.stats = action.payload;
      })
      .addCase(fetchTransactionStats.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const { clearTransactions, clearCurrentTransaction, clearError } =
  transactionSlice.actions;

// Selectors
export const selectTransactions = (state: RootState) => state.transactions.transactions;
export const selectCurrentTransaction = (state: RootState) =>
  state.transactions.currentTransaction;
export const selectTransactionStats = (state: RootState) => state.transactions.stats;
export const selectTransactionLoading = (state: RootState) => state.transactions.isLoading;
export const selectTransactionError = (state: RootState) => state.transactions.error;
export const selectTransactionPagination = (state: RootState) => ({
  page: state.transactions.page,
  perPage: state.transactions.perPage,
  total: state.transactions.total,
  totalPages: state.transactions.totalPages,
});

export default transactionSlice.reducer;
