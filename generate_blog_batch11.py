"""
Blog Batch 11 - 25 new articles (249 total)
Country guides, route guides, breed guides, practical articles
"""

import os

OUTPUT_DIR = "site/content/blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [

# ── COUNTRY IMPORT GUIDES ──────────────────────────────────────────────────

{
"slug": "slovakia-pet-import-guide",
"title": "Moving to Slovakia with Pets: EU Rules Made Simple",
"description": "Slovakia is an EU member with straightforward pet import rules. Here is what you need for dogs and cats: microchip, EU Pet Passport or AHC, and rabies vaccination.",
"date": "2026-05-06",
"tags": ["Slovakia", "pet import", "EU pet travel"],
"faqs": [
{"question": "Does Slovakia require quarantine for imported pets?", "answer": "No. Dogs and cats entering Slovakia from other EU countries with a valid EU Pet Passport face no quarantine. Pets from non-EU countries must have a current AHC, microchip, and rabies vaccination, but no mandatory quarantine applies if paperwork is complete."},
{"question": "What vaccinations are required to bring a pet into Slovakia?", "answer": "Rabies vaccination is mandatory for all dogs, cats, and ferrets entering Slovakia. The first rabies vaccine must be given at least 21 days before travel. Boosters must be within the validity period shown on the vaccine data sheet."},
{"question": "Which airport handles pet arrivals in Slovakia?", "answer": "Bratislava Airport (BTS) is the main international gateway. It has a veterinary inspection point for live animal arrivals. Vienna Airport (VIE) in neighbouring Austria is also commonly used and is about an hour from Bratislava by road."}
],
"body": """
Slovakia joined the EU in 2004 and the Schengen Area in 2007, which makes it one of the simpler EU destinations for pet travel. The rules are standard EU requirements -- no unusual local additions that catch people off-guard.

## From EU Countries: Standard EU Pet Passport

Travelling from Germany, Austria, Czech Republic, Hungary, or any EU member? You need:

- ISO-standard microchip (15-digit, ISO 11784/11785)
- Valid EU Pet Passport
- Rabies vaccination that is current (administered at least 21 days after the first-ever microchip implant)

The EU Pet Passport covers everything -- keep it accessible at border crossings.

## From Non-EU Countries (Including the UK)

For pets arriving from outside the EU:

1. **Microchip** (ISO 11784/11785 standard)
2. **Rabies vaccination** -- current, administered at least 21 days before first EU entry
3. **Animal Health Certificate (AHC)** -- issued by an official government vet within 10 days of entry, endorsed by your national authority (APHA for UK, USDA for USA)
4. **Tapeworm treatment** (dogs only) -- 1 to 5 days before entering any EU state

Slovakia follows the standard EU framework -- no additional national requirements beyond these.

## Bratislava vs Vienna Entry

Many people moving to western Slovakia use Vienna Airport (VIE) rather than Bratislava Airport (BTS). Vienna has a larger and better-equipped veterinary border inspection post. If your pet is arriving as air cargo, VIE may offer more handling options. BTS is perfectly adequate for cabin-carried or accompanied baggage pets.

## Slovak Registration

Dogs must be registered in Slovakia within 30 days of taking up residence. The registration is handled by your local municipality (obec or mestska cast). Annual rabies vaccination is compulsory under Slovak law for dogs.

## Useful Contacts

- **State Veterinary and Food Administration of the Slovak Republic (SVPS)**: svps.sk
- **EU Pet Travel Rules**: ec.europa.eu/food/animals/movement-pets

*Information current as of May 2026. Verify with SVPS before travel.*
"""
},

{
"slug": "luxembourg-pet-import-guide",
"title": "Moving to Luxembourg with Pets: A Short Guide to EU Pet Travel Rules",
"description": "Luxembourg is a small EU and Schengen member with standard EU pet import rules. Here is what dogs and cats need to enter Luxembourg from within and outside the EU.",
"date": "2026-05-06",
"tags": ["Luxembourg", "pet import", "EU pet travel"],
"faqs": [
{"question": "Does Luxembourg require anything beyond the standard EU pet passport?", "answer": "No additional requirements apply beyond standard EU rules. Pets from EU countries need a valid EU Pet Passport, microchip, and current rabies vaccination. Pets from non-EU countries (including the UK) additionally need an AHC and tapeworm treatment for dogs."},
{"question": "Is there a vet available at Luxembourg Airport for pet arrivals?", "answer": "Luxembourg Airport (LUX) is a small international airport and handles live animal imports through its border inspection post. For large pet cargo operations, Brussels Airport (BRU) in Belgium (about 200 km away) has larger facilities. Check with your airline which airport handles your specific cargo routing."},
{"question": "Are there any breed bans in Luxembourg?", "answer": "Luxembourg has legislation on dangerous dogs. Certain breeds including Pit Bull Terriers, Staffordshire Bull Terriers, American Staffordshire Terriers, and Rottweilers are subject to additional registration requirements, muzzle and leash requirements in public, and some import restrictions. Verify current Luxembourg legislation before importing a restricted breed."}
],
"body": """
Luxembourg is one of Europe's smallest countries but also one of its most internationally connected -- it hosts numerous EU institutions and international companies, and expats make up a significant portion of the population. Pet moves into Luxembourg follow standard EU rules, with one area of caution: restricted breed legislation.

## EU Arrivals: Standard Rules

From another EU member state:

- Microchip (ISO standard)
- EU Pet Passport
- Current rabies vaccination

Luxembourg's ASTA (Administration des services veterinaires) manages live animal import oversight.

## Non-EU Arrivals (Including the UK)

- Microchip (ISO 11784/11785)
- Rabies vaccination (at least 21 days before first EU entry if first vaccine)
- AHC issued within 10 days of entry
- Tapeworm treatment for dogs (1 to 5 days before entering any EU member state)

## Restricted Breeds: Read Before You Move

Luxembourg's 2004 law on dangerous animals covers several breeds. If you are bringing a Rottweiler, Pit Bull, American Staffordshire Terrier, Tosa Inu, Dogo Argentino, or Fila Brasileiro, you need to research Luxembourg's current breed requirements carefully.

Restricted breed owners typically need:
- Registration with Luxembourg ASTA
- Liability insurance
- Muzzle and leash in public spaces
- In some cases, proof of behavioural assessment

This is not an outright import ban for most breeds, but the compliance requirements are real and enforced.

## Living in Luxembourg with Pets

Luxembourg is a compact, pet-friendly country. Parks and trails are well-maintained, vets are generally excellent (many speak English, French, and German), and there is no shortage of pet services in the capital.

Annual rabies vaccination is required for dogs. Register your pet with your Commune within 30 days of residence.

## Useful Contacts

- **ASTA (Luxembourg veterinary authority)**: asta.etat.lu
- **EU TRACES movement certificates**: traces.ec.europa.eu

*Information current as of May 2026. Verify breed restriction rules directly with ASTA.*
"""
},

{
"slug": "indonesia-pet-import-guide",
"title": "Bringing Pets to Indonesia: Import Rules for Expats Moving to Bali or Jakarta",
"description": "Indonesia requires advance import permits, microchipping, and rabies vaccination for pet imports. Bali has stricter rules than other islands. Here is what expats need to know.",
"date": "2026-05-06",
"tags": ["Indonesia", "pet import", "Bali", "expat pet travel"],
"faqs": [
{"question": "Does Bali allow pet imports from the UK or Australia?", "answer": "Bali (Denpasar, Ngurah Rai Airport) accepts pet imports, but the island's quarantine rules are stricter than other parts of Indonesia due to Bali's rabies-free status historically being contested. As of 2026, Bali is not a designated rabies-free zone under Indonesian law, but authorities apply extra scrutiny to incoming animals. Jakarta (CGK) or another Javanese port of entry may be simpler for first-time pet imports to Indonesia."},
{"question": "What authority controls pet imports into Indonesia?", "answer": "The Ministry of Agriculture through its Agricultural Quarantine Agency (BARANTAN) manages all live animal imports into Indonesia. Import permits must be obtained from BARANTAN before the animal travels."},
{"question": "How long is quarantine in Indonesia for imported pets?", "answer": "Indonesia typically requires 7 to 14 days of quarantine for imported dogs and cats, depending on the country of origin and the documentation presented. The quarantine is conducted at a BARANTAN facility at the port of entry."}
],
"body": """
Indonesia is home to hundreds of thousands of expats across Bali, Jakarta, Surabaya, and other cities. Moving a pet to Indonesia is achievable, but the process requires advance planning, particularly around the import permit and quarantine requirements.

## The Core Authority: BARANTAN

All pet imports are controlled by the Agricultural Quarantine Agency of Indonesia (BARANTAN). Your first step is to secure an import permit from BARANTAN before your pet travels. The permit specifies the entry point -- your actual travel must match it.

Apply at karantina.pertanian.go.id at least 4 to 6 weeks before intended travel.

## What You Need

1. **Import permit** from BARANTAN (applied for in advance)
2. **Microchip** (ISO 11784/11785 strongly recommended)
3. **Rabies vaccination** -- current, administered at least 14 to 30 days before entry (check current BARANTAN guidance for exact timing)
4. **Rabies titre test** -- required from most countries. Blood drawn from an approved lab; result must show adequate antibody level
5. **Health certificate** -- issued by a government-accredited vet in your country of origin, endorsed by your national authority (APHA for UK, USDA for USA, DAFF for Australia)
6. **Parasite treatment** records (flea, tick, deworming within specified windows)

## Quarantine on Arrival

Expect 7 to 14 days of quarantine at the designated BARANTAN facility. Quarantine facilities vary by port of entry -- Jakarta Soekarno-Hatta (CGK) has the best-equipped facility.

During quarantine, your pet will be:
- Checked by a BARANTAN vet
- Held in the quarantine kennel
- Released when the quarantine period completes and all documentation is verified

## Entry Points

- **Jakarta Soekarno-Hatta (CGK)**: The main entry point, best-equipped quarantine facility
- **Bali Ngurah Rai (DPS)**: Accepts imports but stricter scrutiny applies; some agents recommend CGK as a safer first entry point
- **Surabaya Juanda (SUB)**: Also accepts pets with BARANTAN facilities on-site

## Using an Agent

Given the complexity and the Indonesian language documentation involved, most expats use a specialist pet relocation agent with Indonesia experience. Agents in Jakarta and Bali handle this route regularly and manage the BARANTAN permit process on your behalf.

## Practical Life with Pets in Indonesia

- Rabies is present in most Indonesian provinces; keep your pet's vaccination current at all times
- Reliable veterinary care is available in Jakarta and south Bali (Kuta, Seminyak, Ubud areas)
- Heat management is important for cold-weather breeds -- consult your vet before travelling

*Always verify current BARANTAN requirements before making bookings. This guide reflects conditions as of May 2026.*
"""
},

