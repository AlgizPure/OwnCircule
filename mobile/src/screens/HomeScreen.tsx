/**
 * Home Screen
 * Main dashboard with real user data from API
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  StatusBar,
  ScrollView,
  TouchableOpacity,
  RefreshControl,
  ActivityIndicator,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import type { MainTabScreenProps } from '@/types/navigation';
import { useAppDispatch, useAppSelector } from '@/store';
import { selectCurrentUser } from '@/store/slices/userSlice';
import {
  fetchBonusBalance,
  selectBonusBalance,
  selectBonusLoading,
} from '@/store/slices/bonusSlice';

export default function HomeScreen({ navigation }: MainTabScreenProps<'Home'>) {
  const dispatch = useAppDispatch();
  const user = useAppSelector(selectCurrentUser);
  const bonusBalance = useAppSelector(selectBonusBalance);
  const isLoadingBonus = useAppSelector(selectBonusLoading);

  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    await dispatch(fetchBonusBalance());
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadData();
    setRefreshing(false);
  };

  const navigateToBonusHistory = () => {
    navigation.navigate('Bonuses');
  };

  // Calculate next tier progress
  const tierInfo = calculateTierProgress(user?.statusTier || 'insider', user?.totalSpend || 0);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={colors.background.default} />

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.content}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
            tintColor={colors.primary.tiffanyBlue}
          />
        }
      >
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.greeting}>
            Здравствуйте, {user?.firstName || 'Гость'}!
          </Text>
          <Text style={styles.subtitle}>Свой Круг</Text>
        </View>

        {/* Status Card */}
        <TouchableOpacity
          style={styles.statusCard}
          activeOpacity={0.9}
        >
          <View style={styles.statusHeader}>
            <Text style={styles.statusTier}>{formatTierName(user?.statusTier || 'insider')}</Text>
            <View style={styles.tierBadge}>
              <Text style={styles.tierBadgeText}>Ваш статус</Text>
            </View>
          </View>

          <View style={styles.balanceRow}>
            <View style={styles.balanceItem}>
              <Text style={styles.balanceLabel}>Баллы</Text>
              {isLoadingBonus ? (
                <ActivityIndicator color={colors.text.onPrimary} />
              ) : (
                <Text style={styles.balanceValue}>
                  {bonusBalance.toLocaleString('ru-RU')}
                </Text>
              )}
            </View>
            <View style={styles.balanceDivider} />
            <View style={styles.balanceItem}>
              <Text style={styles.balanceLabel}>Траты</Text>
              <Text style={styles.balanceValue}>
                {(user?.totalSpend || 0).toLocaleString('ru-RU')} ₽
              </Text>
            </View>
          </View>

          {tierInfo.nextTier && (
            <Text style={styles.statusFooter}>
              До статуса {tierInfo.nextTier} осталось потратить{' '}
              {tierInfo.amountToNextTier.toLocaleString('ru-RU')} ₽
            </Text>
          )}
        </TouchableOpacity>

        {/* Quick Actions */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Быстрые действия</Text>

          <View style={styles.actionGrid}>
            <ActionCard title="Бонусы" emoji="🎁" onPress={navigateToBonusHistory} />
            <ActionCard title="Мероприятия" emoji="✨" onPress={() => {}} />
            <ActionCard title="Партнёры" emoji="💎" onPress={() => {}} />
            <ActionCard title="QR-кошелёк" emoji="📱" onPress={() => {}} />
          </View>
        </View>

        {/* Cashback Info */}
        <View style={styles.infoCard}>
          <Text style={styles.infoTitle}>💰 Ваш кэшбэк</Text>
          <Text style={styles.infoText}>
            С текущим статусом {formatTierName(user?.statusTier || 'insider')} вы получаете{' '}
            {tierInfo.cashbackRate}% от каждой покупки в виде бонусов
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

function ActionCard({
  title,
  emoji,
  onPress,
}: {
  title: string;
  emoji: string;
  onPress?: () => void;
}) {
  return (
    <TouchableOpacity
      style={styles.actionCard}
      activeOpacity={0.7}
      onPress={onPress}
    >
      <Text style={styles.actionEmoji}>{emoji}</Text>
      <Text style={styles.actionTitle}>{title}</Text>
    </TouchableOpacity>
  );
}

// Helper functions
function formatTierName(tier: string): string {
  const tierNames: Record<string, string> = {
    insider: 'INSIDER',
    vip: 'VIP',
    elite: 'ELITE',
    inner_circle: 'INNER CIRCLE',
  };
  return tierNames[tier] || tier.toUpperCase();
}

function calculateTierProgress(tier: string, totalSpend: number) {
  const tiers = {
    insider: { threshold: 0, cashback: '5', next: 'VIP', nextThreshold: 50000 },
    vip: { threshold: 50000, cashback: '7', next: 'ELITE', nextThreshold: 150000 },
    elite: { threshold: 150000, cashback: '10', next: 'INNER CIRCLE', nextThreshold: 300000 },
    inner_circle: { threshold: 300000, cashback: '15', next: null, nextThreshold: null },
  };

  const currentTier = tiers[tier as keyof typeof tiers] || tiers.insider;

  return {
    cashbackRate: currentTier.cashback,
    nextTier: currentTier.next,
    amountToNextTier: currentTier.nextThreshold
      ? Math.max(0, currentTier.nextThreshold - totalSpend)
      : 0,
  };
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
  infoTitle: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
    textAlign: 'center',
  },
  infoText: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    lineHeight: typography.lineHeight.caption,
  },
});
