"""
Block 23 / Task 2.2: P2 Route Page Generation
Generates Hugo markdown route pages for all P2 country pairs.
Covers: P2 x P1 (both directions) + high-value P2 x P2 pairs.
Skip-if-exists: never overwrites existing files.

Output: site/content/routes/[origin-slug]-to-[destination-slug].md
"""

import json
import os
import random
import re

# ============================================================
# PATHS
# ============================================================
REPO_ROOT = r"c:\Users\garet\Desktop\pet-transport"
DATA_DIR = os.path.join(REPO_ROOT, "data")
CONTENT_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")
AIRLINE_DATA = os.path.join(DATA_DIR, "airline_pet_policies.json")
COUNTRY_DATA = os.path.join(DATA_DIR, "countries_pet_regulations.json")

os.makedirs(CONTENT_DIR, exist_ok=True)

# ============================================================
# LOAD SOURCE DATA
# ============================================================
with open(COUNTRY_DATA, "r", encoding="utf-8") as f:
    countries_raw = json.load(f)["countries"]

with open(AIRLINE_DATA, "r", encoding="utf-8") as f:
    airlines_raw = json.load(f)["airlines"]

# ============================================================
# COUNTRY REGISTRY
# All 25 countries: JSON key -> (display name, ISO alpha2, slug)
# ============================================================
COUNTRY_REGISTRY = {
    # P1
    "UK":           ("United Kingdom",       "GB", "united-kingdom"),
    "USA":          ("United States",        "US", "united-states"),
    "UAE":          ("United Arab Emirates", "AE", "united-arab-emirates"),
    "Australia":    ("Australia",            "AU", "australia"),
    "Canada":       ("Canada",               "CA", "canada"),
    "Germany":      ("Germany",              "DE", "germany"),
    "France":       ("France",               "FR", "france"),
    "Singapore":    ("Singapore",            "SG", "singapore"),
    "Hong_Kong":    ("Hong Kong",            "HK", "hong-kong"),
    "South_Africa": ("South Africa",         "ZA", "south-africa"),
    # P2
    "Japan":        ("Japan",                "JP", "japan"),
    "Thailand":     ("Thailand",             "TH", "thailand"),
    "Philippines":  ("Philippines",          "PH", "philippines"),
    "Malaysia":     ("Malaysia",             "MY", "malaysia"),
    "India":        ("India",                "IN", "india"),
    "Portugal":     ("Portugal",             "PT", "portugal"),
    "Netherlands":  ("Netherlands",          "NL", "netherlands"),
    "Italy":        ("Italy",                "IT", "italy"),
    "Denmark":      ("Denmark",              "DK", "denmark"),
    "Mexico":       ("Mexico",               "MX", "mexico"),
    "Brazil":       ("Brazil",               "BR", "brazil"),
    "Switzerland":  ("Switzerland",          "CH", "switzerland"),
    "Indonesia":    ("Indonesia",            "ID", "indonesia"),
    "South Korea":  ("South Korea",          "KR", "south-korea"),
    "Greece":       ("Greece",               "GR", "greece"),
}

# Reverse: ISO code -> JSON key
CODE_TO_KEY = {v[1]: k for k, v in COUNTRY_REGISTRY.items()}

P1_KEYS = ["UK", "USA", "UAE", "Australia", "Canada", "Germany", "France",
           "Singapore", "Hong_Kong", "South_Africa"]

P2_KEYS = ["Japan", "Thailand", "Philippines", "Malaysia", "India", "Portugal",
           "Netherlands", "Italy", "Denmark", "Mexico", "Brazil", "Switzerland",
           "Indonesia", "South Korea", "Greece"]

# High-value P2 x P2 pairs (both directions added below)
P2_P2_PAIRS = [
    ("Japan",       "Australia"),
    ("Japan",       "UK"),
    ("Japan",       "USA"),
    ("India",       "UK"),
    ("India",       "USA"),
    ("India",       "Australia"),
    ("India",       "Canada"),
    ("India",       "UAE"),
    ("Thailand",    "UK"),
    ("Thailand",    "Australia"),
    ("Thailand",    "USA"),
    ("Malaysia",    "UK"),
    ("Malaysia",    "Australia"),
    ("South Korea", "USA"),
    ("South Korea", "Australia"),
    ("South Korea", "UK"),
    ("Philippines", "USA"),
    ("Philippines", "Australia"),
    ("Philippines", "UK"),
    ("Italy",       "Australia"),
    ("Netherlands", "Australia"),
    ("Portugal",    "UK"),
    ("Portugal",    "USA"),
    ("Mexico",      "USA"),
    ("Mexico",      "UK"),
    ("Brazil",      "UK"),
    ("Brazil",      "USA"),
    ("Switzerland", "UK"),
    ("Switzerland", "USA"),
    ("Greece",      "Australia"),
    ("Indonesia",   "Australia"),
]

# Build full route list
ALL_ROUTES = []

# P2 x P1 both ways
for p2 in P2_KEYS:
    for p1 in P1_KEYS:
        ALL_ROUTES.append((p2, p1))
        ALL_ROUTES.append((p1, p2))

# P2 x P2 pairs (both directions)
for a, b in P2_P2_PAIRS:
    ALL_ROUTES.append((a, b))
    ALL_ROUTES.append((b, a))

# Deduplicate
seen = set()
DEDUPED_ROUTES = []
for pair in ALL_ROUTES:
    if pair not in seen:
        seen.add(pair)
        DEDUPED_ROUTES.append(pair)


