#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert J-M base theme CSS (header/hero/works) into the style block.
Run AFTER apply_changes.py (which adds N/O + J-M section fixes)."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '[data-theme="baroque"] .hn' in html:
    print('J-M base CSS already present, skipping')
    raise SystemExit(0)

jm_base = """
/* ══ J-M BASE THEMES (header/hero/works) ══════════════ */
/* J — Baroque 巴洛克 */
[data-theme="baroque"]{--bg:#1A0A0E;--fg:#F5EDD6;--accent:#C9922A;--line:rgba(201,146,42,.25);--dim:rgba(201,146,42,.08);font-family:'Cormorant Garamond',serif}
[data-theme="baroque"] header{background:rgba(26,10,14,.97);border-bottom:2px solid #C9922A;box-shadow:0 2px 24px rgba(201,146,42,.25)}
[data-theme="baroque"] .logo{font-family:'Cinzel Decorative',serif;font-weight:700;color:#C9922A;letter-spacing:.15em}
[data-theme="baroque"] .ni{font-family:'Cormorant Garamond',serif;color:#C9922A;font-size:.72rem;letter-spacing:.1em;border-left:1px solid rgba(201,146,42,.2)}
[data-theme="baroque"] .ni:hover,[data-theme="baroque"] .ni.on{color:#F5EDD6;background:rgba(201,146,42,.12)}
[data-theme="baroque"] #hero{background:radial-gradient(ellipse at center,#2A1218,#1A0A0E)}
[data-theme="baroque"] .hn{font-family:'Cinzel Decorative',serif;font-weight:700;color:#C9922A;text-shadow:0 2px 20px rgba(201,146,42,.4)}
[data-theme="baroque"] .hn .ol{-webkit-text-stroke:1px #C9922A;color:transparent;font-family:'Cinzel Decorative',serif}
[data-theme="baroque"] .he{color:#F5EDD6;font-family:'Cormorant Garamond',serif;font-style:italic}
[data-theme="baroque"] .htag{font-family:'Cormorant Garamond',serif;font-style:italic;color:#C9922A}
[data-theme="baroque"] #catBar{border-bottom:1px solid rgba(201,146,42,.25)}
[data-theme="baroque"] .ct{font-family:'Cinzel Decorative',serif;font-size:.6rem;color:#C9922A;background:none;border:none;border-right:1px solid rgba(201,146,42,.15);padding:.5rem 1.2rem;letter-spacing:.1em;cursor:pointer}
[data-theme="baroque"] .ct:hover,[data-theme="baroque"] .ct.on{color:#F5EDD6}
[data-theme="baroque"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:2rem;padding:2rem;background:#1A0A0E}
[data-theme="baroque"] .wi{background:#2A1218;border:3px solid #C9922A;box-shadow:0 0 0 1px #1A0A0E,0 8px 30px rgba(0,0,0,.5),inset 0 0 30px rgba(201,146,42,.1);position:relative;overflow:hidden}
[data-theme="baroque"] .wi img{filter:sepia(25%) contrast(1.05) brightness(.92);transition:filter .5s,transform .6s}
[data-theme="baroque"] .wi:hover img{filter:sepia(10%) contrast(1.1) brightness(1);transform:scale(1.05)}
[data-theme="baroque"] .wt{font-family:'Cinzel Decorative',serif;color:#C9922A;font-size:1rem}
[data-theme="baroque"] .wm{font-family:'Cormorant Garamond',serif;font-style:italic;color:#F5EDD6;font-size:.85rem}
[data-theme="baroque"] .wio{background:linear-gradient(to top,rgba(26,10,14,.97),transparent);padding:2rem 1rem .8rem}
/* K — Bauhaus 包浩斯 */
[data-theme="bauhaus"]{--bg:#ffffff;--fg:#000000;--accent:#E63329;--line:rgba(0,0,0,.15);--dim:rgba(0,0,0,.05);font-family:'DM Sans',sans-serif}
[data-theme="bauhaus"] header{background:#fff;border-bottom:4px solid #000}
[data-theme="bauhaus"] .logo{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;letter-spacing:-.02em}
[data-theme="bauhaus"] .ni{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;font-size:.7rem;border-left:none}
[data-theme="bauhaus"] .ni:hover,[data-theme="bauhaus"] .ni.on{color:#fff;background:#E63329}
[data-theme="bauhaus"] #hero{background:#fff;position:relative;overflow:hidden}
[data-theme="bauhaus"] #hero::before{content:'';position:absolute;top:10%;right:8%;width:160px;height:160px;border-radius:50%;background:#FFD500;z-index:0}
[data-theme="bauhaus"] #hero::after{content:'';position:absolute;bottom:12%;left:6%;width:0;height:0;border-left:90px solid transparent;border-right:90px solid transparent;border-bottom:150px solid #0F5EAD;z-index:0}
[data-theme="bauhaus"] .hn{font-family:'DM Sans',sans-serif;font-weight:700;color:#000;letter-spacing:-.03em;position:relative;z-index:2}
[data-theme="bauhaus"] .hn .ol{-webkit-text-stroke:2px #E63329;color:transparent}
[data-theme="bauhaus"] .he{color:#E63329;font-family:'DM Sans',sans-serif;font-weight:700}
[data-theme="bauhaus"] .htag{font-family:'DM Sans',sans-serif;color:#000;position:relative;z-index:2}
[data-theme="bauhaus"] #catBar{border-bottom:4px solid #000}
[data-theme="bauhaus"] .ct{font-family:'DM Sans',sans-serif;font-weight:700;font-size:.62rem;color:#000;background:none;border:none;padding:.5rem 1.2rem;cursor:pointer}
[data-theme="bauhaus"] .ct:hover,[data-theme="bauhaus"] .ct.on{color:#fff;background:#000}
[data-theme="bauhaus"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:0;padding:0;background:#000;border-top:4px solid #000}
[data-theme="bauhaus"] .wi{background:#fff;border:4px solid #000;position:relative;overflow:hidden}
[data-theme="bauhaus"] .wi img{filter:none;transition:transform .4s}
[data-theme="bauhaus"] .wi:hover img{transform:scale(1.05)}
[data-theme="bauhaus"] .wt{font-family:'DM Sans',sans-serif;font-weight:700;color:#000}
[data-theme="bauhaus"] .wm{font-family:'DM Sans',sans-serif;color:#E63329;font-size:.8rem}
[data-theme="bauhaus"] .wio{background:#fff;border-top:4px solid #000;padding:1rem;transform:none}
/* L — Pop Art 普普 */
[data-theme="popart"]{--bg:#FFE600;--fg:#000000;--accent:#FF3EA5;--line:rgba(0,0,0,.2);--dim:rgba(0,0,0,.06);font-family:'Bangers',cursive}
[data-theme="popart"] header{background:#FFE600;border-bottom:4px solid #000}
[data-theme="popart"] .logo{font-family:'Bangers',cursive;color:#000;letter-spacing:.05em;font-size:1.2rem}
[data-theme="popart"] .ni{font-family:'Bangers',cursive;color:#000;letter-spacing:.05em;border-left:3px solid #000}
[data-theme="popart"] .ni:hover,[data-theme="popart"] .ni.on{color:#fff;background:#FF3EA5}
[data-theme="popart"] #hero{background:#FFE600;background-image:radial-gradient(#000 12%,transparent 13%);background-size:18px 18px;position:relative}
[data-theme="popart"] .hn{font-family:'Bangers',cursive;color:#FF3EA5;-webkit-text-stroke:2px #000;letter-spacing:.04em;text-shadow:4px 4px 0 #000}
[data-theme="popart"] .hn .ol{-webkit-text-stroke:2px #000;color:#fff}
[data-theme="popart"] .he{color:#000;font-family:'Bangers',cursive}
[data-theme="popart"] .htag{font-family:monospace;color:#000;background:#fff;border:2px solid #000;display:inline-block;padding:.3rem .6rem}
[data-theme="popart"] #catBar{border-bottom:4px solid #000}
[data-theme="popart"] .ct{font-family:'Bangers',cursive;font-size:.85rem;color:#000;background:none;border:none;border-right:3px solid #000;padding:.4rem 1.2rem;letter-spacing:.05em;cursor:pointer}
[data-theme="popart"] .ct:hover,[data-theme="popart"] .ct.on{color:#fff;background:#FF3EA5}
[data-theme="popart"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;padding:1.5rem;background:#FFE600}
[data-theme="popart"] .wi{background:#fff;border:4px solid #000;box-shadow:8px 8px 0 #000;position:relative;overflow:hidden}
[data-theme="popart"] .wi img{filter:saturate(1.4) contrast(1.1);transition:transform .3s}
[data-theme="popart"] .wi:hover{box-shadow:8px 8px 0 #FF3EA5}
[data-theme="popart"] .wi:hover img{transform:scale(1.06)}
[data-theme="popart"] .wt{font-family:'Bangers',cursive;color:#000;font-size:1.3rem;letter-spacing:.03em}
[data-theme="popart"] .wm{font-family:monospace;color:#FF3EA5;font-size:.78rem}
[data-theme="popart"] .wio{background:#fff;border-top:4px solid #000;padding:1rem;transform:none}
/* M — Newspaper 報紙 */
[data-theme="newspaper"]{--bg:#F8F5ED;--fg:#0A0A0A;--accent:#CC0000;--line:rgba(10,10,10,.2);--dim:rgba(10,10,10,.05);font-family:'Source Serif 4',serif}
[data-theme="newspaper"] header{background:#F8F5ED;border-bottom:3px double #0A0A0A}
[data-theme="newspaper"] .logo{font-family:'Playfair Display',serif;font-weight:700;color:#0A0A0A;letter-spacing:.02em}
[data-theme="newspaper"] .ni{font-family:'Source Serif 4',serif;color:#0A0A0A;font-size:.7rem;border-left:1px solid rgba(10,10,10,.2)}
[data-theme="newspaper"] .ni:hover,[data-theme="newspaper"] .ni.on{color:#CC0000}
[data-theme="newspaper"] #hero{background:#F8F5ED;border-bottom:3px double #0A0A0A}
[data-theme="newspaper"] .hn{font-family:'Playfair Display',serif;font-weight:700;color:#0A0A0A;letter-spacing:-.01em;border-bottom:4px solid #0A0A0A;border-top:4px solid #0A0A0A;padding:.4rem 0}
[data-theme="newspaper"] .hn .ol{-webkit-text-stroke:1px #0A0A0A;color:transparent;font-family:'Playfair Display',serif}
[data-theme="newspaper"] .he{color:#CC0000;font-family:'Playfair Display',serif;font-style:italic}
[data-theme="newspaper"] .htag{font-family:'Source Serif 4',serif;color:#0A0A0A;font-size:.82rem;text-align:justify}
[data-theme="newspaper"] #catBar{border-bottom:1px solid #0A0A0A}
[data-theme="newspaper"] .ct{font-family:'Playfair Display',serif;font-size:.62rem;color:#0A0A0A;background:none;border:none;border-right:1px solid rgba(10,10,10,.2);padding:.5rem 1.2rem;text-transform:uppercase;letter-spacing:.08em;cursor:pointer}
[data-theme="newspaper"] .ct:hover,[data-theme="newspaper"] .ct.on{color:#CC0000}
[data-theme="newspaper"] .wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.5rem;padding:1.5rem;background:#F8F5ED}
[data-theme="newspaper"] .wi{background:#F8F5ED;border:1px solid #0A0A0A;position:relative;overflow:hidden}
[data-theme="newspaper"] .wi img{filter:grayscale(60%) contrast(1.1);transition:filter .4s,transform .5s}
[data-theme="newspaper"] .wi:hover img{filter:grayscale(20%);transform:scale(1.04)}
[data-theme="newspaper"] .wt{font-family:'Playfair Display',serif;font-weight:700;color:#0A0A0A;font-size:1.05rem}
[data-theme="newspaper"] .wm{font-family:monospace;color:#555;font-size:.76rem}
[data-theme="newspaper"] .wio{background:linear-gradient(to top,rgba(248,245,237,.97),transparent);padding:1.5rem 1rem .8rem}
"""

last_style = html.rfind('</style>')
html = html[:last_style] + jm_base + html[last_style:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'J-M base CSS inserted ({len(jm_base)} chars). New size: {len(html):,}')
