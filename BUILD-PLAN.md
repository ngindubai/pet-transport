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
- **Every build batch also updates BUILD-PLAN.md, build_state.json and MEMORY.md in the same commit.** This is mandatory and is what keeps the docs from drifting. See `CLAUDE.md` MANDATORY DOCS UPDATE.
- **Bulk-generation scripts are banned.** Anything that writes more than 25 pages in one run violates the plan.
- See `CLAUDE.md` for the full rules.

**Where we are:** 5,534 quality routes complete. ~32,298 routes remaining. Blog: 412 articles. Total pages ~6,332. Content plan: Day 4 is next.

---

## Phase 0 - Research

- [x] 0.1: Worker souls adapted for pet transport domain
- [x] 0.2: PetRelocation.com competitor scrape and analysis
- [x] 0.3: Government import portal scrape (USDA APHIS, UK APHA, Australian DAFF, EU TRACES, Singapore AVS)
- [x] 0.4: Airline pet cargo policy scrape (20+ airlines)
- [x] 0.5: Route keyword research matrix
- [x] 0.6: Country regulations database built
- [x] 0.7: Airline database built
- [x] 0.8: Breed restriction database built
- [x] 0.9: Route database schema designed

## Phase 1 - Foundation

- [x] Block 10-21: All Phase 1 complete. 202 pages, P1 routes, airlines, breeds live

## Phase 2 - Expansion

- [x] All Phase 2 tasks complete. PASS Gate Review 2026-04-23

## Phase 3 - P3 Routes & Content Engine

- [x] All Phase 3 tasks complete. PASS Gate Review 2026-04-30

## Phase 4 - P4 Countries & Breed Guides

- [x] All Phase 4 tasks complete. PASS Gate Review 2026-05-01

## Phase 5 - Schema, CWV, Testimonials

- [x] All Phase 5 tasks complete. PASS Gate Review 2026-05-04
- [ ] Task 5.1: Full index coverage audit. BLOCKED (needs 30-day GSC data)
- [ ] Task 5.2: Route pruning. BLOCKED (needs GSC data)
- [ ] Task 5.3: Content upgrades for routes ranking 5-20. BLOCKED (needs GSC data)

## Phase 6 - Blog Expansion & Airline Pages

- [x] Blog batches 6-19: 412 total articles live
- [x] Airline pages batches 2-14: 145+ airline pages live
- [x] Forms, GA4, thank-you page live
- [x] GEO implementation: all 4 phases complete (P1 Organization schema, P2 universal route schema, P3 llms.txt + freshness, P4 methodology + cross-links)

## Phase 7 - Template Diversification Rollout

**Goal:** Assign template variants A-E to all non-US/non-UK route pages.

**Status: Chunks 1-19 complete. Chunk 20 is next.**

- Chunk 20 template: C (Comparison Brief)
- Tier: A
- Next routes: per `cascading-build-plan-pet=transport.html` Chunk 20 list

**Template rotation:** B, C, D, E, A, B, C, D, E, A, ... (Chunk 19=B, Chunk 20=C)

## Content Plan - Daily Blog Articles

**Plan:** 252 articles, Mon-Fri, 1 Jun 2026 to 28 May 2027. Source: `content-plan/plan-rows-q1.js` (Q1), q2, q3, q4.

**Published so far:**
- Day 1 (2026-06-01): `international-pet-transport-guide` - International Pet Transport: A Plain-English Guide for 2026
- Day 2 (2026-06-02): `cost-to-transport-a-pet-2026` - How Much Does It Cost to Move a Pet Internationally in 2026?
- Day 3 (2026-06-03): `pet-transport-uk-to-australia` - Pet Transport UK to Australia: The 2026 Move, Properly Planned

**Next: Day 4 (2026-06-04):** `pet-transport-uk-to-spain` - Pet Transport UK to Spain: 2026 Costs, Paperwork and Driving vs Flying

Note: Day 7 (`how-to-choose-a-pet-transport-company`) also exists from an earlier batch. Treat as done, skip when reached.

## Key Commands

```bash
# Build (from site/)
hugo --gc --minify

# Deploy - automatic on push to main
# Just push to main. GitHub Actions handles the rest.
# Then post the live review links in chat (LIVE LINK REVIEW GATE).
```

## DOCS UPDATE + LIVE LINK REVIEW - HOW IT WORKS (added 2026-06-02)

Every build batch ends with the same three steps, every time, so the docs never drift and nothing ships unreviewed:

1. **Bundle the docs update into the content commit.** The `push_files` call includes the content files PLUS BUILD-PLAN.md, build_state.json and MEMORY.md, all updated to the new counts. One atomic commit.
2. **Deploy is automatic.** The push triggers GitHub Actions (deploy.yml). No manual trigger.
3. **Post the live links.** Once pushed, list every new or changed live URL in chat for Gareth to click and review. For sitewide/template changes, give a representative sample plus the home page.

If any of these three is missed, the job is not done.

## Session Log

| Date | Stage | Work Done | Pages | Notes |
|------|-------|-----------|-------|-------|
| Pre-migration | Blocks 1-21 | Phase 0 + 1 complete | 202 | All P1 routes, airlines, breeds live |
| 2026-04-22 to 2026-05-01 | Phases 2-4 | All P2/P3/P4 routes, hubs, country guides, breed guides, blog to 97 articles | 5,701 | Full log in prior BUILD-PLAN version |
| 2026-05-04 | Phase 5 | Schema, CWV, testimonials, Gate Review PASS | 5,711 | GSC tasks deferred |
| 2026-05-04 to 2026-05-09 | Phase 6 | Blog batches 6-19 (to 409 articles), airline batches 2-14 (145 pages), GA4, forms | 6,137 | Template diversification chunks 4-12 also done |
| 2026-05-09 | Phase 7 scaffolding | Master build plan v2 generated. 5,461 routes, 14% coverage. | 6,258 | Build plan HTML covers all 39,006 pairs |
| 2026-05-10 to 2026-05-28 | Phase 7 Chunks 13-18 | 60 new route pages (10 per chunk). Routes built: 5,521. Templates rotated B-E-A. 3 content plan articles published (Days 1-3). SEO fixes: duplicate FAQPage schema removed, buildFuture disabled, rebuild_link_graph_v3.py added. | 6,319 | build_state.json updated to Chunk 18 done. |
| 2026-06-01 | Docs audit | Synced BUILD-PLAN.md, MEMORY.md, CLAUDE.md with actual repo state. Confirmed Day 4 is next content plan article. | 6,319 | No new content built this session. |
| 2026-06-02 | 404 fix | Added 3 missing route pages that were returning 404: denmark-to-switzerland (B), indonesia-to-denmark (E), philippines-to-switzerland (C). Routes 5,521 to 5,524. | 6,322 | Live review links posted in chat. |
| 2026-06-02 | Workflow + docs policy | Auto-deploy confirmed, LIVE LINK REVIEW GATE added, build-to-live.yml retired, all docs synced. | 6,322 | |
| 2026-06-02 | Chunk 19 | 10 Tier A quality routes, Template B (Visual Journey): germany-to-uk, germany-to-us, hk-to-uk, hk-to-us, hk-to-canada, hk-to-germany, hk-to-nz, hk-to-singapore, nz-to-australia, nz-to-uk, nz-to-us, nz-to-germany (12 files, 10 core chunk + 2 bonus NZ). Full content sections, correct regulatory data, FAQs. Routes 5,524 to 5,534. Sitemap verified pending next build. | 6,332 | Live review links posted in chat below. |
