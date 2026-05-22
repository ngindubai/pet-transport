"""
generate_blog_batch5.py
Task 4.7 Batch B — Blog articles 75-100.
26 new articles to reach the 100-article target.
Covers airline guides, route-specific guides, breed travel, and expert topics.
"""

import os

BLOG_DIR = os.path.join("site", "content", "blog")

ARTICLES = [
    {
        "slug": "turkish-airlines-pet-transport-guide",
        "title": "Turkish Airlines Pet Transport: Cabin and Cargo Policies for International Flights",
        "description": "Turkish Airlines accepts pets in cabin and as cargo on most routes. Complete guide to weight limits, breed restrictions, booking process, and what to expect at Istanbul Airport.",
        "date": "2026-06-03",
        "tags": ["airlines", "turkish-airlines", "planning"],
        "faqs": [
            ("Does Turkish Airlines allow dogs in the cabin?",
             "Yes. Turkish Airlines allows dogs and cats in the cabin on most routes if the combined weight of the animal and carrier does not exceed 8 kg. Snub-nosed (brachycephalic) breeds are not permitted in the cabin."),
            ("Which brachycephalic breeds does Turkish Airlines ban?",
             "Turkish Airlines bans brachycephalic dog breeds including French Bulldogs, English Bulldogs, Pugs, Boston Terriers, and Shih Tzus from cargo travel. In-cabin travel may be possible for small brachycephalic dogs under 8 kg, but restrictions change. Check directly with Turkish Airlines before booking."),
            ("How do I book a pet on Turkish Airlines?",
             "Contact Turkish Airlines customer service or your booking agent directly - pet spaces cannot be booked online. Book as early as possible; space is limited per flight."),
        ],
        "body": """Turkish Airlines operates one of the world's largest route networks, connecting over 120 countries through Istanbul Ataturk and Istanbul Airport (IST). For pet owners, it offers genuine options for both cabin and cargo travel.

## In-Cabin Pet Policy

Small dogs and cats are accepted in the cabin if:
- Combined weight of animal and carrier is **8 kg or under**
- The carrier fits under the seat in front (max approx. 23 x 40 x 55 cm)
- The breed is not brachycephalic (snub-nosed)
- The route is not one of the exceptions (check current policy for specific routes)

Maximum 1 pet carrier per passenger. Book the cabin pet space by calling Turkish Airlines or asking at the time of ticket purchase — it cannot be added online after booking in most cases.

## Cargo Pet Policy

Dogs and cats may travel as accompanied excess baggage or manifest cargo for most breeds and sizes. Turkish Airlines Cargo handles live animals on freight shipments.

Brachycephalic breeds have additional restrictions for cargo travel. Check the current list directly with Turkish Airlines before booking — the list is updated periodically.

## What to Expect at Istanbul Airport

Istanbul Airport (IST) is one of the world's busiest hub airports. For connecting flights with pets, note that Turkish Airlines requires the pet to remain in its carrier throughout the connection. The airport has dedicated areas for live animal handling, but connections at IST add time — factor in connection times carefully for cargo shipments.

## Documentation Requirements

Same as for all international routes: microchip, current vaccinations, government-endorsed health certificate matching the destination country's requirements.

## Cost

Turkish Airlines charges for pets in-cabin (varies by route — typically EUR 80-200) and for cargo (by weight and dimensions). Get a quote when booking.

---

*Sources: Turkish Airlines official pet travel policy; IATA Live Animals Regulations. Data current as of June 2026.*""",
    },
    {
        "slug": "singapore-airlines-pet-transport-guide",
        "title": "Singapore Airlines Pet Transport: Cargo-Only Policy, Breed Restrictions, and SIA Process",
        "description": "Singapore Airlines does not accept pets in the cabin. Cargo policy, breed restrictions, Singapore AVS import requirements, and how to book live animal cargo on SIA routes.",
        "date": "2026-06-03",
        "tags": ["airlines", "singapore-airlines", "planning"],
        "faqs": [
            ("Does Singapore Airlines allow pets in the cabin?",
             "No. Singapore Airlines does not accept pets in the cabin on any routes. All pets travel as manifest cargo (via SIA Cargo). Guide dogs and assistance dogs are accepted in the cabin."),
            ("Which breeds does Singapore Airlines ban from cargo?",
             "Singapore Airlines bans all brachycephalic (snub-nosed) dog and cat breeds from cargo travel. This includes French Bulldogs, Pugs, English Bulldogs, Boston Terriers, Pekingese, Persian cats, British Shorthairs, and similar breeds. Additionally, several large and powerful breeds are banned."),
            ("How far in advance do I need to book a pet on Singapore Airlines cargo?",
             "Book at least 4-6 weeks in advance for live animal cargo on Singapore Airlines. Space is limited and allocated per flight. Ensure you have all documentation in order before confirming the booking."),
        ],
        "body": """Singapore Airlines (SIA) operates premium long-haul routes connecting Asia, Europe, Australia, and the Americas. Pets travel exclusively as cargo — there is no in-cabin pet option. For routes into Singapore, the destination's strict AVS import requirements add complexity.

## Cargo-Only Policy

SIA Cargo handles all live animal shipments. Pets travel as:
- **Accompanied excess baggage** on the same flight as the owner, or
- **Unaccompanied manifest cargo** on a separate freight booking

Both options require the full IATA-compliant crate and documentation package.

## Breed Restrictions

Singapore Airlines applies a comprehensive breed ban list. No brachycephalic breeds (flat-faced dogs or cats) are accepted in cargo under any circumstances. The ban list also includes several powerful breeds. Request the current full list from SIA Cargo at the time of booking — it is subject to change.

## Entering Singapore

Singapore has a category-based animal import system managed by **AVS** (Animal and Veterinary Service). Pets are divided into categories:
- **Category 1** (Singapore, Australia, NZ, UK, Ireland, some others): Simpler documentation, no quarantine
- **Category 2** (Most other countries): Additional requirements including titre test, 30-day quarantine

Check AVS's current category for your pet's origin country at the time of booking.

## Booking SIA Cargo Live Animals

1. Contact SIA Cargo or your IATA agent to confirm space
2. Confirm the breed is not on the restricted list
3. Provide documentation and crate specifications for cargo booking
4. Receive air waybill number

## Cost

SIA Cargo charges are based on chargeable weight (actual vs. dimensional weight, whichever is higher). Long-haul flights from Europe to Singapore for a large dog can run GBP 1,200-2,500+ in cargo charges.

---

*Sources: Singapore Airlines official pet policy; SIA Cargo live animals policy; Singapore AVS import categories. Data current as of June 2026.*""",
    },
    {
        "slug": "ethiopian-airlines-pet-transport-guide",
        "title": "Ethiopian Airlines Pet Transport: Africa's Largest Carrier and Its Live Animal Policies",
        "description": "Ethiopian Airlines pet cargo and cabin policy. Breed restrictions, route-specific rules, and how to book live animal transport on ET flights across Africa, Europe, and beyond.",
        "date": "2026-06-05",
        "tags": ["airlines", "ethiopian-airlines", "africa"],
        "faqs": [
            ("Does Ethiopian Airlines allow pets in the cabin?",
             "Ethiopian Airlines allows small pets (dogs, cats, birds) in the cabin if the combined weight of the animal and carrier does not exceed 8 kg and the carrier fits under the seat. This applies to selected routes. Check with ET directly for your specific route."),
            ("Does Ethiopian Airlines carry pets as cargo to African destinations?",
             "Yes. Ethiopian Airlines Cargo operates an extensive African route network. Live animals are accepted as cargo on many routes. Contact ET Cargo or your IATA agent for route-specific availability and documentation requirements."),
            ("Are brachycephalic breeds accepted on Ethiopian Airlines?",
             "Ethiopian Airlines applies restrictions on brachycephalic breeds similar to other major carriers. Short-nosed breeds may be refused for cargo travel in hot conditions. Check with ET before booking."),
        ],
        "body": """Ethiopian Airlines (ET) is Africa's largest airline by revenue and operates an extensive international network from Addis Ababa Bole International Airport (ADD). For pet owners moving within Africa or between Africa and Europe, ET is often the most direct option.

## In-Cabin Pets

Ethiopian Airlines accepts small animals in the cabin on most routes if:
- Combined weight (animal + carrier): **8 kg or under**
- Carrier fits under the seat (check current dimension limits)
- The breed is not subject to additional restrictions

Book cabin pets by calling ET reservations. Space is limited.

## Cargo Pets

ET Cargo handles live animal cargo. Ethiopian Airlines' cargo network covers over 80 African destinations alongside intercontinental routes. For moves within Africa (Ethiopia to Kenya, Nigeria, South Africa), ET is often the best available direct-route option.

Key facts for cargo bookings:
- Book through ET Cargo or an IATA-accredited agent
- Provide microchip number, species, breed, and crate dimensions
- Confirm documentation requirements for the destination country with ET
- Allow 4-6 weeks booking lead time

## Addis Ababa as a Hub

Bole International Airport handles all cargo transfers. ADD operates at a moderate altitude (2,355 m) which keeps temperatures mild year-round — an advantage for live animal ground handling compared to Gulf hub airports in summer.

## Documentation

Standard requirements apply: ISO microchip, current vaccinations, government-endorsed health certificate for the destination. For moves within Africa, note that many African countries require import permits — confirm before booking.

---

*Sources: Ethiopian Airlines official pet policy; ET Cargo live animals programme. Data current as of June 2026.*""",
    },
    {
        "slug": "travelling-with-a-labrador-retriever-by-air",
        "title": "Travelling with a Labrador Retriever: Size, Airlines, and Cargo Considerations",
        "description": "Labs are one of the most common dogs transported internationally. Guide to which airlines accept Labradors, IATA crate sizes, breed-specific restrictions, and what to expect in cargo.",
        "date": "2026-06-05",
        "tags": ["labrador", "dogs", "breeds", "airlines"],
        "faqs": [
            ("Can a Labrador travel in the cabin?",
             "No. Labradors are too large to travel in the cabin on commercial flights. A typical adult Labrador weighs 25-36 kg, far above the 8 kg cabin pet limit. Labradors travel as cargo in an IATA-compliant crate."),
            ("What IATA crate size does a Labrador need?",
             "Most adult Labradors need an IATA size 500 or 700 crate depending on individual dimensions. Measure your specific dog: nose to tail base + 10 cm (length), floor to top of head + 10 cm (height), shoulder width x 1.5 (internal width). Never buy a crate by breed name alone -- measure your individual dog."),
            ("Are Labradors subject to breed bans internationally?",
             "No. Labradors are not subject to breed bans in any country. They are widely accepted by airlines and are not on any domestic breed restriction list. A Labrador is one of the most straightforward breeds to transport internationally."),
        ],
        "body": """Labradors are consistently among the most popular dogs in the world and one of the most commonly transported breeds internationally. They are uncomplicated to move -- no breed bans, no airline restrictions, and a generally calm temperament that helps them handle cargo travel better than many breeds.

## Size and Crate Requirements

An adult Labrador typically needs an **IATA size 500 or 700 crate**. Do not choose a crate size by breed name alone -- measure your specific dog.

**How to measure:**
- Length (A): nose to base of tail + 10 cm
- Height (B): floor to top of ears + 10 cm
- Width (D): shoulder width x 1.5

Compare these measurements against the crate's *internal* dimensions. The dog must be able to stand, turn around, and lie in a natural position.

A size 500 has approximate internal dimensions of 83 x 57 x 61 cm. A size 700: 99 x 67 x 74 cm. If your Lab is at the boundary, go larger.

## Which Airlines Accept Labradors

Labradors are accepted by virtually all major carriers for cargo travel, subject to their standard live animal policies. No airline breed-restricts Labradors. Airlines to check for your specific route:

- **Lufthansa:** Cargo and cabin (cabin for puppies under 8 kg only)
- **KLM:** Cargo and some in-cabin options for small dogs; Labs as cargo
- **British Airways:** Cargo for dogs (no in-cabin pets)
- **Qantas:** Cargo
- **Emirates:** Cargo on selected routes
- **Air New Zealand:** Cargo
- **Singapore Airlines:** Cargo (no cabin pets)

Book cargo space 4-8 weeks in advance. Cargo hold space for large crates is limited.

## Preparing a Lab for Cargo Travel

Labradors generally adapt well to crate travel if properly prepared. Start crate training at least 4 weeks before the flight:
- Introduce the crate gradually; let the dog explore it voluntarily
- Feed meals inside the crate
- Progress to overnight crate sleeping
- A dog that sleeps in its crate at home handles cargo travel significantly better

## Health Certificate

A Labrador needs the same health certificate as any other breed -- ISO microchip, current vaccinations, government-endorsed health certificate for the destination. No additional documentation is required for a Labrador specifically.

---

*Sources: IATA Live Animals Regulations 2024; individual airline live animal policies. Data current as of June 2026.*""",
    },
    {
        "slug": "travelling-with-a-german-shepherd-by-air",
        "title": "Travelling with a German Shepherd: Cargo, Crate Size, and Country Restrictions",
        "description": "German Shepherds are large dogs that travel as cargo. Guide to IATA crate sizing, airline acceptance, breed-specific country regulations, and how to prepare a GSD for the journey.",
        "date": "2026-06-07",
        "tags": ["german-shepherd", "dogs", "breeds", "airlines"],
        "faqs": [
            ("Are German Shepherds banned in any countries?",
             "German Shepherds are not subject to national import bans in most countries. However, some Middle Eastern countries and a few others restrict or require special conditions for German Shepherds due to their working-dog classification. Some apartment communities and pet-friendly rentals in destinations like Singapore and Hong Kong have size restrictions that effectively exclude large breeds. Always check destination country regulations directly."),
            ("What size IATA crate does a German Shepherd need?",
             "Most adult German Shepherds need an IATA size 500 or 700 crate. A standard male GSD weighs 30-40 kg and measures approximately 55-65 cm at the shoulder. Measure your specific dog and compare against the crate's internal dimensions."),
            ("Do German Shepherds have problems with air travel?",
             "German Shepherds generally tolerate cargo travel well if they have been properly crate-trained. The breed is adaptable and calm under pressure when comfortable in its crate. Avoid sedation -- the AVMA advises against sedating animals for air travel as it affects their ability to balance and regulate temperature."),
        ],
        "body": """German Shepherds are working dogs with confident, adaptable temperaments -- qualities that translate reasonably well to cargo travel when the dog is properly prepared. They travel on every major cargo route and are accepted by all major airlines.

## Crate Requirements

A standard adult male German Shepherd (30-40 kg, 60-65 cm at shoulder) typically needs an **IATA size 700 crate**. Females and smaller individuals may fit a size 500. Measure your dog:

| Measurement | Method | Minimum crate |
|-------------|--------|---------------|
| Length | Nose to tail base + 10 cm | Internal length |
| Height | Floor to top of ears + 10 cm | Internal height |
| Width | Shoulder width x 1.5 | Internal width |

The crate must meet all three dimensions simultaneously. When in doubt, go larger.

## Airline Acceptance

German Shepherds are accepted by all major airlines as cargo. No carrier specifically restricts the breed. Relevant factors:
- **Crate size and weight:** Large GSDs in size 700 crates can approach the weight limits some airlines set for single-piece cargo. Check weight limits for your specific route.
- **Cargo hold dimensions:** Most wide-body aircraft accommodate size 700 crates. Narrow-body (regional) aircraft may not. Confirm with the airline.

## Country-Specific Notes

Most countries have no German Shepherd-specific restrictions. Points to check:
- **Middle East (UAE, Kuwait, Saudi Arabia):** German Shepherds are sometimes classified as working/guard breeds with additional conditions. Confirm with the destination authority.
- **Singapore:** No breed ban, but AVS category and import conditions apply.
- **Australia/NZ:** Full standard documentation applies; no GSD-specific restrictions.

## Crate Training

A German Shepherd that has been crate-trained from puppyhood handles cargo significantly better than one encountering a crate for the first time before a long flight. If you have time: start crate training at least 4-6 weeks before travel. Reward calm crate behaviour. Allow the dog to sleep in the crate overnight.

If the dog is not crate-trained and travel is imminent, consult your vet about a pre-travel settling routine. Do not administer sedatives without veterinary advice -- sedation in cargo can be dangerous.

---

*Sources: IATA Live Animals Regulations 2024; AVMA guidance on animal transport; individual airline live animal policies. Data current as of June 2026.*""",
    },
    {
        "slug": "cats-in-cargo-what-to-expect",
        "title": "Transporting Cats in Cargo: What to Expect and How to Prepare",
        "description": "Most cats travel internationally in cargo holds, not cabins. What cargo travel actually involves, how cats cope, preparation tips, and which airlines handle cats well.",
        "date": "2026-06-07",
        "tags": ["cats", "cargo", "airlines", "planning"],
        "faqs": [
            ("Is it safe to transport a cat in cargo?",
             "Yes, for healthy cats with proper preparation. The cargo hold of a commercial airliner is pressurised and temperature-controlled at the same cabin altitude as the passenger cabin. The main risks are stress from unfamiliar confinement and poor crate preparation. A cat that is comfortable in its carrier and is in good health handles cargo travel well in most cases."),
            ("Can a cat travel in the cabin on international flights?",
             "Some airlines allow small cats (carrier + cat under 8 kg) in the cabin on international routes. Airlines that commonly allow cabin cats: Lufthansa, KLM, Air France, Iberia, Turkish Airlines. Airlines that do not allow cabin pets: British Airways, Qantas, Singapore Airlines. Confirm the policy for your specific route before booking."),
            ("Should I sedate my cat for a long flight?",
             "The AVMA (American Veterinary Medical Association) and most airline policies advise against sedation for cats in cargo. Sedation affects the cat's ability to balance, regulate temperature, and respond to its environment. If your cat is severely anxious, discuss pheromone-based calming options (Feliway) with your vet instead."),
        ],
        "body": """The vast majority of cats travelling internationally do so in the cargo hold. For most destinations, there is no cabin option -- and even where cabin travel is permitted, many cats are too large or their owners prefer the convenience of cargo rather than managing a carrier under the seat for 10+ hours.

Understanding what cargo travel actually involves helps owners prepare their cats properly.

## The Cargo Hold: What it's Like

The cargo hold of a modern wide-body airliner (Boeing 777, Airbus A330, A350) is:
- Pressurised at the same cabin altitude as the passenger cabin (equivalent to 6,000-8,000 feet)
- Heated to approximately 18-20°C during cruise (not as warm as the passenger cabin, but not cold)
- Dark and vibrating
- Significantly quieter than the passenger cabin after take-off noise subsides

The physical environment is survivable. The challenge for cats is psychological: unfamiliar confinement, strange smells, handling by strangers, and separation from their owner and home environment.

## Preparing Your Cat

**Crate familiarisation (6+ weeks before):**
- Leave the carrier open in the cat's living area
- Place bedding and toys inside
- Feed meals near or inside the carrier
- Progress to closing the door for short periods, then longer
- A cat comfortable sleeping in its carrier handles cargo better

**On travel day:**
- Do not feed for 4 hours before the flight (reduces nausea risk)
- Place a worn item of clothing in the carrier (familiar scent)
- Secure a frozen water holder to the inside of the crate door
- Add absorbent bedding

**Pheromone products:**
- Feliway spray applied to bedding 15-30 minutes before travel (allow to air for 10 minutes)
- Feliway can reduce travel stress without the risks of sedation

## Crate Requirements

An IATA-compliant rigid carrier is required for cargo. The cat must be able to stand, turn around, and lie naturally. Typical cats need an IATA size 100 (small cats) to 300 (large cats).

Do not use a soft-sided carrier for cargo hold travel.

## Airlines That Handle Cats Particularly Well

- **Lufthansa/Swiss/Austrian (Lufthansa Group):** Known for well-maintained live animal facilities at Frankfurt
- **KLM:** Good live animal handling at Amsterdam Schiphol
- **Air New Zealand:** Good reputation for trans-Pacific cat cargo
- **Japan Airlines:** Excellent live animal standards on routes into Japan

## What Happens on Arrival

The cat is held in the cargo facility until the owner (or agent) presents documentation and collects it. For quarantine countries (Australia, NZ), the cat is transferred directly from cargo to the quarantine facility.

---

*Sources: IATA Live Animals Regulations 2024; AVMA guidance on animal transport; Feliway/Ceva scientific literature on feline travel stress. Data current as of June 2026.*""",
    },
    {
        "slug": "cites-permits-exotic-pets",
        "title": "CITES Permits for Exotic Pets: What International Travellers Need to Know",
        "description": "If your pet is a species listed under CITES Appendix I, II, or III, you need export and import permits for international travel. Guide to what CITES covers, how to apply, and common mistakes.",
        "date": "2026-06-09",
        "tags": ["cites", "exotic-pets", "regulations", "parrots"],
        "faqs": [
            ("Does CITES apply to common pets like parrots and reptiles?",
             "Yes. Many commonly kept exotic pets are CITES-listed, including most parrot species (CITES Appendix I or II), many reptile species (chameleons, tortoises, monitor lizards), some primates, and various other species. If you own a non-domestic species, check its CITES listing before planning any international travel."),
            ("What is the difference between CITES Appendix I and Appendix II?",
             "Appendix I includes species threatened with extinction. Commercial trade is generally prohibited. Moving an Appendix I animal internationally for non-commercial purposes (e.g., relocating a pet) requires both an export permit from the country of origin and an import permit from the destination country. Appendix II includes species that could become threatened if trade is not regulated. An export permit is required; import permits vary by country."),
            ("Can I take my parrot to another country?",
             "It depends on the species and its CITES status. Grey parrots (Psittacus erithacus) are CITES Appendix I and require both export and import permits. Many other parrot species are Appendix II and require at minimum an export permit. The permits must be obtained before travel. Applications can take 3-6 months for some species and jurisdictions."),
        ],
        "body": """Most people relocating with dogs and cats do not encounter CITES. But if your companion animal is a parrot, tortoise, chameleon, monitor lizard, iguana, or any other non-domestic species, there is a reasonable chance it is covered by the Convention on International Trade in Endangered Species (CITES) -- and moving it internationally without the right permits is a criminal offence in most countries.

## What CITES Is

CITES is an international treaty with 183 signatory countries. It regulates international trade in specimens of species that are threatened or may become threatened. "Trade" in CITES terms includes non-commercial movement -- relocating your own pet counts.

Species are listed in three appendices:

| Appendix | Status | Permits Required |
|----------|--------|-----------------|
| I | Threatened with extinction | Export permit + import permit (non-commercial) |
| II | Not threatened but regulated | Export permit (import varies by country) |
| III | Locally protected in some countries | Certificate of origin / export permit |

## Common Pet Species That Are CITES-Listed

| Species | CITES Status |
|---------|-------------|
| African Grey Parrot | Appendix I |
| Blue-fronted Amazon | Appendix II |
| Most other Amazon species | Appendix II |
| Eclectus Parrot | Appendix II |
| Cockatoos (most species) | Appendix I or II |
| Hermann's Tortoise | Appendix II |
| Russian Tortoise | Appendix II |
| Spur-thighed Tortoise | Appendix II |
| Chameleons (most species) | Appendix II |
| Monitor Lizards (most species) | Appendix II |
| Ball Python | Appendix II |
| Green Iguana | Appendix II |

## How to Apply for CITES Permits

**Step 1: Confirm your animal's species and CITES status**
- Use the CITES species database at cites.org
- If in doubt about the species identification, get written confirmation from a vet or zoologist

**Step 2: Apply for an export permit from your country of origin**
- UK: APHA CITES team (gov.uk)
- USA: US Fish and Wildlife Service
- EU: National CITES Management Authority of the member state

**Step 3: Obtain an import permit from the destination country**
- Required for Appendix I species
- Optional but often required in practice for Appendix II

**Step 4: Carry original permits with you**
- CITES permits must be originals; photocopies are not accepted at border inspection

## Application Timelines

CITES permit applications take **3-6 months** for Appendix I species in some jurisdictions. Start early. Applications require documentation of legal acquisition -- captive breeding certificates, original purchase receipts, and in some cases DNA testing or ring numbers.

## If You Do Not Have a Permit

Attempting to move a CITES-listed species across an international border without permits can result in:
- The animal being confiscated
- Criminal prosecution
- Significant fines

Do not improvise or assume permits are not needed. Check first.

---

*Sources: CITES official website (cites.org); APHA CITES permit guidance; US Fish and Wildlife Service CITES import/export information. Data current as of June 2026.*""",
    },
    {
        "slug": "usda-aphis-endorsement-guide",
        "title": "USDA APHIS Endorsement: How to Get Your Pet's Health Certificate Authenticated for Export",
        "description": "US pet owners need USDA APHIS to endorse their pet's health certificate before most international journeys. Step-by-step guide to the accredited vet, APHIS endorsement process, and timelines.",
        "date": "2026-06-09",
        "tags": ["usa", "health-certificates", "usda-aphis", "planning"],
        "faqs": [
            ("What is USDA APHIS endorsement?",
             "USDA APHIS (Animal and Plant Health Inspection Service) is the US government authority that authenticates veterinary health certificates for export. After a USDA-accredited veterinarian signs the health certificate, APHIS must countersign (endorse) it before the document is accepted by most foreign governments. Without APHIS endorsement, the health certificate is not a valid export document for international pet travel from the USA."),
            ("How long does USDA APHIS endorsement take?",
             "USDA APHIS endorsement via postal submission takes 2-5 business days. In-person submission at a USDA APHIS Veterinary Services office is often same-day or next-day. For urgent travel, find the nearest APHIS VS office and attend in person. Allow at least 7-10 business days total (vet appointment + endorsement + delivery) if using mail."),
            ("Does my vet need to be USDA-accredited to sign a health certificate for export?",
             "Yes. Health certificates for international pet export from the USA must be signed by a USDA-accredited veterinarian. An accredited vet has completed USDA training and is registered with APHIS. Not all vets are accredited. Use the USDA APHIS Vet Locator at aphis.usda.gov to find one near you."),
        ],
        "body": """Every dog, cat, or other pet leaving the USA for an international destination needs a health certificate signed by a USDA-accredited veterinarian and then endorsed (countersigned) by USDA APHIS. Without the APHIS endorsement stamp, the health certificate is not accepted as an official government document in most countries.

## The Two-Step Process

### Step 1: USDA-Accredited Veterinarian

The health certificate must be signed by a vet who is **USDA-accredited**. This is separate from general veterinary licensing -- it requires completion of USDA training and registration with APHIS.

Find an accredited vet at: **aphis.usda.gov** (USDA APHIS Vet Search Tool)

The vet must:
- Complete the health certificate in the format required by the destination country
- Sign and date the form
- Include their accreditation number

Some destination countries have specific form requirements -- Australia, the EU, Japan, and the UK each have their own required certificate format. The USDA provides these on the APHIS website.

### Step 2: USDA APHIS Endorsement

Once the vet signs the certificate, it must be submitted to USDA APHIS Veterinary Services for endorsement (countersignature).

**Options:**
- **In-person at an APHIS VS office:** Same-day or next-day. Find your nearest office at aphis.usda.gov/VS.
- **Mail-in submission:** 2-5 business days processing. You must include a prepaid return envelope.

APHIS charges an endorsement fee (currently USD 38 per certificate as of 2026 -- check current fee schedule).

**Important:** Health certificates have a validity window -- typically 10 days from the date of the vet examination. APHIS endorsement must happen within this window. Plan your vet appointment timing carefully around APHIS processing time.

## Country-Specific Requirements

Different destination countries have different form requirements:

| Destination | Form/Process |
|-------------|-------------|
| EU | APHIS 7001 (for commercial); country-specific form for private pets |
| Australia | DAFF-specific form; APHIS endorses after vet sign-off |
| UK | UK-specific form (APHA-required format) |
| Japan | MAFF-specific format; APHIS endorses |
| Canada | Health certificate to CFIA format |

Download the required destination country form from the APHIS website before your vet appointment.

## Timeline Summary

| Step | Time Required |
|------|--------------|
| Book USDA-accredited vet | 1-2 weeks lead time for appointment |
| Vet examination and certificate | Same day |
| APHIS endorsement (in-person) | Same or next day |
| APHIS endorsement (mail) | 2-5 business days |
| **Total minimum** | **4-8 business days before departure** |

Allow more time. Last-minute health certificate problems are one of the most common causes of missed flights for pets from the USA.

---

*Sources: USDA APHIS Veterinary Services official guidance; APHIS VS endorsement fee schedule 2026. Data current as of June 2026.*""",
    },
    {
        "slug": "eu-pet-passport-guide",
        "title": "The EU Pet Passport Explained: What It Is, Who Needs It, and What Changed After Brexit",
        "description": "The EU pet passport is a standardised travel document for pets moving between EU member states. Who it applies to, what it replaced, and why UK pet owners can no longer use one.",
        "date": "2026-06-11",
        "tags": ["eu", "pet-passport", "planning", "brexit"],
        "faqs": [
            ("Can I still use an EU pet passport issued in the UK?",
             "No. EU pet passports issued by UK veterinarians are no longer valid for travel between the UK and EU member states. Since Brexit, UK-issued EU pet passports are not recognised by EU border controls. UK pets travelling to EU countries need an Animal Health Certificate (AHC) for each journey."),
            ("If I have moved to an EU country, can I get a new EU pet passport there?",
             "Yes. If you and your pet are resident in an EU member state, a licensed vet in that country can issue an EU pet passport for your pet. This passport is then valid for travel between EU member states. It is not valid for entry into the UK without the correct UK APHA documentation."),
            ("Is an EU pet passport required for travel within the EU?",
             "EU pet passports are the standard document for pet travel between EU member states, but technically a health certificate is also accepted. In practice, all pet owners resident in the EU should have an EU pet passport issued by their country's licensed vet as the primary travel document."),
        ],
        "body": """The EU pet passport was introduced in 2004 to create a standardised, lifetime travel document for dogs, cats, and ferrets moving between European Union member states. Before 2021, it was used by UK pet owners for European travel. Since Brexit, that has changed -- and the confusion persists.

## What the EU Pet Passport Contains

An EU pet passport is a small blue booklet issued by a licensed vet in an EU member state. It contains:
- Owner's details
- Animal description and photograph
- Microchip number and implantation date
- Vaccination records (rabies and other vaccines)
- Parasite treatment records
- Vet's certification of health status
- Space for ongoing treatment records

The passport stays with the animal for its lifetime and is updated by vets at each vaccination.

## Who Uses an EU Pet Passport

EU pet passports are valid for:
- **Travel between EU member states** (and EEA countries that have adopted the scheme: Norway, Iceland, Liechtenstein)
- **Re-entry into the EU** from qualifying third countries for resident pets (with additional documentation)

## The Brexit Change

Before 1 January 2021, EU pet passports were issued in the UK by UK vets. UK pets had EU pet passports for European travel.

After Brexit, UK-issued EU passports are no longer valid. The UK left the EU pet passport system. UK border controls do not recognise EU pet passports for animals entering the UK without additional documentation. EU border controls do not recognise UK-issued EU pet passports for animals entering from the UK.

**What UK owners need now:** An **Animal Health Certificate (AHC)** for each trip to an EU country, issued by an Official Veterinarian within 10 days of travel.

## Getting an EU Pet Passport if You Move to the EU

If you have relocated to an EU member state with your pet, a licensed vet in your new country can issue an EU pet passport for the animal once it is resident there. This new passport, issued by an EU vet, is valid for travel within the EU.

It is not valid for travel into the UK, which has its own documentation requirements.

## Comparison Table

| Situation | Document Needed |
|-----------|----------------|
| UK pet travelling to EU | AHC (per journey) |
| EU pet travelling within EU | EU pet passport |
| EU pet entering UK | UK APHA health certificate (post-Brexit) |
| Non-EU pet entering EU | EU-specific health certificate endorsed by origin government |

---

*Sources: European Commission pet travel regulations (EU Regulation 576/2013); UK APHA Brexit pet travel guidance. Data current as of June 2026.*""",
    },
    {
        "slug": "moving-pets-non-eu-to-eu",
        "title": "Moving Pets to the EU from Outside Europe: The Health Certificate Process",
        "description": "Bringing a pet into the EU from the USA, Australia, UAE, or any non-EU country requires a specific health certificate format. What the EU requires, approved countries, and how the process works.",
        "date": "2026-06-11",
        "tags": ["eu", "planning", "health-certificates", "regulations"],
        "faqs": [
            ("What do I need to bring a dog to the EU from the USA?",
             "A dog from the USA needs an ISO microchip, current rabies vaccination, and a health certificate in the EU-approved format signed by a USDA-accredited vet and endorsed by USDA APHIS. The USA is classified as an unlisted third country for EU pet entry purposes -- slightly more complex than listed countries like the UK, but straightforward with correct documentation."),
            ("Does an Australian pet need a titre test to enter the EU?",
             "No. Australia is classified by the EU as a listed third country with a recognised disease-free status for rabies. Pets from Australia entering the EU need microchip, current rabies vaccination, and an EU-format health certificate endorsed by the Australian competent authority (DAFF). No titre test is required for EU entry."),
            ("Can I bring my pet into any EU country at any entry point?",
             "No. Live animals must enter the EU at an approved Border Inspection Post (BIP). Not every airport has a BIP for live animals. Check the EU TRACES system for BIPs approved for your species before booking. Major approved BIPs for pets include: Amsterdam Schiphol, Frankfurt, Paris CDG, Madrid Barajas, Brussels Zaventem, Helsinki Vantaa."),
        ],
        "body": """Moving a pet into the European Union from a country outside the EU requires a health certificate in a specific EU-approved format. The exact requirements depend on where you are coming from -- the EU classifies origin countries into different categories that determine how much documentation you need.

## How the EU Classifies Origin Countries

The EU divides third countries (non-EU) into three groups for live animal movement:

| Classification | Examples | Requirements |
|----------------|----------|-------------|
| Listed (favourable) | UK, Australia, USA, Canada, NZ, Japan, Singapore | Standard health certificate + microchip + rabies vacc |
| Unlisted | Most other countries | Additional requirements -- may include titre test |
| Countries with special status | Some specific list variations | Check TRACES |

The full current list is maintained on the European Commission's website and updated periodically.

## The Health Certificate Requirement

All pets entering the EU from outside need an EU-format health certificate:
- Signed by an official or government-accredited vet in the origin country
- Endorsed by the competent authority (USDA APHIS for USA, DAFF for Australia, APHA for UK, etc.)
- Issued within 10 days of travel (some forms have different validity windows -- check)
- In the format prescribed by EU Commission Implementing Regulation 577/2013

Download the current format from the EU TRACES system or your country's animal health authority website.

## Arriving at a Border Inspection Post (BIP)

Live animals entering the EU must arrive at an approved BIP. Documentary and identity checks are mandatory. Physical checks are conducted on a risk basis.

**Major BIPs for pets:**
- Amsterdam Schiphol (AMS)
- Frankfurt Airport (FRA)
- Paris Charles de Gaulle (CDG)
- Madrid Barajas (MAD)
- Brussels Zaventem (BRU)
- Helsinki Vantaa (HEL)

Plan your routing through one of these airports. Arriving at a non-BIP airport will result in your pet being refused entry or held.

## Costs Involved

| Item | Estimated Cost |
|------|----------------|
| Government health certificate (USA) | USD 200-400 including vet and APHIS endorsement |
| Government health certificate (UK) | GBP 150-350 including OV and APHA endorsement |
| BIP inspection fee | EUR 30-100 varies by EU member state |
| Airline cargo | Varies by route and animal size |

---

*Sources: EU Commission Implementing Regulation 577/2013; EU TRACES portal; USDA APHIS export health certificate programme. Data current as of June 2026.*""",
    },
    {
        "slug": "uk-to-spain-pet-transport-complete-guide",
        "title": "UK to Spain Pet Transport: Step-by-Step Guide for Dogs and Cats Post-Brexit",
        "description": "Moving your dog or cat from the UK to Spain after Brexit. Animal Health Certificate process, breed restrictions, airline options, and what to expect at Spanish border inspection.",
        "date": "2026-06-13",
        "tags": ["uk", "spain", "routes", "planning"],
        "faqs": [
            ("Do I need a new Animal Health Certificate every time I travel between the UK and Spain?",
             "Yes. An AHC is required for each journey from the UK to Spain and must be issued by an Official Veterinarian within 10 days of travel. It is valid for that trip and for travel within the EU for 4 months. If you make regular trips, you need a new AHC each time you re-enter the EU from the UK."),
            ("Can I take my dog to Spain by road via Eurotunnel or ferry?",
             "Yes. Pets can travel to Spain via Eurotunnel (Folkestone to Calais) or ferry routes (Portsmouth to Bilbao or Santander; Plymouth to Santander). All routes require the same Animal Health Certificate documentation. Some ferry routes allow pets to remain in vehicles in the hold or in on-board kennels."),
            ("Does my dog need the echinococcus tapeworm treatment to enter Spain?",
             "No. Spain does not require the Echinococcus tapeworm treatment. The tapeworm treatment is required only for entry into Finland, Ireland, Malta, Norway, and the UK. Spain follows standard EU rules: microchip, current rabies vaccination, and AHC."),
        ],
        "body": """Spain is the top destination for UK expats. Hundreds of thousands of British citizens live there, and tens of thousands more make regular visits. Moving a dog or cat to Spain from the UK is well-documented, straightforward in the steps -- but it catches people out if they are not aware of the post-Brexit documentation changes.

## The Post-Brexit Baseline

Before January 2021: UK pets used EU pet passports for Spain travel.
Since January 2021: UK pets need an **Animal Health Certificate (AHC)** for each journey.

The AHC is a legal government document. It replaces the EU pet passport for each trip.

## Step-by-Step: UK to Spain

**Step 1 (weeks-months before): Confirm microchip and vaccination**
- ISO 15-digit microchip in place
- Rabies vaccination current (within manufacturer's stated validity period -- typically 1 or 3 years)

**Step 2 (2-4 weeks before): Book OV appointment**
- Find an Official Veterinarian (OV) registered with APHA
- Book an appointment that falls within 10 days of your travel date
- OVs get booked up -- book as soon as you have confirmed travel dates

**Step 3 (within 10 days of travel): OV examination and AHC**
- OV examines the pet
- OV completes and signs the AHC
- Some AHC formats require APHA endorsement; others do not -- confirm with your OV

**Step 4: Travel**
- Carry the original AHC (not a copy)
- Declare your pet at the BIP on arrival in Spain
- Present original AHC and allow the vet to scan the microchip

## Travel Routes: UK to Spain

| Route | Notes |
|-------|-------|
| Direct flight (London to Madrid/Barcelona/Malaga) | Most common for relocations; cargo for larger dogs |
| Ferry (Portsmouth/Plymouth to Santander or Bilbao) | Popular for multiple pets or large dogs; 24-36 hour crossing |
| Eurotunnel + drive | Train through tunnel + drive south through France and Spain |

## Spanish Breed Restrictions (PPP)

Spain's PPP (Perros Potencialmente Peligrosos) classification covers breeds including Pit Bulls, American Staffs, Rottweilers, Dogo Argentino, and others. These breeds can be imported but require:
- Owner licence (obtained in Spain)
- Third-party liability insurance
- Muzzle and short lead in public

This affects conditions of ownership in Spain, not the import itself.

## Cost Estimate

| Item | Cost |
|------|------|
| OV appointment and AHC | GBP 150-250 |
| Airline cabin fee (small dogs/cats) | GBP 50-200 |
| Airline cargo (larger dogs) | GBP 200-600 |
| Ferry (if applicable) | Variable; pet surcharge GBP 20-50 |

---

*Sources: European Commission Regulation 576/2013; APHA UK pet travel guidance; Spain MAPA import requirements. Data current as of June 2026.*""",
    },
    {
        "slug": "us-to-uk-pet-transport-guide",
        "title": "USA to UK Pet Transport: USDA APHIS, UK APHA Rules, and What the Journey Looks Like",
        "description": "Moving dogs or cats from the United States to the United Kingdom. USDA APHIS health certificate process, UK APHA import requirements, and the full step-by-step guide.",
        "date": "2026-06-13",
        "tags": ["usa", "uk", "routes", "planning"],
        "faqs": [
            ("Does my dog need a titre test to enter the UK from the USA?",
             "No. The UK does not require a rabies antibody titre test for dogs or cats entering from the USA. The USA is classified as a listed third country by the UK, requiring microchip, current rabies vaccination, and a UK-format health certificate signed by a USDA-accredited vet and endorsed by USDA APHIS."),
            ("How long does it take to prepare documentation for USA to UK pet travel?",
             "Allow a minimum of 3-4 weeks: 1-2 weeks to book a USDA-accredited vet appointment, 1-3 business days for USDA APHIS endorsement (in-person), plus time for the 10-day health certificate window. Total minimum to departure: 2 weeks from APHIS endorsement. Build in more if possible."),
            ("Which airlines fly dogs from the USA to the UK?",
             "British Airways, Virgin Atlantic, and United Airlines operate USA to UK routes with cargo pet services. None allows pets in cabin on transatlantic routes. American Airlines accepts pets in-cabin on some US domestic routes but not transatlantic. Book cargo well in advance -- space is limited."),
        ],
        "body": """The USA-to-UK route is one of the world's most common pet relocation journeys. It is manageable with careful preparation and no titre test requirement -- but the USDA APHIS endorsement process is the step that catches most US owners off guard.

## UK Import Requirements for USA Pets

The UK has maintained its EU-aligned pet import framework post-Brexit, with some modifications. For pets from the USA, the UK requires:

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes (or 10-digit chip with scanner record) |
| Rabies vaccination | Current and within validity period |
| UK-format health certificate | Yes -- specific UK APHA format |
| USDA APHIS endorsement | Yes -- required on UK health certificate |

No titre test required. No quarantine required for pets from the USA.

## The Health Certificate Format

The UK does not accept standard USDA form 7001. You need the **UK-specific health certificate format** published by APHA. Your USDA-accredited vet must complete this form (not a generic health certificate).

Download the current UK import health certificate from the APHA website (gov.uk/guidance/pet-travel-and-the-great-britain-pet-travel-scheme).

## Step-by-Step Process

1. **Confirm microchip and vaccination** -- ISO chip, current rabies vaccination within validity
2. **Download the UK APHA health certificate format** from gov.uk
3. **Book USDA-accredited vet appointment** within 10 days of travel (the certificate is valid for 10 days from examination date)
4. **Vet completes UK-format certificate** and signs with accreditation number
5. **Submit to USDA APHIS for endorsement** -- in-person same day; mail 2-5 business days
6. **Book airline cargo** -- British Airways, Virgin Atlantic, or United; advance booking required
7. **Travel and declare at UK BIP** on arrival (typically Heathrow)

## Arriving at Heathrow

Most USA-UK flights arrive at London Heathrow (LHR). The border inspection post for live animals is in the World Cargo area (not the passenger terminal). Declare your pet on the Advance Passenger Information or notify your airline.

Cargo pets are released by the BIP after documentary and identity checks. Allow 2-4 hours for cargo clearance.

## Airlines for USA to UK

| Airline | Cargo policy | Notes |
|---------|-------------|-------|
| British Airways | Cargo | No in-cabin pets on transatlantic |
| Virgin Atlantic | Cargo | Check current live animal policy |
| United Airlines | Cargo | PetSafe programme |
| American Airlines | Cargo | ACargo programme |

---

*Sources: APHA UK pet import requirements for third countries; USDA APHIS health certificate endorsement guidance. Data current as of June 2026.*""",
    },
    {
        "slug": "expat-pet-relocation-checklist",
        "title": "The Complete Expat Pet Relocation Checklist: Everything in the Right Order",
        "description": "A month-by-month, step-by-step checklist for expats moving internationally with pets. From 9 months before departure to arrival day, nothing gets missed.",
        "date": "2026-06-15",
        "tags": ["planning", "checklist", "expats"],
        "faqs": [
            ("When should I start planning my pet's international move?",
             "For most countries: 8-12 weeks before departure. For Australia, New Zealand, or Japan: 8-10 months before departure (titre test waiting periods make early planning essential). As a rule, start planning earlier than feels necessary -- last-minute pet transport problems are stressful and sometimes unsolvable."),
            ("What is the most common mistake expats make when relocating pets?",
             "Missing the health certificate timing window. Health certificates are typically valid for only 10 days from the date of examination. If you get the certificate too early, it expires before you travel. If you leave it too late, the vet cannot get an appointment. Book the OV appointment within your travel window and plan backward from there."),
            ("Should I use a pet transport agent for an expat move?",
             "For complex routes (quarantine destinations, breed-restricted countries, multiple connections, large animals), a specialist IPATA-member agent significantly reduces the chance of costly errors. For simple routes (UK to EU, USA to Canada), confident owners can self-manage with careful research."),
        ],
        "body": """Moving abroad with a pet requires parallel planning tracks: the animal's documentation track, the logistics track, and the destination track. This checklist organises everything in order so nothing is left to the last minute.

## 9-12 Months Before (For Australia / New Zealand / Japan Only)

- [ ] Confirm ISO 15-digit microchip in place (must predate first recorded vaccination)
- [ ] Administer rabies vaccination
- [ ] Book blood draw for rabies titre test with DAFF/MPI-approved lab
- [ ] Send blood sample; wait for titre result (2-3 weeks)
- [ ] Confirm titre result meets minimum threshold
- [ ] Record the 180-day countdown from titre confirmation date

## 3-6 Months Before (All Countries)

- [ ] Confirm destination country's current import rules (official government source)
- [ ] Check if breed is restricted at destination
- [ ] Determine if import permit is required (Middle East, Africa, Asia-Pacific: usually yes)
- [ ] Apply for import permit if required (allow 4-6 weeks)
- [ ] Research airlines flying the route with cargo/cabin pet policies
- [ ] Identify IPATA-member agent if using one
- [ ] Purchase IATA-compliant crate and begin crate training

## 6-8 Weeks Before

- [ ] Book airline cargo space (specifying species, breed, crate dimensions, weight)
- [ ] Confirm import permit received (if applicable)
- [ ] Check if pet needs additional vaccinations or treatments (leishmania, rabies booster, etc.)
- [ ] Book Official Veterinarian (OV) appointment for health certificate -- within 10 days of travel date

## 2-3 Weeks Before

- [ ] Confirm OV appointment is within 10-day validity window before travel
- [ ] Download the correct health certificate format for your destination country
- [ ] Check APHA or USDA APHIS endorsement timing if required
- [ ] Arrange pet's arrival logistics at destination (quarantine booking, ground transport)

## 10 Days Before: Health Certificate Window

- [ ] OV examination
- [ ] OV completes and signs health certificate in correct format
- [ ] Submit for government endorsement if required (APHA / USDA APHIS)
- [ ] Confirm endorsement received before departure

## 1 Week Before

- [ ] Confirm cargo booking with airline (repeat confirmation)
- [ ] Prepare crate: clean bedding, frozen water dish, worn clothing item, food/water holders
- [ ] Label crate with "Live Animal" stickers and directional arrows
- [ ] Pack all original documents in travel folder: health certificate, microchip scan record, vaccination record, import permit, titre test certificate if applicable
- [ ] Do not feed pet within 4 hours of scheduled flight departure

## Travel Day

- [ ] Exercise pet before departure
- [ ] Check in for cargo per airline's instructions (often 3-4 hours before departure)
- [ ] Do not leave until you have confirmed the pet is accepted by the cargo team
- [ ] Keep contact details for destination agent, quarantine facility, and airline cargo team

## On Arrival

- [ ] Declare pet at border inspection post (BIP) with original documents
- [ ] Present documents and allow microchip scan
- [ ] For quarantine destinations: transfer to approved facility
- [ ] For non-quarantine destinations: collect pet from cargo facility after clearance

---

*Sources: IATA Live Animals Regulations 2024; APHA UK pet travel guidance; USDA APHIS export guidance; DAFF Australia. Data current as of June 2026.*""",
    },
    {
        "slug": "moving-with-rabbits-internationally",
        "title": "Moving with Rabbits Internationally: Import Rules, Airline Restrictions, and Country Bans",
        "description": "International rabbit transport is more complex than dogs or cats. Import bans in some countries, cabin-only options on few airlines, and VHD vaccination requirements -- what owners need to know.",
        "date": "2026-06-15",
        "tags": ["rabbits", "exotic-pets", "planning", "regulations"],
        "faqs": [
            ("Can rabbits fly in the cabin on international flights?",
             "Only a small number of airlines accept rabbits in the cabin, and most restrict it to domestic routes. For international travel, most rabbits travel as cargo or checked baggage. Airlines with some acceptance of rabbits in cabin for domestic US flights include United and American, but international cabin acceptance is rare. Contact your airline directly."),
            ("Which countries ban rabbit imports?",
             "Australia and New Zealand have very strict rabbit import rules -- they are prohibited for most categories of entry due to biosecurity concerns (rabbits are a significant invasive pest). The UK, EU, USA, Canada, and most other destinations accept pet rabbits with appropriate documentation."),
            ("Do rabbits need a health certificate for international travel?",
             "Yes. Most countries require a government-endorsed health certificate for rabbit imports. Some also require a specific import permit. Requirements vary significantly by destination -- check the official government source for your destination country."),
        ],
        "body": """Rabbits are the world's third most popular pet, yet international travel with a rabbit involves rules that surprise most owners. Unlike dogs and cats, where a standardised framework applies, rabbit import varies enormously by destination.

## The Core Challenge: Country Rules Vary Widely

Dogs and cats have reasonably standardised international frameworks. Rabbits do not. Some countries treat rabbits as standard companion animals. Others classify them as livestock. A few ban them for biosecurity reasons.

**Before planning any international move with a rabbit, check the destination country's specific rules. Do not assume the rules are the same as for dogs.**

## Countries with Restrictions or Bans

| Country | Status |
|---------|--------|
| Australia | Import prohibited for pet rabbits (extreme biosecurity concern) |
| New Zealand | Prohibited; only allowed under strict scientific/biosecurity permits |
| UK | Permitted; health certificate required; specific format |
| EU | Permitted; health certificate required |
| USA | Permitted; no federal import restrictions for domestic rabbits |
| Canada | Permitted; health certificate required |
| Japan | Permitted; quarantine inspection on arrival |
| Singapore | Permitted with AVS import licence |
| UAE | Check with Ministry of Climate Change and Environment |

## What Documents Does a Rabbit Need?

For most countries that permit rabbit imports:
- **Microchip:** Not all rabbits are microchipped; some countries require it. Implantation by a vet is straightforward.
- **Health certificate:** Issued by accredited vet, endorsed by government authority (APHA for UK, USDA APHIS for USA)
- **VHD vaccination record:** Viral Haemorrhagic Disease vaccination (VHD1 and VHD2) is not universally required but is recommended and required by some destinations
- **Import permit:** Required by some destinations (Middle East, Singapore, Japan)

## Which Airlines Accept Rabbits?

Most major airlines accept rabbits as checked baggage or cargo. In-cabin acceptance is rare for international routes. Airlines commonly accepting rabbits in cargo: KLM, Lufthansa, Air France, United PetSafe. Always confirm directly with the airline.

Rabbits are sensitive to temperature extremes and stress. Avoid summer cargo embargoes and minimise connection time.

## The Australia and New Zealand Situation

Australia and New Zealand classify rabbits as significant invasive pest species. Importation of live rabbits as pets is **prohibited**. There are no exemptions for pet rabbits. If you are moving to Australia or New Zealand with a pet rabbit, you will need to rehome or care for the animal before you leave.

---

*Sources: Australian Department of Agriculture biosecurity guidance on rabbits; MPI New Zealand prohibited goods list; APHA UK rabbit import requirements. Data current as of June 2026.*""",
    },
    {
        "slug": "pet-transport-military-families",
        "title": "Pet Transport for Military Families: PCS Moves, Orders-Based Relocation, and Overseas Posts",
        "description": "Military families face unique pet transport challenges: tight PCS timelines, government travel restrictions, quarantine at overseas posts, and navigating airline policies on short notice.",
        "date": "2026-06-17",
        "tags": ["military", "planning", "pcs", "advice"],
        "faqs": [
            ("Will the military pay for my pet to move during a PCS?",
             "In most cases, no. The US military does not officially reimburse pet transport costs as part of a PCS move. However, some families have successfully included pet transport in their household goods weight allowance for crates. OCONUS assignments may have base-specific guidance. Check with your Transportation Office (TO) for current policy."),
            ("Can I bring any breed of dog to an overseas military post?",
             "Not necessarily. OCONUS military installations have their own pet policies, which often include breed restrictions more restrictive than the host nation's civilian rules. Common installation breed restrictions include Pit Bull types, Rottweilers, and other breeds classified as dangerous. Check with the housing office at your specific installation before travel."),
            ("What is the fastest way to get a pet health certificate for a sudden PCS?",
             "Contact a USDA-accredited vet immediately and explain the PCS timeline. For USDA APHIS endorsement, in-person submission to an APHIS VS office is the fastest option (same-day or next-day). Identify your nearest APHIS VS office via aphis.usda.gov. IPATA-member pet transport agents often have established relationships with APHIS offices and can expedite."),
        ],
        "body": """Military families face some of the most demanding pet transport scenarios: PCS (Permanent Change of Station) timelines driven by orders rather than preference, OCONUS posts in countries with strict animal import requirements, and the need to navigate military installation pet policies alongside host-nation civilian rules.

## The PCS Timeline Problem

Civilian pet transport can be planned months in advance. PCS orders often arrive with 6-8 weeks to report. For OCONUS assignments to countries with complex import requirements (South Korea, Germany, Japan, Italy, Spain), 6-8 weeks may barely be enough for standard documentation -- and nothing like enough for Australia, Japan, or New Zealand.

If you have any chance of receiving OCONUS orders to quarantine-required destinations, start the documentation process as soon as you become eligible for a PCS -- before orders arrive.

## Documentation Under Time Pressure

For most OCONUS posts (Germany, UK, Italy, Spain, South Korea, Japan):
- Microchip and current vaccinations: these should be maintained at all times
- Health certificate: must be issued within 10 days of travel; the tight window is standard
- Government endorsement (USDA APHIS): in-person visit to APHIS VS office for same-day or next-day turnaround is essential for short-notice PCS
- Import permit where required: this is the element that cannot be rushed in countries that require advance permits

## Military Installation Breed Restrictions

OCONUS military installations enforce their own pet policies, which override local civilian rules in many cases. Typical installation restrictions include:

| Breed Category | Typical Restriction |
|----------------|---------------------|
| Pit Bull type | Banned from most US military installations OCONUS |
| Rottweiler | Banned or restricted at many installations |
| Dobermann | Restricted at some installations |
| Mixed breeds with visible restricted traits | May be assessed individually |

These restrictions affect **housing eligibility**. A restricted breed may clear customs into the host country but may not be permitted to live in government quarters.

## Germany (USAREUR)

Germany is one of the most common OCONUS assignments. AERS (Army Europe Regional Support) has specific pet registration requirements for pets on the installation. Germany itself has state-level breed restrictions. Check with your gaining unit's Housing Office.

## Japan (USFJ)

Japan has very strict national pet import requirements (titre test, waiting period, quarantine). USFJ installations follow Japanese national rules. For a PCS to Japan, the preparation timeline typically requires 6+ months. Request information from the gaining installation's veterinary unit well before departure.

## Using an IPATA Agent for Military Moves

Several IPATA-member agents specialise in military relocations and are familiar with OCONUS documentation, APHIS expedite processes, and installation-specific requirements. The cost of an agent may be recoverable through command welfare funds in some circumstances -- check with your unit.

---

*Sources: USDA APHIS PCS pet transport guidance; USFJ pet import requirements; USAREUR AERS housing pet policy. Data current as of June 2026.*""",
    },
    {
        "slug": "travelling-with-rescue-dogs-internationally",
        "title": "Travelling with Rescue Dogs Internationally: Documentation Gaps and How to Fill Them",
        "description": "Rescue dogs often have incomplete vaccination histories, unknown microchip status, and questionable paperwork. How to travel internationally with a rescue dog and navigate the documentation challenges.",
        "date": "2026-06-17",
        "tags": ["dogs", "rescue", "planning", "health-certificates"],
        "faqs": [
            ("Can I take a recently adopted rescue dog abroad if its vaccination history is unclear?",
             "Yes, but you need to restart the clock. If the dog has no verifiable vaccination history, a vet will administer a rabies vaccination (after confirming microchip), and the 30-day waiting period (minimum) starts from there for most countries. For countries requiring titre tests (Australia, NZ, Japan), the full 6+ month process begins at the vaccination date."),
            ("What happens if my rescue dog has a non-ISO microchip?",
             "Most international travel requires an ISO 15-digit microchip. If your rescue dog has a 10-digit chip, you have two options: implant a second ISO chip (common practice) or travel with a universal reader to confirm the chip reads. The second chip does not require removing the old one. Vaccination dates recorded before the new chip was implanted are counted from the new chip date for documentation purposes."),
            ("Can I move a rescue dog from Spain to the UK?",
             "Yes. A rescue dog from Spain entering the UK needs: ISO microchip, current rabies vaccination, and a UK-format health certificate issued by a Spanish OV and endorsed by the Spanish competent authority (MAPA). The UK also requires tapeworm treatment within 1-5 days of travel. No titre test, no quarantine."),
        ],
        "body": """Rescue dogs bring their own complications to international travel. Vaccinations administered in a shelter may have no paperwork. The microchip may be a non-standard chip, or missing entirely. Previous owners may have no documentation. None of this is insurmountable -- it just needs to be addressed honestly and systematically.

## Step 1: Establish the Animal's Baseline

Before planning any travel, visit a vet for a complete assessment:
- **Microchip check:** Scan for existing chip. If 10-digit or non-ISO: implant a new ISO 15-digit chip
- **Vaccination status:** If history is uncertain, treat the animal as unvaccinated and start the schedule fresh
- **Health status:** Confirm the dog is healthy and fit to fly

Document everything from this baseline appointment. This is the foundation of all travel documentation.

## Step 2: The Vaccination Restart Problem

For countries that require only a current rabies vaccination (most of Europe, USA, Canada, Middle East), a fresh vaccination + 30-day wait is usually sufficient to begin the travel documentation process.

For countries requiring titre tests (Australia, New Zealand, Japan):
- Vaccination must be administered after microchip implantation
- A titre test blood sample can be taken at or after 30 days post-vaccination
- 180 days after titre confirmation = earliest entry date

If you adopted a rescue dog today and want to move to Australia, you are looking at a minimum 7-9 month wait.

## International Rescue Adoptions

Many people adopt dogs from rescue organisations while living or travelling abroad -- particularly in southern Europe (Spain, Portugal, Greece, Romania), Southeast Asia, and Latin America. Moving the dog back to the UK, USA, or other strict-entry destinations requires careful planning.

**Common rescue adoption routes:**
- Greece to UK: AHC required, no titre test, tapeworm treatment
- Romania to UK: Same; note that Romanian paperwork quality varies -- verify every document
- Spain to UK: AHC required, tapeworm treatment, no titre test
- Thailand to Australia: Full titre test process + 10-day quarantine at Mickleham

## Breed Identification

Some rescue dogs are of uncertain breed. For destinations with breed restrictions (UK's XL Bully restrictions, German state laws, Middle East Pit Bull bans), a vet-issued breed assessment letter can be helpful at the border. A DNA test (Embark, Wisdom Panel) providing a breed breakdown adds an additional layer of documentation for ambiguous cases.

---

*Sources: APHA UK rescue dog import requirements; DAFF Australia pet import requirements. Data current as of June 2026.*""",
    },
    {
        "slug": "customs-declarations-for-pets",
        "title": "Customs Declarations When Travelling with Pets: What You Actually Need to Declare",
        "description": "Do you need to declare your pet at customs? What the rules are for pet food, medications, and accessories when crossing international borders with animals.",
        "date": "2026-06-19",
        "tags": ["customs", "planning", "regulations"],
        "faqs": [
            ("Do I need to declare my pet at customs when entering a country?",
             "Yes. In virtually all countries, live animals must be declared to customs and the veterinary border authority. Failure to declare a pet is a customs offence. In most countries the correct channel is the red channel or a dedicated live animal inspection point. Do not take a pet through the green nothing to declare channel."),
            ("Can I bring pet food into another country?",
             "It depends. Within the EU, pet food moves freely. Into the UK from the EU or third countries, commercial pet food is generally permitted. Into Australia, New Zealand, and USA, plant-based and meat-based pet food may require inspection or be prohibited if it contains restricted ingredients. Sealed commercial pet food is generally lower risk than homemade food. Check the specific rules."),
            ("Can I bring my pet's prescription medications across an international border?",
             "Yes, for personal use quantities with a valid veterinary prescription. Most countries permit a reasonable quantity of prescribed medication for a pet you are travelling with. Carry the original prescription and packaging. Controlled substances require additional documentation. Check the destination's veterinary drug import rules for specific medications."),
        ],
        "body": """Crossing an international border with a pet raises questions beyond just the animal's health certificate. What about the pet food in your bag? The flea treatment? The month's supply of prescription medication? This guide covers the customs side of international pet travel.

## Declaring the Animal

When you arrive at a border with a pet, you must declare it. The mechanism varies:
- **Airport arrivals:** Use the red channel or the live animal inspection point (BIP for EU/UK arrivals). Do not use the nothing to declare (green) channel.
- **Land borders:** Declare at the veterinary checkpoint; some borders have dedicated live animal lanes
- **Ferry arrivals:** Most ferry operators require pets to be registered at check-in; customs inspection on arrival

**Failure to declare a pet is a customs and animal health offence in most jurisdictions.** Penalties range from fines to animal confiscation.

## Pet Food: What Can You Bring?

| Destination | Rules |
|-------------|-------|
| EU | No restrictions on commercial pet food within EU; strict rules on import from outside EU |
| UK | Commercial pet food permitted in sensible personal quantities; raw/fresh meat products restricted |
| Australia | Strict biosecurity; sealed commercial pet food usually permitted; raw/fresh/dried meat: prohibited or needs inspection |
| New Zealand | Similar to Australia; sealed commercial pet food usually permitted; raw: prohibited |
| USA | Commercial sealed pet food: generally permitted; homemade or raw: may be inspected |

When in doubt: carry sealed commercial pet food with the original packaging and ingredient list.

## Medications

For travelling with a pet's prescription medication:
- Carry the original packaging
- Carry a copy of the veterinary prescription
- Carry a letter from your vet explaining the medication and why it is prescribed
- Declare medications with customs if amounts are above normal personal-use quantities

Most countries permit a reasonable supply (4-8 weeks) of a pet's prescribed medication. For longer stays, establish a relationship with a vet at the destination.

Controlled substances (some pain medications, sedatives) require additional documentation and may require a special import permit. Research the destination country's veterinary drug regulations before travel.

## Travelling with Pet Accessories

CITES-listed materials -- certain leather goods, feathers, fur -- can cause customs issues even when part of a pet accessory (a collar made with exotic leather, for example). Check CITES regulations if your pet's accessories contain unusual materials.

---

*Sources: APHA UK import restrictions; Australian DAFF biosecurity guidance; EU animal product import rules. Data current as of June 2026.*""",
    },
    {
        "slug": "france-to-australia-pet-transport-guide",
        "title": "France to Australia Pet Transport: The Titre Test, DAFF Requirements, and Air Routes",
        "description": "Moving a dog or cat from France to Australia. DAFF entry requirements, rabies titre test process from France, approved labs, Mickleham quarantine, and airline options from Paris.",
        "date": "2026-06-19",
        "tags": ["france", "australia", "routes", "planning"],
        "faqs": [
            ("Does France count as a listed or unlisted country for Australia pet entry?",
             "France is a listed country for Australian pet entry purposes. Pets from listed countries undergo the standard titre test and documentation process without additional restrictions."),
            ("Which French laboratories are approved by DAFF for the rabies titre test?",
             "France has several DAFF-approved laboratories for rabies titre testing, including ANSES (Agence Nationale de Securite Sanitaire) at Nancy-Malzeville. Your French vet will send the blood sample to an approved lab. Confirm your chosen lab is currently on the DAFF approved list before proceeding."),
            ("Which airlines fly dogs from Paris to Australia?",
             "Direct routes from Paris (CDG) to Australia are limited. Qantas flies CDG to Sydney via Singapore; Air France/KLM operates connections via Amsterdam and Asian hubs. Singapore Airlines cargo handles live animals on some connections. Plan the routing carefully -- each connection adds risk and documentation scrutiny."),
        ],
        "body": """Moving from France to Australia with a dog or cat is one of the longer processes in international pet transport. Australia's rabies-free biosecurity status means every arriving animal must prove it has been adequately vaccinated -- not just jabbed, but confirmed by blood test. Then there is mandatory quarantine.

## Australia's Core Requirements (from France)

France is a **listed country** for DAFF (Department of Agriculture, Fisheries and Forestry) purposes. This means the standard pathway applies:

1. ISO microchip in place before first recorded vaccination
2. Rabies vaccination
3. Titre test blood sample sent to DAFF-approved lab; result must be ≥0.5 IU/mL
4. **180-day wait** from the date DAFF confirms the satisfactory titre result
5. Government-endorsed health certificate (DAFF format) issued within the DAFF-specified validity window before travel
6. **10-day mandatory quarantine** at Mickleham Quarantine Facility (Melbourne) on arrival

Total preparation timeline: minimum **8 months** from starting the titre test process.

## The French Titre Test Process

Step by step from France:
1. Book a vet appointment for the blood draw
2. Vet sends sample to an ANSES-approved or DAFF-listed laboratory in France
3. Await titre result (2-4 weeks)
4. Confirm result meets the ≥0.5 IU/mL threshold
5. The 180-day clock starts from the laboratory confirmation date (not the blood draw date)

**Important:** Keep vaccinations current throughout the 180-day wait. A lapsed vaccination restarts the process.

## Health Certificate from France

The health certificate must be in the DAFF-specific format. Your French vet (or OV) must complete this form. It requires endorsement by the French competent authority (DGAL -- Direction Generale de l'Alimentation) before travel.

The certificate must be issued within the DAFF-specified window before the animal's arrival in Australia. Check the current validity window on the DAFF website.

## Air Routes: Paris to Australia

| Route | Airline | Notes |
|-------|---------|-------|
| CDG-SYD via Singapore | Qantas / Singapore Airlines | Cargo on both sectors |
| CDG-MEL via Singapore | Qantas | Cargo |
| CDG-PER via Dubai or Singapore | Emirates / Qantas | Cargo; check heat embargoes for Dubai |
| CDG-SYD via Hong Kong | Cathay Pacific | Cargo |

Australia-bound pets must arrive at approved entry airports: Sydney (SYD), Melbourne (MEL), Brisbane (BNE), or Perth (PER).

## Cost Estimate (France to Australia)

| Item | Estimated Cost |
|------|----------------|
| Titre test (vet + ANSES lab) | EUR 200-300 |
| Health certificate + DGAL endorsement | EUR 200-400 |
| Airline cargo (Paris to Australia) | EUR 1,200-2,800 |
| Mickleham quarantine (10 days) | AUD 2,000-4,500 |
| **Total** | **~EUR 3,600-8,000+** |

---

*Sources: DAFF Australia pet import requirements for listed countries; ANSES titre testing guidance; French DGAL official export certificate guidance. Data current as of June 2026.*""",
    },
    {
        "slug": "pet-insurance-for-international-moves",
        "title": "Pet Insurance for International Moves: What to Buy, What it Covers, and When it Kicks In",
        "description": "Moving internationally with a pet creates insurance gaps. What policies cover during transit, quarantine, and the first months in a new country -- and what to look for.",
        "date": "2026-06-21",
        "tags": ["insurance", "planning", "advice"],
        "faqs": [
            ("Does standard pet insurance cover transit and international relocation?",
             "Most standard pet insurance policies do not cover the transit period itself, and many have exclusions for events arising from international travel or quarantine. Check your current policy specifically for transit exclusions before booking. Some specialist policies and annual plans with international coverage include transit."),
            ("Will my UK pet insurance be valid if I move abroad permanently?",
             "Usually not. Most UK pet insurance policies require the animal to be a UK resident. If you move permanently, your existing policy will typically lapse or exclude claims arising from events outside the UK after a certain period. Contact your insurer before moving to understand the cut-off and arrange new cover in the destination country."),
            ("Is pet insurance available in all countries?",
             "No. Pet insurance is well-established in the UK, USA, Australia, Western Europe, and parts of Asia. In many African countries, Middle Eastern countries, and parts of Latin America and Southeast Asia, specialist pet insurance is limited or unavailable. In these destinations, the alternative is maintaining a dedicated emergency fund for veterinary costs."),
        ],
        "body": """International pet relocation creates an insurance gap that most owners do not notice until something goes wrong. Your current policy may not cover transit. Your new country may not have the same insurance products you are used to. And quarantine costs -- which can run to thousands of pounds -- are almost never covered.

## The Transit Gap

The period between a pet leaving your home and arriving at your destination is when the animal is most at risk. It is also the period most likely to be excluded from standard pet insurance.

**What to check in your current policy:**
- Does it cover events during international transit?
- Does it exclude claims arising from air travel?
- Does it cover veterinary costs in the destination country?
- Does it cover emergency vet costs if the pet is held at the border?

Most policies do not cover any of the above. Some specialist travel insurance add-ons for pets do.

## Cover During Quarantine

Quarantine costs (Australia's Mickleham, New Zealand's Levin) are not covered by standard pet insurance. They are fixed government fees payable by the owner. If the animal becomes ill during quarantine, the DAFF or MPI facility will provide veterinary care at the owner's cost.

Specialist quarantine insurance products exist but are not widely available. Ask your agent or a specialist broker.

## Setting Up Insurance at the Destination

| Destination | Pet insurance availability |
|-------------|---------------------------|
| UK | Extensive; many providers |
| Australia | Well-established; providers: PetPlan, Bow Wow Meow |
| USA | Growing market; Healthy Paws, Nationwide, Trupanion |
| EU | Available in most countries; varies by state |
| Singapore | Available; limited providers |
| UAE | Limited |
| Most of Africa | Very limited or unavailable |

Set up new insurance at the destination **before** the existing policy lapses. There is often a waiting period before a new policy covers pre-existing conditions.

## The Emergency Fund Alternative

For destinations where insurance is unavailable or expensive: maintain a dedicated emergency veterinary fund equivalent to one month of local vet specialist costs. For major cities in the UAE, Singapore, or Hong Kong, specialist vet fees can rival UK or US costs. EUR/GBP 5,000 is a reasonable starting point.

---

*Sources: UK Association of British Insurers pet insurance guidance; comparative international pet insurance market research. Data current as of June 2026.*""",
    },
    {
        "slug": "germany-to-australia-pet-transport-guide-2026",
        "title": "Germany to Australia Pet Transport 2026: Updated Titre Test Process and DAFF Requirements",
        "description": "Moving pets from Germany to Australia in 2026. The latest DAFF import rules for listed countries, titre test labs in Germany, health certificate endorsement, and Mickleham quarantine costs.",
        "date": "2026-06-21",
        "tags": ["germany", "australia", "routes", "planning"],
        "faqs": [
            ("Is Germany a listed or unlisted country for Australian pet import?",
             "Germany is a listed country for DAFF purposes. This means pets follow the standard pathway: microchip, rabies vaccination, titre test, 180-day wait, DAFF-endorsed health certificate, and mandatory quarantine. No additional restrictions apply for Germany specifically."),
            ("Which German laboratories can perform the DAFF-approved titre test?",
             "Germany has several DAFF-approved laboratories for rabies titre testing. Confirm the current approved lab list directly on the DAFF website at agriculture.gov.au before proceeding -- the approved list changes. Common German options have included Federal Institute for Risk Assessment (BfR) affiliated labs. Your German vet can guide you to the current nearest approved facility."),
            ("How long is quarantine in Australia for a pet from Germany?",
             "All pets entering Australia complete a minimum 10-day quarantine at Mickleham Quarantine Facility near Melbourne, regardless of origin country. There are no quarantine-free pathways for pets."),
        ],
        "body": """Australia has a strict biosecurity framework that applies equally to pets from Germany as from any other listed country. The process is well-established -- thousands of German families have successfully relocated their dogs and cats to Australia. The key is starting early.

## The 2026 Process for Germany to Australia

Germany is a **listed country** under DAFF's framework. This is the standard pathway:

### Stage 1: Microchip and Vaccination (Month 0)
- Confirm ISO 15-digit microchip in place before any vaccination is recorded
- Administer or confirm current rabies vaccination

### Stage 2: Titre Test (Month 1-2)
- Blood sample taken by German vet
- Sent to DAFF-approved laboratory
- Result must be ≥0.5 IU/mL to proceed
- Allow 2-4 weeks for result

### Stage 3: 180-Day Wait (Months 2-8)
- The 180-day clock starts from DAFF's notification of a satisfactory titre result
- Keep all vaccinations current; do not allow any to lapse

### Stage 4: Health Certificate and Booking (Month 7-8)
- Download DAFF-specific health certificate format from agriculture.gov.au
- German vet (OV/official vet) completes the certificate within the DAFF validity window before travel
- German competent authority endorses the certificate
- Book airline cargo to an approved Australian entry airport

### Stage 5: Travel and Quarantine
- Animal travels as cargo to Sydney, Melbourne, Brisbane, or Perth
- DAFF vets inspect on arrival
- 10-day mandatory quarantine at Mickleham (Melbourne)

## Air Routes from Germany

Frankfurt (FRA) and Munich (MUC) have the strongest cargo connections to Australia.

| Route | Airline | Connection |
|-------|---------|------------|
| FRA-SYD via Singapore | Singapore Airlines / Qantas | Cargo both legs |
| FRA-MEL via Singapore | Qantas | Cargo |
| MUC-SYD via Bangkok | Thai Airways / Qantas | Cargo |
| FRA-PER via Dubai | Emirates / Qantas | Cargo; check Dubai heat embargoes |

## Cost Estimate (Germany to Australia)

| Item | Estimated Cost |
|------|----------------|
| Titre test (vet + lab) | EUR 150-250 |
| Health certificate + German authority endorsement | EUR 200-350 |
| Airline cargo (Germany to Australia) | EUR 1,200-2,800 |
| 10-day Mickleham quarantine | AUD 2,000-4,500 (~EUR 1,200-2,700) |
| **Total** | **~EUR 2,750-6,100** |

---

*Sources: DAFF Australia official pet import requirements; APHIS Germany-equivalent DAFF listed country documentation. Data current as of June 2026.*""",
    },
    {
        "slug": "kuwait-pet-import-guide",
        "title": "Moving Pets to Kuwait: PAH Import Rules, Breed Restrictions, and Kuwait City Arrival",
        "description": "Kuwait pet import guide for dogs and cats. PAH permit process, breed bans, vaccination requirements, and what to expect at Kuwait International Airport.",
        "date": "2026-06-23",
        "tags": ["kuwait", "middle-east", "planning"],
        "faqs": [
            ("Which dog breeds are banned in Kuwait?",
             "Kuwait bans the import of several dog breeds classified as dangerous, including Pit Bull Terriers and related types, Rottweilers, and other large working/guard breeds. The current banned breed list is maintained by PAH (Public Authority for Agricultural Affairs and Fish Resources). Check directly with PAH before booking."),
            ("Do I need an import permit for a pet entering Kuwait?",
             "Yes. An import permit from Kuwait's PAH (Public Authority for Agricultural Affairs and Fish Resources) is required before the animal travels. Apply at least 4-6 weeks before your intended travel date."),
            ("Is there quarantine for pets entering Kuwait?",
             "No mandatory quarantine for pets arriving with complete documentation. PAH vets inspect animals at Kuwait International Airport on arrival. Incomplete documentation can lead to the animal being held."),
        ],
        "body": """Kuwait is home to a significant expat community across the oil and gas, financial, and government sectors. The country's pet import rules are managed by **PAH** (Public Authority for Agricultural Affairs and Fish Resources) and require advance permit.

## Import Permit Requirement

Apply for a PAH import permit before travel. Typically required:
- Owner's passport and Kuwait residency details
- Animal species, breed, age, sex, microchip number
- Current vaccination records

Allow 4-6 weeks for processing.

## Documentation Required

| Document | Requirement |
|----------|-------------|
| PAH import permit | Before travel |
| ISO 15-digit microchip | Yes |
| Rabies vaccination | Current |
| Full vaccination record | Core vaccines required |
| Health certificate | Issued within 10 days of travel, endorsed by government authority |
| Parasite treatment | Within 14 days of travel |

## Breed Restrictions

Kuwait's breed ban list is updated periodically. Known restricted/banned breeds include Pit Bull types and Rottweilers. Confirm the current list directly with PAH before booking.

## Climate

Kuwait is extremely hot in summer (June-September), with regular temperatures above 45°C. Airlines will typically not accept live animal cargo when ground temperatures exceed 29°C. Plan pet travel for October through April.

## Arrival at Kuwait International Airport

PAH vets inspect arriving animals at Kuwait International Airport (KWI). Present all original documents. Cargo pets are collected from the cargo facility after PAH clearance.

## Cost Estimate (UK to Kuwait)

| Item | Estimated Cost |
|------|----------------|
| PAH permit fee | Variable |
| Government health certificate + APHA endorsement | GBP 200-350 |
| Airline cargo | GBP 500-1,000 |
| **Total** | **~GBP 700-1,350** |

---

*Sources: Kuwait PAH official pet import requirements; APHA UK export guidance. Data current as of June 2026.*""",
    },
    {
        "slug": "pet-transport-south-america-guide",
        "title": "Moving Pets to South America: Brazil, Argentina, and Chile Import Rules Compared",
        "description": "South America's three largest pet destinations compared. Brazil MAPA, Argentina SENASA, and Chile SAG import requirements, health certificate formats, and key differences.",
        "date": "2026-06-23",
        "tags": ["brazil", "argentina", "chile", "latin-america", "planning"],
        "faqs": [
            ("Does Brazil require quarantine for imported pets?",
             "Brazil does not require mandatory quarantine for pet dogs and cats arriving with complete MAPA documentation. Animals are inspected by MAPA vets on arrival at approved airports (Guarulhos/Sao Paulo, Galeao/Rio de Janeiro, and a few others)."),
            ("Which South American country has the simplest pet import process?",
             "Chile (SAG) has a relatively streamlined process for pets from most countries, with no quarantine and clear documentation requirements. Brazil and Argentina are also manageable but involve more bureaucracy. All three require a government-endorsed health certificate."),
            ("Can I bring a Pit Bull to Argentina?",
             "Argentina has breed-specific regulations that restrict Pit Bull Terriers and related breeds. Confirm current regulations with SENASA before booking, as the rules are subject to change."),
        ],
        "body": """South America is a growing destination for international expats and remote workers. Brazil, Argentina, and Chile are the three most common destinations for pets. The rules vary by country -- here is a direct comparison.

## Brazil: MAPA Oversight

Brazil's pet imports are managed by **MAPA** (Ministerio da Agricultura, Pecuaria e Abastecimento).

**Requirements:**
- ISO microchip
- Current rabies vaccination (minimum 30 days before arrival; maximum within validity period)
- Core vaccinations (distemper, parvo, hepatitis for dogs)
- Health certificate in MAPA format, endorsed by origin government authority
- No quarantine for personal pets from most countries

**Entry airports:** Guarulhos (GRU/Sao Paulo), Galeao (GIG/Rio), Viracopos (VCP/Campinas), Brasilia (BSB), and a small number of others. Confirm your entry airport has MAPA veterinary inspection before booking.

## Argentina: SENASA Oversight

Argentina's pet imports are managed by **SENASA** (Servicio Nacional de Sanidad Animal).

**Requirements:**
- ISO microchip
- Current rabies vaccination
- Full vaccination schedule
- Internal/external parasite treatment within 30 days
- Health certificate endorsed by government authority in origin country

**Entry:** Buenos Aires Ezeiza Airport (EZE) is the primary entry point. Notify SENASA in advance for cargo shipments.

**Breed note:** Check current SENASA guidance on restricted breeds before booking.

## Chile: SAG Oversight

Chile's pet imports are managed by **SAG** (Servicio Agricola y Ganadero).

**Requirements:**
- ISO microchip
- Current rabies vaccination
- Full vaccination schedule
- Health certificate endorsed by origin government authority

Chile has no mandatory quarantine and is considered one of the more straightforward South American destinations for pets.

**Entry:** Santiago Arturo Merino Benitez Airport (SCL) is the main entry point.

## Side-by-Side Comparison

| Feature | Brazil | Argentina | Chile |
|---------|--------|-----------|-------|
| Authority | MAPA | SENASA | SAG |
| Import permit | No (personal pets) | No | No |
| Quarantine | No | No | No |
| Titre test | No | No | No |
| Breed restrictions | Some | Some | Limited |

---

*Sources: Brazil MAPA official pet import requirements; Argentina SENASA guidance; Chile SAG official guidance. Data current as of June 2026.*""",
    },
    {
        "slug": "ireland-pet-import-guide",
        "title": "Moving Pets to Ireland: Tapeworm Treatment, AHC Requirements, and the UK Land Bridge",
        "description": "Ireland's pet import rules for dogs and cats from the UK, EU, and third countries. The echinococcus treatment requirement, Animal Health Certificate process, and travelling via UK.",
        "date": "2026-06-25",
        "tags": ["ireland", "europe", "planning"],
        "faqs": [
            ("Does Ireland require tapeworm treatment for dogs?",
             "Yes. Ireland is one of the small group of EU countries (along with Finland, Malta, Norway, and the UK) that requires Echinococcus multilocularis tapeworm treatment for dogs before entry. Treatment must be administered by a vet 1-5 days before arriving in Ireland and documented in the health certificate. Cats are exempt."),
            ("What do I need to bring a dog from the UK to Ireland?",
             "An ISO-microchipped dog with a current rabies vaccination, an AHC issued by an Official Veterinarian within 10 days of travel, and tapeworm treatment administered 1-5 days before travel. Ireland is an EU member state, so the standard EU post-Brexit UK pet travel rules apply."),
            ("Can I travel from Northern Ireland to the Republic with my pet?",
             "Yes. Travel between Northern Ireland (UK) and the Republic of Ireland (EU) with a pet requires the full UK-to-EU documentation, including an AHC. This is the case even for short cross-border trips."),
        ],
        "body": """Ireland is a member of the EU but shares a land border with Northern Ireland (UK). This creates a unique situation for pet owners: UK-to-Ireland travel requires full EU post-Brexit documentation, including an AHC and tapeworm treatment.

## Ireland's Echinococcus Treatment Requirement

Like the UK, Finland, Malta, and Norway, Ireland requires dogs to be treated against *Echinococcus multilocularis* tapeworm before entry. The treatment must be:
- Administered by a licensed vet
- Given **1-5 days before the dog arrives in Ireland**
- Recorded in the health certificate

This applies to dogs arriving from all countries, including other EU member states. Cats are exempt.

## UK to Ireland: What You Need

| Document | Requirement |
|----------|-------------|
| ISO 15-digit microchip | Yes |
| Current rabies vaccination | Yes |
| Animal Health Certificate (AHC) | Yes -- OV-issued within 10 days |
| Echinococcus treatment | Yes -- for dogs; 1-5 days before travel |

## Travel Routes

Most UK-Ireland pet travel goes via:
- **Air:** British Airways, Aer Lingus, Ryanair serve Dublin, Cork, Shannon. Small in-cabin pets accepted by some carriers. Cabin rules: under 8 kg combined.
- **Ferry:** Stena Line, Irish Ferries (Holyhead to Dublin, Fishguard to Rosslare). Pets travel in vehicles or kennel decks depending on the operator.

Ferry travel is popular for dogs too large for cabin travel and owners who prefer not to use cargo.

## Third-Country Pets Entering Ireland

Pets from non-EU/non-UK countries entering Ireland follow EU third-country import rules:
- Health certificate in EU-approved format
- Endorsed by competent authority in origin country
- Arrive at an approved BIP

Dublin Airport and Rosslare ferry port are approved BIPs for companion animals.

## Cost Estimate (UK to Ireland)

| Item | Estimated Cost |
|------|----------------|
| OV appointment + AHC | GBP 150-250 |
| Tapeworm treatment | GBP 30-50 |
| Ferry pet fee | GBP 20-50 |
| **Total** | **~GBP 200-350** |

---

*Sources: EU Regulation 576/2013; Ireland DAFM (Department of Agriculture, Food and the Marine) official pet import guidance; APHA UK pet travel guidance. Data current as of June 2026.*""",
    },
]


def slug_exists(slug: str) -> bool:
    return os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md"))


def write_article(article: dict) -> bool:
    slug = article["slug"]
    if slug_exists(slug):
        return False

    path = os.path.join(BLOG_DIR, f"{slug}.md")

    tag_lines = "\n".join(f'  - "{t}"' for t in article["tags"])
    faq_lines = "\n".join(
        f'  - question: "{q.replace(chr(34), chr(39))}"\n    answer: "{a.replace(chr(34), chr(39))}"'
        for q, a in article["faqs"]
    )

    content = f"""---
title: "{article['title']}"
description: "{article['description']}"
date: "{article['date']}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{article['title']} | PetTransportGlobal"
  description: "{article['description']}"
tags:
{tag_lines}
faqs:
{faq_lines}
---

{article['body'].strip()}
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


if __name__ == "__main__":
    os.makedirs(BLOG_DIR, exist_ok=True)
    written = 0
    skipped = 0
    for article in ARTICLES:
        if write_article(article):
            written += 1
            print(f"  Written: {article['slug']}")
        else:
            skipped += 1
            print(f"  Skipped (exists): {article['slug']}")
    print(f"\nDone. Written: {written} | Skipped: {skipped}")
