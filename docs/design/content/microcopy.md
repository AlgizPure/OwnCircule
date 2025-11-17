# MICROCOPY
## Small Words, Big Impact

**Version:** 2.0
**Last Updated:** November 2025
**Definition:** Microcopy = The small texts that guide, instruct, and reassure users throughout the interface

---

## 🎯 WHAT IS MICROCOPY?

Microcopy is every small piece of text that helps users navigate:

- **Button labels** - "Записаться", "Сохранить"
- **Form labels** - "Телефон", "Дата рождения"
- **Placeholders** - "Введите ваше имя..."
- **Helper text** - "Пароль должен быть минимум 8 символов"
- **Tooltips** - "Нажмите, чтобы скопировать"
- **Empty states** - "Вы ещё не посетили партнёров"
- **Loading states** - "Загружаем события..."
- **Confirmation messages** - "Бронирование подтверждено"
- **Status labels** - "Gold Member", "В ожидании"

**Microcopy is often overlooked but absolutely critical to UX.** It's where personality meets function.

---

## 🔘 BUTTON LABELS

Buttons are calls-to-action. Make them clear, specific, and compelling.

### DO'S - Good Button Labels

**Use action verbs (clear intent):**
```
✅ "Записаться на услугу"
✅ "Сохранить изменения"
✅ "Подтвердить номер"
✅ "Добавить в избранное"
✅ "Отправить приглашение"
```

**Be specific (not generic):**
```
✅ "Забронировать маникюр" (specific)
❌ "Отправить" (what am I sending?)

✅ "Скачать квитанцию" (specific)
❌ "Скачать" (what?)

✅ "Поделиться в Instagram" (specific)
❌ "Поделиться" (where?)
```

**Be concise (1-3 words when possible):**
```
✅ "Записаться" (1 word - when context is clear)
✅ "Записаться на услугу" (3 words - clear context)
❌ "Нажмите здесь, чтобы записаться на услугу в нашу систему" (too long)
```

**Match the action:**
```
✅ Primary CTA: "Записаться" (main action)
✅ Secondary CTA: "Узнать больше" (additional info)
✅ Tertiary CTA: "Назад" (cancel/exit)
✅ Destructive CTA: "Удалить" (dangerous action - usually red)
```

### DON'Ts - Bad Button Labels

```
❌ Generic verbs:
- "ОК" (doesn't say what it does)
- "Подтвердить" (too vague)
- "Отправить" (to where? what?)
- "Продолжить" (continue what?)

❌ Vague phrasing:
- "Нажмите здесь"
- "Выполнить действие"
- "Применить"

❌ Too casual/wrong tone:
- "Давай" (too casual for premium audience)
- "Ща будет" (slang, unprofessional)
- "Забей" (dismissive)

❌ Too formal/stiff:
- "Произвести действие записи" (overly complex)
- "Осуществить сохранение" (bureaucratic)
```

### Button Label Patterns

**Svoy Krug specific patterns:**

```
PRIMARY ACTION (Main goal):
✅ "Записаться на услугу"
✅ "Забронировать время"
✅ "Присоединиться к событию"

SECONDARY ACTION (Additional options):
✅ "Добавить в избранное"
✅ "Поделиться партнёром"
✅ "Оставить отзыв"

NAVIGATION:
✅ "Назад"
✅ "Далее"
✅ "Просмотреть все партнёры"

DESTRUCTIVE (Delete/Cancel):
✅ "Отменить бронирование"
✅ "Удалить из избранного"
✅ "Выйти из клуба" (rare, serious)
```

### React Native Button Implementation

