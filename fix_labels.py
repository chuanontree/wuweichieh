#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

replacements = [
    ('C · Systemic Void', 'Systemic Void'),
    ('D · Infinite Canvas', 'Infinite Canvas'),
    ('G · Multiverse', 'Multiverse'),
    ('H · Apple Editorial', 'Apple Editorial'),
    ('I · Cyberpunk', 'Cyberpunk'),
]
for old, new in replacements:
    html = html.replace(old, new)
    print(f'{old!r} -> {new!r}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: {:+,}'.format(orig, len(html), len(html)-orig))
