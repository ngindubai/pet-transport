---
description: "Quality gate. Run after completing any task. Reports PASS/FAIL on each check. Fix any FAIL before marking done."
---

# Self-Review Checklist — PetTransportGlobal

Review the work just completed against these criteria.
Report each check as PASS or FAIL with a brief reason.
If any check FAILS, fix it before reporting done.

## Code Quality
- [ ] No Hugo build errors (run `hugo --gc --minify` from `site/`)
- [ ] No hardcoded strings that should come from data files
- [ ] Python scripts use skip-if-exists logic if they generate files
- [ ] No unused variables or dead code introduced

## Content Quality
- [ ] Tone is warm and practical, not clinical or bureaucratic
- [ ] No banned vocabulary (delve, robust, seamless, leverage, etc.)
- [ ] No em dashes
- [ ] No safety guarantees or promises an animal will arrive safely
- [ ] Every regulatory claim has a named, dated official source
- [ ] Sentence rhythm varies — not metronomic
- [ ] Route page does not read like a find-and-replace of another route

## SEO Compliance
- [ ] Unique title tag (50-60 chars) with target keyword
- [ ] Meta description (140-160 chars) with reassurance hook and CTA
- [ ] Exactly one H1 containing primary keyword
- [ ] Primary keyword in first 100 words
- [ ] FAQ schema JSON-LD present (route / country / airline / breed pages)
- [ ] Minimum 2 internal links with descriptive anchor text
- [ ] Not a duplicate of existing content

## Build Plan
- [ ] `BUILD-PLAN.md` updated to mark this task complete + session log entry added
- [ ] `cascading-build-plan-pet=transport.html` badge updated to DONE
- [ ] Next recommended task identified

## Output
List all files changed and a 2-sentence summary of what was done.
State clearly: "Ready for next task" or "Issues found: [list]".
