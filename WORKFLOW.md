# PetTransportGlobal — Claude App Workflow Guide

## What this project is
Programmatic SEO site at pettransportglobal.com. Built with Hugo (static site). Hosted on Hostinger. Repository is on GitHub. GitHub Actions auto-deploys on every push to `main`.

## Production deployment

`build-to-live.yml` is the only production publisher. It validates and builds `main`, publishes compiled output to `live`, and Hostinger Git deploys `live`. Pull requests run the non-publishing `quality-gates.yml` workflow. See `DEPLOY.md` for configuration and rollback details.

---

## Build pipeline (local)

```bash
# Full local build — runs link graph rebuild + hugo + sitemap split
build.bat               # Windows
make build              # Linux/macOS
```

Or step by step:
```bash
python rebuild_link_graph_v3.py   # Step 1: regenerate all internal links
cd site && hugo --gc --minify     # Step 2: hugo build
cd .. && python split_sitemap.py  # Step 3: split sitemap
```

---

## How to say "go" — three modes

### Mode 1: Build the next 10 quality routes (Tier A or B)
When the user says **"go"** or **"next chunk"**, Claude should:
1. Read `build_state.json` in the repo root to find `next_tier_a_index` or `next_tier_b_index`
2. Read `pet-transport-build-plan.html` or run `python generate_build_plan_v2.py --state` to get the next 10 unbuilt routes
3. Write each route file to `site/content/routes/{slug}.md` using the route format below
4. Update `build_state.json`: increment the chunk index
5. Commit all new route files + updated `build_state.json`
6. Push to `main` — GitHub Actions will build Hugo + deploy to Hostinger

### Mode 2: Auto-generate a batch of lower-tier routes (Tier C/D)
When the user says **"auto-generate C"** or **"run the batch generator"**:
- Push a trigger commit to GitHub that updates `build_state.json` with `run_auto_gen: true`
- In GitHub Actions, after Hugo build, `generate_all_remaining.py --batch 500 --tier C` runs and creates up to 500 Tier C routes
- Full site rebuilds and deploys

**Or — run it locally first:**
```
python generate_all_remaining.py --batch 500 --tier C
git add site/content/routes/
git commit -m "feat: auto-generate 500 Tier C routes"
git push
```

### Mode 3: Generate ALL remaining routes at once (fastest path to completion)
```
python generate_all_remaining.py
git add site/content/routes/
git commit -m "feat: generate all remaining routes"
git push
```
This generates all 33,545 routes in ~10 minutes, commits them, pushes, and GitHub Actions deploys.

---

## Route file format

All files go to: `site/content/routes/{origin-slug}-to-{destination-slug}.md`

Slugs: lowercase, hyphen-separated. Example: `united-kingdom-to-australia.md`

Front matter must include:
```yaml
---
title: "Pet Transport [Origin] to [Destination] | PetTransportGlobal"
description: "140-160 char description with reassurance hook and CTA."
type: "routes"
layout: "single"
author: "Pet Transport Global Editorial Team"
slug: "{origin-slug}-to-{destination-slug}"
origin_name: "Origin Country"
destination_name: "Destination Country"
route_data:
  origin:
    code: "XX"
    country: "Origin Country"
    export_requirements:
      export_permit: "..."
  destination:
    code: "YY"
    country: "Destination Country"
    import_requirements:
      microchip: "..."
      rabies_vaccination: "..."
      titre_test: "..."
      quarantine: "..."
      import_permit: "..."
      health_certificate: "..."
  airlines:
    - name: "Emirates"
      type: "cargo_only"
      policy_summary: "..."
  timeline_steps:
    - step: 1
      action: "..."
      timing: "..."
      responsible: "owner"
  cost_factors:
    - "..."
  key_warnings:
    - "..."
  route_complexity: "low|moderate|high|very_high"
  estimated_timeline_weeks: "4-8"
content:
  h1: "Pet Transport from [Origin] to [Destination]"
  overview: |
    2-3 paragraph warm-expert overview. No em dashes. No banned vocab.
  sections:
    - heading: "Key requirements..."
      body: |
        ...
faqs:
  - question: "..."
    answer: "..."
links:
  sideways:
    - url: "/pet-transport/{dest-slug}-to-{origin-slug}/"
      text: "Pet Transport {Destination} to {Origin}"
  upward:
    - url: "/pet-transport/origins/{origin-slug}-pet-export-guide/"
      text: "Shipping from {Origin}"
    - url: "/pet-transport/countries/{dest-slug}/"
      text: "Importing to {Destination}"
---
```

---

## Content rules (non-negotiable)
1. No em dashes (use commas, full stops, or "and" instead)
2. No banned vocabulary: "delve", "meticulous", "comprehensive", "tailored", "navigate", "leverage", "seamless", "robust", "vital", "crucial", "utilize"
3. No safety guarantees — say "reduce risk", "IATA-compliant", "experienced handlers"
4. Every regulatory claim needs a named source (USDA APHIS, UK APHA, Australian DAFF, etc.)
5. Warm, practical, expert tone — not clinical. Pet owners are anxious.
6. FAQ schema JSON-LD is generated automatically by the Hugo template from `faqs:` front matter

---

## After writing route files
```bash
build.bat       # Windows — runs link graph rebuild + hugo + sitemap
make build      # Linux/macOS
```

Or manually:
```bash
python rebuild_link_graph_v3.py
cd site && hugo --gc --minify
cd .. && python split_sitemap.py
git add site/content/routes/
git commit -m "feat: build chunk [N] — [origin] routes ([template])"
git push
```

---

## Track progress
Run this to see current state:
```
python generate_all_remaining.py --dry-run
```

Or open `pet-transport-build-plan.html` in a browser — it shows built/remaining with progress bars per country.

---

## Build tracker files
| File | Purpose |
|------|---------|
| `pet-transport-build-plan.html` | Master route tracker (39,006 pairs, tier/score, progress) |
| `cascading-build-plan-pet=transport.html` | Full project plan (all phases) |
| `BUILD-PLAN.md` | Session log + quick-reference checklist |
| `build_state.json` | Machine-readable current chunk index (read by Claude app) |

---

## Tier priority order
Build in this order for best ROI:

| Tier | Score | Count | Strategy |
|------|-------|-------|----------|
| A | ≥ 7.0 | 45 | Hand-crafted by Claude — 5 chunks of 10 |
| B | 5.5–6.9 | 1,094 | Claude-assisted or auto-gen — 110 chunks |
| C | 4.0–5.4 | 7,720 | Auto-gen with `generate_all_remaining.py` |
| D | < 4.0 | 24,686 | Auto-gen with `generate_all_remaining.py` |

**Fastest path to completion:** Run `generate_all_remaining.py` (all tiers at once).
**Quality path:** Build A + B manually via Claude sessions, auto-gen C + D.