{
"slug": "tanzania-pet-import-guide",
"title": "Moving to Tanzania with Pets: Import Permits and Vet Requirements",
"description": "Tanzania requires an import permit, health certificate, and current vaccinations for pet imports. Here is what dog and cat owners need to know before moving to Dar es Salaam or Arusha.",
"date": "2026-05-06",
"tags": ["Tanzania", "pet import", "Africa pet travel"],
"faqs": [
{"question": "Do I need a permit to bring a pet to Tanzania?", "answer": "Yes. An import permit from the Tanzania Veterinary Council or the Ministry of Agriculture and Livestock Development is required before your pet travels. Apply at least four to six weeks before the intended travel date."},
{"question": "Is there quarantine for pets arriving in Tanzania?", "answer": "Tanzania may require a short inspection and holding period at Julius Nyerere International Airport (DAR) in Dar es Salaam depending on documentation completeness and the animal's health. A mandatory quarantine of several days may apply for animals from certain origins. Confirm current requirements with the Ministry of Livestock Development."},
{"question": "What vaccinations does Tanzania require for imported pets?", "answer": "Rabies vaccination is mandatory. Dogs should also be vaccinated against distemper, parvovirus, and leptospirosis. Cats need FVRCP vaccination. All vaccines must be current and recorded in the health certificate issued by an official vet."}
],
"body": """
Tanzania is East Africa's largest country and home to a significant expat community in Dar es Salaam, Arusha, and the Zanzibar islands. Bringing a pet requires advance permit work and veterinary preparation, but the process is achievable with the right planning.

## Import Permit: Start Here

Contact the Tanzania Veterinary Council or the Directorate of Veterinary Services at the Ministry of Agriculture and Livestock Development to apply for a pet import permit. You will need:

- Species, breed, age, sex, and microchip number of your pet
- Your passport details and intended Tanzanian address
- Copies of current vaccination certificates

Allow at least four to six weeks for permit processing.

## Health Certificate

An official health certificate, issued by an accredited vet in your home country and endorsed by your national authority (APHA for UK, USDA for USA, DAFF for Australia), is required. The certificate should:

- Be issued within 14 days of travel
- List all current vaccinations and their expiry dates
- Include microchip number
- Confirm the animal is free from external parasites
- Reference the Tanzania import permit number

## Recommended Vaccinations

**Dogs:**
- Rabies (mandatory)
- Distemper, Parvovirus, Hepatitis, Leptospirosis
- Kennel Cough (Bordetella) recommended

**Cats:**
- Rabies
- FVRCP

All vaccinations should be current at time of entry.

## Entry at Dar es Salaam

Julius Nyerere International Airport (DAR) is the main point of entry. The airport has a Veterinary Services inspection office. On arrival, the border vet will check the import permit, health certificate, and microchip. Keep all originals accessible.

## Zanzibar Note

Zanzibar is a semi-autonomous island within Tanzania. Bringing pets to Zanzibar involves an additional layer of administration beyond the mainland permit. If your destination is Zanzibar rather than the mainland, confirm specifically with the Zanzibar government's veterinary authority, as different regulations may apply.

## Health Risks for Pets in Tanzania

- Tick-borne diseases are a significant risk -- monthly tick prevention is essential
- Bilharzia, trypanosomiasis, and other tropical diseases can affect dogs
- Good veterinary care is available in Dar es Salaam and Arusha; smaller towns have limited access

*This guide is accurate as of May 2026. Always verify with the Tanzania Ministry of Agriculture and Livestock Development before travel.*
"""
},

{
"slug": "bangladesh-pet-import-guide",
"title": "Bringing Pets to Bangladesh: What the Import Rules Actually Require",
"description": "Bangladesh has specific requirements for pet imports including health certificates, rabies vaccination, and customs declarations. Here is a practical guide for expats moving to Dhaka.",
"date": "2026-05-06",
"tags": ["Bangladesh", "pet import", "South Asia pet travel"],
"faqs": [
{"question": "Is there a dedicated pet import process in Bangladesh?", "answer": "Bangladesh does not have a streamlined online pet import system. Imports are managed through the Department of Livestock Services (DLS) and customs at Hazrat Shahjalal International Airport (DAC). Personal imports by returning residents or expats are typically handled as accompanied personal effects, but veterinary inspection on arrival is standard."},
{"question": "What vaccinations does Bangladesh require for pet imports?", "answer": "Rabies vaccination is the core requirement. Dogs should additionally have distemper, parvovirus, and hepatitis vaccines. All vaccinations must be current and documented in an official health certificate from your country of origin."},
{"question": "Is there quarantine for pets arriving in Bangladesh?", "answer": "Bangladesh does not operate a formal mandatory quarantine facility for household pets. However, pets arriving without complete documentation may be detained at the airport while issues are resolved. Complete paperwork significantly reduces the risk of delays."}
],
"body": """
Bangladesh is not one of the more common expat pet destinations, but international development workers, UN staff, and corporate expats in Dhaka do bring their animals. The formal system for pet imports is less codified than in many countries, which actually means flexibility -- but also uncertainty.

## The Key Authority: DLS

The Department of Livestock Services (DLS) under the Ministry of Fisheries and Livestock manages veterinary import matters. There is no straightforward online permit system as of 2026. The most reliable approach is:

1. Contact the Bangladesh High Commission or Embassy in your country before travel for current guidance
2. Contact the DLS in Dhaka directly (available via the Ministry of Fisheries and Livestock website)
3. Use a specialist pet relocation agent with Bangladesh experience, who will have contacts within DLS and customs

## What You Need

1. **Microchip** (ISO 11784/11785 recommended)
2. **Rabies vaccination** -- current
3. **Official health certificate** -- issued by an official vet in your home country, endorsed by your national authority
4. **Customs declaration** -- list your pet on your customs arrival form as an accompanying personal item
5. **Vaccination booklet/EU Pet Passport or equivalent** -- bring the original documentation plus copies

## On Arrival at Dhaka (DAC)

Hazrat Shahjalal International Airport (DAC) is the main international entry point. DLS vets at the airport will inspect documentation. Keep original certificates accessible. If anything is missing or unclear, the pet may be temporarily held in the airport's holding area -- a stressful but usually resolvable situation.

## Practical Considerations

- Dhaka has several competent private veterinary practices; ask your employer or the British High Commission for recommendations
- Heat and humidity are significant factors -- brachycephalic breeds need particular care
- Rabies is present in Bangladesh; keep vaccinations current throughout your stay
- Departing with your pet requires an export permit from DLS when you eventually leave

*This guide reflects conditions as of May 2026. The Bangladesh pet import process can change with little notice -- contact DLS and your country's embassy before travel.*
"""
},

# ── ROUTE GUIDES ──────────────────────────────────────────────────────────

{
"slug": "uk-to-ireland-pet-transport-guide",
"title": "Pet Transport from the UK to Ireland: An Easier Route Than You Might Expect",
"description": "Moving from Britain to Ireland with a dog or cat? Ireland stays in the EU, which creates a simple process for pets -- but the Common Travel Area means different rules than other EU moves.",
"date": "2026-05-06",
"tags": ["UK to Ireland", "pet transport", "Ireland pet import"],
"faqs": [
{"question": "Does the UK to Ireland pet travel route require a full EU Animal Health Certificate?", "answer": "Pets travelling from Great Britain to Ireland do need to meet EU pet entry requirements, including a microchip, valid rabies vaccination, and either an EU-issued Pet Passport or an Animal Health Certificate (AHC). However, travel via land/sea routes from Northern Ireland to the Republic of Ireland operates under different arrangements. Contact the DAFM (Ireland) for the current position."},
{"question": "What routes can I use to take a pet from the UK to Ireland?", "answer": "Main pet-friendly routes include: ferry from Holyhead to Dublin (Irish Ferries, Stena Line), Fishguard or Pembroke to Rosslare (Irish Ferries, Stena Line). Some ferries allow pets in vehicles or in designated pet kennels on board. All routes require pre-booking a pet space."},
{"question": "Is there quarantine for pets entering Ireland from Britain?", "answer": "No. Ireland does not impose quarantine on pets entering from Great Britain if the EU pet travel requirements are met. Ireland (the Republic) follows EU pet passport rules as an EU member, but applies some specific rules around tapeworm treatment for dogs. Verify current DAFM guidance before travel."}
],
"body": """
The UK to Ireland route has an unusual set of rules. Ireland is an EU member but shares the Common Travel Area with the UK, which creates a different situation than most UK-to-EU moves. For most travellers, it is simpler than moving to France or Spain -- but there are nuances to understand.

## Ireland's Position: EU Member, Not Schengen

Ireland is an EU member but not part of the Schengen Area (it opted out). This means:
- EU pet travel rules apply (microchip, rabies vaccination)
- Ireland has its own border controls
- The Northern Ireland / Republic of Ireland border is a special case

## What You Need to Move from Great Britain to Ireland

Since Brexit, pets moving from Great Britain (England, Scotland, Wales) to the Republic of Ireland are moving from a non-EU country into an EU member state. The requirements are:

1. **Microchip** (ISO 11784/11785)
2. **Rabies vaccination** -- current, administered at least 21 days before first EU entry if a new vaccine
3. **Animal Health Certificate (AHC)** or valid EU-issued Pet Passport
4. **Tapeworm treatment** (dogs only) -- 1 to 5 days before arrival in Ireland, recorded in the AHC

The AHC must be issued by a UK Official Veterinarian (OV) within 10 days of the pet's arrival in Ireland.

## Northern Ireland to Republic of Ireland

This route is different. Under the Windsor Framework, Northern Ireland maintains EU single market alignment for animal and plant products. Pets moving from Northern Ireland to the Republic of Ireland may use EU Pet Passports issued in Northern Ireland. This is a complex area -- contact DAERA (Northern Ireland) and DAFM (Republic of Ireland) for current guidance if this applies to you.

## Ferry Routes and What to Expect

The main ferry routes are practical and pet-friendly:

**Holyhead to Dublin** (Irish Ferries, Stena Line): 3.5 to 4 hour crossing. Pets travel in the vehicle deck in your car, or in the ship's pet kennel area if you are a foot passenger.

**Fishguard to Rosslare** (Stena Line): approximately 3.5 hours. Same arrangements.

**Pembroke to Rosslare** (Irish Ferries): approximately 4 hours.

Pre-book your pet's place. Ferry operators have a limited number of pet kennels for foot passengers. If you are driving, your pet stays in your vehicle -- a much calmer option.

## Irish Registration

Once in Ireland, dogs must be licensed annually (under the Control of Dogs Act 1986). Your local county council manages this. Microchip registration in the Republic of Ireland is managed through the national microchip database -- update your details when you arrive.

## Useful Contacts

- **DAFM Ireland (Department of Agriculture, Food and the Marine)**: gov.ie/agriculture
- **Irish Ferries pet travel**: irishferries.com
- **Stena Line pet travel**: stenaline.co.uk
- **APHA (UK)**: apha.defra.gov.uk

*Rules around the UK-Ireland route have evolved since Brexit and continue to develop. Always check the latest guidance from DAFM before travel. Information current as of May 2026.*
"""
},

{
"slug": "japan-to-uk-pet-transport-guide",
"title": "Pet Transport from Japan to the UK: What the Return Journey Requires",
"description": "Moving from Japan to the UK with a dog or cat? Japan exports are straightforward for UK entry. Here is what documents you need and how to book the journey.",
"date": "2026-05-06",
"tags": ["Japan to UK", "pet transport", "UK pet import from Japan"],
"faqs": [
{"question": "Is Japan on the UK's approved country list for pet imports?", "answer": "Yes. Japan is on Great Britain's Part 1 listed countries, which means dogs and cats from Japan can enter the UK without a rabies titre test. You need a microchip, current rabies vaccination, a health certificate from a Japanese official vet, and tapeworm treatment for dogs."},
{"question": "What Japanese authority issues the export health certificate for pets?", "answer": "The Ministry of Agriculture, Forestry and Fisheries (MAFF) in Japan oversees animal exports. Your vet in Japan prepares the health certificate, which is then endorsed by MAFF. Allow 5 to 10 working days for MAFF processing."},
{"question": "Which airlines fly pets from Japan to the UK?", "answer": "British Airways (from Tokyo Haneda or Narita to London Heathrow), Japan Airlines (JAL, as cargo), and ANA (All Nippon Airways, as cargo) are the main options for the Japan-UK route. In-cabin pet acceptance is typically only for very small animals on select routes. Larger pets travel as accompanied cargo in the hold."}
],
"body": """
If you have survived the notoriously complex process of bringing a pet into Japan, you will find the return journey to the UK considerably more straightforward. Japan is on the UK's listed countries table, which eliminates the titre test requirement on the UK side.

## UK Entry Requirements for Pets from Japan

Since Japan is Part 1 listed under UK pet travel rules, the requirements are:

1. **Microchip** (ISO 11784/11785)
2. **Rabies vaccination** -- current (at least 21 days before travel if first vaccine; if your pet had a booster in Japan, this is already satisfied)
3. **Animal Health Certificate (AHC)** -- issued by a MAFF-accredited Japanese vet and endorsed by MAFF, within 10 days of arrival in Great Britain
4. **Tapeworm treatment** (dogs only) -- 1 to 5 days before arriving in Great Britain, recorded in the AHC

## Getting the AHC in Japan

Ask your vet in Japan about preparing an export health certificate for Great Britain. Not all vets in Japan are MAFF-accredited for export certification, so check in advance. The MAFF endorsement can take 5 to 10 business days, so schedule the vet appointment accordingly within the 10-day window before travel.

MAFF regional offices handle endorsement. Your vet should be familiar with the process; if not, contact MAFF directly at maff.go.jp.

## Flight Options

The Tokyo to London route is well-served:
- **British Airways** (Haneda/Narita to Heathrow): accepts pets as accompanied excess baggage in the hold on many flights. Confirm in advance as not all operated flights accept animals.
- **Japan Airlines (JAL)**: Accepts pets as cargo. Book through JAL Cargo.
- **ANA**: Accepts pets as cargo on international routes from Narita.

The flight time is approximately 11 to 12 hours non-stop. Both Tokyo airports (NRT and HND) have established live animal handling facilities.

## What Your Pet Experienced in Japan

If your pet lived in Japan for several years, they are accustomed to a structured, clean environment. The UK adjustment is generally smooth -- the climate is wetter and cooler, but the regulatory requirements are familiar.

## On Arrival in the UK

APHA veterinary inspectors at Heathrow's live animal facility will check:
- Microchip (scanned)
- Rabies vaccination date (must be within validity)
- AHC (dates, endorsement, tapeworm treatment record for dogs)

Allow extra time at the airport. Live animal arrivals at Heathrow go through a separate facility.

*This guide is accurate as of May 2026. Always verify with APHA and MAFF before travel.*
"""
},

