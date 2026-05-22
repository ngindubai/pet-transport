"""
fix_routes.py — Fix all P1 route pages:
1. Add overview paragraph (if empty)
2. Add FAQs (if missing)
3. Populate sideways/upward links (url+text format)
4. Fix short meta descriptions (<140 chars)

Reads existing YAML front matter to generate route-specific content.
Skips files that already have content.
"""
import os
import re
import yaml

ROUTES_DIR = "site/content/routes"
ORIGINS_DIR = "site/content/origins"
COUNTRIES_DIR = "site/content/countries"

# Map of country name -> slug
COUNTRY_SLUGS = {
    "Australia": "australia",
    "Canada": "canada",
    "France": "france",
    "Germany": "germany",
    "Hong Kong": "hong-kong",
    "New Zealand": "new-zealand",
    "Singapore": "singapore",
    "South Africa": "south-africa",
    "Spain": "spain",
    "United Arab Emirates": "united-arab-emirates",
    "United Kingdom": "united-kingdom",
    "United States": "united-states",
}

# Complexity descriptions
COMPLEXITY_DESC = {
    "low": "a straightforward route",
    "moderate": "a moderately complex route",
    "high": "a high-complexity route",
    "very_high": "one of the most involved international pet moves you can make",
}

# Quarantine facts per destination country
QUARANTINE_FACTS = {
    "Australia": "Mandatory quarantine applies: all pets must complete a stay at the Mickleham Post-Entry Quarantine Facility in Melbourne. The facility is government-run and owner-paid. Plan for at least 10 days.",
    "New Zealand": "Mandatory quarantine applies: a minimum 10-day stay at the MPI-approved Auckland facility. Capacity is limited, so book early once your import permit is approved.",
    "Singapore": "Singapore requires a 30-day quarantine for most dogs and cats unless your pet qualifies for Group A (approved country of origin with short-term stay). Check Singapore AVS rules for your origin country.",
    "United Kingdom": "No routine quarantine for pets entering with valid documentation. Arriving with incorrect paperwork can result in penalty quarantine of up to 4 months at the owner's expense.",
    "United States": "No general quarantine for dogs and cats, but dogs must meet the CDC rabies vaccination requirements. Puppies under 6 months from certain countries face additional rules.",
    "Canada": "No routine quarantine for pets meeting import requirements.",
    "France": "No quarantine within the EU. Pets from approved third countries with correct documentation can enter without quarantine.",
    "Germany": "No quarantine within the EU for compliant pets.",
    "Spain": "No quarantine within the EU for compliant pets.",
    "United Arab Emirates": "Pets entering the UAE must be cleared by Dubai Municipality or Abu Dhabi Agriculture and Food Safety Authority. No mandatory quarantine for compliant pets, but documentation must be exact.",
    "Hong Kong": "Mandatory quarantine of 120 days applies for most origins. Approved countries (Australia, New Zealand, Ireland, Fiji, Hawaii, Japan, UK, Singapore) may qualify for shorter periods.",
    "South Africa": "No routine quarantine for dogs and cats entering South Africa, but a 5-day post-arrival health inspection and rabies requirements apply.",
}

# Titre test required info per destination
TITRE_REQUIRED = {
    "Australia": True,
    "New Zealand": True,
    "Singapore": True,  # some groups
    "United Kingdom": False,  # for EU/approved countries
    "United States": False,
    "Canada": False,
    "France": False,
    "Germany": False,
    "Spain": False,
    "United Arab Emirates": False,
    "Hong Kong": True,
    "South Africa": False,
}

def parse_front_matter(content):
    """Extract YAML front matter dict from markdown file."""
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None, content
    try:
        data = yaml.safe_load(m.group(1))
    except Exception:
        return None, content
    return data, content

