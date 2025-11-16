# 🎯 UPMT BOOTSTRAP ORCHESTRATOR

**Версия:** 3.0.1 (Модульная архитектура)  
**Дата:** 2025-11-14  
**Назначение:** Главный контроллер bootstrap процесса

---

## 📋 ЧТО ЭТО

Этот файл - **главный оркестратор** bootstrap процесса. Он:
- Определяет последовательность выполнения всех фаз
- Связывает модульные компоненты (фазы, адаптеры)
- Управляет checkpoint системой
- Обеспечивает принцип "снежного кома" (контекст между фазами)

---

## 🔧 АРХИТЕКТУРА СИСТЕМЫ

```
ORCHESTRATOR (этот файл)
    ↓
    ├── Читает: Адаптер (CLI или Web)
    ├── Читает: Параметры сценария
    └── Выполняет: Фазы 1-8 последовательно (+ PHASE 9 опционально)
        ↓
        ├── PHASE 1: Analysis        → prompts/phases/phase-1-analysis.md
        ├── PHASE 2: Interview       → prompts/phases/phase-2-interview.md
        ├── PHASE 3: Tech Verify     → prompts/phases/phase-3-tech-verification.md
        ├── PHASE 4: Synthesis       → prompts/phases/phase-4-synthesis.md
        ├── PHASE 5: Documentation   → prompts/phases/phase-5-documentation.md
        ├── PHASE 5.4: Figma Make Prompt (optional) → prompts/phases/phase-5.4-figma-prompt.md
        ├── PHASE 5.5: Design        → prompts/phases/phase-5.5-design.md
        ├── PHASE 5.7: Backend       → prompts/phases/phase-5.7-backend.md
        ├── PHASE 6: Setup           → prompts/phases/phase-6-setup.md
        ├── PHASE 7: Validation      → prompts/phases/phase-7-validation.md
        ├── PHASE 8: Report          → prompts/phases/phase-8-report.md
        └── PHASE 9: Cleanup         → prompts/phases/phase-9-cleanup.md (optional - запускается вручную)
```

---

## ⚙️ ПАРАМЕТРЫ СЦЕНАРИЯ

Параметры устанавливаются в алиасах (`UPMT/start/1.X.md`):

```yaml
scenario:
  name: "[CLI/Web] + [New/Existing] Project"
  code: "1.X"
  mode: "CLI" или "WEB_GITHUB"
  existing_project: true/false
  
data_sources:
  - raw_data: "UPMT/bootstrap/00_RAW_DATA_TEMPLATE/"
  - code_analysis: true/false
  - code_location: "../src, ../app" (если existing_project)
```

---

## 📖 ИНСТРУКЦИИ ПО ВЫПОЛНЕНИЮ

### Глобальные переменные даты (для динамических меток)

- Определи актуальный месяц и год выполнения и используй их во всех фазах/отчётах вместо статичных дат:
  ```python
  from datetime import datetime
  CURRENT_MONTH_YEAR = datetime.now().strftime("%B %Y")  # пример: "November 2025"
  ```
  
  Для русской локали (если доступна в окружении):
  ```python
  import locale
  try:
      locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
  except:
      pass  # fallback, если локаль недоступна
  CURRENT_MONTH_YEAR = datetime.now().strftime("%B %Y")  # пример: "ноябрь 2025"
  ```
  
  Всюду, где раньше встречались статичные строки вроде "November 2025"/"ноябрь 2025", используй плейсхолдер `{CURRENT_MONTH_YEAR}`.

### ШАГ 0: ИНИЦИАЛИЗАЦИЯ

**0.0: ЯЗЫК ОБЩЕНИЯ**

⚠️ **КРИТИЧНО:** ВСЕ сообщения пользователю должны быть на РУССКОМ ЯЗЫКЕ!

**Правила:**
- ✅ Все диалоги с пользователем → русский язык
- ✅ Все сообщения о прогрессе → русский язык  
- ✅ Все вопросы → русский язык
- ✅ Все отчеты → русский язык
- ⚠️ Только технические термины (git commit messages, file paths) могут быть на английском

**Примеры правильных сообщений:**
- ✅ "Отлично! Начинаю PHASE 1: ANALYSIS"
- ✅ "Я извлек 158 функций из ваших данных"
- ✅ "Жду вашего подтверждения перед продолжением"
- ✅ "📋 EXTRACTED FEATURES - СОГЛАСОВАНИЕ"

