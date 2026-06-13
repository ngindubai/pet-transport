# MEMORY.md - PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO + content-driven lead generation. International pet transport
- **Stack:** Hugo static site generator + Python generation scripts + GitHub Actions CI/CD
- **Repository:** https://github.com/ngindubai/pet-transport (private)
- **Deploy:** Push to `main` triggers GitHub Actions automatically. Hugo build + incremental FTP to Hostinger. Live within ~80 seconds for a single article. After every build batch, the live URLs of new/changed pages are posted in chat for review (LIVE LINK REVIEW GATE in CLAUDE.md).

## Current State (2026-06-13, reconciled from disk by verify_build_state.py)

- **Routes built:** 5,706 of ~37,830 country pairs (~15.1%). True on-disk count (5,696 in `routes/` + 10 in `pet-transport/`).
- **Blog articles:** 425
- **Total .md source files:** 6,504 (build_state.json `total_site_pages`). Full deployed page total, including Hugo taxonomy, verified from live sitemap.xml after a build.
- **Phase 7 progress:** Chunks 1-50 complete. **Chunk 51 is next** (Template A, Tier B). Tier A is fully complete (0 pairs remaining). Chunk 50 (Template E, Tier B): 25 routes: AU/CA/US to LB/RW/UG; IT to AM/AZ/GE/KZ/LB/RW/UG; NL to AM/AZ/GE/KZ/LB/RW/UG; ES to RW/UG.
- **Content plan:** Days 1-6 + Days 8-18 complete (18 articles written). Day 7 skipped (pre-existing). **Day 19 is next:** check content-plan/plan-rows-q1.js for slug. Day 18 = importing-pets-to-indonesia-2026 (Dr. Sarah Okafor, ~2200 words, rekomendasi permit, Bali dog ban via Jakarta mainland entry, FAVN titre, quarantine 7-14 days, cost ranges).
- **Counts are never hand-edited.** Run `python verify_build_state.py` to check for drift and `--write` to reconcile. A SessionStart hook runs the check automatically at the start of every web session.
- **Enquiry tracker:** Live. PTG-001 to PTG-007 in sheet. Webhook v4 confirmed working.
- **Route template redesign (live on all ~5,531 route pages):** Six new premium templates render via `site/layouts/routes/single.html` -> partials `route-new-{na,nb,nc,nd,ne,nl}.html` with scoped CSS `static/css/route-new-{na..nl}.css`. Variant routing: front-matter `template_variant` A->na, B->nb, C->nc, D->nd, E->ne, legacy->nl.
  - **2026-06-10 reveal-bug fix (CRITICAL, resolved):** Content was invisible on live (`.r` reveal elements stuck at opacity:0; the IntersectionObserver adding `.in` did not fire on deployed pages). Permanent fix: opacity is now ALWAYS 1 on content; all content-reveal keyframes (tplReveal, fadeUp, slideInLeft, fadeIn, counterUp, checkPop) animate transform only, never opacity. RULE GOING FORWARD: never let opacity:0 be the resting state of content, and never make content visibility depend on JS firing or an animation completing. Also fixed route_complexity underscore ("Very_high" -> "Very High") via replaceRE.
  - Local-only test artifact: `.claude/launch.json` (preview server config) is NOT committed.

### DEPLOY INCIDENT 2026-06-05: routine committed to feature branches, never to main (ROOT CAUSE + FIX)

- **Symptom:** Three routine runs reported "committed + live" in Slack, but nothing ever reached the live site.
- **Root cause:** `build-to-live.yml` triggers only on `push: branches: [main]`. The routine was committing to a per-session `claude/<random>` feature branch instead of `main`, so the GitHub Action never fired and Hostinger never updated. Because `main` never advanced, every run re-read `next_chunk: 25` and rebuilt "chunk 25" with a different, overlapping set of routes. Three branches resulted: `youthful-volta-fHktH`, `youthful-volta-ubyDO`, `eloquent-bell-grEAl`, each with 25 routes, ~54 unique after dedup.
- **Immediate fix (done):** Combined all three batches into one commit on `main`, deduped overlapping slugs, QA'd the full set, reconciled counts from disk, pushed to `main` to trigger the deploy. Routes 5,217 -> 5,254.
- **Durable fix (REQUIRED, owner action):** The routine's STEP 3 already says `git push origin HEAD:main`, but a conflicting "Git Development Branch Requirements" block pins it to a `claude/*` feature branch and says never push elsewhere without permission. That block wins, so work never lands on main. The routine config must be changed so the working/push branch is `main` (or a merge-to-main step added). This is cloud routine config, not in-repo, so it cannot be self-edited from a session. Until changed, every scheduled run will again strand its work on a feature branch and re-build the same chunk number.

### Known legacy content debt (tracked)
- **Em dashes:** CLEARED 2026-06-04 from all rendered content: site/content (89 files), the blog/route-C/route-A/breeds templates, llms.txt, and countries_pet_regulations.json. Verified by local Hugo build: 0 em dashes in rendered HTML. Remaining em dashes are only in code comments (CSS/PHP/Hugo template headers) and vendor bootstrap.min.css, which do not render as page content.
- **Author persona:** 248 of 412 blog articles are authored as "Gareth" (pre-date the 2026-05-28 persona rule). The blog template now renders whatever the author field says (fixed 2026-06-04), so a backfill of these 248 articles will now actually change the visible byline. Discrete future block: "author persona backfill". NOTE: llms.txt also still says "authored by Gareth, Founder" and should be updated in that block.
- **JSON-LD double-quoting (pre-existing):** blog JSON-LD wraps jsonify values in doubled quotes (e.g. `"name": "\"Marcus Webb\""`), affecting headline, description, and author. Present on unchanged lines too, so it pre-dates this work. Likely a minifier interaction. Out of scope; fix in a dedicated SEO pass.

