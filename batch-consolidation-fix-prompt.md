# Batch Consolidation Fix: prompt + plan

## How to use this
Paste everything under "PROMPT FOR THE AGENT" into a new Claude Code session that has
**all five repos attached** (pet-transport, mortgagecompare-ae, global-bus-hire,
funeral-repatriation, closeprotectionhure-com). The agent edits the repo instruction files.
The schedule and routine-prompt changes are UI tasks only you can do, collected in the
"FOR GARETH (manual, claude.ai UI)" section at the end.

## Why this change
Claude Pro Max includes 15 routine runs/day. The current setup fires each of the 5 site
routines about 8 times/day (40+ runs), which exceeds the allowance. The fix is fewer runs,
each building a bigger batch, so total daily output stays flat.

- Old: ~8 runs/day/site x 1 block = 8 blocks/day/site.
- New: 2 runs/day/site x 4 blocks = 8 blocks/day/site. Output unchanged.
- 5 sites x 2 runs + 1 reporter = 11 runs/day, under the 15 cap.
- Batch multiplier: x4.

The instruction files currently forbid bigger batches ("one block at a time", "one go = one
block, never more"), so those caps must be lifted to "up to 4 blocks per run". The ban on
bulk-generation scripts stays: a batch is still N individually quality-gated blocks, not a
mass-generation script.

---

## PROMPT FOR THE AGENT

You are updating the build instructions across five repos so each scheduled routine builds a
batch of blocks per run instead of a single block. You are NOT building site content in this
session. You only edit instruction/doc files and commit them. Make no other changes.

GLOBAL TARGET (applies to every repo):
- A scheduled run now builds UP TO 4 blocks (a "batch"), not 1. Floor is 1.
- "Block" keeps each repo's own existing definition (see per-repo notes below).
- Every block in the batch still runs that repo's FULL quality gate. Quality first: if a run
  cannot finish 4 blocks cleanly, it builds as many as it can do well (minimum 1), commits
  those, and reports the shortfall. Never skip the quality gate to hit 4.
- The whole batch is committed ONCE per run (one commit, one push, one deploy), not one
  commit per block. This avoids the concurrent-deploy race that funeral and close-protection
  warn about, and keeps a single clean deploy per run.
- The old "if already built today, SKIP" logic must be removed or rewritten, because each
  site now runs twice a day. Replace it with: skip only if the build pointer (next chunk /
  next content-plan day / next unchecked plan item) shows nothing left to build.
- Preserve every existing rule: the em dash ban, banned vocabulary, British English, author
  personas, no-prices or pricing rules as they stand per repo, the bulk-generation-script
  ban, and the correct branch (main for pet-transport, mortgagecompare-ae, global-bus-hire;
  master for funeral-repatriation and closeprotectionhure-com).

FOR EACH REPO, DO THIS:
1. Read the repo's CLAUDE.md and BUILD-PLAN.md (and any cascading-plan file it references,
   e.g. the bodyguard or global-bus-hire cascading plan HTML).
2. Find every place that caps work at one block per run. Typical phrasings: "one block at a
   time", "one go = one block", "never more than one block", "build exactly one block",
   "one block per run". Change each to the batch rule: "one run builds a batch of up to 4
   blocks; each block runs the full quality gate; the batch is committed once; bulk-generation
   scripts remain banned."
3. Find any "already built today, skip" guidance in the repo docs and rewrite it to the
   pointer-based skip described above (skip only when nothing is left to build).
4. Add a one-line note in BUILD-PLAN.md recording the change: date, "switched to batch builds
   of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap".
5. Commit the doc changes to the repo's correct branch using native git (git add, git commit,
   git push origin HEAD:<branch>), then verify the remote advanced (git ls-remote origin
   <branch> SHA matches your commit) before moving on. One commit per repo. Commit message:
   "docs: batch builds (up to 4 blocks/run) to fit 15-run routine cap".
6. Do NOT touch .github/workflows (403). Do NOT edit the live/master deploy branches directly.

PER-REPO BLOCK DEFINITIONS (so "4 blocks" is concrete):
- pet-transport (main): block = one route chunk (~10-25 routes) OR one content-plan blog day.
  A batch = up to 4 chunks (or 3 chunks + the due blog day). After building, run
  `python verify_build_state.py --write` ONCE for the whole batch, update BUILD-PLAN.md,
  build_state.json and MEMORY.md once, commit once. The next_chunk pointer advances across
  the batch.
- mortgagecompare-ae (main): block = one content-plan article. Batch = up to 4 next articles
  in date order. Update knowledge-hub/guides index and sitemap.xml once for the batch.
- global-bus-hire (main): block = one _patch city batch. Batch = up to 4 such batches (or one
  larger _patch covering ~4x the cities). Every page keeps the mobile hamburger nav and
  LocalBusiness schema. Never touch site/index.html.
