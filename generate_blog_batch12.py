"""
Blog Batch 12 - 25 new articles
Country guides, route guides, breed guides, practical guides
Run from repo root: python generate_blog_batch12.py
"""

import os

OUTPUT_DIR = "site/content/blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [

# ─── COUNTRY GUIDES ───────────────────────────────────────────────────────

{
"slug": "cambodia-pet-import-guide",
"title": "Moving to Cambodia with Pets: Import Rules for Phnom Penh-Bound Expats",
"description": "Cambodia has relaxed pet import rules compared to many Asian neighbours. No mandatory quarantine, no titre test. Here is what dogs and cats need to enter Cambodia legally.",
"date": "2026-05-09",
"tags": ["Cambodia", "pet import", "Southeast Asia"],
"faqs": [
{"q": "Does Cambodia require quarantine for imported pets?",
 "a": "Cambodia does not operate a mandatory quarantine facility for household pets. Pets arriving with complete documentation (health certificate, rabies vaccination, microchip) are inspected at Phnom Penh International Airport by the Department of Animal Health and Production and released to the owner."},
{"q": "What authority manages pet imports into Cambodia?",
 "a": "The General Directorate of Animal Health and Production (GDAHP) under the Ministry of Agriculture, Forestry and Fisheries manages live animal imports into Cambodia. For individual pet imports, inspection is conducted at Phnom Penh International Airport (PNH)."},
{"q": "Are there breed restrictions for dogs entering Cambodia?",
 "a": "Cambodia does not maintain a published list of banned dog breeds for import as of 2026. Cambodian authorities have discretionary border powers. Confirm with the Cambodian embassy if travelling with a breed classified as dangerous in other countries."}
],
"body": """## What Cambodia Requires

Cambodia is one of the more accessible Southeast Asian countries for pet relocation. No rabies titre test, no long quarantine waiting period.

**Required documentation:**
- Microchip (ISO 11784/11785 strongly recommended)
- Current rabies vaccination
- Official health certificate from an accredited vet, endorsed by your national authority (APHA for UK, USDA for USA, DAFF for Australia), issued within 14 days of travel
- Parasite treatment records (not always mandatory but recommended)

The health certificate should list all current vaccinations, the microchip number, and confirm the animal is free from clinical signs of disease.

## Arriving at Phnom Penh

Phnom Penh International Airport (PNH) is the primary port of entry. GDAHP inspectors check documentation. Processing is typically smooth with complete paperwork.

Siem Reap International Airport also handles international arrivals. Confirm live animal handling capabilities if routing through Siem Reap.

## Life with Pets in Cambodia

Rabies is present in Cambodia -- keep vaccinations current throughout your stay. Phnom Penh has expatriate-standard veterinary clinics, particularly in the BKK1 and Russian Market areas. The heat and humidity are significant; brachycephalic breeds need careful management. Tick-borne diseases are present; monthly prevention is important.

## Departing Cambodia

Export from Cambodia requires a health certificate from a GDAHP-licensed vet and an export permit. Allow 2 to 3 weeks for the process.

*Verify current GDAHP requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "zimbabwe-pet-import-guide",
"title": "Moving to Zimbabwe with Pets: DVS Permit and Import Requirements",
"description": "Zimbabwe requires an import permit, health certificate, and veterinary inspection for pet imports. Here is what expat families moving to Harare need to know about the DVS process.",
"date": "2026-05-09",
"tags": ["Zimbabwe", "pet import", "Africa"],
"faqs": [
{"q": "Do I need an import permit to bring a pet to Zimbabwe?",
 "a": "Yes. An import permit from the Department of Veterinary Services (DVS) is required before your pet enters Zimbabwe. Apply at least 4 to 6 weeks before travel."},
{"q": "What vaccinations are required for pets entering Zimbabwe?",
 "a": "Rabies vaccination is mandatory. Dogs should also have distemper, parvovirus, and leptospirosis vaccinations. Cats should have FVRCP. All vaccines must be current and recorded on the official health certificate."},
{"q": "Is there quarantine for pets arriving in Zimbabwe?",
 "a": "Zimbabwe does not operate a mandatory long-term quarantine facility for household pets. DVS inspects the animal at the port of entry. If documentation is complete, pets are typically released after a brief inspection at Robert Gabriel Mugabe International Airport."}
],
"body": """## Import Permit: First Step

Apply to the Zimbabwe Department of Veterinary Services (DVS) for an import permit before travel.

DVS contact: Cnr Borrowdale Rd and Glenara Ave, Harare | Tel: +263 4 860099

Allow 4 to 6 weeks. The permit specifies the entry point -- typically Robert Gabriel Mugabe International Airport (HRE).

## Health Documentation Required

1. Import permit (reference the permit number in the health certificate)
2. Official health certificate -- issued by an accredited vet in your country, endorsed by your national authority, issued within 14 days of travel
3. Rabies vaccination -- current
4. Core vaccinations (as above for dogs/cats)
5. Microchip (strongly recommended)
6. Parasite treatment (internal and external)

## On Arrival in Harare

DVS vets check documentation at Robert Gabriel Mugabe International Airport and may inspect the animal. Keep originals accessible.

## Life with Pets in Zimbabwe

Rabies is present in Zimbabwe -- keep vaccinations current throughout your stay. Tick-borne diseases are a significant risk; monthly tick prevention is essential. Harare has several competent private veterinary practices. The subtropical highland climate is generally comfortable for most breeds.

## Departing Zimbabwe

Export requires a health certificate from a DVS-approved vet and an export permit. Plan at least 3 weeks ahead.

*Verify current DVS requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "panama-pet-import-guide",
"title": "Moving to Panama with Pets: AUPSA Requirements and What to Expect at Tocumen",
"description": "Panama is a popular expat destination. Here is what dogs and cats need to enter Panama legally: AUPSA health certificate requirements, vaccinations, and entry at Tocumen Airport.",
"date": "2026-05-09",
"tags": ["Panama", "pet import", "Central America"],
"faqs": [
{"q": "Does Panama require quarantine for imported pets?",
 "a": "Panama does not impose mandatory quarantine for properly documented pets. AUPSA (Autoridad Panamenha de Seguridad de Alimentos) inspectors at Tocumen International Airport check documentation and inspect the animal on arrival. Pets with complete documentation are released the same day."},
{"q": "What authority manages pet imports to Panama?",
 "a": "AUPSA (Autoridad Panamenha de Seguridad de Alimentos -- Panama Food Safety Authority) manages live animal imports to Panama. AUPSA veterinary inspectors are stationed at Tocumen International Airport (PTY) to process arriving animals."},
{"q": "What vaccinations does Panama require for imported dogs?",
 "a": "Panama requires current rabies, distemper, parvovirus, adenovirus/hepatitis, and leptospirosis vaccinations for dogs. Cats require FVRCP and rabies. All vaccinations must be recorded on the official health certificate."}
],
"body": """## AUPSA Health Certificate

The health certificate is the critical document for Panama entry. It must be:
- Issued by an accredited vet in your country
- Endorsed by your national veterinary authority (USDA APHIS for USA; APHA for UK)
- Issued within 14 days of travel (check current AUPSA time window before booking)

AUPSA may require the health certificate to be in Spanish or have a certified Spanish translation. Confirm this requirement with AUPSA before travel.

AUPSA website: aupsa.gob.pa

## Required Documentation

1. AUPSA-compliant health certificate
2. Rabies vaccination -- current
3. Core vaccinations (as specified above)
4. Microchip (ISO 11784/11785 -- increasingly expected)
5. Internal and external parasite treatment within 21 days before travel

## Arriving at Tocumen

Tocumen International Airport (PTY) near Panama City is the main international entry point. AUPSA vets check documentation. Processing is generally smooth with complete paperwork.

## Living with Pets in Panama

Panama has a well-developed expatriate community, particularly in Panama City's Marbella, San Francisco, and Clayton areas. Several international-standard veterinary clinics operate in these areas. Panama's tropical climate means tick and parasite prevention is year-round. Brachycephalic breeds need careful heat management.

*Verify current AUPSA requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "uruguay-pet-import-guide",
"title": "Moving to Uruguay with Pets: MGAP Requirements for Montevideo-Bound Families",
"description": "Uruguay is one of South America's most liveable countries for expats. Here is what dogs and cats need to enter Uruguay: MGAP health certificate, vaccinations, and what happens at Carrasco Airport.",
"date": "2026-05-09",
"tags": ["Uruguay", "pet import", "South America"],
"faqs": [
{"q": "What authority manages pet imports to Uruguay?",
 "a": "MGAP (Ministerio de Ganaderia, Agricultura y Pesca -- Ministry of Agriculture) manages pet imports to Uruguay. MGAP veterinary inspectors at Montevideo Carrasco International Airport (MVD) check arriving animals."},
{"q": "Does Uruguay require quarantine for imported pets?",
 "a": "Uruguay does not impose mandatory quarantine for household pets from most countries, provided documentation is complete. MGAP inspects the animal on arrival and releases it if documentation is in order."},
{"q": "Do I need a rabies titre test to bring my pet to Uruguay?",
 "a": "Uruguay does not require a rabies titre test for pets from most countries. A current rabies vaccination and health certificate are the primary requirements. Verify current MGAP requirements for your specific country of origin before travel."}
],
"body": """## Uruguay's Pet Import Framework

Uruguay is one of South America's most accessible countries for pet relocation. The process is well-defined and typically smooth for pets with complete documentation.

## Health Documentation Required

1. Official health certificate -- issued by a government-accredited vet in your country, endorsed by your national authority
2. Rabies vaccination -- current (administered at least 30 days before travel for first-time vaccination)
3. Core vaccinations -- distemper, parvovirus, leptospirosis (dogs); FVRCP (cats)
4. Microchip (increasingly expected for documentation linkage)
5. Internal and external parasite treatment within 15 days before travel

The health certificate should be in Spanish or include a certified Spanish translation. Confirm with MGAP.

## Arriving at Carrasco Airport (MVD)

MGAP vets at Montevideo Carrasco International Airport process arriving animals. Keep originals accessible. Processing is typically efficient.

MGAP contact: mgap.gub.uy

## Life with Pets in Montevideo

Uruguay is a genuinely good country for pets. Montevideo has several good private veterinary practices. The temperate climate suits most breeds. Uruguay has a culture of dog ownership; parks and open spaces are accessible. Leash laws apply in public areas.

*Verify current MGAP requirements at mgap.gub.uy before travel. Information accurate as of May 2026.*
"""},

{
"slug": "bolivia-pet-import-guide",
"title": "Moving to Bolivia with Pets: SENASAG Requirements and Altitude Considerations",
"description": "Bolivia is home to a growing expat community in La Paz and Santa Cruz. Here is what dogs and cats need to enter Bolivia legally, including SENASAG health certificate requirements and high-altitude health notes.",
"date": "2026-05-09",
"tags": ["Bolivia", "pet import", "South America"],
"faqs": [
{"q": "What authority manages pet imports to Bolivia?",
 "a": "SENASAG (Servicio Nacional de Sanidad Agropecuaria e Inocuidad Alimentaria) manages animal health and pet imports in Bolivia. SENASAG vets inspect arriving animals at the main international airports."},
{"q": "What does Bolivia require for importing a dog?",
 "a": "Bolivia requires a current rabies vaccination, core vaccinations (distemper, parvovirus, leptospirosis), parasite treatment, and an official health certificate from your country endorsed by your national veterinary authority. A microchip is strongly recommended."},
{"q": "Is altitude a concern when moving a pet to La Paz?",
 "a": "La Paz sits at approximately 3,600 metres above sea level. Pets can adapt to altitude but the transition takes time. Brachycephalic breeds (flat-faced dogs and cats) face higher respiratory risk at altitude and should be assessed by a vet before the move. Healthy, non-brachycephalic dogs and cats generally adapt within 1 to 2 weeks. Arrive during a calm period and allow your pet to rest initially."}
],
"body": """## SENASAG Health Documentation

The health certificate must be:
- Issued by an accredited vet in your country
- Endorsed by your national veterinary authority (USDA for USA; APHA for UK)
- Issued within 14 days of travel
- Accompanied by a Spanish translation or bilingual version (confirm with SENASAG)

SENASAG website: senasag.gob.bo

## Required Documentation

1. Health certificate (endorsed by national authority)
2. Rabies vaccination -- current
3. Core vaccinations (distemper, parvovirus, leptospirosis for dogs; FVRCP for cats)
4. Microchip (recommended)
5. Parasite treatment records

## Entry Points

El Alto International Airport (LPB) serves La Paz and is at 4,061 metres altitude -- one of the highest commercial airports in the world. Viru Viru International Airport (VVI) serves Santa Cruz de la Sierra, which sits at a much lower 416 metres and is an easier altitude for arriving pets.

If your destination is La Paz, consider the altitude transition. A vet check before travel is sensible.

## Altitude Advice

**General dogs and cats:** Most adapt to La Paz within 1 to 2 weeks. Keep exercise gentle initially and watch for lethargy, loss of appetite, or difficulty breathing.

**Brachycephalic breeds:** Flat-faced dogs (Bulldogs, Pugs, French Bulldogs) and cats (Persians, Exotics) are at elevated risk at altitude. Consult your vet before committing to a high-altitude move with a brachycephalic pet.

**Senior pets:** Older animals with cardiac or respiratory conditions should be assessed for altitude suitability before the move.

*Verify current SENASAG requirements at senasag.gob.bo before travel. Information accurate as of May 2026.*
"""},

{
"slug": "senegal-pet-import-guide",
"title": "Moving to Senegal with Pets: DIREL Requirements for Dakar-Bound Expats",
"description": "Senegal is West Africa's most prominent diplomatic and business hub. Here is what dogs and cats need to enter Senegal: DIREL health certificate, vaccinations, and arrival at Blaise Diagne Airport.",
"date": "2026-05-09",
"tags": ["Senegal", "pet import", "West Africa"],
"faqs": [
{"q": "What authority manages pet imports to Senegal?",
 "a": "DIREL (Direction de l'Elevage -- Livestock Directorate) under the Ministry of Agriculture manages animal imports in Senegal. DIREL vets inspect arriving animals at Blaise Diagne International Airport (DSS)."},
{"q": "Does Senegal require quarantine for imported pets?",
 "a": "Senegal does not impose mandatory quarantine for household pets from most countries. DIREL inspects the animal on arrival. If documentation is complete, pets are typically released the same day."},
{"q": "What vaccinations are required for dogs entering Senegal?",
 "a": "Rabies vaccination is mandatory. Dogs should also have current distemper, parvovirus, hepatitis, and leptospirosis vaccinations. All must be recorded on the official health certificate. Cats require FVRCP and rabies."}
],
"body": """## Dakar as an Expat Hub

Senegal has long been home to diplomatic missions, NGOs, business operations, and a growing expatriate community. Dakar is the access point for much of West Africa's international activity. Pet imports are managed by DIREL.

## Health Documentation

DIREL requires:
1. Official health certificate -- issued by an accredited vet, endorsed by your national authority (USDA for USA; APHA for UK)
2. Rabies vaccination -- current
3. Core vaccinations (as above)
4. Microchip (increasingly expected)
5. Parasite treatment records

The health certificate should ideally include a French translation given Senegal's official language. Confirm with DIREL whether an English certificate is accepted or whether French translation is required.

## Arriving at Blaise Diagne Airport (DSS)

Blaise Diagne International Airport (DSS) opened in 2017 and replaced the old Dakar-Yoff airport. Most international flights now use DSS. DIREL vets check documentation at the airport.

## Life with Pets in Dakar

Dakar has a reasonable veterinary infrastructure by West African standards. Several clinics operate in the Almadies, Mermoz, and Plateau areas. The climate is hot and dry (Harmattan season) or hot and humid (rainy season). Tick and parasite prevention is year-round. Rabies is present in Senegal; keep vaccinations current.

*Verify current DIREL requirements before travel. Information accurate as of May 2026.*
"""},

# ─── ROUTE GUIDES ─────────────────────────────────────────────────────────

{
"slug": "usa-to-germany-pet-transport-guide",
"title": "Pet Transport from the USA to Germany: EU Entry for American Pets",
"description": "Moving from the USA to Germany with a dog or cat? The USA is an approved EU third country. Here is the full process: microchip, AHC endorsed by USDA APHIS, and tapeworm treatment for dogs.",
"date": "2026-05-09",
"tags": ["USA to Germany", "pet transport", "EU pet import"],
"faqs": [
{"q": "Does the USA qualify for simplified EU pet travel?",
 "a": "Yes. The USA is on the EU's approved third country list under Regulation 576/2013. Dogs and cats from the USA can enter EU member states including Germany without a rabies titre test. You need a microchip, current rabies vaccination (at least 21 days old), and an EU Animal Health Certificate (AHC) endorsed by USDA APHIS."},
{"q": "What is the best airport to use when flying a pet from the USA to Germany?",
 "a": "Frankfurt Airport (FRA) is the most commonly used entry point for pets to Germany. It has established live animal facilities and is one of Europe's largest cargo hubs. Munich (MUC) and Dusseldorf (DUS) also handle international live animal arrivals but Frankfurt is the best-served option."},
{"q": "Do dogs entering Germany from the USA need tapeworm treatment?",
 "a": "Yes. Dogs entering the EU (including Germany) from any non-EU country require tapeworm treatment (praziquantel) administered by a vet 1 to 5 days before arriving in the EU. The treatment date and product must be recorded in the AHC."}
],
"body": """## USA Status Under EU Rules

The USA is listed as a Part 1 third country under EU Regulation 576/2013. This means no titre test is required, which is a significant advantage compared to moving from the USA to Australia or Japan.

## What Your Pet Needs

1. **Microchip** -- ISO 11784/11785 15-digit chip. Many US dogs have 10-digit chips. Add a compliant ISO chip if your dog has a legacy chip.
2. **Rabies vaccination** -- current, at least 21 days before EU entry if it is the first vaccination ever; booster within validity for existing vaccinations
3. **Animal Health Certificate (AHC)** -- issued by a USDA-accredited vet on the EU-approved template, endorsed by USDA APHIS, issued within 10 days of EU arrival
4. **Tapeworm treatment** (dogs only) -- administered 1 to 5 days before arrival in Germany by a vet

## Getting the AHC in the USA

Find a USDA-accredited vet at aphis.usda.gov/pet-travel. After your vet prepares the AHC, submit to USDA APHIS for endorsement. Allow 2 to 5 business days. Expedited USDA endorsement is available.

## Flight Options to Germany

Direct routes:
- **Lufthansa** from major US hubs to Frankfurt, Munich, Dusseldorf (accepts pets in cabin and hold on many routes)
- **United Airlines** from Newark, Washington to Frankfurt
- **American Airlines** to Frankfurt
- **Condor** from US East Coast cities to Frankfurt

## After Arrival in Germany

Dogs must be registered with the local Einwohnermeldeamt. Hundesteuer (dog tax) applies in Germany -- rates vary significantly by municipality. Register within 4 weeks of arrival.

*Verify current USDA APHIS and EU entry requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "usa-to-france-pet-transport-guide",
"title": "Pet Transport from the USA to France: AHC Requirements and Paris Entry",
"description": "Moving from the USA to France with a pet? France follows EU pet travel rules. Here is the full process: USDA-endorsed AHC, microchip, tapeworm treatment, and arriving at Charles de Gaulle.",
"date": "2026-05-09",
"tags": ["USA to France", "pet transport", "France pet import"],
"faqs": [
{"q": "Can I bring my pet from the USA to France without a titre test?",
 "a": "Yes. The USA is on the EU's approved third country list. Pets from the USA do not need a rabies titre test to enter France (EU). You need a microchip, current rabies vaccination (at least 21 days old if first-time), and an EU Animal Health Certificate endorsed by USDA APHIS."},
{"q": "What airport is best for bringing a pet into France from the USA?",
 "a": "Paris Charles de Gaulle Airport (CDG) is the primary port of entry for live animal cargo arriving from the USA. CDG has dedicated live animal handling facilities. Lyon Saint-Exupery and Marseille Provence also handle international live animal arrivals but CDG is the main hub."},
{"q": "How do I get a health certificate endorsed for France from the USA?",
 "a": "Your vet must be USDA-accredited. They complete the EU Animal Health Certificate (AHC). You then submit the certificate to USDA APHIS for endorsement. Allow 2 to 5 business days. The endorsed AHC must be issued within 10 days of your pet arriving in France."}
],
"body": """## France as an EU Member State

France follows EU Regulation 576/2013 for pet imports from third countries. Since the USA is a listed approved country, the process is significantly simpler than moves to Australia or Japan.

## What Your Pet Needs

1. **Microchip** -- ISO 11784/11785. Add a compliant 15-digit chip if your dog or cat has an older 10-digit US chip.
2. **Rabies vaccination** -- current. First-ever vaccination must be at least 21 days before EU entry. Boosters within validity do not need the 21-day wait.
3. **EU Animal Health Certificate** -- prepared by a USDA-accredited vet, endorsed by USDA APHIS, issued within 10 days of arrival in France
4. **Tapeworm treatment** (dogs only) -- praziquantel, administered 1 to 5 days before arrival, recorded in the AHC

## USDA APHIS Endorsement

Find USDA-accredited vets at aphis.usda.gov/pet-travel. After the vet prepares the AHC:
- Submit to USDA APHIS state office for endorsement
- Allow 2 to 5 business days (expedited service available)
- Keep endorsed original safe -- this is your travel document

## Airlines from the USA to France

- **Air France** -- accepts pets in cabin (small) and hold on transatlantic routes
- **Delta Air Lines** -- restricted transatlantic pet cargo; check current policy
- **American Airlines** -- hold cargo to Paris
- **La Compagnie** -- premium carrier with more flexible pet policies

## After Arrival in France

France has an EU Pet Passport system. You can obtain a French EU Pet Passport from a registered vet after arrival. This makes future travel within the EU and to listed third countries easier. The passport links vaccination records, microchip, and titres (if applicable).

*Verify current USDA and EU requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "australia-to-germany-pet-transport-guide",
"title": "Pet Transport from Australia to Germany: What Australian Pets Need for EU Entry",
"description": "Moving from Australia to Germany? Australia is on the EU's approved list. Here is what Australian pets need for German entry: microchip, AHC endorsed by DAFF, tapeworm treatment, and flight options.",
"date": "2026-05-09",
"tags": ["Australia to Germany", "pet transport", "EU pet import"],
"faqs": [
{"q": "Does Australia qualify for EU pet travel without a titre test?",
 "a": "Yes. Australia is a listed approved country under EU Regulation 576/2013 (Part 1). Australian dogs and cats can enter Germany and other EU member states without a rabies titre test. You need a microchip, current rabies vaccination (21 days old if first vaccination), and an EU AHC endorsed by the Australian Department of Agriculture (DAFF)."},
{"q": "How is the health certificate prepared for an Australian pet going to Germany?",
 "a": "Your vet in Australia prepares the EU Animal Health Certificate. The completed AHC must be endorsed by the Australian Department of Agriculture (DAFF). You can arrange DAFF endorsement through their export certification service at agriculture.gov.au. The endorsed AHC must be issued within 10 days of your pet arriving in the EU."},
{"q": "What is the best routing for flying a pet from Australia to Germany?",
 "a": "There are no direct flights from Australia to Germany. Common routes involve connecting through Singapore (SIN), Dubai (DXB), or Doha (DOH). Check with Lufthansa, Singapore Airlines, or Emirates for live animal cargo acceptance on each leg. The pet travels as cargo throughout."}
],
"body": """## Australia's EU Status

Australia is a listed Part 1 country under EU Regulation 576/2013, which means Australian pets do not need a titre test to enter Germany. This is a significant advantage -- getting a titre test done in Australia and waiting 180 days is not necessary for the EU.

## What Your Australian Pet Needs

1. **Microchip** -- ISO 11784/11785 (standard Australian chips comply)
2. **Rabies vaccination** -- current. First-ever vaccine must be at least 21 days before EU arrival.
3. **EU Animal Health Certificate (AHC)** -- issued by an Australian government-accredited vet on the EU template, endorsed by DAFF, issued within 10 days of EU arrival
4. **Tapeworm treatment** (dogs only) -- praziquantel, 1 to 5 days before EU arrival, recorded in the AHC

## DAFF AHC Endorsement

DAFF issues export health certificates for pets leaving Australia. Process at agriculture.gov.au. Allow 3 to 5 business days. The vet who prepares the AHC must be DAFF-registered.

## Routing Options

Australia to Germany requires at least one transit. Common routes:
- **Sydney or Melbourne via Singapore (SIN) to Frankfurt** -- Singapore Airlines or Qantas to Singapore, then Lufthansa or Singapore Airlines to Frankfurt
- **Via Dubai (DXB)** -- Qantas or Emirates to Dubai, then Lufthansa or Emirates to Frankfurt
- **Via Doha (DOH)** -- Qantas via Doha, then Qatar Airways or Lufthansa to Frankfurt

Each airline and each leg must accept live animal cargo. Confirm on the specific dates and aircraft types for your route.

## German Registration After Arrival

Register your dog with the local Einwohnermeldeamt (residence registration office). Hundesteuer applies. Register within 4 weeks of establishing residence.

*Verify current DAFF and EU entry requirements at agriculture.gov.au and your destination EU member state's authority. Information accurate as of May 2026.*
"""},

{
"slug": "ireland-to-uk-pet-transport-guide",
"title": "Pet Transport from Ireland to the UK: Post-Brexit Rules for Irish Pet Owners",
"description": "Moving from Ireland to Great Britain with a pet? Post-Brexit, GB has changed from EU rules. Here is what Irish pet owners need: AHC from a listed vet, tapeworm treatment, and what happens at the port.",
"date": "2026-05-09",
"tags": ["Ireland to UK", "pet transport", "Brexit pet travel"],
"faqs": [
{"q": "Can I still use my EU Pet Passport to travel from Ireland to Great Britain after Brexit?",
 "a": "No. EU Pet Passports are no longer accepted for entry into Great Britain (England, Scotland, Wales) after Brexit. You need a Great Britain Animal Health Certificate (GB AHC) issued by an Irish government-authorised vet within 10 days of travel. Note: travel from Ireland to Northern Ireland (part of the UK) follows different rules and EU passports remain accepted under the Windsor Framework."},
{"q": "What does a dog from Ireland need to enter Great Britain?",
 "a": "Dogs travelling from Ireland to Great Britain need: a microchip, current rabies vaccination (at least 21 days old), tapeworm treatment administered by a vet 1 to 5 days before UK arrival, and a GB AHC issued by an Irish government-authorised vet within 10 days of travel."},
{"q": "Which routes from Ireland to Great Britain accept pets?",
 "a": "Pets travel to Great Britain by sea (ferry) or by air. Approved ferry routes include Dublin to Holyhead and Rosslare to Pembroke. Irish Ferries and Stena Line operate these routes and accept pets in vehicles or designated pet areas. By air, pets travel as cargo on specific flights. Many passenger ferry routes allow pets in cars on board."}
],
"body": """## The Brexit Change for Irish Pet Owners

Before Brexit, Ireland and the UK were both EU members. Travel between them (including pets) used EU Pet Passports. Since 1 January 2021, Great Britain (England, Scotland, Wales) left the EU pet travel system. The change affects Irish pet owners travelling to the British mainland.

**Northern Ireland is different:** Travel from Ireland to Northern Ireland still falls under the Windsor Framework, which means EU rules continue to apply. EU Pet Passports are accepted for Ireland-to-Northern-Ireland travel.

## What Your Pet Needs for Great Britain

1. **Microchip** -- ISO 11784/11785
2. **Rabies vaccination** -- current, at least 21 days old
3. **Tapeworm treatment** (dogs) -- administered by a vet 1 to 5 days before arrival in Great Britain, recorded in the AHC
4. **GB Animal Health Certificate (GB AHC)** -- issued by an Irish government-authorised vet within 10 days of travel

## GB AHC: Who Issues It

Only government-authorised vets (OVs -- Official Veterinarians in Irish terminology) can issue the GB AHC. Your regular vet may or may not be an OV. Contact Department of Agriculture, Food and the Marine (DAFM) or check veterinary practices in your area -- many general practices have vets who can issue the AHC.

DAFM website: gov.ie/agriculture

## Ferry Travel from Ireland to Great Britain

Most Irish pet owners take their pets by ferry. Approved approved points of entry for pets include:
- Dublin Port to Holyhead (Ireland to Wales)
- Rosslare Europort to Pembroke (Ireland to Wales)

**Irish Ferries** and **Stena Line** both operate these routes and accept pets. Pets typically stay in the vehicle on the car deck (for short crossings) or in dedicated pet areas on overnight sailings.

Bring the GB AHC and keep it accessible at the border.

*Verify current DAFM and UK government requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "canada-to-france-pet-transport-guide",
"title": "Pet Transport from Canada to France: EU Entry for Canadian Pets",
"description": "Moving from Canada to France with a pet? Canada is an approved EU third country. Here is the full process: CFIA-endorsed AHC, microchip, and what to expect at Charles de Gaulle on arrival.",
"date": "2026-05-09",
"tags": ["Canada to France", "pet transport", "EU pet import"],
"faqs": [
{"q": "Does Canada qualify for EU pet travel without a titre test?",
 "a": "Yes. Canada is listed as an approved third country under EU Regulation 576/2013. Canadian dogs and cats can enter France and other EU member states without a rabies titre test. You need a microchip, current rabies vaccination (at least 21 days old if first vaccination), and a CFIA-endorsed EU Animal Health Certificate."},
{"q": "How do I get a health certificate for my Canadian pet to enter France?",
 "a": "A Canadian Accredited Veterinarian (CV) or registered vet prepares the EU Animal Health Certificate. The CFIA (Canadian Food Inspection Agency) endorses the certificate. Allow 3 to 7 business days for CFIA endorsement. The endorsed certificate must be issued within 10 days of your pet arriving in France."},
{"q": "What airlines fly pets as cargo from Canada to France?",
 "a": "Air Canada and Air France both operate direct routes between Canada and France (Toronto-Paris and Montreal-Paris primarily). Both airlines accept pets as cargo on these routes. Air Canada also accepts small pets in cabin on certain routes -- confirm weight limits and aircraft type for your specific flight."}
],
"body": """## Canada's EU Pet Travel Status

Canada is a listed Part 1 country under EU Regulation 576/2013. This means the process for Canadian pets entering France is relatively straightforward -- no titre test, no extended waiting period.

## What Your Canadian Pet Needs

1. **Microchip** -- ISO 11784/11785. Standard Canadian chips are typically compliant.
2. **Rabies vaccination** -- current. First-ever vaccination must be at least 21 days before EU arrival.
3. **EU Animal Health Certificate** -- prepared by a Canadian Accredited Veterinarian (CV), endorsed by CFIA, issued within 10 days of arrival in France
4. **Tapeworm treatment** (dogs only) -- praziquantel, 1 to 5 days before EU arrival, recorded in the AHC

## CFIA Endorsement

CFIA endorses the AHC at their regional offices. Contact information and process at inspection.canada.ca. Allow 3 to 7 business days. Expedited service may be available; contact CFIA directly.

## Flight Routes Canada to France

- **Air France** -- Montreal (YUL) and Toronto (YYZ) to Paris CDG direct. Accepts pets as hold cargo on many transatlantic routes.
- **Air Canada** -- Montreal and Toronto to Paris CDG direct. Accepts pets in hold and small pets in cabin on certain routes.

Air Canada's cabin pet policy for transatlantic routes changes periodically -- confirm before booking.

## Practical Points

The timing pressure for the AHC (issued within 10 days of arrival) means your vet appointment and CFIA endorsement must happen in the week before travel. Plan this carefully around your departure date.

After arriving in France, you can obtain a French EU Pet Passport from a registered vet. This makes future EU travel and travel to listed countries easier.

*Verify current CFIA and EU requirements at inspection.canada.ca before travel. Information accurate as of May 2026.*
"""},

