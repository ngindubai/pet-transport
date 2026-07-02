# SEO Build Plan - 2 July 2026

Execution companion to `seo-audit-2026-07-02.html`. Derived from the SEO and Search Brief dated 29 June 2026, verified against the repo on 2 July 2026.

## How to use this file

- Work top to bottom. Tasks are ordered so cheap, safe wins land first and dependencies are respected.
- Every task is tagged **[SONNET]** or **[OPUS]**. Only A1 needs Opus, and only for its design step. Everything else is Sonnet.
- Follow the existing rules in `CLAUDE.md`: no em dashes anywhere, British English, correct author personas, no bulk generation scripts, full quality gate per content block, and the docs update plus live link review gate on every commit that changes site content.
- Tasks A3, A7, A8, A6, A4, A5 are template or config edits, not content blocks, so they do not consume build-plan route budget. A1, A2, A9, A10 touch content and must respect the batch and quality gate rules.

## Open question for Gareth before starting

- **A6 canonical host:** is the live site canonical on `https://www.pettransportglobal.com/` or `https://pettransportglobal.com/`? Whichever serves without a redirect and matches Search Console is the answer. Do not touch `baseURL` until this is confirmed.
- **A3 social links:** are there real Facebook, Instagram and LinkedIn URLs for the brand? If yes, provide them. If no, the `sameAs` array gets removed.

---

## Phase 1 - Same day quick wins (safe, strict improvements)

### A3 [SONNET] Remove TODO placeholders from Organization schema
- **File:** `site/layouts/_default/baseof.html`
- **Find:** the `"sameAs"` array containing `"TODO: Facebook URL"`, `"TODO: Instagram URL"`, `"TODO: LinkedIn URL"`.
- **Do:** replace with the real profile URLs if provided, otherwise delete the entire `"sameAs"` block (an absent field is valid JSON-LD; placeholder strings are not).
- **Verify:** view source on the home page and any route page, confirm no `TODO` string remains in the JSON-LD.
- **Effort:** tiny. One file.

### A7 [SONNET] Fix or remove the SearchAction in WebSite schema
- **File:** `site/layouts/_default/baseof.html`
- **Find:** the `"potentialAction"` / `"SearchAction"` block with `urlTemplate` `https://pettransportglobal.com/pet-transport/routes/{search_term_string}/`.
- **Do:** unless a real search results page resolves that path, remove the `potentialAction` block. (The `/pet-transport/routes/` breadcrumb target itself is fine, it resolves as the section index, leave it.)
- **Verify:** JSON-LD still valid, no SearchAction pointing at a non existent endpoint.
- **Effort:** tiny.

### A8 [SONNET] Correct llms.txt author line and domain
- **File:** `site/static/llms.txt`
- **Do:** replace "authored by Gareth, Founder" with a persona framing, for example "authored by our team of pet relocation and animal health specialists". Align the domain (www or not) with the A6 decision once made; if A6 is not settled yet, leave the domain and come back after A6.
- **Do not** expand the file further. Google does not read it for AI ranking (brief Story 2); keep it only for other engines.
- **Verify:** no "Gareth" reference remains in the file.
- **Effort:** tiny.

**Phase 1 commit:** these are template and static edits, not content blocks. Commit together, push to `main`, post the affected representative URLs (home page plus one route page) per the live link review gate, since schema on every page changed.

---

## Phase 2 - Confirm then fix

### A6 [SONNET, after Gareth confirms host] Set the canonical host
- **File:** `site/hugo.toml` (`baseURL`).
- **Do:** set `baseURL` to the confirmed canonical host exactly. Confirm at Hostinger that the other host 301 redirects to it.
- **Then:** re-run A8's domain alignment in `llms.txt` and check the robots.txt `Sitemap:` line resolves to the same host.
- **Verify:** after deploy, `curl -I` both hosts, confirm one 200s and the other 301s to it; confirm canonical tags on a sample of pages point at the live host.
- **Trade-off / caution:** this rewrites canonicals sitewide in one deploy. Do not run it on a guess. Blocked on the open question above.
- **Effort:** tiny edit, but gated on confirmation.

---

## Phase 3 - Author authority

### A2 [SONNET] Reassign authors to the correct personas
- **Scope:** 4,963 route pages and 245 blog posts currently authored "Gareth", plus normalising the two Marcus Webb spellings and three Editorial Team spellings.
- **Mapping (from `CLAUDE.md`):**
  - Route and logistics, cost, timeline content -> `Marcus Webb, Senior Pet Relocation Consultant, PetTransportGlobal`
  - Country import/export and health rules -> `Dr. Sarah Okafor, International Animal Health Consultant, PetTransportGlobal`
  - Breed welfare, anxiety, sedation, senior pets -> `Emma Hartley, Certified Animal Behaviourist and Pet Travel Adviser, PetTransportGlobal`
  - Checklists, timelines, documentation, choosing a company, insurance, multi-pet, emergency moves -> `James Osei, Pet Transport Planning Specialist, PetTransportGlobal`
  - Default for route pages (the bulk): Marcus Webb.
- **Do:** update the `author:` front matter field. Use the exact comma spelling above, drop the hyphen variants. Route pages default to Marcus Webb unless the page is clearly a health, welfare or planning topic.
- **Rule compliance:** this edits many files, so under the no bulk generation rule it flows through the normal batch and commit process alongside A1 where possible (same files). Do not write a mass rewrite script.
- **Verify:** `grep -rc 'author: "Gareth' site/content/` returns 0 when complete; author spellings collapse to one per persona.
- **Effort:** small per file, large in aggregate. Piggyback on A1 sessions.

