# Recovery Scenarios

**Версия:** 1.0.0

## СЦЕНАРИЙ B: Нет checkpoint (Git recovery)

Восстановление по Git history + session logs

**Действия:**
1. Проверь последний commit в .dev/logs/
2. Прочитай последний session log
3. Восстанови контекст из log
4. Создай новый checkpoint
5. Продолжи с определенной точки

## СЦЕНАРИЙ C: Handoff from another agent

Чтение handoff report и продолжение работы

**Действия:**
1. Прочитай .dev/handoff/handoff-to-web-*.md
2. Загрузи контекст из handoff
3. Открой указанные файлы
4. Продолжи с указанной точки
5. Создай checkpoint после первой итерации

