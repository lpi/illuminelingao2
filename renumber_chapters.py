#!/usr/bin/env python3
"""Renumber chapters across all volumes to remove the gap from chapters 1-4."""

import os
import re

SOURCE_DIR = "english_chapters"
CHAPTER_OFFSET = -4  # Subtract 4 from all chapter numbers

def renumber_chapter_in_content(content, offset):
    """Update chapter number in the markdown content (first line header)."""
    lines = content.split('\n')
    if lines and lines[0].startswith('# Chapter '):
        # Match "# Chapter N: Title" or "# Chapter N - Title" 
        match = re.match(r'^# Chapter (\d+)([\s:-]+)(.*)$', lines[0])
        if match:
            old_num = int(match.group(1))
            new_num = old_num + offset
            if new_num > 0:  # Only renumber if result is positive
                separator = match.group(2)
                title = match.group(3)
                lines[0] = f"# Chapter {new_num}{separator}{title}"
                return '\n'.join(lines), old_num, new_num
    return content, None, None

def renumber_filename(filename, offset):
    """Update chapter number in filename."""
    # Match patterns like "001-Chapter5-Title.md" or "001-Chapter123-Title.md"
    match = re.match(r'^(\d+)-Chapter(\d+)-(.+\.md)$', filename)
    if match:
        file_num = match.group(1)
        old_chapter_num = int(match.group(2))
        title = match.group(3)
        new_chapter_num = old_chapter_num + offset
        if new_chapter_num > 0:
            return f"{file_num}-Chapter{new_chapter_num}-{title}", old_chapter_num, new_chapter_num
    return filename, None, None

def main():
    # Process all volume directories except preface and extras
    volumes_to_process = []
    for entry in sorted(os.listdir(SOURCE_DIR)):
        vol_path = os.path.join(SOURCE_DIR, entry)
        if os.path.isdir(vol_path) and entry.startswith(('01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-', '09-', '10-')):
            volumes_to_process.append(entry)
    
    total_renamed = 0
    
    for vol_dir in volumes_to_process:
        vol_path = os.path.join(SOURCE_DIR, vol_dir)
        print(f"\nProcessing {vol_dir}...")
        
        for filename in sorted(os.listdir(vol_path)):
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(vol_path, filename)
            
            # Update content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, old_num, new_num = renumber_chapter_in_content(content, CHAPTER_OFFSET)
            
            if old_num is not None:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            
            # Update filename
            new_filename, _, _ = renumber_filename(filename, CHAPTER_OFFSET)
            
            if new_filename != filename:
                new_filepath = os.path.join(vol_path, new_filename)
                os.rename(filepath, new_filepath)
                print(f"  {filename} -> {new_filename}")
                total_renamed += 1
    
    print(f"\nTotal files renamed: {total_renamed}")

if __name__ == "__main__":
    main()
