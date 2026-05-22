"""
Blog Batch 18 - PetTransportGlobal
20 articles: country guides, route guides, breed guides, practical guides
ASCII-only content. Skip-if-exists logic.
"""

import os

OUTPUT_DIR = r"site\content\blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [

# ─── 1. Laos pet import guide ─────────────────────────────────────────────────
{
"slug": "laos-pet-import-guide",
"content": """---
title: "Importing a Pet to Laos: Rules, Documents and What to Expect"
description: "A practical guide to importing cats and dogs to Laos. Covers the Department of Livestock and Fisheries permit process, vaccination requirements, health certificates and border entry."
date: "2025-07-22"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/laos-pet-import-guide/"
tags: ["laos", "southeast asia", "country guide", "pet import"]
---

Laos sits at a crossroads in Southeast Asia, bordered by Thailand, Vietnam, China, Cambodia and Myanmar. It has a growing expat community -- particularly in Vientiane and Luang Prabang -- and an increasing number of foreign residents arrive or depart with companion animals. The import process is less formalised than in some neighbouring countries, but the core requirements are well-established.

## Who Controls Pet Imports into Laos?

The Department of Livestock and Fisheries (DLF) under the Ministry of Agriculture and Forestry oversees live animal imports. The customs and agriculture inspection point at the port of entry will check your documents.

For cats and dogs entering Laos, the general requirements are:

1. **Microchip** -- ISO 15-digit chip strongly recommended; in practice it is checked at many borders
2. **Rabies vaccination** -- current and within the valid period; primary vaccination must have been given at least 30 days before travel
3. **Core vaccinations** -- for dogs: distemper, parvovirus, hepatitis; for cats: panleukopenia, herpesvirus, calicivirus
4. **Official health certificate** -- from a licensed veterinarian in the country of origin; endorsed by the government veterinary authority of that country
5. **Import permit** -- issued by the DLF Vientiane; apply through the DLF at least 2 to 4 weeks before travel; fees apply

There is no titre test requirement for Laos from most standard origin countries.

## Approved Entry Points

Most international arrivals into Laos happen via:
- **Wattay International Airport, Vientiane (VTE)** -- the main international gateway
- **Luang Prabang International Airport (LPQ)** -- selected international routes
- Land crossings from Thailand (Nong Khai/Vientiane Friendship Bridge, Mukdahan, others) -- live animal acceptance at land crossings requires pre-notification to DLF

If entering overland from Thailand, confirm with the DLF well in advance that the specific crossing you plan to use can process live animal imports.

## After Arrival

Veterinary inspection is carried out at the port of entry. For pets arriving with complete documentation from recognised countries, this is typically a brief check. If documents are incomplete, your animal may be held at the DLF facilities in Vientiane for further inspection.

Laos does not impose mandatory quarantine for pets from most countries with full documentation, but DLF has discretion to require this if they have concerns.

## Practical Points

- Vientiane has a small but functioning expat veterinary community; finding a vet who can issue export documentation when you eventually leave is generally possible
- Thai-language documentation may be accepted at some crossings given the close relationship between Laos and Thailand; confirm with DLF
- Laos uses the Lao kip and border inspection fees are modest; have local currency available

---

**Sources:** Department of Livestock and Fisheries, Lao PDR; ASEAN animal health frameworks; OIE/WOAH country profile for Lao PDR.
"""},

# ─── 2. Mongolia pet import guide ─────────────────────────────────────────────
{
"slug": "mongolia-pet-import-guide",
"content": """---
title: "Importing a Pet to Mongolia: Permits, Health Certificates and Ulaanbaatar Entry"
description: "Everything you need to bring a cat or dog to Mongolia. Covers the MASM import permit, health certificate requirements, approved entry points and what to expect at Chinggis Khaan Airport."
date: "2025-07-23"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/mongolia-pet-import-guide/"
tags: ["mongolia", "ulaanbaatar", "country guide", "pet import", "central asia"]
---

Mongolia is a destination that comes up less frequently in pet relocation conversations, but the country has a small and established expat community in Ulaanbaatar, and many NGO workers and diplomatic staff relocate there with animals. The import process is manageable but requires planning and the right paperwork.

## Regulatory Authority

The General Agency for Veterinary and Breeding (GAVB) under Mongolia's Ministry of Food, Agriculture and Light Industry oversees live animal imports. Customs veterinary officers at Chinggis Khaan International Airport (ULN) carry out the physical inspection on arrival.

## Core Requirements for Pets Entering Mongolia

For cats and dogs arriving from most countries:

1. **ISO microchip** -- 15-digit; implanted before vaccinations
2. **Rabies vaccination** -- current and valid; primary vaccination at least 21 to 30 days before travel
3. **Core vaccinations** -- dogs: distemper, parvovirus, hepatitis, leptospirosis; cats: panleukopenia, calicivirus, herpesvirus
4. **FAVN rabies antibody titre test** -- required for pets arriving from countries outside a recognised low-risk list; result must show at least 0.5 IU/ml; test conducted at an OIE-approved laboratory; allow at least 30 days between vaccination and the test, and confirm the current waiting period requirement with GAVB
5. **Import permit** -- issued by GAVB; apply 3 to 4 weeks before travel with accompanying documentation
6. **Official health certificate** -- issued by the government veterinary authority of the country of origin; must be translated into Mongolian or English; Mongolian customs may request a certified translation for health certificates in other languages

## Entry via Chinggis Khaan International Airport

Almost all international pet arrivals come through Chinggis Khaan International Airport (ULN, also coded as MXX). MIAT Mongolian Airlines and a small number of international carriers (Aero Mongolia, Korean Air, Air China, Turkish Airlines) operate routes to Ulaanbaatar.

On arrival, the veterinary officer at the airport will inspect your documents. If everything is in order, your pet is released after the inspection. If documentation is incomplete, your animal may be detained at the airport veterinary holding facility.

## Quarantine

Mongolia does not impose a mandatory quarantine period for pets from recognised countries with full documentation. However, GAVB has discretion to quarantine animals that appear ill or whose documentation raises concerns.

## Export from Mongolia

When leaving Mongolia with a pet, you need an export certificate issued by GAVB. Contact the GAVB well in advance of departure as obtaining this certificate requires a veterinary inspection and can take several working days. The destination country's specific health certificate requirements must also be met.

## Living Conditions for Pets in Ulaanbaatar

Ulaanbaatar has a continental climate with extreme cold winters (temperatures regularly reach -30 degrees Celsius) and warm summers. If you are relocating with a cold-weather breed, they may cope well with the climate. Short-coated breeds and brachycephalic dogs will need appropriate clothing and shelter in winter.

---

**Sources:** General Agency for Veterinary and Breeding, Mongolia; OIE/WOAH country profile for Mongolia; MIAT Mongolian Airlines live animal cargo guidance.
"""},

# ─── 3. Algeria pet import guide ──────────────────────────────────────────────
{
"slug": "algeria-pet-import-guide",
"content": """---
title: "Importing a Pet to Algeria: Health Certificates, Permits and Border Rules"
description: "A practical guide to bringing a cat or dog to Algeria. Covers the ONVSA permit process, endorsed health certificates, vaccination requirements and arrival procedures at Algiers Airport."
date: "2025-07-24"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/algeria-pet-import-guide/"
tags: ["algeria", "north africa", "country guide", "pet import"]
---

Algeria is North Africa's largest country and home to a growing number of expatriates, particularly in Algiers, Oran and the energy sector hubs in the south. Pet import rules are managed by the Direction des Services Veterinaires (DSV) within the Ministry of Agriculture and Rural Development. The process is not especially complex by regional standards, but documentation must be exact.

## Regulatory Framework

Algeria's veterinary authority -- the Office National des Services Veterinaires Avicoles (ONVSA) and the broader DSV network -- regulates the import of live animals including companion animals. The framework is broadly aligned with OIE standards.

## Requirements for Cats and Dogs

For pets arriving from Europe, North America and other recognised countries:

1. **ISO microchip** -- 15-digit standard chip required
2. **Rabies vaccination** -- current; for animals coming from outside the North Africa region, the vaccine must be within valid period; primary vaccination at least 21 days before travel
3. **Additional vaccinations** -- dogs: distemper, parvovirus, leptospirosis; cats: panleukopenia, viral rhinotracheitis; recommended at a minimum
4. **Official health certificate** -- completed by a licensed vet in the country of origin and endorsed by the government veterinary authority of that country; the French-language format is accepted and preferred (Algeria is a French-speaking administrative environment); English certificates with a certified French translation are also accepted
5. **Import permit or authorisation** -- issued by the DSV central offices in Algiers; apply through the Algerian consulate in your home country or the DSV directly at least 3 to 4 weeks before travel
6. **Serology test** -- a rabies antibody titre test (FAVN) may be required for pets arriving from countries with a higher rabies risk profile; confirm with DSV in advance

## Entry Points

International flights arrive at Houari Boumediene Airport, Algiers (ALG) and at a number of regional airports (Oran Mohamed Boudiaf, Constantine Mohamed Boudiaf, etc.). Algiers is the primary international gateway for live animal arrivals.

Algeria has several land borders, though the Algeria-Morocco land border has been closed since 1994. Entry from Tunisia is possible but must be pre-cleared with the DSV.

## Quarantine

Algeria does not impose a mandatory quarantine period for pets from most recognised countries that arrive with complete documentation. Veterinary inspection takes place on arrival and pets are released to the owner after the inspector is satisfied.

## Breed Restrictions

Algeria has enacted legislation restricting the ownership and import of certain dog breeds including pit bull-type dogs and Rottweilers under public safety laws. If you are travelling with a restricted breed, contact the DSV and the Algerian consulate in your home country before making any travel arrangements.

## Key Considerations for Expats

Many expat workers in Algeria are based in gated compounds or serviced accommodation that may have rules about pets. Confirm your accommodation's pet policy before arranging a relocation. In the southern energy hubs such as Hassi Messaoud and In Amenas, veterinary services are very limited and emergency care for animals is difficult to access.

---

**Sources:** Direction des Services Veterinaires, Ministry of Agriculture and Rural Development, Algeria; OIE/WOAH country profile for Algeria; Algerian Consulate general guidance on animal import.
"""},

