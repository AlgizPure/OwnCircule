# Module 8: CRM Integrations - Requirements

**Module ID:** MOD-08
**Total Functions:** 20
**Priority:** P0 (Critical - MVP)
**Dependencies:** Module 3 (Transactions), Module 2 (Loyalty System)
**Tech Stack:** Python 3.13, Celery 5.4.x, Redis 8.2, httpx 0.28.x

---

## 📋 Module Overview

CRM Integration module synchronizes transaction data from partner business CRM systems (YCLIENTS, Iiko, 1С, AMO CRM, МИС Renovatio) into platform database. Supports bidirectional sync for bonus accrual/redemption, webhook processing, error handling with retry logic, and CSV fallback for businesses without APIs.

**Key Subsystems:**
- 8.1 CRM Connectors (7 functions): Adapters for 6 CRM systems + CSV upload
- 8.2 Data Synchronization (8 functions): Scheduled sync, webhook processing, duplicate detection, error handling
- 8.3 Integration Management (5 functions): Configuration, health checks, logs, statistics

---

## 8.1 CRM Connectors (7 functions)

### User Story 8.1.1: 1С Integration (Skinerica, Лисичкино)
**As a** platform administrator
**I want to** integrate with 1С accounting system
**So that** transactions are synced automatically from Skinerica and Лисичкино

**Acceptance Criteria:**
```gherkin
Scenario: Configure 1С integration
  Given Skinerica uses 1С for accounting
  When I configure integration in admin panel
  Then I enter 1С REST API credentials:
    - API URL: https://api.1c.ru/skinerica
    - Username: admin
    - Password: ******
    - Database ID: skinerica_db
  And I test connection with "Test Connection" button
  And connection succeeds: "✅ Connected to 1С"

Scenario: Sync transactions from 1С
  Given 1С integration is active
  When sync task runs (every 5 minutes)
  Then I fetch new transactions via GET /api/transactions?since=:last_sync
  And I parse 1С transaction format:
    {
      "id": "1C-12345",
      "date": "2025-11-17T14:30:00",
      "customer_phone": "+79991234567",
      "amount": 10000,
      "items": [{"name": "Процедура", "price": 10000}]
    }
  And I create platform transaction with external_id="1C-12345"
  And I match customer by phone to platform user
```

**Technical Requirements:**
- Use `OneCAdapter` class implementing `BaseCRMAdapter` interface
- API authentication: HTTP Basic Auth or OAuth2 (depends on 1С version)
- Transaction mapping:
  ```python
  def map_transaction(self, onec_tx):
      return Transaction(
          external_id=f"1C-{onec_tx['id']}",
          amount=onec_tx['amount'],
          user_id=self.find_user_by_phone(onec_tx['customer_phone']),
          business_id=self.business_id,
          created_at=onec_tx['date']
      )
  ```

---

### User Story 8.1.2: YCLIENTS Integration (Миндаль salon)
**As a** platform administrator
**I want to** integrate with YCLIENTS CRM
**So that** Миндаль salon transactions sync automatically

**Acceptance Criteria:**
```gherkin
Scenario: Configure YCLIENTS integration
  Given Миндаль uses YCLIENTS for booking and payments
  When I configure integration
  Then I enter YCLIENTS API credentials:
    - API Token: yclients_token_here
    - Company ID: 12345
  And I test connection: GET https://api.yclients.com/api/v1/company/12345
  And response: "✅ Connected to YCLIENTS - Миндаль"

Scenario: Sync transactions from YCLIENTS
  Given YCLIENTS integration is active
  When sync task runs
  Then I fetch records via GET /api/v1/records?company_id=12345&start_date=:last_sync
  And I parse YCLIENTS record format:
    {
      "id": 67890,
      "client": {"phone": "79991234567"},
      "date": "2025-11-17 14:30",
      "cost": 5000,
      "paid": 5000,
      "services": [{"title": "Стрижка", "cost": 5000}]
    }
  And I create transaction with external_id="YCLIENTS-67890"
```

**Technical Requirements:**
- Use `YCLIENTSAdapter` class
- API docs: https://yclients.docs.apiary.io
- Authentication: Bearer token in `Authorization` header
- Rate limiting: 120 requests/minute (YCLIENTS API limit)

---

