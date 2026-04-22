# AGENTS.md — PetTransportGlobal

## Agent Setup

Two agents are configured in `.github/agents/`:

| Agent | File | Use for |
|-------|------|---------|
| `pet-transport` | `.github/agents/pet-transport.agent.md` | Primary build agent — executes build stages |
| `reviewer` | `.github/agents/reviewer.agent.md` | Read-only QA reviewer |

In VS Code Copilot, select the `pet-transport` agent to continue the build. Start with: **"Continue the build"** and it will read the plan and find the next TODO block.

---

## 14 Worker Souls

Workers are domain-specific expert roles, each with their own rules, voice, and quality gates. Load only the workers needed for each block.

| Worker | File | Role |
|--------|------|------|
| The Architect | `workforce/leadership/the-architect.md` | Orchestration, planning, phase gates |
| The Auditor | `workforce/leadership/the-auditor.md` | YMYL compliance, regulatory accuracy, QA |
| The Wordsmith | `workforce/content/the-wordsmith.md` | Copywriting, authority voice |
| The Chameleon | `workforce/content/the-chameleon.md` | Anti-AI humaniser (mandatory on all content) |
| The Interrogator | `workforce/content/the-interrogator.md` | FAQ generation |
| The Geographer | `workforce/intelligence/the-geographer.md` | Route regulations, quarantine, country intelligence |
| The Scout | `workforce/intelligence/the-scout.md` | Keyword research, market reconnaissance |
| The Spider | `workforce/intelligence/the-spider.md` | Web scraping, regulatory data extraction |
| The Builder | `workforce/development/the-builder.md` | Hugo templates, page generation, deployment |
| The Librarian | `workforce/development/the-librarian.md` | Route JSON assembly, data management |
| The Optimiser | `workforce/seo/the-optimiser.md` | On-page SEO, schema markup, E-E-A-T |
| The Connector | `workforce/seo/the-connector.md` | Internal linking, link graph |
| The Analyst | `workforce/monitoring/the-analyst.md` | Performance tracking, analytics |
| The Watchdog | `workforce/monitoring/the-watchdog.md` | Site health monitoring |

All paths above are relative to the repo root.

---

## First Session Opening

When opening a new VS Code session on this project, say:

> "Continue the pet transport build."

The agent will:
1. Read `MEMORY.md` and `BUILD-PLAN.md`
2. Open `cascading-build-plan-pet=transport.html`
3. Find the first TODO block
4. Load the relevant workers
5. Execute

---

## Vetting Framework

`workforce/vetting_framework.md` defines Bronze/Silver/Gold operator tiers. Reference when building operator directory pages or quote form logic.
