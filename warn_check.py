import re, os
from collections import Counter

BASE = r"c:\Users\garet\Desktop\pet-transport\site\content"
DIRS = {"route": "routes", "country": "countries", "origin": "origins", "airline": "airlines", "breed": "breeds", "blog": "blog"}

BANNED_WORDS = [
    "delve", "tapestry", "vibrant", "crucial", "comprehensive", "meticulous",
    "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy",
    "transformative", "paramount", "multifaceted", "myriad", "cornerstone",
    "reimagine", "empower", "catalyst", "invaluable", "bustling", "nestled",
    "realm", "furthermore", "moreover", "paradigm", "holistic", "utilize",
    "facilitate", "nuanced", "illuminate", "encompasses", "catalyze", "proactive",
    "ubiquitous", "quintessential", "navigate", "navigating", "testament",
    "landscape", "ecosystem",
]

warn_cats = Counter()
banned_detail = []

for pt, dn in DIRS.items():
    d = os.path.join(BASE, dn)
    if not os.path.isdir(d):
        continue
    for fn in os.listdir(d):
        if not fn.endswith(".md") or fn == "_index.md":
            continue
        content = open(os.path.join(d, fn), encoding="utf-8").read()
        cl = content.lower()

        # Title length
        m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if m:
            tlen = len(m.group(1).strip().strip('"'))
            if tlen > 75:
                warn_cats["title_too_long_" + pt] += 1
            if tlen < 30:
                warn_cats["title_too_short_" + pt] += 1

        # Description length
        m = re.search(r'^description:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if m:
            dlen = len(m.group(1).strip().strip('"'))
            if dlen > 175:
                warn_cats["desc_too_long_" + pt] += 1
            if dlen < 100:
                warn_cats["desc_too_short_" + pt] += 1

        # Banned words
        found = [w for w in BANNED_WORDS if re.search(r"\b" + re.escape(w) + r"\b", cl)]
        if found:
            warn_cats["banned_word_" + pt] += 1
            banned_detail.append((fn, pt, found[:5]))

        # FAQs
        faqs = len(re.findall(r"question:", content))
        if pt in ("route", "country", "airline", "breed") and faqs < 4:
            warn_cats["few_faqs_" + pt] += 1

        # Sideways links
        if pt == "route" and "sideways:" not in content:
            warn_cats["no_sideways_route"] += 1

        # Origin hub popular routes
        if pt == "origin" and "popular routes" not in cl:
            warn_cats["missing_popular_routes_origin"] += 1

print("=== WARNING BREAKDOWN ===")
for k, v in sorted(warn_cats.items(), key=lambda x: -x[1]):
    print(f"  {v:3d}  {k}")

print("\n=== BANNED WORD SAMPLES (first 20) ===")
for fn, pt, words in banned_detail[:20]:
    print(f"  [{pt}] {fn}: {words}")
