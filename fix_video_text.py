#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix team names and description text for 限時動態 Action! Figure."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

old_wm = (
    '<div class="wm" contenteditable="true">Video &middot; 2026 &middot; 點擊前往 YouTube'
    '&nbsp;<div>創作團隊：武威栗 陳彥甫 林慧儲 楊茗柯 鄭欣宜 謝浩理 林廣騎 江育瘍</div>'
    '<div>進行式蒸發：動作捕捉舞者身體，生成數位分身漂浮展出空間；觀眾透過手機界面出價競標，拍下的分身隨買家磁碟離開，流標者於演出結束後消失。將「上傳限時動態」的比喻，施加於活生生的身體之上。</div>'
    '</div>'
)

new_wm = (
    '<div class="wm" contenteditable="true">Video &middot; 2026 &middot; 點擊前往 YouTube'
    '&nbsp;<div>創作團隊：武威桀 陳彥甫 林慧儒 楊茗柯 鄭欣怡 謝浩理 林廣騏 江育葳</div>'
    '<div>透過科技，動作可以被即時捕捉、數位複製、定價出售。一具勞動的肉身在舞台上持續產出動作，每一個動作被掃描成獨立的數位副本，漂浮於現場空間。觀眾以手機進入競標介面，選擇購買哪一個。被選中的副本離場，進入買家的硬碟；未被選中的，在演出結束時消失。</div>'
    '<div>這件作品把當代最普遍的日常行為「上傳限時動態」，從手機螢幕移至藝術館。我們每天生產、上架、然後失去那些只屬於24小時內的自己。沒有人質疑這個過程，因為我們從未把生命這個詞用在那些消失的內容上。</div>'
    '<div>但這件作品中漂浮的副本不是隨機檔案。它們承載一位舞者的真實肌肉、骨骼、平衡與呼吸，是從活著的身體上取下的、獨立存在於現場的副本。它們在15分鐘的演出中構成一種新的生命範疇：被剝奪了演化能力、由市場決定存活、沒有任何法律或倫理保護的生命。</div>'
    '<div>被選擇的，被擁有；沒被選擇的，消失。沒有殺戮，沒有屍體，沒有聲音。這是之後生命被處理的方式——不是被殺死，而是不再被觀看。</div>'
    '</div>'
)

if old_wm in html:
    html = html.replace(old_wm, new_wm, 1)
    print('Fixed.')
else:
    print('ERROR: pattern not found.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig, len(html), len(html) - orig))
