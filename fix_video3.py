#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

old = (
    '<div class="wm" contenteditable="true">Video &middot; 2026 &middot; 點擊前往 YouTube'
    '&nbsp;<div>創作團隊：武威桀 陳彥甫 林慧儒 楊茗柯 鄭欣怡 謝浩理 林廣騏 江育葳</div>'
    '<div>進行式蒸發：動作捕捉舞者身體，生成數位分身漂浮展出空間；觀眾透過手機界面出價競標，拍下的分身隨買家下載離開，流標者於演出結束後被消失。將「上傳限時動態」的比喻，施加於活生生的數位身體之上。</div></div>'
)

new = (
    '<div class="wm" contenteditable="true">Video &middot; 2026 &middot; 點擊前往 YouTube'
    '<br><div>創作團隊：武威桀 陳彥甫 林慧儒 楊茗柯 鄭欣怡 謝浩理 林廣騏 江育葳</div>'
    '<div>動作捕捉舞者身體，生成數位分身漂浮展出空間；觀眾透過手機界面出價競標，拍下的分身隨買家下載離開，流標者於演出結束後被消失。將「上傳限時動態」的比喻，施加於活生生的數位身體之上。</div></div>'
)

if old in html:
    html = html.replace(old, new, 1)
    print('Fixed.')
else:
    print('Pattern not found.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: {:+,}'.format(orig, len(html), len(html)-orig))