# ─── 4. Australia to India pet transport guide ────────────────────────────────
{
"slug": "australia-to-india-pet-transport-guide",
"content": """---
title: "Pet Transport from Australia to India: Permits, Health Certs and Airline Routes"
description: "Moving your cat or dog from Australia to India. Covers DAHD import permit requirements, AQIS-endorsed health certificates, approved entry airports and airline options for this route."
date: "2025-07-25"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/australia-to-india-pet-transport-guide/"
tags: ["australia", "india", "route guide", "pet transport", "pet relocation"]
---

Moving a pet from Australia to India is a route many Australians of Indian origin or corporate transferees navigate. The journey is operationally straightforward -- direct flights are plentiful -- but the paperwork requires careful coordination between two distinct regulatory systems.

## Australia's Export Requirements

Before your pet can leave Australia, the Australian Department of Agriculture, Fisheries and Forestry (DAFF, formerly known as DAFF or AQIS under previous naming) must issue an export health certificate. To obtain this:

1. Book an appointment with an **accredited export veterinarian** in Australia; not all vets are accredited for export certification
2. The vet conducts a health inspection and completes the export health certificate in the approved format
3. The certificate is endorsed by DAFF; this endorsement is done online via the DAFF export certification system; timing is typically 2 to 5 business days after the vet submits the paperwork
4. The endorsed certificate is valid for a limited period -- confirm the current validity window with your exporting vet

Your pet also needs:
- ISO microchip (Australia-chipped pets typically have compliant chips, but confirm the number is 15-digit ISO)
- Current rabies vaccination (Australia is rabies-free but India requires this; arrange the vaccination in Australia before departure)
- Core vaccinations current (distemper, parvovirus for dogs; panleukopenia, herpesvirus, calicivirus for cats)

## India's Import Requirements

India requires:
1. **Import permit from the Department of Animal Husbandry and Dairying (DAHD)** -- apply at least 3 to 4 weeks before travel; the permit specifies the permitted port of entry
2. **Endorsed health certificate** -- the Australian DAFF-endorsed certificate is accepted
3. **Current vaccinations** including rabies

No titre test is currently required for Australia-to-India moves.

## Approved Indian Entry Airports

The import permit will specify which Indian airport your pet may enter through. Currently designated ports include Delhi (DEL), Mumbai (BOM), Bengaluru (BLR), Chennai (MAA) and Kolkata (CCU).

## Airlines on This Route

Direct flights between Australia and India operate with:
- **Air India** -- Sydney, Melbourne, Perth direct to Delhi and Mumbai; cargo policies vary by route
- **Qantas** (via codeshare, sometimes operated by partners) -- confirm live animal cargo acceptance
- **Singapore Airlines / Scoot** (via Singapore SIN) -- a popular transit routing that adds Singapore as a connection; confirm whether Singapore transit rules affect live animal transit
- **IndiGo**, **Vistara** (now merged into Air India) -- primarily domestic India but some international routes

For cargo shipments, contact Air India Cargo directly for the Australia-India route. Not all aircraft types on this route accept live animals in hold.

## Timeline

- Allow 4 to 6 weeks for the India import permit
- The Australian DAFF export certificate cannot be issued more than 10 days before departure
- Rabies vaccination must be complete and within valid period before the export certificate is signed

The tightest part of the timing is the DAFF endorsement and the India permit running in parallel. Start the India permit application first, then align the DAFF export certificate appointment close to your departure date.

---

**Sources:** Australian DAFF export certification process; Department of Animal Husbandry and Dairying, India; IATA Live Animals Regulations; Air India Cargo live animals policy.
"""},

# ─── 5. Canada to Germany pet transport guide ─────────────────────────────────
{
"slug": "canada-to-germany-pet-transport-guide",
"content": """---
title: "Pet Transport from Canada to Germany: Health Certificates, Titre Tests and EU Entry"
description: "How to move your cat or dog from Canada to Germany. Covers the EU third-country health certificate, CFIA endorsement, rabies titre test rules, 3-month wait and airline options."
date: "2025-07-26"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/canada-to-germany-pet-transport-guide/"
tags: ["canada", "germany", "europe", "route guide", "pet transport"]
---

Canada is classified as a third country for EU pet entry purposes. For pet owners moving from Canada to Germany -- whether as returning EU nationals, corporate transferees or international students -- the process involves EU third-country import rules, which include a titre test and a waiting period that requires advance planning.

## Canada's Export Requirements

When exporting a pet from Canada, the Canadian Food Inspection Agency (CFIA) is the regulatory body. The steps are:

1. Have your pet examined by a **CFIA-accredited veterinarian** who can complete an official health certificate in the appropriate format
2. The health certificate is submitted to CFIA for **federal endorsement** (required for most international destinations); this typically takes 3 to 10 business days; CFIA offices in major cities can process same-day or next-day if you book in advance
3. The endorsed certificate must be issued within 10 days of travel to Germany

Your pet also needs:
- ISO 15-digit microchip (most Canadian-chipped pets are ISO compliant, but verify)
- Current core vaccinations

## Germany/EU Entry Requirements

Germany, as an EU member state, applies EU Regulation 576/2013 (and successor regulations) for third-country pet imports. Canada is currently classified as a **non-listed third country** for the EU's pet travel rules. This means:

1. **ISO microchip**
2. **Rabies vaccination** -- primary course complete; the vaccination must have been administered after the microchip was implanted
3. **FAVN rabies antibody titre test** at an EU-approved laboratory -- result must be at least 0.5 IU/ml; the test must be conducted at least 30 days after the rabies vaccination; you must then wait **3 months from a satisfactory titre test result** before the animal may enter the EU
4. **Official health certificate in the EU third-country format** -- completed by a CFIA-accredited vet and endorsed by CFIA
5. **TRACES NT notification** -- the German border inspection post (BIP) must be notified in advance via the TRACES NT system; this is usually handled by the receiving party or a pet relocation agent in Germany
6. **Entry through a designated BIP** -- only certain ports of entry in Germany can accept third-country pet arrivals; Frankfurt Airport (FRA) is the primary German BIP for air arrivals

## The 3-Month Wait Explained

The mandatory 3-month wait after the titre test is the main timeline driver. Here is an example:

- February: Microchip implanted, rabies vaccination given
- March: Titre test conducted (at least 30 days after vaccination)
- June: Earliest possible arrival in Germany (3 months after positive titre result)

Once a valid titre result exists and rabies boosters are kept current, the 3-month wait does not need to be repeated for future EU travel.

## Airlines on This Route

Direct flights from Canada to Germany operate with:
- **Lufthansa** -- Toronto (YYZ) and Montreal (YUL) to Frankfurt (FRA); Munich (MUC) on some routes; cargo pet acceptance available
- **Air Canada** -- Toronto and Vancouver (YVR) to Frankfurt; cargo hold pets accepted on long-haul routes
- **Condor** -- seasonal leisure routes from Canadian cities to Germany; confirm cargo pet acceptance
- **Eurowings Discover** -- charter/leisure subsidiary; confirm availability

Frankfurt is also the primary German BIP, so routing into FRA is the cleanest option both logistically and in terms of border inspection.

---

**Sources:** Canadian Food Inspection Agency (CFIA) export requirements; European Commission EU Regulation 576/2013 pet travel; TRACES NT system; Lufthansa Cargo live animals; Air Canada cargo.
"""},

