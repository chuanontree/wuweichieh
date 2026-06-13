#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add themes P (Sky), Q (Crystal), R (Y2K Liquid Metal):
full-site CSS + AI widget theming + 3D models + GSAP-friendly hooks."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html)
log = []

# ── 1. Switcher buttons P/Q/R ──────────────────────────
anchor = '<button class="ts-btn" data-theme="medieval" title="O · 鋼鐵誓約">O</button>'
new_btns = anchor + """
  <button class="ts-btn" data-theme="sky" title="P · 天空懸浮">P</button>
  <button class="ts-btn" data-theme="crystal" title="Q · 水晶">Q</button>
  <button class="ts-btn" data-theme="y2k" title="R · Y2K液態金屬">R</button>"""
if 'data-theme="sky"' not in html:
    html = html.replace(anchor, new_btns, 1)
    log.append('switcher P/Q/R added')
else:
    log.append('switcher already has P/Q/R')

# ── 2. CSS block before last </style> ──────────────────
css = """
/* ══ THEME P · 天空懸浮碎石 · SKY ══════════════════════ */
[data-theme="sky"]{--bg:#cfe6f7;--fg:#243446;--accent:#FF9E5E;--metal:#8FB8DE;--line:rgba(36,52,70,.12);--dim:rgba(255,255,255,.5);font-family:'DM Sans',sans-serif}
[data-theme="sky"] header{background:rgba(207,230,247,.8);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.6);box-shadow:0 4px 30px rgba(143,184,222,.25)}
[data-theme="sky"] .logo{font-family:'DM Sans',sans-serif;font-weight:700;color:#243446;letter-spacing:.04em}
[data-theme="sky"] .ni{font-family:'DM Sans',sans-serif;color:#3d566e;border-left:none;font-size:.68rem}
[data-theme="sky"] .ni:hover,[data-theme="sky"] .ni.on{color:#FF9E5E}
[data-theme="sky"] #hero{background:linear-gradient(180deg,#aacdf0 0%,#cfe6f7 45%,#f3f9ff 100%);position:relative;overflow:hidden}
[data-theme="sky"] #hero::before{content:'';position:absolute;width:240px;height:90px;background:#fff;border-radius:50%;top:18%;left:8%;box-shadow:90px 20px 0 -10px #fff,180px -10px 0 -20px #fff;opacity:.8;animation:skyDrift 24s linear infinite;z-index:0}
[data-theme="sky"] #hero::after{content:'';position:absolute;width:180px;height:70px;background:#fff;border-radius:50%;top:60%;right:10%;opacity:.65;animation:skyDrift 32s linear infinite reverse;z-index:0}
[data-theme="sky"] .hn{font-family:'DM Sans',sans-serif;font-weight:700;color:#243446;text-shadow:0 6px 24px rgba(143,184,222,.5);position:relative;z-index:2;animation:skyFloat 6s ease-in-out infinite}
[data-theme="sky"] .hn .ol{-webkit-text-stroke:1px #FF9E5E;color:transparent}
[data-theme="sky"] .he{color:#FF9E5E;font-family:'DM Sans',sans-serif}
[data-theme="sky"] .htag{font-family:'DM Sans',sans-serif;color:#3d566e;position:relative;z-index:2}
[data-theme="sky"] #catBar{border-bottom:1px solid rgba(36,52,70,.12);background:rgba(255,255,255,.35)}
[data-theme="sky"] .ct{font-family:'DM Sans',sans-serif;font-size:.62rem;color:#3d566e;background:none;border:none;padding:.5rem 1.2rem;border-radius:20px;cursor:pointer}
[data-theme="sky"] .ct:hover,[data-theme="sky"] .ct.on{color:#fff;background:#FF9E5E}
[data-theme="sky"] #pg-works,[data-theme="sky"] #pg-about,[data-theme="sky"] #pg-cv,[data-theme="sky"] #pg-gallery{background:linear-gradient(180deg,#e8f3fc,#f3f9ff)}
[data-theme="sky"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:2rem;padding:2.5rem}
[data-theme="sky"] .wi{background:rgba(255,255,255,.7);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.8);border-radius:20px;box-shadow:0 14px 40px rgba(143,184,222,.35);position:relative;overflow:hidden;animation:skyFloat 7s ease-in-out infinite}
[data-theme="sky"] .wi:nth-child(2n){animation-delay:-2s}
[data-theme="sky"] .wi:nth-child(3n){animation-delay:-4s}
[data-theme="sky"] .wi img{transition:transform .6s;border-radius:20px 20px 0 0}
[data-theme="sky"] .wi:hover{transform:translateY(-10px);box-shadow:0 26px 60px rgba(143,184,222,.5)}
[data-theme="sky"] .wi:hover img{transform:scale(1.05)}
[data-theme="sky"] .wt{font-family:'DM Sans',sans-serif;font-weight:700;color:#243446}
[data-theme="sky"] .wm{font-family:'DM Sans',sans-serif;color:#FF9E5E;font-size:.8rem}
[data-theme="sky"] .wio{background:linear-gradient(to top,rgba(255,255,255,.95),transparent);padding:1.5rem 1rem .8rem}
[data-theme="sky"] .al2 img{border-radius:50%;border:5px solid #fff;box-shadow:0 12px 40px rgba(143,184,222,.5)}
[data-theme="sky"] .sh{font-family:'DM Sans',sans-serif;font-weight:700;color:#FF9E5E;border-bottom:2px solid rgba(255,158,94,.3)}
[data-theme="sky"] .eyr{border-left:2px solid #8FB8DE;padding-left:1.5rem;margin-bottom:1.5rem}
[data-theme="sky"] .yl{font-family:'DM Sans',sans-serif;font-weight:700;color:#8FB8DE}
[data-theme="sky"] .en{font-family:'DM Sans',sans-serif;color:#243446}
[data-theme="sky"] .et{font-family:'DM Sans',sans-serif;color:#7a93a8;font-size:.8rem}
[data-theme="sky"] #galleryHint{background:rgba(255,255,255,.7);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.8);border-radius:24px;box-shadow:0 14px 50px rgba(143,184,222,.4)}
[data-theme="sky"] #galleryHint h2{font-family:'DM Sans',sans-serif;font-weight:700;color:#243446}
[data-theme="sky"] #galleryHint button{background:#FF9E5E;color:#fff;border:none;border-radius:30px;font-family:'DM Sans',sans-serif;font-weight:700}
[data-theme="sky"] footer{background:linear-gradient(180deg,#cfe6f7,#aacdf0);color:#243446;border-top:1px solid rgba(255,255,255,.7);font-family:'DM Sans',sans-serif}
[data-theme="sky"] footer a{color:#FF9E5E}
[data-theme="sky"] #wwc-btn{background:linear-gradient(135deg,#8FB8DE,#FF9E5E);box-shadow:0 8px 30px rgba(143,184,222,.5)}
[data-theme="sky"] #wwc-panel{background:rgba(243,249,255,.92);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.8);border-radius:20px}
[data-theme="sky"] .wwc-head{background:linear-gradient(135deg,#aacdf0,#8FB8DE)}
#skyModel3D{position:absolute;right:6vw;top:50%;transform:translateY(-50%);width:300px;height:300px;z-index:3;pointer-events:none;display:none}
[data-theme="sky"] #skyModel3D{display:block}
@keyframes skyFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@keyframes skyDrift{0%{transform:translateX(-120px)}100%{transform:translateX(120px)}}

/* ══ THEME Q · 水晶 · CRYSTAL ══════════════════════════ */
[data-theme="crystal"]{--bg:#eef0ff;--fg:#2a2350;--accent:#a06bff;--metal:#b8c6ff;--line:rgba(160,107,255,.18);--dim:rgba(255,255,255,.5);font-family:'DM Sans',sans-serif}
[data-theme="crystal"] body{background:linear-gradient(135deg,#eef0ff,#ffe9fb,#e2fbff)}
[data-theme="crystal"] header{background:rgba(255,255,255,.45);backdrop-filter:blur(18px) saturate(1.5);border-bottom:1px solid rgba(255,255,255,.6);box-shadow:0 4px 30px rgba(160,107,255,.18)}
[data-theme="crystal"] .logo{font-family:'DM Sans',sans-serif;font-weight:700;background:linear-gradient(90deg,#a06bff,#6bd5ff,#ff8fe0);-webkit-background-clip:text;background-clip:text;color:transparent;letter-spacing:.05em}
[data-theme="crystal"] .ni{color:#5a4b8a;border-left:none;font-size:.68rem}
[data-theme="crystal"] .ni:hover,[data-theme="crystal"] .ni.on{color:#a06bff}
[data-theme="crystal"] #hero{background:linear-gradient(135deg,rgba(238,240,255,.6),rgba(255,233,251,.6),rgba(226,251,255,.6));position:relative;overflow:hidden}
[data-theme="crystal"] .hn{font-weight:700;background:linear-gradient(120deg,#a06bff,#6bd5ff,#ff8fe0,#a06bff);background-size:300% 300%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:crystalShine 8s ease infinite;position:relative;z-index:2}
[data-theme="crystal"] .hn .ol{-webkit-text-stroke:1px #a06bff;color:transparent;-webkit-background-clip:initial;background:none}
[data-theme="crystal"] .he{color:#a06bff}
[data-theme="crystal"] .htag{color:#5a4b8a;position:relative;z-index:2}
[data-theme="crystal"] #catBar{border-bottom:1px solid rgba(160,107,255,.18);background:rgba(255,255,255,.3)}
[data-theme="crystal"] .ct{font-size:.62rem;color:#5a4b8a;background:none;border:1px solid transparent;padding:.4rem 1.1rem;border-radius:20px;cursor:pointer}
[data-theme="crystal"] .ct:hover,[data-theme="crystal"] .ct.on{color:#a06bff;border-color:rgba(160,107,255,.4);background:rgba(255,255,255,.5)}
[data-theme="crystal"] #pg-works,[data-theme="crystal"] #pg-about,[data-theme="crystal"] #pg-cv,[data-theme="crystal"] #pg-gallery{background:linear-gradient(135deg,#eef0ff,#ffe9fb,#e2fbff)}
[data-theme="crystal"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.8rem;padding:2.2rem}
[data-theme="crystal"] .wi{background:rgba(255,255,255,.35);backdrop-filter:blur(12px) saturate(1.4);border:1.5px solid rgba(255,255,255,.7);border-radius:18px;box-shadow:0 10px 40px rgba(160,107,255,.25),inset 0 1px 0 rgba(255,255,255,.9);position:relative;overflow:hidden}
[data-theme="crystal"] .wi::before{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent 30%,rgba(255,255,255,.6) 50%,transparent 70%);transform:translateX(-100%);transition:transform .7s;z-index:2;pointer-events:none}
[data-theme="crystal"] .wi:hover::before{transform:translateX(100%)}
[data-theme="crystal"] .wi img{transition:transform .6s;filter:saturate(1.1)}
[data-theme="crystal"] .wi:hover{transform:translateY(-6px) scale(1.02);box-shadow:0 20px 60px rgba(160,107,255,.4)}
[data-theme="crystal"] .wt{font-weight:700;color:#2a2350}
[data-theme="crystal"] .wm{color:#a06bff;font-size:.8rem}
[data-theme="crystal"] .wio{background:linear-gradient(to top,rgba(255,255,255,.85),transparent);padding:1.5rem 1rem .8rem}
[data-theme="crystal"] .al2 img{border-radius:24px;border:2px solid rgba(255,255,255,.8);box-shadow:0 12px 50px rgba(160,107,255,.4)}
[data-theme="crystal"] .sh{font-weight:700;background:linear-gradient(90deg,#a06bff,#6bd5ff);-webkit-background-clip:text;background-clip:text;color:transparent;border-bottom:2px solid rgba(160,107,255,.25)}
[data-theme="crystal"] .eyr{border-left:2px solid #a06bff;padding-left:1.5rem;margin-bottom:1.5rem}
[data-theme="crystal"] .yl{font-weight:700;color:#a06bff}
[data-theme="crystal"] .en{color:#2a2350}
[data-theme="crystal"] .et{color:#8a7db5;font-size:.8rem}
[data-theme="crystal"] #galleryHint{background:rgba(255,255,255,.4);backdrop-filter:blur(16px);border:1.5px solid rgba(255,255,255,.7);border-radius:24px;box-shadow:0 14px 60px rgba(160,107,255,.35)}
[data-theme="crystal"] #galleryHint h2{font-weight:700;background:linear-gradient(90deg,#a06bff,#6bd5ff);-webkit-background-clip:text;background-clip:text;color:transparent}
[data-theme="crystal"] #galleryHint button{background:linear-gradient(135deg,#a06bff,#6bd5ff);color:#fff;border:none;border-radius:30px;font-weight:700}
[data-theme="crystal"] footer{background:rgba(255,255,255,.3);backdrop-filter:blur(12px);color:#2a2350;border-top:1px solid rgba(255,255,255,.6)}
[data-theme="crystal"] footer a{color:#a06bff}
[data-theme="crystal"] #wwc-btn{background:linear-gradient(135deg,#a06bff,#6bd5ff,#ff8fe0);box-shadow:0 8px 30px rgba(160,107,255,.5)}
[data-theme="crystal"] #wwc-panel{background:rgba(255,255,255,.55);backdrop-filter:blur(20px) saturate(1.5);border:1px solid rgba(255,255,255,.7);border-radius:20px}
[data-theme="crystal"] .wwc-head{background:linear-gradient(135deg,#a06bff,#6bd5ff)}
#crystalModel3D{position:absolute;right:6vw;top:50%;transform:translateY(-50%);width:300px;height:300px;z-index:3;pointer-events:none;display:none}
[data-theme="crystal"] #crystalModel3D{display:block}
@keyframes crystalShine{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}

/* ══ THEME R · Y2K 液態金屬 · LIQUID CHROME ════════════ */
[data-theme="y2k"]{--bg:#0a0a14;--fg:#dfe6ff;--accent:#ff5ed2;--metal:#b9c4d6;--line:rgba(185,196,214,.18);--dim:rgba(185,196,214,.08);font-family:'Orbitron',sans-serif}
[data-theme="y2k"] body{background:radial-gradient(ellipse at 30% 20%,#1a1e3a,#0a0a14)}
[data-theme="y2k"] header{background:rgba(10,10,20,.85);backdrop-filter:blur(10px);border-bottom:1px solid;border-image:linear-gradient(90deg,#ff5ed2,#5ed7ff,#b9c4d6) 1;box-shadow:0 2px 24px rgba(255,94,210,.25)}
[data-theme="y2k"] .logo{font-family:'Orbitron',sans-serif;font-weight:900;background:linear-gradient(135deg,#fff,#b9c4d6 40%,#7d8aa3 60%,#fff);-webkit-background-clip:text;background-clip:text;color:transparent;letter-spacing:.1em}
[data-theme="y2k"] .ni{font-family:'Rajdhani',sans-serif;font-weight:600;color:#9fb0d0;border-left:1px solid rgba(185,196,214,.18);letter-spacing:.05em}
[data-theme="y2k"] .ni:hover,[data-theme="y2k"] .ni.on{color:#ff5ed2;background:rgba(255,94,210,.12)}
[data-theme="y2k"] #hero{background:radial-gradient(ellipse at center,#1a1e3a,#0a0a14);position:relative;overflow:hidden}
[data-theme="y2k"] #hero::before{content:'';position:absolute;inset:0;background:linear-gradient(115deg,transparent 40%,rgba(94,215,255,.08) 50%,transparent 60%);animation:y2kSheen 6s linear infinite;z-index:1}
[data-theme="y2k"] .hn{font-family:'Orbitron',sans-serif;font-weight:900;background:linear-gradient(135deg,#fff 0%,#b9c4d6 30%,#7d8aa3 50%,#fff 70%,#5ed7ff 100%);background-size:200% 200%;-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:0 0 40px rgba(94,215,255,.3);animation:y2kFlow 7s ease infinite;position:relative;z-index:2;letter-spacing:.04em}
[data-theme="y2k"] .hn .ol{-webkit-text-stroke:1px #ff5ed2;color:transparent;background:none;-webkit-background-clip:initial}
[data-theme="y2k"] .he{color:#5ed7ff;font-family:'Rajdhani',sans-serif;font-weight:600}
[data-theme="y2k"] .htag{font-family:'Rajdhani',sans-serif;color:#9fb0d0;position:relative;z-index:2;letter-spacing:.04em}
[data-theme="y2k"] #catBar{border-bottom:1px solid rgba(185,196,214,.18);background:rgba(20,24,46,.4)}
[data-theme="y2k"] .ct{font-family:'Rajdhani',sans-serif;font-weight:600;font-size:.66rem;color:#9fb0d0;background:none;border:none;border-right:1px solid rgba(185,196,214,.12);padding:.5rem 1.2rem;letter-spacing:.06em;cursor:pointer}
[data-theme="y2k"] .ct:hover,[data-theme="y2k"] .ct.on{color:#ff5ed2;background:rgba(255,94,210,.12)}
[data-theme="y2k"] #pg-works,[data-theme="y2k"] #pg-about,[data-theme="y2k"] #pg-cv,[data-theme="y2k"] #pg-gallery{background:radial-gradient(ellipse at top,#14182e,#0a0a14)}
[data-theme="y2k"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.8rem;padding:2.2rem}
[data-theme="y2k"] .wi{background:linear-gradient(135deg,#1c2238,#10131f);border:1px solid transparent;border-image:linear-gradient(135deg,#b9c4d6,#5ed7ff,#ff5ed2) 1;box-shadow:0 10px 40px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.15);position:relative;overflow:hidden}
[data-theme="y2k"] .wi::after{content:'';position:absolute;top:0;left:0;right:0;height:40%;background:linear-gradient(180deg,rgba(255,255,255,.18),transparent);pointer-events:none}
[data-theme="y2k"] .wi img{filter:saturate(1.2) contrast(1.05);transition:transform .5s}
[data-theme="y2k"] .wi:hover{transform:translateY(-6px) scale(1.02);box-shadow:0 18px 50px rgba(94,215,255,.35)}
[data-theme="y2k"] .wi:hover img{transform:scale(1.07)}
[data-theme="y2k"] .wt{font-family:'Orbitron',sans-serif;font-weight:700;color:#dfe6ff;letter-spacing:.03em}
[data-theme="y2k"] .wm{font-family:'Rajdhani',sans-serif;color:#5ed7ff;font-size:.82rem}
[data-theme="y2k"] .wio{background:linear-gradient(to top,rgba(10,10,20,.95),transparent);padding:2rem 1rem .8rem}
[data-theme="y2k"] .al2 img{border-radius:14px;border:2px solid;border-image:linear-gradient(135deg,#5ed7ff,#ff5ed2) 1;box-shadow:0 0 40px rgba(94,215,255,.4)}
[data-theme="y2k"] .sh{font-family:'Orbitron',sans-serif;font-weight:700;background:linear-gradient(90deg,#fff,#5ed7ff,#ff5ed2);-webkit-background-clip:text;background-clip:text;color:transparent;border-bottom:1px solid rgba(94,215,255,.3)}
[data-theme="y2k"] .eyr{border-left:2px solid #ff5ed2;padding-left:1.5rem;margin-bottom:1.5rem}
[data-theme="y2k"] .yl{font-family:'Orbitron',sans-serif;font-weight:700;color:#5ed7ff}
[data-theme="y2k"] .en{font-family:'Rajdhani',sans-serif;color:#dfe6ff;font-weight:600}
[data-theme="y2k"] .et{font-family:'Rajdhani',sans-serif;color:#7d8aa3;font-size:.82rem}
[data-theme="y2k"] #galleryHint{background:linear-gradient(135deg,rgba(28,34,56,.9),rgba(16,19,31,.9));backdrop-filter:blur(10px);border:1px solid transparent;border-image:linear-gradient(135deg,#5ed7ff,#ff5ed2) 1;box-shadow:0 0 50px rgba(94,215,255,.25)}
[data-theme="y2k"] #galleryHint h2{font-family:'Orbitron',sans-serif;font-weight:900;background:linear-gradient(90deg,#fff,#5ed7ff);-webkit-background-clip:text;background-clip:text;color:transparent}
[data-theme="y2k"] #galleryHint button{background:linear-gradient(135deg,#ff5ed2,#5ed7ff);color:#0a0a14;border:none;font-family:'Orbitron',sans-serif;font-weight:700;letter-spacing:.05em}
[data-theme="y2k"] footer{background:#06060d;color:#9fb0d0;border-top:1px solid;border-image:linear-gradient(90deg,#ff5ed2,#5ed7ff) 1;font-family:'Rajdhani',sans-serif}
[data-theme="y2k"] footer a{color:#5ed7ff}
[data-theme="y2k"] #wwc-btn{background:linear-gradient(135deg,#b9c4d6,#5ed7ff,#ff5ed2);box-shadow:0 8px 30px rgba(94,215,255,.5)}
[data-theme="y2k"] #wwc-panel{background:linear-gradient(135deg,rgba(28,34,56,.95),rgba(10,10,20,.95));backdrop-filter:blur(14px);border:1px solid transparent;border-image:linear-gradient(135deg,#5ed7ff,#ff5ed2) 1}
[data-theme="y2k"] .wwc-head{background:linear-gradient(135deg,#1a1e3a,#5ed7ff)}
[data-theme="y2k"] .wwc-name{font-family:'Orbitron',sans-serif}
#y2kModel3D{position:absolute;right:6vw;top:50%;transform:translateY(-50%);width:300px;height:300px;z-index:3;pointer-events:none;display:none}
[data-theme="y2k"] #y2kModel3D{display:block}
@keyframes y2kFlow{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
@keyframes y2kSheen{0%{transform:translateX(-60%)}100%{transform:translateX(60%)}}
"""
if '[data-theme="sky"]' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('CSS block inserted')
else:
    log.append('CSS already present')

