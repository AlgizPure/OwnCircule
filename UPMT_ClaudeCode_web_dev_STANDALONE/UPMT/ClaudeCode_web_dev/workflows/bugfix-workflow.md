# 🐛 BUG FIX WORKFLOW

**Версия:** 1.0.0

## Шаги

1. **Reproduce:** Воспроизведи баг локально
2. **Root Cause:** Найди причину (debug, logs)
3. **Fix:** Исправь минимальными изменениями
4. **Test Fix:** Проверь что баг исправлен
5. **Regression Test:** Проверь что ничего не сломалось
6. **Commit:** git commit -m "fix(module): bug description"
7. **Checkpoint:** Сохрани checkpoint
8. **Report:** Добавь в session log

## Best Practices

- Minimal changes
- Add test для предотвращения regression
- Update docs если баг был из-за неправильной docs