# ─── 6. USA to China pet transport guide ──────────────────────────────────────
{
"slug": "usa-to-china-pet-transport-guide",
"content": """---
title: "Pet Transport from USA to China: GACC Rules, 180-Day Wait and Quarantine"
description: "How to move your cat or dog from the USA to China. Full breakdown of GACC requirements, the 180-day post-titre wait, mandatory quarantine and airline cargo options for this route."
date: "2025-07-27"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/usa-to-china-pet-transport-guide/"
tags: ["usa", "china", "route guide", "quarantine", "pet transport"]
---

Moving a pet from the USA to China is one of the longer preparation processes in international pet relocation. China's General Administration of Customs (GACC) enforces a strict pre-arrival protocol that begins 6 to 9 months before you plan to travel. Get the sequence right from the start and the process is manageable; skip a step or misjudge the timeline and the delays are significant.

## Step 1: Microchip (First)

Your pet must have an ISO 15-digit microchip implanted **before** any rabies vaccination that will count toward the Chinese protocol. In the USA, many pets are chipped with 9-digit non-ISO chips -- verify your pet's chip is 15-digit ISO; if not, arrange a second ISO chip implantation.

## Step 2: Rabies Vaccinations

Two rabies vaccinations are required, given at least 30 days apart. Both must be given **after** the microchip is recorded in the vet's notes. Use a vaccine brand that is on the GACC approved list -- your vet can confirm; most standard US-licensed rabies vaccines are accepted.

## Step 3: Titre Test (180-Day Clock Starts Here)

After the second vaccination, wait at least 30 days before collecting a blood sample for the **FAVN rabies antibody titre test**. The lab must be on the GACC approved list. In the USA, the Kansas State University Veterinary Diagnostic Laboratory and a small number of other facilities are GACC approved -- confirm the current list at the GACC or AQS website.

The result must show 0.5 IU/ml or above. After the test passes, the **180-day wait** begins. Your pet cannot enter China for 180 days after the titre test date.

## Step 4: USDA APHIS-Endorsed Health Certificate

Within 10 days of your travel date to China, your USDA-accredited veterinarian completes the health certificate. This must follow the Chinese government's specific format -- ask your vet to use the template available from USDA APHIS International. The certificate is then **endorsed by USDA APHIS Veterinary Services** (your regional area office); book this appointment in advance as same-day endorsements are not always available.

## Step 5: Import Permit and GACC Registration

China requires an import permit/registration through GACC. For personal pets, this is typically handled at the destination city's customs office or by a GACC-registered import agent in China. It is strongly recommended to use a licensed Chinese import agent for this step -- they will also handle the quarantine facility booking.

## Step 6: Mandatory Quarantine

All pets entering China undergo a mandatory **30-day quarantine** at a GACC-approved facility near the arrival airport. Common quarantine facilities:
- **Shanghai Pudong (PVG)** -- Pudong Free Trade Zone quarantine facility
- **Beijing Capital (PEK) or Daxing (PKX)** -- Beijing facilities
- **Guangzhou Baiyun (CAN)** -- Guangzhou facility
- **Shenzhen Bao'an (SZX)** -- Shenzhen facility

Costs for 30-day quarantine range from approximately USD 800 to 2,000 depending on facility and animal size. You cannot take your pet home until the full 30 days has elapsed and the quarantine certificate is issued.

## Airlines on This Route

Long-haul flights from USA to China with live animal cargo:
- **Air China** -- Los Angeles (LAX), San Francisco (SFO), New York (JFK) to Beijing (PEK); Shanghai (PVG); cargo pets accepted on selected routes
- **China Eastern** -- LAX, JFK to Shanghai PVG; confirm current cargo pet acceptance
- **China Southern** -- LAX to Guangzhou (CAN); cargo acceptance varies by aircraft type
- **United Airlines** -- SFO, LAX, JFK to Shanghai, Beijing; long-haul cargo pet acceptance; confirm route-specific availability

## Total Timeline

For a pet with no prior titre test history, allow **9 months** from start to finish:
- Month 1: Chip + first vaccination
- Month 2: Second vaccination (30+ days after first)
- Month 2-3: Titre test (30+ days after second vaccination)
- Months 3-9: 180-day wait
- Month 9: Health certificate + travel (with quarantine on arrival)

---

**Sources:** General Administration of Customs of China (GACC) live animal import regulations; USDA APHIS international pet travel (aphis.usda.gov); Kansas State University Veterinary Diagnostic Laboratory; IATA LAR 50th Edition.
"""},

# ─── 7. UK to Portugal pet transport guide ────────────────────────────────────
{
"slug": "uk-to-portugal-pet-transport-guide",
"content": """---
title: "Pet Transport from UK to Portugal: Post-Brexit Rules, Titre Test and Airline Options"
description: "How to move your cat or dog from the UK to Portugal after Brexit. Covers the Animal Health Certificate, APHA endorsement, 3-month titre test wait, TRACES notification and airlines."
date: "2025-07-28"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/uk-to-portugal-pet-transport-guide/"
tags: ["uk", "portugal", "europe", "route guide", "post-brexit", "pet transport"]
---

Portugal has become one of the most popular destinations for British expats. The climate, the lower cost of living relative to the UK and Portugal's Golden Visa programme have drawn tens of thousands of UK residents over the past decade. For those moving with pets, the post-Brexit rules add a layer of planning that was not required before January 2021 -- but the process is well-understood and manageable.

## The Post-Brexit Change

Before Brexit, a UK pet passport and current rabies vaccination was all that was needed for UK-to-Portugal travel. Since January 2021, the UK is a third country for EU entry purposes. This means:

- The old UK pet passport is no longer valid for EU travel from the UK
- A new **Animal Health Certificate (AHC)** is required each trip
- A **rabies titre test** is required if your pet does not already have a valid titre result from after their current rabies vaccination
- A **3-month wait** after a passing titre test applies before the animal can enter Portugal/EU

## Step-by-Step Process

**1. ISO microchip** -- must be implanted before any rabies vaccination you intend to rely on

**2. Rabies vaccination** -- current and within valid period; the vaccine must have been administered after the microchip

**3. Titre test** -- at an EU-approved laboratory (many UK labs are EU-approved; check the approved list); result must be 0.5 IU/ml or above; test must be given at least 30 days after the rabies vaccination; you must then wait **3 months** from a positive titre result before entering Portugal

**4. Animal Health Certificate (AHC)** -- completed by a UK Official Veterinarian (OV) within 10 days of your arrival date in Portugal; the OV must be approved by APHA; the AHC is valid for 10 days for EU entry and then 4 months for onward EU travel

**5. APHA endorsement** -- the AHC does not require APHA endorsement for all EU destinations, but many border officers prefer an APHA-stamped document; confirm with your OV what is currently required for Portugal specifically

**6. TRACES NT notification** -- Portugal has Border Inspection Posts (BIPs) at Lisbon Humberto Delgado Airport (LIS) and Porto Francisco Sa Carneiro Airport (OPO); the BIP must be notified via TRACES NT before your arrival; your OV or pet relocation agent typically handles this

## What About Once You Have a Valid Titre?

Once your pet has a successful titre test on record and you keep the rabies vaccination current, you do not need to repeat the titre test for future UK-to-EU trips. You will still need a new AHC for each entry (valid 10 days). This makes regular commuting between the UK and Portugal with a pet workable, just expensive in vet fees.

## Flying UK to Portugal

Direct flights from London to Lisbon and Porto are operated by **TAP Air Portugal**, **British Airways**, **easyJet**, **Ryanair** and **Jet2** (seasonal). Most low-cost carriers do not accept pets in the hold -- TAP Air Portugal accepts cabin pets (small dogs and cats) and pets as checked baggage on some routes. British Airways uses PetAir UK for hold transport.

For cabin pets, the combined weight limit is typically 6 to 8 kg. A Chihuahua, Maltese or small cat in a soft carrier generally qualifies. A Labrador does not.

## Living in Portugal with a Pet

Portugal has good veterinary infrastructure in the Lisbon, Porto and Algarve regions. Rural Alentejo and the interior have fewer vets. NIF (fiscal number) registration is useful for veterinary records and municipal dog licensing (registo de canino) is required for dogs.

---

**Sources:** UK APHA official veterinarian guidance; European Commission EU third-country pet travel rules (Regulation EU 576/2013); TRACES NT platform; TAP Air Portugal pet policy.
"""},

# ─── 8. France to Germany pet transport guide ─────────────────────────────────
{
"slug": "france-to-germany-pet-transport-guide",
"content": """---
title: "Pet Transport from France to Germany: EU Pet Passport and Cross-Border Rules"
description: "Moving a cat or dog from France to Germany within the EU. Covers the EU pet passport, microchip requirements, documentation, driving and flying options for this common expat route."
date: "2025-07-29"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/france-to-germany-pet-transport-guide/"
tags: ["france", "germany", "europe", "route guide", "eu pet travel", "pet transport"]
---

France and Germany share a long border, a deeply integrated economy and a large population of expats who move between the two countries for work, study and family. The good news for pet owners on this route is that both countries are EU member states -- which makes the move far simpler than most international pet relocations.

## It Is Intra-EU Travel

Moving a pet between France and Germany is regulated under **EU Regulation 576/2013** (non-commercial movement of companion animals within the EU). The rules apply equally to citizens of any nationality who are legally resident in France or Germany.

The requirements are:
1. **ISO microchip** (15-digit)
2. **Valid EU pet passport** -- or an AHC (Animal Health Certificate) for non-EU-origin animals
3. **Current rabies vaccination** recorded in the pet passport
4. That's it -- no titre test, no import permit, no quarantine for intra-EU moves

The EU pet passport is issued by a licensed veterinarian. It records microchip number, vaccinations, owner details and is valid for the lifetime of the animal. If your pet was vaccinated and microchipped in France and has a French EU pet passport, that document is fully recognised in Germany and vice versa.

## What About Titre Tests?

No titre test is required for intra-EU travel. The titre test requirement applies to animals entering the EU from third countries (non-EU), not to animals already resident in an EU country.

## Road Travel

France and Germany share borders at several crossing points between Alsace (Strasbourg, Mulhouse, Colmar area) and Baden-Wurttemberg/Rhineland-Palatinate on the German side. There are no routine border checks for pets crossing these frontiers within the Schengen area, but you should always carry your pet's EU passport in case of a random check.

## Flying

Direct flights between Paris (CDG, ORY) and the main German airports (Frankfurt FRA, Munich MUC, Berlin BER, Hamburg HAM, Dusseldorf DUS) are operated by **Lufthansa**, **Air France**, **easyJet** and **Vueling**, among others. For a short-haul intra-EU flight, carrying a small cat or dog in the cabin is the most practical option. Check each airline's cabin pet policy for weight limits and carrier requirements.

## German Registration

On arriving in Germany, dogs must be registered with the local municipality (Einwohnermeldeamt or equivalent) and a dog tax (Hundesteuer) applies. This is a local government fee, not a veterinary requirement, but it is mandatory and the local rates vary by municipality. Failure to register and pay the tax can result in a fine.

## French Export Documentation

No formal French export certificate is needed for intra-EU travel. The EU pet passport is sufficient. If for any reason you need to show the animal's French vaccination history, your French vet can provide a clinical certificate but this is supplementary to the passport.

---

**Sources:** European Commission EU pet travel rules (Regulation 576/2013); Lufthansa cabin pet policy; Air France pet travel guide; German Hundesteuer information.
"""},

