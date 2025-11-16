# FIGMA

Экспорты из Figma и ссылки на design files.

---

## ЧТО КЛАСТЬ

- Экспорты компонентов (PNG/JPG)
- Экспорты экранов (PNG/JPG)
- Design specs (PDF)
- `figma-links.md` - ссылки на live files

---

## СТРУКТУРА

```
figma/
├── components/              # Компоненты
│   ├── button-variants.png
│   ├── input-fields.png
│   └── cards.png
├── screens/                 # Экраны
│   ├── home-dashboard.png
│   ├── login-screen.png
│   └── settings.png
├── figma-links.md          # Ссылки на Figma
└── design-specs.pdf        # Specs (если есть)
```

---

## FIGMA-LINKS.MD

Создай файл со ссылками:

```markdown
# Figma Links

## Main Design File
https://figma.com/file/ABC123/Project-Name

**Contains:**
- All screens (20+)
- Component library
- Design system tokens

## Component Library
https://figma.com/file/DEF456/Components

**Contains:**
- Button variants
- Input fields
- Cards
- Modals
- Navigation

## Prototype
https://figma.com/proto/GHI789/Prototype

**Flow:** User onboarding → Dashboard → Task management

---

## Access
- Email: your-email@example.com
- Permissions: View/Comment
```

---

## TIPS

1. **Экспортируй ключевые screens** (не все, только важные)
2. **Добавляй ссылки** на live Figma files
3. **Указывай что где** (какой file для чего)
4. **Обновляй регулярно** если дизайн меняется

---

**Если Figma нет:** Пропусти эту папку!

