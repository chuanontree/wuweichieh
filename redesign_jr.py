#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Redesign J-R with structurally DISTINCT layouts (not just recolor) +
add 3D models for baroque/bauhaus/popart/newspaper."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

orig = len(html)
log = []

# ════ 1. DISTINCT LAYOUT CSS (inserted last → wins by source order) ════
css = """
/* ══ J-R STRUCTURAL LAYOUT REDESIGN ════════════════════ */

/* J · Baroque — Salon hanging wall (masonry columns, ornate frames) */
[data-theme="baroque"] .wg{display:block !important;column-count:3;column-gap:2.6rem;padding:3.5rem 6vw;background:repeating-linear-gradient(0deg,#1A0A0E,#1A0A0E 38px,#210d12 38px,#210d12 40px)}
@media(max-width:900px){[data-theme="baroque"] .wg{column-count:2}}
@media(max-width:600px){[data-theme="baroque"] .wg{column-count:1}}
[data-theme="baroque"] .wi{break-inside:avoid;display:inline-block;width:100%;margin:0 0 2.8rem;border:7px solid #C9922A;border-radius:6px;box-shadow:0 0 0 2px #1A0A0E,0 0 0 5px #6e4f1d,0 14px 40px rgba(0,0,0,.6);background:#2A1218;position:relative;transition:transform .5s}
[data-theme="baroque"] .wi:nth-child(3n){margin-top:1.6rem}
[data-theme="baroque"] .wi:nth-child(4n){margin-top:.8rem}
[data-theme="baroque"] .wi:hover{transform:scale(1.03) rotate(-.6deg)}
[data-theme="baroque"] .wi::before{content:'❧';position:absolute;top:-30px;left:50%;transform:translateX(-50%);color:#C9922A;font-size:1.4rem;z-index:3}
[data-theme="baroque"] .wi img{filter:sepia(35%) contrast(1.05) brightness(.9) !important}

/* K · Bauhaus — Asymmetric modular composition with primary blocks */
[data-theme="bauhaus"] .wg{display:grid !important;grid-template-columns:repeat(6,1fr);grid-auto-rows:150px;grid-auto-flow:dense;gap:0;padding:0;background:#000;border:6px solid #000}
[data-theme="bauhaus"] .wi{border:4px solid #000 !important;margin:0;border-radius:0 !important;position:relative;overflow:hidden}
[data-theme="bauhaus"] .wi:nth-child(7n+1){grid-column:span 3;grid-row:span 2}
[data-theme="bauhaus"] .wi:nth-child(7n+2){grid-column:span 2;grid-row:span 1}
[data-theme="bauhaus"] .wi:nth-child(7n+3){grid-column:span 1;grid-row:span 2}
[data-theme="bauhaus"] .wi:nth-child(7n+4){grid-column:span 2;grid-row:span 2}
[data-theme="bauhaus"] .wi:nth-child(7n+5){grid-column:span 2;grid-row:span 1}
[data-theme="bauhaus"] .wi:nth-child(7n+6){grid-column:span 3;grid-row:span 1}
[data-theme="bauhaus"] .wi:nth-child(7n){grid-column:span 1;grid-row:span 1;background:#E63329}
[data-theme="bauhaus"] .wi:nth-child(5n){background:#0F5EAD}
[data-theme="bauhaus"] .wi:nth-child(9n){background:#FFD500}
[data-theme="bauhaus"] .wi img{width:100%;height:100%;object-fit:cover}
[data-theme="bauhaus"] .wi:hover{outline:6px solid #E63329;outline-offset:-6px;z-index:2}

/* L · Pop Art — Comic strip panels (irregular spans, halftone, tilt) */
[data-theme="popart"] .wg{display:grid !important;grid-template-columns:repeat(4,1fr);grid-auto-rows:200px;grid-auto-flow:dense;gap:10px;padding:14px;background:#000;background-image:radial-gradient(#FFE600 14%,transparent 15%);background-size:22px 22px}
[data-theme="popart"] .wi{border:5px solid #000 !important;border-radius:0 !important;box-shadow:none !important;background:#fff;position:relative;overflow:hidden}
[data-theme="popart"] .wi:nth-child(5n+1){grid-column:span 2;grid-row:span 2;transform:rotate(-1.2deg)}
[data-theme="popart"] .wi:nth-child(5n+2){transform:rotate(1deg)}
[data-theme="popart"] .wi:nth-child(5n+3){grid-row:span 2;transform:rotate(-.8deg)}
[data-theme="popart"] .wi:nth-child(5n+4){grid-column:span 2;transform:rotate(.6deg)}
[data-theme="popart"] .wi::before{content:counter(none);position:absolute;top:6px;left:8px;font-family:'Bangers',cursive;font-size:1.3rem;color:#FF3EA5;-webkit-text-stroke:1px #000;z-index:3}
[data-theme="popart"] .wi::after{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.18) 18%,transparent 19%);background-size:7px 7px;mix-blend-mode:multiply;pointer-events:none}
[data-theme="popart"] .wi img{filter:saturate(1.6) contrast(1.2) !important}
[data-theme="popart"] .wi:hover{transform:scale(1.05) rotate(0deg);z-index:4}

/* M · Newspaper — Broadsheet column flow with full-width lead */
[data-theme="newspaper"] .wg{display:block !important;column-count:4;column-gap:1.6rem;column-rule:1px solid #0A0A0A;padding:2.4rem 3vw;background:#F8F5ED}
@media(max-width:900px){[data-theme="newspaper"] .wg{column-count:2}}
@media(max-width:560px){[data-theme="newspaper"] .wg{column-count:1}}
[data-theme="newspaper"] .wi{break-inside:avoid;display:inline-block;width:100%;margin:0 0 1.4rem;border:none !important;border-bottom:2px solid #0A0A0A !important;border-radius:0 !important;box-shadow:none !important;background:#F8F5ED;padding-bottom:.8rem}
[data-theme="newspaper"] .wi:first-child{column-span:all;border-bottom:4px double #0A0A0A !important;margin-bottom:2rem;padding-bottom:1.4rem}
[data-theme="newspaper"] .wi:first-child img{max-height:340px;object-fit:cover}
[data-theme="newspaper"] .wi img{filter:grayscale(100%) contrast(1.12) !important}
[data-theme="newspaper"] .wi:hover img{filter:grayscale(60%) !important}

/* P · Sky — Floating constellation (varied heights, drift) */
[data-theme="sky"] .wg{display:flex !important;flex-wrap:wrap;justify-content:center;align-items:flex-start;gap:2.4rem 3rem;padding:5rem 6vw}
[data-theme="sky"] .wi{width:clamp(200px,22vw,260px) !important;border-radius:24px !important;animation:skyFloat 7s ease-in-out infinite}
[data-theme="sky"] .wi:nth-child(3n+1){margin-top:0}
[data-theme="sky"] .wi:nth-child(3n+2){margin-top:4.5rem}
[data-theme="sky"] .wi:nth-child(3n){margin-top:2.2rem}
[data-theme="sky"] .wi:nth-child(4n){margin-top:6rem}

/* Q · Crystal — Honeycomb hexagon facets */
[data-theme="crystal"] .wg{display:grid !important;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px 14px;padding:3rem 5vw}
[data-theme="crystal"] .wi{clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);border-radius:0 !important;border:none !important;box-shadow:0 6px 24px rgba(160,107,255,.3) !important;aspect-ratio:1/1.1}
[data-theme="crystal"] .wi:nth-child(even){transform:translateY(34px)}
[data-theme="crystal"] .wi img{width:100%;height:100%;object-fit:cover}
[data-theme="crystal"] .wi:hover{transform:scale(1.08);z-index:3}
[data-theme="crystal"] .wi:nth-child(even):hover{transform:translateY(34px) scale(1.08)}
[data-theme="crystal"] .wi .wio{display:none}

/* R · Y2K — Chrome bubble pods (blob shapes, varied sizes) */
[data-theme="y2k"] .wg{display:flex !important;flex-wrap:wrap;justify-content:center;align-items:center;gap:2.4rem;padding:4rem 5vw}
[data-theme="y2k"] .wi{border-radius:48% 52% 47% 53%/55% 48% 52% 45% !important;border:2px solid #b9c4d6 !important;overflow:hidden;box-shadow:0 10px 40px rgba(94,215,255,.35),inset 0 2px 10px rgba(255,255,255,.4) !important;transition:border-radius .6s,transform .5s}
[data-theme="y2k"] .wi:nth-child(3n+1){width:clamp(200px,22vw,280px);height:clamp(200px,22vw,280px)}
[data-theme="y2k"] .wi:nth-child(3n+2){width:clamp(160px,18vw,220px);height:clamp(160px,18vw,220px)}
[data-theme="y2k"] .wi:nth-child(3n){width:clamp(180px,20vw,250px);height:clamp(180px,20vw,250px)}
[data-theme="y2k"] .wi img{width:100%;height:100%;object-fit:cover}
[data-theme="y2k"] .wi:hover{border-radius:50% !important;transform:scale(1.06)}

/* model containers for J-M */
#baroqueModel3D,#bauhausModel3D,#popartModel3D,#newspaperModel3D{position:absolute;right:6vw;top:50%;transform:translateY(-50%);width:300px;height:300px;z-index:3;pointer-events:none;display:none}
[data-theme="baroque"] #baroqueModel3D{display:block}
[data-theme="bauhaus"] #bauhausModel3D{display:block}
[data-theme="popart"] #popartModel3D{display:block}
[data-theme="newspaper"] #newspaperModel3D{display:block}
"""
if 'J-R STRUCTURAL LAYOUT REDESIGN' not in html:
    last_style = html.rfind('</style>')
    html = html[:last_style] + css + html[last_style:]
    log.append('layout CSS inserted')
