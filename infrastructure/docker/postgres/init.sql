-- PostgreSQL Initialization Script
-- Creates database, extensions, and initial configuration

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For text search
CREATE EXTENSION IF NOT EXISTS "btree_gin"; -- For GIN indexes

-- Set timezone
SET timezone = 'Europe/Moscow';

-- Create database schema is handled by Alembic migrations
-- This file is for extensions and initial setup only

-- Log initialization
DO $$
BEGIN
    RAISE NOTICE 'PostgreSQL initialized for OwnCircule at %', NOW();
END
$$;