# ============================================================
# AIRLINE SELECTOR
# Pick airlines relevant to the route based on hubs/regions
# ============================================================
AIRLINE_SUMMARY = {
    "Emirates": ("Emirates", "cargo_only",
        "Cargo: Emirates SkyCargo handles all pet transport as manifested cargo. "
        "Brachycephalic breeds accepted with additional requirements and seasonal restrictions. "
        "Temperature embargoes during extreme heat (summer months in Gulf region)"),
    "British Airways": ("British Airways", "cargo_only",
        "Cargo: Pets transported via British Airways World Cargo in temperature-controlled hold. "
        "Book through approved cargo agent. No cabin pets on any route."),
    "Singapore Airlines": ("Singapore Airlines", "cargo_only",
        "Cargo: Pets travel in temperature-controlled hold. "
        "Brachycephalic breeds subject to restrictions. Temperature embargoes apply on certain routes/seasons"),
    "Qantas": ("Qantas", "cargo_only",
        "Cargo: QantasFreighter network for pet transport. "
        "Brachycephalic breeds restricted year-round. Temperature embargoes: seasonal restrictions during Australian summer (Dec-Feb)"),
    "Air France": ("Air France", "cabin_and_cargo",
        "Small pets allowed in cabin (up to 8kg including carrier). "
        "Cargo transport available for larger pets. Brachycephalic breeds subject to restrictions/seasonal embargoes"),
    "Lufthansa": ("Lufthansa", "cabin_and_cargo",
        "Small pets (up to 8kg with carrier) allowed in cabin. "
        "Cargo: larger pets via Lufthansa Cargo in pressurised, temperature-controlled hold. "
        "Brachycephalic breeds restricted from cargo year-round"),
    "KLM": ("KLM", "cabin_and_cargo",
        "Small pets allowed in cabin (up to 8kg including carrier). "
        "Cargo: pets transported via KLM Cargo. Temperature restrictions apply. "
        "Brachycephalic breeds restricted from cargo"),
    "United Airlines": ("United Airlines", "cabin_only",
        "Small pets allowed in cabin in approved carrier (under seat). "
        "No cargo transport for pets. Temperature restrictions limit summer/winter travel"),
    "Delta Air Lines": ("Delta Air Lines", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: Delta Cargo handles larger pets in temperature-controlled hold. Brachycephalic breeds restricted from cargo"),
    "American Airlines": ("American Airlines", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: American Airlines Cargo handles pet transport. Seasonal temperature embargoes apply"),
    "Cathay Pacific": ("Cathay Pacific", "cargo_only",
        "Cargo: Pets travel as manifested cargo in temperature-controlled hold. "
        "Brachycephalic breeds restricted during summer months. Hong Kong AFCD import regulations must be met"),
    "Etihad Airways": ("Etihad Airways", "cargo_only",
        "Cargo: Pets travel through Etihad Cargo. "
        "Brachycephalic breeds subject to seasonal restrictions. Temperature embargoes during Abu Dhabi summer months"),
    "Air Canada": ("Air Canada", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: Air Canada Cargo handles pet transport in heated/pressurised hold. "
        "Brachycephalic breeds restricted from cargo year-round"),
    "Korean Air": ("Korean Air", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: Larger pets in hold as checked baggage or Korean Air Cargo. "
        "Seasonal temperature restrictions apply"),
    "Japan Airlines (JAL)": ("Japan Airlines (JAL)", "cargo_only",
        "Cargo: Pets transported as checked baggage in temperature-controlled hold. "
        "Brachycephalic breeds: French Bulldogs BANNED from cargo (May-October). English Bulldogs banned year-round. "
        "Summer restrictions: May-October temperature embargoes on some routes"),
    "Thai Airways": ("Thai Airways", "cargo_only",
        "Cargo: Pets as checked baggage or Thai Cargo for larger animals. "
        "Brachycephalic breeds restricted during hot season (March-May). Some breed restrictions apply"),
    "Philippine Airlines": ("Philippine Airlines", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: Pets as checked baggage or PAL Cargo. "
        "Brachycephalic breeds restricted from cargo. Temperature restrictions during extreme heat"),
    "Garuda Indonesia": ("Garuda Indonesia", "cabin_and_cargo",
        "Small pets allowed in cabin. "
        "Cargo: Larger pets transported as checked baggage in pressurised, temperature-controlled hold. "
        "Brachycephalic breeds: check specific restrictions. Weight limits apply per aircraft type"),
    "Air India": ("Air India", "cabin_and_cargo",
        "Small pets allowed in cabin (up to 5kg with carrier). "
        "Cargo: Larger pets via Air India Cargo. Breed restrictions apply. "
        "Temperature embargoes during extreme heat on Indian domestic sectors"),
    "IndiGo": ("IndiGo", "cabin_only",
        "Small pets allowed in cabin on domestic India routes only. "
        "International cargo via partner airlines. Temperature restrictions apply"),
}


def get_airlines_for_route(origin_key, dest_key):
    """Return a relevant subset of airlines for this route pair."""
    origin_name, origin_code, _ = COUNTRY_REGISTRY[origin_key]
    dest_name, dest_code, _ = COUNTRY_REGISTRY[dest_key]

    selected = []

    # Region-based logic
    origin_region = countries_raw.get(origin_key, {}).get("region", "")
    dest_region = countries_raw.get(dest_key, {}).get("region", "")

    def add(name):
        if name in AIRLINE_SUMMARY and name not in [a[0] for a in selected]:
            selected.append(AIRLINE_SUMMARY[name])

    # Flag carriers based on origin/destination
    flag_map = {
        "GB": "British Airways", "US": "United Airlines", "AE": "Emirates",
        "AU": "Qantas", "CA": "Air Canada", "DE": "Lufthansa", "FR": "Air France",
        "SG": "Singapore Airlines", "HK": "Cathay Pacific", "ZA": "British Airways",
        "JP": "Japan Airlines (JAL)", "TH": "Thai Airways", "PH": "Philippine Airlines",
        "MY": "Malaysian Airlines", "IN": "Air India", "PT": "Air France",
        "NL": "KLM", "IT": "Air France", "DK": "British Airways", "MX": "American Airlines",
        "BR": "Air France", "CH": "Lufthansa", "ID": "Garuda Indonesia",
        "KR": "Korean Air", "GR": "Air France",
    }

    # Add origin flag carrier
    if origin_code in flag_map:
        add(flag_map[origin_code])
    # Add destination flag carrier
    if dest_code in flag_map:
        add(flag_map[dest_code])

    # Core connecting carriers (almost always relevant)
    for airline in ["Emirates", "Lufthansa", "Singapore Airlines", "British Airways",
                    "Cathay Pacific", "Air France", "KLM"]:
        add(airline)

    # Route-specific extras
    if dest_code in ("AU", "NZ") or origin_code in ("AU", "NZ"):
        add("Qantas")
        add("Singapore Airlines")

    if "Americas" in (origin_region, dest_region):
        add("Delta Air Lines")
        add("American Airlines")
        add("Air Canada")

    if origin_code in ("JP",) or dest_code in ("JP",):
        add("Japan Airlines (JAL)")
        add("Korean Air")

    if origin_code in ("TH",) or dest_code in ("TH",):
        add("Thai Airways")

    if origin_code in ("PH",) or dest_code in ("PH",):
        add("Philippine Airlines")

    if origin_code in ("ID",) or dest_code in ("ID",):
        add("Garuda Indonesia")

    if origin_code in ("IN",) or dest_code in ("IN",):
        add("Air India")

    if origin_code in ("KR",) or dest_code in ("KR",):
        add("Korean Air")

    # Cap at 10 airlines
    return selected[:10]


# ============================================================
# FLATTEN IMPORT REQUIREMENTS (nested JSON -> flat strings)
# ============================================================
def flatten_import_reqs(country_key):
    reqs = countries_raw.get(country_key, {}).get("import_requirements", {})
    result = {}

    # Microchip
    mc = reqs.get("microchip", {})
    if isinstance(mc, dict):
        parts = []
        if mc.get("required"):
            parts.append(f"Required ({mc.get('standard', 'ISO 11784/11785')})")
        if mc.get("timing"):
            parts.append(mc["timing"])
        result["microchip"] = ". ".join(parts) if parts else "Required (ISO 11784/11785)"
    elif mc:
        result["microchip"] = str(mc)
    else:
        result["microchip"] = "Required (ISO 11784/11785)"

    # Rabies vaccination
    rv = reqs.get("rabies_vaccination", {})
    if isinstance(rv, dict):
        parts = []
        if rv.get("required"):
            parts.append("Required")
        if rv.get("minimum_age_weeks"):
            parts.append(f"Minimum age: {rv['minimum_age_weeks']} weeks")
        wait = rv.get("wait_after_first_vaccination_days") or rv.get("wait_after_vaccination_days")
        if wait:
            parts.append(f"{wait}-day wait after vaccination before travel")
        if rv.get("notes"):
            parts.append(rv["notes"])
        result["rabies_vaccination"] = ". ".join(parts) if parts else "Required"
    elif rv:
        result["rabies_vaccination"] = str(rv)
    else:
        result["rabies_vaccination"] = "Required"

    # Titre test
    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict):
        if tt.get("required") is False:
            result["titre_test"] = tt.get("notes", "Not required")
        else:
            parts = []
            if tt.get("required_for"):
                parts.append(f"Required for: {tt['required_for']}")
            elif tt.get("required") is True:
                parts.append("Required")
            if tt.get("not_required_for"):
                parts.append(f"Not required for: {tt['not_required_for']}")
            if tt.get("minimum_result"):
                parts.append(f"Minimum: {tt['minimum_result']}")
            wait = tt.get("wait_period_days") or tt.get("wait_after_test_days")
            if wait:
                parts.append(f"{wait}-day wait from test date before entry")
            if tt.get("notes") and not parts:
                parts.append(tt["notes"])
            result["titre_test"] = ". ".join(parts) if parts else "Check with destination authority"
    elif tt:
        result["titre_test"] = str(tt)

    # Quarantine
    q = reqs.get("quarantine", {})
    if isinstance(q, dict):
        if q.get("required") is True or q.get("mandatory") is True:
            parts = ["Mandatory quarantine"]
            dur = q.get("duration_days") or q.get("minimum_days")
            if dur:
                parts.append(f"{dur} days")
            fac = q.get("facility")
            if isinstance(fac, dict):
                if fac.get("name"):
                    parts.append(f"Facility: {fac['name']}")
                if fac.get("location"):
                    parts.append(f"Location: {fac['location']}")
            elif isinstance(fac, str) and fac:
                parts.append(f"Facility: {fac}")
            if q.get("notes"):
                parts.append(q["notes"])
            result["quarantine"] = ". ".join(parts)
        elif q.get("required") is False:
            note = "No routine quarantine for compliant pets"
            if q.get("penalty_quarantine") or q.get("penalty_duration_days"):
                note += f". Penalty quarantine applies if documentation is non-compliant"
            if q.get("notes"):
                note = q["notes"]
            result["quarantine"] = note
        else:
            result["quarantine"] = q.get("notes", "Check current requirements with destination authority")
    elif q:
        result["quarantine"] = str(q)

    # Import permit
    ip = reqs.get("import_permit", {})
    if isinstance(ip, dict):
        if ip.get("required") is True:
            parts = ["Required"]
            if ip.get("issued_by"):
                parts.append(f"Issued by: {ip['issued_by']}")
            if ip.get("timeline") or ip.get("lead_time"):
                parts.append(f"Apply: {ip.get('timeline') or ip.get('lead_time')}")
            if ip.get("notes"):
                parts.append(ip["notes"])
            result["import_permit"] = ". ".join(parts)
        elif ip.get("required") is False:
            result["import_permit"] = ip.get("alternative", ip.get("notes", "Not required"))
        else:
            result["import_permit"] = ip.get("notes", "Check with destination authority")
    elif ip:
        result["import_permit"] = str(ip)

    # Health certificate
    hc = reqs.get("health_certificate", {})
    if isinstance(hc, dict):
        parts = []
        if hc.get("required") is True:
            parts.append("Required")
        if hc.get("name"):
            parts.append(hc["name"])
        if hc.get("issued_by"):
            parts.append(f"Issued by: {hc['issued_by']}")
        valid = hc.get("valid_for_days") or hc.get("valid_for_entry_days")
        if valid:
            parts.append(f"Valid for {valid} days from issue")
        if hc.get("notes"):
            parts.append(hc["notes"])
        result["health_certificate"] = ". ".join(parts) if parts else "Required"
    elif hc:
        result["health_certificate"] = str(hc)
    else:
        result["health_certificate"] = "Required. Government-issued veterinary health certificate"

    return result


def flatten_export_reqs(country_key):
    reqs = countries_raw.get(country_key, {}).get("export_requirements", {})
    if not reqs:
        return {"export_permit": "No formal export permit required. Destination import documentation serves as travel authority."}

    result = {}
    # Try direct fields
    for field in ["export_permit", "vet_inspection", "endorsement", "health_certificate"]:
        val = reqs.get(field)
        if val:
            if isinstance(val, dict):
                result[field] = val.get("notes", val.get("description", str(val)))
            else:
                result[field] = str(val)
    # Try nested structure
    if not result:
        for dest_type in ["to_non_eu", "general", "to_eu"]:
            sub = reqs.get(dest_type, {})
            if isinstance(sub, dict):
                for field in ["health_certificate", "export_permit", "endorsement"]:
                    if field in sub and field not in result:
                        val = sub[field]
                        if isinstance(val, dict):
                            result[field] = val.get("notes", val.get("description", str(val)))
                        else:
                            result[field] = str(val)
    if not result:
        result["export_permit"] = "No formal export permit required for pets. Destination country import documentation required."
    return result


# ============================================================
# ROUTE COMPLEXITY & TIMELINE
# ============================================================
def assess_route(dest_key):
    """Return (complexity, timeline_weeks, warnings) based on destination reqs."""
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})

    score = 0
    warnings = []
    timeline_min = 4

    q = reqs.get("quarantine", {})
    if isinstance(q, dict) and (q.get("required") or q.get("mandatory")):
        score += 3
        dur = q.get("duration_days", 14)
        warnings.append(f"Mandatory quarantine required on arrival. Plan for separation from your pet.")
        timeline_min = max(timeline_min, 12)

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict) and tt.get("required") is not False:
        if tt.get("wait_period_days"):
            score += 2
            timeline_min = max(timeline_min, int(tt["wait_period_days"] / 7) + 8)
        elif tt.get("required") is True or tt.get("required_for"):
            score += 2
            timeline_min = max(timeline_min, 20)

    ip = reqs.get("import_permit", {})
    if isinstance(ip, dict) and ip.get("required") is True:
        score += 1
        warnings.append("Import permit must be obtained before travel. Apply well in advance.")

    bans = reqs.get("banned_breeds", {})
    if isinstance(bans, dict):
        banned = bans.get("banned_types", [])
        if banned:
            score += 1
            warnings.append(f"Breed restrictions apply at destination. Check if your dog is affected before booking.")

    warnings.append("Always verify current regulations with the destination country's official veterinary authority before travel.")

    timeline_max = timeline_min + 6

    if score >= 6:
        complexity = "very_high"
        timeline = f"{max(timeline_min, 26)}-{max(timeline_max, 32)}"
    elif score >= 4:
        complexity = "high"
        timeline = f"{max(timeline_min, 16)}-{max(timeline_max, 20)}"
    elif score >= 2:
        complexity = "moderate"
        timeline = f"{max(timeline_min, 8)}-{max(timeline_max, 12)}"
    else:
        complexity = "low"
        timeline = f"{max(timeline_min, 4)}-{max(timeline_max, 8)}"

    return complexity, timeline, warnings


