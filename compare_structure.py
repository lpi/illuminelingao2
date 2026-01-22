
import os
import re

base_dir = "/Users/lipi/illuminelingao2"
c_dir = os.path.join(base_dir, "chapters")
e_dir = os.path.join(base_dir, "english_chapters")

def get_indices(path):
    indices = set()
    if not os.path.exists(path): return indices
    for f in os.listdir(path):
        if not f.endswith('.md'): continue
        # Filename format: POS-第GLOBAL章-TITLE.md OR POS-ChapterGLOBAL-TITLE.md
        # Regex to capture GLOBAL index
        match = re.search(r'[-第Chapter](\d+)[章-]', f)
        if match:
            try:
                indices.add(int(match.group(1)))
            except: pass
    return indices

modules = [
    "05-new_australia",
    "06-entering",
    "07-conflict",
    "08-guangzhou_governance"
]

print(f"{'Volume':<25} | {'Missing in English':<20} | {'Extra in English':<20}")
print("-" * 70)

for m in modules:
    c_set = get_indices(os.path.join(c_dir, m))
    e_set = get_indices(os.path.join(e_dir, m))
    
    missing_in_e = sorted(list(c_set - e_set))
    extra_in_e = sorted(list(e_set - c_set))
    
    # Format for display (ranges or truncation if too long)
    def fmt(lst):
        if not lst: return "None"
        if len(lst) > 5:
            return f"{len(lst)} items ({lst[0]}..{lst[-1]})"
        return str(lst)

    print(f"{m:<25} | {fmt(missing_in_e):<20} | {fmt(extra_in_e):<20}")
    
    if len(missing_in_e) > 0 and len(missing_in_e) < 20:
        print(f"  Missing Details: {missing_in_e}")
    if len(extra_in_e) > 0 and len(extra_in_e) < 20:
        print(f"  Extra Details: {extra_in_e}")

