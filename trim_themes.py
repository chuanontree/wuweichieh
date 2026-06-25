#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

# ── 1. Remove dropdown options for deleted themes ──────────────────
DELETE_OPTIONS = [
    '<option value="brutal">A · Editorial Brutal</option>',
    '<option value="luxury">B · Liquid Luxury</option>',
    '<option value="zen">E · Zen Focus</option>',
    '<option value="iso">F · Isometric 3D</option>',
    '<option value="baroque">J · Baroque</option>',
    '<option value="bauhaus">K · Bauhaus</option>',
    '<option value="popart">L · Pop Art</option>',
    '<option value="newspaper">M · Newspaper</option>',
    '<option value="chinese">N · 水墨丹青</option>',
    '<option value="medieval">O · 鋼鐵誓約</option>',
    '<option value="sky">P · 天空懸浮</option>',
    '<option value="crystal">Q · 水晶</option>',
    '<option value="y2k">R · Y2K 液態金屬</option>',
    '<option value="circuit">S · 電路板</option>',
    '<option value="garden">T · 花園</option>',
]
for opt in DELETE_OPTIONS:
    html = html.replace(opt, '', 1)
print('Options removed.')

# ── 2. Rename kept options to drop letter prefix ───────────────────
html = html.replace('<option value="void">C · Systemic Void</option>', '<option value="void">C · Systemic Void</option>')
html = html.replace('<option value="canvas">D · Infinite Canvas</option>', '<option value="canvas">D · Infinite Canvas</option>')
html = html.replace('<option value="multiverse">G · Multiverse</option>', '<option value="multiverse">G · Multiverse</option>')
html = html.replace('<option value="apple">H · Apple Editorial</option>', '<option value="apple">H · Apple Editorial</option>')
html = html.replace('<option value="cyber">I · Cyberpunk</option>', '<option value="cyber">I · Cyberpunk</option>')

# ── 3. Remove rebuildWorksGrid branches for deleted themes ─────────
# brutal branch
html = html.replace(
    "if (theme === 'brutal') { buildBrutal(); initHorizontalScroll(); }\n    else if (theme === 'luxury') { buildLuxury(); ensureLuxOverlay(); }",
    "if (theme === 'luxury_removed') { /* removed */ }"
)
# zen and iso branches
html = html.replace(
    "else if (theme === 'zen') { buildZen(); ensureLuxOverlay(); }\n    else if (theme === 'iso') { buildIso(); ensureLuxOverlay(); }\n    else if (theme === 'multiverse')",
    "else if (theme === 'multiverse')"
)
print('rebuildWorksGrid branches removed.')

# ── 4. Guard applyTheme: redirect deleted themes to default ────────
DELETED_THEMES = ['brutal','luxury','zen','iso','baroque','bauhaus','popart','newspaper','chinese','medieval','sky','crystal','y2k','circuit','garden']
guard = (
    "var _deletedThemes=['brutal','luxury','zen','iso','baroque','bauhaus','popart','newspaper','chinese','medieval','sky','crystal','y2k','circuit','garden'];"
    "if(_deletedThemes.indexOf(theme)!==-1)theme='default';"
)
old_apply = "function applyTheme(theme) {\n    document.documentElement.setAttribute('data-theme', theme);"
new_apply = "function applyTheme(theme) {\n    " + guard + "\n    document.documentElement.setAttribute('data-theme', theme);"
if old_apply in html:
    html = html.replace(old_apply, new_apply, 1)
    print('applyTheme guard added.')
else:
    print('WARNING: applyTheme pattern not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: {:+,}'.format(orig, len(html), len(html)-orig))
