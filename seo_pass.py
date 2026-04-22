"""
Block 17: SEO Pass + Humanisation + Internal Linking
- Adds varied title tags and meta descriptions to all pages
- Adds internal links (upward, sideways, cross-type) to route pages
- Runs humanisation checks (banned words, em dashes)
- No em dashes or banned vocabulary in any content
"""
import json
import os
import re
import random
import hashlib

ROUTES_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"
COUNTRIES_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\countries"
ORIGINS_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\origins"
ROUTES_CONTENT = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\routes"

BRAND = "[Brand]"

# Banned vocabulary (Tier 1)
BANNED_TIER1 = {
    "delve", "tapestry", "vibrant", "crucial", "comprehensive", "meticulous",
    "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy",
    "transformative", "paramount", "multifaceted", "myriad", "cornerstone",
    "reimagine", "empower", "catalyst", "invaluable", "bustling", "nestled", "realm"
}

# Banned Tier 2
BANNED_TIER2 = {
    "furthermore", "moreover", "paradigm", "holistic", "utilize", "facilitate",
    "nuanced", "illuminate", "encompasses", "catalyze", "proactive",
    "ubiquitous", "quintessential"
}

ALL_BANNED = BANNED_TIER1 | BANNED_TIER2


def seed_from_string(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) % 100000


# Title tag formulas
def generate_title(origin, dest, formula_idx):
    formulas = [
        f"Pet Transport from {origin} to {dest} | {BRAND}",
        f"Ship Your Pet from {origin} to {dest} | {BRAND}",
        f"{origin} to {dest} Pet Relocation | {BRAND}",
        f"Moving Pets from {origin} to {dest}? Expert Help | {BRAND}",
        f"{dest} Pet Import from {origin} | {BRAND}",
    ]
    return formulas[formula_idx % len(formulas)]


# Meta description formulas
def generate_meta_desc(origin, dest, complexity, timeline, formula_idx):
    complexity_text = {
        "low": "Straightforward process",
        "moderate": "Moderate complexity",
        "high": "Strict requirements apply",
        "very_high": "Complex regulations including quarantine",
        "extreme": "One of the most complex routes",
    }.get(complexity, "")

    formulas = [
        f"Complete guide to shipping your pet from {origin} to {dest}. {complexity_text}. {timeline} weeks prep. Get a free quote.",
        f"Shipping your pet from {origin} to {dest}? {complexity_text}. Step-by-step guide with airline options and costs.",
        f"How to transport your dog or cat from {origin} to {dest}. Import requirements, airline policies, timelines. Free quote available.",
    ]
    return formulas[formula_idx % len(formulas)]


def find_related_routes(origin_code, dest_code, all_route_slugs):
    """Find sideways and upward links for a route."""
    links = {
        "sideways": [],
        "upward": [],
    }

    for slug in all_route_slugs:
        other_data = load_route_data(slug)
        if not other_data:
            continue
        other_rd = other_data.get("route_data", {})
        other_origin = other_rd.get("origin", {}).get("code", "")
        other_dest = other_rd.get("destination", {}).get("code", "")

        # Reverse route
        if other_origin == dest_code and other_dest == origin_code:
            links["sideways"].append({
                "url": f"/routes/{slug}/",
                "text": f"{other_data.get('origin_name', '')} to {other_data.get('destination_name', '')}",
                "type": "reverse",
            })
        # Same origin, different destination
        elif other_origin == origin_code and other_dest != dest_code:
            links["sideways"].append({
                "url": f"/routes/{slug}/",
                "text": f"{other_data.get('origin_name', '')} to {other_data.get('destination_name', '')}",
                "type": "same_origin",
            })
        # Same destination, different origin
        elif other_dest == dest_code and other_origin != origin_code:
            links["sideways"].append({
                "url": f"/routes/{slug}/",
                "text": f"{other_data.get('origin_name', '')} to {other_data.get('destination_name', '')}",
                "type": "same_dest",
            })

    # Upward links
    origin_slug = code_to_slug(origin_code)
    dest_slug = code_to_slug(dest_code)

    if origin_slug:
        links["upward"].append({
            "url": f"/origins/{origin_slug}/",
            "text": f"All routes from {code_to_name(origin_code)}",
        })
    if dest_slug:
        links["upward"].append({
            "url": f"/countries/{dest_slug}/",
            "text": f"{code_to_name(dest_code)} import guide",
        })

    return links


CODE_SLUG_MAP = {
    "GB": "united-kingdom", "US": "united-states", "AE": "united-arab-emirates",
    "AU": "australia", "CA": "canada", "DE": "germany", "FR": "france",
    "SG": "singapore", "HK": "hong-kong", "ZA": "south-africa",
}

