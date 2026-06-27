# MEMORY.md - PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO + content-driven lead generation. International pet transport
- **Stack:** Hugo static site generator + Python generation scripts + GitHub Actions CI/CD
- **Repository:** https://github.com/ngindubai/pet-transport (private)
- **Deploy:** Push to `main` triggers GitHub Actions automatically. Hugo build + incremental FTP to Hostinger. Live within ~80 seconds for a single article. After every build batch, the live URLs of new/changed pages are posted in chat for review (LIVE LINK REVIEW GATE in CLAUDE.md).

## Current State (2026-06-27, reconciled)

- **Routes built:** 6,094 of ~37,830 country pairs (~16.1%). All in `site/content/routes/`.
- **Blog articles:** 429 (Day 24 was a rewrite of existing stub, not a new file)
- **Total .md source files:** 6,896 (reconciled by verify_build_state.py, 2026-06-27)
- **Phase 7 progress:** Chunks 1-66 complete. **Chunk 67 is next** (Template B, Tier B). Tier A is fully complete (0 pairs remaining). Tier B remaining: 794.
- **Content plan:** Days 1-6 + Days 8-24 complete (24 articles written). Day 7 skipped (pre-existing). **Day 25 is next.**
- **Jamaica regulatory correction flagged:** Existing routes (jamaica-to-germany, jamaica-to-france, etc.) incorrectly state Jamaica is EU unlisted and requires FAVN titre test. Jamaica IS EU Group 2 listed (Implementing Regulation (EU) 2024/1130) - no titre test required. New Chunk 65/66 Jamaica routes use correct information. A future correction pass on the older Jamaica routes is needed.
- **Counts are never hand-edited.** Run `python verify_build_state.py` to check for drift and `--write` to reconcile.
- **Enquiry tracker:** Live. PTG-001 to PTG-007 in sheet. Webhook v4 confirmed working.
- **Route template redesign (live on all ~5,954 route pages):** Six new premium templates render via `site/layouts/routes/single.html` -> partials `route-new-{na,nb,nc,nd,ne,nl}.html` with scoped CSS.
  - **2026-06-10 reveal-bug fix (CRITICAL, resolved):** Opacity now always 1 on content; all reveal keyframes animate transform only.
  - **2026-06-19 upward link filter (Chunk 4a):** All 6 route partials that render upward links now use site.GetPage existence check before rendering, preventing broken origin hub links from appearing in HTML.
  - **2026-06-19 generator fix (Chunk 4b):** ORIGIN_HUB_URLS in generate_p3_routes_batch1.py now has correct plain-slug entries for 50 origins. scripts/repair_upward_links.py committed for bulk frontmatter repair.

### SEO Fix Plan (2026-06-19)
- **Chunk 3a-3c (funeral-repatriation):** Layout upward link filter + audit script + frontmatter repair committed.
- **Chunk 4a (pet-transport):** Layout upward link filter on all 6 route partials. Stops 114 hard 404s rendering.
- **Chunk 4b (pet-transport):** Generator ORIGIN_HUB_URLS fixed + repair script committed.
- **Chunk 5 (pet-transport):** 10 legacy duplicate route files deleted from site/content/pet-transport/ (canonical conflict causing 186 GSC "alternate canonical" entries). Replaced by proper routes/ versions.
- **Chunk 6 (close-protection):** NEXT
- **Chunk 7 (bus-hire):** Pending
- **Chunk 8 (mortgage-compare):** Pending

### DEPLOY INCIDENT 2026-06-19: 10 sequential deletes caused build race conditions
- **Symptom:** ~50% of the 10 Chunk 5 delete commits showed failed builds in GitHub Actions.
- **Root cause:** Each delete triggered a separate build. Builds raced writing to the orphan `live` branch.
- **Fix:** This commit (docs update) triggers one clean build from the correct main HEAD, which has all 10 deletions. The live branch will be rebuilt from scratch from this state.

### DEPLOY INCIDENT 2026-06-05: routine committed to feature branches
- **Root cause:** build-to-live.yml triggers only on push to `main`. Routine was committing to `claude/*` branches.
- **Fix:** Combined all three batches into one commit on main. Durable fix requires routine config change.

