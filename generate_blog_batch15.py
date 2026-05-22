"""
Blog Batch 15 -- 28 new articles
Topics: P4 country import guides (Ethiopia, Ghana, Peru, Oman, Bahrain, Nepal, Mauritius),
        Route guides, Breed travel guides, Practical guides
Run from repo root: python generate_blog_batch15.py
"""

import os

OUTPUT_DIR = os.path.join("site", "content", "blog")
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [
  {
    "slug": "ethiopia-pet-import-guide",
    "title": "Moving to Ethiopia with a Pet: Import Rules, Vaccines and What to Expect",
    "description": "Everything you need to bring a dog or cat into Ethiopia. Health certificate, rabies vaccine, import permit and what happens at Addis Ababa airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Ethiopia", "import guide", "Africa", "dog", "cat"],
    "body": """Relocating to Ethiopia with a pet is genuinely manageable if you start the paperwork early. Most problems happen because people underestimate the lead time for the import permit, not because Ethiopia's rules are unusually strict.

## What Ethiopia Requires for Pet Import

All dogs and cats entering Ethiopia need a government-issued import permit, obtained before travel from the Ethiopian Ministry of Agriculture. Apply at least four to six weeks ahead -- the permit is not instant.

Once you have the permit, your vet needs to issue a health certificate no more than ten days before the flight. The certificate must confirm your pet is healthy, microchipped, and has a current rabies vaccination. Rabies vaccines need to have been given at least thirty days before travel, so plan this in advance.

A titre test (blood test confirming rabies antibody levels) is not routinely required for Ethiopia, but individual airlines or ground handling agents at Addis Ababa Bole International Airport (ADD) may ask for supporting documentation. Check with your airline cargo team before departure.

## Getting the Import Permit

Contact the Ethiopian Ministry of Agriculture Veterinary Services Directorate for the permit application. Expect to provide:
- Proof of microchip number
- Vaccination records
- A description of the animal (species, breed, age, sex)
- Your arrival date and flight details

Some owners use a local veterinary liaison in Addis Ababa to help coordinate the permit. This can be useful if language or response delays become a problem.

## Flying into Addis Ababa

Ethiopian Airlines is the primary carrier into Addis Ababa and has an active live animal cargo programme. If you are coming from Europe or the USA, Ethiopian Airlines is almost always your best routing option. Contact Ethiopian Airlines Cargo to book the live animal shipment separately from your passenger ticket.

On arrival at Bole International Airport, your pet will be inspected by a Ministry of Agriculture veterinary officer. Have all documents -- import permit, health certificate, vaccination record, microchip documentation -- ready in a single folder.

## Living with a Pet in Ethiopia

Veterinary care in Addis Ababa is available but limited compared to Western cities. The Ethiopian Society for the Prevention of Cruelty to Animals (SPCA) can provide contacts for reputable local vets. Bring a stock of any prescription medication your pet uses regularly, as some veterinary products are not readily available locally.

Rabies is present in Ethiopia. Keep vaccinations current and keep your pet away from unknown stray animals. Tick and flea prevention is important year-round given the climate.

## Summary Checklist

- Import permit from Ethiopian Ministry of Agriculture (apply 4-6 weeks before travel)
- Microchip (ISO 11784/11785)
- Rabies vaccination, at least 30 days before travel
- Health certificate from accredited vet, within 10 days of departure
- IATA-compliant crate for hold travel
""",
    "faqs": [
      {"q": "Does Ethiopia require a rabies titre test for pet import?", "a": "A rabies titre test is not a standard requirement for pet import into Ethiopia, but some airlines and ground agents may request it. Check with Ethiopian Airlines Cargo and confirm the current position with the Ethiopian Ministry of Agriculture Veterinary Services Directorate before travel."},
      {"q": "How do I get an import permit to bring a pet into Ethiopia?", "a": "Apply to the Ethiopian Ministry of Agriculture Veterinary Services Directorate at least four to six weeks before your planned arrival date. Provide your pet's microchip number, vaccination records, and planned arrival details. The permit must be obtained before travel."},
      {"q": "Which airline is best for flying a pet to Addis Ababa?", "a": "Ethiopian Airlines operates the most comprehensive network into Addis Ababa (ADD) and has an active live animal cargo programme. Contact Ethiopian Airlines Cargo to arrange the live animal booking alongside or separately from your passenger ticket."}
    ]
  },
  {
    "slug": "ghana-pet-import-guide",
    "title": "Bringing a Pet to Ghana: Import Permits, Vaccinations and Accra Arrival",
    "description": "Guide to importing a dog or cat into Ghana. Veterinary import permit, rabies and other vaccine requirements, and what to expect at Kotoka International Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Ghana", "import guide", "Africa", "dog", "cat"],
    "body": """Ghana is an accessible destination for pet owners relocating to Accra or other Ghanaian cities, and the country's pet import process is relatively straightforward if the paperwork is in order before you travel.

## What Ghana Requires for Pet Import

The key authority is the Veterinary Services Directorate (VSD) under Ghana's Ministry of Food and Agriculture. All dogs and cats entering Ghana need:

- A veterinary import permit from the VSD (apply before travel)
- A health certificate issued by a government-accredited vet within ten days of travel
- A current rabies vaccination (must be active on the date of arrival)
- Microchip (recommended; ISO standard preferred)
- Records of other core vaccinations (distemper, hepatitis, parvovirus for dogs; feline herpesvirus, calicivirus, panleukopenia for cats)

A rabies titre test is not a standard requirement for Ghana, but it is worth confirming the current position with the VSD when you apply for your permit, as requirements can be updated.

## Applying for the Import Permit

Apply to the Veterinary Services Directorate, Ministry of Food and Agriculture, Ghana. The VSD can be contacted via the Ministry. Allow at least three to four weeks for the permit process.

## Flying into Accra

Kotoka International Airport (ACC) in Accra is Ghana's main international gateway. Airlines serving Accra that accept live animal cargo include Ethiopian Airlines, British Airways, KLM, and Delta. Ethiopian Airlines has a particularly strong Africa-wide cargo network and is often the most convenient option for pet shipments.

Contact the cargo team of your chosen airline to book the live animal space. Do this well ahead of travel -- cargo space for live animals is limited on most aircraft types.

## Veterinary Care in Ghana

Veterinary facilities exist in Accra, but the range of specialists and medications available is narrower than in Europe or North America. Bring a supply of any ongoing prescription medications, and carry copies of your pet's vaccination and health records in case a local vet needs to review them.

## Summary Checklist

- Veterinary import permit from Ghana VSD (apply 3-4 weeks before)
- Microchip (ISO 11784/11785)
- Rabies vaccination (current and valid on arrival)
- Health certificate from accredited vet, within 10 days of departure
- Core vaccination record
- IATA-compliant crate
""",
    "faqs": [
      {"q": "What documents does my dog need to enter Ghana?", "a": "Your dog needs a veterinary import permit from Ghana's Veterinary Services Directorate, a health certificate issued within ten days of travel, a current rabies vaccination, and records of core vaccinations. A microchip is strongly recommended. Contact the VSD for any permit before booking flights."},
      {"q": "Is there a quarantine requirement for pets arriving in Ghana?", "a": "Ghana does not impose a mandatory quarantine period for pets arriving with the correct documentation, including a valid import permit, health certificate, and current vaccinations. Animals arriving without proper paperwork may be quarantined or refused entry."},
      {"q": "Which airlines fly pets to Accra?", "a": "Ethiopian Airlines, British Airways, KLM, and Delta all serve Kotoka International Airport (ACC) and have live animal cargo programmes. Ethiopian Airlines is often the most practical option for pet shipments to Ghana given its extensive Africa network. Book cargo space directly with the airline's cargo team."}
    ]
  },
  {
    "slug": "peru-pet-import-guide",
    "title": "Pet Import to Peru: Requirements for Dogs and Cats Entering Lima",
    "description": "Bringing a dog or cat to Peru? This guide covers SENASA health certificates, rabies vaccines, import permits and what to expect at Jorge Chavez International Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Peru", "import guide", "South America", "dog", "cat"],
    "body": """Peru is a popular destination for expats, and bringing a pet to Lima or other Peruvian cities is achievable with the right preparation. The key agency is SENASA -- the National Agricultural Health Service -- which oversees all live animal imports.

## SENASA Requirements for Pet Import

SENASA is the authority you need to work with. The core requirements for dogs and cats entering Peru are:

- A health certificate issued by an official government veterinarian (not just a private vet) in your country of origin, within ten days of travel
- Rabies vaccination that is current and has been given at least thirty days before travel
- For dogs: distemper, hepatitis, parvovirus, and leptospirosis vaccinations
- For cats: feline herpesvirus, calicivirus, and panleukopenia vaccinations
- Microchip (ISO 11784/11785 strongly recommended)
- A veterinary import permit pre-issued by SENASA (required for many origins)

A rabies titre test is not a standard SENASA requirement, but confirm the current rules for your specific origin country, as requirements do occasionally change.

## Getting the SENASA Import Certificate

Contact SENASA through senasa.gob.pe before travel. Depending on your origin country, SENASA may require advance documentation or an import permit. The processing time is typically one to two weeks for straightforward cases.

## Flying into Lima

Jorge Chavez International Airport (LIM) is Peru's main international hub. Airlines including American Airlines, LATAM Airlines, Delta, Air France, Iberia, and KLM all serve Lima and accept live animal cargo on applicable routes. LATAM Airlines, as South America's largest carrier, has extensive experience handling pet shipments to Peru.

Coordinate with the airline cargo team to book live animal space. The health certificate must be signed and endorsed by an official government veterinarian in your country -- a private vet signature alone is not sufficient for Peruvian customs.

## Practical Notes

- Lima's altitude is close to sea level, but Cusco sits at 3,400 metres. If you plan to travel with your pet to high-altitude locations, discuss altitude acclimatisation with your vet, particularly for brachycephalic breeds.
- Peru's climate varies significantly by region. Prepare for heat in coastal areas and cold at high altitude.
- Bring a stock of any flea, tick, and parasite prevention medication your vet recommends for tropical or subtropical climates.

## Summary Checklist

- SENASA import permit (apply via senasa.gob.pe before travel)
- Official government veterinarian health certificate, within 10 days of departure
- Rabies vaccination (current, given at least 30 days before travel)
- Core vaccinations for dogs and cats
- Microchip
- IATA-compliant crate for hold travel
""",
    "faqs": [
      {"q": "Does Peru require a rabies titre test for pet import?", "a": "A rabies titre test is not a standard SENASA requirement for most origins. However, requirements can vary and are updated periodically. Confirm the current rules for your specific country of origin directly with SENASA at senasa.gob.pe before planning your travel."},
      {"q": "Who issues the health certificate for importing a pet to Peru?", "a": "The health certificate must be issued and signed by an official government veterinarian in your country of origin. In the UK, this means a vet endorsed by APHA. In the USA, an accredited vet endorsed by USDA APHIS. A private vet certificate without official government endorsement is not accepted."},
      {"q": "What is SENASA and how do I contact them for pet import?", "a": "SENASA is Peru's National Agricultural Health Service (Servicio Nacional de Sanidad Agraria), the authority that regulates live animal imports. Visit senasa.gob.pe or contact the SENASA import permit office before travel to confirm current requirements for your pet's country of origin."}
    ]
  },
  {
    "slug": "oman-pet-import-guide",
    "title": "Importing a Pet to Oman: Rules, Rabies Titre Test and What to Know",
    "description": "Guide to importing a dog or cat to Oman. Ministry of Agriculture permit, rabies titre test requirements, approved breeds and what to expect at Muscat airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Oman", "import guide", "Middle East", "dog", "cat"],
    "body": """Oman is an increasingly popular destination for expatriates, and a growing number of residents keep pets. The import process is manageable, but it has more steps than many people expect -- the rabies titre test requirement catches some owners out if they leave preparation too late.

## Oman's Pet Import Requirements

The Ministry of Agriculture, Fisheries and Water Resources oversees live animal imports into Oman. Core requirements for dogs and cats are:

- An import permit from the Ministry of Agriculture (obtain before travel)
- Microchip (ISO 11784/11785)
- Rabies vaccination, given at least thirty days before the blood sample for the titre test
- Rabies titre test (blood test confirming antibody levels meet the required threshold), taken at a Ministry-approved laboratory
- Waiting period after the titre test -- typically three months must pass between the titre test and travel
- Health certificate from an accredited vet, issued within ten days of travel
- Core vaccination record

The three-month wait after the titre test means your minimum preparation window is around four months from starting the process.

## Applying for the Import Permit

Apply to the Ministry of Agriculture, Fisheries and Water Resources in Oman. Many owners have their pet transport specialist handle this, as the application requires documents translated or formatted to Omani government standards.

## Approved Breeds

Oman restricts the import of certain dog breeds. Breeds commonly classified as dangerous or aggressive are generally prohibited. Confirm whether your specific breed is approved before proceeding -- do this as the first step, before any titre tests or permits are initiated.

## Flying into Muscat

Muscat International Airport (MCT) is Oman's main gateway. Oman Air accepts live animals on applicable international routes and is a natural choice for routing. Emirates, Qatar Airways, British Airways, and Lufthansa also serve Muscat and have live animal cargo programmes.

Flights via Dubai (DXB) or Doha (DOH) are common for European origins. Check whether the connecting airline accepts live animals on all legs of the journey -- not all do on short Gulf hops.

## Summary Checklist

- Import permit from Oman Ministry of Agriculture
- Microchip
- Rabies vaccination (at least 30 days before titre test blood draw)
- Rabies titre test at approved laboratory
- Wait three months after titre test before travel
- Health certificate within 10 days of departure
- Breed clearance confirmed
""",
    "faqs": [
      {"q": "Does Oman require a rabies titre test for dog and cat import?", "a": "Yes. Oman requires a rabies titre test for dogs and cats. The vaccination must be given at least thirty days before the blood sample is taken, and at least three months must pass between the titre test date and the date of travel. This means you need a minimum of around four months of preparation time."},
      {"q": "Are there breed restrictions for importing dogs to Oman?", "a": "Yes. Oman restricts the import of certain dog breeds considered dangerous or aggressive. Confirm whether your specific breed is permitted before beginning any import preparations. Contact the Oman Ministry of Agriculture, Fisheries and Water Resources directly, or work with a specialist pet transport company with Oman experience."},
      {"q": "Which airlines fly pets to Muscat?", "a": "Oman Air accepts live animals on applicable routes. Emirates, Qatar Airways, British Airways, and Lufthansa also serve Muscat and have live animal cargo programmes. For routing via Dubai or Doha, confirm that all legs of the journey accept live animals before booking."}
    ]
  },
  {
    "slug": "bahrain-pet-import-guide",
    "title": "Bringing a Pet to Bahrain: Import Permits, Vaccines and the Titre Test",
    "description": "Guide to importing a dog or cat to Bahrain. MAARAF import permit, rabies titre test, approved breeds, and flying into Bahrain International Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Bahrain", "import guide", "Middle East", "dog", "cat"],
    "body": """Bahrain is home to a large expatriate community, and many residents successfully keep pets. The Ministry of Works, Municipalities Affairs and Urban Planning handles pet imports, and the process -- while thorough -- is straightforward if you start early.

## What Bahrain Requires for Pet Import

The core requirements for dogs and cats entering Bahrain are:

- Import permit from Bahrain's Ministry of Works, Municipalities Affairs and Urban Planning (Agricultural Affairs Directorate)
- Microchip (ISO 11784/11785)
- Rabies vaccination (current; given at least thirty days before the titre test blood draw)
- Rabies titre test at an approved laboratory (the required antibody level must be met)
- Three-month waiting period after the titre test date before travel
- Health certificate from an accredited vet, within ten days of departure
- Core vaccinations (distemper, parvovirus, hepatitis for dogs; herpesvirus, calicivirus, panleukopenia for cats)

The titre test and waiting period means you need approximately four months of preparation time minimum.

## Breed Restrictions

Bahrain prohibits the import of certain dog breeds considered dangerous, including pit bull types, Rottweilers (in some circumstances), and other breeds on the banned list. Confirm your breed is permitted before initiating the import process.

## Flying into Bahrain

Bahrain International Airport (BAH) is served by Gulf Air (Bahrain's national carrier), British Airways, KLM, Lufthansa, and other major carriers. Gulf Air accepts live animals on applicable routes -- contact Gulf Air Cargo for bookings. Emirates via Dubai is also a common routing option.

## Practical Notes

Bahrain is a small island nation with a hot, humid climate. Veterinary care in Manama is good, with several well-equipped clinics serving the expatriate community. Flea and tick prevention is important year-round.

## Summary Checklist

- Import permit from Bahrain Ministry of Works (Agricultural Affairs Directorate)
- Microchip
- Rabies vaccination (at least 30 days before titre test)
- Rabies titre test at approved laboratory
- Three-month wait after titre test before travel
- Health certificate within 10 days of departure
- Breed approval confirmed
""",
    "faqs": [
      {"q": "Does Bahrain require a rabies titre test to import a pet?", "a": "Yes. Bahrain requires a rabies titre test. The rabies vaccination must be given at least thirty days before the blood sample, and a minimum of three months must pass between the titre test date and the date of travel. Start the process at least four months before your planned move."},
      {"q": "Which dog breeds are banned in Bahrain?", "a": "Bahrain restricts the import of several breeds considered dangerous, including pit bull types and certain other large, powerful breeds. Confirm whether your specific breed is permitted by contacting Bahrain's Ministry of Works, Municipalities Affairs and Urban Planning (Agricultural Affairs Directorate) before proceeding with any paperwork."},
      {"q": "Which airline is best for flying a pet to Bahrain?", "a": "Gulf Air is Bahrain's national carrier and accepts live animals on applicable international routes. Contact Gulf Air Cargo directly to arrange the live animal booking. British Airways, KLM, and Lufthansa also serve Bahrain and can ship pets as cargo. Emirates via Dubai (DXB) is another common routing option."}
    ]
  },
  {
    "slug": "nepal-pet-import-guide",
    "title": "Importing a Pet to Nepal: Rules, Vaccinations and the Kathmandu Process",
    "description": "What you need to bring a dog or cat to Nepal. Department of Livestock Services requirements, rabies vaccine, health certificate and what to expect at Tribhuvan Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Nepal", "import guide", "South Asia", "dog", "cat"],
    "body": """Nepal is home to a growing expatriate community working in development, trekking, and international organisations, and a reasonable number of residents do bring pets. The regulations are managed by the Department of Livestock Services (DLS) under the Ministry of Agriculture and Livestock Development.

## Nepal's Pet Import Requirements

The Department of Livestock Services oversees live animal imports. Requirements for dogs and cats entering Nepal include:

- A health certificate from a government-accredited veterinarian in your country of origin, issued within ten days of travel
- Rabies vaccination (current and valid on arrival)
- Core vaccinations for dogs and cats
- Microchip (ISO standard recommended)
- Import permit or clearance from the DLS (confirm requirements ahead of travel as processes can vary)

A rabies titre test is not universally required by Nepal, but confirm current requirements with the DLS before travel, as rules can change.

## Arriving at Tribhuvan International Airport

Tribhuvan International Airport (KTM) is the only international airport in Nepal. Live animal imports arrive via cargo at the airport's animal quarantine station for inspection by DLS officials. Allow time on arrival for documentation checks.

Airlines serving Kathmandu with live animal programmes include Qatar Airways, Emirates, Turkish Airlines, IndiGo, and Air India. Routings via Doha or Dubai are common for Western origins.

## Veterinary Care in Kathmandu

Veterinary facilities in Kathmandu have improved significantly in recent years. Several clinics cater to expatriate pet owners. Bring a stock of any ongoing medications, particularly prescription products that may be difficult to source locally.

Altitude is relevant: Kathmandu sits at around 1,400 metres. This is manageable for most pets, but if you plan to travel to high-altitude regions, discuss this with your vet.

## Summary Checklist

- Import permit/clearance from Nepal DLS
- Health certificate from accredited vet, within 10 days of departure
- Rabies vaccination (current)
- Core vaccinations
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "What paperwork does a dog need to enter Nepal?", "a": "Dogs entering Nepal need a government-endorsed health certificate issued within ten days of travel, a current rabies vaccination, core vaccinations, a microchip, and clearance from Nepal's Department of Livestock Services. Confirm current requirements with the DLS before travel as procedures can be updated."},
      {"q": "Is there a quarantine period for pets arriving in Nepal?", "a": "Nepal does not impose a routine quarantine period for pets arriving with correct documentation. Animals are inspected by Department of Livestock Services officials at Tribhuvan International Airport. Animals without proper paperwork may be held for inspection or refused entry."},
      {"q": "Which airlines fly pets to Kathmandu?", "a": "Qatar Airways, Emirates, Turkish Airlines, IndiGo, and Air India all serve Tribhuvan International Airport (KTM) and have live animal cargo programmes on applicable routes. Routings via Doha, Dubai, or Istanbul are common for arrivals from Europe and North America."}
    ]
  },
  {
    "slug": "mauritius-pet-import-guide",
    "title": "Pet Import to Mauritius: A Strict but Manageable Process",
    "description": "Mauritius has some of the strictest pet import rules in the world. Rabies-free status means titre tests, long waiting periods and approved country lists. Here is the full guide.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Mauritius", "import guide", "Indian Ocean", "dog", "cat"],
    "body": """Mauritius is one of the most beautiful island destinations in the world, and it works hard to stay that way. As a rabies-free country, it operates one of the stricter pet import regimes in the Indian Ocean. If you are relocating to Mauritius and want to bring a dog or cat, the paperwork is manageable but needs to start many months before travel.

