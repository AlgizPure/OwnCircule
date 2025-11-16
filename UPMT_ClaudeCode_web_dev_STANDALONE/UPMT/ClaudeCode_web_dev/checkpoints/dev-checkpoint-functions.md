# Checkpoint Functions

**Версия:** 1.0.0

---

## save_checkpoint_cli()

**Для:** CLI/Cursor mode

```python
import json
import os
from datetime import datetime

def save_checkpoint_cli(
    type="development_session",
    current_task=None,
    completed_today=[],
    next_actions=[],
    files_modified=[],
    commits=[],
    stats={}
):
    # Create directory if not exists
    os.makedirs('.dev/checkpoints', exist_ok=True)
    
    # Build checkpoint
    checkpoint = {
        "type": type,
        "session_id": f"dev-cli-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "mode": "CLI",
        "current_task": current_task,
        "completed_today": completed_today,
        "next_actions": next_actions,
        "files_modified": files_modified,
        "commits": commits,
        "stats": stats
    }
    
    # Save latest.json
    with open('.dev/checkpoints/latest.json', 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Checkpoint saved: {checkpoint['session_id']}")
```

---

## save_checkpoint_web()

**Для:** Claude Code Web (GitHub API)

```bash
# Variables
OWNER="your-username"
REPO="your-repo"
CHECKPOINT_JSON="[JSON checkpoint content]"
CHECKPOINT_BASE64=$(echo "$CHECKPOINT_JSON" | base64)

# Get existing file SHA (if exists)
EXISTING_SHA=$(gh api /repos/$OWNER/$REPO/contents/.dev/checkpoints/latest.json \
  --jq '.sha' 2>/dev/null || echo "")

# PUT request to GitHub API
if [ -z "$EXISTING_SHA" ]; then
  # File doesn't exist, create it
  gh api --method PUT /repos/$OWNER/$REPO/contents/.dev/checkpoints/latest.json \
    -f message="checkpoint: dev session" \
    -f content="$CHECKPOINT_BASE64"
else
  # File exists, update it
  gh api --method PUT /repos/$OWNER/$REPO/contents/.dev/checkpoints/latest.json \
    -f message="checkpoint: dev session update" \
    -f content="$CHECKPOINT_BASE64" \
    -f sha="$EXISTING_SHA"
fi
```

---

## read_checkpoint_cli()

```python
import json

def read_checkpoint_cli():
    try:
        with open('.dev/checkpoints/latest.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
```

---

## read_checkpoint_web()

```bash
gh api /repos/$OWNER/$REPO/contents/.dev/checkpoints/latest.json \
  --jq '.content' | base64 -d | jq '.'
```

---

**См. также:**
- `dev-checkpoint-system.md` - Полная документация checkpoint системы
- `UPMT/prompts/utils/checkpoint-functions.md` - Bootstrap checkpoint функции

