"""add_user_categories_table

Revision ID: 20251118_add_user_categories_table
Revises: 20251118_add_bonuses_table
Create Date: 2025-11-18 11:15:00.000000

Description:
    Add user_categories table to track which categories user has purchased in.
    Used for first purchase multiplier (1.5x bonus).

    See: docs/requirements/module-02-loyalty-system.md (Function 2.1.2)
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20251118_add_user_categories_table'
down_revision: Union[str, None] = '20251118_add_bonuses_table'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create user_categories table"""

    # ===================================================================
    # TABLE: user_categories
    # ===================================================================
    # Tracks which categories user has made purchases in
    # Used for first purchase in category multiplier (1.5x)
    # ===================================================================
    op.create_table(
        'user_categories',
        # Primary Key
        sa.Column('id', sa.Integer(), nullable=False),

        # Foreign Key
        sa.Column(
            'user_id',
            sa.Integer(),
            nullable=False,
            comment='User ID'
        ),

        # Category
        sa.Column(
            'category',
            sa.String(length=100),
            nullable=False,
            comment='Business category (Beauty, Fitness, Wellness, etc.)'
        ),

        # First Purchase Info
        sa.Column(
            'first_purchase_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
            comment='Timestamp of first purchase in this category'
        ),

        sa.Column(
            'first_transaction_id',
            sa.Integer(),
            nullable=True,
            comment='ID of first transaction in this category'
        ),

        # Stats
        sa.Column(
            'total_purchases',
            sa.Integer(),
            nullable=False,
            server_default=sa.text('1'),
            comment='Total number of purchases in this category'
        ),

        sa.Column(
            'total_spent',
            sa.Float(),
            nullable=False,
            server_default=sa.text('0.0'),
            comment='Total amount spent in this category'
        ),

        # Timestamps
        sa.Column(
            'last_purchase_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()'),
            comment='Timestamp of most recent purchase in this category'
        ),

        # Constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['first_transaction_id'], ['transactions.id'], ondelete='SET NULL'),
        sa.UniqueConstraint('user_id', 'category', name='uq_user_category'),
    )

    # ===================================================================
    # INDEXES
    # ===================================================================
    op.create_index('ix_user_categories_id', 'user_categories', ['id'])
    op.create_index('ix_user_categories_user_id', 'user_categories', ['user_id'])
    op.create_index('ix_user_categories_category', 'user_categories', ['category'])


def downgrade() -> None:
    """Drop user_categories table"""

    # Drop indexes
    op.drop_index('ix_user_categories_category', table_name='user_categories')
    op.drop_index('ix_user_categories_user_id', table_name='user_categories')
    op.drop_index('ix_user_categories_id', table_name='user_categories')

    # Drop table
    op.drop_table('user_categories')
