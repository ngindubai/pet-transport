"""
Block 12+13: Librarian Route Data Assembly
Assembles route-level JSON from country regs, airline policies, and breed restrictions.
Each output file matches the Hugo template variable format in routes/single.html.
"""
import json
import os
import re

DATA_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\data"
OUT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"

# Load source data
with open(os.path.join(DATA_DIR, "countries_pet_regulations.json"), "r", encoding="utf-8") as f:
    countries_raw = json.load(f)

with open(os.path.join(DATA_DIR, "airline_pet_policies.json"), "r", encoding="utf-8") as f:
    airlines_raw = json.load(f)

with open(os.path.join(DATA_DIR, "breed_restrictions.json"), "r", encoding="utf-8") as f:
    breeds_raw = json.load(f)

# Country name mapping (JSON keys -> display names + ISO codes)
COUNTRY_MAP = {
    "UK": {"code": "GB", "name": "United Kingdom", "key": "UK"},
    "USA": {"code": "US", "name": "United States", "key": "USA"},
    "UAE": {"code": "AE", "name": "United Arab Emirates", "key": "UAE"},
    "Australia": {"code": "AU", "name": "Australia", "key": "Australia"},
    "Canada": {"code": "CA", "name": "Canada", "key": "Canada"},
    "Germany": {"code": "DE", "name": "Germany", "key": "Germany"},
    "France": {"code": "FR", "name": "France", "key": "France"},
    "Singapore": {"code": "SG", "name": "Singapore", "key": "Singapore"},
    "Hong_Kong": {"code": "HK", "name": "Hong Kong", "key": "Hong_Kong"},
    "South_Africa": {"code": "ZA", "name": "South Africa", "key": "South_Africa"},
}

# Reverse lookup: code -> key
CODE_TO_KEY = {v["code"]: v["key"] for v in COUNTRY_MAP.values()}
CODE_TO_NAME = {v["code"]: v["name"] for v in COUNTRY_MAP.values()}

# Tier 1 Batch 1 (Block 12): 8 routes
BATCH_1 = [
    ("GB", "AU"), ("AE", "GB"), ("AE", "AU"), ("AE", "US"),
    ("AU", "GB"), ("HK", "GB"), ("HK", "AU"), ("GB", "AE"),
]

# Tier 1 Batch 2 (Block 13): 7 routes
BATCH_2 = [
    ("US", "GB"), ("US", "AU"), ("GB", "FR"), ("GB", "SG"),
    ("SG", "AU"), ("AU", "SG"), ("ZA", "AU"),
]

# Tier 1 Batch 3 (Block 19): remaining 74 P1 routes
BATCH_3 = [
    # GB missing (5)
    ("GB", "US"), ("GB", "CA"), ("GB", "DE"), ("GB", "HK"), ("GB", "ZA"),
    # US missing (7)
    ("US", "AE"), ("US", "CA"), ("US", "DE"), ("US", "FR"), ("US", "SG"), ("US", "HK"), ("US", "ZA"),
    # AE missing (6)
    ("AE", "CA"), ("AE", "DE"), ("AE", "FR"), ("AE", "SG"), ("AE", "HK"), ("AE", "ZA"),
    # AU missing (7)
    ("AU", "US"), ("AU", "AE"), ("AU", "CA"), ("AU", "DE"), ("AU", "FR"), ("AU", "HK"), ("AU", "ZA"),
    # CA all 9
    ("CA", "GB"), ("CA", "US"), ("CA", "AE"), ("CA", "AU"), ("CA", "DE"), ("CA", "FR"), ("CA", "SG"), ("CA", "HK"), ("CA", "ZA"),
    # DE all 9
    ("DE", "GB"), ("DE", "US"), ("DE", "AE"), ("DE", "AU"), ("DE", "CA"), ("DE", "FR"), ("DE", "SG"), ("DE", "HK"), ("DE", "ZA"),
    # FR missing (8)
    ("FR", "US"), ("FR", "AE"), ("FR", "AU"), ("FR", "CA"), ("FR", "DE"), ("FR", "SG"), ("FR", "HK"), ("FR", "ZA"),
    # SG missing (8)
    ("SG", "GB"), ("SG", "US"), ("SG", "AE"), ("SG", "CA"), ("SG", "DE"), ("SG", "FR"), ("SG", "HK"), ("SG", "ZA"),
    # HK missing (7)
    ("HK", "US"), ("HK", "AE"), ("HK", "CA"), ("HK", "DE"), ("HK", "FR"), ("HK", "SG"), ("HK", "ZA"),
    # ZA missing (8)
    ("ZA", "GB"), ("ZA", "US"), ("ZA", "AE"), ("ZA", "CA"), ("ZA", "DE"), ("ZA", "FR"), ("ZA", "HK"), ("ZA", "SG"),
]

