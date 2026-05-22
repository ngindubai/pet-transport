import os, re

for dirname, page_type in [("routes","route"),("countries","country"),("origins","origin"),("airlines","airline"),("breeds","breed"),("blog","blog")]:
    d = r"c:\Users\garet\Desktop\pet-transport\site\content\\" + dirname
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md") or fn == "_index.md":
            continue
        content = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.search(r'^description:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if not m:
            continue
        desc = m.group(1).strip().strip('"')
        if len(desc) > 175 or len(desc) < 100:
            print(f"[{page_type}] {fn}: {len(desc)} chars")
            print(f"  {desc[:120]}")
