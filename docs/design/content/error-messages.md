# ERROR MESSAGES
## Helpful, Not Blaming, Solutions-Focused

**Version:** 2.0
**Last Updated:** November 2025
**Philosophy:** Errors are moments to build trust, not confirm incompetence

---

## 🎯 ERROR MESSAGE ANATOMY

Every good error message has these elements:

### 1. What Happened (Be Specific)

Never say "Error" or show error codes.

```
❌ "Error 400"
❌ "Invalid request"

✅ "Не удалось подтвердить номер телефона"
✅ "Партнёр недоступен в это время"
```

### 2. Why It Happened (Optional but Helpful)

Help the user understand what went wrong.

```
❌ "Network error"

✅ "Проверьте интернет-соединение — кажется, вы находитесь вне сети"
✅ "Этот телефон уже зарегистрирован — возможно, вы создавали акаунт раньше?"
```

### 3. How to Fix It (Action-Oriented)

Always provide a clear next step.

```
❌ "Something went wrong"

✅ "Попробуйте отправить запрос снова" [Повторить]
✅ "Свяжитесь с поддержкой" [Написать]
✅ "Обновите приложение на последнюю версию" [Обновить]
```

---

## 📋 ERROR TYPES & EXAMPLES

### FORM VALIDATION ERRORS

**When:** User filled in field incorrectly

**Tone:** Helpful, specific, not blaming

```
❌ WRONG:
- "Invalid email"
- "Password too short"
- "Required field"
- "Error in form"

✅ RIGHT:
- "Email должен содержать @ символ"
- "Пароль должен быть минимум 8 символов"
- "Это поле обязательное"
- "Проверьте данные в полях выше"
```

**React Native example:**
```javascript
// WRONG
Alert.alert("Error", "Invalid input");

// RIGHT
Alert.alert(
  "Номер телефона не распознан",
  "Убедитесь, что вы указали номер в формате +7 (XXX) XXX-XX-XX"
);

// With actionable button
Alert.alert(
  "Пароль слишком простой",
  "Используйте буквы, цифры и символы для безопасности",
  [
    { text: "Изменить пароль", onPress: () => { /* ... */ } },
    { text: "Помощь", onPress: () => openHelp() }
  ]
);
```

---

### NETWORK/CONNECTIVITY ERRORS

**When:** No internet, server down, timeout

**Tone:** Apologetic, reassuring, solution-focused

```
❌ WRONG:
- "Connection timeout"
- "Server error"
- "Network unreachable"
- "Failed to connect"

✅ RIGHT:
- "Проверьте интернет-соединение и повторите попытку"
- "Наш сервер на обслуживании. Вернёмся в 18:00"
- "Медленное соединение. Это может занять дольше"
- "Не удалось подключиться. Убедитесь, что Wi-Fi включён"
```

**Recovery options:**
```
"Не удалось загрузить события.
 Проверьте интернет и попробуйте снова"

[Повторить] [Назад] [Написать нам]
```

---

### AUTHENTICATION ERRORS

**When:** Login failed, password wrong, session expired

**Tone:** Helpful, trustworthy, offering recovery

```
❌ WRONG:
- "Authentication failed"
- "Invalid credentials"
- "Login error"
- "Token expired"

✅ RIGHT:
- "Email или пароль неправильны. Попробуйте снова"
- "Ваша сессия истекла. Пожалуйста, войдите снова"
- "Учётная запись заблокирована. Свяжитесь с поддержкой"
- "Email не найден в системе. Создайте новый акаунт?"
```

**With recovery paths:**
```
"Email или пароль неправильны"

[Попробуйте снова]
[Забыли пароль?] ← Helpful link
[Создать новый акаунт?] ← Alternative path
```

---

### BOOKING/AVAILABILITY ERRORS

**When:** Time slot taken, partner unavailable, etc.

**Tone:** Empathetic, offering alternatives

```
❌ WRONG:
- "Slot unavailable"
- "Cannot book"
- "Time conflict"

✅ RIGHT (in Svoy Krug context):
- "К сожалению, мастер недоступен в это время"
- "Это время уже занято. Доступны ещё слоты в 15:00 и 16:30"
- "Партнёр не принимает заказы в выбранный день"
- "У вас уже есть бронирование на это время"
```

**Offering alternatives:**
```
"Салон красоты 'Миндаль' недоступен в понедельник в 14:00

Доступные времена:
- Понедельник 15:30
- Вторник 11:00
- Вторник 14:00

[Выбрать время] [Другой партнёр]"
```

---

### PAYMENT ERRORS

**When:** Payment declined, card invalid, insufficient funds

**Tone:** Reassuring, not accusatory, offering solutions