# ============================================================
# TIMELINE STEPS
# ============================================================
def build_timeline_steps(dest_key):
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})
    steps = []
    step_num = 1

    steps.append({
        "step": step_num, "action": "Microchip your pet (ISO 11784/11785 standard)",
        "timing": "First step — must be done before any vaccinations.",
        "responsible": "Your veterinarian"
    })
    step_num += 1

    rv = reqs.get("rabies_vaccination", {})
    if isinstance(rv, dict) and rv.get("required"):
        wait = rv.get("wait_after_first_vaccination_days") or rv.get("wait_after_vaccination_days", 21)
        steps.append({
            "step": step_num, "action": "Rabies vaccination",
            "timing": f"After microchip. {wait}-day wait before next steps.",
            "responsible": "Your veterinarian"
        })
        step_num += 1

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict) and tt.get("required") is not False:
        if tt.get("required") is True or tt.get("required_for") or tt.get("wait_period_days"):
            wait = tt.get("wait_period_days", 90)
            steps.append({
                "step": step_num, "action": "Rabies titre test (blood test at accredited laboratory)",
                "timing": f"Blood drawn at least 30 days after vaccination. {wait}-day wait after successful result.",
                "responsible": "Your veterinarian + approved laboratory"
            })
            step_num += 1

    ip = reqs.get("import_permit", {})
    dest_name = COUNTRY_REGISTRY.get(dest_key, ("", "", ""))[0]
    if isinstance(ip, dict) and ip.get("required") is True:
        lead = ip.get("timeline") or ip.get("lead_time", "allow 4-6 weeks")
        steps.append({
            "step": step_num, "action": f"Apply for import permit from {dest_name}",
            "timing": f"Apply early: {lead}",
            "responsible": "You (or your pet transport agent)"
        })
        step_num += 1

    steps.append({
        "step": step_num, "action": "Book IATA-compliant flight and cargo/cabin space",
        "timing": "2-4 weeks before travel. Confirm pet space with airline directly.",
        "responsible": "You (or your pet transport agent)"
    })
    step_num += 1

    steps.append({
        "step": step_num, "action": "Obtain official veterinary health certificate",
        "timing": "Within 10 days of travel (check destination-specific requirement)",
        "responsible": "Official veterinarian"
    })
    step_num += 1

    steps.append({
        "step": step_num, "action": "Travel day: arrive early, present all documentation at cargo desk",
        "timing": "3-4 hours before departure for cargo pets; 2 hours for cabin",
        "responsible": "You + airline check-in/cargo desk"
    })

    q = reqs.get("quarantine", {})
    if isinstance(q, dict) and (q.get("required") or q.get("mandatory")):
        dur = q.get("duration_days", "varies")
        step_num += 1
        steps.append({
            "step": step_num, "action": f"Quarantine on arrival ({dur} days)",
            "timing": "Immediately on arrival — mandatory",
            "responsible": f"{dest_name} quarantine authority"
        })

    return steps


