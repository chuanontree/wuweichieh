import io
html = io.open('index.html', encoding='utf-8').read()
css = io.open('_theme_patch/themes_css.txt', encoding='utf-8').read()
js = io.open('_theme_patch/themes_js.txt', encoding='utf-8').read()

anchor = "[data-theme=\"void\"] footer::after { content:' // CONNECTION TERMINATED _'; color:var(--fg); }\n</style>"
assert html.count(anchor) == 1
html = html.replace(anchor, anchor.replace("\n</style>", "\n" + css + "\n</style>"))

ja = "  // ════ DEFAULT restore ═══════════════════════════════════════════════════"
assert html.count(ja) == 1
html = html.replace(ja, js + ja)

old = """    teardownHorizontalScroll();
    if (theme === 'brutal') { buildBrutal(); initHorizontalScroll(); }
    else if (theme === 'luxury') { buildLuxury(); ensureLuxOverlay(); }
    else if (theme === 'void') { buildVoid(); }
    else buildDefault();"""
assert html.count(old) == 1
new = """    teardownHorizontalScroll();
    teardownThemeFx();
    if (theme === 'brutal') { buildBrutal(); initHorizontalScroll(); }
    else if (theme === 'luxury') { buildLuxury(); ensureLuxOverlay(); }
    else if (theme === 'void') { buildVoid(); }
    else if (theme === 'canvas') { buildCanvas(); ensureLuxOverlay(); }
    else if (theme === 'zen') { buildZen(); ensureLuxOverlay(); }
    else if (theme === 'iso') { buildIso(); ensureLuxOverlay(); }
    else if (theme === 'multiverse') { buildMultiverse(); ensureLuxOverlay(); }
    else if (theme === 'apple') { buildApple(); ensureLuxOverlay(); }
    else if (theme === 'cyber') { buildCyber(); ensureLuxOverlay(); }
    else buildDefault();"""
html = html.replace(old, new)

old = """      document.querySelectorAll('#grid > .wi').forEach(function(el) {
        if (el.style.display === 'block') el.style.display = '';
      });
    };"""
assert html.count(old) == 1
new = """      document.querySelectorAll('#grid > .wi').forEach(function(el) {
        if (el.style.display === 'block') el.style.display = '';
      });
      if (themeFilter) themeFilter(cat);
    };"""
html = html.replace(old, new)

sw_old = """      <button class="ts-btn" data-theme="void" title="Systemic Void">C</button>
    </div>"""
assert html.count(sw_old) == 1
sw_new = """      <button class="ts-btn" data-theme="void" title="Systemic Void">C</button>
      <button class="ts-btn" data-theme="canvas" title="Infinite Canvas">D</button>
      <button class="ts-btn" data-theme="zen" title="Zen Single Focus">E</button>
      <button class="ts-btn" data-theme="iso" title="Isometric 3D">F</button>
      <button class="ts-btn" data-theme="multiverse" title="Multiverse">G</button>
      <button class="ts-btn" data-theme="apple" title="Apple Editorial">H</button>
      <button class="ts-btn" data-theme="cyber" title="Cyberpunk Capsule">I</button>
    </div>"""
html = html.replace(sw_old, sw_new)

f_old = """<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>"""
assert html.count(f_old) == 1
f_new = """<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Rajdhani:wght@400;500;600&family=Syncopate:wght@400;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>"""
html = html.replace(f_old, f_new)

io.open('index.html', 'w', encoding='utf-8', newline='').write(html)
print('SPLICE OK')
