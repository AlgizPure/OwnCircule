/**
 * Bonus History Screen
 * Displays user's bonus accrual and redemption history
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  FlatList,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import { useAppDispatch, useAppSelector } from '@/store';
import {
  fetchBonusBalance,
  fetchBonusHistory,
  selectBonusBalance,
  selectBonusHistory,
  selectBonusLoading,
  selectBonusError,
  selectBonusPagination,
} from '@/store/slices/bonusSlice';
import type { Bonus } from '@/services/bonusService';

export default function BonusHistoryScreen() {
  const dispatch = useAppDispatch();
  const balance = useAppSelector(selectBonusBalance);
  const bonusHistory = useAppSelector(selectBonusHistory);
  const isLoading = useAppSelector(selectBonusLoading);
  const error = useAppSelector(selectBonusError);
  const pagination = useAppSelector(selectBonusPagination);

  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    await Promise.all([
      dispatch(fetchBonusBalance()),
      dispatch(fetchBonusHistory({ page: 1, perPage: 50 })),
    ]);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadData();
    setRefreshing(false);
  };

  const loadMore = async () => {
    if (pagination.page * pagination.perPage < pagination.total && !isLoading) {
      await dispatch(fetchBonusHistory({ page: pagination.page + 1, perPage: 50 }));
    }
  };

  const renderBonus = ({ item }: { item: Bonus }) => (
    <View style={styles.bonusCard}>
      <View style={styles.bonusHeader}>
        <View style={styles.bonusIcon}>
          <Text style={styles.bonusEmoji}>{getBonusEmoji(item.type)}</Text>
        </View>

        <View style={styles.bonusInfo}>
          <Text style={styles.bonusType}>{formatBonusType(item.type)}</Text>
          <Text style={styles.bonusDate}>{formatDate(item.createdAt)}</Text>
        </View>

        <Text style={[styles.bonusAmount, getBonusAmountStyle(item.type)]}>
          {formatBonusAmount(item.amount)}
        </Text>
      </View>

      {item.multiplier > 1 && (
        <View style={styles.multiplierBadge}>
          <Text style={styles.multiplierText}>✨ {item.multiplier}x множитель</Text>
        </View>
      )}

      {item.expiresAt && item.status === 'active' && (
        <Text style={styles.expiryText}>
          Истекает: {formatDate(item.expiresAt)}
        </Text>
      )}

      {item.description && (
        <Text style={styles.bonusDescription}>{item.description}</Text>
      )}
    </View>
  );

  const renderEmpty = () => (
    <View style={styles.emptyContainer}>
      <Text style={styles.emptyEmoji}>🎁</Text>
      <Text style={styles.emptyTitle}>Нет истории</Text>
      <Text style={styles.emptyText}>
        Ваши начисления и списания бонусов будут отображаться здесь
      </Text>
    </View>
  );

  const renderFooter = () => {
    if (!isLoading || bonusHistory.length === 0) return null;
    return (
      <View style={styles.footerLoader}>
        <ActivityIndicator color={colors.primary.champagneGold} />
      </View>
    );
  };

  if (isLoading && bonusHistory.length === 0) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.balanceCard}>
          <Text style={styles.balanceLabel}>Баланс бонусов</Text>
          <ActivityIndicator color={colors.text.onPrimary} />
        </View>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={colors.primary.champagneGold} />
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      {/* Balance Card */}
      <View style={styles.balanceCard}>
        <Text style={styles.balanceLabel}>Баланс бонусов</Text>
        <Text style={styles.balanceValue}>{balance.toLocaleString('ru-RU')} ₽</Text>
        <Text style={styles.balanceDescription}>
          Используйте бонусы для оплаты покупок у партнёров
        </Text>
      </View>

      {/* Error Banner */}
      {error && (
        <View style={styles.errorBanner}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      )}

      {/* History List */}
      <View style={styles.historyHeader}>
        <Text style={styles.historyTitle}>История операций</Text>
        {pagination.total > 0 && (
          <Text style={styles.historySubtitle}>
            Всего: {pagination.total} {pluralizeBonuses(pagination.total)}
          </Text>
        )}
      </View>

      <FlatList
        data={bonusHistory}
        renderItem={renderBonus}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.listContent}
        ListEmptyComponent={renderEmpty}
        ListFooterComponent={renderFooter}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
            tintColor={colors.primary.champagneGold}
          />
        }
        onEndReached={loadMore}
        onEndReachedThreshold={0.5}
      />
    </SafeAreaView>
  );
}

