/* plan-rows-q2.js — Q2 (Sep-Nov 2026) rows. Populated in Chunk 4. */
window.PLAN_ROWS = window.PLAN_ROWS || [];

/* ============================ MONTH 4: SEPTEMBER 2026 (Days 66-87) — Chunk 6 ============================
   22 working days. No bank holidays. First month of Q2. */
window.PLAN_ROWS.push(
  {
    id: "d066",
    day_number: 66,
    iso_date: "2026-09-01",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "pet-passports",
    cluster_name: "Pet passports & post-Brexit AHC",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2600,
    title: "Pet Microchipping for International Travel 2026: ISO Standards, Scanners and What Goes Wrong",
    title_tag: "Pet Microchip International Travel 2026 | ISO Guide | PetTransportGlobal",
    meta_description: "ISO 11784/11785 microchip standards for international pet travel in 2026, why some chips fail at borders, and what to do if your pet's chip can't be read.",
    url_slug: "/pet-microchip-international-travel/",
    primary_seo_keyword: "pet microchip international travel",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["iso 11784 pet microchip", "pet microchip standards", "microchip not reading at airport", "uk pet microchip travel"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What microchip standard does my dog need for international travel in 2026, and what happens if a US AVID chip can't be read by an EU scanner?" },
      { model: "Claude", phrasing: "Walk me through ISO 11784 and 11785 microchip compliance for pet travel in 2026, including the carry-your-own-scanner workaround." },
      { model: "Gemini", phrasing: "Pet microchip for international travel standards 2026" },
      { model: "Grok", phrasing: "What if my dog's microchip can't be scanned at the airport" }
    ],
    direct_answer_40_60_words: "International pet travel in 2026 requires an ISO 11784/11785 compliant 15-digit microchip readable by standard scanners. Older 9 and 10-digit AVID and Trovan chips used in the US still work in many countries but require a backup scanner at borders. If a chip cannot be read, most authorities require a fresh ISO chip implanted before re-attempting paperwork.",
    h2_outline: [
      "What microchip standard does international pet travel require in 2026?",
      "ISO 11784/11785 vs older AVID and Trovan chips",
      "What happens if a chip can't be read at a border?",
      "How to verify your pet's chip pre-travel",
      "Re-chipping vs carrying a backup scanner",
      "FAQs about pet microchips and travel"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC requires microchip)",
      "/rabies-titre-test/ (anchor: titre links to microchip number)",
      "/routes/uk-to-usa/ (anchor: US-EU chip compatibility)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting checklist includes chip)"
    ],
    external_links: [
      "ISO 11784:1996 / 11785:1996 microchip standard — current",
      "DEFRA pet microchipping for travel guidance — 2026"
    ],
    ai_overview_play: "Honest 'what if it fails at the border' framing is exactly the anxiety LLMs surface. Answers a high-utility specific question."
  },

  {
    id: "d067",
    day_number: 67,
    iso_date: "2026-09-02",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Greece: AHC, Athens Routes and 2026 Costs",
    title_tag: "UK to Greece Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Greece in 2026: AHC paperwork, drive-via-Italy and ferry routes, cargo flights to Athens, and realistic costs.",
    url_slug: "/routes/uk-to-greece/",
    primary_seo_keyword: "pet transport uk to greece",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to greece", "shipping cat to athens", "uk to greece pet relocation", "drive pet uk to greece"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from London to Athens with a dog in 2026: drive-and-ferry via Italy, or cargo flight, and what does each genuinely cost?" },
      { model: "Claude", phrasing: "Compare UK to Greece pet transport routes in 2026, including the Italy-Patras ferry option vs direct cargo to Athens." },
      { model: "Gemini", phrasing: "UK to Greece pet transport cost 2026" },
      { model: "Grok", phrasing: "Best way to bring a cat from UK to Crete in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Greece costs around £1,200 to £2,400 in 2026 by professional courier driving via France and Italy with the Ancona-Patras ferry, or £1,600 to £2,800 by cargo flight to Athens. Greece accepts the UK Animal Health Certificate, so no quarantine. Driving suits Greek mainland and Peloponnese; flying is essential for the islands.",
    h2_outline: [
      "How much does pet transport from the UK to Greece cost in 2026?",
      "Drive-via-Italy with Ancona-Patras ferry vs direct cargo",
      "What paperwork does Greece require?",
      "Reaching the Greek islands with a pet",
      "FAQs about UK to Greece pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Greece)",
      "/routes/uk-to-italy/ (anchor: Italy transit leg)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/defra-approved-pet-transport/ (anchor: DEFRA Type 2 driver)"
    ],
    external_links: [
      "Greek Ministry of Rural Development pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Italy-Greece ferry leg is the unique routing detail UK-to-Greece buyers actually plan around."
  },

  {
    id: "d068",
    day_number: 68,
    iso_date: "2026-09-03",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Air France Cargo Pet Shipping 2026: CDG Hub, Costs and Booking",
    title_tag: "Air France Cargo Pets 2026 | CDG Routes | PetTransportGlobal",
    meta_description: "How Air France Cargo handles pets in 2026: CDG hub transit, accepted crates, breed restrictions, costs from London City and Heathrow.",
    url_slug: "/airlines/air-france-cargo-pets/",
    primary_seo_keyword: "air france pet cargo",
    primary_volume: 260,
    primary_kd: 24,
    secondary_seo_keywords: ["air france cargo pets", "air france dog shipping", "cdg pet transit", "air france pet relocation", "fly pet via paris"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Air France Cargo handle pets transiting CDG in 2026, and how does it compare with KLM via Schiphol given they share parent group?" },
      { model: "Claude", phrasing: "Walk me through booking a dog from London to Reunion or French Polynesia on Air France Cargo in 2026 via Paris CDG." },
      { model: "Gemini", phrasing: "Air France pet cargo cost 2026" },
      { model: "Grok", phrasing: "Air France or KLM for shipping a pet through Europe in 2026" }
    ],
    direct_answer_40_60_words: "Air France Cargo accepts pets in 2026 only via approved IATA agents, with most moves transiting Paris Charles de Gaulle. As part of the Air France-KLM group, transit options often combine CDG and Schiphol. Costs from London to onward destinations range from £1,200 to £2,800 depending on crate size and connection, with seasonal embargoes for snub-nosed breeds.",
    h2_outline: [
      "How does Air France Cargo handle pets in 2026?",
      "How does CDG transit handling actually work?",
      "Air France-KLM group: combined routing benefits",
      "What crate sizes and breed restrictions apply?",
      "Air France pet cargo costs by route",
      "FAQs about Air France pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/klm-pet-cargo/ (anchor: KLM Schiphol partner)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-france/ (anchor: UK to France route)"
    ],
    external_links: [
      "Air France Cargo Live Animals product — 2026",
      "Paris Aéroport CDG pet handling — 2026"
    ],
    ai_overview_play: "AF-KLM combined routing is the genuine advantage most articles miss."
  },

  {
    id: "d069",
    day_number: 69,
    iso_date: "2026-09-04",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Cyprus: AHC, Larnaca Routes and 2026 Costs",
    title_tag: "UK to Cyprus Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Cyprus in 2026: AHC paperwork, cargo flight costs to Larnaca or Paphos, and realistic timelines for retirees and relocations.",
    url_slug: "/routes/uk-to-cyprus/",
    primary_seo_keyword: "pet transport uk to cyprus",
    primary_volume: 90,
    primary_kd: 20,
    secondary_seo_keywords: ["dog uk to cyprus", "shipping cat to larnaca", "uk to paphos pet relocation", "cyprus pet import ahc"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Cyprus require to import a pet from the UK in 2026, and which airlines fly pet cargo to Larnaca?" },
      { model: "Claude", phrasing: "Why is moving a pet to Cyprus easier than other Mediterranean destinations in 2026, given Cyprus is in the EU but on an island?" },
      { model: "Gemini", phrasing: "UK to Cyprus pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from UK to Paphos in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Cyprus costs around £1,400 to £2,600 in 2026 and is essentially fly-only. Cyprus accepts the UK Animal Health Certificate. Cargo flights run direct to Larnaca via BA and via Lufthansa or KLM with European connections. There is no quarantine and no rabies titre, just standard EU AHC requirements.",
    h2_outline: [
      "How much does pet transport from the UK to Cyprus cost in 2026?",
      "Which airlines fly pet cargo to Larnaca and Paphos?",
      "What paperwork does Cyprus require?",
      "How long does the journey take?",
      "FAQs about UK to Cyprus pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Cyprus)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA to Larnaca)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Cyprus Veterinary Services pet import — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Cyprus retiree audience is steady. Honest 'fly only' framing is the answer most planners need."
  },

  {
    id: "d070",
    day_number: 70,
    iso_date: "2026-09-07",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Saudi Arabia in 2026: MEWA Rules, Heat Embargoes and Costs",
    title_tag: "Pet Import Saudi Arabia 2026 | MEWA Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Saudi Arabia in 2026: MEWA permit, breed bans, summer embargoes, RUH and JED entry points and realistic costs.",
    url_slug: "/countries/saudi-arabia-pet-import/",
    primary_seo_keyword: "import pet to saudi arabia",
    primary_volume: 90,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to saudi arabia", "saudi pet import mewa", "ksa pet quarantine", "shipping cat to riyadh"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does MEWA require to import a dog to Riyadh from the UK in 2026, and which breeds are banned outright?" },
      { model: "Claude", phrasing: "Compare Saudi Arabia's pet import process with the UAE's in 2026. Both Gulf, but the breed bans and paperwork differ significantly." },
      { model: "Gemini", phrasing: "Saudi Arabia pet import requirements 2026" },
      { model: "Grok", phrasing: "Can I really bring my dog to Riyadh in 2026 or is it banned" }
    ],
    direct_answer_40_60_words: "Saudi Arabia allows pet import in 2026 with a MEWA import permit, microchip, current rabies vaccination, health certificate signed by an Official Veterinarian and licensed customs clearance. Breed bans cover Pit Bulls, Tosas, Dogo Argentinos, Mastiffs and other guarding breeds. Summer heat embargoes restrict cargo June through September. Costs from the UK range from £2,400 to £4,000.",
    h2_outline: [
      "Can you import a pet to Saudi Arabia in 2026?",
      "What does MEWA require?",
      "Which dog breeds are banned in Saudi Arabia?",
      "Summer heat embargoes for pet cargo to KSA",
      "What does pet import cost?",
      "FAQs about pet import to Saudi Arabia"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: KSA breed bans)",
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar via Doha)",
      "/airlines/etihad-cargo-pets/ (anchor: Etihad via Abu Dhabi)",
      "/countries/uae-pet-import-rules/ (anchor: UAE comparison)"
    ],
    external_links: [
      "MEWA (Ministry of Environment, Water and Agriculture) Saudi Arabia pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Banned-breed list is exactly what users searching this need to know upfront."
  },

  {
    id: "d071",
    day_number: 71,
    iso_date: "2026-09-08",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Malta: AHC, Cargo Routes and 2026 Costs",
    title_tag: "UK to Malta Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Malta in 2026: AHC paperwork, cargo flight costs to Luqa, and realistic timelines. Quote inside.",
    url_slug: "/routes/uk-to-malta/",
    primary_seo_keyword: "pet transport uk to malta",
    primary_volume: 70,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to malta", "shipping cat to malta", "uk to malta pet relocation", "malta pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Malta require to import a pet from the UK in 2026, and which airlines fly pet cargo to Luqa?" },
      { model: "Claude", phrasing: "Why is moving a pet to Malta straightforward in 2026 despite being an EU island, and what's the realistic cost?" },
      { model: "Gemini", phrasing: "UK to Malta pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to fly a cat from UK to Malta in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Malta costs around £1,300 to £2,400 in 2026 by cargo flight to Luqa via Lufthansa, KLM or Air Malta. Malta accepts the UK Animal Health Certificate, so no quarantine. Direct flights from Heathrow are limited; most pet cargo connects via Frankfurt or Amsterdam. Door-to-door timelines run two to three weeks.",
    h2_outline: [
      "How much does pet transport from the UK to Malta cost in 2026?",
      "Which airlines carry pet cargo to Luqa?",
      "What paperwork does Malta require?",
      "How long does the move take door to door?",
      "FAQs about UK to Malta pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Malta)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/airlines/klm-pet-cargo/ (anchor: KLM via Schiphol)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Malta Veterinary Regulation Directorate pet import — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Underserved EU island route. Honest 'limited direct, mostly via Frankfurt' framing wins the snippet."
  },

  {
    id: "d072",
    day_number: 72,
    iso_date: "2026-09-09",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2800,
    title: "Turkish Airlines Pet Cargo 2026: Istanbul Hub, Costs and Booking",
    title_tag: "Turkish Airlines Pet Cargo 2026 | IST Hub Guide | PetTransportGlobal",
    meta_description: "How Turkish Cargo handles pets in 2026: Istanbul mega-hub transit, accepted crates, breed restrictions, costs from London and US gateways via IST.",
    url_slug: "/airlines/turkish-airlines-pet-cargo/",
    primary_seo_keyword: "turkish airlines pet cargo",
    primary_volume: 590,
    primary_kd: 26,
    secondary_seo_keywords: ["turkish cargo pets", "turkish airlines dog shipping", "istanbul pet transit", "turkish pet relocation", "fly pet via istanbul"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Turkish Cargo handle pets transiting Istanbul in 2026, and how does it compare with the Gulf carriers for routes to Asia and Africa?" },
      { model: "Claude", phrasing: "Why has Turkish Cargo become a more popular pet shipping option in 2026, and where does it genuinely beat Lufthansa and Emirates on route coverage?" },
      { model: "Gemini", phrasing: "Turkish Airlines pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is Turkish Airlines actually safe for shipping pets through Istanbul in 2026" }
    ],
    direct_answer_40_60_words: "Turkish Cargo accepts pets in 2026 via approved IATA agents and direct shipper bookings, transiting Istanbul Airport's Smartist Pet Hotel. Turkish covers more onward African and Central Asian routes than any single Gulf carrier. Costs from London to long-haul destinations range from £1,400 to £3,400 depending on crate size, with embargoes for snub-nosed breeds in summer.",
    h2_outline: [
      "How does Turkish Cargo handle pets in 2026?",
      "What is the Smartist Pet Hotel at IST?",
      "Why is Turkish a strong route option in 2026?",
      "What crate sizes and breed restrictions apply?",
      "Turkish Cargo pet costs by route",
      "FAQs about Turkish Airlines pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: Turkish snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar comparison)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa comparison)"
    ],
    external_links: [
      "Turkish Cargo Live Animals product — 2026",
      "Istanbul Airport Smartist Pet Hotel facility — 2026"
    ],
    ai_overview_play: "590 vol airline pillar with strong GSC traction. Smartist Pet Hotel is a recognisable named facility LLMs cite."
  },

  {
    id: "d073",
    day_number: 73,
    iso_date: "2026-09-10",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Denmark: AHC, Copenhagen Routes and 2026 Costs",
    title_tag: "UK to Denmark Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Denmark in 2026: AHC paperwork, ferry vs cargo costs to Copenhagen, and realistic timelines.",
    url_slug: "/routes/uk-to-denmark/",
    primary_seo_keyword: "pet transport uk to denmark",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to denmark", "shipping cat to copenhagen", "uk to denmark pet relocation", "denmark pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Copenhagen in 2026: ferry-and-drive via the Netherlands and Germany or cargo flight, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Denmark pet transport with UK to Sweden in 2026, given they're often planned as a single Scandinavian relocation." },
      { model: "Gemini", phrasing: "UK to Denmark pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to bring a cat from UK to Copenhagen in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Denmark costs around £1,000 to £2,000 in 2026 by ferry-and-drive via the Netherlands and Germany, or £1,400 to £2,600 by cargo flight to Copenhagen Kastrup. Denmark accepts the UK Animal Health Certificate. Driving suits households relocating with cars and household effects; flying suits faster moves and pet-only relocations.",
    h2_outline: [
      "How much does pet transport from the UK to Denmark cost in 2026?",
      "Ferry-and-drive vs cargo flight to Copenhagen",
      "What does Denmark require from UK pets?",
      "Combining Denmark with Sweden or Norway",
      "FAQs about UK to Denmark pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Denmark)",
      "/routes/uk-to-sweden/ (anchor: combine with Sweden)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Danish Veterinary and Food Administration pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Pairs cleanly with Sweden and Norway pages for Scandinavian retirees and remote-workers."
  },

  {
    id: "d074",
    day_number: 74,
    iso_date: "2026-09-11",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "choose-transporter",
    cluster_name: "Choosing a transporter",
    intent: "Commercial",
    content_type: "Pillar guide",
    word_count_target: 3000,
    title: "How to Vet a Pet Transport Company in 2026: A Bronze, Silver and Gold Tier Framework",
    title_tag: "How to Vet a Pet Transporter 2026 | Bronze Silver Gold | PetTransportGlobal",
    meta_description: "A 2026 framework for vetting pet transport companies: 18 checks across credentials, insurance, welfare and customer experience, scored across three tiers.",
    url_slug: "/how-to-vet-a-pet-transport-company/",
    primary_seo_keyword: "how to vet a pet transport company",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["best pet transport companies uk", "pet relocation company review", "vetting pet shipper", "trusted pet courier", "pet transport accreditation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through a structured framework for vetting a pet transport company in 2026 before I hand over money. What 15 to 20 checks should I run?" },
      { model: "Claude", phrasing: "Compare a Bronze, Silver and Gold tier of pet transport operators in 2026, scored across credentials, insurance, welfare and traceability." },
      { model: "Gemini", phrasing: "Best pet transport companies UK 2026 vetting checklist" },
      { model: "Grok", phrasing: "How to actually tell a real pet shipper from a scam in 2026" }
    ],
    direct_answer_40_60_words: "Vet a pet transport company in 2026 against an 18-point framework: DEFRA Type 1/2 authorisation, IPATA membership, IATA CEIV Live Animals, named insurance underwriter, public office address, transparent quote, named handlers and audited welfare logs. Bronze tier passes the legal minimum, Silver adds welfare audits, Gold adds independent inspection and named ground partners.",
    h2_outline: [
      "Why vetting a pet transport company matters more in 2026",
      "The 18-point framework: credentials, insurance, welfare, traceability",
      "Bronze, Silver and Gold tier definitions",
      "Red flags that disqualify a transporter immediately",
      "How to verify each claim a transporter makes",
      "FAQs about vetting pet transport companies"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/how-to-choose-a-pet-transport-company/ (anchor: choosing a transporter)",
      "/cheap-pet-transport-red-flags/ (anchor: red flags)",
      "/defra-approved-pet-transport/ (anchor: DEFRA authorisation)",
      "/door-to-door-pet-transport/ (anchor: door-to-door tier)",
      "/pet-travel-insurance/ (anchor: insurance verification)"
    ],
    external_links: [
      "DEFRA WIT transporter register — 2026",
      "IPATA member directory — 2026",
      "IATA CEIV Live Animals certified operators — 2026"
    ],
    ai_overview_play: "Structured framework with named tiers is exactly what AI overviews surface for buyer-intent queries."
  },

  {
    id: "d075",
    day_number: 75,
    iso_date: "2026-09-14",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Finland: AHC, Helsinki Routes and 2026 Costs",
    title_tag: "UK to Finland Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Finland in 2026: AHC paperwork, tapeworm rules, cargo flight costs to Helsinki and realistic timelines.",
    url_slug: "/routes/uk-to-finland/",
    primary_seo_keyword: "pet transport uk to finland",
    primary_volume: 40,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to finland", "shipping cat to helsinki", "uk to finland pet relocation", "finland pet import tapeworm"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Finland require to import a pet from the UK in 2026, and how does the tapeworm treatment timing work?" },
      { model: "Claude", phrasing: "Compare UK to Finland pet transport with UK to Sweden in 2026, given both require tapeworm treatment but different timing." },
      { model: "Gemini", phrasing: "UK to Finland pet transport cost 2026" },
      { model: "Grok", phrasing: "Easiest way to move a cat from UK to Helsinki in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Finland costs around £1,300 to £2,400 in 2026 by cargo flight to Helsinki via Lufthansa or Finnair. Finland accepts the UK Animal Health Certificate. Like Sweden and Norway, Finland additionally requires tapeworm treatment for dogs given between 24 and 120 hours before arrival, recorded by an Official Veterinarian.",
    h2_outline: [
      "How much does pet transport from the UK to Finland cost in 2026?",
      "Which airlines fly pet cargo to Helsinki?",
      "What does Finland require, including tapeworm timing?",
      "How long does the journey take?",
      "FAQs about UK to Finland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Finland)",
      "/routes/uk-to-sweden/ (anchor: Sweden tapeworm comparison)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Finnish Food Authority (Ruokavirasto) pet import — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Tapeworm 24-120 hour window is the precise fact users need."
  },

  {
    id: "d076",
    day_number: 76,
    iso_date: "2026-09-15",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "ANA Pet Cargo 2026: Tokyo Hub, Costs and Booking from London and US",
    title_tag: "ANA Pet Cargo 2026 | Tokyo Routes | PetTransportGlobal",
    meta_description: "How All Nippon Airways Cargo handles pets in 2026: Narita and Haneda transit, accepted crates, breed restrictions, costs from London and US gateways.",
    url_slug: "/airlines/ana-pet-cargo/",
    primary_seo_keyword: "ana pet cargo",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["all nippon airways pets", "ana cargo dog shipping", "ana pet relocation japan", "narita haneda pet cargo", "fly pet to tokyo ana"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does ANA Cargo handle pets arriving in Tokyo in 2026, and how does it coordinate with NACAH at Narita and Haneda?" },
      { model: "Claude", phrasing: "Compare ANA and JAL for pet cargo to Japan in 2026. Both Tokyo carriers but the operations and routes differ." },
      { model: "Gemini", phrasing: "ANA pet cargo cost UK to Japan 2026" },
      { model: "Grok", phrasing: "Best Japanese airline for shipping a dog to Tokyo in 2026" }
    ],
    direct_answer_40_60_words: "ANA Cargo accepts pets in 2026 via approved IATA agents, with most UK-origin moves connecting through Frankfurt or Schiphol. ANA coordinates with NACAH at both Narita and Haneda for AQS clearance. Costs from London to Tokyo range from £2,800 to £4,400 depending on crate size and routing, with strict snub-nosed breed restrictions year-round.",
    h2_outline: [
      "How does ANA Cargo handle pets in 2026?",
      "Narita vs Haneda for pet arrival",
      "How do you book ANA pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "ANA pet cargo costs by route",
      "FAQs about ANA pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-japan/ (anchor: UK to Japan)",
      "/countries/japan-pet-import-rules/ (anchor: NACAH process)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: ANA snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "ANA Cargo Live Animals product — 2026",
      "MAFF / NACAH pet import — 2026"
    ],
    ai_overview_play: "Pairs cleanly with the Japan country and route pages from August."
  },

  {
    id: "d077",
    day_number: 77,
    iso_date: "2026-09-16",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Malaysia in 2026: DVS Rules, Quarantine and Realistic Costs",
    title_tag: "Pet Import Malaysia 2026 | DVS Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Malaysia in 2026: DVS permit, breed bans, KLIA quarantine and realistic costs from the UK and US.",
    url_slug: "/countries/malaysia-pet-import/",
    primary_seo_keyword: "import pet to malaysia",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to malaysia", "malaysia pet import dvs", "malaysia pet quarantine 2026", "shipping cat to kuala lumpur"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does DVS require to import a dog to Malaysia from the UK in 2026, and which breeds are banned?" },
      { model: "Claude", phrasing: "Compare Malaysia's pet import process with Singapore's and Thailand's in 2026. Three Southeast Asia neighbours, three quite different paperwork chains." },
      { model: "Gemini", phrasing: "Malaysia pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Kuala Lumpur in 2026" }
    ],
    direct_answer_40_60_words: "Malaysia allows pet import in 2026 with a DVS import permit, microchip, current rabies vaccination, FAVN titre at 0.5 IU/ml or higher and a health certificate signed by an Official Veterinarian. Quarantine is seven days minimum at the KLIA Quarantine Centre. Banned breeds include Pit Bulls, Akitas, Tosas and several mastiff types. Costs from the UK range from £2,400 to £3,800.",
    h2_outline: [
      "Can you import a pet to Malaysia in 2026?",
      "What does DVS require?",
      "Which dog breeds are banned in Malaysia?",
      "What does the seven-day KLIA quarantine involve?",
      "What does pet import to Malaysia cost?",
      "FAQs about pet import to Malaysia"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: Malaysia breed bans)",
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/singapore-airlines-pet-cargo/ (anchor: SIA via Singapore)",
      "/countries/singapore-pet-import/ (anchor: Singapore comparison)",
      "/countries/thailand-pet-import/ (anchor: Thailand comparison)"
    ],
    external_links: [
      "DVS (Department of Veterinary Services Malaysia) pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Quarantine + breed-ban combination is the genuine clarification users need."
  },

  {
    id: "d078",
    day_number: 78,
    iso_date: "2026-09-17",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Israel: VS Permit, Tel Aviv Routes and 2026 Costs",
    title_tag: "UK to Israel Pet Transport 2026 | VS Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Israel in 2026: Veterinary Services permit, Tel Aviv cargo routes, breed bans and realistic costs.",
    url_slug: "/routes/uk-to-israel/",
    primary_seo_keyword: "pet transport uk to israel",
    primary_volume: 70,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to israel", "shipping cat to tel aviv", "uk to israel pet relocation", "israel pet import vs"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Israel's Veterinary Services require to import a dog from the UK in 2026, and which breeds are banned outright?" },
      { model: "Claude", phrasing: "Walk me through pet transport from London to Tel Aviv in 2026, including Ben Gurion arrival inspection and the dangerous-dogs list." },
      { model: "Gemini", phrasing: "UK to Israel pet import requirements 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from London to Tel Aviv in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Israel costs around £2,000 to £3,400 in 2026 and takes around four to six weeks. Israeli VS requires an import permit, microchip, current rabies vaccination, rabies titre and a health certificate signed by an Official Veterinarian. Banned breeds include Pit Bulls, Tosas, Argentine Dogos, Bull Terriers, Brazilian Mastiffs, American Staffords and others.",
    h2_outline: [
      "How much does pet transport from the UK to Israel cost in 2026?",
      "What does the VS import permit require?",
      "Which dog breeds are banned?",
      "Which airlines fly pet cargo to Tel Aviv?",
      "What happens at Ben Gurion on arrival?",
      "FAQs about UK to Israel pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: Israel banned breeds)",
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/turkish-airlines-pet-cargo/ (anchor: Turkish via Istanbul)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)"
    ],
    external_links: [
      "Israeli Veterinary Services pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Banned-breed list is essential planning information."
  },

  {
    id: "d079",
    day_number: 79,
    iso_date: "2026-09-18",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "Korean Air Pet Cargo 2026: Incheon Hub, Costs and Booking",
    title_tag: "Korean Air Pet Cargo 2026 | Incheon Guide | PetTransportGlobal",
    meta_description: "How Korean Air Cargo handles pets in 2026: Incheon hub transit, accepted crates, breed restrictions and costs from London and US gateways.",
    url_slug: "/airlines/korean-air-pet-cargo/",
    primary_seo_keyword: "korean air pet cargo",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["korean air dog shipping", "korean air cat cargo", "incheon pet transit", "korean air pet relocation", "fly pet via seoul"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Korean Air Cargo handle pets transiting Incheon in 2026, and how does it coordinate with APQA?" },
      { model: "Claude", phrasing: "Compare Korean Air and Asiana for pet cargo to South Korea in 2026, and explain why Incheon has emerged as a strong Asia transit option." },
      { model: "Gemini", phrasing: "Korean Air pet cargo cost 2026" },
      { model: "Grok", phrasing: "Korean Air or Cathay Pacific for shipping a pet to East Asia in 2026" }
    ],
    direct_answer_40_60_words: "Korean Air Cargo accepts pets in 2026 via approved IATA agents, with most moves transiting Incheon International. Korean Air coordinates with APQA for transit and import clearance. Costs from London to Seoul range from £2,200 to £3,800 depending on crate size and onward connection, with strict snub-nosed breed restrictions and seasonal embargo windows.",
    h2_outline: [
      "How does Korean Air Cargo handle pets in 2026?",
      "What does Incheon transit handling involve?",
      "How do you book Korean Air pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Korean Air pet cargo costs by route",
      "FAQs about Korean Air pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: Korean Air snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/countries/south-korea-pet-import/ (anchor: South Korea import rules)",
      "/airlines/cathay-pacific-pet-cargo/ (anchor: Cathay via HK comparison)"
    ],
    external_links: [
      "Korean Air Cargo Live Animals product — 2026",
      "APQA South Korea pet import — 2026"
    ],
    ai_overview_play: "Pairs with the South Korea country guide for full coverage."
  },

  {
    id: "d080",
    day_number: 80,
    iso_date: "2026-09-21",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Czech Republic: AHC, Prague Routes and 2026 Costs",
    title_tag: "UK to Czech Republic Pet Transport 2026 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to the Czech Republic in 2026: AHC paperwork, drive vs cargo flight to Prague, and realistic costs.",
    url_slug: "/routes/uk-to-czech-republic/",
    primary_seo_keyword: "pet transport uk to czech republic",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to czech republic", "shipping cat to prague", "uk to prague pet relocation", "czech republic pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Prague in 2026: drive via Germany or fly cargo, and what's the realistic cost?" },
      { model: "Claude", phrasing: "Why is moving a pet to the Czech Republic in 2026 a common 'easy EU' move that's still rarely well-documented?" },
      { model: "Gemini", phrasing: "UK to Czech Republic pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to take a cat from UK to Prague in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to the Czech Republic costs around £1,000 to £2,000 in 2026 by professional courier driving via Germany, or £1,400 to £2,400 by cargo flight to Prague Vaclav Havel. The Czech Republic accepts the UK Animal Health Certificate, so no quarantine. Driving suits door-to-door delivery; flying suits faster moves to Prague city.",
    h2_outline: [
      "How much does pet transport from the UK to the Czech Republic cost in 2026?",
      "Driving via Germany vs cargo flight to Prague",
      "What paperwork does the Czech Republic require?",
      "FAQs about UK to Czech Republic pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Czech Republic)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Czech State Veterinary Administration pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Underserved EU route with growing relocation demand."
  },

  {
    id: "d081",
    day_number: 81,
    iso_date: "2026-09-22",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Mexico: SENASICA Rules, Land Border and 2026 Costs",
    title_tag: "USA to Mexico Pet Transport 2026 | SENASICA Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Mexico in 2026: SENASICA paperwork, land border vs cargo flight options, and realistic costs from Texas, California and Arizona.",
    url_slug: "/routes/usa-to-mexico/",
    primary_seo_keyword: "pet transport usa to mexico",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["dog usa to mexico", "shipping cat to mexico from us", "us mexico land border pet", "usda mexico pet certificate"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from California to Mexico in 2026: land border crossing or cargo flight, and what does SENASICA actually want from a US-origin pet?" },
      { model: "Claude", phrasing: "Compare moving a pet across the US-Mexico land border with shipping by air in 2026. Where does each genuinely win for cost and welfare?" },
      { model: "Gemini", phrasing: "USA to Mexico pet transport cost 2026" },
      { model: "Grok", phrasing: "Easiest way to move a dog from Los Angeles to Mexico City in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Mexico costs around $400 to $1,400 by land via San Ysidro, El Paso or Brownsville, or $1,200 to $2,800 by cargo flight in 2026. SENASICA accepts US-origin pets without quarantine if they have a microchip, current rabies vaccination, ecto-parasite treatment and a USDA APHIS endorsed health certificate within five days of travel.",
    h2_outline: [
      "How much does pet transport from the USA to Mexico cost in 2026?",
      "Land border vs cargo flight: which is right for your move?",
      "What does SENASICA require for US-origin pets?",
      "Which border crossings are best for pets?",
      "FAQs about USA to Mexico pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/countries/mexico-pet-import/ (anchor: Mexico import rules)",
      "/iata-pet-crate-guide/ (anchor: IATA crate for cargo)",
      "/routes/uk-to-mexico/ (anchor: UK to Mexico comparison)"
    ],
    external_links: [
      "USDA APHIS pet export to Mexico — 2026",
      "SENASICA Mexico pet import — 2026"
    ],
    ai_overview_play: "Land-border vs cargo comparison with honest US dollar pricing. Opens USA-anchored expansion."
  },

  {
    id: "d082",
    day_number: 82,
    iso_date: "2026-09-23",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Air Canada Cargo Pet Shipping 2026: Toronto Hub, Costs and AC Animals Process",
    title_tag: "Air Canada Cargo Pets 2026 | YYZ Guide | PetTransportGlobal",
    meta_description: "How Air Canada Cargo handles pets in 2026 via the AC Animals service: Toronto and Vancouver hubs, accepted crates, breed restrictions and route costs.",
    url_slug: "/airlines/air-canada-cargo-pets/",
    primary_seo_keyword: "air canada pet cargo",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["air canada cargo ac animals", "air canada dog shipping", "yyz pet transit", "air canada pet relocation", "fly pet to canada air canada"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Air Canada Cargo's AC Animals service handle pets in 2026, and what is YYZ's pet handling actually like?" },
      { model: "Claude", phrasing: "Compare Air Canada Cargo and WestJet for pet shipping within Canada in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Air Canada AC Animals pet cargo cost 2026" },
      { model: "Grok", phrasing: "Best Canadian airline for shipping a dog domestically in 2026" }
    ],
    direct_answer_40_60_words: "Air Canada Cargo accepts pets in 2026 via the AC Animals service, both direct shipper and through approved IATA agents. Toronto Pearson and Vancouver are the main hubs with dedicated animal terminals. Domestic Canadian costs range from CAD$300 to CAD$1,200, transatlantic from CAD$1,800 to CAD$3,800 depending on crate size and seasonal embargoes.",
    h2_outline: [
      "How does Air Canada Cargo's AC Animals service work in 2026?",
      "Toronto and Vancouver hub pet handling",
      "How do you book AC Animals for a pet?",
      "What crate sizes and breed restrictions apply?",
      "Air Canada pet cargo costs by route",
      "FAQs about Air Canada pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: Air Canada snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-canada/ (anchor: UK to Canada route)"
    ],
    external_links: [
      "Air Canada Cargo AC Animals product — 2026",
      "CFIA pet import requirements — 2026"
    ],
    ai_overview_play: "AC Animals is a recognisable named service LLMs cite. Honest CAD pricing wins North American buyers."
  },

  {
    id: "d083",
    day_number: 83,
    iso_date: "2026-09-24",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Poland: AHC, Warsaw Routes and 2026 Costs",
    title_tag: "UK to Poland Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Poland in 2026: AHC paperwork, drive-via-Germany cost, cargo flight options to Warsaw and realistic timelines.",
    url_slug: "/routes/uk-to-poland/",
    primary_seo_keyword: "pet transport uk to poland",
    primary_volume: 90,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to poland", "shipping cat to warsaw", "uk to poland pet relocation", "poland pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Warsaw in 2026: drive across Europe or fly cargo, and what does each cost realistically?" },
      { model: "Claude", phrasing: "Why does UK to Poland pet transport see such varied pricing in 2026, and what are the realistic windows for each option?" },
      { model: "Gemini", phrasing: "UK to Poland pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to move a dog from UK to Krakow in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Poland costs around £900 to £1,800 in 2026 by professional courier driving via Germany, or £1,400 to £2,400 by cargo flight to Warsaw Chopin. Poland accepts the UK Animal Health Certificate, so no quarantine. Driving routes through Germany are common because Polish road networks are well-connected and predictable.",
    h2_outline: [
      "How much does pet transport from the UK to Poland cost in 2026?",
      "Driving via Germany vs cargo flight to Warsaw",
      "What paperwork does Poland require?",
      "How long does the journey take?",
      "FAQs about UK to Poland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Poland)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/routes/uk-to-czech-republic/ (anchor: Czech Republic transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "GIW (General Veterinary Inspectorate Poland) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Polish diaspora drives steady search volume. Honest cost ranges win the snippet."
  },

  {
    id: "d084",
    day_number: 84,
    iso_date: "2026-09-25",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Vietnam in 2026: DAH Rules, SGN and HAN Entry, Realistic Costs",
    title_tag: "Pet Import Vietnam 2026 | DAH Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Vietnam in 2026: DAH permit, breed bans, Saigon and Hanoi entry, realistic costs from the UK, US and EU.",
    url_slug: "/countries/vietnam-pet-import/",
    primary_seo_keyword: "import pet to vietnam",
    primary_volume: 90,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to vietnam", "vietnam pet import dah", "shipping cat to ho chi minh", "vietnam pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does DAH require to import a dog to Vietnam from the UK in 2026, and which entry airports actually clear pets?" },
      { model: "Claude", phrasing: "Compare Vietnam's pet import process with Thailand's in 2026. Both Southeast Asia, but the inspection regimes and timelines differ." },
      { model: "Gemini", phrasing: "Vietnam pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Ho Chi Minh in 2026" }
    ],
    direct_answer_40_60_words: "Vietnam allows pet import in 2026 with a DAH import permit, microchip, current rabies vaccination at least 30 days old and a health certificate signed by an Official Veterinarian. There is no quarantine for accompanied pets if paperwork is exact. Saigon (SGN) and Hanoi (HAN) clear pets; other airports require pre-arrangement. UK costs range from £2,400 to £3,800.",
    h2_outline: [
      "Can you import a pet to Vietnam in 2026?",
      "What does DAH require?",
      "Which Vietnamese airports actually clear pets?",
      "What does pet import to Vietnam cost?",
      "What happens at SGN or HAN on arrival?",
      "FAQs about pet import to Vietnam"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/singapore-airlines-pet-cargo/ (anchor: SIA via Singapore)",
      "/countries/thailand-pet-import/ (anchor: Thailand comparison)",
      "/countries/malaysia-pet-import/ (anchor: Malaysia comparison)"
    ],
    external_links: [
      "DAH (Department of Animal Health Vietnam) pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "SGN vs HAN clearance distinction is the unique fact most articles miss."
  },

  {
    id: "d085",
    day_number: 85,
    iso_date: "2026-09-28",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "JAL Pet Cargo 2026: Tokyo Routes, Costs and Booking from London and US",
    title_tag: "JAL Pet Cargo 2026 | Tokyo Routes | PetTransportGlobal",
    meta_description: "How Japan Airlines Cargo handles pets in 2026: Narita and Haneda transit, accepted crates, breed restrictions and costs from London and US gateways.",
    url_slug: "/airlines/jal-pet-cargo/",
    primary_seo_keyword: "jal pet cargo",
    primary_volume: 140,
    primary_kd: 24,
    secondary_seo_keywords: ["japan airlines pets", "jal cargo dog shipping", "jal pet relocation japan", "fly pet to tokyo jal", "narita haneda jal pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does JAL Cargo handle pets arriving in Tokyo in 2026, and how does it differ from ANA in operations and routes?" },
      { model: "Claude", phrasing: "Compare JAL and ANA for pet cargo to Japan in 2026 from a UK origin. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "JAL pet cargo cost UK to Japan 2026" },
      { model: "Grok", phrasing: "JAL or ANA for shipping a cat to Tokyo in 2026" }
    ],
    direct_answer_40_60_words: "Japan Airlines Cargo accepts pets in 2026 via approved IATA agents, with most UK-origin moves connecting through Frankfurt, Helsinki or Amsterdam. JAL handles arrivals at both Narita and Haneda, coordinating with NACAH for AQS clearance. Costs from London to Tokyo range from £2,800 to £4,400, with strict snub-nosed restrictions and seasonal embargoes mirroring ANA.",
    h2_outline: [
      "How does JAL Cargo handle pets in 2026?",
      "JAL vs ANA: operational and route differences",
      "How do you book JAL pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "JAL pet cargo costs by route",
      "FAQs about JAL pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/ana-pet-cargo/ (anchor: ANA comparison)",
      "/routes/uk-to-japan/ (anchor: UK to Japan route)",
      "/countries/japan-pet-import-rules/ (anchor: Japan import rules)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "JAL Cargo Live Animals product — 2026",
      "MAFF / NACAH pet import — 2026"
    ],
    ai_overview_play: "JAL vs ANA comparison is the genuine question UK-Japan buyers ask."
  },

  {
    id: "d086",
    day_number: 86,
    iso_date: "2026-09-29",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Austria: AHC, Vienna Routes and 2026 Costs",
    title_tag: "UK to Austria Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Austria in 2026: AHC paperwork, drive-via-Germany costs, cargo flights to Vienna and realistic timelines.",
    url_slug: "/routes/uk-to-austria/",
    primary_seo_keyword: "pet transport uk to austria",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to austria", "shipping cat to vienna", "uk to austria pet relocation", "austria pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Vienna in 2026: drive via Germany or fly cargo, and what does each really cost?" },
      { model: "Claude", phrasing: "Compare UK to Austria pet transport with UK to Switzerland or UK to Germany in 2026. Three Alpine destinations, slightly different paperwork." },
      { model: "Gemini", phrasing: "UK to Austria pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to bring a cat from UK to Salzburg in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Austria costs around £1,000 to £2,000 in 2026 by professional courier driving via France and Germany, or £1,500 to £2,600 by cargo flight to Vienna Schwechat. Austria accepts the UK Animal Health Certificate, so no quarantine. Driving suits households relocating with cars; flying suits faster moves to Vienna or Innsbruck.",
    h2_outline: [
      "How much does pet transport from the UK to Austria cost in 2026?",
      "Driving via Germany vs cargo flight",
      "What paperwork does Austria require?",
      "Connecting Austria with Switzerland or Italy onward",
      "FAQs about UK to Austria pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Austria)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/routes/uk-to-switzerland/ (anchor: Switzerland comparison)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "BMSGPK (Austrian Federal Ministry) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Underserved EU route with steady volume from expat and ski-resort relocations."
  },

  {
    id: "d087",
    day_number: 87,
    iso_date: "2026-09-30",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Canada: CFIA Rules, Land Border vs Cargo and 2026 Costs",
    title_tag: "USA to Canada Pet Transport 2026 | CFIA Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Canada in 2026: CFIA paperwork, land border crossings, cargo flight options and realistic costs from US gateways.",
    url_slug: "/routes/usa-to-canada/",
    primary_seo_keyword: "pet transport usa to canada",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["dog us to canada", "shipping cat to canada from us", "us canada land border pet", "cfia pet import us"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from New York to Toronto in 2026: drive across the border or ship by cargo, and what does CFIA actually want from a US-origin pet?" },
      { model: "Claude", phrasing: "Compare moving a pet across the US-Canada land border with shipping by air in 2026. Where does each genuinely win for cost and welfare?" },
      { model: "Gemini", phrasing: "USA to Canada pet transport cost 2026" },
      { model: "Grok", phrasing: "Easiest way to move a dog from California to Vancouver in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Canada costs around $300 to $1,200 by land via Niagara, Detroit-Windsor or Blaine, or $800 to $2,400 by cargo flight in 2026. CFIA accepts US-origin pets without quarantine if the rabies vaccination is current and a USDA APHIS endorsed health certificate is issued within 30 days. Land crossings are simpler and cheaper for most moves.",
    h2_outline: [
      "How much does pet transport from the USA to Canada cost in 2026?",
      "Land border vs cargo flight: which is right for your move?",
      "What does CFIA require for US-origin pets?",
      "Best border crossings for pet transport",
      "FAQs about USA to Canada pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-canada/ (anchor: UK to Canada comparison)",
      "/airlines/air-canada-cargo-pets/ (anchor: AC Animals service)",
      "/countries/canada-pet-import-rules/ (anchor: Canada CFIA import rules)",
      "/routes/usa-to-mexico/ (anchor: USA to Mexico land border)"
    ],
    external_links: [
      "CFIA pet import requirements — 2026",
      "USDA APHIS pet export to Canada — 2026"
    ],
    ai_overview_play: "Honest land-vs-cargo comparison with US dollar pricing. Closes Month 4 cross-border arc."
  }
);

/* ============================ MONTH 5: OCTOBER 2026 (Days 88-109) — Chunk 7 ============================
   22 working days. No UK bank holidays. First full US-pivot month with CDC pillar + multiple US-anchored routes. */
window.PLAN_ROWS.push(
  {
    id: "d088",
    day_number: 88,
    iso_date: "2026-10-01",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "defra-regulator",
    cluster_name: "Regulator pillars (DEFRA / CDC / USDA)",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 3000,
    title: "CDC Dog Import Rules 2026: How the Post-2024 US Regime Actually Works",
    title_tag: "CDC Dog Import Rules 2026 | USA Guide | PetTransportGlobal",
    meta_description: "How the CDC's post-2024 dog import rules work in 2026: CDC Dog Import Form, microchip, age limits, high-risk vs low-risk countries and approved entry airports.",
    url_slug: "/cdc-dog-import-rules-usa/",
    primary_seo_keyword: "cdc dog import rules",
    primary_volume: 1900,
    primary_kd: 28,
    secondary_seo_keywords: ["bring dog to usa cdc", "cdc dog import form 2026", "high risk rabies country dog import", "us dog import requirements", "cdc rabies vaccination form"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through the CDC's post-2024 dog import rules for arriving in the US in 2026, including the high-risk vs low-risk country split and the CDC Dog Import Form." },
      { model: "Claude", phrasing: "What changed in CDC dog import rules in 2024, what's still in force in 2026, and how does it affect a UK-origin dog flying into JFK?" },
      { model: "Gemini", phrasing: "CDC dog import requirements USA 2026" },
      { model: "Grok", phrasing: "Can I really bring my dog to the US in 2026 or is it impossible now" },
      { model: "Perplexity", phrasing: "CDC dog import form 2026 high risk countries" }
    ],
    direct_answer_40_60_words: "CDC rules in 2026 require all dogs entering the US to be at least six months old, microchipped with an ISO 11784/11785 chip and accompanied by a completed CDC Dog Import Form receipt. Dogs from high-risk rabies countries need additional documentation including a CDC-issued import permit or USDA-endorsed rabies serology. Approved entry airports are limited; check before booking.",
    h2_outline: [
      "What did the CDC change in 2024 and what's still live in 2026?",
      "High-risk vs low-risk rabies countries: the split that matters",
      "What is the CDC Dog Import Form and how do you complete it?",
      "Which US airports actually accept dogs in 2026?",
      "How CDC rules interact with USDA APHIS health certificates",
      "FAQs about CDC dog import rules"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-usa/ (anchor: UK to USA route)",
      "/routes/usa-to-canada/ (anchor: USA to Canada)",
      "/routes/usa-to-mexico/ (anchor: USA to Mexico)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/pet-microchip-international-travel/ (anchor: ISO microchip)"
    ],
    external_links: [
      "CDC dog importation regulations — 2026",
      "USDA APHIS pet travel — 2026"
    ],
    ai_overview_play: "1900-vol US pillar. Post-2024 changes are still confusing buyers. High-risk country split is the genuine clarification users need."
  },

  {
    id: "d089",
    day_number: 89,
    iso_date: "2026-10-02",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to UK: APHA Rules, Heathrow Cargo and 2026 Costs",
    title_tag: "USA to UK Pet Transport 2026 | APHA Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to the UK in 2026: APHA paperwork, rabies and tapeworm timing, Heathrow ARC clearance and realistic costs from US gateways.",
    url_slug: "/routes/usa-to-uk/",
    primary_seo_keyword: "pet transport usa to uk",
    primary_volume: 480,
    primary_kd: 24,
    secondary_seo_keywords: ["dog usa to uk", "shipping cat to london from us", "us to uk pet relocation", "apha pet import us"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from New York to London in 2026: which airline, which paperwork, and what does APHA actually require at Heathrow ARC?" },
      { model: "Claude", phrasing: "Compare BA, Virgin Atlantic, United and Delta for shipping a pet from the US to the UK in 2026, and explain the Heathrow ARC clearance fee." },
      { model: "Gemini", phrasing: "USA to UK pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to bring a dog from California to London in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to the UK costs around $2,400 to $4,800 in 2026, with most pets flying cargo via Heathrow's Animal Reception Centre. The UK requires microchip, rabies vaccination at least 21 days old, USDA APHIS endorsed health certificate and tapeworm treatment for dogs given between 24 and 120 hours before arrival. Heathrow ARC clearance fees apply.",
    h2_outline: [
      "How much does pet transport from the USA to the UK cost in 2026?",
      "Which airlines fly pet cargo from US gateways to LHR?",
      "What does APHA require for US-origin pets?",
      "What is Heathrow Animal Reception Centre and what does it cost?",
      "How long does the journey take door to door?",
      "FAQs about USA to UK pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-usa/ (anchor: reverse UK to USA route)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA pet cargo)",
      "/airlines/virgin-atlantic-pet-cargo/ (anchor: Virgin Atlantic)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export documentation)"
    ],
    external_links: [
      "APHA pet import to GB — 2026",
      "Heathrow Animal Reception Centre — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "480-vol commercial route. Heathrow ARC fee is the unique clarification US-origin movers need."
  },

  {
    id: "d090",
    day_number: 90,
    iso_date: "2026-10-05",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Delta Cargo Pet Shipping 2026: ATL Hub, Live Animal Standards and Booking",
    title_tag: "Delta Cargo Pet Shipping 2026 | Atlanta Guide | PetTransportGlobal",
    meta_description: "How Delta Cargo handles pets in 2026: Atlanta hub, accepted crates, breed restrictions, transatlantic routes and realistic costs from US gateways to Europe.",
    url_slug: "/airlines/delta-cargo-pets/",
    primary_seo_keyword: "delta cargo pet shipping",
    primary_volume: 480,
    primary_kd: 26,
    secondary_seo_keywords: ["delta dog cargo", "delta pet relocation", "atl pet transit", "fly pet via atlanta delta", "delta cargo live animals"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Delta Cargo handle pets in 2026, and how does its Atlanta hub compare with United via ORD or American via DFW for transatlantic moves?" },
      { model: "Claude", phrasing: "Walk me through booking a dog on Delta Cargo from JFK to LHR in 2026, including the live animal acceptance standards and seasonal embargoes." },
      { model: "Gemini", phrasing: "Delta Cargo pet shipping cost 2026" },
      { model: "Grok", phrasing: "Delta or United for shipping a pet from US to UK in 2026" }
    ],
    direct_answer_40_60_words: "Delta Cargo accepts pets in 2026 through approved IATA agents only, having ended direct shipper bookings in 2016. Most pet moves transit Atlanta, with transatlantic routes via JFK or Boston. Domestic US costs range from $400 to $1,400, transatlantic from $2,200 to $4,000 depending on crate size, with summer embargoes for snub-nosed breeds.",
    h2_outline: [
      "How does Delta Cargo handle pets in 2026?",
      "Why Delta is agent-only and what that means",
      "Atlanta hub pet handling: what to expect",
      "What crate sizes and breed restrictions apply?",
      "Delta Cargo pet costs by route",
      "FAQs about Delta Cargo pets"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: Delta snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/usa-to-uk/ (anchor: USA to UK route)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export rules)"
    ],
    external_links: [
      "Delta Cargo Live Animals product — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "480-vol airline pillar. Agent-only fact is the clarification confused US shippers need upfront."
  },

  {
    id: "d091",
    day_number: 91,
    iso_date: "2026-10-06",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Bahrain: NCWCD Rules, Manama Routes and 2026 Costs",
    title_tag: "UK to Bahrain Pet Transport 2026 | NCWCD Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Bahrain in 2026: NCWCD permit, Gulf Air and Etihad cargo options, breed bans and realistic costs.",
    url_slug: "/routes/uk-to-bahrain/",
    primary_seo_keyword: "pet transport uk to bahrain",
    primary_volume: 50,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to bahrain", "shipping cat to manama", "uk to bahrain pet relocation", "bahrain pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does Bahrain require to import a pet from the UK in 2026, and which airlines fly pet cargo to Manama?" },
      { model: "Claude", phrasing: "Compare UK to Bahrain pet transport with UK to UAE in 2026. Two Gulf neighbours with similar rules but different breed lists." },
      { model: "Gemini", phrasing: "UK to Bahrain pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from London to Bahrain in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Bahrain costs around £2,000 to £3,200 in 2026 by cargo flight via Gulf Air, BA or Etihad. NCWCD requires an import permit, microchip, current rabies vaccination at least 21 days old, ecto and endo-parasite treatment and a health certificate signed by an Official Veterinarian. Banned breeds mirror the wider Gulf list. Summer heat embargoes restrict June through September.",
    h2_outline: [
      "How much does pet transport from the UK to Bahrain cost in 2026?",
      "What does NCWCD require?",
      "Which airlines fly pet cargo to Manama?",
      "Banned breeds and summer embargoes",
      "FAQs about UK to Bahrain pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: Gulf breed bans)",
      "/airlines/etihad-cargo-pets/ (anchor: Etihad via Abu Dhabi)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar via Doha)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/countries/uae-pet-import-rules/ (anchor: UAE comparison)"
    ],
    external_links: [
      "NCWCD Bahrain pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Underserved Gulf route. Honest summer embargo framing wins the snippet."
  },

  {
    id: "d092",
    day_number: 92,
    iso_date: "2026-10-07",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Qatar in 2026: MoME Rules, Doha Hub and Realistic Costs",
    title_tag: "Pet Import Qatar 2026 | MoME Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Qatar in 2026: MoME permit, breed bans, summer heat embargoes, Doha Hamad arrival and realistic costs.",
    url_slug: "/countries/qatar-pet-import/",
    primary_seo_keyword: "import pet to qatar",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to qatar", "qatar pet import mome", "doha pet quarantine", "shipping cat to qatar"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does the Qatari Ministry of Municipality require to import a dog from the UK in 2026, and which breeds are banned?" },
      { model: "Claude", phrasing: "Compare Qatar's pet import process with the UAE's and Saudi Arabia's in 2026. Three Gulf states, three slightly different paperwork chains." },
      { model: "Gemini", phrasing: "Qatar pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Doha in 2026" }
    ],
    direct_answer_40_60_words: "Qatar allows pet import in 2026 with a MoME import permit, microchip, current rabies vaccination, ecto and endo-parasite treatment and a health certificate signed by an Official Veterinarian. Banned breeds include Pit Bulls, Tosas, Argentine Dogos and several mastiffs. Summer heat embargoes restrict cargo June through September. Costs from the UK range from £2,200 to £3,600.",
    h2_outline: [
      "Can you import a pet to Qatar in 2026?",
      "What does MoME require?",
      "Which dog breeds are banned in Qatar?",
      "Summer heat embargoes and Doha Hamad arrivals",
      "What does pet import cost?",
      "FAQs about pet import to Qatar"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: Qatar breed bans)",
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar Airways via Doha)",
      "/countries/uae-pet-import-rules/ (anchor: UAE comparison)",
      "/countries/saudi-arabia-pet-import/ (anchor: KSA comparison)"
    ],
    external_links: [
      "MoME (Qatar Ministry of Municipality) pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Pairs cleanly with Qatar Airways airline pillar."
  },

  {
    id: "d093",
    day_number: 93,
    iso_date: "2026-10-08",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2400,
    title: "Aer Lingus Pet Cargo 2026: Dublin Hub, Costs and UK to Ireland Booking",
    title_tag: "Aer Lingus Pet Cargo 2026 | Dublin Guide | PetTransportGlobal",
    meta_description: "How Aer Lingus handles pets in 2026: Dublin hub, transatlantic and intra-Europe routes, accepted crates, breed restrictions and realistic costs.",
    url_slug: "/airlines/aer-lingus-pet-cargo/",
    primary_seo_keyword: "aer lingus pet cargo",
    primary_volume: 320,
    primary_kd: 22,
    secondary_seo_keywords: ["aer lingus dog shipping", "aer lingus pet relocation", "dublin pet cargo", "ireland pet flights", "fly pet to dublin aer lingus"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Aer Lingus handle pets in 2026, and what's the difference between checked baggage Ireland-Europe and cargo for transatlantic moves?" },
      { model: "Claude", phrasing: "Compare Aer Lingus and BA for shipping a pet to Ireland in 2026 from London. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Aer Lingus pet cargo cost 2026" },
      { model: "Grok", phrasing: "Best way to fly a dog from UK to Dublin Aer Lingus 2026" }
    ],
    direct_answer_40_60_words: "Aer Lingus accepts pets in 2026 as cargo through approved IATA agents on transatlantic and most European routes. Direct accompanied baggage on UK-Ireland routes is no longer offered for most live animals. Costs from London to Dublin range from £600 to £1,200 cargo, transatlantic from £2,200 to £3,800 depending on crate size and connection.",
    h2_outline: [
      "How does Aer Lingus handle pets in 2026?",
      "Dublin hub pet handling and Ireland import",
      "Transatlantic pet shipping with Aer Lingus",
      "What crate sizes and breed restrictions apply?",
      "Aer Lingus pet costs by route",
      "FAQs about Aer Lingus pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-ireland/ (anchor: UK to Ireland route)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Aer Lingus Cargo Live Animals — 2026",
      "DAFM Ireland pet import — 2026"
    ],
    ai_overview_play: "320-vol airline. Honest 'no longer accompanied baggage' framing is the clarification confused buyers need."
  },

  {
    id: "d094",
    day_number: 94,
    iso_date: "2026-10-09",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Iceland: MAST Rules, Quarantine and 2026 Costs",
    title_tag: "UK to Iceland Pet Transport 2026 | MAST Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Iceland in 2026: MAST permit, mandatory quarantine, Keflavik arrival and realistic costs. The strictest EEA destination.",
    url_slug: "/routes/uk-to-iceland/",
    primary_seo_keyword: "pet transport uk to iceland",
    primary_volume: 70,
    primary_kd: 24,
    secondary_seo_keywords: ["dog uk to iceland", "shipping cat to reykjavik", "iceland pet quarantine 2026", "iceland pet import mast"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Why is Iceland the strictest EEA pet import destination in 2026, and what does the mandatory quarantine and MAST permit actually involve?" },
      { model: "Claude", phrasing: "Walk me through pet transport from London to Reykjavik in 2026, including the four-week MAST application window and Hrisey quarantine." },
      { model: "Gemini", phrasing: "UK to Iceland pet transport cost 2026" },
      { model: "Grok", phrasing: "Can I really bring my dog to Iceland in 2026 or is it impossible" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Iceland costs around £3,000 to £5,000 in 2026 and takes around four months. MAST requires an import permit applied for at least four weeks ahead, microchip, rabies vaccination, FAVN titre at 0.5 IU/ml or higher, and 14-day mandatory quarantine at the Hrisey or Reykjanes facility on arrival.",
    h2_outline: [
      "How much does pet transport from the UK to Iceland cost in 2026?",
      "What does MAST require?",
      "How does the 14-day quarantine work?",
      "Banned breeds and pre-arrival timing",
      "FAQs about UK to Iceland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/quarantine-rules-by-country/ (anchor: quarantine comparison)",
      "/rabies-titre-test/ (anchor: FAVN titre)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/breed-restrictions/ (anchor: Iceland banned breeds)"
    ],
    external_links: [
      "MAST (Icelandic Food and Veterinary Authority) pet import — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Strictest EEA destination. Honest 'four months, £3-5K, mandatory quarantine' framing is the precise reality users need."
  },

  {
    id: "d095",
    day_number: 95,
    iso_date: "2026-10-12",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "emergency-urgent",
    cluster_name: "Emergency and urgent pet moves",
    intent: "Commercial",
    content_type: "Pillar guide",
    word_count_target: 2600,
    title: "Emergency Pet Transport in 2026: When You Have Days, Not Weeks",
    title_tag: "Emergency Pet Transport 2026 | Urgent Move Guide | PetTransportGlobal",
    meta_description: "How emergency pet transport actually works in 2026 when you have days not weeks: which paperwork can be expedited, which can't, and realistic urgent costs.",
    url_slug: "/emergency-pet-transport/",
    primary_seo_keyword: "emergency pet transport",
    primary_volume: 320,
    primary_kd: 22,
    secondary_seo_keywords: ["urgent pet relocation", "fast pet shipping international", "emergency pet courier", "expedited dog cargo", "pet transport short notice"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I need to move a dog internationally in two weeks because of a job emergency. What's actually achievable in 2026, and which countries are off the table for urgent moves?" },
      { model: "Claude", phrasing: "Walk me through how emergency pet transport works in 2026: which steps can compress, which can't, and what does urgent pricing look like." },
      { model: "Gemini", phrasing: "Urgent pet transport short notice 2026" },
      { model: "Grok", phrasing: "Can I really fly my dog to the US in 10 days in 2026" }
    ],
    direct_answer_40_60_words: "Emergency pet transport in 2026 works for destinations without rabies titre or quarantine requirements. Within ten working days, EU countries, USA from low-risk origins, Canada and most Gulf states are achievable. Australia, New Zealand, Hong Kong, Japan, Iceland and Singapore are not, because their titre and permit windows cannot be compressed below 90 to 180 days legally.",
    h2_outline: [
      "What 'emergency' realistically means for pet transport in 2026",
      "Which destinations can be done in days, weeks, months",
      "What can be expedited and what cannot",
      "Urgent pricing and surcharges",
      "How to brief an emergency move clearly",
      "FAQs about emergency pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/door-to-door-pet-transport/ (anchor: door-to-door tier)",
      "/rabies-titre-test/ (anchor: titre timing constraints)",
      "/quarantine-rules-by-country/ (anchor: quarantine windows)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/how-to-vet-a-pet-transport-company/ (anchor: vet your transporter under pressure)"
    ],
    external_links: [
      "DEFRA export health certificate guidance — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "Fills missing emergency-urgent cluster. Honest list of impossible destinations is exactly what panicking buyers need."
  },

  {
    id: "d096",
    day_number: 96,
    iso_date: "2026-10-13",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Spain: APHIS, Madrid Routes and 2026 Costs",
    title_tag: "USA to Spain Pet Transport 2026 | APHIS Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Spain in 2026: USDA APHIS endorsed certificate, Madrid and Barcelona cargo routes and realistic costs from US gateways.",
    url_slug: "/routes/usa-to-spain/",
    primary_seo_keyword: "pet transport usa to spain",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["dog us to spain", "shipping cat to madrid from us", "usa spain pet relocation", "us to spain pet flight"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from Miami to Madrid in 2026: which airline, which paperwork, and how does Spain treat US-origin pets?" },
      { model: "Claude", phrasing: "Compare Iberia, Air Europa and Delta for shipping a pet from the US to Spain in 2026, with realistic costs and routings." },
      { model: "Gemini", phrasing: "USA to Spain pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to fly a cat from US to Madrid in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Spain costs around $2,200 to $4,200 in 2026 by cargo flight via Iberia, Air Europa, Delta or American. Spain accepts US-origin pets with a USDA APHIS endorsed EU health certificate, microchip and current rabies vaccination at least 21 days old. There is no quarantine. Madrid and Barcelona are the main entry points.",
    h2_outline: [
      "How much does pet transport from the USA to Spain cost in 2026?",
      "Which airlines fly pet cargo from US gateways to MAD or BCN?",
      "What does Spain require for US-origin pets?",
      "How long does the journey take?",
      "FAQs about USA to Spain pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-spain/ (anchor: UK to Spain comparison)",
      "/airlines/iberia-pet-cargo/ (anchor: Iberia pet cargo)",
      "/airlines/delta-cargo-pets/ (anchor: Delta Cargo)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "USDA APHIS pet export to Spain — 2026",
      "MAPA Spain pet import — 2026"
    ],
    ai_overview_play: "Growing US-Spain expat relocation market. Honest USD pricing is rare in this niche."
  },

  {
    id: "d097",
    day_number: 97,
    iso_date: "2026-10-14",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2500,
    title: "Iberia Pet Cargo 2026: Madrid Hub, Costs and Booking",
    title_tag: "Iberia Pet Cargo 2026 | Madrid Guide | PetTransportGlobal",
    meta_description: "How Iberia handles pets in 2026: Madrid hub, Latin America connectivity, accepted crates, breed restrictions and realistic costs from London and US gateways.",
    url_slug: "/airlines/iberia-pet-cargo/",
    primary_seo_keyword: "iberia pet cargo",
    primary_volume: 210,
    primary_kd: 24,
    secondary_seo_keywords: ["iberia dog shipping", "iberia cat cargo", "madrid pet transit", "iberia pet relocation latin america", "fly pet via madrid iberia"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Iberia handle pets transiting Madrid in 2026, and how does its Latin America network make it the strongest carrier for UK or US to Argentina, Chile or Colombia?" },
      { model: "Claude", phrasing: "Compare Iberia and Air Europa for pet cargo from Spain to Latin America in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Iberia pet cargo cost 2026" },
      { model: "Grok", phrasing: "Iberia or Lufthansa for shipping a pet to South America in 2026" }
    ],
    direct_answer_40_60_words: "Iberia accepts pets in 2026 via approved IATA agents and on Iberia Cargo direct booking for some markets. Madrid is the main hub with strong Latin America connectivity to Buenos Aires, Santiago, Bogota, Lima and Mexico City. Costs from London to LATAM via MAD range from £2,400 to £4,000, with embargoes for snub-nosed breeds during summer.",
    h2_outline: [
      "How does Iberia Cargo handle pets in 2026?",
      "Why Madrid is the gateway for Latin America pet moves",
      "What crate sizes and breed restrictions apply?",
      "Iberia pet cargo costs by route",
      "FAQs about Iberia pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-spain/ (anchor: UK to Spain route)",
      "/routes/usa-to-spain/ (anchor: USA to Spain)"
    ],
    external_links: [
      "Iberia Cargo Live Animals product — 2026",
      "MAPA Spain pet import — 2026"
    ],
    ai_overview_play: "Latin America gateway angle is the unique fact most airline summaries miss."
  },

  {
    id: "d098",
    day_number: 98,
    iso_date: "2026-10-15",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Romania: AHC, Bucharest Routes and 2026 Costs",
    title_tag: "UK to Romania Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Romania in 2026: AHC paperwork, drive vs cargo flight to Bucharest, and realistic costs.",
    url_slug: "/routes/uk-to-romania/",
    primary_seo_keyword: "pet transport uk to romania",
    primary_volume: 70,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to romania", "shipping cat to bucharest", "uk to romania pet relocation", "romania pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Bucharest in 2026: drive across Europe or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Why does UK to Romania pet transport see such varied pricing in 2026, and what are the realistic windows for each option?" },
      { model: "Gemini", phrasing: "UK to Romania pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to bring a dog from UK to Bucharest in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Romania costs around £900 to £1,800 in 2026 by professional courier driving via Germany, Austria and Hungary, or £1,400 to £2,400 by cargo flight to Bucharest Otopeni. Romania accepts the UK Animal Health Certificate. Driving is common because the road network through Central Europe is well-mapped and predictable.",
    h2_outline: [
      "How much does pet transport from the UK to Romania cost in 2026?",
      "Driving via Central Europe vs cargo flight to Bucharest",
      "What paperwork does Romania require?",
      "How long does the journey take?",
      "FAQs about UK to Romania pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Romania)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "ANSVSA (Romanian National Sanitary Veterinary Authority) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Romanian diaspora drives steady search. Honest cost ranges win the snippet."
  },

  {
    id: "d099",
    day_number: 99,
    iso_date: "2026-10-16",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Argentina in 2026: SENASA Rules, EZE Arrival and Costs",
    title_tag: "Pet Import Argentina 2026 | SENASA Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Argentina in 2026: SENASA permit, EZE Buenos Aires arrival, accepted vaccines and realistic costs from the UK and US.",
    url_slug: "/countries/argentina-pet-import/",
    primary_seo_keyword: "import pet to argentina",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to argentina", "argentina pet import senasa", "shipping cat to buenos aires", "argentina pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does SENASA require to import a dog to Argentina from the UK in 2026, and how does EZE arrival actually work?" },
      { model: "Claude", phrasing: "Compare Argentina's pet import process with Chile's and Brazil's in 2026. Three South American giants, three different paperwork chains." },
      { model: "Gemini", phrasing: "Argentina pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Buenos Aires in 2026" }
    ],
    direct_answer_40_60_words: "Argentina allows pet import in 2026 with a SENASA-recognised health certificate, microchip, current rabies vaccination at least 30 days old, internal and external parasite treatment within 15 days of travel and a VFI (Veterinary Frontier Inspection) at EZE Buenos Aires on arrival. There is no quarantine for accompanied pets. Costs from the UK range from £2,400 to £3,800.",
    h2_outline: [
      "Can you import a pet to Argentina in 2026?",
      "What does SENASA require?",
      "What happens at EZE Buenos Aires on arrival?",
      "Banned breeds and import gateways",
      "What does pet import cost?",
      "FAQs about pet import to Argentina"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/iberia-pet-cargo/ (anchor: Iberia via Madrid)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/countries/brazil-pet-import-rules/ (anchor: Brazil comparison)"
    ],
    external_links: [
      "SENASA Argentina pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Pairs cleanly with Iberia (d097) for the LATAM gateway story."
  },

  {
    id: "d100",
    day_number: 100,
    iso_date: "2026-10-19",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "welfare",
    cluster_name: "In-transit welfare",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2800,
    title: "Pet Welfare in Transit 2026: How Cargo Holds Are Pressurised, Heated and Monitored",
    title_tag: "Pet Welfare in Transit 2026 | Cargo Hold Guide | PetTransportGlobal",
    meta_description: "What happens to pets in cargo during international flights in 2026: hold pressurisation, temperature, lighting and what good handlers actually do mid-transit.",
    url_slug: "/pet-welfare-in-transit/",
    primary_seo_keyword: "pet welfare cargo flight",
    primary_volume: 590,
    primary_kd: 24,
    secondary_seo_keywords: ["is cargo safe for pets", "cargo hold pet temperature", "pet flight stress", "pets in cargo pressurised", "iata live animal welfare"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What actually happens to a dog in cargo during a 12-hour flight in 2026? Hold pressurisation, temperature, lighting, monitoring." },
      { model: "Claude", phrasing: "Walk me through pet welfare standards in commercial cargo holds in 2026: what airlines actually do, what IATA LAR mandates, and what good handlers add." },
      { model: "Gemini", phrasing: "Is cargo safe for pets 2026" },
      { model: "Grok", phrasing: "What really happens to my dog in the cargo hold for 10 hours" },
      { model: "Perplexity", phrasing: "Pet welfare cargo flight IATA LAR 2026" }
    ],
    direct_answer_40_60_words: "Pet cargo holds in 2026 are pressurised and temperature-controlled to between 15 and 21 degrees Celsius, lit dimly to reduce stress, and physically separated from passenger baggage. IATA Live Animal Regulations mandate hold conditions, crate ventilation and welfare checks. Good handlers add pre-flight walks, hydration topping at transit and arrival decompression to reduce stress.",
    h2_outline: [
      "Is cargo really safe for pets in 2026?",
      "How cargo hold pressurisation, temperature and lighting work",
      "What IATA Live Animal Regulations actually mandate",
      "What good handlers do beyond the minimum",
      "Risk factors: routing, breed, season, crate fit",
      "FAQs about pet welfare in transit"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/cargo-vs-cabin-pet-flight/ (anchor: cargo vs cabin)",
      "/breed-restrictions/ (anchor: snub-nosed welfare)",
      "/how-to-vet-a-pet-transport-company/ (anchor: handler welfare standards)",
      "/door-to-door-pet-transport/ (anchor: door-to-door welfare)"
    ],
    external_links: [
      "IATA Live Animals Regulations (LAR) — 2026",
      "OIE/WOAH animal welfare during transport — 2026"
    ],
    ai_overview_play: "Fills missing welfare cluster. 590-vol topic. Honest factual hold conditions answer the panicking-owner query exactly."
  },

  {
    id: "d101",
    day_number: 101,
    iso_date: "2026-10-20",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Hungary: AHC, Budapest Routes and 2026 Costs",
    title_tag: "UK to Hungary Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Hungary in 2026: AHC paperwork, drive-via-Austria options, cargo flights to Budapest and realistic costs.",
    url_slug: "/routes/uk-to-hungary/",
    primary_seo_keyword: "pet transport uk to hungary",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to hungary", "shipping cat to budapest", "uk to hungary pet relocation", "hungary pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Budapest in 2026: drive via Austria or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Hungary pet transport with UK to Czech Republic and UK to Austria in 2026. Three landlocked Central European routes." },
      { model: "Gemini", phrasing: "UK to Hungary pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to take a dog from UK to Budapest in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Hungary costs around £1,000 to £1,900 in 2026 by professional courier driving via Germany and Austria, or £1,400 to £2,400 by cargo flight to Budapest Liszt Ferenc. Hungary accepts the UK Animal Health Certificate. Driving suits households relocating with cars; flying suits faster moves to Budapest city.",
    h2_outline: [
      "How much does pet transport from the UK to Hungary cost in 2026?",
      "Driving via Austria vs cargo flight to Budapest",
      "What paperwork does Hungary require?",
      "FAQs about UK to Hungary pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Hungary)",
      "/routes/uk-to-austria/ (anchor: Austria transit)",
      "/routes/uk-to-czech-republic/ (anchor: Czech transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Nebih (Hungarian Food Chain Safety Office) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Underserved Central European route with steady expat volume."
  },

  {
    id: "d102",
    day_number: 102,
    iso_date: "2026-10-21",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2400,
    title: "SAS Pet Cargo 2026: Copenhagen and Oslo Routes, Costs and Booking",
    title_tag: "SAS Pet Cargo 2026 | Scandinavia Guide | PetTransportGlobal",
    meta_description: "How SAS handles pets in 2026: Copenhagen and Oslo hubs, accepted crates, Scandinavian routes and realistic costs from London and US gateways.",
    url_slug: "/airlines/sas-pet-cargo/",
    primary_seo_keyword: "sas pet cargo",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["sas dog shipping", "sas cat cargo", "scandinavian airlines pets", "copenhagen pet cargo sas", "fly pet via copenhagen sas"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does SAS handle pets in 2026, and how does its Copenhagen hub compare with Lufthansa via Frankfurt for Scandinavia-bound moves?" },
      { model: "Claude", phrasing: "Compare SAS and Finnair for pet cargo to Scandinavia in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "SAS pet cargo cost 2026" },
      { model: "Grok", phrasing: "SAS or Lufthansa for shipping a pet to Sweden in 2026" }
    ],
    direct_answer_40_60_words: "SAS accepts pets in 2026 via approved IATA agents only, with most moves transiting Copenhagen Kastrup or Oslo Gardermoen. SAS coordinates with Danish, Swedish, Norwegian and Finnish authorities for tapeworm and rabies documentation timing. Costs from London to Scandinavia range from £1,400 to £2,800 depending on crate size and onward connection.",
    h2_outline: [
      "How does SAS Cargo handle pets in 2026?",
      "Copenhagen vs Oslo hub pet handling",
      "How do you book SAS pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "SAS pet cargo costs by route",
      "FAQs about SAS pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/routes/uk-to-sweden/ (anchor: UK to Sweden)",
      "/routes/uk-to-denmark/ (anchor: UK to Denmark)",
      "/routes/uk-to-finland/ (anchor: UK to Finland)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "SAS Cargo Live Animals product — 2026",
      "Danish Veterinary and Food Administration pet import — 2026"
    ],
    ai_overview_play: "Pairs cleanly with Scandinavian route pages already published."
  },

  {
    id: "d103",
    day_number: 103,
    iso_date: "2026-10-22",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2500,
    title: "Pet Transport USA to Australia: USDA, FAVN and 2026 Costs",
    title_tag: "USA to Australia Pet Transport 2026 | DAFF Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Australia in 2026: USDA APHIS, FAVN titre timing, DAFF import permit, Melbourne quarantine and realistic costs.",
    url_slug: "/routes/usa-to-australia/",
    primary_seo_keyword: "pet transport usa to australia",
    primary_volume: 170,
    primary_kd: 26,
    secondary_seo_keywords: ["dog us to australia", "shipping cat to sydney from us", "usa australia pet relocation", "favn titre us dog australia"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from California to Sydney in 2026: USDA paperwork, FAVN titre at a US lab, DAFF permit, Melbourne PEQ. What's the realistic timeline?" },
      { model: "Claude", phrasing: "Walk me through the full 7-month US to Australia pet transport process in 2026, including which US labs are USDA-recognised for FAVN titre." },
      { model: "Gemini", phrasing: "USA to Australia pet transport cost 2026" },
      { model: "Grok", phrasing: "How much does it really cost to fly a dog from USA to Australia in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Australia costs around $5,500 to $9,000 in 2026 and takes seven months minimum. The process requires USDA APHIS endorsement, FAVN rabies titre at a USDA-approved lab, DAFF import permit, MEL Mickleham 10-day quarantine and an approved registered handler. Direct flights into Melbourne are limited; most pets connect via LAX or SFO.",
    h2_outline: [
      "How much does pet transport from the USA to Australia cost in 2026?",
      "The 7-month timeline: FAVN to PEQ release",
      "Which US labs are USDA-approved for FAVN titre?",
      "Which airlines fly pet cargo from US gateways to Melbourne?",
      "FAQs about USA to Australia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-australia/ (anchor: UK to Australia comparison)",
      "/rabies-titre-test/ (anchor: FAVN titre)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/quarantine-rules-by-country/ (anchor: PEQ Mickleham)"
    ],
    external_links: [
      "DAFF (Australian Department of Agriculture, Fisheries and Forestry) cats and dogs — 2026",
      "USDA APHIS pet export to Australia — 2026"
    ],
    ai_overview_play: "Premium 170-vol US route. 7-month timeline + USDA FAVN-approved lab list is high-utility content."
  },

  {
    id: "d104",
    day_number: 104,
    iso_date: "2026-10-23",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2800,
    title: "Importing a Pet to Mainland China in 2026: GACC Rules, PEK and PVG and Realistic Costs",
    title_tag: "Pet Import China 2026 | GACC Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to mainland China in 2026: GACC permit, Beijing and Shanghai 7-day quarantine, breed bans and realistic costs.",
    url_slug: "/countries/china-pet-import/",
    primary_seo_keyword: "import pet to china",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["bring dog to china", "china pet import gacc", "shanghai pet quarantine", "shipping cat to beijing", "china banned dog breeds"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does GACC require to import a dog to mainland China from the UK or US in 2026, and what does the 7-day quarantine actually involve?" },
      { model: "Claude", phrasing: "Compare China's pet import process with Hong Kong's and Taiwan's in 2026. Three ostensibly Chinese-cultural markets, three completely different paperwork chains." },
      { model: "Gemini", phrasing: "China pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Shanghai in 2026" }
    ],
    direct_answer_40_60_words: "Mainland China allows pet import in 2026 with a GACC pre-arrival declaration, microchip, current rabies vaccination, FAVN titre at 0.5 IU/ml or higher (or 30-day quarantine in lieu), and a health certificate signed by an Official Veterinarian. PEK and PVG are the only no-quarantine entry airports if the FAVN is in order. Banned breeds include Pit Bulls, Tosas, Argentine Dogos and others.",
    h2_outline: [
      "Can you import a pet to mainland China in 2026?",
      "What does GACC require?",
      "Beijing PEK vs Shanghai PVG: the no-quarantine entry points",
      "Banned breeds and per-household limits",
      "What does pet import to China cost?",
      "FAQs about pet import to China"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breed-restrictions/ (anchor: China breed bans)",
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/rabies-titre-test/ (anchor: FAVN titre)",
      "/airlines/cathay-pacific-pet-cargo/ (anchor: Cathay via HK)",
      "/quarantine-rules-by-country/ (anchor: quarantine comparison)"
    ],
    external_links: [
      "GACC (General Administration of Customs of China) pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "320-vol country pillar. PEK/PVG no-quarantine distinction is the precise fact LLMs cite."
  },

  {
    id: "d105",
    day_number: 105,
    iso_date: "2026-10-26",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2500,
    title: "EVA Air Pet Cargo 2026: Taipei Hub, Costs and Booking",
    title_tag: "EVA Air Pet Cargo 2026 | Taipei Guide | PetTransportGlobal",
    meta_description: "How EVA Air Cargo handles pets in 2026: Taipei TPE hub, accepted crates, Asia-Pacific routes and realistic costs from London and US gateways.",
    url_slug: "/airlines/eva-air-pet-cargo/",
    primary_seo_keyword: "eva air pet cargo",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["eva air dog shipping", "eva air cat cargo", "tpe pet transit", "taipei pet relocation", "fly pet via taipei eva air"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does EVA Air Cargo handle pets transiting Taipei in 2026, and how does it compare with China Airlines for Asia-Pacific moves?" },
      { model: "Claude", phrasing: "Compare EVA Air and China Airlines for pet cargo to Taiwan in 2026. Two Taipei carriers but different operations." },
      { model: "Gemini", phrasing: "EVA Air pet cargo cost 2026" },
      { model: "Grok", phrasing: "EVA Air or Cathay for shipping a pet to Taiwan in 2026" }
    ],
    direct_answer_40_60_words: "EVA Air Cargo accepts pets in 2026 via approved IATA agents, with most moves transiting Taipei Taoyuan. EVA coordinates with BAPHIQ for Taiwan import clearance. Costs from London to Taipei range from £2,200 to £3,800 depending on crate size and connection, with strict snub-nosed restrictions and seasonal embargo windows.",
    h2_outline: [
      "How does EVA Air Cargo handle pets in 2026?",
      "Taipei hub pet handling and BAPHIQ coordination",
      "What crate sizes and breed restrictions apply?",
      "EVA Air pet cargo costs by route",
      "FAQs about EVA Air pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/airlines/cathay-pacific-pet-cargo/ (anchor: Cathay via HK)"
    ],
    external_links: [
      "EVA Air Cargo Live Animals product — 2026",
      "BAPHIQ Taiwan pet import — 2026"
    ],
    ai_overview_play: "Pairs with upcoming Taiwan country guide for full coverage."
  },

  {
    id: "d106",
    day_number: 106,
    iso_date: "2026-10-27",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Croatia: AHC, Zagreb and Split and 2026 Costs",
    title_tag: "UK to Croatia Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Croatia in 2026: AHC paperwork, drive options, cargo flights to Zagreb and Split and realistic costs.",
    url_slug: "/routes/uk-to-croatia/",
    primary_seo_keyword: "pet transport uk to croatia",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to croatia", "shipping cat to zagreb", "uk to split pet relocation", "croatia pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Zagreb or Split in 2026: drive across Europe or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Why is Croatia an increasingly common UK relocation in 2026, and what's the realistic pet transport cost vs Italy or Slovenia comparable routes?" },
      { model: "Gemini", phrasing: "UK to Croatia pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to take a cat from UK to Split in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Croatia costs around £1,100 to £2,000 in 2026 by professional courier driving via Germany, Austria and Slovenia, or £1,500 to £2,600 by cargo flight to Zagreb or Split. Croatia accepts the UK Animal Health Certificate. Driving is common because the road network through Central Europe is well-mapped.",
    h2_outline: [
      "How much does pet transport from the UK to Croatia cost in 2026?",
      "Driving via Slovenia vs cargo flight to Zagreb or Split",
      "What paperwork does Croatia require?",
      "FAQs about UK to Croatia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Croatia)",
      "/routes/uk-to-italy/ (anchor: Italy comparison)",
      "/routes/uk-to-austria/ (anchor: Austria transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Croatian Veterinary Inspectorate pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Adriatic relocation market growing post-EU accession. Underserved route."
  },

  {
    id: "d107",
    day_number: 107,
    iso_date: "2026-10-28",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "cost-pricing",
    cluster_name: "Cost and pricing",
    intent: "Commercial",
    content_type: "Tool page",
    word_count_target: 1800,
    title: "Pet Transport Cost Calculator (USD): International Shipping Estimates 2026",
    title_tag: "Pet Transport Cost Calculator USD 2026 | PetTransportGlobal",
    meta_description: "Estimate international pet transport costs from US gateways in 2026 in US dollars. Crate size, route distance, season, breed surcharges and route-specific fees.",
    url_slug: "/cost-of-pet-transport-usd/",
    primary_seo_keyword: "pet transport cost calculator usd",
    primary_volume: 880,
    primary_kd: 22,
    secondary_seo_keywords: ["pet shipping cost us dollars", "international pet transport cost us", "ship dog overseas cost usd", "pet relocation cost united states"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Give me a realistic 2026 cost calculator for shipping a Labrador internationally from the US in US dollars, broken down by route, crate size and season." },
      { model: "Claude", phrasing: "Walk me through pet transport cost calculation in USD for 2026, including crate sizing surcharges, snub-nosed embargo premiums and APHIS endorsement fees." },
      { model: "Gemini", phrasing: "Pet transport cost USD calculator 2026" },
      { model: "Grok", phrasing: "How much does it really cost to ship a dog from US in 2026 in USD" }
    ],
    direct_answer_40_60_words: "Pet transport from the US in 2026 typically costs $1,400 to $9,000 depending on destination, crate size and routing. North America and Mexico run $400 to $2,400. Europe runs $2,400 to $4,800. Asia and Middle East run $3,200 to $5,800. Australia and New Zealand run $5,500 to $9,000. Snub-nosed surcharges add $500 to $1,500.",
    h2_outline: [
      "What drives pet transport cost from the US in 2026?",
      "Cost ranges by region in USD",
      "Crate size and airline weight surcharges",
      "APHIS endorsement and CDC fees",
      "Snub-nosed embargo premiums",
      "FAQs about US pet transport cost"
    ],
    schema_required: ["Article", "FAQPage", "WebApplication", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: GBP cost calculator)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC documentation)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed surcharges)",
      "/routes/usa-to-uk/ (anchor: USA to UK)",
      "/routes/usa-to-australia/ (anchor: USA to Australia)"
    ],
    external_links: [
      "USDA APHIS endorsement fees — 2026",
      "CDC dog importation regulations — 2026"
    ],
    ai_overview_play: "880-vol US tool page. Honest USD ranges with per-region breakdowns is exactly what AI overviews surface."
  },

  {
    id: "d108",
    day_number: 108,
    iso_date: "2026-10-29",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Bulgaria: AHC, Sofia Routes and 2026 Costs",
    title_tag: "UK to Bulgaria Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Bulgaria in 2026: AHC paperwork, drive vs cargo flight to Sofia, and realistic costs.",
    url_slug: "/routes/uk-to-bulgaria/",
    primary_seo_keyword: "pet transport uk to bulgaria",
    primary_volume: 40,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to bulgaria", "shipping cat to sofia", "uk to bulgaria pet relocation", "bulgaria pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Sofia in 2026: drive across Europe or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Bulgaria pet transport with UK to Romania in 2026. Both EU Black Sea destinations with growing UK retiree relocations." },
      { model: "Gemini", phrasing: "UK to Bulgaria pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to take a dog from UK to Sofia in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Bulgaria costs around £1,000 to £1,900 in 2026 by professional courier driving via Germany, Austria and Hungary, or £1,500 to £2,500 by cargo flight to Sofia. Bulgaria accepts the UK Animal Health Certificate. Many UK retirees combining a Bulgaria move with Romania or Greece prefer the drive-and-deliver option.",
    h2_outline: [
      "How much does pet transport from the UK to Bulgaria cost in 2026?",
      "Driving via Central Europe vs cargo flight to Sofia",
      "What paperwork does Bulgaria require?",
      "FAQs about UK to Bulgaria pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Bulgaria)",
      "/routes/uk-to-romania/ (anchor: Romania comparison)",
      "/routes/uk-to-greece/ (anchor: Greece transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "BFSA (Bulgarian Food Safety Agency) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "UK retiree market drives steady demand."
  },

  {
    id: "d109",
    day_number: 109,
    iso_date: "2026-10-30",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2500,
    title: "Swiss International Air Lines Pet Cargo 2026: Zurich Hub, Costs and Booking",
    title_tag: "Swiss Pet Cargo 2026 | Zurich Guide | PetTransportGlobal",
    meta_description: "How Swiss handles pets in 2026: Zurich hub, accepted crates, breed restrictions, European and long-haul routes and realistic costs.",
    url_slug: "/airlines/swiss-pet-cargo/",
    primary_seo_keyword: "swiss air pet cargo",
    primary_volume: 210,
    primary_kd: 24,
    secondary_seo_keywords: ["swiss international airlines pets", "swiss dog cargo", "zurich pet transit", "swiss pet relocation", "fly pet via zurich"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Swiss International Air Lines handle pets transiting Zurich in 2026, and how does it compare with Lufthansa via Frankfurt as the alternative German-speaking hub?" },
      { model: "Claude", phrasing: "Compare Swiss and Lufthansa for pet cargo in 2026. Both Lufthansa Group, but the operations and accepted routes differ." },
      { model: "Gemini", phrasing: "Swiss Air pet cargo cost 2026" },
      { model: "Grok", phrasing: "Swiss or Lufthansa for shipping a pet through Europe in 2026" }
    ],
    direct_answer_40_60_words: "Swiss accepts pets in 2026 via approved IATA agents, with most moves transiting Zurich. As part of the Lufthansa Group, Swiss often combines with Lufthansa Animal Lounge handling at Frankfurt. Costs from London to onward destinations range from £1,400 to £3,000 depending on crate size and connection, with snub-nosed embargoes and Swiss federal welfare standards on hold conditions.",
    h2_outline: [
      "How does Swiss handle pets in 2026?",
      "Zurich hub pet handling and Lufthansa Group integration",
      "What crate sizes and breed restrictions apply?",
      "Swiss pet cargo costs by route",
      "FAQs about Swiss pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-switzerland/ (anchor: UK to Switzerland)"
    ],
    external_links: [
      "Swiss WorldCargo Live Animals product — 2026",
      "FSVO Switzerland pet import — 2026"
    ],
    ai_overview_play: "Lufthansa Group integration angle is the unique fact most articles miss. Closes Month 5 cleanly."
  }
);

/* ============================ MONTH 6: NOVEMBER 2026 (Days 110-130) — Chunk 8 ============================
   21 working days. No UK bank holidays. Closes underweight clusters: public-transport, uk-regional, quote-agency-choice, refresh-seasonal. */
window.PLAN_ROWS.push(
  {
    id: "d110",
    day_number: 110,
    iso_date: "2026-11-02",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "defra-regulator",
    cluster_name: "Regulator pillars (DEFRA / CDC / USDA)",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Find an Official Veterinarian (OV) for Pet Export 2026: AHCs, USDA Endorsement and What OVs Actually Do",
    title_tag: "Find an Official Vet (OV) 2026 | AHC & APHIS | PetTransportGlobal",
    meta_description: "How to find an Official Veterinarian for pet export in 2026: AHC issuance in the UK, USDA APHIS endorsement in the US, what OVs actually do and what they charge.",
    url_slug: "/find-an-official-veterinarian/",
    primary_seo_keyword: "find official veterinarian pet export",
    primary_volume: 590,
    primary_kd: 22,
    secondary_seo_keywords: ["ov ahc uk", "usda accredited vet near me", "official vet pet travel", "ahc issuing vet", "usda endorsed health certificate"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How do I find an Official Veterinarian to issue an Animal Health Certificate in the UK in 2026, and how does the equivalent USDA APHIS accredited vet system work in the US?" },
      { model: "Claude", phrasing: "Walk me through what an Official Veterinarian actually does on the day I bring my dog in for an AHC in 2026, and what they typically charge." },
      { model: "Gemini", phrasing: "Find official vet for pet export UK 2026" },
      { model: "Grok", phrasing: "How much does an Official Vet cost for a pet AHC in 2026" }
    ],
    direct_answer_40_60_words: "An Official Veterinarian in the UK is a vet authorised by APHA to issue Animal Health Certificates for pet export. The US equivalent is a USDA APHIS accredited veterinarian. In 2026 a UK AHC appointment costs around £150 to £350; US APHIS-endorsed certificates run $40 to $250 plus the vet's own fee. Both must be timed precisely to the destination's window.",
    h2_outline: [
      "What is an Official Veterinarian and why do you need one?",
      "How to find an OV in the UK in 2026",
      "How USDA APHIS accreditation works in the US",
      "What happens at the appointment: the OV checklist",
      "AHC and APHIS endorsement timing windows",
      "FAQs about Official Veterinarians"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: Pet Passport / AHC pillar)",
      "/defra-approved-pet-transport/ (anchor: DEFRA Type 1/2 transporters)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export documentation)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/how-to-vet-a-pet-transport-company/ (anchor: vetting framework)"
    ],
    external_links: [
      "APHA OV register — 2026",
      "USDA APHIS accredited veterinarian search — 2026"
    ],
    ai_overview_play: "590-vol top-of-funnel pillar. Honest UK and US dual coverage with cost ranges is exactly the AI-overview snippet."
  },

  {
    id: "d111",
    day_number: 111,
    iso_date: "2026-11-03",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport USA to Germany: APHIS, Frankfurt Hub and 2026 Costs",
    title_tag: "USA to Germany Pet Transport 2026 | APHIS Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Germany in 2026: USDA APHIS endorsed certificate, Frankfurt Animal Lounge clearance, breed welfare and realistic costs.",
    url_slug: "/routes/usa-to-germany/",
    primary_seo_keyword: "pet transport usa to germany",
    primary_volume: 320,
    primary_kd: 22,
    secondary_seo_keywords: ["dog us to germany", "shipping cat to frankfurt from us", "us germany pet relocation", "frankfurt animal lounge us pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from Boston to Frankfurt in 2026: which airline, which paperwork, and what does Frankfurt Animal Lounge clearance involve for US-origin pets?" },
      { model: "Claude", phrasing: "Compare Lufthansa, United and Delta for shipping a pet from the US to Germany in 2026, including FRA Animal Lounge handling and onward EU travel." },
      { model: "Gemini", phrasing: "USA to Germany pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from US to Frankfurt in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Germany costs around $2,200 to $4,200 in 2026 by cargo flight via Lufthansa, United or Delta. Most pets clear at Frankfurt Animal Lounge, the world's largest dedicated animal terminal. Germany accepts US-origin pets with a USDA APHIS endorsed EU health certificate, microchip and rabies vaccination at least 21 days old. No quarantine.",
    h2_outline: [
      "How much does pet transport from the USA to Germany cost in 2026?",
      "Frankfurt Animal Lounge clearance for US-origin pets",
      "Which airlines fly pet cargo from US gateways to FRA?",
      "What does Germany require for US-origin pets?",
      "FAQs about USA to Germany pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-germany/ (anchor: UK to Germany comparison)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa Animal Lounge)",
      "/cost-of-pet-transport-usd/ (anchor: USD cost calculator)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export rules)"
    ],
    external_links: [
      "USDA APHIS pet export to Germany — 2026",
      "BMEL Germany pet import — 2026"
    ],
    ai_overview_play: "320-vol US route. FRA Animal Lounge angle is the unique advantage."
  },

  {
    id: "d112",
    day_number: 112,
    iso_date: "2026-11-04",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2400,
    title: "ITA Airways Pet Cargo 2026: Rome Hub, Costs and Booking",
    title_tag: "ITA Airways Pet Cargo 2026 | Rome Guide | PetTransportGlobal",
    meta_description: "How ITA Airways handles pets in 2026: Rome Fiumicino hub, accepted crates, breed restrictions, European and long-haul routes and realistic costs.",
    url_slug: "/airlines/ita-airways-pet-cargo/",
    primary_seo_keyword: "ita airways pet cargo",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["ita airways dog shipping", "ita pet relocation", "fiumicino pet cargo", "rome pet transit", "fly pet via rome"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does ITA Airways handle pets in 2026, and how does the new airline differ operationally from the old Alitalia for pet shippers?" },
      { model: "Claude", phrasing: "Compare ITA Airways and Lufthansa for shipping a pet to Italy in 2026 from London. Which is more reliable for breed restrictions?" },
      { model: "Gemini", phrasing: "ITA Airways pet cargo cost 2026" },
      { model: "Grok", phrasing: "ITA or Lufthansa for shipping a cat to Rome in 2026" }
    ],
    direct_answer_40_60_words: "ITA Airways accepts pets in 2026 via approved IATA agents, with most moves transiting Rome Fiumicino. ITA inherited Alitalia's live animal handling protocols and now operates within the Lufthansa Group orbit, sharing some FRA Animal Lounge integration. Costs from London to Rome range from £1,000 to £1,800 cargo, with snub-nosed embargoes during summer months.",
    h2_outline: [
      "How does ITA Airways handle pets in 2026?",
      "Rome Fiumicino pet cargo handling",
      "ITA vs Lufthansa Group integration",
      "What crate sizes and breed restrictions apply?",
      "ITA Airways pet cargo costs by route",
      "FAQs about ITA Airways pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa Group)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-italy/ (anchor: UK to Italy)"
    ],
    external_links: [
      "ITA Airways Cargo Live Animals — 2026",
      "Italian Ministry of Health pet import — 2026"
    ],
    ai_overview_play: "Post-Alitalia clarification is the unique fact most articles miss."
  },

  {
    id: "d113",
    day_number: 113,
    iso_date: "2026-11-05",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Slovenia: AHC, Ljubljana Routes and 2026 Costs",
    title_tag: "UK to Slovenia Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Slovenia in 2026: AHC paperwork, drive options through Austria, cargo flights to Ljubljana and realistic costs.",
    url_slug: "/routes/uk-to-slovenia/",
    primary_seo_keyword: "pet transport uk to slovenia",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to slovenia", "shipping cat to ljubljana", "uk to slovenia pet relocation", "slovenia pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Ljubljana in 2026: drive via Austria or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Slovenia pet transport with UK to Austria and UK to Croatia in 2026. Three Alpine-Adriatic neighbours." },
      { model: "Gemini", phrasing: "UK to Slovenia pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to take a cat from UK to Ljubljana in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Slovenia costs around £1,000 to £1,900 in 2026 by professional courier driving via Germany and Austria, or £1,500 to £2,500 by cargo flight to Ljubljana. Slovenia accepts the UK Animal Health Certificate. Driving via Salzburg and Klagenfurt is the common path; many movers combine Slovenia with Croatia or Italy.",
    h2_outline: [
      "How much does pet transport from the UK to Slovenia cost in 2026?",
      "Driving via Austria vs cargo flight to Ljubljana",
      "What paperwork does Slovenia require?",
      "Combining Slovenia with Croatia or Italy",
      "FAQs about UK to Slovenia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Slovenia)",
      "/routes/uk-to-austria/ (anchor: Austria transit)",
      "/routes/uk-to-croatia/ (anchor: Croatia onward)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "UVHVVR Slovenia pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Underserved Alpine route. Combination-routing angle wins planners."
  },

  {
    id: "d114",
    day_number: 114,
    iso_date: "2026-11-06",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Chile in 2026: SAG Rules, Santiago Arrival and Realistic Costs",
    title_tag: "Pet Import Chile 2026 | SAG Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Chile in 2026: SAG zoosanitary certificate, Santiago SCL arrival, no quarantine and realistic costs from the UK and US.",
    url_slug: "/countries/chile-pet-import/",
    primary_seo_keyword: "import pet to chile",
    primary_volume: 90,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to chile", "chile pet import sag", "shipping cat to santiago", "chile pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does SAG require to import a dog to Chile from the UK in 2026, and how does Santiago SCL clearance work?" },
      { model: "Claude", phrasing: "Compare Chile's pet import process with Argentina's and Peru's in 2026. Three Pacific-coast neighbours, three different paperwork chains." },
      { model: "Gemini", phrasing: "Chile pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Santiago in 2026" }
    ],
    direct_answer_40_60_words: "Chile allows pet import in 2026 with a SAG-recognised zoosanitary certificate, microchip, current rabies vaccination at least 30 days old, internal and external parasite treatment within 10 days of travel and an inspection at Santiago SCL on arrival. There is no quarantine for accompanied pets. Costs from the UK range from £2,400 to £3,800; from the US $2,400 to $4,000.",
    h2_outline: [
      "Can you import a pet to Chile in 2026?",
      "What does SAG require?",
      "What happens at Santiago SCL on arrival?",
      "Banned breeds and entry gateways",
      "What does pet import cost?",
      "FAQs about pet import to Chile"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/iberia-pet-cargo/ (anchor: Iberia via Madrid)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/countries/argentina-pet-import/ (anchor: Argentina comparison)"
    ],
    external_links: [
      "SAG (Servicio Agricola y Ganadero) Chile pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Pairs with Iberia airline for the LATAM gateway story."
  },

  {
    id: "d115",
    day_number: 115,
    iso_date: "2026-11-09",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2400,
    title: "Finnair Pet Cargo 2026: Helsinki Hub, Costs and Asia Connectivity",
    title_tag: "Finnair Pet Cargo 2026 | Helsinki Guide | PetTransportGlobal",
    meta_description: "How Finnair handles pets in 2026: Helsinki COOL Cargo terminal, Asia connectivity via the polar route and realistic costs from London and US gateways.",
    url_slug: "/airlines/finnair-pet-cargo/",
    primary_seo_keyword: "finnair pet cargo",
    primary_volume: 140,
    primary_kd: 22,
    secondary_seo_keywords: ["finnair dog shipping", "finnair cool cargo pet", "helsinki pet transit", "finnair pet relocation asia", "fly pet via helsinki"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Finnair handle pets transiting Helsinki in 2026, and why does the polar Asia route make Finnair a strong UK to Japan or Korea option?" },
      { model: "Claude", phrasing: "Compare Finnair and SAS for pet cargo to Scandinavia in 2026, and explain Finnair's COOL Cargo facility at HEL." },
      { model: "Gemini", phrasing: "Finnair pet cargo cost 2026" },
      { model: "Grok", phrasing: "Finnair or KLM for shipping a pet to Tokyo in 2026" }
    ],
    direct_answer_40_60_words: "Finnair accepts pets in 2026 via approved IATA agents, with most moves transiting Helsinki Vantaa's COOL Cargo terminal. Finnair's polar route to Asia makes Helsinki one of Europe's shortest connections to Tokyo, Seoul and Shanghai. Costs from London to HEL range from £1,200 to £2,000; UK to Asia via HEL £2,400 to £4,000.",
    h2_outline: [
      "How does Finnair Cargo handle pets in 2026?",
      "Helsinki COOL Cargo facility",
      "Why the polar route makes Finnair strong for Asia moves",
      "What crate sizes and breed restrictions apply?",
      "Finnair pet cargo costs by route",
      "FAQs about Finnair pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/sas-pet-cargo/ (anchor: SAS comparison)",
      "/routes/uk-to-japan/ (anchor: UK to Japan via HEL)",
      "/routes/uk-to-finland/ (anchor: UK to Finland)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Finnair Cargo Live Animals product — 2026",
      "Finnish Food Authority pet import — 2026"
    ],
    ai_overview_play: "Polar route Asia angle is the unique advantage articles consistently miss."
  },

  {
    id: "d116",
    day_number: 116,
    iso_date: "2026-11-10",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Slovakia: AHC, Bratislava Routes and 2026 Costs",
    title_tag: "UK to Slovakia Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Slovakia in 2026: AHC paperwork, drive options through Germany and Austria, cargo flights and realistic costs.",
    url_slug: "/routes/uk-to-slovakia/",
    primary_seo_keyword: "pet transport uk to slovakia",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to slovakia", "shipping cat to bratislava", "uk to slovakia pet relocation", "slovakia pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Bratislava in 2026: drive via Vienna or fly cargo via Vienna with onward, what does each cost?" },
      { model: "Claude", phrasing: "Why is UK to Slovakia pet transport often routed via Vienna in 2026, and how does that compare with direct cargo to BTS?" },
      { model: "Gemini", phrasing: "UK to Slovakia pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to take a dog from UK to Bratislava in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Slovakia costs around £1,000 to £1,900 in 2026 by professional courier driving via Germany and Austria, or £1,400 to £2,400 by cargo flight via Vienna with short onward transfer to Bratislava. Slovakia accepts the UK Animal Health Certificate. Vienna routing is more common than direct BTS cargo because of greater frequency.",
    h2_outline: [
      "How much does pet transport from the UK to Slovakia cost in 2026?",
      "Driving via Vienna vs cargo flight to BTS",
      "What paperwork does Slovakia require?",
      "FAQs about UK to Slovakia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Slovakia)",
      "/routes/uk-to-austria/ (anchor: Vienna routing)",
      "/routes/uk-to-czech-republic/ (anchor: Czech comparison)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "SVPS (State Veterinary and Food Administration of Slovakia) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Vienna-routing reality is the unique clarification."
  },

  {
    id: "d117",
    day_number: 117,
    iso_date: "2026-11-11",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "public-transport",
    cluster_name: "Public transport with pets in the UK",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Travelling on UK Public Transport with a Pet 2026: Trains, Tube, Buses and Ferries",
    title_tag: "Pets on UK Public Transport 2026 | Trains & Buses | PetTransportGlobal",
    meta_description: "How to travel with a pet on UK public transport in 2026: National Rail, Tube, buses, ferries and Eurostar. What's allowed, what's banned and what carriers require.",
    url_slug: "/pets-on-uk-public-transport/",
    primary_seo_keyword: "pets on uk public transport",
    primary_volume: 720,
    primary_kd: 18,
    secondary_seo_keywords: ["dog on train uk", "cat on london underground", "pet on national rail", "pet on uk bus", "pets on eurostar"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through what's allowed for taking a dog or cat on UK trains, the Tube, buses and ferries in 2026, including the policies that vary between operators." },
      { model: "Claude", phrasing: "Compare National Rail, TfL, First Bus, Stagecoach, P&O Ferries and Eurostar pet rules in 2026. What changed in the last two years?" },
      { model: "Gemini", phrasing: "Pets on uk public transport rules 2026" },
      { model: "Grok", phrasing: "Can I take my dog on the Tube in London in 2026" }
    ],
    direct_answer_40_60_words: "UK public transport in 2026 generally accepts dogs and cats free of charge if controlled and not in carriages designated as quiet zones. National Rail allows up to two pets per passenger free; the Tube and London buses accept pets at the driver's or staff's discretion. Eurostar prohibits pets except registered assistance animals. Ferries vary by operator.",
    h2_outline: [
      "Can you take a pet on a UK train in 2026?",
      "London Underground, buses and Overground rules",
      "Pets on UK ferries and Eurostar",
      "Travelling with a nervous or large dog on public transport",
      "What carriers and crates do operators expect?",
      "FAQs about pets on UK public transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/within-uk-pet-transport/ (anchor: within-UK pet transport)",
      "/iata-pet-crate-guide/ (anchor: carriers and crates)",
      "/door-to-door-pet-transport/ (anchor: door-to-door alternative)",
      "/pet-microchip-international-travel/ (anchor: microchip basics)"
    ],
    external_links: [
      "National Rail Conditions of Travel (pets) — 2026",
      "Transport for London accessibility and pets — 2026"
    ],
    ai_overview_play: "720-vol pillar fills the missing public-transport cluster. Multi-operator comparison wins the snippet."
  },

  {
    id: "d118",
    day_number: 118,
    iso_date: "2026-11-12",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Estonia: AHC, Tallinn Routes and 2026 Costs",
    title_tag: "UK to Estonia Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Estonia in 2026: AHC paperwork, ferry-and-drive via the Baltics, cargo flights to Tallinn and realistic costs.",
    url_slug: "/routes/uk-to-estonia/",
    primary_seo_keyword: "pet transport uk to estonia",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to estonia", "shipping cat to tallinn", "uk to estonia pet relocation", "estonia pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Tallinn in 2026: drive across Europe and ferry from Helsinki, or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Estonia, Latvia and Lithuania pet transport in 2026. Three Baltic neighbours often planned as a single Baltic move." },
      { model: "Gemini", phrasing: "UK to Estonia pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route from UK to Tallinn with a cat in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Estonia costs around £1,200 to £2,200 in 2026 by professional courier driving via Germany, Poland and the Baltics, or £1,500 to £2,500 by cargo flight to Tallinn via Helsinki or Riga. Estonia accepts the UK Animal Health Certificate. Driving with the Helsinki-Tallinn ferry final leg is increasingly common.",
    h2_outline: [
      "How much does pet transport from the UK to Estonia cost in 2026?",
      "Drive-via-Baltic vs cargo via Helsinki or Riga",
      "What paperwork does Estonia require?",
      "Combining Estonia with Latvia and Lithuania",
      "FAQs about UK to Estonia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Estonia)",
      "/routes/uk-to-finland/ (anchor: Finland-Estonia ferry)",
      "/airlines/finnair-pet-cargo/ (anchor: Finnair via HEL)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "VTA (Estonian Agriculture and Food Board) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Helsinki-Tallinn ferry leg is the unique routing option for Baltic moves."
  },

  {
    id: "d119",
    day_number: 119,
    iso_date: "2026-11-13",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Colombia in 2026: ICA Rules, Bogota Arrival and Realistic Costs",
    title_tag: "Pet Import Colombia 2026 | ICA Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Colombia in 2026: ICA zoosanitary certificate, Bogota El Dorado arrival, no quarantine and realistic costs from UK and US.",
    url_slug: "/countries/colombia-pet-import/",
    primary_seo_keyword: "import pet to colombia",
    primary_volume: 90,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to colombia", "colombia pet import ica", "shipping cat to bogota", "colombia pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does ICA require to import a dog to Colombia from the UK in 2026, and how does Bogota El Dorado clearance actually work?" },
      { model: "Claude", phrasing: "Compare Colombia's pet import process with Mexico's and Argentina's in 2026. Three Latin American giants, three slightly different paperwork chains." },
      { model: "Gemini", phrasing: "Colombia pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Bogota in 2026" }
    ],
    direct_answer_40_60_words: "Colombia allows pet import in 2026 with an ICA-recognised zoosanitary certificate, microchip, current rabies vaccination at least 30 days old, internal and external parasite treatment and inspection at Bogota El Dorado on arrival. There is no quarantine for accompanied pets. Costs from the UK range from £2,400 to £3,800; from the US $2,200 to $3,800.",
    h2_outline: [
      "Can you import a pet to Colombia in 2026?",
      "What does ICA require?",
      "What happens at Bogota El Dorado on arrival?",
      "Banned breeds and entry gateways",
      "What does pet import cost?",
      "FAQs about pet import to Colombia"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/iberia-pet-cargo/ (anchor: Iberia via Madrid)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/countries/argentina-pet-import/ (anchor: Argentina comparison)",
      "/countries/chile-pet-import/ (anchor: Chile comparison)"
    ],
    external_links: [
      "ICA (Instituto Colombiano Agropecuario) pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Underserved Andean route. Iberia via Madrid is the realistic gateway."
  },

  {
    id: "d120",
    day_number: 120,
    iso_date: "2026-11-16",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "American Airlines Cargo Pet Shipping 2026: DFW Hub, AA PetEmbark and Booking",
    title_tag: "American Airlines Cargo Pets 2026 | DFW Guide | PetTransportGlobal",
    meta_description: "How American Airlines Cargo handles pets in 2026: DFW hub, PetEmbark service, accepted crates, breed restrictions and realistic costs from US gateways.",
    url_slug: "/airlines/american-airlines-cargo-pets/",
    primary_seo_keyword: "american airlines cargo pets",
    primary_volume: 720,
    primary_kd: 26,
    secondary_seo_keywords: ["aa cargo dog shipping", "american airlines petembark", "dfw pet transit", "american pet relocation", "fly pet via dallas american"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does American Airlines Cargo handle pets through PetEmbark in 2026, and how does DFW compare with Delta's ATL hub for transatlantic moves?" },
      { model: "Claude", phrasing: "Walk me through booking a dog on American Airlines Cargo from JFK to LHR in 2026, including embargoes and PetEmbark eligibility." },
      { model: "Gemini", phrasing: "American Airlines Cargo pet cost 2026" },
      { model: "Grok", phrasing: "American or United for shipping a pet to Europe in 2026" }
    ],
    direct_answer_40_60_words: "American Airlines Cargo accepts pets in 2026 through approved IATA agents, having ended direct shipper bookings via PetEmbark in 2021. DFW is the main hub. Domestic costs range from $400 to $1,400, transatlantic via JFK or MIA from $2,200 to $4,200 depending on crate size, with summer embargoes for snub-nosed breeds and high-temperature airports.",
    h2_outline: [
      "How does American Airlines Cargo handle pets in 2026?",
      "What happened to PetEmbark and what replaced it",
      "DFW and JFK hub pet handling",
      "What crate sizes and breed restrictions apply?",
      "American pet cargo costs by route",
      "FAQs about American Airlines Cargo pets"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/delta-cargo-pets/ (anchor: Delta comparison)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: snub-nosed rules)",
      "/cost-of-pet-transport-usd/ (anchor: USD cost calculator)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export rules)"
    ],
    external_links: [
      "American Airlines Cargo Animal Care — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "720-vol US airline pillar. Honest 'PetEmbark ended' framing is the clarification confused buyers need."
  },

  {
    id: "d121",
    day_number: 121,
    iso_date: "2026-11-17",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Latvia: AHC, Riga Routes and 2026 Costs",
    title_tag: "UK to Latvia Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Latvia in 2026: AHC paperwork, drive options, cargo flights to Riga and realistic costs.",
    url_slug: "/routes/uk-to-latvia/",
    primary_seo_keyword: "pet transport uk to latvia",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to latvia", "shipping cat to riga", "uk to latvia pet relocation", "latvia pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Riga in 2026: drive across Poland or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Latvia pet transport with the Baltic alternatives in 2026. How do you choose between flying to RIX or driving via Poland?" },
      { model: "Gemini", phrasing: "UK to Latvia pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to bring a cat from UK to Riga in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Latvia costs around £1,100 to £2,100 in 2026 by professional courier driving via Germany and Poland, or £1,500 to £2,400 by cargo flight to Riga via Helsinki or Frankfurt. Latvia accepts the UK Animal Health Certificate. Driving is common because Riga sits on a clean Berlin-Warsaw-Riga corridor.",
    h2_outline: [
      "How much does pet transport from the UK to Latvia cost in 2026?",
      "Driving via Poland vs cargo flight to Riga",
      "What paperwork does Latvia require?",
      "FAQs about UK to Latvia pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Latvia)",
      "/routes/uk-to-poland/ (anchor: Poland transit)",
      "/routes/uk-to-estonia/ (anchor: Estonia comparison)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "PVD (Latvian Food and Veterinary Service) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Berlin-Warsaw-Riga corridor reality wins planners."
  },

  {
    id: "d122",
    day_number: 122,
    iso_date: "2026-11-18",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "uk-regional",
    cluster_name: "UK regional collection and delivery",
    intent: "Commercial",
    content_type: "UK regional pillar",
    word_count_target: 2400,
    title: "Pet Transport from Manchester 2026: International Routes, Airport Cargo and Costs",
    title_tag: "Pet Transport Manchester 2026 | Airport & Routes | PetTransportGlobal",
    meta_description: "International pet transport from Manchester in 2026: MAN Animal Reception Centre, route costs, North West collection and realistic timelines for owners outside London.",
    url_slug: "/pet-transport-manchester/",
    primary_seo_keyword: "pet transport manchester",
    primary_volume: 720,
    primary_kd: 18,
    secondary_seo_keywords: ["pet shipping manchester airport", "international pet courier manchester", "ship dog from manchester", "manchester airport animal reception", "north west pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Can I ship my dog internationally from Manchester in 2026 instead of driving to Heathrow, and what are the realistic cost and route differences?" },
      { model: "Claude", phrasing: "Walk me through pet transport from Manchester in 2026, including MAN's animal reception facility, North West collection radius and onward routing via FRA or AMS." },
      { model: "Gemini", phrasing: "Pet transport manchester airport 2026" },
      { model: "Grok", phrasing: "Best way to ship a cat from Manchester to USA in 2026" }
    ],
    direct_answer_40_60_words: "Manchester Airport offers limited direct pet cargo in 2026, so most North West moves either truck to Heathrow or fly via Frankfurt or Amsterdam connections. Manchester collection saves £150 to £400 in driver mileage for owners across the North West and North Wales. Total costs typically run within £100 of Heathrow-anchored quotes for the same destination.",
    h2_outline: [
      "Can you ship a pet internationally from Manchester in 2026?",
      "Manchester Airport animal reception and route options",
      "When does it pay to truck to Heathrow vs fly via FRA or AMS?",
      "North West collection radius and saving on driver mileage",
      "Manchester pet transport costs by destination",
      "FAQs about pet transport from Manchester"
    ],
    schema_required: ["Article", "FAQPage", "Service", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/within-uk-pet-transport/ (anchor: within-UK transport)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via FRA)",
      "/airlines/klm-pet-cargo/ (anchor: KLM via AMS)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/door-to-door-pet-transport/ (anchor: door-to-door)"
    ],
    external_links: [
      "Manchester Airport cargo facility — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "720-vol regional pillar. Honest 'mostly via FRA/AMS' framing wins regional buyers."
  },

  {
    id: "d123",
    day_number: 123,
    iso_date: "2026-11-19",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Lithuania: AHC, Vilnius Routes and 2026 Costs",
    title_tag: "UK to Lithuania Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Lithuania in 2026: AHC paperwork, drive options, cargo flights to Vilnius and realistic costs.",
    url_slug: "/routes/uk-to-lithuania/",
    primary_seo_keyword: "pet transport uk to lithuania",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to lithuania", "shipping cat to vilnius", "uk to lithuania pet relocation", "lithuania pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Vilnius in 2026: drive across Europe or fly cargo, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Lithuania pet transport with the rest of the Baltics in 2026. Lithuanian diaspora drives steady demand." },
      { model: "Gemini", phrasing: "UK to Lithuania pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to take a dog from UK to Vilnius in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Lithuania costs around £1,100 to £2,100 in 2026 by professional courier driving via Germany and Poland, or £1,500 to £2,500 by cargo flight to Vilnius via Helsinki or Riga. Lithuania accepts the UK Animal Health Certificate. Lithuanian diaspora moves are common; many couriers run consolidated Baltic runs.",
    h2_outline: [
      "How much does pet transport from the UK to Lithuania cost in 2026?",
      "Driving via Poland vs cargo flight",
      "What paperwork does Lithuania require?",
      "Combining Lithuania with Latvia and Estonia",
      "FAQs about UK to Lithuania pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Lithuania)",
      "/routes/uk-to-poland/ (anchor: Poland transit)",
      "/routes/uk-to-latvia/ (anchor: Latvia comparison)",
      "/routes/uk-to-estonia/ (anchor: Estonia comparison)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "VMVT (Lithuanian State Food and Veterinary Service) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Lithuanian diaspora drives 50-vol with healthy commercial intent."
  },

  {
    id: "d124",
    day_number: 124,
    iso_date: "2026-11-20",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "United Cargo Pet Shipping 2026: PetSafe, ORD and EWR Hubs and Booking",
    title_tag: "United Cargo PetSafe 2026 | ORD & EWR Guide | PetTransportGlobal",
    meta_description: "How United Cargo handles pets via PetSafe in 2026: ORD and EWR hubs, accepted crates, breed restrictions and realistic costs from US gateways to Europe and Asia.",
    url_slug: "/airlines/united-cargo-petsafe/",
    primary_seo_keyword: "united petsafe pet cargo",
    primary_volume: 880,
    primary_kd: 26,
    secondary_seo_keywords: ["united cargo dog shipping", "united petsafe service", "ord pet transit", "united pet relocation", "fly pet via chicago united"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does United Cargo's PetSafe service work in 2026, and how does ORD compare with Delta's ATL or American's DFW for transatlantic moves?" },
      { model: "Claude", phrasing: "Walk me through booking a dog on United PetSafe from EWR to LHR in 2026, including breed restrictions and seasonal embargoes." },
      { model: "Gemini", phrasing: "United PetSafe cost 2026" },
      { model: "Grok", phrasing: "United or American for shipping a pet from US to UK in 2026" }
    ],
    direct_answer_40_60_words: "United Cargo accepts pets in 2026 through the PetSafe programme, available direct shipper or via approved IATA agents. Chicago O'Hare and Newark are the main hubs. Domestic costs range from $400 to $1,500, transatlantic via EWR or IAD from $2,200 to $4,200 depending on crate size, with seasonal embargoes for snub-nosed breeds and high-temperature airports.",
    h2_outline: [
      "How does United Cargo PetSafe work in 2026?",
      "ORD vs EWR vs IAD: which hub is right",
      "How do you book PetSafe?",
      "What crate sizes and breed restrictions apply?",
      "United pet cargo costs by route",
      "FAQs about United PetSafe"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/delta-cargo-pets/ (anchor: Delta comparison)",
      "/airlines/american-airlines-cargo-pets/ (anchor: American comparison)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/cost-of-pet-transport-usd/ (anchor: USD cost calculator)",
      "/routes/usa-to-uk/ (anchor: USA to UK route)"
    ],
    external_links: [
      "United Cargo PetSafe — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "880-vol PetSafe is one of the most-searched US pet airline programs."
  },

  {
    id: "d125",
    day_number: 125,
    iso_date: "2026-11-23",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Taiwan in 2026: BAPHIQ Rules, Quarantine and Realistic Costs",
    title_tag: "Pet Import Taiwan 2026 | BAPHIQ Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Taiwan in 2026: BAPHIQ permit, FAVN titre, 7-day to 21-day home quarantine and realistic costs from the UK and US.",
    url_slug: "/countries/taiwan-pet-import/",
    primary_seo_keyword: "import pet to taiwan",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to taiwan", "taiwan pet import baphiq", "shipping cat to taipei", "taiwan pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does BAPHIQ require to import a dog to Taiwan from the UK in 2026, and how does the home quarantine actually work?" },
      { model: "Claude", phrasing: "Compare Taiwan's pet import process with mainland China's and Japan's in 2026. Three East Asian markets, completely different paperwork chains." },
      { model: "Gemini", phrasing: "Taiwan pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Taipei in 2026" }
    ],
    direct_answer_40_60_words: "Taiwan allows pet import in 2026 with a BAPHIQ import permit, microchip, two rabies vaccinations and a FAVN titre at 0.5 IU/ml or higher at least 90 days before travel. Home quarantine runs 7 to 21 days depending on origin. The UK and US are low-risk so 7 days. Costs from the UK range from £2,400 to £3,800.",
    h2_outline: [
      "Can you import a pet to Taiwan in 2026?",
      "What does BAPHIQ require?",
      "How does the 7-21 day home quarantine work?",
      "What does pet import to Taiwan cost?",
      "FAQs about pet import to Taiwan"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/eva-air-pet-cargo/ (anchor: EVA Air via TPE)",
      "/rabies-titre-test/ (anchor: FAVN titre)",
      "/countries/china-pet-import/ (anchor: China comparison)",
      "/countries/japan-pet-import-rules/ (anchor: Japan comparison)"
    ],
    external_links: [
      "BAPHIQ Taiwan pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Pairs with EVA Air (d105) and China Airlines (d127) for full Taiwan coverage."
  },

  {
    id: "d126",
    day_number: 126,
    iso_date: "2026-11-24",
    day_of_week: "Tue",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2000,
    title: "Pet Transport UK to Luxembourg: AHC, Drive Options and 2026 Costs",
    title_tag: "UK to Luxembourg Pet Transport 2026 | Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Luxembourg in 2026: AHC paperwork, drive via Belgium and Germany, and realistic costs.",
    url_slug: "/routes/uk-to-luxembourg/",
    primary_seo_keyword: "pet transport uk to luxembourg",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to luxembourg", "shipping cat to luxembourg city", "uk to luxembourg pet relocation", "luxembourg pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Luxembourg City in 2026: drive via Belgium or via France, and what does each cost?" },
      { model: "Claude", phrasing: "Why is UK to Luxembourg pet transport almost always done by road in 2026, and what's the realistic cost for a single small dog?" },
      { model: "Gemini", phrasing: "UK to Luxembourg pet transport cost 2026" },
      { model: "Grok", phrasing: "Cost to take a cat from UK to Luxembourg in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Luxembourg costs around £700 to £1,400 in 2026 by professional courier driving via the Eurotunnel and Belgium. Luxembourg accepts the UK Animal Health Certificate. Cargo flights to Luxembourg-Findel for pets are limited; most moves are road-only. Door-to-door delivery from London takes one working day.",
    h2_outline: [
      "How much does pet transport from the UK to Luxembourg cost in 2026?",
      "Driving via Belgium vs France",
      "What paperwork does Luxembourg require?",
      "FAQs about UK to Luxembourg pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Luxembourg)",
      "/routes/uk-to-france/ (anchor: France transit)",
      "/routes/uk-to-germany/ (anchor: Germany alternative)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "ALVA (Luxembourg Veterinary and Food Administration) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Honest 'road-only' framing wins planners."
  },

  {
    id: "d127",
    day_number: 127,
    iso_date: "2026-11-25",
    day_of_week: "Wed",
    quarter: "Q2",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2400,
    title: "China Airlines Pet Cargo 2026: Taipei Hub, Costs and Booking",
    title_tag: "China Airlines Pet Cargo 2026 | Taipei Guide | PetTransportGlobal",
    meta_description: "How China Airlines (CAL) handles pets in 2026: Taipei hub, accepted crates, Asia-Pacific routes, breed restrictions and realistic costs.",
    url_slug: "/airlines/china-airlines-pet-cargo/",
    primary_seo_keyword: "china airlines pet cargo",
    primary_volume: 110,
    primary_kd: 24,
    secondary_seo_keywords: ["cal cargo dog shipping", "china airlines taiwan pets", "tpe china airlines pet transit", "fly pet via taipei china airlines"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does China Airlines (CAL, Taiwan-based) handle pets in 2026, and how does it differ from EVA Air despite both being Taipei carriers?" },
      { model: "Claude", phrasing: "Compare China Airlines and EVA Air for pet cargo to Taiwan in 2026 from London." },
      { model: "Gemini", phrasing: "China Airlines pet cargo cost 2026" },
      { model: "Grok", phrasing: "China Airlines or EVA Air for shipping a pet to Asia in 2026" }
    ],
    direct_answer_40_60_words: "China Airlines (CAL, Taiwan, not mainland) accepts pets in 2026 via approved IATA agents, with most moves transiting Taipei Taoyuan. CAL coordinates with BAPHIQ for Taiwan import clearance. Costs from London to Taipei range from £2,200 to £3,800 depending on crate size and connection. Onward Asia connectivity is strong but slightly behind EVA's network.",
    h2_outline: [
      "How does China Airlines Cargo handle pets in 2026?",
      "China Airlines vs EVA Air: who's better for what?",
      "What crate sizes and breed restrictions apply?",
      "China Airlines pet cargo costs by route",
      "FAQs about China Airlines pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/eva-air-pet-cargo/ (anchor: EVA Air comparison)",
      "/countries/taiwan-pet-import/ (anchor: Taiwan import)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "China Airlines Cargo Live Animals — 2026",
      "BAPHIQ Taiwan pet import — 2026"
    ],
    ai_overview_play: "Honest 'CAL is Taiwan, not mainland China' clarification wins confused searchers."
  },

  {
    id: "d128",
    day_number: 128,
    iso_date: "2026-11-26",
    day_of_week: "Thu",
    quarter: "Q2",
    cluster_id: "quote-agency-choice",
    cluster_name: "Agency vs DIY quote choice",
    intent: "Commercial",
    content_type: "Pillar guide",
    word_count_target: 2800,
    title: "Pet Relocation Agency vs DIY in 2026: When to Hire, When to Self-Manage",
    title_tag: "Pet Agency vs DIY 2026 | Decision Guide | PetTransportGlobal",
    meta_description: "Should you hire a pet relocation agency or self-manage your move in 2026? Honest decision framework by destination, complexity, breed and budget.",
    url_slug: "/pet-relocation-agency-vs-diy/",
    primary_seo_keyword: "pet relocation agency vs diy",
    primary_volume: 320,
    primary_kd: 22,
    secondary_seo_keywords: ["should i use a pet shipper", "diy pet relocation", "self manage pet export", "pet relocation cost vs diy", "is pet relocation agency worth it"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through whether to hire a pet relocation agency or self-manage in 2026, by destination complexity, breed, budget and stress tolerance." },
      { model: "Claude", phrasing: "Where does DIY pet relocation realistically work in 2026 and where does it always go wrong? Give me a decision framework." },
      { model: "Gemini", phrasing: "Pet relocation agency vs diy 2026" },
      { model: "Grok", phrasing: "Is a pet shipper worth £2000 in 2026 or can I do it myself" }
    ],
    direct_answer_40_60_words: "Self-managing a pet relocation in 2026 works for short-haul EU routes by road and within-UK moves. Agencies are essential for Australia, New Zealand, Singapore, Hong Kong, Japan, Iceland, China and Mainland Asia where permit windows, FAVN timing and cargo bookings are non-recoverable if you miss a step. Agency fees of £400 to £900 buy time, paperwork and risk transfer.",
    h2_outline: [
      "When does DIY pet relocation work in 2026?",
      "When you genuinely need an agency",
      "What an agency actually does for the fee",
      "Decision framework: destination, breed, time, money",
      "Hybrid model: agency for paperwork, DIY for transport",
      "FAQs about agency vs DIY"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/how-to-vet-a-pet-transport-company/ (anchor: vetting an agency)",
      "/cheap-pet-transport-red-flags/ (anchor: red flags)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/pet-passports/ (anchor: AHC self-management)",
      "/door-to-door-pet-transport/ (anchor: door-to-door tier)"
    ],
    external_links: [
      "DEFRA export health certificate guidance — 2026",
      "USDA APHIS pet export — 2026"
    ],
    ai_overview_play: "Fills underweight quote-agency-choice cluster. Honest 'where DIY breaks' is the AI-overview snippet."
  },

  {
    id: "d129",
    day_number: 129,
    iso_date: "2026-11-27",
    day_of_week: "Fri",
    quarter: "Q2",
    cluster_id: "routes-uk-anchored",
    cluster_name: "Cross-border route pages (non-UK origin)",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport USA to Italy: APHIS, Rome and Milan Cargo and 2026 Costs",
    title_tag: "USA to Italy Pet Transport 2026 | APHIS Guide | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the USA to Italy in 2026: USDA APHIS endorsed certificate, Rome and Milan arrivals, cargo costs and realistic timelines.",
    url_slug: "/routes/usa-to-italy/",
    primary_seo_keyword: "pet transport usa to italy",
    primary_volume: 170,
    primary_kd: 22,
    secondary_seo_keywords: ["dog us to italy", "shipping cat to rome from us", "usa italy pet relocation", "us to milan pet flight"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from New York to Rome in 2026: which airline, which paperwork, and which Italian airport actually clears US-origin pets?" },
      { model: "Claude", phrasing: "Compare ITA Airways, Delta and Lufthansa for shipping a pet from the US to Italy in 2026, with realistic costs and routings." },
      { model: "Gemini", phrasing: "USA to Italy pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to take a dog from US to Milan in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the USA to Italy costs around $2,400 to $4,400 in 2026 by cargo flight via Lufthansa with FRA transit, ITA via Rome or Delta direct via JFK to FCO. Italy accepts US-origin pets with USDA APHIS endorsed EU health certificate, microchip and rabies vaccination at least 21 days old. Rome FCO and Milan MXP are the main entry airports.",
    h2_outline: [
      "How much does pet transport from the USA to Italy cost in 2026?",
      "Which airlines fly pet cargo from US to Italy?",
      "FCO vs MXP arrival: what's the difference?",
      "What does Italy require for US-origin pets?",
      "FAQs about USA to Italy pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-italy/ (anchor: UK to Italy comparison)",
      "/airlines/ita-airways-pet-cargo/ (anchor: ITA Airways)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via FRA)",
      "/cost-of-pet-transport-usd/ (anchor: USD cost calculator)",
      "/cdc-dog-import-rules-usa/ (anchor: CDC export rules)"
    ],
    external_links: [
      "USDA APHIS pet export to Italy — 2026",
      "Italian Ministry of Health pet import — 2026"
    ],
    ai_overview_play: "Pairs with ITA Airways (d112) for the full US-Italy story."
  },

  {
    id: "d130",
    day_number: 130,
    iso_date: "2026-11-30",
    day_of_week: "Mon",
    quarter: "Q2",
    cluster_id: "refresh-seasonal",
    cluster_name: "Seasonal refresh and timely",
    intent: "Informational",
    content_type: "Seasonal pillar",
    word_count_target: 2400,
    title: "Christmas Pet Relocation 2026: Why December Is the Hardest Month to Ship a Pet",
    title_tag: "Christmas Pet Relocation 2026 | December Shipping | PetTransportGlobal",
    meta_description: "Why December is the most expensive and most cancelled month for pet relocation in 2026: cargo embargoes, holiday queues, and how to plan around them.",
    url_slug: "/christmas-pet-relocation-december/",
    primary_seo_keyword: "christmas pet relocation",
    primary_volume: 170,
    primary_kd: 18,
    secondary_seo_keywords: ["december pet shipping cost", "shipping pet over christmas", "winter pet cargo embargo", "ship dog at christmas", "holiday pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Why is December the worst month to ship a pet internationally in 2026, and what surcharges and cancellation risks should I plan for?" },
      { model: "Claude", phrasing: "Walk me through the realities of pet relocation across the Christmas and New Year window in 2026. What blocks moves and what can still be done?" },
      { model: "Gemini", phrasing: "December pet shipping cost 2026" },
      { model: "Grok", phrasing: "Should I really ship my dog over Christmas in 2026 or wait" }
    ],
    direct_answer_40_60_words: "December is the hardest month for pet relocation in 2026 because cargo space tightens around holiday freight, Official Veterinarian appointments are scarce 22 to 31 December, and Heathrow Animal Reception and Frankfurt Animal Lounge run reduced staffing 24-26 December and 31 December to 1 January. Surcharges of 10 to 25% are typical. Plan moves in early December or after 5 January.",
    h2_outline: [
      "Why is December the worst month for pet relocation in 2026?",
      "Christmas cargo embargoes and reduced staffing windows",
      "OV appointment availability over Christmas",
      "Surcharges and cancellation risks",
      "When to plan early December vs after 5 January",
      "FAQs about Christmas pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/emergency-pet-transport/ (anchor: emergency moves)",
      "/find-an-official-veterinarian/ (anchor: OV scheduling)",
      "/process-timeline-pet-relocation/ (anchor: timeline planning)"
    ],
    external_links: [
      "Heathrow Animal Reception Centre seasonal hours — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Fills missing refresh-seasonal cluster with December-timely angle. Closes Month 6 cleanly."
  }
);
