# 🖥️ CLI ADAPTER - Локальная работа

**Назначение:** Специфичные инструкции для работы в локальном окружении (CLI/Cursor)

---

## 📁 ФАЙЛОВЫЕ ОПЕРАЦИИ

### Чтение файлов

**Используй стандартные инструменты:**

```python
# Прочитай файл
read_file("path/to/file.md")

# Прочитай папку
list_dir("path/to/directory")

# Поиск файлов
glob_file_search("**/*.md", target_directory="path")
```

**Примеры:**

```python
# Читай raw data
read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml")
read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/chat1.txt")

# Читай существующий код (если existing project)
list_dir("../src")
read_file("../src/index.ts")
read_file("../package.json")
```

**⚠️ ОБРАБОТКА БОЛЬШИХ ФАЙЛОВ:**

**Алгоритм автоматического чтения (ИСПОЛЬЗУЙ ВСЕГДА):**

```python
def safe_read_file(file_path):
    """
    Читает файл целиком или по частям, если большой.
    АВТОМАТИЧЕСКИ обрабатывает ошибки размера.
    """
    try:
        # Попытка прочитать целиком
        return read_file(file_path)
    except (FileTooLargeError, TokenLimitExceededError) as e:
        # Файл большой - читай по частям
        print(f"⚠️ Файл {file_path} слишком большой, читаю по частям...")
        
        # 1. Определи размер файла (строки)
        # CLI: wc -l "file_path" или используй grep для подсчета строк
        line_count = get_line_count(file_path)  # Используй wc -l или grep -c
        
        # 2. Читай порциями по 2000 строк (безопасный размер)
        chunks = []
        chunk_size = 2000
        
        for start_line in range(1, line_count + 1, chunk_size):
            end_line = min(start_line + chunk_size - 1, line_count)
            limit = end_line - start_line + 1
            
            chunk = read_file(
                file_path=file_path,
                offset=start_line,
                limit=limit
            )
            chunks.append(chunk)
            
            # Логируй прогресс
            print(f"📖 Прочитано {end_line}/{line_count} строк из {file_path}")
        
        # 3. Объедини все порции
        full_content = "\n".join(chunks)
        print(f"✅ Файл {file_path} прочитан полностью ({line_count} строк)")
        return full_content

# Использование:
content = safe_read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/large_chat.txt")
```

**Если получил ошибку:**
- `File content (XXX KB) exceeds maximum allowed size (256KB)`
- `File content (XXXXX tokens) exceeds maximum allowed tokens (25000)`

**ТОГДА:**

1. **Определи размер файла:**
```bash
wc -l "path/to/file.txt"
# Результат: 6222 строки
```

2. **Читай по частям (по 2000 строк):**
```python
# Порция 1: строки 1-2000
chunk1 = read_file("path/to/file.txt", offset=1, limit=2000)

# Порция 2: строки 2001-4000
chunk2 = read_file("path/to/file.txt", offset=2001, limit=2000)

# Порция 3: строки 4001-6222
chunk3 = read_file("path/to/file.txt", offset=4001, limit=2222)

# Объедини
full_content = "\n".join([chunk1, chunk2, chunk3])
```

3. **Используй полное содержимое для анализа**

**Примеры с автоматической обработкой:**

```python
# Читай raw data (с автоматической обработкой больших файлов)
for chat_file in list_dir("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/"):
    content = safe_read_file(f"UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/{chat_file}")
    # Анализируй content
```

**⚠️ КРИТИЧНО:**
- ВСЕГДА используй `safe_read_file()` вместо `read_file()` для файлов из raw data
- НЕ ПРОПУСКАЙ файлы из-за размера
- Автоматически читай большие файлы по частям
- Объединяй все части перед анализом

---

### Создание файлов

**Используй write tool:**

```python
write(
    file_path="docs/core/00_PROJECT_ESSENCE.md",
    contents="[полное содержимое файла]"
)
```

**⚠️ ВАЖНО:**
- Всегда пиши ПОЛНОЕ содержимое файла
- Не используй placeholders типа `[...]` или `// ... more content`
- Если файл большой - пиши полностью, это важно

---

### Обновление файлов

**Используй search_replace:**

