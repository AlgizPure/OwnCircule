/**
 * Auth Navigator
 * Authentication flow (Login -> Verify OTP -> Register)
 */

import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';

import LoginScreen from '@/screens/LoginScreen';

import type { AuthStackParamList } from '@/types/navigation';

const Stack = createStackNavigator<AuthStackParamList>();

export default function AuthNavigator() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: false,
        cardStyle: { backgroundColor: '#FFFFFF' },
      }}
    >
      <Stack.Screen name="Login" component={LoginScreen} />
      {/* TODO: Add VerifyOTP and Register screens in Sprint 2 */}
    </Stack.Navigator>
  );
}
