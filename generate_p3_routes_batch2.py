"""
Phase 3 / Task 3.3 Batch 2: P3 Route Page Generation
50 more P3 route pages covering the next priority tier:
Kuwait, China expansion, Vietnam/Taiwan return legs, Nordic/EU,
Czech/Romania/Malta/Cyprus, Latin America to UK, Africa/South Asia expansion.
Skip-if-exists: never overwrites existing files.
Imports all shared logic from generate_p3_routes_batch1.
"""

import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

# ============================================================
# BATCH 2 ROUTES — 50 routes, no overlap with Batch 1
# ============================================================
P3_ROUTES_BATCH2 = [
    # Kuwait
    ("Kuwait", "UK"),
    ("UK", "Kuwait"),

    # Middle East expansion
    ("Australia", "Saudi_Arabia"),
    ("Saudi_Arabia", "Australia"),
    ("Australia", "Qatar"),
    ("Qatar", "Australia"),
    ("Australia", "Israel"),
    ("Israel", "Australia"),
    ("USA", "Israel"),
    ("USA", "Saudi_Arabia"),

    # China expansion (more P1/P2 pairs)
    ("China", "Germany"),
    ("Germany", "China"),
    ("China", "France"),
    ("France", "China"),
    ("China", "Singapore"),
    ("Singapore", "China"),
    ("China", "Hong_Kong"),
    ("Hong_Kong", "China"),

    # Vietnam / Taiwan return legs + new pairs
    ("Vietnam", "UK"),
    ("Taiwan", "UK"),
    ("Vietnam", "USA"),
    ("USA", "Vietnam"),
    ("Taiwan", "Canada"),
    ("Taiwan", "Germany"),

    # Nordic expansion
    ("Norway", "Australia"),
    ("Australia", "Norway"),
    ("Sweden", "Australia"),
    ("Sweden", "Germany"),
    ("Austria", "Germany"),

    # EU new countries
    ("Czech_Republic", "UK"),
    ("UK", "Czech_Republic"),
    ("Romania", "UK"),
    ("UK", "Romania"),
    ("Malta", "UK"),
    ("UK", "Malta"),
    ("Cyprus", "UK"),
    ("UK", "Cyprus"),

    # Ireland expansion
    ("Ireland", "Canada"),
    ("Ireland", "Singapore"),
    ("Ireland", "Netherlands"),

    # Norway extra
    ("Norway", "Germany"),

    # Latin America to UK
    ("Argentina", "UK"),
    ("Chile", "UK"),
    ("Colombia", "UK"),

    # Africa / South Asia expansion
    ("Egypt", "Australia"),
    ("Kenya", "Australia"),
    ("South_Africa", "Kenya"),
    ("Sri_Lanka", "Australia"),
    ("India", "Sri_Lanka"),
]


# ============================================================
# MAIN
# ============================================================
def main():
    generated = 0
    skipped = 0
    errors = 0

    print(f"Generating P3 Batch 2 routes... {len(P3_ROUTES_BATCH2)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH2:
        if origin_key not in COUNTRY_REGISTRY:
            print(f"  ERROR (unknown origin): {origin_key}")
            errors += 1
            continue
        if dest_key not in COUNTRY_REGISTRY:
            print(f"  ERROR (unknown dest): {dest_key}")
            errors += 1
            continue

        origin_slug = COUNTRY_REGISTRY[origin_key][2]
        dest_slug = COUNTRY_REGISTRY[dest_key][2]
        filename = f"{origin_slug}-to-{dest_slug}.md"
        filepath = os.path.join(CONTENT_DIR, filename)

        if os.path.exists(filepath):
            print(f"  SKIP (exists): {filename}")
            skipped += 1
            continue

        try:
            content = generate_route_markdown(origin_key, dest_key)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  OK: {filename}")
            generated += 1
        except Exception as e:
            print(f"  ERROR ({filename}): {e}")
            errors += 1

    print(f"\nRoutes generated: {generated} | skipped: {skipped} | errors: {errors}")


if __name__ == "__main__":
    main()
