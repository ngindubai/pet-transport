"""
Generate Task 3.3 Resource Pages:
1. quarantine-countries.md      — which countries require pet quarantine + duration
2. breed-bans-by-country.md     — breed restrictions reference table
3. rabies-free-countries.md     — rabies status map + what it means for pet owners
Reads from data/ JSON files. Skip-if-exists.
"""
import json
import os
from datetime import date

RESOURCES_DIR = os.path.join("site", "content", "resources")
TODAY = date.today().isoformat()  # 2026-04-30


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ─────────────────────────────────────────────
# 1. QUARANTINE COUNTRIES PAGE
# ─────────────────────────────────────────────

def generate_quarantine_page(countries_data):
    quarantine_countries = {}
    for key, v in countries_data.items():
        q = v.get("import_requirements", {}).get("quarantine", {})
        if q.get("required", False):
            quarantine_countries[key] = {
                "name": v.get("country_name", key),
                "quarantine": q,
                "region": v.get("region", ""),
            }

    rows = []
    # Sort by country name
    for key, info in sorted(quarantine_countries.items(), key=lambda x: x[1]["name"]):
        q = info["quarantine"]
        name = info["name"]
        duration = (
            q.get("typical_duration_days")
            or q.get("duration_days")
            or q.get("duration_days_group1", "see notes")
        )
        if isinstance(duration, int):
            duration = f"{duration} days"
        facility = q.get("facility", {})
        if isinstance(facility, dict):
            facility_name = facility.get("name", "Government facility")
        else:
            facility_name = str(facility)
        notes = q.get("notes", "")
        cost = q.get("cost_estimate_aud") or q.get("cost_responsibility", "Owner pays")
        rows.append(f"| **{name}** | {duration} | {facility_name} | {cost} | {notes[:120] if notes else '-'} |")

    table = "\n".join(rows)

    content = f"""---
title: "Countries That Require Pet Quarantine | International Pet Transport Guide"
description: "Which countries require quarantine for imported pets, how long it lasts, where it happens, and what it costs. Updated {TODAY}."
date: "{TODAY}"
lastmod: "{TODAY}"
layout: "single"
faqs:
  - q: "Which countries have the longest pet quarantine?"
    a: "Australia, Thailand, Philippines, Malaysia, India, Brazil, Indonesia and China all impose 30-day quarantines. Taiwan can be up to 180 days for pets from non-approved countries. Japan requires 14 days."
  - q: "Can quarantine be avoided?"
    a: "In most countries, no — it is mandatory. However, the length can sometimes be reduced by meeting all pre-arrival requirements (microchip, vaccinations, titre test) and flying via an approved route. Australia's quarantine cannot be shortened regardless of documentation."
  - q: "Who pays for pet quarantine?"
    a: "The pet owner pays all quarantine costs in every country that requires it. Costs range from a few hundred dollars (South Korea) to AUD 4,000+ (Australia). Always budget for quarantine when planning an international move."
  - q: "Do cats and dogs have different quarantine rules?"
    a: "In some countries yes. China typically requires 30 days for dogs but 7 days for cats from approved countries. Taiwan's duration depends on the origin country group, not the species."
  - q: "What happens to my pet during quarantine?"
    a: "Your pet is housed at a government-approved facility where it is monitored for signs of disease. In Australia, dedicated biosecurity officers manage the facility. In most countries, the pet receives basic care; owners may visit on approved days. Veterinary treatment, if needed, is typically at the owner's expense."
---

Countries that require **mandatory pet quarantine** on arrival present the biggest planning challenge in international pet transport. Unlike paperwork delays, quarantine cannot be fast-tracked — your pet will spend days or weeks in a government facility regardless of how perfect your documents are.

This page covers every country in our database that imposes quarantine, including duration, facility, and cost estimates. All data is sourced from official government veterinary authorities.

## Why Some Countries Require Quarantine

Quarantine protects national biosecurity. Countries that are rabies-free (or have eradicated specific diseases) use mandatory isolation to catch any incubating illness before it can spread. Australia is the clearest example: it is one of the world's most disease-free nations and uses quarantine as a non-negotiable last line of defence.

Countries with endemic rabies or other livestock diseases tend to use documentation requirements (vaccinations, titre tests) rather than physical quarantine — though there are exceptions.

## Countries Requiring Pet Quarantine

| Country | Duration | Quarantine Facility | Cost Responsibility | Notes |
|---------|----------|--------------------|--------------------|-------|
{table}

*Data compiled from official government veterinary portals. Always verify current rules directly with the destination country's authority before travel.*

## Planning Around Quarantine

**Book early.** Australia's Mickleham facility has limited spaces and must be booked months in advance. Japan's MAFF stations also require advance reservation.

**Timing matters.** Australia issues heat stress warnings for December-February arrivals. Brachycephalic breeds (flat-faced dogs and cats) face heightened risk in warm-weather quarantine. Consider scheduling arrivals in cooler months.

**Pre-travel prep reduces risk.** While quarantine duration is fixed, having all documentation correct on arrival prevents your pet being held for additional inspection or refused entry.

**Budget realistically.** Australia's quarantine costs AUD 2,000-4,000+. Add flights, transport to the facility, and ongoing veterinary costs if your pet needs treatment during the stay.

## Country-Specific Notes

### Australia
All dogs and cats entering Australia must complete quarantine at the **Mickleham Post Entry Quarantine Facility** near Melbourne, regardless of origin country. The minimum stay is 10 days; some arrivals spend up to 30 days. The facility is closed on weekends and public holidays — arrival dates must be planned around this. Summer arrivals (December-February) carry significant heatstroke risk for brachycephalic, elderly, or overweight animals.

### Japan
Japan requires a 14-day quarantine at a **MAFF-designated station**. Dogs and cats arriving with fully compliant rabies titre test results and documentation from approved countries face a standard 14-day hold. Non-compliant paperwork triggers a 180-day hold — Japan's regulatory framework is strict and unforgiving of documentation errors.

### Taiwan
Taiwan's quarantine duration depends on the **origin country group** as classified by BAPHIQ. Group 1 countries (US, UK, EU, Australia, New Zealand, Japan, Singapore) typically face 7-day quarantine. Group 2 countries face 21 days. Pets from non-approved countries or those without a valid titre test face up to 180 days.

### China
Dogs typically face **30 days** at a GACC-approved facility. Cats from approved countries may be eligible for 7-day quarantine. Rules change periodically — always check with the General Administration of Customs China (GACC) before planning travel.

### South Korea
South Korea imposes a **10-day quarantine** managed by APQA. Costs are owner-paid and relatively modest compared to Australia or Japan.

### Israel
Israel's "quarantine" is more accurately described as a **1-3 day inspection hold** at Ben Gurion Airport Quarantine Station. Pets with compliant documentation are released after inspection. Non-compliant pets may be held longer or refused entry.

---

*Sources: Australian DAFF, Japan MAFF, Taiwan BAPHIQ, China GACC, South Korea APQA, Philippines BAI, Malaysia DVS, India AQCS, Brazil MAPA, Indonesia Directorate of Animal Health, Israel Veterinary Services. Data current as of {TODAY}.*
"""
    return content


