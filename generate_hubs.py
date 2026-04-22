"""
Block 16: Country Guides + Origin Hubs
Generates 10 country guide pages (destination-focused) and 10 origin hub pages (departure-focused).
Also creates data files for Hugo to consume.
"""
import json
import os
import random

DATA_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\data"
SITE_DATA = r"c:\Users\garet\Desktop\Research\pet-transport\site\data"
CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content"
ROUTES_DATA = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"

with open(os.path.join(DATA_DIR, "countries_pet_regulations.json"), "r", encoding="utf-8") as f:
    countries_raw = json.load(f)

with open(os.path.join(DATA_DIR, "airline_pet_policies.json"), "r", encoding="utf-8") as f:
    airlines_raw = json.load(f)

with open(os.path.join(DATA_DIR, "breed_restrictions.json"), "r", encoding="utf-8") as f:
    breeds_raw = json.load(f)

COUNTRY_MAP = {
    "UK": {"code": "GB", "name": "United Kingdom", "slug": "united-kingdom"},
    "USA": {"code": "US", "name": "United States", "slug": "united-states"},
    "UAE": {"code": "AE", "name": "United Arab Emirates", "slug": "united-arab-emirates"},
    "Australia": {"code": "AU", "name": "Australia", "slug": "australia"},
    "Canada": {"code": "CA", "name": "Canada", "slug": "canada"},
    "Germany": {"code": "DE", "name": "Germany", "slug": "germany"},
    "France": {"code": "FR", "name": "France", "slug": "france"},
    "Singapore": {"code": "SG", "name": "Singapore", "slug": "singapore"},
    "Hong_Kong": {"code": "HK", "name": "Hong Kong", "slug": "hong-kong"},
    "South_Africa": {"code": "ZA", "name": "South Africa", "slug": "south-africa"},
}

# Find which routes exist for each country
def get_existing_routes():
    """Scan route data files to find inbound/outbound routes per country."""
    routes = {}
    if not os.path.exists(ROUTES_DATA):
        return routes

    for f in os.listdir(ROUTES_DATA):
        if not f.endswith(".json"):
            continue
        with open(os.path.join(ROUTES_DATA, f), "r", encoding="utf-8") as fp:
            data = json.load(fp)
        rd = data.get("route_data", {})
        origin_code = rd.get("origin", {}).get("code", "")
        dest_code = rd.get("destination", {}).get("code", "")
        slug = f.replace(".json", "")

        for code in [origin_code, dest_code]:
            if code not in routes:
                routes[code] = {"inbound": [], "outbound": []}

        if origin_code:
            routes[origin_code]["outbound"].append({
                "slug": slug,
                "destination": data.get("destination_name", ""),
                "destination_code": dest_code,
                "complexity": rd.get("route_complexity", "moderate"),
            })
        if dest_code:
            routes[dest_code]["inbound"].append({
                "slug": slug,
                "origin": data.get("origin_name", ""),
                "origin_code": origin_code,
                "complexity": rd.get("route_complexity", "moderate"),
            })

    return routes


