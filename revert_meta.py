#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)
count = 0

# Revert: remove metaHtml extraction line
old_extract = "meta: wm ? wm.textContent.trim() : '',\n        metaHtml: wm ? wm.innerHTML : '',"
new_extract = "meta: wm ? wm.textContent.trim() : '',"
if old_extract in html:
    html = html.replace(old_extract, new_extract, 1)
    count += 1
    print('Extraction reverted.')
else:
    print('WARNING: extraction pattern not found')

# Revert: restore esc(w.meta) from w.metaHtml || esc(w.meta)
html_new = html.replace("w.metaHtml || esc(w.meta)", "esc(w.meta)")
replaced = html.count("w.metaHtml || esc(w.meta)") - html_new.count("w.metaHtml || esc(w.meta)")
html = html_new
count += replaced
print('Reverted', replaced, 'occurrences back to esc(w.meta)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Total changes:', count)
print('Original: {:,} | New: {:,} | Delta: {:+,}'.format(orig, len(html), len(html)-orig))
