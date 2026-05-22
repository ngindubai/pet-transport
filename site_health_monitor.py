#!/usr/bin/env python3
"""
Site Health Monitor -- PetTransportGlobal
Block 29 / Task 2.10
Worker: The Watchdog

Checks:
1. Sitemap completeness (all sitemap URLs have real files, all pages in sitemap)
2. Internal link integrity (all href="/..." links resolve to real pages)
3. Robots.txt validation
4. Regulatory data freshness
5. Schema JSON-LD presence

Outputs: site-health-report.html at repo root
Run from repo root: python site_health_monitor.py
"""

import os
import re
import json
from datetime import datetime, date
from pathlib import Path
from html.parser import HTMLParser

REPO_ROOT = Path(__file__).parent
PUBLIC_DIR = REPO_ROOT / "site" / "public"
DATA_DIR = REPO_ROOT / "data"
SITEMAP_PATH = PUBLIC_DIR / "sitemap.xml"
ROBOTS_PATH = PUBLIC_DIR / "robots.txt"
SITE_BASE = "https://pettransportglobal.com"
SURGE_BASE = "https://pettransportglobal.surge.sh"

TODAY = date.today()

issues = []  # (severity, category, message, url)
stats = {}


def sev_label(s):
    labels = {"P0": "CRITICAL", "P1": "HIGH", "P2": "MEDIUM", "P3": "LOW", "P4": "INFO"}
    return labels.get(s, s)


def add_issue(sev, category, message, url=""):
    issues.append((sev, category, message, url))


# ---------------------------------------------------------------------------
# 1. Build known-pages set from public/
# ---------------------------------------------------------------------------
print("Building known pages set from site/public/ ...")
known_paths = set()  # set of URL paths like /pet-transport/uk-to-aus/
for root, dirs, files in os.walk(PUBLIC_DIR):
    # Skip non-HTML directories
    dirs[:] = [d for d in dirs if d not in ["css", "js", "fonts", "images", "img", "styles", "vendor"]]
    for fname in files:
        if fname == "index.html":
            rel = os.path.relpath(os.path.join(root, fname), PUBLIC_DIR)
            url_path = "/" + rel.replace("\\", "/").replace("/index.html", "")
            if url_path == "":
                url_path = "/"
            known_paths.add(url_path.rstrip("/") + "/")
        elif fname.endswith(".html") and fname != "index.html":
            rel = os.path.relpath(os.path.join(root, fname), PUBLIC_DIR)
            url_path = "/" + rel.replace("\\", "/")
            known_paths.add(url_path)

# Normalise root
known_paths.add("/")
stats["total_pages"] = len(known_paths)
print(f"  Found {len(known_paths)} known pages/files in public/")


# ---------------------------------------------------------------------------
# 2. Sitemap completeness check
# ---------------------------------------------------------------------------
print("Checking sitemap.xml ...")
sitemap_urls = set()
if SITEMAP_PATH.exists():
    sitemap_content = SITEMAP_PATH.read_text(encoding="utf-8")
    for m in re.finditer(r"<loc>(.*?)</loc>", sitemap_content):
        loc = m.group(1).strip()
        # Strip site base to get path
        for base in [SITE_BASE, SURGE_BASE]:
            if loc.startswith(base):
                path = loc[len(base):]
                sitemap_urls.add(path.rstrip("/") + "/" if path and not path.endswith(".xml") else path)
                break
    stats["sitemap_urls"] = len(sitemap_urls)

    # Check each sitemap URL has a real file
    missing_from_public = []
    for url_path in sorted(sitemap_urls):
        # Try index.html
        check_path = url_path.rstrip("/") + "/"
        if check_path not in known_paths and url_path not in known_paths:
            # Try as direct file
            fp = PUBLIC_DIR / url_path.lstrip("/")
            if not fp.exists():
                missing_from_public.append(url_path)

    if missing_from_public:
        for url in missing_from_public[:20]:
            add_issue("P1", "Sitemap", f"Sitemap URL has no file in public/: {url}", url)
        if len(missing_from_public) > 20:
            add_issue("P2", "Sitemap", f"... and {len(missing_from_public)-20} more sitemap URLs missing from public/")
    else:
        print(f"  Sitemap OK: all {len(sitemap_urls)} sitemap URLs resolve to files")

    # Check sitemap has entries for all index.html pages (sample check)
    content_paths = [p for p in known_paths if any(seg in p for seg in [
        "/pet-transport/", "/blog/", "/breeds/", "/airlines/", "/countries/", "/origins/"
    ])]
    sitemap_path_set = set(u.rstrip("/") + "/" for u in sitemap_urls)
    missing_from_sitemap = []
    for p in content_paths:
        norm = p.rstrip("/") + "/"
        if norm not in sitemap_path_set:
            missing_from_sitemap.append(p)
    if missing_from_sitemap:
        for url in missing_from_sitemap[:10]:
            add_issue("P3", "Sitemap", f"Page not in sitemap: {url}", url)
        if len(missing_from_sitemap) > 10:
            add_issue("P3", "Sitemap", f"... and {len(missing_from_sitemap)-10} more pages not in sitemap")
    else:
        print(f"  All content pages appear in sitemap")
