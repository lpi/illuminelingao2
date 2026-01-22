
import os
import shutil
import json
import re

# Load base paths
base_dir = "/Users/lipi/illuminelingao2/chapters"
title_mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"
english_chapters_dir = "/Users/lipi/illuminelingao2/english_chapters"

# Load mapping
with open(title_mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

# Helper function to extract title
def extract_title(filename):
    match = re.search(r'第\d+章-(.+)\.md', filename)
    if match:
        title = match.group(1).strip()
        # Some normalizations if needed
        return title
    return None

files = [f for f in os.listdir(base_dir) if f.endswith('.md')]

print(f"Found {len(files)} files in root.")

for filename in files:
    title = extract_title(filename)
    if not title:
        print(f"Skipping {filename}: Could not extract title")
        continue
    
    # Try to find target
    mapping = title_mapping.get(title)
    if not mapping:
        # Try fuzzy match or removing parts? 
        # For now, simplistic check
        pass
        
    if mapping:
        # There might be multiple destinations for a title.
        # Check which one matches or if we should just pick one?
        # A lot of these remaining files are likely duplicates where the filename number is just an internal index (not global).
        # We need to find the destination that makes sense.
        # But wait, if they are duplicates of EXISTING files, we can just delete them if content is same.
        
        # Let's check all potential destinations
        found_match = False
        for m in mapping:
            target_vol = m['volume_folder']
            target_pos = m['position']
            target_global = m['global_index']
            
            # Construct expected filename
            # Note: We need to know what the existing file is named.
            # It usually starts with {target_pos:03d}-...
            
            vol_path = os.path.join(base_dir, target_vol)
            if not os.path.exists(vol_path):
                continue
                
            # Look for file starting with target_pos
            existing_files = [f for f in os.listdir(vol_path) if f.startswith(f"{target_pos:03d}-")]
            
            if existing_files:
                target_file_path = os.path.join(vol_path, existing_files[0])
                # Compare content
                try:
                    with open(os.path.join(base_dir, filename), 'rb') as f1, open(target_file_path, 'rb') as f2:
                        c1 = f1.read()
                        c2 = f2.read()
                        if c1 == c2:
                            print(f"DELETE Duplicate: {filename} == {target_vol}/{existing_files[0]}")
                            os.remove(os.path.join(base_dir, filename))
                            found_match = True
                            break
                        else:
                            print(f"Content DIFFERS: {filename} vs {target_vol}/{existing_files[0]}")
                            # If content differs, maybe we should overwrite? User said put them in correct folder.
                            # But maybe the one in root is the "wrong" one or an old version?
                            # Or maybe it's a collision title.
                except Exception as e:
                    print(f"Error checking {filename}: {e}")
            else:
                 # Destination doesn't exist? Then move it there!
                 new_name = f"{target_pos:03d}-第{target_global}章-{title}.md"
                 print(f"MOVE: {filename} -> {target_vol}/{new_name}")
                 shutil.move(os.path.join(base_dir, filename), os.path.join(vol_path, new_name))
                 found_match = True
                 break
        
        if not found_match and not os.path.exists(os.path.join(base_dir, filename)):
            # File was deleted/moved
            pass
        elif not found_match:
            print(f"Unresolved: {filename}")

# Also check for English folder structure match
print("\nChecking English folder structure...")
chinese_vols = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')])
english_vols = sorted([d for d in os.listdir(english_chapters_dir) if os.path.isdir(os.path.join(english_chapters_dir, d)) and not d.startswith('.')])

print(f"Chinese Volumes: {len(chinese_vols)}")
print(f"English Volumes: {len(english_vols)}")

for v in chinese_vols:
    c_count = len([f for f in os.listdir(os.path.join(base_dir, v)) if f.endswith('.md')])
    if v in english_vols:
        e_path = os.path.join(english_chapters_dir, v)
        e_count = len([f for f in os.listdir(e_path) if f.endswith('.md')])
        print(f"{v}: Chinese={c_count}, English={e_count}")
        if c_count != e_count:
            print(f"  WARNING: Count mismatch in {v}")
    else:
        print(f"  WARNING: Missing English volume {v}")

