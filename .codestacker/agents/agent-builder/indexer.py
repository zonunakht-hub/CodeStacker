import os
import glob
import re
import yaml

AGENTS_DIR = r"c:\VBOX\devserver\dev_10\.codestacker\agents"
REGISTRY_FILE = os.path.join(AGENTS_DIR, "AGENT_REGISTRY.md")

agents = []

for agent_file in glob.glob(os.path.join(AGENTS_DIR, "**", "AGENT.md"), recursive=True):
    with open(agent_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    name = os.path.basename(os.path.dirname(agent_file))
    desc = ""
    tags_str = "#agent"
    
    yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if yaml_match:
        try:
            frontmatter = yaml.safe_load(yaml_match.group(1))
            if isinstance(frontmatter, dict):
                name = frontmatter.get("name", name)
                desc = frontmatter.get("description", desc)
                if "tags" in frontmatter:
                    tags_str = frontmatter.get("tags")
        except:
            pass
            
    rel_path = os.path.relpath(agent_file, AGENTS_DIR).replace("\\", "/")
    agents.append(f"| {name} | `{rel_path}` | {tags_str} | {desc[:150] + '...' if len(desc) > 150 else desc} |")

# Sort agents alphabetically
agents.sort()

# Check if file exists, if not create barebones:
if not os.path.exists(REGISTRY_FILE):
    os.makedirs(AGENTS_DIR, exist_ok=True)
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        f.write("# 🤖 Agent Registry\n\n*Tracker for specialized Code Stacker team members.*\n\n| Agent | File | Tags | Description |\n|---|---|---|---|\n\n---\n")

if agents:
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        registry = f.read()
        
    start_marker = "| Agent | File | Tags | Description |"
    end_marker = "---"
    
    start_idx = registry.find(start_marker)
    if start_idx != -1:
        end_idx = registry.find(end_marker, start_idx + len(start_marker))
        if end_idx != -1:
            new_registry = registry[:start_idx] + "| Agent | File | Tags | Description |\n|---|---|---|---|\n" + "\n".join(agents) + "\n\n" + end_marker + "\n"
            
            with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
                f.write(new_registry)
            print(f"Indexed {len(agents)} agents into AGENT_REGISTRY.md")
        else:
            print("Couldn't find the end marker.")
    else:
        print("Couldn't find the table headers.")