# ─── 9. USA to Mexico pet transport guide ─────────────────────────────────────
{
"slug": "usa-to-mexico-pet-transport-guide",
"content": """---
title: "Pet Transport from USA to Mexico: Documents, Health Certificates and Entry Rules"
description: "How to take your cat or dog from the USA to Mexico. Covers USDA APHIS-endorsed health certificates, SENASICA requirements, approved entry points and whether a titre test is needed."
date: "2025-07-30"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/usa-to-mexico-pet-transport-guide/"
tags: ["usa", "mexico", "route guide", "north america", "pet transport"]
---

Mexico is one of the most popular destinations for American expats and snowbirds, and the US-Mexico route is one of the busiest pet relocation corridors in the world. The requirements are less onerous than most international moves -- no titre test, no quarantine in normal circumstances -- but the health certificate must be correctly issued and endorsed.

## Mexico's Pet Import Requirements

The Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria (SENASICA) under Mexico's Ministry of Agriculture (SADER) governs live animal imports.

For cats and dogs arriving from the USA, Mexico requires:

1. **USDA APHIS-endorsed health certificate** -- issued by a USDA-accredited veterinarian and endorsed by USDA APHIS Veterinary Services; must be issued within **15 days of entry to Mexico**; the endorsement confirms that USDA has reviewed and authenticated the vet's certification
2. **Current vaccinations** -- rabies vaccination (current, within valid period); for dogs: distemper, parvovirus, hepatitis are strongly recommended and often inspected; for cats: panleukopenia, herpesvirus, calicivirus
3. **Microchip** -- strongly recommended and increasingly checked; ISO-compliant chip is best practice

No titre test is required for the USA-to-Mexico route. No import permit is required for personal companion animals (as distinct from commercial imports).

## Getting the USDA APHIS Endorsement

This is the step that most people underestimate for timing:

1. Visit a USDA-accredited vet (not all vets are USDA accredited -- ask specifically before booking)
2. The vet completes the APHIS-format health certificate
3. You take or mail the certificate to your nearest USDA APHIS Veterinary Services area office for endorsement
4. Processing time varies: **same day to 5 business days** for walk-in or express mail; up to 2 weeks by regular mail

The health certificate must be endorsed no more than 15 days before your Mexico entry date. Plan the APHIS appointment accordingly.

## Driving vs Flying

**By road:** Thousands of pet owners drive across the US-Mexico border annually. The main crossing points that handle vehicle traffic (Tijuana, Nogales, El Paso, Laredo, McAllen) all have SENASICA inspection points. Have your endorsed health certificate readily accessible -- not buried in luggage. Inspectors scan for documentation quickly but randomly stop vehicles.

**By air:** Mexican airlines (Aeromexico, Volaris, VivaAerobus) and US carriers (American, United, Delta, Southwest) operate US-Mexico routes. Many of these airlines accept pets in the cabin for small animals (under 6-8 kg combined) or as cargo hold. Note that Mexico City's Benito Juarez International Airport (MEX) has specific live animal import procedures; confirm with the airline and SENASICA in advance.

## Return from Mexico to the USA

Bringing a pet back to the USA from Mexico requires a CDC-compliant health certificate for dogs (the CDC dog import rules apply; see the [CDC dog import rules guide](/blog/cdc-dog-import-rules-usa-explained/) for details). Dogs vaccinated in Mexico or with Mexican documentation need to meet CDC vaccination requirements, which changed significantly in 2024.

## Breed Restrictions

Mexico does not have a national breed ban list, but some Mexican states and municipalities have enacted breed-specific legislation. Verify local rules for your specific destination.

---

**Sources:** SENASICA, Mexico (gob.mx/senasica); USDA APHIS international pet travel; CDC dog importation requirements; Aeromexico live animal policy.
"""},

# ─── 10. Travelling with a Basset Hound internationally ───────────────────────
{
"slug": "travelling-with-a-basset-hound-internationally",
"content": """---
title: "International Travel with a Basset Hound: Airline Rules and Health Considerations"
description: "A Basset Hound owner's guide to international pet travel. Covers airline cargo policies, whether Bassets are classed as brachycephalic, crate sizing and documentation requirements."
date: "2025-07-31"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-basset-hound-internationally/"
tags: ["basset hound", "breed guide", "dog travel", "international pet travel"]
---

Basset Hounds are among the most recognisable breeds in the world -- those long ears, those deeply mournful eyes. They are also moderately heavy dogs with a few specific health considerations that are worth understanding before booking an international flight.

## Cabin or Cargo?

Adult Basset Hounds typically weigh between 23 and 29 kg and stand 33 to 38 cm at the shoulder. Despite being low to the ground, they are solidly built and will almost certainly travel in the **cargo hold** for international flights.

For a Basset Hound, you will typically need an IATA-compliant hard-shell crate in the **Kennel 400 or 500** size. Measure your individual dog -- the crate must allow the dog to stand (without the head touching the roof), turn around and lie in a natural position.

## Are Basset Hounds Brachycephalic?

This is a legitimate question. Basset Hounds have a moderately shortened muzzle compared to a Labrador or German Shepherd, and some individuals develop BOAS-related breathing issues. However, most major airlines do **not** classify the Basset Hound as a restricted brachycephalic breed in the same category as Pugs, French Bulldogs or English Bulldogs.

That said:
- Airlines with broad "snub-nosed" restrictions may include Basset Hounds in a grey area; **always confirm with the airline specifically** before booking
- A Basset Hound with diagnosed respiratory issues, loud snoring or exercise intolerance should be assessed by a vet for fitness to fly before any booking is made
- Temperature restrictions apply to all cargo animals; a Basset with any respiratory concerns is at higher risk in warm conditions

## Long Ears and Ear Health

Basset Hounds are prone to ear infections due to their long, pendulous ears which restrict airflow around the ear canal. Before any international flight, have the ears checked and cleaned by your vet. An active ear infection makes a cargo hold journey significantly more uncomfortable. Some owners tape the ears back gently during travel to keep them from dragging in the crate; discuss with your vet whether this is appropriate for your dog.

## Intervertebral Disc Disease (IVDD)

Basset Hounds are one of several chondrodystrophic breeds (long body, short legs) prone to IVDD -- a condition where the discs between vertebrae can rupture or bulge, causing pain or paralysis. For an older Basset or one with a history of back problems, a long crate journey needs careful consideration. Discuss fitness to fly with your vet and ensure the crate dimensions allow your dog to remain comfortable in a natural resting position.

## Country Requirements

No national breed restrictions apply to Basset Hounds in the UK, EU, USA, Australia, Canada or New Zealand. Standard documentation requirements apply: microchip, current vaccinations, health certificate and (for rabies-sensitive destinations) a titre test.

For popular destinations:
- [UK to Australia](/blog/uk-to-australia-pet-transport-complete-guide/)
- [USA to Germany](/blog/usa-to-germany-pet-transport-guide/)
- [USA to UK](/blog/uk-to-usa-pet-transport-cats-and-dogs/)
"""},

