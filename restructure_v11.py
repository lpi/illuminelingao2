#!/usr/bin/env python3
"""One-shot restructure: align repo with current 69shuba numbering (site inserted
第2329章 去梧州（四）, shifting everything after it +1) and integrate chapters 2903-2943
as new volume 11-tianjin_wei. Also fixes two long-standing defects:
- chapters/08 256-第2329章-去梧州（四）.md collided with 256-...（五）.md  -> (五)+ shift
- chapters/10 2799-第2799章.md is really 男女之事（二）, missing from position 010
"""
import json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, 'chapters')

site = json.load(open(os.path.join(ROOT, 'chapter_list_current.json')))
old_json = json.load(open(os.path.join(ROOT, 'chapter_list_ordered.json')))

# Real titles for the site's untitled chapters, taken from the old (Qidian-derived) list.
untitled_fix = {}
for e in old_json:
    untitled_fix[e['global_index']] = re.sub(r'^第[零一二三四五六七八九十百千\d]+节\s*', '', e['original_line']).strip()

renames = []   # (old_path, new_path)
moves = []     # (src, dst) across dirs
deletes = []

pat = re.compile(r'^(\d+)-第(\d+)章(-.*)?\.md$')

# --- volume 08: positions/numbers shift +1 from position 256 (except 去梧州（四）which keeps 256/2329)
d = os.path.join(CH, '08-two_guangs_campaign')
for fn in sorted(os.listdir(d)):
    m = pat.match(fn)
    if not m:
        continue  # conflicted_* left untouched
    pos, x, tail = int(m.group(1)), int(m.group(2)), m.group(3) or ''
    if pos < 256:
        continue
    if tail.startswith('-去梧州（四）'):
        continue  # already correct: 256-第2329章
    renames.append((os.path.join(d, fn), os.path.join(d, f'{pos+1:03d}-第{x+1}章{tail}.md')))

# --- volume 09: 第X章 +1, positions unchanged
d = os.path.join(CH, '09-deep_cultivation')
for fn in sorted(os.listdir(d)):
    m = pat.match(fn)
    if not m:
        continue
    pos, x, tail = int(m.group(1)), int(m.group(2)), m.group(3) or ''
    renames.append((os.path.join(d, fn), os.path.join(d, f'{pos:03d}-第{x+1}章{tail}.md')))

# --- volume 10: 第X章 +1, positions unchanged; stray 2799 -> 010-第2799章-男女之事（二）
d = os.path.join(CH, '10-volume_nine')
for fn in sorted(os.listdir(d)):
    if fn == '2799-第2799章.md':
        renames.append((os.path.join(d, fn), os.path.join(d, '010-第2799章-男女之事（二）.md')))
        continue
    m = pat.match(fn)
    if not m:
        continue
    pos, x, tail = int(m.group(1)), int(m.group(2)), m.group(3) or ''
    renames.append((os.path.join(d, fn), os.path.join(d, f'{pos:03d}-第{x+1}章{tail}.md')))

# --- new volume 11: flat 2903..2943 -> chapters/11-tianjin_wei/001..041
newdir = os.path.join(CH, '11-tianjin_wei')
os.makedirs(newdir, exist_ok=True)
for i, c in enumerate(site[2902:2943], start=1):
    x = 2902 + i
    src = os.path.join(CH, f'{x}-{c["title"].replace(" ", "-")}.md')
    dst = os.path.join(newdir, f'{i:03d}-第{x}章-{c["title"].split(" ", 1)[1]}.md')
    moves.append((src, dst))

# --- flat scrape of 2329 was a byte-identical duplicate of the volume-08 file
deletes.append(os.path.join(CH, '2329-第2329章-去梧州（四）.md'))

dry = '--apply' not in sys.argv
for old, new in renames + moves:
    print(('MOVE ' if os.path.dirname(old) != os.path.dirname(new) else 'rename'), os.path.relpath(old, ROOT), '->', os.path.relpath(new, ROOT))
for p in deletes:
    print('DELETE', os.path.relpath(p, ROOT))
if dry:
    print(f'\n{len(renames)} renames, {len(moves)} moves, {len(deletes)} deletes. Re-run with --apply.')
    sys.exit(0)

# apply: two-phase rename via temp names to avoid collisions within a folder
for old, new in renames:
    assert os.path.exists(old), old
    os.rename(old, old + '.tmp-renaming')
for old, new in renames:
    assert not os.path.exists(new), new
    os.rename(old + '.tmp-renaming', new)
for old, new in moves:
    assert os.path.exists(old), old
    shutil.move(old, new)
for p in deletes:
    os.remove(p)
print('Applied.')
