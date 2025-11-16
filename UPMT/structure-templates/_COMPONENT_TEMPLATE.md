# [COMPONENT NAME]

**Component:** [Component Name]  
**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** [Draft / Review / Approved / Implemented]  
**Figma:** [Link to Figma component]

---

## 📋 OVERVIEW

**Purpose:** [Brief description of what this component does]

**Use cases:**
- [When to use this component]
- [Common scenarios]
- [Problem it solves]

**When NOT to use:**
- [When to use alternative]
- [Anti-patterns]

---

## 🏗️ ANATOMY

```
[Visual ASCII representation of component structure]

Example:
┌─────────────────────────┐
│  [Icon]  Label  [Icon]  │  ← Container
└─────────────────────────┘
   ↑       ↑        ↑
  Leading  Text   Trailing
```

**Elements:**
1. **[Element 1]** - [Description, required/optional]
2. **[Element 2]** - [Description]
3. **[Element 3]** - [Description]

---

## 🎨 VARIANTS

### [Variant 1 Name]

**Purpose:** [When to use this variant]

**Visual characteristics:**
- Background: [color]
- Text: [color]
- Border: [style]
- Other: [properties]

**Usage example:**
```html
<component variant="variant1">
  Content
</component>
```

---

### [Variant 2 Name]

**Purpose:** [When to use]

**Visual characteristics:**
- [Properties]

---

## 📏 SIZES

### Small

```yaml
Dimensions: [height x width or other measurements]
Padding: [values]
Font size: [value]
Icon size: [value]
Gap: [value]
```

**Usage:** [When to use small size]

---

### Medium (Default)

```yaml
Dimensions: [values]
Padding: [values]
Font size: [value]
```

**Usage:** [Most common use cases]

---

### Large

```yaml
Dimensions: [values]
Padding: [values]
Font size: [value]
```

**Usage:** [When to use large size]

---

## 🎭 STATES

### Default (Rest)

**Visual:**
```yaml
Background: [color]
Border: [style]
Text: [color]
Other: [properties]
```

**Description:** [Normal, ready for interaction]

---

### Hover

**Visual:**
```yaml
Background: [color change]
Cursor: pointer
Transition: [duration] [easing]
Other changes: [properties]
```

**Trigger:** Mouse hover or keyboard focus

---

### Active (Pressed)

**Visual:**
```yaml
Transform: [if any]
Opacity: [if changed]
Other: [properties]
```

**Trigger:** Mouse down or key press

---

### Focus

**Visual:**
```yaml
Outline: 2px solid [color]
Outline offset: 2px
Box-shadow: [if any]
```

**CRITICAL:** Must be visible for accessibility!

---

### Disabled

**Visual:**
```yaml
Background: [color]
Text: [color]
Cursor: not-allowed
Opacity: [value]
```

**When:** [Explain when to disable vs hide]

**Avoid:** [Why disabled state should be used sparingly]

---

### Loading (if applicable)

**Visual:**
```yaml
Spinner: [position]
Content: [hidden or semi-transparent]
Cursor: wait
```

**When:** [During async operations]

---

### Error/Success (if applicable)

**Visual:**
```yaml
Border: [color change]
Icon: [error/success indicator]
Message: [position and style]
```

---

## 🎯 USAGE GUIDELINES

### Do's

- ✅ [Best practice 1]
- ✅ [Best practice 2]
- ✅ [Best practice 3]
- ✅ [When and how to use]

---

### Don'ts

- ❌ [Anti-pattern 1]
- ❌ [Anti-pattern 2]
- ❌ [Common mistakes]
- ❌ [What to avoid]

---

### Content Guidelines

**[If component has text content]**

**Labels:**
- [Guidelines for labels]
- [Capitalization]
- [Length limits]

**Examples:**
- ✅ Good: "[Example]"
- ❌ Bad: "[Example]"

---

## ♿ ACCESSIBILITY

### Keyboard Navigation

**Keys:**
- Tab: [Behavior]
- Enter/Space: [Behavior]
- Escape: [Behavior]
- Arrow keys: [If applicable]

---

### Screen Readers

**ARIA attributes:**
```html
<component
  role="[role]"
  aria-label="[label]"
  aria-labelledby="[id]"
  aria-describedby="[id]"
  aria-expanded="[true/false]"
  aria-hidden="[true/false]"
/>
```

**Requirements:**
- [What screen reader must announce]
- [State changes to announce]

---

### Focus Management

- [How focus is handled]
- [Focus trap requirements]
- [Return focus behavior]

---

### Color Contrast

- Text on background: [ratio] (WCAG [level])
- Interactive elements: [ratio]
- States clearly distinguishable

---

## 🔧 IMPLEMENTATION

### HTML/JSX Structure

```html
<!-- Basic structure -->
<component class="component-name">
  <element1>Content</element1>
  <element2>Content</element2>
</component>
```

