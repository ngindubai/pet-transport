"""
generate_p4_hubs.py — Task 4.2: P4 Origin Hubs + Country Guides
Generates:
  - site/content/origins/[slug].md   (25 P4 origin hubs)
  - site/content/countries/[slug].md (25 P4 country guides)
Skip-if-exists. Never overwrites existing files.

P4 countries: Spain, New Zealand, Oman, Bahrain, Jordan, Finland, Hungary,
  Bulgaria, Croatia, Morocco, Pakistan, Bangladesh, Nepal, Cambodia, Myanmar,
  Peru, Ecuador, Costa Rica, Ghana, Tanzania, Ethiopia, Zimbabwe, Mauritius,
  Slovakia, Luxembourg
"""

import json
import os
import re

REPO_ROOT = r"c:\Users\garet\Desktop\pet-transport"
DATA_DIR = os.path.join(REPO_ROOT, "data")
ORIGINS_DIR = os.path.join(REPO_ROOT, "site", "content", "origins")
COUNTRIES_DIR = os.path.join(REPO_ROOT, "site", "content", "countries")
ROUTES_DIR = os.path.join(REPO_ROOT, "site", "content", "routes")
COUNTRY_DATA = os.path.join(DATA_DIR, "countries_pet_regulations.json")

with open(COUNTRY_DATA, "r", encoding="utf-8") as f:
    countries_raw = json.load(f)["countries"]

# ============================================================
# P4 COUNTRY REGISTRY
# key -> (display name, ISO alpha2, slug, authority name, authority abbrev)
# ============================================================
P4_COUNTRY_REGISTRY = {
    "Spain":       ("Spain",        "ES", "spain",        "Ministerio de Agricultura, Pesca y Alimentacion", "MAPA"),
    "New_Zealand": ("New Zealand",  "NZ", "new-zealand",  "Ministry for Primary Industries", "MPI"),
    "Oman":        ("Oman",         "OM", "oman",         "Ministry of Agriculture, Fisheries and Water Resources", "MAFWR"),
    "Bahrain":     ("Bahrain",      "BH", "bahrain",      "Animal Wealth Directorate, Ministry of Works", "AWD"),
    "Jordan":      ("Jordan",       "JO", "jordan",       "Ministry of Agriculture, General Directorate of Veterinary Services", "GDVS"),
    "Finland":     ("Finland",      "FI", "finland",      "Finnish Food Authority", "Ruokavirasto"),
    "Hungary":     ("Hungary",      "HU", "hungary",      "National Food Chain Safety Office", "NEBIH"),
    "Bulgaria":    ("Bulgaria",     "BG", "bulgaria",     "Bulgarian Food Safety Agency", "BFSA"),
    "Croatia":     ("Croatia",      "HR", "croatia",      "Ministry of Agriculture, Veterinary and Food Safety Directorate", "HRVet"),
    "Morocco":     ("Morocco",      "MA", "morocco",      "Office National de Securite Sanitaire des produits Alimentaires", "ONSSA"),
    "Pakistan":    ("Pakistan",     "PK", "pakistan",     "Animal Quarantine Department, Ministry of National Food Security and Research", "AQD"),
    "Bangladesh":  ("Bangladesh",   "BD", "bangladesh",   "Department of Livestock Services, Ministry of Fisheries and Livestock", "DLS"),
    "Nepal":       ("Nepal",        "NP", "nepal",        "Department of Livestock Services", "DoLS"),
    "Cambodia":    ("Cambodia",     "KH", "cambodia",     "General Directorate of Animal Health and Production, MAFF", "GDAHP"),
    "Myanmar":     ("Myanmar",      "MM", "myanmar",      "Department of Animal Husbandry, Ministry of Agriculture", "DAH"),
    "Peru":        ("Peru",         "PE", "peru",         "Servicio Nacional de Sanidad Agraria", "SENASA-PE"),
    "Ecuador":     ("Ecuador",      "EC", "ecuador",      "Agencia de Regulacion y Control Fitosanitario y de Sanidad Animal", "AGROCALIDAD"),
    "Costa_Rica":  ("Costa Rica",   "CR", "costa-rica",   "Servicio Nacional de Salud Animal, MAG", "SENASA-CR"),
    "Ghana":       ("Ghana",        "GH", "ghana",        "Veterinary Services Directorate, Ministry of Food and Agriculture", "VSD"),
    "Tanzania":    ("Tanzania",     "TZ", "tanzania",     "Ministry of Livestock and Fisheries", "MLF"),
    "Ethiopia":    ("Ethiopia",     "ET", "ethiopia",     "Ministry of Agriculture Animal and Plant Health Regulatory Directorate", "APHRD"),
    "Zimbabwe":    ("Zimbabwe",     "ZW", "zimbabwe",     "Department of Livestock and Veterinary Services", "DLVS"),
    "Mauritius":   ("Mauritius",    "MU", "mauritius",    "Veterinary Services Division, Ministry of Agro-Industry and Food Security", "VSD-MU"),
    "Slovakia":    ("Slovakia",     "SK", "slovakia",     "State Veterinary and Food Administration", "SVFA"),
    "Luxembourg":  ("Luxembourg",   "LU", "luxembourg",   "Administration des services veterinaires", "ASV"),
}

P4_KEYS = list(P4_COUNTRY_REGISTRY.keys())

