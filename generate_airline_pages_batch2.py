"""
Phase 6 Task 6.5 — New Airline Pages (Batch 2)
10 new airline guide pages for high-value carriers not yet covered.
Skip-if-exists logic on every file.
"""
import os

AIRLINES_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\airlines"
os.makedirs(AIRLINES_DIR, exist_ok=True)

AIRLINES = [
    {
        "slug": "air-new-zealand",
        "title": "Air New Zealand Pet Cargo Policy | Pet Transport Global",
        "description": "Air New Zealand pet transport policy: cargo service, breed restrictions, temperature rules, and what pets need to fly with Air New Zealand.",
        "airline_name": "Air New Zealand",
        "hub": "Auckland Airport (AKL)",
        "alliance": "Star Alliance",
        "cabin_allowed": False,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Dogs and cats accepted as manifest cargo. Animals in cabin not permitted.",
            "crate_requirements": "IATA-compliant rigid container. Pet must be able to stand, sit upright, lie down, and turn around without touching sides.",
            "size_limits": "Varies by aircraft type and route. Confirm with Air New Zealand Cargo before booking.",
            "temperature_restrictions": "Live animal embargoes during extreme heat and cold. Check restrictions at time of booking.",
            "brachycephalic_policy": "Air New Zealand restricts a list of brachycephalic (snub-nosed) breeds including English Bulldogs, French Bulldogs, Pugs, Boston Terriers, Shih Tzus, and others. Check the current restricted breeds list with the airline.",
            "cost_range": "Varies by route, crate dimensions, and total weight. Contact Air New Zealand Cargo for a quote.",
            "booking_process": "Book through Air New Zealand Cargo or an IPATA-accredited pet transport agent. Live animal space is limited — book well in advance.",
        },
        "overview": """Air New Zealand operates from its Auckland hub connecting New Zealand to Australia, Asia, the Pacific Islands, the UK, and North America. The airline accepts dogs and cats as manifest cargo on most international routes, though cabin travel is not available.

New Zealand is a rabies-free country with strict biosecurity rules, which affects pet transport in both directions. Pets arriving in New Zealand face managed isolation requirements managed by MPI (Ministry for Primary Industries). Pets leaving New Zealand for countries that require titre tests will need advance veterinary preparation.

This page covers Air New Zealand's current pet cargo policy. Always confirm details with the airline directly before booking, as policies are subject to change.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on Air New Zealand?",
                "a": "No. Air New Zealand does not allow dogs or cats in the passenger cabin. All pets must travel as manifest cargo in the hold."
            },
            {
                "q": "Does Air New Zealand have a brachycephalic breed restriction?",
                "a": "Yes. Air New Zealand restricts snub-nosed breeds including English Bulldogs, French Bulldogs, Pugs, Boston Terriers, Shih Tzus, Cavalier King Charles Spaniels, Pekingese, and others. Check the current restricted breeds list with Air New Zealand Cargo before booking."
            },
            {
                "q": "How do I book pet cargo on Air New Zealand?",
                "a": "Contact Air New Zealand Cargo directly or use an IPATA-accredited pet transport agent experienced with New Zealand routes. Book as early as possible — live animal cargo space is limited on long-haul routes."
            },
            {
                "q": "What documentation does my pet need to fly Air New Zealand?",
                "a": "At minimum: a valid veterinary health certificate, microchip documentation, and current vaccination records. Destination country import requirements apply in addition — New Zealand arrivals require an MPI import health standard and managed isolation booking."
            },
            {
                "q": "Does Air New Zealand fly pets on UK routes?",
                "a": "Air New Zealand operates London Heathrow to Auckland routes. Pet cargo acceptance on this route should be confirmed directly with Air New Zealand Cargo, as long-haul live animal acceptance can vary."
            },
        ],
    },
    {
        "slug": "ana-all-nippon-airways",
        "title": "ANA (All Nippon Airways) Pet Policy | Pet Transport Global",
        "description": "ANA All Nippon Airways pet transport policy: cabin rules, cargo service, breed restrictions, and what pets need to fly with ANA on domestic and international routes.",
        "airline_name": "ANA (All Nippon Airways)",
        "hub": "Tokyo Narita (NRT) / Tokyo Haneda (HND)",
        "alliance": "Star Alliance",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Dogs, cats, and small birds accepted in cabin (domestic Japan only, size restrictions apply). Dogs and cats accepted as cargo on international routes.",
            "crate_requirements": "In-cabin: soft carrier meeting ANA size limits (45cm x 35cm x 25cm typical, carrier + pet under 10kg). Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin on domestic routes: carrier + pet combined under 10kg. International cargo: varies by route and aircraft.",
            "temperature_restrictions": "Live animal embargoes during summer heat. Temperature restrictions apply on routes transiting Japan in peak summer.",
            "brachycephalic_policy": "Brachycephalic breeds are not accepted for cabin travel on ANA domestic routes. Acceptance as international cargo is subject to route and seasonal conditions. Confirm with ANA before booking.",
            "cost_range": "Domestic in-cabin: fee per flight (confirm with ANA). International cargo: varies by route, weight, and crate dimensions.",
            "booking_process": "In-cabin on domestic routes: book via ANA reservation. International cargo: contact ANA Cargo or use an IPATA-accredited agent.",
        },
        "overview": """ANA (All Nippon Airways) is Japan's largest airline and a Star Alliance member, operating from Tokyo's Narita and Haneda airports. It connects Japan to destinations across Asia, Europe, North America, and Australia.

On domestic Japanese routes, ANA allows small pets (dogs, cats, small birds) in the passenger cabin. On international routes, pets travel as cargo only. Japan's import rules for live animals are managed by the MAFF Quarantine Service, and pets arriving in Japan face a quarantine period that can range from 12 hours to several months depending on origin country and documentation.

This page covers ANA's pet policy. Policies change — always verify with ANA directly before booking.""",
        "faqs": [
            {
                "q": "Can I bring my dog in the cabin on an ANA international flight?",
                "a": "No. ANA only allows pets in the cabin on domestic Japanese routes. On all international flights, dogs and cats travel as cargo."
            },
            {
                "q": "How long is quarantine for pets arriving in Japan?",
                "a": "Japan's quarantine period depends on origin country and documentation completeness. Pets from approved rabies-free countries (e.g., UK, Australia, New Zealand) face a minimum 12-hour quarantine if all paperwork is correct. Pets from other countries may face significantly longer periods. Contact the MAFF Quarantine Service at the destination airport well in advance."
            },
            {
                "q": "Does ANA accept French Bulldogs or Pugs?",
                "a": "Brachycephalic breeds are not accepted for ANA domestic cabin travel. For international cargo, acceptance of brachycephalic breeds varies by route, season, and current conditions. Always confirm with ANA Cargo before booking a snub-nosed breed."
            },
            {
                "q": "What documents does my pet need for an ANA international flight?",
                "a": "Valid veterinary health certificate, microchip documentation, and current vaccination records are required. Japan-bound pets must also meet MAFF quarantine documentation requirements, which vary by origin country. Contact the MAFF Animal Quarantine Service for your specific origin well in advance."
            },
            {
                "q": "How do I book cargo for my pet on ANA?",
                "a": "Contact ANA Cargo directly or work with an IPATA-accredited pet transport agent with Japan experience. Japan's quarantine documentation is complex, and an agent familiar with MAFF procedures can help avoid delays."
            },
        ],
    },
    {
        "slug": "iberia",
        "title": "Iberia Pet Policy | Pet Transport Global",
        "description": "Iberia airlines pet transport policy: cabin rules for small pets, cargo service, breed restrictions, and booking your pet with Iberia on Spanish and Latin American routes.",
        "airline_name": "Iberia",
        "hub": "Madrid Barajas Airport (MAD)",
        "alliance": "Oneworld",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs and cats in cabin (under 8kg combined with carrier). Dogs and cats in cargo hold.",
            "crate_requirements": "In-cabin: carrier max 55cm x 35cm x 25cm, pet + carrier under 8kg. Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: combined weight (pet + carrier) under 8kg. Cargo: no fixed limit but confirm with Iberia Cargo by route.",
            "temperature_restrictions": "Temperature embargoes may apply during peak summer. Confirm at time of booking.",
            "brachycephalic_policy": "Brachycephalic breeds generally accepted in cabin if they meet the weight limit, with a vet health certificate confirming suitability for air travel. Cargo acceptance of snub-nosed breeds is subject to route and conditions.",
            "cost_range": "In-cabin: approximately EUR 20-50 per flight segment (confirm with Iberia). Cargo: varies by weight and route.",
            "booking_process": "In-cabin: book via Iberia website or call centre when reserving flight. Maximum 2 pets per flight. Cargo: contact Iberia Cargo.",
        },
        "overview": """Iberia is Spain's flag carrier and a Oneworld member, operating from Madrid Barajas Airport (MAD). It connects Spain and Europe to Latin America, the USA, Africa, and the Middle East, making it one of the primary carriers for pet transport between Europe and Latin America.

Small pets can travel in the cabin on Iberia flights, which is a useful option for cats and small dogs on shorter European routes. Larger pets travel in the hold as cargo. Iberia's Latin American network is particularly useful for pets moving between Spain, Portugal, and countries like Argentina, Colombia, Brazil, and Mexico.

This page covers Iberia's current pet policy. Always confirm current rules with Iberia before booking.""",
        "faqs": [
            {
                "q": "Can I take my cat in the cabin on Iberia?",
                "a": "Yes, if the cat and carrier combined weigh under 8kg and the carrier fits within Iberia's size limits (55cm x 35cm x 25cm). A health certificate is required. Book in advance — there are limits on the number of pets per flight."
            },
            {
                "q": "Does Iberia fly pets to Latin America?",
                "a": "Yes. Iberia operates extensive routes between Madrid and Latin America including Argentina, Colombia, Mexico, Brazil, Peru, Chile, and others. Pets can travel as cargo on these routes. Each Latin American destination has its own import requirements — check those separately."
            },
            {
                "q": "Does Iberia accept brachycephalic breeds?",
                "a": "Iberia generally accepts brachycephalic breeds in cabin if they meet the weight limit and a vet certifies them as fit for flight. For cargo travel, acceptance depends on route and conditions. Confirm with Iberia before booking any flat-faced breed."
            },
            {
                "q": "How do I book my pet on an Iberia flight?",
                "a": "For in-cabin travel, book through the Iberia website or contact their customer service when reserving your ticket. For cargo, contact Iberia Cargo. In-cabin pets are limited per flight, so book as early as possible."
            },
            {
                "q": "What documents does my pet need for Iberia travel?",
                "a": "A valid veterinary health certificate is required. Within the EU (including Spain), an EU pet passport recording microchip and rabies vaccination is accepted. For non-EU origin countries, an Animal Health Certificate in the correct format is needed. Destination country requirements apply separately."
            },
        ],
    },
    {
        "slug": "tap-air-portugal",
        "title": "TAP Air Portugal Pet Policy | Pet Transport Global",
        "description": "TAP Air Portugal pet transport policy: cabin rules for small pets, cargo options, breed restrictions, and booking your pet on TAP for Europe and transatlantic routes.",
        "airline_name": "TAP Air Portugal",
        "hub": "Lisbon Humberto Delgado Airport (LIS)",
        "alliance": "Star Alliance",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs and cats in cabin (under 8kg combined with carrier, intra-European routes). Larger pets in cargo hold.",
            "crate_requirements": "In-cabin: soft carrier max 55cm x 35cm x 20cm, pet + carrier under 8kg. Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: combined weight under 8kg. Cargo: confirm with TAP Cargo by route.",
            "temperature_restrictions": "Temperature restrictions may apply on certain routes and seasons. Confirm at booking.",
            "brachycephalic_policy": "Snub-nosed breeds are not accepted in the cabin on TAP. Cargo acceptance of brachycephalic breeds is subject to route and conditions.",
            "cost_range": "In-cabin within Europe: approximately EUR 40-60 per segment. Cargo: varies by route and weight.",
            "booking_process": "In-cabin: add when booking ticket via TAP website or contact centre. Cargo: contact TAP Cargo.",
        },
        "overview": """TAP Air Portugal is Portugal's flag carrier and a Star Alliance member, operating from Lisbon (LIS). It connects Portugal to Europe, Brazil, the USA, Canada, Africa, and some Asian destinations.

TAP is often the airline of choice for pets moving between the UK/Europe and Portugal (including Madeira and the Azores), as well as between Europe and Brazil. Note that Madeira and the Azores have stricter pet import rules than mainland Portugal — pets arriving at these island destinations need a rabies titre test.

Small pets can travel in the cabin on TAP's intra-European routes. Larger pets travel as cargo. This page covers TAP's current pet policy — always verify directly with TAP before booking.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on TAP Air Portugal?",
                "a": "Small dogs (combined weight with carrier under 8kg) can travel in cabin on TAP's intra-European routes. Dogs are not permitted in the cabin on transatlantic routes. A health certificate is required."
            },
            {
                "q": "Does TAP fly pets to Brazil?",
                "a": "Yes. TAP operates routes between Lisbon and multiple Brazilian cities including Sao Paulo, Rio de Janeiro, Fortaleza, Recife, and others. Larger pets travel as cargo on these transatlantic routes. Brazil requires a MAPA-format health certificate endorsed by the appropriate authority."
            },
            {
                "q": "Does TAP accept brachycephalic breeds in the cabin?",
                "a": "TAP does not accept brachycephalic (snub-nosed) breeds in the cabin. Cargo acceptance is subject to route and conditions — confirm with TAP Cargo."
            },
            {
                "q": "Can I fly my pet to Madeira or the Azores on TAP?",
                "a": "TAP operates routes to Madeira and the Azores. Note that these are rabies-free island territories with stricter pet import rules than mainland Portugal. Pets from non-EU countries need a rabies titre test result at least 90 days before arrival. Plan well in advance."
            },
            {
                "q": "How do I book pet cargo on TAP?",
                "a": "Contact TAP Cargo for hold travel, or add an in-cabin pet when booking via the TAP website. In-cabin spots are limited — book early."
            },
        ],
    },
    {
        "slug": "aer-lingus",
        "title": "Aer Lingus Pet Policy | Pet Transport Global",
        "description": "Aer Lingus pet transport policy: cargo service, breed restrictions, and what pets need to fly with Aer Lingus on Ireland's transatlantic and European routes.",
        "airline_name": "Aer Lingus",
        "hub": "Dublin Airport (DUB)",
        "alliance": "Oneworld",
        "cabin_allowed": False,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Dogs and cats accepted in the cargo hold. Pets are not accepted in the passenger cabin.",
            "crate_requirements": "IATA-compliant rigid container. Pet must be able to stand, sit upright, lie down, and turn around.",
            "size_limits": "Varies by aircraft and route. Confirm with Aer Lingus before booking.",
            "temperature_restrictions": "Temperature embargoes may apply. Confirm restrictions at time of booking.",
            "brachycephalic_policy": "Snub-nosed breeds face restrictions on Aer Lingus cargo. The airline follows industry guidance on brachycephalic breeds. Confirm current acceptance status for specific breeds before booking.",
            "cost_range": "Varies by route, crate dimensions, and weight. Contact Aer Lingus for a quote.",
            "booking_process": "Contact Aer Lingus cargo team directly or use an IPATA-accredited agent for complex routes.",
        },
        "overview": """Aer Lingus is Ireland's national carrier and a Oneworld member, operating from Dublin (DUB) with secondary hubs at Cork and Shannon. It connects Ireland to the UK, Europe, and the USA, making it an important carrier for pets moving between Ireland and the rest of the world.

