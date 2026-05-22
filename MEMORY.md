# MEMORY.md — PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.surge.sh (surge.sh hosting, pending domain purchase)
- **Type:** Programmatic SEO — international pet transport route pages
- **Total pages:** 202 live (May 2025)
- **Stack:** Hugo static site generator + Python generation scripts + surge.sh deploy
- **Git:** `C:\Users\garet\Desktop\pet-transport\` (standalone VS Code instance)

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- Deploy command: `surge public pettransportglobal.surge.sh` from `site/`
- NOTE: surge deploy requires an interactive terminal session. Cannot be run from subagents.

### Slug Pattern
- Routes: `[origin-country]-to-[destination-country]` — e.g. `uk-to-australia`
- Countries: `[country-slug]` — e.g. `australia`
- Origins: `from-[country-slug]` — e.g. `from-uk`
- Airlines: `[airline-slug]` — e.g. `emirates`
- Breeds: `[breed-slug]` — e.g. `french-bulldog`

### Data File Locations
- Country regulations (P1): `data/countries_pet_regulations.json`
- Government official regulations: `data/govt_import_regulations.json`
- Airline policies: `data/airline_pet_policies.json`
- Breed restrictions: `data/breed_restrictions.json`
- Route keyword matrix: `data/route_keyword_matrix.json`
- Schema + tech stack: `data/schema_and_tech_stack.json`

### Front Matter Format (Hugo)
```yaml
---
title: "Pet Transport UK to Australia | PetTransportGlobal"
description: "140-160 char description with keyword and reassurance hook"
slug: "uk-to-australia"
date: 2025-01-01
draft: false
---
```

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

## Build Status

### Phase 0 — Research (Blocks 1-9): ALL DONE
All worker souls created, competitor scraped, government portals scraped, airline policies scraped, keyword matrix built, all databases assembled.

### Phase 1 — Foundation (Blocks 10-21): ALL DONE
- Block 10-11: Hugo scaffolding + 6 templates + quote form
- Block 12-15: 15 Tier 1 routes (initial batch), content + SEO pass
- Block 16: 10 country guides + 10 origin hubs
- Block 17: SEO pass + humanisation + internal linking
- Block 18: QA + first deploy
- Block 19: All 89 P1 routes complete (132 pages, deployed 21 April 2025)
- Block 20: 23 airline guide pages (190 pages total)
- Block 21: 35 breed guide pages (202 pages total, deployed)
- Blog: 12 articles live in site/content/blog/

### Review #1 Fixes (2026-04-22): ALL DONE
- 208 pages live, all 6 critical YMYL issues resolved (author attribution, FAQs, overviews, broken links, trust pages)

### Block 22 / Task 2.1: DONE (2026-04-23)
- P2 country regulation data — 15 additional countries added to data/countries_pet_regulations.json
- Database now: 25 countries (10 P1 + 15 P2)
- P2 countries: Japan, Thailand, Philippines, Malaysia, India, Portugal, Netherlands, Italy, Denmark, Mexico, Brazil, Switzerland, Indonesia, South Korea, Greece

### Design Fixes Applied (2026-04-23): LIVE
- Equal-height listing cards (.blog-box flexbox)
- Hero column split: col-lg-7 (text) + col-lg-5 (form) — dog visible on desktop
- Country carousel: new glass-dark country-feature-card design replacing plain adopt-cards
- Country card data: pulled from import_requirements.quarantine and import_requirements.rabies_vaccination
- Country card equal height: -webkit-line-clamp on stat values + owl-item flex stretch

### Phase 2 — Next Stage (Block 23): TODO
- 2.2: ~500 P2 route pages (Block 23) — NEXT
- 2.3: 15 P2 origin hubs + 15 P2 country guides (Block 24)
- 2.6: Internal link graph rebuild (Block 25)
- 2.9: Full QA + regulatory audit (Block 28)

## P1 Country Matrix (all routes DONE)
Countries: UK, UAE, Australia, USA, Singapore, France, Hong Kong, South Africa, Canada, Germany
10x10 grid = 90 combinations, 89 unique routes (no self-routes) + 3 bonus routes = 92 route files live

## P2 Countries (data ready, pages not yet generated)
Japan, Thailand, Philippines, Malaysia, India, Portugal, Netherlands, Italy, Denmark, Mexico, Brazil, Switzerland, Indonesia, South Korea, Greece

## Partial/Early P2 Countries (country + origins pages exist, not full route matrix)
- New Zealand (NZ): country guide, origins hub, UK-to-NZ and NZ-to-UK routes only
- Spain (ES): country guide, origins hub, spain-to-uk route only

## Open Strategic Decisions (Gareth's TODO list)
1. Domain purchase — pending
2. Business name — pending
3. Operator model vs marketplace model (affects all CTA copy and pricing display)
4. Payment processing (Stripe, GoCardless, etc.)
5. IPATA membership (~$400/year) — would add trust signal

## Mistakes to Avoid
- `hugo server` and `surge` both require live terminal (can't run from subagent in background)
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- Deploy from `site/` directory, not repo root
- Deploy command: `surge public pettransportglobal.surge.sh` (NOT `surge .`)
- Never fabricate quarantine periods or vaccine requirements — sources are mandatory
- Anti-template gate: route pages that feel identical will hurt SEO and user trust

## Session Log
| Date | Block | Description | Pages |
|------|-------|-------------|-------|
| Pre-migration | 1-21 | Phase 0 + 1 complete | 202 |
