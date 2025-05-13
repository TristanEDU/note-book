import os
import yaml

MKDOCS_FILE = "mkdocs.yml"
DOCS_DIR = "docs"

def human_title(name):
    return name.replace('-', ' ').replace('_', ' ').title()

def scan_directory(path):
    items = []
    for name in sorted(os.listdir(path)):
        full_path = os.path.join(path, name)
        rel_path = os.path.relpath(full_path, DOCS_DIR).replace("\\", "/")

        if os.path.isdir(full_path):
            children = scan_directory(full_path)
            if children:
                items.append({human_title(name): children})
        elif name.endswith(".md") and name != "index.md":
            title = human_title(name[:-3])
            items.append({title: rel_path})
    return items

def update_nav():
    with open(MKDOCS_FILE, "r") as f:
        config = yaml.safe_load(f)

    config["nav"] = [{"Home": "index.md"}] + scan_directory(DOCS_DIR)

    with open(MKDOCS_FILE, "w") as f:
        yaml.dump(config, f, sort_keys=False)

    print("✅ mkdocs.yml nav updated!")

if __name__ == "__main__":
    update_nav()
