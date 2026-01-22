
import os
import shutil
import json
import re

# Paths
base_dir = "/Users/lipi/illuminelingao2/chapters"
title_mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"
english_chapters_dir = "/Users/lipi/illuminelingao2/english_chapters"

# Load mapping
with open(title_mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

# Helper to normalize title for matching
def normalize_title(t):
    # Remove punctuation, spaces, etc.
    return re.sub(r'[^\w\u4e00-\u9fff]', '', t)

# Build a lookup from title -> target info
# We use strict title matching.
title_lookup = {}
for title, entries in title_mapping.items():
    # If duplicates, we might have issues. But usually specific titles are unique.
    # Entries is a list.
    title_lookup[title] = entries

# Also build a set of valid expected files per volume to checking completion later
expected_structure = {}

# Regex for filename
filename_re = re.compile(r'^(?:conflicted_)?(\d+)-第(\d+)章-(.+)\.md$')
# Also handle old format: 001-第1章-Title.md
filename_old_re = re.compile(r'^(\d+)-第(\d+)章-(.+)\.md$')

# Function to extract title from filename
def extract_info(filename):
    match = filename_re.match(filename)
    if match:
        return match.group(3).strip()
    return None

def process_directory(current_dir_name):
    current_dir_path = os.path.join(base_dir, current_dir_name)
    if not os.path.isdir(current_dir_path):
        return

    files = [f for f in os.listdir(current_dir_path) if f.endswith('.md')]
    print(f"Processing {current_dir_name} ({len(files)} files)...")
    
    for filename in files:
        title = extract_info(filename)
        if not title:
            print(f"  Skipping {filename}: unexpected format")
            continue
            
        mapping = title_lookup.get(title)
        if not mapping:
            # Try fuzzy match?
            # For now skip
            print(f"  Unknown title: {title} in {filename}")
            continue
            
        # Determine correct destination
        # If multiple mappings, we need to guess which one.
        # But we are cleaning up, so we should look for the ONE that fits best?
        # Or if one title appears in multiple volumes, we might need to check content?
        # Let's naive approach: use the first mapping, or if current volume is valid, keep it.
        
        target = None
        
        # Check if the file is ALREADY in one of the valid volumes
        valid_vols = [m['volume_folder'] for m in mapping]
        if current_dir_name in valid_vols:
            # It's in a valid volume!
            # Which entry corresponds to this volume?
            for m in mapping:
                if m['volume_folder'] == current_dir_name:
                    target = m
                    break
        else:
            # It's in the WRONG volume (e.g. Vol 6 file in Vol 1)
            # Pick the first mapping? Or try to be smart?
            # Default to first mapping for now.
            target = mapping[0]
            
        target_vol = target['volume_folder']
        target_pos = target['position']
        target_global = target['global_index']
        
        # Construct correct filename
        new_name = f"{target_pos:03d}-第{target_global}章-{title}.md"
        dest_folder = os.path.join(base_dir, target_vol)
        dest_path = os.path.join(dest_folder, new_name)
        
        curr_path = os.path.join(current_dir_path, filename)
        
        # Check if we need to move
        if current_dir_name != target_vol:
            # Move needed
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            if os.path.exists(dest_path):
                print(f"  Collision moving {filename} to {target_vol}: Target exists.")
                # Compare content? 
                # If target exists, maybe we delete this one if content same?
                # Or skip?
                # For safety, skipping, but verify content manually?
                os.rename(curr_path, os.path.join(base_dir, "conflicted_" + filename))
            else:
                print(f"  Moving {filename} -> {target_vol}/{new_name}")
                shutil.move(curr_path, dest_path)
        else:
            # In correct volume, check filename
            if filename != new_name:
                if os.path.exists(dest_path):
                     # Target name exists (maybe duplicate file with different name?)
                     print(f"  Duplicate in same folder? {filename} vs {new_name}")
                     # Check content, if same delete
                else:
                    print(f"  Renaming {filename} -> {new_name}")
                    os.rename(curr_path, dest_path)

# 1. Process Root
print("--- Cleaning Root ---")
# Root is conceptually "not a volume", so everything here should move.
# I pass "" as dir name? No, I scan root separately? 
# The function process_directory assumes subdirs.
# Let's run it on actual subdirs.
# But I also need to process root files.

root_files = [f for f in os.listdir(base_dir) if f.endswith('.md')]
print(f"Processing Root ({len(root_files)} files)...")
for filename in root_files:
    # Logic similar to above, but current_dir is "" so it will always move
    title = extract_info(filename)
    if not title:
        continue
    mapping = title_lookup.get(title)
    if not mapping:
        print(f"  Unmapped root file: {filename}")
        continue
        
    # Default to first target
    target = mapping[0]
    target_vol = target['volume_folder']
    target_pos = target['position']
    target_global = target['global_index']
    
    new_name = f"{target_pos:03d}-第{target_global}章-{title}.md"
    dest_folder = os.path.join(base_dir, target_vol)
    dest_path = os.path.join(dest_folder, new_name)
    
    curr_path = os.path.join(base_dir, filename)
    
    if os.path.exists(dest_path):
        print(f"  Root file duplicate of existing: {target_vol}/{new_name}")
        # Delete root file?
        os.remove(curr_path)
    else:
        print(f"  Moving root to {target_vol}/{new_name}")
        if not os.path.exists(dest_folder):
             os.makedirs(dest_folder)
        shutil.move(curr_path, dest_path)

# 2. Process Volumes
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d != '00-extras-fanworks'] 
# Skip extras? No, process all including extras
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for d in subdirs:
    process_directory(d)

print("Done.")
