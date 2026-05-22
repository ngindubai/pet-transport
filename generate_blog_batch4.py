"""
generate_blog_batch4.py
Task 4.7 Batch A — Blog articles 51-75.
25 new articles covering P4 destination guides, breed travel topics,
regulation deep-dives, and practical planning content.
"""

import os

BLOG_DIR = os.path.join("site", "content", "blog")

ARTICLES = [
    {
        "slug": "spain-pet-import-guide",
        "title": "Moving Pets to Spain: EU Rules, Health Certificates, and What Brexit Changed",
        "description": "How to move a dog or cat to Spain from the UK or USA. EU pet passport rules, Animal Health Certificates, microchip requirements, and rabies vaccination timelines explained.",
        "date": "2026-05-10",
        "tags": ["spain", "europe", "planning"],
        "faqs": [
            ("Can I still use an EU pet passport to take my pet to Spain from the UK?",
             "No. Since Brexit, UK-issued EU pet passports are no longer valid for travel from the UK to EU member states including Spain. You need an Animal Health Certificate (AHC) issued by an Official Veterinarian (OV) within 10 days of travel each time you travel."),
            ("Does my pet need a titre test to enter Spain from the UK?",
             "No. Spain, as an EU member state, does not require a rabies antibody titre test for pets entering from the UK, provided the pet has a valid current rabies vaccination and a correctly completed AHC. Titre tests are required for travel to countries like Australia, New Zealand, and Japan."),
            ("Can I bring more than 5 pets into Spain?",
             "Bringing more than 5 pets into Spain requires a commercial health certificate rather than a standard pet AHC. If you have more than 5 animals, contact Spain's MAPA (Ministerio de Agricultura, Pesca y Alimentación) for the commercial import process."),
        ],
        "body": """Spain is one of the most popular destinations for UK expatriates and retirees relocating with pets. The good news: Spain's EU membership means the import rules are well-established and manageable. The less good news: Brexit changed things for UK pet owners in ways that still catch people out.

## What Changed After Brexit

Before Brexit, UK pets travelled to Spain on EU pet passports — a single booklet that stayed valid for the animal's lifetime with updated vaccination records. Since 1 January 2021, that system no longer applies for UK-to-EU travel.

**What you need now:** An Animal Health Certificate (AHC) issued by a UK Official Veterinarian (OV). The AHC must be issued **within 10 days of travel** and is valid for that journey only. You need a new one for each trip.

If you're moving permanently, you only need it once. If you're planning regular trips between the UK and Spain, the 10-day window means repeat vet visits.

## Core Documentation for UK to Spain

| Document | Requirement |
|----------|-------------|
| Microchip | ISO 15-digit, implanted before or at first rabies vaccination |
| Rabies vaccination | Current (within validity period), administered after microchip |
| Animal Health Certificate | Issued by OV within 10 days of travel |
| EU pet passport | Not required (not valid for UK-origin travel) |

## What Spain Requires at Entry

Spain applies EU Regulation 576/2013 for non-commercial pet movements. Border inspection posts (BIPs) at major Spanish entry points (Madrid Barajas, Barcelona El Prat, Malaga, Bilbao) carry out documentary and identity checks. Physical inspections are conducted on a risk basis.

The main BIP for air arrivals is Barajas (Madrid) and El Prat (Barcelona). Declare your pet at the border health post on arrival.

## Breed Restrictions in Spain

Spain has breed-specific legislation through Royal Decree 1440/2021. Breeds classified as potentially dangerous (PPP — Perros Potencialmente Peligrosos) require:
- Owner licence
- Third-party liability insurance (minimum €120,000 coverage)
- Muzzle in public
- Lead of no more than 2 metres

Affected breeds include: Pit Bull Terrier, Staffordshire Bull Terrier, American Staffordshire Terrier, Rottweiler, Dogo Argentino, Fila Brasileiro, Tosa Inu, Akita Inu, and dogs above a size/weight threshold regardless of breed.

This does not prevent import but affects conditions of keeping.

## Flying Pets to Spain

Most major carriers operate routes to Spanish airports. BA, Iberia, Ryanair (cargo only for pets), Vueling, and Lufthansa Group airlines all serve Spain. In-cabin pets are accepted by Iberia and Vueling for small animals meeting weight limits. British Airways does not accept in-cabin pets.

## Cost Estimate (UK to Spain)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | £150-250 |
| Airline cargo or cabin fee | £50-400 |
| **Total** | **~£200-650** |

---

*Sources: European Commission Pet Travel rules (Regulation 576/2013); UK Government official pet travel guidance (APHA); Spain MAPA official guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "finland-pet-import-guide",
        "title": "Moving Pets to Finland: EU Entry Rules, Echinococcus Treatment, and Winter Travel",
        "description": "Finland's pet import rules for dogs and cats from the UK and outside the EU. Echinococcus tapeworm treatment requirement, health certificates, and cold-weather cargo tips.",
        "date": "2026-05-10",
        "tags": ["finland", "europe", "nordic", "planning"],
        "faqs": [
            ("Does Finland require tapeworm treatment for dogs?",
             "Yes. Finland is one of a small group of EU countries (along with the UK, Ireland, Malta, and Norway) that requires dogs to be treated against Echinococcus multilocularis tapeworm before entry. Treatment must be given by a vet 1-5 days before entering Finland and documented in the health certificate."),
            ("Can I bring my cat to Finland from the UK without a titre test?",
             "Yes. Finland, as an EU member state, does not require a rabies titre test for cats or dogs arriving with valid rabies vaccinations and correct documentation. A titre test is only required for pets entering countries like Australia, New Zealand, or Japan."),
            ("What is the entry point for pets flying into Finland?",
             "Helsinki-Vantaa Airport (HEL) is the primary entry point for pets arriving in Finland by air. Declare your pet at the border inspection post on arrival."),
        ],
        "body": """Finland is a Nordic EU member state with one specific requirement that sets it apart from most EU entry points: **Echinococcus tapeworm treatment** for dogs.

## The Echinococcus Treatment Requirement

Finland, like the UK, Ireland, Malta, and Norway, has maintained a derogation from standard EU pet movement rules requiring dogs to be treated against *Echinococcus multilocularis* — a tapeworm whose intermediate hosts include rodents common in northern and central Europe.

**What you need:**
- A licensed vet administers praziquantel (or equivalent) treatment
- Treatment given **1-5 days before the dog enters Finland**
- The treating vet records it in the health certificate

This applies to dogs entering from any country, including other EU member states. Cats are exempt.

## Documentation for UK to Finland

| Document | Required |
|----------|---------|
| ISO 15-digit microchip | Yes |
| Current rabies vaccination | Yes |
| Animal Health Certificate (AHC) | Yes — issued by OV within 10 days of travel |
| Echinococcus treatment record | Yes — for dogs only |

## Flying Into Finland

Helsinki-Vantaa Airport (HEL) handles most international pet arrivals. Finnish border vets conduct documentary and physical checks at the BIP. Pre-notification is advisable for cargo shipments.

Main carriers serving Helsinki from the UK: Finnair, British Airways, Ryanair. Finnair accepts pets in cabin and cargo. BA requires cargo for all dogs.

## Cold Weather and Nordic Cargo

Finland is cold, particularly in winter. The cargo hold is temperature-controlled, but ground handling time in -20°C conditions matters for short-coated or small breeds. Schedule flights through Helsinki in winter to minimise ground exposure time. Larger, cold-adapted breeds (Huskies, Samoyeds, Malamutes) handle Finnish winter conditions better than short-coated dogs.

## Breed Restrictions

Finland does not have a list of nationally banned breeds. Finnish legislation focuses on individual dog behaviour rather than breed type.

## Cost Estimate (UK to Finland)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | £150-250 |
| Tapeworm treatment | £30-60 |
| Airline cargo or cabin fee | £80-500 |
| **Total** | **~£260-810** |

---

*Sources: EU Regulation 576/2013; Finnish Food Authority (Ruokavirasto) official pet import guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "oman-pet-import-guide",
        "title": "Moving Pets to Oman: Import Permits, Breed Restrictions, and the 6-Month Residency Rule",
        "description": "Oman pet import rules for dogs and cats. The Ministry of Agriculture permit process, breed bans, vaccination requirements, and what the 6-month residency rule means for expats.",
        "date": "2026-05-12",
        "tags": ["oman", "middle-east", "planning"],
        "faqs": [
            ("Does Oman ban any dog breeds?",
             "Yes. Oman bans the import of several breeds including Pit Bull Terriers, Rottweilers, Dobermanns (in some circumstances), and other breeds classified as dangerous. Check the current MARA (Ministry of Agriculture, Fisheries and Water Resources) breed list before booking, as it is updated periodically."),
            ("Do I need a government permit to bring a dog into Oman?",
             "Yes. An import permit from Oman's Ministry of Agriculture, Fisheries and Water Resources (MARA) is required before the animal travels. Apply at least 4 weeks before your planned travel date."),
            ("Is there quarantine in Oman?",
             "There is no mandatory quarantine for pets arriving in Oman with complete documentation. However, MARA vets inspect all arriving animals and can order quarantine if documentation is incomplete or the animal appears unwell."),
        ],
        "body": """Oman is home to a substantial expat community and welcomes pets with the right documentation. The process is more involved than EU entry but manageable with advance planning.

## Import Permit Requirement

Before your pet travels to Oman, you need an **import permit from MARA** (Ministry of Agriculture, Fisheries and Water Resources). Apply through the MARA portal or via a licensed Omani agent. Allow at least 4 weeks for processing.

The permit specifies:
- Animal species and breed
- Country of origin
- Owner details (must match residency documentation)

## Core Documentation

| Document | Requirement |
|----------|-------------|
| Import permit | Obtained from MARA before travel |
| Microchip | ISO 15-digit |
| Rabies vaccination | Current, administered at least 30 days before travel |
| Health certificate | Issued by government vet authority in country of origin within 7 days of travel |
| Rabies-free country certification | If applicable to your origin country |

## Breed Restrictions

Oman maintains a list of banned dog breeds. The current list includes Pit Bull Terriers and related types, Rottweilers, and several other breeds classified as dangerous. Dobermanns may face restrictions depending on current regulations. **Check the current MARA breed list directly before booking** — it is subject to change.

## The Residency Connection

Oman's pet import rules are linked to the owner's residency status. Pets are imported as personal effects of a resident, not as standalone imports. You must be able to demonstrate Omani residency (employment visa, residence permit) to import a pet. Tourist-only entry does not permit pet import.

## Entry Points

Muscat International Airport (MCT) is the primary entry point. Animals are inspected by MARA vets on arrival. Cargo shipments require advance notification to the airport veterinary authority.

## Climate Consideration

Oman is hot. Summer temperatures in Muscat regularly exceed 40°C. Most airlines will not transport live animals as cargo when ground temperatures are above 29°C. This effectively rules out summer cargo for most breeds. Plan travel for the October to March window.

## Cost Estimate (UK to Oman)

| Item | Estimated Cost |
|------|----------------|
| MARA import permit | OMR 10-30 (~£20-60) |
| Government health certificate + endorsement | £200-350 |
| Airline cargo | £400-900 |
| **Total** | **~£620-1,310** |

---

*Sources: Oman MARA official pet import guidance; IATA Live Animals Regulations. Data current as of May 2026.*""",
    },
    {
        "slug": "morocco-pet-import-guide",
        "title": "Moving Pets to Morocco: Rabies Vaccination Rules and What UK Owners Need to Know",
        "description": "Morocco pet import guide for dogs and cats. Rabies vaccination requirements, health certificate process, and practical advice for UK expats relocating to Marrakech, Casablanca, or the coast.",
        "date": "2026-05-12",
        "tags": ["morocco", "africa", "planning"],
        "faqs": [
            ("Does Morocco require a rabies titre test?",
             "No. Morocco does not require a rabies antibody titre test. A current rabies vaccination (administered at least 30 days before travel) is sufficient, along with a government-endorsed health certificate and ISO microchip."),
            ("Is there quarantine for pets entering Morocco?",
             "There is no mandatory quarantine period for pets arriving in Morocco with complete and correct documentation. Animals are inspected by vets at the point of entry."),
            ("Which breeds are banned in Morocco?",
             "Morocco does not publish a specific list of banned breeds at the national level, but Pit Bull-type dogs and other breeds classified as dangerous may face restrictions. Check with the ONSSA (Office National de Sécurité Sanitaire des Produits Alimentaires) before travel."),
        ],
        "body": """Morocco is a popular destination for UK and European expats, particularly around Marrakech, Essaouira, Agadir, and Tangier. The pet import process is comparatively straightforward, without the complexity of quarantine or titre testing.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current; must be administered at least 30 days before entry |
| Health certificate | Issued by official vet in country of origin, endorsed by government authority |
| Anti-parasitic treatment record | Recommended; some border vets ask for tapeworm treatment evidence |

## No Titre Test Required

Unlike Australia, New Zealand, and Japan, Morocco does **not** require a rabies antibody titre test. A valid current rabies vaccination is sufficient.

## Health Certificate Endorsement

Your health certificate must be signed by an accredited vet and then endorsed (countersigned) by the government veterinary authority in your origin country:
- **UK:** APHA (Animal and Plant Health Agency)
- **USA:** USDA APHIS
- **EU:** The national competent authority of the member state

Allow 5-10 working days for government endorsement. Book the vet appointment accordingly.

## Entry Points

Main airports for pet arrivals: Mohammed V International (Casablanca), Marrakech Menara, Agadir Al Massira. Animals are inspected by ONSSA vets on arrival. Notify the destination airport's veterinary services in advance for cargo shipments.

## Practical Notes for Expats

Rabies is present in Morocco. Keep vaccinations current for your pet's safety throughout their stay. Local veterinary care is available in major cities but variable in quality — identify a vet before you arrive.

Morocco is warm to hot year-round. Airlines may apply heat embargoes on cargo in summer (June-September). Plan travel for cooler months if possible.

## Cost Estimate (UK to Morocco)

| Item | Estimated Cost |
|------|----------------|
| Government health certificate + APHA endorsement | £200-350 |
| Airline cargo or cabin fee | £150-600 |
| **Total** | **~£350-950** |

---

*Sources: Morocco ONSSA official guidance; APHA UK pet export requirements. Data current as of May 2026.*""",
    },
    {
        "slug": "ghana-pet-import-guide",
        "title": "Moving Pets to Ghana: Veterinary Import Permits, Rabies Rules, and Expat Advice",
        "description": "Pet import guide for Ghana. The Veterinary Services Directorate permit, vaccination requirements, health certificate process, and practical tips for UK nationals relocating to Accra.",
        "date": "2026-05-14",
        "tags": ["ghana", "africa", "planning"],
        "faqs": [
            ("Do I need an import permit to bring a dog into Ghana?",
             "Yes. An import permit from Ghana's Veterinary Services Directorate (VSD) is required before the animal travels. Contact the VSD well in advance of your travel date to obtain the permit and confirm current requirements."),
            ("Is there quarantine for pets entering Ghana?",
             "Ghana does not currently mandate a fixed quarantine period for pets arriving with complete documentation. However, VSD vets will inspect animals on arrival and can order detention if paperwork is incomplete."),
            ("Is rabies vaccination required?",
             "Yes. A current rabies vaccination is mandatory. Some sources indicate a 30-day pre-travel minimum. Check directly with Ghana's VSD for the current minimum interval requirement before booking."),
        ],
        "body": """Ghana has a stable pet import system operated by the **Veterinary Services Directorate (VSD)** under the Ministry of Food and Agriculture. Advance planning and direct communication with the VSD is the key to a smooth process.

## Permit First

Before booking flights, obtain an **import permit from the VSD**. You'll need to provide:
- Species, breed, age, sex, and microchip number
- Owner's passport details and Ghana contact address
- Copy of current vaccination records

Apply at least 4-6 weeks before intended travel.

## Documentation Package

| Document | Requirement |
|----------|-------------|
| Import permit | Obtained from VSD in advance |
| ISO microchip | Yes |
| Rabies vaccination | Current |
| Other vaccinations | Distemper, hepatitis, parvovirus for dogs; calicivirus, panleukopenia for cats |
| Health certificate | Issued by accredited vet, endorsed by government authority (APHA for UK) |
| Parasite treatment | Tapeworm and tick treatment recommended |

## Entry Point

Kotoka International Airport (ACC) in Accra is the standard entry point. Notify the VSD and airport veterinary office in advance for cargo shipments. The VSD will inspect the animal and documentation on arrival before releasing the pet.

## Climate and Timing

Accra is tropical — hot and humid year-round. Summer travel adds airline heat embargo risk. Airlines may refuse cargo in peak heat. The harmattan season (November-February) brings drier, cooler conditions and is often easier for pet cargo logistics.

## Veterinary Care in Ghana

Veterinary services exist in Accra and Kumasi but are limited outside major cities. Bring a sufficient supply of any regular medications and identify a vet in Accra before you arrive. International pet food brands have limited local availability.

## Cost Estimate (UK to Ghana)

| Item | Estimated Cost |
|------|----------------|
| VSD permit fee | Variable — confirm with VSD |
| Government health certificate + APHA endorsement | £200-350 |
| Airline cargo | £500-1,100 |
| **Total** | **~£700-1,450+** |

---

*Sources: Ghana Veterinary Services Directorate official requirements; APHA UK pet export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "jordan-pet-import-guide",
        "title": "Moving Pets to Jordan: Import Permits, Vaccinations, and Amman Airport Process",
        "description": "Pet import rules for Jordan. What the Ministry of Agriculture requires, breed restrictions, vaccination protocols, and what to expect at Queen Alia International Airport.",
        "date": "2026-05-14",
        "tags": ["jordan", "middle-east", "planning"],
        "faqs": [
            ("Does Jordan require a rabies titre test?",
             "No. Jordan does not require a rabies antibody titre test. A current rabies vaccination and government-endorsed health certificate are the core requirements."),
            ("Which breeds are banned in Jordan?",
             "Jordan bans the import of Pit Bull Terriers and related types. Other breeds may be restricted. Check with Jordan's Ministry of Agriculture before booking."),
            ("Is there quarantine for pets entering Jordan?",
             "No mandatory quarantine exists for pets arriving with complete documentation. Animals are inspected by Ministry of Agriculture vets at Queen Alia International Airport on arrival."),
        ],
        "body": """Jordan is home to a significant expat population around Amman and Aqaba, and the pet import process — while bureaucratic — is navigable with preparation.

## Import Permit

Jordan requires an **import approval from the Ministry of Agriculture** before the animal travels. Apply through the Jordanian Embassy in your home country or via a licensed Jordanian agent. Allow 3-4 weeks minimum.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| Import permit/approval | From Jordan Ministry of Agriculture |
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current |
| Full vaccination record | Distemper, parvovirus, hepatitis for dogs |
| Health certificate | Issued by official vet, endorsed by government authority |
| Parasite treatment | Tapeworm and tick treatment within 5 days of travel |

## At Queen Alia International Airport

Arrive with all documents in order. Ministry of Agriculture vets inspect arriving animals in the veterinary inspection area. Present original documents — photocopies are not accepted. If documentation is incomplete, the animal may be held.

## Breed Restrictions

Pit Bull Terriers and types that substantially resemble them are prohibited. If your dog is a stocky, muscular breed, carry breed registration papers and a letter from a vet confirming breed identity.

## Climate Considerations

Amman is cooler than Gulf cities but summers (June-August) are hot. Airlines may apply cargo embargoes in peak summer. Travel in spring or autumn where possible.

## Cost Estimate (UK to Jordan)

| Item | Estimated Cost |
|------|----------------|
| Health certificate + APHA endorsement | £200-350 |
| Airline cargo | £400-900 |
| **Total** | **~£600-1,250** |

---

*Sources: Jordan Ministry of Agriculture official pet import requirements; APHA UK export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "costa-rica-pet-import-guide",
        "title": "Moving Pets to Costa Rica: SENASA Rules, Vaccinations, and Zero-Quarantine Entry",
        "description": "How to import a dog or cat into Costa Rica. SENASA health certificate requirements, vaccination records, no quarantine on arrival, and tips for expats heading to San José or the coast.",
        "date": "2026-05-16",
        "tags": ["costa-rica", "latin-america", "planning"],
        "faqs": [
            ("Is there quarantine for pets entering Costa Rica?",
             "No. Costa Rica does not require quarantine for pets arriving with a valid SENASA health certificate, current vaccinations, and an ISO microchip. Animals are inspected on arrival at Juan Santamaría International Airport."),
            ("Does my pet need a rabies titre test for Costa Rica?",
             "No. Costa Rica does not require a rabies antibody titre test. A current rabies vaccination (within validity period) is sufficient."),
            ("What is a SENASA health certificate?",
             "SENASA (Servicio Nacional de Sanidad Animal) is Costa Rica's animal health authority. A health certificate must be issued by a USDA-accredited or equivalent government vet in your country, endorsed by the relevant authority (USDA APHIS for US pets, APHA for UK pets), and presented on arrival. The certificate must be issued within 30 days of travel."),
        ],
        "body": """Costa Rica is a popular destination for North American and European expats and retirees — and it's one of the more pet-friendly countries in Latin America. No quarantine, no titre test, and straightforward documentation make the process manageable.

## No Quarantine

Costa Rica operates a **documentation-based import system** rather than quarantine. If your paperwork is correct, your pet is released on arrival after inspection. Incomplete documentation can lead to the animal being held or returned — so precision matters.

## Core Documentation

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current and within validity period |
| Distemper/parvovirus/hepatitis (dogs) | Current |
| Feline respiratory and panleukopenia (cats) | Current |
| Health certificate | Issued within 30 days of travel, endorsed by government authority |
| International air waybill number | Required for cargo shipments |

## Health Certificate Details

The health certificate must:
- Be issued on official government letterhead or SENASA-accepted format
- Be signed by an accredited vet
- Be endorsed by the government authority (APHA for UK, USDA APHIS for USA)
- State that the animal has been examined and is free of signs of infectious disease

**UK to Costa Rica:** Book your OV vet appointment well in advance of the APHA endorsement window. APHA endorsement adds 5-10 working days.

## Entry at Juan Santamaría Airport

All pets arriving in Costa Rica enter through Juan Santamaría International Airport (SJO) near San José. The SENASA inspection office is at the airport. Present all original documents. Cargo pets are collected from the cargo terminal after inspection.

## Small Dog Cabin Option

Costa Rica-bound routes typically connect through Miami, Houston, or New York. Airlines that allow small dogs in the cabin (under 8 kg including carrier) include United, American, and Delta for North American connections. Check individual airline policies for transatlantic legs.

## Cost Estimate (UK to Costa Rica)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + APHA endorsement | £200-350 |
| Airline cargo | £600-1,200 |
| **Total** | **~£800-1,550** |

---

*Sources: Costa Rica SENASA official pet import requirements; APHA UK export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "peru-pet-import-guide",
        "title": "Moving Pets to Peru: SENASA Import Permits and Lima Airport Veterinary Inspection",
        "description": "Peru pet import rules for dogs and cats. The SENASA permit and health certificate process, vaccination requirements, and what happens at Jorge Chávez International Airport.",
        "date": "2026-05-16",
        "tags": ["peru", "latin-america", "planning"],
        "faqs": [
            ("Do I need an import permit for a pet entering Peru?",
             "You need a prior notification/authorisation from Peru's SENASA (Servicio Nacional de Sanidad Agraria). This is obtained by submitting vaccination records and health documentation before travel. An in-person import permit is not always required for personal pets, but pre-arrival notification to SENASA is mandatory."),
            ("Is there quarantine in Peru?",
             "No mandatory quarantine exists for pets arriving with complete documentation. SENASA vets inspect animals on arrival at Jorge Chávez International Airport in Lima."),
            ("What vaccinations does Peru require for dogs?",
             "Peru requires current rabies vaccination, distemper, hepatitis, leptospirosis, and parvovirus for dogs. For cats: rabies, feline panleukopenia (FPV), and feline respiratory viruses."),
        ],
        "body": """Peru is a destination for a growing number of expats, digital nomads, and those retiring to South America. The pet import system is managed by **SENASA** (Servicio Nacional de Sanidad Agraria) and requires pre-arrival notification and a government-endorsed health certificate.

## Pre-Arrival Notification

Before your pet travels to Peru, send the following to SENASA via their official portal or email:
- Current vaccination records
- Microchip number
- Health certificate draft (for pre-approval where required)

Allow at least 2-3 weeks for pre-arrival authorisation. SENASA will confirm documentation requirements based on your origin country.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current |
| Core vaccinations | Distemper, hepatitis, leptospirosis, parvovirus (dogs); FPV and respiratory viruses (cats) |
| Internal/external parasite treatment | Within 30 days of travel |
| Health certificate | Issued within 10-14 days of travel, endorsed by government authority |
| SENASA pre-arrival authorisation | Yes |

## Arrival at Jorge Chávez International Airport

Lima's Jorge Chávez Airport (LIM) is the primary entry point. SENASA vets are on site for inspections. Cargo pets are held in the cargo terminal pending inspection. Present original documents — SENASA may retain copies.

Expect 1-3 hours for inspection and clearance on a good day. Plan your onward connection accordingly.

## Airlines Serving Lima

Connections to Lima from the UK typically route through Madrid (Iberia), Amsterdam (KLM), or Miami (American/United). LATAM Airlines operates within South America. KLM and Iberia accept pets in cargo on European legs.

## Cost Estimate (UK to Peru)

| Item | Estimated Cost |
|------|----------------|
| Government health certificate + APHA endorsement | £200-350 |
| Airline cargo (multi-leg) | £700-1,400 |
| **Total** | **~£900-1,750** |

---

*Sources: Peru SENASA official pet import guidance; APHA UK export documentation requirements. Data current as of May 2026.*""",
    },
    {
        "slug": "mauritius-pet-import-guide",
        "title": "Moving Pets to Mauritius: 30-Day Quarantine and the 6-Month Residency Rule",
        "description": "Mauritius has some of the strictest pet import rules in the Indian Ocean. 30-day quarantine, a 6-month wait period post-vaccination, and limited arrival routes — what you need to know.",
        "date": "2026-05-18",
        "tags": ["mauritius", "indian-ocean", "planning"],
        "faqs": [
            ("How long is quarantine in Mauritius?",
             "All dogs and cats entering Mauritius must complete a minimum 30-day quarantine at the government quarantine facility. There are no exemptions based on origin country, vaccination status, or titre test results."),
            ("Is there a waiting period after rabies vaccination before a pet can enter Mauritius?",
             "Yes. Mauritius requires that the rabies vaccination is administered at least 6 months before the animal's arrival. Combined with the 30-day quarantine, this means you need to start preparations at least 7 months before your intended arrival date."),
            ("Can I visit my pet during quarantine in Mauritius?",
             "Yes. The quarantine facility allows owner visits during designated hours. Contact the Ministry of Agro-Industry and Food Security for current visiting arrangements."),
        ],
        "body": """Mauritius is one of the most beautiful islands in the Indian Ocean, and it maintains some of the most rigorous pet import requirements in the world. The combination of mandatory quarantine and pre-travel waiting periods means you need to start planning at least **seven months before** your intended move date.

## The 30-Day Mandatory Quarantine

Every dog and cat entering Mauritius — regardless of origin country, vaccination history, or titre test status — completes a **30-day quarantine** at the government-approved facility. There are no exemptions.

The quarantine facility is operated by the Ministry of Agro-Industry and Food Security (MAIFS). Costs are borne by the owner.

## The 6-Month Vaccination Wait

Mauritius requires that the rabies vaccination was administered **at least 6 months before the animal arrives**. This is not a 180-day titre test wait (as required by Australia) — it is a 180-day post-vaccination holding period.

Combined with quarantine, your preparation timeline looks like this:
1. Administer rabies vaccination
2. Wait 6 months
3. Obtain health certificate (within 10 days of travel)
4. Travel
5. 30-day quarantine on arrival

Start at Month 0. Earliest possible arrival: Month 7+.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Rabies vaccination | At least 6 months before arrival |
| Full vaccination record | Distemper, parvo, hepatitis for dogs |
| Rabies titre test | Required — must confirm adequate titre |
| Health certificate | Issued within 10 days of travel |
| CITES permit | If the species/breed is CITES-listed |
| Import permit from MAIFS | Yes — apply well in advance |

## Import Permit Process

Apply for an import permit from the **Ministry of Agro-Industry and Food Security** at least 3 months before travel. The permit will specify the quarantine facility and arrival date window.

## Permitted Entry Points

Only specific entry ports are approved for live animal import. Commercial air cargo through Sir Seewoosagur Ramgoolam International Airport (MRU) is the standard route.

## Cost Estimate (UK to Mauritius)

| Item | Estimated Cost |
|------|----------------|
| Import permit | MUR variable |
| Titre test | £150 |
| Government health certificate + APHA endorsement | £200-350 |
| 30-day quarantine facility fee | MUR 10,000-30,000+ (~£170-520+) |
| Airline cargo | £600-1,200 |
| **Total** | **~£1,200-2,400+** |

---

*Sources: Mauritius Ministry of Agro-Industry and Food Security (MAIFS) official import requirements. Data current as of May 2026.*""",
    },
    {
        "slug": "nepal-pet-import-guide",
        "title": "Moving Pets to Nepal: Kathmandu Import Rules and What Expats Need to Know",
        "description": "Nepal pet import guide. Department of Livestock Services permit, vaccination requirements, and practical advice for expats and aid workers relocating to Kathmandu with dogs or cats.",
        "date": "2026-05-18",
        "tags": ["nepal", "asia", "planning"],
        "faqs": [
            ("Do I need a permit to bring a pet to Nepal?",
             "Yes. An import permit from Nepal's Department of Livestock Services (DLS) is required before the animal travels. Apply through the DLS or Nepal Embassy in your home country."),
            ("Is there quarantine for pets entering Nepal?",
             "No mandatory quarantine period. DLS vets inspect animals at Tribhuvan International Airport in Kathmandu. Animals with complete documentation are typically cleared on the same day."),
            ("What vaccinations does Nepal require?",
             "Rabies vaccination (current), distemper, parvovirus, and hepatitis for dogs; rabies, panleukopenia, and respiratory viruses for cats. All vaccinations must be recorded in the health certificate."),
        ],
        "body": """Nepal attracts NGO workers, trekking guides, diplomats, and long-term volunteers — many of whom relocate with pets. The country's pet import system is managed by the **Department of Livestock Services (DLS)** and requires advance planning but no quarantine.

## Import Permit

Apply for an import permit from Nepal's **Department of Livestock Services** before travel. Contact the nearest Nepalese Embassy or consulate for the current application form and fees. Allow 3-4 weeks for processing.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| DLS import permit | Obtained before travel |
| ISO microchip (15-digit preferred) | Yes |
| Rabies vaccination | Current |
| Core vaccinations | Distemper, parvo, hepatitis (dogs); panleukopenia, respiratory viruses (cats) |
| Internal parasite treatment | Within 30 days of travel |
| Health certificate | Issued and endorsed by government authority in origin country |

## Arrival at Tribhuvan International Airport

Kathmandu's Tribhuvan International Airport (KTM) is the only international airport with DLS veterinary presence. All international pet arrivals enter through KTM. Notify the DLS and your airline's cargo team in advance.

Cargo pets are collected from the cargo terminal after DLS inspection and clearance. Allow 2-4 hours.

## Veterinary Care in Nepal

Quality veterinary care is available in Kathmandu, with several clinics familiar with expat pet needs. Outside Kathmandu, veterinary facilities are limited. Stock up on any regular medications before arriving and identify a Kathmandu vet in advance.

## Practical Notes

Nepal's summer monsoon season (June-September) brings heavy rain and disruption to air routes. Travel in the pre-monsoon (March-May) or post-monsoon (October-November) window for more reliable logistics.

## Cost Estimate (UK to Nepal)

| Item | Estimated Cost |
|------|----------------|
| DLS permit fee | NPR variable (~£10-30 estimate) |
| Government health certificate + endorsement | £200-350 |
| Airline cargo | £600-1,200 |
| **Total** | **~£810-1,580** |

---

*Sources: Nepal Department of Livestock Services import requirements; APHA UK export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "ethiopia-pet-import-guide",
        "title": "Moving Pets to Ethiopia: Veterinary Import Permits and Addis Ababa Entry Guide",
        "description": "Pet import guide for Ethiopia. The Ministry of Agriculture permit process, vaccination requirements, and what expats and NGO workers need to know before flying to Addis Ababa.",
        "date": "2026-05-20",
        "tags": ["ethiopia", "africa", "planning"],
        "faqs": [
            ("Do I need an import permit for a pet entering Ethiopia?",
             "Yes. An import permit from Ethiopia's Ministry of Agriculture (MoA) is required before the animal travels. Apply well in advance through the MoA or the nearest Ethiopian Embassy."),
            ("Is there quarantine in Ethiopia?",
             "No fixed quarantine period exists for pets arriving with complete documentation. Ministry of Agriculture vets at Bole International Airport inspect animals on arrival."),
            ("What vaccinations are required for dogs entering Ethiopia?",
             "Rabies vaccination (current), distemper, hepatitis, parvovirus, and leptospirosis. All must be recorded in the government-endorsed health certificate."),
        ],
        "body": """Ethiopia is a significant hub for international NGO activity, UN agencies, and African Union operations, making Addis Ababa home to a large expat community. Pet import is managed through the **Ministry of Agriculture (MoA)** and requires a government import permit.

## Import Permit

Apply through Ethiopia's **Ministry of Agriculture** or the nearest Ethiopian Embassy. You will need to provide:
- Vaccination records
- Microchip number
- Owner passport and Ethiopia residency documentation
- Details of the animal (species, breed, sex, age)

Allow at least 4-6 weeks for processing.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| Import permit from MoA | Yes — before travel |
| ISO microchip | Yes |
| Rabies vaccination | Current |
| Full vaccination record | Distemper, hepatitis, parvovirus, leptospirosis (dogs) |
| Internal/external parasite treatment | Within 14 days of travel |
| Health certificate | Issued within 10 days of travel, endorsed by government authority |

## Arrival at Bole International Airport

All international pets arrive through **Bole International Airport (ADD)** in Addis Ababa. MoA vets are on site for inspections. Cargo clearance can take 3-6 hours. Notify the airline's cargo team and the MoA veterinary office in advance.

Ethiopian Airlines, one of Africa's largest carriers, operates extensive international routes to Addis Ababa and has experience handling live animal cargo.

## Practical Notes

Addis Ababa is at 2,355 metres altitude, which means temperatures are mild year-round despite its latitude. This is a genuine advantage for pet cargo logistics — no extreme heat embargoes. Outside Addis Ababa, veterinary care is very limited. Bring adequate medication supplies.

## Cost Estimate (UK to Ethiopia)

| Item | Estimated Cost |
|------|----------------|
| MoA permit fee | Variable |
| Government health certificate + APHA endorsement | £200-350 |
| Airline cargo | £600-1,100 |
| **Total** | **~£800-1,450** |

---

*Sources: Ethiopia Ministry of Agriculture official import guidance; APHA UK export requirements. Data current as of May 2026.*""",
    },
    {
        "slug": "how-to-move-a-dog-internationally",
        "title": "How to Move a Dog Internationally: The Complete Step-by-Step Guide",
        "description": "Everything dog owners need to know about international relocation. From microchipping to health certificates, airline booking to destination arrival — the complete process in order.",
        "date": "2026-05-20",
        "tags": ["planning", "dogs", "health-certificates"],
        "faqs": [
            ("How far in advance do I need to start preparing to move my dog internationally?",
             "For most countries: 8-12 weeks minimum (microchip, vaccinations, health certificate, airline booking). For Australia, New Zealand, or Japan: 6-9 months minimum due to titre test waiting periods and quarantine. Start earlier than you think you need to."),
            ("Can I move my dog without a pet transport agent?",
             "Yes, for straightforward routes (e.g., UK to most EU countries, USA to Canada). For complex routes — quarantine countries, breed-restriction destinations, multiple connections — a specialist IPATA-member agent significantly reduces the risk of errors that could leave your dog stranded."),
            ("What documents does my dog need for international travel?",
             "The core package: ISO 15-digit microchip scan record, current rabies vaccination, government-endorsed health certificate. Country-specific additions: titre test (Australia/NZ/Japan), import permit (Middle East, Africa, Southeast Asia), breed documentation (restricted-breed destinations)."),
        ],
        "body": """Moving a dog to another country is entirely achievable — millions of dogs relocate internationally every year. The process is more complex than booking a seat, but it follows a clear sequence. Get the steps right in the right order and your dog arrives safely.

## Step 1: Microchip (If Not Already Done)

Your dog needs an **ISO 15-digit microchip** (134.2 kHz standard). This must be in place **before** any vaccination is recorded in the health documentation. A vaccination given before microchipping is not officially linked to your dog's ID and may not be accepted.

If your dog is already microchipped, check the number with a universal scanner (some UK chips are 10-digit — these are not ISO 15-digit compliant for international travel).

## Step 2: Rabies Vaccination

Once the microchip is confirmed, your vet records a rabies vaccination in the health documentation. Most countries require a current rabies vaccination — within the validity period stated by the manufacturer (typically 1 or 3 years).

**For Australia, New Zealand, and Japan:** The rabies vaccination must be done before a blood sample for the titre test. The titre test result must be confirmed at least 180 days before entry. This is the clock that determines your earliest travel date.

## Step 3: Check Destination Country Requirements

Look up the official import rules for your destination country **before** any other steps. Rules vary by:
- Titre test requirements
- Import permit requirements
- Quarantine
- Breed restrictions
- Entry port restrictions

**Primary sources:** USDA APHIS (USA), APHA (UK), DAFF (Australia), MAFF (Japan), EU TRACES portal. Avoid relying on third-party summaries — regulations change.

## Step 4: Book Your Vet and Government Endorsement

Health certificates for international travel must be:
- Issued by an accredited or Official Veterinarian (OV)
- Endorsed by the government authority (APHA in the UK, USDA APHIS in the USA)
- Issued within a specific window before travel (often 10 days, but varies)

Book your vet **before** you book flights. APHA endorsement in the UK takes 3-7 working days — factor that into your timeline.

## Step 5: Choose Your Airline and Book Cargo

Research which airlines:
- Accept your dog's breed (some ban brachycephalic breeds)
- Serve your destination with direct or minimal-connection routing
- Have cargo space available (book as early as possible — large dogs compete for limited hold space)

Check the airline's own live animal policy — not a third-party summary.

## Step 6: IATA-Compliant Crate

Your dog needs an IATA-compliant crate:
- Dog can stand without head touching the roof
- Dog can turn around fully
- Dog can lie in a natural position
- Crate has water/food holders accessible from outside
- Ventilation on 3 sides minimum

Introduce the crate weeks before travel — a dog comfortable sleeping in its crate is far less stressed during transit.

## Step 7: Travel Day

- Do not feed within 4 hours of the flight
- Exercise before departure
- Keep the check-in process calm
- Include a worn item of clothing in the crate for scent comfort
- Freeze the water dish so it melts slowly in transit

## Step 8: Arrival and Clearance

Present all original documents to the border veterinary authority. Keep digital copies as backup. For quarantine countries, confirm the quarantine facility address and booking before travel.

---

*Sources: IATA Live Animals Regulations 2024; APHA official pet travel guidance; USDA APHIS pet import requirements. Data current as of May 2026.*""",
    },
    {
        "slug": "how-to-move-a-cat-to-australia",
        "title": "How to Move a Cat to Australia: Titre Tests, Quarantine, and the 8-Month Timeline",
        "description": "Australia's cat import process explained step by step. The titre test requirement, 180-day wait, Mickleham quarantine, health certificates, and how to plan an 8-month preparation timeline.",
        "date": "2026-05-22",
        "tags": ["australia", "cats", "quarantine", "planning"],
        "faqs": [
            ("How long does it take to prepare a cat for Australia?",
             "A minimum of 6-8 months from starting the titre test process to arrival in Australia. If your cat's vaccinations are not yet current or the microchip was implanted after the first vaccination, add more time. Most owners allow 8-10 months to have a comfortable margin."),
            ("Can a cat fly in the cabin to Australia?",
             "No. Australia does not permit pets to travel in the cabin of commercial aircraft. All cats travel as manifest cargo and complete mandatory quarantine on arrival."),
            ("How much does it cost to send a cat to Australia?",
             "A complete UK-to-Australia move for a cat typically costs £3,000-6,000+, including the titre test, health certificate and endorsement, airline cargo, and mandatory 10-day quarantine at Mickleham. Costs vary by the cat's size, chosen airline, and agent fees."),
        ],
        "body": """Australia imposes some of the world's strictest pet import conditions. For cats, the process involves a titre test, a 180-day waiting period, a government-endorsed health certificate, and mandatory quarantine on arrival. The total timeline is typically 8-10 months from starting preparations.

## Why So Strict?

Australia is rabies-free. Maintaining that status requires rigorous biosecurity controls. Every cat (and dog) entering Australia must prove it has been adequately immunised against rabies — not just vaccinated, but confirmed to have mounted an antibody response above the required threshold.

## Step-by-Step Process

### Month 0: Microchip and Vaccination
- Confirm ISO 15-digit microchip is in place (must be done before vaccination)
- Administer or confirm current rabies vaccination

### Month 1-2: Titre Test Blood Sample
- Blood sample taken by accredited vet
- Sent to an Australian Department of Agriculture, Fisheries and Forestry (DAFF)-approved laboratory
- For UK cats: APHA Weybridge is DAFF-approved; other approved labs listed on DAFF website
- Titre result must be ≥0.5 IU/mL to confirm adequate immunity

### Month 2-8: The 180-Day Wait
- Once DAFF confirms the titre result at ≥0.5 IU/mL, a 180-day clock starts
- The cat cannot enter Australia until 180 days after the confirmation date
- During this period: keep vaccinations current; no lapses in coverage

### Month 7-8: Health Certificate and Booking
- Book your airline and cargo space at least 8 weeks in advance
- Your OV (Official Veterinarian) issues the health certificate within the window required by DAFF
- APHA endorses the health certificate (allow 5-7 working days)

### Month 8: Travel and Quarantine
- Cat travels as manifest cargo
- On arrival, DAFF vets inspect the cat and documentation at the airport
- Cat is transferred to **Mickleham Quarantine Facility** in Victoria for mandatory quarantine (minimum 10 days)
- Owner cannot take the cat home until quarantine is complete and DAFF issues a release notice

## Cost Breakdown

| Item | Estimated Cost |
|------|----------------|
| Titre test (lab + vet) | £150-250 |
| Health certificate + APHA endorsement | £250-400 |
| Airline cargo (UK to Australia) | £900-2,000 |
| Quarantine facility fee | AUD 2,000-4,000 (~£1,000-2,100) |
| Agent fee (if used) | £400-800 |
| **Total** | **~£2,700-5,550** |

## Approved Entry Airports

Cats must arrive at an airport with a DAFF-approved facility. Major approved airports: Sydney (SYD), Melbourne (MEL), Brisbane (BNE), Perth (PER).

---

*Sources: Australian Department of Agriculture, Fisheries and Forestry (DAFF) official cat import requirements; APHA UK pet export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "pet-import-permit-guide",
        "title": "When Do You Need a Pet Import Permit? A Country-by-Country Guide",
        "description": "Not all countries require import permits for pets. This guide explains which destinations need advance permits, how to apply, and what happens if you arrive without one.",
        "date": "2026-05-22",
        "tags": ["planning", "permits", "regulations"],
        "faqs": [
            ("Which countries require advance import permits for pets?",
             "Middle Eastern countries (Oman, Kuwait, Bahrain, Qatar, Jordan, UAE), most African countries (Kenya, Ghana, Tanzania, Ethiopia, Nigeria), Southeast Asian countries (Philippines, Vietnam, Cambodia, Myanmar), and some others including Mauritius and Mexico. EU and most Western countries do not require pre-import permits."),
            ("What happens if I arrive at a country with my pet but no import permit?",
             "Your pet may be refused entry and held in quarantine at your expense, or returned to the origin country on the next available flight. In some countries, the animal may be impounded. Always obtain required permits before travel."),
            ("How far in advance do I need to apply for a pet import permit?",
             "Allow a minimum of 4-6 weeks. Some countries (Mauritius, Australia) have permit processes that take longer. Apply as early as possible once your travel dates are confirmed."),
        ],
        "body": """Many pet owners are surprised to discover they need official government permission — an import permit — before their pet can enter certain countries. Missing this step is one of the most common causes of animals being held at borders, returned to origin, or placed in quarantine at the owner's expense.

Here's a clear breakdown of which countries require advance permits and what the process involves.

## Countries Where an Import Permit IS Required

### Middle East
| Country | Authority | Notes |
|---------|-----------|-------|
| UAE | Ministry of Climate Change & Environment | Apply via TRACES or authorised UAE agent |
| Oman | MARA | Apply 4+ weeks before travel |
| Kuwait | PAHW | Required for all non-GCC origins |
| Qatar | MOPH | Required; process through Hamad Airport vet authority |
| Bahrain | MIAM | Required |
| Jordan | Ministry of Agriculture | Required |
| Saudi Arabia | MEWA | Required; breed restrictions apply |

### Africa
| Country | Authority | Notes |
|---------|-----------|-------|
| Kenya | Directorate of Veterinary Services | Required |
| Ghana | Veterinary Services Directorate | Required |
| Tanzania | MLFD | Required |
| Nigeria | NAQS | Required |
| Ethiopia | Ministry of Agriculture | Required |
| Zimbabwe | Department of Veterinary Services | Required |
| Mauritius | MAIFS | Required + quarantine; very strict |

### Asia-Pacific
| Country | Authority | Notes |
|---------|-----------|-------|
| Philippines | BAI | Required; process takes 4-6 weeks |
| Vietnam | Sub-Department of Animal Health | Required |
| Cambodia | Department of Animal Health | Required |
| Myanmar | Department of Animal Husbandry | Required |
| Australia | DAFF | Permit issued as part of pre-export approval |
| New Zealand | MPI | Pre-export approval required |

### Americas
| Country | Authority | Notes |
|---------|-----------|-------|
| Peru | SENASA | Pre-arrival notification/authorisation |
| Mexico | SENASICA | Import certificate required |

## Countries Where an Import Permit is NOT Required

Most Western countries do not require a pre-import permit:
- **UK:** No permit. Microchip, vaccination, AHC or health certificate only
- **USA:** No permit for personal pets from most countries
- **EU member states:** No permit. Documentation only (AHC for non-EU origin)
- **Canada:** No permit for dogs/cats from most countries
- **Japan:** No permit per se, but strict pre-notification to MAFF required

## How to Apply

Most permit applications require:
1. Owner's passport/residency details
2. Animal species, breed, age, microchip number
3. Current vaccination records
4. Proof of residence at destination
5. The health certificate (or draft) from your vet

Submit via the destination government portal, through their embassy in your home country, or via a licensed agent in the destination country.

---

*Sources: IATA Travel Centre; individual country government authority websites. Data current as of May 2026.*""",
    },
    {
        "slug": "flying-with-small-dogs-in-cabin-guide",
        "title": "Flying with Small Dogs in the Cabin: Which Airlines Allow It and the Rules You Need to Know",
        "description": "Which international airlines allow small dogs in the cabin, what the weight and carrier rules are, and how to book in-cabin pet travel without surprises.",
        "date": "2026-05-24",
        "tags": ["dogs", "cabin-travel", "airlines"],
        "faqs": [
            ("Which airlines allow small dogs in the cabin on international routes?",
             "Airlines that commonly allow small dogs in-cabin on international routes include Lufthansa, KLM, Air France, Iberia, Turkish Airlines, Emirates (on some routes), Singapore Airlines (on some routes), and several US carriers (United, American, Delta on domestic/near-international). British Airways does not allow pets in-cabin on any routes."),
            ("What is the weight limit for a dog in the cabin?",
             "Most airlines apply an 8 kg maximum for the combined weight of the dog and carrier. Some carriers allow up to 10 kg. Weigh your dog in its carrier before booking — exceeding the limit on the day means your dog travels as cargo."),
            ("Does my dog need any special documents to travel in the cabin?",
             "The same health documentation applies as for cargo: microchip, current rabies vaccination (if required by the destination), and a government-endorsed health certificate or AHC for certain routes. The difference is physical location on the plane, not documentation requirements."),
        ],
        "body": """Travelling with a small dog in the cabin is a real option on many international routes — it avoids the hold, keeps the dog with you, and is generally less stressful for both animal and owner. But the rules are strict, vary by airline, and catching the wrong one can result in your dog being rejected at check-in.

## The In-Cabin Weight Rule

The universal constant: **the combined weight of dog and carrier must be under the airline's limit.** Most carriers set this at 8 kg. Some allow up to 10 kg. A few budget carriers ban cabin pets entirely.

Weigh your dog in its actual travel carrier before booking — not estimated weight, actual combined weight. Airlines weigh at check-in. Exceeding the limit means the dog must travel as checked cargo, which may not be possible on the same flight.

## Carrier Dimensions

The carrier must fit under the seat in front of you. Airlines specify maximum dimensions, typically around **55 x 35 x 25 cm** though this varies. Buy the carrier before booking and check it against your specific airline's published dimensions.

The dog must be able to stand, turn around, and lie down in the carrier.

## Airlines That Allow Cabin Pets on International Routes

| Airline | Cabin pets | Weight limit | Notes |
|---------|-----------|--------------|-------|
| Lufthansa | Yes | 8 kg | Most international routes |
| KLM | Yes | 8 kg | Most international routes |
| Air France | Yes | 8 kg | Most international routes |
| Iberia | Yes | 8 kg | Including long-haul |
| Turkish Airlines | Yes | 8 kg | Including long-haul |
| Emirates | Selected routes | 8 kg | Not all routes |
| Singapore Airlines | Selected routes | 7 kg | Not all routes |
| United (USA) | Yes | 10 kg approx | US/near-international routes |
| American Airlines | Yes | 7 kg approx | Varies by route |
| Delta | Yes | Varies | Check current policy |
| Qantas | No | — | Cargo only for all pets |
| British Airways | No | — | No cabin pets (assistance only) |

*Always verify the current policy directly with the airline before booking — policies change.*

## Booking the Cabin Pet Spot

Cabin pet spots are limited — often 1-2 per flight. Book as early as possible and confirm the cabin pet reservation when you receive your booking confirmation. Some airlines do not allow you to book cabin pets online and require a phone call.

## During the Flight

The dog must stay in the carrier, under the seat, for the **entire flight**. Taking the dog out is not permitted. Most dogs settle after takeoff if they've been crate-trained. A worn item of your clothing in the carrier helps.

## Documentation Reminder

Health documentation applies regardless of cabin vs. cargo. Check your destination's specific requirements.

---

*Sources: Individual airline official pet policy pages; IATA Live Animals Regulations. Data current as of May 2026.*""",
    },
    {
        "slug": "iata-crate-sizing-complete-guide",
        "title": "IATA Crate Sizing: How to Pick the Right Size for Your Dog or Cat",
        "description": "The complete guide to IATA live animal container sizing. How to measure your pet, which IATA size number applies, and what vents, door, and floor specifications the regulations require.",
        "date": "2026-05-24",
        "tags": ["dogs", "cats", "crates", "planning"],
        "faqs": [
            ("How do I measure my dog for an IATA crate?",
             "Measure four dimensions: (A) length from nose to base of tail + 10 cm; (B) height from floor to top of head or tip of ears (whichever is taller) + 10 cm; (C) elbow height x 2 for minimum door opening height; (D) shoulder width x 1.5 for minimum internal width. The crate must accommodate all four measurements simultaneously."),
            ("What is the difference between IATA sizes 100 to 700?",
             "IATA container numbers correspond to increasing internal dimensions. A 100 is suitable for very small cats and toy breeds. A 700 is for giant breeds. The exact internal dimensions vary by manufacturer — always measure your pet and compare against the specific crate's internal dimensions, not just the size number."),
            ("Can I use a second-hand crate for international pet travel?",
             "Only if it is fully IATA-compliant and undamaged. The crate must have no cracks, all ventilation panels intact, working door latches, secure bolts, and food/water access doors. Airlines will reject crates with structural damage. Buy new if uncertain."),
        ],
        "body": """Getting the crate size right is not a minor detail — it determines whether the airline will accept your pet, whether the journey is humane, and in some cases whether the animal can physically survive the trip in a confined space over many hours.

IATA Regulation CR82 governs the design of live animal containers. Airlines can and do reject crates that do not meet the standard.

## How to Measure Your Pet

Take four measurements with your pet standing naturally:

| Measurement | Method |
|-------------|--------|
| **A — Length** | Tip of nose to base of tail, add 10 cm |
| **B — Height** | Floor to top of head or ears (whichever is higher), add 10 cm |
| **C — Door height** | Elbow height x 2 (minimum opening height) |
| **D — Width** | Shoulder width x 1.5 (minimum internal width) |

The crate's **internal** dimensions must meet or exceed A, B, C, and D simultaneously.

## IATA Container Size Reference

| IATA Size | Approx. Internal L x W x H | Suitable for |
|-----------|----------------------------|--------------|
| 100 | 46 x 31 x 32 cm | Toy breeds, small cats |
| 200 | 53 x 36 x 39 cm | Small cats, small dogs |
| 300 | 61 x 41 x 45 cm | Medium cats, small dogs |
| 400 | 74 x 50 x 53 cm | Medium dogs, large cats |
| 500 | 83 x 57 x 61 cm | Large dogs |
| 700 | 99 x 67 x 74 cm | Giant breeds |

*These are approximate typical dimensions — always check the internal measurements of the specific crate you are buying.*

## Construction Requirements

An IATA-compliant crate must have:
- Rigid walls (no soft-sided crates for cargo)
- Ventilation on at least 3 sides (typically all 4 for larger sizes)
- Secure locking door
- Spacer feet or a raised floor to allow forklift access and airflow underneath
- External food and water access ports
- "Live Animal" and directional arrows on all sides
- Absorbent bedding

## Common Mistakes

**Crate too small:** The dog cannot stand or turn. The airline will refuse it.
**Crate too large:** The dog is thrown around in turbulence. Size up carefully — the dog should have room to move, but not so much that it can't brace itself.
**Soft-sided crate:** Not permitted for hold travel. Cabin pet carriers can be soft-sided; cargo crates must be rigid.
**Missing water bowl:** Airlines require a water dish attached to the inside of the crate door.

## Buying a Crate

Major IATA-compliant crate suppliers: Vari Kennel (Petmate), Marchioro, Zooplus own-brand, and specialist pet transport suppliers. Buy from a supplier that confirms IATA CR82 compliance. Do not repurpose a storage bin or non-pet container.

---

*Sources: IATA Live Animals Regulations (LAR) 2024 Edition, Container Requirement 82. Data current as of May 2026.*""",
    },
    {
        "slug": "moving-pets-to-germany",
        "title": "Moving Pets to Germany: EU Rules, Breed Restrictions, and What to Do at the Airport",
        "description": "Germany pet import guide for dogs and cats from the UK and USA. EU pet travel rules, Animal Health Certificate process, and Germany's specific breed restrictions by state.",
        "date": "2026-05-26",
        "tags": ["germany", "europe", "planning"],
        "faqs": [
            ("Does Germany require a titre test for pets from the UK?",
             "No. Germany, as an EU member state, does not require a rabies titre test for pets arriving with valid rabies vaccinations and a correctly completed Animal Health Certificate (AHC). A titre test is only required for countries like Australia, New Zealand, and Japan."),
            ("Which dog breeds are banned in Germany?",
             "Germany has no federal breed-specific ban. However, individual German states (Laender) have their own breed restriction laws. The most restrictive states are North Rhine-Westphalia, Bavaria, and Hamburg. Breeds commonly regulated include Pit Bull Terriers, American Staffordshire Terriers, Staffordshire Bull Terriers, Bull Terriers, and in some states Rottweilers and Dogos Argentinos. Check the legislation in your specific destination state."),
            ("What do I need to bring a dog from the UK to Germany?",
             "An ISO-microchipped dog with a current rabies vaccination and an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel. The AHC replaces the EU pet passport for UK-to-EU travel post-Brexit."),
        ],
        "body": """Germany is the most common EU destination for UK expats relocating with pets. It's also a significant hub for arrivals from outside the EU. The import process is well-established and manageable — the main complexity is Germany's patchwork of state-level breed restrictions.

## UK to Germany: Post-Brexit Documentation

Since 1 January 2021, UK pets cannot use EU pet passports to enter Germany. Every trip requires:
- **Animal Health Certificate (AHC)** issued by an Official Veterinarian (OV) within 10 days of travel
- ISO 15-digit microchip (must be implanted before first recorded vaccination)
- Current rabies vaccination

Each journey needs a new AHC. It is valid for that trip only (plus 4 months for travel within the EU once issued).

## USA to Germany

Dogs entering Germany from the USA need:
- ISO 15-digit microchip
- Current rabies vaccination (USA CDC-approved vaccine)
- Government-endorsed health certificate (USDA APHIS form 7001 for commercial; equivalent for private)
- If the dog was vaccinated in the USA against rabies, EU regulations require the vaccination record to include the vaccine batch number, brand, and validity date

## Breed Restrictions by State

Germany has no national breed ban. Restrictions are at state (Land) level:

| State | Regulated breeds |
|-------|-----------------|
| North Rhine-Westphalia | Pit Bull, Am. Staff, Staff Bull Terrier, Bull Terrier (stricter than most) |
| Bavaria | Regulated breeds require registration and conditions |
| Hamburg | Multiple breeds subject to mandatory registration |
| Berlin | Category 1 and 2 breeds with varying conditions |
| Saxony | Breed list varies from NRW |

If you own a breed that appears on any German state list, contact the Veterinäramt (veterinary office) in your destination district before travel to understand the registration and keep requirements.

## At Frankfurt, Munich, or Berlin

Germany's main international pet arrival airports are Frankfurt (FRA), Munich (MUC), and Berlin Brandenburg (BER). Documentary checks occur at the border inspection post (BIP) on arrival. Declare your pet at the BIP — failure to do so is a customs offence.

## Cost Estimate (UK to Germany)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | £150-250 |
| APHA endorsement | £50-100 |
| Airline cargo or cabin fee | £50-500 |
| **Total** | **~£250-850** |

---

*Sources: European Commission Regulation 576/2013; APHA UK pet travel guidance; individual German state Landesrecht breed legislation. Data current as of May 2026.*""",
    },
    {
        "slug": "pet-relocation-agent-questions-to-ask",
        "title": "10 Questions to Ask a Pet Relocation Agent Before You Hire Them",
        "description": "Not all pet transport agents are equal. Before you hand over your dog or cat's wellbeing to a third party, here are the questions that separate the professionals from the rest.",
        "date": "2026-05-26",
        "tags": ["planning", "agents", "advice"],
        "faqs": [
            ("What is IPATA and why does it matter?",
             "IPATA (International Pet and Animal Transportation Association) is the global professional body for pet transport. Members agree to a code of ethics and minimum standards. IPATA membership is not a guarantee of quality, but it means the agent has committed to professional standards and has access to training. Non-member agents have no accountability mechanism."),
            ("Is the cheapest pet transport agent a bad choice?",
             "Not automatically, but price is a poor guide to quality in pet transport. The cheapest quote may involve substandard crating, minimal documentation checks, or use of sub-agents with less experience. Get three quotes, compare what's included, and ask every question on this list."),
            ("What should I do if my pet is delayed or there's a problem mid-transit?",
             "Ask this question in the consultation. A good agent will have a clear protocol for flight delays, documentation issues, and veterinary emergencies during transit. An agent who cannot answer this question clearly is not the right choice."),
        ],
        "body": """Handing your pet to a transport agent is an act of trust. Choose the wrong agent and your dog could end up crated in an unventilated holding area, handed to an inexperienced sub-agent, or delayed at a border because of a documentation error that a professional would have caught.

These 10 questions will help you identify agents who know what they're doing.

## 1. Are You an IPATA Member?

IPATA (International Pet and Animal Transportation Association) is the global body for professional pet transport agents. Members agree to ethical standards and participate in ongoing training. Start here — it filters out casual operators immediately.

## 2. Can I See Your IATA Accreditation?

IATA-accredited agents can issue air waybills directly and have been audited by IATA. This matters for cargo logistics. Non-IATA-accredited agents typically sub-contract the air booking, which adds a hand-off point where things can go wrong.

## 3. Who Will Actually Handle My Pet?

Ask specifically: will your company handle my pet from door to door, or will any part of the journey be sub-contracted? If sub-contracted, to whom, and what is their accreditation status?

## 4. How Many Times Have You Done This Specific Route?

A UK-to-Australia specialist who has done 500 Australia moves is a better choice for that route than a general agent who has done it twice. Route-specific experience reduces the chance of documentation errors.

## 5. Which Veterinary Authority Do You Work With for Health Certificates?

A good agent should be able to name the Official Veterinarians or APHA-accredited vets they use for documentation. Agents who are vague here may be less experienced with government endorsement processes.

## 6. What Is Your Protocol If the Flight Is Delayed or Cancelled?

This is the critical question. What happens if your dog is in a crate in a transit facility and the onward flight is delayed 8 hours? A professional agent has a clear answer: access to partner facilities, 24-hour contacts, a backup plan.

## 7. What Does Your Quote Include, Exactly?

Get a line-by-line breakdown: crate (included?), government health certificate (included?), government endorsement fees (included?), collection and delivery (included?), quarantine fees if applicable (included?). Hidden costs in pet transport are common.

## 8. What Crate Will You Use and Can I See the Specification?

The agent should be able to specify the exact IATA crate size for your pet based on current measurements. "We'll sort the crate" is not an acceptable answer.

## 9. Do You Carry Professional Liability Insurance?

If the agent's error causes your pet to be held, mis-routed, or harmed, what recourse do you have? A professional operator carries insurance. Ask to see the certificate.

## 10. Do You Have References from This Route in the Last 12 Months?

Not general testimonials — specific references from people who have done the same or similar route recently. The regulations change. An agent who last moved a pet to your destination country two years ago may not be current.

---

*A specialist IPATA-member agent charges more than a budget option. For a non-trivial move involving quarantine, breed restrictions, or multiple connections, the cost is worth it.*

*Sources: IPATA Code of Ethics; IATA CEIV Live Animals certification programme. Data current as of May 2026.*""",
    },
    {
        "slug": "cat-import-rules-by-country-2026",
        "title": "Cat Import Rules by Country 2026: Quarantine, Vaccines, and Titre Tests at a Glance",
        "description": "A quick-reference guide to cat import requirements in 20 major destination countries. Which countries need titre tests, which have mandatory quarantine, and where the rules are changing.",
        "date": "2026-05-28",
        "tags": ["cats", "regulations", "planning"],
        "faqs": [
            ("Which countries require a titre test for cats?",
             "Australia, New Zealand, and Japan require rabies antibody titre tests for all cats. A small number of other countries (including Mauritius) also require titre tests. Most countries do not — a current rabies vaccination certificate is sufficient."),
            ("Which countries have mandatory quarantine for cats?",
             "Australia (10 days at Mickleham), New Zealand (minimum 10 days at Levin MPI), Mauritius (30 days), and a small number of Pacific island nations. Most countries do not require quarantine for cats from documented, vaccinated origins."),
            ("Do cats need a health certificate for EU travel from the UK?",
             "Yes. Post-Brexit, cats travelling from the UK to EU member states need an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel. The EU pet passport is no longer valid for UK-origin travel."),
        ],
        "body": """Cat import rules vary more than most owners expect. Before booking any international move, confirm the current requirements directly with the destination authority. This table summarises the rules as of May 2026 — but regulations change, so always verify.

## Quick Reference: Cat Import Requirements

| Country | Microchip | Rabies Vacc | Titre Test | Quarantine | Import Permit | Health Cert |
|---------|-----------|-------------|------------|------------|---------------|-------------|
| Australia | Yes | Yes | Yes (180-day wait) | 10 days | Via DAFF pre-export | Yes (govt endorsed) |
| New Zealand | Yes | Yes | Yes (180-day wait) | Min 10 days | Via MPI | Yes (govt endorsed) |
| Japan | Yes | Yes | Yes (180-day wait) | On arrival inspect | Pre-notification to MAFF | Yes |
| USA | Yes | Yes* | No | No | No | Yes (domestic) |
| Canada | Yes | Yes | No | No | No | Yes |
| UK (from EU) | Yes | Yes | No | No | No | AHC or health cert |
| EU (from UK) | Yes | Yes | No | No | No | AHC within 10 days |
| Germany | Yes | Yes | No | No | No | AHC |
| France | Yes | Yes | No | No | No | AHC |
| UAE | Yes | Yes | No | No | Yes (MoCCAE) | Yes |
| Singapore | Yes | Yes | No | Approved group: no | Yes (AVS) | Yes |
| Malaysia | Yes | Yes | No | No | Yes (DVS) | Yes |
| South Africa | Yes | Yes | No | No | No | Yes |
| Brazil | Yes | Yes | No | No | No (for personal pets) | MAPA format |
| Morocco | Yes | Yes | No | No | No | Yes (endorsed) |
| Mauritius | Yes | Yes | Yes | 30 days | Yes (MAIFS) | Yes |
| India | Yes | Yes | No | No | For personal pets: conditional | Yes |
| Kenya | Yes | Yes | No | Possible | Yes (DVS) | Yes |
| Israel | Yes | Yes | No | No | Yes (IZSV) | Yes |
| Spain | Yes | Yes | No | No | No | AHC (from UK) |

*USA: Cats do not currently require rabies vaccination for entry from most countries. However, this is subject to change — always check current CDC and destination state rules.*

## Three Countries to Plan Months Ahead

**Australia, New Zealand, and Japan** are the destinations requiring the most preparation. For all three:
1. ISO microchip must precede first vaccination
2. Rabies vaccination required
3. Blood sample sent to approved lab for titre test
4. 180-day wait after titre confirmation
5. Government health certificate and endorsement
6. Mandatory quarantine (AU/NZ) or inspection hold (Japan)

Start at least 8-9 months before your intended travel date for these three destinations.

---

*Sources: DAFF Australia; MPI New Zealand; MAFF Japan; European Commission; APHA UK; individual country government authority websites. Data current as of May 2026.*""",
    },
    {
        "slug": "pet-transport-indonesia-guide",
        "title": "Moving Pets to Indonesia: Jakarta Import Rules and the Quarantine Process",
        "description": "Indonesia pet import guide. The Ministry of Agriculture permit, quarantine requirements, breed restrictions, and what to expect at Soekarno-Hatta Airport in Jakarta.",
        "date": "2026-05-28",
        "tags": ["indonesia", "asia", "planning"],
        "faqs": [
            ("Is there quarantine for pets entering Indonesia?",
             "Yes. Indonesia requires a quarantine period for imported animals. The length varies by the animal's origin country and health status, but a minimum of 3 days is typically required with complete documentation. Animals from countries classified as rabies-present may face longer quarantine. Contact Indonesia's BKP (Balai Karantina Pertanian) for current requirements."),
            ("Do I need a permit to bring a pet into Indonesia?",
             "Yes. A recommendation letter from Indonesia's Ministry of Agriculture and an import declaration through BKP (Agricultural Quarantine Agency) are required before the animal travels. Apply at least 4-6 weeks before your planned travel date."),
            ("Which dog breeds are restricted in Indonesia?",
             "Indonesia has restrictions on several breeds under its animal welfare and public safety regulations. Pit Bull Terriers and related types face the strictest restrictions. Check with BKP for the current restricted breed list before booking."),
        ],
        "body": """Indonesia is home to a large expat community across Jakarta, Bali, and Surabaya. Pet import is managed through BKP (Badan Karantina Pertanian — Agricultural Quarantine Agency) and requires advance permit and quarantine.

## Pre-Travel Requirements

Before your pet travels to Indonesia:
1. Obtain a **recommendation letter from Indonesia's Ministry of Agriculture (Kementan)**
2. Submit documentation to **BKP** for pre-import clearance
3. Book quarantine space at a BKP-approved facility

Allow at least 4-6 weeks for the permit and clearance process.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| Ministry of Agriculture recommendation letter | Before travel |
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current (valid within period) |
| Full vaccination record | Distemper, parvo, hepatitis (dogs); FPV, respiratory (cats) |
| Rabies-free certificate or origin health status | Helps reduce quarantine duration |
| Health certificate | Issued within 14 days of travel, endorsed by government vet authority |
| External parasite treatment | Within 14 days of travel |

## Quarantine at Soekarno-Hatta

Animals arriving at Jakarta's Soekarno-Hatta Airport (CGK) are inspected and transferred to BKP's quarantine facility. Quarantine duration:
- Minimum 3 days for animals from lower-risk countries with full documentation
- Longer periods for animals from rabies-present countries

Contact BKP in advance to confirm the expected quarantine duration for your pet's origin country.

## Bali Arrivals

Bali operates through Ngurah Rai International Airport (DPS). BKP has a presence there, but the full quarantine facility is Jakarta-based. Pets arriving in Bali may be transferred to Jakarta for quarantine. Confirm the process with BKP before booking a Bali-direct flight for a pet.

## Cost Estimate (UK to Jakarta)

| Item | Estimated Cost |
|------|----------------|
| Government health certificate + APHA endorsement | £200-350 |
| BKP fees | Variable |
| Quarantine facility fees | Variable (estimate IDR 500,000-2,000,000+) |
| Airline cargo | £600-1,400 |
| **Total** | **~£900-2,100+** |

---

*Sources: Indonesia BKP (Badan Karantina Pertanian) official requirements; APHA UK export guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "moving-pets-to-france",
        "title": "Moving Pets to France: Animal Health Certificates, Breed Restrictions, and Paris Airport Process",
        "description": "France pet import guide for dogs and cats from the UK. Animal Health Certificate requirements post-Brexit, France's breed restrictions by category, and what to expect at CDG.",
        "date": "2026-05-30",
        "tags": ["france", "europe", "planning"],
        "faqs": [
            ("Can I use an EU pet passport to take my pet to France from the UK?",
             "No. Since Brexit, EU pet passports issued in the UK are no longer valid for travel from the UK to EU member states, including France. You need an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel."),
            ("Which dog breeds are restricted in France?",
             "France classifies dogs into Category 1 (attack dogs — import prohibited) and Category 2 (guard and defence dogs — registration and conditions required). Category 1 includes Pit Bull-type dogs and Boerboel. Category 2 includes Rottweilers, Tosa Inus, and American Staffordshire Terriers. Staffordshire Bull Terriers are not banned in France (unlike the UK's Dangerous Dogs Act groupings)."),
            ("Does France require a titre test for pets from the UK?",
             "No. France does not require a rabies titre test for pets from the UK arriving with valid rabies vaccination and AHC. The titre test requirement applies only to countries like Australia, Japan, and New Zealand."),
        ],
        "body": """France is the most popular destination for UK expats in continental Europe — and the post-Brexit documentation requirements are the main new hurdle. The process is clear once you know the steps.

## UK to France: The AHC Process

The **Animal Health Certificate (AHC)** has replaced the EU pet passport for UK-origin travel since 2021. Key points:
- Issued by an Official Veterinarian (OV) or an APHA-registered vet in the UK
- Must be completed within **10 days of travel**
- Valid for entry into France and onward travel within the EU for 4 months
- Required for **every trip** — one AHC per journey

Book your OV appointment in advance. APHA endorsement (for some routes and formats) takes 3-7 working days, though many modern AHC formats do not require separate APHA endorsement. Confirm with your OV.

## France's Breed Restriction Categories

France operates a two-category system:

| Category | Description | Conditions |
|----------|-------------|-----------|
| Category 1 | Attack dogs (Pit Bull-type, Boerboel) | Import prohibited. Cannot legally be kept in France. |
| Category 2 | Guard/defence dogs (Rottweiler, Tosa, Am. Staff) | Allowed but: owner permit required, neutering mandatory for some, muzzle and lead in public, owner must be over 18 and have no criminal record |

**Staffordshire Bull Terriers** are NOT in either category in France. They may be kept without restrictions. This differs from the UK's classification under the Dangerous Dogs Act.

## Entry at Charles de Gaulle or Orly

Pets entering France by air arrive through Charles de Gaulle (CDG) or Orly (ORY). Border inspection post veterinary staff carry out checks. Declare your pet on arrival. The AHC must be presented in its original form.

## Travelling by Eurostar or Ferry

Pets can travel by Eurostar from London St Pancras (cat and dog in carrier). Eurostar has specific pet policies — check current booking procedures. Ferry operators (P&O, DFDS, Brittany Ferries) allow pets on cabin-equipped routes. All routes require the same AHC documentation.

## Cost Estimate (UK to France)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | £150-250 |
| Airline cabin or cargo fee | £50-400 |
| **Total** | **~£200-650** |

---

*Sources: French Ministry of Agriculture (DGAL); European Commission Regulation 576/2013; APHA UK pet travel guidance. Data current as of May 2026.*""",
    },
    {
        "slug": "pets-in-extreme-heat-air-travel",
        "title": "Flying Pets in Extreme Heat: How Airlines Manage Summer Cargo Embargoes",
        "description": "Why airlines suspend live animal cargo in summer, which breeds are most affected, and how to plan pet travel around heat embargoes to keep your animal safe.",
        "date": "2026-05-30",
        "tags": ["airlines", "safety", "summer-travel"],
        "faqs": [
            ("At what temperature do airlines stop accepting live animal cargo?",
             "Most airlines apply a threshold of 26.7°C (80°F) to 29°C (85°F) at the origin or destination airport. Some airlines use a rolling 24-hour maximum rather than a spot reading. The temperature measured is ambient air temperature on the ground, not inside the cargo hold, which is separately climate-controlled."),
            ("Which breeds are most affected by summer cargo embargoes?",
             "Brachycephalic breeds (flat-faced dogs and cats — French Bulldogs, Pugs, Persians, English Bulldogs) are most restricted. Arctic breeds with thick double coats (Huskies, Malamutes, Samoyeds) are also commonly restricted in extreme summer heat. Short-coated breeds in good health face fewer restrictions but are still subject to the airline's general temperature limits."),
            ("Can I fly my pet in summer at all?",
             "Yes, with careful planning. Book early morning or late evening flights when ground temperatures are lower. Choose routes that avoid the hottest hub airports (e.g., Dubai in July). Select airlines known for temperature-controlled ground vehicles for live animals. For brachycephalic breeds, summer travel may simply not be possible — verify the airline's current policy before booking."),
        ],
        "body": """Every summer, thousands of pet owners discover that their airline cargo booking has been cancelled or suspended because temperatures at the origin or destination airport have exceeded the airline's live animal embargo threshold. This is not arbitrary — it exists because animals have died in cargo holds when ground-side handling in extreme heat has gone wrong.

Understanding how it works lets you plan around it.

## How Temperature Embargoes Work

Airlines set a maximum ambient air temperature — typically **26.7°C to 29°C** at origin or destination — above which they will not accept live animals in cargo. The threshold applies at the time of check-in and departure, not at booking.

What this means in practice:
- You can book in April for a July flight
- If July ground temperatures exceed the threshold on the day, the airline cancels the pet cargo
- The animal does not fly; you may lose part of your booking fee
- You need to rebook for when conditions allow

## The Hold vs. The Tarmac

The cargo hold of a modern airliner is pressurised and temperature-controlled during flight. The risk is not in the air — it's on the ground. A crate sitting in a holding area on a 35°C tarmac, or a cargo truck without adequate ventilation, exposes the animal to dangerous temperatures before and after flight.

Airlines that invest in temperature-controlled cargo vehicles and ramp facilities can operate more reliably in warm conditions. Research your chosen airline's specific ground facilities.

## Breeds Most Affected

**Brachycephalic dogs and cats:** British Airways, Qantas, Virgin Atlantic, and Singapore Airlines have year-round cargo bans on brachycephalic breeds. Other carriers apply seasonal restrictions. In summer, even normally-accepted brachycephalic breeds may face refusal.

**Arctic double-coat breeds:** Huskies, Alaskan Malamutes, Samoyeds, and similar thick-coated dogs overheat faster than short-coated breeds. Many airlines apply stricter temperature limits for them in summer.

**All large dogs:** Ground handling time is longer for large crates. More exposure to ambient conditions.

## Planning Around Embargoes

| Strategy | Detail |
|----------|--------|
| Travel in cooler months | October-March for most Northern Hemisphere routes |
| Book early morning departures | Ground temps 5-8°C lower at 06:00 vs. 14:00 |
| Avoid hot hub connections | Dubai (July-August), Doha, Houston in summer |
| Choose airlines with temp-controlled ground vehicles | Ask specifically; not all will confirm in writing |
| Get a backup plan in writing | What does the airline do if the embargo triggers on the day? |

## If Your Cargo Is Refused on the Day

The airline will typically hold the animal at the airport facility and rebook for the next available flight outside the embargo. In some cases you may be asked to collect the animal and rebook yourself. Have a plan: can you take the animal home if the flight is refused? Do you have a local contact who can collect if you are already travelling?

---

*Sources: IATA Live Animals Regulations; individual airline live animal policies. Data current as of May 2026.*""",
    },
    {
        "slug": "checking-vet-credentials-international-pet-travel",
        "title": "How to Check if Your Vet Is Accredited for International Pet Travel",
        "description": "Not every vet can sign an international health certificate. How to find an Official Veterinarian, what APHA accreditation means, and why using the wrong vet can invalidate your documents.",
        "date": "2026-06-01",
        "tags": ["planning", "health-certificates", "vets"],
        "faqs": [
            ("Can any vet sign an international health certificate?",
             "No. In the UK, international health certificates must be signed by an Official Veterinarian (OV) — a vet with specific APHA-approved training and certification. Using a regular vet who is not an OV will result in invalid documents that can be rejected at the destination. Always check OV credentials before booking the appointment."),
            ("How do I find an Official Veterinarian in the UK?",
             "The APHA (Animal and Plant Health Agency) maintains a register of Approved Veterinarians (AVs) and can direct you to Official Veterinarians in your area. You can also call your local APHA Animal Health and Welfare office. Many practices that advertise international pet travel paperwork will have an OV on staff."),
            ("What is the difference between an OV and an AV in the UK?",
             "An Official Veterinarian (OV) is a veterinarian who has completed APHA-approved training and can issue official health certificates on behalf of the government. An Approved Veterinarian (AV) is a vet approved to carry out certain animal health tasks but with a more limited scope. For international travel health certificates, you typically need an OV."),
        ],
        "body": """It seems like a simple step: take your pet to the vet, get a health certificate, travel. But international health certificates are legal government documents. They must be signed by a vet with the specific authority to issue them, and they must follow the correct format for the destination country.

Using the wrong vet for this step can result in invalid documents — discovered when you arrive at the border.

## In the UK: You Need an Official Veterinarian (OV)

The UK's official government body for animal health is **APHA** (Animal and Plant Health Agency). For most international journeys from the UK, the health certificate must be signed by an **Official Veterinarian (OV)** — a vet who has completed APHA-approved training (typically a Level 3 Award in Official Controls and an Animal Health Official Controls course).

OVs have a certificate number issued by APHA. The certificate number appears on official documents.

**How to find one:**
- Ask your regular vet if they have an OV on staff
- Search the APHA Vet Gateway portal (gov.uk)
- Call your regional APHA Animal Health and Welfare office
- Ask the pet transport agent you're working with (most have OV relationships)

## In the USA: USDA-Accredited Veterinarian

In the USA, health certificates for international travel must be signed by a **USDA-Accredited Veterinarian** and in many cases then endorsed by USDA APHIS. An accredited vet has completed USDA training and is listed in the APHIS registry.

After the vet signs, USDA APHIS must endorse the certificate — this is a separate step that takes 3-5 business days.

Find an accredited vet through the USDA APHIS Vet Search tool at aphis.usda.gov.

## In the EU: Official Veterinarian

EU member states use Official Veterinarians (OVs) equivalent to the UK system. The OV must sign the EU health certificate form. Your national competent authority can direct you to registered OVs in your area.

## What to Bring to the OV Appointment

| Item | Why |
|------|-----|
| Microchip scan record | OV must confirm microchip number matches documents |
| Vaccination records (original) | Dates, batch numbers, manufacturer, validity period |
| Titre test certificate (if required) | Original lab certificate |
| Import permit from destination country (if required) | OV may need to reference permit number |
| Destination country health certificate format | Some OVs ask you to supply the destination-specific form |

## Timing: Book Early

OV appointment availability varies. In busy periods (Christmas, summer holidays), slots book up weeks in advance. Government endorsement adds further time. Book the OV appointment **before** you book your flight.

---

*Sources: APHA Official Veterinarian training and certification requirements; USDA APHIS Accredited Veterinarian programme. Data current as of May 2026.*""",
    },
    {
        "slug": "moving-pets-to-netherlands",
        "title": "Moving Pets to the Netherlands: EU Import Rules, Breed Bans, and Schiphol Airport",
        "description": "Netherlands pet import guide for UK owners. Animal Health Certificate requirements, the Dutch breed ban list, and what to expect for cargo and cabin arrivals at Amsterdam Schiphol.",
        "date": "2026-06-01",
        "tags": ["netherlands", "europe", "planning"],
        "faqs": [
            ("Does the Netherlands ban any dog breeds?",
             "The Netherlands lifted its national Pit Bull ban in 2008. However, individual municipalities may still have restrictions. The Netherlands currently has no national breed-specific legislation, but dogs that are assessed as dangerous on an individual basis can be subject to restrictions. Check current municipal rules in your specific destination area."),
            ("What do I need to bring a dog from the UK to the Netherlands?",
             "An ISO-microchipped dog with a current rabies vaccination and an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel. Same as all UK-to-EU pet travel post-Brexit."),
            ("Is there quarantine for pets entering the Netherlands?",
             "No. The Netherlands does not require quarantine for pets arriving from most countries with correct documentation."),
        ],
        "body": """The Netherlands is a common destination for UK expats and international professionals, particularly in the Amsterdam and The Hague areas. Pet import is governed by EU Regulation 576/2013, making it one of the more streamlined EU destinations.

## UK to Netherlands: AHC Requirement

Post-Brexit, all UK pets travelling to the Netherlands need an **Animal Health Certificate (AHC)** issued by an Official Veterinarian within 10 days of travel. The EU pet passport is no longer valid for UK-origin journeys.

The AHC is valid for the entry journey and for 4 months of travel within the EU thereafter.

## Documentation Summary

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Current rabies vaccination | Yes |
| Animal Health Certificate (AHC) | Yes — OV-issued within 10 days |
| EU pet passport | Not required (UK-issued are not valid) |

## Netherlands Breed Legislation

The Netherlands abolished its national Pit Bull ban in 2008, making it one of the few EU countries with **no national breed-specific legislation**. The Dutch approach is behaviour-based: a dog is assessed individually if there is evidence of dangerous behaviour.

However, some municipalities in the Netherlands have retained local restrictions. Check with the local municipality (gemeente) in your area before assuming all breeds are unrestricted. Amsterdam and Rotterdam do not currently enforce breed bans, but smaller municipalities vary.

## KLM and Amsterdam Schiphol for Pet Transport

Schiphol Airport (AMS) is one of Europe's best-equipped airports for live animal handling. KLM's cargo programme (KLM Cargo / Martinair Cargo) is widely regarded as a quality option for pet transport within Europe and intercontinentally. KLM accepts pets in cabin (small animals under 8 kg in carrier) and as cargo.

Schiphol's live animal centre handles dogs, cats, and other species. Pre-notification is required for all cargo shipments.

## Cost Estimate (UK to Netherlands)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | £150-250 |
| Airline cargo or cabin fee | £50-400 |
| **Total** | **~£200-650** |

---

*Sources: EU Regulation 576/2013; APHA UK pet travel guidance; Dutch Ministry of Agriculture, Nature and Food Quality (LNV). Data current as of May 2026.*""",
    },
]


def slug_exists(slug: str) -> bool:
    return os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md"))


def write_article(article: dict) -> bool:
    slug = article["slug"]
    if slug_exists(slug):
        return False

    path = os.path.join(BLOG_DIR, f"{slug}.md")

    tag_lines = "\n".join(f'  - "{t}"' for t in article["tags"])
    faq_lines = "\n".join(
        f'  - question: "{q.replace(chr(34), chr(39))}"\n    answer: "{a.replace(chr(34), chr(39))}"'
        for q, a in article["faqs"]
    )

    content = f"""---
title: "{article['title']}"
description: "{article['description']}"
date: "{article['date']}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{article['title']} | PetTransportGlobal"
  description: "{article['description']}"
tags:
{tag_lines}
faqs:
{faq_lines}
---

{article['body'].strip()}
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


if __name__ == "__main__":
    os.makedirs(BLOG_DIR, exist_ok=True)
    written = 0
    skipped = 0
    for article in ARTICLES:
        if write_article(article):
            written += 1
            print(f"  Written: {article['slug']}")
        else:
            skipped += 1
            print(f"  Skipped (exists): {article['slug']}")
    print(f"\nDone. Written: {written} | Skipped: {skipped}")
