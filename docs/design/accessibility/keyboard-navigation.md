# KEYBOARD NAVIGATION
## Tab Order, Focus Management, Keyboard Shortcuts

**Version:** 2.0
**Last Updated:** November 2025
**WCAG Criteria:** 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.4.3 Focus Order, 2.4.7 Focus Visible
**Platform:** React Native (iOS/Android)

---

## ⌨️ WHY KEYBOARD NAVIGATION?

**All users depend on keyboard navigation:**

- Users with motor disabilities (tremors, arthritis, palsy)
- Blind users using screen readers + keyboard
- Power users who prefer keyboard (faster than mouse)
- Temporary limitations (broken arm, mouse unavailable)
- Mobile users where "keyboard" is the touch interface

**Guideline:** If it's clickable, it must be keyboard accessible.

---

## 🎯 CORE REQUIREMENT

**All functionality must be available via keyboard only.**

Test: Hide the mouse/trackpad. Can you use the entire app?

---

## 📱 KEYBOARD IN REACT NATIVE

React Native maps to native mobile accessibility:

### iOS (Virtual Keyboard)

```
Tab:       Move focus to next element
Shift+Tab: Move focus to previous element
Space:     Activate buttons, toggle switches
Enter:     Activate links, submit forms
Escape:    Close modals, dismiss menus
```

### Android (Virtual Keyboard)

```
Tab:       Move focus to next element
Shift+Tab: Move focus to previous element
Space:     Activate buttons, toggle switches
Enter:     Activate links, submit forms
Back:      Close modals, navigate back
```

**Reality:** Most mobile keyboard is NOT external keyboard, but native touch interface with accessibility adjustments.

### What "Keyboard Navigation" Really Means

In React Native mobile context:
- Focus can be moved via native accessibility APIs
- VoiceOver (iOS) users navigate with swipes + taps
- TalkBack (Android) users navigate with swipes + taps
- Keyboard logic is built into platform APIs

**Our job:** Implement accessibility properties correctly.

---

## 🔑 REACT NATIVE ACCESSIBILITY PROPERTIES

### 1. Make Component Focusable

```javascript
<TouchableOpacity
  accessible={true}  // ← Enable accessibility
  accessibilityRole="button"
  onPress={handlePress}
>
  <Text>Записаться</Text>
</TouchableOpacity>
```

**Which components are focusable by default:**
- ✅ TouchableOpacity, TouchableHighlight
- ✅ TextInput
- ✅ Switch
- ✅ Image (with onPress)
- ❌ View (needs accessible={true})
- ❌ Text (unless interactive)

### 2. Define Accessibility Role

```javascript
// Button
<TouchableOpacity
  accessible={true}
  accessibilityRole="button"
  onPress={handlePress}
>

// Link
<TouchableOpacity
  accessible={true}
  accessibilityRole="link"
  onPress={() => navigation.navigate('Page')}
>

// Header/Heading
<Text
  accessible={true}
  accessibilityRole="header"
  accessibilityLevel={1}  // h1, h2, h3...
>
  Партнёры
</Text>

// Image
<Image
  source={require('./partner.jpg')}
  accessible={true}
  accessibilityRole="image"
  accessibilityLabel="Салон красоты Миндаль"
/>

// Form input
<TextInput
  accessible={true}
  accessibilityRole="textbox"
  accessibilityLabel="Email"
/>

// Checkbox/Toggle
<Switch
  accessible={true}
  accessibilityRole="checkbox"
  accessibilityHint="Получать уведомления"
/>
```

### 3. Provide Accessible Label

```javascript
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Записаться на услугу"
  // Screen reader announces: "Записаться на услугу, button"
  onPress={bookService}
>
  <Text>Записаться</Text>
</TouchableOpacity>
```

**Label examples:**
```
❌ "Button" (too vague)
❌ Empty (screen reader can't announce)
✅ "Записаться на услугу" (specific action)
✅ "Добавить в избранное" (clear intent)
✅ "Удалить бронирование" (specific action)
```

### 4. Add Helpful Hints

