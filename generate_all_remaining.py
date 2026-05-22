"""
generate_all_remaining.py
=========================
Auto-generates ALL remaining route pages for PetTransportGlobal.
Covers all 198 countries in the build plan, handling ~33,500 unbuilt pairs.

Usage:
  python generate_all_remaining.py               # generate everything
  python generate_all_remaining.py --batch 500   # generate next 500 only
  python generate_all_remaining.py --tier A      # only tier A routes
  python generate_all_remaining.py --tier B,C    # tier B and C routes
  python generate_all_remaining.py --dry-run     # show what would be built

Imports core route generation logic from generate_p3_routes_batch1.py.
Extends COUNTRY_REGISTRY with all 198 countries.
Skip-if-exists: safe to run multiple times.
"""

import os
import sys
import math
import argparse

# ---------------------------------------------------------------------------
# Import core generation machinery from existing script
# ---------------------------------------------------------------------------
from generate_p3_routes_batch1 import (
    COUNTRY_REGISTRY,
    ORIGIN_HUB_URLS,
    CONTENT_DIR,
    generate_route_markdown,
)
from generate_p4_routes_auto import P4_EXTENSIONS, P4_HUB_URLS

# Apply P4 extensions (idempotent)
for k, v in P4_EXTENSIONS.items():
    if k not in COUNTRY_REGISTRY:
        COUNTRY_REGISTRY[k] = v
ORIGIN_HUB_URLS.update(P4_HUB_URLS)

