
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"
legacy_dir = os.path.join(base_dir, "000-legacy-chapters")

if not os.path.exists(legacy_dir):
    os.makedirs(legacy_dir)

# Load mapping
with open(mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

# Normalize
def aggressive_norm(k):
    return re.sub(r'[^\u4e00-\u9fff\d]', '', k)

lookup = {}
for k, v in title_mapping.items():
    norm = aggressive_norm(k)
    lookup[norm] = v

    # Also add the stripped key (just text)
    # E.g. "第一节 虫洞降临" -> "虫洞降临"
    match = re.search(r'第[0-9零一二三四五六七八九十百千]+[章节]\s*(.*)', k)
    if match:
        core_title = match.group(1).strip()
        norm_core = aggressive_norm(core_title)
        if norm_core not in lookup:
            lookup[norm_core] = v

print("Title mapping loaded.")

# Scan all volumes
vols = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.') and d != "000-legacy-chapters" and d != "000-surplus"]

moved_count = 0
legacy_count = 0

for vol in vols:
    vol_path = os.path.join(base_dir, vol)
    files = [f for f in os.listdir(vol_path) if f.endswith('.md')]
    print(f"Scanning {vol} ({len(files)} files)...")
    
    for filename in files:
        # Extract title
        match = re.search(r'第[0-9零一二三四五六七八九十百千]+[章节]-(.+)\.md$', filename)
        if not match:
            # Maybe it doesn't have "第X章-" pattern?
            # Try splitting by '-'?
            # E.g. "001-Chapter1-Title.md"? No these are chinese.
            print(f"  Skipping weird filename: {filename}")
            continue
            
        title = match.group(1).strip()
        norm_title = aggressive_norm(title)
        
        # Look up
        entries = lookup.get(norm_title)
        
        target = None
        
        if entries:
            # Found mapping.
            # If multiple entries, check if one matches CURRENT volume.
            found_current = False
            for e in entries:
                if e['volume_folder'] == vol:
                    target = e
                    found_current = True
                    break
            
            if not found_current:
                # If NOT in current volume, move to the first mapped volume?
                # Or closest global index?
                # Default to first one
                target = entries[0]
        
        if target:
            # We have a target.
            target_vol = target['volume_folder']
            target_pos = target['position']
            target_glob = target['global_index']
            
            new_name = f"{target_pos:03d}-第{target_glob}章-{title}.md"
            
            if target_vol != vol:
                # Move to correct volume
                dest_dir = os.path.join(base_dir, target_vol)
                if not os.path.exists(dest_dir): os.makedirs(dest_dir)
                dest_path = os.path.join(dest_dir, new_name)
                src_path = os.path.join(vol_path, filename)
                
                if os.path.exists(dest_path):
                    # Collision
                    # Compare
                    is_same = False
                    try:
                        with open(src_path, 'rb') as f1, open(dest_path, 'rb') as f2:
                            if f1.read() == f2.read(): is_same = True
                    except: pass
                    
                    if is_same:
                        print(f"  Duplicate of {target_vol}/{new_name}. Deleting.")
                        os.remove(src_path)
                    else:
                        print(f"  Move Conflict: {filename} -> {target_vol}. Renaming to conflicted.")
                        conflict_name = f"conflicted_{target_pos:03d}-{title}.md"
                        shutil.move(src_path, os.path.join(dest_dir, conflict_name))
                else:
                    print(f"  Moving Misplaced: {filename} -> {target_vol}/{new_name}")
                    shutil.move(src_path, dest_path)
                moved_count += 1
            else:
                # Correct volume. Check name.
                if filename != new_name and not filename.startswith("conflicted_"):
                    # Rename to canonical
                    # Check collision
                    dest_path = os.path.join(vol_path, new_name)
                    if os.path.exists(dest_path):
                         # Target name exists (e.g. 002-第6章 exists, we have 002-第2章)
                         # If content diff, it's a conflict?
                         # Actually if title maps to SAME entry, name should be same.
                         pass
                    else:
                        print(f"  Renaming Canonical: {filename} -> {new_name}")
                        os.rename(os.path.join(vol_path, filename), dest_path)
        else:
            # Unmapped -> Legacy
            # "Busy Mayor Liu" etc.
            print(f"  Legacy (Unmapped): {filename}")
            shutil.move(os.path.join(vol_path, filename), os.path.join(legacy_dir, f"{vol}-{filename}"))
            legacy_count += 1

print(f"Done. Moved {moved_count}, Legacy {legacy_count}.")
