
import os
import json

base_dir = "/Users/lipi/illuminelingao2/chapters"
english_dir = "/Users/lipi/illuminelingao2/english_chapters"

vols = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')])

print(f"{'Volume':<30} | {'Chinese':<7} | {'English':<7} | {'Diff':<4}")
print("-" * 55)

total_diff = 0

for v in vols:
    c_path = os.path.join(base_dir, v)
    e_path = os.path.join(english_dir, v)
    
    c_files = len([f for f in os.listdir(c_path) if f.endswith('.md')])
    
    if os.path.exists(e_path):
        e_files = len([f for f in os.listdir(e_path) if f.endswith('.md')])
    else:
        e_files = 0
        
    diff = c_files - e_files
    print(f"{v:<30} | {c_files:<7} | {e_files:<7} | {diff:<4}")
    total_diff += abs(diff)

print("-" * 55)
print(f"Structure verification complete. Discrepancies found: {total_diff > 0}")

# Move remaining root files and conflicted files to 'surplus'
surplus_dir = os.path.join(base_dir, "000-surplus")
if not os.path.exists(surplus_dir):
    os.makedirs(surplus_dir)

root_files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f)) and not f.startswith('.')]
for f in root_files:
    print(f"Moving surplus file {f} to 000-surplus")
    os.rename(os.path.join(base_dir, f), os.path.join(surplus_dir, f))