def build_overview(origin, destination, rd):
    """Generate a 3-paragraph overview for a route."""
    complexity = rd.get("route_complexity", "moderate")
    complexity_text = COMPLEXITY_DESC.get(complexity, "a well-travelled route")
    timeline = rd.get("estimated_timeline_weeks", "6-12")
    dest = destination
    orig = origin

    # Quarantine sentence
    dest_reqs = rd.get("destination", {}).get("import_requirements", {})
    quarantine_text = dest_reqs.get("quarantine", "")
    has_quarantine = quarantine_text and "no routine" not in quarantine_text.lower() and "no general" not in quarantine_text.lower()
    quarantine_note = QUARANTINE_FACTS.get(dest, "")

    # Titre test sentence
    titre_raw = dest_reqs.get("titre_test", "")
    needs_titre = bool(titre_raw and titre_raw.lower() not in ["null", "not required", "none", "n/a"])

    # Build intro
    lines = []

    # Para 1 — the route and what it involves
    if complexity == "very_high":
        lines.append(f"Moving a pet from {orig} to {dest} is {complexity_text}. "
                     f"{dest} maintains strict biosecurity rules and every step in the preparation process is mandatory.")
    elif complexity == "high":
        lines.append(f"Moving a pet from {orig} to {dest} is {complexity_text}. "
                     f"The preparation involves several stages and the timeline is longer than most people expect.")
    elif complexity == "moderate":
        lines.append(f"Pet transport from {orig} to {dest} is {complexity_text}. "
                     f"The documentation is specific and there are a few stages to work through, but families who plan ahead get their pets there without major issues.")
    else:
        lines.append(f"Pet transport from {orig} to {dest} is {complexity_text}. "
                     f"The requirements are manageable with good preparation, and the timeline is relatively short compared to high-quarantine destinations.")

    # Para 2 — the key requirements
    reqs = []
    if dest_reqs.get("microchip"):
        reqs.append("a microchip (ISO 11784/11785 standard)")
    if dest_reqs.get("rabies_vaccination"):
        reqs.append("a current rabies vaccination")
    if needs_titre:
        reqs.append("a rabies titre test with a waiting period after the result")
    if dest_reqs.get("import_permit") and "no" not in dest_reqs.get("import_permit", "").lower()[:20]:
        reqs.append("an approved import permit from the destination authority")
    if dest_reqs.get("health_certificate"):
        reqs.append("a government-endorsed health certificate issued close to your travel date")

    if reqs:
        reqs_text = ", ".join(reqs[:-1])
        if len(reqs) > 1:
            reqs_text = reqs_text + ", and " + reqs[-1]
        else:
            reqs_text = reqs[-1]
        lines.append(f"At minimum, your pet needs {reqs_text}. "
                     f"Allow {timeline} weeks from starting preparation to travel day.")
    else:
        lines.append(f"Allow {timeline} weeks from starting preparation to travel day to make sure every requirement is in order.")

    # Para 3 — quarantine or reassurance
    if has_quarantine and quarantine_note:
        lines.append(quarantine_note + " Use our step-by-step guide below to track what you need to do and when.")
    else:
        lines.append(f"Use the step-by-step timeline below to plan your preparation, and get in touch if you want us to coordinate the process for you.")

    return "\n\n    ".join(lines)

