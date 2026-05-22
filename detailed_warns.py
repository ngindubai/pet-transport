"""
Show all remaining warnings from qa_audit_p2 logic - categorized.
"""
import os, re
from collections import Counter

BASE = r"c:\Users\garet\Desktop\pet-transport\site\content"
ROUTES_DIR    = os.path.join(BASE, "routes")
COUNTRIES_DIR = os.path.join(BASE, "countries")
ORIGINS_DIR   = os.path.join(BASE, "origins")
AIRLINES_DIR  = os.path.join(BASE, "airlines")
BREEDS_DIR    = os.path.join(BASE, "breeds")
BLOG_DIR      = os.path.join(BASE, "blog")

def build_slug_set(directory):
    result = set()
    if not os.path.isdir(directory):
        return result
    for f in os.listdir(directory):
        if f.endswith(".md") and f != "_index.md":
            result.add(f[:-3])
    return result

ALL_ORIGIN_SLUGS  = build_slug_set(ORIGINS_DIR)
ALL_COUNTRY_SLUGS = build_slug_set(COUNTRIES_DIR)
ALL_AIRLINE_SLUGS = build_slug_set(AIRLINES_DIR)
ALL_BREED_SLUGS   = build_slug_set(BREEDS_DIR)
ALL_BLOG_SLUGS    = build_slug_set(BLOG_DIR)
ALL_ROUTE_SLUGS   = build_slug_set(ROUTES_DIR)

INTERNAL_PREFIXES = {
    "/pet-transport/origins/":   ORIGINS_DIR,
    "/pet-transport/countries/": COUNTRIES_DIR,
    "/pet-transport/airlines/":  AIRLINES_DIR,
    "/pet-transport/breeds/":    BREEDS_DIR,
    "/blog/":                    BLOG_DIR,
}
ROUTE_URL_PREFIX = "/pet-transport/"

def url_exists(url):
    url = url.rstrip("/")
    for prefix, directory in INTERNAL_PREFIXES.items():
        if url.startswith(prefix.rstrip("/")):
            slug = url[len(prefix.rstrip("/")):].strip("/")
            return os.path.exists(os.path.join(directory, slug + ".md"))
    if url.startswith(ROUTE_URL_PREFIX.rstrip("/")):
        slug = url[len(ROUTE_URL_PREFIX.rstrip("/")):].strip("/")
        if slug and "/" not in slug:
            return os.path.exists(os.path.join(ROUTES_DIR, slug + ".md"))
    return True

BANNED_WORDS = [
    "delve","tapestry","vibrant","crucial","comprehensive","meticulous","embark",
    "robust","seamless","groundbreaking","leverage","synergy","transformative",
    "paramount","multifaceted","myriad","cornerstone","reimagine","empower",
    "catalyst","invaluable","bustling","nestled","realm","furthermore","moreover",
    "paradigm","holistic","utilize","facilitate","nuanced","illuminate","encompasses",
    "catalyze","proactive","ubiquitous","quintessential","navigate","navigating",
    "testament","landscape","ecosystem","dive into","game-changer","cutting-edge",
]

warn_cats = Counter()
warn_details = []

for dirpath, page_type in [
    (ROUTES_DIR,"route"), (COUNTRIES_DIR,"country"), (ORIGINS_DIR,"origin"),
    (AIRLINES_DIR,"airline"), (BREEDS_DIR,"breed"), (BLOG_DIR,"blog"),
]:
    for fn in sorted(os.listdir(dirpath)):
        if not fn.endswith(".md") or fn == "_index.md":
            continue
        path = os.path.join(dirpath, fn)
        raw = open(path, encoding="utf-8").read()
        raw_lower = raw.lower()

        fm_match = re.match(r"^---\s*\n(.*?)\n---", raw, re.DOTALL)
        front_matter = fm_match.group(1) if fm_match else ""

        def fm_get(key):
            m = re.search(r"^" + re.escape(key) + r':\s*["\']?(.+?)["\']?\s*$', front_matter, re.MULTILINE)
            return m.group(1).strip().strip('"\'') if m else ""

        title = fm_get("title")
        description = fm_get("description")

        if title:
            tlen = len(title)
            if tlen < 30:
                warn_cats["title_too_short"] += 1
                warn_details.append((fn, page_type, f"title too short ({tlen} chars): {title}"))
            elif tlen > 75:
                warn_cats["title_too_long"] += 1
                warn_details.append((fn, page_type, f"title too long ({tlen} chars): {title}"))

        if description:
            dlen = len(description)
            if dlen < 100:
                warn_cats["desc_too_short"] += 1
                warn_details.append((fn, page_type, f"desc too short ({dlen} chars)"))
            elif dlen > 175:
                warn_cats["desc_too_long"] += 1
                warn_details.append((fn, page_type, f"desc too long ({dlen} chars)"))

        faq_count = len(re.findall(r"question:", raw))
        if page_type in ("route","country","airline","breed") and faq_count < 4:
            warn_cats["few_faqs"] += 1
            warn_details.append((fn, page_type, f"only {faq_count} FAQs"))

        if page_type == "route" and "sideways:" not in raw:
            warn_cats["no_sideways"] += 1
            warn_details.append((fn, page_type, "no sideways links"))

        if page_type == "origin" and "popular routes" not in raw_lower:
            warn_cats["no_popular_routes"] += 1
            warn_details.append((fn, page_type, "no Popular routes section"))

        internal_urls = re.findall(r'url:\s*["\']?(/[^\s"\'\n]+)["\']?', raw)
        for url in internal_urls:
            url_clean = url.strip('"\'').rstrip("/")
            if (url_clean.startswith("/pet-transport") or url_clean.startswith("/blog")):
                if not url_exists(url_clean):
                    warn_cats["broken_link"] += 1
                    warn_details.append((fn, page_type, f"broken internal link: {url_clean}"))

        banned_found = [w for w in BANNED_WORDS if re.search(r"\b" + re.escape(w) + r"\b", raw_lower)]
        for w in banned_found:
            warn_cats["banned_word"] += 1
            warn_details.append((fn, page_type, f"banned word: '{w}'"))

        if "\u2013" in raw:
            warn_cats["en_dash"] += 1
            warn_details.append((fn, page_type, "en dash found"))

print("=== WARN CATEGORIES ===")
for k, v in sorted(warn_cats.items(), key=lambda x: -x[1]):
    print(f"  {v:3d}  {k}")

print(f"\n=== ALL WARNINGS ({len(warn_details)}) ===")
for fn, pt, msg in warn_details:
    print(f"  [{pt}] {fn}: {msg}")
