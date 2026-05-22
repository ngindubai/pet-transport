"""
PetTransportGlobal — Master Build Plan Generator v2
====================================================
Generates a comprehensive HTML build plan covering ALL possible
country-to-country route pairs from the 190-country list.

Outputs: pet-transport-build-plan.html (replaces existing)

Run from: pet-transport project root
Command:  python generate_build_plan_v2.py
"""
import os
import re
import sys
import json
from datetime import datetime
from math import sqrt

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
ROUTES_DIR = r"site\content\routes"
OUTPUT_FILE = r"pet-transport-build-plan.html"
GENERATED = datetime.now().strftime("%d %B %Y")

# ---------------------------------------------------------------------------
# COMPLETE 190-COUNTRY LIST (from existing build plan)
# ---------------------------------------------------------------------------
ALL_COUNTRIES_RAW = [
    "afghanistan", "albania", "algeria", "andorra", "angola",
    "antigua-and-barbuda", "argentina", "armenia", "australia", "austria",
    "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados",
    "belarus", "belgium", "belize", "benin", "bhutan",
    "bolivia", "bosnia-and-herzegovina", "botswana", "brazil", "brunei",
    "bulgaria", "burkina-faso", "burundi", "cabo-verde", "cambodia",
    "cameroon", "canada", "central-african-republic", "chad", "chile",
    "colombia", "comoros", "croatia", "cuba", "cyprus",
    "czech-republic", "denmark", "djibouti", "dominica", "dominican-republic",
    "dr-congo", "egypt", "el-salvador", "equatorial-guinea", "eritrea",
    "estonia", "eswatini", "fiji", "finland", "france",
    "gabon", "gambia", "georgia", "germany", "ghana",
    "greece", "grenada", "guatemala", "guinea", "guinea-bissau",
    "guyana", "haiti", "honduras", "hong-kong", "hungary",
    "iceland", "india", "indonesia", "iran", "iraq",
    "ireland", "israel", "italy", "ivory-coast", "jamaica",
    "japan", "jordan", "kazakhstan", "kenya", "kiribati",
    "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia",
    "lebanon", "lesotho", "liberia", "libya", "liechtenstein",
    "lithuania", "luxembourg", "macau", "madagascar", "malawi",
    "malaysia", "maldives", "mali", "malta", "marshall-islands",
    "mauritania", "mauritius", "mexico", "micronesia", "moldova",
    "monaco", "mongolia", "montenegro", "morocco", "mozambique",
    "namibia", "nauru", "nepal", "netherlands", "new-zealand",
    "nicaragua", "niger", "nigeria", "north-macedonia", "norway",
    "oman", "pakistan", "palau", "palestinian-territories", "panama",
    "papua-new-guinea", "paraguay", "philippines", "poland", "portugal",
    "qatar", "republic-of-congo", "romania", "russia", "rwanda",
    "saint-kitts-and-nevis", "saint-lucia", "saint-vincent-and-the-grenadines",
    "samoa", "san-marino", "sao-tome-and-principe", "saudi-arabia", "senegal",
    "serbia", "seychelles", "sierra-leone", "singapore", "slovenia",
    "solomon-islands", "somalia", "south-africa", "south-korea", "south-sudan",
    "spain", "sri-lanka", "sudan", "suriname", "sweden",
    "switzerland", "syria", "taiwan", "tajikistan", "thailand",
    "timor-leste", "togo", "tonga", "trinidad-and-tobago", "tunisia",
    "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine",
    "united-arab-emirates", "united-kingdom", "united-states", "uruguay",
    "uzbekistan", "vanuatu", "vatican-city", "venezuela", "vietnam",
    "yemen", "zambia", "zimbabwe",
    # Additional countries not in original alphabetical list
    "china",        # major expat origin — in built routes
    "costa-rica",
    "ecuador",
    "peru",
    "myanmar",
    "tanzania",
    "ethiopia",
    "slovakia",     # EU country — missing from main block
]
# Deduplicate preserving order
seen = set()
ALL_COUNTRIES = []
for c in ALL_COUNTRIES_RAW:
    if c not in seen:
        seen.add(c)
        ALL_COUNTRIES.append(c)