def build_faqs(origin, destination, rd):
    """Generate 5 route-specific FAQs."""
    dest_reqs = rd.get("destination", {}).get("import_requirements", {})
    orig_reqs = rd.get("origin", {}).get("export_requirements", {})
    timeline = rd.get("estimated_timeline_weeks", "6-12")
    complexity = rd.get("route_complexity", "moderate")

    quarantine_text = dest_reqs.get("quarantine", "No routine quarantine")
    has_quarantine = quarantine_text and "no routine" not in quarantine_text.lower() and "no general" not in quarantine_text.lower()

    titre_raw = dest_reqs.get("titre_test", "")
    needs_titre = bool(titre_raw and titre_raw.lower() not in ["null", "not required", "none", "n/a"])

    import_permit = dest_reqs.get("import_permit", "No import permit required for personal pets.")
    microchip = dest_reqs.get("microchip", "Required (ISO 11784/11785).")
    health_cert = dest_reqs.get("health_certificate", "Required — issued by an official veterinarian close to travel date.")
    rabies = dest_reqs.get("rabies_vaccination", "Required.")

    export_permit = orig_reqs.get("export_permit", "No formal export permit required. A government-endorsed health certificate serves as export documentation.")

    faqs = []

    # FAQ 1 — How long does it take?
    if complexity == "very_high":
        time_ans = f"Allow at least {timeline} weeks — more if your pet is not yet vaccinated. The timeline is driven by mandatory waiting periods that cannot be shortened."
    elif needs_titre:
        time_ans = f"The process takes {timeline} weeks from start to finish. The rabies titre test requires a 3-6 month waiting period after the blood draw before your pet can travel, so start early."
    else:
        time_ans = f"Allow {timeline} weeks from your first vet appointment to travel day. The main variable is how quickly your pet's health certificate can be issued and endorsed."

    faqs.append({
        "question": f"How long does it take to prepare a pet for transport from {origin} to {destination}?",
        "answer": time_ans,
    })

    # FAQ 2 — Quarantine
    if has_quarantine:
        faqs.append({
            "question": f"Does my pet need to go into quarantine when entering {destination}?",
            "answer": f"Yes. {quarantine_text} Plan your trip around the quarantine period and factor in the cost, which is owner-paid.",
        })
    else:
        faqs.append({
            "question": f"Is there quarantine when my pet enters {destination}?",
            "answer": f"No routine quarantine for pets entering {destination} with the correct documentation. {quarantine_text}",
        })

    # FAQ 3 — Import permit
    faqs.append({
        "question": f"Do I need an import permit to bring my pet into {destination}?",
        "answer": import_permit,
    })

    # FAQ 4 — Health certificate
    faqs.append({
        "question": f"What health certificate does my pet need for this route?",
        "answer": f"{health_cert} Your {origin} vet must be approved to issue official veterinary certificates. The certificate must be issued within the timeframe required by {destination} — usually 10 days before travel. Present the original at check-in.",
    })

    # FAQ 5 — Titre test or microchip
    if needs_titre:
        faqs.append({
            "question": f"Is a rabies titre test required for pets entering {destination}?",
            "answer": f"Yes. {titre_raw} The microchip must be implanted before the first rabies vaccination for the vaccination to be valid. Start this process as early as possible.",
        })
    else:
        faqs.append({
            "question": f"Does my pet need a microchip to travel from {origin} to {destination}?",
            "answer": f"{microchip} The microchip must be in place before the rabies vaccination is given. If your pet was microchipped after its rabies jab, the vaccination is invalid and must be repeated.",
        })

    return faqs

def build_sideways_links(origin, destination, slug):
    """Build sideways (related routes) and upward (country guides) links."""
    sideways = []
    upward = []

    # Add links to other routes from same origin (if we know them)
    # We'll just add 2 useful fixed cross-links based on what routes exist
    orig_slug = COUNTRY_SLUGS.get(origin)
    dest_slug = COUNTRY_SLUGS.get(destination)

    if dest_slug:
        reverse_slug = f"{dest_slug}-to-{orig_slug}" if orig_slug else None
        if reverse_slug and reverse_slug != slug:
            sideways.append({
                "url": f"/pet-transport/{reverse_slug}/",
                "text": f"Pet Transport {destination} to {origin}",
            })

    if orig_slug:
        upward.append({
            "url": f"/pet-transport/origins/{orig_slug}/",
            "text": f"Shipping from {origin}",
        })
    if dest_slug:
        upward.append({
            "url": f"/pet-transport/countries/{dest_slug}/",
            "text": f"Importing to {destination}",
        })

    return sideways, upward

def fix_description(desc, origin, destination):
    """Pad a short meta description to 140-160 chars."""
    if not desc or len(desc) >= 140:
        return desc
    # Add a reassurance hook
    additions = [
        f" Expert guidance on {destination} import requirements.",
        f" Step-by-step process from {origin} to {destination}.",
        f" Avoid common mistakes with our complete {origin} to {destination} guide.",
        f" Trusted by families relocating internationally with pets.",
    ]
    for add in additions:
        candidate = desc.rstrip(".") + add
        if 140 <= len(candidate) <= 160:
            return candidate
    # Just truncate/pad to hit 140+
    base = desc.rstrip(".")
    pad = f" Complete guide: {destination} import rules, timeline, and airline options."
    return (base + pad)[:160]

