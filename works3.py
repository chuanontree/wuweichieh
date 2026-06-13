#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Redesign chinese WORKS into a horizontal ink handscroll (橫卷) with
drag / wheel horizontal scrolling. cyber & y2k works already have distinct
layouts (capsule deck / chrome pods)."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html)
log = []

css = """
/* ══ 水墨 WORKS · horizontal handscroll 橫卷 ══ */
[data-theme="chinese"] #pg-works{background:linear-gradient(#efe4c9,#e3d4b2)}
[data-theme="chinese"] #catBar{background:rgba(243,234,212,.9)}
[data-theme="chinese"] .wg{display:flex !important;flex-wrap:nowrap !important;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x proximity;gap:0 !important;padding:0 64px !important;background:linear-gradient(180deg,#f5ecd6,#e8dcc0) !important;border-top:14px solid #6e4f1d;border-bottom:14px solid #6e4f1d;box-shadow:inset 0 0 50px rgba(110,79,29,.28);cursor:grab;scrollbar-width:none;min-height:64vh;align-items:stretch}
[data-theme="chinese"] .wg::-webkit-scrollbar{display:none}
[data-theme="chinese"] .wg.grabbing{cursor:grabbing}
[data-theme="chinese"] .wi{flex:0 0 300px !important;width:300px !important;height:auto !important;min-height:60vh;scroll-snap-align:center;border:none !important;border-right:1px dashed rgba(192,57,43,.3) !important;border-radius:0 !important;margin:0 !important;background:transparent !important;box-shadow:none !important;aspect-ratio:auto !important;overflow:hidden;position:relative}
[data-theme="chinese"] .wi a{display:block !important;height:100% !important;min-height:60vh}
[data-theme="chinese"] .wi img{width:100% !important;height:100% !important;min-height:60vh;object-fit:cover !important;filter:sepia(22%) contrast(1.05) brightness(.97) !important}
[data-theme="chinese"] .wi .wio{position:absolute;top:0;right:0;bottom:auto;left:auto;width:auto;background:none !important;writing-mode:vertical-rl;padding:1.2rem .6rem !important;transform:none !important}
[data-theme="chinese"] .wi .wt{font-family:'Noto Serif TC',serif;color:#fbf7ee;font-weight:700;text-shadow:0 1px 6px rgba(0,0,0,.6);font-size:1.05rem}
[data-theme="chinese"] .wi .wm{display:none}
[data-theme="chinese"] .wi::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent 70%,rgba(26,18,9,.35));pointer-events:none}
"""
if '水墨 WORKS · horizontal handscroll' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('handscroll CSS inserted')
else:
    log.append('handscroll CSS present')

js = r"""
<script>
/* ══ 水墨 WORKS handscroll drag/wheel ══ */
(function(){
  var off=null;
  function enable(){
    var g=document.getElementById('grid'); if(!g) return null;
    var down=false,sx=0,sl=0;
    function md(e){ down=true; g.classList.add('grabbing'); sx=e.pageX; sl=g.scrollLeft; }
    function mm(e){ if(!down) return; g.scrollLeft = sl-(e.pageX-sx); }
    function mu(){ down=false; g.classList.remove('grabbing'); }
    function wheel(e){ if(Math.abs(e.deltaY)>Math.abs(e.deltaX)){ g.scrollLeft += e.deltaY; e.preventDefault(); } }
    g.addEventListener('mousedown',md); window.addEventListener('mousemove',mm); window.addEventListener('mouseup',mu);
    g.addEventListener('wheel',wheel,{passive:false});
    return function(){ g.removeEventListener('mousedown',md); window.removeEventListener('mousemove',mm); window.removeEventListener('mouseup',mu); g.removeEventListener('wheel',wheel); g.classList.remove('grabbing'); };
  }
  function sync(theme){ if(off){ off(); off=null; } if(theme==='chinese'){ setTimeout(function(){ off=enable(); },200); } }
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); sync(t); }; }
  window.addEventListener('load',function(){ setTimeout(function(){ sync(localStorage.getItem('wwc-theme')||'default'); },1500); });
})();
</script>
</body>"""
if '水墨 WORKS handscroll drag/wheel' not in html:
    html = html.replace('</body>', js, 1)
    log.append('handscroll JS inserted')
else:
    log.append('handscroll JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)

print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