// Helper functions
function getBonusEmoji(type: string): string {
  const emojiMap: Record<string, string> = {
    accrual: '➕',
    redemption: '➖',
    expiry: '⏰',
    adjustment: '🔧',
    gift: '🎁',
  };
  return emojiMap[type] || '💰';
}

function formatBonusType(type: string): string {
  const typeMap: Record<string, string> = {
    accrual: 'Начисление',
    redemption: 'Списание',
    expiry: 'Сгорание',
    adjustment: 'Корректировка',
    gift: 'Подарок',
  };
  return typeMap[type] || type;
}

function formatBonusAmount(amount: number): string {
  const prefix = amount > 0 ? '+' : '';
  return `${prefix}${Math.abs(amount).toLocaleString('ru-RU')} ₽`;
}

function getBonusAmountStyle(type: string) {
  if (type === 'accrual' || type === 'gift') {
    return { color: colors.success };
  }
  if (type === 'redemption') {
    return { color: colors.error };
  }
  return { color: colors.text.secondary };
}

function formatDate(dateString: string): string {
  const date = new Date(dateString);
  const now = new Date();
  const diffInDays = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24));

  if (diffInDays === 0) {
    return `Сегодня, ${date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })}`;
  } else if (diffInDays === 1) {
    return `Вчера, ${date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })}`;
  } else if (diffInDays < 7) {
    return `${diffInDays} ${pluralizeDays(diffInDays)} назад`;
  } else {
    return date.toLocaleDateString('ru-RU', {
      day: 'numeric',
      month: 'short',
      year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined,
    });
  }
}

function pluralizeDays(count: number): string {
  if (count % 10 === 1 && count % 100 !== 11) return 'день';
  if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100)) return 'дня';
  return 'дней';
}

function pluralizeBonuses(count: number): string {
  if (count % 10 === 1 && count % 100 !== 11) return 'операция';
  if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100))
    return 'операции';
  return 'операций';
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.secondary,
  },
  balanceCard: {
    backgroundColor: colors.primary.champagneGold,
    padding: spacing.lg,
    alignItems: 'center',
    ...shadows[2],
  },
  balanceLabel: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.9)',
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
  },
  balanceValue: {
    fontSize: typography.fontSize.display,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.sm,
  },
  balanceDescription: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.8)',
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
  },
  historyHeader: {
    backgroundColor: colors.background.default,
    padding: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  historyTitle: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
  },
  historySubtitle: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    marginTop: spacing.xs,
  },
  listContent: {
    padding: spacing.lg,
  },
  bonusCard: {
    backgroundColor: colors.background.default,
    borderRadius: 12,
    padding: spacing.md,
    marginBottom: spacing.md,
    ...shadows[1],
  },
  bonusHeader: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  bonusIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: colors.background.secondary,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: spacing.md,
  },
  bonusEmoji: {
    fontSize: 20,
  },
  bonusInfo: {
    flex: 1,
  },
  bonusType: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
  },
  bonusDate: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
  },
  bonusAmount: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.bold,
    fontFamily: typography.fontFamily.display,
  },
  multiplierBadge: {
    backgroundColor: colors.primary.champagneGold,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: 6,
    alignSelf: 'flex-start',
    marginTop: spacing.sm,
  },
  multiplierText: {
    fontSize: typography.fontSize.caption,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
    fontWeight: typography.fontWeight.medium,
  },
  expiryText: {
    fontSize: typography.fontSize.caption,
    color: colors.warning,
    fontFamily: typography.fontFamily.text,
    marginTop: spacing.sm,
  },
  bonusDescription: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    marginTop: spacing.sm,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  emptyContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingVertical: spacing.xl * 2,
  },
  emptyEmoji: {
    fontSize: 64,
    marginBottom: spacing.lg,
  },
  emptyTitle: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.sm,
  },
  emptyText: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    paddingHorizontal: spacing.lg,
  },
  errorBanner: {
    backgroundColor: colors.error,
    padding: spacing.md,
    marginHorizontal: spacing.lg,
    marginTop: spacing.md,
    borderRadius: 8,
  },
  errorText: {
    fontSize: typography.fontSize.caption,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
  },
  footerLoader: {
    paddingVertical: spacing.lg,
    alignItems: 'center',
  },
});