{
"slug": "italy-to-uk-pet-transport-guide",
"title": "Pet Transport from Italy to the UK: Post-Brexit Requirements for EU Pets",
"description": "Moving from Italy to the UK with a pet after Brexit? EU-issued Pet Passports are currently accepted. Here is what you need: tapeworm treatment, microchip, and current rabies vaccination.",
"date": "2026-05-06",
"tags": ["Italy to UK", "pet transport", "EU to UK pet travel"],
"faqs": [
{"question": "Can I use an Italian EU Pet Passport to enter the UK?", "answer": "Currently yes -- EU-issued Pet Passports are accepted for entry into Great Britain from EU countries including Italy. However, the UK government has signalled this arrangement may change. Always check the latest APHA guidance before travel, as the position has evolved since Brexit."},
{"question": "Does my dog need tapeworm treatment before entering Britain from Italy?", "answer": "Yes. Dogs entering Great Britain must have a tapeworm (Echinococcus) treatment administered 1 to 5 days before arrival. This is a fixed UK requirement, regardless of origin country. The treatment must be given by a vet and recorded in the EU Pet Passport or AHC."},
{"question": "What ferry or flight options are there from Italy to the UK with a pet?", "answer": "Most pet owners travel from Italy to the UK by flying, with Italian pets usually going as accompanied cargo. Alitalia/ITA Airways, British Airways, and Ryanair all fly Italian routes to the UK. Driving via France and the Channel Tunnel (Eurotunnel) is also an option but adds significant travel time."}
],
"body": """
Thousands of people move from Italy to the UK every year -- returning British expats, Italian nationals with UK roots, families moving for work or study. Moving a pet on this route requires understanding both what Italy needs for export and what the UK needs on arrival.

## Current Rules: EU Pet Passport Accepted

As of May 2026, Italy-issued EU Pet Passports are accepted for entry into Great Britain. This makes the move simpler than the reverse journey (UK to Italy), where UK-issued passports are no longer valid.

What your pet needs for UK entry from Italy:

1. **Microchip** (ISO 11784/11785)
2. **Valid EU Pet Passport** (Italian-issued)
3. **Current rabies vaccination** (within validity period shown on the data sheet)
4. **Tapeworm treatment** (dogs only) -- administered by a vet 1 to 5 days before UK arrival, recorded in the passport

## Important Warning: This May Change

The UK government has reserved the right to change the EU Pet Passport acceptance policy. The current arrangement is not guaranteed to continue. Check gov.uk/bring-pet-to-great-britain before every trip.

## Getting Italian Pets Ready

If your pet's rabies vaccination is close to expiry, get a booster from an Italian vet before departure. A lapsed vaccine at the UK border causes real problems. The booster date must be within the validity window shown on the vaccine data sheet in the passport.

## Travel Routes

**By air:**
- ITA Airways, British Airways, and Ryanair fly the main Italian cities (Rome, Milan, Venice, Naples) to UK airports
- For pets travelling in the hold, ITA Airways and British Airways are the better-established options
- Book pet spaces well in advance; availability is limited

**By road and Eurotunnel:**
- Driving from Italy through France takes a day and a half minimum (Mont Blanc or Frejus tunnel into France, then north to Calais)
- Eurotunnel from Calais to Folkestone accepts pets in the vehicle
- The same rules apply for UK entry regardless of the route used

## Deregistering in Italy

If permanently leaving Italy, deregister your dog from the Italian microchip database (BDN) or your local ASL. This avoids future registration charges. Your Italian vet can help with this.

## After Arriving in the UK

APHA inspectors at the approved route entry point will check the passport and tapeworm treatment records. Keep originals accessible. After arrival, update the microchip registration to a UK database (Petlog or similar) with your UK address.

*Always verify the latest rules at gov.uk/bring-pet-to-great-britain. This guide is current as of May 2026.*
"""
},

{
"slug": "south-korea-to-australia-pet-transport-guide",
"title": "Pet Transport from South Korea to Australia: Step by Step",
"description": "South Korea is on Australia's approved country list for pet imports. Here is the full process: titre test, 180-day wait, import permit, and Melbourne quarantine.",
"date": "2026-05-06",
"tags": ["South Korea to Australia", "pet transport", "Australia quarantine"],
"faqs": [
{"question": "Is South Korea on Australia's approved country list?", "answer": "Yes. South Korea (Republic of Korea) is on DAFF's approved country list for pet imports to Australia. This means dogs and cats can travel directly from South Korea to Australia without a third-country intermediary -- but all health protocols including the rabies titre test and 180-day wait still apply."},
{"question": "What is the minimum preparation time for moving a pet from Korea to Australia?", "answer": "Approximately 7 to 9 months. The process includes microchipping, two rabies vaccinations (with the required interval), a titre test blood draw, a 180-day wait from the blood draw date, and import permit processing. Start as soon as your move is confirmed."},
{"question": "Which Korean laboratory can do the rabies titre test for Australia?", "answer": "The blood must be sent to an OIE-approved reference laboratory. Korean vets typically send blood to approved labs in the UK, South Africa, or the USA. The Korean Animal and Plant Quarantine Agency (APQA) can advise on current approved labs and procedures."}
],
"body": """
South Korea is one of the cleanest starting points for a move to Australia -- it is on DAFF's approved list, the veterinary system is excellent, and there are direct flights from Incheon to Melbourne. But Australia's biosecurity requirements apply regardless of origin, which means the process still takes the best part of a year.

## The Full Preparation Timeline

### 7+ months before travel:

1. **Microchip** (ISO 11784/11785) -- if not already done
2. **First rabies vaccination** -- at least 90 days before titre test blood draw
3. **Second rabies vaccination** -- at least 30 days after first vaccine
4. **Rabies titre test (FAVN)** -- blood drawn at least 90 days after first vaccine, sent to an OIE-approved lab
5. **Confirm positive titre result** (0.5 IU/mL or higher)
6. **180-day wait begins** from blood draw date

### 3+ months before travel:

7. **Apply for Australian import permit** via DAFF's BICON system (bicon.agriculture.gov.au)
8. **Book quarantine slot** at Mickleham, Victoria (DAFF arranges after permit approval)
9. **Keep rabies vaccination current** throughout the wait period

### Within 10 days of travel:

10. **Official health certificate** -- issued by a Korean APQA-accredited vet and endorsed by APQA
11. **Book Melbourne flight** -- only Melbourne Tullamarine (MEL) accepts pets for Australian quarantine

## The Korean Veterinary System

Korea has an excellent small animal veterinary sector, particularly in Seoul and major cities. Finding an APQA-accredited export vet is straightforward. APQA (the Animal and Plant Quarantine Agency) is the relevant authority -- apqa.go.kr.

The APQA endorsement of your health certificate is the equivalent of the USDA or APHA endorsement in other countries. Allow 3 to 5 working days.

## Direct Flights: Seoul to Melbourne

Korean Air and Qantas both operate the Incheon (ICN) to Melbourne (MEL) route. Both accept pets, though cargo procedures differ. Korean Air has an established PET program. Confirm with the airline's cargo department -- not every operated flight on a route accepts live animals.

## Melbourne Quarantine

All pets entering Australia spend 10 days at the Mickleham facility near Melbourne. DAFF-trained staff care for animals during the quarantine. Costs are government-set and charged per animal per day. Your pet is examined daily and released after the quarantine period if all health checks pass.

After quarantine, you can arrange a domestic flight or road transfer to your final destination anywhere in Australia.

*This guide reflects DAFF requirements as of May 2026. Always verify at bicon.agriculture.gov.au before starting the process.*
"""
},

{
"slug": "canada-to-usa-pet-transport-guide",
"title": "Moving Pets from Canada to the USA: A Simpler Process Than You Might Expect",
"description": "The Canada-to-USA border is one of the more straightforward for pet travel. Here is what the CDC and USDA require for dogs and cats crossing from Canada.",
"date": "2026-05-06",
"tags": ["Canada to USA", "pet transport", "cross-border pet travel"],
"faqs": [
{"question": "Do dogs need a rabies certificate to enter the USA from Canada?", "answer": "Yes. Dogs entering the USA from Canada must have a current rabies vaccination certificate. The CDC requires dogs to be vaccinated against rabies. The certificate must show the dog's description, vaccination date, and expiry date. A microchip is strongly recommended and required if the dog has been outside the USA prior to entering Canada."},
{"question": "Can I drive across the US-Canada border with my pet?", "answer": "Yes. The land border between Canada and the USA is commonly used for pet travel by car. At the border crossing, you will be asked to declare any animals. CBSA (Canadian side) and CBP (US side) may inspect your pet's documentation. Having the rabies certificate and health records accessible significantly speeds up the crossing."},
{"question": "Are there any breed restrictions at the US-Canada border?", "answer": "The USA does not have a federal breed ban for dogs. However, some US states have breed-specific legislation that applies locally. Canada has no federal breed ban (though some provinces did historically -- Ontario's pit bull ban was amended). Research your specific US destination state for any local restrictions."}
],
"body": """
Moving pets between Canada and the USA is genuinely one of the world's simpler international pet moves. The two countries share a long land border, have closely aligned veterinary systems, and the CDC's dog import rules are relatively streamlined for dogs with full US vaccination history.

## What the USA Requires for Dogs from Canada

The CDC (Centers for Disease Control) governs dog imports into the USA:

1. **Rabies vaccination** -- current certificate (must be valid on date of entry)
2. **Microchip** -- required for dogs that have been in certain high-risk countries previously (less relevant for Canada-to-USA moves if the dog has lived only in Canada and the USA)
3. **Health certificate** -- a standard veterinary health certificate is recommended; required by most airlines but not always at land borders

For dogs that have been in countries outside Canada and the USA, CDC's enhanced dog import requirements may apply. Check current CDC guidance at cdc.gov/importation/dogs.html.

## What the USA Requires for Cats

No health certificate or rabies vaccination is federally required for cats entering the USA from Canada. However:
- Individual states may have requirements
- Airlines require a health certificate for all pets
- A current rabies vaccination is good practice and may be required by your destination state

## Land Border Crossings

Crossing by car is the most common route. At the crossing:
- Declare your pets on the CBSA (leaving Canada) and CBP (entering the USA) forms
- Have the rabies certificate and any health records accessible
- CBP may ask basic questions about the animal (species, age, vaccination status)
- Physical inspection is uncommon for pets with complete documentation

Busy crossings (Windsor-Detroit, Niagara, Peace Bridge) are generally efficient. Smaller crossings may have fewer staff but often shorter queues.

## Flying from Canada to the USA

For air travel:
- Most airlines require a health certificate issued within 10 days of travel
- Cabin pet policies vary significantly by airline -- Air Canada, WestJet, and US carriers each have different rules
- Check the specific airline's policy before booking

## Moving to Hawaii

Hawaii is a separate case. Despite being a US state, Hawaii's biosecurity rules mean that even pets from Canada need to meet Hawaii's full import program requirements (titre test, specific waiting period). Pets cannot simply fly from Canada to Hawaii as a domestic US move. See the HDOA website (hdoa.hawaii.gov) for full Hawaii requirements.

## After Crossing: State Registration

Some US states require dogs to be licensed with the local county or city within a specified period of establishing residency. Annual rabies vaccination is required by most states. Check your destination state's requirements.

*This guide is accurate as of May 2026. CDC dog import rules change -- verify at cdc.gov/importation before travel.*
"""
},