# Display name map (slug -> pretty name)
def slug_to_name(slug):
    special = {
        "united-kingdom": "United Kingdom",
        "united-states": "United States",
        "united-arab-emirates": "United Arab Emirates",
        "new-zealand": "New Zealand",
        "south-africa": "South Africa",
        "south-korea": "South Korea",
        "hong-kong": "Hong Kong",
        "saudi-arabia": "Saudi Arabia",
        "czech-republic": "Czech Republic",
        "dominican-republic": "Dominican Republic",
        "el-salvador": "El Salvador",
        "costa-rica": "Costa Rica",
        "ivory-coast": "Ivory Coast",
        "dr-congo": "DR Congo",
        "republic-of-congo": "Republic of Congo",
        "north-macedonia": "North Macedonia",
        "papua-new-guinea": "Papua New Guinea",
        "trinidad-and-tobago": "Trinidad and Tobago",
        "saint-kitts-and-nevis": "Saint Kitts and Nevis",
        "saint-lucia": "Saint Lucia",
        "saint-vincent-and-the-grenadines": "Saint Vincent and the Grenadines",
        "sao-tome-and-principe": "Sao Tome and Principe",
        "guinea-bissau": "Guinea-Bissau",
        "equatorial-guinea": "Equatorial Guinea",
        "burkina-faso": "Burkina Faso",
        "central-african-republic": "Central African Republic",
        "cabo-verde": "Cabo Verde",
        "marshall-islands": "Marshall Islands",
        "solomon-islands": "Solomon Islands",
        "antigua-and-barbuda": "Antigua and Barbuda",
        "bosnia-and-herzegovina": "Bosnia and Herzegovina",
        "sri-lanka": "Sri Lanka",
        "south-sudan": "South Sudan",
        "timor-leste": "Timor-Leste",
        "vatican-city": "Vatican City",
        "san-marino": "San Marino",
        "liechtenstein": "Liechtenstein",
        "palestinian-territories": "Palestinian Territories",
    }
    return special.get(slug, slug.replace("-", " ").title())

