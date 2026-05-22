"""
Fix title length issues:
- Long route titles (> 75 chars): shorten to "Pet Transport [Origin] to [Dest] | PetTransportGlobal"
- Short country titles (< 30 chars): append brand name
- Long breed titles (> 75 chars): shorten pattern
- Long blog title: shorten
"""
import os, re

def fix_title(filepath, old_title, new_title):
    content = open(filepath, encoding="utf-8").read()
    # Escape for replacement
    old_line = f'title: "{old_title}"'
    new_line = f'title: "{new_title}"'
    if old_line not in content:
        # Try without quotes
        old_line = f"title: {old_title}"
        new_line = f'title: "{new_title}"'
    if old_line not in content:
        print(f"  WARN: Could not find title in {os.path.basename(filepath)}")
        return False
    new_content = content.replace(old_line, new_line, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  Fixed: {os.path.basename(filepath)}: {len(new_title)} chars")
    return True


ROUTES = r"c:\Users\garet\Desktop\pet-transport\site\content\routes"
COUNTRIES = r"c:\Users\garet\Desktop\pet-transport\site\content\countries"
BREEDS = r"c:\Users\garet\Desktop\pet-transport\site\content\breeds"
BLOG = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"

# ── Route title fixes ─────────────────────────────────────────────────────────
# Pattern: "Shipping Dogs & Cats from X to Y | PetTransportGlobal" → "Pet Transport X to Y | PetTransportGlobal"
route_fixes = {
    "mexico-to-united-arab-emirates.md":
        "Pet Transport Mexico to UAE | PetTransportGlobal",
    "netherlands-to-united-arab-emirates.md":
        "Pet Transport Netherlands to UAE | PetTransportGlobal",
    "philippines-to-united-kingdom.md":
        "Pet Transport Philippines to UK | PetTransportGlobal",
    "switzerland-to-united-arab-emirates.md":
        "Pet Transport Switzerland to UAE | PetTransportGlobal",
    "thailand-to-united-arab-emirates.md":
        "Pet Transport Thailand to UAE | PetTransportGlobal",
    "united-arab-emirates-to-italy.md":
        "Pet Transport UAE to Italy | PetTransportGlobal",
    "united-arab-emirates-to-portugal.md":
        "Pet Transport UAE to Portugal | PetTransportGlobal",
    "united-arab-emirates-to-south-korea.md":
        "Pet Transport UAE to South Korea | PetTransportGlobal",
    "united-arab-emirates-to-switzerland.md":
        "Pet Transport UAE to Switzerland | PetTransportGlobal",
    "united-arab-emirates-to-thailand.md":
        "Pet Transport UAE to Thailand | PetTransportGlobal",
    "united-kingdom-to-netherlands.md":
        "Pet Transport UK to Netherlands | PetTransportGlobal",
}

print("=== Route titles ===")
for fn, new_title in route_fixes.items():
    path = os.path.join(ROUTES, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    content = open(path, encoding="utf-8").read()
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        old_title = m.group(1).strip().strip('"')
        fix_title(path, old_title, new_title)

# ── Country title fixes ───────────────────────────────────────────────────────
print("\n=== Country titles ===")
country_fixes = {
    "new-zealand.md": "Pet Import Rules: New Zealand | PetTransportGlobal",
    "spain.md":       "Pet Import Rules: Spain | PetTransportGlobal",
}
for fn, new_title in country_fixes.items():
    path = os.path.join(COUNTRIES, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    content = open(path, encoding="utf-8").read()
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        old_title = m.group(1).strip().strip('"')
        fix_title(path, old_title, new_title)

# ── Breed title fixes ─────────────────────────────────────────────────────────
print("\n=== Breed titles ===")
breed_fixes = {
    "american-staffordshire-terrier.md":
        "American Staffordshire Terrier: Country Import Restrictions",
    "perro-de-presa-canario.md":
        "Perro de Presa Canario: Country Import Restrictions",
    "pit-bull-terrier-and-related-types.md":
        "Pit Bull Terrier: Country Import Restrictions by Country",
    "staffordshire-bull-terrier.md":
        "Staffordshire Bull Terrier: Country Import Restrictions",
}
for fn, new_title in breed_fixes.items():
    path = os.path.join(BREEDS, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    content = open(path, encoding="utf-8").read()
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        old_title = m.group(1).strip().strip('"')
        fix_title(path, old_title, new_title)

# ── Blog title fix ────────────────────────────────────────────────────────────
print("\n=== Blog titles ===")
blog_fixes = {
    "global-pet-transport-guide-2026.md":
        "Global Pet Transport Guide 2026: Country Rules, Costs & Airlines",
}
for fn, new_title in blog_fixes.items():
    path = os.path.join(BLOG, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    content = open(path, encoding="utf-8").read()
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        old_title = m.group(1).strip().strip('"')
        fix_title(path, old_title, new_title)

print("\nAll title fixes complete.")