## Why Mauritius Is Strict

Mauritius has been free of rabies for decades. To protect this status, the government tightly controls which animals enter, from which countries, and under what health conditions. The rules are enforced rigorously.

## Pet Import Requirements

The Ministry of Agro-Industry and Food Security oversees pet imports. The requirements include:

- An import permit from the Ministry (apply before travel)
- The permit is only issued for animals coming from approved low-risk countries (check whether your origin country is on the approved list)
- Microchip (ISO 11784/11785)
- Rabies vaccination (primary course followed by booster)
- Rabies titre test (blood sample taken at least thirty days after the most recent rabies vaccination, tested at an approved laboratory)
- Waiting period: at least six months must have passed since the titre test date before travel to Mauritius is permitted
- Additional treatments (tapeworm treatment, tick/flea treatment) as specified on the permit
- Health certificate issued within ten days of travel
- A quarantine period of at least three days on arrival in Mauritius is required even with all documents correct

The minimum preparation window from starting the process is typically around eight months given the titre test waiting period.

## Approved Countries

Not all countries are on Mauritius's approved origin list. Check with the Ministry of Agro-Industry and Food Security whether your country of origin qualifies before beginning any preparations. Animals from non-approved countries face significantly more complex import procedures.

## Flying to Mauritius

Sir Seewoosagur Ramgoolam International Airport (MRU) is served by Air Mauritius, British Airways, Air France, Emirates, and others. Air Mauritius accepts live animals on applicable routes -- contact Air Mauritius Cargo for bookings.

## Summary Checklist

- Import permit from Ministry of Agro-Industry (check approved country list first)
- Microchip
- Rabies vaccination course
- Rabies titre test (30+ days after last vaccine)
- Six-month wait after titre test before travel
- Health certificate within 10 days of departure
- Three-day quarantine on arrival
""",
    "faqs": [
      {"q": "How long does it take to prepare to bring a pet to Mauritius?", "a": "The Mauritius import process takes a minimum of around eight months because of the titre test requirement and the six-month waiting period that follows. Start the rabies vaccination, titre test, and import permit application as early as possible. Missing any step restarts the waiting period."},
      {"q": "Is there a quarantine period for pets arriving in Mauritius?", "a": "Yes. All pets entering Mauritius undergo a minimum three-day quarantine on arrival even if all documentation is complete and correct. The quarantine is at a government facility. If any documentation is missing or incorrect, the quarantine period will be extended and the pet may face deportation."},
      {"q": "Can I bring any dog breed to Mauritius?", "a": "Mauritius bans the import of certain dog breeds, including pit bull types and other breeds classified as dangerous. Confirm whether your breed is permitted as part of the import permit application process with the Ministry of Agro-Industry and Food Security."}
    ]
  },
  {
    "slug": "uk-to-costa-rica-pet-transport-guide",
    "title": "Pet Transport from UK to Costa Rica: Requirements, Airlines and the Journey",
    "description": "Guide to shipping a dog or cat from the UK to Costa Rica. SENASA requirements, microchip, vaccines, health certificate and which airlines fly pets on this route.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["UK", "Costa Rica", "route guide", "dog", "cat"],
    "body": """Costa Rica is one of the top destinations for UK expats seeking a warmer climate, and the country is genuinely welcoming to pets. The import rules are clear, and the route is well-served by airlines -- but the timing of your health certificate matters.

## What Costa Rica Requires

