"""
Blog Batch 19 - PetTransportGlobal
20 articles: country/destination guides, route guides, breed guides, practical guides
ASCII-only content. Skip-if-exists logic.
"""

import os

OUTPUT_DIR = r"site\content\blog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARTICLES = [

# ─── 1. Cuba pet import guide ──────────────────────────────────────────────────
{
"slug": "cuba-pet-import-guide",
"content": """---
title: "Importing a Pet to Cuba: Rules, Permits and What You Need to Know"
description: "A practical guide to importing a cat or dog to Cuba. Covers the health certificate and government endorsement process, vaccination requirements, Havana airport procedures and what to expect."
date: "2025-08-20"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/cuba-pet-import-guide/"
tags: ["cuba", "caribbean", "country guide", "pet import"]
---

Cuba receives fewer international pet relocations than most Caribbean destinations, partly because of the historical restrictions on travel and commerce between Cuba and the United States, and partly because the process is less publicised in English-language sources. For those moving to Cuba on diplomatic, aid, academic or other visas, bringing a companion animal is possible with the right preparation.

## Regulatory Authority

The Centro Nacional de Sanidad Agropecuaria (CENSA) and the Ministerio de la Agricultura (MINAG) govern live animal imports into Cuba. The veterinary inspection at the port of entry is carried out by the Servicio Estatal de Sanidad Vegetal (SESV) or the equivalent veterinary authority at the airport.

## Core Requirements

For cats and dogs arriving in Cuba from most countries:

1. **ISO microchip** -- 15-digit standard; increasingly expected though enforcement has historically varied
2. **Rabies vaccination** -- current and within valid period; primary vaccination at least 30 days before travel
3. **Core vaccinations** -- dogs: distemper, parvovirus, hepatitis, leptospirosis; cats: panleukopenia, herpesvirus, calicivirus
4. **Official health certificate** -- completed by a licensed veterinarian in the country of origin and endorsed (apostilled or authenticated) by the government veterinary authority; the certificate must in many cases also be authenticated by the Cuban consulate in the country of origin
5. **Import permit** -- coordinated through the relevant Cuban ministry or agency for your category of entry; diplomatic and official missions typically handle this through their embassy channel; NGO workers and other foreign residents should confirm the current import process with MINAG or their Cuban host organisation well in advance

A rabies titre test is not routinely required, but this can change depending on the country of origin and current MINAG guidance. Confirm current requirements before assuming no titre test is needed.

## USA-to-Cuba Context

Travel between the USA and Cuba is subject to US Treasury OFAC licensing requirements. US citizens may travel to Cuba under specific authorised categories. For pet import purposes, the Cuban-side requirements are as described above, but the logistics of routing (there is no direct commercial pet cargo service between most US airports and Havana as of the current date) mean that many USA-origin pets travelling to Cuba route via a third country such as Mexico, Panama or the Dominican Republic. Confirm the routing with your airline and with a specialist pet relocation agent before booking.

## Entry Airport

Jose Marti International Airport in Havana (HAV) is the main international gateway. Juan Gualberto Gomez International Airport in Varadero (VRA) and other regional airports handle some international traffic but are not the recommended entry point for live animal arrivals.

## Life with a Pet in Cuba

Cuba has a growing culture of pet ownership, particularly in Havana. Veterinary services exist in the main cities, though access to specialist pharmaceuticals and specialist veterinary care is more limited than in most Western countries. Many expats bring a supply of their pet's regular medications, flea/tick prevention and prescription food if applicable.

---

**Sources:** CENSA Cuba; Ministerio de la Agricultura Cuba; OIE/WOAH country profile for Cuba; US Treasury OFAC Cuba travel guidance.
"""},

# ─── 2. Iceland pet import guide ───────────────────────────────────────────────
{
"slug": "iceland-pet-import-guide",
"content": """---
title: "Importing a Pet to Iceland: MAST Rules, EEA Status and Biosecurity Requirements"
description: "How to import a cat or dog to Iceland. Covers MAST permit requirements, Iceland's EEA status for pet travel, whether a titre test is needed, approved entry points and health certificate format."
date: "2025-08-21"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/iceland-pet-import-guide/"
tags: ["iceland", "reykjavik", "EEA", "country guide", "pet import", "scandinavia"]
---

Iceland is in the European Economic Area (EEA) and aligns closely with EU standards on animal health, but it is not an EU member state. For pet import purposes, Iceland applies rules broadly equivalent to EU third-country import regulations for animals arriving from outside the EEA. The Icelandic Food and Veterinary Authority (Matvaela- og Vetterinaeriradvuneyti, known as MAST) is the regulatory body.

## Iceland's Status for Pet Travel

**From EU and EEA countries (excluding Iceland itself):** An EU pet passport with a current rabies vaccination and ISO microchip is generally accepted. Iceland participates in the EEA single animal health area and recognises EU pet passports.

**From the UK (post-Brexit):** The UK is now a third country for EEA/EU purposes. An Animal Health Certificate (AHC), ISO microchip, current rabies vaccination and evidence that the animal meets Iceland's import requirements apply. Iceland aligns with EU third-country rules for UK pets -- confirm whether the UK is on Iceland's approved non-EEA third country list and whether a titre test is required with MAST directly before travel.

**From the USA, Canada, Australia and other non-EEA countries:** Third-country import rules apply. These typically include: ISO microchip, rabies vaccination, FAVN titre test at an approved laboratory, and the applicable waiting period, plus a government-endorsed health certificate in a format acceptable to MAST.

## Import Permit

An import permit from MAST is required before importing a pet to Iceland. Apply at least 4 weeks before travel. MAST can be contacted at: mast@mast.is (confirm current contact details on the MAST website).

## Approved Entry Points

Keflavik International Airport (KEF), operated as Reykjavik/Keflavik, is the only international airport in Iceland for practical purposes. All commercial international flights arrive here. The veterinary inspection on arrival is carried out by the Border Inspection Post (BIP) at KEF.

Pre-notification of your arrival at the BIP is required. This is typically coordinated through the TRACES NT system for EU/EEA arrivals or through direct pre-arrival notification to MAST for non-EEA arrivals.

## Biosecurity Context

Iceland has a unique position as an island nation with very limited agricultural exposure to many of the diseases that are endemic in mainland Europe and Asia. The country has historically maintained very strict biosecurity. Horses, in particular, face a blanket import ban (once an Icelandic horse leaves Iceland, it cannot return). Cats and dogs are not subject to such extreme restrictions, but the overall framework is conservative by EEA standards.

## Living in Iceland with a Pet

Reykjavik has a compact urban core with good green space. Iceland has a cold, damp climate with very long winter nights in the far north, but the main population areas in the southwest are not as extreme as their latitude suggests. Veterinary care is available in Reykjavik; more rural areas have limited access. Vaccinations must be kept current as Iceland registers pets with a national database.

---

**Sources:** MAST (Icelandic Food and Veterinary Authority, mast.is); European Commission EEA pet travel framework; IATA Live Animals Regulations 50th Edition.
"""},

# ─── 3. Moving to Germany with a pet ───────────────────────────────────────────
{
"slug": "moving-to-germany-with-a-pet",
"content": """---
title: "Moving to Germany with a Pet: EU Passport, Third-Country Rules and Registration"
description: "A complete guide to relocating to Germany with a cat or dog. Covers EU pet passport rules, post-Brexit requirements for UK pets, USA third-country rules, Hundesteuer, breed restrictions by state."
date: "2025-08-22"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-germany-with-a-pet/"
tags: ["germany", "expat guide", "pet relocation", "europe", "eu pet travel"]
---

Germany is one of Europe's most popular expat destinations, home to a large international community across Berlin, Munich, Hamburg, Frankfurt, Cologne and beyond. For pet owners, the good news is that Germany's urban culture is genuinely dog-friendly. The less good news: the registration requirements and breed-specific laws vary by state, which adds a layer of complexity.

## Bringing Your Pet to Germany: What You Need

**From EU countries:**
Your EU pet passport and current rabies vaccination are sufficient. No titre test, no import permit. The EU pet passport is valid across all member states under EU Regulation 576/2013.

**From the UK (post-Brexit):**
UK pets are treated as third-country animals. You need:
- ISO microchip (implanted before vaccinations)
- Current rabies vaccination
- FAVN titre test at an EU-approved lab (result 0.5 IU/ml or above), at least 30 days after vaccination
- 3-month wait from a positive titre result before entering Germany/EU
- Animal Health Certificate (AHC) completed by a UK Official Veterinarian within 10 days of arrival
- TRACES NT pre-notification at Frankfurt Airport (FRA) or another German BIP

**From the USA, Canada and other non-EU countries:**
The same third-country protocol applies: microchip, rabies vaccination, titre test and 3-month wait, government-endorsed health certificate in the EU third-country format, TRACES NT notification at a German BIP. Frankfurt (FRA) and Munich (MUC) airports both have BIP facilities.

## Registering Your Pet in Germany

**Microchip registration:** Germany does not have a single national microchip database; chips are registered with regional databases. The TASSO and Findefix databases are the most widely used. Your German vet will register your pet when you first present. Keep records of the registration confirmation.

**Dog tax (Hundesteuer):** Every dog owner in Germany must register their dog with the local municipality (Gemeinde or Stadtverwaltung) and pay the Hundesteuer annually. Rates vary considerably: from around EUR 90 per year in smaller towns to EUR 200 or more per year in cities. Cats do not pay a Hundesteuer in Germany.

**Dog registration (Tierhalter-Registrierung):** When you register with the local residents' office (Einwohnermeldeamt), you will also register as a dog keeper. Failure to register a dog is a fine-able offence.

## Breed Restrictions in Germany

Germany's breed-specific legislation (Rasseliste) is administered at the state (Land) level, which means the rules differ between Bavaria (Bayern), North Rhine-Westphalia (Nordrhein-Westfalen), Lower Saxony (Niedersachsen) and other states.

**Generally restricted breeds** (rules vary; this is a general guide only -- confirm with the relevant state authority):
- American Pit Bull Terrier
- American Staffordshire Terrier
- Staffordshire Bull Terrier
- Bull Terrier (in some states)
- Rottweiler (in some states, subject to character assessment)
- Tosa Inu

Owners of listed breeds typically need to obtain a special permit, pass a character assessment (Wesenstest) for the dog, and may need additional liability insurance.

## Finding a Vet in Germany

Germany has an excellent density of veterinary practices. Major cities have 24-hour emergency clinics. German veterinary practices often have English-speaking staff in expat-dense areas (Berlin Mitte, Munich international suburbs, Frankfurt's expat quarters).

---

**Sources:** European Commission EU pet travel rules; UK APHA guidance on EU travel post-Brexit; TRACES NT platform; German state breed restriction legislation (Rasseliste); TASSO microchip registry (tasso.net).
"""},

