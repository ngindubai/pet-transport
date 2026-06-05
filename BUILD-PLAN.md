# BUILD-PLAN.md - PetTransportGlobal

> For full stage detail, always reference `cascading-build-plan-pet=transport.html` first.
> This file is a quick-reference checklist and session log. Update it at the end of every session AND on every build batch.

---

## THE BLOCK RHYTHM (read this before every session)

- **One "go" = one batch of up to 4 blocks.** Floor is 1 block. (Changed 2026-06-05 from one block per run, to fit the 15-run routine cap; see session log.)
- **A block = 25 routes** (or one equivalent non-route unit: a country guide, an airline policy update, a blog post). A batch = up to 4 such blocks (for example 4 route chunks, or 3 chunks plus the due blog day).
- Every block in the batch runs the full quality gate independently: **research, write, template rotation (A-E), humanise, QA scan**. Quality first: if a run cannot finish 4 blocks cleanly, build as many as you can do well (minimum 1), commit those, and note the shortfall.
- The whole batch is committed ONCE per run: one commit, one push, one deploy. Advance the build pointer (next_chunk / next content-plan day) across the batch.
- After commit to `main`: deploy is **automatic** (GitHub Actions triggers on push). No manual step needed.
- **After every build batch: post the live URLs of all new/changed pages in chat for review.** Deploy is automatic, so the review now happens AFTER publish. This is the safety gate. See `CLAUDE.md` LIVE LINK REVIEW GATE.
- **Every build batch also updates BUILD-PLAN.md, build_state.json and MEMORY.md in the same commit.** This is mandatory. See `CLAUDE.md` MANDATORY DOCS UPDATE.
- **Bulk-generation scripts are banned.** A batch is still N individually quality-gated blocks, never a mass-generation script.
- **Skip rule:** skip only if the build pointer shows nothing left to build (no chunks remaining and no blog day due). Do NOT skip just because a build already happened earlier today; each site now runs twice a day on purpose.

**Where we are (reconciled from disk 2026-06-05):** 5,322 quality routes complete. ~32,508 routes remaining. Blog: 414 articles. Total .md source files: 6,109. Content plan: Day 7 is next. 140 score-7+ Tier A pairs remain. Chunk 31 (Template B, Visual Journey) is next. Counts come from `python verify_build_state.py`, never hand-edited.

---

## Phase 7 - Template Diversification Rollout

**Status: Chunks 1-28 complete. Chunk 29 is next (Template E, Tier A).**

- Chunk 21 template: D (Conversational Q&A) - DONE 2026-06-04
- Chunk 22 template: E (Data-Forward) - DONE 2026-06-04
- Chunk 23 template: A (Field Manual) - DONE 2026-06-04 (completed the P1 matrix)
- Chunk 24 template: B (Visual Journey) - DONE 2026-06-04 (Japan, South Korea, Switzerland, Netherlands corridors)
- Chunks 25-27 template: C (Comparison Brief) - DONE 2026-06-05 (three parallel routine runs reconciled into one main commit; 54 unique routes deduped)
- Chunk 28 template: D (Conversational Q&A) - DONE 2026-06-05 (Gulf/Asia corridors: SA/QA/TR/ID/TW/BR x4 + USA-MX)
- Chunk 29 template: E (Data-Forward) - DONE 2026-06-05 (Scandinavian/UK, LatAm, Africa, AsiaPac: 18 new + 7 upgraded)
- Chunk 30 template: A (Field Manual) - DONE 2026-06-05 (UK/US outbound to 13 priority destinations; 25 routes)
- Chunk 31 template: B (Visual Journey) - NEXT
- Tier: A (140 score-7+ pairs remain)
- Template rotation: ...D(21), E(22), A(23), B(24), C(25-27), D(28), E(29), A(30), B(31)...

**DEPLOY INCIDENT 2026-06-05 (fixed):** Three routine runs each committed a "chunk 25" to its own `claude/*` feature branch. `build-to-live.yml` only fires on push to `main`, so none deployed and Hostinger never updated. main never advanced, so each run rebuilt chunk 25 with overlapping routes. All three combined into main here. DURABLE FIX: the routine must push to `main` (STEP 3 already says `git push origin HEAD:main`; a conflicting feature-branch instruction was overriding it). See MEMORY.md.

## Content Plan - Daily Blog Articles

**Published so far:**
- Day 1: `international-pet-transport-guide`
- Day 2: `cost-to-transport-a-pet-2026`
- Day 3: `pet-transport-uk-to-australia`

**Day 4 - DONE** - `uk-to-spain-pet-transport-complete-guide` (replaced in place 2026-06-04)

**Day 5 - DONE** - `pet-transport-uk-to-usa` (new article 2026-06-05)

