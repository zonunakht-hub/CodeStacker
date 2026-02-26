# 🧰 Tools & Integrations Registry

*Index of all available External Tools, APIs, and CLI commands accessible to Code Stacker Agents.*

| Category | Tool Name | Description | Access Method |
|---|---|---|---|
| **Database** | Postgres CLI (`psql`) | Direct SQL interaction for complex schema queries. | Standard CLI (must be installed locally) |
| **Backend** | Supabase MCP | Schema generation, Edge Function deployment, Database Management. | System MCP Module |
| **Payments** | Stripe API | Secure processing of checkout sessions, webhooks, and subscriptions. | REST API (Key required in `.env`) |
| **Data Parsing** | Firecrawl API | Advanced web scraping and Markdown conversion for RAG pipelines. | REST API (Key required in `.env`) |
| **Search** | Tavily Search API | Optimized search query engine built specifically for LLM context retrieval. | REST API (Key required in `.env`) |
| **Version Control** | GitHub MCP | Repository management, issue tracking, review requests, and PR automation. | System MCP Module |
| **Messaging** | Resend API | Transactional email delivery (magic links, receipts). | REST API (Key required in `.env`) |

---

## Tool Usage Rules

1. **Discovery:** When entering a new Workspace, the Director AI must read this registry to understand its capabilities.
2. **Setup:** If an Agent needs to use a REST API (like Stripe or Firecrawl), they must verify the appropriate secret keys are loaded via the project's root `.env` file first.
3. **MCP Priority:** If a task can be accomplished using an active MCP Server rather than raw API calls or bash scripts, the MCP method should be prioritized for safety.