# ─── 4. Moving to the Netherlands with a pet ───────────────────────────────────
{
"slug": "moving-to-netherlands-with-a-pet",
"content": """---
title: "Moving to the Netherlands with a Pet: EU Rules, Chip Registration and Amsterdam Life"
description: "Everything you need to know about relocating to the Netherlands with a cat or dog. Covers EU pet passport rules, third-country requirements for UK and US pets, LICG database, and life in Amsterdam."
date: "2025-08-23"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-netherlands-with-a-pet/"
tags: ["netherlands", "amsterdam", "expat guide", "pet relocation", "europe"]
---

The Netherlands is a consistently popular destination for expats working in tech, finance, logistics and international organisations. Amsterdam, Rotterdam, The Hague and Eindhoven have large international communities. The Dutch are, as a generalisation, enthusiastic dog owners -- which makes everyday life with a pet in the Netherlands quite pleasant.

## Importing Your Pet to the Netherlands

**From EU countries:**
EU pet passport, ISO microchip, current rabies vaccination. No import permit, no titre test, no border inspection for intra-EU moves. The Netherlands applies EU Regulation 576/2013 for companion animal movement within the EU.

**From the UK (post-Brexit):**
The UK is a third country. Requirements: ISO microchip, rabies vaccination, FAVN titre test (0.5 IU/ml or above, at least 30 days after vaccination), 3-month wait after a positive titre result, AHC completed by a UK Official Veterinarian within 10 days of arrival. TRACES NT pre-notification is required at Amsterdam Schiphol Airport (AMS) or Rotterdam Airport (RTM). Schiphol has a dedicated BIP with regular veterinary inspection capability.

**From the USA, Canada and other non-EU countries:**
Same third-country protocol: microchip, vaccination, titre test, 3-month wait, USDA/CFIA/equivalent-endorsed health certificate, TRACES NT notification at AMS.

## Microchip Registration in the Netherlands

The Netherlands uses the **LICG** (Landelijk Informatiecentrum Gezelschapsdieren) database system. Your vet in the Netherlands will register your pet's chip on presentation. This is not a legal requirement in the same way as Germany's Hundesteuer, but it is strongly recommended for reunification purposes. The Dutch RDW (vehicle authority) also provides dog taxation in some municipalities.

## Dog Tax in the Netherlands

Most Dutch municipalities (gemeenten) levy a dog tax (hondenbelasting). The rate varies by municipality: in Amsterdam it is abolished in some boroughs, in others it remains. Check the specific policy for your municipality of residence. Only the first dog is taxable in most municipalities; the rate for a second dog is higher.

## Life in the Netherlands with a Pet

Amsterdam is genuinely one of the most dog-friendly capitals in Europe. Dogs are welcome in most cafes, some restaurants, on the GVB metro and many shops. The extensive network of parks (Vondelpark, Amstelpark, Gaasperplaspark) provides good daily walking. Off-lead areas are available in many parks.

The Netherlands is flat, which makes it easy terrain for dogs of any age or fitness level. The climate is mild and damp -- neither very hot nor very cold -- which suits most breeds.

Dutch veterinary care is of high quality. Animal emergency hospitals (Dierenkliniek or Universiteitskliniek) operate in Amsterdam, Utrecht and other cities. The University of Utrecht has one of the top veterinary faculties in Europe and a referral hospital.

**Breed restrictions:** The Netherlands repealed its national breed-specific legislation (muzzle and leash requirements for certain breeds) in 2009. There is no national breed ban. Some housing associations and municipalities have their own rules.

---

**Sources:** European Commission EU pet travel framework; UK APHA guidance; LICG (licg.nl); Dutch Rijksdienst voor Ondernemend Nederland (RVO); TRACES NT platform.
"""},

# ─── 5. Switzerland to UK pet transport guide ──────────────────────────────────
{
"slug": "switzerland-to-uk-pet-transport-guide",
"content": """---
title: "Pet Transport from Switzerland to the UK: Health Certificates, Tapeworm Treatment and Airlines"
description: "How to move your cat or dog from Switzerland to the UK. Covers Switzerland's third-country status for UK entry, health certificate format, FOPH endorsement, tapeworm treatment timing and airline options."
date: "2025-08-24"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/switzerland-to-uk-pet-transport-guide/"
tags: ["switzerland", "uk", "route guide", "pet transport", "post-brexit"]
---

Switzerland sits outside the EU but has bilateral agreements that align it closely with EU standards in many areas -- including animal health. For UK entry purposes, Switzerland is treated as a listed (lower-risk) third country, which simplifies the process considerably compared with unlisted countries like China or India.

## Switzerland's Export Side

Switzerland is regulated by the Federal Food Safety and Veterinary Office (FSVO, in German: BVET). To export a pet from Switzerland to the UK:

1. **ISO microchip** -- must have been implanted before the rabies vaccination you are relying on
2. **Current rabies vaccination** -- within valid period
3. **Official health certificate** -- completed by a Swiss authorised veterinarian in the UK-approved format for listed third-country pets; the FSVO can provide guidance on the current required certificate format
4. **FSVO endorsement** -- the certificate is submitted to the relevant cantonal veterinary office (Kantonaler Veterinardienst) or directly to FSVO for government endorsement; the process takes 1 to 5 business days; book the appointment close to your travel date as the certificate is valid for a limited window

## UK Entry Requirements from Switzerland

Because Switzerland is a **UK-listed country**, the requirements are simpler than for unlisted countries:

- **No titre test required** for pets that meet the basic vaccination and microchip requirements
- **No mandatory quarantine** with complete documentation
- **Tapeworm treatment** (praziquantel, given by a vet) required for dogs (not cats) within **24 to 120 hours** before arrival in the UK -- this is strictly enforced; too early or too late and the dog cannot enter
- The endorsement and tapeworm records must be complete and in order at the UK port of entry

Pets arriving in the UK from Switzerland must enter through a designated Great Britain (GB) entry point that accepts pet arrivals. The main approved routes include: air arrivals at London Heathrow, London Gatwick and Manchester; Eurostar services and ferry routes if applicable. Confirm that your specific entry point is approved with APHA before travel.

## Airlines on This Route

Zurich (ZRH) is the main Swiss international hub:
- **Swiss International Air Lines (SWISS/LX)** -- Zurich to London Heathrow (LHR); hold pet transport available on some routes
- **British Airways** -- Zurich to London Heathrow; cargo pet acceptance via IAG Cargo
- **easyJet** -- Zurich to London Gatwick (LGW) and Manchester (MAN); low-cost carriers typically do not accept hold pets; confirm before booking
- **SWISS** also operates Geneva (GVA) to London routes

For hold pet transport, SWISS and British Airways are the most commonly used options on this route.

## The Tapeworm Timing Challenge

The 24-to-120-hour window for tapeworm treatment is the tightest part of the Switzerland-to-UK process. Here is the logic:

- Book your flight
- Count back 24 hours from your scheduled UK arrival time -- that is the latest your vet can give the treatment
- Count back 120 hours -- that is the earliest
- The vet appointment must fall within this window; it cannot be done the same day as the health certificate endorsement if the endorsement takes several days to come back

Plan the sequence carefully. If you are flying Zurich to London on a Saturday morning, the treatment must be given between Monday evening and Friday morning of the same week.

---

**Sources:** Swiss Federal Food Safety and Veterinary Office (BVET/FSVO); UK APHA listed third countries for pet travel; Swiss International Air Lines cargo policy; British Airways cargo pet policy.
"""},

