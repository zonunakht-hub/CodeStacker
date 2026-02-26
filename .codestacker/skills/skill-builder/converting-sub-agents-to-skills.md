# Converting sub-agents to skills

Use this checklist to convert an existing sub-agent (or long system prompt) into a clean skill.

## Steps
1. Extract the core capability: one skill = one primary job.
2. Rename to a gerund-form skill name (e.g., `reviewing-code`, `triaging-incidents`).
3. Rewrite description to be invocation-focused:
   - triggers: what users actually say
   - scope: what the skill covers and does *not* cover
4. Move deep details out of SKILL.md into supporting files.
5. Remove model/color/tools settings (skills inherit the agent's capabilities).
6. Add examples: 2–4 realistic prompts that should trigger the skill.
7. Add guardrails:
   - safety constraints
   - verification steps
   - “ask before destructive actions”
8. Test: run 5 sample user prompts and verify it triggers when expected.

## Output format
- `SKILL.md` (overview + actionable steps)
- `references/` for deep docs
- `templates/` for scaffold outputs
- `scripts/` only if truly needed