**Примеры НЕПРАВИЛЬНЫХ сообщений:**
- ❌ "Perfect! Starting PHASE 1"
- ❌ "I extracted 158 functions"
- ❌ "Waiting for your approval"
- ❌ "📋 EXTRACTED FEATURES - APPROVAL"

**⚠️ ВАЖНО:** Если ты начал общаться на английском, немедленно переключись на русский и продолжай на русском языке!

---

**0.0.0: Проверка Recovery Mode (КРИТИЧНО!)**

Перед началом любых действий проверь наличие незавершенного bootstrap.

**Алгоритм:**

1. Определи режим работы (`mode` из сценария: CLI, WEB_GITHUB, или CURSOR)

2. Вызови функцию проверки checkpoint:
   ```python
   checkpoint = check_for_incomplete_bootstrap(mode=mode)
   
   if checkpoint:
       # Проверка актуальности уже выполнена в функции
       checkpoint_age_hours = (now() - parse_datetime(checkpoint['timestamp'])).total_hours()
       
       if checkpoint_age_hours < 24 AND checkpoint['phase'] < 8:
           # Показать recovery dialog
           show_recovery_dialog(checkpoint)
           choice = ask_user("Resume (1), Start Fresh (2), View Details (3):")
           
           if choice == "1":
               resume_result = resume_from_checkpoint(checkpoint)
               
               if resume_result and resume_result.get("resume"):
                   # Определить следующую фазу для продолжения
                   current_phase = checkpoint['phase']
                   current_batch = checkpoint.get('batch')
                   
                   # Логика определения следующей фазы
                   if current_phase == 5 and current_batch:
                       # PHASE 5 в процессе - продолжить со следующего batch
                       next_phase = 5
                       next_batch = current_batch + 1
                   elif current_phase == 5 and not current_batch:
                       # PHASE 5 завершена - проверить PHASE 5.4 (Figma Make)
                       # Проверить, был ли выбран Figma Make в checkpoint
                       figma_make_selected = checkpoint.get('state', {}).get('figma_make_selected', False)
                       
                       if figma_make_selected:
                           # PHASE 5.4 была выбрана, но не завершена
                           next_phase = 5.4
                           next_batch = None
                       else:
                           # PHASE 5.4 не выбрана или пропущена - проверить conditional phases
                           # Проверить design data и existing_project
                           design_data_exists, _ = check_design_data_exists()
                           # Прочитать existing_project из metadata.yaml или checkpoint state
                           existing_project = checkpoint.get('state', {}).get('existing_project', False)
                           if not existing_project:
                               # Fallback: прочитать из metadata.yaml
                               try:
                                   metadata = read_yaml("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")
                                   existing_project = metadata.get('existing_project', {}).get('enabled', False)
                               except:
                                   existing_project = False
                           
                           if design_data_exists or existing_project:
                               next_phase = 5.5
                               next_batch = None
                           else:
                               # Проверить backend data
                               backend_data_exists, _ = check_backend_data_exists()
                               if backend_data_exists or existing_project:
                                   next_phase = 5.7
                                   next_batch = None
                               else:
                                   next_phase = 6
                                   next_batch = None
                   elif current_phase == 5.4:
                       # PHASE 5.4 завершена - проверить conditional phases
                       design_data_exists, _ = check_design_data_exists()
                       # Прочитать existing_project из metadata.yaml или checkpoint state
                       existing_project = checkpoint.get('state', {}).get('existing_project', False)
                       if not existing_project:
                           # Fallback: прочитать из metadata.yaml
                           try:
                               metadata = read_yaml("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")
                               existing_project = metadata.get('existing_project', {}).get('enabled', False)
                           except:
                               existing_project = False
                       
                       if design_data_exists or existing_project:
                           next_phase = 5.5
                           next_batch = None
                       else:
                           # Проверить backend data
                           backend_data_exists, _ = check_backend_data_exists()
                           if backend_data_exists or existing_project:
                               next_phase = 5.7
                               next_batch = None
                           else:
                               next_phase = 6
                               next_batch = None
                   else:
                       # Обычный переход к следующей фазе
                       next_phase = current_phase + 1
                       next_batch = None
                   
                   # Продолжить с определенной фазы
                   SKIP to PHASE {next_phase} (batch {next_batch} if applicable)
               else:
                   # Recovery failed - начать заново
                   archive_checkpoint(checkpoint, ".upmt/checkpoints/archive/")
                   delete_file(".upmt/checkpoints/latest.json")
                   # Начать bootstrap с PHASE 1
           elif choice == "3":
               show_detailed_recovery_status(checkpoint)
               # Повторить вопрос после показа деталей
               choice = ask_user("Resume (1), Start Fresh (2), View Details (3):")
               # Повторить логику выше для choice
           else:
               # choice == "2" - начать заново
               archive_checkpoint(checkpoint, ".upmt/checkpoints/archive/")
               delete_file(".upmt/checkpoints/latest.json")
               # Начать bootstrap с PHASE 1
   ```

