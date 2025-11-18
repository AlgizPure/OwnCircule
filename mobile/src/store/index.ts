/**
 * Redux Store Configuration
 * Using Redux Toolkit 2.10.1
 */

import { configureStore } from '@reduxjs/toolkit';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';

import authReducer from './slices/authSlice';
import userReducer from './slices/userSlice';
import transactionReducer from './slices/transactionSlice';
import bonusReducer from './slices/bonusSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    user: userReducer,
    transactions: transactionReducer,
    bonus: bonusReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        // Ignore these action types
        ignoredActions: ['auth/login/fulfilled'],
      },
    }),
});

// Infer types from store
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Typed hooks
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
