# MEMORY.md - PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO + content-driven lead generation. International pet transport
- **Stack:** Hugo static site generator + Python generation scripts + GitHub Actions CI/CD
- **Repository:** https://github.com/ngindubai/pet-transport (private)
- **Deploy:** Push to `main` triggers GitHub Actions automatically. Hugo build + incremental FTP to Hostinger. Live within ~80 seconds for a single article. After every build batch, the live URLs of new/changed pages are posted in chat for review (LIVE LINK REVIEW GATE in CLAUDE.md).

## Current State (2026-06-04, reconciled from disk by verify_build_state.py)

- **Routes built:** 5,172 of ~37,830 country pairs (~13.7%). This is the true on-disk count (5,162 in `routes/` + 10 route pairs in `pet-transport/`). The old 5,534/5,544 figures were inflated by hand-incrementing and have been corrected.
- **Blog articles:** 412
- **Total .md source files:** 5,957 (build_state.json `total_site_pages`). The full deployed page total, including Hugo taxonomy and list pages, is verified from the live sitemap.xml after a build.
- **Phase 7 progress:** Chunks 1-20 complete. **Chunk 21 is next** (Template D, Conversational Q&A, Tier A). ~160 Tier A routes remain.
- **Content plan:** Day 4 is next (`pet-transport-uk-to-spain`). Day 4 is a **replace-in-place** of the existing `uk-to-spain-pet-transport-complete-guide.md`, not a new article (see Content Plan section).
- **Counts are never hand-edited.** Run `python verify_build_state.py` to check for drift and `--write` to reconcile. A SessionStart hook runs the check automatically at the start of every web session.
- **Enquiry tracker:** Live. PTG-001 to PTG-007 in sheet. Webhook v4 confirmed working.

### Known legacy content debt (tracked)
- **Em dashes:** CLEARED 2026-06-04. Removed from all 89 affected files (74 blog+routes, 11 pet-transport, 4 static). Zero em dashes remain in site/content.
- **Author persona:** 248 of 412 blog articles are authored as "Gareth" (pre-date the 2026-05-28 persona rule). Should be backfilled to the four named personas. Discrete future block: "author persona backfill".

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- CI workflow: `.github/workflows/deploy.yml`. Triggers on push to `main`. This is the only active deploy workflow.

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
Every push to `main` triggers automatic deploy. Incremental FTP. Only new/changed files uploaded. Do NOT delete `.ftp-deploy-sync-state.json` from Hostinger. There is exactly one active deploy workflow (deploy.yml); the old build-to-live.yml has been retired to stop two pipelines racing on one push.

### Docs + Live Link Review (added 2026-06-02)
Every build batch does three things together, every time: (1) bundle BUILD-PLAN.md + build_state.json + MEMORY.md updates into the content commit, (2) let the automatic deploy run, (3) post the live URLs of all new/changed pages in chat for review. This keeps the docs from drifting and means nothing reaches the live site unreviewed, even though deploy is automatic. Full rules in CLAUDE.md (MANDATORY DOCS UPDATE + LIVE LINK REVIEW GATE).

## Content Rules (Always On)

### Tone
- Warm, practical, expert. Pet owners are anxious. Reassure without promising.
- British English throughout.
- Author: one of four named personas (see CLAUDE.md). Never use Gareth's real name.

### Hard Prohibitions
- No safety guarantees
- No banned vocabulary (see CLAUDE.md full list)
- No em dashes anywhere, ever
- No unverified regulatory claims. Every claim must cite a named, dated official source

## Author Personas
- **Marcus Webb** (Senior Pet Relocation Consultant). Routes, logistics, costs, airline cargo
- **Dr. Sarah Okafor** (International Animal Health Consultant). Country guides, quarantine, DEFRA/APHIS/DAFF
- **Emma Hartley** (Animal Behaviourist & Pet Travel Adviser). Welfare, brachycephalic, anxiety, senior pets
- **James Osei** (Pet Transport Planning Specialist). Checklists, timelines, documentation, insurance

## SEO Status (2026-05-28)