Pets are not permitted in the Aer Lingus passenger cabin. Dogs and cats can travel as cargo. For routes between Ireland and the UK, note that both countries require specific health documentation — Ireland as an EU member requires EU pet passport standards, while the UK requires an AHC post-Brexit.

This page covers Aer Lingus's current pet cargo policy. Always verify with the airline directly before booking.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on Aer Lingus?",
                "a": "No. Aer Lingus does not allow pets in the passenger cabin. Dogs and cats travel as cargo."
            },
            {
                "q": "Does Aer Lingus accept pets on transatlantic routes?",
                "a": "Aer Lingus operates Dublin to the USA and Canada. Pet cargo acceptance on transatlantic routes should be confirmed directly with Aer Lingus — availability varies. An IPATA-accredited agent can assist with booking and documentation for USA/Canada routes."
            },
            {
                "q": "What documents does my pet need to fly with Aer Lingus from Ireland to the UK?",
                "a": "Ireland is an EU member, so Irish-registered pets have EU pet passports. Pets entering the UK from Ireland need an Animal Health Certificate (AHC) in addition, issued by an Official Veterinarian in Ireland and endorsed by DAFM. The UK's tapeworm treatment requirement (1-5 days before entry) applies to dogs."
            },
            {
                "q": "Are brachycephalic breeds accepted on Aer Lingus?",
                "a": "Aer Lingus follows industry guidelines on brachycephalic breeds. Restrictions apply to flat-faced breeds due to welfare concerns. Confirm the current policy for your specific breed before booking."
            },
            {
                "q": "How do I book cargo for my pet on Aer Lingus?",
                "a": "Contact the Aer Lingus cargo team directly. For complex international routes, an IPATA-accredited pet transport agent can help coordinate the booking and required documentation."
            },
        ],
    },
    {
        "slug": "finnair",
        "title": "Finnair Pet Policy | Pet Transport Global",
        "description": "Finnair pet transport policy: cabin rules for small pets, cargo service, breed restrictions, and what pets need on Finland's gateway to Asia and Europe.",
        "airline_name": "Finnair",
        "hub": "Helsinki-Vantaa Airport (HEL)",
        "alliance": "Oneworld",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs, cats, and small household birds accepted in cabin (size and weight limits apply). Dogs and cats in cargo hold.",
            "crate_requirements": "In-cabin: carrier max 55cm x 40cm x 23cm, pet + carrier under 8kg. Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: combined weight (pet + carrier) under 8kg. Cargo: confirm by route and aircraft.",
            "temperature_restrictions": "Temperature embargoes apply on certain routes and seasons, particularly long-haul. Confirm at time of booking.",
            "brachycephalic_policy": "Brachycephalic breeds not accepted in the cabin. Cargo acceptance is subject to route and conditions — confirm with Finnair.",
            "cost_range": "In-cabin: from approximately EUR 50 per segment. Cargo: varies by route and dimensions.",
            "booking_process": "In-cabin: add when booking ticket online or contact Finnair. Cargo: contact Finnair Cargo or use an IPATA agent.",
        },
        "overview": """Finnair is Finland's flag carrier and a Oneworld member, operating from Helsinki-Vantaa Airport (HEL). Finnair is notable for its Asia routes — it operates some of the most direct connections between Europe and Japan, South Korea, China, and Singapore, flying over the Arctic.

This Arctic routing makes Finnair a popular choice for pets moving between Europe and Asia. However, long-haul routes have specific cargo restrictions, and Finland's cold winters can trigger temperature embargoes.

Small pets can travel in the cabin on Finnair flights within the weight limits. Larger pets and those on long-haul routes travel as cargo. This page covers Finnair's current pet policy — verify with the airline before booking.""",
        "faqs": [
            {
                "q": "Can I take my cat in the cabin on Finnair?",
                "a": "Yes, if the cat and carrier combined weigh under 8kg and fit within Finnair's carrier dimensions (55cm x 40cm x 23cm). A health certificate is required. Cabin pets are limited per flight — book early."
            },
            {
                "q": "Does Finnair fly pets to Japan?",
                "a": "Finnair operates direct Helsinki-Tokyo routes. Larger pets travel as cargo. Japan has strict quarantine requirements managed by MAFF — prepare well in advance and confirm acceptance with Finnair Cargo for Japan-bound shipments."
            },
            {
                "q": "Does Finnair accept brachycephalic breeds in the cabin?",
                "a": "No. Brachycephalic breeds are not accepted in the Finnair cabin. Cargo acceptance depends on route and conditions — confirm with Finnair Cargo."
            },
            {
                "q": "What documents do I need to fly a pet with Finnair within Europe?",
                "a": "Within the EU (Finland is an EU member), an EU pet passport with current microchip and rabies vaccination records is sufficient. For travel to or from non-EU countries, an Animal Health Certificate in the correct format is required."
            },
            {
                "q": "How do I book cargo for my pet on Finnair long-haul routes?",
                "a": "Contact Finnair Cargo directly or use an IPATA-accredited pet transport agent. Long-haul cargo space for live animals is limited — book well in advance, and have destination country import documentation confirmed before booking cargo."
            },
        ],
    },
    {
        "slug": "aeromexico",
        "title": "Aeromexico Pet Policy | Pet Transport Global",
        "description": "Aeromexico pet transport policy: cabin rules for small pets, cargo service, breed restrictions, and what pets need to fly with Mexico's flag carrier.",
        "airline_name": "Aeromexico",
        "hub": "Mexico City Benito Juarez Airport (MEX)",
        "alliance": "SkyTeam",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs and cats in cabin (weight limits apply). Dogs and cats in cargo hold.",
            "crate_requirements": "In-cabin: soft carrier max 55cm x 35cm x 25cm, pet + carrier under 10kg. Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: carrier + pet under 10kg. Cargo: no fixed limit, confirm by route.",
            "temperature_restrictions": "Live animal temperature embargoes may apply on certain routes and seasons.",
            "brachycephalic_policy": "Restrictions on brachycephalic breeds. Snub-nosed dogs and cats are generally not accepted in cabin. Cargo acceptance varies — confirm with Aeromexico.",
            "cost_range": "In-cabin: varies by route and class. Cargo: contact Aeromexico Cargo for a quote.",
            "booking_process": "In-cabin: add when booking via Aeromexico website or contact centre. Cargo: contact Aeromexico Cargo.",
        },
        "overview": """Aeromexico is Mexico's flag carrier and a SkyTeam member, operating from Mexico City's Benito Juarez Airport (MEX). It connects Mexico to the USA, Canada, Europe, Latin America, and selected Asian destinations.

Small pets can travel in the Aeromexico cabin on qualifying routes. Larger pets travel as cargo. As the primary international carrier out of Mexico, Aeromexico is the most common airline used for pets moving between Mexico and North America, Europe, or Latin America.

Mexico's pet import rules are managed by SENASICA and are relatively straightforward compared to many countries. This page covers Aeromexico's current pet policy — always confirm the latest rules with the airline.""",
        "faqs": [
            {
                "q": "Can I bring my dog in the cabin on Aeromexico?",
                "a": "Small dogs with carrier under 10kg combined can travel in the Aeromexico cabin on qualifying routes. Cabin travel is not available for dogs on all routes — confirm with Aeromexico when booking."
            },
            {
                "q": "Does Aeromexico fly pets between Mexico and Europe?",
                "a": "Aeromexico operates routes between Mexico City and several European destinations including Madrid and Amsterdam. Larger pets travel as cargo on these routes. Confirm live animal acceptance with Aeromexico Cargo for your specific route."
            },
            {
                "q": "What documents does my pet need to fly Aeromexico into Mexico?",
                "a": "Mexico (SENASICA) requires a veterinary health certificate issued within 10 days of travel, microchip, and current vaccination records including rabies. No import permit or titre test is required for most countries."
            },
            {
                "q": "Are brachycephalic breeds accepted on Aeromexico?",
                "a": "Snub-nosed breeds are generally not accepted in the Aeromexico cabin. Cargo acceptance varies by route and conditions. Confirm with Aeromexico before booking a brachycephalic breed."
            },
            {
                "q": "How do I book cargo for my pet on Aeromexico?",
                "a": "Contact Aeromexico Cargo directly. For USA-Mexico pet moves, many owners use the cargo option and book through a US or Mexico-based IPATA-accredited pet transport agent."
            },
        ],
    },
    {
        "slug": "latam-airlines",
        "title": "LATAM Airlines Pet Policy | Pet Transport Global",
        "description": "LATAM Airlines pet transport policy: cabin rules, cargo service, breed restrictions, and what South American pet moves need when flying with LATAM.",
        "airline_name": "LATAM Airlines",
        "hub": "Multiple hubs: Sao Paulo (GRU), Santiago (SCL), Lima (LIM), Bogota (BOG)",
        "alliance": "None (departed Oneworld 2020)",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs and cats in cabin (weight limits apply, vary by country). Dogs and cats in cargo hold.",
            "crate_requirements": "In-cabin: carrier max 45cm x 35cm x 22cm, pet + carrier generally under 10kg (varies by country). Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: varies by country-specific LATAM entity. Confirm for your specific origin-destination pair.",
            "temperature_restrictions": "Temperature embargoes may apply on certain routes. Confirm at time of booking.",
            "brachycephalic_policy": "Restrictions on brachycephalic breeds vary by LATAM country entity. Some flat-faced breeds not accepted in cabin or cargo. Confirm current policy for your breed and route.",
            "cost_range": "In-cabin: varies by route and country entity. Cargo: contact LATAM Cargo for a quote.",
            "booking_process": "In-cabin: book via LATAM website for your specific country. Cargo: contact LATAM Cargo.",
        },
        "overview": """LATAM Airlines Group is South America's largest airline group, operating under the LATAM brand across Brazil, Chile, Colombia, Peru, Ecuador, and Argentina. Its multiple hubs connect South America internally and to North America, Europe, and select long-haul destinations.

LATAM is the most commonly used airline for pet transport within South America and between South America and Europe or the USA. The group is made up of several country-specific entities (LATAM Brasil, LATAM Chile, LATAM Colombia, etc.), and pet policies can vary slightly by entity.

Small pets can travel in the cabin on most LATAM routes within weight and size limits. Larger pets travel as cargo. This page covers the general LATAM policy — always confirm rules for your specific route and country with LATAM directly.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on LATAM?",
                "a": "Yes, for small dogs that meet LATAM's weight limits (typically pet + carrier under 10kg). Rules vary slightly by country entity. Confirm the specific limits for your origin country's LATAM operation."
            },
            {
                "q": "Does LATAM fly pets to Europe from South America?",
                "a": "LATAM operates routes between South America and Europe (Sao Paulo/Santiago to Madrid, Frankfurt, London and others). Larger pets travel as cargo. Confirm live animal cargo acceptance with LATAM Cargo for your specific route."
            },
            {
                "q": "Are brachycephalic breeds accepted on LATAM?",
                "a": "Rules vary by LATAM entity. In general, brachycephalic breeds face restrictions for cabin travel. Cargo acceptance for snub-nosed breeds depends on route and conditions. Always confirm for your specific breed before booking."
            },
            {
                "q": "What documents do pets need to fly within South America on LATAM?",
                "a": "Each South American country has its own requirements. Generally: a veterinary health certificate, microchip, and current vaccination records are required. Some countries require government endorsement. Check the specific destination country's requirements."
            },
            {
                "q": "How do I book pet cargo on LATAM?",
                "a": "Contact LATAM Cargo directly. There are LATAM Cargo offices in Brazil, Chile, Colombia, Peru, and Argentina. For routes between South America and Europe or North America, an IPATA-accredited pet transport agent can help coordinate."
            },
        ],
    },
    {
        "slug": "sas-scandinavian-airlines",
        "title": "SAS Scandinavian Airlines Pet Policy | Pet Transport Global",
        "description": "SAS Scandinavian Airlines pet transport policy: cabin rules for small pets, cargo service, and what pets need to fly with SAS across Scandinavia and internationally.",
        "airline_name": "SAS (Scandinavian Airlines)",
        "hub": "Copenhagen Airport (CPH) / Stockholm Arlanda (ARN) / Oslo Gardermoen (OSL)",
        "alliance": "SkyTeam (from 2024)",
        "cabin_allowed": True,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Small dogs and cats in cabin (weight limits apply). Dogs and cats in cargo hold.",
            "crate_requirements": "In-cabin: carrier max 55cm x 40cm x 23cm, pet + carrier under 8kg. Cargo: IATA-compliant rigid container.",
            "size_limits": "In-cabin: combined weight under 8kg. Cargo: confirm by route.",
            "temperature_restrictions": "Temperature embargoes may apply, particularly in summer and winter extremes on Scandinavian routes.",
            "brachycephalic_policy": "Brachycephalic breeds not accepted in the SAS cabin. Cargo acceptance is subject to route and conditions.",
            "cost_range": "In-cabin: approximately SEK/NOK/DKK equivalent to EUR 50-80. Cargo: contact SAS Cargo.",
            "booking_process": "In-cabin: add when booking ticket via SAS website. Cargo: contact SAS Cargo or use an IPATA agent.",
        },
        "overview": """SAS (Scandinavian Airlines) operates from three hubs across Denmark, Sweden, and Norway, connecting Scandinavia to Europe, North America, and Asia. As the primary carrier for Sweden, Norway, and Denmark, SAS is the natural choice for pets moving between Scandinavia and the rest of the world.