def process_route_file(path):
    """Process a single route file, applying all fixes."""
    content = open(path, encoding="utf-8").read()

    # Extract YAML front matter
    m = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not m:
        return False, "no front matter"

    fm_text = m.group(1)
    body = m.group(2)

    try:
        data = yaml.safe_load(fm_text)
    except Exception as e:
        return False, f"yaml error: {e}"

    origin = data.get("origin_name", "")
    destination = data.get("destination_name", "")
    slug = data.get("slug", os.path.basename(path).replace(".md", ""))
    rd = data.get("route_data", {})

    changed = False

    # 1. Fix meta description
    desc = data.get("description", "")
    if desc and len(desc) < 140:
        new_desc = fix_description(desc, origin, destination)
        if new_desc != desc:
            fm_text = fm_text.replace(
                f'description: "{desc}"',
                f'description: "{new_desc}"',
                1,
            )
            changed = True

    # 2. Fix empty overview
    content_block = data.get("content", {}) or {}
    overview = content_block.get("overview", "") or ""
    overview = overview.strip()
    if not overview:
        new_overview = build_overview(origin, destination, rd)
        # Replace the empty overview: | block
        fm_text = re.sub(
            r'(  overview: \|\n)(    \n)?(  links:|$)',
            lambda mo: f'  overview: |\n    {new_overview}\n{mo.group(3) or ""}',
            fm_text,
            count=1,
        )
        # Simpler fallback: find 'overview: |' followed by only whitespace before next key
        if "overview: |\n    " + new_overview[:20] not in fm_text:
            fm_text = re.sub(
                r'  overview: \|(\n\s*\n)',
                f'  overview: |\n    {new_overview}\n\n',
                fm_text,
                count=1,
            )
        changed = True

    # 3. Add FAQs if missing
    has_faqs = "faqs:" in fm_text
    if not has_faqs:
        faqs = build_faqs(origin, destination, rd)
        faqs_yaml = "faqs:\n"
        for faq in faqs:
            q = faq["question"].replace('"', "'")
            a = faq["answer"].replace('"', "'")
            faqs_yaml += f'  - question: "{q}"\n'
            faqs_yaml += f'    answer: "{a}"\n'
        # Insert before `content:` block or before closing ---
        if "content:\n" in fm_text:
            fm_text = fm_text.replace("content:\n", faqs_yaml + "content:\n", 1)
        else:
            fm_text = fm_text.rstrip() + "\n" + faqs_yaml
        changed = True

    # 4. Fix sideways/upward links (fix slug/label -> url/text, or populate empty)
    links_block = data.get("links", {}) or {}
    sideways = links_block.get("sideways", []) or []
    upward = links_block.get("upward", []) or []

    # Check if they use wrong keys (slug/label) or are empty
    needs_link_fix = False
    if sideways and isinstance(sideways[0], dict) and "slug" in sideways[0]:
        needs_link_fix = True
    if upward and isinstance(upward[0], dict) and "slug" in upward[0]:
        needs_link_fix = True
    if not sideways or not upward:
        needs_link_fix = True

    if needs_link_fix:
        new_sideways, new_upward = build_sideways_links(origin, destination, slug)

        # Build the replacement links YAML block
        links_yaml = "links:\n  sideways:\n"
        for lnk in new_sideways:
            links_yaml += f'    - url: "{lnk["url"]}"\n'
            links_yaml += f'      text: "{lnk["text"]}"\n'
        links_yaml += "  upward:\n"
        for lnk in new_upward:
            links_yaml += f'    - url: "{lnk["url"]}"\n'
            links_yaml += f'      text: "{lnk["text"]}"\n'

        # Replace existing links block
        fm_text = re.sub(
            r'links:\n  sideways:.*?(\n(?=\w)|\Z)',
            links_yaml + "\n",
            fm_text,
            count=1,
            flags=re.DOTALL,
        )
        changed = True

    if changed:
        new_content = f"---\n{fm_text}\n---\n{body}"
        open(path, "w", encoding="utf-8").write(new_content)
        return True, "fixed"
    return False, "no changes needed"


def main():
    files = [
        f for f in os.listdir(ROUTES_DIR)
        if f.endswith(".md") and f != "_index.md"
    ]
    fixed = 0
    skipped = 0
    errors = 0

    for fname in sorted(files):
        path = os.path.join(ROUTES_DIR, fname)
        ok, msg = process_route_file(path)
        if ok:
            fixed += 1
        elif msg == "no changes needed":
            skipped += 1
        else:
            errors += 1
            print(f"  ERROR {fname}: {msg}")

    print(f"\nDone: {fixed} fixed, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
