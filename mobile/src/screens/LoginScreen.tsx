/**
 * Login Screen
 * Phone number input for SMS OTP authentication
 * Note: Backend integration deferred to Sprint 2
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import type { AuthStackScreenProps } from '@/types/navigation';

export default function LoginScreen({
  navigation,
}: AuthStackScreenProps<'Login'>) {
  const [phone, setPhone] = useState('');

  const formatPhone = (text: string) => {
    // Remove all non-digits
    const digits = text.replace(/\D/g, '');

    // Format as +7 XXX XXX-XX-XX
    let formatted = '+7';
    if (digits.length > 1) {
      formatted += ' ' + digits.substring(1, 4);
    }
    if (digits.length >= 5) {
      formatted += ' ' + digits.substring(4, 7);
    }
    if (digits.length >= 8) {
      formatted += '-' + digits.substring(7, 9);
    }
    if (digits.length >= 10) {
      formatted += '-' + digits.substring(9, 11);
    }

    return formatted;
  };

  const handlePhoneChange = (text: string) => {
    const formatted = formatPhone(text);
    setPhone(formatted);
  };

  const handleContinue = () => {
    // TODO: Integrate with backend in Sprint 2
    // For now, just navigate (or show alert that backend integration is pending)
    console.log('Phone:', phone);
    // navigation.navigate('VerifyOTP', { phone });
  };

  const isValidPhone = phone.replace(/\D/g, '').length === 11;

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={colors.background.default} />

      <KeyboardAvoidingView
        style={styles.keyboardView}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <View style={styles.content}>
          {/* Header */}
          <View style={styles.header}>
            <View style={styles.logoSmall}>
              <Text style={styles.logoSmallText}>СК</Text>
            </View>
            <Text style={styles.title}>Вход в приложение</Text>
            <Text style={styles.subtitle}>
              Введите номер телефона для входа{'\n'}
              Мы отправим вам код подтверждения
            </Text>
          </View>

          {/* Phone Input */}
          <View style={styles.form}>
            <Text style={styles.label}>Номер телефона</Text>
            <TextInput
              style={styles.input}
              placeholder="+7 999 123-45-67"
              placeholderTextColor={colors.text.disabled}
              keyboardType="phone-pad"
              value={phone}
              onChangeText={handlePhoneChange}
              maxLength={18} // +7 XXX XXX-XX-XX
              autoFocus
            />
          </View>

          {/* CTA Button */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={[
                styles.primaryButton,
                !isValidPhone && styles.primaryButtonDisabled,
              ]}
              onPress={handleContinue}
              disabled={!isValidPhone}
              activeOpacity={0.8}
            >
              <Text
                style={[
                  styles.buttonText,
                  !isValidPhone && styles.buttonTextDisabled,
                ]}
              >
                Получить код
              </Text>
            </TouchableOpacity>

            <Text style={styles.disclaimer}>
              Продолжая, вы соглашаетесь с{' '}
              <Text style={styles.link}>Условиями использования</Text> и{' '}
              <Text style={styles.link}>Политикой конфиденциальности</Text>
            </Text>
          </View>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.default,
  },
  keyboardView: {
    flex: 1,
  },
  content: {
    flex: 1,
    paddingHorizontal: spacing.lg,
  },
  header: {
    alignItems: 'center',
    marginTop: spacing['3xl'],
    marginBottom: spacing.xl,
  },
  logoSmall: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: colors.primary.tiffanyBlue,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.lg,
    ...shadows[1],
  },
  logoSmallText: {
    fontSize: 28,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
  },
  title: {
    fontSize: typography.fontSize.h1,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
    letterSpacing: typography.letterSpacing.h1,
    marginBottom: spacing.sm,
  },
  subtitle: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    lineHeight: typography.lineHeight.body,
  },
  form: {
    flex: 1,
  },
  label: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.sm,
  },
  input: {
    backgroundColor: colors.background.tertiary,
    borderWidth: 2,
    borderColor: colors.border.light,
    borderRadius: 12,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.md,
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
  },
  footer: {
    paddingBottom: spacing.xl,
  },
  primaryButton: {
    backgroundColor: colors.primary.tiffanyBlue,
    paddingVertical: spacing.md,
    borderRadius: 12,
    alignItems: 'center',
    marginBottom: spacing.md,
    ...shadows[2],
  },
  primaryButtonDisabled: {
    backgroundColor: colors.grays[300],
    ...shadows[0],
  },
  buttonText: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
  },
  buttonTextDisabled: {
    color: colors.text.disabled,
  },
  disclaimer: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    lineHeight: typography.lineHeight.caption,
  },
  link: {
    color: colors.primary.tiffanyBlue,
    fontWeight: typography.fontWeight.medium,
  },
});