def flatten_import_requirements(reqs):
    """Flatten import requirements to simple key-value for display."""
    result = {}
    fields = ["microchip", "rabies_vaccination", "rabies_titre_test", "quarantine",
              "import_permit", "health_certificate", "tapeworm_treatment", "banned_breeds"]

    for field in fields:
        val = reqs.get(field, {})
        if isinstance(val, dict):
            # Extract most useful info
            if field == "microchip":
                parts = []
                if val.get("required"):
                    parts.append(f"Required ({val.get('standard', 'ISO 11784/11785')})")
                if val.get("timing"):
                    parts.append(val["timing"])
                result[field] = ". ".join(parts) if parts else "Check requirements"

            elif field == "rabies_vaccination":
                parts = []
                if val.get("required"):
                    parts.append("Required")
                if val.get("wait_after_first_vaccination_days"):
                    parts.append(f"{val['wait_after_first_vaccination_days']}-day wait after first vaccination")
                result[field] = ". ".join(parts) if parts else "Required"

            elif field == "rabies_titre_test":
                if val.get("required") is True:
                    result[field] = f"Required. Minimum {val.get('minimum_result', '0.5 IU/ml')}. {val.get('wait_after_test_days', 90)}-day wait."
                elif val.get("required_for"):
                    result[field] = f"Required for: {val['required_for']}"
                elif val.get("not_required_for"):
                    result[field] = f"Not required for: {val['not_required_for']}"

            elif field == "quarantine":
                if val.get("required") is True or val.get("mandatory") is True:
                    dur = val.get("duration_days") or val.get("minimum_days", "varies")
                    fac = val.get("facility", {})
                    fac_name = fac.get("name", str(fac)) if isinstance(fac, dict) else str(fac)
                    result[field] = f"Mandatory. {dur} days. Facility: {fac_name}"
                elif val.get("required") is False:
                    result[field] = "Not required (penalty quarantine if non-compliant)"

            elif field == "import_permit":
                if val.get("required") is True:
                    result[field] = "Required. " + val.get("notes", "")
                else:
                    result[field] = val.get("alternative", val.get("notes", "Not required"))

            elif field == "health_certificate":
                result[field] = val.get("name", "Required") + ". Valid " + str(val.get("valid_for_entry_days", 10)) + " days."

            elif field == "tapeworm_treatment":
                if val.get("required_for"):
                    result[field] = f"Required for {val['required_for']}. Timing: {val.get('timing', '24-120 hours before arrival')}."

            elif field == "banned_breeds":
                breeds = val.get("banned_types", [])
                if breeds:
                    names = [b if isinstance(b, str) else b.get("name", str(b)) for b in breeds]
                    result[field] = ", ".join(names)
        elif val:
            result[field] = str(val)

    return result


def get_country_airlines(country_code):
    """Find airlines that serve this country."""
    name = next((v["name"] for v in COUNTRY_MAP.values() if v["code"] == country_code), "")
    search_terms = [name.lower(), country_code.lower()]

    city_map = {
        "GB": ["london", "heathrow", "uk"],
        "AU": ["sydney", "melbourne"],
        "AE": ["dubai", "abu dhabi"],
        "US": ["new york", "los angeles"],
        "HK": ["hong kong"],
        "FR": ["paris"],
        "SG": ["singapore"],
        "DE": ["frankfurt", "munich"],
        "CA": ["toronto", "vancouver"],
        "ZA": ["johannesburg"],
    }
    search_terms.extend(city_map.get(country_code, []))

    matched = []
    for key, airline in airlines_raw.get("airlines", {}).items():
        routes = " ".join(str(r).lower() for r in airline.get("key_routes_p1", []))
        hub = str(airline.get("hub", "")).lower()

        if any(t in routes or t in hub for t in search_terms):
            cargo = airline.get("cargo_policy", {})
            cabin = airline.get("cabin_policy", {})
            if cargo.get("allowed") and cabin.get("allowed"):
                atype = "cabin_and_cargo"
            elif cargo.get("allowed"):
                atype = "cargo_only"
            elif cabin.get("allowed"):
                atype = "cabin_only"
            else:
                atype = "check"
            matched.append({
                "name": airline.get("name", key),
                "type": atype,
            })

    return matched


