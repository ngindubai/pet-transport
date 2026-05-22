"""
generate_p4_routes_auto.py — Task 4.3: Auto-generate all P4 route pages.

P4 adds 23 new countries to the registry (Spain + New Zealand were already in P1 list).
New P4 countries: Oman, Bahrain, Jordan, Finland, Hungary, Bulgaria, Croatia, Morocco,
  Pakistan, Bangladesh, Nepal, Cambodia, Myanmar, Peru, Ecuador, Costa Rica,
  Ghana, Tanzania, Ethiopia, Zimbabwe, Mauritius, Slovakia, Luxembourg

Generates all routes:
  - P4 origin -> all 75 countries (new routes only)
  - All 75 countries -> P4 destination (new routes only)
Skip-if-exists. Safe to run multiple times.
"""

import os
import sys

from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    ORIGIN_HUB_URLS,
    CONTENT_DIR,
    generate_route_markdown,
)

# ============================================================
# EXTEND registry with the 23 truly new P4 countries
# (Spain and New_Zealand are already in COUNTRY_REGISTRY from P1)
# ============================================================
P4_EXTENSIONS = {
    "Oman":       ("Oman",        "OM", "oman"),
    "Bahrain":    ("Bahrain",     "BH", "bahrain"),
    "Jordan":     ("Jordan",      "JO", "jordan"),
    "Finland":    ("Finland",     "FI", "finland"),
    "Hungary":    ("Hungary",     "HU", "hungary"),
    "Bulgaria":   ("Bulgaria",    "BG", "bulgaria"),
    "Croatia":    ("Croatia",     "HR", "croatia"),
    "Morocco":    ("Morocco",     "MA", "morocco"),
    "Pakistan":   ("Pakistan",    "PK", "pakistan"),
    "Bangladesh": ("Bangladesh",  "BD", "bangladesh"),
    "Nepal":      ("Nepal",       "NP", "nepal"),
    "Cambodia":   ("Cambodia",    "KH", "cambodia"),
    "Myanmar":    ("Myanmar",     "MM", "myanmar"),
    "Peru":       ("Peru",        "PE", "peru"),
    "Ecuador":    ("Ecuador",     "EC", "ecuador"),
    "Costa_Rica": ("Costa Rica",  "CR", "costa-rica"),
    "Ghana":      ("Ghana",       "GH", "ghana"),
    "Tanzania":   ("Tanzania",    "TZ", "tanzania"),
    "Ethiopia":   ("Ethiopia",    "ET", "ethiopia"),
    "Zimbabwe":   ("Zimbabwe",    "ZW", "zimbabwe"),
    "Mauritius":  ("Mauritius",   "MU", "mauritius"),
    "Slovakia":   ("Slovakia",    "SK", "slovakia"),
    "Luxembourg": ("Luxembourg",  "LU", "luxembourg"),
}

# Inject into the imported registry (modifying in-place is safe)
for k, v in P4_EXTENSIONS.items():
    if k not in COUNTRY_REGISTRY:
        COUNTRY_REGISTRY[k] = v

# Extend origin hub URLs for P4 (all use the -pet-export-guide suffix)
P4_HUB_URLS = {
    "oman":       "/pet-transport/origins/oman-pet-export-guide/",
    "bahrain":    "/pet-transport/origins/bahrain-pet-export-guide/",
    "jordan":     "/pet-transport/origins/jordan-pet-export-guide/",
    "finland":    "/pet-transport/origins/finland-pet-export-guide/",
    "hungary":    "/pet-transport/origins/hungary-pet-export-guide/",
    "bulgaria":   "/pet-transport/origins/bulgaria-pet-export-guide/",
    "croatia":    "/pet-transport/origins/croatia-pet-export-guide/",
    "morocco":    "/pet-transport/origins/morocco-pet-export-guide/",
    "pakistan":   "/pet-transport/origins/pakistan-pet-export-guide/",
    "bangladesh": "/pet-transport/origins/bangladesh-pet-export-guide/",
    "nepal":      "/pet-transport/origins/nepal-pet-export-guide/",
    "cambodia":   "/pet-transport/origins/cambodia-pet-export-guide/",
    "myanmar":    "/pet-transport/origins/myanmar-pet-export-guide/",
    "peru":       "/pet-transport/origins/peru-pet-export-guide/",
    "ecuador":    "/pet-transport/origins/ecuador-pet-export-guide/",
    "costa-rica": "/pet-transport/origins/costa-rica-pet-export-guide/",
    "ghana":      "/pet-transport/origins/ghana-pet-export-guide/",
    "tanzania":   "/pet-transport/origins/tanzania-pet-export-guide/",
    "ethiopia":   "/pet-transport/origins/ethiopia-pet-export-guide/",
    "zimbabwe":   "/pet-transport/origins/zimbabwe-pet-export-guide/",
    "mauritius":  "/pet-transport/origins/mauritius-pet-export-guide/",
    "slovakia":   "/pet-transport/origins/slovakia-pet-export-guide/",
    "luxembourg": "/pet-transport/origins/luxembourg-pet-export-guide/",
    # Update Spain and NZ to use the new P4-style hub URL
    "spain":        "/pet-transport/origins/spain-pet-export-guide/",
    "new-zealand":  "/pet-transport/origins/new-zealand-pet-export-guide/",
}

ORIGIN_HUB_URLS.update(P4_HUB_URLS)

# ============================================================
# ALL 75 COUNTRY KEYS (full registry after extension)
# ============================================================
ALL_KEYS = list(COUNTRY_REGISTRY.keys())

# P4 keys that drive route generation (all 25, including Spain + NZ)
P4_KEYS = list(P4_EXTENSIONS.keys()) + ["Spain", "New_Zealand"]


def build_pairs():
    """Return all unique (origin, dest) pairs involving at least one P4 country."""
    pairs = set()

    for p4_key in P4_KEYS:
        for other_key in ALL_KEYS:
            if p4_key == other_key:
                continue
            # P4 as origin
            pairs.add((p4_key, other_key))
            # P4 as destination
            pairs.add((other_key, p4_key))

    return list(pairs)


def main():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    pairs = build_pairs()
    print(f"Total unique route pairs involving P4 countries: {len(pairs)}")

    generated = 0
    skipped = 0
    errors = 0

    for origin_key, dest_key in sorted(pairs):
        if origin_key not in COUNTRY_REGISTRY:
            print(f"  SKIP (missing key): {origin_key}")
            errors += 1
            continue
        if dest_key not in COUNTRY_REGISTRY:
            print(f"  SKIP (missing key): {dest_key}")
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
            if generated % 50 == 0:
                print(f"  [{generated} generated] latest: {filename}")
        except Exception as exc:
            print(f"  ERROR {origin_key} -> {dest_key}: {exc}")
            errors += 1

    print(f"\nDone.")
    print(f"  Generated: {generated}")
    print(f"  Skipped (already exist): {skipped}")
    print(f"  Errors: {errors}")
    print(f"  Total route files now: {len(os.listdir(CONTENT_DIR))}")


if __name__ == "__main__":
    main()
