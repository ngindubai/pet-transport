"""
Phase 3 / Task 3.3 Batch 3: P3 Route Page Generation
50 more P3 route pages — Turkey expansion, Middle East x Germany,
China x Japan/Korea/NL, Vietnam expansion, Taiwan x Japan,
Sri Lanka/Nigeria/Egypt/Kenya to US, Ireland expansion, Latin America x Spain/Germany.
Skip-if-exists: never overwrites existing files.
Imports all shared logic from generate_p3_routes_batch1.
"""

import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

P3_ROUTES_BATCH3 = [
    # Turkey expansion
    ("Turkey", "Australia"),
    ("Australia", "Turkey"),
    ("Turkey", "Germany"),
    ("Germany", "Turkey"),
    ("Turkey", "USA"),
    ("USA", "Turkey"),

    # Israel expansion
    ("Israel", "Germany"),
    ("Germany", "Israel"),
    ("Israel", "Canada"),
    ("Canada", "Israel"),

    # Gulf x Germany
    ("Saudi_Arabia", "Germany"),
    ("Germany", "Saudi_Arabia"),
    ("Qatar", "Germany"),
    ("Germany", "Qatar"),

    # China x Asia/Europe
    ("China", "Japan"),
    ("Japan", "China"),
    ("China", "South Korea"),
    ("South Korea", "China"),
    ("China", "Netherlands"),
    ("Netherlands", "China"),

    # Vietnam expansion
    ("Vietnam", "Germany"),
    ("Germany", "Vietnam"),
    ("Vietnam", "Singapore"),
    ("Singapore", "Vietnam"),
    ("Vietnam", "France"),
    ("France", "Vietnam"),

    # Taiwan x Japan
    ("Taiwan", "Japan"),
    ("Japan", "Taiwan"),

    # Sri Lanka x USA
    ("Sri_Lanka", "USA"),
    ("USA", "Sri_Lanka"),

    # Ireland expansion
    ("Ireland", "Spain"),
    ("Ireland", "Italy"),
    ("Ireland", "Switzerland"),
    ("Ireland", "Hong_Kong"),
    ("Ireland", "Norway"),
    ("Norway", "Ireland"),
    ("Ireland", "South_Africa"),

    # Nigeria expansion
    ("Nigeria", "USA"),
    ("USA", "Nigeria"),
    ("Nigeria", "Germany"),
    ("Nigeria", "Australia"),

    # Egypt x US/Germany
    ("Egypt", "Germany"),
    ("Egypt", "USA"),

    # Kenya x US/Germany
    ("Kenya", "USA"),
    ("Kenya", "Germany"),

    # Latin America x Spain/Germany
    ("Argentina", "Spain"),
    ("Argentina", "Germany"),
    ("Chile", "Spain"),

    # Gulf x Singapore
    ("Saudi_Arabia", "Singapore"),
    ("Singapore", "Saudi_Arabia"),
]


def main():
    generated = 0
    skipped = 0
    errors = 0

    print(f"Generating P3 Batch 3 routes... {len(P3_ROUTES_BATCH3)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH3:
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