# ─── 11. Travelling with an Irish Wolfhound internationally ───────────────────
{
"slug": "travelling-with-an-irish-wolfhound-internationally",
"content": """---
title: "International Travel with an Irish Wolfhound: Giant Breed Logistics and Airline Rules"
description: "Moving internationally with an Irish Wolfhound? This guide covers crate sizing for giant breeds, which airlines accept large dogs, country restrictions and the unique challenges of this breed."
date: "2025-08-01"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-an-irish-wolfhound-internationally/"
tags: ["irish wolfhound", "breed guide", "giant breeds", "dog travel", "international pet travel"]
---

The Irish Wolfhound is one of the tallest dog breeds in the world. Adult males can stand over 80 cm at the shoulder and weigh up to 55 kg. For their owners, international relocation raises questions that simply do not apply to smaller breeds. Here is what you need to know.

## The Size Challenge

At 50 to 55 kg and over 80 cm tall, an Irish Wolfhound requires a very large crate. IATA regulations specify that the crate must be large enough for the dog to stand without its head touching the roof, turn around and lie in a natural position. For a dog of this stature, you are looking at a custom-built wooden crate or a very large plastic kennel in the **Kennel 700** range -- and even then, the dog's nose-to-tail length plus the head height may exceed what is available off the shelf.

Many Irish Wolfhound owners commission a custom wooden IATA-compliant crate built to the dog's measurements. This adds cost but ensures compliance. The crate dimensions for a large Irish Wolfhound will typically exceed the maximum crate dimensions accepted as standard cargo on narrow-body aircraft.

## Airline Acceptance: A Genuine Challenge

This is where Irish Wolfhound owners face the biggest practical hurdle. The combined weight of a large Irish Wolfhound plus crate may exceed 80 to 100 kg. Many airlines have per-piece cargo weight limits that exclude animals of this size from standard live animal cargo.

Options:
- **Dedicated pet air freight / charter**: companies that specialise in large animal air transport and have established relationships with cargo carriers for oversized live animals
- **Wide-body aircraft cargo only**: routes operated by 747, 777, A330, A350 or A380 aircraft have larger freight compartments; routing matters
- **Sea freight**: for routes where sea transport is feasible, a container service is worth investigating for very large dogs; the absence of altitude stress is a positive welfare consideration

Contact a specialist IPATA-member pet relocation agent before booking any route for an Irish Wolfhound -- standard online airline cargo booking processes are not designed for this weight class.

## Country Restrictions

Irish Wolfhounds are not restricted or banned in any major destination country under national legislation. They are not classified as dangerous dogs in the UK, EU, USA, Australia, Canada or New Zealand.

## Health Considerations

Irish Wolfhounds are deep-chested dogs at risk of bloat (gastric dilatation-volvulus, GDV). Do not feed your dog within 6 hours of travel. Ensure water is available in the crate. The stress of cargo travel elevates the risk of GDV; discuss this with your vet before a long international flight.

Wolfhounds also have a higher than average incidence of heart disease (dilated cardiomyopathy). A cardiac assessment before any international flight is advisable.

## Health Certificate and Documentation

Standard documentation requirements apply (microchip, vaccinations, health certificate, titre test where required). Confirm crate dimensions are noted on the air waybill and that the airline's cargo team is aware of the weight and size in advance of check-in day -- surprises at the cargo terminal with a 55 kg dog in a 100 kg crate tend not to end well.
"""},

# ─── 12. Travelling with a St Bernard internationally ─────────────────────────
{
"slug": "travelling-with-a-st-bernard-internationally",
"content": """---
title: "International Travel with a St Bernard: Large Dog Logistics and Airline Cargo Rules"
description: "Planning to relocate internationally with a St Bernard? This guide covers crate requirements for giant breeds, airline cargo acceptance, country breed restrictions and health considerations."
date: "2025-08-02"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-st-bernard-internationally/"
tags: ["st bernard", "saint bernard", "breed guide", "large dogs", "international pet travel"]
---

St Bernards are gentle giants with devoted owners, many of whom refuse to leave their dog behind when relocating internationally. The practical challenges are real but not insurmountable. Here is a straightforward guide to the key considerations.

## Size and Weight

Adult St Bernards typically weigh between 55 and 80 kg and stand 65 to 90 cm at the shoulder. Combined with the crate, you may be handling total cargo weights of 90 to 120 kg. This places a St Bernard in the same logistical category as Irish Wolfhounds and Great Danes -- well outside the range of standard cargo booking processes.

## Crate Requirements

You will need a large hard-shell crate or a custom-built wooden crate that meets IATA specifications. The key measurements are:
- **Length**: nose to base of tail, plus a few centimetres
- **Width**: width across shoulders, multiplied by 1.5 as a minimum
- **Height**: from floor to top of ears when standing, plus a few centimetres for clearance

For most adult St Bernards, this means a crate in the Kennel 700 range or a custom wooden build. Custom wooden crates can be made by specialist pet relocation suppliers and are sometimes the only practical option for dogs of this size.

## Airlines and Routing

The same constraints that apply to other giant breeds apply here. Wide-body aircraft routes (747, 777, A330, A350) have larger freight compartments and are more likely to accommodate oversized live animal crates. Narrow-body routes (A320, 737) are generally unsuitable.

Work with a specialist IPATA pet relocation agent rather than attempting to book direct. They have established relationships with cargo carriers for large animals and know which routes and which airlines can accommodate the specific dimensions and weight.

## Heat Sensitivity

St Bernards have a thick double coat and are a cold-weather breed. They do not tolerate heat well. Summer embargoes and temperature restrictions are particularly relevant for this breed. If you are relocating during warm months, the timing of your flight (early morning, late evening, winter shoulder season) and the routing via a cooler hub can make a meaningful difference.

Discuss with your vet the specific risks of heat stress for your dog and whether any precautions (such as a cooling pad in the crate during ground handling) are appropriate.

## Breed Restrictions

St Bernards are not subject to breed-specific legislation in the UK, EU, USA, Australia, Canada or New Zealand. They are not classified as dangerous dogs.

## Health Certificate and Timing

Standard documentation (microchip, vaccinations, health certificate, titre test where required by the destination country) applies. Given the logistics involved in arranging a suitable crate and airline slot for a large breed, start the planning process earlier than you would for a standard-sized dog -- ideally 6 to 9 months before your intended travel date.

---

For destination-specific requirements, see the relevant country import guides:
- [Australia pet quarantine](/blog/australia-pet-quarantine-explained/)
- [Japan pet import -- AQS rules](/blog/japan-pet-import-guide/)
- [Germany pet import](/blog/moving-pets-to-germany/)
"""},

# ─── 13. Travelling with a Portuguese Water Dog internationally ───────────────
{
"slug": "travelling-with-a-portuguese-water-dog-internationally",
"content": """---
title: "International Travel with a Portuguese Water Dog: Airline Policies and Country Rules"
description: "Planning international travel with a Portuguese Water Dog? This guide covers airline cargo and cabin policies, breed restrictions, crate sizing and documentation for this popular breed."
date: "2025-08-03"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-portuguese-water-dog-internationally/"
tags: ["portuguese water dog", "breed guide", "dog travel", "international pet travel"]
---

Portuguese Water Dogs -- Porties, as their owners often call them -- are athletic, intelligent dogs that handle novel environments better than many breeds. Their adaptability makes them a good candidate for international travel, and their medium size puts them in a manageable weight class for cargo transport.

## Cabin or Cargo?

Adult Portuguese Water Dogs typically weigh 16 to 23 kg. This is above most airlines' cabin pet weight limits (usually 6 to 8 kg combined). For international flights, Porties travel in the **cargo hold**.

The crate requirement is typically an IATA-compliant **Kennel 400** -- measure your individual dog using the nose-to-tail and height-at-ears method to confirm. A well-trained dog that is comfortable in its crate will handle cargo travel significantly better than an anxious or crate-naive one.

## Breed Restrictions by Country

Portuguese Water Dogs are not classified as dangerous or restricted in any major destination country. They do not appear on national breed ban lists in the UK, USA, EU, Australia, Canada or New Zealand.

## Coat and Water Exposure

Porties have a single-layer, non-shedding coat that can be either curly or wavy. The coat is relatively low-maintenance in a travel context -- it does not pick up debris easily and does not become matted as readily as some other water-resistant coats. Keep the coat clean and dry before travel; damp or dirty fur in a sealed crate is uncomfortable and can cause skin irritation.

If your Portie has been recently groomed (particularly a lion cut), the reduced coat coverage means less insulation in cold conditions. Factor this in if flying through cold-climate hubs in winter.

## Health and Exercise Before Flying

Portuguese Water Dogs are energetic. The best thing you can do before placing your Portie in a cargo crate for a long international flight is give them a good 2 to 3 hour walk or exercise session the day before travel and a moderate session 4 to 5 hours before cargo check-in. A physically tired dog will settle and sleep; an unexercised, high-energy dog will be miserable.

## Documentation

Standard documentation requirements apply:
- ISO microchip
- Current rabies vaccination
- Health certificate from an accredited vet, government-endorsed as required
- Titre test if the destination country requires it (Japan, Australia, New Zealand, UK for non-UK origin pets)
- Import permit where required

For popular expat destinations that the breed's country of origin (Portugal) is connected to, see:
- [UK to Portugal](/blog/uk-to-portugal-pet-transport-guide/)
- [USA to Germany](/blog/usa-to-germany-pet-transport-guide/)
- [USA to Ireland](/blog/usa-to-ireland-pet-transport-guide/)
"""},