SAS joined SkyTeam in 2024 after emerging from bankruptcy restructuring. Small pets can travel in the SAS cabin within weight limits. Larger pets travel as cargo. All three Scandinavian countries are EU members (Denmark, Sweden) or EEA members (Norway), which affects documentation requirements.

This page covers SAS's current pet policy. Always verify with SAS before booking.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on SAS?",
                "a": "Small dogs (carrier + dog under 8kg, carrier fitting within SAS dimensions) can travel in the SAS cabin. One pet per passenger. A health certificate is required. Book in advance as cabin pet spots are limited."
            },
            {
                "q": "Does SAS fly pets to the USA from Scandinavia?",
                "a": "SAS operates routes between Copenhagen/Stockholm/Oslo and multiple US cities. Larger pets travel as cargo. Under the 2024 CDC rules, dogs from Scandinavian countries need a microchip implanted before or on the same date as their rabies vaccination, plus a USDA health certificate."
            },
            {
                "q": "What do pets need to travel with SAS within Scandinavia?",
                "a": "All three Scandinavian countries (Denmark, Sweden, Norway) have slightly different EU/EEA status. Within the EU (Denmark, Sweden), EU pet passports apply. Norway as an EEA member follows similar rules but is technically not an EU member — confirm documentation requirements with SAS for Norway-specific routes."
            },
            {
                "q": "Are brachycephalic breeds accepted on SAS?",
                "a": "SAS does not accept brachycephalic breeds in the passenger cabin. Cargo acceptance varies by route and conditions — confirm with SAS Cargo before booking a flat-faced breed."
            },
            {
                "q": "How do I book cargo for my pet on SAS?",
                "a": "Contact SAS Cargo directly. For complex international routes, work with an IPATA-accredited pet transport agent familiar with Scandinavian regulations."
            },
        ],
    },
    {
        "slug": "royal-jordanian",
        "title": "Royal Jordanian Pet Policy | Pet Transport Global",
        "description": "Royal Jordanian pet transport policy: cargo service, breed restrictions, and what pets need to fly with Jordan's national carrier for Middle East and international routes.",
        "airline_name": "Royal Jordanian",
        "hub": "Queen Alia International Airport, Amman (AMM)",
        "alliance": "Oneworld",
        "cabin_allowed": False,
        "cargo_allowed": True,
        "cargo_suspended": False,
        "policy": {
            "accepted_animals": "Dogs and cats in cargo hold. Pets generally not accepted in the passenger cabin.",
            "crate_requirements": "IATA-compliant rigid container. Pet must be able to stand, sit upright, lie down, and turn around.",
            "size_limits": "Confirm by route and aircraft with Royal Jordanian Cargo.",
            "temperature_restrictions": "Jordan experiences extreme summer heat. Live animal embargoes may apply during peak summer. Confirm at time of booking.",
            "brachycephalic_policy": "Restrictions on brachycephalic breeds follow industry guidance. Confirm acceptance of flat-faced breeds with Royal Jordanian before booking.",
            "cost_range": "Varies by route, weight, and crate dimensions. Contact Royal Jordanian Cargo for a quote.",
            "booking_process": "Contact Royal Jordanian Cargo or use an IPATA-accredited pet transport agent.",
        },
        "overview": """Royal Jordanian is Jordan's flag carrier and a Oneworld member, operating from Amman's Queen Alia International Airport (AMM). It connects Jordan to the UK, Europe, the USA, and destinations across the Middle East, Africa, and Asia.

Amman is an important hub for pets moving between the UK/Europe and the Levant region (Jordan, Lebanon, Israel/Palestine area). Jordan is a popular destination for expats in the NGO, diplomatic, and business sectors who often relocate with pets.

Pets travel in the cargo hold on Royal Jordanian. This page covers the current policy — always confirm with Royal Jordanian directly before booking.""",
        "faqs": [
            {
                "q": "Can I take my dog in the cabin on Royal Jordanian?",
                "a": "Royal Jordanian generally does not accept pets in the passenger cabin. Dogs and cats travel as cargo."
            },
            {
                "q": "What do pets need to enter Jordan on Royal Jordanian?",
                "a": "Jordan requires a veterinary health certificate, microchip, valid rabies vaccination, and confirmation that the animal is free from signs of disease. An import permit from the Jordanian Ministry of Agriculture is required in advance. Confirm current requirements with the Ministry and Royal Jordanian Cargo."
            },
            {
                "q": "Are there temperature embargoes on Royal Jordanian for pets?",
                "a": "Jordan has hot summers, and live animal embargoes may apply during peak heat months. Routes transiting through Amman are also affected. Confirm temperature restrictions at the time of booking."
            },
            {
                "q": "Does Royal Jordanian accept brachycephalic breeds?",
                "a": "Restrictions on flat-faced breeds apply following industry guidance. Confirm acceptance of brachycephalic breeds with Royal Jordanian Cargo before booking."
            },
            {
                "q": "How do I book cargo for my pet on Royal Jordanian?",
                "a": "Contact Royal Jordanian Cargo directly, or work with an IPATA-accredited pet transport agent familiar with Jordan and the Middle East region."
            },
        ],
    },
]

