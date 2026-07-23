#!/usr/bin/env python3
"""
rebuild_link_graph_v3.py — Full internal link graph rebuild.

Run automatically by build-to-live.yml BEFORE hugo build.

Actions:
  1. Scan site/content/routes/ to build a complete route index
     (covers ALL origins/destinations — no hardcoded registry required)
  2. Update every origin hub with a 'Popular routes from X' section
     listing all outbound routes as hyperlinks (idempotent — replaces)
  3. Inject / replace routes_incoming YAML in every country guide
     (enables the route-card grid in countries/single.html)

Safe to re-run: replaces existing sections, never duplicates.
"""

import os
import re
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths — relative to repo root (script lives at repo root)
# ---------------------------------------------------------------------------
REPO_ROOT   = os.path.dirname(os.path.abspath(__file__))
ROUTES_DIR  = os.path.join(REPO_ROOT, "site", "content", "routes")
ORIGINS_DIR = os.path.join(REPO_ROOT, "site", "content", "origins")
COUNTRIES_DIR = os.path.join(REPO_ROOT, "site", "content", "countries")

# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------
SLUG_NAME_OVERRIDES = {
    "united-kingdom":      "United Kingdom",
    "united-states":       "United States",
    "united-arab-emirates":"United Arab Emirates",
    "new-zealand":         "New Zealand",
    "south-africa":        "South Africa",
    "south-korea":         "South Korea",
    "hong-kong":           "Hong Kong",
    "saudi-arabia":        "Saudi Arabia",
    "costa-rica":          "Costa Rica",
    "sri-lanka":           "Sri Lanka",
    "czech-republic":      "Czech Republic",
    "dominican-republic":  "Dominican Republic",
    "ivory-coast":         "Ivory Coast",
    "trinidad-and-tobago": "Trinidad and Tobago",
    "republic-of-ireland": "Republic of Ireland",
}

ISO_MAP = {
    "argentina":"AR","armenia":"AM","australia":"AU","austria":"AT","azerbaijan":"AZ",
    "bahrain":"BH","bangladesh":"BD","belgium":"BE","brazil":"BR","bulgaria":"BG",
    "cambodia":"KH","canada":"CA","chile":"CL","china":"CN","colombia":"CO",
    "costa-rica":"CR","croatia":"HR","cyprus":"CY","czech-republic":"CZ","denmark":"DK",
    "dominican-republic":"DO","ecuador":"EC","egypt":"EG","estonia":"EE","ethiopia":"ET",
    "finland":"FI","france":"FR","georgia":"GE","germany":"DE","ghana":"GH",
    "greece":"GR","hong-kong":"HK","hungary":"HU","india":"IN","indonesia":"ID",
    "ireland":"IE","israel":"IL","italy":"IT","jamaica":"JM","japan":"JP",
    "jordan":"JO","kazakhstan":"KZ","kenya":"KE","kuwait":"KW","latvia":"LV",
    "lebanon":"LB","lithuania":"LT","luxembourg":"LU","malaysia":"MY","malta":"MT",
    "mauritius":"MU","mexico":"MX","morocco":"MA","myanmar":"MM","nepal":"NP",
    "netherlands":"NL","new-zealand":"NZ","nigeria":"NG","norway":"NO","oman":"OM",
    "pakistan":"PK","panama":"PA","peru":"PE","philippines":"PH","poland":"PL",
    "portugal":"PT","qatar":"QA","romania":"RO","rwanda":"RW","saudi-arabia":"SA",
    "singapore":"SG","slovakia":"SK","slovenia":"SI","south-africa":"ZA","south-korea":"KR",
    "spain":"ES","sri-lanka":"LK","sweden":"SE","switzerland":"CH","taiwan":"TW",
    "tanzania":"TZ","thailand":"TH","turkey":"TR","uganda":"UG","united-arab-emirates":"AE",
    "united-kingdom":"GB","united-states":"US","uruguay":"UY","vietnam":"VN","zimbabwe":"ZW",
    "ivory-coast":"CI","trinidad-and-tobago":"TT","republic-of-ireland":"IE",
}