# ============================================================
# COST FACTORS
# ============================================================
def build_cost_factors(dest_key):
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})
    factors = [
        "Airline cargo or cabin fees (varies by carrier, route, pet weight, and crate size)",
        "IATA-compliant travel crate (purchase or hire)",
        "Veterinary fees: vaccinations, microchipping, health certificate",
    ]

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict) and tt.get("required") is not False:
        if tt.get("required") is True or tt.get("required_for"):
            factors.append("Rabies titre test laboratory fee")

    ip = reqs.get("import_permit", {})
    if isinstance(ip, dict) and ip.get("required") is True:
        dest_name = COUNTRY_REGISTRY.get(dest_key, ("", "", ""))[0]
        factors.append(f"Import permit application fee ({dest_name})")

    q = reqs.get("quarantine", {})
    if isinstance(q, dict) and (q.get("required") or q.get("mandatory")):
        factors.append("Quarantine facility fees (owner-paid at destination)")

    factors.append("Pet transport agent fee (recommended for complex routes)")
    return factors


# ============================================================
# CONTENT GENERATION — overview, sections, FAQs
# ============================================================
OVERVIEW_OPENERS = [
    "Moving a pet from {origin} to {dest} involves more paperwork than most owners expect.",
    "Shipping your {pet} from {origin} to {dest} is a process that rewards early planning.",
    "If you're relocating from {origin} to {dest} and taking your pet, the good news is thousands of families do this every year.",
    "Getting your {pet} from {origin} to {dest} is entirely achievable, but the preparation timeline is not flexible.",
    "Pet transport from {origin} to {dest} follows a clear process once you know what {dest} requires.",
    "The {origin} to {dest} route is one many expats and returning families navigate each year with their pets.",
    "Moving to {dest} from {origin} with a dog or cat means starting the paperwork months before your flight.",
    "International pet transport from {origin} to {dest} comes down to documentation timing more than anything else.",
]

