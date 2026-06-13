#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep redesign for 3 themes (chinese / cyber / y2k): distinct layouts for
about, cv, gallery, AI assistant + interactions (drag, click games/eggs,
scroll narrative). Theme-scoped; other themes untouched."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html)
log = []

# ═══════════════ CSS ═══════════════
css = """
/* ══ DEEP-3 THEME PAGE REDESIGNS (chinese / cyber / y2k) ══ */

/* ---------- 水墨 CHINESE ---------- */
[data-theme="chinese"] #about{display:grid;grid-template-columns:300px 1fr;gap:3rem;max-width:1000px;margin:0 auto;padding:5rem 2rem}
[data-theme="chinese"] #about .al2{position:relative}
[data-theme="chinese"] #about .al2 img{cursor:pointer}
[data-theme="chinese"] #about .ar .ir{display:flex;flex-direction:column;gap:0;border-right:2px solid rgba(192,57,43,.25);padding-right:1.5rem}
[data-theme="chinese"] #about .ir>div{display:grid;grid-template-columns:120px 1fr;gap:1rem;padding:.9rem 0;border-bottom:1px dotted rgba(26,18,9,.25);align-items:baseline}
[data-theme="chinese"] #about .il{font-family:'Noto Serif TC',serif;color:#C0392B;font-weight:700;letter-spacing:.1em;font-size:.82rem}
[data-theme="chinese"] #about .iv{font-family:'Noto Serif TC',serif;color:#1A1209;font-size:.95rem;line-height:1.7}
[data-theme="chinese"] #pg-cv{padding:4rem 2rem}
[data-theme="chinese"] #pg-cv>div{display:flex;flex-direction:row-reverse;flex-wrap:wrap;gap:2.5rem;justify-content:center;align-items:flex-start}
[data-theme="chinese"] .eyr{display:block;width:130px;background:linear-gradient(#fbf7ee,#f2ebda);border:1px solid rgba(192,57,43,.3);border-radius:6px 6px 0 0;padding:1.4rem .6rem 2.5rem;box-shadow:2px 4px 14px rgba(26,18,9,.15);position:relative}
[data-theme="chinese"] .eyr::before{content:'';position:absolute;top:-10px;left:50%;transform:translateX(-50%);width:18px;height:18px;border-radius:50%;background:#C0392B;box-shadow:0 0 0 3px #fbf7ee,0 0 0 4px #C0392B}
[data-theme="chinese"] .eyr .yl{writing-mode:vertical-rl;font-size:1.2rem;margin:0 auto 1rem;text-align:center}
[data-theme="chinese"] .eyr .yi{display:flex;flex-direction:column;gap:1rem}
[data-theme="chinese"] .eyr .er{writing-mode:vertical-rl;height:160px;display:flex;gap:.4rem;margin:0 auto}
[data-theme="chinese"] .eyr .en{font-family:'Noto Serif TC',serif;color:#1A1209;font-weight:700;font-size:.92rem}
[data-theme="chinese"] .eyr .et{font-family:'Cormorant Garamond',serif;color:#8C6A3C;font-size:.72rem;font-style:italic}
.wwc-seal{position:absolute;width:60px;height:60px;background:#C0392B;color:#fff;font-family:'Noto Serif TC',serif;font-size:1.6rem;display:flex;align-items:center;justify-content:center;border-radius:6px;pointer-events:none;z-index:60;animation:sealPop .5s cubic-bezier(.34,1.56,.64,1)}
@keyframes sealPop{0%{transform:scale(0) rotate(-25deg);opacity:0}60%{opacity:1}100%{transform:scale(1) rotate(-8deg);opacity:.92}}
#wwcInkCanvas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:55}

/* ---------- 賽博 CYBER ---------- */
[data-theme="cyber"] #about{max-width:880px;margin:0 auto;padding:4.5rem 2rem;position:relative}
[data-theme="cyber"] #about::before{content:'> SUBJECT DOSSIER // ACCESS GRANTED';display:block;font-family:'Syncopate',monospace;color:#00f0ff;font-size:.7rem;letter-spacing:.2em;margin-bottom:1.5rem;border-bottom:1px solid rgba(0,240,255,.3);padding-bottom:.6rem}
[data-theme="cyber"] #about{display:block}
[data-theme="cyber"] #about .al2{float:right;width:200px;margin:0 0 1rem 2rem}
[data-theme="cyber"] #about .al2 img{border:1px solid #00f0ff;box-shadow:0 0 20px rgba(0,240,255,.4);filter:saturate(1.2) contrast(1.1)}
[data-theme="cyber"] #about .ir{display:flex;flex-direction:column;gap:.4rem}
[data-theme="cyber"] #about .ir>div{display:grid;grid-template-columns:160px 1fr;gap:1rem;padding:.5rem .8rem;border-left:2px solid #ff00a0;background:rgba(0,240,255,.04);cursor:grab;transition:background .2s}
[data-theme="cyber"] #about .ir>div:hover{background:rgba(0,240,255,.12)}
[data-theme="cyber"] #about .il{font-family:'Syncopate',monospace;color:#ff00a0;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase}
[data-theme="cyber"] #about .il::before{content:'\\25b8 '}
[data-theme="cyber"] #about .iv{font-family:'Rajdhani',monospace;color:#00f0ff;font-size:1rem;font-weight:600}
[data-theme="cyber"] #about .iv#e3{cursor:pointer}
[data-theme="cyber"] #pg-cv{max-width:820px;margin:0 auto;padding:4rem 2rem;font-family:'Rajdhani',monospace}
[data-theme="cyber"] #pg-cv .sh{color:#00f0ff}
[data-theme="cyber"] .eyr{display:block;background:rgba(0,20,30,.5);border:1px solid rgba(0,240,255,.25);border-left:3px solid #ff00a0;margin-bottom:.7rem;padding:.7rem 1rem}
[data-theme="cyber"] .eyr .yl{font-family:'Syncopate',monospace;color:#ff00a0;font-size:.8rem;margin-bottom:.4rem}
[data-theme="cyber"] .eyr .yl::before{content:'LOG['}
[data-theme="cyber"] .eyr .yl::after{content:']'}
[data-theme="cyber"] .eyr .er{display:flex;justify-content:space-between;padding:.25rem 0;border-bottom:1px dashed rgba(0,240,255,.15)}
[data-theme="cyber"] .eyr .er::before{content:'$ ';color:#00ff88;font-family:monospace}
[data-theme="cyber"] .eyr .en{color:#dfefff;font-weight:600}
[data-theme="cyber"] .eyr .et{color:#5a8aa0;font-size:.78rem}

/* ---------- Y2K ---------- */
[data-theme="y2k"] #about{display:flex;flex-wrap:wrap;gap:2rem;max-width:1000px;margin:0 auto;padding:4.5rem 2rem;align-items:flex-start}
[data-theme="y2k"] #about .al2{flex:0 0 240px}
[data-theme="y2k"] #about .ar{flex:1;min-width:280px}
[data-theme="y2k"] #about .ir{display:flex;flex-wrap:wrap;gap:1rem}
[data-theme="y2k"] #about .ir>div{flex:1 1 200px;background:linear-gradient(135deg,rgba(185,196,214,.25),rgba(94,215,255,.12));border:1px solid rgba(185,196,214,.5);border-radius:18px;padding:1rem 1.2rem;box-shadow:inset 0 2px 8px rgba(255,255,255,.25),0 8px 24px rgba(0,0,0,.4);cursor:grab;backdrop-filter:blur(6px);transition:transform .25s}
[data-theme="y2k"] #about .il{font-family:'Orbitron',sans-serif;color:#ff5ed2;font-size:.6rem;letter-spacing:.1em;margin-bottom:.4rem}
[data-theme="y2k"] #about .iv{font-family:'Rajdhani',sans-serif;color:#dfe6ff;font-size:1rem;font-weight:600}
[data-theme="y2k"] #pg-cv{max-width:760px;margin:0 auto;padding:4rem 2rem}
[data-theme="y2k"] .eyr{display:flex;align-items:center;gap:1.5rem;background:linear-gradient(135deg,rgba(28,34,56,.85),rgba(16,19,31,.85));border:1px solid transparent;border-image:linear-gradient(135deg,#5ed7ff,#ff5ed2) 1;border-radius:40px;margin-bottom:1.2rem;padding:1rem 2rem;box-shadow:0 8px 30px rgba(94,215,255,.2),inset 0 1px 0 rgba(255,255,255,.2);transition:transform .3s}
[data-theme="y2k"] .eyr:hover{transform:translateX(10px) scale(1.02)}
[data-theme="y2k"] .eyr .yl{font-family:'Orbitron',sans-serif;color:#5ed7ff;font-size:1.1rem;flex:0 0 auto;background:rgba(94,215,255,.12);border-radius:30px;padding:.4rem 1rem}
[data-theme="y2k"] .eyr .yi{display:flex;flex-direction:column;gap:.4rem;flex:1}
[data-theme="y2k"] .eyr .er{display:flex;justify-content:space-between}
[data-theme="y2k"] .eyr .en{font-family:'Rajdhani',sans-serif;color:#dfe6ff;font-weight:600}
[data-theme="y2k"] .eyr .et{font-family:'Rajdhani',sans-serif;color:#ff5ed2;font-size:.8rem}
#wwcBlob{position:fixed;width:46px;height:46px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,#5ed7ff 45%,#ff5ed2);box-shadow:0 0 24px rgba(94,215,255,.6);pointer-events:none;z-index:9998;mix-blend-mode:screen;transition:transform .12s;will-change:left,top}

/* shared easter-egg toast */
#wwcToast{position:fixed;bottom:90px;left:50%;transform:translateX(-50%) translateY(20px);opacity:0;background:rgba(0,0,0,.85);color:#fff;padding:.7rem 1.4rem;border-radius:30px;font-size:.85rem;z-index:9999;pointer-events:none;transition:opacity .3s,transform .3s;letter-spacing:.05em}
#wwcToast.show{opacity:1;transform:translateX(-50%) translateY(0)}
"""
if 'DEEP-3 THEME PAGE REDESIGNS' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('CSS inserted')
else:
    log.append('CSS present')

