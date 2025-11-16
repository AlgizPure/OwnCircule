# NAVIGATION

**Component:** Navigation  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Navigation helps users move through the application.

**Types:**
- Top navigation (horizontal)
- Sidebar navigation (vertical)
- Tabs
- Breadcrumbs

---

## 🎨 VARIANTS

### Top Navigation

```html
<nav class="top-nav">
  <div class="nav-brand">
    <logo />
  </div>
  <ul class="nav-links">
    <li><a href="/" class="active">Dashboard</a></li>
    <li><a href="/projects">Projects</a></li>
    <li><a href="/settings">Settings</a></li>
  </ul>
  <div class="nav-actions">
    <button>Profile</button>
  </div>
</nav>
```

**Layout:**
- Logo (left)
- Links (center)
- Actions (right)

---

### Sidebar Navigation

```html
<aside class="sidebar">
  <div class="sidebar-header">
    <logo />
  </div>
  <nav class="sidebar-nav">
    <a href="/" class="nav-item active">
      <icon name="home" />
      <span>Dashboard</span>
    </a>
    <a href="/projects" class="nav-item">
      <icon name="folder" />
      <span>Projects</span>
    </a>
  </nav>
</aside>
```

**Features:**
- Collapsible
- Icons + labels
- Active state highlighting

---

### Tabs

```html
<div class="tabs">
  <button class="tab active">Overview</button>
  <button class="tab">Details</button>
  <button class="tab">Activity</button>
</div>
```

**Usage:** Within page navigation

---

### Breadcrumbs

```html
<nav class="breadcrumbs">
  <a href="/">Home</a>
  <span>/</span>
  <a href="/projects">Projects</a>
  <span>/</span>
  <span aria-current="page">Project Alpha</span>
</nav>
```

**Usage:** Show current location

---

## 🎭 STATES

### Default

```yaml
Text: gray-700
Background: transparent
```

---

### Hover

```yaml
Text: primary-600
Background: gray-100
```

---

### Active

```yaml
Text: primary-600
Background: primary-50
Font weight: 600
```

---

### Focus

```yaml
Outline: 2px solid primary-500
```

---

## ♿ ACCESSIBILITY

### Semantic HTML

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>
```

---

### Active State

```html
<a href="/" aria-current="page">Dashboard</a>
```

---

### Keyboard

- Tab: Navigate items
- Enter: Activate link
- Arrow keys: Move between tabs

---

## 🎯 USAGE

**Do's:**
- ✅ Clear labels
- ✅ Highlight active page
- ✅ Consistent placement
- ✅ Max 5-7 top-level items

**Don'ts:**
- ❌ Too many items (overwhelming)
- ❌ Unclear labels
- ❌ Hidden navigation (always visible)

---

**Navigation is the map. Make it clear.** 🧭

