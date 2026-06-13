#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep batch 5 (final): distinct about/cv layouts + interactions for
iso (F) / crystal (Q)."""

with open('index.html','r',encoding='utf-8') as f:
    html=f.read()
orig=len(html); log=[]

css = """
/* ══ DEEP-BATCH-5 (iso / crystal) ══ */

/* ---------- F Iso: isometric extruded blocks on grid ---------- */
[data-theme="iso"] #about{max-width:920px;margin:0 auto;padding:5rem 2rem;display:grid;grid-template-columns:260px 1fr;gap:3rem;background-image:linear-gradient(rgba(110,133,168,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(110,133,168,.12) 1px,transparent 1px);background-size:40px 40px}
[data-theme="iso"] #about .al2 img{border:2px solid #1B4FFF;box-shadow:12px 12px 0 rgba(27,79,255,.4);transform:rotate(-1deg)}
[data-theme="iso"] #about .ar .ir{display:flex;flex-direction:column;gap:1rem}
[data-theme="iso"] #about .ir>div{background:#13283f;border:1px solid #1B4FFF;padding:.8rem 1rem;box-shadow:7px 7px 0 rgba(27,79,255,.35);transition:transform .25s,box-shadow .25s;cursor:grab}
[data-theme="iso"] #about .ir>div:hover{transform:translate(-4px,-4px);box-shadow:11px 11px 0 rgba(27,79,255,.5)}
[data-theme="iso"] #about .il{font-family:'Syncopate',sans-serif;color:#6E85A8;font-size:.56rem;letter-spacing:.1em;text-transform:uppercase}
[data-theme="iso"] #about .iv{font-family:'Rajdhani',sans-serif;color:#fff;font-size:1.05rem;font-weight:600}
[data-theme="iso"] #pg-cv{max-width:820px;margin:0 auto;padding:4rem 2rem;background-image:linear-gradient(rgba(110,133,168,.1) 1px,transparent 1px),linear-gradient(90deg,rgba(110,133,168,.1) 1px,transparent 1px);background-size:40px 40px}
[data-theme="iso"] .eyr{display:grid !important;grid-template-columns:120px 1fr;gap:1.5rem;background:#13283f;border:1px solid #1B4FFF;box-shadow:9px 9px 0 rgba(27,79,255,.3);margin-bottom:1.6rem;padding:1.2rem 1.4rem;width:auto;column-count:auto;transition:transform .25s}
[data-theme="iso"] .eyr:hover{transform:translate(-5px,-5px)}
[data-theme="iso"] .eyr .yl{font-family:'Syncopate',sans-serif;color:#1B4FFF;font-size:.9rem;writing-mode:horizontal-tb}
[data-theme="iso"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="iso"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb;border-bottom:1px solid rgba(255,255,255,.1);padding:.2rem 0}
[data-theme="iso"] .eyr .en{font-family:'Rajdhani',sans-serif;color:#fff;font-weight:600}
[data-theme="iso"] .eyr .et{font-family:'Rajdhani',sans-serif;color:#6E85A8;font-size:.82rem}

/* ---------- Q Crystal: faceted glass shards ---------- */
[data-theme="crystal"] #about{max-width:960px;margin:0 auto;padding:5rem 2rem;display:grid;grid-template-columns:280px 1fr;gap:3rem}
[data-theme="crystal"] #about .al2 img{clip-path:polygon(50% 0,100% 38%,82% 100%,18% 100%,0 38%);border:none}
[data-theme="crystal"] #about .ar .ir{display:flex;flex-wrap:wrap;gap:1rem}
[data-theme="crystal"] #about .ir>div{flex:1 1 200px;clip-path:polygon(0 0,100% 8%,100% 100%,0 92%);background:rgba(255,255,255,.4);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.7);padding:1.1rem 1.3rem;box-shadow:0 8px 26px rgba(160,107,255,.25);position:relative;overflow:hidden}
[data-theme="crystal"] #about .ir>div::after{content:'';position:absolute;inset:0;background:linear-gradient(120deg,transparent 40%,rgba(255,255,255,.7) 50%,transparent 60%);transform:translateX(-120%);transition:transform .7s}
[data-theme="crystal"] #about .ir>div:hover::after{transform:translateX(120%)}
[data-theme="crystal"] #about .il{font-family:'DM Sans',sans-serif;color:#a06bff;font-size:.6rem;letter-spacing:.1em;font-weight:700;margin-bottom:.3rem}
[data-theme="crystal"] #about .iv{font-family:'DM Sans',sans-serif;color:#2a2350;font-size:1rem;font-weight:600}
[data-theme="crystal"] #pg-cv{max-width:760px;margin:0 auto;padding:5rem 2rem}
[data-theme="crystal"] .eyr{display:grid !important;grid-template-columns:120px 1fr;gap:1.5rem;clip-path:polygon(0 6%,100% 0,100% 94%,0 100%);background:rgba(255,255,255,.45);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.7);box-shadow:0 10px 30px rgba(160,107,255,.25);margin-bottom:1.4rem;padding:1.3rem 1.6rem;width:auto;column-count:auto}
[data-theme="crystal"] .eyr .yl{font-family:'DM Sans',sans-serif;font-weight:700;background:linear-gradient(90deg,#a06bff,#6bd5ff);-webkit-background-clip:text;background-clip:text;color:transparent;font-size:1.3rem;writing-mode:horizontal-tb}
[data-theme="crystal"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="crystal"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="crystal"] .eyr .en{font-family:'DM Sans',sans-serif;color:#2a2350;font-weight:600}
[data-theme="crystal"] .eyr .et{font-family:'DM Sans',sans-serif;color:#a06bff;font-size:.8rem}
.wwc-prism{position:fixed;width:9px;height:9px;pointer-events:none;z-index:9998;border-radius:50%;animation:prismFade .9s ease-out forwards}
@keyframes prismFade{from{opacity:.9;transform:scale(1)}to{opacity:0;transform:scale(2.4) translateY(-30px)}}
"""
if 'DEEP-BATCH-5' not in html:
    ls=html.rfind('</style>'); html=html[:ls]+css+html[ls:]; log.append('CSS inserted')
else: log.append('CSS present')

js = r"""
<script>
/* ══ DEEP-BATCH-5 INTERACTIONS (iso/crystal) ══ */
(function(){
  var fx=null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  /* F iso: draggable blocks + grid parallax */
  function iso(){
    var drags=[],about=document.getElementById('about'),cv=document.getElementById('pg-cv');
    function mv(e){ var px=(e.clientX/innerWidth-.5)*30, py=(e.clientY/innerHeight-.5)*30;
      if(about)about.style.backgroundPosition=px+'px '+py+'px'; if(cv)cv.style.backgroundPosition=px+'px '+py+'px'; }
    addEventListener('mousemove',mv);
    if(window.Draggable){ try{ drags=Draggable.create('[data-theme="iso"] #about .ir > div',{type:'x,y',onPress:function(){this.target.style.cursor='grabbing';this.target.style.zIndex=70;},onRelease:function(){this.target.style.cursor='grab';}}); }catch(e){} }
    fx=function(){ removeEventListener('mousemove',mv); if(about)about.style.backgroundPosition=''; if(cv)cv.style.backgroundPosition=''; (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); document.querySelectorAll('#about .ir > div').forEach(function(el){el.style.transform='';}); };
  }
  /* Q crystal: prism rainbow cursor + shatter sparkle on click */
  function crystal(){
    var last=0,hue=0;
    function mv(e){ var now=Date.now(); if(now-last<24)return; last=now; hue=(hue+40)%360;
      var p=document.createElement('div'); p.className='wwc-prism'; p.style.background='hsl('+hue+',90%,65%)'; p.style.left=e.clientX+'px'; p.style.top=e.clientY+'px';
      document.body.appendChild(p); setTimeout(function(){p.remove();},900); }
    addEventListener('mousemove',mv);
    function clk(e){ for(var i=0;i<12;i++){ var p=document.createElement('div'); p.className='wwc-prism'; p.style.background='hsl('+(i*30)+',90%,65%)';
      var a=i/12*Math.PI*2,d=40+Math.random()*40; p.style.left=(e.clientX+Math.cos(a)*d)+'px'; p.style.top=(e.clientY+Math.sin(a)*d)+'px';
      document.body.appendChild(p); (function(el){setTimeout(function(){el.remove();},900);})(p); } }
    document.addEventListener('click',clk);
    fx=function(){ removeEventListener('mousemove',mv); document.removeEventListener('click',clk); };
  }
  window.initBatch5=function(theme){ teardown();
    if(theme==='iso')iso(); else if(theme==='crystal')crystal(); };
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); setTimeout(function(){ try{initBatch5(t);}catch(e){} },240); }; }
  addEventListener('load',function(){ setTimeout(function(){ try{initBatch5(localStorage.getItem('wwc-theme')||'default');}catch(e){} },1650); });
})();
</script>
</body>"""
if 'DEEP-BATCH-5 INTERACTIONS' not in html:
    html=html.replace('</body>',js,1); log.append('JS inserted')
else: log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
