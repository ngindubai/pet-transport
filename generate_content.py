"""
Blocks 14+15: Wordsmith + Interrogator Content Generation
Generates route-specific content (overview, sections, FAQs) for all 15 Tier 1 routes.
Updates existing route data JSON files with content and FAQ data.
Follows Wordsmith voice rules: warm, practical, honest, no banned vocabulary, no em dashes.
"""
import json
import os
import random

DATA_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"

# Variation pools for opening hooks
OVERVIEW_OPENERS = [
    "Moving your {pet} from {origin} to {dest} takes planning.",
    "Shipping a {pet} between {origin} and {dest} is one of the {complexity_adj} international pet transport routes.",
    "If you're relocating from {origin} to {dest} with a {pet}, here's what you need to know.",
    "Transporting your {pet} from {origin} to {dest} involves several steps, but thousands of families do it every year.",
    "Getting your {pet} from {origin} to {dest} isn't something you can arrange in a weekend.",
    "The {origin} to {dest} route is popular with expats, families on assignment, and people returning home with their pets.",
]

COMPLEXITY_ADJECTIVES = {
    "low": "more straightforward",
    "moderate": "moderately complex",
    "high": "more demanding",
    "very_high": "most complex",
    "extreme": "most challenging",
}


def load_route(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_route(filename, data):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_overview(route):
    """Generate a unique overview paragraph for the route."""
    rd = route["route_data"]
    origin = route["origin_name"]
    dest = route["destination_name"]
    complexity = rd.get("route_complexity", "moderate")
    timeline = rd.get("estimated_timeline_weeks", "8-12")
    airlines = rd.get("airlines", [])
    import_reqs = rd["destination"]["import_requirements"]

    complexity_adj = COMPLEXITY_ADJECTIVES.get(complexity, "moderately complex")
    pet = random.choice(["pet", "dog or cat", "dog", "cat"])

    opener_template = random.choice(OVERVIEW_OPENERS)
    opener = opener_template.format(
        pet=pet, origin=origin, dest=dest, complexity_adj=complexity_adj
    )

    # Build unique middle section based on what's notable about this route
    middle_parts = []

    # Timeline
    middle_parts.append(
        f"Expect to start preparations {timeline} weeks before your travel date."
    )

    # Key requirement highlights
    if import_reqs.get("quarantine") and "mandatory" in import_reqs.get("quarantine", "").lower():
        middle_parts.append(
            f"{dest} requires mandatory quarantine for all arriving pets, which adds time and cost to the process."
        )

    if import_reqs.get("titre_test") and "required" in import_reqs.get("titre_test", "").lower():
        middle_parts.append(
            "A rabies titre test (blood test) is required, which means an additional waiting period after vaccination."
        )

    if import_reqs.get("import_permit") and "required" in import_reqs.get("import_permit", "").lower():
        middle_parts.append(
            f"You'll need to apply for an import permit from {dest} before your pet can travel."
        )

    # Airlines
    airline_names = [a["name"] for a in airlines[:4]]
    if airline_names:
        if len(airline_names) == 1:
            airline_str = airline_names[0]
        elif len(airline_names) == 2:
            airline_str = f"{airline_names[0]} and {airline_names[1]}"
        else:
            airline_str = f"{', '.join(airline_names[:-1])}, and {airline_names[-1]}"
        middle_parts.append(
            f"Airlines serving this route include {airline_str}."
        )

    middle = " ".join(middle_parts)

    # Closing
    closers = [
        "Getting the paperwork right is the hardest part. Once that's sorted, the flight itself is the easy bit.",
        "The process is manageable if you start early and follow the steps in order.",
        "We've put together this guide to walk you through every step.",
        f"This guide covers everything: {dest}'s import rules, what you need from {origin}'s side, airlines, costs, and timelines.",
    ]
    closer = random.choice(closers)

    return f"{opener}\n\n{middle}\n\n{closer}"


def generate_sections(route):
    """Generate content sections specific to this route."""
    rd = route["route_data"]
    origin = route["origin_name"]
    dest = route["destination_name"]
    complexity = rd.get("route_complexity", "moderate")
    import_reqs = rd["destination"]["import_requirements"]
    airlines = rd.get("airlines", [])
    warnings = rd.get("key_warnings", [])

    sections = []

    # Section 1: What makes this route unique
    unique_heading = random.choice([
        f"What makes the {origin} to {dest} route different",
        f"Key things to know about this route",
        f"Why {origin} to {dest} pet transport needs planning",
    ])

    unique_parts = []
    if complexity in ("very_high", "extreme"):
        unique_parts.append(
            f"This is one of the more complex international pet transport routes. {dest}'s regulations are strict, and there's no shortcut through the process."
        )
    elif complexity == "high":
        unique_parts.append(
            f"This route has some additional hurdles compared to simpler corridors. {dest} has specific requirements that catch people off guard if they haven't researched properly."
        )
    else:
        unique_parts.append(
            f"Compared to some international routes, {origin} to {dest} is relatively straightforward. That doesn't mean you can leave it to the last minute."
        )

    # Add destination-specific colour
    if "quarantine" in import_reqs.get("quarantine", "").lower() and "mandatory" in import_reqs.get("quarantine", "").lower():
        unique_parts.append(
            f"{dest} is one of the few countries that still requires mandatory quarantine for arriving pets. Your pet will spend time in a government facility on arrival, and you can't visit during that period. It's the part of the process most owners find hardest."
        )

    if rd["destination"].get("breed_restrictions"):
        breeds = rd["destination"]["breed_restrictions"]
        if breeds:
            breed_names = [b.split(" (")[0] for b in breeds[:3]]
            unique_parts.append(
                f"{dest} bans or restricts certain breeds. {', '.join(breed_names)} types are affected. If your dog is one of these breeds or a mix, contact a specialist before making plans."
            )

    sections.append({
        "heading": unique_heading,
        "body": "\n\n".join(unique_parts),
    })

    # Section 2: Practical tips for this specific route
    tips_heading = random.choice([
        f"Practical tips for shipping your pet from {origin} to {dest}",
        f"Things we'd tell a friend moving their pet to {dest}",
        f"Advice from experience: {origin} to {dest}",
    ])

    tips = []
    tips.append("Start the microchip and vaccination process as early as possible. The biggest mistake people make is leaving it too late. Once you miss a deadline, the entire timeline pushes back.")

    # Route-specific tips
    cargo_airlines = [a for a in airlines if "cargo" in a.get("type", "")]
    cabin_airlines = [a for a in airlines if "cabin" in a.get("type", "")]

    if cargo_airlines and not cabin_airlines:
        tips.append(
            f"All airlines on this route transport pets as cargo, not in the cabin. That means your pet flies in a temperature-controlled hold in an IATA-approved crate. It's standard practice and well-regulated."
        )
    elif cabin_airlines:
        cabin_names = [a["name"] for a in cabin_airlines[:2]]
        tips.append(
            f"Some airlines on this route ({', '.join(cabin_names)}) allow small pets in the cabin. Your pet must fit in a carrier under the seat. Weight limits are strict: usually 8-10kg including the carrier."
        )

    if any("temperature" in w.lower() or "summer" in w.lower() for w in warnings):
        tips.append(
            "Watch the calendar. Temperature embargoes mean airlines won't accept pets during extreme heat or cold. If you're planning a summer move, book early and have a backup date."
        )

    tips.append(
        "Use a pet transport agent if you're not confident handling the paperwork yourself. A good agent knows the current rules, has relationships with airline cargo departments, and can troubleshoot problems before they become disasters."
    )

    sections.append({
        "heading": tips_heading,
        "body": "\n\n".join(tips),
    })

    # Section 3: What happens on travel day
    travel_heading = random.choice([
        "What happens on travel day",
        "The day your pet flies",
        f"Travel day: {origin} to {dest}",
    ])

    travel_parts = []
    travel_parts.append(
        "Arrive at the airport at least 3 hours before departure if your pet is travelling as cargo. You'll need to present all original documents: health certificate, vaccination records, microchip number, and any import permits."
    )
    travel_parts.append(
        "Your pet's crate must be clean, labelled with your contact details and the consignee's details at the destination, and have food and water containers attached. Live animal stickers and orientation arrows are required."
    )

    if "quarantine" in import_reqs.get("quarantine", "").lower() and "mandatory" in import_reqs.get("quarantine", "").lower():
        travel_parts.append(
            f"On arrival in {dest}, your pet goes directly to the quarantine facility. You won't collect them at the airport. The quarantine authorities will contact you when the quarantine period ends."
        )
    else:
        travel_parts.append(
            f"On arrival in {dest}, you (or your agent) collect your pet from the cargo terminal. There may be an inspection by veterinary authorities at the airport. Have copies of all paperwork ready."
        )

    sections.append({
        "heading": travel_heading,
        "body": "\n\n".join(travel_parts),
    })

    return sections


def generate_faqs(route):
    """Generate route-specific FAQs following The Interrogator's format."""
    rd = route["route_data"]
    origin = route["origin_name"]
    dest = route["destination_name"]
    import_reqs = rd["destination"]["import_requirements"]
    airlines = rd.get("airlines", [])
    timeline = rd.get("estimated_timeline_weeks", "8-12")
    breed_restrictions = rd["destination"].get("breed_restrictions", [])

    faqs = []

    # FAQ 1: Quarantine question (always relevant)
    quarantine_text = import_reqs.get("quarantine", "")
    if "mandatory" in quarantine_text.lower():
        faqs.append({
            "question": f"Is there quarantine for pets arriving in {dest} from {origin}?",
            "answer": f"Yes. {dest} requires mandatory quarantine for all arriving pets. {quarantine_text}. You should factor the quarantine period into your planning and budget."
        })
    elif "no routine quarantine" in quarantine_text.lower():
        faqs.append({
            "question": f"Will my pet need to go into quarantine when arriving in {dest}?",
            "answer": f"No, not if all your paperwork is correct. {dest} does not require routine quarantine for pets with valid documentation. However, if anything is missing or incorrect, your pet could face penalty quarantine at your expense. Getting the paperwork right is not optional."
        })
    else:
        faqs.append({
            "question": f"Does {dest} require quarantine for pets from {origin}?",
            "answer": f"It depends on your specific circumstances. {quarantine_text}. Check with the destination authorities or a pet transport specialist for your exact situation."
        })

    # FAQ 2: Airlines
    airline_names = [a["name"] for a in airlines[:5]]
    if airline_names:
        airline_list = ", ".join(airline_names)
        cargo_only = all("cargo" in a.get("type", "") for a in airlines[:5])
        if cargo_only:
            faqs.append({
                "question": f"Which airlines transport pets from {origin} to {dest}?",
                "answer": f"Airlines operating pet cargo on this route include {airline_list}. All transport pets as manifested cargo in temperature-controlled holds, not in the cabin. You'll need an IATA-compliant crate and should book cargo space well in advance. Some airlines have seasonal restrictions and brachycephalic breed embargoes."
            })
        else:
            cabin_names = [a["name"] for a in airlines if "cabin" in a.get("type", "")][:2]
            faqs.append({
                "question": f"Can my pet fly in the cabin from {origin} to {dest}?",
                "answer": f"Some airlines allow small pets (typically under 8kg with carrier) in the cabin. {', '.join(cabin_names)} offer cabin options on this route. Larger pets must travel as cargo. Airlines with cargo service include {airline_list}. Availability varies by season and aircraft type, so confirm when booking."
            })

    # FAQ 3: Timeline
    faqs.append({
        "question": f"How far in advance should I start preparing to move my pet from {origin} to {dest}?",
        "answer": f"Start at least {timeline} weeks before your planned travel date. The process begins with microchipping, then rabies vaccination (with a mandatory waiting period), then any required blood tests, health certificates, and permit applications. Rushing the timeline is the most common reason people hit problems."
    })

    # FAQ 4: Cost question
    faqs.append({
        "question": f"How much does it cost to transport a dog from {origin} to {dest}?",
        "answer": f"The total cost depends on your dog's size, the airline, and whether you use a transport agent. For a medium-sized dog, expect to pay for: veterinary fees (vaccinations, health certificate, microchip), an IATA-compliant crate, airline cargo fees, government endorsements, and any import permits or quarantine fees at the destination. Using a door-to-door agent adds to the cost but handles the complexity for you."
    })

    # FAQ 5: Documents
    docs = []
    if import_reqs.get("microchip"):
        docs.append("proof of ISO microchip")
    if import_reqs.get("rabies_vaccination"):
        docs.append("rabies vaccination certificate")
    if import_reqs.get("titre_test") and "required" in import_reqs.get("titre_test", "").lower():
        docs.append("rabies titre test results")
    if import_reqs.get("health_certificate"):
        docs.append("official health certificate")
    if import_reqs.get("import_permit") and "required" in import_reqs.get("import_permit", "").lower():
        docs.append("import permit")

    if docs:
        doc_list = ", ".join(docs)
        faqs.append({
            "question": f"What documents does my pet need to travel from {origin} to {dest}?",
            "answer": f"Your pet will need: {doc_list}. The health certificate must be issued by an official veterinarian within 10 days of travel. Some documents need government endorsement. Check every requirement against the current rules, because regulations change and an outdated document can mean your pet doesn't fly."
        })

    # FAQ 6: Breed restrictions (if applicable)
    if breed_restrictions:
        breed_names = [b.split(" (")[0] for b in breed_restrictions[:4]]
        faqs.append({
            "question": f"Are any dog breeds banned from entering {dest}?",
            "answer": f"{dest} restricts or bans certain breeds. Currently affected: {', '.join(breed_names)}. This is a type-based assessment in some countries, meaning dogs that physically resemble a banned breed can be classified as that type regardless of pedigree. If your dog is a restricted breed or a mix, get specialist advice before making any arrangements."
        })

    # FAQ 7: Brachycephalic breeds (always relevant for airline routes)
    faqs.append({
        "question": f"Can I fly my French Bulldog or Pug from {origin} to {dest}?",
        "answer": "Brachycephalic (flat-faced) breeds face restrictions on most airlines, particularly for cargo transport. These breeds are more vulnerable to breathing difficulties at altitude and in heat. Many airlines impose seasonal embargoes (typically summer months), and some restrict flat-faced breeds from cargo year-round. A few airlines still accept them with additional veterinary clearance. Check the specific airline's current policy before booking."
    })

    # FAQ 8: Cats (route-specific if interesting)
    if dest in ("United States", "United Kingdom"):
        faqs.append({
            "question": f"Is it easier to transport a cat from {origin} to {dest} than a dog?",
            "answer": f"Generally, yes. Cats face fewer regulatory hurdles than dogs in most countries." + (
                " The US has no federal import requirements for cats at all, which makes the process significantly simpler."
                if dest == "United States" else
                f" {dest} still requires microchip, rabies vaccination, and a health certificate for cats, but cats don't need tapeworm treatment (that's dogs only for UK entry)."
            )
        })

    return faqs


def generate_content_for_route(filename):
    """Generate all content for a single route."""
    route = load_route(filename)

    # Set random seed based on route for reproducibility but variation
    seed = hash(filename) % 10000
    random.seed(seed)

    # Generate content
    route["content"]["overview"] = generate_overview(route)
    route["content"]["sections"] = generate_sections(route)
    route["faqs"] = generate_faqs(route)

    # Update status
    route["status"] = "draft"

    save_route(filename, route)
    return route


# === MAIN ===
route_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".json")])

print(f"Generating content for {len(route_files)} routes...\n")

for rf in route_files:
    route = generate_content_for_route(rf)
    faqs_count = len(route["faqs"])
    sections_count = len(route["content"]["sections"])
    overview_len = len(route["content"]["overview"])
    print(f"  {rf}")
    print(f"    Overview: {overview_len} chars | Sections: {sections_count} | FAQs: {faqs_count}")

print(f"\nDone. Content generated for {len(route_files)} routes.")
