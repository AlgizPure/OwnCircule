# 📚 CHECKPOINT FUNCTIONS LIBRARY

**Версия:** 1.0  
**Дата:** 2025-11-15  
**Назначение:** Библиотека функций для работы с checkpoint системой

---

## 📖 ОБЗОР

Этот файл содержит псевдокод функций для работы с checkpoint системой. Эти функции используются в:
- `UPMT/prompts/orchestrator.md` (ШАГ 0.0.0)
- `UPMT/prompts/phases/phase-*.md` (секция CHECKPOINT)
- `UPMT/prompts/adapters/cli-adapter.md` и `web-adapter.md`

**Важно:** Это псевдокод для Claude Code, не реальный Python/JavaScript код!

---

## 💾 save_checkpoint()

**Назначение:** Сохраняет checkpoint после завершения фазы или батча.

**Параметры:**
- `phase_number` (int): Номер фазы (1-8)
- `phase_name` (string): Название фазы (например, "PHASE 1: Analysis")
- `batch` (int, optional): Номер батча (только для PHASE 5)
- `state` (object): Текущее состояние bootstrap процесса

**Создает:**
- `.upmt/checkpoints/latest.json` (перезаписывается каждый раз)
- `.upmt/checkpoints/phase-{N}[-batch-{M}].json` (архивная копия)

**Структура `state` объекта:**

```python
state = {
    "current_action": "Описание текущего действия",
    "files_created": [
        "docs/requirements/module-1.md",
        "docs/requirements/module-2.md"
    ],
    "context_files": [
        "extracted_features.md",
        "modules_list.md",
        "metadata.yaml",
        "PROJECT_SYNTHESIS.md"
    ],
    # Дополнительные поля зависят от фазы:
    "modules_completed": ["Dashboard", "User Profile"],  # Для PHASE 5
    "total_modules": 8,                                   # Для PHASE 5
    "current_module": "Settings"                          # Для PHASE 5
}
```

**Псевдокод:**

```python
def save_checkpoint(phase_number, phase_name, batch=None, state={}):
    """
    Сохраняет checkpoint в JSON файлы.
    """
    # 1. Создать директорию если не существует
    ensure_directory_exists(".upmt/checkpoints/")
    
    # 2. Собрать данные checkpoint
    checkpoint = {
        "phase": phase_number,
        "phase_name": phase_name,
        "batch": batch,
        "timestamp": current_datetime_iso(),
        "session_id": f"{mode}-{current_datetime_formatted()}",
        "mode": "CLI" or "WEB" or "CURSOR",
        "state": state,
        "stats": {
            "total_files": count_files_in_directory("docs/"),
            "total_lines": count_total_lines("docs/"),
            "elapsed_time": calculate_elapsed_time_from_start()
        },
        "next_action": determine_next_action(phase_number, batch, existing_project=False)
    }
    
    # 3. Сохранить latest.json (перезапись)
    write_json_file(".upmt/checkpoints/latest.json", checkpoint)
    
    # 4. Сохранить архивную копию
    archive_name = f"phase-{phase_number}"
    if batch is not None:
        archive_name += f"-batch-{batch}"
    archive_name += ".json"
    
    write_json_file(f".upmt/checkpoints/{archive_name}", checkpoint)
    
    # 5. Логирование
    print(f"💾 Checkpoint saved: {phase_name}" + 
          (f" (batch {batch})" if batch else ""))
    print(f"   Files: {checkpoint['stats']['total_files']}, " +
          f"Time: {checkpoint['stats']['elapsed_time']}")
```

**Пример вызова:**