# ─── 6. Italy to Australia pet transport guide ─────────────────────────────────
{
"slug": "italy-to-australia-pet-transport-guide",
"content": """---
title: "Pet Transport from Italy to Australia: UVAC Certificate, DAFF Permit and Quarantine"
description: "How to move your cat or dog from Italy to Australia. Covers the Italian UVAC-endorsed health certificate, Australian DAFF import permit, rabies titre test, mandatory quarantine and airline routes."
date: "2025-08-25"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/italy-to-australia-pet-transport-guide/"
tags: ["italy", "australia", "route guide", "quarantine", "pet transport"]
---

Italy is an EU member state and home to a significant expat community, including many Italians and foreigners who eventually relocate to Australia. The move with a pet is one of the more complex international relocations -- Australia's biosecurity is among the strictest in the world -- but it is well-trodden territory for specialist pet relocation agents.

## Italy's Export Requirements

Italy's animal health system is managed by the Ministry of Health (Ministero della Salute) through regional veterinary authorities called UVAC (Uffici di Sanita Animale e Frontiera, or Uffici Veterinari per gli Adempimenti Comunitari). For exporting a pet from Italy:

1. **EU pet passport** -- in place, recording microchip number, vaccination history and owner details
2. **ISO microchip** -- confirmed and recorded
3. **Rabies vaccination** -- current and within valid period; for Australia, this must be followed by a titre test
4. **FAVN rabies antibody titre test** -- conducted at an EU-approved laboratory; result must be at least 0.5 IU/ml; test must be done at least 30 days after the most recent rabies vaccination; the test result and date are the key timeline drivers for Australia
5. **Australian DAFF import permit** -- obtained before completing export preparations; this permit specifies the approved quarantine station and arrival airport
6. **Official health certificate in the Australian format** -- completed by an Italian veterinarian authorised to issue DAFF-approved certificates; endorsed by the UVAC; issued within 10 days of departure
7. **Treatments for parasites** -- specific parasite treatments required by DAFF within certain windows before departure; these are detailed in the DAFF import permit conditions

## Australia's Mandatory Quarantine

All animals entering Australia undergo a mandatory quarantine period regardless of country of origin or completeness of documentation. For pets arriving from Italy (an EU listed country for Australia), the standard quarantine period is **10 days** at the Government-run Australian Centre for Preclinical Research and Training (ACPART) in Melbourne, or the equivalent government quarantine facility.

The 10-day period is not negotiable. Costs are charged to the owner and typically run AUD 2,000 to 4,000 including care, feeding and veterinary oversight.

## Timing the Italy-to-Australia Move

The titre test is the main timeline driver:

1. Ensure rabies vaccination is current
2. Wait at least 30 days, then collect blood for titre test
3. A positive result (0.5 IU/ml+) means your 180-day clock does NOT apply for Italy-to-Australia (Australia's specific waiting requirements are different -- confirm current timelines with DAFF as requirements have changed in recent years and the waiting period after titre test for EU listed countries may differ)
4. Apply for DAFF import permit -- allow 4 to 6 weeks
5. Book the health certificate appointment with an Italian vet/UVAC close to the departure date

Typically allow **6 to 9 months** of preparation for this route from the point where you have zero prior documentation.

## Airlines on This Route

No direct Italy-to-Australia flights exist. All routings are via a hub:
- **Emirates** -- Milan (MXP) or Rome (FCO) to Dubai (DXB) to Sydney (SYD) or Melbourne (MEL); Emirates Cargo accepts pets
- **Qatar Airways** -- Rome to Doha (DOH) to Australian cities; Qatar Cargo
- **Singapore Airlines** -- Rome to Singapore (SIN) to Sydney/Melbourne/Perth; SIA Cargo
- **Etihad** -- Milan to Abu Dhabi (AUH) to Australian cities; Etihad Cargo

The choice of routing hub matters for live animal welfare; transit conditions in Dubai, Doha, Singapore and Abu Dhabi differ. A specialist agent will know which hub handles live animals most efficiently.

---

**Sources:** Australian DAFF import requirements (agriculture.gov.au); Italian Ministero della Salute UVAC offices; IATA Live Animals Regulations 50th Edition; Emirates Cargo live animals.
"""},

# ─── 7. South Korea to UK pet transport guide ──────────────────────────────────
{
"slug": "south-korea-to-uk-pet-transport-guide",
"content": """---
title: "Pet Transport from South Korea to the UK: Health Certificates, Listed Status and Airlines"
description: "How to move your cat or dog from South Korea to the UK. Covers South Korea's listed-country status for UK entry, MAFRA health certificate, tapeworm treatment for dogs and airline options."
date: "2025-08-26"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/south-korea-to-uk-pet-transport-guide/"
tags: ["south korea", "uk", "route guide", "pet transport", "korea"]
---

South Korea is home to a large expat community and many Koreans who relocate to the UK for work, study or family reasons. The good news for pet owners on this route is that South Korea is on the UK's list of countries from which pets can travel without a titre test and without mandatory quarantine -- as long as all the documentation is correctly prepared.

## South Korea's Export Requirements

The Ministry of Agriculture, Food and Rural Affairs (MAFRA) oversees live animal exports from South Korea. The Animal and Plant Quarantine Agency (APQA) -- a MAFRA agency -- issues health certificates for export.

To export a pet from South Korea:

1. **ISO microchip** -- 15-digit; must be implanted before the vaccinations you are relying on
2. **Rabies vaccination** -- current; primary vaccination at least 30 days before the health certificate is issued; booster vaccinations must be current within the manufacturer's validity period
3. **Core vaccinations** -- dogs: distemper, parvovirus, hepatitis; cats: panleukopenia, herpesvirus, calicivirus
4. **APQA health certificate** -- completed in the APQA-approved format for the UK; issued by a licensed Korean vet and endorsed by the APQA district office; the APQA endorsement typically takes 3 to 5 business days; the certificate must be issued within 10 days of your UK arrival date

## UK Entry Requirements from South Korea

South Korea is a **UK-listed country**, which means:

- **No titre test required** -- provided the rabies vaccination schedule is correctly maintained
- **No mandatory quarantine** with complete documentation
- **Tapeworm treatment for dogs** -- praziquantel treatment by a vet within 24 to 120 hours before UK arrival; strictly enforced
- **APHA-approved health certificate** -- the APQA-issued Korean health certificate must follow the UK's listed third-country format; confirm the current approved format with APHA or a UK pet relocation specialist

Pets must arrive through a designated UK entry point approved for pet arrivals. Main options for this route: Heathrow (LHR), Gatwick (LGW) or Manchester (MAN) for air arrivals.

## The Tapeworm Treatment Window

Dogs (not cats) must receive a tapeworm (Echinococcus) treatment from a vet within 24 to 120 hours before arriving in the UK. This is a fixed window with no flexibility. Calculate your schedule:

- UK arrival: Saturday at 10:00
- Latest treatment: Friday at 10:00 (24 hours before)
- Earliest treatment: Monday at 10:00 that week (120 hours before)

The vet must record the treatment in the health certificate, so the certificate appointment and the tapeworm treatment must be coordinated with the flight date.

## Airlines on This Route

Direct flights from Seoul Incheon (ICN) to London (LHR):
- **Korean Air (KE)** -- direct Seoul Incheon to London Heathrow; Korean Air accepts pets in cargo hold
- **Asiana Airlines (OZ)** -- direct Seoul to London Heathrow; cargo hold
- **British Airways (BA)** -- direct London to Seoul; cargo via IAG Cargo
- **Virgin Atlantic** -- London to Seoul; hold cargo on selected routes

Korean Air and Asiana Airlines have experience with Korea-UK pet transport and are the most commonly used carriers for this route.

---

**Sources:** MAFRA Ministry of Agriculture Korea; APQA (Animal and Plant Quarantine Agency Korea); UK APHA listed countries pet travel guidance; Korean Air live animals policy.
"""},

# ─── 8. Australia to South Africa pet transport guide ──────────────────────────
{
"slug": "australia-to-south-africa-pet-transport-guide",
"content": """---
title: "Pet Transport from Australia to South Africa: Permits, Health Certs and Quarantine"
description: "How to move your cat or dog from Australia to South Africa. Covers DAFF export certificate, DALRRD import permit, approved entry airports, quarantine requirements and airline cargo options."
date: "2025-08-27"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/australia-to-south-africa-pet-transport-guide/"
tags: ["australia", "south africa", "route guide", "pet transport", "africa"]
---

Australia to South Africa is a less common pet relocation route but it comes up regularly for Australians of South African heritage returning home, for corporate transfers and for agricultural or research professionals. The documentation from both ends requires careful coordination.

## Australia's Export Requirements

The Australian Department of Agriculture, Fisheries and Forestry (DAFF) oversees pet exports. Steps:

1. Have your pet examined by an **accredited export veterinarian** in Australia; not all vets hold DAFF export accreditation
2. The vet completes the export health certificate in the South Africa-specific format available from DAFF
3. The certificate is submitted to DAFF for online endorsement through the export certification system; allow 2 to 5 business days for endorsement
4. The endorsed certificate must be issued within 10 days of departure

Your pet will also need: ISO microchip, current rabies vaccination, and core vaccinations (distemper, parvovirus, hepatitis for dogs; panleukopenia, herpesvirus, calicivirus for cats).

## South Africa's Import Requirements

The Department of Agriculture, Land Reform and Rural Development (DALRRD) regulates live animal imports into South Africa:

1. **Import permit** from DALRRD -- apply at least 3 to 4 weeks before travel; the permit specifies the entry port and is only valid for the stated period
2. **ISO microchip**
3. **Rabies vaccination** -- current; vaccination record clearly linked to the microchip number in your vet's records
4. **DAFF-endorsed health certificate** -- accepted by DALRRD as the Australian equivalent of a government-endorsed certificate
5. **External parasite treatment** (ticks and fleas) within 7 days of travel; internal parasite treatment within 3 weeks of travel
6. **No titre test required** for Australia-to-South Africa -- this simplifies the timeline considerably

## Entry Airports in South Africa

DALRRD designates specific ports of entry for live animal arrivals. Main approved airports:
- **O.R. Tambo International, Johannesburg (JNB)** -- most routing will come through here
- **Cape Town International (CPT)**
- **King Shaka International, Durban (DUR)**

Given there are no direct Australia-to-South Africa flights, all pets will transit through a hub. Emirates via Dubai (DXB), Qatar via Doha (DOH) and Singapore Airlines via Singapore (SIN) are common routings.

## No Mandatory Quarantine

South Africa does not impose mandatory quarantine for pets from Australia with complete documentation. A DALRRD veterinary officer inspects documents and microchip on arrival at the designated port.

## Airlines and Routing

No direct Australia-South Africa route operates. Common connections:
- **Emirates** -- Sydney/Melbourne/Perth to Dubai (DXB) to Johannesburg (JNB); Emirates Cargo
- **Qatar Airways** -- Sydney/Melbourne to Doha (DOH) to JNB; Qatar Cargo
- **Singapore Airlines** -- Sydney/Melbourne/Perth to Singapore (SIN) to JNB; SIA Cargo
- **Qantas** (via partner codeshare) -- some routings possible; confirm cargo acceptance

Dubai and Doha are often used as transit hubs. South Africa's summer (December to February) and the extreme Middle East summer heat (June to August) are both temperature risk periods for cargo animals in transit.

---

**Sources:** Australian DAFF export certification; DALRRD South Africa import requirements; Emirates Cargo live animals; IATA Live Animals Regulations 50th Edition.
"""},

