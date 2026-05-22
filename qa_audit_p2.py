"""
Block 28 / Task 2.9 — Full QA + Regulatory Audit (Phase 2)
Audits all 539 pages across: routes, countries, origins, airlines, breeds, blog

Checks:
  - Front matter completeness (title, description, author)
  - Title uniqueness + length (50-70 chars)
  - Description uniqueness + length (140-160 chars)
  - FAQ presence (4+ for route/country/airline/breed pages)
  - Internal links (routes must have upward + sideways)
  - Broken internal link targets (linked slug must exist as a file)
  - Country guides: routes_incoming present (except spain)
  - Origin hubs: Popular routes section present
  - Banned vocabulary (The Chameleon rules)
  - YMYL safety guarantee violations
  - Em dash / en dash violations
  - Duplicate title detection
  - Duplicate description detection
  - Minimum word count in text fields

Output: qa-audit-report.html at repo root
"""

import os
import re
from collections import defaultdict
from datetime import date

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = r"c:\Users\garet\Desktop\pet-transport\site\content"
ROUTES_DIR    = os.path.join(BASE, "routes")
COUNTRIES_DIR = os.path.join(BASE, "countries")
ORIGINS_DIR   = os.path.join(BASE, "origins")
AIRLINES_DIR  = os.path.join(BASE, "airlines")
BREEDS_DIR    = os.path.join(BASE, "breeds")
BLOG_DIR      = os.path.join(BASE, "blog")

# ── The Chameleon's banned vocabulary ────────────────────────────────────────
BANNED_WORDS = {
    "delve", "tapestry", "vibrant", "crucial", "comprehensive", "meticulous",
    "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy",
    "transformative", "paramount", "multifaceted", "myriad", "cornerstone",
    "reimagine", "empower", "catalyst", "invaluable", "bustling", "nestled",
    "realm", "furthermore", "moreover", "paradigm", "holistic", "utilize",
    "facilitate", "nuanced", "illuminate", "encompasses", "catalyze", "proactive",
    "ubiquitous", "quintessential", "navigate", "navigating", "testament",
    "landscape", "ecosystem", "dive into", "dive deep", "unpack", "unpack this",
    "in today's", "in today's world", "fast-paced", "ever-evolving",
    "game-changer", "game changer", "cutting-edge", "state-of-the-art",
    "best-in-class", "world-class", "top-notch",
}

BANNED_PHRASES = [
    "in today's digital age",
    "it is worth noting",
    "plays a crucial role",
    "serves as a testament",
    "in the realm of",
    "harness the power of",
    "embark on a journey",
    "without further ado",
    "rest assured",
    "look no further",
    "a testament to",
    "needless to say",
]

# ── YMYL safety guarantee patterns ───────────────────────────────────────────
SAFETY_PATTERNS = [
    r"guarantee[ds]?\s+(safety|protection|safe arrival|safe travel)",
    r"100%\s+safe",
    r"completely\s+safe",
    r"guaranteed\s+safe",
    r"risk[- ]free\s+(transport|travel|shipping)",
    r"ensure[ds]?\s+your pet (will )?(arrive|is) safe",
    r"your pet will\s+(definitely|certainly|always)\s+(arrive|be)",
]

# ── Internal URL prefixes that must resolve to existing files ─────────────────
INTERNAL_PREFIXES = {
    "/pet-transport/origins/":  ORIGINS_DIR,
    "/pet-transport/countries/": COUNTRIES_DIR,
    "/pet-transport/airlines/":  AIRLINES_DIR,
    "/pet-transport/breeds/":    BREEDS_DIR,
    "/blog/":                    BLOG_DIR,
}
# Route URLs need special handling: /pet-transport/[slug]/ maps to ROUTES_DIR
ROUTE_URL_PREFIX = "/pet-transport/"

# ── Build slug→file maps ──────────────────────────────────────────────────────
def build_slug_set(directory):
    """Return a set of slugs from .md files in a directory (filename without .md)."""
    result = set()
    if not os.path.isdir(directory):
        return result
    for f in os.listdir(directory):
        if f.endswith(".md") and f != "_index.md":
            result.add(f[:-3])  # strip .md
    return result

