# ERROR MESSAGES

**Version:** 1.0

---

## 🎯 ANATOMY

**Good error message has 3 parts:**

1. **What happened** (clear explanation)
2. **Why** (if helpful)
3. **How to fix** (actionable next step)

---

## ✅ GOOD EXAMPLES

### Form Validation

```
❌ Error: Invalid input

✅ Email must include @ symbol
✅ Password must be at least 8 characters
✅ This field is required
```

**Specific + actionable**

---

### Server Errors

```
❌ Error 500

✅ Something went wrong on our end.
   We're working on it. Try again in a few minutes?
```

**Apologetic + next step**

---

### Authentication

```
❌ Login failed

✅ Email or password is incorrect. Try again?
   [Forgot password?]
```

**Helpful + recovery option**

---

### File Upload

```
❌ Upload failed

✅ File too large. Maximum size is 5MB.
   Try compressing your image first.
```

**Specific + solution**

---

## ❌ AVOID

**Don't blame user:**
- ❌ "You entered the wrong email"
- ✅ "Email not found. Check spelling?"

**Don't use jargon:**
- ❌ "Authentication token expired"
- ✅ "Your session expired. Please log in again."

**Don't be vague:**
- ❌ "An error occurred"
- ✅ "Couldn't save changes. Check your internet connection."

**Don't be too cute:**
- ❌ "Oopsie doopsie! 🙈"
- ✅ "Couldn't save changes. Try again?"

---

## 🎨 VISUAL TREATMENT

```yaml
Color: error-500 (red)
Icon: X or alert icon
Position: Inline (below field) or toast
Style: Clear, not scary
```

---

## 🔄 RECOVERY

**Always provide next step:**

- Retry button
- Alternative action
- Help link
- Contact support

**Example:**
```
Couldn't connect to server.
[Try Again] [Check Status] [Contact Support]
```

---

**Errors are moments to be helpful, not scary.** 🚨

