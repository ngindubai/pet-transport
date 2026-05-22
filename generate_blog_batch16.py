"""
Blog Batch 16 -- 22 new articles
Topics: Jordan + Finland country guides, route guides (UK-Nigeria, USA-Brazil, Germany-Canada,
        UK-Jordan, USA-Israel, AU-NZ), breed guides (German Shepherd, Corgi, Irish Setter,
        Westie, Standard Poodle), practical guides (crate measuring, connecting flights,
        what is an import permit, fearful dogs, crate labelling, stray dogs from abroad,
        how to read an airline pet policy, pet-friendly expat countries)
Run from repo root: python generate_blog_batch16.py
"""

import os

OUTPUT_DIR = os.path.join("site", "content", "blog")
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [
  {
    "slug": "jordan-pet-import-guide",
    "title": "Moving to Jordan with a Pet: Import Rules, Vaccinations and Amman Arrival",
    "description": "Guide to importing a dog or cat to Jordan. Ministry of Agriculture permit, rabies vaccine, health certificate requirements and what to expect at Queen Alia Airport.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Jordan", "import guide", "Middle East", "dog", "cat"],
    "body": """Jordan is a welcoming country for expatriates, and bringing a dog or cat is entirely possible with the right preparation. The process is managed by the Ministry of Agriculture and overseen by veterinary officers at Queen Alia International Airport in Amman.

## Jordan's Pet Import Requirements

The Ministry of Agriculture's Veterinary Directorate manages live animal imports. For dogs and cats entering Jordan, the requirements typically include:

- An import permit from the Ministry of Agriculture (apply before travel; allow two to four weeks)
- A health certificate issued by a government-accredited veterinarian in your country, within ten days of travel
- Rabies vaccination (current and valid on arrival; must have been given at least thirty days before travel for first vaccinations)
- Core vaccinations for dogs (distemper, parvovirus, hepatitis) and cats (herpesvirus, calicivirus, panleukopenia)
- Microchip (ISO 11784/11785)
- External and internal parasite treatment records

A rabies titre test is not a standard requirement for Jordan, but confirm the current position with the Ministry when applying for the import permit, as requirements can be updated.

## Applying for the Import Permit

Apply to the Jordanian Ministry of Agriculture Veterinary Directorate before travel. Some owners use a local Amman-based pet transport agent to handle the permit application, particularly if language or administrative delays are a concern.

## Flying into Amman

Queen Alia International Airport (AMM) is Jordan's main international gateway. Royal Jordanian accepts live animals on applicable routes and is the natural carrier for Amman-bound pet shipments. Emirates, Qatar Airways, Turkish Airlines, and Lufthansa also serve Amman and have live animal cargo programmes.

On arrival, veterinary officers at AMM inspect all live animal shipments. Have your import permit, health certificate, vaccination records, and microchip documentation in a single folder.

## Breed Restrictions

Jordan restricts the import of several dog breeds considered dangerous, including pit bull types and other breeds on the prohibited list. Confirm whether your breed is permitted when you apply for the import permit.

## Summary Checklist

- Import permit from Jordan Ministry of Agriculture
- Microchip
- Rabies vaccination (current, 30+ days before travel for first vaccine)
- Core vaccinations
- Health certificate within 10 days of departure
- Breed clearance confirmed
""",
    "faqs": [
      {"q": "Does Jordan require a rabies titre test for pet import?", "a": "A rabies titre test is not a standard requirement for importing a dog or cat into Jordan. A current rabies vaccination and Ministry of Agriculture import permit are the primary requirements. Confirm the current rules for your origin country with the Jordanian Ministry of Agriculture Veterinary Directorate when applying for the import permit."},
      {"q": "Which airline is best for flying a pet to Amman?", "a": "Royal Jordanian is Jordan's national carrier and accepts live animals on applicable international routes. Emirates, Qatar Airways, Turkish Airlines, and Lufthansa also serve Queen Alia International Airport (AMM) and have live animal cargo programmes. Contact the cargo team of your chosen carrier to confirm availability and make the booking."},
      {"q": "Are there breed restrictions for dogs entering Jordan?", "a": "Yes. Jordan prohibits the import of certain dog breeds considered dangerous, including pit bull types. Confirm whether your breed is permitted by contacting the Ministry of Agriculture Veterinary Directorate before beginning any import preparations. Do this as the first step, before any permits, vaccinations, or bookings."}
    ]
  },
  {
    "slug": "finland-pet-import-guide",
    "title": "Bringing a Pet to Finland: EU Rules, Rabies Vaccines and the Finnish Process",
    "description": "Finland is an EU member with strict rabies-prevention standards. This guide covers microchip, vaccination, tapeworm treatment and health certificate requirements for pet import.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Finland", "import guide", "Europe", "EU", "dog", "cat"],
    "body": """Finland is an EU member state but has a special status when it comes to tapeworm prevention. It is one of the few EU countries that requires a tapeworm treatment before entry for dogs -- a requirement that catches many owners out.

## EU Rules Apply, Plus Finnish Extras

For pets travelling within the EU or from third countries, the standard EU requirements apply:
- Microchip (ISO 11784/11785)
- Valid rabies vaccination
- EU animal health certificate (or the equivalent third-country certificate recognised by the EU)

For pets entering Finland specifically from EU countries, the additional Finnish tapeworm requirement applies for dogs: a treatment with praziquantel must be given by a vet no more than five days and no fewer than twenty-four hours before arrival in Finland. This rule applies when entering Finland from any EU country except Sweden.

## Arriving from Outside the EU (Third Countries)

For pets arriving in Finland from non-EU countries such as the UK, USA, or Australia, the standard EU third-country import requirements apply:
- For the UK: pets need a Finnish/EU animal health certificate endorsed by APHA (the UK-Finland route is a third-country import since Brexit)
- For the USA: USDA APHIS-endorsed health certificate meeting EU standards
- Rabies vaccination requirements: if coming from a high-risk country, a rabies titre test may be required before EU entry

Finland is a rabies-free country. The strict tapeworm and rabies controls reflect its biosecurity priorities.

## Flying into Helsinki

Helsinki-Vantaa Airport (HEL) is Finland's main international airport. Finnair is the national carrier and has an established live animal cargo programme -- Finnair is the natural choice for Helsinki-bound pet shipments. Lufthansa, British Airways, and Norwegian also serve Helsinki.

## Practical Notes

Finland has a cold climate with long, dark winters. For breeds sensitive to cold, ensure your crate has appropriate bedding. For warm-weather breeds, consult your vet about acclimatisation.

Veterinary care in Finland is excellent. Helsinki has multiple well-equipped veterinary hospitals, and care standards in rural areas are also high.

## Summary Checklist

- Microchip
- Valid rabies vaccination (meeting EU requirements for your origin country)
- Tapeworm treatment for dogs (by vet, 24 hours to 5 days before Finland arrival -- required from all EU countries except Sweden)
- EU-format or third-country health certificate (within 10 days of travel)
- Titre test if arriving from a high-risk rabies country
""",
    "faqs": [
      {"q": "Does my dog need a tapeworm treatment to enter Finland?", "a": "Yes. Dogs entering Finland from any EU country (except Sweden) must receive a tapeworm treatment using praziquantel, administered by a vet no more than five days and no fewer than twenty-four hours before arrival. This is a Finnish-specific requirement on top of the standard EU pet travel rules. Dogs from third countries (including the UK and USA) are subject to this requirement if transiting through the EU or entering Finland directly."},
      {"q": "What is the difference between EU pet travel rules and Finnish rules?", "a": "EU pet travel rules apply throughout the EU: microchip, valid rabies vaccination, and an EU animal health certificate. Finland adds a specific tapeworm treatment requirement for dogs. Finland is also rabies-free, which means it strictly enforces rabies vaccination requirements and may require a titre test for pets from high-risk origin countries."},
      {"q": "Which airline is best for flying a pet to Helsinki?", "a": "Finnair is Finland's national carrier and has an established live animal cargo programme. It is the most natural choice for Helsinki-Vantaa (HEL) bound pet shipments. British Airways, Lufthansa, and Norwegian also serve Helsinki. Contact the cargo team of your chosen carrier to confirm availability."}
    ]
  },
  {
    "slug": "uk-to-nigeria-pet-transport-guide",
    "title": "Pet Transport from UK to Nigeria: NAFDAC Permits, Airlines and the Process",
    "description": "Guide to shipping a dog or cat from the UK to Nigeria. NAFDAC veterinary import permit, APHA health certificate, rabies requirements and airlines flying pets to Lagos.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["UK", "Nigeria", "route guide", "dog", "cat", "West Africa"],
    "body": """Nigeria is home to a significant expatriate community, and British residents relocating to Lagos or Abuja increasingly want to bring their pets. The process works, but it needs a specialist -- the paperwork for Nigeria is specific and the airline options require careful planning.

## What Nigeria Requires from UK-Origin Pets

The National Agency for Food and Drug Administration and Control (NAFDAC) oversees veterinary import permits in Nigeria. Requirements for dogs and cats arriving from the UK include:

- A veterinary import permit from NAFDAC (apply before travel)
- An APHA-endorsed health certificate from a UK vet, issued within ten days of departure
- Rabies vaccination (current and valid on arrival)
- Core vaccinations (distemper, parvovirus, hepatitis for dogs; herpesvirus, calicivirus, panleukopenia for cats)
- External and internal parasite treatment records
- Microchip (ISO 11784/11785)

A rabies titre test is not routinely required for Nigerian import from the UK, but confirm the current requirements when applying for the NAFDAC permit.

## Getting the NAFDAC Import Permit

Apply to NAFDAC before travel. The process is best managed through a Lagos-based pet transport specialist who knows the NAFDAC application requirements. Allow at least three to four weeks for the permit.

## Airlines from UK to Nigeria

Most pet cargo on this route travels via a hub connection. Common options:
- **British Airways via London Heathrow to Lagos (LOS)**: British Airways serves Lagos Murtala Muhammed International Airport and has live animal cargo. Contact British Airways Cargo directly.
- **Virgin Atlantic to Lagos**: Virgin Atlantic also serves LOS. Confirm live animal cargo acceptance with their cargo team.
- **Ethiopian Airlines via Addis Ababa**: A practical routing for cargo, with Ethiopian's strong Africa network.
- **Kenya Airways via Nairobi**: Another Africa-hub option with live animal capability.

Avoid routings that involve multiple tight connections -- cargo live animal space is limited and delays can cause problems at transit points.

## Practical Notes for Lagos and Abuja

Veterinary care in Lagos and Abuja has improved significantly. Several international-standard clinics serve expatriate residents. Bring a supply of any ongoing prescription medications.

Nigeria's climate is hot and humid. Tick and heartworm prevention is important from day one. Brachycephalic breeds are at higher risk in this heat.

## Summary Checklist

- NAFDAC import permit (3-4 weeks lead time)
- APHA-endorsed health certificate, within 10 days of departure
- Rabies vaccination (current)
- Core vaccinations
- Parasite treatments
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "What is NAFDAC and do I need a permit to import a pet to Nigeria?", "a": "NAFDAC is the National Agency for Food and Drug Administration and Control in Nigeria. It oversees veterinary import permits for live animals entering the country. Yes, you need a NAFDAC veterinary import permit before bringing a dog or cat into Nigeria. Apply at least three to four weeks before your travel date. A Lagos-based pet transport specialist can help manage the application."},
      {"q": "Which airlines fly pets from the UK to Lagos?", "a": "British Airways and Virgin Atlantic both serve Lagos Murtala Muhammed International Airport (LOS) from London and have live animal cargo programmes. Ethiopian Airlines via Addis Ababa and Kenya Airways via Nairobi are also used for UK-Nigeria pet cargo. Contact the cargo team of your chosen carrier directly to confirm availability and make the booking."},
      {"q": "Does Nigeria require a rabies titre test for pets from the UK?", "a": "A rabies titre test is not a standard requirement for dogs and cats arriving in Nigeria from the UK. A current rabies vaccination and NAFDAC-issued import permit are the primary requirements. Confirm the current rules when applying for your import permit, as NAFDAC requirements can be updated."}
    ]
  },
  {
    "slug": "usa-to-brazil-pet-transport-guide",
    "title": "Pet Transport from USA to Brazil: MAPA Requirements, Airlines and the São Paulo Process",
    "description": "Moving a dog or cat from the USA to Brazil. MAPA veterinary certificate, USDA APHIS endorsement, import permit process and which airlines fly pets to São Paulo and Rio.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["USA", "Brazil", "route guide", "dog", "cat", "South America"],
    "body": """Brazil is home to millions of expatriates, and the USA-Brazil corridor is one of the busiest international relocation routes in the Americas. Bringing a pet from the USA to São Paulo or Rio de Janeiro is straightforward when the paperwork is done correctly.

## Brazil's Requirements for US-Origin Pets

Brazil's Ministry of Agriculture, Livestock and Food Supply (MAPA) regulates live animal imports through the Secretary of Agriculture. For dogs and cats from the USA, the requirements are:

- A health certificate (Certificado Veterinario Internacional or CVI) issued by a USDA APHIS-accredited vet and endorsed by USDA APHIS
- Rabies vaccination (current; given at least thirty days and no more than one year before travel)
- Core vaccinations for dogs: distemper, parvovirus, hepatitis, parainfluenza, and leptospirosis
- Core vaccinations for cats: herpesvirus, calicivirus, and panleukopenia
- Internal parasite treatment within a specific window before travel (typically within seven days of departure)
- External parasite treatment (flea/tick) within a specific window before travel
- Microchip (ISO 11784/11785 strongly recommended)

A rabies titre test is not required for pets from the USA. Brazil's import requirements are well-defined and LATAM Airlines, as the dominant carrier on this route, has processed countless pet shipments to Brazil.

## The USDA APHIS Endorsement

The health certificate must be signed by a USDA APHIS-accredited vet and then endorsed by USDA APHIS. The APHIS endorsement can take several days by mail, or can be done same-day at an APHIS office. Plan this carefully so the endorsed certificate is in hand within ten days of your departure date.

## Airlines from USA to Brazil

LATAM Airlines is the dominant carrier on US-Brazil routes and has a strong live animal cargo programme for South America. Key routes:
- **LATAM from Miami (MIA) to São Paulo (GRU)**: Most common routing for USA-Brazil pet cargo
- **American Airlines from Miami or New York to São Paulo**: American serves GRU with live animal cargo
- **United Airlines from Newark (EWR) or Houston (IAH) to São Paulo**: United also serves GRU

São Paulo Guarulhos International (GRU) handles most pet cargo. Rio de Janeiro Santos Dumont (SDU) and Galeão (GIG) also receive international shipments.

## Practical Notes

Brazil has an excellent veterinary care system in major cities. São Paulo and Rio have international-standard clinics. Bring a supply of any prescription medications and carry your pet's vaccination records as Brazilian vets will want to see them.

The climate varies widely across Brazil. São Paulo has a mild subtropical climate, while Rio is tropical and humid. Parasite prevention (heartworm, ticks, fleas) is essential from arrival.

## Summary Checklist

- USDA APHIS-endorsed health certificate, within 10 days of departure
- Rabies vaccination (30 days to 1 year before travel)
- Core vaccinations for dogs and cats
- Internal parasite treatment within 7 days of departure
- External parasite treatment within specified window
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "Does Brazil require a titre test for dogs from the USA?", "a": "No. Brazil does not require a rabies titre test for dogs and cats from the USA. A current USDA APHIS-endorsed health certificate confirming a valid rabies vaccination is sufficient. The certificate must be issued within ten days of departure and endorsed by USDA APHIS."},
      {"q": "Who endorses the health certificate for Brazil from the USA?", "a": "The health certificate for Brazil must be signed by a USDA APHIS-accredited veterinarian and then endorsed by USDA APHIS. The endorsement can be done at a USDA APHIS office (same-day) or by mail (several days). Plan the timing so the endorsed certificate is ready and the ten-day validity window covers your departure date."},
      {"q": "Which airlines fly pets from the USA to São Paulo?", "a": "LATAM Airlines (via Miami), American Airlines (via Miami or New York), and United Airlines (via Newark or Houston) all serve São Paulo Guarulhos International (GRU) and accept live animal cargo. LATAM Airlines has particularly extensive experience with pet shipments to Brazil. Contact the cargo team of your chosen carrier to book the live animal space."}
    ]
  },
  {
    "slug": "germany-to-canada-pet-transport-guide",
    "title": "Pet Transport from Germany to Canada: CFIA Requirements, Airlines and the Process",
    "description": "Moving a dog or cat from Germany to Canada. CFIA import rules, EU health certificate, rabies vaccination and which airlines fly pets on Frankfurt-Toronto routes.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Germany", "Canada", "route guide", "dog", "cat"],
    "body": """Germany to Canada is a well-travelled expat route, and the pet import requirements are relatively manageable compared to some other German relocation destinations. Canada's CFIA keeps the requirements for EU-origin pets straightforward.

## Canada's Requirements for German Pets

The Canadian Food Inspection Agency (CFIA) regulates pet imports. For dogs and cats from Germany, the requirements are:

- For dogs: a rabies vaccination that is current and valid on arrival (given at least thirty days before travel for first-time vaccinations)
- For cats: no rabies vaccination requirement from CFIA (Canada does not require it for cats from low-risk countries like Germany)
- A health certificate is not strictly required by CFIA for German pets, but your airline will require one for the cargo booking
- Microchip is not required by CFIA but is strongly recommended and required by most airlines

The relatively light CFIA requirements are offset by the airline documentation requirements, which are often more demanding. The German EU health certificate satisfies the airline documentation requirement and is worth preparing even if CFIA does not strictly require it.

## German Health Certificate (EU Format)

For dogs, a standard EU health certificate endorsed by the official government veterinary authority in Germany (the local Veterinary Office, or Veterinaramt) confirms vaccination status and health. This certificate is recognised by CFIA and by airlines as documentation of the dog's health and rabies vaccination.

Allow time for the Veterinaramt endorsement process -- typically two to four days after the vet appointment.

## Airlines from Germany to Canada

Lufthansa is the primary carrier for Frankfurt (FRA) to Canada routes and has a well-established live animal cargo programme:
- Frankfurt to Toronto (YYZ)
- Frankfurt to Vancouver (YVR)
- Frankfurt to Montreal (YUL)

Air Canada from Frankfurt also accepts live animal cargo on applicable routes. Confirm live animal availability on your specific flight when booking.

## Practical Notes

Canada has excellent veterinary care in all major cities. Toronto, Vancouver, and Montreal all have international-standard veterinary hospitals.

If you are relocating to Quebec, be aware that French-language versions of some documents may be requested. An English-and-French bilingual health certificate is advisable for Montreal-bound shipments.

## Summary Checklist

- EU health certificate (Veterinaramt-endorsed) for dogs
- Rabies vaccination for dogs (current, 30+ days before travel for first vaccine)
- Microchip
- IATA-compliant crate
- Confirm airline cargo booking (Lufthansa or Air Canada cargo teams)
""",
    "faqs": [
      {"q": "Does a dog from Germany need a health certificate to enter Canada?", "a": "CFIA does not strictly require a health certificate for dogs from Germany, but your airline will require one for the cargo booking. An EU-format health certificate endorsed by the German Veterinaramt (Veterinary Office) satisfies both the airline requirement and serves as documentation of the dog's rabies vaccination and general health. Allow two to four days for the Veterinaramt endorsement."},
      {"q": "Does my cat need a rabies vaccination to enter Canada from Germany?", "a": "CFIA does not require a rabies vaccination for cats from Germany, which is a low-risk origin. However, your airline may require it for their own documentation. Check with your airline cargo team when booking. It is good practice to keep your cat's vaccinations current regardless of the specific entry requirement."},
      {"q": "Which airlines fly pets from Germany to Canada?", "a": "Lufthansa operates Frankfurt (FRA) to Toronto (YYZ), Vancouver (YVR), and Montreal (YUL) with an established live animal cargo programme. Air Canada from Frankfurt also accepts live animals on applicable routes. Contact the Lufthansa Cargo or Air Canada Cargo team directly to book the live animal space."}
    ]
  },
  {
    "slug": "uk-to-jordan-pet-transport-guide",
    "title": "Pet Transport from UK to Jordan: Ministry Permit, APHA Certificate and Amman Routes",
    "description": "Guide to shipping a dog or cat from the UK to Jordan. Ministry of Agriculture import permit, APHA health certificate, rabies vaccination and airlines serving Amman.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["UK", "Jordan", "route guide", "dog", "cat", "Middle East"],
    "body": """Jordan is a Middle Eastern destination increasingly popular with UK expats and development sector workers. Moving a dog or cat from the UK to Amman is manageable with around three months of preparation.

## What Jordan Requires from UK-Origin Pets

The Jordanian Ministry of Agriculture Veterinary Directorate manages live animal imports. For dogs and cats from the UK, the requirements include:

- An import permit from the Ministry of Agriculture
- An APHA-endorsed health certificate from a UK vet, within ten days of departure
- Rabies vaccination (current; given at least thirty days before travel)
- Core vaccinations for dogs and cats
- Microchip (ISO 11784/11785)
- External and internal parasite treatment records
- Breed clearance (certain breeds restricted -- confirm for your dog)

A rabies titre test is not a standard requirement for Jordan from the UK, but confirm when applying for the import permit.

## The UK Health Certificate Process

Since Brexit, UK pets travelling to non-EU countries need a health certificate specific to the destination country's requirements. For Jordan, this means a vet issues the certificate in the format approved by Jordan, and APHA endorses it. Use a vet familiar with the APHA endorsement process for Middle Eastern destinations.

## Airlines from UK to Jordan

Royal Jordanian operates direct flights from London Heathrow (LHR) to Amman Queen Alia (AMM) and is the most direct option for pet cargo. British Airways also serves Amman. Emirates via Dubai and Qatar Airways via Doha are common connecting options.

Contact Royal Jordanian Cargo or British Airways Cargo to book the live animal space. Confirm that the specific aircraft on your route accepts live animals in the hold.

## Practical Notes for Amman

Veterinary care in Amman has improved significantly and several English-speaking clinics serve the expatriate community. Bring a stock of any prescription medications. Jordan's climate is hot and dry, with cooler winters. Parasite prevention is important year-round.

## Summary Checklist

- Import permit from Jordan Ministry of Agriculture
- APHA-endorsed health certificate, within 10 days of departure
- Rabies vaccination (current)
- Core vaccinations
- Breed clearance confirmed
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "How long does it take to prepare a pet for relocation from the UK to Jordan?", "a": "For most dogs and cats from the UK, the Jordan import process takes around six to eight weeks. You need the import permit from the Jordanian Ministry of Agriculture, a current rabies vaccination given at least thirty days before travel, and an APHA-endorsed health certificate within ten days of departure. Starting two months before your planned travel date gives comfortable buffer."},
      {"q": "Do I need an APHA endorsement on the health certificate for Jordan?", "a": "Yes. Since Brexit, UK health certificates for non-EU destinations must be endorsed by APHA (Animal and Plant Health Agency). The vet issues the certificate in the destination-country format, and APHA endorses it. Allow several days for the APHA endorsement process on top of the vet appointment. Time this so the endorsed certificate is valid within ten days of your travel date."},
      {"q": "Which airline is best for flying a pet from London to Amman?", "a": "Royal Jordanian operates direct London Heathrow (LHR) to Amman Queen Alia (AMM) flights and is the most direct option for pet cargo on this route. British Airways also serves Amman. Emirates via Dubai and Qatar Airways via Doha are connecting alternatives. Contact Royal Jordanian Cargo or British Airways Cargo directly to book the live animal space."}
    ]
  },
  {
    "slug": "australia-to-new-zealand-pet-transport-guide",
    "title": "Pet Transport from Australia to New Zealand: The Trans-Tasman Rules",
    "description": "Moving a dog or cat from Australia to New Zealand. MPI biosecurity requirements, the approved pathway, approved carriers and what the quarantine process looks like.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Australia", "New Zealand", "route guide", "dog", "cat"],
    "body": """Australia and New Zealand are close neighbours but biosecurity rivals -- both are rabies-free, both are islands, and both guard their disease-free status fiercely. The AU-NZ route for pets involves a process far more rigorous than the two-hour flight would suggest.

## New Zealand's Requirements for Australian Pets

New Zealand's Ministry for Primary Industries (MPI) manages all live animal imports. New Zealand is one of the most demanding destinations in the world for pet imports, even from Australia. The pathway for Australian-origin dogs and cats involves:

- An approved import pathway from MPI (confirm your specific origin state qualifies)
- Microchip (ISO 11784/11785)
- Rabies vaccination: Australia is rabies-free, so the standard process differs from rabies-risk countries. For Australian dogs and cats, a different import pathway applies focused on other disease risks
- Health certificate from an APVMA-approved vet in Australia, endorsed by DAFF
- A ten-day isolation period in New Zealand at an MPI-approved facility on arrival
- Pre-arrival inspection requirements

Unlike most countries, New Zealand's requirements for Australian pets include a mandatory minimum ten-day isolation period even though Australia is also rabies-free. This is to address other disease risks (notably Hendra virus exposure history for dogs in some regions).

## The Approved Import Health Standard

MPI publishes Import Health Standards (IHS) for each species and origin country. The IHS for dogs and cats from Australia is the document you need to follow precisely. Download the current version from mpi.govt.nz and work through it with your vet.

## Airlines for Australia to New Zealand

Air New Zealand and Qantas dominate the Trans-Tasman route. Both have live animal cargo programmes. Common city pairs:
- Sydney (SYD) to Auckland (AKL)
- Melbourne (MEL) to Auckland (AKL) or Christchurch (CHC)
- Brisbane (BNE) to Auckland (AKL)

Contact Air New Zealand Cargo or Qantas Freight to book the live animal space. The Trans-Tasman is a popular route so book well in advance.

## The Isolation Facility

On arrival in New Zealand, your pet goes to an MPI-approved isolation facility. The ten-day stay is at your cost. Costs vary but are typically NZD 1,500 to NZD 2,500 for a standard dog or cat.

## Summary Checklist

- Confirm current MPI Import Health Standard for dogs/cats from Australia
- DAFF-endorsed health certificate from approved Australian vet
- Microchip
- Book MPI-approved isolation facility in advance
- Book Air New Zealand Cargo or Qantas Freight space
- Allow 6-8 weeks minimum preparation from starting the process
""",
    "faqs": [
      {"q": "Is there a quarantine period for pets moving from Australia to New Zealand?", "a": "Yes. All dogs and cats arriving in New Zealand, including those from Australia, must undergo a mandatory ten-day isolation period at an MPI-approved facility. The cost is borne by the owner and is typically NZD 1,500 to NZD 2,500. The isolation facility must be booked in advance before travel."},
      {"q": "Do Australian dogs and cats need a rabies vaccination for New Zealand?", "a": "Australia is a rabies-free country, so the rabies vaccination requirement for New Zealand applies differently than for pets from rabies-risk origins. The MPI Import Health Standard for dogs and cats from Australia outlines the specific requirements. Download the current version from mpi.govt.nz and work through it with your vet well in advance."},
      {"q": "Which airlines fly pets from Australia to New Zealand?", "a": "Air New Zealand and Qantas both serve the Trans-Tasman route extensively and have live animal cargo programmes. Air New Zealand Cargo and Qantas Freight are the primary booking contacts. Popular city pairs include Sydney-Auckland, Melbourne-Auckland, and Brisbane-Auckland. Book the cargo space well in advance as Trans-Tasman flights are often full."}
    ]
  },
  {
    "slug": "travelling-with-a-german-shepherd-internationally",
    "title": "International Travel with a German Shepherd: Rules, Breed Checks and Key Routes",
    "description": "German Shepherds face breed restrictions in some countries. This guide covers where GSDs are allowed, crate sizing, airline policies and key international routes for GSD owners.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["German Shepherd", "breed guide", "travel", "dog"],
    "body": """German Shepherds are one of the most popular dog breeds in the world, and GSD owners relocate internationally in large numbers. The breed is not universally restricted, but it does appear on banned breed lists in a small number of countries and faces airline scrutiny because of its size. Here is what GSD owners need to know.

## Breed Restrictions for German Shepherds

German Shepherds are not commonly subject to breed-specific legislation, but they appear on some countries' import-review lists as a "guard dog" or "large breed" requiring additional scrutiny. The key problematic destinations:

- **Ukraine** (pre-conflict rules): required special documentation for GSDs
- **Some municipalities in Denmark**: breed-specific legislation in Denmark has historically included German Shepherds in some local rules -- confirm with local authorities
- **Some Gulf municipalities**: while UAE, Qatar, and Saudi Arabia do not nationally ban German Shepherds, some residential compounds and housing authorities have their own pet restrictions

For the overwhelming majority of international destinations, German Shepherds face no breed-specific ban at the national level. Always confirm with your destination country's veterinary authority as rules can change.

## Airline Policies for German Shepherds

German Shepherds are a large breed (typically 22 to 40 kg) and will always travel as hold cargo on international flights. No airline accepts a standard adult GSD in the passenger cabin.

Some airlines have specific policies about "working dog" or "guard dog" breeds and may require additional documentation. Contact your airline's cargo team to confirm acceptance. Airlines that explicitly accept GSDs on applicable routes include Lufthansa, British Airways, Emirates, and Qatar Airways.

## Crate Sizing

German Shepherds vary considerably in size. Measure your specific dog:
- A small female GSD (22-27 kg) typically needs an IATA size 4 crate
- A large male GSD (30-40 kg) typically needs an IATA size 5 crate

The crate must be tall enough for your dog to stand at full height with ears up, long enough to lie down fully, and wide enough to turn around.

## Key Routes for German Shepherd Owners

- **Germany to USA**: Natural route. Lufthansa cargo direct. USDA APHIS health certificate required on arrival.
- **UK to Australia**: Full DAFF process. GSDs are not on Australia's restricted breed list. Allow 8-10 months.
- **Germany to Australia**: Same DAFF process. Allow 8-10 months.
- **UK to UAE**: UAE import permit required. German Shepherds are not prohibited in UAE at national level, but confirm housing rules at your destination.

## Preparing a Working Breed for Cargo

German Shepherds are intelligent, alert dogs and can be sensitive to disruption. Crate training is particularly important. Begin three to four months before the move, working up to extended crate sessions of four to six hours. A well-trained GSD in a familiar crate handles hold travel well.

Do not leave any collar, harness, or leads inside the crate -- these are strangulation hazards. Use a breakaway ID tag attached to the crate exterior.
""",
    "faqs": [
      {"q": "Are German Shepherds banned in any country?", "a": "German Shepherds are not banned at the national level in any major international destination we are aware of. They may appear on breed scrutiny lists in a small number of jurisdictions (some Danish municipalities historically included GSDs in local regulations). Always confirm with your destination country's authorities. For Gulf destinations, check both national rules and local housing compound rules."},
      {"q": "What crate size does a German Shepherd need for international travel?", "a": "A small female German Shepherd typically needs an IATA-compliant size 4 crate. A larger male may need a size 5. Measure your dog's standing height (nose to top of head), length (nose to base of tail), and width across the shoulders. The crate must allow the dog to stand, lie down naturally, and turn around. Do not rely on breed averages -- individual dogs vary considerably."},
      {"q": "Which airlines accept German Shepherds as cargo?", "a": "Lufthansa, British Airways, Emirates, Qatar Airways, and most major international carriers accept German Shepherds as hold cargo on applicable routes. Contact the cargo team of your chosen airline to confirm acceptance and book the live animal space. GSDs are too large for in-cabin travel and will always travel in the temperature-controlled hold."}
    ]
  },
  {
    "slug": "travelling-with-a-corgi-internationally",
    "title": "International Travel with a Corgi: Breed Notes, Crate Sizing and Routes",
    "description": "Corgis are compact, sturdy dogs well-suited to international travel. This guide covers breed restrictions, in-cabin options, crate sizing and key routes for Corgi owners.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Corgi", "breed guide", "travel", "dog"],
    "body": """Pembroke Welsh Corgis and Cardigan Welsh Corgis are increasingly popular worldwide, and their compact size makes them practical travel companions. Here is what Corgi owners need to know about international moves.

## Breed Restrictions for Corgis

Corgis are not subject to breed-specific legislation in any country we are aware of. They do not appear on any banned or restricted breed lists. This makes international relocation notably uncomplicated from a breed-restriction perspective.

## Cabin or Hold?

Corgis typically weigh between 10 and 14 kg. Combined with a carrier, the total weight usually falls above the in-cabin limits of most airlines (typically 8 to 10 kg combined). Most adult Corgis travel in the temperature-controlled cargo hold on international routes.

A small Pembroke (10 kg or under) might qualify for in-cabin on certain European routes if the airline's limit is 10 kg combined -- but this is marginal. Always confirm the exact combined weight and the specific airline's limit before booking in-cabin travel.

For in-cabin, soft-sided carriers that fit under the seat are required. For hold travel, an IATA-compliant hard crate is needed.

## Crate Sizing for a Corgi

Most Corgis need an IATA-compliant size 3 crate for hold travel. Measure your specific dog:
- Corgis are long-bodied relative to their height -- the length dimension is often the determining factor
- A standard Pembroke needs a crate approximately 70 to 80 cm long, 50 cm wide, and 50 cm tall

Use your dog's actual measurements, not breed averages. A correctly sized crate -- snug enough for security but roomy enough for movement -- reduces travel stress.

## Key Routes for Corgi Owners

Corgis are particularly popular in the UK, Australia, Japan, and the USA. Common relocation routes:

- **UK to Australia**: Full DAFF process. Allow 8-10 months. No breed restrictions.
- **UK to Japan**: Japan's detailed AQS process applies. Allow 7-8 months.
- **USA to UK**: Standard APHA process. Rabies vaccination, tapeworm treatment, microchip.
- **Australia to UK**: Same APHA process as USA. Rabies vaccination not required as AU is rabies-free -- specific process applies.

## Preparing a Corgi for International Travel

Corgis are intelligent and adapt well to routine disruption. Crate training is still important -- a confident relationship with the crate significantly reduces flight stress.

Note that Corgis are prone to intervertebral disc disease (IVDD). On long-haul flights, the extended period of lying down is not typically problematic for healthy dogs, but if your Corgi has any back or mobility issues, discuss the planned journey with your vet before booking.
""",
    "faqs": [
      {"q": "Can a Corgi travel in the plane cabin?", "a": "Adult Corgis typically weigh 10-14 kg, which usually exceeds the in-cabin weight limits of most airlines when combined with a carrier. A small Corgi (10 kg or under) may qualify on some European routes with a 10 kg combined limit, but this is marginal. For most international travel, Corgis travel in the temperature-controlled hold. Confirm with your specific airline before booking."},
      {"q": "Are Corgis banned in any country?", "a": "Corgis are not banned or restricted in any country we are aware of. They do not appear on any dangerous dog legislation. This makes them one of the more straightforward breeds to relocate internationally."},
      {"q": "How much does it cost to fly a Corgi internationally?", "a": "International pet transport costs for a Corgi (typically travelling as hold cargo) vary by route, airline, and whether you use a specialist pet transport service. As a guide, expect USD 800 to USD 2,000 for the airline cargo fee alone on long-haul routes. A full-service pet transport company including documentation, crate, ground transport, and airline will cost more. Use our pet transport cost calculator for a route-specific estimate."}
    ]
  },
  {
    "slug": "travelling-with-an-irish-setter-internationally",
    "title": "International Travel with an Irish Setter: Size, Routes and Key Considerations",
    "description": "Irish Setters are large, energetic dogs. This guide covers breed restrictions, crate sizing, airline policies and the key international routes for Irish Setter owners moving abroad.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Irish Setter", "breed guide", "travel", "dog"],
    "body": """Irish Setters are beautiful, energetic dogs and, happily, they travel internationally without the breed-restriction complications that affect some other large breeds. The main challenges are size (they need big crates) and temperament preparation.

## Breed Restrictions

Irish Setters are not subject to breed-specific legislation in any country we are aware of. They are not classified as dangerous breeds anywhere and do not appear on any banned breed lists. International relocation for this breed is uncomplicated from a regulatory perspective.

## Hold Travel Only

Adult Irish Setters weigh between 27 and 32 kg. They always travel as hold cargo on international flights. There is no in-cabin option for this breed.

## Crate Sizing for an Irish Setter

Irish Setters are tall and long-bodied. Most need an IATA-compliant size 5 crate. The crate must allow the dog to:
- Stand at full head height (Irish Setters have long legs and a proud head carriage)
- Lie down fully stretched
- Turn around comfortably

Measure carefully. The typical Irish Setter needs a crate approximately 102 cm long, 71 cm wide, and 76 cm tall (size 500 in IATA notation). An undersized crate will be refused by the airline.

## Preparing an Energetic Breed for Cargo

Irish Setters are known for high energy and can be reactive to unfamiliar environments. Crate training is critical for this breed. An Irish Setter that has not been crate trained before travel day is likely to be stressed and distressed in a large unfamiliar crate.

Start crate training four to six months before the move. Feed all meals in the crate, use the crate as a rest space, and work up to four to six hour sessions with the door closed. A calm, confident association with the crate is the single most effective thing you can do for your dog's wellbeing on travel day.

Exercise your dog well on the morning of travel. A tired, well-exercised Irish Setter settles much faster in a crate than one that has not been exercised.

## Key Routes for Irish Setter Owners

Irish Setters are particularly common in the UK and Ireland. Common relocation routes:

- **UK to Australia**: Full DAFF process. No breed restrictions. Allow 8-10 months.
- **Ireland to USA**: USDA APHIS health certificate. Rabies vaccination required.
- **UK to USA**: Standard USDA APHIS process. APHA-endorsed health certificate.
- **Ireland to Australia**: Same DAFF process as UK. Allow 8-10 months.
""",
    "faqs": [
      {"q": "Are Irish Setters banned in any country?", "a": "Irish Setters are not banned or restricted in any country we are aware of. They are a sporting/gun dog breed and do not appear in any dangerous dog legislation. International relocation for Irish Setters is not complicated by breed restrictions."},
      {"q": "What crate size does an Irish Setter need for international travel?", "a": "Most adult Irish Setters need an IATA-compliant size 5 crate (approximately 102 x 71 x 76 cm). The crate must be tall enough for the dog to stand at full head height, long enough to lie down fully, and wide enough to turn around. Always measure your individual dog and confirm crate acceptance with your airline before purchasing or booking."},
      {"q": "How should I prepare my Irish Setter for a long cargo flight?", "a": "Start crate training four to six months before the move, working up to extended crate sessions of four to six hours. Exercise your dog well on the morning of travel. Do not feed for four hours before the flight. Do not sedate without veterinary advice. A familiar-smelling blanket or item in the crate helps. An Irish Setter that knows and trusts its crate handles cargo travel much better than one introduced to the crate for the first time on travel day."}
    ]
  },
  {
    "slug": "travelling-with-a-west-highland-terrier-internationally",
    "title": "International Travel with a West Highland Terrier (Westie)",
    "description": "West Highland Terriers are compact, fearless dogs that travel well. This guide covers breed restrictions, in-cabin options, crate sizing and key international routes for Westie owners.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["West Highland Terrier", "Westie", "breed guide", "travel", "dog"],
    "body": """West Highland White Terriers -- Westies -- are popular dogs in the UK, Europe, and North America, and their compact size makes them one of the more practical breeds for international travel. Here is what Westie owners need to know.

## Breed Restrictions

Westies are not subject to breed-specific legislation in any country we are aware of. They do not appear on any banned or restricted breed list. International travel for this breed is straightforward from a regulatory standpoint.

## Cabin or Hold?

Adult Westies typically weigh between 7 and 10 kg. Combined with a soft-sided carrier, the total weight is usually 9 to 12 kg. This puts them in borderline territory for in-cabin travel:

- On airlines with an 8 kg combined limit, most Westies will be too heavy for the cabin
- On airlines with a 10 kg combined limit (Lufthansa, Air France, KLM), a small Westie in a lightweight carrier may qualify

For long-haul routes (UK-Australia, UK-Japan, UK-USA), in-cabin is not available regardless of weight, and Westies travel as hold cargo.

## Crate Sizing

Westies travelling in the hold need an IATA-compliant size 2 or size 3 crate depending on your individual dog's dimensions. The crate must allow the dog to stand at full height, lie down, and turn around.

For in-cabin, a soft-sided carrier fitting under the seat (approximately 45 x 35 x 20 cm) is required. Confirm carrier dimensions with your airline before purchasing.

## Key Routes for Westie Owners

Westies are common in the UK, Ireland, and across Europe. Key relocation routes:

- **UK to Australia**: Full DAFF process. Allow 8-10 months. No breed restrictions.
- **UK to USA**: APHA-endorsed health certificate. USDA requirements on arrival.
- **UK to Canada**: CFIA requirements. Current rabies vaccination. Simpler process.
- **Europe to USA**: EU health certificate. USDA APHIS requirements on arrival.

## Westie-Specific Travel Notes

Westies are spirited and confident -- they adapt well to new environments. They are not brachycephalic, so they face none of the respiratory restrictions that affect flat-faced breeds. Their double coat provides some insulation, but for long-haul hold travel in a well-ventilated crate, temperature management is not a particular concern.

Westies can be prone to Westie lung disease (pulmonary fibrosis) in older dogs. If your Westie has any respiratory diagnosis, discuss the planned journey with your vet before booking -- this is not a reason to refuse travel, but your vet may want to assess fitness to fly.
""",
    "faqs": [
      {"q": "Can a West Highland Terrier travel in the plane cabin?", "a": "Westies weigh 7-10 kg as adults. Combined with a carrier, this often exceeds the in-cabin weight limit of many airlines. Small Westies may qualify for in-cabin on airlines with a 10 kg combined limit (such as Lufthansa or Air France on European routes). For long-haul international travel, hold cargo is the standard option. Always confirm with your specific airline."},
      {"q": "Are West Highland Terriers banned in any country?", "a": "West Highland Terriers are not banned or restricted in any country we are aware of. They are a small terrier breed and do not appear in any dangerous dog legislation. This makes them one of the more straightforward breeds to relocate internationally."},
      {"q": "How do I prepare a Westie for hold cargo travel?", "a": "Introduce the crate several months before travel. Feed meals in the crate, build up to extended closed-crate sessions, and ensure the crate is associated with positive experiences. On travel day, provide exercise before departure. Do not sedate without veterinary advice. A small familiar-scented item (a worn T-shirt) in the crate provides comfort during the journey."}
    ]
  },
  {
    "slug": "travelling-with-a-standard-poodle-internationally",
    "title": "International Travel with a Standard Poodle: Size, Routes and Key Considerations",
    "description": "Standard Poodles are large, intelligent dogs. This guide covers breed restrictions, crate sizing, airline policies and the key international routes for Standard Poodle owners.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Standard Poodle", "breed guide", "travel", "dog"],
    "body": """Standard Poodles are elegant, intelligent dogs that adapt well to new environments -- a useful trait when international travel is involved. The good news is that Standard Poodles are not subject to any breed restrictions. The practical challenge is their size.

## Breed Restrictions

Standard Poodles are not banned or restricted in any country we are aware of. They do not appear on any dangerous dog legislation or banned breed lists. International travel for this breed is uncomplicated from a regulatory standpoint.

Note: the Poodle's broad family (Toy, Miniature, Standard) is sometimes incorrectly flagged by airlines unfamiliar with brachycephalic breed lists. Poodles are not brachycephalic and should not be subject to flat-faced breed restrictions. If an airline questions this, your vet can confirm on the health certificate that your dog has a full nasal passage and no brachycephalic anatomy.

## Hold Travel

Standard Poodles typically weigh between 20 and 35 kg. They always travel as hold cargo on international flights.

## Crate Sizing

Most Standard Poodles need an IATA-compliant size 4 or size 5 crate depending on your dog's individual dimensions. Measure carefully:
- Poodles have a distinctive posture with a proud, upright head carriage -- measure standing height with the head in a natural upright position
- Long, slender legs mean the length and turning-circle dimensions are also important
- A 30 kg Standard Poodle typically needs a 102 x 69 x 74 cm crate (approximately IATA size 5)

## Key Routes

- **France to USA**: Natural route for this quintessentially French breed. Air France cargo direct from CDG.
- **UK to Australia**: Full DAFF process. Allow 8-10 months. No breed restrictions.
- **USA to UK**: APHA-endorsed health certificate, tapeworm treatment, microchip.
- **Europe to Canada**: CFIA requirements. Rabies vaccination for dogs. Straightforward.

## Preparing a Standard Poodle for Cargo Travel

Standard Poodles are highly intelligent and can be sensitive to routine changes. Early crate training (starting three to four months before travel) is the most effective preparation. Poodles that know and trust their crate adapt well to the cargo environment.

Groom your Poodle to a shorter, practical cut before travel rather than a full show clip -- long, dense grooming can become uncomfortably hot in a crate and may catch on crate fixtures.
""",
    "faqs": [
      {"q": "Are Standard Poodles banned in any country?", "a": "Standard Poodles are not banned or restricted in any country we are aware of. They are not brachycephalic and do not appear on any dangerous dog legislation. If an airline queries breed acceptance, note that Poodles have no brachycephalic anatomy and this can be confirmed on the health certificate."},
      {"q": "What crate size does a Standard Poodle need for international travel?", "a": "Most Standard Poodles need an IATA-compliant size 4 or 5 crate, depending on your individual dog's dimensions. Measure the dog's standing height with head upright, length from nose to tail base, and shoulder width. Allow 10 cm above the head, and choose the crate that meets all three dimensions. Do not undersize -- airlines reject crates too small for the animal."},
      {"q": "Can a Miniature or Toy Poodle travel in the cabin?", "a": "Yes -- Toy Poodles (typically 2-4 kg) and small Miniature Poodles (5-9 kg) often qualify for in-cabin travel on European and some international routes where the combined pet and carrier weight falls within the airline's limit (typically 8-10 kg). This guide focuses on Standard Poodles, which at 20-35 kg always travel as hold cargo."}
    ]
  },
  {
    "slug": "how-to-measure-your-dog-for-a-travel-crate",
    "title": "How to Measure Your Dog for an IATA Travel Crate",
    "description": "Getting the crate size wrong is one of the most common pet travel mistakes. This guide shows you exactly how to measure your dog for an IATA-compliant travel crate.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["crate", "IATA", "practical guide", "crate sizing"],
    "body": """The single most common pre-travel mistake for first-time pet shippers is getting the crate size wrong. An undersized crate is a welfare problem and will be rejected by the airline. An oversized crate can cause the dog to be thrown around during turbulence.

Here is how to measure your dog correctly.

## The Four Measurements You Need

**1. Height (A)**
Measure from the floor to the top of the dog's head when standing naturally. For dogs with upright ears (German Shepherds, Chihuahuas, Huskies), measure to the top of the ears, not the skull. Add 10 cm.

**2. Length (B)**
Measure from the tip of the nose to the base (not the tip) of the tail. Add 10 cm.

**3. Width (C)**
Measure the width across the widest point of the body (usually across the shoulders). Multiply by 2.

**4. Crate height and floor area**
- Minimum crate height = A (the height measurement including +10 cm)
- Minimum crate floor area = B x C

## The IATA Crate Size Chart

IATA crates are sized from 100 (smallest) to 700 (largest). The sizing is not perfectly standardised across manufacturers, so always check the specific dimensions of the crate you are buying against your measurements.

As a rough guide:
- **Size 1 (100)**: Toy breeds, cats under 4 kg
- **Size 2 (200)**: Cats 4-6 kg, small dogs 4-7 kg (Chihuahua, Shih Tzu, small Terriers)
- **Size 3 (300)**: Medium dogs 8-14 kg (Cocker Spaniel, Beagle, Westie, Corgi)
- **Size 4 (400)**: Larger dogs 14-25 kg (Labrador, Golden Retriever, Springer Spaniel)
- **Size 5 (500)**: Large dogs 25-40 kg (German Shepherd, Irish Setter, Labradoodle, Weimaraner)
- **Size 6-7 (600-700)**: Giant breeds (Great Dane, Irish Wolfhound, Saint Bernard)

These are guides only. Always check the actual dimensions.

## What Makes a Crate IATA-Compliant?

An IATA-compliant crate must have:
- A solid (not wire) base and roof
- Ventilation openings on at least three sides (not just the door)
- A secure spring-loaded door with a latch that can be opened from inside (important for emergency access)
- Water and food dishes accessible from outside without opening the door
- Rounded edges internally (no sharp projections)
- Absorbent bedding on the floor
- Clear labelling: "LIVE ANIMALS" on top and on at least one side, directional arrows, your contact information, feeding and watering instructions

## Where to Buy

IATA-compliant crates are available from major pet retailers (Petmate Compass, Vari-Kennel, Ferplast Atlas), specialist pet travel suppliers, and many pet transport companies supply them as part of a full-service package. Avoid cheap unbranded crates that claim IATA compliance but do not specify which edition of the IATA Live Animals Regulations they comply with.

## Crate Training After Purchase

Buy the crate at least two to three months before travel. Begin introducing it immediately. A dog that has spent months comfortable in its crate handles cargo travel far better than one experiencing the crate for the first time at the airport.
""",
    "faqs": [
      {"q": "What happens if my dog's crate is too small?", "a": "If the crate does not meet the minimum IATA size requirements for your dog, the airline will refuse to accept it. The animal cannot travel until a correct crate is provided. If this happens at the airport on travel day, it can result in a missed flight and significant costs. Always measure your dog and verify crate dimensions before travel day."},
      {"q": "Can I use a wire crate for air travel?", "a": "No. Wire crates are not IATA-compliant for hold travel. Live animals regulations require a solid (not wire-mesh) construction for the base, sides, and roof. Only the door and ventilation openings may have a wire or mesh element. If you are considering in-cabin travel on a shorter route, some airlines accept soft-sided carriers for cabin travel -- but the carrier must still fit under the seat."},
      {"q": "How do I measure a dog with very upright ears, like a German Shepherd or Husky?", "a": "For dogs with upright ears, measure to the top of the ear tips (not the skull), as this is the actual height the dog occupies when standing. Add 10 cm to this measurement for the minimum crate height. This is why German Shepherds and Siberian Huskies often need a taller crate than their body weight alone would suggest."}
    ]
  },
  {
    "slug": "pet-relocation-with-connecting-flights",
    "title": "Pet Transport on Connecting Flights: What Happens in Transit?",
    "description": "Most international pet shipments involve a connecting flight. This guide explains how pets are handled at transfer airports, what can go wrong and how to choose a safe routing.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["connecting flights", "transit", "practical guide", "cargo hold"],
    "body": """Most international pet shipments involve at least one connection. Your dog or cat spends time in transit between flights -- sometimes a few hours, sometimes overnight. Understanding what happens during those connections helps you choose the right routing and avoid the situations that cause the most problems.

## How Pets Are Handled in Transit

When a live animal shipment arrives at a transit hub, the following happens:
1. The cargo is offloaded and moved through the airport's cargo handling system
2. The animal is checked by airport staff -- typically a visual welfare check
3. The animal is held in the cargo handling area (which should be climate-controlled)
4. If the layover is long (typically four hours or more), the animal may be taken to a dedicated live animal holding facility where food and water are provided
5. The animal is loaded onto the connecting flight

The quality of transit handling varies significantly between airports and airlines. Major hubs with established live animal facilities (Frankfurt, Amsterdam, Singapore, Dubai) generally handle transit pets well. Smaller hubs with limited animal holding facilities are riskier for long transits.

## What Can Go Wrong in Transit

The most common transit problems:
- **Live animal offload**: Airlines sometimes offload live animals if the connecting flight is full or if there are weight restrictions. This is the most disruptive problem -- your pet misses its connection and may be held for a day or more waiting for the next available flight.
- **Climate control failure**: Rarely, a cargo hold or transit facility fails to maintain appropriate temperature. Quality carriers have monitoring systems but this risk is why routing matters.
- **Documentation check failure**: If the transit country's customs or health officials find a documentation problem at the transit point, the animal can be held.
- **Extended layover without welfare check**: On long layovers without proper animal holding facilities, pets may go extended periods without water.

## How to Choose a Safe Routing

When routing a live animal shipment:
- **Prefer direct flights** when available. One takeoff and landing is better than two.
- **If a connection is unavoidable, choose a hub with good live animal facilities**: Frankfurt (FRA), Amsterdam (AMS), Singapore (SIN), and Dubai (DXB) are all known for quality live animal handling.
- **Avoid tight connections**: The minimum connection time for live animal cargo is typically two hours, but four hours is safer. This gives handling staff time to process the cargo without rushing.
- **Avoid US transit**: Transit through US airports with a live animal in cargo requires US customs clearance under USDA rules. This adds complexity for non-US-bound shipments.
- **Book on the same airline for all legs** where possible, so cargo responsibility does not transfer between carriers.

## The Role of Your Pet Transport Specialist

A good pet transport specialist designs the routing with transit risk in mind. They know which hubs handle live animals well, which carriers have solid offload policies, and which aircraft types have best-in-class cargo climate control. Routing is not just about the fastest connection -- it is about the safest one for your animal.
""",
    "faqs": [
      {"q": "Can my pet be offloaded from a connecting flight?", "a": "Yes. Airlines can offload live animals from connecting flights if the flight is full, if weight limits are reached, or if there are operational reasons. This is one of the risks in live animal cargo transport. Using a specialist pet transport company reduces this risk because they have established relationships with airline cargo teams and can often secure confirmed live animal space."},
      {"q": "How long can a dog or cat safely be in transit at an airport?", "a": "Healthy dogs and cats can safely transit for four to eight hours at a well-managed airport with climate-controlled holding facilities and access to water. Longer transits (over eight hours) require a welfare check and water provision by the cargo handling team. For transits over twelve hours, a dedicated live animal facility with feeding is recommended. Avoid routings with excessively long layovers for your pet's welfare."},
      {"q": "Is it better to book a direct flight for my pet?", "a": "Yes. A direct flight is always preferable for a live animal shipment. Every connection introduces additional handling, another loading and offloading cycle, and another opportunity for delays. If a direct flight is not available on your route, choose a routing with a single connection at a major hub known for good live animal handling (Frankfurt, Amsterdam, Singapore, or Dubai are well-regarded options)."}
    ]
  },
  {
    "slug": "what-is-a-pet-import-permit",
    "title": "What Is a Pet Import Permit and Do You Need One?",
    "description": "Many countries require a pet import permit before your dog or cat can enter. This guide explains what an import permit is, which countries require one and how to apply.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["import permit", "practical guide", "documentation"],
    "body": """A pet import permit is an official government document that authorises a specific animal to enter a country. Not every country requires one, but for those that do, applying for the permit is the first step in any international pet move -- before vaccinations, before crate purchase, and before airline booking.

## Which Countries Require a Pet Import Permit?

Countries that require an import permit for dogs and cats generally include:

- **Australia and New Zealand**: Formal import permits or conditions are issued by DAFF (Australia) and MPI (New Zealand)
- **Japan**: Advance notification and inspection approval from the Animal Quarantine Service (AQS) is required
- **Gulf States** (UAE, Saudi Arabia, Oman, Bahrain, Qatar, Kuwait): Most require a permit from the relevant Ministry
- **Many African countries**: Nigeria (NAFDAC), Kenya, Ghana, Ethiopia, Tanzania, and others
- **Many Asian countries**: Philippines (BAI Veterinary Import Clearance), Vietnam, Indonesia
- **Some South American countries**: Brazil requires MAPA documentation equivalent to a permit
- **Jordan, Morocco, and other Middle Eastern countries**

Countries that do NOT require a permit (and rely on the health certificate alone):
- Most EU/EEA countries (the EU health certificate serves this function)
- Canada (CFIA for personal pets)
- USA (CDC/USDA requirements are met by the health certificate for most origins)
- UK (APHA-endorsed certificate without a separate permit)

## What an Import Permit Contains

A typical import permit specifies:
- The owner's name and contact details
- The animal's microchip number, species, breed, age, and sex
- The country of origin
- The port of entry (you usually must enter through the specified airport)
- The permitted date range for entry
- The specific conditions the animal must meet on arrival (vaccinations, treatments, etc.)

## How to Apply for a Pet Import Permit

The application process varies by country. In most cases:
1. Contact the national veterinary authority (Ministry of Agriculture, Animal Quarantine Service, etc.) in the destination country
2. Submit the required forms with your pet's microchip number, species and breed, vaccination records, and planned travel details
3. Pay the permit fee (varies by country)
4. Wait for the permit to be issued (two to six weeks in most cases)

Many pet transport specialists handle the import permit application as part of their service. This is particularly valuable for countries where the forms are in a language you do not read.

## The Difference Between a Permit and a Health Certificate

The import permit is the destination country's authorisation for the animal to enter. The health certificate is the documentation from your origin country confirming the animal is healthy and meets the entry conditions. Both are usually required together.

The permit is obtained before travel from the destination country's authorities. The health certificate is issued by your vet (and often endorsed by your government veterinary authority) close to the travel date.
""",
    "faqs": [
      {"q": "How far in advance should I apply for a pet import permit?", "a": "Apply for a pet import permit as soon as you know your destination and approximate travel date -- ideally six to eight weeks before travel for most countries. Some countries (Australia, Japan) require more complex advance documentation that effectively functions as a permit and takes longer. For Gulf states and African countries, allow four to six weeks. Do not book flights before confirming that the import permit process has started."},
      {"q": "What happens if I arrive without an import permit?", "a": "If your destination country requires an import permit and you arrive without one, your pet will be refused entry at customs. The animal will be held at the airport quarantine facility at your expense and will either be returned to the origin country or held until a permit is obtained. This is costly, distressing for the animal, and in some cases results in the pet being quarantined for weeks. Never travel to a permit-required country without the permit confirmed."},
      {"q": "Can a pet transport company apply for the import permit on my behalf?", "a": "Yes. Most reputable pet transport companies offer import permit application as part of their full-service package. For countries where the forms are complex or in a foreign language, using a specialist is strongly advisable. They also know the current permit requirements, which can change, and have established contacts with the relevant government veterinary authorities."}
    ]
  },
  {
    "slug": "travelling-with-a-fearful-or-anxious-dog",
    "title": "Travelling Internationally with a Fearful or Anxious Dog",
    "description": "Anxious dogs can travel internationally -- but preparation is different. This guide covers crate training strategies, vet advice, what to tell the airline and how to reduce fear during the flight.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["anxious dog", "fearful dog", "practical guide", "welfare", "stress"],
    "body": """Some dogs find the world fundamentally alarming. Loud noises, strangers, unfamiliar environments, being alone -- the list of triggers varies, but the outcome is the same: travel is harder for these dogs than for a confident, adaptable animal. Harder, but not impossible.

Many anxious dogs travel internationally successfully every year. The difference between a traumatic experience and a manageable one comes down almost entirely to preparation.

## The First Conversation: Talk to Your Vet

Before any planning, have a frank conversation with your vet about your dog's anxiety. Be specific:
- What are the main triggers?
- How does your dog respond when stressed (vocalisation, elimination, destructive behaviour, freezing, panting)?
- Has your vet seen any signs that might indicate a medical component to the anxiety?
- Is there any reason this dog should not fly?

Your vet may recommend a behaviour consultant for dogs with severe anxiety, particularly if the anxiety relates specifically to confinement or noise. A six-month behaviour programme before a major international move is not excessive for a severely anxious dog.

## Sedation: The Evidence

Most vets advise against sedating dogs for air travel. The reasons are:
- Sedated dogs cannot regulate their body temperature effectively
- Pressure changes at altitude affect sedated dogs differently from alert dogs
- The altered state can increase confusion and anxiety rather than reduce it in some dogs
- Most airlines will not accept visibly sedated animals

For dogs with moderate anxiety, pheromone products (DAP diffusers, Adaptil collars) and anxiety wraps (Thundershirt equivalents) are low-risk options worth trying during crate training. These have evidence behind them and are safe for flight.

Some vets prescribe anti-anxiety medication (such as trazodone or gabapentin) that reduces anxiety without full sedation. These are better options than benzodiazepines or heavy sedatives. Discuss with your vet and trial any medication before travel day -- you do not want to discover an adverse reaction on departure morning.

## Crate Training for Anxious Dogs

For an anxious dog, the crate needs to be genuinely safe before travel day. This takes longer than for a confident dog.

Start with the crate in the room where your dog spends most time. Do not close the door. Let the dog investigate and ignore it. Over weeks:
- Place food near the crate, then at the entrance, then inside
- Use your most high-value treats for crate entry
- Never force entry or close the door until the dog enters voluntarily
- When you do close the door, open it before any signs of distress begin
- Build duration very gradually -- one minute, then five, then fifteen, over weeks

A fearful dog may need several months to be genuinely comfortable with a closed crate. If time allows, this investment is worth it.

## What to Tell the Airline

Airlines cannot accommodate special welfare requests for individual animals in the hold, but you can note any sensitivities in your booking and in the documentation attached to the crate. Some owners attach a card to the crate explaining the dog's anxiety and requesting calm handling. While this is not a guarantee, most cargo handlers respond well to personalised information.

## On Travel Day

- Exercise thoroughly in the morning (not vigorously, but enough to be tired)
- Keep the pre-travel environment as calm as possible
- Do not display your own anxiety in front of the dog -- they read your state
- Place a recently worn garment inside the crate (unwashed) for scent comfort
- Attach a note to the crate with the dog's name and a brief description of their personality
""",
    "faqs": [
      {"q": "Should I sedate my anxious dog for an international flight?", "a": "Most vets advise against sedation for air travel. Sedated dogs cannot regulate body temperature effectively, and altitude pressure changes affect sedated animals differently. A better approach is long-term crate training combined with non-sedating anti-anxiety options such as pheromone products, anxiety wraps, or vet-prescribed medications like trazodone or gabapentin. Discuss with your vet and trial any medication well before travel day."},
      {"q": "How long should I crate train a fearful dog before international travel?", "a": "For a fearful or anxious dog, allow a minimum of three to four months for crate training -- and ideally six months. The goal is for the dog to enter and rest in a closed crate voluntarily and calmly for several hours. Rushing this process produces a dog that tolerates the crate under stress rather than one that feels safe inside it. The extra time invested in crate training is the single most effective welfare preparation you can make."},
      {"q": "Can an airline refuse to carry an anxious dog?", "a": "Airlines can refuse to carry a dog that shows visible signs of distress at check-in, as this is a welfare and safety concern. A dog that is vocalising continuously, showing signs of extreme stress, or that has injured itself in the crate may be refused. This is another reason why crate training is so important -- a dog that is calm and settled at check-in is much more likely to be accepted."}
    ]
  },
  {
    "slug": "iata-crate-labelling-requirements",
    "title": "IATA Crate Labelling: What Labels Your Pet's Travel Crate Must Have",
    "description": "IATA regulations require specific labels on any crate carrying a live animal by air. Get this wrong and your pet may not be loaded. Full guide to IATA crate labelling requirements.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["IATA", "crate labelling", "practical guide", "cargo requirements"],
    "body": """Crate labelling is one of those details that seems minor until the airline handler picks up your crate on departure day and says it cannot be loaded. Getting the labelling right is simple once you know what is required.

## IATA Live Animals Regulations (LAR)

The IATA Live Animals Regulations (LAR) is the industry standard for transporting animals by air. It covers crate construction, labelling, handling, and documentation. The labelling requirements are covered in the current edition of the LAR (published annually).

## Required Labels for a Live Animal Crate

**1. LIVE ANIMALS label**
A prominent "LIVE ANIMALS" label must appear on the top of the crate and on at least one side. The label should be large (minimum 12 cm x 12 cm) and clearly visible. Most IATA-compliant crates come with a pre-printed label or a label attachment point. If not, you can attach your own clearly printed label.

**2. Directional arrows ("THIS WAY UP")**
Directional arrows indicating the correct upright position must appear on at least two sides of the crate. These are critical -- cargo handlers use them to ensure the crate is loaded the right way up.

**3. Owner contact information**
Attached to the crate (typically on a tag or label on the outside): your name, phone number, home address, and destination address. Include both origin and destination contact details.

**4. Feeding and watering instructions**
A written note -- attached to the crate or included in a document sleeve -- stating when the animal was last fed and watered, and instructions for feeding and watering during the journey. For journeys over twelve hours, this is particularly important. Example: "Last fed 6am 08/05/2026. Water only. Provide water at layover."

**5. Health certificate and documentation sleeve**
A clear document sleeve attached to the outside of the crate holds the health certificate (or a copy), the import permit (if applicable), and any other travel documentation. The originals should travel with you as the passenger.

## Optional but Recommended Labels

- The animal's name and a photo (helps handlers in an emergency)
- A brief description of the animal's temperament (e.g., "friendly, calm" or "nervous -- handle quietly")
- Your emergency contact number and the contact number of your pet transport specialist

## Where to Get IATA Labels

IATA crate labels are available from pet travel suppliers, pet transport companies, and printable templates are widely available online. Many IATA-compliant crates include a full label pack. If buying separately, ensure the "LIVE ANIMALS" label meets the minimum size requirements in the current LAR.

## Final Check on Departure Day

Before you hand your pet's crate to cargo check-in, run through:
- LIVE ANIMALS label visible on top and at least one side
- Directional arrows on at least two sides
- Your contact information attached
- Feeding/watering instructions attached
- Document sleeve with health certificate and permit copies attached
- Interior: water container filled and attached, absorbent bedding on floor, no leads or collars inside
""",
    "faqs": [
      {"q": "What happens if my pet's crate is not labelled correctly?", "a": "If the crate is missing required IATA labels, the airline cargo handler may refuse to accept it for loading. This can result in a missed flight. In some cases, the handler will allow you to add a missing label on the spot if the issue is minor (such as a missing directional arrow). Critical missing items (no LIVE ANIMALS label, no health certificate sleeve) may result in the shipment being refused entirely."},
      {"q": "Where should the LIVE ANIMALS label be placed on the crate?", "a": "The LIVE ANIMALS label must appear on the top of the crate and on at least one side. It should be prominently visible and not obscured by strapping or other labels. The label should be at least 12 cm x 12 cm. Most IATA-compliant crates have a designated label area on the top -- use it."},
      {"q": "Do I need to include the original health certificate in the document sleeve on the crate?", "a": "A copy of the health certificate in the document sleeve is standard practice. Keep the originals with you as the passenger. At customs and quarantine inspection, you will be asked to present the originals. If your pet travels on a different flight from you, ensure the original documents travel in a sealed envelope attached to the crate or are handed to the cargo agent with instructions to pass them to the receiving agent at the destination."}
    ]
  },
  {
    "slug": "bringing-a-stray-dog-home-from-abroad",
    "title": "Bringing a Stray or Rescue Dog Home from Abroad: A Step-by-Step Guide",
    "description": "Rescued a dog abroad and want to bring it home? This guide covers the process for importing a stray from a holiday destination to the UK, USA, or EU, including CDC rules.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["rescue dog", "stray dog", "import", "practical guide", "UK", "USA"],
    "body": """Every year, thousands of people meet a dog abroad -- on a beach, in a village, at a resort -- and decide to bring it home. It is a rewarding act of rescue, and it is entirely possible to do it legally and safely. But the process is different from moving a pet you already own, and the rules have become stricter in recent years.

## The Key Difference: Stray and Rescue Dogs

A stray dog with no known vaccination history requires a different import process from a pet with a complete vaccination record. The main concern for importing authorities is rabies. If you cannot prove when the dog was last vaccinated (or whether it was ever vaccinated), the authorities treat it as potentially unvaccinated.

## UK Rules for Importing a Stray

The UK has strict rules about pets from high-risk rabies countries. For a stray dog from a non-listed country (most countries outside the EU/EEA/listed country category):
- The dog must be microchipped
- The dog must receive a primary rabies vaccination
- The dog must then undergo a blood sample for a rabies titre test, taken at least thirty days after the vaccination
- The dog must wait three months after the titre test before entering the UK
- A UK government-approved health certificate must be issued within ten days of travel

Total minimum preparation time from rescue: around four to five months.

For dogs from listed countries (EU + some others), the standard EU pet travel rules apply, which are faster.

## USA Rules for Importing a Stray

In 2023, the CDC introduced new rules specifically addressing dogs vaccinated outside the USA. The rules are complex and have changed since their introduction -- always check the current CDC guidance at cdc.gov before importing a dog to the USA.

Key CDC considerations for rescue/stray imports:
- Dogs vaccinated outside the USA against rabies may require a CDC-issued Dog Import Permit before arrival if they do not have a USDA-endorsed health certificate with a compliant vaccination record
- Dogs arriving without proof of US-valid rabies vaccination may be required to be revaccinated at a USDA-designated facility on arrival
- The process varies based on origin country and whether the dog has documentation

## EU Rules for Importing a Stray

The standard EU pet travel rules apply. For a dog from a non-listed (rabies-risk) country being imported into the EU:
- Microchip
- Rabies vaccination (minimum thirty days before titre test if from a non-listed country)
- Titre test at an approved EU laboratory
- Three-month wait after the titre test
- EU-format health certificate

## Using a Specialist Rescue Transport Service

Several organisations specialise in rescue dog imports. These include Street Paws (UK), RSPCA overseas partnerships, and various breed-specific rescue transport networks. Using an established rescue transport organisation is strongly advisable for your first rescue import -- they know the current rules, the approved labs, and the documentation requirements for specific origin countries.

## Welfare and Health on Arrival

A stray dog from abroad may carry parasites, diseases, or health conditions not commonly found in your home country. A thorough veterinary examination within forty-eight hours of arrival is essential. Be prepared to treat for:
- Intestinal parasites
- Tick-borne diseases (Ehrlichia, Leishmania, Babesia depending on origin)
- Heartworm (if from a tropical or subtropical country)
- Skin conditions
""",
    "faqs": [
      {"q": "How long does it take to bring a stray dog from abroad to the UK?", "a": "For a stray dog from a non-listed (rabies-risk) country, the UK import process takes a minimum of four to five months. This includes a primary rabies vaccination, a thirty-day wait, a titre test blood sample, a three-month waiting period, and an APHA-endorsed health certificate within ten days of departure. Start the process immediately after rescuing the dog -- the clock starts from the vaccination date."},
      {"q": "Can I bring a stray dog from a holiday to the USA?", "a": "Yes, but the CDC rules for dogs vaccinated outside the USA are complex and have changed in recent years. The rules depend on the origin country, the vaccination record, and whether the dog has a USDA-compliant health certificate. Check the current CDC guidance at cdc.gov before importing any dog to the USA, and consider using a specialist pet transport company with US import experience."},
      {"q": "What health checks does a rescue dog from abroad need on arrival?", "a": "A thorough veterinary examination within forty-eight hours of arrival is essential. The vet should check for intestinal parasites, tick-borne diseases (Ehrlichia, Leishmania, and Babesia depending on origin), heartworm, skin conditions, and general health. Many tropical and subtropical countries have diseases not commonly found in Western countries. Early detection and treatment improves outcomes significantly."}
    ]
  },
  {
    "slug": "how-to-read-an-airline-pet-policy",
    "title": "How to Read an Airline Pet Policy: What the Fine Print Actually Means",
    "description": "Airline pet policies are full of conditions, exceptions and breed lists. This guide decodes the key terms so you know what to look for and what questions to ask before booking.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["airline pet policy", "practical guide", "in-cabin", "hold cargo"],
    "body": """Airline pet policies are written for legal coverage, not for pet owners trying to understand them. Terms like "manifested baggage," "accompanied air cargo," and "breed restrictions as per the current IATA list" mean specific things -- and misunderstanding them can lead to your pet being refused at the airport.

Here is a guide to the key terms and what they actually mean.

## In-Cabin vs. Checked Baggage vs. Cargo Hold

**In-cabin**: Your pet travels with you in the passenger cabin, in a carrier under the seat in front of you. This is only available for small animals (usually under 8-10 kg combined) on applicable routes. The pet is checked in at the passenger desk, not the cargo counter.

**Checked baggage (excess baggage)**: Your pet travels in the hold but is checked in at the passenger desk alongside your luggage. This is usually only available on routes and aircraft types that allow it, and there are strict weight and crate size limits. Not all airlines offer this option.

**Manifested cargo (air cargo / live animal cargo)**: Your pet is booked as cargo through the airline's cargo division (not the passenger desk). This is the standard method for larger dogs, for unaccompanied shipments, and for most international routes. The booking is made separately from your passenger ticket, through the cargo team.

When an airline says "pets accepted in cabin," this does not mean larger pets are accepted as checked baggage or cargo. Check each category separately.

## "Routes and aircraft types may vary"

This phrase appears in almost every airline pet policy. It means that even if the airline generally accepts pets, your specific flight may not. The reasons:
- Some aircraft types (narrow-body jets, turboprops) have no temperature-controlled hold and cannot carry live animals
- Some routes have regulatory restrictions at the destination airport
- Busy routes may have live animal capacity already booked

Always confirm live animal acceptance on your specific flight and date, not just the route in general.

## Brachycephalic Breed Restrictions

Most airlines have a list of restricted or banned brachycephalic (flat-faced) breeds. The list typically includes:
- Bulldogs (English, French, American)
- Pugs
- Boston Terriers
- Shih Tzus
- Pekingese
- Persian, Himalayan, Exotic Shorthair cats

Some airlines ban all listed breeds from hold travel but accept them in-cabin. Others ban them entirely. The list varies by airline and is updated periodically. Always check the current breed restriction list for your specific carrier.

## "Subject to availability"

Live animal cargo spaces are limited on most aircraft. "Subject to availability" means you cannot simply assume your pet can be added at check-in. Book the live animal space at the same time as your passenger ticket -- or even before.

## Health Certificate Requirements

Airlines typically require a health certificate issued within a specific window before travel (commonly seven to ten days). Some airlines specify a government-endorsed certificate. "Vet-signed certificate" and "government-endorsed health certificate" are different things -- many countries require the latter, and so do most international carriers.

## Questions to Ask Before Booking

- Is my specific route and date confirmed for live animal acceptance?
- Is my breed accepted?
- What is the combined weight limit for in-cabin travel?
- What is the maximum crate size for hold travel on this aircraft type?
- What documentation do you require, and does the health certificate need government endorsement?
- What is your offload policy for live animals?
""",
    "faqs": [
      {"q": "What is the difference between checked baggage and cargo hold for pets?", "a": "Checked baggage means your pet is checked in at the passenger desk alongside your luggage and travels in the hold. Cargo hold (manifested cargo) means your pet is booked through the cargo division as a separate shipment, with a separate booking and documentation process. Most airlines only offer one or the other for international routes. Manifested cargo is the standard for larger dogs and international shipments."},
      {"q": "Does 'pets accepted' on a route mean my specific dog is accepted?", "a": "Not automatically. 'Pets accepted' means the route generally allows live animals -- but your specific dog may not qualify due to breed restrictions, weight limits, aircraft type on your specific date, or lack of available live animal space. Always confirm that your specific breed and size is accepted on your exact flight date, not just the route in general."},
      {"q": "What does 'subject to availability' mean for live animal bookings?", "a": "Live animal cargo spaces are limited on most aircraft -- typically four to eight spaces per flight depending on the aircraft type. 'Subject to availability' means these spaces fill up and cannot be guaranteed without a confirmed booking. Book the live animal space as early as possible, ideally at the same time as your passenger ticket."}
    ]
  },
  {
    "slug": "best-countries-for-expats-with-pets",
    "title": "Best Countries for Expats with Pets: Easy Import Rules and Pet-Friendly Cultures",
    "description": "Choosing where to relocate? Some countries are far more pet-friendly than others. This guide ranks destinations by ease of import, veterinary care, and daily life with a pet.",
    "date": "2026-05-08",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["expat", "practical guide", "destination guide", "pet-friendly"],
    "body": """If you have flexibility in where you relocate, pet considerations might legitimately influence your choice. Some countries make bringing a pet straightforward and provide excellent care on arrival. Others involve months of complex preparation, mandatory quarantine, or restrictions that make the move genuinely difficult.

Here is a practical assessment of some popular expat destinations from a pet owner's perspective.

## Easiest Pet Import: EU Countries

The EU operates a unified pet travel framework. If your pet is microchipped, has a current rabies vaccination, and you have an EU-format health certificate, you can move between EU countries with relative ease. For pets already in the EU, intra-EU travel is about as simple as it gets.

From outside the EU (UK, USA, Australia), you need a third-country import certificate and potentially a titre test if arriving from a high-risk origin. But within the EU, everyday life with a pet is generally excellent. France, Germany, Spain, Portugal, and the Netherlands are all highly pet-friendly in day-to-day terms.

**Best EU choices for ease of life with a pet**: France (dog-friendly culture, pets in restaurants common), Germany (highly organised, excellent vets), Portugal (warm climate, growing expat community, manageable import rules), Netherlands (cycle-friendly, pet-permissive).

## Canada: Simple Import, Excellent Care

Canada has some of the most straightforward pet import requirements of any major destination. For dogs from most Western countries, a current rabies vaccination and a CFIA-compliant health certificate are essentially all that is required.

Veterinary care across Canada is excellent. Pet insurance is widely available. Outdoor pet culture is strong. The climate is challenging (cold winters) but Canadians are well-equipped to manage it.

## USA: Manageable but Watch the CDC Rules

The USA requires a current rabies vaccination for dogs (and since 2023, additional CDC requirements for dogs vaccinated outside the USA). For cats, no federal requirement exists for personal pets from most origins. Veterinary care is outstanding. Pet culture is strong.

The main watch point is the 2023 CDC rule changes -- always check the current requirements at cdc.gov before importing any dog to the USA.

## Singapore: Good Care, Strict Rules

Singapore has strict biosecurity rules but they are well-documented and the quarantine process (if applicable from your origin) is professionally managed. Veterinary care is excellent. The city-state is generally pet-permissive in private housing, though HDB flats have size and breed restrictions.

## Australia and New Zealand: Excellent, But Prepare Early

Both countries have outstanding veterinary care, strong pet culture, and excellent outdoor access. The import process is demanding (titre test, waiting period, quarantine on arrival) but it works reliably. Start eight to ten months before travel.

## Avoid Without Specialist Help: Japan, Mauritius, Hawaii (USA)

Japan and Mauritius are genuinely among the most demanding pet import destinations in the world. The process is manageable but requires specialist management. Hawaii (which has its own rules separate from mainland USA) also has strict rabies-prevention requirements given its rabies-free status.

## The Practical Scorecard

| Destination | Import Ease | Vet Care | Pet Culture | Overall |
|-------------|-------------|----------|-------------|---------|
| EU countries | High | Excellent | High | Excellent |
| Canada | High | Excellent | High | Excellent |
| USA | Medium | Excellent | High | Very Good |
| Singapore | Medium | Excellent | Good | Very Good |
| Australia/NZ | Low (preparation) | Excellent | High | Good (if prepared) |
| UAE/Dubai | Medium | Good | Medium | Good |
| Japan | Low | Excellent | Medium | Difficult without specialist |
""",
    "faqs": [
      {"q": "Which country has the easiest pet import rules for expats?", "a": "EU countries have among the simplest pet import rules for pets already in the EU, using the EU animal health certificate framework. Canada has straightforward requirements for most Western origins. The USA has manageable rules but check current CDC requirements for dogs vaccinated outside the USA. Australia and New Zealand are excellent destinations for pets but require eight to ten months of preparation."},
      {"q": "Which countries have mandatory quarantine for imported pets?", "a": "Australia, New Zealand, and Japan have mandatory quarantine for all imported dogs and cats (typically ten days for Australia and NZ, twelve hours to 180 days for Japan depending on compliance). Mauritius also requires quarantine. Most other countries do not have mandatory quarantine if the pet arrives with correct documentation, though they may hold animals for inspection if papers are not in order."},
      {"q": "Is veterinary care good in the Middle East for expat pet owners?", "a": "Veterinary care in Dubai, Abu Dhabi, Doha, and Riyadh has improved significantly and several international-standard clinics serve expatriate communities. Kuwait, Bahrain, and Muscat also have reasonable care in major cities. In rural or less-developed areas, care is more limited. For specialist or emergency care, Dubai and Doha are the strongest options in the region."}
    ]
  }
]


def make_front_matter(article):
    lines = []
    lines.append("---")
    lines.append("title: \"{}\"".format(article["title"].replace('"', '\\"')))
    lines.append("description: \"{}\"".format(article["description"].replace('"', '\\"')))
    lines.append("date: \"{}\"".format(article["date"]))
    lines.append("type: \"blog\"")
    lines.append("author: \"{}\"".format(article["author"]))
    lines.append("slug: \"{}\"".format(article["slug"]))
    lines.append("url: \"/blog/{}/\"".format(article["slug"]))
    lines.append("seo:")
    lines.append("  title: \"{}\"".format(article["title"].replace('"', '\\"')))
    lines.append("  description: \"{}\"".format(article["description"].replace('"', '\\"')))
    tags = article.get("tags", [])
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append("  - \"{}\"".format(tag.replace('"', '\\"')))
    faqs = article.get("faqs", [])
    if faqs:
        lines.append("faqs:")
        for faq in faqs:
            q = faq["q"].replace('"', '\\"')
            a = faq["a"].replace('"', '\\"')
            lines.append("  - question: \"{}\"".format(q))
            lines.append("    answer: \"{}\"".format(a))
    lines.append("---")
    return "\n".join(lines)


written = 0
skipped = 0

for article in ARTICLES:
    filename = article["slug"] + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        print("SKIP  {}".format(filename))
        skipped += 1
        continue
    front_matter = make_front_matter(article)
    body = article["body"].strip()
    content = front_matter + "\n\n" + body + "\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("WRITE {}".format(filename))
    written += 1

print("\nWritten: {} | Skipped: {} | Total: {}".format(written, skipped, len(ARTICLES)))