### Known legacy content debt
- **Author persona:** 248 of 412 blog articles authored as "Gareth" (pre-date the 2026-05-28 persona rule). Discrete future block.
- **JSON-LD double-quoting (pre-existing):** Blog JSON-LD wraps jsonify values in doubled quotes. Out of scope; fix in dedicated SEO pass.

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- CI workflow: `.github/workflows/build-to-live.yml` is the ACTIVE pipeline. Triggers on push to `main`.

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

### Deploy Pipeline
Every push to `main` triggers an automatic build+publish via `build-to-live.yml`. Hugo builds and publishes `site/public` to the orphan `live` branch, which Hostinger serves. `deploy.yml` (FTP) is `disabled_manually`.

### Docs + Live Link Review
Every build batch: (1) bundle BUILD-PLAN.md + build_state.json + MEMORY.md updates into the content commit, (2) let the automatic deploy run, (3) post the live URLs of all new/changed pages in chat for review.

## Content Rules (Always On)

### Tone
- Warm, practical, expert. British English throughout.
- Author: one of four named personas. Never use Gareth's real name.

### Hard Prohibitions
- No safety guarantees
- No banned vocabulary (see CLAUDE.md full list)
- No em dashes anywhere, ever
- No unverified regulatory claims

## Author Personas
- **Marcus Webb** (Senior Pet Relocation Consultant). Routes, logistics, costs, airline cargo
- **Dr. Sarah Okafor** (International Animal Health Consultant). Country guides, quarantine, DEFRA/APHIS/DAFF
- **Emma Hartley** (Animal Behaviourist & Pet Travel Adviser). Welfare, brachycephalic, anxiety, senior pets
- **James Osei** (Pet Transport Planning Specialist). Checklists, timelines, documentation, insurance

## Key Decisions Log

| Date | Decision | Why |
|------|----------|-----|
| 2026-04-22 | Standalone repo created | Separated from earlier monorepo |
| 2026-04-23 | Surge.sh replaced with Hostinger | Production domain secured |
| 2026-05-22 | 32,686 thin placeholder routes deleted | Rebuild block-by-block for quality |
| 2026-05-28 | Auto-deploy confirmed on push to main | No manual trigger needed |
| 2026-05-28 | Author personas introduced (4 named writers) | YMYL trust signals |
| 2026-05-28 | buildFuture disabled | Prevents future-dated drafts from publishing |
| 2026-05-28 | rebuild_link_graph_v3.py runs on every build | Fixes crawl budget / indexing issue |
| 2026-06-04 | Deploy docs corrected: build-to-live.yml is ACTIVE, deploy.yml disabled | Docs had them reversed |
| 2026-06-04 | Em-dash sweep complete | Zero em dashes in rendered HTML |
| 2026-06-04 | Blog template uses persona authors | single.html was hardcoded to Gareth |
| 2026-06-10 | Reveal-bug fix on all 6 route templates | Content was stuck at opacity:0 on live |
| 2026-06-19 | Chunk 4a: upward link filter on all route partials | 114 hard 404s from broken origin links |
| 2026-06-19 | Chunk 4b: generator ORIGIN_HUB_URLS fixed | Prevents new routes from inheriting the 404 bug |
| 2026-06-19 | Chunk 5: 10 legacy pet-transport/ route files deleted | Canonical conflict: both files built to same URL |

## Mistakes to Avoid
- Never run hugo from repo root. Always `cd site` first
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- `rebuild_link_graph_v3.py` must run BEFORE hugo build
- Never fabricate quarantine periods or vaccine requirements
- The `live` branch is compiled output only. Never edit it directly
- Never delete `.ftp-deploy-sync-state.json` from Hostinger
- `.github/workflows/*.yml` cannot be edited via MCP connector (GitHub 403)
- Never let a content commit go out without BUILD-PLAN.md + build_state.json + MEMORY.md update
- Never hand-edit count fields in build_state.json. Run `python verify_build_state.py --write`
- No em dashes anywhere, ever
- **Never do 10 sequential single-file deletes** — each triggers a separate build and they race on the live branch. Bundle all deletes into one push_files call or use the API to delete then make one trigger commit
