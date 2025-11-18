/**
 * Root Navigator
 * Top-level navigation (Welcome -> Auth -> Main)
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import { useAppSelector } from '@/store';
import { selectIsAuthenticated } from '@/store/slices/authSlice';

import WelcomeScreen from '@/screens/WelcomeScreen';
import AuthNavigator from './AuthNavigator';
import MainNavigator from './MainNavigator';

import type { RootStackParamList } from '@/types/navigation';

const Stack = createStackNavigator<RootStackParamList>();

export default function RootNavigator() {
  const isAuthenticated = useAppSelector(selectIsAuthenticated);

  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        {!isAuthenticated ? (
          <>
            <Stack.Screen name="Welcome" component={WelcomeScreen} />
            <Stack.Screen name="Auth" component={AuthNavigator} />
          </>
        ) : (
          <Stack.Screen name="Main" component={MainNavigator} />
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
}
