import json
d = json.load(open('data/countries_pet_regulations.json', encoding='utf-8'))['countries']
print(f"# total: {len(d)}")
for k, v in d.items():
    name = v.get('country_name') or v.get('name') or '?'
    iso = v.get('iso_code') or v.get('country_code') or '??'
    print(f'    "{k}": ("{name}", "{iso}"),')
