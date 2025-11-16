# DESIGN PRINCIPLES

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Will be customized during bootstrap

---

## 🎯 WHAT ARE DESIGN PRINCIPLES?

Design principles - это **основополагающие убеждения**, которые направляют все дизайн-решения.

**Они:**
- Определяют identity продукта
- Помогают в спорных ситуациях
- Создают consistency
- Объединяют команду

**Принципы > Правила**

---

## 🌟 CORE PRINCIPLES

### 1. CLARITY FIRST

**"Пользователи никогда не должны быть в замешательстве"**

#### What it means
- Очевидное > Умное
- Прямое > Непрямое
- Простое > Сложное
- Clear communication > Clever design

#### In practice

**✅ Good:**
```
Button: "Save Changes"
Helper text: "Your changes will be saved immediately"
```

**❌ Bad:**
```
Button: "Apply"
No helper text (unclear what happens)
```

#### Questions to ask
- Поймет ли пользователь что делает эта кнопка?
- Очевидно ли что произойдет после клика?
- Есть ли альтернативный путь если пользователь запутался?

---

### 2. CONSISTENCY

**"Паттерны повторяются предсказуемо"**

#### What it means
- Одинаковые actions выглядят одинаково
- Одинаковые results после одинаковых actions
- Нет сюрпризов
- Learnable system

#### In practice

**✅ Good:**
- Primary action всегда синяя кнопка справа
- Delete всегда требует confirmation
- Save всегда показывает success toast

**❌ Bad:**
- Иногда Primary справа, иногда слева
- Иногда delete спрашивает, иногда нет
- Inconsistent feedback

#### Questions to ask
- Похоже ли это на другие части продукта?
- Ведет ли себя так же как похожие элементы?
- Можно ли использовать existing паттерн?

---

### 3. EFFICIENCY

**"Минимизировать клики, максимизировать ценность"**

#### What it means
- Быстрый access к частым actions
- Smart defaults
- Keyboard shortcuts
- Progressive disclosure (показать сначала важное)

#### In practice

**✅ Good:**
```
- Автофокус на первое поле формы
- Recent items в dropdown
- Keyboard shortcut: Cmd+S to save
- Most common action = primary button
```

**❌ Bad:**
```
- Пользователь должен кликать на каждое поле
- Нет shortcuts
- Все опции показаны сразу (overwhelming)
```

#### Questions to ask
- Сколько кликов требуется для завершения задачи?
- Можно ли сократить количество шагов?
- Есть ли keyboard shortcut для power users?

---

### 4. ACCESSIBILITY

**"Usable by everyone"**

#### What it means
- WCAG 2.1 AA compliance minimum
- Keyboard navigation
- Screen reader support
- Color contrast
- Not just compliance - usable!

#### In practice

**✅ Good:**
```
- Focus visible (outline on focus)
- ARIA labels на всех interactive elements
- Contrast ratio 4.5:1 minimum
- Keyboard navigable (Tab, Enter, Esc)
```

**❌ Bad:**
```
- No focus indicator
- Icon buttons без labels
- Low contrast text
- Only mouse navigable
```

#### Questions to ask
- Может ли пользователь использовать только клавиатуру?
- Понятен ли screen reader?
- Достаточный ли контраст?
- Testable с accessibility tools?

---

### 5. FEEDBACK

**"Пользователь всегда знает что происходит"**

#### What it means
- Immediate feedback на actions
- Clear status indicators
- Loading states
- Error messages с solutions
- Success confirmations

#### In practice

**✅ Good:**
```
Button clicked:
├─ Immediate visual feedback (hover state)
├─ Loading indicator если долго
├─ Success toast: "Saved successfully"
└─ Or error: "Failed. Try again or contact support"
```

**❌ Bad:**
```
Button clicked → ничего не происходит (или долго)
No loading state
No confirmation (did it work?)
```

#### Questions to ask
- Знает ли пользователь что его action received?
- Понятно ли что система делает (loading)?
- Clear ли result (success/error)?

---

### 6. DELIGHT

**"Продуманные детали имеют значение"**

