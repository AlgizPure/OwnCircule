# Development Setup Guide - Свой Круг

**Last Updated:** 2025-11-17
**Target Audience:** Backend, Mobile, DevOps engineers joining the project
**Estimated Setup Time:** 2-4 hours (first time)

---

## 📋 Prerequisites

### Required Software
- **OS:** macOS 14+, Ubuntu 22.04+, or Windows 11 with WSL2
- **Python:** 3.13+ ([Download](https://www.python.org/downloads/))
- **Node.js:** 20+ LTS ([Download](https://nodejs.org/))
- **Docker Desktop:** Latest ([Download](https://www.docker.com/products/docker-desktop))
- **Git:** 2.40+ ([Download](https://git-scm.com/downloads))

### Mobile Development (Mobile Team Only)
- **Xcode:** 15+ (macOS only, for iOS development)
- **Android Studio:** Latest ([Download](https://developer.android.com/studio))
- **CocoaPods:** 1.12+ (macOS: `sudo gem install cocoapods`)
- **Watchman:** Latest (macOS: `brew install watchman`)

### IDE Recommendations
- **Backend:** PyCharm Professional, VSCode with Python extension
- **Mobile:** VSCode with React Native Tools, Android Studio (Android), Xcode (iOS)
- **AI Assistance:** Cursor IDE (`.cursorrules` already configured)

---

## 🚀 Initial Setup

### Step 1: Clone Repository

```bash
# Clone the project
git clone https://github.com/AlgizPure/OwnCircule.git
cd OwnCircule

# Checkout development branch (or your assigned feature branch)
git checkout claude/upmt-start-1-3-01NzbZsT7jYrAdgQsXszWpS4

# Verify you're on the correct branch
git branch --show-current
```

### Step 2: Environment Variables

```bash
# Copy example .env files
cp backend/.env.example backend/.env
cp mobile/.env.example mobile/.env

# Edit backend/.env with your local settings
# Required variables:
# - DATABASE_URL=postgresql://postgres:password@localhost:5432/svoy_krug
# - REDIS_URL=redis://localhost:6379/0
# - JWT_SECRET_KEY=<generate with: openssl rand -hex 32>
# - SMS_RU_API_KEY=<get from https://sms.ru/>
# - FCM_SERVER_KEY=<Firebase Cloud Messaging key>

# Edit mobile/.env with your local settings
# - API_BASE_URL=http://localhost:8000
# - SENTRY_DSN=<optional, for error tracking>
```

---

## 🐍 Backend Setup (FastAPI + Python 3.13)

### Step 1: Create Virtual Environment

```bash
cd backend

# Create virtual environment
python3.13 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Verify Python version
python --version  # Should show Python 3.13.x
```

### Step 2: Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (testing, linting)
pip install -r requirements-dev.txt

# Verify installation
pip list | grep fastapi  # Should show FastAPI 0.121.2
```

### Step 3: Start Infrastructure (Docker)

```bash
# From project root
cd ..

# Start PostgreSQL, Redis, ClickHouse
docker-compose up -d

# Verify containers are running
docker ps
# Should show: postgres, redis, clickhouse

# Check logs (if issues)
docker-compose logs -f postgres
```

### Step 4: Database Migrations

```bash
cd backend

# Run migrations
alembic upgrade head

# Verify tables created
psql postgresql://postgres:password@localhost:5432/svoy_krug -c "\dt"
# Should show: users, businesses, bonuses, transactions, etc.

# Seed initial data (optional)
python scripts/seed_data.py
```

### Step 5: Run Backend Server

```bash
# Start FastAPI development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Verify server is running
curl http://localhost:8000/health
# Should return: {"status": "healthy"}

# View auto-generated API docs
# Open browser: http://localhost:8000/docs
```

### Step 6: Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html  # macOS
# OR
xdg-open htmlcov/index.html  # Linux
```

---

## 📱 Mobile Setup (React Native 0.81)

### Step 1: Install Dependencies

```bash
cd mobile

# Install npm packages
npm install

# Install iOS pods (macOS only)
cd ios
pod install
cd ..

# Verify installation
npm list react-native  # Should show 0.81.x
```

### Step 2: Start Metro Bundler

```bash
# Start Metro (JavaScript bundler)
npm start

# Metro will run on http://localhost:8081
```

### Step 3: Run on iOS (macOS only)

```bash
# In a new terminal (keep Metro running)
cd mobile

# Run on iOS simulator
npm run ios

# Or run on specific simulator
npx react-native run-ios --simulator="iPhone 15 Pro"

# Or open in Xcode
open ios/SvoyKrug.xcworkspace
# Then press "Run" in Xcode
```

### Step 4: Run on Android

```bash
# Start Android emulator (via Android Studio)
# OR connect physical device with USB debugging enabled

# Run on Android
npm run android

# Verify app is running
# App should open on emulator/device
```

### Step 5: Run Tests

```bash
# Run Jest tests
npm test

# Run with coverage
npm test -- --coverage

# View coverage
open coverage/lcov-report/index.html
```

---

## 🛠️ Development Tools Setup

### 1. VSCode Extensions (Recommended)

**Backend:**
- Python (Microsoft)
- Pylance
- Python Docstring Generator
- Docker
- GitLens

**Mobile:**
- React Native Tools
- ESLint
- Prettier
- React Snippets
- Auto Import

**General:**
- GitHub Copilot / Cursor AI
- Git Graph
- Thunder Client (API testing)

### 2. Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually (first time)
pre-commit run --all-files
```

### 3. Code Formatting

**Backend:**
```bash
# Format with Black
black app/

# Lint with Flake8
flake8 app/

# Type check with mypy
mypy app/
```

**Mobile:**
```bash
# Format with Prettier
npm run format

# Lint with ESLint
npm run lint

# Type check with TypeScript
npm run type-check
```

---

## ☁️ Cloud Infrastructure Setup (DevOps Only)

### 1. Yandex Cloud Account

```bash
# Install Yandex Cloud CLI
curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash

# Initialize CLI
yc init

# Create service account
yc iam service-account create --name svoy-krug-sa

# Assign roles
yc resource-manager folder add-access-binding <folder-id> \
  --role editor \
  --subject serviceAccount:<service-account-id>
```

### 2. PostgreSQL (Managed)

```bash
# Create PostgreSQL cluster
yc managed-postgresql cluster create \
  --name svoy-krug-db \
  --environment production \
  --network-name default \
  --postgresql-version 16 \
  --resource-preset s2.micro \
  --disk-type network-ssd \
  --disk-size 10
```

### 3. Redis (Managed)

```bash
# Create Redis cluster
yc managed-redis cluster create \
  --name svoy-krug-cache \
  --environment production \
  --redis-version 8.2 \
  --resource-preset hm2.nano \
  --disk-size 8
```

### 4. ClickHouse (Managed)

```bash
# Create ClickHouse cluster
yc managed-clickhouse cluster create \
  --name svoy-krug-analytics \
  --environment production \
  --clickhouse-version 25.8 \
  --resource-preset s2.micro \
  --disk-type network-ssd \
  --disk-size 10
```

### 5. CI/CD (GitHub Actions)

GitHub Actions workflows are already configured in `.github/workflows/`:

- `backend-ci.yml` - Backend tests, linting, type checking
- `mobile-ci.yml` - Mobile tests, linting, build verification
- `deploy.yml` - Production deployment (manual trigger)

**Required GitHub Secrets:**
```
YANDEX_CLOUD_SA_KEY
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
SENTRY_DSN
TELEGRAM_BOT_TOKEN (for deployment notifications)
```

---

## 🔐 Security Setup

### 1. Generate Encryption Keys

```bash
# Generate AES-256 key for data encryption
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Add to backend/.env as ENCRYPTION_KEY=<generated-key>

# Generate RS256 key pair for JWT
openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -pubout -out public_key.pem
# Add paths to backend/.env
```

### 2. Configure HTTPS (Production)

```bash
# Install certbot
sudo apt install certbot

# Generate SSL certificate
sudo certbot certonly --standalone -d api.svoykrug.ru
```

---

## 👥 Team Onboarding

### New Developer Checklist

- [ ] Access granted to GitHub repository
- [ ] Yandex Cloud account created (DevOps only)
- [ ] Added to Slack/Telegram team channel
- [ ] Sentry access granted
- [ ] Added to Notion workspace (documentation)
- [ ] Environment variables shared securely (1Password)
- [ ] Read all core documentation (`docs/core/`)
- [ ] Completed this setup guide
- [ ] Ran backend + mobile successfully
- [ ] Reviewed `.cursorrules` file
- [ ] Attended sprint planning/standup

### Useful Resources

- **Project Essence:** [`docs/core/00_PROJECT_ESSENCE.md`](core/00_PROJECT_ESSENCE.md)
- **Architecture:** [`docs/core/04_ARCHITECTURE.md`](core/04_ARCHITECTURE.md)
- **Module Requirements:** [`docs/requirements/`](requirements/)
- **Current Sprint:** [`docs/progress/sprint_current.md`](progress/sprint_current.md)
- **API Documentation:** http://localhost:8000/docs (when backend running)

---

## 🐛 Troubleshooting

### Backend Issues

**Issue:** `ModuleNotFoundError: No module named 'fastapi'`
- **Fix:** Ensure virtual environment is activated: `source venv/bin/activate`

**Issue:** `psycopg2.OperationalError: could not connect to server`
- **Fix:** Verify PostgreSQL is running: `docker ps`, check DATABASE_URL in `.env`

**Issue:** `alembic.util.exc.CommandError: Can't locate revision identified by 'xxxxx'`
- **Fix:** Drop database, recreate, run migrations: `alembic upgrade head`

### Mobile Issues

**Issue:** `error: bundling failed: Error: Unable to resolve module react-native`
- **Fix:** Clear Metro cache: `npm start -- --reset-cache`

**Issue:** iOS build fails with pod errors
- **Fix:** Update pods: `cd ios && pod deintegrate && pod install`

**Issue:** Android build fails with Gradle errors
- **Fix:** Clean build: `cd android && ./gradlew clean && cd ..`

### Docker Issues

**Issue:** `Cannot connect to the Docker daemon`
- **Fix:** Start Docker Desktop, verify it's running

**Issue:** Port 5432 already in use
- **Fix:** Stop local PostgreSQL: `sudo systemctl stop postgresql` (Linux)

---

## 📞 Support

If you encounter issues not covered in this guide:

1. Check [`docs/progress/sprint_current.md`](progress/sprint_current.md) for known blockers
2. Search closed GitHub issues
3. Ask in team Slack/Telegram channel
4. Contact technical lead: [To be added]

---

**Last Updated:** 2025-11-17
**Maintained By:** DevOps Team
**Status:** Ready for Development
