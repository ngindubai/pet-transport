"""
Auto-generate all missing P3-origin route pages.
Iterates every P3 country x all 50 registry countries, skips existing files.
Run repeatedly — safe, idempotent, skip-if-exists.
Imports shared logic from generate_p3_routes_batch1.py
"""
import os
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    CONTENT_DIR,
    generate_route_markdown,
)

# All P3 country registry keys (origin side)
P3_KEYS = [
    "Ireland", "Norway", "Sweden", "Austria", "Belgium", "Poland",
    "Turkey", "Israel", "Saudi_Arabia", "Qatar", "Kuwait",
    "China", "Taiwan", "Vietnam", "Sri_Lanka",
    "Argentina", "Chile", "Colombia",
    "Egypt", "Kenya", "Nigeria",
    "Czech_Republic", "Romania", "Malta", "Cyprus",
]

# All destination keys (full registry)
ALL_KEYS = list(COUNTRY_REGISTRY.keys())

# Slug -> registry key map for reverse lookup
SLUG_TO_KEY = {v[2]: k for k, v in COUNTRY_REGISTRY.items()}


def main():
    generated = skipped = errors = 0
    pairs_to_run = []

    # Build full list: P3 origin x all destinations (both directions)
    for origin_key in P3_KEYS:
        for dest_key in ALL_KEYS:
            if origin_key == dest_key:
                continue
            pairs_to_run.append((origin_key, dest_key))
        # Also reverse: all origins -> P3 destination
        for origin_key2 in ALL_KEYS:
            if origin_key2 == origin_key:
                continue
            pairs_to_run.append((origin_key2, origin_key))

    # Deduplicate while preserving order
    seen = set()
    unique_pairs = []
    for pair in pairs_to_run:
        if pair not in seen:
            seen.add(pair)
            unique_pairs.append(pair)

    print(f"Total unique route pairs to check: {len(unique_pairs)}")

    for origin_key, dest_key in unique_pairs:
        if origin_key not in COUNTRY_REGISTRY:
            errors += 1
            continue
        if dest_key not in COUNTRY_REGISTRY:
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
            if generated % 10 == 0:
                print(f"  [{generated} generated] {filename}")
        except Exception as e:
            print(f"  ERROR {origin_key} -> {dest_key}: {e}")
            errors += 1

    print(f"\nDone. Generated: {generated} | Skipped (exist): {skipped} | Errors: {errors}")
    print(f"Total route files now: {len(os.listdir(CONTENT_DIR))}")


if __name__ == "__main__":
    main()
