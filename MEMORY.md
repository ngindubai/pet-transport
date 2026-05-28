# MEMORY.md — PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO — international pet transport route pages
- **Stack:** Hugo static site generator + Python generation scripts
- **Git:** `C:\Users\garet\Desktop\pet-transport\` (VS Code / GitHub Copilot)
- **Deploy:** Push to `main` → GitHub Actions builds Hugo → pushes compiled output to `live` branch → Hostinger Git OAuth auto-deploys

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- CI workflow: `.github/workflows/build-to-live.yml`

### Slug Pattern
- Routes: `[origin-country]-to-[destination-country]` — e.g. `united-kingdom-to-australia`
- Countries: `[country-slug]` — e.g. `australia`
- Origins: `[country-slug]` or `[country-slug]-pet-export-guide` — e.g. `united-kingdom.md`
- Airlines: `[airline-slug]` — e.g. `emirates`
- Breeds: `[breed-slug]` — e.g. `french-bulldog`

### Data File Locations
- Country regulations (P1): `data/countries_pet_regulations.json`
- Government official regulations: `data/govt_import_regulations.json`
- Airline policies: `data/airline_pet_policies.json`
- Breed restrictions: `data/breed_restrictions.json`
- Route keyword matrix: `data/route_keyword_matrix.json`

### Python Script Convention
All generation scripts use skip-if-exists:
```python
if os.path.exists(output_path):
    print(f"Skipping {output_path} — already exists")
    continue
```

## Content Rules (Always On)

### Tone
- Warm, practical, expert. Pet owners are anxious — reassure without promising.
- British English throughout (colour, licence [noun], travelling, etc.)

### Hard Prohibitions
- No safety guarantees: never "your pet will arrive safely" or "guaranteed safe delivery"
- No banned vocabulary: delve, tapestry, vibrant, crucial, comprehensive, meticulous, embark, robust, seamless, groundbreaking, leverage, synergy, transformative, paramount, multifaceted, myriad, cornerstone, reimagine, empower, catalyst, invaluable, bustling, nestled, realm
- No em dashes (zero tolerance)
- No unverified regulatory claims — every quarantine period, vaccine requirement, or breed ban must cite a named, dated official source

## Build Pipeline

### Local build (Windows)
```
build.bat
```
Runs: rebuild_link_graph_v3.py → hugo --gc --minify → split_sitemap.py

### CI build (GitHub Actions)
`.github/workflows/build-to-live.yml` runs on every push to main:
1. Set up Python 3.12
2. `python rebuild_link_graph_v3.py` — regenerate all internal links
3. Hugo build
4. `python split_sitemap.py` — split into section sitemaps
5. Force-push compiled output to `live` branch

### Key scripts
| Script | Purpose |
|--------|---------|
| `rebuild_link_graph_v3.py` | Scan all routes, update origin hubs + country guides with correct links |
| `split_sitemap.py` | Split Hugo's flat sitemap.xml into sitemap-routes/hubs/blog/pages.xml |
| `build.bat` | Windows local build (all 3 steps above) |
| `Makefile` | Linux/macOS local build (`make build`) |

## SEO Status (as of 2026-05-28)

### Issues fixed this session
1. **Duplicate FAQPage schema** — removed microdata from `faq-accordion.html` partial; JSON-LD in `blog/single.html` is now the sole FAQPage declaration. Affects all 413 blog posts.
2. **Future-dated content** — disabled `buildFuture = true` in hugo.toml. 16 articles dated June 2026 will need their frontmatter dates corrected.
3. **Internal link graph** — `rebuild_link_graph_v3.py` now wires all 5,152 routes to their origin hubs and destination country guides on every build.

### GSC status
- ~1,873 pages "Discovered — currently not indexed" (crawl budget issue, not sitemap)
- Sitemaps: sitemap.xml (index) → sitemap-routes.xml, sitemap-hubs.xml, sitemap-blog.xml, sitemap-pages.xml
- All sitemaps present and referenced in robots.txt
- Root cause of non-indexing: thin internal link graph (now fixed by v3 rebuild script)

## Build Status

### Live page counts (approximate, 2026-05-28)
- Route pages: ~5,152
- Blog articles: ~413
- Country guides: ~89
- Origin hubs: ~89
- Airline guides: ~23
- Breed guides: ~35
- Total: ~5,800+

### Open build tasks
- Fix frontmatter dates on 16 blog articles dated June 2026 (dropped from build due to buildFuture=false)
- Continue expanding route matrix (33,545 routes remaining per build plan)
- Monitor GSC indexing rate after link graph fix deploys

## Mistakes to Avoid
- Never run hugo from repo root — always `cd site` first
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- `rebuild_link_graph_v3.py` must run BEFORE hugo build (origin hub links need to exist as source)
- Never fabricate quarantine periods or vaccine requirements — sources are mandatory
- Anti-template gate: route pages that feel identical will hurt SEO and user trust
- The `live` branch is compiled output only — never edit it directly
- Race condition on simultaneous CI runs: if two pushes fire close together, one deploy may fail with ref lock error — this is normal, re-trigger if needed
