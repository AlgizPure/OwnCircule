# SCREEN READERS
## ARIA Labels, Semantic HTML, VoiceOver/TalkBack

**Version:** 2.0
**Last Updated:** November 2025
**WCAG Criteria:** 1.1 Text Alternatives, 1.3 Adaptable, 4.1 Compatible
**Platforms:** iOS (VoiceOver), Android (TalkBack)

---

## 🔊 SCREEN READER BASICS

### What Are Screen Readers?

Software that reads page content aloud for blind and low-vision users.

**Popular screen readers:**
- **VoiceOver** (iOS/macOS, built-in, free) ← Test priority
- **TalkBack** (Android, built-in, free) ← Test priority
- **NVDA** (Windows, free)
- **JAWS** (Windows, commercial)

### Core Rule #1: SEMANTIC HTML FIRST

Screen readers rely on proper HTML/component structure.

```
❌ WRONG: DIV everything
<View onPress={action}>
  <Text>Click me</Text>
</View>
// Screen reader: "Click me, text"  (no indication it's a button!)

✅ RIGHT: Semantic components
<TouchableOpacity
  accessible={true}
  accessibilityRole="button"
  onPress={action}
>
  <Text>Нажмите</Text>
</TouchableOpacity>
// Screen reader: "Нажмите, button"  (clear it's a button!)
```

---

## 🏗️ SEMANTIC COMPONENTS IN REACT NATIVE

### Use These Out of the Box

```javascript
// ✅ GOOD (semantic by default)
<TouchableOpacity>        // → button
<TouchableHighlight>      // → button
<TextInput>               // → textbox
<Switch>                  // → checkbox
<FlatList>                // → list

// ❌ BAD (not semantic)
<View onPress={action}>   // → no role announced
<Text onPress={action}>   // → text, not button
```

### Proper Role Assignment

```javascript
// Buttons
<TouchableOpacity
  accessible={true}
  accessibilityRole="button"
  accessibilityLabel="Записаться на услугу"
>

// Links
<TouchableOpacity
  accessible={true}
  accessibilityRole="link"
  accessibilityLabel="Перейти к партнёрам"
>

// Headers
<Text
  accessible={true}
  accessibilityRole="header"
  accessibilityLevel={1}  // h1, h2, h3, etc
>
  Партнёры
</Text>

// Images
<Image
  source={photo}
  accessible={true}
  accessibilityRole="image"
  accessibilityLabel="Салон красоты Миндаль"
/>

// Forms
<View
  accessible={true}
  accessibilityRole="form"
>

// Lists
<FlatList
  accessible={true}
  accessibilityRole="list"
  data={items}
  renderItem={/* ... */}
/>
```

---

## 🏷️ ACCESSIBILITY LABELS

### Rule #2: EVERY INTERACTIVE ELEMENT NEEDS A LABEL

```javascript
// ❌ WRONG: No label
<TouchableOpacity onPress={favorite}>
  <HeartIcon />  ← What does this do? Screen reader has no idea
</TouchableOpacity>

// ✅ RIGHT: Clear label
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Добавить в избранное"
  accessibilityRole="button"
  onPress={favorite}
>
  <HeartIcon />
</TouchableOpacity>
```

### Label Guidelines

**Specificity:**
```
❌ "Button" (too generic)
❌ "" (empty, screen reader confused)
✅ "Добавить в избранное" (specific action)
✅ "Удалить бронирование" (clear intent)
```

**Length:**
```
❌ Too long: "Нажмите эту кнопку, чтобы добавить этого партнёра в ваш список избранного для быстрого доступа"
✅ Concise: "Добавить в избранное"
```

**Language:**
```
✅ Russian: "Записаться на услугу"
❌ English in Russian app: "Book service"
❌ Mixed: "Book Записаться"
```

### Images Need Alt Text

```javascript
// ❌ WRONG: No alternative text
<Image source={require('./partner-photo.jpg')} />

// ✅ GOOD: Descriptive label
<Image
  source={require('./partner-photo.jpg')}
  accessible={true}
  accessibilityRole="image"
  accessibilityLabel="Салон красоты Миндаль, интерьер с кресло и зеркалами"
/>

// ✅ ACCEPTABLE: Short description
<Image
  source={require('./partner-photo.jpg')}
  accessible={true}
  accessibilityRole="image"
  accessibilityLabel="Салон красоты Миндаль"
/>
```

