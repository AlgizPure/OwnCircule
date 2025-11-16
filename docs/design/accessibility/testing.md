# ACCESSIBILITY TESTING

**Version:** 1.0

---

## 🧪 TESTING METHODS

### 1. Automated Testing

**Tools:**
- axe DevTools (Chrome)
- Lighthouse (Chrome)
- WAVE (WebAIM)

**Catches:** ~30-40% of issues

**Cannot catch:**
- Focus order
- Alt text quality
- ARIA misuse
- Keyboard traps

**Use as first pass, not complete test!**

---

### 2. Keyboard Testing

**Test checklist:**
- [ ] Tab through all interactive elements
- [ ] All elements have visible focus
- [ ] Tab order is logical
- [ ] Enter/Space activates
- [ ] Escape closes modals
- [ ] No keyboard traps
- [ ] Skip links work

---

### 3. Screen Reader Testing

**Tools:**
- NVDA (Windows, free)
- VoiceOver (Mac, built-in)

**Test checklist:**
- [ ] All content announced
- [ ] Images have alt text
- [ ] Links are descriptive
- [ ] Form labels present
- [ ] Headings in order
- [ ] ARIA correct

---

### 4. Visual Testing

**Test:**
- [ ] Zoom to 200% (readable?)
- [ ] Color contrast (4.5:1+)
- [ ] Color blindness (use simulator)
- [ ] Dark mode (if supported)

---

## 🔧 TOOLS

### Browser Extensions

**axe DevTools:**
- Free
- Comprehensive
- Best for developers

**Lighthouse:**
- Built into Chrome
- Accessibility score
- Quick overview

**WAVE:**
- Visual overlay
- Good for designers

---

### Screen Readers

**NVDA (Windows):**
- Free, open-source
- Download: nvaccess.org

**VoiceOver (Mac):**
- Built-in
- Enable: Cmd + F5

---

### Color Tools

**Contrast checkers:**
- WebAIM Contrast Checker
- Contrast Ratio (contrast-ratio.com)

**Color blindness simulators:**
- Color Oracle (free desktop app)
- Stark (Figma plugin)

---

## 📋 TESTING CHECKLIST

### Before Launch

- [ ] **Automated:** Run axe DevTools (0 errors)
- [ ] **Keyboard:** Full keyboard navigation works
- [ ] **Screen reader:** Tested with NVDA or VoiceOver
- [ ] **Contrast:** All text meets 4.5:1
- [ ] **Zoom:** Readable at 200% zoom
- [ ] **Color blind:** Tested with simulator
- [ ] **Focus:** All focus indicators visible

---

### Ongoing

- [ ] Test new features with keyboard
- [ ] Run automated tests in CI/CD
- [ ] Monthly screen reader spot checks
- [ ] User testing with disabled users

---

## 🎯 PRIORITY ISSUES

### Critical (Fix immediately)

- Cannot access via keyboard
- Missing alt text on images
- Forms without labels
- Contrast below 3:1

### High (Fix soon)

- Poor focus indicators
- Illogical tab order
- Missing ARIA labels
- Contrast 3:1-4.4:1

### Medium (Fix when possible)

- Link text not descriptive
- Heading hierarchy wrong
- Missing landmarks

---

## 👥 USER TESTING

**Best test:** Real users with disabilities

**How:**
- Recruit users with disabilities
- Observe them using your product
- Ask about pain points
- Fix issues found

**Worth it:** Catches issues tools miss

---

**Test early, test often. Fix what you find.** 🧪

