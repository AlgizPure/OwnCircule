# TABLE

**Component:** Table  
**Version:** 1.0  
**Status:** Template

---

## 📋 OVERVIEW

Tables display structured data in rows and columns.

---

## 🏗️ STRUCTURE

```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Status</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John Doe</td>
      <td><span class="badge">Active</span></td>
      <td>
        <button class="icon-btn">Edit</button>
        <button class="icon-btn">Delete</button>
      </td>
    </tr>
  </tbody>
</table>
```

---

## 🎨 VARIANTS

### Basic Table

```css
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid var(--gray-200);
}

th {
  font-weight: 600;
  color: var(--gray-700);
  background: var(--gray-50);
}
```

---

### Striped Rows

```css
tbody tr:nth-child(even) {
  background: var(--gray-50);
}
```

---

### Hoverable Rows

```css
tbody tr:hover {
  background: var(--gray-100);
  cursor: pointer;
}
```

---

### Selectable Rows

```html
<tr>
  <td>
    <input type="checkbox" />
  </td>
  <td>Data</td>
</tr>
```

---

## 🎯 FEATURES

### Sortable Columns

```html
<th>
  <button class="sort-btn">
    Name
    <icon name="arrow-up" />
  </button>
</th>
```

---

### Fixed Header

```css
thead {
  position: sticky;
  top: 0;
  background: white;
  z-index: 10;
}
```

---

### Responsive (Mobile)

**Option 1: Horizontal scroll**

```css
.table-wrapper {
  overflow-x: auto;
}
```

**Option 2: Card view**

```css
@media (max-width: 768px) {
  table, thead, tbody, tr, th, td {
    display: block;
  }
  
  tr {
    border: 1px solid var(--gray-200);
    margin-bottom: 16px;
    padding: 12px;
  }
}
```

---

## ♿ ACCESSIBILITY

### Semantic HTML

```html
<table>
  <caption>User List</caption>
  <thead>
    <tr>
      <th scope="col">Name</th>
    </tr>
  </thead>
</table>
```

---

### Sortable Headers

```html
<th>
  <button 
    aria-label="Sort by name"
    aria-sort="ascending"
  >
    Name
  </button>
</th>
```

---

## 🎯 USAGE

**Do's:**
- ✅ Clear column headers
- ✅ Left-align text, right-align numbers
- ✅ Highlight row on hover
- ✅ Pagination for large data

**Don'ts:**
- ❌ Too many columns (>7 is hard)
- ❌ Inconsistent formatting
- ❌ No empty state
- ❌ No loading state

---

**Tables organize data. Keep them clean.** 📊

