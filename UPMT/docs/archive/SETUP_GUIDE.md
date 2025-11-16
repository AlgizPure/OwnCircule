# PROJECT SETUP GUIDE
## From Template to Working Project in 2-4 Hours

**РЕКОМЕНДАЦИЯ:** Если впервые используешь template, начни с → **[00_START_HERE.md](00_START_HERE.md)**

Этот документ содержит детальные инструкции для всех сценариев.

---

## OVERVIEW

This template provides complete project management infrastructure.

**Time Investment:**
- Your time: ~2 hours (data collection + verification)
- Claude Code time: 2-4 hours (autonomous work)
- **Total: One afternoon to production-ready documentation**

---

## =� PREPARATION (Before You Start)

### What You Need

 Project idea (at least high-level vision)
 Chat transcripts with AI about project (if any)
 Documents/notes about project (if any)
 GitHub account (for repository)
 Claude Code installed (or Claude.ai access)

### What You Get

 Complete documentation structure
 Project requirements (PRD, roadmap, tech stack)
 Module specifications
 AI assistant configurations
 Progress tracking system
 Ready to start coding!

---

## =� STEP-BY-STEP PROCESS

### STEP 1: Create New Project from Template (5 min)

```bash
# Option A: GitHub Template
# 1. Click "Use this template" on GitHub
# 2. Name your new project
# 3. Clone locally

# Option B: Manual Copy
git clone https://github.com/your-username/project-management-template.git
mv project-management-template my-new-project
cd my-new-project
rm -rf .git
git init
git add .
git commit -m "Initial: Project from template"
```

---

### STEP 2: Collect Raw Data (15-30 min)

Navigate to: `00_RAW_DATA_TEMPLATE/`

Follow: `COLLECTION_CHECKLIST.md`

#### 2.1: Gather Chat Transcripts

**Where to find:**
- Gemini: AI Studio � [your chat] � Copy conversation
- Claude: claude.ai � [chat] � Copy or export
- ChatGPT: chat.openai.com � [chat] � Share � Export

**What to save:**

```bash
cd 00_RAW_DATA_TEMPLATE/chats/

# For each chat:
# 1. Copy full conversation
# 2. Save as: [ai-name]-[topic]-[date].txt
# Example: gemini-vision-2024-01.txt

# Name format:
[ai-name]-[main-topic]-[YYYY-MM].txt

# If chat is HUGE (>50k words):
# Break into parts:
gemini-vision-2024-01-part1.txt
gemini-vision-2024-01-part2.txt
```

#### 2.2: Gather Documents

**Where to find:**
- Google Docs: File � Download � Markdown (.md)
- Notion: Export as Markdown
- Local files: Copy directly

**What to save:**

```bash
cd 00_RAW_DATA_TEMPLATE/documents/

# Save as markdown if possible
# If PDF/Word, that's ok too

vision-statement.md
feature-list.md
user-flows.pdf
wireframes.pdf
```

#### 2.3: Gather Notes

**Any other relevant files:**

```bash
cd 00_RAW_DATA_TEMPLATE/notes/

# Code snippets, ideas, sketches, etc.
ideas.txt
code-experiments.js
architecture-sketch.md
```

#### 2.4: Fill Metadata

**Edit:** `00_RAW_DATA_TEMPLATE/metadata.yaml`

```yaml
project:
  name: "Your Project Name"  # � Fill this
  status: "Pre-development"

data_info:
  total_chats: 3              # � Count your files
  total_documents: 5          # � Count your files
  date_range: "2024-01 to 2025-11"  # � Your range

  sources:
    # For EACH chat file:
    - name: "Gemini - Vision Discussion"
      files: ["gemini-vision-2024-01.txt"]  # � File name
      topics: ["Vision, core features, audience"]  # � What discussed
      date: "2024-01"           # � When

    # Add more sources...

known_decisions:
  # What's already decided?
  - "Project Name: [name]"
  - "Target Audience: [who]"
  - "Core Features: [list]"

known_contradictions:
  # What contradicts between chats?
  - "Tech stack: MongoDB vs PostgreSQL in different chats"
  - "Feature priorities changed over time"

questions_to_resolve:
  # What needs clarification?
  - "Final tech stack?"
  - "MVP timeline?"
```