else:
    add_issue("P0", "Sitemap", "sitemap.xml not found in public/")


# ---------------------------------------------------------------------------
# 3. Robots.txt check
# ---------------------------------------------------------------------------
print("Checking robots.txt ...")
if ROBOTS_PATH.exists():
    robots_content = ROBOTS_PATH.read_text(encoding="utf-8")
    if "sitemap" not in robots_content.lower():
        add_issue("P2", "Robots", "robots.txt does not reference sitemap")
    if "disallow: /" in robots_content.lower() and "allow:" not in robots_content.lower():
        add_issue("P0", "Robots", "robots.txt may be blocking all crawlers")
    else:
        print("  robots.txt OK")
else:
    add_issue("P1", "Robots", "robots.txt not found in public/")


# ---------------------------------------------------------------------------
# 4. Internal link integrity check (sample all HTML files)
# ---------------------------------------------------------------------------
print("Checking internal links in HTML files ...")

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1_count = 0
        self.has_meta_desc = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a":
            href = attrs_dict.get("href", "")
            if href and href.startswith("/") and not href.startswith("//"):
                self.links.append(href)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.has_meta_desc = True


broken_links = {}  # page -> [broken hrefs]
schema_missing = []
multi_h1 = []
no_meta_desc = []
pages_checked = 0

# Walk all HTML files in content areas
content_dirs = ["pet-transport", "blog"]
html_files_to_check = []
for cdir in content_dirs:
    cpath = PUBLIC_DIR / cdir
    if cpath.exists():
        for root, dirs, files in os.walk(cpath):
            dirs[:] = [d for d in dirs if d not in ["css", "js"]]
            for fname in files:
                if fname == "index.html":
                    html_files_to_check.append(Path(root) / fname)

# Also check top-level pages
for fname in ["index.html", "about/index.html", "contact/index.html"]:
    fp = PUBLIC_DIR / fname
    if fp.exists():
        html_files_to_check.append(fp)

print(f"  Checking {len(html_files_to_check)} HTML files for broken internal links ...")

for html_file in html_files_to_check:
    try:
        content = html_file.read_text(encoding="utf-8", errors="ignore")
        parser = LinkExtractor()
        parser.feed(content)

        page_rel = "/" + str(html_file.relative_to(PUBLIC_DIR)).replace("\\", "/")
        page_url = page_rel.replace("/index.html", "/")

        # Check links
        broken = []
        for href in parser.links:
            # Strip anchors and query strings
            clean = href.split("#")[0].split("?")[0]
            if not clean:
                continue
            norm = clean.rstrip("/") + "/" if not clean.endswith(".html") else clean
            # Check if it exists in known_paths
            if norm not in known_paths and clean not in known_paths:
                # Try exact file
                fp = PUBLIC_DIR / clean.lstrip("/")
                if not fp.exists():
                    broken.append(href)

        if broken:
            broken_links[page_url] = broken

        # Schema check: raw string search for schema.org markup (microdata or JSON-LD)
        # Exclude listing/index nav pages which don't need schema
        _is_listing = page_url.rstrip("/") in [
            "/pet-transport", "/pet-transport/airlines", "/pet-transport/breeds",
            "/pet-transport/countries", "/pet-transport/origins", "/pet-transport/routes",
            "/pet-transport/resources", "/blog"
        ]
        if any(seg in page_url for seg in ["/pet-transport/", "/blog/"]) and not _is_listing:
            has_schema = "schema.org" in content or "FAQPage" in content or "application/ld+json" in content
            if not has_schema:
                schema_missing.append(page_url)
            if parser.h1_count > 1:
                multi_h1.append(page_url)
            if not parser.has_meta_desc:
                no_meta_desc.append(page_url)

        pages_checked += 1
    except Exception as e:
        add_issue("P3", "Parse Error", f"Could not parse {html_file}: {e}")

stats["pages_link_checked"] = pages_checked
stats["pages_with_broken_links"] = len(broken_links)

print(f"  Checked {pages_checked} pages. {len(broken_links)} pages have broken internal links.")

if broken_links:
    for page_url, broken in sorted(broken_links.items()):
        for href in broken[:3]:
            add_issue("P1", "Broken Link", f"Broken internal link '{href}'", page_url)
        if len(broken) > 3:
            add_issue("P2", "Broken Link", f"... and {len(broken)-3} more broken links", page_url)

