# Module 13: Security & Compliance - Requirements

**Module ID:** MOD-13
**Total Functions:** 8
**Priority:** P0 (Critical - MVP)
**Dependencies:** All modules (cross-cutting concern)
**Tech Stack:** Python 3.13, FastAPI 0.121.2, PyJWT 2.9.x, cryptography, PostgreSQL 16.11

---

## 📋 Module Overview

Security module ensures 152-ФЗ compliance (Russian personal data law), врачебная тайна (medical confidentiality), data encryption, JWT-based authentication, 2FA for business accounts, biometric login, audit logging, data anonymization, and role-based access control (RBAC).

**Key Features:**
- Data storage in Russian Federation (Yandex Cloud)
- AES-256 encryption for sensitive fields
- JWT tokens (access + refresh) with RS256 signing
- 2FA (TOTP) for business admin accounts
- Biometric login (FaceID/TouchID) for mobile app
- Comprehensive audit logging for personal data operations
- Medical data anonymization (врачебная тайна)
- RBAC for user/business/admin roles

---

## Function A.1: Russian Data Residency (152-ФЗ)
**As a** platform
**I want to** store all personal data in Russian Federation
**So that** I comply with 152-ФЗ legal requirements

**Acceptance Criteria:**
```gherkin
Scenario: All data stored in RF
  Given platform is deployed
  When data is written to database
  Then all data resides in Yandex Cloud / VK Cloud (Russian regions)
  And data never leaves RF jurisdiction without explicit consent

Scenario: Consent tracking
  Given a user registers
  When they check "Согласие на обработку персональных данных (152-ФЗ)"
  Then consent timestamp is recorded in database
  And consent is required before any data processing
```

**Technical Requirements:**
- Cloud provider: Yandex Cloud (primary), VK Cloud (backup)
- Database regions: `ru-central1` (Moscow), `ru-central2` (Vladimir)
- Object storage: Yandex Object Storage (S3-compatible) in `ru-central1`
- Consent table:
  ```sql
  user_consents (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    consent_type VARCHAR(50),  -- '152FZ' | 'marketing' | 'medical'
    granted_at TIMESTAMP NOT NULL,
    revoked_at TIMESTAMP NULL
  )
  ```

---

## Function A.2: AES-256 Encryption
**As a** platform
**I want to** encrypt sensitive personal data at rest
**So that** data breaches don't expose plaintext PII

**Acceptance Criteria:**
```gherkin
Scenario: Encrypt sensitive fields
  Given a user's personal data is stored
  When data is written to database
  Then the following fields are encrypted with AES-256:
    - Phone number (searchable via hash)
    - Email (searchable via hash)
    - Birthdate
    - Medical transaction details (if medical business)
  And encryption keys are stored in Yandex Key Management Service (KMS)

Scenario: Decrypt for authorized access
  Given encrypted data exists
  When authorized API request retrieves user profile
  Then data is decrypted on-the-fly before sending response
  And decryption is logged in audit log
```

**Technical Requirements:**
- Use Python `cryptography` library with Fernet (AES-256 in CBC mode)
- Key rotation: monthly via Yandex KMS
- Encrypted fields stored as BYTEA in PostgreSQL
- Hash phone/email for lookup: `SHA256(lowercase(phone))`

---

## Function A.3: JWT Tokens (Access + Refresh)
**As a** user
**I want to** authenticate using secure JWT tokens
**So that** my session is protected from hijacking

**Acceptance Criteria:**
```gherkin
Scenario: Login returns JWT tokens
  Given user completes SMS OTP verification
  When authentication succeeds
  Then API returns:
    - Access token (JWT, 15-minute expiry)
    - Refresh token (JWT, 30-day expiry)
  And access token contains: user_id, status_tier, roles
  And tokens are signed with RS256 (private key on server)

Scenario: Access token expiry
  Given access token expired
  When user makes API request
  Then API returns 401 Unauthorized
  And client uses refresh token to get new access token

Scenario: Refresh token rotation
  Given user uses refresh token to renew session
  When new access token is issued
  Then old refresh token is invalidated (one-time use)
  And new refresh token is issued
```

