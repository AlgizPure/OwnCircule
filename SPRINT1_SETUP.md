# SPRINT 1 SETUP: OwnCircule Infrastructure Guide

**Document Version:** 1.0
**Last Updated:** 2025-11-17
**Sprint Duration:** 2 weeks
**Status:** Ready for Development
**Design Color:** Tiffany Blue (#0ABAB5)

---

## 1. SPRINT 1 OVERVIEW

### Goal
Establish a fully functional development environment for the OwnCircule platform with all infrastructure components operational and ready for feature development in Sprint 2.

### Timeline
- **Duration:** 2 weeks (Week 1-2)
- **Setup Phase:** Days 1-3 (Initial infrastructure)
- **Testing & Validation:** Days 4-5
- **Documentation & Onboarding:** Days 6-10

### Deliverables
- ✓ Docker infrastructure running (PostgreSQL, Redis, ClickHouse)
- ✓ Backend FastAPI server operational with database migrations
- ✓ Mobile development environment configured for iOS/Android
- ✓ All team members with working local environments
- ✓ CI/CD pipelines tested and validated
- ✓ Documentation complete and verified

### Success Criteria
- [ ] Backend API responds to `GET /health` with 200 status
- [ ] PostgreSQL contains all database tables from migrations
- [ ] React Native app builds successfully on iOS and Android simulators
- [ ] All tests pass (backend: >80% coverage, mobile: >70%)
- [ ] Team members can run full stack in < 15 minutes
- [ ] No critical issues in Sentry or logs

---

## 2. PREREQUISITES

### System Requirements

#### Minimum Hardware
- **CPU:** 4 cores (8 cores recommended)
- **RAM:** 8GB (16GB recommended for mobile development)
- **Disk:** 50GB free space
- **Network:** Stable internet connection (≥5 Mbps)

#### Supported Operating Systems
- **macOS:** 14+ (Sonoma, Sequoia)
- **Ubuntu/Linux:** 22.04 LTS or newer
- **Windows:** 11 with WSL2 Ubuntu 22.04

### Required Software Versions

| Component | Version | Download |
|-----------|---------|----------|
| **Python** | 3.13.x | https://www.python.org/downloads/ |
| **Node.js** | 20.x LTS | https://nodejs.org/ |
| **npm** | 10.x+ | Included with Node.js |
| **Docker Desktop** | 27.x+ | https://www.docker.com/products/docker-desktop |
| **Docker Compose** | 2.24.x+ | Included with Docker Desktop |
| **Git** | 2.40+ | https://git-scm.com/downloads |

### Platform-Specific Prerequisites

#### macOS
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required tools
brew install python@3.13
brew install node@20
brew install docker
brew install git
brew install watchman  # For React Native file watching
brew install cocoapods # For iOS dependency management

# Verify installations
python3 --version     # Should show 3.13.x
node --version        # Should show 20.x
npm --version         # Should show 10.x
docker --version      # Should show 27.x
```

#### Ubuntu/Linux
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.13
sudo apt install -y python3.13 python3.13-venv python3-pip

# Install Node.js 20 (via NodeSource repository)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker  # Activate docker group without logout

# Install additional tools
sudo apt install -y git watchman

# Verify installations
python3.13 --version  # Should show 3.13.x
node --version        # Should show 20.x
docker --version      # Should show 27.x
```

#### Windows 11 (WSL2)
```powershell
# Enable WSL2 (run as Administrator)
wsl --install -d Ubuntu-22.04

# Restart Windows and complete Ubuntu setup
# Then in Ubuntu terminal, run the Linux commands above
```

### IDE Setup (Recommended)

#### Backend Development
- **PyCharm Professional** or **VSCode + Python Extension**
- Extensions:
  - `ms-python.python` - Python support
  - `ms-python.vscode-pylance` - Type checking
  - `charliermarsh.ruff` - Fast Python linting
  - `ms-azuretools.vscode-docker` - Docker support

#### Mobile Development
- **VSCode with React Native Tools** or **Android Studio**
- Extensions:
  - `msjsdiag.vscode-react-native` - React Native debugging
  - `dsznajder.es7-react-js-snippets` - React snippets
  - `dbaeumer.vscode-eslint` - ESLint integration
  - `esbenp.prettier-vscode` - Code formatting

#### Optional: AI Assistance
- **Cursor IDE** (alternative VSCode with integrated Claude/GPT)
- **GitHub Copilot** (VSCode extension)

---

## 3. QUICK START

### Step 1: Clone Repository & Configure Git

```bash
# Clone the repository
git clone https://github.com/AlgizPure/OwnCircule.git
cd OwnCircule

# Checkout the development branch
git checkout claude/upmt-start-1-3-01NzbZsT7jYrAdgQsXszWpS4

# Verify current branch
git branch --show-current
# Output: claude/upmt-start-1-3-01NzbZsT7jYrAdgQsXszWpS4

# Configure Git user (if not already set)
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 2: Create Environment Files

```bash
# Backend environment
cp backend/.env.example backend/.env

# Mobile environment
cp mobile/.env.example mobile/.env

# Edit backend/.env with your local settings
cat << 'EOF' > backend/.env
# Database
DATABASE_URL=postgresql+asyncpg://postgres:postgres_dev_password@localhost:5432/owncircle_dev

# Cache & Queue
REDIS_URL=redis://localhost:6379/0

# Analytics
CLICKHOUSE_URL=clickhouse://clickhouse:clickhouse_dev_password@localhost:9000/analytics

# Security
JWT_SECRET_KEY=dev_secret_key_change_in_production
ENCRYPTION_KEY=dev_encryption_key_change_in_production

# Environment
ENVIRONMENT=development
DEBUG=true

# External Services (get these from your team lead)
SMS_RU_API_KEY=your_api_key_here
FCM_SERVER_KEY=your_firebase_key_here
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
EOF

# Edit mobile/.env
cat << 'EOF' > mobile/.env
# Backend API
API_BASE_URL=http://localhost:8000

# Firebase
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_WEB_API_KEY=your_firebase_web_api_key

# Analytics
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
AMPLITUDE_API_KEY=your_amplitude_key_here

# Environment
ENVIRONMENT=development
EOF
```

### Step 3: Start Docker Infrastructure (5 minutes)

```bash
# Start all services in background
docker-compose up -d

# Verify all containers are running
docker-compose ps
# Expected output:
# NAME                COMMAND             STATUS
# owncircle_postgres  postgres            Up (healthy)
# owncircle_redis     redis-server        Up (healthy)
# owncircle_clickhouse clickhouse         Up (healthy)

# Check logs if any service isn't healthy
docker-compose logs postgres
docker-compose logs redis
docker-compose logs clickhouse
```

### Step 4: Setup Backend (5 minutes)

```bash
cd backend

# Create Python virtual environment
python3.13 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Verify Python version
python --version          # Should show Python 3.13.x

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Seed initial data (optional)
python scripts/seed_data.py

# Start FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Verify backend is running (in new terminal)
curl http://localhost:8000/health
# Expected: {"status": "healthy"}
```

### Step 5: Setup Mobile (5 minutes)

```bash
cd mobile

# Install npm dependencies
npm install

# Install iOS pods (macOS only)
cd ios && pod install && cd ..

# Verify installations
npm list react-native     # Should show 0.81.x
npm list typescript       # Should show 5.7.x
```

### Step 6: Verify Everything Works

```bash
# In terminal 1: Docker services
docker-compose ps        # All should be healthy

# In terminal 2: Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
# Open http://localhost:8000/docs to see API documentation

# In terminal 3: Mobile
cd mobile
npm start                # Start Metro bundler

# In terminal 4: Test mobile on iOS/Android
# iPhone (macOS):
cd mobile && npm run ios

# Android:
cd mobile && npm run android
```

---

## 4. BACKEND SETUP

### Architecture Overview

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── core/
│   │   ├── config.py           # Settings from environment
│   │   ├── security.py         # JWT, encryption
│   │   └── celery.py           # Celery configuration
│   ├── models/                 # SQLAlchemy models
│   ├── schemas/                # Pydantic request/response models
│   ├── api/                    # API route handlers
│   ├── services/               # Business logic
│   ├── crud/                   # Database operations
│   └── utils/                  # Helper functions
├── alembic/                    # Database migrations
├── tests/                      # Unit & integration tests
├── requirements.txt            # Production dependencies
└── Dockerfile                  # Container configuration
```

### Database Models Created

| Entity | Status | Description |
|--------|--------|-------------|
| `User` | ✓ | User accounts with roles (member, business, admin) |
| `Business` | ✓ | Business profiles (restaurants, salons, clinics) |
| `Transaction` | ✓ | Loyalty point transactions |
| `Bonus` | ✓ | Loyalty bonuses and rewards |
| `Event` | ✓ | Events and promotions |
| `EventRegistration` | ✓ | Event attendance tracking |
| `StatusTier` | ✓ | Membership tiers (bronze, silver, gold, platinum) |
| `Coupon` | ✓ | Digital coupons and promotional codes |
| `Notification` | ✓ | Push notifications and messages |
| `CrossPromoChain` | ✓ | Cross-promotion partnerships |
| `CRMIntegration` | ✓ | Third-party CRM connections |

All models are documented in `/home/user/OwnCircule/docs/backend/entities/`

### FastAPI Setup Details

#### 1. Core Dependencies
```bash
# View installed versions
pip list | grep -E "fastapi|sqlalchemy|celery|redis"

# Expected:
# FastAPI               0.121.2
# SQLAlchemy           2.0.44
# Celery               5.4.0
# redis                5.0.x
```

#### 2. Async Database Configuration
```python
# In app/core/config.py
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

# Connection pool settings:
# - Pool size: 20 connections
# - Max overflow: 10 additional connections
# - Pool recycle: 3600 seconds
# - Echo SQL: Disabled in production
```

#### 3. API Structure
```
GET  /health                              # Health check
GET  /docs                               # Swagger UI
GET  /redoc                              # ReDoc documentation

# Authentication
POST /auth/register                      # User registration
POST /auth/login                         # User login
POST /auth/refresh                       # Refresh JWT token
POST /auth/logout                        # User logout

# Users
GET  /users/{user_id}                    # Get user profile
PUT  /users/{user_id}                    # Update profile
GET  /users/{user_id}/transactions       # User transactions

# Businesses
GET  /businesses                         # List businesses
POST /businesses                         # Create business
GET  /businesses/{business_id}           # Get business profile

# More endpoints in /docs when server is running
```

### Alembic Migrations

#### View Current Status
```bash
cd backend

# List all migrations
alembic history

# Current revision
alembic current

# Expected: Head points to latest migration with timestamp
```

#### Create New Migration (After Model Changes)
```bash
# Autogenerate migration from model changes
alembic revision --autogenerate -m "Add new_field to users table"

# Review generated migration in alembic/versions/
# Edit if needed for refinement

# Apply migration
alembic upgrade head

# Rollback if needed
alembic downgrade -1
```

#### Database Schema Verification
```bash
# Connect to PostgreSQL directly
psql postgresql://postgres:postgres_dev_password@localhost:5432/owncircle_dev

# List all tables
\dt

# Describe specific table
\d users

# View foreign key constraints
\d+ transactions

# Exit
\q
```

### Celery Configuration (Async Tasks)

#### Available Task Queues
```python
# High priority (15-30 second timeout)
- auth.tasks.send_sms_code
- notifications.tasks.send_push_notification

# Medium priority (1-5 minute timeout)
- analytics.tasks.update_rfm_scores
- events.tasks.send_event_reminders

# Low priority (1+ hour timeout)
- analytics.tasks.generate_daily_report
- backup.tasks.backup_database
```

#### Monitor Celery Tasks
```bash
# Install Flower (web UI for Celery)
pip install flower

# Start Flower
celery -A app.core.celery flower --port=5555

# Open browser: http://localhost:5555
```

---

## 5. MOBILE SETUP

### Architecture Overview

```
mobile/
├── src/
│   ├── screens/                # Screen components
│   ├── components/             # Reusable components
│   ├── navigation/             # Navigation stacks
│   ├── redux/                  # Redux store & slices
│   ├── services/               # API client & utilities
│   ├── hooks/                  # Custom React hooks
│   ├── theme/                  # Design tokens & theming
│   └── App.tsx                 # Root component
├── ios/                        # iOS native code
├── android/                    # Android native code
├── __tests__/                  # Jest tests
├── package.json                # Dependencies
└── tsconfig.json               # TypeScript config
```

### Install Dependencies

```bash
cd mobile

# Install npm packages (2-3 minutes)
npm install

# Verify React Native version
npm list react-native  # Should show 0.81.x

# Verify TypeScript version
npm list typescript    # Should show 5.7.x
```

### iOS Setup (macOS Only)

#### Prerequisites
```bash
# Install Xcode (from App Store or download)
# ~13GB, takes 30+ minutes

# Install Command Line Tools
xcode-select --install

# Install CocoaPods
sudo gem install cocoapods

# Verify installations
pod repo update  # Update pod repository
```

#### Install iOS Dependencies
```bash
cd mobile/ios

# Install pods
pod install

# Verify pod installation
pod install --repo-update

# Return to mobile directory
cd ..
```

#### Run on iOS Simulator
```bash
# Option 1: npm command
npm run ios

# Option 2: Specific simulator
npx react-native run-ios --simulator="iPhone 15 Pro"

# Option 3: Open in Xcode
open ios/OwnCircule.xcworkspace
# Select iPhone 15 Pro simulator
# Press Cmd + R to run
```

#### Available iOS Simulators
```bash
# List available simulators
xcrun simctl list devices

# Common options:
# iPhone 15 Pro (A17 Pro chip, latest)
# iPhone 15
# iPhone 14 Pro
# iPad Pro 12.9-inch
```

### Android Setup

#### Prerequisites
```bash
# Install Android Studio
# Download: https://developer.android.com/studio

# Set Android SDK path (macOS)
echo 'export ANDROID_HOME=$HOME/Library/Android/sdk' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/emulator' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> ~/.zshrc
source ~/.zshrc

# Or Windows (WSL2/native)
setx ANDROID_HOME "%USERPROFILE%\AppData\Local\Android\sdk"
```

#### Run on Android Emulator
```bash
# Option 1: Start emulator from Android Studio
# Tools > AVD Manager > Select emulator > Play button

# Option 2: Command line
emulator -avd Pixel_6_API_35

# Run React Native on Android
npm run android

# Verify app is running on emulator
```

#### Available Android Emulators
```bash
# List available emulators
emulator -list-avds

# Common options:
# Pixel_6_API_35 (Android 15, ARM64)
# Pixel_5_API_33 (Android 13, ARM64)
# Nexus_5X_API_30 (Android 11, x86)
```

### Metro Bundler

#### Start Metro
```bash
# Terminal 1: Metro bundler
cd mobile
npm start

# Metro will run on http://localhost:8081
# Watch for error messages in console

# Press 'i' to open iOS simulator
# Press 'a' to open Android emulator
```

#### Common Metro Commands
```
Press 'r' - Reload the app
Press 'i' - Open iOS simulator
Press 'a' - Open Android emulator
Press 'd' - Open Debugger
Press 'm' - Show menu
Press 'c' - Clear console
```

### Redux Store Structure

```javascript
// Redux store layout
store
├── auth/          # Authentication state
│   ├── user
│   ├── tokens
│   └── loading
├── loyalty/       # Loyalty program state
│   ├── points
│   ├── tier
│   └── transactions
├── businesses/    # Nearby businesses
├── events/        # Events & promotions
├── notifications/ # Push notifications
└── ui/            # UI state
    ├── theme      # Tiffany blue theme
    └── navigation
```

### Design System & Theming

#### Tiffany Blue Color Theme
```javascript
// Primary colors
const colors = {
  primary: '#0ABAB5',           // Tiffany Blue
  primaryLight: '#4DCCCC',      // Light variant
  primaryDark: '#008B88',       // Dark variant
  secondary: '#FF6B6B',         // Accent red
  background: '#FFFFFF',        // White
  surface: '#F8F9FA',           // Light gray
  error: '#DC3545',             // Bootstrap red
  success: '#28A745',           // Bootstrap green
  warning: '#FFC107',           // Bootstrap yellow
  info: '#17A2B8'               // Bootstrap cyan
};
```

#### Available Design Tokens
View at: `/home/user/OwnCircule/docs/design/resources/design-tokens.json`

Components documented at: `/home/user/OwnCircule/docs/design/components/`

---

## 6. RUNNING THE PROJECT

### Full Stack Startup (All Services)

```bash
# Terminal 1: Start Docker containers
docker-compose up -d

# Verify services are healthy
docker-compose ps

# Terminal 2: Backend FastAPI
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Wait for startup message:
# Uvicorn running on http://0.0.0.0:8000

# Terminal 3: Metro bundler
cd mobile
npm start

# Terminal 4: iOS or Android
# For iOS:
npm run ios

# For Android:
npm run android
```

### Docker Compose Commands

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f                    # All services
docker-compose logs -f postgres           # PostgreSQL only
docker-compose logs -f backend            # Backend API

# Stop all services
docker-compose down

# Stop services and remove volumes (clean slate)
docker-compose down -v

# Restart a service
docker-compose restart postgres

# Scale a service (Celery workers)
docker-compose up -d --scale celery_worker=3

# View resource usage
docker stats owncircle_backend
docker stats owncircle_postgres
```

### Health Checks

#### Backend Health
```bash
# Health check endpoint
curl http://localhost:8000/health
# Expected: {"status": "healthy"}

# API documentation
# Open in browser: http://localhost:8000/docs
# Or: http://localhost:8000/redoc
```

#### PostgreSQL Health
```bash
# Connect and verify
psql postgresql://postgres:postgres_dev_password@localhost:5432/owncircle_dev -c "SELECT version();"

# List tables
psql postgresql://postgres:postgres_dev_password@localhost:5432/owncircle_dev -c "\dt"

# Or via Docker
docker-compose exec postgres psql -U postgres -d owncircle_dev -c "\dt"
```

#### Redis Health
```bash
# Connect and verify
redis-cli ping
# Expected: PONG

# Check keys
redis-cli KEYS "*"

# Or via Docker
docker-compose exec redis redis-cli ping
```

#### ClickHouse Health
```bash
# Via docker
docker-compose exec clickhouse clickhouse-client --query "SELECT 1"

# Via HTTP
curl http://localhost:8123/?query=SELECT+1
```

### Environment Variables Summary

| Variable | Backend | Mobile | Purpose |
|----------|---------|--------|---------|
| `ENVIRONMENT` | ✓ | ✓ | development/staging/production |
| `DATABASE_URL` | ✓ | | PostgreSQL connection |
| `REDIS_URL` | ✓ | | Redis cache & Celery broker |
| `CLICKHOUSE_URL` | ✓ | | Analytics database |
| `JWT_SECRET_KEY` | ✓ | | Sign JWT tokens |
| `API_BASE_URL` | | ✓ | Backend API endpoint |
| `SENTRY_DSN` | ✓ | ✓ | Error tracking |
| `FIREBASE_*` | | ✓ | Firebase services |

---

## 7. TESTING

### Backend Testing

#### Setup & Configuration
```bash
cd backend
source venv/bin/activate

# Install testing dependencies
pip install -r requirements.txt  # pytest included

# Verify pytest is installed
pytest --version
```

#### Run Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_auth.py

# Run specific test function
pytest tests/test_auth.py::test_user_registration

# Run with coverage
pytest --cov=app --cov-report=html

# View coverage in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

#### Test Structure
```
tests/
├── __init__.py
├── conftest.py                 # Fixtures & config
├── test_auth.py                # Authentication tests
├── test_users.py               # User API tests
├── test_businesses.py          # Business API tests
├── test_transactions.py        # Transaction logic
├── test_loyalty.py             # Loyalty system
├── test_notifications.py       # Notification service
└── integration/
    ├── test_e2e_user_flow.py   # End-to-end flows
    └── test_crm_integrations.py # Third-party integrations
```

#### Running Specific Test Suites
```bash
# Unit tests only
pytest tests/ -k "not integration"

# Integration tests only
pytest tests/integration/

# Authentication tests
pytest tests/ -k "auth"

# High-priority tests
pytest tests/ -m "critical"

# With detailed failure info
pytest -v --tb=long
```

### Mobile Testing

#### Setup Jest
```bash
cd mobile

# Jest is configured in package.json
# View test setup:
npm test

# First run may take longer for setup
```

#### Run Tests
```bash
# Run all tests
npm test

# Run tests in watch mode (rerun on file changes)
npm test -- --watch

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test -- TestFile.test.ts

# Run tests matching pattern
npm test -- --testNamePattern="button"
```

#### Test Structure
```
mobile/__tests__/
├── components/
│   ├── Button.test.tsx
│   ├── Card.test.tsx
│   └── Navigation.test.tsx
├── screens/
│   ├── HomeScreen.test.tsx
│   └── LoginScreen.test.tsx
├── redux/
│   ├── authSlice.test.ts
│   └── loyaltySlice.test.ts
└── utils/
    └── apiClient.test.ts
```

#### Coverage Goals for Sprint 1
- **Backend:** ≥ 80% line coverage
- **Mobile:** ≥ 70% line coverage
- **Critical paths:** ≥ 95% coverage

### Integration Testing

#### E2E User Flows (Backend)
```bash
cd backend
source venv/bin/activate

# Run E2E tests
pytest tests/integration/test_e2e_user_flow.py -v

# Expected flow:
# 1. User registration
# 2. Email verification
# 3. Profile update
# 4. Add first business
# 5. Create transaction
# 6. Verify loyalty points
```

#### Manual Mobile Testing
```bash
# Open app on iOS simulator
npm run ios

# Test checklist:
# [ ] Login screen loads
# [ ] Can register new account
# [ ] Can view business list
# [ ] Can scan QR code
# [ ] Can view loyalty points
# [ ] Notifications display
# [ ] Theme colors are Tiffany blue
```

---

## 8. TROUBLESHOOTING

### Backend Issues

#### Python & Virtual Environment

**Issue:** `command not found: python3.13`
```bash
# Solution: Install Python 3.13
# macOS:
brew install python@3.13

# Ubuntu:
sudo apt install python3.13

# Verify:
python3.13 --version
```

**Issue:** `ModuleNotFoundError: No module named 'fastapi'`
```bash
# Solution: Virtual environment not activated
source venv/bin/activate  # macOS/Linux
# Verify venv is active (should show (venv) in prompt)
```

**Issue:** `RuntimeError: Event loop is closed`
```bash
# Solution: Update asyncpg
pip install --upgrade asyncpg

# Or restart development server
# Kill with Ctrl+C and restart uvicorn
```

#### Database Issues

**Issue:** `psycopg2.OperationalError: could not connect to server`
```bash
# Verify PostgreSQL is running:
docker-compose ps postgres

# If not running:
docker-compose up -d postgres

# Verify DATABASE_URL in backend/.env:
# Should be: postgresql+asyncpg://postgres:postgres_dev_password@localhost:5432/owncircle_dev

# Test connection:
psql postgresql://postgres:postgres_dev_password@localhost:5432/owncircle_dev -c "SELECT 1"
```

**Issue:** `alembic.util.exc.CommandError: Can't locate revision`
```bash
# Solution: Database is out of sync with migrations
cd backend

# Option 1: Reset database (development only!)
docker-compose down -v postgres
docker-compose up -d postgres

# Wait for postgres to be healthy
docker-compose logs postgres | grep "ready to accept"

# Rerun migrations
alembic upgrade head

# Option 2: Manual migration reset
alembic downgrade base
alembic upgrade head
```

**Issue:** `PostgreSQL pool exhausted: QueuePool limit exceeded`
```bash
# Solution: Too many database connections
# Restart backend:
docker-compose restart backend

# Or restart Docker:
docker-compose down
docker-compose up -d
```

#### Redis Issues

**Issue:** `ConnectionError: Error 111 connecting to localhost:6379`
```bash
# Verify Redis is running:
docker-compose ps redis

# Start Redis if needed:
docker-compose up -d redis

# Test connection:
redis-cli ping
# Expected: PONG
```

**Issue:** `Redis connection reset by peer`
```bash
# Solution: Restart Redis
docker-compose restart redis

# Clear Redis cache (WARNING: clears all sessions)
redis-cli FLUSHALL

# Via Docker:
docker-compose exec redis redis-cli FLUSHALL
```

#### FastAPI Issues

**Issue:** `Address already in use: ('::', 8000)`
```bash
# Port 8000 is already taken
# Find process using port 8000:
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process:
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# Or use different port:
uvicorn app.main:app --port 8001
```

**Issue:** `Startup failed: [Error] import_module failed`
```bash
# Solution: Import error in app code
# Check error message for file/line number
# Fix syntax error in that file

# Or clear pycache:
find . -type d -name __pycache__ -exec rm -r {} +
python -m py_compile app/main.py  # Test import
```

### Mobile Issues

#### Metro Bundler

**Issue:** `Error: Unable to resolve module react-native`
```bash
# Solution: Clear Metro cache
npm start -- --reset-cache

# Or manually clear:
rm -rf $TMPDIR/metro-bundler-*
npm start
```

**Issue:** `Cannot find module '@react-native-async-storage/async-storage'`
```bash
# Solution: Pod not installed (iOS)
cd ios && pod install && cd ..

# Or Android gradle not synced
# In Android Studio: File > Sync Now
```

**Issue:** `Too many open files`
```bash
# Solution: Increase file descriptor limit (macOS)
ulimit -n 2048

# Permanent fix in ~/.zshrc:
echo "ulimit -n 2048" >> ~/.zshrc
source ~/.zshrc
```

#### iOS Specific

**Issue:** `CocoaPods could not find compatible versions for pod`
```bash
# Solution: Update CocoaPods
cd mobile/ios
pod repo update
pod deintegrate
pod install
cd ../..
```

**Issue:** `Xcode build failed: Unable to find any ios simulators`
```bash
# Solution: Create iOS simulator
xcrun simctl create "iPhone 15 Pro" "iPhone 15 Pro" iOS17.0

# Or via Xcode:
# Xcode > Window > Devices and Simulators > Simulators > +
```

**Issue:** `error: sdk "iphoneos" cannot be located`
```bash
# Solution: Update Xcode
xcode-select --install

# Or select different Xcode path:
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

#### Android Specific

**Issue:** `error: SDK location not found`
```bash
# Solution: Create local.properties
echo "sdk.dir=$ANDROID_HOME" > android/local.properties

# Verify ANDROID_HOME is set:
echo $ANDROID_HOME  # Should show SDK path
```

**Issue:** `Gradle build failed: Unable to find Android SDK`
```bash
# Install Android SDK tools:
# Download Android Studio
# Tools > SDK Manager > Install SDK 35

# Or command line:
sdkmanager "platforms;android-35"
sdkmanager "build-tools;35.0.0"
```

**Issue:** `Android emulator won't start`
```bash
# Solution: Create emulator
emulator -list-avds  # List available

# Create new one:
avdmanager create avd -n Pixel_6 -k "system-images;android-35;google_apis;arm64-v8a"

# Start:
emulator -avd Pixel_6
```

### Docker Issues

**Issue:** `Cannot connect to the Docker daemon`
```bash
# Solution: Docker Desktop not running
# macOS: Open Applications > Docker
# Linux: Start Docker service
sudo systemctl start docker

# Verify:
docker --version
docker ps
```

**Issue:** `docker: image not found`
```bash
# Solution: Build Docker image
docker-compose build

# Or pull latest images:
docker-compose pull
docker-compose up -d
```

**Issue:** `Port 5432 already in use`
```bash
# PostgreSQL already running locally
# Stop local PostgreSQL:
sudo systemctl stop postgresql  # Linux
brew services stop postgresql  # macOS

# Or use different port in docker-compose.yml:
# Change "5432:5432" to "5433:5432"
```

**Issue:** `Disk space full in Docker`
```bash
# Clean up unused containers/images:
docker system prune -a

# Clean volumes (careful - deletes data):
docker volume prune

# Check disk usage:
docker system df
```

### General Troubleshooting Steps

1. **Check Error Messages**
   - Read full error message (not just first line)
   - Search error in project docs or Google
   - Check relevant log files

2. **Restart Services**
   ```bash
   # Backend
   docker-compose restart backend

   # All services
   docker-compose restart
   ```

3. **Clean & Reset**
   ```bash
   # Backend cache
   rm -rf backend/.cache
   find backend -type d -name __pycache__ -exec rm -r {} +

   # Mobile cache
   rm -rf mobile/node_modules
   npm install

   # Docker (careful!)
   docker-compose down -v
   docker-compose up -d
   ```

4. **Check Logs**
   ```bash
   docker-compose logs backend
   docker-compose logs postgres
   docker-compose logs redis
   ```

5. **Ask for Help**
   - Check closed GitHub issues
   - Ask in team Slack/Telegram
   - Share full error message and steps to reproduce

---

## 9. NEXT STEPS (SPRINT 2 PREVIEW)

### Sprint 2 Goals
- Implement core authentication module
- Build user registration & profile screens
- Create loyalty point system MVP
- Integrate first CRM (YCLIENTS)
- Deploy to staging environment

### Features to Build

#### Module 1: User Authentication (Week 3-4)
- [x] Database models created
- [ ] SMS-based registration flow
- [ ] JWT authentication with refresh tokens
- [ ] Two-factor authentication
- [ ] Session management
- [ ] Password reset workflow

#### Module 2: Loyalty System (Week 5-6)
- [x] Database models created
- [ ] Point calculation logic
- [ ] Tier membership system
- [ ] Bonus & reward allocation
- [ ] Transaction history
- [ ] Point redemption

#### Module 3: Business Integration (Week 7-8)
- [x] Database models created
- [ ] YCLIENTS API integration
- [ ] Business onboarding workflow
- [ ] Menu/services sync
- [ ] Staff management
- [ ] Transaction import

### Code Examples for Sprint 2

#### Example: Add New API Endpoint
```python
# In app/api/users.py
from fastapi import APIRouter, Depends
from app.schemas import UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    current_user = Depends(get_current_user),
    service: UserService = Depends()
):
    """Get user by ID"""
    user = await service.get_user(user_id)
    return user
```

#### Example: Add Redux Slice (Mobile)
```typescript
// In mobile/src/redux/authSlice.ts
import { createSlice } from '@reduxjs/toolkit';

interface AuthState {
  user: User | null;
  accessToken: string | null;
  refreshToken: string | null;
  loading: boolean;
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setUser(state, action) {
      state.user = action.payload;
    },
    // More reducers...
  }
});
```

### Documentation to Update
- [ ] API endpoints as they're implemented
- [ ] Database schema changes in Alembic migrations
- [ ] Mobile navigation structure
- [ ] Design system additions
- [ ] Troubleshooting guide with new issues

### Team Responsibilities

| Role | Sprint 1 | Sprint 2 |
|------|----------|----------|
| Backend | Infrastructure ✓ | Auth + Loyalty |
| Mobile | Setup ✓ | Auth UI + Redux |
| DevOps | Docker setup ✓ | CI/CD + Staging |
| QA | Test setup ✓ | Integration testing |
| Design | Design system ✓ | Screen designs |

### Sprint 1 Completion Checklist

- [ ] All team members have working environments
- [ ] Docker infrastructure running without issues
- [ ] Backend API responds to health check
- [ ] Database migrations applied successfully
- [ ] Mobile app builds for iOS and Android
- [ ] All tests passing (80%+ backend, 70%+ mobile)
- [ ] Documentation complete and reviewed
- [ ] No critical Sentry errors in logs
- [ ] CI/CD pipelines passing
- [ ] Sprint retrospective completed

---

## Additional Resources

### Documentation
- **Project Essence:** `/home/user/OwnCircule/docs/core/00_PROJECT_ESSENCE.md`
- **Architecture:** `/home/user/OwnCircule/docs/core/04_ARCHITECTURE.md`
- **Tech Stack:** `/home/user/OwnCircule/docs/core/03_TECH_STACK.md`
- **API Overview:** `/home/user/OwnCircule/docs/backend/api/00_API_OVERVIEW.md`
- **Design System:** `/home/user/OwnCircule/docs/design/00_DESIGN_SYSTEM.md`

### External Links
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **React Native Docs:** https://reactnative.dev/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **Docker Documentation:** https://docs.docker.com/
- **Celery Documentation:** https://docs.celeryproject.io/

### Tools & Services
- **API Testing:** http://localhost:8000/docs (Swagger UI)
- **Database Admin:** `psql` command line tool
- **Celery Monitoring:** http://localhost:5555 (Flower)
- **Redux Devtools:** Browser extension for Redux debugging
- **Sentry Dashboard:** https://sentry.io (error tracking)

---

## Support & Communication

### Getting Help
1. **Check this guide** - Many common issues are documented in Troubleshooting
2. **Search GitHub issues** - Other developers may have faced your issue
3. **Ask in team channel** - Slack or Telegram for quick responses
4. **Create GitHub issue** - If you find a bug or missing documentation

### Reporting Issues
When reporting an issue, include:
- Error message (full, not just first line)
- Steps to reproduce
- Your environment (OS, Python version, Node version)
- Relevant log files
- Screenshot if applicable

### Updating This Guide
Found an error or want to improve this guide?
1. Clone the repository
2. Edit this file
3. Submit a pull request with improvements

---

**Status:** Ready for Development
**Last Updated:** 2025-11-17
**Maintained By:** Engineering Team
**Questions?** Contact: [Team Lead Name]

---

> Remember: This is a living document. Update it as you discover new issues, solutions, or improvements!
