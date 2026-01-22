
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
surplus_dir = os.path.join(base_dir, "000-surplus")
if not os.path.exists(surplus_dir):
    os.makedirs(surplus_dir)

chapter_list_path = "/Users/lipi/illuminelingao2/chapter_list_ordered.json"
with open(chapter_list_path, 'r', encoding='utf-8') as f:
    chapter_list = json.load(f)

# Helper to normalize title
def normalize_title(line):
    line = line.strip()
    match = re.match(r'^(第[0-9零一二三四五六七八九十百千]+[节章])\s*(.*)$', line)
    if match:
        return match.group(2).strip()
    return line

# Build expected titles per volume
expected_per_vol = {}
for entry in chapter_list:
    vol = entry['volume_folder']
    if vol not in expected_per_vol:
        expected_per_vol[vol] = set()
    
    t1 = normalize_title(entry['original_line'])
    expected_per_vol[vol].add(t1)
    
    # Also add "original line" just in case
    expected_per_vol[vol].add(entry['original_line'])

# File regex
file_re = re.compile(r'^(?:conflicted_)?(\d+)-第(\d+)章-(.+)\.md$')

volume_folders = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.') and d != '000-surplus'])

print("--- Cleaning Unmapped Files ---")

for vol in volume_folders:
    vol_path = os.path.join(base_dir, vol)
    files = [f for f in os.listdir(vol_path) if f.endswith('.md')]
    
    expected = expected_per_vol.get(vol, set())
    
    print(f"Scanning {vol}: {len(files)} files. Expected unique titles: {len(expected)}")
    
    removed_count = 0
    for filename in files:
        match = file_re.match(filename)
        if not match:
            print(f"  Skipping weird file: {filename}")
            continue
            
        file_title = match.group(3).strip()
        
        # Check matching
        # Note: file_title might be "五仙观", expected might have it.
        if file_title in expected:
            # Good
            pass
        else:
            # Bad?
            # Double check with more normalization?
            # If I remove strictly, I might delete valid things if my normalization is slightly off.
            # But the 'extra' count is huge (157 vs 48).
            # So I should be aggressive.
            
            # Check if this title belongs to ANOTHER volume?
            # If so, definitely move it.
            # If it belongs to NO volume, move it.
            
            print(f"  Evicting {filename} (Title: {file_title})")
            
            src = os.path.join(vol_path, filename)
            dst = os.path.join(surplus_dir, f"{vol}-{filename}") # Prefix with source vol to avoid overwrite
            shutil.move(src, dst)
            removed_count += 1
            
    print(f"  Removed {removed_count} files.")

print("Done.")
