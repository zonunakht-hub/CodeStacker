# 🛠️ Skills — AI Capabilities Registry

## What Are Skills?

Skills are markdown files that teach the AI how to work with specific technologies. Each skill file contains:

- **Common patterns** — how to structure code for this technology
- **Best practices** — what to do and why
- **Common pitfalls** — what to avoid and how
- **Project conventions** — patterns the AI must match in your codebase

The AI references installed skills during `Mode Plan` to ensure correct patterns for your stack.

---

## Folder Structure

| Folder | Category | What Goes Here |
|--------|----------|----------------|
| `languages/` | Programming Languages | JS, TS, Python, Go, Rust, PHP, Ruby |
| `frameworks/` | Web & API Frameworks | Next.js, Express, Django, FastAPI, Laravel |
| `databases/` | Databases & ORMs | PostgreSQL, MongoDB, Supabase, Prisma, Redis |
| `testing/` | Testing Tools | Jest, Playwright, Pytest, Vitest, Cypress |
| `devops/` | Infrastructure & CI/CD | Docker, GitHub Actions, Vercel, Nginx |

---

## Getting Skills

Skills are available from the community repo — install all, by category, or individually:

**[CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills)**

See `community.md` for full installation instructions.

---

## Key Files

| File | Purpose |
|------|---------|
| `INDEX.md` | Full index of all available skills by category and use case |
| `community.md` | Community repo info and installation guide |
| `CONTRIBUTORS.md` | Credits and attribution for skill sources |

---

## After Installing a Skill

1. Place the skill file in the correct category folder
2. Run `Mode Skill Index` — the AI will rebuild `SKILL_REGISTRY.md` automatically
3. The AI references it during the next `Mode Plan`

## Contributing

See `CONTRIBUTORS.md` for how to submit skills to the community repo.

---

## 🔨 Missing Skills Are Auto-Built

You don't need to find a skill before you start. When the AI needs a skill that isn't installed — during `Mode Plan` or `Mode Skill #[tag]` — it **automatically runs the CodeStacker Skill Builder** to generate a starter skill file on the spot.

After building, you'll see:

```
🔨 CodeStacker Skill Builder

✅ New basic skill created: skills/[category]/[skill-name].md

This is a starter skill built from general knowledge.
For full engineering-grade skills with production-ready patterns,
best practices, edge cases, and expert guidance:

→ codestacker.co — The Complete AI Coding Toolkit
```

The auto-built skill is a solid working foundation. For production-ready, expert-curated skills — upgrade at **[codestacker.co](https://codestacker.co)**.