## Build Decisions

### Architecture
- Hugo static site in `site/` subdirectory
- Python scripts at **repo root** (not in `scripts/` folder)
- All Hugo content in `site/content/[section]/`
- Build command: `hugo --gc --minify` from `site/`
- CI workflow: `.github/workflows/build-to-live.yml` is the ACTIVE pipeline. Triggers on push to `main`, builds Hugo, publishes `site/public` to the `live` branch (served by Hostinger). `deploy.yml` (FTP to Hostinger) is currently `disabled_manually` on GitHub. Verified 2026-06-04. (Docs previously had this backwards.)

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
Every push to `main` triggers an automatic build+publish via `build-to-live.yml` (the ACTIVE workflow, verified on GitHub 2026-06-04): it builds Hugo and publishes `site/public` to the orphan `live` branch, which Hostinger serves. `deploy.yml` (the FTP-to-Hostinger workflow) is currently `disabled_manually` and does NOT run. Earlier notes claimed deploy.yml was the only active workflow and build-to-live.yml was retired; that was backwards and is corrected here. If switching back to the FTP pipeline, re-enable deploy.yml and disable build-to-live.yml in the GitHub Actions tab, and do NOT delete `.ftp-deploy-sync-state.json` from Hostinger.

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
- Day 4: `uk-to-spain-pet-transport-complete-guide` replaced in place 2026-06-04 (full rewrite 743 -> 2115 words, Marcus Webb)
- Day 5: `pet-transport-uk-to-usa` published 2026-06-05 (new article, 2266 words, Marcus Webb, post-CDC reset angle)
- Day 6: `pet-transport-europe-to-uk` published 2026-06-05 (new article, 2400 words, Marcus Webb)
- Day 7: `how-to-choose-a-pet-transport-company` - SKIPPED (pre-existing article)
- Day 8: `cheap-pet-transport-honest-look` published 2026-06-06 (new article, 1800 words, Marcus Webb, cost transparency angle)
- Day 9: `pet-transport-uk-to-jersey` published 2026-06-06 (1600 words, Marcus Webb, Condor ferry, Channel Islands rules)
- Day 10: `pet-transport-uae-to-pakistan` published 2026-06-07 (2000 words, Marcus Webb, AQD NOC, AED 3,000-6,000)
- Day 11: `exporting-pets-from-singapore` published 2026-06-08 (2400 words, Marcus Webb, AVS export licence, FAVN titre for AU, Changi cargo, UK/EU/US/AU matrix)
- **Next: Day 12** - check content-plan/plan-rows-q1.js for slug (importing-pets-to-australia-2026)
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
| 2026-06-03 | Day 4 UK-to-Spain = replace in place | Existing thin uk-to-spain-pet-transport-complete-guide.md upgraded in place; no duplicate page. Done 2026-06-04: full rewrite 743 -> 2115 words, Marcus Webb author, costs + driving vs flying angle, 6 FAQs |
| 2026-06-04 | Em-dash sweep complete | Removed all em dashes from site/content: 74 blog+route files + 11 pet-transport + 4 static (89 files). Python sweeper logic: table rows -> colon, headings/bold labels -> colon, author fields -> comma, prose -> comma. Zero em dashes remain |
| 2026-06-04 | Deploy docs were BACKWARDS, corrected | Verified on GitHub: build-to-live.yml is ACTIVE (publishes `live` branch, Hostinger serves it); deploy.yml (FTP) is disabled_manually. Docs (incl the 2026-06-02 "Retired build-to-live.yml" row above) had it reversed. The 2026-06-02 row is left for history but is factually wrong: build-to-live.yml was never actually retired |
| 2026-06-04 | Blog template now uses persona authors | single.html hardcoded "Gareth" in byline, bio, and JSON-LD, ignoring the author front matter. Fixed to parse the author field (handles both "Name - Title, Org" legacy and "Name, Title, Org" formats). Persona backfill on the 248 Gareth-authored articles is now meaningful (was a no-op before) |
| 2026-06-04 | Template + data em dashes cleared | Found rendered em dashes the content sweep missed: blog template bio (&mdash;), Template-C route partial (&mdash; in hero + table cells), Template-A route heading ("Critical Points" on ~1019 pages), breeds template, llms.txt, and countries_pet_regulations.json. All fixed. Verified via local Hugo build: 0 em dashes in rendered HTML. Remaining em dashes exist only in code comments (CSS/PHP/Hugo) and vendor bootstrap.min.css, none rendered as content |

## Mistakes to Avoid
- Never run hugo from repo root. Always `cd site` first (or the workflow handles it)
- Build plan filename has `=` sign: `cascading-build-plan-pet=transport.html`
- `rebuild_link_graph_v3.py` must run BEFORE hugo build
- Never fabricate quarantine periods or vaccine requirements
- The `live` branch is compiled output only (orphan, overwritten every push). Never edit it directly. It is produced by build-to-live.yml, which is the ACTIVE deploy workflow (NOT retired; verified 2026-06-04)
- Never delete `.ftp-deploy-sync-state.json` from Hostinger
- `.github/workflows/*.yml` cannot be edited via MCP connector (GitHub 403). Provide full file for Gareth to paste via GitHub web editor
- Never let a content commit go out without the BUILD-PLAN.md + build_state.json + MEMORY.md update and the live review links
- Never hand-edit count fields in build_state.json (routes_built, blog_articles, total_site_pages). They drift. Run `python verify_build_state.py --write` to reconcile from disk
- No em dashes anywhere, ever
