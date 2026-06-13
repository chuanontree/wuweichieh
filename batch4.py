#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep batch 4: distinct about/cv layouts + interactions for
luxury (B) / apple (H) / bauhaus (K)."""

with open('index.html','r',encoding='utf-8') as f:
    html=f.read()
orig=len(html); log=[]

css = """
/* ══ DEEP-BATCH-4 (luxury / apple / bauhaus) ══ */

/* ---------- B Luxury: gold editorial ---------- */
[data-theme="luxury"] #about{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;max-width:980px;margin:0 auto;padding:5.5rem 2rem}
[data-theme="luxury"] #about .al2 img{border:1px solid #C9A96E;padding:10px;background:#0A0806;box-shadow:0 20px 50px rgba(0,0,0,.6)}
[data-theme="luxury"] #about .ar{align-self:center}
[data-theme="luxury"] #about .ir>div{border-bottom:1px solid rgba(201,169,110,.25);padding:1rem 0}
[data-theme="luxury"] #about .il{font-family:'Playfair Display',serif;color:#C9A96E;font-size:.62rem;letter-spacing:.3em;text-transform:uppercase;margin-bottom:.4rem}
[data-theme="luxury"] #about .iv{font-family:'Playfair Display',serif;color:#EDE8DE;font-size:1.25rem;font-style:italic}
[data-theme="luxury"] #pg-cv{max-width:820px;margin:0 auto;padding:5rem 2rem}
[data-theme="luxury"] .eyr{display:grid !important;grid-template-columns:140px 1fr;gap:2rem;border-bottom:1px solid rgba(201,169,110,.25);padding:1.6rem 0;margin:0;width:auto;column-count:auto;align-items:baseline}
[data-theme="luxury"] .eyr .yl{font-family:'Playfair Display',serif;color:#C9A96E;font-size:1.4rem;font-style:italic;writing-mode:horizontal-tb;text-align:right}
[data-theme="luxury"] .eyr .yi{display:flex;flex-direction:column;gap:.5rem}
[data-theme="luxury"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="luxury"] .eyr .en{font-family:'Playfair Display',serif;color:#EDE8DE;font-size:1.1rem}
[data-theme="luxury"] .eyr .et{font-family:'Cormorant Garamond',serif;font-style:italic;color:#9a8f7d}
#wwcLuxGlow{position:fixed;width:320px;height:320px;border-radius:50%;background:radial-gradient(circle,rgba(201,169,110,.16),transparent 70%);pointer-events:none;z-index:53;transform:translate(-50%,-50%);will-change:left,top}

/* ---------- H Apple: clean product spec ---------- */
[data-theme="apple"] #about{max-width:720px;margin:0 auto;padding:6rem 2rem;text-align:center}
[data-theme="apple"] #about .al2{margin:0 auto 2.5rem;width:200px}
[data-theme="apple"] #about .al2 img{border-radius:24px;box-shadow:0 30px 60px rgba(0,0,0,.18);transition:transform .15s ease-out}
[data-theme="apple"] #about .ar .ir{display:flex;flex-direction:column;gap:0;text-align:left;max-width:540px;margin:0 auto}
[data-theme="apple"] #about .ir>div{display:grid;grid-template-columns:140px 1fr;gap:1.5rem;padding:1.1rem 0;border-bottom:1px solid rgba(29,29,31,.1)}
[data-theme="apple"] #about .ir>div.wwc-rise{animation:appleRise .6s cubic-bezier(.16,1,.3,1) both}
[data-theme="apple"] #about .il{font-family:'DM Sans',sans-serif;color:#86868B;font-size:.85rem;font-weight:600}
[data-theme="apple"] #about .iv{font-family:'DM Sans',sans-serif;color:#1D1D1F;font-size:1.05rem;font-weight:600}
[data-theme="apple"] #about .iv a{color:#0071E3}
@keyframes appleRise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
[data-theme="apple"] #pg-cv{max-width:680px;margin:0 auto;padding:6rem 2rem}
[data-theme="apple"] .eyr{display:block !important;text-align:center;margin-bottom:4rem;width:auto;column-count:auto}
[data-theme="apple"] .eyr .yl{font-family:'DM Sans',sans-serif;color:#1D1D1F;font-size:2.4rem;font-weight:700;letter-spacing:-.02em;margin-bottom:1rem;writing-mode:horizontal-tb}
[data-theme="apple"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="apple"] .eyr .er{display:block;padding:.4rem 0;writing-mode:horizontal-tb}
[data-theme="apple"] .eyr .en{font-family:'DM Sans',sans-serif;color:#1D1D1F;font-size:1.2rem;font-weight:600}
[data-theme="apple"] .eyr .et{font-family:'DM Sans',sans-serif;color:#86868B;font-size:.9rem}

/* ---------- K Bauhaus: geometric primary blocks ---------- */
[data-theme="bauhaus"] #about{display:grid;grid-template-columns:1fr 1fr;gap:0;max-width:1000px;margin:0 auto;padding:4rem 2rem;border:4px solid #000}
[data-theme="bauhaus"] #about .al2{border-right:4px solid #000;padding:1.5rem;background:#FFD500}
[data-theme="bauhaus"] #about .al2 img{border:4px solid #000}
[data-theme="bauhaus"] #about .ar{padding:1.5rem}
[data-theme="bauhaus"] #about .ir>div{display:grid;grid-template-columns:130px 1fr;gap:1rem;padding:.7rem 0;border-bottom:3px solid #000;align-items:center}
[data-theme="bauhaus"] #about .il{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;font-size:.7rem;text-transform:uppercase}
[data-theme="bauhaus"] #about .il::before{content:'';display:inline-block;width:12px;height:12px;background:#E63329;border-radius:50%;margin-right:.5rem;vertical-align:middle}
[data-theme="bauhaus"] #about .ir>div:nth-child(2n) .il::before{background:#0F5EAD;border-radius:0}
[data-theme="bauhaus"] #about .ir>div:nth-child(3n) .il::before{background:#FFD500;border-radius:0;clip-path:polygon(50% 0,100% 100%,0 100%)}
[data-theme="bauhaus"] #about .iv{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;font-size:1rem}
[data-theme="bauhaus"] #pg-cv{max-width:900px;margin:0 auto;padding:4rem 2rem}
[data-theme="bauhaus"] .eyr{display:grid !important;grid-template-columns:120px 1fr;gap:1.5rem;border:4px solid #000;margin-bottom:1.2rem;padding:1.2rem;width:auto;column-count:auto;align-items:start}
[data-theme="bauhaus"] .eyr:nth-child(3n+1){background:#FFD500}
[data-theme="bauhaus"] .eyr:nth-child(3n+2){background:#fff}
[data-theme="bauhaus"] .eyr:nth-child(3n){background:#0F5EAD}
[data-theme="bauhaus"] .eyr:nth-child(3n) .en,[data-theme="bauhaus"] .eyr:nth-child(3n) .yl,[data-theme="bauhaus"] .eyr:nth-child(3n) .et{color:#fff}
[data-theme="bauhaus"] .eyr .yl{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;font-size:1.6rem;writing-mode:horizontal-tb}
[data-theme="bauhaus"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="bauhaus"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="bauhaus"] .eyr .en{font-family:'DM Sans',sans-serif;font-weight:700;color:#000}
[data-theme="bauhaus"] .eyr .et{font-family:'DM Sans',sans-serif;color:#000;font-size:.8rem}
.wwc-shape{position:fixed;pointer-events:none;z-index:9998;width:20px;height:20px;animation:shapeFly 1.2s ease-out forwards}
@keyframes shapeFly{from{opacity:1;transform:translate(0,0) rotate(0)}to{opacity:0;transform:translate(var(--dx),var(--dy)) rotate(360deg)}}
"""
if 'DEEP-BATCH-4' not in html:
    ls=html.rfind('</style>'); html=html[:ls]+css+html[ls:]; log.append('CSS inserted')
else: log.append('CSS present')

js = r"""
<script>
/* ══ DEEP-BATCH-4 INTERACTIONS (luxury/apple/bauhaus) ══ */
(function(){
  var fx=null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  function toast(msg,color){ var t=document.getElementById('wwcToast');
    if(!t){t=document.createElement('div');t.id='wwcToast';document.body.appendChild(t);}
    t.textContent=msg; if(color)t.style.background=color; t.classList.add('show');
    clearTimeout(t._h); t._h=setTimeout(function(){t.classList.remove('show');},1800); }

  /* B luxury: gold glow cursor + click flourish */
  function luxury(){
    var g=document.createElement('div'); g.id='wwcLuxGlow'; document.body.appendChild(g);
    function mv(e){ g.style.left=e.clientX+'px'; g.style.top=e.clientY+'px'; }
    addEventListener('mousemove',mv);
    function clk(e){ if(e.target.closest('#about .al2 img')) toast('✦ Exquisite ✦','#C9A96E'); }
    document.addEventListener('click',clk);
    fx=function(){ removeEventListener('mousemove',mv); document.removeEventListener('click',clk); g.remove(); };
  }
  /* H apple: scroll-rise reveal + magnetic portrait */
  function apple(){
    var io=null, about=document.getElementById('about');
    if('IntersectionObserver' in window){
      io=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('wwc-rise'); } }); },{threshold:.2});
      document.querySelectorAll('[data-theme="apple"] #about .ir > div').forEach(function(el){ io.observe(el); });
    }
    var img=about?about.querySelector('.al2 img'):null;
    function mv(e){ if(!img)return; var r=img.getBoundingClientRect(); var dx=(e.clientX-(r.left+r.width/2))/30, dy=(e.clientY-(r.top+r.height/2))/30; img.style.transform='translate('+Math.max(-12,Math.min(12,dx))+'px,'+Math.max(-12,Math.min(12,dy))+'px)'; }
    addEventListener('mousemove',mv);
    fx=function(){ if(io)io.disconnect(); removeEventListener('mousemove',mv); if(img)img.style.transform=''; document.querySelectorAll('#about .ir > div').forEach(function(el){el.classList.remove('wwc-rise');}); };
  }
  /* K bauhaus: draggable rows + shape burst */
  function bauhaus(){
    var drags=[];
    if(window.Draggable){ try{ drags=Draggable.create('[data-theme="bauhaus"] #pg-cv .eyr',{type:'x,y',onPress:function(){this.target.style.zIndex=70;}}); }catch(e){} }
    function burst(e){ if(!e.target.closest('#about .al2 img')) return;
      var cols=['#E63329','#0F5EAD','#FFD500']; for(var i=0;i<10;i++){ var s=document.createElement('div'); s.className='wwc-shape';
        var k=i%3; s.style.background=cols[k]; if(k===0)s.style.borderRadius='50%'; else if(k===2){s.style.background='transparent';s.style.borderLeft='10px solid transparent';s.style.borderRight='10px solid transparent';s.style.borderBottom='20px solid #FFD500';s.style.width='0';s.style.height='0';}
        s.style.left=e.clientX+'px'; s.style.top=e.clientY+'px';
        s.style.setProperty('--dx',((Math.random()-.5)*300)+'px'); s.style.setProperty('--dy',((Math.random()-.5)*300)+'px');
        document.body.appendChild(s); (function(el){setTimeout(function(){el.remove();},1200);})(s); } }
    document.addEventListener('click',burst);
    fx=function(){ (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); document.querySelectorAll('#pg-cv .eyr').forEach(function(el){el.style.transform='';}); document.removeEventListener('click',burst); };
  }
  window.initBatch4=function(theme){ teardown();
    if(theme==='luxury')luxury(); else if(theme==='apple')apple(); else if(theme==='bauhaus')bauhaus(); };
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); setTimeout(function(){ try{initBatch4(t);}catch(e){} },220); }; }
  addEventListener('load',function(){ setTimeout(function(){ try{initBatch4(localStorage.getItem('wwc-theme')||'default');}catch(e){} },1600); });
})();
</script>
</body>"""
if 'DEEP-BATCH-4 INTERACTIONS' not in html:
    html=html.replace('</body>',js,1); log.append('JS inserted')
else: log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