```javascript
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Статус участницы"
  accessibilityHint="Нажмите, чтобы узнать как повысить статус"
  onPress={showStatusInfo}
>
  <Text>Gold Member</Text>
</TouchableOpacity>

// Screen reader announces:
// "Gold Member, button, Статус участницы, Нажмите, чтобы узнать как повысить статус"
```

### 5. Manage Focus Explicitly

```javascript
// For modals/overlays
const modalRef = useRef();

const openModal = () => {
  setModalOpen(true);
  // Give modal focus
  AccessibilityInfo.setAccessibilityFocus(
    findNodeHandle(modalRef.current)
  );
};

const closeModal = () => {
  setModalOpen(false);
  // Return focus to trigger button
  AccessibilityInfo.setAccessibilityFocus(
    findNodeHandle(triggerRef.current)
  );
};

<View ref={modalRef}>
  {/* Modal content */}
</View>
```

### 6. Announce Dynamic Updates

```javascript
<View
  accessible={true}
  accessibilityLiveRegion="polite"
  accessibilityLabel={`Ваш статус: ${userStatus}`}
>
  <Text>{userStatus}</Text>
</View>

// When status changes, screen reader announces the new value
// "Ваш статус: Gold"
```

---

## 🔄 TAB ORDER (FOCUS ORDER)

### Natural Tab Order (Preferred)

Let the DOM order dictate tab order:

```javascript
// ✅ GOOD: Natural order matches visual layout
<View>
  <Text>Выберите время</Text>
  <TouchableOpacity>
    <Text>14:00</Text>
  </TouchableOpacity>
  <TouchableOpacity>
    <Text>15:30</Text>
  </TouchableOpacity>
  <TouchableOpacity>
    <Text>16:45</Text>
  </TouchableOpacity>
  <TouchableOpacity>
    <Text>Записаться</Text>
  </TouchableOpacity>
</View>

// Tab order: 14:00 → 15:30 → 16:45 → Записаться
```

### When Order Doesn't Match Visual Layout

```javascript
// ❌ PROBLEM: CSS repositioning makes order confusing
<View>
  <TouchableOpacity style={{ position: 'absolute', right: 0 }}>
    {/* Visually on right but comes first in tab order */}
  </TouchableOpacity>
  <TouchableOpacity>
    {/* Visually on left but comes second in tab order */}
  </TouchableOpacity>
</View>

// ✅ SOLUTION: Fix the DOM order (rearrange elements)
<View>
  <TouchableOpacity>
    {/* Visually on left, tab order first */}
  </TouchableOpacity>
  <TouchableOpacity style={{ position: 'absolute', right: 0 }}>
    {/* Visually on right, tab order second */}
  </TouchableOpacity>
</View>
```

### Don't Use accessibilityRole to Override Order

```javascript
// ❌ WRONG: Trying to change tab order with props
<TouchableOpacity
  accessibilityIndex={5}  // ← This doesn't exist in React Native!
  onPress={action}
>

// React Native doesn't support manual tab index manipulation
// The platform handles accessibility order differently
```

---

## 🎯 FOCUS INDICATORS

### Visible Focus (CRITICAL)

Users must be able to see which element has focus:

```javascript
// ✅ GOOD: Visible focus indicator
const [isFocused, setIsFocused] = useState(false);

<TouchableOpacity
  accessible={true}
  style={[
    styles.button,
    isFocused && styles.buttonFocused  // ← Highlight when focused
  ]}
  onAccessibilityFocus={() => setIsFocused(true)}
  onAccessibilityBlur={() => setIsFocused(false)}
  onPress={handlePress}
>
  <Text>Записаться</Text>
</TouchableOpacity>

// Styles
const styles = StyleSheet.create({
  button: {
    padding: 12,
    borderRadius: 8,
    backgroundColor: colors.primary,
  },
  buttonFocused: {
    backgroundColor: colors.primary,
    borderWidth: 3,
    borderColor: colors.focusOutline,  // High contrast
    opacity: 0.9,
  },
});
```

### What Makes Focus Visible

