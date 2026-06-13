#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep batch 3: distinct about/cv layouts + interactions for
brutal (A) / zen (E) / sky (P)."""

with open('index.html','r',encoding='utf-8') as f:
    html=f.read()
orig=len(html); log=[]

css = """
/* ══ DEEP-BATCH-3 (brutal / zen / sky) ══ */

/* ---------- A Brutal: raw offset blocks ---------- */
[data-theme="brutal"] #about{display:grid;grid-template-columns:1fr 1.2fr;gap:2.4rem;max-width:1000px;margin:0 auto;padding:5rem 2rem}
[data-theme="brutal"] #about .al2 img{filter:grayscale(100%) contrast(1.4)!important;border:6px solid #E8FF00;transform:rotate(-1.5deg)}
[data-theme="brutal"] #about .ar .ir{display:flex;flex-direction:column}
[data-theme="brutal"] #about .ir>div{border-bottom:2px solid rgba(240,236,228,.2);padding:.8rem 0;cursor:grab}
[data-theme="brutal"] #about .il{font-family:'Space Mono',monospace;background:#E8FF00;color:#050505;display:inline-block;padding:.1rem .5rem;font-size:.56rem;text-transform:uppercase;letter-spacing:.05em}
[data-theme="brutal"] #about .iv{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.4rem;color:#F0ECE4;margin-top:.35rem}
[data-theme="brutal"] #about .iv#e3{cursor:pointer}
[data-theme="brutal"] #pg-cv{max-width:900px;margin:0 auto;padding:4rem 2rem}
[data-theme="brutal"] .eyr{display:grid !important;grid-template-columns:auto 1fr;gap:1.6rem;border-bottom:2px solid #E8FF00;padding:1.2rem 0;margin:0;width:auto;column-count:auto;align-items:start}
[data-theme="brutal"] .eyr .yl{font-family:'Space Mono',monospace;font-size:2.2rem;font-weight:700;color:#E8FF00;line-height:1;writing-mode:horizontal-tb}
[data-theme="brutal"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="brutal"] .eyr .er{display:flex;justify-content:space-between;padding:.3rem 0;writing-mode:horizontal-tb}
[data-theme="brutal"] .eyr .en{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.3rem;color:#F0ECE4}
[data-theme="brutal"] .eyr .et{font-family:'Space Mono',monospace;font-size:.68rem;color:#888}
[data-theme="brutal"] #about,[data-theme="brutal"] #pg-cv{cursor:crosshair}

/* ---------- E Zen: ultra-minimal centered ---------- */
[data-theme="zen"] #about{display:block;max-width:560px;margin:0 auto;padding:7rem 2rem;text-align:center}
[data-theme="zen"] #about .al2{margin:0 auto 3rem;width:160px}
[data-theme="zen"] #about .al2 img{border-radius:50%;filter:grayscale(100%)!important;opacity:.92}
[data-theme="zen"] #about .ar .ir{display:flex;flex-direction:column;gap:2rem}
[data-theme="zen"] #about .il{font-family:'EB Garamond',serif;color:#9B8E82;font-size:.68rem;letter-spacing:.35em;text-transform:uppercase;margin-bottom:.5rem}
[data-theme="zen"] #about .iv{font-family:'EB Garamond',serif;color:#0D0D0D;font-size:1.2rem;line-height:1.8}
[data-theme="zen"] #pg-cv{max-width:520px;margin:0 auto;padding:6rem 2rem;text-align:center}
[data-theme="zen"] .eyr{display:block !important;margin-bottom:3.5rem;width:auto;column-count:auto;position:relative}
[data-theme="zen"] .eyr::before{content:'';display:block;width:8px;height:8px;border-radius:50%;background:#9B8E82;margin:0 auto 1.2rem;animation:zenBreath 4s ease-in-out infinite}
[data-theme="zen"] .eyr .yl{font-family:'EB Garamond',serif;color:#9B8E82;font-size:.8rem;letter-spacing:.3em;margin-bottom:1rem;writing-mode:horizontal-tb}
[data-theme="zen"] .eyr .yi{display:flex;flex-direction:column;gap:.6rem}
[data-theme="zen"] .eyr .er{display:block;padding:.3rem 0;writing-mode:horizontal-tb}
[data-theme="zen"] .eyr .en{font-family:'EB Garamond',serif;color:#0D0D0D;font-size:1.15rem}
[data-theme="zen"] .eyr .et{font-family:'EB Garamond',serif;color:#9B8E82;font-style:italic;font-size:.85rem}
@keyframes zenBreath{0%,100%{transform:scale(1);opacity:.45}50%{transform:scale(1.9);opacity:1}}
.wwc-enso{position:fixed;border:3px solid rgba(13,13,13,.45);border-radius:50%;pointer-events:none;z-index:9998;animation:ensoExpand 1s ease-out forwards}
@keyframes ensoExpand{from{width:10px;height:10px;opacity:.8;transform:translate(-50%,-50%)}to{width:170px;height:170px;opacity:0;transform:translate(-50%,-50%)}}

/* ---------- P Sky: floating glass cards (parallax tilt) ---------- */
[data-theme="sky"] #about{display:grid;grid-template-columns:280px 1fr;gap:3rem;max-width:980px;margin:0 auto;padding:5rem 2rem;perspective:900px}
[data-theme="sky"] #about .al2 img{border-radius:30px;border:6px solid #fff;box-shadow:0 20px 50px rgba(143,184,222,.5)}
[data-theme="sky"] #about .ar .ir{display:flex;flex-wrap:wrap;gap:1rem}
[data-theme="sky"] #about .ir>div{flex:1 1 200px;background:rgba(255,255,255,.7);backdrop-filter:blur(8px);border:1px solid #fff;border-radius:20px;padding:1rem 1.2rem;box-shadow:0 12px 30px rgba(143,184,222,.35);transition:transform .15s ease-out;transform-style:preserve-3d}
[data-theme="sky"] #about .il{font-family:'DM Sans',sans-serif;color:#FF9E5E;font-size:.6rem;letter-spacing:.1em;font-weight:700;margin-bottom:.3rem}
[data-theme="sky"] #about .iv{font-family:'DM Sans',sans-serif;color:#243446;font-size:1rem;font-weight:600}
[data-theme="sky"] #pg-cv{max-width:720px;margin:0 auto;padding:5rem 2rem}
[data-theme="sky"] .eyr{display:flex !important;align-items:center;gap:1.5rem;background:rgba(255,255,255,.78);backdrop-filter:blur(8px);border-radius:40px;padding:1.2rem 2rem;margin-bottom:1.6rem;box-shadow:0 14px 36px rgba(143,184,222,.4);width:auto;column-count:auto;animation:skyFloat 7s ease-in-out infinite}
[data-theme="sky"] .eyr:nth-child(2n){animation-delay:-2.5s}
[data-theme="sky"] .eyr:nth-child(3n){animation-delay:-4s}
[data-theme="sky"] .eyr .yl{font-family:'DM Sans',sans-serif;font-weight:700;color:#8FB8DE;font-size:1.2rem;background:rgba(143,184,222,.15);border-radius:30px;padding:.4rem 1.1rem;writing-mode:horizontal-tb}
[data-theme="sky"] .eyr .yi{flex:1;display:flex;flex-direction:column;gap:.3rem}
[data-theme="sky"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="sky"] .eyr .en{font-family:'DM Sans',sans-serif;color:#243446;font-weight:600}
[data-theme="sky"] .eyr .et{font-family:'DM Sans',sans-serif;color:#FF9E5E;font-size:.8rem}
.wwc-cloud{position:fixed;pointer-events:none;z-index:9998;font-size:2.2rem;animation:cloudUp 3s ease-out forwards}
@keyframes cloudUp{from{opacity:.95;transform:translateY(0) scale(.6)}to{opacity:0;transform:translateY(-220px) scale(1.2)}}
"""
if 'DEEP-BATCH-3' not in html:
    ls=html.rfind('</style>'); html=html[:ls]+css+html[ls:]; log.append('CSS inserted')
else: log.append('CSS present')

js = r"""
<script>
/* ══ DEEP-BATCH-3 INTERACTIONS (brutal/zen/sky) ══ */
(function(){
  var fx=null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  function toast(msg,color){ var t=document.getElementById('wwcToast');
    if(!t){t=document.createElement('div');t.id='wwcToast';document.body.appendChild(t);}
    t.textContent=msg; if(color)t.style.background=color; t.classList.add('show');
    clearTimeout(t._h); t._h=setTimeout(function(){t.classList.remove('show');},1800); }

  /* A brutal: draggable blocks + name redact */
  function brutal(){
    var drags=[],name=document.getElementById('e3');
    function redact(){ if(!name||name._b)return; name._b=true; var real=name.getAttribute('data-r')||name.textContent; name.setAttribute('data-r',real);
      name.textContent=real.replace(/\S/g,'█'); toast('[ CLASSIFIED ]','#E8FF00');
      var t=document.getElementById('wwcToast'); if(t)t.style.color='#050505';
      setTimeout(function(){ name.textContent=real; name._b=false; if(t)t.style.color=''; },1100); }
    if(name)name.addEventListener('click',redact);
    if(window.Draggable){ try{ drags=Draggable.create('[data-theme="brutal"] #about .ir > div',{type:'x,y',onPress:function(){this.target.style.cursor='grabbing';},onRelease:function(){this.target.style.cursor='grab';}}); }catch(e){} }
    fx=function(){ if(name)name.removeEventListener('click',redact); (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); document.querySelectorAll('#about .ir > div').forEach(function(el){el.style.transform='';}); };
  }
  /* E zen: ensō ripple on click */
  function zen(){
    function clk(e){ var o=document.createElement('div'); o.className='wwc-enso'; o.style.left=e.clientX+'px'; o.style.top=e.clientY+'px'; document.body.appendChild(o); setTimeout(function(){o.remove();},1000); }
    document.addEventListener('click',clk);
    fx=function(){ document.removeEventListener('click',clk); };
  }
  /* P sky: parallax tilt on about cards + cloud release on click */
  function sky(){
    var about=document.getElementById('about');
    function mv(e){ if(!about)return; var cards=about.querySelectorAll('.ir > div'); var cx=innerWidth/2,cy=innerHeight/2; var rx=(e.clientY-cy)/cy*-6, ry=(e.clientX-cx)/cx*6;
      cards.forEach(function(c){ c.style.transform='rotateX('+rx+'deg) rotateY('+ry+'deg)'; }); }
    addEventListener('mousemove',mv);
    function clk(e){ var c=document.createElement('div'); c.className='wwc-cloud'; c.textContent=Math.random()<.5?'☁':'✨'; c.style.left=e.clientX+'px'; c.style.top=e.clientY+'px'; document.body.appendChild(c); setTimeout(function(){c.remove();},3000); }
    document.addEventListener('click',clk);
    fx=function(){ removeEventListener('mousemove',mv); document.removeEventListener('click',clk); if(about)about.querySelectorAll('.ir > div').forEach(function(c){c.style.transform='';}); };
  }
  window.initBatch3=function(theme){ teardown();
    if(theme==='brutal')brutal(); else if(theme==='zen')zen(); else if(theme==='sky')sky(); };
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); setTimeout(function(){ try{initBatch3(t);}catch(e){} },200); }; }
  addEventListener('load',function(){ setTimeout(function(){ try{initBatch3(localStorage.getItem('wwc-theme')||'default');}catch(e){} },1550); });
})();
</script>
</body>"""
if 'DEEP-BATCH-3 INTERACTIONS' not in html:
    html=html.replace('</body>',js,1); log.append('JS inserted')
else: log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