# ─── 9. Germany to Canada pet transport guide ──────────────────────────────────
{
"slug": "germany-to-canada-pet-transport-guide",
"content": """---
title: "Pet Transport from Germany to Canada: CFIA Requirements and Health Certificates"
description: "How to move your cat or dog from Germany to Canada. Covers CFIA import requirements, the German government-endorsed health certificate process, microchip rules and airline options on this route."
date: "2025-08-28"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/germany-to-canada-pet-transport-guide/"
tags: ["germany", "canada", "route guide", "pet transport", "north america"]
---

Germany has a large expat community, many of whom eventually move on to Canada. The Germany-to-Canada pet transport process is relatively straightforward by international standards: no titre test is required, no quarantine, and the documentation timeline is manageable.

## Canada's Import Requirements for Pets from Germany

The Canadian Food Inspection Agency (CFIA) regulates live animal imports. For dogs and cats arriving from Germany:

1. **Microchip** -- recommended and increasingly required; ISO 15-digit chip
2. **Rabies vaccination** -- current for dogs over 3 months of age; puppies under 3 months must arrive without prior vaccination and will receive it on arrival (CFIA rules apply)
3. **Distemper vaccination** -- for dogs; current and recorded
4. **Official health certificate** -- completed by a licensed veterinarian in Germany and endorsed by the competent veterinary authority (in Germany: the Veterinaramt / district veterinary office); the certificate must be in English or French; German-language certificates must be accompanied by a certified translation
5. **No import permit required** for personal companion animals (cats and dogs) arriving from Germany
6. **No titre test required** -- Canada does not require a rabies titre test for dogs and cats from European countries including Germany
7. **No quarantine** -- Canada does not impose mandatory quarantine for dogs and cats from Germany meeting the vaccination requirements

## The German Health Certificate and Endorsement

When you are in Germany preparing to export your pet:

- Your vet completes the health certificate in the CFIA-required format; ask for the CFIA-approved EU health certificate template
- Take the certificate to the **Veterinaramt** (district veterinary office) for government endorsement; this endorsement confirms the vet's credentials and signature; in major German cities this typically takes 1 to 3 business days; smaller districts may be slower
- The endorsed certificate must be issued within 10 days of your arrival in Canada

## Arriving in Canada

The main international airports that handle live animal arrivals are:
- **Toronto Pearson (YYZ)** -- Canada's busiest cargo hub
- **Vancouver International (YVR)**
- **Montreal Trudeau (YUL)**
- **Calgary (YYC)**

On arrival, a CFIA officer at the airport port of entry inspects the health certificate and checks the microchip. For a straightforward case from Germany, this is typically a brief process.

## Airlines on This Route

Direct flights from Germany to Canada:
- **Lufthansa** -- Frankfurt (FRA) and Munich (MUC) to Toronto (YYZ), Vancouver (YVR) and Montreal (YUL); Lufthansa Cargo accepts live animals on long-haul routes
- **Air Canada** -- Toronto and Vancouver to Frankfurt; cargo hold pets accepted
- **Condor** -- Frankfurt to various Canadian cities on seasonal routes; confirm cargo pet acceptance
- **Air Transat** -- seasonal leisure routes from Germany to Canada

Lufthansa is the dominant carrier on this route with the most established live animal cargo process.

## Dogs vs Cats: CFIA Specific Rules

Canada makes a distinction between dogs and cats at import:
- **Dogs**: must have current rabies and distemper vaccinations; puppies under 3 months arriving with no prior vaccination are admitted without vaccination but must receive rabies and distemper vaccines within a specified period after arrival
- **Cats**: no vaccination requirement specified in CFIA rules for domestic cats from Germany, but ensure your vet's health certificate is complete and signed

---

**Sources:** Canadian Food Inspection Agency (CFIA) importing animals; German Bundesministerium fur Ernahrung und Landwirtschaft (BMEL); Lufthansa Cargo live animals; IATA Live Animals Regulations 50th Edition.
"""},

# ─── 10. USA to New Zealand pet transport guide ────────────────────────────────
{
"slug": "usa-to-new-zealand-pet-transport-guide",
"content": """---
title: "Pet Transport from USA to New Zealand: NZSTAP Protocol, Treatments and Quarantine"
description: "How to move your cat or dog from the USA to New Zealand. Covers the NZSTAP protocol, mandatory treatment schedule, government health certificate endorsement, 10-day quarantine and airline options."
date: "2025-08-29"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/usa-to-new-zealand-pet-transport-guide/"
tags: ["usa", "new zealand", "route guide", "quarantine", "pet transport", "nzstap"]
---

New Zealand's biosecurity is among the strictest in the world. The country is rabies-free, free of many diseases endemic in the USA and Northern Hemisphere, and goes to considerable lengths to remain so. For pet owners moving from the USA, the process is detailed and unforgiving of errors, but it is manageable if you start early.

## The NZSTAP Framework

New Zealand uses a system called the **New Zealand Standard Treatment and Assessment Protocol (NZSTAP)**. This is a schedule of treatments and assessments that all cats and dogs entering New Zealand must complete before and after arrival. The full protocol can take **several months** from start to finish.

## USA-Specific Requirements

The USA is on New Zealand's approved country list, which means a titre test is **not** required. However, the treatment schedule must be completed in the correct sequence and within the correct windows.

For a dog entering New Zealand from the USA, the NZSTAP schedule includes:

1. **ISO microchip** -- must be implanted first, before any treatments in the protocol
2. **Vaccinations** -- rabies (current within valid period), distemper, hepatitis, parvovirus; all must be current at the time the health certificate is issued
3. **Brucella canis test** -- dogs over 16 weeks of age must test negative within 30 days before arrival; cats are exempt
4. **Internal parasite treatment** -- must be given within a specified window before travel (currently Milbemycin Oxime or equivalent as specified by NZSTAP); exact window and dosage detailed in the current NZSTAP document available from Biosecurity New Zealand (MPI)
5. **Tick treatment** -- specific acaricide treatment required within a window before arrival
6. **USDA APHIS-endorsed health certificate** -- completed by a USDA-accredited vet in the USA and endorsed by USDA APHIS Veterinary Services within 10 days of travel
7. **Import permit** issued by Biosecurity New Zealand (MPI)

For cats, the Brucella test is not required but the vaccination and parasite treatment requirements apply.

## 10-Day Post-Arrival Managed Isolation

All dogs and cats entering New Zealand undergo a **minimum 10-day managed isolation** period. For the USA-to-NZ route (approved country), this is typically completed at an **MPI-approved facility** before being released to the owner. Alternatively, in some cases the post-arrival component may include time in an approved home isolation under specific conditions -- check with MPI for current policy.

The cost of the 10-day facility stay is charged to the owner and currently runs approximately NZD 1,500 to 2,500.

## Airlines on This Route

No direct USA-to-New Zealand flights exist. Common routings:
- **Air New Zealand** -- Los Angeles (LAX) to Auckland (AKL) via direct or via Pacific stops; Air NZ Cargo accepts live animals
- **United Airlines** -- via Sydney (SYD) to Auckland; cargo acceptance on long-haul routes; confirm current policy
- **Qantas** -- via Sydney or Melbourne to Auckland; confirm cargo acceptance and New Zealand biosecurity compliance

Auckland International Airport (AKL) is the primary MPI-approved arrival point for pets.

## Timing

Working backward from your planned arrival date:
- Import permit application: at least 4 to 6 weeks before travel
- USDA APHIS endorsement: 10 days before travel; book the vet appointment then take the certificate to APHIS
- Brucella test: within 30 days before arrival
- Parasite treatments: within the specific windows set in NZSTAP (days before departure)

---

**Sources:** Biosecurity New Zealand / Ministry for Primary Industries (mpi.govt.nz) NZSTAP; USDA APHIS international travel; Air New Zealand cargo policy; IATA Live Animals Regulations 50th Edition.
"""},

