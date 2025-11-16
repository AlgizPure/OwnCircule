# DESIGN SYSTEM

**Version:** 1.0  
**Last Updated:** [YYYY-MM-DD]  
**Status:** Template - Fill during bootstrap  
**Figma:** [Link to Figma file]

---

## 🎯 PURPOSE

Design system - это единая система дизайна, которая обеспечивает:

**Consistency (Единообразие)**
- Все элементы UI выглядят и работают одинаково
- Пользователи знают чего ожидать
- Меньше путаницы, больше доверия

**Efficiency (Эффективность)**
- Дизайнеры и разработчики говорят на одном языке
- Компоненты переиспользуются, не создаются заново
- Быстрее создание новых фич

**Scalability (Масштабируемость)**
- Легко добавлять новые компоненты
- Легко обновлять существующие
- Система растет вместе с продуктом

**Quality (Качество)**
- Accessibility встроена в компоненты
- Best practices применяются автоматически
- Меньше багов, больше качества

---

## 🏗️ STRUCTURE

Design system состоит из 5 уровней:

### 1. Foundation (Фундамент)
**Токены дизайна** - базовые элементы:
- [Colors](foundation/colors.md) - цветовая палитра
- [Typography](foundation/typography.md) - типографика
- [Spacing](foundation/spacing.md) - отступы и размеры
- [Elevation](foundation/elevation.md) - тени и z-index
- [Motion](foundation/motion.md) - анимации
- [Iconography](foundation/iconography.md) - иконки
- [Principles](foundation/principles.md) - принципы дизайна

**Single source of truth** для всех дизайн-решений.

---

### 2. Components (Компоненты)
**Переиспользуемые UI элементы:**
- [Button](components/button.md) - кнопки
- [Input](components/input.md) - поля ввода
- [Card](components/card.md) - карточки
- [Modal](components/modal.md) - модальные окна
- [Navigation](components/navigation.md) - навигация
- [Form](components/form.md) - формы
- [Table](components/table.md) - таблицы
- [Dropdown](components/dropdown.md) - выпадающие списки
- [Tooltip](components/tooltip.md) - подсказки

Каждый компонент документирован:
- Anatomy (структура)
- Variants (варианты)
- States (состояния)
- Props/API
- Accessibility
- Code examples

---

### 3. Patterns (Паттерны)
**Композиции компонентов:**
- [Forms](patterns/forms.md) - паттерны форм
- [Data Display](patterns/data-display.md) - отображение данных
- [Navigation](patterns/navigation.md) - навигационные паттерны
- [Feedback](patterns/feedback.md) - обратная связь
- [Layouts](patterns/layouts.md) - макеты страниц

Решения повторяющихся UX задач.

---

### 4. Content (Контент)
**Голос и тон продукта:**
- [Voice & Tone](content/voice-and-tone.md) - голос бренда
- [Writing Guidelines](content/writing-guidelines.md) - правила написания
- [Error Messages](content/error-messages.md) - сообщения об ошибках
- [Microcopy](content/microcopy.md) - микротексты

Как мы общаемся с пользователями.

---

### 5. Accessibility (Доступность)
**A11y guidelines:**
- [Overview](accessibility/overview.md) - обзор и WCAG compliance
- [Keyboard Navigation](accessibility/keyboard-navigation.md) - клавиатура
- [Screen Readers](accessibility/screen-readers.md) - скрин-ридеры
- [Color Contrast](accessibility/color-contrast.md) - контрастность
- [Testing](accessibility/testing.md) - тестирование

Usable by everyone.

---

## 🎨 DESIGN TOKENS

**Что такое токены?**

Design tokens = дизайн-решения как данные (colors, spacing, typography)

```
Вместо:
"Используй синий цвет #2196F3"

Токен:
"Используй color-primary-500"
```

**Преимущества:**
- ✅ Single source of truth
- ✅ Легко менять (change once, apply everywhere)
- ✅ Sync между Figma и кодом
- ✅ Consistent naming

**Где:**
- Design tokens (JSON): [design-tokens.json](resources/design-tokens.json)
- Figma variables: [Linked in Figma]
- Code: CSS variables, Tailwind config

**Категории токенов:**
```yaml
Colors:
  - Primary (brand colors)
  - Secondary (accent colors)
  - Semantic (success, error, warning, info)
  - Neutral (grays, black, white)

Typography:
  - Font families
  - Font sizes
  - Font weights
  - Line heights

Spacing:
  - 4px grid (4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80)

Elevation:
  - Shadow levels (1-5)
  - Z-index layers

Motion:
  - Durations (fast, medium, slow)
  - Easing curves (ease-in, ease-out, ease-in-out)
```

---

## 📚 DOCUMENTATION STRUCTURE

