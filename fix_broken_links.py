"""
Fix 41 broken internal links:
1. /pet-transport/airlines/klm/ -> /pet-transport/airlines/klm-royal-dutch-airlines/ (21 files)
2. Remove /pet-transport/airlines/air-india/ and its text: line (21 files)
3. Fix broken reverse route in spain-to-united-kingdom.md
"""
import os, re

ROUTES = r"c:\Users\garet\Desktop\pet-transport\site\content\routes"
COUNTRIES = r"c:\Users\garet\Desktop\pet-transport\site\content\countries"

fixed_klm = 0
fixed_ai = 0

for fn in sorted(os.listdir(ROUTES)):
    if not fn.endswith(".md") or fn == "_index.md":
        continue
    path = os.path.join(ROUTES, fn)
    content = open(path, encoding="utf-8").read()
    changed = False

    # Fix KLM link
    if '"/pet-transport/airlines/klm/"' in content:
        content = content.replace(
            '"/pet-transport/airlines/klm/"',
            '"/pet-transport/airlines/klm-royal-dutch-airlines/"'
        )
        changed = True
        fixed_klm += 1

    # Remove Air India link block (2 lines: url + text)
    if '"/pet-transport/airlines/air-india/"' in content:
        # Remove the entry: '    - url: "/pet-transport/airlines/air-india/"\n      text: "Air India pet policy"\n'
        content = re.sub(
            r'    - url: "/pet-transport/airlines/air-india/"\n      text: "[^"]+"\n',
            '',
            content
        )
        changed = True
        fixed_ai += 1

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print(f"KLM links fixed: {fixed_klm}")
print(f"Air India links removed: {fixed_ai}")

# Fix spain-to-uk: replace broken reverse route sideways link with origin hub link
spain_uk_path = os.path.join(ROUTES, "spain-to-united-kingdom.md")
content = open(spain_uk_path, encoding="utf-8").read()
if '"/pet-transport/united-kingdom-to-spain/"' in content:
    # Replace with the Spain origin hub (valid) - already in upward links probably
    # Just remove this specific sideways entry since the reverse route doesn't exist
    content = re.sub(
        r'    - url: "/pet-transport/united-kingdom-to-spain/"\n      text: "[^"]+"\n',
        '',
        content
    )
    with open(spain_uk_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("spain-to-united-kingdom.md: broken reverse route link removed")
else:
    print("spain-to-uk: link not found (may already be fixed)")

# Fix United States country guide: "landscape" -> "picture"
us_path = r"c:\Users\garet\Desktop\pet-transport\site\content\countries\united-states.md"
content = open(us_path, encoding="utf-8").read()
if re.search(r"\blandscape\b", content, re.I):
    content = re.sub(r"\blandscape\b", "picture", content, flags=re.I)
    with open(us_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("united-states.md: 'landscape' fixed")

print("\nAll broken link fixes complete.")