Costa Rica's pet import rules are administered by SENASA (Servicio Nacional de Sanidad Animal) under the Ministry of Agriculture. For dogs and cats arriving from the UK, the requirements are:

- A health certificate issued by a government-accredited vet in the UK (APHA-endorsed) within ten days of travel
- Rabies vaccination (current and valid on the date of arrival)
- Internal parasite treatment (tapeworm treatment for dogs specifically) given within a defined window before travel
- External parasite treatment (flea/tick treatment) applied close to travel
- Microchip (ISO 11784/11785)
- A healthy clinical examination confirming no signs of infectious disease

A rabies titre test is not a standard SENASA requirement for UK-origin animals, but confirm the current position with SENASA (senasa.go.cr) before travel as rules can be updated.

## The Health Certificate Timing Issue

The ten-day window for the health certificate is the most common cause of problems on this route. You need the APHA endorsement on top of the vet-signed certificate, and the APHA process can take several days. Plan this carefully and use an APHA-approved vet who knows the Costa Rica certificate format.

## Airlines for UK to Costa Rica

There are no direct flights from the UK to Costa Rica. Common routings include:

- British Airways via Miami (MIA) or other US hubs -- note that live animals cannot transit US airports as cargo without meeting USDA requirements
- Iberia via Madrid (MAD) -- Iberia accepts live animals on applicable routes; Madrid is a practical hub for connecting to San Jose
- KLM via Amsterdam (AMS) and then LATAM or other carriers -- check each leg accepts live animals
- American Airlines via US hubs -- same USDA transit rules apply

The Madrid routing via Iberia is often the simplest for pets because it avoids US transit complications.

## Arriving at San Jose

Juan Santamaria International Airport (SJO) is Costa Rica's main gateway. SENASA officers carry out the inspection on arrival. Ensure your documents are in a single clear folder: health certificate, microchip documentation, vaccination record, and parasite treatment records.

## Summary Checklist

