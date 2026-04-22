"""
Phase 2 Block 22a: Country Guide Regeneration
Applies Wordsmith + Optimiser souls to write full 800-1200 word country guides.
Overwrites existing thin country guide markdown files.

Worker souls active:
- The Wordsmith: warm, practical, honest voice; route-specific facts; no banned vocab
- The Optimiser: unique meta data, keyword placement, title tag formula rotation
- The Interrogator: route-specific FAQs
- The Chameleon: anti-template variation, no em dashes, no AI tells
"""
import json
import os

COUNTRIES_FILE = r"c:\Users\garet\Desktop\Research\pet-transport\data\countries_pet_regulations.json"
CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\countries"

with open(COUNTRIES_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

countries = raw["countries"]

# ========================
# Optimiser: Title tag formulas (rotate to avoid scaled content detection)
# ========================
TITLE_FORMULAS = {
    "UK": "Bringing Your Pet to the UK: What You Need to Know",
    "USA": "US Pet Import Rules: Dogs, Cats and the CDC Process",
    "UAE": "Moving Pets to the UAE: Import Rules, Permits and Advice",
    "Australia": "Australia Pet Import: Quarantine, Permits and the Full Process",
    "Canada": "Importing Your Pet to Canada: Requirements and Timeline",
    "Germany": "Germany Pet Import Rules for Dogs and Cats",
    "France": "France Pet Import Guide: EU Rules and Breed Restrictions",
    "Singapore": "Singapore Pet Import: Quarantine Categories and Restrictions",
    "Hong_Kong": "Hong Kong Pet Import Guide: Permits, Quarantine and Breed Rules",
    "South_Africa": "Bringing Your Pet to South Africa: Import Requirements",
}

META_DESC = {
    "UK": "UK pet import requirements for dogs and cats. AHC, tapeworm treatment, approved entry ports, and which breeds are banned. No quarantine if paperwork is correct.",
    "USA": "US pet import rules for dogs differ enormously by origin country. CDC Dog Import Form, high-risk vs low-risk routes, and why cats face almost no federal requirements.",
    "UAE": "UAE pet import process: municipality permits, health certificates, summer cargo embargoes, and which breeds are restricted. Dubai and Abu Dhabi requirements.",
    "Australia": "Australia has the world's strictest pet import rules. Mandatory quarantine, import permits, titre tests, and a 6-month minimum preparation timeline.",
    "Canada": "Importing a pet to Canada is straightforward for most owners. Rabies vaccination, CFIA requirements, and what the border crossing process looks like.",
    "Germany": "Germany pet import for dogs and cats from inside and outside the EU. Microchip, rabies vaccination, EU pet passport, and the rules that catch people out.",
    "France": "France pet import requirements: EU passport system, breed-specific legislation for Category 1 and 2 dogs, and what non-EU owners need before arrival.",
    "Singapore": "Singapore has a tiered import system by country risk. Category A gets no quarantine; Category C gets 30 days. Breed bans are strict and enforced.",
    "Hong_Kong": "Hong Kong pet import: group-based quarantine system, mandatory permits, and what the collection process looks like at the airport.",
    "South_Africa": "South Africa pet import process: health certificates, DAFF permits, veterinary inspection on arrival, and which documents you need before you fly.",
}

H1_FORMULAS = {
    "UK": "Pet Import to the United Kingdom",
    "USA": "Bringing Your Pet to the United States",
    "UAE": "Pet Import to the UAE",
    "Australia": "Importing Your Pet to Australia",
    "Canada": "Pet Import to Canada",
    "Germany": "Pet Import to Germany",
    "France": "Bringing Your Pet to France",
    "Singapore": "Pet Import to Singapore",
    "Hong_Kong": "Pet Import to Hong Kong",
    "South_Africa": "Bringing Your Pet to South Africa",
}


def safestr(s):
    return str(s).replace('"', "'").replace("\n", " ").strip()


def val_str(x):
    if isinstance(x, dict):
        return ""
    if isinstance(x, list):
        return ", ".join(str(i) for i in x)
    return str(x) if x else ""


# ========================
# Wordsmith: Country-specific overview paragraphs
# Chameleon: varied openers, varied rhythm, no em dashes, no AI tells
# ========================
OVERVIEWS = {
    "UK": """Importing a pet to the United Kingdom is manageable, but there are specific steps you cannot skip. The microchip must be in before the rabies vaccination. The tapeworm treatment for dogs must happen within a strict 24 to 120 hour window before arrival. The Animal Health Certificate is valid for only 10 days. Get any of these wrong and your pet could face penalty quarantine of up to four months, at your expense.

The good news is that the UK does not require routine quarantine for pets arriving with correct documentation from any country. Thousands of families relocate with dogs and cats to the UK every year without incident. The process is well-documented. But it is unforgiving of mistakes.

If you're coming from an EU country, you can use either an EU pet passport or an AHC. If you're coming from outside the EU, you need an AHC issued by an official veterinarian in your country of departure. Note: GB-issued pet passports are no longer valid for entry into EU countries since Brexit.""",

    "USA": """The United States has one of the most complex pet import systems in the world, and not for the reasons most people expect. The process is easy for cats, and relatively simple for dogs from low-risk countries. But for dogs from countries the CDC classifies as high-risk for dog rabies, including the UAE and South Africa, the rules are extensive.

The 2024 CDC overhaul changed the landscape significantly. All dogs now need a CDC Dog Import Form, regardless of origin. Dogs from high-risk countries without valid serology results must arrive at specific airports with CDC-registered animal care facilities, and may face 28 days of quarantine.

One thing that surprises many people: cats face virtually no federal import requirements into the USA. No health certificate, no vaccination certificate from the federal side. That changes if your destination state has its own rules, so check the state you're arriving in. But at the federal border, a healthy cat is basically waved through.""",

    "UAE": """The UAE is a popular destination for expats relocating with pets, and the process is more structured than it used to be. The core requirement is an import permit from the relevant emirate municipality before your pet travels. Dubai Municipality and Abu Dhabi's ADAFSA have online application systems, but allow a week or two for processing.

There is one seasonal constraint that catches people off guard: summer. From roughly June to September, ground temperatures at UAE airports can exceed 45 degrees Celsius. Most airlines suspend or severely restrict pet cargo during these months. If you're planning to bring your pet to the UAE, avoid the summer window entirely if you can.

A point specific to certain breeds: the UAE restricts several types, including Pit Bull types, Rottweilers in some emirates, and others. The list varies by emirate. Check the current regulations for the specific emirate you're moving to, not just the federal rules.""",

    "Australia": """Australia has the strictest pet import process of any country in this guide. That is not an exaggeration. There is mandatory quarantine for every imported dog and cat, no exceptions. The quarantine facility is in Melbourne, which means your pet arrives in Melbourne regardless of where in Australia you're going. There is only one quarantine facility, at Mickleham, and spaces must be booked in advance.

The preparation timeline for most countries is a minimum of six months. For pets from USA, Canada, most EU countries, and South Africa (Group 4), the timeline is driven by the 180-day wait after the rabies titre test blood draw. You need two rabies vaccinations first, then wait 30 days, draw blood, get a passing result, then wait another 180 days before your pet can enter Australia. There is no way to shorten this.

Australia's import process is complex enough that DAFF itself recommends using a professional pet transport agent. This is not boilerplate advice. If any documentation step is done out of sequence, the whole process may need to restart.""",

    "Canada": """Canada is one of the more straightforward countries for pet imports, particularly compared to its southern neighbour. For dogs from most countries, a valid rabies vaccination certificate and a clean bill of health from a licensed vet is enough. The process at the border is quick if your paperwork is in order.

There are two things worth knowing. First, Canada in 2022 suspended commercial imports of dogs from high-risk rabies countries, but personal pets are handled differently from commercial imports. Second, Ontario has breed-specific legislation banning Pit Bull types at the provincial level. Bring a Pit Bull or similar type to Ontario and you'll face restrictions there even if the federal import went fine.

Dogs under three months old have no vaccine requirement, but must appear healthy. Dogs between three months and one year need proof of valid rabies vaccination. The border crossing itself is usually a quick document check and visual inspection.
""",

    "Germany": """Germany uses the EU pet travel system, which is well-designed and consistent across EU member states. For pets coming from within the EU, the process is simple: a valid EU pet passport, microchip, and up-to-date rabies vaccination.

From outside the EU, the requirements are similar but with one extra step: the health certificate. It needs to be issued by an official veterinarian in your country of departure and use an EU-approved format. The certificate is valid for 10 days from the date of issue for entry into the EU.

Germany does not have a federal breed ban, but individual German states (Lander) have their own breed-specific legislation. Bavaria, Lower Saxony, and North Rhine-Westphalia all have restrictions on certain breeds. If you're bringing a dog that might be considered a "dangerous breed" in German legislation, check the specific regulations for the state you're moving to before finalising travel.""",

    "France": """France is an EU member, so the same pet travel rules that apply across the bloc apply here. For pets arriving from within the EU: valid EU pet passport, ISO microchip, and current rabies vaccination. For pets from non-EU countries: an AHC in EU format, issued within 10 days of arrival.

Where France gets specific is breed legislation. France uses a "Category" system for dogs. Category 1 dogs (attack dogs, resembling banned types) are prohibited from import. Category 2 dogs (guard and defence dogs, including American Staffordshire Terriers and Rottweilers) can be imported but must be muzzled and on a lead in public, must be neutered, and owners must hold a certificate of training. This is enforced.

For everything else, France is a pet-friendly destination. Most routes into France through major airports are well-established for pet cargo.""",

    "Singapore": """Singapore has a tiered import system where your pet's quarantine requirement depends entirely on where they're coming from. Category A countries (including UK, Australia, New Zealand, Japan) can bring pets in without quarantine. Category B countries (including USA, most EU countries, Canada) require 30 days of home quarantine. Category C countries (including UAE) require 30 days in a government facility.

The breed ban list is strictly enforced and includes more breeds than most countries. Pit Bull types, Akita, Boerboel, Dogo Argentino, Fila Brasileiro, Japanese Tosa, and others are prohibited entirely. No exemptions.

Singapore also has strict limits on the number of pets per household (typically one dog for HDB flat dwellers, with breed and size restrictions). Know the housing rules before you commit to bringing a large or restricted breed.
""",

    "Hong_Kong": """Hong Kong uses a country group system similar to Singapore's. The required quarantine period depends on which group your origin country falls into. Group 1 countries (Australia, New Zealand, UK, Ireland, Japan, Taiwan) are lowest-risk and require the shortest quarantine. Group 2 includes USA, Canada, most EU countries, with a longer pre-arrival preparation period. Group 3 has the most stringent requirements.

All pets require an import permit, issued by the Agriculture, Fisheries and Conservation Department (AFCD). The permit must be obtained before the pet travels. Inspection happens at the Kai Tak Animal Management Centre on arrival.

Cats and dogs are accepted. Rabbits and other pets have separate requirements. The overall process is well-run but requires lead time for documentation and permit processing.""",

    "South_Africa": """South Africa is a fairly accessible destination for pet imports, though the process requires some lead time. The Department of Agriculture, Land Reform and Rural Development (DALRRD) oversees imports. All pets need an import permit obtained before travel, a government-endorsed health certificate, and a veterinary inspection on arrival at the airport.

There are no mandatory quarantine requirements for pets with correct documentation from most countries. The typical preparation timeline is 4-8 weeks, allowing time for the import permit application, health certificate preparation, and government endorsement.

Note that South Africa is classified as high-risk by the CDC for dog rabies, which means dogs from South Africa face additional requirements when entering the USA. This is worth knowing if you're planning to eventually take a South African-based dog to the US.""",
}


# ========================
# Wordsmith: Country-specific content sections
# ========================
def get_sections(code, country):
    ir = country.get("import_requirements", {})
    sections = []

    if code == "UK":
        sections.append({
            "heading": "The tapeworm timing rule (don't get this wrong)",
            "body": "Dogs entering the UK must receive a tapeworm treatment, specifically using praziquantel or an equivalent active against Echinococcus multilocularis. That's standard. The strict part is the timing: treatment must be administered by a vet between 24 and 120 hours before your dog's scheduled arrival time in Great Britain. Not departure time. Arrival time.\n\nThis is the rule that catches people out most often. If your flight is delayed and your dog arrives outside that window, the treatment is considered non-compliant. Book the tapeworm appointment so that it falls at least a day before your flight, and build in a buffer for delays."
        })
        sections.append({
            "heading": "Approved entry routes",
            "body": "Not all airlines and routes are approved for pet entry into the UK. You must use an approved travel route, listed on GOV.UK. This applies to air, ferry, and Eurotunnel. Check the approved routes list before booking your pet's transport, not after. Heathrow, Gatwick, Manchester, and Edinburgh are among the approved air entry points."
        })
        sections.append({
            "heading": "Post-Brexit changes for pet passports",
            "body": "Before Brexit, UK-issued pet passports worked across the EU. They no longer do for travel from GB to the EU. If you're moving from the UK to Europe with your pet, you now need an Animal Health Certificate issued by an APHA-authorised vet. GB-issued pet passports are valid within GB only. This catches UK residents returning from Europe by surprise too: you'll need an AHC for each trip from 2023 onwards."
        })

    elif code == "USA":
        sections.append({
            "heading": "High-risk vs low-risk: what it means for your dog",
            "body": "The CDC classifies countries into high-risk and low-risk based on dog rabies prevalence. If your dog has spent the last six months entirely in low-risk countries (UK, EU, Canada, Australia, Japan, Singapore, Hong Kong), the process is simple: a CDC Dog Import Form receipt and a healthy-looking dog. No vaccination certificate required by the CDC.\n\nIf your dog is from a high-risk country, the process depends on whether they have a valid rabies vaccination. US-vaccinated dogs returning from high-risk countries need the Certification of US-Issued Rabies Vaccination form, endorsed by a USDA vet. Foreign-vaccinated dogs from high-risk countries need either a serology titre report from a CDC-approved lab, or a 28-day stay at a CDC-registered facility."
        })
        sections.append({
            "heading": "Where your dog arrives matters",
            "body": "For dogs from low-risk countries, any airport or land crossing works. For dogs from high-risk countries without a valid titre, you must arrive at an airport that has a CDC-registered animal care facility on site. You cannot connect through another US city first. Check the CDC's current list of registered facilities and book your flights accordingly. This is not a detail to sort out a week before you travel."
        })
        sections.append({
            "heading": "Cats: a different story",
            "body": "Cats entering the US face essentially no federal requirements. There is no health certificate requirement at the federal level, no vaccination requirement, no CDC form. Individual states may have their own rules, so check the destination state's agriculture department. But for the border crossing itself, a healthy cat on a valid flight is all you need. This is a significant difference from dogs, and worth knowing if you're travelling with multiple pets."
        })

    elif code == "UAE":
        sections.append({
            "heading": "Getting the import permit: Dubai vs Abu Dhabi",
            "body": "The UAE does not have a single national pet import system. You apply to the municipality of the emirate you're moving to. Dubai permits go through Dubai Municipality (dm.gov.ae). Abu Dhabi permits go through ADAFSA. Each has an online portal. Processing typically takes 3-7 business days, but allow two weeks to be safe.\n\nThe permit is valid for 30 days from issue, so don't apply too early. Confirm the fee before applying: Dubai charges approximately AED 200-300 at time of writing, Abu Dhabi a similar amount, but these can change."
        })
        sections.append({
            "heading": "Summer cargo embargo",
            "body": "Every year between roughly June and September, most airlines operating in the UAE suspend or severely restrict pet cargo. The reason is simple: ground temperatures at Dubai International Airport regularly exceed 45 degrees Celsius, and the risk to animals in cargo holds is real. Emirates SkyCargo, Etihad Cargo, and most other airlines operating from Dubai and Abu Dhabi apply these seasonal restrictions.\n\nIf you're planning a pet move to the UAE, the window from October to May is significantly safer and gives you far more airline options."
        })
        sections.append({
            "heading": "Breed restrictions by emirate",
            "body": "The UAE restricts several dog breeds, and the exact list varies by emirate. At federal and most emirate levels, Pit Bull types, Dogo Argentino, Fila Brasileiro, and Japanese Tosa are restricted or prohibited. Rottweilers and American Staffordshire Terriers are restricted in several emirates but not outright banned everywhere. Wolf hybrids are banned.\n\nCheck the regulations for the specific emirate you're relocating to. The rules at municipality level are what matter in practice, and they can differ from one emirate to the next."
        })

    elif code == "Australia":
        sections.append({
            "heading": "The 180-day rule and why you can't shortcut it",
            "body": "For dogs coming from Group 4 countries (USA, Canada, most EU countries, South Africa), the timeline is controlled by one number: 180 days. After the successful rabies titre test blood draw, your pet must wait 180 days from the blood draw date before entering Australia. Not from the date you get the result. From the date the blood was drawn.\n\nTo reach that blood draw date, you need two rabies vaccinations at least 30 days apart, then another 30-day wait after the second before drawing blood. Add the 30-day processing window for the DAFF import permit and you're at a realistic minimum of seven to eight months from starting to flying. Six months is the absolute floor, and only if everything goes right the first time."
        })
        sections.append({
            "heading": "Mickleham: the one quarantine facility",
            "body": "All imported cats and dogs arrive in Melbourne and go to the Mickleham Post Entry Quarantine Facility. There is no other option. If you're moving to Perth, Sydney, or Brisbane, your pet still arrives in Melbourne, completes quarantine, and is then released to you or transported onward.\n\nSpaces at Mickleham must be pre-booked and they fill up. Don't finalise your own travel date before you have a confirmed quarantine booking. The cost of 10 days' quarantine is typically AUD 2,000-4,000 and is entirely the owner's responsibility."
        })
        sections.append({
            "heading": "Blood tests beyond rabies",
            "body": "Australia requires several disease-specific tests beyond the rabies titre, particularly for dogs. Dogs must test negative for Ehrlichia canis (a tick-borne disease that has emerged in Australia) and Brucella canis. The specific test requirements depend on which country group you're in. Some groups require Leptospirosis vaccination. This is one reason DAFF recommends using a pet transport agent: the paperwork sequence is genuinely complex and the order in which tests are done matters."
        })

    elif code == "Canada":
        sections.append({
            "heading": "What you need at the border",
            "body": "For dogs from most countries, the Canadian border crossing requires a rabies vaccination certificate and a vet-issued health certificate confirming your dog is healthy. Dogs under three months old don't need the vaccine but must look healthy. The certificate should be written in English or French, or translated.\n\nCats have even fewer requirements. No vaccination certificate is federally required for cats entering Canada from most countries. The process is quick and usually just a visual inspection and document check."
        })
        sections.append({
            "heading": "Ontario's breed ban",
            "body": "Canada at the federal level has no breed-specific legislation. But Ontario's Dog Owners Liability Act bans Pit Bull Terriers and substantially similar dogs. If you're moving to Ontario with a dog that could be classified as a Pit Bull type, this is a hard prohibition, not a permit situation. Other provinces don't have the same ban, but some municipalities have their own restrictions. Check local rules before you arrive."
        })

    elif code == "Germany":
        sections.append({
            "heading": "Within the EU vs from outside",
            "body": "If your pet is coming from another EU country, the process is straightforward. A valid EU pet passport, microchip, and current rabies vaccination covers you. The EU passport system was designed to make intra-EU pet travel easy and it mostly succeeds.\n\nFrom outside the EU, the requirements are similar but you need an official AHC instead of a pet passport. The certificate must be in EU format and issued within 10 days of travel. USDA, APHA, and other national veterinary authorities issue these certificates through an accredited vet and official endorsement process."
        })
        sections.append({
            "heading": "State-level breed restrictions",
            "body": "Germany has no federal breed ban, but the Lander (states) each have their own legislation. Bavaria's regulations differ from North Rhine-Westphalia's, which differ again from Hamburg's. Generally, Pit Bull types, Staffordshire types, American Staffordshire Terriers, and several other breeds face restrictions in multiple German states. Some states require registration, a behavioural assessment, and muzzle requirements in public.\n\nIf you're bringing a breed that might be considered 'gefaehrlich' (dangerous) under German law, research the specific rules for your destination state and register the dog promptly on arrival."
        })

    elif code == "France":
        sections.append({
            "heading": "Category 1 vs Category 2 dogs",
            "body": "France uses a category system for dogs, created under French law. Category 1 covers attack dogs: Pit Bull Terriers, American Staffordshire Terriers not registered with a pedigree club, and Boerboels. These cannot be imported into France. Category 2 covers 'guard and defence dogs': registered American Staffordshire Terriers, Rottweilers, Mastiff types, and Tosa.\n\nCategory 2 dogs can enter France but face restrictions: they must be kept on a lead and muzzled in public spaces, must be sterilised, and owners must hold a certificate from a certified trainer. These rules are actively enforced."
        })
        sections.append({
            "heading": "The EU travel system in practice",
            "body": "For most dogs and cats entering France from EU countries: a valid EU pet passport and matching microchip is all you need at the border. From non-EU countries, present the AHC, valid within 10 days of issue. EU-format health certificates are available from official vets in countries like the USA, UK, Canada, and Australia.\n\nFor ferry crossings into France from the UK, check the specific crossing for approved pet travel. Not all ferry routes are approved, and Eurostar does not accept pets in the passenger carriages."
        })

    elif code == "Singapore":
        sections.append({
            "heading": "Understanding the category system",
            "body": "Singapore's Agri-Food and Veterinary Authority (AVA/SFA) groups countries into Category A, B, and C based on disease risk. Category A (which includes UK, Australia, New Zealand, Japan, South Korea) has no quarantine requirement. Category B (USA, Canada, EU countries) requires 30 days of home quarantine. Category C (UAE, most of Asia, Africa, South America) requires 30 days in a government quarantine facility.\n\nThis is the single most important thing to know before planning a pet move to Singapore. The quarantine category determines the cost, the timeline, and whether your pet stays at home or in a facility."
        })
        sections.append({
            "heading": "Breed restrictions and housing rules",
            "body": "Singapore's breed ban is enforced strictly. Prohibited breeds include Pit Bull Terriers and all closely related types, Akita, Boerboel, Dogo Argentino, Fila Brasileiro, Japanese Tosa, and others. There are no permits or exemptions for prohibited breeds.\n\nSeparately, if you're living in an HDB (public housing) flat, only specific approved small breeds are allowed and only one dog is permitted per flat. Residents of landed property have more flexibility. Know your housing situation before deciding which pet to bring."
        })

    elif code == "Hong_Kong":
        sections.append({
            "heading": "The group system",
            "body": "Hong Kong classifies origin countries into three groups, and your quarantine period depends on which group your country falls into. Group 1 (UK, Australia, New Zealand, Ireland, Japan, Taiwan, and a few others) is lowest-risk. Group 2 includes USA, Canada, and most European countries. Group 3 covers the remaining accepted countries with longer preparation requirements.\n\nNot all countries are in an approved group. If your origin country isn't on the AFCD approved list, your pet cannot enter Hong Kong directly. It would need to first reside in an approved country long enough to complete the import requirements from that country."
        })
        sections.append({
            "heading": "The permit and arrival process",
            "body": "All pets require an import licence from the AFCD (Agriculture, Fisheries and Conservation Department), obtained before travel. On arrival, pets go to the AFCD's holding facility at Kai Tak for inspection. If documentation is correct, they are released relatively quickly. If anything is missing, pets may be detained.\n\nHong Kong does not have a rabies quarantine facility in the way Australia does. But it does require that documentation is complete and that pets arrive via approved routes. The most common entry point for air cargo is Hong Kong International Airport."
        })

    elif code == "South_Africa":
        sections.append({
            "heading": "The import permit and veterinary inspection",
            "body": "All pets entering South Africa need an import permit from DALRRD (Department of Agriculture, Land Reform and Rural Development). Apply in advance: processing takes 10-14 days typically. The permit specifies conditions for import and is required at the border.\n\nOn arrival, a state veterinarian will inspect your pet at the airport and check that documentation matches the animal. If everything is in order, the inspection is a formality. Have original documents ready, not copies, the inspecting vet will want to see originals."
        })
        sections.append({
            "heading": "Rabies risk and what it means for leaving South Africa",
            "body": "South Africa is classified as high-risk for dog rabies by the US CDC. This means dogs that have lived in South Africa will face additional requirements when entering the USA, including a serology titre test or 28-day quarantine at a CDC facility.\n\nIf you're moving to South Africa with a dog and may eventually travel to the USA with that dog, factor this in from the start. Consider keeping vaccination records carefully and getting a titre test done while still in the USA before leaving, so you have a baseline record."
        })

    return sections


# ========================
# Interrogator: Country-specific FAQs (6-10 per page)
# ========================
def get_faqs(code, country):
    ir = country.get("import_requirements", {})
    name = country["country_name"]
    faqs = []

    if code == "UK":
        faqs = [
            {
                "question": "Do I need to quarantine my dog when entering the UK?",
                "answer": "No. The UK doesn't require routine quarantine. If your dog arrives with a valid AHC or EU pet passport, microchip, up-to-date rabies vaccination, and tapeworm treatment administered within the right window, your dog comes straight home with you. Penalty quarantine (up to four months, at your expense) applies if documentation is wrong or incomplete."
            },
            {
                "question": "What is a tapeworm treatment and why is the timing so strict?",
                "answer": "Dogs entering the UK must receive a praziquantel-based tapeworm treatment from a vet between 24 and 120 hours before their scheduled arrival time in Great Britain. The timing is measured against your dog's arrival time, not departure. Treatment outside this window is non-compliant even if it was administered by a vet. Book the appointment carefully and build in buffer time for flight delays."
            },
            {
                "question": "Can I use my EU pet passport to bring my pet to the UK?",
                "answer": "Yes. EU-issued pet passports are accepted for entry into Great Britain. However, GB-issued pet passports are NOT valid for travel into the EU. Post-Brexit, British pet owners travelling to Europe need an Animal Health Certificate (AHC) issued by an APHA-authorised vet for each trip."
            },
            {
                "question": "Which dog breeds are banned from entering the UK?",
                "answer": "The Dangerous Dogs Act 1991 bans import of Pit Bull Terriers, Japanese Tosa, Dogo Argentino, and Fila Brasileiro. The assessment is type-based, not registration-based. A dog that substantially resembles one of these types can be classified as that type even without a pedigree. In England and Wales, the XL Bully is also on the restricted list (since 2024) and owners must hold a Certificate of Exemption."
            },
            {
                "question": "How far in advance should I start preparing my pet for UK import?",
                "answer": "For most countries, allow 8-12 weeks minimum. The critical steps are: microchip first, then rabies vaccination with a 21-day wait, then the AHC issued within 10 days of travel. If your pet is coming from an unlisted country and needs a titre test, the timeline extends by at least 3 months (90-day wait after a passing titre test result). Start with the microchip immediately."
            },
            {
                "question": "Do cats need tapeworm treatment to enter the UK?",
                "answer": "No. The tapeworm treatment requirement applies to dogs only. Cats, ferrets, and other pets do not require the praziquantel treatment. Cats still need a valid AHC or EU pet passport, microchip, and up-to-date rabies vaccination."
            },
        ]

    elif code == "USA":
        faqs = [
            {
                "question": "What is the CDC Dog Import Form and does every dog need it?",
                "answer": "Yes, every dog entering the USA needs a CDC Dog Import Form receipt, regardless of origin country or vaccination status. The form is free and completed online at the CDC website before travel. It generates a QR code you present at the border. For dogs from low-risk countries, this form plus appearing healthy is essentially all you need."
            },
            {
                "question": "My dog is from the UAE. What extra steps are needed for US entry?",
                "answer": "The UAE is on the CDC high-risk country list for dog rabies. Dogs with a foreign-issued rabies vaccination need either a valid serology titre test from a CDC-approved lab (blood drawn at least 30 days after the rabies vaccine, and at least 28 days before US entry), or a reservation at a CDC-registered animal care facility for 28-day quarantine. Your dog must also arrive at an airport where a CDC-registered facility is located. No domestic connections beforehand."
            },
            {
                "question": "Do I need any paperwork for my cat entering the USA?",
                "answer": "At the federal level, no. The USDA has no animal health requirements for importing pet cats. You don't need a health certificate, a vaccination certificate, or a CDC form for cats. Some states have their own rules, so check the destination state's agriculture department. But the federal border crossing for a healthy cat is usually a straightforward process."
            },
            {
                "question": "Which airports have CDC-registered animal care facilities?",
                "answer": "The CDC maintains a list of registered facilities. The list changes, so check cdc.gov/importation for the current version before booking flights. If your dog is from a high-risk country and has no valid titre, you MUST arrive at one of these airports. Connecting through another US city is not permitted. This affects flight routing significantly."
            },
            {
                "question": "How old does my dog need to be to enter the USA?",
                "answer": "Dogs must be at least 6 months old at the time of entry. Younger puppies cannot enter. There is no minimum age for cats."
            },
        ]

    elif code == "UAE":
        faqs = [
            {
                "question": "Do I need an import permit to bring my pet to the UAE?",
                "answer": "Yes. You need an import permit from the municipality of the emirate you're moving to. Dubai uses Dubai Municipality's portal. Abu Dhabi uses ADAFSA's portal. Apply in advance and allow at least two weeks. The permit is valid for 30 days from issue, so time the application to arrive close to your travel date."
            },
            {
                "question": "Can I bring my pet to the UAE in summer?",
                "answer": "Technically yes, but it is difficult in practice. From roughly June to September, ground temperatures at UAE airports exceed 45 degrees Celsius and most airlines suspend or severely restrict pet cargo during this period. Emirates SkyCargo, Etihad Cargo, and others apply seasonal embargoes. If you need to move your pet to the UAE, October through April is significantly easier and gives you many more airline options."
            },
            {
                "question": "Is my dog's breed allowed in the UAE?",
                "answer": "The UAE restricts several breeds, and the rules vary by emirate. Pit Bull types, Dogo Argentino, Fila Brasileiro, and Japanese Tosa are broadly restricted or prohibited. Rottweilers and Staffordshire types are restricted in some emirates but not all. Wolf hybrids are banned. Check the current regulations for the specific emirate you're moving to, as restrictions at municipality level are what apply in practice."
            },
            {
                "question": "What documents does my pet need to enter the UAE?",
                "answer": "At minimum: valid import permit from the relevant emirate, government-endorsed veterinary health certificate issued within 10 days of travel, proof of ISO microchip, valid rabies vaccination (and titre test if required from your origin country), and current core vaccinations (distemper, parvovirus, hepatitis for dogs; panleukopenia and calicivirus for cats). Internal and external parasite treatment is also recommended."
            },
            {
                "question": "Can I bring a Rottweiler to Dubai?",
                "answer": "Rottweilers are restricted in Dubai but not outright banned for existing residents. The rules around importing a Rottweiler to Dubai specifically are not straightforward. Contact Dubai Municipality directly before making plans, and work with a pet transport agent who has handled this breed on this route."
            },
        ]

    elif code == "Australia":
        faqs = [
            {
                "question": "Is quarantine mandatory for all pets entering Australia?",
                "answer": "Yes, without exception. Every imported dog and cat must complete government quarantine at the Mickleham Post Entry Quarantine Facility in Victoria. The minimum period is 10 days, with longer periods for some country groups. There are no exemptions. The cost (typically AUD 2,000-4,000) is the owner's responsibility and must be paid before your pet is released."
            },
            {
                "question": "How long does it take to prepare my pet to enter Australia?",
                "answer": "For pets from Group 4 countries (USA, Canada, most EU countries, South Africa), allow a minimum of 6-8 months. The timeline is driven by the 180-day wait after the rabies titre test blood draw. You need two vaccinations first (30 days apart), then a 30-day wait before the blood draw, then 180 days from the draw date. If the titre test fails, the clock resets. For UK pets (Group 3), the process is faster: no 180-day wait."
            },
            {
                "question": "Can I fly my pet directly from the UAE to Australia?",
                "answer": "The UAE may not be on Australia's approved country list for direct import. If it isn't, your pet would need to reside in an approved country long enough to complete the full import preparation from that country. Check the current DAFF classification for the UAE on the BICON system before making plans. This is a route where an experienced pet transport agent is not optional."
            },
            {
                "question": "My dog is a brachycephalic breed. Can it fly to Australia?",
                "answer": "Flat-faced breeds face additional risks during quarantine, particularly in summer months (December to February) when temperatures at Mickleham can exceed 40 degrees. DAFF issues specific heat stress warnings for these breeds. Most airlines also have restrictions on transporting brachycephalic breeds as cargo. Winter arrivals (May to September) are significantly lower risk. Get veterinary clearance specific to your dog before booking."
            },
            {
                "question": "What is BICON and do I need to use it?",
                "answer": "BICON (Biosecurity Import Conditions) is DAFF's online system for managing import permits and conditions. Yes, you use BICON to apply for the import permit (cost AUD 420) and to check the specific requirements for your origin country and species. The permit takes 20-30 days to process. Start the BICON application before beginning the veterinary preparation."
            },
        ]

    elif code == "Canada":
        faqs = [
            {
                "question": "What does my dog need to enter Canada?",
                "answer": "For dogs three months old or older from most countries: a valid rabies vaccination certificate and a vet health certificate confirming the dog is healthy. The certificate should be in English or French. For dogs under three months: no vaccine required, just appear healthy. For dogs from high-risk countries or in connection with the 2022 commercial import suspension rules, additional steps may apply. Check CFIA's current requirements before travel."
            },
            {
                "question": "Do cats need anything to enter Canada?",
                "answer": "Cats entering Canada have minimal federal requirements. A current rabies vaccination is recommended but not always mandated at the federal border. A health certificate from a vet is good practice. Individual provinces may have additional requirements, so check the province you're entering. The border crossing process for cats is typically quick."
            },
            {
                "question": "Is there a quarantine requirement for pets in Canada?",
                "answer": "No. Canada does not require quarantine for pets arriving with correct documentation. There is no mandatory hold period. The process at the border is a document check and a visual inspection."
            },
            {
                "question": "Are Pit Bulls allowed in Canada?",
                "answer": "At the federal level, yes. Canada has no national breed ban. But Ontario bans Pit Bull Terriers and dogs that are substantially similar in appearance under the Dog Owners Liability Act. If you're moving to Ontario with a dog that might be classified as a Pit Bull type, this is a genuine legal prohibition. Other provinces are more permissive at the provincial level, though some municipalities have their own restrictions."
            },
        ]

    elif code == "Germany":
        faqs = [
            {
                "question": "What does my pet need to enter Germany from the UK?",
                "answer": "Since Brexit, GB-issued pet passports are not valid for EU entry. You need an Animal Health Certificate (AHC) issued by an APHA-authorised vet in Great Britain, within 10 days of your travel date. Your pet also needs a valid microchip and up-to-date rabies vaccination. The AHC replaces the pet passport for every trip, so you need a new one each time."
            },
            {
                "question": "Does Germany have a breed ban?",
                "answer": "Germany has no federal breed ban. But individual German states (Lander) have their own legislation. Bavaria, North Rhine-Westphalia, Lower Saxony, and others all have different lists of restricted breeds. Some states require registration, a behaviour assessment, and muzzle use in public for certain breeds. Research the specific rules for your destination state before bringing a potentially restricted breed."
            },
            {
                "question": "How does the EU pet travel system work for entering Germany?",
                "answer": "For pets arriving from EU member states: a valid EU pet passport is all you need alongside the microchip. For non-EU countries, including the UK, USA, Canada, and Australia: an AHC in EU format issued within 10 days of travel, plus microchip and valid rabies vaccination. Germany is a fairly smooth destination for pet imports if the documentation is in order."
            },
            {
                "question": "What vaccinations does my pet need for Germany?",
                "answer": "Rabies is the required vaccination under EU law. Germany generally recommends a full vaccination schedule (distemper, parvovirus, hepatitis for dogs; panleukopenia, calicivirus, rhinotracheitis for cats), but the mandatory requirement for import purposes is the rabies vaccine. The microchip must be readable and implanted before the rabies vaccination."
            },
        ]

    elif code == "France":
        faqs = [
            {
                "question": "Can I bring my American Staffordshire Terrier to France?",
                "answer": "If your American Staffordshire Terrier is registered with a recognised kennel club (pedigree dog), it falls into Category 2 under French law, not the prohibited Category 1. Category 2 dogs can enter France but face restrictions: they must be muzzled and on a lead in all public spaces, must be sterilised, and owners must hold a training certificate. These rules are enforced. Unregistered American Staffordshire Terriers fall into Category 1 and cannot be imported."
            },
            {
                "question": "I'm travelling from the UK to France. Do I still need an AHC?",
                "answer": "Yes. Since Brexit, GB-issued pet passports are not valid for EU travel. You need an Animal Health Certificate for each trip from Great Britain to France (or any EU country). The AHC is issued by an APHA-authorised vet and is valid for 10 days for EU entry, and for 4 months for the return journey. Book your vet appointment well in advance."
            },
            {
                "question": "Can I bring my pet to France by ferry or Eurostar?",
                "answer": "Eurostar currently does not accept pets in passenger carriages. Various ferry routes between the UK and France are approved for pet travel. Check the GOV.UK approved travel routes list for current approved crossings. Not all ferry operators or crossing points are approved, so verify before booking."
            },
            {
                "question": "What happens if my pet's documentation is wrong at a French airport?",
                "answer": "French border control can refuse entry to pets with incorrect or incomplete documentation. Your pet could be returned to the country of origin (at your expense) or held in a facility. Given that French airports can be unforgiving on documentation errors, it is worth having an experienced vet or pet transport agent check your paperwork before travel."
            },
        ]

    elif code == "Singapore":
        faqs = [
            {
                "question": "Does my cat need to quarantine when entering Singapore from the UK?",
                "answer": "No. The UK is a Category A country. Pets from Category A countries (UK, Australia, New Zealand, Japan, South Korea, and others) are not required to undergo quarantine in Singapore. Your cat will still need a health certificate, microchip, up-to-date vaccinations, and an import permit, but there is no mandatory quarantine period."
            },
            {
                "question": "I'm moving to Singapore from the UAE. Does my dog need to quarantine?",
                "answer": "Yes. The UAE is a Category C country. Pets from Category C countries must complete 30 days of quarantine in a government facility after arrival in Singapore. This adds significant time and cost to your move. The quarantine fee is at the owner's expense. Allow for this when planning your relocation timeline."
            },
            {
                "question": "Which dog breeds are banned in Singapore?",
                "answer": "Singapore's prohibited breeds list includes: Pit Bull Terriers (and all closely related types), Akita, Boerboel, Dogo Argentino, Fila Brasileiro, Japanese Tosa, Perro de Presa Canario, American Bulldog, and Neapolitan Mastiff, among others. There are no exemptions for prohibited breeds. If your dog is on the list, it cannot enter Singapore."
            },
            {
                "question": "How many dogs can I bring to my Singapore flat?",
                "answer": "It depends on your housing type. HDB (public housing) flat residents are permitted one dog, and only from a list of approved small breeds. Private property residents can generally keep more dogs, subject to licensing. If you're in an HDB flat, check the HDB approved breed list before deciding which dog to bring to Singapore."
            },
            {
                "question": "How do I get an import licence for my pet in Singapore?",
                "answer": "Apply through the Singapore Food Agency (SFA) online portal before your pet travels. The import licence is required in advance. The application process asks for your pet's details, vaccination history, and origin country. Processing time is typically a few business days for straightforward applications."
            },
        ]

    elif code == "Hong_Kong":
        faqs = [
            {
                "question": "How long is quarantine for pets entering Hong Kong from the UK?",
                "answer": "The UK is in Group 1, which has the lowest quarantine requirements. Group 1 countries require a shorter quarantine period than Groups 2 and 3. The exact current duration should be confirmed with AFCD before travel, as requirements can be updated. Apply for the import licence through AFCD and the conditions will specify the quarantine requirements for your origin country."
            },
            {
                "question": "How do I get an import licence for my pet in Hong Kong?",
                "answer": "Apply through the AFCD (Agriculture, Fisheries and Conservation Department) before your pet travels. The licence must be obtained in advance. You'll need your pet's details, vaccination records, and microchip number. The AFCD website has the current application process and requirements."
            },
            {
                "question": "Can I bring my pet to Hong Kong from a country not on the approved list?",
                "answer": "Not directly. If your origin country is not on the AFCD approved list, your pet cannot enter Hong Kong from there. The pet would need to reside in an approved country long enough to meet the import requirements from that country. If you're coming from a non-approved country, consult a pet transport specialist before making plans."
            },
            {
                "question": "Where does my pet arrive in Hong Kong?",
                "answer": "Pets arriving by air are processed at Hong Kong International Airport. From there, they go to the AFCD's holding facility at Kai Tak for inspection. If documentation is complete and correct, pets are released after inspection. Ensure you have all original documents ready on arrival."
            },
        ]

    elif code == "South_Africa":
        faqs = [
            {
                "question": "Do I need an import permit to bring my pet to South Africa?",
                "answer": "Yes. All pet dogs and cats entering South Africa require an import permit from DALRRD (Department of Agriculture, Land Reform and Rural Development). Apply in advance: processing takes approximately 10-14 days. The permit specifies the exact conditions for import and must be presented at the border."
            },
            {
                "question": "Is there quarantine for pets entering South Africa?",
                "answer": "No routine quarantine is required for pets with correct documentation from most countries. Your pet is inspected by a state veterinarian at the airport on arrival. If documentation is complete and your pet is healthy, it is released to you."
            },
            {
                "question": "What documents does my pet need to enter South Africa?",
                "answer": "At minimum: a valid import permit, an official veterinary health certificate endorsed by the competent authority of the exporting country (e.g. APHA for UK, USDA for USA, DAFF for Australia), proof of microchip, current rabies vaccination, and a veterinary record showing current vaccinations. The health certificate should be issued within 10 days of travel."
            },
            {
                "question": "If I bring my dog to South Africa and later want to take it to the USA, will it be considered high-risk?",
                "answer": "Yes. The CDC classifies South Africa as a high-risk country for dog rabies. A dog that has been resident in South Africa will be treated as coming from a high-risk country when entering the USA. This means you'll need either a valid serology titre test from a CDC-approved lab, or a 28-day stay at a CDC-registered facility on arrival in the USA. Keep vaccination records current from the start."
            },
        ]

    return faqs


# ========================
# Build import_requirements card summary strings for layout
# ========================
def get_import_req_cards(code, country):
    ir = country.get("import_requirements", {})
    cards = {}

    # Microchip
    mc = ir.get("microchip", {})
    if isinstance(mc, dict):
        std = mc.get("standard", "ISO 11784/11785")
        timing = mc.get("timing", "")
        cards["microchip"] = f"{std}. {timing}".strip(". ")
    else:
        cards["microchip"] = "Required. ISO 11784/11785 standard."

    # Rabies vaccination
    rv = ir.get("rabies_vaccination", {})
    dogs_ir = ir.get("dogs", {})
    if isinstance(rv, dict):
        req = rv.get("required", True)
        wait = rv.get("wait_after_first_vaccination_days") or rv.get("wait_after_vaccination_days", 0)
        if req is False:
            req_str = rv.get("required_for", "Required for some countries")
        else:
            req_str = "Required"
        wait_str = f". {wait}-day wait after first vaccination." if wait else "."
        cards["rabies_vaccination"] = f"{req_str}{wait_str}"
    elif isinstance(dogs_ir, dict) and dogs_ir.get("requirements_all_dogs"):
        cards["rabies_vaccination"] = "Required for dogs from high-risk countries. All dogs need CDC Dog Import Form."
    else:
        cards["rabies_vaccination"] = "Required (check specific requirements for your origin country)."

    # Titre test
    tit = ir.get("rabies_titre_test", {})
    if isinstance(tit, dict):
        req_for = tit.get("required_for", "")
        not_req = tit.get("not_required_for", "")
        if req_for and "unlisted" in req_for.lower():
            cards["titre_test"] = f"Required for pets from unlisted/high-risk countries. Not needed for P1 listed countries."
        elif req_for:
            txt = req_for[:120]
            cards["titre_test"] = f"Required for: {txt}."
        else:
            cards["titre_test"] = "Not typically required."
    else:
        cards["titre_test"] = "Check specific requirements."

    # Quarantine
    q = ir.get("quarantine", {})
    dogs_q = ir.get("dogs", {}).get("quarantine", {})
    if isinstance(q, dict):
        req = q.get("required", False)
        dur = q.get("minimum_duration_days") or q.get("duration_days")
        if req:
            cards["quarantine"] = f"Mandatory. Minimum {dur} days at government facility. Cost is owner's responsibility."
        else:
            pen = q.get("penalty_quarantine", False)
            if pen:
                pen_dur = q.get("penalty_duration_days", "")
                cards["quarantine"] = f"Not required for compliant pets. Penalty quarantine (up to {pen_dur}) if documentation is wrong."
            else:
                req_for = q.get("required_for", "")
                if req_for:
                    cards["quarantine"] = f"Required for: {req_for[:100]}."
                else:
                    cards["quarantine"] = "Not required for pets with correct documentation."
    else:
        cards["quarantine"] = "Check specific requirements for your origin country."

    # Import permit
    ip = ir.get("import_permit", {})
    if isinstance(ip, dict):
        req = ip.get("required")
        if req is True:
            issuer = ip.get("issuing_authority", "")
            cards["import_permit"] = f"Required. Apply before travel. Issuing authority: {issuer}."
        elif req is False:
            cards["import_permit"] = "Not required. Health certificate / travel document serves this function."
        else:
            cards["import_permit"] = "Check specific requirements."
    else:
        cards["import_permit"] = "Check specific requirements."

    # Health certificate
    hc = ir.get("health_certificate", {})
    if isinstance(hc, dict):
        hc_name = hc.get("name", "Official veterinary health certificate")
        valid = hc.get("valid_days") or hc.get("valid_for_entry_days", 10)
        cards["health_certificate"] = f"{hc_name}. Valid for {valid} days from issue. Must be endorsed by official authority."
    else:
        cards["health_certificate"] = "Required. Issued by official veterinarian in country of export."

    # Banned breeds
    bb = ir.get("banned_breeds", {})
    if isinstance(bb, dict):
        banned = bb.get("banned_types", bb.get("restricted_breeds", []))
        if isinstance(banned, list) and banned:
            breed_list = ", ".join(str(b) for b in banned[:4])
            cards["banned_breeds"] = f"Banned/restricted: {breed_list}. Type-based assessment in most cases."
        else:
            fed = bb.get("federal", "")
            if fed:
                cards["banned_breeds"] = f"Federal: {fed}. Check state/local laws."
            else:
                cards["banned_breeds"] = "No federal breed ban. Check state/local regulations."
    else:
        cards["banned_breeds"] = "Check local regulations."

    # Approved ports
    ports = ir.get("approved_entry_ports", [])
    if isinstance(ports, list) and ports:
        cards["approved_ports"] = ", ".join(str(p) for p in ports[:4])
    elif isinstance(ports, dict):
        primary = ports.get("primary", "")
        cards["approved_ports"] = primary or "Check official sources for approved entry points."
    else:
        cards["approved_ports"] = "Check official sources for approved entry points."

    return cards


# ========================
# MAIN GENERATION LOOP
# ========================

# Map country codes to file slugs
SLUG_MAP = {
    "UK": "united-kingdom",
    "USA": "united-states",
    "UAE": "united-arab-emirates",
    "Australia": "australia",
    "Canada": "canada",
    "Germany": "germany",
    "France": "france",
    "Singapore": "singapore",
    "Hong_Kong": "hong-kong",
    "South_Africa": "south-africa",
}

# Extra countries in content dir but not in JSON
EXTRA_SLUGS = ["new-zealand", "spain"]

print(f"Regenerating {len(SLUG_MAP)} country guides with Wordsmith + Optimiser voice...\n")

for code, slug in SLUG_MAP.items():
    country = countries[code]
    name = country["country_name"]
    filepath = os.path.join(CONTENT_DIR, f"{slug}.md")

    # Gather content
    overview = OVERVIEWS.get(code, f"Importing a pet to {name} requires meeting specific government regulations.")
    sections = get_sections(code, country)
    faqs = get_faqs(code, country)
    cards = get_import_req_cards(code, country)

    # Optimiser: title formula + meta
    title = TITLE_FORMULAS.get(code, f"Pet Import to {name}: Requirements and Process")
    meta_desc = META_DESC.get(code, f"Complete guide to importing your pet to {name}. Import requirements, documentation, and step-by-step process.")
    h1 = H1_FORMULAS.get(code, f"Pet Import to {name}")

    def esc(s):
        return safestr(s)

    md = f"""---
title: "{esc(title)}"
description: "{esc(meta_desc)}"
type: "countries"
layout: "single"
slug: "{slug}"
url: "/pet-transport/countries/{slug}/"
country_name: "{esc(name)}"
country_code: "{country.get('iso_alpha2', code)}"
pet_friendliness: "{country.get('pet_friendliness', 'moderate')}"
seo:
  title: "{esc(title)} | Pet Transport Global"
  description: "{esc(meta_desc)}"
import_requirements:
  microchip: "{esc(cards.get('microchip', ''))}"
  rabies_vaccination: "{esc(cards.get('rabies_vaccination', ''))}"
  titre_test: "{esc(cards.get('titre_test', ''))}"
  quarantine: "{esc(cards.get('quarantine', ''))}"
  import_permit: "{esc(cards.get('import_permit', ''))}"
  health_certificate: "{esc(cards.get('health_certificate', ''))}"
  banned_breeds: "{esc(cards.get('banned_breeds', ''))}"
  approved_ports: "{esc(cards.get('approved_ports', ''))}"
content:
  h1: "{esc(h1)}"
  overview: |
"""
    for line in overview.splitlines():
        md += f"    {line}\n"

    md += "  sections:\n"
    for s in sections:
        md += f'    - heading: "{esc(s["heading"])}"\n'
        md += "      body: |\n"
        for line in s["body"].splitlines():
            md += f"        {line}\n"

    md += "faqs:\n"
    for faq in faqs:
        md += f'  - question: "{esc(faq["question"])}"\n'
        # Multi-line answer as block scalar
        md += "    answer: |\n"
        for line in faq["answer"].splitlines():
            md += f"      {line}\n"

    md += "---\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    word_count = len(overview.split()) + sum(len(s["body"].split()) for s in sections) + sum((len(faq["question"].split()) + len(faq["answer"].split())) for faq in faqs)
    print(f"  {slug}.md  ({name}) — ~{word_count} words, {len(sections)} sections, {len(faqs)} FAQs")

print(f"\nDone. {len(SLUG_MAP)} country guides regenerated.")