```python
search_replace(
    file_path="docs/core/01_PRD.md",
    old_string="[старый текст]",
    new_string="[новый текст]",
    replace_all=False  # или True для замены всех вхождений
)
```

---

## 📂 СТРУКТУРА ПРОЕКТА

**Локальная структура:**

```
project-root/
├── UPMT/                          # Шаблонная система (этот проект)
│   ├── bootstrap/
│   │   └── 00_RAW_DATA_TEMPLATE/  # Raw data здесь
│   ├── prompts/                   # Модульные промпты
│   └── START.md                   # Главное меню
│
├── docs/                          # Создаваемая документация
│   ├── core/
│   ├── requirements/
│   ├── progress/
│   ├── design/
│   └── backend/
│
├── .context/                      # Контекст проекта
├── .upmt/                         # Метаданные
└── .cursorrules                   # AI правила
```

**Если existing project:**

```
project-root/
├── UPMT/                          # Шаблон
├── docs/                          # Документация (создаётся)
├── src/                           # Существующий код (читать)
├── app/                           # Существующий код (читать)
├── components/                    # Существующий код (читать)
└── package.json                   # Зависимости (читать)
```

---

## 🔍 CODE ANALYSIS (для existing projects)

**Алгоритм анализа:**

```python
# 1. Найди код
code_dirs = ["../src", "../app", "../components", "../backend", "../frontend"]
for dir in code_dirs:
    if exists(dir):
        list_dir(dir)

# 2. Читай ключевые файлы
read_file("../package.json")        # Зависимости
read_file("../tsconfig.json")       # TypeScript config
read_file("../README.md")           # Project overview

# 3. Анализируй структуру
list_dir("../src")
for module in modules:
    list_dir(f"../src/{module}")
    # Читай ключевые файлы модуля

# 4. Извлеки features из кода
grep(pattern="function|class|export", path="../src")
```

**Что извлекать:**
- ✅ Tech stack (из `package.json`, imports)
- ✅ Реализованные модули (из структуры папок)
- ✅ Реализованные функции (из кода)
- ✅ Архитектурные паттерны (из структуры)
- ✅ Версии зависимостей

---

## 💾 CHECKPOINT ОПЕРАЦИИ (CLI)

**Назначение:** Сохранение и чтение checkpoint для recovery системы.

### Сохранение checkpoint

**⚠️ КРИТИЧНО: Checkpoint ДОЛЖЕН быть сохранен после КАЖДОЙ фазы и КАЖДОГО batch!**

**После каждой фазы и батча (PHASE 5) вызывай (ОБЯЗАТЕЛЬНО!):**

