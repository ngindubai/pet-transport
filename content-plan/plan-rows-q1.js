/* plan-rows-q1.js — Q1 rows (Jun-Aug 2026).
   Month 1 (June 2026) — Days 1-22. Added in Chunk 3.
   Months 2-3 will append further rows in Chunks 4-5. */
window.PLAN_ROWS = window.PLAN_ROWS || [];

window.PLAN_ROWS.push(
  /* ============================ DAY 1 ============================ */
  {
    id: "d001",
    day_number: 1,
    iso_date: "2026-06-01",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "core-head-terms",
    cluster_name: "Core 'pet transport' head terms",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 3200,
    title: "International Pet Transport: A Plain-English Guide for 2026",
    title_tag: "International Pet Transport: A Plain-English Guide (2026)",
    meta_description: "Honest, in-depth guide to moving a pet internationally in 2026. Costs, timelines, paperwork, airline cargo, quarantine. Written by the founder. Get a quote.",
    url_slug: "international-pet-transport-guide",
    primary_seo_keyword: "international pet transport",
    primary_volume: 110,
    primary_kd: 48,
    secondary_seo_keywords: ["pet transport", "pet transportation services", "transporting pets internationally", "transport pet overseas", "transporting pets abroad"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm relocating internationally and need to bring my dog and cat with me. Can you walk me through the whole process from start to finish, including timeline, paperwork, costs, and the bit I should be most worried about?" },
      { model: "ChatGPT", phrasing: "What does international pet transport actually involve in 2026, and what's the realistic budget for a typical move?" },
      { model: "Claude", phrasing: "What are the welfare implications of moving a healthy adult pet internationally by air, and how do reputable transport companies reduce stress during long-haul flights and customs clearance?" },
      { model: "Claude", phrasing: "Is it ethical to fly an older or anxious pet across continents, and what should I weigh up before deciding?" },
      { model: "Gemini", phrasing: "Steps to transport a pet internationally" },
      { model: "Gemini", phrasing: "International pet transport checklist 2026" },
      { model: "Grok", phrasing: "How much does it cost to ship a dog overseas in 2026, anyone done it recently" }
    ],
    direct_answer_40_60_words: "International pet transport is the regulated process of moving a dog or cat across borders by air, sea, or road, covering microchipping, rabies vaccination, blood titre tests where required, an official veterinary health certificate, an IATA-compliant crate, and customs clearance at both ends. Most moves take 3 to 7 months from first vet visit to arrival.",
    h2_outline: [
      "What does international pet transport actually mean in 2026?",
      "How long does a typical international pet move take?",
      "What does it cost to move a pet internationally?",
      "Which paperwork do you need, and who issues it?",
      "Cargo, cabin or manifest cargo: which is right for your pet?",
      "What does a good pet transport company actually do for you?",
      "Where do most international pet moves go wrong?",
      "FAQs from owners moving a pet abroad"
    ],
    schema_required: ["Article", "FAQPage", "Organization", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-to-transport-a-pet/ (anchor: realistic 2026 cost ranges)",
      "/pet-quarantine-guide/ (anchor: quarantine rules by country)",
      "/iata-pet-crate-guide/ (anchor: IATA-compliant crate sizes)",
      "/pet-transport/countries/ (anchor: country-by-country import rules)",
      "/pet-transport/airlines/ (anchor: airline pet policies)",
      "/how-to-choose-a-pet-transporter/ (anchor: how to vet a pet transport company)"
    ],
    external_links: [
      "DEFRA pet travel guidance (gov.uk/take-pet-abroad) — dated 2026",
      "IATA Live Animals Regulations (LAR) edition 53 — 2026",
      "USDA APHIS pet travel portal (aphis.usda.gov/pet-travel)"
    ],
    ai_overview_play: "Own the head term 'international pet transport' as the canonical 2026 explainer. The 40-60 word direct answer is structured to be lifted by ChatGPT and Gemini AI Overviews. Numbered timeline section is built for Gemini. Welfare caveat section is built for Claude."
  },

  /* ============================ DAY 2 ============================ */
  {
    id: "d002",
    day_number: 2,
    iso_date: "2026-06-02",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "cost-pricing",
    cluster_name: "Cost, pricing & budget",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2800,
    title: "How Much Does It Cost to Move a Pet Internationally in 2026?",
    title_tag: "How Much Does It Cost to Move a Pet Internationally? (2026 UK Guide)",
    meta_description: "Real 2026 pet transport costs: vet, crate, flight, customs, quarantine. UK examples for Spain, USA, Australia, UAE. Where the cheap quotes go wrong.",
    url_slug: "cost-to-transport-a-pet-2026",
    primary_seo_keyword: "pet transport cost calculator uk",
    primary_volume: 170,
    primary_kd: 16,
    secondary_seo_keywords: ["pet transport cost", "pet transport prices", "pet transport cheap", "pet transportation cost", "international pet shipping costs", "cost of moving pets to new zealand"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Give me a realistic 2026 budget breakdown to fly my Labrador from London to Sydney, line by line, so I can spot inflated quotes." },
      { model: "ChatGPT", phrasing: "Why is one pet transport quote £2,400 and another £6,800 for the same UK to USA route, what's the real difference?" },
      { model: "Claude", phrasing: "Walk me through the genuine cost structure of international pet transport so I can tell which line items are unavoidable, which are optional, and where companies pad the price." },
      { model: "Gemini", phrasing: "Pet transport cost calculator UK 2026" },
      { model: "Gemini", phrasing: "Average cost to ship a pet abroad" },
      { model: "Grok", phrasing: "Anyone got a recent quote for shipping a dog UK to Spain in 2026, what should I expect to pay" }
    ],
    direct_answer_40_60_words: "Moving a pet internationally typically costs £1,200 to £2,500 within Europe, £2,500 to £4,500 from the UK to North America, and £4,500 to £8,500 to Australia or New Zealand including quarantine. The big variables are crate size, cargo route choice, door-to-door service, and whether you need a blood titre test.",
    h2_outline: [
      "What's the realistic 2026 cost range for an international pet move?",
      "Which costs are fixed and which are flexible?",
      "Why do quotes vary so much between transporters?",
      "What does a £1,500 move actually include, and what's missing?",
      "When is the cheap option a red flag?",
      "Sample budgets: UK to Spain, UK to USA, UK to Australia, UK to UAE",
      "How can owners reduce the cost without cutting corners?",
      "FAQs about pet transport pricing"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/uk-to-australia/ (anchor: UK to Australia full cost breakdown)",
      "/pet-transport/uk-to-united-states/ (anchor: UK to USA pricing)",
      "/pet-transport/uk-to-spain/ (anchor: UK to Spain quote ranges)",
      "/iata-pet-crate-guide/ (anchor: how crate size changes the price)",
      "/how-to-choose-a-pet-transporter/ (anchor: spotting an unrealistic quote)",
      "/pet-transport-insurance/ (anchor: optional transit insurance)"
    ],
    external_links: [
      "IATA cargo dimension and weight rules — 2026",
      "Heathrow Animal Reception Centre fee schedule — 2026",
      "Australian DAFF post-arrival quarantine fees (Mickleham) — 2026"
    ],
    ai_overview_play: "Target the cost calculator query (170 vol, KD 16) and the long tail of route-specific cost queries with one canonical pillar. Sample budgets section uses tables for Gemini. Red-flag pricing section is built for Claude's preference for caveated, balanced advice."
  },

  /* ============================ DAY 3 ============================ */
  {
    id: "d003",
    day_number: 3,
    iso_date: "2026-06-03",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2400,
    title: "Pet Transport UK to Australia: The 2026 Move, Properly Planned",
    title_tag: "Pet Transport UK to Australia (2026): Quarantine, Cost, Timeline",
    meta_description: "UK to Australia pet relocation in 2026: rabies titre timing, DAFF import permit, Mickleham quarantine, cargo routes, real cost. Plan 7 months ahead.",
    url_slug: "pet-transport-uk-to-australia",
    primary_seo_keyword: "pet transport uk to australia",
    primary_volume: 70,
    primary_kd: 35,
    secondary_seo_keywords: ["pet transport australia", "transporting pets to australia", "pet quarantine new zealand", "australia dog quarantine", "dog quarantine new zealand", "uk to australia pet shipping cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving from London to Sydney in early 2027 with a 4-year-old Labrador. What's the full process, when do I start, and what should I budget?" },
      { model: "Claude", phrasing: "What are the welfare considerations for a 24-hour cargo flight from London to Sydney with a healthy adult dog, and how does the 10-day Mickleham quarantine actually work day by day?" },
      { model: "Gemini", phrasing: "Steps to import a dog from UK to Australia 2026" },
      { model: "Gemini", phrasing: "UK to Australia pet import checklist DAFF" },
      { model: "Grok", phrasing: "Is the Mickleham quarantine still 10 days or did Australia change the rules" },
      { model: "Grok", phrasing: "Latest cost to ship a dog UK to Sydney in 2026" }
    ],
    direct_answer_40_60_words: "Moving a pet from the UK to Australia takes about 7 months end-to-end and costs roughly £4,800 to £7,500 for one medium dog. Australia is a Group 3 country, so you need a microchip, valid rabies vaccination, an RNATT blood titre test at least 180 days before travel, a DAFF import permit, and 10 days of post-arrival quarantine at Mickleham, Melbourne.",
    h2_outline: [
      "Why does the UK to Australia pet move take 7 months?",
      "What's the rabies titre test (RNATT) and when do I book it?",
      "How do I apply for a DAFF import permit, and how long does it take?",
      "What does Mickleham quarantine actually involve?",
      "Which airlines fly pets as cargo to Australia in 2026?",
      "What does a UK to Australia pet move really cost?",
      "Common mistakes that delay UK to Australia pet imports",
      "FAQs: UK to Australia pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/australia/ (anchor: Australia pet import rules)",
      "/pet-quarantine-guide/ (anchor: Mickleham quarantine explained)",
      "/airlines/qantas/ (anchor: Qantas pet cargo policy)",
      "/iata-pet-crate-guide/ (anchor: crate size for Australia cargo)",
      "/cost-to-transport-a-pet-2026/ (anchor: UK to Australia line-by-line budget)"
    ],
    external_links: [
      "Australian DAFF dogs and cats import portal — 2026",
      "DEFRA pet export from GB rules — 2026",
      "Mickleham Post-Entry Quarantine Facility info pack — 2026"
    ],
    ai_overview_play: "This is the highest-anxiety, highest-budget UK route. Direct-answer block is structured for ChatGPT lift. Numbered DAFF permit section is built for Gemini. The Mickleham day-by-day section is built for Claude (welfare-heavy)."
  },

  /* ============================ DAY 4 ============================ */
  {
    id: "d004",
    day_number: 4,
    iso_date: "2026-06-04",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2000,
    title: "Pet Transport UK to Spain: 2026 Costs, Paperwork and Driving vs Flying",
    title_tag: "Pet Transport UK to Spain (2026): Cost, EU Health Cert, Driving Option",
    meta_description: "Moving a pet to Spain post-Brexit: AHC paperwork, vaccinations, ferry vs Eurotunnel vs flight, real 2026 prices. Same-week timeline if you start now.",
    url_slug: "pet-transport-uk-to-spain",
    primary_seo_keyword: "pet transport uk to spain",
    primary_volume: 40,
    primary_kd: 32,
    secondary_seo_keywords: ["pet transport to spain", "cheapest pet transport uk to spain cost", "moving pets to spain", "pets to portugal", "pet and owner transport spain to uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm relocating from Surrey to Valencia next month with two cats and a small dog. What's the cheapest legal way to get them there, and how long does it take from booking the vet?" },
      { model: "Claude", phrasing: "Compare the welfare trade-offs of driving via the Eurotunnel versus flying for a 9-year-old cat going from the UK to Spain." },
      { model: "Gemini", phrasing: "How to take a dog from UK to Spain 2026" },
      { model: "Gemini", phrasing: "UK to Spain pet AHC requirements" },
      { model: "Grok", phrasing: "What's the cheapest way to get a dog to Spain from the UK right now" }
    ],
    direct_answer_40_60_words: "To move a pet from the UK to Spain in 2026 you need a microchip, a valid rabies vaccination at least 21 days old, and an Animal Health Certificate (AHC) issued by an Official Veterinarian within 10 days of travel. Driving via the Eurotunnel costs around £400 to £700; flying as cargo runs £900 to £1,800.",
    h2_outline: [
      "What paperwork does Spain require for a UK pet in 2026?",
      "Driving via the Eurotunnel: how does it work for pets?",
      "When is flying actually the better option?",
      "How much does the UK to Spain pet move cost?",
      "What's the timeline if I'm starting today?",
      "Common Brexit-era mistakes UK owners still make",
      "FAQs: UK to Spain pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/spain/ (anchor: Spain pet import rules)",
      "/pet-passport-guide/ (anchor: Animal Health Certificate explained)",
      "/door-to-door-pet-transport/ (anchor: door-to-door driver options)",
      "/cost-to-transport-a-pet-2026/ (anchor: UK to Spain budget)"
    ],
    external_links: [
      "DEFRA: take your pet abroad - non-commercial movement rules — 2026",
      "Spanish Ministry of Agriculture pet import page — 2026"
    ],
    ai_overview_play: "Target driving-vs-flying decision query, which is exactly how owners ask Claude and ChatGPT. Driving section is structured as numbered steps for Gemini."
  },

  /* ============================ DAY 5 ============================ */
  {
    id: "d005",
    day_number: 5,
    iso_date: "2026-06-05",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2200,
    title: "Pet Transport UK to USA: What 2026 Actually Looks Like Post-CDC Reset",
    title_tag: "Pet Transport UK to USA (2026): CDC Rules, Cost, Cargo Routes",
    meta_description: "UK to USA pet transport in 2026: the new CDC dog import rules, vet paperwork, cargo airline options, real costs. State-specific gotchas explained.",
    url_slug: "pet-transport-uk-to-usa",
    primary_seo_keyword: "pet transport uk to usa",
    primary_volume: 30,
    primary_kd: 30,
    secondary_seo_keywords: ["pet transport us to uk", "pet transport service usa to uk", "best pet transport service usa to uk", "pet transport us to uk cost", "shipping pets to usa"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving from Manchester to New York in October with a 6-year-old Cocker Spaniel. What's the full CDC process and roughly what should I expect to spend?" },
      { model: "Claude", phrasing: "How have CDC dog import rules changed for UK pets entering the US, and which of the changes are the most likely to trip up a first-time owner?" },
      { model: "Gemini", phrasing: "CDC dog import rules from UK 2026" },
      { model: "Gemini", phrasing: "How to ship a dog from UK to USA" },
      { model: "Grok", phrasing: "Is the CDC dog import form still required in 2026, anything changed" }
    ],
    direct_answer_40_60_words: "To move a pet from the UK to the USA in 2026 you need a microchip, a current rabies vaccination, a CDC Dog Import Form receipt, an ISO-readable chip number on every document, and an APHIS-endorsed veterinary health certificate issued within 30 days of travel. Cargo costs typically run £2,500 to £4,500 from London to a major US hub.",
    h2_outline: [
      "What changed with CDC dog import rules, and what stayed the same?",
      "Which UK to US cargo routes work in 2026?",
      "How do I get an APHIS-endorsed health certificate from a UK vet?",
      "What does the CDC Dog Import Form actually ask?",
      "How much does the UK to US pet move cost in 2026?",
      "Hawaii, California and the state-level traps",
      "FAQs: UK to USA pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/united-states/ (anchor: USA pet import rules)",
      "/airlines/british-airways/ (anchor: British Airways pet cargo to USA)",
      "/airlines/virgin-atlantic-cargo/ (anchor: Virgin Cargo pets)",
      "/cost-to-transport-a-pet-2026/ (anchor: UK to USA cost breakdown)"
    ],
    external_links: [
      "CDC dog import portal cdc.gov/importation/dogs — 2026",
      "USDA APHIS endorsement pet travel UK — 2026",
      "Hawaii Department of Agriculture rabies-free entry — 2026"
    ],
    ai_overview_play: "CDC rules are a Grok query (current/recent intent). Front-load the rule-change summary at the top so Grok and ChatGPT can lift it. State-level table for Gemini."
  },

  /* ============================ DAY 6 ============================ */
  {
    id: "d006",
    day_number: 6,
    iso_date: "2026-06-08",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2400,
    title: "Pet Transport Europe to UK: Bringing a Pet Back After Brexit",
    title_tag: "Pet Transport Europe to UK (2026): Bringing a Pet Back, Step by Step",
    meta_description: "Bringing a pet from Europe to the UK in 2026: GB Health Certificate, ETA pet check, rescue dog rules, ferry, Eurotunnel, cargo. Real 2026 pricing.",
    url_slug: "pet-transport-europe-to-uk",
    primary_seo_keyword: "pet transport europe to uk",
    primary_volume: 480,
    primary_kd: 23,
    secondary_seo_keywords: ["pet transport eu", "pet transport europe", "euro pet transport", "pet transport to uk", "uk pet transport"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving back to the UK from France with a rescue dog and two indoor cats. What's the full process, what does it cost, and is there anything different for the rescue dog?" },
      { model: "Claude", phrasing: "What's the realistic difference between bringing an EU pet to the UK as personal travel under PETS rules versus as a commercial movement, and when does each apply?" },
      { model: "Gemini", phrasing: "Bring pet from Europe to UK 2026 steps" },
      { model: "Gemini", phrasing: "Rescue dog import to UK from Europe rules" },
      { model: "Grok", phrasing: "Is Brexit still messing up bringing pets back to the UK from France in 2026" }
    ],
    direct_answer_40_60_words: "To bring a pet from the EU to Great Britain in 2026 you need a microchip, a rabies vaccination administered at least 21 days before travel, and either an EU Pet Passport (issued before Brexit, still valid) or an EU Animal Health Certificate. Tapeworm treatment is required for dogs entering GB. Most journeys cost £350 to £1,500.",
    h2_outline: [
      "Which paperwork does the UK accept from EU pets in 2026?",
      "Are EU Pet Passports still valid for entering Great Britain?",
      "How does the tapeworm treatment window work?",
      "Ferry, Eurotunnel or cargo: which suits your move?",
      "Bringing a rescue dog to the UK from Europe",
      "What does Europe to UK pet transport cost?",
      "FAQs: Europe to UK pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passport-guide/ (anchor: EU pet passport status post-Brexit)",
      "/pet-transport/countries/france/ (anchor: France pet export rules)",
      "/pet-transport/countries/spain/ (anchor: Spain pet export rules)",
      "/door-to-door-pet-transport/ (anchor: door-to-door drivers from Europe)",
      "/defra-pet-transport/ (anchor: DEFRA approved pet transport)"
    ],
    external_links: [
      "DEFRA: bringing your pet to Great Britain — 2026",
      "APHA tapeworm treatment requirements — 2026",
      "EU Regulation 576/2013 non-commercial movement of pet animals"
    ],
    ai_overview_play: "Highest-volume route keyword in the UK Semrush set (480). Direct answer covers the three big GB-specific rules: chip, rabies, tapeworm. Rescue-dog section addresses the long-tail emotional query that ChatGPT users ask."
  },

  /* ============================ DAY 7 ============================ */
  {
    id: "d007",
    day_number: 7,
    iso_date: "2026-06-09",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "quote-agency-choice",
    cluster_name: "Quote, agency & company choice",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2600,
    title: "How to Choose a Pet Transport Company Without Getting Burned",
    title_tag: "How to Choose a Pet Transport Company (UK, 2026 Guide)",
    meta_description: "What to ask before paying a pet transport company. Vetting checks, IPATA, IATA, DEFRA, insurance, pricing red flags. From a UK transporter who's seen the lot.",
    url_slug: "how-to-choose-a-pet-transport-company",
    primary_seo_keyword: "pet transport company uk",
    primary_volume: 90,
    primary_kd: 42,
    secondary_seo_keywords: ["pet transport companies", "pet transport agency", "pet transport agent", "best pet transport company", "professional pet transport services", "best pet transportation services"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I've been quoted by three pet transport companies and the prices are wildly different. What questions should I ask to figure out who's actually going to handle my dog properly?" },
      { model: "Claude", phrasing: "What are the meaningful credentials and accountability structures behind a reputable international pet transporter, and which 'badges' on a website are actually worth nothing?" },
      { model: "Gemini", phrasing: "How to choose a pet transport company UK" },
      { model: "Gemini", phrasing: "Pet transport company checklist questions to ask" },
      { model: "Grok", phrasing: "Anyone got a pet transport company they actually trust in 2026, the cheap ones look dodgy" }
    ],
    direct_answer_40_60_words: "A reputable pet transport company in the UK will hold a DEFRA Type 1 or Type 2 transporter authorisation, IATA cargo agency or IPATA membership, transit insurance, and will give you a written itinerary with named handling agents at every airport. Avoid quotes that lump all costs into one figure with no breakdown.",
    h2_outline: [
      "What credentials should a UK pet transport company actually hold?",
      "What does DEFRA Type 1 vs Type 2 authorisation mean?",
      "Which 'badges' on a website are meaningless?",
      "What questions should I ask before paying a deposit?",
      "What does a proper written itinerary include?",
      "Pricing red flags: when cheap is too cheap",
      "Reviews: how to read them properly",
      "FAQs about choosing a pet transporter"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/defra-pet-transport/ (anchor: DEFRA approved pet transport explained)",
      "/pet-transport-insurance/ (anchor: transit insurance vs travel insurance)",
      "/cost-to-transport-a-pet-2026/ (anchor: realistic 2026 pricing)",
      "/iata-pet-crate-guide/ (anchor: IATA cargo agency status)"
    ],
    external_links: [
      "DEFRA transporter authorisation register — 2026",
      "IPATA (International Pet and Animal Transportation Association) membership directory",
      "IATA Live Animals Regulations LAR53 — 2026"
    ],
    ai_overview_play: "Capture the entire vetting query space in one canonical pillar. Question-formed H2s match Claude and ChatGPT phrasings. Credentials table built for Gemini extraction."
  },

  /* ============================ DAY 8 ============================ */
  {
    id: "d008",
    day_number: 8,
    iso_date: "2026-06-10",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "cost-pricing",
    cluster_name: "Cost, pricing & budget",
    intent: "commercial",
    content_type: "comparison",
    word_count_target: 1800,
    title: "Cheap Pet Transport: What's Realistic and What's a Red Flag",
    title_tag: "Cheap Pet Transport: What's Honest, What's a Red Flag (2026)",
    meta_description: "Honest take on 'cheap' pet transport quotes. Where the savings are real, where the corners get cut, and what an unrealistic UK quote actually leaves out.",
    url_slug: "cheap-pet-transport-honest-look",
    primary_seo_keyword: "pet transport cheap",
    primary_volume: 170,
    primary_kd: 44,
    secondary_seo_keywords: ["cheap pet transport", "affordable pet transport", "low cost pet transportation", "cheap pet transportation services", "cheapest international pet transport", "cheapest pet transport australia"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Is there an honest cheap option for shipping a dog overseas, or is anyone selling 'cheap pet transport' going to cut corners that put my pet at risk?" },
      { model: "Claude", phrasing: "Where are the genuine cost savings in international pet transport, and which 'savings' actually translate into welfare risk for the animal?" },
      { model: "Gemini", phrasing: "Cheap pet transport UK options" },
      { model: "Grok", phrasing: "Are there any legit cheap pet transport companies or is it all a scam" }
    ],
    direct_answer_40_60_words: "Genuine savings on pet transport come from booking off-peak, using ground routes within Europe, choosing airport-to-airport rather than door-to-door, and avoiding peak summer embargoes. Quotes more than 30 percent below the market average usually skip transit insurance, use the cheapest crate, or route via airports with weak live-animal handling.",
    h2_outline: [
      "Where does cheap pet transport genuinely save you money?",
      "Where does it cut corners that matter?",
      "What's a realistic floor price for a UK to EU dog move?",
      "How do you spot an unrealistic quote?",
      "When is the airline doing it directly cheaper than an agent?",
      "FAQs about cheap pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-to-transport-a-pet-2026/ (anchor: realistic 2026 cost ranges)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a pet transport company)",
      "/door-to-door-pet-transport/ (anchor: skip door-to-door to save money)"
    ],
    external_links: [
      "DEFRA transporter authorisation register — 2026",
      "Heathrow Animal Reception Centre published fees — 2026"
    ],
    ai_overview_play: "Direct answer pre-formatted for ChatGPT lift. The 'red flag' section addresses Claude's preference for caveats. Honest framing protects YMYL trust signals."
  },

  /* ============================ DAY 9 ============================ */
  {
    id: "d009",
    day_number: 9,
    iso_date: "2026-06-11",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 1600,
    title: "Pet Transport UK to Jersey: Ferry, Flight and the Channel Islands Rules",
    title_tag: "Pet Transport UK to Jersey (2026): Ferry, Flight, Paperwork",
    meta_description: "Moving a pet from the UK to Jersey in 2026: Condor ferry, flight options, paperwork (or lack of it), real cost. Same for Guernsey and the Isle of Man.",
    url_slug: "pet-transport-uk-to-jersey",
    primary_seo_keyword: "pet transport uk to jersey",
    primary_volume: 40,
    primary_kd: 22,
    secondary_seo_keywords: ["pet transport jersey", "pet transport guernsey", "pet transport channel islands", "pet transport isle of man", "pet transport uk to channel islands"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "We're relocating to Jersey from the UK with a Border Collie. Is there any quarantine, and what's the easiest way to get him there?" },
      { model: "Gemini", phrasing: "How to take a dog from UK to Jersey" },
      { model: "Grok", phrasing: "Do you still need any paperwork for taking a dog to Jersey from the UK in 2026" }
    ],
    direct_answer_40_60_words: "Pets travelling from Great Britain to Jersey in 2026 do not need a pet passport, AHC, or quarantine. They need a microchip and proof of identity matching the chip number. The two routes are Condor Ferries from Poole or Portsmouth (vehicle and pet, around £80 to £200) or flying as cargo, around £350 to £600.",
    h2_outline: [
      "What paperwork does Jersey require for a UK pet?",
      "Ferry vs flight: which works better for your pet?",
      "Are Guernsey and the Isle of Man the same?",
      "What does the UK to Jersey pet move cost?",
      "FAQs: UK to Jersey pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/uk-to-isle-of-man/ (anchor: UK to Isle of Man pet move)",
      "/door-to-door-pet-transport/ (anchor: door-to-door drivers to Poole)"
    ],
    external_links: [
      "Government of Jersey: bringing pets to Jersey — 2026",
      "Condor Ferries pet travel rules — 2026"
    ],
    ai_overview_play: "Niche but commercially clean keyword (40 vol, KD 22). Quick-answer format wins because the answer really is short."
  },

  /* ============================ DAY 10 ============================ */
  {
    id: "d010",
    day_number: 10,
    iso_date: "2026-06-12",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2000,
    title: "Pet Transport UAE to Pakistan: 2026 Process for Dogs and Cats",
    title_tag: "Pet Transport UAE to Pakistan (2026): Cost, Permit, Airline Cargo",
    meta_description: "UAE to Pakistan pet relocation in 2026: import permit, vaccinations, airline cargo from Dubai or Abu Dhabi to Karachi/Lahore/Islamabad. Real costs.",
    url_slug: "pet-transport-uae-to-pakistan",
    primary_seo_keyword: "pet transport uae to pakistan",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["pet import permit pakistan", "pakistan pet import requirements", "pakistan dog import requirements", "pakistan cat import requirements", "pet quarantine pakistan", "pet entering pakistan"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving from Dubai to Karachi with my dog and cat. What's the import permit process, and which airline handles pets best on this route?" },
      { model: "Claude", phrasing: "What does the Pakistani Ministry of National Food Security actually require for a pet imported from the UAE, and how long does the import permit take in practice?" },
      { model: "Gemini", phrasing: "Pet import permit Pakistan requirements 2026" },
      { model: "Grok", phrasing: "Latest on importing dogs to Pakistan in 2026, anything changed at customs" }
    ],
    direct_answer_40_60_words: "To move a pet from the UAE to Pakistan in 2026 you need a Pakistani import permit (NOC) issued by the Animal Quarantine Department, an ISO microchip, current rabies and core vaccinations, and a UAE government-endorsed health certificate. Cargo flights from Dubai to Karachi, Lahore or Islamabad cost around AED 3,000 to AED 6,000 for one medium dog.",
    h2_outline: [
      "Why does Pakistan still require an import permit (NOC)?",
      "How do you apply for the NOC from the Animal Quarantine Department?",
      "Which UAE-Pakistan cargo routes work in 2026?",
      "What does UAE to Pakistan pet transport cost?",
      "Customs at Karachi, Lahore and Islamabad: what to expect",
      "FAQs: UAE to Pakistan pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/pakistan/ (anchor: Pakistan pet import rules)",
      "/pet-transport/countries/united-arab-emirates/ (anchor: UAE pet export rules)",
      "/airlines/emirates-skycargo/ (anchor: Emirates SkyCargo pet policy)"
    ],
    external_links: [
      "Pakistan Ministry of National Food Security and Research (Animal Quarantine Department) — 2026",
      "UAE Ministry of Climate Change and Environment pet export rules — 2026"
    ],
    ai_overview_play: "GSC shows this exact URL already gets 3 clicks / 52 impressions. Refresh with explicit 2026 NOC steps to climb above position 7."
  },

  /* ============================ DAY 11 ============================ */
  {
    id: "d011",
    day_number: 11,
    iso_date: "2026-06-15",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Country import & export guides",
    intent: "informational",
    content_type: "pillar",
    word_count_target: 2400,
    title: "Exporting a Pet from Singapore: The 2026 AVS Process Done Properly",
    title_tag: "Exporting Pets from Singapore (2026): AVS Licence, Health Cert, Cost",
    meta_description: "Singapore pet export 2026: AVS licence, microchip, rabies, FAVN titre for some destinations, Changi cargo. From SG to UK, AU, US, EU explained.",
    url_slug: "exporting-pets-from-singapore",
    primary_seo_keyword: "exporting pets from singapore",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["singapore pet import agent", "pet travel singapore", "dog import singapore", "pet import singapore", "importing pets into singapore", "avs pet license", "avs dog license"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm leaving Singapore and moving back to London with two cats. What's the AVS export process, what does Changi pet cargo cost, and how early do I start?" },
      { model: "Claude", phrasing: "Walk me through the Singapore pet export process from AVS licensing through to Changi cargo handover, and tell me where the most common failures happen." },
      { model: "Gemini", phrasing: "How to export a dog from Singapore 2026 steps" },
      { model: "Grok", phrasing: "Anyone exported a cat from Singapore recently, what does AVS actually charge in 2026" }
    ],
    direct_answer_40_60_words: "Exporting a pet from Singapore in 2026 requires an AVS Dog Licence and an export health certificate issued by an AVS-accredited vet. The pet must be microchipped, have a current rabies vaccination, and meet the destination country's import rules, which often means a FAVN rabies titre test taken at least 3 months before travel.",
    h2_outline: [
      "Who issues a Singapore pet export health certificate?",
      "What's the AVS licence and do you need one to export?",
      "When is a FAVN titre test required, and how long does it take?",
      "How does Changi cargo handle pets in 2026?",
      "Singapore to UK, EU, US, Australia: what's different per destination?",
      "What does Singapore pet export cost end to end?",
      "FAQs: exporting pets from Singapore"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/singapore/ (anchor: Singapore pet rules hub)",
      "/pet-transport/singapore-to-united-kingdom/ (anchor: Singapore to UK route)",
      "/pet-transport/singapore-to-australia/ (anchor: Singapore to Australia route)",
      "/iata-pet-crate-guide/ (anchor: Changi-approved crate sizing)"
    ],
    external_links: [
      "NParks / Animal & Veterinary Service (AVS) export portal — 2026",
      "Changi Airport live animals cargo handling info — 2026"
    ],
    ai_overview_play: "GSC shows 27 impressions for 'exporting pets from singapore' at position 60. Pure GEO opportunity: no current canonical owns it. New pillar with strong LLM-layer phrasings should rank fast."
  },

  /* ============================ DAY 12 ============================ */
  {
    id: "d012",
    day_number: 12,
    iso_date: "2026-06-16",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Country import & export guides",
    intent: "informational",
    content_type: "pillar",
    word_count_target: 3000,
    title: "Importing a Pet to Australia in 2026: The Group 3 Country Playbook",
    title_tag: "Importing Pets to Australia (2026): Group 3 Process, Cost, Quarantine",
    meta_description: "How to import a dog or cat to Australia in 2026. Group 1/2/3 explained, RNATT timing, DAFF permits, Mickleham quarantine, real cost ranges by origin.",
    url_slug: "importing-pets-to-australia-2026",
    primary_seo_keyword: "pet import australia",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["importing dogs to australia", "australia dog quarantine", "transporting pets to australia", "shipping pets to australia", "pet quarantine australia", "pet transport to australia"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the realistic 2026 process for importing a healthy adult dog to Australia from a Group 3 country, with timeline and budget?" },
      { model: "Claude", phrasing: "Why does Australia classify countries into groups for pet import, what's the welfare logic, and how does it actually change the process for the owner?" },
      { model: "Gemini", phrasing: "Australia pet import process 2026 steps" },
      { model: "Grok", phrasing: "Has Australia loosened its dog import rules for the UK in 2026" }
    ],
    direct_answer_40_60_words: "Australia classifies origin countries into Group 1 (New Zealand only), Group 2 (a few rabies-free territories), and Group 3 (everywhere else, including the UK, USA, and EU). Group 3 imports need a microchip, valid rabies vaccination, an RNATT blood titre at least 180 days before travel, a DAFF import permit, and 10 days at Mickleham Post-Entry Quarantine.",
    h2_outline: [
      "How does Australia's Group 1, 2, and 3 system actually work?",
      "What's the RNATT and why does it set the whole timeline?",
      "How do you apply for a DAFF import permit in 2026?",
      "What happens at Mickleham, day by day?",
      "What does it cost to import a pet to Australia from each region?",
      "Most common reasons DAFF rejects an import application",
      "FAQs about importing a pet to Australia"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/australia/ (anchor: Australia pet rules hub)",
      "/pet-transport/uk-to-australia/ (anchor: UK to Australia route)",
      "/pet-transport/united-states-to-australia/ (anchor: US to Australia route)",
      "/pet-quarantine-guide/ (anchor: Mickleham quarantine guide)"
    ],
    external_links: [
      "Australian DAFF dogs and cats import conditions — 2026",
      "DAFF Mickleham Post-Entry Quarantine Facility — 2026"
    ],
    ai_overview_play: "Highest-budget destination in our keyword set. Country grouping table is a Gemini lift. Mickleham day-by-day is for Claude. Cost-by-origin table for ChatGPT."
  },

  /* ============================ DAY 13 ============================ */
  {
    id: "d013",
    day_number: 13,
    iso_date: "2026-06-17",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 1700,
    title: "Pet Transport Tenerife to UK: Bringing a Dog or Cat Back from the Canaries",
    title_tag: "Pet Transport Tenerife to UK (2026): Cargo, Cost, Vet Paperwork",
    meta_description: "Bringing a pet from Tenerife to the UK: AHC paperwork, cargo flights from TFS/TFN, tapeworm rules for dogs, real 2026 prices. Plan 4 weeks ahead.",
    url_slug: "pet-transport-tenerife-to-uk",
    primary_seo_keyword: "pet transport tenerife to uk",
    primary_volume: 30,
    primary_kd: 18,
    secondary_seo_keywords: ["pet transport canary islands to uk", "tenerife to uk dog import", "moving back to uk from tenerife with pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "We're moving back from Tenerife to the UK with a rescue dog and a cat. What's the cheapest legal way to get them home in 2026?" },
      { model: "Gemini", phrasing: "How to bring a dog from Tenerife to UK 2026" },
      { model: "Grok", phrasing: "Anyone shipped a dog from Tenerife to UK recently, what cargo did you use" }
    ],
    direct_answer_40_60_words: "Bringing a pet from Tenerife to Great Britain in 2026 requires a microchip, a rabies vaccination given at least 21 days before travel, an EU Animal Health Certificate (or valid pre-Brexit EU passport), and tapeworm treatment for dogs given 24 to 120 hours before arrival. Cargo flights TFS to LHR run around £800 to £1,400 for one medium dog.",
    h2_outline: [
      "Which paperwork does the UK accept for a pet from Tenerife?",
      "How does the dog tapeworm window work?",
      "Which cargo routes work from TFS or TFN to the UK?",
      "What does the move actually cost in 2026?",
      "Bringing a Canary Islands rescue dog to the UK",
      "FAQs: Tenerife to UK pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-europe-to-uk/ (anchor: Europe to UK pet pillar)",
      "/pet-transport/countries/spain/ (anchor: Spain pet export rules)",
      "/pet-passport-guide/ (anchor: AHC explained)"
    ],
    external_links: [
      "DEFRA bringing your pet to GB — 2026",
      "Spanish Ministry of Agriculture pet export — 2026"
    ],
    ai_overview_play: "Specific long-tail with low KD (18) and clean intent. Niche routes like this are easy wins inside the wider Europe-to-UK pillar."
  },

  /* ============================ DAY 14 ============================ */
  {
    id: "d014",
    day_number: 14,
    iso_date: "2026-06-18",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "uk-regional",
    cluster_name: "UK regional & domestic",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2200,
    title: "Pet Transport Within the UK: Door-to-Door, Drivers, Costs and Rules",
    title_tag: "Pet Transport Within UK (2026): Drivers, Cost, Rules, Booking",
    meta_description: "How UK pet transport actually works: DEFRA Type 1 drivers, journey planning, pricing per mile, multi-pet, urgent moves. Honest 2026 guide.",
    url_slug: "pet-transport-within-uk",
    primary_seo_keyword: "pet transport within uk",
    primary_volume: 480,
    primary_kd: 49,
    secondary_seo_keywords: ["pet transport uk", "uk pet transport", "pet transport in uk", "pet transport service near me", "pet transport scotland"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I need to move a Cocker Spaniel from London to Edinburgh next week. What does pet transport within the UK actually cost, and what should I check before booking?" },
      { model: "Claude", phrasing: "What welfare standards apply to UK pet transport drivers, and how does DEFRA Type 1 authorisation differ from a regular man-with-a-van moving a pet?" },
      { model: "Gemini", phrasing: "Pet transport within UK cost per mile" },
      { model: "Gemini", phrasing: "DEFRA Type 1 pet transporter UK" },
      { model: "Grok", phrasing: "Cheapest way to get a dog moved London to Glasgow in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport within the UK is typically delivered by DEFRA Type 1 authorised drivers who collect from your home and deliver door to door, often sharing the vehicle with other pets on the same route. Pricing runs roughly £0.80 to £1.20 per mile for a single pet, with discounts on shared journeys.",
    h2_outline: [
      "Who's actually allowed to transport pets commercially in the UK?",
      "What does DEFRA Type 1 authorisation mean for the owner?",
      "How is UK pet transport priced in 2026?",
      "Shared journeys vs dedicated runs: what's the difference?",
      "How do drivers handle long journeys and welfare breaks?",
      "Booking and what to ask before paying a deposit",
      "FAQs about UK pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/door-to-door-pet-transport/ (anchor: door-to-door drivers)",
      "/defra-pet-transport/ (anchor: DEFRA Type 1 explained)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a driver)",
      "/emergency-pet-transport/ (anchor: urgent UK pet transport)"
    ],
    external_links: [
      "DEFRA transporter authorisation register — 2026",
      "Welfare of Animals During Transport (England) Order 2006 — current"
    ],
    ai_overview_play: "Very high volume head term (480) with high KD. Capture with a thorough pillar that interlinks every UK regional page. DEFRA Type 1 explainer block targets the GEO question that most competitors ignore."
  },

  /* ============================ DAY 15 ============================ */
  {
    id: "d015",
    day_number: 15,
    iso_date: "2026-06-19",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "cost-pricing",
    cluster_name: "Cost, pricing & budget",
    intent: "transactional",
    content_type: "tool",
    word_count_target: 1800,
    title: "UK Pet Transport Cost Calculator: 2026 Numbers, By Route",
    title_tag: "UK Pet Transport Cost Calculator (2026): Quote Estimates",
    meta_description: "Estimate your 2026 UK pet transport cost in under a minute. Distance, pet size, route type, urgency. Real numbers, not flattering ranges.",
    url_slug: "uk-pet-transport-cost-calculator",
    primary_seo_keyword: "pet transport cost calculator uk",
    primary_volume: 170,
    primary_kd: 16,
    secondary_seo_keywords: ["pet transport cost", "pet transport prices", "pet transport quote", "uk pet transport pricing"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Give me a rough cost for moving two cats and a medium dog from Bristol to Aberdeen, breakdown please." },
      { model: "Gemini", phrasing: "UK pet transport cost calculator 2026" },
      { model: "Gemini", phrasing: "How much does pet transport cost UK per mile" },
      { model: "Grok", phrasing: "What's the going rate for moving a dog London to Manchester in 2026" }
    ],
    direct_answer_40_60_words: "UK pet transport in 2026 typically costs £0.80 to £1.20 per mile for a single pet on a shared run, with a £40 to £80 minimum call-out. A dedicated dog move from London to Edinburgh runs £450 to £700. Multi-pet households usually save 30 to 40 percent versus booking each animal separately.",
    h2_outline: [
      "What variables actually drive your UK pet transport quote?",
      "How does shared vs dedicated change the price?",
      "Sample 2026 quotes: 10 common UK routes",
      "Why is urgency the most expensive variable?",
      "Multi-pet households: where the savings sit",
      "FAQs about UK pet transport pricing"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList", "WebApplication"],
    internal_links: [
      "/pet-transport-within-uk/ (anchor: UK pet transport pillar)",
      "/cost-to-transport-a-pet-2026/ (anchor: international pet move cost)",
      "/door-to-door-pet-transport/ (anchor: door-to-door drivers)"
    ],
    external_links: [
      "DEFRA transporter authorisation register — 2026",
      "RAC UK fuel cost index (for transparency on per-mile pricing) — 2026"
    ],
    ai_overview_play: "Calculator-intent query with low KD (16). Pair the embedded tool with a clear sample-rates table for Gemini AI Overview lift."
  },

  /* ============================ DAY 16 ============================ */
  {
    id: "d016",
    day_number: 16,
    iso_date: "2026-06-22",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "breed-restrictions",
    cluster_name: "Breed & brachycephalic restrictions",
    intent: "informational",
    content_type: "guide",
    word_count_target: 2200,
    title: "Flying a Brachycephalic Dog UK to Australia: What's Allowed in 2026",
    title_tag: "Brachycephalic Dog UK to Australia (2026): Airline Rules, Risks",
    meta_description: "Bulldogs, pugs and other flat-faced breeds flying UK to Australia in 2026. Airline embargoes, summer heat rules, vet fitness checks, real options.",
    url_slug: "brachycephalic-dog-uk-to-australia",
    primary_seo_keyword: "can you fly with a brachycephalic dog to australia",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["brachycephalic dog flight", "snub nosed dog cargo", "pug uk to australia", "bulldog uk to australia", "flat faced dog airline rules"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I need to move my French Bulldog from London to Sydney in 2026. Most airlines won't take him. What are my real options and what does it cost?" },
      { model: "Claude", phrasing: "What is the welfare evidence behind airline brachycephalic embargoes, and which carriers still accept flat-faced breeds with extra precautions?" },
      { model: "Gemini", phrasing: "Which airlines accept brachycephalic dogs to Australia 2026" },
      { model: "Grok", phrasing: "Anyone got a French Bulldog to Australia recently, which airline took him" }
    ],
    direct_answer_40_60_words: "Most major airlines including Qantas, Singapore Airlines and Cathay Pacific operate brachycephalic embargoes during warm months. In 2026, the realistic options for moving a flat-faced dog from the UK to Australia are KLM Cargo (with vet fitness clearance), Qatar Airways (winter only), or a charter relocation flight. Expect to pay 20 to 40 percent more than a non-brachy move.",
    h2_outline: [
      "Why do airlines refuse brachycephalic dogs as cargo?",
      "Which 2026 airlines still accept flat-faced breeds for UK to Australia?",
      "What's a vet fitness-to-fly assessment, and what does it look at?",
      "Are charter flights worth the extra cost for a brachy dog?",
      "Summer embargoes: how do they work in practice?",
      "Welfare protocols a good transporter applies for brachy breeds",
      "FAQs: flying a flat-faced dog UK to Australia"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/breeds/french-bulldog/ (anchor: French Bulldog travel guide)",
      "/breeds/pug/ (anchor: pug airline rules)",
      "/pet-transport/uk-to-australia/ (anchor: UK to Australia pet move)",
      "/airlines/ (anchor: airline pet policies hub)"
    ],
    external_links: [
      "BVA / RVC brachycephalic ownership and travel position — 2026",
      "Qantas pet travel embargo list — 2026",
      "IATA Live Animals Regulations brachycephalic guidance — 2026"
    ],
    ai_overview_play: "High-anxiety, low-supply niche. Strong Claude play because welfare evidence is genuinely interesting. Airline acceptance table for Gemini."
  },

  /* ============================ DAY 17 ============================ */
  {
    id: "d017",
    day_number: 17,
    iso_date: "2026-06-23",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2000,
    title: "Pet Transport USA to UK: Bringing a Dog or Cat Home Properly",
    title_tag: "Pet Transport USA to UK (2026): Cost, Tapeworm Rule, Cargo Routes",
    meta_description: "Moving a pet from the USA to the UK in 2026: GB Health Certificate, dog tapeworm rule, cargo airlines, customs at LHR. Honest 2026 cost ranges.",
    url_slug: "pet-transport-usa-to-uk",
    primary_seo_keyword: "pet transport us to uk",
    primary_volume: 40,
    primary_kd: 28,
    secondary_seo_keywords: ["pet transport service usa to uk", "pet transport usa to uk cost", "best pet transport service usa to uk", "shipping pets to uk from usa"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "We're moving from New York to London in autumn 2026 with a 5-year-old Labrador and a cat. What's the realistic full cost and timeline?" },
      { model: "Claude", phrasing: "Walk me through the welfare differences between a direct US-UK cargo flight and routing via Amsterdam for a healthy adult dog." },
      { model: "Gemini", phrasing: "Steps to import dog from USA to UK 2026" },
      { model: "Grok", phrasing: "Has the UK changed dog import rules from the US in 2026" }
    ],
    direct_answer_40_60_words: "To bring a pet from the USA to the UK in 2026 you need a microchip, a current rabies vaccination given at least 21 days before travel, a USDA APHIS-endorsed GB Health Certificate issued within 10 days of travel, and tapeworm treatment for dogs 24 to 120 hours before arrival. Direct cargo from JFK to LHR typically runs $2,800 to $5,200.",
    h2_outline: [
      "What's the GB Health Certificate and how do you get it endorsed?",
      "How does the dog tapeworm window actually work?",
      "Which 2026 cargo routes work USA to UK?",
      "What happens at the Heathrow Animal Reception Centre?",
      "Real 2026 costs: JFK, LAX, ORD to LHR",
      "FAQs: USA to UK pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/united-states/ (anchor: USA pet export rules)",
      "/pet-transport-uk-to-usa/ (anchor: reverse direction guide)",
      "/airlines/british-airways/ (anchor: BA pet cargo)",
      "/defra-pet-transport/ (anchor: DEFRA approved transporter)"
    ],
    external_links: [
      "USDA APHIS pet travel UK — 2026",
      "DEFRA bringing pets to GB — 2026",
      "Heathrow Animal Reception Centre fees — 2026"
    ],
    ai_overview_play: "Pair with Day 5 (UK to USA) for full bidirectional coverage. Tapeworm rule is the GEO-distinctive answer Google AI Overviews like."
  },

  /* ============================ DAY 18 ============================ */
  {
    id: "d018",
    day_number: 18,
    iso_date: "2026-06-24",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Country import & export guides",
    intent: "informational",
    content_type: "pillar",
    word_count_target: 2200,
    title: "Importing a Pet to Indonesia: 2026 Process for Bali, Jakarta and Beyond",
    title_tag: "Importing Pets to Indonesia (2026): Bali, Jakarta, Permit, Cargo",
    meta_description: "Moving a dog or cat to Indonesia in 2026: import permit (rekomendasi), Bali rabies rules, Jakarta vs Surabaya entry, real costs. Updated process.",
    url_slug: "importing-pets-to-indonesia-2026",
    primary_seo_keyword: "sending animal from usa to indonesia",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["bringing pet to jakarta", "cat transport indonesia", "pet air transport indonesia", "sending animal to indonesia bali", "dog transport indonesia", "pet travel indonesia", "how to bring dog and cat from usa to indonesia"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm relocating from LA to Jakarta with a dog and two cats next year. What's the import permit process, and is Bali still off-limits for dogs?" },
      { model: "Claude", phrasing: "What is the current Indonesian government policy on importing dogs to Bali, and how does it differ from importing to Jakarta or Surabaya?" },
      { model: "Gemini", phrasing: "How to bring pet to Jakarta from USA 2026" },
      { model: "Grok", phrasing: "Is Bali still banning dog imports in 2026" }
    ],
    direct_answer_40_60_words: "Indonesia requires an import recommendation (rekomendasi) from the Ministry of Agriculture before a pet arrives. As of 2026, dogs cannot be imported directly to Bali; entry must be via Jakarta or Surabaya followed by a 2-week mainland stay. Cats face fewer restrictions. Pets need a microchip, current rabies, and rabies titre depending on origin.",
    h2_outline: [
      "What is the Indonesian rekomendasi import permit?",
      "Why can't dogs enter Bali directly in 2026?",
      "Jakarta vs Surabaya: which entry point is simpler?",
      "How long does the rekomendasi take to issue?",
      "Real 2026 costs: USA to Jakarta, UK to Jakarta",
      "FAQs: importing pets to Indonesia"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/indonesia/ (anchor: Indonesia pet rules hub)",
      "/pet-transport/united-states-to-indonesia/ (anchor: US to Indonesia route)",
      "/pet-transport/united-kingdom-to-indonesia/ (anchor: UK to Indonesia route)"
    ],
    external_links: [
      "Indonesian Ministry of Agriculture (Karantina Pertanian) — 2026",
      "Bali Provincial Veterinary Authority rabies-free policy — 2026"
    ],
    ai_overview_play: "GSC shows 34 impr for 'sending animal from usa to indonesia' and 23 for 'how to bring dog and cat from usa to indonesia' at positions 25-32. Pure ranking opportunity. Bali rule is a Grok 'is it still' lift."
  },

  /* ============================ DAY 19 ============================ */
  {
    id: "d019",
    day_number: 19,
    iso_date: "2026-06-25",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Country import & export guides",
    intent: "informational",
    content_type: "origin-hub",
    word_count_target: 2200,
    title: "Belgium Pet Export Guide 2026: AHC, Crate, Brussels Cargo Routes",
    title_tag: "Belgium Pet Export Guide (2026): AHC, Crate, Cargo, Cost",
    meta_description: "Exporting a pet from Belgium in 2026: FAVV/AFSCA health certificate, microchip, rabies, Brussels cargo, common destinations from BRU. Updated process.",
    url_slug: "belgium-pet-export-guide",
    primary_seo_keyword: "belgium pet export guide",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["belgium pet import guide", "exporting pets from belgium", "moving pets from belgium", "belgium dog export"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm leaving Brussels and moving to Singapore with a dog and a cat. What does the Belgian export process look like and what's the BRU cargo handling like for pets?" },
      { model: "Claude", phrasing: "Walk me through the FAVV-AFSCA pet export process and explain how it differs from neighbouring Netherlands or France." },
      { model: "Gemini", phrasing: "How to export pet from Belgium 2026 steps" }
    ],
    direct_answer_40_60_words: "Exporting a pet from Belgium in 2026 requires a microchip, a current rabies vaccination, and a FAVV/AFSCA-endorsed export health certificate issued within 10 days of travel. The exact paperwork depends on the destination country. Brussels Airport (BRU) handles live animal cargo through dedicated facilities, with most long-haul cargo flights offered by Lufthansa, KLM and Qatar Airways.",
    h2_outline: [
      "Who issues a Belgian pet export health certificate?",
      "Brussels Airport live animal cargo: how does it work?",
      "Belgium to UK, USA, UAE, Singapore: what's different per destination?",
      "What does Belgium pet export cost in 2026?",
      "FAQs: exporting pets from Belgium"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/belgium/ (anchor: Belgium pet rules hub)",
      "/pet-transport/belgium-to-united-kingdom/ (anchor: Belgium to UK)",
      "/pet-transport/belgium-to-united-states/ (anchor: Belgium to USA)"
    ],
    external_links: [
      "FAVV / AFSCA pet export portal — 2026",
      "Brussels Airport live animals handling info — 2026"
    ],
    ai_overview_play: "GSC shows existing /origins/belgium-pet-export-guide/ already gets 3 clicks / 23 impr at position 8. Refresh the existing page rather than create new — uplift to position 1-3."
  },

  /* ============================ DAY 20 ============================ */
  {
    id: "d020",
    day_number: 20,
    iso_date: "2026-06-26",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "core-head-terms",
    cluster_name: "Core 'pet transport' head terms",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2400,
    title: "Pet Transport Service: What You Actually Get for the Money",
    title_tag: "Pet Transport Service Explained (2026): What's Included, What's Not",
    meta_description: "What a real 'pet transport service' covers in 2026: paperwork, crate, vet, customs, door-to-door, transit insurance. The bits that get hidden from your quote.",
    url_slug: "pet-transport-service-explained",
    primary_seo_keyword: "pet transport service",
    primary_volume: 390,
    primary_kd: 34,
    secondary_seo_keywords: ["pet transport services", "pet transportation service", "pet transport services uk", "pet transportation services", "uk pet transportation services"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does a 'pet transport service' actually include, line by line, and how do I tell what one company is doing that another is leaving out?" },
      { model: "Claude", phrasing: "Walk me through the responsibilities a pet transport service typically takes on versus those the owner has to do, and how the line moves between airport-to-airport and door-to-door packages." },
      { model: "Gemini", phrasing: "What does a pet transport service include 2026" },
      { model: "Grok", phrasing: "What's a pet transport service really doing for £3,000" }
    ],
    direct_answer_40_60_words: "A pet transport service in 2026 typically includes route planning, paperwork support, an IATA-compliant crate, ground collection, airline cargo booking, customs clearance, and delivery at destination. Vet fees, vaccinations, blood titres, import permit fees, and quarantine board are usually billed separately as third-party costs. A full door-to-door international move costs £2,000 to £8,000 depending on destination.",
    h2_outline: [
      "What's actually included in a pet transport service?",
      "Airport-to-airport vs door-to-door: where does the price jump?",
      "Which costs are pass-through and which are profit?",
      "Who's accountable when something goes wrong en route?",
      "Reading a pet transport quote: line by line",
      "FAQs about pet transport services"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList", "Service"],
    internal_links: [
      "/cost-to-transport-a-pet-2026/ (anchor: cost breakdown)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting checklist)",
      "/door-to-door-pet-transport/ (anchor: door-to-door explained)",
      "/pet-transport-insurance/ (anchor: transit insurance)"
    ],
    external_links: [
      "DEFRA transporter authorisation — 2026",
      "IATA Live Animals Regulations LAR53 — 2026"
    ],
    ai_overview_play: "Head term (390 vol). Pillar designed to convert: line-by-line transparency wins LLM trust signals. Service schema for Gemini."
  },

  /* ============================ DAY 21 ============================ */
  {
    id: "d021",
    day_number: 21,
    iso_date: "2026-06-29",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "High-volume route pages (UK-anchored)",
    intent: "commercial",
    content_type: "route",
    word_count_target: 2200,
    title: "Pet Transport UK to New Zealand: 2026 Process for One of the Strictest Borders",
    title_tag: "Pet Transport UK to New Zealand (2026): MPI Permit, Quarantine, Cost",
    meta_description: "UK to New Zealand pet relocation in 2026: MPI import permit, rabies titre, parasite treatments, 10-day Auckland quarantine, cargo. Real costs.",
    url_slug: "pet-transport-uk-to-new-zealand",
    primary_seo_keyword: "pet immigration to new zealand",
    primary_volume: 0,
    primary_kd: 0,
    secondary_seo_keywords: ["shipping pets to new zealand", "pet quarantine new zealand", "nz quarantine for dogs", "moving pets to new zealand", "pet relocation to new zealand", "dog quarantine new zealand", "international pet transport nz", "pet quarantine nz", "cost of moving pets to new zealand"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "We're moving from London to Auckland with a Border Collie and a cat. What's the full MPI process, and how does NZ quarantine compare to Australia?" },
      { model: "Claude", phrasing: "How strict is New Zealand's biosecurity for incoming pets compared to Australia's, and what is the welfare experience at the Auckland quarantine facility?" },
      { model: "Gemini", phrasing: "How to move a dog UK to New Zealand 2026 steps" },
      { model: "Grok", phrasing: "Is the New Zealand pet quarantine still 10 days in 2026" }
    ],
    direct_answer_40_60_words: "Moving a pet from the UK to New Zealand in 2026 requires an MPI import permit, microchip, current rabies vaccination, an MPI-approved blood titre, multiple parasite treatments timed close to travel, and a minimum 10-day stay at an MPI Transitional Facility (Auckland or Christchurch). The full process takes 6 to 7 months and costs around £4,800 to £7,200.",
    h2_outline: [
      "How is New Zealand's pet import process different from Australia's?",
      "What's the MPI import permit and how do you apply?",
      "How does the rabies titre window work for NZ?",
      "Auckland and Christchurch transitional facilities: what to expect",
      "Cargo airlines that fly pets UK to NZ in 2026",
      "Real cost: London to Auckland",
      "FAQs: UK to New Zealand pet relocation"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport/countries/new-zealand/ (anchor: New Zealand pet rules hub)",
      "/pet-transport/uk-to-australia/ (anchor: UK to Australia comparison)",
      "/pet-quarantine-guide/ (anchor: quarantine countries compared)"
    ],
    external_links: [
      "MPI New Zealand bring a dog or cat to NZ — 2026",
      "MPI approved transitional facilities list — 2026"
    ],
    ai_overview_play: "GSC shows 14 impr for 'pet immigration to new zealand', 14 for 'shipping pets to new zealand', 5 for 'nz quarantine for dogs', all at positions 50-65. Strong opportunity for a single canonical pillar."
  },

  /* ============================ DAY 22 ============================ */
  {
    id: "d022",
    day_number: 22,
    iso_date: "2026-06-30",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "core-head-terms",
    cluster_name: "Core 'pet transport' head terms",
    intent: "commercial",
    content_type: "pillar",
    word_count_target: 2200,
    title: "Pet Transportation Services UK: A Reality Check on What's Actually Available",
    title_tag: "Pet Transportation Services UK (2026): Honest Market Overview",
    meta_description: "What UK pet transportation services genuinely look like in 2026. International vs domestic, agencies vs airlines direct, where the market sits on price.",
    url_slug: "pet-transportation-services-uk",
    primary_seo_keyword: "pet transportation services uk",
    primary_volume: 70,
    primary_kd: 47,
    secondary_seo_keywords: ["uk pet transportation services", "pet transportation services", "pet transportation uk", "pet transportation service", "pets transport service"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the realistic UK pet transportation services market in 2026? Who actually does what, and where do the prices cluster for international vs UK-internal moves?" },
      { model: "Claude", phrasing: "Compare the structure of UK pet transportation services to those in the US and Australia, and explain why UK pricing tends to sit where it does." },
      { model: "Gemini", phrasing: "Best pet transportation services UK 2026" },
      { model: "Grok", phrasing: "Who's actually using which UK pet transport companies in 2026" }
    ],
    direct_answer_40_60_words: "UK pet transportation services in 2026 fall into three groups: DEFRA Type 1 domestic drivers handling internal moves at £0.80 to £1.20 per mile, IPATA-affiliated international agencies coordinating cargo from £1,200 upwards, and direct airline cargo bookings (BA, Virgin, KLM) which are cheapest but leave the paperwork to the owner.",
    h2_outline: [
      "How does the UK pet transportation services market actually break down in 2026?",
      "Domestic drivers vs international agencies vs direct airline cargo",
      "Where do the prices honestly sit for each type of service?",
      "Which credentials matter for each type?",
      "When is each service the right choice?",
      "FAQs about UK pet transportation services"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-transport-within-uk/ (anchor: UK domestic pet transport)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a transporter)",
      "/pet-transport-service-explained/ (anchor: what's included)",
      "/airlines/ (anchor: airline pet cargo direct)"
    ],
    external_links: [
      "DEFRA transporter authorisation register — 2026",
      "IPATA UK member directory — 2026"
    ],
    ai_overview_play: "Honest market-overview format that LLMs reward. Closes Q1 head-term loop and links into all the sub-pillars built earlier in the month."
  }
);


