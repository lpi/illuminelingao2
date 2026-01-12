
import os
import re
from collections import defaultdict

def analyze_chapters(directory):
    files = os.listdir(directory)
    chapter_map = defaultdict(list)
    
    # Regex to match chapter numbers. Assuming format like "1416-Chapter1416-Manila.md" 
    # or just "1416-..." at the start.
    pattern = re.compile(r'^(\d+)-')

    for f in files:
        if not f.endswith('.md'):
            continue
        
        match = pattern.match(f)
        if match:
            chapter_num = int(match.group(1))
            chapter_map[chapter_num].append(f)
        else:
            # Try to handle files that might not start with number but contain it?
            # For now strict compliance to naming convention seen in prompt
            pass

    duplicates = {}
    missing = []
    
    # Check for duplicates and missing
    for i in range(1, 2251):
        if i not in chapter_map:
            missing.append(i)
        elif len(chapter_map[i]) > 1:
            # Sort files by size to help decision making
            file_info = []
            for fname in chapter_map[i]:
                path = os.path.join(directory, fname)
                size = os.path.getsize(path)
                file_info.append({'name': fname, 'size': size})
            duplicates[i] = file_info

    return duplicates, missing

if __name__ == "__main__":
    directory = "/Users/lipi/illuminelingao2/english_chapters"
    duplicates, missing = analyze_chapters(directory)
    
    print("--- DUPLICATES ---")
    for chap, files in duplicates.items():
        print(f"Chapter {chap}:")
        for f in files:
            print(f"  {f['name']} (Size: {f['size']})")
            
    print("\n--- MISSING ---")
    if missing:
        ranges = []
        start = missing[0]
        prev = missing[0]
        for x in missing[1:]:
            if x > prev + 1:
                if start == prev:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}-{prev}")
                start = x
            prev = x
        if start == prev:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}-{prev}")
        print(", ".join(ranges))
    else:
        print("None")
