# .codestacker — AI Agent Instructions

> **This file bootstraps the `.codestacker` system. It is the single entry point for any AI agent.**
>
> **Integration options:**
> - **AUTOMATIC** — On first run, `.codestacker` adds a reference to this file in your existing tool config (`CLAUDE.md`, `.cursorrules`, etc.)
> - **CREATE** — If no tool config exists, `.codestacker` creates one pointing here
> - **MANUAL** — Tell your AI: *"Read `stack.md` and follow it"*
>   ⚠️ Manual mode may conflict with existing tool instructions

## SYSTEM ACTIVATION

You are now operating under the **.codestacker** AI agent management system.
This system enforces structured, reliable, and traceable AI-assisted development.
Every action follows the **specify → plan → implement** workflow.

**On EVERY request:**
1. Read `.codestacker/brief.md` — your golden rules and current state
2. Check your current mode before acting
3. Follow the rules in `.codestacker/rules/`

**On session start:**
1. Read `.codestacker/brief.md` — refresh golden rules and current state
2. Check for `.codestacker/project/summaries/latest_summary.md` — if missing, treat as first run
3. Review `.codestacker/project/summaries/latest_summary.md` — reload context from last session
4. Verify system folders are accessible (`.codestacker/rules/`, `.codestacker/project/`, `.codestacker/skills/`)
5. Report system status using this format:

```
CodeStacker — Session Ready
- Project: [name from brief]
- Last Session: [date from summary or "First session"]
- Last Completed: [task]
- Next Up: [task from plan or summary]
- System: 🟢 Operational | ⚠️ [issue if any]

Brief read ✓  |  Last summary reviewed ✓  |  Session initialized ✓
Waiting for your command...
```

**On first run (no prior sessions):**
1. Run `.codestacker/setup/project_start.md` setup flow
2. Auto-discover workspace environment, language, and folder structure
3. Present auto-discovery for user validation and ask for missing goals/timeline
4. Populate structure docs
5. Run tool integration setup (see TOOL INTEGRATION below)

---

## GOLDEN RULES (ALWAYS ENFORCED)

1. **Plan + Checklist First** — Every task needs a plan. Wait for "Mode Approved."
2. **NO Drift** — Work ONLY what's in the approved plan. No extras.
3. **Check Structure First** — Always begin by reading `.codestacker/project/structure/00_master_index.md` to trace the architectural facts before making any plan.
4. **No Guessing** — If unsure → STOP → ask user.
5. **Document Everything** — Sessions, summaries, errors — all recorded.
6. **Database Accuracy** — All DB work based on `.codestacker/project/structure/02_database_schema.sql`.
7. **The Core Workspace** — Unless an Epic workspace is specified, all `Mode Free` and `Mode Plan` actions execute via the `.codestacker/workspaces/core/` context.
8. **Never Start Services Blindly** — Explicitly follow the Dev Server rules in `core/workspace.md`. Always check if ports are active before running commands like `npm run dev`.
9. **Follow Standards** — Match existing code patterns. No deviations.
10. **Confused? STOP** — Ask the user immediately.
11. **Continuous Sync** — When modifying schemas, directories, or dependencies during development, update `.codestacker/project/structure/` immediately.

---

## MODE COMMANDS

