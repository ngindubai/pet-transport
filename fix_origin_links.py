"""Fix broken origin hub links in all route, country, and origin .md files.

Short slug /pet-transport/origins/australia/ -> /pet-transport/origins/pet-export-guide-shipping-from-australia/
"""
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent

ORIGIN_SLUG_MAP = {
    # P1 origins (pet-export-guide-shipping-from-*)
    "australia": "pet-export-guide-shipping-from-australia",
    "canada": "pet-export-guide-shipping-from-canada",
    "france": "pet-export-guide-shipping-from-france",
    "germany": "pet-export-guide-shipping-from-germany",
    "hong-kong": "pet-export-guide-shipping-from-hong-kong",
    "new-zealand": "pet-export-guide-shipping-from-new-zealand",
    "singapore": "pet-export-guide-shipping-from-singapore",
    "south-africa": "pet-export-guide-shipping-from-south-africa",
    "spain": "pet-export-guide-shipping-from-spain",
    "united-arab-emirates": "pet-export-guide-shipping-from-united-arab-emirates",
    "united-kingdom": "pet-export-guide-shipping-from-united-kingdom",
    "united-states": "pet-export-guide-shipping-from-united-states",
    # P2 origins (shipping-your-pet-from-*-export-guide)
    "brazil": "shipping-your-pet-from-brazil-export-guide",
    "denmark": "shipping-your-pet-from-denmark-export-guide",
    "greece": "shipping-your-pet-from-greece-export-guide",
    "india": "shipping-your-pet-from-india-export-guide",
    "indonesia": "shipping-your-pet-from-indonesia-export-guide",
    "italy": "shipping-your-pet-from-italy-export-guide",
    "japan": "shipping-your-pet-from-japan-export-guide",
    "malaysia": "shipping-your-pet-from-malaysia-export-guide",
    "mexico": "shipping-your-pet-from-mexico-export-guide",
    "netherlands": "shipping-your-pet-from-netherlands-export-guide",
    "philippines": "shipping-your-pet-from-philippines-export-guide",
    "portugal": "shipping-your-pet-from-portugal-export-guide",
    "south-korea": "shipping-your-pet-from-south-korea-export-guide",
    "switzerland": "shipping-your-pet-from-switzerland-export-guide",
    "thailand": "shipping-your-pet-from-thailand-export-guide",
}

# Directories to fix
dirs_to_scan = [
    REPO_ROOT / "site" / "content" / "routes",
    REPO_ROOT / "site" / "content" / "countries",
    REPO_ROOT / "site" / "content" / "origins",
]

total_fixed = 0

for scan_dir in dirs_to_scan:
    for md_file in scan_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        original = content
        changed = False

        for short_slug, full_slug in ORIGIN_SLUG_MAP.items():
            old = f"/pet-transport/origins/{short_slug}/"
            new = f"/pet-transport/origins/{full_slug}/"
            if old in content:
                content = content.replace(old, new)
                changed = True

        if changed:
            md_file.write_text(content, encoding="utf-8")
            # Count replacements
            fixes = sum(1 for s in ORIGIN_SLUG_MAP if
                        f"/pet-transport/origins/{s}/" in original)
            total_fixed += 1
            print(f"  Fixed: {md_file.name}")

print(f"\nDone. Fixed {total_fixed} files.")