4. Если checkpoint не найден или старый/завершенный:
   - Продолжай с ШАГ 0.1 (прочитай адаптер)

**Recovery Dialog формат:**

```
╔══════════════════════════════════════════════════════════════╗
║            НЕЗАВЕРШЕННЫЙ BOOTSTRAP ОБНАРУЖЕН                  ║
╚══════════════════════════════════════════════════════════════╝

⚠️  Найден checkpoint от: {checkpoint['timestamp']}
    Возраст: {checkpoint_age_hours} часов назад

📍 Последнее завершенное:
   Фаза: {checkpoint['phase_name']} (PHASE {checkpoint['phase']})
   Батч: {checkpoint['batch']} (если применимо)
   Файлов создано: {len(checkpoint['state']['files_created'])}
   Прогресс: {checkpoint['phase']}/8 фаз ({checkpoint['phase']/8*100}%)
   Время работы: {checkpoint['stats']['elapsed_time']}

🔄 Варианты действий:
   1. Продолжить с checkpoint (рекомендуется)
   2. Начать заново (удалить checkpoint)
   3. Показать детальный статус

Ваш выбор (1/2/3):
```

**Подробности функций:** См. `UPMT/prompts/utils/checkpoint-functions.md`

**Полная документация recovery:** См. `UPMT/prompts/utils/RECOVERY_PROTOCOL.md`

---

**0.1: Прочитай адаптер**

В зависимости от `mode`:
- `CLI` → Прочитай `UPMT/prompts/adapters/cli-adapter.md`
- `WEB_GITHUB` → Прочитай `UPMT/prompts/adapters/web-adapter.md`

Адаптер содержит специфичные инструкции для работы с файлами.

**0.2: Определи параметры сценария**

Используй параметры из алиаса (`UPMT/start/1.X.md`):
- `existing_project` определяет нужен ли code analysis
- `mode` определяет какой адаптер использовать

**0.3: Создай трекер прогресса**

⚠️ **КРИТИЧНО:** Используй Update Todos с ВСЕМИ фазами, включая conditional!

**ОБЯЗАТЕЛЬНЫЙ формат TODO (используй Update Todos tool):**

```markdown
Update Todos
 PHASE 1: Analysis - Read raw data and extract features
 PHASE 2: Interview - Ask clarifying questions
 PHASE 3: Tech Verification - Verify technologies (2025)
 PHASE 4: Synthesis - Create unified project view
 PHASE 5: Documentation - Generate all docs
 PHASE 5.4: Figma Make Prompt (optional)
 PHASE 5.5: Design System (conditional)
 PHASE 5.7: Backend Documentation (conditional)
 PHASE 6: Setup Instructions
 PHASE 7: Validation - Verify completeness
 PHASE 8: Final Report
```

**⚠️ ВАЖНО:**
- ✅ ВСЕГДА включай Phase 5.5 и 5.7 в TODO (даже если conditional)
- ✅ Не пропускай фазы в TODO
- ✅ Используй точные названия из списка выше
- ✅ Используй Update Todos tool, а не просто текст в сообщении

**Пример правильного использования:**

```python
# ✅ ПРАВИЛЬНО - используй Update Todos tool
Update Todos
 PHASE 1: Analysis - Read raw data and extract features
 PHASE 2: Interview - Ask clarifying questions
 PHASE 3: Tech Verification - Verify technologies (2025)
 PHASE 4: Synthesis - Create unified project view
 PHASE 5: Documentation - Generate all docs
 PHASE 5.4: Figma Make Prompt (optional)
 PHASE 5.5: Design System (conditional)
 PHASE 5.7: Backend Documentation (conditional)
 PHASE 6: Setup Instructions
 PHASE 7: Validation - Verify completeness
 PHASE 8: Final Report
```

**❌ НЕПРАВИЛЬНО:**
- Не создавай TODO без Phase 5.5 и 5.7
- Не пропускай фазы
- Не используй только текст без Update Todos tool

---

### ШАГ 1: ВЫПОЛНЕНИЕ ФАЗ