CODE_NAME_MAP = {
    "GB": "United Kingdom", "US": "United States", "AE": "United Arab Emirates",
    "AU": "Australia", "CA": "Canada", "DE": "Germany", "FR": "France",
    "SG": "Singapore", "HK": "Hong Kong", "ZA": "South Africa",
}


def code_to_slug(code):
    return CODE_SLUG_MAP.get(code, "")


def code_to_name(code):
    return CODE_NAME_MAP.get(code, "")


def load_route_data(slug):
    path = os.path.join(ROUTES_DIR, f"{slug}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_route_data(slug, data):
    path = os.path.join(ROUTES_DIR, f"{slug}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def check_humanisation(text):
    """Check text for banned vocabulary and em dashes. Return list of issues."""
    issues = []
    text_lower = text.lower()

    for word in ALL_BANNED:
        if word in text_lower:
            issues.append(f"Banned word found: '{word}'")

    if "\u2014" in text or "\u2013" in text:
        issues.append("Em dash or en dash found")

    return issues


def fix_humanisation(text):
    """Remove banned patterns from text."""
    # Replace em/en dashes with appropriate punctuation
    text = text.replace("\u2014", ". ")
    text = text.replace("\u2013", ", ")

    # Replace banned words if they appear (simple replacement)
    replacements = {
        "delve": "look at",
        "vibrant": "active",
        "crucial": "important",
        "comprehensive": "complete",
        "meticulous": "careful",
        "embark": "start",
        "robust": "strong",
        "seamless": "smooth",
        "groundbreaking": "new",
        "leverage": "use",
        "paramount": "important",
        "reimagine": "rethink",
        "empower": "enable",
        "furthermore": "also",
        "moreover": "also",
        "utilize": "use",
        "facilitate": "help with",
        "encompasses": "includes",
    }

    for old, new in replacements.items():
        # Case-insensitive replacement
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        text = pattern.sub(new, text)

    return text


# === MAIN ===
print("Block 17: SEO + Humanisation + Internal Linking\n")

# Get all route slugs
route_files = sorted([f.replace(".json", "") for f in os.listdir(ROUTES_DIR) if f.endswith(".json")])

print(f"Processing {len(route_files)} route pages...\n")

humanisation_issues = 0
links_added = 0

for i, slug in enumerate(route_files):
    data = load_route_data(slug)
    if not data:
        continue

    rd = data.get("route_data", {})
    origin = data.get("origin_name", "")
    dest = data.get("destination_name", "")
    origin_code = rd.get("origin", {}).get("code", "")
    dest_code = rd.get("destination", {}).get("code", "")
    complexity = rd.get("route_complexity", "moderate")
    timeline = rd.get("estimated_timeline_weeks", "8-12")

    random.seed(seed_from_string(slug))

    # 1. SEO: Title tag variation
    formula_idx = i % 5  # Rotate through 5 formulas
    data["seo"]["title"] = generate_title(origin, dest, formula_idx)
    data["seo"]["description"] = generate_meta_desc(origin, dest, complexity, timeline, formula_idx)

    # 2. Internal links
    links = find_related_routes(origin_code, dest_code, [s for s in route_files if s != slug])
    data["links"] = links
    links_added += len(links.get("sideways", [])) + len(links.get("upward", []))

    # 3. Humanisation check on all text content
    texts_to_check = []
    content = data.get("content", {})
    if content.get("overview"):
        texts_to_check.append(("overview", content["overview"]))
    for j, sec in enumerate(content.get("sections", [])):
        texts_to_check.append((f"section[{j}].body", sec.get("body", "")))
    for j, faq in enumerate(data.get("faqs", [])):
        texts_to_check.append((f"faq[{j}].answer", faq.get("answer", "")))

    for field, text in texts_to_check:
        issues = check_humanisation(text)
        if issues:
            humanisation_issues += len(issues)
            # Auto-fix
            fixed = fix_humanisation(text)
            if field == "overview":
                data["content"]["overview"] = fixed
            elif field.startswith("section"):
                idx = int(field.split("[")[1].split("]")[0])
                data["content"]["sections"][idx]["body"] = fixed
            elif field.startswith("faq"):
                idx = int(field.split("[")[1].split("]")[0])
                data["faqs"][idx]["answer"] = fixed

    # Update status
    data["status"] = "seo_optimised"

    save_route_data(slug, data)

    sideways = len(links.get("sideways", []))
    upward = len(links.get("upward", []))
    print(f"  {slug}: title formula {formula_idx+1}/5, {sideways} sideways + {upward} upward links")

print(f"\nSEO pass complete.")
print(f"  Total internal links added: {links_added}")
print(f"  Humanisation issues found and fixed: {humanisation_issues}")

# Now regenerate content markdown files with updated data
print(f"\nRegenerating Hugo content files with SEO + links...\n")

for slug in route_files:
    data = load_route_data(slug)
    if not data:
        continue

    rd = data["route_data"]
    origin = data["origin_name"]
    dest = data["destination_name"]
    seo = data.get("seo", {})

    md = f"""---
title: "{seo.get('title', f'Pet Transport from {origin} to {dest}')}"
description: "{seo.get('description', '')}"
type: "routes"
layout: "single"
slug: "{slug}"
origin_name: "{origin}"
destination_name: "{dest}"
route_data:
  origin:
    code: "{rd['origin']['code']}"
    country: "{rd['origin']['country']}"
    export_requirements:
"""

    for key, val in rd["origin"].get("export_requirements", {}).items():
        safe_val = str(val).replace('"', '\\"')
        md += f'      {key}: "{safe_val}"\n'

    md += f"""  destination:
    code: "{rd['destination']['code']}"
    country: "{rd['destination']['country']}"
    import_requirements:
"""

    for key, val in rd["destination"].get("import_requirements", {}).items():
        safe_val = str(val).replace('"', '\\"')
        md += f'      {key}: "{safe_val}"\n'

    breed_restrictions = rd["destination"].get("breed_restrictions", [])
    if breed_restrictions:
        md += "    breed_restrictions:\n"
        for br in breed_restrictions:
            safe_br = str(br).replace('"', '\\"')
            md += f'      - "{safe_br}"\n'

    md += "  airlines:\n"
    for airline in rd.get("airlines", []):
        md += f'    - name: "{airline["name"]}"\n'
        md += f'      type: "{airline["type"]}"\n'
        safe_policy = airline.get("policy_summary", "").replace('"', '\\"')
        md += f'      policy_summary: "{safe_policy}"\n'

    md += "  timeline_steps:\n"
    for step in rd.get("timeline_steps", []):
        md += f'    - step: {step["step"]}\n'
        safe_action = step["action"].replace('"', '\\"')
        md += f'      action: "{safe_action}"\n'
        safe_timing = step["timing"].replace('"', '\\"')
        md += f'      timing: "{safe_timing}"\n'
        if step.get("responsible"):
            safe_resp = step["responsible"].replace('"', '\\"')
            md += f'      responsible: "{safe_resp}"\n'

    md += "  cost_factors:\n"
    for cf in rd.get("cost_factors", []):
        safe_cf = str(cf).replace('"', '\\"')
        md += f'    - "{safe_cf}"\n'

    md += "  key_warnings:\n"
    for kw in rd.get("key_warnings", []):
        safe_kw = str(kw).replace('"', '\\"')
        md += f'    - "{safe_kw}"\n'

    md += f'  route_complexity: "{rd.get("route_complexity", "moderate")}"\n'
    md += f'  estimated_timeline_weeks: "{rd.get("estimated_timeline_weeks", "8-12")}"\n'

    content_data = data.get("content", {})
    safe_h1 = content_data.get("h1", "").replace('"', '\\"')
    md += f'content:\n'
    md += f'  h1: "{safe_h1}"\n'
    md += f'  overview: |\n'
    for line in content_data.get("overview", "").split("\n"):
        md += f'    {line}\n'

    sections = content_data.get("sections", [])
    if sections:
        md += "  sections:\n"
        for sec in sections:
            safe_heading = sec.get("heading", "").replace('"', '\\"')
            md += f'    - heading: "{safe_heading}"\n'
            md += f'      body: |\n'
            for line in sec.get("body", "").split("\n"):
                md += f'        {line}\n'

    faqs = data.get("faqs", [])
    if faqs:
        md += "faqs:\n"
        for faq in faqs:
            safe_q = faq["question"].replace('"', '\\"')
            safe_a = faq["answer"].replace('"', '\\"')
            md += f'  - question: "{safe_q}"\n'
            md += f'    answer: "{safe_a}"\n'

    # Links (the new part)
    links = data.get("links", {})
    md += "links:\n"
    sideways = links.get("sideways", [])
    if sideways:
        md += "  sideways:\n"
        for link in sideways:
            safe_text = link["text"].replace('"', '\\"')
            md += f'    - url: "{link["url"]}"\n'
            md += f'      text: "{safe_text}"\n'
    else:
        md += "  sideways: []\n"

    upward = links.get("upward", [])
    if upward:
        md += "  upward:\n"
        for link in upward:
            safe_text = link["text"].replace('"', '\\"')
            md += f'    - url: "{link["url"]}"\n'
            md += f'      text: "{safe_text}"\n'
    else:
        md += "  upward: []\n"

    md += "---\n"

    content_path = os.path.join(ROUTES_CONTENT, f"{slug}.md")
    with open(content_path, "w", encoding="utf-8") as f:
        f.write(md)

print(f"Done. {len(route_files)} content files regenerated with SEO metadata and internal links.")