---

### CSS

```css
.component-name {
  /* Layout */
  display: [value];
  position: [value];
  
  /* Sizing */
  width: [value];
  height: [value];
  padding: [value];
  
  /* Visual */
  background: var(--color);
  border: [value];
  border-radius: [value];
  
  /* Typography */
  font-size: [value];
  font-weight: [value];
  color: [value];
  
  /* Interaction */
  cursor: [value];
  transition: [properties] [duration] [easing];
}

.component-name:hover {
  /* Hover styles */
}

.component-name:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

.component-name:disabled {
  /* Disabled styles */
}
```

---

### React Component Example

```jsx
const ComponentName = ({
  children,
  variant = 'default',
  size = 'medium',
  disabled = false,
  loading = false,
  onClick,
  ...props
}) => {
  return (
    <div
      className={`component ${variant} ${size}`}
      disabled={disabled || loading}
      onClick={onClick}
      {...props}
    >
      {loading && <Spinner />}
      {!loading && children}
    </div>
  );
};

// Usage
<ComponentName variant="primary" size="medium">
  Content
</ComponentName>
```

---

### Vue Component Example

```vue
<template>
  <div 
    :class="['component', variant, size]"
    :disabled="disabled || loading"
    @click="handleClick"
  >
    <Spinner v-if="loading" />
    <slot v-else />
  </div>
</template>

<script>
export default {
  props: {
    variant: { type: String, default: 'default' },
    size: { type: String, default: 'medium' },
    disabled: Boolean,
    loading: Boolean
  }
}
</script>
```

---

### Props/API

```typescript
interface ComponentProps {
  // Required
  children: ReactNode;
  
  // Optional
  variant?: 'default' | 'primary' | 'secondary';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  loading?: boolean;
  className?: string;
  
  // Events
  onClick?: () => void;
  onFocus?: () => void;
  onBlur?: () => void;
}
```

---

## 📝 EXAMPLES

### Basic Usage

```html
<component>
  Basic content
</component>
```

---

### With Variant

```html
<component variant="primary">
  Primary variant
</component>
```

---

### With Size

```html
<component size="small">
  Small size
</component>
```

---

### With State

```html
<component disabled>
  Disabled state
</component>

<component loading>
  Loading...
</component>
```

---

### Complex Example

```html
<component 
  variant="primary"
  size="large"
  icon="save"
  loading={isLoading}
  onClick={handleSave}
>
  Save Changes
</component>
```

---

## 📱 RESPONSIVE BEHAVIOR

### Desktop (≥1024px)

[How component behaves on desktop]

---

### Tablet (768-1023px)

[Adjustments for tablet]

---

### Mobile (< 768px)

[Mobile-optimized behavior]
- [Size adjustments]
- [Layout changes]
- [Touch target size (min 44x44px)]

---

## ⚠️ COMMON MISTAKES

### ❌ Mistake 1

**Problem:** [Description]

**Why it's wrong:** [Explanation]

**Solution:** [How to fix]

---

### ❌ Mistake 2

**Problem:** [Description]

**Solution:** [How to fix]

---

## ⚖️ DESIGN DECISIONS

**Why [decision 1]:**
[Reasoning]

**Why [decision 2]:**
[Reasoning]

**Trade-offs:**
- [What we gained]
- [What we sacrificed]

---

## 🧪 TESTING CHECKLIST

**Visual:**
- [ ] All variants render correctly
- [ ] All sizes render correctly
- [ ] All states visible and distinct
- [ ] Responsive behavior works

**Functional:**
- [ ] All interactions work
- [ ] Loading state functions
- [ ] Disabled state prevents interaction
- [ ] Error/success states show correctly

**Accessibility:**
- [ ] Keyboard navigation works
- [ ] Focus indicator visible
- [ ] Screen reader announces correctly
- [ ] ARIA attributes correct
- [ ] Color contrast passes WCAG AA
- [ ] Touch targets ≥44x44px (mobile)

**Cross-browser:**
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

**Cross-device:**
- [ ] Desktop
- [ ] Tablet
- [ ] Mobile

---

## 🔗 RELATED

**Components:**
- [Related component 1]
- [Related component 2]

**Patterns:**
- [Related pattern]

**Guidelines:**
- [Related guideline]

---

## 📚 RESOURCES

**Design:**
- Figma: [Link]
- Prototype: [Link]

**Code:**
- Storybook: [Link]
- Repository: [Link]

**Research:**
- User testing results: [Link]
- A/B test data: [Link]

---

## 📝 CHANGELOG

**[Version] - [Date]:**
- [Change description]

**[Previous version] - [Date]:**
- [Change description]

---

## 💬 FEEDBACK

**Questions or suggestions?**
- Create issue: [Link]
- Slack channel: [Channel name]
- Contact: [Design team contact]

---

**[Closing message about component purpose]** [Emoji]

