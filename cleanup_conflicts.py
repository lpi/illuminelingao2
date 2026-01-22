
import os
import json

base_dir = "/Users/lipi/illuminelingao2/chapters"
conflicted_files = [
    "conflicted_385-第385章-新的线索.md",
    "conflicted_239-第239章-判决.md",
    "conflicted_286-第286章-少年.md",
    "conflicted_380-第380章-借题发挥.md"
]

# We need to find checks.
# For each conflicted file, we know the title.
# We check ALL valid locations for that title.
# If content matches ANY, it's a duplicate -> Delete.

title_mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"
with open(title_mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

for c_file in conflicted_files:
    c_path = os.path.join(base_dir, c_file)
    if not os.path.exists(c_path):
        continue
        
    # Extract title
    # naming format: conflicted_POS-第GLOBAL章-TITLE.md
    parts = c_file.split('-')
    if len(parts) >= 3:
        title = parts[-1].replace('.md', '')
    else:
        print(f"Skipping {c_file}, weird name")
        continue

    entries = title_mapping.get(title)
    if not entries:
        print(f"Title {title} not found for {c_file}")
        continue
        
    is_duplicate = False
    for entry in entries:
        vol = entry['volume_folder']
        pos = entry['position']
        glob = entry['global_index']
        
        # Expected filename in duplicate location
        # Matches pattern {pos:03d}-第{glob}章-{title}.md
        target_name = f"{pos:03d}-第{glob}章-{title}.md"
        target_path = os.path.join(base_dir, vol, target_name)
        
        if os.path.exists(target_path):
            # Compare
            with open(c_path, 'rb') as f1, open(target_path, 'rb') as f2:
                if f1.read() == f2.read():
                    print(f"File {c_file} is identical to {vol}/{target_name}. Deleting.")
                    os.remove(c_path)
                    is_duplicate = True
                    break
    
    if not is_duplicate:
        print(f"File {c_file} is NOT identical to any target. Check manually.")

