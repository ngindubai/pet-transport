#!/usr/bin/env python3
"""
rebuild_p4_link_graph.py — Task 4.5: P4 link graph refresh

Targets only P4 content:
  1. P4 origin hubs (files ending in -pet-export-guide.md): inject
     "Popular routes from X" section listing all outbound routes.
  2. P4 country guides (files without routes_incoming yet): inject
     routes_incoming YAML block listing all inbound routes.

Skips files already containing the relevant section so re-runs are safe.
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")
ORIGINS_DIR = os.path.join(REPO_ROOT, "site", "content", "origins")
COUNTRIES_DIR = os.path.join(REPO_ROOT, "site", "content", "countries")


def slug_to_name(slug):
    """Convert a hyphenated slug to a human-readable country name."""
    overrides = {
        "uae": "United Arab Emirates",
        "usa": "United States",
        "uk": "United Kingdom",
    }
    if slug in overrides:
        return overrides[slug]
    return " ".join(w.capitalize() for w in slug.split("-"))


def slug_to_iso(slug):
    """Approximate ISO-3166 alpha-2 from slug."""
    iso_map = {
        "australia": "AU", "austria": "AT", "bahrain": "BH", "bangladesh": "BD",
        "belgium": "BE", "brazil": "BR", "bulgaria": "BG", "cambodia": "KH",
        "canada": "CA", "chile": "CL", "china": "CN", "colombia": "CO",
        "costa-rica": "CR", "croatia": "HR", "cyprus": "CY", "czech-republic": "CZ",
        "denmark": "DK", "ecuador": "EC", "egypt": "EG", "ethiopia": "ET",
        "finland": "FI", "france": "FR", "germany": "DE", "ghana": "GH",
        "greece": "GR", "hong-kong": "HK", "hungary": "HU", "india": "IN",
        "indonesia": "ID", "ireland": "IE", "israel": "IL", "italy": "IT",
        "japan": "JP", "jordan": "JO", "kenya": "KE", "kuwait": "KW",
        "luxembourg": "LU", "malaysia": "MY", "malta": "MT", "mauritius": "MU",
        "mexico": "MX", "morocco": "MA", "myanmar": "MM", "nepal": "NP",
        "netherlands": "NL", "new-zealand": "NZ", "nigeria": "NG", "norway": "NO",
        "oman": "OM", "pakistan": "PK", "peru": "PE", "philippines": "PH",
        "poland": "PL", "portugal": "PT", "qatar": "QA", "romania": "RO",
        "saudi-arabia": "SA", "singapore": "SG", "slovakia": "SK",
        "south-africa": "ZA", "south-korea": "KR", "spain": "ES", "sri-lanka": "LK",
        "sweden": "SE", "switzerland": "CH", "taiwan": "TW", "tanzania": "TZ",
        "thailand": "TH", "turkey": "TR", "united-arab-emirates": "AE",
        "united-kingdom": "GB", "united-states": "US", "vietnam": "VN", "zimbabwe": "ZW",
        "argentina": "AR",
    }
    return iso_map.get(slug, "??")


def build_route_index():
    """Scan routes/. Return (by_origin, by_dest) dicts of route info."""
    by_origin, by_dest = {}, {}
    for filename in sorted(os.listdir(ROUTES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        slug = filename[:-3]
        if "-to-" not in slug:
            continue
        # Find the FIRST -to- (some country slugs contain hyphens but never -to-)
        idx = slug.find("-to-")
        origin_slug = slug[:idx]
        dest_slug = slug[idx + 4:]

        info = {
            "url": f"/pet-transport/{slug}/",
            "origin_slug": origin_slug,
            "dest_slug": dest_slug,
            "origin_name": slug_to_name(origin_slug),
            "dest_name": slug_to_name(dest_slug),
            "origin_iso": slug_to_iso(origin_slug),
            "dest_iso": slug_to_iso(dest_slug),
        }
        by_origin.setdefault(origin_slug, []).append(info)
        by_dest.setdefault(dest_slug, []).append(info)
    return by_origin, by_dest


def update_p4_origin_hub(filepath, origin_slug, routes):
    """Inject Popular routes section into a P4 origin hub if missing."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if "Popular routes from" in content:
        return "already-present"

    country_name = slug_to_name(origin_slug)
    link_lines = "\n".join(
        f"      - [{r['origin_name']} to {r['dest_name']}]({r['url']})"
        for r in routes
    )
    section = (
        f'  - heading: "Popular routes from {country_name}"\n'
        f'    body: |\n'
        f'      We have detailed guides for the following routes:\n'
        f'      \n{link_lines}'
    )

    # Find sections: list — append the new entry to it
    sections_match = re.search(r'\nsections:\s*\n', content)
    faqs_pos = content.find("\nfaqs:")

    if sections_match:
        # Append to end of sections list (just before \nfaqs: or closing ---)
        if faqs_pos > sections_match.end():
            insert_pos = faqs_pos
        else:
            last_delim = content.rfind("\n---")
            if last_delim == -1:
                return "no-anchor"
            insert_pos = last_delim
        new_content = content[:insert_pos] + "\n" + section + content[insert_pos:]
    else:
        # No sections list — insert one before faqs or before closing ---
        block = "\nsections:\n" + section + "\n"
        if faqs_pos >= 0:
            insert_pos = faqs_pos
        else:
            last_delim = content.rfind("\n---")
            if last_delim == -1:
                return "no-anchor"
            insert_pos = last_delim
        new_content = content[:insert_pos] + block + content[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return "added"


def update_p4_country_guide(filepath, dest_slug, routes):
    """Inject routes_incoming YAML block into a P4 country guide if missing."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if "routes_incoming:" in content:
        return "already-present"

    lines = ["routes_incoming:"]
    for r in routes:
        lines.append(f'  - slug: "{r["url"]}"')
        lines.append(f'    origin: "{r["origin_name"]}"')
        lines.append(f'    destination: "{r["dest_name"]}"')
        lines.append(f'    origin_code: "{r["origin_iso"]}"')
        lines.append(f'    destination_code: "{r["dest_iso"]}"')
        lines.append(f'    complexity: "medium"')
    block = "\n".join(lines) + "\n"

    # Insert before closing --- of front matter
    if not content.startswith("---"):
        return "no-front-matter"
    end = content.find("\n---", 3)
    if end == -1:
        return "no-front-matter-end"
    new_content = content[:end] + "\n" + block + content[end:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return "added"


def main():
    print("Building route index...")
    by_origin, by_dest = build_route_index()
    print(f"  origins indexed: {len(by_origin)}, destinations indexed: {len(by_dest)}")

    # P4 origin hubs: files ending in -pet-export-guide.md
    print("\nUpdating P4 origin hubs...")
    hub_added = hub_skipped = hub_no_routes = 0
    for filename in sorted(os.listdir(ORIGINS_DIR)):
        if not filename.endswith("-pet-export-guide.md"):
            continue
        origin_slug = filename.replace("-pet-export-guide.md", "")
        filepath = os.path.join(ORIGINS_DIR, filename)
        routes = by_origin.get(origin_slug, [])
        if not routes:
            print(f"  ! {filename}: no routes found for slug '{origin_slug}'")
            hub_no_routes += 1
            continue
        result = update_p4_origin_hub(filepath, origin_slug, routes)
        if result == "added":
            hub_added += 1
        else:
            hub_skipped += 1
    print(f"  hubs: added={hub_added}, skipped={hub_skipped}, no-routes={hub_no_routes}")

    # P4 country guides: files without existing routes_incoming
    print("\nUpdating country guides missing routes_incoming...")
    cg_added = cg_skipped = cg_no_routes = 0
    for filename in sorted(os.listdir(COUNTRIES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        country_slug = filename[:-3]
        filepath = os.path.join(COUNTRIES_DIR, filename)
        routes = by_dest.get(country_slug, [])
        if not routes:
            cg_no_routes += 1
            continue
        result = update_p4_country_guide(filepath, country_slug, routes)
        if result == "added":
            cg_added += 1
            print(f"  + {filename}: {len(routes)} inbound routes")
        else:
            cg_skipped += 1
    print(f"  countries: added={cg_added}, skipped={cg_skipped}, no-routes={cg_no_routes}")


if __name__ == "__main__":
    main()