# ─────────────────────────────────────────────
# 2. BREED BANS BY COUNTRY PAGE
# ─────────────────────────────────────────────

def generate_breed_bans_page(breed_data):
    restrictions = breed_data.get("country_breed_restrictions", {})
    airline_data = breed_data.get("airline_brachycephalic_restrictions", {})
    matrix = breed_data.get("common_restricted_breed_matrix", {})

    # Build breed matrix table
    breed_rows = []
    breed_display = {
        "pit_bull_terrier": "Pit Bull Terrier",
        "japanese_tosa": "Japanese Tosa",
        "dogo_argentino": "Dogo Argentino",
        "fila_brasileiro": "Fila Brasileiro",
        "rottweiler": "Rottweiler",
        "american_staffordshire": "American Staffordshire",
        "dobermann": "Dobermann",
        "xl_bully": "XL Bully",
    }
    for key, display in breed_display.items():
        info = matrix.get(key, {})
        banned = ", ".join(info.get("banned_from_import", ["-"])) or "-"
        restricted = ", ".join(info.get("restricted", ["-"])) or "-"
        breed_rows.append(f"| **{display}** | {banned} | {restricted} |")
    breed_table = "\n".join(breed_rows)

    # Build per-country section
    country_sections = []
    for country_key, info in sorted(restrictions.items()):
        country_name = {
            "UK": "United Kingdom", "USA": "United States", "UAE": "United Arab Emirates",
            "Australia": "Australia", "Canada": "Canada", "Germany": "Germany",
            "France": "France", "Singapore": "Singapore", "Hong_Kong": "Hong Kong",
            "South_Africa": "South Africa",
        }.get(country_key, country_key)
        severity = info.get("severity", "")
        legislation = info.get("legislation", "")
        banned = info.get("banned_types", [])
        banned_list = "\n".join(f"- **{b.get('name', b)}** — {b.get('exemption', 'No import allowed')}" for b in banned) if banned else "- No national breed-specific import ban"
        notes = info.get("notes", "")
        source = info.get("source_url", "")
        country_sections.append(f"""
### {country_name}

**Legislation:** {legislation}  
**Restriction level:** {severity.replace("_", " ").title()}

**Banned breeds / types:**
{banned_list}

{notes}

{f'[Official source]({source})' if source else ''}
""")

    countries_content = "\n".join(country_sections)

    # Airlines brachycephalic section
    airline_policies = airline_data.get("airline_policies", {})
    airline_rows = []
    # complete cargo ban airlines
    for airline in airline_policies.get("complete_cargo_ban", {}).get("airlines", []):
        airline_rows.append(f"| **{airline}** | Allowed if fits under seat | **Banned from cargo** | All brachycephalic breeds |")
    # seasonal or conditional restrictions
    for airline in airline_policies.get("seasonal_embargo", {}).get("airlines", []):
        months = airline_policies.get("seasonal_embargo", {}).get("embargo_months", "summer months")
        airline_rows.append(f"| **{airline}** | Allowed if fits under seat | Banned in cargo during {months} | Brachycephalic breeds |")
    # If no rows found, add a note
    if not airline_rows:
        airline_rows = ["| See airline policies | Check direct with airline | Check direct with airline | All brachycephalic breeds |"]
    airline_table = "\n".join(airline_rows)

    content = f"""---
title: "Dog Breed Bans and Restrictions by Country | Pet Import Rules"
description: "Which dog breeds are banned from import in which countries, plus airline brachycephalic policies. Essential reading before booking international pet transport. Updated {TODAY}."
date: "{TODAY}"
lastmod: "{TODAY}"
layout: "single"
faqs:
  - q: "Which countries ban Pit Bull Terriers?"
    a: "The UK, Germany, Singapore, Hong Kong, and France (for unregistered dogs) all ban Pit Bull Terriers from import. The breed is also restricted in the UAE, parts of Canada, and parts of France."
  - q: "Can I bring my Rottweiler to Germany?"
    a: "Rottweilers are classed as a Category 2 dangerous dog in some German states (Bundeslaender), requiring a permit, liability insurance, and sometimes a behaviour assessment. Rules vary by state — check with the relevant German authority before travel."
  - q: "Are breed bans based on pedigree or appearance?"
    a: "The UK uses a type-based assessment: any dog that substantially conforms to the physical characteristics of a banned breed can be classified as that breed, regardless of pedigree or registration. Other countries use registered breed names."
  - q: "What about mixed-breed dogs with banned ancestry?"
    a: "In the UK, crosses of banned types are also prohibited. In most other countries, rules apply to dogs registered as the specific banned breed. However, customs officers have discretion — dogs with obvious physical characteristics of a banned type may be questioned."
  - q: "Which airlines ban flat-faced breeds in cargo?"
    a: "Many major airlines ban brachycephalic breeds from cargo holds, including Lufthansa, British Airways, and others. Check the airline section below. Policies change frequently — always verify directly with the airline before booking."
---

Breed-specific legislation is one of the most emotionally difficult parts of international pet transport. Owners of banned breeds face either re-homing their dog or restructuring their entire move. This page covers every country in our database with specific breed restrictions, plus airline brachycephalic policies.

**Always verify current rules with the destination country's official veterinary authority before travel.** Laws change, exemptions are granted and revoked, and country-specific court rulings can affect what's enforceable at the border.

## Breed Restriction Quick Reference Matrix

The table below shows which commonly restricted breeds are banned or restricted across our P1 country database.

| Breed | Banned from Import | Restricted (permit/conditions) |
|-------|-------------------|-------------------------------|
{breed_table}

*Sources: UK Dangerous Dogs Act 1991, German Tierschutzgesetz and Bundeslaender BSL, Singapore Animals and Birds Act, Hong Kong Dangerous Dogs Regulations, France Decree 99-1164.*

## Country-by-Country Breed Rules
{countries_content}

## Airline Brachycephalic Policies

Flat-faced (brachycephalic) breeds face breathing difficulties at altitude, especially in cargo. Many airlines have tightened or removed their cargo policies for these breeds.

| Airline | Cabin Policy | Cargo Policy | Specific Banned Breeds |
|---------|-------------|-------------|----------------------|
{airline_table}

*Airline policies change frequently. Always confirm directly with the airline at the time of booking.*

### Which Breeds Are Brachycephalic?

**Dogs:** English Bulldog, French Bulldog, Pug, Boston Terrier, Boxer, Cavalier King Charles Spaniel, Shih Tzu, Lhasa Apso, Chow Chow, Pekinese, Shar Pei, Affenpinscher, Bullmastiff

**Cats:** Persian, Himalayan, Burmese, British Shorthair, Scottish Fold, Exotic Shorthair

If your pet is brachycephalic, discuss travel fitness with your vet before booking any flight. Some vets issue fitness-to-fly certificates; others will advise against air travel entirely for severely affected animals.

---

*Data current as of {TODAY}. Sources: UK Home Office, German Federal Ministry of Food and Agriculture, Singapore AVS, Hong Kong AFCD, France Ministry of Agriculture, airline published policies.*
"""
    return content