# ─── 11. Travelling with a Shetland Sheepdog ──────────────────────────────────
{
"slug": "travelling-with-a-shetland-sheepdog-internationally",
"content": """---
title: "International Travel with a Shetland Sheepdog: Airline Rules and Documentation"
description: "A Shetland Sheepdog owner's guide to international pet travel. Covers airline cargo policies, crate sizing for Shelties, country breed restrictions and key documentation for this popular working breed."
date: "2025-08-30"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-shetland-sheepdog-internationally/"
tags: ["shetland sheepdog", "sheltie", "breed guide", "dog travel", "international pet travel"]
---

Shetland Sheepdogs -- Shelties -- are among the most loyal and trainable breeds in existence. Their expressive faces and silky coats are hard to leave behind, and most Sheltie owners don't even consider the alternative. The practical questions around air travel are worth understanding clearly.

## Cabin or Cargo?

Adult Shelties typically weigh 6 to 12 kg, with females tending toward the lighter end of the scale. For international flights, the cabin pet weight limit (combined pet plus carrier) is typically 6 to 8 kg. A small female Sheltie of 6 kg in a soft carrier of approximately 1.5 to 2 kg may come in at or just above the 8 kg limit -- it depends on the individual dog and the specific airline.

In practice, most Shelties travel in the **cargo hold** for international long-haul flights. The exceptions are smaller individuals on airlines with higher cabin weight limits (some European carriers allow 10 kg combined). Weigh your dog and carrier together before booking; do not rely on estimates.

## Crate Sizing for a Sheltie

A Sheltie typically fits comfortably in an IATA-compliant **Kennel 300** crate. Measure your individual dog: from the tip of the nose to the base of the tail (length), from the floor to the top of the ears when standing (height), and across the shoulders (width). The crate must allow standing, turning and lying in a natural position with no restriction.

## Are Shelties Subject to Any Country Restrictions?

Shelties are not listed on any national breed ban or restriction lists in the UK, EU, USA, Australia, Canada or New Zealand. Standard documentation requirements apply: microchip, vaccinations, government-endorsed health certificate, and (for applicable destinations) a titre test.

## The Sheltie Double Coat and Travel Stress

Shelties have a thick, harsh outer coat and a soft undercoat that requires regular grooming. For air travel, the coat should be:
- Clean and fully dry before travel; damp fur in a sealed crate creates skin irritation and discomfort
- Brushed out to remove any mats before the journey
- Not freshly groomed to the point of being overly fluffy; a natural coat without excessive fluffing-out fits more comfortably in the crate

## Herding Instinct and Crate Training

Shelties are intelligent and can be highly sensitive to new environments. A Sheltie that has never been in a crate and is suddenly placed in one for a 20-hour cargo journey will be significantly more stressed than one that has been positively trained to see the crate as its safe space. Begin crate training as early as possible -- ideally months before the move.

## Country-Specific Links

For your destination's import requirements:
- [UK to Australia](/blog/uk-to-australia-pet-transport-complete-guide/)
- [Moving to Germany](/blog/moving-to-germany-with-a-pet/)
- [USA to UK](/blog/uk-to-usa-pet-transport-cats-and-dogs/)
"""},

# ─── 12. Travelling with a Bullmastiff ────────────────────────────────────────
{
"slug": "travelling-with-a-bullmastiff-internationally",
"content": """---
title: "International Travel with a Bullmastiff: Airline Policies, Crate Sizing and Country Rules"
description: "Planning to move internationally with a Bullmastiff? This guide covers breed restrictions in key countries, cargo crate requirements for large breeds, brachycephalic airline rules and what to check before booking."
date: "2025-08-31"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-bullmastiff-internationally/"
tags: ["bullmastiff", "breed guide", "large dogs", "brachycephalic", "international pet travel"]
---

The Bullmastiff is a powerful, calm breed that is devoted to its family. Their size and their somewhat flattened muzzle create two distinct considerations for international travel: large-dog logistics and the brachycephalic question.

## How Large Is the Problem?

Adult Bullmastiffs typically weigh 45 to 60 kg and stand 60 to 68 cm at the shoulder. You are firmly in large-breed cargo-hold territory for any international flight. The crate will need to be in the **Kennel 500 to 700** range depending on the individual dog's size. Measure your dog carefully and add the required clearance on all sides.

Some Bullmastiffs are on the upper end of this weight range when combined with a suitable crate, which takes the total cargo weight to 80+ kg. This is manageable on wide-body aircraft but may require advance coordination with the airline to confirm acceptance and cargo compartment suitability.

## Brachycephalic Classification

The Bullmastiff has a shortened muzzle and is considered a brachycephalic breed by most airline policies. Many airlines have either:
- A specific list of brachycephalic breeds they will not accept in cargo at any time
- Temperature embargoes that effectively exclude warm-nosed breeds in summer months

Airlines that restrict Bullmastiffs in cargo include (among others) United Airlines and Delta Air Lines under their brachycephalic breed restrictions. Some European carriers classify Bullmastiffs differently. **Always call the airline directly and ask specifically about Bullmastiffs before booking** -- the published breed lists are frequently out of date and the carrier-specific policy is the one that matters.

A Bullmastiff with any history of breathing difficulties, snoring or exercise intolerance should be assessed for fitness to fly by a vet before any travel arrangements are made.

## Country Restrictions

The UK has breed-specific legislation under the Dangerous Dogs Act 1991. The Bullmastiff is **not** on the prohibited breeds list in England and Wales (the prohibited breeds are: Pit Bull Terrier, Japanese Tosa, Dogo Argentino and Fila Brasileiro). However, Bullmastiffs may be subject to assessment in some local authority jurisdictions that consider dogs to be "of type."

Germany, Italy and several other EU countries do not have national legislation targeting Bullmastiffs specifically. However, individual German states have their own lists; confirm with the relevant Bundesland (state) veterinary authority.

Australia and New Zealand do not restrict Bullmastiffs.

## Temperature Awareness

Given the brachycephalic anatomy and the large body size, heat management is critical. A Bullmastiff should not be transported:
- On routes that include ground holds longer than 45 minutes in temperatures above 24 degrees Celsius
- Through hub airports with high ambient temperatures in summer (Dubai, Doha in July/August can exceed 40 degrees in cargo areas)
- On aircraft types where the hold is not climate-controlled (some turboprop aircraft)

Plan the journey for cooler months or choose routes through temperate hubs.

---

**Sources:** IATA Live Animals Regulations 50th Edition; RSPCA guidance on brachycephalic breeds and flying; UK Dangerous Dogs Act 1991; US airline brachycephalic breed restriction policies.
"""},

# ─── 13. Travelling with a Newfoundland ───────────────────────────────────────
{
"slug": "travelling-with-a-newfoundland-internationally",
"content": """---
title: "International Travel with a Newfoundland: Giant Breed Logistics and Airline Requirements"
description: "Moving internationally with a Newfoundland dog? This guide covers crate sizing for giant breeds, which airlines accept very large dogs, health considerations for this breed and country documentation."
date: "2025-09-01"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-newfoundland-internationally/"
tags: ["newfoundland", "breed guide", "giant breeds", "dog travel", "international pet travel"]
---

Newfoundlands are among the most gentle and people-centred giant breeds. Their owners are famously devoted. When relocation comes, the size and health considerations of a Newfoundland require specific planning.

## Size and Weight

Adult Newfoundlands typically weigh 55 to 70 kg and stand 66 to 71 cm at the shoulder. This places them in the same logistical category as St Bernards and Irish Wolfhounds: combined crate weight will typically exceed 100 kg, which is outside the range of standard cargo booking processes on most airlines.

A custom-built IATA-compliant wooden crate or a very large hard-shell crate (Kennel 700 range) will be required. Measure from nose to base of tail, across the shoulders and from floor to top of the head when standing, adding the required clearances.

## Airlines: A Practical Challenge

For dogs in this weight class, the standard online cargo booking process does not apply. You need:

1. An IPATA-accredited specialist pet relocation agent who works regularly with giant breeds and has relationships with cargo carriers
2. A routing on wide-body aircraft (747, 777, A330, A350, A380) -- these have freight compartments that can accommodate oversized live animal crates
3. Pre-clearance with the cargo team at each airport of departure, transit and arrival -- not just the airline head office

Narrow-body routes (737, A320) are generally unsuitable for Newfoundlands due to cargo door dimensions.

## Coat and Climate Considerations

Newfoundlands have a dense double coat that provides significant insulation against cold and wet conditions. This is a cold-water breed: the coat is water-resistant and heavy. For travel in warm climates or in summer months, heat stress is a serious concern. A Newfoundland in a cargo hold at 25 degrees Celsius in a tropical hub is at much higher risk than the same dog passing through Iceland in February.

Route planning should factor in ambient temperatures at transit hubs and at the destination. Avoid summer travel on routes through the Middle East, Southeast Asia or any tropical region if possible.

## Health and Fitness

Newfoundlands are prone to dilated cardiomyopathy (DCM) and hip/elbow dysplasia. Before any international move, have a cardiac examination and orthopaedic check performed by your vet. Older Newfoundlands with DCM should be assessed for fitness to fly with particular care; the stress of cargo travel can exacerbate cardiac conditions.

**Sub-aortic stenosis (SAS)** is also more prevalent in Newfoundlands than in many other breeds -- another reason for a pre-travel cardiac assessment.

## Country Restrictions

Newfoundlands are not subject to breed-specific restrictions in any major destination country. Standard documentation: microchip, vaccinations, health certificate, titre test where required.

## A Note on Timing

For giant breeds with health monitoring needs, additional lead time in the planning process is advisable. Book your specialist agent as soon as relocation becomes definite; last-minute bookings for 100 kg cargo animals are difficult to accommodate and command significant premium rates.
"""},

