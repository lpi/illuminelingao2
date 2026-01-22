#!/usr/bin/env python3
"""
Restore and organize English chapters based on internal content header.
Extracts '# Chapter N' from file content to determine Global Index.
Maps Global Index to Volume and Relative Index using chapter_list_ordered.json.
Renames and moves files to correct volume folders.
"""

import os
import shutil
import re
import json
from pathlib import Path

BASE_DIR = Path("/Users/lipi/illuminelingao2")
ENGLISH_DIR = BASE_DIR / "english_chapters"
ORDERED_LIST_FILE = BASE_DIR / "chapter_list_ordered.json"
UNRESOLVED_DIR = ENGLISH_DIR / "unresolved"

def load_ordered_list():
    if not ORDERED_LIST_FILE.exists():
        print(f"Error: {ORDERED_LIST_FILE} not found.")
        exit(1)
    with open(ORDERED_LIST_FILE, 'r') as f:
        return json.load(f)

def get_global_index_from_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Check first 5 lines
            for _ in range(5):
                line = f.readline()
                if not line:
                    break
                # Match "# Chapter 457" or "# Chapter 457:" or "# Chapter 457 -"
                match = re.match(r'^#\s*Chapter\s*(\d+)', line, re.IGNORECASE)
                if match:
                    return int(match.group(1))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def extract_title_part(filename):
    # Filename format: 001-Chapter1-Title.md OR conflicted_...
    # Remove prefix digits and "ChapterX-"
    # Pattern: ...-Chapter\d+-(.+)\.md
    
    # First remove "conflicted_" if present
    name = filename
    if name.startswith("conflicted_"):
        name = name[11:]
        
    match = re.search(r'-Chapter\d+-(.+)\.md$', name)
    if match:
        return match.group(1)
        
    # Fallback: maybe just digits-Title.md?
    match = re.search(r'^\d+-(.+)\.md$', name)
    if match:
        return match.group(1)
        
    # Last resort: text before .md
    return Path(name).stem

def main():
    ordered_list = load_ordered_list()
    
    # Flatten/Walk logic: We look at ALL files in english_chapters recursively
    files_to_process = []
    for root, dirs, files in os.walk(ENGLISH_DIR):
        for file in files:
            if file.endswith(".md"):
                files_to_process.append(Path(root) / file)
    
    print(f"Found {len(files_to_process)} English chapter files.")
    
    if not UNRESOLVED_DIR.exists():
        UNRESOLVED_DIR.mkdir()

    stats = {"moved": 0, "unresolved": 0, "total": 0}
    
    for file_path in files_to_process:
        stats["total"] += 1
        global_idx = get_global_index_from_content(file_path)
        
        if global_idx is not None:
            # Validate index
            # ordered_list is 0-based. Global Index 1 -> ordered_list[0].
            list_idx = global_idx - 1
            if 0 <= list_idx < len(ordered_list):
                info = ordered_list[list_idx]
                vol_folder = info['volume_folder']
                vol_pos = info['position']
                
                # Extract title part from filename (preserving original English title)
                title_part = extract_title_part(file_path.name)
                
                # Construct new name
                # Format: [VolPos]-Chapter[GlobalIndex]-[Title].md
                # Example: 050-Chapter457-Autumn_Levy_Part_8.md
                new_name = f"{vol_pos:03d}-Chapter{global_idx}-{title_part}.md"
                
                dest_dir = ENGLISH_DIR / vol_folder
                if not dest_dir.exists():
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    
                dest_path = dest_dir / new_name
                
                # Move
                if file_path != dest_path:
                    if dest_path.exists():
                         # If target exists, verify content? checking size?
                         # Assume identical or overwrite?
                         # Safe skip + log
                         # print(f"Target exists, skipping: {dest_path}")
                        pass # Don't overwrite, maybe it's the same file processed twice?
                    else:
                        shutil.move(str(file_path), str(dest_path))
                        stats["moved"] += 1
            else:
                print(f"Global Index {global_idx} out of range for {file_path.name}")
                shutil.move(str(file_path), str(UNRESOLVED_DIR / file_path.name))
                stats["unresolved"] += 1
        else:
            # print(f"No Chapter ID found in {file_path.name}")
            # Move to unresolved ONLY if it's not already in a volume folder?
            # Actually, just move to unresolved to be safe, so we can manual check.
            # But avoid moving if it's already in 'unresolved'.
            if file_path.parent != UNRESOLVED_DIR:
                dest = UNRESOLVED_DIR / file_path.name
                if dest.exists():
                    dest = UNRESOLVED_DIR / f"duplicate_{file_path.name}"
                shutil.move(str(file_path), str(dest))
                stats["unresolved"] += 1

    print(f"Processing complete.")
    print(f"Total: {stats['total']}")
    print(f"Moved: {stats['moved']}")
    print(f"Unresolved: {stats['unresolved']}")

if __name__ == "__main__":
    main()