ALL_ROUTES = BATCH_1 + BATCH_2 + BATCH_3


def get_country_data(code):
    """Get country regulations by ISO code."""
    key = CODE_TO_KEY.get(code)
    if not key:
        raise ValueError(f"Unknown country code: {code}")
    return countries_raw["countries"].get(key, {})


def flatten_import_reqs(country_data):
    """Extract import requirements as simple strings for template."""
    reqs = country_data.get("import_requirements", {})
    result = {}

    # Microchip
    mc = reqs.get("microchip", {})
    if isinstance(mc, dict):
        parts = []
        if mc.get("required"):
            parts.append(f"Required ({mc.get('standard', 'ISO 11784/11785')})")
        if mc.get("timing"):
            parts.append(mc["timing"])
        result["microchip"] = ". ".join(parts) if parts else "Required"
    elif mc:
        result["microchip"] = str(mc)

    # Rabies vaccination
    rv = reqs.get("rabies_vaccination", {})
    if isinstance(rv, dict):
        parts = []
        if rv.get("required"):
            parts.append("Required")
        if rv.get("minimum_age_weeks"):
            parts.append(f"Minimum age: {rv['minimum_age_weeks']} weeks")
        if rv.get("wait_after_first_vaccination_days"):
            parts.append(f"{rv['wait_after_first_vaccination_days']}-day wait after vaccination before travel")
        if rv.get("notes"):
            parts.append(rv["notes"])
        result["rabies_vaccination"] = ". ".join(parts) if parts else "Required"
    elif rv:
        result["rabies_vaccination"] = str(rv)

    # Titre test
    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict):
        parts = []
        if tt.get("required_for"):
            parts.append(f"Required for: {tt['required_for']}")
        elif tt.get("required") is True:
            parts.append("Required")
        if tt.get("not_required_for"):
            parts.append(f"Not required for: {tt['not_required_for']}")
        if tt.get("minimum_result"):
            parts.append(f"Minimum: {tt['minimum_result']}")
        if tt.get("wait_after_test_days"):
            parts.append(f"{tt['wait_after_test_days']}-day wait after blood draw")
        result["titre_test"] = ". ".join(parts) if parts else None
    elif tt:
        result["titre_test"] = str(tt)

    # Quarantine
    q = reqs.get("quarantine", {})
    if isinstance(q, dict):
        if q.get("required") is True or q.get("mandatory") is True:
            parts = ["Mandatory quarantine"]
            dur = q.get("duration_days") or q.get("minimum_days")
            if isinstance(dur, (int, float)):
                parts.append(f"{dur} days minimum")
            elif isinstance(dur, str) and dur:
                parts.append(dur)
            fac = q.get("facility")
            if isinstance(fac, dict):
                fac_name = fac.get("name", "")
                fac_loc = fac.get("location", "")
                if fac_name:
                    parts.append(f"Facility: {fac_name}")
                if fac_loc:
                    parts.append(f"Location: {fac_loc}")
            elif isinstance(fac, str) and fac:
                parts.append(f"Facility: {fac}")
            if q.get("notes"):
                parts.append(str(q["notes"]))
            result["quarantine"] = ". ".join(parts)
        elif q.get("required") is False:
            note = "No routine quarantine"
            if q.get("penalty_quarantine"):
                note += f". Penalty quarantine up to {q.get('penalty_duration_days', 'varies')} days if non-compliant"
            result["quarantine"] = note
        elif q.get("home_quarantine"):
            parts = []
            if q.get("home_quarantine", {}).get("duration_days"):
                parts.append(f"Home quarantine: {q['home_quarantine']['duration_days']} days for qualifying countries")
            if q.get("government_quarantine"):
                gq = q["government_quarantine"]
                parts.append(f"Government quarantine: {gq.get('duration_days', 'varies')} days for other countries")
            result["quarantine"] = ". ".join(parts) if parts else "Check requirements"
        else:
            result["quarantine"] = q.get("notes", "Check requirements")
    elif q:
        result["quarantine"] = str(q)

    # Import permit
    ip = reqs.get("import_permit", {})
    if isinstance(ip, dict):
        if ip.get("required") is True:
            parts = ["Required"]
            if ip.get("issued_by"):
                parts.append(f"Issued by: {ip['issued_by']}")
            if ip.get("lead_time"):
                parts.append(f"Lead time: {ip['lead_time']}")
            if ip.get("notes"):
                parts.append(ip["notes"])
            result["import_permit"] = ". ".join(parts)
        elif ip.get("required") is False:
            result["import_permit"] = ip.get("alternative", ip.get("notes", "Not required"))
        else:
            result["import_permit"] = ip.get("notes", "Check requirements")
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
        if hc.get("valid_for_entry_days"):
            parts.append(f"Valid for {hc['valid_for_entry_days']} days from issue")
        if hc.get("notes"):
            parts.append(hc["notes"])
        result["health_certificate"] = ". ".join(parts) if parts else "Required"
    elif hc:
        result["health_certificate"] = str(hc)

    return result


