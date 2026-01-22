
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
surplus_dir = os.path.join(base_dir, "000-surplus")
mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"

# Load mapping
with open(mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

# Aggressive normalization for mapping
def aggressive_norm(k):
    # Remove all non-chinese and non-digit characters
    return re.sub(r'[^\u4e00-\u9fff\d]', '', k)

lookup = {}
for k, v in title_mapping.items():
    norm = aggressive_norm(k)
    lookup[norm] = v

valid_vols = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')]

print("--- Restoring from Surplus ---")

files = os.listdir(surplus_dir)
count = 0

for filename in files:
    if not filename.endswith('.md'): continue
    
    src_path = os.path.join(surplus_dir, filename)
    
    target_vol = None
    target_filename = filename
    
    # 1. Check for Volume Prefix (Evicted files)
    # Format: {VOL}-{OriginalFilename}
    # We need to be careful not to match partials.
    # Longest match first.
    
    best_match_vol = None
    for vol in valid_vols:
        prefix = vol + "-"
        if filename.startswith(prefix):
            # Verify it's not a false match (e.g. vol "01" matching "011-")
            # The folders are like "01-setting_sail", quite unique.
            if best_match_vol is None or len(vol) > len(best_match_vol):
                best_match_vol = vol
    
    if best_match_vol:
        target_vol = best_match_vol
        target_filename = filename[len(best_match_vol)+1:] # Strip VOL-
        # Validate target_filename is valid?
    else:
        # 2. No prefix? Try mapping title.
        # Extract title
        # Filename might be "conflicted_..." or just "POS-第...章-TITLE.md"
        match = re.search(r'第[0-9零一二三四五六七八九十百千]+[章节]-(.+)\.md$', filename)
        if match:
            t = match.group(1).strip()
            # Normalize
            norm_t = aggressive_norm(t)
            entries = lookup.get(norm_t)
            if entries:
                # Use first entry
                target_entry = entries[0]
                target_vol = target_entry['volume_folder']
                # Construct canonical name
                target_filename = f"{target_entry['position']:03d}-第{target_entry['global_index']}章-{t}.md"
            else:
                 # Mapping failed.
                 pass

    if target_vol:
        dest_folder = os.path.join(base_dir, target_vol)
        dest_path = os.path.join(dest_folder, target_filename)
        
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            
        if os.path.exists(dest_path):
            # Compare
            is_same = False
            try:
                with open(src_path, 'rb') as f1, open(dest_path, 'rb') as f2:
                    if f1.read() == f2.read():
                        is_same = True
            except: pass
            
            if is_same:
                print(f"Deleting duplicate: {filename} (exists in {target_vol})")
                os.remove(src_path)
            else:
                print(f"Conflict restoring {filename} to {target_vol}. Renaming.")
                # Rename to avoid overwrite
                new_name = "restored_" + target_filename
                shutil.move(src_path, os.path.join(dest_folder, new_name))
        else:
            print(f"Restoring {filename} -> {target_vol}/{target_filename}")
            shutil.move(src_path, dest_path)
        count += 1
    else:
        print(f"Could not determine target for {filename}")

print(f"Processed {count} files.")