### User Story 8.1.3: AMO CRM Integration (Стим Центр dentistry)
**As a** platform administrator
**I want to** integrate with AMO CRM
**So that** Стим Центр transactions sync automatically

**Acceptance Criteria:**
```gherkin
Scenario: Configure AMO CRM integration
  Given Стим Центр uses AMO CRM for lead management
  When I configure integration
  Then I enter AMO CRM OAuth2 credentials:
    - Subdomain: stimcentr.amocrm.ru
    - Client ID: ...
    - Client Secret: ...
  And I complete OAuth2 flow to get access token
  And I test connection: GET https://stimcentr.amocrm.ru/api/v4/account
  And response: "✅ Connected to AMO CRM - Стим Центр"

Scenario: Sync leads as transactions
  Given AMO CRM integration is active
  When sync task runs
  Then I fetch leads via GET /api/v4/leads?filter[updated_at][from]=:last_sync
  And I filter leads with status="paid"
  And I create transactions from paid leads
```

**Technical Requirements:**
- Use `AMOCRMAdapter` class
- OAuth2 flow with refresh tokens (30-day expiry)
- Custom field mapping (AMO CRM allows custom fields per account)
- Lead status mapping: only "Успешно реализовано" leads → transactions

---

### User Story 8.1.4: МИС Renovatio Integration (Миллениум medical center)
**As a** platform administrator
**I want to** integrate with МИС Renovatio medical information system
**So that** Миллениум transactions sync with врачебная тайна compliance

**Acceptance Criteria:**
```gherkin
Scenario: Configure МИС Renovatio integration
  Given Миллениум uses МИС Renovatio
  When I configure integration
  Then I enter МИС API credentials (provided by Renovatio vendor)
  And I enable врачебная тайна flag: `is_medical=TRUE`
  And transactions are flagged as medical (excluded from cross-promo)

Scenario: Sync medical transactions with anonymization
  Given МИС Renovatio integration is active
  When sync task runs
  Then I fetch anonymized transactions (patient ID hashed)
  And I create transactions with is_medical=TRUE
  And medical transactions are excluded from Win-Win analytics
```

**Technical Requirements:**
- Use `RenovatioAdapter` class
- Medical data compliance: transactions flagged `is_medical=TRUE`
- Patient ID hashing: `SHA256(patient_id + salt)` to prevent re-identification
- Exclude medical transactions from Module 5 (Cross-Promo) and Module 7 (Analytics)

---

### User Story 8.1.5: Iiko Integration (Лисичкино gastromarket)
**As a** platform administrator
**I want to** integrate with Iiko restaurant management system
**So that** Лисичкино purchases sync automatically

**Acceptance Criteria:**
```gherkin
Scenario: Configure Iiko integration
  Given Лисичкино uses Iiko for POS and inventory
  When I configure integration
  Then I enter Iiko API credentials:
    - API Login: iiko_login
    - API Password: ******
  And I call POST /api/auth to get session token
  And I test connection: GET /api/organization/list
  And response: "✅ Connected to Iiko - Лисичкино"

Scenario: Sync orders from Iiko
  Given Iiko integration is active
  When sync task runs
  Then I fetch orders via POST /api/orders/list {dateFrom: :last_sync}
  And I parse Iiko order format (complex nested JSON)
  And I create transactions from closed orders (status="Закрыт")
```

**Technical Requirements:**
- Use `IikoAdapter` class
- API authentication: Session-based (POST /api/auth returns token valid for 1 hour)
- Complex order structure: nested items, modifiers, discounts
- Map Iiko customer loyalty card to platform phone number

---

### User Story 8.1.6: CSV Upload Fallback
**As a** business owner
**I want to** upload transactions via CSV file
**So that** I can integrate even without API access

**Acceptance Criteria:**
```gherkin
Scenario: Upload CSV file
  Given my business doesn't have API integration
  When I go to Business Admin Panel → "Загрузить транзакции"
  And I upload CSV file with columns:
    - date (YYYY-MM-DD HH:MM:SS)
    - customer_phone (+7XXXXXXXXXX)
    - amount (decimal)
    - description (optional)
  Then CSV is validated (required columns present, valid formats)
  And transactions are imported into database
  And I see summary: "Imported 25 transactions, 2 errors"

Scenario: CSV validation errors
  Given I upload CSV with invalid phone format
  When validation runs
  Then I see error report:
    - Row 3: Invalid phone format (expected +7XXXXXXXXXX)
    - Row 7: Amount is not a number
  And valid rows are imported, invalid rows are skipped
```

