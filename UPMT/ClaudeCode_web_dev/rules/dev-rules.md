# Dev Rules

**Версия:** 1.0.0  
**Для:** Development правила и best practices

---

## Code Style

### TypeScript

- ✅ **Strict mode обязателен**
  ```typescript
  // tsconfig.json
  {
    "compilerOptions": {
      "strict": true,
      "noImplicitAny": true,
      "strictNullChecks": true
    }
  }
  ```

- ✅ **No `any` type** (используй `unknown` если нужно)
- ✅ **Explicit return types** для функций
- ✅ **Interface over type** для объектов

### ESLint

- ✅ Следуй ESLint правилам проекта
- ✅ Fix all linter errors перед commit
- ✅ No warnings в production code

### Prettier

- ✅ Auto-format перед commit
- ✅ Consistent formatting

---

## Best Practices

### Single Responsibility

Каждая функция/класс делает одну вещь:

```typescript
// ❌ BAD
function processUserAndSendEmail(user: User) {
  validateUser(user);
  saveToDatabase(user);
  sendWelcomeEmail(user);
}

// ✅ GOOD
function validateUser(user: User) { /* ... */ }
function saveUserToDatabase(user: User) { /* ... */ }
function sendWelcomeEmail(user: User) { /* ... */ }
```

---

### DRY Principle

Don't Repeat Yourself:

```typescript
// ❌ BAD
function getUserName() { /* duplicate logic */ }
function getAdminName() { /* duplicate logic */ }

// ✅ GOOD
function getName(user: User | Admin) { /* shared logic */ }
```

---

### Error Handling

**Всегда обрабатывай ошибки:**

```typescript
// ✅ GOOD
try {
  await riskyOperation();
} catch (error) {
  logger.error('Operation failed:', error);
  throw new AppError('User-friendly message', error);
}
```

**Используй custom errors:**

```typescript
class AuthenticationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'AuthenticationError';
  }
}
```

---

### Comments

**Когда нужны комментарии:**

- ✅ Сложная бизнес-логика
- ✅ Non-obvious решения
- ✅ Workarounds
- ✅ TODO/FIXME

```typescript
// ✅ GOOD: Explains WHY
// Using bcrypt with 12 rounds for balance between security and performance
const BCRYPT_ROUNDS = 12;

// ❌ BAD: States the obvious
// Set rounds to 12
const BCRYPT_ROUNDS = 12;
```

---

## Testing

### Unit Tests

**Для:**
- Бизнес-логика
- Utility functions
- Service methods

**Framework:** Jest / Vitest

```typescript
describe('AuthService', () => {
  it('should hash password correctly', async () => {
    const result = await authService.hashPassword('password123');
    expect(result).toMatch(/^\$2[aby]\$/);
  });
});
```

---

### Integration Tests

**Для:**
- API endpoints
- Database operations
- External services

```typescript
describe('POST /api/auth/login', () => {
  it('should return JWT token on valid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'password' });
    
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('token');
  });
});
```

---

### E2E Tests

**Для:**
- Critical user flows
- Happy paths
- Error scenarios

**Framework:** Playwright / Cypress

---

## Git Commit Messages

**Формат:**

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: Новая фича
- `fix`: Исправление бага
- `docs`: Обновление документации
- `refactor`: Рефакторинг кода
- `test`: Добавление тестов
- `chore`: Техническая работа

**Примеры:**

```bash
feat(auth): implement GitHub OAuth login

- Add OAuth route handler
- Implement token exchange
- Add error handling

Closes #123
```

```bash
fix(api): handle null response from external API

Previously crashed when API returned null.
Now gracefully handles and logs error.
```

---

## Project Rules Integration

**Dev Rules интегрированы с Project Rules:**

При изменении code автоматически срабатывают RULE_XX из:
```
UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md
```

**Обязательно:**
- ✅ Проверяй какие правила сработали
- ✅ Обновляй связанные docs
- ✅ Уведомляй о сработавших правилах

---

## Performance

### Database

- ✅ Use indexes для часто запрашиваемых полей
- ✅ Lazy loading для связанных данных
- ✅ Pagination для больших списков

### API

- ✅ Caching для статических данных
- ✅ Rate limiting
- ✅ Gzip compression

### Frontend

- ✅ Code splitting
- ✅ Lazy loading компонентов
- ✅ Image optimization

---

## Security

### Authentication

- ✅ Hash passwords (bcrypt/argon2)
- ✅ Use HTTPS only
- ✅ Implement rate limiting

### Input Validation

- ✅ Validate all user input
- ✅ Sanitize HTML
- ✅ Use parameterized queries

### Secrets

- ✅ Never commit secrets
- ✅ Use environment variables
- ✅ Rotate credentials regularly

---

**См. также:**
- `code-quality-checklist.md` - Checklist перед commit
- `UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md` - Project Rules

