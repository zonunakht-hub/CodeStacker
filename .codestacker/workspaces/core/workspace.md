---
name: CodeStacker Core System
description: "The default root workspace for environment management, standard ad-hoc processing, and dev server orchestration."
tags: "#core #environment #dev-server #infrastructure"
---

# 🧠 CodeStacker Core Workspace

## Purpose
This is the **Baseline Execution Environment**. If an Agent is spawned out of `Mode Free` or `Mode Plan` without a dedicated epic workspace, they default to using the context, memory, and rules defined in this `Core` workspace. 

This centralizes overhead and gives ad-hoc tasks a strict memory lineage rather than executing blindly.

## 🚦 Strict Environment Rules: The Dev Server Protocol

AI models are notoriously bad at managing local servers (e.g., trying to run `npm run dev` multiple times, causing port-in-use crashes). The Core Workspace mandates the following checks:

### Rule 1: Port Discovery (NEVER start blindly)
*   **Before** starting a web framework (Vite, Next.js, Express), the Agent **MUST** check if the port is already active.
    *   *Windows command:* `netstat -ano | findstr :3000` (or `5173`)
    *   *Mac/Linux command:* `lsof -i :3000`
*   If the port is active, **assume the server is running** and proceed with the task. DO NOT attempt to run a new dev server instance.

### Rule 2: Graceful Restarts
Instead of force-killing servers recklessly, if a restart is strictly required (e.g., you edited `next.config.js` or `.env`):
1. Kill the specific PID occupying the port.
2. Wait 3 seconds.
3. Start the server using a background terminal (`npx run dev &` or equivalent).

### Rule 3: Framework Scaffolding Standards
When asked to scaffold new applications into the project hierarchy, use these `Core` baseline standards:
*   **React + Vite:** Prefer modern React 18+ with SWC (`npm create vite@latest . -- --template react-ts`). 
*   **React + Next.js:** Use the App Router explicitly (`npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"`).

## Workspace Dashboard
As the global hub, this workspace uses `dashboard.md` to log overall session infrastructure changes.
