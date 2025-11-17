# ACCESSIBILITY TESTING
## Checklist, Tools, and Process

**Version:** 2.0
**Last Updated:** November 2025
**Scope:** React Native (iOS/Android)
**Goal:** WCAG 2.1 Level AA Compliance

---

## 🧪 TESTING METHODS

### 1. Automated Testing (~40% of issues)

Uses tools to scan for common a11y problems.

**Pros:** Fast, consistent, catches obvious issues
**Cons:** Misses context issues, can't test everything

**Tools:**
- axe DevTools (browser, ~40% coverage)
- Lighthouse (Chrome, accessibility score)
- WAVE (visual overlay, good for beginners)

**Limitations:**
- Can't evaluate link text quality
- Can't check focus order
- Can't test keyboard interaction
- Can't evaluate alt text quality

### 2. Manual Testing (Essential!)

Real person using real device with accessibility features.

**Pros:** Catches context issues, real-world usage
**Cons:** Slower, requires training

**Methods:**
- Keyboard navigation testing
- Screen reader testing (VoiceOver/TalkBack)
- Color contrast verification
- Zoom testing (200%)

### 3. User Testing (Gold Standard)

Real users with disabilities testing your product.

**Pros:** Catches real-world issues, provides feedback
**Cons:** Expensive, time-consuming

**When:** Post-MVP or when budget allows

---

## 📋 TESTING CHECKLIST

### Pre-Development

Before implementing a feature:

- [ ] **Plan accessibility:** Consider how disabled users will interact
- [ ] **Design with a11y:** Use proper colors, contrast, labels
- [ ] **Document requirements:** What a11y features does this need?

### Development Checklist

While implementing:

- [ ] **Use semantic components:** Button, TextInput, etc
- [ ] **Add accessibility labels:** accessibilityLabel prop
- [ ] **Add accessibility roles:** accessibilityRole prop
- [ ] **Manage focus:** onAccessibilityFocus handlers
- [ ] **Test locally:** Enable screen reader on device
- [ ] **Run automated tools:** Quick sanity check

### Pre-Launch Checklist

Before releasing:

**Automated:**
- [ ] Run axe DevTools (0 critical/serious errors)
- [ ] Run Lighthouse (accessibility score ≥ 90)

**Keyboard:**
- [ ] Tab through entire flow
- [ ] All elements focusable
- [ ] Focus visible on all elements
- [ ] No keyboard traps
- [ ] Tab order logical

**Screen Readers:**
- [ ] Test with VoiceOver (iOS)
- [ ] Test with TalkBack (Android)
- [ ] All content announced
- [ ] Labels clear and specific
- [ ] Headings in order

**Visual:**
- [ ] Contrast: 4.5:1 for text, 3:1 for UI
- [ ] Tested with Color Oracle (color blindness)
- [ ] Zoom to 200% (readable?)
- [ ] Focus indicators visible

**Forms:**
- [ ] All fields have labels
- [ ] Error messages clear & specific
- [ ] Helper text present
- [ ] Required fields marked

**Content:**
- [ ] Images have alt text
- [ ] Links descriptive
- [ ] Language clear & simple
- [ ] No jargon

---

## 🔧 TESTING TOOLS SETUP

### iOS Testing (VoiceOver)

```
Enable VoiceOver:
1. iPhone Settings
2. Accessibility → VoiceOver
3. Toggle ON
4. Open your app

Basic Gestures:
- Single tap: Select
- Double tap: Activate
- Swipe right: Next element
- Swipe left: Previous element
- Two-finger Z: Go back
- Two-finger Z (swipe up): Read all from top

Reading your app:
1. Start at top
2. Swipe through all elements
3. Note what's announced
4. Verify it's clear & complete

Testing focus:
1. Enable VoiceOver
2. Swipe through each interactive element
3. Double-tap to activate
4. Verify it works
```

### Android Testing (TalkBack)

```
Enable TalkBack:
1. Android Settings
2. Accessibility → TalkBack
3. Toggle ON
4. Open your app

Basic Gestures:
- Single tap: Select
- Double tap: Activate
- Swipe right: Next element
- Swipe left: Previous element
- Swipe up+right: Read all from top
- Swipe down: Read current

Testing voice output:
1. Enable TalkBack
2. Navigate through screen
3. Verify all content announced
4. Verify announcements clear
```

### Contrast Testing