### Form Fields Need Labels

```javascript
// ❌ WRONG: Placeholder only
<TextInput placeholder="Email" />

// ✅ RIGHT: Associated label + placeholder
<Text
  accessible={true}
  accessibilityRole="header"
>
  Email
</Text>
<TextInput
  accessible={true}
  accessibilityLabel="Email для входа"
  accessibilityRole="textbox"
  placeholder="example@email.com"
/>

// ✅ ALSO OK: aria-label alone if space is tight
<TextInput
  accessible={true}
  accessibilityLabel="Email для входа"
  placeholder="example@email.com"
/>
```

---

## 🔗 LINK TEXT

### Rule #3: LINKS MUST MAKE SENSE OUT OF CONTEXT

Screen reader users often jump between links. Link text must be clear without surrounding context.

```
❌ BAD: "Нажмите здесь", "Подробнее", "Читать дальше"
Screen reader user: "What am I reading more about? I'm lost"

✅ GOOD:
- "Читать политику конфиденциальности"
- "Узнать о Gold статусе"
- "Посмотреть все события"
Screen reader user: "I understand what each link does"
```

### Link Implementation

```javascript
// ❌ WRONG
<TouchableOpacity onPress={() => nav.navigate('Page')}>
  <Text>Подробнее</Text>
</TouchableOpacity>
// Announced: "Подробнее, button" (unclear)

// ✅ RIGHT
<TouchableOpacity
  accessible={true}
  accessibilityRole="link"
  accessibilityLabel="Узнать о Gold статусе"
  onPress={() => nav.navigate('StatusPage')}
>
  <Text>Подробнее</Text>  // Visual text can be shorter
</TouchableOpacity>
// Announced: "Узнать о Gold статусе, link"
```

---

## 📊 HEADING HIERARCHY

### Rule #4: HEADINGS MUST BE IN LOGICAL ORDER

Screen reader users navigate by headings. Hierarchy must be correct.

```javascript
// ❌ WRONG: Skipped h2, jumped to h3
<Text accessibilityRole="header" accessibilityLevel={1}>
  Партнёры  // h1
</Text>
<Text accessibilityRole="header" accessibilityLevel={3}>
  Салоны красоты  // h3 (skipped h2!)
</Text>

// ✅ RIGHT: Proper hierarchy
<Text accessibilityRole="header" accessibilityLevel={1}>
  Партнёры  // h1
</Text>
<Text accessibilityRole="header" accessibilityLevel={2}>
  Салоны красоты  // h2
</Text>
<Text accessibilityRole="header" accessibilityLevel={3}>
  Популярные салоны  // h3
</Text>
```

### Heading Best Practices

```
✅ DO:
- Start with h1 (page title)
- Use levels in order (h1 → h2 → h3)
- Use ONE h1 per page
- Use headings for structure, not styling

❌ DON'T:
- Skip levels (h1 → h3)
- Use multiple h1s
- Use headings for styling only
- Make headings too long
```

---

## ⚡ ARIA ATTRIBUTES (When Needed)

### Rule #5: ARIA IS LAST RESORT, NOT FIRST CHOICE

Use semantic components first. ARIA fills gaps only.

**ARIA Rule:** "No ARIA is better than bad ARIA"

### Important ARIA Attributes

```javascript
// aria-label: Custom label (use instead of visual text if needed)
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Добавить в избранное"  // ← aria-label equivalent
  onPress={favorite}
>
  <HeartIcon />  // Icon only, no visible text
</TouchableOpacity>

// aria-labelledby: Label from another element
<View>
  <Text nativeID="modal-title" accessibilityRole="header">
    Выберите время
  </Text>
  <Modal
    accessible={true}
    accessibilityLabelledBy="modal-title"  // ← References header above
    // Screen reader announces: "Выберите время, dialog"
  >
    {/* Content */}
  </Modal>
</View>

// aria-describedby: Additional description
<TextInput
  accessibilityLabel="Email"
  accessibilityDescribedBy="email-help"  // ← aria-describedby
/>
<Text nativeID="email-help">
  Используется для входа и восстановления пароля
</Text>

// aria-hidden: Hide from screen readers (decorative only)
<View
  accessible={false}  // ← aria-hidden equivalent
  accessibilityElementsHidden={true}
>
  <DecorationIcon />  // Just for visual decoration
</View>

// aria-live: Announce updates
<View
  accessible={true}
  accessibilityLiveRegion="polite"  // ← aria-live="polite"
  accessibilityLabel={`Ваш статус: ${status}`}
>
  <Text>{status}</Text>
</View>
// When status changes, screen reader announces: "Ваш статус: Gold"
```

