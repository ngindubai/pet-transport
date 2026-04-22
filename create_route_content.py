"""
Create Hugo content markdown files for all 15 Tier 1 route pages.
Each file has YAML front matter that references the data file.
Hugo renders these using layouts/routes/single.html.
"""
import json
import os

DATA_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\data\routes"
CONTENT_DIR = r"c:\Users\garet\Desktop\Research\pet-transport\site\content\routes"

os.makedirs(CONTENT_DIR, exist_ok=True)

# Create routes section index
with open(os.path.join(CONTENT_DIR, "_index.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: "Pet Transport Routes"
description: "International pet transport routes with step-by-step guides, airline options, and cost breakdowns."
---
""")

route_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".json")])

for rf in route_files:
    with open(os.path.join(DATA_DIR, rf), "r", encoding="utf-8") as f:
        data = json.load(f)

    origin = data["origin_name"]
    dest = data["destination_name"]
    rd = data["route_data"]
    seo = data.get("seo", {})

    # Build slug: origin-to-destination
    slug = rf.replace(".json", "")

    # Create markdown with full front matter
    # Hugo will read params from front matter and render with routes/single.html
    md = f"""---
title: "{seo.get('title', f'Pet Transport from {origin} to {dest}')}"
description: "{seo.get('description', f'Complete guide to transporting your pet from {origin} to {dest}.')}"
type: "routes"
layout: "single"
slug: "{slug}"
origin_name: "{origin}"
destination_name: "{dest}"
route_data:
  origin:
    code: "{rd['origin']['code']}"
    country: "{rd['origin']['country']}"
    export_requirements:
"""

    # Export requirements
    for key, val in rd["origin"].get("export_requirements", {}).items():
        safe_val = str(val).replace('"', '\\"')
        md += f'      {key}: "{safe_val}"\n'

    md += f"""  destination:
    code: "{rd['destination']['code']}"
    country: "{rd['destination']['country']}"
    import_requirements:
"""

    # Import requirements
    for key, val in rd["destination"].get("import_requirements", {}).items():
        safe_val = str(val).replace('"', '\\"')
        md += f'      {key}: "{safe_val}"\n'

    # Breed restrictions
    breed_restrictions = rd["destination"].get("breed_restrictions", [])
    if breed_restrictions:
        md += "    breed_restrictions:\n"
        for br in breed_restrictions:
            safe_br = str(br).replace('"', '\\"')
            md += f'      - "{safe_br}"\n'

    # Airlines
    md += "  airlines:\n"
    for airline in rd.get("airlines", []):
        md += f'    - name: "{airline["name"]}"\n'
        md += f'      type: "{airline["type"]}"\n'
        safe_policy = airline.get("policy_summary", "").replace('"', '\\"')
        md += f'      policy_summary: "{safe_policy}"\n'

    # Timeline steps
    md += "  timeline_steps:\n"
    for step in rd.get("timeline_steps", []):
        md += f'    - step: {step["step"]}\n'
        safe_action = step["action"].replace('"', '\\"')
        md += f'      action: "{safe_action}"\n'
        safe_timing = step["timing"].replace('"', '\\"')
        md += f'      timing: "{safe_timing}"\n'
        if step.get("responsible"):
            safe_resp = step["responsible"].replace('"', '\\"')
            md += f'      responsible: "{safe_resp}"\n'

    # Cost factors
    md += "  cost_factors:\n"
    for cf in rd.get("cost_factors", []):
        safe_cf = str(cf).replace('"', '\\"')
        md += f'    - "{safe_cf}"\n'

    # Key warnings
    md += "  key_warnings:\n"
    for kw in rd.get("key_warnings", []):
        safe_kw = str(kw).replace('"', '\\"')
        md += f'    - "{safe_kw}"\n'

    # Route metadata
    md += f'  route_complexity: "{rd.get("route_complexity", "moderate")}"\n'
    md += f'  estimated_timeline_weeks: "{rd.get("estimated_timeline_weeks", "8-12")}"\n'

    # Content
    content_data = data.get("content", {})
    safe_h1 = content_data.get("h1", f"Pet Transport from {origin} to {dest}").replace('"', '\\"')
    md += f'content:\n'
    md += f'  h1: "{safe_h1}"\n'
    md += f'  overview: |\n'
    for line in content_data.get("overview", "").split("\n"):
        md += f'    {line}\n'

    # Content sections
    sections = content_data.get("sections", [])
    if sections:
        md += "  sections:\n"
        for sec in sections:
            safe_heading = sec.get("heading", "").replace('"', '\\"')
            md += f'    - heading: "{safe_heading}"\n'
            md += f'      body: |\n'
            for line in sec.get("body", "").split("\n"):
                md += f'        {line}\n'

    # FAQs
    faqs = data.get("faqs", [])
    if faqs:
        md += "faqs:\n"
        for faq in faqs:
            safe_q = faq["question"].replace('"', '\\"')
            safe_a = faq["answer"].replace('"', '\\"')
            md += f'  - question: "{safe_q}"\n'
            md += f'    answer: "{safe_a}"\n'

    # Links (placeholder)
    md += """links:
  sideways: []
  upward: []
---
"""

    # Write content file
    content_path = os.path.join(CONTENT_DIR, f"{slug}.md")
    with open(content_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  Created: {slug}.md")

print(f"\nDone. {len(route_files)} route content files created in {CONTENT_DIR}")
