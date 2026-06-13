#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)
changes = []

# ══════════════════════════════════════════════════════
# STEP 1: GSAP scripts before </head>
# ══════════════════════════════════════════════════════
gsap_scripts = """<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/Draggable.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/MotionPathPlugin.min.js"></script>
</head>"""

if 'gsap.min.js' not in html:
    html = html.replace('</head>', gsap_scripts, 1)
    changes.append('STEP 1: GSAP scripts added before </head>')
else:
    changes.append('STEP 1: GSAP scripts already present, skipped')

# ══════════════════════════════════════════════════════
# STEP 2: SVG Morph Transition Overlay after <body>
# ══════════════════════════════════════════════════════
svg_overlay = """<body>
<svg id="themeTransitionOverlay" style="position:fixed;inset:0;width:100%;height:100%;z-index:10000;pointer-events:none;visibility:hidden" aria-hidden="true">
  <circle id="morphCircle" cx="50%" cy="50%" r="0" fill="currentColor"/>
</svg>"""

if 'themeTransitionOverlay' not in html:
    html = html.replace('<body>', svg_overlay, 1)
    changes.append('STEP 2: SVG overlay added after <body>')
else:
    changes.append('STEP 2: SVG overlay already present, skipped')

# ══════════════════════════════════════════════════════
# STEP 3: Update Theme Switcher
# ══════════════════════════════════════════════════════
idx = html.find('id="themeSwitch">')
if idx != -1:
    end_idx = html.find('</div>', idx)
    old_switcher = html[idx:end_idx + 6]
    new_switcher = """id="themeSwitch">
  <button class="ts-btn active" data-theme="default" title="Original">&#9689;</button>
  <button class="ts-btn" data-theme="brutal" title="A · Editorial Brutal">A</button>
  <button class="ts-btn" data-theme="luxury" title="B · Liquid Luxury">B</button>
  <button class="ts-btn" data-theme="void" title="C · Systemic Void">C</button>
  <button class="ts-btn" data-theme="canvas" title="D · Infinite Canvas">D</button>
  <button class="ts-btn" data-theme="zen" title="E · Zen Focus">E</button>
  <button class="ts-btn" data-theme="iso" title="F · Isometric 3D">F</button>
  <button class="ts-btn" data-theme="multiverse" title="G · Multiverse">G</button>
  <button class="ts-btn" data-theme="apple" title="H · Apple Editorial">H</button>
  <button class="ts-btn" data-theme="cyber" title="I · Cyberpunk">I</button>
  <button class="ts-btn" data-theme="baroque" title="J · Baroque">J</button>
  <button class="ts-btn" data-theme="bauhaus" title="K · Bauhaus">K</button>
  <button class="ts-btn" data-theme="popart" title="L · Pop Art">L</button>
  <button class="ts-btn" data-theme="newspaper" title="M · Newspaper">M</button>
  <button class="ts-btn" data-theme="chinese" title="N · 水墨丹青">N</button>
  <button class="ts-btn" data-theme="medieval" title="O · 鋼鐵誓約">O</button>
</div>"""
    html = html.replace(old_switcher, new_switcher, 1)
    changes.append('STEP 3: Theme switcher updated with N and O buttons')
else:
    changes.append('STEP 3: ERROR - themeSwitch not found!')

# STEP 3b: Add/update #themeSwitch CSS
themeswitchcss = """#themeSwitch{display:flex;align-items:center;gap:2px;overflow-x:auto;max-width:380px;scrollbar-width:none;-ms-overflow-style:none}
#themeSwitch::-webkit-scrollbar{display:none}"""
if 'overflow-x:auto;max-width:380px' not in html:
    ts_css_idx = html.find('#themeSwitch{')
    if ts_css_idx == -1:
        ts_css_idx = html.find('#themeSwitch {')
    if ts_css_idx != -1:
        ts_css_end = html.find('}', ts_css_idx) + 1
        old_ts_css = html[ts_css_idx:ts_css_end]
        html = html.replace(old_ts_css, themeswitchcss, 1)
        changes.append('STEP 3b: #themeSwitch CSS updated')
    else:
        html = html.replace('</style>', themeswitchcss + '\n</style>', 1)
        changes.append('STEP 3b: #themeSwitch CSS appended before </style>')