else:
    log.append('layout CSS already present')

# ════ 2. Hero model divs for J-M ════
anchor_div = '<div id="y2kModel3D" style="display:none"></div>'
new_divs = anchor_div + """
<div id="baroqueModel3D" style="display:none"></div>
<div id="bauhausModel3D" style="display:none"></div>
<div id="popartModel3D" style="display:none"></div>
<div id="newspaperModel3D" style="display:none"></div>"""
if 'id="baroqueModel3D"' not in html:
    html = html.replace(anchor_div, new_divs, 1)
    log.append('J-M 3D divs added')
else:
    log.append('J-M 3D divs present')

# ════ 3. init3DModels + builders for J-M ════
old_init = """window.init3DModels = function(theme) {
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
};"""
new_init = """window.init3DModels = function(theme) {
  ['chineseModel3D','medievalModel3D','skyModel3D','crystalModel3D','y2kModel3D','baroqueModel3D','bauhausModel3D','popartModel3D','newspaperModel3D'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) { if (el._cleanup) { el._cleanup(); el._cleanup = null; } while (el.firstChild) { el.removeChild(el.firstChild); } }
  });
  if (typeof THREE === 'undefined') return;
  if (theme === 'chinese') { createJadeDisc('chineseModel3D'); }
  else if (theme === 'medieval') { createMedievalHelmet('medievalModel3D'); }
  else if (theme === 'sky') { createFloatingRocks('skyModel3D'); }
  else if (theme === 'crystal') { createCrystalCluster('crystalModel3D'); }
  else if (theme === 'y2k') { createLiquidChrome('y2kModel3D'); }
  else if (theme === 'baroque') { createBaroqueOrnament('baroqueModel3D'); }
  else if (theme === 'bauhaus') { createBauhausComposition('bauhausModel3D'); }
  else if (theme === 'popart') { createPopBurst('popartModel3D'); }
  else if (theme === 'newspaper') { createNewsprintRoll('newspaperModel3D'); }
};

function createBaroqueOrnament(id) {
  var k = _mk3d(id, 42, 5); if (!k) return;
  var gold = new THREE.MeshPhongMaterial({ color: 0xC9922A, shininess: 220, specular: 0xfff0c0, emissive: 0x3a2a08, emissiveIntensity: 0.4 });
  var knot = new THREE.Mesh(new THREE.TorusKnotGeometry(1.1, 0.34, 160, 20, 2, 3), gold);
  k.scene.add(knot);
  var ring = new THREE.Mesh(new THREE.TorusGeometry(1.9, 0.05, 12, 90), gold.clone()); ring.rotation.x = 1.2; k.scene.add(ring);
  k.scene.add(new THREE.AmbientLight(0x5a4020, 0.6));
  var l1 = new THREE.PointLight(0xfff0c0, 1.6, 14); l1.position.set(3, 3, 5); k.scene.add(l1);
  var l2 = new THREE.PointLight(0xC9922A, 1.0, 14); l2.position.set(-4, -2, 3); k.scene.add(l2);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; knot.rotation.x=t*0.4; knot.rotation.y=t*0.3; ring.rotation.z=t*0.5; k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}

function createBauhausComposition(id) {
  var k = _mk3d(id, 45, 6); if (!k) return;
  var group = new THREE.Group();
  var red = new THREE.Mesh(new THREE.BoxGeometry(1.3,1.3,1.3), new THREE.MeshPhongMaterial({color:0xE63329,shininess:30}));
  red.position.set(-1,0.4,0); group.add(red);
  var blue = new THREE.Mesh(new THREE.SphereGeometry(0.85,32,24), new THREE.MeshPhongMaterial({color:0x0F5EAD,shininess:30}));
  blue.position.set(1.1,-0.6,0.4); group.add(blue);
  var yellow = new THREE.Mesh(new THREE.ConeGeometry(0.8,1.6,32), new THREE.MeshPhongMaterial({color:0xFFD500,shininess:30}));
  yellow.position.set(0.5,1.1,-0.5); group.add(yellow);
  var bar = new THREE.Mesh(new THREE.BoxGeometry(3.2,0.18,0.18), new THREE.MeshPhongMaterial({color:0x111111}));
  bar.rotation.z=-0.5; group.add(bar);
  k.scene.add(group);
  k.scene.add(new THREE.AmbientLight(0xffffff,0.8));
  var dl=new THREE.DirectionalLight(0xffffff,0.9); dl.position.set(2,4,5); k.scene.add(dl);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; group.rotation.y=t*0.5; red.rotation.x=t*0.6; yellow.rotation.y=t*0.7; k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}

function createPopBurst(id) {
  var k = _mk3d(id, 45, 6); if (!k) return;
  var group = new THREE.Group();
  var core = new THREE.Mesh(new THREE.SphereGeometry(0.9,32,24), new THREE.MeshPhongMaterial({color:0xFF3EA5,shininess:90,emissive:0x3a0020,emissiveIntensity:0.3}));
  group.add(core);
  var spikeMat = new THREE.MeshPhongMaterial({color:0xFFE600,shininess:60});
  for(var i=0;i<14;i++){
    var s=new THREE.Mesh(new THREE.ConeGeometry(0.28,0.9,5), spikeMat);
    var ph=Math.acos(1-2*(i+0.5)/14), th=Math.PI*(1+Math.sqrt(5))*i;
    var r=1.25;
    s.position.set(r*Math.sin(ph)*Math.cos(th), r*Math.cos(ph), r*Math.sin(ph)*Math.sin(th));
    s.lookAt(s.position.clone().multiplyScalar(2)); s.rotateX(Math.PI/2);
    group.add(s);
  }
  k.scene.add(group);
  k.scene.add(new THREE.AmbientLight(0xffffff,0.7));
  var l1=new THREE.PointLight(0xffffff,1.3,14); l1.position.set(3,3,5); k.scene.add(l1);
  var l2=new THREE.PointLight(0x6bd5ff,0.8,14); l2.position.set(-3,-2,3); k.scene.add(l2);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; group.rotation.y=t*0.6; group.rotation.x=t*0.25; var p=1+Math.sin(t*3)*0.06; core.scale.set(p,p,p); k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}

function createNewsprintRoll(id) {
  var k = _mk3d(id, 42, 6); if (!k) return;
  var group = new THREE.Group();
  var paperMat = new THREE.MeshPhongMaterial({color:0xF8F5ED,shininess:8,side:THREE.DoubleSide});
  var inkMat = new THREE.MeshPhongMaterial({color:0x111111,shininess:8,side:THREE.DoubleSide});
  for(var i=0;i<5;i++){
    var sheet=new THREE.Mesh(new THREE.PlaneGeometry(2.4,3.2,1,1), i%2?inkMat:paperMat);
    sheet.position.set(0,0,-i*0.06); sheet.rotation.z=(i-2)*0.05; group.add(sheet);
  }
  var roll=new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.5,2.6,32,1,true), paperMat.clone());
  roll.position.set(0,0,0.6); roll.rotation.x=1.2; group.add(roll);
  k.scene.add(group);
  k.scene.add(new THREE.AmbientLight(0xffffff,0.9));
  var dl=new THREE.DirectionalLight(0xffffff,0.7); dl.position.set(2,4,6); k.scene.add(dl);
  var fr; function an(){ fr=requestAnimationFrame(an); var t=Date.now()*0.001; group.rotation.y=Math.sin(t*0.6)*0.5; group.rotation.x=Math.cos(t*0.4)*0.15; k.renderer.render(k.scene,k.camera); } an();
  k.c._cleanup=function(){ cancelAnimationFrame(fr); k.renderer.dispose(); };
}"""
if 'createBaroqueOrnament' not in html:
    html = html.replace(old_init, new_init, 1)
    log.append('init3DModels + 4 J-M builders added')
else:
    log.append('J-M builders present')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig, len(html), len(html)-orig))
for l in log: print('  -', l)