**CHECKLIST:**
- [ ] All chats copied to `/chats/`
- [ ] All documents copied to `/documents/`
- [ ] All notes copied to `/notes/`
- [ ] metadata.yaml filled
- [ ] Committed to git

```bash
git add 00_RAW_DATA_TEMPLATE/
git commit -m "Add: Raw project data"
```

---

### STEP 3: Launch Claude Code (5 min)

```bash
# Navigate to project root
cd /path/to/my-new-project

# Launch Claude Code
claude
```

**First prompt:**

```
I'm setting up a new project using the project management template.

Please read:
1. /01_BOOTSTRAP_CONFIG/BOOTSTRAP_INSTRUCTIONS.md
2. /00_RAW_DATA_TEMPLATE/metadata.yaml
3. All files in /00_RAW_DATA_TEMPLATE/

Then start the bootstrap process as described in BOOTSTRAP_INSTRUCTIONS.

Begin with Phase 1: ANALYSIS.
```

---

### STEP 4: Let Claude Code Analyze (1-2 hours autonomous)

**Claude Code will:**
- Read all your data
- Extract information
- Find contradictions
- Identify gaps
- Generate analysis report

**You can:**
- Step away 
- Do other work
- Check back periodically

**Claude Code will notify you when ready for Phase 2.**

---

### STEP 5: Tech Stack Verification (45-60 min)

#### 5.1: Claude Code Generates Prompt

**Claude Code will:**

```
 Analysis complete!
 Found 5 contradictions
 Identified 8 gaps

Starting tech stack verification...
Generated verification prompt at:
/verification/VERIFICATION_PROMPT_FOR_CLAUDE.md

---

� MANUAL STEP NEEDED:

Your raw data mentions technologies from Jan 2024.
Need to verify they're still optimal for Nov 2025.

Please:
1. Open: /verification/VERIFICATION_PROMPT_FOR_CLAUDE.md
2. Copy the entire prompt
3. Go to: claude.ai (web interface)
4. Paste and send
5. Wait for comprehensive tech stack analysis
6. Copy Claude's response
7. Save to: /verification/tech-stack-analysis.md
8. Commit: git add . && git commit -m "Add: Tech stack verification"
9. Return here and type "continue"

This ensures your tech stack is current! =
```

#### 5.2: You Do Research (via Claude.ai)

```bash
# 1. Open file
cat verification/VERIFICATION_PROMPT_FOR_CLAUDE.md

# 2. Copy entire contents

# 3. Go to claude.ai in browser

# 4. New chat, paste prompt

# 5. Claude.ai researches (uses web search)
#    This takes 10-20 minutes
#    Claude will search:
#    - Current versions
#    - Trends and benchmarks
#    - Best practices 2025
#    - Alternatives

# 6. Copy Claude's full response

# 7. Save locally
cat > verification/tech-stack-analysis.md
[paste response]
Ctrl+D

# 8. Commit
git add verification/
git commit -m "Add: Tech stack verification from Claude.ai research"
```

#### 5.3: Back to Claude Code

```bash
# In Claude Code session:
You: "continue"

Claude Code:
Reading verification results...
Processing recommendations...
Making final tech stack decisions...

 Tech stack verified!

Recommendations:
- React 18.2 � 19.0 (UPGRADE)
- Express � Fastify (REPLACE for better performance)
- Add Tailwind CSS (current best practice)
- PostgreSQL confirmed 

[detailed breakdown...]

Approve? (yes/no/adjust)
```

**You respond:** `yes` (or adjust as needed)

---

### STEP 6: Interview with Claude Code (30-60 min)

**Claude Code asks questions in batches:**

