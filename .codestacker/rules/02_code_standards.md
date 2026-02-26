# 💻 CODE STANDARDS RULES

## Pattern Matching
- ALL new code must match existing patterns in project
- If no pattern exists → Document in plan → Get approval
- Never introduce new patterns without approval

## Language Consistency
- Use the language/framework from structure/
- Match existing style (tabs/spaces, brackets, naming)
- Follow project's established conventions

## Database Rules
- ALL queries must reference `structure/02_database_schema.sql`
- Use parameterized queries (no injection risks)
- Match existing ORM patterns
- Never hardcode credentials

## File Organization
- Place files according to `structure/04_file_structure.md`
- Follow existing naming conventions
- Maintain existing folder structure
- Update structure doc after adding files

## Error Handling
- Match project's error handling patterns
- Add appropriate logging
- Never swallow errors
- Report errors to user appropriately

## Testing
- If project has tests → Update or create tests
- Follow existing test patterns
- Ensure code is testable
- Document test gaps in plan