# ─── BREED GUIDES ─────────────────────────────────────────────────────────

{
"slug": "travelling-with-a-ragdoll-cat-internationally",
"title": "Moving Internationally with a Ragdoll Cat: Size, Temperament, and Practical Advice",
"description": "Ragdoll cats are large, placid, and generally good travellers. Here is what Ragdoll owners need to know for international relocation, including cabin weight limits and crate sizing.",
"date": "2026-05-09",
"tags": ["Ragdoll cat", "cat travel", "large cat international travel"],
"faqs": [
{"q": "Can a Ragdoll cat travel in the aircraft cabin?",
 "a": "Adult Ragdolls typically weigh 5 to 9 kg. Most airlines set a combined weight limit of 6 to 8 kg (pet plus carrier) for cabin travel. Small or young Ragdolls may qualify for cabin travel; large adults often exceed the limit and must travel in the hold. Weigh your cat and carrier before the trip and confirm with your specific airline."},
{"q": "Are Ragdoll cats restricted or banned by any countries?",
 "a": "No. Ragdoll cats are not on any country's restricted or banned breed list. Normal cat import requirements apply: microchip, rabies vaccination, health certificate."},
{"q": "Are Ragdolls good travellers?",
 "a": "Ragdolls are known for their calm, relaxed temperament. They tend to be less reactive to stress than more high-strung breeds. However, all cats vary individually, and a Ragdoll that has never experienced confinement in a carrier will still need crate training before a long international move."}
],
"body": """## The Size Question

Adult Ragdolls typically weigh:
- Females: 4.5 to 7 kg
- Males: 6 to 9 kg

Add a carrier at 0.8 to 1.5 kg and you get a combined weight of:
- Average female: 5.3 to 8.5 kg
- Average male: 6.8 to 10.5 kg

Most airlines cap cabin pets at 6 to 8 kg combined. Many adult Ragdolls -- especially males -- will exceed this and need to travel in the hold.

## Cabin Options for Lighter Ragdolls

If your Ragdoll just qualifies for cabin, use the lightest suitable soft-sided carrier you can find. Ultra-light mesh carriers weigh under 0.8 kg and can make the difference between qualifying and not. Check that your carrier still meets the airline's structural requirements.

## Hold Travel for Ragdolls

Ragdolls generally handle hold travel reasonably well given their calm temperament. Key points:

**Crate training:** Build months of positive association before travel. The crate should be a genuine comfort zone, not just a stress container.

**Crate size:** Use a crate larger than the IATA minimum. Ragdolls are long-bodied cats -- space to stretch out matters.

**Temperature:** Avoid summer travel to Middle Eastern, South Asian, or tropical destinations. Ragdolls have semi-long coats.

## Not Brachycephalic

Ragdolls are not flat-faced. They do not face the respiratory restrictions that apply to Persian or Exotic Shorthair cats. Airline breed restrictions for brachycephalic cats do not apply to Ragdolls.

## Country Requirements

No country restricts Ragdoll cats by breed. Standard cat import requirements apply:
- Microchip
- Rabies vaccination (if required by destination)
- Health certificate

*Check airline weight policies before booking. Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-siamese-cat-internationally",
"title": "Moving Internationally with a Siamese Cat: Vocal Breed, Smart Packing Advice",
"description": "Siamese cats are vocal, sensitive, and form strong bonds. Here is what Siamese owners need for international moves, including cabin travel tips and how to manage their temperament during travel.",
"date": "2026-05-09",
"tags": ["Siamese cat", "cat travel", "sensitive breed travel"],
"faqs": [
{"q": "Are Siamese cats restricted from flying on any airlines?",
 "a": "No. Siamese cats are not brachycephalic and are not on any airline's restricted breed list. They face the same airline policies as any domestic cat. Adult Siamese (3 to 5 kg typically) usually fit within cabin weight limits."},
{"q": "Do Siamese cats handle travel well?",
 "a": "Siamese are known for being vocal and emotionally sensitive to change. They tend to be more expressive of stress than many breeds. With proper crate training and familiar scents in the carrier, most Siamese cats travel adequately. Cabin travel is generally less distressing for them than hold travel."},
{"q": "Are Siamese cats restricted in any country?",
 "a": "No. Siamese cats are not restricted by any country's import regulations. Standard cat import requirements apply."}
],
"body": """## The Temperament Factor

Siamese are among the most vocal and emotionally expressive cats. They form strong owner bonds and are sensitive to environmental change. During travel:
- They may vocalise persistently in the carrier at the airport
- Hold travel separates them from you -- harder on this breed than more independent cats
- In cabin, most Siamese settle once the aircraft reaches cruise altitude

## Cabin vs Hold

For a Siamese, **cabin is strongly preferred** where possible. Hearing your voice and sensing your presence reduces stress significantly.

Most adult Siamese (3 to 5 kg) fall within cabin weight limits. Add a standard carrier (0.8 to 1.5 kg) for a combined weight of 3.8 to 6.5 kg -- typically within the 6 to 8 kg limit most airlines set.

## Crate Training a Siamese

Start months before travel. The goal is a carrier the cat genuinely wants to be in.

For a Siamese specifically:
- Put a piece of your worn clothing in the carrier (familiar scent is powerful for this breed)
- Feed meals in the carrier with the door open
- Build up to extended closed-door periods gradually
- Practice the carrier being picked up and moved around

A Siamese that finds the carrier a comfortable, owner-scented space handles travel dramatically better.

## Country Requirements

No country restricts Siamese cats. Standard requirements apply:
- Microchip
- Rabies vaccination
- Health certificate appropriate to the destination

*Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-doberman-internationally",
"title": "Moving Internationally with a Doberman: Breed Restrictions and Travel Considerations",
"description": "Dobermans face breed-specific legislation in several countries. Here is what Doberman owners need to know before planning an international move, including country-by-country restriction status.",
"date": "2026-05-09",
"tags": ["Doberman", "breed restrictions", "restricted breed travel"],
"faqs": [
{"q": "Is the Doberman a restricted breed for international travel?",
 "a": "Dobermans are restricted or subject to additional requirements in several countries. Portugal classifies Dobermans as dangerous dogs. Some German states and Swiss cantons have additional registration requirements. Always verify the specific regulations of your destination city and country before planning a move."},
{"q": "Can Dobermans travel as air cargo?",
 "a": "Yes. Dobermans are not brachycephalic, so they do not face the breed-based restrictions that apply to flat-faced dogs. Most airlines that accept large dogs in cargo accept Dobermans. Adult Dobermans (32 to 45 kg) require a cargo crate of approximately 100 x 70 x 82 cm."},
{"q": "What is the process for importing a Doberman to Australia?",
 "a": "Standard process applies. Dobermans are not a restricted breed for Australian import. Microchip, two correctly-timed rabies vaccinations, FAVN titre test (0.5 IU/mL minimum, drawn at least 30 days after final vaccine), 180-day wait from blood draw date, DAFF import permit, and 10-day quarantine at Mickleham."}
],
"body": """## Breed Restrictions: Country by Country

The regulatory picture for Dobermans varies. As of May 2026:

**No Doberman-specific restrictions:**
- UK, USA (federal level), Australia, New Zealand, most of Scandinavia, France, Netherlands

**Restrictions or additional requirements:**
- **Portugal**: Dobermans classified as dangerous dogs. Import allowed but requires special registration, mandatory muzzle/leash in public, owner competency documentation.
- **Some German states (Lander)**: Several states have historically listed Dobermans under dangerous dog regulations. The situation has relaxed in several states. Check the specific Bundesland you are moving to.
- **Some Swiss cantons**: Requirements vary by canton. Research your specific destination.

Always verify at national and municipal level, not just national.

## Flying a Doberman

Dobermans are not brachycephalic -- no airline breed restrictions apply. Adult Dobermans typically need:
- Crate: approximately 100 x 70 x 82 cm
- Combined weight (dog plus crate): 50 to 65 kg typically
- Hold travel only (well above cabin weight limits)

## Cardiac Health Check

Dobermans have an elevated prevalence of dilated cardiomyopathy (DCM). Before any international flight, have your vet assess cardiac function. This is not a legal requirement but is sensible given the breed's cardiac profile.

## Australia and New Zealand

No breed restriction applies. Standard process: titre test, 180-day wait, quarantine. (See our UK-to-Australia or USA-to-Australia guides for the full sequence.)

*Always verify breed restrictions directly with the destination country before planning a move. Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-great-dane-internationally",
"title": "Moving Internationally with a Great Dane: Giant Breed Relocation Guide",
"description": "Great Danes are one of the world's largest dog breeds. Here is everything owners need to know about airlines, crate sizing, aircraft hold dimensions, and country rules for international moves.",
"date": "2026-05-09",
"tags": ["Great Dane", "large dog travel", "giant breed relocation"],
"faqs": [
{"q": "Can a Great Dane fly in an aircraft cargo hold?",
 "a": "Yes, but the crate must fit through the cargo door and within the hold of the specific aircraft. A Great Dane typically requires a crate at least 100 to 120 cm long, 75 to 90 cm wide, and 90 to 110 cm tall. Confirm the crate dimensions fit the specific aircraft type operating your route before booking."},
{"q": "Is a Great Dane restricted or banned in any country?",
 "a": "Great Danes are not on most countries' restricted breed lists. Some municipalities in Germany and a few European jurisdictions have registration requirements for large dogs, but these are local regulations, not import bans. Import documentation requirements are the same as for any other breed."},
{"q": "Which airlines handle very large dog crates?",
 "a": "Airlines with strong large animal cargo capabilities include Lufthansa Cargo, British Airways World Cargo, Cathay Pacific Cargo, and Emirates SkyCargo. Contact the cargo division of each airline directly -- not the passenger desk. State the exact crate dimensions and get written confirmation that the crate will fit the aircraft on your specific route."}
],
"body": """## The Size Challenge

Everything about moving a Great Dane internationally centres on size:
- **The crate** must allow the dog to stand at full height, turn around, and lie down. Great Dane crates are typically 110+ cm long and 90+ cm tall.
- **The aircraft hold door** must be large enough for the crate to fit through.
- **The combined weight** (dog plus crate) is typically 80 to 120 kg -- expensive to fly.

## Before Booking: Confirm Aircraft Compatibility

Call the airline cargo department before booking any flight:
1. State exact crate dimensions
2. Confirm the dimensions fit through the cargo door of the aircraft type on your specific route
3. Get written confirmation

Wide-body aircraft (Boeing 777, 787, 747; Airbus A330, A380) generally handle larger crates than narrow-body aircraft. The same route may use different aircraft on different dates -- confirm for your specific travel date.

## Crate Training

For a dog this size, crate training is not optional. A distressed Great Dane attempting to escape a large crate during a 10-hour flight creates dangerous situations. Months of positive crate training -- the crate as a genuine sleeping and resting spot -- are essential.

## Health Considerations

Great Danes are prone to:
- **Dilated cardiomyopathy (DCM)** -- cardiac function assessment before international flight is sensible
- **Bloat/GDV** -- do not feed a large meal within 6 hours of travel
- **Joint issues** -- adequate padding in the crate for long flights

## Country Requirements

Great Danes are not banned by any country's import regulations. Standard requirements (microchip, rabies vaccination, health certificate; titre test and quarantine for AU/NZ/Japan) apply.

*Verify airline cargo dimensions and capacity for your specific route before booking. Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-bichon-frise-internationally",
"title": "Moving Internationally with a Bichon Frise: Cabin Eligibility and Country Rules",
"description": "Bichon Frises are small, cheerful dogs that usually qualify for cabin travel. Here is what Bichon owners need for international moves, including cabin weight limits, grooming notes, and country rules.",
"date": "2026-05-09",
"tags": ["Bichon Frise", "small dog travel", "cabin travel dogs"],
"faqs": [
{"q": "Can a Bichon Frise travel in the aircraft cabin?",
 "a": "Yes. Adult Bichon Frises typically weigh 3 to 5 kg. Add a standard soft-sided carrier (0.8 to 1.5 kg) for a combined weight of 3.8 to 6.5 kg -- within the 6 to 8 kg limit set by most airlines for cabin pets. Bichons are one of the breeds most reliably suited to cabin travel."},
{"q": "Are Bichon Frises restricted in any country?",
 "a": "No. Bichon Frises are not on any country's restricted breed list. They are also not brachycephalic to a clinically significant degree -- they do not face the flat-faced dog restrictions of French Bulldogs or Pugs. Standard dog import requirements apply."},
{"q": "How do Bichon Frises handle long-haul travel?",
 "a": "Bichon Frises are generally adaptable dogs. They do well in cabin travel on most flights. For very long hauls (12+ hours), their small size means they fit under the seat comfortably. With pre-travel crate training and familiar toys in the carrier, most Bichons handle long-haul cabin travel reasonably well."}
],
"body": """## Cabin Travel: Bichons Are Well-Suited

The Bichon Frise is almost ideal for cabin travel in terms of size:
- Adult weight: 3 to 5 kg
- Add carrier: 3.8 to 6.5 kg combined
- Most airline limits: 6 to 8 kg combined

The Bichon's calm, sociable temperament also works in its favour for the airport environment.

## Airlines and Policies

Confirm with your specific airline:
- Cabin pet weight limit (the combined pet-plus-carrier weight is what is measured)
- Carrier dimensions (under-seat carrier must fit in the under-seat space of your aircraft)
- Number of cabin pets per flight (some airlines limit to 2 to 3 cabin pets per cabin)

Airlines change policies -- always confirm directly and get written confirmation.

## Long-Haul Travel Tips

For flights over 8 hours:
- Line the carrier with an absorbent pad and bring spares
- Bring a small amount of food and water accessible on your lap during the flight
- A small familiar toy or blanket reduces stress
- Book a window or aisle seat to keep the carrier under the seat in front

## Grooming Before Travel

Bichons have a dense, curly coat that can mat under the stress and confined conditions of travel. A tidy trim 2 to 3 weeks before travel -- not right before, which can leave the skin temporarily sensitive -- reduces grooming issues during and after the journey.

## Country Requirements

No country restricts Bichon Frises. Standard requirements apply:
- Microchip
- Rabies vaccination
- Health certificate appropriate to the destination

*Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-maltese-internationally",
"title": "Moving Internationally with a Maltese: Tiny Dog, Cabin Travel Tips and Country Rules",
"description": "Maltese are tiny dogs that almost always qualify for cabin travel. Here is what Maltese owners need for international moves, from cabin requirements to health certificate timing.",
"date": "2026-05-09",
"tags": ["Maltese dog", "small dog travel", "cabin pet travel"],
"faqs": [
{"q": "Do Maltese dogs qualify for cabin travel on airlines?",
 "a": "Yes, easily. Adult Maltese typically weigh 2 to 3.5 kg. Add a carrier at 0.8 to 1.5 kg for a combined weight of 2.8 to 5 kg -- well within the 6 to 8 kg cabin limit set by most airlines. The Maltese is one of the smallest breeds and almost always qualifies for cabin travel on most airlines."},
{"q": "Are Maltese dogs restricted in any country?",
 "a": "No. Maltese are not on any country's restricted breed list. They are also not brachycephalic to a clinically significant degree. Standard dog import requirements apply everywhere."},
{"q": "How do Maltese dogs handle international travel?",
 "a": "Maltese are companion dogs that bond closely with their owners. They handle cabin travel well because they can sense and hear their owner. They may be anxious in novel environments, but with pre-travel crate training and familiar scents, most cope well."}
],
"body": """## Cabin Travel for a Maltese

The Maltese is among the smallest of all dog breeds. At 2 to 3.5 kg, they fall well within cabin weight limits for virtually every airline. The main practical considerations are:

**Carrier choice:** Use a soft-sided carrier that fits under the aircraft seat. Standard under-seat dimensions are approximately 45 x 35 x 20 cm -- check your specific airline's requirements.

**In-flight behaviour:** Maltese are companion dogs and settle better in cabin than in the hold. They may whimper initially but most settle within 30 to 45 minutes of takeoff.

## Crate Training

Even for a tiny dog, crate training before travel reduces stress significantly. Start at least 4 to 6 weeks before travel:
- Leave the carrier open in a comfortable area
- Feed treats inside it
- Build up to closing the door for short periods
- Eventually: 30 to 45 minutes of calm confinement with you nearby

## Health Considerations

Maltese can be prone to dental disease and hypoglycaemia (low blood sugar) if they go too long without food. For long-haul flights:
- Give a small meal 2 to 3 hours before travel (not immediately before)
- Bring small treats accessible in your bag for very long flights

## Country Requirements

No country restricts Maltese dogs. Standard requirements:
- Microchip
- Rabies vaccination (if required by destination)
- Health certificate

For Australia, New Zealand, and Japan: standard process applies (titre test, 180-day wait, quarantine) regardless of breed size.

*Information accurate as of May 2026.*
"""},

{
"slug": "travelling-with-a-scottish-fold-cat-internationally",
"title": "Moving Internationally with a Scottish Fold: Health Concerns and Travel Advice",
"description": "Scottish Folds are increasingly restricted by breeding regulations in some countries. Here is what Scottish Fold owners need to know for international moves, including country attitudes and health certificate considerations.",
"date": "2026-05-09",
"tags": ["Scottish Fold cat", "cat travel", "international cat relocation"],
"faqs": [
{"q": "Are Scottish Fold cats banned or restricted in any country?",
 "a": "Scottish Folds are not banned for import in most countries. However, some countries have restrictions on breeding Scottish Folds (notably Scotland itself since 2024 and Germany under some animal welfare interpretations). Importing a Scottish Fold as a pet companion is generally permitted. The restrictions typically target breeding rather than pet ownership."},
{"q": "Do Scottish Folds face airline breed restrictions?",
 "a": "Scottish Folds are not brachycephalic in the sense that Persians or Exotic Shorthairs are. Their nose and airway structure is not severely compromised. They are not on most airlines' flat-faced cat restriction lists. Standard cat travel policies apply."},
{"q": "Are there health considerations for flying a Scottish Fold internationally?",
 "a": "Scottish Folds can carry the OCD (osteochondrodysplasia) gene that causes the folded ears and may also cause joint pain and mobility issues. Before any long-haul flight, have a vet assess your cat's joint health and confirm fitness to travel. A cat in pain or with mobility issues should not be confined in a carrier for extended periods without veterinary guidance."}
],
"body": """## The Breeding Restriction Context

Scottish Folds occupy an unusual position in international animal welfare discourse. The gene that causes the folded ears (Fd) is linked to osteochondrodysplasia -- a condition that can cause painful joint problems in cats that inherit two copies of the gene (fold x fold breeding).

Several countries have moved toward restricting **breeding** of Scottish Folds:
- **Scotland**: The Scottish SPCA successfully advocated for restrictions on breeding Scottish Folds in Scotland from 2024
- **Germany**: Some German veterinary bodies have called for breeding bans; current practice varies by state
- **Netherlands**: Breeding restrictions discussed under animal welfare law

**Importing a pet Scottish Fold** (not for breeding) remains permitted in most countries. The restrictions primarily target breeding programmes, not companion animals.

## Health Assessment Before Travel

Before any international move with a Scottish Fold:
1. Have a vet assess joint health -- is your cat showing any signs of OCD-related discomfort?
2. Assess whether a long period in a carrier is appropriate for your specific cat
3. If the cat has mobility issues, discuss pain management and travel suitability with your vet

A Scottish Fold that is healthy and pain-free travels like any other cat. One with joint issues needs a more careful approach.

## Cabin vs Hold

Scottish Folds are medium-sized cats (3 to 6 kg). Many qualify for cabin travel. Cabin travel is preferable for this breed given the joint concerns -- less time in confinement and less exposure to temperature/pressure variation.

## Country Requirements

No country has a specific **import ban** on Scottish Folds as pets (as of May 2026). Standard cat requirements apply:
- Microchip
- Rabies vaccination
- Health certificate

*Information accurate as of May 2026. Breeding regulations change -- verify the current status in your destination country.*
"""},

# ─── PRACTICAL GUIDES ─────────────────────────────────────────────────────

{
"slug": "moving-to-dubai-with-a-dog",
"title": "Moving to Dubai with a Dog: MOCCAE Permits, Breed Bans, and Expat Life",
"description": "Dubai has hundreds of thousands of expats, many with dogs. Here is the complete guide: MOCCAE import permit, breed restrictions, registration, and practical dog life in Dubai.",
"date": "2026-05-09",
"tags": ["Dubai", "UAE", "moving with a dog", "Middle East"],
"faqs": [
{"q": "Which dog breeds are banned in Dubai?",
 "a": "The UAE restricts several breeds. Prohibited or restricted breeds include Pit Bull Terriers, American Staffordshire Terriers, Staffordshire Bull Terriers, Rottweilers, Dobermans, German Shepherds (in some contexts), Chow Chows, Presa Canarios, Tosa Inus, Fila Brasileiros, and Dogo Argentinos. Verify the current list with MOCCAE before attempting to import a restricted breed."},
{"q": "Do I need an import permit to bring my dog to Dubai?",
 "a": "Yes. An import permit from the UAE Ministry of Climate Change and Environment (MOCCAE) is required before your dog travels to Dubai. Apply via the MOCCAE My Services portal at moccae.gov.ae at least 4 to 6 weeks before travel."},
{"q": "Is there quarantine for dogs arriving in Dubai?",
 "a": "Dubai does not impose mandatory quarantine for dogs from most approved countries when documentation is complete. MOCCAE vets inspect the dog on arrival at Dubai International Airport (DXB). With complete documentation, the dog is typically released the same day."}
],
"body": """## Breed Restrictions: The First Check

The UAE maintains a restricted breed list. If your dog is on this list, it cannot be imported. Check the MOCCAE website before doing anything else.

Restricted breeds as of 2026 include (but may not be limited to):
- Pit Bull Terrier and mixes
- American Staffordshire Terrier
- Staffordshire Bull Terrier
- Rottweiler
- Doberman Pinscher
- Chow Chow
- Presa Canario
- Tosa Inu, Fila Brasileiro, Dogo Argentino
- Wolf hybrids

Individual residential communities in Dubai may add further restrictions beyond the national list. Check both.

## Import Permit Application

Apply through the MOCCAE My Services portal: moccae.gov.ae

You will need:
- Dog's details (breed, sex, age, microchip number)
- Current vaccination records
- Your UAE residency or visa details

Allow 4 to 6 weeks. The permit is the foundation of your documentation -- the health certificate should reference the permit number.

## Health Documentation

1. Import permit
2. Microchip (ISO 11784/11785)
3. Rabies vaccination -- current
4. Core vaccinations -- distemper, parvovirus, hepatitis, leptospirosis
5. Official health certificate -- from a vet in your country, endorsed by your national authority, issued within 14 days of travel
6. Parasite treatment (flea, tick, deworming within 14 days)

## After Arrival in Dubai

Register your dog with Dubai Municipality within 30 days of arrival. Annual renewal applies. Keep rabies vaccination current -- it is a registration requirement.

## Practical Dog Life in Dubai

Dubai has become increasingly dog-friendly:
- Several dedicated dog parks (Safa Park, Barsha Pond Park, Dubai Hills areas)
- Multiple international-standard veterinary hospitals
- Dog-friendly beaches in designated areas
- Well-stocked pet stores throughout the city

**Heat management:** Dubai summers (May to October) are extreme. Walk dogs before 7am and after 8pm. Brachycephalic breeds need careful monitoring year-round.

*Verify current MOCCAE breed restrictions and requirements at moccae.gov.ae. Information accurate as of May 2026.*
"""},

{
"slug": "moving-to-hong-kong-with-a-cat",
"title": "Moving to Hong Kong with a Cat: AFCD Import Requirements Explained",
"description": "Hong Kong has a structured cat import process managed by AFCD. Here is what cat owners moving to Hong Kong need: import licence, health certificate, and 4-day in-situ quarantine.",
"date": "2026-05-09",
"tags": ["Hong Kong", "cat import", "AFCD", "Asia pet travel"],
"faqs": [
{"q": "Does Hong Kong require quarantine for imported cats?",
 "a": "Hong Kong requires an in-situ quarantine period of at least 4 days for cats from most countries (longer for cats from countries with specific disease concerns). The quarantine is conducted at the AFCD quarantine facility at Tsuen Wan or at an approved quarantine facility. The exact duration depends on your cat's country of origin and vaccination history."},
{"q": "What is AFCD and what role does it play in cat imports to Hong Kong?",
 "a": "AFCD (Agriculture, Fisheries and Conservation Department) manages all live animal imports into Hong Kong, including pet cats. You must apply to AFCD for a pet import licence before your cat travels. AFCD inspectors check documentation and manage the quarantine process."},
{"q": "What vaccinations does Hong Kong require for imported cats?",
 "a": "Hong Kong requires current core vaccinations for cats: rabies and FVRCP (feline viral rhinotracheitis, calicivirus, panleukopenia). The vaccination history must be documented in the health certificate. A microchip is required. Confirm the current AFCD requirements at afcd.gov.hk before travel."}
],
"body": """## Why Hong Kong Has a Cat Import Process

Hong Kong is a densely populated urban environment with strict biosecurity concerns. AFCD manages cat imports carefully to protect the territory's cat population from imported diseases.

## AFCD Import Licence: Apply First

You must apply to AFCD for a pet import licence before travel. Do not book flights or transport without an approved licence. Apply at:

AFCD website: afcd.gov.hk (Animal & Plant Health section)

The licence application requires:
- Cat's details (breed, sex, age, microchip number)
- Vaccination history
- Country of origin
- Intended arrival details

Allow 4 to 6 weeks for the licence application.

## The Quarantine Requirement

Most cats arriving in Hong Kong must complete a quarantine period at an AFCD-approved facility. The standard duration for cats from most approved countries is 4 days, but this can be longer depending on origin country.

The quarantine facility at Tsuen Wan is the main AFCD-operated option. Private AFCD-approved facilities also exist. Your cat is cared for, fed, and checked by vets during quarantine.

## Health Documentation

1. AFCD import licence (must be obtained before travel)
2. Microchip (ISO 11784/11785)
3. Current rabies vaccination
4. Current FVRCP vaccination
5. Official health certificate -- from a government-accredited vet in your country, endorsed by your national authority, issued within 10 days of arrival in Hong Kong
6. Treatment and parasite prevention records

## Practical Life with a Cat in Hong Kong

Hong Kong is a comfortable place for cats in urban apartment settings. Several excellent veterinary practices operate across Hong Kong Island, Kowloon, and the New Territories. The warm, humid climate means indoor cats need good ventilation. Balcony safety (mesh or screens) is important given Hong Kong's high-rise nature.

*Verify current AFCD requirements at afcd.gov.hk before travel. Information accurate as of May 2026.*
"""},

{
"slug": "quarantine-free-countries-pet-travel-2026",
"title": "Which Countries Have No Pet Quarantine in 2026: A Complete Guide",
"description": "Many countries do not require quarantine for well-documented pets. Here is a guide to quarantine-free pet travel destinations in 2026 and what you still need even without quarantine.",
"date": "2026-05-09",
"tags": ["quarantine free", "pet travel", "no quarantine countries"],
"faqs": [
{"q": "Which countries require no quarantine for pets from the UK?",
 "a": "Most EU member states, USA, Canada, Japan (if compliant documentation), most Middle Eastern countries, Singapore (Category A/B countries), and many others do not require mandatory quarantine for pets with complete documentation from the UK. Australia and New Zealand are notable exceptions -- both require 10-day quarantine regardless of documentation."},
{"q": "Does no quarantine mean no requirements?",
 "a": "No. Quarantine-free entry still requires full documentation: microchip, vaccinations, health certificate, and sometimes parasite treatment and permits. Quarantine-free means your pet is not held at a government facility after arrival -- it does not mean the process is documentation-free."},
{"q": "Which countries always require quarantine regardless of documentation?",
 "a": "Australia and New Zealand require mandatory quarantine (10 days in Australia, up to 10 days in New Zealand) for all imported dogs and cats, regardless of how well-documented they are. Hawaii (as part of the USA) also has a rabies-free status that creates quarantine-like requirements for pets that do not meet its specific programme requirements."}
],
"body": """## The Key Distinction

Quarantine-free entry means your pet passes through a veterinary inspection on arrival and -- if documentation is complete -- goes home with you the same day. It does not mean there are no requirements. Every country still needs documentation.

## Quarantine-Free for Most Well-Documented Pets

**EU member states (including France, Germany, Spain, Italy, Netherlands):** No quarantine for pets from approved third countries (UK, USA, Canada, Australia, etc.) with correct AHC, rabies vaccination, and microchip. Dogs need tapeworm treatment.

**United Kingdom (post-Brexit):** No quarantine for pets from most countries with correct AHC. Tapeworm treatment required for dogs.

**USA:** No quarantine for dogs and cats from most countries, subject to CDC dog import rules. Cats face minimal entry requirements.

**Canada:** No quarantine for dogs and cats with current vaccination and health certificate from most countries.

**UAE / Dubai / Abu Dhabi:** No quarantine for pets from approved countries with MOCCAE permit, health certificate, and vaccinations.

**Singapore:** No mandatory quarantine for pets from Category A countries (includes UK, Australia, New Zealand) with AVS import licence and documentation. Category B countries may have shorter supervised observation.

**Japan:** No quarantine for dogs and cats from rabies-free countries (Category I). For most countries -- including the UK, USA, Australia -- Japan requires the titre test, 180-day wait, and pre-arrival notification, but the actual quarantine on arrival is brief (180-day wait replaces the holding quarantine that used to apply).

## Countries That Always Require Quarantine

**Australia:** 10-day quarantine at Mickleham, Victoria. No exceptions.

**New Zealand:** Up to 10 days quarantine at MPI-approved facility in Auckland. No exceptions.

**Hawaii (USA):** Rabies-free island. Pets that do not meet the 5-Day-Or-Less programme requirements face 120-day quarantine. The 5-Day-Or-Less programme requires: microchip (ISO), two rabies vaccinations with correct timing, FAVN titre test (at least 30 days after final vaccine, result 0.5 IU/mL), OGF approval. Meeting all requirements allows 5-day post-arrival inspection rather than 120-day quarantine.

## What Quarantine-Free Still Requires

Even for quarantine-free destinations, you will typically need:
- Microchip (ISO 11784/11785)
- Rabies vaccination (current)
- Official health certificate (endorsed by national authority)
- Import permit (some countries)
- Parasite treatments (documented)

The difference is that instead of a facility stay, a vet inspector at the airport or border checks your documents and your pet goes home with you.

*Requirements change. Always verify with the destination country's authority before travel. Information accurate as of May 2026.*
"""},

{
"slug": "crate-training-for-air-travel-guide",
"title": "Crate Training for Air Travel: A Step-by-Step Guide for Dogs and Cats",
"description": "Crate training is the single most important preparation for international pet travel. Here is a step-by-step process for dogs and cats, from first introduction to extended confident confinement.",
"date": "2026-05-09",
"tags": ["crate training", "air travel preparation", "pet travel training"],
"faqs": [
{"q": "How long before the flight do I need to start crate training?",
 "a": "Start as early as possible -- ideally 3 to 6 months before travel. At minimum, 6 to 8 weeks of consistent training is needed for most dogs and cats. The goal is not just tolerance but genuine comfort. A pet that loves its crate travels dramatically better than one that merely tolerates it."},
{"q": "Should the crate be the same one used on the flight?",
 "a": "Yes. Always train with the exact crate you will use on the day. Dimensions, ventilation, and smell all matter. If the training crate is unfamiliar on travel day, the pet is adapting to a new environment at the worst possible time."},
{"q": "Can I put a sedative in the crate for air travel?",
 "a": "Most vets and IATA guidelines recommend against sedation for air travel. Sedated pets have reduced muscle control and thermoregulation, which increases risk during cargo handling. Discuss with your vet before travel. Veterinary-recommended calming supplements (not sedatives) may be appropriate for anxious animals; discuss options with your vet well before travel day."}
],
"body": """## Why Crate Training Matters

A pet that is genuinely comfortable in its crate -- one that chooses to rest there, that finds it calm and familiar -- handles the stresses of air travel (noise, vibration, separation, unfamiliar smells) significantly better than a pet for whom the crate is associated only with vet visits.

The crate training work you do at home is the most important thing you can do for your pet's travel wellbeing.

## Step-by-Step: Dogs

**Weeks 1 to 2: Introduction**
- Place the crate in a high-traffic area with the door open
- Put a familiar blanket or piece of your clothing inside
- Do not force the dog in -- wait for curiosity
- Feed treats at the door, then just inside, then fully inside

**Weeks 3 to 4: Positive association building**
- Feed meals in the crate with door open
- Use a cue word ("crate", "bed", "home") every time the dog goes in
- Begin closing the door for short periods (2 to 5 minutes) while you are present

**Weeks 5 to 6: Building duration**
- Extend closed-door periods: 10 minutes, 30 minutes, 1 hour
- Practice with you in the room, then with you out of sight briefly
- Practice picking up the crate and moving it (simulates airline handling)

**Weeks 7 to 12: Confidence building**
- Leave the dog in the crate for 2 to 4 hour periods
- Practice the full travel sequence: crate up, into a vehicle, travel, out again

## Step-by-Step: Cats

Cats can be trained to use crates positively but take longer and require more patience.

**Weeks 1 to 3:**
- Leave the carrier open in the cat's favourite area
- Do not force any interaction -- let the cat investigate at its own pace
- Put familiar bedding or your worn clothing inside

**Weeks 4 to 6:**
- Feed meals in the carrier with door open
- Use a feather toy or treats to encourage the cat to enter fully

**Weeks 7 onwards:**
- Begin closing the door for 2 to 5 minutes while feeding treats through the door
- Gradually build to 30 to 60 minutes of calm, closed-door confinement

## What to Put in the Crate

- A recently worn (unwashed) item of your clothing
- A familiar blanket
- Absorbent pad on the floor (for long travel)
- A small amount of water in a travel bowl for very long journeys (most short-medium haul is fine without water)
- NOTHING that can be chewed into pieces and swallowed (no rope toys, soft toys with stuffing)

## On the Day

Feed a light meal 3 to 4 hours before travel. Do not withhold food entirely for very long journeys. Ensure the crate is clean and familiar. Load your pet into the crate calmly, at home, before the airport chaos.

*Information accurate as of May 2026.*
"""},

{
"slug": "pet-relocation-common-myths",
"title": "10 Common Pet Relocation Myths (And What Is Actually True)",
"description": "From sedation myths to paperwork confusion, here are 10 misconceptions about international pet travel -- and the facts every pet owner should know before booking.",
"date": "2026-05-09",
"tags": ["pet relocation myths", "pet travel facts", "international pet transport"],
"faqs": [
{"q": "Is it true that airlines refuse to fly brachycephalic breeds?",
 "a": "Many airlines have restrictions on transporting brachycephalic (flat-faced) breeds, particularly in the cargo hold, due to respiratory risks. However, some airlines permit snub-nosed breeds under specific conditions. Restrictions vary by airline, aircraft type, season, and route. Small brachycephalic dogs may fly in cabin on some airlines where they do not qualify for hold cargo. Always check with the specific airline for your specific animal."},
{"q": "Do pets always need quarantine for international moves?",
 "a": "No. Many countries -- including most EU member states, the USA, Canada, and most Middle Eastern countries -- do not require quarantine for well-documented pets. Australia and New Zealand are notable exceptions and require 10-day quarantine regardless. Hawaii has strict requirements but an alternative programme."},
{"q": "Is it true you can send a pet internationally as regular checked baggage?",
 "a": "This depends on the airline, the animal's size, and the route. Small pets (under 6 to 8 kg combined with carrier) may travel in the aircraft cabin on many airlines. Medium and large pets travel as air cargo -- a separate service from checked baggage. The process for air cargo pets is distinct from checked baggage and involves advance booking, separate documentation, and often separate check-in at a cargo terminal."}
],
"body": """## Myth 1: Pets Always Need Quarantine

Only a handful of countries mandate quarantine regardless of documentation -- most notably Australia (10 days), New Zealand (up to 10 days), and Hawaii (120 days unless the 5-Day-Or-Less programme requirements are met). Most countries do not require quarantine for properly documented pets.

## Myth 2: You Must Sedate Your Pet for the Flight

Veterinary guidance and IATA guidelines recommend against sedating pets for air travel. Sedated animals have impaired muscle coordination and thermoregulation. Most well-prepared, crate-trained pets manage travel without sedation. Discuss calming options with your vet -- non-sedative anxiety-reducing supplements may be appropriate for some animals.

## Myth 3: Any Vet Can Sign an International Health Certificate

International health certificates must be signed by a vet with specific government accreditation (USDA-accredited in the USA, an Official Veterinarian in the UK, a DAFF-accredited vet in Australia). Your regular vet may or may not have this accreditation. Check before booking the appointment.

## Myth 4: If Your Pet Has an EU Pet Passport, You Can Go Anywhere

EU Pet Passports cover travel between EU member states and from the EU to listed third countries. They do not work for all destinations. Australia, New Zealand, Japan, and the USA require different documentation. Post-Brexit, EU Pet Passports are not accepted for entry into Great Britain.

## Myth 5: A Microchip Is Optional

In practice, a microchip is required for entry to the EU, UK, Australia, New Zealand, Japan, Singapore, and many other countries. For all practical purposes, microchipping before travel is not optional for international moves.

## Myth 6: Flying Is Traumatising for Pets

Studies on pet air travel suggest that most healthy, well-prepared pets experience moderate stress during travel but recover quickly after arrival. The stress of a well-prepared move is significantly lower than the stress of a poorly-prepared one. Good crate training, familiar scents, and a health check before travel are the most important mitigations.

## Myth 7: The Cheapest Flight Is Best for Your Pet

Low-cost carriers often do not accept pets. Routes with many connections extend the time in cargo and increase the number of stressful loading/unloading events. A direct flight on a carrier with strong live animal handling capabilities is generally better for your pet than a cheaper multi-stop option, even at higher cost.

## Myth 8: You Can Use Any Crate

IATA has specific crate size requirements (Regulation Live Animals 62nd Edition). The crate must allow the animal to stand at full height, turn around, and lie down. It must be well-ventilated on multiple sides, have a leak-proof floor, and be escape-proof. Airline staff can and do reject non-compliant crates at check-in.

## Myth 9: The Process Is the Same for Dogs and Cats

Cats and dogs often have different import requirements at the destination. Japan, for example, has specific documentation differences between dogs and cats. Australia treats them similarly for quarantine but the paperwork process is the same for both. Always verify requirements specifically for your animal's species.

## Myth 10: An Agent Is Just an Extra Cost

For complex moves (Australia, New Zealand, Japan; multi-leg journeys; restricted breeds), an experienced IPATA-member agent reduces errors, handles airline bookings with carriers that have good live animal relationships, and often prevents expensive mistakes. For straightforward EU moves, a well-organised owner can often manage independently.

*Information accurate as of May 2026.*
"""},

{
"slug": "pet-transport-glossary-terms-2026",
"title": "International Pet Transport Glossary: Terms Every Pet Owner Should Know",
"description": "From FAVN to IATA to AHC, international pet transport has a vocabulary all of its own. Here is a plain-English glossary of the key terms every relocating pet owner needs to understand.",
"date": "2026-05-09",
"tags": ["pet transport glossary", "pet travel terms", "international pet transport"],
"faqs": [
{"q": "What does FAVN stand for in pet travel?",
 "a": "FAVN stands for Fluorescent Antibody Virus Neutralisation. It is the specific rabies antibody test required by Australia, New Zealand, Japan, and some other countries. The test measures virus-neutralising antibodies in your pet's blood. A result of 0.5 IU/mL or above is required."},
{"q": "What is an OV in pet transport?",
 "a": "OV stands for Official Veterinarian. In the UK, OVs are government-authorised vets who can issue official Animal Health Certificates (AHCs) for international pet travel. Not every vet is an OV. In the USA, the equivalent is a USDA-accredited veterinarian. In Australia, a DAFF-registered vet."},
{"q": "What is IPATA?",
 "a": "IPATA (International Pet and Animal Transportation Association) is the trade association for professional pet transport agents worldwide. IPATA members agree to a code of ethics and best practice standards. Using an IPATA-member agent provides a baseline assurance of professional standards."}
],
"body": """## A to Z of Key Pet Transport Terms

**AHC (Animal Health Certificate):** The official document required to move a pet internationally in most cases. Must be prepared by an accredited vet and endorsed by a government authority. Each destination country specifies the required format.

**APHA:** Animal and Plant Health Agency (UK). The UK government body that endorses AHCs for pets travelling from the UK to non-EU countries. APHA vets are OVs.

**APHIS:** Animal and Plant Health Inspection Service (USA). The USDA division that endorses health certificates for pets travelling from the USA internationally. USDA APHIS has state offices.

**AVS:** Animal and Veterinary Service (Singapore). Manages all animal imports and exports in Singapore under the National Parks Board (NParks).

**BICON:** Biosecurity Import Conditions database (Australia). Australia's online tool at bicon.agriculture.gov.au where importers check the current import conditions for specific animals into Australia.

**CFIA:** Canadian Food Inspection Agency. The Canadian government authority that endorses health certificates for pets travelling from Canada internationally.

**DAFF:** Department of Agriculture, Fisheries and Forestry (Australia). The Australian government authority that manages pet imports and exports.

**EU Pet Passport:** A standardised booklet issued by EU member state vets that records microchip, vaccinations, and titre test results for pets travelling within the EU and to/from listed third countries.

**FAVN:** Fluorescent Antibody Virus Neutralisation test. The gold-standard rabies antibody test required by Australia, New Zealand, Japan, and some other countries. Blood is drawn by a vet and sent to an approved laboratory.

**IATA:** International Air Transport Association. Sets global standards for live animal transport by air, including crate specifications (Container Requirement 82 for dogs and cats).

**IPATA:** International Pet and Animal Transportation Association. The professional body for pet transport agents.

**ISO 11784/11785:** The international standard for microchips. A compliant chip has 15 digits. Some older US chips have 10 digits -- these may not be readable by standard international scanners.

**IU/mL:** International Units per millilitre. The unit used to express FAVN titre test results. The internationally accepted minimum passing level is 0.5 IU/mL.

**MAFF:** Ministry of Agriculture, Forestry and Fisheries (Japan). The Japanese authority that manages pet imports. Japan has one of the most complex pet import systems in the world.

**MOCCAE:** Ministry of Climate Change and Environment (UAE). The UAE authority that manages pet import permits and live animal imports.

**OIE:** World Organisation for Animal Health (now WOAH). Sets international animal health standards including approved rabies titre test laboratories.

**OV (Official Veterinarian):** A government-authorised vet empowered to issue official health certificates. In the UK: APHA-authorised. In Ireland: Department of Agriculture, Food and Marine-authorised. In the USA: USDA-accredited.

**Titre test:** Blood test measuring antibody levels. In pet travel, usually refers to the FAVN rabies titre test. Results above 0.5 IU/mL confirm adequate rabies immunity.

**Zoonotic disease:** An animal disease that can be transmitted to humans. Rabies is the primary zoonotic disease concern in international pet movement, driving most of the strictest import requirements (Australia, NZ, Japan, Hawaii).

*Information accurate as of May 2026.*
"""},

{
"slug": "guide-dogs-and-assistance-animals-international-travel",
"title": "Guide Dogs and Assistance Animals: International Travel Rights and Requirements",
"description": "Guide dogs and registered assistance animals have special protections for international travel, including cabin rights on many airlines. Here is a country-by-country guide to rights, requirements, and documentation.",
"date": "2026-05-09",
"tags": ["guide dogs", "assistance animals", "disability pet travel"],
"faqs": [
{"q": "Can a guide dog travel in the aircraft cabin internationally?",
 "a": "Yes. Registered guide dogs and assistance dogs have the legal right to travel in the aircraft cabin on most international routes. This is separate from ordinary pet cabin travel and does not count against standard cabin pet allowances. The dog travels on the floor in front of or beside its handler. Documentation of the dog's registered assistance status is typically required."},
{"q": "Does a guide dog still need to comply with pet import requirements at the destination?",
 "a": "Yes. A guide dog entering a foreign country must meet all the same import documentation requirements as any other dog. This includes microchip, rabies vaccination, health certificate, and titre test/quarantine if required by the destination country (Australia and New Zealand, for example, require guide dogs to complete their quarantine programme -- no exemption is made for assistance animal status)."},
{"q": "What documentation does a guide dog owner need for international travel?",
 "a": "In addition to standard pet import documentation, guide dog handlers typically need: official registration documentation from the issuing organisation (Guide Dogs, RNIB, etc.), a letter on headed paper confirming the dog's registered assistance status, and ideally advance notification to the airline. Some airlines have specific forms for assistance animal notification."}
],
"body": """## In-Cabin Rights for Guide and Assistance Dogs

Most major airlines and international aviation authorities recognise that registered guide dogs and assistance dogs should travel in the aircraft cabin with their handlers. This is:
- A distinct category from ordinary pet cabin travel
- Not subject to standard cabin pet weight or size limits
- Not counted against the cabin pet allowance

**UK airlines** (British Airways, Virgin Atlantic, easyJet, etc.) follow UK Equality Act 2010 provisions and international conventions. Guide dogs travel in cabin.

**EU airlines** follow EU rules and the Montreal Convention on passenger rights.

**US carriers** follow the Air Carrier Access Act (ACAA) provisions for service animals.

Advance notification to the airline is always required -- typically 48 hours before departure for guide dogs.

## Still Subject to Import Requirements

Guide dog status provides **cabin travel rights** but does not exempt the dog from destination country veterinary import requirements. This surprises many guide dog handlers.

**Australia:** Guide dogs must complete the same FAVN titre test, 180-day wait, and 10-day quarantine at Mickleham as any other dog. DAFF (Australian Department of Agriculture) makes no exemption for assistance animal status. This means planning a move to Australia with a guide dog requires the same 7-plus-month preparation timeline.

**New Zealand:** Same principle -- guide dogs must meet MPI requirements including titre test and quarantine.

**Japan:** Guide dogs must meet MAFF requirements including titre test and 180-day wait.

**EU member states:** Guide dogs from listed countries follow the same AHC, microchip, and vaccination requirements as pet dogs.

## Documentation for International Guide Dog Travel

In addition to standard pet import documentation, carry:
1. Official registration documentation from your guide dog organisation
2. A letter on the organisation's headed paper confirming the dog's registration number, handler's name, and assistance status
3. Your airline's advance notification confirmation
4. All standard pet import documentation (health certificate, microchip details, vaccination records)

## Practical Planning

Contact both the airline and the destination country's veterinary authority well in advance. For guide dog moves to Australia or Japan in particular, the preparation timeline is the same as for any dog -- start 7 to 9 months before the travel date.

*Information accurate as of May 2026. Rights and requirements vary by country and airline policy.*
"""},

{
"slug": "what-to-pack-in-your-pet-travel-kit",
"title": "What to Pack in Your Pet Travel Kit: Documents, Supplies, and Comfort Items",
"description": "International pet travel requires more preparation than domestic trips. Here is a complete packing list covering documentation, supplies for the journey, and comfort items for your pet.",
"date": "2026-05-09",
"tags": ["pet travel packing", "travel preparation", "pet travel checklist"],
"faqs": [
{"q": "What documents should I carry with me when travelling internationally with a pet?",
 "a": "Carry originals of all documents: health certificate, import permit, microchip documentation, vaccination records, and titre test results (if applicable). Store digital copies in cloud storage as backup. For Australia and New Zealand, also carry the DAFF/MPI import permit and quarantine booking confirmation."},
{"q": "Should I bring food for my pet to the airport?",
 "a": "Yes. Bring a small amount of your pet's regular food in a sealed bag. For cabin travel, a few treats accessible in your hand luggage help with settling your pet. For cargo travel, tape a small sealed bag of food to the top of the crate for the care instructions card -- this allows airline or cargo handlers to feed your pet if there is a significant delay."},
{"q": "What should go inside the crate for a long flight?",
 "a": "Inside the crate: a recently worn, unwashed piece of your clothing (familiar scent), an absorbent floor pad (waterproof-backed), and a small amount of water in a clip-on bowl. Attach a second frozen water supplement on the outside that can be accessed by handlers if needed. Do not include food bowls inside the crate as these become projectile hazards during turbulence."}
],
"body": """## The Documents Folder: Non-Negotiable

Keep all travel documents in one waterproof folder, separate from your own travel documents so they can be handed over quickly at border inspection:

- Original health certificate (AHC or national equivalent)
- Import permit (where required)
- Microchip documentation (or the passport showing chip number)
- Vaccination record
- FAVN titre test certificate (where required -- AU, NZ, Japan, Hawaii)
- Rabies vaccination certificate
- Any breed-specific documentation (for restricted breeds)
- Airlines' booking confirmation for live animal cargo

**Digital backup:** Photograph every document and upload to cloud storage. This has saved multiple pet owners when originals were lost or damaged.

## Crate Preparation Kit

- Absorbent floor pads (bring spares for after quarantine or on connecting legs)
- Clip-on water bowl
- Frozen water supplement that thaws slowly and provides water without a spillable bowl
- Live animal sticker kit (most airlines provide, but bring your own as backup)
- Cable ties for crate security (IATA requires the crate to be securable from outside)

## Comfort Items

- A recently worn, unwashed item of your clothing to place in the carrier or crate
- A familiar toy (check: nothing that can be destroyed and swallowed)
- For cats: a small spritz of Feliway pheromone spray on the bedding, 30 minutes before crating
- For dogs: a favourite chew that keeps them occupied for the initial loading phase

## Health Kit for After Arrival

- 1 to 2 weeks of regular food (familiar food reduces digestive disruption after a stressful journey)
- Any regular medications
- Your home vet's contact details and medical records
- Contact details of the recommended vet at the destination
- First aid items: saline wash, tick tweezers, bandage material

## A Note on Food and Water During Travel

For flights under 8 hours, most healthy adults do not need food or water during the actual flight. For longer journeys:
- Offer a drink of water in the last 2 to 3 hours before travel
- Attach a label to the crate with feeding instructions if your pet is on a schedule or medicated diet
- Do not withhold water for more than 4 to 6 hours

*Information accurate as of May 2026.*
"""},

{
"slug": "australia-to-france-pet-transport-guide",
"title": "Pet Transport from Australia to France: What Australian Pets Need for French Entry",
"description": "Moving from Australia to France? Australia is EU-listed, so no titre test is required. Here is the process: DAFF-endorsed AHC, tapeworm treatment, flight routing, and arriving at Charles de Gaulle.",
"date": "2026-05-09",
"tags": ["Australia to France", "pet transport", "EU pet import"],
"faqs": [
{"q": "Does Australia qualify for EU entry without a titre test?",
 "a": "Yes. Australia is listed as an approved third country under EU Regulation 576/2013. Australian dogs and cats can enter France without a rabies titre test. You need a microchip, current rabies vaccination (at least 21 days old if first-ever vaccination), and a DAFF-endorsed EU Animal Health Certificate (AHC)."},
{"q": "Does a dog from Australia need tapeworm treatment to enter France?",
 "a": "Yes. All dogs entering any EU member state (including France) from a non-EU country require tapeworm treatment (praziquantel) administered by a vet 1 to 5 days before arriving in the EU. This must be documented in the AHC."},
{"q": "What is the best flight routing from Australia to France?",
 "a": "There are no direct flights from Australia to France. Common routes go via Singapore (SIN), Dubai (DXB), Abu Dhabi (AUH), or Doha (DOH). Singapore Airlines and Air France sometimes codeshare through Singapore. Emirates, Qantas via Dubai, and Qatar Airways via Doha are other options. Each leg must accept live animal cargo on the specific aircraft."}
],
"body": """## Australia's EU Status

Australia is a Part 1 listed country under EU Regulation 576/2013. No titre test is required for Australian pets entering France or other EU member states. This is a significant advantage compared to moves from Australia to Japan or New Zealand (which require EU-equivalent processes when moving in).

## What Your Australian Pet Needs

1. **Microchip** (ISO 11784/11785 -- standard Australian chips comply)
2. **Rabies vaccination** -- current, at least 21 days before EU arrival for a first-ever vaccination
3. **EU Animal Health Certificate (AHC)** -- issued by a DAFF-accredited vet on the EU template, endorsed by DAFF, issued within 10 days of arrival in France
4. **Tapeworm treatment** (dogs only) -- praziquantel, 1 to 5 days before EU arrival, documented in the AHC

## DAFF AHC Endorsement

DAFF provides export health certification at agriculture.gov.au. Your DAFF-accredited vet prepares the AHC; DAFF endorses it. Allow 3 to 5 business days. The 10-day validity window means the endorsement must happen close to your travel date.

## Routing Australia to France

Via **Singapore (SIN):** Qantas or Singapore Airlines to Singapore, then Air France, Singapore Airlines, or Lufthansa to Paris CDG. Singapore Airlines has strong live animal cargo handling.

Via **Dubai (DXB):** Qantas or Emirates to Dubai, then Air France or other carriers to Paris CDG. Emirates SkyCargo has good large animal capabilities.

Via **Doha (DOH):** Qantas via Doha, then Qatar Airways or onward to Paris CDG. Qatar Airways accepts pets on many routes.

For each option, confirm the specific flight on your travel date accepts live animal cargo.

## French Registration After Arrival

France does not require dog registration at the national level in the same way Germany does. However, rabies vaccination must be kept current under French law. Obtain a French EU Pet Passport from a registered vet after arrival to simplify future EU travel.

*Verify current DAFF and French/EU requirements before travel. Information accurate as of May 2026.*
"""},

{
"slug": "usa-to-spain-pet-transport-guide",
"title": "Pet Transport from the USA to Spain: EU Rules for American Pet Owners",
"description": "Moving from the USA to Spain with a pet? Spain follows EU pet travel rules. Here is what US pet owners need: USDA-endorsed AHC, tapeworm treatment, and what to expect at Madrid Barajas.",
"date": "2026-05-09",
"tags": ["USA to Spain", "pet transport", "Spain pet import"],
"faqs": [
{"q": "Does the USA qualify for EU entry to Spain without a titre test?",
 "a": "Yes. The USA is on the EU's approved third country list. Pets from the USA can enter Spain without a rabies titre test. You need a microchip, current rabies vaccination (at least 21 days old if first vaccination), and an EU AHC endorsed by USDA APHIS."},
{"q": "What airport should I use when flying a pet to Spain from the USA?",
 "a": "Madrid Barajas International Airport (MAD) is Spain's largest airport and the primary point of entry for live animal cargo from the USA. Barcelona El Prat Airport (BCN) also handles international live animal arrivals. Both have veterinary border inspection posts. For southern Spain destinations, Malaga Airport (AGP) serves Andalucia; confirm live animal facilities before routing through smaller airports."},
{"q": "Do dogs from the USA need tapeworm treatment to enter Spain?",
 "a": "Yes. Dogs entering any EU member state including Spain from a non-EU country require tapeworm treatment (praziquantel) administered by a vet 1 to 5 days before EU arrival. This is documented in the AHC."}
],
"body": """## Spain as an EU Member State

Spain follows EU Regulation 576/2013 for pet imports from third countries. The USA is listed, which means no titre test -- just the standard AHC process.

## What Your Pet Needs

1. **Microchip** -- ISO 11784/11785. Add a 15-digit ISO chip if your pet has a legacy 10-digit US chip.
2. **Rabies vaccination** -- current. First-ever vaccination must be at least 21 days before EU arrival.
3. **EU AHC** -- prepared by a USDA-accredited vet, endorsed by USDA APHIS, issued within 10 days of arriving in Spain
4. **Tapeworm treatment** (dogs only) -- praziquantel, 1 to 5 days before EU arrival, documented in the AHC

## Getting the AHC

Find a USDA-accredited vet at aphis.usda.gov/pet-travel. After the vet prepares the AHC, submit to USDA APHIS for endorsement (2 to 5 business days). The 10-day validity means the endorsement must happen close to your travel date.

## Airlines from USA to Spain

- **Iberia** -- major Spanish carrier. Flies from Miami, New York JFK to Madrid Barajas. Iberia accepts pets in cargo.
- **American Airlines** -- partner of Iberia; flights from US cities to Madrid
- **Air Europa** -- Madrid hub, limited US originating routes
- **Level** -- budget long-haul between US East Coast and Barcelona; check current pet policy

## After Arrival in Spain

Spain requires dog registration (censo canino) at the local municipality. Dogs must be registered with the local council and microchipped (already done for EU entry). Annual vaccination updates required. Sterilisation incentives apply in some municipalities.

Spain also requires all dogs to carry identification (collar tag with owner contact details) in public spaces.

*Verify current USDA APHIS and Spanish/EU requirements before travel. Information accurate as of May 2026.*
"""},

]  # END ARTICLES LIST


def write_article(article):
    slug = article["slug"]
    filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {slug}")
        return

    faqs = article["faqs"]
    faq_block = "\n".join([
        f'  - question: "{q["q"]}"\n    answer: "{q["a"]}"'
        for q in faqs
    ])

    tags_block = "\n".join([f'  - "{t}"' for t in article["tags"]])

    content = f"""---
title: "{article['title']}"
description: "{article['description']}"
date: {article['date']}
type: blog
author: "The PetTransportGlobal Team"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{article['title']}"
  description: "{article['description']}"
tags:
{tags_block}
faqs:
{faq_block}
---

{article['body'].strip()}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"WRITTEN: {slug}")


if __name__ == "__main__":
    written = 0
    skipped = 0
    for article in ARTICLES:
        existed = os.path.exists(os.path.join(OUTPUT_DIR, f"{article['slug']}.md"))
        write_article(article)
        if existed:
            skipped += 1
        else:
            written += 1
    print(f"\nDone. Written: {written} | Skipped: {skipped} | Total: {len(ARTICLES)}")
