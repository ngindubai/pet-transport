"""
generate_blog_articles_batch3.py — final batch to reach 50 blog articles.
Topics: EU pet travel post-Brexit, holiday travel, breed guides, timeline planner,
Korea, Thailand, quarantine survival, airline comparison.
"""
import os
from datetime import date

BLOG_DIR = os.path.join("site", "content", "blog")
TODAY = date.today().isoformat()


def article(slug, title, desc, tags, pub_date, content_body, faqs=None):
    tag_list = "\n".join(f'  - "{t}"' for t in tags)
    faq_block = ""
    if faqs:
        faq_lines = []
        for q, a in faqs:
            faq_lines.append(f'  - question: "{q}"\n    answer: "{a}"')
        faq_block = "faqs:\n" + "\n".join(faq_lines) + "\n"

    return f"""---
title: "{title}"
description: "{desc}"
date: "{pub_date}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{title} | PetTransportGlobal"
  description: "{desc}"
tags:
{tag_list}
{faq_block}---

{content_body}
"""


ARTICLES = [

    ("eu-pet-travel-post-brexit-uk-guide",
     "EU Pet Travel After Brexit: Why Your Pet Passport No Longer Works",
     "Post-Brexit UK pet passports are not accepted in the EU. Here's what replaced them, how to get an Animal Health Certificate, and which countries still accept UK passports.",
     ["uk", "europe", "brexit", "planning"],
     "2026-05-02",
     """Before Brexit, a UK pet passport was accepted for travel to all EU member states. The pet passport system was an EU creation, and the UK was a participant. That ended on 1 January 2021.

## What Changed on 1 January 2021

UK-issued pet passports are no longer valid for travel to:
- All 27 EU member states
- Norway, Iceland, Liechtenstein (EEA countries)

This catches people out years after it happened. The physical passport document still exists in UK vets' filing cabinets. It still has pages filled out correctly. And it is now worthless for EU entry.

## What Replaced the Pet Passport

For travel from the UK to the EU, your pet now needs an **Animal Health Certificate (AHC)**. Key points:

- Issued by a **APHA-authorised vet** (not every vet — check before booking)
- Valid for **10 days** from the date of issue for entry into the EU
- Valid for **4 months** for onward travel within the EU once inside
- Cannot be reused — each trip requires a new certificate
- Cannot be issued in advance and stored

The AHC follows the official EU-UK trade agreement format. It confirms microchip, vaccination status, and fit-to-travel status.

## Microchip and Rabies Requirements

These have not changed:
- ISO 15-digit microchip required
- Up-to-date rabies vaccination required
- The vaccination must have been given after microchipping

For countries like France, Germany, Spain, and all other EU member states, no titre test is required for UK pets. The AHC and current vaccination record are sufficient.

## Tapeworm Treatment

Dogs travelling to Finland, Ireland, Northern Ireland, Malta, and Norway require a **tapeworm treatment certificate** — Praziquantel administered by a vet within 24-120 hours before arrival.

## Northern Ireland Is Different

Northern Ireland has a different status post-Brexit. Travel between Great Britain and Northern Ireland for pets follows specific rules that have changed multiple times since 2021. Check current DAERA (Department of Agriculture, Environment and Rural Affairs) guidance before travelling.

## If You Have an Old UK Pet Passport

It may still record your pet's microchip number and vaccination history. That information is useful — your vet can transcribe it to the AHC. But the passport document itself cannot substitute for the AHC.

## Returning to the UK

When returning to the UK from the EU, your pet needs to meet UK entry requirements:
- Microchip
- Valid rabies vaccination
- AHC issued in the EU by an EU-listed vet
- Tapeworm treatment (dogs) 24-120 hours before return

The UK issued its own AHC format post-Brexit. EU-issued AHCs for UK entry follow the agreed bilateral format.

---

*Sources: UK APHA, European Commission pet movement regulations. Data current as of {TODAY}.*
""",
     [
         ("Can I use my old UK pet passport to travel to France?", "No. UK pet passports issued before Brexit are no longer valid for entry into any EU member state. You need a new Animal Health Certificate (AHC) issued by a APHA-authorised vet within 10 days of travel. This applies to all EU countries including France, Germany, Spain, Italy, and Portugal."),
         ("Do I need a titre test to take my pet from the UK to Europe?", "No. The UK is on the EU's approved third country list for pet imports, and no titre test is required for dogs or cats. A current rabies vaccination and a valid Animal Health Certificate are the standard requirements."),
     ]
    ),

    ("south-korea-pet-import-guide",
     "South Korea Pet Import Guide: APQA Requirements, Quarantine, and the 10-Day Hold",
     "South Korea requires pets from non-approved countries to undergo quarantine. Here's what the 10-day inspection involves, which countries are exempt, and how to prepare.",
     ["south-korea", "asia", "planning"],
     "2026-05-05",
     """South Korea's pet import system is managed by **APQA** (Animal and Plant Quarantine Agency), and the rules vary significantly depending on which country your pet is coming from.

## Approved vs Non-Approved Countries

South Korea divides origin countries into approved (rabies-free) and non-approved (rabies-present).

**Approved countries (no quarantine required, basic inspection only):**
Australia, New Zealand, Iceland, Fiji, Hawaii (USA), Guam, and a handful of others.

**Non-approved countries (full import inspection, possible quarantine):**
The UK, USA (mainland), Canada, most EU countries, and most of the world.

Pets from non-approved countries face a **10-day quarantine inspection** at an APQA-designated facility unless specific vaccination criteria are met.

## Avoiding Quarantine

Pets from non-approved countries can avoid quarantine if:
1. The pet has a valid rabies vaccination
2. A titre test confirms ≥0.5 IU/mL result
3. The titre test is from an approved lab
4. All documentation is correct

With a satisfactory titre test, the 10-day quarantine is reduced or eliminated. Without it, 10 days at the government facility is standard.

## Documentation Required

- ISO 15-digit microchip
- Rabies vaccination certificate
- Titre test result (if seeking to avoid quarantine)
- Health certificate issued within 10 days of travel
- Import quarantine permit (apply through APQA's online system)

## Flights Into South Korea

Pets typically arrive at Incheon International Airport (ICN) outside Seoul. APQA's inspection facility is based there. Gimhae International Airport in Busan also handles pet arrivals with APQA presence.

Pre-notify APQA at least **7 days before arrival** with your pet's documentation.

## Cost Estimate (UK to South Korea)

| Item | Estimated Cost |
|------|----------------|
| Titre test | £150 |
| Health certificate + endorsement | £250 |
| 10-day quarantine (if applicable) | KRW 300,000-600,000 (~£180-360) |
| Airline cargo | £400-900 |
| **Total** | **~£1,000-2,000** |

---

*Sources: APQA South Korea official import requirements. Data current as of {TODAY}.*
""",
     [
         ("Does my dog need quarantine to enter South Korea from the UK?", "Pets from the UK face a potential 10-day inspection period at an APQA facility. This can be avoided with a satisfactory rabies titre test result (≥0.5 IU/mL from an approved lab). With full documentation including a titre test, most pets from the UK are released after inspection without serving a full 10-day hold."),
     ]
    ),

    ("thailand-pet-import-guide",
     "Moving Pets to Thailand: DLD Requirements, Quarantine, and Bangkok Airport Pickup",
     "Thailand requires a government-issued import permit, health certificate, and potentially a quarantine stay. Here's the full process for moving your dog or cat to Bangkok.",
     ["thailand", "asia", "planning"],
     "2026-05-08",
     """Thailand's Department of Livestock Development (**DLD**) manages pet imports. The process is moderately complex but well-documented, and tens of thousands of expat families have completed it successfully.

## Core Requirements

- **ISO 15-digit microchip** (required before any documentation)
- **Rabies vaccination:** current, administered after microchipping
- **Import permit from DLD:** apply before travel through the DLD or via the Thai consulate in your country
- **Health certificate:** issued within 10 days of travel, endorsed by the government veterinary authority in your country
- **Rabies titre test:** required for pets from non-approved countries — the UK requires a titre test. Result must be ≥0.5 IU/mL. Blood drawn at least 30 days after vaccination.

## Quarantine

Thailand operates a **30-day mandatory quarantine** for pets from most countries, including the UK. The quarantine is served at a DLD-approved facility at Suvarnabhumi Airport (BKK) in Bangkok.

Some sources report shorter periods under certain conditions — verify current DLD policy before booking, as rules update periodically.

The quarantine facility at Suvarnabhumi is well-staffed with experienced veterinary care. You can visit your pet during the quarantine period.

## Cost Estimate

| Item | Estimated Cost |
|------|----------------|
| Titre test | £150 |
| Import permit (DLD fee) | THB 1,000-2,000 (~£22-44) |
| Health certificate + endorsement | £250 |
| Airline cargo (UK-Bangkok) | £400-1,000 |
| 30-day quarantine | THB 30,000-60,000 (~£660-1,320) |
| Agent fee | £300-600 |
| **Total** | **~£2,000-3,500** |

## Arriving at Suvarnabhumi (BKK)

Your pet arrives via the cargo terminal at Suvarnabhumi. Arrange advance collection with a Thai-licensed customs agent — your pet cannot be collected without a cleared import permit and customs agent involvement. A Bangkok-based IPATA agent can arrange this.

---

*Sources: Thailand DLD import requirements. Data current as of {TODAY}.*
""",
     [
         ("How long is pet quarantine in Thailand?", "Thailand's standard quarantine period is 30 days at a DLD-approved facility. Some updated provisions may allow a shorter period under specific conditions — verify current DLD requirements before booking. The 30-day quarantine applies to pets from most countries including the UK, USA, and Australia."),
     ]
    ),

    ("pet-relocation-timeline-12-month-planner",
     "International Pet Relocation: A 12-Month Planning Timeline",
     "Australia needs 8 months. Japan needs 9. Even easy routes benefit from 3 months of lead time. This month-by-month guide walks you through the entire pre-travel process.",
     ["planning", "guide", "timeline"],
     "2026-05-10",
     """Most pet relocation disasters happen because of timing — not because of complexity. Start too late, miss a window, get a low titre test result, and you're looking at a 6-month delay while the household has already moved.

This guide is a planning template. Fill in the dates for your specific route.

## Starting Point: How Much Time Do You Have?

Before anything else, identify your latest permitted travel date for your pet and work backward. For most routes:

| Destination | Minimum Lead Time |
|-------------|------------------|
| Australia | 8-9 months |
| Japan | 9-10 months |
| New Zealand | 5-6 months |
| Singapore | 3-4 months |
| UK (from non-listed country) | 4-5 months |
| Thailand | 3-4 months |
| USA/Canada | 1-2 months |
| EU (from UK) | 2-4 weeks |

If you have less time than the minimum for your route, contact a specialist agent immediately. Some cases can be accelerated; others cannot.

## Month 12-10 Before Travel: Research

- Identify your destination country's import requirements (DAFF, MAFF, APHA, MOCCAE, etc.)
- Confirm your pet's microchip number and verify it reads correctly
- Check that the microchip was implanted before any rabies vaccination on record
- Research IPATA-registered agents for your route
- Book initial consultation with your chosen agent

## Month 10-8 Before Travel: Vaccinations and Titre Test

- **Month 10:** Confirm vaccination status. If vaccination is not current or is approaching expiry, re-vaccinate at the earliest permitted point.
- **Month 9:** Blood draw for titre test (minimum 30 days after vaccination). Use an approved laboratory — confirm this with your vet before drawing blood.
- **Month 8-9:** Receive titre test result. If satisfactory (≥0.5 IU/mL), record the date — this is Day 0 for your waiting period countdown.

If the result is below threshold, re-vaccinate and retest. Add 30 days minimum to your timeline.

## Month 8-6 Before Travel: Permits and Bookings

- Apply for destination country import permit (DAFF for Australia, MAFF for Japan, APQA for Korea, DLD for Thailand, MOCCAE for UAE)
- For Australia: book Mickleham quarantine space — do not wait for the permit to arrive first
- Research airline options and verify breed restrictions apply or don't apply to your pet
- Purchase crate, introduce to your pet, allow several weeks for familiarisation

## Month 6-4 Before Travel: Logistics

- Confirm airline booking with cargo space reserved
- Confirm quarantine booking (if applicable)
- Book connecting transport to the airport
- Prepare "second set of everything" — copies of all documentation

## Month 2 Before Travel: Pre-Travel Checks

- Confirm all documents are assembled and cross-reference microchip numbers
- Confirm health certificate appointment with your vet (within the required window before departure)
- Re-confirm airline cargo booking
- Re-confirm quarantine booking

## Week 2-1 Before Travel: Health Certificate Window

- **10 days before travel (7 days for Australia):** Vet appointment for health certificate
- Submit to government endorsement authority immediately (APHA, USDA, etc.)
- Chase endorsement if not returned within 3 working days
- **24-120 hours before travel (dogs):** Tapeworm treatment if required for destination

## Day of Travel

- Arrive at cargo check-in 3-4 hours before departure (confirm exact requirement with airline)
- Bring originals and copies of all documents
- Have water in crate before check-in
- Take photos of your pet in the crate before handover

---

*Data current as of {TODAY}.*
""",
     [
         ("When is the latest I can start preparing to move my pet to Australia?", "For Australia, you need a minimum of 8-9 months of lead time due to the 180-day waiting period after a satisfactory titre test result (plus 30 days between vaccination and blood draw, plus processing time). If you have less than 8 months before your intended travel date, contact an IPATA-registered agent immediately to assess whether acceleration is possible."),
         ("What is the first thing I should do when planning an international pet move?", "Verify your pet's microchip number is correct and was implanted before any rabies vaccination. This is the foundation of the entire documentation chain. Then identify your destination country's exact import requirements — not a general summary, but the official regulatory document. Your vet and a specialist agent can help interpret the requirements."),
     ]
    ),

    ("pet-cargo-vs-excess-baggage-what-is-the-difference",
     "Pet Cargo vs Excess Baggage: What's the Difference and Which Is Right for Your Pet?",
     "Excess baggage means your pet flies on the same plane as you. Cargo means it might not. Here's how to choose and when each option applies.",
     ["airlines", "cargo", "planning"],
     "2026-05-12",
     """Airlines offer two main ways to transport a pet that cannot travel in the cabin: **excess baggage** (also called checked baggage or accompanied excess) and **cargo**. The terms are often confused, and the distinction matters.

## Excess Baggage (Accompanied)

Excess baggage means your pet is checked in at the passenger terminal, loaded onto the same flight you are on, and collected from the oversized baggage belt at your destination. You and your pet travel on the same aircraft.

**Advantages:**
- Same aircraft as you — if your flight is delayed, your pet is delayed with you
- Simpler logistics — handled at the passenger terminal
- Generally cheaper than cargo for the same route
- Your pet arrives when you arrive

**Limitations:**
- Only available on certain routes and airlines
- Weight limits vary (typically up to 45kg including crate for checked baggage, some airlines lower)
- Booking must be made in advance — live animals cannot be added at check-in
- Airline must operate the route and have live animal capability on that aircraft type

## Cargo (Unaccompanied)

Cargo means your pet is shipped as freight, handled through the airline's cargo division, and may travel on a different aircraft to you — possibly on the same day, possibly a day earlier or later.

**Advantages:**
- Available on more routes (cargo networks are broader than passenger networks)
- Can be sent before you travel (useful if you need to arrive before your pet is ready, or vice versa)
- May be the only option for very large dogs that exceed excess baggage limits

**Limitations:**
- More complex logistics — requires cargo bookings separate from your ticket
- Pet may travel on a different flight
- If your cargo flight is delayed, you may be at the destination while your pet is still at the origin
- More ground handling events

## Which to Choose

For most international pet moves, **excess baggage is preferable** if available on your route:
- Same aircraft = same delay/cancellation treatment
- Simpler documentation chain
- Usually cheaper

Use cargo when:
- Excess baggage is not available on your route
- Your pet exceeds the airline's excess baggage weight limit
- You are sending your pet separately (e.g., pet travels ahead while you sort final moving logistics)
- Your route requires a specialist cargo handler (e.g., Lufthansa PetLounge for long-haul)

---

*Data current as of {TODAY}.*
""",
     [
         ("Does my pet fly on the same plane as me if I check it as excess baggage?", "Yes. Excess baggage (checked baggage) means your pet is on the same aircraft as you. If your flight is delayed or cancelled, your pet is affected the same way you are. This is one of the main advantages over cargo, where your pet may travel on a different flight."),
         ("What is the weight limit for a dog as excess baggage?", "Weight limits vary by airline. Most carriers allow up to 32-45kg (including crate) as checked excess baggage; some airlines use lower limits. Verify with your specific airline for your route. If your dog exceeds the limit, cargo is the alternative."),
     ]
    ),

    ("malaysia-pet-import-guide",
     "Moving Pets to Malaysia: DVS Requirements, Quarantine, and Kuala Lumpur Arrivals",
     "Malaysia's DVS manages pet imports with a controlled permit system. Here's what you need, how long quarantine lasts, and how collection from KLIA works.",
     ["malaysia", "asia", "planning"],
     "2026-05-14",
     """Malaysia's **Department of Veterinary Services (DVS)** manages all pet imports. The system is structured and requires advance planning, but is navigable with proper preparation.

## Core Requirements

- **ISO 15-digit microchip**
- **Rabies vaccination** (administered after microchipping)
- **Import permit from DVS** — obtained before travel; apply at least 4-6 weeks in advance
- **Health certificate** issued within 10 days of travel, endorsed by the government vet authority in your country
- **Rabies titre test** — required for pets from countries where rabies is present (including the UK until confirmed otherwise)
- DVS also requires other vaccinations (DHPP for dogs, FVRCP for cats) to be current

## Quarantine

**Dogs from approved countries:** 7-day quarantine at a DVS-approved facility at the port of entry.

**Dogs from non-approved countries:** Longer quarantine periods apply. The UK may qualify for 7-day quarantine depending on the current approved country list — verify with DVS before booking.

**Cats:** Typically 7-day quarantine regardless of origin.

## Arriving at Kuala Lumpur International Airport (KLIA)

Pets arrive via the cargo terminal at KLIA. A DVS-approved veterinary officer inspects documentation and the animal on arrival. You cannot collect your pet directly — a licensed customs agent must handle clearance.

Most IPATA agents for Malaysia can arrange airport collection and deliver your pet to the quarantine facility and then to your address after the quarantine period ends.

## Key Documents Checklist

- [ ] Import permit from DVS
- [ ] Microchip certificate
- [ ] Vaccination records
- [ ] Titre test result (approved lab)
- [ ] Health certificate (endorsed)
- [ ] IATA-compliant crate

---

*Sources: Malaysian DVS import conditions. Data current as of {TODAY}.*
""",
     [
         ("How long is quarantine for a dog entering Malaysia from the UK?", "Typically 7 days at a DVS-approved facility for dogs from approved countries. Verify the current approved country list with Malaysian DVS before booking — approved status can change. Non-approved country pets may face longer quarantine periods."),
     ]
    ),

    ("pet-quarantine-survival-guide",
     "Pet Quarantine: How to Prepare Your Animal, Survive the Separation, and Visit",
     "Quarantine is hard — on your pet and on you. Here's how to prepare your animal, what to pack, whether and how to visit, and what to expect on release day.",
     ["quarantine", "welfare", "planning"],
     "2026-05-16",
     """Quarantine is the hardest part of international pet relocation for most owners. Your animal is in an unfamiliar facility, in a strange country, without you. And you are in a new home, without them.

The good news: the overwhelming majority of pets come through quarantine healthy, and often calmer than you expected.

## Preparing Your Pet Before Quarantine

**Crate training:** If your pet has been crate trained before departure, the quarantine kennel or cattery is less alien. A familiar crate smell — a worn t-shirt, their usual bedding — helps. Check whether the facility allows you to include personal items; some do, some restrict it for biosecurity reasons.

**Veterinary fitness check:** Any health issue that was borderline before travel becomes a genuine concern during quarantine. Ensure your vet is satisfied your animal is healthy before you commit to the journey.

**Diet:** Know what your animal eats and inform the facility. Most quarantine facilities will use their standard diet unless you provide food or make specific arrangements. A sudden diet change during the stress of quarantine can cause digestive issues. If your pet has dietary needs, arrange this in advance.

## What to Pack

For quarantine, prepare a bag that may or may not be accepted depending on facility rules:

- A worn item of your clothing (unwashed) — familiar smell
- Usual bedding (some facilities allow soft bedding, others provide their own)
- 3-5 days of their regular food if the facility allows it
- Toy (check if permitted)
- Your contact details on everything

Label everything with your pet's name and your details.

## Can You Visit?

This varies by country:

- **Australia (Mickleham):** Yes, during visiting hours (typically weekday afternoons). Check the facility's current visiting schedule. You cannot take your pet out of the facility.
- **Singapore (AVS-approved facility):** Yes, the 30-day stay at an approved boarding facility generally allows visits.
- **Japan (MAFF quarantine):** Visiting is permitted in most cases — contact the facility in advance.
- **New Zealand:** Short inspection stay typically doesn't permit a visit.
- **Thailand (DLD facility):** Visiting is generally permitted — verify with the facility.

## The Psychological Reality

Some owners find the separation harder than expected. Others find it easier once they see the facility and meet the staff.

Practical coping:

- Get a contact number for the facility and use it. Regular updates from staff reduce anxiety more than any other single action.
- In Australia, Mickleham provides written updates and some facilities offer photos.
- Focus on the move itself — you have enough to do in the new country.

## Release Day

On release day:

- Arrive at the scheduled time — facilities operate on tight schedules and a late pickup delays the next animal's release
- Bring your collection documents and ID
- Have a secure vehicle ready — your pet may be disoriented after weeks or months in a facility
- Water and a short walk before the car journey
- Keep the first 24 hours calm at home

---

*Data current as of {TODAY}.*
""",
     [
         ("Can I visit my pet during quarantine in Australia?", "Yes. Mickleham Post Entry Quarantine facility in Victoria allows visits during weekday visiting hours. You cannot take your pet outside the facility, but you can spend time with them in a supervised area. Check the current visiting schedule on the Mickleham facility page — hours and booking requirements change."),
         ("How do I make quarantine less stressful for my pet?", "Crate train before travel so the kennel environment is less alien. Pack a worn item of your clothing (unwashed) and familiar bedding if the facility allows it. Ensure your pet is eating a familiar diet — arrange this with the facility in advance. Most pets adjust within the first few days; the early period is the hardest."),
     ]
    ),

    ("british-airways-pet-transport-guide",
     "British Airways Pet Transport: What BA Actually Allows and What Has Changed",
     "British Airways has significantly restricted pet transport in recent years. Here's what BA currently accepts, what it has banned, and what your alternatives are.",
     ["airlines", "british-airways", "planning"],
     "2026-05-19",
     """British Airways is one of the most frequently searched airlines for UK pet transport. And for most routes, it is also one of the most restricted.

## Current BA Pet Policy (2026)

**Cabin:** British Airways does not allow pets in the cabin on any route (with the exception of trained assistance dogs with the relevant documentation).

**Cargo:** BA previously operated a cargo pet service (WorldCargo). BA's current policy on general pet cargo shipments has been significantly curtailed — verify the current status directly with BA Cargo before assuming the service is available on your route.

**Assistance animals:** Trained guide dogs, hearing dogs, and other registered assistance animals travel in the cabin with their handler, free of charge, on most BA routes. Requirements include advance notification and documentation from the relevant national authority.

## What BA Has Banned

British Airways has a **year-round cargo ban on brachycephalic breeds**. This covers all flat-faced dog and cat breeds including:

- English Bulldog
- French Bulldog
- Pug
- Boston Terrier
- Boxer
- Persian cat
- Himalayan cat
- British Shorthair cat

## Alternative Airlines for UK Departures

If BA is not available for your route or your pet, consider:

- **Lufthansa** (via Frankfurt or Munich) — comprehensive cargo service via PetLounge
- **KLM** (via Amsterdam) — good European hub with cargo pet handling
- **Air France** (via Paris CDG) — European and long-haul cargo options
- **Singapore Airlines** (Heathrow direct) — Asian routes
- **Cathay Pacific** (Heathrow direct) — Asian routes via Hong Kong

For USA routes specifically, **Virgin Atlantic** and **American Airlines** both handle pet cargo. Check current breed restrictions for each.

## Booking Process

For cargo transport via airlines that still offer the service, book through the airline's cargo division (not the passenger booking system). Quotes are provided based on your pet's crate weight and dimensions.

---

*Sources: British Airways published pet policies. Policies subject to change — verify directly with BA before booking. Data current as of {TODAY}.*
""",
     [
         ("Can I bring a pet in the cabin on British Airways?", "No. British Airways does not allow pets in the cabin, on any route, for any passenger (except trained assistance animals with the relevant documentation). All pets must travel as cargo."),
         ("What happened to the British Airways pet cargo service?", "BA has significantly reduced its general pet cargo service in recent years. The service that previously operated under WorldCargo is no longer broadly available. Verify the current status directly with BA Cargo for your specific route — availability varies. For most UK departures, Lufthansa, KLM, and Air France offer more comprehensive cargo pet programs."),
     ]
    ),

    ("philippines-pet-import-guide",
     "Philippines Pet Import Guide: BAI Requirements, Accreditation, and Manila Arrivals",
     "The Philippines Bureau of Animal Industry (BAI) controls pet imports. Here's what you need, how long quarantine lasts, and how to collect your pet from NAIA.",
     ["philippines", "asia", "planning"],
     "2026-05-21",
     """The **Bureau of Animal Industry (BAI)** in the Philippines manages all pet imports. The process requires an import accreditation number and advance documentation, but is achievable with proper planning.

## Core Requirements

- **ISO 15-digit microchip** (readable before travel)
- **Rabies vaccination:** current, administered after microchipping
- **Rabies titre test:** required for pets from most countries. Result must be ≥0.5 IU/mL from a BAI-approved laboratory.
- **BAI Import Accreditation Number:** applied for before travel. The accreditation confirms the owner is approved to import the specific animal.
- **Health certificate:** issued within 7-10 days of departure (check current BAI requirement), endorsed by the government vet authority in your country
- **Veterinary Quarantine Clearance Certificate (VQCC):** applied for before travel

## Quarantine

All dogs and cats entering the Philippines undergo a mandatory 7-day quarantine at the BAI facility at the Ninoy Aquino International Airport (NAIA) in Manila.

**Cost (2026):** Approximately PHP 5,000-8,000 (£70-110) for 7 days.

## Manila (NAIA) Arrival Process

Pets arrive via the cargo terminal at NAIA. BAI quarantine officers inspect the documentation and the animal. Your import accreditation documents must be presented.

Collection after quarantine: You can collect directly or through a customs broker. BAI releases the pet on the last day of quarantine after a final health check.

## Approved Labs for Titre Testing

BAI publishes a list of approved laboratories for the rabies titre test. In the UK, APHA Weybridge is typically on this list. Verify the current BAI approved lab list before drawing blood.

---

*Sources: Philippines BAI import requirements. Data current as of {TODAY}.*
""",
     [
         ("How long is quarantine for a dog entering the Philippines?", "7 days at the BAI facility at NAIA, Manila. This applies to all imported dogs and cats regardless of origin country. The 7-day period begins on the day of arrival."),
         ("Do I need a titre test to bring my dog to the Philippines from the UK?", "Yes. The Philippines requires a rabies titre test result of ≥0.5 IU/mL from a BAI-approved laboratory. The blood draw must be at least 30 days after vaccination. Verify the current approved lab list with BAI before proceeding."),
     ]
    ),

    ("taiwan-pet-import-guide",
     "Taiwan Pet Import Guide: Quarantine Tiers, BAPHIQ Requirements, and Taipei Arrivals",
     "Taiwan uses a tiered quarantine system based on your country's rabies status. UK pets face 7-day quarantine minimum. Here's how to prepare.",
     ["taiwan", "asia", "planning"],
     "2026-05-23",
     """Taiwan's **Bureau of Animal and Plant Health Inspection and Quarantine (BAPHIQ)** uses a tiered quarantine system that depends on your origin country's rabies status and your pet's documentation.

## The Three-Tier System

**Tier 1 (0-day quarantine):** Pets from countries on Taiwan's approved list with satisfactory titre test. Typically countries where Taiwan has high confidence in the regulatory framework — including New Zealand and Australia.

**Tier 2 (7-day quarantine):** Most approved Western countries, including the UK, EU, USA, Canada, and Japan, when documentation is correct including titre test.

**Tier 3 (21-day or longer quarantine):** Pets from non-approved countries or where documentation is incomplete.

Most UK-based pet owners will be looking at Tier 2 quarantine: 7 days.

## Documentation Required

- ISO 15-digit microchip
- Valid rabies vaccination (current)
- Titre test: ≥0.5 IU/mL from a BAPHIQ-approved laboratory. Blood drawn at least 30 days after vaccination.
- **Waiting period:** Pet cannot travel to Taiwan until at least 180 days after the titre test blood draw (not the result date)
- Import permit from BAPHIQ (apply before travel)
- Health certificate within 10 days of travel

## The 180-Day Wait

Like Japan, Taiwan's 180-day waiting period is measured from the blood draw date, not the result date. Plan accordingly — if your blood is drawn on Day 0 and results arrive on Day 14, you still have 166 days to wait from that point (not 180 days from the result).

## Arriving at Taipei (Taoyuan, TPE)

Pets arrive via the cargo terminal at Taiwan Taoyuan International Airport. BAPHIQ officers inspect documentation and the animal before the quarantine period begins.

---

*Sources: Taiwan BAPHIQ import requirements. Data current as of {TODAY}.*
""",
     [
         ("How long is quarantine for a UK dog entering Taiwan?", "7 days (Tier 2 quarantine) for pets from the UK with a satisfactory titre test and complete documentation. This can reduce to 0 days only for pets from Taiwan's Tier 1 approved countries (primarily New Zealand and Australia). UK pets achieving Tier 1 status is not typical."),
         ("Does Taiwan count the 180-day wait from blood draw or result date?", "From the blood draw date — the same as Japan. If blood is drawn on Day 0, your pet cannot travel to Taiwan until Day 180 from that date, regardless of when the result was received. This is different from the UK's 90-day wait, which runs from the result date."),
     ]
    ),

    ("choosing-the-right-vet-for-international-pet-travel",
     "Choosing the Right Vet for International Pet Travel: What to Look for and What to Ask",
     "Not every vet can issue international health certificates. Here's how to find an APHA-authorised vet in the UK, what qualifications matter, and what questions to ask before booking.",
     ["planning", "vets", "documentation"],
     "2026-05-25",
     """The health certificate for international pet travel must be issued by an **authorised vet** — not just any registered vet. In the UK, this means being listed with APHA as an Official Veterinarian (OV) for export health certificates. Many excellent, experienced vets are not on this list.

Booking the wrong vet means a certificate that cannot be endorsed. Finding this out two days before travel is a genuine emergency.

## What Is an Official Veterinarian (OV)?

An OV is a vet who has completed APHA's Official Controls Qualification (OCQ) for trade and has been authorised to issue Export Health Certificates (EHCs) on behalf of the UK government. This is different from simply being RCVS-registered.

The OV is authorised to sign the specific EHC format required for your destination country. Different destinations have different EHC forms — your OV must be authorised for the specific form your destination requires.

## How to Find an APHA-Authorised Vet

The most reliable method:
1. Use the **APHA OV finder** on the UK government website
2. Search by postcode or county
3. Filter by the specific export health certificate form you need (e.g., EHC Australia, EHC USA)

Alternatively, call your destination country's UK consulate or embassy — they may be able to recommend local vets experienced with their specific requirements.

## Questions to Ask Before Booking

Before committing to a vet for international documentation:

1. "Are you an authorised OV for the specific export health certificate for [destination country]?"
2. "How many times have you issued this specific certificate in the past year?"
3. "Are you familiar with the microchip verification requirement and timing rules?"
4. "Do you have the current version of the EHC form?" (forms update; old versions are rejected)
5. "What is your turnaround time for completed documentation?"

A vet who has never issued an EHC for Australia, for example, may inadvertently complete the form incorrectly. APHA's endorsement process sometimes catches errors; sometimes it does not.

## APHA Endorsement

After the OV issues the health certificate, it must be endorsed (countersigned) by APHA to be valid for most international destinations. APHA operates endorsement offices and a postal service:

- **Same-day endorsement:** At APHA offices (appointment required)
- **Postal endorsement:** 2-4 working days (check current times)

Factor endorsement time into your health certificate window.

---

*Sources: APHA UK Official Veterinarian requirements and export health certificate processes. Data current as of {TODAY}.*
""",
     [
         ("Can any vet issue an international health certificate for my pet?", "No. In the UK, international export health certificates must be issued by an Official Veterinarian (OV) authorised by APHA. Not all vets hold OV status, and OVs are authorised for specific destination country certificate forms. Use the APHA OV finder to locate an authorised vet for your specific destination."),
         ("What is APHA endorsement and why does my health certificate need it?", "APHA endorsement is the UK government's countersignature on your vet's health certificate, confirming it is authentic. Most destination countries — including Australia, the USA, Singapore, Japan, and all EU countries — require the APHA endorsement for the certificate to be valid. Without it, the certificate is not accepted at the border."),
     ]
    ),

    ("pet-transport-glossary",
     "International Pet Transport Glossary: Every Term You Will Encounter Explained",
     "BICON, FAVN, IATA LAR, OV, AHC — the acronyms in pet transport documentation can be bewildering. Here's a plain-English glossary of every term you're likely to encounter.",
     ["planning", "guide", "documentation"],
     "2026-05-27",
     """Pet transport documentation is full of acronyms and official terminology that can feel deliberately obscure. It isn't — these are precise technical terms that refer to specific regulations, tests, and authorities. Knowing what they mean helps you follow the documentation trail and spot errors before they become expensive.

## A

**AHC (Animal Health Certificate):** The document replacing EU pet passports for UK pets travelling to the EU. Issued by an OV, valid for 10 days for EU entry, 4 months for onward EU travel.

**APHA (Animal and Plant Health Agency):** UK government veterinary authority. Endorses export health certificates, approves Official Veterinarians, maintains approved laboratory lists.

**APQA (Animal and Plant Quarantine Agency):** South Korea's pet import authority. Issues import permits and manages quarantine.

**AVS (Animal and Veterinary Service):** Singapore's pet import authority, part of the National Parks Board (NParks).

## B

**BAI (Bureau of Animal Industry):** Philippines' pet import authority.

**BAPHIQ (Bureau of Animal and Plant Health Inspection and Quarantine):** Taiwan's pet import authority.

**BICON (Biosecurity Import Conditions database):** Australia's DAFF database of import conditions. Search BICON to find the exact current requirements for your specific animal's origin country.

## C

**CFIA (Canadian Food Inspection Agency):** Canada's pet import authority.

**Cold chain:** The requirement to maintain a specific temperature range (typically 2-8°C) during transportation of biological samples (e.g., titre test blood samples) from your vet to the laboratory.

## D

**DAFF (Department of Agriculture, Fisheries and Forestry):** Australia's pet import authority. Issues import permits, manages Mickleham quarantine.

**DLD (Department of Livestock Development):** Thailand's pet import authority.

**DVS (Department of Veterinary Services):** Malaysia's pet import authority.

## E

**EHC (Export Health Certificate):** UK government export document for animals. Each destination country has a specific EHC form. Issued by an OV, endorsed by APHA.

## F

**FAVN (Fluorescent Antibody Virus Neutralisation):** One of two approved methods for the rabies titre test. Measures the level of virus-neutralising antibodies in your pet's blood. The other method is RFFIT.

## I

**IATA (International Air Transport Association):** Sets the Live Animal Regulations (LAR) that airlines worldwide use for pet transport. IATA LAR specifies crate requirements, handling, and documentation.

**IPATA (International Pet and Animal Transportation Association):** Voluntary industry body for pet transport agents. IPATA membership indicates commitment to a code of conduct.

## L

**LAR (Live Animal Regulations):** IATA's rulebook for transporting animals by air. Updated annually. Specifies crate construction, labelling, handling, and documentation requirements.

## M

**MAFF (Ministry of Agriculture, Forestry and Fisheries):** Japan's pet import authority. Operates the Animal Quarantine Service (AQS).

**Mickleham:** The Post Entry Quarantine facility in Victoria, Australia, where all imported dogs and cats must serve their mandatory quarantine period.

**MOCCAE (Ministry of Climate Change and Environment):** UAE's pet import authority.

## O

**OV (Official Veterinarian):** A UK vet authorised by APHA to issue Export Health Certificates. Holds the OCQ (Official Controls Qualification) for the relevant trade certificate.

## R

**RFFIT (Rapid Fluorescent Focus Inhibition Test):** One of two approved methods for the rabies titre test, alongside FAVN.

**RNAT (Rabies Neutralising Antibody Test):** Generic term for the titre test. Also called FAVN, RFFIT, or simply the titre test depending on which method is used.

## T

**Titre test:** See RNAT, FAVN, RFFIT. A blood test measuring the level of rabies virus-neutralising antibodies. The threshold for most destination countries is ≥0.5 IU/mL.

## U

**USDA APHIS (Animal and Plant Health Inspection Service):** USA's agricultural authority, including pet import/export. Accredits US vets to issue export health certificates and endorses those certificates for international use.

---

*Data current as of {TODAY}.*
""",
     [
         ("What does BICON stand for in pet transport to Australia?", "BICON stands for Biosecurity Import Conditions. It is the Australian DAFF database that lists the exact current import conditions for each animal type from each origin country. Search BICON before starting any Australia import paperwork — it is the authoritative source for current requirements."),
         ("What is the difference between FAVN and RFFIT for a titre test?", "Both are approved methods for the rabies titre test measuring virus-neutralising antibodies. FAVN (Fluorescent Antibody Virus Neutralisation) is more widely used internationally. RFFIT (Rapid Fluorescent Focus Inhibition Test) is also accepted by most authorities. The threshold result (≥0.5 IU/mL) is the same for both. Your approved laboratory will use whichever method they are certified for."),
     ]
    ),

]