# ── BREED GUIDES ──────────────────────────────────────────────────────────

{
"slug": "travelling-with-a-persian-cat-internationally",
"title": "Travelling Internationally with a Persian Cat: Breed Considerations and Practical Advice",
"description": "Persian cats are beautiful but have compressed faces that make air travel riskier. Here is what Persian cat owners need to know before planning an international move.",
"date": "2026-05-06",
"tags": ["Persian cat", "brachycephalic cat", "cat air travel"],
"faqs": [
{"question": "Are Persian cats allowed on international flights?", "answer": "Many airlines restrict or ban flat-faced (brachycephalic) breeds including Persians from travelling in the hold due to respiratory risks. Some airlines also restrict them from the cabin. Check the specific airline policy for Persian cats before booking -- policies vary significantly."},
{"question": "Why are Persian cats considered higher risk for air travel?", "answer": "Persian cats are brachycephalic -- they have shortened skulls and compressed airways. Under the stress of air travel, their breathing effort increases. Combined with potential heat stress in a cargo hold and reduced oxygen levels during flight, Persians face a higher risk of respiratory distress than non-brachycephalic cats."},
{"question": "What is the safest way to move a Persian cat internationally?", "answer": "Cabin travel (if the cat is small enough to fit under the seat) is safer than hold travel for Persians. If the cat must travel in the hold, choose an airline known for good live animal handling, travel in cooler months, choose the shortest possible route, and get a specific fitness-to-fly assessment from a vet familiar with brachycephalic breeds."}
],
"body": """
Persian cats are one of the most popular breeds in the world -- calm, affectionate, and adaptable to indoor living. They are also one of the breeds most commonly flagged for air travel risk, due to their flat faces and the breathing challenges that come with them.

## The Brachycephalic Factor

Persians have been selectively bred for a flattened facial structure over generations. This results in:
- Narrowed nostrils
- Elongated soft palate
- Narrowed trachea in some cases
- Prone to overheating (panting is less efficient for them)

Under normal conditions, most Persians breathe adequately. Under the stress of travel -- noise, confinement, unfamiliar smells, temperature changes -- their already-compromised airways are under increased demand. This is why airlines apply restrictions.

## Airline Policies for Persian Cats

Airline policies for brachycephalic cats are less uniformly restrictive than for dogs, but restrictions do exist:

- **US carriers** (United, American, Delta) typically list Persians on restricted breed lists for cargo hold travel
- **Many European carriers** have no blanket Persian ban but apply health certificate requirements and veterinary sign-off more strictly
- **Some Asian and Middle Eastern carriers** still accept Persians in cargo under specific conditions

Always contact the specific airline directly and ask about Persian cats by name. Get written confirmation.

## In-Cabin vs Hold for Persians

If your Persian is small enough to travel in cabin (typically under 5 to 6 kg as an adult), this is the preferred option. In cabin:
- Temperature is controlled to passenger comfort levels
- You can monitor your cat throughout the flight
- The stress profile is lower than solo hold travel

Adult Persians often exceed cabin weight limits (most airlines cap combined pet-plus-carrier weight at 6 to 8 kg). A large Persian can be 6 kg before the carrier is added.

## Pre-Travel Vet Assessment

Before any international flight with a Persian, have your vet assess specifically for:

- Degree of BOAS (Brachycephalic Obstructive Airway Syndrome) severity
- Heart function (Persians can have HCM -- hypertrophic cardiomyopathy)
- General fitness to fly

A fitness-to-fly declaration from your vet is worth having, even if not required. It documents your due diligence.

## Sedation: Use Caution

Sedatives are generally not recommended for brachycephalic cats. Sedation reduces muscle tone, which can worsen airway obstruction. If you and your vet decide a sedative is appropriate, use only a product specifically approved for cats and specifically at a dose for a brachycephalic animal. This is not a decision to make unilaterally based on general internet advice.

## Country-Specific Breed Restrictions

Persians are not banned by any country's import regulations -- the restrictions are from airlines, not governments. Country import requirements are the same as for any cat: microchip, rabies vaccination, health certificate.

*Always check the specific airline policy for Persian cats before booking. Policies change. Information current as of May 2026.*
"""
},

{
"slug": "travelling-with-a-cavalier-king-charles-spaniel-internationally",
"title": "Travelling Internationally with a Cavalier King Charles Spaniel",
"description": "Cavalier King Charles Spaniels are gentle travellers but have brachycephalic and cardiac health considerations. Here is what CKCS owners need to know for international pet moves.",
"date": "2026-05-06",
"tags": ["Cavalier King Charles Spaniel", "CKCS", "dog travel", "brachycephalic"],
"faqs": [
{"question": "Are Cavalier King Charles Spaniels restricted for air travel?", "answer": "Some airlines include Cavaliers on their restricted brachycephalic breed lists due to their shortened muzzles. However, CKCSs are less severely brachycephalic than English Bulldogs or Pugs. Many airlines accept them in the hold with health certification; some accept them in cabin. Check the specific airline policy before booking."},
{"question": "What health conditions should I flag when travelling with a CKCS?", "answer": "Cavaliers have a high prevalence of mitral valve disease (MVD) and syringomyelia/Chiari-like malformation. Before any international flight, have your vet assess heart function and neurological status specifically. MVD can make physical stress more dangerous. A vet fitness-to-fly letter is strongly recommended."},
{"question": "Are Cavalier King Charles Spaniels banned in any countries?", "answer": "No. Cavaliers are not on any country's restricted or banned breed list. Normal pet import requirements (microchip, vaccination, health certificate) apply. The breed restrictions come from airlines, not from government import rules."}
],
"body": """
Cavalier King Charles Spaniels are one of Britain's most beloved breeds -- gentle, sociable, and well-suited to family life. For international relocation, they occupy a grey zone: partially brachycephalic (which creates airline complications), but less severely so than Bulldogs or Pugs. The bigger health concern for most CKCSs travelling internationally is cardiac, not respiratory.

## Brachycephalic Status: Partially Restricted

CKCSs have shorter muzzles than non-brachycephalic breeds, but they are not as compressed as English Bulldogs or French Bulldogs. This means:

- Some airlines list them on restricted breed lists (check each airline individually)
- Others accept them without special restriction
- The risk profile during travel is real but manageable for most CKCSs

Before booking, contact the airline directly and ask specifically about Cavalier King Charles Spaniels. Get the answer in writing.

## Heart Health: The Greater Concern

Mitral valve disease (MVD) is extremely common in the breed -- studies suggest the majority of CKCSs will develop some degree of MVD by age 10. For travel purposes:

- Have your vet assess heart function with a stethoscope before any international flight
- Echocardiography is ideal if your dog is middle-aged or older
- A vet fitness-to-fly letter is strongly recommended, specifically referencing cardiac status
- Avoid travel in extreme heat with a cardiac CKCS

Syringomyelia (SM) / Chiari-like malformation is also common. SM-affected dogs may find pressure changes uncomfortable. Discuss this with your vet before booking.

## Cabin vs Hold

CKCSs typically weigh 5 to 8 kg as adults. Many fall within cabin weight limits (5 to 8 kg including carrier, depending on the airline). In-cabin travel is preferable for a brachycephalic dog with any cardiac history. The temperature is more stable and you can monitor your dog throughout the flight.

For larger or heavier Cavaliers, the hold is the option. Choose an airline with a good live animal cargo reputation, avoid summer travel if possible, and crate train thoroughly before travel.

## Crate Training for a CKCS

CKCSs are adaptable and bond strongly with their owners. The separation of hold travel can cause anxiety. Crate training months before travel -- making the crate a genuinely comfortable, positive space -- makes a significant difference to how they handle the journey.

## International Route Planning

No country bans CKCSs. Your route planning focuses on:
- Which airlines on your specific route accept the breed
- Health fitness before travel (especially cardiac)
- Choosing cooler travel times where possible

*Check airline policies directly and get vet clearance before travel. Information current as of May 2026.*
"""
},

{
"slug": "travelling-with-a-shih-tzu-internationally",
"title": "International Pet Travel with a Shih Tzu: What the Breed Means for Your Journey",
"description": "Shih Tzus are brachycephalic and face airline restrictions for hold travel. Here is a practical guide for Shih Tzu owners planning international relocation.",
"date": "2026-05-06",
"tags": ["Shih Tzu", "brachycephalic dog", "cabin pet travel"],
"faqs": [
{"question": "Can a Shih Tzu travel in the aircraft cabin?", "answer": "In many cases, yes. Adult Shih Tzus typically weigh 4 to 7 kg. Many airlines allow pets in cabin up to 5 to 8 kg combined (pet plus carrier), which means smaller Shih Tzus may qualify. Cabin travel is preferred over hold travel for brachycephalic breeds. Always confirm the specific airline's weight limit and breed policy."},
{"question": "Are Shih Tzus banned from cargo travel?", "answer": "Many major airlines, particularly US carriers, list Shih Tzus on their brachycephalic breed ban for hold/cargo travel. UK and European carriers may have different policies. If your Shih Tzu needs to travel in the hold, research which airlines still accept brachycephalic breeds under specific conditions and get written confirmation before booking."},
{"question": "What is the safest time of year to fly a Shih Tzu internationally?", "answer": "Winter and shoulder seasons (October to November, February to April in the Northern Hemisphere) are safer for brachycephalic breeds like Shih Tzus. High temperatures in cargo holds during summer, combined with the breed's reduced heat tolerance, significantly increase risk. Most airlines that do accept brachycephalic breeds have summer embargoes."}
],
"body": """
Shih Tzus are small, low-shedding dogs that adapt well to apartment living and travel -- which makes them popular among internationally mobile families. The complication is their face. Shih Tzus are brachycephalic, and that affects what airlines will carry them and how safely they travel.

## The Short-Face Problem in Practice

A Shih Tzu's flat face means their airway is compressed. Under normal conditions, most Shih Tzus breathe adequately. Under the stress of travel -- especially warm, pressurised cargo holds with restricted airflow -- breathing becomes harder work. This is the fundamental reason for airline restrictions.

## Cabin Travel: The Best Option

Most adult Shih Tzus weigh 4 to 7 kg. Combined with a carrier (typically 1 to 2 kg), total weight often falls within the 6 to 8 kg cabin limits of many airlines. Cabin travel is significantly safer for brachycephalic dogs:

- Controlled cabin temperature
- You can monitor your dog
- No isolation in a cargo hold
- Less physical stress overall

To travel in cabin, your Shih Tzu needs to fit comfortably in an airline-approved soft carrier under the seat. Measure the under-seat space for your specific aircraft type -- cabin dimensions vary.

## Hold Travel: When Necessary

If your Shih Tzu exceeds cabin weight limits or if the route has no cabin pet option:

- Research which airlines still accept brachycephalic breeds in the hold on your route
- Travel in cooler months
- Choose a non-stop route (shorter hold time is better)
- Get a vet fitness-to-fly assessment
- Use a larger IATA-compliant crate than the minimum size (extra ventilation helps)

US carriers (United, American, Delta) ban most flat-faced breeds from hold travel. UK and European carriers vary. Call the airline and ask specifically about Shih Tzus.

## The Vet Assessment

Before any international flight, have your vet:
- Check for signs of BOAS (airway restriction, stenotic nares, elongated soft palate)
- Confirm fitness to fly in writing
- Discuss whether a heat-tolerant, well-ventilated travel option is appropriate

Some Shih Tzus that have had corrective BOAS surgery (nares widening) tolerate travel better. Document any surgery in the health certificate.

## Country Restrictions

Shih Tzus are not banned in any country. Normal import requirements apply. The challenge is purely the airline, not the destination.

*Check airline policies for your specific route before booking. Brachycephalic breed policies change. Information current as of May 2026.*
"""
},