# ══════════════════════════════════════════════════════
# STEP 4: Replace Google Fonts link
# ══════════════════════════════════════════════════════
new_fonts = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cinzel+Decorative:wght@400;700&family=DM+Sans:wght@400;700&family=Bangers&family=Source+Serif+4:ital,wght@0,400;1,400&family=Noto+Serif+TC:wght@300;400;700&family=UnifrakturMaguntia&family=IM+Fell+English:ital&family=Rajdhani:wght@400;600&family=Syncopate:wght@400;700&family=Orbitron:wght@400;700;900&family=Caveat:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">'
if 'Noto+Serif+TC' not in html:
    fonts_idx = html.find('<link rel="preconnect" href="https://fonts.googleapis.com">')
    if fonts_idx != -1:
        fonts_end = html.find('>', html.find('<link href="https://fonts.googleapis.com', fonts_idx)) + 1
        old_fonts_block = html[fonts_idx:fonts_end]
        html = html.replace(old_fonts_block, new_fonts, 1)
        changes.append('STEP 4: Google Fonts replaced with comprehensive version')
    else:
        changes.append('STEP 4: ERROR - fonts link not found')
else:
    changes.append('STEP 4: Fonts already comprehensive, skipped')

# ══════════════════════════════════════════════════════
# STEP 5: Large CSS block before </style>
# ══════════════════════════════════════════════════════
css_block = """
/* ══ GSAP ANIMATION HELPERS ════════════════════════════ */
.gsap-hidden{opacity:0}
#themeTransitionOverlay circle{transition:none}

/* ══ THEME N · 水墨丹青 · CHINESE INK ═══════════════════ */
[data-theme="chinese"]{--bg:#F7F3EA;--fg:#1A1209;--metal:#8C6A3C;--accent:#C0392B;--line:rgba(26,18,9,.15);--dim:rgba(26,18,9,.06);font-family:'Noto Serif TC','Cormorant Garamond',serif}
[data-theme="chinese"] header{background:rgba(247,243,234,.96);border-bottom:none;box-shadow:0 1px 0 rgba(26,18,9,.12),0 2px 0 rgba(26,18,9,.06)}
[data-theme="chinese"] .logo{font-family:'Noto Serif TC',serif;font-weight:700;color:#1A1209;letter-spacing:.15em}
[data-theme="chinese"] .logo::before{content:'印';display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:#C0392B;color:#fff;font-size:.7rem;font-family:'Noto Serif TC',serif;margin-right:.6rem}
[data-theme="chinese"] .ni{color:#8C6A3C;border-left:none;border-right:1px solid rgba(26,18,9,.1);font-family:'Noto Serif TC',serif;font-size:.58rem;letter-spacing:.12em}
[data-theme="chinese"] .ni:hover,[data-theme="chinese"] .ni.on{color:#C0392B;background:rgba(192,57,43,.06)}
[data-theme="chinese"] #hero{background:#F7F3EA;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding-top:52px;min-height:100vh}
[data-theme="chinese"] .hero-bg img{opacity:.08;filter:sepia(30%) contrast(1.1)}
[data-theme="chinese"] .hc{padding:4rem;position:relative;z-index:2;writing-mode:horizontal-tb;max-width:none}
[data-theme="chinese"] .hn{font-family:'Noto Serif TC',serif;font-weight:700;font-size:clamp(3rem,8vw,6rem);color:#1A1209;writing-mode:vertical-rl;text-orientation:mixed;letter-spacing:.1em;height:60vh;display:flex;align-items:flex-start}
[data-theme="chinese"] .hn .ol{-webkit-text-stroke:1px #8C6A3C;color:transparent;writing-mode:vertical-rl;font-family:'Cormorant Garamond',serif;font-size:.5em;margin-left:1.5rem}
[data-theme="chinese"] .he{color:#C0392B;font-family:'Noto Serif TC',serif}
[data-theme="chinese"] .he::before{background:#C0392B}
[data-theme="chinese"] .htag{font-family:'Noto Serif TC',serif;font-size:.8rem;line-height:2.2;color:#8C6A3C}
#chineseModel3D{position:absolute;right:5vw;top:50%;transform:translateY(-50%);width:280px;height:280px;z-index:3;pointer-events:none;display:none}
[data-theme="chinese"] #chineseModel3D{display:block}
[data-theme="chinese"] #pg-works{background:#F7F3EA}
[data-theme="chinese"] #catBar{padding:1rem 2rem;display:flex;gap:0;border-bottom:1px solid rgba(26,18,9,.12)}
[data-theme="chinese"] .ct{font-family:'Noto Serif TC',serif;font-size:.62rem;color:#8C6A3C;background:none;border:none;padding:.4rem 1.2rem;border-right:1px solid rgba(26,18,9,.1);cursor:pointer;transition:color .2s}
[data-theme="chinese"] .ct:hover,[data-theme="chinese"] .ct.on{color:#C0392B}
[data-theme="chinese"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:2px;padding:2px;background:rgba(26,18,9,.08)}
[data-theme="chinese"] .wi{background:#F7F3EA;position:relative;overflow:hidden;border:none;aspect-ratio:3/4}
[data-theme="chinese"] .wi img{width:100%;height:100%;object-fit:cover;filter:sepia(15%) contrast(1.05);transition:filter .6s,transform .8s}
[data-theme="chinese"] .wi:hover img{filter:sepia(30%) contrast(1.1);transform:scale(1.04)}
[data-theme="chinese"] .wio{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(to top,rgba(247,243,234,.97),transparent);padding:1.5rem 1rem .8rem;transform:translateY(60%);transition:transform .5s cubic-bezier(.22,.61,.36,1)}
[data-theme="chinese"] .wi:hover .wio{transform:translateY(0)}
[data-theme="chinese"] .wt{font-family:'Noto Serif TC',serif;font-size:1rem;color:#1A1209;font-weight:700;margin-bottom:.3rem}
[data-theme="chinese"] .wm{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.8rem;color:#8C6A3C}
[data-theme="chinese"] .wi::after{content:'藝';position:absolute;top:1rem;right:1rem;width:36px;height:36px;background:#C0392B;color:#fff;font-family:'Noto Serif TC',serif;font-size:1.1rem;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(0) rotate(15deg);transition:opacity .3s,transform .4s cubic-bezier(.34,1.56,.64,1)}
[data-theme="chinese"] .wi:hover::after{opacity:1;transform:scale(1) rotate(0deg)}
[data-theme="chinese"] #pg-about{background:#F7F3EA}
[data-theme="chinese"] #about{max-width:900px;margin:0 auto;padding:4rem 2rem;display:grid;grid-template-columns:1fr 2fr;gap:4rem;align-items:start}
[data-theme="chinese"] .al2 img{border-radius:50%;border:4px solid #B8860B;box-shadow:0 0 0 8px #F7F3EA,0 0 0 10px #B8860B,0 0 30px rgba(184,134,11,.3)}
[data-theme="chinese"] .sh{font-family:'Noto Serif TC',serif;font-weight:700;font-size:1.1rem;color:#C0392B;letter-spacing:.18em;border-bottom:2px solid rgba(192,57,43,.2);padding-bottom:.6rem;margin-bottom:1.5rem}
[data-theme="chinese"] #pg-cv{background:#F7F3EA}
[data-theme="chinese"] .eyr{display:grid;grid-template-columns:80px 1fr;border-left:2px solid #C0392B;margin-bottom:2rem;padding-left:1.5rem}
[data-theme="chinese"] .yl{font-family:'Noto Serif TC',serif;font-weight:700;font-size:1.1rem;color:#C0392B;writing-mode:vertical-rl}
[data-theme="chinese"] .en{font-family:'Noto Serif TC',serif;color:#1A1209;font-size:.9rem}
[data-theme="chinese"] .et{font-family:'Cormorant Garamond',serif;font-style:italic;color:#8C6A3C;font-size:.8rem}
[data-theme="chinese"] #pg-gallery{background:#F7F3EA}
[data-theme="chinese"] #galleryHint{background:rgba(247,243,234,.95);border:1px solid rgba(26,18,9,.15);box-shadow:0 4px 40px rgba(26,18,9,.1)}
[data-theme="chinese"] #galleryHint h2{font-family:'Noto Serif TC',serif;color:#C0392B;letter-spacing:.2em}
[data-theme="chinese"] #galleryHint button{background:#C0392B;color:#fff;border:none;font-family:'Noto Serif TC',serif;letter-spacing:.12em}
[data-theme="chinese"] footer{background:#1A1209;color:#F7F3EA;border-top:3px solid #C0392B;font-family:'Noto Serif TC',serif;letter-spacing:.12em}
[data-theme="chinese"] footer a{color:#B8860B}

/* ══ THEME O · 鋼鐵誓約 · MEDIEVAL IRON ═══════════════ */
[data-theme="medieval"]{--bg:#0D0D0D;--fg:#C0C0C0;--metal:#8C6A3C;--accent:#8B0000;--line:rgba(192,192,192,.12);--dim:rgba(192,192,192,.06);font-family:'IM Fell English',serif}
[data-theme="medieval"] body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(circle at 0 0,rgba(140,106,60,.15) 2px,transparent 2px),radial-gradient(circle at 8px 8px,rgba(140,106,60,.1) 2px,transparent 2px);background-size:16px 16px;opacity:.4}
[data-theme="medieval"] header{background:rgba(13,13,13,.98);border-bottom:2px solid #8C6A3C;box-shadow:0 2px 20px rgba(139,0,0,.3)}
[data-theme="medieval"] .logo{font-family:'UnifrakturMaguntia',cursive;font-size:.9rem;color:#C0C0C0;letter-spacing:.05em}
[data-theme="medieval"] .ni{font-family:'IM Fell English',serif;color:#8C6A3C;border-left:1px solid rgba(192,192,192,.12)}
[data-theme="medieval"] .ni:hover,[data-theme="medieval"] .ni.on{color:#C0C0C0;background:rgba(139,0,0,.2)}
[data-theme="medieval"] #hero{background:#0D0D0D;position:relative;overflow:hidden}
[data-theme="medieval"] .hero-bg img{opacity:.15;filter:grayscale(80%) contrast(1.3)}
[data-theme="medieval"] .hn{font-family:'UnifrakturMaguntia',cursive;font-size:clamp(2.5rem,7vw,6rem);color:#C0C0C0;text-shadow:0 0 30px rgba(139,0,0,.6),2px 2px 0 rgba(0,0,0,.8)}
[data-theme="medieval"] .hn .ol{font-family:'UnifrakturMaguntia',cursive;-webkit-text-stroke:1px #8C6A3C;color:transparent}
[data-theme="medieval"] .he{color:#8C6A3C}
[data-theme="medieval"] .htag{font-family:'IM Fell English',serif;font-style:italic;color:#8C6A3C}
[data-theme="medieval"] #hero::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:400px;height:400px;background:radial-gradient(ellipse,rgba(139,0,0,.08),transparent 70%);pointer-events:none;z-index:1}
#medievalModel3D{position:absolute;right:8vw;top:50%;transform:translateY(-50%);width:260px;height:260px;z-index:3;pointer-events:none;display:none}
[data-theme="medieval"] #medievalModel3D{display:block}
[data-theme="medieval"] #pg-works{background:#0D0D0D}
[data-theme="medieval"] #catBar{background:rgba(140,106,60,.1);border-bottom:1px solid rgba(140,106,60,.3)}
[data-theme="medieval"] .ct{font-family:'IM Fell English',serif;color:#8C6A3C;border-left:1px solid rgba(140,106,60,.2);background:none;border-top:none;border-bottom:none;border-right:none}
[data-theme="medieval"] .ct:hover,[data-theme="medieval"] .ct.on{color:#C0C0C0;background:rgba(139,0,0,.2)}
[data-theme="medieval"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1px;padding:2rem;background:#0D0D0D}
[data-theme="medieval"] .wi{background:#111;position:relative;overflow:hidden;border:1px solid rgba(140,106,60,.3);box-shadow:inset 0 0 20px rgba(0,0,0,.5)}
[data-theme="medieval"] .wi img{filter:grayscale(60%) contrast(1.15) sepia(20%);transition:filter .4s,transform .5s}
[data-theme="medieval"] .wi:hover img{filter:grayscale(30%) contrast(1.2) sepia(10%);transform:scale(1.06)}
[data-theme="medieval"] .wt{font-family:'UnifrakturMaguntia',cursive;font-size:1.1rem;color:#C0C0C0}
[data-theme="medieval"] .wm{font-family:'IM Fell English',serif;font-style:italic;color:#8C6A3C;font-size:.78rem}
[data-theme="medieval"] .wio{background:linear-gradient(to top,rgba(13,13,13,.95),transparent);padding:2rem 1rem .8rem}
[data-theme="medieval"] #pg-about{background:#0D0D0D}
[data-theme="medieval"] #about{color:#C0C0C0}
[data-theme="medieval"] .sh{font-family:'UnifrakturMaguntia',cursive;color:#8C6A3C;font-size:1.3rem;letter-spacing:.05em;border-bottom:1px solid rgba(140,106,60,.3)}
[data-theme="medieval"] .al2 img{border:4px solid #8C6A3C;filter:grayscale(40%) contrast(1.1) sepia(20%);box-shadow:0 0 30px rgba(139,0,0,.3)}
[data-theme="medieval"] #pg-cv{background:#0D0D0D;color:#C0C0C0}
[data-theme="medieval"] .eyr{border-bottom:1px solid rgba(140,106,60,.2)}
[data-theme="medieval"] .yl{font-family:'UnifrakturMaguntia',cursive;color:#8C6A3C;font-size:1.2rem}
[data-theme="medieval"] .en{font-family:'IM Fell English',serif;color:#C0C0C0}
[data-theme="medieval"] .et{font-family:'IM Fell English',serif;font-style:italic;color:#5a5a5a}
[data-theme="medieval"] #pg-gallery{background:#0D0D0D}
[data-theme="medieval"] #galleryHint{background:rgba(20,15,10,.95);border:1px solid rgba(140,106,60,.4);box-shadow:0 0 40px rgba(139,0,0,.2)}
[data-theme="medieval"] #galleryHint h2{font-family:'UnifrakturMaguntia',cursive;color:#8C6A3C;font-size:2rem}
[data-theme="medieval"] #galleryHint button{background:linear-gradient(135deg,#8B0000,#5a0000);color:#C0C0C0;border:1px solid #8C6A3C;font-family:'IM Fell English',serif;letter-spacing:.1em}
[data-theme="medieval"] footer{background:#050505;color:#8C6A3C;border-top:2px solid #8C6A3C;font-family:'IM Fell English',serif}
[data-theme="medieval"] footer a{color:#C0C0C0}
@keyframes torchFlicker{0%,100%{opacity:1;text-shadow:0 0 10px rgba(255,140,0,.8)}25%{opacity:.92;text-shadow:0 0 15px rgba(255,100,0,.9)}50%{opacity:.98;text-shadow:0 0 8px rgba(255,160,0,.7)}75%{opacity:.94;text-shadow:0 0 20px rgba(255,80,0,.85)}}
[data-theme="medieval"] .logo{animation:torchFlicker 3s ease infinite}

/* ══ FULL-SITE FIXES FOR EXISTING THEMES ══════════════ */
[data-theme="baroque"] #pg-about,[data-theme="baroque"] #pg-cv,[data-theme="baroque"] #pg-gallery,[data-theme="baroque"] footer{background:#1A0A0E}
[data-theme="baroque"] .sh{font-family:'Cinzel Decorative','Cormorant Garamond',serif;color:#C9922A;font-size:1rem;letter-spacing:.2em;border-bottom:2px solid rgba(201,146,42,.3)}
[data-theme="baroque"] .al2 img{border:5px solid #C9922A;box-shadow:0 0 0 2px #1A0A0E,0 0 0 8px #C9922A,0 0 40px rgba(201,146,42,.4)}
[data-theme="baroque"] .yl{font-family:'Cinzel Decorative',serif;color:#C9922A;font-size:1.2rem}
[data-theme="baroque"] .en{font-family:'Cormorant Garamond',serif;color:#F5EDD6;font-size:1rem}
[data-theme="baroque"] .et{font-family:'Cormorant Garamond',serif;font-style:italic;color:#C9922A}
[data-theme="baroque"] #galleryHint{background:rgba(26,10,14,.95);border:2px solid #C9922A}
[data-theme="baroque"] #galleryHint h2{font-family:'Cinzel Decorative',serif;color:#C9922A}
[data-theme="baroque"] #galleryHint button{background:#C9922A;color:#1A0A0E;border:none;font-family:'Cinzel Decorative',serif}
[data-theme="baroque"] footer{border-top:3px double #C9922A;color:#C9922A;font-family:'Cormorant Garamond',serif}
[data-theme="bauhaus"] #pg-about,[data-theme="bauhaus"] #pg-cv,[data-theme="bauhaus"] #pg-gallery,[data-theme="bauhaus"] footer{background:#fff;color:#000}
[data-theme="bauhaus"] .sh{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;font-size:1.4rem;border-bottom:4px solid #E63329}
[data-theme="bauhaus"] .al2 img{border-radius:0;border:4px solid #000}
[data-theme="bauhaus"] .yl{font-family:'DM Sans',sans-serif;font-weight:700;color:#E63329;font-size:1.5rem}
[data-theme="bauhaus"] .en{font-family:'DM Sans',sans-serif;font-weight:700;color:#000}
[data-theme="bauhaus"] .et{font-family:'DM Sans',sans-serif;color:#555}
[data-theme="bauhaus"] #galleryHint{background:#fff;border:4px solid #000}
[data-theme="bauhaus"] #galleryHint h2{font-family:'DM Sans',sans-serif;font-weight:700;color:#000}
[data-theme="bauhaus"] #galleryHint button{background:#E63329;color:#fff;border:none;font-family:'DM Sans',sans-serif;font-weight:700;border-radius:0}
[data-theme="bauhaus"] footer{background:#000;color:#fff;border-top:4px solid #E63329;font-family:'DM Sans',sans-serif}
[data-theme="popart"] #pg-about,[data-theme="popart"] #pg-cv,[data-theme="popart"] #pg-gallery,[data-theme="popart"] footer{background:#FFE600}
[data-theme="popart"] .sh{font-family:'Bangers',cursive;font-size:2rem;color:#000;letter-spacing:.05em;border-bottom:3px solid #000}
[data-theme="popart"] .al2 img{border:5px solid #000;box-shadow:6px 6px 0 #FF3EA5}
[data-theme="popart"] .yl{font-family:'Bangers',cursive;font-size:2rem;color:#FF3EA5}
[data-theme="popart"] .en{font-family:'Bangers',cursive;font-size:1.1rem;color:#000}
[data-theme="popart"] .et{font-family:monospace;font-size:.75rem;color:#000}
[data-theme="popart"] #galleryHint{background:#FFE600;border:4px solid #000;box-shadow:8px 8px 0 #000}
[data-theme="popart"] #galleryHint h2{font-family:'Bangers',cursive;font-size:3rem;color:#000}
[data-theme="popart"] #galleryHint button{background:#FF3EA5;color:#fff;border:3px solid #000;font-family:'Bangers',cursive;font-size:1.2rem;box-shadow:4px 4px 0 #000}
[data-theme="popart"] footer{background:#FF3EA5;color:#000;border-top:4px solid #000;font-family:'Bangers',cursive;font-size:1.1rem}
[data-theme="newspaper"] #pg-about,[data-theme="newspaper"] #pg-cv,[data-theme="newspaper"] #pg-gallery,[data-theme="newspaper"] footer{background:#F8F5ED;color:#0A0A0A}
[data-theme="newspaper"] .sh{font-family:'Playfair Display',serif;font-weight:700;font-size:1.4rem;color:#CC0000;border-bottom:3px double #0A0A0A;padding-bottom:.4rem}
[data-theme="newspaper"] .al2 img{border:2px solid #0A0A0A;filter:grayscale(20%)}
[data-theme="newspaper"] .yl{font-family:'Playfair Display',serif;font-weight:700;color:#CC0000;font-size:1.3rem}
[data-theme="newspaper"] .en{font-family:'Source Serif 4',serif;color:#0A0A0A}
[data-theme="newspaper"] .et{font-family:monospace;color:#555;font-size:.78rem}
[data-theme="newspaper"] #galleryHint{background:#F8F5ED;border:3px double #0A0A0A}
[data-theme="newspaper"] #galleryHint h2{font-family:'Playfair Display',serif;font-weight:700;color:#0A0A0A}
[data-theme="newspaper"] #galleryHint button{background:#0A0A0A;color:#F8F5ED;border:none;font-family:'Playfair Display',serif;letter-spacing:.08em}
[data-theme="newspaper"] footer{background:#0A0A0A;color:#F8F5ED;border-top:1px solid #555;font-family:'Source Serif 4',serif;font-size:.8rem}
"""