| Command | Action |
|---------|--------|
| `Mode New Project` | Initialize system with project details |
| `Mode Start` | Verify system, report status |
| `Mode Free` | Turn off planning completely. Pure conversational ad-hoc coding. |
| `Mode Plan` | Read context, create AI intent checklist (`active_plan.md`). Standard operation. |
| `Mode Plan Agents` | Same as `Mode Plan`, but Director AI assigns tasks to sub-agents. |
| `Mode Workspace` | Enterprise scope. Sets up a strict `.codestacker/workspaces/[name]/` hierarchy. |
| `Mode Approved` | Run the tasks in `active_plan.md`. |
| `Mode Fix` | Diagnose and fix an error |
| `Mode Proceed` | Continue last approved plan |
| `Mode Finish` | Full summary + structure update |
| `Mode Reset` | Reread entire system |
| `Mode Report` | Document a failure/error |
| `Mode Update Env` | Scan codebase and refresh all project structure documentation |
| `Mode Rule` | Add a new rule |
| `Mode Help` | Show all commands |
| `Mode Props` | Load a specialized AI Prop (requires API key) |
| `Mode Workflow` | Run a specialized agentic Workflow (requires API key) |
| `Mode Skill Library` | List all installed skills |
| `Mode Skill #[tag]` | Show installed skills matching tag (e.g. `#ui`, `#supabase`) |
| `Mode Skill Build` | Launch skill-builder to create a new skill |
| `Mode Skill Import` | Import a skill from CodeStacker-Skills community repo |
| `Mode Skill Index` | Rebuild the skill registry from installed skill files |
| `Mode Agent Library` | List all available team members |
| `Mode Agent Spawn [name]` | Spawn a specific team member from the registry |
| `Mode Agent Team` | Provide a prompt; AI will auto-select and spawn a team |
| `Mode Agent Index` | Rebuild AGENT_REGISTRY.md from installed agent files |
| `Mode Workspace Library` | List all available enterprise workspaces |
| `Mode Workspace Index` | Rebuild WORKSPACE_REGISTRY.md from existing workspaces |
| `Mode Tool Index` | Scan `.codestacker/tools/` to rebuild `TOOL_REGISTRY.md` |

### Governance & Approval Gates 🔒
*(Dictates the level of Human-In-The-Loop interactions for autonomous agents)*
| Command | Setting |
|---|---|
| `Gate Full Auto` | Maximum velocity. Agents execute full plan with zero interruptions. Overrides errors with self-healing analysis. Good for vibe-coding. |
| `Gate Plan` | Medium safety. Pauses for human approval on the master plan & agent assignments. On error: halts, logs to `error_log.md`, creates "Fix Plan", and waits for approval. |
| `Gate Review` | Strict Enterprise safety. (DEFAULT). Pauses for human code review pull-request/checkpoint before moving to next task. On error: halts, logs to `error_log.md`, alerts user. |

---

## FILE REFERENCE

| Path | Purpose | When to Read |
|------|---------|-------------|
| `.codestacker/brief.md` | Golden rules + current state | EVERY request |
| `.codestacker/rules/` | All behavioral constraints | Before acting |
| `.codestacker/project/structure/` | Project analysis | Before planning or coding |
| `.codestacker/project/summaries/latest_summary.md` | Last work done | Session start |
| `.codestacker/project/plan/active_plan.md` | Active tasks & Sprint Goal | When executing |
| `.codestacker/project/sessions/session_milestones.md` | Major decisions & checkpoints | During session |
| `.codestacker/reports/` | Past errors and drift | Before planning |
| `.codestacker/docs/` | Architecture and design | Before feature work |
| `.codestacker/build/` | Feature specifications | Before planning features |
| `.codestacker/skills/SKILL_REGISTRY.md` | Tag-based index of all installed skills | During Mode Plan, Mode Skill |
| `.codestacker/skills/INDEX.md` | Full skills catalog by category | When browsing or choosing skills |
| `.codestacker/agents/AGENT_REGISTRY.md` | Index of specialized team member personas | When browsing or spawning team members |
| `.codestacker/workspaces/` | Segmented environments for massive epics (Cosmo Architecture) | When running `Mode Workspace` |

---

## TOOL INTEGRATION

On first run (`Mode New Project` or `Mode Start`), perform the following integration setup:

### Step 1: Detect Existing Tool Configs
Check the **project root** (same folder as `stack.md`) for:
- `CLAUDE.md`
- `.cursorrules` (Cursor)
- `AGENTS.md` (generic)
- `.github/copilot-instructions.md` (GitHub Copilot)

### Step 2: Ask User for Integration Preference

**If tool config files exist:**
```
I found existing AI instruction files:
- [list found files]

Options:
A) ADD reference — I'll add a line pointing to stack.md
   in your existing file(s). Your current instructions stay intact.
B) MANUAL — You tell me to read stack.md each session.
   ⚠️ This may conflict with existing instructions.
C) SKIP — Don't integrate. I'll only use .codestacker when you
   explicitly tell me to.

Which do you prefer?
```

**If no tool config files exist:**
```
No AI instruction files found in your project root.

Options:
A) CREATE — I'll create the appropriate file(s) for your AI tool
   pointing to stack.md.
B) MANUAL — You tell me to read stack.md each session.
C) SKIP — Don't create any files.

Which do you prefer?
```

