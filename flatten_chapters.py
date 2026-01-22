#!/usr/bin/env python3
"""
Flatten chapter directories back to root.
Moves files from subdirectories of chapters/ and english_chapters/ back to the root level.
"""

import shutil
from pathlib import Path

BASE_DIR = Path("/Users/lipi/illuminelingao2")
DIRS = [BASE_DIR / "chapters", BASE_DIR / "english_chapters"]

def flatten_dir(target_dir):
    if not target_dir.exists():
        return
        
    print(f"Flattening {target_dir}...")
    moved = 0
    
    # Iterate over all items
    for item in target_dir.iterdir():
        if item.is_dir():
            # Move files from subdir to root
            for subfile in item.iterdir():
                if subfile.is_file() and subfile.suffix == '.md':
                    dest = target_dir / subfile.name
                    if dest.exists():
                        print(f"Warning: Collision for {subfile.name}. Renaming...")
                        dest = target_dir / f"conflicted_{subfile.name}"
                    
                    shutil.move(str(subfile), str(dest))
                    moved += 1
            
            # Remove empty subdir
            try:
                item.rmdir()
                print(f"Removed empty dir: {item.name}")
            except OSError:
                print(f"Dir not empty, keeping: {item.name}")
                
    print(f"Moved {moved} files to root.")

def main():
    for d in DIRS:
        flatten_dir(d)

if __name__ == "__main__":
    main()
