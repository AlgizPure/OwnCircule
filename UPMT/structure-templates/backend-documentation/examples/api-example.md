# GET /api/users/:id (Minimal Example)

**Auth Required:** Yes

---

## REQUEST

```http
GET /api/users/550e8400-e29b-41d4-a716-446655440000 HTTP/1.1
Authorization: Bearer YOUR_TOKEN
```

---

## RESPONSE (200 OK)

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "john@example.com",
  "name": "John Doe",
  "createdAt": "2025-11-10T12:00:00Z"
}
```

---

## ERRORS

- **401** - Missing/invalid token
- **403** - Insufficient permissions
- **404** - User not found

---

## FRONTEND USAGE

```typescript
const { data, isLoading } = useQuery(['user', id], () => 
  api.get(`/users/${id}`)
);
```

---

**See:** [Full Template](_API_ENDPOINT_TEMPLATE.md) for complete API documentation structure

