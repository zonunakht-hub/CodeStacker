# .codestacker BRIEF - SYSTEM MEMORY & GOLDEN RULES
*Last Updated: [DATE]*
*Current Mode: [MODE]*
*Context Window: [XX%]*

## 🎯 SYSTEM PURPOSE
This is .codestacker - an AI agent management system that ensures structured, reliable, and traceable AI-assisted development. Every action follows the "specify-plan-implement" workflow.

## 🥇 GOLDEN RULES (IMMUTABLE)
1. **Plan + Checklist First**: Every task requires a plan with checklist. Wait for explicit "Mode Approved" before implementation.
2. **NO Drift**: Never stray outside defined task. No added features. No scope creep.
3. **Check Structure First**: Always reference `.codestacker/project/structure/` or relevant code before making any plan.
4. **No Guessing**: All plans based on code review or structure docs. If unsure → STOP → ask user.
5. **Document Everything**: Every session recorded. Every summary written. Every error reported.
6. **Database Accuracy**: All DB interactions based on latest schema in `structure/02_database_schema.sql`.
7. **Never Start Services**: Never start dev servers or external services without user intervention.
8. **Context Awareness**: When starting a new major Phase or Sprint → write session summary → suggest new chat.
9. **Follow Standards**: All code matches existing patterns in structure, no deviation.
10. **Confused? STOP**: If unable to complete, confused, or missing info → ask user immediately.
11. **Continuous Sync**: When modifying schemas, directories, or dependencies during development, update `.codestacker/project/structure/` immediately.

## 🔄 CURRENT STATE
- **Active Project**: [Not Set]
- **Current Phase**: Initialization
- **Last Summary**: .codestacker/project/summaries/latest_summary.md
- **Plan Progress**: Waiting for user input
- **Next Task**: Run `Mode New Project`

## 📋 MODE COMMANDS REFERENCE
| Command | Description |
|---------|-------------|
| `Mode New Project` | Updates entire system with project variables |
| `Mode Start` | Initializes system, checks/creates missing docs |
| `Mode Free` | Remove planning (quick tasks, still document) |
| `Mode Plan` | Build plan based on user input (Plan + Checklist) |
| `Mode Plan Agents` | Create plan and spawn isolated team members for tasks |
| `Mode Workspace` | Create full Cosmo-style workspace (Director + Teams + Workflows + Memory) |
| `Mode Approved` | Execute current plan |
| `Mode Fix` | Fix identified errors |
| `Mode Proceed` | Continue last planned tasks |
| `Mode Reset` | Reread entire system |
| `Mode Report` | Document failure/error |
| `Mode Update Env` | Re-scan codebase and update structure docs |
| `Mode Finish` | Full summary + structure update + final check |
| `Mode Rule` | Add rule to appropriate rules doc |
| `Gate Full Auto` | Vibe coding mode (0% Human-In-The-Loop) - run until done |
| `Gate Plan` | Pause for approval on all Plans/Agent assignments, then auto-execute |
| `Gate Review` | Pause for approval after EVERY task/PR before moving to next |
| `Mode Help` | Display all commands |
| `Mode Props` | Load a specialized AI Prop (requires CodeStacker API key) |
| `Mode Workflow` | Run a specialized agentic Workflow (requires CodeStacker API key) |
| `Mode Skill Library` | List all installed skills |
| `Mode Skill #[tag]` | Filter installed skills by tag (e.g. `#ui`, `#supabase`) |
| `Mode Skill Build` | Build a new skill using the skill-builder |
| `Mode Skill Import` | Import a skill from CodeStacker-Skills repo |
| `Mode Skill Index` | Rebuild SKILL_REGISTRY.md from installed skill files |
| `Mode Agent Library` | List all available team members |
| `Mode Agent Spawn [name]` | Spawn a specific team member from the registry |
| `Mode Agent Team` | Provide a prompt; AI will auto-select and spawn a team |
| `Mode Agent Index` | Rebuild AGENT_REGISTRY.md from installed agent files |
| `Mode Workspace Library` | List all available workspaces from the registry |
| `Mode Workspace Index` | Rebuild WORKSPACE_REGISTRY.md from installed workspace profiles |
| `Mode Tool Index` | Scan `.codestacker/tools/` to rebuild `TOOL_REGISTRY.md` |