```javascript
// GOOD: Clear, specific, appropriately sized
<Button
  title="Записаться на услугу"
  onPress={() => navigation.navigate('Booking')}
  color={colors.primary}
/>

// BAD: Too generic
<Button
  title="OK"
  onPress={handleConfirm}
/>

// GOOD: With icons (icon + text)
<Button
  title="Добавить в избранное"
  icon={<HeartIcon />}
  onPress={addFavorite}
/>

// CONTEXT: Primary vs Secondary vs Destructive
<View style={styles.buttonGroup}>
  {/* Primary - main action */}
  <TouchableOpacity style={[styles.button, styles.primary]}>
    <Text>Записаться</Text>
  </TouchableOpacity>

  {/* Secondary - alternative */}
  <TouchableOpacity style={[styles.button, styles.secondary]}>
    <Text>Узнать больше</Text>
  </TouchableOpacity>

  {/* Tertiary - cancel */}
  <TouchableOpacity style={[styles.button, styles.tertiary]}>
    <Text>Отмена</Text>
  </TouchableOpacity>

  {/* Destructive - dangerous action */}
  <TouchableOpacity style={[styles.button, styles.destructive]}>
    <Text>Удалить</Text>
  </TouchableOpacity>
</View>
```

---

## 🏷️ FORM LABELS

Labels tell users what information you're asking for.

### Principle: Be Specific

```
❌ Generic/Vague:
- "Имя"
- "Телефон"
- "Адрес"
- "Дата"

✅ Specific/Helpful:
- "Полное имя и отчество"
- "Номер телефона"
- "Адрес проживания"
- "Дата рождения"
```

### Pattern: Label + Hint + Validation

```javascript
// COMPLETE FORM FIELD:

// 1. Label (what we're asking)
<Text style={styles.label}>Номер телефона</Text>

// 2. Input field
<TextInput
  placeholder="+7 (XXX) XXX-XX-XX"
  keyboardType="phone-pad"
  value={phone}
  onChangeText={setPhone}
/>

// 3. Helper text (additional guidance)
<Text style={styles.helperText}>
  Используется для входа и восстановления пароля
</Text>

// 4. Error message (if validation fails)
{errors.phone && (
  <Text style={styles.errorText}>{errors.phone}</Text>
)}
```

### Svoy Krug Form Examples

```
ACCOUNT SETUP:
✅ "Полное имя и отчество"
✅ "Email для входа"
✅ "Номер телефона"

PROFILE:
✅ "Дата рождения"
✅ "Предпочитаемый город"
✅ "Категории услуг"

PREFERENCES:
✅ "Ваши любимые партнёры"
✅ "Типы событий, которые вас интересуют"
```

### Optional Field Indication

```
✅ Inline: "Отчество (не обязательно)"
✅ Bracket: "Отчество [необязательно]"
✅ Asterisk (for required): "Имя *"
✅ Subtle text: "Отчество - необязательно"

BEST PRACTICE: Be explicit about which fields are optional
```

---

## 💬 HELPER TEXT

Helper text provides context, format guidance, and reassurance.

### Use Cases

**Format requirements:**
```
Password
[________________]
✅ "Минимум 8 символов, включая буквы и цифры"
```

**Privacy assurance:**
```
Email
[________________]
✅ "Ваш email не будет видны другим участницам"
✅ "Мы никогда не делимся вашими данными"
```

**Examples:**
```
Отчество (если есть)
[________________]
✅ "Например, Александровна, Сергеевна"
```

**Why it's needed:**
```
Дата рождения
[________________]
✅ "Нужна для проверки возраста в системе"
```

**Capacity/Limit:**
```
Биография
[________________]
✅ "Максимум 200 символов"
```

### Svoy Krug Helper Text Examples

```
"Вашим партнёрам не будет видна эта информация"

"Эта информация используется для персональных рекомендаций"

"Вы получите напоминание за 24 часа до события"

"Кешбэк начисляется на счёт автоматически"

"Gold статус активируется при 5+ визитах"
```

### React Native Implementation

```javascript
<View style={styles.formField}>
  <Text style={styles.label}>Email</Text>
  <TextInput
    style={styles.input}
    placeholder="Ваша почта"
  />
  <Text style={styles.helperText}>
    Мы отправим подтверждение. Спам не отправляем.
  </Text>
</View>
```

---

## 📍 PLACEHOLDERS

Placeholders show the format or give examples of what to enter.

### DO'S

**Show format/example:**
```
✅ name@example.com
✅ +7 (XXX) XXX-XX-XX
✅ Поиск по имени или услуге...
✅ Например, помощь с макияжем...
```

**Use real examples:**
```
✅ "Марина Петрова" (real example)
✅ "Салон красоты 'Миндаль'" (real example)
❌ "ХХХ" (not helpful)
❌ "Text here" (not helpful)
```

