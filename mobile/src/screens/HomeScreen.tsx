/**
 * Home Screen
 * Main dashboard after login (placeholder for Sprint 2)
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  StatusBar,
  ScrollView,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import type { MainTabScreenProps } from '@/types/navigation';

export default function HomeScreen({}: MainTabScreenProps<'Home'>) {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={colors.background.default} />

      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.greeting}>Добро пожаловать!</Text>
          <Text style={styles.subtitle}>Свой Круг</Text>
        </View>

        {/* Status Card */}
        <View style={styles.statusCard}>
          <View style={styles.statusHeader}>
            <Text style={styles.statusTier}>INSIDER</Text>
            <View style={styles.tierBadge}>
              <Text style={styles.tierBadgeText}>Ваш статус</Text>
            </View>
          </View>

          <View style={styles.balanceRow}>
            <View style={styles.balanceItem}>
              <Text style={styles.balanceLabel}>Баллы</Text>
              <Text style={styles.balanceValue}>0</Text>
            </View>
            <View style={styles.balanceDivider} />
            <View style={styles.balanceItem}>
              <Text style={styles.balanceLabel}>Траты</Text>
              <Text style={styles.balanceValue}>0 ₽</Text>
            </View>
          </View>

          <Text style={styles.statusFooter}>
            До статуса VIP осталось потратить 50 000 ₽
          </Text>
        </View>

        {/* Quick Actions (Placeholder) */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Быстрые действия</Text>

          <View style={styles.actionGrid}>
            <ActionCard title="Бонусы" emoji="🎁" />
            <ActionCard title="Мероприятия" emoji="✨" />
            <ActionCard title="Партнёры" emoji="💎" />
            <ActionCard title="QR-кошелёк" emoji="📱" />
          </View>
        </View>

        {/* Info */}
        <View style={styles.infoCard}>
          <Text style={styles.infoText}>
            Это демо-версия приложения для Sprint 1.{'\n'}
            Полный функционал будет доступен в Sprint 2.
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

function ActionCard({ title, emoji }: { title: string; emoji: string }) {
  return (
    <View style={styles.actionCard}>
      <Text style={styles.actionEmoji}>{emoji}</Text>
      <Text style={styles.actionTitle}>{title}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.secondary,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: spacing.lg,
  },
  header: {
    marginBottom: spacing.lg,
  },
  greeting: {
    fontSize: typography.fontSize.h1,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.xs,
  },
  subtitle: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
  },
  statusCard: {
    backgroundColor: colors.primary.tiffanyBlue,
    borderRadius: 16,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    ...shadows[2],
  },
  statusHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  statusTier: {
    fontSize: typography.fontSize.h2,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
  },
  tierBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: 8,
  },
  tierBadgeText: {
    fontSize: typography.fontSize.caption,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
  },
  balanceRow: {
    flexDirection: 'row',
    marginBottom: spacing.md,
  },
  balanceItem: {
    flex: 1,
  },
  balanceDivider: {
    width: 1,
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
    marginHorizontal: spacing.md,
  },
  balanceLabel: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.8)',
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
  },
  balanceValue: {
    fontSize: typography.fontSize.h1,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
  },
  statusFooter: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.8)',
    fontFamily: typography.fontFamily.text,
  },
  section: {
    marginBottom: spacing.lg,
  },
  sectionTitle: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.md,
  },
  actionGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.md,
  },
  actionCard: {
    width: '47%',
    backgroundColor: colors.background.default,
    borderRadius: 12,
    padding: spacing.md,
    alignItems: 'center',
    ...shadows[1],
  },
  actionEmoji: {
    fontSize: 32,
    marginBottom: spacing.sm,
  },
  actionTitle: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
  },
  infoCard: {
    backgroundColor: colors.background.default,
    borderRadius: 12,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: colors.primary.tiffanyBlue,
  },
  infoText: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    lineHeight: typography.lineHeight.caption,
  },
});
