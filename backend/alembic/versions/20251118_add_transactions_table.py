"""add_transactions_table

Revision ID: 20251118_add_transactions_table
Revises: 20251117_add_token_otp_tables
Create Date: 2025-11-18 10:00:00.000000

Description:
    Add transactions table for tracking member purchases across businesses.
    Supports manual creation, CRM synchronization, and bonus accrual tracking.

    See: docs/requirements/module-03-transactions.md
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20251118_add_transactions_table'
down_revision: Union[str, None] = '20251117_add_token_otp_tables'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create transactions table"""

    # ===================================================================
    # CREATE ENUMS
    # ===================================================================
    op.execute("CREATE TYPE transaction_type AS ENUM ('purchase', 'bonus_redemption', 'refund', 'adjustment')")
    op.execute("CREATE TYPE transaction_status AS ENUM ('pending', 'completed', 'cancelled', 'failed')")

    # ===================================================================
    # TABLE: transactions
    # ===================================================================
    # Tracks member purchases across partner businesses
    # ===================================================================
    op.create_table(
        'transactions',
        # Primary Key
        sa.Column('id', sa.Integer(), nullable=False),

        # Foreign Keys
        sa.Column(
            'user_id',
            sa.Integer(),
            nullable=False,
            comment='Member who made the purchase'
        ),
        sa.Column(
            'business_id',
            sa.Integer(),
            nullable=False,
            comment='Business where purchase was made'
        ),

        # Transaction Data
        sa.Column(
            'amount',
            sa.Float(),
            nullable=False,
            comment='Transaction amount in rubles'
        ),
        sa.Column(
            'bonus_amount',
            sa.Float(),
            nullable=False,
            server_default=sa.text('0.0'),
            comment='Bonus amount accrued for this transaction'
        ),
        sa.Column(
            'bonus_redeemed',
            sa.Float(),
            nullable=False,
            server_default=sa.text('0.0'),
            comment='Bonus amount redeemed in this transaction'
        ),

        # Type & Status
        sa.Column(
            'type',
            sa.Enum('purchase', 'bonus_redemption', 'refund', 'adjustment', name='transaction_type'),
            nullable=False,
            server_default=sa.text("'purchase'"),
            comment='Transaction type'
        ),
        sa.Column(
            'status',
            sa.Enum('pending', 'completed', 'cancelled', 'failed', name='transaction_status'),
            nullable=False,
            server_default=sa.text("'pending'"),
            comment='Transaction status'
        ),

        # Business Category (denormalized for analytics)
        sa.Column(
            'category',
            sa.String(length=100),
            nullable=True,
            comment='Business category (Beauty, Fitness, Wellness, etc.)'
        ),

        # Optional Metadata
        sa.Column(
            'description',
            sa.Text(),
            nullable=True,
            comment='Transaction description or notes'
        ),
        sa.Column(
            'receipt_number',
            sa.String(length=100),
            nullable=True,
            comment='Receipt number from POS/CRM system'
        ),
        sa.Column(
            'external_id',
            sa.String(length=255),
            nullable=True,
            comment='ID from external CRM system (YCLIENTS, Iiko, 1C)'
        ),

        # Timestamps
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
            comment='Transaction creation timestamp'
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
            comment='Last update timestamp'
        ),
        sa.Column(
            'completed_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Timestamp when transaction was completed'
        ),
        sa.Column(
            'cancelled_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Timestamp when transaction was cancelled'
        ),

        # Constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ondelete='CASCADE'),
        sa.CheckConstraint('amount >= 0', name='check_amount_positive'),
        sa.CheckConstraint('bonus_amount >= 0', name='check_bonus_amount_positive'),
        sa.CheckConstraint('bonus_redeemed >= 0', name='check_bonus_redeemed_positive'),
    )

    # ===================================================================
    # INDEXES
    # ===================================================================
    op.create_index('ix_transactions_id', 'transactions', ['id'])
    op.create_index('ix_transactions_user_id', 'transactions', ['user_id'])
    op.create_index('ix_transactions_business_id', 'transactions', ['business_id'])
    op.create_index('ix_transactions_type', 'transactions', ['type'])
    op.create_index('ix_transactions_status', 'transactions', ['status'])
    op.create_index('ix_transactions_category', 'transactions', ['category'])
    op.create_index('ix_transactions_external_id', 'transactions', ['external_id'])
    op.create_index('ix_transactions_created_at', 'transactions', ['created_at'])

    # Composite index for common queries (user's transactions ordered by date)
    op.create_index(
        'ix_transactions_user_created',
        'transactions',
        ['user_id', 'created_at'],
        postgresql_ops={'created_at': 'DESC'}
    )

    # Composite index for analytics (business transactions by date)
    op.create_index(
        'ix_transactions_business_created',
        'transactions',
        ['business_id', 'created_at'],
        postgresql_ops={'created_at': 'DESC'}
    )


def downgrade() -> None:
    """Drop transactions table"""

    # Drop indexes
    op.drop_index('ix_transactions_business_created', table_name='transactions')
    op.drop_index('ix_transactions_user_created', table_name='transactions')
    op.drop_index('ix_transactions_created_at', table_name='transactions')
    op.drop_index('ix_transactions_external_id', table_name='transactions')
    op.drop_index('ix_transactions_category', table_name='transactions')
    op.drop_index('ix_transactions_status', table_name='transactions')
    op.drop_index('ix_transactions_type', table_name='transactions')
    op.drop_index('ix_transactions_business_id', table_name='transactions')
    op.drop_index('ix_transactions_user_id', table_name='transactions')
    op.drop_index('ix_transactions_id', table_name='transactions')

    # Drop table
    op.drop_table('transactions')

    # Drop enums
    op.execute('DROP TYPE transaction_status')
    op.execute('DROP TYPE transaction_type')