```python
# После завершения PHASE 1
save_checkpoint(
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

# После завершения PHASE 5, batch 2
save_checkpoint(
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

---

## 🔍 check_for_incomplete_bootstrap()

**Назначение:** Проверяет наличие незавершенного bootstrap процесса.

**Вызывается:** В `orchestrator.md` ШАГ 0.0.0 перед началом любых действий.

**Возвращает:**
- `null` / `None` - если checkpoint не найден или завершен
- `checkpoint object` - если найден незавершенный bootstrap

**Псевдокод:**

```python
def check_for_incomplete_bootstrap(mode="CLI"):
    """
    Проверяет наличие незавершенного bootstrap с обработкой ошибок.
    
    Параметры:
    - mode: "CLI" или "WEB_GITHUB" или "CURSOR"
    """
    # 1. Проверить существование latest.json
    if mode == "WEB_GITHUB":
        # В Web mode проверяем через GitHub API
        try:
            checkpoint_content = read_file_via_api(".upmt/checkpoints/latest.json")
            if not checkpoint_content:
                return None
            checkpoint = parse_json(checkpoint_content)
        except (FileNotFoundError, JSONDecodeError) as e:
            print(f"⚠️  Checkpoint файл поврежден или не найден в GitHub: {e}")
            print("   Пробую восстановление через Git...")
            return try_git_recovery(mode)
    else:
        # CLI/Cursor mode - локальная проверка
        if not file_exists(".upmt/checkpoints/latest.json"):
            return None
        
        # 2. Прочитать checkpoint с обработкой ошибок
        try:
            checkpoint = read_json_file(".upmt/checkpoints/latest.json")
        except (FileNotFoundError, JSONDecodeError) as e:
            print(f"⚠️  Checkpoint файл поврежден или не найден: {e}")
            print("   Пробую восстановление через Git...")
            return try_git_recovery(mode)
    
    # 3. Проверить актуальность
    checkpoint_age_hours = calculate_age_in_hours(checkpoint['timestamp'])
    
    # 4. Проверить завершенность
    if checkpoint_age_hours >= 24:
        print("⚠️  Checkpoint старше 24 часов - игнорируем")
        return None
    
    if checkpoint['phase'] >= 8:
        print("✅ Bootstrap завершен - checkpoint игнорируется")
        return None
    
    # 5. Checkpoint актуален и незавершен
    return checkpoint
```

**Пример вызова:**

```python
# В orchestrator.md ШАГ 0.0.0
checkpoint = check_for_incomplete_bootstrap()

if checkpoint:
    show_recovery_dialog(checkpoint)
    choice = ask_user("Resume (1), Start Fresh (2), View Details (3):")
    
    if choice == "1":
        resume_from_checkpoint(checkpoint)
    elif choice == "3":
        show_detailed_recovery_status(checkpoint)
        # Повторить вопрос
    else:
        archive_and_delete_checkpoint(checkpoint)
        start_fresh_bootstrap()
else:
    # Checkpoint не найден - начать с PHASE 1
    start_fresh_bootstrap()
```

---

## 🔄 resume_from_checkpoint()

**Назначение:** Восстанавливает bootstrap процесс с checkpoint.

**Параметры:**
- `checkpoint` (object): Объект checkpoint из JSON

**Выполняет:**
1. Валидация checkpoint (файлы существуют)
2. Определение фазы для продолжения
3. Загрузка контекстных файлов
4. Вывод recovery status report
5. Запрос подтверждения пользователя

**Псевдокод:**

```python
def resume_from_checkpoint(checkpoint):
    """
    Восстанавливает bootstrap с checkpoint.
    """
    # 1. Валидация checkpoint
    mode = checkpoint.get('mode', 'CLI')
    is_valid = validate_checkpoint_integrity(checkpoint, mode=mode)
    
    if not is_valid:
        print("❌ Checkpoint поврежден или файлы не найдены")
        print("   Попробуйте СЦЕНАРИЙ C (откат к стабильной точке)")
        return False
    
    # 2. Определить фазу для продолжения
    resume_phase = checkpoint['phase']
    resume_batch = checkpoint.get('batch')
    
    # Проверить, завершен ли текущий batch (для PHASE 5)
    if resume_phase == 5 and resume_batch:
        # Проверить, все ли файлы batch созданы
        expected_files = checkpoint['state'].get('files_created', [])
        batch_complete = len(expected_files) > 0  # Упрощенная проверка
        
        # Если batch завершен - продолжить со следующего
        if batch_complete:
            resume_batch = resume_batch + 1
        # Если batch не завершен - продолжить с текущего
        # resume_batch остается прежним
    elif resume_phase == 5 and not resume_batch:
        # PHASE 5 завершена - определить следующую фазу (5.4, 5.5, 5.7 или 6)
        # Эта логика будет в orchestrator.md
        pass
    elif resume_phase == 5.4:
        # PHASE 5.4 завершена - определить следующую фазу (5.5, 5.7 или 6)
        # Эта логика будет в orchestrator.md
        pass
    elif resume_phase < 8:
        # Обычные фазы - продолжить со следующей
        resume_phase = resume_phase + 1
        resume_batch = None
    
    # 3. Загрузить контекстные файлы
    print("\n📖 Загрузка контекстных файлов...")
    
    read_file("UPMT/prompts/orchestrator.md")
    read_file(f"UPMT/prompts/adapters/{mode}-adapter.md")
    read_file(f"UPMT/prompts/phases/phase-{resume_phase}-*.md")
    
    for context_file in checkpoint['state']['context_files']:
        if file_exists(context_file):
            read_file(context_file)
    
    # 4. Вывести recovery status report
    show_recovery_status_report(checkpoint, resume_phase, resume_batch)
    
    # 5. Запросить подтверждение
    confirmed = ask_user("\nПродолжить с этой точки? (yes/no): ")
    
    if confirmed.lower() == "yes":
        print(f"\n✅ Восстанавливаю bootstrap с PHASE {resume_phase}" +
              (f", batch {resume_batch}" if resume_batch else ""))
        
        # SKIP to resume phase
        return {
            "resume": True,
            "phase": resume_phase,
            "batch": resume_batch
        }
    else:
        print("\n❌ Восстановление отменено пользователем")
        return False