- Duplicate FAQPage schema removed from blog template (microdata stripped from faq-accordion.html partial)
- buildFuture disabled in hugo.toml
- rebuild_link_graph_v3.py wires all routes to origin hubs and country guides on every build
- GSC: ~1,873 pages "Discovered, currently not indexed" (crawl budget issue, link graph fix deployed)
- Sitemaps: sitemap.xml (index) pointing to sitemap-routes.xml, sitemap-hubs.xml, sitemap-blog.xml, sitemap-pages.xml

## Content Plan

- **Plan file:** `content-plan/plan-rows-q1.js` (Q1: Jun-Aug 2026), q2, q3, q4
- **Total:** 252 articles, Mon-Fri
- **Published Days 1-3** (slugs: international-pet-transport-guide, cost-to-transport-a-pet-2026, pet-transport-uk-to-australia)
- **Day 7** (`how-to-choose-a-pet-transport-company`) also exists from a prior batch. Skip when reached in sequence
- **Next: Day 4** - `pet-transport-uk-to-spain` - Pet Transport UK to Spain: 2026 Costs, Paperwork and Driving vs Flying. **DECISION (2026-06-03): replace in place.** A UK-to-Spain article already exists at `uk-to-spain-pet-transport-complete-guide.md` (thin, 743 words, authored as Gareth, contains em dashes). Day 4 upgrades that existing file to full quality and keeps its URL. Do NOT publish a second `pet-transport-uk-to-spain` page (duplicate content). This mirrors the Day 7 "already exists" handling.
- Blog layout: `site/layouts/blog/single.html`. col-lg-8 content + col-lg-4 sidebar. Applies to all blog posts.

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
| 2026-06-02 | LIVE LINK REVIEW GATE adopted | Deploy is automatic, so the safety gate moves to after publish: post live URLs of all new/changed pages in chat for review after every build batch |
| 2026-06-02 | Retired build-to-live.yml | Two workflows both fired on push (deploy.yml + build-to-live.yml). Kept deploy.yml only so builds do not race on the sitemap and FTP state file |
| 2026-06-02 | Docs update every build batch (not just session end) | Stops the three docs drifting from reality between sessions |
| 2026-06-02 | Chunk 19 complete | 10 Tier A quality routes (Template B), Germany/HK/NZ corridors |
| 2026-06-03 | Truth audit + anti-drift safeguards | Docs had drifted four ways on the route count (5524/5534/5544 vs ~5172 on disk). Root cause: routes_built was a hand-incremented tally never reconciled to disk. Added verify_build_state.py (single source of truth, counts from disk, `--write` reconciles) and a SessionStart hook that runs it every session. All four docs corrected to true numbers |
| 2026-06-03 | Day 4 UK-to-Spain = replace in place | Existing thin uk-to-spain-pet-transport-complete-guide.md will be upgraded in place rather than publishing a duplicate `pet-transport-uk-to-spain` page |
| 2026-06-04 | Em-dash sweep complete | Removed all em dashes from site/content: 74 blog+route files + 11 pet-transport + 4 static (89 files). Python sweeper logic: table rows -> colon, headings/bold labels -> colon, author fields -> comma, prose -> comma. Zero em dashes remain |

## Mistakes to Avoid
- Never run hugo from repo root. Always `cd site` first (or the workflow handles it)
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- `rebuild_link_graph_v3.py` must run BEFORE hugo build
- Never fabricate quarantine periods or vaccine requirements
- The `live` branch is compiled output only. Never edit it directly (and build-to-live.yml that produced it is now retired)
- Never delete `.ftp-deploy-sync-state.json` from Hostinger
- `.github/workflows/*.yml` cannot be edited via MCP connector (GitHub 403). Provide full file for Gareth to paste via GitHub web editor
- Never let a content commit go out without the BUILD-PLAN.md + build_state.json + MEMORY.md update and the live review links
- Never hand-edit count fields in build_state.json (routes_built, blog_articles, total_site_pages). They drift. Run `python verify_build_state.py --write` to reconcile from disk
- No em dashes anywhere, ever
