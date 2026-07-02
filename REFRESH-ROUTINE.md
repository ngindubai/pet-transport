# Quarterly data-refresh routine (A9)

The site's value is current import rules. Rules change, so once a quarter we check
the data against the official sources and update anything that has moved. This is a
YMYL topic: no regulatory change is auto-applied. A person confirms every change
before it is committed.

## The routine, once a quarter

### Step 1: generate the worklist (2 minutes)

In the repo, run:

```
python3 refresh_audit.py --write
```

This writes `refresh-worklist.md`: a table of destination countries ranked by how
stale their "Regulations verified" date is, weighted by how many routes each one
affects, plus the official source for each. It changes no content. It only tells
you what to check and where.

### Step 2: re-check the top destinations against the official source

Work down the worklist from the top. For each destination, open the official
source (the last column of the table) and compare the current rules to what the
site says on that country's guide page and its route pages. The browser prompts in
`BROWSER-PROMPTS.md` (section "Quarterly regulatory re-check") do this with Claude
in Chrome: they open the authority page, pull the current requirements, and compare
them to the live site, flagging any differences.

Focus on the things that actually change: titre-test rules, quarantine length,
listed/unlisted status, health-certificate validity windows, and breed bans.

### Step 3: update only what changed

For any rule that has genuinely changed:

1. Update the source data in `data/govt_import_regulations.json` (and the relevant
   country/route front matter if the change is specific to it).
2. Update the `date:` field on the affected pages to the new verified date.
3. Commit with a clear message naming the country and what changed.

If nothing changed, still bump the verified `date:` on the checked pages so the
freshness signal stays honest, and note in the commit that it was a no-change
re-verification.

### Step 4: record it

Add a one-line entry to `BUILD-PLAN.md` (date, countries checked, what changed).

## Notes

- Priority = staleness in days x routes affected, so a stale rule on a high-volume
  destination rises to the top.
- `refresh_audit.py --stale-days 120` changes the "stale" threshold. Default is 90.
- Destinations without a specific authority in the script fall back to "national
  veterinary authority"; add them to the `AUTHORITY` map in the script as you go.
- The regulatory checking is deliberately manual. An agent can draft the comparison
  (see the browser prompts), but a human signs off before publish, because a wrong
  rule on a YMYL page is worse than a slightly stale one.
