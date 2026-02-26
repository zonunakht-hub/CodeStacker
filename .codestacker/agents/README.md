# 🤖 Agents — Team Member Registry

## What Are Agents?

Agents are specialized personas that run as **Code Stacker team members**. They break out large tasks into specialized roles, allowing the Lead Director AI to orchestrate parallel tasks, enforce code reviews, and guarantee separation of concerns.

Just like Skills teach the AI *how* to use a specific technology, Agents dictate *who* the AI is acting as when performing a task.

---

## The Agents Registry

All agents are indexed in `AGENT_REGISTRY.md`. 
The primary AI (Director) will automatically consult this file whenever you request team member assistance.

### Included Standard Personas
| Agent | Role / Persona |
|-------|----------------|
| **`project-manager`** | Breaks down tasks into checklists (`active_plan.md`), acts as the plan approval gate. |
| **`vibe-coder`** | Specializes entirely in UI/UX, styling, and glassmorphism components with no concern for backend logic. |
| **`software-engineer`** | General implementation powerhouse focused on executing business logic and tests. |
| **`full-stack-engineer`**| End-to-end implementer spanning the database schema down to the UI. |
| **`agent-builder`** | Meta-agent used to template and create new teammate personas. |

---

## 🛠️ How Agents Use Skills

Agents and Skills are designed to work together recursively. While an Agent dictates the persona, the Skills dictate the technical instructions.

1. **Auto-Discovery**: When the Director spawns an Agent (like the `full-stack-engineer`), the Director will cross-reference the required task against the `skills/SKILL_REGISTRY.md`.
2. **Context Passing**: If the Director knows the `full-stack-engineer` needs to write Supabase RLS policies, it will automatically extract the relevant `#supabase` skill instructions and pass them directly into the newly spawned Agent's context.
3. **Agent Autonomy**: Once spawned, a running Agent has the ability to pause and call `Mode Skill #[tag]` on its own to look up additional coding standards if it encounters a technology it isn't familiar with during the task.

---

## 📋 Mode Commands

You can invoke team members using specific commands in the chat. **You do not strictly need a defined workflow file to use agents.** They are ad-hoc tools that can be summoned organically during a conversation.

| Command | Action |
|---|---|
| `Mode Agent Library` | Lists all available team members from `AGENT_REGISTRY.md` so you can review options. |
| `Mode Agent Spawn [name]` | Spawns a specific team member from the registry. Example: `Mode Agent Spawn vibe-coder`. |
| `Mode Agent Team` | Provide a description of what you need; the Director AI will automatically select the best mix of agents from the registry and spawn the team for you. |
| `Mode Agent Index` | Rebuilds the registry if you hand-code a new `AGENT.md` file. |

---

## 🎯 Example Use Cases

### 1. The Single Agent Manual Spawn (Ad-Hoc)
*You are working on some backend code and realize you need a UI component mocked up quickly, but you don't want to lose your current context.*
**You type:**
> *"Mode Agent Spawn vibe-coder to build a polished, modern login interface component."*
**Result:** The Director AI spawns a `vibe-coder` in a sub-process, letting it focus entirely on the CSS and UI styling without touching your database logic.

### 2. The Auto-Selected Team Spawn
*You need a complex feature built end-to-end, but you want to enforce strict planning first.*
**You type:**
> *"Mode Agent Team. I need to build a shopping cart. Break down the checklist, then execute it. Require plan approval."*
**Result:** The Director AI checks the registry, automatically summons the `project-manager` and `full-stack-engineer`. The Manager writes the plan and asks you for approval. Once you approve, it assigns the tasks to the Full Stack Engineer to execute.

### 3. Creating a Custom Persona
*You realize you need a dedicated Security Auditor to review code before commits.*
**You type:**
> *"Mode Agent Spawn agent-builder. Build me a security-auditor team member focused entirely on catching OWASP vulnerabilities and checking RLS policies."*
**Result:** The `agent-builder` generates the new `.codestacker/agents/security-auditor/AGENT.md` file, and automatically runs the indexer script to add it to the registry for immediate use.
