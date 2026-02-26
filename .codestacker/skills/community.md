# 🌐 Community Skills

## Repository
**[CodeStacker-Skills](https://github.com/CoSama-Ai/CodeStacker-Skills)**

Skills are curated from many contributors and open-source communities, then reviewed and adapted to work within the `.codestacker` system. See `CONTRIBUTORS.md` for full attribution.

---

## Installation Options

### Option 1 — Full Install (All Skills)

```bash
# From your project root
git clone https://github.com/CoSama-Ai/CodeStacker-Skills.git /tmp/cs-skills

cp -r /tmp/cs-skills/language_skills/* .codestacker/skills/languages/
cp -r /tmp/cs-skills/framework_skills/* .codestacker/skills/frameworks/
cp -r /tmp/cs-skills/database_skills/* .codestacker/skills/databases/
cp -r /tmp/cs-skills/testing_skills/* .codestacker/skills/testing/
cp -r /tmp/cs-skills/devops_skills/* .codestacker/skills/devops/

rm -rf /tmp/cs-skills
```

### Option 2 — By Category

Clone the repo, then copy only the folders you need:

```bash
git clone https://github.com/CoSama-Ai/CodeStacker-Skills.git /tmp/cs-skills

# Pick any combination:
cp -r /tmp/cs-skills/language_skills/* .codestacker/skills/languages/
cp -r /tmp/cs-skills/framework_skills/* .codestacker/skills/frameworks/
cp -r /tmp/cs-skills/database_skills/* .codestacker/skills/databases/
cp -r /tmp/cs-skills/testing_skills/* .codestacker/skills/testing/
cp -r /tmp/cs-skills/devops_skills/* .codestacker/skills/devops/

rm -rf /tmp/cs-skills
```

| Category | Source Folder | Local Destination |
|----------|--------------|-------------------|
| Languages | `language_skills/` | `skills/languages/` |
| Frameworks | `framework_skills/` | `skills/frameworks/` |
| Databases | `database_skills/` | `skills/databases/` |
| Testing | `testing_skills/` | `skills/testing/` |
| DevOps | `devops_skills/` | `skills/devops/` |

### Option 3 — Individual Skill File

Download a single skill directly:

```bash
# Example: Next.js framework skill
curl -o .codestacker/skills/frameworks/nextjs.md \
  https://raw.githubusercontent.com/CoSama-Ai/CodeStacker-Skills/main/framework_skills/nextjs.md
```

Browse the repo on GitHub → open any file → click **Raw** → save into the matching local folder.

### Option 4 — AI-Assisted

Tell your AI assistant:

```
Mode Free - Install the Next.js and PostgreSQL skills from the CodeStacker-Skills repo
```

The AI reads this file, downloads the correct files, places them in the right folders, and updates `INDEX.md`.

---

## After Installing

1. Run `Mode Skill Index` — the AI rebuilds `SKILL_REGISTRY.md` automatically
2. The AI automatically references installed skills during `Mode Plan`
3. To remove a skill: delete the file and run `Mode Skill Index` again