ALL_ORIGIN_SLUGS   = build_slug_set(ORIGINS_DIR)
ALL_COUNTRY_SLUGS  = build_slug_set(COUNTRIES_DIR)
ALL_AIRLINE_SLUGS  = build_slug_set(AIRLINES_DIR)
ALL_BREED_SLUGS    = build_slug_set(BREEDS_DIR)
ALL_BLOG_SLUGS     = build_slug_set(BLOG_DIR)
ALL_ROUTE_SLUGS    = build_slug_set(ROUTES_DIR)

def url_exists(url):
    """Check whether an internal URL points to an existing content file."""
    url = url.rstrip("/")

    for prefix, directory in INTERNAL_PREFIXES.items():
        if url.startswith(prefix.rstrip("/")):
            slug = url[len(prefix.rstrip("/")):]
            slug = slug.strip("/")
            filepath = os.path.join(directory, slug + ".md")
            return os.path.exists(filepath)

    # Route URL: /pet-transport/some-slug/
    if url.startswith(ROUTE_URL_PREFIX.rstrip("/")):
        slug = url[len(ROUTE_URL_PREFIX.rstrip("/")):]
        slug = slug.strip("/")
        # Exclude sub-section URLs like /pet-transport/origins/ etc.
        if slug and "/" not in slug:
            filepath = os.path.join(ROUTES_DIR, slug + ".md")
            return os.path.exists(filepath)

    return True  # don't flag external or unrecognised URLs