**Technical Requirements:**
- Use Python `pandas` library for CSV parsing
- CSV validation rules:
  - date: ISO 8601 format
  - customer_phone: E.164 format (+7XXXXXXXXXX)
  - amount: positive decimal
- Max file size: 10MB (~50,000 transactions)
- Celery task for async processing of large files

---

### User Story 8.1.7: Custom Connector Configuration
**As a** platform administrator
**I want to** configure custom connectors for non-standard CRM systems
**So that** any business can integrate

**Acceptance Criteria:**
```gherkin
Scenario: Define custom API connector
  Given a business uses custom in-house CRM
  When I create custom connector
  Then I define:
    - API endpoint URL
    - Authentication type (Basic/Bearer/OAuth2)
    - Request format (JSON/XML)
    - Response field mappings:
      * transaction_id → :response.data.id
      * amount → :response.data.total
      * customer_phone → :response.data.client.phone
  And I test mapping with sample response
  And connector is saved for this business
```

**Technical Requirements:**
- Store connector config as JSON in `crm_integrations` table
- Use Jinja2 templating for field extraction: `{{ response.data.id }}`
- Support JSONPath and XPath for complex structures
- Sandbox mode: test connector with sample data before activating

---

## 8.2 Data Synchronization (8 functions)

### User Story 8.2.1: Scheduled Sync (Every 5 Minutes)
**As a** platform
**I want to** sync transactions automatically every 5 minutes
**So that** bonuses are accrued quickly

**Acceptance Criteria:**
```gherkin
Scenario: Celery Beat scheduled sync
  Given 5 minutes have passed since last sync
  When Celery Beat triggers sync task
  Then sync runs for all active CRM integrations
  And last_sync_at timestamp is updated for each business

Scenario: Sync only new transactions
  Given last_sync_at is 2025-11-17 14:00
  When sync runs at 14:05
  Then I fetch transactions with created_at > 2025-11-17 14:00
  And I don't re-process old transactions
```

**Technical Requirements:**
- Celery Beat task: `@app.task def sync_all_crm_transactions()`
- Runs every 5 minutes: `CELERYBEAT_SCHEDULE = {'sync-crm': {'task': 'sync_all_crm_transactions', 'schedule': 300}}`
- Track last sync: `businesses.last_sync_at TIMESTAMP`

---

### User Story 8.2.2: Manual Sync Trigger
**As a** business owner
**I want to** manually trigger sync from admin panel
**So that** I can force update immediately

**Acceptance Criteria:**
```gherkin
Scenario: Manual sync button
  Given I am on Business Admin Panel
  When I tap "Синхронизировать сейчас"
  Then sync task is triggered immediately (bypasses 5-min schedule)
  And I see loading spinner: "Синхронизация..."
  And after completion: "✅ Синхронизировано 12 транзакций"
```

---

### User Story 8.2.3: Transaction Parsing & Normalization
**As a** platform
**I want to** parse different CRM formats into unified structure
**So that** downstream modules work with consistent data

**Acceptance Criteria:**
```gherkin
Scenario: Parse transaction from YCLIENTS
  Given YCLIENTS returns complex nested JSON
  When I parse transaction
  Then I extract:
    - external_id: "YCLIENTS-{record.id}"
    - amount: record.cost
    - customer_phone: record.client.phone (normalize to E.164)
    - created_at: record.date (convert to UTC)
    - description: record.services[0].title

Scenario: Phone number normalization
  Given CRM returns phone "8 999 123-45-67"
  When I normalize phone
  Then result is "+79991234567" (E.164 format)
  And I can match user by this phone
```

**Technical Requirements:**
- Phone normalization library: `phonenumbers` (Google libphonenumbers)
- Timezone handling: convert all timestamps to UTC
- Amount parsing: handle different decimal separators (1,000.50 vs 1.000,50)

---

### User Story 8.2.4: Duplicate Detection
**As a** platform
**I want to** prevent duplicate transactions
**So that** bonuses aren't accrued twice

