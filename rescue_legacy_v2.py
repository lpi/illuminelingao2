
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
legacy_dir = os.path.join(base_dir, "000-legacy-chapters")
mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"

with open(mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

def norm(s):
    return re.sub(r'[^\u4e00-\u9fff\d]', '', s)

# Robust lookup builder
lookup = {}
# Matches: (第)? [Numbers] [节章] Space* Title
# Numbers can be digits or chinese
# We need to strip the prefix to get the core title
prefix_re = re.compile(r'^(第)?([0-9\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343]+)([节章])\s*')

for k, v in title_mapping.items():
    # Attempt to strip prefix
    match = prefix_re.match(k)
    if match:
        core = k[match.end():] # Everything after the prefix
        n = norm(core)
        if n:
            lookup[n] = v
    else:
        # No prefix match? Maybe just title?
        n = norm(k)
        if n:
            lookup[n] = v
            
print(f"Built lookup with {len(lookup)} keys.")

# Scan Legacy
files = [f for f in os.listdir(legacy_dir) if f.endswith('.md')]
print(f"Scanning {len(files)} files in legacy...")

restored = 0

for filename in files:
    # Legacy filenames: "01-setting_sail-032-第32章-新年贺词.md"
    # We want "新年贺词".
    
    # Regex to find the LAST segment "第XX章-Title"
    # Note: Filenames might be complicated.
    # We rely on the "-第" pattern.
    parts = re.split(r'[-_]第[0-9]+[章节]-', filename)
    if len(parts) > 1:
        # The last part is the title + .md
        potential_title = parts[-1].replace('.md', '').strip()
        n_title = norm(potential_title)
        
        entries = lookup.get(n_title)
        if entries:
            # Found!
            # Use first entry or matching volume if possible? 
            # (Legacy filename has volume prefix, but it's the WRONG volume usually, e.g. "01-setting_sail")
            # So we trust the Mapping Entry.
            
            target_entry = entries[0]
            # If multiple mapping entries, we default to the first one (usually the canonical one).
            
            tgt_vol = target_entry['volume_folder']
            tgt_pos = target_entry['position']
            tgt_glob = target_entry['global_index']
            
            new_name = f"{tgt_pos:03d}-第{tgt_glob}章-{potential_title}.md"
            dest_dir = os.path.join(base_dir, tgt_vol)
            if not os.path.exists(dest_dir): os.makedirs(dest_dir)
            
            dest_path = os.path.join(dest_dir, new_name)
            src_path = os.path.join(legacy_dir, filename)
            
            if os.path.exists(dest_path):
                # Duplicate?
                # Read compare
                same = False
                try:
                    with open(dest_path,'rb') as f1, open(src_path,'rb') as f2:
                        if f1.read() == f2.read(): same = True
                except: pass
                
                if same:
                    print(f"Duplicate {new_name} in {tgt_vol}. Deleting legacy.")
                    os.remove(src_path)
                else:
                    print(f"Conflict {new_name} in {tgt_vol}. Renaming legacy to conflicted_legacy_...")
                    shutil.move(src_path, os.path.join(dest_dir, "conflicted_legacy_" + new_name))
            else:
                print(f"Restoring {potential_title} -> {tgt_vol}/{new_name}")
                shutil.move(src_path, dest_path)
            
            restored += 1
        else:
            # print(f"Unmapped: {potential_title} (norm: {n_title})")
            pass

print(f"Restored {restored} files.")
