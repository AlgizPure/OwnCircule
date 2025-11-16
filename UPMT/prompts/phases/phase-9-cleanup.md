# PHASE 9: PROJECT CLEANUP

**Время выполнения:** 5-10 минут (автономно)

**Назначение:** Очистка проекта от временных файлов bootstrap, оптимизация структуры для разработки

**🎯 ЦЕЛЬ:** Оставить только файлы, нужные для работы над проектом

---

## 📋 СТРАТЕГИЯ ОЧИСТКИ

### ✅ ЧТО ОСТАВИТЬ

**Критически важные файлы:**
- `docs/` - Вся проектная документация
- `.upmt/metadata.yaml` - Метаданные проекта
- `.cursorrules` - Правила для AI ассистентов
- `.context/` - Контекст проекта (state.md, decisions.md, insights.md, changes_log.md)
- `BOOTSTRAP_REPORT.md` - Финальный отчет о bootstrap
- `README.md` - Основной README проекта

**Полезные для референса:**
- `UPMT/bootstrap/00_RAW_DATA_TEMPLATE/` - Исходные данные (как архив)
- `UPMT/bootstrap/BOOTSTRAP_CONFIG/FINAL_SETUP_INSTRUCTIONS.md` - Инструкции настройки
- `UPMT/structure-templates/AI_INSTRUCTIONS/` - Правила для AI

### ❌ ЧТО УДАЛИТЬ

**Временные файлы bootstrap:**
- `UPMT/prompts/` - Все промпты и фазы (уже выполнены)
- `UPMT/start/` - Алиасы запуска сценариев
- `UPMT/START.md` - Меню запуска
- `UPMT/structure-templates/` - Шаблоны (кроме AI_INSTRUCTIONS)

**Документация UPMT:**
- `UPMT/docs/` - Архивная документация UPMT
- `UPMT/README_TEMPLATE.md` - Шаблон README
- `UPMT/LICENSE` - Лицензия UPMT
- `UPMT/VERSION_HISTORY.md` - История версий UPMT
- `UPMT/RELEASE_NOTES_v2.2.1.md` - Release notes UPMT

**Конфигурационные файлы bootstrap:**
- `UPMT/bootstrap/BOOTSTRAP_CONFIG/` - Все файлы кроме FINAL_SETUP_INSTRUCTIONS.md
- `UPMT/bootstrap/00_DESIGN_RAW_DATA/` - Если не содержит реальных данных проекта

**Временные файлы анализа:**
- `Claude code Chats export fo analyses/` - Чаты анализа (если есть)
- `BOOTSTRAP_START_PROMPT.md` - Старый промпт

---

## 📋 ИНСТРУКЦИИ

### ШАГ 1: Проверка существования UPMT_FINAL_STEPS.md

**Убедись что файл создан в PHASE 8:**

```bash
ls -la UPMT_FINAL_STEPS.md
```

**Если файл не существует:**
```bash
# Создай его вручную
cp UPMT/bootstrap/BOOTSTRAP_CONFIG/FINAL_SETUP_INSTRUCTIONS.md ./UPMT_FINAL_STEPS.md
```

---

### ШАГ 2: Анализ файлов для удаления

**Проверь что можно безопасно удалить:**

**CLI режим:**
```bash
# Проверь размер папки UPMT перед удалением
du -sh UPMT/

# Посмотри что будет удалено
find UPMT/ -type f | head -20
```

**Web режим (GitHub API):**
```bash
# Проверь через GitHub API
gh api /repos/{owner}/{repo}/contents/UPMT | jq '.[].name'
```

---

### ШАГ 3: Выборочная очистка

**Удаляй файлы поэтапно:**

```bash
# ШАГ 3.1: Удали промпты и фазы
rm -rf UPMT/prompts/

# ШАГ 3.2: Удали алиасы запуска
rm -rf UPMT/start/
rm UPMT/START.md

# ШАГ 3.3: Удали шаблоны (кроме AI_INSTRUCTIONS)
rm UPMT/structure-templates/_*.md
rm UPMT/structure-templates/backend-documentation/
rm UPMT/structure-templates/changes_log_TEMPLATE.md
rm UPMT/structure-templates/decisions_TEMPLATE.md
rm UPMT/structure-templates/insights_TEMPLATE.md
rm UPMT/structure-templates/state_TEMPLATE.md

# ШАГ 3.4: Удали документацию UPMT
rm -rf UPMT/docs/
rm UPMT/README_TEMPLATE.md
rm UPMT/LICENSE
rm UPMT/VERSION_HISTORY.md
rm UPMT/RELEASE_NOTES_*.md

# ШАГ 3.5: Удали конфиги bootstrap (кроме FINAL_SETUP_INSTRUCTIONS.md)
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/AUTO_FILL_INSTRUCTIONS.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_CHECKLIST.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_FLOW_DIAGRAM.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_INSTRUCTIONS.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_START_PROMPT.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/PHASE_5_7_BACKEND_INSERT.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/SYSTEM_TESTING_GUIDE.md
rm UPMT/bootstrap/BOOTSTRAP_CONFIG/tech-stack-verification.md

# ШАГ 3.6: Удали временные файлы (если есть)
rm -rf "Claude code Chats export fo analyses/"
rm BOOTSTRAP_START_PROMPT.md
```

---

### ШАГ 4: Проверка результатов

**Убедись что остались нужные файлы:**

```bash
# Проверь что критически важные файлы на месте
ls -la docs/
ls -la .upmt/
ls -la .cursorrules
ls -la .context/
ls -la BOOTSTRAP_REPORT.md
ls -la UPMT_FINAL_STEPS.md

# Проверь размер проекта после очистки
du -sh ./
```

**Проверь cross-references:**

```bash
# Убедись что ссылки в документации работают
grep -r "docs/" docs/ | head -5
```

---

### ШАГ 5: Финальный коммит

```bash
git add .
git commit -m "cleanup(bootstrap): PHASE 9 complete - project cleanup finished

- Removed temporary UPMT files
- Kept essential project files
- Added UPMT_FINAL_STEPS.md for reference
- Project ready for development!

Size reduced by ~XX MB"
git push
```

---

## 💾 CHECKPOINT

```bash
git add UPMT_FINAL_STEPS.md
git commit -m "docs(bootstrap): PHASE 9 - project cleanup complete"
git push
```

---

## 🎉 ЗАВЕРШЕНИЕ

**Проект очищен и готов к разработке!**

**Показать финальный статус:**

```markdown
✅ PHASE 9 COMPLETE - PROJECT CLEANUP

**Удалено:**
- UPMT prompts and phases
- Temporary bootstrap files
- UPMT documentation

**Сохранено:**
- Project documentation (docs/)
- AI configuration (.cursorrules)
- Project metadata (.upmt/)
- Context files (.context/)
- Bootstrap report
- Final setup instructions (UPMT_FINAL_STEPS.md)

**Проект оптимизирован для разработки!**
⏱️ PHASE 9 завершена за [время]
```

---

## 🔄 СЛЕДУЮЩИЙ ШАГ

```
🎉 BOOTSTRAP ПРОЦЕСС ЗАВЕРШЕН ПОЛНОСТЬЮ!

Проект готов к разработке. Следуй инструкциям в UPMT_FINAL_STEPS.md
для настройки AI ассистентов и начала работы.
```
