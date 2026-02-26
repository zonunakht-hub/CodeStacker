# 🚀 PROJECT START - System Evaluation & Setup

## First Run Detection
*Running initial system setup...*

## Step 1: System Verification
Checking for required folders and files:
- [ ] .codestacker/brief.md
- [ ] .codestacker/rules/
- [ ] .codestacker/docs/
- [ ] .codestacker/build/
- [ ] .codestacker/skills/
- [ ] .codestacker/reports/
- [ ] .codestacker/project/plan/
- [ ] .codestacker/project/sessions/
- [ ] .codestacker/project/summaries/
- [ ] .codestacker/project/structure/

## Step 2: Missing Documentation Assessment
*Identifying what needs to be created*

### Required for Operation
- [ ] Project brief/basic info
- [ ] Project structure analysis
- [ ] Database schema (if applicable)

### Recommended for Optimal Function
- [ ] Architecture docs
- [ ] UI design specs
- [ ] Build specifications

## Step 3: Information Gathering
*The AI Agent MUST automatically scan the codebase before asking the user for information.*

### Step 3A: Auto-Discovery
The agent must use available tools (e.g., reading `package.json`, `tsconfig.json`, `requirements.txt`, `.env`, and directory listing) to determine:
- **Primary Language/Framework**: (e.g., Next.js, React, Node, Python)
- **Database**: (e.g., PostgreSQL, Supabase, MongoDB, sqlite, or none detected)
- **Environment Structure**: (e.g., Docker, .env variables present)
- **Folder Diagram**: (A brief tree view of the top-level directories)

**Present the auto-discovered findings to the user for validation:**
```markdown
🔍 **CodeStacker Auto-Discovery Complete**
- Language/Framework: [Detected]
- Database: [Detected]
- Environment: [Detected variables/tools]

**Folder Structure:**
` ` `text
/app
/components
/lib
...
` ` `
*Is this correct?*
```

### Step 3B: User Information Gathering
Only ask the user for information that cannot be auto-discovered:
1. **Project Name**: [What is this project called?]
2. **Current Phase**: [Just starting, in progress, maintenance?]
3. **Primary Goal**: [What's the main objective?]
4. **Timeline**: [Any deadlines or priorities?]
5. **Constraints**: [Any technical or business constraints?]

## Step 4: Documentation Generation Plan

Based on your answers, I will:
1. Create missing folders
2. Generate template docs with your info
3. Analyze existing code for structure docs
4. Build initial project structure analysis
5. Create first milestone log
6. Initialize `active_plan.md`

## Step 5: Ready Check
When all info is gathered, I will:
- [ ] Update brief.md with project context
- [ ] Create structure/01_project_overview.md
- [ ] Scan for existing code patterns
- [ ] Generate initial skills based on stack
- [ ] Create first summary
- [ ] Report ready status

## ⚠️ IMPORTANT
- This is a ONE-TIME setup
- After completion, normal .codestacker rules apply
- You can update any generated docs later
- Missing info will be requested as needed