# ─── 14. Travelling with a Bull Terrier ───────────────────────────────────────
{
"slug": "travelling-with-a-bull-terrier-internationally",
"content": """---
title: "International Travel with a Bull Terrier: Breed Restrictions, Country Rules and Airlines"
description: "A Bull Terrier owner's guide to international pet travel. Covers breed ban lists in the UK, Germany and other countries, whether the Miniature Bull Terrier is affected, crate requirements and documentation."
date: "2025-09-02"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/travelling-with-a-bull-terrier-internationally/"
tags: ["bull terrier", "breed guide", "breed restrictions", "dog travel", "international pet travel"]
---

Bull Terriers -- with their distinctive egg-shaped heads and strong builds -- are a breed that comes with genuine breed-specific restrictions in several countries. If you own a Bull Terrier (or a Miniature Bull Terrier) and are planning an international relocation, understanding which restrictions apply at your destination is the first step.

## UK Regulations

In the UK, the Dangerous Dogs Act 1991 prohibits certain breeds. The Bull Terrier **is not** on the prohibited list in England and Wales -- the four prohibited types are: Pit Bull Terrier, Japanese Tosa, Dogo Argentino and Fila Brasileiro. A standard Bull Terrier or Miniature Bull Terrier can be owned and imported legally in the UK.

## Germany

Germany's breed restrictions are administered at the state (Land) level. The Bull Terrier appears on the restricted (Kategorie 1 or 2) breed list in some German states, including **North Rhine-Westphalia** and **Schleswig-Holstein**, where it may be subject to a character assessment (Wesenstest) requirement and potential muzzle/lead requirements in public. In other states (Bavaria, Baden-Wurttemberg) the restrictions are different.

Confirm the specific rules for the German state where you will be living before importing a Bull Terrier to Germany. Some states also require mandatory liability insurance for dogs on the restricted list.

## Other European Countries

- **Denmark**: Bull Terriers are on Denmark's banned breed list. Standard Bull Terriers **cannot legally be imported to Denmark**. This is one of the strictest breed ban lists in Europe.
- **Belgium**: Some municipalities have restrictions; there is no national ban
- **Netherlands**: no national ban (legislation was repealed); no restriction on Bull Terriers
- **France**: France has a Category 2 (restricted) classification for Bull Terriers; owners must obtain a permit, have the dog sterilised and comply with specific handling rules

## Outside Europe

**Australia and New Zealand:** No breed-specific restriction on Bull Terriers. Standard import protocol applies.

**USA and Canada:** No federal breed ban. Some municipalities and homeowner associations (HOAs) or landlords have Bull Terrier restrictions. This is a local/private issue rather than a national one.

## Cabin or Cargo?

Adult Bull Terriers weigh 22 to 38 kg. They travel in the **cargo hold** for international flights. A Kennel 300 to 400 crate typically fits standard Bull Terriers; measure your individual dog. Bull Terriers are not classified as brachycephalic on most airline lists (their muzzle is not short enough to trigger snub-nosed restrictions on most carriers), but always confirm with the airline.

Miniature Bull Terriers (11 to 15 kg) also travel in cargo for most international routes, though a small Miniature Bull Terrier may qualify for cabin travel on routes with a 10 kg combined weight limit on some European carriers.

## Documentation

Standard requirements apply: ISO microchip, vaccinations, government-endorsed health certificate, titre test where the destination requires it.

---

**Sources:** UK Dangerous Dogs Act 1991; Denmark Animal Welfare Act breed ban list; French Code Rural pet classification (Category 2); German Bundesland breed restriction lists.
"""},

# ─── 15. Pet-friendly airlines ranked ─────────────────────────────────────────
{
"slug": "pet-friendly-airlines-ranked-2026",
"content": """---
title: "Most Pet-Friendly Airlines in 2026: How the Major Carriers Compare"
description: "How do the world's major airlines compare for travelling with a cat or dog? This guide ranks and compares pet policies across cabin acceptance, hold conditions, brachycephalic restrictions and costs."
date: "2025-09-03"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/pet-friendly-airlines-ranked-2026/"
tags: ["airline comparison", "pet-friendly airlines", "airline pet policy", "practical guide"]
---

Choosing the right airline for your pet is as important as choosing the right route. Policies vary enormously in how airlines handle cabin pets, whether they accept large dogs in cargo, how they treat brachycephalic breeds and what the conditions are like in hold for a 12-hour flight. This guide compares the major carriers on the dimensions that matter most to pet owners.

## Cabin Pet Acceptance: Who Comes Out on Top?

Cabin travel is only relevant for small pets -- typically under 6 to 8 kg combined -- but for small dog and cat owners, which airline accepts cabin pets most flexibly matters.

**Better cabin policies:**
- **Lufthansa**: accepts pets in cabin within Europe and on some long-haul routes; combined weight up to 8 kg; additional fee applies; advance booking required
- **SWISS (LX)**: cabin pets on European routes, combined under 8 kg; consistent application
- **Air France**: cabin pets on most routes including some transatlantic; combined 8 kg; consistent
- **KLM**: cabin pets on European and some intercontinental routes; 8 kg combined
- **TAP Air Portugal**: cabin pets on European routes; good consistency; also accepts pets as checked baggage
- **Turkish Airlines**: cabin pets on most routes; one of the more flexible major carriers for cabin pet acceptance on long-haul routes; up to 8 kg combined

**More restrictive cabin policies:**
- **United Airlines**: cabin pets accepted on domestic US routes and some international routes, but not all; explicitly bans several routes due to USDA restrictions for certain destinations
- **Delta Air Lines**: cabin pets on domestic US routes; some international routes excluded
- **British Airways**: no pets in cabin on any route; pets only as hold cargo via PetAir UK
- **Ryanair**, **easyJet**: no cabin or hold pets accepted on any route

## Cargo Hold Conditions: What Separates Good from Poor

**Consistently strong cargo pet reputations:**
- **Qatar Airways** (Doha DOH): operates a dedicated live animal cargo terminal; strict temperature control; well-regarded by IPATA agents globally
- **Lufthansa Cargo** (Frankfurt FRA): established live animal programme; Frankfurt hub well-equipped; clear processes
- **Singapore Airlines Cargo** (Singapore SIN): modern hub, temperature-controlled live animal facilities; good track record
- **Emirates SkyCargo** (Dubai DXB): large operation, SkyCargo terminal has live animal facilities; hub is a major global transit point; summer heat management is important but the terminal conditions are controlled

**Notable restrictions:**
- **Delta Air Lines**: extensive brachycephalic breed ban list; no pets in hold on many international routes; among the most restrictive US carriers for cargo hold pets
- **United Airlines**: PetSafe programme for hold pets; but brachycephalic restrictions apply; various route-level restrictions
- **American Airlines**: suspended hold pet transport on international routes; currently does not accept pets in hold on flights outside the USA

## Brachycephalic Breed Handling

The handling of flat-faced breeds is one of the most significant differentiators between airlines. Some carriers ban all snub-nosed dogs from hold cargo; others accept them with conditions; others accept them without distinction.

**Most restrictive on brachycephalic breeds:**
- Delta Air Lines
- United Airlines (PetSafe programme has a breed restriction list)
- Many European budget carriers

**More accommodating (with appropriate conditions):**
- Qatar Airways has its own vet assessment process
- Lufthansa considers cases individually for some restricted breeds

This information changes frequently. Always confirm current policy with the airline for your specific breed before booking.

## Cost Comparison (Approximate 2026 Ranges)

| Category | Range |
|----------|-------|
| Cabin pet fee (one way, international) | USD 50 to 200 |
| Hold cargo (small-medium dog, under 25 kg, one way, transatlantic) | USD 400 to 900 |
| Hold cargo (large dog, 25 to 50 kg, one way, transatlantic) | USD 700 to 1,500 |
| IPATA agent fee (door to door, full service) | USD 1,500 to 4,000 |

These are indicative ranges only. Actual costs vary by carrier, route, season and individual dog size.

## Summary

No single airline is the best for every pet on every route. The best choice depends on: your pet's size and breed, your specific origin and destination, whether you need cabin or cargo, and what time of year you are travelling. Research the specific carrier and route rather than relying on general rankings.

---

**Sources:** Airline pet policy pages (current at time of writing; subject to change); IPATA member agent feedback; IATA Live Animals Regulations 50th Edition; RSPCA air travel guidance.
"""},