COMPLEXITY_PHRASES = {
    "low": "relatively straightforward compared to some international routes",
    "moderate": "moderately involved, with a clear checklist to follow",
    "high": "one of the more document-heavy international pet routes",
    "very_high": "one of the most demanding international pet transport routes",
}

CLOSERS = [
    "Use this guide to map out your preparation timeline and avoid the most common mistakes.",
    "The paperwork is the hard part. Once everything is in order, the journey itself is well-managed.",
    "Start early and follow the steps in sequence. Missing a deadline pushes the whole timeline back.",
    "We've laid out every step below so you know exactly what to prepare and when.",
    "Getting the timing right is critical. Work backwards from your travel date and add a buffer.",
]


def generate_overview(origin_key, dest_key, complexity, timeline):
    origin_name = COUNTRY_REGISTRY[origin_key][0]
    dest_name = COUNTRY_REGISTRY[dest_key][0]
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})
    pet = random.choice(["pet", "dog or cat", "dog"])

    opener = random.choice(OVERVIEW_OPENERS).format(
        origin=origin_name, dest=dest_name, pet=pet
    )

    complexity_phrase = COMPLEXITY_PHRASES.get(complexity, "moderately involved")
    middle_parts = [f"This route is {complexity_phrase}."]

    middle_parts.append(
        f"Start preparations at least {timeline.split('-')[0]} weeks before your travel date — "
        f"some steps have fixed waiting periods that cannot be shortened."
    )

    q = reqs.get("quarantine", {})
    if isinstance(q, dict) and (q.get("required") or q.get("mandatory")):
        dur = q.get("duration_days", "")
        dur_str = f" ({dur} days)" if dur else ""
        middle_parts.append(
            f"{dest_name} requires mandatory quarantine{dur_str} for all arriving pets. "
            f"This is the part of the process most owners find hardest to plan around."
        )

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict) and tt.get("required") is not False and (
        tt.get("required") is True or tt.get("required_for") or tt.get("wait_period_days")
    ):
        middle_parts.append(
            "A rabies titre test is required, which adds a mandatory waiting period after your pet's vaccination. "
            "You cannot speed this up."
        )

    bans = reqs.get("banned_breeds", {})
    if isinstance(bans, dict) and bans.get("banned_types"):
        middle_parts.append(
            f"{dest_name} restricts certain breeds. "
            "Check the breed restriction section below before making any travel arrangements."
        )

    closer = random.choice(CLOSERS)
    return opener + "\n\n" + " ".join(middle_parts) + "\n\n" + closer