# ── 3. Hero 3D model divs ──────────────────────────────
divs = """<div id="medievalModel3D" style="display:none"></div>
<div id="skyModel3D" style="display:none"></div>
<div id="crystalModel3D" style="display:none"></div>
<div id="y2kModel3D" style="display:none"></div>"""
if 'id="skyModel3D"' not in html:
    html = html.replace('<div id="medievalModel3D" style="display:none"></div>', divs, 1)
    log.append('3D model divs added')
else:
    log.append('3D divs already present')

# ── 4. bgColors map ────────────────────────────────────
old_bg = "var bgColors = { chinese: '#F7F3EA', medieval: '#0D0D0D', baroque: '#1A0A0E', bauhaus: '#ffffff', popart: '#FFE600', newspaper: '#F8F5ED', 'default': '#090909' };"
new_bg = "var bgColors = { chinese: '#F7F3EA', medieval: '#0D0D0D', baroque: '#1A0A0E', bauhaus: '#ffffff', popart: '#FFE600', newspaper: '#F8F5ED', sky: '#cfe6f7', crystal: '#eef0ff', y2k: '#0a0a14', 'default': '#090909' };"
if old_bg in html:
    html = html.replace(old_bg, new_bg, 1)
    log.append('bgColors extended')
else:
    log.append('bgColors NOT found (skip)')