# ═══════════════ JS ═══════════════
js = r"""
<script>
/* ══ DEEP-3 THEME INTERACTIONS ══ */
(function(){
  var fx = null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  function toast(msg){
    var t=document.getElementById('wwcToast');
    if(!t){ t=document.createElement('div'); t.id='wwcToast'; document.body.appendChild(t); }
    t.textContent=msg; t.classList.add('show');
    clearTimeout(t._h); t._h=setTimeout(function(){ t.classList.remove('show'); },1800);
  }

  /* ---- 水墨: ink trail + seal stamp ---- */
  function chinese(){
    var cv=document.createElement('canvas'); cv.id='wwcInkCanvas';
    document.body.appendChild(cv);
    var ctx=cv.getContext('2d'), dabs=[], raf;
    function resize(){ cv.width=innerWidth; cv.height=innerHeight; }
    resize(); addEventListener('resize',resize);
    var last=0;
    function move(e){ var now=Date.now(); if(now-last<28)return; last=now;
      dabs.push({x:e.clientX,y:e.clientY,r:Math.random()*10+6,a:.32}); if(dabs.length>60)dabs.shift(); }
    addEventListener('mousemove',move);
    function loop(){ raf=requestAnimationFrame(loop); ctx.clearRect(0,0,cv.width,cv.height);
      for(var i=0;i<dabs.length;i++){var d=dabs[i]; d.a*=.95; d.r*=1.01;
        ctx.beginPath(); ctx.fillStyle='rgba(26,18,9,'+d.a+')'; ctx.arc(d.x,d.y,d.r,0,7); ctx.fill(); } }
    loop();
    function stamp(e){ var img=e.target.closest('#about .al2 img'); if(!img)return;
      var s=document.createElement('div'); s.className='wwc-seal'; s.textContent='桀';
      var r=img.getBoundingClientRect();
      s.style.left=(r.left+r.width-50+scrollX)+'px'; s.style.top=(r.top+r.height-70+scrollY)+'px';
      s.style.position='absolute'; document.body.appendChild(s);
      toast('鈐印 · 落款');
      setTimeout(function(){ s.style.transition='opacity .6s'; s.style.opacity='0'; setTimeout(function(){s.remove();},600); },2200); }
    document.addEventListener('click',stamp);
    fx=function(){ cancelAnimationFrame(raf); removeEventListener('mousemove',move); removeEventListener('resize',resize); document.removeEventListener('click',stamp); cv.remove(); };
  }

  /* ---- 賽博: name decrypt + draggable dossier rows ---- */
  function cyber(){
    var drags=[];
    var name=document.getElementById('e3');
    function decrypt(){ if(!name||name._busy)return; name._busy=true;
      var real=name.getAttribute('data-real')||name.textContent; name.setAttribute('data-real',real);
      var chars='!<>-_\\/[]{}=+*^?#01'; var frame=0;
      var iv=setInterval(function(){ var out='';
        for(var i=0;i<real.length;i++){ out+= i<frame/2 ? real[i] : chars[Math.floor(Math.random()*chars.length)]; }
        name.textContent=out; frame++; if(frame/2>=real.length){ clearInterval(iv); name.textContent=real; name._busy=false; toast('ACCESS GRANTED ✓'); } },45); }
    if(name) name.addEventListener('click',decrypt);
    if(window.Draggable){ try{
      drags=Draggable.create('[data-theme="cyber"] #about .ir > div',{type:'x,y',inertia:false,onDragStart:function(){this.target.style.zIndex=70;this.target.style.cursor='grabbing';},onDragEnd:function(){this.target.style.cursor='grab';}});
    }catch(e){} }
    fx=function(){ if(name)name.removeEventListener('click',decrypt); (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); document.querySelectorAll('#about .ir > div').forEach(function(el){el.style.transform='';}); };
  }

  /* ---- Y2K: liquid cursor blob + draggable chrome chips ---- */
  function y2k(){
    var blob=document.createElement('div'); blob.id='wwcBlob'; document.body.appendChild(blob);
    var tx=innerWidth/2,ty=innerHeight/2,bx=tx,by=ty,raf;
    function move(e){ tx=e.clientX; ty=e.clientY; }
    addEventListener('mousemove',move);
    function loop(){ raf=requestAnimationFrame(loop); bx+=(tx-bx)*.18; by+=(ty-by)*.18;
      blob.style.left=(bx-23)+'px'; blob.style.top=(by-23)+'px'; }
    loop();
    var drags=[];
    if(window.Draggable){ try{
      drags=Draggable.create('[data-theme="y2k"] #about .ir > div',{type:'x,y',onDragStart:function(){this.target.style.cursor='grabbing';this.target.style.zIndex=70;},onDragEnd:function(){var t=this.target; if(window.gsap)gsap.to(t,{x:0,y:0,duration:.8,ease:'elastic.out(1,0.4)'}); t.style.cursor='grab';}});
    }catch(e){} }
    function spark(e){ var chip=e.target.closest('[data-theme="y2k"] #about .al2 img'); if(!chip)return; toast('✧ Y2K ✧'); }
    document.addEventListener('click',spark);
    fx=function(){ cancelAnimationFrame(raf); removeEventListener('mousemove',move); document.removeEventListener('click',spark); (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); blob.remove(); };
  }

  window.initThemeInteractions=function(theme){ teardown();
    if(theme==='chinese')chinese(); else if(theme==='cyber')cyber(); else if(theme==='y2k')y2k(); };

  /* chain into applyTheme */
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); setTimeout(function(){ try{initThemeInteractions(t);}catch(e){} },160); }; }
  addEventListener('load',function(){ setTimeout(function(){ try{initThemeInteractions(localStorage.getItem('wwc-theme')||'default');}catch(e){} },1400); });
})();
</script>
</body>"""
if 'DEEP-3 THEME INTERACTIONS' not in html:
    html = html.replace('</body>', js, 1)
    log.append('JS inserted')
else:
    log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)

print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