```python
def save_checkpoint_cli(phase_number, phase_name, batch=None, state={}):
    """
    Сохраняет checkpoint в JSON файлы для восстановления.
    
    Параметры:
    - phase_number: номер фазы (1-8)
    - phase_name: название фазы (например, "PHASE 1: Analysis")
    - batch: номер батча (опционально, для PHASE 5)
    - state: объект с текущим состоянием
    """
    import json
    import os
    from datetime import datetime
    
    # 1. Создать директорию
    os.makedirs(".upmt/checkpoints", exist_ok=True)
    
    # 2. Собрать checkpoint данные
    checkpoint = {
        "phase": phase_number,
        "phase_name": phase_name,
        "batch": batch,
        "timestamp": datetime.now().isoformat(),
        "session_id": f"cli-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "mode": "CLI",
        "state": state,
        "stats": {
            "total_files": count_files_in_directory("docs/"),
            "total_lines": count_total_lines_in_directory("docs/"),
            "elapsed_time": calculate_elapsed_time_from_start()
        },
        "next_action": determine_next_action(phase_number, batch, existing_project=False)
    }
    
    # 3. Сохранить latest.json (перезапись)
    with open(".upmt/checkpoints/latest.json", "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)
    
    # 4. Сохранить архивную копию
    checkpoint_name = f"phase-{phase_number}"
    if batch:
        checkpoint_name += f"-batch-{batch}"
    checkpoint_name += ".json"
    
    with open(f".upmt/checkpoints/{checkpoint_name}", "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)
    
    # 5. Логирование
    print(f"💾 Checkpoint saved: {phase_name}" + 
          (f" (batch {batch})" if batch else ""))
    print(f"   Files: {checkpoint['stats']['total_files']}, " +
          f"Time: {checkpoint['stats']['elapsed_time']}")


# Вспомогательные функции:

def count_files_in_directory(directory):
    """Подсчет файлов в директории (рекурсивно)."""
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count


def calculate_elapsed_time_from_start():
    """
    Вычисляет время с момента запуска bootstrap.
    Примечание: start_time должен быть сохранен в первом checkpoint.
    """
    # Попытка прочитать первый checkpoint для start_time
    if os.path.exists(".upmt/checkpoints/phase-1.json"):
        with open(".upmt/checkpoints/phase-1.json", "r") as f:
            first_checkpoint = json.load(f)
            start_time = datetime.fromisoformat(first_checkpoint['timestamp'])
    else:
        # Если первого checkpoint нет, используем текущее время
        start_time = datetime.now()
    
    current_time = datetime.now()
    delta = current_time - start_time
    
    hours = int(delta.total_seconds() // 3600)
    minutes = int((delta.total_seconds() % 3600) // 60)
    seconds = int(delta.total_seconds() % 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def determine_next_action(phase_number, batch=None):
    """Определяет следующее действие."""
    actions = {
        1: "Continue to PHASE 2: Interview",
        2: "Continue to PHASE 3: Tech Verification",
        3: "Continue to PHASE 4: Synthesis",
        4: "Continue to PHASE 5: Documentation",
        5: {
            "with_batch": f"Continue PHASE 5: batch {batch + 1}",
            "no_batch": "Continue to PHASE 5.5 or 5.7 (conditional)"
        },
        6: "Continue to PHASE 7: Validation",
        7: "Continue to PHASE 8: Final Report",
        8: "Bootstrap complete - ready for development"
    }
    
    if phase_number == 5 and batch:
        return actions[5]["with_batch"]
    elif phase_number == 5:
        return actions[5]["no_batch"]
    else:
        return actions.get(phase_number, "Unknown phase")
```

**Пример вызова после PHASE 1:**

```python
save_checkpoint_cli(
    phase_number=1,
    phase_name="PHASE 1: Analysis",
    batch=None,
    state={
        "current_action": "Extracted features and modules",
        "files_created": [
            "UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md",
            "UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md",
            "analysis-report.md"
        ],
        "context_files": [
            "extracted_features.md",
            "modules_list.md"
        ]
    }
)
```

**Пример вызова после PHASE 5, batch 2:**

```python
save_checkpoint_cli(
    phase_number=5,
    phase_name="PHASE 5: Documentation",
    batch=2,
    state={
        "current_action": "Generating requirements for modules",
        "modules_completed": ["Dashboard", "User Profile", "Settings"],
        "total_modules": 8,
        "current_module": "Authentication",
        "files_created": [
            "docs/requirements/dashboard.md",
            "docs/requirements/user-profile.md",
            "docs/requirements/settings.md"
        ]
    }
)
```

### Чтение checkpoint

**Для проверки наличия незавершенного bootstrap:**

```python
def read_checkpoint_cli():
    """
    Читает последний checkpoint.
    Возвращает checkpoint объект или None.
    """
    import json
    import os
    
    checkpoint_file = ".upmt/checkpoints/latest.json"
    
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    return None


# Использование в orchestrator.md ШАГ 0.0.0:
checkpoint = read_checkpoint_cli()

if checkpoint:
    # Показать recovery dialog
    show_recovery_dialog(checkpoint)
else:
    # Начать bootstrap с PHASE 1
    start_fresh_bootstrap()
```

**Подробная документация:** См. `UPMT/prompts/utils/checkpoint-functions.md`

---

## 💾 GIT ОПЕРАЦИИ

**Checkpoint коммиты:**

```bash
# После каждой фазы
git add .
git commit -m "docs(bootstrap): PHASE X complete - [описание]"
git push
```

**Batch commits (PHASE 5):**

```bash
# После каждого батча модулей
git add docs/requirements/
git commit -m "docs(bootstrap): PHASE 5 batch {X}/{Y} - modules {start}-{end}"
git push
```

