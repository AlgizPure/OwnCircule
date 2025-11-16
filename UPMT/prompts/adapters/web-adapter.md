# 🌐 WEB ADAPTER - Работа через GitHub API

**Назначение:** Специфичные инструкции для работы через браузер (claude.ai/code) с GitHub API

---

## 🔗 GITHUB API ОПЕРАЦИИ

### Чтение файлов через GitHub API

**⚠️ ВСЕ операции чтения через GitHub API:**

```bash
# Читай файл
gh api /repos/{owner}/{repo}/contents/path/to/file.md --jq '.content' | base64 -d

# Читай структуру папки
gh api /repos/{owner}/{repo}/contents/path/to/directory

# Получи информацию о репозитории
gh api /repos/{owner}/{repo}
```

**Примеры:**

```bash
# Читай raw data
gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/metadata.yaml --jq '.content' | base64 -d

# Читай чаты
gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats

# Для каждого файла в chats/
gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/chat1.txt --jq '.content' | base64 -d
```

**⚠️ ОБРАБОТКА БОЛЬШИХ ФАЙЛОВ:**

**Алгоритм автоматического чтения (ИСПОЛЬЗУЙ ВСЕГДА):**

```python
def safe_read_file_github(owner, repo, file_path):
    """
    Читает файл через GitHub API, автоматически обрабатывает большие файлы.
    """
    try:
        # Попытка прочитать целиком через Contents API
        response = gh_api_get(f"/repos/{owner}/{repo}/contents/{file_path}")
        
        # Проверь размер файла
        if response.get('size', 0) > 1000000:  # > 1MB
            # Файл большой - используй Git Data API или download_url
            download_url = response.get('download_url')
            if download_url:
                # Читай через download_url (raw content)
                return read_file_from_url(download_url)
            else:
                # Используй Git Data API для чтения по частям
                return read_file_via_git_api(owner, repo, file_path)
        else:
            # Маленький файл - читай через Contents API
            content = base64_decode(response['content'])
            return content
            
    except FileTooLargeError:
        # GitHub API вернул ошибку размера
        print(f"⚠️ Файл {file_path} слишком большой для Contents API, используем Git Data API...")
        
        # Используй Git Data API (читает по частям)
        return read_file_via_git_api(owner, repo, file_path)

def read_file_via_git_api(owner, repo, file_path):
    """
    Читает большой файл через Git Data API по частям.
    """
    # Получи дерево файла
    tree_sha = get_file_tree_sha(owner, repo, file_path)
    
    # Читай файл через Git Data API
    blob_response = gh_api_get(f"/repos/{owner}/{repo}/git/blobs/{tree_sha}")
    
    # Если файл все еще большой, читай по частям через raw URL
    if blob_response.get('size', 0) > 1000000:
        # Используй raw.githubusercontent.com с range headers
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{file_path}"
        return read_file_in_chunks_from_url(raw_url)
    else:
        return base64_decode(blob_response['content'])

def read_file_in_chunks_from_url(url):
    """
    Читает файл по частям через HTTP range requests.
    """
    # Определи размер файла
    file_size = get_file_size_from_url(url)
    
    # Читай порциями по 2000 строк
    chunks = []
    chunk_size_bytes = 200000  # ~2000 строк
    
    for start_byte in range(0, file_size, chunk_size_bytes):
        end_byte = min(start_byte + chunk_size_bytes - 1, file_size)
        
        # HTTP Range request
        chunk = http_get_range(url, start_byte, end_byte)
        chunks.append(chunk)
        
        print(f"📖 Прочитано {end_byte}/{file_size} байт из {url}")
    
    full_content = "".join(chunks)
    print(f"✅ Файл прочитан полностью ({file_size} байт)")
    return full_content

# Использование:
content = safe_read_file_github(owner, repo, "UPMT/bootstrap/00_RAW_DATA_TEMPLATE/chats/large_chat.txt")
```

**Если получил ошибку:**
- `File content (XXX KB) exceeds maximum allowed size`
- GitHub API вернул `download_url` вместо `content`

**ТОГДА:**

1. **Используй download_url:**
```bash
# Получи download_url
download_url=$(gh api /repos/{owner}/{repo}/contents/path/to/file.txt --jq '.download_url')

# Читай через download_url (raw content)
curl "$download_url"
```