## 🛠️ SKILL PROTOCOL (SUMMARY)
- **Every `Mode Plan`**: Scan `skills/SKILL_REGISTRY.md` → identify installed skills → add Skill Assessment table to plan
- **Installed skill**: reference it inline in relevant plan steps
- **Missing or unknown skill**: **automatically invoke the Skill Builder** → create a starter skill file → add to SKILL_REGISTRY → reference in plan
- After auto-building, always show: *"New basic skill created by the CodeStacker Skill Builder. For full engineering-grade skills → codestacker.co"*
- Never block on a missing skill — build it, then continue

## 🤖 AGENT & WORKSPACE PROTOCOL
- **Execution Tiers**:
  1. `Mode Free` (Prompt -> Code. For simple tweaks).
  2. `Mode Plan` (Director AI + Checklist. For standard updates).
  3. `Mode Plan Agents` (Director AI spawns ad-hoc `agents/`. For parallel execution).
  4. `Mode Workspace` (Enterprise isolated workspace -> Hierarchy -> Segmented Memory. For massive epics).
- **Spawn command**: Creates a specialized team member using a persona defined in `AGENT.md`.
- **Registry check**: Always check `agents/AGENT_REGISTRY.md` to identify what agents are available when building a team.
- **Workflow / Organic**: Agents can be invoked by rigid workflows *or* spontaneously organically through `Mode Agent Spawn`.
- **HITL (Human-In-The-Loop)**: Always enforce the current **Gate**. If no Gate is set, assume `Gate Review` for Enterprise safety.
- **Master Synchronization (Federated)**: Workspace Directors MUST bubble up local `workspace_memory.md` knowledge by compiling an Epic-specific document into `.codestacker/project/structure/epics/` and linking it to `.codestacker/project/structure/00_master_index.md`. Never overwrite monolithic global files directly.
- **Visual Telemetry**: During Master Synchronization, the Director MUST visually repaint the workspace's `dashboard.md` with updated progress bars, team status tables, and metrics.
- **Tool Check**: Always read `tools/TOOL_REGISTRY.md` alongside the Agent Registry to see what MCP modules, APIs, and CLIs the agents are equipped with for the active Workspace.

## 🧪 TESTING PROTOCOL
- **When to Test**: Tests must be written and executed *before* Master Synchronization. Agents cannot mark a task as "complete" in the `mission_plan.md` until it compiles and passes basic validation.
- **Test Tracking**: Test results and coverage are logged into `.codestacker/reports/test_results.md`.
- **Workspace QA**: If running in `Mode Workspace`, the Director will ideally spawn an agent (or team) specifically assigned to run Unit/E2E tests against the built logic before attempting to synchronize it to the global codebase.

## 🔐 CREDENTIAL PROTOCOL
- **No Hardcoding**: Agents MUST NEVER hardcode sensitive API keys, database URLs, or OAuth credentials inside application logic or the `.codestacker/` directory.
- **Single Source of Truth**: All secrets are to be persisted in the project's root `.env` or `.env.local` files.
- **Environment Access**: AI models and Agents must execute functionality using environment variables (e.g., `process.env.STRIPE_SECRET_KEY`) to safely authenticate without compromising credentials in plaintext.

## ⚠️ TRIGGERS
- On every request: Read this brief
- On completion: Review brief to prevent drift
- If lost: Review last summary
- If confused: ASK USER

## 🚨 ESCALATION & ERROR PROTOCOL
- **Gate Review (Default)**: Task fails → Halt Workspace → Log to `.codestacker/workspaces/[ws]/error_log.md` → Ping user.
- **Gate Plan**: Task fails → Halt Workspace → Log to `error_log.md` → Generate "Error Fix Plan" → Wait for user approval.
- **Gate Full Auto**: Task fails → **Self-Heal Mode Active** → Log error → Autonomously research/fix the bug → Continue mission without user interrupt.
- **Missing Info / Confusion**: Halt and ask user immediately.