{
"slug": "travelling-with-a-boxer-internationally",
"title": "Moving Internationally with a Boxer: Breed Restrictions and Travel Tips",
"description": "Boxers are brachycephalic and restricted by most US airlines for cargo travel. Here is a practical guide for Boxer owners planning international pet relocation.",
"date": "2026-05-06",
"tags": ["Boxer", "brachycephalic", "dog relocation", "cargo restrictions"],
"faqs": [
{"question": "Can a Boxer fly in the aircraft cargo hold?", "answer": "Many airlines ban or restrict Boxers from hold/cargo travel due to their brachycephalic anatomy. US carriers including United, American, and Delta have excluded Boxers from cargo. Some European and Middle Eastern carriers still accept them under specific conditions. Always confirm directly with the airline for your specific route."},
{"question": "Are Boxers banned in any countries?", "answer": "Boxers are not subject to outright import bans in most countries. Some countries with dangerous dog legislation (Portugal, parts of Spain) may classify Boxers as restricted breeds requiring additional registration and public muzzle/leash requirements, but this is not an import ban. Verify with the specific destination country's veterinary authority."},
{"question": "What are the realistic options for moving a Boxer internationally if airlines won't take them?", "answer": "Options include: ferry travel where available (especially for UK-Europe routes), specialist charter pet transport, using a cargo carrier that still accepts brachycephalic breeds under veterinary certification, or identifying a specific airline that accepts Boxers on your route. A specialist IPATA agent can identify viable options."}
],
"body": """
Boxers are loyal, energetic dogs with a devoted following. They are also firmly on the brachycephalic breeds list, which creates real complications for international moves by air. Understanding your options before you start booking anything will save you significant stress.

## Why Boxers Are Restricted for Air Cargo

Boxers have a wide, blunt skull and a significantly shortened muzzle. Their airways are compressed as a result. The stress of cargo travel -- noise, vibration, isolation, temperature variation -- increases breathing effort. Combined with a pre-existing compromised airway, this raises the risk of respiratory distress.

Boxers were involved in several in-flight incidents before airlines began systematically restricting brachycephalic breeds. The restrictions are not arbitrary.

## Current Airline Landscape for Boxers (as of May 2026)

- **US carriers (United, American, Delta)**: Boxers banned from cargo hold
- **European flag carriers**: Policies vary. Some accept Boxers with veterinary certification and specific crate requirements; others do not.
- **Middle Eastern carriers**: Some (particularly Etihad and Qatar Airways on specific routes) have accepted brachycephalic breeds in cargo under controlled conditions. Confirm directly.
- **Asian carriers**: Varies widely

The landscape changes. Call the airline's cargo desk specifically and ask about Boxers. Do not rely on the website FAQ.

## Can Boxers Travel in Cabin?

Adult Boxers typically weigh 25 to 32 kg -- far beyond any airline's cabin pet weight limit. In-cabin travel is not an option for a full-grown Boxer.

## Alternative Routes

**Ferry:** For UK-Europe moves, Brittany Ferries, P&O Ferries, and DFDS all allow pets in vehicles. A Boxer can travel in your car without the restrictions that apply to air cargo. This is a practical solution for European destinations.

**Road:** Driving across Europe with a Boxer is entirely feasible for many destinations. The UK to Southern Spain by road, for example, avoids air cargo entirely.

**Specialist charter:** For routes where conventional carriers won't accept a Boxer, specialist pet transport operators occasionally use smaller aircraft with different cargo configurations. Not cheap, but sometimes the only viable option.

## Health Assessment Before Travel

Boxers are also prone to:
- Dilated cardiomyopathy (DCM) -- get cardiac assessment before any international flight
- Aortic stenosis
- Cancer (higher prevalence than many breeds)

An older Boxer with cardiac involvement is a much higher-risk traveller than a healthy young adult. Your vet needs to assess your specific dog.

*Airline brachycephalic policies change regularly. Always verify directly with the airline cargo department. Information current as of May 2026.*
"""
},

# ── PRACTICAL GUIDES ──────────────────────────────────────────────────────

{
"slug": "how-to-choose-a-pet-relocation-company",
"title": "How to Choose a Pet Relocation Company: What to Look for and What to Avoid",
"description": "Not all pet relocation companies are equal. Here is a practical guide to vetting agents, checking credentials, and getting a quote that actually covers everything.",
"date": "2026-05-06",
"tags": ["pet relocation company", "IPATA", "choosing an agent"],
"faqs": [
{"question": "What is IPATA and why does it matter?", "answer": "IPATA (International Pet and Animal Transportation Association) is the global trade body for pet relocation professionals. Members agree to a code of ethics and have access to professional training. IPATA membership is not a guarantee of quality, but it is a baseline indicator that a company takes the industry seriously. Check membership at ipata.com/member-directory."},
{"question": "How much should pet relocation cost?", "answer": "Costs vary enormously by route, animal size, and destination. Simple European moves might cost GBP 400 to GBP 1,200. Complex routes involving quarantine (Australia, New Zealand, Japan) can cost GBP 5,000 to GBP 15,000 or more. Be very wary of quotes significantly below market rate -- corners are being cut somewhere."},
{"question": "What questions should I ask a pet relocation company before booking?", "answer": "Ask: Are you IPATA members? Can you provide references from clients on this specific route? What is included in your quote (itemised)? What happens if there is a documentation problem on travel day? Do you have professional indemnity insurance? Who handles my pet at the destination end?"}
],
"body": """
Your pet's international move is a significant undertaking -- financially, logistically, and emotionally. The company you choose to handle it matters more than almost any other decision in the process. Here is how to approach the selection.

## Start with IPATA

The International Pet and Animal Transportation Association (IPATA) is the best starting point for finding a reputable agent. Members have agreed to a code of ethics covering animal welfare, accurate information, and fair business practices. The member directory at ipata.com lets you search by location and destination expertise.

IPATA membership is not a formal certification of quality -- it is a trade association, not a licensing body. But a company that has been an active IPATA member for several years, with no complaints against them, is a much safer choice than an unknown non-member.

## What a Good Agent Does

A genuinely professional pet relocation agent:

- Prepares a detailed, itemised quote (not just a headline number)
- Tells you exactly what documentation is required and in what sequence
- Has direct relationships with Official Vets, APHA/USDA/DAFF, and airline cargo departments
- Manages the airline booking for your pet specifically -- not just adding a note
- Provides a named contact for your move
- Has handled your specific route before and can demonstrate this
- Has professional indemnity insurance

## Red Flags to Watch For

- Vague quotes with no itemisation (you cannot compare quotes you cannot break down)
- No IPATA membership or verifiable industry affiliation
- Pressure to book quickly without time to research
- Inability to provide references from clients on your specific route
- Promise that everything will be "fine" without explaining what "fine" entails
- No clear answer on what happens if a document problem arises on travel day

## Getting Comparable Quotes

Get at least two to three quotes for any complex move. When comparing:

- Compare the itemised costs, not the headlines
- Check whether the destination-side handling (airport collection, delivery to address) is included
- Check whether quarantine fees are included or separate (for Australia/NZ/Japan, this is a significant cost)
- Ask each agent what happens if travel is delayed -- is the health certificate reissued at no extra cost?

## DIY vs Agent

For simple European moves (e.g., UK to France with a small dog in cabin), doing it yourself is feasible if you understand the requirements. For routes involving quarantine, multiple countries, or complex health protocols (Japan, Australia, South Korea-to-Australia, etc.), an agent earns their fee many times over. One date error in a complex document chain can set your timeline back 180 days.

## After Booking: Stay Involved

Even with a good agent, stay engaged in the process. Know what is happening at each stage, check that documents are being processed on schedule, and read everything before signing it. You are accountable for your pet's welfare -- an agent acts on your behalf.

*Always verify IPATA membership status directly at ipata.com. Information current as of May 2026.*
"""
},

{
"slug": "pet-microchipping-guide-international-travel",
"title": "Pet Microchipping for International Travel: What You Need to Know",
"description": "Microchipping is mandatory for international pet travel. Here is a guide to ISO standards, chip placement, scanning, and what to do if a chip fails or cannot be read.",
"date": "2026-05-06",
"tags": ["pet microchip", "ISO microchip", "pet travel documentation"],
"faqs": [
{"question": "What microchip standard is required for international pet travel?", "answer": "Almost all countries require ISO 11784/11785 standard microchips for pet travel. These are 15-digit chips operating at 134.2 kHz. If your pet has a 10-digit chip (older US standard, 125 kHz), you either need a secondary ISO chip or to carry your own scanner. Check the specific destination country's requirements."},
{"question": "Where is a microchip implanted in a dog or cat?", "answer": "In dogs and cats, the microchip is typically implanted under the skin between the shoulder blades (dorsal midline, between the scapulae). This is the standard location that scanners are applied to at border inspection. In some cats, chips can migrate over time -- a thorough scan of the whole body is good practice at any vet visit."},
{"question": "What happens if a border scanner cannot detect my pet's microchip?", "answer": "If the scanner cannot detect the chip, the border vet will try multiple scan positions. If still undetected, a second chip may need to be implanted, and all documentation linked to the original chip number becomes disconnected. This is rare but serious. Pre-travel scanning at your vet to confirm chip readability is a standard precaution."}
],
"body": """
The microchip is the foundation of every international pet move. It is the permanent link between your animal and all the documentation that allows it to travel. Understanding how it works -- and the failure modes -- helps you avoid problems at the border.

## Why the Microchip Comes First

Almost every country's pet import rules specify that the microchip must be implanted BEFORE the rabies vaccination. Why? Because the microchip is how the system links a specific animal to a specific vaccination record.

If the vaccination is administered and then the chip is implanted:
- The vaccination record references an animal with no chip ID
- The chip cannot be retroactively linked to that vaccination
- For countries requiring a titre test (Australia, Japan, New Zealand), the entire sequence is invalidated

Always: chip first, vaccinate after.

## ISO 11784/11785: The International Standard

The vast majority of countries require ISO standard chips. These are 15-digit chips that transmit at 134.2 kHz. Standard ISO chips from all reputable manufacturers are read by standard AVID, Trovan, Destron, and universal scanners.

**The 10-digit chip problem:** Some dogs chipped in the USA before the ISO standard became universal may have 10-digit chips (125 kHz). These are not read by standard international scanners. Options:

1. Have a second ISO chip implanted (two chips is not a problem for most border vets)
2. Carry your own scanner and offer to scan the animal yourself (most border posts prefer to use their own equipment)

The cleaner solution is an additional ISO chip.

## Getting Your Pet Microchipped

A microchip implantation is a simple procedure, similar to a vaccination injection. No anaesthetic is needed in most cases. A trained vet inserts the chip via a needle at the recommended position between the shoulder blades.

After implantation:
- The chip number should be recorded immediately in the veterinary record
- Register the chip on the relevant national database (Petlog in the UK, AKC in the USA, national registries elsewhere)
- Update the database with your current contact details

## Pre-Travel Chip Verification

Before any international move, ask your vet to scan your pet specifically to:

1. Confirm the chip is readable
2. Confirm the chip number matches what is recorded in all documents
3. Check for chip migration (particularly in cats)

A mismatch between the chip number on the health certificate and the number actually scanned is one of the most common border problems -- and it is entirely preventable.

## Chip Migration

Chips can migrate from their original implant site, particularly in cats. A chip implanted between the shoulder blades may move to the side of the neck or the flank over months or years. Border scanners should scan the whole body, not just the standard position, but this is not always done under time pressure.

At your pre-travel vet visit, confirm where the chip is actually located and scan it. Note the actual position if it has migrated, and inform the border vet on arrival.

## Database Registration: After International Moves

When you arrive in your new country, register your pet's chip number on the local database:
- UK: Petlog (petlog.org.uk) or MicrochipCentral
- Australia: Australian Animal Registry
- USA: AAHA Universal Pet Microchip Lookup
- EU: Many countries have national databases; some participate in the EU database

This helps reunite you with your pet if they are lost in the new country.

*Microchip requirements may vary by destination. Always verify with the destination country's veterinary authority before travel.*
"""
},

