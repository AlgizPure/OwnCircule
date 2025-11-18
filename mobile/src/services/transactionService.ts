/**
 * Transaction API Service
 * Handles transaction-related API calls
 */

import apiClient from './apiClient';

// ===================================================================
// Types
// ===================================================================

export type TransactionType = 'purchase' | 'bonus_redemption' | 'refund' | 'adjustment';
export type TransactionStatus = 'pending' | 'completed' | 'failed' | 'cancelled';

export interface Transaction {
  id: number;
  userId: number;
  businessId: number;
  amount: number;
  bonusAmount: number;
  type: TransactionType;
  status: TransactionStatus;
  category?: string;
  description?: string;
  receiptNumber?: string;
  metadata?: Record<string, any>;
  createdAt: string;
  updatedAt: string;
  completedAt?: string;
}

export interface TransactionFilters {
  userId?: number;
  businessId?: number;
  category?: string;
  type?: TransactionType;
  status?: TransactionStatus;
  dateFrom?: string;
  dateTo?: string;
  minAmount?: number;
  maxAmount?: number;
  page?: number;
  perPage?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

export interface TransactionListResponse {
  transactions: Transaction[];
  total: number;
  page: number;
  perPage: number;
  totalPages: number;
}

export interface TransactionStats {
  totalTransactions: number;
  totalSpent: number;
  totalBonusEarned: number;
  averageTransactionAmount: number;
  spendingByCategory: {
    category: string;
    totalSpent: number;
    transactionCount: number;
    percentage: number;
  }[];
  monthlySpending: {
    month: string;
    totalSpent: number;
    transactionCount: number;
  }[];
}

// ===================================================================
// Transaction Service
// ===================================================================

class TransactionService {
  /**
   * Get transaction by ID
   */
  async getTransactionById(transactionId: number): Promise<Transaction> {
    const response = await apiClient.get<Transaction>(`/transactions/${transactionId}`);
    return response.data;
  }

  /**
   * Get user's transaction list (paginated and filtered)
   */
  async getTransactions(filters?: TransactionFilters): Promise<TransactionListResponse> {
    const params = new URLSearchParams();

    if (filters) {
      if (filters.userId) params.append('user_id', filters.userId.toString());
      if (filters.businessId) params.append('business_id', filters.businessId.toString());
      if (filters.category) params.append('category', filters.category);
      if (filters.type) params.append('type', filters.type);
      if (filters.status) params.append('status', filters.status);
      if (filters.dateFrom) params.append('date_from', filters.dateFrom);
      if (filters.dateTo) params.append('date_to', filters.dateTo);
      if (filters.minAmount) params.append('min_amount', filters.minAmount.toString());
      if (filters.maxAmount) params.append('max_amount', filters.maxAmount.toString());
      if (filters.page) params.append('page', filters.page.toString());
      if (filters.perPage) params.append('per_page', filters.perPage.toString());
      if (filters.sortBy) params.append('sort_by', filters.sortBy);
      if (filters.sortOrder) params.append('sort_order', filters.sortOrder);
    }

    const response = await apiClient.get<TransactionListResponse>(
      `/transactions?${params.toString()}`
    );
    return response.data;
  }

  /**
   * Get user's transaction statistics
   */
  async getMyStats(): Promise<TransactionStats> {
    const response = await apiClient.get<TransactionStats>('/transactions/stats/me');
    return response.data;
  }

  /**
   * Get transaction statistics for a specific user (admin only)
   */
  async getUserStats(userId: number): Promise<TransactionStats> {
    const response = await apiClient.get<TransactionStats>(`/transactions/stats/${userId}`);
    return response.data;
  }
}

export default new TransactionService();