```
✅ Good indicators:
- 2-3px border around element (high contrast color)
- Background color change
- Scale transformation
- Outline with 2px+ width
- Color contrast: 3:1 minimum

❌ Bad indicators:
- No visible change
- Very subtle (opacity 0.1)
- Same color as background
- Too thin (< 2px)
- Low contrast with surrounding elements
```

### Testing Focus Visibility

```
Test on different backgrounds:
1. Light background → dark focus indicator
2. Dark background → light focus indicator
3. Colored background → high contrast indicator

Test for visibility:
- Is it at least 2px thick?
- Is it distinct from surrounding elements?
- Can you see it from 1 meter away?
- Would color blind users see it?
```

---

## 🏁 FOCUS MANAGEMENT IN MODALS/OVERLAYS

### Pattern: Focus Trap

When a modal opens, focus should:
1. Move to modal
2. Stay within modal (trap)
3. Return to trigger button when closing

```javascript
const BookingModal = ({ isOpen, onClose, triggerRef }) => {
  const modalRef = useRef();
  const closeButtonRef = useRef();

  useEffect(() => {
    if (isOpen) {
      // Move focus to modal when it opens
      setTimeout(() => {
        AccessibilityInfo.setAccessibilityFocus(
          findNodeHandle(closeButtonRef.current)
        );
      }, 100);
    } else {
      // Return focus to trigger when modal closes
      AccessibilityInfo.setAccessibilityFocus(
        findNodeHandle(triggerRef.current)
      );
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <Modal
      accessible={true}
      accessibilityRole="dialog"
      accessibilityLabel="Выберите время для бронирования"
    >
      <View ref={modalRef}>
        {/* Modal content - naturally focusable elements */}
        <TouchableOpacity
          ref={closeButtonRef}
          onPress={onClose}
          accessible={true}
          accessibilityRole="button"
          accessibilityLabel="Закрыть"
        >
          <Text>Закрыть</Text>
        </TouchableOpacity>

        {/* Time slots */}
        <TimeSlotList />

        {/* Book button */}
        <TouchableOpacity
          onPress={confirmBooking}
          accessible={true}
          accessibilityRole="button"
        >
          <Text>Подтвердить</Text>
        </TouchableOpacity>
      </View>
    </Modal>
  );
};
```

---

## 📋 KEYBOARD ACCESSIBILITY CHECKLIST

### Development Checklist

Before submitting code:

- [ ] All interactive elements are focusable (button, link, input, etc)
- [ ] Non-interactive elements aren't focusable (View, Text)
- [ ] Tab order matches visual order (top → bottom, left → right)
- [ ] Focus indicator is clearly visible on all elements
- [ ] Focus indicator works on light AND dark backgrounds
- [ ] No keyboard traps (users can navigate out)
- [ ] Modal focus management implemented
- [ ] Escape closes modals (if applicable)
- [ ] Enter submits forms
- [ ] Space activates buttons

### Testing Checklist

Before launch:

- [ ] Test entire flow with keyboard only
- [ ] Test on iPhone with Accessibility keyboard
- [ ] Test on Android with keyboard navigation
- [ ] Verify focus order is logical
- [ ] Verify focus indicators are visible
- [ ] Test on different iOS/Android versions
- [ ] Test with VoiceOver (iOS)
- [ ] Test with TalkBack (Android)

---

## 🚀 COMMON PATTERNS IN SVOY KRUG

### Booking Flow Keyboard Navigation

```
1. Partners List Screen:
   - Partner card 1 [Focus indicator: border]
   - Partner card 2 [Focus indicator: border]
   - Partner card 3 [Focus indicator: border]
   - "Show more" button
   Tab order: Card 1 → Card 2 → Card 3 → Show more

2. Click Partner → Booking Modal Opens:
   - Modal receives focus
   - "Select time" heading
   - Time slot 14:00 [First in tab order]
   - Time slot 15:30
   - Time slot 16:45
   - "Book" button
   - "Cancel" button [Can press to close]
   Tab trapped in modal

3. Click "Book" → Success Modal:
   - Success message announced
   - "Close" button [Receives focus]
   - Returns to Partners List when closed
```

