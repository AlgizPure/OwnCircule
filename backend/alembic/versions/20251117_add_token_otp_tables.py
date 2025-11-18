"""add_token_otp_tables

Revision ID: 20251117_add_token_otp_tables
Revises: 20251117_initial_user_business_tables
Create Date: 2025-11-17 12:00:00.000000

Description:
    Add tables for JWT authentication and SMS OTP verification:
    - tokens: Refresh token storage for JWT rotation
    - otp_codes: SMS OTP codes for phone verification

    See: docs/adr/ADR-004-jwt-authentication.md
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20251117_add_token_otp_tables'
down_revision: Union[str, None] = '20251117_initial_user_business_tables'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tokens and otp_codes tables"""

    # ===================================================================
    # TABLE: tokens
    # ===================================================================
    # Stores JWT refresh tokens for user authentication
    # Access tokens are stateless (not stored in DB)
    # ===================================================================
    op.create_table(
        'tokens',
        # Primary Key
        sa.Column('id', sa.Integer(), nullable=False),

        # Foreign Key to User
        sa.Column('user_id', sa.Integer(), nullable=False),

        # Token Data
        sa.Column(
            'token_hash',
            sa.String(length=64),
            nullable=False,
            comment='SHA-256 hash of refresh token'
        ),

        # Metadata
        sa.Column(
            'expires_at',
            sa.DateTime(timezone=True),
            nullable=False,
            comment='Token expiration timestamp (7 days from creation)'
        ),
        sa.Column(
            'is_revoked',
            sa.Boolean(),
            nullable=False,
            server_default=sa.text('false'),
            comment='True if token was revoked (logout, rotation, security)'
        ),

        # Audit Fields
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()')
        ),
        sa.Column(
            'revoked_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Timestamp when token was revoked'
        ),

        # Optional: Device/IP tracking for security
        sa.Column(
            'device_info',
            sa.String(length=255),
            nullable=True,
            comment='User-Agent or device identifier'
        ),
        sa.Column(
            'ip_address',
            sa.String(length=45),  # IPv6 max length
            nullable=True,
            comment='IP address where token was issued'
        ),

        # Constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    )

    # Indexes for tokens table
    op.create_index('ix_tokens_id', 'tokens', ['id'])
    op.create_index('ix_tokens_user_id', 'tokens', ['user_id'])
    op.create_index('ix_tokens_token_hash', 'tokens', ['token_hash'], unique=True)
    op.create_index('ix_tokens_expires_at', 'tokens', ['expires_at'])
    op.create_index('ix_tokens_is_revoked', 'tokens', ['is_revoked'])

    # ===================================================================
    # TABLE: otp_codes
    # ===================================================================
    # Stores SMS OTP codes for phone verification
    # Used during registration and login (if 2FA enabled)
    # ===================================================================
    op.create_table(
        'otp_codes',
        # Primary Key
        sa.Column('id', sa.Integer(), nullable=False),

        # Phone Number (not FK - user may not exist yet during registration)
        sa.Column(
            'phone',
            sa.String(length=20),
            nullable=False,
            comment='Phone number in format +7XXXXXXXXXX'
        ),

        # OTP Data
        sa.Column(
            'code_hash',
            sa.String(length=64),
            nullable=False,
            comment='SHA-256 hash of 6-digit OTP code'
        ),

        # Expiration & Usage
        sa.Column(
            'expires_at',
            sa.DateTime(timezone=True),
            nullable=False,
            comment='OTP expiration timestamp (5 minutes from creation)'
        ),
        sa.Column(
            'is_used',
            sa.Boolean(),
            nullable=False,
            server_default=sa.text('false'),
            comment='True if OTP was successfully verified'
        ),
        sa.Column(
            'attempts',
            sa.Integer(),
            nullable=False,
            server_default=sa.text('0'),
            comment='Number of failed verification attempts (max 3)'
        ),

        # Audit Fields
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text('now()')
        ),
        sa.Column(
            'used_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Timestamp when OTP was successfully used'
        ),

        # Optional: SMS delivery tracking
        sa.Column(
            'sms_status',
            sa.String(length=50),
            nullable=True,
            comment='SMS delivery status from SMS.ru API'
        ),
        sa.Column(
            'sms_id',
            sa.String(length=100),
            nullable=True,
            comment='SMS.ru message ID for tracking'
        ),

        # Constraints
        sa.PrimaryKeyConstraint('id'),
    )

    # Indexes for otp_codes table
    op.create_index('ix_otp_codes_id', 'otp_codes', ['id'])
    op.create_index('ix_otp_codes_phone', 'otp_codes', ['phone'])
    op.create_index('ix_otp_codes_expires_at', 'otp_codes', ['expires_at'])
    op.create_index('ix_otp_codes_is_used', 'otp_codes', ['is_used'])
    op.create_index('ix_otp_codes_created_at', 'otp_codes', ['created_at'])  # For rate limiting queries


def downgrade() -> None:
    """Drop tokens and otp_codes tables"""

    # Drop indexes first
    op.drop_index('ix_otp_codes_created_at', table_name='otp_codes')
    op.drop_index('ix_otp_codes_is_used', table_name='otp_codes')
    op.drop_index('ix_otp_codes_expires_at', table_name='otp_codes')
    op.drop_index('ix_otp_codes_phone', table_name='otp_codes')
    op.drop_index('ix_otp_codes_id', table_name='otp_codes')

    op.drop_index('ix_tokens_is_revoked', table_name='tokens')
    op.drop_index('ix_tokens_expires_at', table_name='tokens')
    op.drop_index('ix_tokens_token_hash', table_name='tokens')
    op.drop_index('ix_tokens_user_id', table_name='tokens')
    op.drop_index('ix_tokens_id', table_name='tokens')

    # Drop tables
    op.drop_table('otp_codes')
    op.drop_table('tokens')
