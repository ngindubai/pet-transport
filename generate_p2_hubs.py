"""
Block 24 / Task 2.3: P2 Origin Hubs + Country Guides
Generates:
  - site/content/origins/[slug].md   (15 P2 origin hubs)
  - site/content/countries/[slug].md (15 P2 country guides)
Skip-if-exists. Never overwrites existing files.
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
# COUNTRY REGISTRY  (all 25 countries)
# JSON key -> (display name, ISO alpha2, slug, authority name, authority abbrev)
# ============================================================
COUNTRY_REGISTRY = {
    "UK":           ("United Kingdom",       "GB", "united-kingdom",      "Animal and Plant Health Agency", "APHA"),
    "USA":          ("United States",        "US", "united-states",       "USDA APHIS", "APHIS"),
    "UAE":          ("United Arab Emirates", "AE", "united-arab-emirates","Ministry of Climate Change and Environment", "MOCCAE"),
    "Australia":    ("Australia",            "AU", "australia",           "Department of Agriculture, Fisheries and Forestry", "DAFF"),
    "Canada":       ("Canada",               "CA", "canada",              "Canadian Food Inspection Agency", "CFIA"),
    "Germany":      ("Germany",              "DE", "germany",             "Federal Ministry of Food and Agriculture", "BMEL"),
    "France":       ("France",               "FR", "france",              "Direction Générale de l'Alimentation", "DGAL"),
    "Singapore":    ("Singapore",            "SG", "singapore",          "Animal and Veterinary Service", "AVS"),
    "Hong_Kong":    ("Hong Kong",            "HK", "hong-kong",          "Agriculture, Fisheries and Conservation Department", "AFCD"),
    "South_Africa": ("South Africa",         "ZA", "south-africa",       "Department of Agriculture, Land Reform and Rural Development", "DALRRD"),
    "Japan":        ("Japan",                "JP", "japan",              "Ministry of Agriculture, Forestry and Fisheries", "MAFF"),
    "Thailand":     ("Thailand",             "TH", "thailand",           "Department of Livestock Development", "DLD"),
    "Philippines":  ("Philippines",          "PH", "philippines",        "Bureau of Animal Industry", "BAI"),
    "Malaysia":     ("Malaysia",             "MY", "malaysia",           "Department of Veterinary Services", "DVS"),
    "India":        ("India",                "IN", "india",              "Department of Animal Husbandry and Dairying", "DAHD"),
    "Portugal":     ("Portugal",             "PT", "portugal",           "Direção-Geral de Alimentação e Veterinária", "DGAV"),
    "Netherlands":  ("Netherlands",          "NL", "netherlands",        "Netherlands Food and Consumer Product Safety Authority", "NVWA"),
    "Italy":        ("Italy",                "IT", "italy",              "Ministero della Salute", "Ministry of Health"),
    "Denmark":      ("Denmark",              "DK", "denmark",            "Danish Veterinary and Food Administration", "DVFA"),
    "Mexico":       ("Mexico",               "MX", "mexico",             "Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria", "SENASICA"),
    "Brazil":       ("Brazil",               "BR", "brazil",             "Ministry of Agriculture, Livestock and Food Supply", "MAPA"),
    "Switzerland":  ("Switzerland",          "CH", "switzerland",        "Federal Food Safety and Veterinary Office", "FSVO"),
    "Indonesia":    ("Indonesia",            "ID", "indonesia",          "Agency for Agricultural Quarantine", "BARANTAN"),
    "South Korea":  ("South Korea",          "KR", "south-korea",        "Animal and Plant Quarantine Agency", "APQA"),
    "Greece":       ("Greece",               "GR", "greece",             "Ministry of Rural Development and Food", "MRDF"),
}

P2_KEYS = [
    "Japan", "Thailand", "Philippines", "Malaysia", "India",
    "Portugal", "Netherlands", "Italy", "Denmark", "Mexico",
    "Brazil", "Switzerland", "Indonesia", "South Korea", "Greece",
]

# Airlines relevant to each P2 origin (flag carrier + connecting airlines)
AIRLINES_BY_COUNTRY = {
    "Japan":        [("Japan Airlines (JAL)", "cargo_only"), ("ANA (All Nippon Airways)", "cargo_only"), ("Korean Air", "cabin_and_cargo"), ("Cathay Pacific", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Emirates", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Qantas", "cargo_only"), ("Air France", "cabin_and_cargo")],
    "Thailand":     [("Thai Airways", "cargo_only"), ("Bangkok Airways", "cabin_only"), ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"), ("Emirates", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Qantas", "cargo_only"), ("Korean Air", "cabin_and_cargo")],
    "Philippines":  [("Philippine Airlines", "cabin_and_cargo"), ("Cebu Pacific", "cargo_only"), ("Cathay Pacific", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Emirates", "cargo_only"), ("Korean Air", "cabin_and_cargo"), ("Japan Airlines (JAL)", "cargo_only"), ("Qantas", "cargo_only"), ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo")],
    "Malaysia":     [("Malaysia Airlines", "cabin_and_cargo"), ("AirAsia", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"), ("Emirates", "cargo_only"), ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Qantas", "cargo_only"), ("Korean Air", "cabin_and_cargo")],
    "India":        [("Air India", "cabin_and_cargo"), ("IndiGo", "cabin_only"), ("Emirates", "cargo_only"), ("Etihad Airways", "cargo_only"), ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Air Canada", "cabin_and_cargo")],
    "Portugal":     [("TAP Air Portugal", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Iberia", "cabin_and_cargo"), ("Qantas", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only")],
    "Netherlands":  [("KLM", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only"), ("Cathay Pacific", "cargo_only")],
    "Italy":        [("ITA Airways", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("Etihad Airways", "cargo_only")],
    "Denmark":      [("SAS Scandinavian Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo"), ("KLM", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("Norwegian Air", "cabin_only")],
    "Mexico":       [("Aeromexico", "cabin_and_cargo"), ("American Airlines", "cabin_and_cargo"), ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only"), ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Iberia", "cabin_and_cargo"), ("KLM", "cabin_and_cargo"), ("Air Canada", "cabin_and_cargo")],
    "Brazil":       [("LATAM Airlines", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Emirates", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only"), ("American Airlines", "cabin_and_cargo"), ("Iberia", "cabin_and_cargo"), ("KLM", "cabin_and_cargo")],
    "Switzerland":  [("Swiss International Air Lines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Delta Air Lines", "cabin_and_cargo"), ("Cathay Pacific", "cargo_only")],
    "Indonesia":    [("Garuda Indonesia", "cabin_and_cargo"), ("Batik Air", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"), ("Emirates", "cargo_only"), ("Qantas", "cargo_only"), ("Korean Air", "cabin_and_cargo"), ("Japan Airlines (JAL)", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only")],
    "South Korea":  [("Korean Air", "cabin_and_cargo"), ("Asiana Airlines", "cabin_and_cargo"), ("Japan Airlines (JAL)", "cargo_only"), ("Cathay Pacific", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Emirates", "cargo_only"), ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("Qantas", "cargo_only"), ("Air France", "cabin_and_cargo")],
    "Greece":       [("Aegean Airlines", "cabin_and_cargo"), ("Olympic Air", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"), ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"), ("Qantas", "cargo_only"), ("Etihad Airways", "cargo_only")],
}

# Export requirement notes per P2 country
EXPORT_NOTES = {
    "Japan":       ("No formal export permit required for cats and dogs. A veterinary health certificate endorsed by MAFF is required. The certificate must meet the destination country's format. Certain destinations require rabies vaccination proof and microchip documentation.", "Required. Official export health certificate signed by an accredited veterinarian and endorsed by MAFF (Ministry of Agriculture, Forestry and Fisheries).", "MAFF endorsement required on all export health certificates"),
    "Thailand":    ("No dedicated export permit for pet dogs and cats. An export health certificate issued by DLD is required. Must meet destination country import requirements.", "Required. Official export health certificate from the Department of Livestock Development (DLD). Endorsed by DLD before departure.", "DLD endorsement required"),
    "Philippines": ("Export clearance required from the Bureau of Animal Industry (BAI). Owners must apply with proof of ownership, health certificate, and vaccination records.", "Required. Export health certificate from BAI. Certificate must meet destination country format.", "BAI endorsement required on all export health certificates"),
    "Malaysia":    ("No export permit required for household pets. A health certificate from an accredited veterinarian, endorsed by DVS, is required. Some destinations require additional documentation.", "Required. Official veterinary health certificate endorsed by the Department of Veterinary Services (DVS).", "DVS endorsement required"),
    "India":       ("No formal export permit for cats and dogs as household pets. Health certificate from an accredited veterinarian required. Must be endorsed by the relevant state animal husbandry department and DAHD.", "Required. Government-endorsed veterinary health certificate. Some destinations require DAHD national endorsement in addition to state-level certification.", "State/national endorsement required depending on destination"),
    "Portugal":    ("As an EU member state, Portugal uses the EU Pet Travel Scheme. An EU Pet Passport is the standard travel document for pets going to EU countries. For non-EU destinations, an EU Animal Health Certificate (AHC) is required, endorsed by DGAV.", "EU Animal Health Certificate (AHC) required for travel outside EU. EU Pet Passport for travel within EU/EFTA.", "DGAV endorsement required for non-EU destinations"),
    "Netherlands": ("EU Pet Travel Scheme applies. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU Animal Health Certificate (AHC) endorsed by NVWA is required.", "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "NVWA endorsement required for non-EU destinations"),
    "Italy":       ("EU Pet Travel Scheme applies. EU Pet Passport for EU/EFTA travel. Non-EU destinations require EU AHC endorsed by the Ministry of Health.", "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "Ministry of Health endorsement required for non-EU destinations"),
    "Denmark":     ("EU Pet Travel Scheme applies. EU Pet Passport for EU/EFTA travel. Non-EU destinations require EU AHC endorsed by DVFA.", "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "DVFA endorsement required for non-EU destinations"),
    "Mexico":      ("No formal export permit for pets. Health certificate issued by an accredited veterinarian and endorsed by SENASICA is required for international travel. Certificate must meet destination country requirements.", "Required. Official veterinary health certificate endorsed by SENASICA before departure.", "SENASICA endorsement required"),
    "Brazil":      ("Export health certificate endorsed by MAPA (Ministry of Agriculture) required. Some destinations require specific testing. Brazil requires MAPA endorsement which can take 5-10 business days to process.", "Required. Official export health certificate from an accredited veterinarian, endorsed by MAPA.", "MAPA endorsement required. Allow 5-10 business days processing time."),
    "Switzerland": ("Switzerland is not an EU member but participates in the EU Pet Travel Scheme for movement between Switzerland and EU/EFTA countries. An EU Pet Passport or equivalent is accepted. For non-EU/EFTA destinations, an export health certificate endorsed by FSVO is required.", "EU Pet Passport or FSVO-endorsed health certificate required depending on destination.", "FSVO endorsement required for non-EU/EFTA destinations"),
    "Indonesia":   ("Export certificate from BARANTAN (Agency for Agricultural Quarantine) required. Application must be submitted in advance. Some destination countries have specific requirements beyond the standard Indonesian export health certificate.", "Required. Export health certificate from BARANTAN. Some destinations require additional testing documentation.", "BARANTAN endorsement required"),
    "South Korea": ("No dedicated export permit for household pets. An export health certificate from a government-approved veterinarian, endorsed by APQA, is required. Some destinations require specific disease test results.", "Required. Official export health certificate endorsed by APQA (Animal and Plant Quarantine Agency).", "APQA endorsement required"),
    "Greece":      ("EU Pet Travel Scheme applies. EU Pet Passport for EU/EFTA travel. Non-EU destinations require EU AHC endorsed by the Ministry of Rural Development and Food.", "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "Ministry of Rural Development and Food endorsement required for non-EU destinations"),
}

# Pet import overview per P2 country — unique, warm but expert
COUNTRY_OVERVIEWS = {
    "Japan": (
        "high",
        "Japan's pet import rules are among the most detailed in Asia. The quarantine authority, MAFF (Ministry of Agriculture, Forestry and Fisheries), runs a strict biosecurity programme and the documentation requirements are specific. For most countries, the process takes at least 7 months. For some origins, it can take longer.\n\n"
        "The most important thing to understand about Japan is that the preparation steps must be done in a precise sequence. If any step is done in the wrong order, the timeline resets. Japan checks the dates on every document and will quarantine your pet for an extended period if the sequence is wrong.\n\n"
        "Cats are subject to the same import rules as dogs. Pets arriving without correct documentation can be quarantined for up to 180 days at the owner's expense. Get this right the first time.",
        [
            ("Japan's 180-day rabies programme",
             "For most countries, Japan requires proof that your pet has maintained a valid rabies vaccination for at least 180 days before arrival. This means starting the vaccination sequence early enough that the vaccination record covers the full period. Japan's MAFF checks vaccination dates very carefully.\n\n"
             "The required sequence for most origins: microchip implanted first, then primary rabies vaccination, then booster vaccination (minimum 30 days after primary), then a rabies antibody titre test with a FAVN result of at least 0.5 IU/ml. After the successful blood draw, a minimum 180-day waiting period applies before Japan entry.\n\n"
             "MAFF requires that all tests be conducted at a MAFF-approved laboratory. A list of approved labs is on the MAFF website. Using a non-approved lab will invalidate the test result."),
            ("Booking quarantine before you travel",
             "All imported pets must undergo quarantine in Japan. The standard period is 12 hours for pets arriving with perfect documentation from approved countries. However, if any paperwork is missing, out of sequence, or the titre test date is wrong, the quarantine period can extend to 180 days.\n\n"
             "You must book quarantine with the relevant Animal Quarantine Service (AQS) office before travel. Ports with quarantine facilities include Narita, Tokyo, Osaka (Kansai), and a handful of others. Check the AQS website for the current list and book your arrival port accordingly."),
        ]
    ),
    "Thailand": (
        "moderate",
        "Thailand is a manageable destination for pet import, especially compared to countries like Japan or Australia. There is no mandatory quarantine for pets arriving with correct documentation, which significantly reduces the stress of the process.\n\n"
        "The Department of Livestock Development (DLD) oversees pet imports. An import permit must be obtained before travel, and the health certificate must meet DLD's specific format. The whole process typically takes 6-10 weeks if you start early.\n\n"
        "Dogs arriving from rabies-free countries may benefit from simplified requirements, though the DLD permit is required regardless of origin. Cats generally follow the same process as dogs.",
        [
            ("The import permit: apply before you book",
             "Thailand requires an import permit from the DLD before your pet can enter the country. The permit takes 2-4 weeks to process and must specify your pet's details, the origin country, and the anticipated entry port. Bangkok Suvarnabhumi (BKK) is the main entry point.\n\n"
             "Apply for the permit as soon as you know your travel date. The permit is valid for a specific period, so coordinate the timing with your flight booking. Many owners use a Thai pet import agent to handle this — the DLD process is straightforward but has specific format requirements for the application form."),
            ("Health certificate timing",
             "The veterinary health certificate must be issued within 7 days of departure and must be endorsed by the official government veterinary authority in your origin country. Present the original certificate (not a copy) at the DLD inspection desk on arrival.\n\n"
             "Thailand does not require a rabies titre test for most origins, but does require proof of current rabies vaccination. The microchip must be implanted before the vaccination for the vaccine record to be valid."),
        ]
    ),
    "Philippines": (
        "moderate",
        "The Philippines has a structured pet import system managed by the Bureau of Animal Industry (BAI). The process is manageable but has specific documentation requirements that catch unprepared owners off guard.\n\n"
        "An import permit from the BAI must be obtained before travel. The permit is issued relatively quickly (typically 1-2 weeks for household pets) but must be in place before you fly. Most pets arrive via Manila (NAIA), which has a dedicated animal inspection area.\n\n"
        "The Philippines does not require a rabies titre test for dogs and cats from most origins, making the preparation timeline more flexible than Japan or Australia. A 7-10 day quarantine inspection period may apply on arrival, though full facility quarantine is not required for compliant pets from approved countries.",
        [
            ("Import permit and approved entry points",
             "Apply for the BAI import permit online or through a registered pet transport agent. You'll need your pet's microchip number, rabies vaccination certificate, and health certificate details when applying. The permit specifies the approved port of entry.\n\n"
             "Main ports with animal inspection facilities: Ninoy Aquino International Airport (NAIA) Manila, Mactan Cebu International Airport, and Francisco Bangoy International Airport (Davao). Arrive at the port specified on your import permit — arriving at a different port without prior approval can result in detention of your pet."),
            ("Breed restrictions",
             "The Philippines bans certain dog breeds from import. Banned breeds include Pit Bull Terriers, American Staffordshire Terriers, Staffordshire Bull Terriers, and dogs that are substantially similar in appearance. Mixed breeds with these as a component may also be affected.\n\n"
             "If you own one of these breeds or a breed that could be mistaken for one, contact the BAI directly before making any travel arrangements. Import refusal is enforced at the port."),
        ]
    ),
    "Malaysia": (
        "moderate",
        "Malaysia's pet import rules are managed by the Department of Veterinary Services (DVS). The process is reasonably straightforward for dogs and cats from approved countries, with no mandatory quarantine for pets arriving with correct documentation.\n\n"
        "An import licence from the DVS is required before travel. This is applied for through the DVS and typically takes 2-4 weeks. All pets must arrive at Kuala Lumpur International Airport (KLIA), which has the main DVS inspection facility.\n\n"
        "Malaysia requires pets to be microchipped (ISO standard), vaccinated against rabies, and covered by an official veterinary health certificate. The health certificate must be issued by a government veterinarian in the origin country within 14 days of departure.",
        [
            ("The DVS import licence",
             "Apply for the DVS import licence before booking your flight. The licence specifies the arrival port (KLIA for most international arrivals) and the pet's details. You'll need your pet's microchip number, vaccination history, and a copy of the health certificate format from the origin country.\n\n"
             "Malaysia does not officially require a rabies titre test for most origins, though this is subject to change. Always verify current requirements directly with the DVS or through a registered pet transport agent before finalising your plans."),
            ("Dogs only: tapeworm treatment",
             "Dogs entering Malaysia must be treated for tapeworm (Echinococcus) before arrival if coming from certain countries. Check whether your origin country is on the list that requires treatment. The treatment must be administered by a veterinarian within a specific window before travel and recorded in the health certificate."),
        ]
    ),
    "India": (
        "moderate",
        "India has a two-tier clearance system for pet imports: a No Objection Certificate (NOC) from the Director General of Foreign Trade (DGFT) is required, followed by an import permit from the state Animal Husbandry department at the port of entry. This is the step that causes the most delays for first-time importers.\n\n"
        "The DGFT NOC process has been simplified in recent years, but still requires advance planning. Total preparation time is typically 8-12 weeks. Pets arrive at Mumbai, Delhi, Chennai, or Kolkata, all of which have animal quarantine inspection facilities.\n\n"
        "India does not require mandatory post-arrival quarantine for pets arriving with correct documentation from most countries. However, a vet inspection and documentation check takes place at the airport on arrival.",
        [
            ("DGFT NOC: start this first",
             "The DGFT NOC is the central document for pet import into India. Apply through the DGFT online portal. You'll need your pet's details, the import reason (personal pet / household), origin country, and the entry port. Processing typically takes 2-4 weeks.\n\n"
             "Once the NOC is in hand, you can proceed with the state-level import permit application at your port of entry. Contact the relevant state Animal Husbandry department in advance — requirements and processing times vary by state."),
            ("Airport-specific requirements",
             "The four main entry airports (Delhi, Mumbai, Chennai, Kolkata) each have slightly different procedures. Delhi Indira Gandhi Airport has the most established pet inspection process. Whichever airport you use, confirm the inspection facility operating hours before booking — some ports do not process animal arrivals outside business hours, which can cause overnight detention."),
        ]
    ),
    "Portugal": (
        "relaxed",
        "Portugal is an EU member state and uses the EU Pet Travel Scheme. For pets coming from another EU country or a country listed under EU regulations, the process is relatively smooth. For pets from outside the EU, the process is more involved.\n\n"
        "Portugal does not require mandatory quarantine for pets arriving from EU-listed countries. Pets from non-listed countries may face more detailed checks including potential quarantine. The microchip, vaccination, and health certificate requirements follow the EU standard.\n\n"
        "For most English-speaking countries (UK, USA, Canada, Australia), the process involves a valid EU-format health certificate, rabies vaccination proof, and in some cases a titre test. UK pets specifically need an AHC (Animal Health Certificate) following Brexit.",
        [
            ("EU rules vs. non-EU origins",
             "Portugal follows EU pet import rules administered by DGAV (Direção-Geral de Alimentação e Veterinária). For pets from EU/EFTA countries with an EU pet passport, entry is straightforward. For pets from listed countries (UK, USA, Canada, etc.), an AHC or equivalent is required, endorsed by the origin country's official authority.\n\n"
             "For pets from non-listed countries, a rabies titre test result and a 3-month waiting period after the successful test date are required before the pet can enter Portugal. Contact DGAV directly to confirm the current listing status of your origin country."),
            ("Travelling through Portugal to other EU countries",
             "If your destination is another EU country but you're routing through Lisbon or Porto, the same rules apply as for Portugal itself. Your pet must meet EU import requirements at the first EU port of entry. Portugal uses TRACES (Trade Control and Expert System) for documentary checks."),
        ]
    ),
    "Netherlands": (
        "relaxed",
        "The Netherlands is an EU member state with well-organised pet import procedures managed by the NVWA (Netherlands Food and Consumer Product Safety Authority). The country is a major hub for international travel and the Schiphol Airport (Amsterdam) has an established animal import facility.\n\n"
        "For pets from EU/EFTA countries, an EU Pet Passport is sufficient. For pets from listed countries (UK, USA, Canada, etc.), an endorsed health certificate is required. No mandatory quarantine for compliant pets.\n\n"
        "The Netherlands is often a transit country for pets entering other EU destinations. The same EU rules apply whether the Netherlands is your final destination or an entry point.",
        [
            ("NVWA inspection at Schiphol",
             "All pets arriving from outside the EU enter through Schiphol's dedicated animal import facility. NVWA officers check documentation, microchip, and health certificate on arrival. The inspection is thorough and any missing documentation results in immediate quarantine at the owner's expense.\n\n"
             "Pets arriving as air cargo are held in the cargo facility until documentation is cleared. Allow several hours for this process when planning your arrival logistics."),
            ("Travelling onward within the EU",
             "If you plan to travel onward to another EU country from the Netherlands, your pet is already cleared for EU travel once the NVWA inspection is complete. An EU pet passport or AHC from the origin country covers onward movement within Schengen."),
        ]
    ),
    "Italy": (
        "relaxed",
        "Italy is an EU member state. Pet import follows EU Pet Travel Scheme rules, administered by the Ministry of Health (Ministero della Salute). Rome Fiumicino (FCO) and Milan Malpensa (MXP) are the main entry airports with animal import facilities.\n\n"
        "No mandatory quarantine for pets arriving from EU-listed countries with correct documentation. For pets from non-listed countries, a titre test and 3-month waiting period apply.\n\n"
        "Italy requires the EU standard: microchip, current rabies vaccination, and a valid EU Pet Passport or endorsed health certificate. The certificate must be issued within 10 days of travel.",
        [
            ("Entry through Rome or Milan",
             "Rome Fiumicino is the most common international arrival point for pets entering Italy. The Ministry of Health inspection desk at FCO handles import documentation checks. Milan Malpensa also has animal import capacity. Contact the airport's cargo or live animal section in advance to confirm procedures and operating hours.\n\n"
             "Pets arriving as air cargo must be collected from the cargo terminal. The documentation check by Ministry of Health veterinarians must be completed before your pet is released to you."),
            ("Italy's brachycephalic breed caution",
             "Italy does not have a specific federal ban on brachycephalic breeds, but airlines operating into Italy have their own restrictions. Breeds like French Bulldogs, English Bulldogs, and Pugs face seasonal embargoes on several carriers. If you have a flat-faced breed, check both the airline policy and the transit airport policy well before booking."),
        ]
    ),
    "Denmark": (
        "relaxed",
        "Denmark is an EU member state with pet import procedures managed by the Danish Veterinary and Food Administration (DVFA). Copenhagen Airport (CPH) is the main entry point.\n\n"
        "For pets from EU/EFTA countries, an EU Pet Passport is sufficient. For other origins, an endorsed health certificate is required. No mandatory quarantine for compliant pets.\n\n"
        "Denmark has additional rules for certain breeds under its dog legislation, which is separate from import rules but applies to dogs once they arrive in the country. Some breeds that can be imported may face restrictions on ownership within Denmark.",
        [
            ("Danish breed legislation",
             "Denmark bans 13 specific dog breeds under national law, regardless of how they entered the country. The banned breeds include Pit Bull Terriers, Tosas, American Bulldogs, Fila Brasileiros, Dogo Argentinos, and others. Owners of these breeds cannot legally keep them in Denmark even if import documentation was accepted.\n\n"
             "This is a crucial distinction: import clearance does not override domestic dog legislation. If you own one of these breeds and are moving to Denmark, get specific legal advice before proceeding."),
            ("EU entry at Copenhagen",
             "Pets arriving from outside the EU enter through DVFA's inspection facility at Copenhagen Airport. Documentation checks follow EU import rules. All rabies vaccination, microchip, and health certificate requirements must be met before departure."),
        ]
    ),
    "Mexico": (
        "low",
        "Mexico is one of the more accessible destinations for pet import. SENASICA (the agricultural health authority) manages pet import through a streamlined process. No mandatory quarantine is required for compliant pets, and the documentation requirements are relatively straightforward.\n\n"
        "A veterinary health certificate from an accredited vet in the origin country, endorsed by the origin country's official authority, is the main document required. Mexico City (AICM) and Cancun are the main international arrival airports with established animal inspection processes.\n\n"
        "For pets from the USA and Canada, the process is particularly smooth given the proximity and SENASICA's acceptance of USDA/CFIA-endorsed certificates.",
        [
            ("SENASICA documentation",
             "Mexico requires: a veterinary health certificate issued within 10 days of travel, proof of rabies vaccination (must be current), and proof of internal and external parasite treatment. The health certificate must be endorsed by the official veterinary authority in the origin country (e.g., USDA APHIS for US pets).\n\n"
             "Pets arrive at the SENASICA inspection desk at the airport. The process is generally quick for well-documented pets. Mexico does not require a microchip by federal law, but the destination's rules when you eventually leave Mexico will apply."),
            ("Number of pets and import limits",
             "Mexico allows up to 3 pets per person as household goods. More than 3 pets may require a commercial import process, which is significantly more complex. If you're relocating with multiple animals, confirm the current limit with SENASICA or your airline cargo team before travel."),
        ]
    ),
    "Brazil": (
        "moderate",
        "Brazil's pet import process is managed by MAPA (Ministério da Agricultura, Pecuária e Abastecimento). The country has specific requirements that include a MAPA-endorsed health certificate, and for some origins, a titre test or additional disease screening.\n\n"
        "No mandatory quarantine for pets arriving with correct documentation from approved countries. However, the documentation must be correct in every detail, as Brazilian customs and MAPA take import compliance seriously.\n\n"
        "The process typically takes 8-12 weeks from starting veterinary preparation to travel. São Paulo (GRU) is the main international airport with established MAPA animal inspection capacity.",
        [
            ("Health certificate endorsement by MAPA",
             "Brazil requires the veterinary health certificate to be endorsed by both the origin country's official veterinary authority and the Brazilian consulate or MAPA representative in the origin country. This double-endorsement step adds time to the process — allow at least 2-3 weeks for this paperwork.\n\n"
             "Some origin countries have simplified arrangements with Brazil. Check with your local MAPA representative or a pet transport agent for the current requirement in your specific origin country."),
            ("Arriving in São Paulo",
             "Most international pets arrive at São Paulo Guarulhos International Airport (GRU). The MAPA inspection desk operates during business hours on weekdays. Arranging a weekday daytime arrival avoids the risk of your pet being held overnight. São Paulo's animal inspection facility is well-equipped and the process is typically completed within a few hours for compliant documentation."),
        ]
    ),
    "Switzerland": (
        "relaxed",
        "Switzerland is not an EU member state but participates in the EU Pet Travel Scheme for movement between Switzerland and EU/EFTA countries. For pets coming from EU/EFTA countries, an EU Pet Passport is accepted. For pets from other origins, a health certificate endorsed by the FSVO (Federal Food Safety and Veterinary Office) equivalent is required.\n\n"
        "No mandatory quarantine for compliant pets. Zürich Airport (ZRH) is the main international arrival point with Swiss customs and FSVO inspection facilities.\n\n"
        "Switzerland's requirements closely mirror EU rules: microchip, current rabies vaccination, valid health certificate. For pets from non-EU/EFTA countries (USA, UK, Canada, Australia), the process is similar to entering the EU, with destination-specific variations.",
        [
            ("Switzerland and EU pet rules",
             "Because Switzerland participates in the EU pet scheme bilaterally, a pet arriving in Switzerland from an EU country with a valid EU Pet Passport has a smooth entry. Pets from the UK (post-Brexit) require an AHC endorsed by APHA, just as they would for entering an EU country.\n\n"
             "Pets from countries not on the EU/Switzerland approved list require a rabies titre test and a 3-month waiting period after the successful test. The FSVO website has the current approved country list."),
            ("Zürich customs process",
             "The FSVO veterinary inspection takes place at the cargo terminal for air cargo pets, or at the border check for pets accompanying passengers. For passengers arriving with a pet in the cabin, the passport control area includes a veterinary check point. The process is generally efficient but thorough."),
        ]
    ),
    "Indonesia": (
        "high",
        "Indonesia has strict biosecurity controls for pet imports, managed by BARANTAN (the Agency for Agricultural Quarantine). The country requires a formal import recommendation from BARANTAN before your pet can enter, and all pets undergo a physical inspection and health check on arrival.\n\n"
        "A mandatory quarantine period applies for most incoming pets, though the duration is shorter than some other countries if documentation is in order. Most international arrivals occur at Soekarno-Hatta International Airport (CGK) in Jakarta.\n\n"
        "The process is manageable but requires advance preparation. The BARANTAN import recommendation process and health certificate requirements are specific. Using a local pet agent in Indonesia is recommended for navigating the on-arrival process.",
        [
            ("BARANTAN import recommendation",
             "Apply for the BARANTAN import recommendation before travel. The application requires: your pet's details (species, breed, age, microchip number), origin country, entry port, and accommodation details in Indonesia. The recommendation is issued for a specific flight date and port of entry.\n\n"
             "Processing time is typically 2-4 weeks. The BARANTAN office needs to know your pet is coming and verify that all health documentation will be in order. Arriving without the import recommendation risks rejection at the port."),
            ("On-arrival quarantine inspection",
             "On arrival at Jakarta's Soekarno-Hatta Airport, your pet is taken to the quarantine inspection area. Pets with all documentation in order typically complete the inspection within 1-3 days. Pets with documentation issues can be held for up to 30 days. The cost of quarantine inspection is paid by the owner.\n\n"
             "Indonesia is in a rabies-endemic zone for parts of the country. Pets from rabies-free origins may face different requirements than pets from countries with endemic rabies."),
        ]
    ),
    "South Korea": (
        "moderate",
        "South Korea's pet import process is managed by APQA (Animal and Plant Quarantine Agency). The system is well-organised and the documentation requirements are clear. Most pets from approved countries can enter without mandatory quarantine if paperwork is correct.\n\n"
        "Incheon International Airport (ICN) is the main entry point for international pets. The APQA inspection takes place at the airport and is typically efficient for compliant documentation.\n\n"
        "South Korea does not require a rabies titre test for pets from most approved countries, which significantly reduces the preparation timeline. A standard preparation of 6-8 weeks is generally sufficient for pets from the US, UK, and most European countries.",
        [
            ("Approved country list and requirements",
             "South Korea categorises origin countries by rabies status. Pets from countries classified as rabies-free or low-risk face simplified requirements. For other origins, additional documentation or testing may apply.\n\n"
             "The standard requirements: microchip (ISO 15444 or 11784/11785), valid rabies vaccination (vaccinated after microchipping), and a government-endorsed health certificate from the origin country. The certificate must be in English or Korean — other languages require a certified translation."),
            ("Health certificate: Korean format matters",
             "APQA has a specific preferred format for the health certificate. While it will accept origin-country official formats in most cases, having the certificate match the APQA template avoids delays on arrival. Korean-speaking owners or agents can download the template from the APQA website.\n\n"
             "The health certificate must be issued within 10 days of travel and endorsed by the origin country's official veterinary authority. Present the original at the APQA desk on arrival at Incheon."),
        ]
    ),
    "Greece": (
        "relaxed",
        "Greece is an EU member state and follows EU Pet Travel Scheme rules administered by the Ministry of Rural Development and Food. Athens International Airport (ATH) is the main entry point, with Thessaloniki (SKG) handling some international pet arrivals.\n\n"
        "For pets from EU/EFTA countries, an EU Pet Passport is sufficient. For pets from listed countries (UK, USA, Canada, etc.), an endorsed health certificate is required. No mandatory quarantine for compliant pets.\n\n"
        "Greece is a popular destination for pets of expats and returning Greek nationals. The process is generally smooth for well-documented pets from approved countries.",
        [
            ("EU requirements at Athens",
             "Pets arriving from outside the EU clear through the Ministry of Rural Development and Food inspection at Athens Airport. The documentation check follows standard EU rules: microchip, current rabies vaccination, valid health certificate endorsed by origin country authority.\n\n"
             "For UK pets post-Brexit, an AHC (Animal Health Certificate) endorsed by APHA is required instead of a pet passport. For US pets, a USDA APHIS-endorsed health certificate in EU AHC format is required. Present originals, not copies."),
            ("Greek island travel",
             "If your destination is a Greek island rather than the mainland, factor in the ferry or domestic flight from Athens. Ferries operated by Greek carriers generally accept pets in designated pet areas or kennels. Check individual carrier pet policies before booking."),
        ]
    ),
}

# ============================================================
# HELPER: flatten import requirements for country guides
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
# GENERATE ORIGIN HUB
# ============================================================
def generate_origin_hub(country_key):
    country_name, country_code, slug, authority_name, authority_abbrev = COUNTRY_REGISTRY[country_key]

    # Find all outbound routes for this origin
    outbound_routes = []
    for fname in sorted(os.listdir(ROUTES_DIR)):
        if fname.startswith(f"{slug}-to-") and fname.endswith(".md") and fname != "_index.md":
            dest_slug = fname[len(slug) + len("-to-"):-len(".md")]
            # Look up destination name
            dest_name = dest_slug.replace("-", " ").title()
            for k, (n, c, s, *_) in COUNTRY_REGISTRY.items():
                if s == dest_slug:
                    dest_name = n
                    break
            outbound_routes.append((dest_slug, dest_name))

    export_data = countries_raw.get(country_key, {}).get("export_requirements", {})
    export_notes = EXPORT_NOTES.get(country_key, ("No formal export permit required.", "Official health certificate required.", "Government endorsement required"))
    export_permit_text, health_cert_text, endorsement_text = export_notes

    airlines = AIRLINES_BY_COUNTRY.get(country_key, [])

    # Build route list text
    route_lines = "\n".join(
        f"      - [{country_name} to {dest_name}](/pet-transport/{slug}-to-{dest_slug}/)"
        for dest_slug, dest_name in outbound_routes[:15]
    )

    # Unique overview
    overview_map = {
        "Japan":       f"Moving your pet from Japan involves paperwork that must be done in a specific sequence. MAFF (the Ministry of Agriculture, Forestry and Fisheries) is the authority that endorses all export health certificates. We have detailed guides for {len(outbound_routes)} routes from Japan below.",
        "Thailand":    f"Exporting a pet from Thailand starts with the Department of Livestock Development (DLD). The export health certificate must be issued and endorsed by DLD before departure. We cover {len(outbound_routes)} routes from Thailand.",
        "Philippines": f"The Bureau of Animal Industry (BAI) oversees all pet exports from the Philippines. Export clearance must be obtained before you fly. We have guides for {len(outbound_routes)} routes from the Philippines.",
        "Malaysia":    f"Pet export from Malaysia requires a DVS-endorsed health certificate. Most owners use a licensed pet transport agent to handle the paperwork. We cover {len(outbound_routes)} routes from Malaysia.",
        "India":       f"Exporting a pet from India involves state-level and sometimes national endorsement of the health certificate. The process varies by departure city. We have guides for {len(outbound_routes)} routes from India.",
        "Portugal":    f"Portugal is an EU member state, so pets travelling to other EU countries use the EU Pet Passport system. For non-EU destinations, a DGAV-endorsed health certificate is required. We cover {len(outbound_routes)} routes from Portugal.",
        "Netherlands": f"The Netherlands uses the EU Pet Travel Scheme. Schiphol Airport is one of the most well-organised entry/exit points in Europe for pet transport. We have guides for {len(outbound_routes)} routes from the Netherlands.",
        "Italy":       f"Italy is an EU member state. The Ministry of Health administers pet export documentation. For EU travel: EU Pet Passport. For non-EU destinations: an endorsed AHC. We cover {len(outbound_routes)} routes from Italy.",
        "Denmark":     f"Denmark uses the EU Pet Passport for EU/EFTA travel. For other destinations, the DVFA endorses health certificates. Be aware of Denmark's strict domestic breed legislation before importing a dog. We cover {len(outbound_routes)} routes from Denmark.",
        "Mexico":      f"Exporting a pet from Mexico is relatively straightforward, especially for the USA, Canada, and Europe. SENASICA endorses all export health certificates. We have guides for {len(outbound_routes)} routes from Mexico.",
        "Brazil":      f"Pet export from Brazil requires MAPA endorsement plus, for some destinations, consulate endorsement. Allow extra time for the double-endorsement process. We cover {len(outbound_routes)} routes from Brazil.",
        "Switzerland": f"Switzerland participates in the EU Pet Travel Scheme. For EU/EFTA destinations, an EU Pet Passport is accepted. For other destinations, the FSVO-endorsed health certificate is required. We have guides for {len(outbound_routes)} routes from Switzerland.",
        "Indonesia":   f"Pet export from Indonesia requires BARANTAN certification and endorsement. The process has become more streamlined in recent years but still requires advance planning. We cover {len(outbound_routes)} routes from Indonesia.",
        "South Korea": f"APQA handles all pet export endorsements in South Korea. The process is well-organised and most certificates are turned around within a few days. We have guides for {len(outbound_routes)} routes from South Korea.",
        "Greece":      f"Greece uses the EU Pet Passport system for EU/EFTA travel and the EU AHC for other destinations. The Ministry of Rural Development and Food endorses certificates for non-EU travel. We cover {len(outbound_routes)} routes from Greece.",
    }
    overview = overview_map.get(country_key, f"Shipping your pet from {country_name} requires the right paperwork and planning. We cover {len(outbound_routes)} routes from {country_name} in detail.")

    md = f"""---