### Form Keyboard Navigation

```
<View accessible={true} accessibilityRole="form">
  {/* Email field */}
  <Text accessibilityRole="header">Email</Text>
  <TextInput
    accessible={true}
    accessibilityLabel="Email для входа"
    placeholder="example@email.com"
    onChangeText={setEmail}
  />

  {/* Password field */}
  <Text accessibilityRole="header">Пароль</Text>
  <TextInput
    accessible={true}
    accessibilityLabel="Пароль"
    secureTextEntry={true}
    onChangeText={setPassword}
  />

  {/* Submit button */}
  <TouchableOpacity
    accessible={true}
    accessibilityLabel="Войти"
    accessibilityRole="button"
    onPress={handleSubmit}
  >
    <Text>Войти</Text>
  </TouchableOpacity>
</View>

// Tab order: Email → Password → Login
```

---

## ❌ COMMON MISTAKES

```
1. ❌ Making View clickable instead of Button
   <View onPress={action}>  // Not focusable!

2. ❌ Using onPress on non-interactive elements
   <Text onPress={action}>  // Should be TouchableOpacity

3. ❌ Forgetting accessible={true} on custom components
   <CustomButton />  // Not announced properly

4. ❌ No focus indicator
   <TouchableOpacity onPress={action}>  // Can't see focus

5. ❌ Focus hidden by styling
   border: none; outline: none;  // Removes platform focus

6. ❌ Focus order doesn't match visual order
   CSS repositioning without matching DOM order

7. ❌ Keyboard traps
   Modal without way to escape

8. ❌ Not returning focus after action
   Close modal, focus lost
```

---

## 📱 TESTING WITH NATIVE ACCESSIBILITY

### iOS VoiceOver Navigation

```
Enable VoiceOver:
1. Settings > Accessibility > VoiceOver > On
2. Use on-screen rotors or gestures

Gestures:
- Swipe right: Next element
- Swipe left: Previous element
- Two-finger Z: Dismiss/Go back
- Double tap: Activate
- Swipe up+right: Read all from top
- Swipe down: Read all from current

Test: Navigate to each button with VoiceOver
Verify: Announcement includes label + role
```

### Android TalkBack Navigation

```
Enable TalkBack:
1. Settings > Accessibility > TalkBack > On
2. Use gestures or hardware keys

Gestures:
- Swipe right: Next element
- Swipe left: Previous element
- Swipe up+right: Read all from top
- Double tap: Activate
- Back button: Go back

Test: Navigate to each button with TalkBack
Verify: Announcement is clear and specific
```

---

## 🎯 ACCESSIBILITY PROPERTIES QUICK REFERENCE

```javascript
// Complete accessible button
<TouchableOpacity
  accessible={true}                           // Enable a11y
  accessibilityRole="button"                  // Define role
  accessibilityLabel="Записаться на услугу"  // What it does
  accessibilityHint="Открывает форму бронирования"  // Extra context
  accessibilityState={{
    disabled: !isAvailable,                   // Current state
    checked: isSelected,
  }}
  onAccessibilityFocus={() => setFocused(true)}
  onAccessibilityBlur={() => setFocused(false)}
  style={isFocused && styles.focused}
  onPress={handlePress}
>
  <Text>Записаться</Text>
</TouchableOpacity>
```

---

## ✅ DO'S

- ✅ Use semantic components (Button, Link, etc)
- ✅ Make focus order match visual layout
- ✅ Make focus clearly visible
- ✅ Provide descriptive accessibility labels
- ✅ Test with native screen readers
- ✅ Trap focus in modals
- ✅ Return focus after action
- ✅ Test on real devices

---

## ❌ DON'Ts

- ❌ Don't use View for buttons
- ❌ Don't hide focus indicator
- ❌ Don't make focus hard to see
- ❌ Don't create keyboard traps
- ❌ Don't assume iOS/Android work the same
- ❌ Don't test only in simulator
- ❌ Don't forget accessibility labels
- ❌ Don't remove focus indicators for "cleaner" design

---

**If it's interactive, it must be keyboard accessible.** ⌨️

