# 🏢 Workspaces — Enterprise Execution Environments

## What Is a Workspace?

A Workspace is an enterprise-grade execution environment based on the Cosmo Orchestration Engine strategy. 

While small tasks might use `Mode Free` (ad-hoc coding) or `Mode Plan` (standard checklist), massive multi-stage epics (like "Build the Admin Section") require a dedicated Workspace. 

A Workspace provides **isolation** and **hierarchy**, meaning agents deployed into a Workspace only see the context and memory relevant to that specific epic. This prevents prompt-drift and hallucinations on massive projects.

## The Default `Core` Workspace

When Code Stacker initializes, it automatically creates a `Core` workspace at `.codestacker/workspaces/core/`. 
If you invoke `Mode Free` or `Mode Plan` without explicitly designating a massive Epic context, the Director AI defaults to routing the task into the `Core` workspace memory. This centralizes overall project overhead and manages basic development protocols (such as verifying if a dev server is already running before trying to start a new one).

---

## The Execution Hierarchy

When you trigger `Mode Workspace`, the AI stops acting as a single developer and assumes the role of **The Director**.


### The Workspace Setup Interview
Before spawning any agents or writing code, the Director **MUST** interview the User to configure the environment's governance and tool access:
1. **Goal**: What is the primary objective of this Workspace?
2. **Safety Level**: Which `Gate` should be enforced (Review, Plan, or Full Auto)?
3. **Tool Access**: Which MCP Servers, APIs, or existing DB CLI tools are required from `tools/TOOL_REGISTRY.md`?
4. **Compliance**: Are there specific GDPR or security considerations the `compliance-officer` should enforce?

Once answered, the Director creates the `mission_plan.md` and begins execution.

1. **User**: Provides the high-level goal and approves Gates.
2. **Director (Main AI)**: Analyzes the goal, breaks it into teams, and spawns Agents from `AGENT_REGISTRY.md`.
3. **Teams / Groups**: Logical divisions of labor (e.g., *Frontend Team*, *Auth Team*).
4. **Agents / Workers**: The spawned personas (e.g., `vibe-coder`, `full-stack-engineer`) who iterate on individual tasks.

---

## Folder Structure & The Visual Dashboard

When a Workspace is initialized, a strict directory structure is created under `.codestacker/workspaces/[workspace_name]/` to isolate its memory:

```
.codestacker/workspaces/admin_dashboard/
  ├── workspace_memory.md   # Overall state and context of this epic
  ├── mission_plan.md       # The Director's master plan (replaces active_plan.md)
  ├── dashboard.md          # 📊 High-level visual telemetry of the workspace
  ├── groups/
  │   ├── ui_team/
  │   │   └── manager_memory.md  # Status loops from the vibe-coders
  │   └── auth_team/
  │       └── manager_memory.md  # Status loops from the full-stack-engineers
  └── error_log.md          # Centralized error tracking for the workspace
```

### 📊 The Dashboard Protocol
Humans parse visual data faster than long text logs. Every Workspace **MUST** maintain a `dashboard.md` file. The Director is responsible for constantly updating this file with visual Markdown telemetry, including:
- **Progress Bars**: Representing task completion (e.g., `█████░░░░░ 50%`).
- **Team Status Tables**: Listing exactly which agent is doing what.
- **Metrics**: Current test coverage, open error counts, and recent completed PRs.
- **Charts**: Mermaid diagrams if necessary to track complex architectures.

---

## 🔒 Governance & Approval Gates

Because autonomous agents can cause significant churn in large codebases, Workspaces rely heavily on **Human-In-The-Loop (HITL)** Approval Gates. 

You control how autonomous the Workspace is by setting the Gate Level using chat commands:

| Command | Safety Level | Description |
|---|---|---|
| `Gate Review` | **High** *(Default)* | The strictest, enterprise-grade setting. The Manager must pause and ask for your review/approval after **every single task/pull-request** before moving to the next step. If an error occurs, the Director logs it to `error_log.md`, stops the entire workspace, and pings the user with the report. |
| `Gate Plan` | **Medium** | The Director pauses to ask for your approval on the initial `mission_plan.md` and the Agent Assignments. Once you approve, the agents auto-execute the rest of the plan autonomously. If an error occurs, the Director stops, writes to `error_log.md`, creates an "Error Fix Plan", and requests your approval on the fix plan before continuing. |
| `Gate Full Auto` | **Low** | Vibe-coding mode. The Director maps the plan, spawns the agents, and executes everything end-to-end without stopping for your permission. If an error occurs, the Director **Self-Heals**: it logs it to `error_log.md`, automatically researches the solution, fixes it, and proceeds without interrupting the user. |

---

## 🌍 Master Synchronization (The Federated Source of Truth)

Because Workspaces use isolated `workspace_memory.md` to prevent agent hallucination, there is a strict requirement to prevent the Workspace from branching away from the master codebase realities.

*   **The Law of Synchronization:** When the Director AI detects that a Workspace sub-team has completed a milestone or finished a `mission_plan.md`, the Director **MUST** bubble those results back up.
*   **Federated Documentation:** To prevent file-locking conflicts when multiple Workspaces run in parallel, the Director AI does **NOT** write to monolithic global architecture files.
*   **Target Updates:** The Director is responsible for:
    1.  Compiling the localized `workspace_memory.md` into an Epic-level master document inside `.codestacker/project/structure/epics/[workspace_name]_architecture.md`.
    2.  Adding a link to that new Epic document into the global routing hub: `.codestacker/project/structure/00_master_index.md`.
    3.  Updating the sprint milestone in `.codestacker/reports/latest_summary.md`.
    4.  Checking off the high-level goals in `active_plan.md`.

This Federated Index model ensures the Master Docs remain the single source of truth without Workspaces overwriting each other's concurrent progress.

---

## 🧪 Testing & Validation

Testing is intrinsically tied to Master Synchronization. A Workspace is considered "working" only if it passes tests.

1. **Pre-Sync Testing**: Before the Director synchronizes local `workspace_memory.md` up to the global docs, tests must be run.
2. **The QA Team**: When deploying a massive Workspace, the Director can assign an Agent (or a whole Team) exclusively to Quality Assurance (e.g., a `software-engineer` tasked purely with writing Jest/Playwright tests).
3. **Execution**: The agents are responsible for running the test commands. The Director records test coverage and results into `.codestacker/reports/test_results.md` for historical tracking.

## Addressing All Skill Levels

Code Stacker is designed to scale with you perfectly depending on the task at hand:

*   **Level 1: Quick Fixes (`Mode Free`)**
    *   No plans. No agents. Pure ad-hoc conversational coding. "Hey, fix this CSS bug."
*   **Level 2: Standard Features (`Mode Plan`)**
    *   One AI, one checklist. "Build a new contact page."
*   **Level 3: Parallel Logic (`Mode Plan Agents`)**
    *   One checklist, but the AI spawns multiple teammates to tackle the checklist simultaneously.
*   **Level 4: Enterprise Epics (`Mode Workspace`)**
    *   Segmented memory, Director hierarchies, multiple teams, and distinct HITL approval gates.
