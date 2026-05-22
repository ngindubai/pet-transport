import re
import os

def minify_css(css):
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    css = re.sub(r'\s*([:{};,>~+])\s*', r'\1', css)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r';+}', '}', css)
    return css.strip()

files = [
    'site/static/css/style.css',
    'site/static/css/plugins.css',
    'site/static/fonts/flaticon/flaticon.css',
    'site/static/styles/maincolors.css',
]

for f in files:
    orig_size = os.path.getsize(f)
    with open(f, 'r', encoding='utf-8', errors='replace') as fh:
        css = fh.read()
    minified = minify_css(css)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(minified)
    new_size = os.path.getsize(f)
    pct = (1 - new_size/orig_size) * 100
    print(f'{f}: {orig_size} -> {new_size} bytes ({pct:.1f}% reduction)')

print('Done.')
