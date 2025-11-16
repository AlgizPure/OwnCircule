# 🎯 Universal Project Management Template

[![Version](https://img.shields.io/badge/version-2.2.1-blue.svg)](https://github.com/AlgizPure/project-management-template/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/language-Hybrid%20(RU%2FEN)-orange.svg)](README.md)
[![AI Optimized](https://img.shields.io/badge/AI-Optimized-purple.svg)](README.md)
[![Documentation](https://img.shields.io/badge/docs-15000%2B%20lines-brightgreen.svg)](README.md)
[![Last Commit](https://img.shields.io/github/last-commit/AlgizPure/project-management-template)](https://github.com/AlgizPure/project-management-template/commits/main)

**Version:** 2.2.1
**Last Updated:** 2025-11-11
**Status:** Production Ready

---

## 📖 What Is This?

A **complete, reusable template** for setting up documentation-driven project management with AI assistance.

Transform chaotic project ideas (scattered across chats and docs) into a fully structured, production-ready documentation system in **one afternoon**.

---

## ✨ Features

- 📋 **Complete Documentation Structure** - PRD, roadmap, architecture, tech stack, design system, backend docs
- 🤖 **AI-Optimized** - Works with Claude Code, Cursor, and other AI assistants
- 🔍 **Tech Stack Verification** - Automatically verify technologies are current (2025)
- 📊 **Progress Tracking** - Built-in systems for tracking development
- 🔄 **Context Preservation** - Never lose project context between sessions
- 🚀 **Bootstrap Automation** - Claude Code can set everything up autonomously
- ✅ **Completeness Validation** - Guaranteed 100% documentation completeness (v2.0+)
- 🎨 **Design System Integration** - Automatic design documentation from raw data or code (v2.2+)
- 🔧 **Backend Documentation** - Intelligent backend docs generation with inference (v2.2.1+)
- 📜 **24 Automated Rules** - Auto-update documentation based on triggers (v2.0+)

---

## 🎯 Perfect For

- ✅ Solo developers starting new projects
- ✅ Small teams (2-10 people)
- ✅ Projects with scattered planning materials
- ✅ AI-assisted development workflows
- ✅ Developers who lose context between sessions
- ✅ Anyone who wants structure without bureaucracy

---

## 🚀 Quick Start

**→ [UPMT_START_HERE.md](../UPMT_START_HERE.md) - Выбери свой сценарий и начни!**

**4 сценария bootstrap:**

- 🖥️ CLI + New Project → Local work, ideas only
- 🖥️ CLI + Existing Project → Local work, add docs to code
- 🌐 Web + New Project → GitHub-based, ideas only
- 🌐 Web + Existing Project → GitHub-based, add docs to code

**Key Features:**

- 🤖 **Auto-fill metadata** - Just answer questions, no manual YAML editing
- 🔍 **Smart recommendations** - Tech stack verified against 2025 best practices
- 📊 **Existing code analysis** - Automatically detects features and tech in use
- 🔄 **Modernization suggestions** - Identifies outdated decisions and suggests updates

**Time:** ~1 hour your input + 2-4 hours Claude (autonomous) = **Production-ready docs** 🎉

---

## 📦 What You Get

After bootstrap, you'll have:

```text
my-new-project/
├── docs/                               ✅ Project documentation
│   ├── core/                          ✅ Core docs (PRD, roadmap, tech stack, architecture)
│   ├── requirements/                  ✅ Module requirements
│   ├── progress/                      ✅ Progress tracking
│   ├── design/                        ✅ Design system (if design data provided)
│   └── backend/                       ✅ Backend docs (if backend detected)
│       ├── entities/                  ✅ Entity documentation with ERD
│       ├── api/                       ✅ API endpoint documentation
│       ├── services/                  ✅ Service documentation
│       ├── database/                  ✅ Database schema & relationships
│       └── relationships_matrix.md    ✅ Visual relationship maps (Mermaid diagrams)
│
├── .context/                          ✅ Project context memory
│   ├── state.md                       ✅ Current state
│   ├── decisions.md                   ✅ Decision log
│   ├── insights.md                    ✅ Learnings
│   └── changes_log.md                 ✅ Change history
│
├── .upmt/                             ✅ UPMT metadata
│   └── metadata.yaml                  ✅ Auto-filled project metadata
│
├── .cursorrules                       ✅ AI assistant rules (auto-generated)
│
└── UPMT/                              🔒 Template infrastructure (static)
    ├── bootstrap/                     🔒 Bootstrap configs
    └── structure-templates/           🔒 Templates
```

**Plus:**

- All cross-references working
- Version numbers set
- Change logs initialized
- 100% completeness validated (PHASE 7.5)
- Design system documented (if applicable)
- Backend documentation generated (if applicable)
- Ready for Day 1 of development

---

## 🎓 Learn More

**Essential Reading:**

1. `UPMT_START_HERE.md` - Quick Start guide
2. `docs/core/99_SYSTEM_GUIDE.md` - System philosophy
3. `UPMT/structure-templates/AI_INSTRUCTIONS/WORKFLOW_GUIDE.md` - Daily workflows
4. `UPMT/bootstrap/BOOTSTRAP_CONFIG/BOOTSTRAP_INSTRUCTIONS.md` - Detailed bootstrap process
5. `UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md` - 16 automated rules
6. `UPMT/structure-templates/AI_INSTRUCTIONS/UPMT.md` - Master reference

**Examples:**

- See `UPMT/structure-templates/AI_INSTRUCTIONS/EXAMPLES/` for code examples
- See `UPMT/structure-templates/backend-documentation/examples/` for backend doc examples
- See `docs/backend/relationships_matrix.md` (after bootstrap) for visual relationship maps with Mermaid diagrams

---

## 🛠️ AI Tools Supported

- ✅ **Claude Code** (CLI) - Best for bootstrap & autonomous work
- ✅ **Cursor** (IDE) - Best for development
- ✅ **Claude.ai** (Web) - Best for research & planning
- ✅ Other AI assistants (with .cursorrules)

---

## 📊 System Features

### Documentation-Driven Development

Every code change references requirements:

```typescript
// Implements: FR-AUTH-005 (Avatar Upload)
// Requirements: /MODULES_REQUIREMENTS/auth_requirements.md
```

### Context Preservation

AI always knows:

- Current project state
- What was last worked on
- What's next
- What's blocked

### Progress Tracking

Real-time visibility:

```text
Auth Module:    ████████░░ 80%
Profile Module: ██████░░░░ 60%
Tasks Module:   ██░░░░░░░░ 20%

Overall: ███████░░░ 70% complete
```

### Automatic Documentation

System updates itself via 16 automated rules:

- State after each change
- Decisions logged
- Progress calculated
- Context maintained
- Design system synced (RULE_17)
- Backend docs updated (RULE_18-24)
- Cross-file validation (RULE_16)

**Rule Notifications:**

- 👀 Active rules shown at start of each phase
- ✅ Rules executed shown at end of each phase

---

## 🔄 Workflow

### Daily Development

```bash
# Morning
1. Claude Code reads state.md
2. Shows you current context
3. You confirm or adjust plan
4. Start coding

# During Day
1. Implement features
2. Reference requirements
3. Update progress
4. Commit with proper messages

# End of Day
1. Update state.md
2. Log decisions
3. Plan tomorrow
4. Commit
```

### With AI Assistants

```bash
# Claude Code (Autonomous)
claude
> "Implement FR-AUTH-005"
[Works autonomously following requirements]

# Cursor (Interactive)
# AI reads .cursorrules automatically
# References requirements in suggestions
# Updates docs as you code
```

---

## 🎯 Key Principles

1. **Single Source of Truth**
   Requirements are THE source, code implements them

2. **Context is King**
   Never lose project context, ever

3. **Documentation First**
   Write requirements before code

4. **AI-Friendly**
   Optimized for AI assistant workflows

5. **Incremental**
   Start simple, evolve as needed

6. **Practical**
   Just enough process, not too much

---

## 💡 Tips for Success

**Do:**

- ✅ Collect ALL materials (even old/outdated)
- ✅ Collect design materials (moodboards, Figma, screenshots) in `UPMT/bootstrap/00_DESIGN_RAW_DATA/`
- ✅ Let Claude Code auto-fill metadata.yaml (just answer questions)
- ✅ Let Claude Code work autonomously through all phases
- ✅ Review generated docs carefully (especially PHASE 7.5 validation)
- ✅ Keep state.md updated daily
- ✅ Trust the completeness validation (PHASE 7.5)

**Don't:**

- ❌ Skip data collection step
- ❌ Try to "clean up" raw data first
- ❌ Rush through Claude Code questions
- ❌ Skip PHASE 7.5 validation
- ❌ Forget to commit regularly
- ❌ Ignore the system (defeats the purpose)
- ❌ Manually edit metadata.yaml (use auto-fill mode)

---

## 🤝 Contributing

Found improvements? Learned patterns? Share them!

Submit PR with improvements or open a discussion on GitHub!

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

Built with:

- Claude (Anthropic) - AI assistance
- Years of project management trial & error
- Contributions from developers who used this

---

## 🆘 Support

**Issues:**

- GitHub Issues: [Report bugs or request features](https://github.com/AlgizPure/project-management-template/issues)
- Documentation: See `UPMT_START_HERE.md`
- System Guide: See `docs/core/99_SYSTEM_GUIDE.md`

**Questions:**

- Read docs first (most questions answered there)
- Check examples in `UPMT/structure-templates/AI_INSTRUCTIONS/EXAMPLES/`
- Read `UPMT/structure-templates/AI_INSTRUCTIONS/UPMT.md` for master reference
- Open discussion on [GitHub Discussions](https://github.com/AlgizPure/project-management-template/discussions)

---

## 🚀 Ready to Start?

```bash
# 1. Read quick start guide
cat UPMT_START_HERE.md

# 2. Choose your scenario (CLI/Web, New/Existing Project)

# 3. Collect raw data
# Put chats, docs, notes in UPMT/bootstrap/00_RAW_DATA_TEMPLATE/
# Put design materials in UPMT/bootstrap/00_DESIGN_RAW_DATA/ (optional)

# 4. Run bootstrap with Claude Code
# Copy prompt from BOOTSTRAP_START_PROMPT.md
# Follow all phases including PHASE 7.5 validation

# 5. Start building! 🎉
```

---

## Made with ❤️ for developers who love structure and AI assistance

---

## 🔗 Links

- [Quick Start](../UPMT_START_HERE.md)
- [System Guide](../docs/core/99_SYSTEM_GUIDE.md)
- [Release Notes - Current](./RELEASE_NOTES_v2.2.1.md)
- [Release Notes - Archive](./docs/archive/)
- [Version History](./VERSION_HISTORY.md)
- [GitHub Repository](https://github.com/AlgizPure/project-management-template)

---

## 📝 Changelog

### Version 2.2.1 (2025-11-11) - Backend Documentation System

**Major Feature:** Complete backend documentation integration

✨ **Backend Documentation Generation**

- Automatic backend documentation from raw data, code analysis, or intelligent inference
- PHASE 5.7: Backend Documentation Generation in bootstrap
- Code analysis extracts entities, API, services from existing code
- Entity documentation, API endpoints, database schema, ADRs
- Relationships Matrix with visual Mermaid diagrams

📁 **New Structure:**

- `UPMT/structure-templates/backend-documentation/` - Backend templates
- `docs/backend/` - Generated backend documentation
- `docs/backend/relationships_matrix.md` - Visual relationship maps

**New Rules:** RULE_18-24: Backend Documentation Sync

**Impact:** Projects with backend → Full backend docs auto-generated

**Breaking Change:** Backend rules renumbered from RULE_17-23 to RULE_18-24 (conflict with Design System RULE_17)

---

### Version 2.2.0 (2025-11-10) - Design System & UI/UX Integration

**Major Feature:** Complete design system documentation integration

✨ **Design System Generation**

- Automatic design documentation from raw data or existing code
- PHASE 5.5: Design System Generation in bootstrap
- Code analysis extracts design from CSS/SCSS/Tailwind configs
- Design tokens, components, patterns, accessibility docs
- Integration with module requirements (section 7: UI/UX)

📁 **New Structure:**

- `UPMT/bootstrap/00_DESIGN_RAW_DATA/` - Design materials collection
- `docs/design/` - Generated design system documentation
- `UPMT/structure-templates/_COMPONENT_TEMPLATE.md` - Component docs template

**New Rule:** RULE_17: Design System Sync

**Impact:** Projects with design data → Full design system auto-generated

---

### Version 2.1.0 (2025-11-10) - Structure Reorganization

**Major Change:** Complete structure reorganization for clarity

🏗️ **New Structure:**

- `UPMT/` - Template infrastructure (static)
- `docs/` - Project documentation (dynamic)
- `.context/` - Project context memory (dynamic)
- `.upmt/` - UPMT metadata (dynamic)

**Benefits:**

- Clear separation: template ↔ project files
- Easy cleanup after bootstrap (`echo "UPMT/" >> .gitignore`)
- No conflicts when updating template
- Better maintainability

**Breaking Changes:** Yes - full structure reorganization

---

### Version 2.0.0 (2025-11-10) - Completeness & Automation

**Major Release:** Guaranteed 100% completeness + automated rules

✨ **Key Features:**

- ✅ **PHASE 7.5: Completeness Validation** - Mandatory validation checklist
- 📜 **16 Automated Project Rules** - Auto-update documentation
- 📚 **Master References** - UPMT.md, FILE_INVENTORY.md
- 🔍 **100% Feature Extraction** - No features lost
- 🎯 **Rule Notifications** - 👀 Active, ✅ Executed

**New Files:**

- `UPMT/structure-templates/AI_INSTRUCTIONS/All_Project_rules.md` (~2,500 lines)
- `UPMT/structure-templates/AI_INSTRUCTIONS/UPMT.md` (~500 lines)
- `UPMT/structure-templates/AI_INSTRUCTIONS/FILE_INVENTORY.md` (~1,000 lines)
- `UPMT/bootstrap/BOOTSTRAP_CONFIG/SYSTEM_TESTING_GUIDE.md` (~800 lines)
- `UPMT/structure-templates/AI_INSTRUCTIONS/.cursorrules.template`

**Statistics:**

- Documentation: 7,000+ → 10,500+ lines (+50%)
- AI Instructions: 1,751 → 4,500+ lines (+157%)
- Validation Steps: 0 → 17 (NEW)
- Project Rules: 0 → 16 (NEW)

**Breaking Changes:** Yes - re-bootstrap recommended

---

### Version 1.0.1 (2025-11-09) - Auto-Fill Metadata

✨ **Auto-Fill Metadata System**

- No need to manually fill `metadata.yaml`
- Claude Code reads raw data and asks 5-10 questions
- Metadata fills automatically from data + your answers
- Saves 4-6 hours of manual work → 10-15 minutes

🔍 **Smart Tech Stack Recommendations**

- Analyzes technologies mentioned in raw data
- Compares with 2025 best practices
- Provides recommendations with reasoning

📊 **Existing Code Analysis**

- Support for adding docs to existing projects
- Detects implemented features from code

**Breaking Changes:** None (fully backward compatible)

---

### Version 1.0.0 (2025-11-09) - Initial Release

🎉 **Initial Release - Production Ready**

**Features:**

- Complete documentation template structure (7,000+ lines)
- 6 core documentation templates
- AI integration (Claude Code, Cursor)
- Bootstrap automation system
- Tech stack verification workflow
- Context preservation system
- Progress tracking templates
- Hybrid RU/EN language support

---

**Version History:**

| Version | Date | Key Changes |
|---------|------|-------------|
| 2.2.1 | 2025-11-11 | Backend Documentation System, Relationships Matrix |
| 2.2.0 | 2025-11-10 | Design System integration, PHASE 5.5 |
| 2.1.0 | 2025-11-10 | Structure reorganization (UPMT/, docs/, .context/) |
| 2.0.0 | 2025-11-10 | Completeness validation, 16 automated rules |
| 1.0.1 | 2025-11-09 | Auto-fill metadata, smart recommendations |
| 1.0.0 | 2025-11-09 | Initial template release |

---

**🌟 If this template helps you, consider starring the repository!**