def flatten_export_reqs(country_data):
    """Extract export requirements as simple strings for template."""
    reqs = country_data.get("export_requirements", {})
    result = {}

    # Some countries have structured export reqs, others have nested (to_eu, to_non_eu)
    # Flatten to the most useful fields

    # Check for direct fields first
    if "export_permit" in reqs or "vet_inspection" in reqs or "endorsement" in reqs:
        if "export_permit" in reqs:
            ep = reqs["export_permit"]
            if isinstance(ep, dict):
                result["export_permit"] = ep.get("notes", str(ep))
            else:
                result["export_permit"] = str(ep)
        if "vet_inspection" in reqs:
            vi = reqs["vet_inspection"]
            if isinstance(vi, dict):
                result["vet_inspection"] = vi.get("notes", str(vi))
            else:
                result["vet_inspection"] = str(vi)
        if "endorsement" in reqs:
            en = reqs["endorsement"]
            if isinstance(en, dict):
                result["endorsement"] = en.get("notes", str(en))
            else:
                result["endorsement"] = str(en)
        return result

    # Handle nested structure (to_eu / to_non_eu)
    # Pick the more general one or combine
    for dest_type in ["to_non_eu", "to_eu", "general"]:
        sub = reqs.get(dest_type, {})
        if isinstance(sub, dict):
            for field in ["health_certificate", "export_permit", "endorsement", "vet_inspection"]:
                if field in sub and field not in result:
                    val = sub[field]
                    if isinstance(val, dict):
                        result[field] = val.get("notes", val.get("description", str(val)))
                    else:
                        result[field] = str(val)

    # If we still have nothing, try to extract from whatever structure exists
    if not result:
        for key, val in reqs.items():
            if isinstance(val, dict):
                notes = val.get("notes", val.get("description"))
                if notes:
                    result[key] = str(notes)
            elif isinstance(val, str):
                result[key] = val

    # Map to template fields
    mapped = {}
    if "export_permit" in result:
        mapped["export_permit"] = result["export_permit"]
    if "vet_inspection" in result:
        mapped["vet_inspection"] = result["vet_inspection"]
    if "endorsement" in result:
        mapped["endorsement"] = result["endorsement"]
    elif "health_certificate" in result:
        mapped["endorsement"] = result["health_certificate"]

    return mapped


def get_breed_restrictions(dest_code):
    """Get banned/restricted breed names for destination country."""
    key = CODE_TO_KEY.get(dest_code)
    if not key:
        return []
    country_breeds = breeds_raw.get("country_breed_restrictions", {}).get(key, {})

    breeds = []
    # Banned types
    for b in country_breeds.get("banned_types", []):
        if isinstance(b, dict):
            name = b.get("name", "")
            status = b.get("status", "banned")
            breeds.append(f"{name} ({status})")
        else:
            breeds.append(str(b))

    # Restricted breeds (if separate)
    for b in country_breeds.get("restricted_breeds", []):
        if isinstance(b, dict):
            name = b.get("name", "")
            status = b.get("status", "restricted")
            breeds.append(f"{name} ({status})")
        else:
            breeds.append(f"{b} (restricted)")

    return breeds


