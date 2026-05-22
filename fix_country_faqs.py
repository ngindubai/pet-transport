"""
Add 4th FAQ to new-zealand.md and spain.md country guides.
"""
import os, re

NZ_FAQ = """
  - question: "What breeds are banned or restricted in New Zealand?"
    answer: "New Zealand bans American Pit Bull Terriers, Dogo Argentinos, Brazilian Fila dogs, Japanese Tosa Inus, and Perro de Presa Canarios. If you own one of these breeds, importation is not permitted under any circumstances. Check the New Zealand Dog Control Act 1996 for the current list before making any plans."
"""

SPAIN_FAQ = """
  - question: "What breeds are banned or restricted in Spain?"
    answer: "Spain has breed-specific legislation at both national and regional level. At national level, restrictions apply to pit bull terriers, Rottweilers, Argentine Dogos, Fila Brasileiros, Tosa Inus, Akitas Inus, and dogs with similar characteristics. Some regions (including Catalonia and Aragon) have additional restrictions. Check with the relevant Spanish authority before travelling with any large or powerful breed."
"""

BASE = r"c:\Users\garet\Desktop\pet-transport\site\content\countries"

for fn, faq_text in [("new-zealand.md", NZ_FAQ), ("spain.md", SPAIN_FAQ)]:
    path = os.path.join(BASE, fn)
    content = open(path, encoding="utf-8").read()

    # Find insertion point: after the last FAQ answer, before next top-level key
    m = list(re.finditer(r"  - question:", content))
    if not m or len(m) < 3:
        print(f"  SKIP {fn}: fewer than 3 FAQs found")
        continue

    last_start = m[-1].start()
    after_last = content[last_start:]
    next_key = re.search(r"\n([a-z_]+):", after_last)
    if not next_key:
        print(f"  SKIP {fn}: could not find insertion point")
        continue

    insert_pos = last_start + next_key.start()
    new_content = content[:insert_pos] + faq_text + content[insert_pos:]

    faq_count_after = len(re.findall(r"question:", new_content))
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  Fixed {fn}: now has {faq_count_after} FAQs")
