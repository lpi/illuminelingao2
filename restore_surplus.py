
import os
import shutil
import json
import re

# Paths
base_dir = "/Users/lipi/illuminelingao2/chapters"
surplus_dir = os.path.join(base_dir, "000-surplus")
mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"
english_chapters_dir = "/Users/lipi/illuminelingao2/english_chapters"

# Load mapping
with open(mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

# Helper to normalize title (remove punctuation/spaces key)
# The keys in title_mapping are usually the pure Chinese characters + sometimes numbers
# We need to match what we extracted from filename.
def normalize_key(k):
    return re.sub(r'[^\w\u4e00-\u9fff]', '', k)

# Create a normalized lookup
lookup = {}
for k, v in title_mapping.items():
    norm = normalize_key(k)
    # also store exact k
    lookup[k] = v
    if norm != k:
        lookup[norm] = v

# Regex to extract title from filename
# Filenames in surplus are like: "01-setting_sail-001-第1章-忙碌的刘市长.md"
# Or "conflicted_003-041-第41章-议和（一）.md"
# Or just "001-第1章-....md"
# We want the part after the last "第X章-" or "第X节-" pattern.

def extract_title(filename):
    # Try finding the standard pattern "第X章-" or "第X节-"
    # Use rfind to find the LAST occurrence 
    match = re.search(r'第[0-9零一二三四五六七八九十百千]+[章节]-(.+)\.md$', filename)
    if match:
        return match.group(1).strip()
    return None

files = [f for f in os.listdir(surplus_dir) if f.endswith('.md')]
print(f"Processing {len(files)} files from surplus...")

moved_count = 0
deleted_count = 0
unmapped_count = 0

for filename in files:
    title = extract_title(filename)
    if not title:
        print(f"Skipping {filename} (no title extracted)")
        unmapped_count += 1
        continue
    
    # Try to find in mapping
    entries = lookup.get(title)
    if not entries:
        # Try normalized
        entries = lookup.get(normalize_key(title))
    
    if not entries:
        print(f"Unmapped: {filename} (Title: {title})")
        # Is it a title with English? e.g. "H800型"
        # Maybe fuzzy match?
        unmapped_count += 1
        continue
        
    # We found mapping entries.
    # If multiple entries (e.g. generic title), we need to decide.
    # Since we are restoring from "Surplus", we don't know the volume context easily.
    # However, some filenames have the volume prefix "01-setting_sail-..."
    # We can use that hint!
    
    target_entry = entries[0]
    
    # Check for volume hint in filename
    for entry in entries:
        if entry['volume_folder'] in filename:
            target_entry = entry
            break
            
    # Destination
    vol_folder = target_entry['volume_folder']
    pos = target_entry['position']
    glob = target_entry['global_index']
    
    new_name = f"{pos:03d}-第{glob}章-{title}.md"
    dest_path = os.path.join(base_dir, vol_folder, new_name)
    
    src_path = os.path.join(surplus_dir, filename)
    
    if os.path.exists(dest_path):
        # Target exists. Check content.
        is_same = False
        try:
            with open(src_path, 'rb') as f1, open(dest_path, 'rb') as f2:
                if f1.read() == f2.read():
                    is_same = True
        except:
            pass
            
        if is_same:
            # Delete surplus
            # print(f"Duplicate content for {title} in {vol_folder}. Deleting surplus.")
            os.remove(src_path)
            deleted_count += 1
        else:
            # Conflict.
            # print(f"Content mismatch for {title} in {vol_folder}. Keeping as conflicted.")
            # Move back to root as conflicted? Or keep in surplus?
            # User wants them in "correct volume folder".
            # So move to volume folder with "conflicted_" prefix.
            conflict_name = f"conflicted_{pos:03d}-{title}.md"
            conflict_path = os.path.join(base_dir, vol_folder, conflict_name)
            shutil.move(src_path, conflict_path)
            moved_count += 1
    else:
        # Move
        # print(f"Restoring {title} to {vol_folder}")
        if not os.path.exists(os.path.join(base_dir, vol_folder)):
            os.makedirs(os.path.join(base_dir, vol_folder))
        shutil.move(src_path, dest_path)
        moved_count += 1

print(f"Summary: Moved {moved_count}, Deleted (duplicates) {deleted_count}, Unmapped {unmapped_count}")

# After moving, double check english side matching
print("\n--- English Side Check ---")
for vol in sorted(os.listdir(base_dir)):
    vol_path = os.path.join(base_dir, vol)
    if not os.path.isdir(vol_path) or vol.startswith('.'): continue
    
    c_files = len([f for f in os.listdir(vol_path) if f.endswith('.md')])
    
    e_path = os.path.join(english_chapters_dir, vol)
    if os.path.exists(e_path):
        e_files = len([f for f in os.listdir(e_path) if f.endswith('.md')])
        print(f"{vol}: Chinese {c_files}, English {e_files}")
    else:
        print(f"{vol}: Chinese {c_files}, English 0 (Missing Dir)")

