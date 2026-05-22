"""
Add a 4th FAQ to all [origin]-to-united-states.md routes that only have 3 FAQs.
The new FAQ covers CDC dog import requirements - unique to US destination routes.
"""
import os, re

US_ROUTES_DIR = r"c:\Users\garet\Desktop\pet-transport\site\content\routes"

CDC_FAQ = """  - question: "What are the CDC requirements for dogs entering the United States?"
    answer: "The US Centers for Disease Control (CDC) requires all dogs entering the United States to have a microchip and valid rabies vaccination. Dogs vaccinated outside the US, or those that have lived outside the US, must arrive through a CDC-approved facility. Dogs from certain high-risk rabies countries face additional screening steps. Check the current CDC Dog Import requirements at cdc.gov/importation before finalising your travel plans."
"""

fixed = 0
for fn in sorted(os.listdir(US_ROUTES_DIR)):
    if not fn.endswith(".md") or fn == "_index.md":
        continue
    path = os.path.join(US_ROUTES_DIR, fn)
    content = open(path, encoding="utf-8").read()

    # Only process files with exactly 3 FAQs
    faq_count = len(re.findall(r"question:", content))
    if faq_count != 3:
        continue

    # Only process routes going TO united-states
    if not fn.endswith("-to-united-states.md"):
        continue

    # Insert the new FAQ just before the 'links:' block
    # The FAQ section ends right before 'links:'
    if "links:" not in content:
        print(f"  SKIP (no links block): {fn}")
        continue

    # Find position: insert CDC FAQ before 'links:'
    insert_pos = content.index("links:")
    new_content = content[:insert_pos] + CDC_FAQ + content[insert_pos:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    fixed += 1
    print(f"  Fixed: {fn} ({faq_count} → 4 FAQs)")

print(f"\nTotal fixed: {fixed} files")
