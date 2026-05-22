"""
Phase 6 Task 6.3 -- Blog batch 8 (25 articles, total target: 176)
Covers: Turkey/Israel/Belgium/Czech Republic/Colombia/Chile/Malta/Cyprus country guides;
Australia-Japan/Australia-Singapore/USA-Canada/Germany-UK/Netherlands-UK route guides;
Dachshund/Border Collie/Beagle/Husky breed guides;
should-you-sedate, IPATA, rescue dog import, pet passport renewal, cargo tracking,
cat in cabin, pet anxiety, Hungary country guide practical articles.
Skip-if-exists on all files.
"""
import os

BLOG_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    # -- Country import guides --------------------------------------------------
    {
        "slug": "turkey-pet-import-guide",
        "title": "Bringing a Pet to Turkey: Import Rules, Vaccinations and What Expats Need",
        "description": "Complete guide to bringing your dog or cat to Turkey in 2026: Ministry of Agriculture health certificate, rabies rules, microchip requirements, and Istanbul arrival.",
        "date": "2026-05-06",
        "tags": ["Turkey", "pet import", "expat"],
        "faqs": [
            ("What does my pet need to enter Turkey?", "Dogs and cats entering Turkey need a microchip, current rabies vaccination, a health certificate issued by an accredited vet in the origin country, and an official endorsement from the origin country's government veterinary authority. The certificate must confirm clinical health and vaccination status."),
            ("Is there quarantine for pets arriving in Turkey?", "Turkey does not operate mandatory quarantine for pets arriving with complete documentation from most countries. A veterinary inspection is carried out at the port of entry. Incomplete or incorrect paperwork can result in the animal being held."),
            ("Does Turkey require a rabies titre test?", "Turkey does not currently require a rabies antibody titre test for pets from most countries. A current rabies vaccination recorded on the health certificate is sufficient. Confirm current requirements for your specific origin country with the Turkish Ministry of Agriculture and Forestry."),
            ("Can I bring my dog from the UK to Turkey?", "Yes. UK pets need a health certificate issued by a UK Official Veterinarian and endorsed by APHA, microchip, and current rabies vaccination. Turkey is not an EU member, so the standard EU AHC format is used as a base but Turkey has its own specific requirements. Confirm the required format with a Turkey-specialist vet or IPATA agent."),
        ],
        "body": """Turkey is a popular destination for expats, retirees, and long-term travellers, and the country has a reasonably clear pet import process. The Ministry of Agriculture and Forestry (TKDK) manages live animal imports.

**Health certificate**

Turkey requires a health certificate issued by an accredited vet in the origin country and endorsed by the government veterinary authority. For UK arrivals, APHA endorsement is needed. The certificate must confirm: microchip number, rabies vaccination date and product, other relevant vaccinations, and a clinical examination confirming the animal is healthy.

**Microchip**

ISO 11784/11785 microchip is required. The microchip must be implanted before or on the same date as the rabies vaccination for the vaccination to be considered valid.

**Rabies vaccination**

Current rabies vaccination is required. Turkey does not require a titre test from most origin countries, but the vaccination must be documented with the product name, batch number, and expiry date on the health certificate.

**At the Turkish border**

Pets arriving by air at Istanbul Airport (IST) or Istanbul Sabiha Gokcen (SAW) are inspected by veterinary officials. The process is generally quick with complete documentation. Pets arriving at other Turkish airports or crossing land borders should confirm inspection facilities with the specific port authority in advance.

**Number of pets**

Turkey generally applies a limit of 2 pets per person for personal imports without commercial classification.

**Practical note**

Turkey's summers are very hot, particularly in central and eastern regions. If arriving between June and September, confirm with your airline whether live animal cargo embargoes are in effect for your route. Istanbul is more moderate than inland cities, but summer temperatures still affect some airline operations.""",
    },
    {
        "slug": "israel-pet-import-guide",
        "title": "Bringing a Pet to Israel: Veterinary Services Requirements and What to Prepare",
        "description": "Guide to bringing your dog or cat to Israel in 2026: Ministry of Agriculture import permit, health certificate, approved airports, and what to expect at Ben Gurion.",
        "date": "2026-05-06",
        "tags": ["Israel", "pet import", "Middle East"],
        "faqs": [
            ("Do I need a permit to import a pet into Israel?", "Yes. An import permit from Israel's Veterinary Services department (part of the Ministry of Agriculture) is required before the pet travels. Apply in advance of travel."),
            ("What does my pet need to enter Israel?", "Dogs and cats need a microchip, current rabies vaccination, a health certificate endorsed by the origin country's government authority, and an import permit from Israeli Veterinary Services. Dogs also need distemper, parvovirus, and other core vaccinations recorded on the certificate."),
            ("Does Israel quarantine imported pets?", "Israel does not operate a quarantine system for pets from most countries arriving with complete documentation. Veterinary inspection is carried out at Ben Gurion Airport. Incomplete documentation can result in the animal being detained."),
            ("Are there breed restrictions for dogs entering Israel?", "Yes. Israel has breed-specific legislation. Dangerous breed designations exist at the national level and include Pit Bull types and certain other breeds. These breeds may be subject to additional requirements or may not be importable. Confirm the current breed list with Israeli Veterinary Services before planning your move."),
        ],
        "body": """Israel is a compact country with high quality veterinary facilities and a growing expat community. The pet import process is government-regulated and requires advance work.

**Import permit**

Apply to Israeli Veterinary Services well before travel. The permit application covers the animal's details, origin country, destination in Israel, and travel dates. Processing time varies. The permit must be in hand before the animal departs the origin country.

**Health certificate**

A health certificate issued by an accredited vet in the origin country, endorsed by the government authority, is required. For UK arrivals, APHA endorsement applies. The certificate should list microchip, rabies vaccination, distemper, parvovirus, leptospirosis (for dogs), feline panleukopenia and other core vaccines (for cats), and a clinical examination.

**Arriving at Ben Gurion**

Most international pets arrive at Ben Gurion International Airport (TLV). Veterinary inspectors check documentation and inspect the animal at the border post. If documentation is correct, the process is typically efficient.

**Breed restrictions**

Israeli law lists several breeds as restricted. American Pit Bull Terriers and related types are the most commonly affected. Confirm whether your breed is on the restricted list with the Ministry of Agriculture's Veterinary Services directorate before making travel arrangements.

**Practical note**

Israel's climate includes very hot summers. July and August temperatures in Tel Aviv and inland cities exceed 30 degrees C regularly. Most airlines have cargo embargoes for live animals during peak summer heat. Schedule travel outside July-August if possible, or target early morning/late evening flights that avoid midday heat at both origin and destination airports.""",
    },
    {
        "slug": "belgium-pet-import-guide",
        "title": "Bringing a Pet to Belgium: EU Rules, AHC Requirements and What to Prepare",
        "description": "Guide to bringing your dog or cat to Belgium in 2026: EU pet passport rules, UK AHC requirements, tapeworm treatment, and FASFC inspection at Brussels.",
        "date": "2026-05-07",
        "tags": ["Belgium", "EU pet travel", "pet import"],
        "faqs": [
            ("What does my pet need to enter Belgium from the UK?", "UK pets need a microchip, current rabies vaccination, an Animal Health Certificate (AHC) issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment for dogs administered 1-5 days before arrival."),
            ("Is there a quarantine for pets arriving in Belgium?", "No quarantine for pets from most countries arriving with complete documentation. Belgium's Federal Agency for the Safety of the Food Chain (FASFC) inspects arriving pets at approved border inspection posts."),
            ("Does Belgium have breed-specific legislation?", "Belgium does not have national breed-specific legislation, but several municipalities have local rules. Flanders, Wallonia, and Brussels Capital have different regulatory environments. Some municipalities restrict or require registration of specific breeds. Confirm rules for your specific municipality."),
            ("Are there dog breed restrictions for importing into Belgium?", "No federal import ban on specific breeds, but local restrictions may apply once the dog is resident. Check with the commune (municipality) you're moving to for local bylaws on restricted breeds."),
        ],
        "body": """Belgium is an EU member state and follows EU pet travel rules. It's also the home of the EU's institutions in Brussels, making it a common destination for expats from across Europe and beyond.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination is all you need. Entry at Brussels Airport or other approved BIPs.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA is required. Dogs need tapeworm treatment (praziquantel) 1-5 days before arrival. The AHC is valid for 10 days from the vet examination date. Entry must be at an EU-approved border inspection post - Brussels Zaventem Airport and the port of Zeebrugge are the main options.

**FASFC inspection**

The Federal Agency for the Safety of the Food Chain (FASFC/AFSCA) handles live animal inspection at border posts. For commercial pet movements, pre-notification is required. For household pet relocations, the inspection at the BIP is typically straightforward.

**Belgian registration**

Dogs in Belgium must be registered with the national dog register (DogID system managed by BGFV). Registration is the owner's responsibility and should be completed after arrival. Cats don't have a national register requirement but many vets recommend microchip registration for identification purposes.

**From other non-EU countries**

Pets from EU-approved listed countries (USA, Australia, Canada, etc.) need an AHC plus microchip and current rabies vaccination. Pets from non-listed countries need a titre test in addition.""",
    },
    {
        "slug": "czech-republic-pet-import-guide",
        "title": "Bringing a Pet to Czech Republic: EU Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Czech Republic (Czechia) in 2026: EU pet passport rules, UK AHC requirements, and SVS inspection at Prague.",
        "date": "2026-05-07",
        "tags": ["Czech Republic", "Czechia", "EU pet travel", "pet import"],
        "faqs": [
            ("What does my pet need to enter Czech Republic from the UK?", "UK pets need a microchip, current rabies vaccination, an AHC issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment for dogs 1-5 days before arrival. Entry must be through an approved EU border inspection post."),
            ("Does Czech Republic quarantine imported pets?", "No mandatory quarantine for pets from most countries with complete documentation. The State Veterinary Administration (SVS) inspects arriving pets at the border inspection post at Prague Ruzyne Airport."),
            ("Are there breed restrictions in Czech Republic?", "Czech Republic does not have national breed-specific legislation. Some municipalities may have local rules, but this is not common. American Pit Bull Terriers and similar breeds do not face a national ban."),
            ("Is Prague the main entry point for pets arriving in Czech Republic?", "Yes. Prague Vaclav Havel Airport (PRG) is the primary border inspection post for live animal arrivals into Czech Republic. Pets arriving by land from other EU countries do not need a BIP inspection if they are already within the EU."),
        ],
        "body": """Czech Republic (Czechia) is an EU member state with a clear, EU-standard framework for pet import. Prague is a popular destination for expats and international students.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination. No additional requirements for intra-EU pet travel.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA. Dogs need tapeworm treatment 1-5 days before arrival. The AHC is valid for 10 days. Entry at Prague airport (the main approved BIP for non-EU arrivals).

**State Veterinary Administration**

The SVS (Statni veterinarni sprava) oversees animal welfare and imports. For household pet imports from non-EU countries, the inspection at Prague is standard. Pre-notification is not generally required for household pets, but confirm with the Prague BIP in advance for large or unusual arrivals.

**Czech registration**

Czech Republic does not require national dog registration in the same way as Germany or Belgium, but many municipalities have a Poplatek ze psa (dog tax) requiring local registration. This is typically done at the local municipal (obecni) office shortly after arrival.

**Veterinary care**

Prague has excellent veterinary facilities and several international-standard veterinary clinics used by the expat community.""",
    },
    {
        "slug": "colombia-pet-import-guide",
        "title": "Bringing a Pet to Colombia: ICA Requirements and What Expats Need to Know",
        "description": "Guide to bringing your dog or cat to Colombia in 2026: ICA health certificate requirements, microchip rules, rabies vaccination, and arriving at Bogota El Dorado.",
        "date": "2026-05-07",
        "tags": ["Colombia", "South America", "pet import", "ICA"],
        "faqs": [
            ("What government authority manages pet imports into Colombia?", "The Instituto Colombiano Agropecuario (ICA) manages live animal imports into Colombia. All pets arriving in Colombia need an ICA-approved health certificate issued in the origin country."),
            ("Does Colombia quarantine imported pets?", "Colombia does not operate a mandatory quarantine for pets from most countries with complete documentation. ICA inspectors at El Dorado International Airport in Bogota check documentation and inspect the animal."),
            ("Does Colombia require a rabies titre test?", "Colombia does not currently require a rabies antibody titre test from most origin countries. A current rabies vaccination documented on the health certificate is sufficient. Confirm current requirements with ICA for your specific origin country."),
            ("How many pets can I bring to Colombia as personal import?", "Colombia generally allows up to 2 pets per traveller as personal imports without commercial classification. More than 2 pets requires a commercial import permit process."),
        ],
        "body": """Colombia is a growing expat destination with a vibrant international community in Bogota, Medellin, and Cartagena. The ICA (Instituto Colombiano Agropecuario) manages pet imports.

**ICA health certificate**

Colombia requires a health certificate in ICA-accepted format. This must be issued by an accredited vet in the origin country and endorsed by the government authority (APHA for UK, USDA APHIS for USA, etc.). The certificate must confirm microchip number, rabies vaccination, internal and external parasite treatments, and clinical health.

**Vaccinations required**

Rabies vaccination is mandatory and must be current. For dogs, distemper, parvovirus, and leptospirosis vaccines are typically listed. For cats, panleukopenia and other core vaccines. The certificate must include product name, batch number, and vaccination dates.

**Parasite treatment**

Colombia requires evidence of internal and external parasite treatment within a set period before arrival. Confirm the timing requirements with ICA or a specialist agent.

**Arriving at El Dorado**

Most international pets arrive at El Dorado International Airport (BOG) in Bogota. ICA inspectors check documentation and inspect the animal. If documentation is complete, the process is typically efficient. Medellin and Cartagena also have international airports that can receive pets on some routes.

**Practical note**

Bogota sits at high altitude (2,600 metres), which can affect some animals, particularly those with respiratory conditions. Consult your vet if you have a brachycephalic breed or an older animal with any cardiovascular or respiratory history.""",
    },
    {
        "slug": "chile-pet-import-guide",
        "title": "Bringing a Pet to Chile: SAG Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Chile in 2026: SAG health certificate requirements, rabies vaccination rules, microchip, and arriving at Santiago Arturo Merino Benitez.",
        "date": "2026-05-07",
        "tags": ["Chile", "South America", "pet import", "SAG"],
        "faqs": [
            ("What does my pet need to enter Chile?", "Dogs and cats entering Chile need a microchip, current rabies vaccination, a health certificate in SAG-approved format issued by an accredited vet and endorsed by the origin country's government authority, and internal and external parasite treatment recorded on the certificate."),
            ("Does Chile quarantine imported pets?", "Chile does not operate a general quarantine for pets from most countries with complete documentation. SAG (Servicio Agricola y Ganadero) inspectors check documentation and inspect the animal at Santiago's Arturo Merino Benitez Airport."),
            ("Does Chile require a rabies titre test?", "Chile does not currently require a rabies antibody titre test for pets from most countries. Current rabies vaccination is sufficient. Confirm current requirements with SAG for your origin country."),
            ("What is SAG and what role does it play in pet imports to Chile?", "SAG (Servicio Agricola y Ganadero) is the Chilean Agricultural and Livestock Service. It regulates all live animal imports into Chile and is the authority that inspects arriving pets and approves health certificate formats."),
        ],
        "body": """Chile has a well-organised pet import process managed by the SAG (Servicio Agricola y Ganadero). Santiago is the primary international gateway and handles the majority of pet arrivals.

**SAG health certificate**

Chile requires a health certificate in SAG-accepted format. The certificate must be completed by an accredited vet in the origin country and endorsed by the government authority. SAG specifies the declarations required, covering microchip, vaccination history, parasite treatments, and clinical health.

**Vaccinations**

Rabies is mandatory for all arriving pets. Dogs typically need distemper, parvovirus, hepatitis, and leptospirosis vaccines listed. Cats need panleukopenia and other core vaccines. All must be current and documented with product details.

**Parasite treatment**

Internal (endoparasite) and external (ectoparasite) treatments must be carried out within the required window before travel and recorded on the certificate. Confirm specific treatment products and timing with SAG or a specialist agent.

**Arriving at Santiago**

Arturo Merino Benitez International Airport (SCL) handles international pet arrivals. SAG inspectors at the airport's agricultural inspection area check documentation and inspect the animal. This is a thorough inspection - the certificate needs to be complete and clear.

**Chile's biosecurity**

Chile takes biosecurity seriously due to its unique geographic isolation (Andes to the east, Pacific to the west, Atacama to the north). This means customs checks are strict. Bringing any undeclared animal products alongside your pet can complicate the process.

**Number of pets**

Chile generally allows 2 pets per traveller as a personal import. More than 2 requires a commercial classification and separate approval.""",
    },
    {
        "slug": "malta-pet-import-guide",
        "title": "Bringing a Pet to Malta: EU Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Malta in 2026: EU pet passport rules, UK AHC requirements, approved entry at Malta International Airport, and island biosecurity rules.",
        "date": "2026-05-07",
        "tags": ["Malta", "EU pet travel", "pet import", "Mediterranean"],
        "faqs": [
            ("What does my pet need to enter Malta from the UK?", "UK pets need a microchip, current rabies vaccination, an AHC issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment for dogs 1-5 days before arrival. Malta Airport is the only approved BIP."),
            ("Is Malta the only entry point for pets?", "Yes. Malta International Airport (MLA) is the only approved EU border inspection post for live animal arrivals into Malta. All non-EU pets must arrive via this route."),
            ("Does Malta have its own breed restrictions?", "Malta has national legislation controlling certain breeds. Dogs classified as dangerous or restricted breeds may require specific permits, registration, and handling conditions. The Malta Veterinary Regulation Directorate is the relevant authority."),
            ("Is there quarantine for pets arriving in Malta?", "No mandatory quarantine for pets from most countries with complete documentation. The Veterinary Regulation Directorate inspects arriving pets at Malta Airport."),
        ],
        "body": """Malta is one of the EU's smallest member states but has a vibrant expat community and is a popular retirement destination for UK citizens. As an island with no land borders, all pets must arrive by air.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination. Malta is an EU member, so intra-EU pet travel is straightforward.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA. Dogs need tapeworm treatment 1-5 days before arrival. AHC valid for 10 days. Malta Airport is the only entry point.

**Malta's breed restrictions**

Malta has national legislation on dangerous dogs. The list includes breeds such as Pit Bull Terrier types, Rottweilers, and others. Restricted breeds may require muzzling in public, secure fencing at home, and specific registration. Check the current list with the Malta Veterinary Regulation Directorate before your move.

**Veterinary care**

Malta has several good veterinary practices. The island is small, so access to specialist care is more limited than in larger EU countries. For complex conditions, owners often access specialist veterinary services in Italy (a short flight away).

**Practical note**

Malta's summers are very hot (38-40 degrees C in August). Air travel for pets is generally not recommended during peak summer heat, and some airlines impose live animal embargoes. If you're moving in summer, coordinate with your airline about cargo acceptance for pets on your specific route.""",
    },
    {
        "slug": "cyprus-pet-import-guide",
        "title": "Bringing a Pet to Cyprus: EU Rules, UK Arrivals and What to Prepare",
        "description": "Guide to bringing your dog or cat to Cyprus in 2026: EU pet passport rules, UK AHC requirements, tapeworm treatment, and arriving at Larnaca or Paphos airport.",
        "date": "2026-05-08",
        "tags": ["Cyprus", "EU pet travel", "pet import", "Mediterranean"],
        "faqs": [
            ("What does my pet need to enter Cyprus from the UK?", "UK pets need a microchip, current rabies vaccination, an AHC issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment for dogs 1-5 days before arrival. Entry is at Larnaca or Paphos airports."),
            ("Does Cyprus quarantine imported pets?", "Cyprus does not operate mandatory quarantine for pets from most countries with complete documentation. The Department of Veterinary Services inspects arriving pets at Larnaca or Paphos airports."),
            ("Does Cyprus have breed-specific legislation?", "Cyprus has legislation on dangerous dogs. The list of restricted breeds is managed by the Department of Veterinary Services. Certain breeds require muzzles and leads in public areas. Confirm whether your breed is affected."),
            ("Is the Republic of Cyprus or Northern Cyprus relevant for EU pet travel rules?", "EU pet travel rules apply to the Republic of Cyprus (the southern part of the island, EU member). Northern Cyprus is not an EU member and is subject to different rules. Most international arrivals land at Larnaca (Republic of Cyprus)."),
        ],
        "body": """Cyprus is an EU island nation in the eastern Mediterranean, popular with UK retirees and expats. It's a warm climate destination with good veterinary facilities and a clear pet import process.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination. Cyprus is an EU member state, so intra-EU movement is standard.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA. Dogs need tapeworm treatment (praziquantel) 1-5 days before arrival. AHC valid for 10 days. Entry at Larnaca International Airport (LCA) or Paphos International Airport (PFO).

**Veterinary Services inspection**

The Department of Veterinary Services handles border inspections at both airports. The process is standard EU BIP procedure.

**Breed restrictions**

Cyprus legislation restricts certain breeds in public. Affected breeds are typically required to be muzzled and on a lead in public spaces. Confirm current restrictions with the Department of Veterinary Services.

**Summer heat**

Cyprus has one of the hottest summers in the EU - routinely above 40 degrees C in July and August. Most airlines operate summer cargo embargoes for live animals on Cyprus routes. If you're moving in peak summer, check with your airline well in advance. Early morning flights or autumn/spring timing is strongly preferable for pet welfare.

**Practical note**

Cyprus has strong British cultural ties and several English-speaking vet practices. The vet industry is familiar with UK pet travel requirements, making it easier to find local veterinary support once you arrive.""",
    },
    # -- Route guides -----------------------------------------------------------
    {
        "slug": "australia-to-japan-pet-transport-guide",
        "title": "Pet Transport from Australia to Japan: MAFF Rules and the Preparation Timeline",
        "description": "Complete guide to moving your dog or cat from Australia to Japan in 2026: MAFF requirements, titre test process, 180-day rule, and pre-notification to the Animal Quarantine Service.",
        "date": "2026-05-08",
        "tags": ["Australia to Japan", "pet transport", "MAFF", "quarantine", "route guide"],
        "faqs": [
            ("What is the minimum quarantine for a pet arriving in Japan from Australia?", "If all documentation is correct and the 180-day waiting period after the titre test has been met, pets can qualify for a minimum 12-hour quarantine at the Japanese airport. Any documentation error can trigger up to 180 days of quarantine."),
            ("How long in advance do I need to start preparing my pet for Japan from Australia?", "At least 7-8 months. The timeline includes: microchip, 2 rabies vaccinations (spaced at least 30 days apart), wait 30 days, titre test, then a mandatory 180-day wait. Start early."),
            ("Which airports in Japan accept pets from Australia?", "Narita (NRT), Haneda (HND), Osaka Kansai (KIX), and a small number of other approved airports. Pre-notification to the Animal Quarantine Service (AQS) at the destination airport is required at least 40 days before arrival."),
            ("What laboratory do Australian pets use for the Japan titre test?", "The titre test must be conducted at a laboratory approved by Japan's Ministry of Agriculture, Forestry and Fisheries (MAFF). In Australia, the CSIRO Australian Animal Health Laboratory (AHL) and a small number of other MAFF-approved labs are used. Confirm the current approved lab list with MAFF or through an Australia-Japan specialist agent."),
        ],
        "body": """Australia to Japan is one of the more challenging international pet routes due to Japan's strict documentation and timing requirements. Australia is not on Japan's lowest-risk country list, which means the full titre test and 180-day wait applies. But with early preparation, the route is very manageable.

**Japan's documentation requirements**

Japan's MAFF (Ministry of Agriculture, Forestry and Fisheries) sets the rules for live animal imports. The key steps for Australia-origin pets are:
1. ISO-compliant microchip implanted
2. First rabies vaccination (after microchip)
3. Wait at least 30 days
4. Second rabies vaccination
5. Wait at least 30 days after the second vaccination
6. Titre test at a MAFF-approved laboratory (FAVN test, minimum 0.5 IU/ml)
7. Mandatory 180-day wait after the titre test date before the pet can enter Japan
8. Health certificate issued by an Australian government vet, endorsed by the Australian Department of Agriculture, Fisheries and Forestry (DAFF), within 10 days of travel
9. Pre-notification to Japan AQS at least 40 days before arrival

**Why the 180-day wait matters**

The 180-day wait is the single most important timing element. The clock starts on the day the titre test blood sample is collected - not the result date. If the pet arrives in Japan before 180 days have elapsed, mandatory extended quarantine (up to 180 days in a MAFF facility) applies regardless of documentation quality.

**MAFF-approved laboratories in Australia**

Not all veterinary labs can run a Japan-accepted titre test. Confirm the current approved lab list with MAFF or an Australia-Japan specialist IPATA agent before booking the test.

**Airlines on the route**

Qantas, Japan Airlines (JAL), and ANA operate Australia-Japan routes. Finnair operates Japan routes from Europe. Cargo acceptance for live animals varies by route and season - confirm with the airline before booking.

**Quarantine facility**

You need to pre-book a quarantine facility in Japan before the pet departs Australia. The Animal Quarantine Service manages approved facilities at each entry airport.""",
    },
    {
        "slug": "australia-to-singapore-pet-transport-guide",
        "title": "Pet Transport from Australia to Singapore: AVS Rules and the Preparation Process",
        "description": "Complete guide to moving your dog or cat from Australia to Singapore in 2026: AVS import licence, approved breeds, titre test, 10-day quarantine, and what to expect.",
        "date": "2026-05-08",
        "tags": ["Australia to Singapore", "pet transport", "AVS", "quarantine", "route guide"],
        "faqs": [
            ("How long does quarantine last for pets arriving in Singapore from Australia?", "10 days in an AVS-approved quarantine facility for pets that meet all documentation requirements. Singapore is rabies-free and uses quarantine to maintain that status."),
            ("Does Australia require a titre test for pets travelling to Singapore?", "Yes. Australia is on Singapore's Category C list. Pets need a rabies antibody titre test (FAVN, minimum 0.5 IU/ml), conducted at least 30 days after the most recent rabies vaccination, with a minimum 3-month wait after the titre test before travel."),
            ("What breeds of dogs are allowed into Singapore from Australia?", "Singapore only permits approved breeds listed by NParks/AVS. This list is controlled and excludes several large or powerful breeds. Check the full approved breeds list on the AVS website before planning your move."),
            ("Which airlines fly pets as cargo from Australia to Singapore?", "Singapore Airlines, Qantas, and others operate Australia-Singapore routes. Live animal cargo acceptance varies by route, airline, and season. Confirm with the specific airline for your origin-destination pair."),
        ],
        "body": """Singapore and Australia have strong people-to-people links and the Australia-Singapore pet transport route is well-trodden, but the process is demanding. Singapore's biosecurity requirements are among the strictest in Asia.

**Singapore's category system**

Australia is on Singapore's Category C list (low but non-zero rabies risk). Category C requirements:
1. ISO microchip
2. At least 2 rabies vaccinations
3. Rabies antibody titre test (FAVN, minimum 0.5 IU/ml) at an approved lab
4. At least 30 days between the most recent rabies vaccination and the titre test blood draw
5. Minimum 3-month wait after the titre test before the pet can enter Singapore

Total preparation time: at least 4 months from the first vet appointment.

**Breed restrictions**

Singapore only permits approved breeds. The NParks/AVS approved breed list is available on the Singapore government website. Several large, powerful, or fighting-type breeds are not permitted. Check your breed first - if it is not on the approved list, the move to Singapore is not possible under personal import rules.

**Import licence**

Apply for an AVS import licence before transporting the pet. The licence is obtained through the NParks portal and specifies the travel window. Give yourself enough lead time for approval.

**10-day quarantine**

All arriving pets undergo 10 days at an AVS-approved quarantine facility. Pre-book before the pet departs. You can visit during the quarantine period.

**Health certificate**

The Australian DAFF-endorsed health certificate is required. Singapore specifies the declarations needed - confirm the format with the AVS importation team or through an Australia-Singapore specialist IPATA agent.

**Direct flights**

Singapore Airlines and Qantas operate direct flights between Australian cities and Singapore. Direct is preferable to routing with connections - fewer handling events and less time in transit.

**Climate consideration**

Singapore is equatorial - hot and humid year-round. There are no seasonal cargo embargoes specifically for Singapore-origin routes from Australia, but summer embargoes may apply for Australian domestic origin airports feeding into international routes in December-February.""",
    },
    {
        "slug": "usa-to-canada-pet-transport-guide",
        "title": "Pet Transport from USA to Canada: CFIA Rules and What You Need to Cross the Border",
        "description": "Guide to moving your dog or cat from the USA to Canada in 2026: CFIA requirements, health certificate for dogs, crossing at land borders vs airports, and provincial rules.",
        "date": "2026-05-08",
        "tags": ["USA to Canada", "pet transport", "CFIA", "route guide"],
        "faqs": [
            ("What does my dog need to travel from USA to Canada?", "Dogs from the USA entering Canada need a current rabies vaccination (if over 3 months old) and a vet health certificate signed by a licensed US veterinarian confirming the vaccination. Dogs under 3 months old do not need a rabies vaccination but need a vet health certificate."),
            ("Do cats need a rabies vaccination to cross from USA to Canada?", "Cats travelling from the USA to Canada do not require rabies vaccination under CFIA federal rules. A vet health certificate is recommended."),
            ("Can I drive my pet across the US-Canada border?", "Yes. The US-Canada land border is the most commonly used route for pet relocations between the two countries. At the land border crossing, declare your pet to CBSA (Canada Border Services Agency) and present the vet health certificate for dogs."),
            ("Do I need an import permit to bring my pet from USA to Canada?", "No import permit is required for personal household pets (dogs and cats) entering Canada from the USA. The CFIA health certificate requirement and the rabies vaccination for dogs are the main requirements."),
        ],
        "body": """The USA-Canada border is one of the world's busiest and the pet crossing process is relatively simple for most owners. Both countries have aligned veterinary standards, and the shared border makes land travel an easy option.

**Dogs from USA to Canada**

Dogs entering Canada from the USA need:
- Current rabies vaccination if the dog is over 3 months old
- A vet health certificate from a licensed US veterinarian confirming the rabies vaccination status, microchip (if applicable), and general health

No import permit is required. No quarantine on arrival. CBSA may ask to see the certificate at the border.

**Dogs under 3 months**

Dogs under 3 months old are exempt from the rabies vaccination requirement. A vet health certificate confirming age and health is still recommended.

**Cats from USA to Canada**

Cats do not require rabies vaccination under CFIA federal rules for crossing from the USA. A vet health certificate is recommended for smooth customs clearance.

**Land border crossings**

At land border crossings, you will go through the CBSA primary inspection. Declare your pet on the customs declaration form. Most crossings are quick. Have the vet certificate ready. If there is any question about the animal's health or documentation, CBSA can refer you to the local CFIA office.

**Flying**

For air travel, the same documentation applies. Declare your pet on the customs form. Most major US-Canada airlines (Air Canada, WestJet, United, Delta, American) accept pets in cabin (small) or cargo (larger). Check each airline's specific policy.

**Provincial rules**

Canada's provinces set their own animal import rules on top of the federal CFIA requirements. British Columbia, Ontario, and Quebec each have different rules for breed-specific legislation, registration, and licensing. Once in Canada, register your pet with the local municipality.""",
    },
    {
        "slug": "germany-to-uk-pet-transport-guide",
        "title": "Pet Transport from Germany to UK: AHC, Tapeworm and the Post-Brexit Process",
        "description": "Complete guide to moving your dog or cat from Germany to the UK in 2026: AHC requirements, tapeworm treatment for UK entry, and what APHA endorsement means for Germany-origin pets.",
        "date": "2026-05-09",
        "tags": ["Germany to UK", "pet transport", "AHC", "route guide"],
        "faqs": [
            ("What does my dog need to enter the UK from Germany?", "Dogs entering the UK from Germany (an EU country) need a microchip, current rabies vaccination, an AHC issued by a German Official Veterinarian and endorsed by the German government authority, and tapeworm treatment administered by a vet 24-120 hours before arriving in Great Britain."),
            ("Does my cat need tapeworm treatment to enter the UK from Germany?", "No. The tapeworm treatment requirement applies to dogs only. Cats need microchip, current rabies vaccination, and an AHC endorsed by the German authority."),
            ("How long is the AHC valid for when travelling from Germany to the UK?", "The AHC is valid for 10 days from the date of the veterinary examination. The UK entry must take place within this 10-day window."),
            ("Can I use an EU pet passport to bring my dog from Germany to the UK?", "EU pet passports are not accepted for entry into Great Britain (England, Scotland, Wales) post-Brexit. An AHC is required. EU pet passports are still accepted for entry into Northern Ireland in some circumstances - confirm the current rules with DAERA (Department of Agriculture, Environment and Rural Affairs) for Northern Ireland entry."),
        ],
        "body": """Post-Brexit, the UK is a third country from the EU's perspective - and equally, the EU is a third country from the UK's perspective. Moving your pet from Germany to the UK requires an Animal Health Certificate, even though both countries are close neighbours and Germany was previously the easiest of European origins.

**What you need**

Your dog or cat needs:
- ISO 11784/11785 microchip
- Current rabies vaccination (first vaccination requires a 21-day waiting period)
- Animal Health Certificate issued by a German Official Veterinarian (amtlicher Tierarzt) and endorsed by the relevant German authority (typically the Kreisveterinaeramt - district veterinary office)
- Dogs only: tapeworm treatment (praziquantel) administered by a vet 24-120 hours before arrival in Great Britain

**The AHC process in Germany**

In Germany, the amtlicher Tierarzt (Official Veterinarian, OV) is typically employed by the district veterinary office (Kreisveterinaeramt or Veterinaramt) rather than a private practice. Your private vet can prepare the health documentation, but the endorsement needs to come from the OV. Alternatively, some private practices have staff with OV status.

**Entry into Great Britain**

The approved entry points for pets entering Great Britain from non-listed third countries (including EU members, post-Brexit) are specific. Eurotunnel Le Shuttle (pets in the car), ferry routes to Dover/Portsmouth/other approved ports, and direct flights to approved airports (London, Manchester, Edinburgh, etc.). Air France, Lufthansa, British Airways, and easyJet operate Germany-UK routes.

**Northern Ireland**

Entry into Northern Ireland has different rules under the Windsor Framework. EU pet passports may still be accepted for entry into Northern Ireland from EU countries in some circumstances. Confirm with DAERA before planning your route if Northern Ireland is your destination.

**Timing**

The tapeworm treatment timing is the most common source of errors. It must be between 24 hours (minimum) and 120 hours (maximum) before arrival in Great Britain. Work backwards from your arrival time to schedule the vet appointment.""",
    },
    {
        "slug": "netherlands-to-uk-pet-transport-guide",
        "title": "Pet Transport from Netherlands to UK: AHC, Tapeworm and What to Prepare",
        "description": "Guide to moving your dog or cat from the Netherlands to the UK in 2026: AHC requirements, tapeworm treatment timing, NVWA endorsement, and route options including ferry.",
        "date": "2026-05-09",
        "tags": ["Netherlands to UK", "pet transport", "AHC", "route guide"],
        "faqs": [
            ("What does my dog need to enter the UK from the Netherlands?", "Dogs entering the UK from the Netherlands need a microchip, current rabies vaccination, an AHC issued by a Dutch Official Veterinarian and endorsed by the NVWA, and tapeworm treatment administered 24-120 hours before arriving in Great Britain."),
            ("Which ferry routes can I use to travel from the Netherlands to the UK with my pet?", "Stena Line operates Hoek van Holland to Harwich. P&O Ferries and DFDS operate Rotterdam/Amsterdam to various UK ports. Eurotunnel also accepts pets for the Channel Tunnel crossing from France (requiring driving from the Netherlands to Calais). Check each operator's pet policy before booking."),
            ("Does my cat need a titre test to enter the UK from the Netherlands?", "No. Cats from Netherlands do not need a titre test to enter the UK. Netherlands is an EU member and is on the UK's list of approved countries, meaning only microchip, current rabies vaccination, and an AHC are required."),
            ("Can I use a ferry from Netherlands to the UK with my pet?", "Yes. Ferry routes are a popular option for pet travel. Dogs and cats typically stay in the car on vehicle deck or in designated on-board pet kennels for the overnight routes. Confirm specific pet policy with each ferry operator."),
        ],
        "body": """The Netherlands and the UK have close trade and people links, and the Hook of Holland to Harwich ferry route is one of the most common pathways for pets making this journey. Since Brexit, an AHC is required, but the process is well understood.

**What you need**

Microchip, current rabies vaccination, AHC issued by a Dutch OV and endorsed by the NVWA, and tapeworm treatment (praziquantel) for dogs 24-120 hours before arriving in Great Britain.

**The Dutch OV process**

Official Veterinarians in the Netherlands are typically based at the NVWA (Nederlandse Voedsel- en Warenautoriteit - Netherlands Food and Consumer Product Safety Authority) or authorised private practices. Your regular private vet can prepare the documentation, and the NVWA OV endorses it. Allow a few days for the endorsement process.

**Ferry routes**

The Netherlands-UK ferry routes are a practical option, particularly for people driving with pets:
- Stena Line: Hoek van Holland to Harwich (8 hours overnight)
- P&O Ferries: Rotterdam to Hull
- DFDS: IJmuiden (near Amsterdam) to Newcastle

Pets typically travel in the car on the vehicle deck or in designated on-deck kennels. Overnight crossings mean you'll be separate from your pet for several hours. Most ferries allow brief check visits during the crossing.

**Air routes**

KLM/Air France, British Airways, and easyJet operate Amsterdam Schiphol to multiple UK airports. Most airlines require dogs to travel as cargo on international routes. Small dogs meeting weight limits may travel in cabin on qualifying routes - confirm with the airline.

**Tapeworm timing**

The 24-120 hour window is firm. Work backwards from your scheduled arrival time in the UK to schedule the vet appointment and confirm the ferry/flight booking aligns.""",
    },
    # -- Breed guides ----------------------------------------------------------
    {
        "slug": "travelling-with-a-dachshund-internationally",
        "title": "Travelling Internationally with a Dachshund: Cargo, Cabin Options and What to Know",
        "description": "A practical guide to flying internationally with a Dachshund: cabin eligibility by size, crate requirements for cargo, back health considerations, and breed-specific travel tips.",
        "date": "2026-05-09",
        "tags": ["Dachshund", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a Dachshund travel in the cabin on a flight?", "Miniature Dachshunds may qualify for cabin travel if the pet plus carrier combined weight is under the airline's in-cabin limit (typically 6-8kg). Standard Dachshunds are usually too heavy for cabin limits and travel as cargo."),
            ("Are Dachshunds banned from any countries?", "Dachshunds are not subject to breed-specific legislation in any major international destination. They are widely accepted globally."),
            ("Are there any health concerns for Dachshunds in cargo?", "Dachshunds are not brachycephalic, so they do not face the respiratory concerns of flat-faced breeds. However, Dachshunds are prone to intervertebral disc disease (IVDD). Consult your vet about whether your specific dog's spinal health makes cargo travel appropriate."),
            ("What size crate does a Miniature Dachshund need?", "Most Miniature Dachshunds fit an IATA 200 or 300 crate. The crate must allow the dog to stand, sit, turn, and lie down without touching the walls. Measure your dog before ordering."),
        ],
        "body": """Dachshunds are adaptable, curious dogs that generally travel well. Their main international travel consideration is size: miniature Dachshunds may qualify for cabin travel, while standard Dachshunds typically need to go as cargo.

**Cabin vs cargo**

Miniature Dachshunds typically weigh 4-5kg as adults. Combined with a soft-sided carrier, this often falls within the 6-8kg cabin limit for most airlines. A Miniature Dachshund in a well-ventilated, correctly-sized soft carrier can travel comfortably in the cabin.

Standard Dachshunds are heavier and may not meet airline cabin weight limits. They travel as cargo in a hard-sided IATA crate. The crate must be large enough for the dog to stand at full height, turn completely, sit, and lie down comfortably.

**IVDD consideration**

Dachshunds are predisposed to Intervertebral Disc Disease (IVDD) due to their elongated spines. If your Dachshund has a history of disc problems or has had surgery, discuss with your vet whether long-haul cargo travel is appropriate. The vibration and temperature changes during a long cargo flight are not typically a problem for healthy Dachshunds, but a dog with active spinal issues needs specific veterinary assessment.

**Breed bans**

Dachshunds are not restricted by any country's BSL (breed-specific legislation). They travel freely to all major destinations.

**Crate training**

As with all dogs, crate training before the journey significantly reduces stress. Let the Dachshund spend time in the crate at home before travel. Feed meals in the crate. Build positive associations over several weeks.""",
    },
    {
        "slug": "travelling-with-a-border-collie-internationally",
        "title": "Travelling Internationally with a Border Collie: Cargo Travel and What to Expect",
        "description": "A guide to international pet transport with a Border Collie: crate sizing, the intelligent breed's travel temperament, breed-specific considerations, and health preparation.",
        "date": "2026-05-09",
        "tags": ["Border Collie", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a Border Collie travel in the cabin on a flight?", "No. Border Collies are too large to travel in the cabin. They travel as cargo in an IATA-compliant crate. Most airlines accept them on international routes."),
            ("Are Border Collies banned in any countries?", "No. Border Collies are not subject to breed-specific legislation in any major international destination."),
            ("What size crate does a Border Collie need for air travel?", "Most adult Border Collies require an IATA 400 crate (approximately 81cm x 54cm x 58cm) or an IATA 500 for larger individuals. Measure your dog before ordering - the crate must allow standing, turning, sitting, and lying down without touching the walls."),
            ("How do Border Collies cope with cargo travel?", "Border Collies are highly intelligent and can be more anxious than some other breeds if they are not well prepared. Thorough crate training over several weeks or months is particularly important. A Border Collie that is familiar with its crate and comfortable being confined will handle the journey much better."),
        ],
        "body": """Border Collies are among the world's most intelligent dogs and frequent international movers. They are not subject to any breed bans, are accepted as cargo by most major airlines, and generally travel well when properly prepared.

**Cargo travel**

Border Collies are medium-sized dogs and always travel as checked cargo. They cannot travel in the cabin due to their size. In the hold, they are in a pressurised, temperature-controlled section of the aircraft.

**Crate sizing**

Most adult Border Collies fit an IATA 400 (81cm x 54cm x 58cm). Larger males may need an IATA 500. Measure your specific dog - the crate must allow the dog to:
- Stand at full height (head not touching the top)
- Turn completely around
- Sit without the top of the head touching
- Lie down with legs extended

**Intelligence and crate training**

Border Collies are working dogs with high mental energy needs. A Border Collie that has not been introduced to the crate before travel may find confinement stressful. Begin crate training at least 4-6 weeks before travel. Use positive reinforcement - feed meals in the crate, provide puzzle toys inside, make the crate a positive space.

**Breed bans**

Border Collies are not restricted in any major destination country. They travel freely internationally.

**Exercise before departure**

Give your Border Collie a substantial walk or run before travel. A physically tired dog settles more easily in the crate. Avoid food for 4-6 hours before departure but ensure water is available up to 2-3 hours before loading.""",
    },
    {
        "slug": "travelling-with-a-beagle-internationally",
        "title": "Travelling Internationally with a Beagle: What Owners Need to Know",
        "description": "A guide to flying internationally with a Beagle: cargo sizing, breed-specific health considerations, country restrictions, and preparation tips for a scent hound.",
        "date": "2026-05-10",
        "tags": ["Beagle", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a Beagle travel in the cabin on a flight?", "Beagles are generally too large and heavy for cabin travel on most airlines, which typically cap in-cabin pets at 6-8kg combined with carrier. Beagles travel as cargo."),
            ("Are Beagles restricted in any countries?", "Beagles are not subject to breed-specific legislation in any major international destination. They are widely accepted globally."),
            ("What size crate does a Beagle need for air travel?", "Most adult Beagles fit an IATA 300 or 400 crate. Measure your specific dog - the crate must allow standing, turning, sitting, and lying down without touching the walls."),
            ("How do Beagles cope with air travel?", "Beagles are scent hounds with a strong nose and can be easily distracted or excited by unfamiliar smells during travel. Adequate crate training and familiar bedding with your scent in the crate can help. Consult your vet about whether any calming aids are appropriate for your specific dog."),
        ],
        "body": """Beagles are cheerful, curious dogs and generally make uncomplicated international travellers. They are not subject to any breed bans and are accepted by most major airlines as cargo.

**Cargo travel**

Most adult Beagles weigh 8-14kg, which puts them above the typical cabin pet weight limit. Beagles travel as cargo in IATA-compliant hard-sided crates. The hold is pressurised and temperature-controlled, and the journey is safe for healthy Beagles with proper preparation.

**Crate sizing**

Most adult Beagles fit an IATA 300 (61cm x 46cm x 41cm) or IATA 400 (81cm x 54cm x 58cm) depending on their size. Measure your individual dog - the crate must allow the dog to stand, turn, sit, and lie down without restriction.

**Scent sensitivity**

Beagles have one of the strongest senses of smell in the dog world. Unfamiliar smells at airports and handling facilities can cause excitement or stress. Including a well-worn piece of your clothing in the crate provides a familiar, reassuring scent. Avoid putting novel-smelling bedding in the crate for travel.

**USA entry note**

USA's CDC requires that dogs arriving from all countries have a microchip implanted on or before the date of their first rabies vaccination. Beagles are one of the most commonly used breeds in US laboratory research and have very familiar import rules in the USA - the CDC requirements apply to all dogs regardless.

**Breed bans**

Beagles are not restricted in any country under breed-specific legislation. They travel freely internationally.""",
    },
    {
        "slug": "travelling-with-a-husky-by-air",
        "title": "Flying Internationally with a Husky: Cold-Weather Breed Challenges and What to Prepare",
        "description": "A guide to international pet transport with a Siberian Husky or Alaskan Malamute: size considerations, summer heat risks, crate sizing, and airline acceptance.",
        "date": "2026-05-10",
        "tags": ["Husky", "Siberian Husky", "Alaskan Malamute", "breed guide", "international pet travel"],
        "faqs": [
            ("Can a Husky fly in a plane?", "Yes. Huskies travel as cargo in IATA-compliant crates. They are not brachycephalic and do not face the same respiratory risks as flat-faced breeds. Their thick double coat is the main welfare consideration in warm climates or summer routing."),
            ("Are Huskies banned in any countries?", "Siberian Huskies are not subject to breed-specific legislation in major international destinations. Some countries have cold-climate breed restrictions for animal welfare reasons in very hot climates - this is rare but worth checking."),
            ("What size crate does a Siberian Husky need?", "Most adult Siberian Huskies require an IATA 500 (91cm x 61cm x 66cm) or larger. Alaskan Malamutes typically need an IATA 700 or custom crate. Measure your specific dog."),
            ("Should I be worried about flying a Husky in summer?", "Yes. Huskies have thick double coats designed for cold climates. Flying in summer heat - particularly on routes with hot transit points (Gulf hubs, Mediterranean airports in August) - poses a real overheating risk. Most airlines have summer cargo embargoes that will already restrict routing. Ideally, schedule Husky travel in cooler months."),
        ],
        "body": """Huskies and Malamutes are striking dogs that attract attention wherever they go. They are healthy, strong breeds with no breed bans to worry about - but their thick double coats and association with cold climates create real welfare considerations for summer travel and hot destination routes.

**Cargo travel**

All Huskies travel as cargo. They are large dogs and will always be in the hold. This is safe on modern aircraft in pressurised, temperature-controlled sections, but temperature management during ground handling (at hot airports, during summer months) is the main concern.

**Summer heat restrictions**

Huskies are designed for cold. In temperatures above 25 degrees C on the ground, they can overheat rapidly. Most major airlines have summer live animal cargo embargoes for routes through or to hot regions. These embargoes typically apply when ground temperatures exceed 29-32 degrees C at any point in the journey. For a Husky specifically, erring on the side of caution is advisable.

Schedule Husky travel in:
- Autumn (October-November)
- Winter
- Spring (March-April)

Avoid July and August for any route involving hot airports.

**Crate sizing**

Adult Siberian Huskies typically need an IATA 500. Adult Alaskan Malamutes are considerably larger and may need an IATA 700 or a custom airline-approved crate. Many standard airline cargo crate sizes top out at IATA 700 (122cm x 81cm x 89cm). Contact the airline directly for very large breeds.

**Breed bans**

Huskies are not restricted by breed-specific legislation in any major destination country. They are accepted globally.

**Acclimatisation at destination**

If you're moving a Husky to a warmer climate (e.g., from Canada to Australia or UK to UAE), allow several weeks for acclimatisation after arrival. Keep the dog out of direct midday sun, provide adequate shade and water, and watch for signs of heat stress.""",
    },
    # -- Practical / information articles -------------------------------------
    {
        "slug": "should-you-sedate-your-pet-on-a-flight",
        "title": "Should You Sedate Your Pet for a Flight? What Vets Actually Say",
        "description": "A clear guide to the veterinary consensus on sedating pets for air travel: why it is generally not recommended, what the risks are, and what alternatives exist.",
        "date": "2026-05-10",
        "tags": ["pet sedation", "air travel", "vet advice", "pet welfare"],
        "faqs": [
            ("Is it safe to sedate a dog or cat for a flight?", "Veterinary guidance strongly advises against sedating pets for air travel. Sedation affects heart rate and respiratory function and can be dangerous at altitude. The American Veterinary Medical Association (AVMA) and most airline policies reflect this position. Consult your vet if you have specific concerns about your pet's anxiety."),
            ("Why do vets advise against sedation on flights?", "Sedation relaxes the muscles including those involved in balance and respiratory function. At altitude, where oxygen levels are slightly lower and pressure changes occur, sedated animals are at greater risk of respiratory distress, cardiovascular problems, and inability to adjust their position in the crate. Sedated pets also cannot self-regulate temperature or alert handlers to distress."),
            ("Are there any alternatives to sedation for anxious pets?", "Yes. Options include: prolonged crate training to make the crate a comfortable, familiar space; pheromone products (Adaptil for dogs, Feliway for cats) applied to the crate; nutraceutical calming supplements (confirm with your vet); and short-acting prescription anxiolytics that are safer than full sedation. Discuss your pet's specific anxiety level with your vet."),
            ("Do airlines allow sedated pets?", "Many airlines explicitly prohibit or discourage the transport of sedated animals. Some require the owner to declare on a live animal acceptance form that the animal has not been sedated. Check with your airline before considering any calming medication."),
        ],
        "body": """It is a very common concern among pet owners preparing for international moves: should I sedate my dog or cat for the flight? The short answer from the veterinary community is: generally, no. Here is why.

**Why sedation is not recommended**

The American Veterinary Medical Association (AVMA), the British Veterinary Association (BVA), and most major airline policies align on this: routine sedation of pets for air travel is not recommended. The reasons are physiological.

Sedatives relax muscles and depress the central nervous system. In the lower-oxygen, variable-pressure environment of an aircraft hold, this creates specific risks:
- Respiratory function may be compromised
- Cardiovascular events are harder to monitor
- The animal cannot adjust its position to maintain airway patency
- Temperature regulation becomes impaired
- The animal cannot respond to handlers or signal distress

In a cargo hold, a sedated animal cannot be monitored in real time. If something goes wrong, there is no immediate response available.

**What is actually safer**

Good preparation reduces anxiety far more effectively than sedation. Specifically:
- Crate training over several weeks before travel. A dog or cat that genuinely associates the crate with safety and comfort will be far calmer during transit.
- Pheromone sprays: Adaptil (for dogs) and Feliway (for cats) can be sprayed in the crate 30 minutes before loading. These are not sedatives but can reduce anxiety responses.
- Exercise before departure: a well-exercised dog that has had a long walk or run before check-in will rest more during the flight.
- Familiar bedding with the owner's scent.

**When medication might be appropriate**

There are specific cases where a vet might prescribe a low-dose anxiolytic (not a full sedative). If your pet has severe travel anxiety that cannot be addressed through crate training and preparation alone, discuss this with a vet who knows your animal's health history. The choice of medication, dose, and timing is highly individual.

**Tell your vet the full picture**

Mention the flight duration, transit points, and season when talking to your vet about any pre-travel medications. What works for a 2-hour European flight may not be appropriate for a 14-hour long-haul journey.""",
    },
    {
        "slug": "what-is-ipata-pet-transport-accreditation",
        "title": "What Is IPATA and Why It Matters When Moving Pets Internationally",
        "description": "A guide to IPATA (International Pet and Animal Transportation Association): what it is, what membership means, how to find an IPATA member, and when you should use one.",
        "date": "2026-05-10",
        "tags": ["IPATA", "pet transport agent", "accreditation", "pet relocation"],
        "faqs": [
            ("What does IPATA stand for?", "IPATA stands for the International Pet and Animal Transportation Association. It is the primary international trade association for pet transport professionals. Members include pet relocation companies, freight forwarders, and ground handlers."),
            ("Is IPATA membership mandatory for pet transport agents?", "No. IPATA membership is voluntary. However, membership signals that a company has met IPATA's membership requirements and adheres to its code of ethics and standards. Using an IPATA member provides a degree of assurance that is not available with non-members."),
            ("How do I find an IPATA member in my country?", "IPATA has a member directory on its website at ipata.com. You can search by country or city to find registered members. This is the recommended starting point when selecting a pet transport agent for an international move."),
            ("What does an IPATA agent actually do?", "An IPATA-accredited pet transport agent typically handles: customs and import documentation, airline booking and cargo management, quarantine bookings (where applicable), health certificate guidance, crate procurement and sizing, and coordination with ground handlers at origin and destination airports."),
        ],
        "body": """If you've started researching international pet transport, you've probably come across IPATA. Here's what it means and why it matters.

**What IPATA is**

IPATA (International Pet and Animal Transportation Association) is a non-profit trade association founded in 1979 for companies involved in pet transport. Members include pet relocation specialists, freight forwarders, customs brokers, and ground handlers worldwide. As of 2025, IPATA has members in over 85 countries.

**What membership means**

IPATA membership is not a government certification or a regulatory licence - it is industry membership. Members agree to IPATA's code of ethics and standards, which cover animal welfare, professional conduct, and handling practices. Membership requires demonstration of professional experience and references.

It does not guarantee a perfect outcome - pet transport has inherent unpredictability - but an IPATA member has made professional commitments that non-members have not.

**When you should use an IPATA agent**

For straightforward routes (e.g., USA to Canada, UK to France with an EU pet passport), many owners manage the process themselves. But for complex routes, an IPATA agent provides genuine value:
- Japan, Australia, Singapore, New Zealand: long quarantine-risk destinations with exact documentation requirements
- Multi-country routes or transit through restricted airports
- Brachycephalic breeds with airline acceptance challenges
- Commercial pet imports or multiple animals
- Any situation where a documentation error would trigger extended quarantine

**How to find one**

Search the IPATA member directory at ipata.com. Filter by country or city. Look for agents who list your specific origin-destination pair as their speciality or who have relevant country experience.

**What to ask an IPATA agent**

- Do they have experience with your specific route (not just the destination country)?
- Can they provide references from recent clients on the same route?
- What is included in their fee (documentation, crate procurement, airline booking, customs, quarantine coordination)?
- What happens if documentation is rejected at the border?""",
    },
    {
        "slug": "importing-a-rescue-dog-from-abroad",
        "title": "Importing a Rescue Dog from Abroad: What You Need to Know Before You Commit",
        "description": "A practical guide to importing a rescue dog internationally in 2026: documentation challenges, titre test risks, charity vs private import, and what can go wrong.",
        "date": "2026-05-11",
        "tags": ["rescue dog", "dog import", "international rescue", "pet import"],
        "faqs": [
            ("Can I import a rescue dog from another country?", "Yes, but the process is more complex than importing a known pet from a well-documented background. Rescue dogs from rabies-endemic countries may require a titre test, which adds 3-6 months to the timeline. Documentation gaps are common with rescue animals."),
            ("What are the main risks when importing a rescue dog?", "The main risks are: incomplete or uncertain vaccination history (which may require restarting the vaccination programme), unknown rabies titre test status, documentation that does not meet destination country requirements, and breed uncertainty affecting BSL compliance."),
            ("Does the UK allow rescue dog imports?", "The UK has tightened restrictions on commercial rescue dog imports. The Pet Travel Scheme covers personal pets. Commercial movement of dogs (including rescues from charities) has specific requirements. APHA and DEFRA publish current guidance on non-commercial vs commercial pet movements."),
            ("What should I check before committing to importing a rescue dog?", "Check: vaccination history completeness and verifiability, microchip registration, breed (for BSL countries), origin country's rabies status (which determines whether a titre test is needed), and the documentation format required by your destination country."),
        ],
        "body": """Importing a rescue dog internationally is deeply rewarding and, if done properly, entirely achievable. But it has a different risk profile to importing a known pet with full documentation. Understanding what you're taking on before you commit is important.

**Documentation challenges**

Rescue animals, particularly those from shelters in Eastern Europe, Southeast Asia, Africa, or Latin America, often come with incomplete or uncertain vaccination histories. A dog whose vaccination history is unknown or undocumented cannot simply be given a certificate saying it has been vaccinated - many destination countries require specific timing and product information.

If vaccination history is uncertain, the safest approach is to restart the vaccination programme from the beginning. This adds time but ensures the receiving country's requirements can be met with verifiable, timed documentation.

**Titre test requirements**

If your destination country requires a rabies titre test (Japan, Australia, Singapore, New Zealand, and others), and the rescue dog comes from a country on the required list, the titre test is mandatory. The titre test clock starts from a validated vaccination, not from adoption. A rescue dog with uncertain vaccination history may need:
1. Microchip verification
2. Full vaccination restart
3. Wait for titre test eligibility
4. Titre test
5. Wait period after titre test

This process can take 6-12 months depending on the destination country. If you're on a corporate relocation timeline, this needs early attention.

**Breed uncertainty and BSL**

Some rescue dogs have unclear parentage. If you're moving to a country or region with breed-specific legislation (UK, Germany specific states, some US cities, Singapore), unknown breed composition can create complications. DNA testing can provide some evidence of breed composition, but it is not always accepted as definitive proof for BSL purposes.

**Reputable rescue organisations**

Work with established, reputable rescue charities that have experience with international documentation. These organisations will have vets who understand export requirements and can provide properly timed certificates. Avoid informal arrangements or impulse adoptions on holiday without understanding the documentation implications.

**UK import rules**

The UK tightened restrictions on commercial rescue imports following concerns about fraud and welfare issues. The current APHA guidance distinguishes between personal pets and commercially imported animals. Confirm the current status of rescue imports from your specific origin country with APHA before making commitments.""",
    },
    {
        "slug": "pet-passport-renewal-guide",
        "title": "EU Pet Passport Renewal: When It Expires and What to Do",
        "description": "A guide to EU pet passport expiry, renewal, and what happens if your pet passport is out of date when travelling in 2026.",
        "date": "2026-05-11",
        "tags": ["EU pet passport", "pet passport renewal", "pet travel documents"],
        "faqs": [
            ("Does an EU pet passport expire?", "The EU pet passport itself does not have an expiry date printed on it - it is valid for the life of the animal, assuming the vaccinations within it are kept current. However, the vaccinations recorded in the passport do expire. If the rabies vaccination lapses, travel is not permitted until a valid vaccination is recorded by an authorised vet."),
            ("What happens if my pet's rabies vaccination expires?", "If the rabies vaccination expires, the pet passport is effectively invalid for travel purposes. You need to get a new rabies vaccination administered by an authorised vet who can enter it in the passport. Depending on the vaccination history, a booster may suffice or a new 21-day waiting period may apply."),
            ("Can I get a new EU pet passport if I lose the old one?", "Yes. A replacement EU pet passport can be issued by an authorised vet in the EU. The new passport will record the current microchip and vaccination history that can be verified. You cannot simply reprint the old one - a new physical passport is issued."),
            ("UK pets no longer have EU pet passports after Brexit - what do they use?", "UK pets cannot obtain new EU pet passports since Brexit. UK pets travelling to EU countries use an Animal Health Certificate (AHC) instead, valid for 10 days per journey. UK pet owners can explore getting an EU pet passport if their pet is also registered in an EU country."),
        ],
        "body": """The EU pet passport is a lifelong document - but it only works if the vaccinations inside it are kept current. Understanding the difference between the passport itself and the vaccinations recorded in it prevents unnecessary travel complications.

**What the EU pet passport is**

An EU pet passport is a standardised document issued by authorised vets in EU member states. It records the animal's identity (microchip number, species, breed, colour, date of birth, owner details) and vaccination history. It is valid for the lifetime of the animal - there is no separate passport expiry date.

**When it stops working**

The passport becomes invalid for travel purposes if the rabies vaccination recorded in it has expired. Rabies vaccinations are issued for 1 or 3 years depending on the product. When the expiry date on the last vaccination entry passes, the pet cannot travel on that passport until a new vaccination is entered by an authorised vet.

**Renewals and boosters**

An authorised vet administers the booster vaccination and enters it in the passport. If the vaccination was allowed to lapse completely (missed the booster date), some countries require waiting to confirm the animal has not been exposed to rabies - check with your vet about the specific protocol for your destination.

**Lost passport**

If the passport is lost, an authorised vet in any EU country can issue a new one. The new passport records the current microchip and the vaccination history that can be verified or re-administered. The old passport's history cannot be copied across without verification.

**UK pet owners**

Since Brexit, UK vets can no longer issue EU pet passports. UK pets travelling to EU countries use an AHC (valid 10 days per trip). Some UK owners have their pets registered with EU-country vets (e.g., after holidays in Spain) to obtain a second-country EU passport - this is technically possible but requires careful management to avoid discrepancies.""",
    },
    {
        "slug": "how-to-track-your-pet-in-cargo",
        "title": "How to Track Your Pet While They Are in Air Cargo",
        "description": "A practical guide to tracking your pet's journey in air cargo: what airlines offer, how ground handling works, what you can and cannot know during the flight, and how to stay calm.",
        "date": "2026-05-11",
        "tags": ["pet cargo", "tracking", "air freight", "pet transport", "pet welfare"],
        "faqs": [
            ("Can I track my pet in real time while they are in cargo?", "Real-time GPS tracking of individual pets in cargo holds is not available on most commercial airlines. Some specialist pet cargo services offer tracking updates at key handling points. Airlines typically update the cargo status in their freight tracking systems at check-in, loading, and arrival."),
            ("How do I know if my pet made the same flight as me?", "If your pet is booked as excess baggage (not separate air cargo), they are on the same aircraft as you. If your pet is booked as separate air cargo through a freight forwarder, they may be on the same or a different flight. Confirm at check-in whether the pet has been loaded on your flight."),
            ("What should I do if my pet has not appeared at the destination after the flight?", "Contact the airline's cargo/baggage team at the destination airport immediately. Large airports have a dedicated live animal handling team. Do not leave the airport until you have confirmation of your pet's location."),
            ("Who is responsible for my pet between check-in and collection at the destination?", "Ground handlers at the origin airport, the airline's cabin crew/cargo team during the flight, and ground handlers at the destination airport. IATA LAR (Live Animals Regulations) specify the standards for live animal handling throughout this chain."),
        ],
        "body": """One of the most anxious parts of international pet transport is the time when your pet is in the cargo system and you cannot see them. Understanding what is happening and what information is available makes this period more manageable.

**How pets move through cargo**

After check-in, your pet goes through the following stages:
1. Check-in and documentation check by airline staff
2. Transfer to the animal holding area at the departure airport (temperature-controlled in most major airports)
3. Loading into the aircraft hold prior to departure (the last stage before flight)
4. Flight (pressurised, temperature-controlled hold section)
5. Unloading at the destination airport
6. Transfer to the live animal area at the destination
7. Your collection from the cargo/baggage hall

**What tracking is available**

Airlines do not typically offer real-time GPS tracking of individual animals. What most do offer is:
- Cargo booking reference that can be tracked through the airline's freight tracking system
- Status updates at key handling points: checked in, departed, arrived, available for collection
- Phone or email notification systems on some routes

**Specialist services**

Some IPATA-accredited agents use specialist pet cargo services that offer more detailed tracking updates, including notifications when the animal is loaded, when they arrive, and when they are in the collection area. This is available on premium pet cargo services and some airlines.

**At the destination**

Arrive at the cargo hall with your documentation (cargo AWB number, identification) and the live animal's paperwork. Most major international airports have a dedicated live animals section. The process is typically efficient if you are prepared.

**What to do if something seems wrong**

If there is any delay, contact the airline's cargo team immediately. They have direct access to the handling teams and can locate your pet far faster than waiting at the collection counter. Having the airline's cargo phone number for the destination airport saved in your phone before travel is worth doing.""",
    },
    {
        "slug": "flying-with-a-cat-in-cabin-complete-guide",
        "title": "Flying with a Cat in the Cabin: The Complete Step-by-Step Guide",
        "description": "A practical guide to flying with a cat in the cabin on international and domestic flights in 2026: carrier sizing, airline policies, security screening, and keeping your cat calm.",
        "date": "2026-05-12",
        "tags": ["flying with a cat", "cat in cabin", "airline pet policy", "cat transport"],
        "faqs": [
            ("What is the weight limit for a cat in the cabin?", "Most airlines limit in-cabin pets to a combined weight (cat plus carrier) of 6-8kg. Cats typically weigh 4-6kg, and a soft carrier adds 1-2kg, so many cats qualify. Confirm the specific limit with your airline before booking."),
            ("What carrier does a cat need for in-cabin travel?", "A soft-sided carrier that fits under the seat in front. Typical approved dimensions are approximately 43 x 30 x 20cm (though airlines vary). The carrier must be leak-proof and well-ventilated. Do not use a hard-sided plastic crate for cabin travel."),
            ("Can cats travel in the cabin on international flights?", "It depends on the airline and route. Some airlines permit cats in cabin on international routes; others restrict cabin pets to domestic routes only. Airlines like Lufthansa, Air France, KLM, and Turkish Airlines accept cats in cabin on qualifying international routes. Always confirm with the specific airline for your route."),
            ("How do I get my cat through airport security with them in the carrier?", "At most airports, you will need to remove your cat from the carrier and carry them through the body scanner (or be taken aside for a wand check) while the empty carrier goes through the X-ray machine. Hold your cat firmly during this process. Ask a security officer for assistance if needed."),
        ],
        "body": """Flying with a cat in the cabin is genuinely possible and far less stressful than cargo for both you and the cat, if the cat and carrier meet the requirements. Here is how to make it work.

**Which airlines allow cats in cabin**

Not all airlines accept cats in cabin on international routes. Those that commonly do include: Lufthansa, Air France, KLM, Turkish Airlines, Iberia, Finnair, TAP Air Portugal, and many US carriers (American, Delta, United, JetBlue) on domestic routes. Long-haul carriers are more restrictive. Always confirm in advance.

**Weight and size limits**

Most airlines set a maximum combined weight of 6-8kg (cat plus carrier). Soft-sided carriers typically weigh 1-2kg, leaving room for most adult cats.

**The carrier**

Choose a soft-sided carrier that:
- Fits under the seat in front (check your specific aircraft's under-seat dimensions - they vary by seat class and aircraft type)
- Has a ventilated mesh panel for airflow
- Has a waterproof base (accidents can happen)
- Has a zip or clip closure that is secure

Measure under-seat space for your specific flight - it varies significantly between airlines and aircraft types.

**Preparing your cat**

Start leaving the carrier open at home weeks before travel. Let the cat explore and sleep in it. Feed meals inside the carrier. By the time of travel, the carrier should be a familiar, safe space rather than a threat.

On travel day:
- Withhold food for 3-4 hours before departure
- Provide water up to 1-2 hours before
- Do not use a litter tray in the carrier for in-cabin travel - it creates odour issues for other passengers

**At the airport**

Go through check-in with the carrier visible. Declare your pet if required. At security, hold your cat while the carrier goes through the X-ray. This is the most stressful moment for most cats - hold firmly, move quickly, get the carrier back on as fast as possible.

**During the flight**

The cat must remain in the carrier under the seat throughout the flight. Most cats settle after take-off once the noise stabilises. Talking to your cat quietly can be reassuring. Do not open the carrier during the flight.""",
    },
    {
        "slug": "pet-anxiety-air-travel-guide",
        "title": "Managing Pet Anxiety During Air Travel: Practical Advice from Vets and Owners",
        "description": "A guide to recognising and managing anxiety in dogs and cats during international air travel: signs to watch for, preparation strategies, and what vets recommend.",
        "date": "2026-05-12",
        "tags": ["pet anxiety", "air travel", "pet welfare", "stress management"],
        "faqs": [
            ("How do I know if my pet is anxious about flying?", "Signs of anxiety in dogs include: excessive panting, drooling, trembling, barking, scratching at the crate, refusing food, yawning, and pacing. Cats show anxiety through vocalisation, hiding, excessive grooming, dilated pupils, and flattened ears. Mild anxiety is normal; severe distress needs veterinary assessment before travel."),
            ("Can I give my pet something for anxiety before a flight?", "Discuss this with your vet before travel. Options range from pheromone products (Adaptil for dogs, Feliway for cats, both available as sprays for the carrier) to nutraceutical supplements to prescription anxiolytics for severe cases. Full sedation is generally not recommended for air travel."),
            ("Does crate training help with flight anxiety?", "Yes, significantly. A pet that associates the crate with safety and comfort is far calmer during transport than one that has had no crate exposure. Starting crate training 4-6 weeks before travel is the single most impactful preparation step."),
            ("Is anxiety worse on long-haul flights than short ones?", "It depends on the individual animal. Some pets settle after the initial noise and movement and sleep for the duration of a long-haul flight. Others remain anxious throughout. Animals that have flown before and had a neutral experience often do better on longer routes. First-time flyers may benefit from a shorter test journey if feasible."),
        ],
        "body": """Some level of stress during pet travel is normal and expected - airports are noisy, unfamiliar, and filled with strange smells. The goal is not zero anxiety but managed, welfare-appropriate levels of stress that the animal can recover from quickly on arrival.

**Recognising anxiety**

Dogs: panting beyond what the temperature warrants, drooling, trembling, frantic scratching at the crate, vocalising, eyes showing white sclera, not accepting treats (a sign of high stress in food-motivated dogs), excessive yawning.

Cats: vocalising (calling repeatedly), hiding in the back of the carrier, hyperventilating, excessive drooling, dilated pupils, piloerection (fur standing up). Some cats go very still and silent when extremely stressed - this can be misread as calm.

**Preparation: the most important factor**

The best anxiety prevention is preparation rather than medication:

**Crate training**: Start 4-6 weeks before travel. Leave the crate open in a familiar room. Feed meals inside it. Put a piece of your worn clothing inside. Progress to closing the door briefly, then for longer periods. By travel day, the crate should feel like a safe den rather than a threat.

**Pheromone products**: Adaptil (dog appeasing pheromone) and Feliway (cat facial pheromone) sprays applied to the inside of the carrier 15-30 minutes before the animal enters can reduce anxiety responses. These are not sedatives and are safe to use. Available from vets and pet shops.

**Exercise**: Give dogs a substantial walk or run before departure. A physically tired dog is a calmer dog.

**Routine**: Keep your own behaviour calm at the airport. Animals read owner anxiety. If you're stressed, your pet is more likely to be stressed.

**When to involve a vet**

If your pet has a history of severe anxiety in enclosed spaces, separation anxiety, or known fear of loud noises, discuss travel plans with your vet well before the journey. For severe cases, a vet may prescribe a short-acting anxiolytic that is safer for travel than general sedation. Never use human anxiety medications on animals without veterinary guidance.""",
    },
    {
        "slug": "moving-pets-to-hungary",
        "title": "Moving Pets to Hungary: EU Rules and What International Arrivals Need",
        "description": "Guide to bringing your dog or cat to Hungary in 2026: EU pet passport rules, UK AHC requirements, breed restrictions, and arriving at Budapest Ferenc Liszt Airport.",
        "date": "2026-05-12",
        "tags": ["Hungary", "EU pet travel", "pet import", "Budapest"],
        "faqs": [
            ("What does my pet need to enter Hungary from the UK?", "UK pets need a microchip, current rabies vaccination, an AHC issued by a UK Official Veterinarian and endorsed by APHA, and tapeworm treatment for dogs 1-5 days before arrival. Entry must be through an EU-approved border inspection post at Budapest Airport."),
            ("Does Hungary have breed-specific legislation?", "Yes. Hungary has national breed-specific legislation. The restricted breeds list in Hungary includes American Staffordshire Terriers, Staffordshire Bull Terriers, Bull Terriers, Rottweilers (with conditions), and others. Restricted breeds require special permits, liability insurance, muzzle and lead in public, and secure housing. Some breeds may be prohibited from import. Confirm the current list with the Hungarian government authority (Nebih) before travelling with a restricted breed."),
            ("What is the process at Budapest Airport for non-EU pet arrivals?", "Non-EU pets arriving at Budapest Ferenc Liszt International Airport must go through the EU-approved border inspection post at the airport. Nebih (National Food Chain Safety Office) inspectors check documentation and inspect the animal."),
            ("Is there quarantine for pets arriving in Hungary?", "No mandatory quarantine for pets from most countries with complete documentation. The process is the standard EU BIP inspection."),
        ],
        "body": """Hungary is a growing expat destination, particularly Budapest, which has a vibrant international community. As an EU member state, Hungary follows EU pet travel rules. However, it has its own national breed-specific legislation which is more extensive than many EU neighbours.

**From EU countries**

A valid EU pet passport with current microchip and rabies vaccination. No additional requirements for intra-EU pet travel.

**From the UK**

An AHC issued by a UK OV and endorsed by APHA. Dogs need tapeworm treatment (praziquantel) 1-5 days before arrival. AHC valid for 10 days. Entry at Budapest Ferenc Liszt International Airport (BUD), which has an EU-approved BIP for live animal arrivals.

**Breed-specific legislation**

Hungary has one of the more detailed national breed restriction lists in the EU. Restricted breeds include:
- American Staffordshire Terrier
- Staffordshire Bull Terrier
- Bull Terrier
- Rottweiler (conditions apply - not fully banned but regulated)
- Dogo Argentino
- Fila Brasileiro
- And others

Restricted breeds in Hungary require: a Nebih import permit, owner competency certification, liability insurance, muzzle and lead in public, secure housing with specific fencing requirements. Some breeds may be prohibited entirely from personal import.

If you have a breed that might fall under Hungarian BSL, confirm current rules with Nebih (National Food Chain Safety Office) before planning your move.

**Registration**

Dogs in Hungary must be registered with the local municipal authority and in the national pet registration database within a set period of arrival.

**Veterinary care**

Budapest has good veterinary facilities. Several international-standard practices cater to the expat community and are familiar with import documentation requirements.""",
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
