
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
chapter_list_path = "/Users/lipi/illuminelingao2/chapter_list_ordered.json"

with open(chapter_list_path, 'r', encoding='utf-8') as f:
    chapter_list = json.load(f)

# Helper to normalize title
def normalize_title(line):
    # Remove prefix like "第xxx节" or "第xxx章"
    # Also handle Chinese numerals
    # Example: "第二百七十一节 五仙观" -> "五仙观"
    # Regex: Start with optional whitespace, then 第, then char class of numbers/chinese nums, then 节 or 章, then whitespace
    # We grab the REST.
    
    # Simple strip first
    line = line.strip()
    
    # Advanced strip
    # Try to match the Prefix
    match = re.match(r'^(第[0-9零一二三四五六七八九十百千]+[节章])\s*(.*)$', line)
    if match:
        return match.group(2).strip()
        
    # If no prefix match, return line as is (maybe it's just the title)
    return line

# Build mapping
title_to_target = {}

for entry in chapter_list:
    original = entry['original_line']
    clean = normalize_title(original)
    
    # Store both clean and original if different
    title_to_target[clean] = entry
    if original != clean:
        title_to_target[original] = entry

print(f"Built mapping with {len(title_to_target)} keys.")

# Validate logic
test_t = "五仙观"
if test_t in title_to_target:
    print(f"Mapped '{test_t}' -> Volume {title_to_target[test_t]['volume_folder']}")
else:
    print(f"WARNING: '{test_t}' NOT mapped.")

# Files regex
file_re = re.compile(r'^(?:conflicted_)?(\d+)-第(\d+)章-(.+)\.md$')

def process_dir(dirname):
    dirpath = os.path.join(base_dir, dirname)
    if not os.path.isdir(dirpath): return
    
    files = [f for f in os.listdir(dirpath) if f.endswith('.md')]
    print(f"Scanning {dirname} ({len(files)} files)...")
    
    for filename in files:
        match = file_re.match(filename)
        if not match:
            continue
            
        file_title = match.group(3).strip()
        
        target = title_to_target.get(file_title)
        if not target:
            # Try removing special chars?
            # Or maybe the file title is "五仙观" but mapping has...
            # Actually, let's log failures
            # print(f"  Unmapped: {file_title}")
            continue
            
        target_vol = target['volume_folder']
        target_pos = target['position']
        target_glob = target['global_index']
        
        # Decide
        new_name = f"{target_pos:03d}-第{target_glob}章-{file_title}.md"
        dest_folder = os.path.join(base_dir, target_vol)
        dest_path = os.path.join(dest_folder, new_name)
        curr_path = os.path.join(dirpath, filename)
        
        if dirname != target_vol:
            # Move
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            if os.path.exists(dest_path):
                # Target exists. Duplicate?
                print(f"  Collision: {filename} wants to go to {target_vol}/{new_name} but exists.")
                # Force overwrite if content same? 
                # Rename to verify later
                new_conflict_name = f"conflicted_{target_pos:03d}-{filename}"
                os.rename(curr_path, os.path.join(base_dir, new_conflict_name))
            else:
                print(f"  Moving {filename} -> {target_vol}/{new_name}")
                shutil.move(curr_path, dest_path)
        else:
            # Same volume, check name
            if filename != new_name:
                print(f"  Renaming {filename} -> {new_name}")
                os.rename(curr_path, dest_path)

# Run
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')]
for d in subdirs:
    process_dir(d)

print("Done.")