```
docs/design/
├── 00_DESIGN_SYSTEM.md          # Этот файл (overview)
│
├── foundation/                   # Design tokens & principles
│   ├── colors.md                # Цветовая палитра
│   ├── typography.md            # Типографика
│   ├── spacing.md               # Spacing scale
│   ├── elevation.md             # Shadows, z-index
│   ├── motion.md                # Анимации
│   ├── iconography.md           # Иконки
│   └── principles.md            # Принципы дизайна
│
├── components/                   # Component library
│   ├── _COMPONENT_TEMPLATE.md   # Template для новых
│   ├── button.md                # Button component
│   ├── input.md                 # Input component
│   ├── card.md                  # Card component
│   └── ...                      # Другие компоненты
│
├── patterns/                     # Design patterns
│   ├── forms.md                 # Form patterns
│   ├── data-display.md          # Tables, lists, grids
│   ├── navigation.md            # Navigation patterns
│   ├── feedback.md              # Toasts, alerts
│   └── layouts.md               # Page layouts
│
├── content/                      # Content guidelines
│   ├── voice-and-tone.md        # Brand voice
│   ├── writing-guidelines.md    # UX writing
│   ├── error-messages.md        # Error patterns
│   └── microcopy.md             # Buttons, labels
│
├── accessibility/                # A11y guidelines
│   ├── overview.md              # WCAG goals
│   ├── keyboard-navigation.md   # Keyboard patterns
│   ├── screen-readers.md        # ARIA, semantic HTML
│   ├── color-contrast.md        # Contrast ratios
│   └── testing.md               # A11y testing
│
├── user-research/                # Research artifacts
│   ├── personas.md              # User personas
│   ├── journey-maps.md          # Journey maps
│   └── pain-points.md           # Pain points
│
├── screens/                      # Screen-level designs
│   └── _SCREEN_TEMPLATE.md      # Template для screens
│
└── resources/                    # Resources
    ├── figma-links.md           # Links to Figma
    ├── design-tokens.json       # Machine-readable tokens
    └── changelog.md             # Design system changelog
```

---

## 🔄 WORKFLOW

**Design → Code Process:**

### 1. Research
- User research (интервью, тесты)
- Competitor analysis
- Design inspiration

→ **Output:** [user-research/](user-research/)

---

### 2. Design
- Sketch ideas
- Create in Figma (using design system components)
- Document decisions

→ **Output:** Figma files, [screens/](screens/)

---

### 3. Document
- Update component docs если новый компонент
- Update patterns если новый паттерн
- Update design tokens если изменения

→ **Output:** Updated docs/design/

---

### 4. Review
- Design review (team)
- Accessibility check
- User testing (если нужно)

→ **Output:** Approved design

---

### 5. Build
- Implement using components
- Follow accessibility guidelines
- Apply design tokens

→ **Output:** Code implementation

---

### 6. Test
- Visual QA
- Accessibility testing
- Usability testing

→ **Output:** Validated implementation

---

### 7. Iterate
- Gather feedback
- Update design system если нужно
- Document learnings

→ **Output:** Updated system

---

## 🎯 DESIGN PRINCIPLES

Принципы которые направляют все дизайн-решения:

### 1. Clarity First
**Пользователи никогда не должны быть в замешательстве**

- Очевидное > Умное
- Прямое > Непрямое
- Простое > Сложное

**Example:**
- ✅ Кнопка "Сохранить изменения"
- ❌ Кнопка "Применить"

---

### 2. Consistency
**Паттерны повторяются предсказуемо**

- Одинаковые действия выглядят одинаково
- Одинаковые результаты после одинаковых действий
- Нет сюрпризов

**Example:**
- ✅ Primary кнопка всегда синяя
- ❌ Иногда синяя, иногда зеленая

---

### 3. Efficiency
**Минимизировать клики, максимизировать ценность**

- Быстрый доступ к частым действиям
- Keyboard shortcuts для power users
- Smart defaults

**Example:**
- ✅ Автофокус на первое поле формы
- ❌ Пользователь должен кликать на поле

---

### 4. Accessibility
**Usable by everyone**

- WCAG 2.1 AA compliance minimum
- Keyboard navigation
- Screen reader support
- Color contrast

**Example:**
- ✅ Focus visible, contrast 4.5:1
- ❌ Low contrast, no focus ring

---

### 5. Delight
**Продуманные детали имеют значение**

- Smooth animations
- Helpful microcopy
- Thoughtful empty states
- Personality (где уместно)

**Example:**
- ✅ Loading с прогрессом и сообщением
- ❌ Просто spinner

---

## 📖 HOW TO USE THIS

### For Designers

**1. Read design principles**
- Понять philosophy системы

**2. Use Figma components**
- [Figma link](resources/figma-links.md)
- Все компоненты уже там

**3. Document new patterns**
- Если создал новый паттерн → документируй в `docs/design/`

**4. Update design tokens**
- Изменения цветов/типографики → обнови `foundation/`

---

### For Developers

**1. Import design tokens**
- [design-tokens.json](resources/design-tokens.json)
- CSS variables или Tailwind config