# ---------------------------------------------------------------------------
# COUNTRY PRIORITY WEIGHTS (1-10, higher = more traffic/value)
# ---------------------------------------------------------------------------
WEIGHTS = {
    "united-kingdom": 10.0, "united-states": 10.0,
    "united-arab-emirates": 9.5, "australia": 9.5,
    "canada": 9.0, "germany": 9.0,
    "france": 8.5, "singapore": 8.5,
    "hong-kong": 8.0, "south-africa": 8.0,
    "japan": 8.0, "south-korea": 7.8,
    "netherlands": 7.5, "switzerland": 7.5,
    "new-zealand": 7.5, "ireland": 7.2,
    "spain": 7.0, "italy": 7.0,
    "portugal": 7.0, "india": 7.0,
    "thailand": 6.8, "philippines": 6.5,
    "brazil": 6.5, "mexico": 6.5,
    "saudi-arabia": 6.5, "qatar": 6.3,
    "malaysia": 6.2, "indonesia": 6.0,
    "denmark": 6.0, "sweden": 6.0,
    "norway": 6.0, "finland": 6.0,
    "austria": 5.8, "belgium": 5.8,
    "greece": 5.5, "turkey": 5.5,
    "israel": 5.5, "jordan": 5.2,
    "kenya": 5.0, "nigeria": 5.0,
    "ghana": 5.0, "ethiopia": 5.0,
    "colombia": 5.0, "argentina": 5.0,
    "chile": 5.0, "peru": 4.8,
    "egypt": 4.8, "morocco": 4.8,
    "vietnam": 4.8, "taiwan": 4.8,
    "poland": 4.8, "czech-republic": 4.8,
    "hungary": 4.5, "romania": 4.5,
    "bulgaria": 4.5, "croatia": 4.5,
    "luxembourg": 4.5, "malta": 4.5,
    "cyprus": 4.5, "iceland": 4.5,
    "macau": 4.3, "sri-lanka": 4.3,
    "nepal": 4.3, "pakistan": 4.3,
    "bangladesh": 4.3, "cambodia": 4.0,
    "myanmar": 4.0, "laos": 3.8,
    "brunei": 3.8, "maldives": 4.0,
    "mauritius": 4.0, "seychelles": 3.8,
    "jamaica": 4.0, "trinidad-and-tobago": 3.8,
    "dominican-republic": 4.0, "costa-rica": 4.0,
    "panama": 3.8, "ecuador": 3.8,
    "uruguay": 3.8, "bolivia": 3.5,
    "paraguay": 3.5, "venezuela": 3.5,
    "colombia": 4.5, "guatemala": 3.5,
    "honduras": 3.5, "el-salvador": 3.5,
    "nicaragua": 3.5, "belize": 3.3,
    "guyana": 3.3, "suriname": 3.3,
    "armenia": 3.8, "georgia": 3.8,
    "azerbaijan": 3.8, "kazakhstan": 4.0,
    "uzbekistan": 3.8, "kyrgyzstan": 3.0,
    "tajikistan": 3.0, "turkmenistan": 3.0,
    "mongolia": 3.0, "russia": 3.5,
    "ukraine": 3.5, "belarus": 3.0,
    "moldova": 3.0, "serbia": 3.5,
    "north-macedonia": 3.0, "albania": 3.0,
    "kosovo": 3.0, "montenegro": 3.0,
    "bosnia-and-herzegovina": 3.0, "latvia": 3.5,
    "lithuania": 3.5, "estonia": 3.5,
    "slovakia": 3.5, "slovenia": 3.5,
    "rwanda": 3.5, "tanzania": 3.5,
    "uganda": 3.5, "zimbabwe": 3.5,
    "zambia": 3.3, "mozambique": 3.0,
    "namibia": 3.3, "botswana": 3.3,
    "eswatini": 3.0, "lesotho": 3.0,
    "malawi": 3.0, "madagascar": 3.0,
    "senegal": 3.0, "ivory-coast": 3.0,
    "cameroon": 3.0, "gabon": 2.8,
    "angola": 3.0, "zimbabwe": 3.2,
    "tunisia": 3.5, "algeria": 3.0,
    "libya": 2.8, "sudan": 2.8,
    "south-sudan": 2.5, "somalia": 2.0,
    "eritrea": 2.0, "djibouti": 2.5,
    "iran": 2.5, "iraq": 2.5,
    "syria": 2.0, "yemen": 2.0,
    "afghanistan": 2.0, "lebanon": 3.5,
    "oman": 4.5, "bahrain": 4.5,
    "kuwait": 4.5, "fiji": 3.5,
    "papua-new-guinea": 2.8, "solomon-islands": 2.3,
    "vanuatu": 2.3, "samoa": 2.3,
    "tonga": 2.3, "kiribati": 2.0,
    "nauru": 2.0, "tuvalu": 2.0,
    "palau": 2.3, "micronesia": 2.3,
    "marshall-islands": 2.0, "timor-leste": 2.3,
    "cuba": 2.5, "haiti": 2.0,
    "barbados": 3.3, "antigua-and-barbuda": 2.8,
    "grenada": 2.8, "dominica": 2.5,
    "saint-kitts-and-nevis": 2.5, "saint-lucia": 2.8,
    "saint-vincent-and-the-grenadines": 2.5,
    "benin": 2.5, "togo": 2.5,
    "nigeria": 4.0, "niger": 2.0,
    "mali": 2.0, "burkina-faso": 2.0,
    "guinea": 2.0, "guinea-bissau": 2.0,
    "sierra-leone": 2.0, "liberia": 2.0,
    "gambia": 2.5, "cape-verde": 2.5,
    "cabo-verde": 2.5, "sao-tome-and-principe": 2.0,
    "comoros": 2.0, "mauritania": 2.0,
    "chad": 2.0, "central-african-republic": 2.0,
    "dr-congo": 2.0, "republic-of-congo": 2.0,
    "equatorial-guinea": 2.0, "burundi": 2.0,
    "bhutan": 2.5, "andorra": 2.5,
    "monaco": 2.5, "san-marino": 2.0,
    "liechtenstein": 2.5, "vatican-city": 2.0,
    "palestinian-territories": 2.5,
    "taiwan": 5.0,  # override - popular expat destination
    "china": 7.5,   # large expat community, major origin country
    "slovakia": 3.5,
}

def get_weight(slug):
    return WEIGHTS.get(slug, 3.0)

def score_pair(origin, dest):
    """Score a country pair. Higher = higher priority to build."""
    ow = get_weight(origin)
    dw = get_weight(dest)
    # Geometric mean of weights, boosted for high-traffic pairs
    base = (ow * dw) ** 0.5
    # Bonus for UK/US/UAE/AU routes
    tier1 = {"united-kingdom", "united-states", "united-arab-emirates", "australia", "canada"}
    if origin in tier1 or dest in tier1:
        base = min(base * 1.1, 10.0)
    return round(base, 2)

def tier_for_score(s):
    if s >= 7.0:   return "A"   # both countries high-value
    elif s >= 5.5: return "B"   # one high / one medium
    elif s >= 4.0: return "C"   # medium both
    else:          return "D"   # long tail

# ---------------------------------------------------------------------------
# TEMPLATE ROTATION (6 templates, repeating)
# ---------------------------------------------------------------------------
TEMPLATES = ["Legacy", "A-FieldManual", "B-Journey", "C-Comparison", "D-QA", "E-Data"]
TEMPLATE_VARIANTS = [None, "A", "B", "C", "D", "E"]  # None = legacy

def tmpl_for_chunk(chunk_idx):
    return TEMPLATES[chunk_idx % 6]

