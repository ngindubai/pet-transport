# -*- coding: utf-8 -*-
"""generate_blog_batch14.py -- Blog batch 14 (28 articles).
Country guides: Poland, Saudi Arabia, Japan, Mexico, Costa Rica, Morocco, Jordan.
Route guides: USA-UAE, UK-Morocco, EU-USA, Canada-UK, Ireland-AU, Australia-UAE,
Germany-Singapore, UK-Kenya.
Breed guides: Greyhound, Whippet, Doberman, Vizsla, Weimaraner.
Practical: importing a puppy, flying with two dogs, moving to Costa Rica,
moving to Mexico, moving to Singapore, health cert vs pet passport,
how long does pet transport take, which airlines accept large dogs.
"""

import os

BLOG_DIR = os.path.join("site", "content", "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    # ------------------------------------------------------------------ #
    # COUNTRY IMPORT GUIDES                                                #
    # ------------------------------------------------------------------ #
    {
        "slug": "poland-pet-import-guide",
        "title": "Poland Pet Import Guide 2026",
        "description": "Bringing a dog or cat to Poland explained. EU Pet Travel Scheme rules, AHC requirements for UK pet owners, titre test timelines, and microchip standards.",
        "date": "2026-05-08",
        "tags": ["poland", "eu pet travel", "dog import", "cat import", "microchip"],
        "faqs": [
            {
                "question": "What documents do I need to bring my pet to Poland?",
                "answer": "Poland is an EU member and follows the EU Pet Travel Scheme. Your pet needs an ISO 15444 microchip implanted before vaccination, a current rabies vaccination record, and either a valid EU pet passport (for EU-resident pets) or an official Animal Health Certificate endorsed by your national veterinary authority. From the UK, the AHC must be endorsed by APHA. From the USA, endorsement is via USDA APHIS."
            },
            {
                "question": "Does Poland require a rabies titre test?",
                "answer": "A titre test is required for pets arriving from countries outside the EU that are not on the EU approved list. This includes pets from the USA, Canada, Australia, and most non-EU countries. The test must show at least 0.5 IU/ml and must be conducted at least 30 days after vaccination, with the pet not travelling for at least three months after the blood sample was taken."
            },
            {
                "question": "Can I bring my dog to Poland from the UK after Brexit?",
                "answer": "Yes. UK pets need an Animal Health Certificate endorsed by APHA rather than an EU pet passport. The AHC is valid for 10 days from the vet examination date. Book the vet examination and APHA endorsement slot at least two weeks before travel. A titre test is not required for UK pets entering Poland since the UK maintains approved status under EU Regulation 576/2013."
            }
        ],
        "body": """Poland is a popular destination for expats and returning nationals, and each year a steady number of pets travel here from the UK, USA, Germany, and beyond. As an EU member state, Poland applies the EU Pet Travel Scheme, so the paperwork will feel familiar if you have moved pets within Europe before.

## Core requirements for pet entry to Poland

Your pet needs an ISO 15444 microchip implanted before any rabies vaccination is given. The microchip number links everything: the vaccination record, the health certificate, and any titre test results. The microchip number must match exactly across all documents.

Rabies vaccination must be current. If a booster has lapsed, your vet will need to restart the vaccination course, which resets the titre test clock if a titre test is required.

Pets arriving from outside the EU need an official health certificate completed by an accredited veterinarian and endorsed by the national competent authority: APHA in the UK, USDA APHIS in the USA, CFIA in Canada, and DAFF in Australia.

## UK pets entering Poland

Since Brexit, UK-issued EU pet passports are not valid for EU entry. You need an AHC issued by a listed vet in the UK. APHA endorses the certificate, usually within three to five working days. The AHC is only valid for 10 days, so plan the timing carefully around your flight.

The good news: the UK maintains an approved third-country status under EU rules, meaning UK pets do not need a titre test to enter Poland or any other EU country. Microchip, current rabies vaccination, and endorsed AHC are sufficient.

## Arriving by air or road

Major entry points include Warsaw Chopin Airport (WAW) and Gdansk Airport (GDN). Pets arriving as air cargo will pass through a Border Inspection Post (BIP). Your freight forwarder or airline cargo agent will handle the TRACES notification on arrival.

If you are driving to Poland through Germany, you will cross through Schengen territory. EU pet passports are accepted throughout. UK pets entering the Schengen zone first (e.g. via the Channel Tunnel to France) need only one endorsed AHC for the entire journey.

## Registering your pet in Poland

Poland does not have a single mandatory national pet registry, but many municipalities encourage registration and microchip registration with a vet practice database. Check with your local gmina (district administration) after arrival.

**Official sources:**
- EU Pet Travel Scheme: European Commission, DG SANTE
- APHA pet export information: GOV.UK/APHA
- Polish Chief Veterinary Inspectorate: wetgiw.gov.pl
"""
    },
    {
        "slug": "saudi-arabia-pet-import-guide",
        "title": "Saudi Arabia Pet Import Guide 2026",
        "description": "How to bring your dog or cat to Saudi Arabia. MEWA import permit, health certificate rules, breed restrictions, and what to expect at Riyadh or Jeddah airports.",
        "date": "2026-05-08",
        "tags": ["saudi arabia", "MEWA", "pet import", "dog import", "riyadh"],
        "faqs": [
            {
                "question": "Can I bring a dog to Saudi Arabia?",
                "answer": "Yes, you can bring a dog to Saudi Arabia, though the process involves more steps than many Western countries. An import permit from the Ministry of Environment, Water and Agriculture (MEWA) is required. Dogs must be microchipped, vaccinated against rabies and other core diseases, and accompanied by an endorsed health certificate. Some breeds face restrictions. Guard dogs and pets accompanying expatriates are the most common categories."
            },
            {
                "question": "What vaccinations does my pet need for Saudi Arabia?",
                "answer": "Saudi Arabia requires dogs and cats to be vaccinated against rabies (current and valid), and typically also against distemper, parvovirus, and hepatitis for dogs, and feline calicivirus, rhinotracheitis, and panleukopenia for cats. All vaccinations must be recorded on the health certificate, which must be issued within 10 days of travel and endorsed by your national veterinary authority."
            },
            {
                "question": "Are there breed restrictions for dogs in Saudi Arabia?",
                "answer": "Saudi Arabia restricts the import of certain breeds considered dangerous. The list has historically included Pit Bull Terrier types, Rottweilers, and other large guard breeds. Some breeds require special permits. Check with MEWA or the Saudi Embassy in your country before booking travel, as the approved breed list can change and some breeds may be refused entry."
            }
        ],
        "body": """Saudi Arabia has a large and growing expatriate community, and more families than ever are choosing to bring their pets when relocating for work. The process is more involved than many destinations, but it is absolutely achievable with the right preparation.

## The MEWA import permit

All dogs and cats entering Saudi Arabia require an import permit from the Ministry of Environment, Water and Agriculture (MEWA). You apply for this permit before travel, usually through the Saudi Embassy or consulate in your country, or through a licensed pet transport agent.

The permit application typically requires your pet's microchip number, vaccination records, and a copy of the health certificate. Allow four to six weeks for processing. The permit specifies the entry port, so make sure your flight route matches.

## Health certificate requirements

The health certificate must be:
- Issued by a government-accredited veterinarian within 10 days of your travel date
- Endorsed by your national veterinary authority (USDA APHIS for USA, APHA for UK, CFIA for Canada, DAFF for Australia)
- Stamped by the Saudi Embassy or consulate in your country (in some cases)

Rabies vaccination is mandatory and must be current. Most Saudi entry requirements also specify core disease vaccinations beyond rabies. Your vet should be familiar with the Saudi requirements, or your pet transport agent can provide the specific vaccination list.

## Travelling with a dog in Saudi Arabia

Saudi Arabia is a conservative country and attitudes toward dogs vary. Some residential compounds and family-friendly areas are very accommodating, while public spaces typically do not allow dogs. Many expats keep dogs within compound boundaries.

It is worth researching your specific area and employer's compound before arrival to understand what facilities and spaces will be available for your pet.

## Cats in Saudi Arabia

Cats are more widely accepted in Saudi culture than dogs, and many expats keep cats without difficulty. The import process for cats follows the same MEWA permit and health certificate pathway, though the breed restriction list is shorter.

## Arriving at Riyadh (RUH) or Jeddah (JED)

Most pet imports arrive at King Khalid International Airport in Riyadh or King Abdulaziz International Airport in Jeddah. On arrival, your pet will be inspected by a Saudi Agricultural Quarantine Authority officer. If all documents are in order, your pet will be released. If documentation is incomplete, your pet may be held until it is resolved.

Use a reputable pet freight forwarder who has experience handling Saudi arrivals. They can coordinate with the airport cargo facility and ensure the MEWA permit is correctly presented.

**Official sources:**
- MEWA Saudi Arabia: mewa.gov.sa
- USDA APHIS international pet travel: aphis.usda.gov
- APHA UK pet export: GOV.UK/APHA
"""
    },
    {
        "slug": "japan-pet-import-guide",
        "title": "Japan Pet Import Guide 2026",
        "description": "Everything you need to know about bringing a dog or cat to Japan. MAFF quarantine rules, titre test timelines, rabies-free status, and how to avoid long detention periods.",
        "date": "2026-05-08",
        "tags": ["japan", "MAFF", "pet quarantine", "rabies-free", "dog import"],
        "faqs": [
            {
                "question": "How long is quarantine for pets entering Japan?",
                "answer": "Japan is rabies-free and has strict quarantine rules to stay that way. If all required preparations are completed correctly and in the right order, quarantine at an approved facility can be as short as 12 hours. However, if any step is out of sequence or incomplete, quarantine can extend to 180 days. The Ministry of Agriculture, Forestry and Fisheries (MAFF) controls the process. Most owners who follow the steps precisely experience only the 12-hour hold."
            },
            {
                "question": "What is required to bring a dog to Japan?",
                "answer": "Japan's requirements are: ISO 15444 microchip; two rabies vaccinations given after microchipping with the correct interval; a rabies titre test (FAVN or ELISA) at a MAFF-approved laboratory showing at least 0.5 IU/ml; a waiting period of at least 180 days after the titre test blood draw before the pet can arrive in Japan; official health certificate; and pre-arrival notification to MAFF at least 40 days before the scheduled arrival."
            },
            {
                "question": "What is the 180-day rule for Japan?",
                "answer": "After your pet's blood sample is taken for the titre test, the animal must wait at least 180 days before it can enter Japan. This waiting period begins from the date the blood was drawn (not from when results are received). If your pet arrives before the 180 days have elapsed, it will be held in quarantine for the remaining days, entirely at your expense. This is the most important timeline rule in the entire Japan process."
            }
        ],
        "body": """Japan is one of the strictest destinations in the world for pet imports, and for good reason: it is rabies-free and intends to stay that way. The process is not hard, but the timing is unforgiving. Get the sequence right and your pet will clear quarantine in 12 hours. Get anything out of order and the cost can be substantial.

## Why Japan's rules are so strict

Japan has been rabies-free since 1956. Every aspect of the import process is designed to prevent rabies being reintroduced through an imported animal. The Ministry of Agriculture, Forestry and Fisheries (MAFF) enforces these rules rigorously.

The 180-day waiting period after the titre test blood draw is the cornerstone of the system. During this time, MAFF is confident that any animal exposed to rabies before the blood draw would have shown signs by the time it arrives.

## The correct sequence

This sequence cannot be altered. Every step must happen in the right order:

1. Microchip implanted (ISO 15444)
2. Two rabies vaccinations given after the microchip, with the correct interval between them (21 days minimum between first and second vaccination)
3. Blood sample taken at least 30 days after the second vaccination
4. Blood sent to a MAFF-approved laboratory for FAVN or ELISA titre test
5. Titre test result of at least 0.5 IU/ml confirmed
6. Wait at least 180 days from the blood draw date
7. Submit pre-arrival notification to MAFF at least 40 days before the arrival date
8. Arrive in Japan at an approved entry point with all documentation

If your pet's vaccinations lapse and need to be restarted, the entire sequence resets from step 1.

## Health certificate

An official health certificate endorsed by your national authority (USDA APHIS, APHA, CFIA, DAFF) is required. The certificate must reference the titre test results and confirm the microchip number. MAFF provides specific health certificate forms on its website.

## Arriving in Japan

Tokyo (NRT Narita or HND Haneda), Osaka (KIX Kansai), and a small number of other airports are approved entry points. Not all airports can handle incoming animals, so check MAFF's approved entry port list before booking flights.

On arrival, your pet will be inspected at the MAFF quarantine station. If the 180-day waiting period has been met and all documentation is in order, the minimum hold is 12 hours. You can visit your pet during this time at some facilities.

## Costs

The MAFF quarantine facility charges a daily fee. For a 12-hour stay, costs are minimal. For longer stays due to paperwork issues or timing errors, costs escalate quickly. Budget for several hundred to several thousand USD if complications arise.

**Official sources:**
- MAFF Japan pet import: maff.go.jp
- MAFF approved titre test laboratories: maff.go.jp
- Pre-arrival notification forms: maff.go.jp/aqs
"""
    },
    {
        "slug": "mexico-pet-import-guide",
        "title": "Mexico Pet Import Guide 2026",
        "description": "How to bring your dog or cat to Mexico. SENASICA health certificate rules, vaccination requirements, and what to expect at Mexico City or Cancun airports.",
        "date": "2026-05-08",
        "tags": ["mexico", "SENASICA", "pet import", "dog import", "cat import"],
        "faqs": [
            {
                "question": "What does Mexico require to import a dog?",
                "answer": "Mexico requires a health certificate issued within 10 days of travel by a licensed veterinarian. The certificate must confirm that your dog is free of signs of infectious or contagious disease, has been vaccinated against rabies (current), and is free of external parasites. An ISO microchip is not legally mandated by Mexico for entry but is strongly recommended for identification. SENASICA officers inspect the health certificate on arrival."
            },
            {
                "question": "Do I need a titre test to bring my pet to Mexico?",
                "answer": "No. Mexico does not currently require a rabies titre test for pet imports, which makes it significantly simpler than destinations like Japan, Australia, New Zealand, or Singapore. A current rabies vaccination record on the health certificate is sufficient. However, requirements can change, so always check with the Mexican Consulate or SENASICA before travel."
            },
            {
                "question": "Can I bring my cat to Mexico without quarantine?",
                "answer": "Yes. Mexico does not impose routine quarantine on dogs or cats with valid health certificates and current vaccinations. Pets are inspected by SENASICA on arrival at the airport. If the health certificate is valid and the animal appears healthy, your pet will be cleared and released. Inspect fees are low, typically USD 5 to 30 per animal."
            }
        ],
        "body": """Mexico is one of the more straightforward countries for pet import, which is great news if you are relocating for work or retiring to destinations like Mexico City, Puerto Vallarta, or the Yucatan Peninsula.

## What Mexico actually requires

Mexico's pet import rules are administered by SENASICA (the National Service of Agro-Food Health, Safety and Quality). The core requirement is a health certificate issued by a licensed veterinarian within 10 days of your travel date.

The health certificate must state:
- Your pet's species, breed, age, sex, and microchip or tattoo number
- That the animal shows no clinical signs of infectious or contagious disease
- That the animal is free of external parasites (fleas, ticks, mites)
- Current rabies vaccination with product name, batch number, and expiry date
- Other vaccinations as appropriate (distemper, parvovirus, etc. for dogs; feline viral rhinotracheitis, panleukopenia for cats)

The health certificate does not need to be endorsed by a government authority for most origin countries, though USDA APHIS endorsement is accepted and can smooth the process.

## Arriving in Mexico

SENASICA inspection desks are in place at major international airports including Mexico City Benito Juarez (MEX), Cancun (CUN), and Guadalajara (GDL). In practice, the inspection is usually brief. Present your health certificate and vaccination record. SENASICA may charge a small inspection fee.

Pets travelling in cabin count as carry-on and must stay in an approved carrier under the seat. Pets travelling as checked baggage or cargo follow the airline's specific procedures.

## Living with your pet in Mexico

Once settled, you will want to register your pet with a local vet and consider annual boosters for diseases such as leptospirosis, which can be more prevalent in some Mexican regions. Your vet can advise on local health risks.

Mexico City and other urban areas have active pet communities, dog parks, and strong veterinary infrastructure. Coastal resort areas also have established expat pet communities with access to international-standard vet care.

**Official sources:**
- SENASICA Mexico: gob.mx/senasica
- USDA APHIS Mexico pet entry information: aphis.usda.gov
"""
    },
    {
        "slug": "costa-rica-pet-import-guide",
        "title": "Costa Rica Pet Import Guide 2026",
        "description": "Bringing a dog or cat to Costa Rica. SENASA permit requirements, health certificate rules, vaccination checklist, and practical tips for arriving at San Jose airport.",
        "date": "2026-05-08",
        "tags": ["costa rica", "SENASA", "pet import", "dog import", "san jose"],
        "faqs": [
            {
                "question": "What does Costa Rica require to import a dog?",
                "answer": "Costa Rica requires: a zoo sanitary import permit issued by SENASA (Servicio Nacional de Salud Animal) before travel; a health certificate issued within 15 days of travel by an accredited vet; vaccinations against rabies, distemper, parvovirus, and hepatitis for dogs (and equivalent feline vaccines for cats); and treatment against internal and external parasites applied within 30 days before travel. The permit application is submitted online via SENASA's portal."
            },
            {
                "question": "How do I get a SENASA import permit for my pet?",
                "answer": "Apply online through the SENASA online services portal (senasa.go.cr). You will need your pet's microchip number, vaccination records, and basic owner information. The permit is typically issued within a few days to two weeks. Print the permit and carry it with you to the airport. Without the permit, your pet may be refused entry or held at your expense."
            },
            {
                "question": "Is there quarantine for pets arriving in Costa Rica?",
                "answer": "Costa Rica does not impose routine quarantine for pets arriving with valid permits and documentation. SENASA officers inspect arriving animals at Juan Santamaria International Airport (SJO). If all paperwork is in order and the animal appears healthy, your pet will be cleared on arrival. Ensure your parasite treatment records are current, as this is a common reason for delays."
            }
        ],
        "body": """Costa Rica is a magnet for expats, retirees, and remote workers, and the country has a well-established system for welcoming pets. The key steps are getting the SENASA permit sorted in advance and making sure your vet completes the health certificate correctly.

## The SENASA permit

You cannot bring a dog or cat to Costa Rica without an advance import permit from SENASA. Apply through the SENASA online portal at senasa.go.cr. The application asks for your pet's details, vaccination history, and travel dates. Allow at least two to three weeks for the permit to be issued, though in practice approvals often come through more quickly.

Keep the permit number and print a copy to carry with your pet on travel day. Airlines handling your pet as cargo will also need the permit reference number.

## Health certificate requirements

The health certificate must be issued within 15 days of your travel date. Your vet should confirm:
- Microchip number (ISO 15444 recommended, though Costa Rica does not strictly mandate this format)
- Rabies vaccination current and valid
- Distemper, parvovirus, and hepatitis vaccinations for dogs
- Feline calicivirus, rhinotracheitis, and panleukopenia for cats
- Treatment against internal and external parasites within the last 30 days

Most Costa Rican consulates recommend (but do not strictly require) USDA APHIS or equivalent endorsement on the health certificate. If you are travelling from the USA, APHIS endorsement can prevent any ambiguity on arrival.

## Arriving at San Jose

Most international pets arrive at Juan Santamaria International Airport (SJO) in Alajuela, just outside San Jose. SENASA has an inspection office at the airport. The inspection is usually straightforward: your documentation will be checked, the microchip verified, and a brief physical inspection conducted.

San Jose also receives some international flights at Daniel Oduber Quiros International Airport (LIR) in Liberia, which serves the Guanacaste region.

## Life with your pet in Costa Rica

Costa Rica has a warm, dog-friendly culture in many areas. The country has a large stray dog population, which means vaccination against leptospirosis and other locally prevalent diseases is strongly advised. Your local vet in Costa Rica will give you a regional vaccination and parasite protocol.

**Official sources:**
- SENASA Costa Rica: senasa.go.cr
- USDA APHIS international pet travel: aphis.usda.gov
"""
    },
    {
        "slug": "morocco-pet-import-guide",
        "title": "Morocco Pet Import Guide 2026",
        "description": "Bringing a dog or cat to Morocco. ONSSA health certificate requirements, rabies vaccination rules, breed restrictions, and what happens at Casablanca or Marrakech airports.",
        "date": "2026-05-08",
        "tags": ["morocco", "ONSSA", "pet import", "dog import", "casablanca"],
        "faqs": [
            {
                "question": "What documents does Morocco require for pet import?",
                "answer": "Morocco requires a health certificate issued by an official or accredited veterinarian within five days of departure, endorsed by your national veterinary authority. The certificate must confirm current rabies vaccination, absence of disease symptoms, and microchip details. The National Office for Food Safety (ONSSA) inspects incoming pets at Border Inspection Posts. A zoo sanitary import certificate may also be required from ONSSA in advance for some species."
            },
            {
                "question": "Does Morocco require a rabies titre test for pet entry?",
                "answer": "Morocco does not currently require a rabies titre test as a standard condition of entry for dogs and cats from most countries. A current rabies vaccination is the primary requirement. However, this can change and some origin countries may face additional scrutiny. Always verify with the Moroccan Embassy or ONSSA before travel."
            },
            {
                "question": "Are dogs welcome in Morocco?",
                "answer": "Cultural attitudes toward dogs vary in Morocco. In urban areas such as Casablanca and Marrakech, pet dogs are increasingly common and there are vets, pet shops, and dog-friendly parks. Rural areas and traditional medina neighbourhoods are less accommodating. Cats are very widely accepted throughout the country. Expat communities in coastal cities like Agadir and Essaouira are generally very pet-friendly."
            }
        ],
        "body": """Morocco attracts a growing number of expats and retirees, particularly from France, Spain, and the UK. It is also a popular destination for digital nomads. Bringing your pet to Morocco is achievable, though the process is less well-documented than in EU countries, and it pays to be thorough.

## ONSSA and the health certificate

Morocco's food and animal safety authority, ONSSA (Office National de Securite Sanitaire des Produits Alimentaires), oversees pet imports. The health certificate is the cornerstone of the process.

Your health certificate must be:
- Issued by an official or accredited veterinarian
- Endorsed by your national authority (USDA APHIS, APHA, CFIA, DAFF)
- Issued within five days of your departure date (shorter window than most countries)
- Confirming current rabies vaccination, microchip number, and absence of signs of disease

The five-day window is the main practical challenge. Book your vet appointment and authority endorsement slot carefully to ensure the certificate is dated correctly.

## Arriving in Morocco

Border Inspection Posts at Casablanca Mohammed V International Airport (CMN), Marrakech Menara Airport (RAK), and key ferry ports (Tangier, Ceuta crossings) handle incoming pets. ONSSA officers will inspect your documentation and physically check your pet.

If you are travelling by ferry from Spain or France, the rules are the same: health certificate, microchip, rabies vaccination. Pets in vehicles on the ferry typically remain in the vehicle during crossing.

## Breed restrictions

Morocco has restrictions on the import of certain breeds including Pit Bull Terrier types and Rottweilers, mirroring restrictions in many other countries. Check with the Moroccan Embassy or ONSSA for the current list before travel.

## Daily life with a pet in Morocco

Veterinary care in major cities is good and improving. Casablanca, Rabat, and Marrakech all have well-equipped vet clinics used by both locals and expats. Some areas outside cities have limited vet access, so factor this into your choice of location.

**Official sources:**
- ONSSA Morocco: onssa.gov.ma
- APHA UK pet export: GOV.UK/APHA
- USDA APHIS Morocco: aphis.usda.gov
"""
    },
    {
        "slug": "jordan-pet-import-guide",
        "title": "Jordan Pet Import Guide 2026",
        "description": "How to bring a dog or cat to Jordan. Ministry of Agriculture requirements, health certificate rules, breed restrictions, and arrival procedures at Amman airport.",
        "date": "2026-05-08",
        "tags": ["jordan", "amman", "pet import", "dog import", "middle east"],
        "faqs": [
            {
                "question": "Can I bring my dog to Jordan?",
                "answer": "Yes, you can import a dog to Jordan, though the process requires advance preparation. You need a health certificate issued within 10 days of travel and endorsed by your national veterinary authority, current rabies vaccination, microchip, and approval from Jordan's Ministry of Agriculture. Some breeds face import restrictions. Pet dogs are common in expat communities in Amman and other cities."
            },
            {
                "question": "What vaccinations are required for pet import to Jordan?",
                "answer": "Jordan requires current rabies vaccination for all dogs and cats. Dogs typically also need vaccination against distemper, parvovirus, and hepatitis. The health certificate must list all vaccinations with product names, batch numbers, and expiry dates. The certificate must be issued within 10 days of travel and endorsed by your national veterinary authority."
            },
            {
                "question": "Is there quarantine for pets arriving in Jordan?",
                "answer": "Jordan does not impose routine quarantine for pets arriving with valid documentation and satisfactory health certificates. Arrival inspection is carried out by Ministry of Agriculture veterinary officers at Queen Alia International Airport (AMM). If documentation is complete and the animal appears healthy, clearance is usually straightforward. Incomplete paperwork can result in detention."
            }
        ],
        "body": """Jordan is home to a large expatriate community, particularly in Amman, drawn by work in international organisations, diplomacy, and business. Many expats bring their pets and navigate the process successfully each year.

## What Jordan requires

Jordan's Ministry of Agriculture oversees pet imports. The documentation requirements are similar to many Middle Eastern countries:

- ISO microchip (recommended, increasingly required)
- Current rabies vaccination (valid and not expired)
- Core disease vaccinations for dogs: distemper, parvovirus, hepatitis
- Health certificate issued within 10 days of travel by an accredited vet
- Health certificate endorsed by your national veterinary authority (USDA APHIS, APHA, CFIA, etc.)
- Ministry of Agriculture approval for import (coordinate via your airline or a pet freight forwarder)

## Arriving at Amman

Queen Alia International Airport (AMM) is the main entry point for international pets. Veterinary officers from the Ministry of Agriculture inspect incoming animals. Most airlines operating pet cargo services to Amman, including Royal Jordanian, British Airways, Lufthansa, and Emirates, have experience handling the Jordanian import process.

If you use a specialist pet freight forwarder, they will typically coordinate the inspection and customs clearance on your behalf.

## Breed restrictions

Jordan restricts or regulates some breeds considered dangerous. Pit Bull Terrier types are the most commonly restricted. Check with the Jordanian Embassy or Ministry of Agriculture before travel if you have a breed that might fall into this category.

## Living with a pet in Amman

Amman has a growing number of pet-friendly spaces, vet clinics, and pet supply shops. The expatriate community is well-connected and a good source of local knowledge on vets, groomers, and pet-friendly parks.

**Official sources:**
- Jordan Ministry of Agriculture: moa.gov.jo
- USDA APHIS Jordan information: aphis.usda.gov
- APHA UK pet export: GOV.UK/APHA
"""
    },

    # ------------------------------------------------------------------ #
    # ROUTE GUIDES                                                         #
    # ------------------------------------------------------------------ #
    {
        "slug": "usa-to-uae-pet-transport-guide",
        "title": "Pet Transport from USA to UAE 2026",
        "description": "How to transport your dog or cat from the USA to the United Arab Emirates. MOCCAE permit, USDA APHIS health certificate, breed restrictions, and airline options.",
        "date": "2026-05-08",
        "tags": ["usa to uae", "pet transport", "dubai", "abu dhabi", "MOCCAE"],
        "faqs": [
            {
                "question": "What documents do I need to send my pet from the USA to the UAE?",
                "answer": "You need: a USDA APHIS-endorsed health certificate issued within 10 days of travel; current rabies vaccination; additional core vaccinations; an import permit from the Ministry of Climate Change and Environment (MOCCAE); and in some cases an endorsement from the UAE Embassy in Washington. Work with a specialist pet freight forwarder who knows the UAE import process, as requirements can be updated."
            },
            {
                "question": "Are there breed restrictions for dogs entering the UAE?",
                "answer": "Yes. The UAE maintains a list of restricted dog breeds including Pit Bull Terrier, American Staffordshire Terrier, Rottweiler, Doberman, Chow Chow, Akita, and several others. These breeds cannot be imported as pets. Airlines also apply their own restrictions on top of government rules, so confirm both before booking. Non-restricted breeds travel without issue."
            },
            {
                "question": "Which airlines fly pets from the USA to the UAE?",
                "answer": "Emirates SkyCargo operates a dedicated pet cargo service from major US cities to Dubai (DXB). Etihad Airways also accepts pets as cargo to Abu Dhabi (AUH). Qatar Airways routes via Doha (DOH) are another option. Most large pets travel as manifest cargo rather than excess baggage on transatlantic routes of this distance."
            }
        ],
        "body": """Moving a dog or cat from the United States to the UAE takes careful planning, primarily because of the UAE's specific import permit process and its breed restriction list. Once you have confirmed your breed is permitted and obtained the MOCCAE permit, the logistics are straightforward.

## The MOCCAE import permit

All dogs and cats entering the UAE require an import permit from the Ministry of Climate Change and Environment (MOCCAE). Applications are submitted via the MOCCAE digital services portal. You will need your pet's microchip number, vaccination records, and breed confirmation.

The breed restriction list is strictly enforced. Do not assume your breed is permitted: check the current MOCCAE list before applying. Restricted breeds include Pit Bull Terrier, American Staffordshire Terrier, Rottweiler, Doberman Pinscher, Chow Chow, Akita, and others.

## USDA APHIS health certificate

From the USA, your health certificate must be endorsed by USDA APHIS. Book your appointment with an accredited vet and schedule APHIS endorsement at least 10 days before your flight. APHIS endorsement takes three to five business days in normal circumstances.

The health certificate must reference the microchip number and list all vaccinations with product names, batch numbers, and validity dates. Rabies, distemper, parvovirus, and hepatitis are typically required for dogs.

## Getting your pet to Dubai or Abu Dhabi

Most large dogs travel as manifest cargo. Emirates SkyCargo has a dedicated live animal service and experience handling UAE customs clearance at Dubai World Central or Dubai International Airport cargo terminals. Etihad Cargo handles arrivals at Abu Dhabi.

Small dogs and cats under 8 kg (including carrier) may be accepted in cabin on some carriers. Emirates does not allow pets in cabin on its commercial flights. Qatar Airways and Etihad permit small pets in cabin in economy on some routes.

## Timeline

For a USA to UAE move, allow:
- Four to six weeks for MOCCAE permit processing
- 10 days before travel for vet examination and APHIS endorsement
- Two to three weeks for freight booking and carrier arrangements

**Official sources:**
- MOCCAE UAE: moccae.gov.ae
- USDA APHIS international pet travel: aphis.usda.gov
- Emirates SkyCargo live animals: skycargo.com
"""
    },
    {
        "slug": "uk-to-morocco-pet-transport-guide",
        "title": "Pet Transport from UK to Morocco 2026",
        "description": "How to move your dog or cat from the UK to Morocco. APHA health certificate, ONSSA requirements, ferry or flight options, and breed restriction rules.",
        "date": "2026-05-08",
        "tags": ["uk to morocco", "pet transport", "morocco", "ONSSA", "APHA"],
        "faqs": [
            {
                "question": "Can I bring my pet from the UK to Morocco by ferry?",
                "answer": "Yes. The most popular route is by ferry from southern Spain to Morocco, typically Tarifa or Algeciras to Tangier. Pets must remain in the vehicle during crossing. Before reaching Spain, UK pets need an APHA-endorsed AHC. At the Moroccan border, ONSSA officers inspect pets and documentation. Some owners choose to fly directly from London to Casablanca or Marrakech instead."
            },
            {
                "question": "What documents does my pet need to go from the UK to Morocco?",
                "answer": "Your pet needs an Animal Health Certificate (AHC) endorsed by APHA, issued within five days of the Morocco border crossing or arrival date. The certificate must confirm current rabies vaccination, microchip number, and absence of signs of disease. ONSSA requires the AHC to have been endorsed by the official UK authority. Allow at least 10 working days total for vet preparation and APHA endorsement."
            },
            {
                "question": "Which airlines fly pets from the UK to Morocco?",
                "answer": "Royal Air Maroc operates flights from London Heathrow to Casablanca and accepts pets as hold baggage or cargo on some routes. British Airways and Iberia also operate routes via their hubs. EasyJet and Ryanair do not accept pets in hold. For a direct UK to Morocco pet move, contact the airline's cargo or excess baggage team well in advance to confirm current policies."
            }
        ],
        "body": """Morocco is increasingly popular with UK expats, retirees, and second-home owners. The UK to Morocco pet move is very feasible, but the short five-day health certificate window and the APHA endorsement step require careful timing.

## Two ways to travel

**Option 1: Fly direct.** London to Casablanca (CMN) or Marrakech (RAK) takes three to four hours. Direct flights are available via Royal Air Maroc and some charter services. Pets as hold baggage or cargo is the standard arrangement. In-cabin pets are not widely offered on UK to Morocco routes.

**Option 2: Drive via Spain and ferry.** Many UK pet owners drive through France and Spain, then take a short ferry crossing from Tarifa or Algeciras to Tangier. This can be an excellent option for dogs that travel poorly by air. The journey through Europe is covered by the AHC, and the same certificate is used at the Moroccan border.

## The five-day certificate challenge

Morocco's requirement that the health certificate be issued within five days of entry is tighter than most countries. If you are flying, this means a vet appointment in the final days before travel, then immediate APHA endorsement. APHA offers a priority service, but standard processing is three to five working days.

Plan backwards from your travel date. If flying on a Friday, your vet examination should be no earlier than the Monday of that week, and APHA endorsement must be fast-tracked.

## What to expect on arrival

At Casablanca airport, ONSSA has an inspection facility at the cargo terminal. At the Tangier ferry terminal, ONSSA officers are based at the port. The inspection is usually brief if your documents are correct. Present the endorsed AHC, vaccination record, and microchip details.

## After arrival

Register your pet with a local vet and ensure annual boosters are maintained. Casablanca, Rabat, and Marrakech all have capable vet practices. The expat community in Morocco is well-established and a good resource for local pet service recommendations.

**Official sources:**
- ONSSA Morocco: onssa.gov.ma
- APHA AHC information: GOV.UK/APHA
- Royal Air Maroc pet policy: royalairmaroc.com
"""
    },
    {
        "slug": "eu-to-usa-pet-transport-guide",
        "title": "Pet Transport from EU to USA 2026",
        "description": "How to move your dog or cat from any EU country to the United States. CDC dog import rules, USDA requirements, health certificate steps, and airline cargo options.",
        "date": "2026-05-08",
        "tags": ["eu to usa", "pet transport", "CDC", "dog import usa", "health certificate"],
        "faqs": [
            {
                "question": "What are the CDC rules for importing a dog from Europe to the USA?",
                "answer": "The CDC updated US dog import requirements significantly in 2024. All dogs entering the USA must: be microchipped; appear healthy on arrival; be at least 6 months old; and, if the dog has been in a high-risk country for dog rabies within the previous 6 months, must have a US-issued microchip, proof of USDA-compliant rabies vaccination, and a valid DogBot reservation and CVI. Most EU countries are considered low-risk, which simplifies the process considerably."
            },
            {
                "question": "Does my EU-vaccinated dog need a US-standard rabies vaccination?",
                "answer": "If your dog has only been in low-risk countries (which includes most EU countries), and has a valid rabies vaccination from those countries, the CDC low-risk pathway applies. You still need to present a valid rabies vaccination certificate on arrival. If the dog has been in any high-risk country within 6 months, additional USDA APHIS-compliant vaccination and documentation is required."
            },
            {
                "question": "What happens to my cat when moving from the EU to the USA?",
                "answer": "Cats face simpler US import requirements than dogs. The CDC requirements above apply to dogs only. Cats entering the USA need only a health certificate from an accredited vet confirming the cat is healthy and free from signs of disease. No rabies vaccination is federally required for cat entry (though some US states require it within 30 days of arrival). Check your destination state's requirements."
            }
        ],
        "body": """Moving a pet from Europe to the United States is a common relocation for expats returning home or Americans who have been working in the EU. The USA's approach to pet imports is notably different from Europe's: the focus for dogs is rabies risk management through the CDC's country classification system.

## CDC dog import rules in plain terms

The USA classifies countries by rabies risk level. Most EU countries (Germany, France, the Netherlands, Spain, Italy, and others) are classified as low-risk, which means dogs from these countries face a simplified entry process.

For dogs arriving from low-risk countries only:
- Must be microchipped
- Must be at least 6 months old
- Must appear healthy on arrival
- Must have a valid rabies vaccination certificate if the dog has been vaccinated

If your dog has spent time in a high-risk country (which includes some Eastern European or non-EU countries) within the past 6 months, additional requirements apply including the DogBot reservation system and USDA APHIS-compliant documentation.

## Health certificate for cats

Cats entering the USA do not face the same CDC requirements as dogs. A health certificate from an accredited vet issued within 10 days of travel is standard best practice and required by most airlines. US federal law does not mandate rabies vaccination for cat entry, but individual US states may require it within 30 days of arrival. Check your destination state's requirements.

## The health certificate process from EU countries

An official health certificate from an EU member state is typically endorsed by the national competent authority (for example, the DGAV in Portugal, DGAL in France, or LAVES in Germany). Airlines may require the endorsement as part of their cargo documentation.

In the USA, pets do not pass through a USDA inspection facility on arrival; they clear through US Customs and Border Protection along with their owner. For cargo arrivals, a licensed customs broker handles the process.

## Airlines from Europe to the USA

Most major transatlantic carriers accept pets. Lufthansa, British Airways, Air France, KLM, and others operate cargo pet services. For smaller dogs and cats, some carriers permit in-cabin transport in economy. Contact your chosen airline well in advance.

**Official sources:**
- CDC dog import requirements: cdc.gov
- USDA APHIS dog import: aphis.usda.gov
- US CBP live animals: cbp.gov
"""
    },
    {
        "slug": "canada-to-uk-pet-transport-guide",
        "title": "Pet Transport from Canada to UK 2026",
        "description": "Moving your dog or cat from Canada to the United Kingdom. CFIA health certificate, APHA AHC rules, rabies titre test timeline, and airline options from Toronto or Vancouver.",
        "date": "2026-05-08",
        "tags": ["canada to uk", "pet transport", "CFIA", "APHA", "titre test"],
        "faqs": [
            {
                "question": "What documents does my dog need to move from Canada to the UK?",
                "answer": "To enter the UK from Canada, your dog needs an Animal Health Certificate (AHC) in the format specified by APHA. The AHC is completed by a Canadian accredited vet and then endorsed by the CFIA (Canadian Food Inspection Agency). The certificate must confirm: ISO microchip, current rabies vaccination, and a satisfactory rabies titre test result of at least 0.5 IU/ml. The titre test must be taken at least 30 days after the most recent rabies vaccination and the animal must wait at least three months after the blood draw before entering the UK."
            },
            {
                "question": "How long does the titre test process take for Canada to UK pet travel?",
                "answer": "The titre test is the main timeline driver. Blood must be drawn at least 30 days after the most recent rabies vaccination. The sample goes to a DEFRA-approved laboratory. Results typically take two to three weeks. After the titre test is confirmed satisfactory (at least 0.5 IU/ml), the animal must wait at least three months before travelling to the UK. Total minimum preparation time from starting vaccinations: approximately five to six months."
            },
            {
                "question": "Which airlines take pets from Canada to the UK?",
                "answer": "Air Canada accepts pets as cargo on transatlantic routes from Toronto (YYZ) and Vancouver (YVR) to London Heathrow (LHR). British Airways Cargo and Virgin Atlantic Cargo also handle pet shipments on this route. Small pets (combined weight under 8 kg) may be accepted in cabin on some carriers. Most large dogs travel in the hold as checked baggage or manifest cargo."
            }
        ],
        "body": """Canada to UK is a well-trodden pet transport route, particularly for returning British expats, Canadian families moving to Europe, and dual nationals. The UK's strict rabies controls mean the process takes several months to prepare, but it is very well-defined.

## Why the timeline matters so much

The UK is rabies-free and applies robust import controls to stay that way. The titre test system is the key tool: it proves your pet has a strong enough immune response to rabies vaccination that the risk of carrying the virus is negligible.

The minimum timeline from scratch:
1. Microchip implanted
2. Rabies vaccination given (after microchip)
3. Wait 30 days
4. Blood drawn for titre test at a DEFRA-approved laboratory
5. Wait for results (two to three weeks)
6. If result is at least 0.5 IU/ml, the three-month wait begins from the blood draw date
7. Your pet can travel to the UK after the three-month wait has elapsed

If your pet's vaccinations are already current and an acceptable titre test was done recently, you may be able to move more quickly. Check with your vet and CFIA on the specific documentation trail.

## The CFIA health certificate

From Canada, the health certificate is completed by an accredited vet and endorsed by the CFIA. The certificate must reference the microchip number, titre test result, date of blood draw, and laboratory reference. Allow 10 to 15 business days for CFIA endorsement.

The health certificate is valid for 10 days for entry into the UK. The vet examination must happen in this window, so plan precisely around your departure date.

## Travelling to Heathrow or Gatwick

Most Canada to UK pet journeys arrive at London Heathrow (LHR). APHA has a Border Control Post at Heathrow that handles incoming pets. If travelling via a different UK entry point, confirm it has an active Border Control Post for the animal type.

Air Canada, British Airways, and Virgin Atlantic all have experience with the Canada to UK route. Contact the cargo or live animal team at least three to four weeks before travel to confirm space, crate specifications, and documentation requirements.

**Official sources:**
- APHA UK pet import: GOV.UK/APHA
- CFIA Canada pet export: inspection.gc.ca
- DEFRA-approved titre test laboratories: GOV.UK
"""
    },
    {
        "slug": "ireland-to-australia-pet-transport-guide",
        "title": "Pet Transport from Ireland to Australia 2026",
        "description": "Moving your dog or cat from Ireland to Australia. DAFF approved pathway, titre test timeline, quarantine at Mickleham, health certificate steps, and airline cargo routes.",
        "date": "2026-05-08",
        "tags": ["ireland to australia", "pet transport", "DAFF", "quarantine", "titre test"],
        "faqs": [
            {
                "question": "How long is quarantine for pets arriving in Australia from Ireland?",
                "answer": "Dogs and cats entering Australia from Ireland (an approved country) typically serve 10 days quarantine at the DAFF-approved post-entry quarantine facility in Mickleham, Victoria. Ireland is on Australia's approved country list, which means the pathway is relatively straightforward compared to non-approved countries. The quarantine period allows DAFF to verify the animal's health status before release to the owner."
            },
            {
                "question": "What is the preparation timeline for Ireland to Australia pet transport?",
                "answer": "Australia requires a titre test with a result of at least 0.5 IU/ml. The blood sample must be taken at least 30 days after the most recent rabies vaccination. After a satisfactory result, DAFF requires that certain additional steps (including treatments) are completed within specific windows before departure. Total preparation time is typically six months or more from scratch. Ireland-based DAFF-approved vets can manage the full pathway for you."
            },
            {
                "question": "Which airlines take pets from Ireland to Australia?",
                "answer": "There are no direct flights from Dublin to Australian cities. Most Ireland to Australia pet journeys route via a European hub: London Heathrow (LHR), Amsterdam (AMS), Frankfurt (FRA), or Dubai (DXB). Qantas, Emirates, Singapore Airlines, and Etihad are commonly used for the long-haul sector. Your pet freight forwarder will plan the routing to meet Australian entry requirements."
            }
        ],
        "body": """Moving a pet from Ireland to Australia is a significant undertaking, but it is done successfully by hundreds of owners each year. Australia's biosecurity rules are among the strictest in the world, and the preparation timeline is long. The earlier you start, the smoother the process.

## Australia's approved country system

Australia classifies origin countries by biosecurity risk. Ireland is on Australia's approved country list, which means pets from Ireland can follow the standard pathway rather than the more intensive non-approved country pathway.

The approved country pathway still requires:
- An ISO microchip
- Rabies vaccination (and often a booster)
- A rabies titre test result of at least 0.5 IU/ml from a DAFF-approved laboratory
- Specific treatments (heartworm, flea, tick, and parasite treatments) within defined windows before departure
- An official health certificate endorsed by the relevant Irish authority
- Pre-booking at the Mickleham quarantine facility

## The Mickleham quarantine facility

All dogs and cats entering Australia must spend a quarantine period at the government-approved facility at Mickleham, Victoria (near Melbourne). For approved country pets, this is currently 10 days. Owners can visit their pets during quarantine.

Pre-booking at Mickleham is mandatory. Spaces fill up quickly, especially in summer. Book as early as possible once you have a rough travel date in mind.

## Routing from Ireland

Dublin Airport (DUB) does not have direct flights to Australia. You will route via a hub. London, Amsterdam, Frankfurt, and Dubai are the most commonly used connections. The routing must be planned carefully with your pet freight forwarder because Australia has specific requirements about transit country health status and layover duration.

Qantas, Emirates, Singapore Airlines, and Etihad all have experience handling pet cargo on long-haul routes into Australian airports including Melbourne (MEL), Sydney (SYD), and Brisbane (BNE).

## Starting the process

The six-to-eight month preparation window is not optional if your pet needs the full titre test pathway from scratch. Contact a DAFF-approved vet in Ireland as early as possible, ideally as soon as you have a move date in view.

**Official sources:**
- DAFF Australia pet import: agriculture.gov.au
- Mickleham quarantine bookings: agriculture.gov.au
- APHA Ireland pet export: GOV.UK/APHA (for UK-standard AHC)
"""
    },
    {
        "slug": "australia-to-uae-pet-transport-guide",
        "title": "Pet Transport from Australia to UAE 2026",
        "description": "How to move your dog or cat from Australia to the United Arab Emirates. DAFF export requirements, MOCCAE import permit, breed restrictions, and airline cargo routes.",
        "date": "2026-05-08",
        "tags": ["australia to uae", "pet transport", "DAFF", "MOCCAE", "dubai"],
        "faqs": [
            {
                "question": "What export documents does my Australian pet need for the UAE?",
                "answer": "Your pet needs an export health certificate issued by DAFF (Department of Agriculture, Fisheries and Forestry) or a DAFF-approved vet and endorsed by DAFF. The certificate must confirm microchip, current rabies vaccination, and core disease vaccinations. You also need an import permit from the UAE's MOCCAE before your pet travels. Apply for the MOCCAE permit at least four to six weeks before your departure date."
            },
            {
                "question": "Are there breed restrictions for dogs entering the UAE from Australia?",
                "answer": "Yes. The UAE restricts certain breeds from import, including Pit Bull Terrier, American Staffordshire Terrier, Rottweiler, Chow Chow, Akita, Doberman Pinscher, and others. These restrictions apply regardless of origin country. Check the current MOCCAE breed list before applying for the permit. Airlines may also apply additional breed restrictions."
            },
            {
                "question": "Which airlines fly pets from Australia to Dubai?",
                "answer": "Emirates SkyCargo offers dedicated live animal cargo services on the Australia to Dubai route from Sydney (SYD), Melbourne (MEL), and Brisbane (BNE). Etihad Cargo handles animals into Abu Dhabi (AUH). Qatar Airways Cargo via Doha (DOH) is another option. Most dogs travel as manifest cargo due to the long flight duration. Confirm live animal acceptance well in advance as not all flight types carry animals."
            }
        ],
        "body": """Australia to UAE is a route well-established by the large Australian expat community working in finance, construction, and hospitality across Dubai and Abu Dhabi. The process involves two sets of requirements: Australian export rules and UAE import rules.

## Australian export process

Australia takes pet exports seriously. DAFF oversees the export health certificate, which must be issued by a DAFF-accredited vet and endorsed by DAFF. The certificate confirms:
- ISO microchip
- Current rabies vaccination
- Core disease vaccinations
- Freedom from signs of disease on examination

DAFF endorsement typically takes five to ten business days. Book your vet examination at least three weeks before your departure date to allow time for endorsement and any corrections.

## UAE import process

The UAE's MOCCAE requires an import permit for all pet dogs and cats. Apply via the MOCCAE digital services portal. Processing typically takes two to four weeks. The permit will specify the permitted entry point (Dubai or Abu Dhabi) and must be presented on arrival.

Check the UAE breed restriction list before applying. The list is enforced strictly, and a permit will not be issued for restricted breeds.

## The long-haul logistics

Australia to UAE is a flight of approximately 14 to 17 hours. Most pets travel as manifest cargo, which is separate from passenger cabins and handled by the airline's live animal division. Emirates SkyCargo has climate-controlled cargo facilities at both ends of this route.

Crate specifications must meet IATA Live Animal Regulations. The crate must be large enough for the animal to stand, turn around, and lie down naturally. Provide a water container and consider attaching a small bag of food for the cargo team.

## After arrival in the UAE

On arrival at Dubai Airport or Abu Dhabi Airport cargo terminals, MOCCAE officers inspect incoming pets. If documentation is in order, your pet will be cleared and transferred to you or your freight agent.

**Official sources:**
- DAFF Australia: agriculture.gov.au
- MOCCAE UAE: moccae.gov.ae
- Emirates SkyCargo live animals: skycargo.com
"""
    },
    {
        "slug": "germany-to-singapore-pet-transport-guide",
        "title": "Pet Transport from Germany to Singapore 2026",
        "description": "Moving your dog or cat from Germany to Singapore. NParks AVS import licence, AVS country group status for Germany, quarantine booking, and airline cargo options.",
        "date": "2026-05-08",
        "tags": ["germany to singapore", "pet transport", "NParks", "AVS", "quarantine"],
        "faqs": [
            {
                "question": "Is Germany on Singapore's Group 1 approved country list?",
                "answer": "No. Germany is currently classified in Group 2 by Singapore's AVS/NParks, which means pets from Germany face a longer quarantine period on arrival than pets from Group 1 countries such as the UK or Australia. The quarantine period for Group 2 country pets can be 30 days. Confirm the current group status for Germany with NParks before starting preparations, as classifications are reviewed periodically."
            },
            {
                "question": "What documents does my dog need to move from Germany to Singapore?",
                "answer": "You need: an import licence from Singapore's NParks/AVS (applied for in advance); a health certificate endorsed by the German competent authority; current rabies vaccination; a rabies titre test (required for Group 2 countries) showing at least 0.5 IU/ml; and a pre-booked quarantine facility in Singapore. The health certificate must be completed by a German-accredited vet within 10 days of travel."
            },
            {
                "question": "Which airlines fly pets from Germany to Singapore?",
                "answer": "Lufthansa operates direct flights from Frankfurt (FRA) to Singapore Changi (SIN) and accepts pets as cargo. Singapore Airlines also operates this route with a live animal cargo service. Most large dogs travel as manifest cargo. Singapore Airlines has an established live animal programme through its cargo division. Book well in advance as space is limited."
            }
        ],
        "body": """Germany to Singapore is a popular route for European professionals relocating to Asia, and Singapore's strong expat community includes many pet owners. The process is manageable, but Singapore's quarantine requirements add cost and time to the move.

## Germany's group 2 status in Singapore

Singapore classifies origin countries into groups based on disease risk. Germany is currently in Group 2, which means a longer quarantine period on arrival compared to Group 1 countries like the UK and Australia. Quarantine for Group 2 pets is typically 30 days at an AVS-approved facility in Singapore.

Group status can change. Always check the current NParks classification for Germany before you start the preparation process.

## Getting the import licence

Singapore requires an import licence from NParks/AVS before your pet travels. Apply via the GoBusiness Licensing portal. You must have a quarantine facility booked and confirmed before you can complete the licence application.

NParks-approved quarantine facilities are private boarding facilities that meet Singapore's biosecurity standards. Spaces at these facilities book out quickly, so start this process early.

## Health certificate from Germany

Your German vet must complete a health certificate within 10 days of your travel date. The German competent authority (the relevant Landesamt or Veterinaramt, depending on your state) must endorse the certificate. Allow five to 10 working days for endorsement.

The certificate must confirm:
- Microchip number (ISO 15444)
- Current rabies vaccination
- Satisfactory titre test result for Group 2 country pets
- Freedom from signs of disease

## Flying from Frankfurt to Singapore

Lufthansa from Frankfurt (FRA) to Changi (SIN) is the most direct option and Lufthansa has experience with live animal cargo. Singapore Airlines also accepts live animal cargo on its Frankfurt route. Confirm space and live animal acceptance at least three to four weeks before travel.

**Official sources:**
- NParks/AVS Singapore: nparks.gov.sg
- GoBusiness Licensing: gobusiness.gov.sg
- Lufthansa live animals: lufthansa-cargo.com
"""
    },
    {
        "slug": "uk-to-kenya-pet-transport-guide",
        "title": "Pet Transport from UK to Kenya 2026",
        "description": "How to move your dog or cat from the UK to Kenya. KVB import requirements, APHA health certificate, breed considerations, and arrival procedures at Nairobi airport.",
        "date": "2026-05-08",
        "tags": ["uk to kenya", "pet transport", "kenya", "KVB", "nairobi"],
        "faqs": [
            {
                "question": "What documents does my dog need to travel from the UK to Kenya?",
                "answer": "Dogs entering Kenya require: an import permit from the Kenya Veterinary Board (KVB) or the Director of Veterinary Services; an Animal Health Certificate endorsed by APHA in the UK; current rabies vaccination; core disease vaccinations; and treatment against external and internal parasites within 14 days of travel. The health certificate must be issued within 10 days of travel."
            },
            {
                "question": "Is there quarantine for pets arriving in Kenya from the UK?",
                "answer": "Kenya does not impose routine quarantine for pets arriving with complete documentation and satisfactory health status. Arrival inspection is conducted by veterinary officers at Jomo Kenyatta International Airport (NBO). If your paperwork is correct and your pet appears healthy, clearance is typically granted on the day. Incomplete or incorrect documents can result in the animal being held at the importer's cost."
            },
            {
                "question": "Which airlines fly pets from the UK to Kenya?",
                "answer": "Kenya Airways operates direct flights from London Heathrow to Nairobi Jomo Kenyatta (NBO) and accepts pets as cargo on some services. British Airways and Ethiopian Airlines also operate this route and have live animal cargo experience. Most pets travel as excess baggage or manifest cargo. Contact the airline's cargo team at least three weeks before travel."
            }
        ],
        "body": """Kenya is home to a growing expat community, particularly in Nairobi, and many families relocating for development, NGO, or corporate work bring their pets. The process is workable, but the import permit step and documentation timing need attention.

## The Kenya Veterinary Board import permit

Pets entering Kenya need advance approval from the Kenya Veterinary Board (KVB) or the Director of Veterinary Services. Contact the KVB or the nearest Kenyan Embassy or High Commission to obtain the correct application form and submit it at least two to four weeks before travel.

The permit application typically requires your pet's microchip details, vaccination history, and information about the health certificate that will accompany the animal.

## APHA-endorsed health certificate

From the UK, your health certificate must be an AHC endorsed by APHA. The AHC format covers the core information Kenya requires: microchip number, species, breed, current rabies vaccination, other vaccinations, and parasite treatments.

Allow 10 to 15 working days for your vet to prepare and APHA to endorse the certificate. The certificate is valid for 10 days from the date of the official vet examination, so timing around your departure is important.

## Arriving at Nairobi

Most international pet arrivals come through Jomo Kenyatta International Airport (NBO). The Kenya Veterinary Board has inspection staff at the cargo terminal. Bring all original documents including the import permit, AHC, vaccination record, and any treatment certificates.

A local pet freight forwarder or clearing agent with experience at NBO can handle the customs clearance and inspection on your behalf, which smooths the process considerably.

## Living with a pet in Nairobi

Nairobi has a well-developed expat veterinary network, particularly in areas such as Karen, Westlands, and Lavington. Annual boosters for locally relevant diseases (including leptospirosis, kennel cough, and tick-borne diseases) are advisable. Your vet in Nairobi can provide a local vaccination and parasite protocol.

**Official sources:**
- Kenya Veterinary Board: kvb.go.ke
- APHA UK pet export: GOV.UK/APHA
- Kenya Airways cargo: kenyaairways.com
"""
    },

    # ------------------------------------------------------------------ #
    # BREED GUIDES                                                         #
    # ------------------------------------------------------------------ #
    {
        "slug": "travelling-with-a-greyhound-internationally",
        "title": "Travelling with a Greyhound Internationally",
        "description": "International travel with a Greyhound. Breed-specific airline policies, crate sizing for Greyhounds, country-level breed restrictions, and tips for keeping Greyhounds calm in transit.",
        "date": "2026-05-08",
        "tags": ["greyhound", "international pet travel", "airline policies", "racing greyhound"],
        "faqs": [
            {
                "question": "Do airlines ban Greyhounds?",
                "answer": "Greyhounds are not typically on airline breed ban lists the way brachycephalic breeds or Pit Bull types are. However, Greyhounds are large, and most airlines that accept large dogs in the hold will accept them. Some breed-specific airline policies apply to Greyhounds used as racing dogs, which may be classified under a different category. Check your specific airline's large dog and snout-to-body-ratio policies."
            },
            {
                "question": "What size crate does a Greyhound need for flying?",
                "answer": "Greyhounds are tall and deep-chested. A standard IATA crate that allows the dog to stand at full height, turn around, and lie down naturally is required. For most adult Greyhounds, this means an IATA-compliant crate of at least 91 cm long x 61 cm wide x 71 cm tall (IATA size 4 or 5). Measure your specific dog and add at least 10 cm in each direction to the dog's measurements for the minimum crate dimensions."
            },
            {
                "question": "Are Greyhounds restricted in any countries?",
                "answer": "Greyhounds are not specifically restricted by name in most countries' breed ban lists. However, if your Greyhound has physical characteristics that could cause confusion with a banned breed, carry a breed certificate or veterinary letter confirming breed. Australia restricts some sighthound crossbreeds under its dangerous dog categories. Check the specific destination country's rules."
            }
        ],
        "body": """Greyhounds are gentle, adaptable dogs, and many Greyhound owners successfully travel internationally with them. The main considerations are the size of the crate, the depth of the chest, and the breed's sensitivity to temperature extremes during transit.

## Crate requirements for Greyhounds

Greyhounds are tall and have a distinctive deep chest and narrow waist. Standard sizing charts do not always serve them well: a dog that appears to fit in a medium crate by weight may need a much larger crate due to its height and body shape.

Measure your Greyhound from the tip of the nose to the base of the tail (length), and from the top of the head to the ground (height). Add 10 cm to both measurements to get the minimum crate dimensions. For most adult Greyhounds, IATA size 4 or 5 is appropriate.

The crate must be IATA Live Animal Regulations (LAR) compliant: solid base, ventilated sides and rear, secure door, and a water container accessible from outside.

## Temperature sensitivity

Greyhounds have very little body fat and a thin coat, which makes them sensitive to cold. Airlines apply temperature restrictions to live animal transport: most will not accept dogs if the temperature at any point on the journey drops below 10 degrees Celsius or exceeds 29 degrees Celsius. Plan your travel timing accordingly to avoid winter cargo holds in cold climates.

Conversely, Greyhounds in crates can overheat in hot cargo areas. Avoid booking routes with long ground times in hot destinations.

## Country-specific rules

Greyhounds are not a restricted breed in most destination countries. However, if you are moving to a country with breed-specific legislation (such as the UAE's list of restricted breeds), confirm that Greyhounds are explicitly permitted. Some destinations restrict dog imports to companion animals only and have separate pathways for racing or sports dogs.

## Anxiety management

Greyhounds, particularly retired racing dogs, may have had very little exposure to domestic home life before you adopted them. Some are calm travellers. Others find confinement in a crate stressful. Crate training over several weeks before the journey is strongly recommended.

Speak to your vet about whether an anxiety aid is appropriate. Most vets do not recommend sedation for air travel, as sedatives can affect respiratory and cardiovascular function at altitude.
"""
    },
    {
        "slug": "travelling-with-a-whippet-internationally",
        "title": "Travelling with a Whippet Internationally",
        "description": "International travel guide for Whippet owners. Crate sizing, airline acceptance, country breed rules, and tips for keeping Whippets comfortable during long-haul flights.",
        "date": "2026-05-08",
        "tags": ["whippet", "international pet travel", "airline policies", "sighthound travel"],
        "faqs": [
            {
                "question": "Can Whippets fly in the cabin?",
                "answer": "Small Whippets (under 8 kg including carrier) may qualify for in-cabin travel on carriers that allow it. However, Whippets are medium-sized dogs and most adults are too large and heavy for under-seat travel. Most Whippets travel in the hold as checked baggage or manifest cargo. Confirm with your airline, as weight and size limits vary."
            },
            {
                "question": "Are Whippets restricted by any countries or airlines?",
                "answer": "Whippets are generally not on any country's breed ban list. They are not classified as dangerous and are not brachycephalic. Most airlines accept them in the hold without breed-specific restrictions. Some airline policies on snout-length ratios apply to snub-nosed breeds, which does not affect Whippets."
            },
            {
                "question": "How do I keep my Whippet warm in an airline cargo hold?",
                "answer": "Whippets have a short, single coat and low body fat, making them prone to chilling in cold environments. Airline cargo holds are temperature-controlled during flight but can be cold during ground handling. Fit your Whippet with a close-fitting thermal vest or fleece inside the crate. Avoid late-autumn or winter flights through very cold destinations where ground temperatures drop significantly."
            }
        ],
        "body": """Whippets are one of the most pleasant breeds to travel with internationally. They are generally calm, adaptable, and not prone to excessive stress behaviour when properly prepared. The main considerations are their sensitivity to cold and their lean body composition.

## Crate sizing for Whippets

Whippets are slender and typically lighter than their height might suggest. Unlike a stocky breed, a Whippet's body tucks in at the waist and the chest is relatively narrow.

Measure from nose tip to tail base and from the ground to the top of the head. Add 10 cm to each dimension for the crate minimum. Most adult Whippets need an IATA size 3 or 4 crate. The crate should feel snug but comfortable: a Whippet that finds a crate too large may feel insecure.

## Temperature management

Cold cargo holds are the biggest practical challenge for Whippets. While modern aircraft maintain cargo hold temperatures well during flight, ground time on a cold ramp, transfer periods, and early morning temperatures in northern destinations can cause distress.

A correctly fitted dog coat or fleece vest worn inside the crate provides warmth without compromising airflow. Do not use bulky blankets that could bunch and obstruct breathing.

## In-cabin or hold?

Small Whippets under 8 kg (combined with carrier) may qualify for in-cabin travel. Adult Whippets typically weigh 10 to 15 kg, so hold transport is usually necessary. If cabin travel is an option for a small or juvenile Whippet, a soft-sided carrier is the most comfortable format.

## Country rules

Whippets are not a restricted breed in any major destination country. UK and EU countries have no Whippet-specific rules. Australia, New Zealand, Singapore, Japan, and other strictly regulated countries accept Whippets through their standard pathways.

## Preparing your Whippet for travel

Introduce the crate at home several weeks before travel. Feed meals in the crate and encourage the dog to rest in it. A calm, familiar scent in the crate (an old t-shirt, for example) can reduce anxiety. On travel day, a short walk before the journey helps reduce nervous energy.
"""
    },
    {
        "slug": "travelling-with-a-doberman-internationally",
        "title": "Travelling with a Doberman Internationally",
        "description": "International travel with a Doberman Pinscher. Country breed bans, airline restrictions, crate sizing, and documentation tips for one of the most restricted breeds in international travel.",
        "date": "2026-05-08",
        "tags": ["doberman", "breed restrictions", "international pet travel", "dangerous breeds"],
        "faqs": [
            {
                "question": "Which countries ban or restrict Doberman Pinschers?",
                "answer": "Dobermans are restricted or banned in a significant number of countries. The UAE prohibits Doberman import as pets. Some Australian states and territories include Dobermans on restricted breed registers. Ireland, Portugal, and several Eastern European countries have restrictions for Dobermans in public spaces. Always research the specific destination before travel, as national rules differ from local municipality rules."
            },
            {
                "question": "Do airlines accept Dobermans?",
                "answer": "Many airlines accept Dobermans as cargo, but it depends on the carrier. Airlines with blanket bans on dangerous breed lists sometimes include Dobermans. Confirm with your airline's live animal team before booking. Some cargo-only carriers and specialist pet freight companies are more flexible. Dobermans cannot typically travel in cabin due to their size."
            },
            {
                "question": "What crate size does a Doberman need for flying?",
                "answer": "Adult Dobermans are large and muscular. Most adults need an IATA size 5 or 6 crate (approximately 107 to 122 cm long). Measure your specific dog from nose to tail and head to ground, then add 10 cm to each dimension. The crate must be compliant with IATA LAR standards. Some airlines have maximum crate dimension limits, so confirm the carrier's specifications before purchasing a crate."
            }
        ],
        "body": """Dobermans are one of the breeds most frequently caught out by international breed restriction lists. Before you commit to any destination, check the breed-specific legislation carefully. Many Doberman owners have successfully moved internationally, but thorough research is essential.

## Country-by-country considerations

**UAE:** Dobermans are on the MOCCAE restricted breed list and cannot be imported as pets.

**Australia:** Dobermans are not on the national banned breed list, but some Australian states and territories have local restrictions. Check the relevant state government before planning an Australia move.

**Ireland:** Ireland requires a muzzle and lead in public places for Dobermans and some other breeds listed under the Control of Dogs Act. They can be imported but must be registered and kept to specific control standards.

**Singapore:** Dobermans are on Singapore's restricted breed list and require special approval for import. In practice, most Doberman import applications are declined.

**USA and Canada:** No federal Doberman ban exists, but some US cities and municipalities have breed-specific ordinances. Check your destination city's rules.

**UK:** Dobermans are not on the UK's banned list under the Dangerous Dogs Act, which focuses on Pit Bull Terrier types. They can enter the UK through the standard pathway.

**EU countries:** Most EU countries do not specifically ban Dobermans at a national level, but local municipalities in some countries (particularly in Germany and France) apply additional registration or muzzle requirements.

## Airline acceptance

Before booking, contact your preferred airline's live animal or cargo team and ask specifically about Dobermans. Some airlines class them as dangerous breeds and decline. Others accept them with no special conditions beyond standard crate requirements.

Specialist pet freight forwarders often have relationships with cargo carriers that are more accommodating of restricted breeds where legally permitted at the destination.

## Documentation

For countries that permit Doberman import, carry:
- A clear breed certificate or pedigree from a recognised kennel club
- A veterinary letter confirming the dog's breed and behaviour assessment
- All standard health and vaccination documents

This helps prevent confusion at border inspection, particularly in countries where mixed-breed dogs might be misidentified.
"""
    },
    {
        "slug": "travelling-with-a-vizsla-internationally",
        "title": "Travelling with a Vizsla Internationally",
        "description": "International travel guide for Vizsla owners. Crate sizing, airline acceptance, destination country rules, and keeping your Vizsla calm during long-haul flights.",
        "date": "2026-05-08",
        "tags": ["vizsla", "hungarian pointer", "international pet travel", "breed travel guide"],
        "faqs": [
            {
                "question": "Are Vizslas restricted by any countries?",
                "answer": "Vizslas are not on any country's standard breed ban list. They are classified as a sporting/hunting breed and are not considered dangerous. The USA, UK, EU, Australia, Canada, Singapore, New Zealand, and Japan all accept Vizslas through standard pet import pathways. No breed-specific restrictions apply."
            },
            {
                "question": "Can my Vizsla fly in the cabin?",
                "answer": "Small Vizslas (under 8 kg combined with carrier) may qualify for in-cabin travel on carriers that permit it. Most adult Vizslas weigh 18 to 27 kg and must travel in the hold. Confirm with your airline, as weight and size limits vary."
            },
            {
                "question": "How do I prepare my Vizsla for a long-haul flight?",
                "answer": "Vizslas are sensitive, energetic dogs that bond closely with their owners. Extended separation and confinement can be stressful. Crate train thoroughly over several weeks before the journey. Ensure the dog has had physical exercise before being loaded. A familiar-scented item in the crate helps reduce anxiety. Speak to your vet about whether a short-acting anxiety supplement is appropriate."
            }
        ],
        "body": """The Vizsla, or Hungarian Pointer, is an affectionate, athletic dog that has been accompanying Europeans on relocations for many years. The good news for Vizsla owners is that the breed faces no country-level restrictions anywhere.

## No breed bans to worry about

Vizslas are classified as sporting dogs in every destination country's import framework. They are not on any dangerous dog list in the UK, Australia, USA, EU, Canada, UAE, Singapore, or Japan.

This means you can focus entirely on the procedural and welfare aspects of the move, rather than spending time establishing whether your breed is permitted.

## Crate requirements

Most adult Vizslas are medium-large dogs weighing 18 to 27 kg. They need an IATA-compliant crate of approximately size 4, but measure your specific dog to confirm. Vizslas are athletic and need enough space to stand, turn, and stretch out.

The smooth, short coat makes Vizslas sensitive to cold. Avoid crate lining with slippery material: a rubberised mat or a folded blanket fixed to the crate floor helps the dog maintain balance during ground handling.

## Managing Vizsla anxiety

Vizslas are known for their strong bond with their owners and can suffer separation anxiety. Long-distance cargo travel involves extended periods of separation and unfamiliar handling. The key is thorough crate preparation beforehand.

Start crate training at least six weeks before the journey. Feed meals in the crate, encourage rest there, and build positive associations. On travel day, exercise the dog well before heading to the airport.

Most vets recommend against sedation for air travel, as it can compromise respiratory and cardiovascular function. Natural calming supplements and pheromone sprays are gentler alternatives.

## Destination-specific preparation

Check your specific destination's pet import requirements. Vizslas follow the standard pathway for all countries. The common requirements are: microchip, rabies vaccination (plus a titre test for some destinations), health certificate, and advance import permits where required.
"""
    },
    {
        "slug": "travelling-with-a-weimaraner-internationally",
        "title": "Travelling with a Weimaraner Internationally",
        "description": "International travel with a Weimaraner. Crate sizing, airline large dog policies, country rules, and practical advice for flying with this large, sensitive breed.",
        "date": "2026-05-08",
        "tags": ["weimaraner", "large dog travel", "international pet travel", "airline policies"],
        "faqs": [
            {
                "question": "Are Weimaraners restricted by any countries or airlines?",
                "answer": "Weimaraners are not on any national breed ban list in the UK, EU, USA, Australia, Canada, UAE, or any other major destination. They are classified as sporting or hunting dogs and are not considered dangerous. No airline specifically bans Weimaraners as a breed, though all airlines apply their general large dog policies and crate dimension limits."
            },
            {
                "question": "What size crate does a Weimaraner need for flying?",
                "answer": "Adult Weimaraners typically weigh 25 to 40 kg and stand 55 to 70 cm at the shoulder. Most adults need an IATA size 5 crate (approximately 92 cm long x 61 cm wide x 67 cm tall). Measure your specific dog from nose to tail and from ground to top of head, then add 10 cm to each dimension. Confirm the crate dimensions are within your airline's maximum limits."
            },
            {
                "question": "How do I keep my Weimaraner calm on a long flight?",
                "answer": "Weimaraners are active, intelligent dogs that can become stressed when confined and inactive. Thorough crate training before travel is essential. Exercise well before loading. A familiar-scented item in the crate reduces anxiety. Do not sedate without veterinary advice, as sedation can cause complications at altitude. Some owners use calming supplements or pheromone sprays with good results."
            }
        ],
        "body": """Weimaraners are striking, intelligent dogs that have been accompanying expat families on international moves for decades. Their size means they always travel as hold cargo, but the process is well-established for large dogs.

## Size and crate planning

Weimaraners are solidly built, large dogs with a distinctive deep chest. Measure your dog carefully before purchasing a crate. Standard sizing charts often underestimate the space a Weimaraner needs.

For an adult Weimaraner, an IATA size 5 crate is typical. If your dog is on the larger end of the breed range (over 35 kg), a size 6 may be needed. Confirm the crate fits within your airline's maximum crate dimensions before purchasing.

The crate base should be solid and non-slip. Add a rubberised mat or secured bedding to prevent sliding during movement. Attach a secure water container to the crate door for hydration during transit.

## No breed restrictions

Weimaraners face no country-level breed restrictions anywhere in the world. All major destination countries accept them through standard import pathways. This simplifies planning considerably.

For high-security destinations like Australia, New Zealand, Japan, and Singapore, the standard pathway applies: microchip, rabies vaccination, titre test where required, health certificate, and advance import permits.

## Managing the journey

Weimaraners are active dogs and can find extended confinement stressful. On the day before travel, ensure your dog has a longer-than-usual run or play session. On travel day, exercise again before heading to the airport.

Some owners withhold food for four to six hours before the flight to reduce the risk of motion sickness and to keep the crate clean. Water should always be available.

## Airline considerations

Most airlines that accept large dogs accept Weimaraners. Check your airline's live animal policy, maximum crate dimensions, and any embargoes on routes with extreme temperature stops. Book early: large dog space in cargo holds is limited.
"""
    },

    # ------------------------------------------------------------------ #
    # PRACTICAL GUIDES                                                     #
    # ------------------------------------------------------------------ #
    {
        "slug": "how-to-import-a-puppy-internationally",
        "title": "How to Import a Puppy Internationally 2026",
        "description": "What is different about importing a puppy versus an adult dog? Age restrictions, early vaccination timing, titre test age eligibility, and country-specific minimum age rules.",
        "date": "2026-05-08",
        "tags": ["puppy import", "pet import", "minimum age", "vaccination timing", "practical guide"],
        "faqs": [
            {
                "question": "What is the minimum age for a puppy to be imported internationally?",
                "answer": "Most countries require a puppy to be at least 12 to 16 weeks old before it can be imported. The USA (CDC) requires dogs to be at least 6 months old for some pathways. Australia requires puppies to be at least 6 months old and to have completed the full titre test pathway before arrival. Japan does not permit puppy import until the titre test waiting period (180 days from blood draw) is complete, which effectively means puppies are at least 8 to 9 months old before they can enter. Always check the specific destination's minimum age requirement."
            },
            {
                "question": "When can I start the vaccination process for a puppy being imported internationally?",
                "answer": "Primary vaccinations typically begin at 8 weeks. The microchip must be implanted before or at the first vaccination. For destinations requiring a titre test, the test blood sample can only be taken 30 days after the final course vaccination, typically at around 14 to 16 weeks. The 90 to 180 day waiting period for most strict destinations then begins. This means planning a puppy import should start from birth or before you acquire the puppy."
            },
            {
                "question": "Is it harder to import a puppy than an adult dog?",
                "answer": "In some ways, yes. Adult dogs with established vaccination histories and titre test records may be able to travel more quickly. Puppies have to wait through the entire vaccination course and titre test sequence from the start. The total minimum timeline for a puppy to reach a strict destination like Japan or Australia is typically 8 to 10 months from birth. For less strict destinations like Spain, France, or the USA, a puppy of 12 weeks with current vaccinations and microchip can travel much sooner."
            }
        ],
        "body": """Importing a puppy is in many ways more complicated than moving an adult dog, simply because puppies have to complete the full vaccination sequence from scratch. If you are planning to acquire a puppy in your current country and bring it with you when you relocate, timing is everything.

## Age restrictions by country

**Australia:** Minimum arrival age 6 months. The titre test pathway must be completed before travel. In practice, most puppies arriving in Australia are 8 to 10 months old by the time they have met all requirements.

**Japan:** There is no specific minimum age listed by MAFF, but the 180-day waiting period after the titre test blood draw means that in practice, puppies cannot travel before roughly 8 to 9 months of age.

**New Zealand:** New Zealand requires puppies to be at least 6 months old. The titre test pathway applies from non-approved countries.

**Singapore:** Puppies entering Singapore must be old enough to have completed the required vaccination and titre test sequence. The AVS quarantine system applies to puppies just as to adults.

**USA (CDC pathway):** The 2024 CDC rules require dogs to be at least 6 months old.

**EU and UK:** Generally, a puppy vaccinated from 8 weeks and microchipped can travel at 12 to 15 weeks, once the vaccination course is complete and the waiting period after the final vaccine has passed (usually 21 days).

## Starting the process early

If you are acquiring a puppy specifically for an international move, talk to the breeder before you commit. Ask:
- Can the puppy be microchipped before the first vaccination?
- Can the breeder begin the titre test sequence?
- Does the breeder have experience with export health certificates?

For strict destinations (Japan, Australia, New Zealand), the puppy needs to start the process at 8 weeks and will likely not be able to travel until 8 to 10 months. Factor this into your move timeline.

## Finding a vet experienced with export puppies

Not all vets are familiar with international export pathways, particularly for strict destinations. Seek out a vet who has experience with USDA APHIS, APHA, CFIA, or DAFF export health certificates and titre test submission for your target destination.
"""
    },
    {
        "slug": "flying-with-two-dogs",
        "title": "Flying Internationally with Two Dogs",
        "description": "Can you fly with two dogs? Per-booking limits, crate sharing rules, documentation for multiple pets, and practical tips for managing two dogs in international transit.",
        "date": "2026-05-08",
        "tags": ["flying with two dogs", "multiple pets", "airline pet policy", "dog travel"],
        "faqs": [
            {
                "question": "Can two dogs share one crate on a flight?",
                "answer": "In limited circumstances, yes. IATA Live Animal Regulations permit two dogs under 14 kg each to share a single large crate if they are compatible, under 6 months old, or are a bonded pair from the same household. Airlines have their own policies on crate sharing, and many are more conservative than IATA minimums. Contact your airline directly to confirm whether crate sharing is permitted. Each dog still needs its own documentation."
            },
            {
                "question": "Are there limits on how many pets one person can travel with?",
                "answer": "Most airlines limit one pet per passenger for in-cabin travel. For hold or cargo travel, many airlines accept up to two pets per booking but policies vary. If you have more than two dogs, you may need to use a separate cargo booking, split the shipment across multiple flights or dates, or use a specialist pet freight service. Check your airline's specific multi-pet policy."
            },
            {
                "question": "Does each dog need a separate health certificate?",
                "answer": "Yes. Each individual animal needs its own health certificate, its own microchip record, and its own vaccination documentation. Health certificates are issued per animal. If you are moving two dogs, your vet will prepare two separate certificates. Some national authorities (USDA APHIS, APHA, CFIA) may allow multiple animals on a single endorsed certificate form if they are travelling together, but this varies by country. Check with your specific authority."
            }
        ],
        "body": """Travelling internationally with two dogs is very doable but requires more advance planning than travelling with one. The main considerations are airline limits on the number of pets per booking, crate sharing rules, and the documentation burden of managing two sets of paperwork.

## Airline policies on multiple dogs

Most airlines that accept pets in the hold allow two pets per booking, subject to space availability. However, this is not universal. Some carriers limit live animal bookings to one pet per passenger on certain routes. Call your airline's cargo or live animal team before buying tickets to confirm multi-dog bookings are accepted on your specific route.

For in-cabin travel, nearly all airlines limit passengers to one pet carrier under the seat. Two dogs cannot both travel in-cabin on the same flight unless you have separate passengers for each dog.

## Crate options for two dogs

**Separate crates:** Each dog in its own IATA-compliant crate is the safest and most commonly required option for hold travel. This avoids any stress between dogs during loading, transit, and the unfamiliar cargo environment.

**Shared crate:** IATA regulations permit two animals to share a crate if they are: both under 14 kg, under 6 months old, or from the same household and demonstrably compatible. Airlines apply their own rules on top. Some airlines refuse shared crates for liability reasons.

If you choose shared crate travel, carry documentation confirming both dogs are from the same household. A letter from your vet or a signed statement from you may be requested.

## Documentation for two dogs

Each dog needs:
- Its own microchip record
- Its own vaccination certificate
- Its own health certificate (issued per animal)
- Its own import permit where required (e.g. Singapore, UAE, Costa Rica)

For countries requiring titre tests, each dog's blood must be drawn and tested separately. You cannot share one titre test result between two animals.

## Practical tips

- Book cargo space for two pets well in advance, especially in peak relocation periods
- Label each crate clearly with the dog's name, your contact details, and the crate's contents
- If one dog is significantly larger or heavier than the other, confirm both crates meet the airline's maximum weight limits
- Travel in cooler months where possible to reduce heat stress for dogs in holds
"""
    },
    {
        "slug": "moving-to-costa-rica-with-a-pet",
        "title": "Moving to Costa Rica with a Pet",
        "description": "A practical guide to relocating to Costa Rica with your dog or cat. SENASA permit, health certificate steps, life with pets in Costa Rica, and finding a vet after arrival.",
        "date": "2026-05-08",
        "tags": ["moving to costa rica", "expat pets", "SENASA", "dog relocation", "cat relocation"],
        "faqs": [
            {
                "question": "Is Costa Rica a good country to move to with a dog?",
                "answer": "Generally yes. Costa Rica has a dog-friendly culture in many areas, particularly in urban centres like San Jose, Santa Ana, and coastal towns popular with expats. Veterinary care is widely available and of good quality in main towns. The warm climate suits most breeds, though very large or thick-coated dogs may need extra care in the heat. The main requirements for bringing your dog are a SENASA import permit and a current health certificate."
            },
            {
                "question": "Are there any breed restrictions in Costa Rica?",
                "answer": "Costa Rica passed legislation in 2020 that restricts certain breeds in public, including Pit Bull Terrier, Doberman Pinscher, Rottweiler, and others classified as potentially dangerous. These breeds must be muzzled in public, kept on a lead, and owners must hold third-party liability insurance. Importation of these breeds is more complex. Check the current SENASA rules before importing a restricted breed."
            },
            {
                "question": "What is the climate like for pets in Costa Rica?",
                "answer": "Costa Rica is tropical, with average temperatures of 20 to 30 degrees Celsius year-round in most areas. Coastal and lowland areas are hotter and more humid. Highland areas such as San Jose are cooler and more moderate. Thick-coated breeds (Siberian Husky, Bernese Mountain Dog, Newfoundland) will find lowland Costa Rica uncomfortable. Brachycephalic breeds (Bulldogs, Pugs) are at higher risk in the heat. Most short-coated breeds adapt well."
            }
        ],
        "body": """Costa Rica is one of the most popular destinations for expats from North America and Europe, and the country's warm, dog-friendly culture makes it a good choice for pet owners. The import process is among the most straightforward in Latin America.

## The SENASA permit

The first step is applying for a zoo sanitary import permit from SENASA (Servicio Nacional de Salud Animal). Apply online at senasa.go.cr. The form asks for your pet's species, breed, microchip number, vaccination history, and your travel dates.

SENASA typically issues permits within a few days to two weeks. Print the permit and carry it with you. Airlines handling your pet as cargo will also need the permit number.

## The health certificate

Your health certificate must be issued within 15 days of your travel date. It must confirm:
- Current rabies vaccination
- Distemper, parvovirus, and hepatitis vaccinations for dogs
- Appropriate feline vaccinations for cats
- Parasite treatments within the last 30 days (internal and external)
- Microchip number and physical health confirmation

USDA APHIS endorsement (for US-origin pets) or APHA endorsement (for UK-origin pets) is recommended. Some Costa Rican entry officials accept un-endorsed health certificates from certain countries, but an endorsed certificate removes ambiguity.

## Life with a pet in Costa Rica

**Climate:** Most of the country is warm year-round. San Jose's central valley is the most moderate. Coastal areas are hot and humid. If you have a thick-coated or brachycephalic breed, choose your location carefully and ensure indoor air conditioning is available.

**Veterinary care:** Good vet clinics are available in San Jose and most larger towns. In rural areas, access can be limited. The Costa Rican College of Veterinarians (COLVET) maintains a directory of registered practices.

**Day-to-day life:** Dogs are common pets in Costa Rican society, and many restaurants, shops, and parks are dog-friendly. Leash laws are not universally enforced in rural areas, but urban areas have more structured rules. Rabies, leptospirosis, parvovirus, and tick-borne disease are locally relevant: your Costa Rican vet will advise on a local vaccination and parasite protocol.

**Official sources:**
- SENASA Costa Rica: senasa.go.cr
- USDA APHIS international travel: aphis.usda.gov
"""
    },
    {
        "slug": "moving-to-mexico-with-a-pet",
        "title": "Moving to Mexico with a Pet",
        "description": "A complete guide to relocating to Mexico with your dog or cat. SENASICA health certificate, breed rules, vet access, and practical tips for cities like Mexico City, Merida, and Puerto Vallarta.",
        "date": "2026-05-08",
        "tags": ["moving to mexico", "expat pets", "SENASICA", "dog mexico", "cat mexico"],
        "faqs": [
            {
                "question": "Is it easy to move to Mexico with a dog?",
                "answer": "Yes, Mexico is one of the more straightforward countries for pet import. No advance permit is required from most origin countries. A health certificate issued within 10 days of travel by a licensed vet is the main requirement, along with current rabies vaccination. SENASICA officers at major international airports carry out a brief inspection on arrival. Most dogs are cleared without any issues if the health certificate is correct."
            },
            {
                "question": "Can I bring a large dog to Mexico?",
                "answer": "Yes. Mexico does not restrict import by breed or size through its SENASICA process. Large dogs travel as hold cargo on most airlines serving Mexico. Airlines may have their own size and weight limits for hold-cargo dogs, so confirm with your carrier. Once in Mexico, large dogs are widely accepted in houses and many outdoor spaces."
            },
            {
                "question": "Is veterinary care good in Mexico?",
                "answer": "Veterinary care quality varies by location. In major cities (Mexico City, Guadalajara, Monterrey) and popular expat destinations (San Miguel de Allende, Puerto Vallarta, Merida, Oaxaca), there are well-equipped vet clinics familiar with international standards. In rural areas, access is more limited. Most expat community groups maintain a list of trusted local vets."
            }
        ],
        "body": """Mexico consistently ranks among the top three destinations for North American expat relocations, and for good reason: the process of bringing a pet is among the least complicated of any major destination.

## What SENASICA actually requires

SENASICA (the National Service of Agro-Food Health, Safety and Quality) is Mexico's food and animal safety authority. For pet imports, the requirements are:

- A health certificate issued by a licensed vet within 10 days of travel
- Current rabies vaccination (record on the certificate)
- Other core vaccinations recorded (distemper, parvovirus, hepatitis for dogs; feline viral rhinotracheitis, panleukopenia, and calicivirus for cats)
- The animal is free from signs of disease
- No mandatory advance import permit for companion animals from most countries

That is it. There is no mandatory titre test, no quarantine, and no government endorsement requirement from most origin countries.

## Arriving in Mexico

On arrival at a major airport (Mexico City MEX, Cancun CUN, Guadalajara GDL, Puerto Vallarta PVR, and others), a SENASICA inspector will briefly review your health certificate and may check your pet's microchip. A small inspection fee (typically USD 5 to 30) may apply. If your certificate is in order and your pet appears healthy, clearance is quick.

## Where to live with your pet in Mexico

**Mexico City:** Dog ownership is very high in the capital. Dog parks, groomers, and pet-friendly restaurants are common. Vet care in Condesa, Polanco, and Santa Fe is excellent.

**Puerto Vallarta and the Riviera Nayarit:** Popular with North American expats. Strong dog culture, beaches (though beach rules vary), and a well-connected expat vet network.

**Merida and the Yucatan:** Growing expat community, very pet-friendly culture. Heat can be intense, so air conditioning is important for thick-coated breeds.

**San Miguel de Allende:** Small but affluent expat community. Good vet access, cooler altitude climate.

## Health considerations in Mexico

After arrival, work with a local vet on a Mexico-appropriate booster schedule. Diseases such as ehrlichiosis, leptospirosis, and heartworm are present in many regions. Regular parasite treatment is essential, particularly in coastal and tropical areas.

**Official sources:**
- SENASICA Mexico: gob.mx/senasica
- USDA APHIS Mexico: aphis.usda.gov
"""
    },
    {
        "slug": "moving-to-singapore-with-a-pet",
        "title": "Moving to Singapore with a Pet",
        "description": "A complete guide to relocating to Singapore with your dog or cat. NParks import licence, quarantine booking, breed restrictions, and practical life with pets in the city-state.",
        "date": "2026-05-08",
        "tags": ["moving to singapore", "expat pets", "NParks", "pet quarantine", "singapore expat"],
        "faqs": [
            {
                "question": "How much does it cost to move a dog to Singapore?",
                "answer": "The full cost of moving a dog to Singapore includes: the NParks import licence fee; quarantine facility fees (SGD 30 to 80 per day, typically 10 to 30 days depending on origin country); airline cargo fees (which vary widely by size and route); health certificate and endorsement costs in the origin country; and vet consultation fees. Total costs for a medium dog from the UK or Australia typically range from SGD 2,000 to 6,000 depending on the full route and quarantine duration."
            },
            {
                "question": "Which breeds are banned from Singapore?",
                "answer": "Singapore prohibits the import of several breeds, including: Pit Bull Terrier, Akita, American Bulldog, Bull Terrier, Boerboel, Dogo Argentino, Fila Brasileiro, Neapolitan Mastiff, Perro de Presa Canario, Rottweiler, and various cross-breeds with these dogs. The list is defined in the Schedule to the Animals and Birds (Dogs) Rules. If your dog is on or resembles a breed on this list, contact NParks before proceeding."
            },
            {
                "question": "Can my cat come to Singapore without quarantine?",
                "answer": "No. Cats entering Singapore undergo the same post-arrival quarantine system as dogs. The quarantine duration depends on the origin country group. Cats from Group 1 countries (UK, Australia, New Zealand, Ireland, Japan, etc.) typically quarantine for 10 days. Cats from Group 2 countries quarantine for 30 days. All cats must have a valid import licence from NParks and a confirmed quarantine facility booking before travel."
            }
        ],
        "body": """Singapore is one of the world's great expat cities, and thousands of families with pets relocate here each year. The import process is well-structured and consistently administered. The key to a smooth move is starting early and following the steps in the correct order.

## Understanding Singapore's country group system

NParks (National Parks Board) via its Animal and Veterinary Service (AVS) classifies origin countries into groups:

**Group 1** (shorter quarantine, simpler pathway): Australia, New Zealand, UK, Ireland, Japan, Taiwan, Hong Kong, and a few others. Post-arrival quarantine is typically 10 days.

**Group 2** (longer quarantine): USA, Canada, and most European countries including Germany, France, Netherlands, and others. Post-arrival quarantine is typically 30 days.

**Group 3** (most restrictive): All other countries not in Group 1 or 2.

Always confirm your country's current group status on the NParks website, as classifications are reviewed.

## Step-by-step process

1. **Book a quarantine facility:** NParks-approved private quarantine facilities in Singapore must be booked in advance. Book as soon as you have an approximate travel date.

2. **Apply for the import licence:** Through the GoBusiness portal. You need the quarantine facility booking reference, your pet's microchip number, and vaccination records.

3. **Prepare documentation in your origin country:** Health certificate endorsed by national authority, titre test (for Group 2 countries), microchip record.

4. **Book the cargo flight:** Contact your airline's live animal team. Singapore Airlines and Qantas have well-established live animal programmes to Changi (SIN).

5. **Arrive in Singapore:** Your pet goes directly from the aircraft to the approved quarantine facility. You will be notified when they are settled.

6. **Quarantine completion:** At the end of the quarantine period, collect your pet and register them with the relevant Singapore authorities.

## After quarantine: life in Singapore

Singapore is a comfortable, safe, and well-served city for pet owners. Changi, Bishan, Bukit Timah, and East Coast areas have well-used dog parks. Veterinary care is excellent and internationally trained vets are common.

Heat and humidity are the main welfare consideration. Breeds with thick coats or brachycephalic breeds need careful management in Singapore's climate. Access to air conditioning is essential.

**Official sources:**
- NParks/AVS: nparks.gov.sg
- GoBusiness licensing: gobusiness.gov.sg
- Approved quarantine facilities: nparks.gov.sg
"""
    },
    {
        "slug": "pet-health-certificate-vs-pet-passport",
        "title": "Pet Health Certificate vs Pet Passport: What is the Difference?",
        "description": "EU pet passport versus health certificate explained. Which one you need for international travel, what each document contains, and how Brexit changed UK pet travel.",
        "date": "2026-05-08",
        "tags": ["pet passport", "health certificate", "EU pet travel", "AHC", "brexit pets"],
        "faqs": [
            {
                "question": "What is the difference between a pet passport and a health certificate?",
                "answer": "An EU pet passport is an ongoing document that records your pet's microchip number, vaccinations, and other health information over its lifetime. It is used for travel within the EU and a small number of approved third countries. A health certificate (or Animal Health Certificate) is a single-use document completed by an official vet for one specific journey. It confirms your pet's health status at a particular point in time. Health certificates expire (typically within 10 days for international entry). Passports do not expire but their recorded vaccinations do."
            },
            {
                "question": "Do UK pets still need a pet passport?",
                "answer": "UK pets no longer have access to the EU pet passport since Brexit. UK-issued EU pet passports issued before 1 January 2021 are valid only for travel back into the UK, not for entering EU countries. For EU or international travel, UK pets need an Animal Health Certificate (AHC) endorsed by APHA for each journey. The AHC is valid for 10 days of travel. If you are a UK resident travelling to the EU with a pet, you need a fresh AHC each time."
            },
            {
                "question": "Which countries accept an EU pet passport?",
                "answer": "The EU pet passport is accepted across all 27 EU member states, as well as in non-EU countries that have adopted equivalent frameworks, such as Switzerland, Norway, Iceland, and Liechtenstein. Outside this group, most other countries require a health certificate for pet entry. The EU pet passport is not accepted in the USA, Canada, Australia, New Zealand, Singapore, Japan, UAE, or most non-European destinations."
            }
        ],
        "body": """One of the most common questions from first-time pet travellers is whether they need a pet passport or a health certificate. The answer depends on where you are and where you are going, and since Brexit the situation for UK owners has changed significantly.

## What is an EU pet passport?

An EU pet passport is a standardised document issued by an authorised vet in any EU member state (or by accredited vets in Switzerland, Norway, Iceland, and Liechtenstein). It records:
- The owner's name and contact details
- The animal's species, breed, sex, date of birth, and colour
- The microchip number and implant date
- Rabies vaccination history (dates, product names, batch numbers)
- Other vaccinations
- Parasite treatment records

The passport does not expire, but the vaccinations recorded in it do. If your rabies vaccination lapses, the passport remains valid as a document but your pet is no longer in compliance with vaccination requirements.

The EU pet passport was designed to allow the free movement of pets across EU member state borders. It is a convenient, reusable document.

## What is a health certificate?

A health certificate is a document completed by an official or accredited veterinarian for a specific journey. It certifies that the animal was examined on a specific date and found to be healthy and free of signs of infectious or contagious disease, and confirms all documentation (microchip, vaccination records).

Unlike the passport, a health certificate is single-use and time-limited. Most destination countries require the health certificate to be issued within 10 days of travel. Some require it within 5 or 7 days.

For many international destinations, the health certificate must also be endorsed by the national veterinary authority: USDA APHIS in the USA, APHA in the UK, CFIA in Canada, DAFF in Australia.

## Brexit and UK pet owners

Before Brexit (before 1 January 2021), UK vets could issue EU pet passports and UK pets could travel freely across the EU with one. Since Brexit, the UK is a third country. UK-issued EU pet passports are no longer valid for EU entry. UK pets entering EU countries now need:

- An Animal Health Certificate (AHC) in the EU-specified format
- APHA endorsement
- A new AHC for each trip into the EU (valid 10 days)

This is a significant practical change for UK owners with pets who travel frequently between the UK and continental Europe.

## When do you need each one?

| Scenario | Document needed |
|----------|----------------|
| EU resident travelling within EU | EU pet passport |
| UK resident travelling to EU/EEA | AHC endorsed by APHA |
| USA resident travelling to EU | US-format health certificate endorsed by USDA APHIS |
| Travelling to Japan, Australia, NZ | Health certificate endorsed by national authority |
| Travelling to Singapore | Health certificate + NParks import licence |
| Travelling to UAE | Health certificate + MOCCAE permit |
"""
    },
    {
        "slug": "how-long-does-pet-transport-take",
        "title": "How Long Does International Pet Transport Take?",
        "description": "Timeline guide for international pet transport. Preparation timelines by destination, documentation processing times, and realistic planning windows for a smooth move.",
        "date": "2026-05-08",
        "tags": ["pet transport timeline", "how long", "planning guide", "preparation", "practical guide"],
        "faqs": [
            {
                "question": "How long in advance should I start planning international pet transport?",
                "answer": "It depends entirely on the destination. For straightforward destinations like Spain, France, the USA, or Canada, 4 to 8 weeks is typically sufficient if your pet's vaccinations are current. For strict destinations with titre test requirements (UK, EU from outside), 3 to 6 months is the minimum. For Japan, New Zealand, and Australia, 6 to 9 months is required for the full pathway. Starting early always creates a buffer for unexpected delays."
            },
            {
                "question": "How long does a USDA APHIS health certificate endorsement take?",
                "answer": "Standard USDA APHIS endorsement takes 3 to 5 business days. Priority (rush) service is available at additional cost and can reduce this to 1 to 2 business days. Always schedule the vet appointment and APHIS endorsement booking at least 10 to 14 days before your travel date to account for any delays. The health certificate is only valid once endorsed, and it is typically valid for 10 days for the specific destination."
            },
            {
                "question": "What takes the longest in the international pet transport process?",
                "answer": "For most destinations, the titre test waiting period is the longest single step. After blood is drawn, the laboratory typically takes 2 to 3 weeks to process and issue results. For destinations like Japan, a mandatory 180-day wait then begins from the blood draw date. For Australia, a 3-month wait after a satisfactory titre test result is required. Health certificate and permit processing (typically 1 to 4 weeks) comes next. The actual flight takes hours."
            }
        ],
        "body": """One of the most common miscalculations in international pet moves is underestimating the preparation time. The flight itself may take 12 hours. The preparation can take six months. Here is a realistic breakdown by destination type.

## Quick reference timeline by destination

**Straightforward destinations (4 to 8 weeks from current vaccinations):**
- Spain, France, Germany, Italy, Portugal, and other EU countries (from EU with valid EU passport)
- USA and Canada (cats and vaccinated dogs from most EU countries)
- Mexico and most Latin American countries
- Most Middle Eastern countries with standard documentation

**Medium-complexity destinations (3 to 6 months):**
- UK from outside EU (titre test required from some countries)
- EU from UK (AHC required, titre test for some origins)
- South Korea, UAE, Saudi Arabia
- EU from USA/Australia

**Strict destinations (6 to 12+ months):**
- Australia (6 to 8 months minimum from scratch)
- New Zealand (6 to 8 months minimum)
- Japan (180-day wait after titre test blood draw = minimum 8 to 10 months for puppies)
- Singapore (varies, but quarantine period after arrival is 10 to 30 days additional)
- Hawaii (as strict as international destinations for mainland-US pets)

## Breaking down the steps

**Step 1: Microchip and vaccination** (from scratch: 2 to 4 weeks)
Microchip must be implanted first, then vaccination begins. Primary courses for puppies take 3 to 4 weeks. Adult dogs with up-to-date vaccinations can skip this step.

**Step 2: Titre test blood draw** (30 days after vaccination minimum)
Must wait 30 days from the most recent rabies vaccination before blood is drawn.

**Step 3: Laboratory processing** (2 to 3 weeks)
Blood is sent to an approved laboratory. Results come back within 2 to 3 weeks usually.

**Step 4: Waiting period after satisfactory result** (90 days for UK entry, 180 days for Japan)
This is the longest single step for strict destinations.

**Step 5: Health certificate and endorsement** (1 to 3 weeks)
Vet examination, certificate preparation, national authority endorsement.

**Step 6: Import permit applications** (2 to 6 weeks)
Singapore, UAE, Costa Rica, and others require advance permits.

**Step 7: Cargo booking and crate preparation** (2 to 4 weeks before travel)
Cargo space is limited. Book as early as possible.

## The value of a pet transport specialist

A specialist pet relocation agent can map out your specific timeline, flag steps you might miss, and coordinate multiple stages simultaneously. For complex destinations, the cost of an agent is often recovered by avoiding costly mistakes.
"""
    },
    {
        "slug": "which-airlines-accept-large-dogs",
        "title": "Which Airlines Accept Large Dogs in 2026?",
        "description": "A guide to airlines that accept large dogs in hold cargo or excess baggage. Carrier-by-carrier comparison, weight limits, embargoes, and how to book large dog travel.",
        "date": "2026-05-08",
        "tags": ["airlines large dogs", "large dog travel", "cargo pet", "hold pet", "airline comparison"],
        "faqs": [
            {
                "question": "Which airlines accept the largest dogs as cargo?",
                "answer": "Most major full-service carriers accept large dogs as manifest cargo or checked baggage. Airlines with established large dog cargo programmes include Lufthansa, British Airways, Air France, KLM, Singapore Airlines, Qantas, Emirates SkyCargo, Etihad Cargo, and American Airlines. Weight limits vary by carrier, but dogs up to 50 kg or more in an approved crate are accepted by most of these carriers. Confirm maximum crate and combined weight limits with each airline before booking."
            },
            {
                "question": "Do low-cost airlines accept large dogs?",
                "answer": "No. Most European and US low-cost carriers (easyJet, Ryanair, Jet2, Wizz Air, Spirit, Frontier, and Allegiant) do not accept pets in the hold. This means large dogs have very limited direct flight options if you want to use budget carriers. For international large dog transport, full-service airlines or dedicated cargo carriers are the only realistic options."
            },
            {
                "question": "What is the maximum weight for a dog to fly as excess baggage vs cargo?",
                "answer": "Most airlines accept dogs as excess baggage (booked alongside a passenger ticket) when the combined weight of dog plus crate is under 32 to 45 kg, depending on the carrier. Heavier combinations (typically over 45 kg combined) move to manifest cargo, which is handled by the airline's cargo division rather than the passenger check-in team. Cargo bookings are separate from passenger bookings and often have different lead times."
            }
        ],
        "body": """Large dog owners have fewer airline options than owners of small dogs, but there are plenty of good carriers willing to take big dogs if you plan properly. Here is a practical overview of who accepts large dogs and how the logistics work.

## Full-service carriers that accept large dogs

**Lufthansa:** One of the most accommodating major carriers for large dogs. Accepts dogs as hold baggage (up to 32 kg combined in crate) and as cargo (up to 75 kg combined via Lufthansa Cargo). Operates an extensive network from Frankfurt, Munich, and other German hubs.

**British Airways:** Accepts dogs as checked baggage on some routes and as cargo via BA World Cargo. No pets in the hold on certain route types (some long-haul leisure routes). Check the specific route.

**Air France / KLM:** Both carriers accept large dogs as hold baggage and cargo. Air France Cargo and Martinair (KLM's cargo arm) have active live animal programmes.

**Singapore Airlines:** Accepts live animals as cargo through Singapore Airlines Cargo. No pets in the cabin on any route. Extensive network through Changi Airport (SIN).

**Qantas:** Accepts dogs as checked baggage on domestic Australian routes and as cargo on international routes. Live animal cargo through Qantas Freight.

**Emirates SkyCargo:** Emirates does not accept pets in cabin on any commercial flight. Emirates SkyCargo accepts dogs as live animal cargo from Dubai (DXB). Extensive global network.

**American Airlines / United Airlines / Delta:** All three US major carriers accept large dogs in the hold as checked baggage or cargo, subject to temperature restrictions and route availability.

**Etihad Cargo:** Live animal cargo service via Abu Dhabi (AUH). Accepts dogs. No cabin pets on Emirates or Etihad commercial services.

## Low-cost carriers: not an option for large dogs

easyJet, Ryanair, Jet2, Wizz Air (UK and EU low-cost carriers) do not accept pets in the hold, only guide dogs in cabin. Spirit, Frontier, and Allegiant in the USA similarly do not accept pets in the hold.

If you are on a budget and need to move a large dog internationally, you will need to use a full-service carrier for at least the pet's flight, even if you yourself fly on a budget carrier.

## Seasonal embargoes

Most airlines that accept dogs impose temperature restrictions during summer and winter. If the outdoor temperature at any point on the route exceeds 29 degrees Celsius or falls below 10 degrees Celsius, many carriers will refuse to load live animals. This particularly affects summer US domestic routes and winter northern European routes.

Book flexibility around these windows and check the airline's specific temperature policy before confirming travel dates.
"""
    },
]


