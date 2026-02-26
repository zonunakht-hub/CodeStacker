import os
import glob
import re
import yaml

SKILLS_DIR = r"c:\VBOX\devserver\dev_10\.codestacker\skills"
REGISTRY_FILE = os.path.join(SKILLS_DIR, "SKILL_REGISTRY.md")

skills = []

def infer_tags(text):
    text = text.lower()
    tags = set()
    if "ui" in text or "ux" in text or "component" in text or "design" in text or "frontend" in text or "layout" in text:
        tags.add("#ui")
    if "react" in text or "next" in text:
        tags.add("#react")
    if "supabase" in text or "database" in text or "sql" in text or "postgres" in text:
        tags.add("#database")
    if "api" in text or "rest" in text or "graphql" in text:
        tags.add("#api")
    if "python" in text:
        tags.add("#python")
    if "test" in text or "jest" in text or "cypress" in text or "playwright" in text:
        tags.add("#testing")
    if "css" in text or "tailwind" in text:
        tags.add("#tailwind")
    if "aws" in text or "docker" in text or "vercel" in text or "deploy" in text:
        tags.add("#devops")
    if "automation" in text or "agent" in text or "claude" in text or "ai " in text:
        tags.add("#ai")
    
    if not tags:
        tags.add("#general")
    return " ".join(tags)

for skill_file in glob.glob(os.path.join(SKILLS_DIR, "**", "SKILL.md"), recursive=True):
    with open(skill_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    name = os.path.basename(os.path.dirname(skill_file))
    desc = ""
    
    # Try reading YAML frontmatter
    yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if yaml_match:
        try:
            frontmatter = yaml.safe_load(yaml_match.group(1))
            if isinstance(frontmatter, dict):
                name = frontmatter.get("name", name)
                desc = frontmatter.get("description", desc)
        except:
            pass
            
    if not desc:
        desc_match = re.search(r"^>\s*(.+)$", content, re.MULTILINE)
        if desc_match: 
            desc = desc_match.group(1).strip()
    
    tags_str = infer_tags(name + " " + desc + " " + content)
    
    rel_path = os.path.relpath(skill_file, SKILLS_DIR).replace("\\", "/")
    
    skills.append(f"| {name} | `{rel_path}` | {tags_str} | {desc[:150] + '...' if len(desc) > 150 else desc} |")

if skills:
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        registry = f.read()
        
    start_marker = "| Skill | File | Tags | Description |"
    end_marker = "---"
    
    start_idx = registry.find(start_marker)
    if start_idx != -1:
        end_idx = registry.find(end_marker, start_idx + len(start_marker))
        if end_idx != -1:
            new_registry = registry[:start_idx] + "| Skill | File | Tags | Description |\n|---|---|---|---|\n" + "\n".join(skills) + "\n\n" + registry[end_idx:]
            
            with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
                f.write(new_registry)
            print(f"Indexed {len(skills)} skills into SKILL_REGISTRY.md")
        else:
            print("Couldn't find the end marker.")
    else:
        print("Couldn't find the table headers.")
