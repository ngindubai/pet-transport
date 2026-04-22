"""
Block 18: QA Audit
Checks all content files for:
- YMYL compliance (no safety guarantees)
- Banned vocabulary
- Complete data (all required fields present)
- Internal links (no orphan pages)
- Humaniser rules (no em dashes, no banned patterns)
- Schema data completeness
"""
import json
import os
import re

ROUTES_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"
COUNTRIES_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\countries"
CONTENT_ROUTES = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\routes"
CONTENT_COUNTRIES = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\countries"
CONTENT_ORIGINS = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\origins"

BANNED_WORDS = {
    "delve", "tapestry", "vibrant", "crucial", "comprehensive", "meticulous",
    "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy",
    "transformative", "paramount", "multifaceted", "myriad", "cornerstone",
    "reimagine", "empower", "catalyst", "invaluable", "bustling", "nestled", "realm",
    "furthermore", "moreover", "paradigm", "holistic", "utilize", "facilitate",
    "nuanced", "illuminate", "encompasses", "catalyze", "proactive",
    "ubiquitous", "quintessential"
}

SAFETY_GUARANTEE_PATTERNS = [
    r"guarantee[ds]?\s+(safety|protection|safe)",
    r"100%\s+safe",
    r"completely\s+safe",
    r"stay\s+safe",
    r"guaranteed\s+protection",
    r"ensure[ds]?\s+(safety|your pet is safe)",
    r"risk[- ]free",
]

BANNED_PHRASES = [
    "in today's digital age",
    "it is worth noting",
    "plays a crucial role",
    "serves as a testament",
    "in the realm of",
    "harness the power of",
    "embark on a journey",
    "without further ado",
]

results = {
    "total_pages": 0,
    "passed": 0,
    "warnings": 0,
    "errors": 0,
    "details": [],
}


def check_text(text, page_name):
    """Check text for violations. Returns list of (severity, message)."""
    issues = []
    text_lower = text.lower()

    # Banned vocabulary
    for word in BANNED_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
            issues.append(("ERROR", f"Banned word: '{word}'"))

    # Em dashes
    if "\u2014" in text:
        issues.append(("ERROR", "Em dash found (use periods, commas, or colons)"))
    if "\u2013" in text:
        issues.append(("WARNING", "En dash found"))

    # Safety guarantees (YMYL)
    for pattern in SAFETY_GUARANTEE_PATTERNS:
        if re.search(pattern, text_lower):
            issues.append(("ERROR", f"YMYL violation: safety guarantee pattern '{pattern}'"))

    # Banned phrases
    for phrase in BANNED_PHRASES:
        if phrase.lower() in text_lower:
            issues.append(("ERROR", f"Banned phrase: '{phrase}'"))

    return issues


def audit_route(slug):
    """Audit a single route data file."""
    path = os.path.join(ROUTES_DIR, f"{slug}.json")
    if not os.path.exists(path):
        return [("ERROR", "Route data file missing")]

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    issues = []
    rd = data.get("route_data", {})

    # Required fields check
    required = ["origin_name", "destination_name", "route_data", "seo", "content", "faqs"]
    for field in required:
        if not data.get(field):
            issues.append(("ERROR", f"Missing required field: {field}"))

    # Route data completeness
    rd_required = ["origin", "destination", "airlines", "timeline_steps", "cost_factors", "key_warnings"]
    for field in rd_required:
        if not rd.get(field):
            issues.append(("ERROR", f"Missing route_data.{field}"))

    # Import requirements check
    import_reqs = rd.get("destination", {}).get("import_requirements", {})
    import_fields = ["microchip", "rabies_vaccination", "health_certificate"]
    for field in import_fields:
        if not import_reqs.get(field):
            issues.append(("WARNING", f"Missing import requirement: {field}"))

    # Airlines check
    airlines = rd.get("airlines", [])
    if len(airlines) == 0:
        issues.append(("ERROR", "No airlines listed for route"))
    elif len(airlines) < 2:
        issues.append(("WARNING", f"Only {len(airlines)} airline(s) listed"))

    # Timeline steps check
    steps = rd.get("timeline_steps", [])
    if len(steps) < 5:
        issues.append(("WARNING", f"Only {len(steps)} timeline steps (expected 5+)"))

    # SEO check
    seo = data.get("seo", {})
    title = seo.get("title", "")
    desc = seo.get("description", "")
    if not title:
        issues.append(("ERROR", "Missing SEO title"))
    elif len(title) > 70:
        issues.append(("WARNING", f"SEO title too long ({len(title)} chars, max 70)"))
    if not desc:
        issues.append(("ERROR", "Missing SEO description"))
    elif len(desc) > 170:
        issues.append(("WARNING", f"SEO description too long ({len(desc)} chars, max 170)"))

    # Content check
    content = data.get("content", {})
    if not content.get("overview"):
        issues.append(("ERROR", "Missing content overview"))
    if not content.get("sections"):
        issues.append(("WARNING", "No content sections"))
    elif len(content["sections"]) < 2:
        issues.append(("WARNING", f"Only {len(content['sections'])} content section(s)"))

    # FAQ check
    faqs = data.get("faqs", [])
    if len(faqs) < 5:
        issues.append(("WARNING", f"Only {len(faqs)} FAQs (expected 5+)"))

    # Links check
    links = data.get("links", {})
    sideways = links.get("sideways", [])
    upward = links.get("upward", [])
    if not sideways:
        issues.append(("WARNING", "No sideways (related) links"))
    if not upward:
        issues.append(("WARNING", "No upward links (origin hub, country guide)"))

    # Text content humanisation check
    all_text = content.get("overview", "") + " "
    for sec in content.get("sections", []):
        all_text += sec.get("body", "") + " "
    for faq in faqs:
        all_text += faq.get("answer", "") + " "

    text_issues = check_text(all_text, slug)
    issues.extend(text_issues)

    return issues