FRONTMATTER_TEMPLATE = """\
---
title: "{title}"
description: "{description}"
date: "{date}"
type: "blog"
author: "PetTransportGlobal Editorial Team"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{title}"
  description: "{description}"
tags:
{tags_yaml}
faqs:
{faqs_yaml}
---

{body}
"""


def build_tags_yaml(tags):
    lines = []
    for t in tags:
        lines.append("  - \"{}\"".format(t))
    return "\n".join(lines)


def build_faqs_yaml(faqs):
    lines = []
    for faq in faqs:
        q = faq["question"].replace('"', '\\"')
        a = faq["answer"].replace('"', '\\"')
        lines.append("  - question: \"{}\"".format(q))
        lines.append("    answer: \"{}\"".format(a))
    return "\n".join(lines)


def write_article(article):
    slug = article["slug"]
    filepath = os.path.join(BLOG_DIR, slug + ".md")
    if os.path.exists(filepath):
        return "skipped", slug

    tags_yaml = build_tags_yaml(article["tags"])
    faqs_yaml = build_faqs_yaml(article["faqs"])
    body = article["body"].strip()

    content = FRONTMATTER_TEMPLATE.format(
        title=article["title"],
        description=article["description"],
        date=article["date"],
        slug=slug,
        tags_yaml=tags_yaml,
        faqs_yaml=faqs_yaml,
        body=body,
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return "written", slug


def main():
    written = []
    skipped = []
    for article in ARTICLES:
        status, slug = write_article(article)
        if status == "written":
            written.append(slug)
        else:
            skipped.append(slug)

    print("Written: {} | Skipped: {} | Total: {}".format(
        len(written), len(skipped), len(ARTICLES)
    ))
    if skipped:
        print("Skipped (already exist):")
        for s in skipped:
            print("  -", s)


if __name__ == "__main__":
    main()