def make_faqs_yaml(faqs):
    lines = []
    for faq in faqs:
        q = faq["q"].replace('"', '\\"')
        a = faq["a"].replace('"', '\\"')
        lines.append(f'  - question: "{q}"\n    answer: "{a}"')
    return "\n".join(lines)

def write_airline(airline):
    filepath = os.path.join(AIRLINES_DIR, airline["slug"] + ".md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {airline['slug']}")
        return

    p = airline["policy"]
    faqs_yaml = make_faqs_yaml(airline["faqs"])

    cabin_str = "true" if airline["cabin_allowed"] else "false"
    cargo_str = "true" if airline["cargo_allowed"] else "false"
    suspended_str = "true" if airline["cargo_suspended"] else "false"

    frontmatter = f"""---
title: "{airline['title']}"
description: "{airline['description']}"
type: "airlines"
layout: "single"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{airline['slug']}"
airline_name: "{airline['airline_name']}"
hub: "{airline['hub']}"
alliance: "{airline['alliance']}"
cabin_allowed: {cabin_str}
cargo_allowed: {cargo_str}
cargo_suspended: {suspended_str}
policy:
  accepted_animals: "{p['accepted_animals']}"
  crate_requirements: "{p['crate_requirements']}"
  size_limits: "{p['size_limits']}"
  temperature_restrictions: "{p['temperature_restrictions']}"
  brachycephalic_policy: "{p['brachycephalic_policy']}"
  cost_range: "{p['cost_range']}"
  booking_process: "{p['booking_process']}"
content:
  h1: "{airline['airline_name']} Pet Transport Policy"
  overview: |
    {chr(10).join('    ' + line for line in airline['overview'].strip().split(chr(10)))}
faqs:
{faqs_yaml}
---

## {airline['airline_name']} Pet Transport Policy

{airline['overview'].strip()}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
    print(f"WROTE: {airline['slug']}")

for airline in AIRLINES:
    write_airline(airline)

print(f"\nDone. {len(AIRLINES)} airlines processed.")
