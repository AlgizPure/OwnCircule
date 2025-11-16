# FIGMA MAKE PROMPT TEMPLATE v1.0

**Версия:** 1.0  
**Дата:** 2025-11-16  
**Назначение:** Генерация MVP интерфейса в Figma Make из UPMT Raw Data

---

## 📋 ИСТОЧНИКИ ДАННЫХ

Этот промпт генерируется автоматически из:

```
INPUT SOURCES:
├── UPMT/bootstrap/00_RAW_DATA_TEMPLATE/
│   ├── PROJECT_ESSENCE.md          → Контекст проекта
│   ├── extracted_features.md       → Функции по модулям
│   ├── modules_list.md             → Список модулей
│   └── metadata.yaml               → Метаданные
├── synthesized-project-data.md     → Unified view
└── verification/final-tech-stack.md → Tech stack
```

---

## 🎯 ШАБЛОН ПРОМПТА

```markdown
# PROJECT: {{project_name}}

## CONTEXT & PURPOSE

**What we're building:**
{{project_description}}

**Target users:**
{{target_audience}}

**Core value:**
{{unique_value_proposition}}

**Type:**
{{project_type}} ({{web_app|mobile_app|desktop_app|saas|etc}})

---

## VISUAL DIRECTION

### Style & Mood
{{visual_style_description}}
- **Feel:** {{minimal|modern|bold|playful|professional|etc}}
- **Inspiration:** {{reference_apps_like_Linear_Notion_Figma}}
- **Aesthetic:** {{clean|vibrant|dark|light|gradient|flat}}

### Color Strategy
**Primary:** {{primary_color_hex}} - {{usage_context}}
**Secondary:** {{secondary_color_hex}} - {{usage_context}}
**Accent:** {{accent_color_hex}} - {{for_ctas_highlights}}

**Semantic:**
- Success: {{success_color}} (confirmations, positive states)
- Warning: {{warning_color}} (cautions, pending actions)
- Error: {{error_color}} (errors, destructive actions)
- Info: {{info_color}} (helpful information)

**Neutrals:**
- Background: {{bg_color}}
- Surface: {{surface_color}}
- Text Primary: {{text_primary_color}}
- Text Secondary: {{text_secondary_color}}
- Border: {{border_color}}

### Typography
**Primary Font:** {{font_family_primary}} - For headings and emphasis
**Body Font:** {{font_family_body}} - For readable text
**Mono Font:** {{font_family_mono}} - For code and technical content

**Scale:**
- Display: {{display_size}}px / {{display_weight}}
- H1: {{h1_size}}px / {{h1_weight}}
- H2: {{h2_size}}px / {{h2_weight}}
- H3: {{h3_size}}px / {{h3_weight}}
- Body: {{body_size}}px / {{body_weight}}
- Small: {{small_size}}px / {{small_weight}}
- Caption: {{caption_size}}px / {{caption_weight}}

### Spacing System
Based on {{spacing_base}}px base unit:
- xs: {{spacing_base * 0.5}}px
- sm: {{spacing_base}}px
- md: {{spacing_base * 2}}px
- lg: {{spacing_base * 3}}px
- xl: {{spacing_base * 4}}px
- 2xl: {{spacing_base * 6}}px

### Other Foundations
**Border Radius:**
- Small: {{border_radius_sm}}px (inputs, small cards)
- Medium: {{border_radius_md}}px (cards, modals)
- Large: {{border_radius_lg}}px (hero sections)
- Full: {{border_radius_full}} (pills, avatars)

**Shadows:**
- Subtle: {{shadow_subtle}}
- Default: {{shadow_default}}
- Emphasis: {{shadow_emphasis}}

**Transitions:**
- Fast: {{transition_fast}}ms (hovers, micro-interactions)
- Base: {{transition_base}}ms (standard animations)
- Slow: {{transition_slow}}ms (page transitions)

---

## APPLICATION STRUCTURE

### Core Modules & Screens

{{#each_module_from_modules_list}}

#### MODULE: {{module_name}}
**Purpose:** {{module_description}}
**Priority:** {{must_have|should_have|nice_to_have}}

**User Actions in this module:**
{{#each_function_from_extracted_features}}
- {{function_id}}: {{function_description}}
  - Input: {{what_user_provides}}
  - Output: {{what_system_shows}}
  - Trigger: {{how_initiated}}
{{/each}}

**Screens needed:**
1. **{{screen_1_name}}** - {{screen_purpose}}
   - Layout: {{layout_type}}
   - Key elements: {{list_main_components}}
   - Actions: {{primary_ctas}}

2. **{{screen_2_name}}** - {{screen_purpose}}
   - Layout: {{layout_type}}
   - Key elements: {{list_main_components}}
   - Actions: {{primary_ctas}}

**UI Components required:**
- {{component_1}} ({{usage_context}})
- {{component_2}} ({{usage_context}})
- {{component_3}} ({{usage_context}})

**Data to display:**
- {{data_type_1}}: {{format_example}}
- {{data_type_2}}: {{format_example}}

**States to show:**
- Empty state: {{description}}
- Loading state: {{description}}
- Error state: {{description}}
- Success state: {{description}}

{{/each_module}}

---

## NAVIGATION STRUCTURE

**Primary Navigation:**
{{navigation_type}} ({{sidebar|top_nav|bottom_nav|tabs}})

**Navigation Items:**
{{#each_module_with_nav}}
- {{module_name}} → {{landing_screen}}
  - Icon: {{icon_suggestion}}
  - Badge: {{if_has_notifications}}
{{/each}}

**User Actions Menu:**
- Profile → User settings
- Notifications → Notification center
- Help → Documentation
- {{custom_actions}}

**Navigation Flow Examples:**
```
[Start] → [Dashboard] → [View Project] → [Edit Details] → [Save]
[Start] → [Projects List] → [Create New] → [Fill Form] → [Success]
[Dashboard] → [Analytics] → [Export Data] → [Download]
```

---

## KEY COMPONENTS TO CREATE

### Forms & Inputs
**Text Input:**
- Label placement: {{top|left|floating}}
- Validation: {{inline|on_submit}}
- Error display: {{below_field|tooltip}}
- States: default, focus, filled, error, disabled

**Select/Dropdown:**
- Style: {{native|custom}}
- Search: {{yes|no}}
- Multi-select: {{yes|no}}

**Buttons:**
- Primary: {{description}} - {{color}} background
- Secondary: {{description}} - {{color}} outline
- Tertiary: {{description}} - text only
- Destructive: {{description}} - for delete actions
- Sizes: small, medium, large

**Checkbox/Radio:**
- Style: {{custom|native}}
- Label position: {{right|left}}

**Date Picker:**
- Type: {{single|range|multi}}
- Format: {{date_format}}

### Data Display
**Tables:**
- Style: {{simple|striped|bordered|card_style}}
- Actions: {{inline|dropdown|modal}}
- Sorting: {{yes|no}}
- Filtering: {{yes|no}}
- Pagination: {{classic|infinite_scroll}}

**Cards:**
- Layout: {{vertical|horizontal}}
- Image: {{top|left|background}}
- Actions: {{bottom|corner|hover}}

**Lists:**
- Style: {{simple|detailed|interactive}}
- Avatar/Icon: {{yes|no}}
- Secondary info: {{yes|no}}

### Feedback & Modals
**Toast/Notification:**
- Position: {{top_right|bottom_right|etc}}
- Auto-dismiss: {{yes|no}}
- Types: success, error, warning, info

**Modal/Dialog:**
- Size: {{small|medium|large|fullscreen}}
- Backdrop: {{dimmed|blurred}}
- Close: {{x_button|outside_click|esc_key}}

**Loading States:**
- Spinner: {{style}}
- Skeleton: {{yes|no}}
- Progress bar: {{if_long_operations}}

**Empty States:**
- Illustration: {{yes|no}}
- Message: {{encouraging_helpful}}
- CTA: {{create_first_item}}

---

## RESPONSIVE BEHAVIOR

**Breakpoints:**
- Mobile: < {{mobile_breakpoint}}px
- Tablet: {{mobile_breakpoint}}px - {{tablet_breakpoint}}px
- Desktop: > {{tablet_breakpoint}}px

**Mobile Adaptations:**
- Navigation: {{hamburger_menu|bottom_tabs}}
- Tables: {{cards_on_mobile|horizontal_scroll}}
- Forms: {{single_column|stacked}}
- Spacing: {{reduced|maintained}}

**Touch Targets:**
- Minimum: {{touch_target_size}}px
- Spacing between: {{touch_spacing}}px

---

## INTERACTION PATTERNS

### Hover States
- Links: {{underline|color_change|opacity}}
- Buttons: {{darken|lighten|scale|shadow}}
- Cards: {{lift|border|scale}}

### Focus States
- Color: {{focus_color}}
- Style: {{outline|ring|glow}}
- Width: {{focus_width}}px

### Active States
- Effect: {{press_down|darken|scale}}

### Transitions
- Property: all / specific
- Duration: {{transition_duration}}ms
- Easing: {{ease_in_out|ease_out|cubic_bezier}}

### Micro-interactions
- Success: {{checkmark_animation|confetti|pulse}}
- Delete: {{fade_out|slide_out|shrink}}
- Add: {{slide_in|fade_in|scale_in}}
- Like: {{heart_pop|number_count_up}}

---

## ACCESSIBILITY REQUIREMENTS

**Color Contrast:**
- Target: WCAG 2.1 {{AA|AAA}}
- Text on background: {{min_ratio}}:1
- Interactive elements: {{min_ratio}}:1

**Keyboard Navigation:**
- Tab order: logical flow
- Focus visible: always
- Skip links: {{yes|no}}

**Screen Reader:**
- Alt text: all images
- ARIA labels: interactive elements
- Semantic HTML: proper headings

**Motion:**
- Reduced motion: respect prefers-reduced-motion
- Animations: skippable/pausable for long animations

---

## TECHNICAL CONSTRAINTS

**Framework Compatibility:**
{{tech_stack_framework}} - Ensure components are compatible

**Browser Support:**
{{browser_support_list}}

**Performance:**
- Images: optimized, lazy-loaded
- Icons: {{svg|icon_font|component_library}}
- Animations: GPU-accelerated where possible

**Responsive:**
- Mobile-first: {{yes|no}}
- Fluid typography: {{yes|no}}
- Container queries: {{yes|no}}

---

## SPECIAL FEATURES

{{#if_has_dark_mode}}
**Dark Mode:**
- Toggle: {{location}}
- Strategy: {{css_variables|separate_theme|class_based}}
- Colors: inverted semantic colors
{{/if}}

{{#if_has_i18n}}
**Internationalization:**
- RTL support: {{yes|no}}
- Text expansion: 30% buffer for translations
- Date/number formats: locale-aware
{{/if}}

{{#if_has_auth}}
**Authentication UI:**
- Login: {{modal|page|overlay}}
- Registration: {{multi_step|single_page}}
- Password reset: {{email_link|token}}
{{/if}}

{{#if_has_onboarding}}
**Onboarding:**
- Type: {{tour|checklist|video|walkthrough}}
- Steps: {{number_of_steps}}
- Skippable: {{yes|no}}
{{/if}}

---

## PRIORITY SCREENS (MVP)

Create these screens FIRST for immediate testing:

1. **{{priority_screen_1}}** - {{why_important}}
   - Shows: {{key_functionality}}
   - Tests: {{what_user_flow}}

2. **{{priority_screen_2}}** - {{why_important}}
   - Shows: {{key_functionality}}
   - Tests: {{what_user_flow}}

3. **{{priority_screen_3}}** - {{why_important}}
   - Shows: {{key_functionality}}
   - Tests: {{what_user_flow}}

---

## BRAND ELEMENTS

{{#if_has_brand}}
**Logo:**
- Placement: {{header|footer|both}}
- Size: {{logo_dimensions}}
- Versions: {{full|icon_only|text_only}}

**Brand Voice:**
- Tone: {{professional|friendly|casual|technical}}
- Messaging: {{concise|detailed|conversational}}

**Illustrations:**
- Style: {{if_custom_illustrations}}
- Usage: {{empty_states|hero_sections|onboarding}}
{{/if}}

---

## EXAMPLE USER FLOWS

### Flow 1: {{flow_name}}
```
[Start: {{entry_point}}]
  ↓
