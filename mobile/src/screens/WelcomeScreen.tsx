/**
 * Welcome Screen
 * First screen users see - introduces app with Tiffany Blue branding
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import type { RootStackScreenProps } from '@/types/navigation';

export default function WelcomeScreen({
  navigation,
}: RootStackScreenProps<'Welcome'>) {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={colors.background.secondary} />

      <View style={styles.content}>
        {/* Logo Area */}
        <View style={styles.logoContainer}>
          <View style={styles.logoCircle}>
            <Text style={styles.logoText}>СК</Text>
          </View>
          <Text style={styles.appName}>Свой Круг</Text>
          <Text style={styles.tagline}>Премиальная система лояльности</Text>
        </View>

        {/* Feature Highlights */}
        <View style={styles.features}>
          <FeatureItem
            emoji="💎"
            title="Эксклюзивные бонусы"
            description="Накапливайте баллы в премиальных заведениях"
          />
          <FeatureItem
            emoji="🎁"
            title="Особые привилегии"
            description="Персональные предложения для VIP-клиентов"
          />
          <FeatureItem
            emoji="✨"
            title="Закрытые мероприятия"
            description="Доступ к эксклюзивным событиям"
          />
        </View>

        {/* CTA Button */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={styles.primaryButton}
            onPress={() => navigation.navigate('Auth')}
            activeOpacity={0.8}
          >
            <Text style={styles.buttonText}>Начать</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

function FeatureItem({
  emoji,
  title,
  description,
}: {
  emoji: string;
  title: string;
  description: string;
}) {
  return (
    <View style={styles.featureItem}>
      <Text style={styles.featureEmoji}>{emoji}</Text>
      <View style={styles.featureText}>
        <Text style={styles.featureTitle}>{title}</Text>
        <Text style={styles.featureDescription}>{description}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.secondary,
  },
  content: {
    flex: 1,
    paddingHorizontal: spacing.lg,
  },
  logoContainer: {
    alignItems: 'center',
    marginTop: spacing['3xl'],
    marginBottom: spacing.xl,
  },
  logoCircle: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: colors.primary.tiffanyBlue,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.md,
    ...shadows[2],
  },
  logoText: {
    fontSize: 48,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
  },
  appName: {
    fontSize: typography.fontSize.display,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
    letterSpacing: typography.letterSpacing.display,
    marginBottom: spacing.xs,
  },
  tagline: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
  },
  features: {
    flex: 1,
    justifyContent: 'center',
    gap: spacing.lg,
  },
  featureItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.background.default,
    padding: spacing.md,
    borderRadius: 16,
    ...shadows[1],
  },
  featureEmoji: {
    fontSize: 32,
    marginRight: spacing.md,
  },
  featureText: {
    flex: 1,
  },
  featureTitle: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
  },
  featureDescription: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    lineHeight: typography.lineHeight.body,
  },
  footer: {
    paddingBottom: spacing.xl,
  },
  primaryButton: {
    backgroundColor: colors.primary.tiffanyBlue,
    paddingVertical: spacing.md,
    borderRadius: 12,
    alignItems: 'center',
    ...shadows[2],
  },
  buttonText: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
  },
});
