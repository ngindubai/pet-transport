import os
import re
from pathlib import Path
from html.parser import HTMLParser

REPO_ROOT = Path(__file__).parent
PUBLIC_DIR = REPO_ROOT / "site" / "public"

_LISTING_PAGES = {
    "/pet-transport/", "/pet-transport/airlines/", "/pet-transport/breeds/",
    "/pet-transport/countries/", "/pet-transport/origins/", "/pet-transport/routes/",
    "/pet-transport/resources/"
}

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1_count = 0
        self.has_meta_desc = False
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a":
            href = attrs_dict.get("href","")
            if href and href.startswith("/") and not href.startswith("//"):
                self.links.append(href)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and attrs_dict.get("name","").lower() == "description":
            self.has_meta_desc = True

schema_missing = []
content_dirs = ["pet-transport", "blog"]
for cdir in content_dirs:
    cpath = PUBLIC_DIR / cdir
    if cpath.exists():
        for root, dirs, files in os.walk(cpath):
            dirs[:] = [d for d in dirs if d not in ["css","js"]]
            for fname in files:
                if fname == "index.html":
                    html_file = Path(root) / fname
                    content = html_file.read_text(encoding="utf-8", errors="ignore")
                    page_url = "/" + str(html_file.relative_to(PUBLIC_DIR)).replace("\\","/").replace("/index.html","/")
                    if page_url.rstrip("/") + "/" in _LISTING_PAGES:
                        continue
                    if not ("schema.org" in content or "FAQPage" in content or "application/ld+json" in content):
                        schema_missing.append(page_url)

# Show by type
from collections import Counter
type_counts = Counter()
for u in schema_missing:
    if "/origins/" in u:
        type_counts["origins"] += 1
    elif "/countries/" in u:
        type_counts["countries"] += 1
    elif "/airlines/" in u:
        type_counts["airlines"] += 1
    elif "/breeds/" in u:
        type_counts["breeds"] += 1
    elif "/blog/" in u:
        type_counts["blog"] += 1
    elif "/pet-transport/" in u:
        type_counts["routes"] += 1
    else:
        type_counts["other"] += 1

print(f"Total pages missing schema: {len(schema_missing)}")
print("By type:", dict(type_counts))
print("\nFirst 20:")
for u in schema_missing[:20]:
    print(" ", u)
