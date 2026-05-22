"""
add_p4_countries.py — extend countries_pet_regulations.json with 25 P4 countries.

P4 countries (25):
  Spain, New Zealand, Oman, Bahrain, Jordan, Finland, Hungary, Bulgaria, Croatia,
  Morocco, Pakistan, Bangladesh, Nepal, Cambodia, Myanmar, Peru, Ecuador, Costa Rica,
  Ghana, Tanzania, Ethiopia, Zimbabwe, Mauritius, Slovakia, Luxembourg

Run from repo root.
"""

import json
import os

DATA_FILE = os.path.join("data", "countries_pet_regulations.json")

P4_COUNTRIES = {
    "Spain": {
        "country_name": "Spain",
        "iso_alpha2": "ES",
        "iso_alpha3": "ESP",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member state. Follows EU Regulation 576/2013 (transitioning to Regulation 2026/131 from April 2026). Spain has one of Europe's highest pet ownership rates. Some additional national rules for 'potentially dangerous dogs' (PPP list). Authority: Ministerio de Agricultura, Pesca y Alimentacion (MAPA).",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted before or on same day as first rabies vaccination",
                "non_iso_accepted": False,
                "notes": "EU standard. 15-digit ISO microchip required."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "wait_after_booster_days": 0,
                "booster_condition": "No wait if continuous vaccination record with no lapse",
                "vaccine_type": "Inactivated or recombinant, WHO/OIE approved",
                "notes": "EU-harmonised rules. Vaccination must be recorded in EU pet passport or Animal Health Certificate."
            },
            "rabies_titre_test": {
                "required_for": "Pets from non-EU countries not on the EU listed third countries",
                "not_required_for": "Pets from EU member states and EU-listed countries",
                "test_type": "FAVN at EU-approved laboratory",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90,
                "notes": "For pets from non-listed third countries: 90-day wait after successful titre test. Blood drawn at least 30 days after rabies vaccination."
            },
            "quarantine": {
                "required": False,
                "penalty_quarantine": True,
                "penalty_trigger": "Non-compliant documentation or vaccination",
                "facility": "Officially approved quarantine premises",
                "cost_responsibility": "Owner pays all costs",
                "notes": "No routine quarantine for pets entering with correct EU-standard documentation."
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or Animal Health Certificate serves as the travel document",
                "notes": "No separate import permit. The AHC or EU pet passport is the required document."
            },
            "health_certificate": {
                "required": True,
                "name": "EU Pet Passport (for EU-resident pets) or Animal Health Certificate (AHC) for third-country pets",
                "issued_by": "Official veterinarian",
                "valid_for_entry_days": 10,
                "notes": "AHC valid 10 days from issue for entry. Then valid 4 months for onward EU travel."
            },
            "tapeworm_treatment": {
                "required_for": "Dogs entering from non-EU countries (check specific country rules)",
                "not_required_for": "Cats, most EU-to-EU movements",
                "timing": "24-120 hours before scheduled arrival",
                "drug": "Praziquantel",
                "notes": "Required for dogs from countries where Echinococcus multilocularis is a risk."
            },
            "banned_breeds": {
                "legislation": "Real Decreto 1485/1985 and regional laws. PPP (Perros Potencialmente Peligrosos) list.",
                "banned": ["American Pit Bull Terrier", "Staffordshire Bull Terrier", "American Staffordshire Terrier", "Rottweiler", "Dogo Argentino", "Fila Brasileiro", "Tosa Inu", "Akita Inu"],
                "notes": "PPP dogs require special licence, liability insurance, and muzzle/lead in public. Some regions have stricter rules. Entry may still be possible with documentation but check in advance."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False, "notes": "No export permit required for cats and dogs."},
            "health_certificate": {"required": True, "notes": "AHC required for export to non-EU countries. EU pet passport valid for intra-EU movement."}
        },
        "popular_routes": ["spain-to-uk", "spain-to-australia", "spain-to-usa", "uk-to-spain", "germany-to-spain"]
    },

    "New_Zealand": {
        "country_name": "New Zealand",
        "iso_alpha2": "NZ",
        "iso_alpha3": "NZL",
        "region": "Oceania",
        "subregion": "Australia and New Zealand",
        "rabies_status": "rabies-free",
        "pet_friendliness": "low",
        "notes": "New Zealand is rabies-free with one of the world's strictest pet import systems. All dogs and cats must complete mandatory quarantine at the government-approved facility (Levin MAF Quarantine Station, now MPI). Import permit required in advance. Only cats and dogs permitted from most countries; birds require separate approval. Authority: Ministry for Primary Industries (MPI), Biosecurity New Zealand.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted before or on same day as first rabies vaccination",
                "non_iso_accepted": False,
                "notes": "Microchip number recorded on all documentation."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 28,
                "booster_condition": "Booster required if lapse in vaccination cover",
                "vaccine_type": "Inactivated virus, commercially available",
                "notes": "Vaccination schedule must be complete before titre test blood draw."
            },
            "rabies_titre_test": {
                "required_for": "All pets from all countries (no exemptions)",
                "not_required_for": "None",
                "test_type": "FAVN at MPI-approved laboratory",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 180,
                "notes": "180-day wait (6 months) from successful titre test before pet can enter New Zealand. This wait cannot be shortened under any circumstances. Blood must be drawn at least 30 days after rabies vaccination."
            },
            "quarantine": {
                "required": True,
                "duration_days": "10 (minimum) at MPI Levin facility",
                "facility": "MPI Levin Quarantine Facility, Levin, Manawatu (the only approved facility)",
                "cost_responsibility": "Owner pays all quarantine fees (typically NZD 2,000-4,000+)",
                "notes": "Mandatory 10-day quarantine for all arriving cats and dogs. Pre-booking required well in advance as capacity is limited. Book before flights."
            },
            "import_permit": {
                "required": True,
                "issued_by": "Ministry for Primary Industries (MPI), Biosecurity New Zealand",
                "apply_in_advance_weeks": 8,
                "fee": "Yes, government fee applies",
                "notes": "Apply for import permit before booking flights. Permit specifies all conditions. Non-compliance results in re-export or destruction."
            },
            "health_certificate": {
                "required": True,
                "name": "Government veterinary health certificate",
                "issued_by": "Government (official) veterinarian in country of export",
                "valid_for_entry_days": 14,
                "notes": "Must use MPI-specified format for the exact country of export. No standard format accepted. Download the correct template from the MPI website."
            },
            "banned_breeds": {
                "legislation": "Dog Control Act 1996",
                "banned": ["American Pit Bull Terrier", "Dogo Argentino", "Brazilian Fila", "Japanese Tosa"],
                "notes": "Banned breeds may not enter New Zealand under any circumstances."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False, "notes": "No export permit for cats and dogs from New Zealand."},
            "health_certificate": {"required": True, "notes": "MPI issues AHC or equivalent for export."}
        },
        "popular_routes": ["new-zealand-to-uk", "new-zealand-to-australia", "new-zealand-to-usa", "australia-to-new-zealand", "uk-to-new-zealand"]
    },

    "Oman": {
        "country_name": "Oman",
        "iso_alpha2": "OM",
        "iso_alpha3": "OMN",
        "region": "Asia",
        "subregion": "Western Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Oman is a popular expat destination in the Gulf. Pet imports are regulated by the Ministry of Agriculture, Fisheries and Water Resources (MAFWR). Some breed bans apply. Dogs and cats accepted with prior approval. Authority: MAFWR General Directorate of Veterinary Services.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before travel",
                "notes": "Microchip number must match all documentation."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "notes": "Valid rabies vaccination required. Booster must be within manufacturer's validity period."
            },
            "rabies_titre_test": {
                "required_for": "Pets from countries deemed high risk by MAFWR",
                "not_required_for": "Some Gulf Cooperation Council (GCC) country movements",
                "test_type": "FAVN or ELISA at recognised laboratory",
                "minimum_result": "0.5 IU/ml",
                "notes": "Check current requirements with MAFWR as requirements change. UK and Australian pets typically require titre test."
            },
            "quarantine": {
                "required": False,
                "conditional_quarantine": True,
                "notes": "No routine quarantine for compliant pets. Veterinary inspection on arrival at Muscat International Airport. Non-compliant pets may face quarantine or re-export."
            },
            "import_permit": {
                "required": True,
                "issued_by": "MAFWR General Directorate of Veterinary Services",
                "apply_in_advance_weeks": 4,
                "notes": "Import permit (No Objection Certificate) required before travel. Apply through MAFWR or a local registered agent."
            },
            "health_certificate": {
                "required": True,
                "name": "Veterinary Health Certificate",
                "issued_by": "Official (government) veterinarian in country of export, endorsed by government authority",
                "valid_for_entry_days": 14,
                "notes": "Certificate must be endorsed by the competent veterinary authority in the exporting country."
            },
            "banned_breeds": {
                "legislation": "MAFWR Ministerial Decree",
                "banned": ["American Pit Bull Terrier", "Staffordshire Bull Terrier", "American Staffordshire Terrier", "Rottweiler", "Dogo Argentino", "Fila Brasileiro", "Japanese Tosa", "Wolf hybrids"],
                "notes": "List subject to change. Verify with MAFWR before booking travel."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True, "notes": "Health certificate from MAFWR-registered vet for export."}
        },
        "popular_routes": ["oman-to-uk", "oman-to-australia", "uk-to-oman", "uae-to-oman", "india-to-oman"]
    },

    "Bahrain": {
        "country_name": "Bahrain",
        "iso_alpha2": "BH",
        "iso_alpha3": "BHR",
        "region": "Asia",
        "subregion": "Western Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Bahrain is a GCC member with a significant expat population. Pet import regulated by Ministry of Works, Municipal Affairs and Urban Planning - Animal Wealth Directorate. Breed bans apply. Dogs and cats commonly imported by expats.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before travel",
                "notes": "ISO microchip required and must match all documents."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 21,
                "notes": "Valid rabies vaccination within manufacturer's specified validity."
            },
            "rabies_titre_test": {
                "required_for": "Pets from countries deemed high-risk",
                "not_required_for": "GCC country movements may be exempt",
                "test_type": "FAVN or ELISA",
                "minimum_result": "0.5 IU/ml",
                "notes": "Check current Bahrain requirements. UK, Australian, and US pets typically require titre test."
            },
            "quarantine": {
                "required": False,
                "conditional_quarantine": True,
                "notes": "Veterinary inspection on arrival at Bahrain International Airport. Compliant pets released. Non-compliant pets may face quarantine."
            },
            "import_permit": {
                "required": True,
                "issued_by": "Animal Wealth Directorate, Ministry of Works, Municipal Affairs and Urban Planning",
                "apply_in_advance_weeks": 3,
                "notes": "Import permit required before travel. Apply via the Bahrain eGovernment portal or through a local agent."
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian, endorsed by national authority",
                "valid_for_entry_days": 14,
                "notes": "Endorsed government health certificate required."
            },
            "banned_breeds": {
                "legislation": "Animal Wealth Directorate regulations",
                "banned": ["American Pit Bull Terrier", "Rottweiler", "Dogo Argentino", "Japanese Tosa", "Fila Brasileiro"],
                "notes": "Banned breeds list may be updated. Verify before travel."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True, "notes": "Health certificate from registered vet, endorsed by Animal Wealth Directorate."}
        },
        "popular_routes": ["bahrain-to-uk", "bahrain-to-australia", "uk-to-bahrain", "india-to-bahrain", "uae-to-bahrain"]
    },

    "Jordan": {
        "country_name": "Jordan",
        "iso_alpha2": "JO",
        "iso_alpha3": "JOR",
        "region": "Asia",
        "subregion": "Western Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Jordan regulated by Ministry of Agriculture, General Directorate of Veterinary Services. Expat community in Amman. Process relatively straightforward for cats and dogs from approved countries.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785", "timing": "Before travel"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {
                "required_for": "Pets from rabies-endemic countries",
                "not_required_for": "Pets from rabies-free or low-risk countries (UK, Australia, NZ may be exempt)",
                "minimum_result": "0.5 IU/ml",
                "notes": "Verify current requirements with Ministry of Agriculture."
            },
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "Veterinary inspection on arrival. Non-compliant pets may be quarantined."},
            "import_permit": {"required": True, "issued_by": "Ministry of Agriculture, General Directorate of Veterinary Services", "apply_in_advance_weeks": 4},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority", "valid_for_entry_days": 14},
            "banned_breeds": {"banned": ["American Pit Bull Terrier", "Rottweiler", "Dogo Argentino"], "notes": "Breed restrictions apply. Verify list before travel."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["jordan-to-uk", "uk-to-jordan", "uae-to-jordan", "germany-to-jordan"]
    },

    "Finland": {
        "country_name": "Finland",
        "iso_alpha2": "FI",
        "iso_alpha3": "FIN",
        "region": "Europe",
        "subregion": "Northern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member. Follows EU Regulation 576/2013 and Regulation 2026/131 from April 2026. Finland has specific tapeworm treatment requirements. Authority: Finnish Food Authority (Ruokavirasto).",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785", "timing": "Before rabies vaccination"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {
                "required_for": "Pets from non-EU third countries not on EU listed countries list",
                "not_required_for": "EU member state pets, EU-listed third country pets",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 90
            },
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "No routine quarantine for compliant pets."},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or Animal Health Certificate (AHC)", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "tapeworm_treatment": {
                "required_for": "Dogs entering from non-EU countries",
                "timing": "24-120 hours before scheduled arrival",
                "drug": "Praziquantel",
                "notes": "Finland has specific Echinococcus risk zone requirements."
            },
            "banned_breeds": {"legislation": "Animal Protection Act (Finland)", "banned": [], "notes": "Finland does not have a breed ban list. All breeds accepted subject to welfare rules."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True, "notes": "EU pet passport valid for EU movement. AHC for non-EU export."}
        },
        "popular_routes": ["finland-to-uk", "finland-to-australia", "finland-to-usa", "uk-to-finland", "germany-to-finland"]
    },

    "Hungary": {
        "country_name": "Hungary",
        "iso_alpha2": "HU",
        "iso_alpha3": "HUN",
        "region": "Europe",
        "subregion": "Central Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "moderate",
        "notes": "EU member. EU Regulation 576/2013 applies. Authority: National Food Chain Safety Office (NEBIH). Some local breed restrictions.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from non-listed third countries", "minimum_result": "0.5 IU/ml", "wait_after_test_days": 90},
            "quarantine": {"required": False, "conditional_quarantine": True},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or AHC", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "banned_breeds": {
                "legislation": "Government Decree 35/1997",
                "banned": ["American Pit Bull Terrier", "American Staffordshire Terrier"],
                "restricted": ["Rottweiler", "Bull Terrier", "Staffordshire Bull Terrier"],
                "notes": "Some breeds require special permit and conditions. Verify before travel."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["hungary-to-uk", "hungary-to-australia", "uk-to-hungary", "germany-to-hungary"]
    },

    "Bulgaria": {
        "country_name": "Bulgaria",
        "iso_alpha2": "BG",
        "iso_alpha3": "BGR",
        "region": "Europe",
        "subregion": "Eastern Europe",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "EU member. EU regulations apply but Bulgaria is not on the UK's Part 1 list (has wild rabies). Pets from Bulgaria to UK require titre test. Authority: Bulgarian Food Safety Agency (BFSA).",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from non-listed third countries (into UK/AU/NZ)", "minimum_result": "0.5 IU/ml", "wait_after_test_days": 90},
            "quarantine": {"required": False, "conditional_quarantine": True},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or AHC", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "banned_breeds": {"legislation": "Bulgarian Animal Protection Act and municipal orders", "banned": ["American Pit Bull Terrier"], "notes": "Some municipalities have additional breed restrictions."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["bulgaria-to-uk", "bulgaria-to-germany", "uk-to-bulgaria", "germany-to-bulgaria"]
    },

    "Croatia": {
        "country_name": "Croatia",
        "iso_alpha2": "HR",
        "iso_alpha3": "HRV",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member since 2013. EU Regulation 576/2013 applies. Authority: Ministry of Agriculture, Veterinary and Food Safety Directorate.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from non-listed third countries", "minimum_result": "0.5 IU/ml", "wait_after_test_days": 90},
            "quarantine": {"required": False, "conditional_quarantine": True},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or AHC", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "banned_breeds": {"legislation": "Animal Protection Act (Zakon o zastiti zivotinja)", "banned": [], "notes": "Croatia does not operate a breed ban system."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["croatia-to-uk", "croatia-to-germany", "uk-to-croatia", "germany-to-croatia"]
    },

    "Morocco": {
        "country_name": "Morocco",
        "iso_alpha2": "MA",
        "iso_alpha3": "MAR",
        "region": "Africa",
        "subregion": "North Africa",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Morocco regulated by the Office National de Securite Sanitaire des produits Alimentaires (ONSSA). Rabies present. Import permit required. Popular expat destination and gateway for Africa.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from certain countries (check ONSSA list)", "minimum_result": "0.5 IU/ml", "notes": "Requirements depend on country of origin."},
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "Veterinary inspection on arrival. Non-compliant pets may be quarantined or returned."},
            "import_permit": {"required": True, "issued_by": "ONSSA (Office National de Securite Sanitaire des produits Alimentaires)", "apply_in_advance_weeks": 4},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority", "valid_for_entry_days": 14},
            "banned_breeds": {"banned": ["American Pit Bull Terrier", "Rottweiler", "Dogo Argentino"], "notes": "Breed restrictions apply, verify with ONSSA."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True, "notes": "ONSSA-endorsed health certificate."}
        },
        "popular_routes": ["morocco-to-uk", "morocco-to-france", "morocco-to-spain", "france-to-morocco", "uk-to-morocco"]
    },

    "Pakistan": {
        "country_name": "Pakistan",
        "iso_alpha2": "PK",
        "iso_alpha3": "PAK",
        "region": "Asia",
        "subregion": "South Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Pakistan regulated by Ministry of National Food Security and Research. Importing pets to Pakistan is more complex; exporting pets from Pakistan (expats leaving) is a common use case. Authority: Animal Quarantine Department.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from some countries", "minimum_result": "0.5 IU/ml", "notes": "Verify current requirements with Animal Quarantine Department."},
            "quarantine": {"required": True, "duration_days": "7-14 days", "notes": "Quarantine inspection required. Duration depends on origin country and documentation status."},
            "import_permit": {"required": True, "issued_by": "Animal Quarantine Department, Ministry of National Food Security and Research", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": ["American Pit Bull Terrier", "Rottweiler"], "notes": "Some breeds face additional restrictions. Verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "Animal Quarantine Department"},
            "health_certificate": {"required": True, "notes": "Health certificate endorsed by national authority required for export."}
        },
        "popular_routes": ["pakistan-to-uk", "pakistan-to-uae", "pakistan-to-canada", "pakistan-to-australia", "uk-to-pakistan"]
    },

    "Bangladesh": {
        "country_name": "Bangladesh",
        "iso_alpha2": "BD",
        "iso_alpha3": "BGD",
        "region": "Asia",
        "subregion": "South Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Bangladesh regulated by Department of Livestock Services (DLS), Ministry of Fisheries and Livestock. Large diaspora in UK makes this an active export corridor.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml", "notes": "Verify with DLS."},
            "quarantine": {"required": True, "duration_days": "7 days minimum", "notes": "Quarantine inspection at entry point."},
            "import_permit": {"required": True, "issued_by": "Department of Livestock Services", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": [], "notes": "No specific breed ban list; local regulations may apply."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "DLS"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["bangladesh-to-uk", "bangladesh-to-uae", "bangladesh-to-canada", "uk-to-bangladesh"]
    },

    "Nepal": {
        "country_name": "Nepal",
        "iso_alpha2": "NP",
        "iso_alpha3": "NPL",
        "region": "Asia",
        "subregion": "South Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Nepal regulated by Department of Livestock Services (DoLS). Popular with expats and hikers. Export corridor to UK/Australia common for expats leaving.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": True, "duration_days": "7 days", "notes": "Quarantine inspection on arrival."},
            "import_permit": {"required": True, "issued_by": "Department of Livestock Services", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian"},
            "banned_breeds": {"banned": [], "notes": "No specific breed ban; verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "DoLS"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["nepal-to-uk", "nepal-to-australia", "nepal-to-canada", "uk-to-nepal"]
    },

    "Cambodia": {
        "country_name": "Cambodia",
        "iso_alpha2": "KH",
        "iso_alpha3": "KHM",
        "region": "Asia",
        "subregion": "South-Eastern Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Cambodia regulated by General Directorate of Animal Health and Production (GDAHP), Ministry of Agriculture, Forestry and Fisheries. Significant expat community (Phnom Penh, Siem Reap). Import and export processes can be complex.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Check with GDAHP; requirements change", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "Veterinary inspection on arrival. Quarantine if non-compliant."},
            "import_permit": {"required": True, "issued_by": "GDAHP", "apply_in_advance_weeks": 4},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian"},
            "banned_breeds": {"banned": [], "notes": "No specific list; verify with GDAHP."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "GDAHP"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["cambodia-to-uk", "cambodia-to-australia", "cambodia-to-singapore", "uk-to-cambodia", "singapore-to-cambodia"]
    },

    "Myanmar": {
        "country_name": "Myanmar",
        "iso_alpha2": "MM",
        "iso_alpha3": "MMR",
        "region": "Asia",
        "subregion": "South-Eastern Asia",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Myanmar regulated by Department of Animal Husbandry (DAH), Ministry of Agriculture, Livestock and Irrigation. Complex import/export processes. Expat community in Yangon.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": True, "duration_days": "14 days", "notes": "Quarantine at designated facility."},
            "import_permit": {"required": True, "issued_by": "DAH", "apply_in_advance_weeks": 8},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": ["American Pit Bull Terrier"], "notes": "Verify current breed restrictions with DAH."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "DAH"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["myanmar-to-uk", "myanmar-to-australia", "myanmar-to-singapore", "singapore-to-myanmar"]
    },

    "Peru": {
        "country_name": "Peru",
        "iso_alpha2": "PE",
        "iso_alpha3": "PER",
        "region": "Americas",
        "subregion": "South America",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Peru regulated by SENASA (Servicio Nacional de Sanidad Agraria). Growing expat community. Common export corridor to USA, Spain, UK.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from some countries (check SENASA list)", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "Veterinary inspection on arrival at Lima airport."},
            "import_permit": {"required": True, "issued_by": "SENASA Peru", "apply_in_advance_weeks": 4},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by SENASA"},
            "banned_breeds": {"banned": ["American Pit Bull Terrier"], "notes": "Lima and some regions have breed restrictions for PPP (Perros Potencialmente Peligrosos)."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "SENASA Peru"},
            "health_certificate": {"required": True, "notes": "SENASA-endorsed health certificate required for export."}
        },
        "popular_routes": ["peru-to-usa", "peru-to-spain", "peru-to-uk", "usa-to-peru", "spain-to-peru"]
    },

    "Ecuador": {
        "country_name": "Ecuador",
        "iso_alpha2": "EC",
        "iso_alpha3": "ECU",
        "region": "Americas",
        "subregion": "South America",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Ecuador regulated by AGROCALIDAD (Agencia de Regulacion y Control Fitosanitario y de Sanidad Animal). Quito and Guayaquil are entry points.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from some countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": False, "conditional_quarantine": True, "notes": "Veterinary inspection on arrival."},
            "import_permit": {"required": True, "issued_by": "AGROCALIDAD", "apply_in_advance_weeks": 4},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, AGROCALIDAD-endorsed"},
            "banned_breeds": {"banned": ["American Pit Bull Terrier", "Rottweiler", "Dogo Argentino"], "notes": "Municipal breed restrictions may apply."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "AGROCALIDAD"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["ecuador-to-usa", "ecuador-to-spain", "ecuador-to-uk", "usa-to-ecuador"]
    },

    "Costa_Rica": {
        "country_name": "Costa Rica",
        "iso_alpha2": "CR",
        "iso_alpha3": "CRI",
        "region": "Americas",
        "subregion": "Central America",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "high",
        "notes": "Costa Rica regulated by SENASA (Servicio Nacional de Salud Animal), part of Ministry of Agriculture and Livestock (MAG). Popular destination for North American and European expats. Relatively straightforward pet import process.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 3, "notes": "Vaccination must be current within 1 year (or per manufacturer's guidelines)."},
            "rabies_titre_test": {"required_for": "Not routinely required", "notes": "Costa Rica does not routinely require a titre test. Verify with SENASA for specific origins."},
            "quarantine": {"required": False, "notes": "No quarantine. Veterinary inspection on arrival. All documents must be in order."},
            "import_permit": {"required": True, "issued_by": "SENASA Costa Rica (online application)", "apply_in_advance_weeks": 2, "notes": "Import permit (Permiso de Importacion) required. Apply online via SENASA portal."},
            "health_certificate": {"required": True, "issued_by": "USDA/CFIA/APHA-endorsed vet (or equivalent national authority)", "valid_for_entry_days": 14},
            "banned_breeds": {"banned": ["American Pit Bull Terrier", "Rottweiler"], "notes": "Some municipalities restrict these breeds. Verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "SENASA Costa Rica"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["costa-rica-to-usa", "costa-rica-to-canada", "usa-to-costa-rica", "canada-to-costa-rica", "uk-to-costa-rica"]
    },

    "Ghana": {
        "country_name": "Ghana",
        "iso_alpha2": "GH",
        "iso_alpha3": "GHA",
        "region": "Africa",
        "subregion": "Western Africa",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Ghana regulated by the Veterinary Services Directorate (VSD), Ministry of Food and Agriculture. Accra is the main entry point. Expat community in Accra/Kumasi. Export corridor to UK common.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml", "notes": "Verify with VSD."},
            "quarantine": {"required": True, "duration_days": "7 days", "notes": "Government quarantine facility."},
            "import_permit": {"required": True, "issued_by": "Veterinary Services Directorate", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": [], "notes": "No official breed ban list; verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "Veterinary Services Directorate"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["ghana-to-uk", "ghana-to-canada", "ghana-to-usa", "uk-to-ghana"]
    },

    "Tanzania": {
        "country_name": "Tanzania",
        "iso_alpha2": "TZ",
        "iso_alpha3": "TZA",
        "region": "Africa",
        "subregion": "Eastern Africa",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Tanzania regulated by Tanzania Veterinary Laboratory Agency (TVLA) and the Ministry of Livestock and Fisheries. Dar es Salaam and Kilimanjaro are main entry points. Expat community present.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": True, "duration_days": "10 days minimum", "notes": "Government-approved quarantine facility required."},
            "import_permit": {"required": True, "issued_by": "Ministry of Livestock and Fisheries", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": [], "notes": "Verify current breed restrictions locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "TVLA"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["tanzania-to-uk", "tanzania-to-south-africa", "uk-to-tanzania", "south-africa-to-tanzania"]
    },

    "Ethiopia": {
        "country_name": "Ethiopia",
        "iso_alpha2": "ET",
        "iso_alpha3": "ETH",
        "region": "Africa",
        "subregion": "Eastern Africa",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "low",
        "notes": "Ethiopia regulated by Ethiopian Institute of Agricultural Research (EIAR) and Ministry of Agriculture Animal and Plant Health Regulatory Directorate. Addis Ababa is the main hub. Ethiopian Airlines hub makes this a transit point for Africa.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": True, "duration_days": "10 days", "notes": "Quarantine at designated facility."},
            "import_permit": {"required": True, "issued_by": "Ministry of Agriculture APHRD", "apply_in_advance_weeks": 8},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": [], "notes": "Verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "Ministry of Agriculture APHRD"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["ethiopia-to-uk", "ethiopia-to-canada", "uk-to-ethiopia", "uae-to-ethiopia"]
    },

    "Zimbabwe": {
        "country_name": "Zimbabwe",
        "iso_alpha2": "ZW",
        "iso_alpha3": "ZWE",
        "region": "Africa",
        "subregion": "Eastern Africa",
        "rabies_status": "not-rabies-free",
        "pet_friendliness": "moderate",
        "notes": "Zimbabwe regulated by the Department of Livestock and Veterinary Services, Ministry of Lands, Agriculture, Fisheries, Water and Rural Development. Harare is the main entry point. Expat and diaspora community active, mainly UK corridor.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Most countries", "minimum_result": "0.5 IU/ml"},
            "quarantine": {"required": True, "duration_days": "7-14 days", "notes": "Government quarantine facility, Harare."},
            "import_permit": {"required": True, "issued_by": "Department of Livestock and Veterinary Services", "apply_in_advance_weeks": 6},
            "health_certificate": {"required": True, "issued_by": "Official veterinarian, endorsed by national authority"},
            "banned_breeds": {"banned": [], "notes": "Verify locally."}
        },
        "export_requirements": {
            "export_permit": {"required": True, "issued_by": "Department of Livestock and Veterinary Services"},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["zimbabwe-to-uk", "zimbabwe-to-south-africa", "zimbabwe-to-australia", "uk-to-zimbabwe", "south-africa-to-zimbabwe"]
    },

    "Mauritius": {
        "country_name": "Mauritius",
        "iso_alpha2": "MU",
        "iso_alpha3": "MUS",
        "region": "Africa",
        "subregion": "Eastern Africa",
        "rabies_status": "rabies-free",
        "pet_friendliness": "low",
        "notes": "Mauritius is rabies-free and has extremely strict pet import controls similar to Australia. Pets must have lived in an approved rabies-free country for 6 months before import. Mandatory quarantine applies. Authority: Veterinary Services Division, Ministry of Agro-Industry and Food Security.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {
                "required_for": "All pets from most countries",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 180,
                "notes": "180-day residency requirement in approved country after successful titre test. Only pets from approved countries (similar to Australia Groups) accepted."
            },
            "quarantine": {
                "required": True,
                "duration_days": "30 days minimum",
                "facility": "Government quarantine station, Mauritius",
                "cost_responsibility": "Owner pays all costs",
                "notes": "Mandatory 30-day quarantine for all arriving pets. One of the longest quarantine periods globally."
            },
            "import_permit": {"required": True, "issued_by": "Veterinary Services Division, Ministry of Agro-Industry", "apply_in_advance_weeks": 12, "notes": "Extremely limited import permits issued. Apply well in advance."},
            "health_certificate": {"required": True, "issued_by": "Official government veterinarian in approved country", "valid_for_entry_days": 10},
            "banned_breeds": {
                "legislation": "Animal Welfare Act and Veterinary Services Division policy",
                "banned": ["American Pit Bull Terrier", "Dogo Argentino", "Japanese Tosa", "Fila Brasileiro"],
                "notes": "Banned breeds may not enter Mauritius under any circumstances."
            }
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True, "notes": "Veterinary Services Division health certificate."}
        },
        "popular_routes": ["mauritius-to-uk", "mauritius-to-australia", "mauritius-to-south-africa", "uk-to-mauritius", "south-africa-to-mauritius"]
    },

    "Slovakia": {
        "country_name": "Slovakia",
        "iso_alpha2": "SK",
        "iso_alpha3": "SVK",
        "region": "Europe",
        "subregion": "Central Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "moderate",
        "notes": "EU member. EU Regulation 576/2013 applies. Authority: State Veterinary and Food Administration (SVFA). No breed ban at national level.",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from non-listed third countries", "minimum_result": "0.5 IU/ml", "wait_after_test_days": 90},
            "quarantine": {"required": False, "conditional_quarantine": True},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or AHC", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "banned_breeds": {"legislation": "Animal Protection Act (Slovakia)", "banned": [], "notes": "No national breed ban. Some municipalities may have local restrictions."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["slovakia-to-uk", "slovakia-to-germany", "slovakia-to-australia", "uk-to-slovakia", "germany-to-slovakia"]
    },

    "Luxembourg": {
        "country_name": "Luxembourg",
        "iso_alpha2": "LU",
        "iso_alpha3": "LUX",
        "region": "Europe",
        "subregion": "Western Europe",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "EU member with one of the highest per-capita expat populations in the world (EU institutions, finance sector). EU Regulation 576/2013 applies. Authority: Administration des services veterinaires (ASV).",
        "import_requirements": {
            "microchip": {"required": True, "standard": "ISO 11784/11785"},
            "rabies_vaccination": {"required": True, "minimum_age_weeks": 12, "wait_after_first_vaccination_days": 21},
            "rabies_titre_test": {"required_for": "Pets from non-listed third countries", "minimum_result": "0.5 IU/ml", "wait_after_test_days": 90},
            "quarantine": {"required": False, "conditional_quarantine": True},
            "import_permit": {"required": False, "alternative": "EU pet passport or AHC"},
            "health_certificate": {"required": True, "name": "EU Pet Passport or AHC", "issued_by": "Official veterinarian", "valid_for_entry_days": 10},
            "banned_breeds": {"legislation": "Loi sur la detention des chiens dangereux", "banned": ["American Pit Bull Terrier", "American Staffordshire Terrier (unregistered)"], "notes": "Registered Staffordshire breeds allowed with conditions."}
        },
        "export_requirements": {
            "export_permit": {"required": False},
            "health_certificate": {"required": True}
        },
        "popular_routes": ["luxembourg-to-uk", "luxembourg-to-usa", "luxembourg-to-australia", "uk-to-luxembourg", "germany-to-luxembourg"]
    }
}


def main():
    print(f"Loading {DATA_FILE}...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing = set(data["countries"].keys())
    added = 0
    skipped = 0

    for slug, country_data in P4_COUNTRIES.items():
        if slug in existing:
            print(f"  SKIP (exists): {slug}")
            skipped += 1
        else:
            data["countries"][slug] = country_data
            print(f"  ADDED: {slug} ({country_data['country_name']})")
            added += 1

    # Update metadata
    data["metadata"]["description"] = f"Country pet import/export regulations database: P1 + P2 + P3 + P4 countries ({len(data['countries'])} total)"
    data["metadata"]["p4_countries_added"] = "2026-04-30"

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Added: {added}, Skipped: {skipped}. Total countries: {len(data['countries'])}")


if __name__ == "__main__":
    main()
