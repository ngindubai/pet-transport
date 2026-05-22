"""
generate_p4_breeds.py
Task 4.4 — 30 additional breed guide pages.
Target: ~65 total (35 existing + 30 new).
"""

import os

CONTENT_DIR = os.path.join("site", "content", "breeds")

BREEDS = [
    # ----- popular dogs, no major bans -----
    {
        "slug": "golden-retriever",
        "title": "Flying with a Golden Retriever | Cargo Tips & Airline Rules",
        "description": "What you need to book cargo for a Golden Retriever. Crate sizing, airline options, health certificates, and destination requirements explained.",
        "breed_name": "Golden Retriever",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo with IATA-compliant crate", "notes": "Standard cargo booking applies. Crate must allow the dog to stand, turn, and lie down comfortably."},
            {"airline_name": "British Airways (varies by weight)", "policy": "Accepted in cargo", "notes": "Weight limits apply. Dog + crate combined weight must meet airline threshold."},
            {"airline_name": "Emirates (seasonal weight limits)", "policy": "Accepted in cargo with conditions", "notes": "Seasonal restrictions during peak summer months for large breeds. Confirm before booking."},
        ],
        "h1": "Golden Retriever Air Travel Guide",
        "overview": (
            "Golden Retrievers are one of the most popular family dogs in the world, and they travel internationally in cargo every day. There are no breed-specific bans against Golden Retrievers in any major destination country.\n\n"
            "That said, the logistics of flying a large dog are more involved than flying a small one. A full-grown Golden typically weighs 25-34 kg and needs an IATA-compliant crate large enough to stand, turn around, and lie down without restriction. That usually means an IATA 500 or 700 crate, depending on the individual dog.\n\n"
            "The main variables are the destination country's import paperwork (microchip, rabies vaccine, health certificate, titre test for some countries), the airline's specific cargo booking process, and seasonal weather embargoes that affect large breeds.\n\n"
            "Plan at least three to four months ahead for destinations with strict import requirements like Australia, New Zealand, or Japan."
        ),
        "faqs": [
            {"question": "Can a Golden Retriever fly in the cabin?", "answer": "No. Golden Retrievers are too large to fly in the cabin on international routes. They travel as manifest cargo in the pressurised, temperature-controlled hold. The experience is not comparable to cabin travel, but airlines that specialize in pet cargo ensure the hold is kept at appropriate temperature and pressure throughout the flight."},
            {"question": "What crate size does a Golden Retriever need?", "answer": "Most adult Golden Retrievers require an IATA 500 or 700 crate. The dog should be able to stand up without its head touching the roof, turn around completely, and lie down in a natural position. Measure your specific dog before ordering a crate — size varies considerably across the breed."},
            {"question": "Which countries have the strictest import rules for Golden Retrievers?", "answer": "Australia and New Zealand require a rabies antibody titre test at least 180 days before entry, a mandatory quarantine period, and health certificates endorsed by the government authority in the country of origin. Japan requires a titre test and a minimum 180-day waiting period post-test. Most other countries require a microchip, a current rabies vaccination, and a vet-issued health certificate."},
            {"question": "How far in advance should I book cargo for a Golden Retriever?", "answer": "For routine routes (UK-USA, UK-EU), six to eight weeks is usually enough. For Australia, New Zealand, or Japan, you need three to six months minimum to complete titre testing and government paperwork. Start the process before you book flights."},
            {"question": "Do I need a pet transport agent for a Golden Retriever?", "answer": "Not always, but it helps. A reputable IPATA-member agent can manage the paperwork, book cargo space, and coordinate collection and delivery at both ends. For complex routes or strict-entry countries, the time saved is usually worth the cost."},
        ],
    },
    {
        "slug": "labrador-retriever",
        "title": "Flying with a Labrador Retriever | International Pet Cargo Guide",
        "description": "Airline and country rules for flying a Labrador Retriever internationally. Crate sizes, health paperwork, quarantine countries, and cargo booking tips.",
        "breed_name": "Labrador Retriever",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo with IATA-compliant crate", "notes": "Standard cargo booking. No breed-specific exclusions."},
            {"airline_name": "Qantas (seasonal)", "policy": "Accepted in cargo with conditions", "notes": "Embargoes apply in peak summer months. Confirm routing before booking."},
            {"airline_name": "Emirates (seasonal)", "policy": "Accepted in cargo with conditions", "notes": "Summer restrictions for large breeds on some routes."},
        ],
        "h1": "Labrador Retriever Air Travel Guide",
        "overview": (
            "Labradors are not restricted by any country's breed-specific legislation and face no blanket airline cargo bans. They are a practical breed to fly internationally, provided the logistics are handled properly.\n\n"
            "A medium to large Labrador typically needs an IATA 500 crate. Labs are robust dogs but they need the right crate size, water access during transit, and ideally a direct flight to limit the time they spend in the hold.\n\n"
            "Health paperwork is the main variable. Most countries need a microchip scan record, a current rabies vaccination, and a government-endorsed health certificate. Australia and New Zealand add a titre test and mandatory quarantine. Japan adds a titre test and a 180-day post-test waiting period.\n\n"
            "Start the paperwork process at least three months before your target travel date, longer for quarantine countries."
        ),
        "faqs": [
            {"question": "Is a Labrador allowed in the cabin on international flights?", "answer": "No. Labradors exceed the weight and size limits for cabin pets on virtually all international carriers. They travel in the aircraft hold as manifest cargo, in an IATA-approved crate."},
            {"question": "What crate size does a Labrador need?", "answer": "Most Labradors fit an IATA 500 crate. Larger or heavier Labs may need an IATA 700. The rule is the dog should stand without ducking, turn around fully, and lie flat. Measure before you order."},
            {"question": "Are there any breed bans affecting Labradors?", "answer": "No. Labradors are not subject to breed-specific legislation in any of the major destination countries. Import requirements are standard (microchip, rabies vaccine, health certificate). Some countries add titre tests or quarantine."},
            {"question": "What's the cost of flying a Labrador internationally?", "answer": "Airline cargo charges are typically calculated by volumetric weight (crate dimensions) rather than actual weight. A large Labrador in an IATA 500 crate commonly generates a volumetric weight of 60-80 kg. Costs vary by route and airline. Add government vet endorsement fees, health certificate fees, and any quarantine costs for strict-entry countries."},
            {"question": "Which airlines are best for flying a Labrador?", "answer": "Lufthansa, KLM, Air France, and Singapore Airlines have well-regarded cargo pet programmes. Qantas is the primary option for Australia but applies summer embargoes. British Airways Speedbird Cargo handles large dogs. Always book as early as possible — cargo space for large dogs can be limited."},
        ],
    },
    {
        "slug": "german-shepherd",
        "title": "Flying with a German Shepherd | Breed Restrictions & Cargo Rules",
        "description": "Country bans, airline cargo policies, and import rules for German Shepherds. Which routes are straightforward and which need extra planning.",
        "breed_name": "German Shepherd",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": ["Malaysia (Alsatian/German Shepherd and related types)"],
        "restricted_countries": ["Some US municipalities have BSL covering German Shepherds"],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed-specific restrictions on most carriers. Standard large-dog cargo rules apply."},
            {"airline_name": "Malaysia Airlines", "policy": "Restricted", "notes": "German Shepherds (Alsatians) are banned from import into Malaysia. Malaysian Airlines will not carry them to Malaysia."},
            {"airline_name": "Emirates (seasonal)", "policy": "Seasonal restrictions", "notes": "Large breed embargoes apply during summer months on certain routes."},
        ],
        "h1": "German Shepherd Air Travel Guide",
        "overview": (
            "German Shepherds are large, intelligent working dogs and they relocate internationally with their owners regularly. There are no global breed bans against German Shepherds, but one significant exception applies: Malaysia classifies the Alsatian (German Shepherd) as a restricted breed and prohibits import.\n\n"
            "For most destination countries, German Shepherd import follows standard large-dog procedures: IATA-compliant crate, microchip, rabies vaccination, government-endorsed health certificate, and a route-specific waiting period where required.\n\n"
            "Germany, despite being the breed's country of origin, imposes no domestic breed ban. The UK, Australia, USA, Canada, and EU countries all accept German Shepherds without breed-specific conditions.\n\n"
            "Plan for three to four months lead time on straightforward routes, six months-plus for Australia or New Zealand."
        ),
        "faqs": [
            {"question": "Is the German Shepherd banned anywhere?", "answer": "Malaysia prohibits the import of Alsatians (German Shepherds). No other major destination country applies a breed-specific ban to German Shepherds. Some local jurisdictions in the USA include German Shepherds in their breed-specific legislation, but this is rare and local in scope."},
            {"question": "What crate size does a German Shepherd need?", "answer": "Most German Shepherds require an IATA 500 or 700 crate depending on individual size. Males typically need larger crates than females. The dog must be able to stand, turn, and lie without restriction. Crate-train the dog weeks before travel."},
            {"question": "Can a German Shepherd fly to Australia?", "answer": "Yes. Australia imposes no breed ban on German Shepherds. You need a rabies antibody titre test (done at least 180 days before travel), government-endorsed health certificates, and the dog must complete mandatory quarantine at the Mickleham facility in Victoria. Total timeline from starting paperwork to arrival is typically six to eight months."},
            {"question": "Are there countries other than Malaysia that restrict German Shepherds?", "answer": "No other major destination country bans German Shepherds. However, always check current regulations for your destination before booking, as legislation can change."},
            {"question": "Do German Shepherds need a fitness-to-fly certificate?", "answer": "Not as a breed-specific requirement — that applies mainly to brachycephalic breeds. A standard health certificate from a licensed vet, issued within the timeframe required by your airline and destination country (commonly 10 days before travel), is what you need."},
        ],
    },
    {
        "slug": "siberian-husky",
        "title": "Flying with a Siberian Husky | Air Cargo & Import Guide",
        "description": "Airline cargo rules, import requirements, and seasonal heat restrictions for Siberian Huskies. What changes in summer and which routes need the most planning.",
        "breed_name": "Siberian Husky",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed ban. Subject to standard large-dog cargo rules and seasonal heat restrictions."},
            {"airline_name": "Multiple carriers (summer embargo)", "policy": "Seasonal restrictions", "notes": "Huskies are cold-weather dogs. Many airlines impose temperature restrictions on Husky cargo during peak summer. Travel in cooler months where possible."},
        ],
        "h1": "Siberian Husky Air Travel Guide",
        "overview": (
            "Siberian Huskies have no breed bans against them in any major destination country and no airline imposes a Husky-specific cargo policy. The practical concern is temperature: Huskies are cold-weather dogs with a thick double coat, and many airlines apply seasonal restrictions or require additional documentation during hot months to prevent heat stress.\n\n"
            "If you're flying a Husky in summer, particularly on routes through the Middle East or during North American heatwaves, expect complications. Some airlines refuse to carry double-coated Arctic breeds in cargo above a certain ambient temperature. This can mean rerouting or delaying travel to cooler months.\n\n"
            "Outside of temperature concerns, the process is standard: IATA-compliant crate (Huskies typically need a 500 or 700), microchip, rabies vaccination, government health certificate, and any destination-specific requirements (titre test for Australia/Japan, import permit for some countries)."
        ),
        "faqs": [
            {"question": "Can I fly a Siberian Husky in summer?", "answer": "It's possible but complicated. Huskies are poor heat tolerators and many airlines apply temperature-based embargoes that affect them in summer months. If you must travel in summer, look for airlines that use temperature-controlled cargo vehicles for ground transfer, book early morning or overnight flights when ambient temps are lower, and confirm with the airline in advance."},
            {"question": "What crate size does a Siberian Husky need?", "answer": "Most Siberian Huskies need an IATA 500 crate. Larger males may need a 700. The dog must stand without stooping, turn around, and lie flat in a natural position. Add ventilation spacers so the coat does not block airflow through the crate walls."},
            {"question": "Are there breed bans for Siberian Huskies?", "answer": "No. Siberian Huskies are not subject to breed-specific legislation in any major destination country. Import requirements follow the standard dog import process for your route."},
            {"question": "Do Huskies need special permits to enter Australia?", "answer": "No breed-specific permit is required. The standard Australian dog import process applies: rabies antibody titre test at least 180 days before departure, government-endorsed health certificates, mandatory quarantine at Mickleham in Victoria. Timeline is typically six to eight months from starting paperwork."},
            {"question": "What can go wrong when flying a Husky?", "answer": "The main risks are heat stress (especially in summer or on long connections through warm hub airports), crate rejection at check-in if the dog cannot stand/turn freely, and documentation errors that cause the dog to be held at the destination. Work with an experienced pet transport agent for any complex route."},
        ],
    },
    {
        "slug": "dobermann",
        "title": "Flying with a Dobermann | Country Bans & Cargo Rules",
        "description": "Which countries ban or restrict Dobermanns, which airlines accept them, and what paperwork you need for international relocation.",
        "breed_name": "Dobermann",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": ["Portugal (import of Dobermanns for non-residents restricted)", "Some Swiss cantons (restrictions apply)"],
        "restricted_countries": ["Several European countries (muzzle and lead requirements in public)", "Some US municipalities (BSL)"],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No airline-level breed ban. Destination country restrictions apply."},
        ],
        "h1": "Dobermann Air Travel Guide",
        "overview": (
            "The Dobermann is subject to breed-specific legislation in a small number of countries, though not as many as breeds like the Pit Bull Terrier or Rottweiler. There is no international blanket ban, but restrictions vary by country and even by region within countries.\n\n"
            "Portugal restricts the import of Dobermanns by non-residents. Several Swiss cantons regulate the breed. Some EU member states require muzzle and lead in public but do not ban import outright. The UK does not ban Dobermanns.\n\n"
            "Airlines do not impose Dobermann-specific bans. Standard large-dog cargo rules apply: IATA-compliant crate, current health paperwork, advance booking. The critical step is checking the destination country's current legislation before booking, since breed laws change.\n\n"
            "Always verify with the destination country's official government authority before travel."
        ),
        "faqs": [
            {"question": "Is the Dobermann banned in the UK?", "answer": "No. The UK's Dangerous Dogs Act 1991 lists four banned types: Pit Bull Terrier, Japanese Tosa, Dogo Argentino, and Fila Brasileiro. Dobermanns are not on that list. The XL Bully was added in 2024 but Dobermanns remain unrestricted."},
            {"question": "Can I take my Dobermann to Portugal?", "answer": "Portugal has restrictions on Dobermann import, particularly for non-residents. Regulations require that the dog is registered and the owner can demonstrate residency or meets specific conditions. Check with Portugal's DGAV (Direção-Geral de Alimentação e Veterinária) for the current rules before booking."},
            {"question": "Are Dobermanns banned in Australia?", "answer": "No federal ban exists in Australia. Some states have restrictions on Dobermanns as a \"declared dangerous breed\" requiring registration, enclosure standards, and muzzle/lead requirements in public. Import itself is not banned — standard Australian import process applies (titre test, health certificates, quarantine)."},
            {"question": "What crate size does a Dobermann need?", "answer": "Most Dobermanns require an IATA 500 or 700 crate. Dobermanns are a tall, deep-chested breed — measure the standing height carefully and add 10 cm to determine minimum crate height."},
            {"question": "What documentation does a Dobermann need for international travel?", "answer": "The standard package: ISO-compliant microchip, current rabies vaccination, government-endorsed health certificate, and any destination-specific requirements (titre test, import permit, quarantine). Plus any breed-specific documentation required by the destination country's legislation."},
        ],
    },
    {
        "slug": "alaskan-malamute",
        "title": "Flying with an Alaskan Malamute | Cargo & Heat Restrictions",
        "description": "Large breed cargo logistics, seasonal heat embargoes, and import rules for Alaskan Malamutes. Which airlines and routes work best.",
        "breed_name": "Alaskan Malamute",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Multiple carriers", "policy": "Accepted in cargo with seasonal restrictions", "notes": "Arctic breeds face temperature restrictions in summer. Confirm current policy with the airline before booking."},
            {"airline_name": "Some carriers (oversized cargo)", "policy": "May require specialist cargo booking", "notes": "Large Malamutes in 700-series crates may need specialist cargo rather than standard pet cargo booking."},
        ],
        "h1": "Alaskan Malamute Air Travel Guide",
        "overview": (
            "Alaskan Malamutes are large, heavy-coated Arctic dogs. No breed bans apply anywhere, but the combination of size and cold-weather coat creates real practical challenges for air travel.\n\n"
            "A full-grown Malamute can reach 38 kg or more and typically needs an IATA 700 crate. This takes them into specialist large-dog cargo territory on many airlines, where space is limited and advance booking is essential.\n\n"
            "Temperature is the other constraint. Most airlines have ambient temperature restrictions for live animals in cargo — if it's too hot at either end of the route, the flight can be refused. For a thick-coated Arctic breed, that threshold arrives sooner than it does for short-coated dogs. Summer travel through warm hub airports carries real risk.\n\n"
            "Book early, choose routes that avoid extreme temperatures, and confirm the airline's current large-dog and temperature policies well before travel."
        ),
        "faqs": [
            {"question": "What is the minimum crate size for an Alaskan Malamute?", "answer": "Most adult Malamutes need an IATA 700 crate. Some very large males may need a custom build. The dog must stand without stooping, turn fully, and lie flat. Measure your specific dog — there is wide variation within the breed."},
            {"question": "Are Alaskan Malamutes affected by summer flight restrictions?", "answer": "Yes. Many airlines will not accept thick-coated or Arctic breeds in cargo when ground temperatures exceed a set threshold (commonly 29°C at origin or destination). In practice this can ground your Malamute for several months in summer. Plan travel for spring, autumn, or winter where possible."},
            {"question": "Is an Alaskan Malamute banned anywhere?", "answer": "No. Alaskan Malamutes are not subject to breed-specific legislation in any major destination country. Standard dog import rules apply."},
            {"question": "Can an Alaskan Malamute fly to Australia?", "answer": "Yes, though the process is lengthy. Australia requires a rabies antibody titre test at least 180 days before entry, government-endorsed health certificates, and mandatory quarantine at Mickleham in Victoria. Factor in six to eight months minimum for paperwork. Qantas and Singapore Airlines are the main cargo options for Australia routes."},
            {"question": "How much does it cost to fly an Alaskan Malamute internationally?", "answer": "An IATA 700 crate generates a large volumetric weight, so cargo charges are significant. For a transatlantic or long-haul route, costs including airline cargo, government fees, vet health certificate, and quarantine (if applicable) can reach £2,000–£5,000+. Get quotes from multiple carriers and compare via a pet transport agent."},
        ],
    },
    {
        "slug": "great-dane",
        "title": "Flying with a Great Dane | Giant Breed Air Cargo Guide",
        "description": "How to fly a Great Dane internationally. Giant-breed crate requirements, airline cargo booking, and which routes are feasible for the world's largest dog breed.",
        "breed_name": "Great Dane",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Many commercial airlines", "policy": "May refuse or be unable to accommodate giant breeds", "notes": "Great Danes in IATA 700 or custom crates exceed the standard pet cargo dimensions on many aircraft. Confirm specific aircraft type on your route."},
            {"airline_name": "Specialist pet cargo carriers", "policy": "Usually accommodated with advance booking", "notes": "Charter or specialist freight solutions may be needed for very large dogs."},
        ],
        "h1": "Great Dane Air Travel Guide",
        "overview": (
            "Great Danes are the world's largest dog breed by height and travelling internationally with one is genuinely complex — not because of breed bans, but because of pure size.\n\n"
            "A fully grown Great Dane may need a custom crate larger than the standard IATA 700 series, and not all aircraft have cargo holds that can accommodate this. Airlines operate a range of aircraft, and the belly cargo space varies by aircraft type. Even if the airline in principle accepts large dogs, the specific flight on your route may not be able to carry them physically.\n\n"
            "No country bans Great Danes. The challenges are entirely logistical: finding airlines and aircraft that can physically take the crate, managing the cost (volumetric weight on a giant crate is enormous), and keeping a very large dog comfortable during transit.\n\n"
            "A specialist pet transport agent is essentially mandatory for Great Dane international relocations. This is not a DIY job."
        ),
        "faqs": [
            {"question": "Can any airline fly a Great Dane internationally?", "answer": "In principle, yes. In practice, the crate size for a Great Dane often exceeds what standard commercial pet cargo programmes handle. Some airlines with larger freighter options or dedicated cargo divisions can accommodate giant breeds, but you must confirm the specific aircraft type for your route. This almost always requires booking through a specialist pet transport agent."},
            {"question": "Is a Great Dane banned anywhere?", "answer": "No. Great Danes are not subject to breed-specific legislation in any major destination country."},
            {"question": "What crate does a Great Dane need?", "answer": "Standard IATA 700 crates are 99 x 67 x 74 cm. A Great Dane typically needs a custom-built crate, often 120 x 90 x 100 cm or larger. The dog must stand fully without ducking, turn around, and lie flat. Custom IATA-spec crates can be built by specialist suppliers."},
            {"question": "How much does it cost to fly a Great Dane internationally?", "answer": "Due to the crate size and volumetric weight, the cost is very high. A transatlantic Great Dane relocation including airline cargo, crate, health certificates, and agent fees can easily exceed £5,000–£10,000. Get specialist quotes well in advance."},
            {"question": "What are the alternatives to air cargo for a Great Dane?", "answer": "If the route permits, ground transport and sea freight are options for shorter moves (e.g., within Europe or UK to Europe). For intercontinental moves, air freight in a specialist large-dog crate is the only practical option. A pet transport agent can advise on what is feasible for your specific route."},
        ],
    },
    {
        "slug": "border-collie",
        "title": "Flying with a Border Collie | International Travel Guide",
        "description": "Airline and import rules for Border Collies. Medium-breed cargo logistics, health paperwork, and which routes need the most preparation.",
        "breed_name": "Border Collie",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed restrictions. Standard medium-to-large dog cargo process applies."},
        ],
        "h1": "Border Collie Air Travel Guide",
        "overview": (
            "Border Collies are medium-sized, highly intelligent working dogs with no breed bans in any destination country. They are one of the more straightforward breeds to fly internationally, provided the health paperwork is in order.\n\n"
            "Most Border Collies fit an IATA 400 or 500 crate, depending on individual size. They are not brachycephalic, not classified as aggressive breeds, and attract no special airline restrictions beyond standard large-dog cargo rules.\n\n"
            "The main variable is the destination country's import requirements. Standard routes (UK to EU, UK to USA, USA to Canada) involve microchip registration, a current rabies vaccination, and a government-endorsed health certificate. Australia, New Zealand, and Japan add a titre test and waiting period.\n\n"
            "Border Collies are working dogs and tend to handle crate environments better than many breeds if they have been crate-trained beforehand."
        ),
        "faqs": [
            {"question": "Is a Border Collie allowed in the cabin?", "answer": "On most international routes, no. Border Collies typically exceed the under-seat carrier size and weight limits for cabin pets. They travel in the aircraft hold as manifest cargo."},
            {"question": "What crate size does a Border Collie need?", "answer": "Depends on the individual dog. Lighter Border Collies (under 18 kg) may fit an IATA 400. Larger or longer dogs may need a 500. The dog must stand fully, turn around, and lie down without restriction."},
            {"question": "Can a Border Collie travel to Australia?", "answer": "Yes. Border Collies are not subject to any breed-specific conditions for Australian import. The standard process applies: rabies titre test at least 180 days before travel, health certificates, and mandatory quarantine at Mickleham, Victoria."},
            {"question": "Are Border Collies banned anywhere?", "answer": "No. Border Collies are not targeted by breed-specific legislation anywhere."},
            {"question": "How do I prepare a Border Collie for cargo travel?", "answer": "Crate train the dog weeks before the flight so the crate feels like a safe space rather than a cage. Exercise the dog well before the journey. Do not sedate unless a veterinarian has assessed the dog and specifically recommended it — sedation is generally discouraged for cargo travel as it can affect breathing and balance."},
        ],
    },
    {
        "slug": "beagle",
        "title": "Flying with a Beagle | Cabin & Cargo Rules for International Travel",
        "description": "Small-to-medium breed international travel guide for Beagles. Which routes allow cabin travel, cargo options, and the health paperwork you need.",
        "breed_name": "Beagle",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Some airlines (cabin — small Beagles only)", "policy": "Cabin accepted if under weight limit", "notes": "Smaller Beagles under 8 kg including carrier may qualify for in-cabin travel on some carriers. Weight limits vary by airline."},
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "Standard medium-dog cargo rules. IATA 400 crate typically needed."},
        ],
        "h1": "Beagle Air Travel Guide",
        "overview": (
            "Beagles are sociable, robust little dogs and one of the more practical breeds to fly internationally. No country imposes breed-specific restrictions on Beagles. They attract no special airline policies beyond standard dog rules.\n\n"
            "Smaller Beagles (miniature variety or slim adults under 8 kg including the carrier) may qualify for in-cabin travel on airlines that allow small dogs in the cabin. Most standard-sized adult Beagles weigh 10-11 kg and travel as cargo.\n\n"
            "In cargo, a Beagle typically needs an IATA 400 crate. The health paperwork process is straightforward for most routes: microchip, rabies vaccination, and a government-endorsed health certificate. Australia, New Zealand, and Japan add a titre test."
        ),
        "faqs": [
            {"question": "Can a Beagle fly in the cabin?", "answer": "Possibly, depending on the dog's weight and the airline. In-cabin pet policies typically allow dogs under 8 kg including the carrier. A miniature Beagle or slim puppy might qualify, but most adult Beagles are too heavy. Check the specific airline policy before booking."},
            {"question": "What crate size does a Beagle need for cargo?", "answer": "Most adult Beagles fit an IATA 400 crate comfortably. The dog must be able to stand, turn, and lie without restriction."},
            {"question": "Are there any countries that ban Beagles?", "answer": "No. Beagles are not subject to breed-specific legislation anywhere."},
            {"question": "What documents does a Beagle need for international travel?", "answer": "Microchip (ISO 15-digit), current rabies vaccination, and a government-endorsed health certificate from a licensed vet. For Australia, New Zealand, and Japan, add a rabies antibody titre test at least 180 days before travel. For EU travel from the UK, an AHC (Animal Health Certificate) replaces the EU pet passport post-Brexit."},
            {"question": "Can a Beagle travel to the USA?", "answer": "Yes. The CDC dog import rules (effective 2024) require that all dogs arriving in the USA be microchipped and have documentation of US rabies vaccination or have an approved serological test. Dogs arriving from countries classified as high risk for dog rabies face additional requirements including CDC DogBot approval prior to travel."},
        ],
    },
    {
        "slug": "cocker-spaniel",
        "title": "Flying with a Cocker Spaniel | International Pet Transport Guide",
        "description": "What Cocker Spaniel owners need to know about airline cargo rules, cabin eligibility, and import paperwork for international moves.",
        "breed_name": "Cocker Spaniel",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Some airlines (cabin — small individuals only)", "policy": "Cabin accepted if under weight limit", "notes": "Cocker Spaniels close to 8 kg including carrier may qualify for cabin on some routes. Confirm individual airline policy."},
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed restrictions. IATA 400 or 500 crate depending on size."},
        ],
        "h1": "Cocker Spaniel Air Travel Guide",
        "overview": (
            "Cocker Spaniels — both English and American varieties — are friendly, adaptable dogs with no breed bans anywhere and no airline-specific restrictions. They are a reasonably straightforward breed to fly internationally.\n\n"
            "Adult Cocker Spaniels typically weigh 10-14 kg and travel as cargo in an IATA 400 crate. Smaller dogs may qualify for cabin travel on airlines that permit pets in the cabin, but this depends on individual weight and the airline's under-seat dimensions.\n\n"
            "Cocker Spaniels have a long, floppy ear that can be prone to infection — worth a vet check before any long flight. Otherwise, the process is standard: microchip, rabies vaccine, health certificate, and destination-specific additions."
        ),
        "faqs": [
            {"question": "Can a Cocker Spaniel fly in the cabin internationally?", "answer": "Possibly. Under-seat pet allowances on most international carriers are around 8 kg including the carrier. A lean adult Cocker Spaniel might qualify, but many won't. Check the specific airline's current in-cabin pet policy before booking."},
            {"question": "What crate size does a Cocker Spaniel need?", "answer": "Most Cocker Spaniels need an IATA 400 crate. Measure your dog: height standing plus 10 cm = minimum crate height."},
            {"question": "Are Cocker Spaniels subject to any breed bans?", "answer": "No. Neither English nor American Cocker Spaniels appear on breed restriction lists anywhere."},
            {"question": "What health checks does a Cocker Spaniel need before a long-haul flight?", "answer": "A standard health certificate from a licensed vet issued within the timeframe required by your airline and destination (typically 10 days). The vet will assess general health, eye and ear health, and confirm the dog is fit to travel. For brachycephalic or health-prone breeds, additional assessment may be advised, but Cocker Spaniels do not fall into that category."},
            {"question": "How do Cocker Spaniels handle cargo travel?", "answer": "Generally well. Cocker Spaniels are adaptable dogs. Crate training before the flight significantly reduces stress. Keep the familiar smell of home in the crate (an unwashed blanket or t-shirt). Avoid long connections where possible."},
        ],
    },
    {
        "slug": "maltese",
        "title": "Flying with a Maltese | Cabin Pet Rules & International Guides",
        "description": "Maltese owners' guide to international air travel. Which airlines allow Maltese in the cabin, weight limits, and the paperwork required for each region.",
        "breed_name": "Maltese",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines allowing in-cabin pets", "policy": "Accepted in cabin if under weight limit", "notes": "Maltese typically weigh 2-4 kg — well within the 8 kg limit most airlines apply. Check individual airline policy."},
            {"airline_name": "British Airways", "policy": "No in-cabin pets (except assistance dogs)", "notes": "All pet dogs travel as cargo. No exceptions for small breeds."},
            {"airline_name": "Ryanair / easyJet", "policy": "No pets in cabin", "notes": "Low-cost carriers do not accept pets in cabin on international routes."},
        ],
        "h1": "Maltese Air Travel Guide",
        "overview": (
            "The Maltese is one of the most travel-friendly breeds for international moves. At 2-4 kg, a healthy adult Maltese fits comfortably under the seat in most cabin pet programmes — no cargo, no hold time, no quarantine complications for most destinations.\n\n"
            "No country bans Maltese. No airline specifically restricts them. The constraints are the individual airline's in-cabin pet policy (weight, carrier dimensions, route restrictions) and the destination country's import rules.\n\n"
            "Not all airlines accept in-cabin pets. British Airways, for example, does not allow cabin pets (other than assistance dogs). Low-cost carriers in Europe also typically do not. So the Maltese's size advantage depends entirely on which airline you fly with.\n\n"
            "Health paperwork is the same as for any dog: microchip, rabies vaccination, health certificate. For travel to Australia, New Zealand, or Japan, a titre test and waiting period still apply regardless of how small the dog is."
        ),
        "faqs": [
            {"question": "Can a Maltese fly in the cabin internationally?", "answer": "On most airlines that allow in-cabin pets, yes. A Maltese typically weighs 2-4 kg, well within the 8 kg in-carrier limit that most carriers apply. The carrier itself must fit under the seat in front of you. Check the specific airline's cabin pet policy — not all airlines accept pets in the cabin."},
            {"question": "Which airlines accept Maltese in the cabin?", "answer": "Airlines that commonly accept small dogs in-cabin on international routes include Lufthansa, KLM, Air France, Emirates (on some routes), Singapore Airlines (on some routes), and several others. British Airways does not allow cabin pets. Always verify the current policy with the airline before booking."},
            {"question": "Does a Maltese still need a titre test for Australia?", "answer": "Yes. Australia requires a rabies antibody titre test for all dogs regardless of size. The 180-day post-test waiting period applies to a 3 kg Maltese exactly as it does to a 35 kg Labrador."},
            {"question": "What carrier does a Maltese need?", "answer": "An IATA-approved soft-sided carrier that fits under the seat in front of you. Most airlines specify maximum carrier dimensions (commonly around 55 x 35 x 25 cm). The dog must be able to stand, turn, and lie down inside it."},
            {"question": "What paperwork does a Maltese need for EU travel from the UK?", "answer": "Post-Brexit, dogs travelling from the UK to the EU need an Animal Health Certificate (AHC) issued by an Official Veterinarian (OV) within 10 days of travel. The AHC replaces the EU pet passport for UK-to-EU journeys. Microchip must be scanned first before any vaccination record is created."},
        ],
    },
    {
        "slug": "chihuahua",
        "title": "Flying with a Chihuahua | Cabin Pets & International Travel Rules",
        "description": "The complete guide for flying a Chihuahua internationally. Cabin pet rules, in-carrier requirements, and country-by-country paperwork guide.",
        "breed_name": "Chihuahua",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Accepted in cabin — typically qualifies by weight", "notes": "Chihuahuas typically weigh 1.5-3 kg, well within in-cabin weight limits."},
            {"airline_name": "British Airways", "policy": "No in-cabin pets", "notes": "Chihuahuas must travel as cargo on BA, regardless of size."},
        ],
        "h1": "Chihuahua Air Travel Guide",
        "overview": (
            "Chihuahuas are the smallest recognised dog breed and one of the most practical to fly internationally — on the right airline. At 1.5 to 3 kg, they qualify for in-cabin travel on virtually every airline that allows cabin pets, removing the need for cargo entirely.\n\n"
            "No country bans Chihuahuas. No airline singles them out for restrictions. The only complications come from airlines that do not allow any cabin pets (British Airways is the main UK example) and destination countries with strict import requirements.\n\n"
            "Australia and New Zealand require a titre test and quarantine regardless of dog size. Japan requires a titre test and 180-day waiting period. For most other destinations, the process is a microchip check, a current rabies vaccination, and a health certificate."
        ),
        "faqs": [
            {"question": "Can a Chihuahua fly in the cabin on international flights?", "answer": "On airlines that accept cabin pets, yes. Chihuahuas easily meet in-cabin weight limits (typically under 8 kg including the carrier). However, not all airlines allow cabin pets — British Airways does not. Check before booking."},
            {"question": "Does a Chihuahua need a titre test for Australia?", "answer": "Yes. Australia's 180-day titre test requirement applies to all dogs. A Chihuahua is subject to exactly the same import process as a Labrador."},
            {"question": "What carrier does a Chihuahua need for cabin travel?", "answer": "A soft-sided IATA-approved carrier that fits under the seat in front. Airlines specify exact dimensions — check before purchasing. The dog must be able to stand, turn, and lie down inside. Most Chihuahuas are comfortable in small IATA-approved cabin carriers."},
            {"question": "Can a Chihuahua travel to the USA?", "answer": "Yes. Under CDC rules effective 2024, all dogs entering the USA must be microchipped. Additional requirements depend on the country of origin and rabies vaccination history. A Chihuahua from a low-risk country with a valid US-accepted rabies vaccination and AHC typically clears customs without additional tests."},
            {"question": "Are Chihuahuas allowed in hotels and rentals at the destination?", "answer": "That's outside the scope of air transport — check accommodation pet policies separately. The dog's import requirements at the destination are what the airline and border services care about."},
        ],
    },
    {
        "slug": "yorkshire-terrier",
        "title": "Flying with a Yorkshire Terrier | Cabin & Cargo International Guide",
        "description": "Yorkshire Terrier international travel: cabin pet rules, health certificates, and destination requirements. Why Yorkies are among the easiest breeds to fly.",
        "breed_name": "Yorkshire Terrier",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Accepted in cabin — qualifies by weight", "notes": "Yorkshire Terriers typically weigh 2-3 kg, well within in-cabin limits."},
            {"airline_name": "British Airways", "policy": "No in-cabin pets", "notes": "Must travel as cargo on BA."},
        ],
        "h1": "Yorkshire Terrier Air Travel Guide",
        "overview": (
            "Yorkshire Terriers — Yorkies — are small, adaptable dogs that qualify for in-cabin travel on most airlines that accept cabin pets. At 2-3 kg, they sit comfortably under the 8 kg combined dog-plus-carrier limit that most carriers apply.\n\n"
            "No country bans Yorkshire Terriers. No airline targets them with restrictions. The process is simpler than for large breeds: no cargo logistics, no giant crate, no oversized-animal surcharges on airlines that allow in-cabin pets.\n\n"
            "The health paperwork is identical to all other dogs: microchip, rabies vaccination, government-endorsed health certificate. Australia and New Zealand still require a titre test and quarantine. Japan requires a titre test and 180-day wait. Those requirements are non-negotiable regardless of dog size."
        ),
        "faqs": [
            {"question": "Can a Yorkie fly in the cabin?", "answer": "On airlines that allow cabin pets, yes. A standard Yorkshire Terrier at 2-3 kg is well within in-cabin limits. The carrier must fit under the seat in front. British Airways does not allow cabin pets (except assistance dogs), so on BA, a Yorkie travels as cargo."},
            {"question": "What are the in-cabin rules for a Yorkie?", "answer": "The dog must remain in its carrier for the entire flight, under the seat. The carrier must meet the airline's dimension guidelines. The dog must not be in distress. Most airlines charge a cabin pet fee ranging from £30 to £200 per flight."},
            {"question": "Does a Yorkie need a titre test for New Zealand?", "answer": "Yes. New Zealand requires a rabies antibody titre test for all dogs, with a minimum 180-day wait between the confirmed titre result and entry. Mandatory quarantine at the Levin MPI facility also applies. These rules are the same for all dogs regardless of size or breed."},
            {"question": "What carrier is best for a Yorkie?", "answer": "A soft-sided IATA-approved cabin carrier with adequate ventilation, a non-slip mat inside, and dimensions that fit under the seat (check each airline's specific measurements). Familiarise the dog with the carrier weeks before travel."},
            {"question": "Can a Yorkie fly as excess baggage?", "answer": "In the cabin, a small dog in a carrier typically travels as a cabin fee rather than excess baggage. As cargo, they travel under the airline's live animal cargo programme. Excess baggage as a classification is rarely used for live animals on international routes."},
        ],
    },
    {
        "slug": "dachshund",
        "title": "Flying with a Dachshund | Travel Rules & Spinal Health Considerations",
        "description": "International travel guide for Dachshunds. Cabin eligibility, cargo crate sizing, vet clearance for spinal conditions, and destination paperwork.",
        "breed_name": "Dachshund",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Small/miniature Dachshunds may qualify for cabin", "notes": "Standard Dachshunds typically weigh 7-15 kg. Miniature variety at 3-5 kg may meet in-cabin limits on some carriers."},
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed restrictions. IATA 300-400 crate for miniatures, 400-500 for standards."},
        ],
        "h1": "Dachshund Air Travel Guide",
        "overview": (
            "Dachshunds come in two sizes — standard (7-15 kg) and miniature (3-5 kg) — and the rules differ somewhat between them. Miniature Dachshunds are small enough for in-cabin travel on airlines that accept cabin pets. Standard Dachshunds travel in cargo.\n\n"
            "Neither variety is banned anywhere. Neither faces any airline-level breed restriction.\n\n"
            "There is one health consideration specific to the breed: Dachshunds are prone to intervertebral disc disease (IVDD) due to their long spine and short legs. Before any flight, have a vet specifically assess spinal health and confirm the dog is fit to travel. This is not a standard part of the health certificate process, but it is worth the extra consultation.\n\n"
            "Avoid placing the crate in a position that allows the dog to impact the front wall in turbulence — position bedding to support the spine."
        ),
        "faqs": [
            {"question": "Can a Dachshund fly in the cabin?", "answer": "A miniature Dachshund at 3-5 kg often qualifies for in-cabin travel on airlines that accept cabin pets. A standard Dachshund at 7-15 kg typically does not. Check the specific airline's weight limit."},
            {"question": "Is the long spine of a Dachshund a concern for air travel?", "answer": "It can be. Dachshunds are prone to IVDD (intervertebral disc disease). The vibration and pressure changes of air travel are unlikely to cause problems for a healthy Dachshund, but a vet assessment before any flight is sensible. Ask your vet to specifically assess spinal health if you know your dog has had disc issues."},
            {"question": "What crate size does a Dachshund need?", "answer": "Miniatures: IATA 300 often works. Standards: IATA 400. The dog must stand fully (which for Dachshunds is not much height), turn around, and lie down. They are long dogs — check the crate length as well as height."},
            {"question": "Are Dachshunds banned anywhere?", "answer": "No. Dachshunds are not subject to any breed-specific legislation."},
            {"question": "What documents does a Dachshund need to enter Australia?", "answer": "Same as all dogs: ISO microchip, rabies antibody titre test done at least 180 days before travel, government-endorsed health certificate from an approved vet, treatment records. Mandatory quarantine at Mickleham, Victoria. No breed-specific additions for Dachshunds."},
        ],
    },
    {
        "slug": "miniature-schnauzer",
        "title": "Flying with a Miniature Schnauzer | International Pet Transport",
        "description": "Cabin and cargo options for Miniature Schnauzers, health paperwork for international travel, and a guide to destination requirements.",
        "breed_name": "Miniature Schnauzer",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Usually qualifies for cabin by weight", "notes": "Miniature Schnauzers weigh 5-9 kg. Smaller individuals under 8 kg including carrier may qualify for in-cabin."},
            {"airline_name": "Most major airlines (cargo)", "policy": "Accepted in cargo", "notes": "IATA 300-400 crate. No breed restrictions."},
        ],
        "h1": "Miniature Schnauzer Air Travel Guide",
        "overview": (
            "Miniature Schnauzers are smart, adaptable dogs that handle travel well. They have no breed bans and face no airline-specific restrictions. Their weight (typically 5-9 kg) puts them on the boundary of cabin eligibility: smaller individuals in a light carrier might qualify, while larger ones will travel as cargo.\n\n"
            "Standard health paperwork applies: microchip, rabies vaccination, government-endorsed health certificate. Australia and Japan add titre tests. EU-UK travel from UK requires an AHC post-Brexit.\n\n"
            "Schnauzers are alert and can be reactive in unfamiliar environments. Crate training well in advance of travel is especially worthwhile for this breed."
        ),
        "faqs": [
            {"question": "Can a Miniature Schnauzer fly in the cabin?", "answer": "Possibly. The combined weight of dog plus carrier must typically be under 8 kg. A lean Miniature Schnauzer at 5-6 kg in a 1.5 kg carrier is right at the limit. Weigh both before booking."},
            {"question": "What crate does a Miniature Schnauzer need for cargo?", "answer": "An IATA 300 or 400, depending on the dog's size. The dog must stand fully, turn, and lie down without restriction."},
            {"question": "Are Miniature Schnauzers banned anywhere?", "answer": "No. They are not subject to breed-specific legislation anywhere."},
            {"question": "What's the best way to prepare a Schnauzer for cargo travel?", "answer": "Crate train for several weeks before the flight. Use the crate as a sleeping space at home. Avoid feeding within four hours of the flight to reduce nausea risk. Leave an unwashed item of clothing in the crate for scent comfort."},
            {"question": "Do Miniature Schnauzers need special documentation to enter Japan?", "answer": "No breed-specific documentation. Japan requires all dogs to have an ISO microchip, a current rabies vaccination, and a rabies antibody titre test confirmed at an MAFF-approved laboratory. A minimum 180-day waiting period must pass between the titre result and entry. Contact MAFF (Japan's Ministry of Agriculture, Forestry and Fisheries) for current forms."},
        ],
    },
    {
        "slug": "standard-poodle",
        "title": "Flying with a Standard Poodle | Large Breed Cargo Guide",
        "description": "Cargo logistics, crate sizing, and import requirements for Standard Poodles. No breed bans, but large-dog cargo rules apply.",
        "breed_name": "Standard Poodle",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed restrictions. Standard large-dog cargo rules. IATA 500 crate typically needed."},
        ],
        "h1": "Standard Poodle Air Travel Guide",
        "overview": (
            "Standard Poodles are large, elegant dogs with no breed restrictions anywhere. They travel internationally as cargo on most major airlines without complications — provided the crate and paperwork are in order.\n\n"
            "A full-grown Standard Poodle typically weighs 20-32 kg and needs an IATA 500 crate. They are athletic, intelligent dogs that generally adapt well to new situations, which is a practical advantage in transit.\n\n"
            "No destination country imposes breed-specific conditions on Standard Poodles. The usual rules apply: microchip, rabies vaccination, government-endorsed health certificate, and destination-specific additions for Australia/NZ/Japan."
        ),
        "faqs": [
            {"question": "Can a Standard Poodle fly in the cabin?", "answer": "No. Standard Poodles are too large for in-cabin travel on international routes. Toy and Miniature Poodles may qualify depending on individual weight."},
            {"question": "Are Standard Poodles subject to breed bans?", "answer": "No. Standard Poodles are not subject to any breed-specific legislation anywhere."},
            {"question": "What crate size does a Standard Poodle need?", "answer": "Most Standard Poodles need an IATA 500 crate. Taller dogs may need a 700. Measure standing height and add 10 cm for minimum crate height."},
            {"question": "How far ahead should I book cargo for a Standard Poodle?", "answer": "Six to eight weeks for most routes. Three to six months for Australia, New Zealand, or Japan due to titre test waiting periods."},
            {"question": "Do Poodles need a health certificate for UK-EU travel?", "answer": "Yes. Post-Brexit, all dogs moving from the UK to the EU need an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel."},
        ],
    },
    {
        "slug": "shiba-inu",
        "title": "Flying with a Shiba Inu | Japan Import Rules & Air Travel Guide",
        "description": "Shiba Inu international travel: Japan's import rules for Japanese-born dogs, quarantine requirements, and airline cargo guide.",
        "breed_name": "Shiba Inu",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Japan Airlines (to Japan)", "policy": "Accepted in cargo", "notes": "Standard IATA cargo. Japan's strict 180-day post-titre waiting period means most dogs need several months of preparation before entry."},
            {"airline_name": "ANA (to Japan)", "policy": "Accepted in cargo", "notes": "Same entry requirements as JAL. Dog must arrive via approved port of entry."},
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No breed restrictions. Standard medium-dog cargo process."},
        ],
        "h1": "Shiba Inu Air Travel Guide",
        "overview": (
            "Shiba Inus are a Japanese breed, but that doesn't make returning to Japan any simpler. Japan has some of the strictest pet import regulations in the world, and they apply to all dogs regardless of breed origin.\n\n"
            "For most other destinations, Shiba Inus travel without complications. They are a medium-sized breed (7-11 kg), typically need an IATA 400 crate, and face no breed-specific restrictions anywhere.\n\n"
            "The notable exception is Japan itself. Dogs entering Japan require a rabies antibody titre test performed at an MAFF-approved laboratory, a minimum 180-day wait after the confirmed titre result, at least two valid rabies vaccinations, and inspection on arrival. Dogs that haven't completed the preparation are placed in quarantine at the owner's expense.\n\n"
            "If you're moving a Shiba Inu to Japan, start the process at least nine months before your travel date."
        ),
        "faqs": [
            {"question": "How long does it take to import a dog into Japan?", "answer": "The minimum timeline from starting preparation is 180 days after the titre test is confirmed by an MAFF-approved laboratory. Add time for the titre test itself, the two required vaccinations (if not already done), and the government health certificate process. Realistically, allow nine to twelve months from first vet appointment to Japan arrival."},
            {"question": "Can a Shiba Inu fly in the cabin?", "answer": "On most international routes, no. Adult Shiba Inus typically weigh 7-11 kg, over the in-cabin weight limit of most carriers. They travel as cargo."},
            {"question": "Are Shiba Inus allowed in all countries?", "answer": "Yes. There are no breed bans on Shiba Inus anywhere. Standard dog import rules apply."},
            {"question": "What MAFF-approved laboratory do I use for the Japan titre test?", "answer": "Japan's MAFF (Ministry of Agriculture, Forestry and Fisheries) maintains a list of approved laboratories for the FAVN (Fluorescent Antibody Virus Neutralisation) test. In the UK, the Animal and Plant Health Agency (APHA) laboratory is MAFF-approved. In the USA, Kansas State University Rabies Laboratory is approved. Always confirm the current approved lab list directly with MAFF before submitting samples."},
            {"question": "Do Japanese Shiba Inus imported from Japan have simpler paperwork?", "answer": "No. A dog born in Japan and exported must go through the same re-import process as any other dog. Japan treats re-entry the same as first-time entry."},
        ],
    },
    {
        "slug": "samoyed",
        "title": "Flying with a Samoyed | Arctic Breed Cargo & Temperature Guide",
        "description": "Airline and import rules for Samoyeds. Summer heat restrictions, large crate logistics, and international relocation guide for this thick-coated breed.",
        "breed_name": "Samoyed",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Multiple carriers (summer)", "policy": "Seasonal restrictions for thick-coated breeds", "notes": "Temperature-based embargoes affect Samoyeds during peak summer on many routes. Travel in cooler months."},
        ],
        "h1": "Samoyed Air Travel Guide",
        "overview": (
            "Samoyeds are beautiful, thick-coated Arctic dogs with no breed bans and no airline cargo restrictions beyond those that apply to all double-coated breeds in summer.\n\n"
            "The practical concern is heat. Samoyeds carry a very thick double coat and can overheat in warm conditions. Many airlines apply ambient temperature restrictions for live animal cargo: if it's too hot at either end of the route, the flight is refused. For Samoyeds specifically, some carriers apply stricter temperature thresholds than for short-coated breeds.\n\n"
            "An adult Samoyed typically weighs 16-30 kg and needs an IATA 500 crate. They are calm, friendly dogs that generally handle confinement well — a genuine advantage in cargo transit.\n\n"
            "Choose travel dates in cooler months and avoid hub airports known for extreme summer heat. Confirm the airline's current temperature policy well in advance."
        ),
        "faqs": [
            {"question": "Can a Samoyed fly in summer?", "answer": "Potentially, but with complications. Most airlines apply temperature-based live animal embargoes — if ground temperatures at origin or destination exceed a set threshold (typically 27-29°C), the cargo booking is refused. For a thick-coated Samoyed, some airlines apply more conservative limits. Book for early morning or evening flights in cooler months if possible."},
            {"question": "Are Samoyeds banned anywhere?", "answer": "No. Samoyeds are not subject to breed-specific legislation anywhere."},
            {"question": "What crate size does a Samoyed need?", "answer": "Depending on individual size, an IATA 500 or 700 crate. A large male may approach the limit of a 500. Measure the dog standing fully and add 10 cm for height."},
            {"question": "How do I keep a Samoyed cool during cargo transit?", "answer": "Use a well-ventilated IATA-compliant crate with spacer feet to allow airflow underneath. Freeze a water dish before the flight so ice melts slowly during transit. Do not clip the coat — the double coat actually insulates against heat as well as cold. Avoid flights with long connections in warm locations."},
            {"question": "Do Samoyeds need any breed-specific documentation?", "answer": "No. Standard dog import paperwork applies: microchip, rabies vaccination, health certificate, and destination-specific additions (titre test for Australia/NZ/Japan)."},
        ],
    },
    {
        "slug": "belgian-malinois",
        "title": "Flying with a Belgian Malinois | Country Restrictions & Cargo Guide",
        "description": "Which countries restrict Belgian Malinois import, airline cargo rules, and what working-dog owners need to know before international relocation.",
        "breed_name": "Belgian Malinois",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": ["Some jurisdictions classify Malinois under general 'guard dog' or 'dangerous dog' breed legislation"],
        "restricted_countries": ["Several EU states with working-dog registration requirements", "Some US cities with BSL covering Malinois"],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo", "notes": "No airline-level breed ban. High-drive working dogs may need an experienced handler for crate loading."},
        ],
        "h1": "Belgian Malinois Air Travel Guide",
        "overview": (
            "The Belgian Malinois is a working breed with no universal breed ban, but it appears on restricted-breed lists in a small number of jurisdictions, particularly those with broad 'dangerous dog' legislation that classifies high-drive working breeds.\n\n"
            "Most major destination countries do not ban Belgian Malinois. The UK, USA (no federal ban), Australia, Canada, Germany, and France all accept them under standard import rules. A small number of US municipalities and some EU regional legislation may require registration or impose public muzzle requirements.\n\n"
            "Airline-side, no major carrier imposes a Malinois-specific cargo ban. The breed travels as standard large-dog cargo. The one practical note: Malinois are high-energy, high-drive working dogs. Some are difficult to crate load without an experienced handler. Airlines may refuse to handle a dog that's exhibiting extreme stress during check-in."
        ),
        "faqs": [
            {"question": "Is the Belgian Malinois banned in the UK?", "answer": "No. The UK's Dangerous Dogs Act lists four banned types: Pit Bull Terrier, Japanese Tosa, Dogo Argentino, and Fila Brasileiro. Belgian Malinois are not included. XL Bullies were added in 2024 but Malinois remain unrestricted."},
            {"question": "Can a Belgian Malinois enter Australia?", "answer": "Yes. Australia does not ban Belgian Malinois. Standard dog import applies: titre test (at least 180 days before travel), government-endorsed health certificates, mandatory quarantine at Mickleham."},
            {"question": "What countries restrict Malinois the most?", "answer": "A small number of US cities include Malinois in BSL due to their use in police and military work. Some EU regions apply working-dog registration requirements. Always check the specific city-level rules at the destination, not just national legislation."},
            {"question": "Are working Malinois (police/military dogs) subject to the same rules?", "answer": "Generally yes, with exceptions for official government working dogs travelling with security services on duty. Private owners relocating with a personal Malinois follow standard pet import rules."},
            {"question": "What cargo documentation does a Malinois need?", "answer": "Standard dog import package: ISO microchip, current rabies vaccination, government-endorsed health certificate. Add titre test for AU/NZ/Japan. Add breed-specific documentation only if the destination jurisdiction requires it — verify before travel."},
        ],
    },
    {
        "slug": "neapolitan-mastiff",
        "title": "Flying with a Neapolitan Mastiff | Breed Bans & Giant Dog Guide",
        "description": "Country bans, airline cargo logistics, and import requirements for Neapolitan Mastiffs. Which destinations ban this giant breed and how to check.",
        "breed_name": "Neapolitan Mastiff",
        "brachycephalic": True,
        "species": "dog",
        "banned_countries": ["Singapore (Neapolitan Mastiff on banned list)", "Malaysia (listed as restricted breed)", "Some other jurisdictions with broad mastiff-type bans"],
        "restricted_countries": ["Several countries with broad mastiff or large breed restrictions"],
        "airline_restrictions": [
            {"airline_name": "Many airlines (size limits)", "policy": "May require specialist cargo or refuse due to crate size", "notes": "Neapolitan Mastiffs can exceed 60-70 kg. Giant-dog crates exceed standard cargo programme dimensions on some aircraft."},
            {"airline_name": "Singapore Airlines (to Singapore)", "policy": "Cannot carry — breed banned in Singapore", "notes": "Neapolitan Mastiffs cannot enter Singapore. Singapore Airlines will not transport them to Singapore."},
            {"airline_name": "Multiple carriers (brachycephalic restrictions)", "policy": "Brachycephalic breed restrictions apply", "notes": "Neapolitan Mastiffs have pronounced facial wrinkles and some degree of airway compression. Some airlines apply additional conditions or restrictions."},
        ],
        "h1": "Neapolitan Mastiff Air Travel Guide",
        "overview": (
            "The Neapolitan Mastiff presents two distinct challenges for international travel: breed bans in several destinations, and the sheer logistics of moving a dog that can reach 70 kg or more.\n\n"
            "Singapore bans Neapolitan Mastiffs outright. Malaysia lists them as a restricted breed. Other jurisdictions with broad mastiff-type bans may also apply restrictions. Always verify the current legislation with the destination country's official government authority before planning travel.\n\n"
            "On the airline side, the Neapolitan's size creates problems. A dog of 60-70 kg plus a giant IATA-spec crate generates a volumetric weight that many standard commercial cargo programmes cannot accommodate. Add the breed's brachycephalic features (flat face, heavy skin folds around the face and neck) and some airlines apply additional conditions or restrictions.\n\n"
            "International relocation of a Neapolitan Mastiff requires a specialist pet transport agent. This is not a DIY process."
        ),
        "faqs": [
            {"question": "Where are Neapolitan Mastiffs banned?", "answer": "Singapore bans Neapolitan Mastiffs under their controlled dog regulations. Malaysia lists them as restricted. A number of other jurisdictions include broad mastiff-type bans in their legislation. Always check the specific destination country's current laws — legislation changes and online lists can be out of date."},
            {"question": "Can a Neapolitan Mastiff fly to Australia?", "answer": "Australia does not have a national ban on Neapolitan Mastiffs, but individual Australian states and territories may classify them as restricted breeds under their dangerous dog laws. This affects where the dog can be kept, but not necessarily import. Check with the Australian Department of Agriculture, Fisheries and Forestry (DAFF) and the destination state's animal management authority."},
            {"question": "Are Neapolitan Mastiffs brachycephalic?", "answer": "Partially. Neapolitan Mastiffs have significant facial skin folds and some degree of airway compression compared to long-nosed breeds. They are not as severely brachycephalic as French Bulldogs or Pugs, but some airlines apply conditions based on flat-faced characteristics. Get a vet fitness-to-fly assessment before booking cargo."},
            {"question": "What is the minimum crate size for a Neapolitan Mastiff?", "answer": "Giant Neapolitan Mastiffs often need custom-built IATA-spec crates. Standard IATA 700 crates (99 x 67 x 74 cm) are too small for many adults. A specialist pet transport supplier can build to the required dimensions."},
            {"question": "Do I need an agent for a Neapolitan Mastiff relocation?", "answer": "Yes. Given the combination of breed bans, giant size, brachycephalic considerations, and specialist cargo requirements, a specialist IPATA-member agent is essential. They can confirm destination entry, arrange appropriate carriers and crates, and manage all government paperwork."},
        ],
    },
    {
        "slug": "xl-bully",
        "title": "Flying with an XL Bully | UK Ban & International Travel Rules",
        "description": "The 2024 UK XL Bully ban explained for pet owners. What it means for import, export, and international relocation. Which other countries restrict XL Bullies.",
        "breed_name": "XL Bully",
        "brachycephalic": False,
        "species": "dog",
        "banned_countries": ["England and Wales (banned under the Dangerous Dogs Act 1991 as amended 2023)", "Scotland (effective February 2024)", "Northern Ireland (effective 2024)"],
        "restricted_countries": ["Subject to ongoing legislative developments in other countries"],
        "airline_restrictions": [
            {"airline_name": "UK carriers (to/from UK)", "policy": "Cannot carry XL Bullies to/from UK without exemption certificate", "notes": "UK ban prohibits import and ownership without a Certificate of Exemption. Airlines will not carry XL Bullies into the UK."},
            {"airline_name": "Most non-UK carriers", "policy": "Varies by destination country", "notes": "No airline-wide global ban exists outside UK routes. Check destination country laws."},
        ],
        "h1": "XL Bully Air Travel Guide",
        "overview": (
            "The XL Bully was added to the UK's list of banned dog types in 2023, with enforcement beginning 1 February 2024 in England and Wales, followed by Scotland and Northern Ireland.\n\n"
            "Under the amended Dangerous Dogs Act, importing an XL Bully into the UK is prohibited. Existing owners who applied for a Certificate of Exemption before the deadline may keep their registered, neutered, microchipped, insured dog under strict conditions, but import of new XL Bullies is banned.\n\n"
            "Outside the UK, the situation varies. Other countries are monitoring developments but most have not yet introduced specific XL Bully legislation. The breed is not banned at a federal level in the USA, Australia, Canada, or the EU, though individual states, territories, or municipalities may have restrictions.\n\n"
            "If you own an XL Bully and are planning to relocate internationally, the destination country's current legislation is the first thing to verify. Work with a specialist IPATA-member agent who is tracking active legislative changes."
        ),
        "faqs": [
            {"question": "Can I bring an XL Bully into the UK?", "answer": "No. The XL Bully was added to the UK's list of banned dog types under the Dangerous Dogs Act 1991, with import prohibition effective from 1 February 2024 in England and Wales. Importing an XL Bully into the UK is not permitted."},
            {"question": "Can I take my UK XL Bully abroad?", "answer": "You can potentially export your XL Bully to a country that does not ban it, but you cannot bring it back. Before exporting, verify the destination country's laws. Prepare all standard export documentation (microchip, vaccination records, health certificate, government endorsement). Be aware that once exported, the dog cannot legally return to the UK."},
            {"question": "Are XL Bullies banned in Australia?", "answer": "Australia does not currently have a specific federal ban on XL Bullies. However, the XL Bully is a type rather than a registered breed, and some Australian states may classify dogs as dangerous on the basis of physical characteristics rather than registered breed. Check with the destination state's animal management authority."},
            {"question": "Are XL Bullies banned in the USA?", "answer": "No federal ban exists. Some US cities and counties with broad pit bull-type BSL may classify XL Bullies under those restrictions. Always check local ordinances at the destination city, not just state law."},
            {"question": "What is the difference between an XL Bully and an American Bully?", "answer": "The XL Bully is a size category of the American Bully breed, based on height and weight. The UK ban applies to dogs that substantially conform to the XL Bully physical type, regardless of whether they are registered as American Bully XL or another name. The type-based assessment means mixed-breed dogs that resemble XL Bullies can also be affected."},
        ],
    },
    # ----- cats -----
    {
        "slug": "siamese",
        "title": "Flying with a Siamese Cat | International Travel Rules",
        "description": "Airline cabin rules, cargo options, and import paperwork for Siamese cats. One of the most vocal breeds — how to manage in-flight stress.",
        "breed_name": "Siamese",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Accepted in cabin if under weight limit", "notes": "Siamese typically weigh 3-5 kg — within in-cabin limits on most carriers."},
            {"airline_name": "British Airways", "policy": "No in-cabin pets (except assistance animals)", "notes": "Siamese must travel as cargo on BA."},
        ],
        "h1": "Siamese Cat Air Travel Guide",
        "overview": (
            "Siamese cats are one of the most vocal breeds in the world — and that's worth knowing before you plan international air travel. They are not brachycephalic, not banned anywhere, and their typical weight of 3-5 kg easily qualifies for in-cabin travel on airlines that accept cats in the cabin.\n\n"
            "The practical challenge is the noise. Siamese are communicative by nature and some individuals will vocalise throughout a flight, which creates discomfort for other passengers. The cat is not in danger — it's expressing itself. But it's worth being realistic about this when choosing in-cabin vs. cargo.\n\n"
            "Health paperwork for cats is standard: ISO microchip, current rabies vaccination (required by most destinations), government-endorsed health certificate. Australia, New Zealand, and Japan have strict cat import requirements including titre tests and quarantine."
        ),
        "faqs": [
            {"question": "Can a Siamese cat fly in the cabin?", "answer": "On airlines that accept cabin pets, yes. Siamese easily meet the weight requirements. The concern is noise — Siamese are very vocal and some will meow throughout the flight. This is normal for the breed but can create stress for the cat owner and other passengers."},
            {"question": "Are Siamese cats subject to any breed bans?", "answer": "No. No country restricts Siamese cats based on breed."},
            {"question": "What does a Siamese cat need to enter Australia?", "answer": "Australia has strict cat import rules: ISO microchip, current rabies vaccination, blood test (RNAT or FAVN titre test), a 180-day waiting period after titre confirmation, government-endorsed health certificates, and mandatory quarantine at Mickleham, Victoria. The full process takes at least six to eight months."},
            {"question": "How do I calm a Siamese cat for a flight?", "answer": "Familiarise the cat with the carrier well in advance — leave it out as a sleeping spot for weeks before travel. Feliway spray on the carrier bedding can help. Avoid food in the four hours before the flight. Do not sedate without explicit veterinary guidance and confirmation from the airline that sedation is acceptable."},
            {"question": "What carrier does a Siamese need?", "answer": "A soft-sided IATA-approved cabin carrier that fits under the seat. The cat must be able to stand, turn, and lie down inside. Most Siamese fit a medium soft-sided cabin carrier comfortably."},
        ],
    },
    {
        "slug": "maine-coon",
        "title": "Flying with a Maine Coon | Large Cat Cargo & Import Guide",
        "description": "Maine Coon international travel: why this large cat usually travels as cargo, crate sizing, airline rules, and destination paperwork.",
        "breed_name": "Maine Coon",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines (cargo for large individuals)", "policy": "Large Maine Coons likely exceed in-cabin weight limits", "notes": "Large males can reach 8-12 kg — over most in-cabin limits. Check individual cat weight before booking."},
            {"airline_name": "Some airlines (smaller females)", "policy": "May qualify for cabin", "notes": "Female Maine Coons average 4-6 kg and may qualify for in-cabin on some routes."},
        ],
        "h1": "Maine Coon Air Travel Guide",
        "overview": (
            "Maine Coons are one of the largest domestic cat breeds, and their size is the main consideration for international travel. Large males can reach 8-12 kg — above the in-cabin weight limit on most airlines. Smaller females at 4-6 kg may qualify for in-cabin travel depending on the airline's policy.\n\n"
            "No country bans Maine Coons. No airline restricts them specifically. The standard cat import process applies: microchip, rabies vaccination, health certificate. Australia and Japan add titre tests and mandatory quarantine.\n\n"
            "For Maine Coons travelling as cargo, an IATA 300 or 400 crate is typically needed. They are generally calm, adaptable cats that handle confinement reasonably well."
        ),
        "faqs": [
            {"question": "Can a Maine Coon fly in the cabin?", "answer": "Smaller females (4-6 kg) may qualify if the total cat-plus-carrier weight is under the airline's limit (typically 8 kg). Large males at 8-12 kg will not qualify and must travel as cargo. Weigh your cat and the carrier together before booking."},
            {"question": "What crate does a Maine Coon need for cargo?", "answer": "An IATA 300 for smaller cats, 400 for larger individuals. Maine Coons are long-bodied — check crate length as well as height. The cat must stand, turn, and lie flat without restriction."},
            {"question": "Are Maine Coons banned anywhere?", "answer": "No. They are not subject to any breed-specific restrictions."},
            {"question": "What's the process for flying a Maine Coon to Australia?", "answer": "Australia's cat import process is identical to its dog process in terms of documentation type: ISO microchip, rabies vaccination, titre test at least 180 days before travel, government health certificate, and mandatory quarantine at Mickleham, Victoria."},
            {"question": "Do Maine Coons handle cargo travel well?", "answer": "Generally yes. Maine Coons tend to be calm, adaptable cats with good temperaments. Crate-train in advance by leaving the carrier out as a sleeping spot. Familiar bedding in the crate helps reduce stress during transit."},
        ],
    },
    {
        "slug": "sphynx",
        "title": "Flying with a Sphynx Cat | Hairless Breed Air Travel Guide",
        "description": "How Sphynx cats cope with air cargo travel, airline rules, temperature considerations, and import requirements for this hairless breed.",
        "breed_name": "Sphynx",
        "brachycephalic": True,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Some airlines (brachycephalic concern)", "policy": "May apply additional conditions for snub-nosed cats", "notes": "Sphynx cats have relatively flat faces. Some airlines classify them alongside other brachycephalic breeds. Confirm with the airline."},
            {"airline_name": "Most airlines allowing cabin pets", "policy": "May qualify for cabin by weight", "notes": "Sphynx typically weigh 3-5 kg — within in-cabin limits."},
        ],
        "h1": "Sphynx Cat Air Travel Guide",
        "overview": (
            "Sphynx cats are hairless, sociable, and warmer to the touch than most cats due to their lack of insulating coat. Both of these traits matter for air travel.\n\n"
            "The hairless body means Sphynx cats lose heat quickly in cool environments. The aircraft hold is maintained at a safe temperature, but ground handling time in cold conditions can be a concern. Use a well-insulated crate with warm bedding. If travelling in cold months, include a self-warming pad.\n\n"
            "Sphynx cats also have a moderately flattened face — not as extreme as a Persian, but enough that some airlines treat them as brachycephalic and apply additional conditions. Confirm with your airline before booking.\n\n"
            "No country bans Sphynx cats. Standard cat import documentation applies."
        ),
        "faqs": [
            {"question": "Do airlines restrict Sphynx cats as brachycephalic?", "answer": "Some do. The Sphynx has a moderately flat face compared to longnosed breeds, and some airlines include them in their list of snub-nosed cat breeds subject to additional conditions or fitness-to-fly requirements. Check the specific airline's published brachycephalic breed list."},
            {"question": "Does a Sphynx cat get cold in cargo?", "answer": "The hold is pressurised and temperature-controlled, typically at 16-24°C. Ground handling time in cold conditions is more of a concern. Provide warm bedding in the crate and a self-warming pad for cold-weather travel. Cover ventilation openings with a mesh barrier to reduce cold drafts without blocking airflow."},
            {"question": "Are Sphynx cats banned anywhere?", "answer": "No. Sphynx cats are not subject to breed-specific restrictions in any destination country."},
            {"question": "Can a Sphynx fly in the cabin?", "answer": "On airlines that accept cabin pets, usually yes — Sphynx typically weigh 3-5 kg and meet weight limits. Their sociable, human-attached nature makes in-cabin travel less stressful for them than solitary cargo. If the airline classifies them as snub-nosed, you may need a fitness certificate."},
            {"question": "Do Sphynx cats need special documentation?", "answer": "No breed-specific documentation. Standard cat import paperwork: ISO microchip, rabies vaccination, government-endorsed health certificate. Add titre test for AU/NZ/Japan."},
        ],
    },
    {
        "slug": "ragdoll",
        "title": "Flying with a Ragdoll | Large Cat Cargo & Cabin Guide",
        "description": "Ragdoll international travel: cabin eligibility, cargo crate sizing, and a calm breed's guide to air transport and destination paperwork.",
        "breed_name": "Ragdoll",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines (cabin — for lighter cats)", "policy": "Females and young Ragdolls may qualify for cabin", "notes": "Females average 4-6 kg. Large males reach 8 kg+. Weigh the cat plus carrier before booking."},
            {"airline_name": "Most major airlines (cargo)", "policy": "Accepted in cargo", "notes": "No breed restrictions. IATA 300-400 crate."},
        ],
        "h1": "Ragdoll Cat Air Travel Guide",
        "overview": (
            "Ragdolls are large, placid cats and one of the most temperamentally suited breeds for international travel. They are not brachycephalic, not banned anywhere, and their famously relaxed disposition means they are less prone to severe stress during transit than more anxious breeds.\n\n"
            "The size consideration is the same as for Maine Coons: large adult males can reach 8 kg or more, pushing them over in-cabin weight limits. Smaller females and younger cats may qualify for cabin travel. Weigh carefully.\n\n"
            "Standard cat import documentation applies worldwide: microchip, rabies vaccination, government health certificate. Australia and Japan add titre tests and quarantine."
        ),
        "faqs": [
            {"question": "Can a Ragdoll fly in the cabin?", "answer": "Smaller females and young Ragdolls under 8 kg including the carrier may qualify. Large males typically do not. Weigh your specific cat plus carrier before booking."},
            {"question": "Are Ragdolls good travellers?", "answer": "Yes, in general. Ragdolls are known for their calm, floppy temperament. They tend to handle confinement better than high-strung breeds. Crate training in advance is still beneficial."},
            {"question": "Are Ragdolls banned anywhere?", "answer": "No. No country restricts Ragdolls."},
            {"question": "What crate size does a Ragdoll need for cargo?", "answer": "An IATA 300 for smaller individuals, 400 for larger males. Ragdolls are long-bodied — check crate length as well as height."},
            {"question": "What documents does a Ragdoll need to enter Japan?", "answer": "Japan requires all cats to have an ISO microchip, current rabies vaccination, a titre test confirmed at an MAFF-approved laboratory, and a 180-day waiting period after the titre result. Government health certificates must accompany the cat. Cats arriving without this preparation face extended quarantine at the owner's expense."},
        ],
    },
    {
        "slug": "bengal-cat",
        "title": "Flying with a Bengal Cat | Country Restrictions & Travel Guide",
        "description": "Which countries restrict or ban Bengal cats, airline rules, and what F-generation classification means for international travel.",
        "breed_name": "Bengal Cat",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": ["Hawaii (USA) — F1-F4 Bengals with recent wild ancestry prohibited", "Australia (F1-F3 Bengals banned)", "Some other jurisdictions based on generation"],
        "restricted_countries": ["Several countries check Bengal generation number before import"],
        "airline_restrictions": [
            {"airline_name": "Most major airlines", "policy": "Accepted in cargo or cabin (if weight qualifies)", "notes": "No airline-level breed ban. Destination country laws apply."},
        ],
        "h1": "Bengal Cat Air Travel Guide",
        "overview": (
            "Bengal cats are a hybrid breed, descended from crosses between domestic cats and the Asian Leopard Cat. That wild ancestry creates a specific complication for international travel: some countries restrict or ban early-generation Bengals based on the number of generations from the wild ancestor.\n\n"
            "F1, F2, and F3 Bengals (the first three generations from a wild cat) are banned in Australia and some other jurisdictions. Hawaii prohibits Bengals with recent wild ancestry under its strict endemic wildlife protection laws. Most F4 and later-generation Bengals (which is what the vast majority of pet Bengals are) are accepted without breed-specific restrictions in most countries.\n\n"
            "Before booking any international travel with a Bengal, confirm your cat's generation number from its pedigree papers and check the destination country's current rules on hybrid cat import. The CITES status of the Asian Leopard Cat may also be relevant for some jurisdictions."
        ),
        "faqs": [
            {"question": "Is my Bengal cat allowed in Australia?", "answer": "F1, F2, and F3 Bengals are prohibited in Australia due to regulations on wild-hybrid cats. F4 and later generations (which most pet Bengals are) are generally permitted, but you must be able to document the generation from official pedigree records. Contact the Australian Department of Agriculture, Fisheries and Forestry (DAFF) to confirm before booking."},
            {"question": "What generation is my Bengal?", "answer": "The generation is calculated from the wild ancestor. F1 = first generation from wild cat. F2 = offspring of F1. F3 = offspring of F2. F4 = offspring of F3, and so on. Most pet shop and breeder Bengals are F4 or later. Your cat's pedigree certificate should state the SBT (Studbook Tradition) or F-generation designation."},
            {"question": "Can a Bengal cat fly to the UK?", "answer": "Yes. The UK does not have specific Bengal generation restrictions. Standard cat import rules apply: microchip, rabies vaccination (or titre test for some countries), government-endorsed health certificate. Post-Brexit, cats entering the UK from EU countries need an AHC or UK-issued health certificate."},
            {"question": "Is the Bengal cat banned in Hawaii?", "answer": "Hawaii has specific restrictions on wild-hybrid cats to protect its native ecosystem. Early-generation Bengals with documented wild ancestry may be prohibited. Domestic Bengals of established generation (typically F4+) may be permitted with documentation, but Hawaii's rules are strict — confirm with the Hawaii Department of Agriculture before booking."},
            {"question": "Do I need a CITES permit for a Bengal cat?", "answer": "For most domestic pet Bengals (F4 and later), a CITES permit is not required. Earlier generations that are closer to the wild Asian Leopard Cat may require documentation under CITES Appendix II. If you are uncertain, check with your national CITES authority before travel."},
        ],
    },
    {
        "slug": "norwegian-forest-cat",
        "title": "Flying with a Norwegian Forest Cat | International Travel Guide",
        "description": "Airline rules and import paperwork for Norwegian Forest Cats. Large, thick-coated cats and what that means for cargo travel.",
        "breed_name": "Norwegian Forest Cat",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Smaller cats may qualify for cabin", "notes": "NFC typically weigh 4-9 kg. Lighter females may meet in-cabin limits."},
        ],
        "h1": "Norwegian Forest Cat Air Travel Guide",
        "overview": (
            "Norwegian Forest Cats are large, semi-longhaired cats with no breed bans anywhere and no airline-specific restrictions. Their weight (4-9 kg for adults) means some individuals will qualify for in-cabin travel while larger cats travel as cargo.\n\n"
            "Their thick double coat creates mild temperature considerations similar to Arctic dog breeds: in very hot conditions, the coat retains heat. Standard cargo hold temperature controls are adequate, but long ground handling in hot conditions is worth monitoring.\n\n"
            "Health paperwork follows the standard cat import process for whichever destination you're heading to."
        ),
        "faqs": [
            {"question": "Can a Norwegian Forest Cat fly in the cabin?", "answer": "Lighter females (4-6 kg) may qualify if the cat-plus-carrier weight is under the airline's limit. Larger males will not. Weigh your cat and carrier together."},
            {"question": "Are Norwegian Forest Cats banned anywhere?", "answer": "No."},
            {"question": "What crate does a Norwegian Forest Cat need for cargo?", "answer": "IATA 300 for smaller cats, 400 for larger individuals. They are long-bodied cats — check crate length as well as height."},
            {"question": "What documents does a Norwegian Forest Cat need to enter Australia?", "answer": "ISO microchip, rabies vaccination, titre test (blood sample sent to approved laboratory, result confirmed at least 180 days before entry), government health certificate, and mandatory quarantine at Mickleham, Victoria. Same process as all cats entering Australia."},
            {"question": "How should I prepare a Norwegian Forest Cat for cargo?", "answer": "Crate train well in advance. Leave the carrier out as a sleeping space for several weeks before travel. Trim claws so they do not catch on the crate grille. Provide familiar bedding in the crate."},
        ],
    },
    {
        "slug": "abyssinian",
        "title": "Flying with an Abyssinian Cat | International Transport Guide",
        "description": "Airline cabin rules, import paperwork, and travel tips for Abyssinians. An active, curious breed — what to expect in transit.",
        "breed_name": "Abyssinian",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Qualifies for cabin by weight on most carriers", "notes": "Abyssinians typically weigh 3-5 kg — within in-cabin limits."},
        ],
        "h1": "Abyssinian Cat Air Travel Guide",
        "overview": (
            "Abyssinians are slender, active, highly curious cats. They are not brachycephalic, not restricted by any country's laws, and their typical weight of 3-5 kg qualifies them for in-cabin travel on most airlines that accept cabin pets.\n\n"
            "The practical concern with Abyssinians is temperament. They are intelligent, high-energy cats that do not always handle confinement calmly. Some individuals settle well in a familiar carrier; others are highly stressed by it. Know your cat's temperament before committing to a long-haul flight.\n\n"
            "Standard import paperwork applies. If travelling in-cabin, the carrier must fit under the seat. If in cargo, an IATA 300 crate is standard."
        ),
        "faqs": [
            {"question": "Can an Abyssinian fly in the cabin?", "answer": "Yes, on airlines that accept cabin pets. At 3-5 kg, they easily meet weight requirements."},
            {"question": "Are Abyssinians good fliers?", "answer": "Variable. Some Abyssinians are calm in carriers; others are not. Given their active, curious temperament, crate training is especially important for this breed. A well-crate-trained Abyssinian can travel without problems. An untrained one may be very distressed."},
            {"question": "Are Abyssinians restricted anywhere?", "answer": "No. No country has breed-specific restrictions on Abyssinians."},
            {"question": "What does an Abyssinian need to enter New Zealand?", "answer": "New Zealand requires all cats to have an ISO microchip, current rabies vaccination, a titre test with blood sample from an approved laboratory, 180-day wait after titre confirmation, and mandatory quarantine at the Levin MPI facility. Total timeline is at least six to eight months."},
            {"question": "How do I crate-train an Abyssinian?", "answer": "Leave the carrier open in a room the cat uses regularly. Encourage exploration with treats inside. Feed meals near the carrier and eventually inside it. Gradually close the door for short periods. Build up over several weeks. An Abyssinian that sleeps willingly in its carrier before the flight will manage the flight far better."},
        ],
    },
    {
        "slug": "russian-blue",
        "title": "Flying with a Russian Blue | Calm Breed's International Travel Guide",
        "description": "Russian Blue international travel: airline rules, health documentation, and why this gentle, reserved breed handles air travel better than most.",
        "breed_name": "Russian Blue",
        "brachycephalic": False,
        "species": "cat",
        "banned_countries": [],
        "restricted_countries": [],
        "airline_restrictions": [
            {"airline_name": "Most airlines allowing cabin pets", "policy": "Qualifies for cabin by weight", "notes": "Russian Blues typically weigh 3.5-5.5 kg — within in-cabin limits on most carriers."},
        ],
        "h1": "Russian Blue Air Travel Guide",
        "overview": (
            "Russian Blues are gentle, reserved cats that travel well by temperament. They bond closely with their owners and while they can be shy with strangers, they generally handle change better than more sensitive or anxious breeds.\n\n"
            "At 3.5-5.5 kg, they qualify for in-cabin travel on most airlines that accept cabin pets. No country bans Russian Blues. No airline restricts them. Standard cat import documentation applies.\n\n"
            "Their double coat (which sheds seasonally) is not thick enough to cause temperature concerns in cargo. They are not brachycephalic. In practical terms, Russian Blues are one of the more straightforward breeds to travel internationally."
        ),
        "faqs": [
            {"question": "Can a Russian Blue fly in the cabin?", "answer": "Yes, on airlines that accept cabin pets. At 3.5-5.5 kg, they easily meet in-cabin weight limits on most carriers."},
            {"question": "Are Russian Blues banned anywhere?", "answer": "No."},
            {"question": "Do Russian Blues handle cargo well?", "answer": "They are generally adaptable. Their calm, reserved nature means they are less likely to be severely distressed than highly-strung breeds. Crate training before the flight always helps."},
            {"question": "What documents does a Russian Blue need for EU travel from the UK?", "answer": "An Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel, along with a valid rabies vaccination record and ISO microchip scan. Microchip must have been implanted before or at the time of first rabies vaccination."},
            {"question": "How do I keep a Russian Blue calm during a flight?", "answer": "Familiar carrier (crate-trained in advance), familiar bedding with the owner's scent, Feliway spray on the carrier bedding 30 minutes before the cat goes in. Russian Blues are bonded to their owners, so in-cabin travel where the cat can see and smell you is less stressful than cargo. Use cargo only when size or airline policy requires it."},
        ],
    },
]