def tmpl_variant_for_chunk(chunk_idx):
    return TEMPLATE_VARIANTS[chunk_idx % 6]

# ---------------------------------------------------------------------------
# LOAD BUILT ROUTES
# ---------------------------------------------------------------------------
print("Loading built routes...")
built_slugs = set()
if os.path.isdir(ROUTES_DIR):
    for f in os.listdir(ROUTES_DIR):
        if f.endswith(".md") and f != "_index.md":
            built_slugs.add(f[:-3])  # strip .md
print(f"  Found {len(built_slugs)} built routes")

# ---------------------------------------------------------------------------
# GENERATE ALL PAIRS
# ---------------------------------------------------------------------------
print("Generating all country pairs...")
all_pairs = []
for origin in ALL_COUNTRIES:
    for dest in ALL_COUNTRIES:
        if origin != dest:
            slug = f"{origin}-to-{dest}"
            built = slug in built_slugs
            sc = score_pair(origin, dest)
            all_pairs.append({
                "slug": slug,
                "origin": origin,
                "dest": dest,
                "origin_name": slug_to_name(origin),
                "dest_name": slug_to_name(dest),
                "score": sc,
                "tier": "S" if built else tier_for_score(sc),
                "built": built,
            })

total_pairs = len(all_pairs)
built_count = sum(1 for p in all_pairs if p["built"])
unbuilt = [p for p in all_pairs if not p["built"]]
print(f"  Total pairs: {total_pairs}")
print(f"  Built: {built_count}")
print(f"  Remaining: {len(unbuilt)}")

# Sort unbuilt by score desc
unbuilt_sorted = sorted(unbuilt, key=lambda x: -x["score"])

# Tier breakdown
tier_a = [p for p in unbuilt_sorted if p["tier"] == "A"]
tier_b = [p for p in unbuilt_sorted if p["tier"] == "B"]
tier_c = [p for p in unbuilt_sorted if p["tier"] == "C"]
tier_d = [p for p in unbuilt_sorted if p["tier"] == "D"]
print(f"  Tier A: {len(tier_a)}, B: {len(tier_b)}, C: {len(tier_c)}, D: {len(tier_d)}")

# Organise into chunks of 10 (A first, then B, C, D)
ordered_unbuilt = tier_a + tier_b + tier_c + tier_d
chunks = [ordered_unbuilt[i:i+10] for i in range(0, len(ordered_unbuilt), 10)]
print(f"  Total chunks: {len(chunks)}")

# ---------------------------------------------------------------------------
# COUNTRY STATS (for the tracker table)
# ---------------------------------------------------------------------------
from collections import defaultdict
origin_stats = defaultdict(lambda: {"built": 0, "total": 0, "remaining": 0})
for p in all_pairs:
    origin_stats[p["origin"]]["total"] += 1
    if p["built"]:
        origin_stats[p["origin"]]["built"] += 1
    else:
        origin_stats[p["origin"]]["remaining"] += 1

# Sort by built desc
sorted_origins = sorted(origin_stats.keys(), key=lambda x: -origin_stats[x]["built"])

