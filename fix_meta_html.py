#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)
count = 0

# 1. In extraction, also store metaHtml (innerHTML preserving <br> and <div>)
old_extract = "meta: wm ? wm.textContent.trim() : '',"
new_extract = "meta: wm ? wm.textContent.trim() : '',\n        metaHtml: wm ? wm.innerHTML : '',"
if old_extract in html:
    html = html.replace(old_extract, new_extract, 1)
    count += 1
    print('Extraction updated.')
else:
    print('WARNING: extraction pattern not found')

# 2. Replace all esc(w.meta) usages in build functions with w.metaHtml (except textContent line)
import re
# Replace in innerHTML-context build functions (all occurrences of esc(w.meta) inside string concatenation)
html_new = html.replace("esc(w.meta)", "w.metaHtml || esc(w.meta)")
replaced = html.count("esc(w.meta)") - html_new.count("esc(w.meta)")
html = html_new
count += replaced
print('Replaced', replaced, 'occurrences of esc(w.meta)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Total changes:', count)
print('Original: {:,} | New: {:,} | Delta: {:+,}'.format(orig, len(html), len(html)-orig))