```
WebAIM Contrast Checker:
1. Go to webaim.org/resources/contrastchecker
2. Enter foreground color (text)
3. Enter background color
4. Check result (target 4.5:1+)
5. Document results

Color Blindness Testing:
1. Install Color Oracle (free)
2. Open design file
3. Run Color Oracle
4. View as protanopia, deuteranopia, tritanopia
5. Verify still distinguishable without color alone
```

---

## 🎯 TESTING BY FEATURE

### Forms

```
✅ DO:
- Test all form fields with keyboard (Tab to each)
- Test form submission with Enter key
- Enable error messages and verify clarity
- Test error state styling has sufficient contrast
- Test helper text is clear

CHECKLIST:
- [ ] All inputs focusable
- [ ] Tab order matches visual order
- [ ] Error messages clear (not color alone)
- [ ] Helper text present and clear
- [ ] Required field indication clear
- [ ] Form submits with keyboard (Enter)
```

### Navigation

```
✅ DO:
- Test tab order throughout entire app
- Verify focus moves logically
- Check focus indicator visible at all times
- Test back/exit mechanisms
- Test skip links (if applicable)

CHECKLIST:
- [ ] Tab order top → bottom, left → right
- [ ] All interactive elements reachable
- [ ] Focus indicator visible
- [ ] Can escape any modal or overlay
- [ ] Focus returns to trigger after closing
```

### Images

```
✅ DO:
- Add meaningful alt text
- Test with VoiceOver/TalkBack
- Verify alt text describes image
- Check for decorative images (hidden)

CHECKLIST:
- [ ] All images have accessibilityLabel
- [ ] Alt text is descriptive
- [ ] Decorative images marked accessible={false}
- [ ] Image announcements tested
```

### Buttons

```
✅ DO:
- Test button announces role
- Verify label is clear
- Test activation with Enter/Space (keyboard)
- Test visual focus indicator

CHECKLIST:
- [ ] Button announces as "button"
- [ ] Label describes action
- [ ] Focusable (accessible={true})
- [ ] Focus indicator visible
- [ ] Activates with keyboard
```

---

## 🚀 TESTING WORKFLOWS

### Workflow 1: Keyboard Navigation Testing

```
1. Device: iPhone or Android
2. Feature: Booking flow
3. Method: Tab through without using mouse

Steps:
1. Open app
2. Press Tab (next element)
3. Press Shift+Tab (previous element)
4. Verify focus indicator visible
5. Press Enter to activate
6. Repeat for entire flow
7. Document any issues

Issues to watch for:
- Can't reach element (not focusable)
- Focus disappears
- Can't escape (keyboard trap)
- Focus order wrong
- Focus indicator invisible
```

### Workflow 2: Screen Reader Testing

```
1. Device: iPhone (VoiceOver) or Android (TalkBack)
2. Feature: Partner card
3. Method: Swipe through with screen reader

Steps:
1. Enable VoiceOver/TalkBack
2. Swipe right to next element
3. Listen to announcement
4. Swipe again
5. Repeat through entire card
6. Note any missing information

Example announcement should be:
"Салон Миндаль, салон красоты, link, 4.8 звёзд, 127 отзывов"

Issues to watch for:
- No announcement (not accessible)
- Vague announcement ("Button" instead of specific action)
- Missing information (no rating mentioned)
- Confusing order of announcements
```

### Workflow 3: Contrast Verification

```
1. Colors: All text colors in design
2. Tool: WebAIM Contrast Checker
3. Method: Test each combination

Steps:
1. Identify all text colors
2. Identify all background colors
3. Test each combination
4. Document results
5. Fix any below 4.5:1

Example:
- Gray-700 text on White background: 8.9:1 ✅ (pass)
- Gray-500 text on White background: 4.6:1 ✅ (pass)
- Gray-400 text on White background: 2.9:1 ❌ (fail - fix!)
```

---

## 📊 TESTING REPORT TEMPLATE

