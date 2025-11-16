# Code Quality Checklist

**Версия:** 1.0.0  
**Используй перед каждым commit!**

---

## ✅ PRE-COMMIT CHECKLIST

### 1. TypeScript

- [ ] **TypeScript strict mode** (no `any` types)
- [ ] **Explicit return types** для функций
- [ ] **No TypeScript errors** (`tsc --noEmit`)
- [ ] **Proper types для props/params**

---

### 2. Code Style

- [ ] **ESLint: no errors**
  ```bash
  npm run lint
  ```

- [ ] **Prettier: formatted**
  ```bash
  npm run format
  ```

- [ ] **Naming conventions** consistent
- [ ] **Imports organized** (absolute/relative)

---

### 3. Code Quality

- [ ] **No console.log в production** code
- [ ] **Error handling** добавлен
- [ ] **Comments** для сложного кода
- [ ] **No commented-out code** (удали или объясни)
- [ ] **Single Responsibility** principle
- [ ] **DRY** (no code duplication)

---

### 4. Testing

- [ ] **Tests pass** (`npm test`)
- [ ] **New tests added** (если новая логика)
- [ ] **Coverage** не упала
- [ ] **Edge cases** covered

---

### 5. Documentation

- [ ] **Docs updated** (если изменился API/поведение)
- [ ] **README updated** (если новая фича)
- [ ] **Comments updated** (если изменилась логика)
- [ ] **Project Rules** checked (обновлены ли связанные docs?)

---

### 6. Performance

- [ ] **No N+1 queries** (database)
- [ ] **Proper indexes** используются
- [ ] **Lazy loading** где нужно
- [ ] **No memory leaks** (check subscriptions/listeners)

---

### 7. Security

- [ ] **Input validation** добавлена
- [ ] **SQL injection** protected
- [ ] **XSS protection** added
- [ ] **No secrets в code** (используй env vars)

---

### 8. Git

- [ ] **Branch up to date** with main
- [ ] **Conflicts resolved**
- [ ] **Commit message** follows format
  ```
  type(scope): description
  ```

- [ ] **Small commits** (одна задача = один commit)

---

### 9. Dependencies

- [ ] **No unused dependencies** (`npm prune`)
- [ ] **Versions pinned** (no `^` or `~` в production deps)
- [ ] **Security vulnerabilities** checked
  ```bash
  npm audit
  ```

---

### 10. Code Review (Self-Review)

- [ ] **Прочитал весь свой код**
- [ ] **Удалил debug code**
- [ ] **Проверил edge cases**
- [ ] **Убедился что не сломал другой код**

---

## 🚀 OPTIONAL (но рекомендуется)

### Performance Testing

- [ ] **Load tested** (если критичная фича)
- [ ] **Memory profiled** (если работа с большими данными)
- [ ] **Bundle size** checked (frontend)

### Accessibility

- [ ] **Keyboard navigation** works
- [ ] **Screen reader** friendly
- [ ] **Color contrast** sufficient (WCAG AA)

### i18n

- [ ] **No hardcoded strings** (если проект i18n)
- [ ] **Translation keys** added

---

## ❌ BLOCKERS (НЕ КОММИТЬ если есть)

- ❌ **TypeScript errors**
- ❌ **Linter errors**
- ❌ **Tests failing**
- ❌ **Build failing**
- ❌ **Merge conflicts**
- ❌ **console.log в production code**
- ❌ **Secrets в code**

---

## ✅ READY TO COMMIT

**Если все чекбоксы отмечены:**

```bash
git add [files]
git commit -m "type(scope): description"
git push
```

**Создай checkpoint:**
- Checkpoint автоматически создастся после commit
- Session log обновится
- Progress tracking обновится

---

**После commit:**

```
✅ Code committed
✅ Checkpoint saved
✅ Session log updated
✅ Ready for next iteration
```

---

**См. также:**
- `dev-rules.md` - Детальные правила разработки
- `dev-orchestrator.md` - Цикл dev итераций