if '[data-theme="chinese"]' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css_block + html[last_style:]
    changes.append('STEP 5: CSS block inserted before last </style>')
else:
    changes.append('STEP 5: Chinese theme CSS already present, skipped')

# ══════════════════════════════════════════════════════
# STEP 6a: Inject 3D model divs into hero section
# ══════════════════════════════════════════════════════
model_divs = """<div id="chineseModel3D" style="display:none"></div>
<div id="medievalModel3D" style="display:none"></div>
</section>"""

hero_idx = html.find('<section id="hero">')
if hero_idx == -1:
    hero_idx = html.find('id="hero"')
if hero_idx != -1:
    section_close = html.find('</section>', hero_idx)
    if 'chineseModel3D' not in html[hero_idx:section_close+100]:
        html = html[:section_close] + model_divs + html[section_close+10:]
        changes.append('STEP 6a: 3D model divs injected into hero')
    else:
        changes.append('STEP 6a: 3D model divs already present, skipped')
else:
    changes.append('STEP 6a: ERROR - hero section not found!')

# ══════════════════════════════════════════════════════
# STEP 6b: Large JS block before </body>
# ══════════════════════════════════════════════════════
js_block = """
<script>
(function() {
  if (typeof gsap === 'undefined') return;
  gsap.registerPlugin(ScrollTrigger, Draggable, MotionPathPlugin);
  window.playThemeTransition = function(color, callback) {
    var ov = document.getElementById('themeTransitionOverlay');
    var circle = document.getElementById('morphCircle');
    if (!ov || !circle) { callback && callback(); return; }
    ov.style.color = color || '#000';
    circle.setAttribute('r', '0');
    gsap.timeline()
      .set(ov, { visibility: 'visible' })
      .to(circle, { attr: { r: Math.hypot(window.innerWidth, window.innerHeight) }, duration: 0.45, ease: 'power2.in' })
      .add(function() { callback && callback(); })
      .to(circle, { attr: { r: 0 }, duration: 0.4, ease: 'power2.out', delay: 0.05 })
      .set(ov, { visibility: 'hidden' });
  };
  window.initScrollAnimations = function() {
    ScrollTrigger.getAll().forEach(function(st) { st.kill(); });
    gsap.utils.toArray('.eyr').forEach(function(el, i) {
      gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 88%', toggleActions: 'play none none none' }, opacity: 0, x: -30, duration: 0.6, delay: i * 0.1, ease: 'power2.out' });
    });
    var aboutImg = document.querySelector('.al2 img');
    if (aboutImg) { gsap.from(aboutImg, { scrollTrigger: { trigger: aboutImg, start: 'top 80%' }, opacity: 0, scale: 0.85, duration: 0.9, ease: 'back.out(1.5)' }); }
    gsap.utils.toArray('.sh').forEach(function(el) { gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 85%' }, opacity: 0, y: 20, duration: 0.5, ease: 'power2.out' }); });
  };
  window.staggerWorkItems = function() {
    var items = document.querySelectorAll('.wi');
    if (!items.length) return;
    gsap.from(items, { opacity: 0, y: 50, scale: 0.95, duration: 0.55, stagger: 0.07, ease: 'power3.out', clearProps: 'all' });
    items.forEach(function(el) {
      el.addEventListener('mouseenter', function() { gsap.to(el, { scale: 1.03, duration: 0.3, ease: 'back.out(2)', overwrite: true }); });
      el.addEventListener('mouseleave', function() { gsap.to(el, { scale: 1, duration: 0.5, ease: 'elastic.out(1,0.5)', overwrite: true }); });
    });
  };
  var _origApply = window.applyTheme;
  if (_origApply) {
    window.applyTheme = function(theme) {
      var bgColors = { chinese: '#F7F3EA', medieval: '#0D0D0D', baroque: '#1A0A0E', bauhaus: '#ffffff', popart: '#FFE600', newspaper: '#F8F5ED', 'default': '#090909' };
      var color = bgColors[theme] || '#090909';
      if (typeof playThemeTransition === 'function') {
        playThemeTransition(color, function() { _origApply(theme); setTimeout(function() { staggerWorkItems(); initScrollAnimations(); init3DModels(theme); }, 100); });
      } else { _origApply(theme); }
    };
  }
  window.addEventListener('load', function() {
    setTimeout(function() { staggerWorkItems(); initScrollAnimations(); var saved = localStorage.getItem('wwc-theme') || 'default'; init3DModels(saved); }, 300);
  });
})();

window.init3DModels = function(theme) {
  ['chineseModel3D','medievalModel3D'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) { if (el._cleanup) { el._cleanup(); el._cleanup = null; } while (el.firstChild) { el.removeChild(el.firstChild); } }
  });
  if (typeof THREE === 'undefined') return;
  if (theme === 'chinese') { createJadeDisc('chineseModel3D'); }
  else if (theme === 'medieval') { createMedievalHelmet('medievalModel3D'); }
};

function createJadeDisc(containerId) {
  var container = document.getElementById(containerId);
  if (!container) return;
  var W = container.offsetWidth || 280, H = container.offsetHeight || 280;
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(40, W/H, 0.1, 100);
  camera.position.z = 4.5;
  var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(W, H); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); renderer.setClearColor(0x000000, 0);
  container.appendChild(renderer.domElement);
  var mat = new THREE.MeshPhongMaterial({ color: 0x2E8B57, shininess: 180, specular: 0xaaffcc, emissive: 0x0a2015 });
  var outer = new THREE.Mesh(new THREE.TorusGeometry(1.2, 0.28, 32, 128), mat);
  scene.add(outer);
  var inner = new THREE.Mesh(new THREE.TorusGeometry(0.6, 0.12, 16, 80), mat.clone());
  scene.add(inner);
  var disc = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.04, 64), mat.clone());
  disc.rotation.x = Math.PI / 2; scene.add(disc);
  var goldMat = new THREE.MeshPhongMaterial({ color: 0xB8860B, shininess: 200, specular: 0xffee88 });
  var goldRing = new THREE.Mesh(new THREE.TorusGeometry(1.55, 0.04, 8, 80), goldMat);
  scene.add(goldRing);
  scene.add(new THREE.AmbientLight(0xffffff, 0.5));
  var dLight = new THREE.DirectionalLight(0xffd700, 1.5); dLight.position.set(3, 5, 5); scene.add(dLight);
  var pLight = new THREE.PointLight(0x88ffaa, 0.8, 10); pLight.position.set(-3, -2, 2); scene.add(pLight);
  var frame;
  function animate() { frame = requestAnimationFrame(animate); var t = Date.now() * 0.001; outer.rotation.y = t * 0.4; outer.rotation.x = Math.sin(t * 0.5) * 0.15; inner.rotation.y = -t * 0.6; goldRing.rotation.y = t * 0.3; renderer.render(scene, camera); }
  animate();
  container._cleanup = function() { cancelAnimationFrame(frame); renderer.dispose(); };
}

function createMedievalHelmet(containerId) {
  var container = document.getElementById(containerId);
  if (!container) return;
  var W = container.offsetWidth || 260, H = container.offsetHeight || 260;
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(40, W/H, 0.1, 100);
  camera.position.set(0, 0.5, 4.5);
  var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(W, H); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); renderer.setClearColor(0x000000, 0);
  container.appendChild(renderer.domElement);
  var metalMat = new THREE.MeshPhongMaterial({ color: 0x888888, specular: 0xffffff, shininess: 250, emissive: 0x111111 });
  var bronzeMat = new THREE.MeshPhongMaterial({ color: 0x8C6A3C, specular: 0xffcc44, shininess: 150 });
  var skull = new THREE.Mesh(new THREE.SphereGeometry(0.9, 32, 24, 0, Math.PI*2, 0, Math.PI*0.65), metalMat);
  skull.position.y = 0.3; scene.add(skull);
  [-1, 1].forEach(function(side) { var cheek = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.7, 0.6), metalMat.clone()); cheek.position.set(side * 0.85, -0.25, 0.1); cheek.rotation.z = side * 0.15; scene.add(cheek); });
  var visor = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.25, 0.15), bronzeMat);
  visor.position.set(0, 0.15, 0.82); scene.add(visor);
  for (var i = 0; i < 3; i++) { var slit = new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.04, 0.2), new THREE.MeshPhongMaterial({ color: 0x111111, emissive: 0xff4400, emissiveIntensity: 0.3 })); slit.position.set(0, 0.25 - i * 0.07, 0.9); scene.add(slit); }
  var neck = new THREE.Mesh(new THREE.CylinderGeometry(0.85, 1.0, 0.4, 32, 1, true), metalMat.clone());
  neck.position.y = -0.5; scene.add(neck);
  var plume = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.06, 0.8, 8), new THREE.MeshPhongMaterial({ color: 0x8B0000, emissive: 0x3a0000 }));
  plume.position.set(0, 1.2, 0); scene.add(plume);
  scene.add(new THREE.AmbientLight(0x334455, 0.6));
  var torch = new THREE.PointLight(0xff8844, 1.5, 10); torch.position.set(2, 3, 3); scene.add(torch);
  var torch2 = new THREE.PointLight(0x4466ff, 0.5, 8); torch2.position.set(-3, 1, 2); scene.add(torch2);
  var frame2;
  function animate2() { frame2 = requestAnimationFrame(animate2); var t = Date.now() * 0.001; scene.rotation.y = t * 0.25; torch.intensity = 1.3 + Math.sin(t * 7) * 0.2 + Math.sin(t * 13) * 0.1; renderer.render(scene, camera); }
  animate2();
  container._cleanup = function() { cancelAnimationFrame(frame2); renderer.dispose(); };
}
</script>
</body>"""

if 'init3DModels' not in html:
    html = html.replace('</body>', js_block, 1)
    changes.append('STEP 6b: JS block added before </body>')
else:
    changes.append('STEP 6b: JS already present, skipped')

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Original: {original_len:,} | New: {len(html):,} | Delta: +{len(html)-original_len:,}")
print("Changes:")
for c in changes:
    print(f"  {'OK' if 'ERROR' not in c else 'ERR'} {c}")
print("Validation:")
for label, cond in [
    ("GSAP", 'gsap.min.js' in html), ("SVG overlay", 'themeTransitionOverlay' in html),
    ("Chinese btn", 'data-theme="chinese"' in html), ("Medieval btn", 'data-theme="medieval"' in html),
    ("Noto Serif TC", 'Noto+Serif+TC' in html), ("Chinese CSS", '[data-theme="chinese"]' in html),
    ("Medieval CSS", '[data-theme="medieval"]' in html), ("3D jade fn", 'createJadeDisc' in html),
    ("3D helmet fn", 'createMedievalHelmet' in html), ("init3DModels", 'init3DModels' in html),
]:
    print(f"  {'OK' if cond else 'MISSING'} {label}")
