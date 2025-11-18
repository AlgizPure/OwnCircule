/**
 * Bonus API Service
 * Handles bonus-related API calls
 */

import apiClient from './apiClient';

// ===================================================================
// Types
// ===================================================================

export type BonusType = 'accrual' | 'redemption' | 'expiry' | 'adjustment' | 'gift';
export type BonusStatus = 'active' | 'redeemed' | 'expired' | 'cancelled';

export interface Bonus {
  id: number;
  userId: number;
  transactionId?: number;
  amount: number; // Positive for accrual, negative for redemption
  type: BonusType;
  status: BonusStatus;
  description?: string;
  expiresAt?: string;
  multiplier: number;
  createdAt: string;
  updatedAt: string;
}

export interface BonusBalanceResponse {
  balance: number;
}

export interface BonusHistoryResponse {
  bonuses: Bonus[];
  total: number;
  page: number;
  perPage: number;
}

export interface BonusRedeemRequest {
  amount: number;
}

export interface BonusRedeemResponse {
  bonus: Bonus;
  newBalance: number;
  message: string;
}

// ===================================================================
// Bonus Service
// ===================================================================

class BonusService {
  /**
   * Get current bonus balance
   */
  async getBalance(): Promise<number> {
    const response = await apiClient.get<BonusBalanceResponse>('/bonuses/balance');
    return response.data.balance;
  }

  /**
   * Get bonus history (accruals and redemptions)
   */
  async getBonusHistory(page: number = 1, perPage: number = 50): Promise<BonusHistoryResponse> {
    const response = await apiClient.get<BonusHistoryResponse>(
      `/bonuses?page=${page}&per_page=${perPage}`
    );
    return response.data;
  }

  /**
   * Redeem bonuses (pay with bonuses)
   */
  async redeemBonuses(amount: number): Promise<BonusRedeemResponse> {
    const response = await apiClient.post<BonusRedeemResponse>('/bonuses/redeem', {
      amount,
    });
    return response.data;
  }
}

export default new BonusService();
