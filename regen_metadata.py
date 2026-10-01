#!/usr/bin/env python3
"""Regenerate chapter_list_ordered.json from the current 69shuba chapter list,
using disk volume folders. Extends title_mapping.json with the new chapters."""
import json, re

ROOT = '.'
site = json.load(open('chapter_list_current.json'))
old_json = json.load(open('chapter_list_ordered.json'))

# Real titles for untitled site chapters come from the old Qidian-derived list.
old_by_index = {e['global_index']: e for e in old_json}

def real_title(i, site_title):
    m = re.match(r'^第(\d+)章\s*(.*)$', site_title)
    x, t = int(m.group(1)), m.group(2).strip()
    if not t:
        # untitled on the site: real title from the old list (old index = i-1 after the 2329 insertion)
        old_i = i if i <= 2328 else i - 1
        t = re.sub(r'^第[零一二三四五六七八九十百千\d]+节\s*', '', old_by_index[old_i]['original_line']).strip()
    return x, t

# volume -> (site index start, site index end), derived from disk layout
VOLUMES = [
    ('00-extras-fanworks', 1, 4),
    ('01-setting_sail', 5, 48),
    ('02-new_world', 49, 226),
    ('03-new_society', 227, 561),
    ('04-new_australia', 562, 783),
    ('05-entering', 784, 1226),
    ('06-conflict', 1227, 1669),
    ('07-guangzhou_governance', 1670, 2073),
    ('08-two_guangs_campaign', 2074, 2406),
    ('09-deep_cultivation', 2407, 2789),
    ('10-volume_nine', 2790, 2902),
    ('11-tianjin_wei', 2903, 2943),
]

DIGITS = '零一二三四五六七八九'
def cn_num(n):
    if n <= 0: return str(n)
    if n < 10: return DIGITS[n]
    if n < 20: return '十' + (DIGITS[n % 10] if n % 10 else '')
    if n < 100:
        return DIGITS[n // 10] + '十' + (DIGITS[n % 10] if n % 10 else '')
    if n < 1000:
        b, rest = n // 100, n % 100
        s = DIGITS[b] + '百'
        if rest == 0: return s
        if rest < 10: return s + '零' + DIGITS[rest]
        if rest < 20: return s + '一十' + (DIGITS[rest % 10] if rest % 10 else '')
        return s + DIGITS[rest // 10] + '十' + (DIGITS[rest % 10] if rest % 10 else '')
    return str(n)

entries = []
for folder, lo, hi in VOLUMES:
    for i in range(lo, hi + 1):
        x, title = real_title(i, site[i - 1]['title'])
        pos = i - lo + 1
        original_line = title if folder == '00-extras-fanworks' else f'第{cn_num(pos)}节 {title}'
        assert x == i, (x, i)
        entries.append({'volume_folder': folder, 'position': pos, 'global_index': i, 'original_line': original_line})

assert len(entries) == 2943
json.dump(entries, open('chapter_list_ordered.json', 'w'), ensure_ascii=False, indent=1)

# Extend title_mapping.json: key by bare title and composed "第N节Title" form (existing patterns)
tm = json.load(open('title_mapping.json'))
added = 0
for e in entries:
    if e['global_index'] < 2903:
        continue
    for key in (re.sub(r'^第[零一二三四五六七八九十百千\d]+节\s*', '', e['original_line']).strip(), e['original_line'].replace(' ', '')):
        if key and key not in tm:
            tm[key] = [e]
            added += 1
json.dump(tm, open('title_mapping.json', 'w'), ensure_ascii=False, indent=1)

# Verify against disk
import os
problems = []
for folder, lo, hi in VOLUMES:
    d = os.path.join('chapters', folder)
    files = {}
    for fn in os.listdir(d):
        m = re.match(r'^(\d+)-', fn)
        if m:
            files[int(m.group(1))] = fn
    expected = hi - lo + 1
    gaps = [p for p in range(1, expected + 1) if p not in files]
    if gaps or len(files) > expected:
        problems.append((folder, f'{len(files)} files, positions missing: {gaps[:6]}{"..." if len(gaps) > 6 else ""}'))
print('disk check:', 'OK' if not problems else problems)
print(f'entries={len(entries)}, title_mapping added {added} keys, total {len(tm)}')