# ─── 14. Relocating to Portugal with a pet ────────────────────────────────────
{
"slug": "relocating-to-portugal-with-a-pet",
"content": """---
title: "Relocating to Portugal with a Pet: An Expat's Complete Guide"
description: "A practical guide to moving to Portugal with a cat or dog. Covers EU pet passport rules, post-Brexit requirements for UK residents, microchip registration, vet access and life with a pet in Portugal."
date: "2025-08-04"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/relocating-to-portugal-with-a-pet/"
tags: ["portugal", "expat guide", "pet relocation", "europe"]
---

Portugal has climbed steadily up the expat popularity charts, and for good reason. The climate is gentle, the food is excellent, the people are welcoming and Lisbon and Porto have become genuinely cosmopolitan cities. If you are planning to move here with a cat or dog, this guide covers the practical side of what to expect.

## Where You Are Moving From Determines What You Need to Do

**From the UK (post-Brexit):**
UK pets no longer have EU pet passports recognised in Portugal. You need:
- ISO microchip (implanted before your rabies vaccination)
- Current rabies vaccination
- FAVN titre test (at an EU-approved lab; result 0.5 IU/ml or above; test done at least 30 days after vaccination)
- 3-month wait after a passing titre result before EU entry
- Animal Health Certificate (AHC) completed by a UK Official Veterinarian within 10 days of arrival
- TRACES NT pre-notification at the Lisbon (LIS) or Porto (OPO) border inspection post

**From EU countries:**
The EU pet passport is fully valid. Your pet needs a current rabies vaccination and ISO microchip. No additional paperwork for intra-EU moves.

**From the USA, Canada, Australia and other non-EU third countries:**
Third-country rules apply. These mirror the UK rules above: microchip, rabies vaccination, titre test (3-month wait), AHC or equivalent third-country health certificate endorsed by your country's government veterinary authority. See the [moving pets from non-EU to EU guide](/blog/moving-pets-non-eu-to-eu/) for a detailed breakdown.

## Arriving in Portugal

Lisbon Airport (LIS) and Porto Airport (OPO) both have Border Inspection Posts (BIPs) for third-country animal arrivals. For intra-EU arrivals, there is no border inspection required.

On arrival from a third country, a veterinary officer checks your documents and microchip. With complete paperwork, this is typically a 15 to 30 minute process. Keep originals and copies of everything.

## Registering Your Pet in Portugal

**Microchip registration:** Portugal uses the SIAC (Sistema de Identificacao de Animais de Companhia) database. All dogs (mandatory) and cats (recommended) must be registered. Your Portuguese vet can handle SIAC registration.

**Dog licence:** All dogs must be registered with the local Junta de Freguesia (parish council). The registration involves showing the microchip number, vaccination record and proof of identity. Annual renewal is required. Fines for unregistered dogs apply.

**Rabies vaccination:** Rabies vaccination is mandatory for dogs in Portugal. Your Portuguese vet will continue the vaccination schedule and update the records on the SIAC system.

## Finding a Vet in Portugal

The urban areas -- Lisbon, Porto, the Algarve and major coastal towns -- have good veterinary coverage. Rural areas in the Alentejo and interior have fewer options.

For English-speaking expats, many vet practices in Lisbon, Cascais, Sintra, Porto and the Algarve have English-speaking staff. Expat Facebook groups for Portugal are a good source of local vet recommendations.

## Life with a Pet in Portugal

Portugal is generally pet-friendly. Dogs are permitted in many outdoor cafe areas, public parks and beaches (seasonal restrictions apply on many Algarve beaches in summer). The Portuguese attitude toward dogs in public is relaxed and positive.

The climate suits most dog breeds well for most of the year -- summers in the south can be very hot (regularly above 35 degrees Celsius in July and August), which requires care for brachycephalic breeds and double-coated northern breeds.

---

**Sources:** SIAC pet registration system Portugal; DGAV (Direccao-Geral de Alimentacao e Veterinaria) Portugal; UK APHA guidance for EU travel; European Commission third-country pet travel rules.
"""},

# ─── 15. Relocating to Spain with a pet ───────────────────────────────────────
{
"slug": "relocating-to-spain-with-a-pet",
"content": """---
title: "Relocating to Spain with a Pet: Rules for UK, US and EU Arrivals"
description: "A practical guide to moving to Spain with a cat or dog. Covers post-Brexit paperwork for UK pets, third-country rules for US pets, EU pet passport rules and life with a dog in Spain."
date: "2025-08-05"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/relocating-to-spain-with-a-pet/"
tags: ["spain", "expat guide", "pet relocation", "europe"]
---

Spain remains one of the top three destinations for British expats and attracts significant numbers of American, Canadian and other non-EU nationals each year. The Costa del Sol, Barcelona, Valencia and the Canary Islands have well-established international communities -- and their pets come with them. Here is what you need to know.

## Arriving from the UK

Post-Brexit, UK pets need the full third-country import protocol:

1. **ISO microchip** (before any rabies vaccination that counts)
2. **Rabies vaccination** -- current; administered after microchipping
3. **FAVN titre test** at an EU-approved laboratory; result at least 0.5 IU/ml; test at least 30 days after vaccination
4. **3-month wait** after a positive titre result before entering Spain/EU
5. **Animal Health Certificate (AHC)** -- completed by a UK Official Veterinarian (OV) within 10 days of your arrival in Spain; endorsed by APHA if required
6. **TRACES NT notification** at the Spanish Border Inspection Post (BIP)

Main Spanish BIPs for air arrivals include Madrid Barajas (MAD), Barcelona El Prat (BCN) and Malaga Costa del Sol (AGP). For Canary Islands arrivals, Gran Canaria (LPA) and Tenerife South (TFS) also have processing capability -- confirm current BIP status before booking.

For detailed step-by-step UK-to-EU rules, see [EU pet travel post-Brexit](/blog/eu-pet-travel-post-brexit-uk-guide/).

## Arriving from the USA or Canada

The same third-country protocol applies: microchip, rabies vaccination, FAVN titre test, 3-month wait, endorsed health certificate. For USA-origin pets, the health certificate must be endorsed by USDA APHIS Veterinary Services.

## Arriving from EU Countries

If you are moving from another EU country, your EU pet passport is fully valid in Spain. No additional paperwork, no titre test, no border inspection beyond standard checks.

## Spanish Registration Requirements

**Microchip registration:** Spain uses regional registries managed by the autonomous communities (CCAA). In Catalonia, this is the RIVIA system; in Andalusia, the RAPAD system. Your Spanish vet registers the chip in the regional database.

**Dog licence and census:** Most Spanish municipalities require dogs to be registered on the municipal census (padron municipal de animales). The process varies by town hall (ayuntamiento). Your vet or local expat community can advise on the specific process where you live.

**Potentially dangerous breeds (PPP):** Spain has a national list of breeds classified as potentially dangerous (razas potencialmente peligrosas). This list includes: American Pit Bull Terrier, Rottweiler, Staffordshire Bull Terrier, American Staffordshire Terrier, Dobermann, Argentine Dogo, Fila Brasileiro, Tosa Inu and Akita Inu. Owners of PPP breeds must obtain a special licence, take out mandatory third-party liability insurance and comply with additional handling rules (muzzle, short lead, adult handler). Check whether your breed is on the PPP list before importing.

## Life with a Pet in Spain

Spain is broadly pet-friendly, with a strong culture of walking dogs in parks and along paseos. Many restaurants have outdoor terraces where well-behaved dogs are tolerated or welcomed. Spanish summers can be very hot -- the interior and southern regions regularly exceed 40 degrees Celsius in July and August, which is unsafe for outdoor exercise during midday hours.

Veterinary care is of high quality and generally less expensive than in the UK or USA. Vet practices in coastal and urban areas frequently have English-speaking staff.

---

**Sources:** APHA guidance UK-to-EU travel; USDA APHIS international travel; Real Decreto 287/2002 Spain PPP legislation; TRACES NT platform; DGAV Spain (MAPA).
"""},