```

---

## 🎯 determine_next_action()

**Назначение:** Определяет следующее действие на основе текущей фазы.

**Параметры:**
- `phase_number` (int): Номер текущей фазы
- `batch` (int, optional): Номер батча (если применимо)

**Возвращает:** Строка с описанием следующего действия.

**Псевдокод:**

```python
def determine_next_action(phase_number, batch=None, existing_project=False):
    """
    Определяет следующее действие с учетом conditional phases.
    """
    actions = {
        1: "Continue to PHASE 2: Interview",
        2: "Continue to PHASE 3: Tech Verification",
        3: "Continue to PHASE 4: Synthesis",
        4: "Continue to PHASE 5: Documentation",
        5: {
            "with_batch": f"Continue PHASE 5: batch {batch + 1}",
            "no_batch": None  # Будет определено ниже
        },
        5.4: None,  # Будет определено ниже (conditional phases)
        5.5: "Continue to PHASE 5.7 or PHASE 6 (conditional)",
        5.7: "Continue to PHASE 6: Setup Instructions",
        6: "Continue to PHASE 7: Validation",
        7: "Continue to PHASE 8: Final Report",
        8: "Bootstrap complete - ready for development"
    }
    
    if phase_number == 5:
        if batch:
            # PHASE 5 в процессе - продолжить с batch
            return actions[5]["with_batch"]
        else:
            # PHASE 5 завершена - проверить PHASE 5.4 (Figma Make)
            # Примечание: PHASE 5.4 опциональная, выбор пользователя хранится в checkpoint
            # Здесь возвращаем переход к conditional phases (5.5/5.7/6)
            # Реальная логика выбора PHASE 5.4 находится в orchestrator.md
            design_data_exists, _ = check_design_data_exists()
            backend_data_exists, _ = check_backend_data_exists()
            
            if design_data_exists or existing_project:
                return "Continue to PHASE 5.5: Design System (or PHASE 5.4 if Figma Make selected)"
            elif backend_data_exists or existing_project:
                return "Continue to PHASE 5.7: Backend Documentation (or PHASE 5.4 if Figma Make selected)"
            else:
                return "Continue to PHASE 6: Setup Instructions (or PHASE 5.4 if Figma Make selected)"
    elif phase_number == 5.4:
        # PHASE 5.4 завершена - проверить conditional phases
        design_data_exists, _ = check_design_data_exists()
        backend_data_exists, _ = check_backend_data_exists()
        
        if design_data_exists or existing_project:
            return "Continue to PHASE 5.5: Design System"
        elif backend_data_exists or existing_project:
            return "Continue to PHASE 5.7: Backend Documentation"
        else:
            return "Continue to PHASE 6: Setup Instructions"
    elif phase_number == 5.5:
        # После PHASE 5.5 - проверить PHASE 5.7
        backend_data_exists, _ = check_backend_data_exists()
        if backend_data_exists or existing_project:
            return "Continue to PHASE 5.7: Backend Documentation"
        else:
            return "Continue to PHASE 6: Setup Instructions"
    else:
        return actions.get(phase_number, "Unknown phase")
