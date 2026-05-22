"""
P3 Route Pages — Batch 6 (55 pairs)
High-value corridors: Gulf x India/Philippines (expat routes), China x SE Asia,
Ireland/Nordic x P2, Turkey/Africa x India, LatAm internal, Saudi/Qatar x EU
Imports shared logic from generate_p3_routes_batch1.py
"""
import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

P3_ROUTES_BATCH6 = [
    # Gulf x India (massive expat corridor)
    ("Saudi_Arabia", "India"),
    ("India", "Saudi_Arabia"),
    ("Qatar", "India"),
    ("India", "Qatar"),
    ("Kuwait", "India"),
    ("India", "Kuwait"),
    # Gulf x Philippines (large Filipino expat population)
    ("Saudi_Arabia", "Philippines"),
    ("Philippines", "Saudi_Arabia"),
    ("Qatar", "Philippines"),
    ("Philippines", "Qatar"),
    ("Kuwait", "Philippines"),
    ("Philippines", "Kuwait"),
    # China x SE Asia
    ("China", "Thailand"),
    ("Thailand", "China"),
    ("China", "Malaysia"),
    ("Malaysia", "China"),
    ("China", "Indonesia"),
    ("Indonesia", "China"),
    ("China", "Philippines"),
    ("Philippines", "China"),
    ("China", "India"),
    ("India", "China"),
    # Ireland x P2
    ("Ireland", "Japan"),
    ("Japan", "Ireland"),
    ("Ireland", "India"),
    ("India", "Ireland"),
    ("Ireland", "South Korea"),
    ("Ireland", "Denmark"),
    ("Denmark", "Ireland"),
    # Nordic x P2
    ("Norway", "Japan"),
    ("Japan", "Norway"),
    ("Sweden", "Japan"),
    ("Japan", "Sweden"),
    ("Norway", "India"),
    ("India", "Norway"),
    ("Sweden", "India"),
    ("India", "Sweden"),
    ("Norway", "Denmark"),
    ("Denmark", "Norway"),
    ("Sweden", "Denmark"),
    ("Denmark", "Sweden"),
    # Turkey x India
    ("Turkey", "India"),
    ("India", "Turkey"),
    # Africa x India
    ("Kenya", "India"),
    ("India", "Kenya"),
    ("Egypt", "India"),
    ("India", "Egypt"),
    ("Nigeria", "India"),
    ("India", "Nigeria"),
    # LatAm internal
    ("Argentina", "Brazil"),
    ("Brazil", "Argentina"),
    ("Colombia", "Brazil"),
    ("Brazil", "Colombia"),
    # Saudi/Qatar x France/NL
    ("Saudi_Arabia", "France"),
    ("France", "Saudi_Arabia"),
    ("Qatar", "Netherlands"),
    ("Netherlands", "Qatar"),
]


def main():
    generated = skipped = errors = 0
    print(f"Generating P3 Batch 6 routes... {len(P3_ROUTES_BATCH6)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH6:
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
