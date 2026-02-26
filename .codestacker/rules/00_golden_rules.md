# 🥇 GOLDEN RULES (CORE - NEVER CHANGE)

## 1. THE PLAN LAW
- **Every** task requires a written plan with a checklist
- Plans saved to `.codestacker/project/plan/`
- **NO** implementation without explicit "Mode Approved"
- Plans can be master plans or task-specific sub-plans

## 2. THE NO-DRIFT COMMANDMENT
- Work ONLY what's in the approved plan
- NO feature creep
- NO "while I'm here" additions
- NO unsolicited improvements
- If you see something: Document in reports/ → Suggest for future plan

## 3. THE STRUCTURE FIRST DOCTRINE
- BEFORE planning: Read `.codestacker/project/structure/`
- BEFORE coding: Verify against existing patterns
- ALL code must match established standards
- Database queries MUST use latest schema

## 4. THE NO-GUESSING MANDATE
- If uncertain → STOP
- If missing info → ASK
- If contradictory → CLARIFY
- Never assume. Never hallucinate. Never invent.

## 5. THE DOCUMENTATION IMPERATIVE
- Every milestone → Record in `sessions/session_milestones.md`
- Every task completion → Update `summaries/`
- Every structure change → Update `structure/07_evolving_state.md`
- Every error/drift → Report in `reports/`

## 6. THE CONTEXT AWARENESS RULE
- Monitor Sprint/Phase changes
- When starting a new major Phase or Sprint → Write a `latest_summary.md`
- Instruct the user to start a new chat when crossing sprint boundaries
- Record milestones in `session_milestones.md`

## 7. THE SERVICE BOUNDARY
- NEVER start dev servers
- NEVER start databases
- NEVER run production commands
- ALWAYS get user to execute

## 8. THE ACCURACY REQUIREMENT
- All code must compile/run (conceptually)
- All paths must be correct
- All imports must exist
- All DB operations must match schema

## 9. THE TRANSPARENCY RULE
- Report what you're doing
- Report what you've done
- Report what you don't know
- Report when you're wrong

## 10. THE ASK FIRST PRINCIPLE
- When in doubt → ASK
- When stuck → ASK
- When unclear → ASK
- When done → CONFIRM