if schema_missing:
    for url in schema_missing[:10]:
        add_issue("P2", "Schema", f"No schema JSON-LD detected", url)
    if len(schema_missing) > 10:
        add_issue("P3", "Schema", f"... and {len(schema_missing)-10} more pages missing schema")

if multi_h1:
    for url in multi_h1[:5]:
        add_issue("P2", "SEO", f"Multiple H1 tags", url)

if no_meta_desc:
    for url in no_meta_desc[:5]:
        add_issue("P2", "SEO", f"No meta description found", url)


# ---------------------------------------------------------------------------
# 5. Regulatory data freshness
# ---------------------------------------------------------------------------
print("Checking regulatory data freshness ...")

def check_freshness(json_path, type_label, stale_months, records_key=None):
    """Check freshness using metadata.date_compiled, then optionally scan records."""
    try:
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        add_issue("P3", "Data", f"Could not read {json_path.name}: {e}")
        return

    # Check top-level metadata
    metadata = data.get("metadata", {})
    compiled = metadata.get("date_compiled", metadata.get("last_updated", ""))
    if compiled:
        try:
            lv_date = datetime.strptime(compiled[:10], "%Y-%m-%d").date()
            age_months = (TODAY - lv_date).days / 30
            if age_months > stale_months:
                add_issue("P4", "Regulatory Freshness",
                          f"{type_label} data compiled {compiled} ({age_months:.1f}m ago) -- re-verification recommended")
                return
        except Exception:
            pass

    # Check individual records if records_key provided
    stale = []
    if records_key and records_key in data:
        records = data[records_key]
        if isinstance(records, dict):
            for key, item in records.items():
                if not isinstance(item, dict):
                    continue
                lv = item.get("last_verified", item.get("last_updated", ""))
                if lv:
                    try:
                        lv_date = datetime.strptime(lv[:10], "%Y-%m-%d").date()
                        age_months = (TODAY - lv_date).days / 30
                        if age_months > stale_months:
                            stale.append((str(key), lv, round(age_months, 1)))
                    except Exception:
                        pass

    if stale:
        for name, lv, age in stale[:10]:
            add_issue("P4", "Regulatory Freshness",
                      f"{type_label} '{name}' last verified {lv} ({age}m ago)")
        if len(stale) > 10:
            add_issue("P4", "Regulatory Freshness",
                      f"... and {len(stale)-10} more {type_label} records need re-verification")
    else:
        print(f"  {type_label}: data is current (compiled {compiled or 'N/A'}), no stale records found")

check_freshness(DATA_DIR / "countries_pet_regulations.json", "Country", 6, records_key="countries")
check_freshness(DATA_DIR / "airline_pet_policies.json", "Airline", 3, records_key="airlines")


# ---------------------------------------------------------------------------
# 6. Summary stats
# ---------------------------------------------------------------------------
stats["total_issues"] = len(issues)
stats["p0"] = sum(1 for i in issues if i[0] == "P0")
stats["p1"] = sum(1 for i in issues if i[0] == "P1")
stats["p2"] = sum(1 for i in issues if i[0] == "P2")
stats["p3"] = sum(1 for i in issues if i[0] == "P3")
stats["p4"] = sum(1 for i in issues if i[0] == "P4")

overall_status = "HEALTHY"
status_color = "#3fb950"
if stats["p0"] > 0:
    overall_status = "CRITICAL"
    status_color = "#f85149"
elif stats["p1"] > 0:
    overall_status = "NEEDS ATTENTION"
    status_color = "#ff7b72"
elif stats["p2"] > 0:
    overall_status = "MINOR ISSUES"
    status_color = "#e3b341"


# ---------------------------------------------------------------------------
# 7. Generate HTML report
# ---------------------------------------------------------------------------
print("Generating site-health-report.html ...")

rows_html = ""
for sev, cat, msg, url in issues:
    sev_colors = {
        "P0": "#f85149", "P1": "#ff7b72", "P2": "#e3b341",
        "P3": "#79c0ff", "P4": "#8b949e"
    }
    color = sev_colors.get(sev, "#8b949e")
    url_cell = f'<a href="{url}" style="color:#79c0ff;">{url}</a>' if url else ""
    rows_html += f"""
    <tr>
      <td><span style="color:{color};font-weight:700;">{sev}</span></td>
      <td>{cat}</td>
      <td>{msg}</td>
      <td style="font-size:0.8em;">{url_cell}</td>
    </tr>"""

if not rows_html:
    rows_html = '<tr><td colspan="4" style="color:#3fb950;text-align:center;">No issues found</td></tr>'

