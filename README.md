<div align="center">

# .codestacker 🏗️

![Version](https://img.shields.io/badge/version-1.0.0-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/status-early%20development-red?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)

**From vibe coding to full stack AI development.**

The AI agent management system that brings structure, memory, and precision to every project you build with AI.

<br/>

<img src="assets/terminal.svg" alt="CodeStacker terminal — Mode Plan, Skill Builder, Mode Approved in action" width="720"/>

<br/>

[Quick Start](#-quick-start) · [Commands](#-mode-commands-reference) · [Community Skills](https://github.com/CoSama-Ai/CodeStacker-Skills) · [Marketplace](https://codestacker.co) · [cosama.co](https://cosama.co)

---

Part of the **[CodeStacker Marketplace](https://codestacker.co)** — AI prompts, skills & agentic workflows for building with AI

Built by **[CoSama](https://cosama.co)** — AI Development Company

</div>

> ⚠️ **Early Development — v1.0.0**
> This is an early-stage release. The system is functional and ready to use, but expect active development, evolving documentation, and new features as the project grows. Contributions and feedback are welcome.

---

## 🌊 Vibe Coding vs Full Stack AI Coding

### Vibe Coding
Vibe coding is how most people use AI to build software today — and it's costing them.

You open a chat, describe what you want, and ask the AI to "just build it." The AI generates code. You paste it in. It kind of works. You ask for a fix. It breaks something else. You paste that fix in. Now something else is wrong. You're not building a product — you're playing whack-a-mole with an AI that has no idea what your actual codebase looks like, no memory of what it did last session, and no plan beyond the last prompt.

Vibe coding works for demos, prototypes, and throwaway scripts. For anything real — it creates technical debt faster than you can ship.

**The symptoms are familiar:**
- AI contradicts itself between sessions
- Generates code that doesn't match your existing patterns
- Adds features you didn't ask for
- Skips documentation and test coverage
- Drifts from the original spec halfway through
- Leaves you asking "what did it actually change?"

### Full Stack AI Coding
Full Stack AI Coding is the professional standard for building production software with AI. It treats your AI assistant as a disciplined engineering partner — not a magic text generator.

It means the AI knows your codebase before it touches it. It plans before it builds. It follows rules you've set. It documents everything it does. It stays on scope. It hands off cleanly between sessions. And when it makes a mistake, it records it so it doesn't make it again.

**Full Stack AI Coding is:**
- Specification-driven — every task starts with a written plan
- Structure-aware — AI reads your actual project before acting
- Traceable — every decision, change, and session is documented
- Rule-governed — behavioral constraints enforced on every request
- Context-managed — memory maintained across sessions and handoffs
- Skill-informed — domain expertise loaded for every technology in the stack

This is how you build real products with AI, at pace, without chaos.

---

## 🏗️ What is CodeStacker?

We built CodeStacker because the tools weren't keeping up with how developers actually work with AI.

As AI coding assistants became genuinely powerful, a new problem emerged: the AI itself became the bottleneck. Not because it wasn't capable — but because there was no system to manage it. Every session started from zero. Every decision was undocumented. Every mistake was repeated. Teams were spending more time corralling their AI tools than building their products.

We needed a layer between the developer and the AI. Something that enforced discipline, preserved context, and turned an unpredictable assistant into a reliable engineering partner. Something that lived in the project, worked with any AI tool, and required no external services to get started.

**That's `.codestacker`.**

`.codestacker` is a folder-based AI agent management system that sits inside your project and governs how your AI assistant behaves. It enforces a structured **specify → plan → implement** workflow. It keeps the AI on scope, on spec, and fully documented — from the first line of code to handoff.

One folder. Any AI. Total control.

---

## ✨ Features

- **📋 Plan-First Workflow** — Every task starts with a written plan and checklist. The AI cannot implement until you review and approve. No more "what did it just do?"

- **🚫 Zero Drift** — Strict scope enforcement. The AI works only what's in the approved plan. No added features, no scope creep, no surprise refactors.

- **🔍 Structure-Aware Planning** — Before every plan, the AI reads your actual project structure, schema, and architecture docs. Plans are based on what's real, not what it assumes.

- **🛠️ Skill System with Auto-Builder** — AI capabilities are loaded from skill files for every technology in your stack. Missing a skill? The built-in **CodeStacker Skill Builder** auto-generates one on the spot, then flags it for upgrade to an engineering-grade version from the marketplace.

- **🏷️ Tag-Based Skill Registry** — Skills are indexed by tag (`#react`, `#supabase`, `#docker`) for instant lookup. Query with `Mode Skill #[tag]` — the AI finds, loads, or builds the right skill automatically.

- **📝 Full Session Traceability** — Every session is recorded. Every decision documented. Every error logged. You always know what the AI did, when, and why.

- **🧠 Context Window Management** — The AI monitors its own context, writes a full summary at 80%, and signals when a clean handoff is needed. No lost context between sessions.

- **📊 Error Reporting & Learning** — When the AI makes a mistake, it documents it in `reports/`. Patterns are visible. Rules can be tightened. The same mistake doesn't happen twice.

- **🎮 Mode Command System** — Simple, memorable commands (`Mode Plan`, `Mode Approved`, `Mode Fix`, `Mode Finish`) control exactly what the AI is allowed to do at any moment.

- **🎭 Props — Specialized AI Personas** *(Marketplace)* — Load a Prop to instantly transform your AI into a role-specific expert: senior engineer, API architect, security auditor, and more. Each Prop bundles a Persona, system instructions, and a matched skills set.

- **⚙️ Agentic Workflows** *(Marketplace)* — Deploy coordinated agent teams for complex, assignment-oriented tasks. Spec Agent → Planner → Implementer → Tester → Documenter — fully managed, fully traced.

- **🔌 Tool Agnostic** — Works with Cursor, GitHub Copilot, GPT, Gemini, or any AI assistant that reads files. No lock-in.

- **🌐 Community Skills Library** — 2,800+ community-built skills available via [CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills), curated from the open-source AI development ecosystem.

---

## 🌐 CodeStacker Marketplace

**[codestacker.co](https://codestacker.co)**

The CodeStacker Marketplace is the home of engineering-grade AI development resources — built for developers who build with AI professionally.

Browse and install:
- **Skill Packs** — Expert-curated skill files for every major language, framework, database, and tool. Production-ready patterns, edge cases, and best practices — far beyond what the auto-builder generates.
- **Props** — Specialized AI system prompts that turn your assistant into a domain expert with the right persona, instructions, and skills pre-loaded.
- **Workflows** — Agentic workflow pipelines that deploy coordinated agent teams to handle complete development assignments from spec to delivery.

> The `.codestacker` base system is free and open source. The marketplace is where you go to level up.

---

## 🏢 About CoSama

**[cosama.co](https://cosama.co)**

CoSama is the AI development company behind CodeStacker. We build tools, systems, and infrastructure for developers who use AI as a core part of their engineering workflow — not as a shortcut, but as a first-class development partner.

CodeStacker is our answer to the question every serious AI developer eventually asks: *"How do I actually manage this thing?"*

We're building the tooling layer that makes Full Stack AI Coding the default — not the exception.

---

## ⚡ Quick Start

### 1. Add .codestacker to Your Project

**Option A — One-liner (Mac/Linux)**
```bash
curl -sSL https://raw.githubusercontent.com/CoSama-Ai/CodeStacker/main/install.sh | bash
```

---

**Option B — One-liner (Windows PowerShell)**
```powershell
iwr -useb https://raw.githubusercontent.com/CoSama-Ai/CodeStacker/main/install.ps1 | iex
```

---

**Option C — Git (Manual)**
```bash
git clone --depth 1 https://github.com/CoSama-Ai/CodeStacker.git /tmp/cs
cp /tmp/cs/stack.md .
cp -r /tmp/cs/.codestacker .
rm -rf /tmp/cs
```

---

**Option D — ZIP Download**

Download the ZIP from GitHub → **Code → Download ZIP**, extract it, then copy `stack.md` and the `.codestacker/` folder into your project root.

> ⚠️ Windows File Explorer won't show `.codestacker` by default (hidden folder) — use PowerShell or enable "Show hidden items".

### 2. Connect Your AI Tool

The core instruction file is **`stack.md`** — it tells any AI how to operate under `.codestacker`. You have three integration options:

**Option A — Automatic (Recommended)**
Run `Mode Start` or `Mode New Project`. The system detects your existing AI config files (`CLAUDE.md`, `.cursorrules`, `AGENTS.md`, `.github/copilot-instructions.md`, etc.) and asks to add a reference to `stack.md`. Your existing instructions stay intact.

**Option B — Create New**
If you have no AI config files yet, the system offers to create the appropriate one for your tool, pointing to `stack.md`.

**Option C — Manual**
Tell your AI: *"Read `stack.md` and follow it."*
> ⚠️ Manual mode may conflict with existing tool instructions.

### 3. Start Your First Session

Open a chat with your AI assistant. The system auto-detects first run:

```
You: (start chat)

AI: 🔍 Detected first run — initializing .codestacker...

    I found existing AI instruction files:
    - CLAUDE.md
    → Add .codestacker reference? (A) Add / (B) Manual / (C) Skip

    Please answer a few questions:
    1. What is your project name?
    2. What language/framework?
    3. Do you have existing code?
    4. What's the main goal?
```

### 4. Start Building

Once initialized, use mode commands to control the AI:

```
You: Mode Plan - Add user authentication

AI: 📋 Creating plan with checklist...
    [creates plan in .codestacker/project/plan/]

You: Mode Approved

AI: ✅ Executing plan...
    [implements with full documentation]
```

---

## 🎮 Mode Commands Reference

### Core Workflow

| Command | Description | When To Use |
|---------|-------------|-------------|
| `Mode New Project` | Initialize entire system with project details | First time setting up |
| `Mode Start` | Verify system, check docs, report status | Beginning of each session |
| `Mode Plan` | Create detailed plan + checklist | Before any new feature/task |
| `Mode Approved` | Execute current plan | After reviewing and approving a plan |
| `Mode Free` | Quick tasks — skip planning, still document | Minor tweaks, small fixes |
| `Mode Fix` | Create fix plan and implement | When bugs/errors are identified |
| `Mode Proceed` | Continue last approved plan | After interruption or context switch |
| `Mode Finish` | Full summary + structure update + final check | End of session or milestone |

### Skills

| Command | Description | When To Use |
|---------|-------------|-------------|
| `Mode Skill Library` | List all installed skills | See what's available in your skills folder |
| `Mode Skill #[tag]` | Filter skills by tag (`#ui`, `#supabase`, `#react`) | Find skills for a specific technology |
| `Mode Skill Build` | Build a new skill with the skill-builder | Create a custom skill file |
| `Mode Skill Import` | Import from CodeStacker-Skills community repo | Add pre-built community skills |
| `Mode Skill Index` | Rebuild the skill registry | After adding new skill files manually |

> 💡 Skills are **automatically assessed during `Mode Plan`** — the AI scans `skills/SKILL_REGISTRY.md`, builds any missing skills on the spot with the Skill Builder, and references them inline in the plan.

### Marketplace Features

| Command | Description | When To Use |
|---------|-------------|-------------|
| `Mode Props` | Load a specialized AI Prop (requires API key) | When you need expert-level AI persona + skills |
| `Mode Workflow` | Run a specialized agentic Workflow (requires API key) | When you need a full agent team for an assignment |

> 🔑 Props and Workflows require a **CodeStacker API key**. [Get access at codestacker.co →](https://codestacker.co)

### System Management

| Command | Description | When To Use |
|---------|-------------|-------------|
| `Mode Reset` | AI rereads entire system | If AI seems confused or off-track |
| `Mode Report` | Document why AI failed | After any mistake |
| `Mode Rule` | Add new rule to rules doc | Establishing new project standards |
| `Mode Help` | Display all commands | Any time you need a reminder |

---

## 📁 Folder Structure

```
your-project/                   # ← your project root
│
├── stack.md                    # 🚀 AI ENTRY POINT — the only CodeStacker file in your root
│
└── .codestacker/               # 📦 Entire system lives here — clean, contained, hidden
    ├── brief.md                # 🎯 Core memory + golden rules (read on EVERY request)
    ├── .codestacker_init       # Marker file — detects first run
    │
    ├── setup/                  # 🔧 One-time setup (internal — auto-invoked on first run)
    │   └── project_start.md
    │
    ├── rules/                  # 🤖 What AI can/cannot do
    │   ├── 00_golden_rules.md
    │   ├── 01_behavioral_rules.md
    │   ├── 02_code_standards.md
    │   ├── 03_communication_rules.md
    │   └── 04_security_rules.md
    │
    ├── docs/                   # 📚 Your architecture & design notes
    │   ├── 01_architecture.md
    │   ├── 02_ui_design.md
    │   ├── 03_api_design.md
    │   └── 04_data_models.md
    │
    ├── build/                  # 🏗️ What to build (specs)
    │   ├── 01_project_overview.md
    │   ├── 02_phase_1_spec.md
    │   └── backlog/
    │
    ├── props/                  # 🎭 AI Props (Marketplace — requires API key)
    │   └── README.md
    │
    ├── workflows/              # ⚙️ Agentic Workflows (Marketplace — requires API key)
    │   └── README.md
    │
    ├── skills/                 # 🛠️ AI capabilities registry
    │   ├── SKILL_REGISTRY.md   # 🏷️ Tag-based index (AI reads during Mode Plan)
    │   ├── INDEX.md            # Full skills catalog by category
    │   ├── community.md        # Install guide → CodeStacker-Skills repo
    │   ├── skill-builder/      # 🔨 Auto-builds missing skills
    │   │   ├── SKILL.md
    │   │   └── templates/skill-template.md
    │   ├── languages/          # JS, TS, Python, Go, Rust, PHP, Ruby
    │   ├── frameworks/         # Next.js, Express, Django, FastAPI, Laravel
    │   ├── databases/          # PostgreSQL, MongoDB, Supabase, Prisma, Redis
    │   ├── testing/            # Jest, Playwright, Pytest, Vitest, Cypress
    │   └── devops/             # Docker, GitHub Actions, Vercel, Nginx
    │
    ├── reports/                # 📊 Failure analysis & corrections
    │   ├── 01_error_log.md
    │   ├── 02_drift_reports.md
    │   ├── 03_misinterpretations.md
    │   └── 04_system_violations.md
    │
    └── project/                # 📁 All project tracking lives here
        ├── plan/               # 📋 Plans + checklists
        │   ├── 01_master_plan.md
        │   ├── 02_current_sprint.md
        │   ├── 03_checklists/
        │   └── 04_completed/
        ├── sessions/           # 📝 Every conversation recorded
        │   ├── session_log.md
        │   └── archive/
        ├── summaries/          # 📄 Work summaries + handoffs
        │   ├── latest_summary.md
        │   ├── handoff_notes.md
        │   └── archive/
        └── structure/          # 🔍 Complete project analysis
            ├── 01_project_overview.md
            ├── 02_database_schema.sql
            ├── 03_environment.md
            ├── 04_file_structure.md
            ├── 05_dependencies.md
            ├── 06_credentials.md
            └── 07_evolving_state.md
```

> Every folder includes a `README.md` explaining what goes there and how to use it.

---

## 🌐 Community Skills

Pre-built skill files for common languages, frameworks, databases, and testing tools — curated from many contributors across the AI development ecosystem.

### **[CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills)**

Skills are gathered, reviewed, and adapted from open-source communities including [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) (2,800+ community-built AI skills), direct contributor PRs, and the [CoSama](https://cosama.co) team. All skills are reviewed for quality and compatibility before inclusion.

| Skill Category | Examples |
|---------------|----------|
| Language Skills | JavaScript, TypeScript, Python, Go, Rust |
| Framework Skills | Next.js, Express, Django, FastAPI |
| Database Skills | PostgreSQL, MongoDB, Supabase, Prisma |
| Testing Skills | Jest, Pytest, Playwright, Vitest |

### Install Options

| Method | Use Case | Command |
|--------|----------|---------|
| **Full Install** | Want everything | Clone repo → copy all folders into `skills/` |
| **By Category** | Only need frameworks + databases | Clone repo → copy specific folders |
| **Individual** | Just need one skill | `curl` a single file from GitHub raw |
| **AI-Assisted** | Let the AI handle it | `Mode Free - Install the Next.js skill from CodeStacker-Skills` |

```bash
# Full install example
git clone https://github.com/CoSama-Ai/CodeStacker-Skills.git /tmp/cs-skills
cp -r /tmp/cs-skills/language_skills/* .codestacker/skills/languages/
cp -r /tmp/cs-skills/framework_skills/* .codestacker/skills/frameworks/
cp -r /tmp/cs-skills/database_skills/* .codestacker/skills/databases/
cp -r /tmp/cs-skills/testing_skills/* .codestacker/skills/testing/
cp -r /tmp/cs-skills/devops_skills/* .codestacker/skills/devops/
rm -rf /tmp/cs-skills
```

```bash
# Single skill example
curl -o .codestacker/skills/frameworks/nextjs.md \
  https://raw.githubusercontent.com/CoSama-Ai/CodeStacker-Skills/main/framework_skills/nextjs.md
```

See `skills/community.md` for full installation guide.

> 💡 **Can't find a skill for your stack?** The [CodeStacker Complete AI Coding Toolkit](https://codestacker.co) includes curated skill packs for every major language, framework, and tool.

---

## 🎭 Props & ⚙️ Workflows — Marketplace Features

Take `.codestacker` further with **Props** and **Workflows** — premium features available through the [CodeStacker Marketplace](https://codestacker.co).

### 🎭 Props — Specialized AI System Prompts

Props instantly transform your AI assistant into a highly capable, role-specific expert by bundling a **Persona + System Instructions + Skills** into a single ready-to-use file.

```
Mode Props - senior-fullstack-engineer

AI: 🎭 Loading Prop: senior-fullstack-engineer
    ✅ Persona active — Expert full-stack engineer
    ✅ Instructions loaded — Architecture-first approach
    ✅ Skills bundled — React, Node, PostgreSQL
    Ready to build.
```

### ⚙️ Workflows — Agentic Task Pipelines

Workflows deploy coordinated agent teams that handle complete, assignment-oriented development tasks end-to-end — from spec to implementation to testing to docs.

```
Mode Workflow - feature-development - Add user authentication

Workflow: ⚙️ Deploying Feature Development Workflow...
    Stage 1: Spec Agent → Stage 2: Planner → Stage 3: Implementer
    → Stage 4: Tester → Stage 5: Documenter
    ✅ Complete. Summary in project/summaries/.
```

### Getting Access

Both features require a **CodeStacker API key**.

> 🔑 **[Sign up at codestacker.co →](https://codestacker.co)**

See `props/README.md` and `workflows/README.md` for full details.

---

## 💡 Workflow Examples

### Adding a New Feature

```
You: Mode Plan - Add user profile page with avatar upload

AI: 📋 Reading project structure...
    🔍 Checking existing patterns...

    Plan ready:
    - Create Profile component
    - Add avatar upload handler
    - Update database schema
    - Add tests

    Approve with "Mode Approved" to proceed.

You: Mode Approved

AI: ✅ Executing plan...
    [implements each checklist item]
    [updates structure doc]
    [records session]
```

### Quick UI Tweak

```
You: Mode Free - Change button color from blue to green

AI: ⚡ Free mode active — skipping planning, still documenting

    [Makes change]
    [Updates session log]

    Done. Return to planned work with "Mode Proceed".
```

### Fixing a Bug

```
You: Mode Fix - Login form throwing 500 error

AI: 🔧 Fix mode activated
    [Creates fix plan]

    Found: Missing DATABASE_URL env var
    Fix plan: Add var → Update connection settings

    Approve fix?

You: Mode Approved

AI: [Implements fix]
    [Documents in reports/ why error occurred]
```

### End of Session

```
You: Mode Finish

AI: 📊 Generating final summary...
    - Completed: User profile page
    - Files modified: 5
    - Structure updated: Yes

    Handoff document created. Use "Mode Start" next session.
```

---

## ✅ Best Practices

**DO:**
- ✅ Start every session with `Mode Start`
- ✅ Always review plans before approving
- ✅ Use `Mode Free` sparingly — only tiny tweaks
- ✅ Run `Mode Finish` at natural stopping points
- ✅ Keep `docs/` updated with architecture decisions

**DON'T:**
- ❌ Never approve a plan without reading it
- ❌ Don't let AI implement without a plan (except `Mode Free`)
- ❌ Never ignore structure docs
- ❌ Don't let context grow too large — start fresh sessions

### Context Window Management

The AI monitors context and alerts you at 80%:

```
⚠️ Context at 82% — recommend new chat
   Summary written to summaries/
   Start fresh with "Mode Start" to continue
```

---

## 🔧 Troubleshooting

**AI seems confused or off-track:**
```
You: Mode Reset

AI: 🔄 Resetting... rereading entire .codestacker system
    ✅ System reloaded
```

**Missing documentation:**
```
AI: ⚠️ Missing: project/structure/02_database_schema.sql
    Please provide your database type and existing tables.
```

**AI made a mistake:**
```
You: Mode Report

AI: 📝 Documenting failure...
    Report saved to reports/
    Ready to proceed with fix.
```

---

## ❓ FAQ

**Q: Do I need to use all the folders?**
A: Yes — each folder serves a critical purpose. The system works as a whole.

**Q: Can I use this with any AI assistant?**
A: Yes. `.codestacker` works with any AI that can read/write files — GPT, Gemini, Cursor, Copilot, and more.

**Q: What if I'm starting a brand new project?**
A: Use `Mode New Project` first. The AI will guide setup.

**Q: How do I hand off to another developer?**
A: Run `Mode Finish` — it generates a complete handoff doc in `summaries/handoff_notes.md`.

**Q: Can I customize the rules?**
A: Yes — use `Mode Rule` to add project-specific rules, saved in `rules/`.

**Q: What if the AI isn't following the system?**
A: Try `Mode Reset`. If that doesn't work, check `reports/` for drift patterns and tighten rules with `Mode Rule`.

**Q: What if I need a skill that isn't installed?**
A: The AI auto-builds a starter skill on the spot using the Skill Builder. For engineering-grade skills, browse [codestacker.co](https://codestacker.co) or the [CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills) community repo.

---

## 🚀 Pro Tips

- **Start every day with `Mode Start`** — refreshes AI context
- **Review `reports/` weekly** — spot recurring AI mistake patterns
- **Keep `structure/` accurate** — better structure = better AI performance
- **Finish clean** — always end with `Mode Finish` for clean handoffs
- **Browse [CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills)** — don't reinvent skill files others have built

---

## 🤝 Contributing

Contributions are welcome!

- 🐛 **Report bugs** — [open an issue](https://github.com/CoSama-Ai/CodeStacker/issues)
- 💡 **Suggest features** — [start a discussion](https://github.com/CoSama-Ai/CodeStacker/issues)
- 📝 **Improve docs** — fix typos, add examples
- 🔧 **Submit PRs** — follow existing conventions
- 🛠️ **Share skills** — contribute to [CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills)
- 🛒 **Publish on the marketplace** — share prompts, skills & workflows at [codestacker.co](https://codestacker.co)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## ⚖️ Disclaimer

CodeStacker provides structure and context to AI models — it does not control them. **You are responsible for reviewing all skills, prompts, Props, and Workflows before use.** CoSama accepts no liability for AI model behavior or outcomes resulting from use of this software or any associated content, free or paid.

→ [Read the full disclaimer](.codestacker/DISCLAIMER.md)

---

<div align="center">

**Stop vibe coding. Start CodeStacking. 🏗️**

[CodeStacker](https://codestacker.co) · [CoSama](https://cosama.co) · [GitHub](https://github.com/CoSama-Ai/CodeStacker) · [Community Skills](https://github.com/CoSama-Ai/CodeStacker-Skills) · [Report Bug](https://github.com/CoSama-Ai/CodeStacker/issues) · [Request Feature](https://github.com/CoSama-Ai/CodeStacker/issues)

---

🚦 **Status:** 🟡 v1.0.0 — Early development, actively evolving
🔮 **Roadmap:** IDE plugins · Skill auto-install · Analytics dashboard · More Props & Workflows

Part of the **[CodeStacker](https://codestacker.co)** marketplace — AI prompts, skills & agentic workflows

Created by **[CoSama](https://cosama.co)** — AI Development Company

</div>
