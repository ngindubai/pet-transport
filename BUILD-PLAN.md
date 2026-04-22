# BUILD-PLAN.md — PetTransportGlobal

> For full stage detail, always reference `cascading-build-plan-pet=transport.html` first.
> This file is a quick-reference checklist and session log. Update it at the end of every session.

## Phase 0 — Research

- [x] 0.1: Worker souls adapted for pet transport domain
- [x] 0.2: PetRelocation.com competitor scrape and analysis
- [x] 0.3: Government import portal scrape (USDA APHIS, UK APHA, Australian DAFF, EU TRACES, Singapore AVS)
- [x] 0.4: Airline pet cargo policy scrape (20+ airlines)
- [x] 0.5: Route keyword research matrix
- [x] 0.6: Country regulations database built
- [x] 0.7: Airline database built
- [x] 0.8: Breed restriction database built
- [x] 0.9: Route database schema designed

## Phase 1 — Foundation

- [x] Block 10: Hugo project scaffolding
- [x] Block 11: All 6 templates + quote form widget
- [x] Block 12: Route data assembly — Tier 1 Batch 1 (first 8 routes)
- [x] Block 13: Route data assembly — Tier 1 Batch 2 (next 7 routes)
- [x] Block 14: Route page content — Batch 1
- [x] Block 15: Route page content — Batch 2
- [x] Block 16: 10 country guides + 10 origin country hubs
- [x] Block 17: SEO pass + humanisation + internal linking
- [x] Block 18: QA + first deploy
- [x] Block 19: All 89 P1 routes complete — 132 pages, deployed 21 April 2025
- [x] Block 20: 23 airline guide pages — 190 pages total
- [x] Block 21: 35 breed guide pages — 202 pages total, deployed

## Phase 2 — Expansion

- [ ] Block 22 / Task 2.1: P2 country regulation data (15 additional countries)
- [ ] Block 23 / Task 2.2: ~500 P2 route pages
- [ ] Block 24 / Task 2.3: 15 P2 origin hubs + 15 P2 country guides
- [ ] Block 25 / Task 2.6: Internal link graph rebuild (all content types)
- [ ] Block 26 / Task 2.7: Blog launch — 12 research-intent articles
- [ ] Block 27 / Task 2.8: Backlink campaign
- [ ] Block 28 / Task 2.9: Full QA + regulatory audit (all 800+ pages)
- [ ] Block 29 / Task 2.10: Site health monitoring setup

## Current Status

**202 pages live.** Next stage: Block 22 — P2 country regulation data.

## Key Commands

```bash
# Build (from site/)
hugo --gc --minify

# Deploy (from site/, requires live terminal)
surge public pettransportglobal.surge.sh
```

## Session Log

| Date | Stage | Work Done | Pages | Notes |
|------|-------|-----------|-------|-------|
| Pre-migration | Blocks 1-21 | Phase 0 + 1 complete | 202 | All P1 routes, airlines, breeds live |