def generate_sections(origin_key, dest_key, complexity):
    origin_name = COUNTRY_REGISTRY[origin_key][0]
    dest_name = COUNTRY_REGISTRY[dest_key][0]
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})
    origin_reqs = countries_raw.get(origin_key, {}).get("import_requirements", {})

    sections = []

    # Section 1: What makes this route distinct
    heading_variants = [
        f"What to know about the {origin_name} to {dest_name} route",
        f"Key requirements for moving your pet to {dest_name}",
        f"Why this route needs early planning",
        f"Understanding {dest_name}'s pet import rules",
    ]
    heading = random.choice(heading_variants)

    body_parts = []
    if complexity in ("very_high", "extreme"):
        body_parts.append(
            f"This is one of the more demanding international pet transport corridors. "
            f"{dest_name} runs a strict biosecurity programme and there are no shortcuts through it."
        )
    elif complexity == "high":
        body_parts.append(
            f"{dest_name} has specific requirements that trip people up when they haven't researched properly. "
            f"The documentation process is thorough but manageable if you start early."
        )
    else:
        body_parts.append(
            f"Compared to some international pet transport routes, {origin_name} to {dest_name} is manageable. "
            f"That said, every country's rules are different and the timing requirements are strict."
        )

    q = reqs.get("quarantine", {})
    if isinstance(q, dict) and (q.get("required") or q.get("mandatory")):
        dur = q.get("duration_days", "")
        fac = q.get("facility", "a government-designated facility")
        body_parts.append(
            f"All pets must complete quarantine on arrival in {dest_name} "
            f"({'at ' + fac if isinstance(fac, str) else 'at the designated facility'})"
            f"{(' for ' + str(dur) + ' days') if dur else ''}. "
            f"This is non-negotiable and is entirely separate from the pre-travel preparation."
        )

    dest_notes = countries_raw.get(dest_key, {}).get("notes", "")
    if dest_notes:
        body_parts.append(dest_notes)

    sections.append({"heading": heading, "body": "\n\n".join(body_parts)})

    # Section 2: Practical advice
    tips_heading_variants = [
        f"Practical advice for shipping your pet from {origin_name}",
        f"Things to sort before you book",
        f"Step-by-step: what to do first",
        f"From experience: {origin_name} to {dest_name} pet transport",
    ]
    tips_heading = random.choice(tips_heading_variants)

    tips = []
    tips.append(
        "Microchip first, then vaccinate. The microchip must be implanted before any rabies vaccination "
        "for the vaccination to count. It's the most common and costly mistake people make."
    )

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict) and tt.get("required") is not False and (
        tt.get("required") is True or tt.get("required_for")
    ):
        tips.append(
            "Book the titre test laboratory well in advance. Approved labs have limited appointment slots "
            "and the blood sample processing takes time. Don't leave this to the last few weeks."
        )

    tips.append(
        "Get the health certificate from an official (government-approved) veterinarian, not just your regular vet. "
        "Some countries have strict requirements about who can sign the certificate. Check the destination "
        "authority's approved list."
    )

    tips.append(
        "If this is your first international pet move, consider using a registered pet transport agent. "
        "They handle the documentation, airline booking, crate sizing, and can troubleshoot issues. "
        "IPATA-registered agents are the recognised standard."
    )

    sections.append({"heading": tips_heading, "body": "\n\n".join(tips)})

    return sections