{
"slug": "travelling-with-senior-pets-internationally",
"title": "Moving Internationally with an Older Pet: Special Considerations for Senior Dogs and Cats",
"description": "Senior pets face additional risks during international travel. Here is how to assess fitness, manage the journey, and ensure your older dog or cat arrives in good health.",
"date": "2026-05-06",
"tags": ["senior pet travel", "older dog", "older cat", "pet relocation"],
"faqs": [
{"question": "Is there an age limit for pets to fly internationally?", "answer": "No universal age limit exists for pet air travel, but senior pets (generally dogs over 8 and cats over 10) should have a thorough vet assessment before any international flight. Many vets will discuss the risks honestly; some will decline to provide a fitness-to-fly certificate for an animal with significant health issues."},
{"question": "What health conditions make international travel riskier for older pets?", "answer": "Heart disease, kidney disease, respiratory conditions, arthritis (can make confinement painful), cognitive decline (increases disorientation and stress), and cancer are the main conditions that elevate travel risk in senior pets. A geriatric blood panel before travel gives your vet a clear picture."},
{"question": "How can I make international travel less stressful for a senior dog or cat?", "answer": "Choose the shortest available route. Book a direct flight if at all possible -- every layover adds stress and time. Use familiar bedding in the crate. Travel in cooler months. Have a vet at the destination lined up before you arrive. Keep the quarantine period as short as possible if required."}
],
"body": """
Moving internationally with a 12-year-old Labrador or a 14-year-old cat is a different conversation than moving with a young adult animal. The stakes are higher, the risk profile is different, and the decisions need to be made with clear-eyed veterinary input -- not just optimism.

## Have the Honest Conversation With Your Vet

Before planning any aspect of an international move with a senior pet, sit down with your vet for a frank discussion. Ask:

- Is my animal fit to travel internationally?
- What are the specific risks given their health status?
- Is there a point at which you would not provide a fitness-to-fly certificate?
- What monitoring should I do in the weeks before travel?
- What should I watch for on arrival?

A good vet will be honest with you. If they have concerns about cardiac function, kidney disease, or significant arthritis, those concerns are relevant. You need to know.

## Pre-Travel Health Assessment

For senior pets, a pre-travel blood panel makes sense:

- Complete blood count
- Biochemistry panel (kidney function, liver values, glucose, electrolytes)
- Thyroid function (for cats -- hyperthyroidism is common in older cats and affects stress tolerance)
- Cardiac assessment for dogs with murmurs

This gives your vet a baseline and may reveal conditions that affect travel safety decisions.

## Managing the Journey

**Crate comfort:** Senior pets may have arthritis or joint pain. The crate floor needs extra padding -- a thick memory foam mat rather than a thin rubber one. The crate must be large enough for the animal to shift positions without difficulty.

**Route selection:** Every unnecessary hour in a cargo hold is additional stress and physical discomfort for an older animal. Choose direct flights where possible, even if they cost more.

**Temperature:** Senior animals thermoregulate less effectively. Avoid summer cargo travel entirely for senior pets. Cool months are significantly safer.

**Hydration:** Older animals can dehydrate more quickly. Ensure water is accessible in the crate (a spill-resistant bowl attached to the crate door) throughout the journey.

## After Arrival

Senior pets need time to recover from international travel. Plan for:

- A quiet first few days -- no visitors, minimal change
- Familiar food (bring enough from home to avoid a sudden diet change)
- Veterinary check-up within the first week at your destination
- Patience -- disorientation and unusual behaviour after a long international move is normal and usually resolves within 1 to 2 weeks

## When Not to Travel

If your vet expresses serious concern about travel fitness, listen. A 14-year-old cat in renal failure and an 11-year-old dog with advanced cardiac disease are not good candidates for a 20-hour journey to Australia.

In some situations, the kindest decision is to keep your pet in its home country under trusted care until natural end of life, rather than subject it to a high-risk journey. This is a deeply personal decision -- but it is one worth having the information to make properly.

*Always involve your vet early in planning any international move with a senior pet.*
"""
},

{
"slug": "flying-with-a-cat-in-cabin-complete-guide",
"title": "Flying with a Cat in the Cabin: A Complete Practical Guide",
"description": "Cats can fly in the aircraft cabin if they meet weight requirements. Here is everything you need: carrier selection, booking, vet preparation, and what to expect on the day.",
"date": "2026-05-06",
"tags": ["cat in cabin", "flying with a cat", "cabin pet travel"],
"faqs": [
{"question": "What weight limit applies to cats in the aircraft cabin?", "answer": "Most airlines set a combined weight limit (cat plus carrier) of 5 to 8 kg for in-cabin pets. A typical adult domestic cat weighs 3.5 to 5 kg, and a soft carrier weighs 0.8 to 1.5 kg -- so most adult cats fall within cabin limits if the airline allows up to 6 to 8 kg combined. Check your specific airline's limit before booking."},
{"question": "Do cats need a health certificate to fly in the cabin internationally?", "answer": "Yes. Even for cabin travel, international flights require a health certificate for your cat. For EU entry from the UK, this is an AHC issued within 10 days of travel. For US domestic travel, airlines require a health certificate within 10 days. Requirements vary by destination -- always check before travel."},
{"question": "How do I stop my cat escaping from the carrier during the flight?", "answer": "Use a carrier with a secure zip or locking mechanism, not just a velcro closure. Do not open the carrier in flight unless strictly necessary. At security, ask to keep the carrier with you through the scanner rather than putting the cat through the X-ray belt. Keep one hand on the carrier at all times in the airport."}
],
"body": """
Cats are actually well-suited to cabin travel -- they are small, quiet, and once settled, often sleep for most of the flight. The challenge is the airport, the security process, and the first 20 minutes of every flight when the noise and vibration are at their peak.

## Is Your Cat Within Weight?

Most airlines set a cabin pet weight limit of 5 to 8 kg combined (cat plus carrier). Weigh your cat at the vet and weigh your carrier -- their combined weight must be under the airline limit.

Common adult cat weights:
- Domestic shorthair/longhair: 3.5 to 5 kg typically
- Maine Coon, Norwegian Forest Cat, Ragdoll: 4 to 9 kg (large breeds may exceed limits)
- Siamese, Abyssinian: 3 to 5 kg typically

If your cat is borderline, bring the carrier and weigh it before the flight day. Carriers vary significantly in weight.

## Choosing the Right Carrier

For cabin travel, you need a soft-sided carrier that fits under the seat in front of you. The specific dimensions vary by airline and aircraft type -- check the airline's website for under-seat dimensions on the aircraft type operating your route.

The carrier must:
- Fit the under-seat space completely (not stick out into the aisle)
- Have solid, ventilated sides (mesh panels on at least two sides)
- Have a secure closure (zipper with a locking clip)
- Be large enough for your cat to turn around and lie down

Popular options: Sleepypod Air, IATA-compliant soft carriers from Petmate, Sherpa, or similar.

## Booking Your Cat's Cabin Spot

Most airlines allow 1 to 2 pets in the cabin per flight. These spots fill up. Book your cat's place as soon as flights are confirmed:

1. Make your own booking
2. Call the airline (or use their online manage booking) to add the cabin pet
3. Pay the cabin pet fee (typically GBP 30 to GBP 100 per flight sector)
4. Get written confirmation with your pet's details on the booking

Do not leave this until check-in. If the spots are full, your cat cannot fly.

## Airport: The Stressful Part

The airport is usually harder for the cat than the flight itself. Your cat will hear and smell hundreds of new things and will not understand what is happening.

**Security:** You will be asked to remove your cat from the carrier and carry them through the metal detector while the carrier goes through the X-ray. Have a firm grip before you unzip. Hold the cat against your body with both hands. If your cat is likely to claw and escape, ask the security officer whether an alternative (wand scan with cat in carrier) is available -- some airports offer this.

**At the gate:** Keep the carrier zipped. Do not try to reassure your cat by opening the carrier in the terminal. This increases escape risk.

**On board:** Stow the carrier under the seat. Do not put it in the overhead bin. The carrier should be at your feet or at the feet of the seat in front. Once the seatbelt sign is off, you can discreetly reach your hand in to reassure your cat, but do not open the carrier.

## The Flight: What Usually Happens

Once the aircraft reaches cruise altitude, most cats settle. The white noise of the engines is actually calming for many cats. They typically lie down in the carrier and sleep for most of a medium-haul flight.

If your cat is vocalising throughout, other passengers will tolerate occasional meows but persistent yowling is disruptive. Check that the carrier is not too warm and that air is circulating. A piece of your worn clothing in the carrier helps with scent comfort.

## Feeding and Water

Do not feed a full meal within four hours of the flight. Cats can become nauseous from the motion. Offer water before going through security; most carriers allow a small water dispenser attached inside.

## After Landing

At the destination, keep the carrier zipped until you are in a secure, closed space. International arrivals with pets may involve a border veterinary check -- have your health certificate accessible in your hand luggage, not in the carrier.

*Check airline-specific cabin pet policies and international health certificate requirements before travel. Information current as of May 2026.*
"""
},

{
"slug": "settling-your-pet-after-international-move",
"title": "Settling Your Pet After an International Move: The First Two Weeks",
"description": "Pets need time to adjust after an international relocation. Here is how to help your dog or cat settle in, what normal post-move behaviour looks like, and when to call a vet.",
"date": "2026-05-06",
"tags": ["pet settling in", "post-move adjustment", "new country with pet"],
"faqs": [
{"question": "How long does it take for a dog to settle after an international move?", "answer": "Most dogs show significant settling within 1 to 2 weeks. Full adjustment to a new home, new smells, and a new routine typically takes 4 to 8 weeks. Older dogs and anxious dogs may take longer. Maintaining a consistent daily routine accelerates the process significantly."},
{"question": "Is it normal for cats to hide after an international move?", "answer": "Yes. Hiding is a very common and normal response to stress and new environments in cats. Most cats will emerge gradually over several days to a week as they build confidence in the new space. Provide hiding spots (boxes, a covered cat bed), keep the environment quiet, and let the cat come to you rather than forcing interaction."},
{"question": "When should I be concerned about my pet's behaviour after a move?", "answer": "Call your vet if: your pet has not eaten or drunk water in 24 hours, there is visible injury or pain from the journey, respiratory distress or persistent coughing, repeated vomiting or diarrhoea, or any neurological signs (disorientation, seizure, collapse). Mild appetite loss and behaviour changes for the first 48 hours are normal; prolonged issues are not."}
],
"body": """
The hard part of an international move is the logistics -- the documents, the flights, the quarantine. But the part that takes the most patience is the adjustment period once you arrive. Your pet has been through a significant stress event, moved to an unfamiliar environment, and is processing all of it without knowing what is happening.

## What to Expect: The First 48 Hours

Dogs may be:
- Hypervigilant and unable to settle
- Clingy and unwilling to leave your side
- Reluctant to eat (normal for up to 24 hours)
- Having disrupted sleep
- Toileting more or less frequently than usual

Cats may:
- Hide completely for the first day or two
- Refuse food
- Be silent or excessively vocal
- Show no interest in exploring

All of this is within normal range for a healthy animal that has just experienced a major disruption. Do not panic.

## What Helps: The Basics

**Familiar scent:** Your pet's own bedding from before the move should go with them -- not washed. The familiar smell is genuinely reassuring in a new space.

**Familiar food:** Do not change diet during the move or in the first few weeks after. This removes one variable. Bring enough food from your previous country to last 2 to 4 weeks while you find equivalent products locally.

**Consistent routine:** Feed at the same times you always have. Walk at the same times. This consistency communicates safety to your pet faster than any other single intervention.

**Quiet first days:** Resist the urge to introduce neighbours, friends, and the new local community to your pet in the first week. Give them space to decompress.

**Confined space initially:** Particularly for cats, starting in one room before opening the whole house reduces the overwhelm of a completely new environment. Let the cat claim the first room before expanding access.

## After Quarantine (Australia, New Zealand, Japan)

If your pet has spent 10 to 30 days in a quarantine facility, the adjustment period may be longer. They have been in a sterile, unfamiliar environment for weeks. Be patient:

- Do not expect immediate affectionate behaviour from a cat that has been in quarantine
- Dogs from quarantine may be over-excited and unsettled -- structured walks and calm handling help
- Keep things very quiet for the first week after collection

## When to Call the Vet

The issues above are normal adjustment responses. Call your vet for:

- No food or water for 24 hours
- Persistent vomiting or diarrhoea
- Respiratory difficulties
- Evidence of injury from the journey
- Neurological symptoms
- Any unusual discharge or wounds

It is worth registering with a local vet in your new country before your pet arrives, so you have a number to call. Do not wait until there is a problem to find a vet.

## The 8-Week Horizon

Most dogs and cats are substantially settled within 8 weeks of an international move. By this point they understand the new home, the routine, and the key people in their environment. Some sensitive animals take longer -- particularly cats, and particularly older animals.

Patience, consistency, and familiar smells are the most powerful tools you have.
"""
},