[{{screen_1}}: {{user_sees}}]
  ↓ (User action: {{what_user_does}})
[{{screen_2}}: {{system_response}}]
  ↓ (User action: {{what_user_does}})
[{{screen_3}}: {{final_state}}]
  ↓
[Success: {{what_achieved}}]
```

### Flow 2: {{flow_name}}
```
[Start: {{entry_point}}]
  ↓
[{{screen_1}}: {{user_sees}}]
  ↓ (User action: {{what_user_does}})
[{{screen_2}}: {{system_response}}]
  ↓
[Success: {{what_achieved}}]
```

{{additional_critical_flows}}

---

## NOTES & SPECIAL INSTRUCTIONS

{{special_instructions_or_constraints}}

**Important considerations:**
- {{consideration_1}}
- {{consideration_2}}
- {{consideration_3}}

**Known challenges:**
- {{challenge_1}}: {{how_to_approach}}
- {{challenge_2}}: {{how_to_approach}}

---

## OUTPUT REQUEST

Please create an interactive, high-fidelity prototype with:

✅ All screens for the MVP modules listed above
✅ Realistic content (not lorem ipsum)
✅ Proper navigation between screens
✅ Interactive states (hover, focus, active)
✅ Responsive layouts (mobile + desktop)
✅ Consistent design system throughout
✅ Accessibility considerations built-in

**Focus on:**
1. User flows for core functionality
2. Visual consistency across screens
3. Clear information hierarchy
4. Intuitive interactions
5. Professional polish

**The prototype should feel:**
- {{adjective_1}} (e.g., modern)
- {{adjective_2}} (e.g., intuitive)
- {{adjective_3}} (e.g., efficient)

---

Generated by UPMT Bootstrap Process  
Based on {{source_files}}  
Ready for Figma Make ✨
```

