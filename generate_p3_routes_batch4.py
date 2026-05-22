"""
P3 Route Pages — Batch 4 (50 routes)
Covers: EU internal corridors, Latin America x EU, Gulf x EU, Africa x EU,
        SE Asia expansion, Nordic x AU/NL, South Asia x CA/SG, China x CA/AU
Imports shared logic from generate_p3_routes_batch1.py
"""
import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

P3_ROUTES_BATCH4 = [
    # EU internal / Germany hub
    ("Poland", "Germany"),
    ("Germany", "Poland"),
    ("Belgium", "Germany"),
    ("Germany", "Belgium"),
    ("Czech_Republic", "Germany"),
    ("Germany", "Czech_Republic"),
    ("Romania", "Germany"),
    ("Germany", "Romania"),
    ("Austria", "Germany"),
    ("Germany", "Austria"),
    # Latin America x EU
    ("Colombia", "Germany"),
    ("Germany", "Colombia"),
    ("Argentina", "France"),
    ("France", "Argentina"),
    ("Chile", "Germany"),
    ("Germany", "Chile"),
    ("Colombia", "France"),
    ("France", "Colombia"),
    # Gulf x EU
    ("Saudi_Arabia", "Germany"),
    ("Germany", "Saudi_Arabia"),
    ("Qatar", "France"),
    ("France", "Qatar"),
    ("Kuwait", "Germany"),
    ("Germany", "Kuwait"),
    ("Qatar", "Germany"),
    ("Germany", "Qatar"),
    # Africa x EU
    ("Egypt", "France"),
    ("France", "Egypt"),
    ("Kenya", "France"),
    ("France", "Kenya"),
    ("Nigeria", "France"),
    ("France", "Nigeria"),
    ("Egypt", "Netherlands"),
    ("Nigeria", "Netherlands"),
    # SE Asia expansion
    ("Vietnam", "Australia"),
    ("Australia", "Vietnam"),
    ("Vietnam", "Canada"),
    ("Canada", "Vietnam"),
    ("Taiwan", "Singapore"),
    ("Singapore", "Taiwan"),
    ("Taiwan", "France"),
    ("France", "Taiwan"),
    # Nordic x NL/AU
    ("Norway", "Netherlands"),
    ("Netherlands", "Norway"),
    ("Sweden", "Netherlands"),
    ("Netherlands", "Sweden"),
    ("Norway", "Australia"),
    ("Sweden", "Australia"),
    # South Asia x CA/SG
    ("Sri_Lanka", "Canada"),
    ("Canada", "Sri_Lanka"),
    ("Sri_Lanka", "Germany"),
    ("Germany", "Sri_Lanka"),
]

# Trim to exactly 50
P3_ROUTES_BATCH4 = P3_ROUTES_BATCH4[:50]


def main():
    generated = skipped = errors = 0
    print(f"Generating P3 Batch 4 routes... {len(P3_ROUTES_BATCH4)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH4:
        if origin_key not in COUNTRY_REGISTRY:
            print(f"  MISSING key: {origin_key}")
            errors += 1
            continue
        if dest_key not in COUNTRY_REGISTRY:
            print(f"  MISSING key: {dest_key}")
            errors += 1
            continue

        origin_slug = COUNTRY_REGISTRY[origin_key][2]
        dest_slug = COUNTRY_REGISTRY[dest_key][2]
        filename = f"{origin_slug}-to-{dest_slug}.md"
        filepath = os.path.join(CONTENT_DIR, filename)

        if os.path.exists(filepath):
            skipped += 1
            continue

        try:
            content = generate_route_markdown(origin_key, dest_key)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            generated += 1
            print(f"  + {filename}")
        except Exception as e:
            print(f"  ERROR {origin_key} -> {dest_key}: {e}")
            errors += 1

    print(f"\nRoutes generated: {generated} | skipped: {skipped} | errors: {errors}")


if __name__ == "__main__":
    main()