{
"slug": "how-to-prepare-your-pet-for-quarantine",
"title": "Preparing Your Pet for Quarantine: What to Expect and How to Help",
"description": "If your pet is heading to Australia, New Zealand, or Japan, quarantine is mandatory. Here is how to prepare your dog or cat and what happens during the stay.",
"date": "2026-05-06",
"tags": ["pet quarantine", "Australia quarantine", "New Zealand quarantine", "Japan quarantine"],
"faqs": [
{"question": "Can I visit my pet during quarantine in Australia?", "answer": "Yes. The Mickleham quarantine facility in Victoria allows owner visits during set visiting hours. Contact DAFF or the Mickleham facility directly for current visit times and protocols. Visits have been shown to reduce stress in dogs; for cats, the effect is more variable -- some cats settle better without disruption to their new routine."},
{"question": "What do I need to bring for my pet going into quarantine?", "answer": "Packing requirements vary by facility. Typically you can send: a small comfort item with your scent (T-shirt, soft toy), a supply of the pet's regular food (to avoid dietary disruption), any prescription medication with veterinary instructions, and contact information. Do not send items that cannot be laundered (biosecurity requirements). Contact the facility in advance for the approved list."},
{"question": "Is quarantine stressful for pets?", "answer": "Quarantine involves a change of environment and temporary separation from owners, which is stressful for most pets. Modern quarantine facilities (Mickleham in Australia, MPI in New Zealand) are professionally staffed, climate-controlled, and provide daily exercise. Most pets adapt within a few days. Highly anxious animals or animals with separation anxiety may find it harder."}
],
"body": """
Quarantine is mandatory for pets entering Australia, New Zealand, and Japan (and several other destinations). It is not a punishment -- it is a biosecurity check designed to protect these countries' disease-free status. Understanding what it involves and preparing your pet appropriately makes a real difference to how smoothly the experience goes.

## What Quarantine Actually Looks Like

Modern quarantine facilities are not neglectful holding areas. At Mickleham (Australia's facility near Melbourne):

- Dogs and cats are housed in individual, climate-controlled kennels
- Daily exercise sessions are provided
- Animals are monitored by trained staff
- Veterinary care is available
- The facilities are cleaned to high standards

At New Zealand's MPI facility in Auckland:
- Similar standards apply
- Individual exercise sessions
- Climate control

At Japan's AQS facilities:
- Highly professional operation
- Individual kennels
- Staff trained in animal handling

The length is fixed (10 days in Australia and NZ, varying in Japan). If all documentation is correct, the release date is predictable.

## Preparing Your Pet: Months Before

**Crate training:** This is the most important preparation step. An animal that is comfortable in a crate adapts to quarantine housing much better. Start months before travel:

1. Leave the crate open as a rest spot with comfortable bedding
2. Feed meals in the crate
3. Practice closing the door for increasing periods
4. Work up to the crate being locked for 4 to 6 hours without distress

**Scent familiarisation:** Animals that have a scent-comforting item (your worn T-shirt, a familiar blanket) in the quarantine kennel show lower stress indicators. Most facilities allow one or two soft items.

**Food familiarity:** Bring a two-week supply of your pet's regular food. Quarantine staff usually use it at the start of the stay before transitioning to facility food if needed. Sudden diet changes during the stress of quarantine can cause gastrointestinal issues.

## Packing for Quarantine

Check the specific facility's guidelines -- each has slightly different rules around what is permitted. Generally:

- A worn T-shirt or small blanket (launderable)
- 2-week supply of regular food
- Any prescription medications with clear instructions and dosing schedule
- Contact information (yours and an alternative)
- Comfort toy (check whether allowed under biosecurity)

Do not send expensive items -- they may be destroyed under biosecurity protocols.

## During Quarantine

Stay in contact with the facility. Request updates if you are not receiving them. For Australia's Mickleham, you can call or email for welfare updates. Visiting is permitted during set hours.

Most pets adapt within the first few days. Dogs often show initial distress followed by adjustment. Cats are variable -- some settle quickly, others remain anxious throughout.

## Collection Day

On the day of release, arrive at the scheduled time. Your pet will likely be:

- Excited and vocal (dogs)
- Subdued and slightly disoriented (cats often)
- Thinner than expected (mild weight loss from stress and reduced appetite is common)

Bring a familiar carrier or lead. Drive directly to your new home. Keep the first day very quiet.

*Contact your specific quarantine facility directly for current procedures and packing rules. This guide is accurate as of May 2026.*
"""
},

{
"slug": "pet-travel-documentation-checklist",
"title": "Pet Travel Documentation Checklist: Everything You Need in One List",
"description": "A complete checklist of pet travel documents for international moves. Print this out, tick each item off, and travel with confidence that nothing has been forgotten.",
"date": "2026-05-06",
"tags": ["pet travel checklist", "pet documentation", "international pet travel"],
"faqs": [
{"question": "Which documents are required for all international pet moves?", "answer": "The core documents for any international pet move are: microchip documentation, rabies vaccination certificate, and an official health certificate. Depending on destination, additional documents include a rabies titre test result, import permit, tapeworm treatment record, and CITES permit (for restricted species)."},
{"question": "Should I carry originals or copies of pet travel documents?", "answer": "Carry original documents AND at least one photocopy set. Border vets require originals. Keep the originals in your hand luggage (never checked bags). Store digital scans in cloud storage as a backup. If originals are lost, having digital copies does not solve the immediate problem but helps with replacement."},
{"question": "Do documents need to be translated for international pet travel?", "answer": "Health certificates issued on official templates (EU AHC, USDA APHIS template, etc.) are internationally recognised and do not require translation. For destinations with non-Latin script requirements (Japan, South Korea, certain Middle Eastern countries), a certified translation may be required -- your relocation agent or the destination country's embassy can advise."}
],
"body": """
Documentation errors cause more pet border refusals than anything else. This checklist is designed to be printed, ticked off, and taken with you. Work through it systematically -- not all items apply to every route, but use it as a complete master list and cross out what does not apply to you.

## Universal Requirements (All International Pet Moves)

- [ ] **Microchip certificate / implant record** -- showing chip number, implant date, chip position
- [ ] **Rabies vaccination certificate** -- current, within validity period, post-microchip implant date
- [ ] **Official veterinary health certificate** -- issued within 10 days of travel (or the period specified by destination)
- [ ] **National authority endorsement** -- APHA (UK), USDA APHIS (USA), DAFF (Australia) countersignature on health certificate where required
- [ ] **Vaccination history** -- complete prior vaccine records (useful even when not mandated)

## EU Entry (from non-EU countries including UK)

- [ ] **Animal Health Certificate (AHC)** -- issued within 10 days
- [ ] **Tapeworm treatment record** (dogs) -- 1 to 5 days before entry
- [ ] **Microchip** (ISO 11784/11785)
- [ ] **Rabies vaccination** (at least 21 days if first vaccine)

## Australia / New Zealand

- [ ] **Import permit** -- from DAFF (Australia) or MPI (NZ), confirmed before travel
- [ ] **Rabies titre test result** -- from OIE-approved laboratory, meeting 0.5 IU/mL threshold
- [ ] **180-day wait confirmation** -- date calculations showing wait period elapsed
- [ ] **Health certificate** -- issued within 10 days of travel, endorsed by national authority
- [ ] **Quarantine booking confirmation** -- Mickleham (AU) or Auckland (NZ) facility
- [ ] **Airline booking confirmation** for live animal -- not just a note, a confirmed booking

## Japan

- [ ] **Import notification** -- submitted to Japan AQS at least 40 days before arrival
- [ ] **Two rabies vaccines** with correct timing relative to each other and titre test
- [ ] **FAVN titre test result** -- from approved laboratory
- [ ] **180-day wait** -- from blood draw date
- [ ] **USDA-endorsed health certificate** (for US pets) or equivalent national endorsement
- [ ] **Japan AQS pre-arrival confirmation**

## Birds and Exotic Animals

- [ ] **CITES export permit** -- from origin country
- [ ] **CITES import permit** -- from destination country
- [ ] **Avian health certificate** -- Newcastle Disease, Avian Influenza, psittacosis declarations
- [ ] **Quarantine booking** at destination country facility

## Practical Document Management

- [ ] All originals in a clear document folder in hand luggage
- [ ] Photocopies of everything (one set)
- [ ] Digital scans stored in cloud / emailed to yourself
- [ ] Your vet's emergency contact number accessible
- [ ] Destination country's border veterinary authority phone number written down
- [ ] Microchip number noted independently (in case chip fails to scan)
- [ ] Your contact number written in permanent marker on the crate

## Before Leaving Home

- [ ] All documents dated and checked (no expired certificates)
- [ ] All dates cross-checked against each other (microchip before vaccine; vaccine before titre test; 180-day period elapsed)
- [ ] Chip scanned at pre-travel vet appointment and confirmed readable
- [ ] Airline booking confirmed with live animal reference number
- [ ] Crate checked: all bolts present, door latch secure, water bowl attached

*Adjust this checklist for your specific route. When in doubt, include more documentation rather than less.*
"""
},