### DON'Ts

```
❌ Just repeat the label:
- Label: "Имя"
- Placeholder: "Имя" (redundant!)

❌ Use placeholder as label:
- No visible label, only placeholder
- Placeholder disappears when typing
- Confusing for accessibility

❌ Vague placeholders:
- "Information here"
- "Enter something"
```

### Svoy Krug Placeholder Examples

```
BOOKING:
✅ "Например, маникюр, стрижка, консультация"

SEARCH:
✅ "Салон красоты, косметолог, фотограф..."

MESSAGING:
✅ "Напишите сообщение партнёру..."

FEEDBACK:
✅ "Поделитесь впечатлением от посещения..."
```

---

## 🎈 EMPTY STATES

Empty states occur when there's no content yet. They're an opportunity to educate and encourage.

### Anatomy of Good Empty State

```
┌─────────────────────────┐
│                         │
│      [Icon/Image]       │  1. Visual (friendly, relevant)
│                         │
│  "Вы ещё не записаны"   │  2. Headline (what's missing)
│                         │
│  Забронируйте услугу у  │  3. Description (why it matters)
│  наших партнёров и      │
│  откройте доступ к      │
│  эксклюзивным событиям  │
│                         │
│  [Найти партнёра]       │  4. CTA (what to do)
│                         │
└─────────────────────────┘
```

### Examples

**Empty Bookings List:**
```
📅 "Вы ещё не забронировали услуги"

Начните с посещения наших партнёров:
- Откройте доступ к эксклюзивным событиям
- Накопите бонусы и повысьте статус
- Получите персональные рекомендации

[Найти партнёра]
```

**Empty Favorites:**
```
❤️ "Нет сохранённых партнёров"

Добавляйте понравившихся специалистов:
- Быстро находите их позже
- Будете в курсе их новых предложений
- Получите персональные скидки

[Просмотреть партнёров]
```

**Empty Messages:**
```
💬 "Нет сообщений"

Свяжитесь с партнёром:
- Уточните детали услуги
- Задайте вопросы перед визитом
- Получите рекомендации

[Найти партнёра]
```

**Empty Events:**
```
🎉 "Мероприятия будут добавлены скоро"

Подпишитесь на уведомления, чтобы не пропустить:
- Закрытые события для участниц
- Мастер-классы от партнёров
- Встречи сообщества

[Подписаться]
```

### React Native Empty State Component

```javascript
const EmptyState = ({
  icon,
  title,
  description,
  ctaLabel,
  onCTA
}) => {
  return (
    <View style={styles.emptyContainer}>
      {icon && (
        <Icon source={icon} size={64} />
      )}
      <Text style={styles.emptyTitle}>{title}</Text>
      <Text style={styles.emptyDescription}>
        {description}
      </Text>
      {ctaLabel && (
        <TouchableOpacity
          style={styles.ctaButton}
          onPress={onCTA}
        >
          <Text style={styles.ctaLabel}>{ctaLabel}</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};

// Usage:
<EmptyState
  icon="calendar"
  title="Вы ещё не записаны"
  description="Забронируйте услугу у наших партнёров и получите эксклюзивные преимущества"
  ctaLabel="Найти партнёра"
  onCTA={() => navigation.navigate('Partners')}
/>
```

---

## ⏳ LOADING STATES

Show what's loading, not just "Loading..."

### DO'S

```
✅ "Загружаем события..."
✅ "Проверяем доступность времени..."
✅ "Сохраняем ваши изменения..."
✅ "Отправляем приглашение..."
```

### DON'Ts

```
❌ "Загружается..." (too vague)
❌ "Подождите..." (no info)
❌ "Loading..." (English in Russian app)
❌ "Обработка..." (too technical)
```

### React Native Loading Pattern

```javascript
{isLoading ? (
  <View style={styles.loadingContainer}>
    <ActivityIndicator size="large" />
    <Text style={styles.loadingText}>
      "Загружаем события..."
    </Text>
    <Text style={styles.loadingSubtext}>
      "Это займёт всего несколько секунд"
    </Text>
  </View>
) : (
  <EventsList data={events} />
)}
```

---

