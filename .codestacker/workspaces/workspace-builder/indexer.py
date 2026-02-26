import os
import glob
import re
import yaml

WORKSPACES_DIR = r"c:\VBOX\devserver\dev_10\.codestacker\workspaces"
REGISTRY_FILE = os.path.join(WORKSPACES_DIR, "WORKSPACE_REGISTRY.md")

workspaces = []

# Search for both WORKSPACE.md and workspace_profile.md files
for profile_file in glob.glob(os.path.join(WORKSPACES_DIR, "**", "*.md"), recursive=True):
    filename = os.path.basename(profile_file).lower()
    if filename not in ["workspace.md", "workspace_profile.md"]:
        continue
        
    with open(profile_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get the parent folder name as the workspace ID
    dirname = os.path.basename(os.path.dirname(profile_file))
    name = dirname.replace("_", " ").title()
    desc = ""
    tags_str = "#workspace"
    
    # Extract YAML frontmatter if it exists
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
            
    # Extract Markdown H1 if YAML name wasn't found
    if not desc:
        desc_match = re.search(r"^## Purpose\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip()
            
    rel_path = os.path.relpath(profile_file, WORKSPACES_DIR).replace("\\", "/")
    
    # Avoid inserting the workspace registry or readme itself if processed accidentally
    if "REGISTRY" not in rel_path and "README" not in rel_path:
        # Avoid duplicate index entries for the same workspace
        if not any(f"| `{dirname}/` |" in w for w in workspaces):
            workspaces.append(f"| {name} | `{dirname}/` | {tags_str} | {desc[:150] + '...' if len(desc) > 150 else desc} |")

# Sort workspaces alphabetically
workspaces.sort()

# Create barebones registry if it doesn't exist
if not os.path.exists(REGISTRY_FILE):
    os.makedirs(WORKSPACES_DIR, exist_ok=True)
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        f.write("# 🏢 Workspace Registry\n\n*Index of all isolated enterprise environments.*\n\n| Workspace | Directory | Tags | Purpose |\n|---|---|---|---|\n\n---\n")

if workspaces:
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        registry = f.read()
        
    start_marker = "| Workspace | Directory | Tags | Purpose |"
    end_marker = "---"
    
    start_idx = registry.find(start_marker)
    if start_idx != -1:
        end_idx = registry.find(end_marker, start_idx + len(start_marker))
        if end_idx != -1:
            new_registry = registry[:start_idx] + "| Workspace | Directory | Tags | Purpose |\n|---|---|---|---|\n" + "\n".join(workspaces) + "\n\n" + end_marker + "\n"
            
            with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
                f.write(new_registry)
            print(f"Indexed {len(workspaces)} workspaces into WORKSPACE_REGISTRY.md")
        else:
            print("Couldn't find the end marker.")
    else:
        print("Couldn't find the table headers.")
else:
    print("0 active workspaces found to log.")