**Technical Requirements:**
- Library: PyJWT 2.9.x with RS256 algorithm
- Private/public key pair stored in Yandex KMS
- Access token expiry: 15 minutes
- Refresh token expiry: 30 days, stored in database with `is_revoked` flag
- Token payload:
  ```json
  {
    "user_id": "uuid",
    "status_tier": "VIP",
    "roles": ["member"],
    "exp": 1700000000,
    "iat": 1699999000
  }
  ```

---

## Function A.4: 2FA for Business Accounts (TOTP)
**As a** business owner
**I want to** enable two-factor authentication on my admin account
**So that** my business data is protected from unauthorized access

**Acceptance Criteria:**
```gherkin
Scenario: Enable 2FA
  Given I am a business admin
  When I go to Security Settings → "Включить 2FA"
  Then I see QR code to scan with authenticator app (Google Authenticator, Authy)
  And I enter 6-digit TOTP code to confirm setup
  Then 2FA is enabled on my account
  And I must enter TOTP code on every login

Scenario: Login with 2FA
  Given I have 2FA enabled
  When I log in with phone + SMS code
  Then I am prompted for 6-digit TOTP code
  And login succeeds only if TOTP is correct
  
Scenario: Backup codes
  Given I enabled 2FA
  When setup completes
  Then I see 10 backup codes (one-time use)
  And I can download codes as PDF
  And I can use backup code if I lose authenticator device
```

**Technical Requirements:**
- Library: `pyotp` for TOTP generation/validation
- TOTP secret stored encrypted in database
- Backup codes: 10 random 8-character codes, hashed (bcrypt)
- 30-second TOTP window with ±1 window tolerance

---

## Function A.5: Biometric Login (FaceID/TouchID)
**As a** mobile app user
**I want to** log in using FaceID/TouchID
**So that** access is fast and secure

**Acceptance Criteria:**
```gherkin
Scenario: Enable biometric login
  Given I completed first SMS login
  When I am prompted "Включить вход по FaceID?"
  And I tap "Включить"
  Then my JWT refresh token is stored in iOS Keychain / Android Keystore
  And next app open prompts for FaceID/TouchID

Scenario: Successful biometric login
  Given biometric login is enabled
  When I open the app
  And I complete FaceID/TouchID verification
  Then I am logged in immediately (using stored refresh token)
  
Scenario: Biometric failure fallback
  Given biometric verification failed 3 times
  When I am prompted "Не удалось распознать. Войти через SMS?"
  And I tap "Да"
  Then I am taken to SMS login flow
```

**Technical Requirements:**
- Mobile library: react-native-biometrics
- Store refresh token in secure storage: iOS Keychain (biometric-protected), Android Keystore
- Refresh token automatically renewed when accessed
- Fallback to SMS login if biometric unavailable or fails

---

## Function A.6: Audit Logging
**As a** compliance officer
**I want to** log all personal data operations
**So that** I can audit 152-ФЗ compliance

**Acceptance Criteria:**
```gherkin
Scenario: Log personal data access
  Given a user's profile is accessed
  When API endpoint GET /api/v1/users/:id is called
  Then an audit log entry is created:
    - Timestamp: 2025-11-17 14:35:22
    - Action: "READ_USER_PROFILE"
    - Actor: admin_user_id or system
    - Target: user_id
    - IP address: 192.168.1.1
    - Result: success/failure

Scenario: Log data modification
  Given a user updates their email
  When PUT /api/v1/users/:id is called
  Then audit log records:
    - Action: "UPDATE_USER_EMAIL"
    - Old value: "old@example.com" (hashed)
    - New value: "new@example.com" (hashed)
    - Actor: user_id (self-modification)

Scenario: Export audit logs
  Given it's year-end audit
  When compliance officer requests audit logs
  Then logs can be exported as CSV with filters (date range, action type, user_id)
```

**Technical Requirements:**
- Audit logs stored in separate table (append-only):
  ```sql
  audit_logs (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
    action VARCHAR(100) NOT NULL,
    actor_id UUID,
    target_user_id UUID,
    ip_address INET,
    user_agent TEXT,
    result VARCHAR(20),  -- 'success' | 'failure'
    details JSONB
  )
  ```
- Log retention: 3 years (152-ФЗ requirement)
- Indexed on timestamp and target_user_id for fast queries

---