**Acceptance Criteria:**
```gherkin
Scenario: Detect duplicate by external_id
  Given transaction with external_id="YCLIENTS-123" already exists
  When sync task processes same transaction again
  Then I check: SELECT COUNT(*) FROM transactions WHERE external_id='YCLIENTS-123'
  And if count > 0, skip transaction
  And log: "Duplicate skipped: YCLIENTS-123"

Scenario: Handle missing external_id
  Given CSV upload doesn't have unique ID
  When I import transaction
  Then I generate hash: SHA256(date + phone + amount + business_id)
  And use hash as external_id for duplicate detection
```

---

### User Story 8.2.5: Webhook Processing (Real-Time Sync)
**As a** platform
**I want to** receive webhooks from CRM systems
**So that** transactions sync in real-time (not every 5 minutes)

**Acceptance Criteria:**
```gherkin
Scenario: Register webhook with YCLIENTS
  Given YCLIENTS supports webhooks
  When I configure integration
  Then I register webhook URL: https://api.svoykrug.ru/webhooks/yclients
  And YCLIENTS calls webhook when new record is created

Scenario: Process webhook payload
  Given YCLIENTS webhook is triggered
  When POST /webhooks/yclients is called with payload
  Then I validate webhook signature (HMAC-SHA256)
  And I extract transaction data from payload
  And I create transaction immediately (no 5-min delay)
  And I return HTTP 200 OK to acknowledge
```