### A5 [SONNET, after A2] Visible byline and author Person schema
- **Files:** route partials in `site/layouts/partials/routes/` and the shared schema block in `site/layouts/routes/single.html`; mirror for blog in `site/layouts/blog/single.html`.
- **Do:**
  1. Render a small byline near the existing `verified-date.html` stamp: "Reviewed by [author name], [title]".
  2. Add an `author` Person node to the page schema using the front matter `author` value split into name and title. Standard structured data only, no AI specific schema.
- **Dependency:** must come after A2 so the surfaced names are correct and consistent.
- **Verify:** byline renders on a sample route and blog page; JSON-LD includes a valid `author` Person; names match front matter.
- **Effort:** small.

---

## Phase 4 - AI Overview capture

### A4 [SONNET] Direct answer capsule on route pages
- **Files:** the route variant partials in `site/layouts/partials/routes/` (`route-new-na.html` through `route-new-nl.html`, and the `route-a`..`route-e` set). Add the capsule once and reuse, or add per partial consistently.
- **Do:** directly under the H1, render a two to three sentence "quick answer" built from existing data fields:
  - `route_data.estimated_timeline_weeks` (present on 6,082 routes) -> preparation time
  - `quarantine_required` / `quarantine_days` -> quarantine yes/no and days
  - titre test flag from `route_data.destination.import_requirements.titre_test` -> titre needed yes/no
  - `route_data.cost_factors` (present on all 6,094) -> cost range
- **Must:** pull from the per route data so the capsule differs page to page. Do not hard code sentences, that would work against A1.
- **Do not:** add AI specific schema or content chunking (brief Story 2 lists these as things Google does not use).
- **Verify:** capsule renders in the first screenful on a sample of each variant, reads naturally, and shows different numbers on different routes.
- **Effort:** small, template only.

---

## Phase 5 - The big one: de-duplicate route prose (multi session)

### A1 step 1 [OPUS] Design the variation strategy and exemplar pools
- **Why Opus:** producing genuinely varied, on brand, non repetitive prose across thousands of near identical pages is a judgement task. Sonnet reliably re-templatises it. Opus does the design and the first exemplar pools; Sonnet then applies.
- **Do:**
  1. Confirm the problem on more samples (compare `content.overview` and `content.sections` across several same destination and same complexity routes) to map exactly which sentences are shared.
  2. Design a variant selection model keyed off real per route data: complexity band, quarantine yes/no, titre test yes/no, timeline weeks, listed vs non listed country, plus at least one lane specific fact (the specific airlines on that route, the specific export authority such as SENASA for Argentina).
  3. Hand write the expanded sentence pools for **Template C first** (1,251 pages, the largest variant), enough variety that two pages only read alike when their actual regulations are alike.
  4. Run the pools through the quality gate: no em dashes, no banned vocabulary, British English, correct persona voice.
- **Output:** the variant pools plus the selection logic, documented so Sonnet can apply deterministically.

### A1 step 2 [SONNET] Roll out, prioritised by traffic
- **Do:** apply the pools and selection logic route by route, highest value routes first (the high volume routes listed in `llms.txt`, plus anything with Search Console impressions), through the normal build batches (two blocks per run, full quality gate each, minimum one).
- **Rule compliance:** absolutely no bulk generation script. Each block runs the full quality gate. This is a multi session programme, not a single run. Report the shortfall honestly each session.
- **Verify each batch:** spot check that same destination pages no longer share whole paragraphs; run the auditor checks; confirm the docs update and live link review gate on each commit.
- **Effort:** large, spread across many sessions.

---

## Phase 6 - Ongoing

### A9 [SONNET] Quarterly data freshness refresh
- **Do:** define a quarterly routine that rechecks the source data files under `data/` against the named authorities (DEFRA, USDA APHIS, DAFF, EU TRACES), flags changed rules, updates affected `route_data` and the verified date, through the normal quality gate.
- **Caution:** YMYL topic. A human must sign off any regulatory change before publish. Build it as assisted review, not unattended automation. Keep it inside the no bulk generation rule (review and update, do not regenerate en masse).
- **Effort:** medium to build, then recurring.

### A10 [SONNET] Targeted title and meta tuning
- **Do:** pull the top routes by Search Console impressions (use the performance report, not the indexing report, which is lagging per brief Story 6). Hand tune titles and descriptions for the top ~50 to 100 only, leading with the standout fact (quarantine days, cost range, or "no quarantine"). Leave the long tail on the template.
- **Effort:** medium, targeted.

---

## Do not do

- No AI specific schema, no content chunking (Google says it does not use them, brief Story 2). Existing HowTo, FAQPage, BreadcrumbList markup is correct, keep it.
- No paid brand mentions or GEO placements (black hat, ineffective, brief Story 3).
- No mass regeneration scripts for A1 or A2 (violates `CLAUDE.md`, and would re-create the duplication problem).
- Do not trust the Search Console indexing report until Google fixes it (stale since 11 June, brief Story 6). Use URL Inspection for single pages, performance report for traffic.

## Monitoring

- Check position tracking Monday mornings for pet transport route queries (spam update watch, brief Story 1). Mainstream volatility trackers sample US head terms and will not show your niche drops.
- Search fragmentation to YouTube, Reddit and AI chatbots (brief Story 4) is an off site distribution question, out of scope for this repo plan, worth a separate conversation.

## Model summary

| Task | Model | Note |
|---|---|---|
| A1 step 1 (variation design + exemplar pools) | **OPUS** | Judgement heavy, avoids re-templatising |
| A1 step 2 (rollout) | SONNET | Deterministic once pools and logic exist |
| A2, A3, A4, A5, A6, A7, A8, A9, A10 | SONNET | Template, config, data and rule based edits |

No em dashes were used in this document.
