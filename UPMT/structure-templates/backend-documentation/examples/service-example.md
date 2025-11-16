# Auth Service (Minimal Example)

**Purpose:** Handle user authentication and authorization

---

## RESPONSIBILITIES

- User registration & login
- JWT token generation & validation
- Password hashing & verification
- Session management

---

## API ENDPOINTS

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login user |
| POST | `/api/auth/logout` | Logout user |
| POST | `/api/auth/refresh` | Refresh token |

---

## DEPENDENCIES

- **PostgreSQL** - User data storage
- **Redis** - Session storage
- **bcrypt** - Password hashing

---

## CORE FUNCTION

```typescript
async function login(email: string, password: string): Promise<AuthResponse> {
  // 1. Find user
  const user = await db.users.findByEmail(email);
  
  // 2. Verify password
  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) throw new UnauthorizedError();
  
  // 3. Generate JWT
  const token = jwt.sign({ userId: user.id }, SECRET);
  
  return { user, token };
}
```

---

**See:** [Full Template](_SERVICE_TEMPLATE.md) for complete service documentation structure