# ─── 16. Stopover with a pet guide ────────────────────────────────────────────
{
"slug": "stopover-layover-with-a-pet-guide",
"content": """---
title: "Stopover and Layover with a Pet: What Happens to Your Animal at Transit Hubs"
description: "A practical guide to what happens to your pet during a connecting flight or stopover. Covers transit conditions at major hubs, live animal handling, temperature risks, connection timing and what to ask your airline."
date: "2025-09-04"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/stopover-layover-with-a-pet-guide/"
tags: ["transit", "layover", "stopover", "pet cargo", "practical guide", "airline hubs"]
---

Most international pet relocations involve at least one transit -- a connection through a hub airport before the final destination. What happens to your pet during that connection is one of the questions owners ask most often, and it is one that deserves a clear answer.

## What Happens to a Pet in the Cargo Hold During a Transit?

When your pet travels as cargo hold freight:

**On the aircraft:** The pet remains in the cargo hold for the full flight. On wide-body aircraft the hold is pressurised and temperature-controlled to a range that typically stays between 7 and 24 degrees Celsius (45 to 75 degrees Fahrenheit), though the specific range varies by aircraft type and airline.

**At the transit hub:** On landing, the cargo off-loading process begins. Your pet's crate is removed from the hold and placed in a staging area. At a well-equipped hub (Frankfurt, Singapore, Doha, Dubai, Amsterdam, London Heathrow), there is a dedicated live animal cargo facility where the temperature is managed and the animal can be checked by the cargo staff.

The pet is then held in this facility until the connecting flight is ready. It is loaded back into the hold of the next aircraft before departure.

## How Long Can a Transit Take?

IATA Live Animals Regulations (LAR) specify maximum journey time limits including transits. For most dogs and cats, the combined air journey and transit time should not exceed 24 hours from first check-in to final arrival, under normal conditions.

Many hubs have transit connection times of 2 to 6 hours for cargo pets. A connection of less than 2 hours is considered tight for cargo transfer and can result in your pet missing the connection (known as an off-load). A connection of more than 12 hours at a hub may trigger additional care or feeding requirements.

## Best Transit Hubs for Pet Cargo

**Well-equipped, with dedicated live animal facilities:**
- **Frankfurt (FRA)**: Lufthansa Cargo's Animal Lounge is purpose-built; one of the best facilities in Europe; temperature-controlled; 24-hour staffing
- **Amsterdam (AMS)**: Amsterdam Schiphol has strong live animal handling infrastructure
- **Singapore (SIN)**: Changi Airport has modern live animal facilities; SIA Cargo invests heavily in animal welfare
- **Doha (DOH)**: Qatar Airways' hub has a dedicated animal care station within the cargo complex
- **Dubai (DXB)**: Emirates SkyCargo operates a large live animal facility; summer temperatures outside the facility are extreme but inside conditions are controlled

**Hubs where conditions are more variable:**
- Hub airports with limited dedicated live animal infrastructure may hold cargo animals in general temperature-controlled areas; conditions are adequate but not purpose-built
- Any transit hub in a hot climate during summer months requires that the connection is during cooler hours and the on-ground time is minimised

## The Summer Temperature Risk

For a connection through Dubai, Doha, Abu Dhabi or any tropical hub in July and August, the ambient temperature on the tarmac can exceed 45 degrees Celsius. The time between the aircraft door opening and the cargo reaching the temperature-controlled facility matters. Most cargo handlers move live animals as a priority, but delays happen.

**Request confirmation from your airline that your pet will be treated as a priority live cargo item during ground handling** and that the transit hub's live animal facility will be used.

## Questions to Ask Your Airline

1. What live animal facility is used at the transit hub?
2. What is the minimum and maximum recommended connection time for live cargo animals?
3. Will my pet be able to receive water during a transit of more than 6 hours?
4. At what temperatures will you refuse to handle my pet on the tarmac?
5. What happens if my pet misses its connection?

## Cabin Transit: Different Rules

For small pets in the cabin, the transit is simpler -- you and your pet travel together through the connection. However, some transit airports have rules about animals leaving and re-entering the terminal. Confirm whether your pet is permitted to remain in the cabin for a connection on the same booking or whether you need to recollect from cargo and re-check in.

---

**Sources:** IATA Live Animals Regulations 50th Edition; Frankfurt Animal Lounge (Lufthansa Cargo); Qatar Airways live animals cargo guide; Singapore Airlines Cargo live animals; Emirates SkyCargo live animals.
"""},

# ─── 17. Moving to Italy with a pet ───────────────────────────────────────────
{
"slug": "moving-to-italy-with-a-pet",
"content": """---
title: "Moving to Italy with a Pet: EU Rules, Microchip Registration and Life in Italy"
description: "A complete guide to relocating to Italy with a cat or dog. Covers EU pet passport rules, third-country requirements for UK and US pets, Italian microchip database registration and life with a pet in Italy."
date: "2025-09-05"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-italy-with-a-pet/"
tags: ["italy", "expat guide", "pet relocation", "europe"]
---

Italy has been attracting expats for centuries, and in recent years the Italian government's flat-tax and digital nomad visa schemes have accelerated the trend. For those arriving with a cat or dog, Italy's approach to pets -- particularly in the south and rural areas -- can differ quite noticeably from the northern European approach, but the country is broadly manageable.

## Importing Your Pet to Italy

**From EU countries:**
EU pet passport, ISO microchip, current rabies vaccination. No additional paperwork, no import permit, no titre test. Italy is fully subject to EU Regulation 576/2013 for intra-EU companion animal movement.

**From the UK (post-Brexit):**
UK pets entering Italy follow EU third-country import rules: ISO microchip, rabies vaccination, FAVN titre test (0.5 IU/ml or above; at least 30 days after vaccination), 3-month wait after a positive titre result, AHC completed by a UK Official Veterinarian within 10 days of arrival, TRACES NT pre-notification at an Italian Border Inspection Post. Main BIPs for air arrivals: Rome Fiumicino (FCO) and Milan Malpensa (MXP).

**From the USA, Canada, Australia and other non-EU countries:**
Third-country protocol applies: microchip, vaccination, titre test, 3-month wait, USDA/CFIA/DAFF-endorsed health certificate, TRACES NT at an Italian BIP. Rome and Milan are the primary entry points.

## Registering Your Pet in Italy

Italy uses the **AnagrafeAnimali d'Affezione** national database for microchip registration. All dogs, cats and ferrets must be registered. Registration is done by a licensed veterinarian. If your pet has a foreign microchip number, it can be transferred into the Italian national database by an Italian vet.

**Dogs:** Dogs in Italy must be microchipped, registered on the national database, licensed with the local municipality (ASL -- Azienda Sanitaria Locale) and vaccinated against rabies. An annual fee may apply in some municipalities.

**Cats:** Registration is strongly recommended but not universally mandatory for indoor cats. Many Italian municipalities require registration for any cat that has outdoor access.

## Dangerous Breeds in Italy

Italy repealed its national breed ban list in 2009. There is no longer a national list of prohibited or restricted breeds in Italy. However, some regions and municipalities have retained local restrictions; confirm local rules at your specific address.

## Life with a Pet in Italy

Italy's attitude to pets in urban spaces has improved considerably in the past decade. Most Italian cities have designated off-lead areas (aree per cani or dog parks). Dogs are generally welcome in outdoor restaurant spaces. Access rules on public transport vary by city and region -- in Rome, small pets in carriers are allowed on the metro; larger dogs on leads are allowed on buses.

Veterinary care in northern Italy (Milan, Turin, Bologna) is excellent and generally accessible. In the deep south and rural areas, specialist veterinary care is more limited. The summer heat in southern Italy (Sicily, Calabria, Puglia) regularly exceeds 35 to 40 degrees Celsius, which requires care for brachycephalic breeds and double-coated northern breeds.

---

**Sources:** EU Regulation 576/2013; UK APHA guidance; AnagrafeAnimali d'Affezione Italy; Ministero della Salute Italy; TRACES NT platform.
"""},

# ─── 18. Switzerland pet import guide ─────────────────────────────────────────
{
"slug": "switzerland-pet-import-guide",
"content": """---
title: "Importing a Pet to Switzerland: EU Passport Rules, Third-Country Requirements and FSVO"
description: "How to import a cat or dog to Switzerland. Covers Switzerland's alignment with EU pet travel rules, third-country requirements for UK and US pets, FSVO permit process and approved entry points."
date: "2025-09-06"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/switzerland-pet-import-guide/"
tags: ["switzerland", "zurich", "country guide", "pet import", "europe"]
---

Switzerland is not an EU member state, but it participates in many EU frameworks through bilateral agreements -- and its pet import rules are very closely aligned with EU standards. The Federal Food Safety and Veterinary Office (FSVO, in German: BLV/BVET) manages live animal imports.

## Importing a Pet to Switzerland from an EU Country

Switzerland has a bilateral agreement with the EU that essentially mirrors EU pet travel rules for companion animals. For pets arriving from EU member states:

- **EU pet passport** is accepted
- **ISO microchip** required
- **Current rabies vaccination** required
- No titre test, no import permit, no quarantine

The process is comparable to intra-EU travel. The EU pet passport is fully recognised at Swiss entry points.

## Importing a Pet to Switzerland from the UK (Post-Brexit)

The UK is now a third country relative to the EU framework Switzerland uses. For UK-origin pets:

- **ISO microchip**
- **Current rabies vaccination** (administered after the microchip)
- **FAVN titre test** at an EU/FSVO-approved laboratory; result at least 0.5 IU/ml; test at least 30 days after vaccination
- **3-month wait** after a positive titre result before entry into Switzerland
- **Official health certificate** in the format required by the FSVO; completed by a UK Official Veterinarian and endorsed by APHA
- Pre-notification at the Swiss entry point is required; contact the FSVO or an authorised agent for the current pre-notification procedure

## Importing a Pet to Switzerland from the USA, Canada or Australia

Third-country rules apply:
- ISO microchip, rabies vaccination, titre test (3-month wait), USDA/CFIA/DAFF-endorsed health certificate
- Apply to FSVO for confirmation of current requirements and whether an import permit is required for your specific country of origin

Switzerland's approach for non-EU third countries mirrors the EU's; there is generally no specific Swiss import permit for companion animals from recognised countries, but health documentation must meet the FSVO standard.

## Entry Points

Switzerland has no sea borders. International pet arrivals come by air through:
- **Zurich Kloten Airport (ZRH)** -- primary international gateway
- **Geneva Cointrin Airport (GVA)** -- second major international airport
- Land border crossings from France, Germany, Italy and Austria -- animals arriving overland from EU countries with a valid EU passport do not require formal inspection at the Swiss land border; non-EU animals arriving overland are inspected at the designated Swiss border veterinary inspection post

## Living in Switzerland with a Pet

Switzerland has excellent veterinary infrastructure. Zurich, Geneva, Basel and Berne all have high-quality veterinary practices and 24-hour emergency clinics.

Dog registration and taxation vary by canton. Most Swiss cantons require dog owners to register with the cantonal authority and pay an annual dog tax. Microchip registration on the ANIS database (Schweizerische Heimtierdatenbank) is mandatory for dogs and cats in Switzerland.

---

**Sources:** Swiss Federal Food Safety and Veterinary Office (blv.admin.ch); EU-Switzerland bilateral animal health agreements; ANIS microchip database Switzerland; FSVO import requirements.
"""},

