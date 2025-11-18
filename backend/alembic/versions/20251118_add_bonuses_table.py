"""add_bonuses_table

Revision ID: 20251118_add_bonuses_table
Revises: 20251118_add_transactions_table
Create Date: 2025-11-18 11:00:00.000000

Description:
    Add bonuses table for loyalty points accrual and redemption.
    Supports automatic accrual from transactions, redemption, expiry, and manual adjustments.

    See: docs/requirements/module-02-loyalty-system.md
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20251118_add_bonuses_table'
down_revision: Union[str, None] = '20251118_add_transactions_table'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create bonuses table"""

    # ===================================================================
    # CREATE ENUMS
    # ===================================================================
    op.execute("CREATE TYPE bonus_type AS ENUM ('accrual', 'redemption', 'expiry', 'adjustment', 'gift')")
    op.execute("CREATE TYPE bonus_status AS ENUM ('pending', 'completed', 'cancelled', 'expired')")

    # ===================================================================
    # TABLE: bonuses
    # ===================================================================
    # Tracks bonus points accrual and redemption
    # ===================================================================
    op.create_table(
        'bonuses',
        # Primary Key
        sa.Column('id', sa.Integer(), nullable=False),

        # Foreign Keys
        sa.Column(
            'user_id',
            sa.Integer(),
            nullable=False,
            comment='User who earned/redeemed bonuses'
        ),
        sa.Column(
            'transaction_id',
            sa.Integer(),
            nullable=True,
            comment='Transaction that triggered bonus (null for manual adjustments)'
        ),

        # Bonus Data
        sa.Column(
            'amount',
            sa.Float(),
            nullable=False,
            comment='Bonus amount (positive for accrual, negative for redemption)'
        ),

        # Type & Status
        sa.Column(
            'type',
            sa.Enum('accrual', 'redemption', 'expiry', 'adjustment', 'gift', name='bonus_type'),
            nullable=False,
            server_default=sa.text("'accrual'"),
            comment='Bonus type'
        ),
        sa.Column(
            'status',
            sa.Enum('pending', 'completed', 'cancelled', 'expired', name='bonus_status'),
            nullable=False,
            server_default=sa.text("'pending'"),
            comment='Bonus status'
        ),

        # Expiration
        sa.Column(
            'expires_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Bonus expiration date (1 year from accrual)'
        ),

        # Metadata
        sa.Column(
            'description',
            sa.Text(),
            nullable=True,
            comment='Bonus description or notes'
        ),
        sa.Column(
            'multiplier',
            sa.Float(),
            nullable=False,
            server_default=sa.text('1.0'),
            comment='Multiplier applied (e.g., 1.5 for first purchase in category)'
        ),

        # Timestamps
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()')
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()')
        ),
        sa.Column(
            'completed_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Timestamp when bonus was completed'
        ),

        # Constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], ondelete='SET NULL'),
    )

    # ===================================================================
    # INDEXES
    # ===================================================================
    op.create_index('ix_bonuses_id', 'bonuses', ['id'])
    op.create_index('ix_bonuses_user_id', 'bonuses', ['user_id'])
    op.create_index('ix_bonuses_transaction_id', 'bonuses', ['transaction_id'])
    op.create_index('ix_bonuses_type', 'bonuses', ['type'])
    op.create_index('ix_bonuses_status', 'bonuses', ['status'])
    op.create_index('ix_bonuses_expires_at', 'bonuses', ['expires_at'])
    op.create_index('ix_bonuses_created_at', 'bonuses', ['created_at'])

    # Composite index for user bonus history (ordered by date)
    op.create_index(
        'ix_bonuses_user_created',
        'bonuses',
        ['user_id', 'created_at'],
        postgresql_ops={'created_at': 'DESC'}
    )

    # Index for expiry job (find bonuses expiring soon)
    op.create_index(
        'ix_bonuses_expiry',
        'bonuses',
        ['status', 'expires_at'],
        postgresql_where=sa.text("status = 'completed' AND expires_at IS NOT NULL")
    )


def downgrade() -> None:
    """Drop bonuses table"""

    # Drop indexes
    op.drop_index('ix_bonuses_expiry', table_name='bonuses')
    op.drop_index('ix_bonuses_user_created', table_name='bonuses')
    op.drop_index('ix_bonuses_created_at', table_name='bonuses')
    op.drop_index('ix_bonuses_expires_at', table_name='bonuses')
    op.drop_index('ix_bonuses_status', table_name='bonuses')
    op.drop_index('ix_bonuses_type', table_name='bonuses')
    op.drop_index('ix_bonuses_transaction_id', table_name='bonuses')
    op.drop_index('ix_bonuses_user_id', table_name='bonuses')
    op.drop_index('ix_bonuses_id', table_name='bonuses')

    # Drop table
    op.drop_table('bonuses')

    # Drop enums
    op.execute('DROP TYPE bonus_status')
    op.execute('DROP TYPE bonus_type')