```

---

## ✅ validate_checkpoint_integrity()

**Назначение:** Проверяет целостность checkpoint.

**Параметры:**
- `checkpoint` (object): Объект checkpoint для проверки

**Проверяет:**
- Существование файлов из `checkpoint['state']['files_created']`
- Соответствие Git истории
- Возраст checkpoint (<24 часов)

**Возвращает:** `true` / `false`

**Псевдокод:**

```python
def validate_checkpoint_integrity(checkpoint, mode="CLI"):
    """
    Проверяет целостность checkpoint с учетом режима работы.
    
    Параметры:
    - checkpoint: Объект checkpoint для проверки
    - mode: "CLI" или "WEB_GITHUB" или "CURSOR"
    """
    errors = []
    
    # 1. Проверить возраст
    age_hours = calculate_age_in_hours(checkpoint['timestamp'])
    if age_hours >= 24:
        errors.append(f"Checkpoint старше 24 часов ({age_hours:.1f}h)")
    
    # 2. Проверить существование файлов
    files_created = checkpoint['state'].get('files_created', [])
    missing_files = []
    empty_files = []
    
    for file_path in files_created[:20]:  # Проверяем первые 20 файлов
        if mode == "WEB_GITHUB":
            # В Web mode проверяем через GitHub API
            if not file_exists_via_api(file_path):
                missing_files.append(file_path)
            else:
                # Проверяем размер файла через API
                file_size = get_file_size_via_api(file_path)
                if file_size == 0:
                    empty_files.append(file_path)
                elif file_size < 100:  # Минимальный размер для документации
                    empty_files.append(f"{file_path} ({file_size} bytes - слишком маленький)")
        else:
            # CLI/Cursor mode - локальная проверка
            if not file_exists(file_path):
                missing_files.append(file_path)
            else:
                file_size = get_file_size(file_path)
                if file_size == 0:
                    empty_files.append(file_path)
                elif file_size < 100:  # Минимальный размер для документации
                    empty_files.append(f"{file_path} ({file_size} bytes - слишком маленький)")
    
    if missing_files:
        errors.append(f"Отсутствуют файлы: {len(missing_files)}")
        for f in missing_files[:5]:  # Показать первые 5
            errors.append(f"  - {f}")
    
    if empty_files:
        errors.append(f"Пустые или слишком маленькие файлы: {len(empty_files)}")
        for f in empty_files[:5]:  # Показать первые 5
            errors.append(f"  - {f}")
    
    # 3. Проверка Git истории (только для CLI mode)
    if mode == "CLI" or mode == "CURSOR":
        last_git_commit = get_last_commit_message_with_grep("bootstrap")
        
        if last_git_commit:
            expected_phase = f"PHASE {checkpoint['phase']}"
            if expected_phase not in last_git_commit:
                errors.append(
                    f"Git история не совпадает: "
                    f"ожидается {expected_phase}, найдено '{last_git_commit}'"
                )
    elif mode == "WEB_GITHUB":
        # В Web mode проверяем через GitHub API
        # Если файлы существуют в репозитории - checkpoint валиден
        files_exist_in_github = check_files_exist_via_api(files_created[:10])
        if not files_exist_in_github:
            errors.append("Файлы не найдены в GitHub репозитории")
    
    # 4. Вывод результата
    if errors:
        print("\n❌ Проблемы с checkpoint:")
        for error in errors:
            print(f"   {error}")
        return False
    
    print("\n✅ Checkpoint валиден")
    return True
```

---

## 📊 show_recovery_dialog()

**Назначение:** Показывает dialog с информацией о найденном checkpoint.

**Параметры:**
- `checkpoint` (object): Объект checkpoint

**Псевдокод:**

```python
def show_recovery_dialog(checkpoint):
    """
    Показывает recovery dialog.
    """
    age_hours = calculate_age_in_hours(checkpoint['timestamp'])
    progress_percent = (checkpoint['phase'] / 8) * 100
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║            НЕЗАВЕРШЕННЫЙ BOOTSTRAP ОБНАРУЖЕН                  ║
╚══════════════════════════════════════════════════════════════╝

⚠️  Найден checkpoint от: {checkpoint['timestamp']}
    Возраст: {age_hours:.1f} часов назад

