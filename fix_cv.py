#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix: gsap.from() leaves .eyr/.sh/.al2 img stuck at opacity:0 when their
page is display:none at load (ScrollTrigger never fires). Add
immediateRender:false + clearProps so content stays visible."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

repls = [
    (
        "gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 88%', toggleActions: 'play none none none' }, opacity: 0, x: -30, duration: 0.6, delay: i * 0.1, ease: 'power2.out' });",
        "gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 92%', toggleActions: 'play none none none' }, immediateRender: false, clearProps: 'opacity,transform', opacity: 0, x: -30, duration: 0.6, delay: i * 0.05, ease: 'power2.out' });"
    ),
    (
        "gsap.from(aboutImg, { scrollTrigger: { trigger: aboutImg, start: 'top 80%' }, opacity: 0, scale: 0.85, duration: 0.9, ease: 'back.out(1.5)' });",
        "gsap.from(aboutImg, { scrollTrigger: { trigger: aboutImg, start: 'top 90%' }, immediateRender: false, clearProps: 'opacity,transform', opacity: 0, scale: 0.85, duration: 0.9, ease: 'back.out(1.5)' });"
    ),
    (
        "gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 85%' }, opacity: 0, y: 20, duration: 0.5, ease: 'power2.out' });",
        "gsap.from(el, { scrollTrigger: { trigger: el, start: 'top 92%' }, immediateRender: false, clearProps: 'opacity,transform', opacity: 0, y: 20, duration: 0.5, ease: 'power2.out' });"
    ),
]

n = 0
for old, new in repls:
    if old in html:
        html = html.replace(old, new, 1)
        n += 1

# Safety net: when a page tab becomes active, refresh ScrollTrigger and
# guarantee CV/about content is visible (covers any edge case).
if 'wwcCvSafety' not in html:
    safety = """
<script>
/* wwcCvSafety: ensure tab content never stays hidden by GSAP */
(function(){
  function reveal(){
    document.querySelectorAll('.eyr,.sh,.al2 img').forEach(function(el){
      if (getComputedStyle(el).opacity === '0') { el.style.opacity='1'; el.style.transform='none'; }
    });
    if (window.ScrollTrigger) { try { ScrollTrigger.refresh(); } catch(e){} }
  }
  if (window.pg) { var _pg = window.pg; window.pg = function(n,b){ _pg(n,b); setTimeout(reveal, 80); }; }
  window.addEventListener('load', function(){ setTimeout(reveal, 1200); });
})();
</script>
</body>"""
    html = html.replace('</body>', safety, 1)
    n += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('replacements applied:', n)
