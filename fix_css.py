#!/usr/bin/env python3
"""Fix: bare CSS was injected outside <style> tags. Wrap it properly."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

MARKER = '/* ══ GSAP ANIMATION HELPERS'

if MARKER not in html:
    print('Marker not found — nothing to fix')
    exit(0)

idx = html.index(MARKER)
before = html[:idx]
last_style_open = before.rfind('<style')
last_style_close = before.rfind('</style>')

if last_style_open != -1 and last_style_open > last_style_close:
    print('CSS is already inside a <style> block — nothing to fix')
    exit(0)

# CSS is bare. Find where it ends: first tag-like token after the marker.
after = html[idx:]
import re
# Find first HTML tag that signals end of bare CSS block
m = re.search(r'<(?:script|link|title|meta|\/head)', after)
if not m:
    print('Could not find end of CSS block')
    exit(1)

end_idx = m.start()
bare_css = after[:end_idx].rstrip()
rest = after[end_idx:]

# Build fixed version
fixed = html[:idx] + '<style>\n' + bare_css + '\n</style>\n' + rest

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed)

print(f'Fixed: wrapped {len(bare_css)} chars of CSS in <style> tags')
