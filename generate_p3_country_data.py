"""
generate_p3_country_data.py
Phase 3.1 — Add 25 P3 countries to countries_pet_regulations.json

Countries added:
Ireland, Norway, Sweden, Austria, Belgium, Poland, Turkey, Israel,
Saudi Arabia, Qatar, Kuwait, China, Taiwan, Vietnam, Sri Lanka,
Argentina, Chile, Colombia, Egypt, Kenya, Nigeria, Czech Republic,
Romania, Malta, Cyprus

Sources cited per official government portals.
Run from repo root: python generate_p3_country_data.py
"""

import json
from pathlib import Path
from datetime import date

DATA_FILE = Path("data/countries_pet_regulations.json")

P3_COUNTRIES = {

    "Ireland": {
        "country_name": "Ireland",
        "iso_alpha2": "IE",
        "iso_alpha3": "IRL",
        "region": "Europe",
        "subregion": "Northern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Ireland uses the EU pet travel scheme. Part 1 listed country for UK entry. Large population of pets moving between Ireland, UK, and Europe.",
        "official_source": "Department of Agriculture, Food and the Marine (DAFM) — gov.ie/en/organisation/department-of-agriculture-food-and-the-marine/",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted before or on same day as rabies vaccination",
                "non_iso_accepted": False,
                "notes": "Microchip must be readable and match all documents."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0,
                "vaccine_type": "Inactivated or recombinant, EU-approved",
                "notes": "21-day wait from first vaccination. Boosters given in-time have no additional wait."
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-EU/non-listed countries",
                "not_required_for": "Pets from EU member states and approved listed countries",
                "test_type": "FAVN or ELISA at EU-approved lab",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90,
                "notes": "Blood drawn at least 30 days after rabies vaccination. 3-month wait after successful result before entry."
            },
            "quarantine": {
                "required": False,
                "penalty_quarantine": True,
                "penalty_duration_days": "Determined by DAFM",
                "penalty_trigger": "Non-compliant documentation or vaccination records",
                "notes": "No routine quarantine for compliant pets from listed/EU countries."
            },
            "import_permit": {
                "required": False,
                "notes": "EU Pet Passport or Animal Health Certificate (AHC) serves as the travel document. No separate import permit needed."
            },
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or Animal Health Certificate (AHC)",
                "issued_by": "Official or authorised veterinarian",
                "valid_for_entry_days": 10,
                "notes": "EU pet passport valid indefinitely as long as vaccinations are current. AHC valid 10 days for entry."
            },
            "tapeworm_treatment": {
                "required_for": "Dogs entering from UK (Great Britain)",
                "not_required_for": "Cats, ferrets, dogs from EU",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel (effective against Echinococcus multilocularis)",
                "notes": "Required for dogs entering Ireland from Great Britain. Record must be in pet passport or AHC."
            },
            "banned_breeds": {
                "legislation": "Control of Dogs Regulations 1998 (Ireland)",
                "restricted_breeds": [
                    "American Pit Bull Terrier",
                    "English Bull Terrier",
                    "Staffordshire Bull Terrier",
                    "Bull Mastiff",
                    "Dobermann Pinscher",
                    "German Shepherd",
                    "Japanese Akita",
                    "Japanese Tosa",
                    "Rottweiler",
                    "Rhodesian Ridgeback"
                ],
                "restrictions": "Listed breeds and their crosses must be kept on a strong lead and muzzled in public. Not banned from import but owner liable for compliance.",
                "notes": "Ireland does not ban import of these breeds but they are restricted in public. Check local council rules."
            }
        },
        "export_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "notes": "Valid, current vaccination required for health certificate."},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official veterinarian registered with DAFM",
                "notes": "EU pets can use existing EU passport. Non-EU destinations require destination-country AHC."
            },
            "export_permit": {"required": False, "notes": "No export permit required for pet cats and dogs."},
            "tapeworm_treatment": {
                "required_for": "Dogs travelling to UK (Great Britain)",
                "notes": "Required by UK (APHA). Must be done by vet and recorded."
            }
        },
        "key_contacts": {
            "authority": "DAFM — Veterinary Policy, Trade and Laboratory Division",
            "website": "gov.ie",
            "email": "animalhealthcert@agriculture.gov.ie"
        }
    },

    "Norway": {
        "country_name": "Norway",
        "iso_alpha2": "NO",
        "iso_alpha3": "NOR",
        "region": "Europe",
        "subregion": "Northern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EEA/Schengen member but not EU. Norway follows EU pet travel rules for dogs, cats, and ferrets. Part 1 listed country for UK entry.",
        "official_source": "Norwegian Food Safety Authority (Mattilsynet) — mattilsynet.no",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination",
                "non_iso_accepted": False,
                "notes": "ISO microchip mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0,
                "vaccine_type": "Inactivated or recombinant, approved vaccine",
                "notes": "Same rules as EU. 21-day wait after first primary vaccination."
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "Pets from EU member states and listed countries (UK, etc.)",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90,
                "notes": "3-month waiting period after titre test before travel to Norway."
            },
            "quarantine": {
                "required": False,
                "penalty_quarantine": True,
                "penalty_trigger": "Non-compliant documentation",
                "notes": "No routine quarantine for pets arriving with correct documents."
            },
            "import_permit": {
                "required": False,
                "notes": "No import permit needed for compliant pets from listed countries."
            },
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official veterinarian",
                "valid_for_entry_days": 10,
                "notes": "EU pet passport or AHC accepted."
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from all countries outside Norway",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel",
                "notes": "Required for all dogs entering Norway. Must be recorded in pet travel document."
            },
            "banned_breeds": {
                "legislation": "Norwegian Animal Welfare Act",
                "banned_types": ["Pit Bull Terrier"],
                "notes": "Pit Bull Terrier is banned in Norway. Other breeds may face restrictions."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU-format AHC",
                "issued_by": "Official vet (Mattilsynet-authorised)",
                "notes": "Norway follows EU health certificate formats for export."
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "Mattilsynet (Norwegian Food Safety Authority)",
            "website": "mattilsynet.no",
            "phone": "+47 22 40 00 00"
        }
    },

    "Sweden": {
        "country_name": "Sweden",
        "iso_alpha2": "SE",
        "iso_alpha3": "SWE",
        "region": "Europe",
        "subregion": "Northern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Sweden follows standard EU pet travel rules. No routine quarantine for compliant pets.",
        "official_source": "Swedish Board of Agriculture (Jordbruksverket) — jordbruksverket.se",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination",
                "notes": "ISO standard mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0,
                "notes": "21-day wait from primary vaccination."
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {
                "required": False,
                "penalty_quarantine": True,
                "notes": "No routine quarantine. Penalty quarantine for non-compliance."
            },
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from non-EU/non-listed countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel",
                "notes": "Check Jordbruksverket list. Required when arriving from echinococcosis-endemic areas."
            },
            "banned_breeds": {
                "legislation": "Sweden has no breed-specific legislation",
                "banned_types": [],
                "notes": "No breed bans in Sweden. All breeds permitted."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official veterinarian"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "Jordbruksverket (Swedish Board of Agriculture)",
            "website": "jordbruksverket.se"
        }
    },

    "Austria": {
        "country_name": "Austria",
        "iso_alpha2": "AT",
        "iso_alpha3": "AUT",
        "region": "Europe",
        "subregion": "Central Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Austria follows standard EU pet travel rules. No routine quarantine.",
        "official_source": "Federal Ministry of Social Affairs, Health, Care and Consumer Protection (BMSGPK) — sozialministerium.at",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel",
                "notes": "Check BMSGPK list for which origin countries require treatment."
            },
            "banned_breeds": {
                "legislation": "Varies by Austrian state (Bundesland). No federal ban.",
                "notes": "Breed restrictions are set at state level. Some states restrict Pit Bull, Rottweiler, and other breeds. Check specific state rules."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official veterinarian"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "BMSGPK — Veterinary Services",
            "website": "sozialministerium.at"
        }
    },

    "Belgium": {
        "country_name": "Belgium",
        "iso_alpha2": "BE",
        "iso_alpha3": "BEL",
        "region": "Europe",
        "subregion": "Western Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Home of many EU and NATO staff, making it a significant pet relocation market. Standard EU rules apply.",
        "official_source": "FASFC (Federal Agency for the Safety of the Food Chain / AFSCA) — favv.be",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain non-EU countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel",
                "notes": "Required when entering from echinococcosis-endemic countries."
            },
            "banned_breeds": {
                "legislation": "Flemish, Walloon and Brussels-Capital Region have separate rules",
                "notes": "No federal breed ban. Some regions restrict Pit Bull and related types. Check regional rules before import."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "FASFC-authorised vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "FASFC / AFSCA",
            "website": "favv.be"
        }
    },

    "Poland": {
        "country_name": "Poland",
        "iso_alpha2": "PL",
        "iso_alpha3": "POL",
        "region": "Europe",
        "subregion": "Eastern Europe",
        "rabies_status": "rabies-free (mainland, border surveillance ongoing)",
        "pet_friendliness": "moderate",
        "notes": "EU member. Poland follows standard EU pet travel rules. Large diaspora population means significant pet movement between Poland and UK, Germany, Ireland.",
        "official_source": "Main Veterinary Inspectorate (Główny Inspektorat Weterynarii) — wetgiw.gov.pl",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel"
            },
            "banned_breeds": {
                "legislation": "Polish Act on Animal Protection",
                "banned_types": [],
                "notes": "Poland has no breed ban but some aggressive breeds require muzzle and leash in public."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official veterinarian"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "Główny Inspektorat Weterynarii (GIW)",
            "website": "wetgiw.gov.pl"
        }
    },

    "Turkey": {
        "country_name": "Turkey",
        "iso_alpha2": "TR",
        "iso_alpha3": "TUR",
        "region": "Asia/Europe",
        "subregion": "Western Asia / Southeast Europe",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "moderate",
        "notes": "Not EU member. Turkey (officially Turkiye) has a large expat community, especially in Istanbul and coastal areas. Import requirements are more relaxed than many countries but documentation is required.",
        "official_source": "Turkish Ministry of Agriculture and Forestry (TRGM) — tarimorman.gov.tr",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted and readable at time of travel",
                "notes": "Microchip required for dogs and cats."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_months": 3,
                "valid_within_months": 12,
                "wait_after_first_vaccination_days": 0,
                "notes": "Rabies vaccination must be current (within 12 months). For puppies/kittens minimum 3 months old at time of vaccination."
            },
            "rabies_titre_test": {
                "required_for": "Generally not required for standard companion animals from most countries",
                "not_required_for": "Most origin countries",
                "notes": "Turkey does not routinely require titre tests for dogs and cats."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for dogs and cats arriving with correct documentation. Inspection on arrival by veterinary officer."
            },
            "import_permit": {
                "required": False,
                "notes": "No pre-travel import permit required for dogs and cats (up to 5 animals per person)."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official veterinarian in country of origin",
                "valid_for_entry_days": 10,
                "notes": "Certificate must state microchip number, rabies vaccination details, and confirm animal is healthy. Must be in English or Turkish or accompanied by translation."
            },
            "banned_breeds": {
                "legislation": "Turkish Veterinary Services Law",
                "banned_types": ["American Pit Bull Terrier", "Japanese Tosa"],
                "notes": "Pit Bull Terrier and Japanese Tosa are banned. All breed mixes of banned dogs also prohibited."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate (EU or destination format)",
                "issued_by": "Official vet authorised by TRGM",
                "notes": "Health certificate must match destination country requirements. Issued by TRGM-authorised official vet."
            },
            "export_permit": {
                "required": False,
                "notes": "No export permit for pet dogs and cats."
            }
        },
        "key_contacts": {
            "authority": "General Directorate of Food and Control (KKGM) / TRGM",
            "website": "tarimorman.gov.tr"
        }
    },

    "Israel": {
        "country_name": "Israel",
        "iso_alpha2": "IL",
        "iso_alpha3": "ISR",
        "region": "Asia",
        "subregion": "Middle East",
        "rabies_status": "rabies-controlled (wildlife reservoir in some areas)",
        "pet_friendliness": "moderate",
        "notes": "Israel has strict import rules for pets. Pre-approval from the Veterinary Services is required before travel. Allow at least 3-6 months lead time.",
        "official_source": "Israel Ministry of Agriculture and Rural Development — veterinary.moag.gov.il",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted before rabies vaccination",
                "notes": "Microchip is mandatory. Must be functional and match all documents."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_months": 3,
                "valid_within_months": 12,
                "wait_after_first_vaccination_days": 21,
                "notes": "Rabies vaccination must be current and correctly documented."
            },
            "rabies_titre_test": {
                "required_for": "All pets except those from approved listed countries (US, Canada, most EU, UK, Australia, New Zealand)",
                "not_required_for": "Pets from fully approved countries with appropriate documentation",
                "test_type": "FAVN at approved lab",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90,
                "notes": "Titre test required for most countries. Blood drawn at least 30 days after most recent rabies vaccination. 3-month wait after successful test."
            },
            "quarantine": {
                "required": True,
                "duration_days": "1-3 days (inspection hold)",
                "facility": "Ben Gurion Airport Quarantine Station",
                "notes": "All dogs and cats undergo a mandatory veterinary inspection on arrival. This is an inspection hold of 1-3 days, not extended quarantine, for pets with correct documents. Pets with non-compliant docs may be held longer or refused entry."
            },
            "import_permit": {
                "required": True,
                "name": "Pre-approval from Israeli Veterinary Services",
                "how_to_apply": "Apply via Israeli Ministry of Agriculture Veterinary Services at least 60 days before travel",
                "notes": "Import must be pre-approved. Do not travel without confirmed permit. Form available via veterinary.moag.gov.il."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government veterinarian in origin country",
                "must_be_endorsed_by": "National veterinary authority",
                "valid_for_entry_days": 10,
                "notes": "Certificate must be issued and endorsed no more than 10 days before arrival. Lists microchip, vaccinations, titre test result, parasite treatment."
            },
            "banned_breeds": {
                "legislation": "Israeli Dangerous Dogs Regulations 2004",
                "banned_types": [
                    "American Pit Bull Terrier",
                    "American Staffordshire Terrier",
                    "Rottweiler",
                    "Bull Terrier",
                    "Dogo Argentino",
                    "Fila Brasileiro",
                    "Japanese Tosa"
                ],
                "notes": "Banned breeds cannot be imported. Check hybrid and mixed breed status with Veterinary Services before applying."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "Export health certificate",
                "issued_by": "Official vet authorised by Israeli Veterinary Services",
                "notes": "Required for export. Format depends on destination country."
            },
            "export_permit": {
                "required": True,
                "notes": "Export permit required from Israeli Veterinary Services for certain species/breeds."
            }
        },
        "key_contacts": {
            "authority": "Israeli Veterinary Services (IVS) — Ministry of Agriculture",
            "website": "veterinary.moag.gov.il"
        }
    },

    "Saudi_Arabia": {
        "country_name": "Saudi Arabia",
        "iso_alpha2": "SA",
        "iso_alpha3": "SAU",
        "region": "Asia",
        "subregion": "Middle East",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low-moderate",
        "notes": "Large expat community. Dogs are less culturally common than in Western countries, but expats routinely bring dogs and cats. Strict documentation and embassy attestation required.",
        "official_source": "Ministry of Environment, Water and Agriculture (MEWA) — mewa.gov.sa",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip mandatory for all dogs and cats."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "minimum_age_months": 3,
                "notes": "Valid rabies vaccination within the past 12 months."
            },
            "rabies_titre_test": {
                "required_for": "Varies — check current MEWA requirements as rules change periodically",
                "notes": "Titre test not universally required but may be demanded by customs officer. Best to have recent titre results available."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for compliant pets. Airport veterinary inspection on arrival."
            },
            "import_permit": {
                "required": True,
                "name": "MEWA Import Permit",
                "how_to_apply": "Apply via MEWA portal or agent",
                "lead_time_weeks": 4,
                "notes": "Import permit from MEWA required before travel. Some pet relocation companies can handle this. Permit specifies number and species of animals."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "attestation": "Must be endorsed by national veterinary authority AND attested by Saudi Arabian embassy in country of origin",
                "valid_for_entry_days": 14,
                "notes": "Embassy attestation adds 1-2 weeks. Plan accordingly. Certificate must list microchip, vaccinations, parasite treatments, and declare the animal free of infectious disease."
            },
            "banned_breeds": {
                "legislation": "MEWA regulations",
                "banned_types": ["Pit Bull Terrier", "Rottweiler (restricted)"],
                "notes": "Pit Bull Terriers are banned. Rottweilers face additional restrictions. Check current MEWA banned/restricted list before applying."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "Official Export Health Certificate",
                "issued_by": "MEWA-authorised official vet",
                "notes": "Format depends on destination. MEWA endorsement required for most destinations."
            },
            "export_permit": {
                "required": True,
                "notes": "Export permit from MEWA required. Apply in advance."
            }
        },
        "key_contacts": {
            "authority": "MEWA — Ministry of Environment, Water and Agriculture",
            "website": "mewa.gov.sa"
        }
    },

    "Qatar": {
        "country_name": "Qatar",
        "iso_alpha2": "QA",
        "iso_alpha3": "QAT",
        "region": "Asia",
        "subregion": "Middle East",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "moderate",
        "notes": "Growing expat community (majority of Qatar population is expat). Pet transport into Qatar is common but requires careful documentation and embassy attestation.",
        "official_source": "Ministry of Environment and Climate Change (MECC) — mecc.gov.qa",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current rabies vaccination required. Some sources specify last booster within 12 months."
            },
            "rabies_titre_test": {
                "required_for": "Pets from countries without established 3-year vaccination records",
                "notes": "MECC may require titre test results. Carry FAVN results if available."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for compliant pets. Veterinary inspection at Hamad International Airport."
            },
            "import_permit": {
                "required": True,
                "name": "MECC Import Permit",
                "lead_time_weeks": 4,
                "notes": "Apply to MECC at least 4 weeks before travel. Required before the health certificate is issued."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "attestation": "Must be endorsed by national veterinary authority AND attested by Qatari embassy",
                "valid_for_entry_days": 14,
                "notes": "Embassy attestation required. Allow 2 weeks for attestation process."
            },
            "banned_breeds": {
                "legislation": "MECC regulations",
                "banned_types": [
                    "American Pit Bull Terrier",
                    "Japanese Tosa",
                    "Dogo Argentino",
                    "Fila Brasileiro"
                ],
                "notes": "Banned breeds cannot be imported."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "MECC-authorised official vet"
            },
            "export_permit": {"required": True, "notes": "Export permit from MECC."}
        },
        "key_contacts": {
            "authority": "MECC — Ministry of Environment and Climate Change",
            "website": "mecc.gov.qa"
        }
    },

    "Kuwait": {
        "country_name": "Kuwait",
        "iso_alpha2": "KW",
        "iso_alpha3": "KWT",
        "region": "Asia",
        "subregion": "Middle East",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low-moderate",
        "notes": "Large expat population. Pet import possible but documentation requirements are strict. Embassy attestation required.",
        "official_source": "Public Authority for Agricultural Affairs and Fish Resources (PAM) — paaafr.gov.kw",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785"
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Rabies vaccination required and current."
            },
            "rabies_titre_test": {
                "required_for": "May be required — check current PAM requirements",
                "notes": "Carry titre test results. Requirements can change."
            },
            "quarantine": {
                "required": False,
                "notes": "Inspection on arrival by PAM veterinary officer at Kuwait International Airport."
            },
            "import_permit": {
                "required": True,
                "name": "PAM Import Permit",
                "notes": "Apply to PAM before travel. Permit issued per animal."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "attestation": "Endorsed by national vet authority + attested by Kuwaiti embassy",
                "valid_for_entry_days": 14,
                "notes": "Embassy attestation required. Plan 2+ weeks."
            },
            "banned_breeds": {
                "legislation": "PAM regulations",
                "banned_types": ["American Pit Bull Terrier", "Japanese Tosa", "Dogo Argentino"],
                "notes": "Banned breeds not permitted."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {"required": True, "issued_by": "PAM-authorised vet"},
            "export_permit": {"required": True}
        },
        "key_contacts": {
            "authority": "PAM — Public Authority for Agricultural Affairs and Fish Resources",
            "website": "paaafr.gov.kw"
        }
    },

    "China": {
        "country_name": "China",
        "iso_alpha2": "CN",
        "iso_alpha3": "CHN",
        "region": "Asia",
        "subregion": "East Asia",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low",
        "notes": "China has strict pet import controls. Only dogs and cats. Limited approved entry points. Mandatory quarantine applies. Allow 4-6 months lead time. Dogs limited to 1 per household in many cities.",
        "official_source": "General Administration of Customs of China (GACC) — english.customs.gov.cn",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 15 digit",
                "timing": "Must be implanted before vaccinations",
                "notes": "15-digit ISO microchip mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_months": 3,
                "valid_within_months": 12,
                "notes": "Must be administered at least 30 days before travel but within 12 months."
            },
            "rabies_titre_test": {
                "required_for": "All dogs and cats from most countries",
                "test_type": "FAVN at GACC-approved lab",
                "minimum_result": "0.5 IU/ml",
                "blood_draw_timing": "At least 30 days after most recent rabies vaccination",
                "wait_after_test_days": 180,
                "notes": "6-month wait after titre test before travel. Very strict. Plan at least 6 months ahead."
            },
            "quarantine": {
                "required": True,
                "duration_days": "30 days (dogs); 7 days (cats, if from approved countries) — check current rules",
                "facility": "GACC-approved quarantine facility",
                "cost_responsibility": "Owner pays all quarantine costs",
                "notes": "Quarantine is mandatory. Facility and duration depends on origin country and species. Cats from some listed countries may be 7 days. Dogs typically 30 days."
            },
            "import_permit": {
                "required": True,
                "name": "GACC Import Permit",
                "how_to_apply": "Through official channels or licensed pet relocation company",
                "lead_time_months": 4,
                "notes": "Import permit must be obtained before travel. Very limited entry airports: Beijing, Shanghai, Guangzhou main points. Must declare on arrival customs form."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government veterinarian",
                "must_be_endorsed_by": "National veterinary authority",
                "attestation": "Chinese embassy attestation required for some countries",
                "valid_for_entry_days": 14,
                "notes": "Must include microchip, vaccination records, titre test results, rabies-free status of origin region, and parasite treatment."
            },
            "banned_breeds": {
                "legislation": "Beijing, Shanghai, and other cities have breed-specific municipal laws",
                "notes": "Breed restrictions vary by city. Beijing bans many breeds over 35cm shoulder height. Shanghai restricts specific breeds. Research your destination city before travel."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "GACC-authorised official vet",
                "notes": "Export health certificate in destination-country required format."
            },
            "export_permit": {
                "required": True,
                "notes": "Export permit from GACC. Required particularly for purebred/registered breeds."
            }
        },
        "key_contacts": {
            "authority": "GACC — General Administration of Customs of China",
            "website": "english.customs.gov.cn"
        }
    },

    "Taiwan": {
        "country_name": "Taiwan",
        "iso_alpha2": "TW",
        "iso_alpha3": "TWN",
        "region": "Asia",
        "subregion": "East Asia",
        "rabies_status": "rabies-free (dogs and cats; wildlife reservoir eradicated since 2013)",
        "pet_friendliness": "moderate",
        "notes": "Taiwan is rabies-free for dogs/cats and has strict biosecurity requirements. Dogs and cats from approved low-risk countries face shorter quarantine. Allow 3-6 months.",
        "official_source": "Bureau of Animal and Plant Health Inspection and Quarantine (BAPHIQ) — baphiq.gov.tw",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "timing": "Within 1 year of arrival, at least 30 days before travel for primary vaccination",
                "notes": "Current rabies vaccination mandatory."
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-approved countries (Group 3 and 4 countries per BAPHIQ classification)",
                "not_required_for": "Pets from approved Group 1 or 2 countries (includes US, UK, Australia, most EU, Japan, etc.)",
                "test_type": "FAVN at BAPHIQ-approved lab",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 180,
                "notes": "6-month wait after titre test. Check BAPHIQ country classification list."
            },
            "quarantine": {
                "required": True,
                "duration_days_group1": "7 (approved low-risk countries)",
                "duration_days_group2": "21 (approved countries with some risk factors)",
                "duration_days_group3": "180 (non-approved countries or missing titre test)",
                "facility": "BAPHIQ-designated Animal Quarantine Station, Taoyuan Airport",
                "cost_responsibility": "Owner",
                "notes": "Quarantine duration depends on country of origin classification. Group 1 countries (US, UK, most EU, Japan, Australia, NZ, Singapore, etc.) = 7-day quarantine. Check current BAPHIQ country list."
            },
            "import_permit": {
                "required": True,
                "name": "Import Permit from BAPHIQ",
                "how_to_apply": "Apply online via BAPHIQ portal at least 60 days before travel",
                "lead_time_days": 60,
                "notes": "Permit required before booking flights. Must specify flight details."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet in origin country",
                "issued_within_days_of_travel": 14,
                "notes": "Must include microchip, vaccinations, titre test (if applicable), and declare freedom from infectious disease."
            },
            "banned_breeds": {
                "legislation": "Animal Protection Act",
                "notes": "No specific breed ban under national law, but certain local government rules may apply."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "BAPHIQ-authorised official vet"
            },
            "export_permit": {"required": False, "notes": "No export permit for pets."}
        },
        "key_contacts": {
            "authority": "BAPHIQ — Bureau of Animal and Plant Health Inspection and Quarantine",
            "website": "baphiq.gov.tw"
        }
    },

    "Vietnam": {
        "country_name": "Vietnam",
        "iso_alpha2": "VN",
        "iso_alpha3": "VNM",
        "region": "Asia",
        "subregion": "Southeast Asia",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "moderate",
        "notes": "Growing expat community in Hanoi and Ho Chi Minh City. Pet import is allowed for dogs and cats with proper documentation. Import permit required.",
        "official_source": "Department of Animal Health, Ministry of Agriculture and Rural Development (MARD) — cucthuy.gov.vn",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip required."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "minimum_age_months": 3,
                "notes": "Rabies vaccination within 12 months."
            },
            "rabies_titre_test": {
                "required_for": "Not routinely required for companion animals",
                "notes": "Titre test not normally required. But carry documentation in case of border inspection."
            },
            "quarantine": {
                "required": False,
                "notes": "No mandatory quarantine for compliant pets. Veterinary inspection at point of entry."
            },
            "import_permit": {
                "required": True,
                "name": "Import Permit from MARD / Department of Animal Health",
                "how_to_apply": "Apply to the Department of Animal Health in advance",
                "lead_time_weeks": 4,
                "notes": "Import permit must be obtained before travel."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet in origin country",
                "valid_for_entry_days": 14,
                "notes": "Must state microchip number, vaccinations, and health status. Should be endorsed by national vet authority."
            },
            "banned_breeds": {
                "legislation": "MARD regulations",
                "notes": "Some cities and residential buildings restrict large dogs. No national breed ban for import, but check local rules."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "MARD-authorised official vet"
            },
            "export_permit": {"required": False, "notes": "No export permit for pet dogs and cats."}
        },
        "key_contacts": {
            "authority": "Department of Animal Health, MARD",
            "website": "cucthuy.gov.vn"
        }
    },

    "Sri_Lanka": {
        "country_name": "Sri Lanka",
        "iso_alpha2": "LK",
        "iso_alpha3": "LKA",
        "region": "Asia",
        "subregion": "South Asia",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low",
        "notes": "Island nation with strict biosecurity. Mandatory quarantine applies. Only animals meeting all requirements can enter. Allow 6 months minimum lead time.",
        "official_source": "Department of Animal Production and Health (DAPH) — daph.gov.lk",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "All dogs and cats",
                "test_type": "FAVN at DAPH-approved lab",
                "minimum_result": "0.5 IU/ml",
                "blood_draw_timing": "At least 30 days after primary rabies vaccination",
                "wait_after_test_days": 90,
                "notes": "3-month wait after titre test."
            },
            "quarantine": {
                "required": True,
                "duration_days": 21,
                "facility": "DAPH Quarantine Station",
                "cost_responsibility": "Owner",
                "notes": "21-day mandatory quarantine for all dogs and cats. No exceptions."
            },
            "import_permit": {
                "required": True,
                "name": "Import Permit from DAPH",
                "how_to_apply": "Apply to DAPH with health certificate, titre test, vaccination records, and microchip cert",
                "lead_time_months": 3,
                "notes": "Strict documentation review. Allow 3 months for permit approval."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Government vet, endorsed by national veterinary authority",
                "attestation": "Must be attested by Sri Lanka High Commission in origin country",
                "valid_for_entry_days": 14,
                "notes": "Embassy attestation required."
            },
            "banned_breeds": {
                "legislation": "DAPH regulations",
                "banned_types": ["American Pit Bull Terrier"],
                "notes": "Pit Bull Terriers banned."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "DAPH-authorised official vet"
            },
            "export_permit": {"required": True, "notes": "Export permit from DAPH."}
        },
        "key_contacts": {
            "authority": "DAPH — Department of Animal Production and Health",
            "website": "daph.gov.lk"
        }
    },

    "Argentina": {
        "country_name": "Argentina",
        "iso_alpha2": "AR",
        "iso_alpha3": "ARG",
        "region": "South America",
        "subregion": "Latin America",
        "rabies_status": "rabies-endemic (bats; dog/cat controlled in most areas)",
        "pet_friendliness": "high",
        "notes": "Argentina is relatively pet-friendly and has lower barriers to import than many countries. Growing expat community in Buenos Aires. SENASA (national food safety authority) manages pet imports.",
        "official_source": "SENASA — Servicio Nacional de Sanidad y Calidad Agroalimentaria — senasa.gob.ar",
        "import_requirements": {
            "microchip": {
                "required": False,
                "recommended": True,
                "notes": "Microchip not legally mandatory for entry but strongly recommended. Some regions require it for local registration."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "minimum_age_months": 3,
                "notes": "Current rabies vaccination required. Valid within 12 months."
            },
            "rabies_titre_test": {
                "required_for": "Not required for most origin countries",
                "notes": "No titre test requirement for standard companion animal import from most countries."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for dogs and cats arriving with correct documentation."
            },
            "import_permit": {
                "required": False,
                "notes": "No import permit for up to 3 companion animals per person."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official veterinarian in country of origin",
                "must_be_endorsed_by": "National veterinary authority",
                "valid_for_entry_days": 10,
                "notes": "Certificate must state animal is free of contagious disease, fully vaccinated, and microchipped. Must be in Spanish or accompanied by certified Spanish translation."
            },
            "banned_breeds": {
                "legislation": "Argentine Dangerous Dogs Act 954/94",
                "banned_types": [],
                "restricted_breeds": ["American Pit Bull Terrier", "Rottweiler", "Dogo Argentino"],
                "notes": "Dogo Argentino is an Argentine breed and is not banned. Some municipalities restrict Pit Bulls and Rottweilers in public. No national import ban."
            }
        },
        "export_requirements": {
            "microchip": {"recommended": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "SENASA-authorised official vet",
                "notes": "SENASA issues export health certificates. Allow 1-2 weeks."
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "SENASA — Servicio Nacional de Sanidad y Calidad Agroalimentaria",
            "website": "senasa.gob.ar"
        }
    },

    "Chile": {
        "country_name": "Chile",
        "iso_alpha2": "CL",
        "iso_alpha3": "CHL",
        "region": "South America",
        "subregion": "Latin America",
        "rabies_status": "rabies-free (dogs and cats)",
        "pet_friendliness": "moderate",
        "notes": "Chile is rabies-free for companion animals and has strict biosecurity controls. SAG (Servicio Agricola y Ganadero) manages all agricultural and animal imports. Documentation must be precise.",
        "official_source": "SAG — Servicio Agricola y Ganadero — sag.gob.cl",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Mandatory for all imported pets."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "Dogs and cats from countries classified as rabies-endemic by SAG",
                "not_required_for": "Pets from countries with equivalent rabies-free status",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "notes": "Check current SAG country classification list."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for compliant pets. SAG inspection at Santiago Airport."
            },
            "import_permit": {
                "required": True,
                "name": "SAG Import Permit",
                "how_to_apply": "Apply via SAG at least 30 days before travel",
                "notes": "Permit required. SAG reviews documentation before approving."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet",
                "must_be_endorsed_by": "National veterinary authority",
                "attestation": "Must be apostilled or legalised",
                "valid_for_entry_days": 10,
                "notes": "Must list microchip, vaccinations, titre test (if applicable), and parasite treatments. Apostille or legalisation required."
            },
            "banned_breeds": {
                "legislation": "Ley de Tenencia Responsable de Mascotas Chile",
                "banned_types": [],
                "notes": "No national breed ban, but certain municipalities may restrict specific breeds."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "SAG-authorised official vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "SAG — Servicio Agricola y Ganadero",
            "website": "sag.gob.cl"
        }
    },

    "Colombia": {
        "country_name": "Colombia",
        "iso_alpha2": "CO",
        "iso_alpha3": "COL",
        "region": "South America",
        "subregion": "Latin America",
        "rabies_status": "rabies-endemic (wildlife; urban rabies controlled)",
        "pet_friendliness": "moderate",
        "notes": "Colombia has become a growing expat destination, particularly Medellin and Bogota. ICA manages animal import controls.",
        "official_source": "ICA — Instituto Colombiano Agropecuario — ica.gov.co",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip mandatory for dogs and cats."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Annual rabies vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "Not routinely required",
                "notes": "Titre test not normally required. Carry documentation in case."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine. Veterinary inspection on arrival at El Dorado or other main airports."
            },
            "import_permit": {
                "required": True,
                "name": "ICA Import Permit",
                "how_to_apply": "Apply via ICA online portal at least 15 days before travel",
                "notes": "Import permit required from ICA."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet",
                "must_be_endorsed_by": "National veterinary authority or USDA/APHA equivalent",
                "valid_for_entry_days": 14,
                "notes": "Certificate in Spanish or with certified Spanish translation required."
            },
            "banned_breeds": {
                "legislation": "Ley 1774 de 2016 and municipal regulations",
                "notes": "Some cities restrict specific breeds. No national ban on import of specific breeds, but check Bogota and Medellin municipal rules."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "ICA-authorised official vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "ICA — Instituto Colombiano Agropecuario",
            "website": "ica.gov.co"
        }
    },

    "Egypt": {
        "country_name": "Egypt",
        "iso_alpha2": "EG",
        "iso_alpha3": "EGY",
        "region": "Africa",
        "subregion": "North Africa",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low-moderate",
        "notes": "Egypt has a significant expat community in Cairo. GOVS (General Organisation for Veterinary Services) oversees animal imports. Embassy attestation of health certificate required.",
        "official_source": "GOVS — General Organisation for Veterinary Services — govs.gov.eg",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip mandatory."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current rabies vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "May be required at customs officer discretion",
                "notes": "Carry titre test results. Requirements can vary."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine. Inspection on arrival at Cairo International Airport by GOVS vet."
            },
            "import_permit": {
                "required": True,
                "name": "GOVS Import Permit",
                "notes": "Import permit from GOVS required in advance."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "attestation": "Must be endorsed by national vet authority AND attested by Egyptian embassy",
                "valid_for_entry_days": 14,
                "notes": "Embassy attestation required. Allow 2 weeks for attestation."
            },
            "banned_breeds": {
                "legislation": "GOVS regulations",
                "banned_types": ["American Pit Bull Terrier"],
                "notes": "Pit Bull Terriers banned. Some large breeds may require additional permits."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "GOVS-authorised vet"
            },
            "export_permit": {"required": True}
        },
        "key_contacts": {
            "authority": "GOVS — General Organisation for Veterinary Services",
            "website": "govs.gov.eg"
        }
    },

    "Kenya": {
        "country_name": "Kenya",
        "iso_alpha2": "KE",
        "iso_alpha3": "KEN",
        "region": "Africa",
        "subregion": "East Africa",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "moderate",
        "notes": "Nairobi is a major expat hub (UN agencies, NGOs, multinationals). Pet import is permitted with correct documentation. Directorate of Veterinary Services (DVS) is the competent authority.",
        "official_source": "Directorate of Veterinary Services (DVS), Ministry of Agriculture — kilimo.go.ke",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip required for all imported companion animals."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current rabies vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "Not routinely required",
                "notes": "DVS may request titre results. Carry documentation."
            },
            "quarantine": {
                "required": False,
                "notes": "No routine quarantine for compliant pets. DVS inspection at Jomo Kenyatta International Airport."
            },
            "import_permit": {
                "required": True,
                "name": "DVS Import Permit",
                "how_to_apply": "Apply to DVS at least 21 days before travel",
                "notes": "Import permit required. DVS reviews documentation."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet in origin country",
                "valid_for_entry_days": 14,
                "notes": "Certificate must list vaccinations, microchip, and declare freedom from contagious disease."
            },
            "banned_breeds": {
                "legislation": "DVS regulations",
                "notes": "No national breed ban for import, but city-level restrictions may apply. Certain breeds require additional documentation."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "DVS-authorised official vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "DVS — Directorate of Veterinary Services",
            "website": "kilimo.go.ke"
        }
    },

    "Nigeria": {
        "country_name": "Nigeria",
        "iso_alpha2": "NG",
        "iso_alpha3": "NGA",
        "region": "Africa",
        "subregion": "West Africa",
        "rabies_status": "rabies-endemic",
        "pet_friendliness": "low-moderate",
        "notes": "Pet import possible but requires strict documentation. Federal Department of Veterinary and Pest Control Services (FDVPCS) manages imports. Lagos is the main entry point.",
        "official_source": "Federal Department of Veterinary and Pest Control Services (FDVPCS) — fmard.gov.ng",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "notes": "Microchip required."
            },
            "rabies_vaccination": {
                "required": True,
                "valid_within_months": 12,
                "notes": "Current vaccination required."
            },
            "rabies_titre_test": {
                "required_for": "May be required",
                "notes": "Requirements can vary. Carry titre test documentation."
            },
            "quarantine": {
                "required": False,
                "notes": "Inspection on arrival by FDVPCS. No routine quarantine for compliant pets."
            },
            "import_permit": {
                "required": True,
                "name": "FDVPCS Import Permit",
                "notes": "Permit required from FDVPCS. Apply in advance."
            },
            "health_certificate": {
                "required": True,
                "name": "Official Veterinary Health Certificate",
                "issued_by": "Official government vet",
                "attestation": "Must be endorsed by national vet authority",
                "valid_for_entry_days": 14
            },
            "banned_breeds": {
                "legislation": "FDVPCS regulations",
                "notes": "No specific breed ban nationally, but customs officers may restrict certain breeds."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "issued_by": "FDVPCS-authorised vet"
            },
            "export_permit": {"required": True}
        },
        "key_contacts": {
            "authority": "FDVPCS — Federal Department of Veterinary and Pest Control Services",
            "website": "fmard.gov.ng"
        }
    },

    "Czech_Republic": {
        "country_name": "Czech Republic",
        "iso_alpha2": "CZ",
        "iso_alpha3": "CZE",
        "region": "Europe",
        "subregion": "Central Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Czech Republic follows standard EU pet travel rules. Growing expat community in Prague. No routine quarantine.",
        "official_source": "State Veterinary Administration (SVA) — svscr.cz",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain origin countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel"
            },
            "banned_breeds": {
                "legislation": "Czech Act on Municipalities / regional rules",
                "notes": "No national breed ban. Some municipalities may restrict specific breeds in public."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "SVA-authorised official vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "SVA — State Veterinary Administration",
            "website": "svscr.cz"
        }
    },

    "Romania": {
        "country_name": "Romania",
        "iso_alpha2": "RO",
        "iso_alpha3": "ROU",
        "region": "Europe",
        "subregion": "Eastern Europe",
        "rabies_status": "rabies-controlled (some wildlife risk in rural areas)",
        "pet_friendliness": "moderate",
        "notes": "EU member. Romania follows standard EU pet travel rules. Large Romanian diaspora in UK/EU creates significant reverse-migration pet movement.",
        "official_source": "National Sanitary Veterinary and Food Safety Authority (ANSVSA) — ansvsa.ro",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel"
            },
            "banned_breeds": {
                "legislation": "Romanian Law No. 227/2002",
                "banned_types": ["Pit Bull Terrier", "Romanian Carpathian Shepherd Dog (in urban areas, regulated not banned)"],
                "notes": "Pit Bull and crosses are restricted. Rottweiler and other large breeds subject to muzzle/leash rules in public."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "ANSVSA-authorised official vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "ANSVSA — National Sanitary Veterinary and Food Safety Authority",
            "website": "ansvsa.ro"
        }
    },

    "Malta": {
        "country_name": "Malta",
        "iso_alpha2": "MT",
        "iso_alpha3": "MLT",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "moderate",
        "notes": "EU member island nation. Malta is rabies-free and has strict biosecurity. Additional tick treatment required for dogs. No routine quarantine for compliant pets.",
        "official_source": "Ministry for the Environment — msdec.gov.mt / Veterinary Regulation Directorate",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from countries with echinococcosis risk",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel"
            },
            "tick_treatment": {
                "required_for": "Dogs entering Malta",
                "timing": "24-48 hours before arrival",
                "drug": "Tick prevention product effective against Rhipicephalus ticks",
                "notes": "Malta (and Cyprus) require tick treatment for dogs. Must be recorded in pet passport or AHC."
            },
            "banned_breeds": {
                "legislation": "Maltese Dog Ownership and Protection Regulations",
                "notes": "No full breed ban but certain breeds must be muzzled in public and registered as dangerous dogs."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Veterinary Regulation Directorate-authorised vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "Veterinary Regulation Directorate, MSDEC",
            "website": "msdec.gov.mt"
        }
    },

    "Cyprus": {
        "country_name": "Cyprus",
        "iso_alpha2": "CY",
        "iso_alpha3": "CYP",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "moderate",
        "notes": "EU member island nation. Cyprus has a large British expat community and significant pet transport traffic. EU standard rules plus tick treatment for dogs.",
        "official_source": "Department of Veterinary Services, Ministry of Agriculture — moa.gov.cy",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before or on same day as first rabies vaccination"
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-listed countries",
                "not_required_for": "EU/listed countries",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "penalty_quarantine": True},
            "import_permit": {"required": False},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Official vet",
                "valid_for_entry_days": 10
            },
            "tapeworm_treatment": {
                "required_for": "Dogs from certain countries",
                "timing": "1-5 days before arrival",
                "drug": "Praziquantel"
            },
            "tick_treatment": {
                "required_for": "All dogs entering Cyprus",
                "timing": "24-48 hours before arrival",
                "drug": "Tick prevention product effective against Rhipicephalus sanguineus",
                "notes": "Must be documented in pet passport or AHC. Treated by veterinarian."
            },
            "banned_breeds": {
                "legislation": "Dangerous Dogs Laws Cyprus",
                "banned_types": ["American Pit Bull Terrier", "Japanese Tosa"],
                "notes": "Banned breeds cannot be imported."
            }
        },
        "export_requirements": {
            "microchip": {"required": True},
            "rabies_vaccination": {"required": True},
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport or AHC",
                "issued_by": "Department of Veterinary Services-authorised vet"
            },
            "export_permit": {"required": False}
        },
        "key_contacts": {
            "authority": "Department of Veterinary Services, Ministry of Agriculture",
            "website": "moa.gov.cy"
        }
    }

}


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    existing = set(data["countries"].keys())
    added = 0
    skipped = 0

    for key, country_data in P3_COUNTRIES.items():
        if key in existing:
            print(f"  SKIP (exists): {key}")
            skipped += 1
        else:
            data["countries"][key] = country_data
            print(f"  ADDED: {key} ({country_data['country_name']})")
            added += 1

    # Update metadata
    data["metadata"]["description"] = (
        f"Country pet import/export regulations database: P1 + P2 + P3 countries "
        f"({len(data['countries'])} total)"
    )
    data["metadata"]["p3_countries_added"] = str(date.today())
    data["metadata"]["date_compiled"] = str(date.today())

    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone. Added {added} countries, skipped {skipped}.")
    print(f"Total countries in database: {len(data['countries'])}")
    print(f"Countries: {sorted(data['countries'].keys())}")


if __name__ == "__main__":
    main()