# ─── 16. Pet transport cost-saving tips ───────────────────────────────────────
{
"slug": "pet-transport-cost-saving-tips",
"content": """---
title: "10 Ways to Reduce the Cost of International Pet Transport"
description: "International pet transport is expensive -- but there are real ways to cut the bill without cutting corners on welfare or compliance. This guide shares practical cost-saving strategies."
date: "2025-08-06"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/pet-transport-cost-saving-tips/"
tags: ["cost saving", "pet transport costs", "budget", "practical guide"]
---

International pet transport is not cheap. A full-service move from the UK to Australia can cost USD 3,000 to 5,000. A UK-to-USA move for a large dog runs USD 1,500 to 3,000. There are ways to reduce these costs without compromising on welfare or legal compliance -- but some apparent savings are false economies. Here is what actually works.

## 1. Start Planning Early

The single biggest cost driver is time pressure. When you have 6 months, you can shop multiple agents, wait for airline cargo availability at better rates and meet documentation deadlines without paying for express government endorsements. When you have 3 weeks, you pay premium rates for everything.

Start the process as soon as relocation becomes a realistic possibility, even if the date is uncertain.

## 2. Compare Multiple Agents

IPATA (International Pet and Animal Transportation Association) members compete for business. Get quotes from at least 3 agents, ensure the quotes cover the same scope (door to door vs airport to airport makes a large cost difference) and ask each agent what the quote includes and excludes.

See [how to choose a pet relocation company](/blog/how-to-choose-a-pet-relocation-company/) for the right questions to ask.

## 3. Know What You Can DIY

Many parts of the process do not require an agent:
- Booking the title test at the lab directly
- Organising your own USDA APHIS or APHA endorsement appointment
- Completing your own TRACES NT notification (for EU arrivals) with guidance
- Purchasing the IATA-compliant crate yourself (rather than through the agent at a mark-up)

A partial DIY approach -- handling document preparation yourself and only using the agent for the airline cargo booking and airport handling -- can cut costs by 20 to 40%.

## 4. Buy the Crate Yourself

Agents often supply IATA crates as part of a package at a significant mark-up. An IATA-compliant crate purchased directly from a pet supplies retailer or manufacturer costs USD 80 to 250 depending on size. The same crate via an agent may cost USD 200 to 500.

Buy the correct size crate yourself, well in advance, and use it for crate training.

## 5. Choose Your Route Strategically

Some routings are significantly cheaper than others because of airline competition. For example, USA-to-EU routes through Amsterdam (AMS) or Frankfurt (FRA) often have more cargo competition and lower rates than smaller hub connections.

Talk to your agent or do independent cargo rate research before assuming one routing is fixed.

## 6. Avoid Peak Season

Summer (June to August in the Northern Hemisphere) and the Christmas holiday period see both higher demand and more embargoes that force rerouting and rebooking costs. Moving in spring (March to May) or autumn (September to November) often gives you better availability and lower rates.

## 7. Travel Yourself in the Same Booking

For pets travelling as excess baggage (not as separate cargo freight), booking your own ticket and the pet on the same airline booking is often cheaper than booking the pet cargo separately. Some airlines offer reduced rates for pets travelling on the same reservation as the owner.

## 8. Use a Titre Test Result That Is Already Valid

If your pet has a current titre test on record and rabies boosters are maintained, you do not need to repeat the titre test for a second international move. Titre tests cost USD 150 to 250 plus lab fees. A valid prior result saves this cost entirely.

## 9. Book Government Endorsements Yourself

USDA APHIS and UK APHA endorsements are priced at a set government fee (typically USD 38 to 100 per endorsement for USDA; a similar range for APHA). Agents sometimes mark up the cost of arranging this appointment. You can book USDA APHIS appointments directly and take or mail your vet certificate yourself.

## 10. Do Not Under-Insure

This sounds counterintuitive in a cost-saving guide, but inadequate insurance can create costs far greater than the premium. Pet transport insurance that covers the cargo journey, emergency veterinary care on arrival and quarantine costs if required protects against catastrophic outlays. See [pet transport insurance explained](/blog/pet-transport-insurance-explained/) for what to look for.
"""},

# ─── 17. Cabin vs cargo: which is better for your dog ────────────────────────
{
"slug": "cabin-vs-cargo-which-is-better-for-your-dog",
"content": """---
title: "Cabin vs Cargo: Which Is Better for Your Dog on an International Flight?"
description: "Should your dog fly in the cabin or the cargo hold? This guide breaks down the welfare, cost and practical differences to help you make the right decision for your individual dog."
date: "2025-08-07"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/cabin-vs-cargo-which-is-better-for-your-dog/"
tags: ["cabin vs cargo", "dog travel", "airline pet policy", "welfare guide"]
---

Every dog owner asks this question before an international flight: is it better for my dog to fly in the cabin with me, or in the cargo hold? The honest answer is that it depends on your dog's size, temperament and health -- and on the specific route and airline. Here is a clear breakdown.

## Who Can Fly in the Cabin?

Most airlines restrict cabin pets to those with a combined weight (dog plus carrier) of **6 to 8 kg**. Some airlines extend this to 10 kg on specific routes. In practice, this means:

- Chihuahuas, Maltese, Toy Poodles, small Dachshunds and most cats: potentially eligible
- Miniature Schnauzers, Pugs, Jack Russells, Bichon Frise (some individuals): borderline; weigh carefully including the carrier
- Border Collies, Labradors, German Shepherds and almost all medium to large breeds: cargo hold only

If your dog weighs more than 6 kg, you do not have a cabin vs cargo choice on most international flights. The cargo hold is your only option.

## Welfare in the Cabin

Flying in the cabin has obvious advantages for the dog: they are near you, they can hear and smell you, and they have access to the microclimate of the passenger cabin. For anxious dogs that are bonded to their owner, the cabin is genuinely less stressful.

However:
- The dog must stay inside the carrier under the seat for the entire flight -- typically 2 to 14 hours depending on the route
- A dog that is not comfortable being confined cannot be let out
- Flights over approximately 8 hours with no access to a toilet area create discomfort for most dogs

## Welfare in the Cargo Hold

The cargo hold of a modern wide-body aircraft is pressurised and temperature-controlled. It is not the dark, freezing freight compartment that many people imagine. For a calm, crate-trained dog, cargo travel is manageable.

- The dog has more space in the crate than under an aircraft seat
- Longer-bodied and heavier dogs can lie in a more natural position
- Multiple hours in a crate is something dogs do routinely at home (overnight, for example)

The primary welfare risks in cargo are: heat stress on the tarmac or in an un-cooled hold during delays, anxiety in dogs that are not crate trained, and respiratory difficulty in brachycephalic breeds.

## The Size Factor as a Decision Maker

For dogs over 6 to 8 kg, the decision is made for you: cargo hold. For dogs under 6 kg, you have a choice on many airlines and routes. This is where it gets genuinely individual:

- A 4 kg Chihuahua that sleeps 14 hours a day and is perfectly calm in a carrier: cabin is comfortable and practical
- A 4 kg Chihuahua that pants, whines, tries to escape and has never been in a carrier before a 10-hour flight: cargo may actually be less stressful because the dog is in a covered, dark crate and not surrounded by the sensory overload of a passenger cabin

Honest self-assessment of your dog's temperament and prior carrier experience matters more than a blanket "cabin is always better" assumption.

## Country Restrictions

Some destination countries affect the cabin vs cargo choice regardless of size:
- **Japan**: pets must arrive via approved cargo channels; cabin arrival does not bypass AQS quarantine requirements
- **Australia**: all arrivals go through DAFF quarantine regardless of how the animal traveled
- **UK (for non-UK origin pets)**: specific APHA documentation requirements apply; confirm whether cabin or cargo arrival affects the inspection process

---

**Sources:** IATA Live Animals Regulations (LAR) 50th Edition; RSPCA guidance on flying with pets; BSAVA guidance on fitness to fly.
"""},

# ─── 18. Pet documentation errors to avoid ────────────────────────────────────
{
"slug": "pet-documentation-errors-to-avoid",
"content": """---
title: "10 Pet Documentation Errors That Can Derail Your International Move"
description: "The most common pet transport documentation mistakes -- and how to avoid them. From microchip sequencing errors to expired health certificates, these are the errors that get animals detained."
date: "2025-08-08"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/pet-documentation-errors-to-avoid/"
tags: ["pet documentation", "common mistakes", "health certificate", "import permits", "practical guide"]
---

Every year, animals are detained, quarantined or refused entry at borders because of documentation errors that could have been prevented. Some of these errors are subtle. Others are obvious in retrospect. Here are the ten most common -- and how to avoid them.

## 1. Microchip Implanted After the Vaccination It Is Supposed to Validate

The rule: the ISO microchip must be implanted **before** any vaccination that you intend to use as part of the travel protocol. If the vaccination was given first and the chip implanted second, that vaccination cannot count. The clock must restart from the chip implant date.

This error is more common than it should be. Confirm the sequence in your pet's records before assuming everything is in order.

## 2. Rabies Vaccination Given Before the Chip Was Recorded in the Vet's Notes

A subtler version of the above: the chip was implanted before the vaccination, but the vet's system had not updated the record to include the chip number before the vaccine was administered. The physical sequence was correct but the paper trail shows the vaccine before the chip.

Always ask your vet to confirm the chip number is recorded against the consult before they administer any vaccinations in the protocol.

## 3. Health Certificate Not Government-Endorsed

A health certificate signed by your vet is not the same as one that has been government-endorsed. For most international destinations, the health certificate must be endorsed by:
- **USDA APHIS** (for USA-origin pets)
- **UK APHA** (for UK-origin pets)
- **CFIA** (for Canada-origin pets)
- **DAFF** (for Australia-origin pets)
- The relevant national veterinary authority for all other countries

An unendorsed certificate is not accepted at borders. Book the endorsement appointment well in advance -- it cannot be done the same day you pick up the certificate in most countries.

## 4. Health Certificate Issued Too Early

Health certificates have a validity window. For most international destinations, the certificate must be issued within **10 days of travel**. A certificate issued 15 or 20 days before departure is invalid on arrival. The vet appointment must be timed precisely.

## 5. Titre Test Done at a Non-Approved Laboratory

Japan, Australia, New Zealand, the EU (for third-country animals) and several other destinations require the titre test to be conducted at a laboratory on a specific approved list. A titre test done at a reputable but non-approved lab produces a result that is not recognised by the destination country's authorities.

Always verify the lab is on the approved list **before** collecting the blood sample.

## 6. Titre Test Result Below the Threshold

The FAVN titre test must produce a result of at least **0.5 IU/ml** to be accepted. A result of 0.4 IU/ml means the test must be repeated -- and the waiting period starts again from the new test date.

Ensure your pet's rabies vaccination is fully current before testing. A booster given close to the test date may not have produced full antibody levels by the time the blood is drawn.

## 7. Import Permit Expired on Arrival

Import permits have validity windows. An import permit for Barbados, Jamaica or India is valid for a specific period from the date of issue. If your travel date falls outside that window, you are arriving without a valid permit.

Check the expiry date when the permit arrives and confirm your travel date is within the window.

## 8. Wrong Format Health Certificate

Many countries specify a particular format or template for the health certificate. Japan, China, Australia and others provide their own template that must be used. A vet using a general health certificate format rather than the country-specific template can result in a rejection at the border.

Download the destination country's specific certificate template (available from the destination country's government veterinary authority website) and give it to your vet well before the appointment.

## 9. Tapeworm Treatment Not Given at the Right Time

For dogs entering the UK (from non-UK-origin) and some other destinations, a tapeworm (Echinococcus) treatment must be given within a specific window -- typically 24 to 120 hours before arrival. A treatment given outside this window (too early or skipped entirely) is grounds for refusal or additional quarantine.

## 10. Not Notifying the Destination BIP in Advance

Many countries require advance notification of a live animal arrival at the Border Inspection Post (BIP). For EU arrivals via TRACES NT, this pre-notification triggers the BIP to have an inspector available. Arriving without pre-notification can result in a long wait or, at busy BIPs, a rescheduled inspection the following day.

---

**Sources:** EU Regulation 576/2013 pet travel rules; USDA APHIS international travel requirements; Animal Quarantine Service Japan (MAFF); Australian DAFF export and import requirements; IATA Live Animals Regulations.
"""},