def slug_exists(slug: str) -> bool:
    path = os.path.join(CONTENT_DIR, f"{slug}.md")
    return os.path.exists(path)


def write_breed_page(breed: dict) -> bool:
    slug = breed["slug"]
    if slug_exists(slug):
        return False

    path = os.path.join(CONTENT_DIR, f"{slug}.md")

    banned = "\n".join(f'  - "{c}"' for c in breed["banned_countries"]) if breed["banned_countries"] else ""
    restricted = "\n".join(f'  - "{c}"' for c in breed["restricted_countries"]) if breed["restricted_countries"] else ""

    airline_lines = []
    for a in breed["airline_restrictions"]:
        airline_lines.append(
            f'  - airline_name: "{a["airline_name"]}"\n'
            f'    policy: "{a["policy"]}"\n'
            f'    notes: "{a["notes"]}"'
        )

    faq_lines = []
    for f in breed["faqs"]:
        q = f["question"].replace('"', "'")
        a = f["answer"].replace('"', "'")
        faq_lines.append(f'  - question: "{q}"\n    answer: "{a}"')

    content = f"""---
title: "{breed['title']}"
description: "{breed['description']}"
type: "breeds"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
breed_name: "{breed['breed_name']}"
brachycephalic: {str(breed['brachycephalic']).lower()}
species: "{breed['species']}"
banned_countries:
{banned if banned else "  []"}
restricted_countries:
{restricted if restricted else "  []"}
airline_restrictions:
{chr(10).join(airline_lines)}
content:
  h1: "{breed['h1']}"
  overview: |
{chr(10).join('    ' + line for line in breed['overview'].splitlines())}
faqs:
{chr(10).join(faq_lines)}
---
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


if __name__ == "__main__":
    os.makedirs(CONTENT_DIR, exist_ok=True)
    written = 0
    skipped = 0
    for breed in BREEDS:
        if write_breed_page(breed):
            written += 1
            print(f"  Written: {breed['slug']}")
        else:
            skipped += 1
            print(f"  Skipped (exists): {breed['slug']}")
    print(f"\nDone. Written: {written} | Skipped: {skipped} | Total in breeds/: {written + 35}")
