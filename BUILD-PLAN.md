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

**Where we are (reconciled from disk 2026-06-03):** 5,172 quality routes complete. ~32,658 routes remaining. Blog: 412 articles. Total .md source files: 5,957 (full deployed total verified from sitemap.xml after a build). Content plan: Day 4 is next. Counts come from `python verify_build_state.py`, never hand-edited.

---

## Phase 7 - Template Diversification Rollout

**Status: Chunks 1-20 complete. Chunk 21 is next.**

- Chunk 21 template: D (Conversational Q&A)
- Tier: A
- Template rotation: ...B(19), C(20), D(21), E(22), A(23)...

## Content Plan - Daily Blog Articles

**Published so far:**
- Day 1: `international-pet-transport-guide`
- Day 2: `cost-to-transport-a-pet-2026`
- Day 3: `pet-transport-uk-to-australia`

**Next: Day 4** - `pet-transport-uk-to-spain` (REPLACE IN PLACE: upgrade the existing `uk-to-spain-pet-transport-complete-guide.md` to full quality and keep its URL. Do not publish a duplicate. See MEMORY.md Content Plan.)

## Session Log

| Date | Stage | Work Done | Pages | Notes |
|------|-------|-----------|-------| ------|
| 2026-06-02 | Chunk 19 | 12 Tier A routes, Template B (Visual Journey). Germany-UK/US, HK corridors, NZ corridors. YAML fix pushed separately (stray top-level key in germany-to-uk). | 6,332 | Live links posted. |
| 2026-06-02 | Chunk 20 | 11 Tier A routes, Template C (Comparison Brief). NZ-Canada/SG/UAE, Singapore corridors (AU/CA/DE/NZ/UK/US/HK/FR). All with comparison tables and airline comparison tables. | 6,342 | Live links to be posted. |
| 2026-06-03 | Truth audit | No site pages. Added `verify_build_state.py` + SessionStart hook (anti-drift). Reconciled all four docs to true disk counts: routes 5,544 -> 5,172, total 6,342 -> 5,957. Logged legacy debt (248 Gareth-authored blogs, em dashes in 5 blog + 69 route files). Recorded Day 4 = replace-in-place. | 5,957 | Docs/script/hook only, no deploy, no live links. |
| 2026-06-04 | Legacy cleanup 1: em-dash sweep | No pages added/removed. Removed all em dashes from site/content: 74 blog+route files via Python sweeper + 11 pet-transport files + 4 static pages. Zero em dashes remain. Counts unchanged: 5,172 routes, 412 blog, 5,957 total. | 5,957 | Changed pages on all routes/blog/static with em dashes. Deploy will run; no new pages to review. |