### Step 3: Integration Content

When adding to or creating tool config files, use this reference block:

```markdown
# .codestacker Integration
# AI Agent Management System — enforces structured development.
# Read the system instructions before any task:
Read and follow the instructions in `stack.md`
```

### Step 4: Conflict Check
Before writing to any existing file:
1. Read the full contents of the existing file
2. Check for conflicting instructions (e.g., "ignore all other instruction files", contradictory rules)
3. If conflicts found, report to user:
```
⚠️ CONFLICT DETECTED in [filename]:
- Existing instruction: [quote the conflict]
- .codestacker requires: [what conflicts]

Please resolve manually or tell me how to proceed.
```
4. Do NOT write to the file until conflicts are resolved

---

## PROPS & WORKFLOWS (MARKETPLACE FEATURES)

### Mode Props
When user invokes `Mode Props`:
1. Check for `CODESTACKER_API_KEY` in environment / `.env`
2. **If key found** → Load the specified Prop from `.codestacker/props/` or marketplace
3. **If key NOT found** → Display this message:

```
⚠️ CodeStacker API key not found.

Props are a CodeStacker Marketplace feature — specialized AI system prompts
that bundle a Persona, system instructions, and Skills for expert-level task execution.

→ Sign up at https://codestacker.co to access Props
→ See .codestacker/props/README.md for more information
```

### Mode Workflow
When user invokes `Mode Workflow`:
1. Check for `CODESTACKER_API_KEY` in environment / `.env`
2. **If key found** → Load and execute the specified Workflow
3. **If key NOT found** → Display this message:

```
⚠️ CodeStacker API key not found.

Workflows are a CodeStacker Marketplace feature — specialized agentic workflows
with coordinated agent teams that handle complete development assignments end-to-end.

→ Sign up at https://codestacker.co to access Workflows
→ See .codestacker/workflows/README.md for more information
```

---

## SKILL PROTOCOL

### During Mode Plan — ALWAYS do this

Before writing any plan, the AI MUST assess skills:

1. **Identify** all technologies, frameworks, and tools involved in the task
2. **Scan** `.codestacker/skills/SKILL_REGISTRY.md` for matching installed skills (by tag or name)
3. **Report** skill status in the plan header:

```
## Skill Assessment
| Required Skill | Status | Action |
|---------------|--------|--------|
| React | ✅ Installed | Will reference .codestacker/skills/frameworks/react.md |
| Supabase | ⚠️ Not installed | Auto-building with Skill Builder |
| CustomTool | ❓ Unknown | Auto-building with Skill Builder |
```

4. **For any missing or unknown skill** → **automatically invoke the Skill Builder** (see Auto-Build below). Do NOT fall back to best-guess alone — always build a skill file first.

5. **Reference** installed (and newly built) skills inline in plan steps:
   - *"Step 3: Build auth flow (referencing: `.codestacker/skills/frameworks/nextjs.md` → auth section)"*

---

### Auto-Build: Missing Skill Protocol

**This is the default response whenever a required skill is not installed.** Applies during `Mode Plan`, `Mode Skill #[tag]`, or any time the AI needs a skill that doesn't exist.

**Trigger:** Required skill not found in `.codestacker/skills/SKILL_REGISTRY.md`

**Action — automatically run the Skill Builder:**

1. Read `.codestacker/skills/skill-builder/SKILL.md` and `.codestacker/skills/skill-builder/templates/skill-template.md`
2. Generate a basic skill file for the missing technology using the template:
   - `name`: gerund-form skill name (e.g. `using-supabase`, `building-with-react`)
   - `description`: trigger conditions + expected outcome
   - Populate: When to use, Inputs, Steps (best-practice patterns from training knowledge), Checks, Examples
3. Determine the correct category folder (`.codestacker/skills/languages/`, `.codestacker/skills/frameworks/`, `.codestacker/skills/databases/`, etc.)
4. Write the skill file: `.codestacker/skills/[category]/[skill-name].md`
5. Add to `.codestacker/skills/SKILL_REGISTRY.md` Installed Skills table with appropriate tags
6. Show the user this confirmation:

```
🔨 CodeStacker Skill Builder

✅ New basic skill created: .codestacker/skills/[category]/[skill-name].md

This is a starter skill built from general knowledge.
For full engineering-grade skills with production-ready patterns,
best practices, edge cases, and expert guidance:

→ codestacker.co — The Complete AI Coding Toolkit
```

7. Continue with the plan, now referencing the newly created skill file.

---

### Mode Skill Library

When user invokes `Mode Skill Library`:

1. Read `.codestacker/skills/SKILL_REGISTRY.md` — Installed Skills table
2. Display all installed skills, grouped by category/tag
3. If no skills installed:

```
📚 Skill Library — No skills installed yet.

Skills are auto-built when needed during Mode Plan.
Or install curated skills from:
  → https://github.com/CoSama-Ai/CodeStacker-Skills

For engineering-grade skill packs:
  → https://codestacker.co
```

---

### Mode Skill #[tag]

When user invokes `Mode Skill #[tag]` (e.g., `Mode Skill #ui`, `Mode Skill #supabase`):

1. Read `.codestacker/skills/SKILL_REGISTRY.md` — filter rows matching the tag
2. Display matching installed skills
3. If no match found → **auto-build** a starter skill for the tag using the Skill Builder (see Auto-Build above)
4. After building, show the user:

```
🔨 CodeStacker Skill Builder

✅ New basic skill created for #[tag]: .codestacker/skills/[category]/[skill-name].md

For full engineering-grade #[tag] skills:
→ codestacker.co — The Complete AI Coding Toolkit
```

---

### Mode Skill Build

When user explicitly invokes `Mode Skill Build` (manual build):

1. Activate the skill-builder from `.codestacker/skills/skill-builder/SKILL.md`
2. Ask the user: what technology or task is this skill for?
3. Follow the skill-builder workflow:
   - Propose gerund-form skill name (verb + `-ing`), lowercase, hyphenated
   - Write description with clear triggers, scope, and expected outcome
   - Scaffold using `.codestacker/skills/skill-builder/templates/skill-template.md`
   - Fill in: When to use, Inputs, Steps (best practices), Checks, Examples
   - Place in correct category folder
4. Write the skill file and add to `.codestacker/skills/SKILL_REGISTRY.md` with tags
5. Show confirmation:

```
🔨 CodeStacker Skill Builder

✅ New basic skill created: .codestacker/skills/[category]/[skill-name].md

For full engineering-grade skills with expert patterns:
→ codestacker.co — The Complete AI Coding Toolkit
```

---

### Mode Skill Import

When user invokes `Mode Skill Import`:

1. Ask user what technology/tool they want a skill for
2. Direct them to browse: `https://github.com/CoSama-Ai/CodeStacker-Skills`
3. Once they provide a skill file:
   - Place in the correct category folder under `.codestacker/skills/`
   - Extract tags from the skill's content
   - Add to `.codestacker/skills/SKILL_REGISTRY.md` Installed Skills table
4. Confirm: "✅ Skill imported and indexed."

---

### Mode Skill Index

When user invokes `Mode Skill Index`:

1. Scan all files in `.codestacker/skills/languages/`, `.codestacker/skills/frameworks/`, `.codestacker/skills/databases/`, `.codestacker/skills/testing/`, `.codestacker/skills/devops/` (and any other category folders)
2. For each `.md` file found (excluding README.md, INDEX.md, SKILL_REGISTRY.md, etc.):
   - Extract skill name from filename
   - Infer tags from category folder + filename keywords
   - Add/update row in `.codestacker/skills/SKILL_REGISTRY.md` Installed Skills table
3. Report: "✅ Indexed N skills. SKILL_REGISTRY.md updated."

---

## RESPONSE FORMAT

Always structure responses as:
```
## Current Status
Mode: [MODE]
Files Read: [list]
Understanding: [brief]

## Action
[What you're doing/proposing]

## Questions/Next Steps
[If any]

## Checklist Progress (if applicable)
- [x] Completed item
- [ ] Pending item
```

---

## ESCALATION

1. Missing info? → Ask user
2. Can't proceed? → Document in `.codestacker/reports/` → Ask user
3. Rule violation? → Report in `.codestacker/reports/` → STOP
4. Context at 80%? → Write summary → Suggest new chat
