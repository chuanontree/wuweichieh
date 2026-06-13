#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep batch 2: distinct about/cv layouts + interactions for
baroque (J) / newspaper (M) / medieval (O). Independent JS module."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html); log = []

css = """
/* ══ DEEP-BATCH-2 (baroque / newspaper / medieval) ══ */

/* ---------- J Baroque: gilded portrait + brass plaques ---------- */
[data-theme="baroque"] #about{display:grid;grid-template-columns:300px 1fr;gap:3rem;max-width:960px;margin:0 auto;padding:5rem 2rem;position:relative}
[data-theme="baroque"] #about::before{content:'\\2766';position:absolute;top:1.6rem;left:50%;transform:translateX(-50%);color:#C9922A;font-size:2rem}
[data-theme="baroque"] #about .al2 img{border:14px solid transparent;border-image:linear-gradient(135deg,#e7c45a,#9c6b1f,#f3df9b,#7a4e12) 1;box-shadow:0 0 0 2px #1A0A0E,0 16px 50px rgba(0,0,0,.6);filter:sepia(20%) contrast(1.05)}
[data-theme="baroque"] #about .ar .ir{display:flex;flex-direction:column;gap:.7rem}
[data-theme="baroque"] #about .ir>div{display:grid;grid-template-columns:140px 1fr;gap:1rem;padding:.7rem 1rem;background:linear-gradient(#241016,#1a0c10);border:1px solid #C9922A;border-radius:4px;box-shadow:inset 0 0 14px rgba(201,146,42,.15)}
[data-theme="baroque"] #about .il{font-family:'Cinzel Decorative',serif;color:#C9922A;font-size:.68rem;letter-spacing:.12em}
[data-theme="baroque"] #about .iv{font-family:'Cormorant Garamond',serif;color:#F5EDD6;font-size:1.05rem}
[data-theme="baroque"] #pg-cv{max-width:820px;margin:0 auto;padding:4rem 2rem}
[data-theme="baroque"] .eyr{display:grid !important;grid-template-columns:90px 1fr;gap:1.4rem;background:linear-gradient(#241016,#1a0c10);border:1px solid rgba(201,146,42,.4);border-left:4px solid #C9922A;border-radius:4px;margin-bottom:1.2rem;padding:1.2rem 1.4rem;align-items:start;width:auto;column-count:auto}
[data-theme="baroque"] .eyr .yl{font-family:'Cinzel Decorative',serif;color:#1A0A0E;background:radial-gradient(circle,#f3df9b,#C9922A);border-radius:50%;width:74px;height:74px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:.66rem;box-shadow:0 4px 14px rgba(0,0,0,.5);writing-mode:horizontal-tb}
[data-theme="baroque"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="baroque"] .eyr .er{border-bottom:1px dotted rgba(201,146,42,.3);padding:.3rem 0;display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="baroque"] .eyr .en{font-family:'Cormorant Garamond',serif;color:#F5EDD6;font-size:1.05rem}
[data-theme="baroque"] .eyr .et{font-family:'Cormorant Garamond',serif;font-style:italic;color:#C9922A}
#wwcGoldCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:55}

/* ---------- M Newspaper: front-page article + classified cv ---------- */
[data-theme="newspaper"] #about{max-width:920px;margin:0 auto;padding:3rem 2rem;display:block}
[data-theme="newspaper"] #about::before{content:'THE WU WEI CHIEH TIMES \\2014 EST. 2000';display:block;text-align:center;font-family:'Playfair Display',serif;font-weight:700;letter-spacing:.08em;font-size:1.3rem;border-top:4px double #0A0A0A;border-bottom:3px double #0A0A0A;padding:.5rem 0;margin-bottom:1.4rem;color:#0A0A0A}
[data-theme="newspaper"] #about .al2{float:left;width:230px;margin:0 1.6rem 1rem 0}
[data-theme="newspaper"] #about .al2 img{filter:grayscale(100%) contrast(1.25)!important;border:1px solid #0A0A0A}
[data-theme="newspaper"] #about .al2 .ig,[data-theme="newspaper"] #about .al2 a{font-family:monospace;font-size:.62rem;color:#333}
[data-theme="newspaper"] #about .ar{columns:2;column-gap:1.6rem;column-rule:1px solid #0A0A0A}
[data-theme="newspaper"] #about .ir>div{break-inside:avoid;margin-bottom:.7rem}
[data-theme="newspaper"] #about .il{font-family:'Playfair Display',serif;font-weight:700;color:#CC0000;font-size:.68rem;text-transform:uppercase;letter-spacing:.04em}
[data-theme="newspaper"] #about .iv{font-family:'Source Serif 4',serif;color:#0A0A0A;font-size:.92rem;line-height:1.5}
[data-theme="newspaper"] #about .iv#e3{cursor:pointer;font-weight:700}
[data-theme="newspaper"] #pg-cv{max-width:860px;margin:0 auto;padding:4rem 2rem}
[data-theme="newspaper"] .eyr{display:block !important;border-bottom:2px solid #0A0A0A;padding:.6rem 0 1rem;margin:0 0 1rem;width:auto;column-count:auto}
[data-theme="newspaper"] .eyr .yl{font-family:'Playfair Display',serif;font-weight:700;color:#CC0000;font-size:1.05rem;border-bottom:1px solid #0A0A0A;display:block;margin-bottom:.5rem;writing-mode:horizontal-tb}
[data-theme="newspaper"] .eyr .er{display:flex;justify-content:space-between;align-items:baseline;font-family:'Source Serif 4',serif;border-bottom:1px dotted #aaa;padding:.25rem 0;writing-mode:horizontal-tb}
[data-theme="newspaper"] .eyr .en{color:#0A0A0A;font-weight:600}
[data-theme="newspaper"] .eyr .et{color:#666;font-family:monospace;font-size:.74rem}
.wwc-stamp{position:fixed;font-family:'Playfair Display',serif;font-weight:700;color:#CC0000;border:4px solid #CC0000;padding:.3rem 1rem;font-size:2rem;letter-spacing:.1em;transform:rotate(-12deg);z-index:9999;pointer-events:none;border-radius:6px;animation:stampIn .4s cubic-bezier(.34,1.8,.64,1)}
@keyframes stampIn{from{transform:rotate(-12deg) scale(2);opacity:0}to{transform:rotate(-12deg) scale(1);opacity:1}}

/* ---------- O Medieval: illuminated codex + stone tablets ---------- */
[data-theme="medieval"] #about{display:grid;grid-template-columns:240px 1fr;gap:2.5rem;max-width:920px;margin:0 auto;padding:4rem 2.5rem;background:linear-gradient(#15140f,#0d0d0d);border:1px solid #8C6A3C;box-shadow:inset 0 0 60px rgba(0,0,0,.7)}
[data-theme="medieval"] #about .al2 img{clip-path:polygon(0 0,100% 0,100% 68%,50% 100%,0 68%);border:none !important;filter:grayscale(45%) sepia(25%) contrast(1.1)}
[data-theme="medieval"] #about .ar .ir{display:flex;flex-direction:column;gap:.5rem}
[data-theme="medieval"] #about .ir>div{display:grid;grid-template-columns:150px 1fr;gap:1rem;border-bottom:1px solid rgba(140,106,60,.3);padding:.6rem 0}
[data-theme="medieval"] #about .il{font-family:'UnifrakturMaguntia',cursive;color:#8C6A3C;font-size:1.05rem}
[data-theme="medieval"] #about .iv{font-family:'IM Fell English',serif;color:#C0C0C0;font-size:1rem}
[data-theme="medieval"] #pg-cv{max-width:820px;margin:0 auto;padding:4rem 2rem}
[data-theme="medieval"] .eyr{display:grid !important;grid-template-columns:90px 1fr;gap:1.2rem;background:linear-gradient(#1a1a17,#111);border:1px solid #555;border-left:5px solid #8C6A3C;box-shadow:inset 0 0 22px rgba(0,0,0,.8),0 4px 10px rgba(0,0,0,.5);margin-bottom:1rem;padding:1rem 1.4rem;width:auto;column-count:auto}
[data-theme="medieval"] .eyr .yl{font-family:'UnifrakturMaguntia',cursive;color:#8C6A3C;font-size:1.4rem;writing-mode:horizontal-tb}
[data-theme="medieval"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="medieval"] .eyr .er{border-bottom:1px solid rgba(140,106,60,.2);padding:.3rem 0;display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="medieval"] .eyr .en{font-family:'IM Fell English',serif;color:#C0C0C0}
[data-theme="medieval"] .eyr .et{font-family:'IM Fell English',serif;font-style:italic;color:#7a6a4a}
#wwcTorch{position:fixed;inset:0;pointer-events:none;z-index:54;transition:background .08s}
"""
if 'DEEP-BATCH-2' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('CSS inserted')
else:
    log.append('CSS present')

