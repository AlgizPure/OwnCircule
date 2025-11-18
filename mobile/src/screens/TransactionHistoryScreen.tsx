/**
 * Transaction History Screen
 * Displays user's transaction history with filtering and pagination
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import { useAppDispatch, useAppSelector } from '@/store';
import {
  fetchTransactions,
  selectTransactions,
  selectTransactionLoading,
  selectTransactionError,
  selectTransactionPagination,
} from '@/store/slices/transactionSlice';
import type { Transaction } from '@/services/transactionService';

interface TransactionHistoryScreenProps {
  navigation: any;
}

export default function TransactionHistoryScreen({ navigation }: TransactionHistoryScreenProps) {
  const dispatch = useAppDispatch();
  const transactions = useAppSelector(selectTransactions);
  const isLoading = useAppSelector(selectTransactionLoading);
  const error = useAppSelector(selectTransactionError);
  const pagination = useAppSelector(selectTransactionPagination);

  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadTransactions();
  }, []);

  const loadTransactions = async () => {
    await dispatch(fetchTransactions({ page: 1, perPage: 20 }));
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadTransactions();
    setRefreshing(false);
  };

  const loadMore = async () => {
    if (pagination.page < pagination.totalPages && !isLoading) {
      await dispatch(fetchTransactions({ page: pagination.page + 1, perPage: 20 }));
    }
  };

  const navigateToDetail = (transactionId: number) => {
    navigation.navigate('TransactionDetail', { transactionId });
  };

  const renderTransaction = ({ item }: { item: Transaction }) => (
    <TouchableOpacity
      style={styles.transactionCard}
      onPress={() => navigateToDetail(item.id)}
      activeOpacity={0.7}
    >
      <View style={styles.transactionHeader}>
        <Text style={styles.businessName}>{item.category || 'Покупка'}</Text>
        <Text style={[styles.amount, getAmountStyle(item.type)]}>
          {formatAmount(item.amount, item.type)}
        </Text>
      </View>

      <View style={styles.transactionDetails}>
        <Text style={styles.date}>{formatDate(item.createdAt)}</Text>
        <View style={styles.statusBadge}>
          <Text style={styles.statusText}>{formatStatus(item.status)}</Text>
        </View>
      </View>

      {item.bonusAmount > 0 && (
        <View style={styles.bonusInfo}>
          <Text style={styles.bonusText}>+{item.bonusAmount} бонусов</Text>
        </View>
      )}
    </TouchableOpacity>
  );

  const renderEmpty = () => (
    <View style={styles.emptyContainer}>
      <Text style={styles.emptyEmoji}>📝</Text>
      <Text style={styles.emptyTitle}>Нет транзакций</Text>
      <Text style={styles.emptyText}>
        Ваши покупки будут отображаться здесь
      </Text>
    </View>
  );

  const renderFooter = () => {
    if (!isLoading || transactions.length === 0) return null;
    return (
      <View style={styles.footerLoader}>
        <ActivityIndicator color={colors.primary.tiffanyBlue} />
      </View>
    );
  };

  if (isLoading && transactions.length === 0) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.header}>
          <Text style={styles.headerTitle}>История покупок</Text>
        </View>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={colors.primary.tiffanyBlue} />
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>История покупок</Text>
        {pagination.total > 0 && (
          <Text style={styles.headerSubtitle}>
            Всего: {pagination.total} {pluralizeTransactions(pagination.total)}
          </Text>
        )}
      </View>

      {error && (
        <View style={styles.errorBanner}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      )}

      <FlatList
        data={transactions}
        renderItem={renderTransaction}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.listContent}
        ListEmptyComponent={renderEmpty}
        ListFooterComponent={renderFooter}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
            tintColor={colors.primary.tiffanyBlue}
          />
        }
        onEndReached={loadMore}
        onEndReachedThreshold={0.5}
      />
    </SafeAreaView>
  );
}

// Helper functions
function formatAmount(amount: number, type: string): string {
  const prefix = type === 'refund' ? '+' : '';
  return `${prefix}${amount.toLocaleString('ru-RU')} ₽`;
}

function getAmountStyle(type: string) {
  if (type === 'refund') {
    return { color: colors.success };
  }
  if (type === 'bonus_redemption') {
    return { color: colors.primary.champagneGold };
  }
  return {};
}

function formatDate(dateString: string): string {
  const date = new Date(dateString);
  const now = new Date();
  const diffInDays = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24));

  if (diffInDays === 0) {
    return `Сегодня, ${date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })}`;
  } else if (diffInDays === 1) {
    return `Вчера, ${date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' })}`;
  } else {
    return date.toLocaleDateString('ru-RU', {
      day: 'numeric',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit',
    });
  }
}

function formatStatus(status: string): string {
  const statusMap: Record<string, string> = {
    pending: 'Ожидает',
    completed: 'Завершена',
    failed: 'Отклонена',
    cancelled: 'Отменена',
  };
  return statusMap[status] || status;
}

function pluralizeTransactions(count: number): string {
  if (count % 10 === 1 && count % 100 !== 11) return 'транзакция';
  if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100))
    return 'транзакции';
  return 'транзакций';
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.secondary,
  },
  header: {
    backgroundColor: colors.background.default,
    padding: spacing.lg,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  headerTitle: {
    fontSize: typography.fontSize.h2,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
  },
  headerSubtitle: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    marginTop: spacing.xs,
  },
  listContent: {
    padding: spacing.lg,
  },
  transactionCard: {
    backgroundColor: colors.background.default,
    borderRadius: 12,
    padding: spacing.md,
    marginBottom: spacing.md,
    ...shadows[1],
  },
  transactionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: spacing.sm,
  },
  businessName: {
    flex: 1,
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
  },
  amount: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
  },
  transactionDetails: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  date: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
  },
  statusBadge: {
    backgroundColor: colors.background.secondary,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: 6,
  },
  statusText: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
  },
  bonusInfo: {
    marginTop: spacing.sm,
    paddingTop: spacing.sm,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  bonusText: {
    fontSize: typography.fontSize.caption,
    color: colors.primary.champagneGold,
    fontFamily: typography.fontFamily.text,
    fontWeight: typography.fontWeight.medium,
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
  },
  errorBanner: {
    backgroundColor: colors.error,
    padding: spacing.md,
    margin: spacing.lg,
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
