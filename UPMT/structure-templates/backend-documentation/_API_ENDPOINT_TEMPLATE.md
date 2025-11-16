# [Resource] API - [Endpoint Name]

**Endpoint:** `[METHOD] /api/v1/[resource]/[path]`  
**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Auth Required:** [Yes/No]

---

## 📋 OVERVIEW

**Purpose:** [What does this endpoint do? One sentence.]

**Use Case:** [When would a client call this endpoint?]

**Example:**
Purpose: Retrieve a user by their unique ID  
Use Case: Display user profile page, show user details in admin panel

---

## 🔐 AUTHENTICATION & AUTHORIZATION

**Authentication:** [Required/Optional/Not Required]  
**Required Token:** [Access Token / Refresh Token / None]

**Authorization Rules:**
- [Role/Permission required to access]
- [Resource ownership requirements]

**Example:**
Authentication: Required (Bearer token)  
Authorization:
- User can access own data
- Admin can access any user data
- Guest cannot access

---

## 📥 REQUEST

### HTTP Method & URL

```http
[METHOD] /api/v1/[resource]/[path] HTTP/1.1
Host: api.example.com
Authorization: Bearer [token]
Content-Type: application/json
```

---

### Path Parameters

| Parameter | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| `[param]` | [type] | [Yes/No] | [Description] | [Validation rules] |

**Example:**
| Parameter | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| `id` | UUID | Yes | User unique identifier | Valid UUID v4 |

---

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `[param]` | [type] | [Yes/No] | [value] | [Description] |

**Example:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `include` | string | No | - | Related resources to include (comma-separated) |
| `fields` | string | No | all | Fields to return (comma-separated) |

---

### Request Headers

**Required Headers:**
```http
Authorization: Bearer [access_token]
Content-Type: application/json
```

**Optional Headers:**
```http
X-Request-ID: [uuid]  (for tracing)
Accept-Language: [language]  (for i18n)
```

---

### Request Body

**Schema:**
```json
{
  "field1": "type",
  "field2": "type",
  "nested": {
    "field": "type"
  }
}
```

**Field Descriptions:**

| Field | Type | Required | Description | Validation |
|-------|------|----------|-------------|------------|
| `field1` | string | Yes | [Description] | [Validation rules] |
| `field2` | number | No | [Description] | [Validation rules] |

**Example Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user"
}
```

---

### Request Example

**cURL:**
```bash
curl -X [METHOD] https://api.example.com/v1/[resource]/[id] \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "field": "value"
  }'
```

**JavaScript (fetch):**
```javascript
const response = await fetch('https://api.example.com/v1/[resource]/[id]', {
  method: '[METHOD]',
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    field: 'value'
  })
});

const data = await response.json();
```

**TypeScript (with types):**
```typescript
interface [Resource]Request {
  field: string;
  field2?: number;
}

interface [Resource]Response {
  id: string;
  field: string;
  createdAt: string;
}

const response = await fetch<[Resource]Response>(
  `https://api.example.com/v1/[resource]/${id}`,
  {
    method: '[METHOD]',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
  }
);
```

---

## 📤 RESPONSE

### Success Response

**Status Code:** `[200/201/204] [Status Name]`

**Response Headers:**
```http
Content-Type: application/json
X-Request-ID: [uuid]
X-RateLimit-Remaining: [number]
```

**Response Body Schema:**
```json
{
  "id": "uuid",
  "field": "value",
  "createdAt": "ISO 8601",
  "updatedAt": "ISO 8601"
}
```

**Field Descriptions:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Unique identifier |
| `field` | string | [Description] |
| `createdAt` | ISO 8601 | Creation timestamp |

**Success Example (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user",
  "createdAt": "2025-11-10T12:00:00Z",
  "updatedAt": "2025-11-10T14:30:00Z"
}
```

---

### Error Responses

#### 400 Bad Request

**When:** Invalid input, validation errors