# ---------------------------------------------------------------------------
# HTML HELPERS
# ---------------------------------------------------------------------------
CSS = """
:root{
  --bg:#f8f7f4;--surface:#fff;--border:#e2dfd8;--ink:#1a1a1a;--ink-mute:#666;
  --accent:#1a5fa8;--green:#2a7a3b;--amber:#b8861f;--red:#b53636;
  --s:#0d6e2f;--a:#1a5fa8;--b:#5c6bc0;--c:#888;--d:#999;
  --tleg:#5c4b8a;--ta:#1a5fa8;--tb:#27ae60;--tc:#c0392b;--td:#e67e22;--te:#8e44ad;
  --radius:5px;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:13px;background:var(--bg);color:var(--ink);line-height:1.5}
header{background:var(--ink);color:#fff;padding:24px 36px}
header h1{font-size:20px;font-weight:700}
header p{opacity:.65;font-size:12px;margin-top:3px}
.wrap{max-width:1400px;margin:0 auto;padding:20px 20px}
h2{font-size:15px;font-weight:700;margin:24px 0 8px;padding-bottom:5px;border-bottom:2px solid var(--border)}
h3{font-size:12px;font-weight:700;margin:10px 0 4px;color:var(--ink-mute)}
.context-box{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:12px 16px;margin-bottom:16px;font-size:12px}
.stat-row{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:8px 14px;min-width:100px;text-align:center}
.stat .num{font-size:22px;font-weight:800;line-height:1}
.stat .lbl{font-size:9px;color:var(--ink-mute);margin-top:2px;text-transform:uppercase;letter-spacing:.4px}
.badge{display:inline-block;font-size:9px;font-weight:700;padding:1px 5px;border-radius:2px;letter-spacing:.3px;white-space:nowrap;vertical-align:middle}
.bs{background:#d4edda;color:var(--s)}.ba{background:#dce8f7;color:var(--a)}
.bb{background:#e8eaf6;color:var(--b)}.bc{background:#f0f0f0;color:var(--c)}.bd{background:#f5f5f5;color:var(--d)}
.t-leg{background:#ede7f6;color:var(--tleg)}.t-a{background:#dce8f7;color:var(--ta)}
.t-b{background:#d4edda;color:var(--tb)}.t-c{background:#fde8e8;color:var(--tc)}
.t-d{background:#fef3e2;color:var(--td)}.t-e{background:#f3e8f8;color:var(--te)}
table{width:100%;border-collapse:collapse;font-size:11px;background:var(--surface)}
th{background:#f2f0eb;padding:6px 8px;text-align:left;font-size:9px;text-transform:uppercase;letter-spacing:.4px;color:var(--ink-mute);border-bottom:2px solid var(--border)}
td{padding:5px 8px;border-bottom:1px solid var(--border);vertical-align:top}
code{background:#f0f0f0;padding:0 4px;border-radius:2px;font-family:monospace;font-size:10px}
pre{background:#1a1a2e;color:#cdd6f4;padding:10px 12px;border-radius:var(--radius);font-size:11px;overflow-x:auto;white-space:pre-wrap;line-height:1.45;margin:0}
.callout{border-left:3px solid var(--amber);background:#fffbf0;padding:8px 12px;margin:8px 0;border-radius:0 var(--radius) var(--radius) 0;font-size:11px}
details{margin:4px 0}
summary{cursor:pointer;padding:8px 12px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);font-size:11px;font-weight:700;list-style:none;display:flex;align-items:center;gap:6px;user-select:none}
summary::before{content:'▶';font-size:8px;color:var(--ink-mute);flex-shrink:0;margin-right:2px}
details[open]>summary{border-radius:var(--radius) var(--radius) 0 0;border-bottom:none}
details[open]>summary::before{content:'▼'}
.chunk-body{padding:10px 12px;border:1px solid var(--border);border-top:none;border-radius:0 0 var(--radius) var(--radius);background:#fafafa}
.chunk-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px}
@media(max-width:900px){.chunk-grid{grid-template-columns:1fr}}
.prompt-wrap{position:relative}
.copy-btn{position:absolute;top:6px;right:6px;background:#3a3a5c;color:#aac;border:none;padding:2px 8px;border-radius:2px;font-size:9px;cursor:pointer}
.copy-btn:hover{background:#5a5a8c}
nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.96);border-bottom:1px solid var(--border);padding:5px 20px;font-size:11px;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
nav a{color:var(--accent);text-decoration:none;font-weight:700}
.tmpl-key{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.tk{display:flex;align-items:center;gap:5px;font-size:10px;padding:3px 7px;border-radius:2px;background:var(--surface);border:1px solid var(--border)}
.chunk-meta{display:flex;align-items:center;gap:6px;flex:1;min-width:0}
.cnum{font-size:12px;font-weight:800;color:var(--ink-mute);min-width:68px;flex-shrink:0}
.cpages{font-size:10px;color:var(--ink-mute);margin-left:auto;flex-shrink:0}
.section-divider{margin:20px 0 6px;padding:8px 12px;background:var(--ink);color:#fff;border-radius:var(--radius);font-size:12px;font-weight:700}
.progress-bar-outer{background:#e8e8e8;border-radius:6px;height:10px;width:100%;margin:4px 0}
.progress-bar-inner{background:var(--green);border-radius:6px;height:10px}
.tracker-table td:nth-child(3){min-width:80px}
.filter-row{display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap}
.filter-row input,.filter-row select{padding:5px 8px;border:1px solid var(--border);border-radius:var(--radius);font-size:11px;background:var(--surface)}
"""

JS = r"""
function copyPrompt(id) {
  const el = document.getElementById(id);
  if (!el) return;
  navigator.clipboard.writeText(el.innerText).then(() => {
    const btn = document.querySelector('[data-for="' + id + '"]');
    if (btn) { btn.textContent = 'Copied!'; setTimeout(()=>btn.textContent='Copy', 1500); }
  });
}
function filterTracker() {
  const q = document.getElementById('tracker-filter').value.toLowerCase();
  const show = document.getElementById('tracker-status').value;
  const rows = document.querySelectorAll('#tracker-tbody tr');
  rows.forEach(r => {
    const txt = r.dataset.origin || '';
    const status = r.dataset.status || '';
    const matchQ = !q || txt.includes(q);
    const matchS = !show || status === show;
    r.style.display = (matchQ && matchS) ? '' : 'none';
  });
}
"""