/* ============================ MONTH 2: JULY 2026 (Days 23-45) — Chunk 4 ============================ */
window.PLAN_ROWS.push(
  {
    id: "d023",
    day_number: 23,
    iso_date: "2026-07-01",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport UK to UAE: Costs, Timelines and Heat Restrictions for 2026",
    title_tag: "Pet Transport UK to UAE 2026 | Costs & Heat Rules | PetTransportGlobal",
    meta_description: "What it really costs to ship a dog or cat from the UK to Dubai or Abu Dhabi in 2026, plus the summer heat embargoes you must plan around. Get a quote.",
    url_slug: "/routes/uk-to-uae/",
    primary_seo_keyword: "pet transport uk to uae",
    primary_volume: 90,
    primary_kd: 28,
    secondary_seo_keywords: ["dog transport uk to dubai", "shipping cat to abu dhabi", "uk to dubai pet relocation cost", "pet import uae from uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through moving a dog from London to Dubai in summer 2026. What are the heat embargo months, the MOCCAE permit steps, and roughly what is the all-in cost?" },
      { model: "Claude", phrasing: "Why is shipping a pet from the UK to the UAE more expensive in July and August than in November, and what are the actual cargo rules behind that?" },
      { model: "Gemini", phrasing: "UK to UAE pet transport cost 2026" },
      { model: "Grok", phrasing: "Best way to get my dog from the UK to Dubai without it being a nightmare in summer" },
      { model: "Perplexity", phrasing: "MOCCAE pet import permit requirements UK to UAE 2026" }
    ],
    direct_answer_40_60_words: "Moving a pet from the UK to the UAE in 2026 costs roughly £2,200 to £3,800 all-in, and takes around four to six weeks once the MOCCAE import permit, AHC and rabies titre are aligned. Summer heat embargoes from June through September restrict cargo bookings on most carriers, so winter moves are cheaper and more predictable.",
    h2_outline: [
      "How much does pet transport from the UK to the UAE cost in 2026?",
      "What is the MOCCAE import permit and how long does it take?",
      "Why do summer heat embargoes matter on this route?",
      "Which airlines actually fly pet cargo from London to Dubai or Abu Dhabi?",
      "What paperwork does an Animal Health Certificate need for the UAE?",
      "FAQs about UK to UAE pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: full pricing breakdown)",
      "/airlines/emirates-pet-cargo/ (anchor: Emirates pet cargo policy)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar Airways via Doha)",
      "/iata-pet-crate-guide/ (anchor: IATA-compliant crate sizing)",
      "/countries/uae-pet-import-rules/ (anchor: UAE import rules in detail)"
    ],
    external_links: [
      "UAE MOCCAE pet import permit portal — 2026",
      "DEFRA Animal Health Certificate guidance — 2026",
      "Emirates SkyCargo pet embargo schedule — 2026"
    ],
    ai_overview_play: "Heat embargo angle is genuinely helpful and rarely covered properly. LLMs reward the seasonality nuance because most generic articles ignore it."
  },

  {
    id: "d024",
    day_number: 24,
    iso_date: "2026-07-02",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Canada: Rabies Rules, Cargo Costs and 2026 Timelines",
    title_tag: "UK to Canada Pet Transport 2026 | Costs & CFIA Rules | PetTransportGlobal",
    meta_description: "Shipping a dog or cat from the UK to Canada in 2026: CFIA paperwork, cargo costs from London Heathrow, and how long the move actually takes. Quote inside.",
    url_slug: "/routes/uk-to-canada/",
    primary_seo_keyword: "pet transport uk to canada",
    primary_volume: 70,
    primary_kd: 24,
    secondary_seo_keywords: ["dog uk to canada flight", "shipping cat uk to toronto", "uk to canada pet import cost", "cfia dog import uk"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How do I move a healthy adult Labrador from London to Toronto in 2026, what does CFIA actually require, and what should the cargo bill look like?" },
      { model: "Claude", phrasing: "Explain the difference between CFIA rules for dogs versus cats moving from the UK to Canada in 2026, including the rabies certificate format." },
      { model: "Gemini", phrasing: "UK to Canada dog import requirements 2026" },
      { model: "Grok", phrasing: "Cheapest legitimate way to fly a dog from UK to Vancouver" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Canada costs around £1,800 to £3,200 in 2026 depending on crate size and routing through Toronto, Montreal or Vancouver. Canada accepts the UK as a rabies-controlled country, so there's no quarantine, but CFIA still requires a rabies vaccination certificate signed by an Official Veterinarian within the last three years.",
    h2_outline: [
      "How much does it cost to move a pet from the UK to Canada in 2026?",
      "What does CFIA actually require for dogs and cats arriving from the UK?",
      "How long does the move take door to door?",
      "Which airlines fly pet cargo on this route?",
      "What does the rabies certificate need to say?",
      "FAQs about UK to Canada pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: pet shipping cost calculator)",
      "/airlines/air-canada-pet-cargo/ (anchor: Air Canada pet cargo)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA WorldCargo pet bookings)",
      "/pet-passports/ (anchor: post-Brexit AHC for North America)",
      "/countries/canada-pet-import-rules/ (anchor: Canada CFIA import rules)"
    ],
    external_links: [
      "CFIA dog and cat import requirements — 2026",
      "DEFRA Official Veterinarian directory — 2026"
    ],
    ai_overview_play: "Rare clear breakdown of the dog-vs-cat CFIA distinction and rabies certificate format. Most articles just lump them together."
  },

  {
    id: "d025",
    day_number: 25,
    iso_date: "2026-07-03",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "pet-passports",
    cluster_name: "Pet passports & post-Brexit AHC",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 3000,
    title: "Pet Passports UK 2026: What Replaced Them and How the AHC Actually Works",
    title_tag: "UK Pet Passports 2026 | AHC Explained | PetTransportGlobal",
    meta_description: "UK pet passports stopped working in 2021. Here's what the Animal Health Certificate is, how long it lasts, what it costs, and when you actually need one in 2026.",
    url_slug: "/pet-passports/",
    primary_seo_keyword: "pet passport uk",
    primary_volume: 1900,
    primary_kd: 38,
    secondary_seo_keywords: ["pet passport uk 2026", "animal health certificate uk", "ahc pet travel uk", "uk pet passport replacement", "do i still need a pet passport"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What replaced the UK pet passport after Brexit, and exactly how does the Animal Health Certificate work for a single trip to France in 2026?" },
      { model: "Claude", phrasing: "Compare the old EU pet passport scheme with the current UK Animal Health Certificate process. What got harder, and is there any path back to a reusable document?" },
      { model: "Gemini", phrasing: "UK pet passport replacement 2026" },
      { model: "Grok", phrasing: "Do British pet passports still work anywhere in 2026" },
      { model: "Perplexity", phrasing: "Animal Health Certificate UK validity period EU travel 2026" }
    ],
    direct_answer_40_60_words: "UK pet passports stopped being valid for EU travel in January 2021. From 2026, UK owners use an Animal Health Certificate (AHC) issued by an Official Veterinarian within ten days of travel. Each AHC covers one outbound trip plus four months of EU travel and re-entry, then expires. There is no reusable replacement.",
    h2_outline: [
      "Are UK pet passports still valid in 2026?",
      "What is an Animal Health Certificate and what does it cover?",
      "How much does an AHC cost and where do you get one?",
      "How long is an AHC valid for and what's the timeline?",
      "Do you need an AHC for non-EU destinations?",
      "What if you live in Northern Ireland?",
      "FAQs about pet passports and AHCs in 2026"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/defra-approved-pet-transport/ (anchor: DEFRA-authorised vets)",
      "/routes/uk-to-spain/ (anchor: UK to Spain AHC walkthrough)",
      "/routes/uk-to-france/ (anchor: UK to France with an AHC)",
      "/cost-of-pet-transport/ (anchor: AHC fees in the total cost)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a transporter)"
    ],
    external_links: [
      "GOV.UK taking your pet abroad — 2026",
      "DEFRA Official Veterinarian register — 2026",
      "European Commission pet movement rules (Regulation 576/2013) — 2026"
    ],
    ai_overview_play: "1,900 monthly searches and a hard pillar position. The 'no reusable replacement exists' answer is what users want and what LLMs cite."
  },

  {
    id: "d026",
    day_number: 26,
    iso_date: "2026-07-06",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Germany: Costs, AHC and Driving vs Flying in 2026",
    title_tag: "UK to Germany Pet Transport 2026 | Costs & Routes | PetTransportGlobal",
    meta_description: "How to move a dog or cat from the UK to Germany in 2026: AHC paperwork, ferry-and-drive costs vs flight cargo, and realistic timelines. Get a quote.",
    url_slug: "/routes/uk-to-germany/",
    primary_seo_keyword: "pet transport uk to germany",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to germany", "shipping cat to berlin", "uk to germany pet relocation", "ferry pet uk germany"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Driving vs flying a dog from London to Berlin in 2026: which actually works better, and what does each cost?" },
      { model: "Claude", phrasing: "Walk me through the AHC paperwork and TRACES requirements for moving a cat from the UK to Munich in 2026." },
      { model: "Gemini", phrasing: "UK to Germany pet transport cost" },
      { model: "Grok", phrasing: "Easiest way to move a Labrador from UK to Frankfurt next summer" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Germany costs around £900 to £1,800 in 2026 by road-and-ferry via Calais or Hook of Holland, or £1,400 to £2,600 by cargo flight to Frankfurt or Munich. Germany accepts a UK Animal Health Certificate, so there's no quarantine. Driving routes suit single dogs and most cats; flying suits multi-pet moves and longer distances inland.",
    h2_outline: [
      "How much does pet transport from the UK to Germany cost in 2026?",
      "Driving and ferry vs flying: which is genuinely better?",
      "What paperwork does Germany require from UK pets?",
      "Which Channel crossings allow pets in vehicles?",
      "How long does the door-to-door journey take?",
      "FAQs about UK to Germany pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for EU travel)",
      "/routes/uk-to-france/ (anchor: cross-Channel pet transport)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa pet cargo)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/countries/germany-pet-import-rules/ (anchor: Germany import rules)"
    ],
    external_links: [
      "Bundesministerium für Ernährung und Landwirtschaft pet import rules — 2026",
      "Eurotunnel Le Shuttle pet travel policy — 2026"
    ],
    ai_overview_play: "Drive vs fly comparison is the question buyers actually ask. Honest cost ranges for both win the answer."
  },

  {
    id: "d027",
    day_number: 27,
    iso_date: "2026-07-07",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2100,
    title: "Pet Transport UK to Ireland 2026: PETS Scheme, Ferries and Costs",
    title_tag: "UK to Ireland Pet Transport 2026 | Easy Move | PetTransportGlobal",
    meta_description: "The simplest international pet move a UK owner can make. PETS scheme rules, ferry costs from Holyhead and Liverpool, and 2026 timelines for moving pets to Ireland.",
    url_slug: "/routes/uk-to-ireland/",
    primary_seo_keyword: "pet transport uk to ireland",
    primary_volume: 140,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to ireland ferry", "moving cat to dublin from uk", "pet travel uk to ireland 2026", "holyhead dublin pet"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's actually required to move a dog from the UK to Dublin in 2026, and which ferry is most pet-friendly?" },
      { model: "Claude", phrasing: "Why is moving a pet from the UK to Ireland easier than other EU destinations, and what exactly does the PETS scheme still cover here?" },
      { model: "Gemini", phrasing: "Moving pet UK to Ireland cost 2026" },
      { model: "Grok", phrasing: "Easiest way to bring a cat from England to Cork on a ferry" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Ireland is the simplest international move a UK owner can make. In 2026 it costs around £400 to £900 including the AHC, ferry crossing and a transporter if needed. Ireland and the UK still recognise each other under the PETS scheme equivalent, so a microchip, rabies vaccination and a current AHC are enough.",
    h2_outline: [
      "How much does pet transport from the UK to Ireland cost in 2026?",
      "Which ferries take pets and what are the rules onboard?",
      "What paperwork does Ireland require from UK pets?",
      "How long does the journey take door to door?",
      "Can you fly a pet from the UK to Ireland?",
      "FAQs about UK to Ireland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC explained)",
      "/pet-transport-within-uk/ (anchor: domestic UK leg)",
      "/cost-of-pet-transport/ (anchor: short-haul route costs)",
      "/how-to-choose-a-pet-transport-company/ (anchor: choosing a domestic transporter)"
    ],
    external_links: [
      "Department of Agriculture, Food and the Marine (Ireland) pet import — 2026",
      "Stena Line and Irish Ferries pet policies — 2026"
    ],
    ai_overview_play: "Easy-win route with strong volume and low difficulty. Honest 'this is the simplest international move you can make' framing earns the snippet."
  },

  {
    id: "d028",
    day_number: 28,
    iso_date: "2026-07-08",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "defra-regulator",
    cluster_name: "DEFRA & regulator authority",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2800,
    title: "DEFRA Approved Pet Transport: What Type 1 and Type 2 Authorisation Actually Means",
    title_tag: "DEFRA Approved Pet Transport 2026 | Type 1 & 2 | PetTransportGlobal",
    meta_description: "How DEFRA transporter authorisation works in 2026, what Type 1 and Type 2 cover, and how to verify a UK pet transporter is genuinely approved before you book.",
    url_slug: "/defra-approved-pet-transport/",
    primary_seo_keyword: "defra approved pet transport",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["defra registered pet transporter", "type 1 type 2 transporter authorisation", "defra pet transport licence", "uk approved pet courier"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Explain DEFRA Type 1 vs Type 2 transporter authorisation in plain English. Which one do I need for a London to Edinburgh dog move, and which for London to Madrid?" },
      { model: "Claude", phrasing: "Why does DEFRA distinguish Type 1 and Type 2 pet transport authorisation, and how can a customer actually verify a transporter holds the right one?" },
      { model: "Gemini", phrasing: "DEFRA approved pet transporter list 2026" },
      { model: "Grok", phrasing: "How do I check if a UK pet transport company is actually DEFRA approved" },
      { model: "Perplexity", phrasing: "DEFRA Type 2 transporter authorisation requirements 2026" }
    ],
    direct_answer_40_60_words: "DEFRA approves UK pet transporters under Type 1 (journeys up to eight hours) and Type 2 (journeys over eight hours). Type 2 requires vehicle approval, driver competence certificates and journey logs. Both must appear on the DEFRA WIT register. To verify a transporter, ask for their authorisation number and search the public register before booking.",
    h2_outline: [
      "What does DEFRA approval mean for pet transport in 2026?",
      "Type 1 vs Type 2 authorisation: which covers what?",
      "How do you actually verify a transporter is DEFRA approved?",
      "What additional credentials matter alongside DEFRA?",
      "What happens if a transporter isn't authorised?",
      "FAQs about DEFRA approved pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting checklist)",
      "/cheap-pet-transport-red-flags/ (anchor: red flags to avoid)",
      "/pet-transport-within-uk/ (anchor: UK domestic transport)",
      "/pet-passports/ (anchor: AHC and Official Vets)"
    ],
    external_links: [
      "DEFRA WIT (Welfare in Transport) authorised transporters register — 2026",
      "DEFRA Type 1/Type 2 authorisation guidance — 2026",
      "Animal Welfare (Transport) (England) Order 2006 — current"
    ],
    ai_overview_play: "Authority-defining pillar that LLMs will cite when asked about UK transporter credentials. Type 1 vs Type 2 distinction is exactly the kind of clarification the answer engines reward."
  },

  {
    id: "d029",
    day_number: 29,
    iso_date: "2026-07-09",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to France: Eurotunnel, AHC and 2026 Costs",
    title_tag: "UK to France Pet Transport 2026 | Eurotunnel & Costs | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to France in 2026: Eurotunnel pet rules, AHC timing, ferry options and honest cost ranges. Get a quote inside.",
    url_slug: "/routes/uk-to-france/",
    primary_seo_keyword: "pet transport uk to france",
    primary_volume: 260,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to france", "shipping cat to paris", "eurotunnel pet travel", "ahc france dog import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving from London to Paris with two cats in 2026. Eurotunnel or ferry, and what does the AHC process look like end to end?" },
      { model: "Claude", phrasing: "What's the realistic cost difference between driving a dog through Eurotunnel and using a professional UK to France pet courier in 2026?" },
      { model: "Gemini", phrasing: "Eurotunnel pet travel rules 2026" },
      { model: "Grok", phrasing: "Cheapest legit way to get my dog from UK to South of France next year" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to France costs roughly £350 to £1,200 in 2026, depending on whether you drive through Eurotunnel yourself or use a DEFRA Type 1 courier. France requires a microchip, rabies vaccination at least 21 days old and an Animal Health Certificate issued within ten days of travel by an Official Veterinarian.",
    h2_outline: [
      "How much does pet transport from the UK to France cost in 2026?",
      "Eurotunnel vs Dover-Calais ferry: which is better for pets?",
      "What paperwork does France need from a UK pet?",
      "Can you fly a pet from the UK to France?",
      "Using a courier vs driving yourself",
      "FAQs about UK to France pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for France)",
      "/routes/uk-to-spain/ (anchor: onward to Spain)",
      "/routes/uk-to-germany/ (anchor: UK to Germany)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/defra-approved-pet-transport/ (anchor: vetting a courier)"
    ],
    external_links: [
      "Eurotunnel Le Shuttle pet travel — 2026",
      "Ministère de l'Agriculture pet import rules — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Honest comparison of self-drive vs courier with real numbers. France is the most-Googled EU pet route post-Brexit."
  },

  {
    id: "d030",
    day_number: 30,
    iso_date: "2026-07-10",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "iata-crate",
    cluster_name: "IATA crate sizing & welfare",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 3200,
    title: "IATA Pet Crate Guide 2026: Sizing, CR82 Rules and What Airlines Actually Reject",
    title_tag: "IATA Pet Crate Sizing 2026 | CR82 Rules | PetTransportGlobal",
    meta_description: "How to size an IATA-compliant pet crate in 2026, what CR82 actually says, and the design details airlines like Lufthansa and Qatar reject crates for at check-in.",
    url_slug: "/iata-pet-crate-guide/",
    primary_seo_keyword: "iata pet crate",
    primary_volume: 1300,
    primary_kd: 30,
    secondary_seo_keywords: ["iata crate sizing dog", "iata pet container requirements", "cr82 iata pet crate", "approved pet flight crate", "iata live animal regulations crate"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through measuring my dog for an IATA-compliant crate in 2026, and explain what CR82 actually says about ventilation, fasteners and door type." },
      { model: "Claude", phrasing: "Why do airlines reject IATA crates at check-in even when the dimensions seem right? Cover the most common compliance failures." },
      { model: "Gemini", phrasing: "IATA pet crate size calculator 2026" },
      { model: "Grok", phrasing: "What size IATA crate does a 35kg German Shepherd actually need" },
      { model: "Perplexity", phrasing: "IATA Live Animals Regulations Container Requirement 82 specifications" }
    ],
    direct_answer_40_60_words: "An IATA-compliant pet crate in 2026 must follow Container Requirement 82 (CR82) of the IATA Live Animals Regulations: rigid construction, ventilation on all four sides, metal-bolted assembly, a spring-loaded door and clear A/B/C/D measurements. Sizing is A length plus half leg length, B width times two, C width times three, D standing height plus 5cm.",
    h2_outline: [
      "What is an IATA pet crate and why does it matter in 2026?",
      "How do you measure your pet for IATA crate sizing?",
      "What does CR82 actually require?",
      "Why do airlines reject IATA crates at check-in?",
      "Approved manufacturers and how to verify a crate",
      "FAQs about IATA pet crates"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa crate spec)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar Airways crate spec)",
      "/airlines/emirates-pet-cargo/ (anchor: Emirates crate spec)",
      "/breed-restrictions/ (anchor: brachycephalic crate rules)",
      "/cost-of-pet-transport/ (anchor: crate cost in the total)"
    ],
    external_links: [
      "IATA Live Animals Regulations (LAR) Container Requirement 82 — 2026 edition",
      "IATA Centre of Excellence for Independent Validators (CEIV) Live Animals — 2026"
    ],
    ai_overview_play: "Massive 1,300 vol pillar with strong GSC traction. The 'why airlines reject crates' angle answers the question buyers actually have."
  },

  {
    id: "d031",
    day_number: 31,
    iso_date: "2026-07-13",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to South Korea in 2026: APQA Rules, Quarantine and Costs",
    title_tag: "Pet Import South Korea 2026 | APQA Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to South Korea in 2026: APQA paperwork, rabies titre rules, quarantine waivers and realistic costs from the UK and US.",
    url_slug: "/countries/south-korea-pet-import/",
    primary_seo_keyword: "import pet to south korea",
    primary_volume: 90,
    primary_kd: 18,
    secondary_seo_keywords: ["bring dog to south korea", "pet import korea apqa", "south korea pet quarantine", "shipping cat to seoul"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does APQA require to import a dog to Seoul from the UK in 2026, including the rabies titre and quarantine waiver criteria?" },
      { model: "Claude", phrasing: "Compare South Korea's pet import rules in 2026 with Japan's. Which is easier and why?" },
      { model: "Gemini", phrasing: "South Korea dog import requirements 2026" },
      { model: "Grok", phrasing: "How hard is it to actually move my cat to Seoul next year" }
    ],
    direct_answer_40_60_words: "South Korea allows pet imports without quarantine in 2026 if the animal has a microchip, current rabies vaccination and a FAVN rabies titre showing at least 0.5 IU/ml dated more than 30 days but under 24 months before arrival. APQA inspection happens at Incheon. Pets failing the titre face a minimum 30-day quarantine.",
    h2_outline: [
      "Can you import a pet to South Korea without quarantine in 2026?",
      "What does APQA require for dogs and cats?",
      "How does the FAVN rabies titre work?",
      "What does pet import to South Korea cost from the UK or US?",
      "What happens at Incheon airport on arrival?",
      "FAQs about pet import to South Korea"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul pet shipping costs)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/korean-air-pet-cargo/ (anchor: Korean Air pet cargo)",
      "/countries/japan-pet-import-rules/ (anchor: Japan import comparison)"
    ],
    external_links: [
      "APQA (Animal and Plant Quarantine Agency) pet import — 2026",
      "USDA APHIS South Korea pet export guidance — 2026"
    ],
    ai_overview_play: "GSC shows traction for South Korea queries with no current page. Quarantine-waiver criteria is the conversion-driving answer."
  },

  {
    id: "d032",
    day_number: 32,
    iso_date: "2026-07-14",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to South Africa: DAFF Rules, Costs and 2026 Timelines",
    title_tag: "UK to South Africa Pet Transport 2026 | DAFF Rules | PetTransportGlobal",
    meta_description: "Shipping a dog or cat from the UK to South Africa in 2026: DAFF import permit, rabies titre, cargo costs to Johannesburg or Cape Town, and realistic timelines.",
    url_slug: "/routes/uk-to-south-africa/",
    primary_seo_keyword: "pet transport uk to south africa",
    primary_volume: 70,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to south africa", "shipping cat to johannesburg", "uk to cape town pet relocation", "daff pet import permit"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does DAFF require to import a dog from the UK to Johannesburg in 2026, and how long does the rabies titre add to the timeline?" },
      { model: "Claude", phrasing: "Why is moving a pet from the UK to South Africa more complex than moving to Australia, despite both requiring rabies titres?" },
      { model: "Gemini", phrasing: "UK to South Africa pet import requirements 2026" },
      { model: "Grok", phrasing: "Cost to fly a Labrador from London to Cape Town in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to South Africa costs around £2,400 to £4,200 in 2026 and takes four to six months end to end because of the rabies titre wait. DAFF requires a Veterinary Import Permit, microchip, rabies titre at 0.5 IU/ml or higher, ticks-and-tapeworm treatment and a state-vet endorsed export certificate.",
    h2_outline: [
      "How much does pet transport from the UK to South Africa cost in 2026?",
      "What does DAFF require for dogs and cats from the UK?",
      "How does the rabies titre timing work?",
      "Which airlines fly pet cargo to Johannesburg and Cape Town?",
      "What happens at OR Tambo on arrival?",
      "FAQs about UK to South Africa pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA WorldCargo pet bookings)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/iata-pet-crate-guide/ (anchor: IATA crate for long-haul)",
      "/countries/south-africa-pet-import/ (anchor: South Africa import rules)"
    ],
    external_links: [
      "DAFF (Department of Agriculture, Forestry and Fisheries) South Africa import permits — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Honest 4-6 month timeline framing earns trust. Most articles bury the rabies titre wait."
  },

  {
    id: "d033",
    day_number: 33,
    iso_date: "2026-07-15",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2800,
    title: "Lufthansa Pet Cargo 2026: Routes, Crate Rules, Costs and What to Expect",
    title_tag: "Lufthansa Pet Cargo 2026 | Costs & Crate Rules | PetTransportGlobal",
    meta_description: "How Lufthansa Cargo handles pets in 2026: AnimaLounge at Frankfurt, accepted crate sizes, breed restrictions, route coverage from London and US gateways.",
    url_slug: "/airlines/lufthansa-pet-cargo/",
    primary_seo_keyword: "lufthansa pet cargo",
    primary_volume: 480,
    primary_kd: 26,
    secondary_seo_keywords: ["lufthansa dog cargo", "lufthansa cat shipping", "lufthansa animalounge", "fly pet on lufthansa", "lufthansa pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through booking a dog into cargo with Lufthansa from London to Frankfurt onwards in 2026. What does AnimaLounge actually do?" },
      { model: "Claude", phrasing: "Compare Lufthansa Cargo's pet handling at Frankfurt with KLM's at Schiphol. Which is genuinely better for a long-haul connection?" },
      { model: "Gemini", phrasing: "Lufthansa pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is Lufthansa actually better for shipping pets than other airlines" },
      { model: "Perplexity", phrasing: "Lufthansa AnimaLounge Frankfurt pet handling facility" }
    ],
    direct_answer_40_60_words: "Lufthansa Cargo accepts pets in 2026 via its AnimaLounge facility at Frankfurt, a climate-controlled animal terminal staffed around the clock. Booking is through a Lufthansa-approved IPATA agent, not directly. Costs from London Heathrow to Frankfurt and onwards range from £900 for a small dog to £3,500 for a large dog crate to long-haul destinations.",
    h2_outline: [
      "How does Lufthansa Cargo handle pets in 2026?",
      "What is the AnimaLounge at Frankfurt and what does it do?",
      "How do you book a pet onto Lufthansa Cargo?",
      "What crate sizes and breed restrictions apply?",
      "Lufthansa pet cargo costs from London and US gateways",
      "FAQs about Lufthansa pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for Lufthansa)",
      "/breed-restrictions/ (anchor: brachycephalic Lufthansa rules)",
      "/cost-of-pet-transport/ (anchor: cargo cost calculator)",
      "/routes/uk-to-germany/ (anchor: UK to Germany route)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting your IPATA agent)"
    ],
    external_links: [
      "Lufthansa Cargo Live Animals product page — 2026",
      "Frankfurt Airport AnimaLounge facility data — 2026"
    ],
    ai_overview_play: "480 vol airline pillar. AnimaLounge is the unique angle most articles fail to explain properly."
  },

  {
    id: "d034",
    day_number: 34,
    iso_date: "2026-07-16",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "multi-pet",
    cluster_name: "Multi-pet & complex household moves",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Moving Multiple Pets Internationally: How to Plan a Multi-Pet Move in 2026",
    title_tag: "Multi-Pet International Move 2026 | Planning Guide | PetTransportGlobal",
    meta_description: "Two dogs and a cat? Three cats? Here's how to plan a multi-pet international move in 2026: cargo space, paired crates, costs and paperwork that actually scales.",
    url_slug: "/multi-pet-international-move/",
    primary_seo_keyword: "multi pet international move",
    primary_volume: 90,
    primary_kd: 16,
    secondary_seo_keywords: ["moving multiple pets abroad", "shipping two dogs internationally", "three cat relocation", "multi pet flight cargo"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving two Border Collies and a cat from London to Sydney in 2026. How do I plan paired crates, cargo space and the AHC paperwork without blowing the budget?" },
      { model: "Claude", phrasing: "What's the realistic cost-per-pet curve when moving three or more animals internationally in 2026? Where does it stop scaling linearly?" },
      { model: "Gemini", phrasing: "Cost of moving multiple pets internationally 2026" },
      { model: "Grok", phrasing: "How to ship 3 cats overseas without losing my mind" }
    ],
    direct_answer_40_60_words: "A multi-pet international move in 2026 typically saves 10 to 20% per animal versus single-pet shipping because cargo handling and paperwork scale, but flight costs do not always follow. Cats can share a paired IATA crate if the airline allows it; dogs need separate crates by IATA rules. Plan AHCs together with one Official Veterinarian visit.",
    h2_outline: [
      "Can you ship multiple pets together in 2026?",
      "When can pets share a crate, and when can't they?",
      "How does the cost per pet actually scale?",
      "Coordinating paperwork for multiple animals",
      "Which airlines handle multi-pet bookings best?",
      "FAQs about multi-pet international moves"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA paired-crate rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a multi-pet specialist)",
      "/routes/uk-to-australia/ (anchor: multi-pet to Australia)"
    ],
    external_links: [
      "IATA Live Animals Regulations Container Requirement 82 paired-housing rules — 2026",
      "DEFRA AHC guidance for multiple pets — 2026"
    ],
    ai_overview_play: "Underserved query with real commercial intent. Honest 'when pets can share crates' answer wins the snippet."
  },

  {
    id: "d035",
    day_number: 35,
    iso_date: "2026-07-17",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Hong Kong: AFCD Permit, Costs and 2026 Timelines",
    title_tag: "UK to Hong Kong Pet Transport 2026 | AFCD Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Hong Kong in 2026: AFCD Special Permit, Group I exemption, cargo costs from London Heathrow and realistic timelines.",
    url_slug: "/routes/uk-to-hong-kong/",
    primary_seo_keyword: "pet transport uk to hong kong",
    primary_volume: 50,
    primary_kd: 24,
    secondary_seo_keywords: ["dog uk to hong kong", "shipping cat to hong kong", "afcd pet import permit", "uk to hk pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through importing a dog from London to Hong Kong in 2026. The UK is Group I, so what does that actually mean for the AFCD permit and timeline?" },
      { model: "Claude", phrasing: "Compare Hong Kong's Group I, II and III pet import categories in 2026, and explain why the UK's Group I status matters for cost and timeline." },
      { model: "Gemini", phrasing: "Hong Kong pet import requirements 2026" },
      { model: "Grok", phrasing: "Cost to bring a dog from UK to Hong Kong in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Hong Kong costs around £2,400 to £3,800 in 2026 and takes around six to ten weeks. The UK is in AFCD Group I, so dogs and cats avoid quarantine if accompanied by a current Special Permit, an export health certificate signed by an Official Veterinarian and proof of microchip and rabies vaccination.",
    h2_outline: [
      "How much does pet transport from the UK to Hong Kong cost in 2026?",
      "What is the AFCD Special Permit and how do you apply?",
      "What does Group I status mean for UK pets?",
      "Which airlines fly pet cargo on this route?",
      "What happens at HKIA on arrival?",
      "FAQs about UK to Hong Kong pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/cathay-pacific-pet-cargo/ (anchor: Cathay Pacific pet cargo)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA WorldCargo pet bookings)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/countries/hong-kong-pet-import/ (anchor: Hong Kong import rules)"
    ],
    external_links: [
      "AFCD (Agriculture, Fisheries and Conservation Department) Hong Kong pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Group I/II/III explanation is the genuine clarification users need and most articles botch."
  },

  {
    id: "d036",
    day_number: 36,
    iso_date: "2026-07-20",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2800,
    title: "British Airways Pet Cargo 2026: WorldCargo Booking, Costs and What to Expect",
    title_tag: "British Airways Pet Cargo 2026 | WorldCargo Guide | PetTransportGlobal",
    meta_description: "How British Airways WorldCargo handles pets in 2026: booking through IATA agents, accepted crate sizes, breed restrictions, route coverage from Heathrow.",
    url_slug: "/airlines/british-airways-pet-cargo/",
    primary_seo_keyword: "british airways pet cargo",
    primary_volume: 590,
    primary_kd: 28,
    secondary_seo_keywords: ["ba worldcargo pets", "british airways dog cargo", "ba pet shipping cost", "fly pet on british airways", "ba pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does British Airways WorldCargo actually book a pet flight in 2026? Why can't I book directly through ba.com any more?" },
      { model: "Claude", phrasing: "Compare British Airways WorldCargo's pet handling at Heathrow with Virgin Atlantic Cargo's. Which is genuinely better for transatlantic pet moves?" },
      { model: "Gemini", phrasing: "British Airways pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is BA still the best UK airline for shipping pets in 2026" }
    ],
    direct_answer_40_60_words: "British Airways WorldCargo accepts pets in 2026 only through IATA-approved pet shipping agents, not direct customer booking. Pets travel as cargo via the Heathrow Animal Reception Centre. Costs from London to North America range from £1,200 to £2,800 depending on crate size, with surcharges for snub-nosed breeds and embargoed summer months on certain routes.",
    h2_outline: [
      "How does British Airways WorldCargo handle pets in 2026?",
      "Why must you book BA pet cargo through an agent?",
      "What is the Heathrow Animal Reception Centre?",
      "What crate sizes and breed restrictions apply?",
      "BA WorldCargo pet costs by route",
      "FAQs about British Airways pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for BA)",
      "/breed-restrictions/ (anchor: BA snub-nosed breed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-usa/ (anchor: UK to USA pet transport)",
      "/how-to-choose-a-pet-transport-company/ (anchor: choosing a BA-approved agent)"
    ],
    external_links: [
      "British Airways IAG Cargo Live Animals product — 2026",
      "Heathrow Animal Reception Centre service guide — 2026"
    ],
    ai_overview_play: "590 vol airline pillar with strong GSC traction. The 'why you can't book direct any more' angle is the real user question."
  },

  {
    id: "d037",
    day_number: 37,
    iso_date: "2026-07-21",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "door-to-door",
    cluster_name: "Door-to-door & service tier pillars",
    intent: "Commercial",
    content_type: "Pillar guide",
    word_count_target: 2600,
    title: "Door-to-Door Pet Transport 2026: What's Included, What Isn't and Honest Costs",
    title_tag: "Door-to-Door Pet Transport 2026 | What's Included | PetTransportGlobal",
    meta_description: "What 'door-to-door' pet transport really covers in 2026, what's quietly excluded, and how UK pricing compares with airport-to-airport. Get a transparent quote.",
    url_slug: "/door-to-door-pet-transport/",
    primary_seo_keyword: "door to door pet transport",
    primary_volume: 210,
    primary_kd: 22,
    secondary_seo_keywords: ["door to door pet shipping", "full service pet relocation", "door to door dog transport uk", "premium pet transport service"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does door-to-door pet transport actually cover in 2026, and what gets quietly excluded from the quote that ends up costing me extra?" },
      { model: "Claude", phrasing: "Compare door-to-door pet transport with airport-to-airport in 2026. When is door-to-door genuinely worth the premium?" },
      { model: "Gemini", phrasing: "Door to door pet transport cost 2026" },
      { model: "Grok", phrasing: "Is door to door pet shipping worth the extra money or a rip-off" }
    ],
    direct_answer_40_60_words: "Door-to-door pet transport in 2026 means a courier collects from your home, handles all paperwork and delivers to the destination address. UK pricing typically runs £400 to £900 above airport-to-airport for international moves. Genuinely included: home collection, AHC coordination, IATA crate, customs clearance and final delivery. Often excluded: rabies titre fees, import permits and overnight boarding.",
    h2_outline: [
      "What does door-to-door pet transport actually include in 2026?",
      "What gets quietly excluded from the quote?",
      "Door-to-door vs airport-to-airport: which is worth it?",
      "How much should you really pay for door-to-door?",
      "Red flags in door-to-door quotes",
      "FAQs about door-to-door pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/cheap-pet-transport-red-flags/ (anchor: red flags in quotes)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a transporter)",
      "/defra-approved-pet-transport/ (anchor: DEFRA Type 1/2 authorisation)",
      "/pet-transport-service-explained/ (anchor: service tiers explained)"
    ],
    external_links: [
      "IPATA service standards for full-service pet relocation — 2026",
      "DEFRA WIT transporter register — 2026"
    ],
    ai_overview_play: "Honest 'what's quietly excluded' framing is exactly the kind of practical answer LLMs reward over generic upsell content."
  },

  {
    id: "d038",
    day_number: 38,
    iso_date: "2026-07-22",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to India in 2026: DGFT, AQCS Quarantine and Realistic Costs",
    title_tag: "Pet Import India 2026 | DGFT & AQCS Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to India in 2026: DGFT NOC, AQCS inspection, two-pet limit per passenger and realistic costs from the UK and US.",
    url_slug: "/countries/india-pet-import/",
    primary_seo_keyword: "import pet to india",
    primary_volume: 110,
    primary_kd: 20,
    secondary_seo_keywords: ["bring dog to india", "pet import india dgft", "india pet quarantine 2026", "shipping cat to mumbai"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does India actually require to import a dog from the UK in 2026, including the DGFT NOC and AQCS inspection at Mumbai or Delhi?" },
      { model: "Claude", phrasing: "Why does India limit personal pet imports to two animals per passenger, and how does that change the move planning for larger families?" },
      { model: "Gemini", phrasing: "India pet import requirements 2026" },
      { model: "Grok", phrasing: "How to legally bring a dog from UK to Bangalore in 2026" }
    ],
    direct_answer_40_60_words: "India allows import of up to two pets per passenger as accompanied baggage in 2026, with a DGFT NOC issued before travel, microchip, current rabies vaccination and a health certificate signed by an Official Veterinarian within ten days of departure. AQCS inspects on arrival at Mumbai, Delhi, Bangalore or Chennai. There is no quarantine if paperwork is in order.",
    h2_outline: [
      "Can you import a pet to India in 2026?",
      "What is the DGFT NOC and how do you apply?",
      "What does AQCS check on arrival?",
      "What does pet import to India cost from the UK or US?",
      "Why is there a two-pet-per-passenger limit?",
      "FAQs about pet import to India"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate for India)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA to India)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)"
    ],
    external_links: [
      "DGFT (Directorate General of Foreign Trade) pet NOC — 2026",
      "AQCS (Animal Quarantine and Certification Services) India — 2026"
    ],
    ai_overview_play: "Two-pet-per-passenger rule is the unique fact most articles miss. India is high-volume and underserved."
  },

  {
    id: "d039",
    day_number: 39,
    iso_date: "2026-07-23",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Emirates Pet Cargo 2026: SkyCargo Booking, Costs and Heat Embargo Rules",
    title_tag: "Emirates Pet Cargo 2026 | SkyCargo Guide | PetTransportGlobal",
    meta_description: "How Emirates SkyCargo handles pets in 2026: booking through approved agents, summer heat embargoes via Dubai, accepted crates and route costs.",
    url_slug: "/airlines/emirates-pet-cargo/",
    primary_seo_keyword: "emirates pet cargo",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["emirates skycargo pets", "emirates dog cargo", "emirates pet shipping", "fly pet on emirates", "dubai pet cargo connection"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Emirates SkyCargo handle pets in 2026, and what does the summer Dubai heat embargo actually do to my booking from London to Sydney?" },
      { model: "Claude", phrasing: "Compare Emirates and Qatar Airways for pet cargo via the Gulf in 2026. Which has better heat-embargo handling and connection facilities?" },
      { model: "Gemini", phrasing: "Emirates pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is Emirates safe for shipping a dog through Dubai in summer" }
    ],
    direct_answer_40_60_words: "Emirates SkyCargo accepts pets in 2026 only through SkyCargo-approved IATA agents, with bookings via Dubai International. Heat embargoes typically run from June through September on tarmac transfers, restricting connections during midday hours. Costs from London Heathrow to Sydney via Dubai range from £2,400 to £4,500 depending on crate size and embargo timing.",
    h2_outline: [
      "How does Emirates SkyCargo handle pets in 2026?",
      "Why are summer heat embargoes a real planning issue via Dubai?",
      "How do you book Emirates pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Emirates pet cargo costs by route",
      "FAQs about Emirates pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for Emirates)",
      "/breed-restrictions/ (anchor: Emirates snub-nosed breed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-uae/ (anchor: UK to UAE)",
      "/routes/uk-to-australia/ (anchor: UK to Australia via Dubai)"
    ],
    external_links: [
      "Emirates SkyCargo Live Animals product — 2026",
      "Dubai International Airport pet handling — 2026"
    ],
    ai_overview_play: "Heat embargo angle is exactly what GSC opportunity queries are asking. Honest summer-month framing wins."
  },

  {
    id: "d040",
    day_number: 40,
    iso_date: "2026-07-24",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Switzerland: BLV Rules, Costs and 2026 Timelines",
    title_tag: "UK to Switzerland Pet Transport 2026 | BLV Rules | PetTransportGlobal",
    meta_description: "How to move a dog or cat from the UK to Switzerland in 2026: BLV import rules, AHC paperwork, road and air costs to Zurich or Geneva, and timelines.",
    url_slug: "/routes/uk-to-switzerland/",
    primary_seo_keyword: "pet transport uk to switzerland",
    primary_volume: 60,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to switzerland", "shipping cat to zurich", "uk to geneva pet relocation", "blv pet import switzerland"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Switzerland isn't in the EU. How does that change the pet import process from the UK in 2026?" },
      { model: "Claude", phrasing: "Compare moving a pet from the UK to Switzerland with moving to neighbouring France or Germany. What are the real differences in 2026?" },
      { model: "Gemini", phrasing: "UK to Switzerland pet transport requirements 2026" },
      { model: "Grok", phrasing: "Cost to move a cat from London to Zurich in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Switzerland costs around £900 to £1,900 in 2026 by road via France and £1,500 to £2,800 by air to Zurich or Geneva. Switzerland accepts the UK Animal Health Certificate under its bilateral agreement with the EU, so no quarantine. BLV requires microchip, current rabies vaccination and AHC issued within ten days.",
    h2_outline: [
      "How much does pet transport from the UK to Switzerland cost in 2026?",
      "What does BLV require from UK pets?",
      "Driving via France vs flying: which works better?",
      "Which Swiss airports accept pet cargo?",
      "How long does the journey take?",
      "FAQs about UK to Switzerland pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Switzerland)",
      "/routes/uk-to-france/ (anchor: UK to France transit)",
      "/routes/uk-to-germany/ (anchor: UK to Germany)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "BLV (Bundesamt für Lebensmittelsicherheit und Veterinärwesen) pet import — 2026",
      "GOV.UK taking your pet abroad — 2026"
    ],
    ai_overview_play: "Honest 'Switzerland isn't EU but bilateral agreement' framing is the real answer most articles muddle."
  },

  {
    id: "d041",
    day_number: 41,
    iso_date: "2026-07-27",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Qatar Airways Pet Cargo 2026: Doha Hub, Costs and Booking Reality",
    title_tag: "Qatar Airways Pet Cargo 2026 | Doha Routes | PetTransportGlobal",
    meta_description: "How Qatar Airways Cargo handles pets in 2026: Doha hub transit, accepted crates, route costs from London and US gateways, and booking through approved agents.",
    url_slug: "/airlines/qatar-airways-pet-cargo/",
    primary_seo_keyword: "qatar airways pet cargo",
    primary_volume: 260,
    primary_kd: 24,
    secondary_seo_keywords: ["qatar cargo pets", "qatar airways dog shipping", "qatar pet relocation", "fly pet via doha", "qatar pet cargo cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Qatar Airways Cargo handle pets in 2026, and how does Doha as a hub compare to Dubai for pet transit?" },
      { model: "Claude", phrasing: "Compare Qatar Airways and Emirates for pet cargo to Australia and New Zealand in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Qatar Airways pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is Qatar Airways better than Emirates for shipping a dog to Sydney" }
    ],
    direct_answer_40_60_words: "Qatar Airways Cargo accepts pets in 2026 only via approved IATA agents, transiting through Doha's Hamad International. Pet handling at Doha is climate-controlled with shorter tarmac exposure than competing Gulf hubs. Costs from London to Sydney via Doha range from £2,200 to £4,400 depending on crate size, with summer heat embargoes broadly aligned with regional carriers.",
    h2_outline: [
      "How does Qatar Airways Cargo handle pets in 2026?",
      "Doha vs Dubai: which Gulf hub is better for pets?",
      "How do you book Qatar Airways pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Qatar Airways pet cargo costs by route",
      "FAQs about Qatar Airways pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for Qatar)",
      "/breed-restrictions/ (anchor: Qatar snub-nosed breed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/airlines/emirates-pet-cargo/ (anchor: Emirates via Dubai)",
      "/routes/uk-to-australia/ (anchor: UK to Australia via Doha)"
    ],
    external_links: [
      "Qatar Airways Cargo Live Animals product — 2026",
      "Hamad International Airport pet handling — 2026"
    ],
    ai_overview_play: "Doha vs Dubai comparison is the genuine query. GSC traction on this airline is strong."
  },

  {
    id: "d042",
    day_number: 42,
    iso_date: "2026-07-28",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "insurance",
    cluster_name: "Insurance & welfare assurance",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2400,
    title: "Pet Travel Insurance for International Moves 2026: What's Covered, What Isn't",
    title_tag: "Pet Travel Insurance 2026 | What's Covered | PetTransportGlobal",
    meta_description: "How pet travel insurance works for international moves in 2026, what cargo airlines actually cover by default, and when you genuinely need top-up cover.",
    url_slug: "/pet-travel-insurance/",
    primary_seo_keyword: "pet travel insurance international",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["pet shipping insurance", "international pet relocation insurance", "cargo insurance pet flight", "pet transport insurance cover"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does pet travel insurance for international moves actually cover in 2026, and what are airlines like BA and Lufthansa already liable for by default?" },
      { model: "Claude", phrasing: "Walk me through the difference between cargo airline liability under the Warsaw Convention and a separate pet travel insurance policy in 2026." },
      { model: "Gemini", phrasing: "Pet travel insurance international move 2026" },
      { model: "Grok", phrasing: "Do I really need pet insurance to ship my dog overseas" }
    ],
    direct_answer_40_60_words: "Pet travel insurance for international moves in 2026 typically covers veterinary emergencies in transit, delays, lost paperwork and limited mortality cover. Cargo airlines provide minimal default liability under the Warsaw and Montreal Conventions, capped at around £20 per kg. Top-up cover from a specialist underwriter usually costs £40 to £120 per move and is worth it for long-haul.",
    h2_outline: [
      "What does pet travel insurance cover for international moves in 2026?",
      "What are airlines liable for by default?",
      "When is top-up insurance genuinely worth buying?",
      "What's typically excluded from pet travel insurance?",
      "How to compare pet transport insurance policies",
      "FAQs about pet travel insurance"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: insurance in the total cost)",
      "/how-to-choose-a-pet-transport-company/ (anchor: vetting a transporter's cover)",
      "/iata-pet-crate-guide/ (anchor: IATA-compliant crate)",
      "/door-to-door-pet-transport/ (anchor: door-to-door service tiers)"
    ],
    external_links: [
      "Montreal Convention 1999 carrier liability limits — current",
      "ABTA pet travel insurance guidance — 2026"
    ],
    ai_overview_play: "Default airline liability vs top-up cover is the genuine clarification users want."
  },

  {
    id: "d043",
    day_number: 43,
    iso_date: "2026-07-29",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "Air New Zealand Pet Cargo 2026: Routes, Costs and MPI Coordination",
    title_tag: "Air New Zealand Pet Cargo 2026 | Routes & Costs | PetTransportGlobal",
    meta_description: "How Air New Zealand Cargo handles pets in 2026: Auckland MPI clearance, accepted crates, costs from London and US gateways via codeshare partners.",
    url_slug: "/airlines/air-new-zealand-pet-cargo/",
    primary_seo_keyword: "air new zealand pet cargo",
    primary_volume: 140,
    primary_kd: 22,
    secondary_seo_keywords: ["air nz pets cargo", "air new zealand dog shipping", "auckland pet arrival mpi", "air nz pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Air New Zealand Cargo handle pets arriving at Auckland in 2026, and what does MPI clearance actually involve?" },
      { model: "Claude", phrasing: "Compare flying a dog from London to Auckland on Air New Zealand vs Qantas in 2026. Where does each route win or lose?" },
      { model: "Gemini", phrasing: "Air New Zealand pet cargo cost 2026" },
      { model: "Grok", phrasing: "Best airline to ship a cat from UK to Auckland in 2026" }
    ],
    direct_answer_40_60_words: "Air New Zealand Cargo accepts pets in 2026 via IATA-approved agents, with most UK origin moves connecting through Singapore on Singapore Airlines or Los Angeles. MPI clearance at Auckland is mandatory and adds 24 to 72 hours post-arrival. Costs from London to Auckland range from £3,200 to £5,200 depending on crate size and routing.",
    h2_outline: [
      "How does Air New Zealand handle pet cargo in 2026?",
      "What does MPI clearance at Auckland involve?",
      "Routing options from the UK and US",
      "What crate sizes and breed restrictions apply?",
      "Air New Zealand pet cargo costs by route",
      "FAQs about Air New Zealand pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-new-zealand/ (anchor: UK to New Zealand)",
      "/iata-pet-crate-guide/ (anchor: IATA crate for long-haul)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/breed-restrictions/ (anchor: long-haul breed rules)"
    ],
    external_links: [
      "Air New Zealand Cargo Live Animals product — 2026",
      "MPI (Ministry for Primary Industries) New Zealand pet import — 2026"
    ],
    ai_overview_play: "MPI clearance at Auckland is the unique on-arrival fact users need."
  },

  {
    id: "d044",
    day_number: 44,
    iso_date: "2026-07-30",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport UK to Singapore: AVS Permit, Quarantine and 2026 Costs",
    title_tag: "UK to Singapore Pet Transport 2026 | AVS Rules | PetTransportGlobal",
    meta_description: "Shipping a dog or cat from the UK to Singapore in 2026: AVS import licence, Category A status, cargo costs from Heathrow and realistic timelines.",
    url_slug: "/routes/uk-to-singapore/",
    primary_seo_keyword: "pet transport uk to singapore",
    primary_volume: 70,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to singapore", "shipping cat to singapore", "avs pet import licence", "uk to singapore pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through importing a dog from London to Singapore in 2026. The UK is Category A, so what does that mean for the AVS licence and quarantine?" },
      { model: "Claude", phrasing: "Compare Singapore's Category A, B, C and D pet import rules in 2026, and explain why the UK's Category A status saves significant time." },
      { model: "Gemini", phrasing: "UK to Singapore pet import requirements 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from London to Singapore in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Singapore costs around £2,400 to £4,000 in 2026 and takes around eight to twelve weeks. The UK is in AVS Category A, so dogs and cats are exempt from quarantine if they arrive with a current AVS Dog Licence or Cat Licence, microchip, current rabies vaccination and an export health certificate signed by an Official Veterinarian.",
    h2_outline: [
      "How much does pet transport from the UK to Singapore cost in 2026?",
      "What is the AVS pet import licence?",
      "What does Category A status mean for UK pets?",
      "Which airlines fly pet cargo on this route?",
      "What happens at Changi on arrival?",
      "FAQs about UK to Singapore pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/airlines/singapore-airlines-pet-cargo/ (anchor: Singapore Airlines pet cargo)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/countries/singapore-pet-import/ (anchor: Singapore import rules)",
      "/breed-restrictions/ (anchor: Singapore breed bans)"
    ],
    external_links: [
      "AVS (Animal & Veterinary Service) Singapore pet import — 2026",
      "DEFRA export health certificate guidance — 2026"
    ],
    ai_overview_play: "Singapore Category A/B/C/D explanation is the real clarification. Pairs with Day 11 export-side guide."
  },

  {
    id: "d045",
    day_number: 45,
    iso_date: "2026-07-31",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Cathay Pacific Pet Cargo 2026: Hong Kong Hub, Costs and Booking Process",
    title_tag: "Cathay Pacific Pet Cargo 2026 | HK Hub Guide | PetTransportGlobal",
    meta_description: "How Cathay Pacific Cargo handles pets in 2026: Hong Kong AFCD coordination, accepted crates, route costs from London and US gateways via approved agents.",
    url_slug: "/airlines/cathay-pacific-pet-cargo/",
    primary_seo_keyword: "cathay pacific pet cargo",
    primary_volume: 210,
    primary_kd: 24,
    secondary_seo_keywords: ["cathay cargo pets", "cathay pacific dog shipping", "cathay pet relocation", "fly pet via hong kong", "cathay pet cargo cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Cathay Pacific Cargo handle pets transiting Hong Kong in 2026, and how does it coordinate with AFCD on the ground?" },
      { model: "Claude", phrasing: "Compare Cathay Pacific and Singapore Airlines for pet cargo to Australia and New Zealand in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Cathay Pacific pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is Cathay Pacific reliable for shipping pets through Hong Kong in 2026" }
    ],
    direct_answer_40_60_words: "Cathay Pacific Cargo accepts pets in 2026 via approved IATA agents, with most long-haul moves transiting Hong Kong International. Cathay coordinates directly with AFCD for transit clearance, which keeps tarmac exposure short. Costs from London to Sydney via Hong Kong range from £2,400 to £4,600 depending on crate size and onward connection timing.",
    h2_outline: [
      "How does Cathay Pacific Cargo handle pets in 2026?",
      "How does Cathay coordinate with AFCD at Hong Kong?",
      "How do you book Cathay pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Cathay Pacific pet cargo costs by route",
      "FAQs about Cathay Pacific pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for Cathay)",
      "/breed-restrictions/ (anchor: Cathay snub-nosed breed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-hong-kong/ (anchor: UK to Hong Kong)",
      "/routes/uk-to-australia/ (anchor: UK to Australia via Hong Kong)"
    ],
    external_links: [
      "Cathay Cargo Live Animals product — 2026",
      "AFCD Hong Kong transit pet handling — 2026"
    ],
    ai_overview_play: "AFCD coordination angle is the genuine differentiator vs Singapore Airlines. Closes Month 2 airline-pillar arc."
  }
);