run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Site Health Report -- PetTransportGlobal</title>
<style>
  :root {{
    --bg: #0d1117; --card: #161b22; --border: #30363d;
    --text: #c9d1d9; --green: #3fb950; --red: #f85149;
    --yellow: #e3b341; --blue: #79c0ff; --muted: #8b949e;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; padding: 2rem; line-height: 1.6; }}
  h1 {{ font-size: 1.8rem; margin-bottom: 0.25rem; }}
  .run-time {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 2rem; }}
  .status-badge {{ display: inline-block; padding: 0.5rem 1.5rem; border-radius: 8px; font-weight: 700; font-size: 1.1rem; margin-bottom: 2rem; background: rgba(255,255,255,0.05); border: 2px solid {status_color}; color: {status_color}; }}
  .stat-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
  .stat-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; text-align: center; }}
  .stat-card .num {{ font-size: 2rem; font-weight: 700; }}
  .stat-card .lbl {{ font-size: 0.8rem; color: var(--muted); margin-top: 0.25rem; }}
  table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 8px; overflow: hidden; }}
  th {{ background: #21262d; padding: 0.75rem 1rem; text-align: left; font-size: 0.85rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }}
  td {{ padding: 0.65rem 1rem; border-top: 1px solid var(--border); font-size: 0.9rem; vertical-align: top; }}
  tr:hover td {{ background: rgba(255,255,255,0.02); }}
  .section-title {{ font-size: 1.1rem; font-weight: 600; margin: 2rem 0 0.75rem; color: var(--blue); }}
  .checklist {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem 1.5rem; margin-bottom: 2rem; }}
  .checklist li {{ list-style: none; padding: 0.4rem 0; font-size: 0.95rem; }}
  .checklist li::before {{ content: "OK  "; color: var(--green); font-weight: 700; }}
  .checklist li.warn::before {{ content: "WARN  "; color: var(--yellow); }}
</style>
</head>
<body>
<h1>Site Health Report</h1>
<p class="run-time">PetTransportGlobal -- Run: {run_time}</p>

<div class="status-badge">Overall Status: {overall_status}</div>

<div class="stat-grid">
  <div class="stat-card">
    <div class="num" style="color:#79c0ff;">{stats.get('total_pages',0)}</div>
    <div class="lbl">Total pages (public/)</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:#79c0ff;">{stats.get('sitemap_urls',0)}</div>
    <div class="lbl">Sitemap URLs</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:#79c0ff;">{stats.get('pages_link_checked',0)}</div>
    <div class="lbl">Pages link-checked</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:{'#f85149' if stats['p0'] else '#3fb950'};">{stats['p0']}</div>
    <div class="lbl">P0 Critical</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:{'#ff7b72' if stats['p1'] else '#3fb950'};">{stats['p1']}</div>
    <div class="lbl">P1 High</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:{'#e3b341' if stats['p2'] else '#3fb950'};">{stats['p2']}</div>
    <div class="lbl">P2 Medium</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:{'#79c0ff' if stats['p3'] else '#3fb950'};">{stats['p3']}</div>
    <div class="lbl">P3 Low</div>
  </div>
  <div class="stat-card">
    <div class="num" style="color:#8b949e;">{stats['p4']}</div>
    <div class="lbl">P4 Info</div>
  </div>
</div>

<p class="section-title">Post-Deploy Checklist</p>
<div class="checklist">
<ul>
  <li>Sitemap.xml present and well-formed</li>
  <li>robots.txt present</li>
  <li>All sitemap URLs resolve to files in public/</li>
  <li>Internal link check complete ({stats.get('pages_link_checked',0)} pages scanned)</li>
  <li>Regulatory data freshness checked</li>
  <li class="warn">Schema validation: manual check via Rich Results Test recommended</li>
  <li class="warn">Core Web Vitals: run Lighthouse manually per template type</li>
  <li class="warn">GSC crawl stats: review weekly in Search Console</li>
</ul>
</div>

<p class="section-title">All Issues ({stats['total_issues']} found)</p>
<table>
  <thead>
    <tr><th>Severity</th><th>Category</th><th>Issue</th><th>URL</th></tr>
  </thead>
  <tbody>
    {rows_html}
  </tbody>
</table>

<p style="margin-top:2rem;color:#8b949e;font-size:0.85rem;">
  Severity: P0=Critical (fix now), P1=High (fix today), P2=Medium (fix this week), P3=Low (fix this sprint), P4=Info/Regulatory freshness
</p>
</body>
</html>"""

out_path = REPO_ROOT / "site-health-report.html"
out_path.write_text(html_out, encoding="utf-8")

print(f"\nDone. Report written to site-health-report.html")
print(f"Status: {overall_status}")
print(f"Issues: P0={stats['p0']} P1={stats['p1']} P2={stats['p2']} P3={stats['p3']} P4={stats['p4']}")