TMPL_BADGE = {
    "Legacy": '<span class="badge t-leg">Legacy</span>',
    "A-FieldManual": '<span class="badge t-a">A–FieldManual</span>',
    "B-Journey": '<span class="badge t-b">B–Journey</span>',
    "C-Comparison": '<span class="badge t-c">C–Comparison</span>',
    "D-QA": '<span class="badge t-d">D–QA</span>',
    "E-Data": '<span class="badge t-e">E–Data</span>',
}

TIER_BADGE = {
    "S": '<span class="badge bs">S</span>',
    "A": '<span class="badge ba">A</span>',
    "B": '<span class="badge bb">B</span>',
    "C": '<span class="badge bc">C</span>',
    "D": '<span class="badge bd">D</span>',
}

# ---------------------------------------------------------------------------
# BUILD PROMPT TEXT
# ---------------------------------------------------------------------------
def build_prompt(chunk_pages, tmpl_variant):
    variant_line = f'template_variant: "{tmpl_variant}"' if tmpl_variant else "(omit — uses default legacy template)"
    lines = [
        "Build 10 pet transport route pages for PetTransportGlobal.",
        "",
        f"TEMPLATE: {variant_line}",
        "",
        "ROUTES TO BUILD:",
    ]
    for i, p in enumerate(chunk_pages, 1):
        lines.append(f"  {i:>2}. {p['slug']}  ({p['origin_name']} → {p['dest_name']}, score: {p['score']})")
    lines += [
        "",
        "INSTRUCTIONS:",
        "1. File path for each: site/content/routes/{slug}.md",
        "2. Check an existing route page for frontmatter structure.",
        "3. Populate all route_data fields: import requirements, microchip/vaccine rules,",
        "   quarantine, airline options, estimated timeline and cost factors.",
        "4. Do NOT create a file if it already exists in site/content/routes/.",
        "5. Build ALL 10 routes before stopping.",
        "6. When finished, list the exact filenames created.",
        "7. After all 10: run hugo --gc --minify from site/ and report page count.",
    ]
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# BUILD CHUNK HTML
# ---------------------------------------------------------------------------
def build_chunk_html(chunk_idx, pages):
    tmpl = tmpl_for_chunk(chunk_idx)
    tmpl_variant = tmpl_variant_for_chunk(chunk_idx)
    global_num = chunk_idx + 1
    already_built_chunks = built_count // 10  # approximate
    overall_num = already_built_chunks + global_num

    tmpl_badge = TMPL_BADGE.get(tmpl, "")
    prompt_id = f"pp{chunk_idx}"
    prompt_text = build_prompt(pages, tmpl_variant)

    rows_html = ""
    for i, p in enumerate(pages, 1):
        tier_badge = TIER_BADGE.get(p["tier"], "")
        rows_html += (
            f'<tr><td style="color:var(--ink-mute);text-align:center">{i}</td>'
            f'<td>{tier_badge}</td>'
            f'<td><strong>{p["origin_name"]} → {p["dest_name"]}</strong><br>'
            f'<code>{p["slug"]}</code></td>'
            f'<td style="text-align:center">{p["score"]}</td></tr>'
        )

    return f"""
<details>
<summary><div class="chunk-meta">
  <span class="cnum">Chunk {global_num}</span>
  {tmpl_badge} <span style="font-size:10px;color:var(--ink-mute)">#{(chunk_idx*10)+1}–#{(chunk_idx*10)+len(pages)}</span>
  <span class="cpages">10 pages</span>
</div></summary>
<div class="chunk-body"><div class="chunk-grid">
<div>
  <h3>Sonnet prompt — paste into VS Code chat</h3>
  <div class="prompt-wrap">
    <button class="copy-btn" data-for="{prompt_id}" onclick="copyPrompt('{prompt_id}')">Copy</button>
    <pre id="{prompt_id}">{prompt_text}</pre>
  </div>
</div>
<div>
  <h3>Pages in this chunk</h3>
  <table><thead><tr><th>#</th><th>Tier</th><th>Route slug</th><th>Score</th></tr></thead>
  <tbody>{rows_html}</tbody></table>
</div>
</div></div></details>"""