## 📊 TOOLTIPS & HINTS

Short, helpful text that explains a UI element or action.

### Guidelines

**Keep them short (1-2 sentences):**
```
✅ "Нажмите, чтобы скопировать код приглашения"
❌ "Скопировать уникальный код приглашения, который можно поделиться с друзьями или использовать для их приглашения"
```

**Be action-oriented:**
```
✅ "Свайп влево, чтобы отменить бронирование"
✅ "Удерживайте, чтобы сохранить партнёра"
```

**Don't explain what's obvious:**
```
❌ "Нажмите кнопку сохранить, чтобы сохранить ваши изменения"
✅ "Изменения сохраняются автоматически"
```

### React Native Implementation

```javascript
<Tooltip
  message="Скопировать код приглашения"
  duration={2000}
>
  <TouchableOpacity onPress={copyCode}>
    <Text>000123-ABC-456</Text>
  </TouchableOpacity>
</Tooltip>
```

---

## 🏆 STATUS & BADGE LABELS

Small labels that show state or achievement.

### Status Labels

```
IN PROGRESS:
✅ "В обработке"
✅ "Подтверждение..."
✅ "В ожидании"

CONFIRMED:
✅ "Подтверждено"
✅ "Принято"
✅ "Готово"

MEMBER STATUS:
✅ "Bronze" (without explanation if clear)
✅ "Bronze (1-2 визита)"
✅ "Gold · VIP Member"
```

### Achievement Labels

```
✅ "Новый уровень: Gold!"
✅ "Вы помогли 3 участницам"
✅ "Заработано 500 бонусов"
```

---

## 🔔 NOTIFICATION MICROCOPY

**Push Notifications (ultra-brief):**
```
✅ "Ваш любимый партнёр опубликовал новое предложение"
✅ "До события 'Гастро-вечер' осталось 2 часа"
✅ "Марина оставила отзыв на вашу услугу"

❌ "Новое уведомление"
❌ "Проверьте приложение"
```

**In-App Notifications (slightly more context):**
```
✅ "Марина оставила 5-звёздочный отзыв на вашу консультацию
   по макияжу. Спасибо за отличный сервис!"

✅ "До события 'Мастер-класс по уходу за кожей'
   осталось 3 часа. Не забудьте!
   [Напомнить позже]"
```

---

## ✅ MICROCOPY CHECKLIST

Before publishing any microcopy, ask:

- [ ] Is it specific (not vague)?
- [ ] Is it as brief as possible?
- [ ] Does it use active voice?
- [ ] Is the tone appropriate?
- [ ] Does it use "Вы" (formal Russian)?
- [ ] Would a busy person understand it instantly?
- [ ] Does it help users succeed?
- [ ] Could I use fewer words?
- [ ] Would I add punctuation? (Avoid unless necessary)

---

## 📱 MICROCOPY PATTERNS IN SVOY KRUG

### Booking Flow

```
1. Landing:
   Button: "Найти партнёра"

2. Partner List:
   Button: "Записаться на услугу"
   Helper: "Выберите удобное время"

3. Time Selection:
   Label: "Выберите время"
   Empty state: "Свободные слоты будут добавлены скоро"

4. Confirmation:
   Label: "Подтверждаю время"
   CTA: "Записаться"

5. Success:
   Message: "Бронирование подтверждено!"
   Helper: "Напоминание придёт за 24 часа"
```

### Event Flow

```
1. Events List:
   Empty: "Мероприятия будут скоро"
   Upcoming: "Осталось 3 места"

2. Event Details:
   Button: "Присоединиться"
   Helper: "Только для участниц клуба"

3. Success:
   Message: "Вы добавлены в событие!"
   Helper: "Мы пришлём деталь о месте и времени"
```

---

## 🎯 COMMON MISTAKES TO AVOID

```
❌ Using English in Russian app
❌ Generic copy ("Click here", "Submit")
❌ Jargon ("Sync error", "System error")
❌ Too much copy for such small space
❌ Inconsistent terminology
❌ Passive voice ("Changes were saved")
❌ Blaming user ("You entered wrong")
❌ Assuming context
```

---

**Microcopy is often the difference between a confusing and an intuitive experience.** Make every word count. 🎯

