#!/usr/bin/env python3
"""
rebuild_link_graph.py — Block 25: Internal link graph rebuild

Actions:
  1. Scan all route files to build origin + destination indexes
  2. Update ALL origin hub "Popular routes" sections with full route lists
     (adds section if missing, for Canada/Germany-style P1 hubs)
  3. Inject routes_incoming YAML into all 25 country guides
     (enables the route-card grid in the countries/single.html template)
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")
ORIGINS_DIR = os.path.join(REPO_ROOT, "site", "content", "origins")
COUNTRIES_DIR = os.path.join(REPO_ROOT, "site", "content", "countries")

# Complete country registry: slug → (display_name, ISO_code)
COUNTRY_REGISTRY = {
    "australia":            ("Australia",              "AU"),
    "canada":               ("Canada",                 "CA"),
    "france":               ("France",                 "FR"),
    "germany":              ("Germany",                "DE"),
    "hong-kong":            ("Hong Kong",              "HK"),
    "new-zealand":          ("New Zealand",            "NZ"),
    "singapore":            ("Singapore",              "SG"),
    "south-africa":         ("South Africa",           "ZA"),
    "spain":                ("Spain",                  "ES"),
    "united-arab-emirates": ("United Arab Emirates",   "AE"),
    "united-kingdom":       ("United Kingdom",         "GB"),
    "united-states":        ("United States",          "US"),
    "brazil":               ("Brazil",                 "BR"),
    "denmark":              ("Denmark",                "DK"),
    "greece":               ("Greece",                 "GR"),
    "india":                ("India",                  "IN"),
    "indonesia":            ("Indonesia",              "ID"),
    "italy":                ("Italy",                  "IT"),
    "japan":                ("Japan",                  "JP"),
    "malaysia":             ("Malaysia",               "MY"),
    "mexico":               ("Mexico",                 "MX"),
    "netherlands":          ("Netherlands",            "NL"),
    "philippines":          ("Philippines",            "PH"),
    "portugal":             ("Portugal",               "PT"),
    "south-korea":          ("South Korea",            "KR"),
    "switzerland":          ("Switzerland",            "CH"),
    "thailand":             ("Thailand",               "TH"),
}

# P1 origin slugs — these get special "Popular routes" section treatment
P1_ORIGINS = {
    "australia", "canada", "france", "germany", "hong-kong",
    "new-zealand", "singapore", "south-africa", "spain",
    "united-arab-emirates", "united-kingdom", "united-states",
}


# ---------------------------------------------------------------------------
# Step 1 — Build route index
# ---------------------------------------------------------------------------

def build_route_index():
    """Scan all route .md files; return (by_origin, by_dest) dicts."""
    by_origin = {}  # origin_slug → [route_info, ...]
    by_dest   = {}  # dest_slug   → [route_info, ...]

    for filename in sorted(os.listdir(ROUTES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue

        slug = filename.replace(".md", "")
        if "-to-" not in slug:
            continue

        parts = slug.split("-to-", 1)
        if len(parts) != 2:
            continue

        origin_slug, dest_slug = parts

        if origin_slug not in COUNTRY_REGISTRY or dest_slug not in COUNTRY_REGISTRY:
            continue

        origin_name, origin_code = COUNTRY_REGISTRY[origin_slug]
        dest_name,   dest_code   = COUNTRY_REGISTRY[dest_slug]

        # Extract complexity from front matter
        filepath = os.path.join(ROUTES_DIR, filename)
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
        m = re.search(r'route_complexity:\s*["\']?(\w+)["\']?', content)
        complexity = m.group(1) if m else "medium"

        route_info = {
            "slug":             f"/pet-transport/{slug}/",
            "origin":           origin_name,
            "destination":      dest_name,
            "origin_code":      origin_code,
            "destination_code": dest_code,
            "origin_slug":      origin_slug,
            "dest_slug":        dest_slug,
            "complexity":       complexity,
        }

        by_origin.setdefault(origin_slug, []).append(route_info)
        by_dest.setdefault(dest_slug,   []).append(route_info)

    return by_origin, by_dest


# ---------------------------------------------------------------------------
# Step 2 — Origin hubs: Popular routes sections
# ---------------------------------------------------------------------------

def build_popular_routes_section_text(country_name, routes):
    """Return the full YAML text for a 'Popular routes from X' section entry."""
    link_lines = "\n".join(
        f"      - [{r['origin']} to {r['destination']}]({r['slug']})"
        for r in routes
    )
    body = f"      We have detailed guides for the following routes:\n      \n{link_lines}"
    return f'  - heading: "Popular routes from {country_name}"\n    body: |\n{body}'


def update_origin_hub(filepath, country_name, routes):
    """Update or add the Popular routes section in an origin hub file."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    new_section = build_popular_routes_section_text(country_name, routes)

    if "Popular routes from" in content:
        # --- Replace existing Popular routes section body ---
        # The section ends just before \nfaqs: or \n--- or the next \n  - heading:
        pattern = re.compile(
            r'  - heading: "Popular routes from [^"]+"\n    body: \|.*?(?=\nfaqs:|\n  - heading:|\n---)',
            re.DOTALL,
        )
        if pattern.search(content):
            new_content = pattern.sub(new_section, content)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return "replaced"
        else:
            return "pattern-not-matched"

    else:
        # --- Add new Popular routes section before faqs: ---
        faqs_pos = content.find("\nfaqs:")
        if faqs_pos >= 0:
            insert_pos = faqs_pos  # insert just before \nfaqs:
            new_content = (
                content[:insert_pos]
                + "\n"
                + new_section
                + content[insert_pos:]
            )
        else:
            # Fallback: insert before the closing ---
            last_delim = content.rfind("\n---")
            if last_delim == -1:
                return "no-anchor-found"
            new_content = (
                content[:last_delim]
                + "\n"
                + new_section
                + content[last_delim:]
            )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return "added"


