"""
Phase 2 Block 21: Breed Guide Pages
Generates Hugo markdown + data JSON for:
  - 9 restricted/dangerous breeds (country ban data from breed_restrictions.json)
  - 25 brachycephalic breeds (airline restriction data from breed_restrictions.json)
Layout: site/layouts/breeds/single.html
"""
import json
import os
import re

DATA_FILE = r"c:\Users\garet\Desktop\Research\pet-transport\data\breed_restrictions.json"
DATA_OUT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\breeds"
CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\breeds"

os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(CONTENT_DIR, exist_ok=True)

with open(DATA_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

country_restrictions = raw["country_breed_restrictions"]
brachy_data = raw["airline_brachycephalic_restrictions"]
breed_matrix = {k: v for k, v in raw["common_restricted_breed_matrix"].items() if k != "description"}

COUNTRY_SLUGS = {
    "UK": "united-kingdom",
    "USA": "united-states",
    "UAE": "united-arab-emirates",
    "Australia": "australia",
    "AU": "australia",
    "Canada": "canada",
    "CA": "canada",
    "Germany": "germany",
    "DE": "germany",
    "France": "france",
    "FR": "france",
    "Singapore": "singapore",
    "SG": "singapore",
    "Hong Kong": "hong-kong",
    "HK": "hong-kong",
    "South Africa": "south-africa",
    "ZA": "south-africa",
    "New Zealand": "new-zealand",
    "NZ": "new-zealand",
    "Spain": "spain",
    "ES": "spain",
}

COUNTRY_NAMES = {
    "UK": "United Kingdom",
    "USA": "United States",
    "UAE": "United Arab Emirates",
    "AU": "Australia",
    "CA": "Canada",
    "DE": "Germany",
    "FR": "France",
    "SG": "Singapore",
    "HK": "Hong Kong",
    "ZA": "South Africa",
    "NZ": "New Zealand",
    "ES": "Spain",
}


def slugify(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name


def country_to_slug(country_code_or_name):
    """Map country code or name to a slug."""
    clean = country_code_or_name.split("(")[0].strip()
    if clean in COUNTRY_SLUGS:
        return COUNTRY_SLUGS[clean]
    return slugify(clean)


def country_code_to_name(code):
    return COUNTRY_NAMES.get(code, code)


def safestr(s):
    """Escape double quotes for YAML front matter."""
    return str(s).replace('"', "'")


# ===== RESTRICTED BREEDS =====

# Collect all breeds mentioned across all countries
all_restricted = {}
for country_code, data in country_restrictions.items():
    for item in data.get("banned_types", []):
        bn = item["name"]
        if bn not in all_restricted:
            all_restricted[bn] = {"banned": [], "restricted": [], "legislation": {}}
        all_restricted[bn]["banned"].append(country_code)
        all_restricted[bn]["legislation"][country_code] = data.get("legislation", "")
    for item in data.get("restricted_breeds", []):
        if isinstance(item, dict):
            bn = item["name"]
        else:
            bn = item
        if bn not in all_restricted:
            all_restricted[bn] = {"banned": [], "restricted": [], "legislation": {}}
        all_restricted[bn]["restricted"].append(country_code)
        all_restricted[bn]["legislation"][country_code] = data.get("legislation", "")
    for item in data.get("controlled_breeds", []):
        if isinstance(item, dict):
            bn = item["name"]
        else:
            bn = item
        if bn not in all_restricted:
            all_restricted[bn] = {"banned": [], "restricted": [], "legislation": {}}
        all_restricted[bn]["restricted"].append(country_code)
        all_restricted[bn]["legislation"][country_code] = data.get("legislation", "")

# Supplement with breed_matrix
MATRIX_DISPLAY = {
    "pit_bull_terrier": "Pit Bull Terrier",
    "rottweiler": "Rottweiler",
    "japanese_tosa": "Japanese Tosa",
    "dogo_argentino": "Dogo Argentino",
    "akita": "Akita",
    "american_staffordshire_terrier": "American Staffordshire Terrier",
}

for key, display_name in MATRIX_DISPLAY.items():
    if display_name not in all_restricted:
        matrix_entry = breed_matrix.get(key, {})
        all_restricted[display_name] = {
            "banned": matrix_entry.get("banned_from_import", []),
            "restricted": matrix_entry.get("restricted", []),
            "legislation": {},
        }


def get_airline_restrictions_for_breed(breed_name, is_brachy=False):
    """Build airline restriction list for a breed."""
    restrictions = []
    if is_brachy:
        pol = brachy_data.get("airline_policies", {})
        ban = pol.get("complete_cargo_ban", {}).get("airlines", [])
        seasonal = pol.get("seasonal_cargo_ban", {}).get("airlines", [])
        accepted = pol.get("accepted_with_restrictions", {}).get("airlines", [])
        cabin = pol.get("cabin_alternative", {}).get("airlines", [])

        for airline in ban:
            restrictions.append({
                "airline_name": airline,
                "policy": "Complete cargo ban",
                "notes": "Not accepted in cargo year-round"
            })
        for airline in seasonal:
            restrictions.append({
                "airline_name": airline,
                "policy": "Seasonal cargo embargo",
                "notes": "Not accepted in cargo during hot months (typically May-September)"
            })
        for airline in accepted[:4]:
            restrictions.append({
                "airline_name": airline,
                "policy": "Accepted with restrictions",
                "notes": "Accepted with valid fitness-to-fly certificate from vet"
            })
    return restrictions


def generate_restricted_breed_overview(breed_name, banned, restricted):
    banned_names = [country_code_to_name(b.split(" (")[0].strip()) for b in banned[:5]]
    restricted_names = [country_code_to_name(r.split(" (")[0].strip()) for r in restricted[:5]]

    lines = []
    if banned_names:
        lines.append(f"{breed_name} is banned from import into {', '.join(banned_names)}. If you are relocating with a {breed_name} to any of these countries, you cannot bring your dog with you.")
    if restricted_names:
        lines.append(f"In {', '.join(restricted_names)}, ownership is restricted. Import may be possible with permits, but conditions apply and regulations change.")
    lines.append("Breed restriction laws are based on physical characteristics in many countries, not registration or pedigree. A dog that looks like this type can be refused entry regardless of its papers.")
    lines.append("Before making any travel plans, get written confirmation from the destination country's official veterinary authority. A pet transport agent with regional knowledge is your best resource.")
    return "\n\n".join(lines)


def generate_brachycephalic_overview(breed_name):
    overview_parts = [
        f"{breed_name} is a brachycephalic (flat-faced) breed. The short skull structure compresses the airway, which creates real risks during air transport: reduced oxygen tolerance, heat stress, and difficulty breathing under the physical stress of travel.",
        "Most major international airlines impose restrictions on brachycephalic breeds. Some ban them from cargo year-round. Others apply seasonal embargoes (typically during summer months). A small number will accept them as cabin or cargo pets with a fitness-to-fly certificate from a licensed vet.",
        "If you need to fly your dog internationally, the airline policy is one constraint. The destination country's import rules are another entirely. Both apply.",
        "Check the current airline policy directly before booking. Policies change and online guides can be out of date. This page reflects the most recently verified information, but confirmation from the airline is essential."
    ]
    return "\n\n".join(overview_parts)


def generate_restricted_breed_faqs(breed_name, banned, restricted):
    faqs = []

    banned_names = [country_code_to_name(b.split(" (")[0].strip()) for b in banned[:4]]
    restricted_names = [country_code_to_name(r.split(" (")[0].strip()) for r in restricted[:3]]

    if banned_names:
        faqs.append({
            "question": f"Which countries ban {breed_name} import?",
            "answer": f"{', '.join(banned_names)} do not allow {breed_name} import. In these countries, the breed cannot be brought in from abroad. This is not a documentation issue that can be resolved with extra paperwork."
        })

    if restricted_names:
        faqs.append({
            "question": f"Can I relocate with a {breed_name} to {restricted_names[0]}?",
            "answer": f"{restricted_names[0]} restricts but does not fully ban {breed_name} ownership. Import may be possible under specific conditions. Contact the destination country's official veterinary import authority directly to get current requirements in writing before making plans."
        })

    faqs.append({
        "question": f"My {breed_name} is a registered pedigree. Does that mean it isn't subject to the ban?",
        "answer": "Not necessarily. Many countries operate type-based bans, not pedigree-based ones. If your dog substantially conforms to the physical characteristics of the banned type, it can be refused regardless of registration papers. This is how the UK's Dangerous Dogs Act operates, for example. Do not assume your dog is exempt without checking the specific legal test applied in your destination country."
    })

    faqs.append({
        "question": f"Are mixed-breed dogs with some {breed_name} ancestry affected?",
        "answer": "In most countries with breed-specific legislation, yes. If a dog visually resembles a banned type, it is treated as that type. There is no exemption for being part of a different breed. A vet or legal specialist in the destination country can give you the most accurate assessment."
    })

    faqs.append({
        "question": f"Which airlines will transport a {breed_name}?",
        "answer": "Breed-specific legislation does not apply to airlines directly. However, country import laws mean some airlines will refuse to transport restricted breeds to destinations where they would be refused entry. Your options depend on the origin and destination country. A pet transport agent familiar with your route can advise on current airline acceptance."
    })

    return faqs


def generate_brachycephalic_faqs(breed_name):
    faqs = []

    faqs.append({
        "question": f"Can I fly my {breed_name} in the cabin?",
        "answer": f"Some airlines allow small brachycephalic breeds in the cabin if they meet the weight and size limits for under-seat carriers. The risk in the cabin is generally lower than cargo because the environment is more controlled. Check each airline's current cabin policy for brachycephalic breeds. Rules vary by airline and route."
    })

    faqs.append({
        "question": f"Which airlines will accept a {breed_name} as cargo?",
        "answer": f"British Airways, Virgin Atlantic, and Singapore Airlines do not accept brachycephalic breeds in cargo year-round. Other airlines apply seasonal embargoes during hot months. Emirates, Lufthansa, and Air France may accept flat-faced breeds with a vet-issued fitness-to-fly certificate, subject to route and season. Always verify with the airline before booking."
    })

    faqs.append({
        "question": f"What is a fitness-to-fly certificate for a {breed_name}?",
        "answer": f"A fitness-to-fly certificate is a written assessment from a licensed veterinarian confirming that your dog is in good enough health to withstand air transport. For brachycephalic breeds, the vet must specifically assess airway health. Some airlines require pre-approval from their veterinary team in addition to the certificate. The certificate does not guarantee acceptance: the airline makes the final call."
    })

    faqs.append({
        "question": f"Are there countries that will not accept a {breed_name}?",
        "answer": f"{breed_name} is not subject to specific country breed bans as a brachycephalic breed. The restrictions you'll face are from airlines, not destination governments. However, always check the destination country's current import rules for any specific breed-related notes."
    })

    faqs.append({
        "question": f"What's the safest way to fly a {breed_name} internationally?",
        "answer": f"If the route allows it, a small {breed_name} travelling as a cabin pet in an under-seat carrier faces fewer risks than cargo. Avoid peak summer travel if possible. Choose a direct flight over connections. Use a vet who specialises in brachycephalic breeds to assess your dog's fitness before booking. Work with a pet transport agent who knows which airlines are currently accepting flat-faced breeds on your specific route."
    })

    return faqs


print("Generating restricted breed pages...\n")

restricted_count = 0
for breed_name, data in all_restricted.items():
    slug = slugify(breed_name)
    banned = data.get("banned", [])
    restricted = data.get("restricted", [])

    banned_countries = []
    for b in banned:
        clean = b.split(" (")[0].strip()
        banned_countries.append({
            "slug": country_to_slug(clean),
            "name": country_code_to_name(clean),
            "restriction_type": "banned"
        })

    restricted_countries = []
    for r in restricted:
        clean = r.split(" (")[0].strip()
        if clean not in [b.split(" (")[0].strip() for b in banned]:
            restricted_countries.append({
                "slug": country_to_slug(clean),
                "name": country_code_to_name(clean),
                "restriction_type": "restricted"
            })

    overview = generate_restricted_breed_overview(breed_name, banned, restricted)
    faqs = generate_restricted_breed_faqs(breed_name, banned, restricted)

    page_data = {
        "breed_name": breed_name,
        "slug": slug,
        "breed_type": "restricted",
        "brachycephalic": False,
        "banned_countries": banned_countries,
        "restricted_countries": restricted_countries,
        "airline_restrictions": get_airline_restrictions_for_breed(breed_name, False),
        "content": {
            "h1": f"{breed_name} International Travel Restrictions",
            "overview": overview,
            "sections": [],
        },
        "faqs": faqs,
        "seo": {
            "title": f"{breed_name} Import Restrictions by Country | Pet Transport Global",
            "description": f"Which countries ban or restrict {breed_name} import, and what it means for international relocation. Country-by-country breakdown with current regulations.",
        },
    }

    # Save data JSON
    with open(os.path.join(DATA_OUT_DIR, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)

    # Create markdown
    md = f"""---
title: "{safestr(page_data['seo']['title'])}"
description: "{safestr(page_data['seo']['description'])}"
type: "breeds"
layout: "single"
slug: "{slug}"
breed_name: "{safestr(breed_name)}"
brachycephalic: false
banned_countries:
"""
    for bc in banned_countries:
        md += f'  - slug: "{bc["slug"]}"\n'
        md += f'    name: "{safestr(bc["name"])}"\n'
        md += f'    restriction_type: "banned"\n'
    md += "restricted_countries:\n"
    for rc in restricted_countries:
        md += f'  - slug: "{rc["slug"]}"\n'
        md += f'    name: "{safestr(rc["name"])}"\n'
        md += f'    restriction_type: "restricted"\n'
    md += "airline_restrictions: []\n"
    md += "content:\n"
    md += f'  h1: "{safestr(page_data["content"]["h1"])}"\n'
    md += "  overview: |\n"
    for line in overview.splitlines():
        md += f"    {line}\n"
    md += "faqs:\n"
    for faq in faqs:
        md += f'  - question: "{safestr(faq["question"])}"\n'
        md += f'    answer: "{safestr(faq["answer"])}"\n'
    md += "---\n"

    with open(os.path.join(CONTENT_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  {slug}.md  ({breed_name}) — banned: {[b.split(' (')[0].strip() for b in banned[:3]]}")
    restricted_count += 1

# ===== BRACHYCEPHALIC BREEDS =====

brachy_dogs = brachy_data.get("universally_affected_dog_breeds", [])
brachy_cats = brachy_data.get("universally_affected_cat_breeds", [])
all_brachy = [(b, "dog") for b in brachy_dogs] + [(b, "cat") for b in brachy_cats]

print(f"\nGenerating brachycephalic breed pages ({len(all_brachy)} breeds)...\n")

# Get airline policy data for brachy
brachy_pol = brachy_data.get("airline_policies", {})
banned_airlines = brachy_pol.get("complete_cargo_ban", {}).get("airlines", [])
seasonal_airlines = brachy_pol.get("seasonal_cargo_ban", {}).get("airlines", [])
accepted_airlines = brachy_pol.get("accepted_with_restrictions", {}).get("airlines", [])

airline_restrictions_brachy = []
for airline in banned_airlines:
    airline_restrictions_brachy.append({
        "airline_name": airline,
        "policy": "Complete cargo ban",
        "notes": "Not accepted in cargo year-round"
    })
for airline in seasonal_airlines:
    airline_restrictions_brachy.append({
        "airline_name": airline,
        "policy": "Seasonal cargo embargo",
        "notes": "Not accepted in cargo during peak summer months"
    })
for airline in accepted_airlines[:4]:
    airline_restrictions_brachy.append({
        "airline_name": airline,
        "policy": "Accepted with vet clearance",
        "notes": "Fitness-to-fly certificate required from licensed vet"
    })

brachy_count = 0
for breed_name, species in all_brachy:
    slug = slugify(breed_name)
    overview = generate_brachycephalic_overview(breed_name)
    faqs = generate_brachycephalic_faqs(breed_name)

    page_data = {
        "breed_name": breed_name,
        "slug": slug,
        "breed_type": "brachycephalic",
        "species": species,
        "brachycephalic": True,
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": airline_restrictions_brachy,
        "content": {
            "h1": f"{breed_name} Air Travel Guide",
            "overview": overview,
            "sections": [],
        },
        "faqs": faqs,
        "seo": {
            "title": f"Flying with a {breed_name} | Airline Restrictions & Advice",
            "description": f"Which airlines accept {breed_name} as cargo or cabin? Seasonal embargoes, breed bans, and what you need before booking your flat-faced {species}.",
        },
    }

    # Save data JSON
    with open(os.path.join(DATA_OUT_DIR, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)

    # Create markdown
    md = f"""---
title: "{safestr(page_data['seo']['title'])}"
description: "{safestr(page_data['seo']['description'])}"
type: "breeds"
layout: "single"
slug: "{slug}"
breed_name: "{safestr(breed_name)}"
brachycephalic: true
species: "{species}"
banned_countries: []
restricted_countries: []
airline_restrictions:
"""
    for ar in airline_restrictions_brachy:
        md += f'  - airline_name: "{safestr(ar["airline_name"])}"\n'
        md += f'    policy: "{safestr(ar["policy"])}"\n'
        md += f'    notes: "{safestr(ar["notes"])}"\n'
    md += "content:\n"
    md += f'  h1: "{safestr(page_data["content"]["h1"])}"\n'
    md += "  overview: |\n"
    for line in overview.splitlines():
        md += f"    {line}\n"
    md += "faqs:\n"
    for faq in faqs:
        md += f'  - question: "{safestr(faq["question"])}"\n'
        md += f'    answer: "{safestr(faq["answer"])}"\n'
    md += "---\n"

    with open(os.path.join(CONTENT_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  {slug}.md  ({breed_name} / {species})")
    brachy_count += 1

total = restricted_count + brachy_count
print(f"\nDone. {restricted_count} restricted breed pages + {brachy_count} brachycephalic breed pages = {total} breed pages.")