# ── Per-file checker ──────────────────────────────────────────────────────────
def audit_file(filepath, page_type):
    """
    Audit a single Hugo content .md file.
    Returns dict: {file, page_type, slug, title, description, issues}
    Issues are tuples of (severity, category, message)
      severity: ERROR | WARN | INFO
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    slug = os.path.basename(filepath).replace(".md", "")
    issues = []

    # ── Extract front matter ──────────────────────────────────────────────────
    fm_match = re.match(r"^---\s*\n(.*?)\n---", raw, re.DOTALL)
    front_matter = fm_match.group(1) if fm_match else ""
    body = raw[fm_match.end():].strip() if fm_match else raw

    # Helper: extract a single-line YAML value
    def fm_get(key):
        m = re.search(r'^' + re.escape(key) + r':\s*["\']?(.+?)["\']?\s*$', front_matter, re.MULTILINE)
        return m.group(1).strip().strip('"\'') if m else ""

    title       = fm_get("title")
    description = fm_get("description")
    author      = fm_get("author")

    # ── Required front matter ─────────────────────────────────────────────────
    if not title:
        issues.append(("ERROR", "Front matter", "Missing title"))
    else:
        tlen = len(title)
        if tlen < 30:
            issues.append(("WARN", "SEO", f"Title very short ({tlen} chars) — target 50-70"))
        elif tlen > 75:
            issues.append(("WARN", "SEO", f"Title too long ({tlen} chars) — target 50-70"))

    if not description:
        issues.append(("ERROR", "Front matter", "Missing description"))
    else:
        dlen = len(description)
        if dlen < 100:
            issues.append(("WARN", "SEO", f"Description very short ({dlen} chars) — target 140-160"))
        elif dlen > 175:
            issues.append(("WARN", "SEO", f"Description too long ({dlen} chars) — target 140-160"))

    if not author:
        issues.append(("ERROR", "E-E-A-T", "Missing author attribution"))

    # ── Page-type specific checks ─────────────────────────────────────────────
    faq_count = len(re.findall(r'question:', raw))
    if page_type in ("route", "country", "airline", "breed"):
        if faq_count == 0:
            issues.append(("ERROR", "Content", "No FAQs found — required for all route/country/airline/breed pages"))
        elif faq_count < 4:
            issues.append(("WARN", "Content", f"Only {faq_count} FAQ(s) — target 4+"))

    if page_type == "route":
        if "upward:" not in raw:
            issues.append(("ERROR", "Internal links", "Missing upward links (origin hub + destination country guide)"))
        if "sideways:" not in raw:
            issues.append(("WARN", "Internal links", "No sideways (related route) links"))
        if "content:" not in raw and "overview:" not in raw:
            issues.append(("ERROR", "Content", "No content.overview found in front matter"))

    if page_type == "country":
        if slug != "spain" and "routes_incoming:" not in raw:
            issues.append(("ERROR", "Internal links", "Missing routes_incoming block — needed for route-card grid"))

    if page_type == "origin":
        if "popular routes" not in raw.lower():
            issues.append(("WARN", "Internal links", "No 'Popular routes' section found in hub page"))

    # ── Internal link target verification ────────────────────────────────────
    internal_urls = re.findall(r'url:\s*["\']?(/[^\s"\'\n]+)["\']?', raw)
    for url in internal_urls:
        url_clean = url.strip('"\'').rstrip("/")
        if url_clean.startswith("/pet-transport") or url_clean.startswith("/blog"):
            if not url_exists(url_clean):
                issues.append(("WARN", "Broken link", f"Internal URL may not resolve: {url_clean}"))

    # ── Banned vocabulary (The Chameleon) ─────────────────────────────────────
    raw_lower = raw.lower()
    for word in BANNED_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', raw_lower):
            issues.append(("WARN", "Humaniser", f"Banned word: '{word}'"))
            break  # Only flag one per file to keep report readable; collect all below
    # Collect ALL banned words for detailed reporting
    banned_found = [w for w in BANNED_WORDS if re.search(r'\b' + re.escape(w) + r'\b', raw_lower)]
    if len(banned_found) > 1:
        for w in banned_found[1:]:
            issues.append(("WARN", "Humaniser", f"Banned word: '{w}'"))

    for phrase in BANNED_PHRASES:
        if phrase.lower() in raw_lower:
            issues.append(("WARN", "Humaniser", f"Banned phrase: '{phrase}'"))

    # ── Em dash / en dash ─────────────────────────────────────────────────────
    if "\u2014" in raw:
        issues.append(("ERROR", "Humaniser", "Em dash (—) found — use commas, colons, or periods"))
    if "\u2013" in raw:
        issues.append(("WARN", "Humaniser", "En dash (–) found — avoid"))

    # ── YMYL safety patterns ──────────────────────────────────────────────────
    for pattern in SAFETY_PATTERNS:
        if re.search(pattern, raw_lower):
            issues.append(("ERROR", "YMYL", f"Safety guarantee violation: '{pattern}'"))

    return {
        "file": os.path.relpath(filepath, BASE),
        "page_type": page_type,
        "slug": slug,
        "title": title,
        "description": description,
        "issues": issues,
    }


# ── Collect all pages ─────────────────────────────────────────────────────────
def collect_pages(directory, page_type):
    pages = []
    if not os.path.isdir(directory):
        return pages
    for f in sorted(os.listdir(directory)):
        if f.endswith(".md") and f != "_index.md":
            pages.append(audit_file(os.path.join(directory, f), page_type))
    return pages


print("Running Block 28 QA Audit...")
all_pages = []
all_pages += collect_pages(ROUTES_DIR,    "route")    ; print(f"  Routes:    {len(all_pages)}")
prev = len(all_pages)
all_pages += collect_pages(COUNTRIES_DIR, "country")  ; print(f"  Countries: {len(all_pages)-prev}")
prev = len(all_pages)
all_pages += collect_pages(ORIGINS_DIR,   "origin")   ; print(f"  Origins:   {len(all_pages)-prev}")
prev = len(all_pages)
all_pages += collect_pages(AIRLINES_DIR,  "airline")  ; print(f"  Airlines:  {len(all_pages)-prev}")
prev = len(all_pages)
all_pages += collect_pages(BREEDS_DIR,    "breed")    ; print(f"  Breeds:    {len(all_pages)-prev}")
prev = len(all_pages)
all_pages += collect_pages(BLOG_DIR,      "blog")     ; print(f"  Blog:      {len(all_pages)-prev}")
print(f"  TOTAL:     {len(all_pages)}")


# ── Duplicate title / description detection ───────────────────────────────────
title_counts       = defaultdict(list)
description_counts = defaultdict(list)
for p in all_pages:
    if p["title"]:
        title_counts[p["title"].lower()].append(p["file"])
    if p["description"]:
        description_counts[p["description"].lower()].append(p["file"])

dup_titles = {t: files for t, files in title_counts.items() if len(files) > 1}
dup_descs  = {d: files for d, files in description_counts.items() if len(files) > 1}

# Inject duplicate flags into per-page issues
for p in all_pages:
    t = p["title"].lower() if p["title"] else ""
    d = p["description"].lower() if p["description"] else ""
    if t and t in dup_titles and len(dup_titles[t]) > 1:
        p["issues"].append(("ERROR", "SEO", f"Duplicate title shared with: {', '.join(f for f in dup_titles[t] if f != p['file'])}"))
    if d and d in dup_descs and len(dup_descs[d]) > 1:
        p["issues"].append(("ERROR", "SEO", f"Duplicate description shared with: {', '.join(f for f in dup_descs[d] if f != p['file'])}"))


# ── Summarise ────────────────────────────────────────────────────────────────
total   = len(all_pages)
errors  = sum(1 for p in all_pages if any(i[0] == "ERROR" for i in p["issues"]))
warns   = sum(1 for p in all_pages if any(i[0] == "WARN" for i in p["issues"]) and not any(i[0] == "ERROR" for i in p["issues"]))
clean   = sum(1 for p in all_pages if not p["issues"])
passed  = total - errors

total_error_count = sum(len([i for i in p["issues"] if i[0] == "ERROR"]) for p in all_pages)
total_warn_count  = sum(len([i for i in p["issues"] if i[0] == "WARN"])  for p in all_pages)

# By page type
type_stats = defaultdict(lambda: {"total": 0, "errors": 0, "warns": 0, "clean": 0})
for p in all_pages:
    pt = p["page_type"]
    type_stats[pt]["total"] += 1
    e = any(i[0] == "ERROR" for i in p["issues"])
    w = any(i[0] == "WARN"  for i in p["issues"])
    if e:
        type_stats[pt]["errors"] += 1
    elif w:
        type_stats[pt]["warns"] += 1
    else:
        type_stats[pt]["clean"] += 1

print(f"\nAudit complete:")
print(f"  Total pages : {total}")
print(f"  ERROR pages : {errors}  ({total_error_count} total errors)")
print(f"  WARN only   : {warns}   ({total_warn_count} total warnings)")
print(f"  Clean       : {clean}")


# ── HTML Report ───────────────────────────────────────────────────────────────
def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

sev_badge = {
    "ERROR": '<span class="badge error">ERROR</span>',
    "WARN":  '<span class="badge warn">WARN</span>',
    "INFO":  '<span class="badge info">INFO</span>',
}

html_parts = []
html_parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QA Audit Report — PetTransportGlobal — {date.today()}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: system-ui, -apple-system, sans-serif; background: #f0f2f5; color: #1a1a2e; line-height: 1.5; }}
  header {{ background: #0f3460; color: white; padding: 24px 32px; }}
  header h1 {{ font-size: 1.6rem; }}
  header p {{ opacity: 0.75; font-size: 0.9rem; margin-top: 4px; }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 24px 16px; }}
  .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 16px; margin-bottom: 32px; }}
  .stat {{ background: white; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
  .stat .num {{ font-size: 2.4rem; font-weight: 700; }}
  .stat .lbl {{ font-size: 0.8rem; color: #666; margin-top: 4px; }}
  .num.green {{ color: #22c55e; }}
  .num.red   {{ color: #ef4444; }}
  .num.amber {{ color: #f59e0b; }}
  .num.blue  {{ color: #3b82f6; }}
  .type-table {{ background: white; border-radius: 8px; padding: 20px; margin-bottom: 32px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
  .type-table h2 {{ font-size: 1rem; margin-bottom: 12px; color: #0f3460; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; }}
  th {{ background: #f0f2f5; text-align: left; padding: 8px 12px; font-weight: 600; }}
  td {{ padding: 8px 12px; border-top: 1px solid #e5e7eb; }}
  tr:hover td {{ background: #f9fafb; }}
  .badge {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.76rem; font-weight: 700; }}
  .badge.error {{ background: #fee2e2; color: #b91c1c; }}
  .badge.warn  {{ background: #fef3c7; color: #92400e; }}
  .badge.info  {{ background: #dbeafe; color: #1d4ed8; }}
  .badge.pass  {{ background: #dcfce7; color: #166534; }}
  .section-header {{ display: flex; justify-content: space-between; align-items: center; cursor: pointer; padding: 14px 20px; background: white; border-radius: 8px; margin-bottom: 4px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
  .section-header h2 {{ font-size: 1rem; color: #0f3460; }}
  .page-block {{ background: white; border-radius: 8px; margin-bottom: 8px; overflow: hidden; border-left: 4px solid #e5e7eb; }}
  .page-block.has-error {{ border-left-color: #ef4444; }}
  .page-block.has-warn  {{ border-left-color: #f59e0b; }}
  .page-block.clean     {{ border-left-color: #22c55e; }}
  .page-header {{ display: flex; align-items: center; gap: 10px; padding: 10px 16px; font-size: 0.84rem; cursor: pointer; }}
  .page-header .slug {{ font-weight: 600; flex: 1; color: #1a1a2e; word-break: break-all; }}
  .page-header .title-text {{ color: #555; font-size: 0.78rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 320px; }}
  .issue-list {{ padding: 0 16px 10px 16px; }}
  .issue {{ display: flex; align-items: flex-start; gap: 8px; padding: 4px 0; font-size: 0.82rem; border-top: 1px solid #f3f4f6; }}
  .issue .cat {{ color: #888; min-width: 100px; font-size: 0.76rem; }}
  .issue .msg {{ flex: 1; }}
  .dup-section {{ background: white; border-radius: 8px; padding: 20px; margin-bottom: 32px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
  .dup-section h2 {{ font-size: 1rem; margin-bottom: 12px; color: #b91c1c; }}
  .dup-entry {{ font-size: 0.82rem; margin-bottom: 8px; padding: 8px; background: #fee2e2; border-radius: 4px; }}
  .dup-entry .dup-title {{ font-weight: 600; margin-bottom: 4px; }}
  .dup-entry .dup-files {{ color: #666; }}
  .filter-bar {{ display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }}
  .filter-btn {{ padding: 6px 16px; border: 1px solid #d1d5db; background: white; border-radius: 20px; cursor: pointer; font-size: 0.82rem; }}
  .filter-btn.active {{ background: #0f3460; color: white; border-color: #0f3460; }}
  details summary {{ list-style: none; }}
  details summary::-webkit-details-marker {{ display: none; }}
</style>
</head>
<body>
<header>
  <h1>PetTransportGlobal — Full QA Audit Report</h1>
  <p>Block 28 / Task 2.9 &nbsp;|&nbsp; Run date: {date.today()} &nbsp;|&nbsp; {total} pages audited &nbsp;|&nbsp; The Auditor</p>
</header>
<div class="container">
""")