```
=� CRITICAL QUESTIONS (must answer):

Based on analysis, I need decisions on:

1. Database (CONTRADICTION FOUND):
   " Early chats: MongoDB
   " Later chat: PostgreSQL
   " Verification: PostgreSQL recommended for your data model

   Final decision: ____

2. Authentication:
   " Not specified in raw data
   " Options: JWT / OAuth / Session-based
   " Recommendation: JWT (stateless, scalable)

   Your choice: ____

[... more critical questions ...]

---

Answer in format:
1. PostgreSQL
2. JWT
3. ...

Or discuss any question individually.
```

**You answer questions.**

**Claude Code continues with IMPORTANT, then OPTIONAL questions.**

**Process:**
- Critical: ~5 questions (must answer)
- Important: ~10 questions (should answer)
- Optional: ~5 questions (can infer)

**Your choice:** Answer all or let Claude infer some.

---

### STEP 7: Claude Code Works Autonomously (2-4 hours)

**After interview, Claude Code:**

```
 All questions answered!
 Tech stack verified!
 Contradictions resolved!

Starting autonomous deployment...

Phase 3: SYNTHESIS (15 min)
Phase 4: DOCUMENTATION (2-3 hours)
Phase 5: VALIDATION (15 min)

You can step away. I'll notify you at milestones.
```

**Progress updates:**

```bash
[30 min]   Created PROJECT_CORE/ (5 files)
           PROJECT_ESSENCE.md filled
           PRD.md 60% complete

[60 min]   PRD.md complete (15 features, 30 user stories)
           ROADMAP.md (MVP + 2 phases)
           TECH_STACK.md (with verification data)

[90 min]   ARCHITECTURE.md complete
           Started module requirements (4/10)

[120 min]  All 10 modules created
           CONTEXT_MEMORY files filled
           PROGRESS_TRACKING set up

[150 min]  Validation running...
           Checking consistency...
           Verifying cross-references...

[180 min]  BOOTSTRAP COMPLETE!
```

---

### STEP 8: Review Results (30-40 min)

**Claude Code generates:**

```
<� PROJECT BOOTSTRAP COMPLETE!

=� Generated:
- 52 files
- ~150 pages of documentation
- 10 modules specified
- 30 user stories
- 75 functional requirements

=� Review checklist created:
� Open: /REVIEW_CHECKLIST.md

Follow checklist to review systematically:
1. PROJECT_ESSENCE (5 min)
2. PRD (15 min)
3. ROADMAP (5 min)
4. TECH_STACK (5 min - already verified!)
5. ARCHITECTURE (10 min)
6. Module requirements (5 min - spot check)
7. TODOs (5 min)

Total: ~40 minutes

Start review? I can guide you through each document.
```

**You review:**
- Follow checklist
- Approve or request changes
- Mark TODOs for later

---

### STEP 9: Finalize (10 min)

**After review:**

```bash
# Claude Code asks:
Any changes needed? (yes/no)

# If yes: You discuss, Claude updates
# If no:

Claude Code:
 Finalizing...
 Committing all documentation...
 Generating final report...

---

<� PROJECT SETUP COMPLETE!

Repository structure:
/02_PROJECT_STRUCTURE/  � All documentation ready
/verification/          � Tech stack research saved
/00_RAW_DATA_TEMPLATE/  � Original data preserved

Next steps:
1. Share docs with team (if applicable)
2. Set up development environment
3. Start implementing!

Documentation is version-controlled and can evolve.

Ready to code? =�
```

**Commit everything:**

```bash
git add .
git commit -m "Bootstrap complete: Full project documentation"
git push origin main
```

---

## <� YOU'RE DONE!

**What you have:**
 Complete project vision (PROJECT_ESSENCE)
 Detailed requirements (PRD)
 Clear roadmap (ROADMAP)
 Verified tech stack (TECH_STACK)
 System architecture (ARCHITECTURE)
 Module specifications (requirements/)
 AI assistant rules (.cursorrules, .clauderules)
 Progress tracking ready
 Context management set up

