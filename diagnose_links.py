import os
import re
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter

REPO_ROOT = Path(__file__).parent
PUBLIC_DIR = REPO_ROOT / "site" / "public"

# Build known_paths
known_paths = set()
for root, dirs, files in os.walk(PUBLIC_DIR):
    dirs[:] = [d for d in dirs if d not in ["css","js","fonts","images","img","styles","vendor"]]
    for fname in files:
        if fname == "index.html":
            rel = os.path.relpath(os.path.join(root, fname), PUBLIC_DIR)
            url_path = "/" + rel.replace("\\","/").replace("/index.html","")
            url_path = url_path.rstrip("/") + "/"
            known_paths.add(url_path)
        elif fname.endswith(".html") and fname != "index.html":
            rel = os.path.relpath(os.path.join(root, fname), PUBLIC_DIR)
            known_paths.add("/" + rel.replace("\\","/"))
known_paths.add("/")

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a":
            href = attrs_dict.get("href", "")
            if href and href.startswith("/") and not href.startswith("//"):
                self.links.append(href)

broken_counter = Counter()
example_pages = {}

content_dirs = ["pet-transport", "blog"]
for cdir in content_dirs:
    cpath = PUBLIC_DIR / cdir
    if cpath.exists():
        for root, dirs, files in os.walk(cpath):
            dirs[:] = [d for d in dirs if d not in ["css","js"]]
            for fname in files:
                if fname == "index.html":
                    html_file = Path(root) / fname
                    try:
                        content = html_file.read_text(encoding="utf-8", errors="ignore")
                        parser = LinkExtractor()
                        parser.feed(content)
                        page_url = "/" + str(html_file.relative_to(PUBLIC_DIR)).replace("\\","/").replace("/index.html","/")
                        for href in parser.links:
                            clean = href.split("#")[0].split("?")[0]
                            if not clean:
                                continue
                            norm = clean.rstrip("/") + "/"
                            if norm not in known_paths and clean not in known_paths:
                                fp = PUBLIC_DIR / clean.lstrip("/")
                                if not fp.exists():
                                    broken_counter[href] += 1
                                    if href not in example_pages:
                                        example_pages[href] = page_url
                    except:
                        pass

print("Top 30 most common broken links:")
for href, count in broken_counter.most_common(30):
    print(f"  {count:4d}x  {href}   (e.g. {example_pages[href]})")

print(f"\nTotal unique broken hrefs: {len(broken_counter)}")