# ---------------------------------------------------------------------------
# BUILD TRACKER TABLE (origin-level summary)
# ---------------------------------------------------------------------------
def build_tracker_html():
    rows = ""
    for origin in sorted_origins:
        stats = origin_stats[origin]
        pct = round(stats["built"] / stats["total"] * 100) if stats["total"] > 0 else 0
        bar_w = pct
        status = "complete" if pct == 100 else ("active" if pct > 0 else "todo")
        status_badge = {
            "complete": '<span class="badge bs">DONE</span>',
            "active": '<span class="badge ba">IN PROGRESS</span>',
            "todo": '<span class="badge bd">TODO</span>',
        }[status]
        rows += (
            f'<tr data-origin="{origin}" data-status="{status}">'
            f'<td><strong>{slug_to_name(origin)}</strong><br>'
            f'<code>{origin}</code></td>'
            f'<td style="text-align:center">{stats["built"]}</td>'
            f'<td style="text-align:center">{stats["remaining"]}</td>'
            f'<td style="text-align:center">{stats["total"]}</td>'
            f'<td><div class="progress-bar-outer">'
            f'<div class="progress-bar-inner" style="width:{bar_w}%"></div></div>'
            f'<span style="font-size:9px;color:var(--ink-mute)">{pct}%</span></td>'
            f'<td>{status_badge}</td>'
            f'</tr>'
        )
    return f"""
<div class="filter-row">
  <input type="text" id="tracker-filter" placeholder="Filter by country..." oninput="filterTracker()" style="width:200px">
  <select id="tracker-status" onchange="filterTracker()">
    <option value="">All statuses</option>
    <option value="complete">Done</option>
    <option value="active">In Progress</option>
    <option value="todo">Todo</option>
  </select>
</div>
<table class="tracker-table">
<thead><tr>
  <th>Country</th>
  <th style="text-align:center">Built</th>
  <th style="text-align:center">Remaining</th>
  <th style="text-align:center">Total</th>
  <th>Progress</th>
  <th>Status</th>
</tr></thead>
<tbody id="tracker-tbody">{rows}</tbody>
</table>"""

