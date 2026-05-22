"""
Phase 6 Task 6.3 -- Blog batch 9 (25 articles, total target: 201)
Covers: Denmark/Norway/Sweden/Qatar/Sri Lanka/Egypt/Nigeria/Romania/Bahrain country guides;
SG-AU/UK-India/UK-Thailand/CA-AU/France-UK/HK-UK route guides;
Pug/Cocker Spaniel/Maine Coon/Chihuahua breed guides;
DIY-vs-agent/health cert contents/EU-to-USA/cold weather/NZ-AU/airport cargo guide practical articles.
Skip-if-exists on all files.
"""
import os

BLOG_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    # -------------------------------------------------------------------------
    # COUNTRY IMPORT GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "denmark-pet-import-guide",
        "title": "Bringing a Pet to Denmark: EU Rules, Breed Bans and Border Controls",
        "description": "Complete guide to bringing your dog or cat to Denmark in 2026: EU pet passport, microchip, rabies vaccine, breed bans, and what to expect at Copenhagen Airport.",
        "date": "2026-05-06",
        "tags": ["Denmark", "pet import", "EU"],
        "faqs": [
            ("What does my pet need to enter Denmark?", "Pets entering Denmark from other EU countries need a valid EU pet passport, ISO microchip, and current rabies vaccination. Pets from outside the EU also need a rabies antibody titre test showing at least 0.5 IU/ml, carried out at least three months before travel."),
            ("Does Denmark have breed-specific legislation?", "Yes. Denmark bans 13 dog breeds including American Pit Bull Terrier, Tosa, Dogo Argentino, Fila Brasileiro, and American Staffordshire Terrier. These breeds cannot be imported or kept in Denmark. Check the full list with the Danish Veterinary and Food Administration before travel."),
            ("Is there quarantine for pets arriving in Denmark?", "No quarantine for pets arriving from EU or listed countries with correct documentation. Pets from unlisted countries that cannot demonstrate a valid titre test result may face compulsory quarantine or be refused entry."),
            ("What authority oversees pet imports to Denmark?", "The Danish Veterinary and Food Administration (Foedevarestyrelsen) oversees live animal imports. Regulatory information is available at foedevarestyrelsen.dk."),
        ],
        "body": """Denmark is an EU member state and applies the standard EU pet travel rules. Import requirements are enforced by the Danish Veterinary and Food Administration (DVFA), and Denmark is part of the TRACES NT notification system for live animal movements.

**From EU countries**

Dogs and cats travelling from another EU member state need an EU pet passport, ISO 11784/11785 microchip, and a valid rabies vaccination given after the microchip. The EU pet passport is issued by a licensed vet in the origin country.

**From outside the EU**

Pets arriving from outside the EU (including post-Brexit UK) need: ISO microchip, rabies vaccination after microchip, a rabies antibody titre test (RNATT) showing at least 0.5 IU/ml from an EU-approved laboratory, and a wait of three months after the titre test blood sample before travel. UK pets also need an official animal health certificate (AHC) issued and endorsed by a UK Official Veterinarian and APHA. The certificate is valid for 10 days after the vet exam date.

**Breed bans**

Denmark maintains one of Europe's more restrictive breed-specific legislation lists. The following 13 breeds are banned: American Pit Bull Terrier, Tosa, Dogo Argentino, Fila Brasileiro, American Staffordshire Terrier (Amstaff), Boerboel, Kangal, Central Asian Ovtcharka, Caucasian Ovtcharka, South Russian Ovtcharka, Tornjak, Sarplaninac, and mixed breeds of the above. The ban applies to import as well as ownership. If your dog is a mixed breed with any banned ancestry, it may still be refused. Check with the DVFA before committing to travel.

**Arriving at Copenhagen**

Most international pet imports arrive through Copenhagen Airport (CPH). Veterinary inspection takes place at the border post. Keep documentation accessible and do not check it into hold luggage.

**Useful links**

- Danish Veterinary and Food Administration: foedevarestyrelsen.dk
- TRACES NT: traces.ec.europa.eu""",
    },
    {
        "slug": "norway-pet-import-guide",
        "title": "Bringing a Pet to Norway: EEA Rules, Tapeworm Treatment and What to Expect",
        "description": "Full guide to bringing your dog or cat to Norway in 2026: EEA pet passport, titre test, tapeworm treatment for dogs, and Norwegian Food Safety Authority requirements.",
        "date": "2026-05-06",
        "tags": ["Norway", "pet import", "EEA"],
        "faqs": [
            ("Does Norway follow EU pet travel rules?", "Norway is an EEA member and applies the same pet travel rules as EU countries. Dogs and cats need an EU or EEA-equivalent pet passport, ISO microchip, and current rabies vaccination. From outside the EU/EEA, a rabies titre test and three-month wait are required."),
            ("Do dogs entering Norway need tapeworm treatment?", "Yes. Dogs arriving in Norway from countries outside the Nordic region (Denmark, Finland, Iceland, Sweden) must be treated against Echinococcus multilocularis tapeworm. The treatment must be given by a vet between 1 and 5 days before arrival. A record of the treatment must be in the pet passport or health certificate."),
            ("Is there quarantine for pets entering Norway?", "There is no quarantine for pets from EU/EEA or listed countries with complete documentation. Pets from unlisted countries require prior notification and may face quarantine."),
            ("What authority handles pet imports to Norway?", "The Norwegian Food Safety Authority (Mattilsynet) oversees pet imports. Their website at mattilsynet.no has import requirements by country of origin."),
        ],
        "body": """Norway is not an EU member but is a full member of the European Economic Area (EEA) and applies the EU pet travel rules. The Norwegian Food Safety Authority (Mattilsynet) is the competent authority for live animal imports.

**From EU/EEA countries**

Dogs and cats from EU or EEA countries need an EU pet passport, ISO microchip, and current rabies vaccination. Dogs must also be treated against Echinococcus multilocularis tapeworm, unless travelling from Denmark, Finland, Iceland, or Sweden. The treatment (praziquantel-based) must be given by a vet 1 to 5 days before arrival and documented in the pet passport.

**From outside the EU/EEA**

Pets from non-listed countries need: ISO microchip, rabies vaccination (after microchip), a rabies antibody titre test at an EU-approved lab showing at least 0.5 IU/ml, and a three-month wait after the blood sample. They also need an official health certificate in the EU AHC format, endorsed by the government veterinary authority in the origin country.

UK-origin pets (post-Brexit) follow the third-country pathway: microchip, rabies vaccine, titre test with 3-month wait, APHA-endorsed health certificate, and tapeworm treatment for dogs.

**Tapeworm treatment**

This is a strict requirement for dogs from most origin countries. Praziquantel at a minimum dose of 5mg/kg must be administered. The vet records the treatment in the health certificate. Norway checks this consistently at the border, so do not omit it.

**Breed bans**

Norway has breed-specific legislation banning the American Pit Bull Terrier and four other breeds. Check the current list with Mattilsynet before travel if you have a large or guardian-type breed.

**Practical note**

Norway has long winters. Airlines serving Oslo (OSL) may apply cold-weather embargoes for live animal cargo from November to March. Confirm with your carrier before booking a winter journey.""",
    },
    {
        "slug": "sweden-pet-import-guide",
        "title": "Bringing a Pet to Sweden: EU Import Rules, Tapeworm and Jordbruksverket Requirements",
        "description": "Complete guide to bringing your dog or cat to Sweden in 2026: EU pet passport, titre test, tapeworm treatment, and Swedish Board of Agriculture requirements.",
        "date": "2026-05-06",
        "tags": ["Sweden", "pet import", "EU"],
        "faqs": [
            ("What does my pet need to enter Sweden?", "Pets from EU countries need an EU pet passport, ISO microchip, and rabies vaccination. Pets from outside the EU, including the UK, need these plus a rabies antibody titre test showing at least 0.5 IU/ml and a three-month wait after the blood draw."),
            ("Do dogs need tapeworm treatment to enter Sweden?", "Yes. Dogs entering Sweden from any country outside the Nordic area must be treated against Echinococcus tapeworm within 1 to 5 days before entry. The treatment (praziquantel) must be administered by a vet and documented in the health certificate or pet passport."),
            ("Does Sweden have breed-specific legislation?", "No. Sweden does not have national breed-specific legislation and does not maintain a banned breeds list, which makes it more permissive than some EU neighbours for certain dog types."),
            ("What authority oversees pet imports to Sweden?", "The Swedish Board of Agriculture (Jordbruksverket) manages pet import rules. Current requirements are at jordbruksverket.se."),
        ],
        "body": """Sweden is an EU member state and applies the standard EU framework for pet travel. The Swedish Board of Agriculture (Jordbruksverket) is the competent authority, and Sweden participates in the TRACES NT notification system.

**From EU countries**

Dogs and cats from EU member states need an EU pet passport, ISO microchip, and current rabies vaccination. Dogs must also be treated for Echinococcus multilocularis tapeworm unless travelling from another Nordic country (Norway, Finland, Denmark, Iceland). Treatment is praziquantel-based, given by a vet 1 to 5 days before travel.

**From outside the EU**

Pets from non-EU countries (including post-Brexit UK) need: ISO microchip, rabies vaccination post-microchip, a rabies antibody titre test (at least 0.5 IU/ml from an approved lab), and a minimum wait of three months after the titre test blood draw. A health certificate in the EU AHC format, endorsed by the government authority in the origin country, is also required.

**Tapeworm treatment**

Like Norway and Finland, Sweden requires documented tapeworm treatment for dogs arriving from most countries. This is checked at the border and cannot be omitted. Make sure your vet records the praziquantel dose and date in the health certificate.

**No breed ban**

Sweden has no national breed ban, which is notable among EU countries. Your dog's breed alone will not prevent entry to Sweden.

**Arriving at Stockholm**

Most international pet shipments arrive at Stockholm Arlanda (ARN). Veterinary inspection takes place at the designated border inspection post. Keep health documents in the cabin or easily accessible -- do not pack them in checked luggage.

**Cats and other pets**

Cats follow the same rules as dogs (minus tapeworm treatment). Other pets (rabbits, birds, reptiles) have separate import rules through Jordbruksverket. This guide covers only dogs and cats.""",
    },
    {
        "slug": "qatar-pet-import-guide",
        "title": "Bringing a Pet to Qatar: Ministry of Environment Rules, Import Permits and What to Expect",
        "description": "Full guide to bringing your dog or cat to Qatar in 2026: MECC import permit, approved breeds, health certificate, and arrival process at Hamad International Airport.",
        "date": "2026-05-06",
        "tags": ["Qatar", "pet import", "Middle East"],
        "faqs": [
            ("Does Qatar allow dogs and cats as pets?", "Yes, Qatar permits dogs and cats as pets. However, Qatar has a list of restricted and banned dog breeds that may not be imported. An import permit from the Ministry of Environment and Climate Change (MECC) is required before the animal travels."),
            ("What documentation does my pet need to enter Qatar?", "Pets entering Qatar need: an import permit from the MECC, a microchip (ISO 15digit), a valid rabies vaccination, a health certificate issued by an official vet in the origin country and endorsed by the government authority, and sometimes additional tests depending on the origin country."),
            ("Which dog breeds are banned in Qatar?", "Qatar maintains a list of restricted breeds that are either banned outright or require additional approval. The list includes fighting-type and large guard breeds. Check the current approved breed list with the MECC before applying for your import permit."),
            ("Is there quarantine for pets entering Qatar?", "There is no mandatory quarantine for pets with correct documentation entering Qatar. However, veterinary inspection at Hamad International Airport is thorough, and incomplete documentation can result in temporary holding."),
        ],
        "body": """Qatar has become a significant expat destination, and thousands of families relocate there each year with pets. The Ministry of Environment and Climate Change (MECC) oversees live animal imports, and the process requires an import permit obtained before travel.

**Import permit**

Before your pet travels, you must obtain an import permit from the MECC. The permit application includes details of the animal (species, breed, microchip number, vaccination history) and the owner. Processing takes approximately 5 to 10 business days. Start this process at least 4 to 6 weeks before your intended travel date to allow time for any queries.

**Microchip**

An ISO 11784/11785 compatible 15-digit microchip is required. If your pet has a 10-digit chip, a compatible reader may not read it in Qatar -- consider having a 15-digit chip implanted by a vet before travel.

**Rabies vaccination**

A current rabies vaccination is required. The vaccine must be administered after the microchip and must be valid at the time of travel. Keep the vaccination certificate with batch number and product name.

**Health certificate**

An official health certificate issued by a licensed veterinarian in the origin country and endorsed by the government veterinary authority (e.g., APHA in the UK, USDA APHIS in the USA) is required. The certificate must confirm: microchip status, vaccination history, absence of ectoparasites, and the animal's fitness to travel.

**Breed restrictions**

Qatar restricts or bans import of certain dog breeds. The list typically includes fighting breeds and large powerful dogs perceived as a public safety risk. Check the current list directly with the MECC before applying for your permit. Mixed breeds that visually resemble a restricted breed may also be subject to assessment.

**Arriving at Hamad International**

Hamad International Airport (DOH) has a dedicated live animal facility operated by Qatar Airways Cargo. Pets as manifest cargo are handled separately from cabin pets. Veterinary officials inspect documentation at arrival. Keep all documents accessible.

**Working with an agent**

Given the complexity of Qatar's permit system and the breed restriction nuances, using an IPATA-accredited agent with Gulf region experience is strongly recommended for first-time importers.""",
    },
    {
        "slug": "sri-lanka-pet-import-guide",
        "title": "Bringing a Pet to Sri Lanka: Quarantine Rules, Import Permits and What to Know",
        "description": "Complete guide to bringing your dog or cat to Sri Lanka in 2026: mandatory quarantine, import permit from DAPH, titre test requirements, and Colombo airport process.",
        "date": "2026-05-06",
        "tags": ["Sri Lanka", "pet import", "quarantine"],
        "faqs": [
            ("Is there quarantine for pets entering Sri Lanka?", "Yes. All dogs and cats entering Sri Lanka must undergo a period of quarantine at the government quarantine facility. The standard period is 14 days, though it can vary based on origin country and documentation. Quarantine facilities are government-operated."),
            ("What permits are required to bring a pet to Sri Lanka?", "An import permit from the Department of Animal Production and Health (DAPH) is required before travel. The application requires details of the animal, health records, and proof of ownership. Apply at least 6 to 8 weeks before travel."),
            ("Does Sri Lanka require a rabies titre test?", "Yes. Sri Lanka requires a rabies antibody titre test from an internationally accredited laboratory, with a result of at least 0.5 IU/ml. The blood sample must be taken at least three months before the animal's arrival in Sri Lanka."),
            ("Can I bring a pet to Sri Lanka from the UK?", "Yes, but the process is involved. UK pets need a DAPH import permit, APHA-endorsed health certificate, ISO microchip, rabies vaccination, titre test, and will undergo quarantine on arrival. Use an IPATA agent with Sri Lanka experience."),
        ],
        "body": """Sri Lanka requires careful planning for pet imports. Mandatory quarantine, a government import permit, and titre test requirements mean owners need to start the process at least 4 to 6 months before travel. The Department of Animal Production and Health (DAPH), under the Ministry of Agriculture, is the competent authority.

**Import permit**

An import permit from DAPH is required before your pet departs. The application includes: species, breed, age, sex, microchip number, vaccination history, titre test results, and owner details. Processing can take several weeks. Apply as early as possible, ideally 8 to 10 weeks before travel.

**Microchip**

ISO 11784/11785 microchip required. The chip must be implanted before or on the same day as the first rabies vaccination.

**Rabies vaccination**

Current rabies vaccination is required. The vaccination must be on record in the health certificate with product name, batch number, and expiry.

**Titre test**

Sri Lanka requires a rabies antibody titre test (RNATT) at an internationally accredited laboratory, showing at least 0.5 IU/ml. The blood sample must be drawn at least three months before arrival. Results from OIE-accredited labs are accepted.

**Quarantine**

All pets entering Sri Lanka undergo quarantine at the government facility in Pelawatte, Colombo. The standard period is 14 days. Owners are not usually permitted to visit during quarantine. Quarantine fees are payable on arrival. The facility provides basic care, but many owners arrange for additional comfort items to be delivered (check current rules with DAPH, as this varies).

**Health certificate**

An official health certificate from an accredited vet in the origin country, endorsed by the government veterinary authority, is required. The certificate must have been issued within 10 days of travel.

**Arriving at Colombo**

Pets arrive at Bandaranaike International Airport (CMB). Live animals must be declared on arrival and will be directed to DAPH officials for inspection and quarantine processing.

**Practical advice**

Given the titre test window and quarantine requirements, the minimum total preparation time is around 4 to 5 months. Work with an IPATA agent who has Sri Lanka experience -- the permit process and quarantine booking require local knowledge.""",
    },
    {
        "slug": "egypt-pet-import-guide",
        "title": "Bringing a Pet to Egypt: GOVS Health Certificate and Cairo Airport Process",
        "description": "Guide to bringing your dog or cat to Egypt in 2026: GOVS health certificate, microchip, rabies vaccination, advance notification, and arrival process at Cairo Airport.",
        "date": "2026-05-06",
        "tags": ["Egypt", "pet import", "Africa"],
        "faqs": [
            ("What does my pet need to enter Egypt?", "Dogs and cats entering Egypt need a microchip, current rabies vaccination, a health certificate issued by the origin country's government veterinary authority (e.g., APHA in the UK, USDA in the USA), and advance notification to the importing airport's veterinary authority."),
            ("Is there quarantine for pets entering Egypt?", "Egypt does not operate a standard mandatory quarantine for pets with complete documentation from most countries. However, documentation is inspected carefully at the border and animals may be held briefly if paperwork is incomplete."),
            ("Does Egypt require a rabies titre test?", "Egypt does not currently require a rabies titre test from most origin countries. A valid rabies vaccination on the health certificate is sufficient for most arrivals. Confirm current requirements for your specific origin country with the General Organization for Veterinary Services (GOVS)."),
            ("Which authority handles pet imports to Egypt?", "The General Organization for Veterinary Services (GOVS), under the Ministry of Agriculture and Land Reclamation, oversees live animal imports to Egypt."),
        ],
        "body": """Egypt is a popular expat destination for workers in Cairo, the Gulf-adjacent business sector, and the Suez Canal zone. The pet import process is managed by the General Organization for Veterinary Services (GOVS), and preparation is needed 4 to 8 weeks before travel.

**Health certificate**

The health certificate must be issued by an official vet in the origin country and endorsed by the government veterinary authority. For UK arrivals, APHA endorsement is required. For US arrivals, USDA APHIS endorsement is needed. The certificate must confirm: microchip number, species and breed, age and sex, rabies and other vaccination records, and clinical fitness for travel. The certificate is typically valid for 10 days after the exam date.

**Microchip**

ISO 11784/11785 microchip required. The chip must be implanted before vaccinations for those vaccinations to count.

**Rabies vaccination**

A current rabies vaccination is required and must be within the validity period at time of arrival. Egypt does not generally require a titre test from most Western countries, but confirm this for your specific origin country, as requirements can vary.

**Additional vaccinations**

Egypt typically requires evidence of distemper, parvovirus, and hepatitis (for dogs) and cat flu vaccinations for cats. These should be on the health certificate.

**Advance notification**

Airlines and GOVS vets at Cairo Airport (CAI), Alexandria Borg el Arab (HBE), and other major airports generally expect prior notification when live animals are in transit or arriving. Notify your agent or the cargo facility 24 to 48 hours before arrival.

**Arriving at Cairo Airport**

Live animal facilities at CAI are operated by EgyptAir Cargo and approved handlers. Veterinary officials from GOVS inspect arriving animals. The process is generally manageable with complete paperwork but can be time-consuming.

**Practical note**

Egypt's climate is hot and dry. Summer arrivals (June to September) in Cairo see temperatures above 38C. Confirm with your airline whether heat embargoes apply to your routing before booking cargo space.""",
    },
    {
        "slug": "nigeria-pet-import-guide",
        "title": "Bringing a Pet to Nigeria: Federal Department of Livestock Requirements",
        "description": "Guide to bringing your dog or cat to Nigeria in 2026: import permit, health certificate, vaccination schedule, arrival process at Lagos and Abuja airports.",
        "date": "2026-05-06",
        "tags": ["Nigeria", "pet import", "Africa"],
        "faqs": [
            ("What documents are needed to bring a pet to Nigeria?", "Pets entering Nigeria need: an import permit from the Federal Department of Livestock, a health certificate endorsed by the origin country's government veterinary authority, ISO microchip, rabies vaccination, and other required vaccinations (distemper, parvo, hepatitis for dogs; cat flu for cats). Additional parasite treatments are often required."),
            ("Is there quarantine for pets entering Nigeria?", "Nigeria does not operate a standard quarantine facility. However, documentation is inspected at the border and animals may be held pending clearance. In practice, the process at Lagos and Abuja airports can be lengthy without an experienced local agent."),
            ("Do I need an import permit to bring my pet to Nigeria?", "Yes. An import permit from the Federal Department of Livestock and Animal Services (FDLAS) under the Ministry of Agriculture and Rural Development is required before the animal travels."),
            ("What is the best airport to use when importing a pet to Nigeria?", "Murtala Muhammed International Airport (LOS) in Lagos is the most commonly used and has the most established veterinary inspection process. Nnamdi Azikiwe International Airport (ABV) in Abuja also handles live animal imports."),
        ],
        "body": """Nigeria is home to a significant expat community, particularly in Lagos, Abuja, and Port Harcourt. Bringing a pet to Nigeria requires an import permit, a multi-vaccination schedule, and patience with the arrival process. Working with an IPATA-accredited agent with West Africa experience is strongly recommended.

**Import permit**

An import permit from the Federal Department of Livestock and Animal Services (FDLAS), under the Federal Ministry of Agriculture and Rural Development, is required before travel. Apply through the ministry's veterinary services division. The permit specifies the animal species, breed, number, and valid travel window. Processing can take several weeks -- apply as early as possible.

**Health certificate**

An official health certificate from the origin country's government veterinary authority is required. For UK pets, APHA endorsement is needed. For US pets, USDA APHIS endorsement. The certificate must confirm the microchip number, rabies and other vaccination records, parasite treatments, and clinical fitness.

**Microchip**

ISO 11784/11785 microchip required.

**Vaccinations**

Nigeria requires evidence of the following vaccinations:
- Dogs: rabies, distemper, parvovirus, infectious canine hepatitis, leptospirosis, and bordetella (kennel cough)
- Cats: rabies and cat flu (herpes + calicivirus) vaccine

All vaccinations must be current at time of travel.

**Parasite treatments**

Evidence of internal and external parasite treatment (deworming, tick/flea treatment) is typically required and should be documented on the health certificate.

**Arriving at Lagos**

Murtala Muhammed International Airport (LOS) handles the majority of live animal imports. Nigerian Customs and the Federal Department of Livestock both have a role in clearance. The process can be lengthy -- have all documents organised and an agent who can meet the shipment at the airport.

**Practical note**

Nigeria's bureaucratic processes are complex. Having an IPATA-accredited local agent arrange the clearance at the Nigerian end is not just recommended -- it is practically essential for a smooth arrival.""",
    },
    {
        "slug": "romania-pet-import-guide",
        "title": "Bringing a Pet to Romania: EU Rules, ANSVSA and What to Prepare",
        "description": "Guide to bringing your dog or cat to Romania in 2026: EU pet passport, titre test from outside EU, and ANSVSA border inspection requirements.",
        "date": "2026-05-06",
        "tags": ["Romania", "pet import", "EU"],
        "faqs": [
            ("What does my pet need to enter Romania?", "Pets from EU countries need an EU pet passport, ISO microchip, and current rabies vaccination. Pets from outside the EU, including the UK, need these plus a rabies antibody titre test with at least 0.5 IU/ml and a three-month wait after the blood draw."),
            ("Is there quarantine for pets entering Romania?", "No quarantine for pets from EU or listed countries with complete documentation. Pets from unlisted countries without a valid titre test may be refused or quarantined."),
            ("Does Romania have breed-specific legislation?", "Romania previously had strict breed-specific legislation but this has been reformed. Confirm current rules with ANSVSA, particularly if travelling with a large or guard-type breed."),
            ("What authority manages pet imports in Romania?", "The National Sanitary Veterinary and Food Safety Authority (ANSVSA) oversees pet imports. Information is at ansvsa.ro."),
        ],
        "body": """Romania is an EU member state and applies the standard EU pet travel rules, enforced by the National Sanitary Veterinary and Food Safety Authority (ANSVSA).

**From EU countries**

Dogs and cats from EU countries need an EU pet passport, ISO microchip, and current rabies vaccination. The EU pet passport must show the vaccination date and the vaccinator's stamp. Pets should travel on an approved route -- most international arrivals come through Bucharest Henri Coanda Airport (OTP).

**From outside the EU**

Pets from non-EU countries (including post-Brexit UK) require: ISO microchip, rabies vaccination after microchip, a rabies antibody titre test (RNATT) showing at least 0.5 IU/ml from an EU-approved laboratory, and a three-month wait after the titre test blood sample. An official health certificate in the EU AHC format, endorsed by the origin country's government veterinary authority, is also required.

UK pets need APHA endorsement on the health certificate. The EU AHC is valid for four months from signing or until the date of the rabies vaccination expiry, whichever is earlier, for repeat travel.

**Arriving at Bucharest**

OTP has a border inspection post for live animals. Veterinary officials from ANSVSA will inspect documentation. Keep health certificates and passport accessible at all times.

**Breed considerations**

Romania has historically had concerns about large breeds following public incidents. While national breed-specific legislation has been amended, confirm the current status with ANSVSA or a Romanian-based vet before travelling with a large guarding or fighting-type breed.

**Practical note**

Romanian winters are cold (Bucharest averages minus 3 to minus 5C in January). Airlines may apply cold-weather embargoes for live animal cargo on some routes in winter. Check with your carrier for seasonal restrictions.""",
    },
    {
        "slug": "bahrain-pet-import-guide",
        "title": "Bringing a Pet to Bahrain: Import Permit, Health Certificate and Gulf Rules",
        "description": "Guide to bringing your dog or cat to Bahrain in 2026: import permit from Directorate of Agricultural Affairs, health certificate, microchip, and arrival at Bahrain International Airport.",
        "date": "2026-05-06",
        "tags": ["Bahrain", "pet import", "Middle East"],
        "faqs": [
            ("What documents are needed to bring a pet to Bahrain?", "Pets entering Bahrain need an import permit from the Directorate of Agricultural Affairs, a health certificate endorsed by the origin country's government vet authority, ISO microchip, rabies vaccination, and often additional vaccinations. Apply for the permit 4 to 6 weeks before travel."),
            ("Is there quarantine for pets entering Bahrain?", "Bahrain does not operate mandatory quarantine for pets with complete documentation from most countries. Veterinary inspection takes place at Bahrain International Airport on arrival."),
            ("Does Bahrain restrict certain dog breeds?", "Bahrain restricts certain breeds. Confirm the current list of approved breeds with the Directorate of Agricultural Affairs before applying for your import permit."),
            ("What authority handles pet imports to Bahrain?", "The Directorate of Agricultural Affairs under the Ministry of Works, Municipalities Affairs and Urban Planning manages live animal imports to Bahrain."),
        ],
        "body": """Bahrain is a small island nation with a large expat workforce, and pet imports are well-established. The Directorate of Agricultural Affairs, under the Ministry of Works, Municipalities Affairs and Urban Planning, manages the import process.

**Import permit**

An import permit is required before the animal travels. The application includes: species, breed, microchip number, vaccination records, and owner information. Apply through the Directorate of Agricultural Affairs. Processing typically takes 7 to 14 business days. Start the process 4 to 6 weeks before your travel date.

**Microchip**

ISO 11784/11785 compatible 15-digit microchip required.

**Rabies vaccination**

A current rabies vaccination is required, administered after the microchip. Keep the certificate with product name, batch number, and expiry date.

**Health certificate**

An official health certificate issued by a licensed vet in the origin country and endorsed by the government veterinary authority (APHA for UK, USDA APHIS for USA) is required. The certificate typically needs to confirm: microchip status, species and breed, vaccination history, fitness to travel, and absence of ectoparasites.

**Additional vaccinations**

Bahrain typically requires dogs to be vaccinated against distemper, parvo, hepatitis, and leptospirosis. Cats need cat flu vaccination. Confirm current requirements at the time of application.

**Breed restrictions**

Like other Gulf countries, Bahrain restricts certain dog breeds. Confirm approved breeds with the Directorate before applying for your permit. Some breeds that are common as pets in Europe or North America may be restricted.

**Arriving at Bahrain International Airport**

Bahrain International Airport (BAH) handles live animal imports through its cargo facility. Veterinary officials inspect arriving animals and documentation. The process is generally smooth with a complete permit and health certificate.

**Practical note**

Bahrain's climate is hot and very humid from June to September, with temperatures often exceeding 38C and high humidity. Airlines may restrict live animal cargo during peak summer months. Confirm heat embargoes with your carrier before booking.""",
    },

    # -------------------------------------------------------------------------
    # ROUTE GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "singapore-to-australia-pet-transport-guide",
        "title": "Pet Transport from Singapore to Australia: DAFF Rules and What to Prepare",
        "description": "Complete guide to moving your dog or cat from Singapore to Australia in 2026: DAFF requirements, titre test, pre-export isolation, and 10-day quarantine at AQIS.",
        "date": "2026-05-06",
        "tags": ["Singapore", "Australia", "pet transport"],
        "faqs": [
            ("How long does it take to move a pet from Singapore to Australia?", "The process typically takes 6 to 8 months from start to finish. Australia requires a rabies titre test with a three-month wait, pre-export isolation, and a 10-day quarantine on arrival. The total timeline depends on when you start the titre test process."),
            ("Is there quarantine for pets arriving in Australia from Singapore?", "Yes. All dogs and cats entering Australia must complete a 10-day post-arrival quarantine at an approved facility (Mickleham in Victoria or Eastern Creek in New South Wales). Singapore is a listed country, but quarantine is still mandatory."),
            ("What vaccinations does Australia require for pets from Singapore?", "Dogs need rabies vaccination (post-microchip), and a rabies antibody titre test showing at least 0.5 IU/ml. Other required vaccinations include distemper, parvovirus, hepatitis, and leptospirosis. Cats need rabies vaccination and other core vaccines. Full requirements are published by DAFF."),
            ("Which airports accept pet imports into Australia from Singapore?", "Pets from Singapore can arrive into Melbourne (Tullamarine, for Mickleham quarantine) or Sydney (for Eastern Creek quarantine). Most Singapore-Australia pet moves are routed through Singapore Airlines or Qantas via Sydney or Melbourne."),
        ],
        "body": """Moving a pet from Singapore to Australia is one of the more involved routes in Southeast Asia. Australia's biosecurity rules are among the strictest in the world, and even though Singapore is a listed country, the process is rigorous. Allow at least 6 to 8 months for preparation.

**Australia's biosecurity framework**

Australia operates a strict live animal import system managed by the Department of Agriculture, Fisheries and Forestry (DAFF). Singapore is classified as an approved country, which means the full quarantine pathway applies: microchip, vaccinations, titre test, pre-export isolation, and 10-day post-arrival quarantine.

**Step 1: Microchip**

ISO 11784/11785 microchip must be fitted by an accredited vet in Singapore. This must be done before rabies vaccination.

**Step 2: Vaccinations**

Core vaccinations required: rabies (after microchip), distemper, parvovirus, hepatitis, leptospirosis for dogs. Cats need rabies and core cat vaccines. All vaccinations must be current at time of export.

**Step 3: Rabies titre test**

A rabies antibody blood test must be taken at an AFCD-approved or DAFF-recognised laboratory, showing at least 0.5 IU/ml. The blood sample must be drawn at least three months before the animal's arrival in Australia. A recognised Singapore laboratory for this test is the Agri-Food and Veterinary Authority laboratory (now under SFA).

**Step 4: Pre-export isolation**

Pets must be isolated in an approved facility or under controlled conditions before export. Duration depends on the quarantine category. The Australian import permit specifies the isolation requirements for Singapore-origin pets.

**Step 5: Australian import permit**

An import permit from DAFF is required. Apply through the Biosecurity Import Conditions (BICON) database at agriculture.gov.au. Processing typically takes several weeks.

**Step 6: Quarantine on arrival**

10 days at the Australian Government quarantine facility in Mickleham (VIC) or Eastern Creek (NSW). Owners cannot visit during quarantine. Fees are charged to the owner and must be paid in advance.

**Airlines serving this route**

Singapore Airlines (SQ) and Qantas (QF) both carry pets as manifest cargo on this route. Both require IATA-compliant crates and advance booking. Singapore Airlines has a good live animal record on this corridor.

**Using an agent**

Given the complexity, an IPATA-accredited agent with Australian quarantine experience is strongly recommended. Agents manage the BICON permit, coordinate the quarantine booking, and arrange crate-to-facility handover.""",
    },
    {
        "slug": "uk-to-india-pet-transport-guide",
        "title": "Pet Transport from UK to India: DADF NOC, Health Certificate and What to Expect",
        "description": "Complete guide to moving your dog or cat from the UK to India in 2026: DADF import NOC, APHA health certificate, arrival cities, and practical tips for the UK-India route.",
        "date": "2026-05-06",
        "tags": ["UK", "India", "pet transport"],
        "faqs": [
            ("What does my pet need to travel from the UK to India?", "Pets travelling from the UK to India need: an NOC (No Objection Certificate) from India's Department of Animal Husbandry, Dairying and Fisheries (DADF), an APHA-endorsed health certificate, ISO microchip, rabies vaccination, and a health check from an Official Veterinarian within 10 days of travel."),
            ("Is there quarantine for pets entering India from the UK?", "India does not operate mandatory quarantine for pets with complete documentation from the UK. A veterinary inspection takes place on arrival at the designated border inspection post. Some owners report brief holding periods for documentation review, but this is not formal quarantine."),
            ("Which Indian cities accept international pet imports?", "Mumbai (BOM), Delhi (DEL), Bangalore (BLR), Chennai (MAA), and Kolkata (CCU) are the main airports with established live animal import facilities. Delhi and Mumbai have the most experienced veterinary inspection teams for international pet arrivals."),
            ("How long before travel should I apply for the India DADF NOC?", "Apply for the DADF NOC at least 6 to 8 weeks before travel. The application requires proof of microchip, current vaccination records, and owner details. Processing times can vary, particularly during government holidays in India."),
        ],
        "body": """Moving a pet from the UK to India requires a government-to-government paperwork chain and careful timing. With preparation, the journey is manageable, but the DADF NOC and APHA endorsement process means you need to start 8 to 10 weeks before travel.

**Step 1: India DADF NOC**

The No Objection Certificate from India's Department of Animal Husbandry, Dairying and Fisheries (DADF) must be obtained before the animal travels. The application requires: species, breed, sex, approximate age, microchip number, and vaccination history. Apply online through the DADF portal or through an IPATA agent with India experience. Processing typically takes 2 to 4 weeks but can be longer during peak periods.

**Step 2: APHA-endorsed health certificate**

A UK Official Veterinarian must issue the health certificate and APHA must endorse it. The certificate must confirm: ISO microchip number, rabies vaccination (product, batch, date, expiry), other core vaccinations, fitness to travel, and absence of infectious disease signs. The health certificate must be issued within 10 days of travel.

**Microchip**

ISO 11784/11785 microchip required. The chip must be readable before the NOC and health certificate process begins.

**Vaccinations**

Rabies is the primary required vaccination. Also recommended (and often checked): distemper, parvo, hepatitis for dogs; cat flu for cats.

**Airlines on the UK-India route**

British Airways (BA), Virgin Atlantic (VS), Air India (AI), Vistara (formerly), and IndiGo operate this route, though not all accept pets as cargo in all configurations. British Airways and Air India both handle pet cargo on this corridor. Check current pet policies at time of booking, as policies change.

**Arriving at Delhi or Mumbai**

Delhi (DEL) and Mumbai (BOM) both have veterinary inspection facilities. Have the DADF NOC, APHA-endorsed certificate, and microchip verification accessible on arrival. The customs and veterinary clearance process can take 2 to 4 hours at busy airports.

**Working with an agent**

The combination of DADF NOC, APHA process, and airport clearance in India makes this route complex. An IPATA agent with UK-India experience can manage both ends of the process and significantly reduce the risk of documentation errors.""",
    },
    {
        "slug": "uk-to-thailand-pet-transport-guide",
        "title": "Pet Transport from UK to Thailand: DLD Import Rules and Bangkok Arrival",
        "description": "Complete guide to moving your dog or cat from the UK to Thailand in 2026: Department of Livestock Development import permit, APHA health certificate, and Suvarnabhumi Airport process.",
        "date": "2026-05-06",
        "tags": ["UK", "Thailand", "pet transport"],
        "faqs": [
            ("What does my pet need to travel from the UK to Thailand?", "Pets travelling from the UK to Thailand need an import permit from Thailand's Department of Livestock Development (DLD), an APHA-endorsed health certificate, ISO microchip, rabies vaccination, and sometimes a titre test depending on import category. Apply for the DLD permit 4 to 6 weeks in advance."),
            ("Is there quarantine for pets entering Thailand from the UK?", "Thailand does not operate mandatory quarantine for pets with complete documentation from most approved countries including the UK. Veterinary inspection takes place at Suvarnabhumi Airport's livestock inspection station. Incomplete documentation can result in brief holding."),
            ("Does Thailand require a rabies titre test for UK pets?", "Thailand's DLD may require a rabies antibody titre test depending on the category under which the import is classified. For personal pet imports from the UK, confirm current titre test requirements with the DLD or an IPATA agent, as the requirement can change."),
            ("Which authority handles pet imports in Thailand?", "The Department of Livestock Development (DLD), under the Ministry of Agriculture and Cooperatives, manages live animal imports to Thailand."),
        ],
        "body": """Thailand is a popular destination for expats and long-term residents, and the pet import process, while bureaucratic, is well-established. The Department of Livestock Development (DLD) manages live animal imports, and having the correct permit before travel is essential.

**DLD import permit**

Before your pet travels, you must obtain an import permit from the DLD. Apply online through the DLD's e-services portal or through a licensed Thai importer (often arranged by your IPATA agent). The application requires: species, breed, microchip number, vaccination history, and owner details. Permits are typically granted within 2 to 3 weeks.

**APHA-endorsed health certificate**

A UK Official Veterinarian must issue the health certificate and APHA must endorse it. The certificate must be issued within 10 days of travel and confirm: microchip number, vaccination history (rabies with product and batch number), fitness to travel, and absence of ectoparasites.

**Microchip**

ISO 11784/11785 microchip required.

**Rabies vaccination**

A current rabies vaccination is required. Some import categories also require a titre test -- confirm with the DLD for your specific situation.

**Additional vaccinations**

Thailand often requires core vaccinations beyond rabies: for dogs, distemper, parvovirus, hepatitis, leptospirosis; for cats, cat flu and feline enteritis. Document all of these on the health certificate.

**Airlines on the UK-Thailand route**

Thai Airways (TG), British Airways (BA), Emirates (EK), Qatar Airways (QR), and Finnair (AY) operate this route. Check current live animal cargo policies before booking, as not all carriers accept pets on all configurations.

**Arriving at Suvarnabhumi**

Suvarnabhumi Airport (BKK) has a livestock inspection station (operated by DLD officials) at the cargo facility. Pets arriving as manifest cargo are inspected on arrival. The process typically takes 1 to 3 hours with complete documentation. Ensure all docs (DLD permit, health cert, microchip record) travel with the pet or are emailed to your receiving agent in Bangkok.

**Practical note**

Bangkok is hot year-round (average 28 to 35C). Air cargo embargoes for live animals during peak summer months can affect routing. Confirm seasonal availability with your airline before booking.""",
    },
    {
        "slug": "canada-to-australia-pet-transport-guide",
        "title": "Pet Transport from Canada to Australia: DAFF Requirements and Full Timeline",
        "description": "Full guide to moving your dog or cat from Canada to Australia in 2026: DAFF import permit, titre test, CFIA health certificate, quarantine booking, and 10-day post-arrival process.",
        "date": "2026-05-06",
        "tags": ["Canada", "Australia", "pet transport"],
        "faqs": [
            ("How long does it take to move a pet from Canada to Australia?", "The full process typically takes 6 to 9 months. Australia requires a rabies titre test with a three-month wait, pre-export isolation, and a 10-day post-arrival quarantine. Start the titre test at least 6 months before your travel date."),
            ("Which laboratory should I use for the Australia titre test from Canada?", "DAFF maintains a list of approved laboratories. In North America, the Kansas State University Rabies Laboratory (KSVDL) is the most commonly used. Check the current DAFF BICON requirements for approved labs at the time of your application."),
            ("What is the quarantine process for pets arriving in Australia from Canada?", "All pets from Canada must spend 10 days at the Australian Government quarantine facility -- Mickleham (VIC) or Eastern Creek (NSW). Owners cannot visit during the 10-day period. Fees must be paid in advance and a confirmed quarantine booking is required before the animal travels."),
            ("Which Canadian authority endorses the health certificate for Australia?", "The Canadian Food Inspection Agency (CFIA) endorses the official health certificate for live animal export to Australia. An accredited Canadian vet must issue the certificate and CFIA endorses it."),
        ],
        "body": """Canada to Australia is a long and complex route for pet transport, primarily because Australia's biosecurity rules are strict and the paperwork chain involves both the Canadian Food Inspection Agency (CFIA) and Australia's DAFF. Allow at least 6 to 9 months for preparation.

**Australia's requirements**

Australia operates one of the world's most stringent live animal import regimes. For Canada-origin pets, the requirements include: ISO microchip, core vaccinations, rabies vaccination, rabies antibody titre test (at least 0.5 IU/ml from a DAFF-approved lab), pre-export isolation, and 10 days post-arrival quarantine.

**Microchip**

ISO 11784/11785 chip required, implanted before rabies vaccination.

**Rabies vaccination**

Current rabies vaccination required. Must be given after microchip for the vaccination to be considered valid for titre test purposes.

**Titre test**

A rabies antibody titre test (RNATT) must be conducted at a DAFF-approved laboratory. In Canada, the Kansas State University Veterinary Diagnostic Lab (KSVDL) in Manhattan, Kansas is the most accessible North American option. The blood sample must be drawn at least three months before arrival in Australia, and the result must show at least 0.5 IU/ml.

**Australian import permit (BICON)**

Apply for the import permit through Australia's BICON database (agriculture.gov.au/biosecurity/bicon). The permit specifies the treatment pathway and confirms the quarantine facility booking. Apply well in advance of travel -- processing takes several weeks.

**Pre-export isolation**

Canada-origin pets must be isolated in an approved facility for a period before export. The duration is specified in the import permit.

**CFIA health certificate**

A CFIA-accredited vet must issue an official health certificate and CFIA must endorse it. The certificate must be issued within 10 days of travel.

**Quarantine on arrival**

10 days at Mickleham (VIC) or Eastern Creek (NSW). Book in advance through the quarantine facility -- space is limited and must be confirmed before the animal's departure. Fees apply.

**Routing**

Canada to Australia routing typically goes via Los Angeles (LAX), Vancouver (YVR), or direct if available. Air Canada and Qantas have code-share arrangements. Confirm live animal cargo acceptance at time of booking.

**Agent recommendation**

This route benefits enormously from IPATA agent support at both the Canadian and Australian end. The title test timeline, BICON permit, and quarantine booking all have strict dependencies and deadlines.""",
    },
    {
        "slug": "france-to-uk-pet-transport-guide",
        "title": "Pet Transport from France to UK: Post-Brexit Rules and What You Need",
        "description": "Complete guide to moving your dog or cat from France to the UK in 2026: APHA health certificate, tapeworm treatment, approved routes, and what post-Brexit rules mean for French-registered pets.",
        "date": "2026-05-06",
        "tags": ["France", "UK", "pet transport", "post-Brexit"],
        "faqs": [
            ("Can I bring my pet from France to the UK after Brexit?", "Yes. Pets can travel from France to the UK after Brexit, but the rules changed in 2021. French pets (or pets registered in the EU) now need an official animal health certificate (AHC) issued by an Official Vet in France, microchip, current rabies vaccination, tapeworm treatment for dogs, and must use an approved route."),
            ("Does my French-registered pet need a titre test to enter the UK?", "No. France is a listed country for UK pet travel, which means a rabies titre test is not required. A valid rabies vaccination and the AHC are sufficient."),
            ("Does my dog need tapeworm treatment to enter the UK from France?", "Yes. Dogs entering the UK from France must be treated against Echinococcus tapeworm (tapeworm treatment using praziquantel). The treatment must be administered by a vet between 24 and 120 hours (1 to 5 days) before arrival. The vet must document it in the health certificate."),
            ("Which routes can I use to bring a pet from France to the UK?", "Approved routes include: ferry services (Eurostar in the car, Dover-Calais ferries operated by DFDS and P&O), and air cargo. Not all ferry routes are PETS-approved. Check the UK Government's list of approved routes at gov.uk/bring-pet-to-great-britain."),
        ],
        "body": """Since Brexit, the UK and EU have separate pet travel regimes. Bringing a pet from France to the UK is possible, but the process now involves more paperwork than when the UK was in the EU. The key requirement is an official animal health certificate (AHC) issued by an official vet in France.

**The UK's requirements for EU pets**

The UK accepts pets from EU-listed countries (which includes France) without a titre test, but requires: ISO microchip, current rabies vaccination, an AHC issued by an Official Vet in France and endorsed by the French veterinary authority (DDPP or DDETSPP), tapeworm treatment for dogs, and travel on an approved route.

**EU pet passport: no longer valid for UK entry**

French-issued EU pet passports are no longer valid for entry to Great Britain (England, Scotland, Wales). You need the official AHC for each journey. Northern Ireland has different rules (it remains under a specific protocol).

**The AHC**

The AHC must be issued by an Official Vet (Veterinaire Sanitaire) in France. The vet will confirm: microchip, rabies vaccination (with date, product, batch, expiry), and fitness to travel. The certificate is valid for 10 days after the vet examination date for entry into the UK, then for onward travel for a further 4 months.

**Tapeworm treatment for dogs**

This is mandatory. Praziquantel at 5mg/kg minimum must be given by a vet between 1 and 5 days before UK arrival. The vet must record the treatment in the health certificate. Missing this step means your dog will be refused entry.

**Approved routes**

You must use a PETS-approved route. Popular options include:
- Eurostar (Le Shuttle car train, not passenger trains) through the Channel Tunnel
- DFDS ferry (Dunkirk/Calais to Dover)
- P&O ferry (Calais to Dover)

Notify the ferry or Eurostar operator in advance that you are travelling with a pet.

**Cats and ferrets**

Cats follow the same rules as dogs (minus tapeworm treatment). Ferrets can also travel but have specific additional requirements.

**What changed since Brexit**

Before 2021, French pets with an EU passport could enter the UK without the AHC. Now every journey requires a fresh AHC and tapeworm treatment for dogs. Plan for a vet appointment 24 to 120 hours before each cross-Channel trip.""",
    },
    {
        "slug": "hong-kong-to-uk-pet-transport-guide",
        "title": "Pet Transport from Hong Kong to UK: APHA Rules and What to Prepare",
        "description": "Full guide to moving your dog or cat from Hong Kong to the UK in 2026: titre test, three-month wait, APHA health certificate, tapeworm treatment, and approved entry routes.",
        "date": "2026-05-06",
        "tags": ["Hong Kong", "UK", "pet transport"],
        "faqs": [
            ("What does my pet need to travel from Hong Kong to the UK?", "Pets from Hong Kong entering the UK need: ISO microchip, rabies vaccination (post-microchip), a rabies antibody titre test showing at least 0.5 IU/ml from an approved laboratory, a three-month wait after the titre test blood draw, an official health certificate endorsed by the Agriculture, Fisheries and Conservation Department (AFCD) in Hong Kong, and tapeworm treatment for dogs."),
            ("How long does it take to prepare a pet to travel from Hong Kong to the UK?", "Preparation typically takes 5 to 7 months from start to finish. The three-month wait after the titre test blood draw is the main timeline driver. If your pet already has an up-to-date titre test result, the timeline shortens considerably."),
            ("Which laboratory should I use for the UK titre test from Hong Kong?", "The UK government requires titre tests from approved laboratories. In Hong Kong, the Agriculture, Fisheries and Conservation Department (AFCD) veterinary laboratory or internationally approved labs are used. Check the current UK DEFRA approved laboratory list before drawing the blood sample."),
            ("Does my dog need tapeworm treatment before entering the UK?", "Yes. Dogs entering the UK from Hong Kong (a non-EU, non-listed country for tapeworm purposes) must be treated against Echinococcus tapeworm between 24 and 120 hours before UK arrival. This must be documented in the health certificate."),
        ],
        "body": """Hong Kong is a listed country for UK pet travel, which means pets can enter the UK without quarantine -- but the titre test and three-month wait still apply. This is one of the most organised routes for pet transport from Asia to Europe.

**UK's requirements for Hong Kong pets**

Hong Kong is on the UK's list of approved countries from which pets can enter without quarantine. However, the full set of requirements still applies: ISO microchip, rabies vaccination, titre test, three-month wait, official health certificate, tapeworm treatment for dogs.

**Microchip**

ISO 11784/11785 microchip must be implanted before the rabies vaccination and titre test.

**Rabies vaccination**

A current rabies vaccination is required. It must be given after the microchip is implanted. The vaccination must remain valid at the time of travel.

**Titre test (RNATT)**

A rabies neutralising antibody titre test must be conducted at an approved laboratory, with a result of at least 0.5 IU/ml. The blood sample must be drawn at least three months before arrival in the UK. AFCD in Hong Kong can advise on approved laboratories. The KABS Neu-Ulm laboratory in Germany and Biobest in Edinburgh (UK) are among the most commonly used for this route.

**The three-month wait**

The clock starts from the date the blood sample is drawn (not the date the result comes back). Results typically come within 7 to 14 days, but the three-month wait is from the blood draw date.

**Official health certificate**

An AHC must be issued by a licensed vet in Hong Kong and endorsed by the AFCD. The certificate must be issued within 10 days of travel and confirm: microchip, vaccination dates, titre test result, and tapeworm treatment for dogs.

**Tapeworm treatment**

Dogs entering the UK must have praziquantel tapeworm treatment documented in the health certificate, administered between 24 and 120 hours before UK arrival.

**Airlines on the Hong Kong-UK route**

Cathay Pacific (CX) and British Airways (BA) both operate direct Hong Kong-London flights. Cathay Pacific has established live animal cargo procedures on this route. Emirates (EK) via Dubai is also used for this corridor.

**Practical note**

Hong Kong has a hot, humid summer (June to September) and airlines may apply heat embargoes for live animal cargo during this period. Schedule travel in spring or autumn for the best conditions.""",
    },

    # -------------------------------------------------------------------------
    # BREED GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "travelling-with-a-pug-internationally",
        "title": "Travelling Internationally with a Pug: Airline Bans, Safety and What to Know",
        "description": "Complete guide to international travel with a Pug in 2026: which airlines ban Pugs, snub-nosed flight risks, cabin vs cargo, and how to plan a safe journey.",
        "date": "2026-05-06",
        "tags": ["Pug", "brachycephalic", "breed guide"],
        "faqs": [
            ("Can Pugs travel on aeroplanes?", "Many airlines ban or severely restrict Pugs in cargo because they are a brachycephalic (flat-faced) breed. Some airlines allow Pugs in the cabin if they fit under the seat in an approved carrier and weigh under the limit (typically 8kg including carrier). Always confirm with your specific airline before booking."),
            ("Which airlines allow Pugs in the cabin?", "Airlines that generally permit Pugs in cabin (subject to weight/size limits) include Lufthansa, Air France, KLM, and some others. Airlines that ban Pugs in cargo include British Airways, Qantas, Air Canada, and many others. Policies change -- always verify directly with the airline at time of booking."),
            ("Is it safe for a Pug to fly in cargo?", "Flying in cargo is higher risk for Pugs than for non-brachycephalic breeds due to their restricted airways. The stress and reduced oxygen at altitude can cause respiratory distress. If cargo is the only option, travel during cooler months, choose direct flights, and get a fitness-to-fly certificate from your vet before travel."),
            ("What should I do before flying with my Pug?", "Get a vet check confirming your Pug is fit to fly. Ask about respiratory health, heat tolerance, and stress response. Choose the coolest time of year for travel, book the shortest possible routing, and have an emergency contact at the destination with a known vet."),
        ],
        "body": """Pugs are one of the most popular dog breeds worldwide, but international travel with a Pug requires careful planning because of their brachycephalic (flat-faced) anatomy. Many airlines restrict or ban Pugs in cargo, and their physiology makes them more vulnerable to heat stress and respiratory difficulty during air travel.

**The brachycephalic problem**

Pugs have shortened skulls, narrowed nostrils, and elongated soft palates. At altitude, in a warmer-than-usual environment or under stress, these features can restrict airflow significantly. Airlines have experienced in-flight deaths with brachycephalic breeds, which is why so many now either ban them outright in cargo or require additional documentation.

**Airlines that ban Pugs in cargo**

British Airways, Qantas, Singapore Airlines, Air Canada, Etihad, Korean Air, and several others do not accept Pugs as checked baggage or manifest cargo. The specific banned breed lists vary -- always check the current list with your carrier.

**Airlines that may accept Pugs in cabin**

Pugs under the weight and size limit (usually 8 to 10kg including carrier) may be accepted in the cabin by: Lufthansa, Air France, KLM, Iberia, TAP Air Portugal, and some others. The key is that the carrier must fit under the seat and the total weight must be within the airline's cabin pet limit. Most Pugs can travel in-cabin as puppies or if they are small and very compact adults.

**Fitness to fly**

Before any international trip, have your vet examine your Pug specifically for travel fitness. A fitness-to-fly certificate is often required by airlines and is good practice regardless. Vet-assessed issues to check: degree of stenotic nares (narrow nostrils), elongated soft palate, tracheal width, and current respiratory health.

**Planning for a safe journey**

- Book the shortest possible routing (fewest connections, shortest total journey time)
- Travel in the coolest part of the year -- summer heat is dangerous for Pugs in cargo
- Avoid travel in very hot destinations if cargo is the only option
- Choose airlines with live animal experience and a good safety record
- Keep the Pug well-hydrated before travel (not overfed -- full stomach increases respiratory effort)
- Attach a comfort item with your scent to the crate

**Countries with breed-specific import restrictions**

Some countries ban or restrict specific dog breeds. Pugs are not typically on these lists, but confirm with the destination country's veterinary authority before travel.

**Realistic assessment**

For many international Pug moves, cabin travel is both safer and more practical. If your Pug is too large for cabin, discuss all options with an IPATA agent before committing to a cargo route. The safety of your Pug must come first.""",
    },
    {
        "slug": "travelling-with-a-cocker-spaniel-internationally",
        "title": "Travelling Internationally with a Cocker Spaniel: Airline Policies and Import Rules",
        "description": "Guide to international travel with a Cocker Spaniel or English Springer Spaniel in 2026: airline cargo options, cabin eligibility, ear care, and country import rules.",
        "date": "2026-05-06",
        "tags": ["Cocker Spaniel", "Spaniel", "breed guide"],
        "faqs": [
            ("Can a Cocker Spaniel travel in the cabin on an aeroplane?", "A Cocker Spaniel may travel in the cabin if the combined weight of dog and carrier is within the airline's cabin pet limit (usually 6 to 10kg depending on the carrier). Most adult Cocker Spaniels (around 9 to 13kg) exceed the limit without carrier, so cabin travel is often only possible for puppies or very small Cockers."),
            ("Is a Cocker Spaniel allowed in cargo on international flights?", "Yes. Cocker Spaniels are not brachycephalic and are not on standard airline breed ban lists. Most international carriers accept Cocker Spaniels as manifest cargo in an IATA-compliant crate, subject to booking and size requirements."),
            ("Do Cocker Spaniels have any breed-specific travel restrictions?", "Cocker Spaniels are not subject to breed-specific bans in most countries. They are not considered a dangerous breed and are not on any standard prohibited import lists. Check the specific destination country's rules."),
            ("What special care does a Cocker Spaniel need for air travel?", "Cocker Spaniels' long floppy ears make them prone to ear infections, which can worsen with changes in humidity during travel. Have a vet check the ears before travel and treat any existing infections. Keep ears clean and dry before departure."),
        ],
        "body": """Cocker Spaniels -- both English and American -- are sociable, adaptable dogs that generally cope well with air travel. They are not on airline breed ban lists, and with proper preparation, international moves with a Cocker Spaniel are straightforward.

**Cabin vs cargo**

Adult Cocker Spaniels typically weigh 9 to 13kg. Most airlines set a cabin pet limit of 6 to 10kg (including carrier). A small, compact adult Cocker Spaniel in a lightweight soft carrier might just make the weight limit on some airlines, but cargo is the more common option for adult dogs of this size. Puppies under 12 weeks and small Cockers may qualify for cabin.

**IATA crate sizing**

For cargo travel, your Cocker Spaniel needs an IATA-compliant hard crate (usually a variation of IATA crate size 300 or 400 depending on the dog's height and length). The dog must be able to stand, turn, and lie down in the crate. Add a few centimetres for bedding. Ask your vet or IPATA agent for the specific crate measurement.

**Ear care before travel**

Cocker Spaniels are prone to ear infections due to their pendulous, hair-covered ear canals. Air travel, with pressure changes and humidity variations, is not ideal for ears that are already irritated. Have a vet check the ears 2 to 3 weeks before travel. Treat any infection before departure -- flying with an active ear infection is uncomfortable for the dog and the infection may worsen in transit.

**Not a restricted breed**

Cocker Spaniels are not on any standard airline breed ban list and are not subject to import breed restrictions in any of the major destination countries. They are generally considered low-risk for airline and government purposes.

**Health certificate**

Like all dogs travelling internationally, your Cocker Spaniel needs an official health certificate endorsed by the government veterinary authority in your origin country. The certificate must confirm the microchip number, vaccination history, and fitness to travel. Timing requirements vary by destination.

**Temperament and crate training**

Cocker Spaniels can be sensitive and velcro-like in their attachment to owners. Crate training several months before travel makes the flight experience significantly less stressful. Build up gradually from short crate sessions to overnight confinement so the crate becomes a safe and familiar space.""",
    },
    {
        "slug": "travelling-with-a-maine-coon-cat-internationally",
        "title": "Travelling Internationally with a Maine Coon: Size, Crates and Import Rules",
        "description": "Guide to international travel with a Maine Coon cat in 2026: IATA crate sizing for large cats, airline cabin limits, microchip and vaccination requirements, and country rules.",
        "date": "2026-05-06",
        "tags": ["Maine Coon", "cat", "breed guide"],
        "faqs": [
            ("Can a Maine Coon travel in the cabin on a plane?", "It depends on the size of your Maine Coon and the airline's weight limit. Maine Coons typically weigh 5 to 9kg as adults. Most cabin cat limits are 6 to 8kg (including carrier). A large Maine Coon may exceed the limit and need to travel as cargo. Many airlines accept cats in-cabin -- check the specific carrier's policy and weigh your cat before booking."),
            ("What size crate does a Maine Coon need for cargo travel?", "Maine Coons are large cats and often need a bigger crate than most breeds. Use the IATA guideline: the crate must allow the cat to stand at full height, turn around completely, and lie stretched out. For a large Maine Coon, an IATA 400 or 500 may be needed. Have your vet measure your cat before buying the crate."),
            ("Do Maine Coons have any breed-specific travel restrictions?", "No. Maine Coons are not on any airline breed ban list or country import restriction list. They are a natural (non-brachycephalic) breed and are generally considered low-risk for air travel."),
            ("Are Maine Coons good travellers?", "Maine Coons are known for being relatively calm and adaptable, which makes them better candidates for travel than some breeds. Individual temperament varies, so crate training well before travel is important. Some Maine Coons travel in the cabin with their owners on long-haul routes with no issues."),
        ],
        "body": """Maine Coons are one of the largest domestic cat breeds, and their size means travel logistics need more planning than with a typical cat. They are not restricted by any airline breed ban or country import rule, but getting the crate sizing right is essential.

**Size and weight considerations**

Adult Maine Coons typically weigh 5 to 9kg (some reach 10 to 12kg). Female Maine Coons are usually at the lower end (5 to 7kg). When it comes to cabin travel, most airlines set a weight limit of 6 to 8kg including the carrier. A soft-sided carrier for an average Maine Coon might just make the cut -- but a larger male may need to go as manifest cargo.

**Airlines that accept cats in cabin**

Many airlines allow cats in the cabin, including: Lufthansa, Air France, KLM, Emirates (on some routes), Turkish Airlines, and others. Some long-haul carriers restrict cabin pets entirely. Check the specific route and carrier policy at time of booking. Weight limits are strictly enforced at check-in.

**IATA crate sizing for cargo**

If your Maine Coon travels as cargo, the crate must meet IATA standards. The interior height must allow the cat to stand at full height without the top of the head touching the roof. The length must allow the cat to lie stretched out. For a large Maine Coon, you may need an IATA 400 or even 500 series crate. Measure your cat (standing height plus 10cm, body length plus half the leg length) and check against IATA sizing charts.

**Temperament for travel**

Maine Coons are generally described as dog-like in temperament -- sociable, curious, and calm. This makes them better candidates for travel than highly anxious breeds. Individual temperament still varies. Crate train your Maine Coon over several months before a long international move. Familiar bedding with the cat's scent in the crate helps significantly.

**Standard import requirements**

Like all cats travelling internationally, a Maine Coon needs: ISO microchip, rabies vaccination, any country-specific requirements (titre test, health certificate, import permit), and IATA-compliant crating. Destination-specific rules apply -- check the destination country guide for details.

**Grooming before travel**

Maine Coons have a thick, semi-longhaired coat. If travelling in cargo during summer, ensure the crate has good ventilation. Avoid heavy grooming products close to travel (scented sprays can be stressful). A professional groom a week before travel is fine.""",
    },
    {
        "slug": "travelling-with-a-chihuahua-internationally",
        "title": "Travelling Internationally with a Chihuahua: Cabin Options, Regulations and Tips",
        "description": "Complete guide to international travel with a Chihuahua in 2026: in-cabin travel options, weight limits, microchip rules, country import requirements, and keeping tiny dogs safe.",
        "date": "2026-05-06",
        "tags": ["Chihuahua", "small dog", "breed guide"],
        "faqs": [
            ("Can a Chihuahua travel in the cabin on an aeroplane?", "Yes. Chihuahuas are small enough to travel in-cabin on most airlines. Adult Chihuahuas typically weigh 1.5 to 3kg, and with a soft carrier they comfortably come in under most airline cabin pet weight limits of 6 to 10kg. Confirm the specific airline's weight limit, carrier dimensions, and in-cabin pet policy before booking."),
            ("Do Chihuahuas have any breed-specific import restrictions?", "No. Chihuahuas are not on any country breed ban list and are not subject to airline breed restrictions. They are one of the most travel-friendly breeds from a regulatory perspective."),
            ("What size carrier should I use for a Chihuahua in the cabin?", "Use a soft-sided carrier that fits under the seat (typically 45cm x 25cm x 28cm, but check your specific airline's under-seat dimensions). The Chihuahua must be able to stand, turn, and lie down in the carrier. For most Chihuahuas, a small or extra-small carrier is appropriate."),
            ("What health considerations should I be aware of for a Chihuahua flying?", "Chihuahuas can be prone to anxiety, dental issues, and hypoglycaemia (low blood sugar). Do not fly a Chihuahua that is unwell, underweight, or very young. Bring a small amount of their regular food in case they need a blood sugar boost. Keep the carrier covered with a light cloth to reduce visual stimulation during the flight."),
        ],
        "body": """Chihuahuas are natural candidates for in-cabin air travel. Their small size means they comfortably fit under the seat in most cabin carriers, and they are not subject to any breed ban or country import restriction. With the right preparation, flying internationally with a Chihuahua is one of the more manageable small dog travel experiences.

**Cabin travel advantages**

At 1.5 to 3kg, a Chihuahua in a soft carrier comes in well under most airlines' 6 to 10kg cabin pet weight limits. Keeping your Chihuahua in the cabin with you means less separation anxiety for both of you and avoids the risks associated with cargo hold travel. This is one of the few breeds where in-cabin travel is the default option on most routes.

**Airlines and cabin pet rules**

Most major international carriers accept small dogs in the cabin, including: Lufthansa, Air France, KLM, Emirates (some routes), Turkish Airlines, TAP Air Portugal, Iberia, and many others. Long-haul US carriers like Delta and United allow cabin pets on domestic routes but have restrictions on international transatlantic flights. British Airways does not allow pets in the cabin on any route. Check the specific carrier's policy at the time of booking.

**Carrier dimensions**

Buy a soft-sided carrier that fits under the seat in front of you. Common dimensions that fit most airline under-seat spaces: approximately 45cm x 25cm x 28cm. Always check your specific airline's stated dimensions -- they vary. The carrier must allow your Chihuahua to stand (not hunched), turn, and lie down. For most Chihuahuas, a small or extra-small carrier works well.

**Standard import documents**

Despite their small size, Chihuahuas need the same documentation as any other dog for international travel: ISO microchip, rabies vaccination, and all destination-country specific requirements (titre test, health certificate, import permit as applicable). See the destination country guide for details.

**Anxiety management**

Chihuahuas are lively and can be anxious. A few weeks of crate training before travel helps enormously. The goal is for the carrier to feel like a den rather than a cage. Put the open carrier in your living room with familiar bedding and let your Chihuahua choose to sleep in it. Gradually close the door for short periods.

**Hypoglycaemia risk**

Very small or young Chihuahuas can experience low blood sugar (hypoglycaemia) if they do not eat for extended periods. On long journeys, bring some of their regular food or a small amount of honey to give if they seem lethargic or wobbly. Have your vet check blood sugar and weight before travel.

**Country-specific considerations**

Most countries welcome Chihuahuas without breed-specific restrictions. A few Gulf countries have restricted breed lists, but Chihuahuas are never on them. Always verify the destination country's requirements through official channels regardless of breed.""",
    },

    # -------------------------------------------------------------------------
    # PRACTICAL GUIDES
    # -------------------------------------------------------------------------
    {
        "slug": "pet-relocation-diy-vs-agent-comparison",
        "title": "DIY Pet Relocation vs Hiring an Agent: Which is Right for You?",
        "description": "Honest comparison of DIY pet relocation versus using a professional IPATA agent in 2026: costs, risks, paperwork complexity, and when each approach makes sense.",
        "date": "2026-05-06",
        "tags": ["pet relocation", "IPATA", "planning"],
        "faqs": [
            ("Is it cheaper to do pet relocation yourself or hire an agent?", "DIY is typically cheaper in direct fees -- you pay the airline and vet directly rather than an agent's coordination fee. However, mistakes in documentation can result in fines, refused entry, or quarantine at your expense, which can easily exceed what an agent would have cost. For complex routes or strict-quarantine countries, an agent usually saves money overall."),
            ("What routes are suitable for DIY pet relocation?", "Straightforward EU-to-EU moves, domestic flights, and routes where documentation requirements are simple (microchip plus EU pet passport) are the most DIY-friendly. Routes involving Australia, New Zealand, Japan, Singapore, Rabies-free island nations, or countries with permit requirements are much harder to self-manage."),
            ("What does an IPATA pet transport agent actually do?", "An IPATA agent handles: documentation preparation, permit applications, health certificate coordination, airline booking, crate procurement, live animal declarations, destination clearance, quarantine booking if required, and in some cases door-to-door collection and delivery. They also troubleshoot problems if documentation is queried at the border."),
            ("How do I find a reputable pet transport agent?", "Use the IPATA agent directory at ipata.org to find accredited members. Look for agents with specific experience on your route -- a specialist in Australia moves will know BICON processes; a Gulf specialist will know the MECC permit system. Ask for references from recent clients."),
        ],
        "body": """One of the first questions pet owners ask when planning an international move is whether to hire an agent or manage the process themselves. The answer depends on the route, the destination country's rules, your comfort with bureaucracy, and how much risk you are prepared to manage.

**The case for DIY**

For simple routes, DIY is perfectly viable. If you are moving within the EU, the paperwork is: EU pet passport, microchip, and rabies vaccine. There is no permit application, no titre test, no quarantine to book. A competent, organised owner can handle this independently with a vet who is familiar with EU pet travel rules.

Similarly, for moves to countries with clear, straightforward rules (and no quarantine), a well-prepared owner with an accredited vet on their side can manage the process. The key resources are: the destination country's government veterinary authority website, APHA (for UK origin), and the IATA regulations for crating.

**The case for an agent**

An agent earns their fee on complex routes. Specifically, you benefit from an agent when:
- The destination has quarantine (Australia, NZ, Japan, Sri Lanka, Hawaii)
- The destination requires a permit (Qatar, India, Nigeria, Thailand)
- The route involves multiple legs with transit country rules
- You have a brachycephalic or large breed and need airline policy expertise
- The timeline has tight dependencies (titre test, 3-month wait, quarantine booking windows)
- It is your first time relocating internationally

An IPATA-accredited agent has experience with the specific permit systems, knows which officials to contact when documentation is queried, and can often solve problems that would strand an unassisted owner.

**Cost comparison**

A professional agent typically charges between 500 and 3,000 GBP/USD for a full-service move, depending on complexity and destination. DIY costs include: vet fees, government endorsement fees, crate purchase, airline cargo charges. On a simple EU move, DIY might save 500 to 1,000 GBP. On an Australia move with quarantine, agent fees are a fraction of the total cost and the risk of a documentation error (which would require repeat quarantine at your expense) is significant.

**Middle ground: partial agent support**

Some agents offer documentation-only services -- they prepare the paperwork and you handle the physical logistics. This can be a cost-effective option for owners who want expert support on the complex part (documents) but are comfortable managing the logistics.""",
    },
    {
        "slug": "pet-health-certificate-what-it-contains",
        "title": "What Is in a Pet Health Certificate? A Plain-Language Breakdown",
        "description": "Plain-language guide to what a pet health certificate contains in 2026: the EU AHC format, what each section means, how to check it is correct, and what to do if there is an error.",
        "date": "2026-05-06",
        "tags": ["health certificate", "documentation", "planning"],
        "faqs": [
            ("What is an official pet health certificate?", "An official animal health certificate is a government-format document issued by an accredited vet and endorsed by the government veterinary authority in the origin country. It certifies the animal's health status, microchip, vaccination history, and fitness to travel. It is required for most international pet movements."),
            ("How long is a pet health certificate valid for?", "The EU AHC is valid for 10 days after the vet examination date for entry into the destination country, then remains valid as a re-entry document for 4 months or until the rabies vaccination expires, whichever is earlier. Other countries have different validity rules -- check with your destination country."),
            ("What happens if there is an error in the health certificate?", "If a material error is found at the border (wrong microchip number, expired vaccination date, incorrect country), the animal may be held pending documentation correction. In the worst case, it may be returned to the origin country. Always check the health certificate carefully before travel."),
            ("Who issues the pet health certificate?", "In the UK, an Official Veterinarian (OV) issues the certificate and APHA endorses it. In the USA, an accredited vet issues and USDA APHIS endorses. In EU countries, a vet with official status (Veterinaire Sanitaire in France, for example) issues it and the regional authority endorses it."),
        ],
        "body": """The official pet health certificate is arguably the most important document in international pet travel. A mistake on it can hold up an entire journey. Understanding what it contains helps you check it for errors before departure.

**What it is**

A pet health certificate is a legal document issued by a licensed vet and countersigned or endorsed by a government veterinary authority. It certifies that the animal has been examined, meets the health requirements of the destination country, and is fit to travel. For most international moves from the UK, the EU AHC (official animal health certificate) format is used.

**Section 1: Animal identification**

This section covers:
- Species (dog, cat, ferret)
- Breed (as stated, not breed-verified -- the vet records what you tell them)
- Sex (male/female, neutered or intact)
- Date of birth
- Coat colour and distinguishing features
- Microchip number (ISO 11784/11785 standard, 15 digits)
- Microchip location and date of implantation

Check: the microchip number must match exactly what is in the pet. Ask the vet to scan the chip and verify the number printed on the certificate. A single digit error will cause problems at the border.

**Section 2: Owner information**

Name, address, and contact details of the owner or the authorised person responsible for the animal during transport.

**Section 3: Vaccination history**

- Rabies vaccination: product name, manufacturer, batch number, date of vaccination, date of expiry
- Other required vaccines (if applicable for the destination)

Check: the rabies vaccination must be within its valid period at time of travel. If it expires during a long sea journey or quarantine period, you may have a problem.

**Section 4: Titre test result (where required)**

For countries that require a rabies antibody titre test: the laboratory that ran the test, the date of the blood sample, the date of the result, the result (in IU/ml), and whether the animal meets the minimum threshold (0.5 IU/ml).

Check: the date of the blood sample (not the result date) must be at least three months before arrival where required.

**Section 5: Treatments (tapeworm/ectoparasites)**

For destinations like the UK, Norway, Sweden, and others: documentation of tapeworm treatment (praziquantel dose, date, time of administration). This section may also include tick treatment records.

Check: for UK entry from the EU, the tapeworm treatment must be administered between 24 and 120 hours before arrival. The certificate records the time of treatment, not just the date.

**Section 6: Veterinary attestation**

The vet signs and dates the certificate, confirming:
- The animal was clinically examined on the stated date
- The animal showed no signs of disease or infection
- The animal is fit to travel

This signature and the vet's official stamp are what make the document legally valid.

**Section 7: Government endorsement**

For most international moves, a government authority (APHA in the UK, USDA APHIS in the USA) must countersign or stamp the certificate. This adds a layer of official authentication. In the UK, APHA endorsement currently takes 24 to 48 hours online.

**Before you travel**

Read the entire health certificate carefully. Check: microchip number, vaccination dates, expiry dates, tapeworm treatment timing (if required), and owner name. If anything is wrong, contact your vet immediately -- some errors can be corrected by the vet before APHA endorsement; others require a new certificate.""",
    },
    {
        "slug": "moving-to-usa-from-europe-with-pets",
        "title": "Moving to the USA from Europe with Your Pet: CDC Rules and Practical Guide",
        "description": "Complete guide to bringing your dog or cat from Europe to the USA in 2026: CDC dog import requirements, airline policies, state-specific rules, and what to expect at US customs.",
        "date": "2026-05-06",
        "tags": ["USA", "Europe", "pet import", "CDC"],
        "faqs": [
            ("What does my dog need to enter the USA from Europe?", "Since August 2024, the CDC requires all dogs entering the USA to: be microchipped, appear healthy on arrival, be at least 6 months old, and have a signed CDC Dog Import Form (online). Dogs that were in a country with dog rabies (DMRVV) in the previous 6 months have additional requirements. Most European countries are low-risk countries for CDC purposes."),
            ("Does my cat need anything to enter the USA from Europe?", "Cats entering the USA from most European countries do not face federal-level vaccine requirements beyond appearing healthy on arrival. Some US states have their own requirements. A health certificate from a vet (issued within 10 days of travel) is good practice and may be required by your airline."),
            ("Do dogs from Europe need a rabies vaccine to enter the USA?", "The USA does not federally require a rabies vaccine for dogs from low-risk countries (most of Europe). However, the CDC Dog Import Form still applies, and individual states may require a rabies vaccine. Airlines typically require a health certificate and may have their own vaccine requirements. Check both federal and state rules for your destination."),
            ("What is the CDC Dog Import Form and how do I get it?", "The CDC online Dog Import Form (Form 5542) is completed at cdc.gov/importation/dogs. You fill in details about your dog, origin country, travel dates, and microchip. The form must be submitted and approved before travel. It is free of charge."),
        ],
        "body": """The USA updated its dog import rules significantly in August 2024, introducing the CDC Dog Import Form requirement for all dogs entering the country. The process is generally straightforward for dogs coming from low-risk European countries, but understanding the rules ahead of time avoids surprises at the airport.

**CDC dog import rules (post-August 2024)**

All dogs entering the USA, regardless of origin, must:
1. Be microchipped (ISO 15-digit chip or have a compatible chip that can be read)
2. Appear healthy on arrival
3. Be at least 6 months old
4. Have a completed and approved CDC Dog Import Form (submitted online before travel)

For dogs from low-risk countries (most of Europe, including the UK, EU member states, Norway, Switzerland), no rabies titre test is required at a federal level. The main requirement is the CDC form and microchip.

**CDC Dog Import Form**

Complete the form at cdc.gov/importation/dogs. The form asks for: owner details, dog details (species, breed, microchip), origin country, US state of destination, and date of US arrival. You must submit it 3 days before arrival at minimum. The approval is emailed back and must be shown at customs. It is free of charge.

**State-level requirements**

Individual US states may have their own import requirements for dogs and cats. Hawaii, for example, has strict rabies quarantine rules. California and some other states require proof of rabies vaccination. Check the specific state's Department of Agriculture website for requirements in your destination state.

**Cats**

There are no current federal vaccine requirements for cats entering the USA from most countries. Airlines may require a health certificate. Some states require a health certificate issued within 10 days of travel. Cats from all countries must appear healthy on arrival.

**Airlines**

Airlines flying dogs as cargo to the USA require: a health certificate issued within 10 days of travel, IATA-compliant crate, and advance booking. Delta, United, and American Airlines all have specific live animal cargo policies for international routes. British Airways and Lufthansa handle cargo pets on transatlantic routes. Check current policies at time of booking -- they change seasonally.

**Customs and border inspection**

Dogs entering the USA are inspected by US Customs and Border Protection (CBP) and USDA Animal and Plant Health Inspection Service (USDA APHIS) officials. The CDC approval form, microchip, and health certificate will be verified. The process typically takes 30 to 60 minutes for a well-documented pet.

**Practical note**

The USA does not operate quarantine for dogs and cats from most countries. For pets coming from countries with active dog rabies, additional CDC conditions apply -- check the CDC website for the current list of dog rabies virus variant countries.""",
    },
    {
        "slug": "flying-with-pets-in-cold-weather",
        "title": "Flying with Your Pet in Cold Weather: Winter Cargo Safety and What to Check",
        "description": "Practical guide to cold-weather pet air travel in 2026: winter airline embargoes, minimum temperature rules, crate insulation, and how to prepare your pet for cold conditions in cargo.",
        "date": "2026-05-06",
        "tags": ["cold weather", "winter travel", "safety"],
        "faqs": [
            ("Do airlines restrict pet cargo in cold weather?", "Yes. Most airlines have temperature-based live animal embargoes at both the origin and destination airports. If the temperature at any point in the journey falls below the airline's minimum (often 7C or 10C at the cargo area), the shipment may be refused or delayed. Cold embargoes typically apply from November to March at northern hemisphere airports."),
            ("What can I do to protect my pet in cold cargo conditions?", "Use a well-ventilated but insulated hard crate, add a thick absorbent mat or crate pad, do not clip your pet's coat before winter travel, and book the warmest part of the day (typically mid-morning) for departure. Avoid layovers at cold-weather hub airports if possible."),
            ("Are some breeds more at risk from cold during air travel?", "Yes. Short-coated breeds (Greyhound, Whippet, Doberman, Dalmatian), toy breeds, senior pets, and pets with circulation issues are more vulnerable to cold stress. Similarly, very young puppies and kittens have limited ability to self-regulate body temperature."),
            ("Can I use heating pads or heat packs in my pet's cargo crate?", "Do not use electric heating pads or chemical heat packs in a cargo crate. These create a fire risk and an overheating risk. The best cold-weather solution is a thick crate mat, dry bedding, and an insulated crate lining approved by your carrier. Confirm with the airline before adding any materials to the crate."),
        ],
        "body": """Heat embargoes in summer get most of the press, but cold-weather restrictions are equally relevant for pet owners shipping animals in winter, particularly in northern Europe, Canada, and the northern USA. Understanding the winter rules helps you plan a safe and compliant journey.

**Cold-weather airline embargoes**

Airlines typically set minimum temperature thresholds for live animal cargo. Common thresholds:
- Refused shipment if the temperature at origin or destination is below 7C (45F)
- Some carriers set a higher minimum of 10C (50F)
- The embargo applies to the cargo hold loading area, not just the outside temperature

These rules apply at the time of loading, not just at departure. A flight might depart in the morning after a cold night -- if cargo facilities are below threshold when loading, the shipment is refused.

**Winter booking strategy**

- Book mid-morning departures when temperatures are at their daily peak
- Avoid red-eye or overnight flights in winter (coldest temperatures)
- Choose direct flights (every stop is another loading bay where cold exposure occurs)
- Avoid routing through cold hub airports (Chicago, Toronto, Oslo, Helsinki in January, for example)
- Check the 5-day forecast for both origin and destination airports before confirming travel

**Crate preparation for cold**

- Use a hard crate with solid sides (not wire mesh throughout) to reduce cold air circulation
- Add a thick, dry crate mat -- multiple layers are fine
- Do NOT shave, clip, or trim your pet's coat in the weeks before winter travel
- Line the crate with a familiar blanket (your scent helps)
- Do NOT add electric heating pads or chemical heat packs (fire risk, overheating risk)
- Some owners use approved crate liners with natural insulation -- confirm with the airline

**Breeds at higher risk in cold**

Thin-coated breeds: Greyhound, Italian Greyhound, Whippet, Doberman, Dalmatian, Weimaraner, and similar lean-muscled breeds lose body heat faster than double-coated breeds. Toy breeds and very small dogs also struggle with temperature regulation. If you have one of these breeds and must travel in winter, try to achieve cabin travel or postpone until spring.

**Older and very young pets**

Senior pets and very young puppies/kittens have reduced thermoregulatory capacity. Winter cargo travel for a 12-year-old dog or a 10-week-old puppy is high-risk. Discuss timing with your vet and consider postponing cold-weather moves for vulnerable animals.

**Informing the airline**

When booking live animal cargo, ask specifically about the carrier's cold weather embargo policy for your route. Get it in writing if possible. If the temperature drops on the day of travel, having the policy confirmed in writing helps when discussing rebooking options with the cargo team.""",
    },
    {
        "slug": "new-zealand-to-australia-pet-transport-guide",
        "title": "Pet Transport from New Zealand to Australia: Trans-Tasman Rules and What to Know",
        "description": "Guide to moving your dog or cat from New Zealand to Australia in 2026: DAFF requirements, the trans-Tasman route, crate standards, and what makes NZ-Australia one of the easier pathways.",
        "date": "2026-05-06",
        "tags": ["New Zealand", "Australia", "pet transport"],
        "faqs": [
            ("Is there quarantine for pets moving from New Zealand to Australia?", "New Zealand is in a special category for Australian pet imports. Dogs and cats from New Zealand can enter Australia without the standard 10-day quarantine that applies to most other countries, provided they meet all the documentation and treatment requirements. Confirm current status via the DAFF BICON database before travel."),
            ("What does my pet need to travel from New Zealand to Australia?", "Pets from New Zealand need: ISO microchip, core vaccinations (including rabies for some pathways), CFIA-equivalent health certificate from a New Zealand official vet, and DAFF import permit. The specific treatment pathway differs from most countries due to NZ's favourable biosecurity status. Check BICON for current requirements."),
            ("How do I book the Australia import permit for a pet from New Zealand?", "Apply through the BICON (Biosecurity Import Conditions) database at agriculture.gov.au/biosecurity/bicon. Select dogs or cats and New Zealand as the origin country to see the current pathway conditions. The permit is issued electronically and must accompany the animal to Australia."),
            ("Which airlines fly pets from New Zealand to Australia?", "Air New Zealand (NZ) and Qantas (QF) both operate this route and handle pet cargo. Both airlines have established live animal procedures. Advance booking is essential -- live animal cargo space is limited on trans-Tasman flights."),
        ],
        "body": """The New Zealand to Australia route is one of the more manageable international pet moves, partly because New Zealand's biosecurity status is recognised by Australia as relatively low-risk. However, Australia still applies its biosecurity framework, and the paperwork must be correct.

**New Zealand's special status with Australia**

Australia classifies source countries by their disease risk profile. New Zealand, as a rabies-free country with similarly strict biosecurity standards, is treated more favourably than most. Dogs and cats from New Zealand may be eligible to bypass the standard 10-day post-arrival quarantine, subject to meeting treatment conditions. This is a significant advantage over the standard pathway from most other countries.

**BICON: confirm requirements before travel**

Always check the current import conditions via the DAFF BICON database (agriculture.gov.au/biosecurity/bicon) before starting the process. Requirements can change, and the BICON database is the authoritative source for current New Zealand pathway conditions.

**Standard requirements**

From New Zealand, pets typically need:
- ISO 11784/11785 microchip
- Core vaccinations (distemper, parvo, hepatitis for dogs; cat flu/enteritis for cats)
- Official health certificate issued by a New Zealand government-authorised vet and endorsed by the Ministry for Primary Industries (MPI)
- DAFF import permit (from BICON)

**Rabies vaccination**

New Zealand is rabies-free, and the pathway for NZ-origin pets may not require rabies vaccination or a titre test. However, this depends on the current pathway conditions in BICON. Confirm at the time of your application.

**The health certificate**

A New Zealand Official Vet (authorised by MPI) must issue the health certificate. MPI endorses it. The certificate must be issued within 10 days of travel.

**Airlines**

Air New Zealand and Qantas are the primary carriers on Auckland (AKL) or Christchurch (CHC) to Sydney (SYD) or Melbourne (MEL). Both have live animal booking processes and require advance notice (typically 5 to 7 days minimum). The route is short -- around 3 to 4 hours -- which is one reason this is considered a manageable pet transport route.

**Arriving in Australia**

Dogs and cats arriving from NZ are inspected at the DAFF border inspection post on arrival (Sydney, Melbourne, or Brisbane). If the pathway conditions for NZ are met, the animals may be released directly to owners without quarantine. Confirm the current clearance procedure with your IPATA agent or DAFF before travel.""",
    },
    {
        "slug": "best-airports-for-pet-transit-cargo",
        "title": "The Best (and Worst) Airports for Pet Cargo: What to Know Before You Book",
        "description": "Guide to major international airports for pet cargo in 2026: which airports have dedicated live animal facilities, temperature-controlled holding, and the smoothest customs processes.",
        "date": "2026-05-06",
        "tags": ["airports", "pet cargo", "planning"],
        "faqs": [
            ("Which airports have the best facilities for live animal cargo?", "Frankfurt (FRA), Amsterdam Schiphol (AMS), Dubai (DXB), Singapore Changi (SIN), and Sydney (SYD) are generally considered among the best equipped for live animal transit. They have temperature-controlled holding areas, experienced handling staff, and established veterinary inspection processes."),
            ("Should I avoid layovers at certain airports with my pet?", "Some airports have longer clearance times or less predictable live animal handling. For pets as cargo, try to minimise connection times and avoid airports where seasonal temperatures (very hot or very cold) regularly cause embargo issues. If possible, book direct flights."),
            ("What is a live animal acceptance facility at an airport?", "A live animal acceptance facility (often part of the cargo terminal) is where pets are checked in for air cargo transport. It includes temperature-controlled holding rooms where animals wait before loading and after arrival. Not all airports have purpose-built facilities -- some use general cargo areas."),
            ("How do I find out if my transit airport has good live animal facilities?", "Ask your IPATA agent to confirm the live animal handling capabilities at each airport on your routing. You can also contact the cargo facility directly at each airport. Airlines that regularly handle live animals (Lufthansa Cargo, Singapore Airlines Cargo) choose transit hubs based on their live animal infrastructure."),
        ],
        "body": """When shipping a pet internationally, the airport choices matter. A direct flight to a well-equipped destination is ideal -- but layovers at airports with strong live animal infrastructure are far safer than trying to connect through an airport that handles animals as an afterthought.

**Airports with strong live animal infrastructure**

**Frankfurt (FRA)**

Lufthansa Cargo's main hub. FRA has one of Europe's most developed live animal handling centres, with temperature-controlled holding areas, experienced ground staff, and fast veterinary clearance. If your European routing goes through Frankfurt, this is a good transit choice.

**Amsterdam Schiphol (AMS)**

KLM Cargo operates extensive live animal services through Schiphol. AMS has dedicated animal hotel facilities (Schiphol Animal Centre) with temperature-controlled rooms, feeding, and care for pets in transit. One of the best European options for longer transits.

**Dubai (DXB)**

Emirates SkyCargo operates one of the world's largest animal cargo operations from Dubai. DXB has a purpose-built live animal facility (Al Maktoum International Airport also has cargo infrastructure). Humidity and heat in summer can be a concern -- embargoes apply from May to October for some species.

**Singapore Changi (SIN)**

Changi has good live animal facilities, experienced handlers, and efficient customs processes. Singapore Airlines Cargo handles significant volumes of pet cargo on Asia-Pacific routes. The airport is clean, organised, and well-maintained.

**Sydney (SYD) and Melbourne (MEL)**

For arrivals into Australia, both Sydney and Melbourne have dedicated DAFF inspection facilities at their cargo terminals. Sydney handles the majority of international pet arrivals into Australia. The AQIS quarantine facility at Mickleham (near Melbourne Airport) receives most quarantine-bound pets.

**Airports to approach with caution**

**Lagos (LOS)**

Live animal clearance at Lagos is complex. Customs processes can be lengthy and unpredictable. An experienced local agent at the Lagos end is essential for smooth clearance.

**Cairo (CAI)**

CAI facilities are functional but variable in quality. Advance notification to the cargo facility and GOVS is important. An agent who has handled Cairo clearances previously is advisable.

**Certain regional airports**

Small regional airports may have limited or no dedicated live animal holding facilities. Pets transiting through these may be held in general cargo areas without temperature control. If your routing uses a small regional hub, confirm live animal capabilities in advance.

**Seasonal considerations**

Even excellent airports become problematic in extreme weather. Amsterdam and Frankfurt apply cold embargoes in January and February. Dubai and Singapore apply heat embargoes from May to October. Route your pet's journey to avoid the most extreme seasonal conditions at each transit point.

**The best approach**

When booking, ask your IPATA agent or airline about the live animal infrastructure at every airport on the route, not just the destination. The safest pet journeys are direct, through airports with dedicated live animal facilities, at a time of year when neither heat nor cold embargoes are likely to be triggered.""",
    },
]

def write_article(article):
    slug = article["slug"]
    filepath = os.path.join(BLOG_DIR, f"{slug}.md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {slug}")
        return

    tags_yaml = "\n".join(f'  - "{t}"' for t in article["tags"])
    faqs_yaml = ""
    for q, a in article["faqs"]:
        q_safe = q.replace('"', "'")
        a_safe = a.replace('"', "'")
        faqs_yaml += f'  - question: "{q_safe}"\n    answer: "{a_safe}"\n'

    title_safe = article["title"].replace('"', "'")
    desc_safe = article["description"].replace('"', "'")

    content = f"""---
title: "{title_safe}"
description: "{desc_safe}"
date: "{article['date']}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{title_safe} | PetTransportGlobal"
  description: "{desc_safe}"
tags:
{tags_yaml}
faqs:
{faqs_yaml}---

{article['body'].strip()}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"WROTE: {slug}")

if __name__ == "__main__":
    for article in ARTICLES:
        write_article(article)
    print(f"\nDone. {len(ARTICLES)} articles processed.")