Выполняй фазы **СТРОГО ПОСЛЕДОВАТЕЛЬНО**:

#### PHASE 1: ANALYSIS

**Файл:** `UPMT/prompts/phases/phase-1-analysis.md`

**Что делает:**
- Читает raw data из `00_RAW_DATA_TEMPLATE/`
- (Если `existing_project: true`) Анализирует существующий код
- Извлекает ВСЕ функции → `extracted_features.md`
- **Показывает список пользователю → ЖДЁТ APPROVED**
- Создаёт `modules_list.md`

**Выход:**
- ✅ `extracted_features.md` (согласовано)
- ✅ `modules_list.md`
- ✅ `analysis-report.md`

**Checkpoint:** Коммит после согласования

**CLI mode:**
```bash
git commit -m "docs(bootstrap): PHASE 1 complete - extracted X features, Y modules"
git push
```

**Web mode (GitHub API):**
- ✅ Каждый PUT request автоматически создаёт коммит
- ✅ Commit message указывается в `-f message="..."`
- ✅ Checkpoint сохраняется через `save_checkpoint_github()` (создаст коммит)
- ✅ НЕ используй `git commit` или `git push` (это CLI команды!)
- **См. также:** `UPMT/prompts/adapters/web-adapter.md` - секция "💾 GITHUB API COMMITS"

---

#### PHASE 2: INTERVIEW

**Файл:** `UPMT/prompts/phases/phase-2-interview.md`

**Контекст (читай перед phase):**
- `extracted_features.md`
- `modules_list.md`

**Что делает:**
- Показывает summary findings
- Задаёт 5-10 уточняющих вопросов
- AUTO-FILL `metadata.yaml`

**Выход:**
- ✅ `metadata.yaml` (заполнен)
- ✅ Ответы пользователя (в контексте)

**Checkpoint:** Коммит после interview

**CLI mode:**
```bash
git commit -m "docs(bootstrap): PHASE 2 complete - interview finished, metadata filled"
git push
```

**Web mode (GitHub API):**
- ✅ Файлы коммитятся автоматически при создании/обновлении через PUT
- ✅ Checkpoint через `save_checkpoint_github()` создаст коммит

---

#### PHASE 3: TECH VERIFICATION

**Файл:** `UPMT/prompts/phases/phase-3-tech-verification.md`

**Контекст:**
- `metadata.yaml`
- `extracted_features.md`

**Что делает:**
- Анализирует упоминания технологий
- Создаёт verification prompt
- **PAUSE - ждёт user action (web search)**
- Читает результат analysis
- Создаёт `final-tech-stack.md`

**Выход:**
- ✅ `/verification/VERIFICATION_PROMPT_FOR_CLAUDE.md`
- ✅ `/verification/tech-stack-analysis.md` (user создаёт)
- ✅ `/verification/final-tech-stack.md`

**Checkpoint:** Коммит после tech approval

```bash
git commit -m "docs(bootstrap): PHASE 3 complete - tech stack verified"
```

---

#### PHASE 4: SYNTHESIS

**Файл:** `UPMT/prompts/phases/phase-4-synthesis.md`

**Контекст (читай перед phase):**
- `extracted_features.md`
- `modules_list.md`
- `metadata.yaml`
- `tech-stack-analysis.md`
- `final-tech-stack.md`

**Что делает:**
- Объединяет все данные в unified view
- Создаёт `synthesized-project-data.md`

**Выход:**
- ✅ `/synthesized-project-data.md`

**Checkpoint:** Коммит

```bash
git commit -m "docs(bootstrap): PHASE 4 complete - synthesized unified view"
```

---

#### PHASE 5: DOCUMENTATION GENERATION

**Файл:** `UPMT/prompts/phases/phase-5-documentation.md`

**⚠️ САМАЯ БОЛЬШАЯ ФАЗА - 2-4 часа**

**Контекст (читай перед phase):**
- `synthesized-project-data.md`
- `extracted_features.md`
- `modules_list.md`
- `metadata.yaml`

**Что делает:**
- Создаёт `docs/core/` (6 файлов)
- Создаёт `docs/requirements/` (по файлу на каждый модуль из `modules_list.md`)
- Создаёт `.context/` (4 файла)
- Создаёт `docs/progress/` (3 файла)
- Создаёт `.upmt/metadata.yaml` и `.cursorrules`

**⚠️ ДИНАМИЧЕСКОЕ СОЗДАНИЕ MODULE REQUIREMENTS:**