js = r"""
<script>
/* ══ DEEP-BATCH-2 INTERACTIONS (baroque/newspaper/medieval) ══ */
(function(){
  var fx=null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  function toast(msg,color){
    var t=document.getElementById('wwcToast');
    if(!t){ t=document.createElement('div'); t.id='wwcToast'; document.body.appendChild(t); }
    t.textContent=msg; if(color)t.style.background=color; t.classList.add('show');
    clearTimeout(t._h); t._h=setTimeout(function(){ t.classList.remove('show'); },1800);
  }
  /* J baroque: gold sparkle cursor + click portrait flourish */
  function baroque(){
    var cv=document.createElement('canvas'); cv.id='wwcGoldCanvas'; document.body.appendChild(cv);
    var ctx=cv.getContext('2d'),ps=[],raf;
    function rs(){cv.width=innerWidth;cv.height=innerHeight;} rs(); addEventListener('resize',rs);
    function mv(e){ for(var i=0;i<2;i++)ps.push({x:e.clientX,y:e.clientY,vx:(Math.random()-.5)*1.6,vy:(Math.random()-.5)*1.6-.4,a:1,s:Math.random()*2.4+1}); if(ps.length>180)ps.splice(0,ps.length-180); }
    addEventListener('mousemove',mv);
    function loop(){ raf=requestAnimationFrame(loop); ctx.clearRect(0,0,cv.width,cv.height);
      for(var i=0;i<ps.length;i++){var p=ps[i];p.x+=p.vx;p.y+=p.vy;p.vy+=.02;p.a*=.96;
        ctx.fillStyle='rgba('+[230,196,90].join(',')+','+p.a+')'; ctx.fillRect(p.x,p.y,p.s,p.s);} }
    loop();
    function clk(e){ if(e.target.closest('#about .al2 img')) toast('✦ Bravissimo ✦','#9c6b1f'); }
    document.addEventListener('click',clk);
    fx=function(){cancelAnimationFrame(raf);removeEventListener('mousemove',mv);removeEventListener('resize',rs);document.removeEventListener('click',clk);cv.remove();};
  }
  /* M newspaper: typewriter name + EXTRA stamp */
  function newspaper(){
    var name=document.getElementById('e3');
    function tw(){ if(!name||name._b)return; name._b=true; var real=name.getAttribute('data-r')||name.textContent; name.setAttribute('data-r',real); var i=0;
      var iv=setInterval(function(){ name.textContent=real.slice(0,i)+(i<real.length?'█':''); i++; if(i>real.length){clearInterval(iv);name.textContent=real;name._b=false;} },70);
      var s=document.createElement('div'); s.className='wwc-stamp'; s.textContent='EXTRA!'; s.style.left='50%'; s.style.top='40%'; document.body.appendChild(s);
      setTimeout(function(){s.style.transition='opacity .5s';s.style.opacity='0';setTimeout(function(){s.remove();},500);},1400); }
    if(name)name.addEventListener('click',tw);
    fx=function(){ if(name)name.removeEventListener('click',tw); };
  }
  /* O medieval: torch light cursor + wax seal click */
  function medieval(){
    var t=document.createElement('div'); t.id='wwcTorch'; document.body.appendChild(t);
    function mv(e){ t.style.background='radial-gradient(circle at '+e.clientX+'px '+e.clientY+'px, rgba(0,0,0,0) 90px, rgba(0,0,0,.35) 240px, rgba(0,0,0,.6) 420px)'; }
    addEventListener('mousemove',mv);
    function clk(e){ if(e.target.closest('#about .al2 img')||e.target.closest('.eyr')) toast('✠ Sigillum ✠','#5a0000'); }
    document.addEventListener('click',clk);
    fx=function(){removeEventListener('mousemove',mv);document.removeEventListener('click',clk);t.remove();};
  }
  window.initBatch2=function(theme){ teardown();
    if(theme==='baroque')baroque(); else if(theme==='newspaper')newspaper(); else if(theme==='medieval')medieval(); };
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); setTimeout(function(){ try{initBatch2(t);}catch(e){} },180); }; }
  addEventListener('load',function(){ setTimeout(function(){ try{initBatch2(localStorage.getItem('wwc-theme')||'default');}catch(e){} },1500); });
})();
</script>
</body>"""
if 'DEEP-BATCH-2 INTERACTIONS' not in html:
    html = html.replace('</body>', js, 1)
    log.append('JS inserted')
else:
    log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
