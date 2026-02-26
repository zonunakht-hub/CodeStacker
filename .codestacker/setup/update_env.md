# 🔄 UPDATE ENV - Resync CodeStacker Memory
*Use this protocol when invoking `Mode Update Env`*

## Intent
The `Mode Update Env` command is used to re-evaluate the local environment, codebase, file structure, and database schemas dynamically, ensuring that the AI has the most accurate mental model of the project as it scales and evolves.

## Execution Steps

### 1. Database Schema Sync
1. Scan the codebase for schema updates, specifically looking for `.sql` files (`supabase-schema.sql`, migrations, etc.).
2. Merge or replace the contents of `.codestacker/project/structure/02_database_schema.sql` to accurately reflect the active tables, columns, constraints, and RLS policies.

### 2. File Structure Map
1. Traverse the primary code directories (e.g., `app`, `src`, `components`, `lib`, `api`, `actions`).
2. Write a high-level visual tree map (omitting low-level clutter) representing the architectural layout into `.codestacker/project/structure/04_file_structure.md`.
3. Explicitly document where different concerns live (e.g. "auth is located in `/app/auth`", "database logic is in `/lib/supabase`").

### 3. Dependency Map
1. Read the `package.json`, `requirements.txt`, or equivalent package manager configuration.
2. Identify core frameworks, libraries, APIs, and tooling (ignoring unessential dependencies).
3. Update `.codestacker/project/structure/05_dependencies.md` outlining the current tech stack versions.

### 4. Report Findings
After updating these documents, output to the user:
```markdown
✅ **CodeStacker Environment Updated**
- 02_database_schema.sql (Synced)
- 04_file_structure.md (Synced)
- 05_dependencies.md (Synced)

The AI's context model is now up to date with the current codebase.
```