def get_airlines_for_route(origin_code, dest_code):
    """Find airlines that serve between origin and destination."""
    origin_name = CODE_TO_NAME.get(origin_code, "")
    dest_name = CODE_TO_NAME.get(dest_code, "")

    # Build search terms for route matching
    origin_terms = [origin_name.lower(), origin_code.lower()]
    dest_terms = [dest_name.lower(), dest_code.lower()]

    # Add city names for major hubs
    city_map = {
        "GB": ["london", "heathrow", "gatwick", "uk", "britain"],
        "AU": ["sydney", "melbourne", "australia"],
        "AE": ["dubai", "abu dhabi", "uae"],
        "US": ["new york", "los angeles", "usa", "jfk", "lax"],
        "HK": ["hong kong"],
        "FR": ["paris", "cdg", "france"],
        "SG": ["singapore", "changi"],
        "DE": ["frankfurt", "munich", "germany"],
        "CA": ["toronto", "vancouver", "canada"],
        "ZA": ["johannesburg", "cape town", "south africa"],
    }
    origin_terms.extend(city_map.get(origin_code, []))
    dest_terms.extend(city_map.get(dest_code, []))

    matched = []
    for airline_key, airline in airlines_raw.get("airlines", {}).items():
        # Check key_routes_p1 for route mentions
        routes = airline.get("key_routes_p1", [])
        route_str = " ".join(str(r).lower() for r in routes)

        serves_origin = any(t in route_str for t in origin_terms)
        serves_dest = any(t in route_str for t in dest_terms)

        # Also check hub location
        hub = str(airline.get("hub", "")).lower()
        hub_matches_origin = any(t in hub for t in origin_terms)
        hub_matches_dest = any(t in hub for t in dest_terms)

        if (serves_origin and serves_dest) or (hub_matches_origin and serves_dest) or (serves_origin and hub_matches_dest):
            # Build airline summary
            cargo = airline.get("cargo_policy", {})
            cabin = airline.get("cabin_policy", {})

            if cargo.get("allowed") and cabin.get("allowed"):
                atype = "cabin_and_cargo"
            elif cargo.get("allowed"):
                atype = "cargo_only"
            elif cabin.get("allowed"):
                atype = "cabin_only"
            else:
                atype = "check_policy"

            # Build policy summary
            summary_parts = []
            if cabin.get("allowed"):
                weight = cabin.get("max_weight_kg") or cabin.get("combined_weight_limit")
                if weight:
                    summary_parts.append(f"Cabin: pets up to {weight}kg (in carrier)")
                else:
                    summary_parts.append("Small pets allowed in cabin")
            if cargo.get("allowed"):
                if cargo.get("service"):
                    summary_parts.append(f"Cargo: {cargo['service']}")
                else:
                    summary_parts.append("Cargo transport available")
            if cargo.get("restrictions"):
                for r in cargo["restrictions"][:2]:  # First 2 restrictions
                    summary_parts.append(str(r))

            matched.append({
                "name": airline.get("name", airline_key.replace("_", " ").title()),
                "type": atype,
                "policy_summary": ". ".join(summary_parts) if summary_parts else "Contact airline for current pet policy.",
            })

    return matched


def get_route_complexity(origin_code, dest_code):
    """Determine route complexity based on destination strictness and route factors."""
    dest_data = get_country_data(dest_code)
    friendliness = dest_data.get("pet_friendliness", "moderate")

    complexity_map = {
        "easy": "low",
        "moderate": "moderate",
        "strict": "high",
        "very-strict": "very_high",
    }
    base = complexity_map.get(friendliness, "moderate")

    # Special cases
    if dest_code == "AU":
        base = "very_high"  # Australia is always high complexity
    if origin_code == "AE" and dest_code == "AU":
        base = "extreme"  # UAE to Australia may need transit country
    if origin_code == "AE" and dest_code == "US":
        base = "high"  # UAE is CDC high-risk country

    return base


