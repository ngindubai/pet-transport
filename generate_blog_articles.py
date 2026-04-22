"""
Phase 2 Block 22b: Blog Article Generation
12 articles applying Wordsmith + Optimiser + Chameleon + Interrogator souls.
Topics: cost guides, quarantine explainers, breed travel tips, route-specific advice,
        airline comparisons, documentation how-tos.
"""
import os

CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\blog"
os.makedirs(CONTENT_DIR, exist_ok=True)

# ========================
# 12 blog articles, each hand-crafted per Wordsmith soul rules:
# - Warm, practical, honest. Write for the pet owner, not for Google.
# - No banned vocabulary (delve, robust, seamless, paramount, etc.)
# - No em dashes. No generic conclusions. No significance inflation.
# - High burstiness: mix short punches with longer explanatory sentences.
# - Route-specific facts from the Geographer data.
# - Varied openers, varied rhythm across articles.
# ========================

ARTICLES = [
    {
        "slug": "how-much-does-international-pet-transport-cost",
        "title": "How Much Does International Pet Transport Cost?",
        "seo_title": "International Pet Transport Cost: A Realistic Breakdown",
        "description": "Vet fees, health certificates, crates, airline cargo, quarantine charges. Here's what pet transport actually costs, with realistic figures for popular routes.",
        "date": "2026-04-10",
        "tags": ["cost", "planning", "airlines"],
        "content": """The most common question we get is some version of: how much is this going to cost?

The honest answer is: more than most people expect. But the number varies widely depending on your route, your pet's size, whether quarantine is involved, and whether you use a transport agent.

Here is a realistic breakdown.

## Veterinary preparation

This is the part that surprises people. Before your pet flies anywhere, they need:

- Microchipping (if not already done): around GBP 30-50 / USD 50-80 / AED 100-200
- Rabies vaccination: GBP 50-80 / USD 80-120 / AED 150-300
- Booster vaccinations as required: similar costs
- Rabies titre test (if required by destination, e.g. Australia, Singapore Category B): GBP 150-250 / USD 200-350 for the blood draw and lab fees
- Official health certificate: GBP 100-300 / USD 150-400 depending on country format and endorsement required
- Tapeworm treatment (UK entry for dogs): GBP 40-80

For a dog travelling to Australia, veterinary preparation alone can cost GBP 600-1,000 or more. For a cat travelling from the UK to the USA: under GBP 200 in most cases.

## Import permits and government fees

Several countries require import permits before your pet travels:

- Australia (BICON permit): AUD 420 (around GBP 220)
- UAE (municipality permit): AED 200-400 per emirate
- South Africa (DALRRD permit): varies, budget ZAR 500-1,000
- Singapore (SFA import licence): SGD 30-50

Countries like the UK, USA, Germany, France, and Canada don't charge import permit fees. The documentation system serves as the permit.

## The crate

An IATA-approved crate for a medium dog (say a Labrador) costs around GBP 80-200 for a decent quality rigid crate. For giant breeds, add another GBP 100-200. Soft-sided carriers for cabin travel typically cost GBP 40-100.

Buy the right size: your pet must be able to stand, sit upright, lie down, and turn around without touching the sides. Go one size up if in doubt. Airlines will reject an undersized crate.

## Airline cargo fees

This varies the most. Airline cargo fees are based on the dimensional weight of the crate (length x width x height divided by 6,000), not your pet's actual weight.

Rough figures per route:

- UK to USA: GBP 400-900 for a medium dog
- UAE to UK: AED 1,500-3,500 (GBP 330-770)
- USA to Australia: USD 800-2,000 depending on dog size and crate dimensions
- UK to Singapore: GBP 500-1,200

Smaller pets in cabin cost significantly less: typically GBP 50-150 as an in-cabin pet fee, depending on the airline and route.

## Quarantine costs

This is where Australia stands apart from every other country in this guide.

Australia's mandatory quarantine at Mickleham costs AUD 2,000-4,000 for a 10-day stay. That's the government facility fee. It doesn't include the flights, the vet prep, or the permit.

Singapore Category C countries (including UAE) require 30 days in a government facility: costs around SGD 1,500-2,500 (GBP 900-1,500).

Most other countries have no quarantine requirement for compliant pets, so this cost is zero.

## Pet transport agent fees

Using an IPATA-accredited agent to handle the whole process costs GBP 500-2,500 depending on the route and complexity. For an Australia route, many people consider this essential. The agent coordinates the vet timing, permit applications, airline bookings, documentation sequence, and collection at the other end.

For simpler routes (UK to EU, USA to Canada, intra-EU), many confident owners handle the process themselves.

## Total cost estimates

These are approximate ranges. Your actual costs depend on dog size, airline, season, and origin country.

**UK to USA (medium dog, low-risk route):** GBP 600-1,400  
**UK to Australia (medium dog, Group 3):** GBP 3,000-6,000  
**UAE to UK (medium dog):** AED 5,000-12,000 (GBP 1,100-2,600)  
**USA to Australia (medium dog, Group 4 with 180-day wait):** USD 4,000-9,000  
**UK to Germany (cat, EU travel):** GBP 300-600  

If you're seeing quotes significantly below these ranges from a provider, ask what's included. Some quotes exclude quarantine, DAFF permits, government endorsements, or collection at the destination.
"""
    },
    {
        "slug": "australia-pet-quarantine-explained",
        "title": "Australia Pet Quarantine: What Actually Happens at Mickleham",
        "seo_title": "Australia Pet Quarantine Explained: Mickleham, Costs and the 180-Day Rule",
        "description": "Australia requires mandatory quarantine for every imported dog and cat. Here's what happens at Mickleham, how long it takes, and what the 180-day titre test rule actually means.",
        "date": "2026-04-11",
        "tags": ["australia", "quarantine", "planning"],
        "content": """Australia is the one destination that stops most pet owners cold when they first look into it.

Every imported cat and dog undergoes mandatory government quarantine. No exceptions, no exemptions. The facility is in Melbourne. Your pet goes there regardless of which Australian city you're moving to. If you're moving to Perth or Brisbane or Sydney, your pet still arrives in Melbourne.

Here is what actually happens.

## Mickleham Post Entry Quarantine Facility

The facility is run by DAFF (Department of Agriculture, Fisheries and Forestry) through a contracted operator. It's outside Melbourne, purpose-built for this. Pets are housed in individual enclosures, monitored by trained staff, and have access to exercise. It is not a kennel in the familiar sense. It's a biosecurity facility, which means strict protocols around movement and interaction.

The minimum quarantine period is 10 days. Most pets from Group 3 countries (UK, Japan, Singapore, Hawaii) serve 10 days. Pets from Group 4 countries (USA, Canada, EU, South Africa) also serve 10 days of quarantine, but the longer preparation window happens before the pet travels, not inside the facility.

## The 180-day rule: what it is and why it matters

For Group 4 countries, the preparation timeline is what makes Australia different. The requirement is:

1. Two rabies vaccinations, at least 30 days apart
2. Wait at least 30 days after the second vaccination
3. Blood draw for rabies titre test (RNATT/FAVN)
4. Titre test must show at least 0.5 IU/ml at a DAFF-approved lab
5. **Wait 180 days from the date of blood draw** before your pet can enter Australia

That 180-day wait is the constraint. It is measured from the blood draw date, not from when you get the result. If the result comes back in week 3 and shows 0.5, you still wait 180 days from the draw date.

If the titre test fails, you restart from step 3. The whole 180-day clock starts again from the next blood draw.

This is why DAFF and most pet transport agents quote 6-8 months minimum preparation time for Group 4 countries.

## Booking quarantine space

Spaces at Mickleham must be pre-booked and they fill up. This is not a theoretical constraint. If you fail to secure a quarantine booking, your pet cannot travel.

Book the quarantine space before finalising your own travel date. Then work backwards from your quarantine booking date to determine when veterinary preparation needs to start.

The quarantine fee is roughly AUD 2,000-4,000 for a 10-day stay for a single pet. This is the government facility charge. It is paid by the owner.

## Summer and brachycephalic breeds

December through February in Australia brings temperatures that can exceed 40 degrees Celsius at Mickleham. DAFF issues specific heat stress warnings for brachycephalic (flat-faced) breeds during this period, and for elderly, overweight, or medically compromised animals.

If your dog is an English Bulldog, French Bulldog, Pug, Boxer, or similar flat-faced breed, a summer arrival is significantly higher risk. May through September is the safer window.

Most airlines also impose seasonal restrictions on transporting brachycephalic breeds as cargo. The timing issue therefore applies twice: both to the quarantine environment and to the airline cargo booking.

## What happens after quarantine

When the quarantine period ends and all health checks pass, your pet is released. If you're in Melbourne, you collect them directly from Mickleham. If you're in another city, a domestic flight to your destination is needed. Some owners use a pet transport agent to coordinate the collection and onward journey.

Your pet arrives having been in a facility for 10+ days. Give them time to readjust. Some animals need a few days to decompress after the experience.

## Using a transport agent for Australia

DAFF themselves recommend it. The documentation sequence for Australia is unforgiving: steps must be done in the right order, with the right timing, and using the right labs. An error at any point can reset the timeline.

IPATA-accredited agents in the UK, USA, UAE, and other major origins handle Australia pet imports regularly. They coordinate the vet schedule, title test labs, BICON permit applications, airline bookings, Mickleham pre-booking, and collection.

For most routes, you can handle pet transport yourself. For Australia, the complexity is real.
"""
    },
    {
        "slug": "flying-with-a-french-bulldog-what-airlines-accept",
        "title": "Flying with a French Bulldog: Which Airlines Will Take Them",
        "seo_title": "Flying with a French Bulldog: Airline Restrictions and What You Need to Know",
        "description": "French Bulldogs face stricter airline restrictions than most breeds. Here's which airlines accept them, which ban them from cargo, and how to plan an international move.",
        "date": "2026-04-12",
        "tags": ["breeds", "brachycephalic", "airlines"],
        "content": """The French Bulldog is the most popular dog breed in several countries. It's also one of the most restricted when it comes to air travel.

If you own a Frenchie and you're planning an international move, you need to know the airline landscape before you book anything.

## Why French Bulldogs are restricted

French Bulldogs are brachycephalic. That word means short-skulled, and it describes the flattened face and compressed airway structure that defines the breed. The same anatomy that makes them look the way they do also means they have reduced capacity to thermoregulate, get less oxygen under stress, and are more vulnerable to breathing difficulties during air travel.

The risks are real. Several brachycephalic dogs have died in airline cargo holds over the years, leading airlines to tighten their policies significantly from around 2018 onwards.

## Airlines that ban French Bulldogs from cargo

Several major international airlines have blanket cargo bans for brachycephalic breeds:

**British Airways:** No brachycephalic breeds in cargo, year-round. No exceptions.

**Virgin Atlantic:** Same policy. Year-round ban.

**Singapore Airlines:** No brachycephalic breeds in cargo.

**Qantas:** English Bulldogs banned year-round. French Bulldogs and other flat-faced breeds restricted.

If you're planning a UK-to-Singapore route, for example, your options with these airlines are very limited.

## Airlines with seasonal restrictions

Other airlines don't ban flat-faced breeds outright but apply seasonal embargoes:

**Emirates SkyCargo:** Imposes heat embargoes during summer months (roughly May to September). Brachycephalic breeds are additionally restricted. Check current policy for your specific route.

**Lufthansa:** Seasonal embargoes apply. Outside the embargo periods, brachycephalic breeds may be accepted with a vet fitness-to-fly certificate.

**Air France:** Similar seasonal approach. Policy varies by route.

**KLM:** Seasonal restrictions. Some routes more lenient than others.

## Airlines that accept French Bulldogs with conditions

Some airlines will accept French Bulldogs in cargo with additional conditions:

- A fitness-to-fly certificate from a licensed veterinarian, specifically assessing the dog's airway health
- Booking outside summer months
- Pre-approval from the airline's veterinary or cargo team before booking

Korean Air and Japan Airlines have historically been more flexible on brachycephalic cargo than European carriers, depending on the route. Policies change, so always verify directly with the airline's cargo desk for your specific route and travel dates.

## The cabin option

If your French Bulldog is small enough, cabin travel is a viable alternative on many routes. The cabin environment is climate-controlled and you can monitor your dog throughout the flight.

Most airlines that allow cabin pets set a weight limit of 8-10kg including the carrier. A French Bulldog at healthy weight is typically 8-14kg. Some fit under the cabin limit; many don't.

Airlines that allow cabin pets on relevant international routes include Lufthansa, KLM, Air France, and several others. On long-haul routes (London to Singapore, Dubai to London), cabin pet policies vary and some airlines don't permit in-cabin pets on certain aircraft types.

## Getting a fitness-to-fly certificate

A fitness-to-fly certificate from a vet is not the same as a standard health certificate. It requires a vet to specifically assess your dog's airway, check BOAS (Brachycephalic Obstructive Airway Syndrome) grade, and confirm the dog is healthy enough to handle the physiological stress of air travel.

Not all vets are familiar with this assessment. Look for vets with experience in brachycephalic breeds or aviation medicine. The certificate is only as useful as the airline finds it: some airlines accept them as conditions for carriage; others won't accept brachycephalic breeds regardless of what the certificate says.

## Practical advice

If you're planning an international move with a French Bulldog:

1. Identify the route first. Know your origin, destination, and typical flight time.
2. Call the cargo desks of every major airline on that route and ask specifically about brachycephalic breeds. Get the answer in writing if possible.
3. Plan around the cooler months. Summer cargo embargoes eliminate most options on many routes.
4. Get a vet assessment early, specifically from someone experienced with brachycephalic health.
5. Consider whether a pet transport agent might be worth it. Agents with specific brachycephalic experience know which airlines are currently accepting flat-faced breeds on which routes.

The process is manageable. But it requires more lead time and more specific research than moving a Labrador.
"""
    },
    {
        "slug": "cdc-dog-import-rules-usa-explained",
        "title": "CDC Dog Import Rules for the USA: The 2024 Changes Explained",
        "seo_title": "CDC Dog Import Rules USA 2024: High-Risk, Low-Risk and What Changed",
        "description": "The CDC overhauled US dog import rules in 2024. Here's what changed, what high-risk vs low-risk means for your dog, and what the CDC Dog Import Form actually does.",
        "date": "2026-04-13",
        "tags": ["usa", "regulations", "dogs"],
        "content": """The United States overhauled its dog import rules in 2024 in ways that catch a lot of people off guard. If you're bringing a dog to the USA, or taking your dog abroad and returning, the rules are not what they were before August 2024.

Here is what actually changed and what it means in practice.

## The core change: CDC now manages all dog imports

Before 2024, USDA (specifically APHIS) handled dog import health requirements. The CDC has taken over as the primary agency for dog imports. The practical implication is a new system: the CDC Dog Import Form.

**Every dog entering the USA now needs a CDC Dog Import Form receipt.** Every single dog, regardless of breed, age, origin country, or vaccination status. The form is free, completed online at cdc.gov/importation before travel, and generates a QR code you present at the border or airport.

For dogs from low-risk countries, this form plus appearing healthy is the entire process.

## High-risk vs low-risk: what the CDC means

The CDC classifies every country as either high-risk or low-risk for dog rabies. The classification is based on the country's rabies prevalence in dogs specifically (not wildlife).

**Low-risk countries** include the UK, all EU member states, Canada, Australia, Japan, Singapore, and Hong Kong, among others. Pets from these countries had no elevated rabies risk from dogs in the CDC's view.

**High-risk countries** include the UAE, South Africa, India, Pakistan, Mexico (certain states), most of Africa, much of Asia and South America. The full list is on the CDC website.

If your dog has lived entirely in low-risk countries for the past six months: CDC Dog Import Form receipt plus a healthy-looking dog at the border. Done.

If your dog is from a high-risk country, or has spent time there: the process depends on their vaccination status.

## High-risk dogs: US-vaccinated vs foreign-vaccinated

The CDC distinguishes between dogs with US-issued rabies vaccinations and dogs with foreign-issued vaccinations.

**US-vaccinated dogs returning from high-risk countries** need:
- CDC Dog Import Form receipt
- Certification of U.S.-Issued Rabies Vaccination form, completed by a USDA-accredited vet and endorsed by USDA
- Arrival at an airport with CBP inspection (most major airports)

**Foreign-vaccinated dogs from high-risk countries** need:
- CDC Dog Import Form receipt
- Certification of Foreign Rabies Vaccination and Microchip form, completed by a vet and endorsed by government vet in the departure country
- Reservation at a CDC-registered animal care facility
- Either: a valid rabies serology titre from a CDC-approved lab (blood drawn at least 30 days after the rabies vaccine, at least 28 days before US entry), OR: willingness to complete 28-day quarantine at the CDC-registered facility

## The airport restriction for high-risk foreign-vaccinated dogs

This is the rule that creates the most problems for people who don't know about it.

If your dog is from a high-risk country, has a foreign-issued rabies vaccination, and doesn't have a valid titre: your dog must arrive at a US airport that has a CDC-registered animal care facility. You cannot fly to a different city first. No domestic connections.

The reason: the CDC-registered facility needs to complete their services before the dog enters the US domestic network. This can force people to change their planned routing significantly.

## The 6-month age requirement

All dogs entering the USA must be at least 6 months old. No exceptions. Puppies under 6 months cannot enter. This applies regardless of country of origin, vaccination status, or owner circumstances.

## What this means for common routes

**Dubai to New York:** The UAE is high-risk. Your dog needs a titre test or CDC facility reservation. You must arrive at JFK or another CDC-registered airport. No connecting through another US city first.

**London to New York:** UK is low-risk. CDC Dog Import Form plus healthy appearance. That's it.

**Johannesburg to Los Angeles:** South Africa is high-risk. Same process as UAE route. Must arrive at LAX or another CDC facility airport.

**Toronto to Boston:** Canada is low-risk. CDC form only.

## What about cats?

US federal law has no animal health requirements for importing pet cats. No CDC form, no health certificate, no vaccination requirement from the federal side. Individual states may have rules, so check your destination state. But at the federal border, a healthy cat is not your documentation problem.

## Checking current requirements

The CDC list of high-risk countries and the list of CDC-registered animal care facilities both change. Check cdc.gov/importation for the current versions before booking any travel. Don't rely on guides published more than six months ago for the specific lists.
"""
    },
    {
        "slug": "iata-crate-guide-international-pet-transport",
        "title": "IATA Crates for Pet Travel: Sizing, Rules and What Airlines Check",
        "seo_title": "IATA Pet Crate Requirements: Size Guide for International Air Travel",
        "description": "Every pet travelling by air cargo needs an IATA-compliant crate. Here's the sizing formula, what airlines actually check, and the mistakes that get crates rejected.",
        "date": "2026-04-14",
        "tags": ["equipment", "airlines", "planning"],
        "content": """You can have all your paperwork perfect and your pet ready to fly, but if the crate is wrong, the airline will not accept your pet.

IATA (International Air Transport Association) sets the standards for live animal transport by air. Every airline follows these standards for cargo pets. This guide explains what the standards actually require.

## The sizing rule

The single most misunderstood part of crate selection is the sizing requirement.

Your pet must be able to:
- Stand upright without their head touching the top
- Turn around completely inside the crate
- Lie down in a natural position
- Sit upright

This means the crate must be larger than your pet's current dimensions in every direction. The standard formula is:

- **Length:** Pet's body length (tip of nose to base of tail) + half the length from the floor to the top of the head when standing
- **Width:** Twice the width across the shoulders
- **Height:** Pet's height from floor to top of head when standing + a few centimetres

For a medium Labrador: this typically comes out at an IATA size 4 or 5 (approximately 91cm x 61cm x 69cm or larger). For a small Beagle, a size 3. For giant breeds like a Great Dane, you may need a custom or size 7 crate.

When in doubt, go larger. Airlines will not reject a correctly built crate for being too big. They will reject one that's too small.

## Construction requirements

IATA-approved crates for cargo must be:

**Rigid construction.** Plastic moulded crates like the Petmate Sky Kennel, Vari-Kennel, or similar designs from IATA-approved manufacturers. Soft-sided carriers are not accepted for cargo. Wire mesh crates are not accepted for cargo.

**Ventilation on at least three sides.** The ventilation must not allow any part of your pet to protrude outside the crate.

**Secure door.** The door must latch properly and cannot be opened by the animal from inside. Some airlines require zip-ties or secondary securing on the door bolts.

**Non-slip floor.** Either a moulded non-slip base or absorbent bedding material. Some airlines require absorbent lining.

**Water and food containers.** Must be attached to the inside of the door so staff can refill without opening the crate. Wire or clip-on bowls are standard.

**Live animal labels.** Orange "LIVE ANIMALS" stickers on the top and at least one side. These come with most airline-approved crates or can be purchased separately.

**Orientation arrows.** "This side up" arrows on at least two sides.

**Contact labels.** Attach a label to the crate with your name, phone number, address, and the consignee's contact details at the destination.

## What airlines check at drop-off

At the cargo desk, the airline agent will:

1. Check that the crate type and construction matches IATA standards for the route
2. Verify that the pet can stand, turn, and lie down comfortably
3. Confirm the door mechanism is secure
4. Look for live animal labels and orientation arrows
5. Check that water containers are attached and accessible
6. Verify your pet's documentation matches the animal in the crate (microchip number, species, colour)

Airlines are not trying to be difficult. These checks protect your pet. A crate that falls apart in the hold, or a pet that overheats because ventilation was inadequate, is a serious welfare incident.

## Common reasons crates are rejected

- Soft-sided carrier presented for cargo (only for cabin)
- Crate assembled incorrectly (bolts not fully engaged)
- No water container
- No live animal labels
- Too small (the most common reason)
- Damaged or cracked crate
- Non-approved design (folding wire crates, travel bags)

## Cabin pet carriers

Different rules apply for in-cabin pets. The carrier must fit under the seat in front of you. Most aircraft have a space roughly 45cm x 35cm x 20cm under the seat, though this varies by airline and aircraft type. The carrier can be soft-sided. The combined weight (pet plus carrier) must meet the airline's limit, usually 8-10kg.

Check the specific dimensions and limits for your airline and your aircraft type. The A380 configuration differs from the 737 configuration.

## Buying the right crate

Reputable IATA-approved crate brands include: Petmate Sky Kennel, Vari-Kennel by Petmate, Bergan Comfort Carrier, and airline-specific branded crates. Most major airlines sell approved crates at their cargo desks.

Buy the crate well before your travel date. Acclimatise your pet to the crate over several weeks if possible. A pet that is comfortable in their crate before the journey handles the experience better.

Don't modify the crate. Drilling additional holes, adding internal shelving, or attaching external items will likely make the crate non-compliant.
"""
    },
    {
        "slug": "pet-health-certificate-guide-international-travel",
        "title": "Pet Health Certificates for International Travel: A Practical Guide",
        "seo_title": "Pet Health Certificate for International Travel: Which One, When, and How",
        "description": "Not all health certificates are the same. AHC, USDA-endorsed, government-endorsed. Here's which certificate your pet needs, who issues it, and how long it's valid.",
        "date": "2026-04-15",
        "tags": ["documentation", "planning", "regulations"],
        "content": """A pet health certificate sounds like a simple document. A vet looks at your dog, confirms they're healthy, writes a note. Done.

In practice, different countries require different certificate formats, different endorsements, and have different validity windows. Getting the wrong certificate, or getting the right certificate at the wrong time, can ground your pet.

## Three main certificate types

**Animal Health Certificate (AHC)**
Used primarily for travel within and into the EU, and to enter the UK from outside the EU. The AHC is an official document issued by an official veterinarian (not just any vet) who is authorised by their national authority. In the UK, that's an APHA-authorised vet. In the USA, that's a USDA-accredited vet (with USDA endorsement for EU-bound pets).

AHCs for entering the UK are valid for 10 days from the date of issue for entry, and for 4 months for the return journey or onward EU travel. You need a new AHC for each trip.

**USDA-Endorsed Health Certificate**
For pets leaving the USA for most destinations. A USDA-accredited vet completes the health examination and fills in the certificate. You then submit it to USDA APHIS Veterinary Services for endorsement. USDA verifies and stamps the certificate. Cost: USD 38 per certificate for the USDA endorsement fee. Processing time: 2-10 business days depending on method.

**Country-specific government health certificate**
Some countries (Australia being the main example) require health certificates in a specific DAFF-approved format. The certificate format is negotiated between DAFF and each approved exporting country. You must use the exact format DAFF specifies for your specific origin country. There is no flexibility on this.

## Timing: the 10-day rule

Most health certificates have a validity window of 10 days from issue for initial entry into the destination country. This means the vet examination and signing must happen within 10 days of your pet's arrival at the destination.

Not departure. Arrival.

If your flight is 12 hours and your certificate was issued 9 days ago, you have one day to spare. If you're on a 24-hour journey involving connections and the certificate was issued exactly 10 days before you depart, it will likely be expired by the time you arrive.

Plan the vet appointment for 7-9 days before your arrival date, not 10.

## Endorsement: when do you need it?

Many countries require that the health certificate is endorsed (authenticated) by the official veterinary authority of the exporting country, not just by a private vet.

**UK export (APHA endorsement):** Required for most exports from the UK to non-EU countries. The vet completes the certificate; APHA endorses it. APHA offers online and postal endorsement. Allow 3-5 working days.

**USA export (USDA endorsement):** Required for most destinations. USDA endorsement adds USD 38 per certificate. USDA's VEHCS (Veterinary Export Health Certification System) allows electronic submission for some countries.

**Australia export (DAFF endorsement):** Required. All pet export health certificates from Australia must be endorsed by a DAFF-authorised vet and then by DAFF itself.

## The microchip: sequence matters

Almost all countries require that the microchip is implanted before the rabies vaccination. If your pet is vaccinated before being microchipped, the vaccination may not be recognised by the destination country. This is not a theoretical rule. Australia, the UK, the EU, and the USA all have this requirement.

On the health certificate, the vet confirms:
1. The microchip was read at the appointment
2. The microchip number matches the vaccination record
3. The vaccination was given after the microchip was implanted

If these three things don't line up on the paperwork, the certificate will not be accepted.

## Which certificate do you need?

| Route | Certificate needed |
|-------|-------------------|
| Any country to UK | AHC (issued by official vet in origin country) |
| USA to EU (incl. Germany, France) | USDA-endorsed AHC in EU format |
| UK to EU | AHC from APHA-authorised vet |
| Any country to Australia | DAFF-approved country-specific format |
| Any country to UAE | Government-endorsed official health certificate |
| UK to USA | AHC or equivalent (UK pets from low-risk country) |
| USA to Canada | USDA-endorsed certificate |
| Any country to Singapore | Certificate per SFA format |

## Practical checklist

Before booking the vet appointment:

- Confirm the exact certificate format required by your destination country
- Confirm whether USDA/APHA/DAFF endorsement is required and how to get it
- Calculate your arrival date, count back 7-9 days, book the vet for that date
- Ensure your vet is officially authorised to issue the certificate (not all are)
- Bring all vaccination records, microchip documentation, and titre test results to the appointment

If any of this is unclear, a pet transport agent or your destination country's official import authority can confirm the exact requirements. Don't rely on guides published more than a year ago: certificate formats and endorsement requirements change.
"""
    },
    {
        "slug": "uae-to-uk-pet-transport-guide",
        "title": "UAE to UK Pet Transport: The Complete Guide",
        "seo_title": "UAE to UK Pet Transport: AHC, Tapeworm Rules, Airlines and Costs",
        "description": "Moving your pet from the UAE to the UK? Here's the documentation process, tapeworm timing rule, which airlines operate the route, and realistic costs.",
        "date": "2026-04-16",
        "tags": ["routes", "uae", "united-kingdom"],
        "content": """Moving a pet from the UAE to the UK is one of the most popular international pet transport routes. Thousands of families make this journey every year as they relocate back to Britain from Dubai, Abu Dhabi, or Sharjah. The process is well-established, but it has several specific rules that catch people out if they haven't done their research.

## The short version

Your pet needs: ISO microchip, valid rabies vaccination, Animal Health Certificate issued within 10 days of arrival in the UK, and (for dogs) a tapeworm treatment administered 24-120 hours before UK arrival time. No quarantine, provided documentation is correct.

Allow 8-12 weeks for preparation from scratch.

## Step by step

**Week 1: Microchip and vaccination**

If your pet isn't already microchipped, start here. The ISO 11784/11785 chip must be in before the rabies vaccination for the vaccination to be valid. UAE vets are generally familiar with this requirement, but confirm the chip standard before proceeding.

After the microchip is implanted (or verified), administer the rabies vaccination. For dogs, distemper, parvovirus, hepatitis, and leptospirosis are standard. For cats, add panleukopenia, calicivirus, and rhinotracheitis. These aren't UK import requirements specifically, but they should be current for a healthy travelling animal.

**21-day wait**

After the first rabies vaccination (or a booster if there was no break in vaccination cover), wait 21 full days before travel. The UK counts 21 days from the vaccination date. Day 1 is the day after the vaccination.

Note: the UAE is on the UK's listed country list, so no titre test is required for pets coming from there.

**Book your travel**

Emirates and Etihad both operate the Dubai/Abu Dhabi to London Heathrow route. Emirates operates the cargo service through Emirates SkyCargo. Etihad uses Etihad Cargo. Both are well-established for live animal transport.

British Airways also operates this route and accepts pet cargo via IAG Cargo.

Check current seasonal restrictions before booking. Summer months (June through August) may affect availability and routing, though the UK is less affected by summer cargo embargoes than the UAE origin side.

**The AHC: your most time-sensitive document**

The Animal Health Certificate must be issued by a government veterinarian (or government-authorised vet) in the UAE within 10 days of your pet's arrival in the UK. This is the document that replaces the EU pet passport system for non-EU countries.

In the UAE, the AHC must be issued by a government-approved clinic and endorsed by the relevant emirate municipality and, for UK requirements, endorsed by the competent authority. Allow 3-5 days for the endorsement process, which means the vet appointment should happen around 7-8 days before your UK arrival date.

**Tapeworm treatment for dogs (critical timing)**

If you have a dog, the tapeworm treatment is the rule that catches people out most often. The treatment (praziquantel, at a dose effective against Echinococcus multilocularis) must be administered by a vet between 24 and 120 hours before your dog's scheduled arrival time in Great Britain.

That timing window is measured against arrival, not departure. A flight from Dubai to London is roughly 7 hours. Factor that in when booking the vet appointment.

Outside that 24-120 hour window (even by an hour) and the treatment is non-compliant. If your flight is delayed and your dog arrives 121 hours after the treatment, you have a problem. Book the treatment at the earlier end of the window (around 100 hours before planned arrival) to give yourself buffer.

## Approved entry ports from UAE

Heathrow is the primary entry point for pets arriving by air from the UAE. The Heathrow Animal Reception Centre (HARC) at the airport handles incoming live animals. Your pet goes through HARC on arrival for document verification.

Manchester and Gatwick are also approved entry airports. Check the GOV.UK approved travel routes page to confirm your specific route is on the approved list before booking.

## Costs

Expect to spend on this route:

- UAE veterinary preparation (microchip if needed, vaccinations, health certificate, endorsement): AED 1,500-3,500
- IATA-approved crate (medium dog): AED 400-800
- Airline cargo fee Dubai/Abu Dhabi to London (medium dog): AED 1,500-3,500
- Pet transport agent (if used): AED 3,000-8,000

For a medium dog using a professional agent door-to-door, budget AED 8,000-15,000 total (roughly GBP 1,700-3,300).

## Common mistakes on this route

**Starting the process too late.** People book flights first, then discover the documentation timeline. If you're leaving in 6 weeks, check immediately whether 21 days of vaccination wait plus AHC timing is achievable.

**Tapeworm appointment at the wrong time.** The 24-120 hour window is strict. Have the exact arrival time booked before scheduling the tapeworm treatment.

**Travelling in peak summer.** June through August from the UAE adds complexity. Not impossible, but more difficult with airline cargo.

**Using a vet not authorised to issue AHCs.** Not every vet in the UAE can issue the correct certificate. Confirm your vet is government-approved for export documentation before the appointment.
"""
    },
    {
        "slug": "usa-to-australia-pet-transport-guide",
        "title": "USA to Australia Pet Transport: The 6-Month Process Explained",
        "seo_title": "USA to Australia Pet Transport: Titre Test, 180-Day Wait and Quarantine",
        "description": "Moving pets from the USA to Australia is one of the most complex routes in international pet transport. This guide covers the full 6-8 month process step by step.",
        "date": "2026-04-17",
        "tags": ["routes", "usa", "australia"],
        "content": """The USA to Australia pet transport route is one of the most time-intensive in the world. If you're starting the process now, your pet is not flying for at least six months. Possibly eight.

That is not pessimism. It's the structure of Australia's import requirements for Group 4 countries, which includes the USA.

## Why it takes so long

Australia requires a rabies titre test (blood test) before entry. But the titre test doesn't start the clock for entry immediately. For Group 4 countries including the USA, the waiting period is 180 days from the date the blood was drawn, regardless of when you get the result.

Before you can draw blood, you need two rabies vaccinations at least 30 days apart, plus a 30-day wait after the second vaccination.

The sequence:
1. First rabies vaccination
2. Wait at least 30 days
3. Second rabies vaccination (or confirm no break in cover if booster only)
4. Wait at least 30 days
5. Draw blood for titre test
6. Submit to DAFF-approved lab
7. Receive passing result (0.5 IU/ml minimum)
8. Wait 180 days from blood draw date (not result date)
9. Apply for BICON import permit (AUD 420, 20-30 day processing)
10. Book quarantine space at Mickleham
11. Arrange flights and USDA-endorsed health certificate
12. Your pet can enter Australia

If step 7 shows a failing titre result, restart from step 5. The 180-day clock resets.

## The BICON import permit

Before your pet can travel, you need an import permit from DAFF's BICON (Biosecurity Import Conditions) system. The cost is AUD 420. Processing takes 20-30 days.

Apply for the permit once you have the passing titre test result and are confident in your travel dates. The permit is valid for 12 months from issue.

## Flights

Your pet arrives in Melbourne. All imported pets in Australia are required to enter through Melbourne and go to Mickleham for quarantine. No other airport accepts pet imports.

Airlines operating this route with pet cargo: Qantas, United Airlines, Singapore Airlines (connecting through Singapore), Cathay Pacific (connecting through Hong Kong). Check current policies for brachycephalic breeds if applicable.

The flight from the US East Coast to Melbourne is long: 20+ hours with connections. Most pets travel via a connection in Asia or the Middle East. Your agent or the airline cargo desk will advise on routing and stopovers.

## Mickleham quarantine

10 days minimum for US-origin pets. The facility is in Victoria, outside Melbourne. Costs AUD 2,000-4,000 for a single pet. Must be pre-booked. Book the quarantine space before you finalise your travel date.

Consider the season. Summer in Melbourne (December through February) means temperatures that can exceed 40 degrees at Mickleham. Flat-faced breeds are at elevated risk. If possible, time arrival for May through September.

## The USDA-endorsed health certificate

This is your most time-sensitive document. The USDA-endorsed health certificate for Australia must be in DAFF's approved format for the USA and must be issued by a USDA-accredited vet. After the vet issues it, submit it to USDA APHIS for endorsement (USD 38 plus processing time of 2-10 business days depending on method).

The certificate must be issued within 5 days of export (Australia's requirement is stricter than the UK's 10-day window). Plan the vet appointment and USDA endorsement submission carefully against your travel date.

## What does it cost?

For a medium dog, USA to Australia, realistic total costs:

- Veterinary preparation (vaccinations, titre test, USDA health certificate): USD 800-2,000
- BICON import permit: AUD 420
- IATA crate (medium dog): USD 150-350
- Airline cargo fees USA to Melbourne: USD 1,200-3,000
- Mickleham quarantine: AUD 2,000-4,000
- Collection from Mickleham and domestic transport (if needed): AUD 300-1,000
- Pet transport agent (strongly recommended): USD 1,500-4,000

Total: roughly USD 6,000-14,000 for a medium dog, depending on origin city, dog size, and whether you use an agent.

## Using an agent

DAFF recommends it. The documentation sequence is genuinely complex. Missing one step or doing them out of order can set the timeline back by months. IPATA-accredited agents in the USA who specialise in Australia routes know which DAFF-approved labs are fastest, which airlines operate the route best for live animals, and how to coordinate the Mickleham booking with airline routing.

This is not a route to manage alone unless you've done it before.

## Starting the process

If you're reading this because you've just found out you're relocating to Australia with your dog: start the vaccination process this week. Every week you wait at the start translates directly to a week of delay at the end.
"""
    },
    {
        "slug": "how-to-choose-a-pet-transport-agent",
        "title": "How to Choose a Pet Transport Agent: What to Ask, What to Check",
        "seo_title": "Choosing a Pet Transport Agent: IPATA Accreditation, Questions to Ask",
        "description": "Not all pet transport agents are equal. Here's how to check accreditation, what questions to ask before committing, and the red flags to watch for.",
        "date": "2026-04-18",
        "tags": ["planning", "agents", "advice"],
        "content": """There are hundreds of companies offering pet transport services internationally. Some are excellent. Some take your money and leave you to figure out the paperwork.

Choosing the wrong one is an expensive mistake. Choosing the right one makes a complex process manageable.

## Start with IPATA accreditation

IPATA (International Pet and Animal Transportation Association) is the industry body for pet transport agents. Membership requires meeting standards and signing a code of ethics. It doesn't guarantee perfection, but it means the company has been vetted.

Check that any agent you're considering is a current IPATA member. The IPATA website has a search function for accredited agents by country. If a company is not on that list, ask why.

DEFRA-registered agents for UK import are a separate requirement. If your pet is entering the UK, the agent you use must be registered with DEFRA to handle live animal imports.

## Route-specific experience matters

Ask directly: how many UAE to UK moves have you handled in the past 12 months? How many USA to Australia routes? Ask them to describe the standard process for your specific route.

A competent agent can answer these questions in detail and without hesitation. They know which airlines currently accept pets on your route. They know which labs are DAFF-approved or CDC-approved for your origin country. They know the typical processing time for import permits in the UAE right now, not what it was two years ago.

If an agent gives you a vague answer or redirects to their website, that's not confidence-inspiring.

## What services should be included?

A good pet transport agent handles:

- Documentation guidance: which certificate format, which vet to use, endorsement process
- Airline booking: cargo booking with appropriate airline on your route
- Transit coordination: handling during connections
- Import permit applications (where applicable, e.g. UAE, Australia, South Africa)
- Collection at the destination or handoff to a local agent
- Ongoing communication throughout the process

Some agents offer door-to-door service including pickup from your home and delivery to your door at the destination. This costs more but reduces the number of handoffs.

## The quote: what to check

When you receive a quote, read the line items carefully. Common items that get excluded from headline quotes:

- DAFF/BICON import permit fee for Australia
- Government endorsement fees (USDA, APHA)
- Quarantine costs (Australia, Singapore)
- Collection at destination airport
- Domestic transport at destination
- Emergency veterinary cover during transit

Ask: "What is not included in this quote?" Not "What is included?" A transparent agent will tell you directly what their quote excludes.

## Red flags

- Agents who guarantee a delivery date on complex routes. No legitimate agent can guarantee a delivery date for Australia or Singapore due to quarantine. Any agent who does is setting false expectations.
- Agents who quote without asking for your pet's details (weight, breed, crate size). Accurate cargo quotes require these numbers.
- Agents who claim you don't need a titre test for Australia from the USA. You do, and the 180-day wait is mandatory.
- Agents who don't ask about breed-specific restrictions when you mention a Pit Bull type or French Bulldog. A competent agent knows these issues and raises them proactively.
- Upfront deposit requests for vague services with no contract or itemised quote.

## Getting multiple quotes

Get at least two quotes for any major route. The variation in pricing can be significant. But price is not the only variable. Ask each agent the same questions and compare the quality of the answers, not just the numbers.

For complex routes (Australia, Singapore Category C from high-risk countries, UAE summer travel), experience and track record matter more than price. Paying GBP 500 more for an agent who has done your specific route 50 times this year is usually worth it.
"""
    },
    {
        "slug": "singapore-pet-import-category-guide",
        "title": "Singapore Pet Import Categories: A, B and C Explained",
        "seo_title": "Singapore Pet Import: Category A, B and C Countries Explained",
        "description": "Singapore classifies pet origin countries into three categories with different quarantine requirements. Here's what Category A, B and C means and which category your country is in.",
        "date": "2026-04-19",
        "tags": ["singapore", "quarantine", "regulations"],
        "content": """Singapore's pet import system is more structured than most people expect. The requirement for your pet depends almost entirely on where they're coming from.

The Singapore Food Agency (SFA) classifies pet origin countries into three groups. Your group determines whether your pet faces no quarantine, 30 days at home, or 30 days in a government facility.

## Category A: no quarantine required

Category A countries are those the SFA considers lowest risk. These include:

- Australia
- New Zealand
- United Kingdom
- Republic of Ireland
- Japan
- South Korea
- Taiwan
- Norway
- Sweden
- Finland
- Iceland

Pets from Category A countries don't require quarantine on arrival in Singapore. They still need an import licence (from the SFA), a microchip, current vaccinations, and a health certificate. But they come home with you on the day they arrive.

## Category B: 30-day home quarantine

Category B includes most developed countries with controlled rabies status. This includes:

- United States
- Canada
- Most EU countries (Germany, France, Netherlands, Belgium, Austria, Switzerland)
- United Kingdom territories not in Category A

Pets from Category B countries serve 30 days of home quarantine in Singapore. This means your pet stays at your residence, must not leave the home premises, and a vet inspection confirms the quarantine is complete at the 30-day mark. There is a government fee for this process.

For people moving to Singapore from the USA or Europe, Category B is the typical experience. The 30-day home quarantine is inconvenient but manageable.

## Category C: 30-day government quarantine

Category C includes higher-risk origin countries. The UAE falls here, as do most countries in South and Southeast Asia, Africa, the Middle East, and parts of South America.

Pets from Category C countries serve 30 days at a government quarantine facility. This is not your home. The facility is a veterinary-supervised government centre. You can visit during specified hours. The cost is roughly SGD 1,500-2,500 and is entirely at the owner's expense.

If you're relocating from Dubai to Singapore with your dog, plan for a 30-day facility stay from the day your dog lands.

## What all categories require

Regardless of category, all pets entering Singapore need:

- A valid import licence from the SFA (apply before travel)
- An ISO microchip (11784/11785 standard)
- Current vaccinations (rabies for cats and dogs, distemper and parvovirus for dogs, feline herpesvirus and calicivirus for cats at minimum)
- An official veterinary health certificate from a government-approved vet in the origin country
- A rabies titre test for Category B and C countries

The titre test requirement adds time to the preparation. Blood must be drawn at least 30 days after the rabies vaccination. The test result needs to show the minimum antibody level before the SFA will approve import.

## Breed restrictions

Singapore's breed ban is one of the most extensive in the world. The following breeds cannot be imported under any circumstances:

Pit Bull Terriers and all related types (including American Pit Bull Terrier, American Staffordshire Terrier, Staffordshire Bull Terrier); Akita; Boerboel; Dogo Argentino; Fila Brasileiro; Japanese Tosa; Perro de Presa Canario; American Bulldog; Neapolitan Mastiff; Rottweiler (in HDB flats, restricted more broadly); and several others.

The list is enforced. There are no permits, no exemptions, and no case-by-case assessments for prohibited breeds. Confirm your breed is not on the list before making any plans.

## Housing and dog numbers

HDB (Housing Development Board) flat owners in Singapore face the most restrictive rules. Only one dog is allowed, and only from the HDB's approved breeds list (small breeds only, with specific weight limits). If you're in an HDB flat, check the approved breed list on the HDB website before deciding which dog to bring.

Private property residents can keep more dogs and a wider range of breeds, subject to licensing and the national breed restrictions.

## The import licence

Apply for the import licence through the SFA website before your pet travels. You'll need your pet's details, vaccination history, titre test results (for Category B and C), and origin country information. Processing typically takes a few business days for Category A applications. Category B and C applications may take longer.

Don't book airline cargo before you have the licence approval. If the SFA rejects the application for any reason, you'd have a booking you can't use.
"""
    },
    {
        "slug": "uk-to-usa-pet-transport-cats-and-dogs",
        "title": "UK to USA Pet Transport: Dogs, Cats and the CDC Process",
        "seo_title": "UK to USA Pet Transport: CDC Form, Airline Options and Route Guide",
        "description": "Moving your pet from the UK to the USA? Dogs need a CDC form; cats need almost nothing. Here's the full process, airlines, and what to expect at the US border.",
        "date": "2026-04-20",
        "tags": ["routes", "united-kingdom", "usa"],
        "content": """Moving from the UK to the USA with a pet is one of the simpler international routes. The UK is a low-risk country in the CDC's classification for dog rabies, which means most of the complex documentation that applies to dogs from high-risk countries doesn't apply here.

That said, there are specifics to get right.

## For dogs

All dogs entering the USA need a CDC Dog Import Form, completed online before travel at cdc.gov/importation. The form is free and generates a QR code you present at the US border or airport. Don't skip this step: customs officers will ask for it.

Beyond the form: your dog must be at least 6 months old, appear healthy at the border, and have a microchip. For dogs from the UK (a low-risk country), no rabies vaccination certificate is required by the CDC, though your dog should have one for the health certificate your vet issues.

The health certificate itself is not federally required for dogs from low-risk countries entering the USA. But most airlines require one for live animal cargo bookings. The USDA-endorsed health certificate is the standard for US airport acceptance.

One thing to know: some US states have their own requirements. Hawaii is the main one. Hawaii requires a separate HDOA (Hawaii Department of Agriculture) process, including rabies titre tests and a specific quarantine or direct release procedure. If you're going to Hawaii, treat it as a completely different process from mainland USA.

## For cats

Cats entering the USA face essentially no federal requirements. No health certificate, no CDC form, no vaccination record required at the federal border. A healthy cat arrives and is waved through.

Your airline will still require documentation for cargo bookings, so have a standard health certificate from your vet. But the US government asks for nothing from a cat arriving from the UK.

## Airlines on the UK to USA route

This is a well-served route with many options:

**British Airways / IAG Cargo:** BA operates the route with pet cargo service through IAG Cargo. Accepts dogs and cats in cargo. Note: BA bans brachycephalic breeds from cargo year-round.

**Virgin Atlantic:** Operates UK to USA routes but does not accept pets in the passenger cabin. Check current cargo pet policy as it varies by route.

**American Airlines:** Accepts cargo pets on transatlantic routes. Policies on breeds and routes vary.

**United Airlines:** Has a PetSafe programme for cargo pets. Good reputation on this route. Does not allow pets in the cabin on transatlantic routes but the cargo service is established.

**Delta Air Lines:** Accepts cargo pets. Check current embargoes and breed restrictions.

**Lufthansa, KLM, Air France:** All operate via their European hubs (Frankfurt, Amsterdam, Paris). These can be good options as they allow small pets in the cabin on European connections, and the US legs have cargo pet services. Useful if you want to fly your cat in the cabin to Amsterdam and then ship them as cargo to the US on a separate booking.

## What to expect at the US border

Your pet arrives as manifested cargo. You collect them from the airline cargo terminal, not the passenger baggage hall. Cargo terminals are usually in a separate facility from the main terminal.

CBP (Customs and Border Protection) will check your documents: CDC Dog Import Form receipt, health certificate, and microchip verification. For dogs from the UK, this is a quick process. Have originals ready.

Your dog is released to you at the cargo terminal after CBP clearance.

## Costs

For a medium dog, London to New York City:

- Health certificate from UK vet (USDA-endorsed for US requirements): GBP 150-300 plus GBP 20-40 USDA endorsement equivalent
- IATA crate (medium dog): GBP 80-200
- IAG Cargo or equivalent airline fees: GBP 500-1,200 depending on dog size
- Agent fee (if used): GBP 500-1,500

Without an agent: GBP 800-1,700 total for a medium dog.
With an agent handling booking and documentation: GBP 1,300-2,900.

For a cat in cargo: GBP 400-900 all-in.

## Timeline

For a UK dog with all vaccinations current: 2-4 weeks lead time is enough. Get the CDC form done first. Book airline cargo. Get the health certificate within 10 days of departure (check the destination state for any certificate validity requirements; federal US entry has no specific window but airlines will have their own).

For a dog starting from scratch (no microchip, no rabies vaccination): allow 4-6 weeks to complete microchip, vaccination, and the 21-day wait before the health certificate appointment.
"""
    },
    {
        "slug": "top-10-pet-import-mistakes",
        "title": "The 10 Most Common Pet Import Mistakes (and How to Avoid Them)",
        "seo_title": "10 Common Pet Import Mistakes: What Goes Wrong and How to Avoid It",
        "description": "From wrong microchip timing to expired health certificates, these are the mistakes that ground pets at airports. Here's what to watch for on every international route.",
        "date": "2026-04-21",
        "tags": ["advice", "planning", "documentation"],
        "content": """The paperwork for international pet transport looks complicated. But most of the problems that actually occur come from a small number of repeatable mistakes.

Here are the ten most common errors, and how to avoid each one.

## 1. Microchipping after vaccination

Nearly every country requires that your pet's microchip is implanted before the rabies vaccination. If the vaccination was given before the chip, or if the chip can't be read, the vaccination may not be recognised by the destination country.

The fix: microchip first, always. Verify the chip is readable with the vet's scanner on the same day. Get the chip number written into every record.

## 2. Starting too late

Australia needs 6-8 months minimum. Singapore Category C routes need 3-4 months. Even simpler routes like UK to Germany need 3-4 weeks. People book their own flights first, then discover the timeline.

The fix: research the pet import requirements for your destination on day one of your relocation planning, not three weeks before you leave.

## 3. Tapeworm treatment at the wrong time

For dogs entering the UK, the tapeworm treatment window is 24-120 hours before arrival in Great Britain. Not departure. Arrival. If your treatment was given 122 hours before your dog lands, it's non-compliant.

The fix: calculate the arrival time first. Count back 96 hours (giving yourself buffer). Book the vet for that time. Tell the vet why the timing matters.

## 4. Using the wrong health certificate format

Australia requires a specific DAFF-approved certificate format. The EU requires an AHC in EU format. Some countries have country-specific formats. Using the wrong format, even if all the information is correct, means your pet may not be admitted.

The fix: contact the destination country's official veterinary import authority to confirm the exact certificate format required before your vet appointment.

## 5. Not allowing time for government endorsement

Most countries require that the health certificate is endorsed by the official veterinary authority of the exporting country (APHA for UK, USDA for USA, DAFF for Australia). This takes time: 3-10 business days typically.

If you book the vet appointment 7 days before travel and then discover you need 5 days for USDA endorsement, you have no buffer.

The fix: add endorsement time to your timeline from the start. Book the vet earlier than you think you need to.

## 6. Booking flights before getting airline confirmation

Airline pet cargo policies change. Some airlines have embargoes by breed, by season, or by route. Booking your own flight and then calling the airline to add your pet is a common sequence. But cargo space for live animals is limited and sometimes unavailable.

The fix: confirm airline cargo availability and breed acceptance before booking any ticket. Book cargo space at the same time as the passenger ticket.

## 7. Overlooking import permits

Australia, the UAE, Singapore, South Africa, and Hong Kong all require import permits applied for before travel. The permit processing time adds days or weeks to the timeline.

The fix: add "apply for import permit" to the very first step in your planning list for any country that requires one.

## 8. Not checking breed restrictions at the destination

A common scenario: a family relocates with their Rottweiler from the UK to Singapore. Rottweilers are on Singapore's prohibited breeds list. The dog cannot enter.

The fix: before any planning starts, confirm your pet's breed is not restricted at the destination. Check the official government source, not a third-party guide.

## 9. Expired titre test or failing result

For Australia from Group 4 countries, a failing titre test restarts the 180-day clock. For Singapore, an expired titre means the preparation may need to start again.

The fix: use DAFF-approved or SFA-approved labs. Get the titre test done well before it's needed to allow time for a retest if necessary.

## 10. Assuming last year's rules still apply

Pet import regulations change. The USA CDC introduced major changes in 2024. The UK changed AHC requirements post-Brexit. Australia regularly updates approved country groups.

The fix: always check the current official government source before making decisions. Guides and forums can be outdated. The official government portal reflects the current rules.

---

None of these mistakes are difficult to avoid with sufficient lead time and attention to detail. The process is well-documented. The errors that ground pets at airports are almost always avoidable with better planning.
"""
    },
]


# ========================
# Write all articles
# ========================
print(f"Writing {len(ARTICLES)} blog articles...\n")

for article in ARTICLES:
    slug = article["slug"]
    filepath = os.path.join(CONTENT_DIR, f"{slug}.md")

    tags_yaml = "\n".join(f'  - "{t}"' for t in article.get("tags", []))

    md = f"""---
title: "{article['title'].replace('"', "'")}"
description: "{article['description'].replace('"', "'")}"
date: "{article['date']}"
type: "blog"
slug: "{slug}"
url: "/blog/{slug}/"
seo:
  title: "{article['seo_title'].replace('"', "'")} | Pet Transport Global"
  description: "{article['description'].replace('"', "'")}"
tags:
{tags_yaml}
---

{article['content'].strip()}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    word_count = len(article["content"].split())
    print(f"  {slug}.md  — {word_count} words")

print(f"\nDone. {len(ARTICLES)} blog articles written.")
