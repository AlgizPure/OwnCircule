# ACCESSIBILITY OVERVIEW
## WCAG 2.1 Level AA Compliance & Current State

**Version:** 2.0
**Last Updated:** November 2025
**Status:** In Progress (Pre-MVP Phase)
**Target Compliance:** WCAG 2.1 Level AA
**Platform:** React Native (Mobile-first)

---

## 🎯 WHY ACCESSIBILITY MATTERS

**Accessibility is not optional. It's essential.**

- **15% of the global population** has disabilities
- **Legal requirement** in many jurisdictions (GDPR, ADA, AODA)
- **Better UX for everyone** (benefits all users, not just disabled)
- **Business case**: Accessible apps are easier to use, more inclusive, and reach wider audiences
- **Ethical responsibility**: Our users deserve the same access

### Impact at OwnCircule

Women 30-50, especially premium service consumers, may have:
- Low vision (presbyopia, macular degeneration)
- Motor disabilities (tremors, arthritis)
- Hearing impairments
- Cognitive disabilities (dyslexia, ADHD)
- Temporary limitations (broken arm, eye surgery recovery)

---

## 📋 WCAG 2.1 OVERVIEW

### What is WCAG?

**Web Content Accessibility Guidelines (WCAG)** are international standards developed by the W3C to make digital content accessible.

Latest version: **WCAG 2.1** (2018)
Replacement coming: WCAG 3.0 (draft)

### Compliance Levels

| Level | Name | Requirement | Target |
|-------|------|------------|--------|
| **A** | Minimum | Basic accessibility | Baseline (rare) |
| **AA** | Recommended | Good accessibility for most people | **OUR TARGET** ⭐ |
| **AAA** | Enhanced | Exceptional accessibility | Nice to have (expensive) |

**Our goal: WCAG 2.1 Level AA compliance**

This ensures usability for most users with disabilities while being practical to implement.

---

## 🏗️ FOUR CORE PRINCIPLES (POUR)

All WCAG guidelines are built on these four pillars:

### 1. PERCEIVABLE
**Users can see/hear the content**

```
Content must be presented in ways users can perceive it.
This includes providing alternatives for non-text content.
```

**Key requirements:**
- ✅ Text alternatives for images (alt text)
- ✅ Captions and transcripts for videos
- ✅ Sufficient color contrast (4.5:1 for normal text)
- ✅ Don't rely on color alone to convey meaning
- ✅ Resizable text (no fixed sizes)
- ✅ No flashing that could cause seizures

**OwnCircule context:**
- All partner images have descriptive alt text
- Event descriptions have captions
- Color + icons/patterns for status indicators
- Text sizes meet 1.2x zoom without loss of functionality

---

### 2. OPERABLE
**Users can navigate and use the interface**

```
All functionality must be available via keyboard.
No mouse required, no time limits.
```

**Key requirements:**
- ✅ All functionality accessible via keyboard
- ✅ Enough time to complete tasks (no auto-timeouts)
- ✅ Logical tab order (top-to-bottom, left-to-right)
- ✅ Visible focus indicators (must be obvious)
- ✅ No keyboard traps (users can get out)
- ✅ Skip links to bypass repetitive navigation
- ✅ No seizure-inducing content (no flashing >3x/second)

**OwnCircule context:**
- All bookings possible via keyboard
- No session timeout during active use
- Native tab order follows visual layout
- Focus indicators clearly visible (outline + color)
- Booking flow has predictable navigation
- No autoplay of videos with sound

---

### 3. UNDERSTANDABLE
**Users can understand content and how to use it**

```
Information must be presented clearly.
Interface behavior must be predictable.
```

**Key requirements:**
- ✅ Readable language (simple vocabulary, short sentences)
- ✅ Predictable navigation (consistent patterns)
- ✅ Input assistance (hints, error messages, validation)
- ✅ Clear labels for form fields
- ✅ Descriptive link text ("Read more" vs "Click here")
- ✅ Consistent terminology
- ✅ Logical heading hierarchy

**OwnCircule context:**
- Russian language uses formal "Вы" for respect
- Clear, concise microcopy
- Form fields have associated labels (not placeholders only)
- Error messages explain what went wrong and how to fix it
- Booking flow has consistent navigation patterns
- Headings follow logical structure

---

### 4. ROBUST
**Works with assistive technologies**

```
Content must be compatible with current and future
assistive technologies (screen readers, magnifiers, etc).
```