📍 Последнее завершенное:
   Фаза: {checkpoint['phase_name']} (PHASE {checkpoint['phase']})
   Батч: {checkpoint['batch'] if checkpoint['batch'] else 'N/A'}
   Файлов создано: {len(checkpoint['state']['files_created'])}
   Прогресс: {checkpoint['phase']}/8 фаз ({progress_percent:.0f}%)
   Время работы: {checkpoint['stats']['elapsed_time']}

🔄 Варианты действий:
   1. Продолжить с checkpoint (рекомендуется)
   2. Начать заново (удалить checkpoint)
   3. Показать детальный статус

Ваш выбор (1/2/3):
    """)
```

---

## 📋 show_recovery_status_report()

**Назначение:** Показывает детальный отчет о состоянии для восстановления.

**Параметры:**
- `checkpoint` (object): Объект checkpoint
- `resume_phase` (int): Фаза для продолжения
- `resume_batch` (int, optional): Батч для продолжения

**Псевдокод:**

```python
def show_recovery_status_report(checkpoint, resume_phase, resume_batch=None):
    """
    Показывает детальный recovery status report.
    """
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║              BOOTSTRAP RECOVERY - STATUS REPORT               ║
╚══════════════════════════════════════════════════════════════╝

📍 CHECKPOINT DETECTED:
   Phase: {checkpoint['phase_name']}
   Batch: {checkpoint['batch'] if checkpoint['batch'] else 'N/A'}
   Timestamp: {checkpoint['timestamp']}
   Files created: {len(checkpoint['state']['files_created'])}

📊 PROGRESS SUMMARY:
   ✅ Completed phases:
    """)
    
    # Список завершенных фаз
    for i in range(1, checkpoint['phase'] + 1):
        phase_name = get_phase_name(i)
        print(f"      - PHASE {i}: {phase_name}")
    
    print(f"""
   🔄 TO RESUME:
      - PHASE {resume_phase}: {get_phase_name(resume_phase)}""" + 
      (f" (batch {resume_batch})" if resume_batch else ""))
    
    # Оставшиеся фазы
    for i in range(resume_phase + 1, 9):
        phase_name = get_phase_name(i)
        print(f"      - PHASE {i}: {phase_name}")
    
    print(f"""
🎯 NEXT ACTION:
   Resume from: PHASE {resume_phase}""" + 
   (f", batch {resume_batch}" if resume_batch else "") + f"""
   Expected action: {checkpoint.get('next_action', 'Continue bootstrap')}

🔍 VALIDATION:
   {'✅' if validate_checkpoint_integrity(checkpoint, mode=checkpoint.get('mode', 'CLI')) else '❌'} Checkpoint integrity checked
   {'✅' if checkpoint['state']['context_files'] else '❌'} Context files available
   ✅ Ready to resume
    """)
```

---

## 🗂️ archive_and_delete_checkpoint()

**Назначение:** Архивирует checkpoint перед удалением (при выборе "Start Fresh").

**Параметры:**
- `checkpoint` (object): Объект checkpoint для архивации

**Псевдокод:**

```python
def archive_and_delete_checkpoint(checkpoint):
    """
    Архивирует и удаляет checkpoint.
    """
    # 1. Создать папку архива
    archive_dir = f".upmt/checkpoints/archive/{current_date()}/"
    ensure_directory_exists(archive_dir)
    
    # 2. Скопировать latest.json в архив
    archive_name = f"abandoned-{checkpoint['session_id']}.json"
    copy_file(
        ".upmt/checkpoints/latest.json",
        f"{archive_dir}{archive_name}"
    )
    
    # 3. Удалить latest.json
    delete_file(".upmt/checkpoints/latest.json")
    
    print(f"📦 Checkpoint archived to: {archive_dir}{archive_name}")
    print("✅ Starting fresh bootstrap")
```

---

## 🔧 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

### calculate_age_in_hours()

```python
def calculate_age_in_hours(timestamp_iso):
    """
    Вычисляет возраст checkpoint в часах.
    """
    checkpoint_time = parse_datetime(timestamp_iso)
    current_time = now()
    delta = current_time - checkpoint_time
    return delta.total_seconds() / 3600
