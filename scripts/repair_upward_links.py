#!/usr/bin/env python3
"""
repair_upward_links.py — Fix broken origin upward links in pet-transport route files.

Root cause: generate_p3_routes_batch1.py used a fallback of
  /pet-transport/origins/{slug}-pet-export-guide/
for origins that only have a plain {slug}.md file (not a -pet-export-guide.md).
This causes 114 hard 404s in GSC.

This script replaces each broken URL with the correct plain-slug URL.
Idempotent: safe to run multiple times.

Usage:
    python scripts/repair_upward_links.py          # dry-run (shows what would change)
    python scripts/repair_upward_links.py --apply  # write changes to disk
"""

import os
import sys
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")

# These 50 origins only have a plain {slug}.md file in site/content/origins/.
# Their upward links must point to /pet-transport/origins/{slug}/
# NOT to /pet-transport/origins/{slug}-pet-export-guide/
PLAIN_SLUG_ORIGINS = [
    "argentina",
    "australia",
    "austria",
    "belgium",
    "brazil",
    "canada",
    "chile",
    "china",
    "colombia",
    "cyprus",
    "czech-republic",
    "denmark",
    "egypt",
    "france",
    "germany",
    "greece",
    "hong-kong",
    "india",
    "indonesia",
    "ireland",
    "israel",
    "italy",
    "japan",
    "kenya",
    "kuwait",
    "malaysia",
    "malta",
    "mexico",
    "netherlands",
    "nigeria",
    "norway",
    "philippines",
    "poland",
    "portugal",
    "qatar",
    "romania",
    "saudi-arabia",
    "singapore",
    "south-africa",
    "south-korea",
    "sri-lanka",
    "sweden",
    "switzerland",
    "taiwan",
    "thailand",
    "turkey",
    "united-arab-emirates",
    "united-kingdom",
    "united-states",
    "vietnam",
]

# Build the substitution map: broken URL -> correct URL
SUBSTITUTIONS = {
    f"/pet-transport/origins/{slug}-pet-export-guide/": f"/pet-transport/origins/{slug}/"
    for slug in PLAIN_SLUG_ORIGINS
}


def repair_file(filepath, apply=False):
    with open(filepath, encoding="utf-8") as f:
        original = f.read()

    modified = original
    changes = []
    for broken, correct in SUBSTITUTIONS.items():
        if broken in modified:
            modified = modified.replace(broken, correct)
            changes.append((broken, correct))

    if not changes:
        return 0

    if apply:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(modified)

    return len(changes)


def main():
    apply = "--apply" in sys.argv
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"repair_upward_links.py [{mode}]")
    print(f"Routes dir: {ROUTES_DIR}")
    print()

    if not os.path.isdir(ROUTES_DIR):
        print(f"ERROR: routes dir not found: {ROUTES_DIR}")
        sys.exit(1)

    total_files = 0
    total_changes = 0

    for filename in sorted(os.listdir(ROUTES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        filepath = os.path.join(ROUTES_DIR, filename)
        n = repair_file(filepath, apply=apply)
        if n:
            total_files += 1
            total_changes += n
            print(f"  {'FIXED' if apply else 'WOULD FIX'}: {filename} ({n} substitution{'s' if n > 1 else ''})")

    print()
    print(f"Summary: {total_files} files {'updated' if apply else 'would be updated'}, {total_changes} substitutions total.")
    if not apply:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
