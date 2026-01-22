
import os
import shutil
import json
import re

base_dir = "/Users/lipi/illuminelingao2/chapters"
legacy_dir = os.path.join(base_dir, "000-legacy-chapters")
mapping_path = "/Users/lipi/illuminelingao2/title_mapping.json"

# Load mapping
with open(mapping_path, 'r', encoding='utf-8') as f:
    title_mapping = json.load(f)

def norm(s):
    return re.sub(r'[^\u4e00-\u9fff\d]', '', s)

# Build a reverse lookup: Normalized Title Text -> Entry
# The mapping keys are like "二百二十六节忙碌的刘市长". 
# We want to map "忙碌的刘市长" -> Entry.
# So we strip the leading numbering from the keys.

title_lookup = {}

# Regex to strip "第xx节" or "二百二十六节" etc from the start
# Chinese numbers: 零一二三四五六七八九十百千
# Structure: (第)? [Numbers] (节|章)
# Note: "Section 226" might be "二百二十六节" or "第226节"
prefix_re = re.compile(r'^(?:第)?[0-9\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343]+[节章]')

for key, entries in title_mapping.items():
    # Key is normalized.
    # Try to strip prefix
    match = prefix_re.match(key)
    if match:
        pure_title = key[match.end():]
        if pure_title:
            title_lookup[pure_title] = entries
    else:
        # If no prefix match, use whole key (maybe title is just "Introduction")
        title_lookup[key] = entries
        
    # Also index the full key just in case
    title_lookup[key] = entries

print(f"Built advanced lookup with {len(title_lookup)} titles.")

files = [f for f in os.listdir(legacy_dir) if f.endswith('.md')]
print(f"Scanning {len(files)} legacy files...")

restored_count = 0

for filename in files:
    # Filename format: Volume-001-第1章-Title.md OR 001-第1章-Title.md
    # We want to extract "Title".
    
    # Simple regex for extract after last '-'
    # But some titles have dashes? "临高-广州"
    # The format seems to be: [Prefix-] {POS}-第{NUM}章-{TITLE}.md
    # Let's try to match the "第xx章-" part.
    
    match = re.search(r'第[0-9]+\S?章-(.+)\.md$', filename)
    if not match:
        print(f"Skipping {filename}: no title pattern")
        continue
        
    title_part = match.group(1).strip()
    norm_title = norm(title_part)
    
    entries = title_lookup.get(norm_title)
    if entries:
        # Match!
        # If multiple entries, handle...
        target_entry = entries[0]
        
        # Check volume hint if available
        for e in entries:
            if e['volume_folder'] in filename:
                target_entry = e
                break
        
        tgt_vol = target_entry['volume_folder']
        tgt_pos = target_entry['position']
        tgt_glob = target_entry['global_index']
        
        new_name = f"{tgt_pos:03d}-第{tgt_glob}章-{title_part}.md"
        
        dest_dir = os.path.join(base_dir, tgt_vol)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        dest_path = os.path.join(dest_dir, new_name)
        
        if os.path.exists(dest_path):
            print(f"Duplicate content for {tgt_vol}/{new_name}? Deleting legacy.")
            os.remove(os.path.join(legacy_dir, filename))
        else:
            print(f"Restoring {filename} -> {tgt_vol}/{new_name}")
            shutil.move(os.path.join(legacy_dir, filename), dest_path)
        restored_count += 1
    else:
        # Fallback partial match?
        # Maybe title_part is "忙碌的刘市长" and key is "忙碌的刘市长" -> it should match.
        pass

print(f"Restored {restored_count} files.")