**2. Use component library**
- Реализуй компоненты как задокументировано
- Follow prop API из документации

**3. Reference accessibility guidelines**
- [accessibility/](accessibility/)
- Build in a11y from start

**4. Ask questions**
- Если неясно → спроси дизайнера
- Update docs если нашел gaps

---

### For Product Managers

**1. Understand design principles**
- Почему дизайн такой какой есть

**2. Reference user research**
- [user-research/](user-research/)
- Insights for feature decisions

**3. Use patterns for specs**
- [patterns/](patterns/)
- Standard решения для common задач

**4. Consistency in communication**
- [content/](content/)
- Как мы говорим с users

---

## 🔗 QUICK LINKS

**For Everyone:**
- [Design Principles](#design-principles)
- [Figma Files](resources/figma-links.md)
- [Changelog](resources/changelog.md)

**For Designers:**
- [Foundation](foundation/colors.md) - tokens
- [Components](components/button.md) - library
- [Patterns](patterns/forms.md) - compositions

**For Developers:**
- [Design Tokens JSON](resources/design-tokens.json)
- [Accessibility Overview](accessibility/overview.md)
- [Component API docs](components/)

**For PMs:**
- [User Research](user-research/personas.md)
- [Content Guidelines](content/voice-and-tone.md)

---

## 🔄 MAINTENANCE

### When to Update

**Foundation:**
- При ребрендинге
- При добавлении новых токенов
- При accessibility improvements

**Components:**
- При создании нового компонента
- При изменении существующего
- При обнаружении паттерна

**Patterns:**
- При решении новой UX задачи
- При оптимизации существующего flow

**Content:**
- При изменении brand voice
- При feedback от пользователей

**Accessibility:**
- При изменении WCAG стандартов
- При обнаружении a11y issues

### How to Update

1. **Make change** (в Figma и/или коде)
2. **Update docs** (соответствующий .md файл)
3. **Update tokens** (если применимо)
4. **Update changelog** ([resources/changelog.md](resources/changelog.md))
5. **Notify team** (design review, PR)

---

## ⚠️ IMPORTANT NOTES

### Design System ≠ Static

Design system - это **living system**, которая:
- Эволюционирует с продуктом
- Обновляется на основе feedback
- Растет вместе с командой

**Не бойся изменений!** Лучше обновить систему, чем работать вокруг неё.

---

### Start Small, Scale Later

Не нужно создавать всё сразу:
1. ✅ Начни с foundation (colors, typography)
2. ✅ Добавь базовые components (button, input, card)
3. ✅ Expand по мере роста

**Главное:** Consistency > Completeness

---

### Documentation > Perfection

Лучше иметь:
- ✅ Простую документацию, которую все используют
- ❌ Идеальную документацию, которую никто не читает

**Keep it simple!**

---

## 📊 SUCCESS METRICS

Как понять что design system работает?

**Efficiency:**
- ⏱ Время создания новой фичи сокращается
- 🔄 Меньше back-and-forth между design и dev
- ♻️ Больше переиспользования компонентов

**Consistency:**
- 👀 Продукт выглядит unified
- 🎯 Меньше design debt
- ✅ Меньше inconsistencies reported

**Quality:**
- ♿ Accessibility compliance растет
- 🐛 Меньше UI bugs
- 😊 Пользователи довольны (NPS, feedback)

**Adoption:**
- 📚 Team использует документацию
- 💬 Дизайнеры reference систему
- 💻 Разработчики используют компоненты

---

## ❓ FAQ

**Q: Нужна ли design system для маленького проекта?**
A: Да! Даже базовый набор (colors, typography, button, input) сэкономит время.

**Q: Когда начинать создавать design system?**
A: Как можно раньше. Лучше добавлять в систему, чем рефакторить потом.

**Q: Что если мы используем готовую библиотеку (Material-UI, Ant Design)?**
A: Отлично! Документируй как вы её используете, кастомизации, ваши паттерны.

**Q: Кто отвечает за design system?**
A: Вся команда! Дизайнеры создают, разработчики реализуют, PM используют.

**Q: Как часто обновлять?**
A: Continuous. Каждое изменение в дизайне → обновление системы.

---

## ✨ GETTING STARTED

**Новая в команде?**

1. ✅ Прочитай этот файл (overview)
2. ✅ Изучи [Design Principles](foundation/principles.md)
3. ✅ Посмотри [Figma](resources/figma-links.md)
4. ✅ Explore [Components](components/)
5. ✅ Начинай использовать!

**Вопросы?** Спроси команду или создай issue.

---

## 🙏 CONTRIBUTING

Design system - это командный effort.

**Как помочь:**
- 🐛 Нашел inconsistency? Report it
- 💡 Есть идея? Propose it
- 📝 Нашел gap в документации? Fill it
- ✨ Создал новый компонент? Document it

**Together we build better!**

---

**Made with ❤️ for consistency, efficiency, and quality**