```

### get_phase_name()

```python
def get_phase_name(phase_number):
    """
    Возвращает название фазы по номеру.
    """
    phase_names = {
        1: "Analysis",
        2: "Interview",
        3: "Tech Verification",
        4: "Synthesis",
        5: "Documentation",
        6: "Setup Instructions",
        7: "Validation",
        8: "Final Report"
    }
    return phase_names.get(phase_number, "Unknown")
```

### count_files_in_directory()

```python
def count_files_in_directory(directory):
    """
    Подсчитывает количество файлов в директории (рекурсивно).
    """
    count = 0
    for file in list_files_recursively(directory):
        if not is_directory(file):
            count += 1
    return count
```

### calculate_elapsed_time_from_start()

```python
def calculate_elapsed_time_from_start():
    """
    Вычисляет время с момента запуска bootstrap.
    Предполагается, что start_time сохранен где-то.
    """
    start_time = get_bootstrap_start_time()  # Из первого checkpoint
    current_time = now()
    delta = current_time - start_time
    
    hours = int(delta.total_seconds() // 3600)
    minutes = int((delta.total_seconds() % 3600) // 60)
    seconds = int(delta.total_seconds() % 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```

---

## 📚 ИСПОЛЬЗОВАНИЕ В ДРУГИХ ФАЙЛАХ

### В orchestrator.md (ШАГ 0.0.0):

```python
checkpoint = check_for_incomplete_bootstrap()

if checkpoint:
    show_recovery_dialog(checkpoint)
    choice = ask_user("Resume (1), Start Fresh (2), View Details (3):")
    
    if choice == "1":
        resume_result = resume_from_checkpoint(checkpoint)
        if resume_result['resume']:
            # SKIP to resume_result['phase']
            pass
```

### В phase файлах (секция CHECKPOINT):

```python
# После завершения фазы
save_checkpoint(
    phase_number=X,
    phase_name="PHASE X: [название]",
    batch=None,
    state={...}
)
```

---

**Версия:** 1.0  
**Статус:** Ready for integration  
**Использование:** См. `RECOVERY_PROTOCOL.md` для полного контекста

---

**Готово к интеграции в UPMT v3.0.2+** ✅

---

## 🔄 try_git_recovery()

**Назначение:** Пытается восстановить checkpoint из Git истории, если JSON файл поврежден или отсутствует.

**Параметры:**
- `mode`: "CLI" или "WEB_GITHUB" или "CURSOR"

**Возвращает:**
- `checkpoint object` - если найден в Git истории
- `None` - если восстановление невозможно

**Псевдокод:**

```python
def try_git_recovery(mode="CLI"):
    """
    Пытается восстановить checkpoint из Git истории.
    """
    print("\n🔍 Пробую восстановление через Git историю...")
    
    if mode == "WEB_GITHUB":
        # В Web mode проверяем через GitHub API
        try:
            # Найти последний коммит с паттерном "bootstrap"
            commits = get_commits_via_api(grep="bootstrap", limit=10)
            
            for commit in commits:
                commit_message = commit['message']
                if "PHASE" in commit_message and "complete" in commit_message:
                    # Извлечь номер фазы из commit message
                    phase_match = re.search(r"PHASE (\d+(?:\.\d+)?)", commit_message)
                    if phase_match:
                        phase_num = float(phase_match.group(1))
                        
                        # Проверить batch в commit message
                        batch_match = re.search(r"batch (\d+)", commit_message)
                        batch_num = int(batch_match.group(1)) if batch_match else None
                        
                        # Создать recovery checkpoint из Git
                        recovery_checkpoint = {
                            "phase": int(phase_num),
                            "phase_name": get_phase_name(int(phase_num)),
                            "batch": batch_num,
                            "timestamp": commit['date'],
                            "session_id": f"git-recovery-{commit['sha'][:8]}",
                            "mode": "WEB_GITHUB",
                            "state": {
                                "current_action": f"Recovered from Git commit: {commit['sha'][:8]}",
                                "files_created": [],  # Будет определено из файлов в коммите
                                "context_files": []
                            },
                            "stats": {
                                "total_files": 0,
                                "elapsed_time": "Unknown"
                            },
                            "recovered_from_git": True,
                            "git_commit": commit['sha']
                        }
                        
                        print(f"✅ Найден Git checkpoint: PHASE {phase_num}" + 
                              (f", batch {batch_num}" if batch_num else ""))
                        return recovery_checkpoint
        except Exception as e:
            print(f"⚠️  Ошибка при восстановлении через GitHub API: {e}")
            return None
    else:
        # CLI/Cursor mode - локальная Git проверка
        try:
            # Найти последний коммит с паттерном "bootstrap"
            git_log = run_command("git log --oneline --grep='bootstrap' -10")
            
            for line in git_log.split('\n'):
                if "PHASE" in line and "complete" in line:
                    # Извлечь номер фазы
                    phase_match = re.search(r"PHASE (\d+(?:\.\d+)?)", line)
                    if phase_match:
                        phase_num = float(phase_match.group(1))
                        commit_hash = line.split()[0]
                        
                        # Проверить batch
                        batch_match = re.search(r"batch (\d+)", line)
                        batch_num = int(batch_match.group(1)) if batch_match else None
                        
                        # Получить дату коммита
                        commit_date = run_command(f"git log -1 --format=%cI {commit_hash}")
                        
                        # Создать recovery checkpoint
                        recovery_checkpoint = {
                            "phase": int(phase_num),
                            "phase_name": get_phase_name(int(phase_num)),
                            "batch": batch_num,
                            "timestamp": commit_date.strip(),
                            "session_id": f"git-recovery-{commit_hash[:8]}",
                            "mode": mode,
                            "state": {
                                "current_action": f"Recovered from Git commit: {commit_hash[:8]}",
                                "files_created": [],  # Будет определено из файлов в коммите
                                "context_files": []
                            },
                            "stats": {
                                "total_files": 0,
                                "elapsed_time": "Unknown"
                            },
                            "recovered_from_git": True,
                            "git_commit": commit_hash
                        }
                        
                        print(f"✅ Найден Git checkpoint: PHASE {phase_num}" + 
                              (f", batch {batch_num}" if batch_num else ""))
                        return recovery_checkpoint
        except Exception as e:
            print(f"⚠️  Ошибка при восстановлении через Git: {e}")
            return None
    
    print("❌ Не удалось восстановить checkpoint из Git истории")
    return None
```

---

## 🔍 check_backend_data_exists()

**Назначение:** Проверяет наличие backend raw data для conditional PHASE 5.7.

**Возвращает:** `(exists: bool, details: dict)`

**Псевдокод:**

```python
def check_backend_data_exists():
    """
    Проверяет наличие backend raw data в 00_BACKEND_RAW_DATA/ или существующий код.
    Returns: (exists: bool, details: dict)
    """
    print("\n🔍 Checking for backend raw data...\n")
    
    backend_folders = {
        "chats": "UPMT/bootstrap/00_BACKEND_RAW_DATA/chats/",
        "api_docs": "UPMT/bootstrap/00_BACKEND_RAW_DATA/api_docs/",
        "database": "UPMT/bootstrap/00_BACKEND_RAW_DATA/database/",
        "entities": "UPMT/bootstrap/00_BACKEND_RAW_DATA/entities/",
        "services": "UPMT/bootstrap/00_BACKEND_RAW_DATA/services/"
    }
    
    found_files = {}
    total_files = 0
    
    for category, folder in backend_folders.items():
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
    
    # Также проверяем существующий код (если existing_project)
    existing_code_backend = False
    if metadata.get('existing_project', {}).get('enabled', False):
        # Проверить наличие backend кода
        backend_code_paths = [
            "src/api/",
            "src/server/",
            "src/services/",
            "src/lib/api/",
            "app/api/",
            "pages/api/"
        ]
        
        for path in backend_code_paths:
            if directory_exists(path) and len(list_files(path)) > 0:
                existing_code_backend = True
                print(f"   ✅ Existing backend code found: {path}")
                break
    
    if total_files > 0 or existing_code_backend:
        print(f"\n✅ Backend data DETECTED: {total_files} files" + 
              (" + existing code" if existing_code_backend else ""))
        print(f"   → PHASE 5.7 (Backend Documentation) WILL BE EXECUTED\n")
        return (True, {
            "total_files": total_files,
            "files_by_category": found_files,
            "existing_code": existing_code_backend
        })
    else:
        print(f"\nℹ️ No backend data found (only README files)")
        print(f"   → PHASE 5.7 (Backend Documentation) WILL BE SKIPPED\n")
        return (False, {})
```

**Готово к интеграции в UPMT v3.0.2+** ✅