2. **Или используй Git Data API:**
```bash
# Получи SHA файла
sha=$(gh api /repos/{owner}/{repo}/contents/path/to/file.txt --jq '.sha')

# Читай через Git Data API
gh api /repos/{owner}/{repo}/git/blobs/$sha --jq '.content' | base64 -d
```

**⚠️ КРИТИЧНО:**
- ВСЕГДА используй `safe_read_file_github()` вместо прямого чтения через Contents API
- НЕ ПРОПУСКАЙ файлы из-за размера
- Автоматически переключайся на Git Data API или download_url для больших файлов
- Объединяй все части перед анализом

---

### Создание файлов через GitHub API

**Используй PUT request:**

```bash
# Создай файл
gh api \
  --method PUT \
  /repos/{owner}/{repo}/contents/path/to/file.md \
  -f message="docs(bootstrap): create file.md" \
  -f content="$(echo '[content]' | base64)" \
  -f branch="main"
```

**⚠️ ВАЖНО:**
- Content должен быть base64 encoded
- Каждый PUT = новый коммит
- Указывай правильный commit message

**Пример:**

```bash
# Создай PROJECT_ESSENCE.md
gh api \
  --method PUT \
  /repos/{owner}/{repo}/contents/docs/core/00_PROJECT_ESSENCE.md \
  -f message="docs(bootstrap): PHASE 5 - create PROJECT_ESSENCE" \
  -f content="$(cat content.md | base64)" \
  -f branch="main"
```

---

### Обновление файлов через GitHub API

**Для обновления нужен SHA:**

```bash
# 1. Получи текущий SHA
sha=$(gh api /repos/{owner}/{repo}/contents/path/to/file.md --jq '.sha')

# 2. Обнови файл
gh api \
  --method PUT \
  /repos/{owner}/{repo}/contents/path/to/file.md \
  -f message="docs(bootstrap): update file.md" \
  -f content="$(echo '[new content]' | base64)" \
  -f sha="$sha" \
  -f branch="main"
```

---

## 📂 СТРУКТУРА ПРОЕКТА В GITHUB

**GitHub репозиторий:**

```
github.com/{owner}/{repo}/
├── UPMT/                          # Шаблонная система
│   ├── bootstrap/
│   │   └── 00_RAW_DATA_TEMPLATE/  # Raw data (загружено пользователем)
│   ├── prompts/                   # Модульные промпты
│   └── START.md                   # Главное меню
│
├── docs/                          # Создаваемая документация (через API)
│   ├── core/
│   ├── requirements/
│   ├── progress/
│   ├── design/
│   └── backend/
│
├── .context/                      # Контекст проекта (через API)
├── .upmt/                         # Метаданные (через API)
└── .cursorrules                   # AI правила (через API)
```

**Если existing project:**

```
github.com/{owner}/{repo}/
├── UPMT/                          # Шаблон
├── docs/                          # Документация (создаётся через API)
├── src/                           # Существующий код (читать через API)
├── app/                           # Существующий код (читать через API)
├── components/                    # Существующий код (читать через API)
└── package.json                   # Зависимости (читать через API)
```

---

## 🔍 CODE ANALYSIS через GitHub API (для existing projects)

**Алгоритм анализа:**

```bash
# 1. Найди код
gh api /repos/{owner}/{repo}/contents/ | jq -r '.[].name' | grep -E "^(src|app|components|backend|frontend)$"

# 2. Для каждой найденной директории
for dir in src app components; do
    # Читай структуру
    gh api /repos/{owner}/{repo}/contents/$dir | jq -r '.[].name'
done

# 3. Читай ключевые файлы
gh api /repos/{owner}/{repo}/contents/package.json --jq '.content' | base64 -d
gh api /repos/{owner}/{repo}/contents/tsconfig.json --jq '.content' | base64 -d
gh api /repos/{owner}/{repo}/contents/README.md --jq '.content' | base64 -d

# 4. Анализируй структуру модулей
gh api /repos/{owner}/{repo}/contents/src
gh api /repos/{owner}/{repo}/contents/src/components
# И так далее для каждого модуля
```

**Что извлекать:**
- ✅ Tech stack (из `package.json`, imports в файлах)
- ✅ Реализованные модули (из структуры через API)
- ✅ Реализованные функции (из кода, прочитанного через API)
- ✅ Архитектурные паттерны (из структуры)
- ✅ Версии зависимостей (из `package.json`)

