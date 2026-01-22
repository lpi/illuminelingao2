#!/usr/bin/env python3
"""
Parse raw Qidian chapter list text files and generate title_mapping.json.
Mapping keys point to a LIST of entries to handle duplicate titles.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path("/Users/lipi/illuminelingao2")
INPUT_FILES = [
    BASE_DIR / "chapter_list_raw_part1.txt",
    BASE_DIR / "chapter_list_raw_part2.txt",
    BASE_DIR / "chapter_list_raw_part3.txt",
    BASE_DIR / "chapter_list_raw_part4.txt",
    BASE_DIR / "chapter_list_raw_part5.txt",
    BASE_DIR / "chapter_list_raw_part6.txt",
    BASE_DIR / "chapter_list_raw_part7.txt",
]

# Mapping from Chinese volume header keywords to folder names
VOLUME_MAP = {
    "同人作": "00-extras-fanworks",
    "第一卷": "01-setting_sail",
    "第二卷": "02-new_world",
    "VIP卷": "03-vip",
    "第三卷": "04-new_society",
    "第四卷": "05-new_australia",
    "第五卷": "06-entering",
    "第六卷": "07-conflict",
    "第七卷　大陆-广州治理篇": "08-guangzhou_governance",
    "第七卷　大陆-两广攻略篇": "09-two_guangs_campaign",
    "第八卷": "10-deep_cultivation",
    "第九卷": "11-volume_nine",
}

def normalize_title(title):
    """Normalize a title for matching."""
    # Remove all dash-like characters and spaces
    title = re.sub(r'[ \-－—_]', '', title)
    title = title.replace("(", "").replace(")", "").replace("（", "").replace("）", "")
    title = title.replace(".", "")
    title = re.sub(r'（修改）$', '', title)
    title = re.sub(r'(大改)$', '', title)
    title = re.sub(r'\(二更\)$', '', title)
    title = re.sub(r'（本日第二更）$', '', title)
    return title.lower()

def parse_files():
    content = ""
    for file_path in INPUT_FILES:
        if file_path.exists():
            content += file_path.read_text(encoding='utf-8') + "\n"
    
    lines = content.splitlines()
    
    mapping = {}
    ordered_list = [] 
    
    current_volume = None
    if "同人作" in lines[0]:  # Special case for start
        current_volume = "00-extras-fanworks"
        
    volume_chapter_count = 0
    global_chapter_count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for volume headers
        is_volume_header = False
        
        # Specific checks for volume 7 split
        if "第七卷" in line and "广州治理篇" in line:
            current_volume = "08-guangzhou_governance"
            volume_chapter_count = 0
            is_volume_header = True
        elif "第七卷" in line and "两广攻略篇" in line:
            current_volume = "09-two_guangs_campaign"
            volume_chapter_count = 0
            is_volume_header = True
        else:
            # General checks
            for key, folder in VOLUME_MAP.items():
                if key in line and "第七卷" not in key: 
                     if line.startswith(key) or (key in line and "·共" in line):
                         current_volume = folder
                         volume_chapter_count = 0
                         is_volume_header = True
                         break
        
        if is_volume_header:
            print(f"Found volume: {current_volume} in line: {line}")
            continue
            
        # Process chapter
        if "订阅本卷" in line or "作品相关" in line:
            continue
        
        volume_chapter_count += 1
        global_chapter_count += 1
        
        norm_full = normalize_title(line)
        
        match = re.match(r'^第[0-9零一二三四五六七八九十百千]+[节章]\s*(.*)$', line)
        pure_title = match.group(1) if match else line
        norm_pure = normalize_title(pure_title)
        
        entry = {
            "volume_folder": current_volume,
            "position": volume_chapter_count,
            "global_index": global_chapter_count,
            "original_line": line
        }
        
        ordered_list.append(entry)
        
        # Key by Normalized Title
        # APPEND to list
        if norm_full not in mapping:
            mapping[norm_full] = []
        mapping[norm_full].append(entry)
        
        if norm_pure != norm_full:
            if norm_pure not in mapping:
                mapping[norm_pure] = []
            mapping[norm_pure].append(entry)

    return mapping, ordered_list

if __name__ == "__main__":
    mapping, ordered_list = parse_files()
    
    output_path = BASE_DIR / "title_mapping.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    
    list_path = BASE_DIR / "chapter_list_ordered.json"
    with open(list_path, "w", encoding="utf-8") as f:
        json.dump(ordered_list, f, ensure_ascii=False, indent=2)
        
    print(f"Generated:")
    print(f"- Mapping: {len(mapping)} keys at {output_path}")
    print(f"- Ordered List: {len(ordered_list)} entries at {list_path}")
