# FIGMA MAKE PROMPTS - READY TO USE

Автоматически сгенерированные промпты для создания MVP прототипа проекта "Свой Круг" через Figma Make.

---

## 📋 NEXT STEPS

### Шаг 1: Улучшить промпты через Claude Web

**Зачем:** Claude Web прочитает GitHub репозиторий и создаст улучшенные промпты с учётом всех 13 скриншотов дизайна и полной документации.

1. **Открой:** https://claude.ai/code (Web версия, Sonnet 4.5)

2. **Скопируй промпт из:**
   `CLAUDE_WEB_PROMPT.md`

3. **Замени плейсхолдеры:**
   - `{{owner}}` → `AlgizPure`
   - `{{repo}}` → `OwnCircule`

4. **Вставь в Claude Web** и дождись ответа (10-20 минут)

5. **Сохрани результаты:**
   - SECTION A → `global_prompt.md`
   - SECTION B → `module_prompts/module-XX.md` (для каждого модуля)
   - SECTION C → `iterations/module-XX_steps.md` (если есть)

6. **Напиши "continue"** в этот чат для продолжения

---

### Шаг 2: Используй промпты в Figma Make

**После получения промптов от Claude Web:**

1. **Открой Figma Make:**
   - https://www.figma.com/
   - Figma Make → New Project
   - **Требование:** Figma Professional план ($16/мес)

2. **Сначала используй GLOBAL PROMPT:**
   - Скопируй: `global_prompt.md`
   - Вставь в Figma Make → Generate
   - Это создаст базовую структуру, color palette, typography, навигацию

3. **Затем добавляй модули:**
   - По одному используй промпты из `module_prompts/module-XX.md`
   - Начни с Module 1 (Mobile App), затем Module 2 (Loyalty), и т.д.

4. **Для сложных модулей используй итерационные шаги:**
   - Из `iterations/module-XX_steps.md`
   - Пример: Module 1 → Step 1 (wireframe) → Step 2 (visual) → Step 3 (states) → Step 4 (mobile)

5. **Итерируй и улучшай:**
   - "Add empty state for events screen"
   - "Change primary color to #0ABAB5"
   - "Make QR code larger, 300x300px"
   - "Create responsive mobile version for profile screen"
   - "Add loading skeleton for transaction list"

6. **Экспорт результата:**
   - **Screenshots:** Export all screens as PNG → `exports/screens/`
   - **Design tokens:** Extract JSON → `exports/design-tokens.json`
   - **Figma link:** Share link → `exports/figma-link.md`

7. **После экспорта:**
   - Continue bootstrap → PHASE 5.5 (Design System)
   - PHASE 5.5 автоматически обработает Figma exports

---

## 📁 СТРУКТУРА ФАЙЛОВ

```
figma-make/
├── README.md                        # This file
├── FIGMA_MAKE_PROMPT_base.md        # Базовый промпт (локально сгенерированный)
├── CLAUDE_WEB_PROMPT.md             # Промпт для Claude Web
├── global_prompt.md                 # Улучшенный промпт (создаётся Claude Web)
├── module_prompts/                  # Per-module промпты (создаются Claude Web)
│   ├── module-01-mobile-app.md
│   ├── module-02-loyalty-system.md
│   ├── module-03-transactions.md
│   ├── module-04-events.md
│   ├── module-05-cross-promo.md
│   └── module-13-security.md
├── iterations/                      # Итерационные промпты (создаются Claude Web)
│   ├── module-01-mobile-app_steps.md
│   ├── module-02-loyalty-system_steps.md
│   └── module-04-events_steps.md
└── exports/                         # Результаты Figma Make (после работы)
    ├── screens/                     # PNG screenshots всех экранов
    ├── design-tokens.json           # Extracted design tokens
    └── figma-link.md                # Link to Figma file
```

---

## 💡 TIPS & BEST PRACTICES

### Работа с Figma Make:

1. **Будь специфичным:** "Tiffany Blue #0ABAB5" лучше чем "синий"
2. **Итерируй постепенно:** Wireframe → Visual → States → Responsive
3. **Используй примеры:** "Like Linear's navigation" vs "современная навигация"
4. **Проверяй консистентность:** Используй один и тот же spacing (8px), border-radius (12px)
5. **Создавай компоненты:** Button, Card, Input должны быть переиспользуемыми
6. **Тестируй на реальных данных:** Не "Lorem ipsum", а реальные названия бизнесов (Skinerica, Лисичкино)

### Приоритеты для MVP:

Создай в первую очередь:
1. **Home Dashboard** - центральный хаб
2. **QR Code Screen** - ключевая ценность
3. **Events List + Detail** - вовлечение сообщества
4. **Profile + Bonuses** - показать награды
5. **Phone Registration** - точка входа

---

## 📊 QUALITY CHECKLIST

Перед завершением проверь:

**Визуальная консистентность:**
- [ ] Tiffany Blue (#0ABAB5) используется для всех primary actions
- [ ] Typography scale соблюдён (28px/22px/18px/16px/14px/12px)
- [ ] Spacing на базе 8px (8/16/24/32/48px)
- [ ] Border radius консистентен (8/12/20px, full для аватаров)
- [ ] Shadows используются унифицированно

**Функциональная полнота:**
- [ ] Все топ-6 модулей покрыты (Mobile App, Loyalty, Transactions, Events, Cross-Promo, Security)
- [ ] Все критические flows работают (Registration, QR scan, Event registration)
- [ ] Empty states созданы (no events, no transactions, no bonuses)
- [ ] Error states созданы (failed login, network error, validation errors)
- [ ] Loading states созданы (skeletons, spinners)

**UX качество:**
- [ ] Touch targets ≥44px (Apple HIG)
- [ ] Text contrast ≥4.5:1 (WCAG AA)
- [ ] Focus indicators видны (2px Tiffany Blue ring)
- [ ] Навигация интуитивна (bottom tabs, breadcrumbs)
- [ ] Feedback на действия (toast notifications, success animations)

**Mobile optimization:**
- [ ] Responsive layouts (375-428px width)
- [ ] Bottom tabs вместо sidebar
- [ ] Cards вместо tables
- [ ] Single column forms
- [ ] Swipe gestures где уместно

---

## 🎯 SUCCESS CRITERIA

Прототип готов когда:
✅ Все MVP экраны созданы (20+ screens)
✅ Навигация работает (tap между экранами)
✅ Визуальный стиль консистентен
✅ Можно показать заинтересованным лицам (investors, partners)
✅ Можно использовать для user testing

---

**Made for UPMT v3.1+**  
**Figma Make Integration v1.0**  
**Dual Prompting: Local Base + Claude Web Enhanced**