def slug_to_name(slug):
    if slug in SLUG_NAME_OVERRIDES:
        return SLUG_NAME_OVERRIDES[slug]
    return " ".join(w.capitalize() for w in slug.split("-"))


def slug_to_iso(slug):
    return ISO_MAP.get(slug, "??")


# ---------------------------------------------------------------------------
# Step 1 — Build route index from routes/ directory
# ---------------------------------------------------------------------------

def build_route_index():
    """Scan all route .md files; return (by_origin, by_dest) dicts."""
    by_origin = defaultdict(list)
    by_dest   = defaultdict(list)

    if not os.path.isdir(ROUTES_DIR):
        print(f"  WARNING: routes dir not found: {ROUTES_DIR}")
        return by_origin, by_dest

    for filename in sorted(os.listdir(ROUTES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        slug = filename[:-3]
        if "-to-" not in slug:
            continue

        idx = slug.find("-to-")
        orig = slug[:idx]
        dest = slug[idx + 4:]

        orig_name = slug_to_name(orig)
        dest_name = slug_to_name(dest)

        info = {
            "slug":      slug,
            "url":       f"/pet-transport/{slug}/",
            "orig":      orig,
            "dest":      dest,
            "orig_name": orig_name,
            "dest_name": dest_name,
            "orig_iso":  slug_to_iso(orig),
            "dest_iso":  slug_to_iso(dest),
        }
        by_origin[orig].append(info)
        by_dest[dest].append(info)

    return by_origin, by_dest


# ---------------------------------------------------------------------------
# Step 2 — Update origin hub files
# ---------------------------------------------------------------------------

def build_popular_routes_section(orig_name, routes):
    """Return the YAML/markdown section text for Popular routes."""
    link_lines = "\n".join(
        f"      - [{r['orig_name']} to {r['dest_name']}]({r['url']})"
        for r in sorted(routes, key=lambda r: r["dest_name"])
    )
    return (
        f'  - heading: "Popular routes from {orig_name}"\n'
        f'    body: |\n'
        f'      We have detailed guides for the following routes:\n'
        f'\n'
        f'{link_lines}'
    )


def update_origin_hub(filepath, orig_name, routes):
    """Insert or replace the Popular routes section in an origin hub."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    new_section = build_popular_routes_section(orig_name, routes)

    # Pattern: match existing Popular routes section (to the end of its body block)
    # The body block ends just before the next `  - heading:` or `\nfaqs:` or `\n---`
    existing_pattern = re.compile(
        r'  - heading: "Popular routes from [^"]+"\n'
        r'    body: \|.*?'
        r'(?=\n  - heading:|\nfaqs:|\nairlines:|\noutbound_routes:|\n---)',
        re.DOTALL,
    )

    if existing_pattern.search(content):
        new_content = existing_pattern.sub(new_section, content, count=1)
        status = "replaced"
    else:
        # No existing section — insert before faqs: / airlines: / closing ---
        for anchor in ("\nfaqs:", "\nairlines:", "\noutbound_routes:"):
            pos = content.find(anchor)
            if pos >= 0:
                # Make sure there's a sections: list to append to
                if "sections:" not in content:
                    new_content = (
                        content[:pos]
                        + "\nsections:\n"
                        + new_section
                        + content[pos:]
                    )
                else:
                    new_content = content[:pos] + "\n" + new_section + content[pos:]
                status = "added"
                break
        else:
            # Fallback: insert before closing ---
            last_delim = content.rfind("\n---")
            if last_delim == -1:
                return "no-anchor"
            if "sections:" not in content:
                new_content = (
                    content[:last_delim]
                    + "\nsections:\n"
                    + new_section
                    + content[last_delim:]
                )
            else:
                new_content = content[:last_delim] + "\n" + new_section + content[last_delim:]
            status = "added"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return status


def process_origin_hubs(by_origin):
    """Update all origin hub files in site/content/origins/."""
    results = defaultdict(int)

    if not os.path.isdir(ORIGINS_DIR):
        print(f"  WARNING: origins dir not found: {ORIGINS_DIR}")
        return results

    for filename in sorted(os.listdir(ORIGINS_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue

        # Determine the origin slug from the filename
        if filename.endswith("-pet-export-guide.md"):
            orig_slug = filename.replace("-pet-export-guide.md", "")
        else:
            orig_slug = filename[:-3]

        routes = by_origin.get(orig_slug)
        if not routes:
            results["no-routes"] += 1
            continue

        filepath = os.path.join(ORIGINS_DIR, filename)
        orig_name = slug_to_name(orig_slug)
        status = update_origin_hub(filepath, orig_name, routes)
        results[status] += 1
        print(f"  [{status:8s}] {filename} ({len(routes)} routes)")

    return results


# ---------------------------------------------------------------------------
# Step 3 — Update country guide files (routes_incoming)
# ---------------------------------------------------------------------------

def build_routes_incoming_yaml(routes):
    """Return the routes_incoming YAML block."""
    lines = ["routes_incoming:"]
    for r in sorted(routes, key=lambda r: r["orig_name"]):
        lines.append(f'  - slug: "{r["url"]}"')
        lines.append(f'    origin: "{r["orig_name"]}"')
        lines.append(f'    destination: "{r["dest_name"]}"')
        lines.append(f'    origin_code: "{r["orig_iso"]}"')
        lines.append(f'    destination_code: "{r["dest_iso"]}"')
        lines.append(f'    complexity: "medium"')
    return "\n".join(lines) + "\n"


def update_country_guide(filepath, routes):
    """Inject or replace routes_incoming YAML in a country guide."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    new_block = build_routes_incoming_yaml(routes)

    if "routes_incoming:" in content:
        # Replace the existing block.
        # BUG FIX: must stop at \n--- (closing frontmatter delimiter) as well as
        # at the next top-level YAML key. Previously \Z consumed the closing ---
        # which caused Hugo to error with "EOF looking for end YAML front matter delimiter".
        pattern = re.compile(
            r'^routes_incoming:.*?(?=^[a-z_]+:|\n---|\Z)',
            re.MULTILINE | re.DOTALL,
        )
        if pattern.search(content):
            new_content = pattern.sub(new_block, content, count=1)
            status = "replaced"
        else:
            return "pattern-not-matched"
    else:
        # Insert before closing --- of front matter
        if not content.startswith("---"):
            return "no-front-matter"
        end = content.find("\n---", 3)
        if end == -1:
            return "no-front-matter-end"
        new_content = content[:end] + "\n" + new_block + content[end:]
        status = "added"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return status


def process_country_guides(by_dest):
    """Update all country guide files in site/content/countries/."""
    results = defaultdict(int)

    if not os.path.isdir(COUNTRIES_DIR):
        print(f"  WARNING: countries dir not found: {COUNTRIES_DIR}")
        return results

    for filename in sorted(os.listdir(COUNTRIES_DIR)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue

        dest_slug = filename[:-3]
        routes = by_dest.get(dest_slug)
        if not routes:
            results["no-routes"] += 1
            continue

        filepath = os.path.join(COUNTRIES_DIR, filename)
        status = update_country_guide(filepath, routes)
        results[status] += 1
        print(f"  [{status:8s}] {filename} ({len(routes)} inbound routes)")

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    sep = "=" * 65
    print(sep)
    print("rebuild_link_graph_v3.py — Internal link graph rebuild")
    print(sep)

    print("\n[1/3] Scanning route files...")
    by_origin, by_dest = build_route_index()
    total_routes = sum(len(v) for v in by_origin.values())
    print(f"      {total_routes} routes | {len(by_origin)} origins | {len(by_dest)} destinations")

    print("\n[2/3] Updating origin hub files...")
    hub_results = process_origin_hubs(by_origin)
    print(f"\n      Summary: {dict(hub_results)}")

    print("\n[3/3] Updating country guide files (routes_incoming)...")
    country_results = process_country_guides(by_dest)
    print(f"\n      Summary: {dict(country_results)}")

    total_links = (
        hub_results.get("replaced", 0) + hub_results.get("added", 0)
        + country_results.get("replaced", 0) + country_results.get("added", 0)
    )
    print(f"\n{sep}")
    print(f"Done. {total_links} files updated. Hugo build will now have a complete")
    print(f"internal link graph covering all {total_routes} route pages.")
    print(sep)


if __name__ == "__main__":
    main()