def get_timeline_steps(origin_code, dest_code):
    """Generate step-by-step timeline for route."""
    dest_data = get_country_data(dest_code)
    origin_data = get_country_data(origin_code)
    import_reqs = dest_data.get("import_requirements", {})

    steps = []
    step_num = 1

    # Step 1: Microchip
    steps.append({
        "step": step_num,
        "action": "Get your pet microchipped (ISO 11784/11785)",
        "timing": "Before any vaccinations. Must be done first.",
        "responsible": "Your veterinarian"
    })
    step_num += 1

    # Step 2: Rabies vaccination
    rv = import_reqs.get("rabies_vaccination", {})
    wait = rv.get("wait_after_first_vaccination_days", 21)
    steps.append({
        "step": step_num,
        "action": "Rabies vaccination",
        "timing": f"At least {wait} days before travel (after microchip)",
        "responsible": "Your veterinarian"
    })
    step_num += 1

    # Step 3: Titre test (if required)
    tt = import_reqs.get("rabies_titre_test", {})
    titre_required = tt.get("required") is True or (
        tt.get("required_for") and "unlisted" not in str(tt.get("not_required_for", "")).lower()
    )
    # For AU, titre test is always required
    if dest_code == "AU" or titre_required:
        wait_days = tt.get("wait_after_test_days", 90)
        steps.append({
            "step": step_num,
            "action": "Rabies titre test (RNATT blood test)",
            "timing": f"Blood drawn 30+ days after vaccination. {wait_days}-day wait after successful result.",
            "responsible": "Your veterinarian + approved laboratory"
        })
        step_num += 1

    # Step 4: Import permit (if required)
    ip = import_reqs.get("import_permit", {})
    if ip.get("required") is True:
        lead = ip.get("lead_time", "Check with authorities")
        steps.append({
            "step": step_num,
            "action": f"Apply for import permit from {CODE_TO_NAME.get(dest_code, 'destination')}",
            "timing": f"Lead time: {lead}",
            "responsible": "You (or your pet transport agent)"
        })
        step_num += 1

    # Step 5: Tapeworm treatment (UK destination, dogs only)
    tw = import_reqs.get("tapeworm_treatment", {})
    if tw and tw.get("required_for"):
        steps.append({
            "step": step_num,
            "action": f"Tapeworm treatment ({tw.get('required_for', 'dogs')})",
            "timing": f"{tw.get('timing', '24-120 hours before arrival')}",
            "responsible": "Your veterinarian"
        })
        step_num += 1

    # Step 6: Health certificate
    steps.append({
        "step": step_num,
        "action": "Obtain health certificate / veterinary clearance",
        "timing": "Within 10 days of travel (check destination-specific requirements)",
        "responsible": "Official veterinarian"
    })
    step_num += 1

    # Step 7: Government endorsement (if applicable)
    export = origin_data.get("export_requirements", {})
    has_endorsement = False
    for sub in [export, export.get("to_non_eu", {}), export.get("to_eu", {}), export.get("general", {})]:
        if isinstance(sub, dict) and ("endorsement" in sub or "usda_endorsement" in sub):
            has_endorsement = True
            break
    if has_endorsement:
        steps.append({
            "step": step_num,
            "action": f"Government endorsement of health certificate ({CODE_TO_NAME.get(origin_code, 'origin')})",
            "timing": "After health certificate issued, before travel",
            "responsible": "Government veterinary authority"
        })
        step_num += 1

    # Step 8: Book airline
    steps.append({
        "step": step_num,
        "action": "Book IATA-compliant flight and arrange pet cargo/cabin booking",
        "timing": "2-4 weeks before travel. Confirm pet space availability.",
        "responsible": "You (or your pet transport agent)"
    })
    step_num += 1

    # Step 9: Travel day
    steps.append({
        "step": step_num,
        "action": "Travel day: arrive early, present all documentation",
        "timing": "3-4 hours before departure for cargo pets",
        "responsible": "You + airline cargo desk"
    })
    step_num += 1

    # Step 10: Quarantine (if applicable)
    q = import_reqs.get("quarantine", {})
    if q.get("required") is True or q.get("mandatory") is True:
        dur = q.get("duration_days") or q.get("minimum_days", "varies")
        steps.append({
            "step": step_num,
            "action": f"Quarantine on arrival ({dur} days)",
            "timing": "Immediately on arrival",
            "responsible": f"{CODE_TO_NAME.get(dest_code, 'Destination')} quarantine authorities"
        })
        step_num += 1

    return steps