def generate_country_guide(country_key, country_info):
    """Generate country guide content (destination-focused)."""
    data = countries_raw["countries"].get(country_key, {})
    code = country_info["code"]
    name = country_info["name"]
    slug = country_info["slug"]

    import_reqs = flatten_import_requirements(data.get("import_requirements", {}))
    routes = existing_routes.get(code, {"inbound": [], "outbound": []})

    friendliness = data.get("pet_friendliness", "moderate")
    friendliness_text = {
        "easy": "relatively straightforward",
        "moderate": "moderately strict",
        "strict": "strict",
        "very-strict": "very strict",
    }.get(friendliness, "moderate")

    # Build overview
    overview = f"Importing a pet to {name} is {friendliness_text}. "
    if "quarantine" in import_reqs and "mandatory" in import_reqs.get("quarantine", "").lower():
        overview += f"One of the biggest factors is the mandatory quarantine requirement. "
    if import_reqs.get("banned_breeds"):
        overview += f"{name} also bans certain breeds from entry. "
    overview += "Here's what you need to know."

    # Build sections
    sections = []

    # Import requirements overview
    req_parts = []
    for key, val in import_reqs.items():
        if key != "banned_breeds" and val:
            label = key.replace("_", " ").title()
            req_parts.append(f"**{label}:** {val}")
    sections.append({
        "heading": f"Import requirements for {name}",
        "body": "\n\n".join(req_parts) if req_parts else "Check with authorities for current requirements.",
    })

    # Breed restrictions
    breed_data = breeds_raw.get("country_breed_restrictions", {}).get(country_key, {})
    if breed_data:
        breed_parts = []
        legislation = breed_data.get("legislation", "")
        if legislation:
            breed_parts.append(f"Governed by: {legislation}")
        for bt in breed_data.get("banned_types", []):
            if isinstance(bt, dict):
                breed_parts.append(f"- {bt.get('name', '')}: {bt.get('status', 'restricted')}")
            else:
                breed_parts.append(f"- {bt}")
        if breed_parts:
            sections.append({
                "heading": f"Breed restrictions in {name}",
                "body": "\n\n".join(breed_parts),
            })

    # Routes to this country
    if routes["inbound"]:
        route_links = []
        for r in routes["inbound"]:
            route_links.append(f"- [{r['origin']} to {name}](/routes/{r['slug']}/)")
        sections.append({
            "heading": f"Routes to {name}",
            "body": "We have detailed guides for the following routes:\n\n" + "\n".join(route_links),
        })

    # FAQs
    faqs = [
        {
            "question": f"What vaccinations does my pet need to enter {name}?",
            "answer": f"At minimum, a rabies vaccination is required. {import_reqs.get('rabies_vaccination', 'Check specific requirements.')} Your pet must also be microchipped before vaccination."
        },
        {
            "question": f"Is there quarantine in {name}?",
            "answer": import_reqs.get("quarantine", f"Check with {name}'s authorities for current quarantine policy.")
        },
        {
            "question": f"Which airlines fly pets to {name}?",
            "answer": "Multiple airlines serve pet cargo to " + name + ". Check our route-specific guides for airline details on your particular origin-destination pair."
        },
    ]

    return {
        "title": f"Pet Import Guide: {name}",
        "description": f"Complete guide to importing your dog or cat to {name}. Import requirements, quarantine, breed restrictions, and step-by-step process.",
        "name": name,
        "code": code,
        "slug": slug,
        "pet_friendliness": friendliness,
        "overview": overview,
        "import_requirements": import_reqs,
        "sections": sections,
        "faqs": faqs,
        "airlines": get_country_airlines(code),
        "inbound_routes": routes["inbound"],
    }


def generate_origin_hub(country_key, country_info):
    """Generate origin hub content (departure-focused)."""
    data = countries_raw["countries"].get(country_key, {})
    code = country_info["code"]
    name = country_info["name"]
    slug = country_info["slug"]

    export_reqs = data.get("export_requirements", {})
    routes = existing_routes.get(code, {"inbound": [], "outbound": []})

    # Build overview
    overview = f"Shipping your pet from {name} requires the right paperwork and planning. "
    if routes["outbound"]:
        overview += f"We cover {len(routes['outbound'])} routes from {name} in detail. "
    overview += "Here's what you need to arrange before your pet can leave."

    # Export requirements
    export_flat = {}
    for key, val in export_reqs.items():
        if isinstance(val, dict):
            notes = val.get("notes", val.get("description", ""))
            if notes:
                export_flat[key] = str(notes)
            else:
                # Try to extract from sub-keys
                for sub_key, sub_val in val.items():
                    if isinstance(sub_val, str):
                        export_flat[f"{key}_{sub_key}"] = sub_val
                    elif isinstance(sub_val, dict) and sub_val.get("notes"):
                        export_flat[f"{key}_{sub_key}"] = sub_val["notes"]
        elif isinstance(val, str):
            export_flat[key] = val

    # Sections
    sections = []

    # Export process
    if export_flat:
        req_parts = []
        for key, val in export_flat.items():
            label = key.replace("_", " ").title()
            req_parts.append(f"**{label}:** {val}")
        sections.append({
            "heading": f"Export requirements from {name}",
            "body": "\n\n".join(req_parts),
        })

    # Routes from this country
    if routes["outbound"]:
        route_links = []
        for r in routes["outbound"]:
            route_links.append(f"- [{name} to {r['destination']}](/routes/{r['slug']}/)")
        sections.append({
            "heading": f"Popular routes from {name}",
            "body": "We have detailed guides for the following routes:\n\n" + "\n".join(route_links),
        })

    # FAQs
    faqs = [
        {
            "question": f"What do I need to export my pet from {name}?",
            "answer": f"You'll need a health certificate from an official veterinarian, proof of microchip and vaccinations, and any government endorsement required by your destination country. " + (list(export_flat.values())[0] if export_flat else f"Check with {name}'s veterinary authority.")
        },
        {
            "question": f"Where can I get a pet health certificate in {name}?",
            "answer": f"Any government-approved veterinarian in {name} can issue a health certificate for pet export. For some destinations, the certificate then needs endorsement from the national veterinary authority."
        },
    ]

    return {
        "title": f"Pet Export Guide: Shipping from {name}",
        "description": f"Guide to exporting your dog or cat from {name}. Export requirements, airlines, and routes.",
        "name": name,
        "code": code,
        "slug": slug,
        "overview": overview,
        "export_requirements": export_flat,
        "sections": sections,
        "faqs": faqs,
        "airlines": get_country_airlines(code),
        "outbound_routes": routes["outbound"],
    }


