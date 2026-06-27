#!/usr/bin/env python3
import os, base64, shutil

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CHUNKS_DIR = os.path.join(REPO_ROOT, '.tmp_acc')
ASSETS_DIR = os.path.join(REPO_ROOT, 'assets', 'acc')
INDEX_HTML = os.path.join(REPO_ROOT, 'index.html')

IMAGES = {
    'acc08': [f'acc08_p{i}.txt' for i in range(1, 4)],
    'acc09': [f'acc09_p{i}.txt' for i in range(1, 5)],
    'acc10': [f'acc10_p{i}.txt' for i in range(1, 4)],
    'acc11': [f'acc11_p{i}.txt' for i in range(1, 6)],
    'acc12': [f'acc12_p{i}.txt' for i in range(1, 4)],
    'acc13': [f'acc13_p{i}.txt' for i in range(1, 4)],
    'acc14': [f'acc14_p{i}.txt' for i in range(1, 5)],
    'acc15': [f'acc15_p{i}.txt' for i in range(1, 4)],
}

os.makedirs(ASSETS_DIR, exist_ok=True)

for img_name, parts in IMAGES.items():
    b64 = ''
    for part in parts:
        path = os.path.join(CHUNKS_DIR, part)
        with open(path) as f:
            b64 += f.read().strip()
    data = base64.b64decode(b64)
    out_path = os.path.join(ASSETS_DIR, f'{img_name}.jpg')
    with open(out_path, 'wb') as f:
        f.write(data)
    print(f'Written {out_path} ({len(data)} bytes)')

GRID_ITEMS = ''.join([
    f'<div class="wi fi vis" data-cat="accessories" style="" draggable="false">'
    f'<img src="assets/acc/acc{i:02d}.jpg" alt="" loading="lazy" style="width:100%;height:auto;display:block">'
    f'<div class="wio"><div class="wt" contenteditable="true">Accessories</div>'
    f'<div class="wm" contenteditable="true">Accessories</div></div>'
    f'<button class="db" onclick="di(this.parentElement)">&#x2715;</button>'
    f'</div>\n'
    for i in range(1, 16)
])

MARKER = '</div><!-- /grid -->'
with open(INDEX_HTML) as f:
    html = f.read()
if MARKER in html and 'acc01.jpg' not in html:
    html = html.replace(MARKER, GRID_ITEMS + MARKER)
    with open(INDEX_HTML, 'w') as f:
        f.write(html)
    print('Patched index.html')
else:
    print('index.html not patched (marker missing or already patched)')

shutil.rmtree(CHUNKS_DIR, ignore_errors=True)
print('Cleaned up .tmp_acc/')
os.remove(__file__)
print('Self-deleted')
