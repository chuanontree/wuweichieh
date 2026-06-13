#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add S circuit + T garden full themes (all sections + 3D + about/cv +
interactions), and convert the theme switcher into a Style dropdown (◉ + A-T)."""

with open('index.html','r',encoding='utf-8') as f:
    html=f.read()
orig=len(html); log=[]

# ───────────── 1. Switcher → dropdown ─────────────
opts=[('default','◉ Original'),('brutal','A · Editorial Brutal'),('luxury','B · Liquid Luxury'),
('void','C · Systemic Void'),('canvas','D · Infinite Canvas'),('zen','E · Zen Focus'),
('iso','F · Isometric 3D'),('multiverse','G · Multiverse'),('apple','H · Apple Editorial'),
('cyber','I · Cyberpunk'),('baroque','J · Baroque'),('bauhaus','K · Bauhaus'),
('popart','L · Pop Art'),('newspaper','M · Newspaper'),('chinese','N · 水墨丹青'),
('medieval','O · 鋼鐵誓約'),('sky','P · 天空懸浮'),('crystal','Q · 水晶'),
('y2k','R · Y2K 液態金屬'),('circuit','S · 電路板'),('garden','T · 花園')]
sel='id="themeSwitch"><label class="style-lab">Style</label><select id="themeSelect" onchange="applyTheme(this.value)">'
for v,l in opts: sel+='<option value="'+v+'">'+l+'</option>'
sel+='</select></div>'
s=html.find('id="themeSwitch">')
if s!=-1 and 'id="themeSelect"' not in html:
    e=html.find('</div>',s)+len('</div>')
    html=html[:s]+sel+html[e:]
    log.append('switcher → dropdown')
else:
    log.append('dropdown present/anchor missing')

# ───────────── 2. bgColors extend ─────────────
oldbg="var bgColors = { chinese: '#F7F3EA', medieval: '#0D0D0D', baroque: '#1A0A0E', bauhaus: '#ffffff', popart: '#FFE600', newspaper: '#F8F5ED', sky: '#cfe6f7', crystal: '#eef0ff', y2k: '#0a0a14', 'default': '#090909' };"
newbg=oldbg.replace("y2k: '#0a0a14',","y2k: '#0a0a14', circuit: '#04140a', garden: '#f4f8ee',")
if oldbg in html: html=html.replace(oldbg,newbg,1); log.append('bgColors extended')
else: log.append('bgColors anchor missing')

# ───────────── 3. CSS ─────────────
css = """
/* ══ STYLE DROPDOWN ══ */
#themeSwitch{display:flex;align-items:center;gap:.5rem;overflow:visible;max-width:none}
.style-lab{font-size:.55rem;letter-spacing:.25em;text-transform:uppercase;opacity:.65}
#themeSelect{background:transparent;color:inherit;border:1px solid currentColor;border-radius:5px;padding:.32rem .6rem;font-family:inherit;font-size:.72rem;cursor:pointer;max-width:190px;outline:none}
#themeSelect option{background:#111;color:#fff}

