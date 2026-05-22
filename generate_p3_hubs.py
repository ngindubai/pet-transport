"""
Task 3.2: P3 Origin Hubs + Country Guides
Generates:
  - site/content/origins/[slug].md   (25 P3 origin hubs)
  - site/content/countries/[slug].md (25 P3 country guides)
Skip-if-exists. Never overwrites existing files.

P3 origin hub title format: "[Country] Pet Export Guide"
→ Hugo derives slug: [country-slug]-pet-export-guide
"""

import json
import os
import re

# ============================================================
# PATHS
# ============================================================
REPO_ROOT = r"c:\Users\garet\Desktop\pet-transport"
DATA_DIR = os.path.join(REPO_ROOT, "data")
ORIGINS_DIR = os.path.join(REPO_ROOT, "site", "content", "origins")
COUNTRIES_DIR = os.path.join(REPO_ROOT, "site", "content", "countries")
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")
COUNTRY_DATA = os.path.join(DATA_DIR, "countries_pet_regulations.json")

with open(COUNTRY_DATA, "r", encoding="utf-8") as f:
    countries_raw = json.load(f)["countries"]

# ============================================================
# P3 COUNTRY REGISTRY
# JSON key -> (display name, ISO alpha2, slug, authority name, authority abbrev)
# ============================================================
P3_COUNTRY_REGISTRY = {
    "Ireland":        ("Ireland",       "IE", "ireland",        "Dept of Agriculture, Food and Marine", "DAFM"),
    "Norway":         ("Norway",        "NO", "norway",         "Norwegian Food Safety Authority", "Mattilsynet"),
    "Sweden":         ("Sweden",        "SE", "sweden",         "Swedish Board of Agriculture", "Jordbruksverket"),
    "Austria":        ("Austria",       "AT", "austria",        "Federal Ministry of Social Affairs, Health, Care and Consumer Protection", "BMSGPK"),
    "Belgium":        ("Belgium",       "BE", "belgium",        "Federal Agency for the Safety of the Food Chain", "FASFC"),
    "Poland":         ("Poland",        "PL", "poland",         "Main Veterinary Inspectorate", "GIW"),
    "Turkey":         ("Turkey",        "TR", "turkey",         "Ministry of Agriculture and Forestry", "TRGM"),
    "Israel":         ("Israel",        "IL", "israel",         "Israeli Veterinary Services", "IVS"),
    "Saudi_Arabia":   ("Saudi Arabia",  "SA", "saudi-arabia",   "Ministry of Environment, Water and Agriculture", "MEWA"),
    "Qatar":          ("Qatar",         "QA", "qatar",          "Ministry of Environment and Climate Change", "MECC"),
    "Kuwait":         ("Kuwait",        "KW", "kuwait",         "Public Authority for Agricultural Affairs and Fish Resources", "PAM"),
    "China":          ("China",         "CN", "china",          "General Administration of Customs of China", "GACC"),
    "Taiwan":         ("Taiwan",        "TW", "taiwan",         "Bureau of Animal and Plant Health Inspection and Quarantine", "BAPHIQ"),
    "Vietnam":        ("Vietnam",       "VN", "vietnam",        "Department of Animal Health, MARD", "DAH"),
    "Sri_Lanka":      ("Sri Lanka",     "LK", "sri-lanka",      "Department of Animal Production and Health", "DAPH"),
    "Argentina":      ("Argentina",     "AR", "argentina",      "Servicio Nacional de Sanidad y Calidad Agroalimentaria", "SENASA"),
    "Chile":          ("Chile",         "CL", "chile",          "Servicio Agricola y Ganadero", "SAG"),
    "Colombia":       ("Colombia",      "CO", "colombia",       "Instituto Colombiano Agropecuario", "ICA"),
    "Egypt":          ("Egypt",         "EG", "egypt",          "General Organisation for Veterinary Services", "GOVS"),
    "Kenya":          ("Kenya",         "KE", "kenya",          "Directorate of Veterinary Services", "DVS"),
    "Nigeria":        ("Nigeria",       "NG", "nigeria",        "Federal Dept of Veterinary and Pest Control Services", "FDVPCS"),
    "Czech_Republic": ("Czech Republic","CZ", "czech-republic", "State Veterinary Administration", "SVA"),
    "Romania":        ("Romania",       "RO", "romania",        "National Sanitary Veterinary and Food Safety Authority", "ANSVSA"),
    "Malta":          ("Malta",         "MT", "malta",          "Veterinary Regulation Directorate", "VRD"),
    "Cyprus":         ("Cyprus",        "CY", "cyprus",         "Department of Veterinary Services", "DVS-CY"),
}

P3_KEYS = [
    "Ireland", "Norway", "Sweden", "Austria", "Belgium", "Poland",
    "Turkey", "Israel", "Saudi_Arabia", "Qatar", "Kuwait",
    "China", "Taiwan", "Vietnam", "Sri_Lanka",
    "Argentina", "Chile", "Colombia",
    "Egypt", "Kenya", "Nigeria",
    "Czech_Republic", "Romania", "Malta", "Cyprus",
]