# ─── 19. Moving to France with a pet ──────────────────────────────────────────
{
"slug": "moving-to-france-with-a-pet",
"content": """---
title: "Moving to France with a Pet: EU Passport Rules, Third-Country Requirements and Registration"
description: "A complete guide to relocating to France with a cat or dog. Covers EU pet passport rules, post-Brexit requirements for UK pets, US third-country rules, ICAD microchip registration and life in France."
date: "2025-09-07"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-france-with-a-pet/"
tags: ["france", "expat guide", "paris", "pet relocation", "europe"]
---

France has one of the largest expat communities in the EU, drawing people from the UK, USA, Germany and beyond. For pet owners, France's urban culture -- particularly Paris -- is mixed: Parisians are culturally dog-positive but certain formal rules around registration, vaccination and breed restrictions apply.

## Importing Your Pet to France

**From EU countries:**
EU pet passport, ISO microchip, current rabies vaccination. Standard intra-EU movement rules under EU Regulation 576/2013. No titre test, no import permit, no quarantine.

**From the UK (post-Brexit):**
EU third-country rules apply: ISO microchip, rabies vaccination, FAVN titre test (0.5 IU/ml or above), 3-month wait after a positive titre result, AHC completed by a UK Official Veterinarian within 10 days of arrival, TRACES NT pre-notification. Main French BIPs for air arrivals include Paris Charles de Gaulle (CDG), Lyon Saint-Exupery (LYS) and Bordeaux-Merignac (BOD). CDG handles the bulk of international pet arrivals.

For the Eurotunnel (Le Shuttle) or ferry routes from the UK to France: the same documentation requirements apply. P&O Ferries, Brittany Ferries and DFDS operate pet-friendly cabin services between UK and French ports; check individual ferry company pet booking policies.

**From the USA, Canada and other non-EU countries:**
Third-country protocol: microchip, vaccination, titre test, 3-month wait, government-endorsed health certificate, TRACES NT notification.

## French Breed Restrictions (Races Canines Dangereuses)

France classifies certain dog breeds into two categories:

**Category 1 (banned from import and breeding):** Pit Bull-type dogs (American Pit Bull Terrier type without LOOF pedigree), Tosa Inu, American Staffordshire Terrier (without pedigree), Mastiff-type dogs similar to Boerboel. Category 1 dogs cannot legally be imported to France.

**Category 2 (restricted, may be owned with conditions):** Rottweiler, American Staffordshire Terrier (with LOOF pedigree), Tosa Inu (with pedigree), and certain other breeds. Category 2 owners must: obtain a permit (attestation d'aptitude), have the dog tattooed or microchipped, sterilise the dog, carry third-party liability insurance.

If your dog is a Rottweiler, a Staffordshire Bull Terrier type, or a breed that might be assessed as falling into these categories, confirm your dog's legal classification in France with the Direction Departementale de la Protection des Populations (DDPP) before importing.

## Microchip Registration in France

France uses the **ICAD** (Identification des Carnivores Domestiques) national database. All dogs are legally required to be identified (microchip or tattoo) and registered with ICAD. Cats are strongly recommended to register. Your French vet registers the chip with ICAD when you present.

## Rabies Vaccination in France

Rabies vaccination is mandatory for dogs in France. The first vaccination creates a titre; the first booster is given one year later; subsequent boosters follow the manufacturer's recommended schedule (typically every 3 years for modern vaccines). Keep the vaccination card updated.

## Life with a Pet in Paris and France

Paris has a famous (and somewhat exaggerated) reputation for dogs in restaurants. In reality, well-behaved dogs on leads are tolerated at many Parisian cafe terraces. Dogs are not permitted in most food shops, indoor public spaces or on the Paris Metro (except in a carrier under 6 kg). Jardins (formal gardens like the Jardin du Luxembourg and Tuileries) generally prohibit dogs; bois (woodlands like Bois de Boulogne and Bois de Vincennes) are more accessible.

Veterinary care in Paris and major French cities is of high quality. Emergency clinics (cliniques veterinaires d'urgences) operate in Paris and regional capitals.

---

**Sources:** French Direction Generale de l'Alimentation (DGAL); EU third-country pet travel rules; ICAD France (icad-animal.com); French Code Rural breed category legislation; UK APHA guidance.
"""},

# ─── 20. Moving to Sweden with a pet ──────────────────────────────────────────
{
"slug": "moving-to-sweden-with-a-pet",
"content": """---
title: "Moving to Sweden with a Pet: EU Passport, Third-Country Rules and Swedish Registration"
description: "A practical guide to relocating to Sweden with a cat or dog. Covers EU pet passport rules, requirements for UK and non-EU pets, Swedish Board of Agriculture (Jordbruksverket) rules and life in Stockholm."
date: "2025-09-08"
author: "PetTransport Global Editorial Team"
type: "blog"
url: "/blog/moving-to-sweden-with-a-pet/"
tags: ["sweden", "stockholm", "expat guide", "pet relocation", "scandinavia", "europe"]
---

Sweden is a consistently high-quality expat destination: clean, well-organised, with excellent public services and a strong culture of outdoor activity that suits dogs particularly well. The pet import rules are broadly EU-aligned, though Sweden has some additional biosecurity requirements of its own.

## Importing Your Pet to Sweden

**From EU countries:**
EU pet passport, ISO microchip, current rabies vaccination. Standard intra-EU movement. Sweden applies EU Regulation 576/2013. No titre test, no import permit.

**From the UK (post-Brexit):**
UK pets are third-country animals: ISO microchip, rabies vaccination, FAVN titre test (0.5 IU/ml), 3-month wait after passing titre, AHC completed by a UK OV within 10 days of arrival, TRACES NT pre-notification at a Swedish BIP. Stockholm Arlanda Airport (ARN) is the main Swedish BIP for international pet arrivals.

**From the USA, Canada and other non-EU countries:**
Third-country protocol applies: microchip, vaccination, titre test, 3-month wait, government-endorsed health certificate, TRACES NT at ARN.

## Sweden's Additional Requirements: Echinococcus Treatment

Sweden, along with Finland, has a special status within the EU regarding Echinococcus (tapeworm). Dogs (not cats) entering Sweden from any country **including other EU countries** must receive a treatment for Echinococcus multilocularis (praziquantel) within **1 to 5 days** (24 to 120 hours) before entering Sweden.

This applies even for intra-EU travel. A dog moving from Germany to Sweden with an EU pet passport still needs the tapeworm treatment within this window.

The vet who administers the treatment records it in the EU pet passport or on the health certificate. Failure to have this treatment in the correct window results in the animal being refused entry or held.

## Microchip Registration in Sweden

Sweden uses the **SKK** (Svenska Kennelklubben) and Agria/Jordbruksverket databases for pet registration. Your Swedish vet registers the chip when you present. There is no formal mandatory registration process separate from your vet records for most companion animals, but registration with the dog registration system is strongly recommended for reunification purposes.

## No Breed Restrictions

Sweden has no national breed ban. No breed is prohibited from import on the basis of type alone. Sweden's approach to dangerous dogs focuses on individual dog behaviour rather than breed-based prohibitions.

## Animal Welfare Standards

Sweden has among the highest animal welfare standards in the world. The Animal Welfare Act (Djurskyddslagen) sets requirements for housing, exercise, social interaction and veterinary care that exceed many other countries' requirements. Dogs must have daily outdoor exercise, social interaction and appropriate mental stimulation. Leaving a dog alone for extended periods without meeting these requirements is a welfare offence.

## Life in Sweden with a Pet

Stockholm is highly dog-friendly. Many restaurants and cafes allow dogs on outdoor terraces. Public parks (Djurgarden, Hagaparken) are popular dog walking destinations. Off-lead areas are available in many parks.

The Swedish climate suits cold-weather and double-coated breeds very well. Winters in Stockholm are cold (regularly below -10 degrees Celsius) with good snow cover. Summers are mild and pleasant. For cold-sensitive, short-coated breeds, a dog coat is needed from October to April.

---

**Sources:** Swedish Board of Agriculture (Jordbruksverket); European Commission EU pet travel (Regulation 576/2013); UK APHA guidance; Swedish Animal Welfare Act (Djurskyddslagen 2018:1192).
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
