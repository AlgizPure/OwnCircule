# 🔧 CLI DEV ADAPTER

**Версия:** 1.0.0
**Для:** CLI/Cursor (Local file system development)

## Особенности CLI Mode

- Прямой доступ к файловой системе
- Быстрые операции с файлами
- Локальный Git
- Checkpoint в локальные файлы

## Functions

### save_checkpoint_cli()
`python
import json
with open('.dev/checkpoints/latest.json', 'w') as f:
    json.dump(checkpoint, f, indent=2)
`

### read_files_cli()
`python
with open(file_path, 'r') as f:
    return f.read()
`

**Детали:** См. UPMT/prompts/adapters/cli-adapter.md для bootstrap операций