# Airlines relevant to each P4 origin
AIRLINES_BY_COUNTRY = {
    "Spain":      [("Iberia", "cabin_and_cargo"), ("Vueling", "cargo_only"), ("Air Europa", "cabin_and_cargo"),
                   ("Ryanair", "cargo_only"), ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"), ("Qantas", "cargo_only"),
                   ("American Airlines", "cabin_and_cargo")],
    "New_Zealand": [("Air New Zealand", "cargo_only"), ("Qantas", "cargo_only"),
                    ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                    ("Emirates", "cargo_only"), ("British Airways", "cargo_only"),
                    ("Lufthansa", "cabin_and_cargo"), ("Air Canada", "cabin_and_cargo"),
                    ("Korean Air", "cabin_and_cargo"), ("United Airlines", "cabin_only")],
    "Oman":       [("Oman Air", "cargo_only"), ("flydubai", "cargo_only"), ("Emirates", "cargo_only"),
                   ("Etihad Airways", "cargo_only"), ("Qatar Airways", "cargo_only"),
                   ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Air India", "cabin_and_cargo")],
    "Bahrain":    [("Gulf Air", "cargo_only"), ("Emirates", "cargo_only"), ("Etihad Airways", "cargo_only"),
                   ("flydubai", "cargo_only"), ("Qatar Airways", "cargo_only"),
                   ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Air India", "cabin_and_cargo")],
    "Jordan":     [("Royal Jordanian", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                   ("Lufthansa", "cabin_and_cargo"), ("Qatar Airways", "cargo_only"),
                   ("EgyptAir", "cargo_only"), ("Air France", "cabin_and_cargo"),
                   ("Etihad Airways", "cargo_only"), ("flydubai", "cargo_only")],
    "Finland":    [("Finnair", "cabin_and_cargo"), ("SAS Scandinavian Airlines", "cabin_and_cargo"),
                   ("Lufthansa", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                   ("KLM", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Singapore Airlines", "cargo_only"),
                   ("Norwegian Air", "cabin_only"), ("Swiss International Air Lines", "cabin_and_cargo")],
    "Hungary":    [("Wizz Air", "cargo_only"), ("Ryanair", "cargo_only"),
                   ("Lufthansa", "cabin_and_cargo"), ("Austrian Airlines", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("LOT Polish Airlines", "cabin_and_cargo")],
    "Bulgaria":   [("Bulgaria Air", "cabin_and_cargo"), ("Wizz Air", "cargo_only"),
                   ("Ryanair", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Austrian Airlines", "cabin_and_cargo")],
    "Croatia":    [("Croatia Airlines", "cabin_and_cargo"), ("Ryanair", "cargo_only"),
                   ("easyJet", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Austrian Airlines", "cabin_and_cargo")],
    "Morocco":    [("Royal Air Maroc", "cargo_only"), ("Ryanair", "cargo_only"),
                   ("easyJet", "cargo_only"), ("Air France", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Iberia", "cabin_and_cargo"), ("KLM", "cabin_and_cargo")],
    "Pakistan":   [("Pakistan International Airlines", "cargo_only"), ("Emirates", "cargo_only"),
                   ("Qatar Airways", "cargo_only"), ("Etihad Airways", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                   ("Lufthansa", "cabin_and_cargo"), ("Air France", "cabin_and_cargo"),
                   ("Saudi Arabian Airlines (Saudia)", "cargo_only"), ("Air India", "cabin_and_cargo")],
    "Bangladesh": [("Biman Bangladesh Airlines", "cargo_only"), ("Emirates", "cargo_only"),
                   ("Qatar Airways", "cargo_only"), ("Etihad Airways", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("British Airways", "cargo_only"),
                   ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                   ("Air India", "cabin_and_cargo"), ("Malaysia Airlines", "cabin_and_cargo")],
    "Nepal":      [("Nepal Airlines", "cargo_only"), ("Air India", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("Etihad Airways", "cargo_only"),
                   ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                   ("British Airways", "cargo_only"), ("Lufthansa", "cabin_and_cargo")],
    "Cambodia":   [("Cambodia Angkor Air", "cargo_only"), ("Vietnam Airlines", "cargo_only"),
                   ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                   ("Thai Airways", "cargo_only"), ("Korean Air", "cabin_and_cargo"),
                   ("China Southern Airlines", "cargo_only"), ("Malaysia Airlines", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Lufthansa", "cabin_and_cargo")],
    "Myanmar":    [("Myanmar National Airlines", "cargo_only"), ("Thai Airways", "cargo_only"),
                   ("Singapore Airlines", "cargo_only"), ("Cathay Pacific", "cargo_only"),
                   ("China Southern Airlines", "cargo_only"), ("Malaysia Airlines", "cabin_and_cargo"),
                   ("Vietnam Airlines", "cargo_only"), ("Emirates", "cargo_only"),
                   ("British Airways", "cargo_only"), ("Korean Air", "cabin_and_cargo")],
    "Peru":       [("LATAM Airlines", "cabin_and_cargo"), ("Avianca", "cabin_and_cargo"),
                   ("Copa Airlines", "cabin_and_cargo"), ("American Airlines", "cabin_and_cargo"),
                   ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only"),
                   ("Air France", "cabin_and_cargo"), ("Iberia", "cabin_and_cargo"),
                   ("KLM", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo")],
    "Ecuador":    [("LATAM Airlines", "cabin_and_cargo"), ("Avianca", "cabin_and_cargo"),
                   ("Copa Airlines", "cabin_and_cargo"), ("American Airlines", "cabin_and_cargo"),
                   ("Delta Air Lines", "cabin_and_cargo"), ("United Airlines", "cabin_only"),
                   ("Air France", "cabin_and_cargo"), ("Iberia", "cabin_and_cargo"),
                   ("KLM", "cabin_and_cargo"), ("British Airways", "cargo_only")],
    "Costa_Rica": [("LATAM Airlines", "cabin_and_cargo"), ("Avianca", "cabin_and_cargo"),
                   ("Copa Airlines", "cabin_and_cargo"), ("American Airlines", "cabin_and_cargo"),
                   ("United Airlines", "cabin_only"), ("Delta Air Lines", "cabin_and_cargo"),
                   ("Air Canada", "cabin_and_cargo"), ("Iberia", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("Air France", "cabin_and_cargo")],
    "Ghana":      [("African Airlines", "cargo_only"), ("British Airways", "cargo_only"),
                   ("Virgin Atlantic", "cargo_only"), ("Emirates", "cargo_only"),
                   ("KLM", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Ethiopian Airlines", "cargo_only"), ("Air France", "cabin_and_cargo"),
                   ("Lufthansa", "cabin_and_cargo"), ("Delta Air Lines", "cabin_and_cargo")],
    "Tanzania":   [("Air Tanzania", "cargo_only"), ("British Airways", "cargo_only"),
                   ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"),
                   ("KLM", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Ethiopian Airlines", "cargo_only"), ("Kenya Airways", "cargo_only"),
                   ("Air France", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo")],
    "Ethiopia":   [("Ethiopian Airlines", "cargo_only"), ("British Airways", "cargo_only"),
                   ("Emirates", "cargo_only"), ("Qatar Airways", "cargo_only"),
                   ("Lufthansa", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo"),
                   ("Kenya Airways", "cargo_only"), ("Air France", "cabin_and_cargo"),
                   ("KLM", "cabin_and_cargo"), ("Etihad Airways", "cargo_only")],
    "Zimbabwe":   [("Air Zimbabwe", "cargo_only"), ("British Airways", "cargo_only"),
                   ("Emirates", "cargo_only"), ("Kenya Airways", "cargo_only"),
                   ("Ethiopian Airlines", "cargo_only"), ("South African Airways", "cargo_only"),
                   ("Turkish Airlines", "cabin_and_cargo"), ("Qatar Airways", "cargo_only"),
                   ("Fastjet", "cargo_only"), ("Air Botswana", "cargo_only")],
    "Mauritius":  [("Air Mauritius", "cargo_only"), ("British Airways", "cargo_only"),
                   ("Air France", "cabin_and_cargo"), ("Emirates", "cargo_only"),
                   ("Singapore Airlines", "cargo_only"), ("Condor", "cargo_only"),
                   ("Corsair", "cargo_only"), ("South African Airways", "cargo_only"),
                   ("Ethiopian Airlines", "cargo_only"), ("Lufthansa", "cabin_and_cargo")],
    "Slovakia":   [("Ryanair", "cargo_only"), ("Wizz Air", "cargo_only"),
                   ("Austrian Airlines", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Czech Airlines (CSA)", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Turkish Airlines", "cabin_and_cargo")],
    "Luxembourg": [("Luxair", "cabin_and_cargo"), ("Lufthansa", "cabin_and_cargo"),
                   ("British Airways", "cargo_only"), ("KLM", "cabin_and_cargo"),
                   ("Air France", "cabin_and_cargo"), ("Swiss International Air Lines", "cabin_and_cargo"),
                   ("Emirates", "cargo_only"), ("Brussels Airlines", "cabin_and_cargo"),
                   ("Iberia", "cabin_and_cargo"), ("Turkish Airlines", "cabin_and_cargo")],
}

# Export notes: (overview, cert_type, endorsement)
EXPORT_NOTES = {
    "Spain":      ("Spain uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by MAPA is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "MAPA endorsement required for non-EU/EFTA destinations"),
    "New_Zealand": ("No export permit required. An official health certificate from MPI is required for export. For Australia, a specific Biosecurity Australia-approved AHC format is required.",
                    "MPI-issued official health certificate. Australia requires MPI-approved specific format.", "MPI endorsement required"),
    "Oman":       ("No export permit required. An official health certificate from an MAFWR-registered veterinarian, endorsed by MAFWR, is required.",
                   "Official health certificate endorsed by MAFWR.", "MAFWR endorsement required"),
    "Bahrain":    ("No export permit required. Official health certificate from Animal Wealth Directorate-registered vet, endorsed by AWD.",
                   "Official health certificate endorsed by AWD.", "AWD endorsement required"),
    "Jordan":     ("No export permit required. Official health certificate endorsed by GDVS is required.",
                   "Official health certificate endorsed by GDVS.", "GDVS endorsement required"),
    "Finland":    ("Finland uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by Ruokavirasto is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "Ruokavirasto (Finnish Food Authority) endorsement required for non-EU/EFTA destinations"),
    "Hungary":    ("Hungary uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by NEBIH is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "NEBIH endorsement required for non-EU/EFTA destinations"),
    "Bulgaria":   ("Bulgaria uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by BFSA is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "BFSA endorsement required for non-EU/EFTA destinations"),
    "Croatia":    ("Croatia uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by HRVet is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "HRVet endorsement required for non-EU/EFTA destinations"),
    "Morocco":    ("No export permit required. Official health certificate endorsed by ONSSA is required.",
                   "Official health certificate endorsed by ONSSA.", "ONSSA endorsement required"),
    "Pakistan":   ("Export permit from Animal Quarantine Department (AQD) is required for all pet exports. Allow 2-3 weeks for permit processing.",
                   "Official health certificate endorsed by AQD.", "AQD export permit and endorsement required"),
    "Bangladesh": ("Export permit from Department of Livestock Services (DLS) required. Official health certificate endorsed by DLS.",
                   "Official health certificate endorsed by DLS.", "DLS export permit and endorsement required"),
    "Nepal":      ("Export permit from Department of Livestock Services (DoLS) required. Official health certificate endorsed by DoLS.",
                   "Official health certificate endorsed by DoLS.", "DoLS export permit and endorsement required"),
    "Cambodia":   ("Export permit from GDAHP required. Official health certificate endorsed by GDAHP.",
                   "Official health certificate endorsed by GDAHP.", "GDAHP export permit and endorsement required"),
    "Myanmar":    ("Export permit from DAH required. Official health certificate endorsed by DAH. Allow 3-4 weeks.",
                   "Official health certificate endorsed by DAH.", "DAH export permit and endorsement required"),
    "Peru":       ("No formal export permit required. Official health certificate from SENASA-accredited vet, endorsed by SENASA-PE.",
                   "Official health certificate endorsed by SENASA-PE.", "SENASA Peru endorsement required"),
    "Ecuador":    ("No formal export permit required. Official health certificate from AGROCALIDAD-accredited vet, endorsed by AGROCALIDAD.",
                   "Official health certificate endorsed by AGROCALIDAD.", "AGROCALIDAD endorsement required"),
    "Costa_Rica": ("No formal export permit required. Official health certificate from SENASA CR-accredited vet, endorsed by SENASA CR.",
                   "Official health certificate endorsed by SENASA CR.", "SENASA Costa Rica endorsement required"),
    "Ghana":      ("Export health certificate from VSD-registered vet, endorsed by VSD. No advance export permit required.",
                   "Official health certificate endorsed by VSD.", "VSD endorsement required"),
    "Tanzania":   ("Export health certificate from MLF-registered vet, endorsed by MLF. Export permit may be required for some destinations.",
                   "Official health certificate endorsed by MLF.", "MLF endorsement required"),
    "Ethiopia":   ("Export permit from APHRD required. Official health certificate endorsed by APHRD.",
                   "Official health certificate endorsed by APHRD.", "APHRD export permit and endorsement required"),
    "Zimbabwe":   ("Export permit from DLVS required. Official health certificate endorsed by DLVS.",
                   "Official health certificate endorsed by DLVS.", "DLVS export permit and endorsement required"),
    "Mauritius":  ("No formal export permit for cats and dogs. Official health certificate from VSD-registered vet, endorsed by VSD-MU.",
                   "Official health certificate endorsed by VSD-MU.", "VSD Mauritius endorsement required"),
    "Slovakia":   ("Slovakia uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by SVFA is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "SVFA endorsement required for non-EU/EFTA destinations"),
    "Luxembourg": ("Luxembourg uses the EU Pet Travel Scheme. EU Pet Passport for EU/EFTA travel. For non-EU destinations, an EU AHC endorsed by ASV is required.",
                   "EU AHC for non-EU travel. EU Pet Passport for EU/EFTA travel.", "ASV endorsement required for non-EU/EFTA destinations"),
}

# Country overview data (complexity, overview_text, [(heading, body), ...])
COUNTRY_OVERVIEWS = {
    "Spain": (
        "moderate",
        "Spain is one of the most pet-friendly countries in the EU and welcomes cats and dogs with correct EU-standard "
        "documentation. The Ministerio de Agricultura, Pesca y Alimentacion (MAPA) administers veterinary controls. "
        "Spain follows the EU Pet Travel Scheme and uses the EU Pet Passport system for intra-EU movements.\n\n"
        "For pets arriving from outside the EU -- including the UK post-Brexit -- an Animal Health Certificate (AHC) "
        "is required. Spain has one of Europe's highest dog ownership rates and a strong culture of pet-friendly "
        "travel. Airports at Madrid Barajas, Barcelona El Prat, and Malaga all handle regular pet imports.",
        [("EU and non-EU arrivals: what Spain requires",
          "For pets arriving from EU member states, an EU Pet Passport is the main travel document. No titre test "
          "is required for EU-originating pets with a valid rabies vaccination and continuous vaccination record.\n\n"
          "For UK pets (post-Brexit): an AHC issued by an Official Veterinarian and endorsed by APHA is required. "
          "If the pet has been continuously vaccinated and comes from GB, no titre test is required.\n\n"
          "For US, Australian, and other third-country pets: an AHC meeting the EU-approved format is required. "
          "If the origin country is not on the EU's listed third countries, a rabies titre test is mandatory with "
          "a 90-day wait after a successful result."),
         ("Spain's PPP breed restrictions",
          "Spain operates a PPP (Perros Potencialmente Peligrosos - Potentially Dangerous Dogs) system. Certain "
          "breeds are subject to restrictions: they must be registered, owner must hold PPP insurance, and the dog "
          "must be kept on a lead and muzzled in public spaces.\n\n"
          "The breed list includes American Pit Bull Terrier, Rottweiler, American Staffordshire Terrier, "
          "Staffordshire Bull Terrier, Dogo Argentino, Fila Brasileiro, Tosa Inu, and Akita Inu among others. "
          "These breeds are not banned outright but require the owner to comply with PPP rules from day of arrival. "
          "Some regional governments have additional restrictions.")]
    ),
    "New_Zealand": (
        "very high",
        "New Zealand is one of the world's strictest countries for pet imports. As a biosecurity-critical island nation, "
        "the Ministry for Primary Industries (MPI) administers an exceptionally thorough entry system. Every dog and "
        "cat entering New Zealand must undergo mandatory quarantine at the government facility in Levin.\n\n"
        "The process from first preparation to arrival typically takes at least 6-7 months because of the 180-day "
        "wait period after a successful rabies titre test. There are no shortcuts. Banned breeds are not permitted "
        "to enter under any circumstances. The Levin facility is the only approved quarantine station.",
        [("The New Zealand timeline: why you need 6+ months",
          "The 180-day waiting period is non-negotiable. After your pet's rabies titre test comes back above 0.5 IU/ml, "
          "the clock starts. Your pet cannot enter New Zealand until 180 days (6 calendar months) from the date the "
          "blood was drawn -- not from when you got the result.\n\n"
          "Before that, there are additional steps: the microchip must be in before any vaccination, the titre test "
          "blood must be drawn at least 30 days after the rabies vaccine, and you must apply for an import permit "
          "from MPI (Biosecurity New Zealand) before booking flights. The permit specifies all conditions.\n\n"
          "Levin quarantine must be pre-booked well in advance. Capacity is limited and popular dates fill up months "
          "out. Book the quarantine slot before you book your flights."),
         ("Arriving in New Zealand: quarantine and release",
          "All pets arriving in New Zealand go directly to the MPI Levin Quarantine Station in Manawatu. The minimum "
          "stay is 10 days. During quarantine, pets are monitored and examined. Owners cannot visit during the stay "
          "but receive regular updates. The cost is borne by the owner and typically runs NZD 2,000-4,000+ depending "
          "on species and stay length.\n\n"
          "Pets from countries deemed highest risk (Group 5 and 6 equivalent) have longer quarantine periods. "
          "On release, your pet will have passed MPI's compliance checks and be ready to come home.")]
    ),
    "Oman": (
        "moderate",
        "Oman is a Gulf Cooperation Council member with a significant expat population, particularly in Muscat. "
        "The Ministry of Agriculture, Fisheries and Water Resources (MAFWR) administers pet imports. Dogs and cats "
        "are accepted with appropriate documentation. Breed bans apply.\n\n"
        "The process requires advance planning: an import permit (No Objection Certificate) from MAFWR is required "
        "before travel. Processing typically takes 3-4 weeks. A title test may be required depending on origin country.",
        [("Getting the Oman import permit",
          "The import permit (often called a No Objection Certificate) must be obtained from MAFWR's General "
          "Directorate of Veterinary Services before your pet travels. Apply by email or through a registered "
          "Oman pet transport agent at least 4 weeks before travel.\n\n"
          "The permit application needs: your pet's microchip number, vaccination records, destination address "
          "in Oman, and owner identification. Once issued, the permit has a validity period -- check the dates "
          "match your travel itinerary before booking."),
         ("Breed restrictions in Oman",
          "Oman prohibits import of several breeds considered dangerous. The list includes American Pit Bull Terrier, "
          "Staffordshire Bull Terrier, American Staffordshire Terrier, Rottweiler, Dogo Argentino, Fila Brasileiro, "
          "Japanese Tosa, and wolf-hybrids. This list is subject to MAFWR updates.\n\n"
          "If your dog resembles a restricted breed, you may be asked to provide breed certification. Mixed-breed "
          "dogs that visually resemble banned breeds can face complications at the border. Contact MAFWR directly "
          "or use a registered agent if in doubt.")]
    ),
    "Bahrain": (
        "moderate",
        "Bahrain is a small GCC island nation with a large expat community, particularly in Manama. Pet imports "
        "are regulated by the Animal Wealth Directorate. The process is similar to other Gulf states: import permit, "
        "health certificate, and microchip are required. Bahrain handles most pet arrivals through Bahrain International Airport.",
        [("Bahrain import permit and documentation",
          "An import permit from the Animal Wealth Directorate must be obtained before travel. Apply online via the "
          "Bahrain eGovernment portal or through a registered local agent. The permit specifies the conditions for "
          "your pet's arrival.\n\n"
          "Documents required: microchip certificate, rabies vaccination record, health certificate from an official "
          "veterinarian (endorsed by your national veterinary authority), and the import permit. All documents should "
          "accompany the animal and be in English or Arabic."),
         ("What to expect at Bahrain airport",
          "Pets arriving at Bahrain International Airport are inspected by Animal Wealth Directorate officials. "
          "Compliant pets with correct documentation are released directly. Non-compliant pets may be placed in "
          "government quarantine at the owner's expense.\n\n"
          "Using an experienced Gulf pet transport agent reduces complications at the airport. They can coordinate "
          "with the airline, the AWD, and your arrival logistics to make sure everything runs smoothly.")]
    ),
    "Jordan": (
        "moderate",
        "Jordan is a Middle Eastern country with a growing expat community in Amman. Pet imports are regulated by "
        "the Ministry of Agriculture's General Directorate of Veterinary Services (GDVS). The process requires "
        "advance import approval, health certificate, and standard veterinary documentation.",
        [("Jordan pet import requirements",
          "An import approval from the GDVS must be obtained before travel. Apply at least 4 weeks in advance. "
          "Required documents: microchip certificate, rabies vaccination record, health certificate endorsed by "
          "the national veterinary authority in the origin country.\n\n"
          "Rabies titre test requirements depend on origin country. Pets from the UK, EU, US, and Australia may "
          "not require a titre test. Pets from endemic countries will require one. Verify with GDVS or a registered "
          "agent before making travel arrangements."),
         ("Travelling with pets to Jordan via Amman",
          "Queen Alia International Airport in Amman is the main entry point for pets. GDVS officials carry out "
          "veterinary inspections on arrival. Compliant pets are released. Keep all original documents -- copies "
          "are not accepted. If travelling by land from neighbouring countries, additional border crossing permits "
          "may be required.")]
    ),
    "Finland": (
        "low",
        "Finland is an EU member and one of the more straightforward destinations for pet arrivals within the EU "
        "framework. The Finnish Food Authority (Ruokavirasto) administers veterinary controls. Finland is rabies-free "
        "and follows EU Regulation 576/2013, transitioning to the new framework from April 2026.\n\n"
        "For pets from EU member states, an EU Pet Passport is all that is needed. For pets from the UK and other "
        "third countries, an Animal Health Certificate (AHC) is required. Finland also has specific tapeworm treatment "
        "requirements for dogs arriving from outside the EU.",
        [("UK and non-EU pets entering Finland",
          "UK pets require an AHC issued by an Official Veterinarian and endorsed by APHA. The AHC is valid for "
          "10 days from issue for entry into the EU. For US, Australian, and other third-country pets: AHC "
          "meeting the EU-approved format from the relevant national authority.\n\n"
          "If the origin country is not on the EU's listed third countries, a titre test is mandatory with a "
          "90-day waiting period after a successful result. Verify your origin country's status with Ruokavirasto."),
         ("Tapeworm treatment for dogs",
          "Dogs arriving in Finland from non-EU countries, or from EU countries with Echinococcus risk, must "
          "receive tapeworm treatment (praziquantel) within a 24-120 hour window before their scheduled arrival "
          "in Finland. The treatment must be administered by a veterinarian and recorded in the pet's documentation.\n\n"
          "The timing window is strict. Treatment outside the 24-120 hour window makes the pet non-compliant. "
          "Schedule the treatment carefully based on your exact arrival time.")]
    ),
    "Hungary": (
        "moderate",
        "Hungary is an EU member following EU pet travel regulations. The National Food Chain Safety Office (NEBIH) "
        "administers veterinary controls. Hungary has breed restrictions under national law. Budapest Liszt Ferenc "
        "International Airport is the main entry point.",
        [("Arriving in Hungary with a pet",
          "EU pets with a valid EU Pet Passport and current rabies vaccination can enter Hungary without further "
          "documentation. From UK (post-Brexit): AHC endorsed by APHA required. From US and other third countries: "
          "AHC in EU-approved format from the national authority.\n\n"
          "If the origin country is not on the EU listed countries list, a titre test with 90-day wait applies. "
          "Hungary's breed restrictions (see below) are checked on arrival."),
         ("Hungary's breed restrictions",
          "Hungary has national legislation restricting certain breeds. American Pit Bull Terrier and American "
          "Staffordshire Terrier face outright restrictions. Rottweiler, Bull Terrier, and Staffordshire Bull "
          "Terrier face special conditions including muzzle requirements in public, mandatory registration, "
          "and owner liability insurance.\n\n"
          "Verify the current status of your breed with NEBIH before travel. Regulations have been updated "
          "periodically and regional rules may apply in addition to national restrictions.")]
    ),
    "Bulgaria": (
        "moderate",
        "Bulgaria is an EU member but is not on the UK's Part 1 listed countries because wild rabies has been "
        "detected in wildlife. This means pets from Bulgaria travelling to the UK require a rabies titre test. "
        "The Bulgarian Food Safety Agency (BFSA) administers veterinary controls.",
        [("Bulgaria and the UK-specific rules",
          "Bulgaria is not on the UK's Part 1 or Part 2 listed countries. Pets from Bulgaria travelling to "
          "the UK require a titre test with a 90-day wait after a successful result. This is unusual for an "
          "EU member state and catches many pet owners by surprise.\n\n"
          "For other EU destinations, pets from Bulgaria with an EU Pet Passport and current rabies vaccination "
          "can travel freely within the EU. The titre test issue is specific to UK travel."),
         ("Importing a pet to Bulgaria",
          "Pets from EU member states can enter Bulgaria with an EU Pet Passport. From the UK and other third "
          "countries, an AHC in EU format is required. From non-listed third countries, a titre test with "
          "90-day wait applies.\n\n"
          "Bulgaria does not have routine quarantine for compliant pets. BFSA carries out veterinary inspections "
          "at the point of entry.")]
    ),
    "Croatia": (
        "low",
        "Croatia joined the EU in 2013 and follows EU pet travel regulations. The Ministry of Agriculture's "
        "Veterinary and Food Safety Directorate oversees imports. Croatia is rabies-free and has no breed ban. "
        "Zagreb International Airport and Split Airport are main entry points.",
        [("EU and non-EU arrivals",
          "EU pets with a valid EU Pet Passport can enter Croatia with no additional paperwork. UK pets require "
          "an AHC (post-Brexit). For US and other third-country pets: AHC in EU format from the national authority.\n\n"
          "Non-listed third country pets require a titre test with a 90-day wait. Croatia carries out veterinary "
          "inspections on arrival at designated border inspection posts."),
         ("Croatia: a note on pet-friendly travel",
          "Croatia has no breed ban and is generally considered a pet-friendly country. Many hotels, restaurants, "
          "and tourist attractions in Croatia accept pets, particularly in coastal areas during summer.\n\n"
          "For long-term stays, residents with pets from outside the EU should register with a local veterinarian "
          "shortly after arrival. A Croatian veterinary ID card (similar to an EU passport) may be issued for "
          "long-term resident pets.")]
    ),
    "Morocco": (
        "moderate",
        "Morocco is regulated by ONSSA (Office National de Securite Sanitaire des produits Alimentaires). Rabies "
        "is present in Morocco, which affects titre test requirements for pets leaving Morocco to rabies-free "
        "destinations. Import permit required for incoming pets.",
        [("Importing a pet to Morocco",
          "An import permit from ONSSA is required before travel. Apply at least 4 weeks in advance. Documents "
          "needed: microchip certificate, rabies vaccination record, health certificate from an official veterinarian "
          "endorsed by the national authority.\n\n"
          "Pets from EU member states and other European countries may not require a titre test to enter Morocco. "
          "Verify your specific origin country's requirements with ONSSA."),
         ("Exporting a pet from Morocco",
          "Pets leaving Morocco to rabies-free destinations (UK, Australia, New Zealand, etc.) will typically "
          "need a titre test because Morocco is not considered rabies-free. Blood must be drawn at least 30 days "
          "after the rabies vaccine, and a waiting period of 90 days (for UK) or 180 days (for Australia/NZ) "
          "applies after a successful result.\n\n"
          "The ONSSA-endorsed health certificate is required for all exports. Allow extra time for endorsement.")]
    ),
    "Pakistan": (
        "high",
        "Pakistan has a complex pet import and export process. The Animal Quarantine Department (AQD) administers "
        "controls. Importing pets to Pakistan requires a permit and quarantine. Exporting pets from Pakistan -- "
        "common for expats leaving -- requires an AQD export permit and endorsed health certificate.",
        [("Exporting your pet from Pakistan",
          "Most people using this guide are expats leaving Pakistan and taking their pets with them. The process "
          "requires an export permit from the Animal Quarantine Department. Apply at least 6 weeks before travel.\n\n"
          "You will need: AQD export permit, health certificate from a government-approved vet endorsed by AQD, "
          "microchip certificate, rabies vaccination record, and any destination country-specific requirements "
          "(titre test, import permit, etc.). Allow time for the destination country's paperwork as well."),
         ("Quarantine on arrival at most destinations",
          "Pets from Pakistan are typically treated as coming from a rabies-endemic country by strict destinations "
          "like the UK, Australia, and New Zealand. A titre test is almost always required for these routes.\n\n"
          "For the UK: titre test + 90-day wait. For Australia: titre test + 180-day wait (minimum). For New Zealand: "
          "titre test + 180-day wait. Start the titre test process as early as possible.")]
    ),
    "Bangladesh": (
        "high",
        "Bangladesh's pet export process is managed by the Department of Livestock Services (DLS). The large "
        "Bangladesh diaspora in the UK makes UK-Bangladesh the most active route. Export permit from DLS required. "
        "Pets from Bangladesh are treated as coming from a rabies-endemic country by most strict destinations.",
        [("Leaving Bangladesh with your pet",
          "Export permit from DLS is required. Apply well in advance. You will need a DLS-endorsed health certificate, "
          "microchip certificate, and rabies vaccination record. For the UK, Australia, and New Zealand, a titre "
          "test is required with the associated waiting period.\n\n"
          "Direct flights from Dhaka (Hazrat Shahjalal International Airport) serve the UK, UAE, Singapore, and "
          "Malaysia. Some routes require stopovers which add complexity."),
         ("Pet-friendly considerations in Bangladesh",
          "Pet culture in Bangladesh is growing but is not as established as in Western countries. International-grade "
          "veterinary clinics are available in Dhaka. When preparing for export, use a vet experienced with international "
          "export documentation -- the certificate format requirements are strict and errors cause rejection.")]
    ),
    "Nepal": (
        "high",
        "Nepal's pet export process is handled by the Department of Livestock Services (DoLS). Pets from Nepal "
        "are treated as coming from a rabies-endemic country. An export permit from DoLS is required. This route "
        "is primarily used by expats and NGO workers leaving Nepal.",
        [("Preparing for export from Nepal",
          "Allow at least 6 months if travelling to the UK, Australia, or New Zealand -- the titre test waiting "
          "periods are long and the destination country paperwork adds more time.\n\n"
          "Start with microchipping, then vaccination, then titre test (30 days after vaccination), then wait. "
          "Simultaneously apply for the destination country's import permit and the DoLS export permit. "
          "International-standard veterinary clinics in Kathmandu can assist with export documentation."),
         ("Transit considerations for Nepal routes",
          "Most flights from Kathmandu (Tribhuvan International Airport) require at least one stopover -- "
          "commonly through Delhi, Doha, Dubai, or Bangkok. Check whether transit countries have rules about "
          "pets in transit (some require a transit permit). Your pet transport agent can map out the best route.")]
    ),
    "Cambodia": (
        "high",
        "Cambodia is regulated by the General Directorate of Animal Health and Production (GDAHP). Pets from "
        "Cambodia are treated as coming from a rabies-endemic country. An export permit from GDAHP is required. "
        "The expat community in Phnom Penh and Siem Reap is active.",
        [("Export documentation from Cambodia",
          "GDAHP export permit and endorsed health certificate are both required. Most people apply through a "
          "registered Cambodian pet transport agent, as the process requires in-person steps at GDAHP offices.\n\n"
          "For the UK, Australia, and New Zealand: titre test + waiting period applies. For Singapore and "
          "other Southeast Asian destinations: requirements are simpler but still require a health certificate "
          "and often a destination country import permit."),
         ("Airlines from Phnom Penh and Siem Reap",
          "Direct routes from Cambodia are limited. Most pets travel via Bangkok (Suvarnabhumi), Singapore, "
          "Kuala Lumpur, or Hong Kong. Check that your transit airline and airport will handle pets in transit. "
          "Singapore Changi handles pet transits well. Bangkok can be more complex.")]
    ),
    "Myanmar": (
        "very high",
        "Myanmar has a complex pet export process managed by the Department of Animal Husbandry (DAH). An export "
        "permit is required and processing can take 3-4 weeks. Pets from Myanmar are treated as coming from a "
        "rabies-endemic country. Use an experienced Myanmar pet transport agent.",
        [("DAH export permit and process",
          "The DAH export permit requires: application form, microchip certificate, full vaccination records, "
          "health certificate from a DAH-registered veterinarian. Processing can take 3-4 weeks.\n\n"
          "For the UK, Australia, and New Zealand: titre test is required with associated waiting periods. "
          "This means starting the process 7-8 months before your planned travel date. For Singapore and "
          "Thailand: requirements are simpler but still require a health certificate and destination country "
          "permit."),
         ("Yangon international airport pet handling",
          "Yangon International Airport (RGN) handles pet cargo but capacity can be limited. Book cargo space "
          "with the airline well in advance. Confirm live animal acceptance with the airline directly -- "
          "some airlines have seasonal embargoes or route-specific restrictions for pets from Myanmar.")]
    ),
    "Peru": (
        "moderate",
        "Peru's SENASA (Servicio Nacional de Sanidad Agraria) administers pet imports and exports. Peru has a "
        "moderate complexity pet travel system. The main entry point is Lima's Jorge Chavez International Airport. "
        "Spain, USA, and UK are the most active corridors.",
        [("SENASA import permit and health certificate",
          "An import permit from SENASA Peru is required before travel. Apply via the SENASA online portal "
          "at least 4 weeks in advance. The health certificate from the origin country must be endorsed by "
          "the equivalent national authority and translated to Spanish if required.\n\n"
          "Rabies vaccination is required and must be current. Titre test requirements depend on origin country."),
         ("Lima airport pet arrival process",
          "Pets arrive at Jorge Chavez International Airport in Lima. SENASA officials inspect documentation "
          "on arrival. Compliant pets are released after a veterinary check. The process is generally "
          "straightforward if documentation is complete and correct.")]
    ),
    "Ecuador": (
        "moderate",
        "Ecuador's AGROCALIDAD administers pet imports and exports. The main entry airports are Quito's "
        "Mariscal Sucre International and Guayaquil's Jose Joaquin de Olmedo. AGROCALIDAD has an online "
        "import permit system.",
        [("AGROCALIDAD import permit",
          "Import permit from AGROCALIDAD is required. Apply online at least 4 weeks before travel. "
          "Health certificate from the origin country must be endorsed by the national authority. "
          "Certificate must list microchip number, vaccinations, and owner details.\n\n"
          "Ecuador does not routinely require a titre test from most countries. Verify with AGROCALIDAD "
          "for your specific origin."),
         ("Breed restrictions in Ecuador",
          "Ecuador and several municipalities (including Quito and Guayaquil) restrict or regulate certain breeds. "
          "American Pit Bull Terrier, Rottweiler, and Dogo Argentino face municipal restrictions. "
          "Owners must hold liability insurance and comply with local muzzle and lead laws. "
          "Verify current local rules before travel.")]
    ),
    "Costa_Rica": (
        "low",
        "Costa Rica is one of the more straightforward destinations in the Americas for pet import. SENASA "
        "Costa Rica has an online import permit system and no quarantine is required for compliant pets. "
        "San Jose's Juan Santamaria International Airport handles regular pet arrivals.",
        [("SENASA Costa Rica import permit",
          "An import permit (Permiso de Importacion) from SENASA Costa Rica is required. Apply online at "
          "the SENASA CR portal at least 2 weeks before travel. The permit has a validity period -- "
          "ensure your travel dates fall within it.\n\n"
          "Costa Rica does not routinely require a titre test. Rabies vaccination and health certificate "
          "from an endorsed national veterinary authority are the key requirements."),
         ("No quarantine, but a strict inspection",
          "Costa Rica does not quarantine compliant pets but carries out a thorough veterinary inspection "
          "on arrival at San Jose airport. All documentation must be present and correct. Original documents "
          "only -- copies are not accepted.\n\n"
          "Costa Rica's SENASA is known for being thorough. Owners who have prepared correctly find the "
          "process smooth. Those who arrive with incomplete documentation can face significant delays.")]
    ),
    "Ghana": (
        "high",
        "Ghana's Veterinary Services Directorate (VSD) administers pet imports. An import permit and quarantine "
        "are required. Ghana is treated as a rabies-endemic country so titre tests are required for pets leaving "
        "for strict destinations. Accra's Kotoka International Airport is the main entry and exit point.",
        [("Ghana import permit and quarantine",
          "An import permit from VSD is required at least 6 weeks before travel. Pets undergo quarantine on "
          "arrival (minimum 7 days). The government quarantine facility in Accra is used. Owner pays all costs.\n\n"
          "Documentation: VSD import permit, health certificate endorsed by national authority, microchip "
          "certificate, rabies vaccination record."),
         ("Exporting from Ghana: titre test requirements",
          "Pets from Ghana travelling to the UK, Australia, or New Zealand need a titre test because Ghana "
          "is not rabies-free. Blood drawn at least 30 days after vaccination; then 90-day wait for UK, "
          "180-day wait for Australia and New Zealand. The total preparation time is typically 7-8 months.\n\n"
          "VSD export permit and endorsed health certificate are required for export.")]
    ),
    "Tanzania": (
        "high",
        "Tanzania's Ministry of Livestock and Fisheries administers pet imports. A permit and quarantine are "
        "required. Tanzania is treated as rabies-endemic. The main entry/exit airports are Dar es Salaam's "
        "Julius Nyerere International and Kilimanjaro International.",
        [("Tanzania pet import requirements",
          "Import permit from MLF is required. Quarantine on arrival (minimum 10 days). "
          "Health certificate endorsed by national authority required, along with microchip and vaccination records.\n\n"
          "Tanzania does not have an online import permit system; applications go through the MLF office "
          "in Dar es Salaam or via a registered pet transport agent."),
         ("Exporting from Tanzania",
          "Pets from Tanzania leaving for strict destinations (UK, AU, NZ) require a titre test. Export permit "
          "from MLF and endorsed health certificate are required.\n\n"
          "For South Africa: a simpler health certificate-based process applies. For Kenya: health certificate "
          "and proof of vaccinations typically sufficient.")]
    ),
    "Ethiopia": (
        "high",
        "Ethiopia is regulated by the Ministry of Agriculture's Animal and Plant Health Regulatory Directorate "
        "(APHRD). Ethiopian Airlines operates one of Africa's largest hub networks from Addis Ababa Bole "
        "International Airport, making it a common connection point for pets travelling across Africa and "
        "beyond. Export permit required.",
        [("APHRD export and import permits",
          "Both an import permit (for incoming pets) and an export permit (for outgoing pets) are required "
          "from APHRD. Processing takes up to 8 weeks. Apply early.\n\n"
          "Pets in transit through Addis Ababa: Ethiopian Airlines handles transit pets but check their "
          "current live animal acceptance policies for transit routes."),
         ("Ethiopia as a transit hub",
          "Many international routes between Africa and Europe/Asia connect through Addis Ababa. If your pet "
          "is transiting through Ethiopia but not entering, Ethiopian Airlines' cargo team handles the transit "
          "arrangements. Transit does not require an Ethiopian import permit unless the pet is offloaded.")]
    ),
    "Zimbabwe": (
        "high",
        "Zimbabwe's Department of Livestock and Veterinary Services (DLVS) administers pet imports and exports. "
        "An import or export permit is required. Zimbabwe is treated as rabies-endemic. The UK-Zimbabwe corridor "
        "is the most active, driven by the large Zimbabwe diaspora in Britain.",
        [("DLVS permit requirements",
          "Import permit from DLVS is required at least 6 weeks before travel. Export permit from DLVS "
          "required for pets leaving Zimbabwe.\n\n"
          "Documentation: DLVS permit, health certificate from a government-endorsed vet endorsed by DLVS, "
          "microchip certificate, rabies vaccination records."),
         ("Zimbabwe to UK: titre test timeline",
          "Pets from Zimbabwe travelling to the UK require a titre test because Zimbabwe is not on the "
          "UK's listed countries. Blood drawn 30+ days after vaccination; 90-day wait after successful "
          "result. Total preparation: 5-6 months minimum from microchip to departure.\n\n"
          "International flights from Harare (Robert Gabriel Mugabe International Airport) serve "
          "the UK, UAE, and South Africa. Book cargo space well in advance.")]
    ),
    "Mauritius": (
        "very high",
        "Mauritius has some of the world's strictest pet import controls. The island is rabies-free and "
        "intends to stay that way. The Veterinary Services Division administers a system comparable to "
        "Australia's in its strictness: mandatory quarantine, approved country groups, 180-day wait. "
        "Import permits are issued in very limited numbers.",
        [("Why Mauritius is so strict",
          "Mauritius is a small island nation that has never had a recorded case of rabies. The government "
          "takes extraordinary measures to keep it that way. Every cat and dog entering Mauritius, regardless "
          "of origin, must complete 30 days quarantine at the government facility.\n\n"
          "A 180-day residency requirement applies: your pet must have lived in an approved, rabies-free "
          "country for 6 months before the travel date (after a successful titre test). This is in addition "
          "to the 180-day wait after the titre test."),
         ("Getting a Mauritius import permit",
          "The Veterinary Services Division issues a limited number of import permits. Apply at least "
          "3-4 months before your intended travel date. Permits are not guaranteed.\n\n"
          "The permit specifies exactly which country your pet must be in during the 6-month pre-travel "
          "period, which approved quarantine station will be used, and which flight routing is accepted. "
          "Do not book travel until the permit is confirmed.")]
    ),
    "Slovakia": (
        "low",
        "Slovakia is an EU member following EU pet travel regulations. The State Veterinary and Food "
        "Administration (SVFA) oversees veterinary controls. Bratislava is the main entry point. "
        "Slovakia has no national breed ban.",
        [("EU and non-EU arrivals to Slovakia",
          "EU pets with EU Pet Passport enter freely. UK pets need an AHC endorsed by APHA. "
          "Other third-country pets need an AHC in EU format from the national authority.\n\n"
          "Non-listed third country pets require a titre test with 90-day wait. "
          "No quarantine for compliant pets. SVFA inspection at border."),
         ("Transit through Slovakia",
          "Slovakia shares borders with Austria, Czech Republic, Poland, Hungary, and Ukraine. "
          "Transit through Slovakia is straightforward for EU-documented pets. "
          "Non-EU pets in transit should ensure their documents cover all countries on the route.")]
    ),
    "Luxembourg": (
        "low",
        "Luxembourg is a small EU member with the highest per-capita expat population in the EU -- "
        "driven by EU institutions, NATO, and financial services. The Administration des services "
        "veterinaires (ASV) administers veterinary controls. Luxembourg follows EU Regulation 576/2013.",
        [("Luxembourg for expat pet owners",
          "The high expat population means Luxembourg handles a disproportionate number of "
          "international pet movements relative to its size. The process is standard EU: "
          "EU Pet Passport for EU pets, AHC for UK/third-country pets.\n\n"
          "From the UK: AHC endorsed by APHA required. Continuous vaccination record means "
          "no titre test required if pet has always been vaccinated."),
         ("Breed restrictions in Luxembourg",
          "Luxembourg restricts import of unregistered American Staffordshire Terriers and "
          "American Pit Bull Terriers. Registered Staffordshire breeds may be kept under "
          "strict conditions. Verify current status with ASV before travel with a restricted breed.")]
    ),
}


def slugify(name: str) -> str:
    """Convert country name to URL slug."""
    return re.sub(r"[^a-z0-9-]", "", name.lower().replace(" ", "-").replace("_", "-"))


def get_outbound_routes(country_key: str, country_slug: str) -> list[str]:
    """Scan routes/ directory for all outbound routes from this country."""
    routes = []
    prefix = country_slug + "-to-"
    if os.path.exists(ROUTES_DIR):
        for fname in sorted(os.listdir(ROUTES_DIR)):
            if fname.startswith(prefix) and fname.endswith(".md"):
                dest_slug = fname[len(prefix):-3]
                dest_name = dest_slug.replace("-", " ").title()
                route_slug = fname[:-3]
                routes.append((dest_name, dest_slug, route_slug))
    return routes


def build_origin_hub(country_key: str) -> str:
    """Build origin hub markdown for a P4 country."""
    name, iso, slug, auth_name, auth_abbrev = P4_COUNTRY_REGISTRY[country_key]
    data = countries_raw.get(country_key, {})
    imp = data.get("import_requirements", {})
    exp = data.get("export_requirements", {})

    export_overview, cert_type, endorsement = EXPORT_NOTES.get(
        country_key,
        (f"No formal export permit required for household pets from {name}. An official health certificate endorsed by {auth_abbrev} is required.",
         f"Official health certificate endorsed by {auth_abbrev}.",
         f"{auth_abbrev} endorsement required")
    )

    airlines = AIRLINES_BY_COUNTRY.get(country_key, [])
    airline_lines = "\n".join(
        f'    - name: "{a[0]}"\n      type: "{a[1]}"' for a in airlines
    )

    outbound_routes = get_outbound_routes(country_key, slug)
    routes_yaml = "\n".join(
        f'    - url: "/pet-transport/{r[2]}/"\n      text: "Pet Transport from {name} to {r[0]}"'
        for r in outbound_routes[:30]
    )

    microchip = imp.get("microchip", {})
    rabies_vax = imp.get("rabies_vaccination", {})
    titre = imp.get("rabies_titre_test", {})
    quarantine = imp.get("quarantine", {})
    permit = imp.get("import_permit", {})
    health_cert = imp.get("health_certificate", {})
    banned = imp.get("banned_breeds", {})
    banned_list = banned.get("banned", [])

    quarantine_text = (
        f"Mandatory quarantine at {quarantine.get('facility', 'government facility')} "
        f"({quarantine.get('duration_days', 'duration varies')})"
        if quarantine.get("required")
        else "No routine quarantine for compliant pets. Veterinary inspection on arrival."
    )

    titre_req = titre.get("required_for", "Check with authority")
    titre_wait = titre.get("wait_after_test_days", "")
    titre_text = f"Required for: {titre_req}. Minimum: {titre.get('minimum_result', '0.5 IU/ml')}."
    if titre_wait:
        titre_text += f" {titre_wait}-day wait after successful result."

    permit_text = (
        f"Required (apply {permit.get('apply_in_advance_weeks', 4)} weeks in advance from {permit.get('issued_by', auth_name)})"
        if permit.get("required")
        else "Not required for most commercial pets. EU pet passport or AHC serves as travel document."
    )

    banned_text = (
        "None" if not banned_list
        else ", ".join(banned_list[:5]) + (" and others" if len(banned_list) > 5 else "")
    )

    airline_section = ""
    if airlines:
        airline_section = "\n\n## Airlines commonly used from " + name + "\n\n" + "\n".join(
            f"- **{a[0]}** — {'cabin and cargo' if a[1] == 'cabin_and_cargo' else 'cargo only' if a[1] == 'cargo_only' else 'cabin only'}"
            for a in airlines[:6]
        )

    routes_section = ""
    if outbound_routes:
        routes_section = "\n\n## Popular routes from " + name + "\n\n" + "\n".join(
            f"- [{name} to {r[0]}](/pet-transport/{r[2]}/)" for r in outbound_routes[:20]
        )

    # Build hub title variants
    title_variants = [
        f"Pet Transport from {name} | Export Requirements & Routes",
        f"Shipping Pets from {name} Internationally | PetTransportGlobal",
        f"{name} Pet Export Guide | International Pet Transport",
    ]
    title = title_variants[hash(name) % 3]
    desc_base = f"How to ship your dog or cat from {name} internationally. Export requirements, health certificates, and {auth_abbrev} endorsement explained."
    desc = desc_base[:160]

    h1 = f"Pet Transport from {name}: Export Guide"

    overview_para = (
        f"Moving abroad from {name} with a dog or cat means preparing the correct export documentation "
        f"before you leave. The rules depend on where you are heading -- but the starting point is always "
        f"the same: get your pet microchipped (if not already), vaccinate against rabies, and obtain an "
        f"official health certificate endorsed by {auth_abbrev}.\n\n"
        f"This guide covers what {name} requires before your pet leaves, the most common destination "
        f"requirements for {name} pets, and which airlines serve the main corridors."
    )

    return f"""---
title: "{title}"
description: "{desc}"
type: "origins"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}-pet-export-guide"
origin_country: "{name}"
origin_iso: "{iso}"
authority: "{auth_name}"
authority_abbrev: "{auth_abbrev}"
export_requirements:
  export_permit: "{exp.get('export_permit', {}).get('required', False)}"
  health_certificate: "{cert_type}"
  endorsement: "{endorsement}"
microchip: "ISO 11784/11785 required. Must be implanted before any rabies vaccination."
rabies_vaccination: "Required. Valid at time of travel."
titre_test: "{titre_text}"
quarantine_at_destination: "Varies by destination. Check destination country guide."
airlines:
{airline_lines}
popular_routes:
{routes_yaml}
faqs:
  - question: "What documents does my pet need to leave {name}?"
    answer: "Your pet needs a valid microchip (ISO standard), current rabies vaccination, and an official health certificate endorsed by {auth_abbrev}. Specific destination countries may require additional documents such as a titre test result, import permit, or specific certificate formats."
  - question: "Is an export permit required from {name}?"
    answer: "{export_overview}"
  - question: "Which airline should I use to fly my pet from {name}?"
    answer: "The best airline depends on your destination. {airlines[0][0] if airlines else 'Major carriers'} {'operates cabin and cargo pet services' if airlines and airlines[0][1] == 'cabin_and_cargo' else 'operates cargo-only pet services'} from {name}. Always confirm live animal acceptance with the airline before booking."
  - question: "Are any dog breeds banned or restricted when leaving {name}?"
    answer: "{'Your destination country may restrict certain breeds regardless of your origin. Commonly restricted breeds include ' + banned_text + '. Always check destination country rules for your specific breed.' if banned_list else 'No export breed ban applies in ' + name + '. However, your destination country may restrict certain breeds. Always check destination country rules.'}"
  - question: "How far in advance should I start preparing my pet for international transport from {name}?"
    answer: "Start at least 3 months before travel for most destinations. For Australia, New Zealand, or Mauritius, start 7-8 months ahead because of mandatory titre test waiting periods (180 days) and limited quarantine facility availability."
seo:
  canonical: "https://pettransportglobal.com/pet-transport/origins/{slug}-pet-export-guide/"
  og_title: "{h1}"
  og_description: "{desc}"
---

# {h1}

{overview_para}

## Export requirements for {name}

Before your pet can leave {name}, the following must be in place:

- **Microchip:** ISO 11784/11785 standard. Must be implanted before or on the same day as the first rabies vaccination.
- **Rabies vaccination:** Required and must be valid at the time of travel. Allow the full post-vaccination wait before international travel.
- **Titre test (if required):** {titre_text}
- **Health certificate:** {cert_type} {endorsement}.
- **Quarantine at destination:** {quarantine_text}
- **Import permit (destination):** {permit_text}
- **Banned breeds at destination:** {banned_text} (varies by destination country -- always verify).
{airline_section}
{routes_section}

## Quick checklist: leaving {name} with your pet

1. Microchip (ISO standard) -- must be in before any rabies vaccination
2. Rabies vaccination -- must be current at travel date
3. Titre test (if destination requires it) -- blood drawn 30+ days after vaccination
4. Wait period after titre test (90 or 180 days depending on destination)
5. Apply for destination country import permit
6. Book IATA-compliant crate and cargo/cabin space with airline
7. Obtain official health certificate from {auth_abbrev}-endorsed veterinarian
8. Travel day -- arrive at airport 3-4 hours early for cargo pets
"""


def build_country_guide(country_key: str) -> str:
    """Build country guide markdown for a P4 destination country."""
    name, iso, slug, auth_name, auth_abbrev = P4_COUNTRY_REGISTRY[country_key]
    data = countries_raw.get(country_key, {})
    imp = data.get("import_requirements", {})

    microchip = imp.get("microchip", {})
    rabies_vax = imp.get("rabies_vaccination", {})
    titre = imp.get("rabies_titre_test", {})
    quarantine = imp.get("quarantine", {})
    permit = imp.get("import_permit", {})
    health_cert = imp.get("health_certificate", {})
    banned = imp.get("banned_breeds", {})
    banned_list = banned.get("banned", [])
    rabies_status = data.get("rabies_status", "check authority")

    complexity, overview_text, sections = COUNTRY_OVERVIEWS.get(
        country_key,
        ("moderate", f"{name} requires an official health certificate and standard vaccinations for all imported pets.", [])
    )

    quarantine_text = (
        f"Mandatory quarantine at {quarantine.get('facility', 'government facility')} "
        f"({quarantine.get('duration_days', 'duration varies')})"
        if quarantine.get("required")
        else "No routine quarantine for compliant pets."
    )

    titre_req = titre.get("required_for", "Check with authority")
    titre_wait = titre.get("wait_after_test_days", "")
    titre_text = f"Required for: {titre_req}. Minimum: {titre.get('minimum_result', '0.5 IU/ml')}."
    if titre_wait:
        titre_text += f" {titre_wait}-day wait after successful result."

    banned_text = (
        "None confirmed" if not banned_list
        else ", ".join(banned_list[:5]) + (" and others" if len(banned_list) > 5 else "")
    )

    sections_md = "\n\n".join(
        f"## {h}\n\n{b}" for h, b in sections
    )

    # Inbound routes from major P1 origins
    p1_origins = [
        ("UK", "united-kingdom"), ("USA", "united-states"), ("UAE", "united-arab-emirates"),
        ("Australia", "australia"), ("Canada", "canada"), ("Germany", "germany"),
        ("France", "france"), ("Singapore", "singapore"),
    ]
    inbound_links = []
    for orig_name, orig_slug in p1_origins:
        route_file = os.path.join(ROUTES_DIR, f"{orig_slug}-to-{slug}.md")
        if os.path.exists(route_file):
            inbound_links.append(
                f'    - url: "/pet-transport/{orig_slug}-to-{slug}/"\n      text: "Pet Transport {orig_name} to {name}"'
            )
    routes_yaml = "\n".join(inbound_links)

    title_variants = [
        f"Importing Pets to {name} | Requirements & Regulations | PetTransportGlobal",
        f"Pet Import Rules for {name} | Microchip, Vaccines, Quarantine Explained",
        f"Moving Pets to {name} | {auth_abbrev} Import Requirements",
    ]
    title = title_variants[hash(name) % 3]
    desc_base = f"Complete guide to importing dogs and cats into {name}. {auth_abbrev} import requirements, quarantine rules, and banned breeds explained."
    desc = desc_base[:160]

    h1 = f"Importing Pets to {name}: Complete Guide"

    return f"""---
title: "{title}"
description: "{desc}"
type: "countries"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
destination_country: "{name}"
destination_iso: "{iso}"
authority: "{auth_name}"
authority_abbrev: "{auth_abbrev}"
rabies_status: "{rabies_status}"
import_requirements:
  microchip: "ISO 11784/11785 required"
  rabies_vaccination: "Required"
  titre_test: "{titre_text}"
  quarantine: "{quarantine_text}"
  import_permit: "{'Required -- apply in advance from ' + auth_abbrev if permit.get('required') else 'Not required for most pets'}"
  health_certificate: "Official government veterinary certificate required"
  banned_breeds: "{banned_text}"
incoming_routes:
{routes_yaml}
faqs:
  - question: "What vaccinations does my pet need to enter {name}?"
    answer: "Rabies vaccination is required. Your pet must be microchipped (ISO standard) and have a current, valid rabies vaccination. Additional vaccinations may be recommended but are not required for import. The health certificate must list all vaccinations."
  - question: "Is quarantine required when entering {name}?"
    answer: "{quarantine_text} Ensure all documentation is complete before travel to avoid penalty quarantine."
  - question: "Does my pet need a titre test to enter {name}?"
    answer: "{titre_text}"
  - question: "Are any dog breeds banned in {name}?"
    answer: "{'Banned breeds include: ' + banned_text + '. ' + banned.get('notes', '') if banned_list else 'No specific national breed ban confirmed for ' + name + '. Check local and municipal regulations as additional restrictions may apply.'}"
  - question: "How long before travel should I start preparing my pet for {name}?"
    answer: "Start at least 3 months before travel for most origins. If a titre test is required, start 6-8 months ahead to allow for the post-vaccination wait (30 days), test processing, and the waiting period (90-180 days depending on the route)."
seo:
  canonical: "https://pettransportglobal.com/pet-transport/countries/{slug}/"
  og_title: "{h1}"
  og_description: "{desc}"
---

# {h1}

{overview_text}

## Key requirements for pet import to {name}

| Requirement | Detail |
|-------------|--------|
| Microchip | ISO 11784/11785 required |
| Rabies vaccination | Required |
| Titre test | {titre_text} |
| Quarantine | {quarantine_text} |
| Import permit | {'Required -- apply in advance' if permit.get('required') else 'Not required'} |
| Banned breeds | {banned_text} |
| Authority | {auth_name} ({auth_abbrev}) |

{sections_md}

## Sources and regulatory authority

Requirements are sourced from {auth_name} ({auth_abbrev}) official guidance. Regulations can change. Always verify current requirements directly with {auth_abbrev} or your pet transport agent before finalising travel arrangements.
"""


def main():
    os.makedirs(ORIGINS_DIR, exist_ok=True)
    os.makedirs(COUNTRIES_DIR, exist_ok=True)

    origins_written = 0
    origins_skipped = 0
    countries_written = 0
    countries_skipped = 0

    for country_key in P4_KEYS:
        name, iso, slug, auth_name, auth_abbrev = P4_COUNTRY_REGISTRY[country_key]

        # Origin hub
        origin_path = os.path.join(ORIGINS_DIR, f"{slug}-pet-export-guide.md")
        if os.path.exists(origin_path):
            print(f"  SKIP origin: {origin_path}")
            origins_skipped += 1
        else:
            content = build_origin_hub(country_key)
            with open(origin_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  WRITE origin: {slug}-pet-export-guide.md")
            origins_written += 1

        # Country guide
        country_path = os.path.join(COUNTRIES_DIR, f"{slug}.md")
        if os.path.exists(country_path):
            print(f"  SKIP country: {country_path}")
            countries_skipped += 1
        else:
            content = build_country_guide(country_key)
            with open(country_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  WRITE country: {slug}.md")
            countries_written += 1

    print(f"\nDone.")
    print(f"  Origins: {origins_written} written, {origins_skipped} skipped")
    print(f"  Countries: {countries_written} written, {countries_skipped} skipped")


if __name__ == "__main__":
    main()
