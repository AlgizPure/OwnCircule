# 🔧 WEB DEV ADAPTER

**Версия:** 1.0.0
**Для:** Claude Code Web (GitHub API based development)

## Особенности Web Mode

- Работа через GitHub API
- Нет прямого доступа к файловой системе
- Все операции через gh CLI или API calls
- Checkpoint через GitHub файлы

## Functions

### save_checkpoint_web()
`python
gh api --method PUT /repos/{owner}/{repo}/contents/.dev/checkpoints/latest.json \
  -f message='checkpoint: dev session' \
  -f content='{base64_encoded_checkpoint}'
`

### read_files_web()
`ash
gh api /repos/{owner}/{repo}/contents/{file_path} --jq '.content' | base64 -d
`

**Детали:** См. UPMT/prompts/adapters/web-adapter.md для bootstrap операций