---

## 📋 TESTING WITH SCREEN READERS

### iOS VoiceOver Testing

**Enable VoiceOver:**
```
Settings → Accessibility → VoiceOver → On
```

**Navigation:**
```
Swipe right:  Next element
Swipe left:   Previous element
Double tap:   Activate element
Two-finger Z: Go back/dismiss

Test process:
1. Start at top of screen
2. Swipe through each element
3. Verify announcements are:
   - Complete (label + role + hint if applicable)
   - Accurate (describes what user will get)
   - Non-redundant (doesn't repeat obviously)
4. Verify interactive elements announce role
5. Verify images have alt text
6. Verify headings are in order
```

### Android TalkBack Testing

**Enable TalkBack:**
```
Settings → Accessibility → TalkBack → On
```

**Navigation:**
```
Swipe right:      Next element
Swipe left:       Previous element
Double tap:       Activate element
Swipe up+right:   Read all from top
Swipe down:       Read from current

Test process:
1. Enable TalkBack
2. Swipe through screen
3. Verify all content is announced
4. Verify buttons announce role
5. Verify form fields have labels
6. Verify navigation is logical
```

---

## 🔥 COMMON MISTAKES

```
1. ❌ No accessibility labels
   <Button />
   Announced: "button" (unclear what it does)

2. ❌ Placeholder used as label
   <TextInput placeholder="Email" />
   Placeholder disappears when typing!

3. ❌ Images without alt text
   <Image source={photo} />

4. ❌ Link text is vague
   "Read more" without context

5. ❌ Wrong heading hierarchy
   h1 → h3 (skipped h2)

6. ❌ Non-semantic components
   <View onPress={action}>  (not announced as button)

7. ❌ Too much text in one label
   accessibilityLabel="This is a very long description..."

8. ❌ Using emojis in labels
   "❤️ Add to favorites"  (emoji pronounced)
```

---

## ✅ SVOY KRUG SPECIFIC EXAMPLES

### Partner Card

```javascript
<TouchableOpacity
  accessible={true}
  accessibilityRole="link"
  accessibilityLabel={`Салон ${partner.name}, ${partner.category}`}
  accessibilityHint={`${partner.rating} звёзд, ${partner.reviewCount} отзывов`}
  onPress={() => nav.navigate('PartnerDetail', { id: partner.id })}
>
  <Image
    source={{ uri: partner.photo }}
    accessible={true}
    accessibilityRole="image"
    accessibilityLabel={partner.name}
  />
  <Text>{partner.name}</Text>
  <Text>{partner.category}</Text>
</TouchableOpacity>

// VoiceOver announces:
// "Салон Миндаль, салон красоты, link, 4.8 звёзд, 127 отзывов"
```

### Booking Form

```javascript
<View accessible={true} accessibilityRole="form">
  <Text accessibilityRole="header" accessibilityLevel={1}>
    Выберите услугу
  </Text>

  {services.map(service => (
    <TouchableOpacity
      key={service.id}
      accessible={true}
      accessibilityRole="radio"
      accessibilityLabel={service.name}
      accessibilityState={{ checked: selected === service.id }}
      onPress={() => setSelected(service.id)}
    >
      <Text>{service.name}</Text>
      <Text>{service.price}₽</Text>
    </TouchableOpacity>
  ))}

  <TouchableOpacity
    accessible={true}
    accessibilityRole="button"
    accessibilityLabel="Продолжить к выбору времени"
    onPress={next}
  >
    <Text>Далее</Text>
  </TouchableOpacity>
</View>
```

---

## ✅ SCREEN READER CHECKLIST

Before launch:

- [ ] All interactive elements have clear labels
- [ ] All images have alt text
- [ ] Form fields have associated labels
- [ ] Link text makes sense out of context
- [ ] Headings in logical order
- [ ] No empty states confusing to screen readers
- [ ] Dynamic content announces updates
- [ ] Tested with VoiceOver (iOS)
- [ ] Tested with TalkBack (Android)

---

**Screen readers reveal structure. Make it meaningful.** 🔊