def get_cost_factors(origin_code, dest_code):
    """Generate cost factor list for route."""
    factors = [
        "Airline cargo/cabin fees (varies by carrier, pet weight, and crate size)",
        "IATA-compliant travel crate (purchase or hire)",
        "Veterinary fees (vaccinations, health certificate, microchip)",
    ]

    dest_data = get_country_data(dest_code)
    import_reqs = dest_data.get("import_requirements", {})

    # Titre test cost
    tt = import_reqs.get("rabies_titre_test", {})
    if tt.get("required") is True or dest_code == "AU":
        factors.append("Rabies titre test (laboratory fee)")

    # Import permit cost
    ip = import_reqs.get("import_permit", {})
    if ip.get("required") is True:
        factors.append(f"Import permit application fee ({CODE_TO_NAME.get(dest_code, 'destination')})")

    # Quarantine cost
    q = import_reqs.get("quarantine", {})
    if q.get("required") is True or q.get("mandatory") is True:
        factors.append("Quarantine facility fees (owner-paid)")

    # Government endorsement
    factors.append("Government endorsement/USDA endorsement fee (if applicable)")

    # Agent fee (always relevant)
    factors.append("Pet transport agent fee (if using a relocation service)")

    return factors


def get_key_warnings(origin_code, dest_code):
    """Generate warnings specific to this route."""
    warnings = []
    dest_data = get_country_data(dest_code)
    origin_data = get_country_data(origin_code)
    import_reqs = dest_data.get("import_requirements", {})

    # Quarantine warnings
    q = import_reqs.get("quarantine", {})
    if q.get("required") is True or q.get("mandatory") is True:
        dur = q.get("duration_days") or q.get("minimum_days", "")
        dur_str = f" {dur} days minimum." if isinstance(dur, (int, float)) else ""
        warnings.append(f"Mandatory quarantine in {CODE_TO_NAME.get(dest_code, 'destination')}:{dur_str} Plan for separation from your pet.")

    # Brachycephalic warning
    warnings.append("Brachycephalic (flat-faced) breeds face cargo restrictions on most airlines. Check breed-specific policies before booking.")

    # Microchip timing
    warnings.append("Microchip MUST be implanted before rabies vaccination. Vaccination given before microchip is invalid and the clock restarts.")

    # Temperature embargoes
    if origin_code == "AE" or dest_code == "AE":
        warnings.append("Temperature embargoes apply during Gulf summer months (June to September). Airlines may refuse pet cargo when ground temperatures exceed 30C.")
    if dest_code == "AU" or origin_code == "AU":
        warnings.append("Australian airlines may restrict pet cargo during peak summer (December to February) when temperatures exceed safe thresholds.")

    # CDC high-risk
    if dest_code == "US" and origin_code in ("AE", "ZA"):
        warnings.append(f"{CODE_TO_NAME.get(origin_code)} is classified as a CDC high-risk country for dog rabies. Additional requirements apply: dogs must arrive at a CDC-registered animal care facility, have FAVN titre test results, and a CDC Dog Import Form.")

    # UK breed bans
    if dest_code == "GB":
        warnings.append("The UK enforces type-based breed bans under the Dangerous Dogs Act. Dogs resembling banned types (Pit Bull, Japanese Tosa, Dogo Argentino, Fila Brasileiro) may be seized regardless of pedigree documentation.")

    # Australia complexity
    if dest_code == "AU":
        warnings.append("Australia has the strictest pet import process globally. Expect a minimum 180-day preparation period. Pets can only enter through Melbourne (Mickleham quarantine facility).")

    # Penalty quarantine (UK)
    if dest_code == "GB":
        warnings.append("Arriving with incorrect documentation results in penalty quarantine of up to 4 months at the owner's expense.")

    return warnings