```
❌ WRONG:
- "Payment failed"
- "Card rejected"
- "Transaction declined"
- "Insufficient funds"

✅ RIGHT:
- "Платёж не прошёл. Проверьте данные карты и попробуйте снова"
- "Карта отклонена банком. Позвоните в банк или используйте другую карту"
- "На вашей карте недостаточно средств"
- "Платёж заблокирован сервисом безопасности. Подтвердите в приложении банка"
```

**With solutions:**
```
"Платёж не прошёл

Возможные причины:
- На карте недостаточно средств
- Карта заблокирована для онлайн-платежей
- Неверно введены данные карты

[Попробовать снова]
[Использовать другую карту]
[Связаться с банком]"
```

---

### PERMISSION/ACCESS ERRORS

**When:** Not authorized, feature locked, trial expired

**Tone:** Clear about limitations, offering upgrade path

```
❌ WRONG:
- "Access denied"
- "Unauthorized"
- "Feature unavailable"
- "Permission required"

✅ RIGHT:
- "Эта функция доступна только участницам Gold статуса"
- "Вы не можете редактировать профиль другой участницы"
- "Это событие только для членов клуба"
- "Вы использовали все приглашения на этот месяц"
```

**Suggesting action:**
```
"Персональный консьерж — только для Gold членов

Ваш статус: Silver (2 визита из 5 до Gold)

Хотите перейти в Gold сейчас?"

[Узнать о Gold] [Нет, спасибо]
```

---

### SYNC/DATA ERRORS

**When:** Data conflict, sync failed, duplicate action

**Tone:** Technical but clear, reassuring about data safety

```
❌ WRONG:
- "Sync error"
- "Data mismatch"
- "Database error"

✅ RIGHT:
- "Изменения не удалось сохранить. Попробуйте ещё раз"
- "Ваши данные загружены, но уведомления ещё не синхронизированы"
- "Это действие уже выполнено. Проверьте историю"
- "Данные обновляются. Подождите..."
```

---

## 🚨 CRITICAL ERRORS (Should Rarely Happen)

**When:** System critical, data loss risk, security issue

**Tone:** Serious but calm, clear action required

```
❌ WRONG:
- "FATAL ERROR"
- "SYSTEM FAILURE"
- "CRITICAL BUG"

✅ RIGHT:
- "⚠️ ВНИМАНИЕ: Это действие удалит все ваши данные.
     Эту операцию нельзя отменить. Вы уверены?"

- "🔒 По соображениям безопасности, мы удалили вашу сессию.
     Пожалуйста, войдите снова"

- "🛡️ Мы обнаружили необычную активность.
     Пожалуйста, измените пароль сейчас
     [Изменить пароль]"
```

---

## 📱 ERROR PRESENTATION (React Native)

### Toast Notifications (Small, non-blocking)

**Use for:** Non-critical, not urgent, temporary

```javascript
import { Snackbar } from '@react-native-material/core';

// Bad network (but will retry)
<Snackbar
  message="Медленное соединение..."
  duration={3000}
/>

// Minor validation issue
<Snackbar
  message="Проверьте заполненные поля"
  action={{ label: 'ОК' }}
/>
```

### Modal/Alert (Blocking, needs response)

**Use for:** Important errors, requires user action

```javascript
// Form validation
Alert.alert(
  "Проверьте данные",
  "Email должен содержать @ символ",
  [{ text: "ОК" }]
);

// Booking error with alternatives
Alert.alert(
  "Время недоступно",
  "Мастер занят в это время. Доступны 15:30 и 16:45",
  [
    { text: "15:30", onPress: () => selectTime('15:30') },
    { text: "16:45", onPress: () => selectTime('16:45') },
    { text: "Отмена", isPreferred: true }
  ]
);
```

### Inline Validation (Under field)

**Use for:** Form fields, real-time validation

```javascript
<TextInput
  placeholder="Номер телефона"
  onChangeText={(text) => {
    setPhone(text);
    if (!isValidPhone(text)) {
      setPhoneError("Номер должен содержать 11 цифр");
    }
  }}
/>
{phoneError && (
  <Text style={styles.errorText}>{phoneError}</Text>
)}
```

---

## 🎨 VISUAL TREATMENT

### Color & Icons

```
Error (blocking): Red (#EF5350)
- Icon: ❌ X or alert-circle
- Background: Light red (#FFEBEE)
- Example: Form validation, payment failed

Warning (caution needed): Orange (#FF9800)
- Icon: ⚠️ Alert triangle
- Background: Light orange (#FFF3E0)
- Example: About to delete, limited time

Info (FYI, not a problem): Blue (#2196F3)
- Icon: ℹ️ Info circle
- Background: Light blue (#E3F2FD)
- Example: Helpful hints, status updates

Success (recovery option): Green (#4CAF50)
- Icon: ✓ Check mark
- Background: Light green (#E8F5E9)
- Example: "Retry successful", "Send email"
```