{
"slug": "moving-abroad-with-pets-first-30-days",
"title": "Your First 30 Days Abroad with a Pet: A Practical Checklist",
"description": "The first month after an international move with a pet has a lot to sort out. Here is a practical checklist covering registration, vet registration, insurance, and settling-in tasks.",
"date": "2026-05-06",
"tags": ["moving abroad with pets", "expat pet care", "settling in"],
"faqs": [
{"question": "Do I need to register my dog in my new country?", "answer": "In most EU countries, yes. Germany, France, Spain, Austria, Italy, and many others require dogs to be registered with the local municipality within 30 days of establishing residency. Registration typically involves a fee, proof of rabies vaccination, and your address. Your new vet can usually advise on the local process."},
{"question": "When should I get new pet insurance in my new country?", "answer": "As soon as possible after arrival -- ideally from day one. Check whether your existing home-country policy has any overseas extension, but do not rely on this for long-term cover. Most home-country policies lapse when you establish permanent residency abroad. A gap in insurance leaves you exposed to potentially significant vet bills."},
{"question": "How do I find a good vet in my new country?", "answer": "Ask your employer's HR team, expat Facebook groups for your city, or InterNations community for recommendations. WSAVA-affiliated practices follow internationally recognised standards. Your pet relocation agent may also have recommendations -- good agents build relationships with vets in major destination cities."}
],
"body": """
You have arrived. Your pet is with you. The documents that consumed months of preparation are in a folder somewhere. Now what? The first 30 days after an international move with a pet have several things to take care of. Here is a practical checklist to work through.

## Week 1: Immediate Priorities

**Register with a local vet.**
Find a local vet before you urgently need one. A routine post-arrival check-up is a good excuse to register and establish a relationship. Bring your complete vaccination history, health certificate, and microchip documentation.

**Update microchip registration.**
Your pet's chip is registered to a home-country database. Register the same number on the relevant local/national database in your new country. In the EU, many countries have national pet databases linked to TRACES. In Australia, register on the Australian Animal Registry.

**Check insurance.**
Decide whether your existing pet insurance extends to your new country and for how long. If not, arrange new cover immediately. Contact local or international pet insurance providers -- companies like Agria and Petplan operate across multiple countries, and there are local equivalents in most major destinations.

**Check local vaccination requirements.**
Some countries require annual rabies vaccination by law. Others require kennel cough vaccines for dogs using boarding or day care. Your new vet will tell you what is locally required. Do not assume your home country vaccination schedule matches the local expectation.

## Week 2: Administrative Tasks

**Register with the local municipality (if required).**
In Germany, France, Spain, Italy, Austria, and many other countries, dogs must be registered with the local authority (Gemeinde, Mairie, Ayuntamiento, Comune) within 30 days. This involves providing proof of rabies vaccination and paying an annual licence fee. Your vet may help; alternatively, the local town hall will direct you.

**Arrange a local supply of any prescription medication.**
If your pet is on a repeat prescription, ensure a new prescription from your new vet is in place before your existing supply runs out. Bring the original prescription documentation to the first vet visit.

**Find emergency veterinary cover.**
Know where the nearest 24-hour emergency vet practice is before you need it. Ask your regular vet at registration.

## Week 3 to 4: Settling In

**Establish the local routine.**
Walk routes, feeding times, rest spots. Consistency in the new country is the fastest way to help your pet feel secure.

**Introduce the neighbourhood carefully.**
Short, controlled introductions to local dogs and the new neighbourhood. Do not overwhelm a newly-arrived pet with too many new experiences at once.

**Post-move vet check-up (if not done already).**
A wellness check at around three to four weeks post-arrival -- when the settling-in phase is mostly done -- gives the vet a more accurate baseline than an appointment on arrival day when your pet is still stressed.

## Local Laws Worth Knowing

Laws vary significantly by country:
- **Leash laws**: Many countries require dogs to be on a lead in all public spaces; others have off-lead parks
- **Microchip laws**: Some countries require re-chipping or re-registration by law
- **Breed restrictions**: Check local rules for restricted breeds
- **Fouling laws**: Dog fouling fines are enforced in most EU cities

Your new employer's HR department (if on a company relocation) or a local expat community group are the best sources of practical local guidance.

*This checklist is general guidance. Specific requirements vary by country and municipality.*
"""
},

{
"slug": "pet-export-from-australia-complete-guide",
"title": "Exporting Your Pet from Australia: What DAFF Requires for Departure",
"description": "Moving out of Australia with a dog or cat? DAFF manages pet exports as well as imports. Here is what you need: export permit, health certificate, and destination country requirements.",
"date": "2026-05-06",
"tags": ["Australia pet export", "leaving Australia with pet", "DAFF export"],
"faqs": [
{"question": "Do I need a permit to export my pet from Australia?", "answer": "Yes. All dogs and cats being permanently exported from Australia require an export permit from DAFF. Apply via the BICON system (bicon.agriculture.gov.au) well in advance. DAFF-accredited vets prepare the export health certificate, which must comply with the destination country's import requirements."},
{"question": "How far in advance should I apply for an Australian pet export permit?", "answer": "Apply at least 4 to 6 weeks before your intended travel date. Health certificate preparation and endorsement add additional time. If the destination country requires a titre test (UK, USA, EU countries generally do not for Australian pets), the export preparation may need to start months earlier."},
{"question": "Can I take my pet to any country from Australia?", "answer": "You can export a pet to any country that accepts pet imports, subject to that country's own requirements. Each destination has its own health certificate requirements. Australia's DAFF accredited export vets prepare health certificates to international templates. Some countries (Japan, for example) have very specific requirements -- verify with the destination country well in advance."}
],
"body": """
Australia is known for its strict pet import rules, but the export process is equally structured. DAFF manages both incoming and outgoing animal movements, and the export of a pet requires the same systematic approach as an import.

## The DAFF Export Process

All permanent pet exports from Australia must be facilitated through DAFF:

1. **Apply for export permit** -- via BICON (bicon.agriculture.gov.au). Select your destination country to see the applicable requirements.

2. **Find a DAFF-accredited export vet** -- not all vets are accredited for pet export work. Find one via the DAFF website or ask your regular vet if they are accredited.

3. **Destination country health certificate** -- your accredited vet prepares this according to the destination country's template. DAFF endorses it.

4. **Timing** -- the health certificate is valid for a specific period (typically 10 days for most countries). Book the vet appointment to fit within this window before travel.

## Destination-Specific Requirements

The destination country drives what is needed:

**To the UK:** Microchip, rabies vaccination, AHC template, DAFF endorsement. Australia is Part 1 listed -- no titre test required for UK entry. Dogs need tapeworm treatment 1 to 5 days before UK arrival.

**To the USA:** Standard USDA-endorsed health certificate. Rabies vaccination required for dogs. CDC import requirements apply. Relatively straightforward.

**To EU countries:** AHC template as above (UK-style). Australia is an approved third country for EU pet imports in many categories.

**To Japan:** Very specific. Two rabies vaccinations with correct timing, titre test, 180-day wait, advance notification to Japan AQS. Start this process 8+ months before intended departure.

**To New Zealand:** Titre test, import permit via MPI, 10-day quarantine. Relatively well-defined process.

## Airline Booking from Australia

Major carriers on Australian routes handling live animals include Qantas, Emirates, Singapore Airlines, and Cathay Pacific. Each has specific policies on crate sizes, breed restrictions, and seasonal restrictions. Book the animal's space with the airline cargo department directly -- not through the passenger booking system alone.

## Post-Export: Cancelling Australian Registrations

When permanently leaving Australia:
- Cancel your dog's council registration (or notify the council of the permanent export)
- Update microchip registration databases (Australian Animal Registry, or relevant state registry) to note the export
- Cancel Australian pet insurance

## DAFF and BICON

Everything export-related runs through BICON: bicon.agriculture.gov.au

DAFF's export team can be reached via the portal for specific queries. For complex routes (multi-country, restricted species, birds), contact DAFF directly before starting the process.

*This guide is accurate as of May 2026. DAFF export requirements are regularly updated -- always verify via BICON before beginning the export process.*
"""
},

{
"slug": "usa-to-uk-via-direct-routes-pet-guide",
"title": "Moving Pets from the USA to the UK: The Direct Route Guide",
"description": "Moving from the USA to Britain with a dog or cat? The USA is a listed country for UK entry. Here is the process: rabies vaccination, CDC-endorsed health certificate, and tapeworm for dogs.",
"date": "2026-05-06",
"tags": ["USA to UK", "pet transport", "UK pet import from USA"],
"faqs": [
{"question": "Is the USA on the UK's listed countries for pet imports?", "answer": "Yes. The USA is on Great Britain's Part 2 listed countries (unlisted countries with approved status). Dogs and cats from the USA can enter Great Britain without a rabies titre test, provided they have a microchip, current rabies vaccination, and an AHC issued within 10 days of travel by a USDA-endorsed vet."},
{"question": "Do dogs from the USA need tapeworm treatment before entering the UK?", "answer": "Yes. All dogs entering Great Britain require a tapeworm treatment given 1 to 5 days before arrival, regardless of origin country. The treatment must be administered by a vet and recorded in the AHC."},
{"question": "Which airline should I use to move a large dog from the USA to the UK?", "answer": "British Airways, Virgin Atlantic, and American Airlines are the main direct-route options. United Airlines has historically been one of the few US carriers that still accepts dogs in cargo on international routes. Always confirm directly with the airline cargo department before booking -- policies change."}
],
"body": """
The USA to UK route is one of the most-travelled international pet moves in the world. Tens of thousands of American families relocate to Britain each year, many with dogs and cats. The process is well-defined and, relative to routes like USA-to-Australia, quite manageable.

## What the UK Requires from USA Pets

Great Britain classifies the USA as a listed country, meaning:

1. **Microchip** (ISO 11784/11785) -- important note: many US-chipped pets have 10-digit chips that are not read by UK scanners. If your pet has an older 10-digit chip, have an additional ISO chip implanted before travel.
2. **Rabies vaccination** -- current, administered at least 21 days before travel if it is a first vaccine; if boosters are current this is already satisfied
3. **Animal Health Certificate (AHC)** -- issued by a USDA-accredited vet and endorsed by USDA APHIS within 10 days of arrival in Great Britain
4. **Tapeworm treatment** (dogs only) -- 1 to 5 days before UK arrival

**No titre test required.** This significantly simplifies the USA-UK route compared to moving to Australia or New Zealand.

## Getting the AHC in the USA

Your vet must be USDA-accredited (not all vets are) to issue the AHC. Find an accredited vet via the USDA APHIS Veterinary Accreditation Program website.

After your vet signs the AHC, it must be endorsed by USDA APHIS. You can submit to:
- Your local APHIS Veterinary Services Area Office (fastest for in-person or overnight courier)
- APHIS Headquarters by post (allow more time)

APHIS endorsement typically takes 2 to 5 working days. Build this into your timing.

## The 10-Digit Chip Problem

This is the most common complication on this route. Many US dogs were chipped before ISO standards became universal in the USA, and they carry 10-digit (134 kHz) chips. UK scanners read 15-digit ISO chips (134.2 kHz).

Solution: Have an additional ISO-standard chip implanted by your vet. This is simple and painless. The new chip number must be noted in the AHC alongside the original chip number. UK border vets scan both positions and accept both numbers with proper documentation.

## Flight Options

**Non-stop routes:** London Heathrow (LHR) from New York (JFK/EWR), Los Angeles (LAX), Chicago (ORD/MDW), Atlanta (ATL), Dallas (DFW), Miami (MIA), San Francisco (SFO), and other major cities.

**Airlines:** British Airways, Virgin Atlantic, American Airlines, United Airlines. Each has different policies on whether pets travel as checked baggage or cargo. For large dogs, cargo-only may apply. Confirm with the airline.

## On Arrival in the UK

APHA veterinary inspectors at Heathrow's live animal facility process arriving pets. The inspection is usually efficient for pets from listed countries with complete documentation. Keep originals accessible.

After arrival, update microchip registration to a UK database and arrange local pet insurance.

*This guide is accurate as of May 2026. Verify USDA APHIS requirements and APHA guidance before travel.*
"""
},

]

def write_article(article):
    slug = article["slug"]
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")

    if os.path.exists(filepath):
        print(f"SKIP (exists): {slug}")
        return

    title = article["title"]
    description = article["description"]
    date = article["date"]
    tags_list = "\n".join(f'    - "{t}"' for t in article["tags"])
    faqs_block = ""
    for f in article["faqs"]:
        q = f["question"].replace('"', "'")
        a = f["answer"].replace('"', "'")
        faqs_block += f'    - question: "{q}"\n      answer: "{a}"\n'

    body = article["body"].strip()

    seo_title = title + " | PetTransportGlobal"
    if len(seo_title) > 65:
        seo_title = title[:55].rstrip() + "... | PetTransportGlobal"

    content = f"""---
title: "{title}"
description: "{description}"
date: "{date}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{seo_title}"
  description: "{description[:155]}"
tags:
{tags_list}
faqs:
{faqs_block.rstrip()}
---

{body}
"""

    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"WROTE: {slug}")


for article in ARTICLES:
    write_article(article)

print(f"\nDone. {len(ARTICLES)} articles processed.")
