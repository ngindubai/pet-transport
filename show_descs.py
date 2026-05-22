import re, os

files = [
    ("airline", r"c:\Users\garet\Desktop\pet-transport\site\content\airlines\emirates-skycargo-cargo-division.md"),
    ("airline", r"c:\Users\garet\Desktop\pet-transport\site\content\airlines\swiss-international-air-lines.md"),
    ("breed",   r"c:\Users\garet\Desktop\pet-transport\site\content\breeds\pit-bull-terrier-and-related-types.md"),
    ("blog",    r"c:\Users\garet\Desktop\pet-transport\site\content\blog\australia-pet-quarantine-explained.md"),
    ("blog",    r"c:\Users\garet\Desktop\pet-transport\site\content\blog\global-pet-transport-guide-2026.md"),
    ("blog",    r"c:\Users\garet\Desktop\pet-transport\site\content\blog\singapore-pet-import-category-guide.md"),
]
for pt, fp in files:
    content = open(fp, encoding="utf-8").read()
    m = re.search(r'^description:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        desc = m.group(1).strip().strip('"')
        print(f"[{pt}] {len(desc)} chars:")
        print(f"  {desc}")
        print()
