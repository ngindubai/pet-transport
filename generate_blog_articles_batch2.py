"""
Generate Task 3.4 blog articles — ramp from 12 to ~50.
38 new articles covering: country-specific guides, breed travel, airline guides,
cost deep-dives, paperwork how-tos, route-specific tips, and pet welfare.
All skip-if-exists. Content follows Wordsmith + Chameleon rules.
"""
import os
from datetime import date

BLOG_DIR = os.path.join("site", "content", "blog")
TODAY = date.today().isoformat()

# Each article: (slug, title, description, tags, date_offset_days, body_func)
# We use a rolling date starting 2026-03-01 to backfill publication history


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

    # ── COUNTRY GUIDES ──────────────────────────────────────────────────────────

    ("uk-to-australia-pet-transport-complete-guide",
     "UK to Australia Pet Transport: The Complete 2026 Guide",
     "Moving your pet from the UK to Australia is one of the world's most complex routes. This guide covers every step: titre test timing, Mickleham quarantine, approved labs, and what can go wrong.",
     ["australia", "uk", "quarantine", "planning"],
     "2026-03-03",
     """Moving a dog or cat from the UK to Australia is genuinely one of the hardest pet relocations in the world. Not because of cruelty or bureaucracy for its own sake, but because Australia is one of the last genuinely rabies-free countries on earth — and it intends to stay that way.

The good news is that it is entirely achievable. Thousands of families do it every year. The bad news is that it takes a minimum of six months from start to finish, and a single timing mistake can reset the clock.

## The Six-Month Minimum

Australia's Department of Agriculture, Fisheries and Forestry (DAFF) requires that your pet's rabies titre test result be at least 180 days old on the day of departure. That 180 days does not start from the date the blood is drawn — it starts from the date the laboratory confirms a satisfactory result (0.5 IU/mL or above).

So the earliest possible timeline looks like this:

1. Microchip implanted (if not already done — must predate any vaccination)
2. Rabies vaccination given
3. Blood drawn for titre test at least 30 days after vaccination
4. Sample sent to an approved laboratory — AAHL (CSIRO) or an approved state lab
5. **Day 0:** Satisfactory result received
6. **Day 180+:** Earliest permitted departure date

Miss any step, get a borderline titre result that requires a retest, or have the microchip implanted after the vaccination, and the clock resets.

## Approved Laboratories

DAFF only accepts titre test results from specific laboratories. For UK-based pets, this means:

- **APHA Weybridge** (Animal and Plant Health Agency)
- **Approved private labs** — check the current DAFF approved lab list at the time of testing

Do not assume your vet's preferred lab is on the list. Verify before drawing blood.

## The Import Permit

You need an import permit from DAFF before your pet can travel. Apply at least 4-6 months in advance — permits are processed in order, and seasonal demand means delays. The permit specifies the entry point (Melbourne is the only option for cats and dogs, because Mickleham is there).

## Mickleham: What to Expect

All dogs and cats entering Australia complete quarantine at the **Post Entry Quarantine facility at Mickleham, Victoria**. The minimum stay is 10 days. Your pet will be:

- Housed in individual or pair kennels/catteries
- Fed and watered twice daily
- Observed by biosecurity officers for signs of illness
- Given access to an outdoor run (dogs)

You can visit your pet during approved visiting hours, but cannot take your pet out of the facility.

The facility is closed on weekends and public holidays. Arrival must be on a weekday and the quarantine period excludes weekends — so a Monday arrival means the 10-day count does not include the following Saturday and Sunday.

**Summer arrivals (December-February):** DAFF issues explicit heat stress warnings. Brachycephalic breeds, elderly animals, and those with existing health conditions are at serious risk during the Australian summer. Book an autumn or spring arrival if possible.

## Cost Estimate (UK to Australia, 2026)

| Item | Estimated Cost |
|------|----------------|
| Microchip (if needed) | £20-50 |
| Rabies vaccination | £40-80 |
| Titre test (APHA) | £120-180 |
| Import permit | AUD 70 |
| Vet health certificate (UK) | £150-250 |
| Airline cargo fee (UK-AU) | £500-1,500+ |
| Quarantine (10 days minimum) | AUD 2,000-4,000+ |
| Pet transport agent | £300-800 |
| **Total** | **£3,500-8,000+** |

These are estimates. Agent fees vary significantly, and cargo costs depend on crate size and airline.

## Common Mistakes

**Microchip after vaccination.** The microchip must be implanted before the rabies vaccination. An unchipped pet receiving a vaccination means the vaccination is not valid for import purposes — you must start again.

**Using a non-approved lab.** Only approved laboratories are accepted. A titre test from an unapproved lab will be rejected.

**Booking Mickleham without a confirmed space.** The facility has limited spaces. Book as soon as you have a departure date in mind — not after you've booked flights.

**Ignoring the weekend rule.** Quarantine days do not count weekends. A Friday arrival delays release by two extra days compared to a Monday arrival.

---

*Sources: Australian DAFF import conditions database (BICON), Mickleham Post Entry Quarantine facility information. Data current as of {TODAY}.*
""",
     [
         ("How long does it take to move a pet from UK to Australia?", "A minimum of 6 months from when you receive a satisfactory rabies titre test result. The 180-day wait starts from the date of the approved lab result, not the vaccination date. Add time for permit processing and booking quarantine."),
         ("How much does UK to Australia pet transport cost?", "Budget £3,500-8,000+ for a straightforward case. This includes titre testing (£120-180), vet health certificate, airline cargo fees (£500-1,500+), quarantine at Mickleham (AUD 2,000-4,000+), and a professional agent. Complex cases or large breeds cost more."),
         ("Can I bring a Bulldog from the UK to Australia?", "Yes, but with extra care. Brachycephalic breeds face heat stress risk during Australian summer quarantine. DAFF issues heat stress warnings for December-February arrivals. Book an autumn or winter arrival and notify the quarantine facility of your breed in advance."),
     ]
    ),

    ("uk-to-new-zealand-pet-transport-guide",
     "UK to New Zealand Pet Transport: Complete Guide (2026)",
     "New Zealand has among the world's strictest pet import rules. This guide covers approved countries, titre test requirements, MPI permits, and the managed isolation process.",
     ["new-zealand", "uk", "quarantine", "planning"],
     "2026-03-07",
     """New Zealand and Australia share a biosecurity philosophy: protect island status at all costs. For pets, this means a process that is meticulous, unforgiving of errors, and ultimately rewarding when it works.

## Is the UK an Approved Country?

Yes. The UK is on New Zealand's **Group 1 approved country list** (MPI designation). This means:

- No quarantine on arrival (for most pets with compliant documentation)
- Titre test required, but the waiting period is shorter than for non-approved countries

## Pre-Travel Requirements

**Microchip:** ISO 15-digit microchip required. Must be implanted before vaccination.

**Rabies vaccination:** Up to date. If your pet has a lapsed vaccination, you may need to restart the titre test process.

**Rabies titre test:** Required for pets from the UK travelling to New Zealand. The result must be at least **0.5 IU/mL** and the test must be performed at an MPI-approved laboratory. In the UK, APHA Weybridge is the primary approved option.

**Waiting period:** For UK-based pets, the titre test result must be at least **3 months old** before travel (compared to Australia's 6 months).

**Import permit:** Required from MPI (Ministry for Primary Industries). Apply well in advance.

**Health certificate:** Issued by your vet and endorsed by APHA (UK government vet authority). Must be issued no more than 10 days before departure.

**Treatment certificates:** Tapeworm treatment (Praziquantel) required within 24-120 hours before departure.

## The Managed Isolation Process

New Zealand does not have a traditional quarantine facility for pets from approved countries. Instead, pets from Group 1 countries undergo:

- **Inspection on arrival** at the MPI border inspection post
- **Short hold** (typically 24-72 hours) while documentation is verified

If paperwork is in order, your pet is released directly to you. This is a significant advantage over the Australian 10-day minimum.

## Costs (UK to New Zealand)

| Item | Estimated Cost |
|------|----------------|
| Titre test (APHA) | £120-180 |
| Import permit | NZD 276 |
| Health certificate + APHA endorsement | £200-350 |
| Tapeworm treatment certificate | £30-60 |
| Airline cargo fee | £600-1,800+ |
| Agent fee | £300-700 |
| **Total** | **£1,500-4,000+** |

No quarantine cost is the major saving compared to Australia.

## Key Timing Rule

Plan a **minimum of 5 months** before travel:

1. Microchip in place
2. Rabies vaccination given
3. Blood drawn 30+ days after vaccination
4. Titre test result received (Day 0 of the 90-day wait)
5. **Day 90+:** Earliest departure

---

*Sources: MPI New Zealand import health standard IHS/CAT&DOG, APHA UK. Data current as of {TODAY}.*
""",
     [
         ("Does a UK pet need quarantine to enter New Zealand?", "Not for pets from Group 1 approved countries like the UK — provided all documentation is in order. Instead of full quarantine, pets undergo a 24-72 hour inspection hold at the MPI border post. This is much shorter than Australia's mandatory 10-day minimum."),
         ("How long before travel do I need the titre test for New Zealand?", "The titre test result must be at least 3 months (90 days) old on the day of travel. That 90-day wait starts from the date of a satisfactory result (0.5 IU/mL or above) from an MPI-approved laboratory."),
     ]
    ),

    ("moving-pets-to-japan-complete-guide",
     "Moving Your Pet to Japan: The 180-Day Rule and What It Really Means",
     "Japan's pet import rules are among the world's strictest. The 180-day titre test timing rule catches most people out. Here's exactly how to get it right.",
     ["japan", "quarantine", "planning", "titre-test"],
     "2026-03-10",
     """Japan surprises many pet owners. It looks straightforward — vaccinations, a titre test, a health certificate — until you realise that the timing of those steps must be almost surgically precise, or your pet faces a **180-day quarantine** instead of the standard 14 days.

## The Two Quarantine Outcomes

Japan's MAFF (Ministry of Agriculture, Forestry and Fisheries) uses a tiered system:

**14 days:** Pet meets all requirements in the correct order and timing. This is what you want.

**180 days:** Pet does not meet requirements, documentation is missing, or the titre test was not timed correctly. This is what you must avoid.

## The Exact Sequence Required

Japan requires these steps in this exact order, with no exceptions:

1. **Microchip implanted** (ISO 15-digit)
2. **Primary rabies vaccination** (at least 91 days after microchip)
3. **Booster rabies vaccination** (given before the titre test, if required)
4. **Titre test blood draw** — minimum 30 days after the last vaccination
5. **Titre test result confirmed** at a MAFF-approved laboratory: must be ≥0.5 IU/mL
6. **180 days after the titre test result date** — earliest permitted arrival in Japan
7. **Import inspection** booked with MAFF quarantine station
8. **Health certificate** issued no more than 10 days before departure

If any step is out of order or the timing is wrong, MAFF imposes the 180-day facility quarantine. At a government facility. At your expense.

## Wait — 180 Days from the Titre Test?

Yes. Unlike Australia (which measures 180 days from the titre test result), Japan measures **180 days from the date of the blood draw for the titre test** — not from when you receive the result.

This is a critical distinction. Your vet draws blood on Day 0. The lab reports a satisfactory result on Day 14. Japan counts from Day 0. So by the time you get the result, you have already used 14 of your 180 days of waiting.

Plan accordingly. Most families working with a professional agent are looking at a minimum 8-9 month preparation period for Japan.

## MAFF-Approved Laboratories

Only laboratories approved by MAFF can perform titre tests for Japan import. In the UK, APHA Weybridge is approved. In the US, the Kansas State University Veterinary Diagnostic Laboratory is a common choice. Always verify the current approved lab list on the MAFF website before drawing blood.

## Arrival Inspection

All pets entering Japan must arrive at an airport or port with a MAFF quarantine facility. Tokyo (Narita and Haneda), Osaka (Kansai), and Nagoya are the main options. You must **pre-notify MAFF at least 40 days before arrival** — failure to do so adds delays.

The quarantine station must receive your documentation before the pet arrives. Send copies well in advance.

## Cost Estimate (UK to Japan)

| Item | Estimated Cost |
|------|----------------|
| Titre test | £120-180 |
| Health certificate + APHA endorsement | £200-350 |
| MAFF pre-notification (no fee) | - |
| Airline cargo | £400-1,200+ |
| 14-day quarantine facility | ¥50,000-100,000 |
| Agent fee | £300-700 |
| **Total** | **£1,500-3,500+** |

---

*Sources: Japan MAFF Animal Quarantine Service (AQS), official import requirement documentation. Data current as of {TODAY}.*
""",
     [
         ("What happens if my pet's titre test timing is wrong for Japan?", "Your pet will face a mandatory 180-day quarantine at a MAFF quarantine station, at your expense. This is why professional guidance is strongly recommended for Japan — a single timing error costs months and significant money."),
         ("Which airports can my pet arrive at in Japan?", "Narita (Tokyo), Haneda (Tokyo), Kansai (Osaka), and Nagoya all have MAFF quarantine facilities. You must pre-notify MAFF at least 40 days before arrival and confirm which facility your pet will use."),
     ]
    ),

    ("moving-pets-to-singapore-what-you-need-to-know",
     "Moving Pets to Singapore: AVS Categories, Approved Countries, and What to Prepare",
     "Singapore uses a strict category system for pet imports. Here's which category your pet falls into, what documents you need, and how to book the required stay at an AVS facility.",
     ["singapore", "planning", "asia"],
     "2026-03-14",
     """Singapore's Animal and Veterinary Service (AVS) divides the world into categories based on rabies risk. Which category your home country falls into determines what your pet needs before it can enter Singapore.

## The Three Categories

**Category 1 (Approved Low-Risk Countries):** Australia, New Zealand, UK, most EU countries, Japan, USA, Canada, and others. Pets from Category 1 countries face the least restrictive requirements.

**Category 2 (Approved Higher-Risk Countries):** Various countries with controlled or present rabies. More documentation required.

**Category 3 (Non-Approved Countries):** No direct import permitted. Pet must first reside in an approved country for a set period.

Always verify the current AVS category list — it updates periodically and a country can move between categories.

## Core Requirements for Category 1 Pets

- ISO 15-digit microchip
- Valid rabies vaccination
- Titre test: required if your country is not on the simplified documentation list
- AVS import licence
- Health certificate issued and endorsed by a government vet
- Pre-arrival stay at an AVS-approved facility (mandatory, even for Category 1 pets)

## The Pre-Arrival Stay

All dogs and cats must stay at an **AVS-approved animal holding facility** for a minimum of **30 days after arrival** in Singapore. This is not a quarantine facility in the traditional sense — your pet is housed at a licensed boarding facility, and you can visit. But it is mandatory, and you pay the boarding costs.

Book your space before booking flights. Approved facilities have limited capacity.

## Permits and Timing

Apply for the **import licence from AVS** at least 4-6 weeks before travel. The licence specifies the approved entry point (Changi Airport only for air arrivals).

The health certificate must be issued no more than **7 days before departure** and endorsed by a government authority in your country.

## Cost Estimate (UK to Singapore)

| Item | Estimated Cost |
|------|----------------|
| Titre test (if required) | £120-180 |
| Import licence | SGD 16-26 |
| Health certificate + APHA endorsement | £200-350 |
| Airline cargo | £300-900+ |
| 30-day approved facility stay | SGD 800-2,500+ |
| Agent fee | £200-500 |
| **Total** | **£1,500-3,500+** |

---

*Sources: Singapore AVS import conditions. Data current as of {TODAY}.*
""",
     [
         ("Does my pet need quarantine to enter Singapore?", "Not traditional quarantine, but a mandatory 30-day stay at an AVS-approved animal boarding facility is required for all imported cats and dogs, even from low-risk Category 1 countries. You can visit your pet during this period. Costs are paid by the owner."),
         ("How do I know which AVS category my country is in?", "Check the current AVS approved countries list on the Singapore National Parks Board website. Categories change periodically. If your country is not listed as Category 1 or 2, direct import is not permitted and your pet must first reside in an approved country."),
     ]
    ),

    ("how-to-move-a-cat-internationally",
     "How to Move a Cat Internationally: What's Different From Dogs",
     "Cats and dogs face the same core paperwork, but cats often have advantages — smaller crates, fewer breed bans, and shorter quarantine in some countries. Here's what to know.",
     ["cats", "planning", "guide"],
     "2026-03-17",
     """Most pet transport guides talk about dogs. Cats get lumped in as an afterthought — same rules, smaller crate. That's mostly true, but there are meaningful differences that can save cat owners significant time and money.

## Where Cats Have an Advantage

**Quarantine duration.** China typically requires 30 days quarantine for dogs but only 7 days for cats from approved countries. Taiwan's quarantine tiers also sometimes favour cats.

**Breed bans.** Breed-specific legislation applies only to dogs. No country bans cats by breed for import purposes (though some countries restrict keeping certain exotic cat species).

**Crate requirements.** IATA crate requirements for cats follow the same principles as dogs, but a cat travelling in a small crate meets airline size limits more easily. Most airlines with weight limits (8-10kg including carrier) can accommodate adult cats but struggle with medium and large dogs.

**Cabin travel.** More cats than dogs fit the cabin weight threshold of 8kg including carrier. A cat in a soft-sided carrier under the seat is a calmer, cheaper, and less stressful option than cargo when available.

## Where Cats Have a Disadvantage

**Microchip resistance.** Some cats tolerate microchipping poorly compared to dogs, and microchip migration (the chip moving from the implant site) is slightly more common in cats. Always verify the microchip reads correctly before the vet visit for any paperwork.

**Stress and hiding.** Cats are territorial and often more stressed by transport than dogs. A long journey in cargo — even in a compliant crate — is genuinely difficult for some cats. Discuss sedation options with your vet: most vets advise against it at altitude, but acepromazine and similar drugs are sometimes used for the pre-flight drive to the airport.

**Titre tests are not waived.** Countries requiring titre tests require them for cats too. The same timing rules apply.

## Crate Requirements for Cats

The same IATA Live Animal Regulations apply:
- Rigid crate, ventilated on three sides minimum
- Tall enough for the cat to stand with head clearance
- Wide enough to turn around
- Water attachment on the outside, food attachment available
- Absorbent bedding
- Your contact details and directional arrows on the exterior

Soft-sided carriers are acceptable for cabin travel on airlines that permit them. They are not accepted for cargo.

## Health Certificate Timing

Countries that specify a 10-day window on health certificates (Australia, Singapore, the UK) apply this equally to cats and dogs. Book the vet appointment at the last possible moment within the window to give yourself maximum schedule flexibility.

---

*Content reflects current IATA LAR standards and destination country requirements. Data current as of {TODAY}.*
""",
     [
         ("Do cats need the same documents as dogs for international travel?", "Yes — microchip, vaccinations, health certificate, and (where required) a titre test. The paperwork is identical. The main practical differences are in crate size, some countries' shorter quarantine for cats, and the higher likelihood of cabin travel being feasible for cats."),
         ("Can I sedate my cat for a long international flight?", "Most vets advise against sedation at altitude — sedatives affect breathing and balance, and an animal that cannot right itself in a moving crate is at risk. Discuss this specifically with your vet, who knows your cat's health. Natural calming products (Feliway, Zylkene) are generally preferred to chemical sedation for air travel."),
     ]
    ),

    ("pet-transport-costs-breakdown-2026",
     "What Does International Pet Transport Actually Cost in 2026?",
     "A full cost breakdown for 8 common international pet routes. Airline fees, vet costs, quarantine, agents — no vague 'it depends' answers.",
     ["costs", "planning", "guide"],
     "2026-03-20",
     """Every article about pet transport costs eventually says "it depends on your pet's size, destination, and requirements." That is true, but it's not helpful. Here are real cost breakdowns for eight common routes, using 2026 prices where possible.

All costs are estimates. Get quotes from agents and airlines for your specific situation.

## How Pet Transport Costs Break Down

Before the route tables, here are the cost categories:

**Documentation costs:** Vet examinations, health certificates, government endorsements, titre tests, import permits. These are largely fixed regardless of your pet's size.

**Airline costs:** Cargo fees are calculated by weight (actual or volumetric, whichever is higher). A small dog in a small crate might travel cargo for £200-400. A large dog in a 120x80x90cm crate might cost £1,000-2,000+ on the same route.

**Quarantine costs:** Only apply to destinations requiring quarantine. Fixed per-day rates, not per-pet-size.

**Agent fees:** Optional but valuable. A good agent catches mistakes before they happen. Fees range from £200-1,000+ depending on complexity.

## Route Cost Tables

### UK to Australia (medium dog, ~25kg in crate)

| Item | Cost |
|------|------|
| Titre test (APHA) | £150 |
| Vet health certificate | £180 |
| APHA endorsement | £70 |
| Import permit (DAFF) | AUD 70 (~£35) |
| Airline cargo (UK-Melbourne) | £900 |
| Mickleham quarantine (10 days) | AUD 2,800 (~£1,400) |
| Agent | £500 |
| **Total** | **~£3,235** |

### UK to USA (medium dog)

| Item | Cost |
|------|------|
| Health certificate | £120 |
| APHA endorsement | £70 |
| Airline cargo (transatlantic) | £500 |
| Agent (optional) | £250 |
| **Total** | **~£940** |

No quarantine, no titre test (UK pets to USA).

### UK to Germany / France / EU (any pet)

| Item | Cost |
|------|------|
| EU pet passport (if UK-issued — no longer valid for EU) | - |
| Health certificate + APHIS-style endorsement | £120-200 |
| Airline (small dog cabin or cargo) | £100-400 |
| **Total** | **~£300-600** |

Note: Post-Brexit, UK pet passports are not accepted in the EU. A new health certificate is required.

### UK to Singapore (cat, 4kg with carrier)

| Item | Cost |
|------|------|
| Titre test | £150 |
| Import licence (AVS) | SGD 20 (~£12) |
| Health certificate + endorsement | £200 |
| Airline cabin fee | £80 |
| 30-day approved facility | SGD 1,200 (~£720) |
| Agent | £300 |
| **Total** | **~£1,462** |

### USA to Australia (large dog, ~40kg in crate)

| Item | Cost |
|------|------|
| Titre test (KSU lab) | USD 90 (~£70) |
| USDA-accredited vet + health cert | USD 300 |
| USDA endorsement | USD 38 |
| Import permit (DAFF) | AUD 70 |
| Airline cargo (US-Australia) | USD 1,800 (~£1,400) |
| Quarantine (14 days, large dog) | AUD 4,200 (~£2,100) |
| Agent | USD 800 (~£620) |
| **Total** | **~£4,600** |

### Ireland to Australia (medium dog)

Broadly the same as UK to Australia. Ireland is in the EU, so documentation follows EU routes. Titre test timing and quarantine requirements are identical to the UK route.

### Germany to Singapore (small dog, cabin)

| Item | Cost |
|------|------|
| EU health certificate | €150 |
| Import licence (AVS) | SGD 20 |
| Airline cabin fee | €70 |
| 30-day approved facility | SGD 1,000 |
| **Total** | **~€850 + SGD 1,020** (~£1,100) |

### Australia to UK (medium dog)

The UK's requirements focus on the titre test and correct documentation. Australia is on the UK's approved country list.

| Item | Cost |
|------|------|
| Titre test (Australian approved lab) | AUD 200 (~£100) |
| Vet health certificate | AUD 300 (~£150) |
| Export permit (Australia) | AUD 120 |
| Airline cargo (AU-UK) | AUD 1,800 (~£900) |
| Agent | £400 |
| **Total** | **~£1,550** |

No UK quarantine for pets from Australia (approved country), provided titre test and documentation are correct.

---

*Prices correct as of early 2026. Currency conversions approximate. Always obtain quotes from airlines and agents for your specific situation.*
""",
     [
         ("What is the cheapest international pet transport route?", "Short European routes (e.g. UK to France, Germany to Netherlands) are cheapest — often £150-400 total if the pet travels in the cabin. Transatlantic routes without quarantine (UK or EU to USA/Canada) typically cost £600-1,500. Long-haul routes to Australia, Japan, or Singapore are the most expensive, often £2,000-6,000+ due to quarantine or mandatory facility stays."),
         ("Does pet size affect transport cost?", "Yes, significantly. Airline cargo fees are charged by actual or volumetric weight, whichever is higher. A 5kg cat in a small crate might cost a fraction of what a 40kg dog in a large crate costs. Quarantine costs are usually per-day per-animal regardless of size, but some facilities charge more for larger kennels."),
     ]
    ),

    ("pet-microchipping-for-international-travel",
     "Pet Microchipping for International Travel: ISO Standards, Timing, and Common Problems",
     "The microchip must go in before the rabies vaccination. That single rule catches out thousands of pet owners every year. Here's everything you need to know.",
     ["microchip", "planning", "documentation"],
     "2026-03-24",
     """A pet microchip is a grain-of-rice-sized transponder implanted under the skin, usually between the shoulder blades. It carries a unique 15-digit number that identifies your animal for life. For international travel, the microchip is the cornerstone of the entire documentation chain.

Get the microchip wrong and everything else is invalid.

## The One Rule That Overrides Everything Else

**The microchip must be implanted before any rabies vaccination that counts toward your international travel documentation.**

If your vet vaccinates first and chips second — even on the same day — that vaccination is not valid for import purposes. The destination country cannot verify that the vaccinated animal and the chipped animal are the same. You must start the vaccination sequence again.

This is not a technicality. Australian DAFF, Japan MAFF, the UK APHA, and every other major regulatory body enforce this rule. Appeals are almost never successful.

## ISO Standard: Which Microchips Are Accepted

The international standard is **ISO 11784/11785** (15-digit FDXA format). All microchips implanted in the UK, EU, and most countries since the early 2000s should comply.

Non-ISO microchips (common in the US before ISO adoption) are the grey area. The US uses both ISO-compliant and non-ISO chips. If your pet was chipped in the US before ISO standardisation:

- Check whether your chip is 10-digit (non-ISO) or 15-digit (ISO)
- If non-ISO, your vet can scan for the older frequency
- Some countries will accept non-ISO chips provided you bring your own scanner
- The safest solution is to implant a new ISO-compliant chip

## Microchip Position and Migration

Chips are typically implanted between the shoulder blades. Over time, they can migrate — moving down the neck, into the shoulder, or occasionally further. Always ask your vet to scan your pet before any document-generating appointment to confirm:

1. The chip is still readable
2. The number on the reader matches the number on all documents
3. The chip is in a location the destination country's vet can locate

A chip that reads differently from the documents — even by one digit — invalidates the entire documentation chain.

## What the Health Certificate Says

Every international health certificate records the microchip number. The certifying vet must physically scan your pet and record the number they read. If there is a discrepancy between the chip number and any vaccination record, titre test, or import permit, the documentation will be rejected at the border.

## Practical Steps Before Any International Vet Appointment

1. Ask your vet to scan the microchip at the start of every appointment
2. Note the exact number read (photograph the scanner screen)
3. Cross-reference against all existing documents
4. Raise any discrepancy before the appointment proceeds

---

*Sources: IATA Live Animal Regulations, ISO 11784/11785 standards, destination country veterinary import requirements. Data current as of {TODAY}.*
""",
     [
         ("What happens if my pet's microchip was implanted after the rabies vaccination?", "The vaccination is not valid for international travel documentation purposes. You will need to re-vaccinate your pet after microchipping and restart any waiting periods that depend on vaccination date — including titre test timing and the 180-day countdown for Australia."),
         ("My pet has a non-ISO microchip from the US. What should I do?", "Check whether your destination country accepts non-ISO chips — some do, provided you bring a compatible scanner. The safest option is to implant a new ISO 15-digit chip alongside the existing one. Your vet can do this, and both numbers can be noted on documentation. Discuss with your agent or destination country authority before travel."),
     ]
    ),

    ("pet-health-certificate-timing-guide",
     "Pet Health Certificates: Timing Rules That Catch People Out",
     "Most countries require a health certificate issued within 10 days of travel. Miss that window and your pet cannot fly. Here's how to plan the final vet visit correctly.",
     ["documentation", "planning", "health-certificate"],
     "2026-03-27",
     """The health certificate is the document your vet issues to confirm your pet is healthy and meets the destination country's requirements. It is one of the last steps in the pre-travel process — and one of the easiest to get wrong.

## The 10-Day Window

Most countries — including the USA, Australia, Singapore, the UK, and EU member states — require a health certificate issued within **10 days of your pet's departure date**.

Ten calendar days. Not 10 business days. Not two weeks. Ten days.

This means:
- If your flight is on a Friday, your vet appointment must be no earlier than the previous Tuesday
- If the appointment is on Wednesday and the flight is pushed back two weeks, the certificate is invalid and you need a new one

## Booking the Vet Appointment

The golden rule: **book the vet appointment as late as possible within the window.**

Book it too early and you risk the certificate expiring if your flight is delayed. Book it the day before and you are fine — as long as your pet passes the examination and no issues arise.

Practically, most people aim for Day 7-8 of the 10-day window: late enough to be safe, early enough to allow time to fix anything unexpected.

## What the Vet Checks

The certifying vet physically examines your pet and confirms:

- Microchip present and readable (number recorded)
- Pet appears healthy and fit for air travel
- All required vaccinations are current (dates and lot numbers recorded)
- Titre test results are within validity period (if applicable)
- Treatments (tapeworm, tick) administered within the required window (if applicable)
- Pet meets the description on the import permit (if applicable)

The vet must be licensed to issue international health certificates. In the UK, this means being listed with APHA. In the US, vets must be USDA-accredited.

## Government Endorsement

Most destinations require the health certificate to be endorsed by a government veterinary authority before it is valid for import. In the UK, this is APHA. In the US, it is the USDA APHIS Veterinary Services.

**APHA endorsement timing (UK):** APHA processes endorsements within 2-4 working days by post, or same-day at some APHA offices. Always check current processing times and book accordingly.

**USDA endorsement timing (US):** USDA accredited vets can complete USDA Form 7001 (the standard export health certificate), and most regional USDA Veterinary Services offices endorse within 1-3 business days.

With a 10-day window and government processing time of 2-4 days, your timeline is:
- Day 1-2: Vet appointment
- Day 2-5: Certificate sent for endorsement
- Day 5-7: Endorsed certificate returned
- Day 8-10: Travel day

This leaves very little margin. Any delay in endorsement and you are rebooking the vet appointment.

## Australia's 7-Day Rule

Australia uses a **7-day window**, not 10. The health certificate must be issued and endorsed within 7 days of departure. This compresses the timeline significantly. If you are using postal APHA endorsement for Australia, you may need to use a same-day or next-day APHA office.

## Replacement Certificates

If your flight is delayed and your certificate expires, you will need a new one. Your vet can usually issue a replacement quickly, but government endorsement takes time. Have a contingency plan.

---

*Sources: APHA UK, USDA APHIS, Australian DAFF BICON, Singapore AVS. Data current as of {TODAY}.*
""",
     [
         ("How many days before travel does the health certificate need to be issued?", "Most countries require a certificate issued within 10 days of departure. Australia's window is 7 days. The USA generally accepts 10 days. Always check the specific destination country requirement — rules change."),
         ("What if my vet is not authorised to issue international health certificates?", "In the UK, vets must be registered with APHA to issue international export health certificates (EHCs). Not all vets are registered. Ask your vet directly, or use the APHA approved vet finder on the government website. In the US, vets must be USDA-accredited."),
     ]
    ),

    ("travelling-with-dogs-on-long-haul-flights",
     "Travelling With Dogs on Long-Haul Flights: Cargo, Comfort, and What Airlines Don't Tell You",
     "Long-haul cargo travel is hard on dogs. Here's how to minimise stress, pick the right crate, choose the right airline, and prepare your dog for 12+ hours in the hold.",
     ["dogs", "airlines", "welfare", "cargo"],
     "2026-03-31",
     """No dog finds air travel pleasant. The combination of unfamiliar smells, engine vibration, pressure changes, and complete isolation from their owner is genuinely stressful for most animals. A 2-hour European flight is manageable. A 24-hour journey to Australia, with a connection, is a different category of experience.

That does not mean you should not do it — millions of dogs travel internationally every year and arrive healthy. But the preparation matters enormously.

## Choosing the Right Airline

Not all cargo holds are the same. Relevant factors for dog welfare:

**Temperature control:** IATA requires cargo holds to be temperature-controlled between 7°C and 29°C during flight. Most modern widebody aircraft (Boeing 777, Airbus A380, A350) maintain stable temperatures. Narrow-body regional aircraft are less reliable.

**Loading and handling:** Your dog will be loaded, offloaded, and possibly transferred between flights by baggage handlers. Some handlers are experienced and calm with animals; others treat live animal crates like luggage. Routing via a single connection with a reputable airline reduces handling events.

**Connection time:** A 2-hour connection is stressful. A 6-hour connection is worse — your dog sits in a cargo warehouse. Aim for connections of 2-4 hours: enough time to make the connection comfortably, not so long that your dog sits in a warehouse indefinitely.

**Breed embargoes:** Airlines like Lufthansa, British Airways, and others have banned brachycephalic breeds from cargo year-round. If your dog has a flat face, your airline options are limited. Verify the current policy directly with the airline before booking anything.

## Crate Preparation

The crate your dog travels in is their entire world for the duration of the journey. It should:

- Be the right size: your dog should be able to stand, turn around, and lie down fully stretched
- Be familiar: introduce the crate weeks before travel, feed meals in it, leave it open in the living area
- Contain familiar bedding (not loose — must be absorbent)
- Have a water dispenser attached to the door (fill partially so ice forms — melts during transit)
- Have your contact details on every panel (in the destination country's language if possible)
- Be labelled with directional arrows, LIVE ANIMAL stickers, and feeding/watering instructions

Do not send toys that could be swallowed. Do not send food unless specifically required.

## Pre-Flight Feeding

Feed your dog a light meal 4-6 hours before the flight — not immediately before. A full stomach plus stress plus altitude equals vomiting in the crate. Not dangerous, but miserable and potentially indicative of underlying stress.

Water on the morning of travel is fine. Hydration matters for long journeys.

## On Arrival

Your dog has been in a crate for many hours. On arrival:

- Let them out slowly in a contained area — they may be disoriented
- Offer water immediately
- A short, calm walk before getting in the car
- Watch for signs of stress: panting, trembling, reluctance to eat. Most dogs recover within 24 hours.

---

*Sources: IATA Live Animal Regulations (LAR), airline published cargo policies. Data current as of {TODAY}.*
""",
     [
         ("Can I sedate my dog for a long-haul flight?", "Most vets advise against sedation for dogs flying in cargo. Sedatives affect balance and respiratory function, and a dog that cannot right itself in a moving crate is at risk of injury. The American Veterinary Medical Association has stated that sedation increases health risks for pets travelling by air. Discuss with your vet; some may consider mild natural calming supplements (Adaptil, Zylkene) as an alternative."),
         ("Which airlines are best for transporting dogs long-haul?", "Airlines with dedicated pet programs and proper temperature-controlled holds include Lufthansa (via Lufthansa Cargo), KLM, Air France, and Emirates SkyCargo. For routes to Australia and New Zealand, Qantas and Air New Zealand both have established pet cargo programs. Always verify current policies directly — breed embargoes and seasonal rules change."),
     ]
    ),

    ("pet-transport-agents-what-they-do-and-when-you-need-one",
     "Pet Transport Agents: What They Do, What They Cost, and When You Actually Need One",
     "For simple routes you probably don't need an agent. For Australia, Japan, or New Zealand you almost certainly do. Here's how to decide and what to look for.",
     ["agents", "planning", "costs"],
     "2026-04-03",
     """A pet transport agent handles some or all of the logistics of moving your pet internationally. They know the current regulations, have relationships with airlines, know which vets issue clean paperwork, and can catch mistakes before they become expensive problems.

You do not always need one. But for complex routes, they pay for themselves.

## What an Agent Actually Does

A full-service agent typically handles:

- Confirming current import requirements for your specific route (regulations change)
- Advising on the correct sequence and timing of vet visits, tests, and documents
- Booking airline cargo space
- Completing and checking all documentation before submission
- Liaising with government endorsement agencies
- Arranging crate purchase and labelling
- Coordinating pickup/delivery to the airport
- Handling the quarantine booking at the destination (for Australia, Japan, etc.)
- Being available by phone if something goes wrong

A documentation-only agent does the paperwork but not the logistics. You handle crate, airline booking, and airport yourself.

## When You Need a Full-Service Agent

**Australia:** Almost every experienced agent recommends professional help for Australia. The 180-day titre test rule, the DAFF permit, the Mickleham booking, and the strict documentation chain leave very little margin for self-managed error.

**Japan:** The 180-day timing rule from the blood draw date — not the result date — is the kind of detail that catches experienced owners out. A wrong date on one document triggers a 180-day quarantine.

**Any route involving quarantine:** Where quarantine is mandatory, the cost of a documentation error far exceeds the cost of an agent.

**Multiple-pet households:** Managing paperwork for three cats and a dog, all with different vaccination histories, across a complex route is a significant administrative task. Agents handle this efficiently.

## When You Probably Don't Need an Agent

- **EU to EU travel** with a pet passport (straightforward)
- **UK to USA/Canada** (documentation is moderate, no quarantine)
- **Short European routes** (UK to France, Germany to Netherlands)
- **Experienced travellers** who have done the route before

## What to Look For in an Agent

- **IPATA membership** (International Pet and Animal Transportation Association) — the main industry body
- **Experience on your specific route** — ask how many times they have handled UK-to-Australia, or wherever you are going
- **Clear written quote** — what is included and what is not
- **References** — ask for reviews from people who did your route
- **Regulatory knowledge** — they should cite specific regulations, not vague reassurances
- **Response time** — you are trusting this person with your pet. They should be reachable.

## What Agents Charge

Documentation-only agents: £150-400 for simple routes, £400-800 for complex ones.

Full-service agents: £400-1,200+ for complex long-haul routes. Some charge a flat fee; others charge a percentage of total costs.

On a £5,000 Australia relocation, an agent fee of £600 is 12% of total cost. On a route where a single mistake adds £2,000 in quarantine, it is cheap insurance.

---

*Data current as of {TODAY}.*
""",
     [
         ("Are pet transport agents regulated?", "In the UK and most countries, pet transport agents are not specifically regulated as a profession. The main voluntary accreditation is IPATA (International Pet and Animal Transportation Association) membership. Members agree to a code of conduct. Look for IPATA membership as a baseline indicator of professionalism, then verify with references and route-specific experience."),
         ("Can I move my pet internationally without an agent?", "Yes, for many routes. EU pet travel, UK to USA, and other well-documented routes are managed by many owners independently. For Australia, Japan, New Zealand, and Singapore, the complexity and cost of errors makes professional guidance strongly advisable. The Australian DAFF website provides full documentation guidance for self-managed moves."),
     ]
    ),

    # ── AIRLINE GUIDES ───────────────────────────────────────────────────────────

    ("lufthansa-pet-transport-guide",
     "Lufthansa Pet Transport: Cabin Rules, Cargo Fees, and Breed Restrictions",
     "Lufthansa is one of Europe's most popular airlines for pet transport. Here's what cabin and cargo travel cost, which breeds are banned, and how to book.",
     ["airlines", "lufthansa", "europe"],
     "2026-04-07",
     """Lufthansa allows small pets in the cabin on most routes and accepts larger pets as checked baggage or cargo. It is one of the more pet-friendly European carriers, but has firm restrictions on brachycephalic breeds in cargo.

## Cabin Travel

**Eligibility:** Small dogs and cats up to **8kg including carrier**. The carrier must fit under the seat in front of you (typically 55x40x23cm — verify current dimensions before purchase).

**Fee:** Approximately €50-65 per sector within Europe. Intercontinental cabin fees are higher.

**Number allowed:** One pet per passenger, maximum two pets in the cabin per flight.

**Booking:** Must be booked in advance by calling Lufthansa reservations or using the manage booking function. Cannot be added at check-in.

## Cargo (Lufthansa Cargo / PetLounge)

Lufthansa operates a dedicated **PetLounge** service at Frankfurt Airport — one of the most comprehensive pet handling facilities in Europe. It includes temperature-controlled holding areas, veterinary check stations, and experienced animal handlers.

Larger dogs and pets over the cabin weight limit travel in the hold as accompanied excess baggage or as unaccompanied cargo through Lufthansa Cargo.

**Fees:** Calculated on actual or volumetric weight, whichever is higher. A medium dog in a 70x50x50cm crate might cost €200-500 within Europe; long-haul routes cost significantly more.

## Brachycephalic Breed Restrictions

Lufthansa imposes a **year-round cargo embargo** on the following dog breeds:
- All brachycephalic (flat-faced) dog and cat breeds including Bulldogs, French Bulldogs, Pugs, Boston Terriers, Boxers, Shih Tzus, and similar

These breeds may travel in the cabin if they meet the weight limit. They cannot travel as cargo or checked baggage.

**Short-nosed cats** (Persian, Himalayan, Exotic Shorthair, British Shorthair) are also restricted from cargo.

## Documentation Requirements

For all flights, Lufthansa requires:
- Current vaccination records
- Health certificate issued by a licensed vet within 10 days of travel
- For international routes: all destination country import documentation

Lufthansa staff check documentation at check-in. Missing or incorrect documents result in the pet not travelling.

---

*Sources: Lufthansa published pet travel policies. Policies change — always verify directly with Lufthansa before booking. Data current as of {TODAY}.*
""",
     [
         ("How much does it cost to bring a dog on Lufthansa?", "Cabin travel (up to 8kg with carrier) costs approximately €50-65 per sector within Europe. Cargo fees depend on crate weight and dimensions — expect €200-500+ within Europe for a medium dog, significantly more for intercontinental routes. Always get a quote from Lufthansa Cargo directly."),
         ("Does Lufthansa allow French Bulldogs in cargo?", "No. Lufthansa has a year-round cargo ban on all brachycephalic breeds including French Bulldogs. A French Bulldog under 8kg with carrier may travel in the cabin. Above that weight, Lufthansa is not an option for cargo transport of brachycephalic breeds."),
     ]
    ),

    ("emirates-pet-transport-guide",
     "Emirates Pet Transport: No Cabin Pets, Cargo Options, and Dubai Connections",
     "Emirates does not allow pets in the cabin. All pets travel as cargo via Emirates SkyCargo. Here's how it works, what it costs, and the Dubai transit consideration.",
     ["airlines", "emirates", "middle-east"],
     "2026-04-10",
     """Emirates is one of the world's busiest airlines for long-haul routes, but it has one of the strictest pet policies among major carriers: **no pets in the cabin, on any route, without exception**.

If you need to fly your pet on an Emirates route, the only option is Emirates SkyCargo.

## Emirates SkyCargo: How It Works

Emirates SkyCargo operates through dedicated facilities at Dubai International Airport (DXB). The process:

1. **Booking:** Through Emirates SkyCargo directly or via an IPATA-registered agent. Cannot be booked through the passenger booking system.
2. **Documentation:** All destination country import documentation must be provided at the time of booking.
3. **Drop-off:** Pets are delivered to the Emirates SkyCargo facility, not the passenger terminal.
4. **Dubai connection:** Many Emirates routes connect through Dubai. Pets in transit through Dubai are held in climate-controlled facilities at DXB's dedicated animal lounge.

## Dubai Transit: What to Know

Dubai's Animal Care Centre at DXB can hold pets in transit for up to 48 hours. The facility is climate-controlled with experienced staff. However:

- **UAE import permits are required for stays over 4 hours**, even for transit. This is a significant administrative step if you are connecting through Dubai — verify the current UAE transit requirements before booking.
- Summer temperatures in Dubai (June-September) are extreme. DXB is fully air-conditioned, but ground crew handling between aircraft and terminals are working in heat. Emirates imposes summer embargoes on certain breeds during extreme heat.

## Breed Restrictions

Emirates SkyCargo restricts or prohibits:

- All brachycephalic dog and cat breeds (year-round or seasonal depending on route)
- Some dangerous dog breeds per UAE regulations (Pit Bull Terriers, Rottweilers, and others are banned from import into the UAE)

If your destination is the UAE itself, check both Emirates cargo restrictions and UAE import regulations for restricted breeds.

## Cost

Emirates SkyCargo pricing is based on actual or volumetric weight. Long-haul routes (e.g. UK to Australia via Dubai) for a large dog can cost £1,200-2,500+ for the cargo segment alone. Get a formal quote from Emirates SkyCargo or your agent.

---

*Sources: Emirates SkyCargo published policies, UAE MOCCAE import requirements. Data current as of {TODAY}.*
""",
     [
         ("Can I bring my pet in the cabin on Emirates?", "No. Emirates does not allow pets in the cabin on any route. All pets must travel as cargo via Emirates SkyCargo. This applies to all pets regardless of size."),
         ("How long can my pet stay in transit at Dubai Airport?", "Emirates SkyCargo can hold pets in transit for up to 48 hours at Dubai's animal care facilities. However, UAE import documentation may be required for stays over 4 hours even in transit — verify current UAE transit requirements before booking a Dubai connection."),
     ]
    ),

    ("qatar-airways-pet-transport-guide",
     "Qatar Airways Pet Transport: Cargo Rules, Breed Bans, and Doha Connections",
     "Qatar Airways carries pets as cargo only via QR Cargo. Here's how to book, which breeds are banned, and what Doha transit means for your pet.",
     ["airlines", "qatar-airways", "middle-east"],
     "2026-04-13",
     """Qatar Airways operates one of the world's most extensive route networks, making it a frequent choice for pet owners on routes through the Middle East. Like Emirates, there are **no pets in the cabin** on Qatar Airways — all animals travel as cargo via QR Cargo.

## Booking via QR Cargo

Qatar Airways Cargo (QR Cargo) handles all live animal shipments. Book through:

- QR Cargo directly at qrcargo.com
- An IPATA-registered pet transport agent (recommended for complex routes)

The booking must be made in advance — QR Cargo imposes maximum quantities of live animals per flight, and popular routes fill up.

## Doha (DOH) Connections

Many QR routes connect through Hamad International Airport in Doha. The airport has a purpose-built animal holding facility with climate control. Qatar's climate (June-September temperatures regularly exceeding 40°C) means:

- Summer embargoes apply to brachycephalic breeds on certain routes
- All pets in Doha transit are held in the climate-controlled cargo facility, not the terminal
- Transit time at Doha should be 3-5 hours minimum to allow for handling and documentation — very tight connections risk missing the onward flight

## Breed Restrictions

QR Cargo prohibits or restricts:

- All brachycephalic dog and cat breeds (year-round on some routes; seasonal embargo during Gulf summer on others)
- Breeds banned under Qatar's national regulations
- Some dog breeds banned from destination countries (enforced at the time of booking documentation check)

## Documentation

For all live animal shipments, QR Cargo requires:

- IATA-compliant crate with correct labelling
- Health certificate issued within 10 days of travel
- All destination country import documentation
- Live Animal Checklist (IATA)

Documentation must be presented at the cargo facility, not the passenger terminal.

---

*Sources: Qatar Airways Cargo published live animal policies. Data current as of {TODAY}.*
""",
     [
         ("Does Qatar Airways allow pets in the cabin?", "No. Qatar Airways does not allow pets in the cabin on any route. All pets travel via QR Cargo as freight shipments. The only exception is guide dogs and registered assistance animals, which travel in the cabin with the handler."),
         ("Is Doha a safe transit point for pets in summer?", "Doha's summer temperatures are extreme (40°C+), but the cargo animal facility at Hamad International Airport is fully climate-controlled. The risk period is ground handling between the aircraft and the facility. Qatar Airways imposes seasonal embargoes on brachycephalic breeds to mitigate this risk. For non-restricted breeds, summer transit through Doha is routinely handled."),
     ]
    ),

    ("air-france-klm-pet-transport-guide",
     "Air France KLM Pet Transport: Cabin Allowances, Cargo Fees, and What's Different Between the Two",
     "Air France and KLM both allow small pets in the cabin and carry larger pets as cargo. The policies are similar but not identical. Here's what to know for each.",
     ["airlines", "air-france", "klm", "europe"],
     "2026-04-15",
     """Air France and KLM are sister airlines under the Air France-KLM group, but they operate independently and their pet policies have minor differences. Both are solid choices for pet transport within Europe and on many intercontinental routes.

## Cabin Travel

**Air France:** Small pets up to **8kg including carrier**. Soft-sided carriers only in the cabin. Fee: approximately €50 within Europe, €200+ long-haul.

**KLM:** Small pets up to **8kg including carrier**. Hard and soft carriers accepted if they fit under the seat. Fee: approximately €50 within Europe (Pet in Cabin option must be selected during booking).

Both airlines: one pet per passenger, maximum two pets in the cabin per flight.

## Cargo (Excess Baggage / Cargo)

Both carriers offer pet transport as checked excess baggage (accompanied) and via their cargo divisions.

- **Air France Cargo** handles unaccompanied pets through its IATA-certified live animal program
- **KLM Cargo** operates similarly

For large dogs (over cabin weight) travelling internationally, cargo is the standard route. Fees vary by route and crate weight.

## Brachycephalic Policies

Both Air France and KLM restrict brachycephalic breeds from cargo transport:

- Brachycephalic dogs and cats cannot travel in the hold as checked baggage or cargo on most routes
- They may travel in the cabin if they meet the weight limit
- Some routes have additional restrictions — verify at time of booking

## Paris CDG and Amsterdam AMS as Hubs

Both airports have well-developed animal handling facilities. CDG has a dedicated animal lounge for transiting pets in cargo. AMS similarly handles transit animals within Schiphol's cargo complex.

## Key Difference: Long-Haul Cabin Allowances

Air France allows pets in the cabin on some long-haul routes (including selected transatlantic flights). KLM typically restricts cabin pets to European routes. Check specific routes when booking — this distinction matters for pets travelling to North America.

---

*Sources: Air France and KLM published pet travel policies. Data current as of {TODAY}.*
""",
     [
         ("Can I bring a dog in the cabin on Air France to the US?", "On some transatlantic Air France routes, small pets (up to 8kg with carrier) are permitted in the cabin. This is not universal across all routes — verify at the time of booking. KLM generally restricts cabin pets to European routes and does not allow them on transatlantic services."),
     ]
    ),

    # ── ROUTE-SPECIFIC TIPS ──────────────────────────────────────────────────────

    ("uk-to-dubai-uae-pet-transport-guide",
     "UK to Dubai (UAE) Pet Transport: What You Actually Need",
     "Moving a pet from the UK to Dubai requires a UAE import permit from MOCCAE and compliance with breed bans. Here's the full checklist.",
     ["uae", "dubai", "uk", "planning"],
     "2026-04-17",
     """Dubai is one of the most popular expat destinations in the world, and thousands of families move their pets there every year. The UAE's import process is more straightforward than Australia or Japan — but there are genuine pitfalls, particularly around breed bans and permit timing.

## The UAE MOCCAE Import Permit

All dogs and cats must have an **import permit from MOCCAE** (Ministry of Climate Change and Environment) before arrival. The permit is issued electronically and must be obtained before your pet travels.

Apply through the MOCCAE e-services portal. Processing takes 3-5 working days under normal circumstances. Apply at least 2-3 weeks before travel.

The permit specifies:
- Pet's microchip number
- Breed, species, age, and sex
- Owner details
- Port of entry

## Microchip and Vaccinations

- **ISO 15-digit microchip** required
- **Rabies vaccination:** current, administered after microchipping
- **Other vaccines:** Distemper, Hepatitis, Parvovirus (DHPP for dogs); Feline calici, herpesvirus, panleukopenia (FVRCP for cats)
- No titre test required for pets travelling from the UK

## Health Certificate

Issued by a UK APHA-approved vet, endorsed by APHA, within **10 days of departure**. The health certificate must reference the import permit number.

## Breed Bans — Read Before Proceeding

The UAE (and specifically Dubai) bans certain breeds from import entirely. Banned dogs include:

- Pit Bull Terrier / American Pit Bull
- American Staffordshire Terrier
- Rottweiler (some emirates — Dubai has additional restrictions)
- Tosa Inu
- Dogo Argentino
- Fila Brasileiro
- Wolfdog / Czech Wolfdog
- And others

If your dog is one of these breeds — or visually resembles one — contact MOCCAE before applying for a permit. Some breeds that are not formally banned are refused at the owner's discretion of the customs officer based on visual assessment.

## Arriving in Dubai

Pets arrive through Dubai International Airport (DXB) cargo terminal. You must arrange collection with a UAE-based customs agent unless your transport agent handles this.

After customs clearance, pets must be inspected by a MOCCAE-approved vet within 48 hours of arrival and registered with the local authority.

---

*Sources: MOCCAE UAE animal import regulations. Data current as of {TODAY}.*
""",
     [
         ("Do I need a titre test to bring my dog from the UK to Dubai?", "No. The UK is not on the UAE's list of countries requiring a titre test. A current rabies vaccination, health certificate, and UAE import permit are the core requirements. Always verify current requirements with MOCCAE before travel."),
         ("Is my dog breed allowed into the UAE?", "The UAE bans several breeds including Pit Bull Terriers, Rottweilers (Dubai), Tosa Inu, Dogo Argentino, and Fila Brasileiro. If your dog is a mixed breed that visually resembles a banned type, there is a risk of refusal at customs. Contact MOCCAE before applying for a permit if you have any concern about your breed."),
     ]
    ),

    ("germany-to-australia-pet-transport-guide",
     "Germany to Australia Pet Transport: EU Rules, DAFF Requirements, and How the Two Interact",
     "Germany to Australia involves EU export rules at one end and DAFF's strict quarantine system at the other. Here's how the two frameworks fit together.",
     ["australia", "germany", "europe", "planning"],
     "2026-04-19",
     """Germany to Australia is a long-haul route with requirements at both ends. The EU has its own health certificate format; Australia has its own import conditions. Getting both right simultaneously is where the complexity lies.

## The EU End: Export from Germany

Germany requires an **official veterinary health certificate** endorsed by the German veterinary authority (the relevant Veterinäramt, typically at the district level). This certificate confirms:

- ISO microchip present and readable
- Current vaccination status
- Pet is healthy and fit for transport

The German certificate must be issued within **10 days of departure** and be issued by an officially authorised vet.

## The Australia End: DAFF Import Conditions

Australia's DAFF requirements are independent of the EU framework. They require:

- Rabies titre test from an approved laboratory (blood drawn at least 30 days after vaccination; result must be ≥0.5 IU/mL; departure must be 180+ days after the result date)
- Import permit from DAFF (apply at least 4-6 months in advance)
- Health certificate using DAFF's prescribed format — this is a separate document from the German/EU export certificate
- Pre-approved Australian entry point (Melbourne, Mickleham quarantine)

In practice, you need **two health certificates**: one that satisfies German export requirements, and one (or the same one adapted to DAFF format) that satisfies Australian import requirements. Many agents use a combined certificate that meets both; others use separate documents. Confirm with your agent.

## German Approved Laboratories for Titre Testing

Germany has DAFF-approved laboratories for the rabies titre test. Ensure you use an approved lab — the DAFF website maintains the current list.

## Airlines from Germany to Australia

Main options routing through hubs:

- **Lufthansa** via Singapore, Bangkok, or Hong Kong (Frankfurt or Munich departure)
- **Singapore Airlines** via Singapore
- **Cathay Pacific** via Hong Kong
- **Emirates** via Dubai (no cabin pets; cargo only)
- **Qatar Airways** via Doha (cargo only)

For a dog, Lufthansa's PetLounge at Frankfurt provides the best handling for the first leg. Verify cargo acceptance for your specific routing.

---

*Sources: German Veterinäramt, Australian DAFF BICON. Data current as of {TODAY}.*
""",
     [
         ("Does my German-issued pet passport work for Australia?", "No. EU pet passports are not accepted for import into Australia. You need a formal health certificate that meets DAFF's specific requirements, issued by an authorised vet and meeting DAFF's format. This is separate from the EU pet passport system."),
     ]
    ),

    ("moving-pets-canada-complete-guide",
     "Moving Pets to Canada: CFIA Rules, Rabies Requirements, and Province-by-Province Notes",
     "Canada's pet import rules are managed by CFIA and are relatively straightforward from most countries. Here's everything you need to know before crossing the border.",
     ["canada", "planning", "guide"],
     "2026-04-21",
     """Canada is one of the easier countries to move a pet to from most English-speaking nations. The CFIA (Canadian Food Inspection Agency) manages pet imports, and the rules are relatively transparent.

## Core Requirements

**From the UK, US, or EU:**

- **Microchip:** Strongly recommended but not technically required for dogs from many countries. However, most airlines require it, and many provinces require it for licensing. Implant one.
- **Rabies vaccination:** Dogs over 3 months must have a current rabies vaccination. Must be administered by a licensed vet.
- **Health certificate:** Required for dogs. Issued by a licensed vet. CFIA does not require a specific format for most countries, but airline requirements usually mean a standardised certificate is issued.
- **Proof of rabies vaccination:** The vaccination certificate must accompany the animal.

Cats do not require a rabies vaccination for entry to Canada (though it is recommended and required by most provinces for licensing).

## Province-Specific Notes

Canada's animal welfare and licensing rules are primarily provincial:

- **Ontario, British Columbia, Alberta:** Require a valid rabies vaccination for dog licensing. No titre test required.
- **Quebec:** French-language requirements for some documents if the destination is Quebec City or rural Quebec — though border officials generally accept English documentation.
- **British Columbia:** Has strict rules on importing certain dog breeds from the US (where rabies is more prevalent).

## Breed Restrictions

Canada has no **federal** breed-specific legislation. However:

- **Ontario** banned Pit Bull Terriers in 2005 under the Dog Owners' Liability Act — this provincial ban means Pit Bulls cannot enter Ontario regardless of where they originated
- Other provinces have no such bans, though municipalities may have local restrictions

## Arriving by Air

Pets arriving by air at major Canadian airports (Toronto Pearson, Vancouver, Montreal) clear Canadian Border Services Agency (CBSA) at the terminal. Declare your pet on your customs form. An officer will inspect documents and may examine the animal.

For cargo arrivals, CBSA releases pets after document verification. Clear through the air cargo terminal.

---

*Sources: CFIA pet import requirements, CBSA border information. Data current as of {TODAY}.*
""",
     [
         ("Do dogs need a titre test to enter Canada?", "No, for most countries. Canada does not require a rabies titre test for dogs from the UK, US, or EU. A current rabies vaccination and health certificate are the standard requirements. However, for dogs from countries where rabies is endemic, additional requirements may apply."),
         ("Can I bring a Pit Bull to Canada?", "Canada has no federal Pit Bull ban. However, Ontario's provincial ban under the Dog Owners' Liability Act prohibits Pit Bull Terriers and pit bull-type dogs in Ontario. If your destination is any city in Ontario, a Pit Bull cannot legally enter the province. Other Canadian provinces do not have this restriction at the provincial level."),
     ]
    ),

    ("india-to-uk-pet-transport-guide",
     "India to UK Pet Transport: Titre Tests, DEFRA Requirements, and Finding Approved Labs",
     "Moving a pet from India to the UK requires a titre test, specific timing, and documentation from APHA. Here's the complete guide.",
     ["india", "uk", "planning", "titre-test"],
     "2026-04-23",
     """India is classified as a **non-listed country** by the UK government — meaning it is not on the list of approved rabies-free or low-risk countries. This triggers the full UK import process for pets, including a mandatory rabies titre test.

## The UK's Non-Listed Country Requirements

For pets entering the UK from non-listed countries (which includes India), APHA requires:

1. **ISO 15-digit microchip** implanted before vaccination
2. **Rabies vaccination** administered after microchipping
3. **Rabies titre test** performed at a UK-approved laboratory:
   - Blood drawn at least 30 days after vaccination
   - Result must be ≥0.5 IU/mL
   - Test must be performed at an approved lab (see below)
4. **Waiting period:** Your pet cannot travel to the UK until **3 months (90 days)** after a satisfactory titre test result
5. **Animal Health Certificate (AHC)** issued within 10 days of travel by an APHA-authorised vet (in India, this will be a vet authorised by the Indian government veterinary authority)
6. **Tapeworm treatment** for dogs within 24-120 hours before arrival

## Finding Approved Titre Test Labs in India

UK-approved laboratories for the rabies titre test include international reference labs. In India, samples are typically sent to:

- Sent to approved labs abroad (UK APHA Weybridge, or approved EU reference labs)
- Or tested at Indian labs that are UK-approved — check the current APHA approved laboratory list

Blood must be drawn by a licensed vet and the sample shipped under cold chain conditions. Confirm the cold chain requirements with your lab.

## The 90-Day Wait

The 90-day waiting period runs from the **date of a satisfactory result** at the approved lab. It does not start from the blood draw date. Once 90 days have passed, your pet can travel within a 10-day window from the date of the health certificate.

## Approved Airfreight Routes

Direct flights from major Indian cities (Mumbai, Delhi, Bangalore, Chennai) to the UK are operated by:

- **Air India** (cabin for small pets on some routes)
- **British Airways** cargo
- **Emirates** via Dubai (cargo only)
- **Qatar Airways** via Doha (cargo only)
- **Lufthansa** via Frankfurt

Check the current pet policies for each airline — cargo space must be booked in advance.

---

*Sources: UK APHA non-listed country pet import requirements. Data current as of {TODAY}.*
""",
     [
         ("How long does it take to move a pet from India to the UK?", "A minimum of 4-5 months. You need at least 30 days between vaccination and the titre test blood draw, then up to 14 days for lab results, then 90 days of waiting from the satisfactory result. Add time for the health certificate and travel arrangements."),
         ("Is a rabies titre test required to bring my dog from India to the UK?", "Yes. India is a non-listed country for UK pet imports. All pets from non-listed countries require a titre test with a result of at least 0.5 IU/mL, performed at a UK-approved laboratory, followed by a 90-day waiting period before UK entry is permitted."),
     ]
    ),

    ("south-africa-to-uk-pet-transport-guide",
     "South Africa to UK Pet Transport: APHA Requirements, Approved Labs, and Airline Options",
     "South Africa is classified as a non-listed country for UK pet imports. Here's the full titre test and documentation process for moving pets from SA to the UK.",
     ["south-africa", "uk", "planning"],
     "2026-04-24",
     """Like India, South Africa is a **non-listed country** for UK pet imports. The same titre test and 90-day waiting period apply. But South Africa has unique advantages: high veterinary standards, established approved labs, and direct flight options.

## Core Requirements (Same as All Non-Listed Countries)

1. ISO microchip (before vaccination)
2. Rabies vaccination (after microchip)
3. Titre test at an approved lab (30+ days post-vaccination; result ≥0.5 IU/mL)
4. 90-day wait from satisfactory result
5. Animal Health Certificate within 10 days of travel
6. Tapeworm treatment for dogs (24-120 hours before arrival)

## Approved Labs in South Africa

South Africa has strong veterinary diagnostic infrastructure. Check the current APHA approved lab list for South Africa — the OIE/WOAH reference lab network includes institutions in the region. Some samples may need to be couriered to European reference labs; discuss with your vet.

## Airline Options from South Africa to UK

Direct routes:

- **British Airways** (Johannesburg to London Heathrow) — BA allows pets in cargo on this route; check current policy
- **South African Airways** — has carried pets; verify current cargo program
- **Virgin Atlantic** — cargo options; no cabin pets
- **Emirates** — via Dubai (cargo only)

For large dogs, direct BA or SAA services are generally preferable to avoid a second handling event in Dubai.

## South Africa's Export Requirements

Before leaving South Africa, your pet needs a clearance certificate from the South African state veterinarian. Export permit requirements vary by province. Your vet or transport agent can arrange this.

---

*Sources: UK APHA non-listed country requirements, South African DAFF veterinary export documentation. Data current as of {TODAY}.*
""",
     [
         ("How long does the titre test take in South Africa?", "Blood draw to result typically takes 7-14 days depending on which approved laboratory is used. If the sample is shipped internationally to a reference lab, allow 2-3 weeks for results. The 90-day waiting period starts from the date of a satisfactory result."),
     ]
    ),

    # ── WELFARE AND PRACTICAL GUIDES ────────────────────────────────────────────

    ("brachycephalic-dogs-international-travel",
     "Brachycephalic Dogs and International Travel: Which Airlines Still Accept Them",
     "Airlines have been tightening brachycephalic breed policies for a decade. Here's which airlines still accept French Bulldogs and Pugs in cargo, and which have banned them entirely.",
     ["breeds", "airlines", "brachycephalic", "welfare"],
     "2026-04-25",
     """Brachycephalic dogs — flat-faced breeds including French Bulldogs, English Bulldogs, Pugs, and Boxers — have faced increasing airline restrictions over the past decade. Multiple high-profile incidents of brachycephalic dogs dying in cargo holds prompted most major carriers to tighten or remove their cargo policies for these breeds.

The situation in 2026 is this: **cargo transport for brachycephalic breeds is significantly restricted**, but some options remain.

## Why Brachycephalic Breeds Are Restricted

The physical structure of brachycephalic breeds — compressed skulls, narrowed nostrils, elongated soft palates — means their airways are mechanically compromised even at rest. Under stress, exertion, or in warm temperatures, their oxygen intake can become critically insufficient.

In a cargo hold at altitude, with temperature fluctuations, engine vibration, and no owner present, a brachycephalic dog in respiratory distress cannot signal for help. Airlines have responded to fatality data by withdrawing cargo acceptance.

## Which Airlines Have a Complete Cargo Ban (2026)

The following airlines have banned all brachycephalic breeds from cargo (year-round, all routes) as of 2026:

- **Lufthansa**
- **British Airways**
- **Air France**
- **KLM**
- **Swiss International Air Lines**
- **Austrian Airlines**

Policies change — verify directly with each airline before booking.

## Which Airlines Still Accept Brachycephalic Breeds in Cargo

A smaller number of airlines accept brachycephalic breeds in cargo under specific conditions:

- **Korean Air:** Accepts on some routes with a veterinary fitness-to-fly certificate
- **Cathay Pacific:** Seasonal restrictions only (summer embargo); accepts some brachycephalic breeds outside peak summer
- **Air Canada:** Seasonal embargo June-September; accepts outside that period

Always verify directly with the airline's cargo division — policies change seasonally and without notice.

## The Cabin Option

If your brachycephalic dog or cat is under 8kg including carrier, and the airline permits cabin pets, this is almost always the better option. In the cabin:

- Temperature is stable and comfortable
- You are present to observe your pet
- Stress levels are typically lower
- No cargo handling risks

For a French Bulldog at 10kg, however, even the cabin option is unavailable due to weight. These dogs are in a genuinely difficult position for international travel.

## Specialist Pet Transport for Brachycephalic Breeds

Some specialist pet transport companies offer ground transport (van or land crossing) as an alternative to air for routes where this is feasible — particularly within Europe. For UK to mainland Europe, this can be a practical alternative to air cargo for a breed that cannot fly.

For long-haul routes (UK to Australia, US to Japan), there is no viable non-air alternative. The welfare consideration has to be weighed carefully, ideally with your vet's guidance.

---

*Data current as of {TODAY}.*
""",
     [
         ("Can a French Bulldog fly in cargo internationally?", "Most major airlines have banned brachycephalic breeds including French Bulldogs from cargo. Lufthansa, British Airways, Air France, KLM, and Swiss all have year-round cargo bans. Some carriers (Korean Air, Cathay Pacific outside summer) still accept brachycephalic breeds with conditions. A French Bulldog under 8kg with carrier can fly in the cabin on airlines that permit cabin pets."),
         ("What is the safest way to transport a brachycephalic dog internationally?", "Cabin travel is safer than cargo for brachycephalic breeds — stable temperature, your presence, and no ground handling. If cabin is not possible due to weight, seek a specialist transport company and veterinary guidance. For routes where only cargo is available, your vet should assess your individual dog's fitness for travel before booking."),
     ]
    ),

    ("pet-crate-guide-iata-requirements",
     "Choosing the Right Pet Travel Crate: IATA Size Requirements, Materials, and What Airlines Check",
     "Airlines reject non-compliant crates at check-in. Here's how to measure your pet correctly, understand IATA requirements, and choose the right crate first time.",
     ["crates", "iata", "planning", "cargo"],
     "2026-04-26",
     """A non-compliant crate means your pet does not travel. Airlines check crates at check-in, and a crate that fails any IATA requirement is grounds for refusal. This is one of those areas where getting it right the first time saves significant stress.

## IATA's Core Crate Requirements

The IATA Live Animal Regulations (LAR) specify minimum standards. These are the rules airlines enforce:

**Construction:**
- Rigid (hard plastic or metal) for cargo travel
- Solid floor, no gaps larger than 1.9cm (3/4 inch)
- Ventilation on at least three sides (some airlines require four)
- Doors must be secure — spring-loaded or bolted shut, not twist-close catches only
- Nuts and bolts on the door hinges (some airlines require bolt-through nuts, not just clips)

**Size:**
The crate must be large enough for your pet to:
- Stand with full head clearance (head does not touch the roof)
- Turn around fully
- Lie down in a natural position (stretched out)

**Interior measurements to aim for (dogs):**
- Length: animal's length nose-to-tail + half that length again
- Width: animal's width at widest point x 2
- Height: animal's standing shoulder height to highest point x 1.1-1.25

**Accessories required:**
- Water dispenser attached to the door (accessible from outside)
- Food dispenser (for journeys over 4 hours)
- Absorbent bedding (not loose material)
- Live Animal stickers on all four sides (usually supplied by the airline)
- Directional arrows (THIS WAY UP) on two sides
- Your name, address, phone number, and destination contact on the crate
- "Do Not Feed" or feeding instructions with schedule

## Soft-Sided Carriers

Soft-sided carriers are acceptable for **cabin travel only** if they meet the airline's under-seat dimensions. They are not acceptable for cargo. Each airline specifies maximum dimensions — typically around 40x25x20cm, but check your specific carrier.

## Common Rejection Reasons

- **Crate too small:** The most common reason. Measure your pet in position, not from memory.
- **Non-rigid construction:** Soft crates are not accepted for cargo.
- **Inadequate ventilation:** Bottom of crate or solid walls on all four sides.
- **Unsecured door:** Doors must not be able to open under pressure.
- **Missing water dispenser:** Required for all cargo flights.
- **No contact information:** Must be on the outside of the crate.

## Buying the Right Crate

Brands that consistently meet IATA requirements include Vari Kennel, Petmate, Sky Kennel, and Ruff Tuff. Measure your pet before purchasing — manufacturers list sizes by weight as a guide, but weight-based sizing is unreliable across breeds. Measure, then buy.

Purchase the crate 2-3 weeks before travel and leave it in your home, open, with bedding inside. A familiar crate is a less stressful crate.

---

*Sources: IATA Live Animal Regulations (current edition). Data current as of {TODAY}.*
""",
     [
         ("How do I measure my dog for an airline crate?", "Measure your dog: (1) length from nose to base of tail, (2) height from floor to top of head while standing, (3) width at the widest point. The crate should allow your dog to stand upright with headroom, turn around completely, and lie fully stretched. Add at least 5-10cm to each dimension as a minimum."),
         ("Can I use a soft crate for international cargo travel?", "No. IATA Live Animal Regulations require a rigid crate for cargo transport. Soft-sided carriers are only acceptable for cabin travel, where they must fit under the seat in front of you. For cargo, use a hard plastic or metal crate meeting IATA construction requirements."),
     ]
    ),

    ("rabies-titre-test-complete-guide",
     "The Rabies Titre Test: Which Countries Require It, Where to Get It Done, and What the Numbers Mean",
     "A rabies titre test result of 0.5 IU/mL is the threshold most countries use. Here's what that means, which labs are approved, and what happens if your pet fails.",
     ["titre-test", "rabies", "planning", "documentation"],
     "2026-04-27",
     """The rabies titre test (also called the Rabies Neutralising Antibody Test, RNAT, FAVN, or RFFIT) is one of the most misunderstood parts of international pet transport. It is not a vaccination. It is a blood test that proves your pet's vaccination has worked.

## Which Countries Require It

The titre test is required by countries that are rabies-free or rabies-controlled and want to keep it that way. As of 2026:

- **Australia:** Required for pets from all countries
- **Japan:** Required for pets from most countries (timing is critical)
- **New Zealand:** Required for pets from non-Group 1 countries (UK is Group 1 and still requires it)
- **UK:** Required for pets from non-listed countries (India, South Africa, most of the world)
- **Singapore:** Required for some AVS categories
- **Taiwan:** Required; duration of quarantine depends on result
- **Hawaii (USA):** Required for direct entry (mainland USA does not require it)

EU countries entering from approved countries do not typically require titre tests.

## The Test Process

1. Your pet must be **microchipped** (before any vaccination)
2. Your pet must be **vaccinated against rabies** (after microchipping)
3. Wait at least **30 days** after vaccination
4. A licensed vet draws blood
5. Blood sample is sent to an **approved laboratory** under cold chain conditions
6. Lab measures the level of virus-neutralising antibodies

## The 0.5 IU/mL Threshold

Most countries use a minimum threshold of **0.5 IU/mL** (international units per millilitre). Results above this are considered satisfactory. Results below this mean:

- The vaccination has not produced a sufficient immune response
- The pet cannot travel until re-vaccinated and retested with a satisfactory result
- The waiting period resets from the new satisfactory result date

A low result is not a disaster — it happens. Re-vaccination and a second test 30+ days later usually produces a satisfactory result.

## Approved Laboratories

Each destination country has its own approved lab list. Common approved labs:

| Country | Lab |
|---------|-----|
| UK | APHA Weybridge (via vet submission) |
| USA | Kansas State University VDL, Colorado State University |
| Germany | Friedrich-Loeffler-Institut |
| France | ANSES Nancy |
| Australia (DAFF) | CSIRO AAHL, approved state labs |
| Japan (MAFF) | National Institute of Infectious Diseases |

Always verify against the current list published by the destination country — lab approvals change.

## Result Validity

**Japan:** The titre test result has a specific validity window. It must be retested if more than a certain period has passed. Check MAFF current requirements.

**Australia:** The titre test result itself does not expire, but the 180-day waiting period from the result date is fixed. If you miss the travel window, you will need to reconfirm current requirements with DAFF.

**UK:** A satisfactory result from a valid approved lab is accepted without re-testing for a defined period — check APHA current guidance.

---

*Sources: WOAH FAVN test standards, APHA UK, DAFF Australia, Japan MAFF. Data current as of {TODAY}.*
""",
     [
         ("What happens if my pet's titre test result is below 0.5 IU/mL?", "Your pet will need to be re-vaccinated and the titre test repeated at least 30 days later. The waiting period for travel (e.g. 90 days for the UK, 180 days for Australia) resets from the date of the new satisfactory result. A below-threshold result does not mean your pet is permanently ineligible — it usually just means the vaccination schedule needs to be repeated."),
         ("How much does a rabies titre test cost?", "In the UK, APHA Weybridge charges approximately £120-180 for the FAVN test. In the US, Kansas State University charges approximately USD 75-90. Factor in your vet's blood draw fee (£30-60) and cold-chain courier costs to the lab. Total cost per test is typically £150-250 in the UK."),
     ]
    ),

    ("moving-multiple-pets-internationally",
     "Moving Multiple Pets Internationally: How to Manage the Paperwork When You Have Three Animals",
     "Each pet needs its own documentation chain. Here's how to track timelines, share vet appointments, and avoid letting one pet's issue delay the whole move.",
     ["planning", "guide", "multiple-pets"],
     "2026-04-28",
     """Moving two cats and a dog internationally is not twice as hard as moving one animal. It is at least three times harder, because each animal has an independent documentation chain, and the slowest animal determines when you can all travel together.

## The Core Problem: One Pet Can Hold Up the Others

Imagine your dog has a satisfactory titre test result. Your older cat has a result just below threshold — she needs to be revaccinated and retested. That 30-day revaccination wait, plus another 30 days for the test, plus the destination country waiting period, means the whole household is delayed by months.

The only solution is to start all animals simultaneously — and to build buffer time into the schedule.

## Documentation Tracking

For each animal, you need to track:

- Microchip number and implant date
- Vaccination dates and lot numbers
- Titre test blood draw date
- Titre test result date and value
- Destination country waiting period start date
- Earliest permitted travel date
- Health certificate issue window

A simple spreadsheet with one row per animal and one column per step makes this manageable. Share it with your vet and agent at the start of the process.

## Shared Vet Appointments

Many steps can be done simultaneously for multiple pets:

- Microchips can be implanted in all animals on the same day
- Vaccinations can be given on the same day
- Blood for titre tests can be drawn at the same appointment
- Health certificates can be issued at the same appointment

This reduces cost (single consultation fee for all animals) and keeps all animals on the same timeline.

## Crate Planning

Each animal needs its own compliant crate. For three animals, that is three crates to purchase, label, and present to the airline. Book cargo space for all animals simultaneously — live animal quotas per flight apply, and late bookings may find the quota full.

## Different Species, Different Rules

If you have both dogs and cats, check whether the destination country has different rules for each. China's quarantine differs by species. Some countries' titre test requirements differ. Cats may have a faster processing path in some jurisdictions.

## If One Animal Fails Documentation

If one of your pets cannot travel on the planned date:

- Do not delay the compliant animals indefinitely
- Consider whether a family member or trusted friend can remain with the delayed animal
- Some agents offer boarding and re-export services for animals that miss the travel window

---

*Data current as of {TODAY}.*
""",
     [
         ("Can I move all my pets on the same flight?", "Yes, if the airline's live animal quota and crate capacity allows. Each pet will need its own crate and its own set of documentation. Book cargo space for all animals simultaneously — live animal quotas per flight are limited, and popular routes book up quickly."),
         ("What if one of my pets fails the titre test but the others pass?", "You have options: delay all animals until the failing pet is cleared (simplest but potentially adds months), travel with the compliant animals and arrange separate transport for the failing pet later, or ask a trusted person to care for the failing pet until they can travel. Discuss with your transport agent which option is most practical for your route."),
     ]
    ),

    ("pet-insurance-international-moves",
     "Pet Insurance When Moving Abroad: What Your Policy Covers and the Gaps You Should Know About",
     "Most standard pet insurance policies exclude international transport. Here's what to check in your policy, what transit insurance covers, and whether specialist travel insurance is worth it.",
     ["insurance", "planning", "welfare"],
     "2026-04-29",
     """Pet insurance and international transport occupy an uncomfortable grey area. Most standard policies were written with domestic vet bills in mind. Moving your pet internationally introduces risks — death or injury during transit, quarantine expenses, vet bills abroad — that fall outside most standard cover.

This is not a reason to panic. It is a reason to read your policy and ask direct questions before you travel.

## What Standard Pet Insurance Typically Covers

- Vet bills for illness or injury within the insured country (and sometimes short overseas trips)
- Dental treatment (on some policies)
- Third-party liability for dog owners (UK and EU policies)

What it usually does not cover:
- Death or injury during international transport
- Quarantine costs
- Repatriation costs if you need to return your pet
- Vet bills in the destination country after a specified period abroad

## Reading Your Policy for International Travel

Look for these clauses:

**Geographical limit:** Many UK policies cover temporary travel to EU countries for up to 60-90 days. Permanent moves abroad are excluded.

**Transit exclusion:** Some policies explicitly exclude "death or injury during air or sea transport."

**Quarantine:** Almost no standard policy covers quarantine costs. Australia's mandatory quarantine (AUD 2,000-4,000+) is not insured by any standard UK pet policy.

**Continuous cover abroad:** If you are permanently relocating, your UK policy will likely terminate at some point. You need to arrange cover in your destination country.

## Specialist Transit Insurance

Some IPATA-registered pet transport agents offer optional transit insurance that covers:

- Death or loss during transport (typically market value of the animal)
- Veterinary treatment required during transit
- Kennel fees if transport is delayed

This is distinct from general pet insurance. It is event-specific insurance for the transport journey itself.

Premium amounts vary but typically run £100-400 for a long-haul journey, depending on the animal's declared value.

## Setting Up Insurance in the Destination Country

Before you travel, research pet insurance options in your destination:

- **Australia:** PetSure, Bow Wow Meow, and others offer comprehensive cover
- **USA:** Healthy Paws, Trupanion, Nationwide Pet Insurance
- **UAE:** AXA and Oman Insurance offer pet policies
- **Singapore:** HL Assurance, Great Eastern

Allow a waiting period (typically 14-30 days after policy inception) before the policy covers illness — start the policy early.

---

*Data current as of {TODAY}. Always read your specific policy documents. This article is not insurance advice.*
""",
     [
         ("Does pet insurance cover international transport costs?", "Standard pet insurance policies almost never cover international transport costs, quarantine fees, or death during transit. You need specialist transit insurance from an IPATA agent or cargo insurer for these risks. Check your specific policy documents — clauses vary."),
         ("When should I get pet insurance in my new country?", "As soon as possible after arrival — ideally before landing if the insurer allows it. Most policies have a waiting period of 14-30 days before illness cover activates. If your pet becomes ill in the first two weeks, you may not be covered. Research options in advance and set up the policy before you leave your home country."),
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

        faq_pairs = faqs  # already list of (question, answer) tuples
        content = article(slug, title, desc, tags, pub_date, body, faq_pairs)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        generated += 1
        print(f"  + {slug}.md")

    print(f"\nDone. Generated: {generated} | Skipped: {skipped}")
    print(f"Total blog articles: {len(os.listdir(BLOG_DIR)) - 1}")  # -1 for _index.md


if __name__ == "__main__":
    main()
