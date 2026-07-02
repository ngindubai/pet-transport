#!/usr/bin/env python3
"""
refresh_audit.py  (A9 - quarterly data-freshness routine)

Purpose
-------
This is the "what needs re-checking" half of the quarterly refresh. It does NOT
change any content. It scans the route pages, groups them by destination country
(import rules are per destination), reads each route's "Regulations verified"
date, and prints a prioritised worklist of which countries' rules are the
stalest and how many routes each one affects. It also lists the official sources
recorded in data/govt_import_regulations.json so the reviewer knows where to look.

The actual re-checking (opening DEFRA, DAFF, APHIS, EU, CDC, etc. and comparing
the current rules to what the site says) is a human step, done with the browser
prompts in REFRESH-ROUTINE.md. A regulatory change is YMYL, so nothing here is
auto-applied: a person confirms every change before it is committed.

Usage
-----
    python3 refresh_audit.py                 # print the worklist
    python3 refresh_audit.py --write         # also write refresh-worklist.md
    python3 refresh_audit.py --top 20        # limit the printed table
    python3 refresh_audit.py --stale-days 120 # flag anything older than N days

Run it at the start of each quarter.
"""
import re, json, pathlib, argparse, datetime, collections, sys

ROOT = pathlib.Path(__file__).resolve().parent
ROUTES = ROOT / "site" / "content" / "routes"
REG = ROOT / "data" / "govt_import_regulations.json"

# Minimal destination -> authority hint for the major regimes. Everything else
# falls back to "national veterinary authority" in the worklist.
AUTHORITY = {
    "United Kingdom": "DEFRA / APHA (gov.uk/bring-pet-to-great-britain)",
    "Australia": "DAFF (agriculture.gov.au/biosecurity-trade/cats-dogs)",
    "United States": "CDC + USDA APHIS (cdc.gov/importation, aphis.usda.gov)",
    "New Zealand": "MPI (mpi.govt.nz)",
    "Canada": "CFIA (inspection.canada.ca)",
    "Japan": "MAFF Animal Quarantine Service (maff.go.jp/aqs)",
    "Singapore": "NParks AVS (nparks.gov.sg/avs)",
    "United Arab Emirates": "MOCCAE (moccae.gov.ae)",
}
EU = {"Austria","Belgium","Bulgaria","Croatia","Cyprus","Czech Republic","Denmark",
      "Estonia","Finland","France","Germany","Greece","Hungary","Ireland","Italy",
      "Latvia","Lithuania","Luxembourg","Malta","Netherlands","Poland","Portugal",
      "Romania","Slovakia","Slovenia","Spain","Sweden"}


def field(text, key):
    m = re.search(r'(?m)^%s:\s*"?(.*?)"?\s*$' % key, text)
    return m.group(1) if m else ""


def parse_date(s):
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s or "")
    if not m:
        return None
    try:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--stale-days", type=int, default=90)
    ap.add_argument("--today", default=datetime.date.today().isoformat(),
                    help="reference date (YYYY-MM-DD), defaults to today")
    args = ap.parse_args()
    today = parse_date(args.today) or datetime.date.today()

    by_dest = collections.defaultdict(lambda: {"count": 0, "dates": [], "undated": 0})
    for p in ROUTES.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        dest = field(t, "destination_name")
        if not dest:
            continue
        d = parse_date(field(t, "date"))
        rec = by_dest[dest]
        rec["count"] += 1
        if d:
            rec["dates"].append(d)
        else:
            rec["undated"] += 1

    rows = []
    for dest, rec in by_dest.items():
        oldest = min(rec["dates"]) if rec["dates"] else None
        newest = max(rec["dates"]) if rec["dates"] else None
        age = (today - oldest).days if oldest else None
        # Priority = staleness (days) weighted by how many routes are affected.
        priority = (age or 9999) * rec["count"]
        auth = AUTHORITY.get(dest) or ("EU Reg 2020/692 (food.ec.europa.eu/animals)" if dest in EU
                                       else "national veterinary authority")
        rows.append({
            "dest": dest, "routes": rec["count"], "undated": rec["undated"],
            "oldest": oldest.isoformat() if oldest else "no date",
            "newest": newest.isoformat() if newest else "no date",
            "age_days": age if age is not None else "-",
            "authority": auth, "priority": priority,
        })
    rows.sort(key=lambda r: r["priority"], reverse=True)

    flagged = [r for r in rows if isinstance(r["age_days"], int) and r["age_days"] >= args.stale_days]
    lines = []
    lines.append(f"# Quarterly refresh worklist  (generated for {today.isoformat()})")
    lines.append("")
    lines.append(f"Destinations: {len(rows)}. Flagged as stale (verified >= {args.stale_days} days ago): {len(flagged)}.")
    lines.append("Re-check the highest-priority destinations first. Priority = staleness x routes affected.")
    lines.append("")
    lines.append("| # | Destination | Routes | Oldest verified | Age (days) | Where to re-check |")
    lines.append("|---|---|---|---|---|---|")
    for i, r in enumerate(rows[:args.top], 1):
        lines.append(f"| {i} | {r['dest']} | {r['routes']} | {r['oldest']} | {r['age_days']} | {r['authority']} |")

    # Sources recorded in the regulations data file, for reference.
    if REG.exists():
        try:
            meta = json.load(open(REG)).get("metadata", {})
            srcs = meta.get("sources", [])
            if srcs:
                lines.append("")
                lines.append("## Official sources on record (data/govt_import_regulations.json)")
                for s in srcs:
                    lines.append(f"- {s}")
        except Exception:
            pass

    out = "\n".join(lines)
    print(out)
    if args.write:
        (ROOT / "refresh-worklist.md").write_text(out + "\n", encoding="utf-8")
        print("\n[written to refresh-worklist.md]", file=sys.stderr)


if __name__ == "__main__":
    main()