# ---------------------------------------------------------------------------
# EXTENDED COUNTRY REGISTRY
# All countries not yet in P1-P4 registry (format: Name -> (Name, ISO2, slug))
# ---------------------------------------------------------------------------
EXTENDED_COUNTRIES = {
    # Eastern Europe / Former Soviet
    "Ukraine":              ("Ukraine",              "UA", "ukraine"),
    "Russia":               ("Russia",               "RU", "russia"),
    "Belarus":              ("Belarus",              "BY", "belarus"),
    "Moldova":              ("Moldova",              "MD", "moldova"),
    "Georgia":              ("Georgia",              "GE", "georgia"),
    "Armenia":              ("Armenia",              "AM", "armenia"),
    "Azerbaijan":           ("Azerbaijan",           "AZ", "azerbaijan"),
    "Kazakhstan":           ("Kazakhstan",           "KZ", "kazakhstan"),
    "Uzbekistan":           ("Uzbekistan",           "UZ", "uzbekistan"),
    "Kyrgyzstan":           ("Kyrgyzstan",           "KG", "kyrgyzstan"),
    "Tajikistan":           ("Tajikistan",           "TJ", "tajikistan"),
    "Turkmenistan":         ("Turkmenistan",         "TM", "turkmenistan"),
    "Latvia":               ("Latvia",               "LV", "latvia"),
    "Lithuania":            ("Lithuania",            "LT", "lithuania"),
    "Estonia":              ("Estonia",              "EE", "estonia"),
    "Albania":              ("Albania",              "AL", "albania"),
    "Kosovo":               ("Kosovo",               "XK", "kosovo"),
    "North_Macedonia":      ("North Macedonia",      "MK", "north-macedonia"),
    "Montenegro":           ("Montenegro",           "ME", "montenegro"),
    "Bosnia":               ("Bosnia and Herzegovina", "BA", "bosnia-and-herzegovina"),
    "Slovenia":             ("Slovenia",             "SI", "slovenia"),
    "Iceland":              ("Iceland",              "IS", "iceland"),
    # Middle East / North Africa
    "Iran":                 ("Iran",                 "IR", "iran"),
    "Iraq":                 ("Iraq",                 "IQ", "iraq"),
    "Syria":                ("Syria",                "SY", "syria"),
    "Lebanon":              ("Lebanon",              "LB", "lebanon"),
    "Yemen":                ("Yemen",                "YE", "yemen"),
    "Palestinian":          ("Palestinian Territories", "PS", "palestinian-territories"),
    "Libya":                ("Libya",                "LY", "libya"),
    "Algeria":              ("Algeria",              "DZ", "algeria"),
    "Tunisia":              ("Tunisia",              "TN", "tunisia"),
    "Sudan":                ("Sudan",                "SD", "sudan"),
    "South_Sudan":          ("South Sudan",          "SS", "south-sudan"),
    # Sub-Saharan Africa
    "Senegal":              ("Senegal",              "SN", "senegal"),
    "Ivory_Coast":          ("Ivory Coast",          "CI", "ivory-coast"),
    "Cameroon":             ("Cameroon",             "CM", "cameroon"),
    "Angola":               ("Angola",               "AO", "angola"),
    "Mozambique":           ("Mozambique",           "MZ", "mozambique"),
    "Namibia":              ("Namibia",              "NA", "namibia"),
    "Botswana":             ("Botswana",             "BW", "botswana"),
    "Zambia":               ("Zambia",               "ZM", "zambia"),
    "Malawi":               ("Malawi",               "MW", "malawi"),
    "Lesotho":              ("Lesotho",              "LS", "lesotho"),
    "Eswatini":             ("Eswatini",             "SZ", "eswatini"),
    "Gabon":                ("Gabon",                "GA", "gabon"),
    "Republic_Congo":       ("Republic of Congo",    "CG", "republic-of-congo"),
    "DR_Congo":             ("DR Congo",             "CD", "dr-congo"),
    "Rwanda":               ("Rwanda",               "RW", "rwanda"),
    "Burundi":              ("Burundi",              "BI", "burundi"),
    "Uganda":               ("Uganda",               "UG", "uganda"),
    "Mali":                 ("Mali",                 "ML", "mali"),
    "Burkina_Faso":         ("Burkina Faso",         "BF", "burkina-faso"),
    "Niger":                ("Niger",                "NE", "niger"),
    "Chad":                 ("Chad",                 "TD", "chad"),
    "Togo":                 ("Togo",                 "TG", "togo"),
    "Benin":                ("Benin",                "BJ", "benin"),
    "Liberia":              ("Liberia",              "LR", "liberia"),
    "Sierra_Leone":         ("Sierra Leone",         "SL", "sierra-leone"),
    "Guinea":               ("Guinea",               "GN", "guinea"),
    "Guinea_Bissau":        ("Guinea-Bissau",        "GW", "guinea-bissau"),
    "Gambia":               ("Gambia",               "GM", "gambia"),
    "Cabo_Verde":           ("Cabo Verde",           "CV", "cabo-verde"),
    "Sao_Tome":             ("Sao Tome and Principe","ST", "sao-tome-and-principe"),
    "Equatorial_Guinea":    ("Equatorial Guinea",    "GQ", "equatorial-guinea"),
    "Central_African":      ("Central African Republic", "CF", "central-african-republic"),
    "Djibouti":             ("Djibouti",             "DJ", "djibouti"),
    "Eritrea":              ("Eritrea",              "ER", "eritrea"),
    "Somalia":              ("Somalia",              "SO", "somalia"),
    "Comoros":              ("Comoros",              "KM", "comoros"),
    "Madagascar":           ("Madagascar",           "MG", "madagascar"),
    "Seychelles":           ("Seychelles",           "SC", "seychelles"),
    # Caribbean / Central America
    "Jamaica":              ("Jamaica",              "JM", "jamaica"),
    "Trinidad":             ("Trinidad and Tobago",  "TT", "trinidad-and-tobago"),
    "Barbados":             ("Barbados",             "BB", "barbados"),
    "Dominican_Republic":   ("Dominican Republic",   "DO", "dominican-republic"),
    "Haiti":                ("Haiti",                "HT", "haiti"),
    "Cuba":                 ("Cuba",                 "CU", "cuba"),
    "Bahamas":              ("Bahamas",              "BS", "bahamas"),
    "Grenada":              ("Grenada",              "GD", "grenada"),
    "Dominica":             ("Dominica",             "DM", "dominica"),
    "Saint_Lucia":          ("Saint Lucia",          "LC", "saint-lucia"),
    "Saint_Vincent":        ("Saint Vincent and the Grenadines", "VC", "saint-vincent-and-the-grenadines"),
    "Saint_Kitts":          ("Saint Kitts and Nevis","KN", "saint-kitts-and-nevis"),
    "Antigua":              ("Antigua and Barbuda",  "AG", "antigua-and-barbuda"),
    "Guatemala":            ("Guatemala",            "GT", "guatemala"),
    "Honduras":             ("Honduras",             "HN", "honduras"),
    "El_Salvador":          ("El Salvador",          "SV", "el-salvador"),
    "Nicaragua":            ("Nicaragua",            "NI", "nicaragua"),
    "Belize":               ("Belize",               "BZ", "belize"),
    # South America
    "Uruguay":              ("Uruguay",              "UY", "uruguay"),
    "Paraguay":             ("Paraguay",             "PY", "paraguay"),
    "Bolivia":              ("Bolivia",              "BO", "bolivia"),
    "Venezuela":            ("Venezuela",            "VE", "venezuela"),
    "Guyana":               ("Guyana",               "GY", "guyana"),
    "Suriname":             ("Suriname",             "SR", "suriname"),
    # Asia / Pacific
    "Mongolia":             ("Mongolia",             "MN", "mongolia"),
    "Afghanistan":          ("Afghanistan",          "AF", "afghanistan"),
    "Bhutan":               ("Bhutan",               "BT", "bhutan"),
    "Macau":                ("Macau",                "MO", "macau"),
    "Maldives":             ("Maldives",             "MV", "maldives"),
    "Brunei":               ("Brunei",               "BN", "brunei"),
    "Laos":                 ("Laos",                 "LA", "laos"),
    "Timor_Leste":          ("Timor-Leste",          "TL", "timor-leste"),
    "Papua_New_Guinea":     ("Papua New Guinea",     "PG", "papua-new-guinea"),
    "Fiji":                 ("Fiji",                 "FJ", "fiji"),
    "Samoa":                ("Samoa",                "WS", "samoa"),
    "Tonga":                ("Tonga",                "TO", "tonga"),
    "Vanuatu":              ("Vanuatu",              "VU", "vanuatu"),
    "Solomon_Islands":      ("Solomon Islands",      "SB", "solomon-islands"),
    "Kiribati":             ("Kiribati",             "KI", "kiribati"),
    "Micronesia":           ("Micronesia",           "FM", "micronesia"),
    "Marshall_Islands":     ("Marshall Islands",     "MH", "marshall-islands"),
    "Palau":                ("Palau",                "PW", "palau"),
    "Nauru":                ("Nauru",                "NR", "nauru"),
    "Tuvalu":               ("Tuvalu",               "TV", "tuvalu"),
    # Micro-states
    "Andorra":              ("Andorra",              "AD", "andorra"),
    "Monaco":               ("Monaco",               "MC", "monaco"),
    "Liechtenstein":        ("Liechtenstein",        "LI", "liechtenstein"),
    "San_Marino":           ("San Marino",           "SM", "san-marino"),
    "Vatican_City":         ("Vatican City",         "VA", "vatican-city"),
}