#### What it means
- Smooth animations
- Helpful microcopy
- Thoughtful empty states
- Personality (где уместно)
- Surprise & delight moments

#### In practice

**✅ Good:**
```
Empty state:
├─ Friendly illustration
├─ "No tasks yet! Create your first task to get started"
└─ Clear CTA button

Loading:
├─ Progress indicator
├─ "Hang tight, we're loading your data..."
└─ Smooth animation
```

**❌ Bad:**
```
Empty state: "No data"
Loading: Just spinner (no context)
Generic, boring
```

#### Questions to ask
- Делает ли это пользователя счастливым?
- Есть ли personality (без overdoing)?
- Продуманы ли edge cases (empty, loading, error)?

---

## 🎨 HOW TO USE PRINCIPLES

### In Design Reviews

**Before:**
"Я не уверен в этом дизайне..."

**After:**
"Этот дизайн нарушает принцип CLARITY - неясно что произойдет после клика. Давайте добавим helper text."

---

### In Debates

**Спорная ситуация:**
Designer: "Давайте спрячем advanced options в submenu"
Developer: "Но это дополнительный клик"

**Решение через принципы:**
- CLARITY: Advanced options overwhelming для новых users → hide
- EFFICIENCY: Power users нуждаются в quick access → keyboard shortcut

**Result:** Hide в submenu + добавить keyboard shortcut (best of both)

---

### In Feature Planning

**New feature proposal:**
1. Does it follow CLARITY? (Понятно ли пользователю?)
2. Does it follow CONSISTENCY? (Соответствует ли existing паттернам?)
3. Does it follow EFFICIENCY? (Минимально ли кликов?)
4. Does it follow ACCESSIBILITY? (Доступно ли всем?)
5. Does it provide FEEDBACK? (Понятен ли результат?)
6. Does it add DELIGHT? (Есть ли thoughtful details?)

**If NO to any → revise!**

---

## 📝 CUSTOMIZATION

**These are TEMPLATE principles.**

During bootstrap, customize based on:
- Your product type (B2B vs B2C)
- Your users (technical vs non-technical)
- Your brand personality
- Your goals

**Examples:**

**SaaS Product:**
- Speed First (for productivity)
- Power User Focused (keyboard shortcuts)
- Minimal & Clean (no distractions)

**Consumer App:**
- Fun & Playful (personality matters)
- Mobile First (touch optimized)
- Delight Focused (wow moments)

**Developer Tool:**
- Technical Excellence (precision matters)
- Customizable (power users)
- Documentation First (clear docs)

---

## ⚖️ WHEN PRINCIPLES CONFLICT

**Example conflict:**
- CLARITY says: "Show all options clearly"
- EFFICIENCY says: "Hide advanced options"

**Resolution:**
1. What is primary goal? (New users vs power users?)
2. What does user research say?
3. Can we satisfy both? (Progressive disclosure)

**Best:** Progressive disclosure (simple first, advanced later)

---

## 🔄 EVOLVING PRINCIPLES

**Principles should evolve:**
- As product matures
- As users change
- As you learn

**Review annually:**
- Do principles still reflect product?
- Do team members follow them?
- Do they help decision making?

**Update when:**
- Product pivot
- User feedback patterns
- New team members confused

---

## ✅ CHECKLIST

Use these principles to evaluate any design:

- [ ] **CLARITY:** Понятно ли пользователю что это и как работает?
- [ ] **CONSISTENCY:** Соответствует ли existing patterns?
- [ ] **EFFICIENCY:** Минимально ли кликов/шагов?
- [ ] **ACCESSIBILITY:** Доступно ли всем (keyboard, screen reader, contrast)?
- [ ] **FEEDBACK:** Понятен ли result и status?
- [ ] **DELIGHT:** Есть ли thoughtful details?

**If all ✅ → Good design!**

---

## 💡 REMEMBER

**Principles guide, not dictate**
- They help make decisions
- They don't replace judgment
- Context matters

**Principles unite team**
- Shared language
- Faster decisions
- Better collaboration

**Principles evolve**
- Not set in stone
- Learn and adapt
- Review regularly

---

**Good principles = Good decisions = Good design** 🎯

