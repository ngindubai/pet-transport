"""
Phase 6 Blog Batch 6 — 25 new articles
Topics: country import guides for gaps (USA, NZ, Brazil, HK, Italy, Portugal,
South Africa, Saudi Arabia, Canada pet entry, Mexico, Greece, Poland, Czech Republic,
Romania, Vietnam, Indonesia update), reverse route guides, and practical topic guides.
Skip-if-exists logic on every file.
"""
import os

BLOG_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\blog"
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    {
        "slug": "usa-pet-import-guide",
        "title": "USA Pet Import Guide: CDC Rules, Rabies Vaccinations, and What Changed in 2024",
        "description": "The USA tightened dog import rules in 2024. Here is what dogs and cats need to enter the United States, including the CDC screwworm certificate for some origins.",
        "date": "2026-05-05",
        "tags": ["usa", "north-america", "planning"],
        "faqs": [
            {"q": "Does my dog need a rabies vaccination to enter the USA?", "a": "Dogs arriving from countries with dog rabies (which includes the UK, Europe, and most of the world) must meet CDC import requirements, including a valid rabies vaccination issued outside the USA or a CDC dog import permit. The rules changed significantly in August 2024."},
            {"q": "Do cats need rabies vaccination to enter the USA?", "a": "The USA has no federal rabies vaccination requirement for cats arriving from most countries. However, some states have their own requirements, and airlines may ask for a health certificate. Always check with your airline and destination state."},
            {"q": "What is the USDA health certificate for entering the USA?", "a": "A USDA-accredited veterinarian must issue a health certificate for dogs. It must be completed within 10 days of travel. For some origins it also needs endorsement by the relevant government authority."},
        ],
        "content": """The United States is one of the more straightforward destinations for pet relocation -- but rules tightened considerably in 2024, and the changes caught a lot of people off guard.

Here is what you need to know.

## The 2024 CDC change for dogs

In August 2024, the **CDC** (Centers for Disease Control and Prevention) updated its dog import requirements. The change affects dogs arriving from countries classified as **high-risk for dog rabies** -- which is essentially most of the world, including the UK, most of Europe, the UAE, and Australia.

Under the new rules, dogs from high-risk countries must either:

1. Have a valid **rabies vaccination** issued by a USDA-accredited or equivalent veterinarian while the dog was physically outside the USA, **plus** a microchip implanted before the vaccination, OR
2. Arrive with a **CDC dog import permit** (for unvaccinated dogs, dogs vaccinated in the USA, or dogs under 6 months)

The microchip before vaccination requirement is the one that trips people up. If your vet microchipped your dog after they gave the rabies jab, the vaccination technically doesn't count under the new rules. Check the date order on your pet's records before you travel.

## What dogs need to enter the USA

- ISO microchip (15-digit, implanted before the rabies vaccination)
- Rabies vaccination record showing the vaccine was given after the microchip was implanted
- USDA health certificate completed by a USDA-accredited vet within 10 days of travel
- For dogs arriving via screwworm-affected countries: a Screwworm Treatment Certificate issued within 5 days of travel

Dogs under 6 months old cannot be imported from high-risk countries without a CDC permit. The permit process takes several weeks, so plan well in advance.

## What cats need to enter the USA

Cats have a simpler path. There is no federal rabies vaccination requirement for cats entering the USA from most countries. Airlines typically require a health certificate, and some US states have additional requirements -- but federally, it is much lighter than the dog rules.

Your airline will have specific rules about what documentation they want for cats. Check early, as requirements vary.

## The USDA health certificate

Both dogs and cats need a health certificate issued by a **USDA-accredited veterinarian** within 10 days of travel. This is important: not just any vet can issue a USDA health certificate. They must be accredited with the USDA.

For some destinations within the USA (particularly Hawaii), the requirements are stricter. Hawaii is rabies-free and has its own import rules separate from the mainland.

## Hawaii

Hawaii is effectively treated as a different country for pet imports. It is a **rabies-free state** and enforces strict arrival requirements:

- Microchip
- Two rabies vaccinations at least 30 days apart (the most recent given more than 90 days before arrival)
- Rabies titre test from an approved lab showing 0.5 IU/mL or higher, taken more than 90 days before arrival
- 5-day-or-less rabies quarantine at the Honolulu Animal Quarantine Station on arrival (if all requirements met)

Pets that don't meet the requirements face 120 days' quarantine in Honolulu. The programme is called the **5-Day-Or-Less** programme and requires advance booking.

## Timing for USA (mainland) entry

Most mainland US entry requirements can be met within a few weeks once you have a microchipped, vaccinated dog. The bottleneck is usually the health certificate timing (within 10 days of travel) and finding a USDA-accredited vet.

**Allow at least 6-8 weeks** to get the paperwork organised, more if you are unsure about the microchip/vaccination date order.

## Source

CDC Dog Import Requirements: cdc.gov/importation/dogs.html (verified May 2026). USDA APHIS: aphis.usda.gov (verified May 2026).
"""
    },
    {
        "slug": "new-zealand-pet-import-guide",
        "title": "New Zealand Pet Import Guide: Biosecurity Rules, MPI Approval, and What to Expect",
        "description": "New Zealand has some of the world's most rigorous pet import rules. Here is what dogs and cats need to enter NZ, including approved countries, quarantine, and MPI requirements.",
        "date": "2026-05-05",
        "tags": ["new-zealand", "oceania", "quarantine"],
        "faqs": [
            {"q": "How long is quarantine for pets entering New Zealand?", "a": "Dogs and cats from most countries face 10 days' managed isolation at the MPI facility at Auckland Airport. Pets from Australia, Norfolk Island, and Hawaii that meet all requirements may qualify for 10-day home isolation instead. The managed isolation booking must be secured well in advance."},
            {"q": "What countries can send pets to New Zealand without quarantine?", "a": "Pets from Australia, Norfolk Island, and qualified Hawaii addresses may be eligible for home isolation rather than managed isolation facility quarantine, provided all documentation and treatment requirements are met. No country is fully exempt from inspection on arrival."},
            {"q": "Can I bring a brachycephalic dog to New Zealand by air?", "a": "Many airlines restrict brachycephalic (flat-faced) breeds from cargo hold travel. Air New Zealand has restrictions on breeds including Bulldogs, Pugs, and Boxers. Check with your chosen airline before booking."},
        ],
        "content": """New Zealand is fiercely protective of its biosecurity -- and for good reason. As an island nation that has remained free of rabies and many other diseases, the country enforces some of the world's strictest pet import rules.

The process is manageable, but it requires planning that starts months before your intended travel date.

## MPI: New Zealand's biosecurity authority

All pet imports to New Zealand are managed by **MPI** (Ministry for Primary Industries). Before your pet can travel, you must submit an **Import Health Standard** application and receive approval. You cannot simply turn up at the border with a dog and a health certificate.

The full application, pre-export requirements, and managed isolation booking should all be arranged **at least 4-6 months before travel**.

## Which countries can send pets to New Zealand?

New Zealand accepts dogs and cats from a list of approved countries. These include the UK, USA, most of Europe, Australia, Singapore, Japan, and several others. Each country has its own pre-export requirements set out in New Zealand's Import Health Standards.

If your origin country is not on the approved list, importation may not be possible, or may require additional steps through a third country. Check the MPI website or speak with a registered pet transport agent.

## What dogs and cats need

The exact requirements depend on your origin country, but the common requirements for dogs and cats from most approved countries include:

- ISO microchip (15-digit, implanted before rabies vaccination)
- Rabies vaccinations -- series completed at least 6 months before departure in most cases
- Rabies titre test from a recognised lab showing 0.5 IU/mL or above, taken at least 6 months before travel
- Treatment for internal and external parasites within specified timeframes before travel
- Official government-endorsed health certificate
- Managed isolation booking confirmed before travel

For pets from Australia: a lighter set of requirements applies, and home isolation is generally possible rather than a government facility.

## Managed isolation

Pets from most countries will spend **10 days** in managed isolation at the **MPI Biosecurity Inspection Facility** at Auckland International Airport on arrival. The cost of managed isolation is paid by the owner and is typically around **NZD 1,400-2,000** (approximately GBP 650-950 / USD 840-1,200).

You must book a managed isolation space in advance. Spaces are limited, and failing to have a booking confirmed before departure is grounds for denial of entry. Book early.

## Timing

The 6-month titre test wait is the longest lead item. If your dog has never had a rabies titre test, the clock starts when you get a satisfactory result -- not when you draw the blood. Budget at least 7-8 months from start to finish, longer for complex cases.

For cats from most countries: similar requirements apply, including the titre test and 6-month stand-down.

## Source

MPI Import Health Standards: mpi.govt.nz/importing-exporting/live-animals/pets/ (verified May 2026).
"""
    },
    {
        "slug": "brazil-pet-import-guide",
        "title": "Brazil Pet Import Guide: MAPA Requirements, Health Certificates, and Quarantine Rules",
        "description": "Brazil's pet import process is managed by MAPA. Here is what dogs and cats need to enter Brazil, including the health certificate format, vaccination requirements, and what to expect on arrival.",
        "date": "2026-05-05",
        "tags": ["brazil", "south-america", "planning"],
        "faqs": [
            {"q": "Do pets entering Brazil need a rabies vaccination?", "a": "Yes. Dogs and cats must have a valid rabies vaccination. Brazil requires the vaccination was given at least 30 days before travel but no more than 12 months before. Annual boosters must be kept current."},
            {"q": "What health certificate does Brazil require for pets?", "a": "Brazil requires an official government-endorsed health certificate from the origin country, following the MAPA model format. The certificate must be issued by an accredited veterinarian and endorsed by the relevant government authority (e.g. APHA in the UK, USDA in the USA)."},
            {"q": "Is there quarantine for pets entering Brazil?", "a": "There is no standard quarantine for dogs and cats entering Brazil from most countries, provided all documentation is correct. Pets may be inspected at the port of entry. If documentation is incomplete, pets may be held at the airport at the owner's cost."},
        ],
        "content": """Brazil is South America's largest country and one of the most popular expat destinations on the continent. The pet import process is managed by **MAPA** (Ministerio da Agricultura, Pecuaria e Abastecimento) and is generally straightforward -- provided the paperwork is correct.

## What Brazil requires for dogs and cats

- ISO microchip (strongly recommended; Brazil aligns with ISO 11784/11785)
- Up-to-date vaccinations including: distemper, hepatitis, leptospirosis, parvovirus, parainfluenza (dogs); feline viral rhinotracheitis, calicivirus, panleukopenia (cats)
- Rabies vaccination: given at least 30 days before travel, no more than 12 months before
- Official MAPA-format health certificate, endorsed by the government authority of the origin country
- Treatment for external parasites (ticks, fleas) within 10 days before travel

Brazil does not require a rabies titre test for pets from most origin countries. The vaccination record is sufficient.

## The MAPA health certificate

The health certificate must follow the **MAPA model format** for the specific origin country. Brazil has published specific certificate templates for the UK, USA, EU countries, and others. Using the wrong format is a common mistake.

In the UK: the certificate must be issued by an Official Veterinarian (OV) and endorsed by **APHA** (Animal and Plant Health Agency).
In the USA: it must be issued by a USDA-accredited veterinarian and endorsed by the **USDA APHIS**.

The certificate must be issued within 10 days of travel.

## Arriving in Brazil

Brazil's main international airports (Guarulhos in Sao Paulo, Galeao in Rio de Janeiro, Brasilia, and others) all have agricultural inspection areas. Your pet will be inspected on arrival. If everything is in order, the process is quick.

Common reasons for delays or temporary detention:

- Missing government endorsement on the health certificate
- Rabies vaccination outside the 30-day to 12-month window
- Microchip details not matching the certificate
- Incomplete parasite treatment record

Allow extra time in the arrivals process and keep all original documents with you in your hand luggage.

## Travelling to Brazil with a cat

Cats need the same documentation as dogs, minus the canine-specific vaccines. The feline vaccines listed above (rhinotracheitis, calicivirus, panleukopenia) are the standard requirement. Check the current MAPA template for your origin country.

## Source

MAPA (Ministry of Agriculture, Livestock and Food Supply, Brazil): gov.br/agricultura (verified May 2026).
"""
    },
    {
        "slug": "hong-kong-pet-import-guide",
        "title": "Hong Kong Pet Import Guide: AFCD Permits, Quarantine Options, and Import Requirements",
        "description": "Bringing a pet to Hong Kong requires an AFCD import licence and varies by origin country. Here is what to expect, including quarantine durations and required documentation.",
        "date": "2026-05-05",
        "tags": ["hong-kong", "asia", "quarantine"],
        "faqs": [
            {"q": "How long is quarantine for pets entering Hong Kong?", "a": "Quarantine duration depends on origin country. Pets from Category 1 countries (rabies-free, including UK, Australia, Singapore) typically face 4 months' quarantine. Pets from approved countries with lower risk may qualify for shorter periods. Check the AFCD country category list before planning."},
            {"q": "What is an AFCD import licence and how do I apply?", "a": "The AFCD (Agriculture, Fisheries and Conservation Department) issues import licences for pets arriving in Hong Kong. You must apply before your pet travels. The application requires details of your pet, origin country, vaccination records, and proposed arrival details. Apply at least 2-3 months in advance."},
            {"q": "Can I bring a brachycephalic dog to Hong Kong?", "a": "Hong Kong's AFCD does not specifically ban brachycephalic breeds from import, but many airlines restrict them from cargo travel. Check with your airline before booking. Cabin travel is not available for dogs on most routes to Hong Kong."},
        ],
        "content": """Hong Kong operates an independent pet import system from mainland China. Imports are managed by **AFCD** (Agriculture, Fisheries and Conservation Department), and quarantine is mandatory for all dogs and cats arriving from most countries.

## AFCD import licence

Before your pet travels to Hong Kong, you must obtain an **AFCD import licence**. This is a formal permit authorising your specific pet to enter Hong Kong. You cannot import a pet without one.

Apply to AFCD at least **2-3 months** before your intended travel date. The application requires:

- Passport-style details of your pet (species, breed, age, microchip number, colour)
- Vaccination records
- Proposed route and arrival date
- Contact details in Hong Kong

There is a fee for the import licence (currently around HKD 150 per animal).

## Quarantine

All dogs and cats entering Hong Kong from most countries face mandatory quarantine at the **Government Quarantine Facility** in Lok Ma Chau. The duration depends on your origin country:

**Category 1 countries** (pets face up to 4 months' quarantine):
This category includes many countries -- check the AFCD website for the current list, as it is updated periodically.

**Reduced-duration quarantine** may be available for pets from approved countries with clean rabies records and full documentation including a valid titre test result. Titre tests from AFCD-recognised labs showing 0.5 IU/mL or above can reduce or modify the quarantine period in some cases.

The quarantine facility has limited capacity. You must book a space well in advance and confirm availability before your pet's travel is arranged.

## Documentation required

- ISO 15-digit microchip
- Rabies vaccination (valid and current)
- Rabies titre test from an AFCD-recognised laboratory (for reduced quarantine)
- Vaccinations against relevant diseases (distemper, parvovirus, leptospirosis for dogs; panleukopenia, herpesvirus, calicivirus for cats)
- Official health certificate issued and endorsed within 10 days of travel
- AFCD import licence

## Moving from Hong Kong to other countries

If you have a pet already in Hong Kong and are leaving to the UK, Australia, or New Zealand, be aware that Hong Kong is not classified the same as mainland China for most destination countries. The UK and Australia have specific import rules for pets from Hong Kong -- check APHA and DAFF respectively for the current requirements.

## Source

AFCD, Hong Kong: afcd.gov.hk/english/quarantine/qua_ie/qua_ie_dog/qua_ie_dog_import.html (verified May 2026).
"""
    },
    {
        "slug": "italy-pet-import-guide",
        "title": "Italy Pet Import Guide: EU Pet Passport, Microchip, and Entry Requirements",
        "description": "Bringing a pet to Italy from inside or outside the EU. Here is what the EU pet passport covers, what non-EU pets need, and the rules for dogs, cats, and ferrets.",
        "date": "2026-05-05",
        "tags": ["italy", "europe", "eu-travel"],
        "faqs": [
            {"q": "Can I bring my dog to Italy from the UK without quarantine?", "a": "Yes. There is no quarantine for dogs entering Italy from the UK, provided the pet has a valid microchip, a current rabies vaccination (given at least 21 days before travel), and an Animal Health Certificate issued by an Official Veterinarian and endorsed by APHA within 10 days of travel."},
            {"q": "Do I need an EU pet passport to take my pet to Italy?", "a": "EU pet passports are for pets already registered within EU member states. Pets arriving from outside the EU (including the UK) do not use an EU pet passport -- they use an Animal Health Certificate (AHC) instead. Once your pet is registered with an Italian vet, they can get an EU pet passport for future travel within the EU."},
            {"q": "What are the breed restrictions for dogs entering Italy?", "a": "Italy does not operate a national breed-specific legislation list at the federal level, but some municipalities have local restrictions. Dangerous breeds (including pit bulls, Rottweilers, and similar) may face restrictions in certain areas. Check local regulations in your destination city."},
        ],
        "content": """Italy is an EU member state, which means the same rules that apply across the EU apply here: pets need a microchip, a valid rabies vaccination, and correct documentation. For travellers arriving from within the EU, the process is simple. For those coming from outside the EU, including the UK, there are extra steps.

## Pets arriving from within the EU

If you and your pet are already in an EU country, you can travel to Italy using an **EU pet passport**. The passport is issued by a registered vet and records your pet's microchip number, vaccination history, and owner details. No additional documentation is needed for EU-to-EU travel.

## Pets arriving from outside the EU (including the UK)

Post-Brexit, UK pets cannot use EU pet passports. Instead, you need:

- **ISO microchip** (15-digit, 11784/11785 standard)
- **Rabies vaccination** -- must be administered at least **21 days** before travel to Italy (or any EU member state)
- **Animal Health Certificate (AHC)** -- issued by an Official Veterinarian in the UK and endorsed by **APHA** within 10 days of travel

There is no titre test required for travel from the UK to Italy. No quarantine.

## Dogs: tapeworm treatment

If you are travelling from the UK to Italy (and back), note that the UK requires dogs to have a tapeworm treatment (Praziquantel, administered by a vet) between 1 and 5 days before they re-enter the UK. This is a UK entry requirement, not an Italian one -- but it affects your planning if you plan to return.

## Arriving in Italy

Italy uses the same EU border inspection system as other member states. Pets arriving from outside the EU enter through a **Border Inspection Post (BIP)**. Most major Italian airports (Rome Fiumicino, Milan Malpensa, Venice Marco Polo) have BIPs for pets.

Check in advance that your flight arrives at an airport with a BIP that handles live animals. Not all airports do.

## Bringing a pet home from Italy to the UK

If you adopt a dog in Italy and want to bring it back to the UK:

- The dog needs a microchip, rabies vaccination (at least 21 days before entry to the UK)
- An AHC issued in Italy (from an Italian official veterinarian)
- Tapeworm treatment 1-5 days before UK entry (dogs only)

## Source

EU pet travel regulation: ec.europa.eu/food/animals/pet-movement (verified May 2026). APHA UK: gov.uk/bring-pet-to-great-britain (verified May 2026).
"""
    },
    {
        "slug": "portugal-pet-import-guide",
        "title": "Portugal Pet Import Guide: EU Entry Rules, Non-EU Requirements, and What UK Owners Need",
        "description": "Portugal is an EU member state. Here is what pets from inside and outside the EU need to enter Portugal, including post-Brexit UK requirements.",
        "date": "2026-05-05",
        "tags": ["portugal", "europe", "eu-travel"],
        "faqs": [
            {"q": "Can I bring my dog from the UK to Portugal without quarantine?", "a": "Yes. There is no quarantine for dogs entering Portugal from the UK. You need a microchip, a valid rabies vaccination (given at least 21 days before travel), and an Animal Health Certificate issued by an Official Veterinarian and endorsed by APHA within 10 days of travel."},
            {"q": "Can I bring my dog to the Azores or Madeira?", "a": "The Azores and Madeira are part of Portugal and are rabies-free territories with stricter pet import rules than mainland Portugal. Dogs and cats travelling to the Azores or Madeira from outside the EU typically need a rabies titre test with a satisfactory result taken at least 90 days before travel. Plan well in advance."},
            {"q": "How many pets can I bring to Portugal from the UK at once?", "a": "Up to 5 pets per trip is permitted for non-commercial movements. More than 5 pets counts as a commercial movement and requires additional documentation. If travelling with a large number of pets, contact APHA and DGAV (Portugal) in advance."},
        ],
        "content": """Portugal's warm climate, good infrastructure, and expat-friendly culture make it one of the most popular relocation destinations in Europe. Bringing your pet along is straightforward for most travellers -- but the Azores and Madeira have stricter rules that catch people out.

## Pets from within the EU

EU-to-Portugal travel uses the standard **EU pet passport** system. Your pet needs a microchip and a valid rabies vaccination recorded in their EU passport. No additional documentation needed.

## Pets from outside the EU (including the UK)

Post-Brexit requirements for UK pets entering Portugal (and all EU member states):

- ISO 15-digit microchip
- Rabies vaccination given at least **21 days** before travel
- **Animal Health Certificate (AHC)** issued by a UK Official Veterinarian and endorsed by APHA, within 10 days of travel

No titre test, no quarantine for mainland Portugal.

## The Azores and Madeira

This is where people get surprised. The **Azores** (Acores) and **Madeira** are Portuguese autonomous regions and are classified as **rabies-free territories** by the EU. This means they apply stricter import rules:

For dogs and cats from non-EU countries (including the UK) entering the Azores or Madeira:

- ISO microchip
- Rabies vaccination series (primary course + booster at least 30 days apart)
- Rabies titre test from an EU-recognised lab showing **at least 0.5 IU/mL**, taken at least **90 days before travel** to the islands
- All usual documentation and AHC

The 90-day stand-down after the titre test is the critical item. If your dog has never had a titre test, the earliest you can travel to the Azores or Madeira is 90 days after getting a satisfactory test result. Start planning at least 6 months in advance.

## Arriving in mainland Portugal

Pets arriving from outside the EU enter through a Border Inspection Post. Lisbon Humberto Delgado Airport and Porto Francisco Sa Carneiro Airport both have BIP facilities. Check that your specific flight arrives at an airport with a BIP for live animals.

## Getting an EU pet passport after arrival

Once your pet has arrived in Portugal and is registered with a licensed Portuguese vet, they can be issued an **EU pet passport** for future travel within the EU. This simplifies future trips within the Schengen area considerably.

## Source

DGAV (Directorate-General for Food and Veterinary, Portugal): dgav.pt (verified May 2026). APHA UK: gov.uk/bring-pet-to-great-britain (verified May 2026). EU pet travel: ec.europa.eu/food/animals/pet-movement (verified May 2026).
"""
    },
    {
        "slug": "south-africa-pet-import-guide",
        "title": "South Africa Pet Import Guide: DALRRD Import Permit, Rabies Rules, and Arrival Process",
        "description": "Bringing a pet to South Africa requires a DALRRD import permit and a vet-certified health certificate. Here is the full process for dogs and cats.",
        "date": "2026-05-05",
        "tags": ["south-africa", "africa", "planning"],
        "faqs": [
            {"q": "Do I need an import permit to bring my dog to South Africa?", "a": "Yes. Dogs and cats entering South Africa require an import permit issued by DALRRD (Department of Agriculture, Land Reform and Rural Development). Apply well in advance -- processing can take several weeks. The permit must accompany your pet on arrival."},
            {"q": "Is there quarantine for pets entering South Africa?", "a": "South Africa does not operate routine quarantine for dogs and cats from most approved countries, provided all documentation is in order. Pets may be held at the port of entry while documentation is checked. If documents are incomplete, pets face detention at the owner's cost."},
            {"q": "What vaccinations does South Africa require for dogs?", "a": "Dogs must be vaccinated against distemper, hepatitis, leptospirosis, parvovirus, and rabies. Vaccinations must be current (within the validity window on the certificate). The rabies vaccination must have been given at least 30 days before travel."},
        ],
        "content": """South Africa is one of Africa's most popular relocation destinations, and its pet import rules -- while requiring advance planning -- are manageable. The main requirement that trips people up is the import permit, which must be obtained before your pet travels.

## DALRRD import permit

The **Department of Agriculture, Land Reform and Rural Development (DALRRD)** issues import permits for dogs and cats entering South Africa. You apply online at the DALRRD portal, submitting:

- Owner and contact details
- Pet details (species, breed, sex, age, microchip number)
- Origin country
- Proposed port of entry and travel dates
- Supporting vaccination records

The permit fee is modest (around ZAR 500-1,000 depending on permit type). Processing typically takes **3-6 weeks** but can be longer during busy periods. Apply at least 2 months in advance.

## Documentation required

- DALRRD import permit (original)
- ISO microchip (15-digit, 11784/11785)
- Vaccination record including: rabies (given at least 30 days before travel), distemper, hepatitis, leptospirosis, parvovirus (dogs); panleukopenia, rhinotracheitis, calicivirus (cats)
- Official veterinary health certificate issued in the origin country within 10 days of travel, endorsed by the relevant government authority
- Treatment for external parasites within 7 days of travel

## No quarantine for compliant pets

South Africa does not operate routine quarantine for dogs and cats from most countries. Pets that arrive with all paperwork in order are typically cleared quickly at the port of entry. The main risk is documentation errors -- a missing permit or incorrect health certificate format can mean your pet is held at the airport at your expense.

## Major ports of entry

OR Tambo International Airport (Johannesburg) is the primary entry point for international pets. Cape Town International also handles pet arrivals. Both airports have DALRRD inspection facilities.

## Returning to your home country

If you plan to return to the UK, USA, or Australia with your South African-acquired pet, be aware:

- UK: requires AHC, microchip, rabies vaccination (21-day wait), tapeworm treatment 1-5 days before entry
- Australia: requires titre test, microchip, extensive documentation -- budget 7-12 months minimum
- USA: requires rabies vaccination and USDA health certificate

## Source

DALRRD (Department of Agriculture, Land Reform and Rural Development): dalrrd.gov.za (verified May 2026).
"""
    },
    {
        "slug": "saudi-arabia-pet-import-guide",
        "title": "Saudi Arabia Pet Import Guide: MEWA Requirements, Breed Restrictions, and Entry Rules",
        "description": "Saudi Arabia has specific breed restrictions and requires a MEWA health certificate for pet imports. Here is what dogs and cats need to enter Saudi Arabia.",
        "date": "2026-05-05",
        "tags": ["saudi-arabia", "middle-east", "planning"],
        "faqs": [
            {"q": "Are dogs allowed in Saudi Arabia?", "a": "Dogs are permitted in Saudi Arabia but face stricter social restrictions than in Western countries. All dogs require valid import documentation including a health certificate and vaccinations. Some breeds are restricted. Dogs are generally not permitted in public areas like parks and streets in many cities, though this varies."},
            {"q": "What breeds are restricted from entering Saudi Arabia?", "a": "Saudi Arabia restricts the import of breeds considered dangerous, including pit bulls, Rottweilers, Dobermanns, and similar breeds. The full restricted list should be verified with MEWA and your airline before travel. Some airlines also carry their own brachycephalic breed restrictions."},
            {"q": "Do cats need a health certificate to enter Saudi Arabia?", "a": "Yes. All cats entering Saudi Arabia require an official veterinary health certificate issued and endorsed within 10 days of travel, covering microchip, vaccinations (including rabies), and a declaration of health. The certificate must follow the MEWA-accepted format."},
        ],
        "content": """Saudi Arabia is home to a large expat population, and many families relocate there with pets. The import process is managed by **MEWA** (Ministry of Environment, Water and Agriculture) and is straightforward for most pets -- but there are breed restrictions and documentation requirements that need careful attention.

## Documentation required

- ISO microchip (15-digit, 11784/11785)
- Rabies vaccination (valid, given at least 30 days before travel in most cases)
- Core vaccinations: distemper, hepatitis, leptospirosis, parvovirus (dogs); panleukopenia, rhinotracheitis, calicivirus (cats)
- Official health certificate issued by a government-accredited vet in the origin country, endorsed by the relevant authority (APHA for UK, USDA for USA), within 10 days of travel
- Treatment for internal and external parasites

No rabies titre test is required for most origin countries.

## Breed restrictions

Saudi Arabia restricts the import of certain dog breeds. These include pit bulls, American Staffordshire Terriers, Rottweilers, Dobermanns, and similar working/guard breeds. The list is enforced at the point of entry.

If you have a mixed-breed dog that resembles a restricted breed, carry documentation from a vet confirming the breed composition. Airlines may also require this.

## Riyadh, Jeddah, and Dammam airports

The three main international airports -- King Khalid (Riyadh), King Abdulaziz (Jeddah), and King Fahd (Dammam) -- all handle pet arrivals. Pets travelling as cargo are inspected by MEWA officials on arrival. Processing typically takes 1-3 hours when documentation is complete.

## Practical notes for expats

Dogs in Saudi Arabia are generally kept as indoor or private garden pets. Public areas in most cities do not permit dogs, though enforcement varies by district and city. Cats face fewer social restrictions.

Veterinary care in Riyadh and Jeddah has improved considerably -- there are now several international-standard vet clinics serving the expat community. The SCVS (Saudi Council of Veterinary Surgeons) maintains a register of licensed practitioners.

## Source

MEWA (Ministry of Environment, Water and Agriculture, Saudi Arabia): mewa.gov.sa (verified May 2026).
"""
    },
    {
        "slug": "mexico-pet-import-guide",
        "title": "Mexico Pet Import Guide: SENASICA Requirements, Health Certificates, and Entry Rules",
        "description": "Bringing a dog or cat to Mexico is relatively simple. Here is what SENASICA requires, including the health certificate format, vaccination rules, and what to expect at the border.",
        "date": "2026-05-05",
        "tags": ["mexico", "north-america", "planning"],
        "faqs": [
            {"q": "Does my dog need a health certificate to enter Mexico?", "a": "Yes. Mexico requires a veterinary health certificate for dogs and cats issued within 10 days of travel. The certificate must confirm microchip, current vaccinations, and that the animal is free from signs of disease. It should be issued by an accredited veterinarian."},
            {"q": "Is there quarantine for pets entering Mexico?", "a": "There is no routine quarantine for dogs and cats entering Mexico from most countries, provided documentation is in order. Pets are inspected at the port of entry by SENASICA officials."},
            {"q": "Can I drive into Mexico with my pet?", "a": "Yes. Land border crossings into Mexico handle pets regularly. You need the same documentation as for air travel: health certificate, vaccination records, and microchip information. The process is usually quick when paperwork is complete."},
        ],
        "content": """Mexico is one of the more accessible countries for pet relocation. The documentation requirements are lighter than many countries, and there is no mandatory quarantine -- making it a relatively stress-free destination for pet owners, provided the paperwork is sorted.

## SENASICA

Pet imports to Mexico are managed by **SENASICA** (Servicio Nacional de Sanidad, Inocuidad y Calidad Agroalimentaria), the agricultural health authority. Inspectors at airports and land borders carry out checks.

## What dogs and cats need for Mexico

- ISO microchip (strongly recommended; Mexico aligns with international standards)
- Valid vaccinations: rabies (no specific pre-travel window required, just current/valid), plus core vaccines (distemper, parvovirus, leptospirosis for dogs; panleukopenia and respiratory viruses for cats)
- Health certificate issued by a licensed veterinarian within **10 days of travel**

Mexico does not currently require a government endorsement on the health certificate for most origins, though some airlines ask for one. Check with your airline.

No titre test, no import permit, no quarantine.

## Arriving by air

Most major Mexican airports handle pet arrivals without difficulty. Pets arriving as cargo are inspected on arrival. The process typically takes 30-60 minutes when documentation is complete.

Airlines serving Mexico include Aeromexico, American Airlines, Delta, United, British Airways codeshares, and many others. Each has its own rules for pets -- check the pet policy for your specific carrier before booking.

## Arriving overland

Land border crossings into Mexico are an option for pets, particularly for travellers from the USA. The main crossings at Tijuana, Ciudad Juarez, Laredo, and others process pets regularly. Have printed copies of all documentation. Some crossings are busier than others -- Tijuana in particular can have long waits.

## Returning to the USA with a Mexico-acquired pet

If you adopt or acquire a pet in Mexico and want to bring it to the USA, be aware of the 2024 CDC dog import rules. Dogs from Mexico are subject to the requirements for high-risk countries. An unvaccinated puppy or dog vaccinated while in the USA will need a CDC import permit. Plan ahead.

## Source

SENASICA (Mexico): gob.mx/senasica (verified May 2026).
"""
    },
    {
        "slug": "greece-pet-import-guide",
        "title": "Greece Pet Import Guide: EU Entry Rules, Non-EU Requirements, and Island Travel",
        "description": "Greece is an EU member state. Here is what dogs and cats need to enter from both EU and non-EU countries, including what UK pets need post-Brexit.",
        "date": "2026-05-05",
        "tags": ["greece", "europe", "eu-travel"],
        "faqs": [
            {"q": "Can I bring my pet to Greek islands as well as the mainland?", "a": "Yes. The Greek islands are part of Greece and do not have separate pet import rules. Ferries between islands and the mainland accept pets -- rules vary by ferry company, with most requiring pets to be on a lead or in a carrier and some banning them from cabins."},
            {"q": "What does my UK dog need to enter Greece?", "a": "A microchip, a valid rabies vaccination (given at least 21 days before travel), and an Animal Health Certificate issued by an Official Veterinarian and endorsed by APHA within 10 days of travel. No quarantine, no titre test for mainland Greece."},
            {"q": "Are there breed-specific laws in Greece?", "a": "Greece has national BSL (breed-specific legislation) covering breeds including American Pit Bull Terriers, Rottweilers, and several others. These breeds must be muzzled and on a lead in public areas. Import is not banned but is subject to additional rules. Check with DAAOK (the Greek agricultural authority) before importing a restricted breed."},
        ],
        "content": """Greece -- the islands, the archipelago, the ancient sites -- is a popular destination for expats and retirees. Bringing your pet is straightforward for EU residents, and manageable for non-EU travellers including those from the UK.

## Pets from within the EU

Standard EU pet travel rules apply. Your pet needs a microchip and a valid rabies vaccination recorded in an EU pet passport. No additional documentation needed for EU-to-Greece travel.

## Pets from the UK (post-Brexit)

UK pets need:

- ISO 15-digit microchip
- Rabies vaccination given at least **21 days** before travel to Greece (any EU destination)
- **Animal Health Certificate (AHC)** issued by an Official Veterinarian in the UK and endorsed by **APHA** within 10 days of travel

No quarantine, no titre test for mainland Greece.

## Dogs: tapeworm treatment on return to the UK

If you plan to bring your dog back to the UK after the trip, the dog needs tapeworm treatment (Praziquantel) administered by a vet between 1 and 5 days before re-entering the UK. This is a UK entry requirement, not a Greek one.

## Greece's breed-specific legislation

Greece has a national **dangerous dogs law** covering several breeds including American Pit Bull Terriers, Rottweilers, Bull Terriers, Tosa Inus, and several others. In public areas, these breeds must be muzzled and kept on a short lead. Import is permitted but owners must register with local authorities on arrival.

## Travelling to the Greek islands

All the major Greek islands -- Crete, Corfu, Rhodes, Mykonos, Santorini, and others -- are part of Greece and use the same import rules. You do not need separate documentation for island travel.

Domestic ferries between Athens (Piraeus) and the islands typically allow pets in designated areas. Rules vary: some companies require pets to remain in vehicles or designated outdoor areas; others allow small pets in carriers in cabins. Book early and confirm the pet policy with the ferry company.

Domestic flights within Greece (Athens to Thessaloniki, to island airports) have their own pet cabin/hold rules. Aegean Airlines and Olympic Air carry pets -- check their current policies before booking.

## Source

DAAOK (Directorate of Animal Health and Welfare, Greece): minagric.gr (verified May 2026). APHA UK: gov.uk/bring-pet-to-great-britain (verified May 2026).
"""
    },
    {
        "slug": "poland-pet-import-guide",
        "title": "Poland Pet Import Guide: EU Travel, UK Pet Requirements, and What to Know",
        "description": "Poland is an EU member state. Here is what pets from inside and outside the EU need to enter, including post-Brexit UK rules.",
        "date": "2026-05-05",
        "tags": ["poland", "europe", "eu-travel"],
        "faqs": [
            {"q": "Can I bring my dog from the UK to Poland without quarantine?", "a": "Yes, no quarantine. UK pets need a microchip, a valid rabies vaccination given at least 21 days before travel, and an Animal Health Certificate issued by an Official Veterinarian and endorsed by APHA, within 10 days of travel."},
            {"q": "Do I need an EU pet passport for travel within the EU once in Poland?", "a": "If you relocate to Poland with your pet, a Polish veterinarian can issue an EU pet passport. This allows you to travel with your pet to other EU countries without an Animal Health Certificate. It is issued after registration with a Polish vet."},
            {"q": "Are there breed restrictions in Poland?", "a": "Poland has a list of breeds classified as aggressive, including American Pit Bull Terriers, Rottweilers, Caucasian Shepherd Dogs, and others. These breeds require a muzzle and lead in public. Import is not banned but owners must follow local registration and control rules."},
        ],
        "content": """Poland is one of the EU's most popular relocation destinations, particularly for UK nationals with family connections. The pet import process follows standard EU rules and is one of the simpler destinations for UK pet owners.

## Pets from within the EU

EU pet passport is all you need. Microchip + valid rabies vaccination recorded in the passport. No additional paperwork for EU-to-Poland travel.

## Pets from the UK

- ISO microchip
- Rabies vaccination given at least **21 days** before travel
- **Animal Health Certificate (AHC)** issued by a UK Official Veterinarian and endorsed by APHA, within 10 days of travel

No titre test, no quarantine. Straightforward.

## Tapeworm on return to the UK

Dogs returning to the UK from Poland need tapeworm treatment (Praziquantel) given by a vet between 1 and 5 days before UK re-entry. Plan this into any return travel.

## Poland's approach to breed-specific legislation

Poland classifies several breeds as aggressive under national law. These include American Pit Bull Terriers, Rottweilers, Caucasian Shepherd Dogs, Central Asian Shepherd Dogs, South Russian Ovcharkas, and a few others. In public, these dogs must be muzzled and on a lead. Owners may need to register with local authorities.

Import of these breeds is not specifically banned, but you should check local municipality rules in your destination city, as enforcement can vary.

## Practical notes for expats

Poland has a growing expat veterinary sector, particularly in Warsaw and Krakow. EU-standard veterinary care is available. Vets in Poland can issue EU pet passports once your pet is registered.

Travelling onwards from Poland to Germany, France, Netherlands, or other EU countries uses the EU pet passport -- no AHC needed once your pet is registered in the EU system.

## Source

APHA UK: gov.uk/bring-pet-to-great-britain (verified May 2026). EU pet travel regulation: ec.europa.eu/food/animals/pet-movement (verified May 2026).
"""
    },
    {
        "slug": "vietnam-pet-import-guide",
        "title": "Vietnam Pet Import Guide: DAH Requirements, Quarantine, and Entry Documentation",
        "description": "Bringing a pet to Vietnam requires advance planning and a DAH-approved health certificate. Here is what dogs and cats need to enter Vietnam.",
        "date": "2026-05-05",
        "tags": ["vietnam", "asia", "planning"],
        "faqs": [
            {"q": "Is there quarantine for pets entering Vietnam?", "a": "Pets entering Vietnam may face a quarantine period of up to 21 days depending on origin country and documentation. Pets with full documentation from approved countries often face a shorter inspection period (3-7 days). Budget for quarantine when planning your timeline and costs."},
            {"q": "What government body manages pet imports to Vietnam?", "a": "The DAH (Department of Animal Health), under the Ministry of Agriculture and Rural Development (MARD), manages pet imports. An import permit from DAH is required before your pet travels."},
            {"q": "Can I bring a cat to Vietnam without quarantine?", "a": "Cats entering Vietnam are subject to the same import rules as dogs, including the DAH import permit and potential quarantine period. The duration depends on origin country and documentation completeness."},
        ],
        "content": """Vietnam's expat community has grown significantly in recent years, and with it the number of families relocating with pets. The import process is more involved than many expect -- quarantine is the norm rather than the exception, and advance planning is essential.

## DAH import permit

Before your pet travels to Vietnam, you must obtain an import permit from the **Department of Animal Health (DAH)**, part of the Ministry of Agriculture and Rural Development (MARD). The permit must be in hand before your pet departs.

Apply through the DAH portal or through a licensed agent in Vietnam. The process typically takes **2-4 weeks**. Provide:

- Owner details and contact in Vietnam
- Pet details (species, breed, sex, microchip number, age)
- Origin country
- Vaccination and health records
- Proposed entry point and travel dates

## Documentation required

- ISO microchip (15-digit)
- Rabies vaccination (valid and current)
- Core vaccinations (distemper, parvovirus, leptospirosis for dogs; panleukopenia, herpesvirus for cats)
- DAH import permit (original)
- Official health certificate issued by a government-accredited vet in the origin country, endorsed within 10 days of travel
- Negative test results may be required for some diseases depending on origin country

## Quarantine

Pets entering Vietnam face a quarantine period at a government-approved facility on arrival. The standard period is **21 days** for most origins. Pets from approved countries with full documentation may have this reduced.

Quarantine facilities in Vietnam are located at or near the major airports (Noi Bai in Hanoi, Tan Son Nhat in Ho Chi Minh City). The cost of quarantine is paid by the owner and varies but typically runs VND 3-6 million per week (around USD 120-240).

## Practical notes

Vietnam has a growing expat veterinary sector in Hanoi and Ho Chi Minh City. International-standard clinics with English-speaking vets are available in both cities.

The heat and humidity in Vietnam are significant factors for pet welfare, particularly for brachycephalic breeds. Dogs and cats that are sensitive to heat should have their crate and travel timing carefully considered.

## Source

DAH, MARD (Vietnam): cucthuy.mard.gov.vn (verified May 2026).
"""
    },
    {
        "slug": "australia-to-uk-pet-transport-guide",
        "title": "Australia to UK Pet Transport: What Your Dog or Cat Needs to Enter Britain",
        "description": "Moving from Australia to the UK with pets? Here is exactly what microchip, vaccination, titre test, and AHC rules apply when bringing dogs or cats from Australia to Great Britain.",
        "date": "2026-05-05",
        "tags": ["australia", "uk", "routes"],
        "faqs": [
            {"q": "Does my Australian dog need a titre test to enter the UK?", "a": "Yes. Dogs entering the UK from Australia need a valid rabies titre test showing 0.5 IU/mL or above. The test must be taken from a blood sample drawn at least 30 days after the most recent rabies vaccination, and the UK travel must occur at least 3 months after the date of the satisfactory titre test result."},
            {"q": "How long does it take to prepare a dog for travel from Australia to the UK?", "a": "Allow at least 4-6 months from start to finish. The titre test must be taken at least 30 days post-vaccination, and UK entry must occur at least 3 months after the titre test. If vaccinations need to be set up from scratch, add another month."},
            {"q": "Does my cat need a titre test to enter the UK from Australia?", "a": "Yes. Cats entering the UK from non-EU countries (which includes Australia) require the same titre test process as dogs. The same 30-day post-vaccination wait and 3-month post-titre-test stand-down apply."},
        ],
        "content": """The UK to Australia route gets a lot of coverage -- but the reverse, bringing a pet from Australia to the UK, is just as popular and has its own quirks. Here is what you need to know.

## UK entry rules for pets from Australia

Australia is classified by APHA as a **non-EU listed country** for pet travel. This means pets from Australia must meet the UK's unlisted country requirements, which include a titre test.

The requirements for dogs and cats entering Great Britain (England, Scotland, Wales) from Australia:

- ISO 15-digit microchip (implanted before or on the same date as the first rabies vaccination)
- Rabies vaccination series: primary vaccination, then a titre test blood draw at least **30 days after the most recent rabies vaccination**
- Rabies titre test from a UK-approved laboratory, showing **0.5 IU/mL or above**
- UK travel must not begin until at least **3 months after the date of the satisfactory titre test result** (APHA calls this the "3-month wait")
- Animal Health Certificate (AHC) issued by an Australian government-authorised veterinarian within 10 days of UK arrival
- For dogs only: tapeworm treatment (Praziquantel) given by a vet between **1 and 5 days** before arriving in Great Britain

## Timeline for travel from Australia to the UK

If your pet has never been vaccinated against rabies (Australia is rabies-free, so many pets haven't):

1. Microchip (if not already done)
2. Rabies vaccination -- clock starts now
3. Wait at least 30 days
4. Rabies titre test blood draw
5. Wait for lab result (usually 2-4 weeks)
6. If titre is 0.5 IU/mL or above: the 3-month stand-down begins from the **date of the blood sample**, not the date you received the result
7. Can travel to the UK after the 3-month period expires

Total minimum time: approximately **4.5-5 months** from first vaccination to eligible travel.

## Approved laboratories for titre tests in Australia

Australia has several APHA-approved laboratories for rabies titre testing. The main ones used by Australian vets are:

- Australian Animal Health Laboratory (AAHL) / CSIRO, Geelong
- Various accredited private labs -- confirm approval status with your vet and check the APHA list

## Which airports handle pet arrivals into the UK?

Pets arriving in the UK as cargo must enter through one of the approved Border Control Posts (BCPs). The main BCPs handling live animals are:

- London Heathrow (cargo terminal)
- Manchester Airport (cargo)
- Some ferry ports for land entry

Most Australian-origin pets arrive via Heathrow. Confirm the routing with your transport agent.

## Source

APHA (UK): gov.uk/bring-pet-to-great-britain (verified May 2026). Department of Agriculture (Australia): agriculture.gov.au (verified May 2026).
"""
    },
    {
        "slug": "singapore-to-uk-pet-transport-guide",
        "title": "Singapore to UK Pet Transport: APHA Requirements and the Titre Test Timeline",
        "description": "Moving from Singapore to the UK with your pet? Here is exactly what dogs and cats need to meet UK entry requirements, including the titre test process and timeline.",
        "date": "2026-05-05",
        "tags": ["singapore", "uk", "routes"],
        "faqs": [
            {"q": "Does my Singapore dog need a titre test to enter the UK?", "a": "Yes. Singapore is not on the EU-listed countries list for UK pet travel. Dogs and cats from Singapore need a rabies titre test showing 0.5 IU/mL or above, taken at least 30 days after the most recent rabies vaccination, with UK travel occurring at least 3 months after the satisfactory titre test date."},
            {"q": "How long does it take to move a pet from Singapore to the UK?", "a": "Allow at least 4-6 months from the start of the vaccination and titre test process. The 3-month stand-down post-titre-test is the binding constraint. Pets that already have a recent titre test may qualify to travel sooner."},
            {"q": "Does Singapore have approved labs for UK rabies titre testing?", "a": "The Animal and Veterinary Service (AVS) in Singapore can advise on approved laboratories. Check the APHA website for the current list of UK-approved titre test labs globally to confirm which Singapore-based or regional labs are accepted."},
        ],
        "content": """Singapore's large expat population means many pets make the journey from Singapore back to the UK or onwards to Australia, New Zealand, or Europe. The UK leg has specific requirements that require advance planning.

## UK entry requirements for pets from Singapore

Singapore is classified as a **non-EU listed third country** by APHA for UK pet travel purposes. This means:

- ISO 15-digit microchip
- Rabies vaccination series (primary + current booster)
- Rabies titre test blood drawn at least **30 days after the most recent rabies vaccination**
- Titre test result must show **0.5 IU/mL or above** from a UK-approved lab
- UK travel must not begin until at least **3 months after the date of the satisfactory titre test** (APHA 3-month wait)
- Animal Health Certificate (AHC) issued by a Singapore government-authorised veterinarian within 10 days of UK arrival
- Dogs only: tapeworm treatment (Praziquantel) by a vet between **1 and 5 days** before arriving in Great Britain

## Timeline

If your pet currently has no titre test result on record:

1. Check your pet's microchip and vaccination status with a Singapore vet
2. Get a titre test blood draw (at least 30 days after last rabies vaccination)
3. Send to an approved lab -- results typically take 2-3 weeks
4. If result is satisfactory: the 3-month stand-down begins from the date of the blood draw
5. Can travel to the UK after the 3-month period expires

For a pet that is already vaccinated and has a recent titre test in range: you may be able to travel much sooner -- check the dates carefully.

## Connecting through EU countries

Some pets travelling from Singapore to the UK route through EU countries (Amsterdam, Frankfurt, Paris). If your pet transits through an EU airport as cargo, the transit documentation requirements vary by airline and cargo handler. Discuss this with your transport agent.

## Source

APHA (UK): gov.uk/bring-pet-to-great-britain (verified May 2026). AVS Singapore: nparks.gov.sg/avs (verified May 2026).
"""
    },
    {
        "slug": "canada-to-uk-pet-transport-guide",
        "title": "Canada to UK Pet Transport: Bringing Your Dog or Cat from Canada to Great Britain",
        "description": "Moving from Canada to the UK with pets? Here is what APHA requires for dogs and cats arriving from Canada, including the titre test timeline and health certificate.",
        "date": "2026-05-05",
        "tags": ["canada", "uk", "routes"],
        "faqs": [
            {"q": "Does my Canadian dog need a titre test to enter the UK?", "a": "Yes. Canada is not on the EU-listed countries list for UK pet travel. Dogs and cats from Canada need a rabies titre test showing 0.5 IU/mL or above, with the blood draw at least 30 days post-vaccination and UK entry at least 3 months after the satisfactory result date."},
            {"q": "What is the health certificate required for pets entering the UK from Canada?", "a": "Dogs and cats need an Animal Health Certificate (AHC) issued by a Canadian Official Veterinarian within 10 days of UK arrival. The certificate must be in the APHA-approved format for Canada."},
            {"q": "Are there direct flights from Canada to the UK that accept pets as cargo?", "a": "Several airlines offer direct Canada-UK routes with cargo pet transport, including Air Canada, British Airways, and others. Not all routes accept pets year-round, and some brachycephalic breeds are restricted. Check with your airline well in advance."},
        ],
        "content": """Canada and the UK share deep cultural ties, and many Canadians relocate to the UK each year -- often with pets. The process is manageable, but the titre test requirement means you need to start planning at least 5 months before your intended move date.

## UK entry requirements for pets from Canada

Canada is a **non-EU listed third country** under APHA's pet travel rules. Requirements:

- ISO 15-digit microchip (implanted before or same day as first rabies vaccination)
- Rabies vaccination -- current and valid
- Rabies titre test blood drawn at least **30 days after the most recent rabies vaccination**
- Titre test showing **0.5 IU/mL or above** from a UK-approved laboratory
- UK travel at least **3 months after the date of the satisfactory titre test**
- Animal Health Certificate (AHC) issued by a Canadian Official Veterinarian and endorsed by the Canadian Food Inspection Agency (CFIA) within 10 days of UK arrival
- Dogs only: tapeworm treatment (Praziquantel) by a vet between **1 and 5 days** before arriving in Great Britain

## Getting the titre test done in Canada

Canada has several APHA-approved labs for rabies titre testing. The main one used by Canadian vets is:

- **Rabies Laboratory, Cornell University** (processes samples from Canada)
- Some vets also use **IDEXX** or other approved labs -- confirm the lab is on the APHA approved list before testing

Ask your vet to confirm which approved lab they use for titre testing before the blood draw. The result is only valid for UK entry if the lab is APHA-approved.

## CFIA endorsement

The AHC must be endorsed by the **Canadian Food Inspection Agency (CFIA)**. Your vet issues the certificate; CFIA endorses it. Allow time for CFIA processing -- typically 3-5 business days, but during busy periods it can take longer. Some vets send the certificate to CFIA directly; others ask the owner to do it.

## Flying from Canada to the UK

The main direct routes are from Toronto (YYZ), Vancouver (YVR), and Montreal (YUL) to London (LHR or LGW). Air Canada and British Airways are the primary carriers. Both accept pets in cargo on many transatlantic routes, but policies vary by season and breed.

Book early -- cargo space for pets is limited, especially in summer.

## Source

APHA (UK): gov.uk/bring-pet-to-great-britain (verified May 2026). CFIA: inspection.canada.ca (verified May 2026).
"""
    },
    {
        "slug": "japan-to-australia-pet-transport-guide",
        "title": "Japan to Australia Pet Transport: DAFF Requirements and the Longest Preparation in the World",
        "description": "Moving from Japan to Australia with a pet? Australia's biosecurity rules are among the world's strictest. Here is the full Japan-to-Australia process, including quarantine.",
        "date": "2026-05-05",
        "tags": ["japan", "australia", "routes"],
        "faqs": [
            {"q": "How long does it take to prepare a dog for travel from Japan to Australia?", "a": "At minimum 6 months, often 9-12 months. The titre test must show a satisfactory result at least 6 months before entry into Australia. With additional import permit processing, serology lab wait times, and treatment scheduling, most owners allow 9-12 months."},
            {"q": "Is there quarantine for pets arriving in Australia from Japan?", "a": "Yes. All dogs and cats entering Australia from Japan face 10 days' quarantine at the Post-Entry Quarantine (PEQ) facility at Melbourne Airport (Mickleham). Japan is in Group 3 (higher risk), so the quarantine is mandatory and cannot be reduced."},
            {"q": "What labs in Japan are approved for Australian titre testing?", "a": "DAFF's list of approved serology laboratories includes labs in Japan. Your Japanese vet will know which labs they work with. Ensure the lab is on the current DAFF approved list before drawing blood -- an unapproved lab result will not be accepted."},
        ],
        "content": """Japan to Australia is one of the most demanding pet relocation routes in the world. Australia's Post-Entry Quarantine (PEQ) requirements and the 6-month titre test stand-down make this a process that takes the better part of a year to complete properly.

That said, it is done regularly by expat families, and with good preparation, your pet will come through safely.

## Why Australia is so strict

Australia is rabies-free, has no foot-and-mouth disease, and is free of many other animal diseases that are common elsewhere. Its biosecurity rules reflect decades of investment in keeping it that way. DAFF (Department of Agriculture, Fisheries and Forestry) enforces these rules strictly.

## Japan's group classification

Japan is classified as **Group 3** for Australian pet imports. This means:

- Quarantine is mandatory (10 days at the Mickleham PEQ facility near Melbourne)
- More extensive pre-export treatments and documentation are required compared to Group 1 or 2 countries

## What dogs and cats from Japan need for Australia

- ISO microchip
- Rabies vaccinations (DAFF requires a specific vaccination schedule depending on the animal's previous vaccination history)
- Rabies titre test from a DAFF-approved laboratory in Japan, showing **0.5 IU/mL or above**
- Blood drawn for titre test at least **30 days after the most recent rabies vaccination**
- Australia entry must not begin until at least **6 months after the satisfactory titre test date**
- BICON import permit from DAFF (applied for online; current cost AUD 420)
- Treatments for internal parasites (Praziquantel, Ivermectin) given within 14 days and 5 days before departure
- Official veterinary health certificate, endorsed by MAFF (Ministry of Agriculture, Forestry and Fisheries) in Japan, completed within 10 days of travel

## The 6-month stand-down

The single most important timeline constraint: your pet cannot enter Australia until at least **6 months have passed from the date of the satisfactory titre test**. If the first test result is below 0.5 IU/mL, the clock does not start -- you re-vaccinate and re-test.

This is why most Japan-to-Australia pet relocations take 9-12 months from first contact with a vet to arrival in Australia.

## Quarantine in Melbourne

The **Post-Entry Quarantine facility at Mickleham**, near Melbourne Airport, is where all Group 3 country pets spend their quarantine. The cost is currently around AUD 2,000-2,500 for 10 days (approximately GBP 1,000-1,250). The facility provides professional care, and daily video check-ins are available for owners.

Dogs must enter Australia via Melbourne Airport for Mickleham quarantine. Some routing adjustments may be needed if your preferred airline does not fly directly to Melbourne.

## Source

DAFF (Australia): agriculture.gov.au/pets (verified May 2026). MAFF (Japan): maff.go.jp/aqs/english (verified May 2026).
"""
    },
    {
        "slug": "dubai-to-australia-pet-transport-guide",
        "title": "Dubai to Australia Pet Transport: UAE Pets and Australia's Strict Biosecurity Requirements",
        "description": "Moving from Dubai to Australia with a dog or cat? Here is the full UAE-to-Australia process including Group 3 quarantine, titre test stand-down, and DAFF import permit.",
        "date": "2026-05-05",
        "tags": ["uae", "australia", "routes"],
        "faqs": [
            {"q": "How long does it take to move a pet from Dubai to Australia?", "a": "At minimum 7-9 months. The titre test must show a satisfactory result at least 6 months before Australian entry. With processing time, vaccination scheduling, and import permit lead time, most families allow 9-12 months."},
            {"q": "What group is UAE in for Australian pet imports?", "a": "The UAE is classified as Group 3 for Australian pet imports. This means 10 days' mandatory quarantine at the Mickleham PEQ facility and the full pre-export requirement set."},
            {"q": "Can my pet fly direct from Dubai to Melbourne?", "a": "Emirates operates Dubai to Melbourne routes and accepts pets as cargo on some services. Not all flights accept pets -- check with Emirates cargo well in advance. Your pet must arrive into Melbourne for Mickleham quarantine."},
        ],
        "content": """Dubai is home to hundreds of thousands of expats, many of whom eventually relocate onward to Australia. The UAE-to-Australia pet route is one of the more common long-haul moves we see -- and one of the most demanding in terms of preparation time.

## UAE's Group 3 classification

The UAE is classified as **Group 3** for Australian pet imports. This is the same category as most of the Middle East, Asia, and Africa. It means:

- Mandatory 10 days' quarantine at the Mickleham Post-Entry Quarantine facility near Melbourne
- Full pre-export requirements including titre test, parasite treatments, and government-endorsed documentation

## What dogs and cats from Dubai need for Australia

- ISO microchip (15-digit, implanted before first rabies vaccination)
- Rabies vaccination series, following DAFF's specific requirements for Group 3 countries
- Rabies titre test from a DAFF-approved laboratory, showing **0.5 IU/mL or above**
- Blood drawn at least **30 days after the most recent rabies vaccination**
- Australian entry at least **6 months after the satisfactory titre test date**
- BICON import permit from DAFF (AUD 420, apply online through the BICON portal)
- Parasite treatments: Praziquantel and Ivermectin within 14 days and 5 days before departure
- Official health certificate endorsed by the UAE Ministry of Climate Change and Environment (MOCCAE), completed within 10 days of travel

## The title test in Dubai

Several veterinary clinics in Dubai and Abu Dhabi can perform rabies titre test blood draws and arrange dispatch to a DAFF-approved laboratory. The main labs approved by DAFF for UAE samples include laboratories in Europe and Australia. Ask your vet which lab they use and confirm it is on the current DAFF list.

Results typically take 2-4 weeks after the blood draw.

## Timing worked example

If you decide today to move your dog from Dubai to Australia:

- Week 1: microchip confirmed, rabies vaccination given (if not current)
- Week 5: titre test blood draw (30 days after vaccination)
- Week 7-9: titre test result received
- Months 3-9: stand-down period (6 months from titre test date)
- Month 9-10: BICON permit, health certificate, parasite treatments, travel

Realistic minimum: **9 months** from start to arrival in Australia.

## Emirates and cargo for pets

Emirates accepts pets in cargo on Dubai-Melbourne routes, but not all flights have cargo capacity for live animals and not all year round. Book cargo space early -- summer months (June-August) can be restricted due to temperature embargoes.

Your pet must enter Australia at Melbourne International Airport for Mickleham quarantine.

## Source

DAFF (Australia): agriculture.gov.au/pets (verified May 2026). MOCCAE (UAE): moccae.gov.ae (verified May 2026).
"""
    },
    {
        "slug": "germany-to-usa-pet-transport-guide",
        "title": "Germany to USA Pet Transport: CDC Rules, USDA Health Certificates, and What Changed in 2024",
        "description": "Moving from Germany to the USA with your dog or cat? Here is what changed in 2024 and what German pet owners need to meet CDC import requirements.",
        "date": "2026-05-05",
        "tags": ["germany", "usa", "routes"],
        "faqs": [
            {"q": "Does my German dog need special documentation to enter the USA?", "a": "Yes. Under the 2024 CDC update, dogs from Germany (a country with dog rabies on the CDC list) must have a valid rabies vaccination issued by a non-USA vet with the microchip implanted before the vaccination. A USDA health certificate from a USDA-accredited vet is also required within 10 days of travel."},
            {"q": "Can my German cat travel to the USA without a titre test?", "a": "Yes. Cats entering the USA do not need a rabies titre test. A health certificate from an accredited vet is typically required by the airline. There is no federal US titre test requirement for cats."},
            {"q": "Does my dog need to fly cargo from Germany to the USA?", "a": "Cabin travel is not permitted for dogs on transatlantic flights. Dogs from Germany to the USA travel as checked baggage (small breeds) or cargo. Check with your specific airline for size and breed restrictions."},
        ],
        "content": """Germany to USA is one of the busiest expat routes in the world, with thousands of families and military personnel making the move each year. The 2024 CDC update changed the documentation requirements for dogs significantly -- here is what German pet owners need to know.

## The 2024 CDC update for dogs

In August 2024, the CDC updated its dog import rules for dogs arriving from countries with dog rabies. Germany falls into this category. Under the new rules:

- Your dog must have a microchip **implanted before or on the same date as** the rabies vaccination
- The rabies vaccination must have been given by a veterinarian located **outside the USA**
- A USDA-accredited vet must issue a health certificate within **10 days of travel**

The critical detail: if your dog's microchip was implanted after the rabies vaccination, the vaccination does not count under the new rules. Check the date order on all documentation before you travel.

## What dogs from Germany need for the USA

- ISO microchip (implanted before or same date as rabies vaccination)
- Valid rabies vaccination given by a non-USA vet, after microchip implantation
- USDA health certificate issued by a USDA-accredited veterinarian within 10 days of travel

No titre test, no quarantine for mainland USA.

## What cats from Germany need for the USA

- Health certificate from an accredited veterinarian (airline requirement)
- No federal rabies vaccination requirement, though some states have their own rules
- No titre test, no quarantine

## USDA-accredited vets in Germany

Germany has a network of USDA-accredited veterinarians who can issue the required health certificate. The USDA APHIS website maintains a searchable list by country. Search for accredited veterinarians in your city.

Allow **2-3 weeks** to identify the right vet, book an appointment, and get the certificate issued within the 10-day window before travel.

## Hawaii

If you are moving to Hawaii (not the mainland USA), the rules are much stricter. See our USA Pet Import Guide for the Hawaii 5-Day-Or-Less programme requirements.

## Source

CDC Dog Import Requirements: cdc.gov/importation/dogs.html (verified May 2026). USDA APHIS: aphis.usda.gov (verified May 2026).
"""
    },
    {
        "slug": "ireland-to-australia-pet-transport-guide",
        "title": "Ireland to Australia Pet Transport: What Irish Pet Owners Need to Know",
        "description": "Moving from Ireland to Australia with your dog or cat? Here is the full process including Group 3 requirements, the 6-month titre test stand-down, and Mickleham quarantine.",
        "date": "2026-05-05",
        "tags": ["ireland", "australia", "routes"],
        "faqs": [
            {"q": "What group is Ireland in for Australian pet imports?", "a": "Ireland is classified as Group 3 for Australian pet imports, the same as the UK and most European countries. This means 10 days' mandatory quarantine at the Mickleham PEQ facility."},
            {"q": "How long does it take to prepare a pet in Ireland for travel to Australia?", "a": "At minimum 7-9 months. The titre test result must be satisfactory and at least 6 months must pass before Australian entry. With processing and preparation, most Irish pet owners allow 9-12 months total."},
            {"q": "Which airlines fly from Ireland to Australia for pet cargo?", "a": "There are no direct flights from Ireland (Dublin) to Australia. Most pets route via London Heathrow, Dubai, Singapore, or another hub. Emirates, Qantas, and Singapore Airlines carry pets as cargo on various Australia-bound routes. Your pet transport agent will arrange the optimal routing."},
        ],
        "content": """Ireland to Australia is a route we see frequently -- many Irish expats settle in Australia, and when they decide to bring their pets over, they find the process more involved than expected.

## Ireland is Group 3 for Australia

Ireland is classified as **Group 3** for Australian pet imports. This is the same as the UK, USA, and most developed countries. Group 3 means:

- 10 days' mandatory quarantine at the **Mickleham Post-Entry Quarantine** facility near Melbourne
- Full pre-export requirements including titre test, multiple parasite treatments, BICON permit, and government-endorsed documentation

## What dogs and cats from Ireland need for Australia

- ISO microchip
- Rabies vaccination series (Ireland is rabies-free, so most Irish pets have never been vaccinated -- this is where the timeline starts)
- Rabies titre test from a DAFF-approved laboratory, showing **0.5 IU/mL or above**
- Blood drawn at least **30 days after the most recent rabies vaccination**
- Australian entry at least **6 months after the satisfactory titre test date**
- BICON import permit (AUD 420, apply at agriculture.gov.au)
- Parasite treatments (Praziquantel and Ivermectin) within specified windows before departure
- Official health certificate endorsed by the **Department of Agriculture, Food and the Marine (DAFM)** in Ireland, completed within 10 days of travel

## The challenge for Irish pets

Because Ireland is a rabies-free country, most Irish dogs and cats have never been vaccinated against rabies. That means the vaccination and titre test process starts from zero.

Typical timeline:
1. Microchip (if not done)
2. Rabies vaccination -- clock starts
3. Wait 30 days
4. Titre test blood draw
5. Wait for result (2-4 weeks)
6. If satisfactory: 6-month stand-down begins
7. Travel to Australia after 6 months

Minimum time from vaccination to travel: **approximately 7 months**. Realistically, with permit processing and scheduling, **9-10 months** is a safer estimate.

## Routing from Ireland

No direct flights connect Dublin to Australia. Most Ireland-Australia pet movements route through:

- **London Heathrow** → direct to Melbourne, Sydney, or Brisbane (Qantas, British Airways)
- **Dubai** → Melbourne, Sydney (Emirates)
- **Singapore** → Melbourne, Sydney (Singapore Airlines)

Your pet transport agent will arrange the most suitable routing based on available cargo capacity and breed restrictions.

## Source

DAFF (Australia): agriculture.gov.au/pets (verified May 2026). DAFM (Ireland): gov.ie/en/organisation/department-of-agriculture-food-and-the-marine/ (verified May 2026).
"""
    },
    {
        "slug": "pet-transport-military-families-updated",
        "title": "Pet Relocation for Military Families: Orders, Tight Timelines, and Making It Work",
        "description": "Military families face unique challenges with pet relocation -- short PCS timelines, restricted airline routes, and destinations with strict quarantine. Here is how to manage it.",
        "date": "2026-05-05",
        "tags": ["military", "planning", "usa"],
        "faqs": [
            {"q": "Can the military help pay for pet transport during a PCS move?", "a": "The US military does not reimburse pet transport costs as part of PCS entitlements. Pet shipping is considered a personal expense. Some families find that the Joint Travel Regulations (JTR) permit certain pet-related expenses in limited circumstances -- check with your installation's transportation office."},
            {"q": "What destinations are hardest for military pets?", "a": "Hawaii, Japan, South Korea, and Australia are the most challenging. Hawaii requires the 5-Day-Or-Less programme with titre tests and specific vaccination schedules. Japan and South Korea have their own import requirements. Australia requires 6-month titre test stand-downs and quarantine."},
            {"q": "Is there a military-specific pet transport service?", "a": "Several pet transport agents specialise in military moves, particularly for US military families moving to Okinawa, Germany, Korea, and other bases. IATA-accredited agents with military relocation experience can help navigate installation-specific requirements and base quarantine rules."},
        ],
        "content": """A permanent change of station (PCS) move is stressful enough without worrying about how to get your dog or cat to the new duty station. The short timelines, unfamiliar destinations, and strict entry requirements at some bases make military pet relocation one of the most challenging scenarios in the industry.

Here is a realistic guide to making it work.

## The timeline problem

Most military families get PCS orders with 30-90 days' notice. For many international destinations, that is nowhere near enough time if your pet hasn't already started the required preparation.

Destinations with long lead times include:

- **Hawaii**: requires titre test drawn at least 90 days before entry, and the test result must be satisfactory at least 90 days before arrival. If you haven't started this process, you may need to ship your pet ahead or behind you.
- **Japan**: the Japan Ministry of Agriculture requires specific quarantine documentation; the import process can take 6-12 months
- **Australia** (for families moving to joint bases or exchanges): 6-month titre test stand-down + 10 days' quarantine
- **South Korea**: pets from most countries face a 10-day inspection period at APQA

**Recommendation**: start the pet relocation process the moment you expect orders are possible. Don't wait for official orders. Getting your pet's vaccinations, titre test, and documentation started early costs nothing but time.

## Hawaii: the 5-Day-Or-Less programme

If you're heading to Hawaii (Schofield Barracks, Marine Corps Base Hawaii, Pearl Harbor, Hickam), the 5-Day-Or-Less programme is the only realistic option to avoid 120 days' quarantine. Requirements:

- Microchip
- Two rabies vaccinations at least 30 days apart, the most recent given more than 90 days before arrival
- Titre test showing 0.5 IU/mL or above from an approved lab, drawn more than 90 days before arrival
- Rabies serology certificate
- Advance reservation at the Honolulu airport quarantine station
- Tapeworm treatment within 14 days of arrival (dogs)

Total minimum time: approximately **6 months** from scratch. If you already have a vaccinated dog with a titre test on record, check the dates -- you may qualify sooner.

## Choosing a military-experienced transport agent

Not all pet transport agents have experience with military moves. For complex destinations like Japan, Korea, and Hawaii, look for agents who:

- Have worked with military families specifically
- Understand the timing constraints of PCS orders
- Know the base-specific procedures at your destination
- Are IPATA members (International Pet and Animal Transportation Association)

Ask the agent directly: "Have you shipped pets to this installation before?"

## What the military doesn't cover

US military PCS entitlements do not include pet transport costs. The average cost of shipping a dog to Japan or Hawaii from the continental USA is USD 2,000-5,000+. This is a personal expense. Some families choose to rehome pets rather than pay this, but many find the cost worth it for the family's wellbeing.

IATA-certified crates, veterinary preparation, health certificates, and cargo fees are all out-of-pocket.
"""
    },
    {
        "slug": "what-to-do-when-your-pet-is-denied-entry",
        "title": "What Happens When Your Pet Is Denied Entry at the Border?",
        "description": "Pet entry denial is rare but it happens. Here is what typically causes it, what border officials will do, and how to handle it if you find yourself in this situation.",
        "date": "2026-05-05",
        "tags": ["planning", "documentation", "advice"],
        "faqs": [
            {"q": "Can a pet be sent back if denied entry?", "a": "Yes. If a pet arrives at the border with missing or incorrect documentation, the destination country can refuse entry and require the animal to be returned to the origin country at the owner's expense. In some cases the pet may be held in a government facility pending correct documentation."},
            {"q": "What is the most common reason pets are denied entry?", "a": "Documentation errors are by far the most common cause. These include health certificates issued more than 10 days before travel, missing government endorsements, incorrect vaccination dates, microchip numbers not matching certificates, or titre test results from unapproved laboratories."},
            {"q": "Can I fix a documentation error at the border?", "a": "In some countries, minor errors can be corrected on the spot if the underlying requirement is met (e.g., the vaccination is valid but the certificate has a typo). In others, the rules are strictly applied and no on-the-spot corrections are possible. Australia, New Zealand, and the UK are among the stricter countries."},
        ],
        "content": """No one wants to think about their pet being refused at the border. But it does happen, and knowing what to expect can help you either prevent it or deal with it calmly if it occurs.

## Why pets get denied entry

The vast majority of entry denials come down to documentation errors, not animal health problems. The most common causes:

**Health certificate timing**: certificates must be issued within 10 days of travel in most countries. A certificate issued 11 days before travel is invalid. Airlines sometimes miss this; owners sometimes miss it. Build a checklist and check dates the night before travel.

**Missing government endorsement**: for countries that require an endorsed health certificate (Australia, New Zealand, USA, Brazil, South Africa), a certificate from a vet without the government agency's stamp is not accepted at the border. This is particularly common for UK and USA exports, where APHA/USDA endorsement is required but owners don't realise this until it's too late.

**Microchip/certificate mismatch**: if the microchip number on the health certificate doesn't match the number scanned on arrival, the pet cannot be cleared. Check every document.

**Titre test from an unapproved laboratory**: Australia, New Zealand, and the UK maintain lists of approved labs for rabies titre testing. A result from a non-approved lab is not accepted.

**Expired rabies vaccination**: if the vaccination expired before the travel date, the pet doesn't meet the vaccination requirements. Check expiry dates.

## What happens at the border

If border officials identify a problem with your pet's documentation:

1. They will flag the entry and begin a formal assessment
2. You will be asked to wait with your pet (or the pet will be taken to a holding facility)
3. A senior inspector or veterinarian will review the case
4. Possible outcomes: clearance if the error is minor and fixable; temporary detention pending additional documentation; refusal of entry; return to origin

In some countries, pets held pending documentation can remain at airport facilities for days or weeks at the owner's expense. Fees can be significant.

## If your pet is refused

Stay calm and follow the inspector's instructions. Your options typically include:

- Return the pet to the origin country on the next available flight
- If the error is fixable (e.g., a missing endorsement), you may be able to have the documentation corrected and resubmit -- but this varies by country and is at the inspector's discretion

Travel insurance for pets sometimes covers documentation-related delays or returns. Check your policy before you travel.

## Prevention is everything

The good news: documentation-related refusals are almost entirely preventable. Use a checklist for every document, check dates, verify laboratory approvals, and have a transport agent or experienced vet review everything before travel day.

For high-stakes destinations (Australia, New Zealand, Hawaii), have a second person review the complete document pack independently.
"""
    },
    {
        "slug": "pet-transport-with-exotic-pets-birds-reptiles",
        "title": "Travelling Internationally with Birds, Reptiles, and Exotic Pets: What You Need to Know",
        "description": "International travel with birds, reptiles, and exotic pets is far more complex than dogs and cats. CITES permits, country bans, and airline restrictions make this a specialist area.",
        "date": "2026-05-05",
        "tags": ["exotic-pets", "planning", "cites"],
        "faqs": [
            {"q": "Can I take my parrot internationally?", "a": "Many parrot species are covered by CITES Appendix I or II, which means they require export and import permits. Some species are banned from commercial trade entirely. The rules depend heavily on the species and the destination country. Always check the CITES database and contact your destination country's wildlife authority before planning travel."},
            {"q": "Do I need a CITES permit for my pet tortoise?", "a": "Many tortoise species are listed under CITES Appendix I or II. If your tortoise is a CITES-listed species, you will need export and import permits even for personal travel. Proving legal acquisition (captive-bred documentation) is essential. Penalties for CITES violations are severe."},
            {"q": "Can I bring a snake into the UK?", "a": "Some snake species are permitted; others are banned entirely. CITES-listed species require permits. Certain species are banned from import into the UK regardless of documentation. Check with APHA and the CITES trade database before attempting to import any snake species."},
        ],
        "content": """The focus on dogs and cats sometimes overshadows the fact that many families travel internationally with birds, reptiles, fish, rabbits, or other exotic species. The rules for these animals are often considerably stricter -- and in some cases, travel is simply not possible.

## CITES: the international trade framework

The **Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES)** governs the international movement of hundreds of thousands of animal and plant species. Many popular pet species are listed:

**Appendix I** (most restricted -- commercial trade banned): includes some parrot species, certain tortoises, some chameleons, large cats
**Appendix II** (regulated -- permits required): includes many common parrots (African Greys, macaws, cockatiels), many reptiles, some birds of prey
**Appendix III**: requires certificates of origin

If your pet is a CITES-listed species, you will need:

- **Export permit** from the country you are leaving
- **Import permit** from the country you are entering (if required)
- Proof of legal acquisition (captive breeding certificate, purchase documentation)

Without these documents, the animal can be seized at the border, and you may face criminal penalties.

## Birds

Parrots are the most common bird species affected by CITES. African Grey Parrots (CITES Appendix I), Blue and Gold Macaws (Appendix II), and many others require permits. Canaries and budgerigars are not CITES-listed and can generally travel with standard health certificates.

Beyond CITES, birds face **avian influenza** import restrictions in many countries. During outbreaks, import bans may be in place. Check with the destination country's agricultural authority before planning travel.

Australia, New Zealand, and some other countries have strict biosecurity rules for birds that go beyond CITES. Some countries do not permit bird imports at all outside of commercial licensed facilities.

## Reptiles

Many popular reptile species (bearded dragons, leopard geckos, blue-tongue skinks, some tortoises) are subject to CITES controls. Blue-tongue skinks, for instance, require CITES documentation depending on species. Veiled chameleons require Appendix II permits.

Some countries ban the import of reptiles entirely, or restrict certain species for biosecurity reasons. Australia is particularly strict about reptile imports.

## The practical reality

For most exotic pet species, international relocation is:

- Complex and paperwork-intensive
- Time-consuming (permits can take months)
- Expensive (permit fees, specialist transport)
- In some cases, simply not possible

If you are seriously considering travelling internationally with an exotic pet, contact a specialist exotic animal transport agent well in advance -- ideally 6-12 months before your move date.

## Source

CITES trade database: cites.org (verified May 2026). APHA wildlife trade licensing (UK): gov.uk/guidance/cites-permits-and-certificates (verified May 2026).
"""
    },
    {
        "slug": "how-to-prepare-your-pet-for-a-long-haul-flight",
        "title": "How to Prepare Your Pet for a Long-Haul Flight: A Practical Pre-Travel Guide",
        "description": "Long-haul flights are stressful for pets. Here is how to prepare your dog or cat for a 10-20 hour journey, from crate training to pre-travel vet checks.",
        "date": "2026-05-05",
        "tags": ["welfare", "planning", "crate-training"],
        "faqs": [
            {"q": "Should I sedate my pet for a long-haul flight?", "a": "Most vets and veterinary associations advise against sedating pets for air travel. Sedatives can cause respiratory depression at altitude and interfere with the animal's ability to balance in a moving crate. If your pet has severe anxiety, discuss non-sedative calming options with your vet."},
            {"q": "How long before a flight should I stop feeding my pet?", "a": "Most airlines and vets recommend withholding solid food for 4-6 hours before a long flight. Water should remain available up until departure. An empty stomach reduces the chance of vomiting and discomfort during travel."},
            {"q": "How long can a dog be in a crate on a flight?", "a": "IATA guidelines recommend that total crate time (from check-in to collection) should not exceed 48 hours for dogs and cats, with regular checks en route. Most long-haul pet cargo movements stay well within this. For routes over 24 hours, reputable transport agents build in stopovers where permitted."},
        ],
        "content": """The flight itself is often the part pet owners worry most about. The good news: most healthy dogs and cats travel better than their owners expect. The key is preparation.

## Start crate training weeks in advance

If your pet has never spent time in a crate, don't expect them to settle calmly in one for 15 hours. Begin crate training at least **4-6 weeks before travel**:

1. Leave the crate open in a room your pet uses
2. Feed meals near or inside the crate
3. Encourage short periods inside with the door closed
4. Gradually increase the time the door is closed
5. Practice loading and removing your pet calmly

By travel day, the crate should feel like a familiar, safe space -- not a punishment.

## Choose the right crate size

Your pet must be able to **stand fully, sit upright, lie down, and turn around** without touching the sides or top of the crate. Measure your pet carefully:

- Height: floor to top of ears while standing normally
- Length: nose to base of tail
- Width: widest point (usually shoulders or haunches)

Add 10 cm to each dimension. When in doubt, go up a size. Airlines will reject crates that don't meet IATA standards.

## The pre-travel vet check

Book a vet check **at least 2 weeks before travel** -- not 2 days. This gives you time to address any issues the vet identifies.

Your vet should:
- Confirm your pet is healthy enough to fly
- Check microchip is readable and matches documentation
- Review and sign the health certificate (within the required timeframe before travel)
- Advise on any destination-specific requirements you may have missed
- Discuss anxiety management options if needed

## Feeding and water before the flight

- Withhold food for **4-6 hours** before travel (reduces vomiting risk)
- Water should be available until departure; a small frozen water dish in the crate provides hydration during the flight without spillage
- Most crates have a clip-on water bowl -- attach one, even if it's nearly empty

## What to put in the crate

Keep it simple:
- Bedding with your scent (a worn t-shirt works well)
- A small favourite toy that can't be chewed into swallowable pieces
- Clip-on water bowl
- Live animal stickers on the crate (airlines require these)
- "This way up" arrows on all sides

Don't overload the crate -- it needs to be easy to access for welfare checks.

## On the day of travel

- Exercise your dog thoroughly 1-2 hours before drop-off -- tired dogs settle better
- Arrive at the cargo check-in point on time; cargo acceptance has strict cut-off times
- Stay calm. Dogs especially pick up on owner anxiety. Hand over the crate quietly and confidently.
- For cats: minimise stimulation before the journey; a quiet, darkened crate feels safer
"""
    },
    {
        "slug": "pet-transport-south-africa-to-uk",
        "title": "South Africa to UK Pet Transport: What Dogs and Cats Need to Enter Great Britain",
        "description": "Moving from South Africa to the UK with your pet? Here is what APHA requires for dogs and cats from South Africa, including the titre test timeline and tapeworm rules.",
        "date": "2026-05-05",
        "tags": ["south-africa", "uk", "routes"],
        "faqs": [
            {"q": "Does my South African dog need a titre test to enter the UK?", "a": "Yes. South Africa is not on the UK's EU-listed countries list. Dogs from South Africa need a rabies titre test showing 0.5 IU/mL or above, blood drawn at least 30 days post-vaccination, with UK entry at least 3 months after the satisfactory titre test date."},
            {"q": "How long does it take to prepare a pet in South Africa for UK travel?", "a": "Allow at least 4-6 months. The titre test must be drawn 30 days post-vaccination, and UK entry can only happen 3 months after the satisfactory result. If your pet is already vaccinated and has a recent titre test, the timeline may be shorter."},
            {"q": "Which airlines fly from South Africa to the UK for pet cargo?", "a": "South African Airways, British Airways, and Virgin Atlantic operate direct routes between Johannesburg and London. Not all routes accept pets as cargo year-round. Check with airlines directly and book cargo space early."},
        ],
        "content": """South Africa to UK is one of the more common pet relocation routes we see, particularly for South Africans moving to the UK for work or families returning. The process is manageable but requires planning -- the titre test stand-down is the main constraint.

## UK entry requirements for pets from South Africa

South Africa is classified as a **non-EU listed third country** for UK pet travel. Requirements:

- ISO 15-digit microchip (implanted before or same date as first rabies vaccination)
- Rabies vaccination -- valid and current
- Rabies titre test blood drawn at least **30 days after the most recent rabies vaccination**
- Titre test showing **0.5 IU/mL or above** from a UK-approved laboratory
- UK entry at least **3 months after the date of the satisfactory titre test**
- Animal Health Certificate (AHC) issued by a South African Official Veterinarian and endorsed by **DALRRD** (Department of Agriculture, Land Reform and Rural Development) within 10 days of UK arrival
- Dogs only: tapeworm treatment (Praziquantel) by a vet between **1 and 5 days** before arriving in Great Britain

## Getting the titre test done in South Africa

South Africa has several veterinary laboratories capable of performing rabies titre tests for UK purposes. The main approved labs include those operated by the Agricultural Research Council (ARC) and private diagnostic labs. Your vet will know which approved labs they use -- confirm the lab is on the current APHA approved list before the blood draw.

Results typically take 2-3 weeks.

## DALRRD endorsement

The AHC must be endorsed by **DALRRD**. In South Africa, this involves submitting the vet-signed certificate to the nearest DALRRD provincial office or state veterinarian for official endorsement. Allow **5-10 working days** for this process, longer during busy periods.

## Routing from Johannesburg to London

Direct flights from Johannesburg (OR Tambo) to London (Heathrow or Gatwick) operate via South African Airways, British Airways, and Virgin Atlantic. SAA and BA both accept pets in cargo on some routes -- check with the airline's cargo desk for current availability and breed restrictions.

The flight time is approximately 11 hours. Most pets tolerate this well when properly prepared.

## Source

APHA (UK): gov.uk/bring-pet-to-great-britain (verified May 2026). DALRRD (South Africa): dalrrd.gov.za (verified May 2026).
"""
    },
    {
        "slug": "indoor-vs-outdoor-cats-pet-relocation",
        "title": "Indoor vs Outdoor Cats: How International Relocation Changes Everything",
        "description": "Relocating internationally with a cat is different depending on whether they are indoor or outdoor cats. Here is what to expect and how to help your cat adapt.",
        "date": "2026-05-05",
        "tags": ["cats", "welfare", "planning"],
        "faqs": [
            {"q": "How do cats cope with international relocation?", "a": "Cats are territorial animals and find change stressful. Most cats adapt within 2-8 weeks after an international move. The key is giving them a small, safe space initially and allowing them to explore the new environment gradually rather than overwhelming them with space."},
            {"q": "Should I let my cat outside after international relocation?", "a": "Not immediately. Newly arrived cats should be kept indoors for at least 4-6 weeks to establish the new home as their territory. Letting a cat outside too soon in a new country risks them becoming disoriented and not finding their way back."},
            {"q": "Do outdoor cats need different preparation for international travel than indoor cats?", "a": "The documentation requirements are the same. However, outdoor cats may have more exposure to parasites and may need additional parasite treatment history documentation. Destination countries with specific parasite requirements (like Australia and New Zealand) apply the same rules to both."},
        ],
        "content": """Moving internationally with a cat means thinking about more than just the paperwork. Cats are territorial, routine-dependent animals, and the combination of a long flight, an unfamiliar environment, and a completely different climate can be genuinely disorienting for them.

Here is how to approach it depending on your cat's lifestyle.

## Indoor cats: generally easier to relocate

Indoor cats have a smaller established territory (your home) and are already accustomed to being in a controlled environment. They often adapt more quickly to a new country, because they transfer their sense of home to wherever you are and their familiar possessions are.

Practical tips for indoor cats during relocation:

- Keep their bedding, toys, and scratching post with them -- familiar smells help enormously
- Set up one room first at the new destination, with all their usual items, before allowing access to the whole house
- Maintain feeding routines as closely as possible
- A feliway diffuser (synthetic feline pheromone) in the new home can reduce anxiety

## Outdoor cats: the trickier transition

Outdoor cats have established territories that extend well beyond the house -- paths they patrol, places they sleep, social relationships with neighbourhood cats. All of this disappears when they move internationally.

The main risk with outdoor cats after a move: they wander in search of their old territory and can't find their way back to the new home. This happens more often than people expect.

**Keep outdoor cats completely indoors for at least 6-8 weeks** after an international move before allowing any outside access. This is hard for cats that are used to being outside, but it significantly reduces the risk of losing them.

When you do start letting them outside, do it in very short, supervised sessions initially. Feed them inside, so they always have a reason to come back.

## Quarantine countries: an extra complication

For cats moving to Australia or New Zealand, the quarantine period (10 days at the facility) can be stressful for both indoor and outdoor cats. The facility provides professional care, but it is still 10 days away from you and in an unfamiliar environment.

Most cats emerge from Australian quarantine unsettled but physically healthy. Have their familiar bedding waiting for them. Keep the first few days after quarantine calm and low-stimulation.

## The flight itself

Most cats tolerate the flight better than their owners expect. Cats in cargo hold travel in pressurised, temperature-controlled holds -- not in the luggage area. IATA-compliant crates provide adequate ventilation and space.

The most stressful part for cats is usually the handling at airports -- the noise, the movement, the unfamiliar smells. A crate that smells of home (put worn bedding in it) helps.
"""
    },
]


def write_article(article):
    filepath = os.path.join(BLOG_DIR, article["slug"] + ".md")
    if os.path.exists(filepath):
        print(f"SKIP (exists): {article['slug']}")
        return

    faqs_yaml = ""
    for faq in article.get("faqs", []):
        q = faq["q"].replace('"', '\\"')
        a = faq["a"].replace('"', '\\"')
        faqs_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    tags_yaml = "\n".join(f'  - "{t}"' for t in article.get("tags", []))

    frontmatter = f"""---
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
{faqs_yaml}---

{article['content'].strip()}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
    print(f"WROTE: {article['slug']}")


for article in ARTICLES:
    write_article(article)

print(f"\nDone. {len(ARTICLES)} articles processed.")