def audit_page_file(filepath, page_type):
    """Audit a Hugo content markdown file."""
    if not os.path.exists(filepath):
        return [("ERROR", "Content file missing")]

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []

    # Check for required front matter fields
    if "title:" not in content:
        issues.append(("ERROR", "Missing title in front matter"))
    if "description:" not in content:
        issues.append(("ERROR", "Missing description in front matter"))

    # Check text content for humanisation
    text_issues = check_text(content, filepath)
    issues.extend(text_issues)

    return issues


# === MAIN ===
print("=" * 60)
print("PHASE 1 QA AUDIT REPORT")
print("=" * 60)
print()

# 1. Audit route data files
print("ROUTE PAGES (15 Tier 1)")
print("-" * 40)

route_files = sorted([f.replace(".json", "") for f in os.listdir(ROUTES_DIR) if f.endswith(".json")])

for slug in route_files:
    results["total_pages"] += 1
    issues = audit_route(slug)

    errors = [i for i in issues if i[0] == "ERROR"]
    warnings = [i for i in issues if i[0] == "WARNING"]

    if errors:
        status = "FAIL"
        results["errors"] += len(errors)
    elif warnings:
        status = "WARN"
    else:
        status = "PASS"
        results["passed"] += 1

    results["warnings"] += len(warnings)

    if issues:
        print(f"\n  [{status}] {slug}")
        for severity, msg in issues:
            print(f"    {severity}: {msg}")
    else:
        print(f"  [PASS] {slug}")

# 2. Audit route content markdown
print(f"\nROUTE CONTENT FILES")
print("-" * 40)

route_md_files = sorted([f for f in os.listdir(CONTENT_ROUTES) if f.endswith(".md") and f != "_index.md"])
for rf in route_md_files:
    issues = audit_page_file(os.path.join(CONTENT_ROUTES, rf), "route")
    errors = [i for i in issues if i[0] == "ERROR"]
    if errors:
        print(f"  [FAIL] {rf}: {len(errors)} errors")
        for s, m in errors:
            print(f"    {s}: {m}")
    else:
        print(f"  [PASS] {rf}")

# 3. Audit country guides
print(f"\nCOUNTRY GUIDES")
print("-" * 40)

country_files = sorted([f for f in os.listdir(CONTENT_COUNTRIES) if f.endswith(".md") and f != "_index.md"])
for cf in country_files:
    results["total_pages"] += 1
    issues = audit_page_file(os.path.join(CONTENT_COUNTRIES, cf), "country")
    errors = [i for i in issues if i[0] == "ERROR"]
    if errors:
        print(f"  [FAIL] {cf}: {len(errors)} errors")
    else:
        print(f"  [PASS] {cf}")
        results["passed"] += 1

# 4. Audit origin hubs
print(f"\nORIGIN HUBS")
print("-" * 40)

origin_files = sorted([f for f in os.listdir(CONTENT_ORIGINS) if f.endswith(".md") and f != "_index.md"])
for of_name in origin_files:
    results["total_pages"] += 1
    issues = audit_page_file(os.path.join(CONTENT_ORIGINS, of_name), "origin")
    errors = [i for i in issues if i[0] == "ERROR"]
    if errors:
        print(f"  [FAIL] {of_name}: {len(errors)} errors")
    else:
        print(f"  [PASS] {of_name}")
        results["passed"] += 1

# 5. Check site structure
print(f"\nSITE STRUCTURE CHECK")
print("-" * 40)

required_files = [
    r"c:\Users\garet\Desktop\Research\pet-transport\site\hugo.toml",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\_default\baseof.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\routes\single.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\countries\single.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\origins\single.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\assets\css\main.css",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\assets\js\main.js",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\partials\header.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\partials\footer.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\partials\quote-form.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\partials\faq-accordion.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\partials\breadcrumbs.html",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\layouts\robots.txt",
    r"c:\Users\garet\Desktop\Research\pet-transport\site\.gitignore",
]

for fp in required_files:
    if os.path.exists(fp):
        print(f"  [OK] {os.path.basename(fp)}")
    else:
        print(f"  [MISSING] {fp}")
        results["errors"] += 1

# Summary
print(f"\n{'=' * 60}")
print(f"QA AUDIT SUMMARY")
print(f"{'=' * 60}")
print(f"  Total pages audited: {results['total_pages']}")
print(f"  Passed: {results['passed']}")
print(f"  Warnings: {results['warnings']}")
print(f"  Errors: {results['errors']}")

route_count = len(route_files)
country_count = len(country_files)
origin_count = len(origin_files)
total_content_pages = route_count + country_count + origin_count

print(f"\n  Content inventory:")
print(f"    Route pages: {route_count}")
print(f"    Country guides: {country_count}")
print(f"    Origin hubs: {origin_count}")
print(f"    Total content pages: {total_content_pages}")

internal_links = 0
for slug in route_files:
    data = json.load(open(os.path.join(ROUTES_DIR, f"{slug}.json"), "r", encoding="utf-8"))
    links = data.get("links", {})
    internal_links += len(links.get("sideways", [])) + len(links.get("upward", []))
print(f"    Internal links: {internal_links}")

if results["errors"] == 0:
    print(f"\n  VERDICT: PHASE 1 READY FOR DEPLOYMENT")
    print(f"  (pending Gareth's TODO items: domain, brand, quote form email)")
else:
    print(f"\n  VERDICT: {results['errors']} ERRORS NEED FIXING BEFORE DEPLOYMENT")
