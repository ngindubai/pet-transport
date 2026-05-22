import os, re, random

base = 'site/content/routes/'
p4_origins = ['spain','new-zealand','oman','bahrain','jordan','finland','hungary','bulgaria','croatia','morocco','pakistan','bangladesh','nepal','cambodia','myanmar','peru','ecuador','costa-rica','ghana','tanzania','ethiopia','zimbabwe','mauritius','slovakia','luxembourg']

all_routes = [f for f in os.listdir(base) if f.endswith('.md') and f != '_index.md']
p4_routes = [f for f in all_routes if any(f.startswith(o+'-to-') for o in p4_origins)]

random.seed(42)
sample = random.sample(p4_routes, 10)
sample.sort()

print(f'Total P4 routes sampled from: {len(p4_routes)}')
print()
for fn in sample:
    txt = open(base+fn, encoding='utf-8').read()
    title_m = re.search(r'^title:\s*(.+)', txt, re.MULTILINE)
    desc_m = re.search(r'^description:\s*(.+)', txt, re.MULTILINE)
    faq_count = len(re.findall(r'question:', txt))
    has_h1 = 'h1:' in txt
    has_upward = 'upward:' in txt
    words = len(txt.split())
    title = title_m.group(1).strip().strip('"') if title_m else 'MISSING'
    desc = desc_m.group(1).strip().strip('"') if desc_m else 'MISSING'
    print(fn)
    print('  Title (' + str(len(title)) + ' chars): ' + title[:70])
    print('  Desc (' + str(len(desc)) + ' chars): ' + desc[:80])
    print('  FAQs: ' + str(faq_count) + '  H1: ' + str(has_h1) + '  Upward: ' + str(has_upward) + '  Words: ' + str(words))
    print()
