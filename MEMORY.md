# MEMORY.md - PetTransportGlobal

## Site Overview
- **Domain:** pettransportglobal.com (Hostinger hosting)
- **Type:** Programmatic SEO + content-driven lead generation. International pet transport
- **Stack:** Hugo static site generator + Python generation scripts + GitHub Actions CI/CD
- **Repository:** https://github.com/ngindubai/pet-transport (private)
- **Deploy:** Push to `main` triggers GitHub Actions automatically. Hugo build + incremental FTP to Hostinger. Live within ~80 seconds for a single article. After every build batch, the live URLs of new/changed pages are posted in chat for review (LIVE LINK REVIEW GATE in CLAUDE.md).

## Current State (2026-07-09, reconciled)
- **2026-07-09 Chunk 74 + Blog Day 27:** 25 new Tier B routes (Template D, 1 block). Gap analysis confirmed the hub-market set (UK/US/CA/AU/DE/FR/IT/NL/ES/PT/BE/AT/CH/CZ/PL/HU/DK/SE/NO/FI/GR/IE/UAE) crossed with the chunks 61-73 low-tier cluster (Uruguay/Jamaica/Dominican Republic/Panama/Rwanda/Lebanon/Uganda/Georgia/Armenia/Kazakhstan/Azerbaijan/Estonia/Lithuania/Latvia/Slovenia) is now fully saturated (0 missing pairs). Opened a new cluster: Turkey x the same 15 countries. 15 X-to-Turkey routes plus 10 Turkey-to-X routes (Lebanon/Georgia/Armenia/Azerbaijan/Kazakhstan/Estonia/Latvia/Lithuania/Slovenia/Rwanda); Turkey-to-Uruguay/Jamaica/Dominican-Republic/Panama/Uganda (5) remain for a future chunk. **Safety-critical correction:** the site's data file (`data/countries_pet_regulations.json`) and several older Turkey route files (e.g. `germany-to-turkey.md`, whose structured `titre_test` field contradicts its own FAQ prose) state or imply Turkey doesn't require a rabies titre test. Verified via USDA APHIS's official Turkey guidance and independent sources that Turkey DOES require a FAVN/RNATT titre test from unlisted origins: blood drawn 30+ days post-vaccination, 90-day wait from the draw date, 0.5 IU/ml minimum, 21-day quarantine penalty for non-compliance. All 25 new pages use the corrected rule; older Turkey pages are not yet fixed (flagged below). Also corrected Turkey's banned-breed list against Law No. 5199 (amended 2021): the data file names only Pit Bull Terrier and Japanese Tosa; the real list is broader (adds American Staffordshire Terrier, Staffordshire Bull Terrier, Fila Brasileiro, Dogo Argentino, Rottweiler). Verified Georgia/Armenia/Azerbaijan/Kazakhstan require no titre test from any origin, not just from the EU as older site precedent implied. Panama and Rwanda get genuine non-stop Turkish Airlines cargo routes to Istanbul; Armenia's pages (both directions) cover the airline's first-ever scheduled Istanbul-Yerevan flights, launched 11 March 2026, despite the Turkey-Armenia land border staying closed since 1993; Georgia's pages note the Sarpi land crossing as a real overland option. Blog Day 27: `uk-to-ireland-pet-transport-guide.md` replaced in place (Marcus Webb), full rewrite from a thin 2026-05-06 stub, correcting the outdated "PETS scheme" framing (ended for GB pets January 2021, replaced by the AHC) and a ferry-routing error (Liverpool serves Belfast, not Dublin; Holyhead-Dublin is the direct route). Routes 6,271 -> 6,296, pages 7,075 -> 7,100.
- **2026-07-09 Chunk 73:** 25 new Tier B routes (Template C, 1 block), the first chunk since 61-72 to move off the exhausted Baltic/Caucasus/Lebanon/Rwanda/Caribbean cluster. New cluster: EU/other high-value origins into Mexico/Brazil/Malaysia/Indonesia/South Korea, plus Slovenia's reciprocal gap with the same five countries. Mexico destination (6): Netherlands/Switzerland/India/Italy/Portugal/Slovenia, no titre test (EU-listed low-risk under Annex II to Implementing Regulation (EU) 2026/636), no advance import permit (SENASICA clears at the port of entry). Brazil destination (3): Switzerland/India/Slovenia; corrected a conflict found across existing Brazil route files (some claimed a mandatory 30-day quarantine, others none) by checking MAPA's own guidance directly: no quarantine, no import permit, 30-day wait after a first rabies vaccination, no titre test. Malaysia destination (4): Switzerland/Italy/Portugal/Slovenia, DVS process, FAVN titre test, 90-day wait, 14-day quarantine. Indonesia destination (4): Switzerland/India/Portugal/Slovenia, Barantin rekomendasi permit, FAVN titre 0.5 IU/ml, 7-14 day quarantine. South Korea destination (3): Portugal/Greece/Slovenia, QIAS process, no titre test for EU origins but a 1-3 day inspection hold at Incheon. Slovenia destination (5, reverse direction): Mexico/Brazil/Malaysia/Indonesia/South Korea. Safety-critical QA catch: the build agent initially wrote both mexico-to-slovenia.md and malaysia-to-slovenia.md as EU-unlisted (titre test + 90-day wait required), based on apparent site precedent rather than a checked primary source. Independently verified against two sources (the EU's own territory-listing page and Germany's BMLEH published country list) that Mexico and Malaysia are in fact EU-listed low-risk countries; rewrote both files in full to remove the titre test requirement and shorten the estimated timeline from 18-22 weeks to 5-8 weeks. Brazil, Indonesia and South Korea remain correctly unlisted. All 25 files QA-scanned clean (zero em dashes, banned vocabulary, curly quotes, dead route paths, email/phone mentions; sibling-file sentence overlap under 7%, well inside the 15% shared-copy threshold). Two new legacy data-quality conflicts flagged below for a future correction pass. Routes 6,246 -> 6,271, pages 7,050 -> 7,075.
- **2026-07-08 Chunk 72:** 27 new Tier B routes (Template B, 1 block), closing every remaining reciprocal gap in the Baltic/Slovenia/Caucasus/Lebanon/Rwanda/Caribbean hub-country cluster built up across chunks 61-71. Caucasus/Lebanon/Rwanda to Greece (6, all EU-unlisted titre test plus 90-day wait; Lebanon-Greece uses a rare direct Aegean/MEA Beirut-Athens routing). Rwanda to Ireland (1, titre test plus TRACES plus the dog tapeworm rule, since Rwanda is not on Ireland's Finland/Malta/Norway/Northern Ireland exemption list). Intra-EU inbound gap-fills to Estonia/Latvia/Lithuania/Slovenia from Portugal/Greece/Ireland/Czech Republic/Poland/Hungary as applicable, plus Lithuania outbound to Poland and Hungary (18, all straightforward EU pet passport moves with no titre test; Czech Republic-Slovenia and Hungary-Slovenia both flag driving as a realistic alternative given the short distance, and Hungary-Slovenia notes Wizz Air carries no cargo pets from Budapest). Caribbean cluster (4): Dominican Republic to Sweden (titre test applies, but unlike Norway and Finland, Sweden has no mandatory tapeworm treatment since the parasite is already present in its own fox population); Greece to Dominican Republic and Greece/Ireland to Jamaica (no titre test into the DR; Jamaica's Preliminary Application Form, FAVN titre test and up to 14-day Plumb Point quarantine apply regardless of origin). This closes the last dense reciprocal-gap pocket from the chunks 61-71 build sequence; chunk 73 moves to a new Tier B cluster. Routes 6,219 -> 6,246, pages 7,023 -> 7,050.
- **2026-07-07 Chunk 71:** 25 new Tier B routes (Template A, 1 block), closing reciprocal gaps for Uruguay, Panama and the Dominican Republic left over from chunks 65/66/70. Uruguay to Denmark/Finland/Ireland/Norway/Portugal/Sweden/Greece/UAE (8, EU/MOCCAE unlisted-origin titre test; Finland/Ireland/Norway also carry the dog tapeworm rule); Ireland/Portugal/Greece/UAE to Uruguay (4, no titre test, MGAP import permit plus 72-hour-to-30-day echinococcus treatment for dogs); Belgium to Uruguay (1). Panama to Ireland/Portugal/Greece/UAE (4); Ireland/Portugal/Greece/UAE to Panama (4, no titre test, but the certificate needs legalisation by a Panamanian embassy or consulate in every case, including via Panama's Abu Dhabi embassy and Dubai consulate for the UAE-origin route). Dominican Republic to Denmark/Finland/Norway (3); Ireland to Dominican Republic (1, no titre test, no import permit for up to 5 pets). Web-verified that Ireland's tapeworm rule is broader than the data file suggested: it applies to dogs from every country except Finland, Malta, Norway and Northern Ireland, not just Great Britain (the data file's "required for dogs entering from UK" wording undersells this; flagged below for a future data file update rather than fixed in the file itself). Confirmed the Dominican Republic's correct export authority is DIGEGA (Dirección General de Ganadería), resolving a naming inconsistency against a small number of older route files that use other names for the same authority. Confirmed Panama has an embassy in Abu Dhabi and a consulate in Dubai; Uruguay, unlike Panama, does not require embassy legalisation of its import certificate. Built as 1 block rather than 2 to keep every page individually researched and quality-gated; the shortfall against the 50-page target is intentional, per the routine's own quality-first rule. Routes 6,194 -> 6,219, pages 6,998 -> 7,023.
- **2026-07-07 Chunk 70:** 25 new Tier B routes (Template E), two reciprocal-gap clusters. Cluster 1: United Arab Emirates outbound to Lebanon/Rwanda/Uganda/Armenia/Georgia/Azerbaijan/Kazakhstan (the reverse of chunk 69's corridor, no titre test on any of these); UAE to Dominican Republic and Jamaica; UAE to Estonia/Latvia/Lithuania/Slovenia (web-verified the UAE is EU Annex II, not low-risk Annex I, so the titre test and 90-day wait apply despite MOCCAE's lighter export side). Cluster 2: United States/Canada/Australia to Dominican Republic/Jamaica/Panama/Uruguay, the first non-EU-origin routes into these four destinations. Key web-verified facts: Panama needs a Panamanian consulate/embassy legalisation stamp on the health certificate plus parasite treatment within 14 days, no titre test from any origin; Uruguay needs a dog-only praziquantel echinococcus treatment (72 hours to 30 days pre-arrival) and a mandatory MGAP import permit despite no titre test; Jamaica needs a FAVN titre test and VSD's Preliminary Application Form approved before any vaccination begins, an 18-24 week process; Dominican Republic needs no import permit for up to 5 pets and no titre test from non-high-risk origins. Australia's three routes are honestly reflected as multi-leg (Qantas transpacific plus a US or Chilean connection) in route_complexity and timeline fields. Routes 6,169 -> 6,194, pages 6,973 -> 6,998.
- **2026-07-06 Chunk 69 + Blog Day 26:** 25 new Tier B routes (Template D): Lebanon/Rwanda/Uganda/Armenia/Georgia/Azerbaijan/Kazakhstan to United Arab Emirates (7, unlisted-risk MOCCAE entry, titre test required with no fixed post-draw wait, contrasting with the EU's 90-day rule); Estonia/Latvia/Lithuania/Slovenia to United Arab Emirates (4, EU-member low-risk MOCCAE entry, same category as the UK, no titre test); Dominican Republic and Jamaica to United Arab Emirates (2, unlisted-risk MOCCAE entry); Estonia/Latvia/Lithuania/Slovenia to Greece (4, intra-EU pet passport) and Dominican Republic/Jamaica to Greece (2, contrasts the EU-unlisted titre test against Jamaica's EU Group 2 exemption); Dominican Republic and Jamaica to Ireland (2, TRACES pre-notification applies regardless of the Jamaica titre exemption); Slovenia to Portugal/Czech Republic/Poland/Hungary (4, intra-EU, Czech Republic and Hungary flag driving as a realistic alternative, Portugal is fly-only). Web search confirmed the UAE's MOCCAE import rules differ genuinely from the EU pattern: no fixed wait after the titre test blood draw, only a 365-day result validity, plus a 90-day online import permit. Blog Day 26 replaced in place: uk-to-germany-pet-transport-guide.md (Marcus Webb), drive-and-ferry vs cargo-flight cost comparison. Routes 6,144 -> 6,169, blog unchanged at 430 (replace in place), pages 6,948 -> 6,973.
- **2026-07-06 Chunk 68:** 25 new Tier B routes (Template C): Uganda to Italy/Belgium/Austria/Switzerland/Czech Republic/Poland/Hungary/Denmark/Sweden/Norway/Finland/Ireland/Portugal/Greece (completes Uganda's outbound EU coverage); Greece to Lebanon/Rwanda/Uganda/Armenia/Georgia/Azerbaijan/Kazakhstan (fills reciprocal gaps); Estonia and Latvia to Poland/Hungary (closes the last Baltic-to-Central-Europe gaps). New pages cite the current post-22-April-2026 EU framework (Commission Delegated Regulation (EU) 2026/131, Implementing Regulations (EU) 2026/705 and 2026/636), which supersedes the 576/2013 and 577/2013 citations still used on older route pages, a distinct gap now flagged for a future correction pass (see below). Confirmed via web search that Wizz Air has a strict no-pet policy across all routes; excluded from every airline pick. Routes 6,119 -> 6,144, pages 6,923 -> 6,948.
- **2026-07-05 Chunk 67 + Blog Day 25:** 25 new Tier B routes (Template B): Lebanon to Austria/Belgium/Czech Republic/Denmark/Finland/Hungary/Ireland/Italy/Norway/Poland/Portugal/Sweden/Switzerland, and Rwanda to the same 12 destinations minus Ireland. Both origins are EU-unlisted third countries, full FAVN titre test + 90-day wait (Switzerland: 3-month wait + FSVO advance permission). Blog Day 25: uk-pet-passports-2026-guide (Dr. Sarah Okafor), what replaced the UK pet passport post-Brexit and how the AHC works. Routes 6,094 -> 6,119, blog 429 -> 430, pages 6,897 -> 6,923.
- **2026-07-04 design + conversion audit executed and merged to live (D1-D20):** fixed 42k broken internal link instances, H1 title leak, fake footer-email claim, home-form country limit (now 75 via `quote_form_countries.json`), worst route CTA placements, WhatsApp float overlap, added quote/WhatsApp CTA cards + mid-page CTAs on guide pages, extracted the sticky stat sub-bar into a shared partial, added hero background images to airline/breed/methodology pages, styled blog tables, gave the methodology page a proper layout, standardised breadcrumb + form-label styling across route variants, added popular-search links to /search/, softened the thank-you promise to "within one business day", swapped the sitewide footer CTA image off the dark departure board onto the warm hero photo, and wired up the previously-unused `.wa-btn` WhatsApp sidebar button on 5 route templates. Then handled two external SEO re-audits: **non-www is canonical** (CLAUDE.md had this backwards and is now corrected; www 301-redirects to non-www), GSC is verified via DNS (the blank `googleSearchConsole` field in hugo.toml is moot), robots.txt generates correctly from `layouts/robots.txt` (no static file needed), and hreflang is not needed (English-only). Design plan: design-build-plan-2026-07-02.md, all items closed. Counts unchanged (design/template work, verifier confirms no drift).
- **2026-07-02 SEO audit executed and merged to live:** on-site search at /search/ (+ header box), llms.txt rebuilt (personas, no Gareth), all authors reassigned to personas sitewide (zero Gareth), author byline + Person schema, answer-first capsule on routes, A1 route-prose de-duplication via data-keyed template composition (route-overview.html + route-sections.html; stored .md overview/sections now unused on complexity-bearing routes, kept as fallback). Fixed sitewide JSON-LD double-escaping (safeJS), a YAML error in dominican-republic-to-austria that was breaking the whole Hugo build, and hero quarantine misinformation on Australia routes. Quarterly refresh routine: refresh_audit.py + REFRESH-ROUTINE.md. Manual follow-ups in BROWSER-PROMPTS.md. Verified with a full Hugo build.


- **Routes built:** 6,296 of ~37,830 country pairs (~16.6%). All in `site/content/routes/`.
- **Blog articles:** 430
- **Total .md source files:** 7,100 (reconciled by verify_build_state.py, 2026-07-09)
- **Phase 7 progress:** Chunks 1-74 complete. **Chunk 75 is next** (Template E, Tier B). Tier A is fully complete (0 pairs remaining). Tier B: 592 remaining.
- **Turkey titre test conflict (flagged 2026-07-09):** `data/countries_pet_regulations.json`'s Turkey entry, and several older Turkey route files (e.g. `germany-to-turkey.md`, whose structured `route_data.destination.import_requirements.titre_test` field says "not routinely required" while its own FAQ prose correctly says a titre test and 90-day wait apply), understate or contradict Turkey's real requirement. Verified via USDA APHIS's official Turkey pet import guidance: Turkey requires a FAVN/RNATT titre test from unlisted origins, 30-day post-vaccination draw, 90-day wait, 0.5 IU/ml minimum. Chunk 74's 25 new Turkey-cluster pages use the corrected rule. Older Turkey route files (X-to-turkey.md for the ~75 countries built before chunk 74) have not been corrected; needs a dedicated pass. Also: the data file's Turkey banned-breed list (Pit Bull Terrier, Japanese Tosa only) is narrower than Law No. 5199 as amended in 2021, which also covers American Staffordshire Terrier, Staffordshire Bull Terrier, Fila Brasileiro, Dogo Argentino and Rottweiler.
- **Brazil quarantine conflict (flagged 2026-07-09):** existing Brazil-destination route files disagree with each other: `italy-to-brazil.md`/`portugal-to-brazil.md` say no quarantine and a 21-day post-vaccination wait, while `austria-to-brazil.md`/`germany-to-brazil.md`/`spain-to-brazil.md`/`mexico-to-brazil.md` say a mandatory 30-day quarantine and import permit. Chunk 73's new Brazil pages (switzerland/india/slovenia-to-brazil) use the version checked directly against MAPA's own guidance: no quarantine, no import permit, a 30-day wait after a first rabies vaccination, no titre test. The older conflicting files have not been corrected; needs a dedicated pass.
- **Mexico import permit conflict (flagged 2026-07-09):** some older Mexico-destination route files state a SAGARPA import permit is required; this is outdated. SENASICA now clears personal pets at the port of entry with no advance permit (confirmed via chunk 73's live web search, cross-checked against the most recent Mexico-destination files from June 2026). Older files with the SAGARPA-permit framing have not been corrected; needs a dedicated pass.
- **Dominican Republic export authority naming inconsistency (flagged 2026-07-07):** a handful of older route files (e.g. `dominican-republic-to-canada.md`) name the export authority "DSA (Departamento de Sanidad Animal)" while newer files (chunk 69 onward, confirmed correct via web search) use "DIGEGA (Dirección General de Ganadería)". DIGEGA is the verified correct name. Lower-priority future correction pass, same category as the Jamaica and EU-citation items below.
- **Ireland tapeworm data file gap (flagged 2026-07-07):** `data/countries_pet_regulations.json`'s Ireland entry describes the Echinococcus multilocularis tapeworm treatment as required only for dogs from Great Britain. Web search confirms the actual DAFM rule is broader: required for dogs entering Ireland from any country except Finland, Malta, Norway and Northern Ireland. Chunk 71's new Ireland-bound routes (Uruguay, Panama) use the correct broader rule; the data file itself has not been updated. Worth fixing at the source so future chunks pull the right answer automatically.
- **Regulation citation currency (flagged 2026-07-06):** EU pet import rules changed on 22 April 2026 (Commission Delegated Regulation (EU) 2026/131, Implementing Regulation (EU) 2026/705, Implementing Regulation (EU) 2026/636, superseding Regulation 576/2013 and Implementing Regulation 577/2013; substantive requirements unchanged). Chunk 68's new pages cite the current regulation numbers. Older route pages (chunk 67 and earlier) still cite 576/2013 / 2020/692, which is now outdated wording though the underlying rule is the same. A future correction pass should update the citation text on older EU-destination routes for currency, lower priority than the Jamaica factual error below since the rule itself has not changed.
- **Content plan:** Days 1-6 + Days 8-27 complete (27 articles written). Day 7 skipped (pre-existing). **Day 28 is next** (check content-plan/plan-rows-q1.js).
- **Jamaica regulatory correction flagged:** Existing routes (jamaica-to-germany, jamaica-to-france, etc.) incorrectly state Jamaica is EU unlisted and requires FAVN titre test. Jamaica IS EU Group 2 listed (Implementing Regulation (EU) 2024/1130) - no titre test required. New Chunk 65 Jamaica routes use correct information. A future correction pass on the ~10 existing Jamaica routes is needed.
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