Алгоритм:
```
1. Прочитай modules_list.md
2. Посчитай количество модулей: TOTAL_MODULES
3. Разбей на батчи по 6 модулей:
   BATCH_SIZE = 6
   BATCHES = ceil(TOTAL_MODULES / BATCH_SIZE)

4. Для каждого батча:
   FOR batch in 1..BATCHES:
     module_start = (batch - 1) * 6 + 1
     module_end = min(batch * 6, TOTAL_MODULES)
     
     Создай requirements для модулей [module_start..module_end]
     
     CHECKPOINT: Коммит батча
     git commit -m "docs(bootstrap): PHASE 5 batch {batch}/{BATCHES} - modules {module_start}-{module_end}"
     
     ПОКАЗАТЬ ПРОГРЕСС:
     "✅ PHASE 5: Batch {batch}/{BATCHES} complete"
     "→ Created requirements for modules {module_start}-{module_end}"
     "→ Remaining: {TOTAL_MODULES - module_end} modules"

5. После всех батчей:
   FINAL CHECKPOINT
```

**Выход:**
- ✅ `docs/core/00_PROJECT_ESSENCE.md`
- ✅ `docs/core/01_PRD.md`
- ✅ `docs/core/02_ROADMAP.md`
- ✅ `docs/core/03_TECH_STACK.md`
- ✅ `docs/core/04_ARCHITECTURE.md`
- ✅ `docs/core/99_SYSTEM_GUIDE.md`
- ✅ `docs/requirements/[module_name]_requirements.md` (для КАЖДОГО модуля)
- ✅ `.context/state.md`, `decisions.md`, `insights.md`, `changes_log.md`
- ✅ `docs/progress/modules_status.md`, `sprint_current.md`, `backlog.md`
- ✅ `.upmt/metadata.yaml`
- ✅ `.cursorrules`

**Checkpoint:** Коммит после каждого батча + финальный коммит

```bash
# После каждого батча
git commit -m "docs(bootstrap): PHASE 5 batch {X}/{Y} - modules {start}-{end}"

# Финальный
git commit -m "docs(bootstrap): PHASE 5 complete - full documentation generated"
```

---

#### PHASE 5.4: FIGMA MAKE PROMPT (OPTIONAL)

**Файл:** `UPMT/prompts/phases/phase-5.4-figma-prompt.md`

**⚠️ ОПЦИОНАЛЬНАЯ ФАЗА - спрашивает пользователя:**
"Хочешь сгенерировать визуальный прототип через Figma Make?"

**Если YES:**
- Генерирует базовый промпт из Raw Data (локально)
- Создаёт промпт для Claude Web (dual prompting)
- Пользователь работает с Claude Web → получает улучшенные промты
- Сохраняет промты в `00_DESIGN_RAW_DATA/figma-make/`
- Инструктирует пользователя работать с Figma Make
- Ждёт экспорта результатов

**Если NO:**
- SKIP → переход к PHASE 5.5

**Выход:**
- ✅ `FIGMA_MAKE_PROMPT_base.md` (локально сгенерированный)
- ✅ `global_prompt.md` (улучшенный Claude Web)
- ✅ `module_prompts/{module}.md` (per-module промты)
- ✅ `iterations/{module}_steps.md` (итерационные промты)
- ✅ Инструкции для пользователя

**User Action Required:**
1. Работа с Claude Web (10-20 минут) - улучшение промтов
2. Работа с Figma Make (2-3 часа) → Export в 00_DESIGN_RAW_DATA/

**Checkpoint:** Коммит после генерации промтов

**CLI mode:**
```bash
git commit -m "docs(bootstrap): PHASE 5.4 complete - Figma Make prompts generated (base + Claude Web enhanced)"
git push
```

**Web mode (GitHub API):**
- ✅ Каждый PUT request автоматически создаёт коммит
- ✅ Checkpoint через `save_checkpoint_github()` создаст коммит

**После User Action:**
→ Переход к PHASE 5.5 (которая обработает Figma exports)

---

#### PHASE 5.5: DESIGN SYSTEM (CONDITIONAL)

**Файл:** `UPMT/prompts/phases/phase-5.5-design.md`

**⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ:**

```
IF (design_data_exists OR existing_project):
    EXECUTE PHASE 5.5
ELSE:
    SKIP → ПЕРЕХОД К PHASE 5.7
```

**⚠️ КРИТИЧНО: Правильная проверка `design_data_exists`**

