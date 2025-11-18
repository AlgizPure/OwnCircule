/**
 * Transaction Detail Screen
 * Shows full details of a single transaction
 */

import React, { useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  ScrollView,
  ActivityIndicator,
  TouchableOpacity,
} from 'react-native';
import { colors, typography, spacing, shadows } from '@/theme';
import { useAppDispatch, useAppSelector } from '@/store';
import {
  fetchTransactionById,
  selectCurrentTransaction,
  selectTransactionLoading,
  selectTransactionError,
} from '@/store/slices/transactionSlice';

interface TransactionDetailScreenProps {
  navigation: any;
  route: {
    params: {
      transactionId: number;
    };
  };
}

export default function TransactionDetailScreen({
  navigation,
  route,
}: TransactionDetailScreenProps) {
  const { transactionId } = route.params;
  const dispatch = useAppDispatch();

  const transaction = useAppSelector(selectCurrentTransaction);
  const isLoading = useAppSelector(selectTransactionLoading);
  const error = useAppSelector(selectTransactionError);

  useEffect(() => {
    dispatch(fetchTransactionById(transactionId));
  }, [transactionId]);

  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={colors.primary.tiffanyBlue} />
        </View>
      </SafeAreaView>
    );
  }

  if (error || !transaction) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <Text style={styles.errorEmoji}>❌</Text>
          <Text style={styles.errorTitle}>Ошибка загрузки</Text>
          <Text style={styles.errorText}>{error || 'Транзакция не найдена'}</Text>
          <TouchableOpacity style={styles.backButton} onPress={() => navigation.goBack()}>
            <Text style={styles.backButtonText}>Назад</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        {/* Header Card */}
        <View style={styles.headerCard}>
          <View style={styles.statusBadge}>
            <Text style={styles.statusText}>{formatStatus(transaction.status)}</Text>
          </View>

          <Text style={styles.amount}>
            {formatAmount(transaction.amount, transaction.type)}
          </Text>
          <Text style={styles.date}>{formatDate(transaction.createdAt)}</Text>
        </View>

        {/* Details Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Детали транзакции</Text>

          <DetailRow label="ID транзакции" value={`#${transaction.id}`} />
          <DetailRow label="Тип" value={formatType(transaction.type)} />
          <DetailRow label="Категория" value={transaction.category || '—'} />
          <DetailRow label="Статус" value={formatStatus(transaction.status)} />
        </View>

        {/* Bonus Info */}
        {transaction.bonusAmount > 0 && (
          <View style={styles.bonusCard}>
            <Text style={styles.bonusTitle}>Начислено бонусов</Text>
            <Text style={styles.bonusAmount}>+{transaction.bonusAmount} ₽</Text>
            <Text style={styles.bonusDescription}>
              Бонусы зачислены на ваш счёт и доступны для использования
            </Text>
          </View>
        )}

        {/* Additional Info */}
        {(transaction.description || transaction.receiptNumber) && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Дополнительная информация</Text>

            {transaction.description && (
              <DetailRow label="Описание" value={transaction.description} />
            )}
            {transaction.receiptNumber && (
              <DetailRow label="Номер чека" value={transaction.receiptNumber} />
            )}
          </View>
        )}

        {/* Timestamps */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Временные метки</Text>

          <DetailRow label="Создано" value={formatFullDate(transaction.createdAt)} />
          <DetailRow label="Обновлено" value={formatFullDate(transaction.updatedAt)} />
          {transaction.completedAt && (
            <DetailRow label="Завершено" value={formatFullDate(transaction.completedAt)} />
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// Helper component
function DetailRow({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.detailRow}>
      <Text style={styles.detailLabel}>{label}</Text>
      <Text style={styles.detailValue}>{value}</Text>
    </View>
  );
}

// Helper functions
function formatAmount(amount: number, type: string): string {
  const prefix = type === 'refund' ? '+' : '';
  return `${prefix}${amount.toLocaleString('ru-RU')} ₽`;
}

function formatStatus(status: string): string {
  const statusMap: Record<string, string> = {
    pending: 'Ожидает обработки',
    completed: 'Завершена',
    failed: 'Отклонена',
    cancelled: 'Отменена',
  };
  return statusMap[status] || status;
}

function formatType(type: string): string {
  const typeMap: Record<string, string> = {
    purchase: 'Покупка',
    bonus_redemption: 'Оплата бонусами',
    refund: 'Возврат',
    adjustment: 'Корректировка',
  };
  return typeMap[type] || type;
}

function formatDate(dateString: string): string {
  const date = new Date(dateString);
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}

function formatFullDate(dateString: string): string {
  const date = new Date(dateString);
  return date.toLocaleString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background.secondary,
  },
  content: {
    padding: spacing.lg,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: spacing.lg,
  },
  errorEmoji: {
    fontSize: 64,
    marginBottom: spacing.lg,
  },
  errorTitle: {
    fontSize: typography.fontSize.h3,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.sm,
  },
  errorText: {
    fontSize: typography.fontSize.body,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
    marginBottom: spacing.lg,
  },
  backButton: {
    backgroundColor: colors.primary.tiffanyBlue,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    borderRadius: 8,
  },
  backButtonText: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
  },
  headerCard: {
    backgroundColor: colors.primary.tiffanyBlue,
    borderRadius: 16,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    alignItems: 'center',
    ...shadows[2],
  },
  statusBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderRadius: 8,
    marginBottom: spacing.md,
  },
  statusText: {
    fontSize: typography.fontSize.caption,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.text,
  },
  amount: {
    fontSize: typography.fontSize.display,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.xs,
  },
  date: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.8)',
    fontFamily: typography.fontFamily.text,
  },
  section: {
    backgroundColor: colors.background.default,
    borderRadius: 12,
    padding: spacing.md,
    marginBottom: spacing.md,
    ...shadows[1],
  },
  sectionTitle: {
    fontSize: typography.fontSize.body,
    fontWeight: typography.fontWeight.semibold,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.md,
  },
  detailRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  detailLabel: {
    fontSize: typography.fontSize.caption,
    color: colors.text.secondary,
    fontFamily: typography.fontFamily.text,
    flex: 1,
  },
  detailValue: {
    fontSize: typography.fontSize.caption,
    fontWeight: typography.fontWeight.medium,
    color: colors.text.primary,
    fontFamily: typography.fontFamily.text,
    flex: 2,
    textAlign: 'right',
  },
  bonusCard: {
    backgroundColor: colors.primary.champagneGold,
    borderRadius: 12,
    padding: spacing.lg,
    marginBottom: spacing.md,
    alignItems: 'center',
    ...shadows[2],
  },
  bonusTitle: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.9)',
    fontFamily: typography.fontFamily.text,
    marginBottom: spacing.xs,
  },
  bonusAmount: {
    fontSize: typography.fontSize.h1,
    fontWeight: typography.fontWeight.bold,
    color: colors.text.onPrimary,
    fontFamily: typography.fontFamily.display,
    marginBottom: spacing.sm,
  },
  bonusDescription: {
    fontSize: typography.fontSize.caption,
    color: 'rgba(255, 255, 255, 0.8)',
    fontFamily: typography.fontFamily.text,
    textAlign: 'center',
  },
});