**Day 6 - DONE** - `pet-transport-europe-to-uk` - Pet Transport Europe to UK: Bringing a Pet Back After Brexit (2026-06-05, 2400 words, Marcus Webb)

**Next: Day 7** - check content plan for next slug

## Session Log

| Date | Stage | Work Done | Pages | Notes |
|------|-------|-----------|-------| ------|
| 2026-06-05 | Routine config | Switched to batch builds of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap. Docs only (CLAUDE.md BEHAVIOR RULES + this BLOCK RHYTHM). No pages added/removed, no deploy expected beyond the docs commit. | 6,065 | Instruction change only. |
| 2026-06-02 | Chunk 19 | 12 Tier A routes, Template B (Visual Journey). Germany-UK/US, HK corridors, NZ corridors. YAML fix pushed separately (stray top-level key in germany-to-uk). | 6,332 | Live links posted. |
| 2026-06-02 | Chunk 20 | 11 Tier A routes, Template C (Comparison Brief). NZ-Canada/SG/UAE, Singapore corridors (AU/CA/DE/NZ/UK/US/HK/FR). All with comparison tables and airline comparison tables. | 6,342 | Live links to be posted. |
| 2026-06-03 | Truth audit | No site pages. Added `verify_build_state.py` + SessionStart hook (anti-drift). Reconciled all four docs to true disk counts: routes 5,544 -> 5,172, total 6,342 -> 5,957. Logged legacy debt (248 Gareth-authored blogs, em dashes in 5 blog + 69 route files). Recorded Day 4 = replace-in-place. | 5,957 | Docs/script/hook only, no deploy, no live links. |
| 2026-06-04 | Legacy cleanup 1: em-dash sweep | No pages added/removed. Removed all em dashes from site/content: 74 blog+route files via Python sweeper + 11 pet-transport files + 4 static pages. Zero em dashes remain. Counts unchanged: 5,172 routes, 412 blog, 5,957 total. | 5,957 | Changed pages on all routes/blog/static with em dashes. Deploy will run; no new pages to review. |
| 2026-06-04 | Blog Day 4 | uk-to-spain-pet-transport-complete-guide.md replaced in place. Full rewrite 743 -> 2115 words. Title: "Pet Transport UK to Spain: 2026 Costs, Paperwork and Driving vs Flying". Author fixed to Marcus Webb. Covers AHC, Eurotunnel vs flying, cost table, timeline, Brexit mistakes, 6 FAQs. Content plan articles: 3 -> 4. Day 5 next (UK to USA). | 5,957 | Existing page updated live. |
| 2026-06-04 | Template + deploy-truth fixes | No .md pages added/removed. (1) Blog template single.html now renders persona authors (was hardcoded Gareth) in byline, bio, JSON-LD. (2) Cleared rendered em dashes the content sweep missed: blog template, Template-C partial, Template-A heading (~1019 pages), breeds template, llms.txt, countries data file. Verified 0 em dashes in built HTML via local Hugo 0.160.1 build. (3) Corrected deploy docs: build-to-live.yml is the active pipeline (publishes `live` branch, Hostinger serves it); deploy.yml FTP is disabled. | 5,957 | Template changes affect all blog + Template-A/C route pages. |
| 2026-06-05 | Blog Day 5 | pet-transport-uk-to-usa.md published. New article, 2,266 words, Marcus Webb. Post-CDC reset angle: CDC Dog Import Form, UK low-risk classification, APHIS endorsement process, airline options (BA/IAG, Delta, AA; United cargo suspended), cats with no federal requirements, Hawaii HDOA 5-day programme, cost table, 6 FAQs. Content plan Day 5 complete; Day 6 next (Europe to UK). | 5,958 | New page. Live link posted. |
| 2026-06-04 | Chunk 21 | 10 Tier A routes, Template D (Conversational Q&A). All top-priority P1 routes (scores 8-10): UK-AU, UAE-UK, UK-UAE, USA-AU, UAE-USA, AU-UK, UK-USA, UK-FR, UK-SG, USA-UK. Full regulatory data, QA passed, zero em dashes. | 5,968 | Live links posted. |
| 2026-06-04 | Chunk 22 | 11 Tier A routes, Template E (Data-Forward). Scores 6-7: UK-HK, USA-UAE, USA-SG, AU-USA, FR-UK, ZA-UK, ZA-USA, UK-CA, UK-DE, USA-DE, CA-UK. Grounded in route_keyword_matrix regulatory notes. QA passed, zero em dashes. | 5,979 | Live links posted. |
| 2026-06-04 | Chunk 23 | 12 Tier A routes, Template A (Field Manual). Completed the P1 matrix: USA-HK, UK-ZA, USA-CA, CA-USA, USA-FR, FR-USA, USA-ZA. Plus 5 new top Tier A pairs: UK-Japan, Japan-UK, UK-NZ, Ireland-UK, UK-Netherlands. Japan 180-day process, NZ MPI regime, Ireland CTA exemption. P1 matrix now fully built (90 routes). QA passed, zero em dashes. | 5,991 | Live links posted. |
| 2026-06-04 | Chunk 24 | 12 Tier A routes, Template B (Visual Journey). Japan corridors (USA-Japan, Japan-USA), South Korea corridors (USA-KR, UK-KR, KR-USA, KR-UK), Switzerland corridors (USA-CH, UK-CH, CH-USA, CH-UK), Netherlands corridors (NL-USA, NL-UK). Japan/Korea 180-day titre + quarantine, Switzerland no quarantine, NL EU passport still accepted for UK. QA passed, zero em dashes. | 6,003 | Live links below. |
| 2026-06-05 | Chunks 25-27 (reconciled) | DEPLOY INCIDENT FIX. Three parallel routine runs each built a "chunk 25" on its own feature branch; none reached main so none deployed. Combined all three into one main commit: 54 unique Template C Tier A routes (overlaps deduped). Corridors: Spain, Italy, Portugal, Thailand, Malaysia, Philippines, Vietnam, NZ, China, India, Ireland, UAE, HK, Germany, France, Australia (UK and US legs, plus AU/CA/SG/UAE destinations). Net +37 new slugs, 17 placeholder upgrades. All QA passed (zero em dashes, no banned vocab, Marcus Webb author). Pushed direct to main to trigger deploy. | 6,040 | Live links posted in Slack. Durable routine fix (push to main) flagged. |
| 2026-06-05 | Chunk 28 | 25 Tier A routes, Template D (Conversational Q&A). Gulf and Asia corridors: Saudi Arabia x4 (SA-UK, SA-US, UK-SA, US-SA), Qatar x4 (QA-UK, QA-US, UK-QA, US-QA), Turkey x4 (TR-UK, TR-US, UK-TR, US-TR), Indonesia x4 (ID-UK, ID-US, UK-ID, US-ID), Taiwan x4 (TW-UK, TW-US, UK-TW, US-TW), Brazil x4 (BR-UK, BR-US, UK-BR, US-BR), plus USA-Mexico. Key data: Saudi/Qatar dog restrictions, Turkey Staffordshire ban, Indonesia BARANTAN/quarantine, Taiwan BAPHIQ 7-day quarantine, Brazil no titre test. Zero em dashes, all Marcus Webb. Routes 5,254 -> 5,279. | 6,065 | Live links below. |
| 2026-06-05 | Chunk 29 | 25 Tier A routes, Template E (Data-Forward). 18 new routes + 7 thin placeholder upgrades. New: Scandinavian-UK corridors (SE, NO, DK, BE, AT, GR x UK both directions), Mexico-to-US/UK, Argentina-to-US/UK, Kenya-to-UK, Nigeria-to-UK, Egypt-to-UK, USA-to-Netherlands. Upgraded: DE-CA, FR-CA, ZA-AU, ZA-CA, AU-SG, CA-AU, CA-SG. Key regulatory detail: AHC + tapeworm for all UK corridors, CDC high-risk for Mexico-US, SENASICA/SENASA paperwork, Egyptian embassy attestation requirement, USDA APHIS endorsement for USA-NL, AVS Category B/C for Singapore routes, DAFF Group 4 for AU. Zero em dashes, all Marcus Webb. Routes 5,279 -> 5,297. | 6,083 | Live links below. Chunk 30 (Template A, Tier A) is next. |
| 2026-06-05 | Chunk 30 + Blog Day 6 | 25 Tier A routes (Template A, Field Manual) + Blog Day 6. Routes: UK and US outbound to 13 priority destinations: Israel (UK no titre/US requires FAVN titre), Pakistan, Bangladesh, Colombia (no import permit for personal pets), Chile (apostille on health cert), Peru, Morocco, Ghana, Ethiopia, Jordan, Nepal, Sri Lanka (30-day home quarantine at owner premises, not facility; 90-day titre wait), Nigeria. 4 data corrections applied vs. source data file. Blog: pet-transport-europe-to-uk.md, 2400 words, Marcus Webb. AHC for EU-to-GB, EU passports not accepted, tapeworm 24-120h window, Eurotunnel/ferry/cargo options, rescue dog IPAFFS rules, cost tables. Zero em dashes, all QA passed. Routes 5,297 -> 5,322, blog 413 -> 414, pages 6,083 -> 6,109. | 6,109 | Live links below. Chunk 31 (Template B, Tier A) is next. Blog Day 7 next. |