def generate_faqs(origin_key, dest_key, complexity, timeline):
    origin_name = COUNTRY_REGISTRY[origin_key][0]
    dest_name = COUNTRY_REGISTRY[dest_key][0]
    reqs = countries_raw.get(dest_key, {}).get("import_requirements", {})

    faqs = []

    # 1. How long
    faqs.append({
        "question": f"How long does it take to prepare a pet for transport from {origin_name} to {dest_name}?",
        "answer": (
            f"Allow at least {timeline.split('-')[0]} weeks from starting preparations to travel day. "
            f"Some steps involve mandatory waiting periods that cannot be shortened, so starting early "
            f"is the only way to keep to your schedule."
        )
    })

    # 2. Quarantine
    q = reqs.get("quarantine", {})
    if isinstance(q, dict):
        if q.get("required") or q.get("mandatory"):
            dur = q.get("duration_days", "")
            fac = q.get("facility", "a government-run facility")
            faqs.append({
                "question": f"Does my pet need to quarantine when entering {dest_name}?",
                "answer": (
                    f"Yes, quarantine is mandatory in {dest_name}. "
                    f"Your pet will stay {'for ' + str(dur) + ' days ' if dur else ''}"
                    f"at {fac if isinstance(fac, str) else 'the designated quarantine facility'} on arrival. "
                    f"This is non-negotiable and the cost is paid by the owner."
                )
            })
        else:
            faqs.append({
                "question": f"Does my pet need to quarantine when entering {dest_name}?",
                "answer": (
                    f"No routine quarantine is required in {dest_name} for pets arriving with correct documentation. "
                    f"However, if your pet arrives without the right paperwork, penalty quarantine can apply. "
                    f"Get everything right before you travel."
                )
            })

    # 3. Titre test
    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict):
        if tt.get("required") is False:
            faqs.append({
                "question": f"Is a rabies titre test required for pets entering {dest_name}?",
                "answer": (
                    f"No, {dest_name} does not require a rabies titre test for most pets arriving from "
                    f"{origin_name}. Your pet still needs a valid rabies vaccination and microchip. "
                    f"Check the current requirements with the destination authority before travel."
                )
            })
        elif tt.get("required") is True or tt.get("required_for") or tt.get("wait_period_days"):
            wait = tt.get("wait_period_days", 90)
            faqs.append({
                "question": f"Is a rabies titre test required for pets entering {dest_name}?",
                "answer": (
                    f"Yes, a rabies titre test is required. Blood must be drawn at least 30 days after "
                    f"your pet's rabies vaccination, and there is a {wait}-day waiting period after a "
                    f"successful result before your pet can enter {dest_name}. "
                    f"Start this process as early as possible."
                )
            })

    # 4. Import permit
    ip = reqs.get("import_permit", {})
    if isinstance(ip, dict) and ip.get("required") is True:
        faqs.append({
            "question": f"Do I need an import permit to bring my pet into {dest_name}?",
            "answer": (
                f"Yes, an import permit is required from {dest_name}'s authority "
                f"({ip.get('issued_by', 'the relevant government body')}). "
                f"Apply before you book your flight. "
                f"The permit specifies conditions your pet must meet and must be obtained in advance."
            )
        })

    # 5. Health certificate
    hc = reqs.get("health_certificate", {})
    if isinstance(hc, dict) and hc.get("required"):
        valid = hc.get("valid_for_days") or hc.get("valid_for_entry_days", 10)
        faqs.append({
            "question": f"What health certificate does my pet need for this route?",
            "answer": (
                f"Your pet needs a government-issued veterinary health certificate from an official vet "
                f"in {origin_name}. "
                f"The certificate must be issued within {valid} days of travel. "
                f"Present the original (not a copy) at check-in. "
                f"Check {dest_name}'s authority for the exact format required."
            )
        })

    # 6. Breed restrictions
    bans = reqs.get("banned_breeds", {})
    if isinstance(bans, dict) and bans.get("banned_types"):
        banned_list = bans["banned_types"]
        if isinstance(banned_list, list) and banned_list:
            sample = [str(b) for b in banned_list[:3]]
            faqs.append({
                "question": f"Are there breed restrictions for entering {dest_name}?",
                "answer": (
                    f"Yes, {dest_name} bans or restricts certain breeds including "
                    f"{', '.join(sample)}{'.' if len(banned_list) <= 3 else ', and others.'} "
                    f"If your dog is one of these types or a mix, contact the destination authority "
                    f"before making any travel arrangements."
                )
            })

    # Ensure at least 4 FAQs
    if len(faqs) < 4:
        faqs.append({
            "question": f"Can I take my cat to {dest_name} from {origin_name}?",
            "answer": (
                f"Yes, cats can be transported from {origin_name} to {dest_name}. "
                f"The same microchip, vaccination, and health certificate requirements apply as for dogs, "
                f"though some rules (such as tapeworm treatment) apply to dogs only. "
                f"Check the full requirements for cats with the destination authority."
            )
        })

    return faqs[:8]  # Cap at 8 FAQs