title: "Shipping Your Pet from {country_name} | Export Guide"
description: "Complete guide to exporting your pet from {country_name}. Export requirements, airlines, and route guides for {len(outbound_routes)} international destinations."
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
  last_verified: "2026-04-23"
sections:
  - heading: "Export requirements from {country_name}"
    body: |
      **Export Permit:** {export_permit_text}

      **Health Certificate:** {health_cert_text}

      **Government Endorsement:** {endorsement_text}

      **Issuing Authority:** {authority_name} ({authority_abbrev})

      **Last Verified:** 2026-04-23
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
    country_name, country_code, slug, authority_name, authority_abbrev = COUNTRY_REGISTRY[country_key]

    overview_data = COUNTRY_OVERVIEWS.get(country_key)
    if not overview_data:
        return None

    complexity, overview_text, sections_data = overview_data

    # Map complexity to pet_friendliness label
    friendliness_map = {
        "low": "relaxed",
        "relaxed": "relaxed",
        "moderate": "moderate",
        "high": "moderate",  # show 'moderate' for 'high' since template uses title()
        "very_high": "strict",
        "strict": "strict",
    }
    pet_friendliness = friendliness_map.get(complexity, "moderate")

    import_reqs = flatten_import_reqs(country_key)

    # SEO title variants
    title_pool = [
        f"Importing a Pet to {country_name}: Requirements & Full Process",
        f"{country_name} Pet Import: Regulations, Permits & Timeline",
        f"Pet Transport to {country_name} | Requirements & Guide",
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

    # Generate FAQs based on available data
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
                "a": f"No routine quarantine is required in {country_name} for pets arriving with correct documentation. Penalty quarantine may apply if any documentation is missing or incorrect. Get everything right before you travel."
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
                "a": f"Yes, a rabies titre test is required for pets entering {country_name} from most origins. Blood must be drawn at least 30 days after vaccination, and there is a {wait}-day waiting period after a successful result before entry. Start this process early."
            })

    ip_data = reqs.get("import_permit", {})
    if isinstance(ip_data, dict) and ip_data.get("required") is True:
        faqs.append({
            "q": f"Do I need an import permit to bring my pet to {country_name}?",
            "a": f"Yes, an import permit is required. Apply through {authority_name} ({authority_abbrev}) before booking your flight. The permit must be obtained before travel."
        })

    faqs.append({
        "q": f"Can I bring a cat to {country_name}?",
        "a": f"Yes, cats can be imported into {country_name}. The same microchip, vaccination, and health certificate requirements apply as for dogs. Some rules (such as tapeworm treatment) apply to dogs only. Verify current requirements with {authority_abbrev}."
    })

    faqs.append({
        "q": f"What health certificate does my pet need to enter {country_name}?",
        "a": f"A government-issued veterinary health certificate is required, endorsed by the official veterinary authority in your origin country. The certificate must be issued close to the travel date (typically within 7-10 days). Contact {authority_abbrev} or a pet transport agent for the required certificate format."
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

    for country_key in P2_KEYS:
        _, _, slug, *_ = COUNTRY_REGISTRY[country_key]

        # --- Origin hub ---
        origin_path = os.path.join(ORIGINS_DIR, f"{slug}.md")
        if os.path.exists(origin_path):
            origins_skipped += 1
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