# ─────────────────────────────────────────────
# 3. RABIES-FREE COUNTRIES PAGE
# ─────────────────────────────────────────────

def generate_rabies_page(countries_data):
    # Group countries by rabies status
    groups = {
        "rabies-free": [],
        "rabies-controlled": [],
        "present": [],
        "rabies-endemic": [],
    }
    for key, v in countries_data.items():
        name = v.get("country_name", key)
        status = v.get("rabies_status", "unknown")
        # Normalise
        s = status.lower()
        if "free" in s:
            cat = "rabies-free"
        elif "controlled" in s:
            cat = "rabies-controlled"
        elif "endemic" in s:
            cat = "rabies-endemic"
        else:
            cat = "present"
        groups[cat].append(name)

    def country_list(names):
        return "\n".join(f"- {n}" for n in sorted(names))

    free_list = country_list(groups["rabies-free"])
    controlled_list = country_list(groups["rabies-controlled"])
    present_list = country_list(groups["present"])
    endemic_list = country_list(groups["rabies-endemic"])

    content = f"""---
title: "Rabies-Free Countries | Pet Import Requirements and Travel Guide"
description: "Which countries are officially rabies-free, which are controlled, and what that means for importing your pet. Titre test requirements and quarantine implications. Updated {TODAY}."
date: "{TODAY}"
lastmod: "{TODAY}"
layout: "single"
faqs:
  - q: "Which countries are officially rabies-free?"
    a: "Among the countries in our database: UK, Ireland, Germany, France, Netherlands, Belgium, Austria, Denmark, Switzerland, Italy, Portugal, Spain, Norway, Sweden, Czech Republic, Malta, Cyprus, Singapore, Hong Kong, Australia, New Zealand, Japan, Taiwan, and Chile are all considered rabies-free or have achieved rabies elimination in domestic animals. Always check the current OIE/WOAH status before travel."
  - q: "What is a rabies titre test and when do I need one?"
    a: "A rabies titre test (also called FAVN or RFFIT) measures the level of rabies antibodies in your pet's blood. It proves the rabies vaccination has been effective. Rabies-free countries like Australia, UK, Japan, New Zealand, and Singapore require a titre test result above a minimum threshold (typically 0.5 IU/mL) before your pet can enter."
  - q: "How far in advance do I need the titre test?"
    a: "For most rabies-free countries, the titre test must be taken at least 3 months before travel — and in some cases the waiting period starts from the date of a satisfactory result. For Australia, the titre test is part of a 6-month pre-travel preparation period. Start planning at least 6 months ahead for rabies-free destinations."
  - q: "Does travelling from a rabies-free country make import easier?"
    a: "Generally yes. If you are travelling from a country that is also rabies-free (for example, UK to New Zealand), some waiting periods and titre test requirements may be reduced or waived. The key factor is the rabies status of your pet's country of residence, not country of birth."
  - q: "What does endemic rabies mean for my pet?"
    a: "If you are moving your pet TO a country with endemic rabies, it typically means fewer import restrictions — those countries are already managing rabies domestically. However, if you are moving FROM an endemic country TO a rabies-free destination, expect strict requirements: titre tests, extended waiting periods, and possibly quarantine."
---

Rabies status is the single most important factor in determining how hard it is to import a pet into any given country. Rabies-free nations protect their status aggressively — expect titre tests, waiting periods, and quarantine. Countries with endemic rabies tend to have simpler import paperwork for incoming pets.

This page explains the four rabies status categories used across our 50-country database, lists which countries fall into each, and explains what each status means for your pet's travel preparation.

## The Four Rabies Status Categories

**Rabies-free** — No confirmed cases in domestic animals or wildlife for a sustained period. Recognised by WOAH (formerly OIE). These countries impose the strictest import requirements to stay that way.

**Rabies-controlled** — Rabies exists or existed but is managed through vaccination programmes. Not fully eliminated, but risk is low and monitored. Import requirements are typically moderate.

**Rabies present** — Rabies is present but not necessarily described as endemic. Some countries use this classification for ongoing but limited transmission.

**Rabies-endemic** — Rabies is a known, ongoing public health concern. Dog-mediated rabies is present and widespread. These countries focus on domestic control programmes.

---

## Rabies-Free Countries

These countries are officially recognised as rabies-free (in domestic dogs and cats). Importing a pet here typically requires a **rabies titre test** with a result of at least **0.5 IU/mL**, taken at an approved laboratory, with a mandatory waiting period.

{free_list}

### Key requirements when importing into rabies-free countries

- **Microchip** implanted before vaccination (mandatory)
- **Rabies vaccination** by a licensed vet
- **Titre test** at an approved laboratory (not all labs are accepted — check the destination country's approved lab list)
- **Waiting period** of 3-6 months from a satisfactory titre test result
- **Health certificate** issued by a government-authorised vet close to departure

---

## Rabies-Controlled Countries

Rabies is managed or effectively eliminated in domestic animals, but not fully certified free. Import requirements are typically moderate — vaccinations and a health certificate are standard; titre tests may or may not be required.

{controlled_list}

---

## Countries Where Rabies Is Present

Rabies is present but import documentation focuses on vaccination status rather than titre testing.

{present_list}

---

## Rabies-Endemic Countries

Rabies is an ongoing concern. Dog-mediated rabies transmission occurs. Domestic control programmes are active. Moving a pet FROM these countries to rabies-free destinations triggers the strictest requirements.

{endemic_list}

---

## The Titre Test: What You Need to Know

The **Fluorescent Antibody Virus Neutralisation (FAVN) test** or **Rapid Fluorescent Focus Inhibition Test (RFFIT)** measures rabies antibodies in your pet's blood. Most rabies-free countries require:

- A result of **at least 0.5 IU/mL**
- The test must be performed at an **OIE-approved or nationally approved laboratory**
- Blood must be taken **after** vaccination, not before
- A waiting period applies from the date of a satisfactory result — typically **3 months** for the UK, EU, and New Zealand; **180 days** for Japan (or 14 days if the titre test was done before the pet left its previous country and results were sufficient)

**Approved laboratories** include:

- **UK:** APHA Weybridge, approved private labs
- **USA:** Kansas State University Veterinary Diagnostic Laboratory
- **EU:** OIE reference laboratories (France, Germany, UK)
- **Australia:** CSIRO AAHL, approved state labs
- **Japan:** National Institute of Infectious Diseases, approved labs

Always check the destination country's current approved lab list — it changes, and a test from a non-approved lab will not be accepted.

## Travelling Between Rabies-Free Countries

If your pet is moving from one rabies-free country to another, requirements are often reduced:

| Route | Typical Simplification |
|-------|----------------------|
| UK to Ireland | No titre test required (same travel area) |
| EU to EU | Pet passport or health certificate; no titre test |
| UK/EU to New Zealand | Titre test required but waiting period may be shorter from approved low-risk countries |
| UK/EU to Australia | Full titre test + 6-month preparation regardless of origin |
| EU/UK to Japan | Titre test + waiting period; duration depends on when titre was taken |

Japan and Australia do not simplify requirements based on the origin country's rabies-free status — all imports go through the same process.

---

*Sources: WOAH (World Organisation for Animal Health) rabies status data; APHA UK, Australian DAFF, Japan MAFF, New Zealand MPI, Singapore AVS, Taiwan BAPHIQ. Data current as of {TODAY}.*
"""
    return content


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    countries_data = load_json("data/countries_pet_regulations.json")["countries"]
    breed_data = load_json("data/breed_restrictions.json")

    pages = [
        ("quarantine-countries.md", generate_quarantine_page(countries_data)),
        ("breed-bans-by-country.md", generate_breed_bans_page(breed_data)),
        ("rabies-free-countries.md", generate_rabies_page(countries_data)),
    ]

    os.makedirs(RESOURCES_DIR, exist_ok=True)

    for filename, content in pages:
        filepath = os.path.join(RESOURCES_DIR, filename)
        if os.path.exists(filepath):
            print(f"  SKIP (exists): {filename}")
            continue
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  + {filename}")

    print(f"\nDone. {len(pages)} resource pages processed.")


if __name__ == "__main__":
    main()
