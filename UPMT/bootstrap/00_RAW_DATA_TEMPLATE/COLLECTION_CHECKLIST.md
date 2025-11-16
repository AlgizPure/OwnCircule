# DATA COLLECTION CHECKLIST

Use this checklist to ensure you've collected all necessary data.

---

## =� PREPARATION

- [ ] Read `README_UPMT_raw_data_collection.md` in this folder
- [ ] Read `UPMT_START_HERE.md` in project root
- [ ] Have all project materials accessible

---

## =� CHATS

### For Each Chat Platform

#### Gemini (Google AI Studio)

- [ ] Go to https://aistudio.google.com
- [ ] Open relevant chat
- [ ] Copy entire conversation
- [ ] Save to `/chats/gemini-[topic]-[YYYY-MM].txt`
- [ ] Repeat for all relevant chats

**Format:**
```
gemini-vision-2025-01.txt
gemini-features-2025-03.txt
gemini-tech-stack-2025-08.txt
```

#### Claude (Claude.ai)

- [ ] Go to https://claude.ai
- [ ] Open relevant chat
- [ ] Copy conversation OR use export (if available)
- [ ] Save to `/chats/claude-[topic]-[YYYY-MM].md`
- [ ] Repeat for all relevant chats

**Format:**
```
claude-architecture-2025-08.md
claude-user-flows-2025-09.md
```

#### ChatGPT

- [ ] Go to https://chat.openai.com
- [ ] Open relevant chat
- [ ] Click share � Copy link or export
- [ ] Save to `/chats/chatgpt-[topic]-[YYYY-MM].txt`

#### Other Platforms

- [ ] [Platform name]: [Export method]
- [ ] Save to `/chats/[platform]-[topic]-[date].txt`

### Chat Checklist

- [ ] All relevant chats exported?
- [ ] File names include date (YYYY-MM)?
- [ ] File names include topic/theme?
- [ ] Text is readable (not garbled)?
- [ ] Very long chats split into parts?

---

## =� DOCUMENTS

### Google Docs

- [ ] Open each relevant Doc
- [ ] File � Download � Markdown (.md)
- [ ] Save to `/documents/[descriptive-name].md`
- [ ] Repeat for all Docs

**Examples:**
```
vision-statement.md
feature-list.md
user-personas.md
competitive-analysis.md
```

### Other Document Types

**PDFs:**
- [ ] Copy to `/documents/[name].pdf`

**Images (Wireframes, Diagrams):**
- [ ] Copy to `/documents/[name].png` (or .jpg)

**Notion Pages:**
- [ ] Export as Markdown
- [ ] Save to `/documents/[name].md`

**Excel/Sheets:**
- [ ] Export as CSV
- [ ] Save to `/documents/[name].csv`

### Document Checklist

- [ ] All relevant documents exported?
- [ ] File names are descriptive?
- [ ] Markdown format preferred (when possible)?
- [ ] Images readable (if screenshots)?

---

## =� NOTES

### Loose Notes, Ideas

- [ ] Copy any text files with ideas
- [ ] Copy any code snippets (prototypes)
- [ ] Copy any rough drafts
- [ ] Save to `/notes/[descriptive-name].txt` or `.md`

**Examples:**
```
initial-ideas.txt
architecture-sketch.md
code-prototype.js
brainstorm-session.md
```

### Notes Checklist

- [ ] All relevant notes collected?
- [ ] No important ideas lost?
- [ ] File names descriptive?

---

## <� METADATA

### Fill metadata.yaml

Open `/00_RAW_DATA_TEMPLATE/metadata.yaml` and fill:

- [ ] Project name
- [ ] Total chats count
- [ ] Total documents count
- [ ] Date range of materials
- [ ] For each chat file:
  - [ ] File name
  - [ ] Topics discussed
  - [ ] Date
- [ ] Known decisions (what's already decided)
- [ ] Known contradictions (what conflicts)
- [ ] Questions to resolve (what's unclear)

**See `metadata.yaml` for template**

---

##  FINAL CHECKS

- [ ] All files in correct folders?
- [ ] metadata.yaml completely filled?
- [ ] File names follow naming conventions?
- [ ] No sensitive data (passwords, keys) in files?
- [ ] Everything committed to git?

### Git Commit
```bash
cd /path/to/project

# Check what's new
git status

# Add all raw data
git add 00_RAW_DATA_TEMPLATE/

# Commit
git commit -m "Add: Raw project data for bootstrap"

# Verify
git log --oneline -1
```

---

## =� READY TO BOOTSTRAP!

Once all checkboxes are , you're ready to:

1. Launch Claude Code
2. Start bootstrap process
3. See `UPMT_START_HERE.md` for next steps

---

**Questions?** Check `UPMT_START_HERE.md` or `docs/core/99_SYSTEM_GUIDE.md`
