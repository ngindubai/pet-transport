#!/usr/bin/env python3
"""
fix_p4_qa_issues.py — Fix QA audit issues in P4 route files:
  1. Replace banned word 'navigate' (and 'navigating') with neutral synonyms
  2. Fix broken airline links:
     - /pet-transport/airlines/klm/ → /pet-transport/airlines/klm-royal-dutch-airlines/
     - Remove lines with air-china, egyptair, kenya-airways, qatar-airways,
       vietnam-airlines, air-india from upward/sideways link lists
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")

# Broken airline slugs to REMOVE entirely from link lists
REMOVE_AIRLINE_SLUGS = {
    "air-china",
    "egyptair",
    "kenya-airways",
    "qatar-airways",
    "vietnam-airlines",
    "air-india",
}

# Airline slugs to RENAME (old → new)
RENAME_AIRLINE_SLUGS = {
    "/pet-transport/airlines/klm/": "/pet-transport/airlines/klm-royal-dutch-airlines/",
}

NAVIGATE_REPLACEMENTS = [
    # Most common patterns first
    (r'\bnavigating the\b', 'handling the'),
    (r'\bnavigating\b', 'working through'),
    (r'\bnavigate the\b', 'handle the'),
    (r'\bnavigate\b', 'use'),
]


def remove_airline_link_block(text, slug):
    """Remove a YAML list item block containing the given airline slug URL."""
    # Match the list item that contains the airline slug (multi-line YAML block)
    # Pattern: "    - url: ..." followed by indented sub-lines
    pattern = re.compile(
        r'\n    - url: "/pet-transport/airlines/' + re.escape(slug) + r'/[^"]*"'
        r'(?:\n      [^\n]+)*',
        re.MULTILINE
    )
    new_text, count = pattern.subn('', text)
    if count == 0:
        # Also try single-line or slightly different indent
        pattern2 = re.compile(
            r'\n\s+- url: "/pet-transport/airlines/' + re.escape(slug) + r'/?"'
            r'(?:\n\s+[^\n]+)*',
            re.MULTILINE
        )
        new_text, count = pattern2.subn('', text)
    return new_text, count


def fix_route_file(path):
    """Fix a single route file. Returns (navigate_fixed, airlines_removed, airlines_renamed)."""
    with open(path, encoding='utf-8') as f:
        text = f.read()

    original = text
    nav_count = 0
    removed_count = 0
    renamed_count = 0

    # 1. Fix navigate/navigating
    for pattern, replacement in NAVIGATE_REPLACEMENTS:
        new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        if new_text != text:
            nav_count += text.count(re.sub(r'\\b', '', pattern).replace('\\', ''))
            text = new_text

    # 2. Rename airline slugs
    for old_url, new_url in RENAME_AIRLINE_SLUGS.items():
        if old_url in text:
            count = text.count(old_url)
            text = text.replace(old_url, new_url)
            renamed_count += count

    # 3. Remove broken airline links
    for slug in REMOVE_AIRLINE_SLUGS:
        if slug in text:
            text, count = remove_airline_link_block(text, slug)
            removed_count += count

    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True, nav_count, removed_count, renamed_count
    return False, 0, 0, 0


def main():
    route_files = glob.glob(os.path.join(ROUTES_DIR, "*.md"))
    print(f"Processing {len(route_files)} route files...")

    changed = nav_total = removed_total = renamed_total = 0
    for path in route_files:
        was_changed, nav, removed, renamed = fix_route_file(path)
        if was_changed:
            changed += 1
            nav_total += nav
            removed_total += removed
            renamed_total += renamed

    print(f"Files changed: {changed}")
    print(f"  navigate/navigating occurrences fixed: (in {changed} files)")
    print(f"  Broken airline links removed: ~{removed_total} blocks")
    print(f"  KLM links renamed: ~{renamed_total}")

    # Verify
    em = chr(8212)
    nav_remaining = sum(1 for p in route_files if re.search(r'\bnavigate\b|\bnavigating\b', open(p, encoding='utf-8').read(), re.IGNORECASE))
    broken_remaining = sum(1 for p in route_files if any(f'/airlines/{s}/' in open(p, encoding='utf-8').read() for s in REMOVE_AIRLINE_SLUGS))
    klm_remaining = sum(1 for p in route_files if '/airlines/klm/' in open(p, encoding='utf-8').read())
    print(f"\nVerification:")
    print(f"  Files still with navigate/navigating: {nav_remaining}")
    print(f"  Files still with broken airline links: {broken_remaining}")
    print(f"  Files still with /klm/ (old slug): {klm_remaining}")


if __name__ == "__main__":
    main()