```python
def check_design_data_exists():
    """
    Проверяет наличие design raw data в 00_DESIGN_RAW_DATA/.
    Returns: (exists: bool, details: dict)
    """
    print("\n🔍 Checking for design raw data...\n")
    
    design_folders = {
        "chats": "00_DESIGN_RAW_DATA/chats/",
        "moodboards": "00_DESIGN_RAW_DATA/moodboards/",
        "figma": "00_DESIGN_RAW_DATA/figma/",
        "screenshots": "00_DESIGN_RAW_DATA/screenshots/",
        "research": "00_DESIGN_RAW_DATA/research/",
        "brand": "00_DESIGN_RAW_DATA/brand/"
    }
    
    found_files = {}
    total_files = 0
    
    for category, folder in design_folders.items():
        # Список файлов в папке
        all_files = list_files(folder)
        
        # Исключаем README и _example файлы
        actual_files = [f for f in all_files 
                       if not f.startswith("README") 
                       and not f.startswith("_example")]
        
        found_files[category] = actual_files
        total_files += len(actual_files)
        
        if actual_files:
            print(f"   ✅ {folder}: {len(actual_files)} files")
            for file in actual_files[:3]:  # Показываем первые 3
                print(f"      - {file}")
            if len(actual_files) > 3:
                print(f"      ... and {len(actual_files) - 3} more")
        else:
            print(f"   ⚠️ {folder}: empty (only README)")
    
    if total_files > 0:
        print(f"\n✅ Design data DETECTED: {total_files} files total")
        print(f"   → PHASE 5.5 (Design System) WILL BE EXECUTED\n")
        return (True, {
            "total_files": total_files,
            "files_by_category": found_files
        })
    else:
        print(f"\nℹ️ No design data found (only README files)")
        print(f"   → PHASE 5.5 (Design System) WILL BE SKIPPED\n")
        return (False, {})

# В orchestrator ПЕРЕД PHASE 5.5:
design_data_exists, design_details = check_design_data_exists()

# Conditional execution
if design_data_exists OR existing_project:
    print("✅ PHASE 5.5: EXECUTING (design data found or existing project)")
    execute_phase_5_5()
else:
    print("ℹ️ PHASE 5.5: SKIPPED (no design data, new project)")
    skip_to_phase_5_7()
```

**Контекст:**
- `modules_list.md`
- Existing code (если есть)
- Design raw data (если есть) - **ПРОВЕРЯЕТСЯ ФУНКЦИЕЙ ВЫШЕ**
- Параметры сценария (`scenario.existing_project`)

**Структура выполнения:**

**ШАГ 0:** Проверка параметров и условий
- Проверь `scenario.existing_project` из алиаса
- **Выполни `check_design_data_exists()` для проверки design raw data**
- Покажи результаты проверки пользователю

**ШАГИ 1-4:** Общие для всех сценариев
- ШАГ 1: Анализ Design Data (raw data + code если existing)
- ШАГ 2: Создание Design System Structure
- ШАГ 3: Заполнение Foundation (разный контент для new/existing)
- ШАГ 4: Components Documentation (разный подход для new/existing)

**ШАГИ 6-10:** ТОЛЬКО для `existing_project == true`
- ШАГ 6: Patterns - ЧТО ИСПОЛЬЗУЕТСЯ
- ШАГ 7: Content Guidelines - ТЕКУЩИЙ STYLE
- ШАГ 8: Accessibility - CURRENT STATE
- ШАГ 9: User Research (если есть)
- ШАГ 10: Resources & Tokens - Извлечение из кода

**ШАГИ 11-14:** Общие для всех сценариев
- ШАГ 11: Resources & Tokens (для new) / Skip (для existing)
- ШАГ 12: Integration with Module Requirements
- ШАГ 13: Design Questions (разные вопросы для new/existing)
- ШАГ 14: Finalize & Validate

**Логика выполнения:**
```
IF existing_project == true:
    Выполни ШАГИ 1-4, затем ШАГИ 6-10, затем ШАГИ 11-14 (все шаги)
ELSE:
    Выполни ШАГИ 1-4, затем SKIP 6-10, затем ШАГИ 11-14
```

**Что делает:**
- Анализирует design из кода (если existing project)
- Читает design raw data
- Создаёт `docs/design/` (foundation, components, patterns, accessibility)
- Документирует существующие patterns и accessibility state (если existing)

**Выход:**
- ✅ `docs/design/` (полная структура)
- ✅ Patterns documented (если existing)
- ✅ Accessibility audit (если existing)

**Checkpoint:** Коммит