---

## 💾 CHECKPOINT ОПЕРАЦИИ (WEB/GitHub API)

**Назначение:** Сохранение и чтение checkpoint для recovery системы через GitHub API.

### Сохранение checkpoint

**⚠️ КРИТИЧНО: Checkpoint ДОЛЖЕН быть сохранен после КАЖДОЙ фазы и КАЖДОГО batch!**

**После каждой фазы и батча (PHASE 5) вызывай (ОБЯЗАТЕЛЬНО!):**

```python
def save_checkpoint_github(phase_number, phase_name, batch=None, state={}, owner=None, repo=None):
    """
    Сохраняет checkpoint в JSON файлы через GitHub API.
    
    Параметры:
    - phase_number: номер фазы (1-8)
    - phase_name: название фазы
    - batch: номер батча (опционально, для PHASE 5)
    - state: объект с текущим состоянием
    - owner: владелец репозитория (GitHub username)
    - repo: название репозитория
    """
    import json
    import base64
    from datetime import datetime
    
    # 1. Собрать checkpoint данные
    checkpoint = {
        "phase": phase_number,
        "phase_name": phase_name,
        "batch": batch,
        "timestamp": datetime.now().isoformat(),
        "session_id": f"web-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "mode": "WEB_GITHUB",
        "state": state,
        "stats": {
            "total_files": count_files_via_api(owner, repo, "docs/"),
            "elapsed_time": calculate_elapsed_time_from_start()
        },
        "next_action": determine_next_action(phase_number, batch, existing_project=False)
    }
    
    # 2. Преобразовать в JSON
    checkpoint_json = json.dumps(checkpoint, indent=2, ensure_ascii=False)
    checkpoint_base64 = base64.b64encode(checkpoint_json.encode('utf-8')).decode('utf-8')
    
    # 3. Проверить существование latest.json
    try:
        gh api /repos/{owner}/{repo}/contents/.upmt/checkpoints/latest.json \
          --jq '.sha'
        existing_sha = [результат команды]
    except:
        existing_sha = None
    
    # 4. Сохранить latest.json (PUT через API)
    gh api \
      --method PUT \
      /repos/{owner}/{repo}/contents/.upmt/checkpoints/latest.json \
      -f message="checkpoint: PHASE {phase_number}" + (f" batch {batch}" if batch else "") \
      -f content="{checkpoint_base64}" \
      -f sha="{existing_sha}"  # Только если файл уже существует
    
    # 5. Сохранить архивную копию
    checkpoint_name = f"phase-{phase_number}"
    if batch:
        checkpoint_name += f"-batch-{batch}"
    checkpoint_name += ".json"
    
    # Проверить существование архивного файла
    try:
        archive_sha = gh api /repos/{owner}/{repo}/contents/.upmt/checkpoints/{checkpoint_name} --jq '.sha'
    except:
        archive_sha = None
    
    gh api \
      --method PUT \
      /repos/{owner}/{repo}/contents/.upmt/checkpoints/{checkpoint_name} \
      -f message="checkpoint: archive PHASE {phase_number}" + (f" batch {batch}" if batch else "") \
      -f content="{checkpoint_base64}" \
      -f sha="{archive_sha}"  # Только если файл уже существует
    
    # 6. Логирование
    print(f"💾 Checkpoint saved (GitHub): {phase_name}" + 
          (f" (batch {batch})" if batch else ""))
    print(f"   Files: {checkpoint['stats']['total_files']}, " +
          f"Time: {checkpoint['stats']['elapsed_time']}")


# Вспомогательные функции:

def count_files_via_api(owner, repo, directory):
    """
    Подсчет файлов в директории через GitHub API (рекурсивно).
    """
    # Получить tree recursively
    tree = gh api /repos/{owner}/{repo}/git/trees/main?recursive=1
    
    # Фильтровать по директории и типу "blob" (файл)
    count = 0
    for item in tree['tree']:
        if item['path'].startswith(directory) and item['type'] == 'blob':
            count += 1
    
    return count


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
save_checkpoint_github(
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
    },
    owner="AlgizPure",
    repo="Brain-Rent"
)
```

### Чтение checkpoint

**Для проверки наличия незавершенного bootstrap:**

