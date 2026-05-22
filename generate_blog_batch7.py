"""
Phase 6 Task 6.3 — Blog batch 7 (25 articles, total target: 150)
Covers: France/Ireland/Netherlands/Switzerland/Austria/Nordic/LatAm/Africa/India/China
country import guides; UK-Germany/Canada/Singapore/Japan/France route guides;
AU-USA; breed guides (Golden Retriever, French Bulldog); practical guides.
Skip-if-exists on all files.
"""
import os

BLOG_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    # ── Country import guides ──────────────────────────────────────────────
    {
        "slug": "france-pet-import-guide",
        "title": "Moving to France with a Pet: Import Rules and What You Need in 2026",
        "description": "Complete guide to bringing your dog or cat to France in 2026: EU pet passport rules, microchip requirements, rabies vaccination, and what non-EU arrivals need.",
        "date": "2026-04-28",
        "tags": ["France", "EU pet travel", "pet import"],
        "faqs": [
            ("Do I need a special permit to bring my dog to France?", "No import permit is required for dogs and cats entering France from EU countries with a valid EU pet passport. Non-EU arrivals need an Animal Health Certificate (AHC) in the EU format, and the animal must enter through an approved border inspection post (BIP)."),
            ("Does my pet need a rabies titre test to enter France?", "Pets from EU countries do not need a titre test. Pets from non-listed third countries (outside the approved list in EU Regulation 577/2013) need a valid rabies antibody titre test result showing at least 0.5 IU/ml, carried out at least 30 days after rabies vaccination and at least 3 months before travel."),
            ("Can I bring my dog to France from the UK post-Brexit?", "Yes. UK pets travelling to France need an AHC issued by an authorised UK vet and endorsed by the APHA. Dogs must also have tapeworm treatment (praziquantel) administered 1-5 days before arrival. The AHC is valid for 10 days from the vet examination date."),
            ("What microchip does France require?", "France requires ISO 11784/11785 compliant microchips (15-digit). The microchip must be implanted before or on the same date as the rabies vaccination for the vaccination to be counted as valid."),
        ],
        "body": """France is one of the most pet-friendly countries in the world for living with animals, but getting your pet there requires the right paperwork. The rules depend entirely on where you're coming from.

**Arriving from EU countries**

If your pet has a valid EU pet passport showing current microchip and rabies vaccination records, entry into France is straightforward. No import permit, no titre test, no additional endorsement needed. Present the passport at entry.

**Arriving from the UK**

Post-Brexit, UK pets travel as non-EU animals. You need an Animal Health Certificate (AHC) issued by an Official Veterinarian (OV) in the UK and endorsed by the Animal and Plant Health Agency (APHA). Dogs additionally need a tapeworm treatment (praziquantel, 50-150mg per kg body weight) administered by a vet 1-5 days before arrival in France. The AHC is valid for 10 days from the date of the vet examination, so timing matters.

Dogs travelling from the UK for the first time without a previous EU pet passport will also need a rabies antibody titre test if they have not previously been vaccinated before the microchip was implanted.

**Arriving from other non-EU countries**

Pets from countries on the EU's approved list (which includes the USA, Canada, Australia, and others) need an AHC in the EU format, plus microchip and rabies vaccination. Pets from non-listed countries additionally need a valid titre test result.

All non-EU arrivals must enter through an EU border inspection post (BIP) that handles live animals. Check approved entry points with French customs (DGAL) before booking travel.

**Rabies vaccination**

France requires current rabies vaccination for all arriving pets. The vaccine must be administered after the microchip is implanted to be valid. First-time vaccination requires a 21-day waiting period before the pet can travel into the EU.

**Tapeworm treatment**

Only dogs are affected. Cats are exempt from the tapeworm requirement. Treatment must be carried out by a vet 1-5 days (24-120 hours) before arrival in France.

**Practical note**

France does not operate a quarantine system for pets arriving with complete, correct documentation. Get the paperwork right and your pet steps off the plane or ferry and comes straight home with you.""",
    },
    {
        "slug": "ireland-pet-import-guide",
        "title": "Bringing a Pet to Ireland: Import Rules, Titre Tests and What to Prepare",
        "description": "Guide to bringing your dog or cat to Ireland in 2026: EU pet passport rules, UK arrivals, titre test requirements for non-EU pets, and tapeworm treatment for dogs.",
        "date": "2026-04-29",
        "tags": ["Ireland", "EU pet travel", "pet import"],
        "faqs": [
            ("Does my pet need a titre test to enter Ireland?", "Pets arriving from EU countries with valid EU pet passports do not need a titre test. Pets from non-EU countries that are not on the EU's approved list require a rabies antibody titre test showing at least 0.5 IU/ml, taken at least 30 days after rabies vaccination and at least 3 months before travel."),
            ("Can I bring my dog from the UK to Ireland?", "Yes. UK pets need an Animal Health Certificate (AHC) issued by an authorised UK vet and endorsed by APHA. Dogs must also have tapeworm treatment 1-5 days before arrival. The AHC is valid for 10 days from issue."),
            ("Is Ireland an EU member for pet travel purposes?", "Yes. Ireland is an EU member state and follows EU pet travel rules under Regulation (EU) 576/2013. EU pet passports issued in Ireland are valid throughout the EU."),
            ("Do I need to book a specific entry point for my pet?", "Non-EU arrivals must enter through an EU-approved border inspection post (BIP). The main approved BIP for pets entering Ireland is Dublin Port and Dublin Airport. Confirm your entry point with the Department of Agriculture, Food and the Marine (DAFM) before travel."),
        ],
        "body": """Ireland is an EU member with full EU pet travel rules in place. It also sits on an island, so all pet arrivals come by air or sea - there's no land crossing, which affects which entry points are approved.

**From EU countries**

An EU pet passport with valid microchip and current rabies vaccination is all you need. Entry at Dublin or other approved BIPs.

**From the UK**

UK pets need an AHC issued by a UK OV and endorsed by APHA. Dogs must have tapeworm treatment 1-5 days before arrival. The AHC must be issued within 10 days of travel. UK pets that previously had EU pet passports (issued before Brexit came into effect) may still use those passports if they remain valid.

**From Australia, USA, Canada, and other approved countries**

Pets from countries on the EU's approved list enter with an AHC in the EU format. Microchip and current rabies vaccination required. No titre test needed if from an approved country.

**From all other countries**

A rabies antibody titre test is required showing at least 0.5 IU/ml, conducted at an EU-approved laboratory, at least 30 days after the most recent rabies vaccination, and the pet must wait at least 3 months after the titre test before travelling.

**Entry points**

All non-EU arrivals must use an approved border inspection post. Dublin Airport and Dublin Port are the primary approved BIPs for pets entering Ireland. Arriving via a UK port and then taking a ferry from the UK mainland to Ireland is possible, but the UK-Ireland land/sea crossing documentation requirements add complexity. Contact DAFM (Department of Agriculture, Food and the Marine) for current approved entry routes.

**Tapeworm for dogs**

Dogs arriving in Ireland from non-EU countries must have tapeworm treatment (praziquantel) administered by a vet 1-5 days before arrival. This applies regardless of whether the UK or another non-EU country is the point of departure.""",
    },
    {
        "slug": "netherlands-pet-import-guide",
        "title": "Bringing a Pet to the Netherlands: EU Rules and What Non-EU Arrivals Need",
        "description": "Complete guide to bringing your dog or cat to the Netherlands in 2026: EU pet passport, AHC requirements for UK arrivals, breed bans, and Dutch import rules.",
        "date": "2026-04-30",
        "tags": ["Netherlands", "EU pet travel", "pet import"],
        "faqs": [
            ("What does my pet need to enter the Netherlands from the UK?", "UK pets need an Animal Health Certificate (AHC) issued by a UK Official Veterinarian and endorsed by APHA. Dogs must have tapeworm treatment 1-5 days before arrival. The AHC is valid for 10 days from the vet examination date."),
            ("Does the Netherlands ban any dog breeds?", "Yes. The Netherlands has a national dog bite incident monitoring system and local municipalities may have restrictions. At the national level, breed-specific legislation was largely lifted in 2009, but some municipalities retain byelaws. American Pit Bull Terriers still face restrictions in many areas. Always check local municipal rules before relocating with a listed breed."),
            ("Does my cat need a titre test to enter the Netherlands?", "Cats from EU countries with a valid EU pet passport do not need a titre test. Cats from non-EU countries outside the approved list need a titre test showing at least 0.5 IU/ml, taken at least 30 days after rabies vaccination and at least 3 months before travel."),
            ("Where can my pet enter the Netherlands?", "Non-EU pets must arrive via an EU-approved border inspection post (BIP). Amsterdam Schiphol Airport and Rotterdam port are the primary approved BIPs for live animals entering the Netherlands. Confirm current approved points with the Netherlands Food and Consumer Product Safety Authority (NVWA)."),
        ],
        "body": """The Netherlands is an EU member state, so the framework for pet travel is the same as France, Germany, Spain, and other EU countries. What differs is the Dutch specifics: local breed restrictions, approved entry points, and how the NVWA handles inspections.

**From EU countries**

A valid EU pet passport with microchip and current rabies vaccination is all you need. Entry is smooth at Schiphol and other approved points.

**From the UK**

Post-Brexit, UK pets are non-EU animals. An AHC is required, issued by a UK OV and endorsed by APHA. Dogs must have tapeworm treatment (praziquantel) administered 1-5 days before arrival. The AHC is valid 10 days from the vet examination date. Pets must arrive at an approved BIP - Schiphol Airport is the main option for air arrivals.

**Breed restrictions**

The Netherlands lifted national breed-specific legislation in 2009, but individual municipalities retain the right to impose their own rules. Amsterdam, Rotterdam, and other cities may have byelaws affecting specific breeds. The NVWA website and local municipality websites are the places to check for current restrictions. American Pit Bull Terriers and related types are the most commonly affected.

**From other non-EU countries**

Pets from EU-approved listed countries (USA, Canada, Australia, etc.) need an AHC plus microchip and current rabies vaccination. Pets from non-listed countries need a titre test in addition.

**NVWA inspection**

The Netherlands Food and Consumer Product Safety Authority (NVWA) handles border inspections at approved BIPs. Pre-notification may be required for commercial pet movements. For most household pet relocations, notification is not required, but confirm with the BIP before travel.""",
    },
    {
        "slug": "switzerland-pet-import-guide",
        "title": "Bringing a Pet to Switzerland: What Non-EU Arrivals Need to Know",
        "description": "Guide to bringing your dog or cat to Switzerland in 2026: EU passport rules, UK arrivals, microchip requirements, and Switzerland's non-EU status explained.",
        "date": "2026-04-30",
        "tags": ["Switzerland", "pet import", "Europe"],
        "faqs": [
            ("Is Switzerland in the EU for pet travel?", "No. Switzerland is not an EU member, but it has bilateral agreements that align its pet import rules very closely with EU regulations. EU pet passports are accepted, and the requirements for microchip and rabies vaccination are the same."),
            ("What does my pet need to enter Switzerland from the UK?", "UK pets need an Animal Health Certificate (AHC). Switzerland accepts the EU-format AHC. The AHC must be issued by an Official Veterinarian and certified by the UK government authority (APHA). Dogs need tapeworm treatment 1-5 days before arrival."),
            ("Does Switzerland require a rabies titre test?", "Pets from most countries do not need a titre test to enter Switzerland if they have valid rabies vaccination. However, pets from countries with high rabies risk or from countries not on the approved list may need a titre test. Confirm with the Swiss Federal Food Safety and Veterinary Office (FSVO) for your origin country."),
            ("Are there dog breed restrictions in Switzerland?", "Switzerland does not have federal breed-specific legislation, but some cantons (Zurich, Geneva, Ticino, and others) have their own restrictions on certain breeds. Check with the specific canton you are moving to before travelling with a restricted breed."),
        ],
        "body": """Switzerland is not an EU member, but for pet travel purposes it behaves much like one. Switzerland has bilateral agreements with the EU, and EU pet passports are accepted for pets entering from EU countries. The Swiss Federal Food Safety and Veterinary Office (FSVO/BLV) manages pet import rules.

**From EU countries**

A valid EU pet passport is accepted. Rabies vaccination and microchip required. No titre test needed from EU countries.

**From the UK**

The UK is now treated as a third country. An Animal Health Certificate in the format accepted by Switzerland is required. Switzerland accepts the EU-format AHC, which UK vets can issue and APHA can endorse. Dogs must have tapeworm treatment 1-5 days before arrival.

**Rabies vaccination**

Switzerland requires current rabies vaccination for all arriving pets. The microchip must be implanted before or on the date of the rabies vaccination. There is a 21-day waiting period after first vaccination before the pet can travel.

**From other countries**

Pets from non-EU, non-approved countries may need a rabies titre test. Confirm your origin country's status with the FSVO before planning travel.

**Canton-level restrictions**

While Switzerland has no national breed bans, individual cantons can restrict specific breeds. Ticino, Geneva, Zurich, and others have had restrictions on breeds including American Staffordshire Terriers, Rottweilers, and others. Check the specific canton you're moving to - the rules vary significantly across the country.""",
    },
    {
        "slug": "austria-pet-import-guide",
        "title": "Bringing a Pet to Austria: EU Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Austria in 2026: EU pet passport rules, AHC for UK arrivals, dog registration requirements, and Austrian import rules.",
        "date": "2026-05-01",
        "tags": ["Austria", "EU pet travel", "pet import"],
        "faqs": [
            ("What does my pet need to enter Austria from the UK?", "UK pets need an Animal Health Certificate (AHC) issued by a UK Official Veterinarian and endorsed by APHA. Dogs must have tapeworm treatment 1-5 days before arrival. Entry must be through an EU-approved border inspection post."),
            ("Does Austria have a dog registration requirement?", "Yes. All dogs must be registered with the local municipality within 3 months of arrival or of the dog turning 3 months old. Austria also has a dog tax (Hundesteuer) in most municipalities. Register at your local Gemeindeamt."),
            ("Are there dog breed restrictions in Austria?", "Austria has federal legislation on dangerous dogs, but breed-specific rules are set at the state (Bundesland) level. Vienna, Lower Austria, Styria, and Tyrol all have lists of restricted breeds. American Pit Bull Terriers, Rottweilers, and other breeds may require a competency test, liability insurance, and muzzling in public in some states."),
            ("What rabies vaccination does Austria require?", "Austria follows EU rules: rabies vaccination must be current and administered after microchip implantation. First vaccination requires a 21-day waiting period. Annual boosters or 3-year boosters depending on the brand used."),
        ],
        "body": """Austria is an EU member state, so the framework is the same as for France, Germany, or Spain. EU pet passports are accepted. Non-EU arrivals need an AHC. What makes Austria slightly different is the state-level breed legislation and the dog registration system.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination is all that's needed. Entry at Vienna International Airport or other approved BIPs.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA is required. Dogs need tapeworm treatment 1-5 days before arrival. The AHC is valid for 10 days from the vet examination. Entry must be at an approved EU border inspection post.

**Dog registration**

All dogs in Austria must be registered with the local Gemeindeamt (municipal office). The registration involves paying the annual Hundesteuer (dog tax), which varies by municipality. In Vienna, this is done online or at local district offices. Some states also require microchip registration in the national dog register.

**Breed restrictions by state**

Austria has no uniform national list. Each Bundesland sets its own rules:
- Vienna: requires a Hundeführerschein (competency test) for all dogs
- Lower Austria, Styria, Upper Austria: restrictions on certain breeds including Pit Bull types, Rottweilers, and others
- Check the specific state rules for your destination before relocating with a breed that might be affected""",
    },
    {
        "slug": "nordic-countries-pet-import-guide",
        "title": "Bringing a Pet to Scandinavia: Sweden, Norway, and Denmark Compared",
        "description": "Guide to pet import rules for Sweden, Norway, and Denmark in 2026: EU membership status, titre test requirements, tapeworm treatment, and what UK arrivals need.",
        "date": "2026-05-01",
        "tags": ["Sweden", "Norway", "Denmark", "Scandinavia", "pet import"],
        "faqs": [
            ("Are Sweden, Norway, and Denmark all in the EU?", "Denmark and Sweden are EU members. Norway is not in the EU but is in the EEA (European Economic Area) and follows aligned rules. For pet travel, Norway accepts EU pet passports and follows similar requirements, but technically treats non-EEA animals differently at border inspection."),
            ("Do pets need a titre test to enter Sweden or Norway?", "Pets from EU countries with valid EU pet passports do not need a titre test. Pets from non-listed third countries need a rabies antibody titre test. Norway additionally has its own import health certificate requirements for non-EEA animals."),
            ("Does Norway have tapeworm treatment requirements?", "Yes. Norway requires tapeworm treatment (echinococcus) for dogs arriving from all countries except a small approved list. The treatment must be administered by a vet 1-7 days before arrival - a slightly wider window than the EU's 1-5 days."),
            ("Can my cat enter Sweden from the UK without a titre test?", "UK-origin cats entering Sweden need an AHC (EU format, APHA-endorsed). Sweden is an EU member, so UK arrivals are treated as non-EU. A titre test is not required for cats from the UK as the UK is on the EU's approved list. Microchip and current rabies vaccination are required."),
        ],
        "body": """Sweden, Norway, and Denmark are three of the most desirable relocation destinations in the world, and all three have clear frameworks for pet import. The key distinction is that Denmark and Sweden are EU members while Norway sits outside the EU but inside the EEA.

**Sweden (EU member)**

Sweden follows EU pet travel rules. EU pet passports accepted from EU countries. Non-EU arrivals (including UK post-Brexit) need an AHC in EU format. Dogs need tapeworm treatment 1-5 days before arrival. Sweden's Swedish Board of Agriculture (Jordbruksverket) administers pet imports.

**Denmark (EU member)**

Same framework as Sweden. EU pet passports accepted. UK arrivals need an AHC endorsed by APHA. Dogs need tapeworm treatment. Danish Veterinary and Food Administration (Foedevarestyrelsen) handles import oversight.

**Norway (EEA, not EU)**

Norway accepts EU pet passports for pets from EU member states. Non-EU arrivals need documentation aligned with EU requirements. Norway has its own import health certificate format for non-EEA animals, managed by the Norwegian Food Safety Authority (Mattilsynet). Tapeworm treatment is required for dogs arriving from all countries except Norway's own short approved list. The treatment window is 1-7 days (slightly wider than the EU's 1-5 days). Norway also requires a 4-hour waiting period after tapeworm treatment before travel.

**From the UK to any Scandinavian country**

UK pets are non-EU animals post-Brexit. An AHC is required for Sweden and Denmark. For Norway, the Mattilsynet format applies. Dogs need tapeworm treatment. All three countries require entry through approved border inspection posts - Oslo Gardermoen, Stockholm Arlanda, and Copenhagen Kastrup all handle live animal arrivals.

**Breeding restrictions**

Sweden has a law banning ear and tail docking, and any dog showing signs of docking may be barred from shows. Otherwise there are no national breed bans in any of the three countries, though individual municipalities may have rules.""",
    },
    {
        "slug": "india-pet-import-guide",
        "title": "Bringing a Pet to India: Import Rules, Documentation and What to Expect",
        "description": "Guide to bringing your dog or cat to India in 2026: DAHD import requirements, health certificate format, approved airports, and breed restrictions.",
        "date": "2026-05-02",
        "tags": ["India", "pet import", "DAHD"],
        "faqs": [
            ("What government authority manages pet imports into India?", "The Department of Animal Husbandry and Dairying (DAHD) under India's Ministry of Fisheries, Animal Husbandry and Dairying regulates live animal imports. Import into India requires a No Objection Certificate (NOC) from DAHD."),
            ("Does India require a rabies titre test for pet imports?", "India does not currently require a rabies antibody titre test for dogs and cats from most countries. A valid rabies vaccination certificate issued by a licensed vet, current at the time of travel, is sufficient."),
            ("What airports accept live animal imports in India?", "Pets can arrive at approved international airports. Delhi (Indira Gandhi International), Mumbai (Chhatrapati Shivaji Maharaj International), Bengaluru (Kempegowda International), and Chennai International are among the airports with facilities for live animal inspection. Confirm current approved entry points with DAHD before booking."),
            ("Are there dog breed restrictions in India?", "India does not have a national breed ban list for household pets, though some states and municipalities have local regulations. Exotic pets and certain wild animal species require additional CITES permits."),
        ],
        "body": """India's pet import rules are managed by the Department of Animal Husbandry and Dairying (DAHD). The process is more paperwork-intensive than many countries, and advance preparation is important.

**DAHD No Objection Certificate**

An import NOC from DAHD is typically required for bringing pets into India. Applications can be submitted to the regional DAHD office for your destination city. The NOC specifies the animal, origin country, and travel details. Apply well in advance - processing times vary.

**Health certificate**

A veterinary health certificate issued by an accredited vet in the origin country is required. For many countries, the certificate must be endorsed by the government authority (e.g., APHA for UK, USDA APHIS for USA). India's DAHD specifies the required health declarations - the vet must certify that the animal is free from signs of infectious disease, is microchipped, and has current vaccinations.

**Microchip and vaccinations**

ISO 11784/11785 microchip is required. Rabies vaccination must be current. Distemper, parvovirus, and other core vaccines are typically listed on the health certificate.

**Approved entry airports**

Not all Indian airports have live animal inspection facilities. Delhi, Mumbai, Bengaluru, and Chennai are the main approved entry points. If you're travelling to another city, you'll arrive at one of these airports and then travel domestically with your pet.

**Practical note**

India's summer heat can be extreme. Pets travelling to India between April and June face temperatures that may trigger airline cargo embargoes. Schedule travel outside peak summer or confirm temperature restrictions with your airline before booking.""",
    },
    {
        "slug": "china-pet-import-guide",
        "title": "Bringing a Pet to China: Import Permits, Quarantine and 2026 Rules",
        "description": "Guide to bringing your dog or cat to China in 2026: GACC import permits, quarantine requirements, approved airports, and the advance documentation process.",
        "date": "2026-05-02",
        "tags": ["China", "pet import", "quarantine"],
        "faqs": [
            ("Does China quarantine imported pets?", "Yes. All dogs and cats arriving in China are subject to quarantine. The standard quarantine period is 7 days for pets from approved countries with complete documentation, but can be extended to 30 days or more depending on origin country and documentation status."),
            ("What is the GACC and how does it affect pet imports to China?", "The General Administration of Customs of China (GACC) oversees live animal imports. All pets entering China require a GACC-approved health certificate from the origin country, issued in a specific format. China's customs authorities inspect arriving pets and documentation at the border."),
            ("Can I only bring one pet to China per person?", "China generally limits one pet per traveller on a personal import basis. Commercial pet imports require a separate approval process. Confirm current limits with GACC or through a China-specialist IPATA agent."),
            ("What are the requirements for bringing a dog from the UK to China?", "UK dogs need a health certificate endorsed by APHA, current rabies vaccination (and in some cases a rabies titre test), microchip, and a Chinese customs-format health certificate countersigned by the relevant authority. A quarantine booking at an approved facility in China is typically required in advance."),
        ],
        "body": """China has one of the more complex pet import processes among major destinations. Preparation needs to start at least 3-6 months before travel, and the paperwork requirements are specific about format and timing.

**Who manages pet imports into China**

The General Administration of Customs of China (GACC) regulates live animal imports. The process involves getting a specific health certificate format signed off by both your origin country's vet and government authority, then inspected by Chinese customs at arrival.

**Quarantine**

All pets entering China undergo quarantine. For pets with complete, correct documentation from approved origin countries, the period is typically 7 days in an approved quarantine facility. Pets with incomplete documentation or from non-approved countries may face 30-day quarantine. You need to pre-book a quarantine facility before the pet arrives.

**Health certificate requirements**

China specifies the exact format of the health certificate required. The vet must use the Chinese-format certificate (not simply the origin country's standard format), and it must be endorsed by the government authority (APHA, USDA, etc.) and in some cases the Chinese embassy in the origin country.

**Titre test**

Some routes to China require a rabies antibody titre test. This is route-dependent - confirm current requirements for your specific origin country with GACC or through a specialist agent.

**Number of pets**

China generally limits one dog or cat per passenger on personal imports. Two pets requires specific approval.

**Working with a specialist agent**

Given the complexity - the specific certificate format, quarantine booking, embassy endorsement, and timing requirements - China is one destination where working with an IPATA-accredited agent who has China experience is strongly recommended. Getting one step wrong can result in extended quarantine or refused entry.""",
    },
    {
        "slug": "argentina-pet-import-guide",
        "title": "Bringing a Pet to Argentina: SENASA Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Argentina in 2026: SENASA health certificate requirements, rabies vaccination rules, and what to prepare for the Buenos Aires arrival.",
        "date": "2026-05-03",
        "tags": ["Argentina", "South America", "pet import", "SENASA"],
        "faqs": [
            ("What does SENASA require for pets entering Argentina?", "SENASA (Servicio Nacional de Sanidad y Calidad Agroalimentaria) requires a health certificate in SENASA format, signed by an accredited vet and endorsed by the government authority of the origin country. The certificate must confirm microchip, rabies vaccination, internal/external parasite treatments, and that the animal is clinically healthy."),
            ("Is there a quarantine period for pets arriving in Argentina?", "Argentina does not quarantine pets from most countries if documentation is complete. Inspection is carried out by SENASA officials at the airport on arrival. Incomplete or incorrect paperwork may result in the animal being held."),
            ("Does Argentina require a rabies titre test?", "Argentina does not currently require a rabies titre test for dogs and cats from most countries. Current rabies vaccination documented on the SENASA health certificate is sufficient."),
            ("What treatments do pets need before arriving in Argentina?", "Pets must be treated for internal parasites (endoparasites) and external parasites (ectoparasites) within a set number of days before arrival. The health certificate must record the treatment product, dose, and date. Confirm current timing requirements with SENASA or through an IPATA agent."),
        ],
        "body": """Argentina is a popular expat destination, and SENASA manages the country's pet import process with a relatively clear set of requirements. The key is getting the health certificate in the right format and endorsed correctly.

**SENASA health certificate**

Argentina requires a SENASA-format health certificate. This is not the same as a standard origin-country vet certificate. The SENASA form asks for specific declarations including microchip details, rabies and other vaccination records, internal and external parasite treatment dates and products, and clinical health status.

The certificate must be signed by an accredited vet in the origin country and endorsed by the government authority (APHA for UK, USDA APHIS for USA, SENASA-equivalent in other countries, etc.).

**Arriving at Buenos Aires Ezeiza**

Most international pets arrive at Ezeiza International Airport (EZE). SENASA inspectors are present at the airport for live animal arrivals. They check the documentation and physically inspect the animal. If all is in order, the pet is released. If documentation is incomplete or incorrect, the animal may be held.

**Vaccinations**

Rabies vaccination must be current. Argentina also typically requires distemper, parvovirus, and other core vaccines to be recorded on the certificate.

**Parasite treatment**

Both internal (endoparasite) and external (ectoparasite) treatments must be carried out within the required window before departure and documented on the certificate. The specific treatments and timing window should be confirmed with SENASA directly or through a specialist agent, as requirements can be updated.

**Number of pets**

Argentina generally allows up to 3 pets per traveller as personal baggage. More than 3 is treated as a commercial import and requires a separate approval process.""",
    },
    {
        "slug": "kenya-pet-import-guide",
        "title": "Bringing a Pet to Kenya: DVS Requirements and What Expats Need to Know",
        "description": "Guide to bringing your dog or cat to Kenya in 2026: DVS import permit, health certificate requirements, rabies rules, and arriving at Nairobi Jomo Kenyatta Airport.",
        "date": "2026-05-03",
        "tags": ["Kenya", "Africa", "pet import", "expat"],
        "faqs": [
            ("What government authority manages pet imports into Kenya?", "The Directorate of Veterinary Services (DVS) under Kenya's State Department for Livestock manages live animal imports. An import permit from DVS is required before the pet travels."),
            ("Does Kenya require a rabies titre test?", "Kenya does not currently require a rabies antibody titre test for dogs and cats from most countries. Current rabies vaccination documented on a valid health certificate is sufficient. Confirm current requirements with DVS for your specific origin country."),
            ("Do pets need to be quarantined when arriving in Kenya?", "Kenya does not operate a mandatory quarantine for pets with complete documentation from most countries. KEPHIS (Kenya Plant Health Inspectorate Service) and DVS inspectors check documents and inspect the animal at Nairobi's Jomo Kenyatta International Airport."),
            ("How do I apply for a Kenya pet import permit?", "Apply to the Directorate of Veterinary Services (DVS) in advance of travel. The application requires details of the animal (species, breed, microchip number, vaccination history), origin country, and travel dates. DVS issues the import permit, which must accompany the pet on arrival."),
        ],
        "body": """Kenya has a growing expat community and receives significant numbers of pets relocating with diplomatic, NGO, and corporate staff. The process is managed by the Directorate of Veterinary Services (DVS) and requires advance preparation.

**DVS import permit**

An import permit from DVS is required before your pet travels. Apply with enough lead time for processing - the permit needs to be in hand before the pet departs the origin country. The permit specifies the animal, origin, destination, and travel window.

**Health certificate**

A veterinary health certificate from an accredited vet in the origin country is required. For UK arrivals, APHA endorsement is needed. The certificate must cover microchip, rabies vaccination, other core vaccines, and a clinical examination confirming the animal is healthy and free from signs of disease.

**Arriving at JKIA**

Most international pets arrive at Jomo Kenyatta International Airport (JKIA) in Nairobi. DVS and KEPHIS inspectors are present for live animal arrivals. They verify the import permit, health certificate, and physically inspect the animal.

**Rabies**

Kenya is in a region with active rabies in wildlife. Rabies vaccination for arriving pets is non-negotiable. First vaccination requires adequate time for immunity development before travel. If you're travelling with a pet that hasn't been vaccinated for rabies, start the process at least 6 weeks before planned travel to allow a completed vaccination course.

**Practical considerations**

Nairobi's climate is moderate (it sits at high altitude), but routes transiting through hot Gulf hubs can create airline cargo embargoes issues. If routing via Dubai or Doha to Nairobi, confirm live animal acceptance at the transit point during summer months.""",
    },
    # ── Route guides ───────────────────────────────────────────────────────
    {
        "slug": "uk-to-germany-pet-transport-guide",
        "title": "Pet Transport from UK to Germany: The Complete 2026 Guide",
        "description": "Everything you need to know about moving your dog or cat from the UK to Germany in 2026: AHC requirements, tapeworm treatment, approved entry points, and what the process looks like.",
        "date": "2026-05-04",
        "tags": ["UK to Germany", "pet transport", "AHC", "route guide"],
        "faqs": [
            ("What does my dog need to travel from the UK to Germany?", "Your dog needs a microchip, current rabies vaccination, an Animal Health Certificate (AHC) issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment administered by a vet 1-5 days before arrival in Germany."),
            ("Does my cat need tapeworm treatment to travel from the UK to Germany?", "No. The tapeworm treatment requirement only applies to dogs, not cats. Your cat needs microchip, current rabies vaccination, and an AHC endorsed by APHA."),
            ("How long is the UK to Germany AHC valid for?", "The AHC is valid for 10 days from the date of the veterinary examination. Your entry into Germany must occur within this 10-day window. For travel by air, align the vet appointment 1-5 days before departure."),
            ("Can I drive from the UK to Germany with my pet via the Channel Tunnel?", "Yes. You can travel with your pet via Eurotunnel Le Shuttle (pet on board with you) or via ferry to France and then drive to Germany. The same AHC and tapeworm requirements apply regardless of route. Pets must have a microchip readable by Eurotunnel staff before boarding."),
        ],
        "body": """Moving from the UK to Germany is one of the most common European relocation routes, and the pet transport process is well-understood. Since Brexit, UK pets are non-EU animals and need an Animal Health Certificate instead of an EU pet passport.

**What you need**

Your dog or cat needs:
- ISO 11784/11785 microchip (implanted before or on the date of rabies vaccination)
- Current rabies vaccination (first vaccination requires a 21-day waiting period before EU travel)
- Animal Health Certificate (AHC) - issued by a UK Official Veterinarian (OV) and endorsed by APHA
- Dogs only: tapeworm treatment (praziquantel) administered by a vet 1-5 days before arrival in Germany

**The AHC process**

Find an APHA-authorised Official Veterinarian. Not all vets are OVs - check the RCVS Find a Vet tool for OV status. The vet examines your pet and completes the AHC. The APHA then endorses it (online via APHA's system - this can be done quickly). Time the vet appointment 1-5 days before departure so the tapeworm treatment timing and AHC validity both line up.

**Entry into Germany**

Germany has multiple approved border inspection posts for pets arriving from non-EU countries. Frankfurt am Main, Munich, Berlin Brandenburg, Hamburg, and Dusseldorf airports all process live animal arrivals. Pets arriving by land via the Netherlands or Belgium must also pass through approved BIPs.

**German registration**

Once in Germany, dogs must be registered with the local Einwohnermeldeamt or Hundesteuer registration system within a short period of arrival. Most German states charge a Hundesteuer (dog tax). Berlin, Munich, and Hamburg each have their own registration processes.

**Route options**

By air: direct UK-Germany flights are quick and low-stress. Dogs must travel as cargo (most airlines don't allow dogs in cabin on European routes). By land: Eurotunnel with your pet on board, then drive through France/Belgium/Netherlands to Germany. This is popular and lets you keep your pet close.""",
    },
    {
        "slug": "uk-to-canada-pet-transport-guide",
        "title": "Pet Transport from UK to Canada: Rules, Requirements and What to Expect",
        "description": "Complete guide to moving your dog or cat from the UK to Canada in 2026: CFIA import rules, health certificate requirements, and what arriving at a Canadian airport looks like.",
        "date": "2026-05-04",
        "tags": ["UK to Canada", "pet transport", "CFIA", "route guide"],
        "faqs": [
            ("What does my dog need to travel from the UK to Canada?", "Dogs entering Canada from the UK need a current rabies vaccination (if over 3 months old), microchip, and a CFIA-format health certificate signed by a UK vet. A USDA/CFIA import permit is not required for household pets, but the health certificate must be present at arrival."),
            ("Do cats need a rabies vaccination to enter Canada from the UK?", "Cats entering Canada do not require rabies vaccination under CFIA rules (unlike dogs). However, most airlines and provinces recommend keeping vaccinations current. Check provincial requirements for the specific Canadian province you're moving to."),
            ("Does Canada have a quarantine requirement for pets?", "Canada does not quarantine pets from the UK with complete documentation. CFIA inspectors at the port of entry check the health certificate and inspect the animal."),
            ("Can I bring more than one pet to Canada from the UK?", "Yes. There is no fixed limit on the number of pets per traveller for personal imports to Canada, but each animal needs its own health certificate. Airlines have their own per-booking limits on live animals."),
        ],
        "body": """Canada is among the more pet-friendly countries for international arrivals. The CFIA (Canadian Food Inspection Agency) manages pet imports, and the requirements for dogs and cats from the UK are straightforward.

**Dogs entering Canada from the UK**

Dogs over 3 months old need:
- Current rabies vaccination
- Health certificate - there is no mandatory CFIA-specific form for personal household pets, but the certificate should come from a licensed vet and confirm microchip, vaccination status, and clinical health. CFIA may ask for it at arrival.

Canada does not require an import permit for household pets, and does not require the AHC format used for EU entry. This makes the Canada process simpler than EU destinations.

**Cats entering Canada from the UK**

Cats do not need rabies vaccination under CFIA's federal rules, though this may vary by province. A vet health certificate is still strongly recommended to confirm microchip and vaccination history.

**At the Canadian airport**

CFIA inspectors are present at major international airports (Toronto Pearson, Vancouver, Montreal, Calgary, and others). They will check the health certificate and inspect the animal. The process is typically quick if documentation is in order. Declare your pet on the customs declaration form on the aircraft.

**Provincial rules**

Each Canadian province can set its own rules. British Columbia, Ontario, and Quebec are the most common destinations for UK expats. Check the specific province's animal control and import rules, as breed-specific legislation varies significantly. Ontario has no BSL provincially, but individual municipalities may have restrictions.

**Flying cargo or in-cabin**

Most major UK-Canada airlines (Air Canada, British Airways, WestJet) allow small pets in cabin for qualifying pets. Larger dogs travel as cargo. Air Canada has an extensive cargo network and accepts a wide range of breeds as cargo. Check breed restrictions with your specific airline before booking.""",
    },
    {
        "slug": "uk-to-singapore-pet-transport-guide",
        "title": "Pet Transport from UK to Singapore: Licences, Quarantine and the Process",
        "description": "Complete guide to moving your dog or cat from the UK to Singapore in 2026: AVS licence, approved breeds, quarantine rules, and the full preparation timeline.",
        "date": "2026-05-05",
        "tags": ["UK to Singapore", "pet transport", "AVS", "quarantine", "route guide"],
        "faqs": [
            ("How long does quarantine last for pets arriving in Singapore from the UK?", "Pets from the UK entering Singapore undergo a 10-day quarantine in an AVS-approved facility. Singapore is a rabies-free country and maintains this status through mandatory quarantine of arriving pets."),
            ("What licence does my pet need to enter Singapore?", "All dogs and cats require a licence from Singapore's National Parks Board (NParks) / Animal and Veterinary Service (AVS) before arrival. The licence application must be submitted in advance, and approval must be received before the pet is transported."),
            ("How long does the Singapore pet import preparation take?", "Allow at least 4-6 months. The preparation timeline includes rabies vaccination, 30-day titre test wait, titre test, 3-month wait post-titre test (for many countries), and then the licence application. The UK is on Singapore's Category C list - the titre test and 3-month wait apply."),
            ("Are there breed restrictions for dogs entering Singapore?", "Yes. Singapore maintains a list of approved dog breeds. Only listed breeds are allowed. This list is controlled and includes many common breeds but excludes several large or powerful types. Check the full approved breeds list on the AVS website before planning your move."),
        ],
        "body": """Singapore is a rabies-free city-state with strict biosecurity rules. The pet import process is well-documented but requires months of advance planning. There are no shortcuts.

**Singapore's category system**

Singapore categorises origin countries by rabies risk. The UK is currently on Category C (countries with low but non-zero rabies risk). Category C requires:
1. ISO-compliant microchip
2. Rabies vaccination (at least 2 vaccinations)
3. Rabies antibody titre test (FAVN test) at an approved laboratory showing at least 0.5 IU/ml
4. A 30-day wait after vaccination before the titre test can be conducted
5. A minimum 3-month wait after the titre test before travel

This means your preparation window is at least 4 months from the first vet appointment. Start early.

**Breed restrictions**

Singapore only permits specific approved dog breeds. The list is on the NParks/AVS website and is strict - several large or fighting-type breeds are not permitted at all. Check your breed before doing anything else.

**The licence application**

Before transport, you must apply for and receive an import licence from AVS/NParks. The application is online via the NParks portal. Submit it well in advance of your intended travel date. The licence specifies the travel window.

**Quarantine**

All arriving pets undergo 10 days in an AVS-approved quarantine facility at Pet Motel or similar approved centres. You can visit your pet during quarantine. Costs vary by facility and species.

**Health certificate**

The UK's APHA issues the required health certificate for Singapore, endorsed in the UK format that Singapore accepts. The certificate must be issued within 10 days of travel.

**Practical note**

Singapore-UK is a 13-14 hour flight. Pets travel as cargo. Most airlines routing through the Middle East (Emirates, Qatar, Etihad) or via India (British Airways, Singapore Airlines) accept pet cargo on this route - confirm with your chosen carrier well in advance.""",
    },
    {
        "slug": "uk-to-japan-pet-transport-guide",
        "title": "Pet Transport from UK to Japan: MAFF Rules, Quarantine and the Preparation Timeline",
        "description": "Complete guide to moving your dog or cat from the UK to Japan in 2026: MAFF requirements, titre test, the 180-day quarantine risk, and how to qualify for the short quarantine pathway.",
        "date": "2026-05-05",
        "tags": ["UK to Japan", "pet transport", "MAFF", "quarantine", "route guide"],
        "faqs": [
            ("How long is quarantine for pets arriving in Japan from the UK?", "If all documentation is correct and the UK is recognised as an approved low-rabies country, pets can qualify for a minimum 12-hour quarantine. However, any documentation error or timing issue can result in 180 days (6 months) of quarantine. Preparation must be meticulous."),
            ("What tests and vaccinations does Japan require?", "Japan requires: microchip (ISO compliant), 2 rabies vaccinations (spaced at least 30 days apart), a rabies antibody titre test showing at least 0.5 IU/ml, a 180-day wait after the titre test before arrival, and a health certificate issued within 10 days of travel endorsed by APHA."),
            ("When should I start preparing to move my pet to Japan?", "Start at least 7-8 months before travel. The preparation timeline includes: microchip, first vaccination, 30+ days, second vaccination, 30 days minimum, titre test, then a mandatory 180-day wait after the titre test. Total: at least 210 days from first vet visit to travel."),
            ("Which airports in Japan accept pet arrivals?", "Pets can arrive at Narita International Airport (NRT), Tokyo Haneda (HND), Osaka Kansai (KIX), and a small number of other approved airports. Pre-notification to the Animal Quarantine Service (AQS) at the destination airport is required at least 40 days before arrival."),
        ],
        "body": """Japan is one of the most documentation-intensive pet import destinations in the world. The reward is a country with excellent veterinary care and a high standard of living for pets. The preparation process, however, is long and unforgiving of errors.

**The 180-day rule**

This is the critical timeline element for UK pets entering Japan. After the rabies antibody titre test (which must show at least 0.5 IU/ml), there is a mandatory 180-day waiting period before the pet can enter Japan. Get the titre test date right, and you'll qualify for the short 12-hour quarantine on arrival. Get it wrong - or have a documentation error - and your pet faces up to 180 days in a MAFF quarantine facility at your cost.

**The full preparation timeline**

1. Microchip implanted (ISO 11784/11785)
2. First rabies vaccination (must be after microchip)
3. Wait at least 30 days
4. Second rabies vaccination
5. Wait at least 30 days after the second vaccination
6. Rabies antibody titre test at an approved laboratory (UK: only a few approved labs)
7. Mandatory 180-day wait after the titre test date
8. Health certificate issued by a UK OV, endorsed by APHA, within 10 days of travel
9. Pre-notification to the Animal Quarantine Service (AQS) at least 40 days before arrival

Total minimum timeline: approximately 7-8 months from first vet visit.

**Pre-notification to Japan AQS**

This step catches many pet owners out. You must notify the Animal Quarantine Service at the specific Japanese airport you're arriving at, at least 40 days before travel. Failure to pre-notify means the pet cannot enter at that airport.

**Documentation**

Japan's documentation requirements are exact about format. Work with a vet experienced in Japan export, use an IPATA-accredited agent who has Japan experience, and triple-check every date and test result before the pet travels. One error can cost 180 days in quarantine.

**Airlines for UK-Japan**

Finnair (via Helsinki), British Airways (via Heathrow), Japan Airlines (JAL), and ANA all operate UK-Japan routes. Pets travel as cargo. Finnair's Arctic routing is one of the shortest transit options. Confirm live animal cargo acceptance and breed restrictions with the airline.""",
    },
    {
        "slug": "uk-to-france-pet-transport-guide",
        "title": "Pet Transport from UK to France: AHC, Tapeworm Treatment and the 2026 Rules",
        "description": "Step-by-step guide to moving your dog or cat from the UK to France in 2026: AHC documentation, tapeworm timing, approved entry points, and the Channel Tunnel option.",
        "date": "2026-05-06",
        "tags": ["UK to France", "pet transport", "AHC", "route guide"],
        "faqs": [
            ("What does my dog need to travel from the UK to France?", "Microchip, current rabies vaccination (21-day wait after first vaccination), an Animal Health Certificate (AHC) issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment (praziquantel) administered by a vet 1-5 days before arrival in France."),
            ("Can I take my cat through the Channel Tunnel to France?", "Yes. Cats can travel via Eurotunnel Le Shuttle with you in the car. Cats need microchip, current rabies vaccination, and an AHC. Cats do not need tapeworm treatment (this applies to dogs only)."),
            ("How much does it cost to get an AHC for my pet?", "AHC costs vary by vet practice. Expect to pay GBP 100-200 for the vet examination and certificate, plus a small APHA endorsement fee. The endorsement is processed online by the vet through APHA's system and is usually completed on the same day or next day."),
            ("Can I use the same AHC to re-enter the UK after visiting France?", "No. Each entry into an EU/EEA country requires a new AHC from a UK OV. The AHC is valid for 10 days from the vet examination date, for a single entry. For frequent travel, consider whether a pet travel pass or registered third-country animal status could simplify the process."),
        ],
        "body": """France and the UK share one of the world's busiest cross-channel travel routes. With pets, the process has added steps post-Brexit, but it's still very manageable with a bit of advance planning.

**What your pet needs**

Microchip - ISO 11784/11785, implanted before or on the same date as the rabies vaccination.

Rabies vaccination - must be current. First vaccination requires a 21-day waiting period before EU entry is permitted. Annual boosters or 3-year boosters depending on the product used.

Animal Health Certificate (AHC) - issued by an APHA-authorised Official Veterinarian in the UK, endorsed by APHA. Valid for 10 days from the vet examination date. Time the appointment carefully: the AHC must be valid when you cross the border, and dogs need their tapeworm treatment 1-5 days before crossing (not before the vet appointment, but before the French border).

Tapeworm treatment (dogs only) - praziquantel, administered by a vet, 1-5 days before arrival in France. Ask your OV to record the treatment on or alongside the AHC.

**Channel Tunnel**

Eurotunnel Le Shuttle allows pets to stay in the car with you for the 35-minute crossing. You'll go through DEFRA/Border Force checks at the UK end and French customs at Coquelles. Make sure all documentation is ready and accessible for inspection at both ends. Pet microchips are scanned.

**Ferry routes**

Dover-Calais, Portsmouth-Le Havre, Portsmouth-Caen, Newhaven-Dieppe, and other routes accept pets. Cats and dogs are typically kept in the car or in designated on-deck pet areas. Check each ferry company's specific pet policy as they vary.

**Air**

Direct UK-France flights are short - Paris, Nice, Bordeaux, Lyon. Most airlines require dogs to travel as cargo for international flights. Air France, British Airways, and easyJet (select routes) all operate the route.""",
    },
    {
        "slug": "australia-to-usa-pet-transport-guide",
        "title": "Pet Transport from Australia to USA: CDC Rules and the Documentation Process",
        "description": "Complete guide to moving your dog or cat from Australia to the USA in 2026: CDC dog import requirements, microchip timing rules, USDA health certificate, and airline options.",
        "date": "2026-05-06",
        "tags": ["Australia to USA", "pet transport", "CDC", "route guide"],
        "faqs": [
            ("What are the CDC's requirements for dogs arriving in the USA from Australia?", "Under CDC's 2024 rules, dogs arriving in the USA from Australia need: microchip implanted on or before the date of the first rabies vaccination, current rabies vaccination, USDA-endorsed health certificate or a CDC Dog Import Permit for dogs vaccinated outside the USA. Australia is a low-risk country for dog screwworm, so some additional requirements that apply to other countries do not apply here."),
            ("Does my cat need any special documents to enter the USA from Australia?", "Cats do not face the same CDC requirements as dogs when entering the USA. A standard vet health certificate confirming the cat is healthy and microchipped is recommended but a federal permit is not required."),
            ("Do I need a USDA health certificate for my dog from Australia to USA?", "Yes. Dogs entering the USA from Australia require a USDA APHIS-endorsed health certificate. This is completed by a vet and endorsed by USDA APHIS (or in Australia, by a government vet in the format accepted by USDA)."),
            ("Which airlines fly dogs as cargo from Australia to the USA?", "Qantas, United Airlines, and American Airlines operate Australia-USA routes. Cargo policies for live animals vary by route, season, and aircraft type. Confirm live animal cargo acceptance with each airline for your specific origin-destination pair, as not all routes have live animal hold approval."),
        ],
        "body": """Australia to USA is a long-haul route (14-24 hours depending on the connection), and the documentation requirements have become more complex following the CDC's 2024 dog import rule changes. Cats have a simpler process.

**CDC's 2024 dog import rules**

The key change for dogs is the microchip-vaccination timing rule: the microchip must have been implanted on or before the date of the first rabies vaccination. If your dog was vaccinated before being microchipped, or if you're not sure about the order, the rabies vaccination course may need to be repeated (boosted) after microchipping for the vaccination to be considered valid under CDC rules.

Australia is classed as a low-risk country for dog screwworm, which means the separate screwworm treatment that some other origin countries require does not apply.

**Health certificate**

Dogs need a health certificate completed by a vet in Australia and endorsed by USDA APHIS (or the equivalent Australian government authority in USDA-accepted format). The Australian Veterinary Association and the Australian Department of Agriculture, Fisheries and Forestry can advise on the correct format.

**Cats**

Cats do not require CDC permits or specific federal health certificates for USA entry. A vet health certificate is recommended and individual states may have their own requirements.

**The flight itself**

Australia-USA is among the longest pet transport routes in the world. The journey typically routes through Los Angeles (LAX) or other West Coast hubs. Pets travel as cargo. The long flight time plus temperature requirements at both ends make airline selection and transit timing important. Most direct routes (Qantas Sydney-Los Angeles, for example) are around 14-15 hours. Connecting via Asia adds significant time.

**On arrival in the USA**

USDA APHIS or CBP (Customs and Border Protection) inspectors at the port of entry check documentation and may inspect the animal. Declare your pet on the customs form.""",
    },
    # ── Breed blog guides ──────────────────────────────────────────────────
    {
        "slug": "travelling-with-a-golden-retriever-internationally",
        "title": "Travelling Internationally with a Golden Retriever: What You Need to Know",
        "description": "A practical guide to flying with a Golden Retriever on international routes: cargo requirements, crate sizing, health prep, and which destinations have breed-specific considerations.",
        "date": "2026-05-06",
        "tags": ["Golden Retriever", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a Golden Retriever travel in the cabin on a flight?", "No. Golden Retrievers are too large to travel in the cabin on commercial flights. They must travel as cargo in the hold in an IATA-compliant crate. Most major airlines accept them as checked cargo on international routes."),
            ("What size crate does a Golden Retriever need for air travel?", "Most adult Golden Retrievers require an IATA-compliant crate of approximately 91cm x 61cm x 66cm (IATA size 500 or equivalent). The crate must be large enough for the dog to stand, sit, turn around, and lie down without touching the sides or top. Measure your dog before ordering."),
            ("Are Golden Retrievers banned from any countries?", "No. Golden Retrievers are not subject to breed-specific legislation in any major destination country. They are widely accepted globally."),
            ("How do I prepare my Golden Retriever for a long cargo flight?", "Crate train over several weeks before travel so the crate is a comfortable space. Avoid feeding 4-6 hours before departure. Provide water via a drip bottle attached inside the crate. Line the crate with absorbent bedding. Include a worn clothing item for comfort. Consult your vet about whether any calming aids are appropriate."),
        ],
        "body": """Golden Retrievers are one of the most popular international travel dogs - friendly, adaptable, and not subject to breed bans anywhere. The main considerations are their size (cargo only), crate sizing, and preparing them for the experience.

**Cargo travel**

Golden Retrievers are medium-large dogs and will always travel as checked cargo rather than as carry-on baggage. This means they're in the temperature-controlled hold section of the aircraft, not in the cabin with you. The hold is pressurised and temperature-controlled on modern aircraft. Your dog will not be in the same physical space as you during the flight, but can be reunited with you at the baggage/cargo hall on arrival.

**Crate requirements**

IATA regulations specify that the crate must be large enough for the dog to stand, sit, turn around, and lie down naturally. For an average adult Golden Retriever:
- Crate length: dog's length from nose to tail base + 10cm
- Crate height: dog's height from ground to top of head when standing + 10cm
- Crate width: dog's width x 2

Most adult Goldens fit an IATA 500 (91cm x 61cm x 66cm) or equivalent. Measure your specific dog.

**Crate training**

Start introducing the crate weeks or months before travel. Feed meals in the crate, leave it open in a familiar space, encourage exploration. A dog that is relaxed in its crate will handle the flight far better than one that has never been crated.

**Health preparation**

Ensure vaccinations are current for the destination country. Golden Retrievers do not have specific breed-related respiratory issues (unlike brachycephalic breeds), but the usual pre-travel vet check is important. Confirm the dog is fit to fly.

**Sedation**

Veterinary guidance strongly advises against sedating dogs for air travel. Sedation can affect heart and respiratory function and can be dangerous at altitude. Some calming aids (adaptil, certain supplements) can help but always discuss with your vet before using anything.""",
    },
    {
        "slug": "travelling-with-a-french-bulldog-internationally",
        "title": "Flying Internationally with a French Bulldog: Restrictions, Risks and What to Do",
        "description": "A guide to the realities of flying internationally with a French Bulldog in 2026: which airlines accept them, cargo restrictions, health risks, and safer alternatives to explore.",
        "date": "2026-05-06",
        "tags": ["French Bulldog", "brachycephalic", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a French Bulldog fly in a plane?", "Many airlines have banned French Bulldogs from cargo travel due to respiratory risks associated with brachycephalic (flat-faced) anatomy. A small number of airlines may accept them under specific conditions. Confirm with each airline directly and consult your vet before booking."),
            ("Why are French Bulldogs restricted on flights?", "French Bulldogs have shortened airways due to their brachycephalic (flat-faced) anatomy. At altitude, in heat, or under stress, they can experience respiratory distress. A number of in-flight deaths of brachycephalic breeds led airlines and aviation bodies to introduce breed restrictions."),
            ("Is it safe for a French Bulldog to fly as cargo?", "The risk is higher than for other breeds. Vets generally advise against air travel for French Bulldogs unless necessary. If travel is unavoidable, consult a vet experienced with brachycephalic breeds, choose a non-summer route to avoid heat, and confirm the airline's specific policy."),
            ("What are alternatives to flying a French Bulldog internationally?", "For shorter routes (e.g., UK to France, UK to Belgium), consider ferry travel with the dog in the car or on deck in a carrier - this avoids the pressure and temperature stresses of cargo holds. For longer international moves where flying is unavoidable, consult a vet and an IPATA-accredited specialist agent experienced with brachycephalic breed transport."),
        ],
        "body": """French Bulldogs are one of the world's most popular dog breeds, and one of the most complicated to move internationally. The flat-faced anatomy that makes them so appealing as companions also creates real health risks when flying.

**Why the restrictions exist**

Brachycephalic breeds (French Bulldogs, English Bulldogs, Pugs, Boston Terriers, Shih Tzus, and others) have shortened skulls that compress their airways. Under normal conditions, most are fine. Under the stresses of air travel - heat, altitude, confinement, anxiety - the risk of respiratory distress increases significantly. Several airline cargo fatalities involving French Bulldogs and similar breeds led to widespread airline restrictions from around 2018 onwards.

**Airline policies**

Most major airlines now restrict French Bulldogs from cabin travel and many from cargo as well. The list of airlines that accept them is short and conditions-dependent. Always confirm directly with the airline - policies change, and what was accepted last year may not be accepted today.

**Vet assessment**

Before any international move with a French Bulldog, a vet assessment by someone experienced with brachycephalic syndrome is important. A vet can evaluate your specific dog's anatomy and respiratory health and advise on whether the planned journey is appropriate.

**If flying is unavoidable**

Choose early morning or late evening flights to reduce heat exposure. Avoid routes with summer temperature embargoes. Ensure the crate is the correct size - too small increases stress, too large can cause the dog to be thrown around during turbulence. Brief the cargo handlers at check-in that the animal is a brachycephalic breed. Have a vet health certificate confirming fitness for flight.

**Alternatives**

For moves within Europe, ferry travel avoids the cargo hold entirely. For moves between continents where alternatives don't exist, work with an IPATA-accredited agent who has experience specifically with brachycephalic breed transport - they will know which airlines, routes, and conditions currently offer the best options.""",
    },
    # ── Practical guides ───────────────────────────────────────────────────
    {
        "slug": "pet-relocation-budget-guide",
        "title": "Pet Relocation Budget Guide: What International Pet Transport Actually Costs",
        "description": "A realistic breakdown of international pet transport costs in 2026: vet and certificate fees, cargo costs, quarantine fees, agent fees, and what affects the final price.",
        "date": "2026-05-06",
        "tags": ["cost guide", "pet transport", "budget", "relocation"],
        "faqs": [
            ("What is the average cost to move a pet internationally?", "International pet transport costs typically range from USD 1,000 to USD 5,000 for simple moves (e.g., UK to France, USA to Canada). Complex routes involving quarantine countries (Australia, New Zealand, Singapore, Japan) commonly cost USD 5,000 to USD 15,000 or more, including quarantine fees."),
            ("What does a pet transport agent charge?", "IPATA-accredited agent fees typically range from USD 500 to USD 2,500 depending on route complexity, number of animals, and services included. Agent fees usually cover documentation coordination, airline booking, and guidance but are separate from airline cargo and quarantine fees."),
            ("How much does quarantine cost in Australia?", "Australia's mandatory quarantine typically costs AUD 2,000 to AUD 4,000 per animal for a 10-day quarantine period, depending on the facility and species. This is in addition to airline cargo fees and agent fees."),
            ("Can I save money on pet transport by doing it myself without an agent?", "On simple routes (e.g., within the EU or UK to USA), experienced pet owners can manage the documentation themselves and save agent fees. On complex quarantine routes (Australia, NZ, Singapore, Japan), an agent's experience typically pays for itself by avoiding costly documentation errors."),
        ],
        "body": """International pet transport is not cheap, and the costs vary enormously depending on destination, dog size, and route complexity. Here's a realistic breakdown of what you're actually paying for.

**Vet and documentation costs**

These are the foundational costs regardless of destination:
- Microchip (if not already implanted): GBP/USD 30-70
- Rabies vaccination: GBP/USD 50-100
- Rabies titre test (if required): GBP/USD 100-200 for the blood draw, plus lab fee GBP/USD 60-120
- Health certificate: GBP/USD 80-200 depending on complexity
- APHA/USDA/government endorsement: GBP/USD 30-100
- Additional vaccinations (distemper, parvovirus, etc.): GBP/USD 50-100

Total vet/docs: typically GBP/USD 250-700 for simple routes, 500-1,000+ for titre test destinations.

**Airline cargo costs**

Cargo costs are calculated on volumetric weight (the greater of actual weight vs dimensional weight). A medium dog in an IATA 400 crate might weigh 25kg actual but have a dimensional weight of 40kg+ depending on airline calculation methods.

Typical cargo costs:
- UK to France (short haul): GBP 200-500
- UK to USA (transatlantic): GBP 400-1,200
- UK to Australia (long haul, complex route): GBP 800-2,500+
- Small dogs in cabin (where permitted): GBP/USD 50-150 per segment

**Quarantine fees**

For quarantine destinations:
- Australia: AUD 2,000-4,000 for 10 days
- New Zealand: NZD 1,800-3,500 for 10 days
- Singapore: SGD 800-1,800 for 10 days
- Japan: varies but can be substantial for longer quarantine stays

**Agent fees**

IPATA agents typically charge USD 500-2,500 for international moves, depending on complexity. On simple routes you may not need an agent. On quarantine routes, an agent's knowledge of timing, documentation format, and quarantine facility booking is worth the fee.

**Total cost examples**

UK to France (small dog, cabin): GBP 400-800
UK to USA (medium dog, cargo): GBP 1,200-2,500
UK to Australia (any dog, 10-day quarantine): GBP 4,000-9,000+
UK to Japan (any dog, short quarantine if docs perfect): GBP 3,500-8,000+""",
    },
    {
        "slug": "first-time-pet-relocation-guide",
        "title": "First Time Moving Your Pet Internationally? A Step-by-Step Guide",
        "description": "A practical first-timer's guide to international pet relocation in 2026: where to start, what to research, how documentation works, and what to expect on travel day.",
        "date": "2026-05-06",
        "tags": ["first time", "pet relocation", "step by step", "practical guide"],
        "faqs": [
            ("Where do I start when planning to move my pet internationally?", "Start with your destination country's import rules. Look up the official government veterinary authority for your destination and confirm: (1) whether your breed is permitted, (2) what vaccinations and tests are required, (3) whether a titre test is needed, and (4) whether there's a mandatory wait time after the titre test. Then work backwards from your travel date to create a preparation timeline."),
            ("Do I need a pet transport agent for an international move?", "For simple routes (e.g., within the EU, UK to France, USA to Canada), experienced pet owners can often manage documentation themselves. For quarantine destinations (Australia, NZ, Singapore, Japan) or routes with complex multi-country transit requirements, an IPATA-accredited agent is strongly recommended."),
            ("How far in advance do I need to start preparing?", "For simple routes: 4-8 weeks minimum. For titre test destinations (Australia, Singapore, Hawaii, UK entering EU): at least 3-4 months. For Japan: at least 7-8 months. Start earlier than you think you need to."),
            ("What is an IPATA-accredited agent?", "IPATA (International Pet and Animal Transportation Association) is the global trade association for pet transport professionals. IPATA members operate to a defined code of conduct and professional standards. Using an IPATA agent gives you a verified baseline of professional competence for international pet moves."),
        ],
        "body": """Moving a pet internationally for the first time can feel overwhelming. There's a lot of information online, some of it contradictory or outdated. This guide gives you the framework to approach it methodically.

**Step 1: Check your destination's import rules**

Before anything else, go to the official government veterinary authority website for your destination country and look up live animal (specifically dog or cat) import requirements. Don't rely on forum posts or travel blogs as your primary source - these go out of date. The official sources are:

- Australia: DAFF (Department of Agriculture, Fisheries and Forestry)
- New Zealand: MPI (Ministry for Primary Industries)
- USA: CDC (for dogs) + USDA APHIS
- UK: APHA (Animal and Plant Health Agency) / DEFRA
- EU: European Commission DG SANTE
- Singapore: NParks / AVS
- Japan: MAFF Animal Quarantine Service

For other countries, search "pet import [country name] official" and look for government domains (.gov, .go.jp, .europa.eu, etc.).

**Step 2: Check whether your breed is permitted**

Some countries ban specific breeds. Before investing in vaccines, vet visits, and planning, confirm your breed is not on a restricted list. Check the destination country's breed-specific legislation and the airline's restricted breeds list.

**Step 3: Build your preparation timeline**

Work backwards from your planned travel date. Key variables:
- Does the destination require a titre test? Add 4+ months (titre test + 30-day wait for results + 3-month wait post-titre for many destinations)
- Does the destination require a 21-day post-vaccination wait? Add 3-4 weeks after first rabies vaccination
- When does the health certificate need to be issued? Usually within 10 days of travel

Create a calendar. Mark each date. Do not assume you have time to spare.

**Step 4: Choose your airline and route**

Find out which airlines accept your pet on your specific route. Check cargo policies (not just their general pet page - check the specific origin-destination route live animal acceptance). Look at whether you want to route direct or via a hub, and what the temperature restrictions are at the hub in your travel month.

**Step 5: Book cargo and quarantine (if needed)**

For quarantine destinations, book your quarantine space before booking your flight. Quarantine facilities have limited capacity. Confirm the booking with the facility, then book the airline cargo.

**Step 6: Get your pet's documentation in order**

With your timeline confirmed and your vet briefed, work through: microchip check, vaccinations, titre test (if needed), health certificate timing. Do not leave the health certificate to the last minute.

**Step 7: Travel day**

Arrive early at the airport. Have all documents in a folder, originals on top. Confirm your cargo drop-off process with the airline. Brief check-in staff that you have a live animal. Once through, your pet is in the airline's care until you collect at the destination cargo hall.""",
    },
    {
        "slug": "pets-and-international-schools-relocation-families",
        "title": "Relocating with Pets as an Expat Family: What International School Families Need to Know",
        "description": "A guide to pet relocation for families moving for international school assignments: timing your pet's move, destination rules for common expat locations, and managing the process with children.",
        "date": "2026-05-05",
        "tags": ["expat families", "international schools", "pet relocation", "practical guide"],
        "faqs": [
            ("Should I move my pet at the same time as the family?", "Not always. For quarantine destinations (Australia, Singapore, Japan), the pet's quarantine period may mean the pet arrives weeks after the family. Plan the pet's documentation timeline independently and align quarantine release with your settling-in period rather than your initial arrival."),
            ("What are the most common expat family destinations that require pet quarantine?", "Australia, New Zealand, Singapore, and Japan all require quarantine for arriving pets. Hawaii (USA) also has quarantine requirements for dogs. These are all common postings for international school families."),
            ("How do I explain pet travel to young children?", "Be honest about what will happen: the pet will travel in a special safe part of the plane, will be looked after by trained staff, and you'll all be reunited after a short wait (or at the quarantine facility for visits, if allowed). Avoid saying it's 'like a holiday' - children will question why the pet isn't excited."),
            ("Can I visit my pet in quarantine?", "Australia, New Zealand, and Singapore all allow owner visits to quarantined pets, though booking in advance is required. Japan's quarantine rules around visits are stricter. Check facility-specific policies when booking quarantine accommodation."),
        ],
        "body": """International school postings come with complex logistics, and adding a pet into the mix requires careful coordination. The families that handle it best are those who start the pet's preparation timeline as soon as the posting is confirmed - sometimes months before the children's school year changes.

**The timing challenge**

For non-quarantine destinations (UK, Germany, USA, Canada, most EU countries), the pet can typically travel with the family or within a few weeks. For quarantine destinations, the timeline is different:

- Australia: pet preparation takes 3+ months, then 10 days quarantine on arrival. The pet often goes ahead or arrives just behind the family.
- Singapore: 4-6 months preparation, 10 days quarantine. Many families send the pet before the move to align quarantine release with arrival.
- Japan: 7-8 months preparation, 12-hour quarantine if perfect docs. No flexibility on timeline.
- New Zealand: 3+ months preparation, 10 days quarantine.

**Breed check first**

Some postings go to countries with breed restrictions. Singapore only allows approved breeds (check the AVS list). Australia has state-level breed legislation (dangerous dogs lists vary by state). If your family has a breed that might be affected, check before accepting the posting or before making the posting permanent.

**Common expat family destinations: quick reference**

Singapore: 4-6 months prep, 10-day quarantine, approved breeds list - check before you travel.
Dubai/UAE: relatively straightforward, vet cert + import permit required, some breed restrictions on large/powerful breeds.
Australia: 3+ months prep depending on origin country, 10-day quarantine at Mickleham, Melbourne.
Japan: 7-8 months prep, documentation must be perfect.
USA: simpler than most - microchip, health cert, CDC rules for dogs.
Germany/EU: AHC for UK/non-EU origin, tapeworm for dogs. Relatively quick process.

**Using an agent for family moves**

When you're also managing school applications, accommodation, and a family move, adding pet documentation to the personal to-do list can become overwhelming. An IPATA-accredited agent can take the entire pet logistics off your plate, which many expat families find is well worth the fee.""",
    },
    {
        "slug": "how-to-find-a-good-pet-transport-agent",
        "title": "How to Find a Good Pet Transport Agent: What to Ask and What to Avoid",
        "description": "A guide to choosing an international pet transport agent in 2026: IPATA accreditation, what to look for, questions to ask, red flags to avoid, and what a good agent actually does.",
        "date": "2026-05-05",
        "tags": ["pet transport agent", "IPATA", "choosing an agent", "practical guide"],
        "faqs": [
            ("What is IPATA and why does it matter?", "IPATA (International Pet and Animal Transportation Association) is the global trade body for pet transport professionals. Members operate to a defined code of conduct and professional standards. Using an IPATA member gives you a verified baseline of professional competence and recourse if something goes wrong."),
            ("How much should a pet transport agent cost?", "Agent fees vary by route complexity. For straightforward moves (UK to USA, within EU), expect USD 500-1,500. For quarantine routes (Australia, New Zealand, Singapore, Japan), expect USD 1,500-3,000+. These fees are usually separate from airline cargo and quarantine facility costs."),
            ("What are red flags when choosing a pet transport agent?", "Red flags include: no IPATA membership, no physical address or verifiable business registration, unwillingness to provide references, very low upfront quotes that later increase significantly, inability to explain the documentation process in plain terms, and pressure to commit quickly without time to consider."),
            ("Do I need an agent for a simple EU pet move?", "For simple moves within the EU or from a neighbouring country, many owners handle documentation themselves. An agent adds most value on quarantine routes, complex multi-leg journeys, and moves involving restricted breeds or unusual documentation requirements."),
        ],
        "body": """The pet transport industry has a mix of highly professional IPATA-accredited operators and less rigorous services. On a route where a documentation error means your pet faces 180 days in Japanese quarantine, the difference matters enormously.

**What a good agent actually does**

A professional pet transport agent coordinates:
- Destination country import rules and documentation requirements (they stay current so you don't have to)
- Health certificate preparation and government endorsement coordination
- Airline cargo booking (including live animal cargo holds, not just excess baggage)
- Quarantine facility booking in destinations that require it
- Transit documentation for routes through third countries
- Practical guidance on crate sizing, travel preparation, and travel day logistics
- Being reachable if something goes wrong at an airport

**IPATA accreditation**

The International Pet and Animal Transportation Association (ipata.org) maintains a member directory. IPATA members agree to a professional code of conduct and are required to maintain knowledge of current regulations. This is your starting point when searching for an agent.

**Questions to ask**

Before committing to an agent:
1. Are you an IPATA member? (Verify on ipata.org)
2. How many moves like mine have you handled in the last 12 months?
3. What documentation will my pet need, and what is the timeline?
4. What exactly is included in your fee, and what are the add-on costs?
5. What happens if there's a documentation problem at the airport?
6. Can you provide references from clients who moved to [my destination]?

**Red flags**

An agent who cannot explain the documentation process clearly, has no verifiable IPATA membership, gives you a significantly lower quote than everyone else, or pressures you to commit without time to research is worth avoiding. Pet documentation errors are expensive and stressful to fix.

**When you might not need an agent**

Simple EU moves, UK to France, USA to Canada, within the EU - these are well-documented routes with straightforward processes. If you're reasonably organised and willing to read government guidance documents carefully, you can handle these yourself. The documentation is manageable. Where agents earn their fee is on quarantine routes and complex multi-leg moves.""",
    },
    {
        "slug": "pet-travel-with-multiple-pets",
        "title": "Moving Internationally with Multiple Pets: Practical Guide for 2026",
        "description": "A guide to moving more than one pet internationally in 2026: documentation for each animal, airline limits, quarantine for multiple pets, and how to manage the logistics.",
        "date": "2026-05-04",
        "tags": ["multiple pets", "pet relocation", "practical guide"],
        "faqs": [
            ("Can two pets travel in the same crate on an international flight?", "IATA standards generally require one adult animal per crate for most species. Some exceptions apply for young siblings of the same litter travelling together, and for small compatible animals. Check the specific airline's policy - most carriers follow IATA standards and require individual crates for adult dogs and cats."),
            ("Is there a limit on how many pets I can import into a country?", "Many countries have limits on the number of pets that can be imported as personal household pets (as opposed to commercial imports). Australia limits 2 per owner per consignment without special permits. Singapore generally limits to 3 dogs or 3 cats. USA has no federal limit but airlines have per-booking limits. Check your specific destination."),
            ("Do all my pets need separate health certificates?", "Yes. Each individual animal needs its own health certificate, regardless of how many pets you're moving. The certificate is specific to the individual animal (microchip, vaccination records, etc.)."),
            ("Can I fly multiple pets on the same booking?", "Airlines have limits on the number of live animals per booking and per aircraft. Some airlines limit one pet per passenger in cabin, and have total live animal limits per flight for cargo. If you're moving multiple pets, book early and confirm the number of live animals accepted per flight with the airline."),
        ],
        "body": """Moving with multiple pets adds layers to an already complex process. The documentation multiplies, airline capacity limits become relevant, and quarantine costs add up quickly.

**Each pet needs its own documentation**

There is no shortcut here. Every animal needs:
- Individual microchip
- Individual vaccination records
- Individual health certificate
- Individual health certificate endorsement

Even two dogs from the same household travelling together need separate paperwork for each animal.

**Airline capacity limits**

Airlines have limits on live animal cargo capacity per flight. For popular routes during peak moving season (summer, school year transitions), these spots book up quickly. If you're moving 3 dogs plus a cat, you may need to confirm with the airline that all four animals can be on the same flight, or you may need to stagger travel dates.

**Quarantine country limits**

Australia limits the number of animals per consignment on personal importation. Two animals is standard, more requires special authorisation from DAFF. The Mickleham quarantine facility in Melbourne has capacity limits and advance booking is essential. Book quarantine spaces for all animals before booking flights.

Singapore limits dog ownership to 1 dog per household in Housing Development Board (HDB) flats (most public housing). If you have more than one dog, confirm your accommodation type allows multiple dogs before planning the move.

**Cost implications**

Quarantine costs per animal. Two dogs in Australian quarantine costs roughly twice one dog. Four pets relocating to Japan with full documentation preparation costs four times one pet in vet fees and certification costs. Budget carefully.

**Staging the move**

Some families with multiple pets choose to move one or two animals first, then the remainder. This can help if quarantine facility capacity is tight, if one animal needs additional documentation time, or to reduce the logistical complexity on travel day. A trusted friend, family member, or pet sitter can care for remaining animals until the second group travels.""",
    },
    {
        "slug": "what-happens-at-destination-airport-with-pet",
        "title": "What Actually Happens When Your Pet Arrives at the Destination Airport",
        "description": "A step-by-step guide to what happens when your pet arrives internationally: government inspection, documentation checks, cargo collection, and what to do if there's a problem.",
        "date": "2026-05-04",
        "tags": ["arrival", "airport", "practical guide", "pet transport"],
        "faqs": [
            ("How long does it take to collect my pet after an international flight?", "Allow 1-3 hours after landing for cargo pets. The animal must clear customs/border inspection and be processed through the cargo facility before you can collect. For quarantine countries, you will not collect your pet at the airport - they go directly to the quarantine facility."),
            ("What inspection does my pet go through at a destination airport?", "A government veterinary official or border inspection post officer checks the health certificate, microchip, and vaccination records against the requirements for that country. They may physically inspect the animal. If all is in order, the animal is cleared. If documentation is missing or incorrect, the animal may be held."),
            ("What should I bring to collect my pet from airport cargo?", "Your government-issued ID (matching the name on the health certificate), the cargo booking reference, copies of all pet documentation (health certificate, microchip record, vaccination history), and ideally your own vehicle (cargo animals can be large and need space)."),
            ("What happens if there's a documentation error at the destination airport?", "Depending on the country, the animal may be held at an airport facility, sent back on the next available flight, or placed in quarantine at your cost pending resolution. This is why documentation accuracy matters. If an error is found pre-departure, address it before the pet travels."),
        ],
        "body": """The flight is done. Your pet has arrived. Here is what actually happens next.

**Cargo arrivals: the process**

Cargo pets do not come out with the passenger baggage. They are processed through the airline's cargo facility at the destination airport - a separate building from the main terminal in most major airports. You'll need to go to the cargo terminal, not the passenger arrivals hall, to collect your pet.

The process at most airports:
1. The aircraft lands and cargo is unloaded
2. Live animals are moved to the cargo facility's live animal holding area
3. A government veterinary official or border inspection post (BIP) officer checks the documentation and inspects the animal
4. If everything is in order, the animal is cleared for release
5. You present your ID and cargo booking reference at the cargo office and collect your pet

This process typically takes 1-3 hours after landing. For very busy airports or if inspectors are busy with multiple arrivals, it can take longer. Do not expect to collect your pet within 30 minutes of landing.

**What the inspector checks**

Microchip: the inspector will scan the microchip and verify it matches the number on the health certificate. If the microchip cannot be read (failed implant, reader incompatibility), this can delay or prevent clearance. It's worth having the microchip scanned at your origin country vet as a final check before travel.

Health certificate: the inspector checks it is in the required format, signed by the right authority, within the validity period, and that the declarations match the requirements for that country. Any discrepancy - even a minor one like a birth date format error - can cause delays.

**Quarantine countries**

For Australia, New Zealand, Singapore, Japan, and other quarantine destinations: you will not collect your pet at the airport. The animal is transferred directly to the approved quarantine facility. You (or your agent) will have booked a space at the facility in advance. You can typically visit your pet during quarantine (facility-specific policies apply).

**If something goes wrong**

If documentation is incorrect or the animal cannot be cleared, the airline and the government authority will contact you (or your agent). Depending on the issue and the country, options may include: holding the animal at an airport facility while documentation is corrected (if possible), sending the animal back to the origin on the next available flight, or placing the animal in quarantine at your cost. This is rare with correct preparation, but it does happen.""",
    },
    {
        "slug": "eu-pet-passport-guide-2026",
        "title": "EU Pet Passport Guide 2026: What It Is, Who Needs One, and How It Works",
        "description": "A complete guide to the EU pet passport in 2026: what it records, which countries accept it, how UK pets are affected post-Brexit, and how to get one for your pet.",
        "date": "2026-05-03",
        "tags": ["EU pet passport", "Europe", "pet travel", "documentation guide"],
        "faqs": [
            ("What is an EU pet passport?", "An EU pet passport is an official travel document for dogs, cats, and ferrets issued by an official veterinarian in an EU or EEA member state. It records the animal's microchip number, rabies vaccination history, and other relevant health information. It is accepted across the EU and EEA without additional documentation."),
            ("Can UK pets still use EU pet passports after Brexit?", "EU pet passports issued before January 1, 2021 to UK-resident pets are no longer accepted for travel from the UK into the EU. UK pets now need an Animal Health Certificate (AHC) for each trip into the EU. However, EU pet passports issued to UK-resident pets remain valid documents for travel within EU countries once the pet has entered the EU (e.g., if the passport was issued while you lived in an EU country and you have not relocated back to the UK)."),
            ("How do I get an EU pet passport for my pet?", "Only official veterinarians (OVs) authorised by EU member states can issue EU pet passports. If you live in an EU country, contact an OV vet in your country to have the passport issued. The vet records the microchip, issues the passport, and enters the first vaccination details."),
            ("Does the EU pet passport expire?", "The passport itself does not expire. However, the vaccinations recorded in it do. A pet passport with an expired rabies vaccination is not valid for travel into or within the EU. Keep vaccinations current and ensure they are recorded in the passport by an OV."),
        ],
        "body": """The EU pet passport is one of the most useful documents in European pet travel. If you live in an EU country and travel within the EU with your pet, the passport is what makes movement between countries seamless. Here's how it works.

**What the EU pet passport is**

An official document issued under EU Regulation 576/2013. It records:
- Owner information
- Animal information (name, species, breed, date of birth, colour, sex)
- Microchip number and implant date
- Rabies vaccination dates and the vaccine product used
- Rabies antibody test results (if applicable)
- Clinical health record
- Anti-parasite treatments (where required)

The passport is issued in a standardised EU format, recognised across all EU and EEA member states.

**Who can issue it**

Only Official Veterinarians (OVs) authorised by the competent authority of an EU member state. Your regular vet may or may not be an OV - you'll need to check. In most EU countries, the local agricultural or veterinary ministry maintains a list of OV-authorised practices.

**Travelling within the EU**

An EU pet passport plus valid rabies vaccination (and the 21-day post-first-vaccination wait for new vaccinations) is all you need to move between EU countries. No additional health certificates, no border inspection post visits for EU-to-EU travel.

**UK pets post-Brexit**

This is the point of most confusion. UK pets travelling from the UK into the EU no longer use EU pet passports - they need an AHC. However:
- UK pets that already had EU pet passports issued before Brexit may still use them if the pet has not returned to the UK, and the pet is travelling within EU countries.
- UK pets that previously had EU passports but have since returned to the UK start again as non-EU animals and need AHCs for EU travel.

If you're moving from the UK to an EU country and plan to stay, once your pet is in an EU country and you are resident there, an EU vet can add a new EU country entry to the animal's record - or a new passport can be issued.

**Non-EU, non-UK arrivals into the EU**

Pets from countries outside the EU (other than the UK) enter the EU with an AHC in the EU format, issued by their origin country's government authority. Once the pet is resident in an EU country, the vet can then issue an EU pet passport for future EU travel.""",
    },
    {
        "slug": "pet-transport-documentation-checklist",
        "title": "International Pet Transport Documentation Checklist: What You Need and When",
        "description": "A practical checklist of all the documents your pet needs for international travel in 2026: what each document is, when to get it, and how long it stays valid.",
        "date": "2026-05-03",
        "tags": ["documentation", "checklist", "pet transport", "practical guide"],
        "faqs": [
            ("What is the most common documentation mistake people make?", "The most common error is getting the health certificate too early (making it expire before the travel date) or leaving it too late (not giving APHA or USDA time to endorse it). The second most common is a microchip implanted after a rabies vaccination, which invalidates the vaccination for many destinations."),
            ("How long is a pet health certificate valid?", "Most international health certificates are valid for 10 days from the date of the veterinary examination. Some destinations (USA, Canada, Australia) accept different formats with different validity periods, but 10 days is the most common window. Plan your vet appointment accordingly."),
            ("Does the microchip have to be in before the rabies vaccination?", "Yes, for most destinations. If the microchip is not implanted before or on the same date as the rabies vaccination, the vaccination is not considered valid for most major destinations (UK into EU, USA, Australia, Japan, Singapore, etc.). This is the most expensive mistake to make."),
            ("What is a government-endorsed health certificate?", "A government-endorsed certificate has been signed by an official government veterinary authority (APHA in the UK, USDA APHIS in the USA, etc.) in addition to the issuing vet. Most major destinations (EU, Australia, Singapore, USA for dogs) require this endorsement. Your vet completes the certificate, then submits it to the government authority for endorsement."),
        ],
        "body": """Documentation for international pet travel is not complicated, but it does require careful timing. The most expensive mistakes are usually timing errors - getting things in the wrong order or leaving things too late.

**The core documents**

1. Microchip record
- What: proof that your pet has an ISO 11784/11785 (15-digit) microchip implanted
- When: before any vaccination, and before travel documentation begins
- Validity: permanent

2. Vaccination records
- What: official records of rabies and other required vaccinations, issued by a vet
- When: microchip first, then vaccination
- Validity: depends on product (annual or 3-year rabies vaccines vary by country)

3. Rabies titre test (if required)
- What: blood test showing rabies antibody level at or above 0.5 IU/ml
- When: at least 30 days after the most recent rabies vaccination, at an EU/destination-approved laboratory
- Validity: once passed, generally permanent unless a booster lapses (rules vary by country)

4. Veterinary health certificate
- What: a vet examination confirming the animal is healthy and fit to travel, with all relevant details
- When: within 10 days of travel (for most destinations)
- Validity: 10 days from vet examination date

5. Government endorsement
- What: an official government veterinary authority countersigning the health certificate
- When: after the vet completes the certificate, before travel. APHA in the UK processes online - often same day or next day.
- Validity: tied to the certificate's validity period

6. Import permit (if required)
- What: advance authorisation from the destination country's government to bring the animal in
- When: weeks to months before travel (varies by country)
- Validity: usually specifies a travel window

7. Quarantine booking confirmation (if required)
- What: written confirmation from an approved quarantine facility at the destination
- When: before booking the airline cargo
- Validity: tied to the booked quarantine dates

**Timing your documentation**

Work backwards from your travel date:
- Health certificate: vet appointment 3-7 days before departure (to allow endorsement time and stay within the 10-day window)
- Tapeworm treatment (dogs only, for EU entry): vet administers 1-5 days before arrival at destination
- Titre test wait: if a 3-month post-titre wait applies, this determines your minimum travel date
- Vaccination course: first vaccination + 21-day wait + (if titre test needed) 30-day wait for titre test

The microchip is the first step. Everything else follows.""",
    },
    {
        "slug": "relocating-a-cat-internationally",
        "title": "Relocating a Cat Internationally: A Practical Guide for 2026",
        "description": "A practical guide to moving your cat internationally in 2026: documentation, crate training, cat-specific airline considerations, quarantine cats, and settling in at the destination.",
        "date": "2026-05-02",
        "tags": ["cats", "cat relocation", "international pet travel", "practical guide"],
        "faqs": [
            ("Can cats travel in the cabin on international flights?", "On some airlines and routes, cats can travel in the cabin in an approved soft carrier. Typical requirements: carrier fits under the seat in front (usually 45-55cm x 35cm x 20-25cm), cat plus carrier weighs under 8-10kg (varies by airline). Many international routes do not permit cabin pets regardless of size - confirm with your specific airline and route."),
            ("Do cats need a titre test for quarantine countries?", "Yes. Cats moving to Australia, New Zealand, Singapore, and Japan require the same titre test preparation as dogs, even though they're typically less expensive to transport. The documentation timeline (microchip, rabies vaccinations, titre test, waiting period) applies to cats just as it does to dogs."),
            ("Are cats banned from any countries?", "Cats face very few country-level breed bans compared to dogs. Some countries restrict wild-type hybrids (Savannah cats, Bengal cats in certain generations, etc.). Check the specific regulations for hybrid breeds at your destination."),
            ("How do I stop my cat from spraying or vocalising during transport?", "Confine the cat to the carrier for brief periods before travel to reduce novelty stress. Feliway spray (synthetic feline pheromone) in the carrier has a calming effect for some cats. Avoid feeding 4 hours before travel. Keep the carrier covered during the journey. Sedation is generally not recommended - consult your vet about calming options specific to your cat."),
        ],
        "body": """Cats are adaptable travellers, but they also have specific anxieties that make the process slightly different from moving a dog. Here's what you need to know.

**In-cabin vs cargo**

Cats are more likely than dogs to qualify for cabin travel on international flights, simply because they're smaller. Many cats and their carriers fall within the 7-8kg combined limit that most airlines use for in-cabin pets. If your cat is eligible for cabin travel on your route, this is usually preferable to cargo - less noise, less temperature variation, and less isolation.

However, not all routes allow cabin pets, and not all airlines have the same policies. Confirm with your specific airline, your specific route, and your specific booking class. Some airlines only allow cabin pets in economy, not business or premium economy.

**Crate training for cats**

Cats that have never been in a carrier will find travel far more stressful than cats that are comfortable in one. Introduce the carrier weeks before travel. Leave it out in a familiar room with bedding inside. Feed the cat near the carrier and then inside it. Most cats will voluntarily enter and rest in a carrier they associate with comfort.

**Documentation**

Cats need the same documentation as dogs for most destinations (microchip, vaccination records, health certificate, government endorsement), with a few exceptions:
- Tapeworm treatment (1-5 days before EU entry) applies to dogs only - not cats
- Some countries' health certificates have cat-specific formats vs dog-specific formats - check which your vet uses

**Quarantine countries**

Cats in Australia, New Zealand, Singapore, and Japan face the same quarantine processes as dogs. The documentation timeline is identical. In Australia, cats and dogs use the same quarantine facility (Mickleham). In Singapore, separate approved quarantine facilities handle cats.

**Settling in at the destination**

Cats can take several weeks to feel settled in a new home. Set up a single room initially with the familiar carrier, bedding, food, and litter tray. Let the cat explore from this base rather than releasing into an unfamiliar entire house immediately. Gradual expansion of the territory over days or weeks reduces stress.""",
    },
]

def write_article(article):
    filepath = os.path.join(BLOG_DIR, article["slug"] + ".md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {article['slug']}")
        return

    tags_yaml = "\n".join(f'  - "{t}"' for t in article["tags"])
    faqs_yaml = "\n".join(
        f'  - question: "{q.replace(chr(34), chr(92)+chr(34))}"\n    answer: "{a.replace(chr(34), chr(92)+chr(34))}"'
        for q, a in article["faqs"]
    )

    front_matter = f"""---
title: "{article['title']}"
description: "{article['description']}"
date: "{article['date']}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{article['slug']}"
url: "/blog/{article['slug']}/"
seo:
  title: "{article['title']} | PetTransportGlobal"
  description: "{article['description']}"
tags:
{tags_yaml}
faqs:
{faqs_yaml}
---

{article['body'].strip()}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter)
    print(f"WROTE: {article['slug']}")


for article in ARTICLES:
    write_article(article)

print(f"\nDone. {len(ARTICLES)} articles processed.")