# ─── 19. Moving to South Africa with a pet ────────────────────────────────────
{
"slug": "moving-to-south-africa-with-a-pet",
"content": """---
title: "Moving to South Africa with a Pet: Import Rules, Permits and Life in SA"
description: "A practical guide to relocating to South Africa with a cat or dog. Covers DAFF import permits, endorsed health certificates, approved entry airports and what to expect on arrival."
date: "2025-08-09"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-south-africa-with-a-pet/"
tags: ["south africa", "expat guide", "pet relocation", "africa"]
---

South Africa has a large and diverse expat community, particularly in Cape Town, Johannesburg, Durban and Pretoria. The country has a well-developed veterinary infrastructure and a culture that is broadly welcoming to pets. Importing a cat or dog is straightforward if the paperwork is managed correctly.

## Who Regulates Pet Imports into South Africa?

The Department of Agriculture, Land Reform and Rural Development (DALRRD) -- specifically the Directorate Animal Health -- regulates live animal imports. The process begins with obtaining an import permit.

## Core Requirements

For cats and dogs arriving from the UK, USA, Europe, Australia and other recognised countries:

1. **Import permit** from DALRRD -- apply at least 3 to 4 weeks before travel; permits are issued for a specific period and must not have expired before your travel date
2. **ISO microchip** (15-digit)
3. **Rabies vaccination** -- current; for most countries, the rabies vaccine must have been administered at least 30 days before the date of the import permit application
4. **Core vaccinations** -- dogs: distemper, parvovirus, hepatitis, kennel cough; cats: panleukopenia, herpesvirus, calicivirus; all current
5. **Official health certificate** -- completed by a licensed veterinarian in the country of origin and endorsed by the government veterinary authority of that country; issued within 10 days of travel
6. **External parasite treatment** (ticks and fleas) within 7 days of travel
7. **Internal parasite treatment** within 3 weeks of travel

A rabies antibody titre test (FAVN) is **not** currently required for pets arriving from the UK, USA and most European countries, which simplifies the timeline considerably compared to destinations like Japan or Australia.

## Entry Points

DALRRD designates specific ports of entry for live animal imports. The main approved airports are:
- **O.R. Tambo International Airport, Johannesburg (JNB)** -- the primary hub
- **Cape Town International Airport (CPT)**
- **King Shaka International Airport, Durban (DUR)**

Most international flights routing to South Africa go through Johannesburg or Cape Town. Confirm that your specific arrival airport can process the import on the day you arrive.

## Quarantine

South Africa does not impose a mandatory quarantine for pets arriving from most recognised countries with complete documentation. Your pet is inspected by a DALRRD veterinary officer on arrival and released after documents and microchip are verified.

## Life with a Pet in South Africa

South Africa has good veterinary care in urban areas. Cape Town, Johannesburg, Pretoria and Durban have modern vet practices. Some expat pets arrive from countries where certain parasites and diseases are rare or absent -- South Africa has tick-borne diseases (including ehrlichiosis and babesiosis), which your vet in SA will advise on prevention for.

Security in urban areas influences how pets are kept: most homes in gated communities have dogs as part of their security profile. Regular off-lead exercise in secure parks is available in Cape Town's southern suburbs and green areas. Joburg has dog-friendly parks as well.

For breed restrictions: South Africa has no national breed ban list, though some insurance policies and sectional title complexes (apartments) have their own pet restrictions.

---

**Sources:** Department of Agriculture, Land Reform and Rural Development, South Africa; DALRRD import permit guidelines; OIE/WOAH country profile South Africa.
"""},

# ─── 20. How to find pet-friendly housing abroad ──────────────────────────────
{
"slug": "how-to-find-pet-friendly-housing-abroad",
"content": """---
title: "How to Find Pet-Friendly Housing When Moving Abroad"
description: "Practical advice on finding accommodation abroad that accepts cats and dogs. Covers where to search, what to say to landlords, lease clauses to watch for and countries with pet-friendly rental cultures."
date: "2025-08-10"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/how-to-find-pet-friendly-housing-abroad/"
tags: ["pet-friendly housing", "expat guide", "renting abroad", "practical guide"]
---

One of the hardest parts of international relocation with a pet is something most guides do not cover well: actually finding somewhere to live. Clearing customs and quarantine is only half the battle. Showing up in a new country with a large dog and no housing sorted is a situation many expats have found themselves in. Here is how to avoid it.

## Start Before You Leave

The golden rule: secure housing before you land. This is harder in some countries than others -- some rental markets (especially in hot cities like Lisbon, Amsterdam or Sydney) move so quickly that good properties are gone before you arrive. But arriving without a confirmed address creates a cascade of problems: where does your pet go from the airport? Where do you both sleep on night one?

Options:
- **Serviced apartments**: usually more pet-friendly than standard rental properties; the short-term nature of the agreement and the commercial operation model tends to make pet policies more flexible; more expensive but provides a base to search from
- **Airbnb / VRBO**: check the "pets allowed" filter; useful for the first 2 to 4 weeks while you search for permanent accommodation
- **Expat housing Facebook groups**: often have landlords who specifically target expats and are accustomed to pets

## Which Countries Are Most Pet-Friendly for Renters?

**Broadly pet-friendly rental cultures:**
- **Germany**: Germans are generally enthusiastic dog owners; many landlords accept pets, especially dogs, particularly if you offer a pet deposit
- **Netherlands**: Amsterdam and other Dutch cities have more pet-acceptable housing than the EU average; check "huisdieren toegestaan" (pets permitted) in listings
- **Spain**: private landlords in coastal and rural areas tend to be flexible; apartment blocks in cities can be stricter
- **Portugal**: generally pet-accepting landlord culture outside Lisbon's competitive market
- **New Zealand**: pet bonds are allowed (additional deposit for pets) which makes many landlords more willing

**Markets where finding pet-friendly housing is harder:**
- **Japan**: many Japanese rental contracts explicitly exclude pets (pets not permitted is common in standard apartment leases); look for "ペット可" (pets permitted) listings specifically; expat-targeted housing agencies often have better access to pet-friendly properties
- **Singapore**: most HDB (public housing) rules restrict pets, particularly large dogs; private condominiums have their own rules; most condominiums allow cats and small dogs but have breed restrictions on dogs
- **UAE**: residential leases vary; most villa compounds allow pets; many apartment buildings do not; check explicitly and get pet permission in writing

## How to Approach Landlords About Pets

- Be upfront early -- mentioning a large dog at the lease signing stage rather than at the viewing will save everyone time
- Offer a pet deposit (typically one month's rent is reasonable) to cover any damage
- Provide references from a previous landlord confirming your pet caused no damage
- Offer professional carpet/upholstery cleaning at the end of tenancy as a standard clause
- For cats, note that cats are generally viewed as less risky than dogs by landlords

## Lease Clauses to Watch For

- "No pets" clauses in standard lease templates are common in many countries; a verbal agreement to allow your pet that is not reflected in a lease addendum provides no legal protection
- Some leases specify "no pets" but mean "no large pets" -- clarify in writing
- If the landlord agrees to pets, ensure the lease addendum specifies the species, breed and maximum number of animals
- Check whether the lease restricts the maximum size (weight or breed) of the animal

## Online Resources

- **Rentola.com**, **Rightmove Overseas**, **Idealista** (Spain/Portugal), **Funda** (Netherlands), **ImmobilienScout24** (Germany) -- most major property portals allow you to filter by "pets welcome"
- **InterNations.org** expat groups for your destination city: a direct question on the forum often yields the best local agent or landlord contacts
- Country-specific expat Facebook groups: for every major expat destination city, there is a large Facebook group where members actively help each other find pet-friendly housing

---

**Sources:** Expat housing survey data; rental law summaries for Germany (BGB), Netherlands, Spain, Japan, Singapore; IPATA member agent guidance on pre-arrival housing.
"""},

]

written = 0
skipped = 0

for article in ARTICLES:
    slug = article["slug"]
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(article["content"].strip())
    print(f"WRITTEN: {slug}")
    written += 1

print(f"\nDone. Written: {written}, Skipped: {skipped}")