/* ══ S CIRCUIT 電路板 ══ */
[data-theme="circuit"]{--bg:#04140a;--fg:#c8f7d8;--metal:#d9883b;--accent:#39ff14;--line:rgba(57,255,20,.2);--dim:rgba(57,255,20,.06);font-family:'Rajdhani',sans-serif}
[data-theme="circuit"] body{background:#04140a;background-image:linear-gradient(rgba(57,255,20,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(57,255,20,.06) 1px,transparent 1px);background-size:32px 32px}
[data-theme="circuit"] header{background:rgba(4,20,10,.95);border-bottom:1px solid #39ff14;box-shadow:0 0 20px rgba(57,255,20,.25)}
[data-theme="circuit"] .logo{font-family:'Syncopate',sans-serif;color:#39ff14;text-shadow:0 0 8px rgba(57,255,20,.7);letter-spacing:.1em}
[data-theme="circuit"] .ni{font-family:'Rajdhani',sans-serif;color:#7fd9a0;border-left:1px solid rgba(57,255,20,.2)}
[data-theme="circuit"] .ni:hover,[data-theme="circuit"] .ni.on{color:#39ff14;background:rgba(57,255,20,.1)}
[data-theme="circuit"] #hero{background:radial-gradient(ellipse at center,#072011,#04140a)}
[data-theme="circuit"] .hn{font-family:'Syncopate',sans-serif;color:#39ff14;text-shadow:0 0 20px rgba(57,255,20,.6)}
[data-theme="circuit"] .hn .ol{-webkit-text-stroke:1px #d9883b;color:transparent}
[data-theme="circuit"] .he{color:#d9883b}
[data-theme="circuit"] .htag{font-family:'Rajdhani',sans-serif;color:#7fd9a0}
[data-theme="circuit"] #catBar{border-bottom:1px solid rgba(57,255,20,.2)}
[data-theme="circuit"] .ct{font-family:'Rajdhani',sans-serif;color:#7fd9a0;background:none;border:none;border-right:1px solid rgba(57,255,20,.15);padding:.5rem 1.2rem;cursor:pointer}
[data-theme="circuit"] .ct:hover,[data-theme="circuit"] .ct.on{color:#39ff14}
[data-theme="circuit"] #pg-works,[data-theme="circuit"] #pg-about,[data-theme="circuit"] #pg-cv,[data-theme="circuit"] #pg-gallery{background:#04140a}
[data-theme="circuit"] .wg{display:grid !important;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:2.6rem;padding:3.2rem;background:#04140a}
[data-theme="circuit"] .wi{background:#0a2415 !important;border:1px solid #39ff14 !important;border-radius:4px !important;box-shadow:0 0 18px rgba(57,255,20,.2),inset 0 0 20px rgba(0,0,0,.4) !important;position:relative;overflow:visible}
[data-theme="circuit"] .wi::before{content:'';position:absolute;top:-11px;left:18px;right:18px;height:11px;background:repeating-linear-gradient(90deg,#d9883b 0 4px,transparent 4px 10px)}
[data-theme="circuit"] .wi::after{content:'';position:absolute;bottom:-11px;left:18px;right:18px;height:11px;background:repeating-linear-gradient(90deg,#d9883b 0 4px,transparent 4px 10px)}
[data-theme="circuit"] .wi img{filter:hue-rotate(55deg) saturate(.8) brightness(.9);transition:filter .4s}
[data-theme="circuit"] .wi:hover{box-shadow:0 0 32px rgba(57,255,20,.55)}
[data-theme="circuit"] .wi:hover img{filter:none}
[data-theme="circuit"] .wt{font-family:'Syncopate',sans-serif;color:#39ff14;font-size:.88rem}
[data-theme="circuit"] .wm{font-family:'Rajdhani',sans-serif;color:#d9883b}
[data-theme="circuit"] .wio{background:linear-gradient(to top,rgba(4,20,10,.95),transparent)}
[data-theme="circuit"] #about{max-width:900px;margin:0 auto;padding:5rem 2rem;display:grid;grid-template-columns:240px 1fr;gap:3rem}
[data-theme="circuit"] #about .al2 img{border:1px solid #39ff14;box-shadow:0 0 20px rgba(57,255,20,.3)}
[data-theme="circuit"] #about .ir>div{display:grid;grid-template-columns:150px 1fr;gap:1rem;padding:.5rem .8rem;border-left:2px solid #d9883b;background:rgba(57,255,20,.04);margin-bottom:.4rem;cursor:grab}
[data-theme="circuit"] #about .il{font-family:'Syncopate',sans-serif;color:#d9883b;font-size:.55rem;letter-spacing:.05em;text-transform:uppercase}
[data-theme="circuit"] #about .il::before{content:'◇ '}
[data-theme="circuit"] #about .iv{font-family:'Rajdhani',sans-serif;color:#39ff14;font-size:1rem;font-weight:600}
[data-theme="circuit"] #pg-cv{max-width:820px;margin:0 auto;padding:4rem 2rem}
[data-theme="circuit"] .eyr{display:grid !important;grid-template-columns:110px 1fr;gap:1.2rem;background:rgba(10,36,21,.6);border:1px solid rgba(57,255,20,.25);border-left:3px solid #d9883b;margin-bottom:.8rem;padding:.8rem 1.1rem;width:auto;column-count:auto}
[data-theme="circuit"] .eyr .yl{font-family:'Syncopate',sans-serif;color:#39ff14;font-size:.8rem;writing-mode:horizontal-tb}
[data-theme="circuit"] .eyr .yi{display:flex;flex-direction:column;gap:.2rem}
[data-theme="circuit"] .eyr .er{display:flex;justify-content:space-between;border-bottom:1px dashed rgba(57,255,20,.15);padding:.2rem 0;writing-mode:horizontal-tb}
[data-theme="circuit"] .eyr .er::before{content:'> ';color:#d9883b}
[data-theme="circuit"] .eyr .en{color:#c8f7d8;font-weight:600}
[data-theme="circuit"] .eyr .et{color:#5a8a6a;font-size:.8rem}
[data-theme="circuit"] #galleryHint{background:rgba(10,36,21,.92);border:1px solid #39ff14;box-shadow:0 0 30px rgba(57,255,20,.25)}
[data-theme="circuit"] #galleryHint h2{font-family:'Syncopate',sans-serif;color:#39ff14}
[data-theme="circuit"] #galleryHint button{background:#39ff14;color:#04140a;border:none;font-family:'Syncopate',sans-serif}
[data-theme="circuit"] footer{background:#020a05;color:#7fd9a0;border-top:1px solid #39ff14}
[data-theme="circuit"] footer a{color:#d9883b}
[data-theme="circuit"] #wwc-btn{background:linear-gradient(135deg,#39ff14,#0a2415);box-shadow:0 0 20px rgba(57,255,20,.5)}
[data-theme="circuit"] #wwc-panel{background:rgba(10,36,21,.95);border:1px solid #39ff14}
[data-theme="circuit"] .wwc-head{background:linear-gradient(135deg,#0a2415,#39ff14)}
#circuitModel3D,#gardenModel3D{position:absolute;right:6vw;top:50%;transform:translateY(-50%);width:300px;height:300px;z-index:3;pointer-events:none;display:none}
[data-theme="circuit"] #circuitModel3D{display:block}
.wwc-node{position:fixed;width:7px;height:7px;border-radius:50%;background:#39ff14;box-shadow:0 0 10px #39ff14;pointer-events:none;z-index:9998;animation:nodeFade .8s ease-out forwards}
@keyframes nodeFade{from{opacity:.9;transform:scale(1)}to{opacity:0;transform:scale(.3)}}
.wwc-pulse{position:fixed;border:2px solid #39ff14;border-radius:50%;pointer-events:none;z-index:9998;animation:pulseExp .7s ease-out forwards}
@keyframes pulseExp{from{width:8px;height:8px;opacity:.8;transform:translate(-50%,-50%)}to{width:200px;height:200px;opacity:0;transform:translate(-50%,-50%)}}

/* ══ T GARDEN 花園 ══ */
[data-theme="garden"]{--bg:#f4f8ee;--fg:#2f3d28;--metal:#6a9a4f;--accent:#e08ab0;--line:rgba(47,61,40,.12);--dim:rgba(106,154,79,.1);font-family:'EB Garamond',serif}
[data-theme="garden"] body{background:linear-gradient(180deg,#f4f8ee,#e9f1dd)}
[data-theme="garden"] header{background:rgba(244,248,238,.9);backdrop-filter:blur(8px);border-bottom:2px solid #6a9a4f}
[data-theme="garden"] .logo{font-family:'Cormorant Garamond',serif;font-weight:700;color:#3d5a2a;letter-spacing:.05em}
[data-theme="garden"] .logo::before{content:'❀ ';color:#e08ab0}
[data-theme="garden"] .ni{font-family:'EB Garamond',serif;color:#6a9a4f}
[data-theme="garden"] .ni:hover,[data-theme="garden"] .ni.on{color:#e08ab0}
[data-theme="garden"] #hero{background:linear-gradient(180deg,#eaf3dc,#f4f8ee)}
[data-theme="garden"] .hn{font-family:'Cormorant Garamond',serif;font-style:italic;color:#3d5a2a}
[data-theme="garden"] .hn .ol{-webkit-text-stroke:1px #e08ab0;color:transparent}
[data-theme="garden"] .he{color:#e08ab0}
[data-theme="garden"] .htag{font-family:'EB Garamond',serif;color:#6a9a4f}
[data-theme="garden"] #catBar{border-bottom:1px solid rgba(106,154,79,.3)}
[data-theme="garden"] .ct{font-family:'EB Garamond',serif;color:#6a9a4f;background:none;border:none;padding:.5rem 1.2rem;border-radius:20px;cursor:pointer}
[data-theme="garden"] .ct:hover,[data-theme="garden"] .ct.on{color:#fff;background:#e08ab0}
[data-theme="garden"] #pg-works,[data-theme="garden"] #pg-about,[data-theme="garden"] #pg-cv,[data-theme="garden"] #pg-gallery{background:linear-gradient(180deg,#f4f8ee,#e9f1dd)}
[data-theme="garden"] .wg{display:grid !important;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:2.4rem;padding:3rem}
[data-theme="garden"] .wi{background:#fff !important;border:1px solid #cfe0bd !important;border-radius:50% 50% 8px 8px/16% 16% 8px 8px !important;box-shadow:0 12px 30px rgba(106,154,79,.2) !important;overflow:hidden;position:relative}
[data-theme="garden"] .wi::before{content:'❦';position:absolute;top:6px;left:50%;transform:translateX(-50%);color:#e08ab0;z-index:3;font-size:1.1rem}
[data-theme="garden"] .wi img{filter:saturate(1.05);transition:transform .5s}
[data-theme="garden"] .wi:hover img{transform:scale(1.05)}
[data-theme="garden"] .wt{font-family:'Cormorant Garamond',serif;font-style:italic;color:#3d5a2a;font-size:1.1rem}
[data-theme="garden"] .wm{font-family:'EB Garamond',serif;color:#e08ab0}
[data-theme="garden"] .wio{background:linear-gradient(to top,rgba(255,255,255,.95),transparent)}
[data-theme="garden"] #about{max-width:920px;margin:0 auto;padding:5rem 2rem;display:grid;grid-template-columns:280px 1fr;gap:3rem}
[data-theme="garden"] #about .al2 img{border-radius:50%;border:6px solid #fff;box-shadow:0 10px 30px rgba(106,154,79,.3)}
[data-theme="garden"] #about .ir{display:flex;flex-direction:column;gap:.7rem}
[data-theme="garden"] #about .ir>div{background:#fff;border:1px solid #cfe0bd;border-radius:18px 18px 18px 4px;padding:.8rem 1.2rem;position:relative}
[data-theme="garden"] #about .ir>div::before{content:'🌿';position:absolute;left:-8px;top:-10px;font-size:1rem}
[data-theme="garden"] #about .il{font-family:'EB Garamond',serif;color:#6a9a4f;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase}
[data-theme="garden"] #about .iv{font-family:'Cormorant Garamond',serif;color:#2f3d28;font-size:1.15rem}
[data-theme="garden"] #pg-cv{max-width:720px;margin:0 auto;padding:4rem 2rem}
[data-theme="garden"] .eyr{display:grid !important;grid-template-columns:100px 1fr;gap:1.5rem;border-left:3px solid #6a9a4f;margin:0 0 1.5rem 1rem;padding:1rem 1.2rem;background:#fff;border-radius:0 18px 18px 0;box-shadow:0 8px 20px rgba(106,154,79,.15);width:auto;column-count:auto;position:relative}
[data-theme="garden"] .eyr::before{content:'❀';position:absolute;left:-14px;top:1rem;color:#e08ab0;background:#f4f8ee;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center}
[data-theme="garden"] .eyr .yl{font-family:'Cormorant Garamond',serif;font-style:italic;color:#6a9a4f;font-size:1.2rem;writing-mode:horizontal-tb}
[data-theme="garden"] .eyr .yi{display:flex;flex-direction:column;gap:.3rem}
[data-theme="garden"] .eyr .er{display:flex;justify-content:space-between;writing-mode:horizontal-tb}
[data-theme="garden"] .eyr .en{font-family:'Cormorant Garamond',serif;color:#2f3d28;font-size:1.05rem}
[data-theme="garden"] .eyr .et{font-family:'EB Garamond',serif;font-style:italic;color:#e08ab0}
[data-theme="garden"] #galleryHint{background:rgba(255,255,255,.88);border:1px solid #cfe0bd;border-radius:20px;box-shadow:0 14px 40px rgba(106,154,79,.25)}
[data-theme="garden"] #galleryHint h2{font-family:'Cormorant Garamond',serif;color:#3d5a2a}
[data-theme="garden"] #galleryHint button{background:#e08ab0;color:#fff;border:none;border-radius:30px;font-family:'EB Garamond',serif}
[data-theme="garden"] footer{background:#dfe9cf;color:#3d5a2a;border-top:2px solid #6a9a4f}
[data-theme="garden"] footer a{color:#e08ab0}
[data-theme="garden"] #wwc-btn{background:linear-gradient(135deg,#6a9a4f,#e08ab0)}
[data-theme="garden"] #wwc-panel{background:rgba(255,255,255,.92);border:1px solid #cfe0bd;border-radius:18px}
[data-theme="garden"] .wwc-head{background:linear-gradient(135deg,#6a9a4f,#9bc47a)}
[data-theme="garden"] #gardenModel3D{display:block}
.wwc-leaf{position:fixed;pointer-events:none;z-index:9998;font-size:1.3rem;animation:leafFall 2.6s ease-in forwards}
@keyframes leafFall{from{opacity:.95;transform:translateY(0) rotate(0)}to{opacity:0;transform:translateY(160px) rotate(220deg)}}
.wwc-bloom{position:fixed;pointer-events:none;z-index:9998;font-size:1.6rem;animation:bloomPop 1.1s ease-out forwards}
@keyframes bloomPop{0%{opacity:0;transform:scale(0)}40%{opacity:1;transform:scale(1.3)}100%{opacity:0;transform:scale(1.6) translateY(-30px)}}
"""
if 'S CIRCUIT' not in html:
    ls=html.rfind('</style>'); html=html[:ls]+css+html[ls:]; log.append('CSS inserted')
else: log.append('CSS present')

# ───────────── 4. hero 3D divs ─────────────
anchor='<div id="newspaperModel3D" style="display:none"></div>'
if anchor in html and 'id="circuitModel3D"' not in html:
    html=html.replace(anchor,anchor+'\n<div id="circuitModel3D" style="display:none"></div>\n<div id="gardenModel3D" style="display:none"></div>',1)
    log.append('3D divs added')
else: log.append('3D divs present/anchor missing')

# ───────────── 5. init3DModels + builders ─────────────
old_clear="['chineseModel3D','medievalModel3D','skyModel3D','crystalModel3D','y2kModel3D','baroqueModel3D','bauhausModel3D','popartModel3D','newspaperModel3D']"
new_clear="['chineseModel3D','medievalModel3D','skyModel3D','crystalModel3D','y2kModel3D','baroqueModel3D','bauhausModel3D','popartModel3D','newspaperModel3D','circuitModel3D','gardenModel3D']"
if old_clear in html: html=html.replace(old_clear,new_clear,1)
old_case="  else if (theme === 'newspaper') { createNewsprintRoll('newspaperModel3D'); }\n};"
new_case="""  else if (theme === 'newspaper') { createNewsprintRoll('newspaperModel3D'); }
  else if (theme === 'circuit') { createCircuitChip('circuitModel3D'); }
  else if (theme === 'garden') { createFlower('gardenModel3D'); }
};

function createCircuitChip(id){ var k=_mk3d(id,45,6); if(!k)return;
  var board=new THREE.Mesh(new THREE.BoxGeometry(3,3,0.18), new THREE.MeshPhongMaterial({color:0x0a3a1a,shininess:40,emissive:0x031a0c,emissiveIntensity:.5}));
  k.scene.add(board);
  var trace=new THREE.MeshPhongMaterial({color:0x39ff14,emissive:0x39ff14,emissiveIntensity:.6});
  for(var i=0;i<8;i++){ var t=new THREE.Mesh(new THREE.BoxGeometry(Math.random()*1.6+.4,0.05,0.02),trace); t.position.set((Math.random()-.5)*2.4,(Math.random()-.5)*2.4,0.1); k.scene.add(t); }
  var cop=new THREE.MeshPhongMaterial({color:0xd9883b,shininess:120});
  for(var j=0;j<5;j++){ var c=new THREE.Mesh(new THREE.BoxGeometry(.5,.5,.16),cop); c.position.set((Math.random()-.5)*2,(Math.random()-.5)*2,0.12); k.scene.add(c); }
  var chip=new THREE.Mesh(new THREE.BoxGeometry(1,1,.25),new THREE.MeshPhongMaterial({color:0x111111,shininess:80})); chip.position.z=.18; k.scene.add(chip);
  k.scene.add(new THREE.AmbientLight(0x224422,.7)); var l=new THREE.PointLight(0x39ff14,1.4,12); l.position.set(2,2,5); k.scene.add(l);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*.001; k.scene.rotation.y=t*.4; k.scene.rotation.x=Math.sin(t*.3)*.25; trace.emissiveIntensity=.4+Math.abs(Math.sin(t*3))*.5; k.renderer.render(k.scene,k.camera);} an();
  k.c._cleanup=function(){cancelAnimationFrame(fr);k.renderer.dispose();};
}

function createFlower(id){ var k=_mk3d(id,45,6); if(!k)return; var g=new THREE.Group();
  var stem=new THREE.Mesh(new THREE.CylinderGeometry(.06,.08,2.6,8),new THREE.MeshPhongMaterial({color:0x4f7a35})); stem.position.y=-1.3; g.add(stem);
  var center=new THREE.Mesh(new THREE.SphereGeometry(.42,24,18),new THREE.MeshPhongMaterial({color:0xf4c542,shininess:40})); center.position.y=.9; g.add(center);
  var petalMat=new THREE.MeshPhongMaterial({color:0xe08ab0,shininess:30,side:THREE.DoubleSide});
  for(var i=0;i<8;i++){ var p=new THREE.Mesh(new THREE.SphereGeometry(.42,16,12),petalMat); p.scale.set(1,.35,.6); var a=i/8*Math.PI*2; p.position.set(Math.cos(a)*.75,.9,Math.sin(a)*.75); p.lookAt(0,.9,0); g.add(p); }
  var leafMat=new THREE.MeshPhongMaterial({color:0x6a9a4f,side:THREE.DoubleSide});
  [[-1,-.4],[1,-.7]].forEach(function(d){ var lf=new THREE.Mesh(new THREE.SphereGeometry(.4,12,8),leafMat); lf.scale.set(1.4,.18,.6); lf.position.set(d[0]*.4,d[1],0); lf.rotation.z=d[0]*.6; g.add(lf); });
  k.scene.add(g); k.scene.add(new THREE.AmbientLight(0xffffff,.7)); var dl=new THREE.DirectionalLight(0xffffff,.9); dl.position.set(2,4,5); k.scene.add(dl);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*.001; g.rotation.y=t*.5; g.rotation.z=Math.sin(t*.8)*.08; k.renderer.render(k.scene,k.camera);} an();
  k.c._cleanup=function(){cancelAnimationFrame(fr);k.renderer.dispose();};
}"""
if 'createCircuitChip' not in html and old_case in html:
    html=html.replace(old_case,new_case,1); log.append('init3D + builders added')
else: log.append('init3D present/anchor missing')

# ───────────── 6. interactions ─────────────
js = r"""
<script>
/* ══ S/T INTERACTIONS (circuit/garden) + dropdown sync ══ */
(function(){
  var fx=null;
  function teardown(){ if(fx){ try{fx();}catch(e){} fx=null; } }
  function circuit(){
    var last=0;
    function mv(e){ var n=Date.now(); if(n-last<26)return; last=n; var d=document.createElement('div'); d.className='wwc-node'; d.style.left=e.clientX+'px'; d.style.top=e.clientY+'px'; document.body.appendChild(d); setTimeout(function(){d.remove();},800); }
    addEventListener('mousemove',mv);
    function clk(e){ var p=document.createElement('div'); p.className='wwc-pulse'; p.style.left=e.clientX+'px'; p.style.top=e.clientY+'px'; document.body.appendChild(p); setTimeout(function(){p.remove();},700); }
    document.addEventListener('click',clk);
    var drags=[]; if(window.Draggable){ try{ drags=Draggable.create('[data-theme="circuit"] #about .ir > div',{type:'x,y'}); }catch(e){} }
    fx=function(){ removeEventListener('mousemove',mv); document.removeEventListener('click',clk); (drags||[]).forEach(function(d){try{d.kill();}catch(e){}}); document.querySelectorAll('#about .ir > div').forEach(function(el){el.style.transform='';}); };
  }
  function garden(){
    var last=0;
    function mv(e){ var n=Date.now(); if(n-last<140)return; last=n; var l=document.createElement('div'); l.className='wwc-leaf'; l.textContent=Math.random()<.5?'🍃':'🌸'; l.style.left=e.clientX+'px'; l.style.top=e.clientY+'px'; document.body.appendChild(l); setTimeout(function(){l.remove();},2600); }
    addEventListener('mousemove',mv);
    function clk(e){ var f=['🌸','🌼','🌷','🌹','💐']; for(var i=0;i<5;i++){ var b=document.createElement('div'); b.className='wwc-bloom'; b.textContent=f[Math.floor(Math.random()*f.length)]; b.style.left=(e.clientX+(Math.random()-.5)*50)+'px'; b.style.top=(e.clientY+(Math.random()-.5)*50)+'px'; document.body.appendChild(b); (function(el){setTimeout(function(){el.remove();},1100);})(b); } }
    document.addEventListener('click',clk);
    fx=function(){ removeEventListener('mousemove',mv); document.removeEventListener('click',clk); };
  }
  window.initST=function(t){ teardown(); if(t==='circuit')circuit(); else if(t==='garden')garden(); };
  var prev=window.applyTheme;
  if(prev){ window.applyTheme=function(t){ prev(t); var sel=document.getElementById('themeSelect'); if(sel&&sel.value!==t)sel.value=t; setTimeout(function(){ try{initST(t);}catch(e){} },200); }; }
  addEventListener('load',function(){ var t=localStorage.getItem('wwc-theme')||'default'; var sel=document.getElementById('themeSelect'); if(sel)sel.value=t; setTimeout(function(){ try{initST(t);}catch(e){} },1650); });
})();
</script>
</body>"""
if 'S/T INTERACTIONS' not in html:
    html=html.replace('</body>',js,1); log.append('JS inserted')
else: log.append('JS present')

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig,len(html),len(html)-orig))
for l in log: print('  -',l)
