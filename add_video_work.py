#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add artwork 限時動態 Action! Figure to works video tab."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

MARKER = 'WQ0qF_Lh0-k'
if MARKER in html:
    print('Already present, skipping.')
else:
    new_item = (
        '\n<div class="wi fi vis" data-cat="video" data-src="https://img.youtube.com/vi/WQ0qF_Lh0-k/maxresdefault.jpg" style="" draggable="false">\n'
        '      <a href="https://www.youtube.com/watch?v=WQ0qF_Lh0-k" target="_blank" rel="noopener" style="display:block;position:relative;overflow:hidden;background:#0c0c0c;">\n'
        '        <img src="https://img.youtube.com/vi/WQ0qF_Lh0-k/maxresdefault.jpg" alt="限時動態 Action! Figure" loading="lazy" style="width:100%;height:auto;display:block;filter:grayscale(100%) contrast(1.05);transition:filter .35s,transform .55s">\n'
        '        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">\n'
        '          <div style="width:56px;height:56px;background:rgba(200,188,154,.15);border:1px solid rgba(200,188,154,.35);border-radius:50%;display:flex;align-items:center;justify-content:center;">\n'
        '            <div style="width:0;height:0;border-style:solid;border-width:10px 0 10px 18px;border-color:transparent transparent transparent rgba(200,188,154,.8);margin-left:3px"></div>\n'
        '          </div>\n'
        '        </div>\n'
        '      </a>\n'
        '      <div class="wio"><div class="wt" contenteditable="true">限時動態 Action! Figure</div>'
        '<div class="wm" contenteditable="true">Video · 2026 · 點擊前往 YouTube'
        '&nbsp;<div>創作團隊：武威桀 陳彥甫 林慧儒 楊茗柯 鄭欣宜 謝浩理 林廣騎 江育噌</div>'
        '<div>進行式蒸發：動作捕捉舞者身體，生成數位分身漂浮展出空間；觀眾透過手機界面出價競標，拍下的分身隨買家磨磟離開，流標者於演出結束後消失。將「上傳限時動態」的比喻，施加於活生生的身體之上。</div></div></div>\n'
        '      <button class="db" onclick="di(this.parentElement)">✕</button>\n'
        '    </div>\n'
    )
    grid_end = '</div><!-- /grid -->'
    if grid_end in html:
        html = html.replace(grid_end, new_item + grid_end, 1)
        print('Inserted before /grid marker')
    else:
        print('ERROR: grid end marker not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig, len(html), len(html) - orig))
