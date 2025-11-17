"""Initial migration: User and Business tables

Revision ID: 001_initial
Revises: 
Create Date: 2025-11-17 20:30:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create enum types
    op.execute("CREATE TYPE user_role AS ENUM ('member', 'business_admin', 'super_admin')")
    op.execute("CREATE TYPE status_tier AS ENUM ('insider', 'vip', 'elite', 'inner_circle')")
    
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('first_name', sa.String(length=100), nullable=False),
        sa.Column('last_name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('role', postgresql.ENUM('member', 'business_admin', 'super_admin', name='user_role'), nullable=False, server_default='member'),
        sa.Column('status_tier', postgresql.ENUM('insider', 'vip', 'elite', 'inner_circle', name='status_tier'), nullable=False, server_default='insider'),
        sa.Column('total_spend', sa.Float(), nullable=False, server_default='0'),
        sa.Column('bonus_balance', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('is_verified', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('last_login_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indexes for users
    op.create_index('ix_users_id', 'users', ['id'])
    op.create_index('ix_users_phone', 'users', ['phone'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    
    # Create businesses table
    op.create_table(
        'businesses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('slug', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('category', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('website', sa.String(length=500), nullable=True),
        sa.Column('address', sa.String(length=500), nullable=True),
        sa.Column('city', sa.String(length=100), nullable=False, server_default='Москва'),
        sa.Column('coordinates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('bonus_percentage', sa.Float(), nullable=False, server_default='5.0'),
        sa.Column('accepts_bonus_redemption', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('crm_type', sa.String(length=50), nullable=True),
        sa.Column('crm_credentials', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('logo_url', sa.String(length=500), nullable=True),
        sa.Column('cover_image_url', sa.String(length=500), nullable=True),
        sa.Column('gallery_urls', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('is_featured', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indexes for businesses
    op.create_index('ix_businesses_id', 'businesses', ['id'])
    op.create_index('ix_businesses_slug', 'businesses', ['slug'], unique=True)
    op.create_index('ix_businesses_name', 'businesses', ['name'])
    op.create_index('ix_businesses_category', 'businesses', ['category'])


def downgrade() -> None:
    # Drop businesses table
    op.drop_index('ix_businesses_category', table_name='businesses')
    op.drop_index('ix_businesses_name', table_name='businesses')
    op.drop_index('ix_businesses_slug', table_name='businesses')
    op.drop_index('ix_businesses_id', table_name='businesses')
    op.drop_table('businesses')
    
    # Drop users table
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_phone', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    
    # Drop enum types
    op.execute('DROP TYPE status_tier')
    op.execute('DROP TYPE user_role')
