# BUILD-PLAN.md - PetTransportGlobal

> For full stage detail, always reference `cascading-build-plan-pet=transport.html` first.
> This file is a quick-reference checklist and session log. Update it at the end of every session AND on every build batch.

---

## THE BLOCK RHYTHM (read this before every session)

- **One "go" = one block.** Never more.
- **A block = 25 routes** (or one equivalent non-route unit: a country guide, an airline policy update, a blog post).
- Every block runs the full quality gate: **research, write, template rotation (A-E), humanise, QA scan, commit**.
- After commit to `main`: deploy is **automatic** (GitHub Actions triggers on push). No manual step needed.
- **After every build batch: post the live URLs of all new/changed pages in chat for review.** Deploy is automatic, so the review now happens AFTER publish. This is the safety gate. See `CLAUDE.md` LIVE LINK REVIEW GATE.
- **Every build batch also updates BUILD-PLAN.md, build_state.json and MEMORY.md in the same commit.** This is mandatory. See `CLAUDE.md` MANDATORY DOCS UPDATE.
- **Bulk-generation scripts are banned.**

**Where we are (reconciled from disk 2026-06-05):** 5,242 quality routes complete. ~32,588 routes remaining. Blog: 413 articles. Total .md source files: 6,028 (full deployed total verified from sitemap.xml after a build). Content plan: Day 6 is next. 227 score-7+ Tier A pairs remain after Chunk 25. Counts come from `python verify_build_state.py`, never hand-edited.

---

## Phase 7 - Template Diversification Rollout

**Status: Chunks 1-25 complete. Chunk 26 is next.**

- Chunk 21 template: D (Conversational Q&A) - DONE 2026-06-04
- Chunk 22 template: E (Data-Forward) - DONE 2026-06-04
- Chunk 23 template: A (Field Manual) - DONE 2026-06-04 (completed the P1 matrix)
- Chunk 24 template: B (Visual Journey) - DONE 2026-06-04 (Japan, South Korea, Switzerland, Netherlands corridors)
- Chunk 25 template: C (Comparison Brief) - DONE 2026-06-05 (China, India, Malaysia, Thailand, Philippines, Vietnam, Ireland, NZ corridors)
- Chunk 26 template: D (Conversational Q&A) - next in rotation
- Tier: A (227 score-7+ pairs remain)
- Template rotation: ...D(21), E(22), A(23), B(24), C(25), D(26)...

## Content Plan - Daily Blog Articles

**Published so far:**
- Day 1: `international-pet-transport-guide`
- Day 2: `cost-to-transport-a-pet-2026`
- Day 3: `pet-transport-uk-to-australia`

**Day 4 - DONE** - `uk-to-spain-pet-transport-complete-guide` (replaced in place 2026-06-04)

**Day 5 - DONE** - `pet-transport-uk-to-usa` (new article 2026-06-05)

**Next: Day 6** - `europe-to-uk-pet-transport` - Pet Transport Europe to UK: 2026 Guide (AHC, tapeworm, costs)

## Session Log

| Date | Stage | Work Done | Pages | Notes |
|------|-------|-----------|-------| ------|
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
| 2026-06-05 | Chunk 25 | 25 Tier A routes, Template C (Comparison Brief). China corridors (UK/USA pairs), India corridors (UK/USA pairs), Malaysia corridors (UK/USA pairs), Thailand corridors (UK/USA pairs), Philippines corridors (UK/USA pairs + UK-inbound), Vietnam-UK and UK-Vietnam, Ireland-USA, USA-Ireland, USA-New-Zealand. Philippines 180-day titre + 30-day quarantine. Vietnam NO quarantine NO titre (simplest SEA). NZ all-countries 180-day + 10-day MPI quarantine. Ireland CDC low-risk. New EU AHC format from April 2026 for USA-Ireland. QA passed, zero em dashes. Routes 5217 -> 5242, pages 6003 -> 6028. | 6,028 | Live links below. Chunk 26 (Template D, Tier A) next. Blog Day 6 also next. |