# ── 5. init3DModels + new Three.js builders ────────────
old_init = """window.init3DModels = function(theme) {
  ['chineseModel3D','medievalModel3D'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) { if (el._cleanup) { el._cleanup(); el._cleanup = null; } while (el.firstChild) { el.removeChild(el.firstChild); } }
  });
  if (typeof THREE === 'undefined') return;
  if (theme === 'chinese') { createJadeDisc('chineseModel3D'); }
  else if (theme === 'medieval') { createMedievalHelmet('medievalModel3D'); }
};"""
new_init = """window.init3DModels = function(theme) {
  ['chineseModel3D','medievalModel3D','skyModel3D','crystalModel3D','y2kModel3D'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) { if (el._cleanup) { el._cleanup(); el._cleanup = null; } while (el.firstChild) { el.removeChild(el.firstChild); } }
  });
  if (typeof THREE === 'undefined') return;
  if (theme === 'chinese') { createJadeDisc('chineseModel3D'); }
  else if (theme === 'medieval') { createMedievalHelmet('medievalModel3D'); }
  else if (theme === 'sky') { createFloatingRocks('skyModel3D'); }
  else if (theme === 'crystal') { createCrystalCluster('crystalModel3D'); }
  else if (theme === 'y2k') { createLiquidChrome('y2kModel3D'); }
};

function _mk3d(containerId, fov, camz) {
  var c = document.getElementById(containerId); if (!c) return null;
  var W = c.offsetWidth || 300, H = c.offsetHeight || 300;
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(fov||42, W/H, 0.1, 100); camera.position.z = camz||5;
  var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(W, H); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); renderer.setClearColor(0x000000, 0);
  c.appendChild(renderer.domElement);
  return { c: c, scene: scene, camera: camera, renderer: renderer };
}

function createFloatingRocks(id) {
  var k = _mk3d(id, 45, 7); if (!k) return;
  var rockMat = new THREE.MeshPhongMaterial({ color: 0x7a8a99, flatShading: true, shininess: 10 });
  var grassMat = new THREE.MeshPhongMaterial({ color: 0x8fc97a, flatShading: true, shininess: 5 });
  var group = new THREE.Group();
  var data = [[0,0,0,1.1],[-2.2,1.1,-1,0.6],[2,1.4,-1.5,0.5],[1.6,-1.3,-0.5,0.45],[-1.8,-1.2,-1,0.4]];
  data.forEach(function(d){
    var g = new THREE.Group();
    var rock = new THREE.Mesh(new THREE.DodecahedronGeometry(d[3],0), rockMat);
    rock.scale.y = 0.7; g.add(rock);
    var cap = new THREE.Mesh(new THREE.SphereGeometry(d[3]*0.95,12,8,0,Math.PI*2,0,Math.PI*0.5), grassMat);
    cap.position.y = d[3]*0.15; g.add(cap);
    g.position.set(d[0],d[1],d[2]); g.userData.sp = Math.random()*Math.PI*2; group.add(g);
  });
  k.scene.add(group);
  k.scene.add(new THREE.AmbientLight(0xffffff,0.7));
  var dl = new THREE.DirectionalLight(0xffffff,1.0); dl.position.set(3,5,4); k.scene.add(dl);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; group.rotation.y=t*0.25; group.children.forEach(function(ch,i){ ch.position.y += Math.sin(t*1.2+ch.userData.sp)*0.003; ch.rotation.y=t*0.3+i; }); k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}

function createCrystalCluster(id) {
  var k = _mk3d(id, 42, 5); if (!k) return;
  var group = new THREE.Group();
  var cols = [0xa06bff,0x6bd5ff,0xff8fe0,0xffffff,0xc9b8ff];
  for (var i=0;i<7;i++){
    var mat = new THREE.MeshPhongMaterial({ color: cols[i%cols.length], transparent:true, opacity:0.55, shininess:240, specular:0xffffff, emissive:0x1a1030, emissiveIntensity:0.4 });
    var geo = new THREE.OctahedronGeometry(0.5+Math.random()*0.7, 0);
    var m = new THREE.Mesh(geo, mat);
    m.scale.y = 1.6+Math.random();
    m.position.set((Math.random()-0.5)*2.4,(Math.random()-0.5)*2.4,(Math.random()-0.5)*1.6);
    m.rotation.set(Math.random()*3,Math.random()*3,Math.random()*3);
    group.add(m);
  }
  k.scene.add(group);
  k.scene.add(new THREE.AmbientLight(0xffffff,0.6));
  var l1=new THREE.PointLight(0xa06bff,1.2,12); l1.position.set(3,2,4); k.scene.add(l1);
  var l2=new THREE.PointLight(0x6bd5ff,1.0,12); l2.position.set(-3,-1,3); k.scene.add(l2);
  var l3=new THREE.PointLight(0xff8fe0,0.8,12); l3.position.set(0,3,-2); k.scene.add(l3);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; group.rotation.y=t*0.4; group.rotation.x=Math.sin(t*0.3)*0.2; group.children.forEach(function(ch,i){ ch.rotation.y=t*(0.5+i*0.1); }); k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}

function createLiquidChrome(id) {
  var k = _mk3d(id, 42, 4.2); if (!k) return;
  var mat = new THREE.MeshPhongMaterial({ color: 0xc8d2e0, shininess: 300, specular: 0xffffff, emissive: 0x101830, emissiveIntensity: 0.3 });
  var geo = new THREE.IcosahedronGeometry(1.4, 4);
  var base = geo.attributes.position.array.slice(0);
  var blob = new THREE.Mesh(geo, mat); k.scene.add(blob);
  var torus = new THREE.Mesh(new THREE.TorusGeometry(1.9,0.07,16,80), new THREE.MeshPhongMaterial({color:0xff5ed2,shininess:200,specular:0xffffff})); torus.rotation.x=1.1; k.scene.add(torus);
  k.scene.add(new THREE.AmbientLight(0x334466,0.5));
  var l1=new THREE.PointLight(0x5ed7ff,1.5,15); l1.position.set(4,3,5); k.scene.add(l1);
  var l2=new THREE.PointLight(0xff5ed2,1.2,15); l2.position.set(-4,-2,3); k.scene.add(l2);
  var l3=new THREE.DirectionalLight(0xffffff,0.8); l3.position.set(0,5,2); k.scene.add(l3);
  var pos=geo.attributes.position, fr;
  function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001;
    for(var i=0;i<pos.count;i++){ var ix=i*3; var x=base[ix],y=base[ix+1],z=base[ix+2];
      var n=Math.sin(x*2+t*1.5)*0.12+Math.cos(y*2.5+t*1.2)*0.12+Math.sin(z*2+t)*0.1;
      var s=1+n/1.4;
      pos.array[ix]=x*s; pos.array[ix+1]=y*s; pos.array[ix+2]=z*s; }
    pos.needsUpdate=true; geo.computeVertexNormals();
    blob.rotation.y=t*0.4; torus.rotation.z=t*0.5; k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}"""
if 'createFloatingRocks' not in html:
    html = html.replace(old_init, new_init, 1)
    log.append('init3DModels + 3 builders added')
else:
    log.append('3D builders already present')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig, len(html), len(html)-orig))
for l in log: print('  -', l)