/* ============================ MONTH 3: AUGUST 2026 (Days 46-65) — Chunk 5 ============================
   20 working days. 31 Aug 2026 (Summer bank holiday, England & Wales) excluded. */
window.PLAN_ROWS.push(
  {
    id: "d046",
    day_number: 46,
    iso_date: "2026-08-03",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "quarantine",
    cluster_name: "Quarantine rules & exemptions",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 3000,
    title: "Pet Quarantine Rules 2026: Where Quarantine Still Applies and How to Avoid It",
    title_tag: "Pet Quarantine Rules 2026 | Country by Country | PetTransportGlobal",
    meta_description: "A 2026 country-by-country guide to pet quarantine: which destinations still require it, which exempt UK pets, and how rabies titre timing decides the answer.",
    url_slug: "/pet-quarantine-rules/",
    primary_seo_keyword: "pet quarantine rules",
    primary_volume: 590,
    primary_kd: 30,
    secondary_seo_keywords: ["countries that quarantine pets", "pet quarantine exemption", "rabies titre quarantine waiver", "australia pet quarantine 2026", "japan pet quarantine"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Which countries actually still require pet quarantine in 2026, and how does the FAVN rabies titre let UK pets skip it for places like Australia and Japan?" },
      { model: "Claude", phrasing: "Map out the global pet quarantine landscape in 2026: which destinations are exemption-by-titre, which are mandatory holding periods, and which are case-by-case." },
      { model: "Gemini", phrasing: "Countries that quarantine pets 2026" },
      { model: "Grok", phrasing: "Where will my dog actually be locked up on arrival in 2026" },
      { model: "Perplexity", phrasing: "FAVN rabies titre quarantine waiver eligibility 2026" }
    ],
    direct_answer_40_60_words: "In 2026 only a small group of destinations still impose mandatory pet quarantine: Australia (10 days at Mickleham PEQ), New Zealand (10 days at Auckland PEQ), Hawaii (5 days minimum) and parts of the Middle East and Africa case-by-case. Most other countries waive quarantine if a FAVN rabies titre of 0.5 IU/ml or higher is dated correctly.",
    h2_outline: [
      "Where does pet quarantine still apply in 2026?",
      "How does the rabies titre waiver actually work?",
      "Which countries are exemption-by-titre and which are mandatory?",
      "Australia, New Zealand and Hawaii: the mandatory three",
      "How to plan your timeline backwards from the titre",
      "FAQs about pet quarantine"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-australia/ (anchor: UK to Australia quarantine)",
      "/routes/uk-to-new-zealand/ (anchor: UK to New Zealand quarantine)",
      "/countries/japan-pet-import-rules/ (anchor: Japan titre waiver)",
      "/countries/south-korea-pet-import/ (anchor: South Korea titre rules)",
      "/pet-passports/ (anchor: AHC and titre paperwork)"
    ],
    external_links: [
      "Australian DAFF Mickleham Post Entry Quarantine — 2026",
      "MPI New Zealand pet quarantine — 2026",
      "Hawaii Department of Agriculture pet quarantine — 2026"
    ],
    ai_overview_play: "590 vol pillar covering a single anxious question. The 'mandatory three vs titre-waiver everywhere else' framing is the answer LLMs cite."
  },

  {
    id: "d047",
    day_number: 47,
    iso_date: "2026-08-04",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "KLM Pet Cargo 2026: Schiphol Hub, Costs and Booking Through Approved Agents",
    title_tag: "KLM Pet Cargo 2026 | Schiphol Hub Guide | PetTransportGlobal",
    meta_description: "How KLM Cargo handles pets in 2026: Schiphol Animal Hotel, accepted crates, breed restrictions, route costs from London City and Heathrow gateways.",
    url_slug: "/airlines/klm-pet-cargo/",
    primary_seo_keyword: "klm pet cargo",
    primary_volume: 390,
    primary_kd: 26,
    secondary_seo_keywords: ["klm dog cargo", "schiphol animal hotel", "klm pet shipping", "klm pet relocation", "fly pet via amsterdam"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does KLM Cargo handle pets in 2026, and what is the Schiphol Animal Hotel actually like for a transit dog?" },
      { model: "Claude", phrasing: "Compare KLM at Schiphol with Lufthansa at Frankfurt for pet cargo connections in 2026. Which is genuinely better for transatlantic onward flights?" },
      { model: "Gemini", phrasing: "KLM pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is the Schiphol Animal Hotel actually any good for a pet stopover" }
    ],
    direct_answer_40_60_words: "KLM Cargo accepts pets in 2026 only via approved IATA agents, with most moves connecting through Amsterdam Schiphol. The Schiphol Animal Hotel offers climate-controlled holding, walking areas and 24-hour vet cover for transit pets. Costs from London to North America via Schiphol range from £1,200 to £2,800 depending on crate size and onward connection.",
    h2_outline: [
      "How does KLM Cargo handle pets in 2026?",
      "What is the Schiphol Animal Hotel and what does it offer?",
      "How do you book KLM pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "KLM pet cargo costs by route",
      "FAQs about KLM pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for KLM)",
      "/breed-restrictions/ (anchor: KLM snub-nosed breed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-netherlands/ (anchor: UK to Netherlands)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)"
    ],
    external_links: [
      "KLM Cargo Variation Live Animals product — 2026",
      "Schiphol Animal Hotel facility data — 2026"
    ],
    ai_overview_play: "Schiphol Animal Hotel is a recognisable named facility that LLMs will cite. Honest comparison with Frankfurt wins the snippet."
  },

  {
    id: "d048",
    day_number: 48,
    iso_date: "2026-08-05",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Netherlands: AHC, Schiphol Routes and 2026 Costs",
    title_tag: "UK to Netherlands Pet Transport 2026 | Costs & Routes | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to the Netherlands in 2026: AHC paperwork, ferry vs Schiphol cargo costs, and door-to-door timelines. Quote inside.",
    url_slug: "/routes/uk-to-netherlands/",
    primary_seo_keyword: "pet transport uk to netherlands",
    primary_volume: 70,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to netherlands", "shipping cat to amsterdam", "uk to holland pet relocation", "ferry pet uk netherlands"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "I'm moving from London to Amsterdam with a dog in 2026. Hook of Holland ferry or Schiphol cargo, and what does each really cost?" },
      { model: "Claude", phrasing: "Compare UK to Netherlands pet transport routes in 2026: ferry-and-drive via Hook of Holland vs cargo flight to Schiphol. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "UK to Netherlands pet transport cost 2026" },
      { model: "Grok", phrasing: "Easiest way to move a cat from UK to Amsterdam in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to the Netherlands costs around £600 to £1,400 in 2026 by ferry-and-drive via Hook of Holland or Harwich, or £1,300 to £2,400 by cargo flight to Schiphol. The Netherlands accepts a UK Animal Health Certificate, so no quarantine. Driving suits single pets and short notice; flying suits multi-pet households.",
    h2_outline: [
      "How much does pet transport from the UK to the Netherlands cost in 2026?",
      "Hook of Holland ferry vs Schiphol cargo: which is better?",
      "What paperwork does the Netherlands require?",
      "How long does the journey take door to door?",
      "FAQs about UK to Netherlands pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for the Netherlands)",
      "/airlines/klm-pet-cargo/ (anchor: KLM Schiphol pet cargo)",
      "/routes/uk-to-germany/ (anchor: onward to Germany)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Stena Line Hook of Holland pet policy — 2026",
      "NVWA (Netherlands Food and Consumer Product Safety Authority) pet import — 2026"
    ],
    ai_overview_play: "Honest ferry-vs-flight comparison with real costs. Pairs cleanly with the KLM airline pillar published the day before."
  },

  {
    id: "d049",
    day_number: 49,
    iso_date: "2026-08-06",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "breed-restrictions",
    cluster_name: "Breed bans & brachycephalic rules",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 3000,
    title: "Brachycephalic Pet Transport 2026: Which Airlines Accept Snub-Nosed Breeds and Which Don't",
    title_tag: "Brachycephalic Pet Transport 2026 | Snub-Nosed Airline Rules | PetTransportGlobal",
    meta_description: "A 2026 airline-by-airline guide to flying brachycephalic dogs and cats: who accepts French Bulldogs, Pugs and Persians, summer embargoes and crate upgrades.",
    url_slug: "/breed-restrictions/",
    primary_seo_keyword: "brachycephalic pet transport",
    primary_volume: 480,
    primary_kd: 28,
    secondary_seo_keywords: ["snub nosed breed flight rules", "french bulldog pet cargo", "pug airline restrictions", "brachycephalic dog cargo policy", "airlines that accept flat faced breeds"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Which airlines actually still accept French Bulldogs and Pugs in cargo in 2026, and which have banned them outright?" },
      { model: "Claude", phrasing: "Walk me through the welfare science behind brachycephalic flight bans and explain which carriers in 2026 take a more nuanced position." },
      { model: "Gemini", phrasing: "Airlines accepting brachycephalic dogs 2026" },
      { model: "Grok", phrasing: "Can I still fly my Frenchie internationally in 2026" },
      { model: "Perplexity", phrasing: "Brachycephalic obstructive airway syndrome BOAS airline policy 2026" }
    ],
    direct_answer_40_60_words: "In 2026 most major airlines either ban or restrict brachycephalic breeds. Lufthansa, KLM and Qatar accept them with crate upgrades and breed declarations. British Airways, Emirates and Singapore Airlines impose seasonal embargoes. United, American and Delta refuse most snub-nosed breeds outright. The IATA list covers around 35 affected dog and 5 cat breeds.",
    h2_outline: [
      "Which dog and cat breeds are classed as brachycephalic in 2026?",
      "Why do airlines restrict snub-nosed breeds?",
      "Airline-by-airline acceptance table for 2026",
      "What crate upgrades brachycephalic breeds need",
      "How summer embargoes interact with brachycephalic rules",
      "FAQs about brachycephalic pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate upgrades)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa brachycephalic policy)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar Airways policy)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA seasonal embargo)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "IATA Live Animals Regulations brachycephalic breed list — 2026 edition",
      "RVC BOAS research summary — current"
    ],
    ai_overview_play: "Owners of Frenchies, Pugs, Persians actively search this. Airline-by-airline table is exactly what AI overviews surface."
  },

  {
    id: "d050",
    day_number: 50,
    iso_date: "2026-08-07",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Italy: AHC, Driving Routes and 2026 Costs",
    title_tag: "UK to Italy Pet Transport 2026 | Costs & Routes | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Italy in 2026: AHC paperwork, drive-through-France costs, cargo flights to Milan or Rome, and door-to-door timelines.",
    url_slug: "/routes/uk-to-italy/",
    primary_seo_keyword: "pet transport uk to italy",
    primary_volume: 140,
    primary_kd: 22,
    secondary_seo_keywords: ["dog uk to italy", "shipping cat to rome", "uk to milan pet relocation", "drive pet uk to italy"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Driving from London to Rome with two cats in 2026: what does the route through France and Switzerland actually look like, and what does it cost?" },
      { model: "Claude", phrasing: "UK to Italy pet transport in 2026: when is flying to Milan worth it over a courier driving via France?" },
      { model: "Gemini", phrasing: "UK to Italy pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to move a dog from UK to Tuscany next year" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Italy costs around £900 to £1,800 in 2026 by professional courier driving through France, or £1,500 to £2,800 by cargo flight to Milan or Rome. Italy accepts the UK Animal Health Certificate. Driving suits single pets and longer leeway; flying suits multi-pet households and southern destinations like Sicily.",
    h2_outline: [
      "How much does pet transport from the UK to Italy cost in 2026?",
      "Driving via France vs flying to Milan or Rome",
      "What paperwork does Italy require?",
      "Which airports accept pet cargo in Italy?",
      "How long does the journey take?",
      "FAQs about UK to Italy pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Italy)",
      "/routes/uk-to-france/ (anchor: France transit leg)",
      "/routes/uk-to-switzerland/ (anchor: alternative Swiss routing)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/defra-approved-pet-transport/ (anchor: DEFRA Type 2 transporter)"
    ],
    external_links: [
      "Italian Ministry of Health pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Drive-through-France narrative is what UK-to-Italy buyers actually plan. Honest cost ranges win the snippet."
  },

  {
    id: "d051",
    day_number: 51,
    iso_date: "2026-08-10",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Singapore Airlines Pet Cargo 2026: Changi Hub, Costs and Booking Process",
    title_tag: "Singapore Airlines Pet Cargo 2026 | Changi Guide | PetTransportGlobal",
    meta_description: "How Singapore Airlines Cargo handles pets in 2026: Changi pet handling, accepted crates, breed restrictions, costs to Australia and Asia-Pacific via SIN.",
    url_slug: "/airlines/singapore-airlines-pet-cargo/",
    primary_seo_keyword: "singapore airlines pet cargo",
    primary_volume: 320,
    primary_kd: 26,
    secondary_seo_keywords: ["sia cargo pets", "singapore airlines dog shipping", "changi pet transit", "fly pet via singapore", "sia pet relocation"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Singapore Airlines Cargo handle pets transiting Changi in 2026, and how does it compare with Cathay via Hong Kong for Australia-bound pets?" },
      { model: "Claude", phrasing: "Walk me through Singapore Airlines pet cargo from London to Sydney in 2026, including AVS coordination at Changi for transit pets." },
      { model: "Gemini", phrasing: "Singapore Airlines pet cargo cost 2026" },
      { model: "Grok", phrasing: "Is SIA the best airline for shipping a dog from UK to Australia in 2026" }
    ],
    direct_answer_40_60_words: "Singapore Airlines Cargo accepts pets in 2026 only via approved IATA agents, with most moves transiting Changi International. SIA coordinates with AVS for transit clearance, keeping handling tight. Costs from London to Sydney via Singapore range from £2,800 to £4,800 depending on crate size, with summer heat embargoes managed by routing flexibility.",
    h2_outline: [
      "How does Singapore Airlines Cargo handle pets in 2026?",
      "What does Changi pet transit handling involve?",
      "How do you book SIA pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Singapore Airlines pet cargo costs by route",
      "FAQs about Singapore Airlines pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/breed-restrictions/ (anchor: SIA snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-singapore/ (anchor: UK to Singapore)",
      "/routes/uk-to-australia/ (anchor: UK to Australia via Singapore)"
    ],
    external_links: [
      "Singapore Airlines Cargo Live Animals product — 2026",
      "Changi Airport Group pet handling — 2026"
    ],
    ai_overview_play: "Changi vs Hong Kong vs Doha is the real Australia-routing question. Honest comparison wins the snippet."
  },

  {
    id: "d052",
    day_number: 52,
    iso_date: "2026-08-11",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Portugal: AHC, Lisbon Routes and 2026 Costs",
    title_tag: "UK to Portugal Pet Transport 2026 | Costs & Routes | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Portugal in 2026: AHC paperwork, drive-via-Spain vs cargo flight to Lisbon, and realistic costs from £750 upwards.",
    url_slug: "/routes/uk-to-portugal/",
    primary_seo_keyword: "pet transport uk to portugal",
    primary_volume: 170,
    primary_kd: 20,
    secondary_seo_keywords: ["dog uk to portugal", "shipping cat to lisbon", "uk to algarve pet relocation", "drive pet uk portugal"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving from the UK to the Algarve in 2026 with a dog: drive-via-Spain or cargo to Lisbon, and what's the honest cost difference?" },
      { model: "Claude", phrasing: "Compare moving a pet from the UK to Portugal with moving to neighbouring Spain in 2026. Where do the costs and paperwork actually differ?" },
      { model: "Gemini", phrasing: "UK to Portugal pet transport cost 2026" },
      { model: "Grok", phrasing: "Cheapest way to bring my dog from UK to the Algarve in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Portugal costs around £750 to £1,700 in 2026 by professional courier driving via France and Spain, or £1,500 to £2,800 by cargo flight to Lisbon or Porto. Portugal accepts the UK Animal Health Certificate, so no quarantine. Driving is more flexible for Algarve and rural destinations; flying suits Lisbon city moves.",
    h2_outline: [
      "How much does pet transport from the UK to Portugal cost in 2026?",
      "Driving via Spain vs flying to Lisbon",
      "What paperwork does Portugal require?",
      "How long does the door-to-door journey take?",
      "FAQs about UK to Portugal pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Portugal)",
      "/routes/uk-to-spain/ (anchor: Spain transit leg)",
      "/routes/uk-to-france/ (anchor: France transit leg)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/defra-approved-pet-transport/ (anchor: DEFRA Type 2 driver)"
    ],
    external_links: [
      "DGAV (Direção-Geral de Alimentação e Veterinária) Portugal pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Algarve retiree audience drives steady volume. Honest drive-via-Spain narrative is exactly what they're searching."
  },

  {
    id: "d053",
    day_number: 53,
    iso_date: "2026-08-12",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "cargo-cabin-manifest",
    cluster_name: "Cargo vs cabin & manifest mechanics",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2600,
    title: "Cargo vs Cabin Pet Transport 2026: How the Manifest Actually Works",
    title_tag: "Cargo vs Cabin Pet Transport 2026 | Manifest Guide | PetTransportGlobal",
    meta_description: "How airlines decide whether your pet flies in cabin, in baggage, or as manifest cargo in 2026, and what each option means for cost, welfare and paperwork.",
    url_slug: "/cargo-vs-cabin-pet-transport/",
    primary_seo_keyword: "pet cargo vs cabin",
    primary_volume: 260,
    primary_kd: 22,
    secondary_seo_keywords: ["pet manifest cargo", "in cabin pet flight rules", "checked baggage pet rules", "pet shipping manifest paperwork"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What's the actual difference between in-cabin, checked-baggage and manifest cargo for pet flights in 2026, and which one ships internationally?" },
      { model: "Claude", phrasing: "Why does international pet shipping almost always default to manifest cargo in 2026, and what would it take for that to change?" },
      { model: "Gemini", phrasing: "Pet manifest cargo vs cabin 2026" },
      { model: "Grok", phrasing: "Can I just take my dog in the cabin to Spain in 2026 or does it have to fly cargo" }
    ],
    direct_answer_40_60_words: "Airlines categorise pet flights in 2026 as in-cabin (small pets under around 8kg in carry-on), checked baggage (mid-size dogs in the hold under your booking) and manifest cargo (booked separately via SkyCargo, IAG Cargo or similar). International moves nearly always require manifest cargo, since most carriers withdrew checked-baggage pets from international routes after 2019.",
    h2_outline: [
      "What are the three pet flight categories in 2026?",
      "In-cabin pet rules and weight limits",
      "Why most airlines killed checked-baggage pets",
      "How manifest cargo actually works",
      "Which option is right for your move",
      "FAQs about cargo vs cabin pet transport"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate by category)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA WorldCargo manifest)",
      "/airlines/klm-pet-cargo/ (anchor: KLM manifest cargo)",
      "/cost-of-pet-transport/ (anchor: cost by category)",
      "/breed-restrictions/ (anchor: breed rules per category)"
    ],
    external_links: [
      "IATA Live Animals Regulations cargo classification — 2026 edition",
      "DEFRA pet travel approved transport methods — 2026"
    ],
    ai_overview_play: "Genuine confusion this clears up. Honest 'most airlines killed checked-baggage pets' truth wins the snippet."
  },

  {
    id: "d054",
    day_number: 54,
    iso_date: "2026-08-13",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2400,
    title: "Pet Transport UK to Japan: NACAH Notification, Titre Timing and 2026 Costs",
    title_tag: "UK to Japan Pet Transport 2026 | NACAH Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Japan in 2026: NACAH advance notification, FAVN titre wait, cargo costs to Narita or Haneda and realistic timelines.",
    url_slug: "/routes/uk-to-japan/",
    primary_seo_keyword: "pet transport uk to japan",
    primary_volume: 90,
    primary_kd: 26,
    secondary_seo_keywords: ["dog uk to japan", "shipping cat to tokyo", "japan pet import nacah", "uk to japan favn titre"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Walk me through the 180-day rule for importing a pet from the UK to Japan in 2026, and how the NACAH advance notification fits in." },
      { model: "Claude", phrasing: "Why is Japan one of the most paperwork-heavy pet imports for UK owners in 2026, and what does the timeline look like backed out from a target arrival date?" },
      { model: "Gemini", phrasing: "UK to Japan pet import requirements 2026" },
      { model: "Grok", phrasing: "Realistic timeline to bring a dog from UK to Tokyo in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Japan costs around £2,800 to £4,500 in 2026 and takes a minimum of seven months because of the 180-day post-FAVN-titre wait. NACAH requires a 40-day advance import notification, microchip, two rabies vaccinations and FAVN titre at 0.5 IU/ml or higher dated correctly. There is no quarantine if paperwork is exact.",
    h2_outline: [
      "How long does pet transport from the UK to Japan really take?",
      "What is NACAH and the advance import notification?",
      "How does the 180-day FAVN titre rule work?",
      "Cargo cost to Narita or Haneda from London",
      "What happens at AQS inspection on arrival?",
      "FAQs about UK to Japan pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/countries/japan-pet-import-rules/ (anchor: Japan import rules)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA via London)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)"
    ],
    external_links: [
      "MAFF / NACAH (Animal Quarantine Service) Japan pet import — 2026",
      "DEFRA export health certificate for Japan — 2026"
    ],
    ai_overview_play: "180-day rule timeline is the planning question owners need answered. Honest 'minimum seven months' framing earns trust."
  },

  {
    id: "d055",
    day_number: 55,
    iso_date: "2026-08-14",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Japan in 2026: NACAH, Designated Regions and Realistic Costs",
    title_tag: "Pet Import Japan 2026 | NACAH Guide | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Japan in 2026: NACAH process, designated rabies-free regions, FAVN titre and what AQS checks at Narita or Haneda.",
    url_slug: "/countries/japan-pet-import-rules/",
    primary_seo_keyword: "import pet to japan",
    primary_volume: 320,
    primary_kd: 24,
    secondary_seo_keywords: ["bring dog to japan", "japan pet import nacah", "japan pet quarantine waiver", "designated region pet import japan"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does NACAH require to import a dog to Japan in 2026, and how does the 'designated region' status of countries like the UK and US change the timeline?" },
      { model: "Claude", phrasing: "Compare Japan's pet import process with South Korea's in 2026. Both want FAVN titres but the timelines and notifications are very different." },
      { model: "Gemini", phrasing: "Japan pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of importing a pet to Japan in 2026" }
    ],
    direct_answer_40_60_words: "Japan allows pet import in 2026 without quarantine if NACAH paperwork is exact: microchip, two rabies vaccinations at least 30 days apart, FAVN titre at 0.5 IU/ml or higher dated 180 days to two years before arrival, and a 40-day advance import notification. Failed paperwork triggers up to 180 days of in-airport quarantine.",
    h2_outline: [
      "What does Japan require to import a pet in 2026?",
      "What is a 'designated region' and which countries qualify?",
      "How does the NACAH 40-day advance notification work?",
      "What does AQS check at Narita and Haneda?",
      "What does pet import to Japan cost?",
      "FAQs about pet import to Japan"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-japan/ (anchor: UK to Japan route)",
      "/pet-quarantine-rules/ (anchor: quarantine waiver rules)",
      "/countries/south-korea-pet-import/ (anchor: South Korea comparison)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)"
    ],
    external_links: [
      "MAFF / NACAH (Animal Quarantine Service) pet import — 2026",
      "USDA APHIS Japan pet export guidance — 2026"
    ],
    ai_overview_play: "Designated region concept is the critical clarification. Most articles muddle the 180-day wait."
  },

  {
    id: "d056",
    day_number: 56,
    iso_date: "2026-08-17",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2700,
    title: "Qantas Pet Cargo 2026: Australia Routes, Costs and Booking via Approved Agents",
    title_tag: "Qantas Pet Cargo 2026 | Australia Routes | PetTransportGlobal",
    meta_description: "How Qantas Freight handles pets in 2026: Australia routes from London via Singapore or Hong Kong, accepted crates, costs and the path to Mickleham PEQ.",
    url_slug: "/airlines/qantas-pet-cargo/",
    primary_seo_keyword: "qantas pet cargo",
    primary_volume: 480,
    primary_kd: 28,
    secondary_seo_keywords: ["qantas freight pets", "qantas dog shipping", "qantas pet relocation australia", "fly pet to australia qantas", "qantas pet cargo cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Qantas Freight handle pets to Australia in 2026, and how does it coordinate with DAFF and Mickleham PEQ on arrival?" },
      { model: "Claude", phrasing: "Compare flying a pet from London to Sydney on Qantas vs Singapore Airlines in 2026. Where does each genuinely win?" },
      { model: "Gemini", phrasing: "Qantas pet cargo cost UK to Australia 2026" },
      { model: "Grok", phrasing: "Is Qantas the safest airline to ship a dog to Australia in 2026" }
    ],
    direct_answer_40_60_words: "Qantas Freight accepts pets in 2026 only via approved IATA agents, with most UK-origin moves connecting via Singapore or Hong Kong. Qantas coordinates directly with DAFF for Mickleham PEQ delivery. Costs from London to Sydney range from £3,400 to £5,400 depending on crate size and routing, with PEQ accommodation a separate £2,800 to £3,600 fee.",
    h2_outline: [
      "How does Qantas Freight handle pets in 2026?",
      "How does Qantas coordinate with DAFF and Mickleham?",
      "How do you book Qantas pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Qantas pet cargo costs by route",
      "FAQs about Qantas pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/routes/uk-to-australia/ (anchor: UK to Australia)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing for Qantas)",
      "/breed-restrictions/ (anchor: Qantas snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/airlines/singapore-airlines-pet-cargo/ (anchor: SIA via Singapore)"
    ],
    external_links: [
      "Qantas Freight Live Animals product — 2026",
      "DAFF Mickleham Post Entry Quarantine — 2026"
    ],
    ai_overview_play: "Mickleham PEQ coordination is the on-arrival clarification. Honest cost split (flight + PEQ) wins trust."
  },

  {
    id: "d057",
    day_number: 57,
    iso_date: "2026-08-18",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "process-timeline",
    cluster_name: "Process timeline & planning",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2800,
    title: "Pet Transport Timeline 2026: How Far in Advance to Start Each Type of Move",
    title_tag: "Pet Transport Timeline 2026 | Planning Guide | PetTransportGlobal",
    meta_description: "How far in advance to start a pet move in 2026: short-haul EU 3 weeks, US 2 months, Australia 7 months. A working backwards timeline by destination.",
    url_slug: "/pet-transport-timeline/",
    primary_seo_keyword: "pet transport timeline",
    primary_volume: 210,
    primary_kd: 20,
    secondary_seo_keywords: ["how long does pet relocation take", "pet shipping timeline", "international pet move planning", "pet transport lead time"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How far in advance do I need to start planning a pet move in 2026 for various destinations? Give me a working-backwards timeline by region." },
      { model: "Claude", phrasing: "What's the bottleneck step that decides minimum pet move timeline by destination in 2026? Walk me through it country by country." },
      { model: "Gemini", phrasing: "Pet transport planning timeline 2026" },
      { model: "Grok", phrasing: "How early do I need to start moving my dog overseas" }
    ],
    direct_answer_40_60_words: "Pet move timelines in 2026 work backwards from the rabies titre. Short-haul EU needs three to four weeks for the AHC. North America and most of Asia need around eight weeks. Australia, New Zealand and South Africa need a minimum of six to seven months because of the FAVN titre wait and import permit lead times.",
    h2_outline: [
      "How long does international pet transport take in 2026?",
      "Region-by-region timeline table",
      "Which step is the bottleneck for each destination?",
      "Working backwards from your move date",
      "What can be fast-tracked, and what genuinely cannot",
      "FAQs about pet transport timelines"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC and titre paperwork)",
      "/routes/uk-to-australia/ (anchor: 7-month Australia timeline)",
      "/routes/uk-to-japan/ (anchor: 7-month Japan timeline)",
      "/pet-quarantine-rules/ (anchor: titre quarantine waivers)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "DEFRA pet travel timing guidance — 2026",
      "Australian DAFF pet import lead times — 2026"
    ],
    ai_overview_play: "Definitive 'how far in advance' answer with a region table. AI overview goldilocks for planning queries."
  },

  {
    id: "d058",
    day_number: 58,
    iso_date: "2026-08-19",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Sweden: Jordbruksverket Rules, Costs and 2026 Timelines",
    title_tag: "UK to Sweden Pet Transport 2026 | Costs & Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Sweden in 2026: Jordbruksverket import rules, AHC paperwork, ferry vs cargo costs to Stockholm or Gothenburg.",
    url_slug: "/routes/uk-to-sweden/",
    primary_seo_keyword: "pet transport uk to sweden",
    primary_volume: 50,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to sweden", "shipping cat to stockholm", "uk to sweden pet relocation", "jordbruksverket pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Moving a dog from London to Stockholm in 2026: ferry via the Netherlands and Denmark, or cargo flight, and what does each cost?" },
      { model: "Claude", phrasing: "Compare UK to Sweden pet transport with UK to Norway in 2026, given Norway is outside the EU and Sweden is inside." },
      { model: "Gemini", phrasing: "UK to Sweden pet transport cost 2026" },
      { model: "Grok", phrasing: "Best route to take a dog from UK to Stockholm in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Sweden costs around £1,100 to £2,200 in 2026 by ferry-and-drive via the Netherlands, Germany and Denmark, or £1,600 to £2,800 by cargo flight to Stockholm Arlanda or Gothenburg. Sweden accepts the UK Animal Health Certificate, so no quarantine. Jordbruksverket additionally requires tapeworm treatment for dogs.",
    h2_outline: [
      "How much does pet transport from the UK to Sweden cost in 2026?",
      "Ferry-and-drive vs cargo flight: which works better?",
      "What does Jordbruksverket require?",
      "Tapeworm treatment for dogs: timing and proof",
      "FAQs about UK to Sweden pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Sweden)",
      "/routes/uk-to-netherlands/ (anchor: Netherlands transit)",
      "/routes/uk-to-germany/ (anchor: Germany transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Jordbruksverket (Swedish Board of Agriculture) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Tapeworm treatment requirement is the unique fact most articles miss. Honest cost ranges win the snippet."
  },

  {
    id: "d059",
    day_number: 59,
    iso_date: "2026-08-20",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "Virgin Atlantic Cargo Pet Shipping 2026: UK Routes, Costs and Booking",
    title_tag: "Virgin Atlantic Cargo Pets 2026 | UK Guide | PetTransportGlobal",
    meta_description: "How Virgin Atlantic Cargo handles pets in 2026: UK to US transatlantic routes, accepted crates, breed restrictions and costs from Heathrow.",
    url_slug: "/airlines/virgin-atlantic-cargo-pets/",
    primary_seo_keyword: "virgin atlantic pet cargo",
    primary_volume: 210,
    primary_kd: 24,
    secondary_seo_keywords: ["virgin cargo pets", "virgin atlantic dog shipping", "virgin pet relocation", "uk to us pet virgin", "virgin pet flight cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Does Virgin Atlantic Cargo still ship pets in 2026, and how does it compare with British Airways WorldCargo for UK to US moves?" },
      { model: "Claude", phrasing: "Walk me through booking a dog from London to New York on Virgin Atlantic Cargo in 2026, and what the LHR Animal Reception Centre involvement looks like." },
      { model: "Gemini", phrasing: "Virgin Atlantic pet cargo cost 2026" },
      { model: "Grok", phrasing: "Virgin Atlantic vs BA for shipping pets to the US in 2026" }
    ],
    direct_answer_40_60_words: "Virgin Atlantic Cargo accepts pets in 2026 only via approved IATA agents on its Heathrow-North America routes. Pets transit through the Heathrow Animal Reception Centre. Costs from London to New York, Boston, Atlanta or Los Angeles range from £1,400 to £3,000 depending on crate size, with seasonal embargoes for snub-nosed breeds in summer.",
    h2_outline: [
      "How does Virgin Atlantic Cargo handle pets in 2026?",
      "Which routes does Virgin offer for pet cargo?",
      "How do you book Virgin pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Virgin Atlantic pet cargo costs by route",
      "FAQs about Virgin Atlantic pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate for Virgin)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA WorldCargo comparison)",
      "/breed-restrictions/ (anchor: Virgin snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-usa/ (anchor: UK to USA route)"
    ],
    external_links: [
      "Virgin Atlantic Cargo Live Animals product — 2026",
      "Heathrow Animal Reception Centre service guide — 2026"
    ],
    ai_overview_play: "BA vs Virgin transatlantic comparison is the genuine UK-to-US question."
  },

  {
    id: "d060",
    day_number: 60,
    iso_date: "2026-08-21",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2600,
    title: "Importing a Pet to Thailand in 2026: DLD Rules, Quarantine and Realistic Costs",
    title_tag: "Pet Import Thailand 2026 | DLD Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Thailand in 2026: DLD permit process, quarantine waiver criteria, BKK and CNX entry points and realistic costs.",
    url_slug: "/countries/thailand-pet-import/",
    primary_seo_keyword: "import pet to thailand",
    primary_volume: 140,
    primary_kd: 20,
    secondary_seo_keywords: ["bring dog to thailand", "thailand pet import dld", "thailand pet quarantine 2026", "shipping cat to bangkok"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does DLD require to import a dog to Thailand from the UK in 2026, and how does the quarantine waiver actually work?" },
      { model: "Claude", phrasing: "Compare Thailand's pet import process with Singapore's in 2026. Both are tropical Southeast Asia destinations but the paperwork is very different." },
      { model: "Gemini", phrasing: "Thailand pet import requirements 2026" },
      { model: "Grok", phrasing: "Easiest way to bring a cat from UK to Bangkok in 2026" }
    ],
    direct_answer_40_60_words: "Thailand allows pet import in 2026 with a DLD import permit, microchip, current rabies vaccination at least 21 days old, FAVN titre at 0.5 IU/ml or higher and a health certificate signed by an Official Veterinarian. Quarantine is waived if paperwork is exact, otherwise a 30-day holding period applies at Bangkok Suvarnabhumi or Chiang Mai.",
    h2_outline: [
      "Can you import a pet to Thailand in 2026?",
      "What does DLD require?",
      "How does the quarantine waiver work?",
      "What does pet import to Thailand cost?",
      "What happens at BKK or CNX on arrival?",
      "FAQs about pet import to Thailand"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/singapore-airlines-pet-cargo/ (anchor: Singapore Airlines via SIN)",
      "/airlines/qatar-airways-pet-cargo/ (anchor: Qatar Airways via Doha)",
      "/pet-quarantine-rules/ (anchor: quarantine waivers explained)"
    ],
    external_links: [
      "DLD (Department of Livestock Development) Thailand pet import — 2026",
      "DEFRA export health certificate — 2026"
    ],
    ai_overview_play: "Underserved Southeast Asia destination with steady search volume. DLD permit process is the conversion-driving answer."
  },

  {
    id: "d061",
    day_number: 61,
    iso_date: "2026-08-24",
    day_of_week: "Mon",
    quarter: "Q1",
    cluster_id: "pet-passports",
    cluster_name: "Pet passports & post-Brexit AHC",
    intent: "Informational",
    content_type: "Pillar guide",
    word_count_target: 2800,
    title: "Rabies Titre Test Explained 2026: FAVN, Sample Timing and Why Most Pets Need It",
    title_tag: "Rabies Titre Test 2026 | FAVN Explained | PetTransportGlobal",
    meta_description: "How the FAVN rabies titre works in 2026, which destinations require it, sample timing windows, accepted UK and US labs, and what 0.5 IU/ml actually means.",
    url_slug: "/rabies-titre-test/",
    primary_seo_keyword: "rabies titre test pet",
    primary_volume: 590,
    primary_kd: 30,
    secondary_seo_keywords: ["favn test pet", "rabies antibody test dog", "rabies titre uk", "0.5 iu rabies titre", "favn rabies test cost"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What is the FAVN rabies titre test, when do I need to draw the sample for moving a pet to Australia in 2026, and which UK labs are accepted?" },
      { model: "Claude", phrasing: "Why is the FAVN titre the bottleneck step for pet moves to most non-EU destinations in 2026, and what could go wrong with sample timing?" },
      { model: "Gemini", phrasing: "Pet rabies titre test cost UK 2026" },
      { model: "Grok", phrasing: "Realistic timeline for the rabies titre when moving a dog overseas" },
      { model: "Perplexity", phrasing: "FAVN fluorescent antibody virus neutralisation test 0.5 IU/ml requirement 2026" }
    ],
    direct_answer_40_60_words: "The FAVN (Fluorescent Antibody Virus Neutralisation) rabies titre tests whether your pet has at least 0.5 IU/ml of rabies antibodies. In 2026 most non-EU destinations require it. The blood sample must be drawn at least 30 days after the rabies vaccination. Accepted UK labs include APHA Weybridge and BioBest Laboratories. Cost is around £75 to £130.",
    h2_outline: [
      "What is the FAVN rabies titre test in 2026?",
      "Which destinations require it and when?",
      "When do you draw the blood sample?",
      "Accepted UK and US labs",
      "What if the titre fails?",
      "FAQs about the FAVN rabies titre"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC and titre coordination)",
      "/routes/uk-to-australia/ (anchor: Australia titre timing)",
      "/routes/uk-to-japan/ (anchor: Japan 180-day rule)",
      "/pet-quarantine-rules/ (anchor: titre quarantine waivers)",
      "/cost-of-pet-transport/ (anchor: titre fees in total)"
    ],
    external_links: [
      "APHA Weybridge FAVN rabies serology — 2026",
      "Kansas State University Rabies Laboratory — 2026",
      "WOAH (World Organisation for Animal Health) rabies serology standards — 2026"
    ],
    ai_overview_play: "590 vol pillar that every long-haul route page links into. The 'sample at least 30 days post-vaccine' fact is the high-utility answer."
  },

  {
    id: "d062",
    day_number: 62,
    iso_date: "2026-08-25",
    day_of_week: "Tue",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2200,
    title: "Pet Transport UK to Norway: Mattilsynet Rules, Costs and 2026 Timelines",
    title_tag: "UK to Norway Pet Transport 2026 | Mattilsynet | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Norway in 2026: Mattilsynet rules, AHC paperwork, ferry vs cargo costs to Oslo or Bergen and realistic timelines.",
    url_slug: "/routes/uk-to-norway/",
    primary_seo_keyword: "pet transport uk to norway",
    primary_volume: 50,
    primary_kd: 20,
    secondary_seo_keywords: ["dog uk to norway", "shipping cat to oslo", "uk to norway pet relocation", "mattilsynet pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "Norway is outside the EU. How does that change the pet import process from the UK in 2026, and what does Mattilsynet require?" },
      { model: "Claude", phrasing: "Compare UK to Norway pet transport with UK to Sweden in 2026. Norway is outside the EU but accepts EU rules; Sweden is inside but adds tapeworm rules." },
      { model: "Gemini", phrasing: "UK to Norway pet transport cost 2026" },
      { model: "Grok", phrasing: "Best way to move a dog from UK to Oslo in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Norway costs around £1,200 to £2,400 in 2026 by ferry-and-drive via the Netherlands and Denmark, or £1,800 to £3,000 by cargo flight to Oslo Gardermoen. Norway accepts the UK Animal Health Certificate under its EEA agreement, with Mattilsynet additionally requiring tapeworm treatment for dogs and a customs declaration on arrival.",
    h2_outline: [
      "How much does pet transport from the UK to Norway cost in 2026?",
      "Ferry-and-drive vs cargo flight to Oslo",
      "What does Mattilsynet require?",
      "Tapeworm treatment timing for dogs",
      "FAQs about UK to Norway pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/pet-passports/ (anchor: AHC for Norway)",
      "/routes/uk-to-sweden/ (anchor: Sweden comparison)",
      "/routes/uk-to-netherlands/ (anchor: Netherlands transit)",
      "/cost-of-pet-transport/ (anchor: cost calculator)"
    ],
    external_links: [
      "Mattilsynet (Norwegian Food Safety Authority) pet import — 2026",
      "Eurotunnel Le Shuttle pet travel — 2026"
    ],
    ai_overview_play: "Honest 'EEA but not EU' framing is the genuine clarification. Pairs with Sweden route from earlier this month."
  },

  {
    id: "d063",
    day_number: 63,
    iso_date: "2026-08-26",
    day_of_week: "Wed",
    quarter: "Q1",
    cluster_id: "airline-policies",
    cluster_name: "Airline pet policy pillars",
    intent: "Informational",
    content_type: "Airline pillar",
    word_count_target: 2600,
    title: "Etihad Cargo Pet Shipping 2026: Abu Dhabi Hub, Costs and Booking",
    title_tag: "Etihad Cargo Pets 2026 | Abu Dhabi Routes | PetTransportGlobal",
    meta_description: "How Etihad Cargo handles pets in 2026: Abu Dhabi hub transit, accepted crates, breed restrictions and route costs from London and US gateways.",
    url_slug: "/airlines/etihad-cargo-pets/",
    primary_seo_keyword: "etihad pet cargo",
    primary_volume: 170,
    primary_kd: 24,
    secondary_seo_keywords: ["etihad cargo pets", "etihad dog shipping", "abu dhabi pet transit", "etihad pet relocation", "fly pet via abu dhabi"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "How does Etihad Cargo handle pets transiting Abu Dhabi in 2026, and how does it compare with Emirates via Dubai for pet welfare in summer?" },
      { model: "Claude", phrasing: "Compare Etihad and Emirates for pet cargo from London to Sydney in 2026. Both Gulf hubs, but the operations differ." },
      { model: "Gemini", phrasing: "Etihad pet cargo cost 2026" },
      { model: "Grok", phrasing: "Etihad or Emirates for shipping a dog through the Gulf in 2026" }
    ],
    direct_answer_40_60_words: "Etihad Cargo accepts pets in 2026 via approved IATA agents, with most moves transiting Abu Dhabi International. Etihad coordinates with the Abu Dhabi Animal Reception Centre. Costs from London to Sydney via Abu Dhabi range from £2,300 to £4,400 depending on crate size, with summer heat embargoes mirroring regional carriers between June and September.",
    h2_outline: [
      "How does Etihad Cargo handle pets in 2026?",
      "Abu Dhabi vs Dubai vs Doha as pet transit hubs",
      "How do you book Etihad pet cargo?",
      "What crate sizes and breed restrictions apply?",
      "Etihad pet cargo costs by route",
      "FAQs about Etihad pet cargo"
    ],
    schema_required: ["Article", "FAQPage", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/iata-pet-crate-guide/ (anchor: IATA crate for Etihad)",
      "/breed-restrictions/ (anchor: Etihad snub-nosed rules)",
      "/cost-of-pet-transport/ (anchor: cost calculator)",
      "/routes/uk-to-uae/ (anchor: UK to UAE route)",
      "/airlines/emirates-pet-cargo/ (anchor: Emirates via Dubai comparison)"
    ],
    external_links: [
      "Etihad Cargo Live Animals product — 2026",
      "Abu Dhabi International Airport pet handling — 2026"
    ],
    ai_overview_play: "Three-Gulf-hubs comparison (Abu Dhabi vs Dubai vs Doha) is exactly what users want."
  },

  {
    id: "d064",
    day_number: 64,
    iso_date: "2026-08-27",
    day_of_week: "Thu",
    quarter: "Q1",
    cluster_id: "routes-uk-anchored",
    cluster_name: "UK-anchored route pages",
    intent: "Commercial",
    content_type: "Route page",
    word_count_target: 2300,
    title: "Pet Transport UK to Mexico: SENASICA Rules, Costs and 2026 Timelines",
    title_tag: "UK to Mexico Pet Transport 2026 | SENASICA Rules | PetTransportGlobal",
    meta_description: "Moving a dog or cat from the UK to Mexico in 2026: SENASICA paperwork, no rabies titre needed, cargo costs to Mexico City or Cancun and timelines.",
    url_slug: "/routes/uk-to-mexico/",
    primary_seo_keyword: "pet transport uk to mexico",
    primary_volume: 60,
    primary_kd: 18,
    secondary_seo_keywords: ["dog uk to mexico", "shipping cat to mexico city", "uk to cancun pet relocation", "senasica pet import"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does SENASICA require to import a dog from the UK to Mexico in 2026, and is it really one of the easier non-EU moves?" },
      { model: "Claude", phrasing: "Why is moving a pet from the UK to Mexico in 2026 simpler than to most South American countries, despite a longer flight?" },
      { model: "Gemini", phrasing: "UK to Mexico pet import requirements 2026" },
      { model: "Grok", phrasing: "Cost to fly a dog from UK to Mexico City in 2026" }
    ],
    direct_answer_40_60_words: "Pet transport from the UK to Mexico costs around £1,800 to £3,200 in 2026 and takes around four to six weeks. SENASICA accepts UK pets without a rabies titre or quarantine. Requirements are a microchip, current rabies vaccination, treatment for external parasites within six months and a health certificate signed by an Official Veterinarian within ten days.",
    h2_outline: [
      "How much does pet transport from the UK to Mexico cost in 2026?",
      "What does SENASICA require?",
      "Why is Mexico easier than most non-EU destinations?",
      "Which airlines fly pet cargo on this route?",
      "What happens at MEX or CUN on arrival?",
      "FAQs about UK to Mexico pet transport"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA via London)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)"
    ],
    external_links: [
      "SENASICA (Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria) Mexico pet import — 2026",
      "DEFRA export health certificate — 2026"
    ],
    ai_overview_play: "Underserved route. 'No rabies titre needed' is the headline answer that wins the snippet."
  },

  {
    id: "d065",
    day_number: 65,
    iso_date: "2026-08-28",
    day_of_week: "Fri",
    quarter: "Q1",
    cluster_id: "country-guides",
    cluster_name: "Destination country guides",
    intent: "Informational",
    content_type: "Country pillar",
    word_count_target: 2700,
    title: "Importing a Pet to Brazil in 2026: MAPA Rules, VS Inspection and Realistic Costs",
    title_tag: "Pet Import Brazil 2026 | MAPA Rules | PetTransportGlobal",
    meta_description: "How to legally import a dog or cat to Brazil in 2026: MAPA permit, Veterinary Service inspection, GRU and GIG entry points and realistic costs from Europe and the US.",
    url_slug: "/countries/brazil-pet-import/",
    primary_seo_keyword: "import pet to brazil",
    primary_volume: 110,
    primary_kd: 22,
    secondary_seo_keywords: ["bring dog to brazil", "brazil pet import mapa", "shipping cat to sao paulo", "brazil vs pet inspection"],
    llm_layer_keywords: [
      { model: "ChatGPT", phrasing: "What does MAPA require to import a dog to Brazil from the UK or US in 2026, and how does the VS inspection at GRU actually work?" },
      { model: "Claude", phrasing: "Compare Brazil's pet import process with Mexico's in 2026. Both Latin American but the paperwork and inspection steps differ significantly." },
      { model: "Gemini", phrasing: "Brazil pet import requirements 2026" },
      { model: "Grok", phrasing: "Hardest part of bringing a dog to Sao Paulo in 2026" }
    ],
    direct_answer_40_60_words: "Brazil allows pet import in 2026 with a MAPA-issued International Veterinary Certificate, microchip, current rabies vaccination at least 30 days old, treatment for ecto- and endoparasites and a Veterinary Service inspection on arrival at GRU or GIG. There is no rabies titre or quarantine for accompanied pets. Costs from the UK range from £2,200 to £3,800.",
    h2_outline: [
      "Can you import a pet to Brazil in 2026?",
      "What does MAPA require?",
      "What does the VS inspection check?",
      "Which airports accept pet cargo in Brazil?",
      "What does pet import to Brazil cost?",
      "FAQs about pet import to Brazil"
    ],
    schema_required: ["Article", "FAQPage", "HowTo", "Speakable", "BreadcrumbList"],
    internal_links: [
      "/cost-of-pet-transport/ (anchor: long-haul cost calculator)",
      "/iata-pet-crate-guide/ (anchor: IATA crate sizing)",
      "/airlines/british-airways-pet-cargo/ (anchor: BA via London)",
      "/airlines/lufthansa-pet-cargo/ (anchor: Lufthansa via Frankfurt)"
    ],
    external_links: [
      "MAPA (Ministério da Agricultura, Pecuária e Abastecimento) pet import — 2026",
      "USDA APHIS Brazil pet export guidance — 2026"
    ],
    ai_overview_play: "Underserved Latin America destination with steady search volume. Closes Month 3 country-guide arc."
  }
);
