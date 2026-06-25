#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add artwork '限時動態 Action! Figure' to works video tab."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
orig = len(html)

new_item = '''<div class="wi" data-cat="video">
  <a href="https://www.youtube.com/watch?v=WQ0qF_Lh0-k" target="_blank" rel="noopener">
    <img src="https://img.youtube.com/vi/WQ0qF_Lh0-k/maxresdefault.jpg" alt="限時動態 Action! Figure" loading="lazy">
    <div class="wio">
      <div class="wt">限時動態 Action! Figure</div>
      <div class="wm">2026 ／ 行為藝術・互動裝置</div>
    </div>
  </a>
</div>'''

# Insert before closing of grid div
marker = '</div><!-- /grid -->'
if 'add_video_action_figure' not in html:
    if marker in html:
        html = html.replace(marker, new_item + '\n' + marker, 1)
        print('Inserted via /grid marker')
    else:
        # fallback: find grid div end
        idx = html.find('id="grid"')
        if idx != -1:
            # find the closing </div> of the grid
            # search for pattern of last .wi closing then </div>
            close = html.rfind('</div>', 0, html.find('</section>', idx))
            html = html[:close] + new_item + '\n' + html[close:]
            print('Inserted via rfind fallback')
        else:
            print('ERROR: could not find insertion point')

    # Tag so we don't double-insert
    html = html.replace('add_video_action_figure', 'add_video_action_figure', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Original: {:,} | New: {:,} | Delta: +{:,}'.format(orig, len(html), len(html) - orig))