# Inject all extended countries
for k, v in EXTENDED_COUNTRIES.items():
    if k not in COUNTRY_REGISTRY:
        COUNTRY_REGISTRY[k] = v

# Origin hub URLs for all extended countries (P3+ style pattern)
for key, (name, code, slug) in EXTENDED_COUNTRIES.items():
    if slug not in ORIGIN_HUB_URLS:
        ORIGIN_HUB_URLS[slug] = f"/pet-transport/origins/{slug}-pet-export-guide/"

# ---------------------------------------------------------------------------
# COUNTRY WEIGHTS (for priority scoring — must match generate_build_plan_v2.py)
# ---------------------------------------------------------------------------
WEIGHTS = {
    "united-kingdom": 10.0, "united-states": 10.0,
    "united-arab-emirates": 9.5, "australia": 9.5,
    "canada": 9.0, "germany": 9.0, "france": 8.5,
    "singapore": 8.5, "hong-kong": 8.0, "south-africa": 8.0,
    "japan": 8.0, "south-korea": 7.8, "netherlands": 7.5,
    "switzerland": 7.5, "new-zealand": 7.5, "ireland": 7.2,
    "spain": 7.0, "italy": 7.0, "portugal": 7.0,
    "india": 7.0, "china": 7.5, "thailand": 6.8,
    "philippines": 6.5, "brazil": 6.5, "mexico": 6.5,
    "saudi-arabia": 6.5, "qatar": 6.3, "malaysia": 6.2,
    "indonesia": 6.0, "denmark": 6.0, "sweden": 6.0,
    "norway": 6.0, "finland": 6.0, "austria": 5.8,
    "belgium": 5.8, "greece": 5.5, "turkey": 5.5,
    "israel": 5.5, "jordan": 5.2, "kenya": 5.0,
    "nigeria": 4.0, "ghana": 5.0, "ethiopia": 5.0,
    "colombia": 4.5, "argentina": 5.0, "chile": 5.0,
    "peru": 4.8, "egypt": 4.8, "morocco": 4.8,
    "vietnam": 4.8, "taiwan": 5.0, "poland": 4.8,
    "czech-republic": 4.8, "hungary": 4.5, "romania": 4.5,
    "bulgaria": 4.5, "croatia": 4.5, "luxembourg": 4.5,
    "malta": 4.5, "cyprus": 4.5, "iceland": 4.5,
    "macau": 4.3, "sri-lanka": 4.3, "nepal": 4.3,
    "pakistan": 4.3, "bangladesh": 4.3, "cambodia": 4.0,
    "myanmar": 4.0, "laos": 3.8, "brunei": 3.8,
    "maldives": 4.0, "mauritius": 4.0, "seychelles": 3.8,
    "jamaica": 4.0, "trinidad-and-tobago": 3.8, "barbados": 3.3,
    "dominican-republic": 4.0, "costa-rica": 4.0,
    "panama": 3.8, "ecuador": 3.8, "uruguay": 3.8,
    "bolivia": 3.5, "paraguay": 3.5, "venezuela": 3.5,
    "guatemala": 3.5, "honduras": 3.5, "el-salvador": 3.5,
    "nicaragua": 3.5, "belize": 3.3, "guyana": 3.3,
    "suriname": 3.3, "armenia": 3.8, "georgia": 3.8,
    "azerbaijan": 3.8, "kazakhstan": 4.0, "uzbekistan": 3.8,
    "kyrgyzstan": 3.0, "tajikistan": 3.0, "turkmenistan": 3.0,
    "mongolia": 3.0, "russia": 3.5, "ukraine": 3.5,
    "belarus": 3.0, "moldova": 3.0, "serbia": 3.5,
    "north-macedonia": 3.0, "albania": 3.0, "kosovo": 3.0,
    "montenegro": 3.0, "bosnia-and-herzegovina": 3.0,
    "latvia": 3.5, "lithuania": 3.5, "estonia": 3.5,
    "slovakia": 3.5, "slovenia": 3.5, "rwanda": 3.5,
    "tanzania": 3.5, "uganda": 3.5, "zimbabwe": 3.5,
    "zambia": 3.3, "mozambique": 3.0, "namibia": 3.3,
    "botswana": 3.3, "eswatini": 3.0, "lesotho": 3.0,
    "malawi": 3.0, "madagascar": 3.0, "senegal": 3.0,
    "ivory-coast": 3.0, "cameroon": 3.0, "gabon": 2.8,
    "angola": 3.0, "tunisia": 3.5, "algeria": 3.0,
    "libya": 2.8, "sudan": 2.8, "south-sudan": 2.5,
    "somalia": 2.0, "eritrea": 2.0, "djibouti": 2.5,
    "iran": 2.5, "iraq": 2.5, "syria": 2.0, "yemen": 2.0,
    "afghanistan": 2.0, "lebanon": 3.5,
    "oman": 4.5, "bahrain": 4.5, "kuwait": 4.5,
    "fiji": 3.5, "papua-new-guinea": 2.8, "solomon-islands": 2.3,
    "vanuatu": 2.3, "samoa": 2.3, "tonga": 2.3,
    "kiribati": 2.0, "nauru": 2.0, "tuvalu": 2.0,
    "palau": 2.3, "micronesia": 2.3, "marshall-islands": 2.0,
    "timor-leste": 2.3, "cuba": 2.5, "haiti": 2.0,
    "antigua-and-barbuda": 2.8, "grenada": 2.8, "dominica": 2.5,
    "saint-kitts-and-nevis": 2.5, "saint-lucia": 2.8,
    "saint-vincent-and-the-grenadines": 2.5,
    "benin": 2.5, "togo": 2.5, "niger": 2.0, "mali": 2.0,
    "burkina-faso": 2.0, "guinea": 2.0, "guinea-bissau": 2.0,
    "sierra-leone": 2.0, "liberia": 2.0, "gambia": 2.5,
    "cabo-verde": 2.5, "sao-tome-and-principe": 2.0,
    "comoros": 2.0, "mauritania": 2.0, "chad": 2.0,
    "central-african-republic": 2.0, "dr-congo": 2.0,
    "republic-of-congo": 2.0, "equatorial-guinea": 2.0,
    "burundi": 2.0, "bhutan": 2.5, "andorra": 2.5,
    "monaco": 2.5, "san-marino": 2.0, "liechtenstein": 2.5,
    "vatican-city": 2.0, "palestinian-territories": 2.5,
}

