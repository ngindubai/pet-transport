"""
Fix description length issues:
- Origin hubs: too short (< 100 chars) - expand with specific detail
- Airline/breed/blog: too long (> 175 chars) - trim
"""
import os, re


def fix_description(filepath, old_desc, new_desc):
    content = open(filepath, encoding="utf-8").read()
    old_line = f'description: "{old_desc}"'
    new_line = f'description: "{new_desc}"'
    if old_line not in content:
        old_line = f"description: {old_desc}"
        new_line = f'description: "{new_desc}"'
    if old_line not in content:
        print(f"  WARN: Could not find description in {os.path.basename(filepath)}")
        return False
    new_content = content.replace(old_line, new_line, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  Fixed ({len(old_desc)} -> {len(new_desc)} chars): {os.path.basename(filepath)}")
    return True


ORIGINS  = r"c:\Users\garet\Desktop\pet-transport\site\content\origins"
AIRLINES = r"c:\Users\garet\Desktop\pet-transport\site\content\airlines"
BREEDS   = r"c:\Users\garet\Desktop\pet-transport\site\content\breeds"
BLOG     = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"

# ── Origin hubs: expand short descriptions ───────────────────────────────────
print("=== Origin hubs (expand) ===")
origin_descs = {
    "australia.md": (
        "Guide to exporting your dog or cat from Australia. Export requirements, airlines, and routes.",
        "Exporting your pet from Australia: export health certificate requirements, airline options, and routes from Australia to popular destinations worldwide.",
    ),
    "canada.md": (
        "Guide to exporting your dog or cat from Canada. Export requirements, airlines, and routes.",
        "Exporting your pet from Canada: health certificate requirements, airline options, and routes from Canada to destinations across Europe, Asia, and beyond.",
    ),
    "france.md": (
        "Guide to exporting your dog or cat from France. Export requirements, airlines, and routes.",
        "Exporting your pet from France: EU export health certificate requirements, airline options, and routes from France to popular international destinations.",
    ),
    "germany.md": (
        "Guide to exporting your dog or cat from Germany. Export requirements, airlines, and routes.",
        "Exporting your pet from Germany: EU export health certificate requirements, airline options, and routes from Germany to destinations worldwide.",
    ),
    "hong-kong.md": (
        "Guide to exporting your dog or cat from Hong Kong. Export requirements, airlines, and routes.",
        "Exporting your pet from Hong Kong: AFCD health certificate requirements, airline options, and routes from Hong Kong to popular destinations worldwide.",
    ),
    "new-zealand.md": (
        "Guide to exporting your dog or cat from New Zealand. Export requirements, airlines, and routes.",
        "Exporting your pet from New Zealand: MPI health certificate requirements, airline options, and routes from New Zealand to international destinations.",
    ),
    "singapore.md": (
        "Guide to exporting your dog or cat from Singapore. Export requirements, airlines, and routes.",
        "Exporting your pet from Singapore: AVS health certificate requirements, airline options, and routes from Singapore to popular destinations worldwide.",
    ),
    "south-africa.md": (
        "Guide to exporting your dog or cat from South Africa. Export requirements, airlines, and routes.",
        "Exporting your pet from South Africa: DAFF health certificate requirements, airline options, and routes from South Africa to popular destinations.",
    ),
    "spain.md": (
        "Guide to exporting your dog or cat from Spain. Export requirements, airlines, and routes.",
        "Exporting your pet from Spain: EU export health certificate requirements, airline options, and routes from Spain to popular international destinations.",
    ),
    "united-kingdom.md": (
        "Guide to exporting your dog or cat from United Kingdom. Export requirements, airlines, and routes.",
        "Exporting your pet from the UK: APHA health certificate requirements, airline options, and routes from the United Kingdom to popular destinations.",
    ),
    "united-states.md": (
        "Guide to exporting your dog or cat from United States. Export requirements, airlines, and routes.",
        "Exporting your pet from the United States: USDA APHIS health certificate requirements, airline options, and routes from the USA to destinations worldwide.",
    ),
}
for fn, (old, new) in origin_descs.items():
    path = os.path.join(ORIGINS, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    fix_description(path, old, new)

# ── Airline descriptions: trim ─────────────────────────────────────────────
print("\n=== Airline descriptions (trim) ===")
airline_descs = {
    "emirates-skycargo-cargo-division.md": (
        "Emirates SkyCargo (cargo division) pet transport policy: cabin rules, cargo service, breed restrictions, crate requirements, and how to book your pet on Emirates SkyCargo (cargo division).",
        "Emirates SkyCargo pet transport policy: cargo service details, breed restrictions, crate requirements, and how to book your pet as air cargo.",
    ),
    "swiss-international-air-lines.md": (
        "Swiss International Air Lines pet transport policy: cabin rules, cargo service, breed restrictions, crate requirements, and how to book your pet on Swiss International Air Lines.",
        "Swiss International Air Lines pet transport policy: cabin and cargo rules, breed restrictions, crate requirements, and how to book your pet on SWISS.",
    ),
}
for fn, (old, new) in airline_descs.items():
    path = os.path.join(AIRLINES, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    fix_description(path, old, new)

# ── Breed description: trim ───────────────────────────────────────────────────
print("\n=== Breed descriptions (trim) ===")
breed_descs = {
    "pit-bull-terrier-and-related-types.md": (
        "Which countries ban or restrict Pit Bull Terrier (and related types) import, and what it means for international relocation. Country-by-country breakdown with current regulations.",
        "Which countries ban or restrict Pit Bull Terrier imports, and what it means for international relocation. Country-by-country breakdown with current regulations.",
    ),
}
for fn, (old, new) in breed_descs.items():
    path = os.path.join(BREEDS, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    fix_description(path, old, new)

# ── Blog descriptions: trim ────────────────────────────────────────────────
print("\n=== Blog descriptions (trim) ===")
blog_descs = {
    "australia-pet-quarantine-explained.md": (
        "Australia requires mandatory quarantine for every imported dog and cat. Here's what happens at Mickleham, how long it takes, and what the 180-day titre test rule actually means.",
        "Australia requires mandatory quarantine for every imported dog and cat. What happens at Mickleham, how long it takes, and what the 180-day titre test rule means.",
    ),
    "global-pet-transport-guide-2026.md": (
        "The most complete free reference for international pet transport in 2026. Quarantine rankings, airline comparison tables, titre test requirements, and cost estimates for 25 countries.",
        "The most complete free reference for international pet transport in 2026. Quarantine rankings, airline comparison, titre test requirements, and cost estimates for 25 countries.",
    ),
    "singapore-pet-import-category-guide.md": (
        "Singapore classifies pet origin countries into three categories with different quarantine requirements. Here's what Category A, B and C means and which category your country is in.",
        "Singapore classifies pet countries into three categories with different quarantine requirements. What Category A, B and C means and which category your country falls into.",
    ),
}
for fn, (old, new) in blog_descs.items():
    path = os.path.join(BLOG, fn)
    if not os.path.exists(path):
        print(f"  MISSING: {fn}")
        continue
    fix_description(path, old, new)

print("\nAll description fixes complete.")
