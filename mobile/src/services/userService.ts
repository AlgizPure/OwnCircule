/**
 * User API Service
 * Handles user profile-related API calls
 */

import apiClient from './apiClient';
import tokenStorage from '../utils/tokenStorage';

// ===================================================================
// Types
// ===================================================================

export interface User {
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
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface UpdateUserRequest {
  firstName?: string;
  lastName?: string;
  email?: string;
}

// ===================================================================
// User Service
// ===================================================================

class UserService {
  /**
   * Get user profile by ID
   */
  async getUserById(userId: number): Promise<User> {
    const response = await apiClient.get<User>(`/users/${userId}`);

    // Save user data to local storage
    await tokenStorage.saveUser(response.data as any);

    return response.data;
  }

  /**
   * Update user profile
   */
  async updateUser(userId: number, data: UpdateUserRequest): Promise<User> {
    const response = await apiClient.patch<User>(`/users/${userId}`, {
      first_name: data.firstName,
      last_name: data.lastName,
      email: data.email,
    });

    // Update user data in local storage
    await tokenStorage.saveUser(response.data as any);

    return response.data;
  }

  /**
   * Get current user from local storage
   */
  async getStoredUser() {
    return tokenStorage.getUser();
  }
}

export default new UserService();