```markdown
# Accessibility Testing Report
**Date:** 2025-11-17
**Feature:** Booking Flow
**Tester:** [Name]
**Status:** Ready for Launch / Needs Fixes

## Automated Testing
- axe DevTools: 0 errors ✅
- Lighthouse Accessibility: 95/100 ✅

## Keyboard Navigation
- [✅] All elements focusable
- [✅] Tab order logical
- [✅] Focus indicator visible
- [✅] No keyboard traps
- [✅] Escape closes modals

## Screen Readers
- [✅] VoiceOver tested (iOS)
- [✅] TalkBack tested (Android)
- [✅] All content announced
- [✅] Labels clear

## Visual
- [✅] Contrast: 4.5:1+ for text
- [✅] Focus indicators visible
- [✅] Color blindness tested
- [✅] Zoom 200% readable

## Issues Found
1. Error message text too light (Gray-400) - FIX: Use Gray-600
2. Form submit button not announcing role - FIX: Add accessibilityRole="button"

## Recommendation
✅ Ready for launch (after fixes applied)
```

---

## 🔥 COMMON TESTING MISTAKES

```
1. ❌ Testing only in simulator
   Real devices behave differently!
   DO: Test on actual iOS/Android devices

2. ❌ Testing only on one device type
   iOS and Android have different a11y implementations
   DO: Test on both iPhone and Android

3. ❌ Not actually enabling screen readers
   "I know what it should announce"
   DO: Enable VoiceOver/TalkBack and listen

4. ❌ Assuming keyboard = working
   Keyboard navigation is complex
   DO: Manually tab through every interaction

5. ❌ Not testing with real users
   Your app might work differently for disabled users
   DO: Get feedback from people with disabilities

6. ❌ Testing only happy path
   What about errors? Empty states? Disabled buttons?
   DO: Test all states and error conditions

7. ❌ Ignoring contrast issues as "design aesthetic"
   Low contrast is inaccessible
   DO: Fix contrast issues or redesign
```

---

## 📱 TESTING EACH COMPONENT

### Button

```javascript
// Test procedure:
// 1. Enable VoiceOver
// 2. Swipe to button
// 3. Verify announcement includes "button"
// 4. Double-tap to activate
// 5. Verify action happens

// Before testing:
<TouchableOpacity>
  <Text>Click</Text>
</TouchableOpacity>
// Screen reader: "Click, text" ❌ (not announced as button)

// After testing:
<TouchableOpacity
  accessible={true}
  accessibilityRole="button"
  accessibilityLabel="Записаться на услугу"
>
  <Text>Click</Text>
</TouchableOpacity>
// Screen reader: "Записаться на услугу, button" ✅
```

### Form

```javascript
// Test procedure:
// 1. Tab to each field
// 2. Verify label announced
// 3. Type in field
// 4. Verify helper text clear
// 5. Submit form
// 6. Verify error handling

// Checklist:
// [ ] Email field labeled
// [ ] Password field labeled
// [ ] Helper text announced
// [ ] Error message clear
// [ ] Submit button works with keyboard
```

### Modal

```javascript
// Test procedure:
// 1. Open modal with keyboard (Tab to trigger, press Enter)
// 2. Verify focus moves to modal
// 3. Tab through modal content
// 4. Press Escape (should close)
// 5. Verify focus returns to trigger

// Checklist:
// [ ] Modal receives focus when opened
// [ ] Focus trapped in modal (can't tab out)
// [ ] Can close with Escape key
// [ ] Focus returns to trigger
// [ ] Modal title announced (aria-labelledby)
```

---

## ✅ TESTING CHECKLIST (FINAL)

### Before Each Code Review

- [ ] Manually tested with keyboard
- [ ] Ran axe DevTools
- [ ] VoiceOver/TalkBack tested
- [ ] Contrast verified
- [ ] No console errors

### Before Each Release

- [ ] All above completed
- [ ] Full feature flow tested
- [ ] Tested on multiple devices
- [ ] Tested on multiple iOS versions
- [ ] Tested on multiple Android versions
- [ ] Accessibility report written
- [ ] Issues documented and tracked
- [ ] Team aware of any limitations

### Ongoing

- [ ] Accessibility audit every 6 months
- [ ] New features tested before merge
- [ ] User feedback integrated
- [ ] Team training updated
- [ ] Tools/process improved

---

## 📞 WHEN TO ESCALATE

```
CRITICAL (Fix immediately):
- Cannot access via keyboard
- Screen reader can't announce
- Contrast below 3:1
- Modal keyboard traps

HIGH (Fix soon):
- Poor focus indicators
- Illogical tab order
- Missing labels
- Contrast 3:1-4.4:1

MEDIUM (Fix when possible):
- Link text not descriptive
- Heading hierarchy wrong
- Error messages could be clearer
```

---

**Test early, test often. Fix what you find.** 🧪