## Function A.7: Medical Data Anonymization (врачебная тайна)
**As a** platform
**I want to** anonymize medical transactions
**So that** I comply with врачебная тайна (medical confidentiality)

**Acceptance Criteria:**
```gherkin
Scenario: Identify medical businesses
  Given Миллениум and Стим Центр are medical businesses
  When they are added to platform
  Then they are flagged with `is_medical=TRUE`

Scenario: Exclude medical transactions from cross-promo
  Given a user purchased at Миллениум (medical center)
  When cross-promo chains are evaluated
  Then this transaction is NOT used to trigger coupons at other businesses
  And medical transactions are hidden in business analytics (except for the medical business itself)

Scenario: Anonymize in Win-Win matrix
  Given Win-Win matrix analyzes cross-business conversions
  When medical businesses are involved
  Then their data is aggregated without user-level details
  And matrix shows "Medical (anonymized)" instead of business name
```

**Technical Requirements:**
- Add `is_medical BOOLEAN DEFAULT FALSE` to `businesses` table
- Transactions from medical businesses: `is_medical=TRUE` flag
- Medical transactions excluded from:
  - Cross-promo chain triggers (Module 5)
  - Win-Win analytics (Module 7)
  - Ecosystem-wide analytics (Module 10) unless aggregated

---

## Function A.8: Role-Based Access Control (RBAC)
**As a** platform
**I want to** restrict access based on user roles
**So that** data is only accessible to authorized parties

**Acceptance Criteria:**
```gherkin
Scenario: Member role permissions
  Given I am a regular member (role='member')
  When I try to access my own profile
  Then access is granted
  When I try to access another user's profile
  Then access is denied (403 Forbidden)

Scenario: Business owner role
  Given I am a business owner (role='business_owner')
  When I try to view my business's transactions
  Then access is granted
  When I try to view another business's transactions
  Then access is denied

Scenario: Superadmin role
  Given I am a superadmin (role='superadmin')
  When I try to access any user or business data
  Then access is granted
  And all actions are logged in audit_logs

Scenario: Role hierarchy
  Given roles have hierarchy: superadmin > business_owner > member
  When permissions are checked
  Then higher roles inherit lower role permissions
```

**Technical Requirements:**
- Roles stored in `users` table: `roles JSONB` (array of role strings)
- Possible roles: `member`, `vip`, `elite`, `inner_circle`, `business_owner`, `business_staff`, `superadmin`, `moderator`
- FastAPI dependency for permission checks:
  ```python
  def require_role(required_role: str):
      def dependency(current_user: User = Depends(get_current_user)):
          if required_role not in current_user.roles:
              raise HTTPException(status_code=403, detail="Insufficient permissions")
          return current_user
      return dependency
  ```

---

## 📊 Technical Requirements

### Encryption Stack
- AES-256 (Fernet) for data at rest
- TLS 1.3 for data in transit
- Key management: Yandex KMS

### Authentication Stack
- JWT (PyJWT 2.9.x) with RS256
- TOTP (pyotp) for 2FA
- Biometric (react-native-biometrics) for mobile

### Compliance
- 152-ФЗ: Data in RF, consent tracking, audit logs
- Врачебная тайна: Medical data isolation, anonymization
- GDPR-adjacent: Right to export, right to delete (account deletion)

### Monitoring
- Failed login attempts: >5 in 10 minutes → account lock + alert
- Suspicious API access: unusual IP/location → alert
- Data breach detection: monitor audit logs for bulk exports

---

## 🔄 Dependencies

- **All Modules:** Security is cross-cutting concern
- **Module 1 (Mobile App):** Biometric login integration
- **Module 9/10 (Admin Panels):** RBAC enforcement

---

## ✅ Success Criteria

- [ ] 100% data stored in Russian Federation
- [ ] All sensitive fields encrypted at rest
- [ ] JWT token expiry: 15 minutes (access), 30 days (refresh)
- [ ] 2FA enabled for 100% of business accounts
- [ ] 0 medical data leaks in cross-promo
- [ ] Audit log completeness: 100% of personal data operations logged
- [ ] 152-ФЗ compliance audit passed

---

**Last Updated:** 2025-11-17
**Owner:** Security + Backend Teams
**Status:** Critical - MVP Required