```python
def read_checkpoint_github(owner, repo):
    """
    Читает последний checkpoint через GitHub API.
    Возвращает checkpoint объект или None.
    """
    import json
    import base64
    
    try:
        # Получить latest.json
        response = gh api /repos/{owner}/{repo}/contents/.upmt/checkpoints/latest.json
        
        # Декодировать из base64
        content_base64 = response['content']
        content_json = base64.b64decode(content_base64).decode('utf-8')
        
        # Распарсить JSON
        checkpoint = json.loads(content_json)
        
        return checkpoint
        
    except Exception as e:
        # Файл не существует или ошибка чтения
        print(f"⚠️  Checkpoint not found: {e}")
        return None


# Использование в orchestrator.md ШАГ 0.0.0:
checkpoint = read_checkpoint_github(owner="AlgizPure", repo="Brain-Rent")

if checkpoint:
    # Показать recovery dialog
    show_recovery_dialog(checkpoint)
else:
    # Начать bootstrap с PHASE 1
    start_fresh_bootstrap()
```

**⚠️ ВАЖНО для Web режима:**

1. **Checkpoint файлы создаются через GitHub API** - они сразу в репозитории
2. **Каждое сохранение = отдельный коммит** с message `"checkpoint: PHASE X"`
3. **Recovery работает между сессиями** - checkpoint сохранен в GitHub
4. **Не нужен локальный доступ** - всё через API

**Подробная документация:** См. `UPMT/prompts/utils/checkpoint-functions.md`

---

## 💾 GITHUB API COMMITS

**Каждый PUT = commit:**

```bash
# PUT request автоматически создаёт коммит
gh api \
  --method PUT \
  /repos/{owner}/{repo}/contents/docs/core/00_PROJECT_ESSENCE.md \
  -f message="docs(bootstrap): PHASE 5 - create PROJECT_ESSENCE" \
  -f content="$(echo '[content]' | base64)"
```

**Checkpoint strategy:**

**PHASE 1-4, 6-8:**
- 1 файл = 1 коммит

**PHASE 5 (много файлов):**
- Батчи по 6 модулей
- После каждого батча - показывай прогресс

**PHASE 5.5, 5.7:**
- Группируй по секциям (foundation, components, entities, api)
- 1 секция = несколько файлов = несколько коммитов подряд

---

## 📊 ПРОГРЕСС TRACKING

**Показывай прогресс каждые 30 минут:**

```markdown
⏱️ BOOTSTRAP PROGRESS UPDATE (GitHub API)

**Текущая фаза:** PHASE X - [название]
**Прогресс:** [X%]
**Время работы:** [HH:MM]

**Последние действия:**
- ✅ Создано через API: docs/core/00_PROJECT_ESSENCE.md
- ✅ Создано через API: docs/core/01_PRD.md
- 🔄 Создаю через API: docs/requirements/module_1_requirements.md

**GitHub API requests:** [N requests]
**Commits в репозитории:** [M commits]

**Следующие шаги:**
- [ ] Создать requirements для модуля 2
- [ ] ...
```

---

## 🚨 КРИТИЧЕСКИЕ ПРАВИЛА WEB (GitHub API)

1. **ВСЕ ОПЕРАЦИИ ЧЕРЕЗ GITHUB API**
   - ❌ Локальное чтение файлов
   - ✅ `gh api /repos/{owner}/{repo}/contents/...`

2. **НЕ МОЖЕШЬ ВЫПОЛНЯТЬ BASH КОМАНДЫ**
   - ❌ `npm install`
   - ❌ `git clone`
   - ❌ Локальные команды
   - ✅ Только GitHub API requests

3. **КАЖДЫЙ ФАЙЛ = КОММИТ**
   - PUT request автоматически коммитит
   - Используй осмысленные commit messages

4. **CONTENT ДОЛЖЕН БЫТЬ BASE64**
   ```bash
   -f content="$(echo 'text content' | base64)"
   ```

5. **ДЛЯ ОБНОВЛЕНИЯ НУЖЕН SHA**
   - Сначала GET для получения SHA
   - Потом PUT с SHA для обновления

6. **API RATE LIMITS**
   - GitHub API: 5000 requests/hour (authenticated)
   - Если лимит близок - сообщи пользователю
   - Группируй операции где возможно