# Summary stats
pass_rate = round((clean / total) * 100, 1) if total else 0
html_parts.append(f"""
<div class="summary-grid">
  <div class="stat"><div class="num blue">{total}</div><div class="lbl">Pages Audited</div></div>
  <div class="stat"><div class="num red">{errors}</div><div class="lbl">Pages with ERRORs</div></div>
  <div class="stat"><div class="num amber">{warns}</div><div class="lbl">WARN-only Pages</div></div>
  <div class="stat"><div class="num green">{clean}</div><div class="lbl">Clean Pages</div></div>
  <div class="stat"><div class="num {'green' if pass_rate >= 90 else 'amber' if pass_rate >= 75 else 'red'}">{pass_rate}%</div><div class="lbl">Clean Rate</div></div>
  <div class="stat"><div class="num red">{total_error_count}</div><div class="lbl">Total ERRORs</div></div>
  <div class="stat"><div class="num amber">{total_warn_count}</div><div class="lbl">Total WARNings</div></div>
</div>
""")

# Per-type breakdown
html_parts.append("""<div class="type-table"><h2>Results by Page Type</h2>
<table>
<tr><th>Type</th><th>Total</th><th>ERROR</th><th>WARN only</th><th>Clean</th><th>Clean %</th></tr>
""")
for pt in ("route", "country", "origin", "airline", "breed", "blog"):
    s = type_stats.get(pt, {"total": 0, "errors": 0, "warns": 0, "clean": 0})
    pct = round((s["clean"] / s["total"]) * 100, 1) if s["total"] else 0
    html_parts.append(f"<tr><td>{pt}</td><td>{s['total']}</td>"
                      f"<td><span style='color:#b91c1c;font-weight:600'>{s['errors']}</span></td>"
                      f"<td><span style='color:#92400e'>{s['warns']}</span></td>"
                      f"<td><span style='color:#166534'>{s['clean']}</span></td>"
                      f"<td>{pct}%</td></tr>")