**What you can do:**
 Start development immediately
 Onboard team members (all docs ready)
 Use AI assistants (configured)
 Track progress from day 1
 Never lose context
 Scale the project

---

## = UPDATING THE TEMPLATE

After completing multiple projects, you'll learn what works.

**Update the template:**

```bash
# Go to template repo
cd /path/to/project-management-template

# Pull learnings from completed project
cp /path/to/completed-project/AI_INSTRUCTIONS/.cursorrules ./02_PROJECT_STRUCTURE/AI_INSTRUCTIONS/
# (if you improved the rules)

# Add new examples
cp -r /path/to/completed-project/02_PROJECT_STRUCTURE/ ./04_EXAMPLES/example-project-2/

# Update documentation
# Edit SETUP_GUIDE.md with new insights

# Commit and push
git add .
git commit -m "Update: Template improvements from Project X"
git push origin main
```

**All future projects get the improvements!** <�

---

## � TROUBLESHOOTING

### Claude Code doesn't start bootstrap

**Fix:**

```bash
# Ensure you're in project root
pwd  # Should show project directory

# Check BOOTSTRAP_INSTRUCTIONS exists
ls 01_BOOTSTRAP_CONFIG/BOOTSTRAP_INSTRUCTIONS.md

# Try explicit prompt:
claude --prompt "@01_BOOTSTRAP_CONFIG/BOOTSTRAP_INSTRUCTIONS.md Start bootstrap process"
```

### Verification prompt generation fails

**Fix:**
- Manually copy template from `01_BOOTSTRAP_CONFIG/tech-stack-verification.md`
- Fill in your project details
- Use in Claude.ai

### Claude Code asks too many questions

**Fix:**
- Say: "Infer reasonable defaults, I'll adjust later"
- Review inferred decisions in generated docs
- Update as needed

### Tech stack analysis incomplete

**Fix:**
- In Claude.ai, ask follow-up questions
- Be specific: "Compare X vs Y for [use case]"
- Ask for benchmarks, recent articles
- Synthesize yourself if needed

---

## =� TIPS FOR BEST RESULTS

### When Collecting Data

 DO:
- Include ALL relevant chats (even old ones)
- Note dates (helps with chronology)
- Mark contradictions in metadata
- Include visual materials (wireframes, diagrams)

L DON'T:
- Skip old chats (even if decisions changed)
- Delete contradictory information
- Try to "clean up" data first
- Omit uncertain ideas

### When Answering Questions

 DO:
- Answer critical questions carefully
- Say "I don't know" if unsure (Claude will infer)
- Ask Claude to explain options if unclear
- Take time to think

L DON'T:
- Rush through questions
- Guess if uncertain
- Skip questions (mark for later if needed)
- Contradict your raw data without reason

### When Reviewing

 DO:
- Read PROJECT_ESSENCE carefully (foundation)
- Spot-check requirements (sample modules)
- Verify tech stack makes sense
- Check for glaring omissions

L DON'T:
- Try to perfect everything now (can iterate)
- Get stuck on minor details
- Rewrite everything (trust the process)
- Delay starting development

---

## <� LEARNING RESOURCES

After setup, read these from your project:

1. `/02_PROJECT_STRUCTURE/PROJECT_CORE/99_SYSTEM_GUIDE.md`
   � Understand how the system works

2. `/02_PROJECT_STRUCTURE/AI_INSTRUCTIONS/WORKFLOW_GUIDE.md`
   � Daily workflows for development

3. `/02_PROJECT_STRUCTURE/AI_INSTRUCTIONS/CHANGE_SCENARIOS.md`
   � How to handle changes

---

## <� GETTING HELP

If stuck:

1. **Check this guide** (you are here)
2. **Read SYSTEM_GUIDE.md** (comprehensive)
3. **Ask Claude Code**: "How do I [X]?"
4. **Check examples**: `04_EXAMPLES/`
5. **Review template repo**: Issues, Discussions

---

**Ready to bootstrap your first project?** =�

Follow STEP 1 above and let's go!