7. **ПИШИ ПОЛНЫЕ ФАЙЛЫ**
   - Не используй `[...]` или placeholders
   - Всё содержимое целиком

---

## 💡 ПРИМЕРЫ

### Пример: Создание module requirements через API

```bash
# 1. Прочитай context через API
gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md --jq '.content' | base64 -d > modules.md

gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/extracted_features.md --jq '.content' | base64 -d > features.md

# 2. Обработай локально (в памяти)
total_modules = count_modules(modules.md)

# 3. Для каждого модуля создай файл через API
for module in modules:
    module_name = module["name"]
    requirements_content = generate_requirements(module, features)
    
    # Создай через API
    gh api \
      --method PUT \
      /repos/{owner}/{repo}/contents/docs/requirements/${module_name}_requirements.md \
      -f message="docs(bootstrap): create ${module_name} requirements" \
      -f content="$(echo "$requirements_content" | base64)"
    
    # Каждые 6 модулей - показывай прогресс
    if i % 6 == 0:
        show_progress("PHASE 5: Batch ${i/6} complete")
```

### Пример: Code analysis через GitHub API

```bash
# 1. Проверь наличие кода
code_exists=$(gh api /repos/{owner}/{repo}/contents/ | jq -r '.[].name' | grep -E "^src$")

if [ -n "$code_exists" ]; then
    # 2. Читай package.json
    package=$(gh api /repos/{owner}/{repo}/contents/package.json --jq '.content' | base64 -d)
    tech_stack=$(extract_dependencies "$package")
    
    # 3. Анализируй структуру
    structure=$(gh api /repos/{owner}/{repo}/contents/src | jq -r '.[].name')
    modules_in_code=$(extract_modules "$structure")
    
    # 4. Читай modules_list.md
    modules_in_raw_data=$(gh api /repos/{owner}/{repo}/contents/UPMT/bootstrap/00_RAW_DATA_TEMPLATE/modules_list.md --jq '.content' | base64 -d)
    
    # 5. Сравни
    comparison=$(compare "$modules_in_raw_data" "$modules_in_code")
    
    # 6. Задай вопросы пользователю
    if [ -n "$comparison.discrepancies" ]; then
        ask_user "$comparison.questions"
    fi
fi
```

### Пример: Batch создание файлов с прогрессом

```bash
# PHASE 5: Создание module requirements батчами

total_modules=24
batch_size=6
batches=$((total_modules / batch_size))

for batch in $(seq 1 $batches); do
    start=$(( (batch - 1) * 6 + 1 ))
    end=$(( batch * 6 ))
    
    echo "📦 PHASE 5: Batch $batch/$batches - modules $start-$end"
    
    # Создай requirements для модулей в батче
    for i in $(seq $start $end); do
        module=$(get_module $i)
        content=$(generate_requirements $module)
        
        gh api \
          --method PUT \
          /repos/{owner}/{repo}/contents/docs/requirements/${module}_requirements.md \
          -f message="docs(bootstrap): PHASE 5 batch $batch - module $i" \
          -f content="$(echo "$content" | base64)"
    done
    
    echo "✅ Batch $batch/$batches complete"
    echo "→ Remaining: $((total_modules - end)) modules"
done

echo "✅ PHASE 5 complete - all $total_modules module requirements created"
```

---

## ⚠️ ОСОБЕННОСТИ WEB РЕЖИМА

1. **Нельзя запустить npm install**
   - Только читать `package.json`
   - Анализировать зависимости

2. **Нельзя выполнить команды пользователя**
   - Только GitHub API
   - Только операции с репозиторием

3. **Все файлы через API**
   - GET для чтения
   - PUT для создания/обновления
   - DELETE для удаления (не используй без крайней необходимости)

4. **Медленнее чем CLI**
   - Каждый файл = API request
   - Показывай прогресс чаще
   - Группируй где можно

---

## 📚 ССЫЛКИ

- **Оркестратор:** `UPMT/prompts/orchestrator.md` (прочитай через GitHub API)
- **Фазы:** `UPMT/prompts/phases/phase-X-*.md` (прочитай через GitHub API)
- **Этот адаптер используется для сценариев:** 1.3, 1.4

---

**Адаптер прочитан. Возвращайся к оркестратору и начинай PHASE 1 (через GitHub API).**

