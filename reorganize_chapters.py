#!/usr/bin/env python3
"""
Reorganize Lingao Qiming chapters into volume folders.
Uses title-based mapping from title_mapping.json for Chinese.
Uses Global Index mapping from chapter_list_ordered.json for English (as best effort).
Handles duplicate titles by closest distance to chapter number.
"""

import os
import shutil
import re
import json
from pathlib import Path

# Base paths
BASE_DIR = Path("/Users/lipi/illuminelingao2")
CHINESE_DIR = BASE_DIR / "chapters"
ENGLISH_DIR = BASE_DIR / "english_chapters"
MAPPING_FILE = BASE_DIR / "title_mapping.json"
ORDERED_LIST_FILE = BASE_DIR / "chapter_list_ordered.json"

def normalize_title(title):
    """Normalize a title for matching - MUST match parse_qidian_chapters.py logic"""
    # Remove all dash-like characters and spaces
    title = re.sub(r'[ \-－—_]', '', title)
    title = title.replace("(", "").replace(")", "").replace("（", "").replace("）", "")
    title = title.replace(".", "")
    title = re.sub(r'（修改）$', '', title)
    title = re.sub(r'(大改)$', '', title)
    title = re.sub(r'\(二更\)$', '', title)
    title = re.sub(r'（本日第二更）$', '', title)
    return title.lower()

def load_mapping():
    data = {}
    if MAPPING_FILE.exists():
        with open(MAPPING_FILE, "r", encoding="utf-8") as f:
            data['title_map'] = json.load(f)
    else:
        print(f"Error: Mapping file not found at {MAPPING_FILE}")
        exit(1)
        
    if ORDERED_LIST_FILE.exists():
        with open(ORDERED_LIST_FILE, "r", encoding="utf-8") as f:
            data['ordered_list'] = json.load(f)
    else:
        print(f"Error: Ordered list file not found at {ORDERED_LIST_FILE}")
        exit(1)
            
    return data

def get_best_match(entries, current_num):
    """
    Given a list of mapping entries and the current file number,
    return the entry whose global_index is closest to current_num.
    """
    if not entries:
        return None
    if len(entries) == 1:
        return entries[0]
        
    # Find closest global index
    # We use global_index from entry.
    # We assume current_num approximates the global index.
    
    best_entry = None
    min_dist = float('inf')
    
    for entry in entries:
        dist = abs(entry['global_index'] - current_num)
        if dist < min_dist:
            min_dist = dist
            best_entry = entry
            
    return best_entry

def get_file_info_chinese(filename, mapping_data):
    """
    Get volume info for Chinese file.
    """
    title = None
    chapter_num = None
    
    # Extract Title and Number
    match = re.match(r'^(\d+)-第(\d+)章-(.+)\.md$', filename)
    if match:
        chapter_num = int(match.group(1))
        title = match.group(3)
    else:
        # Try simplified: 001-Title.md
        match = re.match(r'^(\d+)-(.+)\.md$', filename)
        if match:
            chapter_num = int(match.group(1))
            part = match.group(2)
            # Check for inner '第x章'
            submatch = re.match(r'^第\d+章-(.+)$', part)
            if submatch:
                title = submatch.group(1)
            else:
                title = part

    # Strategy 1: Title Match
    if title:
        norm_title = normalize_title(title)
        if norm_title in mapping_data['title_map']:
            entries = mapping_data['title_map'][norm_title]
            # Resolve ambiguity if list has > 1 item
            if chapter_num is not None:
                best_entry = get_best_match(entries, chapter_num)
                return best_entry, "title_match"
            else:
                return entries[0], "title_match_guess"
            
    # Strategy 2: Global Index Match (Fallback)
    if chapter_num is not None:
        ordered_list = mapping_data['ordered_list']
        if 1 <= chapter_num <= len(ordered_list):
            return ordered_list[chapter_num - 1], "index_fallback"
            
    return None, "failed"

def get_file_info_english(filename, mapping_data):
    """
    Get volume info for English file.
    """
    match = re.match(r'^(\d+)-Chapter', filename)
    if match:
        chapter_num = int(match.group(1))
        ordered_list = mapping_data['ordered_list']
        if 1 <= chapter_num <= len(ordered_list):
            return ordered_list[chapter_num - 1], "index_match"
            
    return None, "failed"

def process_directory(src_dir, mapping_data, get_info_func, is_english=False, dry_run=False):
    """Process all chapters in a directory"""
    if not src_dir.exists():
        print(f"Directory not found: {src_dir}")
        return
    
    # Create output folders
    if not dry_run:
        folders = set(item['volume_folder'] for item in mapping_data['ordered_list'])
        for folder in folders:
            if folder: (src_dir / folder).mkdir(exist_ok=True)

    files = sorted([f for f in src_dir.iterdir() if f.is_file() and f.suffix == '.md'])
    
    stats = {"moved": 0, "skipped": 0, "title_match": 0, "index_match": 0, "index_fallback": 0}
    
    for file_path in files:
        filename = file_path.name
        info, method = get_info_func(filename, mapping_data)
        
        if not info or not info.get('volume_folder'):
            # print(f"Skipping (no match): {filename}")
            stats["skipped"] += 1
            continue
            
        stats[method] = stats.get(method, 0) + 1
        
        vol_folder = info['volume_folder']
        vol_pos = info['position']
        
        # New name construction
        new_name = transform_filename(filename, vol_pos, is_english)
        
        new_path = src_dir / vol_folder / new_name
        
        if dry_run:
            print(f"[Dry Run] {filename} -> {vol_folder}/{new_name} ({method})")
        else:
            if new_path.exists():
                 # Overwrite safely if collision? No, skipping matches better
                 # print(f"Warning: Target exists {new_path}, skipping.")
                 pass
            else:
                 shutil.move(str(file_path), str(new_path))
            
        stats["moved"] += 1
        
    print(f"\nSummary for {src_dir.name}:")
    print(f"  Total processed: {len(files)}")
    print(f"  Moved: {stats['moved']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Methods: {stats}")

def transform_filename(old_name, new_chapter_num, is_english):
    """
    Renumber the file.
    """
    if is_english:
        match = re.match(r'^\d+-Chapter\d+-(.+)$', old_name)
        if match:
            title_part = match.group(1)
            return f"{new_chapter_num:03d}-Chapter{new_chapter_num}-{title_part}"
    else:
        match = re.match(r'^\d+-第\d+章-(.+)$', old_name)
        if match:
            title_part = match.group(1)
            return f"{new_chapter_num:03d}-第{new_chapter_num}章-{title_part}"
            
    return old_name 

def main():
    import sys
    dry_run = "--dry-run" in sys.argv
    
    if dry_run:
        print("=== DRY RUN MODE ===")
    
    mapping_data = load_mapping()
    
    print("\nProcessing Chinese chapters...")
    process_directory(CHINESE_DIR, mapping_data, get_file_info_chinese, is_english=False, dry_run=dry_run)
    
    print("\nProcessing English chapters...")
    process_directory(ENGLISH_DIR, mapping_data, get_file_info_english, is_english=True, dry_run=dry_run)

if __name__ == "__main__":
    main()