---

## 🔧 ПЕРЕМЕННЫЕ ДЛЯ ЗАМЕНЫ

### Из PROJECT_ESSENCE.md:
- `{{project_name}}`
- `{{project_description}}`
- `{{target_audience}}`
- `{{unique_value_proposition}}`

### Из metadata.yaml:
- `{{project_type}}`
- `{{visual_style_description}}`
- `{{tech_stack_framework}}`
- `{{primary_color_hex}}`
- `{{secondary_color_hex}}`
- Design preferences

### Из extracted_features.md:
- Функции по модулям
- User actions
- Screens needed

### Из modules_list.md:
- Список модулей
- Приоритеты модулей
- Описания модулей

### Из final-tech-stack.md:
- Framework info
- Browser support
- Technical constraints

---

## 📊 МЕТРИКИ КАЧЕСТВА ПРОМПТА

**Хороший промпт должен:**
- ✅ Специфичность: >80% конкретных деталей (не "красивый", а "HEX цвета")
- ✅ Полнота: Все модули из modules_list покрыты
- ✅ Структурированность: Четкие секции, легко читается
- ✅ Actionability: Figma Make может начать создавать сразу
- ✅ Контекстность: Связь между модулями и функциями ясна

**Плохие признаки:**
- ❌ Абстрактные термины без деталей
- ❌ Пропущенные модули
- ❌ Противоречия в требованиях
- ❌ Неясные user flows
- ❌ Отсутствие приоритетов

---

## 🎯 ИСПОЛЬЗОВАНИЕ

1. Генерация: Автоматически в PHASE 5.4 bootstrap.
2. Ревью: Проверка человеком перед отправкой.
3. Итерация: Дополнение после ответов пользователя.
4. Экспорт: В Figma Make для создания прототипа.

---

**Made for UPMT v3.0.1**  
**Compatible with Figma Make (2025)**


