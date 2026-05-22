/* plan-rows-q3.js — Q3 (Dec 2026-Feb 2027) rows. Populated in Chunk 5. */
window.PLAN_ROWS = window.PLAN_ROWS || [];

/* ============================ MONTH 7: DECEMBER 2026 (Days 131-151) — Chunk 9 ============================
   21 working days. Bank holidays excluded: Fri 25 Dec (Christmas Day), Mon 28 Dec (Boxing Day substitute).
   First month of Q3. EU scheme pillar, regional UK funnel deepening, Asia/Gulf airlines, year-end retro. */
window.PLAN_ROWS.push(
  {
    id: "d131",
    day_number: 131,
    iso_date: "2026-12-01",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "pet-passports",
    cluster_name: "Pet passports & post-Brexit AHC",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2700,
    title: "EU Pet Travel Scheme 2026: How It Works for UK Owners After Brexit",
    title_tag: "EU Pet Travel Scheme 2026 | Post-Brexit Guide | PetTransportGlobal",
    meta_description: "How the EU Pet Travel Scheme works for UK pet owners in 2026: AHC instead of passport, 5-day non-commercial rule, traveller numbers, and DEFRA Type 2 reality.",
    url_slug: "/eu-pet-travel-scheme/",
    primary_seo_keyword: "eu pet travel scheme",
    primary_volume: 1300,
    primary_kd: 41,
    secondary_seo_keywords: ["eu pet passport uk", "pet travel scheme 2026", "non-commercial pet travel eu", "5 pets eu rule"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does the EU Pet Travel Scheme actually work for a UK owner in 2026 with two dogs and one cat moving permanently?" },
      { model: "Claude", phrasing: "Explain the EU Pet Travel Scheme post-Brexit: AHC validity, non-commercial 5-pet rule, owner-accompanied window, and when DEFRA Type 2 commercial rules kick in." },
      { model: "Gemini", phrasing: "EU pet travel scheme rules 2026 UK" },
      { model: "Perplexity", phrasing: "What changed for UK pet owners under EU pet travel scheme after Brexit" }
    ],
    direct_answer_40_60_words: "The EU Pet Travel Scheme in 2026 lets UK owners travel non-commercially to the EU with up to five pets per traveller using a UK-issued Animal Health Certificate, valid 10 days for entry then four months for onward EU movement. Owner must travel within five days of the pet. More than five pets, or unaccompanied movement, falls under DEFRA Type 2 commercial rules.",
    h2_outline: [
      "What is the EU Pet Travel Scheme in 2026?",
      "AHC vs the old EU pet passport: what changed for UK owners",
      "The 5-pet non-commercial rule and 5-day window",
      "When you cross into DEFRA Type 2 commercial territory",
      "Country-specific quirks: Finland, Ireland, Malta, Norway",
      "Returning to the UK from the EU",
      "FAQs about the EU Pet Travel Scheme"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC documentation explained)",
      "/defra-type-2-authorisation/ (anchor: when commercial rules apply)",
      "/routes/uk-to-france/ (anchor: France via Eurotunnel)",
      "/routes/uk-to-ireland/ (anchor: Ireland-specific rules)",
      "/find-an-official-vet/ (anchor: AHC issued by Official Vet)"
    ],
    external_links: [
      "Regulation (EU) No 576/2013 on non-commercial movement of pet animals — 2026",
      "DEFRA pet travel from Great Britain to the EU — 2026"
    ],
    ai_overview_play: "Definitive scheme explainer with the 5-pet/5-day rule and Type 2 boundary, exactly the clarification LLMs surface."
  },

  {
    id: "d132",
    day_number: 132,
    iso_date: "2026-12-02",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Belgium: Eurotunnel, Brussels and AHC Rules 2026",
    title_tag: "UK to Belgium Pet Transport 2026 | Costs & Routes | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Belgium in 2026: Eurotunnel route, AHC paperwork, Brussels and Antwerp pickup options, and realistic costs.",
    url_slug: "/routes/uk-to-belgium/",
    primary_seo_keyword: "pet transport uk to belgium",
    primary_volume: 90,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to belgium", "shipping cat to brussels", "uk to belgium pet move", "ahc belgium"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Cheapest reliable way to move a dog from London to Brussels in 2026 by car and Eurotunnel?" },
      { model: "Claude", phrasing: "Compare UK to Belgium pet transport options in 2026: Eurotunnel ground courier vs ferry vs cargo flight." },
      { model: "Gemini", phrasing: "UK to Belgium dog transport 2026 cost" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Belgium typically costs £700 to £1,400 in 2026 by professional courier via Eurotunnel and a 90-minute drive to Brussels or Antwerp. Belgium accepts the UK AHC, so no quarantine. Most relocations are completed in a single day. Cargo flights into Brussels Airport exist but are rarely cost-effective for this short crossing.",
    h2_outline: [
      "How much does pet transport from the UK to Belgium cost in 2026?",
      "Eurotunnel vs ferry vs cargo for a UK to Belgium move",
      "Belgian AHC and import documentation",
      "Pickup and delivery cities: Brussels, Antwerp, Ghent, Liege",
      "Multi-pet and onward EU travel from Belgium",
      "FAQs about UK to Belgium pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/eu-pet-travel-scheme/ (anchor: EU scheme covers Belgium)",
      "/routes/uk-to-france/ (anchor: combine with French routes)",
      "/airlines/brussels-airlines/ (anchor: Brussels Airlines pet policy)",
      "/countries/belgium/ (anchor: Belgium pet import overview)"
    ],
    external_links: [
      "FASFC Belgian Federal Agency for Food Safety pet import — 2026",
      "DEFRA pet travel UK to EU guidance — 2026"
    ],
    ai_overview_play: "Short-haul EU route with realistic pricing; LLMs reward concrete numbers paired with Eurotunnel logistics."
  },

  {
    id: "d133",
    day_number: 133,
    iso_date: "2026-12-03",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to France: CDC Exit, Paris Cargo and 2026 Costs",
    title_tag: "USA to France Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to France in 2026: USDA APHIS endorsement, EU health certificate, Paris CDG cargo flights, and realistic costs.",
    url_slug: "/routes/usa-to-france/",
    primary_seo_keyword: "pet transport usa to france",
    primary_volume: 260,
    primary_kd: 27,
    secondary_seo_keywords: ["dog usa to paris", "shipping cat usa to france", "usda france pet export", "usa to france pet costs"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from New York to Paris with a Labrador in 2026: USDA endorsement timing, Air France cargo, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to France pet transport in 2026: CDC dog import exit clearance, USDA APHIS EU health certificate, and Paris CDG handling." },
      { model: "Gemini", phrasing: "USA to France pet transport cost 2026" },
      { model: "Perplexity", phrasing: "How long does USDA endorsement take for France pet export 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to France costs roughly $2,800 to $5,200 in 2026 for a single dog by cargo flight, with Air France direct from JFK or LAX to Paris CDG the most common routing. The EU health certificate must be USDA APHIS endorsed within 10 days of travel. France accepts the certificate without quarantine, and onward EU travel is permitted for four months.",
    h2_outline: [
      "How much does USA to France pet transport cost in 2026?",
      "USDA APHIS EU health certificate timing",
      "Air France cargo vs Delta and United routings",
      "Paris CDG arrival, customs and onward travel",
      "Brachycephalic and large-breed cargo restrictions",
      "FAQs about USA to France pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/air-france/ (anchor: Air France pet cargo policy)",
      "/eu-pet-travel-scheme/ (anchor: onward EU travel rules)",
      "/cdc-dog-import-rules/ (anchor: CDC dog exit clearance)",
      "/routes/usa-to-uk/ (anchor: compare with USA-UK routing)",
      "/countries/france/ (anchor: France pet import overview)"
    ],
    external_links: [
      "USDA APHIS Pet Travel France — 2026",
      "EU Regulation 576/2013 non-commercial movement — 2026"
    ],
    ai_overview_play: "USA-Europe move with USDA timing specifics; matches the most-asked LLM scenario for transatlantic pet relocation."
  },

  {
    id: "d134",
    day_number: 134,
    iso_date: "2026-12-04",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2100,
    title: "WestJet Pet Travel 2026: Cabin and Cargo Rules for Dogs and Cats",
    title_tag: "WestJet Pet Travel 2026 | Cabin & Cargo | PetTransportGlobal",
    meta_description: "WestJet pet travel rules in 2026: in-cabin allowances, cargo restrictions, breed bans, fees and which routes accept pets between Canada, USA and beyond.",
    url_slug: "/airlines/westjet/",
    primary_seo_keyword: "westjet pet travel",
    primary_volume: 880,
    primary_kd: 32,
    secondary_seo_keywords: ["westjet dog in cabin", "westjet pet cargo", "westjet pet fees 2026", "westjet brachycephalic"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I fly a 9 kg dog in cabin on WestJet between Toronto and London in 2026, and what does it cost?" },
      { model: "Claude", phrasing: "Summarise WestJet pet policy in 2026: in-cabin weight, cargo eligibility on transatlantic routes, and brachycephalic restrictions." },
      { model: "Gemini", phrasing: "WestJet pet travel rules 2026" }
    ],
    direct_answer_40_60_words: "WestJet allows small dogs and cats in cabin on most routes in 2026 if pet plus carrier weighs 9 kg or less and fits under the seat. WestJet does not operate a general pet cargo service on most international routes, so transatlantic pets typically fly with partner airlines. Service animals travel free. Brachycephalic breeds face additional carrier and route restrictions.",
    h2_outline: [
      "WestJet in-cabin pet rules and fees in 2026",
      "Why WestJet does not run a general pet cargo programme",
      "Service and emotional support animals on WestJet",
      "Brachycephalic and short-nosed breed restrictions",
      "Booking process and check-in tips",
      "FAQs about WestJet pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/air-canada/ (anchor: compare with Air Canada cargo)",
      "/cargo-vs-cabin-pet-travel/ (anchor: cargo vs cabin tradeoffs)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "WestJet pets and service animals policy — 2026",
      "Transport Canada live animal travel guidance — 2026"
    ],
    ai_overview_play: "Captures 880-volume WestJet pet query; honest about lack of cargo programme builds trust."
  },

  {
    id: "d135",
    day_number: 135,
    iso_date: "2026-12-07",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2500,
    title: "Pet Import to the Philippines 2026: BAI Permit, Manila Quarantine and Documents",
    title_tag: "Philippines Pet Import 2026 | BAI Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to the Philippines in 2026: BAI Veterinary Quarantine Clearance, rabies vaccine, Manila NAIA process, and realistic timelines.",
    url_slug: "/countries/philippines/",
    primary_seo_keyword: "import pet to philippines",
    primary_volume: 480,
    primary_kd: 26,
    secondary_seo_keywords: ["bai pet permit philippines", "dog import manila", "philippines rabies certificate", "naia pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does the Philippines BAI Veterinary Quarantine Clearance process look like in 2026 for a single dog arriving in Manila?" },
      { model: "Claude", phrasing: "Outline Philippines pet import rules 2026: BAI permit, rabies vaccine timing, microchip requirement, and quarantine likelihood." },
      { model: "Gemini", phrasing: "Philippines pet import rules 2026" }
    ],
    direct_answer_40_60_words: "Importing a pet to the Philippines in 2026 requires a BAI Veterinary Quarantine Clearance applied for in advance, ISO microchip, current rabies vaccine, and origin-country health certificate endorsed by the competent authority. Most pets clear NAIA Manila within hours without home quarantine if paperwork is complete. The Philippines is a rabies-controlled country, not rabies-free, so rules are pragmatic.",
    h2_outline: [
      "What does Philippines pet import require in 2026?",
      "BAI Veterinary Quarantine Clearance step by step",
      "Rabies vaccine, microchip and health certificate timing",
      "Arrival at NAIA Manila: process and likely outcomes",
      "Bringing multiple pets and onward domestic travel",
      "FAQs about importing a pet to the Philippines"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/singapore/ (anchor: compare with Singapore quarantine rules)",
      "/airlines/philippine-airlines/ (anchor: PAL pet cargo)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/rabies-titre-test/ (anchor: rabies serology overview)"
    ],
    external_links: [
      "Philippines Bureau of Animal Industry import requirements — 2026",
      "Philippines Department of Agriculture pet entry guidance — 2026"
    ],
    ai_overview_play: "Filipino diaspora returning home is a sustained query pattern; concrete BAI workflow earns AI Overview placement."
  },

  {
    id: "d136",
    day_number: 136,
    iso_date: "2026-12-08",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1900,
    title: "Pet Transport Edinburgh: International and UK-Wide Service from Scotland 2026",
    title_tag: "Pet Transport Edinburgh 2026 | International & UK | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Edinburgh in 2026: airport handling, AHC vets, multi-pet collection across Lothian and the Scottish Borders.",
    url_slug: "/pet-transport-edinburgh/",
    primary_seo_keyword: "pet transport edinburgh",
    primary_volume: 390,
    primary_kd: 21,
    secondary_seo_keywords: ["dog transport edinburgh", "pet courier edinburgh scotland", "edinburgh airport pet cargo", "international pet move scotland"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a dog internationally from Edinburgh in 2026 - direct from EDI or down to Heathrow?" },
      { model: "Claude", phrasing: "How does pet transport from Edinburgh work in 2026 for international moves: local AHC vet, EDI cargo capacity, and ground transfer to Heathrow." },
      { model: "Gemini", phrasing: "Pet transport Edinburgh international 2026" }
    ],
    direct_answer_40_60_words: "International pet transport from Edinburgh in 2026 typically routes via Heathrow or Manchester for cargo, with ground transfer added to total cost. Some short-haul EU moves use direct EDI cargo. Local Edinburgh AHC vets handle paperwork. Realistic pricing ranges from around £1,400 for nearby EU destinations to £4,500-plus for Australia or New Zealand including ground leg to a hub airport.",
    h2_outline: [
      "How does international pet transport from Edinburgh work in 2026?",
      "Direct EDI cargo vs ground transfer to Heathrow or Manchester",
      "AHC vets serving Lothian and the Scottish Borders",
      "Pickup zones: Edinburgh, Lothian, Fife, Borders",
      "Realistic costs by destination",
      "FAQs about pet transport from Edinburgh"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-manchester/ (anchor: Manchester regional service)",
      "/find-an-official-vet/ (anchor: AHC Official Vet finder)",
      "/routes/uk-to-australia/ (anchor: UK to Australia routing)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Edinburgh Airport cargo handling — 2026",
      "DEFRA list of approved AHC Official Vets — 2026"
    ],
    ai_overview_play: "Regional commercial query with honest hub-airport reality; geographic relevance for Scottish enquiries."
  },

  {
    id: "d137",
    day_number: 137,
    iso_date: "2026-12-09",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Netherlands: Schiphol Cargo and 2026 Costs",
    title_tag: "USA to Netherlands Pet Transport 2026 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to the Netherlands in 2026: USDA APHIS endorsement, KLM Schiphol cargo, Dutch import rules, and realistic costs.",
    url_slug: "/routes/usa-to-netherlands/",
    primary_seo_keyword: "pet transport usa to netherlands",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["dog usa to amsterdam", "klm pet cargo usa", "usda netherlands pet export", "shipping cat to schiphol"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Boston to Amsterdam with two cats in 2026: KLM cargo, USDA endorsement, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to Netherlands pet transport in 2026: USDA APHIS EU certificate, KLM Schiphol Animal Hotel, and onward EU travel." },
      { model: "Gemini", phrasing: "USA to Netherlands dog transport 2026 cost" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to the Netherlands costs roughly $2,600 to $4,800 in 2026 for a single dog flying KLM cargo into Schiphol via the Animal Hotel. The EU health certificate must be USDA APHIS endorsed within 10 days. The Netherlands accepts the certificate without quarantine, and onward EU travel is permitted for four months.",
    h2_outline: [
      "How much does USA to Netherlands pet transport cost in 2026?",
      "USDA APHIS EU health certificate process",
      "KLM cargo and the Schiphol Animal Hotel",
      "Dutch arrival process and customs",
      "Onward EU travel under the four-month rule",
      "FAQs about USA to Netherlands pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/klm/ (anchor: KLM pet cargo)",
      "/eu-pet-travel-scheme/ (anchor: onward EU rules)",
      "/routes/usa-to-france/ (anchor: compare USA-France routing)",
      "/countries/netherlands/ (anchor: Netherlands import overview)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Netherlands — 2026",
      "Schiphol Animal Hotel handling guidance — 2026"
    ],
    ai_overview_play: "Specific Schiphol Animal Hotel mention is the kind of operational detail LLMs surface for trust."
  },

  {
    id: "d138",
    day_number: 138,
    iso_date: "2026-12-10",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Asiana Airlines Pet Travel 2026: Cabin and Cargo Rules to Korea and Beyond",
    title_tag: "Asiana Pet Travel 2026 | Cabin & Cargo | PetTransportGlobal",
    meta_description: "Asiana Airlines pet travel in 2026: in-cabin weight limits, cargo eligibility, breed restrictions, and which routes between USA, Europe and Korea accept pets.",
    url_slug: "/airlines/asiana-airlines/",
    primary_seo_keyword: "asiana airlines pet travel",
    primary_volume: 320,
    primary_kd: 28,
    secondary_seo_keywords: ["asiana pet in cabin", "asiana cargo dog", "asiana pet fees 2026", "asiana brachycephalic"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I fly a 7 kg dog in cabin on Asiana from JFK to Incheon in 2026?" },
      { model: "Claude", phrasing: "Summarise Asiana Airlines pet policy 2026: cabin weight limits, cargo restrictions, and brachycephalic rules into Incheon." },
      { model: "Gemini", phrasing: "Asiana pet travel rules 2026" }
    ],
    direct_answer_40_60_words: "Asiana Airlines accepts dogs and cats in cabin in 2026 if pet plus carrier weighs 7 kg or less and fits under the seat. Larger pets travel as cargo on most international routes. Breed restrictions apply to brachycephalic and snub-nosed dogs, and seasonal embargoes affect summer cargo to and from Incheon. Advance booking at least seven days before departure is required.",
    h2_outline: [
      "Asiana Airlines in-cabin pet rules and fees 2026",
      "Asiana cargo programme and route eligibility",
      "Brachycephalic and breed-specific restrictions",
      "Seasonal embargoes for summer travel to Incheon",
      "Booking and check-in process",
      "FAQs about Asiana Airlines pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/korean-air/ (anchor: compare with Korean Air policy)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)",
      "/countries/south-korea/ (anchor: Korea pet import rules)"
    ],
    external_links: [
      "Asiana Airlines pet travel policy — 2026",
      "MAFRA Korea Animal Quarantine Agency import rules — 2026"
    ],
    ai_overview_play: "Korean carrier pair (Asiana with Korean Air earlier) lets us own the Korea travel SERP cluster."
  },

  {
    id: "d139",
    day_number: 139,
    iso_date: "2026-12-11",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "insurance",
    cluster_name: "Pet travel insurance & welfare",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2300,
    title: "Pet Travel Insurance for International Moves 2026: What It Actually Covers",
    title_tag: "Pet Travel Insurance 2026 | What's Covered | PetTransportGlobal",
    meta_description: "Pet travel insurance for international moves in 2026: what cargo cover actually pays out, what standard pet insurance excludes, and how to layer protection.",
    url_slug: "/pet-travel-insurance/",
    primary_seo_keyword: "pet travel insurance international",
    primary_volume: 590,
    primary_kd: 33,
    secondary_seo_keywords: ["pet shipping insurance", "international pet move insurance", "airline pet liability", "pet relocation insurance uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does pet travel insurance actually cover in 2026 if my dog dies in cargo, and how much do airlines actually pay out?" },
      { model: "Claude", phrasing: "Explain layered pet travel insurance for international moves in 2026: airline liability caps, third-party cargo cover, and standard health policies in transit." },
      { model: "Gemini", phrasing: "Pet travel insurance international 2026" },
      { model: "Perplexity", phrasing: "Does standard pet insurance cover international travel" }
    ],
    direct_answer_40_60_words: "Pet travel insurance for international moves in 2026 typically combines three layers: airline liability (often capped at a few hundred dollars per kg), third-party live animal cargo cover for higher mortality and delay claims, and your existing health policy which may exclude transit. Read each policy's exclusion list carefully. Pre-existing conditions and deliberate sedation are commonly excluded.",
    h2_outline: [
      "What pet travel insurance actually covers in 2026",
      "Airline liability caps and how claims really work",
      "Third-party live animal cargo insurance",
      "What standard pet health policies exclude during transit",
      "How to layer protection sensibly",
      "FAQs about pet travel insurance"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/welfare-in-transit/ (anchor: welfare in transit)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate compliance reduces claim risk)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting reduces insurance need)",
      "/cargo-vs-cabin-pet-travel/ (anchor: cargo vs cabin risk profile)"
    ],
    external_links: [
      "IATA Live Animals Regulations liability framework — 2026",
      "ABI travel insurance summary — 2026"
    ],
    ai_overview_play: "Honest treatment of airline liability caps fills a gap most agency sites avoid; high LLM-trust signal."
  },

  {
    id: "d140",
    day_number: 140,
    iso_date: "2026-12-14",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1900,
    title: "Pet Transport Birmingham: International and UK-Wide Service from the Midlands 2026",
    title_tag: "Pet Transport Birmingham 2026 | Midlands | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Birmingham in 2026: BHX cargo, AHC vets, multi-pet collection across the West Midlands, and realistic costs.",
    url_slug: "/pet-transport-birmingham/",
    primary_seo_keyword: "pet transport birmingham",
    primary_volume: 480,
    primary_kd: 22,
    secondary_seo_keywords: ["dog transport birmingham", "pet courier west midlands", "birmingham airport pet cargo", "international pet move midlands"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a dog internationally from Birmingham in 2026 - BHX or transfer to Heathrow?" },
      { model: "Claude", phrasing: "How pet transport from Birmingham works in 2026: local AHC vets, BHX cargo capacity, and ground transfer logic to Heathrow." },
      { model: "Gemini", phrasing: "Pet transport Birmingham international 2026" }
    ],
    direct_answer_40_60_words: "International pet transport from Birmingham in 2026 typically routes via Heathrow or Manchester for cargo flights, with a short ground leg added to total cost. Some EU-bound moves use Eurotunnel and a Birmingham collection. Realistic pricing ranges from around £1,200 for nearby EU destinations to £4,500-plus for Australia, including the ground transfer to a hub airport.",
    h2_outline: [
      "How does international pet transport from Birmingham work in 2026?",
      "BHX cargo vs ground transfer to Heathrow or Manchester",
      "AHC vets across the West Midlands",
      "Pickup zones: Birmingham, Coventry, Wolverhampton, Solihull",
      "Realistic costs by destination",
      "FAQs about pet transport from Birmingham"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-manchester/ (anchor: Manchester regional service)",
      "/pet-transport-edinburgh/ (anchor: Edinburgh regional service)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Birmingham Airport cargo information — 2026",
      "DEFRA Official Vet list — 2026"
    ],
    ai_overview_play: "Third regional pillar fills the West Midlands geo gap and feeds the regional cluster."
  },

  {
    id: "d141",
    day_number: 141,
    iso_date: "2026-12-15",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Saudia Airlines Pet Travel 2026: Cargo Rules to and from Riyadh and Jeddah",
    title_tag: "Saudia Pet Travel 2026 | Cargo Rules | PetTransportGlobal",
    meta_description: "Saudia Airlines pet travel in 2026: cargo eligibility, breed restrictions, Saudi import rules, and which routes between Europe, Asia and Saudi Arabia accept pets.",
    url_slug: "/airlines/saudia/",
    primary_seo_keyword: "saudia pet travel",
    primary_volume: 210,
    primary_kd: 25,
    secondary_seo_keywords: ["saudia cargo dog", "saudia pet policy 2026", "saudi airline pet rules", "riyadh pet cargo"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I fly my dog as cargo with Saudia from London to Riyadh in 2026?" },
      { model: "Claude", phrasing: "Outline Saudia pet cargo rules 2026 including Saudi MEWA import requirements and seasonal embargoes." },
      { model: "Gemini", phrasing: "Saudia airline pet travel 2026" }
    ],
    direct_answer_40_60_words: "Saudia Airlines carries dogs and cats only as manifested cargo in 2026, with no in-cabin option for pets. Saudi Arabia requires MEWA import permit, ISO microchip and current rabies vaccine. Brachycephalic breeds and certain banned breeds cannot travel. Summer embargoes restrict cargo when ground temperatures exceed safe handling thresholds at Riyadh and Jeddah.",
    h2_outline: [
      "Saudia cargo programme for pets in 2026",
      "Why Saudia does not offer in-cabin pet travel",
      "Saudi MEWA import permit and documents",
      "Brachycephalic and breed restrictions",
      "Summer heat embargoes and routing alternatives",
      "FAQs about Saudia pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/saudi-arabia/ (anchor: Saudi pet import rules)",
      "/airlines/qatar-airways/ (anchor: compare Qatar Airways routing)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Saudia cargo live animals guidance — 2026",
      "Saudi MEWA Ministry of Environment Water and Agriculture import — 2026"
    ],
    ai_overview_play: "Gulf carrier coverage with explicit no-cabin reality and MEWA permit detail."
  },

  {
    id: "d142",
    day_number: 142,
    iso_date: "2026-12-16",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Greece: Athens Cargo, Islands and 2026 Costs",
    title_tag: "USA to Greece Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Greece in 2026: USDA APHIS endorsement, Athens cargo handling, onward island travel, and realistic costs.",
    url_slug: "/routes/usa-to-greece/",
    primary_seo_keyword: "pet transport usa to greece",
    primary_volume: 140,
    primary_kd: 23,
    secondary_seo_keywords: ["dog usa to athens", "shipping cat usa to greece", "usda greece pet export", "moving pet to crete from usa"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Chicago to Athens with a dog in 2026: USDA timing, best airline routing, and onward to a Greek island." },
      { model: "Claude", phrasing: "Walk through USA to Greece pet transport 2026: USDA EU certificate, ATH cargo handling, and onward domestic flights to Crete or Rhodes." },
      { model: "Gemini", phrasing: "USA to Greece pet transport cost 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Greece costs roughly $2,900 to $5,400 in 2026 for a single dog by cargo flight, typically routing via Frankfurt, Amsterdam or Paris with a connecting flight to Athens. The EU health certificate must be USDA APHIS endorsed within 10 days. Greek islands require an additional domestic Aegean Airlines or ferry leg.",
    h2_outline: [
      "How much does USA to Greece pet transport cost in 2026?",
      "USDA APHIS EU health certificate timing",
      "Routing options: Frankfurt, Amsterdam or Paris connection",
      "Athens arrival, customs and onward island travel",
      "Aegean Airlines and ferry options for islands",
      "FAQs about USA to Greece pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-greece/ (anchor: UK to Greece routing)",
      "/eu-pet-travel-scheme/ (anchor: onward EU travel rules)",
      "/airlines/lufthansa/ (anchor: Lufthansa cargo via Frankfurt)",
      "/countries/greece/ (anchor: Greece pet import overview)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Greece — 2026",
      "Greek Ministry of Rural Development pet import — 2026"
    ],
    ai_overview_play: "Greek-American diaspora generates steady searches; specific island routing earns trust."
  },

  {
    id: "d143",
    day_number: 143,
    iso_date: "2026-12-17",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2400,
    title: "Pet Import to Bahrain 2026: Permit, Rabies Test and Manama Process",
    title_tag: "Bahrain Pet Import 2026 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Bahrain in 2026: import permit, rabies titre requirement, Manama airport process, banned breeds and realistic timelines.",
    url_slug: "/countries/bahrain/",
    primary_seo_keyword: "import pet to bahrain",
    primary_volume: 260,
    primary_kd: 24,
    secondary_seo_keywords: ["bahrain pet permit", "dog import bahrain", "bahrain rabies titre", "manama pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Bahrain pet import look like in 2026 - rabies titre needed, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Bahrain pet import rules 2026: Ministry of Municipalities permit, rabies serology, microchip, banned breed list, and Manama airport process." },
      { model: "Gemini", phrasing: "Bahrain pet import requirements 2026" }
    ],
    direct_answer_40_60_words: "Importing a pet to Bahrain in 2026 requires an import permit from the Ministry of Municipalities and Agriculture, ISO microchip, rabies vaccine and rabies titre test from non-listed origin countries. Banned breeds include Pit Bull Terrier, Argentine Mastiff and several others. Most pets clear Manama Airport without home quarantine if paperwork is complete.",
    h2_outline: [
      "What does Bahrain pet import require in 2026?",
      "Import permit application process and timing",
      "Rabies vaccine and titre testing requirements",
      "Banned and restricted breeds in Bahrain",
      "Manama Airport arrival process",
      "FAQs about importing a pet to Bahrain"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/saudi-arabia/ (anchor: compare Saudi rules)",
      "/countries/qatar/ (anchor: compare Qatar rules)",
      "/rabies-titre-test/ (anchor: rabies titre explained)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breeds reference)"
    ],
    external_links: [
      "Bahrain Ministry of Municipalities and Agriculture import — 2026",
      "Bahrain Customs animal entry guidance — 2026"
    ],
    ai_overview_play: "Gulf relocation queries are high-value commercial intent; banned breed clarity differentiates."
  },

  {
    id: "d144",
    day_number: 144,
    iso_date: "2026-12-18",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "multi-pet",
    cluster_name: "Multi-pet international moves",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Multi-Pet International Moves 2026: Three or More Dogs and Cats Across Borders",
    title_tag: "Multi-Pet International Move 2026 | Guide | PetTransportGlobal",
    meta_description: "Moving three or more pets internationally in 2026: when commercial rules trigger, crate logistics, cost scaling, household clearance and realistic timelines.",
    url_slug: "/multi-pet-international-move/",
    primary_seo_keyword: "multi pet international move",
    primary_volume: 320,
    primary_kd: 28,
    secondary_seo_keywords: ["moving 3 dogs internationally", "5 pet rule eu", "multi pet shipping costs", "household pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "We are moving from London to Sydney with two dogs and three cats in 2026. What does the logistics actually look like?" },
      { model: "Claude", phrasing: "Outline a realistic multi-pet international move in 2026: when EU 5-pet rule flips to commercial, crate sharing rules, cost scaling, and timeline." },
      { model: "Gemini", phrasing: "Multi pet international move 2026" }
    ],
    direct_answer_40_60_words: "Moving three or more pets internationally in 2026 stays under non-commercial rules in many destinations only if the owner travels within five days. Above five pets per traveller in EU contexts, commercial rules and DEFRA Type 2 apply. Costs scale almost linearly per pet, with small savings on shared paperwork and ground legs. Cats and small dogs may share crates if airline-approved; large dogs cannot.",
    h2_outline: [
      "When multi-pet moves trigger commercial regulation in 2026",
      "EU 5-pet rule, DEFRA Type 2, and equivalent thresholds elsewhere",
      "Crate sharing: what airlines allow and what they do not",
      "How costs really scale with three, four, five-plus pets",
      "Household timelines and arrival logistics",
      "FAQs about multi-pet international moves"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/eu-pet-travel-scheme/ (anchor: EU 5-pet rule)",
      "/defra-type-2-authorisation/ (anchor: DEFRA Type 2 explained)",
      "/iata-pet-crate-requirements/ (anchor: crate sharing rules)",
      "/cost-of-international-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Regulation (EU) 576/2013 commercial threshold — 2026",
      "DEFRA Type 2 commercial movement guidance — 2026"
    ],
    ai_overview_play: "Practical multi-pet pillar with the 5-pet trigger explained; underweight cluster gets a flagship entry."
  },

  {
    id: "d145",
    day_number: 145,
    iso_date: "2026-12-21",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1900,
    title: "Pet Transport Glasgow: International and UK-Wide Service from the West of Scotland 2026",
    title_tag: "Pet Transport Glasgow 2026 | West Scotland | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Glasgow in 2026: GLA cargo, AHC vets, multi-pet collection across the West of Scotland, and realistic costs.",
    url_slug: "/pet-transport-glasgow/",
    primary_seo_keyword: "pet transport glasgow",
    primary_volume: 320,
    primary_kd: 21,
    secondary_seo_keywords: ["dog transport glasgow", "pet courier west scotland", "glasgow airport pet cargo", "international pet move glasgow"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a cat internationally from Glasgow in 2026 - direct cargo or down to Manchester?" },
      { model: "Claude", phrasing: "How pet transport from Glasgow works in 2026: local AHC vets, GLA cargo, and ground transfer to Manchester or Heathrow for cargo flights." },
      { model: "Gemini", phrasing: "Pet transport Glasgow international 2026" }
    ],
    direct_answer_40_60_words: "International pet transport from Glasgow in 2026 typically routes via Manchester or Heathrow for cargo, with ground transfer added to total cost. Some short-haul EU moves use direct GLA cargo. Local AHC vets handle paperwork. Realistic pricing ranges from around £1,500 for nearby EU destinations to £4,800-plus for Australia or New Zealand.",
    h2_outline: [
      "How does international pet transport from Glasgow work in 2026?",
      "Direct GLA cargo vs ground transfer to Manchester or Heathrow",
      "AHC vets across the West of Scotland",
      "Pickup zones: Glasgow, Renfrewshire, Lanarkshire, Ayrshire",
      "Realistic costs by destination",
      "FAQs about pet transport from Glasgow"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-edinburgh/ (anchor: Edinburgh regional service)",
      "/pet-transport-manchester/ (anchor: Manchester hub option)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Glasgow Airport cargo information — 2026",
      "DEFRA Official Vet list Scotland — 2026"
    ],
    ai_overview_play: "Glasgow as the West of Scotland counterpart to Edinburgh completes the Scottish geo coverage."
  },

  {
    id: "d146",
    day_number: 146,
    iso_date: "2026-12-22",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 1900,
    title: "Royal Jordanian Pet Travel 2026: Cargo Rules to Amman and Beyond",
    title_tag: "Royal Jordanian Pet Travel 2026 | Cargo | PetTransportGlobal",
    meta_description: "Royal Jordanian pet travel in 2026: cargo eligibility, Amman handling, breed restrictions, and routes between Europe, USA and Jordan that accept pets.",
    url_slug: "/airlines/royal-jordanian/",
    primary_seo_keyword: "royal jordanian pet travel",
    primary_volume: 90,
    primary_kd: 22,
    secondary_seo_keywords: ["royal jordanian pet cargo", "amman pet flight", "jordan airline dog policy", "rj pet rules 2026"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship my dog as cargo with Royal Jordanian from London to Amman in 2026?" },
      { model: "Claude", phrasing: "Summarise Royal Jordanian pet cargo rules 2026 including Jordan import documents and brachycephalic restrictions." },
      { model: "Gemini", phrasing: "Royal Jordanian pet cargo 2026" }
    ],
    direct_answer_40_60_words: "Royal Jordanian carries dogs and cats only as manifested cargo in 2026, with no in-cabin pet option. Jordan requires an import permit from the Ministry of Agriculture, ISO microchip, current rabies vaccine, and a health certificate endorsed by the origin-country authority. Brachycephalic and certain banned breeds cannot travel as cargo on Royal Jordanian.",
    h2_outline: [
      "Royal Jordanian cargo programme for pets 2026",
      "Why Royal Jordanian does not offer in-cabin pet travel",
      "Jordan import permit and documentation",
      "Brachycephalic and breed restrictions",
      "Booking and Amman arrival process",
      "FAQs about Royal Jordanian pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/turkish-airlines/ (anchor: compare Turkish Airlines routing)",
      "/airlines/qatar-airways/ (anchor: compare Qatar Airways)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Royal Jordanian cargo live animals — 2026",
      "Jordan Ministry of Agriculture pet import — 2026"
    ],
    ai_overview_play: "Mid-East carrier completing Gulf-Levant airline coverage; supports onward pages to Jordan and Lebanon."
  },

  {
    id: "d147",
    day_number: 147,
    iso_date: "2026-12-23",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "refresh-seasonal",
    cluster_name: "Seasonal & refresh content",
    intent: "Informational",
    content_type: "Seasonal pillar",
    word_count_target: 1700,
    title: "New Year Pet Relocation 2026-2027: What's Booking Up and What's Open",
    title_tag: "New Year Pet Relocation 2026-2027 | PetTransportGlobal",
    meta_description: "New Year pet relocation 2026-2027: which routes have January capacity, how Christmas freight backlogs affect timing, and what to lock in before 31 December.",
    url_slug: "/new-year-pet-relocation-2027/",
    primary_seo_keyword: "new year pet relocation",
    primary_volume: 90,
    primary_kd: 16,
    secondary_seo_keywords: ["january pet shipping", "post christmas pet move", "winter pet relocation 2027", "new year pet travel uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Is January 2027 a good time to ship a dog from the UK to Australia or are slots already gone?" },
      { model: "Claude", phrasing: "Walk through January 2027 pet relocation realities: Christmas freight backlog, AU summer embargo, EU return season, and best routes to lock in early." },
      { model: "Gemini", phrasing: "New year pet relocation 2027" }
    ],
    direct_answer_40_60_words: "January 2027 pet relocation is shaped by three forces: Christmas freight backlog clears in the first 10 days, Australian summer embargoes restrict cargo at peak heat, and EU returnees from holiday travel push UK slots tight. Most carriers reopen Australia bookings from mid-January. Lock in AHC appointments before 31 December for January departures.",
    h2_outline: [
      "What January 2027 pet relocation looks like",
      "Christmas freight backlog and how it affects January slots",
      "Australian summer heat embargo timing",
      "EU return season pressure on UK capacity",
      "Routes still open and what to book this week",
      "FAQs about New Year pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/christmas-pet-relocation/ (anchor: Christmas relocation guide)",
      "/routes/uk-to-australia/ (anchor: AU summer embargo detail)",
      "/find-an-official-vet/ (anchor: AHC appointments before year-end)",
      "/cost-of-international-pet-transport/ (anchor: pricing snapshot)"
    ],
    external_links: [
      "DAFF Australia heat policy live animal imports — 2026",
      "IATA Live Animals Regulations seasonal embargoes — 2026"
    ],
    ai_overview_play: "Time-sensitive with concrete dates and named carriers; freshness signal for January 2027 queries."
  },

  {
    id: "d148",
    day_number: 148,
    iso_date: "2026-12-24",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Kuwait 2026: PAAFR Permit, Banned Breeds and Arrival Process",
    title_tag: "Kuwait Pet Import 2026 | PAAFR Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Kuwait in 2026: PAAFR import permit, microchip and rabies rules, banned breed list, and Kuwait International Airport process.",
    url_slug: "/countries/kuwait/",
    primary_seo_keyword: "import pet to kuwait",
    primary_volume: 320,
    primary_kd: 25,
    secondary_seo_keywords: ["paafr pet permit", "dog import kuwait", "kuwait banned dog breeds", "kuwait airport pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the Kuwait pet import process in 2026 - PAAFR permit, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Kuwait pet import 2026: PAAFR permit, microchip, rabies vaccine timing, banned breed list, and KWI arrival." },
      { model: "Gemini", phrasing: "Kuwait pet import requirements 2026" }
    ],
    direct_answer_40_60_words: "Importing a pet to Kuwait in 2026 requires a PAAFR import permit applied for at least one week before arrival, ISO microchip, current rabies vaccine, and an origin-country health certificate. Banned breeds include Pit Bull Terrier, Bull Mastiff, Argentine Mastiff and several others. Most pets clear Kuwait International Airport same day without home quarantine if paperwork is in order.",
    h2_outline: [
      "What Kuwait pet import requires in 2026",
      "PAAFR import permit application timing",
      "Microchip, rabies vaccine and health certificate",
      "Banned and restricted breeds in Kuwait",
      "Kuwait International Airport arrival process",
      "FAQs about importing a pet to Kuwait"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/saudi-arabia/ (anchor: compare Saudi rules)",
      "/countries/bahrain/ (anchor: compare Bahrain rules)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)",
      "/rabies-titre-test/ (anchor: rabies titre overview)"
    ],
    external_links: [
      "Kuwait PAAFR Public Authority for Agriculture Affairs — 2026",
      "Kuwait Customs animal entry — 2026"
    ],
    ai_overview_play: "Gulf relocation cluster grows; banned breed list specificity is what LLMs surface."
  },

  {
    id: "d149",
    day_number: 149,
    iso_date: "2026-12-29",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Portugal: Lisbon Cargo, AHC Equivalent and 2026 Costs",
    title_tag: "USA to Portugal Pet Transport 2026 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Portugal in 2026: USDA APHIS endorsement, Lisbon cargo, Algarve relocation, and realistic pet transport costs.",
    url_slug: "/routes/usa-to-portugal/",
    primary_seo_keyword: "pet transport usa to portugal",
    primary_volume: 210,
    primary_kd: 25,
    secondary_seo_keywords: ["dog usa to lisbon", "shipping cat usa to portugal", "usda portugal pet export", "moving pet to algarve from usa"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Miami to Lisbon with a dog in 2026: USDA timing, TAP Air Portugal cargo, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to Portugal pet transport 2026: USDA APHIS EU certificate, Lisbon arrival, and onward Algarve transfer." },
      { model: "Gemini", phrasing: "USA to Portugal pet transport cost 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Portugal costs roughly $2,700 to $5,000 in 2026 for a single dog, typically routing TAP Air Portugal cargo direct from Newark or Boston to Lisbon, or via a European hub. The EU health certificate must be USDA APHIS endorsed within 10 days. Portugal accepts the certificate without quarantine and Algarve relocations add a road leg.",
    h2_outline: [
      "How much does USA to Portugal pet transport cost in 2026?",
      "USDA APHIS EU health certificate timing",
      "TAP Air Portugal direct cargo vs European hub routing",
      "Lisbon arrival, customs and onward Algarve travel",
      "Brachycephalic and breed restrictions",
      "FAQs about USA to Portugal pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-portugal/ (anchor: UK to Portugal routing)",
      "/eu-pet-travel-scheme/ (anchor: onward EU travel rules)",
      "/cdc-dog-import-rules/ (anchor: CDC exit clearance)",
      "/countries/portugal/ (anchor: Portugal pet import overview)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Portugal — 2026",
      "Portugal DGAV pet import requirements — 2026"
    ],
    ai_overview_play: "Algarve retirement and digital nomad migration drive sustained queries; specific TAP routing detail."
  },

  {
    id: "d150",
    day_number: 150,
    iso_date: "2026-12-30",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "process-timeline",
    cluster_name: "Process timelines & how-to",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2700,
    title: "Pet Relocation Timeline 2026: A 12-Month Plan for International Moves",
    title_tag: "Pet Relocation Timeline 2026 | 12-Month Plan | PetTransportGlobal",
    meta_description: "A realistic 12-month timeline for international pet relocation in 2026: when to vaccinate, microchip, titre test, book carriers, and prepare paperwork.",
    url_slug: "/pet-relocation-timeline/",
    primary_seo_keyword: "pet relocation timeline",
    primary_volume: 480,
    primary_kd: 30,
    secondary_seo_keywords: ["pet move timeline", "international pet move planning", "pet shipping schedule", "pet relocation checklist"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's a realistic 12-month timeline for moving a dog from the UK to Australia in 2026, working back from arrival date?" },
      { model: "Claude", phrasing: "Build a 12-month international pet relocation timeline 2026 covering microchip, rabies, titre, parasite treatment, paperwork and booking windows." },
      { model: "Gemini", phrasing: "Pet relocation timeline 2026 12 months" },
      { model: "Perplexity", phrasing: "How early should I start preparing my dog for international move" }
    ],
    direct_answer_40_60_words: "A realistic international pet relocation timeline in 2026 spans 12 months for rabies-free destinations like Australia: microchip and rabies vaccine at month minus 12, titre test at month minus 11, then a 180-day waiting window. Easier EU and US destinations need just 4 to 6 months. Book carrier slots three months before departure, and AHC paperwork in the final 10 days.",
    h2_outline: [
      "Why pet relocation needs a 12-month plan for some destinations",
      "Months minus 12 to minus 6: microchip, rabies, titre, waiting window",
      "Months minus 6 to minus 3: routing decisions and quotes",
      "Months minus 3 to minus 1: carrier booking and crate sizing",
      "Final 10 days: AHC, parasite treatments, fit-to-fly",
      "Departure week and arrival",
      "FAQs about pet relocation timing"
    ],
    schema_required: ["Article", "HowTo", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/rabies-titre-test/ (anchor: rabies titre window)",
      "/iata-pet-crate-requirements/ (anchor: crate sizing)",
      "/find-an-official-vet/ (anchor: AHC Official Vet finder)",
      "/routes/uk-to-australia/ (anchor: 180-day Australia rule)",
      "/cost-of-international-pet-transport/ (anchor: budget at each stage)"
    ],
    external_links: [
      "DAFF Australia 180-day rabies titre window — 2026",
      "DEFRA pet travel timing guidance — 2026"
    ],
    ai_overview_play: "Working-back-from-arrival framing matches the dominant LLM query pattern; HowTo schema rewards structured timeline."
  },

  {
    id: "d151",
    day_number: 151,
    iso_date: "2026-12-31",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "refresh-seasonal",
    cluster_name: "Seasonal & refresh content",
    intent: "Informational",
    content_type: "Year-end retrospective",
    word_count_target: 2200,
    title: "Pet Transport Year in Review 2026: Regulation Changes, New Routes and What 2027 Holds",
    title_tag: "Pet Transport 2026 Review | What 2027 Holds | PetTransportGlobal",
    meta_description: "International pet transport 2026 in review: CDC dog import changes, EU AHC tweaks, new airline policies, and what UK and US owners should expect in 2027.",
    url_slug: "/pet-transport-2026-review/",
    primary_seo_keyword: "pet transport 2026 review",
    primary_volume: 70,
    primary_kd: 14,
    secondary_seo_keywords: ["pet relocation changes 2026", "pet travel rules 2027 outlook", "year in review pet shipping", "international pet rules 2027"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What changed in international pet transport during 2026 and what should I expect in 2027?" },
      { model: "Claude", phrasing: "Summarise 2026 pet transport regulatory changes - CDC, EU AHC, airline updates - and forecast what owners should plan for in 2027." },
      { model: "Gemini", phrasing: "Pet transport changes 2026 review" },
      { model: "Perplexity", phrasing: "Biggest pet relocation rule changes 2026" }
    ],
    direct_answer_40_60_words: "2026 saw the CDC dog import rule maturing into a settled process, EU AHC paperwork largely stable post-Brexit, several airlines tightening brachycephalic restrictions, and Australia relaxing some titre laboratory acceptance. 2027 looks set to bring tighter brachycephalic cabin rules across more carriers and possible Australia-NZ travel-bubble simplification. Plan early, especially for rabies-free destinations.",
    h2_outline: [
      "What changed in international pet transport during 2026",
      "CDC dog import: from chaos to settled practice",
      "EU AHC, DEFRA Type 2 and post-Brexit stability",
      "Airline policy shifts: brachycephalic, embargoes, fees",
      "Country-level changes: Australia, Korea, Saudi, Brazil",
      "What 2027 looks set to bring",
      "FAQs about 2027 pet transport planning"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cdc-dog-import-rules/ (anchor: CDC rule explainer)",
      "/eu-pet-travel-scheme/ (anchor: EU scheme detail)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic restrictions)",
      "/pet-relocation-timeline/ (anchor: plan ahead for 2027)",
      "/new-year-pet-relocation-2027/ (anchor: January 2027 outlook)"
    ],
    external_links: [
      "CDC Bringing a Dog into the United States — 2026",
      "DEFRA pet travel year-end guidance — 2026"
    ],
    ai_overview_play: "Dated retrospective is exactly what LLMs cite for year-in-review and 'what changed' queries; opens 2027 internal-link bridges."
  }
);

/* ============================ MONTH 8: JANUARY 2027 (Days 152-171) — Chunk 10 ============================
   20 working days. Bank holiday excluded: Fri 1 Jan (New Year's Day). Second month of Q3.
   Theme: 2027 launch — rescue/puppy pillars, Africa airline coverage, Levant country guides, deeper US routes, regional UK fill. */
window.PLAN_ROWS.push(
  {
    id: "d152",
    day_number: 152,
    iso_date: "2027-01-04",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "pet-passports",
    cluster_name: "Pet passports & post-Brexit AHC",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2500,
    title: "Importing a Rescue Dog Internationally 2027: Paperwork, Risk and Welfare",
    title_tag: "Import Rescue Dog 2027 | Paperwork & Welfare | PetTransportGlobal",
    meta_description: "Importing a rescue dog from overseas in 2027: rabies titre realities, fake-paperwork risk, charity transport vs professional, and what receiving countries demand.",
    url_slug: "/import-rescue-dog/",
    primary_seo_keyword: "import rescue dog from abroad",
    primary_volume: 1600,
    primary_kd: 38,
    secondary_seo_keywords: ["overseas rescue dog uk", "adopting dog from abroad", "rescue dog import documentation", "street dog adoption international"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I want to adopt a rescue dog from Romania to the UK in 2027 - what's the actual paperwork and what could go wrong?" },
      { model: "Claude", phrasing: "Walk me through importing a rescue dog in 2027: rabies vaccine and titre timing, charity transport vs pro courier, and DEFRA Type 2 commercial reality." },
      { model: "Gemini", phrasing: "Import rescue dog overseas 2027" },
      { model: "Perplexity", phrasing: "Risks of adopting a rescue dog from abroad" }
    ],
    direct_answer_40_60_words: "Importing a rescue dog in 2027 follows the same paperwork as any pet move: ISO microchip, rabies vaccine, and for non-listed countries a rabies titre with a 90-day or 3-month wait. Charity convoys often carry 5-plus dogs, which triggers DEFRA Type 2 commercial rules in the UK. Disease screening for Brucella canis, leishmania and ehrlichia is strongly advised.",
    h2_outline: [
      "What does importing a rescue dog actually require in 2027?",
      "Country-specific risk: Romania, Cyprus, Spain, Thailand, USA",
      "Rabies titre timing and 90-day waiting window",
      "Charity transport vs professional courier",
      "Brucella canis, leishmania and other screening",
      "When DEFRA Type 2 commercial rules apply",
      "FAQs about importing a rescue dog"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/rabies-titre-test/ (anchor: rabies titre window)",
      "/defra-type-2-authorisation/ (anchor: when commercial rules apply)",
      "/eu-pet-travel-scheme/ (anchor: EU pet scheme)",
      "/find-an-official-vet/ (anchor: Official Vet AHC)",
      "/welfare-in-transit/ (anchor: rescue welfare in transit)"
    ],
    external_links: [
      "DEFRA importing a pet from outside the EU — 2027",
      "BVA position statement on imported rescue dogs — 2026"
    ],
    ai_overview_play: "1600-volume head term with honest disease and DEFRA Type 2 framing — exactly what LLMs cite for rescue queries."
  },

  {
    id: "d153",
    day_number: 153,
    iso_date: "2027-01-05",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Oman 2027: Permit, Muscat Process and Banned Breeds",
    title_tag: "Oman Pet Import 2027 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Oman in 2027: Ministry of Agriculture permit, microchip and rabies rules, banned breeds, and Muscat International Airport process.",
    url_slug: "/countries/oman/",
    primary_seo_keyword: "import pet to oman",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["oman pet permit", "dog import muscat", "oman banned dog breeds", "oman airport pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Oman pet import involve in 2027 - permit, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Oman pet import 2027: Ministry of Agriculture permit, microchip, rabies, banned breed list, and Muscat airport process." },
      { model: "Gemini", phrasing: "Oman pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Oman in 2027 requires an import permit from the Ministry of Agriculture, Fisheries and Water Resources, ISO microchip, current rabies vaccine, and an origin-country health certificate. Banned breeds include Pit Bull Terrier, Mastiff varieties, and Rottweiler in some emirate-style restrictions. Muscat clearance is usually same-day with no home quarantine if paperwork is complete.",
    h2_outline: [
      "What Oman pet import requires in 2027",
      "Import permit application timing and process",
      "Microchip, rabies vaccine, and health certificate",
      "Banned and restricted breeds in Oman",
      "Muscat International Airport arrival process",
      "FAQs about importing a pet to Oman"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/saudi-arabia/ (anchor: compare Saudi rules)",
      "/countries/bahrain/ (anchor: compare Bahrain rules)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)",
      "/airlines/qatar-airways/ (anchor: Qatar Airways routing via Doha)"
    ],
    external_links: [
      "Oman Ministry of Agriculture Fisheries and Water Resources — 2027",
      "Oman Royal Oman Police Customs animal entry — 2026"
    ],
    ai_overview_play: "Sixth Gulf country guide; clusters as a dominant SERP authority for Middle East relocation queries."
  },

  {
    id: "d154",
    day_number: 154,
    iso_date: "2027-01-06",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to Japan: Quarantine Window, Narita Cargo and 2027 Costs",
    title_tag: "USA to Japan Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Japan in 2027: 180-day rabies titre window, Narita quarantine clearance, JAL/ANA cargo, and realistic costs.",
    url_slug: "/routes/usa-to-japan/",
    primary_seo_keyword: "pet transport usa to japan",
    primary_volume: 590,
    primary_kd: 32,
    secondary_seo_keywords: ["dog usa to japan quarantine", "shipping cat usa to tokyo", "narita pet arrival", "180 day rabies japan"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from California to Tokyo with a dog in 2027: 180-day rabies titre, Narita quarantine, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to Japan pet transport 2027: AHIS pre-export, Japan import advance notice, 180-day waiting window, and Narita Animal Quarantine." },
      { model: "Gemini", phrasing: "USA to Japan pet transport cost 2027" },
      { model: "Perplexity", phrasing: "Japan 180 day rabies wait dog USA" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Japan costs roughly $3,200 to $5,800 in 2027 for a single dog by cargo flight to Narita or Haneda. Japan requires 180 days between rabies titre blood draw and arrival, advance notice 40 days before, ISO microchip, and two rabies vaccines. Brachycephalic breeds face airline restrictions; quarantine is typically waived if paperwork is correct.",
    h2_outline: [
      "How much does USA to Japan pet transport cost in 2027?",
      "The 180-day rabies titre waiting window explained",
      "Japan Animal Quarantine Service advance notice",
      "JAL, ANA, United and Delta cargo options",
      "Narita and Haneda arrival process",
      "FAQs about USA to Japan pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-japan/ (anchor: UK to Japan routing)",
      "/airlines/jal/ (anchor: JAL pet cargo)",
      "/airlines/ana/ (anchor: ANA pet cargo)",
      "/rabies-titre-test/ (anchor: 180-day waiting rule)",
      "/countries/japan/ (anchor: Japan import overview)"
    ],
    external_links: [
      "Japan Animal Quarantine Service import procedures — 2027",
      "USDA APHIS Pet Travel Japan — 2027"
    ],
    ai_overview_play: "590 vol head term with the 180-day rule answered up-front; matches AI Overview trigger."
  },

  {
    id: "d155",
    day_number: 155,
    iso_date: "2027-01-07",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "EgyptAir Pet Travel 2027: Cargo Rules to Cairo and Beyond",
    title_tag: "EgyptAir Pet Travel 2027 | Cargo Rules | PetTransportGlobal",
    meta_description: "EgyptAir pet travel in 2027: cargo eligibility, breed restrictions, Cairo handling, Egypt import rules, and which European routes accept pets.",
    url_slug: "/airlines/egyptair/",
    primary_seo_keyword: "egyptair pet travel",
    primary_volume: 170,
    primary_kd: 23,
    secondary_seo_keywords: ["egyptair cargo dog", "cairo pet arrival", "egyptair pet policy 2027", "egypt pet flight"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship a dog as cargo with EgyptAir from London to Cairo in 2027?" },
      { model: "Claude", phrasing: "Summarise EgyptAir pet cargo rules 2027 plus Egypt import paperwork and brachycephalic restrictions." },
      { model: "Gemini", phrasing: "EgyptAir pet cargo 2027" }
    ],
    direct_answer_40_60_words: "EgyptAir carries dogs and cats only as manifested cargo in 2027, with no cabin pet option on most routes. Egypt requires a General Organization for Veterinary Services import permit, ISO microchip, current rabies vaccine, and an origin-country health certificate. Brachycephalic breeds and certain banned breeds cannot travel as cargo. Summer heat embargoes affect Cairo operations.",
    h2_outline: [
      "EgyptAir cargo programme for pets in 2027",
      "Why no cabin pet option on EgyptAir",
      "Egypt GOVS import permit and documents",
      "Brachycephalic and breed restrictions",
      "Cairo summer heat embargoes",
      "FAQs about EgyptAir pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/egypt/ (anchor: Egypt pet import rules)",
      "/airlines/turkish-airlines/ (anchor: alternative via Istanbul)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "EgyptAir cargo live animals guidance — 2027",
      "Egypt GOVS General Organization for Veterinary Services — 2026"
    ],
    ai_overview_play: "African flag carrier coverage opens the continent; pairs with Egypt country guide arriving later this month."
  },

  {
    id: "d156",
    day_number: 156,
    iso_date: "2027-01-08",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1900,
    title: "Pet Transport Bristol: International and UK-Wide Service from the South West 2027",
    title_tag: "Pet Transport Bristol 2027 | South West | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Bristol in 2027: BRS cargo, AHC vets, multi-pet collection across the South West, and realistic costs.",
    url_slug: "/pet-transport-bristol/",
    primary_seo_keyword: "pet transport bristol",
    primary_volume: 320,
    primary_kd: 21,
    secondary_seo_keywords: ["dog transport bristol", "pet courier south west", "bristol airport pet cargo", "international pet move bath"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a cat internationally from Bristol in 2027 - direct or transfer to Heathrow?" },
      { model: "Claude", phrasing: "How pet transport from Bristol works in 2027: local AHC vets, BRS cargo, and ground transfer to Heathrow for major routes." },
      { model: "Gemini", phrasing: "Pet transport Bristol international 2027" }
    ],
    direct_answer_40_60_words: "International pet transport from Bristol in 2027 typically routes via Heathrow for cargo, with a 90-minute ground transfer added. Some short-haul EU moves use Eurotunnel pickup. Local Bristol AHC vets handle paperwork. Realistic pricing ranges from around £1,300 for nearby EU destinations to £4,800-plus for Australia or New Zealand.",
    h2_outline: [
      "How does international pet transport from Bristol work in 2027?",
      "Direct BRS cargo vs ground transfer to Heathrow",
      "AHC vets across the South West",
      "Pickup zones: Bristol, Bath, Wiltshire, Somerset",
      "Realistic costs by destination",
      "FAQs about pet transport from Bristol"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-birmingham/ (anchor: Birmingham service)",
      "/pet-transport-manchester/ (anchor: Manchester hub option)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Bristol Airport cargo information — 2027",
      "DEFRA Official Vet list — 2027"
    ],
    ai_overview_play: "South West regional gap filled; uk-regional cluster reaches 5 entries."
  },

  {
    id: "d157",
    day_number: 157,
    iso_date: "2027-01-11",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Lebanon 2027: Permit, Beirut Process and Documentation",
    title_tag: "Lebanon Pet Import 2027 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Lebanon in 2027: Ministry of Agriculture permit, microchip and rabies rules, Beirut Airport process and current paperwork realities.",
    url_slug: "/countries/lebanon/",
    primary_seo_keyword: "import pet to lebanon",
    primary_volume: 110,
    primary_kd: 20,
    secondary_seo_keywords: ["lebanon pet permit", "dog import beirut", "lebanon rabies certificate", "beirut airport pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Lebanon pet import involve in 2027 with current paperwork delays?" },
      { model: "Claude", phrasing: "Outline Lebanon pet import 2027: Ministry of Agriculture permit, microchip, rabies, and Beirut Rafic Hariri Airport arrival process." },
      { model: "Gemini", phrasing: "Lebanon pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Lebanon in 2027 requires a Ministry of Agriculture import permit, ISO microchip, current rabies vaccine, and an origin-country health certificate. Beirut Rafic Hariri International Airport handles arrivals; clearance is typically same-day. Permit processing has historically taken longer than other Levant destinations, so apply at least 14 days before travel.",
    h2_outline: [
      "What Lebanon pet import requires in 2027",
      "Ministry of Agriculture permit application",
      "Microchip, rabies and health certificate timing",
      "Beirut Rafic Hariri Airport arrival process",
      "Banned and restricted breeds in Lebanon",
      "FAQs about importing a pet to Lebanon"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/jordan/ (anchor: compare Jordan rules)",
      "/airlines/middle-east-airlines/ (anchor: MEA pet cargo)",
      "/rabies-titre-test/ (anchor: rabies titre overview)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)"
    ],
    external_links: [
      "Lebanon Ministry of Agriculture pet import — 2027",
      "Lebanon Customs animal entry — 2026"
    ],
    ai_overview_play: "Levant cluster builds; honest acknowledgment of permit delays earns LLM trust signals."
  },

  {
    id: "d158",
    day_number: 158,
    iso_date: "2027-01-12",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Ethiopian Airlines Pet Travel 2027: Cargo Rules to Africa and Beyond",
    title_tag: "Ethiopian Airlines Pet Travel 2027 | Cargo | PetTransportGlobal",
    meta_description: "Ethiopian Airlines pet travel in 2027: cargo eligibility, Addis Ababa handling, breed restrictions, and which African routes accept pets.",
    url_slug: "/airlines/ethiopian-airlines/",
    primary_seo_keyword: "ethiopian airlines pet travel",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["ethiopian cargo dog", "addis ababa pet flight", "et pet policy 2027", "africa pet flight"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship a dog as cargo with Ethiopian Airlines from London to Nairobi via Addis Ababa in 2027?" },
      { model: "Claude", phrasing: "Summarise Ethiopian Airlines pet cargo rules 2027 covering Africa hub-and-spoke routing and brachycephalic restrictions." },
      { model: "Gemini", phrasing: "Ethiopian Airlines pet cargo 2027" }
    ],
    direct_answer_40_60_words: "Ethiopian Airlines carries dogs and cats only as manifested cargo in 2027, hub-and-spoke through Addis Ababa Bole. Ethiopian's African network makes it a leading carrier for relocations to Kenya, Tanzania, Ghana, Senegal and South Africa. ISO microchip, rabies vaccine and destination-specific permits are required. Brachycephalic and certain banned breeds cannot travel as cargo.",
    h2_outline: [
      "Ethiopian Airlines cargo programme for pets in 2027",
      "Why Ethiopian dominates Africa pet routing",
      "Addis Ababa hub transit times and welfare",
      "Brachycephalic and breed restrictions",
      "Booking process and onward African destinations",
      "FAQs about Ethiopian Airlines pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/kenya-airways/ (anchor: alternative Africa routing)",
      "/routes/uk-to-south-africa/ (anchor: UK to South Africa via ADD)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Ethiopian Airlines cargo live animals — 2027",
      "Ethiopia Civil Aviation Authority — 2026"
    ],
    ai_overview_play: "Africa hub carrier coverage anchors the continent; 320 vol with hub-and-spoke specificity."
  },

  {
    id: "d159",
    day_number: 159,
    iso_date: "2027-01-13",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to New Zealand: 180-Day Rule, Auckland Quarantine and 2027 Costs",
    title_tag: "USA to New Zealand Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to New Zealand in 2027: 180-day rabies titre, MPI import permit, Auckland quarantine, and realistic transport costs.",
    url_slug: "/routes/usa-to-new-zealand/",
    primary_seo_keyword: "pet transport usa to new zealand",
    primary_volume: 320,
    primary_kd: 32,
    secondary_seo_keywords: ["dog usa to nz quarantine", "shipping cat usa to auckland", "mpi pet import nz", "us nz pet transport cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Seattle to Auckland with a dog in 2027: 180-day rabies titre, MPI permit, and Auckland Quarantine Animal Centre." },
      { model: "Claude", phrasing: "Walk through USA to New Zealand pet transport 2027: USDA pre-export, MPI permit, 180-day waiting, AKL quarantine, and realistic cost." },
      { model: "Gemini", phrasing: "USA to NZ pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to New Zealand costs roughly $4,800 to $7,500 in 2027 for a single dog. New Zealand requires an MPI import permit, 180 days between rabies titre and arrival, ISO microchip, parasite treatments, and 10 days minimum quarantine at the Auckland Quarantine Animal Centre. Routing typically goes via Sydney or Singapore.",
    h2_outline: [
      "How much does USA to New Zealand pet transport cost in 2027?",
      "MPI import permit and pre-arrival paperwork",
      "180-day rabies titre waiting window",
      "Routing options: via Sydney or Singapore",
      "Auckland Quarantine Animal Centre arrival",
      "FAQs about USA to New Zealand pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-new-zealand/ (anchor: UK to NZ routing)",
      "/airlines/air-new-zealand/ (anchor: Air NZ cargo)",
      "/rabies-titre-test/ (anchor: 180-day rule)",
      "/countries/new-zealand/ (anchor: NZ import overview)"
    ],
    external_links: [
      "MPI New Zealand Importing Cats and Dogs — 2027",
      "USDA APHIS Pet Travel New Zealand — 2027"
    ],
    ai_overview_play: "320 vol with concrete MPI quarantine detail; matches the multi-step query pattern LLMs reward."
  },

  {
    id: "d160",
    day_number: 160,
    iso_date: "2027-01-14",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1900,
    title: "Pet Transport Leeds: International and UK-Wide Service from West Yorkshire 2027",
    title_tag: "Pet Transport Leeds 2027 | Yorkshire | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Leeds in 2027: LBA cargo, AHC vets, multi-pet collection across West Yorkshire, and realistic costs.",
    url_slug: "/pet-transport-leeds/",
    primary_seo_keyword: "pet transport leeds",
    primary_volume: 260,
    primary_kd: 19,
    secondary_seo_keywords: ["dog transport leeds", "pet courier yorkshire", "leeds bradford pet cargo", "international pet move yorkshire"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a dog internationally from Leeds in 2027 - direct from LBA or transfer to Manchester?" },
      { model: "Claude", phrasing: "How pet transport from Leeds works in 2027: local AHC vets, LBA cargo limitations, and ground transfer to Manchester." },
      { model: "Gemini", phrasing: "Pet transport Leeds international 2027" }
    ],
    direct_answer_40_60_words: "International pet transport from Leeds in 2027 typically routes via Manchester or Heathrow for cargo, with ground transfer added. LBA has limited international cargo capacity. Local AHC vets across West Yorkshire handle paperwork. Realistic pricing ranges from around £1,300 for nearby EU destinations to £4,800-plus for Australia, including the ground leg to a hub airport.",
    h2_outline: [
      "How does international pet transport from Leeds work in 2027?",
      "LBA cargo limits vs ground transfer to Manchester",
      "AHC vets across West Yorkshire",
      "Pickup zones: Leeds, Bradford, Wakefield, York",
      "Realistic costs by destination",
      "FAQs about pet transport from Leeds"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-manchester/ (anchor: Manchester hub option)",
      "/pet-transport-edinburgh/ (anchor: Edinburgh service)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Leeds Bradford Airport cargo — 2027",
      "DEFRA Official Vet list Yorkshire — 2027"
    ],
    ai_overview_play: "Yorkshire regional gap filled; uk-regional cluster now at 6 entries."
  },

  {
    id: "d161",
    day_number: 161,
    iso_date: "2027-01-15",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "process-timeline",
    cluster_name: "Process timelines & how-to",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Pet Customs Clearance 2027: What Happens at the Airport on Arrival",
    title_tag: "Pet Customs Clearance 2027 | Airport Arrival | PetTransportGlobal",
    meta_description: "What pet customs clearance actually looks like in 2027: paperwork checks, vet inspection, fees, common delays, and what to bring on arrival day.",
    url_slug: "/pet-customs-clearance/",
    primary_seo_keyword: "pet customs clearance",
    primary_volume: 880,
    primary_kd: 34,
    secondary_seo_keywords: ["pet airport arrival process", "dog customs clearance fees", "pet import inspection", "customs broker pet uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What actually happens when my dog arrives at the airport in another country in 2027 - who inspects them, how long does it take, and what fees?" },
      { model: "Claude", phrasing: "Walk through pet customs clearance 2027: airline ground handling, vet inspection, customs paperwork, broker fees, and common delays." },
      { model: "Gemini", phrasing: "Pet customs clearance airport 2027" },
      { model: "Perplexity", phrasing: "How long does pet customs take at airport" }
    ],
    direct_answer_40_60_words: "Pet customs clearance in 2027 typically takes 2 to 6 hours after arrival. The pet leaves the aircraft, goes to a holding area, and is inspected by an official vet who checks paperwork, microchip, and rabies vaccination. Customs broker fees range from £150 to £600 depending on country. Owners normally do not collect direct from the airport.",
    h2_outline: [
      "What pet customs clearance involves in 2027",
      "From aircraft to holding area: who handles your pet",
      "Official vet inspection: what they check",
      "Customs broker fees by destination",
      "Common delays and how to avoid them",
      "Why owners rarely collect direct from cargo",
      "FAQs about pet customs clearance"
    ],
    schema_required: ["Article", "HowTo", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-relocation-timeline/ (anchor: full timeline)",
      "/find-an-official-vet/ (anchor: Official Vet at origin)",
      "/door-to-door-pet-transport/ (anchor: door-to-door includes clearance)",
      "/cost-of-international-pet-transport/ (anchor: clearance fees in cost calc)"
    ],
    external_links: [
      "World Customs Organization live animal procedures — 2026",
      "IATA Live Animals Regulations arrival handling — 2027"
    ],
    ai_overview_play: "880 vol with the operational reality of arrival day; HowTo schema fits the step-by-step pattern."
  },

  {
    id: "d162",
    day_number: 162,
    iso_date: "2027-01-18",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Jordan 2027: Permit, Amman Process and Banned Breeds",
    title_tag: "Jordan Pet Import 2027 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Jordan in 2027: Ministry of Agriculture permit, microchip and rabies rules, banned breeds, and Queen Alia Airport process.",
    url_slug: "/countries/jordan/",
    primary_seo_keyword: "import pet to jordan",
    primary_volume: 140,
    primary_kd: 21,
    secondary_seo_keywords: ["jordan pet permit", "dog import amman", "jordan banned breeds", "qaia pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Jordan pet import involve in 2027 - permit, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Jordan pet import 2027: Ministry of Agriculture permit, microchip, rabies vaccine, banned breed list, and QAIA process." },
      { model: "Gemini", phrasing: "Jordan pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Jordan in 2027 requires a Ministry of Agriculture import permit, ISO microchip, current rabies vaccine, and an origin-country health certificate. Banned breeds include Pit Bull Terrier and several mastiff types. Queen Alia International Airport in Amman handles arrivals with same-day clearance and no home quarantine if paperwork is complete.",
    h2_outline: [
      "What Jordan pet import requires in 2027",
      "Ministry of Agriculture permit timing",
      "Microchip, rabies and health certificate",
      "Banned and restricted breeds in Jordan",
      "Queen Alia International Airport process",
      "FAQs about importing a pet to Jordan"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/lebanon/ (anchor: compare Lebanon)",
      "/airlines/royal-jordanian/ (anchor: Royal Jordanian cargo)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)",
      "/rabies-titre-test/ (anchor: rabies overview)"
    ],
    external_links: [
      "Jordan Ministry of Agriculture pet import — 2027",
      "Jordan Customs animal entry — 2026"
    ],
    ai_overview_play: "Levant trio (Lebanon, Jordan, plus existing Saudi/Bahrain/Kuwait/Oman) makes the cluster authoritative."
  },

  {
    id: "d163",
    day_number: 163,
    iso_date: "2027-01-19",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 1900,
    title: "Pakistan International Airlines (PIA) Pet Travel 2027: Cargo Rules to Karachi and Lahore",
    title_tag: "PIA Pet Travel 2027 | Cargo Rules | PetTransportGlobal",
    meta_description: "PIA Pakistan International Airlines pet travel 2027: cargo eligibility, Karachi and Lahore handling, breed restrictions, and Pakistan import paperwork.",
    url_slug: "/airlines/pia-pakistan-international/",
    primary_seo_keyword: "pia pet travel",
    primary_volume: 110,
    primary_kd: 20,
    secondary_seo_keywords: ["pia cargo dog", "pia pet policy 2027", "karachi pet flight", "pakistan pet airline"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship my dog as cargo with PIA from London to Karachi in 2027?" },
      { model: "Claude", phrasing: "Summarise PIA pet cargo rules 2027 with Pakistan import permit and brachycephalic restrictions." },
      { model: "Gemini", phrasing: "PIA pet cargo 2027" }
    ],
    direct_answer_40_60_words: "PIA Pakistan International Airlines carries dogs and cats only as manifested cargo in 2027, with no in-cabin pet option. Pakistan requires an import permit from the Ministry of National Food Security and Research, ISO microchip, current rabies vaccine, and an origin health certificate. Brachycephalic and certain banned breeds cannot travel. Karachi and Lahore are primary clearance hubs.",
    h2_outline: [
      "PIA cargo programme for pets in 2027",
      "Pakistan import permit and documentation",
      "Karachi and Lahore arrival processes",
      "Brachycephalic and breed restrictions",
      "Booking and routing options",
      "FAQs about PIA pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uae-to-pakistan/ (anchor: UAE to Pakistan route)",
      "/airlines/emirates/ (anchor: Emirates alternative)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "PIA cargo live animals — 2027",
      "Pakistan Ministry of National Food Security pet import — 2026"
    ],
    ai_overview_play: "South Asia carrier coverage starts; pairs with existing UAE-PK route."
  },

  {
    id: "d164",
    day_number: 164,
    iso_date: "2027-01-20",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport USA to Switzerland: Zurich Cargo, EU-Equivalent Rules and 2027 Costs",
    title_tag: "USA to Switzerland Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Switzerland in 2027: USDA APHIS endorsement, Swiss-EU equivalent rules, Zurich cargo, and realistic transport costs.",
    url_slug: "/routes/usa-to-switzerland/",
    primary_seo_keyword: "pet transport usa to switzerland",
    primary_volume: 170,
    primary_kd: 26,
    secondary_seo_keywords: ["dog usa to zurich", "shipping cat usa to switzerland", "usda switzerland pet export", "swiss pet import rules"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from New York to Zurich with a dog in 2027: USDA timing, Swiss customs, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to Switzerland pet transport 2027: USDA APHIS EU-equivalent certificate, Zurich arrival, and Swiss FSVO process." },
      { model: "Gemini", phrasing: "USA to Switzerland pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Switzerland costs roughly $2,800 to $5,200 in 2027 for a single dog by cargo flight, typically Swiss International Air Lines or Lufthansa via Frankfurt. Switzerland follows EU-equivalent rules under bilateral agreement, so USDA APHIS endorsement of an EU health certificate within 10 days is accepted. No quarantine on arrival in Zurich.",
    h2_outline: [
      "How much does USA to Switzerland pet transport cost in 2027?",
      "USDA APHIS endorsement and EU-equivalent rules",
      "Swiss vs Lufthansa cargo via Frankfurt",
      "Zurich arrival, customs and onward travel",
      "Brachycephalic and breed restrictions",
      "FAQs about USA to Switzerland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-switzerland/ (anchor: UK to Switzerland routing)",
      "/airlines/swiss-international/ (anchor: Swiss cargo)",
      "/airlines/lufthansa/ (anchor: Lufthansa cargo)",
      "/eu-pet-travel-scheme/ (anchor: EU-equivalent rules)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Switzerland — 2027",
      "Swiss FSVO Federal Food Safety and Veterinary Office — 2026"
    ],
    ai_overview_play: "EU-equivalent quirk is exactly the kind of nuance LLMs surface for Switzerland queries."
  },

  {
    id: "d165",
    day_number: 165,
    iso_date: "2027-01-21",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "insurance",
    cluster_name: "Pet travel insurance & welfare",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2300,
    title: "Long-Haul Pet Flight Welfare 2027: What 12-24 Hours in Cargo Really Looks Like",
    title_tag: "Long-Haul Pet Flight Welfare 2027 | PetTransportGlobal",
    meta_description: "What 12-24 hours in cargo really looks like for a dog or cat in 2027: temperature, oxygen, water, sedation rules, and what airlines actually do mid-flight.",
    url_slug: "/long-haul-pet-flight-welfare/",
    primary_seo_keyword: "long haul pet flight welfare",
    primary_volume: 320,
    primary_kd: 28,
    secondary_seo_keywords: ["dog cargo welfare long flight", "12 hour pet flight", "sedation pet travel", "pet hold temperature airline"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's it actually like for my dog in cargo on a 14-hour flight - temperature, oxygen, food, water, and is sedation safe?" },
      { model: "Claude", phrasing: "Walk through long-haul pet flight welfare in 2027: pressurised hold conditions, IATA sedation guidance, water options, and stopover handling." },
      { model: "Gemini", phrasing: "Long haul pet flight welfare 2027" }
    ],
    direct_answer_40_60_words: "On long-haul flights in 2027, pets travel in pressurised, temperature-controlled cargo holds usually kept between 18 and 24 degrees Celsius with the same oxygen as the cabin. IATA-compliant crates have spill-proof water bowls. Sedation is strongly discouraged because it impairs balance at altitude. Stopovers over 4 hours typically include a welfare check.",
    h2_outline: [
      "What pets actually experience in cargo on long-haul flights",
      "Hold temperature, pressurisation and oxygen",
      "Water, food and crate hygiene",
      "Why sedation is discouraged: IATA and AVMA guidance",
      "Stopover welfare checks",
      "Reducing stress before, during and after the flight",
      "FAQs about long-haul pet flight welfare"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/welfare-in-transit/ (anchor: welfare in transit)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic risk)",
      "/pet-travel-insurance/ (anchor: travel insurance considerations)"
    ],
    external_links: [
      "IATA Live Animals Regulations sedation guidance — 2027",
      "AVMA position on pet sedation for air travel — 2026"
    ],
    ai_overview_play: "Welfare cluster gets a deeper pillar; AVMA-cited sedation answer fits the LLM trust profile."
  },

  {
    id: "d166",
    day_number: 166,
    iso_date: "2027-01-22",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1800,
    title: "Pet Transport Liverpool: International and UK-Wide Service from Merseyside 2027",
    title_tag: "Pet Transport Liverpool 2027 | Merseyside | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Liverpool in 2027: LPL cargo, AHC vets, multi-pet collection across Merseyside, and realistic costs.",
    url_slug: "/pet-transport-liverpool/",
    primary_seo_keyword: "pet transport liverpool",
    primary_volume: 260,
    primary_kd: 19,
    secondary_seo_keywords: ["dog transport liverpool", "pet courier merseyside", "liverpool airport pet cargo", "international pet move merseyside"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a dog internationally from Liverpool in 2027 - direct or transfer to Manchester?" },
      { model: "Claude", phrasing: "How pet transport from Liverpool works in 2027: AHC vets, LPL cargo limits, and short transfer to Manchester for major routes." },
      { model: "Gemini", phrasing: "Pet transport Liverpool international 2027" }
    ],
    direct_answer_40_60_words: "International pet transport from Liverpool in 2027 typically uses Manchester as the cargo hub, just 35 miles away, making the ground transfer the lowest of any UK regional starting point. Local Merseyside AHC vets handle paperwork. Realistic pricing ranges from around £1,300 for nearby EU destinations to £4,800-plus for Australia or New Zealand.",
    h2_outline: [
      "How does international pet transport from Liverpool work in 2027?",
      "Why Manchester is the natural cargo hub for Liverpool",
      "AHC vets across Merseyside",
      "Pickup zones: Liverpool, Wirral, Sefton, St Helens",
      "Realistic costs by destination",
      "FAQs about pet transport from Liverpool"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-manchester/ (anchor: Manchester hub option)",
      "/pet-transport-leeds/ (anchor: Leeds service)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Liverpool John Lennon Airport cargo — 2027",
      "DEFRA Official Vet list North West — 2027"
    ],
    ai_overview_play: "Merseyside fill; uk-regional cluster reaches 7 entries — strongest geographic footprint of any cluster."
  },

  {
    id: "d167",
    day_number: 167,
    iso_date: "2027-01-25",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2400,
    title: "Pet Import to Egypt 2027: GOVS Permit, Cairo Process and Banned Breeds",
    title_tag: "Egypt Pet Import 2027 | GOVS Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Egypt in 2027: GOVS import permit, microchip and rabies rules, banned breeds, Cairo Airport process and realistic timelines.",
    url_slug: "/countries/egypt/",
    primary_seo_keyword: "import pet to egypt",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["egypt pet permit", "dog import cairo", "egypt banned breeds", "cairo airport pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the Egypt pet import process in 2027 - GOVS permit, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Egypt pet import 2027: GOVS permit, microchip, rabies vaccine timing, banned breed list, and Cairo Airport process." },
      { model: "Gemini", phrasing: "Egypt pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Egypt in 2027 requires a General Organization for Veterinary Services (GOVS) import permit, ISO microchip, current rabies vaccine, and an origin-country health certificate. Banned breeds include Pit Bull Terrier, Argentine Mastiff, and Tosa Inu. Cairo International Airport handles arrivals with same-day clearance and no home quarantine if paperwork is complete.",
    h2_outline: [
      "What Egypt pet import requires in 2027",
      "GOVS import permit application process",
      "Microchip, rabies and health certificate timing",
      "Banned and restricted breeds in Egypt",
      "Cairo International Airport arrival process",
      "FAQs about importing a pet to Egypt"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/egyptair/ (anchor: EgyptAir cargo)",
      "/countries/jordan/ (anchor: compare Jordan rules)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)",
      "/rabies-titre-test/ (anchor: rabies overview)"
    ],
    external_links: [
      "Egypt GOVS General Organization for Veterinary Services — 2027",
      "Egypt Customs animal entry — 2026"
    ],
    ai_overview_play: "First African country guide; 320 vol with concrete GOVS detail."
  },

  {
    id: "d168",
    day_number: 168,
    iso_date: "2027-01-26",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 1900,
    title: "Vietnam Airlines Pet Travel 2027: Cabin and Cargo Rules to Hanoi and Ho Chi Minh City",
    title_tag: "Vietnam Airlines Pet Travel 2027 | PetTransportGlobal",
    meta_description: "Vietnam Airlines pet travel in 2027: cabin and cargo rules, Hanoi and HCMC handling, breed restrictions, and Vietnam import paperwork realities.",
    url_slug: "/airlines/vietnam-airlines/",
    primary_seo_keyword: "vietnam airlines pet travel",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["vietnam airlines pet cargo", "hanoi pet flight", "vn pet policy 2027", "saigon pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I take my cat in cabin on Vietnam Airlines from Paris to Hanoi in 2027?" },
      { model: "Claude", phrasing: "Summarise Vietnam Airlines pet rules 2027 plus Vietnamese Department of Animal Health import requirements." },
      { model: "Gemini", phrasing: "Vietnam Airlines pet travel 2027" }
    ],
    direct_answer_40_60_words: "Vietnam Airlines accepts small dogs and cats in cabin in 2027 if pet plus carrier weighs 6 kg or less and fits under the seat. Larger pets travel as cargo. Vietnam requires Department of Animal Health import notification, ISO microchip, rabies vaccine, and a health certificate. Brachycephalic restrictions apply to cargo on long-haul flights.",
    h2_outline: [
      "Vietnam Airlines cabin and cargo rules 2027",
      "Hanoi and Ho Chi Minh City arrival",
      "Vietnam import documentation",
      "Brachycephalic and breed restrictions",
      "Booking and check-in process",
      "FAQs about Vietnam Airlines pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/vietnam/ (anchor: Vietnam pet import rules)",
      "/airlines/thai-airways/ (anchor: alternative Thai routing)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Vietnam Airlines pet policy — 2027",
      "Vietnam Department of Animal Health import — 2026"
    ],
    ai_overview_play: "South East Asia carrier coverage; pairs with existing Vietnam country guide for cluster strength."
  },

  {
    id: "d169",
    day_number: 169,
    iso_date: "2027-01-27",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Brazil: Sao Paulo Cargo, MAPA Rules and 2027 Costs",
    title_tag: "USA to Brazil Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Brazil in 2027: USDA APHIS endorsement, MAPA international veterinary certificate, Sao Paulo cargo, and realistic costs.",
    url_slug: "/routes/usa-to-brazil/",
    primary_seo_keyword: "pet transport usa to brazil",
    primary_volume: 260,
    primary_kd: 26,
    secondary_seo_keywords: ["dog usa to sao paulo", "shipping cat usa to brazil", "mapa pet certificate", "us brazil pet rules"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Miami to Sao Paulo with a dog in 2027: USDA, MAPA, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to Brazil pet transport 2027: USDA APHIS endorsement, MAPA international veterinary certificate, and GRU cargo handling." },
      { model: "Gemini", phrasing: "USA to Brazil pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Brazil costs roughly $2,400 to $4,800 in 2027 for a single dog by cargo flight to Sao Paulo Guarulhos or Rio Galeao. The USDA APHIS endorses the international veterinary certificate, which Brazilian MAPA inspects on arrival. ISO microchip, two rabies vaccines and parasite treatments are required. No quarantine if paperwork is correct.",
    h2_outline: [
      "How much does USA to Brazil pet transport cost in 2027?",
      "USDA APHIS endorsement and MAPA acceptance",
      "Routing options: direct vs via Panama or Miami",
      "Sao Paulo and Rio arrival processes",
      "Parasite treatment and timing requirements",
      "FAQs about USA to Brazil pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-brazil/ (anchor: UK to Brazil routing)",
      "/airlines/latam-airlines/ (anchor: LATAM cargo)",
      "/countries/brazil/ (anchor: Brazil pet import overview)",
      "/cdc-dog-import-rules/ (anchor: CDC exit clearance)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Brazil — 2027",
      "Brazil MAPA Ministry of Agriculture pet import — 2026"
    ],
    ai_overview_play: "Latin America cross-border route adds breadth; named MAPA process is the operational specificity LLMs reward."
  },

  {
    id: "d170",
    day_number: 170,
    iso_date: "2027-01-28",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "brachycephalic",
    cluster_name: "Brachycephalic & breed-specific",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2300,
    title: "Snub-Nosed Cats and International Travel 2027: Persians, Exotics and Burmese in Cargo",
    title_tag: "Snub-Nosed Cat Air Travel 2027 | PetTransportGlobal",
    meta_description: "Air travel risks for Persian, Exotic Shorthair, Himalayan, and Burmese cats in 2027: airline embargoes, route choices, and how to reduce respiratory risk.",
    url_slug: "/snub-nosed-cat-air-travel/",
    primary_seo_keyword: "snub nosed cat air travel",
    primary_volume: 210,
    primary_kd: 24,
    secondary_seo_keywords: ["persian cat international travel", "exotic shorthair flight", "burmese cat cargo", "brachycephalic cat airline"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can my Persian cat fly cargo from London to Sydney in 2027 or do airlines refuse?" },
      { model: "Claude", phrasing: "Outline snub-nosed cat air travel risks 2027: airline embargoes for Persian, Exotic, Himalayan, and Burmese, plus how to minimise risk on accepted routes." },
      { model: "Gemini", phrasing: "Brachycephalic cat travel rules 2027" }
    ],
    direct_answer_40_60_words: "In 2027 several airlines restrict or refuse cargo travel for snub-nosed cat breeds including Persian, Exotic Shorthair, Himalayan, British Shorthair, and Burmese, citing higher respiratory and overheating risk. Restrictions vary by airline and route. Cabin travel for small cats remains possible on most carriers. Direct flights, cooler-month travel, and IATA-compliant ventilated crates reduce risk.",
    h2_outline: [
      "Why snub-nosed cats face travel restrictions in 2027",
      "Which breeds are flagged: Persian, Exotic, Himalayan, British Shorthair, Burmese",
      "Airline-by-airline acceptance for cabin and cargo",
      "Reducing respiratory and overheating risk",
      "Route and seasonal choices that help",
      "FAQs about snub-nosed cat air travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/brachycephalic-airline-rules/ (anchor: brachycephalic dog rules)",
      "/welfare-in-transit/ (anchor: welfare in transit)",
      "/long-haul-pet-flight-welfare/ (anchor: long-haul flight welfare)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate ventilation)"
    ],
    external_links: [
      "IATA Live Animals Regulations brachycephalic notes — 2027",
      "International Cat Care welfare guidance — 2026"
    ],
    ai_overview_play: "Cat-specific brachycephalic content is a content gap on competitor sites; clear LLM ranking opportunity."
  },

  {
    id: "d171",
    day_number: 171,
    iso_date: "2027-01-29",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "process-timeline",
    cluster_name: "Process timelines & how-to",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Shipping a Puppy Internationally 2027: Minimum Age, Welfare and Paperwork",
    title_tag: "Shipping Puppy Internationally 2027 | Age & Rules | PetTransportGlobal",
    meta_description: "Shipping a puppy internationally in 2027: minimum age limits by country, vaccination timing, fit-to-fly checks, and welfare considerations for young dogs.",
    url_slug: "/shipping-puppy-internationally/",
    primary_seo_keyword: "shipping puppy internationally",
    primary_volume: 720,
    primary_kd: 33,
    secondary_seo_keywords: ["puppy international flight age", "minimum age puppy travel", "puppy export uk", "ship puppy abroad welfare"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I fly an 8-week-old puppy from the UK to USA in 2027 or is it too young?" },
      { model: "Claude", phrasing: "Outline shipping a puppy internationally 2027: minimum age by destination, rabies vaccine timing constraints, fit-to-fly assessment, and welfare." },
      { model: "Gemini", phrasing: "Shipping puppy internationally minimum age 2027" },
      { model: "Perplexity", phrasing: "Minimum age for puppy international flight" }
    ],
    direct_answer_40_60_words: "Shipping a puppy internationally in 2027 is constrained by destination minimum age. Most countries require puppies to be at least 15 weeks old: 12 weeks for rabies vaccination plus a 21-day wait. The CDC requires dogs entering the USA to be at least 6 months old since 2024. Australia and New Zealand have additional titre and treatment timing constraints.",
    h2_outline: [
      "What shipping a puppy internationally involves in 2027",
      "Minimum age by destination: USA, EU, UK, AU, NZ, Asia, Gulf",
      "Why rabies vaccine timing controls puppy travel",
      "Fit-to-fly assessment and welfare considerations",
      "When breeders ship vs when owners should travel",
      "FAQs about shipping a puppy internationally"
    ],
    schema_required: ["Article", "HowTo", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cdc-dog-import-rules/ (anchor: CDC 6-month minimum age)",
      "/rabies-titre-test/ (anchor: rabies vaccine timing)",
      "/welfare-in-transit/ (anchor: puppy welfare)",
      "/pet-relocation-timeline/ (anchor: full timeline)",
      "/iata-pet-crate-requirements/ (anchor: crate sizing for growing puppies)"
    ],
    external_links: [
      "CDC Bringing a Dog into the United States minimum age — 2027",
      "DEFRA pet travel rules minimum age guidance — 2026"
    ],
    ai_overview_play: "720 vol head term with the CDC 6-month rule answered up-front; sustains AI Overview placement."
  }
);

/* ============================ MONTH 9: FEBRUARY 2027 (Days 172-191) — Chunk 11 ============================
   20 working days. No bank holidays. Final month of Q3.
   Theme: Africa & South Asia expansion, Latin America airlines, senior/first-timer welfare pillars, regional UK fill. */
window.PLAN_ROWS.push(
  {
    id: "d172",
    day_number: 172,
    iso_date: "2027-02-01",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "uk-regional",
    cluster_name: "UK regional service pages",
    intent: "Commercial",
    content_type: "Regional page",
    word_count_target: 1800,
    title: "Pet Transport Newcastle: International and UK-Wide Service from the North East 2027",
    title_tag: "Pet Transport Newcastle 2027 | North East | PetTransportGlobal",
    meta_description: "International and UK-wide pet transport from Newcastle in 2027: NCL cargo, AHC vets, multi-pet collection across the North East, and realistic costs.",
    url_slug: "/pet-transport-newcastle/",
    primary_seo_keyword: "pet transport newcastle",
    primary_volume: 210,
    primary_kd: 18,
    secondary_seo_keywords: ["dog transport newcastle", "pet courier north east", "newcastle airport pet cargo", "international pet move tyne"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Best way to ship a dog internationally from Newcastle in 2027 - direct or transfer to Manchester or Edinburgh?" },
      { model: "Claude", phrasing: "How pet transport from Newcastle works in 2027: AHC vets, NCL cargo limits, and ground transfer to Manchester or Edinburgh." },
      { model: "Gemini", phrasing: "Pet transport Newcastle international 2027" }
    ],
    direct_answer_40_60_words: "International pet transport from Newcastle in 2027 typically routes via Manchester or Edinburgh for cargo, with ground transfer added to total cost. Some EU-bound moves use Eurotunnel pickup. Local Tyne and Wear AHC vets handle paperwork. Realistic pricing ranges from around £1,400 for nearby EU destinations to £4,800-plus for Australia or New Zealand.",
    h2_outline: [
      "How does international pet transport from Newcastle work in 2027?",
      "NCL cargo limits vs ground transfer to Manchester or Edinburgh",
      "AHC vets across the North East",
      "Pickup zones: Newcastle, Sunderland, Durham, Northumberland",
      "Realistic costs by destination",
      "FAQs about pet transport from Newcastle"
    ],
    schema_required: ["Article", "Service", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-edinburgh/ (anchor: Edinburgh hub option)",
      "/pet-transport-manchester/ (anchor: Manchester hub option)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)"
    ],
    external_links: [
      "Newcastle Airport cargo information — 2027",
      "DEFRA Official Vet list North East — 2027"
    ],
    ai_overview_play: "North East regional gap filled; uk-regional cluster reaches 8 entries."
  },

  {
    id: "d173",
    day_number: 173,
    iso_date: "2027-02-02",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Morocco 2027: ONSSA Permit, Casablanca Process and Documentation",
    title_tag: "Morocco Pet Import 2027 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Morocco in 2027: ONSSA import authorisation, microchip and rabies rules, Casablanca arrival process and realistic timelines.",
    url_slug: "/countries/morocco/",
    primary_seo_keyword: "import pet to morocco",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["onssa pet permit", "dog import morocco", "casablanca pet airport", "morocco rabies certificate"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Morocco pet import involve in 2027 with ONSSA paperwork?" },
      { model: "Claude", phrasing: "Outline Morocco pet import 2027: ONSSA authorisation, microchip, rabies, and Casablanca Mohammed V Airport process." },
      { model: "Gemini", phrasing: "Morocco pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Morocco in 2027 requires authorisation from ONSSA, ISO microchip, current rabies vaccine, and an origin-country health certificate endorsed by the competent authority. Casablanca Mohammed V International Airport is the primary clearance hub. Marrakesh, Rabat and Tangier also accept pets. Same-day clearance is standard with no home quarantine if paperwork is complete.",
    h2_outline: [
      "What Morocco pet import requires in 2027",
      "ONSSA authorisation timing and process",
      "Microchip, rabies, and health certificate",
      "Casablanca, Marrakesh, Rabat and Tangier arrival",
      "Banned and restricted breeds",
      "FAQs about importing a pet to Morocco"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/egypt/ (anchor: compare Egypt rules)",
      "/airlines/royal-air-maroc/ (anchor: Royal Air Maroc cargo)",
      "/rabies-titre-test/ (anchor: rabies overview)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)"
    ],
    external_links: [
      "Morocco ONSSA Office National de Securite Sanitaire des Aliments — 2027",
      "Morocco Customs animal entry — 2026"
    ],
    ai_overview_play: "North African coverage extends; ONSSA process specificity rewards LLM trust."
  },

  {
    id: "d174",
    day_number: 174,
    iso_date: "2027-02-03",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport UK to Turkey: Istanbul Routes, Rabies Titre and 2027 Costs",
    title_tag: "UK to Turkey Pet Transport 2027 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Turkey in 2027: rabies titre requirement, Istanbul cargo, drive-via-Bulgaria option, and realistic transport costs.",
    url_slug: "/routes/uk-to-turkey/",
    primary_seo_keyword: "pet transport uk to turkey",
    primary_volume: 480,
    primary_kd: 28,
    secondary_seo_keywords: ["dog uk to turkey", "shipping cat to istanbul", "uk to turkey pet rules", "turkey rabies titre"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from London to Istanbul with a dog in 2027: rabies titre, Turkish Airlines cargo, and total cost." },
      { model: "Claude", phrasing: "Walk through UK to Turkey pet transport 2027: rabies titre window for non-EU country, Turkish Ministry permit, Istanbul arrival, and realistic costs." },
      { model: "Gemini", phrasing: "UK to Turkey pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Turkey costs roughly £1,400 to £2,800 in 2027 by professional courier. Turkey requires rabies vaccine plus a titre test for entry from countries outside its listed group, plus a Ministry of Agriculture permit. Turkish Airlines cargo to Istanbul is the most common routing. Driving via the EU and Bulgaria is possible but takes 4-5 days.",
    h2_outline: [
      "How much does UK to Turkey pet transport cost in 2027?",
      "Turkish Ministry permit and rabies titre window",
      "Turkish Airlines cargo vs ground via Bulgaria",
      "Istanbul, Ankara and Antalya arrival processes",
      "Banned and restricted breeds in Turkey",
      "FAQs about UK to Turkey pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/turkish-airlines/ (anchor: Turkish Airlines pet cargo)",
      "/rabies-titre-test/ (anchor: rabies titre window)",
      "/routes/uk-to-greece/ (anchor: ground route via Greece)",
      "/countries/turkey/ (anchor: Turkey pet import overview)"
    ],
    external_links: [
      "Turkish Ministry of Agriculture pet entry — 2027",
      "DEFRA pet travel UK to Turkey — 2027"
    ],
    ai_overview_play: "480 vol UK route corridor with the rabies titre nuance answered up-front."
  },

  {
    id: "d175",
    day_number: 175,
    iso_date: "2027-02-04",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Avianca Pet Travel 2027: Cabin and Cargo Rules to Bogota and Latin America",
    title_tag: "Avianca Pet Travel 2027 | Cabin & Cargo | PetTransportGlobal",
    meta_description: "Avianca pet travel in 2027: in-cabin allowances, cargo rules, Bogota hub handling, breed restrictions, and which Latin American routes accept pets.",
    url_slug: "/airlines/avianca/",
    primary_seo_keyword: "avianca pet travel",
    primary_volume: 590,
    primary_kd: 28,
    secondary_seo_keywords: ["avianca pet in cabin", "avianca cargo dog", "bogota pet flight", "av pet policy 2027"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I take my dog in cabin on Avianca from Madrid to Bogota in 2027?" },
      { model: "Claude", phrasing: "Summarise Avianca pet rules 2027: cabin weight, cargo eligibility on transatlantic and Latin America routes, and breed restrictions." },
      { model: "Gemini", phrasing: "Avianca pet travel rules 2027" }
    ],
    direct_answer_40_60_words: "Avianca accepts small dogs and cats in cabin in 2027 if pet plus carrier weighs 8 kg or less and fits under the seat. Larger pets travel as cargo on most routes through the Bogota hub. Breed restrictions apply to brachycephalic and certain banned breeds. Advance booking is required, and seasonal embargoes affect summer travel to high-altitude or hot destinations.",
    h2_outline: [
      "Avianca cabin pet rules and fees in 2027",
      "Avianca cargo programme via Bogota",
      "Brachycephalic and breed restrictions",
      "Routes that accept pets across Latin America",
      "Booking and check-in process",
      "FAQs about Avianca pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/latam-airlines/ (anchor: compare LATAM)",
      "/countries/colombia/ (anchor: Colombia import rules)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Avianca pet travel policy — 2027",
      "Colombia ICA Instituto Colombiano Agropecuario import — 2026"
    ],
    ai_overview_play: "590 vol Latin America carrier head term; pairs with Colombia and Argentina country guides."
  },

  {
    id: "d176",
    day_number: 176,
    iso_date: "2027-02-05",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "insurance",
    cluster_name: "Pet travel insurance & welfare",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Senior Dog International Travel 2027: Risks, Vet Sign-Off and Welfare",
    title_tag: "Senior Dog International Travel 2027 | PetTransportGlobal",
    meta_description: "International travel for senior dogs in 2027: vet fit-to-fly sign-off, age-related risks, sedation realities, and when to choose ground over air.",
    url_slug: "/senior-dog-international-travel/",
    primary_seo_keyword: "senior dog international travel",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["old dog international flight", "elderly pet relocation", "fit to fly senior dog", "senior pet airline rules"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "My 13-year-old Labrador needs to move from London to Sydney in 2027 - is air travel safe at her age?" },
      { model: "Claude", phrasing: "Walk through senior dog international travel 2027: vet fit-to-fly assessment, age-related risks in cargo, sedation guidance, and ground alternatives." },
      { model: "Gemini", phrasing: "Senior dog international travel 2027" }
    ],
    direct_answer_40_60_words: "Senior dog international travel in 2027 requires a vet fit-to-fly assessment within 10 days of travel covering cardiac, respiratory, joint and cognitive function. There is no maximum age set by IATA but airlines may decline based on the assessment. Sedation is discouraged. Direct flights, cooler-month travel, and IATA-compliant crates with extra padding reduce stress for older dogs.",
    h2_outline: [
      "Why senior dog international travel needs extra planning in 2027",
      "Vet fit-to-fly assessment: what's checked",
      "Cargo conditions and senior dog welfare",
      "Why sedation is discouraged for older dogs",
      "When ground transport beats air travel",
      "FAQs about senior dog international travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/welfare-in-transit/ (anchor: welfare in transit)",
      "/long-haul-pet-flight-welfare/ (anchor: long-haul welfare)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/pet-travel-insurance/ (anchor: insurance for senior pets)"
    ],
    external_links: [
      "AVMA pet sedation for air travel — 2026",
      "BSAVA senior dog welfare guidance — 2026"
    ],
    ai_overview_play: "Anxiety-driven query with high LLM cite rate; named-source vet guidance differentiates."
  },

  {
    id: "d177",
    day_number: 177,
    iso_date: "2027-02-08",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2400,
    title: "Pet Import to Mexico 2027: SENASICA Rules, Mexico City Process and Documentation",
    title_tag: "Mexico Pet Import 2027 | SENASICA | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Mexico in 2027: SENASICA OISA inspection, microchip and rabies rules, Mexico City and Cancun arrival, realistic timelines.",
    url_slug: "/countries/mexico/",
    primary_seo_keyword: "import pet to mexico",
    primary_volume: 720,
    primary_kd: 30,
    secondary_seo_keywords: ["senasica pet rules", "dog import mexico city", "cancun pet airport", "mexico pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Mexico pet import involve in 2027 - SENASICA inspection, banned breeds, and home quarantine?" },
      { model: "Claude", phrasing: "Outline Mexico pet import 2027: SENASICA OISA inspection at port of entry, microchip, rabies vaccine timing, and Mexico City vs Cancun process." },
      { model: "Gemini", phrasing: "Mexico pet import requirements 2027" },
      { model: "Perplexity", phrasing: "Do I need a permit to bring my dog to Mexico" }
    ],
    direct_answer_40_60_words: "Importing a pet to Mexico in 2027 requires SENASICA OISA inspection at the airport, ISO microchip recommended, current rabies vaccine for pets over three months old, and an origin-country health certificate within 15 days of travel. No advance permit is needed in most cases. Mexico City, Cancun, Guadalajara and Monterrey are primary clearance hubs with same-day approval.",
    h2_outline: [
      "What Mexico pet import requires in 2027",
      "SENASICA OISA inspection at port of entry",
      "Microchip, rabies, and health certificate",
      "Mexico City, Cancun, Guadalajara, Monterrey arrival",
      "Banned and restricted breeds",
      "FAQs about importing a pet to Mexico"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/usa-to-mexico/ (anchor: USA to Mexico routing)",
      "/airlines/aeromexico/ (anchor: Aeromexico cargo)",
      "/cdc-dog-import-rules/ (anchor: CDC exit clearance from USA)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)"
    ],
    external_links: [
      "Mexico SENASICA Servicio Nacional de Sanidad import — 2027",
      "Mexico OISA inspection guidance — 2026"
    ],
    ai_overview_play: "720 vol head term with no-advance-permit nuance LLMs love to surface."
  },

  {
    id: "d178",
    day_number: 178,
    iso_date: "2027-02-09",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Aeromexico Pet Travel 2027: Cabin and Cargo Rules to Mexico City and Beyond",
    title_tag: "Aeromexico Pet Travel 2027 | Cabin & Cargo | PetTransportGlobal",
    meta_description: "Aeromexico pet travel in 2027: in-cabin weight, cargo eligibility, Mexico City handling, breed restrictions, and routes between USA, Europe and Mexico.",
    url_slug: "/airlines/aeromexico/",
    primary_seo_keyword: "aeromexico pet travel",
    primary_volume: 480,
    primary_kd: 27,
    secondary_seo_keywords: ["aeromexico pet in cabin", "aeromexico cargo dog", "am pet policy 2027", "mexico city pet flight"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I take my cat in cabin on Aeromexico from JFK to Mexico City in 2027?" },
      { model: "Claude", phrasing: "Summarise Aeromexico pet rules 2027: cabin weight limits, cargo on transatlantic routes, and breed restrictions." },
      { model: "Gemini", phrasing: "Aeromexico pet travel 2027" }
    ],
    direct_answer_40_60_words: "Aeromexico accepts small dogs and cats in cabin in 2027 if pet plus carrier weighs 9 kg or less and fits under the seat. Larger pets travel as cargo on most international routes. Brachycephalic breeds face additional restrictions and seasonal embargoes affect summer travel into hot Mexican destinations. Advance booking is required at least 48 hours before departure.",
    h2_outline: [
      "Aeromexico cabin pet rules and fees 2027",
      "Aeromexico cargo programme",
      "Brachycephalic and breed restrictions",
      "Seasonal embargoes for summer Mexico arrivals",
      "Booking and check-in process",
      "FAQs about Aeromexico pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/mexico/ (anchor: Mexico pet import rules)",
      "/airlines/avianca/ (anchor: compare Avianca)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Aeromexico pet travel policy — 2027",
      "Mexico SENASICA pet import — 2027"
    ],
    ai_overview_play: "Mexico carrier complete; route + airline + country triangle for Mexico cluster."
  },

  {
    id: "d179",
    day_number: 179,
    iso_date: "2027-02-10",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to South Korea: Quarantine, Incheon Cargo and 2027 Costs",
    title_tag: "USA to South Korea Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to South Korea in 2027: APQA inspection, microchip and rabies rules, Incheon cargo handling, and realistic costs.",
    url_slug: "/routes/usa-to-south-korea/",
    primary_seo_keyword: "pet transport usa to south korea",
    primary_volume: 320,
    primary_kd: 30,
    secondary_seo_keywords: ["dog usa to seoul", "shipping cat usa to korea", "apqa pet inspection", "incheon pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from Los Angeles to Seoul with a dog in 2027: APQA, Korean Air or Asiana, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to South Korea pet transport 2027: USDA APHIS endorsement, APQA inspection at Incheon, and quarantine likelihood." },
      { model: "Gemini", phrasing: "USA to South Korea pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to South Korea costs roughly $2,800 to $5,200 in 2027 for a single dog flying Korean Air or Asiana cargo into Incheon. Korea requires ISO microchip, current rabies vaccine, rabies titre test for some origins, and APQA inspection on arrival. Quarantine is typically waived if paperwork is complete. USDA APHIS endorsement is required.",
    h2_outline: [
      "How much does USA to South Korea pet transport cost in 2027?",
      "USDA APHIS endorsement and Korean import requirements",
      "Korean Air vs Asiana cargo routing",
      "APQA Animal and Plant Quarantine Agency inspection",
      "Incheon arrival process",
      "FAQs about USA to South Korea pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/korean-air/ (anchor: Korean Air cargo)",
      "/airlines/asiana-airlines/ (anchor: Asiana cargo)",
      "/countries/south-korea/ (anchor: Korea pet import overview)",
      "/rabies-titre-test/ (anchor: rabies titre window)"
    ],
    external_links: [
      "USDA APHIS Pet Travel Korea — 2027",
      "Korea APQA Animal and Plant Quarantine Agency — 2026"
    ],
    ai_overview_play: "320 vol with named-process specificity; Korean Air + Asiana airline pages funnel here."
  },

  {
    id: "d180",
    day_number: 180,
    iso_date: "2027-02-11",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "process-timeline",
    cluster_name: "Process timelines & how-to",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "First-Time International Pet Shipper Checklist 2027: 30-Step Plan",
    title_tag: "First-Time Pet Shipper Checklist 2027 | PetTransportGlobal",
    meta_description: "A 30-step checklist for first-time international pet shippers in 2027: from microchip to arrival day, with realistic timing and cost markers throughout.",
    url_slug: "/first-time-pet-shipper-checklist/",
    primary_seo_keyword: "first time pet shipper checklist",
    primary_volume: 590,
    primary_kd: 30,
    secondary_seo_keywords: ["pet shipping checklist", "first time international pet move", "pet relocation step by step", "moving pet abroad first time"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I've never shipped a pet abroad before - can I get a complete step-by-step checklist for 2027?" },
      { model: "Claude", phrasing: "Build a 30-step first-time international pet shipper checklist 2027 from microchip through arrival, with realistic timing markers." },
      { model: "Gemini", phrasing: "First time pet shipper checklist 2027" },
      { model: "Perplexity", phrasing: "Step by step international pet shipping" }
    ],
    direct_answer_40_60_words: "A first-time international pet shipper in 2027 follows roughly 30 sequential steps: research destination at month minus 12, microchip, rabies vaccine, titre test where required, AHC vet booked, carrier selected at month minus 3, IATA crate fitted, paperwork finalised in final 10 days, then transit and arrival. Costs accumulate at every stage, so budget early.",
    h2_outline: [
      "Why a step-by-step plan matters for first-time pet shippers",
      "Steps 1 to 8: Months minus 12 to minus 6 (foundation paperwork)",
      "Steps 9 to 16: Months minus 6 to minus 3 (carrier and routing)",
      "Steps 17 to 24: Final month (paperwork and crate)",
      "Steps 25 to 30: Departure day to arrival",
      "Common first-timer mistakes to avoid",
      "FAQs about first-time international pet shipping"
    ],
    schema_required: ["Article", "HowTo", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-relocation-timeline/ (anchor: full 12-month timeline)",
      "/find-an-official-vet/ (anchor: Official Vet finder)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/cost-of-international-pet-transport/ (anchor: budget at each stage)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting checklist)"
    ],
    external_links: [
      "DEFRA pet travel step-by-step — 2027",
      "USDA APHIS Pet Travel pre-departure checklist — 2027"
    ],
    ai_overview_play: "590 vol checklist query with HowTo schema; ideal for AI Overview structured answers."
  },

  {
    id: "d181",
    day_number: 181,
    iso_date: "2027-02-12",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2300,
    title: "Pet Import to Sri Lanka 2027: DAPH Permit, Colombo Process and Quarantine",
    title_tag: "Sri Lanka Pet Import 2027 | DAPH Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Sri Lanka in 2027: DAPH import permit, microchip and rabies rules, Colombo airport quarantine reality, and realistic timelines.",
    url_slug: "/countries/sri-lanka/",
    primary_seo_keyword: "import pet to sri lanka",
    primary_volume: 210,
    primary_kd: 22,
    secondary_seo_keywords: ["daph pet permit sri lanka", "dog import colombo", "sri lanka rabies certificate", "colombo airport pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Sri Lanka pet import look like in 2027 - DAPH permit and home quarantine?" },
      { model: "Claude", phrasing: "Outline Sri Lanka pet import 2027: DAPH permit, microchip, rabies vaccine, parasite treatments, and Colombo Bandaranaike Airport process." },
      { model: "Gemini", phrasing: "Sri Lanka pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Sri Lanka in 2027 requires a DAPH import permit, ISO microchip, current rabies vaccine, rabies titre from non-listed origins, and parasite treatments. Bandaranaike International Airport at Colombo handles arrivals. Most pets clear within hours without home quarantine when paperwork is complete. Some non-listed origins may face short supervised quarantine pending titre verification.",
    h2_outline: [
      "What Sri Lanka pet import requires in 2027",
      "DAPH import permit application timing",
      "Microchip, rabies vaccine and titre testing",
      "Parasite treatments and timing",
      "Colombo Bandaranaike Airport arrival",
      "FAQs about importing a pet to Sri Lanka"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/india/ (anchor: compare India rules)",
      "/airlines/sri-lankan-airlines/ (anchor: Sri Lankan Airlines cargo)",
      "/rabies-titre-test/ (anchor: rabies titre overview)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)"
    ],
    external_links: [
      "Sri Lanka DAPH Department of Animal Production and Health — 2027",
      "Sri Lanka Customs animal entry — 2026"
    ],
    ai_overview_play: "South Asia coverage extends; rare topic with low competition for clear LLM ranking."
  },

  {
    id: "d182",
    day_number: 182,
    iso_date: "2027-02-15",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Morocco: Casablanca Cargo and 2027 Costs",
    title_tag: "UK to Morocco Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Morocco in 2027: ONSSA permit, AHC paperwork, Casablanca cargo, drive-via-Spain option and realistic costs.",
    url_slug: "/routes/uk-to-morocco/",
    primary_seo_keyword: "pet transport uk to morocco",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to morocco", "shipping cat to casablanca", "uk to morocco pet rules", "tangier ferry pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from London to Marrakesh with a dog in 2027: ONSSA, Royal Air Maroc, and total cost." },
      { model: "Claude", phrasing: "Walk through UK to Morocco pet transport 2027: ONSSA authorisation, AHC paperwork, and Casablanca cargo vs drive-and-ferry via Spain." },
      { model: "Gemini", phrasing: "UK to Morocco pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Morocco costs roughly £1,400 to £2,600 in 2027 by professional courier. Morocco requires an ONSSA authorisation, AHC paperwork, ISO microchip and current rabies vaccine. Royal Air Maroc cargo into Casablanca is the most common air routing. Driving through France and Spain to the Algeciras-Tangier ferry is feasible and takes 4-5 days.",
    h2_outline: [
      "How much does UK to Morocco pet transport cost in 2027?",
      "ONSSA authorisation and AHC paperwork",
      "Royal Air Maroc cargo vs drive-and-ferry via Spain",
      "Casablanca, Marrakesh and Tangier arrival",
      "Banned and restricted breeds",
      "FAQs about UK to Morocco pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/morocco/ (anchor: Morocco import overview)",
      "/airlines/royal-air-maroc/ (anchor: Royal Air Maroc cargo)",
      "/routes/uk-to-spain/ (anchor: UK-Spain ground stage)",
      "/eu-pet-travel-scheme/ (anchor: EU transit rules)"
    ],
    external_links: [
      "Morocco ONSSA pet entry — 2027",
      "DEFRA pet travel UK to Morocco — 2027"
    ],
    ai_overview_play: "Drive-and-ferry option is the operational nuance LLMs surface; second North African route after UK-Egypt potential."
  },

  {
    id: "d183",
    day_number: 183,
    iso_date: "2027-02-16",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 1900,
    title: "Garuda Indonesia Pet Travel 2027: Cargo Rules to Jakarta and Bali",
    title_tag: "Garuda Indonesia Pet Travel 2027 | Cargo | PetTransportGlobal",
    meta_description: "Garuda Indonesia pet travel in 2027: cargo rules, Jakarta and Bali handling, breed restrictions, and Indonesian import paperwork realities.",
    url_slug: "/airlines/garuda-indonesia/",
    primary_seo_keyword: "garuda indonesia pet travel",
    primary_volume: 170,
    primary_kd: 23,
    secondary_seo_keywords: ["garuda cargo dog", "jakarta pet flight", "bali pet airline", "ga pet policy 2027"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship a dog as cargo with Garuda Indonesia from Amsterdam to Jakarta in 2027?" },
      { model: "Claude", phrasing: "Summarise Garuda Indonesia pet cargo rules 2027 plus Indonesian Ministry of Agriculture import paperwork." },
      { model: "Gemini", phrasing: "Garuda Indonesia pet cargo 2027" }
    ],
    direct_answer_40_60_words: "Garuda Indonesia carries dogs and cats only as manifested cargo in 2027, with no in-cabin pet option on most routes. Indonesia requires Ministry of Agriculture import permit, ISO microchip, current rabies vaccine, and rabies titre testing. Jakarta and Denpasar are primary clearance hubs. Brachycephalic and certain banned breeds cannot travel as cargo on Garuda.",
    h2_outline: [
      "Garuda Indonesia cargo programme for pets in 2027",
      "Indonesian Ministry of Agriculture import requirements",
      "Jakarta and Bali Denpasar arrival processes",
      "Brachycephalic and breed restrictions",
      "Booking and routing options",
      "FAQs about Garuda Indonesia pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/countries/indonesia/ (anchor: Indonesia import rules)",
      "/airlines/singapore-airlines/ (anchor: alternative Singapore routing)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Garuda Indonesia cargo live animals — 2027",
      "Indonesian Ministry of Agriculture pet import — 2026"
    ],
    ai_overview_play: "South East Asia carrier coverage; pairs with existing Indonesia country guide."
  },

  {
    id: "d184",
    day_number: 184,
    iso_date: "2027-02-17",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "quarantine",
    cluster_name: "Quarantine countries & rules",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2600,
    title: "Pet Quarantine Countries 2027: Where Dogs and Cats Still Face Mandatory Holding",
    title_tag: "Pet Quarantine Countries 2027 | Full List | PetTransportGlobal",
    meta_description: "Which countries still require pet quarantine in 2027: Australia, New Zealand, Hong Kong, Hawaii, Iceland and others, with realistic durations and costs.",
    url_slug: "/pet-quarantine-countries/",
    primary_seo_keyword: "pet quarantine countries",
    primary_volume: 1300,
    primary_kd: 38,
    secondary_seo_keywords: ["countries with pet quarantine 2027", "mandatory pet quarantine list", "quarantine free countries pet", "dog quarantine on arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Which countries still quarantine dogs and cats on arrival in 2027 and how long is each?" },
      { model: "Claude", phrasing: "List all countries with mandatory pet quarantine in 2027 with durations: Australia, NZ, HK, Hawaii, Iceland, Norway in some scenarios, and others." },
      { model: "Gemini", phrasing: "Pet quarantine countries 2027" },
      { model: "Perplexity", phrasing: "Where do dogs need quarantine on arrival" }
    ],
    direct_answer_40_60_words: "In 2027 mandatory pet quarantine still applies on arrival in: Australia (10 days minimum at Mickleham), New Zealand (10 days at Auckland), Hong Kong (4 months for non-listed origins), Hawaii (5-day or direct release), Iceland (14 days), and certain non-listed-origin entries to Singapore and Malaysia. Many other countries waive quarantine if paperwork is complete.",
    h2_outline: [
      "What pet quarantine actually means in 2027",
      "Australia: 10-day minimum at Mickleham",
      "New Zealand: 10 days at Auckland Quarantine Animal Centre",
      "Hong Kong: 4-month rule for non-listed origins",
      "Hawaii: 5-day or direct release",
      "Iceland: 14-day mandatory holding",
      "Borderline cases: Singapore, Malaysia, Taiwan",
      "Quarantine-free destinations and why",
      "FAQs about pet quarantine countries"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-australia/ (anchor: Mickleham quarantine)",
      "/routes/uk-to-new-zealand/ (anchor: Auckland quarantine)",
      "/routes/uk-to-hong-kong/ (anchor: Hong Kong 4-month rule)",
      "/rabies-titre-test/ (anchor: titre window controls quarantine)",
      "/pet-relocation-timeline/ (anchor: timeline for quarantine destinations)"
    ],
    external_links: [
      "DAFF Australia post-arrival quarantine — 2027",
      "MPI New Zealand quarantine — 2027",
      "Hong Kong AFCD quarantine — 2026"
    ],
    ai_overview_play: "1300 vol head term with the comprehensive list LLMs cite; quarantine cluster gets its anchor pillar."
  },

  {
    id: "d185",
    day_number: 185,
    iso_date: "2027-02-18",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2400,
    title: "Pet Import to Kenya 2027: DVS Permit, Nairobi Process and Rabies Rules",
    title_tag: "Kenya Pet Import 2027 | DVS Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Kenya in 2027: Directorate of Veterinary Services permit, microchip and rabies rules, JKIA Nairobi process, realistic timelines.",
    url_slug: "/countries/kenya/",
    primary_seo_keyword: "import pet to kenya",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["kenya dvs pet permit", "dog import nairobi", "jkia pet arrival", "kenya rabies certificate"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Kenya pet import involve in 2027 - DVS permit and Nairobi airport process?" },
      { model: "Claude", phrasing: "Outline Kenya pet import 2027: DVS permit, microchip, rabies, parasite treatments, and JKIA arrival." },
      { model: "Gemini", phrasing: "Kenya pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Kenya in 2027 requires a Directorate of Veterinary Services import permit, ISO microchip, current rabies vaccine, parasite treatments and an origin-country health certificate. Jomo Kenyatta International Airport in Nairobi handles arrivals with same-day clearance. No mandatory quarantine if paperwork is complete. Mombasa and Eldoret also accept pet arrivals on selected airlines.",
    h2_outline: [
      "What Kenya pet import requires in 2027",
      "DVS Directorate of Veterinary Services permit",
      "Microchip, rabies vaccine and parasite treatments",
      "Jomo Kenyatta International Airport arrival",
      "Banned and restricted breeds",
      "FAQs about importing a pet to Kenya"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/kenya-airways/ (anchor: Kenya Airways cargo)",
      "/airlines/ethiopian-airlines/ (anchor: Ethiopian via Addis)",
      "/countries/south-africa/ (anchor: compare South Africa rules)",
      "/rabies-titre-test/ (anchor: rabies overview)"
    ],
    external_links: [
      "Kenya Directorate of Veterinary Services pet import — 2027",
      "Kenya Civil Aviation Authority animal handling — 2026"
    ],
    ai_overview_play: "East Africa expansion; pairs naturally with Kenya Airways pillar tomorrow and Ethiopian Airlines from Jan."
  },

  {
    id: "d186",
    day_number: 186,
    iso_date: "2027-02-19",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "airline-pet-policies",
    cluster_name: "Airline pet policies",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2000,
    title: "Kenya Airways Pet Travel 2027: Cargo Rules to Nairobi and Africa Network",
    title_tag: "Kenya Airways Pet Travel 2027 | Cargo | PetTransportGlobal",
    meta_description: "Kenya Airways pet travel in 2027: cargo rules, Nairobi JKIA hub, breed restrictions, and which African and intercontinental routes accept pets.",
    url_slug: "/airlines/kenya-airways/",
    primary_seo_keyword: "kenya airways pet travel",
    primary_volume: 260,
    primary_kd: 25,
    secondary_seo_keywords: ["kenya airways cargo dog", "kq pet policy 2027", "nairobi pet flight", "africa pet airline"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship a dog with Kenya Airways from London to Nairobi in 2027?" },
      { model: "Claude", phrasing: "Summarise Kenya Airways pet cargo rules 2027 covering African network and breed restrictions." },
      { model: "Gemini", phrasing: "Kenya Airways pet cargo 2027" }
    ],
    direct_answer_40_60_words: "Kenya Airways carries dogs and cats only as manifested cargo in 2027, with no in-cabin pet option. The Nairobi JKIA hub serves a wide African network and direct routes to London, Amsterdam, Paris and the Gulf. Brachycephalic and certain banned breeds cannot travel as cargo. Bookings require at least seven days advance notice.",
    h2_outline: [
      "Kenya Airways cargo programme for pets in 2027",
      "Nairobi JKIA hub and African network reach",
      "Brachycephalic and breed restrictions",
      "Direct routes that accept pets to and from Europe",
      "Booking process and welfare during transit",
      "FAQs about Kenya Airways pet travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/ethiopian-airlines/ (anchor: compare Ethiopian)",
      "/countries/kenya/ (anchor: Kenya pet import rules)",
      "/iata-pet-crate-requirements/ (anchor: IATA crate sizing)",
      "/brachycephalic-airline-rules/ (anchor: brachycephalic airline rules)"
    ],
    external_links: [
      "Kenya Airways cargo live animals — 2027",
      "Kenya Civil Aviation Authority — 2026"
    ],
    ai_overview_play: "Africa airline duo (Ethiopian + Kenya) covers the continent; high-trust LLM topic cluster."
  },

  {
    id: "d187",
    day_number: 187,
    iso_date: "2027-02-22",
    day_of_week: "Mon",
    quarter: "Q3",
    cluster_id: "routes-cross-border",
    cluster_name: "Cross-border routes (non-UK)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to India: AQCS, Mumbai Cargo and 2027 Costs",
    title_tag: "USA to India Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to India in 2027: AQCS NOC, microchip and rabies rules, Mumbai and Delhi cargo handling, and realistic transport costs.",
    url_slug: "/routes/usa-to-india/",
    primary_seo_keyword: "pet transport usa to india",
    primary_volume: 480,
    primary_kd: 30,
    secondary_seo_keywords: ["dog usa to india", "shipping cat usa to mumbai", "aqcs noc india", "delhi pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from California to Bangalore with a dog in 2027: AQCS NOC, Air India, and total cost." },
      { model: "Claude", phrasing: "Walk through USA to India pet transport 2027: USDA APHIS endorsement, AQCS NOC application, Mumbai and Delhi arrival, and quarantine reality." },
      { model: "Gemini", phrasing: "USA to India pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to India costs roughly $2,800 to $5,400 in 2027 for a single dog by cargo flight to Mumbai or Delhi. India requires an AQCS NOC, ISO microchip, current rabies vaccine, USDA-endorsed health certificate within 10 days, and a five-week prior import application. Personal-effects route limits apply. Quarantine is rare with complete paperwork.",
    h2_outline: [
      "How much does USA to India pet transport cost in 2027?",
      "AQCS NOC application and timing",
      "USDA APHIS endorsement requirements",
      "Mumbai vs Delhi vs Bangalore arrival",
      "Personal-effects rule and pet limits per traveller",
      "FAQs about USA to India pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-india/ (anchor: UK to India routing)",
      "/airlines/air-india/ (anchor: Air India cargo)",
      "/countries/india/ (anchor: India import overview)",
      "/cdc-dog-import-rules/ (anchor: CDC exit clearance)"
    ],
    external_links: [
      "USDA APHIS Pet Travel India — 2027",
      "India AQCS Animal Quarantine and Certification Services — 2026"
    ],
    ai_overview_play: "480 vol diaspora corridor; AQCS NOC named-process specificity wins LLM placement."
  },

  {
    id: "d188",
    day_number: 188,
    iso_date: "2027-02-23",
    day_of_week: "Tue",
    quarter: "Q3",
    cluster_id: "cargo-cabin-choice",
    cluster_name: "Cargo vs cabin & accompanied baggage",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Cargo vs Accompanied Baggage vs Cabin 2027: Which Option for Your Pet",
    title_tag: "Cargo vs Accompanied Baggage 2027 | PetTransportGlobal",
    meta_description: "Comparing pet travel options in 2027: cabin, accompanied baggage, and manifested cargo. Cost, availability, welfare, and which suits your pet best.",
    url_slug: "/cargo-vs-accompanied-baggage-cabin/",
    primary_seo_keyword: "cargo vs accompanied baggage pet",
    primary_volume: 590,
    primary_kd: 31,
    secondary_seo_keywords: ["pet checked baggage airline", "manifested cargo pet", "in cabin vs cargo dog", "pet travel options compared"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the difference between cargo, accompanied baggage, and in-cabin for my dog in 2027 and which is safest?" },
      { model: "Claude", phrasing: "Compare pet travel options 2027: cabin, accompanied baggage and manifested cargo, with welfare, cost and availability tradeoffs." },
      { model: "Gemini", phrasing: "Cargo vs accompanied baggage pet 2027" }
    ],
    direct_answer_40_60_words: "In 2027 there are three pet flight options: in-cabin (small pets only, you keep control), accompanied baggage (medium pets in cargo on the same flight as the owner), and manifested cargo (the standard for international moves, often unaccompanied). Cabin is cheapest, cargo is the only option for many countries, and accompanied baggage sits in between with mixed availability.",
    h2_outline: [
      "What each pet flight option means in 2027",
      "In-cabin: weight limits, country restrictions",
      "Accompanied baggage: airlines that still offer it",
      "Manifested cargo: the international standard",
      "Cost, welfare, and availability compared",
      "Which option fits your pet and route",
      "FAQs about pet flight options"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cargo-vs-cabin-pet-travel/ (anchor: original cargo vs cabin)",
      "/iata-pet-crate-requirements/ (anchor: crate sizing for cargo)",
      "/welfare-in-transit/ (anchor: welfare in transit)",
      "/long-haul-pet-flight-welfare/ (anchor: long-haul welfare)"
    ],
    external_links: [
      "IATA Live Animals Regulations classification — 2027",
      "DEFRA pet travel cargo vs baggage — 2027"
    ],
    ai_overview_play: "590 vol comparison query with three-way breakdown that LLMs structure into AI Overview cards."
  },

  {
    id: "d189",
    day_number: 189,
    iso_date: "2027-02-24",
    day_of_week: "Wed",
    quarter: "Q3",
    cluster_id: "country-import-rules",
    cluster_name: "Country import rule guides",
    intent: "Informational",
    content_type: "Country guide",
    word_count_target: 2400,
    title: "Pet Import to Pakistan 2027: Permit, Karachi Process and Banned Breeds",
    title_tag: "Pakistan Pet Import 2027 | Rules | PetTransportGlobal",
    meta_description: "Importing a dog or cat to Pakistan in 2027: Ministry of National Food Security permit, microchip and rabies rules, Karachi and Lahore process, banned breeds.",
    url_slug: "/countries/pakistan/",
    primary_seo_keyword: "import pet to pakistan",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["pakistan pet permit", "dog import karachi", "pakistan banned dog breeds", "lahore pet airport"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Pakistan pet import involve in 2027 - permit, banned breeds, and quarantine?" },
      { model: "Claude", phrasing: "Outline Pakistan pet import 2027: Ministry of National Food Security permit, microchip, rabies, banned breed list, and Karachi/Lahore process." },
      { model: "Gemini", phrasing: "Pakistan pet import requirements 2027" }
    ],
    direct_answer_40_60_words: "Importing a pet to Pakistan in 2027 requires a Ministry of National Food Security and Research import permit, ISO microchip, current rabies vaccine, and an origin-country health certificate. Banned breeds include Pit Bull Terrier and certain mastiff varieties under provincial laws. Karachi and Lahore are primary clearance hubs with same-day approval and no mandatory home quarantine.",
    h2_outline: [
      "What Pakistan pet import requires in 2027",
      "Ministry of National Food Security permit",
      "Microchip, rabies, and health certificate timing",
      "Banned and restricted breeds in Pakistan",
      "Karachi, Lahore and Islamabad arrival",
      "FAQs about importing a pet to Pakistan"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/pia-pakistan-international/ (anchor: PIA cargo)",
      "/routes/uae-to-pakistan/ (anchor: UAE to Pakistan route)",
      "/breeds/banned-dog-breeds-by-country/ (anchor: banned breed reference)",
      "/rabies-titre-test/ (anchor: rabies overview)"
    ],
    external_links: [
      "Pakistan Ministry of National Food Security and Research — 2027",
      "Pakistan Customs animal entry — 2026"
    ],
    ai_overview_play: "South Asia diaspora corridor; named ministry plus banned breed list earns trust."
  },

  {
    id: "d190",
    day_number: 190,
    iso_date: "2027-02-25",
    day_of_week: "Thu",
    quarter: "Q3",
    cluster_id: "quote-agency-choice",
    cluster_name: "Choose-an-agency vetting & comparison",
    intent: "Commercial",
    content_type: "Pillar guide",
    word_count_target: 2500,
    title: "Pet Relocation Company Red Flags vs Green Flags 2027: How to Vet Before Paying",
    title_tag: "Pet Relocation Red Flags 2027 | Vetting Guide | PetTransportGlobal",
    meta_description: "How to spot dodgy pet relocation companies in 2027: red flags including no IATA membership, vague pricing, and no insurance, vs green flags that prove credibility.",
    url_slug: "/pet-relocation-red-flags/",
    primary_seo_keyword: "pet relocation red flags",
    primary_volume: 590,
    primary_kd: 27,
    secondary_seo_keywords: ["pet shipping scam", "dodgy pet courier", "iata pet shipper check", "vet pet relocation company"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How do I spot a dodgy pet relocation company in 2027 before paying a deposit?" },
      { model: "Claude", phrasing: "List red and green flags for vetting pet relocation companies 2027: IATA membership, IPATA, insurance, pricing transparency, contracts." },
      { model: "Gemini", phrasing: "Pet relocation company red flags 2027" },
      { model: "Perplexity", phrasing: "How to avoid pet shipping scams" }
    ],
    direct_answer_40_60_words: "Red flags for pet relocation companies in 2027 include no IATA cargo agent or IPATA membership, deposits over 50% upfront, vague pricing, no liability insurance, no formal contract, and refusal to name handling agents at each leg. Green flags include published IATA/IPATA numbers, itemised quotes, named carriers and agents, transparent terms, and willingness to accept staged payments.",
    h2_outline: [
      "Why vetting matters more in 2027",
      "Red flags: paperwork, payment, and pricing",
      "Red flags: communication, contracts, and aftercare",
      "Green flags: credentials, transparency, accountability",
      "Questions to ask before paying any deposit",
      "What to do if you suspect a scam after paying",
      "FAQs about pet relocation company vetting"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/how-to-choose-a-pet-transport-company/ (anchor: full vetting checklist)",
      "/cheap-pet-transport-red-flags/ (anchor: cheap quote red flags)",
      "/agency-vs-diy-pet-transport/ (anchor: agency vs DIY)",
      "/vetting-framework/ (anchor: Bronze/Silver/Gold framework)"
    ],
    external_links: [
      "IPATA International Pet and Animal Transportation Association — 2027",
      "IATA Cargo Agency Directory — 2027"
    ],
    ai_overview_play: "590 vol vetting query with concrete IPATA/IATA verifiable signals; commercial-intent jackpot."
  },

  {
    id: "d191",
    day_number: 191,
    iso_date: "2027-02-26",
    day_of_week: "Fri",
    quarter: "Q3",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Brazil: Sao Paulo Cargo, MAPA Rules and 2027 Costs",
    title_tag: "UK to Brazil Pet Transport 2027 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Brazil in 2027: AHC paperwork, MAPA international veterinary certificate, Sao Paulo cargo, and realistic costs.",
    url_slug: "/routes/uk-to-brazil/",
    primary_seo_keyword: "pet transport uk to brazil",
    primary_volume: 210,
    primary_kd: 26,
    secondary_seo_keywords: ["dog uk to brazil", "shipping cat to sao paulo", "uk to brazil pet rules", "rio pet arrival"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from London to Sao Paulo with a dog in 2027: AHC, MAPA, and total cost." },
      { model: "Claude", phrasing: "Walk through UK to Brazil pet transport 2027: AHC paperwork, MAPA international veterinary certificate, and Guarulhos arrival." },
      { model: "Gemini", phrasing: "UK to Brazil pet transport cost 2027" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Brazil costs roughly £2,400 to £4,400 in 2027 for a single dog by cargo flight to Sao Paulo Guarulhos or Rio Galeao. The UK AHC must be endorsed by APHA and accompanied by Brazil's international veterinary certificate. Two rabies vaccines, ISO microchip and parasite treatments are required. No quarantine if paperwork is correct.",
    h2_outline: [
      "How much does UK to Brazil pet transport cost in 2027?",
      "AHC plus MAPA international veterinary certificate",
      "Routing options: direct vs via Madrid or Lisbon",
      "Sao Paulo and Rio arrival processes",
      "Parasite treatment timing",
      "FAQs about UK to Brazil pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/usa-to-brazil/ (anchor: USA to Brazil routing)",
      "/airlines/latam-airlines/ (anchor: LATAM cargo)",
      "/airlines/iberia/ (anchor: Iberia via Madrid)",
      "/countries/brazil/ (anchor: Brazil import overview)"
    ],
    external_links: [
      "Brazil MAPA Ministry of Agriculture pet import — 2027",
      "DEFRA pet travel UK to Brazil — 2027"
    ],
    ai_overview_play: "Q3 closes with a Latin America corridor; pairs with USA-Brazil and Brazil country pages."
  }
);