- funeral-repatriation (master): block = one blog batch or route set. Batch = up to 4. One
  push per run (concurrent deploys clobber). No prices. Persona authors only.
- closeprotectionhure-com (master): block = one service x 10 cities OR one 5-blog batch.
  Batch = up to 4 blocks. master ONLY, never main. Keep buildFuture, no escaped-quote printf,
  no invented layouts.

AT THE END:
- For EACH repo, also output (in your final message, do not commit to .github) the updated
  routine prompt text Gareth should paste into that routine in the claude.ai UI: specifically
  the rewritten STEP 1 (build a batch of up to 4 blocks), the rewritten budget/skip step (no
  same-day skip; pointer-based skip), the single batched commit+push+verify step, and the
  final "stop after one batch per run" step. Use the pet-transport example below as the
  pattern and adapt each to that repo's block type and branch.
- Post a short summary: which repos were edited, the commit SHA per repo, and the five updated
  prompt blocks for Gareth to paste.

PET-TRANSPORT PROMPT PATTERN (adapt per repo; this replaces the single-block steps):

  STEP 0 - BUDGET TRIPWIRE + POINTER SKIP (no same-day skip)
  - On any usage/rate-limit error: STOP, post to the site's Slack channel
    "PAUSED <site>: usage limit, protecting reserve." End.
  - Skip ONLY if the build pointer shows nothing left to build (e.g. no chunks and no blog
    day due). Do NOT skip just because a build happened earlier today; this routine runs
    twice a day on purpose.

  STEP 1 - BUILD A BATCH OF UP TO 4 BLOCKS
  - Build up to 4 blocks this run, each through the FULL quality gate (research from data
    files + named sources, voice, template rotation, humanise, QA scan, zero em dashes, zero
    banned vocab). Advance the pointer after each block. Quality first: if you cannot finish
    4 cleanly, build as many as you can do well (minimum 1) and note the shortfall in Slack.

  STEP 2 - RECONCILE COUNTS ONCE (pet-transport)
  - After the whole batch: python verify_build_state.py --write. Never hand-edit counts. If
    verify fails: STOP, post "BUILD HALTED <site>: count verification failed." End.

  STEP 3 - ONE COMMIT + PUSH FOR THE WHOLE BATCH (native git, not push_files)
  - git add -A
  - git commit -m "build: <site> batch of <N> blocks (<detail>)"
  - git push origin HEAD:<branch>   (main for pet-transport)

  STEP 4 - VERIFY THE PUSH LANDED, then retry, then alarm
  - git ls-remote origin <branch> SHA must equal git rev-parse HEAD. If not, wait 30s and
    retry the push, then 60s and retry once more (two retries), re-verifying each time.
  - Only when the remote SHA matches do you proceed to Slack. If it still does not match after
    three attempts: post "COMMIT FAILED <site> after 3 attempts. Nothing pushed." End. Do not
    post live links.

  STEP 5 - DEPLOY IS AUTOMATIC
  - The single push triggers the site's deploy workflow. Do not touch .github/workflows. Do
    not edit the deploy branch. One push per run = one deploy.

  STEP 6 - SLACK: COMMITTED + LIVE LINK REVIEW
  - Post ONE message to the site's channel: "COMMITTED <site> batch: <N> blocks, <X> pages.
    Live in ~<deploy time> mins." Then every new/changed page's full live URL, one per line.

  STEP 7 - STOP. One batch (up to 4 blocks) per run.

---

## FOR GARETH (manual, claude.ai UI) - the agent cannot do these

### 1. Reschedule each routine to 2 runs/day, staggered (all times UAE)
Keep 40-minute spacing inside each wave so two Hugo-to-live deploys never collide.

| Routine | Morning | Afternoon |
|---|---|---|
| Pet Transport | 06:00 | 14:00 |
| Mortgage Compare | 06:40 | 14:40 |
| Bus Hire | 07:20 | 15:20 |
| Funeral Repatriation | 08:00 | 16:00 |
| Close Protection | 08:40 | 16:40 |
| Daily Reporter | (one run) 20:00 | - |

Total: 11 runs/day. Under the 15 cap, leaving ~4 spare for manual "Run now" or catch-up.

### 2. Update each routine's pasted prompt
For each routine, replace its single-block steps with the batch steps the agent outputs at the
end of its run (STEP 0 pointer-skip, STEP 1 build up to 4 blocks, STEP 3 one batched
commit+push, STEP 4 verify, STEP 7 stop after one batch).

### 3. Confirm the GitHub connector is attached to each routine
Not just Slack. The commit+push and verify steps rely on the repo being reachable.

### 4. Tune after the first day
4 blocks per run is the target to hold output flat. If a run cannot finish 4 cleanly (time,
context, or usage window), it will build fewer and report it. If that happens repeatedly,
either lower the batch to 3 or add a third daily run for that site (budget permitting: 5 sites
at 3 runs would be 15, leaving no room for the reporter, so prefer batch 3).
