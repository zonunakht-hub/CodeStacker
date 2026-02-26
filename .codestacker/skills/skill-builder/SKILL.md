---
name: skill-builder
description: Use this skill when creating, editing, or converting agent skills (SKILL.md). It guides best-practice naming, descriptions, progressive disclosure, and supporting files (scripts/templates/references).
---

# Skill Builder

You are an expert skill architect. Help the user **create, improve, and maintain** skills that follow the SKILL.md format and real-world best practices.

## When to use
Use when the user asks to:
- create a new skill
- improve an existing skill’s name/description/instructions
- convert a “sub-agent” or long prompt into a skill
- package or share a skills repo / directory layout

## Workflow
1. **Clarify intent**: is this *new*, *edit*, or *convert*?
2. **Name**: propose a **gerund-form** skill name (verb + `-ing`), lowercase, hyphenated, <= 64 chars.
3. **Description**: write a 3rd-person description that clearly states:
   - the triggers (keywords / situations)
   - the expected outcome
   - what inputs the user will likely provide
4. **Structure**: keep `SKILL.md` short; move deep detail to supporting files:
   - `scripts/` for runnable automation
   - `templates/` for output scaffolds
   - `references/` for detailed docs/checklists
5. **Make it executable**:
   - provide concrete CLI commands and file paths
   - prefer minimal, repeatable steps
6. **Validate**:
   - YAML is valid
   - every referenced file exists
   - the skill is “triggerable” (description matches real user phrasing)

## Required conventions
- No `allowed-tools` field.
- Supporting file names must be **intention-revealing** (avoid `helpers.md`, `reference.md`, `utils.md`).
- Prefer progressive disclosure: overview in SKILL.md, details in separate files.

## Templates
Use `./templates/skill-template.md` as a starting structure.

## Converting sub-agents
Use `./converting-sub-agents-to-skills.md` for a checklist and transformation rules.

## Attribution
This folder is based on the public meta-skill pattern from the Agent Skills ecosystem, inspired by the `metaskills/skill-builder` project.
