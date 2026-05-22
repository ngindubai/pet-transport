"""
P3 Route Pages — Batch 7 (~55 pairs)
Covers: South Korea x P1/P3, Thailand x EU/AU, Malaysia x EU/AU,
        Philippines x AU/UK/DE, Brazil x US/UK/DE/CA, Mexico x UK/AU/DE,
        Indonesia x AU/UK/DE, Taiwan x AU/CA, Vietnam x AU/UK returns
Imports shared logic from generate_p3_routes_batch1.py
"""
import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

P3_ROUTES_BATCH7 = [
    # South Korea x P1
    ("South Korea", "Australia"),
    ("Australia", "South Korea"),
    ("South Korea", "USA"),
    ("USA", "South Korea"),
    ("South Korea", "UK"),
    ("UK", "South Korea"),
    ("South Korea", "Canada"),
    ("Canada", "South Korea"),
    ("South Korea", "Germany"),
    ("Germany", "South Korea"),
    ("South Korea", "France"),
    ("South Korea", "Singapore"),
    # Thailand x EU/AU
    ("Thailand", "Australia"),
    ("Australia", "Thailand"),
    ("Thailand", "Germany"),
    ("Germany", "Thailand"),
    ("Thailand", "France"),
    ("France", "Thailand"),
    ("Thailand", "Netherlands"),
    ("Thailand", "Canada"),
    ("Canada", "Thailand"),
    # Malaysia x EU/AU
    ("Malaysia", "Australia"),
    ("Australia", "Malaysia"),
    ("Malaysia", "Germany"),
    ("Germany", "Malaysia"),
    ("Malaysia", "UK"),
    ("UK", "Malaysia"),
    ("Malaysia", "Canada"),
    ("Canada", "Malaysia"),
    # Philippines x AU/UK/DE
    ("Philippines", "Australia"),
    ("Australia", "Philippines"),
    ("Philippines", "UK"),
    ("UK", "Philippines"),
    ("Philippines", "Germany"),
    ("Germany", "Philippines"),
    ("Philippines", "Canada"),
    ("Canada", "Philippines"),
    # Brazil x US/UK/DE/CA
    ("Brazil", "USA"),
    ("USA", "Brazil"),
    ("Brazil", "UK"),
    ("UK", "Brazil"),
    ("Brazil", "Germany"),
    ("Germany", "Brazil"),
    ("Brazil", "Canada"),
    ("Canada", "Brazil"),
    # Mexico x UK/AU/DE
    ("Mexico", "UK"),
    ("UK", "Mexico"),
    ("Mexico", "Australia"),
    ("Australia", "Mexico"),
    ("Mexico", "Germany"),
    ("Germany", "Mexico"),
    # Indonesia x AU/UK/DE
    ("Indonesia", "Australia"),
    ("Australia", "Indonesia"),
    ("Indonesia", "UK"),
    ("UK", "Indonesia"),
    ("Indonesia", "Germany"),
    ("Germany", "Indonesia"),
    # Taiwan x AU/CA
    ("Taiwan", "Australia"),
    ("Australia", "Taiwan"),
    ("Taiwan", "Canada"),
    ("Canada", "Taiwan"),
    # Vietnam x AU/UK
    ("Vietnam", "UK"),
    ("UK", "Vietnam"),
]


def main():
    generated = skipped = errors = 0
    print(f"Generating P3 Batch 7 routes... {len(P3_ROUTES_BATCH7)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH7:
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