- APHA-endorsed health certificate, within 10 days of departure
- Rabies vaccination (current)
- Tapeworm treatment (within specified window before travel)
- Flea/tick treatment (close to travel date)
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "Is there a direct flight from the UK to Costa Rica with pets?", "a": "There are no direct non-stop flights from the UK to Costa Rica. Common routing options include via Madrid with Iberia (practical for pets as it avoids US transit complications) or via US hubs with British Airways or American Airlines. If routing via the USA, be aware that live animal cargo transit through US airports involves USDA requirements."},
      {"q": "Does Costa Rica require a rabies titre test for UK pets?", "a": "A rabies titre test is not a standard SENASA requirement for dogs and cats imported from the UK. A current rabies vaccination and APHA-endorsed health certificate are the primary requirements. Always confirm the current position with SENASA at senasa.go.cr before travel as requirements can change."},
      {"q": "Who endorses the UK health certificate for Costa Rica?", "a": "The health certificate must be signed by your vet and then endorsed by APHA (Animal and Plant Health Agency). Use a vet who is familiar with the APHA endorsement process and the specific Costa Rica certificate format. Allow several days for the APHA endorsement on top of the vet appointment."}
    ]
  },
  {
    "slug": "australia-to-canada-pet-transport-guide",
    "title": "Pet Transport from Australia to Canada: Rules, Timing and the Best Airlines",
    "description": "Shipping a dog or cat from Australia to Canada. CFIA requirements, Australian export certificate, rabies vaccination, and which airlines fly pets on this long-haul route.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Australia", "Canada", "route guide", "dog", "cat"],
    "body": """Australia to Canada is a long-haul move -- typically 20 to 24 hours of flying time including a connection. The good news is that Canada's pet import requirements for Australian-origin dogs and cats are relatively straightforward, and the airlines serving this corridor have solid live animal programmes.

## Canada's Requirements for Australian Pets

Canada's pet import rules are administered by the Canadian Food Inspection Agency (CFIA). For dogs and cats from Australia, the requirements are notably lighter than for many other origins:

- Dogs must have a rabies vaccination that is current and valid on arrival
- Cats have no rabies vaccination requirement from CFIA (as Canada requires it only for dogs from rabies-risk countries -- Australia is considered low-risk)
- A health certificate is not strictly required by CFIA for dogs and cats from Australia, but your airline will almost certainly require one for the cargo booking
- Microchip is strongly recommended and required by most airlines

The simple CFIA rules do not mean you can skip the airline requirements. Airlines have their own health certificate and documentation demands which are often more stringent.

## Australian Export Requirements

Before your pet can leave Australia, the Australian Government Department of Agriculture, Fisheries and Forestry (DAFF) must issue an export permit. DAFF also requires that the pet has been examined by an accredited vet and meets any destination-country requirements.

For Canadian entry, DAFF's export health certificate will confirm your dog's rabies vaccination and general health. Apply to DAFF for the export permit well ahead of your travel date.

## Airlines for Australia to Canada

Air Canada and Qantas are the most relevant carriers for this route. Both have live animal cargo programmes. Common routings include:

- Qantas via Los Angeles (LAX) or Dallas (DFW) then connecting to a Canadian city -- check that the US connecting carrier accepts live animals and note that the USDA rules on transit apply
- Air Canada from Sydney or Melbourne via a US hub, or via Auckland
- United Airlines via Los Angeles connecting to Canada

The Vancouver (YVR) arrival point is the most common for Sydney-origin pets as it involves a US west coast transit.

## Summary Checklist

- DAFF export permit and health certificate (Australia)
- Rabies vaccination for dogs (current)
- CFIA notification if required for your specific situation
- Microchip
- IATA-compliant crate (large for most dog breeds on this distance)
- Confirm each airline leg accepts live animals
""",
    "faqs": [
      {"q": "Do I need a health certificate to bring my dog from Australia to Canada?", "a": "CFIA does not require a health certificate for dogs and cats arriving from Australia for non-commercial personal pets. However, your airline will require a health certificate for the cargo booking. Use a vet endorsed by Australia's DAFF to issue the export health certificate, which also satisfies the airline's documentation requirement."},
      {"q": "How long does the journey take for a pet from Australia to Canada?", "a": "The flight from Sydney or Melbourne to Toronto or Vancouver involves at least one stop, typically in the USA or through Auckland. Total journey time including connections is usually 22 to 28 hours depending on the routing. Use a specialist pet transport company for such long journeys to ensure the crate setup, water access, and handover protocols are correctly managed."},
      {"q": "Does my cat need a rabies vaccination to enter Canada from Australia?", "a": "CFIA does not require a rabies vaccination for cats from Australia, which is considered a low-risk origin. However, your airline may require it for their own live animal documentation. Check with your airline cargo team when booking the live animal space."}
    ]
  },
  {
    "slug": "usa-to-south-africa-pet-transport-guide",
    "title": "Pet Transport from USA to South Africa: DALRRD Permits, Airlines and the Process",
    "description": "Guide to shipping a dog or cat from the USA to South Africa. Import permit from DALRRD, health certificate, rabies requirements and which airlines serve Johannesburg.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["USA", "South Africa", "route guide", "dog", "cat"],
    "body": """South Africa is a popular destination for American expats and returning South Africans, and the country accepts dogs and cats from the USA. The process has a few steps but is well-understood by specialists.

## South Africa's Requirements for US-Origin Pets

The Department of Agriculture, Land Reform and Rural Development (DALRRD) regulates live animal imports. Requirements for dogs and cats from the USA include:

- An import permit from DALRRD (apply before travel; standard processing takes two to four weeks)
- A health certificate issued by a USDA APHIS accredited veterinarian and endorsed by USDA APHIS, issued within ten days of travel
- Rabies vaccination (current and valid on arrival)
- Core vaccinations (distemper, parvovirus, hepatitis for dogs; herpesvirus, calicivirus, panleukopenia for cats)
- Internal parasite treatment within a specified window before travel
- External parasite treatment (flea and tick) within a specified window before travel
- Microchip (ISO 11784/11785)

A rabies titre test is not a standard DALRRD requirement for US-origin pets, but confirm the current position when applying for your import permit.

## Getting the DALRRD Import Permit

Apply to DALRRD before booking flights. The import permit specifies the port of entry (typically OR Tambo International Airport in Johannesburg), the species and breed, and the required treatments. Keep the permit number -- you will need it when booking the airline cargo space.

## Airlines for USA to South Africa

South African Airways (SAA) historically operated this route but has had operational disruptions. The most reliable current carriers for this corridor are:

- Delta Air Lines via Atlanta (ATL) -- Delta accepts live animal cargo on applicable long-haul routes
- United Airlines via Newark (EWR) or Washington (IAD)
- British Airways via London Heathrow -- pets travel as cargo on the US-UK leg and the UK-Johannesburg leg (two bookings required)
- Lufthansa via Frankfurt -- a popular routing for hold pets

## Summary Checklist

- DALRRD import permit (apply 2-4 weeks before)
- USDA APHIS-endorsed health certificate, within 10 days of departure
- Rabies vaccination (current)
- Core vaccinations
- Internal and external parasite treatments
- Microchip
- IATA-compliant crate
""",
    "faqs": [
      {"q": "How do I get a pet import permit for South Africa?", "a": "Apply to DALRRD (Department of Agriculture, Land Reform and Rural Development) before your travel date. Allow two to four weeks for standard processing. The permit specifies your port of entry, the animal description, and the treatment requirements. Apply via the DALRRD website or contact their import control section directly."},
      {"q": "Does South Africa require a rabies titre test for pets from the USA?", "a": "A rabies titre test is not a standard DALRRD requirement for pets arriving from the USA. A current USDA APHIS-endorsed health certificate and valid rabies vaccination are the primary requirements. Confirm the current rules when you apply for your import permit, as requirements can change."},
      {"q": "Which airlines fly pets from the USA to Johannesburg?", "a": "Delta Air Lines and United Airlines both serve OR Tambo International Airport (JNB) from the USA and accept live animal cargo on applicable routes. British Airways via London and Lufthansa via Frankfurt are also popular options. Contact the airline cargo team of your chosen carrier to book the live animal space."}
    ]
  },
  {
    "slug": "travelling-with-a-border-terrier-internationally",
    "title": "Travelling Internationally with a Border Terrier",
    "description": "Border Terriers travel well but have specific documentation needs for international moves. This guide covers health certs, airline crate sizing, breed restrictions and key routes.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Border Terrier", "breed guide", "travel", "dog"],
    "body": """Border Terriers are sturdy, adaptable little dogs. They handle travel better than many breeds -- they are not brachycephalic, they are small enough for in-cabin options on some routes, and their temperament tends towards calm pragmatism rather than anxiety. That said, international travel with a Border Terrier still needs careful planning.

## Are Border Terriers Restricted Anywhere?

Border Terriers are not subject to breed-specific legislation in most countries. They appear on no banned breed lists that we are aware of. This makes international travel considerably simpler compared to breeds like Rottweilers or American Pit Bull Terriers, which face restrictions in some countries.

Always confirm with your destination country's authorities, as local rules can differ from national rules and can change.

## Cabin or Hold Travel?

Border Terriers typically weigh between 5 and 7 kg. The combined weight of the dog and a soft-sided carrier is usually in the range of 7 to 9 kg -- which falls within the in-cabin limit of some airlines (typically 8 to 10 kg combined).

Airlines that may accept a Border Terrier in cabin on relevant routes include Lufthansa, Air France, KLM, and TAP Air Portugal (for EU/European routes). In-cabin acceptance varies by route, aircraft type, and availability, so always confirm before booking.

For long-haul routes (UK to Australia, USA to Japan, etc.), in-cabin is not available and your Border Terrier will travel as manifested cargo in a temperature-controlled hold. This is safe and well-managed on quality carriers.

## Crate Sizing for a Border Terrier

For hold travel, the standard crate size for a Border Terrier is typically an IATA-compliant size 2 or size 3 crate, depending on your individual dog's dimensions. The crate must be tall enough for your dog to stand at full height, long enough to lie down, and wide enough to turn around. Measure your specific dog rather than going by breed averages.

## Key Routes for Border Terrier Owners

Border Terriers are popular among UK and British expatriate communities. Common relocation routes include:

- **UK to Australia**: One of the most document-intensive routes. Rabies titre test, DAFF-approved vet, and a waiting period apply. Start eight to ten months before travel.
- **UK to USA**: USDA-endorsed health certificate, rabies vaccination, and microchip. Relatively straightforward.
- **UK to UAE**: UAE Ministry of Climate Change and Environment permit required. Breed clearance straightforward for Border Terriers.
- **UK to Canada**: Simpler than Australia. CFIA-compliant health certificate and current rabies vaccination.

## Getting Your Border Terrier Ready

Six to eight months before your move:
- Confirm breed clearance for your destination country
- Start the titre test process if required (Australia, Mauritius, some Gulf states)
- Confirm your airline's in-cabin weight limits and crate size requirements

Three to four months before:
- Begin crate training if your dog is not already comfortable
- Schedule all required vaccinations and treatments with your vet
- Apply for any required import permits

One to two weeks before:
- Final vet check and health certificate (check the specific window required by your destination)
- Final tapeworm treatment if required (Australia, UK)
""",
    "faqs": [
      {"q": "Can a Border Terrier travel in the cabin on a plane?", "a": "Border Terriers can sometimes travel in the cabin on shorter routes, as they are small enough to meet the weight limits of some airlines (combined weight under 8-10 kg depending on the carrier). In-cabin acceptance varies by airline, route, and aircraft type. For long-haul international flights, hold travel as manifested cargo is the standard option. Always confirm with your airline before booking."},
      {"q": "Are Border Terriers banned in any country?", "a": "Border Terriers are not subject to breed-specific bans in most countries and do not appear on restricted breed lists in any country we are aware of. This makes them relatively straightforward to relocate internationally. Always confirm with your specific destination country's authorities before travel."},
      {"q": "What crate size does a Border Terrier need for hold travel?", "a": "Most Border Terriers need an IATA-compliant size 2 or size 3 crate for hold travel. The crate must be large enough for your dog to stand at full height, lie down naturally, and turn around. Measure your individual dog and choose the crate accordingly, rather than relying on breed average sizes."}
    ]
  },
  {
    "slug": "travelling-with-a-miniature-schnauzer-internationally",
    "title": "Travelling Internationally with a Miniature Schnauzer",
    "description": "Everything Miniature Schnauzer owners need to know about international travel. Breed restrictions, cabin vs hold, crate sizing, and key routes covered.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Miniature Schnauzer", "breed guide", "travel", "dog"],
    "body": """Miniature Schnauzers are one of the more popular breeds among expat families -- they are smart, adaptable, and compact enough to qualify for in-cabin travel on some routes. Here is what owners need to know before booking an international move.

## Breed Restrictions for Miniature Schnauzers

Miniature Schnauzers are not on any banned breed list we are aware of. They are not classified as dangerous breeds in any country's legislation. This gives them a relatively unrestricted international passport.

Standard Schnauzers (medium-sized) and Giant Schnauzers are occasionally included in broader "guard dog" categories in some countries' import review processes, so confirm with your specific destination if you have one of the larger variants. For Miniature Schnauzers specifically, breed restrictions are generally not a concern.

## Cabin Travel with a Miniature Schnauzer

Miniature Schnauzers typically weigh between 4 and 8 kg. Combined with a soft-sided carrier, the total weight usually falls in the range of 6 to 10 kg, which is within the in-cabin limits of many European and some international airlines.

Airlines that accept small dogs in the cabin on relevant routes include Lufthansa, Air France, KLM, Swiss, and Austrian Airlines. In-cabin pets are typically limited to one or two per cabin per flight, so book this early and confirm at the time of reservation.

For routes where in-cabin is not available (Australia, Japan, some Middle East destinations), your Miniature Schnauzer will travel as hold cargo in a temperature-controlled section.

## Hold Travel Crate Sizing

Miniature Schnauzers travelling in the hold need an IATA-compliant crate sized so they can stand, lie down, and turn around comfortably. Most Miniature Schnauzers fit in a size 2 or size 3 IATA crate. Measure your specific dog -- width across the shoulders plus room to move is more important than breed averages.

## Key Routes for Miniature Schnauzer Owners

Miniature Schnauzers are popular in Germany, Switzerland, and across Europe -- not surprising given the breed's German origins. Common relocation routes:

- **Germany to USA**: Lufthansa accepts hold pets with a valid EU health certificate, US APHIS requirements on arrival.
- **UK to Australia**: The full DAFF process applies. Allow eight to ten months.
- **Switzerland to UAE**: Swiss Airlines or Emirates depending on routing. UAE import permit required.
- **Europe to Canada**: CFIA requirements for dogs include current rabies vaccination. Shorter preparation than Australia.

## Preparing Your Miniature Schnauzer

Schnauzers are alert and can be vocal when anxious. Crate training is particularly valuable for this breed -- a familiar crate reduces flight stress significantly. Begin crate training several months before the move so the crate feels safe and familiar by travel day.

Avoid feeding for four to six hours before travel. A light meal is acceptable if your dog is prone to anxiety, but check with your vet. Do not sedate without veterinary guidance -- most vets do not recommend sedation for hold travel as it can affect breathing at altitude.
""",
    "faqs": [
      {"q": "Can a Miniature Schnauzer travel in the cabin internationally?", "a": "Miniature Schnauzers often qualify for in-cabin travel on European routes, as they typically weigh 4-8 kg and fit within most airlines' combined weight limits. In-cabin acceptance depends on the airline, route, and aircraft type. For long-haul routes such as Europe-Australia or Europe-USA, hold travel is standard. Always confirm with your airline at the time of booking."},
      {"q": "Are Miniature Schnauzers subject to breed restrictions anywhere?", "a": "Miniature Schnauzers are not banned or restricted in any country we are aware of. They are not included in any dangerous dog legislation. This makes them one of the more straightforward breeds to relocate internationally. Always confirm with your specific destination authority as local rules can differ."},
      {"q": "How should I prepare my Miniature Schnauzer for a long international flight?", "a": "Start crate training several months before the move so your dog is comfortable in the travel crate. Introduce the crate gradually, feeding meals inside it and leaving it available as a rest space. On travel day, avoid a large meal for four to six hours before departure. Do not sedate without specific veterinary advice. A familiar-scented item in the crate can help with anxiety."}
    ]
  },
  {
    "slug": "travelling-with-a-labradoodle-internationally",
    "title": "International Travel with a Labradoodle: Routes, Restrictions and What to Prepare",
    "description": "Labradoodles are generally unrestricted internationally but face challenges with airline breed policies and crate sizing. This guide covers everything owners need.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Labradoodle", "breed guide", "travel", "dog"],
    "body": """Labradoodles are one of the most popular dogs in the world right now, and a huge number of expat families are trying to work out how to bring one when they relocate. The good news is that Labradoodles are not banned anywhere. The challenge is that they are often too large for cabin travel, and some airlines have confusing policies about crossbreeds.

## Breed Classification for Labradoodles

A Labradoodle is a cross between a Labrador Retriever and a Poodle -- neither of which appears on any banned breed list. The crossbreed itself is not restricted in any country we know of.

The complication is with documentation. Some countries ask for a breed to be declared on import paperwork. For a Labradoodle, the correct answer is "crossbreed (Labrador x Poodle)" or "mixed breed." Some airlines and some border agencies can be uncertain about how to process a non-pedigree breed declaration. Working with a pet transport specialist on this route avoids any confusion.

## Cabin vs Hold Travel

Most adult Labradoodles weigh between 14 and 35 kg depending on whether they are standard or miniature Labradoodle types. This puts them firmly in hold-cargo territory for virtually all international routes and all major airlines.

Miniature Labradoodles (typically 7 to 13 kg) may qualify for in-cabin on some European routes if the combined weight with a soft carrier falls within the airline's limit. Confirm the specific weight with your airline before assuming in-cabin is possible.

## Crate Sizing

Labradoodles vary significantly in size. Measure your dog carefully:
- Length: from tip of nose to base of tail, plus 10 cm
- Height: from floor to top of head or ears (whichever is taller), plus 10 cm
- Width: two times the width across the widest point of the shoulders

Most standard Labradoodles need an IATA-compliant size 4 or size 5 crate. A miniature Labradoodle may fit a size 3. Do not undersize -- airlines will reject a crate that is too small.

## Key Routes

- **UK to Australia**: The full DAFF process. Labradoodles are not on the restricted breed list. Allow eight to ten months.
- **UK to USA**: USDA-endorsed health certificate, microchip, current rabies vaccination.
- **UK to Canada**: CFIA requirements. Rabies vaccination. Simpler than Australia.
- **Europe to UAE**: UAE Ministry import permit. No breed restrictions for Labradoodles.

## Dealing with Poodle Airline Restrictions

Some airlines apply brachycephalic breed restrictions broadly and occasionally flag Poodles (incorrectly) or "Doodle" type dogs with uncertain breed tags. Labradoodles are not brachycephalic and should not be subject to brachycephalic restrictions. If your airline asks, clarify that your dog is a Labrador/Poodle cross with no brachycephalic ancestry and a clear nasal passage. Your vet can confirm this on the health certificate.
""",
    "faqs": [
      {"q": "Are Labradoodles banned in any country?", "a": "Labradoodles are not banned or restricted in any country we are aware of. As a Labrador-Poodle cross, neither parent breed appears on any banned breed list. Documentation should describe the dog as a crossbreed or mixed breed (Labrador x Poodle). Working with a pet transport specialist can avoid any administrative confusion around non-pedigree breed declarations."},
      {"q": "Can a Labradoodle travel in a plane cabin?", "a": "Most adult Labradoodles are too large for in-cabin travel. Standard Labradoodles typically weigh 14-35 kg and must travel as hold cargo. Miniature Labradoodles (7-13 kg) may qualify for in-cabin on some European routes if the combined weight with the carrier falls within the airline's limit. Confirm with your specific airline before booking."},
      {"q": "What crate size does a Labradoodle need?", "a": "Most standard Labradoodles need an IATA-compliant size 4 or 5 crate for hold travel. The crate must allow the dog to stand at full height, lie down naturally, and turn around comfortably. Measure your specific dog (length, height, width) and use those measurements to select the correct crate size. Do not rely on breed averages."}
    ]
  },
  {
    "slug": "travelling-with-a-shiba-inu-internationally",
    "title": "International Travel with a Shiba Inu: Japan Rules, Breed Notes and Routes",
    "description": "Shiba Inu owners planning international moves need to know about breed classification, airline policies and the Japan import process for returning home. Full guide here.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Shiba Inu", "breed guide", "travel", "dog", "Japan"],
    "body": """Shiba Inus are increasingly popular outside Japan, and many owners find themselves relocating and wondering how to manage the move. Whether you are taking a Shiba to Japan (or back), to the UK, or across to Australia, here is what you need to know.

## Breed Restrictions for Shiba Inus

Shiba Inus are not on any banned breed list and are not subject to breed-specific legislation in any country we know of. They are a Japanese Spitz-type breed, compact and athletic, and not classified as dangerous in any jurisdiction.

## Cabin or Hold?

Shiba Inus typically weigh between 7 and 11 kg. Combined with a carrier, they often fall just over the in-cabin weight limits of most airlines. Some small female Shibas may qualify for in-cabin on shorter European or Japanese domestic routes.

For most international routes, Shiba Inus travel in the cargo hold as manifested live animals. They handle this well compared to more anxious breeds -- Shibas are stoic and self-contained.

## Moving to Japan with a Shiba Inu

Returning a Shiba to Japan is one of the more demanding pet relocations in the world. Japan has a complex multi-step process managed by the Ministry of Agriculture, Forestry and Fisheries (MAFF) Animal Quarantine Service:

1. Microchip (ISO standard)
2. Two rabies vaccinations given at least thirty days apart
3. Rabies titre test (blood sample taken at least thirty days after the second vaccination, at an approved laboratory)
4. Advance inspection and paperwork filing with Japan's Animal Quarantine Service
5. A twelve-hour (or longer) quarantine on arrival if all requirements are met, or up to 180 days if they are not

Start the process a minimum of seven to eight months before travel to Japan. Missing any step extends the quarantine.

## Other Key Routes

- **UK to USA**: Standard USDA APHIS requirements. No breed-specific issues for Shiba Inus.
- **Japan to UK**: UK APHA-compliant health certificate, microchip, current vaccinations.
- **USA to Australia**: Australian DAFF requirements, titre test, waiting period.

## Temperament and Travel

Shiba Inus are known for independence and can be reserved with strangers. Introduce the crate well in advance of travel -- some Shibas take longer than most breeds to accept crate confinement. Once comfortable, they typically travel without distress.
""",
    "faqs": [
      {"q": "How long does it take to move a Shiba Inu to Japan?", "a": "Moving a dog to Japan requires a minimum of seven to eight months of preparation. The process involves two rabies vaccinations at least thirty days apart, a titre test at least thirty days after the second vaccination, advance filing with Japan's Animal Quarantine Service, and a quarantine period on arrival (minimum twelve hours with full compliance, up to 180 days if requirements are not met)."},
      {"q": "Can a Shiba Inu travel in the cabin on a plane?", "a": "Shiba Inus weigh 7-11 kg as adults. Combined with a carrier, this often exceeds the in-cabin limit of most airlines (typically 8-10 kg combined). Smaller female Shibas may qualify on some routes. For most international travel, a Shiba Inu will travel in the temperature-controlled cargo hold. Confirm with your airline at time of booking."},
      {"q": "Are Shiba Inus banned in any country?", "a": "Shiba Inus are not banned or restricted in any country we are aware of. They are not classified as dangerous breeds in any jurisdiction. This makes them relatively simple to relocate internationally compared to restricted breeds."}
    ]
  },
  {
    "slug": "travelling-with-an-australian-shepherd-internationally",
    "title": "International Travel with an Australian Shepherd",
    "description": "Australian Shepherds are medium-large working dogs. This guide covers crate sizing, airline policies, breed notes and key international routes for Aussie Shepherd owners.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Australian Shepherd", "breed guide", "travel", "dog"],
    "body": """Australian Shepherds -- confusingly -- are an American breed with no direct connection to Australia, but they are enormously popular globally. Owners relocating internationally with an Aussie Shepherd face no breed-specific bans but do need to plan for their size and energy levels during the journey.

## Breed Restrictions

Australian Shepherds are not banned in any country we know of. They do not appear on any dangerous dog legislation. International relocation for this breed is not complicated by breed restrictions.

## Cabin or Hold?

Adult Australian Shepherds weigh between 16 and 32 kg. This is well above in-cabin limits. Australian Shepherds travel in the temperature-controlled cargo hold on all international routes. There is no in-cabin option for an adult Aussie.

## Crate Sizing

Most Australian Shepherds need an IATA-compliant size 4 or size 5 crate. Measure your individual dog:
- Nose-to-tail length plus 10 cm determines the minimum crate length
- Standing height plus 10 cm determines the minimum crate height
- Two times the shoulder width determines the minimum crate width

A well-fitted crate is safer and more comfortable than an oversized one -- too much space means the dog can be thrown around during turbulence. The crate must meet IATA LAR specifications with a solid base, ventilated sides, secure spring-loaded door, and water and food dishes attached inside.

## Preparing an Energetic Breed for Travel

Australian Shepherds are high-drive working dogs. A calm travel day starts with good exercise the morning before the flight and a period of rest. Avoid high-energy play in the final two hours before travel.

Crate training is particularly important for this breed. Begin three to four months before the move. Feed meals in the crate, encourage voluntary entry, and work up to multi-hour crate sessions before the travel date.

## Key Routes

- **USA to UK**: APHA-endorsed health certificate, microchip, core vaccinations, tapeworm treatment.
- **UK to Australia**: Full DAFF process. Australian Shepherds are not related to Australian livestock lines and face no special Australian restrictions. Allow eight to ten months.
- **USA to Germany**: Lufthansa hold cargo, EU health certificate requirements.
- **USA to Canada**: CFIA requirements. Rabies vaccination. Simpler process.
""",
    "faqs": [
      {"q": "Does an Australian Shepherd need a specific crate size for international travel?", "a": "Most adult Australian Shepherds need an IATA-compliant size 4 or size 5 crate. The correct size depends on your individual dog's measurements. The crate must be tall enough for the dog to stand at full height, long enough to lie down naturally, and wide enough to turn around. Measure your dog and do not use breed averages."},
      {"q": "Are Australian Shepherds banned anywhere internationally?", "a": "Australian Shepherds are not banned or restricted in any country we are aware of. They are not included in any dangerous dog legislation. This makes them one of the more straightforward breeds to relocate internationally."},
      {"q": "How do I prepare an energetic Australian Shepherd for a long flight?", "a": "Start crate training several months before the move. Exercise your dog well the morning of travel, then allow a rest period before the flight. Avoid feeding for four to six hours before departure. Do not sedate without veterinary advice. A familiar-smelling blanket or item in the crate can reduce anxiety."}
    ]
  },
  {
    "slug": "how-to-choose-a-pet-transport-company",
    "title": "How to Choose a Pet Transport Company: What to Ask Before You Book",
    "description": "Not all pet transport companies are equal. This guide explains what IPATA membership means, what questions to ask, red flags to avoid and how to compare quotes.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["pet transport", "choosing a company", "IPATA", "practical guide"],
    "body": """Choosing a pet transport company is one of the most important decisions you make in an international move. A good operator coordinates every step -- documentation, airline booking, crate supply, vet liaison, import permits, and delivery at the other end. A poor one takes your money and leaves you dealing with problems alone at customs.

Here is how to tell the difference.

## The IPATA Standard

IPATA (the International Pet and Animal Transportation Association) is the main professional body for pet relocation specialists. IPATA members agree to a code of ethics, carry appropriate insurance, and have demonstrated experience in international live animal transport.

Membership alone does not guarantee quality, but it is a meaningful baseline filter. A company that is not an IPATA member and cannot explain why should give you pause.

Ask directly: "Are you an IPATA member?" If yes, you can verify membership at ipata.com. If no, ask what professional association they belong to and what standards they meet.

## What to Ask Any Pet Transport Company

**About their experience:**
- How many shipments have you done on this specific route (your origin to your destination)?
- Have you handled this breed before?
- Do you have contacts at the destination airport's quarantine station?

**About the process:**
- What documentation will I be responsible for and what will you handle?
- How do you book the airline cargo space and which carriers do you prefer for this route?
- What happens if the flight is cancelled or my pet is offloaded?
- Will my pet be in a climate-controlled facility if there is a transit stop?

**About costs:**
- Is your quote all-inclusive (documentation, airline fees, ground transport, quarantine if applicable)?
- Are there any costs not included in this quote?
- What is your payment and cancellation policy?

**About communication:**
- Who is my point of contact throughout the process?
- Will I receive updates when my pet is checked in, when the flight departs, and when my pet has cleared customs?

## Red Flags

- Vague or evasive answers about documentation responsibilities
- A quote that seems unusually low (often means airline fees, import permits, or vet costs are not included)
- No fixed point of contact or the same person handles everything across different time zones
- Unwilling to provide references from past clients on your route
- No mention of IATA compliance for crates

## Comparing Quotes

Pet transport quotes vary widely because the costs involved are route-specific. A like-for-like comparison needs:
- The same airline (or equivalent quality carrier)
- All documentation costs included
- Ground transport at origin and destination included
- Quarantine costs included where applicable

A very cheap quote that excludes airline fees is not comparable to an all-inclusive quote. Ask for a full cost breakdown.

## The Role of Your Own Vet

A good pet transport company works with your vet, not around them. They provide your vet with the correct health certificate template for your destination country and give the vet the correct timeline for treatments and endorsements.

If a company tells you the vet just needs to sign something and it does not matter what, walk away. The health certificate content and timing are critically important for many destination countries.
""",
    "faqs": [
      {"q": "What is IPATA and should I use an IPATA member?", "a": "IPATA (International Pet and Animal Transportation Association) is the main professional body for pet relocation companies. Members follow a code of ethics and have demonstrated experience in international live animal transport. Using an IPATA member is a sensible baseline requirement. Verify membership at ipata.com before paying any deposit."},
      {"q": "How do I know if a pet transport quote is all-inclusive?", "a": "Ask for an itemised cost breakdown. A genuine all-inclusive quote should cover airline cargo fees, documentation preparation, government endorsement fees, crate supply (if included), ground transport at origin, ground transport at destination, and quarantine fees where applicable. If any of these items are listed as separate or 'may apply', the headline quote is not all-inclusive."},
      {"q": "What should I ask a pet transport company before booking?", "a": "Ask about their experience on your specific route and with your breed. Ask who handles documentation and which airline they plan to use. Ask what happens if the flight is cancelled. Ask for a full cost breakdown. Ask for references from past clients on the same route. A professional company will answer all of these directly."}
    ]
  },
  {
    "slug": "pet-transport-insurance-explained",
    "title": "Pet Transport Insurance: What Is Covered and Do You Need It?",
    "description": "Does your pet need insurance for international travel? This guide explains what pet transport insurance covers, what it does not, and how to buy it.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["pet transport insurance", "practical guide", "costs"],
    "body": """Pet transport insurance is one of those topics that owners ask about after something goes wrong, rather than before. Understanding what is and is not covered before you book can save you significant money and stress.

## What Pet Transport Insurance Covers

Pet transport insurance typically covers:

- **Loss or death during transit**: If your pet dies as a result of the transport process (airline mishandling, climate failure, etc.), the policy pays out based on the pet's declared value.
- **Veterinary costs arising from transit**: If your pet requires emergency veterinary treatment as a direct result of the journey, medical costs may be covered.
- **Flight cancellation or delay costs**: Some policies cover the cost of re-booking a flight or extending a stay in a holding facility if the airline cancels your pet's flight.
- **Third-party liability**: For dogs travelling as cargo, some policies include third-party liability if your dog injures a handler.

## What Pet Transport Insurance Does NOT Cover

- Pre-existing conditions
- Deaths caused by the owner's failure to comply with import documentation requirements
- Quarantine costs resulting from incorrect paperwork
- The cost of the transport itself being refused because of breed bans
- Emotional distress (no policy covers your distress at your pet's delayed arrival)

## How to Value Your Pet for Insurance

Many policies ask for a declared value. This is the amount you would claim if the pet were lost. For pedigree dogs with known market values, use a realistic market figure. For rescue or non-pedigree animals, this is harder -- some policies have a fixed benefit regardless of declared value.

Be honest about value. Overclaiming can void a policy.

## Who Provides Pet Transport Insurance

Several specialist providers offer cover for live animal transit. Your pet transport company may have a policy that covers the transit period as part of their service -- ask specifically whether this is included in your quote.

You can also buy standalone cover through specialist animal insurance brokers. Some general travel insurance policies exclude live animals entirely, so check the terms carefully.

## Is It Worth It?

For long-haul transits on well-managed carriers with experienced operators, serious incidents are rare. However, for a high-value animal -- a pedigree show dog, a champion breeding animal, or simply a pet that means the world to your family -- the peace of mind from transit insurance is usually worth the cost.

The premium on most transit policies is modest relative to the overall cost of international pet transport.
""",
    "faqs": [
      {"q": "Does my regular pet insurance cover international transport?", "a": "Most standard pet insurance policies do not cover international transit by air. They typically cover veterinary costs for illness and injury, but exclude events that occur during commercial air transport. Check your policy wording carefully under exclusions. If your regular policy does not cover transit, consider a standalone pet transport insurance policy for the journey."},
      {"q": "What is the declared value for pet transport insurance?", "a": "The declared value is the amount you would claim if your pet were lost or died during transit. For pedigree animals, use a realistic current market value. For non-pedigree pets, use a reasonable figure based on the cost of rehoming a similar animal. Be honest -- overclaiming can void a policy and constitute insurance fraud."},
      {"q": "Does my pet transport company provide insurance for my pet?", "a": "Some pet transport companies include basic transit insurance as part of their service. Ask directly whether insurance is included in your quote and what exactly it covers. Many companies offer it as an optional add-on at an additional cost. If it is not included, ask your company to recommend a specialist provider."}
    ]
  },
  {
    "slug": "moving-to-japan-with-a-pet",
    "title": "Moving to Japan with a Pet: The Complete 2026 Guide",
    "description": "Japan has some of the strictest pet import rules in the world. This guide walks through every step of the MAFF Animal Quarantine Service process for dogs and cats.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Japan", "moving abroad", "import guide", "dog", "cat"],
    "body": """Moving to Japan with a dog or cat takes serious advance planning. Japan is one of the countries with the most rigorous pet import requirements in the world -- not because it is trying to be difficult, but because it is genuinely rabies-free and intends to stay that way. The good news is that if you follow the steps correctly, the process works and your pet arrives healthy and legally.

## Why Japan Is Strict

Japan has been rabies-free since 1956. The quarantine requirements exist to prevent reintroduction of the virus. The system is managed by the Ministry of Agriculture, Forestry and Fisheries (MAFF) through the Animal Quarantine Service (AQS).

## The Six-Step Process

The AQS runs a six-step process for dogs and cats entering Japan:

**Step 1 -- Microchip**
ISO 11784/11785 compliant microchip. Must be done before any vaccinations for the quarantine clock to count.

**Step 2 -- Rabies vaccination (first)**
Must be given after the microchip is in place. Primary vaccination.

**Step 3 -- Rabies vaccination (second)**
Must be given at least thirty days after the first vaccination.

**Step 4 -- Rabies titre test**
Blood sample taken at least thirty days after the second vaccination. Tested at a MAFF-approved laboratory. The antibody level must meet the required threshold. If it fails, the process restarts.

**Step 5 -- Waiting period**
At least 180 days must pass between the date the titre test blood sample was taken and the date of arrival in Japan. This is the minimum quarantine-reduction period.

**Step 6 -- Advance notification to AQS**
Submit your advance notification to the AQS at least forty days before arrival. This includes all documentation, flight details, and port of entry.

If all six steps are completed correctly, the quarantine period on arrival in Japan is reduced to a minimum of twelve hours. If any step is missed or incorrectly timed, the full 180-day quarantine applies at your cost.

## Total Preparation Time

From step 1 (microchipping) to arrival in Japan, the minimum total time is approximately seven to eight months. Most specialists recommend ten to twelve months to allow buffer for titre test rescheduling and administrative processing.

## MAFF-Approved Laboratories for the Titre Test

The blood sample must be sent to a MAFF-approved laboratory. In the UK, the approved laboratory is the APHA Weybridge laboratory. In the USA, approved labs include Kansas State Veterinary Diagnostic Laboratory and others. Check the AQS website (maff.go.jp/aqs) for the current approved laboratory list for your country.

## Arriving in Japan

Most international pets arrive at Narita (NRT) or Haneda (HND) near Tokyo, or Kansai (KIX) near Osaka. AQS stations are at all major international airports. Have all documents in order: advance notification confirmation, titre test result, health certificate, vaccination records, microchip documentation.

Japan Airlines (JAL) and ANA both have strong live animal cargo programmes and are the natural choice for flights into Japan.

## After Arrival

Once cleared by AQS, your pet is free to accompany you. Microchip and vaccination records should be maintained while in Japan. Registered veterinary clinics are available in all major Japanese cities.
""",
    "faqs": [
      {"q": "How long does it take to bring a pet to Japan?", "a": "The minimum preparation time for bringing a dog or cat to Japan is around seven to eight months. This accounts for the two rabies vaccinations at least thirty days apart, the titre test at least thirty days after the second vaccine, and the 180-day waiting period after the titre test. Most specialists recommend allowing ten to twelve months to avoid any timing errors that would require restarting the process."},
      {"q": "What is the quarantine period for pets arriving in Japan?", "a": "With all steps completed correctly -- including the 180-day post-titre-test waiting period -- the quarantine on arrival in Japan is a minimum of twelve hours. If any step was missed or incorrectly timed, the full 180-day quarantine applies at the owner's cost. This is why following the AQS timeline precisely is so important."},
      {"q": "Which laboratory should I use for the Japan rabies titre test?", "a": "The blood sample must be sent to a MAFF-approved laboratory. In the UK, the APHA Weybridge laboratory is approved. In the USA, Kansas State Veterinary Diagnostic Laboratory and others are on the approved list. Check the current list on the AQS website at maff.go.jp/aqs for your specific country."}
    ]
  },
  {
    "slug": "moving-to-thailand-with-a-pet",
    "title": "Moving to Thailand with a Pet: Bangkok Permits, Vaccines and What to Expect",
    "description": "Guide to moving to Thailand with a dog or cat. Department of Livestock Development import permit, health certificate requirements and what happens at Suvarnabhumi Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Thailand", "moving abroad", "import guide", "dog", "cat"],
    "body": """Thailand is home to one of the largest expatriate communities in Asia, and the number of foreign residents with pets is significant. Moving to Bangkok or Chiang Mai with a dog or cat is straightforward if the paperwork is done correctly.

## Thailand's Pet Import Requirements

The Department of Livestock Development (DLD) under the Ministry of Agriculture and Cooperatives regulates pet imports. Requirements for dogs and cats entering Thailand include:

- An import permit from the DLD (apply before travel, allow two to four weeks)
- A health certificate issued by a government-accredited vet in your country, within ten days of travel (in some cases, the certificate must be endorsed by your country's government veterinary authority)
- Rabies vaccination (current and valid on arrival)
- For dogs: core vaccinations including distemper, parvovirus, and hepatitis
- For cats: core vaccinations including herpesvirus, calicivirus, and panleukopenia
- Microchip (ISO 11784/11785)

A rabies titre test is not a standard DLD requirement for most Western origins, but confirm the current position for your specific country of origin when you apply for the import permit.

## Getting the Import Permit

Apply to the Bureau of Disease Control and Veterinary Services, Department of Livestock Development. The application can be made via the DLD website (dld.go.th) or through a Bangkok-based pet transport specialist. Allow two to four weeks.

## Flying into Bangkok

Suvarnabhumi Airport (BKK) is the main international hub. Don Mueang (DMK) handles some international routes. Bangkok is served by Thai Airways, Emirates, Qatar Airways, Lufthansa, British Airways, and many other carriers with live animal cargo programmes.

Thai Airways accepts live animals on applicable routes -- contact their cargo team. Emirates, Qatar Airways, and Lufthansa are also popular choices for routing pets to Bangkok.

On arrival, DLD officers carry out the inspection at the airport. Have your import permit, health certificate, vaccination records, and microchip documentation ready.

## Living with a Pet in Thailand

Veterinary care in Bangkok and major Thai cities is good. Bangkok has several international-standard veterinary hospitals. In resort towns and rural areas, care is more limited.

Heat and humidity are significant factors. Brachycephalic breeds (Pugs, French Bulldogs, English Bulldogs) are at higher risk in Thailand's climate. Take veterinary advice on managing your pet in tropical conditions.

Tick-borne diseases, heartworm, and other tropical parasites are present in Thailand. A prevention programme should start before or on arrival.
""",
    "faqs": [
      {"q": "How do I apply for a pet import permit for Thailand?", "a": "Apply to the Bureau of Disease Control and Veterinary Services at Thailand's Department of Livestock Development (dld.go.th). Allow two to four weeks for processing. You will need to provide your pet's microchip number, vaccination records, and planned arrival details. Many owners use a Bangkok-based pet transport specialist to manage the permit application."},
      {"q": "Does Thailand require a rabies titre test for pet import?", "a": "A rabies titre test is not a standard requirement for pets entering Thailand from most Western countries. A current rabies vaccination and DLD-endorsed health certificate are the primary requirements. Confirm the current rules for your specific origin country with the DLD when you apply for your import permit."},
      {"q": "Which airlines fly pets to Bangkok as cargo?", "a": "Thai Airways, Emirates, Qatar Airways, Lufthansa, and British Airways all serve Suvarnabhumi Airport (BKK) and have live animal cargo programmes on applicable routes. Contact the cargo team of your chosen carrier directly to book the live animal space. Confirm that the specific aircraft type on your route accepts live animals in the hold."}
    ]
  },
  {
    "slug": "moving-to-philippines-with-a-pet",
    "title": "Moving to the Philippines with a Pet: BAI Requirements and What to Know",
    "description": "Guide to importing a dog or cat to the Philippines. Bureau of Animal Industry veterinary import clearance, health certificate, vaccinations and Manila airport process.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Philippines", "moving abroad", "import guide", "dog", "cat"],
    "body": """The Philippines is home to a large expatriate community, particularly in Manila and Cebu, and many residents keep dogs and cats. The import process is managed by the Bureau of Animal Industry (BAI), and while it has several steps, it is well-understood by specialist pet transport companies.

## BAI Requirements for Pet Import

The Bureau of Animal Industry (BAI) under the Department of Agriculture regulates live animal imports. For dogs and cats entering the Philippines, the requirements include:

- A Veterinary Import Clearance (VIC) from the BAI (apply before travel, allow two to four weeks)
- A health certificate issued by an official government veterinarian in your country, within ten days of travel
- Rabies vaccination (current and valid on arrival)
- For dogs: leptospirosis vaccination in addition to core vaccines
- For cats: core vaccinations
- Microchip (ISO standard)
- A clean bill of health with no signs of infectious disease

The VIC is the critical document -- no pet enters the Philippines without it. Apply at bai.da.gov.ph.

## Quarantine Requirements

Pets arriving in the Philippines undergo an inspection by BAI officers at Ninoy Aquino International Airport (MNL) or other ports of entry. Animals with correct documentation and a clean health inspection are typically released without a prolonged quarantine.

Pets arriving without the VIC or with incomplete documentation face detention and may be refused entry.

## Airlines for Philippines Routes

Philippine Airlines (PAL) and Cebu Pacific are the main carriers, but their international live animal policies are limited. For international pet cargo arriving in Manila, the most reliable carriers are:

- Qatar Airways via Doha -- Qatar accepts live animals on many routes including Manila
- Cathay Pacific via Hong Kong -- Cathay has strong cargo operations to Manila
- Singapore Airlines via Singapore -- reliable live animal cargo programme
- Emirates via Dubai

## Practical Notes

Manila is hot, humid, and tropical. Heat stress is a concern for all pets on arrival and during transport. Ensure your crate is well-ventilated and arrange for early-morning flights where possible to avoid peak daytime heat on the ground.

Veterinary facilities in Manila and Cebu are reasonable, with international-standard clinics in the business districts.
""",
    "faqs": [
      {"q": "What is the Veterinary Import Clearance for the Philippines?", "a": "The Veterinary Import Clearance (VIC) is a permit issued by the Bureau of Animal Industry (BAI) that must be obtained before your pet can enter the Philippines. Apply at bai.da.gov.ph at least two to four weeks before travel. The VIC specifies the conditions under which your pet may enter. No pet enters the Philippines without a valid VIC."},
      {"q": "Does my dog need extra vaccinations to enter the Philippines?", "a": "Yes. In addition to core vaccinations, dogs entering the Philippines are typically required to have a current leptospirosis vaccination. Cats require standard core vaccinations. Confirm the complete vaccination list with the BAI or your pet transport specialist when applying for the Veterinary Import Clearance."},
      {"q": "Which airline is best for flying a pet to Manila?", "a": "Qatar Airways via Doha, Cathay Pacific via Hong Kong, and Singapore Airlines via Singapore are among the most reliable carriers for live animal cargo to Ninoy Aquino International Airport (MNL). Philippine Airlines' international live animal cargo service is limited for inbound shipments. Contact the cargo team of your chosen carrier to confirm availability and make the booking."}
    ]
  },
  {
    "slug": "moving-to-vietnam-with-a-pet",
    "title": "Moving to Vietnam with a Pet: NAHABS Permits, Vaccines and Ho Chi Minh City",
    "description": "Complete guide to importing a dog or cat to Vietnam. Ministry of Agriculture permits, health certificate requirements, rabies vaccines and arriving at Tan Son Nhat Airport.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Vietnam", "moving abroad", "import guide", "dog", "cat"],
    "body": """Vietnam's growing expatriate community, particularly in Ho Chi Minh City and Hanoi, means more people are navigating the country's pet import process. The system is manageable with preparation, but it differs depending on whether you are arriving at a northern or southern airport.

## Vietnam's Pet Import Requirements

The Ministry of Agriculture and Rural Development (MARD) regulates live animal imports through the Department of Animal Health (DAH) and the National Agro-Forestry-Fisheries Quality Assurance Department (NAFIQAD). For dogs and cats, the requirements typically include:

- An import permit from the competent authority (MARD/DAH)
- A health certificate issued by an official government veterinarian in your country, within ten days of travel
- Rabies vaccination (current and valid on arrival)
- Core vaccinations for dogs and cats
- Microchip (ISO standard recommended)
- An animal health certificate confirming the animal is free from infectious disease

Requirements can vary by origin country. Work with a Vietnamese-based pet transport specialist or the local MARD office to confirm the current documentation list for your origin.

## Arriving in Vietnam

Tan Son Nhat Airport (SGN) in Ho Chi Minh City and Noi Bai Airport (HAN) in Hanoi are the main international entry points. Customs and MARD inspection happens on arrival. Keep all documents accessible.

## Airlines for Vietnam Routes

Vietnam Airlines, Qatar Airways, Thai Airways, Singapore Airlines, and Cathay Pacific all serve major Vietnamese airports and have live animal cargo programmes on applicable routes. Singapore Airlines via Singapore is a commonly used routing for pets arriving in Vietnam from Europe.

## Practical Notes

Vietnam is hot and humid in the south year-round. Brachycephalic breeds are at higher risk in this climate. Ensure your crate is well-ventilated and discuss heat precautions with your vet.

Veterinary care in Ho Chi Minh City and Hanoi has improved significantly. Several clinics now serve the expatriate community with international standards.

Tick, heartworm, and other tropical parasite prevention is important from arrival day.
""",
    "faqs": [
      {"q": "What documents does a dog need to enter Vietnam?", "a": "Dogs entering Vietnam need an import permit from MARD/Department of Animal Health, a health certificate from an official government veterinarian issued within ten days of travel, a current rabies vaccination, core vaccinations, and microchip documentation. Requirements can vary by origin country -- confirm with the Vietnamese competent authority or a local pet transport specialist before travel."},
      {"q": "Can I bring a cat to Vietnam?", "a": "Yes. Cats can be imported into Vietnam with the appropriate documentation, including an import permit, health certificate, current vaccinations, and microchip. The same process through the Ministry of Agriculture and Rural Development applies. Confirm the current requirements for your specific origin country."},
      {"q": "Which airline is best for flying a pet to Ho Chi Minh City or Hanoi?", "a": "Singapore Airlines via Singapore, Qatar Airways via Doha, and Cathay Pacific via Hong Kong are commonly used for live animal cargo to Vietnam. Singapore Airlines in particular has a reliable live animal programme and a convenient Singapore hub for connections to both Ho Chi Minh City and Hanoi."}
    ]
  },
  {
    "slug": "what-happens-at-destination-customs-with-your-pet",
    "title": "What Happens at Customs When Your Pet Arrives Internationally",
    "description": "What to expect when your dog or cat clears customs at an international airport. The inspection process, what officials check, and what can go wrong.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["customs", "arrival", "practical guide", "import process"],
    "body": """The moment your pet lands is when all the preparation either pays off or falls apart. Understanding the customs arrival process before you travel helps you know what to expect and what to have ready.

## Who Inspects Your Pet at Customs

Depending on the country, your pet is inspected by one or more of the following:

- **Agricultural or veterinary officers** from the national authority (USDA APHIS, Australian DAFF, APHA in the UK, etc.) -- these are the key officials for import clearance
- **Customs officers** -- check for the import permit and validate documentation against the manifest
- **Quarantine station staff** -- if a quarantine period applies, these officials take charge of your pet

In most countries, the veterinary officer's clearance is what matters most. If the paperwork is correct and the animal passes a physical health check, clearance is usually quick.

## What Officials Check

The veterinary officer will typically check:
- Microchip (scanned against the documents)
- Health certificate (within the valid date window, correctly signed and endorsed)
- Vaccination records (rabies, core vaccines, any specific destination requirements)
- Titre test result (for countries that require it)
- Import permit (where applicable)
- Parasite treatments (tapeworm, flea/tick treatments recorded and within the required window)
- Physical condition of the animal (healthy, not showing signs of disease)
- Crate compliance (IATA standards, labelling)

They are checking that every item on the import requirement list is present and valid. A thorough document preparation process should mean there are no surprises here.

## What Can Go Wrong

- **Expired health certificate**: The most common problem. Health certificates have a narrow validity window (typically ten days from issue date). If your flight is delayed and you miss the window, you may need a new certificate.
- **Missing endorsement**: Some countries require a government stamp or endorsement on the vet's certificate. If the private vet signed it but the government endorsement is missing, the certificate is invalid.
- **Wrong microchip number**: The number on the documents must exactly match the chip in the animal. Transcription errors cause significant problems.
- **Titre test not meeting the required level**: If the test passed but the level recorded is borderline, officers may question it.
- **Arriving at the wrong port of entry**: Some countries (Australia is a notable example) only accept pets at specific airports. Check this carefully.

## If Something Goes Wrong

If an officer finds a problem with your documentation, stay calm. Ask clearly what the specific issue is and whether it can be resolved on the spot. Some documentation issues can be corrected in real time. Others -- like an expired certificate -- cannot be and may result in your pet being held at a quarantine station while the issue is resolved.

Having a pet transport specialist's emergency contact number is useful in these situations. A good specialist has dealt with customs problems before and can often help navigate the resolution process remotely.
""",
    "faqs": [
      {"q": "What documents should I carry when my pet arrives at customs?", "a": "Have all documents in a single folder: health certificate, import permit (where required), vaccination records, titre test results (if applicable), microchip documentation, and parasite treatment records. If your country required a government endorsement on the health certificate, ensure that endorsement is present and legible."},
      {"q": "Can my pet be refused entry at customs?", "a": "Yes. Pets can be refused entry if documentation is missing, expired, or incorrect. The most common reasons are an expired health certificate, missing government endorsement, microchip number mismatch, or absence of a required import permit. Refused pets are typically held at the airport quarantine facility at the owner's cost while the issue is resolved, or returned to the country of origin."},
      {"q": "How long does customs clearance take for a pet?", "a": "With all documentation correct, customs clearance for a pet at most airports takes between thirty minutes and two hours. Countries with strict biosecurity regimes (Australia, New Zealand, Japan) have more thorough processes that can take longer. If your pet is arriving as cargo and you are arriving as a passenger on the same flight, allow time for the cargo to be processed before attempting to collect."}
    ]
  },
  {
    "slug": "vaccinations-your-pet-needs-for-international-travel",
    "title": "Which Vaccinations Does Your Pet Need for International Travel?",
    "description": "A country-by-country guide to pet vaccination requirements for international travel. Rabies, core vaccines, titre tests and which countries require what.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["vaccinations", "rabies", "titre test", "practical guide", "health certificate"],
    "body": """Every country that allows pet imports has a list of required vaccinations. Getting these right -- and getting the timing right -- is one of the most important steps in any international pet move.

## The Universal Requirement: Microchip First

Before any vaccination counts toward an international move, your pet must be microchipped. The vaccination record is only valid if the vaccine was given after the microchip was implanted. This is a specific rule for countries with titre test requirements, but it is good practice for all international travel.

ISO 11784/11785 standard microchips are accepted everywhere. Some older chip standards may not be readable by foreign scanners -- check your microchip type.

## Rabies Vaccination: Required Almost Everywhere

Rabies vaccination is required for entry into almost every country in the world. The specific requirements vary:

- **Single current vaccination**: Most countries require a valid rabies vaccination (given within the past one to three years depending on vaccine type). No titre test needed.
- **Rabies titre test countries**: Australia, New Zealand, Japan, Mauritius, Bahrain, Oman, and several others require a rabies titre test confirming the vaccination has produced sufficient antibody levels. These countries also impose a waiting period after the test.

## Core Vaccines for Dogs

The standard core vaccines for dogs that most countries reference:
- Distemper
- Parvovirus (CPV)
- Infectious Hepatitis (Adenovirus)
- Leptospirosis (required specifically by some countries, notably the UK, Philippines, and several Caribbean nations)

Your vet's vaccination certificate should list each vaccine, the date given, and the brand/batch number.

## Core Vaccines for Cats

Standard core vaccines for cats:
- Feline herpesvirus (FHV-1)
- Feline calicivirus (FCV)
- Feline panleukopenia (FPV)

Feline leukaemia (FeLV) is required by some countries. Rabies vaccination for cats is required by all countries that require it for dogs.

## Country-Specific Additions

**Australia and New Zealand**: Titre test required. Two rabies vaccinations with a thirty-day gap, titre test thirty days after the second vaccine, 180-day wait before entry.

**Japan**: Same as Australia/New Zealand process plus formal AQS advance notification.

**Gulf States (UAE, Saudi Arabia, Oman, Bahrain, Kuwait, Qatar)**: Most require a titre test. Requirements vary slightly by country -- confirm with the specific Ministry before travel.

**EU countries**: For pets from third countries (non-EU), a valid EU-format health certificate and current rabies vaccination is the baseline. Some EU countries have additional requirements.

**USA**: Rabies vaccination for dogs (current, given at least thirty days before arrival if first vaccination). No titre test required. Recent CDC changes added restrictions on dogs vaccinated outside the USA -- check CDC current rules.

## Timing Your Vaccinations

Leaving vaccinations to the last minute is the most common mistake. Many vaccines need to be given at a minimum number of days before travel. A titre test (if required) adds three to seven months to the minimum preparation window.

Speak to your vet at least six months before your move to confirm your pet's vaccination status and plan any boosters or primary courses needed.
""",
    "faqs": [
      {"q": "Which countries require a rabies titre test for pet import?", "a": "Countries that require a rabies titre test for pet import include Australia, New Zealand, Japan, Mauritius, Oman, Bahrain, Kuwait, and several others. These countries have rabies-free or low-risk status and require the titre test as proof that the vaccination has produced sufficient antibody levels. The test must be done at an approved laboratory and is followed by a mandatory waiting period before travel."},
      {"q": "Does my cat need a rabies vaccination for international travel?", "a": "Yes, in most countries that require rabies vaccination for dogs, the same requirement applies to cats. Australia, New Zealand, Japan, and Gulf states all require rabies vaccination and titre testing for cats as well as dogs. The process and timeline are the same as for dogs."},
      {"q": "How long before travel should my pet be vaccinated?", "a": "Core vaccines should be given well before any international move. The minimum timing depends on your destination: a current booster is sufficient for most countries (rabies vaccination valid within the past one to three years). For titre test countries (Australia, Japan, etc.), allow a minimum of seven to eight months from starting the process to arrival. Always consult your vet and the destination country's official requirements."}
    ]
  },
  {
    "slug": "uk-to-bahrain-pet-transport-guide",
    "title": "Pet Transport from UK to Bahrain: Requirements, Titre Test Timeline and Airlines",
    "description": "Guide to shipping a dog or cat from the UK to Bahrain. Ministry permit, rabies titre test, APHA health certificate, breed checks and which airlines fly pets on this route.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["UK", "Bahrain", "route guide", "dog", "cat", "Middle East"],
    "body": """Bahrain is a popular base for British expats, and many want to bring their dogs and cats. The process is more involved than most European routes because of the rabies titre test requirement, but it is well-understood and manageable with a four-to-five month lead time.

## What Bahrain Requires from UK-Origin Pets

The Agricultural Affairs Directorate under Bahrain's Ministry of Works, Municipalities Affairs and Urban Planning manages pet imports. For dogs and cats arriving from the UK, the requirements are:

- Import permit from the Agricultural Affairs Directorate (apply before the titre test is taken ideally, so you have the permit specifications confirmed)
- Microchip (ISO 11784/11785)
- Rabies vaccination (current; must be given at least thirty days before the titre test blood draw)
- Rabies titre test at a MAFF-approved laboratory (the blood sample must be taken at least thirty days after the most recent rabies vaccination)
- Three-month waiting period after the titre test date before travel to Bahrain
- APHA-endorsed health certificate from a UK vet, issued within ten days of departure
- Core vaccinations (distemper, parvovirus, hepatitis for dogs; herpesvirus, calicivirus, panleukopenia for cats)
- External parasite treatment close to travel date
- Breed clearance (some breeds are restricted -- confirm before starting the process)

## UK-Specific Steps

The health certificate must be issued by a UK vet who is RCVS-registered and familiar with the Bahrain certificate format. The certificate must then be endorsed by APHA (Animal and Plant Health Agency). This endorsement process takes several days, so allow time in your planning.

For the titre test, the blood sample is taken by your vet and sent to an approved laboratory. Results typically take two to three weeks. The waiting period begins from the date the sample was taken, not the date results arrived.

## Airlines for UK to Bahrain

There are no non-stop flights from the UK to Bahrain with live animal cargo service. Common routings:

- **Gulf Air via Bahrain (BAH)**: Gulf Air is Bahrain's national carrier. Contact Gulf Air Cargo for live animal bookings on the London (LHR) to Bahrain route.
- **British Airways via Bahrain**: British Airways serves BAH and has live animal cargo on applicable routes.
- **Emirates via Dubai**: A routing that avoids the need for UK-to-Bahrain direct cargo but requires two legs -- confirm both accept live animals.
- **Qatar Airways via Doha**: Doha is very close to Bahrain geographically, and this routing works well for cargo.

## Summary Timeline for UK to Bahrain

| Month | Action |
|-------|--------|
| Month 1 | Apply for import permit. Confirm breed clearance. |
| Month 1 | Microchip (if not already done). |
| Month 1 | Rabies vaccination (or confirm booster is current). |
| Month 2 | Wait 30 days after vaccination. |
| Month 2 | Blood sample for rabies titre test at approved laboratory. |
| Month 3-4 | Three-month wait from titre test sample date. |
| Month 4-5 | Book airline cargo space. Schedule APHA health certificate. |
| Within 10 days of departure | APHA-endorsed health certificate issued. |
| Travel day | Depart. |
""",
    "faqs": [
      {"q": "How long does it take to move a pet from the UK to Bahrain?", "a": "The UK to Bahrain pet transport process takes a minimum of around four to five months. This accounts for the rabies vaccination timing before the titre test, the titre test itself, the three-month waiting period after the test, and the APHA-endorsed health certificate within ten days of departure. Start the process at least five months before your planned move date."},
      {"q": "Which laboratory should I use for the Bahrain rabies titre test from the UK?", "a": "The titre test blood sample must be tested at a laboratory approved by Bahrain's Agricultural Affairs Directorate. In the UK, the APHA Weybridge laboratory is the standard approved facility. Confirm the current approved laboratory list with the Bahrain Ministry or your pet transport specialist when applying for the import permit."},
      {"q": "Do I need an APHA endorsement on the health certificate for Bahrain?", "a": "Yes. The health certificate for Bahrain must be issued by a RCVS-registered UK vet and endorsed by APHA (Animal and Plant Health Agency). The endorsement process takes several days on top of the vet appointment. Allow for this in your planning so the certificate is endorsed and ready within the ten-day window before your travel date."}
    ]
  },
  {
    "slug": "how-to-prepare-your-cat-for-a-long-flight",
    "title": "How to Prepare Your Cat for a Long International Flight",
    "description": "Cats handle long-haul travel differently to dogs. This guide covers crate training, feeding, in-cabin vs hold options and how to reduce stress for your cat on a long flight.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["cats", "practical guide", "long-haul", "stress", "cabin"],
    "body": """Cats are famously independent, but that independence does not extend to enjoying air travel. Most cats find it stressful -- the noise, the smells, the movement, the strangers handling their crate. Your job in the preparation phase is to reduce every controllable source of stress so the unavoidable ones are easier to manage.

## In-Cabin vs Hold: The Cat Decision

For short to medium routes (within Europe, within Asia, North America internal), cats often qualify for in-cabin travel if they weigh under 8 to 10 kg combined with their carrier. In-cabin is generally better for cats because they can see, hear, and smell you.

For long-haul routes (UK to Australia, USA to Japan, Europe to South Africa), in-cabin is not available and cats travel in the temperature-controlled cargo hold. Hold travel is safe and well-managed on quality carriers -- the hold is climate-controlled and pressurised.

## Crate Training: The Most Important Preparation Step

Start at least three months before the flight. The goal is for your cat to choose to spend time in the crate voluntarily.

Week 1-2: Leave the crate open in your home with a familiar blanket inside. Do not close the door.
Week 3-4: Feed meals near the crate, then inside the crate.
Week 5-6: Close the crate door briefly during meals. Open immediately when the meal is finished.
Week 7-8: Increase the duration with the door closed. Add a familiar-scented item.
Month 2-3: Practice crate sessions of two to four hours with the door closed.

A cat that has spent months comfortable in its crate will handle travel far better than one introduced to the crate for the first time on travel day.

## Feeding on Travel Day

Do not fast your cat for longer than four hours before a flight. Unlike dogs, cats can develop hepatic lipidosis (fatty liver disease) relatively quickly with extended fasting. A small meal four hours before is fine.

Make sure fresh water is available in the crate. For hold travel, attach a water container inside the crate that your cat can drink from.

## Sedation: Mostly a Bad Idea

Most vets do not recommend sedating cats for air travel. Sedated cats cannot regulate their body temperature effectively, and the pressure changes during flight affect sedated animals differently. If your cat has severe flight anxiety, discuss options with your vet -- there are anti-anxiety approaches that do not involve full sedation.

## On Arrival

Your cat will likely be stressed on arrival. Find a quiet room and open the crate without forcing the cat out. Leave the crate available as a familiar retreat space. Food and water should be available but do not worry if your cat does not eat immediately -- this is normal. Most cats normalise within twenty-four to forty-eight hours.
""",
    "faqs": [
      {"q": "How long should I fast my cat before an international flight?", "a": "Do not fast your cat for more than four to six hours before a flight. Unlike dogs, cats are susceptible to hepatic lipidosis (fatty liver disease) with extended fasting. A small meal four hours before departure is appropriate. Ensure water is available in the crate for the duration of the journey."},
      {"q": "Should I sedate my cat for a long flight?", "a": "Most vets advise against sedating cats for air travel. Sedated cats cannot regulate body temperature effectively, and pressure changes during flight can affect sedated animals more severely. If your cat has significant anxiety, discuss anti-anxiety medications with your vet that do not involve full sedation. Crate training from an early stage is the most effective way to reduce flight stress."},
      {"q": "Is the cargo hold safe for cats on long-haul flights?", "a": "Yes. The cargo hold used for live animals is temperature-controlled and pressurised on the same system as the passenger cabin. On quality carriers with IATA-compliant procedures, hold travel is safe for healthy cats. The main stress factors are noise and unfamiliarity, both of which are reduced by thorough crate training before the journey."}
    ]
  },
  {
    "slug": "germany-to-australia-pet-transport-guide",
    "title": "Pet Transport from Germany to Australia: DAFF Rules, Titre Test and the Long Haul",
    "description": "Moving a dog or cat from Germany to Australia. Australian DAFF requirements, EU health certificate, rabies titre test timeline and best airlines for Frankfurt-Sydney routes.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["Germany", "Australia", "route guide", "dog", "cat"],
    "body": """Germany to Australia is one of the longer pet relocation routes, and Australia's strict biosecurity requirements make it one of the most document-intensive as well. German pet owners moving to Sydney, Melbourne, or Brisbane need to start the process at least eight to ten months before travel.

## Australia's DAFF Requirements for German Pets

The Australian Department of Agriculture, Fisheries and Forestry (DAFF) controls all live animal imports. Germany is not in Australia's Group 1 approved country list (which would allow simpler entry). German pets fall under Group 2 requirements, which include:

- Microchip (ISO 11784/11785)
- Two rabies vaccinations given at least thirty days apart
- Rabies titre test at a DAFF-approved laboratory (blood sample taken at least thirty days after the second vaccination)
- Thirty-day pre-export residency in an approved country or region (Germany qualifies)
- Treatment for external parasites (tick treatment), flea treatment, and internal parasite treatment within specified windows before travel
- An official Australian export health certificate issued by a DAFF-approved vet in Germany and endorsed by the German competent authority (Friedrich-Loeffler-Institut or equivalent state authority)
- A ten-day quarantine in Australia after arrival at an approved facility (Melbourne AQIS station or similar)

## DAFF-Approved Laboratories for German Titre Tests

The blood sample from Germany must be sent to a DAFF-approved laboratory. Several laboratories in Germany and Europe are approved for Australian titre tests. Your vet will know which facilities to use, or check the DAFF website (agriculture.gov.au) for the current list.

## Airlines from Germany to Australia

Lufthansa is the natural first choice for Germany to Australia pet cargo. Lufthansa operates direct Frankfurt (FRA) to Sydney (SYD) and Melbourne (MEL) flights and has a well-established live animal cargo programme. Contact Lufthansa Cargo to book the live animal space.

Alternative routings include Singapore Airlines via Singapore and Qantas via a Southeast Asian hub.

## The Quarantine Period

All dogs and cats arriving in Australia undergo ten days of quarantine at the Melbourne Airport Animal Quarantine Station (or occasionally another approved facility). The quarantine costs are paid by the owner. Expect costs of approximately AUD 2,000 to AUD 3,500 depending on the animal and the current fee schedule.

## Summary Timeline for Germany to Australia

- Month 1: Microchip. First rabies vaccination.
- Month 2: Second rabies vaccination (at least 30 days after first).
- Month 3: Blood sample for titre test (at least 30 days after second vaccination).
- Month 3-10: Wait for the 180-day minimum to pass after the titre test.
- Month 9-10: Book Lufthansa Cargo space. Arrange export health certificate.
- Travel day: Depart. Ten-day quarantine on arrival.
""",
    "faqs": [
      {"q": "How long does it take to move a pet from Germany to Australia?", "a": "The minimum preparation time for Germany to Australia is eight to ten months. This includes two rabies vaccinations at least thirty days apart, a titre test at least thirty days after the second vaccine, and a 180-day waiting period after the titre test. Add time for export certificate endorsement and airline booking. Start the process as early as possible."},
      {"q": "Is there a quarantine period for pets arriving in Australia from Germany?", "a": "Yes. All dogs and cats entering Australia undergo a mandatory ten-day quarantine at an approved facility on arrival. The quarantine takes place at the Melbourne Airport Animal Quarantine Station in most cases. Costs are paid by the owner and are typically AUD 2,000 to AUD 3,500 depending on the current fee schedule."},
      {"q": "Which airline is best for flying a pet from Germany to Australia?", "a": "Lufthansa is the primary choice for Germany to Australia pet cargo, operating direct Frankfurt (FRA) to Sydney (SYD) and Melbourne (MEL) routes with an established live animal cargo programme. Singapore Airlines via Singapore and Qantas via Southeast Asian hubs are alternative options. Contact the cargo team of your chosen carrier directly."}
    ]
  },
  {
    "slug": "france-to-australia-pet-transport-guide",
    "title": "Pet Transport from France to Australia: DAFF Process, Airlines and the Quarantine",
    "description": "Moving a dog or cat from France to Australia. DAFF requirements, titre test timeline, French health certificate process and which airlines fly pets on Paris-Sydney routes.",
    "date": "2026-05-07",
    "author": "PetTransportGlobal Editorial Team",
    "tags": ["France", "Australia", "route guide", "dog", "cat"],
    "body": """France to Australia is a popular relocation corridor, particularly for expats and returning Australians based in Paris or other French cities. The Australian DAFF process is demanding but well-understood, and several airlines operate useful services for this route.

## Australia's Requirements for French Pets

France falls under Australia's Group 2 import requirements. The DAFF requirements for dogs and cats from France are:

- Microchip (ISO 11784/11785), implanted before all vaccinations
- Two rabies vaccinations, at least thirty days apart
- Rabies titre test at a DAFF-approved laboratory, blood sample taken at least thirty days after the second vaccination
- 180-day waiting period after the titre test date before travel to Australia
- Treatment for ticks (at specific intervals before departure), fleas, and internal parasites
- Official Australian export health certificate issued by a DAFF-approved vet in France, endorsed by the French competent veterinary authority (DGAL -- Direction Generale de l'Alimentation)
- Ten-day quarantine in Australia on arrival

## French Health Certificate Process

The health certificate for Australia must be completed by a veterinarian enrolled in the DGAL export system. The certificate must be endorsed by the DGAL or your regional DRAAF (Regional Directorate for Food, Agriculture and Forestry). Allow a week to ten days for the endorsement process. The endorsed certificate must be issued within ten days of departure.

## Airlines from France to Australia

Air France is the natural starting point for Paris to Australia. Air France Cargo has an active live animal programme and operates routes from Paris Charles de Gaulle (CDG) to Sydney (SYD), Melbourne (MEL), and Brisbane (BNE) via connections.

Direct long-haul options also include:
- Singapore Airlines via Singapore -- strong cargo programme
- Qantas via Dubai or Singapore -- Qantas has detailed DAFF documentation guidance
- Cathay Pacific via Hong Kong

## Quarantine in Australia

The ten-day quarantine at Melbourne Airport Animal Quarantine Station applies to all arrivals from France. Costs are borne by the owner (typically AUD 2,000 to AUD 3,500). Your pet cannot be released to you until the ten days are complete and DAFF is satisfied with the animal's health.

## Summary Timeline for France to Australia

- Month 1: Microchip. First rabies vaccination.
- Month 2: Second vaccination (30+ days after first).
- Month 3: Titre test blood sample (30+ days after second vaccine).
- Months 3-10: 180-day wait.
- Month 9-10: Book airline cargo. Schedule DGAL-endorsed health certificate.
- Travel day: Depart. 10-day quarantine in Australia.
""",
    "faqs": [
      {"q": "How long does it take to relocate a pet from France to Australia?", "a": "The minimum timeline is eight to ten months from starting the process. Two rabies vaccinations at least thirty days apart, a titre test at least thirty days after the second vaccine, a 180-day post-titre-test waiting period, and the DGAL-endorsed health certificate within ten days of departure are all required. Start at least ten months before your planned travel date to allow buffer."},
      {"q": "Who endorses the health certificate for Australia from France?", "a": "The health certificate must be issued by a vet enrolled in the DGAL export system and then endorsed by the DGAL (Direction Generale de l'Alimentation) or the regional DRAAF. Allow seven to ten days for the endorsement on top of the vet appointment. The endorsed certificate is only valid for ten days from issue, so timing is critical."},
      {"q": "Which airlines fly pets from Paris to Australia?", "a": "Air France Cargo operates Paris CDG to Sydney and Melbourne with live animal cargo service. Singapore Airlines via Singapore and Qantas via connections are also reliable options. Cathay Pacific via Hong Kong is another commonly used routing. Contact the cargo team of your chosen airline to confirm availability and pricing for your specific travel dates."}
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