**⚠️ RETRY LOGIC если push failed:**

```python
def safe_push(max_retries=3):
    for attempt in range(max_retries):
        try:
            git push
            return True
        except NetworkError:
            if attempt < max_retries - 1:
                wait(30)  # 30 секунд
                retry
            else:
                alert_user("Push failed after 3 attempts")
                save_state(".bootstrap-state.json")
                return False
```

---

## 📊 ПРОГРЕСС TRACKING

**Показывай прогресс каждые 30 минут:**

```markdown
⏱️ BOOTSTRAP PROGRESS UPDATE

**Текущая фаза:** PHASE X - [название]
**Прогресс:** [X%]
**Время работы:** [HH:MM]

**Последние действия:**
- ✅ Создано docs/core/00_PROJECT_ESSENCE.md
- ✅ Создано docs/core/01_PRD.md
- 🔄 Создаю docs/requirements/module_1_requirements.md

**Следующие шаги:**
- [ ] Создать requirements для модуля 2
- [ ] ...

**Checkpoint commits:** 5
```

---

## 🚨 КРИТИЧЕСКИЕ ПРАВИЛА CLI

1. **НЕ ИСПОЛЬЗУЙ TERMINAL ДЛЯ ЧТЕНИЯ ФАЙЛОВ**
   - ❌ `cat file.md`
   - ✅ `read_file("file.md")`

2. **НЕ ИСПОЛЬЗУЙ TERMINAL ДЛЯ СОЗДАНИЯ ФАЙЛОВ**
   - ❌ `echo "content" > file.md`
   - ✅ `write("file.md", "content")`

3. **ИСПОЛЬЗУЙ СПЕЦИАЛИЗИРОВАННЫЕ ИНСТРУМЕНТЫ**
   - ✅ `read_file` - для чтения
   - ✅ `write` - для создания
   - ✅ `search_replace` - для обновления
   - ✅ `list_dir` - для просмотра структуры
   - ✅ `glob_file_search` - для поиска

4. **GIT OPERATIONS - ТОЛЬКО ЧЕРЕЗ TERMINAL**
   - ✅ `git add`, `git commit`, `git push`
   - ❌ Никакие другие операции

5. **ПИШИ ПОЛНЫЕ ФАЙЛЫ**
   - Не используй `[...]` или placeholders
   - Не используй `// ... rest of content`
   - Пиши всё полностью

---

## 💡 ПРИМЕРЫ

### Пример: Создание module requirements

```python
# 1. Прочитай context
modules = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")
features = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md")

# 2. Посчитай модули
total_modules = count_modules(modules)

# 3. Создай requirements для каждого модуля
for i, module in enumerate(modules, start=1):
    module_name = module["name"]
    module_features = filter_features(features, module_name)
    
    requirements_content = generate_requirements(module, module_features)
    
    write(
        file_path=f"docs/requirements/{module_name}_requirements.md",
        contents=requirements_content
    )
    
    # Checkpoint после каждых 6 модулей
    if i % 6 == 0:
        git_commit(f"docs(bootstrap): PHASE 5 batch {i//6} - modules {i-5}-{i}")

# 4. Финальный commit
git_commit("docs(bootstrap): PHASE 5 complete - all module requirements")
```

### Пример: Code analysis (existing project)

```python
# 1. Найди код
if os.path.exists("../src"):
    # 2. Читай package.json
    package = read_file("../package.json")
    tech_stack = extract_dependencies(package)
    
    # 3. Анализируй структуру
    structure = list_dir("../src")
    modules_in_code = extract_modules(structure)
    
    # 4. Сравни с requirements
    modules_in_raw_data = read_file("UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md")
    
    comparison = compare(modules_in_raw_data, modules_in_code)
    
    # 5. Задай вопросы пользователю о расхождениях
    if comparison.has_discrepancies:
        ask_user(comparison.questions)
```

---

## 📚 ССЫЛКИ

- **Оркестратор:** `UPMT/prompts/orchestrator.md`
- **Фазы:** `UPMT/prompts/phases/phase-X-*.md`
- **Этот адаптер используется для сценариев:** 1.1, 1.2

---

**Адаптер прочитан. Возвращайся к оркестратору и начинай PHASE 1.**