# Airlines relevant to each P3 origin
AIRLINES_BY_COUNTRY = {
    "Ireland":      [("Aer Lingus", "cabin_and_cargo"), ("Ryanair", "cargo_only"), ("British Airways", "cargo_only"),
                     ("KLM", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("United Airlines", "cabin_only"), ("Delta Air Lines", "cabin_and_cargo"),
                     ("American Airlines", "cabin_and_cargo")],
    "Norway":       [("Norwegian Air", "cabin_only"), ("SAS Scandinavian Airlines", "cabin_and_cargo"),
                     ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                     ("Finnair", "cabin_and_cargo"), ("Swiss International Air Lines", "cabin_and_cargo")],
    "Sweden":       [("SAS Scandinavian Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Finnair", "cabin_and_cargo"),
                     ("Swiss International Air Lines", "cabin_and_cargo"), ("Delta Air Lines", "cabin_and_cargo")],
    "Austria":      [("Austrian Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Swiss International Air Lines", "cabin_and_cargo"),
                     ("Etihad Airways", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo")],
    "Belgium":      [("Brussels Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Swiss International Air Lines", "cabin_and_cargo"),
                     ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only")],
    "Poland":       [("LOT Polish Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                     ("Ryanair", "cargo_only"), ("Wizz Air", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Swiss International Air Lines", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo")],
    "Turkey":       [("Turkish Airlines", "cabin_and_cargo"), ("Pegasus Airlines", "cargo_only"),
                     ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                     ("Etihad Airways", "cargo_only"), ("Swiss International Air Lines", "cabin_and_cargo")],
    "Israel":       [("El Al", "cabin_and_cargo"), ("Arkia Airlines", "cargo_only"),
                     ("Turkish Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                     ("Swiss International Air Lines", "cabin_and_cargo"), ("KLM", "cabin_and_cargo"),
                     ("easyJet", "cargo_only")],
    "Saudi_Arabia": [("Saudia", "cargo_only"), ("flynas", "cargo_only"),
                     ("Emirates", "cargo_only"), ("Etihad Airways", "cargo_only"), ("Qatar Airways", "cargo_only"),
                     ("Turkish Airlines", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                     ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                     ("Egypt Air", "cargo_only")],
    "Qatar":        [("Qatar Airways", "cargo_only"), ("Emirates", "cargo_only"),
                     ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("Singapore Airlines", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("Etihad Airways", "cargo_only"),
                     ("Cathay Pacific", "cargo_only"), ("Korean Air", "cabin_and_cargo")],
    "Kuwait":       [("Kuwait Airways", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Etihad Airways", "cargo_only"), ("British Airways", "cargo_only"),
                     ("Lufthansa", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                     ("Qatar Airways", "cargo_only"), ("Air France", "cabin_and_cargo"),
                     ("flydubai", "cargo_only"), ("Egypt Air", "cargo_only")],
    "China":        [("Air China", "cargo_only"), ("China Eastern Airlines", "cargo_only"),
                     ("China Southern Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                     ("Singapore Airlines", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Korean Air", "cabin_and_cargo"), ("Japan Airlines (JAL)", "cargo_only")],
    "Taiwan":       [("EVA Air", "cargo_only"), ("China Airlines", "cargo_only"),
                     ("Cathay Pacific", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                     ("Japan Airlines (JAL)", "cargo_only"), ("Korean Air", "cabin_and_cargo"),
                     ("ANA (All Nippon Airways)", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Emirates", "cargo_only")],
    "Vietnam":      [("Vietnam Airlines", "cargo_only"), ("VietJet Air", "cargo_only"),
                     ("Bamboo Airways", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                     ("Cathay Pacific", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Korean Air", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Thai Airways", "cargo_only")],
    "Sri_Lanka":    [("SriLankan Airlines", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Qatar Airways", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                     ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("Cathay Pacific", "cargo_only"), ("Thai Airways", "cargo_only"),
                     ("Etihad Airways", "cargo_only"), ("Air India", "cabin_and_cargo")],
    "Argentina":    [("Aerolineas Argentinas", "cabin_and_cargo"), ("LATAM Airlines", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"),
                     ("American Airlines", "cabin_and_cargo"), ("United Airlines", "cabin_only"),
                     ("Iberia", "cabin_and_cargo"), ("KLM", "cabin_and_cargo")],
    "Chile":        [("LATAM Airlines", "cabin_and_cargo"), ("Sky Airline", "cargo_only"),
                     ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"),
                     ("American Airlines", "cabin_and_cargo"), ("Iberia", "cabin_and_cargo"),
                     ("KLM", "cabin_and_cargo"), ("Air Canada", "cabin_and_cargo")],
    "Colombia":     [("Avianca", "cabin_and_cargo"), ("LATAM Airlines", "cabin_and_cargo"),
                     ("Copa Airlines", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                     ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                     ("Delta Air Lines", "cabin_and_cargo"), ("American Airlines", "cabin_and_cargo"),
                     ("United Airlines", "cabin_only"), ("Iberia", "cabin_and_cargo")],
    "Egypt":        [("EgyptAir", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Qatar Airways", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("Etihad Airways", "cargo_only"),
                     ("Swiss International Air Lines", "cabin_and_cargo"), ("KLM", "cabin_and_cargo")],
    "Kenya":        [("Kenya Airways", "cargo_only"), ("British Airways", "cargo_only"),
                     ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"),
                     ("Lufthansa", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                     ("Ethiopian Airlines", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Rwandair", "cargo_only"), ("Air France", "cabin_and_cargo")],
    "Nigeria":      [("Air Peace", "cargo_only"), ("British Airways", "cargo_only"),
                     ("Virgin Atlantic", "cargo_only"), ("Emirates", "cargo_only"),
                     ("Qatar Airways", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo"),
                     ("Lufthansa", "cabin_and_cargo"), ("Ethiopian Airlines", "cargo_only"),
                     ("Air France", "cabin_and_cargo"), ("KLM", "cabin_and_cargo")],
    "Czech_Republic": [("Czech Airlines (CSA)", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                       ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                       ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                       ("Swiss International Air Lines", "cabin_and_cargo"), ("Ryanair", "cargo_only"),
                       ("Wizz Air", "cargo_only"), ("Austrian Airlines", "cabin_and_cargo")],
    "Romania":      [("TAROM", "cabin_and_cargo"), ("Ryanair", "cargo_only"),
                     ("Wizz Air", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                     ("Turkish Airlines", "cabin_and_cargo"), ("Austrian Airlines", "cabin_and_cargo")],
    "Malta":        [("Air Malta", "cabin_and_cargo"), ("Ryanair", "cargo_only"),
                     ("easyJet", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("KLM", "cabin_and_cargo"),
                     ("Wizz Air", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo")],
    "Cyprus":       [("Cyprus Airways", "cabin_and_cargo"), ("Ryanair", "cargo_only"),
                     ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                     ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"),
                     ("Turkish Airlines", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                     ("easyJet", "cargo_only"), ("KLM", "cabin_and_cargo")],
}

# Export notes per P3 country: (permit text, health cert text, endorsement text)
EXPORT_NOTES = {
    "Ireland":      ("Ireland uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU Animal Health Certificate (AHC) endorsed by DAFM is required.",
                     "EU AHC required for non-EU destinations. EU Pet Passport for EU/EFTA travel.",
                     "DAFM endorsement required for all non-EU/EFTA destinations"),
    "Norway":       ("Norway participates in the EU Pet Travel Scheme as an EEA country. EU Pet Passport accepted for movements within EU/EEA. For non-EU destinations, an official health certificate endorsed by Mattilsynet is required.",
                     "Official veterinary health certificate endorsed by Mattilsynet for non-EU destinations.",
                     "Mattilsynet (Norwegian Food Safety Authority) endorsement required"),
    "Sweden":       ("Sweden uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by Jordbruksverket is required.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "Jordbruksverket (Swedish Board of Agriculture) endorsement required for non-EU/EFTA destinations"),
    "Austria":      ("Austria uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by BMSGPK is required.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "BMSGPK endorsement required for non-EU/EFTA destinations"),
    "Belgium":      ("Belgium uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by FASFC is required.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "FASFC (Federal Agency for the Safety of the Food Chain) endorsement required for non-EU/EFTA destinations"),
    "Poland":       ("Poland uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by GIW is required.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "GIW (Main Veterinary Inspectorate) endorsement required for non-EU/EFTA destinations"),
    "Turkey":       ("No formal export permit required for household dogs and cats. A health certificate from a government-approved veterinarian, endorsed by the Ministry of Agriculture and Forestry (TRGM), is required before departure.",
                     "Official health certificate endorsed by TRGM. Certificate must meet destination country format.",
                     "TRGM (Ministry of Agriculture and Forestry) endorsement required"),
    "Israel":       ("No formal export permit required for household pets. An official health certificate from a licensed veterinarian, endorsed by the Israeli Veterinary Services (IVS), is required for international travel.",
                     "Official health certificate endorsed by IVS. Must meet destination country format and requirements.",
                     "Israeli Veterinary Services (IVS) endorsement required"),
    "Saudi_Arabia": ("No formal export permit required for household pets. An official health certificate endorsed by MEWA is required. Some destination countries require additional documentation or consulate endorsement.",
                     "Official health certificate endorsed by MEWA (Ministry of Environment, Water and Agriculture).",
                     "MEWA endorsement required. Some destinations require additional consulate endorsement."),
    "Qatar":        ("No formal export permit required for household pets. An official health certificate endorsed by MECC is required. Certificate must meet destination country format.",
                     "Official health certificate endorsed by MECC (Ministry of Environment and Climate Change).",
                     "MECC endorsement required for all international pet movements"),
    "Kuwait":       ("No formal export permit required for household pets. An official health certificate from a government-approved veterinarian, endorsed by PAM, is required.",
                     "Official health certificate endorsed by PAM (Public Authority for Agricultural Affairs and Fish Resources).",
                     "PAM endorsement required for all international pet movements"),
    "China":        ("Export certificate from GACC (General Administration of Customs of China) or local CIQ (Customs and Inspection Quarantine) authority is required. The certificate must meet destination country format.",
                     "Official export health certificate endorsed by GACC or local CIQ. Must meet destination country specific requirements.",
                     "GACC or CIQ endorsement required. Some destinations require additional apostille or consulate endorsement."),
    "Taiwan":       ("An export health certificate from BAPHIQ (Bureau of Animal and Plant Health Inspection and Quarantine) is required. Some destinations require specific disease test results in addition to the standard certificate.",
                     "Official export health certificate from BAPHIQ. Certificate must meet destination country format.",
                     "BAPHIQ endorsement required for all international pet movements"),
    "Vietnam":      ("An export health certificate from DAH (Department of Animal Health) is required. The certificate must be endorsed by DAH before departure.",
                     "Official export health certificate endorsed by DAH (Department of Animal Health, MARD). Must be issued within 7 days of travel.",
                     "DAH endorsement required. Certificate must be obtained within 7 days of departure."),
    "Sri_Lanka":    ("No formal export permit required for household pets. An official health certificate from a government-approved veterinarian, endorsed by DAPH, is required before departure.",
                     "Official health certificate endorsed by DAPH (Department of Animal Production and Health).",
                     "DAPH endorsement required for all international pet movements"),
    "Argentina":    ("No formal export permit required for household pets from Argentina. A health certificate from an accredited veterinarian, endorsed by SENASA, is required for international travel.",
                     "Official health certificate endorsed by SENASA (Servicio Nacional de Sanidad y Calidad Agroalimentaria). Some destinations require consulate endorsement in addition.",
                     "SENASA endorsement required. Allow 3-5 business days for endorsement processing."),
    "Chile":        ("No formal export permit required for household pets. A health certificate from an accredited veterinarian, endorsed by SAG (Servicio Agricola y Ganadero), is required before departure.",
                     "Official health certificate endorsed by SAG. Must be issued within 10 days of departure for most destinations.",
                     "SAG endorsement required. Certificate must be endorsed before your pet boards the plane."),
    "Colombia":     ("No formal export permit required for household pets. An official health certificate from an ICA-accredited veterinarian, endorsed by ICA, is required.",
                     "Official health certificate endorsed by ICA (Instituto Colombiano Agropecuario). Certificate must meet destination country requirements.",
                     "ICA endorsement required for all international pet movements from Colombia"),
    "Egypt":        ("No formal export permit for household pets, but an official health certificate from a licensed vet endorsed by GOVS is required. Some destination countries may also require Egyptian embassy endorsement.",
                     "Official health certificate endorsed by GOVS (General Organisation for Veterinary Services).",
                     "GOVS endorsement required. Some destinations require additional embassy endorsement."),
    "Kenya":        ("Export health certificate from an accredited veterinarian, endorsed by the Directorate of Veterinary Services (DVS), is required. No advance export permit is required for household pets.",
                     "Official health certificate endorsed by DVS (Directorate of Veterinary Services). Must list all vaccinations and microchip details.",
                     "DVS endorsement required. Certificate must be issued within 10 days of travel for most destinations."),
    "Nigeria":      ("An export health certificate from a government-approved veterinarian, endorsed by FDVPCS (Federal Dept of Veterinary and Pest Control Services), is required. Some destination countries also require consulate or embassy endorsement.",
                     "Official health certificate endorsed by FDVPCS. Must meet destination country specific requirements.",
                     "FDVPCS endorsement required. Allow extra time for endorsement as processing can take several days."),
    "Czech_Republic": ("Czech Republic uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by SVA is required.",
                       "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                       "SVA (State Veterinary Administration) endorsement required for non-EU/EFTA destinations"),
    "Romania":      ("Romania uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by ANSVSA is required.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "ANSVSA endorsement required for non-EU/EFTA destinations"),
    "Malta":        ("Malta uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by VRD is required. As an island, Malta takes biosecurity very seriously.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "VRD (Veterinary Regulation Directorate) endorsement required for non-EU/EFTA destinations"),
    "Cyprus":       ("Cyprus uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by DVS is required. Advance notification required for all pet arrivals into Cyprus.",
                     "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.",
                     "DVS (Department of Veterinary Services) endorsement required for non-EU/EFTA destinations"),
}

# Unique country overview data for country guide pages
# (complexity, overview_text, [(heading, body), ...])
COUNTRY_OVERVIEWS = {
    "Ireland": (
        "moderate",
        "Ireland is an EU member state and follows the EU Pet Travel Scheme for most pet movements. The DAFM "
        "(Department of Agriculture, Food and Marine) administers import controls. Ireland has been free of "
        "rabies for many decades and its island status means the authorities take biosecurity seriously.\n\n"
        "For pets arriving from within the EU and EFTA, an EU Pet Passport is the main travel document. "
        "For pets from the UK (post-Brexit), the United States, and other non-EU origins, a specific health "
        "certificate format is required. The UK's departure from the EU created extra steps for UK pet owners "
        "moving to Ireland, and the process now requires an ISO microchip and a recent AHC endorsed by APHA.\n\n"
        "Ireland does not have routine quarantine for compliant pets, which makes it more straightforward "
        "than some other island destinations. Get the paperwork right and the arrival process is smooth.",
        [
            ("UK and non-EU pets entering Ireland",
             "Since Brexit, UK pet owners bringing pets to Ireland need an Animal Health Certificate (AHC) "
             "rather than a pet passport. The AHC must be issued by an Official Veterinarian (OV) in the "
             "UK within 10 days before travel and endorsed by APHA. From the US, a USDA APHIS-endorsed "
             "health certificate in EU AHC format is required.\n\n"
             "For all non-EU origins: microchip (ISO 15-digit) must be implanted before or on the same "
             "day as the first rabies vaccination. Rabies vaccination must be valid at the time of travel. "
             "From countries where a titre test is required (rabies-free status not established), blood "
             "must be drawn at least 30 days after vaccination and the pet must wait 3 months after a "
             "successful titre test result before entering Ireland."),
            ("Travelling to Ireland through Northern Ireland or Great Britain",
             "Pets moving from Great Britain to Ireland (via the land border with Northern Ireland or by ferry) "
             "face the same documentation requirements as pets arriving by air. The entry point for official "
             "checks may vary. For any non-EU pets, ensure your documentation is complete before you travel. "
             "Using a ferry service that operates between Great Britain and Republic of Ireland means your "
             "pet will be checked on arrival. Book with a service that has approved animal landing points."),
        ]
    ),
    "Norway": (
        "moderate",
        "Norway is not an EU member but participates in the EU Pet Travel Scheme as an EEA/EFTA country. "
        "The Norwegian Food Safety Authority (Mattilsynet) handles all animal import controls. Dogs, cats, "
        "and ferrets can enter Norway using an EU Pet Passport or equivalent documentation.\n\n"
        "Norway has been rabies-free for many years and maintains strict biosecurity to keep it that way. "
        "Pets from countries where rabies is present face more documentation requirements, and some origins "
        "require a rabies titre test with a 3-month waiting period before Norway entry.\n\n"
        "Norway also has specific rules around tapeworm treatment for dogs. Dogs arriving from most "
        "countries must be treated against Echinococcus multilocularis (fox tapeworm) between 1-5 days "
        "before arrival. This treatment must be recorded by a vet. Cats are exempt from this requirement.",
        [
            ("Tapeworm treatment requirement for dogs",
             "Dogs entering Norway from most origins must receive treatment against Echinococcus "
             "multilocularis (fox tapeworm) between 1 and 5 days before entry. The treatment must be "
             "recorded in the pet passport or on the health certificate and must include the product name, "
             "dose, and date. Praziquantel is the approved treatment. Your vet must administer it.\n\n"
             "Exemptions apply for dogs coming from EU/EEA countries specifically approved by Norway as "
             "low-risk for this tapeworm. Check the Mattilsynet website for the current approved country list."),
            ("Pets from outside the EU/EEA entering Norway",
             "Pets from non-EU/EEA countries such as the US, UK, Australia, or the Middle East face "
             "additional steps. A government-endorsed health certificate meeting Norway's requirements "
             "is needed. From high-rabies-risk countries, a titre test is required with a minimum "
             "result of 0.5 IU/ml and a 3-month waiting period after the blood draw.\n\n"
             "Pre-notification to Mattilsynet is recommended for pets from outside EU/EEA. Contact "
             "the point of entry (typically Oslo Gardermoen Airport) Mattilsynet office before travel."),
        ]
    ),
    "Sweden": (
        "moderate",
        "Sweden is an EU member state and uses the EU Pet Travel Scheme for most pet movements. "
        "Jordbruksverket (the Swedish Board of Agriculture) administers import controls. For EU/EFTA "
        "pets, an EU Pet Passport is the main document. For pets from the UK, US, and other non-EU "
        "origins, an EU Animal Health Certificate (AHC) is required.\n\n"
        "Sweden has been free of rabies for decades and its documentation requirements reflect this. "
        "Dogs arriving from many countries must be treated against Echinococcus multilocularis "
        "(tapeworm) within 1-5 days of entry. This requirement follows the same EU guidance as "
        "other Scandinavian destinations.\n\n"
        "Stockholm Arlanda Airport has dedicated animal handling facilities. Pre-notification of "
        "your pet's arrival to Jordbruksverket is required for pets coming from outside the EU/EEA.",
        [
            ("Entry requirements from the UK post-Brexit",
             "UK pets entering Sweden now require an Animal Health Certificate (AHC) rather than "
             "an EU Pet Passport. The AHC must be issued by an Official Veterinarian (OV) within "
             "10 days before travel and endorsed by APHA. ISO microchip must be implanted before "
             "or on the same day as the first rabies vaccination.\n\n"
             "The AHC has replaced the EU Pet Passport for all UK-to-EU movements. Each trip requires "
             "a new AHC. Keep records of previous documents for future reference."),
            ("Tapeworm treatment for dogs entering Sweden",
             "Dogs from most origins outside a list of approved low-risk countries must be treated "
             "for Echinococcus multilocularis by a vet between 1-5 days before arrival. The treatment "
             "must be recorded on the health certificate or pet passport with the product name, dose, "
             "and date.\n\n"
             "Contact Jordbruksverket or a pet transport agent for the current approved country list "
             "and to confirm whether your dog needs this treatment before travel to Sweden."),
        ]
    ),
    "Austria": (
        "moderate",
        "Austria is an EU member state and follows the EU Pet Travel Scheme. The BMSGPK (Federal "
        "Ministry of Social Affairs, Health, Care and Consumer Protection) administers veterinary "
        "import controls. For EU/EFTA pets: EU Pet Passport. For non-EU origins: an EU Animal "
        "Health Certificate (AHC).\n\n"
        "Austria does not require quarantine for compliant pets and is considered one of the simpler "
        "EU destinations for pet imports. Vienna Airport handles a reasonable volume of pet movements "
        "and the process at border control is usually smooth when documentation is complete.\n\n"
        "Austria does have its own rules around certain dog breeds, particularly the 'Kampfhunde' "
        "(fighting dog) classification. Some breeds that are permitted in other EU countries face "
        "restrictions or registration requirements in Austria. Check breed-specific rules before travel.",
        [
            ("Non-EU pets entering Austria",
             "Pets from the US, UK, Australia, Canada, and other non-EU countries need an EU AHC "
             "endorsed by the origin country's official vet authority. From the UK, the AHC must be "
             "endorsed by APHA. From the US, the certificate must be endorsed by USDA APHIS.\n\n"
             "From high-risk rabies countries, a titre test may be required with a minimum result "
             "of 0.5 IU/ml. There is a 3-month waiting period after the titre test before Austria entry."),
            ("Breed restrictions in Austria",
             "Austria classifies certain breeds as potentially dangerous. While federal law provides "
             "the framework, individual Austrian states (Bundeslaender) have their own lists and "
             "registration requirements. Breeds often subject to restrictions include Rottweiler, "
             "American Pit Bull Terrier, and similar working or guard breeds.\n\n"
             "If you are moving to Austria with a breed that might be considered 'listed', contact "
             "the relevant state authority before travel to confirm registration requirements. "
             "A liability insurance policy is often required."),
        ]
    ),
    "Belgium": (
        "moderate",
        "Belgium is an EU member state and follows the EU Pet Travel Scheme. The FASFC (Federal "
        "Agency for the Safety of the Food Chain / Agence federale pour la securite de la chaine "
        "alimentaire) administers animal import controls. EU/EFTA pets use EU Pet Passports. "
        "Pets from non-EU countries need an AHC.\n\n"
        "Brussels Airport is one of Europe's busiest hubs and handles significant volumes of "
        "pet movements. Belgium's central location in Europe makes it a common transit point "
        "for pets arriving from outside the EU before connecting to other EU destinations.\n\n"
        "Belgium does not require quarantine for compliant pets arriving with correct documentation. "
        "The process at Brussels Airport is generally efficient, with dedicated FASFC staff for "
        "animal checks during business hours.",
        [
            ("Post-Brexit UK pets entering Belgium",
             "Since Brexit, UK pets need an AHC instead of an EU Pet Passport to enter Belgium. "
             "The AHC must be issued within 10 days of travel by a UK Official Veterinarian (OV) "
             "and endorsed by APHA. If your pet had an EU Pet Passport issued in the UK before "
             "Brexit, it is no longer valid for EU entry.\n\n"
             "Belgium is a popular first EU entry point for UK pets on their way to other EU "
             "destinations. If transiting through Belgium, the same entry documentation applies."),
            ("Using Belgium as an EU transit point",
             "Many pets transit through Brussels Airport en route to other destinations. If your "
             "pet's final destination is another EU country, entering Belgium is the official "
             "EU entry point for all third-country (non-EU) animals. The documentation check "
             "happens at Brussels, and once through, the pet can continue to other EU countries "
             "on the same journey.\n\n"
             "Make sure you pre-notify FASFC for pets arriving from non-EU countries. The FASFC "
             "border inspection post (BIP) at Brussels Airport handles these checks."),
        ]
    ),
    "Poland": (
        "moderate",
        "Poland is an EU member state following the EU Pet Travel Scheme. The Main Veterinary "
        "Inspectorate (Glowny Inspektorat Weterynarii, GIW) handles import controls. For EU/EFTA "
        "pets: EU Pet Passport. For pets from the UK, US, and other non-EU origins: an EU AHC "
        "endorsed by the origin country's official veterinary authority.\n\n"
        "Poland borders several non-EU countries including Ukraine, Belarus, and Russia, and "
        "has experience handling pet imports from these origins. Warsaw Chopin Airport has "
        "official veterinary check facilities for imported animals.\n\n"
        "Poland does not require routine quarantine for pets arriving with correct documentation. "
        "The process is aligned with EU standards and the documentation requirements are clear.",
        [
            ("Pets arriving from Ukraine, Belarus, and CIS countries",
             "Poland handles a significant number of pet movements from Eastern European non-EU "
             "countries. Pets from Ukraine, Belarus, and Moldova must comply with EU third-country "
             "import rules, including an endorsed health certificate, valid rabies vaccination, "
             "and in many cases a rabies titre test with a 3-month waiting period.\n\n"
             "Poland has dedicated border inspection facilities at road, rail, and air entry points "
             "for animals from non-EU Eastern European countries. Pre-notification of GIW is "
             "required for all third-country pet imports."),
            ("EU Pet Passport rules at Poland entry",
             "For pets from EU/EEA countries with valid EU Pet Passports, entry into Poland is "
             "straightforward. The passport must show: valid rabies vaccination, ISO microchip, "
             "and a rabies titre test if coming from certain origins.\n\n"
             "If travelling from an EU country where your pet was issued an EU Pet Passport, "
             "ensure the vaccination record is up to date. An expired rabies vaccination in the "
             "EU Pet Passport can cause delays at the border."),
        ]
    ),
    "Turkey": (
        "high",
        "Turkey has its own pet import requirements that are separate from EU rules. The Ministry "
        "of Agriculture and Forestry (TRGM) administers animal import controls. Dogs and cats "
        "entering Turkey require a valid microchip (ISO 11784/11785), an up-to-date rabies "
        "vaccination, and a health certificate endorsed by the official veterinary authority "
        "of the origin country.\n\n"
        "Turkey requires the health certificate to be issued within 10 days of travel for most "
        "origins. Some origin countries also require their certificates to be apostilled or "
        "endorsed by the Turkish consulate, so check the specific requirements for your origin "
        "country well in advance.\n\n"
        "Istanbul Airport handles the highest volume of pet imports into Turkey. There is a "
        "dedicated veterinary control point at the airport. Pets from non-approved origins "
        "may face additional examination on arrival.",
        [
            ("Health certificate and apostille requirements",
             "Turkey requires health certificates from some origin countries to have an apostille "
             "(a Hague Convention authentication stamp) or consulate endorsement in addition to "
             "the standard government veterinary stamp. The requirement varies by origin country.\n\n"
             "For pets from the EU: an EU AHC endorsed by the origin country's vet authority is "
             "accepted. From the UK: an AHC endorsed by APHA, often with an apostille. From the US: "
             "a USDA APHIS-endorsed health certificate. Check with the Turkish consulate in your "
             "origin country for the most current requirements before arranging documentation."),
            ("Breed restrictions in Turkey",
             "Turkey has restrictions on certain breeds. Pit Bull Terrier types, American Staffordshire "
             "Terrier, Bull Terrier, and related breeds are subject to specific rules. These breeds may "
             "require additional permits or may not be permitted without specific conditions.\n\n"
             "If you are travelling with a breed that might fall under restricted categories, contact "
             "TRGM or a Turkish pet transport specialist before booking flights. Rules can change and "
             "it is better to verify in advance than face refusal at the border."),
        ]
    ),
    "Israel": (
        "high",
        "Israel has strict biosecurity requirements for pet imports, particularly focused on "
        "rabies control. The Israeli Veterinary Services (IVS) regulates all pet imports. "
        "Pets entering Israel from most countries require an up-to-date rabies vaccination, "
        "ISO microchip, and a government-endorsed health certificate. From many origins, "
        "a rabies titre test is also required.\n\n"
        "An import permit must be obtained from IVS before your pet travels. The permit process "
        "typically takes 2-4 weeks. Some origin countries require longer lead times. Start the "
        "permit process as soon as you know your travel date.\n\n"
        "Tel Aviv Ben Gurion Airport is the main entry point for pets entering Israel. There "
        "is a government veterinary office at the airport that processes all arriving animals. "
        "Your pet will be inspected on arrival before being released.",
        [
            ("Import permit process for Israel",
             "To bring a pet into Israel, you must submit an import permit application to the "
             "Israeli Veterinary Services (IVS) before travel. The application requires: proof of "
             "microchip, valid rabies vaccination record, titre test results (if required for your "
             "origin), and a completed application form.\n\n"
             "The permit is typically issued within 2-4 weeks. Once issued, it is valid for a "
             "specific period. Travel must be within the permit validity window. Do not book flights "
             "until the permit is in hand.\n\n"
             "From countries with endemic rabies, a titre test is required. The blood draw must "
             "be at least 30 days after the rabies vaccination. A minimum result of 0.5 IU/ml "
             "is required. A 3-month waiting period after the successful titre test applies before "
             "Israel entry."),
            ("Pet inspection on arrival at Ben Gurion Airport",
             "All pets arriving in Israel are inspected by an IVS veterinary officer at Ben Gurion "
             "Airport. Have all original documents ready: import permit, health certificate, "
             "vaccination record, and titre test results. Copies are not accepted.\n\n"
             "If your documentation is complete and correct, the inspection is usually quick. "
             "If any documentation is missing or incorrect, your pet may be held in government "
             "quarantine at the owner's expense until the issue is resolved."),
        ]
    ),
    "Saudi_Arabia": (
        "very_high",
        "Saudi Arabia has detailed pet import rules administered by MEWA (Ministry of Environment, "
        "Water and Agriculture). An import permit is required before bringing any pet into the Kingdom. "
        "The permit process can take several weeks, so start early.\n\n"
        "Dogs and cats must be microchipped (ISO 15-digit), vaccinated against rabies and other "
        "diseases (including distemper, parvovirus, hepatitis for dogs, and cat flu vaccinations), "
        "and accompanied by an official health certificate endorsed by the origin country's authority.\n\n"
        "Saudi Arabia also has restrictions on certain breeds. Bull breeds and large working dogs "
        "are often restricted. Some breeds are outright prohibited. Check with MEWA or a specialist "
        "agent for the current breed restriction list before making any travel arrangements.",
        [
            ("Import permit and documentation process",
             "The import permit must be obtained from MEWA before your pet travels. Applications "
             "can be submitted online through the MEWA portal. Required documents include: "
             "microchip certificate, rabies vaccination record, other required vaccination records, "
             "health certificate from a licensed vet endorsed by the national authority, and "
             "sometimes an apostille.\n\n"
             "Processing time varies. Allow at least 3-4 weeks. Once the permit is issued, it has "
             "a validity period. Travel must occur within this window. Some people find it helpful "
             "to use a specialist Saudi Arabia pet import agent who knows the current requirements."),
            ("Quarantine and breed restrictions",
             "Saudi Arabia does not have routine quarantine for pets arriving with complete "
             "documentation. However, pets arriving with missing or incorrect paperwork may be "
             "detained at the port of entry.\n\n"
             "Breed restrictions in Saudi Arabia include many bull-type breeds, certain large guard "
             "breeds, and dogs perceived as aggressive. The list is enforced at the border. If your "
             "breed might fall under any restricted category, get written confirmation from MEWA "
             "before booking flights. Some breeds have been refused entry despite having full "
             "paperwork because the breed restriction was overlooked."),
        ]
    ),
    "Qatar": (
        "high",
        "Qatar requires an import permit for pets, obtained from the Ministry of Environment and "
        "Climate Change (MECC) before travel. Pets must be microchipped, vaccinated against "
        "rabies (and other diseases), and accompanied by a government-endorsed health certificate.\n\n"
        "Qatar's import rules have been updated and clarified in recent years, and the process "
        "is cleaner than it once was. However, advance preparation is still essential. The "
        "certificate must be issued close to the travel date (typically within 7-10 days) and "
        "endorsed by the official vet authority of your origin country.\n\n"
        "Doha Hamad International Airport is a major hub with good animal handling facilities. "
        "Pets arriving as cargo are handled through the airport cargo centre with a dedicated "
        "live animal section.",
        [
            ("Import permit for Qatar",
             "Apply for your import permit through MECC before booking flights. The application "
             "requires: microchip number, rabies vaccination details, other vaccination records, "
             "health certificate from your origin country's official vet authority.\n\n"
             "Processing times vary but typically take 5-10 business days. The permit is issued "
             "for a specific entry window. Make sure your travel dates fall within the permit "
             "validity period. Some origin countries require additional steps such as a titre test."),
            ("Which pets are permitted in Qatar",
             "Dogs and cats are the most commonly imported pets into Qatar. Most breeds are "
             "permitted, although Qatar, in common with many Gulf countries, has restrictions "
             "on certain aggressive or fighting breeds. If your pet is a breed that might be "
             "classified as dangerous, get confirmation from MECC before booking.\n\n"
             "Qatar has a good community of expatriate pet owners and the process for bringing "
             "pets into the country is well established. Working with a specialist pet transport "
             "agent familiar with Qatar is the easiest way to ensure all documentation is correct."),
        ]
    ),
    "Kuwait": (
        "high",
        "Kuwait requires an import permit from PAM (Public Authority for Agricultural Affairs and "
        "Fish Resources) before any pet can enter the country. The permit process typically takes "
        "2-4 weeks. Dogs require a health certificate listing all vaccinations, microchip number, "
        "and a statement of good health from an official vet.\n\n"
        "Kuwait has breed restrictions, particularly for large and working breeds. A number of "
        "breeds are prohibited outright. Check the current list with PAM before making any "
        "travel arrangements if your pet might be in a restricted category.\n\n"
        "Kuwait International Airport has a dedicated veterinary inspection point for arriving "
        "animals. Have all original documents available for inspection. Copies are not accepted.",
        [
            ("Import permit process for Kuwait",
             "Submit the import permit application to PAM well in advance. Required documents: "
             "microchip certificate, vaccination records (rabies and others), health certificate "
             "endorsed by the official vet authority in your origin country.\n\n"
             "Allow at least 3-4 weeks for the permit to be processed and issued. The permit "
             "has a limited validity period. Your pet must arrive within the permit window. "
             "If your travel dates change, you may need to request an amended permit."),
            ("Breed restrictions in Kuwait",
             "Kuwait restricts or prohibits a number of dog breeds. Bull-type breeds, large "
             "guard dogs, and breeds perceived as aggressive are commonly on the restricted list. "
             "The exact list can change, so always verify with PAM or a specialist agent "
             "before travel.\n\n"
             "Cats are generally unrestricted by breed in Kuwait. Dogs that are not on any "
             "restricted list follow the standard permit process. If in doubt about your breed, "
             "get written confirmation from PAM before booking flights."),
        ]
    ),
    "China": (
        "very_high",
        "China has some of the most detailed pet import requirements in Asia. The General "
        "Administration of Customs (GACC) and local CIQ (Customs and Inspection Quarantine) "
        "offices oversee pet imports. A health certificate from your origin country, endorsed "
        "by the national veterinary authority, is required. From most origins, a rabies titre "
        "test is also required.\n\n"
        "All pets entering China must undergo quarantine in a government-approved facility. "
        "The standard quarantine period is 7 days (from approved countries with correct "
        "documentation) or up to 30 days depending on origin and health status. The quarantine "
        "cost is the owner's responsibility and must be pre-booked.\n\n"
        "The whole process, from starting vaccinations to China entry, typically takes at least "
        "6 months for countries where a titre test is required. Start preparations early.",
        [
            ("Quarantine and pre-booking process",
             "All pets entering China must be quarantined, even with perfect documentation. "
             "Quarantine must be pre-booked at an approved government facility before your "
             "pet's arrival. Do not assume a facility will have space - book well in advance.\n\n"
             "The quarantine period is typically 7 days for pets arriving from approved countries "
             "with compliant documentation. Pets from non-approved origins or with documentation "
             "gaps may face 30 days. The cost varies by facility and is paid by the owner.\n\n"
             "Approved entry points for live animal imports include Shanghai Pudong, Beijing Capital, "
             "Guangzhou Baiyun, and others. Not all airports can accept live animal imports. "
             "Always confirm your arrival airport has approved animal import facilities."),
            ("Rabies titre test and preparation timeline",
             "For most origin countries, China requires a rabies titre test with a minimum result "
             "of 0.5 IU/ml. The test must be done at a GACC-approved laboratory. A waiting period "
             "applies after a successful titre test before China entry.\n\n"
             "Typical timeline: microchip first, then primary rabies vaccination, then booster "
             "(if required), then titre test (at least 30 days after vaccination), then waiting "
             "period, then health certificate issued close to travel date.\n\n"
             "Start this process at least 6-8 months before your planned travel date. China's "
             "requirements are unforgiving of documentation errors and the timeline cannot be "
             "shortened once you have missed a step."),
        ]
    ),
    "Taiwan": (
        "high",
        "Taiwan's BAPHIQ (Bureau of Animal and Plant Health Inspection and Quarantine) "
        "administers pet imports. BAPHIQ classifies origin countries into groups with different "
        "requirements. From most origins, pets require microchip, rabies vaccination, a titre "
        "test, and a BAPHIQ-approved health certificate.\n\n"
        "Quarantine is required on arrival. The standard period is 7 days for compliant pets "
        "from approved origins. Pets from higher-risk origins may face 21 days quarantine. "
        "Quarantine must be pre-booked with BAPHIQ before travel.\n\n"
        "An import permit from BAPHIQ is required before your pet travels. The permit application "
        "process takes 2-4 weeks. Do not book flights until the permit is confirmed.",
        [
            ("Import permit and quarantine booking",
             "Apply for an import permit from BAPHIQ before booking flights. The application "
             "requires: microchip number, vaccination records, titre test results (if required "
             "for your origin), and the intended entry date range.\n\n"
             "Once the permit is issued, it is valid for a limited period. Quarantine must also "
             "be pre-booked at an approved BAPHIQ facility. Most quarantine facilities are at "
             "or near Taipei Taoyuan International Airport. The quarantine cost is paid by the "
             "owner on arrival."),
            ("Approved origins and titre test requirements",
             "Taiwan categorises countries by their rabies status. For pets from countries without "
             "rabies (such as the UK, Australia, New Zealand, and others), the process is simpler: "
             "microchip, valid rabies vaccination, and health certificate. Titre test may not be "
             "required from some approved origins.\n\n"
             "For pets from countries where rabies is present (most of Asia, Africa, South America), "
             "a titre test is required with a minimum result of 0.5 IU/ml. A waiting period applies "
             "after a successful test. Check the BAPHIQ website for the current approved country "
             "list and requirements for your specific origin."),
        ]
    ),
    "Vietnam": (
        "high",
        "Vietnam requires an import permit from DAH (Department of Animal Health, under the "
        "Ministry of Agriculture and Rural Development, MARD) before any pet can be imported. "
        "The permit takes several weeks to obtain. Pets must be microchipped, vaccinated "
        "against rabies, and accompanied by a health certificate endorsed by the origin "
        "country's official vet authority.\n\n"
        "Quarantine may be required on arrival depending on origin country and the health "
        "status declared in the documentation. Vietnam's import rules have been strengthened "
        "in recent years as the country improves its biosecurity controls.\n\n"
        "Ho Chi Minh City (Tan Son Nhat Airport) and Hanoi (Noi Bai Airport) are the main "
        "entry points for pet imports into Vietnam. Not all entry points have veterinary "
        "inspection facilities, so always confirm your entry point before booking.",
        [
            ("Import permit process for Vietnam",
             "Submit the import permit application to DAH before booking flights. Required: "
             "microchip details, vaccination records, health certificate from origin vet authority, "
             "photos of the pet, and owner information.\n\n"
             "Processing takes several weeks. Allow at least 4-6 weeks from application to "
             "permit issue. The permit specifies the entry window, entry point, and other "
             "conditions. Travel must comply with the permit conditions."),
            ("Health certificate requirements from Vietnam",
             "For pets coming from the UK, EU, US, or Australia, a health certificate endorsed "
             "by the origin country's official vet authority (APHA, USDA APHIS, DAFF, etc.) "
             "is required. The certificate must list: microchip number, rabies vaccination "
             "date and expiry, other vaccinations, and a general health statement.\n\n"
             "The certificate must typically be issued within 7-10 days before travel. "
             "Some origin countries are required to have their certificate apostilled or "
             "endorsed by the Vietnamese embassy. Check with DAH or a specialist agent "
             "for your specific origin country requirements."),
        ]
    ),
    "Sri_Lanka": (
        "high",
        "Sri Lanka has strict pet import rules reflecting its rabies-free status for dogs. "
        "The DAPH (Department of Animal Production and Health) administers all pet imports. "
        "An import permit must be obtained before travel. All dogs require microchip, rabies "
        "vaccination, a titre test with a minimum result of 0.5 IU/ml, and a government-"
        "endorsed health certificate.\n\n"
        "After a successful titre test, a 3-month waiting period applies before Sri Lanka "
        "entry. This means the total preparation time, from starting vaccinations to arrival "
        "in Sri Lanka, is at least 6-7 months for most origins.\n\n"
        "Quarantine on arrival is mandatory for most origins. The quarantine period is "
        "typically 3-7 days for compliant pets. Longer quarantine applies for pets where "
        "the documentation has any gaps.",
        [
            ("Titre test and waiting period for Sri Lanka",
             "Sri Lanka requires a rabies titre test for dogs from most origins. The blood draw "
             "must be at least 30 days after the rabies vaccination. The test must be conducted "
             "at an internationally recognised laboratory. A minimum result of 0.5 IU/ml is required.\n\n"
             "After a successful titre test, a 3-month waiting period must pass before the dog "
             "can enter Sri Lanka. Plan your timeline from the vaccination date: "
             "vaccination (month 1) → titre test blood draw (month 2) → waiting period (months 3-5) → "
             "travel (month 6+). Start this process as early as possible."),
            ("Quarantine facilities and permit application",
             "Apply for an import permit from DAPH well in advance of your travel date. "
             "Required documents: microchip certificate, vaccination records, titre test results, "
             "and a completed DAPH application form.\n\n"
             "Quarantine is carried out at approved government facilities. The cost and duration "
             "depends on origin and documentation. Pre-book your quarantine before travel. "
             "Colombo Bandaranaike International Airport is the main entry point for pet imports. "
             "Contact DAPH directly for current processing times and approved facility lists."),
        ]
    ),
    "Argentina": (
        "moderate",
        "Argentina's pet import rules are administered by SENASA (Servicio Nacional de Sanidad "
        "y Calidad Agroalimentaria). The process is generally straightforward for pets from "
        "most developed countries. No advance import permit is required for most origins.\n\n"
        "Pets require a microchip (or tattoo, though microchip is strongly preferred), "
        "up-to-date vaccinations including rabies, and a health certificate endorsed by "
        "SENASA in the origin country. For pets from Europe and North America, the certificate "
        "must be endorsed by the origin country's official vet authority and countersigned "
        "by the Argentine consulate or apostilled in some cases.\n\n"
        "Argentina does not require routine quarantine for compliant pets. Buenos Aires "
        "Ezeiza International Airport handles most pet movements into Argentina and has "
        "a SENASA inspection office.",
        [
            ("Health certificate and consulate endorsement",
             "For pets from EU countries, the UK, and the US, SENASA requires the health "
             "certificate to be endorsed by the national vet authority in the origin country "
             "(APHA, USDA APHIS, DGAV, NVWA, etc.) and, for some origins, also endorsed by "
             "the Argentine consulate or apostilled.\n\n"
             "Check with the Argentine consulate in your origin country whether consulate "
             "endorsement is required. The process takes additional time and has a fee. "
             "The health certificate must typically be issued within 10 days of travel."),
            ("Travelling to Argentina with a cat",
             "Cats follow the same general import process as dogs. Microchip, rabies "
             "vaccination (where applicable), and health certificate are required. "
             "Argentina does not have strict breed restrictions for cats.\n\n"
             "Some vaccinations required for dogs (parvovirus, distemper, hepatitis) may "
             "also be noted on cat health certificates for completeness. Check the SENASA "
             "website or contact a specialist agent for the current required vaccines "
             "for cats entering Argentina."),
        ]
    ),
    "Chile": (
        "moderate",
        "Chile has relatively clear pet import rules administered by SAG (Servicio Agricola "
        "y Ganadero). Dogs and cats from most countries require a microchip, valid rabies "
        "vaccination, and a health certificate endorsed by SAG in the origin country. No "
        "pre-import permit is needed for most origins.\n\n"
        "Chile takes its biosecurity seriously, particularly because it borders Peru, "
        "Bolivia, and Argentina where some animal diseases circulate. The health certificate "
        "and vaccination records are checked carefully on arrival. SAG has a streamlined "
        "process and the documentation requirements are clearly published on the SAG website.\n\n"
        "Santiago's Arturo Merino Benitez Airport handles most pet imports into Chile and "
        "has a SAG inspection area.",
        [
            ("What SAG requires on arrival in Chile",
             "On arrival, SAG officials will inspect: the original health certificate (endorsed "
             "by the origin country's official vet authority), vaccination records (rabies "
             "and required others), microchip documentation.\n\n"
             "The health certificate must typically be issued within 10 days of travel and "
             "must be endorsed by SAG at the origin side (i.e., the Chilean consulate or "
             "SAG representative in your origin country countersigns it). This double-endorsement "
             "requirement catches some owners by surprise. Check the SAG website for the "
             "current endorsed certificate format for your specific origin country."),
            ("Brief SAG holding period on arrival",
             "Pets arriving in Chile from some origins may be subject to a brief SAG inspection "
             "period. If your documentation is complete, this is usually resolved quickly. "
             "In some cases, SAG may require a short observation period (typically up to 5 days) "
             "at an approved facility if there are any documentation gaps or health concerns.\n\n"
             "To avoid delays, have all original documentation organised and ready for SAG "
             "inspection on arrival. Do not carry only copies."),
        ]
    ),
    "Colombia": (
        "moderate",
        "Colombia's ICA (Instituto Colombiano Agropecuario) handles pet imports. Dogs and "
        "cats need a microchip, valid rabies vaccination certificate, and an official health "
        "certificate. For some origins, a rabies titre test is also required. The health "
        "certificate must be endorsed by the origin country's official vet authority.\n\n"
        "No advance import permit is required for most origins. Colombia's pet import process "
        "has become more organised in recent years and the documentation requirements are "
        "clearer than they used to be. Bogota El Dorado International Airport is the main "
        "entry point for international pet imports into Colombia.\n\n"
        "Colombia does not require routine quarantine for compliant pets. ICA officers at "
        "the airport inspect the documentation and the pet on arrival.",
        [
            ("Health certificate requirements for Colombia",
             "The health certificate must list: microchip number, rabies vaccination date "
             "and expiry, other required vaccinations, and a general health statement signed "
             "by an accredited vet. The certificate must then be endorsed by the official vet "
             "authority in the origin country (APHA for UK, USDA APHIS for US, etc.).\n\n"
             "For some origins, Colombia also requires the health certificate to be endorsed "
             "by the Colombian consulate in the origin country. Check with ICA or the "
             "Colombian consulate for the current requirements for your specific origin."),
            ("Restrictions on certain breeds in Colombia",
             "Colombia has breed-specific legislation. Several breeds are restricted or require "
             "special registration, including Pit Bull Terrier types, Rottweiler, Dogo Argentino, "
             "Fila Brasileiro, and similar breeds. Restricted breeds must be registered with "
             "local authorities on arrival and may face additional restrictions on public spaces.\n\n"
             "If your dog is a breed that might be on Colombia's restricted list, research "
             "the current legislation before travel. The rules are enforced and "
             "non-compliance can result in seizure of the animal."),
        ]
    ),
    "Egypt": (
        "high",
        "Egypt requires an import permit from GOVS (General Organisation for Veterinary Services) "
        "before importing a pet. Permits must be obtained at least 2 weeks before travel. Pets "
        "must be microchipped and vaccinated against rabies (and other diseases as specified).\n\n"
        "The health certificate from the origin country must be endorsed by the national vet "
        "authority and, for some origins, also endorsed by the Egyptian consulate or embassy. "
        "This double-endorsement requirement adds time and cost to the process.\n\n"
        "Cairo International Airport handles the majority of pet imports into Egypt and has "
        "a GOVS inspection office. Pets arriving without the import permit may be refused "
        "entry or detained.",
        [
            ("Import permit and consulate endorsement for Egypt",
             "Apply for the import permit from GOVS at least 3-4 weeks before travel. "
             "Required documents: microchip certificate, vaccination records, and a completed "
             "GOVS application form. The permit is issued with a specific entry window.\n\n"
             "In addition to GOVS permission, pets from many origin countries also need their "
             "health certificate endorsed by the Egyptian consulate in the origin country. "
             "The consulate endorsement is separate from the GOVS permit. Allow time for both."),
            ("Restrictions and special rules in Egypt",
             "Egypt has restrictions on certain dog breeds, particularly large or 'fighting' "
             "breeds. The list includes Pit Bull types, Rottweiler, and similar. Check with "
             "GOVS for the current breed restriction list before travel.\n\n"
             "Egypt also has rules about the number of pets a traveller can bring. "
             "Generally, one or two pets per person is acceptable for personal travel. "
             "Importing multiple animals for commercial purposes requires a separate process "
             "and may not be permitted for individuals."),
        ]
    ),
    "Kenya": (
        "high",
        "Kenya requires an import permit from the Directorate of Veterinary Services (DVS) "
        "before any pet can be imported. The permit is obtained by submitting health "
        "documentation to DVS. Pets need microchip, rabies vaccination, and an official "
        "health certificate endorsed by the origin country's authority.\n\n"
        "Some origins also require a rabies titre test. Mandatory quarantine is required "
        "on arrival at the owner's expense (typically 7 days for compliant pets). The "
        "quarantine facility must be pre-booked before travel.\n\n"
        "Nairobi Jomo Kenyatta International Airport is the main entry point for pet "
        "imports into Kenya. DVS has an inspection office at the airport.",
        [
            ("Import permit and quarantine for Kenya",
             "Apply to DVS for an import permit before booking flights. Required: microchip "
             "details, vaccination records, health certificate from origin vet authority, "
             "and owner information.\n\n"
             "Once approved, the permit specifies conditions including quarantine details. "
             "Quarantine is mandatory and must be pre-booked at an approved government facility. "
             "Most quarantine facilities are located near Nairobi. The quarantine period is "
             "typically 7 days. Costs are paid directly to the facility."),
            ("Vaccinations required to enter Kenya",
             "Kenya requires rabies vaccination as a minimum. For dogs, additional vaccinations "
             "typically required include distemper, parvovirus, hepatitis, and leptospirosis. "
             "For cats: feline parvovirus (panleukopenia), herpesvirus, and calicivirus. "
             "All vaccinations must be current at the time of entry.\n\n"
             "Check with DVS or your specialist agent for the current vaccination list as "
             "requirements may be updated. Present original vaccination certificates, not copies."),
        ]
    ),
    "Nigeria": (
        "very_high",
        "Nigeria has strict and at times complex pet import rules. All pets must have a valid "
        "import permit from FDVPCS (Federal Department of Veterinary and Pest Control Services). "
        "The permit process can take several months, so allow plenty of time.\n\n"
        "Pets must be microchipped, vaccinated against rabies and other listed diseases, and "
        "accompanied by a health certificate endorsed by the origin country's authority. "
        "Quarantine on arrival is required (typically 14-30 days at the owner's expense). "
        "Nigeria's import rules have some breed-specific restrictions.\n\n"
        "Lagos Murtala Muhammed International Airport and Abuja Nnamdi Azikiwe International "
        "Airport are the main entry points. Both have FDVPCS veterinary inspection offices.",
        [
            ("Import permit and quarantine process for Nigeria",
             "Apply for the import permit through FDVPCS well in advance. Required documents: "
             "microchip details, full vaccination history, health certificate from origin vet "
             "authority, and owner information. The permit process can take 4-8 weeks or longer.\n\n"
             "Quarantine on arrival is mandatory. The standard period is 14 days, though this "
             "can be extended if health concerns arise. Quarantine facilities are government-run "
             "and must be pre-booked. Cost is the owner's responsibility. Pre-book as soon as "
             "your permit is approved."),
            ("Breed restrictions and import limitations in Nigeria",
             "Nigeria restricts certain dog breeds. Bull-type breeds (Pit Bull, American "
             "Staffordshire Terrier, etc.) and some large working breeds face restrictions "
             "or may be prohibited. The list is strictly enforced at the border.\n\n"
             "Nigeria also limits the number of pets per person for personal imports. "
             "If you are moving with multiple pets, each animal needs its own permit. "
             "Given the processing time, apply for all permits simultaneously as early "
             "as possible. Working with a specialist Nigerian pet import agent is "
             "strongly recommended given the complexity of the process."),
        ]
    ),
    "Czech_Republic": (
        "moderate",
        "The Czech Republic is an EU member state and follows the EU Pet Travel Scheme. "
        "The SVA (State Veterinary Administration / Statni veterinarni sprava) handles "
        "import controls. For EU/EFTA pets: EU Pet Passport. For pets from the UK, US, "
        "and other non-EU countries: an EU Animal Health Certificate (AHC).\n\n"
        "The Czech Republic does not require quarantine for compliant pets. Prague Vaclav "
        "Havel Airport handles most pet movements into the country and has official "
        "veterinary check facilities.\n\n"
        "The Czech Republic borders several non-EU countries including Ukraine and Belarus, "
        "and the SVA has experience handling third-country pet movements.",
        [
            ("Pets from non-EU countries entering the Czech Republic",
             "From the UK: an AHC endorsed by APHA is required. From the US: a USDA APHIS-"
             "endorsed health certificate in EU AHC format. From Australia: a health certificate "
             "endorsed by DAFF.\n\n"
             "All non-EU pets need: ISO microchip, valid rabies vaccination, and the endorsed "
             "health certificate. From countries where a titre test is required, the blood "
             "must be drawn at least 30 days after vaccination and the pet must wait 3 months "
             "after a successful result before EU entry. Pre-notify SVA for third-country imports."),
            ("Using the Czech Republic as an EU entry point",
             "Pets from non-EU countries sometimes enter the EU through the Czech Republic, "
             "particularly those arriving overland from Ukraine, Poland or Slovakia. The Czech "
             "Republic has an official EU entry point at Prague Airport and at road border "
             "crossings with approved Border Inspection Posts (BIPs).\n\n"
             "If entering the EU through the Czech Republic before travelling to another EU "
             "member state, all documentation must comply with EU import rules. Once through "
             "Czech border control, the pet can move freely within the Schengen area."),
        ]
    ),
    "Romania": (
        "moderate",
        "Romania is an EU member state following the EU Pet Travel Scheme. ANSVSA "
        "(Autoritatea Nationala Sanitara Veterinara si pentru Siguranta Alimentelor) "
        "administers import controls. EU/EFTA pets use EU Pet Passports. Non-EU pets "
        "need an AHC endorsed by the origin country's official vet authority.\n\n"
        "Romania shares borders with Ukraine and Moldova and has become a route into "
        "the EU for people and pets displaced from conflict zones. The ANSVSA has set "
        "up pragmatic procedures for these specific circumstances. For standard pet "
        "moves, the process follows normal EU rules.\n\n"
        "Bucharest Henri Coanda Airport is the main international pet entry point "
        "for Romania and has official veterinary inspection facilities.",
        [
            ("Standard EU rules for pets entering Romania",
             "For pets from EU/EEA countries, a valid EU Pet Passport is all that is "
             "needed. The passport must show a current rabies vaccination and ISO microchip. "
             "For dogs from certain origins, tapeworm treatment may be required within 1-5 "
             "days of entry.\n\n"
             "For pets from non-EU countries, an AHC is required. From the UK: APHA-endorsed "
             "AHC. From the US: USDA APHIS-endorsed health certificate. The certificate "
             "must be issued within 10 days of travel for most origins."),
            ("Pets displaced from Ukraine entering Romania",
             "Romania established specific temporary procedures for pets accompanying "
             "people fleeing conflict in Ukraine. These procedures have evolved over time. "
             "If you are in this situation, contact ANSVSA or a registered vet in Romania "
             "for the most current guidance. General EU import rules still apply as a baseline."),
        ]
    ),
    "Malta": (
        "moderate",
        "Malta is an EU member state with additional attention to biosecurity as an island. "
        "The VRD (Veterinary Regulation Directorate) administers pet imports. EU/EFTA pets "
        "use EU Pet Passports. Non-EU pets need an AHC endorsed by the origin country's "
        "official vet authority.\n\n"
        "Malta's island status means it has historically been careful about animal disease "
        "controls. All documentation must be correct before your pet is allowed off the plane. "
        "Malta International Airport has a veterinary inspection point for imported animals.\n\n"
        "Pets from non-EU countries with certain titre test requirements face the same "
        "3-month waiting period after a successful test as for other EU island nations. "
        "Start the process early for non-EU origins.",
        [
            ("Non-EU pets entering Malta",
             "From the UK: an AHC endorsed by APHA within 10 days of travel is required. "
             "From the US: a USDA APHIS-endorsed health certificate in EU AHC format. "
             "Both must show a valid ISO microchip and current rabies vaccination.\n\n"
             "From countries where a titre test is required (generally countries outside "
             "the EU/US/UK/Australia approved list), blood must be drawn at least 30 days "
             "after vaccination and a 3-month waiting period applies after a successful "
             "result before Malta entry."),
            ("Malta and re-entry to the UK",
             "If you are taking your pet from Malta back to the UK, note that UK entry rules "
             "are now separate from EU rules (post-Brexit). Your pet will need a GB Pet Passport "
             "or AHC for UK entry. Malta-based vets can issue AHCs for UK-bound pets. "
             "Ensure your pet is microchipped to ISO standard and has a valid rabies "
             "vaccination before organising the AHC for the return journey."),
        ]
    ),
    "Cyprus": (
        "high",
        "Cyprus is an EU member state with strict biosecurity controls reflecting its "
        "island status and historically rabies-free status. DVS (Department of Veterinary "
        "Services) administers pet imports. EU/EFTA pets use EU Pet Passports. Non-EU pets "
        "need an AHC endorsed by the origin country's official vet authority.\n\n"
        "Cyprus requires advance notification for all pet arrivals. For pets from non-EU "
        "countries, DVS must be contacted before travel and the relevant documentation "
        "submitted for pre-approval. Titre test requirements from some origins apply with "
        "a 3-month waiting period.\n\n"
        "Larnaca International Airport is the main entry point for pets entering Cyprus. "
        "There is a DVS inspection office at the airport.",
        [
            ("Advance notification and non-EU entry to Cyprus",
             "Before bringing a pet from outside the EU into Cyprus, contact DVS in advance. "
             "For some origins, pre-approval is required before the pet is allowed to travel. "
             "This is particularly important for pets from countries where rabies is endemic.\n\n"
             "From the UK: AHC endorsed by APHA, plus pre-notification to DVS. "
             "From the US: USDA APHIS-endorsed health certificate, plus pre-notification. "
             "From countries requiring a titre test: blood drawn at least 30 days post-vaccination, "
             "minimum 0.5 IU/ml result, then a 3-month waiting period before Cyprus entry."),
            ("Re-entry to other EU countries from Cyprus",
             "Cyprus uses the EU Pet Travel Scheme, so pets with EU Pet Passports can travel "
             "freely between Cyprus and other EU member states. Note that direct routes between "
             "Cyprus and some neighbouring non-EU countries (Turkey, Lebanon, etc.) may have "
             "different rules.\n\n"
             "Cyprus vets can issue EU Pet Passports for pets registered in Cyprus. If you are "
             "relocating from Cyprus to another EU country, ensure your pet's EU Pet Passport "
             "is up to date before travel. For return trips to the UK, an AHC is required."),
        ]
    ),
}

# ============================================================
# HELPER: flatten import requirements from JSON data
# ============================================================
def flatten_import_reqs(country_key):
    reqs = countries_raw.get(country_key, {}).get("import_requirements", {})
    result = {}

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

    rv = reqs.get("rabies_vaccination", {})
    if isinstance(rv, dict):
        parts = ["Required"]
        if rv.get("minimum_age_weeks"):
            parts.append(f"Minimum age: {rv['minimum_age_weeks']} weeks")
        wait = rv.get("wait_after_first_vaccination_days") or rv.get("wait_after_vaccination_days")
        if wait:
            parts.append(f"{wait}-day wait after vaccination before travel")
        if rv.get("notes"):
            parts.append(rv["notes"])
        result["rabies_vaccination"] = ". ".join(parts)
    elif rv:
        result["rabies_vaccination"] = str(rv)
    else:
        result["rabies_vaccination"] = "Required"

    tt = reqs.get("rabies_titre_test", {})
    if isinstance(tt, dict):
        if tt.get("required") is False:
            result["titre_test"] = tt.get("notes", "Not required for most origins")
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
            if parts:
                result["titre_test"] = ". ".join(parts)
    elif tt:
        result["titre_test"] = str(tt)

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
            elif isinstance(fac, str) and fac:
                parts.append(f"Facility: {fac}")
            if q.get("notes"):
                parts.append(q["notes"])
            result["quarantine"] = ". ".join(parts)
        elif q.get("required") is False:
            note = "No routine quarantine for compliant pets"
            if q.get("notes"):
                note = q["notes"]
            result["quarantine"] = note
        else:
            result["quarantine"] = q.get("notes", "Check current requirements with destination authority")
    elif q:
        result["quarantine"] = str(q)

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

    hc = reqs.get("health_certificate", {})
    if isinstance(hc, dict):
        parts = ["Required"]
        if hc.get("name"):
            parts.append(hc["name"])
        if hc.get("issued_by"):
            parts.append(f"Issued by: {hc['issued_by']}")
        valid = hc.get("valid_for_days") or hc.get("valid_for_entry_days")
        if valid:
            parts.append(f"Valid for {valid} days from issue")
        if hc.get("notes"):
            parts.append(hc["notes"])
        result["health_certificate"] = ". ".join(parts)
    elif hc:
        result["health_certificate"] = str(hc)
    else:
        result["health_certificate"] = "Required. Government-issued veterinary health certificate"

    bans = reqs.get("banned_breeds", {})
    if isinstance(bans, dict) and bans.get("banned_types"):
        banned_list = [str(b) for b in bans["banned_types"][:6]]
        result["banned_breeds"] = ", ".join(banned_list)
    elif isinstance(bans, dict) and bans.get("notes"):
        result["banned_breeds"] = bans["notes"]

    return result


def esc(s):
    return str(s).replace('"', "'").replace("\n", " ").strip()


# ============================================================
# ORIGIN HUB OVERVIEWS (short, used in origin hub pages)
# ============================================================
ORIGIN_OVERVIEWS = {
    "Ireland":        lambda n, c: f"Ireland uses the EU Pet Travel Scheme. For EU/EFTA travel, an EU Pet Passport is the main document. For non-EU destinations, a DAFM-endorsed AHC is required. We cover {c} routes from Ireland.",
    "Norway":         lambda n, c: f"Norway participates in the EU Pet Travel Scheme as an EEA country. For non-EU destinations, a Mattilsynet-endorsed health certificate is required. Dogs need tapeworm treatment before entry. We cover {c} routes from Norway.",
    "Sweden":         lambda n, c: f"Sweden uses the EU Pet Travel Scheme. For EU/EFTA travel: EU Pet Passport. For non-EU destinations: Jordbruksverket-endorsed AHC. We have guides for {c} routes from Sweden.",
    "Austria":        lambda n, c: f"Austria uses the EU Pet Travel Scheme. For EU/EFTA travel: EU Pet Passport. For non-EU destinations: BMSGPK-endorsed AHC. We cover {c} routes from Austria.",
    "Belgium":        lambda n, c: f"Belgium uses the EU Pet Travel Scheme. Brussels Airport handles significant pet volumes. For non-EU destinations: FASFC-endorsed AHC. We have guides for {c} routes from Belgium.",
    "Poland":         lambda n, c: f"Poland uses the EU Pet Travel Scheme. For EU/EFTA travel: EU Pet Passport. For non-EU destinations: GIW-endorsed AHC. We cover {c} routes from Poland.",
    "Turkey":         lambda n, c: f"Pet export from Turkey requires a health certificate endorsed by the Ministry of Agriculture (TRGM). Some destinations also require an apostille. We have guides for {c} routes from Turkey.",
    "Israel":         lambda n, c: f"Pet export from Israel requires an IVS-endorsed health certificate. Some destinations also require a titre test. We cover {c} routes from Israel.",
    "Saudi_Arabia":   lambda n, c: f"Pet export from Saudi Arabia requires a MEWA-endorsed health certificate. Some destinations require consulate endorsement. We have guides for {c} routes from Saudi Arabia.",
    "Qatar":          lambda n, c: f"Pet export from Qatar requires a MECC-endorsed health certificate. Start the process early. We cover {c} routes from Qatar.",
    "Kuwait":         lambda n, c: f"Pet export from Kuwait requires a PAM-endorsed health certificate. We have guides for {c} routes from Kuwait.",
    "China":          lambda n, c: f"Pet export from China requires endorsement by GACC or local CIQ. Allow extra time for the endorsement process. We cover {c} routes from China.",
    "Taiwan":         lambda n, c: f"Pet export from Taiwan requires a BAPHIQ health certificate. Requirements vary by destination. We have guides for {c} routes from Taiwan.",
    "Vietnam":        lambda n, c: f"Pet export from Vietnam requires a DAH-endorsed health certificate issued within 7 days of travel. We cover {c} routes from Vietnam.",
    "Sri_Lanka":      lambda n, c: f"Pet export from Sri Lanka requires a DAPH-endorsed health certificate. Plan well in advance. We have guides for {c} routes from Sri Lanka.",
    "Argentina":      lambda n, c: f"Pet export from Argentina requires a SENASA-endorsed health certificate. Some destinations require additional consulate endorsement. We cover {c} routes from Argentina.",
    "Chile":          lambda n, c: f"Pet export from Chile requires a SAG-endorsed health certificate. The double-endorsement process can take extra time. We have guides for {c} routes from Chile.",
    "Colombia":       lambda n, c: f"Pet export from Colombia requires an ICA-endorsed health certificate. No advance permit is needed for most destinations. We cover {c} routes from Colombia.",
    "Egypt":          lambda n, c: f"Pet export from Egypt requires a GOVS-endorsed health certificate. Some destinations also require embassy endorsement. We have guides for {c} routes from Egypt.",
    "Kenya":          lambda n, c: f"Pet export from Kenya requires a DVS-endorsed health certificate. Allow at least 2 weeks for the endorsement process. We cover {c} routes from Kenya.",
    "Nigeria":        lambda n, c: f"Pet export from Nigeria requires a FDVPCS-endorsed health certificate. Allow extra time as processing can take several days. We have guides for {c} routes from Nigeria.",
    "Czech_Republic": lambda n, c: f"Czech Republic uses the EU Pet Travel Scheme. For EU/EFTA travel: EU Pet Passport. For non-EU destinations: SVA-endorsed AHC. We cover {c} routes from Czech Republic.",
    "Romania":        lambda n, c: f"Romania uses the EU Pet Travel Scheme. For EU/EFTA travel: EU Pet Passport. For non-EU destinations: ANSVSA-endorsed AHC. We have guides for {c} routes from Romania.",
    "Malta":          lambda n, c: f"Malta uses the EU Pet Travel Scheme. As an island, Malta takes biosecurity seriously. For non-EU destinations: VRD-endorsed AHC. We cover {c} routes from Malta.",
    "Cyprus":         lambda n, c: f"Cyprus uses the EU Pet Travel Scheme and requires advance notification for all pet arrivals. For non-EU destinations: DVS-endorsed AHC. We have guides for {c} routes from Cyprus.",
}


# ============================================================
# GENERATE ORIGIN HUB
# ============================================================
def generate_origin_hub(country_key):
    country_name, country_code, slug, authority_name, authority_abbrev = P3_COUNTRY_REGISTRY[country_key]

    # Find all outbound routes for this origin
    outbound_routes = []
    for fname in sorted(os.listdir(ROUTES_DIR)):
        if fname.startswith(f"{slug}-to-") and fname.endswith(".md") and fname != "_index.md":
            dest_slug = fname[len(slug) + len("-to-"):-len(".md")]
            dest_name = dest_slug.replace("-", " ").title()
            for k, (n, c, s, *_) in P3_COUNTRY_REGISTRY.items():
                if s == dest_slug:
                    dest_name = n
                    break
            outbound_routes.append((dest_slug, dest_name))

    export_notes = EXPORT_NOTES.get(country_key, ("No formal export permit required.", "Official health certificate required.", "Government endorsement required"))
    export_permit_text, health_cert_text, endorsement_text = export_notes

    airlines = AIRLINES_BY_COUNTRY.get(country_key, [])

    route_lines = "\n".join(
        f"      - [{country_name} to {dest_name}](/pet-transport/{slug}-to-{dest_slug}/)"
        for dest_slug, dest_name in outbound_routes[:20]
    )
    if not route_lines:
        route_lines = f"      Routes from {country_name} are being added. Check back soon."

    overview_fn = ORIGIN_OVERVIEWS.get(country_key)
    overview = overview_fn(country_name, len(outbound_routes)) if overview_fn else \
        f"Shipping your pet from {country_name} requires the right paperwork and planning. We cover {len(outbound_routes)} routes from {country_name} in detail."

    # Title pattern: "[Country] Pet Export Guide" → Hugo slugifies to [country]-pet-export-guide
    md = f"""---
title: "{country_name} Pet Export Guide"
description: "Complete guide to exporting your pet from {country_name}. Export requirements, airline options, and route guides for international destinations."
type: "origins"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
country_name: "{country_name}"
country_code: "{country_code}"
content:
  h1: "Pet Transport from {country_name}"
  overview: |
    {overview}
export_requirements:
  export_permit: "{esc(export_permit_text)}"
  health_certificate: "{esc(health_cert_text)}"
  endorsement: "{esc(endorsement_text)}"
  issuing_authority: "{authority_name} ({authority_abbrev})"
  last_verified: "2026-04-24"
sections:
  - heading: "Export requirements from {country_name}"
    body: |
      **Export Permit:** {export_permit_text}

      **Health Certificate:** {health_cert_text}

      **Government Endorsement:** {endorsement_text}

      **Issuing Authority:** {authority_name} ({authority_abbrev})

      **Last Verified:** 2026-04-24
  - heading: "Popular routes from {country_name}"
    body: |
      We have detailed guides for the following routes:

{route_lines}
faqs:
  - question: "What do I need to export my pet from {country_name}?"
    answer: "{esc(export_permit_text + ' ' + health_cert_text)}"
  - question: "Where can I get a pet health certificate in {country_name}?"
    answer: "Any government-approved veterinarian in {country_name} can issue a health certificate for pet export. The certificate then needs endorsement from {authority_name} ({authority_abbrev}) before departure."
  - question: "How long does pet export take from {country_name}?"
    answer: "Allow at least 4-8 weeks from starting preparations to travel day. Some steps require waiting periods that cannot be shortened. Start the process as early as possible."
airlines:
"""
    for a_name, a_type in airlines:
        md += f'  - name: "{a_name}"\n'
        md += f'    type: "{a_type}"\n'

    md += "outbound_routes:\n"
    for dest_slug, dest_name in outbound_routes[:20]:
        md += f'  - slug: "{slug}-to-{dest_slug}"\n'
        md += f'    destination: "{dest_name}"\n'

    md += "---\n"
    return md


# ============================================================
# GENERATE COUNTRY GUIDE
# ============================================================
def generate_country_guide(country_key):
    country_name, country_code, slug, authority_name, authority_abbrev = P3_COUNTRY_REGISTRY[country_key]

    overview_data = COUNTRY_OVERVIEWS.get(country_key)
    if not overview_data:
        return None

    complexity, overview_text, sections_data = overview_data

    friendliness_map = {
        "low": "relaxed", "relaxed": "relaxed",
        "moderate": "moderate", "high": "moderate",
        "very_high": "strict", "strict": "strict",
    }
    pet_friendliness = friendliness_map.get(complexity, "moderate")

    import_reqs = flatten_import_reqs(country_key)

    title_pool = [
        f"Importing a Pet to {country_name}: Requirements and Full Process",
        f"{country_name} Pet Import: Regulations, Permits and Timeline",
        f"Pet Transport to {country_name} | Requirements and Guide",
        f"How to Bring Your Pet to {country_name} | Import Rules Explained",
    ]
    title = title_pool[hash(slug) % len(title_pool)]

    desc_pool = [
        f"Complete guide to importing your dog or cat into {country_name}. Import requirements, quarantine, permits, and preparation timeline.",
        f"Everything you need to bring your pet to {country_name}: import regulations, vaccinations, permits, and what to expect on arrival.",
        f"{country_name} pet import rules explained. Microchip, rabies vaccination, quarantine status, and health certificate requirements.",
    ]
    desc = desc_pool[hash(slug) % len(desc_pool)]
    if len(desc) > 160:
        desc = desc[:157] + "..."

    reqs = countries_raw.get(country_key, {}).get("import_requirements", {})
    faqs = []

    q_data = reqs.get("quarantine", {})
    if isinstance(q_data, dict):
        if q_data.get("required") is True or q_data.get("mandatory") is True:
            dur = q_data.get("duration_days", "")
            faqs.append({
                "q": f"Is quarantine required when bringing my pet to {country_name}?",
                "a": f"Yes, quarantine is mandatory in {country_name}. {'Your pet will be held for ' + str(dur) + ' days ' if dur else ''}on arrival. The cost is the owner's responsibility. Ensure all documentation is in order before travel to avoid extended quarantine."
            })
        else:
            faqs.append({
                "q": f"Is quarantine required when bringing my pet to {country_name}?",
                "a": f"No routine quarantine is required in {country_name} for pets arriving with correct documentation. Penalty quarantine may apply if any documentation is missing or incorrect."
            })

    tt_data = reqs.get("rabies_titre_test", {})
    if isinstance(tt_data, dict):
        if tt_data.get("required") is False:
            faqs.append({
                "q": f"Is a rabies titre test required to bring my pet to {country_name}?",
                "a": f"No, {country_name} does not generally require a rabies titre test. Your pet still needs a valid rabies vaccination and microchip. Verify current requirements with {authority_abbrev} before travel."
            })
        elif tt_data.get("required") is True or tt_data.get("required_for") or tt_data.get("wait_period_days"):
            wait = tt_data.get("wait_period_days", 90)
            faqs.append({
                "q": f"Is a rabies titre test required to bring my pet to {country_name}?",
                "a": f"Yes, a rabies titre test is required for pets entering {country_name} from most origins. Blood must be drawn at least 30 days after vaccination, and there is a {wait}-day waiting period after a successful result before entry."
            })

    ip_data = reqs.get("import_permit", {})
    if isinstance(ip_data, dict) and ip_data.get("required") is True:
        faqs.append({
            "q": f"Do I need an import permit to bring my pet to {country_name}?",
            "a": f"Yes, an import permit is required. Apply through {authority_name} ({authority_abbrev}) before booking your flight. The permit must be obtained before travel."
        })

    faqs.append({
        "q": f"Can I bring a cat to {country_name}?",
        "a": f"Yes, cats can be imported into {country_name}. The same microchip, vaccination, and health certificate requirements apply as for dogs. Some rules (such as tapeworm treatment) may apply to dogs only. Verify current requirements with {authority_abbrev}."
    })

    faqs.append({
        "q": f"What health certificate does my pet need to enter {country_name}?",
        "a": f"A government-issued veterinary health certificate is required, endorsed by the official vet authority in your origin country. The certificate must be issued close to the travel date (typically within 7-10 days). Contact {authority_abbrev} or a pet transport agent for the required format."
    })

    md = f"""---
title: "{esc(title)}"
description: "{esc(desc)}"
type: "countries"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/pet-transport/countries/{slug}/"
country_name: "{country_name}"
country_code: "{country_code}"
pet_friendliness: "{pet_friendliness}"
seo:
  title: "{esc(title)} | Pet Transport Global"
  description: "{esc(desc)}"
import_requirements:
"""
    for k, v in import_reqs.items():
        if v:
            md += f'  {k}: "{esc(v)}"\n'

    md += f"""content:
  h1: "Importing Your Pet to {country_name}"
  overview: |
"""
    for line in overview_text.split("\n"):
        md += f"    {line}\n"

    if sections_data:
        md += "  sections:\n"
        for heading, body in sections_data:
            md += f'    - heading: "{esc(heading)}"\n'
            md += f'      body: |\n'
            for line in body.split("\n"):
                md += f'        {line}\n'

    md += "faqs:\n"
    for faq in faqs:
        md += f'  - question: "{esc(faq["q"])}"\n'
        md += f'    answer: |\n'
        for line in faq["a"].split("\n"):
            md += f'      {line}\n'

    md += "---\n"
    return md


# ============================================================
# MAIN
# ============================================================
def main():
    origins_generated = 0
    origins_skipped = 0
    countries_generated = 0
    countries_skipped = 0
    errors = 0

    for country_key in P3_KEYS:
        _, _, slug, *_ = P3_COUNTRY_REGISTRY[country_key]

        # --- Origin hub ---
        origin_path = os.path.join(ORIGINS_DIR, f"{slug}.md")
        if os.path.exists(origin_path):
            origins_skipped += 1
            print(f"  [skip origin]   {slug}.md (already exists)")
        else:
            try:
                content = generate_origin_hub(country_key)
                with open(origin_path, "w", encoding="utf-8") as f:
                    f.write(content)
                origins_generated += 1
                print(f"  [origin]   {slug}.md")
            except Exception as e:
                print(f"  ERROR [origin] {slug}: {e}")
                errors += 1

        # --- Country guide ---
        country_path = os.path.join(COUNTRIES_DIR, f"{slug}.md")
        if os.path.exists(country_path):
            countries_skipped += 1
            print(f"  [skip country]  {slug}.md (already exists)")
        else:
            try:
                content = generate_country_guide(country_key)
                if content:
                    with open(country_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    countries_generated += 1
                    print(f"  [country]  {slug}.md")
            except Exception as e:
                print(f"  ERROR [country] {slug}: {e}")
                errors += 1

    print(f"\nDone.")
    print(f"  Origin hubs generated: {origins_generated} | skipped: {origins_skipped}")
    print(f"  Country guides generated: {countries_generated} | skipped: {countries_skipped}")
    print(f"  Errors: {errors}")


if __name__ == "__main__":
    main()
