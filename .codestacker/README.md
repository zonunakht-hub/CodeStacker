# 📚 Code Stacker: The Official Usage Guide

Welcome to the Code Stacker architecture. This directory (`.codestacker/`) is the persistent, structured brain of an AI-assisted development environment modeled after enterprise-grade software engineering teams.

By explicitly forcing language models to operate within physical directory structures, we effectively eliminate "prompt-drift" and hallucinations. This manual outlines how the system operates and how you (and the AI) should govern it.

---

## 🏗️ 1. The Core Hierarchy

Code Stacker functions on a rigid hierarchy. AI models start with zero context and incrementally load rules based on these progressive layers:

### The Global Brain (`brief.md` & `stack.md`)
These are the foundational rulebooks. The first thing an AI reads when spawned is `.codestacker/brief.md`. It contains the immutable Golden Rules, Escalation Procedures, and Global Protocols (such as demanding API keys leverage `.env` variables).

### The Working Memory (`workspaces/`)
Instead of a giant, unmanageable chat history, physical work happens inside **Workspaces**. 
*   **The `Core` Workspace:** (`workspaces/core/`) – All ad-hoc tasks, environment configurations (starting a dev server), and `Mode Free` activities resolve here by default. This centralizes daily overhead.
*   **Epic Workspaces:** (`workspaces/[epic_name]/`) – For massive features (e.g., building a complete Admin Dashboard), a dedicated Workspace is spawned to isolate the AI's context window.

---

## 🗂️ 2. The Federated Documentation System

How do isolated workspaces know about each other? We utilize a **Federated Master Index**.

1.  When an AI model needs to understand the overarching system architecture, it **always** begins at `.codestacker/project/structure/00_master_index.md`.
2.  `00_master_index.md` acts purely as a Table of Contents. It maps foundational items (like the Database Schema) alongside completed "Epics."
3.  When a Workspace finishes an undertaking (e.g., building out Stripe Billing), it compiles its isolated memory into a specific file inside `structure/epics/` (e.g., `stripe_billing_architecture.md`) and links it back to the Master Index.

> [!TIP]
> This structure is critical. It prevents two concurrent Workspaces from accidentally overwriting the global state logic while attempting a simultaneous "Master Synchronization."

---

## 🚀 3. Running a Workspace (The Execution Flow)

If you have a massive goal (e.g., "Build the Admin Authentication UI"), you will deploy a dedicated Workspace using the command `Mode Workspace`.

### 1) The Setup Interview
The AI transforms into **The Director**. Before writing a single line of code, The Director must interview you to formally define the environment:
*   **Goal:** The primary objective.
*   **Complexity Gate:** Should the AI ask permission for every change (`Gate Review`), every plan (`Gate Plan`), or run blindly until completion (`Gate Full Auto`)?
*   **Tool Setup:** Which APIs (Stripe, Firecrawl) or MCPs (Supabase, GitHub) should be attached to the memory context?

### 2) The Mission Plan
The Director breaks the task into logical sub-teams (e.g., `Frontend UI Team`, `Backend Auth Team`) and generates a strict checklist in `mission_plan.md`.

### 3) Execution & Telemetry
The Director spins up individual, specialized personas from `agents/AGENT_REGISTRY.md` (e.g., a `vibe-coder` or a `sql-architect`).
Throughout the build, the AI manages a visual `dashboard.md` within the Workspace directory, generating progress bars and Mermaid charts to keep human operators informed visually.

### 4) Master Synchronization
When the Epic tests green, the Director compiles the isolated environment memory, pushes the resulting architecture overview into `structure/epics/`, updates the `00_master_index.md`, and safely shuts the Workspace down.

---

## 🔐 4. Integrity Protocols

Enterprise applications require enterprise security. Code Stacker strictly enforces the following inside the AI prompt loop:

### The Credential Protocol
An AI model inside Code Stacker is instructed to **NEVER** write a plaintext API key or Database String inside `.codestacker/` or inside an application configuration file.
**Rule:** The absolute single source of truth for secrets is the primary framework `.env` file (`process.env.API_KEY`). 

### The Tool Registry (`tools/TOOL_REGISTRY.md`)
Code Stacker features an intelligent mapping layer for 3rd party tooling. The AI dynamically scans `tools/TOOL_REGISTRY.md` to identify what external abilities it has (such as using a Postgres CLI, scraping with Firecrawl, or interacting with a Model Context Protocol). 
You can update these parameters organically as the project expands.

## 📋 5. Common AI Commands

Use these inputs in chat to physically drive the internal state of the Code Stacker Application Framework:

| Command | Action |
| :--- | :--- |
| `Mode Free` | Executes quick tasks mapped directly into `Core` workspace memory. |
| `Mode Plan` | Stiffer validation. Forces the AI to write a checklist before coding. |
| `Mode Workspace` | Triggers a full-scale Epic deployment, requiring a setup interview. |
| `Mode Tool Index` | Forces the AI to re-scan `/tools` to understand new MCPs/APIs. |
| `Gate Review` | Halts the AI workspace loop after *every* action for manual code review. |
| `Gate Full Auto` | Gives the AI maximum autonomy allowing for self-healing error resolution. |