TIER1 = {"united-kingdom", "united-states", "united-arab-emirates", "australia", "canada"}


def get_weight(slug):
    return WEIGHTS.get(slug, 3.0)


def score_pair(origin_slug, dest_slug):
    ow, dw = get_weight(origin_slug), get_weight(dest_slug)
    base = math.sqrt(ow * dw)
    if origin_slug in TIER1 or dest_slug in TIER1:
        base = min(base * 1.1, 10.0)
    return round(base, 2)


def tier_for_score(s):
    if s >= 7.0:   return "A"
    elif s >= 5.5: return "B"
    elif s >= 4.0: return "C"
    else:          return "D"


# ---------------------------------------------------------------------------
# LOAD BUILT ROUTES
# ---------------------------------------------------------------------------
def load_built():
    if not os.path.isdir(CONTENT_DIR):
        return set()
    return {f[:-3] for f in os.listdir(CONTENT_DIR)
            if f.endswith(".md") and f != "_index.md"}


# ---------------------------------------------------------------------------
# BUILD ALL COUNTRY PAIRS IN PRIORITY ORDER
# ---------------------------------------------------------------------------
def build_pair_list(built, tiers_wanted=None):
    """Return list of (score, tier, origin_key, dest_key, slug) for unbuilt pairs."""
    pairs = []
    all_keys = list(COUNTRY_REGISTRY.keys())

    for ok in all_keys:
        o_name, o_code, o_slug = COUNTRY_REGISTRY[ok]
        for dk in all_keys:
            if ok == dk:
                continue
            d_name, d_code, d_slug = COUNTRY_REGISTRY[dk]
            slug = f"{o_slug}-to-{d_slug}"
            if slug in built:
                continue
            sc = score_pair(o_slug, d_slug)
            tier = tier_for_score(sc)
            if tiers_wanted and tier not in tiers_wanted:
                continue
            pairs.append((sc, tier, ok, dk, slug))

    # Sort by score descending so highest-value routes are built first
    pairs.sort(key=lambda x: -x[0])
    return pairs


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate remaining PetTransportGlobal routes")
    parser.add_argument("--batch", type=int, default=0,
                        help="Max routes to generate this run (0 = all)")
    parser.add_argument("--tier", type=str, default="",
                        help="Comma-separated tier(s) to build: A,B,C,D (default: all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be generated without creating files")
    args = parser.parse_args()

    tiers_wanted = set(t.strip().upper() for t in args.tier.split(",") if t.strip()) or None

    print("Loading built routes ...")
    built = load_built()
    print(f"  {len(built)} routes already built")

    print("Computing unbuilt pairs ...")
    pairs = build_pair_list(built, tiers_wanted)
    total_remaining = len(pairs)
    print(f"  {total_remaining} unbuilt pairs to generate")

    if args.batch > 0:
        pairs = pairs[:args.batch]
        print(f"  Processing first {len(pairs)} (--batch {args.batch})")

    if args.dry_run:
        print("\nDRY RUN — routes that would be generated (first 20):")
        for sc, tier, ok, dk, slug in pairs[:20]:
            print(f"  [{tier}] {slug}  (score={sc})")
        if len(pairs) > 20:
            print(f"  ... and {len(pairs)-20} more")
        return

    # Generate
    generated = 0
    errors = 0

    for i, (sc, tier, ok, dk, slug) in enumerate(pairs):
        filepath = os.path.join(CONTENT_DIR, f"{slug}.md")
        if os.path.exists(filepath):
            continue
        try:
            content = generate_route_markdown(ok, dk)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            generated += 1
            if generated % 100 == 0:
                print(f"  [{generated}/{len(pairs)}] last: {slug}")
        except Exception as e:
            print(f"  ERROR ({slug}): {e}")
            errors += 1

    print(f"\nDone.")
    print(f"  Generated: {generated}")
    print(f"  Errors:    {errors}")
    print(f"  Remaining (after this run): {total_remaining - generated}")
    print()
    print("Next step:")
    print("  git add site/content/routes/")
    print("  git commit -m 'feat: auto-generate remaining routes (batch)'")
    print("  git push")
    print("  -> GitHub Actions builds Hugo + deploys to Hostinger automatically")


if __name__ == "__main__":
    main()