# ---------------------------------------------------------------------------
# TIER SECTIONS
# ---------------------------------------------------------------------------
def build_tier_section(tier_label, tier_color, tier_desc, tier_pages, start_chunk_idx, tier_id):
    chunk_count = (len(tier_pages) + 9) // 10
    chunks_html = ""
    for i in range(0, len(tier_pages), 10):
        chunk_pages = tier_pages[i:i+10]
        chunk_html = build_chunk_html(start_chunk_idx + (i // 10), chunk_pages)
        chunks_html += chunk_html

    return f"""
<div class="section-divider" id="{tier_id}">
  Tier {tier_label} — {tier_desc} — {len(tier_pages):,} pages, {chunk_count:,} chunks
</div>
{chunks_html}
""", chunk_count

# ---------------------------------------------------------------------------
# ASSEMBLE FULL HTML
# ---------------------------------------------------------------------------
print("Assembling HTML...")

pct_done = round(built_count / total_pairs * 100, 1)

# Calculate chunk starts
a_start = 0
b_start = (len(tier_a) + 9) // 10
c_start = b_start + (len(tier_b) + 9) // 10
d_start = c_start + (len(tier_c) + 9) // 10

tier_a_html, a_chunks = build_tier_section(
    "A", "var(--a)", "High priority — score ≥ 8.5", tier_a, a_start, "tier-a"
)
tier_b_html, b_chunks = build_tier_section(
    "B", "var(--b)", "Medium priority — score 7.0–8.4", tier_b, b_start, "tier-b"
)
tier_c_html, c_chunks = build_tier_section(
    "C", "var(--c)", "Standard — score 5.0–6.9", tier_c, c_start, "tier-c"
)
tier_d_html, d_chunks = build_tier_section(
    "D", "var(--d)", "Long tail — score < 5.0", tier_d, d_start, "tier-d"
)

tracker_html = build_tracker_html()

total_chunks = a_chunks + b_chunks + c_chunks + d_chunks

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pet Transport Global — Master Build Plan (All {total_pairs:,} Routes)</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Pet Transport Global — Master Build Plan</h1>
  <p>{total_pairs:,} possible routes ({len(ALL_COUNTRIES)} countries &times; {len(ALL_COUNTRIES)-1}) &mdash;
     {built_count:,} built ({pct_done}%) &mdash; {len(ordered_unbuilt):,} remaining &mdash;
     {total_chunks:,} chunks of 10 &mdash; Generated {GENERATED}</p>
</header>

<nav>
  <a href="#overview">Overview</a>
  <a href="#tracker">Tracker</a>
  <a href="#tier-a">Tier A ({len(tier_a):,})</a>
  <a href="#tier-b">Tier B ({len(tier_b):,})</a>
  <a href="#tier-c">Tier C ({len(tier_c):,})</a>
  <a href="#tier-d">Tier D ({len(tier_d):,})</a>
</nav>

<div class="wrap">

<h2 id="overview">Overview</h2>
<div class="stat-row">
  <div class="stat"><div class="num" style="color:var(--green)">{built_count:,}</div><div class="lbl">Built (Tier S)</div></div>
  <div class="stat"><div class="num" style="color:var(--a)">{len(tier_a):,}</div><div class="lbl">Tier A queued</div></div>
  <div class="stat"><div class="num" style="color:var(--b)">{len(tier_b):,}</div><div class="lbl">Tier B queued</div></div>
  <div class="stat"><div class="num" style="color:var(--c)">{len(tier_c):,}</div><div class="lbl">Tier C queued</div></div>
  <div class="stat"><div class="num" style="color:var(--d)">{len(tier_d):,}</div><div class="lbl">Tier D queued</div></div>
  <div class="stat"><div class="num">{total_pairs:,}</div><div class="lbl">Total possible</div></div>
  <div class="stat"><div class="num">{total_chunks:,}</div><div class="lbl">Remaining chunks</div></div>
  <div class="stat"><div class="num">{pct_done}%</div><div class="lbl">Complete</div></div>
</div>

<div class="context-box">
<strong>How to use:</strong> Work chunks in order (Tier A → B → C → D). Open a chunk,
copy the prompt, paste into VS Code chat in the pet-transport repo. Sonnet builds all 10 pages,
you move to the next chunk. Tier A = highest value routes (both countries score &ge;8.5).
Complete all Tier A before starting B, etc.
<br><br>
<strong>Country count:</strong> {len(ALL_COUNTRIES)} countries &mdash;
<strong>Total possible directional pairs:</strong> {len(ALL_COUNTRIES)} &times; {len(ALL_COUNTRIES)-1} = {total_pairs:,} &mdash;
<strong>Progress:</strong> {built_count:,} / {total_pairs:,} ({pct_done}%) &mdash;
<strong>Remaining:</strong> {len(ordered_unbuilt):,} routes in {total_chunks:,} chunks
</div>

<h2 id="templates">Template rotation</h2>
<div class="context-box">
<div class="tmpl-key">
  <div class="tk"><span class="badge t-leg">Legacy</span> <span>Legacy — balanced prose, how-to structure</span></div>
  <div class="tk"><span class="badge t-a">A–FieldManual</span> <span>A — Field Manual (tabular, regulation-first)</span></div>
  <div class="tk"><span class="badge t-b">B–Journey</span> <span>B — Journey (narrative, pet owner perspective)</span></div>
  <div class="tk"><span class="badge t-c">C–Comparison</span> <span>C — Comparison (airline tables, route options)</span></div>
  <div class="tk"><span class="badge t-d">D–QA</span> <span>D — Q&amp;A (FAQ-led, triggers FAQ schema)</span></div>
  <div class="tk"><span class="badge t-e">E–Data</span> <span>E — Data (compliance tables, stats-dense)</span></div>
</div>
</div>

<h2 id="tracker">Country Progress Tracker</h2>
<div class="context-box">Routes built per origin country. All {len(ALL_COUNTRIES)} countries shown.
Use the filter to find a specific country or status.</div>
{tracker_html}

{tier_a_html}
{tier_b_html}
{tier_c_html}
{tier_d_html}

</div><!-- /wrap -->

<script>{JS}</script>
</body>
</html>"""

# ---------------------------------------------------------------------------
# WRITE OUTPUT
# ---------------------------------------------------------------------------
print(f"Writing {OUTPUT_FILE}...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

size_mb = os.path.getsize(OUTPUT_FILE) / 1_000_000
print(f"\nDone! {OUTPUT_FILE} — {size_mb:.1f} MB")
print(f"\nSummary:")
print(f"  Countries:      {len(ALL_COUNTRIES)}")
print(f"  Total pairs:    {total_pairs:,}")
print(f"  Built:          {built_count:,} ({pct_done}%)")
print(f"  Remaining:      {len(ordered_unbuilt):,}")
print(f"    Tier A:       {len(tier_a):,} ({a_chunks} chunks)")
print(f"    Tier B:       {len(tier_b):,} ({b_chunks} chunks)")
print(f"    Tier C:       {len(tier_c):,} ({c_chunks} chunks)")
print(f"    Tier D:       {len(tier_d):,} ({d_chunks} chunks)")
print(f"  Total chunks:   {total_chunks:,}")