**Key requirements:**
- ✅ Valid, semantic HTML structure
- ✅ Proper use of ARIA attributes
- ✅ Correct heading hierarchy
- ✅ Form fields associated with labels
- ✅ Sufficient color contrast
- ✅ Functional without JavaScript (graceful degradation)

**OwnCircule context:**
- React Native components follow platform accessibility APIs
- VoiceOver (iOS) and TalkBack (Android) supported
- Semantic component usage (buttons, forms, etc)
- ARIA labels where needed (but semantic HTML first)
- Works on latest iOS/Android versions

---

## 📊 CURRENT COMPLIANCE STATE

### Pre-MVP Accessibility Assessment

**Stage:** Pre-MVP / Bootstrap Phase
**Status:** Foundation in place, improvements needed

#### What's Good

- ✅ Using React Native (has good a11y foundations)
- ✅ Planning for keyboard navigation early
- ✅ Considering screen reader support
- ✅ Documentation in place (this file!)
- ✅ Team awareness of a11y importance

#### What Needs Work

- ⚠️ No comprehensive automated testing yet
- ⚠️ Limited manual screen reader testing
- ⚠️ Contrast ratios need verification
- ⚠️ Focus management in modals needs implementation
- ⚠️ ARIA labels pending implementation
- ⚠️ Error message improvements needed

#### What's Not Started

- ❌ User testing with people with disabilities
- ❌ CI/CD accessibility testing pipeline
- ❌ Detailed audit of all components
- ❌ Android TalkBack specific testing

---

## ✅ QUICK WINS (Easy, High Impact)

These require minimal effort but solve major accessibility issues:

### 1. Use Semantic HTML

```
WRONG:
<div onClick={handleClick}>Click me</div>

RIGHT:
<button onPress={handleClick}>Click me</button>
```

**Impact:** Buttons work with screen readers, keyboard navigation

### 2. Add Alt Text

```
WRONG:
<Image source={partnerPhoto} />

RIGHT:
<Image
  source={partnerPhoto}
  accessible={true}
  accessibilityLabel="Салон красоты 'Миндаль', интерьер"
/>
```

**Impact:** Screen reader users understand images

### 3. Label Form Fields

```
WRONG:
<TextInput placeholder="Email" />

RIGHT:
<Text accessibilityRole="header">Email</Text>
<TextInput
  accessibilityLabel="Email"
  accessible={true}
  placeholder="example@email.com"
/>
```

**Impact:** Users know what field is what

### 4. Show Focus

```css
/* React Native */
<TouchableOpacity style={[
  styles.button,
  focused && styles.buttonFocused
]}>
```

**Impact:** Keyboard users see where they are

### 5. Sufficient Contrast

```
CHECK: Text color vs background color
MINIMUM: 4.5:1 ratio for normal text
TOOL: WebAIM Contrast Checker
```

**Impact:** Low vision users can read

---

## 🔧 ACCESSIBILITY TESTING TOOLS

### Automated Tools

| Tool | Platform | Purpose | Limitations |
|------|----------|---------|-------------|
| **axe DevTools** | Browser | General a11y audit | ~40% coverage |
| **Lighthouse** | Chrome | Performance + a11y | Quick but shallow |
| **WAVE** | Web/Browser | Visual overlay | Good for beginners |
| **Contrast Checkers** | Online | Color contrast verification | Specific use case |

### Manual Testing

| Method | Why It Matters | Effort |
|--------|---------------|--------|
| **Keyboard navigation** | Detects keyboard traps, focus issues | Low |
| **Screen reader testing** | Validates announcements, structure | Medium |
| **Color blindness test** | Checks contrast + color usage | Low |
| **Zoom testing** | Text readability at 200% | Low |
| **User testing** | Real-world usage patterns | High |

### Specific Tools for React Native

```
iOS (VoiceOver built-in):
- Enable: Settings > Accessibility > VoiceOver
- Navigate: Swipe right (next), left (previous)
- Activate: Double tap
- Special: Two-finger Z (dismiss), Two-finger swipe (scroll)

Android (TalkBack built-in):
- Enable: Settings > Accessibility > TalkBack
- Navigate: Swipe right (next), left (previous)
- Activate: Double tap
- Special: Swipe up+right (read from top), Swipe down (read all)
```

---

## 📱 ACCESSIBILITY IN REACT NATIVE

React Native has built-in accessibility support via platform APIs:

### iOS (VoiceOver)

```javascript
// Make component announced
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Записаться на услугу"
  accessibilityRole="button"
  onPress={bookService}
>
  <Text>Записаться</Text>
</TouchableOpacity>

// Announce dynamic changes
<View
  accessible={true}
  accessibilityLiveRegion="polite"
  accessibilityLabel={`Статус: ${status}`}
>
  <Text>{status}</Text>
</View>
```

### Android (TalkBack)

```javascript
// Same API works for Android too
// But test to verify announcements

// Test with:
// 1. Enable TalkBack
// 2. Navigate to component
// 3. Verify announcement is clear
```

### Key React Native A11y Props

```javascript
// Label the component
accessibilityLabel="Описание для screen reader"

// Define the role
accessibilityRole="button" | "link" | "image" | etc

// Announce live updates
accessibilityLiveRegion="polite" | "assertive"

// Hide decorative elements
accessible={false} // or aria-hidden

// Disable element from interactions
accessibilityElementsHidden={true}

// Notify of state changes
accessibilityState={{ disabled: true }}
```

---

## 🎯 ACCESSIBILITY ROADMAP

### Phase 1: Foundation (NOW - Pre-MVP)
- ✅ Documentation complete (this file)
- ✅ Team trained on basics
- ✅ Semantic components in place
- [ ] Keyboard navigation testing
- [ ] Initial screen reader testing

### Phase 2: MVP (Release)
- [ ] Comprehensive keyboard testing
- [ ] VoiceOver/TalkBack testing
- [ ] Contrast ratio verification
- [ ] Error message improvements
- [ ] Focus management implementation

### Phase 3: Polish (Post-MVP)
- [ ] Detailed WCAG audit
- [ ] Automated testing in CI/CD
- [ ] User testing with people with disabilities
- [ ] AAA enhancements
- [ ] Android TalkBack specific fixes

### Phase 4: Maintenance (Ongoing)
- [ ] Regular accessibility audits
- [ ] Team training updates
- [ ] User feedback integration
- [ ] New feature accessibility reviews

---

## 📚 RESOURCES & STANDARDS

### Official Standards
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Official standard
- [WebAIM](https://webaim.org/) - Best practices & tutorials
- [A11y Project](https://www.a11yproject.com/) - Community resources

### React Native Specific
- [React Native Accessibility Docs](https://reactnative.dev/docs/accessibility)
- [VoiceOver Guide](https://www.apple.com/accessibility/voiceover/)
- [TalkBack Guide](https://support.google.com/accessibility/android/answer/6283677)

### Testing Tools
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Oracle](https://colororacle.org/) - Color blindness simulator

### Learning Resources
- [Inclusive Components](https://inclusive-components.design/) - Design patterns
- [a11ycasts](https://www.youtube.com/playlist?list=PLNYkxOF6rcICWx0C9Xc-RgEzwLvIYkXKe) - YouTube series
- [WebAIM Blog](https://webaim.org/blog/) - Latest news & tips

---

## 🚀 GETTING STARTED

### For Developers
1. Read [keyboard-navigation.md](./keyboard-navigation.md)
2. Read [screen-readers.md](./screen-readers.md)
3. Test your components with keyboard
4. Test with native screen readers (VoiceOver/TalkBack)
5. Check [testing.md](./testing.md) for detailed process

### For Designers
1. Read [color-contrast.md](./color-contrast.md)
2. Use Stark plugin to test in Figma
3. Use Color Oracle to simulate color blindness
4. Ensure focus indicators are visible

### For Product Managers
1. Understand the business case (this document)
2. Allocate time for a11y testing in sprints
3. Consider user testing with people with disabilities
4. Plan accessibility improvements in roadmap

---

## 🎓 TEAM CHECKLIST

Before launch, ensure team has:

- [ ] **Understanding:** Everyone knows why a11y matters
- [ ] **Skills:** Developers trained on implementation
- [ ] **Tools:** Team has access to testing tools
- [ ] **Process:** Accessibility review in definition of done
- [ ] **Testing:** Manual testing process documented
- [ ] **Documentation:** Guidelines published (✅ done!)

---

## 📞 QUESTIONS?

- **Quick questions:** Check specific guides (keyboard, screen readers, contrast)
- **Complex issues:** Review WCAG guidelines or consult a11y specialist
- **Team training:** Schedule accessibility workshop

---

**Accessibility is how we show respect for all users.** 🤝

