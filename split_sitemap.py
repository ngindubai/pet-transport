"""
split_sitemap.py — post-build sitemap restructuring for PetTransportGlobal.

Run after: hugo --gc --minify (from site/)

Reads site/public/sitemap.xml (Hugo's flat output) and produces:
  site/public/sitemap.xml           → sitemap index (replaces flat file)
  site/public/sitemap-routes.xml    → 2,300+ route pages (priority 0.8)
  site/public/sitemap-hubs.xml      → countries/origins/airlines/breeds (priority 0.7)
  site/public/sitemap-blog.xml      → blog articles (priority 0.6)
  site/public/sitemap-pages.xml     → home, about, contact, privacy, resources (various)

Also updates robots.txt Sitemap directive if needed.
"""

import os
import xml.etree.ElementTree as ET

PUBLIC_DIR = os.path.join("site", "public")
SITEMAP_IN = os.path.join(PUBLIC_DIR, "sitemap.xml")
ROBOTS_TXT = os.path.join(PUBLIC_DIR, "robots.txt")
BASE_URL = "https://pettransportglobal.com"

# Namespace
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)

# Sections and their output files
SECTIONS = {
    "routes": {
        "file": "sitemap-routes.xml",
        "default_priority": "0.8",
        "changefreq": "monthly",
    },
    "hubs": {
        "file": "sitemap-hubs.xml",
        "default_priority": "0.7",
        "changefreq": "monthly",
    },
    "blog": {
        "file": "sitemap-blog.xml",
        "default_priority": "0.6",
        "changefreq": "weekly",
    },
    "pages": {
        "file": "sitemap-pages.xml",
        "default_priority": "0.5",
        "changefreq": "monthly",
    },
}


def classify_url(url: str) -> tuple[str, str]:
    """Return (section_key, priority) for a given URL."""
    path = url.replace(BASE_URL, "").strip("/")
    parts = path.split("/")
    top = parts[0] if parts else ""
    sub = parts[1] if len(parts) > 1 else ""

    # Home page
    if path == "":
        return "pages", "1.0"

    # Static pages
    if top in ("about", "contact", "privacy", "terms", "search"):
        return "pages", "0.5"

    # Blog listing + articles
    if top == "blog":
        if sub == "" or path == "blog":
            return "pages", "0.6"   # blog index
        return "blog", "0.6"

    # Pet-transport sub-sections
    if top == "pet-transport":
        if path in ("pet-transport", "pet-transport/routes", "pet-transport/how-we-source-route-data"):
            return "pages", "0.6"
        if sub in ("countries", "origins", "airlines", "breeds"):
            return "hubs", "0.7"
        if sub == "resources":
            return "pages", "0.6"
        # Everything else under /pet-transport/ is a route
        return "routes", "0.8"

    # Fallback
    return "pages", "0.5"


def parse_input_sitemap():
    """Parse Hugo's generated sitemap.xml and return list of url dicts."""
    tree = ET.parse(SITEMAP_IN)
    root = tree.getroot()
    ns = {"sm": NS}

    entries = []
    for url_el in root.findall("sm:url", ns):
        loc = url_el.findtext("sm:loc", namespaces=ns) or ""
        lastmod = url_el.findtext("sm:lastmod", namespaces=ns) or ""
        entries.append({"loc": loc, "lastmod": lastmod})
    return entries


def build_section_xml(entries: list[dict], section_key: str) -> str:
    """Build a <urlset> XML string for the given section entries."""
    cfg = SECTIONS[section_key]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in entries:
        loc = entry["loc"]
        lastmod = entry["lastmod"][:10] if entry["lastmod"] else ""
        _, priority = classify_url(loc)
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{cfg['changefreq']}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines)


def build_index_xml(section_files: list[tuple[str, int, str]]) -> str:
    """
    Build a sitemap index XML string.
    section_files: list of (filename, url_count, lastmod_date)
    """
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for fname, count, lastmod in section_files:
        lines.append("  <sitemap>")
        lines.append(f"    <loc>{BASE_URL}/{fname}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </sitemap>")
    lines.append("</sitemapindex>")
    return "\n".join(lines)


def main():
    print("Reading Hugo sitemap...")
    entries = parse_input_sitemap()
    print(f"  {len(entries)} URLs found")

    # Classify all entries into sections
    sections_data: dict[str, list[dict]] = {k: [] for k in SECTIONS}
    unknown = []
    for entry in entries:
        section_key, _ = classify_url(entry["loc"])
        if section_key in sections_data:
            sections_data[section_key].append(entry)
        else:
            unknown.append(entry)

    # Report distribution
    for key, items in sections_data.items():
        print(f"  {key:12s}: {len(items)} URLs → {SECTIONS[key]['file']}")
    if unknown:
        print(f"  UNKNOWN    : {len(unknown)} URLs (will go to pages)")
        sections_data["pages"].extend(unknown)

    # Write section sitemaps
    index_entries = []
    for section_key, items in sections_data.items():
        if not items:
            continue
        xml_str = build_section_xml(items, section_key)
        fname = SECTIONS[section_key]["file"]
        outpath = os.path.join(PUBLIC_DIR, fname)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(xml_str)

        # Determine most recent lastmod for index
        dates = [e["lastmod"][:10] for e in items if e.get("lastmod")]
        latest = max(dates) if dates else ""
        index_entries.append((fname, len(items), latest))
        print(f"  Written: {fname} ({len(items)} URLs)")

    # Write sitemap index (replaces sitemap.xml)
    # Sort: routes first (most important for crawl budget)
    priority_order = {"sitemap-routes.xml": 0, "sitemap-hubs.xml": 1,
                      "sitemap-blog.xml": 2, "sitemap-pages.xml": 3}
    index_entries.sort(key=lambda x: priority_order.get(x[0], 9))

    index_xml = build_index_xml(index_entries)
    with open(SITEMAP_IN, "w", encoding="utf-8") as f:
        f.write(index_xml)
    print(f"\nWritten sitemap index → sitemap.xml")

    # Update robots.txt if needed
    if os.path.exists(ROBOTS_TXT):
        txt = open(ROBOTS_TXT, encoding="utf-8").read()
        if "sitemap.xml" in txt.lower():
            # Already points to sitemap.xml — index is now at same location, OK
            print("robots.txt already references sitemap.xml (now the index) — no change needed")
        else:
            with open(ROBOTS_TXT, "a", encoding="utf-8") as f:
                f.write(f"\nSitemap: {BASE_URL}/sitemap.xml\n")
            print("robots.txt updated with Sitemap directive")

    print(f"\nDone. Sitemap index + {len(index_entries)} section sitemaps written to {PUBLIC_DIR}/")
    print("\nSubmit these to Google Search Console:")
    print(f"  {BASE_URL}/sitemap.xml  (index)")
    for fname, count, _ in index_entries:
        print(f"  {BASE_URL}/{fname}  ({count} URLs)")


if __name__ == "__main__":
    main()
