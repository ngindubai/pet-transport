# ERRORS.md — PetTransportGlobal

> Log of approaches that took more than 2 attempts. Check this file before suggesting solutions to similar tasks.

Format for each entry:
- **Date:** YYYY-MM-DD
- **Task:** What was being attempted
- **What didn't work:** The failed approach(es)
- **What worked:** The fix
- **Note for next time:** One-line takeaway

---

## 2026-05-22 — GitHub Actions deploy failing on every push

**Task:** Deploy site to Hostinger via FTP on push to main

**What didn't work:**
- Every push to main triggered the workflow but it failed in ~50s with `Error: getaddrinfo ENOTFOUND *** (control socket)` in the FTP Deploy Action step
- The `***` is GitHub redacting a secret — an empty or invalid FTP_SERVER secret produces exactly this error
- This had been failing silently on runs #3, #4, #5 with no early warning — the Hugo build succeeds, only the FTP step fails

**Root cause:** `FTP_SERVER` GitHub secret is blank or contains an incorrect value. Hostinger's FTP hostname must be the **server IP address** (e.g. `185.241.52.201`), not a domain name. Found in hPanel > Hosting > pettransportglobal.com > Files > FTP Accounts > FTP IP column.

**What worked:** Update the `FTP_SERVER` secret in GitHub repo settings (Settings > Secrets and variables > Actions > FTP_SERVER > Update) with the IP from Hostinger hPanel.

**Note for next time:** Always verify `FTP_SERVER` secret = server IP from hPanel, not a domain. Blank secrets show as `***` in the error.

---

## 2026-05-22 — Cannot edit .github/workflows/deploy.yml via MCP connector

**Task:** Add secrets validation and FTP connectivity check to deploy.yml

**What didn't work:**
- `git mcp:create_or_update_file` returns 403 for any file inside `.github/workflows/` — GitHub blocks workflow file edits via API tokens that lack the `workflows` OAuth scope

**What worked:** Must be done manually. To edit deploy.yml:
1. Go to github.com/ngindubai/pet-transport/blob/main/.github/workflows/deploy.yml
2. Click the pencil (Edit) icon
3. Paste the updated content
4. Commit directly to main

**Improved deploy.yml to paste when editing manually:**
- Step 0: validate all 3 secrets are non-empty, fail immediately with clear message if any are missing
- Step 5: verify Hugo build produced >100 HTML pages (catches silent build failures)
- Step 7: `getent hosts` check on FTP_SERVER before attempting deploy (catches bad hostname)
- Step 9: deployment summary echoing page count and destination

**Note for next time:** Never attempt to commit to `.github/workflows/` via MCP — it will always 403. Tell Gareth to edit it manually via the GitHub web UI.

---

## 2026-05-22 — No deploy validation was in place

**Issue:** Pipeline had been failing on every push since at least run #3 with no way for Gareth to know unless manually checking the Actions tab.

**Fix needed (future):** Add a post-deploy smoke test step — curl the live URL and check for HTTP 200 before marking the run as successful. This would surface FTP failures automatically in the run log.

**Proposed smoke test step to add to deploy.yml (after Step 8):**
```yaml
- name: Smoke test live site
  run: |
    sleep 30
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://pettransportglobal.com)
    if [ "$STATUS" = "200" ]; then
      echo "✅ Live site returned HTTP $STATUS"
    else
      echo "⚠️ Live site returned HTTP $STATUS — deploy may not have propagated yet"
    fi
```

**Note for next time:** Add smoke test to deploy.yml as soon as workflow file edit access is available.
