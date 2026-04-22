"""
Phase 2 Block 20: Airline Guide Pages
Generates data JSON + Hugo markdown content for each airline in airline_pet_policies.json.
Layout: site/layouts/airlines/single.html
"""
import json
import os
import re

DATA_FILE = r"c:\Users\garet\Desktop\Research\pet-transport\data\airline_pet_policies.json"
DATA_OUT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\airlines"
CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\airlines"

os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(CONTENT_DIR, exist_ok=True)

with open(DATA_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

airlines = raw.get("airlines", {})


def slugify(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name


def build_cabin_summary(cabin):
    if not cabin.get("allowed"):
        note = cabin.get("note", "Pets are not accepted in the passenger cabin.")
        exception = cabin.get("exception", "")
        if exception:
            return f"{note} Exception: {exception}"
        return note
    parts = []
    weight = cabin.get("max_weight_kg") or cabin.get("combined_weight_limit")
    if weight:
        parts.append(f"Pets up to {weight}kg (including carrier) allowed in cabin.")
    else:
        parts.append("Small pets allowed in the cabin.")
    if cabin.get("carrier_requirements"):
        parts.append(cabin["carrier_requirements"])
    if cabin.get("restrictions"):
        for r in cabin["restrictions"][:2]:
            parts.append(str(r))
    return " ".join(parts)


def build_cargo_summary(cargo):
    if not cargo.get("allowed"):
        return "Cargo pet transport is not available on this airline."
    parts = []
    if cargo.get("service"):
        parts.append(f"Service: {cargo['service']}.")
    elif cargo.get("service_from_uk"):
        parts.append(f"UK exports: {cargo['service_from_uk']}.")
    if cargo.get("species"):
        parts.append(f"Accepted: {cargo['species']}.")
    if cargo.get("restrictions"):
        for r in cargo["restrictions"][:3]:
            parts.append(str(r))
    if cargo.get("lead_time"):
        parts.append(f"Book at least {cargo['lead_time']} in advance.")
    return " ".join(parts)


def build_policy_section(airline_data):
    cabin = airline_data.get("cabin_policy", {})
    cargo = airline_data.get("cargo_policy", {})

    accepted_animals = cargo.get("species") or "Dogs and cats (subject to route restrictions)"
    crate_req = "IATA-compliant rigid container. Pet must be able to stand, sit upright, lie down, and turn around."
    size_limits = cargo.get("size_limits") or cabin.get("max_weight_kg")
    if size_limits and not isinstance(size_limits, str):
        size_limits = f"Cabin: max {size_limits}kg including carrier. Cargo: by crate dimensions."
    elif not size_limits:
        size_limits = "Varies by route and aircraft. Contact cargo desk for current limits."

    # Brachycephalic policy
    brachy = None
    for r in cargo.get("restrictions", []):
        if "brachycephalic" in str(r).lower() or "snub" in str(r).lower() or "flat" in str(r).lower():
            brachy = str(r)
            break
    if not brachy:
        brachy = "Flat-faced breeds may face seasonal restrictions or year-round embargoes. Verify current policy before booking."

    # Temperature
    temp = None
    for r in cargo.get("restrictions", []):
        if "temperature" in str(r).lower() or "embargo" in str(r).lower() or "heat" in str(r).lower():
            temp = str(r)
            break
    if not temp:
        temp = "Temperature embargoes may apply during extreme weather. Confirm with the airline at time of booking."

    # Cost
    fees_raw = airline_data.get("fees", "")
    if isinstance(fees_raw, dict):
        parts = []
        for k, v in fees_raw.items():
            parts.append(f"{k}: {v}")
        fees = ". ".join(parts) + "." if parts else "Fees vary by route. Contact the airline for a quote."
    elif fees_raw:
        fees = str(fees_raw)
    else:
        fees = "Fees vary by route, pet weight, and crate size. Contact the airline cargo desk or your pet transport agent for a quote."

    # Booking
    booking = cargo.get("booking") or "Contact the airline's cargo department directly or book through an IPATA-accredited pet transport agent."

    return {
        "accepted_animals": accepted_animals,
        "crate_requirements": crate_req,
        "size_limits": size_limits,
        "temperature_restrictions": temp,
        "brachycephalic_policy": brachy,
        "cost_range": fees,
        "booking_process": booking,
    }


def generate_overview(airline_data, name):
    cabin = airline_data.get("cabin_policy", {})
    cargo = airline_data.get("cargo_policy", {})
    hub = airline_data.get("hub", "")
    routes = airline_data.get("key_routes_p1", [])

    cabin_allowed = cabin.get("allowed", False)
    cargo_allowed = cargo.get("allowed", True)

    if cabin_allowed and cargo_allowed:
        transport_summary = f"{name} accepts small pets in the cabin and larger animals as cargo."
    elif cabin_allowed:
        transport_summary = f"{name} allows small pets in the passenger cabin but does not offer a general cargo pet service."
    elif cargo_allowed:
        transport_summary = f"{name} does not allow pets in the passenger cabin. All pets travel as manifested cargo in temperature-controlled holds."
    else:
        transport_summary = f"{name} has limited pet transport options. Check current policy before booking."

    overview = transport_summary

    if hub:
        overview += f" The airline is based in {hub}."

    key = airline_data.get("key_consideration", "")
    if key:
        overview += f"\n\n{key}"

    overview += "\n\nThis page covers the current pet transport policy, breed restrictions, temperature embargoes, and how to book. Policies change, so always confirm with the airline before making firm plans."

    return overview


def generate_faqs(airline_data, name, slug):
    cabin = airline_data.get("cabin_policy", {})
    cargo = airline_data.get("cargo_policy", {})

    faqs = []

    # Can I bring my dog in the cabin?
    if cabin.get("allowed"):
        weight = cabin.get("max_weight_kg") or "8"
        faqs.append({
            "question": f"Can I bring my dog in the cabin on {name}?",
            "answer": f"Yes, for small dogs. {name} allows pets in the cabin up to around {weight}kg including the carrier. The carrier must fit under the seat in front of you. Check the current weight and size limits when booking, as these change."
        })
    else:
        note = cabin.get("note", f"{name} does not allow pets in the passenger cabin.")
        faqs.append({
            "question": f"Can I bring my pet in the cabin on {name}?",
            "answer": note
        })

    # How do I book pet cargo?
    booking = cargo.get("booking") or "Contact the airline cargo desk directly, or use an IPATA-accredited pet transport agent."
    faqs.append({
        "question": f"How do I book pet cargo on {name}?",
        "answer": f"{booking} Book as early as possible. Space for live animals is limited, and airlines often have only a few slots per flight. Confirm the booking 48-72 hours before departure."
    })

    # Brachycephalic
    brachy_note = None
    for r in cargo.get("restrictions", []):
        if "brachycephalic" in str(r).lower() or "snub" in str(r).lower():
            brachy_note = str(r)
            break
    if not brachy_note:
        brachy_note = f"{name} imposes restrictions on brachycephalic (flat-faced) breeds. Policies vary by season and route."
    faqs.append({
        "question": f"Does {name} accept French Bulldogs or Pugs as cargo?",
        "answer": f"{brachy_note} Always check the current policy for your specific route and travel dates. Some airlines allow flat-faced breeds with a vet certificate confirming fitness to fly."
    })

    # What documents are needed?
    faqs.append({
        "question": f"What documents does my pet need to fly with {name}?",
        "answer": "At minimum: a valid veterinary health certificate (usually issued within 10 days of travel), proof of microchip (ISO 11784/11785 standard), and up-to-date vaccination records. Import-specific documents depend on the destination country. Some routes require rabies titre test results, import permits, or government endorsement of the health certificate. Your destination country's requirements apply regardless of which airline you use."
    })

    # Crate
    faqs.append({
        "question": f"What crate does my pet need for {name} cargo?",
        "answer": "All airlines require IATA-compliant rigid crates for cargo pet transport. The crate must allow your pet to stand, sit upright, lie down, and turn around without touching the sides or top. It must have ventilation on at least three sides, a water container, and live animal labels. Soft-sided carriers are not accepted for cargo. For cabin travel, the carrier must fit under the seat in front of you."
    })

    return faqs


def build_routes_served(airline_data, name):
    routes_raw = airline_data.get("key_routes_p1", [])
    return [{"description": str(r)} for r in routes_raw[:8]]


# Create section _index.md
with open(os.path.join(CONTENT_DIR, "_index.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: "Airline Pet Transport Policies"
description: "Pet cargo and cabin policies for major international airlines. Find out which airlines accept pets, breed restrictions, crate requirements, and how to book."
---
""")

print(f"Processing {len(airlines)} airlines...\n")

for key, airline_data in airlines.items():
    name = airline_data.get("name", key.replace("_", " ").title())
    slug = slugify(name)

    cabin = airline_data.get("cabin_policy", {})
    cargo = airline_data.get("cargo_policy", {})

    cabin_allowed = cabin.get("allowed", False)
    cargo_allowed = cargo.get("allowed", True)
    cargo_suspended = not cargo_allowed

    page_data = {
        "airline_name": name,
        "slug": slug,
        "hub": airline_data.get("hub", ""),
        "alliance": airline_data.get("alliance", ""),
        "cabin_allowed": cabin_allowed,
        "cargo_allowed": cargo_allowed,
        "cargo_suspended": cargo_suspended,
        "policy": build_policy_section(airline_data),
        "routes_served": build_routes_served(airline_data, name),
        "content": {
            "h1": f"{name} Pet Transport Policy",
            "overview": generate_overview(airline_data, name),
            "sections": [],
        },
        "faqs": generate_faqs(airline_data, name, slug),
        "seo": {
            "title": f"{name} Pet Cargo Policy | Pet Transport Global",
            "description": f"{name} pet transport policy: cabin rules, cargo service, breed restrictions, crate requirements, and how to book your pet on {name}.",
        },
    }

    # Save data JSON
    data_path = os.path.join(DATA_OUT_DIR, f"{slug}.json")
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)

    # Create Hugo markdown
    md = f"""---
title: "{page_data['seo']['title']}"
description: "{page_data['seo']['description']}"
type: "airlines"
layout: "single"
slug: "{slug}"
airline_name: "{name}"
hub: "{page_data['hub']}"
alliance: "{page_data['alliance']}"
cabin_allowed: {str(cabin_allowed).lower()}
cargo_allowed: {str(cargo_allowed).lower()}
cargo_suspended: {str(cargo_suspended).lower()}
policy:
  accepted_animals: "{page_data['policy']['accepted_animals'].replace('"', "'")}"
  crate_requirements: "{page_data['policy']['crate_requirements'].replace('"', "'")}"
  size_limits: "{page_data['policy']['size_limits'].replace('"', "'")}"
  temperature_restrictions: "{page_data['policy']['temperature_restrictions'].replace('"', "'")}"
  brachycephalic_policy: "{page_data['policy']['brachycephalic_policy'].replace('"', "'")}"
  cost_range: "{page_data['policy']['cost_range'].replace('"', "'")}"
  booking_process: "{page_data['policy']['booking_process'].replace('"', "'")}"
content:
  h1: "{page_data['content']['h1']}"
  overview: |
"""
    for line in page_data['content']['overview'].splitlines():
        md += f"    {line}\n"

    md += "faqs:\n"
    for faq in page_data['faqs']:
        q = faq['question'].replace('"', "'")
        a = faq['answer'].replace('"', "'")
        md += f'  - question: "{q}"\n'
        md += f'    answer: "{a}"\n'

    md += "---\n"

    content_path = os.path.join(CONTENT_DIR, f"{slug}.md")
    with open(content_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  {slug}.md  ({name})")

print(f"\nDone. {len(airlines)} airline pages created.")