def write_country_content(guide, content_type):
    """Write Hugo content markdown for country guide or origin hub."""
    section = "countries" if content_type == "guide" else "origins"
    content_path = os.path.join(CONTENT_DIR, section, f"{guide['slug']}.md")

    md = f"""---
title: "{guide['title']}"
description: "{guide['description']}"
type: "{section}"
layout: "single"
country_name: "{guide['name']}"
country_code: "{guide['code']}"
"""

    if content_type == "guide":
        md += f'pet_friendliness: "{guide.get("pet_friendliness", "moderate")}"\n'

    md += f"""overview: |
  {guide['overview']}
"""

    # Sections
    if guide.get("sections"):
        md += "sections:\n"
        for sec in guide["sections"]:
            safe_heading = sec["heading"].replace('"', '\\"')
            md += f'  - heading: "{safe_heading}"\n'
            md += f'    body: |\n'
            for line in sec["body"].split("\n"):
                md += f'      {line}\n'

    # FAQs
    if guide.get("faqs"):
        md += "faqs:\n"
        for faq in guide["faqs"]:
            safe_q = faq["question"].replace('"', '\\"')
            safe_a = faq["answer"].replace('"', '\\"')
            md += f'  - question: "{safe_q}"\n'
            md += f'    answer: "{safe_a}"\n'

    # Airlines
    if guide.get("airlines"):
        md += "airlines:\n"
        for a in guide["airlines"]:
            md += f'  - name: "{a["name"]}"\n'
            md += f'    type: "{a["type"]}"\n'

    # Routes
    route_key = "inbound_routes" if content_type == "guide" else "outbound_routes"
    if guide.get(route_key):
        md += f"{route_key}:\n"
        for r in guide[route_key]:
            md += f'  - slug: "{r["slug"]}"\n'
            if "origin" in r:
                md += f'    origin: "{r["origin"]}"\n'
            if "destination" in r:
                md += f'    destination: "{r["destination"]}"\n'

    md += "---\n"

    os.makedirs(os.path.dirname(content_path), exist_ok=True)
    with open(content_path, "w", encoding="utf-8") as f:
        f.write(md)

    return content_path


# === MAIN ===
existing_routes = get_existing_routes()

# Also write data files for Hugo data directory
os.makedirs(os.path.join(SITE_DATA, "countries"), exist_ok=True)

print("Generating 10 country guides + 10 origin hubs...\n")

for country_key, country_info in COUNTRY_MAP.items():
    # Country guide (destination-focused)
    guide = generate_country_guide(country_key, country_info)
    path = write_country_content(guide, "guide")
    print(f"  Country guide: {country_info['slug']}.md ({len(guide.get('sections', []))} sections, {len(guide.get('faqs', []))} FAQs)")

    # Also save as data file for Hugo
    data_path = os.path.join(SITE_DATA, "countries", f"{country_info['slug']}.json")
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(guide, f, indent=2, ensure_ascii=False)

    # Origin hub (departure-focused)
    hub = generate_origin_hub(country_key, country_info)
    path = write_country_content(hub, "origin")
    print(f"  Origin hub:    {country_info['slug']}.md ({len(hub.get('sections', []))} sections, {len(hub.get('faqs', []))} FAQs)")

print(f"\nDone. 10 country guides + 10 origin hubs created.")
print(f"Content: {CONTENT_DIR}/countries/ and {CONTENT_DIR}/origins/")
print(f"Data: {SITE_DATA}/countries/")