```bash
git commit -m "docs(bootstrap): PHASE 5.5 complete - design system documented"
```

---

#### PHASE 5.7: BACKEND DOCUMENTATION (CONDITIONAL)

**Файл:** `UPMT/prompts/phases/phase-5.7-backend.md`

**⚠️ УСЛОВНОЕ ВЫПОЛНЕНИЕ:**

```
IF (backend_detected):
    EXECUTE PHASE 5.7
ELSE:
    SKIP → ПЕРЕХОД К PHASE 6
```

**Триггеры:**
- Backend упомянут в raw data
- Tech stack содержит backend framework
- Тип проекта требует backend

**Что делает:**
- Анализирует backend requirements
- Создаёт `docs/backend/` (entities, api, services, database)
- Создаёт `docs/adr/` (architecture decisions)

**Выход:**
- ✅ `docs/backend/` (entities, api, services, database)
- ✅ `docs/adr/` (минимум 3 ADR)

**Checkpoint:** Коммит

```bash
git commit -m "docs(bootstrap): PHASE 5.7 complete - backend documented"
```

---

#### PHASE 6: FINAL SETUP INSTRUCTIONS

**Файл:** `UPMT/prompts/phases/phase-6-setup.md`

**Контекст:**
- `.upmt/metadata.yaml`
- `docs/core/03_TECH_STACK.md`
- `.cursorrules`

**Что делает:**
- Создаёт `FINAL_SETUP_INSTRUCTIONS.md`
- Инструкции по настройке AI ассистентов

**Выход:**
- ✅ `UPMT/bootstrap/BOOTSTRAP_CONFIG/FINAL_SETUP_INSTRUCTIONS.md`

**Checkpoint:** Коммит

```bash
git commit -m "docs(bootstrap): PHASE 6 complete - setup instructions"
```

---

#### PHASE 7: VALIDATION

**Файл:** `UPMT/prompts/phases/phase-7-validation.md`

**⚠️ КРИТИЧЕСКАЯ ФАЗА - ПРОВЕРКА 100% ПОЛНОТЫ**

**Что делает:**
- Проверяет что ВСЕ файлы созданы
- Проверяет что ВСЕ функции учтены
- Проверяет что файлы НЕ templates (заполнены реальными данными)
- Cross-references работают

**Выход:**
- ✅ Validation report (в логе)

**Если validation failed:**
- Возврат к нужной фазе
- Исправление
- Повтор validation

**Checkpoint:** Коммит validation report

```bash
git commit -m "docs(bootstrap): PHASE 7 complete - validation passed"
```

---

#### PHASE 8: FINAL REPORT

**Файл:** `UPMT/prompts/phases/phase-8-report.md`

**Что делает:**
- Создаёт `BOOTSTRAP_REPORT.md`
- Копирует `FINAL_SETUP_INSTRUCTIONS.md` → `UPMT_FINAL_STEPS.md` в корень проекта
- Summary всего процесса
- Рекомендации next steps

**Выход:**
- ✅ `BOOTSTRAP_REPORT.md`
- ✅ `UPMT_FINAL_STEPS.md` в корне проекта

**Checkpoint:** Финальный коммит

```bash
git commit -m "docs(bootstrap): PHASE 8 complete - bootstrap finished! 🎉"
```

---

#### PHASE 9: PROJECT CLEANUP

**Файл:** `UPMT/prompts/phases/phase-9-cleanup.md`

**Что делает:**
- Проверяет наличие `UPMT_FINAL_STEPS.md` (создан в PHASE 8)
- Удаляет временные файлы bootstrap
- Оптимизирует структуру проекта для разработки
- Оставляет только нужные файлы

**Выход:**
- ✅ Очищенный проект

**Checkpoint:** Финальный коммит очистки

```bash
git commit -m "cleanup(bootstrap): PHASE 9 complete - project cleanup finished"
```

---

## 🔄 CHECKPOINT СИСТЕМА

**Правила:**

1. **После каждой фазы** - коммит
2. **PHASE 5: После каждого батча модулей** - коммит
3. **После критических согласований** (extracted_features APPROVED, tech stack approved) - коммит

**Формат commit message:**

```
docs(bootstrap): PHASE X [название] - [краткое описание]

- Создано: [N файлов]
- Обновлено: [M файлов]
- Следующая фаза: PHASE X+1
```

**⚠️ ВАЖНО: Разница между CLI и Web mode:**

**CLI mode:**
```bash
git add .
git commit -m "docs(bootstrap): PHASE X complete - ..."
git push
```