# ============================================================
# GENERATE MARKDOWN FILE
# ============================================================
def generate_route_markdown(origin_key, dest_key):
    origin_name, origin_code, origin_slug = COUNTRY_REGISTRY[origin_key]
    dest_name, dest_code, dest_slug = COUNTRY_REGISTRY[dest_key]

    slug = f"{origin_slug}-to-{dest_slug}"

    # Title variation to avoid duplicate patterns
    title_templates = [
        f"Pet Transport from {origin_name} to {dest_name} | PetTransportGlobal",
        f"Moving Your Pet from {origin_name} to {dest_name} | Complete Guide",
        f"Pet Relocation {origin_name} to {dest_name} | Requirements & Guide",
        f"Shipping Dogs & Cats from {origin_name} to {dest_name} | PetTransportGlobal",
    ]
    # Rotate based on slug hash for consistent variation
    title = title_templates[hash(slug) % len(title_templates)]

    desc_templates = [
        f"Complete guide to pet transport from {origin_name} to {dest_name}. Import requirements, quarantine rules, airline options, and step-by-step timeline.",
        f"How to ship your dog or cat from {origin_name} to {dest_name}. {dest_name} import rules, vaccinations, permits, and airline options explained.",
        f"Pet relocation from {origin_name} to {dest_name}: {dest_name} import requirements, timeline, airlines, costs, and documentation checklist.",
    ]
    desc = desc_templates[hash(slug) % len(desc_templates)]
    # Ensure 140-160 chars
    if len(desc) > 160:
        desc = desc[:157] + "..."

    complexity, timeline, warnings = assess_route(dest_key)
    airlines = get_airlines_for_route(origin_key, dest_key)
    timeline_steps = build_timeline_steps(dest_key)
    cost_factors = build_cost_factors(dest_key)
    import_reqs = flatten_import_reqs(dest_key)
    export_reqs = flatten_export_reqs(origin_key)
    overview_text = generate_overview(origin_key, dest_key, complexity, timeline)
    sections = generate_sections(origin_key, dest_key, complexity)
    faqs = generate_faqs(origin_key, dest_key, complexity, timeline)

    def esc(s):
        """Escape double quotes for YAML inline strings."""
        return str(s).replace('"', "'")

    # Internal links
    origin_hub_url = f"/pet-transport/origins/{origin_slug}/"
    dest_country_url = f"/pet-transport/countries/{dest_slug}/"
    reverse_url = f"/pet-transport/{dest_slug}-to-{origin_slug}/"

    # Airline page links (first 2 relevant airlines)
    airline_links = []
    for a in airlines[:2]:
        a_name = a[0]
        a_slug = re.sub(r"[^a-z0-9]+", "-", a_name.lower()).strip("-")
        a_slug = a_slug.replace("(", "").replace(")", "").strip("-")
        airline_links.append({
            "url": f"/pet-transport/airlines/{a_slug}/",
            "text": f"{a_name} pet policy"
        })

    # Build YAML front matter
    md = f"""---
title: "{esc(title)}"
description: "{esc(desc)}"
type: "routes"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
origin_name: "{origin_name}"
destination_name: "{dest_name}"
route_data:
  origin:
    code: "{origin_code}"
    country: "{origin_name}"
    export_requirements:
"""

    for k, v in export_reqs.items():
        md += f'      {k}: "{esc(v)}"\n'

    md += f"""  destination:
    code: "{dest_code}"
    country: "{dest_name}"
    import_requirements:
"""

    for k, v in import_reqs.items():
        if v:
            md += f'      {k}: "{esc(v)}"\n'

    # Breed restrictions in route data
    bans = countries_raw.get(dest_key, {}).get("import_requirements", {}).get("banned_breeds", {})
    if isinstance(bans, dict) and bans.get("banned_types"):
        md += "    breed_restrictions:\n"
        for b in bans["banned_types"][:6]:
            md += f'      - "{esc(str(b))}"\n'

    # Airlines
    md += "  airlines:\n"
    for a_name, a_type, a_summary in airlines:
        md += f'    - name: "{esc(a_name)}"\n'
        md += f'      type: "{a_type}"\n'
        md += f'      policy_summary: "{esc(a_summary)}"\n'

    # Timeline steps
    md += "  timeline_steps:\n"
    for step in timeline_steps:
        md += f'    - step: {step["step"]}\n'
        md += f'      action: "{esc(step["action"])}"\n'
        md += f'      timing: "{esc(step["timing"])}"\n'
        md += f'      responsible: "{esc(step["responsible"])}"\n'

    # Cost factors
    md += "  cost_factors:\n"
    for cf in cost_factors:
        md += f'    - "{esc(cf)}"\n'

    # Warnings
    md += "  key_warnings:\n"
    for w in warnings:
        md += f'    - "{esc(w)}"\n'

    md += f'  route_complexity: "{complexity}"\n'
    md += f'  estimated_timeline_weeks: "{timeline}"\n'

    # Content
    h1 = f"Pet Transport from {origin_name} to {dest_name}"
    md += f'content:\n'
    md += f'  h1: "{esc(h1)}"\n'
    md += f'  overview: |\n'
    for line in overview_text.split("\n"):
        md += f'    {line}\n'

    if sections:
        md += "  sections:\n"
        for sec in sections:
            md += f'    - heading: "{esc(sec["heading"])}"\n'
            md += f'      body: |\n'
            for line in sec["body"].split("\n"):
                md += f'        {line}\n'

    # FAQs
    if faqs:
        md += "faqs:\n"
        for faq in faqs:
            md += f'  - question: "{esc(faq["question"])}"\n'
            md += f'    answer: "{esc(faq["answer"])}"\n'

    # Links
    md += "links:\n"
    md += "  sideways:\n"
    md += f'    - url: "{reverse_url}"\n'
    md += f'      text: "Pet Transport {dest_name} to {origin_name}"\n'
    md += "  upward:\n"
    md += f'    - url: "{origin_hub_url}"\n'
    md += f'      text: "Shipping from {origin_name}"\n'
    md += f'    - url: "{dest_country_url}"\n'
    md += f'      text: "Importing to {dest_name}"\n'
    for link in airline_links:
        md += f'    - url: "{link["url"]}"\n'
        md += f'      text: "{esc(link["text"])}"\n'

    md += "---\n"
    return md


# ============================================================
# MAIN — generate all routes
# ============================================================
def main():
    generated = 0
    skipped = 0
    errors = 0

    print(f"Generating P2 routes... {len(DEDUPED_ROUTES)} route pairs to process")

    for origin_key, dest_key in DEDUPED_ROUTES:
        # Validate both countries are in our registry
        if origin_key not in COUNTRY_REGISTRY or dest_key not in COUNTRY_REGISTRY:
            print(f"  SKIP (unknown country): {origin_key} -> {dest_key}")
            errors += 1
            continue

        origin_slug = COUNTRY_REGISTRY[origin_key][2]
        dest_slug = COUNTRY_REGISTRY[dest_key][2]
        filename = f"{origin_slug}-to-{dest_slug}.md"
        filepath = os.path.join(CONTENT_DIR, filename)

        # Skip if already exists (P1 routes, bonus routes)
        if os.path.exists(filepath):
            skipped += 1
            continue

        try:
            content = generate_route_markdown(origin_key, dest_key)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            generated += 1
            if generated % 25 == 0:
                print(f"  {generated} files written...")
        except Exception as e:
            print(f"  ERROR generating {filename}: {e}")
            errors += 1

    print(f"\nDone.")
    print(f"  Generated: {generated} new route files")
    print(f"  Skipped (already exist): {skipped} files")
    print(f"  Errors: {errors}")
    print(f"\nTotal route files now in {CONTENT_DIR}:")
    total = len([f for f in os.listdir(CONTENT_DIR) if f.endswith(".md") and f != "_index.md"])
    print(f"  {total} route pages")


if __name__ == "__main__":
    main()
