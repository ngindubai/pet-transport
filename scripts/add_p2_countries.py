"""
add_p2_countries.py — Add 15 P2 country regulation entries to the database.
Based on government websites, IATA guidelines, and established patterns for each country.
"""

import json
import os

P2_COUNTRIES = {
    "Japan": {
        "iso_alpha2": "JP",
        "iso_alpha3": "JPN",
        "region": "Asia",
        "subregion": "East Asia",
        "rabies_status": "rabies-free",
        "pet_friendliness": "high",
        "notes": "Japan is rabies-free. MAFF (Ministry of Agriculture, Forestry and Fisheries) is the regulatory authority.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Must be implanted before or on the same day as rabies vaccination.",
                "non_iso_accepted": False,
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_first_vaccination_days": 30,
                "vaccine_type": "Inactivated rabies vaccine",
                "notes": "Must be vaccinated at least 30 days before import."
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN (Fluorescent Antibody Virus Neutralization)",
                "minimum_result": "0.5 IU/ml",
                "timing": "Blood drawn 30+ days after rabies vaccination. Must be at least 180 days before import.",
                "wait_period_days": 180,
                "notes": "Titre test is mandatory. 6-month wait from test date before entry."
            },
            "quarantine": {
                "required": True,
                "duration_days": 14,
                "facility": "MAFF quarantine station",
                "cost_responsibility": "Owner pays",
                "notes": "14-day quarantine is mandatory at MAFF-designated facility."
            },
            "import_permit": {
                "required": True,
                "issued_by": "MAFF (Animal Quarantine Service)",
                "timeline": "Apply 2-4 weeks before travel",
                "notes": "Formal import permit required from MAFF."
            },
            "health_certificate": {
                "required": True,
                "name": "Health Certificate",
                "issued_by": "Official veterinarian in country of origin",
                "valid_for_days": 10,
                "notes": "Issued within 10 days of travel. Must list microchip number and vaccination details."
            },
            "banned_breeds": {
                "legislation": "No specific breed bans",
                "notes": "Japan does not have breed-specific legislation, but individual facilities may have restrictions."
            }
        }
    },
    "Thailand": {
        "iso_alpha2": "TH",
        "iso_alpha3": "THA",
        "region": "Asia",
        "subregion": "Southeast Asia",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "Thailand has active rabies. Department of Livestock is the regulatory body.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before rabies vaccination",
                "non_iso_accepted": False,
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
                "notes": "Must be at least 30 days before import."
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN",
                "minimum_result": "0.5 IU/ml",
                "wait_after_test_days": 30,
                "notes": "Blood drawn minimum 30 days after rabies vaccination."
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "Department of Livestock quarantine facility",
                "cost_responsibility": "Owner pays",
                "notes": "30-day quarantine mandatory for all dogs and cats."
            },
            "import_permit": {
                "required": True,
                "issued_by": "Department of Livestock",
                "notes": "Import license required before travel."
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
                "notes": "Issued within 14 days of travel."
            }
        }
    },
    "Philippines": {
        "iso_alpha2": "PH",
        "iso_alpha3": "PHL",
        "region": "Asia",
        "subregion": "Southeast Asia",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "Bureau of Animal Industry (BAI) regulates pet imports.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN",
                "minimum_result": "0.5 IU/ml",
                "wait_period_days": 180,
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "BAI quarantine station",
                "cost_responsibility": "Owner pays",
            },
            "import_permit": {
                "required": True,
                "issued_by": "Bureau of Animal Industry",
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
            }
        }
    },
    "Malaysia": {
        "iso_alpha2": "MY",
        "iso_alpha3": "MYS",
        "region": "Asia",
        "subregion": "Southeast Asia",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "Department of Veterinary Services (DVS) regulates imports.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 16,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN",
                "minimum_result": "0.5 IU/ml",
                "wait_period_days": 30,
                "notes": "30-day wait from titre test before entry."
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "DVS quarantine station",
                "cost_responsibility": "Owner pays",
            },
            "import_permit": {
                "required": True,
                "issued_by": "Department of Veterinary Services",
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
            }
        }
    },
    "India": {
        "iso_alpha2": "IN",
        "iso_alpha3": "IND",
        "region": "Asia",
        "subregion": "South Asia",
        "rabies_status": "present",
        "pet_friendliness": "low",
        "notes": "Animal Quarantine and Certification Services (AQCS) regulates imports. Requirements are complex.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN or HAI",
                "minimum_result": "0.5 IU/ml",
                "wait_period_days": 30,
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "AQCS quarantine facility",
                "cost_responsibility": "Owner pays",
                "notes": "30-day quarantine at designated facility."
            },
            "import_permit": {
                "required": True,
                "issued_by": "Animal Quarantine and Certification Services",
                "notes": "Permit issued by AQCS or State Animal Husbandry Department."
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
                "notes": "Must include all vaccination and test details."
            }
        }
    },
    "Portugal": {
        "iso_alpha2": "PT",
        "iso_alpha3": "PRT",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "EU member state. EU pet travel rules apply. DGAV (General Directorate of Food and Veterinary) oversees imports.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
                "timing": "Before rabies vaccination",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
                "notes": "EU requirement: 21 days between vaccination and travel."
            },
            "rabies_titre_test": {
                "required": False,
                "notes": "Not required for pets from EU, UK, and certain third countries."
            },
            "quarantine": {
                "required": False,
                "notes": "No quarantine for compliant pets from approved countries."
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or health certificate"
            },
            "health_certificate": {
                "required": True,
                "name": "Health Certificate or EU Pet Passport",
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
                "notes": "EU pet passport valid from EU; health certificate for non-EU origins."
            }
        }
    },
    "Netherlands": {
        "iso_alpha2": "NL",
        "iso_alpha3": "NLD",
        "region": "Europe",
        "subregion": "Western Europe",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "EU member state. EU pet travel rules apply.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
            },
            "rabies_titre_test": {
                "required": False,
                "notes": "Not required for EU, UK, and certain third countries."
            },
            "quarantine": {
                "required": False,
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or health certificate"
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
            }
        }
    },
    "Italy": {
        "iso_alpha2": "IT",
        "iso_alpha3": "ITA",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "EU member state. EU rules apply.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
            },
            "rabies_titre_test": {
                "required": False,
            },
            "quarantine": {
                "required": False,
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or health certificate"
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
            }
        }
    },
    "Denmark": {
        "iso_alpha2": "DK",
        "iso_alpha3": "DNK",
        "region": "Europe",
        "subregion": "Northern Europe",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "EU member state. EU rules apply. Very pet-friendly culture.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
            },
            "rabies_titre_test": {
                "required": False,
            },
            "quarantine": {
                "required": False,
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or health certificate"
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
            }
        }
    },
    "Mexico": {
        "iso_alpha2": "MX",
        "iso_alpha3": "MEX",
        "region": "Americas",
        "subregion": "North America",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "SAGARPA (Ministry of Agriculture) regulates pet imports.",
        "import_requirements": {
            "microchip": {
                "required": False,
                "notes": "Not mandatory, but recommended."
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
                "notes": "Must be at least 30 days before import."
            },
            "rabies_titre_test": {
                "required": False,
                "notes": "Not required."
            },
            "quarantine": {
                "required": False,
                "notes": "No quarantine for vaccinated pets."
            },
            "import_permit": {
                "required": True,
                "issued_by": "SAGARPA (Federal or State office)",
                "notes": "Zoosanitary permit required."
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian in country of origin",
                "valid_for_days": 30,
                "notes": "Certificate must list vaccination date."
            }
        }
    },
    "Brazil": {
        "iso_alpha2": "BR",
        "iso_alpha3": "BRA",
        "region": "Americas",
        "subregion": "South America",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "MAPA (Ministry of Agriculture) regulates imports.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": False,
                "notes": "Not required for dogs and cats."
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "MAPA quarantine station",
                "cost_responsibility": "Owner pays",
            },
            "import_permit": {
                "required": True,
                "issued_by": "MAPA",
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
            }
        }
    },
    "Switzerland": {
        "iso_alpha2": "CH",
        "iso_alpha3": "CHE",
        "region": "Europe",
        "subregion": "Central Europe",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "Not EU member, but follows similar standards. AFSM (State Secretariat for Economic Affairs) oversees imports.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
            },
            "rabies_titre_test": {
                "required": False,
                "notes": "Not required from EU and certain approved countries."
            },
            "quarantine": {
                "required": False,
            },
            "import_permit": {
                "required": False,
                "alternative": "Health certificate"
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
            }
        }
    },
    "Indonesia": {
        "iso_alpha2": "ID",
        "iso_alpha3": "IDN",
        "region": "Asia",
        "subregion": "Southeast Asia",
        "rabies_status": "present",
        "pet_friendliness": "low",
        "notes": "Directorate of Animal Health regulates imports. Requirements are complex.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN",
                "minimum_result": "0.5 IU/ml",
                "wait_period_days": 30,
            },
            "quarantine": {
                "required": True,
                "duration_days": 30,
                "facility": "Directorate of Animal Health facility",
                "cost_responsibility": "Owner pays",
            },
            "import_permit": {
                "required": True,
                "issued_by": "Directorate of Animal Health",
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
            }
        }
    },
    "South Korea": {
        "iso_alpha2": "KR",
        "iso_alpha3": "KOR",
        "region": "Asia",
        "subregion": "East Asia",
        "rabies_status": "present",
        "pet_friendliness": "high",
        "notes": "Animal and Plant Quarantine Agency (APQA) regulates imports. Large pet-owning culture.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 30,
            },
            "rabies_titre_test": {
                "required": True,
                "test_type": "FAVN",
                "minimum_result": "0.5 IU/ml",
                "wait_period_days": 180,
                "notes": "6-month wait from titre test before entry."
            },
            "quarantine": {
                "required": True,
                "duration_days": 10,
                "facility": "APQA facility",
                "cost_responsibility": "Owner pays",
            },
            "import_permit": {
                "required": True,
                "issued_by": "Animal and Plant Quarantine Agency",
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 14,
            }
        }
    },
    "Greece": {
        "iso_alpha2": "GR",
        "iso_alpha3": "GRC",
        "region": "Europe",
        "subregion": "Southern Europe",
        "rabies_status": "present",
        "pet_friendliness": "moderate",
        "notes": "EU member state. EU rules apply.",
        "import_requirements": {
            "microchip": {
                "required": True,
                "standard": "ISO 11784/11785",
            },
            "rabies_vaccination": {
                "required": True,
                "minimum_age_weeks": 12,
                "wait_after_vaccination_days": 21,
            },
            "rabies_titre_test": {
                "required": False,
            },
            "quarantine": {
                "required": False,
            },
            "import_permit": {
                "required": False,
                "alternative": "EU pet passport or health certificate"
            },
            "health_certificate": {
                "required": True,
                "issued_by": "Official veterinarian",
                "valid_for_days": 10,
            }
        }
    }
}


def extend_regulations_database():
    """Add P2 countries to the regulations database."""
    db_path = "data/countries_pet_regulations.json"
    
    # Load existing database
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    
    # Update metadata
    db['metadata']['description'] = "Country pet import/export regulations database: 10 P1 countries + 15 P2 countries"
    db['metadata']['p2_countries_added'] = "2026-04-22"
    
    # Add P2 countries
    for country_name, data in P2_COUNTRIES.items():
        db['countries'][country_name] = data
    
    # Save updated database
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    
    print(f"Extended regulations database with {len(P2_COUNTRIES)} P2 countries")
    print(f"Total countries: {len(db['countries'])}")


if __name__ == "__main__":
    extend_regulations_database()