### Positioning

**Inline (preferred for forms):**
```
Email
[_________________]
❌ Email должен содержать @ символ
```

**Toast (for non-blocking errors):**
```
[❌ Не удалось сохранить] ✕
```

**Full-screen modal (for critical errors):**
```
┌─────────────────────┐
│ ⚠️ Внимание          │
│                     │
│ Это действие нельзя │
│ отменить.           │
│ Вы уверены?        │
│                     │
│ [Отмена] [Удалить] │
└─────────────────────┘
```

---

## 🔄 ERROR RECOVERY

Always provide a clear recovery path:

### Recovery Buttons

```
PRIMARY ACTION (preferred):
[Повторить] or [Попробуйте снова]

ALTERNATIVE ACTIONS:
[Другой способ] or [Альтернатива]
[Назад] or [Отмена]
[Написать нам] or [Служба поддержки]
```

### Retry Logic

```javascript
// Exponential backoff for network errors
const retryWithBackoff = async (fn, maxAttempts = 3) => {
  for (let i = 1; i <= maxAttempts; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxAttempts) throw error;
      // Wait 1s, 2s, 4s between retries
      await delay(Math.pow(2, i - 1) * 1000);
    }
  }
};

// Usage
await retryWithBackoff(() => bookSlot(data))
  .catch(() => {
    Alert.alert(
      "Не удалось записать",
      "Попробуйте позже или напишите нам"
    );
  });
```

---

## ✅ DO'S

**Error Message Best Practices:**

- ✅ Be specific ("Email должен содержать @", not "Invalid email")
- ✅ Be polite and respectful (never blame)
- ✅ Offer solutions (always provide next step)
- ✅ Use plain language (no tech jargon)
- ✅ Be brief (say it once, clearly)
- ✅ Use appropriate tone (serious for critical, helpful for minor)
- ✅ Show related recovery options
- ✅ Make errors easy to dismiss
- ✅ Offer contact options for support
- ✅ Remember the context (in Russia, formal "Вы")

---

## ❌ DON'TS

**What Makes Bad Error Messages:**

- ❌ Don't show error codes ("Error 500", "HTTP 400")
- ❌ Don't blame the user ("You entered wrong data")
- ❌ Don't use jargon ("Authentication token expired")
- ❌ Don't be vague ("Something went wrong")
- ❌ Don't use all caps ("ERROR!")
- ❌ Don't be cute or emoji-heavy ("Oopsie doopsie! 🙈")
- ❌ Don't provide no recovery path
- ❌ Don't hide errors (validate early, show clearly)
- ❌ Don't use technical language for non-technical users
- ❌ Don't repeat the same error message for different issues

---

## 📋 ERROR MESSAGE CHECKLIST

Before publishing an error message:

- [ ] Is it specific? (not "Error")
- [ ] Does it explain what happened?
- [ ] Does it explain why?
- [ ] Does it tell user how to fix it?
- [ ] Is it in plain language?
- [ ] Is tone appropriate?
- [ ] Is recovery path clear?
- [ ] Would I understand this in 3 seconds?
- [ ] Would user feel blamed? (Fix if yes)
- [ ] Is it using "Вы" (formal Russian)?

---

## 🌍 PROJECT-SPECIFIC EXAMPLES

### Svoy Krug Booking Errors

```
❌ WRONG: "Booking failed"
✅ RIGHT: "Не удалось записаться на услугу.
           Проверьте доступность времени и попробуйте снова"

Recovery:
[Выбрать другое время] [Другой партнёр]
```

### Svoy Krug Event Errors

```
❌ WRONG: "Event unavailable"
✅ RIGHT: "К сожалению, мест на событии больше нет.
           Вас добавим в список ожидания?"

Recovery:
[В список ожидания] [Другие события]
```

### Svoy Krug Status/Points Errors

```
❌ WRONG: "Cannot redeem"
✅ RIGHT: "Недостаточно бонусов. Вам нужно 500 точек,
           у вас есть 350"

Recovery:
[Как получить ещё баллы?] [Назад]
```

---

## 📞 SUPPORT ESCALATION

For errors user can't fix:

```
"Что-то пошло не так с нашей стороны.
 Наша команда уже работает над этим.

 Хотите, чтобы мы вам написали?"

[Напишите нам] [Назад]

// If they click "Напишите нам"
// Pre-fill support ticket with:
// - What they were trying to do
// - What error they saw
// - Their device info
// - Timestamp
```

---

**Errors are chances to build trust. Handle them with care.** 🛡️

