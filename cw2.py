#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Elevate chinese WORKS handscroll into a real 國畫長卷: parallax ink
mountains, silk mounting on each panel, 引首/拖尾 panels, unroll entrance."""

import base64

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html)
log = []

# ---- ink-mountain SVG (two soft layers) → base64 data URI ----
svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='500'>"
       "<path d='M0,360 C160,300 260,260 380,300 C520,348 600,250 760,300 "
       "C900,344 1000,280 1160,316 C1320,352 1440,300 1600,330 L1600,500 L0,500 Z' "
       "fill='rgba(26,18,9,0.07)'/>"
       "<path d='M0,420 C200,380 320,400 480,372 C640,344 760,420 940,392 "
       "C1120,364 1240,408 1420,388 C1500,380 1560,392 1600,386 L1600,500 L0,500 Z' "
       "fill='rgba(26,18,9,0.11)'/>"
       "<path d='M120,300 C160,250 200,250 240,300 Z' fill='rgba(26,18,9,0.06)'/>"
       "</svg>")
uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()

css = """
/* ══ 水墨 WORKS · 國畫長卷 enrich ══ */
[data-theme="chinese"] #pg-works{background:linear-gradient(180deg,#f3ead0,#e6d6b4);background-image:url("__URI__");background-repeat:repeat-x;background-position:0 bottom;background-size:auto 78%}
[data-theme="chinese"] .wg{background:linear-gradient(180deg,rgba(245,236,214,.5),rgba(232,220,192,.5)) !important}
/* silk brocade mounting on each panel */
[data-theme="chinese"] .wi{padding:54px 0 !important;background:linear-gradient(#b9c5b2,#a9b7a2) !important;box-shadow:inset 0 0 0 6px #f5ecd6,inset 0 0 0 8px #8c6a3c !important}
[data-theme="chinese"] .wi a{margin:0 14px;min-height:46vh !important;height:46vh !important;box-shadow:0 0 0 1px rgba(26,18,9,.3)}
[data-theme="chinese"] .wi img{min-height:46vh !important;height:46vh !important}
[data-theme="chinese"] .wi .wio{top:8px;right:6px;padding:.4rem !important}
[data-theme="chinese"] .wi::after{content:'藝';position:absolute;left:12px;bottom:14px;width:30px;height:30px;background:#C0392B;color:#fff;font-family:'Noto Serif TC',serif;font-size:1rem;display:flex;align-items:center;justify-content:center;border-radius:3px;z-index:4;opacity:.9}
/* 引首 opening title panel */
[data-theme="chinese"] .wg::before{content:'武威桀 作品長卷';flex:0 0 46vw;writing-mode:vertical-rl;font-family:'Noto Serif TC',serif;font-weight:700;font-size:clamp(2rem,5vw,3.4rem);color:#1A1209;letter-spacing:.3em;display:flex;align-items:center;justify-content:center;padding:0 3vw;border-right:2px solid rgba(192,57,43,.3);background:linear-gradient(90deg,transparent,rgba(245,236,214,.4));position:relative}
[data-theme="chinese"] .wg::after{content:'丙午年 · 鈐印';flex:0 0 30vw;writing-mode:vertical-rl;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.4rem;color:#8C6A3C;display:flex;align-items:center;justify-content:center;letter-spacing:.2em;border-left:2px solid rgba(192,57,43,.25)}
/* unroll entrance */
[data-theme="chinese"] .wg.unroll .wi{animation:wwcUnroll .7s cubic-bezier(.22,.61,.36,1) backwards}
@keyframes wwcUnroll{from{opacity:0;transform:translateX(60px) scaleX(.6)}to{opacity:1;transform:none}}
"""
css = css.replace('__URI__', uri)
if '國畫長卷 enrich' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('enrich CSS inserted')
else:
    log.append('enrich CSS present')

# JS: parallax mountains on scroll + unroll stagger on chinese activation
js = r"""
<script>
/* ══ 水墨 WORKS 國畫長卷 parallax + unroll ══ */
(function(){
  var bound=null;
  function activate(){
    var g=document.getElementById('grid'); var pg=document.getElementById('pg-works');
    if(!g||!pg) return null;
    function onScroll(){ pg.style.backgroundPositionX=(-g.scrollLeft*0.4)+'px'; }
    g.addEventListener('scroll',onScroll,{passive:true});
    g.classList.add('unroll');
    setTimeout(function(){ var i=0; g.querySelectorAll('.wi').forEach(function(el){ el.style.animationDelay=(i*0.06)+'s'; i++; }); },20);
    setTimeout(function(){ g.classList.remove('unroll'); g.querySelectorAll('.wi').forEach(function(el){el.style.animationDelay='';}); },1600);
    return function(){ g.removeEventListener('scroll',onScroll); pg.style.backgroundPositionX=''; g.classList.remove('unroll'); };
  }
  function sync(t){ if(bound){bound();bound=null;} if(t==='chinese'){ setTimeout(function(){ bound=activate(); },260); } }
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); sync(t); }; }
  window.addEventListener('load',function(){ setTimeout(function(){ sync(localStorage.getItem('wwc-theme')||'default'); },1600); });
})();
</script>
</body>"""
if '國畫長卷 parallax + unroll' not in html:
    html = html.replace('</body>', js, 1)
    log.append('enrich JS inserted')
else:
    log.append('enrich JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)

print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
