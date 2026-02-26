# 🧰 The Code Stacker Tools System

## What are Tools?

While "Skills" (`.codestacker/skills/`) tell an AI **HOW** to write code using a specific framework, "Tools" are the physical utilities the AI uses to **DO WORK** outside of its native conversational environment.

Code Stacker supports three tiers of Tools:

1.  **MCP (Model Context Protocol) Servers:** The most deeply integrated tools. The Director and Agents connect directly to these servers (e.g., Supabase MCP, GitHub MCP) to perform system-level actions safely.
2.  **REST APIs:** Standard endpoints (e.g., Stripe, Firecrawl) that the Agents can query directly from their Python/Node runtime environments using API keys.
3.  **Command-Line Interfaces (CLIs):** Raw executable binaries installed on the host machine (e.g., `psql`, `stripe-cli`, `docker`) that the Agents invoke via standard terminal shell commands.

---

## Tool Governance

Because Tools grant the AI significant power (such as modifying databases or pushing to production), their use is strictly bound by the active **Approval Gate**:

*   **Gate Full Auto:** Agents use tools autonomously based on the `TOOL_REGISTRY.md`.
*   **Gate Plan:** The Director explicitly lists which tools it plans to use for which steps. You must approve the list before execution.
*   **Gate Review (Default):** The Agent must pause and explicitly ask for your permission every single time before executing a CLI command or making a destructive API/MCP call.

---

## Keeping the Registry Updated

The `TOOL_REGISTRY.md` file tracks all official integrations. When you add a new API to your application or install a new MCP server to your local Claude/Cursor client, update the Registry so the Code Stacker Director knows the capability exists.
