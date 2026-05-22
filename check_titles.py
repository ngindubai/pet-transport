import os, re

for dirname, page_type in [("routes", "route"), ("countries", "country"), ("breeds", "breed"), ("blog", "blog"), ("airlines", "airline"), ("origins", "origin")]:
    d = r"c:\Users\garet\Desktop\pet-transport\site\content\\" + dirname
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md") or fn == "_index.md":
            continue
        content = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if not m:
            continue
        title = m.group(1).strip().strip('"')
        if len(title) > 75 or len(title) < 30:
            print(f"[{page_type}] {fn}: {len(title)} chars: {title}")