**Technical Requirements:**
- Webhook endpoints: `/webhooks/{crm_type}` (yclients, iiko, amocrm, etc.)
- Signature validation: verify HMAC-SHA256 using shared secret
- Async processing: queue webhook payload to Celery task (don't block webhook response)
- Retry mechanism: if processing fails, webhook provider retries (exponential backoff)

---

### User Story 8.2.6: Sync Error Logging
**As a** platform administrator
**I want to** see detailed error logs when sync fails
**So that** I can debug integration issues

**Acceptance Criteria:**
```gherkin
Scenario: API connection error
  Given YCLIENTS API is down
  When sync task tries to connect
  Then error is logged to `integration_logs` table:
    - timestamp: 2025-11-17 14:05
    - business_id: миндаль_id
    - error_type: "ConnectionError"
    - error_message: "Failed to connect to api.yclients.com"
    - stack_trace: full traceback
  And I receive alert email (if 3+ consecutive failures)

Scenario: Data parsing error
  Given YCLIENTS returns unexpected JSON structure
  When I try to parse transaction
  Then error is logged:
    - error_type: "ParseError"
    - error_message: "Missing field 'client.phone' in response"
    - raw_data: (store problematic JSON for debugging)
```

**Technical Requirements:**
- Log table:
  ```sql
  integration_logs (
    id UUID PRIMARY KEY,
    business_id UUID REFERENCES businesses(id),
    log_type VARCHAR(20),  -- 'success' | 'error' | 'warning'
    error_type VARCHAR(50),
    message TEXT,
    raw_data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
  )
  ```

---

### User Story 8.2.7: Alert on Sync Failure
**As a** business owner
**I want to** receive alerts when sync fails repeatedly
**So that** I can fix the issue quickly

**Acceptance Criteria:**
```gherkin
Scenario: 3 consecutive sync failures trigger alert
  Given sync failed at 14:00, 14:05, 14:10 (3 times)
  When 3rd failure occurs
  Then I receive email alert:
    Subject: "Ошибка синхронизации с YCLIENTS - Миндаль"
    Body:
      - Error description
      - Last successful sync: 2025-11-16 18:00
      - Link to integration logs in admin panel
      - CTA: "Check Integration Settings"
```

---

### User Story 8.2.8: Retry Logic for Failed Transactions
**As a** platform
**I want to** retry failed transactions automatically
**So that** temporary issues don't cause data loss

**Acceptance Criteria:**
```gherkin
Scenario: Retry failed transaction
  Given transaction sync failed due to timeout
  When retry task runs (after 2 minutes)
  Then I attempt to sync the transaction again
  And retry up to 3 times with exponential backoff (2min, 4min, 8min)
  And if all retries fail, mark as "permanently_failed"

Scenario: Permanent failure notification
  Given transaction failed 3 times
  When max retries reached
  Then I log to integration_logs with status="permanently_failed"
  And I send alert to business owner
```

**Technical Requirements:**
- Celery retry: `@app.task(bind=True, max_retries=3, default_retry_delay=120)`
- Exponential backoff: `self.retry(countdown=2 ** self.request.retries * 60)`

---

## 8.3 Integration Management (5 functions)

### User Story 8.3.1: Configure Integration Settings
**As a** business owner
**I want to** configure CRM integration from admin panel
**So that** sync works with my CRM system

**Acceptance Criteria:**
```gherkin
Scenario: Configure YCLIENTS integration
  Given I am on Business Admin Panel → "Интеграции"
  When I select "YCLIENTS"
  And I enter API token, Company ID
  And I click "Save Settings"
  Then settings are saved to `crm_integrations` table
  And integration is marked as `active=TRUE`
```

**Technical Requirements:**
- CRM integrations table:
  ```sql
  crm_integrations (
    business_id UUID PRIMARY KEY REFERENCES businesses(id),
    crm_type VARCHAR(50),  -- 'yclients' | '1c' | 'iiko' | 'amocrm' | 'renovatio' | 'custom'
    credentials JSONB,  -- encrypted
    active BOOLEAN DEFAULT TRUE,
    last_sync_at TIMESTAMP,
    created_at TIMESTAMP
  )
  ```

---

### User Story 8.3.2: Test Connection (Health Check)
**As a** business owner
**I want to** test my CRM connection before saving
**So that** I know credentials are correct

**Acceptance Criteria:**
```gherkin
Scenario: Test YCLIENTS connection
  Given I entered YCLIENTS API token
  When I click "Test Connection"
  Then API call is made: GET https://api.yclients.com/api/v1/company/{company_id}
  And if successful: "✅ Connection successful"
  And if failed: "❌ Invalid API token or Company ID"
```

---

### User Story 8.3.3-8.3.5: View Logs & Statistics
**As a** business owner
**I want to** see integration logs and statistics
**So that** I monitor sync health

**Acceptance Criteria:**
```gherkin
Scenario: View integration logs
  Given I am on Admin Panel → "Интеграции" → "Логи"
  When I view logs
  Then I see last 100 log entries:
    - 2025-11-17 14:10 | SUCCESS | Synced 5 transactions
    - 2025-11-17 14:05 | ERROR | Connection timeout
    - 2025-11-17 14:00 | SUCCESS | Synced 3 transactions

Scenario: View sync statistics
  Given I view "Статистика интеграции"
  When page loads
  Then I see:
    - Total synced transactions: 1,245
    - Last successful sync: 5 minutes ago
    - Success rate (30 days): 98.5%
    - Failed syncs (30 days): 12
    - Average sync time: 2.3 seconds
```

---

## 📊 Technical Requirements

### CRM Adapter Architecture
- **Base adapter interface:**
  ```python
  class BaseCRMAdapter(ABC):
      @abstractmethod
      async def fetch_transactions(self, since: datetime) -> List[Dict]:
          pass
      
      @abstractmethod
      def map_transaction(self, crm_tx: Dict) -> Transaction:
          pass
      
      @abstractmethod
      async def health_check(self) -> bool:
          pass
  ```

### Sync Performance
- Sync frequency: Every 5 minutes
- Max sync time: <30 seconds per business
- Webhook processing: <200ms (async queue)
- Duplicate detection: <10ms (indexed external_id)

---

## 🔄 Dependencies

- **Module 2 (Loyalty):** Trigger bonus accrual after transaction sync
- **Module 3 (Transactions):** Store synced transactions
- **Module 13 (Security):** Encrypt CRM credentials (AES-256)

---

## ✅ Success Criteria

- [ ] All 6 CRM connectors operational (1С, YCLIENTS, AMO CRM, Renovatio, Iiko, CSV)
- [ ] Sync latency: <5 minutes (scheduled) or <1 minute (webhook)
- [ ] 0 duplicate transactions
- [ ] 99% sync success rate (30-day average)
- [ ] Retry mechanism: 95% of temporary failures resolved automatically
- [ ] CSV upload supports 50K+ transactions

---

**Last Updated:** 2025-11-17
**Owner:** Backend Integrations Team
**Status:** Critical - MVP Required