**Web mode (GitHub API):**
- ✅ Каждый `PUT` request автоматически создаёт коммит
- ✅ Commit message указывается в параметре `-f message="..."`
- ✅ НЕ используй `git commit` или `git push` (это CLI команды!)
- ✅ Checkpoint через `save_checkpoint_github()` создаст коммит автоматически
- ✅ Все файлы коммитятся при создании/обновлении через API
- **См. также:** `UPMT/prompts/adapters/web-adapter.md` - секция "💾 GITHUB API COMMITS"

**Retry Logic (если push failed - только для CLI mode):**

```
IF push_failed:
    WAIT 30 seconds
    RETRY push (max 3 attempts)
    
    IF still_failed:
        ALERT USER
        SAVE STATE to .bootstrap-state.json
        PAUSE
```

**Для Web mode:**
- Если PUT request failed - GitHub API вернёт ошибку
- Повтори PUT request (max 3 attempts)
- Если всё ещё failed - ALERT USER и сохрани checkpoint

---

## 📊 PROGRESS TRACKING

**Каждые 30 минут** показывай прогресс:

```markdown
⏱️ BOOTSTRAP PROGRESS UPDATE

**Текущая фаза:** PHASE X - [название]
**Прогресс:** [X%] (X/8 фаз завершено)
**Время работы:** [HH:MM]

**Последние действия:**
- ✅ [действие 1]
- ✅ [действие 2]
- 🔄 [текущее действие]

**Следующие шаги:**
- [ ] [следующее действие]

**Checkpoint commits:** [N коммитов]
```

---

## ⚠️ ПРИНЦИП "СНЕЖНОГО КОМА"

Данные из предыдущих фаз ОБЯЗАТЕЛЬНО используются в следующих:

```
PHASE 1 → extracted_features.md, modules_list.md
           ↓
PHASE 2 → (использует extracted_features, modules_list) → metadata.yaml
           ↓
PHASE 3 → (использует metadata) → final-tech-stack.md
           ↓
PHASE 4 → (использует ВСЁ выше) → synthesized-project-data.md
           ↓
PHASE 5 → (использует synthesized-project-data, extracted_features, modules_list) → docs/*
           ↓
PHASE 6 → (использует metadata, tech stack, .cursorrules) → FINAL_SETUP_INSTRUCTIONS.md
           ↓
PHASE 7 → (проверяет ВСЁ созданное)
           ↓
PHASE 8 → (итоговый отчёт)
```

**Перед каждой фазой:**
- Проверь список контекстных файлов в описании фазы
- Прочитай их ВСЕ перед выполнением фазы
- Используй данные из них

---

## 🚨 КРИТИЧЕСКИЕ ПРАВИЛА

1. **НЕ ПРОПУСКАЙ ФАЗЫ** - выполняй строго последовательно
2. **НЕ ПРОПУСКАЙ CHECKPOINT** - коммит после каждой фазы
3. **НЕ ПРОПУСКАЙ СОГЛАСОВАНИЕ** - ждёт APPROVED от пользователя
4. **НЕ ПРОПУСКАЙ ФУНКЦИИ** - ВСЕ функции из extracted_features должны быть в requirements
5. **НЕ ОСТАВЛЯЙ TEMPLATES** - все файлы должны быть заполнены реальными данными
6. **ИСПОЛЬЗУЙ АДАПТЕР** - CLI или Web, в зависимости от сценария
7. **ДИНАМИЧЕСКИЕ МОДУЛИ** - количество модулей читай из `modules_list.md`, не хардкодь

---

## 📚 ССЫЛКИ НА ФАЙЛЫ

- **Фазы:** `UPMT/prompts/phases/phase-X-*.md`
- **Адаптеры:** `UPMT/prompts/adapters/cli-adapter.md`, `web-adapter.md`
- **Алиасы:** `UPMT/start/1.X.md`
- **Полные сценарии:** `UPMT/prompts/scenarios/1.X-*.md`

---

## 🎯 НАЧАЛО РАБОТЫ

**Ты вызван из алиаса (`UPMT/start/1.X.md`)**

1. ✅ Параметры сценария установлены
2. ✅ Адаптер прочитан
3. ✅ Оркестратор прочитан (ты здесь)

**Следующий шаг:**

```
→ НАЧИНАЙ PHASE 1: ANALYSIS
→ Прочитай: UPMT/prompts/phases/phase-1-analysis.md
```

**НАЧИНАЙ! 🚀**