```json
{
  "error": "Validation failed",
  "code": "VALIDATION_ERROR",
  "details": {
    "email": ["Invalid email format"],
    "name": ["Too short, min 2 characters"]
  },
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 401 Unauthorized

**When:** Missing or invalid authentication token

```json
{
  "error": "Authentication required",
  "code": "UNAUTHORIZED",
  "details": "Valid access token required",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 403 Forbidden

**When:** Insufficient permissions

```json
{
  "error": "Insufficient permissions",
  "code": "FORBIDDEN",
  "details": "You don't have permission to perform this action",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 404 Not Found

**When:** Resource doesn't exist

```json
{
  "error": "[Resource] not found",
  "code": "[RESOURCE]_NOT_FOUND",
  "details": "No [resource] found with id: [id]",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 409 Conflict

**When:** Resource already exists (duplicate)

```json
{
  "error": "[Resource] already exists",
  "code": "DUPLICATE_RESOURCE",
  "details": "[Field] '[value]' is already taken",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 422 Unprocessable Entity

**When:** Business rule violation

```json
{
  "error": "Business rule violation",
  "code": "BUSINESS_RULE_VIOLATION",
  "details": "[Specific business rule explanation]",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

#### 429 Too Many Requests

**When:** Rate limit exceeded

```json
{
  "error": "Rate limit exceeded",
  "code": "RATE_LIMIT_EXCEEDED",
  "details": "You have exceeded 1000 requests per hour",
  "retryAfter": 3600,
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

**Headers:**
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1699635600
Retry-After: 3600
```

---

#### 500 Internal Server Error

**When:** Unexpected server error

```json
{
  "error": "Internal server error",
  "code": "INTERNAL_SERVER_ERROR",
  "details": "An unexpected error occurred",
  "requestId": "uuid",
  "timestamp": "2025-11-10T12:00:00Z"
}
```

---

## 💡 USAGE EXAMPLES

### Frontend Implementation

**React Hook:**
```typescript
import { useQuery, useMutation } from '@tanstack/react-query';

// For GET requests
function use[Resource](id: string) {
  return useQuery(['[resource]', id], () => 
    api.get(`/[resource]/${id}`)
  );
}

// For POST/PATCH/DELETE requests
function use[Resource]Mutation() {
  return useMutation((data: [Resource]Data) => 
    api.[method](`/[resource]`, data)
  );
}

// Usage in component
function [Resource]Component({ id }: Props) {
  const { data, isLoading, error } = use[Resource](id);
  
  if (isLoading) return <Loading />;
  if (error) return <Error error={error} />;
  
  return <div>{data.name}</div>;
}
```

---

### Backend Implementation Example

**Node.js/Express:**
```typescript
router.[method]('/[resource]/:id', 
  authenticate, // Auth middleware
  authorize('user'), // Permission middleware
  validate(schema), // Validation middleware
  async (req, res) => {
    try {
      const result = await [Resource]Service.[method](req.params.id, req.body);
      res.status([200/201]).json(result);
    } catch (error) {
      if (error instanceof ValidationError) {
        return res.status(400).json({ error: error.message });
      }
      if (error instanceof NotFoundError) {
        return res.status(404).json({ error: error.message });
      }
      res.status(500).json({ error: 'Internal server error' });
    }
  }
);
```

---

## 📝 VALIDATION RULES

| Field | Rules | Error Message |
|-------|-------|---------------|
| `field1` | Required, min 2 chars, max 100 chars | "[Field] must be 2-100 characters" |
| `field2` | Optional, valid email format | "Invalid email format" |
| `field3` | Required, enum: [val1, val2] | "[Field] must be one of: val1, val2" |

---

## 🔄 SIDE EFFECTS

**What happens when this endpoint is called:**

1. [Primary action]
2. [Secondary action (if any)]
3. [Database changes]
4. [External API calls (if any)]
5. [Notifications sent (if any)]

**Example:**
1. User created in database
2. Welcome email sent
3. Audit log entry created
4. User added to default team
5. Notification sent to admins

---

## ⚡ PERFORMANCE

**Expected Response Time:** [X]ms  
**Database Queries:** [N] queries  
**Caching:** [Yes/No] - [Cache strategy]

**Rate Limiting:**
- Window: [time period]
- Limit: [number] requests
- Scope: [per user/per IP/global]

---

## 🧪 TESTING

**Test Cases:**
1. Valid request returns [expected status]
2. Missing auth token returns 401
3. Invalid input returns 400 with validation errors
4. Non-existent resource returns 404
5. Duplicate resource returns 409
6. Permission check: non-owner returns 403

**Example Test (Jest):**
```typescript
describe('[METHOD] /[resource]', () => {
  it('returns [resource] on success', async () => {
    const response = await request(app)
      .[method]('/api/v1/[resource]/[id]')
      .set('Authorization', `Bearer ${token}`)
      .send(validData)
      .expect([status]);
    
    expect(response.body).toMatchObject({
      id: expect.any(String),
      field: 'value'
    });
  });
  
  it('returns 401 without auth', async () => {
    await request(app)
      .[method]('/api/v1/[resource]/[id]')
      .send(validData)
      .expect(401);
  });
});
```

---

## 📚 RELATED DOCUMENTATION

- [API Overview](00_API_OVERVIEW.md)
- [[Resource] Entity](../entities/[resource].md)
- [Authentication API](authentication-api.md)
- [Error Responses](error-responses.md)
- [API Conventions](api-conventions.md)

---

## 📝 CHANGELOG

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [YYYY-MM-DD] | Initial documentation | [Name] |

---

**Navigation:** [← API Overview](00_API_OVERVIEW.md) | [Next Endpoint →]

