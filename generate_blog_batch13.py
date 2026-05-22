# -*- coding: utf-8 -*-
"""generate_blog_batch13.py -- Blog batch 13 (28 articles).
Country guides: Romania, Singapore, South Korea, Spain, Switzerland, Thailand,
Philippines, Myanmar, Taiwan.
Route guides: USA-Ireland, USA-Netherlands, Spain-Australia, UK-South Africa,
Japan-USA.
Breed guides: Bernese Mountain Dog, Bengal cat, Norwegian Forest Cat, Jack
Russell Terrier, Akita, Samoyed.
Practical: fish travel, reptile travel, moving to NZ, UK-AU cost, USA-EU cost,
import permits by country, summer heat precautions, air freight vs manifest cargo.
"""

import os
import sys

BLOG_DIR = os.path.join("site", "content", "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    # ------------------------------------------------------------------ #
    # COUNTRY IMPORT GUIDES                                                #
    # ------------------------------------------------------------------ #
    {
        "slug": "romania-pet-import-guide",
        "title": "Romania Pet Import Guide 2026",
        "description": "Everything you need to know about bringing a dog or cat into Romania. EU Pet Travel Scheme rules, microchip, rabies vaccine, and health certificate requirements.",
        "date": "2026-05-08",
        "tags": ["romania", "eu pet travel", "dog import", "cat import", "microchip"],
        "faqs": [
            {
                "question": "What documents do I need to bring my pet to Romania?",
                "answer": "Romania follows the EU Pet Travel Scheme. You need an ISO 15444 microchip, a valid rabies vaccination (given after microchipping), and an EU animal health certificate or EU pet passport. If travelling from outside the EU, your vet must complete an official health certificate endorsed by your government veterinary authority. From the UK post-Brexit, this is the AHC (Animal Health Certificate) endorsed by APHA."
            },
            {
                "question": "Does Romania require a rabies titre test for pet entry?",
                "answer": "A titre test is only required if your pet is travelling from a country that is not approved under EU rules. Most Western countries, including the USA, Canada, and Australia, require pets to have a valid titre test result of at least 0.5 IU/ml taken no less than three months after vaccination. Check the EU's TRACES system for your country's specific status."
            },
            {
                "question": "Can I bring my pet into Romania from the UK?",
                "answer": "Yes. Since Brexit, UK pets entering Romania (and all EU countries) need an AHC issued by a listed vet and endorsed by APHA. The AHC is valid for 10 days of travel. If your pet previously held an EU pet passport, that is no longer valid for re-entry into the EU from the UK."
            }
        ],
        "body": """Romania is a full EU member state, which means it applies the EU Pet Travel Scheme to all incoming animals. The rules are consistent with every other EU country, which is genuinely helpful if you are relocating across multiple European borders.

## What Romania requires for pet entry

Your pet must be microchipped to ISO standard 15444 before any vaccinations are administered. Rabies vaccination must be current and given after the microchip was inserted. A valid EU animal health certificate (AHC) or EU pet passport is required for entry.

Pets arriving from non-EU countries with approved status (such as the USA, Canada, Australia, and Japan) also need a satisfactory rabies antibody titre test result. The test must show a result of at least 0.5 IU/ml, taken at an EU-approved laboratory, and the sample must have been collected at least 30 days after vaccination and no less than three months before travel.

The titre test waiting period is the main timeline driver for most owners moving to Romania from outside Europe. Plan for a minimum of four to five months from the point your pet is microchipped and vaccinated to the point they can travel.

## Entering Romania from the UK

Since Brexit, UK-issued EU pet passports are no longer valid for EU entry. Instead, you need an Animal Health Certificate (AHC) completed by a listed vet in the UK and endorsed by the Animal and Plant Health Agency (APHA).

AHC endorsement typically takes three to five working days. The certificate is valid for 10 days from the date of the official vet examination, so timing matters. If your travel plans change, you may need to get a fresh certificate.

APHA recommends booking endorsement slots well in advance, especially during busy relocation periods in summer.

## Health certificate for Romania from other countries

If you are travelling from the USA, Canada, Australia, or another non-EU country, your government veterinary authority must endorse the health certificate. In the USA this is USDA APHIS, in Canada it is the CFIA, and in Australia it is the Department of Agriculture, Fisheries and Forestry (DAFF).

The Romanian Border Inspection Post (BIP) at Bucharest Henri Coanda Airport (OTP) handles incoming pet arrivals. Airlines operating cargo and excess baggage pet services typically handle the paperwork submission on arrival.

## Breed restrictions in Romania

Romania has no additional breed-specific import bans beyond any airline restrictions that may apply to brachycephalic dogs. However, Romanian law does regulate dangerous breeds domestically (including Pit Bull Terrier, Boerboel, Tosa Inu, and others), so if you are planning to live in Romania with one of these breeds, check local registration requirements.

## Costs and practical tips

Health certificate fees vary by country and endorsement body. In the UK, expect to pay GBP 30 to 100 for vet preparation and GBP 30 for APHA endorsement. Airline pet fees depend on carrier and whether the animal travels in cabin or as cargo.

Romania is served by numerous European carriers including Tarom (the national airline), Wizz Air, Ryanair, and British Airways. Not all of these accept pets, so confirm your preferred airline's policy before booking.

**Quick reference sources:**
- EU Pet Travel Scheme: European Commission, Directorate-General Health and Food Safety
- UK AHC information: APHA (Animal and Plant Health Agency), GOV.UK
- Romanian BIP information: Romanian National Sanitary Veterinary and Food Safety Authority (ANSVSA)
"""
    },
    {
        "slug": "singapore-pet-import-guide",
        "title": "Singapore Pet Import Guide 2026",
        "description": "How to bring your dog or cat to Singapore. AVS approved country lists, import permits, quarantine requirements, and timeline planning for the Lion City.",
        "date": "2026-05-08",
        "tags": ["singapore", "AVS", "pet quarantine", "dog import", "cat import"],
        "faqs": [
            {
                "question": "Does Singapore require quarantine for imported pets?",
                "answer": "Yes. Dogs and cats imported to Singapore must undergo a period of post-arrival quarantine at an AVS-approved facility. The quarantine duration depends on where your pet is coming from. Pets from Group 1 countries (such as Australia, New Zealand, the UK, and other approved low-risk countries) typically serve a shorter quarantine of around 10 days. Pets from Group 2 and Group 3 countries face longer stays."
            },
            {
                "question": "How do I get an import permit for my pet in Singapore?",
                "answer": "You must apply for an import licence through the Animal and Veterinary Service (AVS), a cluster of the National Parks Board (NParks). Applications are submitted online via the GoBusiness Licensing portal. You will need to supply microchip number, vaccination records, and details of your approved quarantine facility. Apply at least 30 days before travel."
            },
            {
                "question": "Which countries are on Singapore's Group 1 approved list?",
                "answer": "Singapore's Group 1 list includes countries considered to have low rabies risk and equivalent biosecurity standards. Countries currently on the list include Australia, New Zealand, the UK, Ireland, Japan, Taiwan, and several others. The full and current list is published by AVS/NParks. Countries not on the list face stricter requirements and longer quarantine."
            }
        ],
        "body": """Singapore takes biosecurity seriously, and the import rules for pets reflect that. The country is rabies-free and intends to stay that way. If you are planning to bring a dog or cat to Singapore, the key word is preparation: the process is very manageable but it takes time.

## Singapore's pet import group system

AVS (Animal and Veterinary Service, a cluster of NParks) categorises origin countries into groups based on disease risk. Group 1 countries face the simplest process and shortest quarantine. Group 2 and 3 countries face additional requirements and longer quarantine periods.

Group 1 currently includes: Australia, New Zealand, the United Kingdom, Ireland, Japan, Taiwan, Hong Kong, and a handful of others. If you are coming from the USA, Canada, or most European countries, you are likely in Group 2, which means a longer quarantine at an AVS-approved facility.

Always verify your country's current group status on the NParks/AVS website before starting preparations. The list is reviewed periodically.

## What your pet needs before departure

For most origin countries, your pet will need:

- An ISO 15444 microchip (implanted before vaccinations)
- A current rabies vaccination (and often a booster)
- For Group 2 and 3 countries: a satisfactory rabies titre test at an approved laboratory
- A health certificate issued by a government-listed veterinarian and endorsed by your national veterinary authority
- An import licence issued by AVS Singapore (applied for in advance)

## Applying for the import licence

Singapore requires you to have an approved quarantine facility booked before you can apply for the licence. You cannot simply arrive with your pet. AVS-approved quarantine facilities are listed on the NParks website, and most are private boarding facilities that have met Singapore's standards.

Apply via the GoBusiness Licensing portal at least four weeks before your intended travel date. The licence specifies the entry point, quarantine facility, and validity period.

## Quarantine at an approved facility

On arrival, your pet will be transported directly to the approved quarantine facility. Owners are typically able to visit during the quarantine period, though specific visiting arrangements vary by facility.

Quarantine costs are not included in airline or import licence fees. Expect to pay SGD 30 to 80 per day for quarantine, plus any veterinary checks required during the stay.

## Breed restrictions

Singapore bans the import of certain breeds considered dangerous. The current list includes Pit Bull Terrier, Neapolitan Mastiff, Tosa, American Bulldog, and several others. Some restricted breeds can be kept by existing owners under a licensing scheme but cannot be newly imported.

Brachycephalic dogs and cats are allowed but may face airline restrictions. Air cargo is the most common method for pet transport to Singapore.

## Getting your pet to Singapore

Most pets travel as manifest cargo or excess baggage in the hold. Singapore Airlines, Qantas, British Airways, and Lufthansa are among the carriers that operate cargo pet services on routes to Changi Airport (SIN).

**Official sources:**
- NParks/AVS Singapore pet import: nparks.gov.sg
- Import licence applications: GoBusiness Licensing portal
- Approved quarantine facilities: NParks website
"""
    },
    {
        "slug": "south-korea-pet-import-guide",
        "title": "South Korea Pet Import Guide 2026",
        "description": "Bringing a dog or cat to South Korea explained. APQA import requirements, microchip, rabies vaccination, titre test rules, and how to avoid quarantine delays.",
        "date": "2026-05-08",
        "tags": ["south korea", "APQA", "pet import", "dog import", "korea"],
        "faqs": [
            {
                "question": "Does South Korea require quarantine for imported pets?",
                "answer": "South Korea may require a period of quarantine for pets arriving from countries that do not have a recognised equivalent animal health status. Pets arriving from countries with valid rabies vaccination records and satisfactory titre test results (where required) can often be cleared at the border without extended quarantine. The Animal and Plant Quarantine Agency (APQA) makes the final determination on arrival."
            },
            {
                "question": "What documents does South Korea require to import a dog?",
                "answer": "You need: an ISO 15444 microchip implanted before vaccination; current rabies vaccination; a rabies titre test (if coming from a non-approved country) showing at least 0.5 IU/ml; a health certificate issued within 10 days of travel by an accredited veterinarian and endorsed by your national authority (e.g. USDA APHIS in the USA, APHA in the UK); and a declaration form submitted to APQA at the port of entry."
            },
            {
                "question": "Can I bring my dog to South Korea from the UK?",
                "answer": "Yes. The UK is generally considered a low-risk origin country, and pets with valid rabies vaccination records, current health certificates endorsed by APHA, and ISO microchips can enter South Korea. A titre test is recommended as an added precaution. Contact the Korean Embassy or APQA directly to confirm current requirements before travel."
            }
        ],
        "body": """South Korea is a popular destination for expats from the USA, UK, Australia, and Japan, and each year thousands of pets make the journey. The import process is handled by APQA (Animal and Plant Quarantine Agency) and is straightforward if you start your paperwork early.

## What APQA requires

The core requirements for importing a dog or cat to South Korea are:

- ISO 15444 microchip (implanted before vaccination)
- Rabies vaccination given after microchipping, with a current booster
- Rabies antibody titre test from an approved laboratory, showing a result of at least 0.5 IU/ml (required for pets from most non-Korean-approved countries)
- Official health certificate, issued within 10 days of travel and endorsed by your national authority
- APQA inspection on arrival at Incheon International Airport (ICN)

## The titre test timeline

If a titre test is required, the sample must be taken at least 30 days after the most recent rabies vaccination. Many APQA-accepted laboratories require the sample to be from a blood draw performed at least 90 days before travel to allow for processing and documentation.

This is the single biggest timeline factor. Start planning at least five to six months before your intended move if your pet needs a titre test.

## South Korea from the USA

Pets from the USA need a health certificate endorsed by USDA APHIS. APHIS endorsement takes three to five business days in normal circumstances, so book your vet appointment and APHIS slot at least two weeks before the flight.

The USA is not on South Korea's list of countries with equivalent disease-free status, so a titre test is required for dogs. Cats have slightly different rules, check with APQA for the current cat-specific requirements.

## South Korea from the UK

Post-Brexit, UK pets need an AHC endorsed by APHA. The process is similar to the USA pathway above. A titre test is also advisable. APHA recommends applying for endorsement at least five working days in advance.

## Arriving at Incheon Airport

Incheon Airport (ICN) has an APQA inspection facility at Terminal 1. On arrival, your documents will be inspected and your pet's microchip confirmed. If everything is in order, your pet will be cleared and released to you or your cargo agent. Pets that fail documentation checks may be held for further inspection or returned to origin at the owner's expense.

## Breed restrictions and local rules

South Korea does not have a national breed ban, but local authorities in Seoul and some other cities regulate certain breeds. Pit Bull Terrier types are the most commonly restricted. Always check local registration requirements once you have settled.

**Official sources:**
- APQA (Animal and Plant Quarantine Agency): qia.go.kr
- Korean Ministry of Agriculture, Food and Rural Affairs: mafra.go.kr
"""
    },
    {
        "slug": "spain-pet-import-guide",
        "title": "Spain Pet Import Guide 2026",
        "description": "How to bring your pet to Spain. EU Pet Travel Scheme requirements, health certificate rules from the UK and non-EU countries, and what to expect on arrival.",
        "date": "2026-05-08",
        "tags": ["spain", "eu pet travel", "dog import", "cat import", "apha"],
        "faqs": [
            {
                "question": "What paperwork does my dog need to enter Spain?",
                "answer": "Spain follows the EU Pet Travel Scheme. Your dog needs an ISO 15444 microchip, a valid rabies vaccination administered after microchipping, and either an EU pet passport (for EU-resident pets) or an official animal health certificate (AHC) endorsed by your national veterinary authority. UK pets need an AHC endorsed by APHA."
            },
            {
                "question": "Do I need a rabies titre test to bring my dog to Spain?",
                "answer": "A titre test is required for pets arriving from countries outside the EU that are not on the EU-approved list. This includes pets from the USA, Canada, Australia, and many other non-EU countries. The test must show a result of at least 0.5 IU/ml and must be taken at least 30 days after vaccination and at least three months before travel to Spain."
            },
            {
                "question": "Can I bring my cat to Spain from the UK?",
                "answer": "Yes. From the UK post-Brexit, you need an AHC issued by a listed vet and endorsed by APHA. This applies to cats and dogs equally. A UK EU pet passport is no longer accepted for re-entry into EU countries including Spain. Allow five to 10 working days for APHA endorsement."
            }
        ],
        "body": """Spain is one of the most popular destinations for relocating pet owners, whether for retirement, remote work, or an EU move. The good news is that Spain, as an EU member, applies the same well-established EU Pet Travel Scheme as France, Germany, Italy, and every other EU country.

## EU Pet Travel Scheme basics

To bring a dog, cat, or ferret into Spain, your pet needs:

1. An ISO 15444 microchip (implanted before the first rabies vaccination)
2. A valid rabies vaccination, given after the microchip
3. An EU pet passport (for EU-resident pets) or an official health certificate (for non-EU pets)
4. A rabies titre test result of at least 0.5 IU/ml, if arriving from a non-approved third country

Pets arriving with owners from within the EU travelling by road, ferry, or air need only a valid EU pet passport and their vaccination records.

## Arriving from the UK

Since January 2021, UK-issued EU pet passports are no longer valid for re-entry into the EU. UK pet owners travelling to Spain need:

- An Animal Health Certificate (AHC) completed by a listed vet in the UK
- Endorsement by APHA (Animal and Plant Health Agency)
- The AHC is valid for 10 days of travel

APHA endorsement typically takes three to five working days. Book your vet appointment and APHA slot at least 10 days before your departure to allow for any delays.

If you already hold a Spanish residency permit and have registered your pet on the Spanish registry (REIAC), check with your vet whether your pet's existing paperwork is sufficient for re-entry after a visit to the UK.

## Arriving from the USA, Canada, or Australia

Pets from non-EU countries need a health certificate endorsed by their national authority (USDA APHIS for the USA, CFIA for Canada, DAFF for Australia) and a titre test if required for their origin country.

Most airline pet cargo services flying to Madrid (MAD), Barcelona (BCN), or Malaga (AGP) can advise on document submission through the TRACES system, which Spain uses for registering pet arrivals.

## Registering your pet in Spain

Once settled in Spain, you will need to register your pet on the Spanish national pet registry (REIAC) and with your local municipality. Spanish law requires all dogs to be microchipped and registered. Failure to register can result in fines.

Spain also has regional breed-specific legislation (BSL). The national list of potentially dangerous breeds (PPP breeds) includes American Pit Bull Terrier, Rottweiler, Fila Brasileiro, Tosa Inu, and several others. PPP breed owners need a special licence, third-party liability insurance, and must keep the dog on a lead and muzzled in public.

**Official sources:**
- EU Pet Travel Scheme: European Commission, DG SANTE
- APHA UK pet export: GOV.UK/APHA
- Spanish Ministry of Agriculture, Fisheries and Food: mapa.gob.es
"""
    },
    {
        "slug": "switzerland-pet-import-guide",
        "title": "Switzerland Pet Import Guide 2026",
        "description": "Importing a dog or cat to Switzerland explained. Switzerland follows EU-equivalent rules but has its own authority. Health certificate, titre test, and registration requirements.",
        "date": "2026-05-08",
        "tags": ["switzerland", "pet import", "dog import", "cat import", "eu equivalent"],
        "faqs": [
            {
                "question": "Does Switzerland follow EU pet travel rules?",
                "answer": "Switzerland is not an EU member but it is part of the Schengen Area and has a bilateral agreement with the EU on the movement of animals. In practice, Switzerland applies rules that are equivalent to the EU Pet Travel Scheme. Dogs and cats travelling to Switzerland need a microchip, valid rabies vaccination, and a health certificate. EU pet passports are accepted in Switzerland."
            },
            {
                "question": "Do UK pets need a special certificate to enter Switzerland?",
                "answer": "Yes. Post-Brexit UK pets cannot use EU pet passports for re-entry into Switzerland. UK owners need an official health certificate endorsed by APHA. Switzerland has bilateral recognition with the UK for this purpose. The AHC format used for EU entry is also accepted in Switzerland. Allow five to 10 working days for APHA endorsement."
            },
            {
                "question": "Does Switzerland require a titre test for dogs from the USA or Australia?",
                "answer": "Switzerland follows EU rules for titre test requirements. Pets arriving from countries outside the EU approved list (which includes the USA, Canada, Australia, and others) need a rabies titre test result of at least 0.5 IU/ml. The test must be performed at least 30 days after vaccination and the pet cannot travel for at least three months after the sample was taken."
            }
        ],
        "body": """Switzerland sits at the heart of Europe and is one of the most welcoming countries for pet owners, with excellent veterinary care, generous public transport access for pets, and clear import rules. The process is virtually identical to entering an EU country.

## How Switzerland's pet rules work

Switzerland is part of the Schengen Area and applies animal health rules that mirror the EU Pet Travel Scheme. The Federal Food Safety and Veterinary Office (FSVO) oversees pet imports and uses the same microchip, vaccination, and titre test framework as the EU.

For travel from within the EU, a valid EU pet passport and accompanying health records are sufficient. For travel from outside the EU (including the UK post-Brexit, the USA, Canada, and Australia), an official health certificate endorsed by the relevant national authority is required.

## Requirements at a glance

- ISO 15444 microchip implanted before any rabies vaccination
- Rabies vaccination given after the microchip, current booster record
- Titre test result of at least 0.5 IU/ml (for pets from non-EU-approved countries)
- Official health certificate endorsed by national authority (USDA APHIS, APHA, CFIA, DAFF, etc.)
- Entry via a registered border crossing point

## UK pets entering Switzerland

From the UK, owners need an AHC endorsed by APHA. Switzerland explicitly accepts this document. The Swiss FSVO has confirmed that UK-style AHC forms are valid for Swiss entry. The AHC is valid for 10 days from the date of the official vet examination.

## Arriving and registering in Switzerland

Switzerland does not have a national pet registry equivalent to some EU countries, but all dogs must be registered with the cantonal authority in the canton where they live. Many cantons use the AMICUS central database. Failure to register your dog can result in a fine.

Dogs in Switzerland must be on a lead in public unless in designated off-lead areas. Some cantons have additional rules about specific breeds, so check the regulations in your specific canton after arrival.

## Costs and practicalities

Switzerland is an expensive country, and veterinary costs reflect this. Budget accordingly for any health certificates or veterinary checks required on arrival.

Airlines serving Zurich (ZRH), Geneva (GVA), and Basel (BSL) include Swiss International Air Lines, Lufthansa, British Airways, Air France, and others. Swiss International Air Lines accepts pets as checked baggage (up to 8 kg cabin) and as cargo.

**Official sources:**
- FSVO (Federal Food Safety and Veterinary Office): blv.admin.ch
- APHA UK pet export: GOV.UK/APHA
"""
    },
    {
        "slug": "thailand-pet-import-guide",
        "title": "Thailand Pet Import Guide 2026",
        "description": "How to bring your dog or cat to Thailand. DLD import permit, rabies vaccination, health certificate rules, and what happens at Bangkok Suvarnabhumi airport.",
        "date": "2026-05-08",
        "tags": ["thailand", "DLD", "pet import", "dog import", "bangkok"],
        "faqs": [
            {
                "question": "Do I need an import permit to bring my pet to Thailand?",
                "answer": "Yes. An import permit from the Department of Livestock Development (DLD) is mandatory for all dogs and cats entering Thailand. Apply at least 15 to 30 days before your travel date. The DLD may take one to two weeks to process applications. Without a confirmed import permit, your pet may be refused entry or held in quarantine at your expense."
            },
            {
                "question": "What vaccinations does my dog need for Thailand?",
                "answer": "Thailand requires dogs and cats to be vaccinated against rabies. The vaccination must be current (not expired) and was administered after the microchip was implanted. A valid health certificate issued within 10 days of travel by an accredited veterinarian is also required, along with endorsement by your national veterinary authority."
            },
            {
                "question": "Is there quarantine for pets arriving in Thailand?",
                "answer": "Thailand does not impose a mandatory quarantine period for most pets arriving with valid documentation. However, all animals are inspected by DLD officers on arrival at the airport. If documentation is incomplete or the animal appears unwell, the DLD has authority to detain the animal for further inspection or quarantine at a government facility, at the owner's cost."
            }
        ],
        "body": """Thailand is home to a large expat community and is increasingly popular as a long-stay destination. Bringing your pet is absolutely possible, and the rules are clearer than many people expect, but you do need to apply for an import permit in advance.

## Thailand's import permit requirement

The Department of Livestock Development (DLD) controls all animal imports into Thailand. Before your pet can enter the country, you must have a confirmed import permit from the DLD. Without it, your airline may refuse to load your pet, or Thai customs may refuse entry on arrival.

Apply through the DLD website or via a local agent. The application requires microchip number, vaccination records, and your arrival details. Processing typically takes one to two weeks. Apply at least 30 days before travel to allow time for any queries.

## Core documentation

- ISO 15444 microchip implanted before vaccination
- Current rabies vaccination (and distemper, parvovirus, and other core vaccines are recommended)
- Official health certificate from an accredited vet, issued within 10 days of travel
- Government endorsement of the health certificate (USDA APHIS, APHA, CFIA, DAFF, etc.)
- Import permit number from DLD

## Arriving at Suvarnabhumi Airport

Bangkok Suvarnabhumi (BKK) and Don Mueang (DMK) both handle pet arrivals. At Suvarnabhumi, DLD inspection happens at the cargo terminal rather than the passenger arrival hall, so pets travelling as manifest cargo have a different handling process from pets travelling as excess baggage.

Confirm with your airline whether your pet will be collected by you directly or will need to be cleared through the cargo terminal, as this affects timing and any additional handling fees.

## After arrival in Thailand

Thailand has no national pet registry, but rabies vaccination records should be kept up to date. There are no breed-specific import bans at the national level, though individual airlines may restrict brachycephalic breeds.

Thailand is a hot and humid country year-round. Consider the timing of your pet's flight carefully: early morning or late evening departures reduce the risk of heat stress during ground handling.

**Official sources:**
- Department of Livestock Development (DLD): dld.go.th
- Thai Customs: customs.go.th
"""
    },
    {
        "slug": "philippines-pet-import-guide",
        "title": "Philippines Pet Import Guide 2026",
        "description": "Importing a dog or cat to the Philippines explained. BAI import permit, quarantine rules, rabies vaccine requirements, and how long the process takes.",
        "date": "2026-05-08",
        "tags": ["philippines", "BAI", "pet import", "quarantine", "dog import"],
        "faqs": [
            {
                "question": "How long is quarantine for pets arriving in the Philippines?",
                "answer": "Dogs and cats arriving in the Philippines must undergo a minimum of seven days of quarantine at a Bureau of Animal Industry (BAI) approved facility. Pets from countries not on the BAI approved list may face a longer quarantine of up to 30 days. Quarantine is mandatory regardless of documentation status."
            },
            {
                "question": "Do I need an import permit from BAI?",
                "answer": "Yes. An import permit from the Bureau of Animal Industry (BAI) is required before your pet can enter the Philippines. Apply to BAI at least 30 days before your travel date. The permit specifies the port of entry, arrival date window, and approved quarantine facility."
            },
            {
                "question": "What vaccinations does my pet need for the Philippines?",
                "answer": "At minimum, dogs need a current rabies vaccination and a distemper, hepatitis, and parvovirus (DHPPi) vaccination. Cats need a current rabies vaccination and a feline respiratory combination vaccine. A health certificate from an accredited vet, endorsed by your national authority, is required, along with the BAI import permit."
            }
        ],
        "body": """The Philippines is a popular destination for expats, with large communities in Manila, Cebu, and around the US military bases on Luzon. Importing a pet requires advance planning and a mandatory quarantine period, but thousands of pets make this journey every year.

## Import permit from BAI

The Bureau of Animal Industry (BAI) under the Department of Agriculture handles all pet imports. You must apply for an import permit before your pet travels. Applications can be submitted online through the BAI website or in person at BAI offices.

The permit specifies an entry window (usually a week or two) and names the approved quarantine facility. You cannot switch facilities after the permit is issued without reapplying. Apply at least 30 days before your intended travel date, and allow more time if you are applying during holiday periods.

## Quarantine requirements

All dogs and cats must complete a minimum seven-day quarantine at a BAI-approved facility. Animals from countries with a higher disease risk profile may be required to undergo 30 days of quarantine. The quarantine period starts on the day of arrival, not the day of release from customs.

Quarantine facilities are located near major airports. Most are private kennelling operations that have met BAI standards. Owners can visit during the quarantine period at most facilities. Costs range from PHP 500 to 2,000 per day depending on the facility and species.

## What your pet needs

- ISO 15444 microchip
- Current rabies vaccination (primary and booster)
- Core vaccinations for the species (DHPPi for dogs, feline respiratory for cats)
- Official health certificate from an accredited vet, issued within 10 days of travel
- Government endorsement (USDA APHIS, APHA, CFIA, etc.)
- BAI import permit issued in advance

## Arriving at Ninoy Aquino International Airport

NAIA Terminal 1 and Terminal 3 both handle international arrivals. Pets travelling as cargo or excess baggage are processed at the cargo area. BAI officers inspect documents and confirm the microchip on arrival before releasing the animal to the approved quarantine facility.

## Breed restrictions

The Philippines has no national breed ban but individual municipalities may have additional regulations. Brachycephalic breeds face airline restrictions from most carriers serving Manila, which may affect your route choices.

**Official sources:**
- Bureau of Animal Industry (BAI): bai.gov.ph
- Department of Agriculture Philippines: da.gov.ph
"""
    },
    {
        "slug": "myanmar-pet-import-guide",
        "title": "Myanmar Pet Import Guide 2026",
        "description": "What you need to know about bringing a dog or cat to Myanmar. Veterinary import certificate, health documentation, and practical advice for relocating with pets.",
        "date": "2026-05-08",
        "tags": ["myanmar", "burma", "pet import", "dog import", "veterinary certificate"],
        "faqs": [
            {
                "question": "What documents do I need to bring my pet to Myanmar?",
                "answer": "Myanmar requires a veterinary health certificate from an accredited vet in your country of origin, endorsed by your national veterinary authority. Rabies vaccination is required. A microchip is strongly recommended. Myanmar does not currently operate a formal import permit system equivalent to countries like Singapore or the Philippines, but all animals must be declared to customs on arrival."
            },
            {
                "question": "Is there quarantine for pets arriving in Myanmar?",
                "answer": "Myanmar does not have a standardised mandatory quarantine programme for pet dogs and cats from low-risk countries, unlike Singapore or Australia. However, customs and veterinary officers on arrival have discretion to hold animals for inspection if documentation appears incomplete. This can add days of delay, so ensuring your paperwork is thorough is important."
            },
            {
                "question": "Are there flights to Myanmar that accept pets?",
                "answer": "International flights to Yangon (RGN) are limited compared to other Southeast Asian hubs. The airline options for carrying pets to Myanmar as cargo or excess baggage are restricted. Thai Airways, Myanmar National Airlines, and a small number of regional carriers operate services. Confirm pet acceptance directly with any carrier before booking."
            }
        ],
        "body": """Myanmar (Burma) is a less commonly covered destination in pet transport guides, but there is a steady flow of expats, NGO workers, and diplomatic staff who relocate with pets. The import rules are less formalised than those of neighbouring Singapore or Thailand, but that does not mean anything goes.

## What Myanmar requires for pet entry

Myanmar's veterinary import framework is administered by the Department of Animal Husbandry, Land Management and Statistics (DALHMS) under the Ministry of Agriculture, Livestock and Irrigation.

The core requirements are:
- A veterinary health certificate from an accredited vet in the country of origin
- Endorsement by the national veterinary authority (USDA APHIS, APHA, CFIA, etc.)
- Current rabies vaccination record
- Microchip strongly recommended (ISO 15444 preferred)

Myanmar does not have a published equivalent of Singapore's AVS approved country list, so requirements can be applied with some flexibility by customs officers. Having thorough documentation is your best protection.

## Practical considerations

Direct international flights to Yangon (RGN) have reduced significantly in recent years. Bangkok (BKK) is the most common transit hub for Myanmar-bound passengers, but transit rules for pets vary and many carriers do not accept pets on short-haul connections.

If you are relocating to Myanmar for work, consult your employer or relocation agent about current ground transport options from Bangkok, which some expats prefer for moving pets due to the road crossing at Myawaddy or Mae Sot.

## Veterinary care in Myanmar

Quality veterinary care in Myanmar is concentrated in Yangon and Mandalay. If you are relocating to a more remote area, research veterinary services carefully before committing, as emergency care for animals can be difficult to access outside major cities.

Ensure your pet's vaccinations, including rabies, are up to date before departure, as access to certain vaccines may be limited locally.

**Official sources:**
- DALHMS: moali.gov.mm
- USDA APHIS pet travel: aphis.usda.gov/pet-travel
"""
    },
    {
        "slug": "taiwan-pet-import-guide",
        "title": "Taiwan Pet Import Guide 2026",
        "description": "Bringing your dog or cat to Taiwan explained. COA import permit, 21-day quarantine rules, rabies titre test, and how the quarantine process works at Taoyuan Airport.",
        "date": "2026-05-08",
        "tags": ["taiwan", "COA", "pet quarantine", "dog import", "21 days"],
        "faqs": [
            {
                "question": "How long is quarantine for pets arriving in Taiwan?",
                "answer": "Most dogs and cats arriving in Taiwan must serve a 21-day quarantine at a government-approved facility. Pets arriving from designated rabies-free countries or areas may be eligible for a shorter 12-day home quarantine, subject to COA approval. Pets from high-risk origin countries may face longer quarantine. The Council of Agriculture (COA) publishes the current country risk classifications."
            },
            {
                "question": "Do I need an import permit for Taiwan?",
                "answer": "Yes. You must obtain an import permit from the Bureau of Animal and Plant Health Inspection and Quarantine (BAPHIQ) under the COA. Apply at least three to four weeks before your travel date. The permit specifies the port of entry, arrival window, and approved quarantine facility."
            },
            {
                "question": "Does my dog need a titre test to enter Taiwan?",
                "answer": "A rabies titre test is required for dogs arriving from countries that are not on Taiwan's designated rabies-free list. The test must be performed at a BAPHIQ-approved laboratory. The result must show at least 0.5 IU/ml and the test must be taken at least 30 days after the most recent rabies vaccination."
            }
        ],
        "body": """Taiwan has a reputation for strict biosecurity at its borders, and the pet import rules reflect this. The country is rabies-free and the 21-day quarantine requirement is the centrepiece of its protection system. However, the process is well-organised and well-explained, and many pet owners navigate it without problems.

## Taiwan's quarantine system

The Bureau of Animal and Plant Health Inspection and Quarantine (BAPHIQ), under the Council of Agriculture (COA), manages all animal imports. Dogs and cats must serve a minimum 21-day quarantine at a BAPHIQ-approved facility. There is no option to bypass this.

Some countries are on Taiwan's designated rabies-free list, which may allow pets to qualify for home quarantine instead of facility quarantine, at BAPHIQ's discretion. Countries currently on this list include Australia, New Zealand, Japan, Singapore, Iceland, and a small number of others.

## Applying for the import permit

Apply to BAPHIQ at least four weeks before travel. You will need to provide:
- Microchip number
- Vaccination records (rabies and other core vaccines)
- Titre test results (where required)
- Details of the quarantine facility you intend to use
- Your personal identification and Taiwan arrival details

BAPHIQ issues the permit and specifies the conditions of the quarantine stay.

## Core requirements

- ISO 15444 microchip implanted before vaccination
- Current rabies vaccination
- Rabies titre test from a BAPHIQ-approved laboratory (if required for your origin country)
- Health certificate endorsed by national authority
- BAPHIQ import permit

## Arriving at Taoyuan Airport

Pets travelling to Taiwan arrive through Taoyuan International Airport (TPE). The BAPHIQ inspection unit is located at the cargo terminal for manifest cargo shipments. Pets travelling as excess baggage in the hold are processed at the animal quarantine facility after customs clearance.

Your quarantine facility should arrange collection. Confirm this with the facility in advance.

## Breed restrictions

Taiwan bans the import of dogs classified as aggressive breeds. The list includes Pit Bull Terrier, Tosa Inu, Dogo Argentino, and Fila Brasileiro. Owners of other breeds should confirm whether any airline or authority restrictions apply.

**Official sources:**
- BAPHIQ Taiwan: baphiq.gov.tw
- Council of Agriculture Taiwan: coa.gov.tw
"""
    },
    # ------------------------------------------------------------------ #
    # ROUTE GUIDES                                                         #
    # ------------------------------------------------------------------ #
    {
        "slug": "usa-to-ireland-pet-transport-guide",
        "title": "Pet Transport USA to Ireland 2026 | Complete Guide",
        "description": "Moving your dog or cat from the USA to Ireland. Rabies titre test, USDA APHIS health cert, EU entry rules via Dublin, and how long the whole process takes.",
        "date": "2026-05-08",
        "tags": ["usa to ireland", "pet transport", "usda aphis", "titre test", "eu entry"],
        "faqs": [
            {
                "question": "How long does it take to move a pet from the USA to Ireland?",
                "answer": "Planning a minimum of five to six months is wise. Your pet needs a microchip, a rabies vaccination, and then a titre test taken at least 30 days after vaccination. The result must be satisfactory (at least 0.5 IU/ml) and you cannot travel for at least three months after the titre blood draw. On top of this, allow time for USDA APHIS endorsement of the health certificate, which takes three to five business days."
            },
            {
                "question": "Does Ireland require quarantine for pets from the USA?",
                "answer": "Ireland does not impose mandatory quarantine for pets arriving from the USA with valid documentation. However, all pets enter as part of the EU Pet Travel Scheme and must meet all EU requirements including microchip, rabies vaccination, titre test, and endorsed health certificate. Pets that fail documentation checks may be detained at the port of entry, typically Dublin Airport."
            },
            {
                "question": "Can my pet fly directly from the USA to Ireland?",
                "answer": "Yes. Aer Lingus, American Airlines, and United Airlines operate transatlantic routes to Dublin (DUB). Direct cargo pet services are available on some routes. Many owners choose to fly via London Heathrow or Amsterdam Schiphol, both of which have established pet cargo handling facilities. Confirm pet acceptance and routing options with your airline and cargo agent."
            }
        ],
        "body": """Moving from the USA to Ireland with a pet is one of the more popular transatlantic relocations, driven by Irish heritage connections, US multinational offices in Dublin, and a generally pet-friendly culture in Ireland. The route is well-trodden and the process is manageable, but the titre test timeline means you need to start at least five months out.

## Why the titre test takes so long

Ireland is an EU member and applies EU pet travel rules. The USA is not on the EU's list of approved countries for simplified entry, so pets from the USA must have a rabies antibody titre test before travel.

The test requires a blood sample taken at least 30 days after the most recent rabies vaccination. After the sample, there is a mandatory waiting period: your pet cannot travel for at least three months after the date the blood was drawn. Total minimum timeline from microchip to travel readiness: around 180 days.

A satisfactory titre result is defined as at least 0.5 IU/ml measured at an EU-approved laboratory. In the USA, the Kansas State University Rabies Laboratory is a commonly used approved facility.

## USDA APHIS health certificate

Within 10 days of travel, your USDA-accredited veterinarian completes a health certificate (APHIS Form 7001). You then submit it to USDA APHIS for endorsement. APHIS endorses documents at its regional offices and the National Veterinary Services Laboratories. Allow three to five business days. Some APHIS offices offer a priority service for an additional fee.

The endorsed certificate must travel with your pet and be presented at Dublin Airport.

## Entering Ireland via Dublin

Dublin Airport (DUB) has a Border Inspection Post (BIP) that handles EU pet arrivals. All incoming pets from non-EU countries are inspected here. The BIP will check microchip, vaccination records, titre test result, and health certificate. With everything in order, clearance is usually quick.

If your pet travels as manifest cargo, coordinate with the airline's cargo team at DUB to ensure the BIP inspection is scheduled at the time of arrival.

## Which airlines fly pets from the USA to Ireland

Aer Lingus and American Airlines serve the Dublin route from New York, Boston, Chicago, and other US cities. United Airlines also serves Dublin. Cargo pet services are available but not universal: confirm with the specific airline and route.

Some owners route via London Heathrow (LHR) or Amsterdam Schiphol (AMS), both of which have more frequent cargo pet handling capacity.

## After arrival in Ireland

Ireland requires all dogs to be microchipped and licensed with the local authority. Dog licences are issued by councils across Ireland. There is no national pet registry equivalent, but microchip records are held through private databases.

Ireland has no domestic breed ban at the national level, though the Control of Dogs Act lists restricted breeds that require special insurance and muzzling in public.
"""
    },
    {
        "slug": "usa-to-netherlands-pet-transport-guide",
        "title": "Pet Transport USA to Netherlands 2026 | Complete Guide",
        "description": "Moving your dog or cat from the USA to the Netherlands. EU Pet Travel Scheme requirements, USDA APHIS health certificate, titre test, and arriving at Amsterdam Schiphol.",
        "date": "2026-05-08",
        "tags": ["usa to netherlands", "pet transport", "amsterdam", "usda aphis", "eu entry"],
        "faqs": [
            {
                "question": "What is the timeline for moving my pet from the USA to the Netherlands?",
                "answer": "Allow five to six months minimum. Your pet needs a microchip followed by a rabies vaccination, then a titre test taken at least 30 days after vaccination. You cannot travel for at least three months after the titre blood draw. USDA APHIS health certificate endorsement takes a further three to five business days. Start the microchip and vaccination process immediately once you know you are relocating."
            },
            {
                "question": "Does Amsterdam Schiphol accept pets as cargo?",
                "answer": "Yes. Schiphol Airport (AMS) has an NFIA (Netherlands Food and Consumer Product Safety Authority) Border Inspection Post and handles a large volume of pet cargo arrivals. Several specialist animal cargo handlers operate at AMS. Most major airlines flying the USA-Netherlands route offer cargo pet services, including KLM, Delta, and United."
            },
            {
                "question": "Can my pet travel in the cabin from the USA to the Netherlands?",
                "answer": "Cabin pet travel on transatlantic flights is not permitted by most airlines. Only service animals and some very small pets under specific policies may travel in the passenger cabin. Most dogs and cats travel as excess baggage in the pressurised hold or as manifest cargo, which is the safest and most common option for pets on long-haul international routes."
            }
        ],
        "body": """The Netherlands is a top destination for US expats, particularly those working in Amsterdam's financial district or at US multinational European headquarters. Moving your pet from the USA to the Netherlands involves the standard EU titre test pathway: it is a well-known route that any experienced pet relocation agent can manage smoothly.

## The five-to-six-month rule

The EU does not accept pet arrivals from the USA under the simplified entry rules it applies to other approved third countries. This means your pet needs a titre test.

The sequence is: microchip first, then rabies vaccination, then blood draw for titre test (at least 30 days after vaccination), then wait at least three months from the blood draw before travelling. There is no way to accelerate the three-month waiting period.

The blood sample must be sent to an EU-approved laboratory. In the USA, the Kansas State University Rabies Laboratory is the most commonly used. Allow two to four weeks for results.

## USDA APHIS endorsement

Once you have all records in order, your USDA-accredited vet completes a health certificate (APHIS Form 7001) within 10 days of travel. Submit to USDA APHIS for endorsement, which takes three to five business days. Some APHIS regional offices offer a priority service for urgent cases.

## Arriving at Amsterdam Schiphol

Schiphol (AMS) has one of Europe's best-equipped animal handling facilities. The Netherlands Food and Consumer Product Safety Authority (NVWA) operates the Border Inspection Post. Inspectors will check all documents and scan the microchip before releasing your pet.

Pets arriving as manifest cargo go through the cargo terminal handling agents. Several specialist pet cargo agents operate at Schiphol and can coordinate documentation submissions in advance, reducing clearance time.

## Registering in the Netherlands

The Netherlands has a national pet registry and all dogs must be registered with the municipality (gemeente) where you live. Dutch law requires microchipping of all dogs. Failure to register can result in fines.

There is no national breed ban in the Netherlands, though some municipalities have local regulations. Amsterdam itself has no breed ban.

## Getting your pet to the Netherlands

KLM Royal Dutch Airlines is the obvious choice for the route and accepts pets as cargo and excess baggage on many transatlantic routes. Delta Air Lines, United Airlines, and other carriers also serve AMS from major US cities. Confirm pet acceptance and booking requirements at least six weeks before your departure date.
"""
    },
    {
        "slug": "spain-to-australia-pet-transport-guide",
        "title": "Pet Transport Spain to Australia 2026 | Complete Guide",
        "description": "Moving your dog or cat from Spain to Australia. DAFF requirements, titre test, approved country pathway, quarantine in Australia, and which airlines fly the route.",
        "date": "2026-05-08",
        "tags": ["spain to australia", "pet transport", "daff", "australia quarantine", "titre test"],
        "faqs": [
            {
                "question": "What is the minimum timeline for moving a pet from Spain to Australia?",
                "answer": "Spain is an EU country and on Australia's approved country list, which means pets from Spain follow the standard 180-day pathway. The countdown starts from the date of the rabies titre test blood draw, and your pet cannot travel for at least 180 days after that date. On top of this, allow time for your Australian import permit application (four to six weeks) and pre-export documentation."
            },
            {
                "question": "Does quarantine in Australia apply to pets from Spain?",
                "answer": "Yes. All dogs and cats entering Australia must complete a minimum 10-day post-arrival quarantine at a DAFF-approved facility, regardless of origin country. For pets from approved countries including Spain, this quarantine is served at the Post Entry Quarantine (PEQ) facility in Mickleham, Victoria. Pre-booking is essential as capacity is limited."
            },
            {
                "question": "Which airlines carry pets from Spain to Australia?",
                "answer": "There are no direct flights from Spain to Australia. Most pets travel via Singapore (Singapore Airlines/SilkAir Cargo), Dubai (Emirates SkyCargo), or Doha (Qatar Airways Cargo). Some travel via London Heathrow and then connect to Australian cities. Qantas does not accept pets as cargo or excess baggage on international routes, so alternative carriers must be used."
            }
        ],
        "body": """Moving a pet from Spain to Australia is a multi-step journey that requires careful planning well in advance. Australia has some of the world's strictest biosecurity rules, and the compliance pathway from Spain is longer than from some other countries due to the rabies titre test and 180-day wait.

## Why Australia requires 180 days

Australia is rabies-free and intends to remain so. All dogs and cats from approved countries must have a valid titre test result (at least 0.5 IU/ml) taken at least 30 days after the most recent rabies vaccination. From that blood draw date, you must wait 180 days before your pet can travel to Australia.

Spain, as an EU country, is on Australia's list of approved countries, which simplifies some aspects of the process. However, the 180-day wait still applies.

## Step-by-step summary

1. Microchip your pet (ISO 15444)
2. Administer rabies vaccination after microchipping
3. Allow at least 30 days, then take blood for titre test
4. Wait 180 days from blood draw date
5. Apply for Australian import permit from DAFF (allow four to six weeks)
6. Complete pre-export health procedures within the required timeframe before departure
7. Fly via an approved transit country if required
8. Serve 10-day quarantine at PEQ Mickleham

## The import permit

You must have a DAFF import permit before your pet can enter Australia. Apply through the DAFF website. The permit specifies the species, breed, origin country, arrival method, and quarantine booking. Once issued, the permit is linked to a specific PEQ quarantine booking.

PEQ capacity is limited. As soon as you have a target travel window, contact DAFF to check availability and reserve a slot. Quarantine fees (around AUD 2,000 per animal for 10 days) are paid in advance.

## Flying from Spain to Australia

From Spain, most pets fly via Dubai (Emirates SkyCargo), Singapore (Singapore Airlines Cargo), or Doha (Qatar Airways Cargo). Emirates SkyCargo and Qatar Airways Cargo both have strong track records for pet transport on long-haul routes.

Madrid (MAD) and Barcelona (BCN) both have international cargo facilities. Book your cargo agent at least eight weeks before departure.

## On arrival in Australia

Pets arrive at the quarantine facility in Mickleham, Victoria. All species landing in Australia are inspected, treated, and monitored throughout the quarantine period. Owners can visit during business hours.

**Official sources:**
- DAFF pet import: agriculture.gov.au/pets
- PEQ Mickleham: agriculture.gov.au
"""
    },
    {
        "slug": "uk-to-south-africa-pet-transport-guide",
        "title": "Pet Transport UK to South Africa 2026 | Complete Guide",
        "description": "How to move your dog or cat from the UK to South Africa. DAFF-SA import permit, health cert, rabies vaccination, and which airlines carry pets to Johannesburg or Cape Town.",
        "date": "2026-05-08",
        "tags": ["uk to south africa", "pet transport", "south africa daff", "health certificate", "johannesburg"],
        "faqs": [
            {
                "question": "What documents do I need to take my pet from the UK to South Africa?",
                "answer": "You need: an ISO 15444 microchip; current rabies vaccination; an official health certificate completed by a UK veterinarian and endorsed by APHA within five days of travel; and a South African import permit issued by the Department of Agriculture, Land Reform and Rural Development (DALRRD). Some veterinarians refer to the South African authority as DAFF-SA, though the department was renamed after a 2019 restructuring."
            },
            {
                "question": "Is there quarantine for pets arriving in South Africa from the UK?",
                "answer": "South Africa does not impose mandatory quarantine for dogs and cats from approved countries including the UK, provided all documentation is in order. Animals are inspected by DALRRD veterinary officers at the port of entry. If documentation is incomplete or the animal appears unwell, temporary detention may apply."
            },
            {
                "question": "Which airlines carry pets from the UK to South Africa?",
                "answer": "British Airways, Virgin Atlantic, and South African Airways operate the UK to South Africa route. British Airways accepts pets in the hold as excess baggage on some routes. South African Airways accepts pets as cargo. Several specialist pet cargo agents also offer direct freight services from Heathrow to Johannesburg O.R. Tambo (JNB) or Cape Town (CPT)."
            }
        ],
        "body": """South Africa is one of the most sought-after destinations for UK relocations, with year-round sunshine, a large English-speaking community, and a generally welcoming attitude toward pets. The import process is manageable, and with the right preparation it should not cause significant delays.

## What South Africa requires

The Department of Agriculture, Land Reform and Rural Development (DALRRD, previously known as DAFF-SA) regulates pet imports. The core requirements for dogs and cats entering South Africa from the UK are:

- ISO 15444 microchip implanted before any rabies vaccination
- Current rabies vaccination (primary and booster as appropriate)
- Official health certificate completed by a UK government-listed veterinarian, endorsed by APHA, issued within five days of travel
- Import permit issued by DALRRD in advance

## The health certificate and APHA endorsement

Unlike some countries, South Africa requires the health certificate to be endorsed within five days of travel rather than the more common 10-day window. Book your vet appointment to align with this timeline. Allow two to three working days for APHA endorsement on top of the vet appointment.

APHA endorsement fees are standard. Book your APHA slot at the same time as your vet appointment. Both can be done online.

## Applying for the import permit

Apply to DALRRD for an import permit at least four weeks before travel. The permit specifies the species, breed, origin country, and entry point. Without a confirmed permit, your pet may be refused entry.

Applications can be submitted to DALRRD's Plant and Animal Health Inspection Services (PAHIS) division.

## Airlines and cargo options

British Airways accepts dogs and cats as excess baggage in the hold on its Heathrow to Johannesburg and Cape Town routes, subject to crate size limits and temperature embargoes. South African Airways accepts pets as cargo. Virgin Atlantic does not currently accept live animals.

Specialist pet cargo agents at Heathrow (LHR) can manage the full cargo chain, including document submission to DALRRD's inspection facility at O.R. Tambo (JNB) or Cape Town (CPT).

## Arriving in South Africa

At arrival, DALRRD veterinary officers will inspect your pet and check all documents. With a valid permit, health certificate, microchip, and vaccination records, inspection is usually straightforward. Released pets can travel home with their owners or with a ground transfer arranged by your cargo agent.

## Life in South Africa with a pet

South Africa has no national breed ban, but certain breeds face restrictions in residential complexes and gated communities, particularly Pit Bull types. Always check your residential rules before arrival.

Veterinary care is generally excellent in major cities, with specialist practices in Johannesburg, Cape Town, and Durban.
"""
    },
    {
        "slug": "japan-to-usa-pet-transport-guide",
        "title": "Pet Transport Japan to USA 2026 | Complete Guide",
        "description": "Moving your dog or cat from Japan to the USA. CDC rules for dogs, USDA APHIS requirements, and what to expect when arriving at a US airport with a pet from a rabies-free country.",
        "date": "2026-05-08",
        "tags": ["japan to usa", "pet transport", "cdc dog import", "rabies free", "usda aphis"],
        "faqs": [
            {
                "question": "Does my dog need a rabies vaccination to enter the USA from Japan?",
                "answer": "Japan is classified by the CDC as a dog-screwworm-free and rabies-free country. Dogs from Japan can enter the USA under the simplified pathway for dogs from rabies-free countries, provided they were not vaccinated with a US-produced USDA-licensed rabies vaccine. The dog must have a microchip and arrive at a CDC-registered facility. Always verify CDC requirements at the time of travel, as the rules have been updated in recent years."
            },
            {
                "question": "What documents do I need for my cat travelling from Japan to the USA?",
                "answer": "Cats have fewer import restrictions than dogs when entering the USA. There is no federal rabies vaccination requirement for cats, though some US states require vaccination for cats. A health certificate from a licensed veterinarian is good practice. Airlines typically require a health certificate issued within 10 days of travel."
            },
            {
                "question": "Can my dog fly in the cabin from Japan to the USA?",
                "answer": "Very few airlines allow pets in the cabin on long-haul transpacific flights. Most dogs travel as excess baggage in the pressurised hold or as manifest cargo. Japan Airlines (JAL), All Nippon Airways (ANA), and United Airlines all accept pets on some transpacific routes. Confirm the specific route, aircraft type, and pet policy before booking."
            }
        ],
        "body": """Japan to USA is one of the more straightforward international pet routes for dog owners, largely because Japan is a CDC-classified rabies-free country, which simplifies the process compared to moving from Europe or Australia. That said, the USA introduced new CDC dog import rules in 2023 that all pet owners should verify before travel.

## CDC dog import requirements

Since August 2024, all dogs entering the USA must be microchipped (ISO 15444 or 11784/11785). Dogs from Japan, a country on the CDC's rabies-free list, are eligible for the simplified entry pathway. This means the mandatory pre-travel rabies vaccination requirement may not apply, subject to the specific circumstances of the dog.

However, if your dog was vaccinated against rabies in the USA or with a US-produced USDA-licensed vaccine, additional rules apply. Check the CDC's current dog import requirements at cdc.gov/importation at the time you are planning your move, as the rules have been subject to ongoing revision.

All dogs entering the USA must arrive at a CDC-registered airport with a registered animal facility. These include major international airports such as Los Angeles (LAX), New York JFK, Chicago O'Hare (ORD), and several others.

## Cats from Japan to the USA

There is no federal vaccination requirement for cats entering the USA. A health certificate from a Japanese licensed veterinarian, issued within 10 days of travel, is good practice and is required by most airlines. Check individual state requirements, as some states have their own vaccination rules for cats.

## Health certificate for dogs

Even for simplified entry, airlines require a health certificate. The certificate is typically issued by a Japanese registered veterinarian within 10 days of the flight. Japanese veterinary authorities may issue an official endorsement, which is helpful if your airline or the airline cargo handler requests it.

## Airlines for Japan-USA pet transport

JAL, ANA, United, Delta, and American Airlines all serve the transpacific route. JAL and ANA have specific domestic Japan pet policies that differ from their international cargo policies. On transpacific routes, pets generally travel as manifest cargo.

Direct routes operate from Tokyo Narita (NRT) and Tokyo Haneda (HND) to Los Angeles, San Francisco, New York, and other US cities. Non-stop routes minimise handling and are always preferable for pets.

## Arriving in the USA from Japan

On arrival, customs and border protection will check your documentation. Dogs are typically inspected at the CDC-registered facility at the arrival airport. With the simplified Japan pathway, inspection is usually quick provided the microchip matches and all records are in order.

**Official sources:**
- CDC dog import rules: cdc.gov/importation
- USDA APHIS: aphis.usda.gov/pet-travel
- Japan Animal Quarantine Service: maff.go.jp/aqs
"""
    },
    # ------------------------------------------------------------------ #
    # BREED GUIDES                                                         #
    # ------------------------------------------------------------------ #
    {
        "slug": "travelling-with-a-bernese-mountain-dog-internationally",
        "title": "Travelling with a Bernese Mountain Dog Internationally",
        "description": "What you need to know about flying internationally with a Bernese Mountain Dog. Crate sizes, airline restrictions, cargo-only rules, and keeping large breeds comfortable in transit.",
        "date": "2026-05-08",
        "tags": ["bernese mountain dog", "large breed travel", "pet cargo", "international travel"],
        "faqs": [
            {
                "question": "Can a Bernese Mountain Dog travel in the cabin?",
                "answer": "No. Bernese Mountain Dogs are large dogs and cannot travel in the passenger cabin. They must travel in the hold as checked baggage or as manifest cargo. The breed is not brachycephalic and does not face the specific respiratory restrictions that apply to flat-faced breeds, but their size means cargo travel is the only option on commercial flights."
            },
            {
                "question": "What size crate does a Bernese Mountain Dog need?",
                "answer": "Adult Berners typically need an IATA-compliant crate in the 500 to 700 range (roughly 91 cm x 61 cm x 71 cm or larger depending on the individual dog). Your dog must be able to stand, turn around, and lie down comfortably with at least 5 cm headroom. Measure your dog before purchasing a crate and verify the dimensions against the specific airline's cargo size limits."
            },
            {
                "question": "Are there any country bans on Bernese Mountain Dogs?",
                "answer": "No. Bernese Mountain Dogs are not on any country's restricted or banned breed list. They are working dogs with a calm temperament and no history of being classified as dangerous. Standard vaccination, microchip, and health certificate requirements apply based on the destination country."
            }
        ],
        "body": """Bernese Mountain Dogs are large, gentle, and generally calm travellers, which is a good starting point. The main practical challenges are their size (most adults weigh 30 to 50 kg) and the logistics of finding appropriate crates and cargo space.

## Cargo travel is the only option

No commercial airline will allow a Bernese Mountain Dog to travel in the passenger cabin. Even small adults exceed the weight limits for cabin pets, which are typically capped at 8 to 10 kg including carrier.

Your Berner will travel in the pressurised, temperature-controlled hold as either excess baggage (booked with the passenger) or as manifest cargo. Both options are safe for healthy, fit dogs in an IATA-compliant crate, but the logistics differ and you should confirm your preferred option with the airline well in advance.

## Choosing the right crate

IATA crate sizing standards are based on the dog's measurements, not the breed. Measure your Berner before buying a crate:
- Height: from the ground to the top of their head when standing
- Length: from the tip of their nose to the base of their tail
- Width: across the shoulders at the widest point

Add the required IATA clearance (typically 5 cm in all directions for smaller crates, up to 10 cm for very large crates). Most adult Berners need a 500 or 700 series crate.

Hard-sided, rigid, ventilated crates are required for air travel. Wire crates are not acceptable for cargo.

## Training your Berner for crate travel

Berners are intelligent and respond well to crate training. Start at least two to three months before travel. Begin with short periods in the crate with the door open, building up to overnight stays with the door closed. A dog that is relaxed in its crate will experience less stress during the flight.

Place a familiar item, such as an unwashed t-shirt or a favourite toy, inside the crate to provide scent comfort.

## Health and fitness for travel

Berners are prone to certain health conditions including hip and elbow dysplasia and bloat (gastric dilatation-volvulus). Consult your vet before international travel to ensure your dog is fit to fly. Avoid feeding a large meal within four to six hours of travel to reduce the risk of bloat during transit.

## Destination country rules

Bernese Mountain Dogs face no breed-specific restrictions in any country. Standard country import requirements apply: microchip, vaccinations, health certificate, and (if required) titre test and import permit. Check the destination country guide for specific requirements.
"""
    },
    {
        "slug": "travelling-with-a-bengal-cat-internationally",
        "title": "Travelling with a Bengal Cat Internationally",
        "description": "Bengal cats and international travel. CITES considerations for early generations, airline policies, microchip requirements, and how to keep an active breed calm in transit.",
        "date": "2026-05-08",
        "tags": ["bengal cat", "cites", "international travel", "cat in cargo", "exotic breeds"],
        "faqs": [
            {
                "question": "Do Bengal cats need a CITES permit for international travel?",
                "answer": "It depends on the generation. Early generation Bengals (F1 and F2, meaning first or second cross with an Asian Leopard Cat) may be subject to CITES Appendix II restrictions in some countries, as the Asian Leopard Cat is a protected species. Bengals of F5 generation and beyond, which are considered fully domestic cats, are generally not subject to CITES restrictions. Check the generation of your cat's documented pedigree and consult a specialist."
            },
            {
                "question": "Can Bengal cats travel in the cabin?",
                "answer": "Most Bengal cats, like other domestic cats, can travel in the cabin on shorter flights if they are small enough to fit in an approved carrier under the seat (typically total weight of cat plus carrier under 6 to 10 kg, depending on airline). On long-haul international flights, most airlines do not permit cats in the cabin. Always verify with your specific airline."
            },
            {
                "question": "Are Bengal cats banned from any countries?",
                "answer": "Early generation Bengals (F1 and F2) may face restrictions or outright bans in some countries due to their wild cat heritage. Australia, for example, has banned the import of all Bengal cats. Hawaii (within the USA) also bans Bengal cats. For standard domestic Bengal cats of F5 generation or later, normal destination country import rules apply."
            }
        ],
        "body": """Bengal cats are striking, energetic, and intelligent. They are also, in their early generations, derived from wild Asian Leopard Cats, which creates specific considerations for international travel that owners of other domestic breeds do not need to worry about.

## Understanding Bengal cat generations

Bengals are categorised by generation:
- F1: offspring of a domestic cat x Asian Leopard Cat pairing
- F2: offspring of an F1 Bengal x domestic cat
- F3: offspring of an F2 x domestic cat
- F4 and beyond: considered domestic cats in most regulatory frameworks

F1 and F2 Bengals are often considered wild hybrids and may require CITES export permits (Asian Leopard Cats are listed under CITES Appendix II). In some countries, F3 Bengals are also subject to these restrictions. If you have a pedigree certificate from the TICA or GCCF, check the generation documentation carefully.

F5 and beyond (sometimes labelled SBT, Stud Book Tradition) are treated as fully domestic cats under most regulations.

## CITES considerations

If your Bengal is of a generation requiring CITES documentation, you will need:
- A CITES export permit from the exporting country authority
- A CITES import permit from the destination country authority (if required)
- Some countries will not issue import permits for any generation of Bengal

Contact the wildlife trade authority in both your origin and destination countries to confirm what is required for your specific cat.

## Countries with Bengal restrictions

Australia bans the import of all Bengal cats, regardless of generation. This is a blanket policy with no exceptions. Hawaii (a US state) also bans all Bengals. Some other countries may have local restrictions: always check with the destination country's veterinary authority.

For international Bengals (F5+), standard destination country import requirements apply: microchip, vaccinations, health certificate, titre test if required, import permit if required.

## Keeping a Bengal calm during travel

Bengals are active and curious cats and can become stressed in confined spaces. Work on crate habituation well before travel. Many Bengal owners find that a well-worn item of clothing in the carrier helps. Some vets may recommend a short course of anxiety-reducing medication for particularly stressed cats, though sedation is not recommended for air travel.

## Airline policies for cats

Most airlines accept domestic cats in the cabin on short routes or in cargo for long hauls. A standard IATA-compliant soft carrier is acceptable for cabin travel (verify dimensions with your airline). For cargo, a rigid ventilated hard carrier is required.
"""
    },
    {
        "slug": "travelling-with-a-norwegian-forest-cat-internationally",
        "title": "Travelling with a Norwegian Forest Cat Internationally",
        "description": "Norwegian Forest Cats and international travel. Crate requirements, airline policies for large cats, health certificate needs, and how to prepare a Wegie for long-haul transit.",
        "date": "2026-05-08",
        "tags": ["norwegian forest cat", "large cat travel", "international travel", "cat cargo"],
        "faqs": [
            {
                "question": "Can Norwegian Forest Cats travel in the cabin?",
                "answer": "Norwegian Forest Cats are a large breed, with adults weighing 4 to 9 kg. Whether your specific cat can travel in the cabin depends on the airline's weight limit (usually 6 to 10 kg including carrier) and on the carrier dimensions fitting under the seat. Large Wegies, particularly males, may need to travel as excess baggage or cargo. Verify your cat's weight and your chosen airline's cabin pet policy before booking."
            },
            {
                "question": "Are Norwegian Forest Cats brachycephalic?",
                "answer": "No. Norwegian Forest Cats are not brachycephalic (flat-faced). They have a normal cat facial structure and do not face the breed-specific airline restrictions that apply to Persian, Exotic Shorthair, and Scottish Fold cats. This makes them safer candidates for air travel from a respiratory risk perspective."
            },
            {
                "question": "Are there any country bans on Norwegian Forest Cats?",
                "answer": "No. Norwegian Forest Cats are not on any country's restricted or banned breed list. They are a recognised pedigree domestic breed with no wild heritage concerns. Standard destination country import requirements apply."
            }
        ],
        "body": """Norwegian Forest Cats (Wegies) are well-suited to travel in terms of temperament: they are calm, adaptable, and generally less anxious than some other breeds. The main practical consideration is their size, as adult Wegies can be quite large.

## Size and weight considerations

Male Norwegian Forest Cats typically weigh 6 to 9 kg as adults, and some individuals exceed this. When combined with an IATA-compliant carrier, the total weight may exceed the cabin weight limit set by many airlines (typically 6 to 10 kg total).

Before booking, weigh your cat and add the weight of your carrier. If the total exceeds the airline's cabin limit, you will need to book hold/cargo travel. For most long-haul international routes, cabin pets are not accepted regardless of weight, so this is mainly relevant for shorter European or domestic flights.

## Health and fitness for travel

Norwegian Forest Cats are generally a healthy breed, though they can be prone to hypertrophic cardiomyopathy (HCM) and glycogen storage disease (GSD). Before long-haul travel, have your vet confirm your cat is fit to fly. A cardiac check is worth doing for any cat travelling long-haul, particularly for adults over five years.

## Crate requirements for cargo

If your Wegie travels in the hold, an IATA-compliant rigid hard-sided crate is required. The crate must be large enough for your cat to stand, turn around, and lie down comfortably. Most adults fit in a crate of around 60 x 40 x 40 cm, but measure your individual cat.

## Preparing for travel

Introduce the crate at least two months before travel. Leave it open in the house with bedding inside so your cat can explore it voluntarily. Gradually build up time spent with the door closed. A Wegie accustomed to its crate will be significantly less stressed in transit.

On the day of travel, do not give a large meal within four hours of departure. Water should be available in the crate if travelling cargo.

## Destination requirements

Norwegian Forest Cats follow standard destination country import rules. Check the relevant country guide for microchip, vaccination, titre test, health certificate, and import permit requirements for your specific destination.
"""
    },
    {
        "slug": "travelling-with-a-jack-russell-terrier-internationally",
        "title": "Travelling with a Jack Russell Terrier Internationally",
        "description": "International travel with a Jack Russell Terrier. Cabin vs cargo, crate training tips for an energetic breed, country restrictions, and health certificate requirements.",
        "date": "2026-05-08",
        "tags": ["jack russell terrier", "small dog travel", "international travel", "cabin travel"],
        "faqs": [
            {
                "question": "Can a Jack Russell Terrier travel in the cabin?",
                "answer": "Yes, on many routes. Jack Russells are small dogs, typically weighing 5 to 8 kg. Combined with a carrier, they may just meet most airlines' cabin pet weight limits of 6 to 10 kg. It depends on the individual dog and airline. For long-haul international flights, most airlines do not permit pets in the cabin regardless of size, so cargo travel is the standard option for intercontinental moves."
            },
            {
                "question": "Are Jack Russell Terriers brachycephalic?",
                "answer": "No. Jack Russells are not brachycephalic. They have a standard terrier muzzle length and do not face breed-specific restrictions applied to flat-faced breeds. They are generally good candidates for air travel from a respiratory risk perspective, though their energetic temperament means crate habituation is especially important."
            },
            {
                "question": "Are there any country bans on Jack Russell Terriers?",
                "answer": "No. Jack Russells are not on any country's restricted or dangerous breed list. They are a well-established breed with no specific import restrictions beyond standard country requirements. Standard microchip, vaccination, and health certificate rules apply at the destination."
            }
        ],
        "body": """Jack Russell Terriers are small, bold, and often surprisingly unfazed by new environments. That said, their energy and instinct to investigate can make them more reactive to the unusual sights, sounds, and smells of air travel, so preparation matters.

## Cabin vs cargo

Jack Russells are small enough to qualify for cabin travel on many airline routes, subject to total carrier weight limits. For European and short-haul routes, a Jack Russell in an approved soft carrier under the seat is a practical option.

For long-haul international travel, most airlines do not permit pets in the cabin at all. Your Jack Russell will travel in the pressurised, temperature-controlled hold as excess baggage or manifest cargo. This is safe for healthy dogs in IATA-compliant crates, and many Jack Russells manage the journey well.

## Crate training

Jack Russells can be strong-willed and may resist confinement if not properly trained. Start crate training at least two months before travel. Use positive reinforcement exclusively: feed meals in the crate, reward calm behaviour with treats, and avoid using the crate as punishment.

Build up from short sessions with the door open to longer periods with the door closed. Once your Jack Russell sleeps voluntarily in the crate, you can be reasonably confident they will cope in transit.

## Health considerations

Jack Russells are a robust and generally healthy breed. There are no breed-specific health conditions that significantly increase travel risk. Consult your vet before any long-haul journey, particularly if your dog is over seven years old or has any chronic health issues.

Do not feed a large meal within four to six hours of the flight. Water should be available in the crate via an attached bowl.

## Destination requirements

Jack Russells follow standard import rules at the destination country. Check the relevant country guide for microchip, vaccination, titre test, health certificate, and import permit requirements. No breed-specific restrictions apply.
"""
    },
    {
        "slug": "travelling-with-an-akita-internationally",
        "title": "Travelling with an Akita Internationally",
        "description": "Moving internationally with an Akita. Country bans, crate sizing, cargo-only travel, health certificate needs, and what to check before booking your Akita on an international flight.",
        "date": "2026-05-08",
        "tags": ["akita", "restricted breed", "international travel", "large dog cargo", "breed ban"],
        "faqs": [
            {
                "question": "Is the Akita a restricted breed in any countries?",
                "answer": "Yes. The Akita is subject to breed-specific legislation in several countries. In the UK, the Akita is not on the prohibited list, but it is considered a 'type of dog' in some local authority regulations. In some European countries and in parts of Australia, the Akita faces registration, muzzling, and lead requirements. In some US cities and states, Akitas are on local restricted breed lists. Always verify the rules in your specific destination before travel."
            },
            {
                "question": "Can an Akita travel in the cabin?",
                "answer": "No. Akitas are large dogs, with adults typically weighing 25 to 45 kg or more, and they must travel in the hold as excess baggage or manifest cargo. There is no option for cabin travel for a breed of this size. Large and powerful dog breeds may also face additional scrutiny from airlines: some carriers restrict large and powerful breeds as cargo, so confirm acceptance before booking."
            },
            {
                "question": "What crate size does an Akita need for air travel?",
                "answer": "Most adult Akitas need a 500 or 700 series IATA-compliant crate. The exact size depends on your individual dog's measurements. Your dog must be able to stand at full height, turn a full circle, and lie down stretched out in the crate, with a minimum 5 to 10 cm clearance in all directions. Many Akitas need a 700 series or custom-sized crate."
            }
        ],
        "body": """Akitas are loyal, powerful, and dignified dogs with a rich history in Japan. They are also large, strong-willed, and subject to breed-specific legislation in a number of countries, which means international travel with an Akita requires careful research well before booking.

## Breed-specific restrictions

The Akita is not banned at the national level in most major destination countries, but it does appear on local restricted breed lists in some jurisdictions. In Australia, some states have specific requirements for Akitas, and in the USA, several cities and counties include Akitas in their restricted breed ordinances.

Before booking any international pet transport for an Akita, check:
1. Does the destination country have a national breed ban or registration requirement?
2. Does your specific destination city or region have local breed restrictions?
3. Does your airline accept Akitas as cargo?

Some airlines have their own restricted breed lists that go beyond country regulations.

## Airline acceptance

Akitas are not brachycephalic, but their size and strength mean some carriers require additional confirmation before accepting them. Japanese carriers (JAL, ANA) are generally accustomed to the breed given its Japanese heritage. Contact your chosen airline's cargo team directly to confirm acceptance.

## Crate sizing for an Akita

Most adult Akitas need a large IATA crate, typically 700 series (approximately 106 x 71 x 76 cm), though your dog's specific measurements should drive the final selection. Measure your dog as follows:

- Height: floor to top of head/ears when standing
- Length: tip of nose to base of tail
- Width: widest point across shoulders

Add 10 cm to each measurement for correct IATA clearance for large breeds.

## Preparing your Akita for travel

Akitas can be independent and stubborn, which makes early crate training essential. Start two to three months before travel. Akitas respond well to patient, consistent training with rewards. Avoid punishing the dog for crate resistance, which can create negative associations.

Ensure your Akita's vaccination records are fully current, particularly for rabies, and consult your vet about fitness for long-haul travel.

## Japan-specific notes

If you are bringing an Akita from or to Japan (the breed's country of origin), note that Japan has detailed import requirements including quarantine. See the Japan pet import guide for full details.
"""
    },
    {
        "slug": "travelling-with-a-samoyed-internationally",
        "title": "Travelling with a Samoyed Internationally",
        "description": "International travel with a Samoyed. Heat sensitivity concerns, cargo-only travel, crate sizing, and destination country requirements for this Nordic breed.",
        "date": "2026-05-08",
        "tags": ["samoyed", "nordic breed", "international travel", "large dog cargo", "heat sensitivity"],
        "faqs": [
            {
                "question": "Can a Samoyed travel in the cabin on international flights?",
                "answer": "No. Samoyeds are large dogs, typically weighing 20 to 30 kg as adults, and must travel as cargo or excess baggage in the hold. There is no option for cabin travel at this size. Samoyeds are not brachycephalic and do not face the specific respiratory restrictions of flat-faced breeds, but their size requires cargo travel."
            },
            {
                "question": "Are Samoyeds at risk in warm weather during air travel?",
                "answer": "Yes. Samoyeds are a Nordic breed with a thick double coat adapted for cold climates. They can overheat more quickly than short-coated breeds in warm conditions. Most airlines apply live animal temperature embargoes when ground temperatures at departure or arrival airports exceed 29 to 32 degrees Celsius. In summer months, book early morning or late evening flights to reduce exposure to high ground temperatures during loading and unloading."
            },
            {
                "question": "Are there any country bans on Samoyeds?",
                "answer": "No. Samoyeds are not on any country's restricted or dangerous breed list. They are a recognised pedigree breed with no specific import restrictions beyond standard country requirements. Standard microchip, vaccination, and health certificate rules apply at the destination."
            }
        ],
        "body": """Samoyeds are among the most striking dogs in any airport, and they generally attract a lot of attention during travel. Their thick white coats, which are such a distinctive feature of the breed, are also the main practical challenge for international travel: heat management is essential.

## The heat sensitivity issue

Samoyeds were bred in Siberia to work in extreme cold. Their double coat provides insulation in both directions (cold and heat), but it makes them more vulnerable to overheating in warm conditions than many other breeds.

Most airlines apply temperature embargoes that prevent live animal loading when ground temperatures exceed a threshold, typically 29 degrees Celsius (85 degrees Fahrenheit) or 32 degrees Celsius depending on the carrier. These embargoes protect all animals, including Samoyeds.

When planning travel with a Samoyed:
- Avoid summer midday or afternoon flights where possible
- Choose routes with the shortest possible ground time in warm climates
- Confirm the airline's temperature embargo policy for your specific route and travel dates

## Cargo travel logistics

Adult Samoyeds need a large IATA-compliant rigid crate, typically 500 to 700 series depending on your individual dog. Measure your dog carefully (height, length, width) and add the required IATA clearance before selecting a crate.

Ensure water is available in the crate via an attached, secured bowl. On longer flights, ask your cargo agent whether water top-ups are available during any transit or stop.

## Crate training

Samoyeds are sociable and may find confinement stressful if not properly prepared. Start crate training early, ideally two to three months before travel. Make the crate a positive space: feed meals in it, leave favourite toys inside, and build up to overnight stays with the door closed.

A calm, crate-habituated Samoyed will cope much better with the long-haul journey than one that has not been prepared.

## Grooming before travel

Some owners choose to have their Samoyed professionally groomed before travel to reduce shedding in the crate. Avoid shaving the coat: the double coat provides both heat and cold protection and should not be removed.

## Destination country requirements

Samoyeds follow standard destination country import rules. No breed-specific restrictions apply anywhere. Check the relevant country guide for microchip, vaccination, titre test, health certificate, and import permit requirements for your specific destination.
"""
    },
    # ------------------------------------------------------------------ #
    # PRACTICAL GUIDES                                                     #
    # ------------------------------------------------------------------ #
    {
        "slug": "travelling-with-fish-internationally",
        "title": "Travelling with Fish Internationally | Import Rules and Tips",
        "description": "How to transport fish across international borders. CITES permits for tropical species, disease certifications, and practical advice for moving aquarium fish by air.",
        "date": "2026-05-08",
        "tags": ["fish travel", "cites", "aquarium fish", "import permit", "ornamental fish"],
        "faqs": [
            {
                "question": "Do I need a CITES permit to travel internationally with tropical fish?",
                "answer": "It depends on the species. Many common aquarium fish are not CITES-listed and do not require a permit. However, some species (such as certain freshwater stingrays, arapaima, and others) are listed under CITES Appendix I or II and require export and import permits. Check your species against the CITES database at cites.org before any international movement."
            },
            {
                "question": "Can you fly internationally with pet fish?",
                "answer": "Fish can be transported by air as cargo or unaccompanied freight in properly oxygenated, sealed water bags or containers. Most commercial passenger airlines do not accept fish as carry-on or checked baggage. Specialist fish shipping services can manage the oxygen, temperature, and documentation requirements. Fish cannot be simply packed in a suitcase."
            },
            {
                "question": "Which countries have strict import rules for fish?",
                "answer": "Australia has very strict biosecurity rules for ornamental fish: only species on the approved import list can be brought in, and they must come from approved source countries via licensed importers. The USA requires an import declaration and disease health certificate for live fish. The EU requires health certificates for fish from outside the EU. Always check destination country rules before attempting to import fish."
            }
        ],
        "body": """Moving aquarium fish internationally is significantly more complex than moving dogs or cats. The rules vary widely by species, country, and transport method, and mistakes can result in fish being confiscated or euthanised at the border.

## Is your species permitted?

The first question is always: is the species you want to transport permitted in the destination country? Check:
1. CITES status: is the species on the CITES Appendix I (trade banned) or Appendix II (trade regulated) list?
2. Destination country approved species list: countries like Australia have a positive list of approved species, and anything not on the list cannot be imported, regardless of CITES status
3. Origin country export rules: some countries restrict or ban the export of certain species regardless of destination

## Disease certification

For most countries, ornamental fish imports require a health certificate from a government-authorised aquatic animal veterinarian, confirming the fish are free from specific notifiable diseases. In the EU this is governed by Regulation (EU) 2016/429 on transmissible animal diseases.

Common diseases of concern for imported fish include koi herpesvirus (KHV) in koi and goldfish, and viral haemorrhagic septicaemia (VHS) in various species.

## Transport conditions

Fish for air transport are typically packed in sealed oxygen-enriched bags inside polystyrene-lined cardboard boxes. Professional fish shippers use:
- Water conditioned to reduce stress (temperature stabilised, stress coat added)
- Oxygen injection before sealing bags
- Double-bag method to prevent leaks
- Adequate space per fish to prevent overcrowding and waste build-up

The transport time (door to door) is critical. Most tropical fish can tolerate 24 to 48 hours in transit bags if properly prepared. Delicate or rare species may require shorter transit times.

## Australia: the strictest destination

Australia only permits the import of ornamental fish from approved species lists and approved source countries. Applications go to the Department of Agriculture, Fisheries and Forestry (DAFF). Fish that arrive without approval are destroyed. Australia does not have provisions for bringing in unapproved species even for personal collections.

If you are relocating to Australia with an aquarium, it is typically impractical to bring your fish. Most owners donate or sell their collections before departure and start fresh in Australia with locally sourced approved species.

## Practical advice

Work with a specialist ornamental fish shipper who has experience with international cargo documentation. This is not a task to attempt without professional help, particularly for rare or CITES-listed species.
"""
    },
    {
        "slug": "travelling-with-reptiles-internationally",
        "title": "Travelling with Reptiles Internationally | Permits and Rules",
        "description": "How to transport reptiles across international borders. CITES Appendix I and II rules, import permits, health certificates, and practical advice for moving snakes, lizards, and tortoises.",
        "date": "2026-05-08",
        "tags": ["reptile travel", "cites", "snake travel", "tortoise import", "lizard travel"],
        "faqs": [
            {
                "question": "Do reptiles need a CITES permit for international travel?",
                "answer": "Many reptiles do. A large proportion of reptile species in the pet trade are listed under CITES Appendix I or II. This includes all tortoises and turtles of the Testudo genus, many chameleons, boa constrictors, ball pythons (Python regius, Appendix II), and many monitors and geckos. Check every species you plan to move against the CITES database before planning travel."
            },
            {
                "question": "Can I travel on a passenger flight with a reptile?",
                "answer": "Most airlines do not accept reptiles as carry-on or checked baggage. Snakes and lizards in particular are typically refused. Some airlines accept small, enclosed reptiles (such as tortoises in a secure container) as cargo or excess baggage, but this must be confirmed with the airline individually. Specialist reptile couriers are often the safest option for international reptile transport."
            },
            {
                "question": "Which countries ban the import of reptiles?",
                "answer": "Australia bans the import of all exotic reptiles, with very limited exceptions for zoos and research institutions. New Zealand also has strict restrictions. The USA bans the import of certain species under the Lacey Act and has specific rules for venomous species. The EU restricts CITES-listed species to licensed importers. Most countries require import permits for reptiles."
            }
        ],
        "body": """Reptiles are among the most regulated animals in international trade, and for good reason: the illegal wildlife trade in reptiles is a significant conservation concern, and invasive reptile species can cause ecological damage when introduced to new regions.

## CITES and reptiles

The Convention on International Trade in Endangered Species (CITES) regulates international movement of over 38,000 species, and reptiles are heavily represented. Before moving any reptile internationally:

1. Identify the species by its scientific name (common names can be shared by multiple species with different CITES statuses)
2. Check cites.org for the species' listing
3. Confirm whether export and import permits are required for both countries involved

**Appendix I species:** International commercial trade is prohibited. Movement is only permitted for non-commercial purposes with specific documentation, and even then, it is difficult to arrange.

**Appendix II species:** Commercial trade is permitted but regulated. You need an export permit from the exporting country and, in most cases, an import permit from the destination country.

## Country of origin certification

For captive-bred reptiles, a certificate of captive breeding can simplify the CITES permit process. This certificate must be issued by the relevant authority in the country of origin and confirms the animal was not taken from the wild. Many popular pet reptiles (such as ball pythons and bearded dragons) are now almost exclusively captive-bred, which helps.

## Airline restrictions

Most major airlines refuse to carry reptiles, particularly snakes. Some airlines will accept small, fully enclosed reptiles (tortoises, small lizards) as cargo freight, but this is not universal. Specialist reptile couriers who work with approved freight forwarders are the safest route for most international reptile movements.

## Destination restrictions

Australia has some of the world's strictest biosecurity rules for reptiles. All exotic reptiles (non-native to Australia) are banned from import, period. This includes common pets like bearded dragons and leopard geckos, which are ironically native to Australia: Australian reptiles cannot be exported from Australia, and non-native reptiles cannot be imported.

New Zealand also bans exotic reptiles. If you are relocating to either country with reptiles, the realistic advice is to rehome them before departure.

## Practical advice for moving reptiles

Work with an organisation that specialises in CITES compliance and animal cargo for reptiles. The documentation chain (export CITES permit, import CITES permit, health certificate, airline cargo manifest) is complex and errors are costly. Contact the wildlife trade authority in both countries at least three months before your intended travel date.
"""
    },
    {
        "slug": "moving-to-new-zealand-with-a-pet",
        "title": "Moving to New Zealand with a Pet | Practical Guide 2026",
        "description": "Everything you need to know about moving to New Zealand with a dog or cat. Approved countries, the 10-day quarantine process at Levin, costs, and how to plan the journey.",
        "date": "2026-05-08",
        "tags": ["new zealand", "pet relocation", "nz quarantine", "moving to nz", "dog import nz"],
        "faqs": [
            {
                "question": "Is there quarantine for pets arriving in New Zealand?",
                "answer": "Yes. All dogs and cats entering New Zealand must complete a minimum 10-day quarantine at the government-managed facility in Levin, north of Wellington. The 10-day period begins on arrival. Pre-booking is essential as the facility has limited capacity. Quarantine costs approximately NZD 1,500 to 2,500 per animal depending on species and the quarantine period required."
            },
            {
                "question": "Which countries does New Zealand accept pets from?",
                "answer": "New Zealand maintains a list of approved countries from which dogs and cats can be imported. Category 1 countries (such as Australia, the UK, Ireland, Hawaii, and a small number of others) face the simplest requirements. Category 2 countries face additional requirements. Pets from non-approved countries generally cannot be imported, with very limited exceptions."
            },
            {
                "question": "How far in advance do I need to plan my pet's move to New Zealand?",
                "answer": "For most countries, allow at least five to six months. The timeline is dominated by the rabies titre test requirement: the blood sample must be taken at least 30 days after vaccination, and you cannot travel for at least 180 days after the blood draw. Add time for the import permit application (six to eight weeks) and quarantine facility booking."
            }
        ],
        "body": """New Zealand is one of the world's most beautiful places to live, and the good news is that thousands of pet owners successfully make the move every year. The bad news is that New Zealand's biosecurity system is strict, and the process requires time and careful planning.

## New Zealand's approved country system

MPI (Ministry for Primary Industries) manages all animal imports into New Zealand. Countries are classified by risk level, which determines how many requirements apply.

Category 1 countries include Australia, the UK, Ireland, Hawaii (USA), Niue, and a handful of others. If you are coming from one of these, the process is more straightforward, though quarantine is still mandatory.

For most other countries (including the USA, Canada, Singapore, and continental European countries), the process is more intensive and involves a titre test and a longer compliance pathway.

## The titre test and 180-day wait

For pets from most countries, a rabies antibody titre test is required. Your vet takes a blood sample at least 30 days after the most recent rabies vaccination. The result must be at least 0.5 IU/ml, and your pet cannot travel for at least 180 days from the date the blood was drawn.

There is no way to shorten this waiting period. Start the process immediately if you know you are relocating to New Zealand.

## Import permit from MPI

Before your pet can travel to New Zealand, you need an import permit from MPI. Apply via the Biosecurity New Zealand portal. The application requires species, breed, microchip number, vaccination history, titre test results, and origin country details.

Processing takes four to six weeks for straightforward applications. Apply well in advance of your travel date.

## Quarantine at Levin

All cats and dogs must serve their quarantine at the Beak Street quarantine facility in Levin. There is no home quarantine option for cats and dogs. The facility is managed by the government and meets high welfare standards.

Pre-book your quarantine slot as soon as you have a confirmed travel date. The facility books up quickly, particularly in the months around Christmas.

## Getting your pet to New Zealand

Air New Zealand accepts pets in the hold on domestic routes but has specific policies for international cargo. Most pets flying to New Zealand arrive as manifest cargo via Sydney or Singapore. Qantas does not accept pets on international routes.

Specialist pet relocation companies handle the full logistics for New Zealand, which is a well-known and well-serviced route.

## After quarantine

Once released, your pet is yours to take home. Reunions happen at the Levin facility or at a collection point arranged with your logistics provider. From there, your pet can travel within New Zealand freely, though all dogs must be registered with the local council within two months of arrival.

New Zealand has no breed bans at the national level, though the American Pit Bull Terrier is a banned breed under the Dog Control Act 1996.

**Official sources:**
- MPI New Zealand pet imports: mpi.govt.nz
- Levin quarantine facility: mpi.govt.nz
"""
    },
    {
        "slug": "pet-transport-cost-uk-to-australia",
        "title": "Cost of Moving a Pet from UK to Australia | 2026 Guide",
        "description": "How much does it cost to move a dog or cat from the UK to Australia? A detailed breakdown of vet fees, health certificate costs, DAFF fees, quarantine, and airline cargo charges.",
        "date": "2026-05-08",
        "tags": ["uk to australia cost", "pet transport cost", "australia quarantine fees", "pet relocation budget"],
        "faqs": [
            {
                "question": "How much does it cost to move a large dog from the UK to Australia?",
                "answer": "Total costs for moving a large dog from the UK to Australia typically range from GBP 4,000 to 8,000 or more, depending on the dog's size, the airline cargo rates at the time of booking, and the quarantine duration. This includes titre test, health certificate and APHA endorsement, Australian import permit fee, airline cargo charges, quarantine facility fees at PEQ Mickleham, and veterinary checks. Using a specialist relocation agent typically costs GBP 500 to 1,500 on top of the direct costs."
            },
            {
                "question": "How much does quarantine in Australia cost for a pet from the UK?",
                "answer": "Post-entry quarantine (PEQ) at the Mickleham facility in Victoria is charged per animal per day. As of 2025, DAFF charges approximately AUD 100 to 200 per day depending on species. A 10-day minimum quarantine for one cat costs approximately AUD 1,000 to 2,000. Dogs are often charged at a higher rate than cats. Pre-booking deposit is required."
            },
            {
                "question": "Are there ways to reduce the cost of moving a pet to Australia?",
                "answer": "The fixed costs (titre test, health certificate, DAFF permit, quarantine) cannot be avoided. Costs you can manage include: booking airline cargo early for better rates; comparing specialist agent quotes; consolidating multiple pets on one manifest if you have more than one animal; and choosing a direct route to minimise transit handling fees."
            }
        ],
        "body": """Moving a pet from the UK to Australia is not cheap. It is, however, absolutely achievable with the right planning and budget. Here is a realistic breakdown of what to expect, based on current 2025-2026 costs.

## The cost breakdown

**Pre-travel veterinary costs:**
- Microchip (if not already done): GBP 20 to 60
- Rabies vaccination: GBP 30 to 80
- Titre test (blood draw): GBP 60 to 120
- Titre test laboratory fee (UK approved lab): GBP 80 to 150
- Health certificate preparation by government-listed vet (within 10 days of travel): GBP 80 to 200
- APHA endorsement of health certificate: GBP 30 per animal

**Australian import requirements:**
- DAFF import permit application fee: approximately AUD 60 to 120
- Pre-export health treatment (such as internal parasite treatment): GBP 30 to 80

**Airline cargo charges:**
- These vary significantly by route, aircraft type, and time of year
- Typical range for a medium dog (e.g. Cocker Spaniel, crate approximately 70 x 50 x 50 cm): GBP 800 to 1,800
- Large dog (e.g. Labrador, crate approximately 90 x 60 x 67 cm): GBP 1,200 to 2,500
- Cat (small to medium, crate approximately 60 x 40 x 40 cm): GBP 600 to 1,200
- Rates from London Heathrow (LHR) to Sydney (SYD), Melbourne (MEL), or Brisbane (BNE)

**Quarantine at PEQ Mickleham (Australia):**
- Approximately AUD 100 to 200 per animal per day
- Minimum 10 days = approximately AUD 1,000 to 2,000 per animal
- Pre-booking deposit required

**Agent fee (optional but recommended):**
- GBP 500 to 1,500 for a specialist pet relocation agent to manage the full process

## Total estimated costs

| Pet size | Estimated total (GBP) |
|----------|-----------------------|
| Cat | 3,000 to 5,500 |
| Small dog | 3,500 to 6,000 |
| Medium dog | 4,000 to 7,000 |
| Large dog | 5,000 to 9,000 |

These figures are estimates based on typical market rates. Costs vary by route, airline, and the specific services required. Get quotes from at least two or three specialist agents before committing.

## Cost-saving tips

Early booking for airline cargo typically secures better rates. Routes via Singapore (Singapore Airlines Cargo) or Dubai (Emirates SkyCargo) are often competitive for UK-Australia services.

If you have two pets, check whether a combined cargo booking is cheaper than two individual bookings. Some agents offer multi-pet discounts.
"""
    },
    {
        "slug": "pet-transport-cost-usa-to-europe",
        "title": "Cost of Moving a Pet from USA to Europe | 2026 Guide",
        "description": "How much does it cost to move a dog or cat from the USA to Europe? Breakdown of USDA APHIS fees, airline cargo costs, EU entry requirements, and agent charges.",
        "date": "2026-05-08",
        "tags": ["usa to europe cost", "pet transport cost", "usda aphis fee", "eu pet import budget"],
        "faqs": [
            {
                "question": "How much does it cost to move a medium dog from the USA to Europe?",
                "answer": "Total costs typically range from USD 3,000 to 7,000 for a medium dog. This includes titre test laboratory fees (USD 80 to 200), USDA APHIS endorsement (USD 38 per document), health certificate vet fees (USD 100 to 200), airline cargo charges (USD 1,500 to 3,500 depending on crate size and route), and any local agent handling fees. Costs are lower for cats and small dogs."
            },
            {
                "question": "What is the USDA APHIS endorsement fee?",
                "answer": "USDA APHIS charges USD 38 per endorsement for health certificates, as of 2025. Priority service (24 hours) may cost more depending on the regional office. The endorsement fee is separate from the vet's fee for completing the health certificate, which can range from USD 80 to 250 depending on the practice."
            },
            {
                "question": "Are there cheaper ways to move a pet to Europe from the USA?",
                "answer": "The fixed costs (titre test, APHIS endorsement, health certificate) cannot be avoided. Airline cargo rates vary: booking early and flying on less popular routes (such as smaller European cities vs major hubs) can reduce cargo charges. Some owners find that transatlantic repositioning flights offer lower cargo rates, though routing via non-standard hubs may add complexity."
            }
        ],
        "body": """Relocating from the USA to Europe with a pet involves the EU titre test pathway, USDA APHIS endorsement, and transatlantic cargo. Here is a realistic 2026 cost breakdown.

## Pre-travel veterinary and regulatory costs

**Microchip (if not done):** USD 40 to 90

**Rabies vaccination:** USD 20 to 60 at a standard vet

**Titre test (blood draw at vet):** USD 80 to 150
**Titre test laboratory fee (Kansas State University or another USDA-approved lab):** USD 80 to 200
**Results turnaround:** two to four weeks

**Health certificate (vet fee):** USD 100 to 250. This must be completed within 10 days of travel by a USDA-accredited veterinarian using the correct EU-format certificate.

**USDA APHIS endorsement fee:** USD 38 per certificate. Allow three to five business days, or one to two days for priority service at additional cost.

## Airline cargo costs

Transatlantic cargo rates depend heavily on crate size, route, airline, and season.

| Pet/crate size | Estimated USA to Europe cargo cost (USD) |
|----------------|------------------------------------------|
| Cat (small crate) | 900 to 1,800 |
| Small dog | 1,200 to 2,500 |
| Medium dog | 1,800 to 3,500 |
| Large dog | 2,500 to 5,000 |

Routes from New York (JFK), Chicago (ORD), Los Angeles (LAX), or Washington Dulles (IAD) to major European hubs (London Heathrow, Frankfurt, Amsterdam, Paris CDG) generally have the most competitive rates and best cargo handling facilities.

## Agent fees

A specialist pet relocation agent will charge USD 500 to 2,000 for end-to-end management of the process. This is often worth the cost for first-time exporters, as a single documentation error can result in the pet being refused at the European Border Inspection Post.

## Total estimated costs (USD)

| Pet | Low estimate | High estimate |
|-----|-------------|---------------|
| Cat | 2,000 | 4,500 |
| Small dog | 2,500 | 5,500 |
| Medium dog | 3,000 | 7,000 |
| Large dog | 4,000 | 9,000 |

## Ways to reduce costs

Book airline cargo early. Direct routes are generally cheaper than connections. If you have more than one pet, ask your agent about consolidated booking. Consider less popular departure airports if rates at major hubs are significantly higher.
"""
    },
    {
        "slug": "understanding-pet-import-permits-by-country",
        "title": "Which Countries Require a Pet Import Permit? | 2026 Guide",
        "description": "Which countries require a formal import permit before your pet can arrive? A guide to countries that mandate advance permits and the steps to apply for each.",
        "date": "2026-05-08",
        "tags": ["import permit", "pet import", "advance permit", "dog import permit", "cat import permit"],
        "faqs": [
            {
                "question": "Do all countries require an import permit for pets?",
                "answer": "No. Many countries, including most EU member states, do not require a separate import permit for dogs and cats travelling under the EU Pet Travel Scheme. Instead, they require a health certificate and may require a titre test. However, countries like Singapore, Taiwan, the Philippines, Thailand, Australia, New Zealand, and South Africa require a formal advance import permit before the animal can travel."
            },
            {
                "question": "How far in advance should I apply for a pet import permit?",
                "answer": "It depends on the country. Australia recommends applying for the import permit at least six weeks before travel. Singapore's AVS typically takes two to four weeks. Taiwan's BAPHIQ typically takes two to three weeks. Thailand's DLD takes two to four weeks. The Philippines' BAI recommends applying at least 30 days before travel. Always apply earlier than the minimum, as processing times can extend."
            },
            {
                "question": "What happens if my pet arrives without the required import permit?",
                "answer": "The consequences vary by country, but in most cases, your pet will be refused entry, held in quarantine at your expense, or returned to the origin country at your cost. In Australia, animals arriving without the correct permit may be euthanised if no return flight can be arranged. Never travel with a pet to a permit-required country without confirmed advance approval."
            }
        ],
        "body": """One of the most common mistakes pet owners make is assuming that a health certificate and vaccinations are all that is needed for international travel. Many countries require a formal import permit issued in advance, before the animal is even loaded onto a flight.

## Countries that require advance import permits

**Australia**
Import permits are issued by the Department of Agriculture, Fisheries and Forestry (DAFF). Apply via the DAFF website. Permits are tied to a specific quarantine facility booking. Processing takes four to six weeks.

**New Zealand**
MPI (Ministry for Primary Industries) issues import permits. Processing takes four to six weeks. The permit is linked to a quarantine facility booking at Levin.

**Singapore**
AVS (Animal and Veterinary Service, NParks) issues import licences. Apply at least four weeks before travel via the GoBusiness portal. You must book an approved quarantine facility first.

**Taiwan**
BAPHIQ (Bureau of Animal and Plant Health Inspection and Quarantine) issues import permits. Apply at least three to four weeks before travel.

**The Philippines**
BAI (Bureau of Animal Industry) issues import permits. Apply at least 30 days before travel.

**Thailand**
DLD (Department of Livestock Development) issues import permits. Apply at least 15 to 30 days before travel.

**South Africa**
DALRRD (Department of Agriculture, Land Reform and Rural Development) requires an import permit. Apply at least four weeks before travel.

**Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, UAE**
Gulf countries generally require import permits from the Ministry of Agriculture or equivalent authority. Requirements vary by country; confirm directly with the destination country authority.

## Countries that do NOT require advance import permits

Within the EU, most countries do not require a separate import permit. The health certificate (EU AHC or EU pet passport) combined with vaccination records is sufficient for entry. The same applies to many developed countries that apply simplified frameworks.

Countries that generally do not require an advance permit for domestic pets include: USA (no federal permit for dogs from approved countries), Canada, UK, most EU member states, Japan, and Switzerland.

## What happens if you skip the permit

The risks of arriving without a required permit are severe. Australia has strict rules and animals without correct documentation may be detained indefinitely or returned at the owner's cost. Do not underestimate the risk.

## Practical tip

When researching a destination, check the official government veterinary authority website for the country, not third-party sources. Requirements change and only the official source is authoritative.
"""
    },
    {
        "slug": "summer-heat-pet-air-travel-precautions",
        "title": "Travelling with Pets in Summer Heat | Safety Guide 2026",
        "description": "How to protect your pet during summer air travel. Temperature embargoes explained, breeds at highest risk, how to time your flights, and what airlines do to keep animals safe in the heat.",
        "date": "2026-05-08",
        "tags": ["summer pet travel", "temperature embargo", "heat safety", "brachycephalic breeds", "pet cargo heat"],
        "faqs": [
            {
                "question": "What is an airline temperature embargo for pets?",
                "answer": "A temperature embargo is a policy that prevents an airline from loading live animals onto a flight when ground temperatures at the departure or arrival airport exceed a set threshold. Typical thresholds are 29 to 32 degrees Celsius (84 to 90 degrees Fahrenheit), depending on the airline. The embargo protects animals from the risk of heat stress or heat stroke during loading, unloading, and ground transit. If the embargo triggers on your travel date, your pet's flight will be rescheduled."
            },
            {
                "question": "Which dog breeds are most at risk during summer air travel?",
                "answer": "Brachycephalic (flat-faced) breeds are at significantly higher risk because they cannot pant as efficiently as normal-muzzled dogs. Breeds including Bulldogs, Pugs, French Bulldogs, Boxers, Boston Terriers, Pekingese, and flat-faced cats such as Persians should not travel in summer heat if avoidable. Double-coated Nordic and mountain breeds (Samoyed, Husky, Malamute, Saint Bernard) are also at elevated risk due to heat retention."
            },
            {
                "question": "What can I do to reduce heat risk for my pet during summer travel?",
                "answer": "Book the earliest morning departure available: ground temperatures are lowest in the early morning, reducing the risk of triggering an embargo. Choose routes that avoid stops in hot-climate airports during summer. Use a well-ventilated IATA-compliant crate. Freeze water in the crate bowl so it gradually melts rather than sloshing and becoming unavailable. Avoid summer travel for brachycephalic breeds if at all possible."
            }
        ],
        "body": """Summer is the busiest season for international pet relocation, and it is also the period of greatest risk for animals travelling in aircraft holds. Understanding the heat risks and how airlines manage them will help you protect your pet and avoid last-minute cancellations.

## Why heat is dangerous for pets in aircraft holds

The hold of a commercial aircraft is pressurised and temperature-controlled during flight, but animals on the ground are exposed to ambient temperatures during loading, unloading, and any tarmac wait. In summer, tarmac temperatures can be significantly higher than air temperatures due to heat absorption from the asphalt.

Dogs and cats regulate temperature primarily through panting. When ambient temperatures rise above about 27 degrees Celsius, the panting mechanism becomes less effective, and heat stress can develop quickly. Brachycephalic dogs and thick-coated breeds are at highest risk.

## Temperature embargo thresholds

Most airlines apply live animal temperature embargoes when ground temperatures at departure or arrival airports exceed a set level. Common thresholds:

- American Airlines: 29.5 degrees Celsius (85 degrees Fahrenheit)
- Delta Air Lines: 29.5 degrees Celsius
- United Airlines: 30.5 degrees Celsius
- Lufthansa: 30 degrees Celsius
- British Airways: 30 degrees Celsius

Some airlines apply blanket summer bans on brachycephalic breeds regardless of temperature.

Check your specific airline's current embargo thresholds before booking. Policies change and the thresholds listed above are approximate.

## Best and worst airports for summer pet travel

The hottest airports for summer pet travel include Dubai (DXB), Doha (DOH), Las Vegas (LAS), Phoenix (PHX), and other airports in hot desert climates. Even in summer, early morning departures at these airports may fall within acceptable temperature windows.

Cooler airports such as London Heathrow (LHR), Frankfurt (FRA), Amsterdam Schiphol (AMS), and Tokyo Narita (NRT) rarely trigger temperature embargoes.

## Practical steps to reduce summer travel risk

1. **Book the earliest morning departure.** Ground temperatures are lowest in the first two hours after sunrise.
2. **Choose non-stop routes.** Every transit adds handling exposure to ground temperatures.
3. **Freeze water in the crate bowl** so it is available as it melts.
4. **Check embargo policies before booking,** not after.
5. **Avoid travelling brachycephalic breeds in July and August** via hot climate airports.
6. **Consider holding at an air-conditioned facility** at the destination airport if you cannot collect immediately after landing.
7. **Ask your cargo agent about climate-controlled handling.** Some airlines and handling agents offer air-conditioned storage for animals waiting to be loaded or collected.
"""
    },
    {
        "slug": "air-freight-vs-manifest-cargo-pet-guide",
        "title": "Air Freight vs Manifest Cargo for Pets | Which is Better?",
        "description": "Understanding the difference between excess baggage, manifest cargo, and unaccompanied air freight for pet transport. Which option is safer, cheaper, and better for your animal.",
        "date": "2026-05-08",
        "tags": ["manifest cargo", "air freight pets", "excess baggage", "unaccompanied cargo", "pet transport method"],
        "faqs": [
            {
                "question": "What is the difference between excess baggage and manifest cargo for pets?",
                "answer": "Excess baggage means your pet travels on the same flight as you and is booked through the passenger airline. Manifest cargo means your pet travels as freight, potentially on a different flight, managed by the airline's cargo division or a freight forwarder. Excess baggage typically costs more per kilogram but keeps the pet on your flight. Manifest cargo is often cheaper for large animals and allows you to choose the best cargo route rather than being tied to a passenger route."
            },
            {
                "question": "Is manifest cargo safe for pets?",
                "answer": "Yes, manifest cargo is a safe and well-established method for international pet transport. The cargo hold of a commercial aircraft is pressurised and temperature-controlled. Animals transported as manifest cargo are subject to IATA Live Animal Regulations. The cargo handling team manages feeding, watering, and welfare throughout the journey. Many thousands of pets travel this way safely every year."
            },
            {
                "question": "Can my pet travel as unaccompanied air freight?",
                "answer": "Yes. Unaccompanied air freight (where the animal travels without the owner on the same flight) is a common method for long-haul pet transport. This is particularly useful when the owner is travelling to the destination ahead of the pet, or when the pet needs to travel via a different routing to comply with import regulations. Specialist pet freight agents manage the entire process."
            }
        ],
        "body": """When you look into moving your pet internationally, you will quickly encounter three terms: excess baggage, manifest cargo, and unaccompanied air freight. They sound similar but work differently, and choosing the right option depends on your pet's size, your route, and your timeline.

## Excess baggage (accompanied)

Your pet travels on the same flight as you, booked through the passenger airline as excess baggage. You check your pet in at the departure airport, and they travel in the pressurised hold of your aircraft.

**Advantages:**
- Your pet is on your flight and arrives when you do
- Simpler coordination: one booking, one transit
- You know exactly which flight your pet is on

**Disadvantages:**
- Cabin/hold space is limited and must be booked well in advance
- Many long-haul routes have no capacity for live animals
- Rates can be higher than cargo for large animals
- Your routing choices are constrained to routes where your airline accepts pets

## Manifest cargo (airline cargo division)

Your pet is booked as cargo through the airline's cargo division, often on the same aircraft as passengers but managed separately. Specialist handling staff manage the animal at origin, transit (if any), and destination.

**Advantages:**
- Access to dedicated cargo routing options
- Often cheaper for large animals
- Not dependent on the same flight as the owner
- More flexible routing options (e.g. via a transit hub with better cargo handling)

**Disadvantages:**
- Your pet may travel on a different date than you (if cargo schedules differ)
- More complex coordination with cargo agents
- Cargo offices have different booking and documentation requirements from passenger services

## Unaccompanied air freight

The same as manifest cargo in practice, but specifically describes the situation where the owner is not on the same aircraft or is not travelling at all. This is common when:
- The owner arrives at the destination several days before the pet
- The pet needs to transit via a country the owner is not visiting
- The owner is shipping a pet to another family member in a different country

Specialist pet freight agents manage the full chain: collection from the owner, crate preparation, documentation, airline booking, customs clearance at destination, and delivery.

## Which is better?

For most international moves, manifest cargo via a specialist pet relocation agent is the most practical and often the most cost-effective option, particularly for large dogs. It offers the most routing flexibility and the most experienced handling staff.

For cats and small dogs, excess baggage on the same flight as the owner is a viable and convenient option where the route and airline allow it.

Discuss both options with at least two specialist agents before deciding.
"""
    },
]


def write_article(article):
    slug = article["slug"]
    path = os.path.join(BLOG_DIR, slug + ".md")
    if os.path.exists(path):
        print(f"  SKIP (exists): {slug}")
        return False

    faqs_yaml = ""
    for faq in article["faqs"]:
        q = faq["question"].replace('"', "'")
        a = faq["answer"].replace('"', "'")
        faqs_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    tags_yaml = "\n".join(f'  - "{t}"' for t in article["tags"])

    content = f"""---
title: "{article['title']}"
description: "{article['description']}"
date: "{article['date']}"
type: "blog"
author: "PetTransportGlobal Editorial Team"
slug: "{slug}"
url: "/pet-transport/blog/{slug}/"
seo:
  title: "{article['title']}"
  description: "{article['description']}"
tags:
{tags_yaml}
faqs:
{faqs_yaml}---

{article['body'].strip()}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  WRITE: {slug}")
    return True


def main():
    written = 0
    skipped = 0
    for article in ARTICLES:
        if write_article(article):
            written += 1
        else:
            skipped += 1
    print(f"\nDone. Written: {written} | Skipped: {skipped} | Total: {written + skipped}")


if __name__ == "__main__":
    main()
