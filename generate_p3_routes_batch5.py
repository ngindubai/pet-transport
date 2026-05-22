"""
P3 Route Pages — Batch 5 (55 pairs, ~50 new)
Covers: UK return legs for P3 countries, Austria/Belgium/Poland x P1/P2,
        Turkey x FR/NL/CA/SG, Malta/Cyprus x AU/US/DE, Israel expansion,
        Kuwait expansion, Nordic x CA, Ireland return legs from EU
Imports shared logic from generate_p3_routes_batch1.py
"""
import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

P3_ROUTES_BATCH5 = [
    # UK return legs (batch 1 had P3→UK; these are UK→P3)
    ("UK", "Norway"),
    ("UK", "Sweden"),
    ("UK", "Austria"),
    ("UK", "Belgium"),
    ("UK", "Poland"),
    ("UK", "Czech_Republic"),
    ("UK", "Romania"),
    # Austria x P1/P2
    ("Austria", "Australia"),
    ("Australia", "Austria"),
    ("Austria", "USA"),
    ("USA", "Austria"),
    ("Austria", "Singapore"),
    ("Singapore", "Austria"),
    ("Austria", "France"),
    ("France", "Austria"),
    # Belgium x P1
    ("Belgium", "Australia"),
    ("Australia", "Belgium"),
    ("Belgium", "USA"),
    ("USA", "Belgium"),
    ("Belgium", "Singapore"),
    ("Singapore", "Belgium"),
    # Poland x P1/P2
    ("Poland", "Australia"),
    ("Australia", "Poland"),
    ("Poland", "USA"),
    ("USA", "Poland"),
    ("Poland", "France"),
    ("France", "Poland"),
    # Turkey x more destinations
    ("Turkey", "France"),
    ("France", "Turkey"),
    ("Turkey", "Netherlands"),
    ("Netherlands", "Turkey"),
    ("Turkey", "Canada"),
    ("Canada", "Turkey"),
    ("Turkey", "Singapore"),
    # Malta x P1
    ("Malta", "Australia"),
    ("Australia", "Malta"),
    ("Malta", "USA"),
    ("USA", "Malta"),
    ("Malta", "Germany"),
    # Cyprus x P1
    ("Cyprus", "Australia"),
    ("Australia", "Cyprus"),
    ("Cyprus", "USA"),
    ("USA", "Cyprus"),
    ("Cyprus", "Germany"),
    # Israel expansion
    ("Israel", "France"),
    ("France", "Israel"),
    ("Israel", "Singapore"),
    # Kuwait expansion
    ("Kuwait", "Australia"),
    ("Kuwait", "Singapore"),
    ("Singapore", "Kuwait"),
    # Nordic x Canada
    ("Norway", "Canada"),
    ("Canada", "Norway"),
    ("Sweden", "Canada"),
    ("Canada", "Sweden"),
    # Ireland return legs from EU
    ("Germany", "Ireland"),
    ("France", "Ireland"),
    ("Spain", "Ireland"),
]


def main():
    generated = skipped = errors = 0
    print(f"Generating P3 Batch 5 routes... {len(P3_ROUTES_BATCH5)} route pairs to process")

    for origin_key, dest_key in P3_ROUTES_BATCH5:
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