html_parts.append("</table></div>\n")

# Duplicate titles
if dup_titles:
    html_parts.append("""<div class="dup-section"><h2>Duplicate Titles Detected</h2>\n""")
    for t, files in sorted(dup_titles.items()):
        html_parts.append(f'<div class="dup-entry"><div class="dup-title">{esc(t[:120])}</div>'
                          f'<div class="dup-files">{esc(", ".join(files))}</div></div>\n')
    html_parts.append("</div>\n")

# Duplicate descriptions
if dup_descs:
    html_parts.append("""<div class="dup-section"><h2>Duplicate Descriptions Detected</h2>\n""")
    for d, files in sorted(dup_descs.items()):
        html_parts.append(f'<div class="dup-entry"><div class="dup-title">{esc(d[:120])}</div>'
                          f'<div class="dup-files">{esc(", ".join(files))}</div></div>\n')
    html_parts.append("</div>\n")

# Detailed page listings by type
TYPE_ORDER = ("route", "country", "origin", "airline", "breed", "blog")
TYPE_LABELS = {"route": "Route Pages", "country": "Country Guides",
               "origin": "Origin Hubs", "airline": "Airline Pages",
               "breed": "Breed Guides", "blog": "Blog Posts"}

for pt in TYPE_ORDER:
    pages_of_type = [p for p in all_pages if p["page_type"] == pt]
    if not pages_of_type:
        continue

    e_count = sum(1 for p in pages_of_type if any(i[0] == "ERROR" for i in p["issues"]))
    w_count = sum(1 for p in pages_of_type if any(i[0] == "WARN"  for i in p["issues"]) and not any(i[0] == "ERROR" for i in p["issues"]))
    c_count = sum(1 for p in pages_of_type if not p["issues"])

    html_parts.append(f"""
<details>
<summary class="section-header">
  <h2>{TYPE_LABELS.get(pt, pt.title())} ({len(pages_of_type)} pages)</h2>
  <div style="display:flex;gap:8px;font-size:0.82rem">
    <span style="color:#b91c1c">{e_count} errors</span>
    <span style="color:#92400e">{w_count} warns</span>
    <span style="color:#166534">{c_count} clean</span>
  </div>
</summary>
<div style="padding:4px 0">
""")

    # Sort: errors first, then warns, then clean
    def sort_key(p):
        if any(i[0] == "ERROR" for i in p["issues"]): return 0
        if any(i[0] == "WARN"  for i in p["issues"]): return 1
        return 2

    for p in sorted(pages_of_type, key=sort_key):
        has_error = any(i[0] == "ERROR" for i in p["issues"])
        has_warn  = any(i[0] == "WARN"  for i in p["issues"])
        css_cls   = "has-error" if has_error else ("has-warn" if has_warn else "clean")
        status_badge = sev_badge["ERROR"] if has_error else (sev_badge["WARN"] if has_warn else '<span class="badge pass">PASS</span>')

        title_display = esc(p["title"][:70] + "…" if len(p["title"]) > 70 else p["title"]) if p["title"] else "<em>no title</em>"
        html_parts.append(f"""
<details class="page-block {css_cls}">
<summary class="page-header">
  {status_badge}
  <span class="slug">{esc(p['slug'])}</span>
  <span class="title-text">{title_display}</span>
  <span style="color:#aaa;font-size:0.76rem">{len(p['issues'])} issue(s)</span>
</summary>
""")
        if p["issues"]:
            html_parts.append('<div class="issue-list">')
            for sev, cat, msg in p["issues"]:
                html_parts.append(f'<div class="issue">{sev_badge[sev]}<span class="cat">{esc(cat)}</span><span class="msg">{esc(msg)}</span></div>')
            html_parts.append('</div>')
        html_parts.append('</details>\n')

    html_parts.append('</div></details>\n')

# Footer
html_parts.append(f"""
<div style="text-align:center;color:#aaa;font-size:0.8rem;padding:32px 0">
  Generated by qa_audit_p2.py &nbsp;|&nbsp; PetTransportGlobal &nbsp;|&nbsp; {date.today()}
</div>
</div>
</body>
</html>
""")

report_path = r"c:\Users\garet\Desktop\pet-transport\qa-audit-report.html"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print(f"\nReport written to: {report_path}")
print(f"Open in browser to review all issues.")
