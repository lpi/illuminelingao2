
import os
import shutil

base_dir = "/Users/lipi/illuminelingao2/chapters"

moves = [
    # (Source Filename, Destination Folder Relative Path, New Filename)
    ("conflicted_392-第392章-家务事.md", "07-conflict/347-第347章-家务事.md"),
    ("conflicted_208-第208章-理想.md", "07-conflict/288-第288章-理想.md"),
    ("conflicted_241-第241章-新的线索.md", "08-guangzhou_governance/385-第385章-新的线索.md"),
    ("conflicted_244-第244章-借题发挥.md", "08-guangzhou_governance/380-第380章-借题发挥.md"),
    ("conflicted_248-第248章-判决.md", "08-guangzhou_governance/239-第239章-判决.md"),
    ("conflicted_374-第374章-少年.md", "08-guangzhou_governance/286-第286章-少年.md"),
]

for src_name, dest_rel_path in moves:
    src_path = os.path.join(base_dir, src_name)
    dest_path = os.path.join(base_dir, dest_rel_path)
    
    if os.path.exists(src_path):
        print(f"Moving {src_name} -> {dest_rel_path}")
        # Ensure dest dir exists (it should)
        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        shutil.move(src_path, dest_path)
    else:
        print(f"Source not found: {src_path}")

print("Done resolving conflicts.")