def main():
    os.makedirs(BLOG_DIR, exist_ok=True)
    generated = skipped = 0

    for slug, title, desc, tags, pub_date, body, faqs in ARTICLES:
        filepath = os.path.join(BLOG_DIR, f"{slug}.md")
        if os.path.exists(filepath):
            skipped += 1
            continue

        faq_pairs = faqs  # list of (question, answer) tuples

        faq_block = ""
        if faq_pairs:
            faq_lines = []
            for q, a in faq_pairs:
                faq_lines.append(f'  - question: "{q}"\n    answer: "{a}"')
            faq_block = "faqs:\n" + "\n".join(faq_lines) + "\n"

        tag_list = "\n".join(f'  - "{t}"' for t in tags)

        content = f"""---
title: "{title}"
description: "{desc}"
date: "{pub_date}"
type: "blog"
author: "Gareth - Founder, PetTransportGlobal"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{title} | PetTransportGlobal"
  description: "{desc}"
tags:
{tag_list}
{faq_block}---

{body}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        generated += 1
        print(f"  + {slug}.md")

    print(f"\nDone. Generated: {generated} | Skipped: {skipped}")
    total = len([f for f in os.listdir(BLOG_DIR) if f != "_index.md"])
    print(f"Total blog articles (excluding index): {total}")


if __name__ == "__main__":
    main()