def get_estimated_timeline(origin_code, dest_code):
    """Estimate total timeline in weeks."""
    dest_data = get_country_data(dest_code)
    import_reqs = dest_data.get("import_requirements", {})

    base_weeks = 6  # Minimum for microchip + vaccination + 21-day wait

    # Titre test adds time
    tt = import_reqs.get("rabies_titre_test", {})
    if tt.get("required") is True or dest_code == "AU":
        wait = tt.get("wait_after_test_days", 90)
        base_weeks = max(base_weeks, (wait // 7) + 8)

    # Quarantine
    q = import_reqs.get("quarantine", {})
    if q.get("required") is True or q.get("mandatory") is True:
        dur = q.get("duration_days") or q.get("minimum_days", 10)
        if isinstance(dur, (int, float)):
            base_weeks += dur // 7

    # Australia special case
    if dest_code == "AU":
        base_weeks = max(base_weeks, 26)  # 6 months minimum

    return f"{base_weeks}-{base_weeks + 4}"


def build_route_data(origin_code, dest_code):
    """Assemble complete route data for one route."""
    origin_data = get_country_data(origin_code)
    dest_data = get_country_data(dest_code)

    route_data = {
        "origin": {
            "code": origin_code,
            "country": CODE_TO_NAME.get(origin_code, origin_code),
            "export_requirements": flatten_export_reqs(origin_data),
        },
        "destination": {
            "code": dest_code,
            "country": CODE_TO_NAME.get(dest_code, dest_code),
            "import_requirements": flatten_import_reqs(dest_data),
            "breed_restrictions": get_breed_restrictions(dest_code),
        },
        "airlines": get_airlines_for_route(origin_code, dest_code),
        "timeline_steps": get_timeline_steps(origin_code, dest_code),
        "cost_factors": get_cost_factors(origin_code, dest_code),
        "key_warnings": get_key_warnings(origin_code, dest_code),
        "route_complexity": get_route_complexity(origin_code, dest_code),
        "estimated_timeline_weeks": get_estimated_timeline(origin_code, dest_code),
    }

    return route_data


def build_page_data(origin_code, dest_code):
    """Build the full page data file that Hugo consumes."""
    origin_name = CODE_TO_NAME.get(origin_code, origin_code)
    dest_name = CODE_TO_NAME.get(dest_code, dest_code)

    page = {
        "origin_name": origin_name,
        "destination_name": dest_name,
        "route_data": build_route_data(origin_code, dest_code),
        "seo": {
            "title": f"Pet Transport from {origin_name} to {dest_name} | Complete Guide",
            "description": f"How to transport your dog or cat from {origin_name} to {dest_name}. Import requirements, airline options, costs, and step-by-step process.",
        },
        "content": {
            "h1": f"Pet Transport from {origin_name} to {dest_name}",
            "overview": "",
            "sections": [],
        },
        "faqs": [],
        "links": {
            "sideways": [],
            "upward": [],
        },
        "status": "draft",
        "version": 1,
        "updated_at": "2026-04-16",
    }

    return page


def slug_from_codes(origin_code, dest_code):
    """Generate filename slug from country codes."""
    origin_slug = CODE_TO_NAME.get(origin_code, origin_code).lower().replace(" ", "-")
    dest_slug = CODE_TO_NAME.get(dest_code, dest_code).lower().replace(" ", "-")
    return f"{origin_slug}-to-{dest_slug}"


# === MAIN ===
os.makedirs(OUT_DIR, exist_ok=True)

print(f"Assembling {len(ALL_ROUTES)} route data files...\n")

for origin, dest in ALL_ROUTES:
    slug = slug_from_codes(origin, dest)
    filename = f"{slug}.json"
    filepath = os.path.join(OUT_DIR, filename)

    page_data = build_page_data(origin, dest)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)

    airlines_count = len(page_data["route_data"]["airlines"])
    complexity = page_data["route_data"]["route_complexity"]
    timeline = page_data["route_data"]["estimated_timeline_weeks"]
    warnings_count = len(page_data["route_data"]["key_warnings"])
    print(f"  {filename}")
    print(f"    Airlines: {airlines_count} | Complexity: {complexity} | Timeline: {timeline} weeks | Warnings: {warnings_count}")

print(f"\nDone. {len(ALL_ROUTES)} route data files written to {OUT_DIR}")
