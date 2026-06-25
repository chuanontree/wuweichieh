#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

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
    if opt in html:
        html = html.replace(opt, '', 1)
        print('Removed:', opt[:40])
    else:
        print('NOT FOUND:', opt[:40])

html = html.replace(
    "if (theme === 'brutal') { buildBrutal(); initHorizontalScroll(); }\n    else if (theme === 'luxury') { buildLuxury(); ensureLuxOverlay(); }",
    "if (theme === '__removed__') { }"
)
html = html.replace(
    "else if (theme === 'zen') { buildZen(); ensureLuxOverlay(); }\n    else if (theme === 'iso') { buildIso(); ensureLuxOverlay(); }\n    else if (theme === 'multiverse')",
    "else if (theme === 'multiverse')"
)
print('rebuildWorksGrid branches removed.')

guard = "var _del=['brutal','luxury','zen','iso','baroque','bauhaus','popart','newspaper','chinese','medieval','sky','crystal','y2k','circuit','garden'];if(_del.indexOf(theme)!==-1)theme='default';"
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