# ---------------------------------------------------------------------------
# Step 3 — Country guides: inject routes_incoming
# ---------------------------------------------------------------------------

def build_routes_incoming_yaml(routes):
    """Return YAML block string for routes_incoming front matter field."""
    lines = ["routes_incoming:"]
    for r in routes:
        lines.append(f'  - slug: "{r["slug"]}"')
        lines.append(f'    origin: "{r["origin"]}"')
        lines.append(f'    destination: "{r["destination"]}"')
        lines.append(f'    origin_code: "{r["origin_code"]}"')
        lines.append(f'    destination_code: "{r["destination_code"]}"')
        lines.append(f'    complexity: "{r["complexity"]}"')
    return "\n".join(lines) + "\n"


def update_country_guide(filepath, routes):
    """Inject routes_incoming YAML block into a country guide file."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if "routes_incoming:" in content:
        return "already-exists"

    yaml_block = build_routes_incoming_yaml(routes)

    # Insert just before the closing --- of the YAML front matter
    last_delim = content.rfind("\n---")
    if last_delim == -1:
        return "no-closing-delimiter"

    new_content = content[:last_delim] + "\n" + yaml_block + content[last_delim:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return "ok"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Block 25 — Internal link graph rebuild")
    print("=" * 60)

    # Build index
    print("\nScanning route files...")
    by_origin, by_dest = build_route_index()
    total = sum(len(v) for v in by_origin.values())
    print(f"  {total} routes indexed across {len(by_origin)} origin countries")

    # --- Update ALL origin hubs ---
    print("\n--- Updating origin hubs (Popular routes sections) ---")
    hub_results = {"replaced": 0, "added": 0, "no-routes": 0, "missing-file": 0, "error": 0}

    for slug in sorted(COUNTRY_REGISTRY.keys()):
        filepath = os.path.join(ORIGINS_DIR, f"{slug}.md")
        if not os.path.exists(filepath):
            print(f"  MISSING FILE: {slug}.md")
            hub_results["missing-file"] += 1
            continue

        routes = by_origin.get(slug, [])
        if not routes:
            print(f"  SKIP (no outbound routes): {slug}")
            hub_results["no-routes"] += 1
            continue

        country_name = COUNTRY_REGISTRY[slug][0]
        result = update_origin_hub(filepath, country_name, routes)
        status_emoji = "OK" if result in ("replaced", "added") else "WARN"
        print(f"  [{status_emoji}] {slug} ({len(routes)} routes): {result}")
        hub_results[result] = hub_results.get(result, 0) + 1

    print(f"\n  Summary: {hub_results}")

    # --- Update country guides ---
    print("\n--- Updating country guides (routes_incoming) ---")
    country_results = {"ok": 0, "already-exists": 0, "no-routes": 0, "missing-file": 0, "error": 0}

    for slug in sorted(COUNTRY_REGISTRY.keys()):
        filepath = os.path.join(COUNTRIES_DIR, f"{slug}.md")
        if not os.path.exists(filepath):
            print(f"  MISSING FILE: {slug}.md")
            country_results["missing-file"] += 1
            continue

        routes = by_dest.get(slug, [])
        if not routes:
            print(f"  SKIP (no inbound routes): {slug}")
            country_results["no-routes"] += 1
            continue

        result = update_country_guide(filepath, routes)
        status_emoji = "OK" if result in ("ok", "already-exists") else "WARN"
        print(f"  [{status_emoji}] {slug} ({len(routes)} inbound routes): {result}")
        country_results[result] = country_results.get(result, 0) + 1

    print(f"\n  Summary: {country_results}")

    print("\n" + "=" * 60)
    print("Done. Run hugo --gc --minify from site/ to verify the build.")
    print("=" * 60)


if __name__ == "__main__":
    main()
