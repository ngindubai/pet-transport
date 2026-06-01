# MEMORY.md — PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO + content-driven lead generation — international pet transport
- **Stack:** Hugo static site generator + Python generation scripts + GitHub Actions CI/CD
- **Repository:** https://github.com/ngindubai/pet-transport (private)
- **Deploy:** Push to `main` triggers GitHub Actions automatically. Hugo build + incremental FTP to Hostinger. Live within ~80 seconds for a single article.

## Current State (2026-06-01)

- **Routes built:** 5,521 of ~37,830 country pairs (~14.6%)
- **Blog articles:** 412
- **Total pages:** ~6,319
- **Phase 7 progress:** Chunks 1-18 complete. Chunk 19 is next (Template B, Tier A routes).
- **Content plan:** Day 4 is next (`pet-transport-uk-to-spain`, 2026-06-04)
- **Enquiry tracker:** Live. PTG-001 to PTG-007 in sheet. Webhook v4 confirmed working.

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- CI workflow: `.github/workflows/deploy.yml` — triggers on push to `main`

### Slug Patterns
- Routes: `[origin-country]-to-[destination-country]` e.g. `united-kingdom-to-australia`
- Countries: `[country-slug]` e.g. `australia`
- Origins: `[country-slug]` or `[country-slug]-pet-export-guide`
- Airlines: `[airline-slug]` e.g. `emirates`
- Breeds: `[breed-slug]` e.g. `french-bulldog`
- Blog: `[descriptive-slug]` per content plan `url_slug` field

### Data File Locations
- Country regulations: `data/countries_pet_regulations.json` (75 countries)
- Government regulations: `data/govt_import_regulations.json`
- Airline policies: `data/airline_pet_policies.json`
- Breed restrictions: `data/breed_restrictions.json`
- Route keyword matrix: `data/route_keyword_matrix.json`

### Python Script Convention
All generation scripts use skip-if-exists to protect existing content.

### Deploy Pipeline
Every push to `main` triggers automatic deploy. Incremental FTP — only new/changed files uploaded. Do NOT delete `.ftp-deploy-sync-state.json` from Hostinger.

## Content Rules (Always On)

### Tone
- Warm, practical, expert. Pet owners are anxious — reassure without promising.
- British English throughout.
- Author: one of four named personas (see CLAUDE.md). Never use Gareth's real name.

### Hard Prohibitions
- No safety guarantees
- No banned vocabulary (see CLAUDE.md full list)
- No em dashes anywhere, ever
- No unverified regulatory claims — every claim must cite a named, dated official source

## Author Personas
- **Marcus Webb** (Senior Pet Relocation Consultant) — routes, logistics, costs, airline cargo
- **Dr. Sarah Okafor** (International Animal Health Consultant) — country guides, quarantine, DEFRA/APHIS/DAFF
- **Emma Hartley** (Animal Behaviourist & Pet Travel Adviser) — welfare, brachycephalic, anxiety, senior pets
- **James Osei** (Pet Transport Planning Specialist) — checklists, timelines, documentation, insurance

## SEO Status (2026-05-28)

- Duplicate FAQPage schema removed from blog template (microdata stripped from faq-accordion.html partial)
- buildFuture disabled in hugo.toml
- rebuild_link_graph_v3.py wires all routes to origin hubs and country guides on every build
- GSC: ~1,873 pages "Discovered — currently not indexed" (crawl budget issue, link graph fix deployed)
- Sitemaps: sitemap.xml (index) pointing to sitemap-routes.xml, sitemap-hubs.xml, sitemap-blog.xml, sitemap-pages.xml

## Content Plan

- **Plan file:** `content-plan/plan-rows-q1.js` (Q1: Jun-Aug 2026), q2, q3, q4
- **Total:** 252 articles, Mon-Fri
- **Published Days 1-3** (slugs: international-pet-transport-guide, cost-to-transport-a-pet-2026, pet-transport-uk-to-australia)
- **Day 7** (`how-to-choose-a-pet-transport-company`) also exists from a prior batch — skip when reached in sequence
- **Next: Day 4** — `pet-transport-uk-to-spain` — Pet Transport UK to Spain: 2026 Costs, Paperwork and Driving vs Flying
- Blog layout: `site/layouts/blog/single.html` — col-lg-8 content + col-lg-4 sidebar. Applies to all blog posts.

## Key Decisions Log

| Date | Decision | Why |
|------|----------|-----|
| 2026-04-22 | Standalone repo created | Separated from earlier monorepo |
| 2026-04-23 | Surge.sh replaced with Hostinger | Production domain secured |
| 2026-05-22 | 32,686 thin placeholder routes deleted | Rebuild block-by-block for quality |
| 2026-05-28 | Auto-deploy confirmed on push to main | No manual trigger needed |
| 2026-05-28 | Author personas introduced (4 named writers) | YMYL trust signals, avoid Gareth's real name |
| 2026-05-28 | buildFuture disabled | Prevents future-dated drafts from publishing |
| 2026-05-28 | rebuild_link_graph_v3.py runs on every build | Fixes crawl budget / indexing issue |

## Mistakes to Avoid
- Never run hugo from repo root — always `cd site` first (or the workflow handles it)
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- `rebuild_link_graph_v3.py` must run BEFORE hugo build
- Never fabricate quarantine periods or vaccine requirements
- The `live` branch is compiled output only — never edit it directly (if it exists)
- Never delete `.ftp-deploy-sync-state.json` from Hostinger
- `.github/workflows/deploy.yml` cannot be edited via MCP connector (GitHub 403) — provide full file for Gareth to paste via GitHub web editor
- No em dashes anywhere, ever
