#!/usr/bin/env python3
"""Fast, dependency-free source checks used before every Hugo build."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "site" / "content"
ROUTES = CONTENT / "routes"
COMPANY_AUTHOR = "Pet Transport Global Editorial Team"


def front_matter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end >= 0 else ""


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*['\"]?(.+?)['\"]?\s*$", frontmatter)
    return match.group(1).strip().strip("'\"") if match else ""


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    counts: Counter[str] = Counter()

    production = ROOT / ".github" / "workflows" / "build-to-live.yml"
    if not production.exists():
        errors.append("missing the live-branch production workflow")
    if (ROOT / ".github" / "workflows" / "deploy.yml").exists():
        errors.append("legacy FTP production workflow still exists")
    for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
        body = workflow.read_text(encoding="utf-8")
        if re.search(r"FTP-Deploy|FTP_PASSWORD|ftp://", body, re.I):
            errors.append(f"FTP deployment code remains in {workflow.relative_to(ROOT)}")

    sensitive_files = [
        ROOT / "site" / "assets" / "js" / "main.js",
        ROOT / "site" / "static" / "submit.php",
        ROOT / "CLAUDE.md",
        ROOT / "cascading-build-plan-pet=transport.html",
    ]
    for path in sensitive_files:
        body = path.read_text(encoding="utf-8")
        if re.search(r"garethsomers@outlook\.com|uRc1IHymlMUnYfAB", body, re.I):
            errors.append(f"known exposed credential or personal inbox remains in {path.relative_to(ROOT)}")
        if path.suffix == ".js" and re.search(r"x-api-key|(?:CRM|API)_KEY\s*=", body, re.I):
            errors.append(f"client-side API credential handling remains in {path.relative_to(ROOT)}")

    all_public_source = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in [ROOT / "site" / "content" / "privacy.md", ROOT / "site" / "content" / "terms.md"]
    )
    if re.search(r"\b0?9897762\b", all_public_source):
        errors.append("the unverified company registration number is present in legal copy")

    if 'data-sitekey=""' in (ROOT / "site" / "layouts" / "partials" / "quote-form.html").read_text(encoding="utf-8"):
        errors.append("empty bot-protection widget remains in the quote form")

    invalid_sideways = re.compile(r"(?ms)^\s{2}sideways:\s*$.*?(?=^\s{2}\w|^\S|\Z)")
    string_item = re.compile(r"(?m)^\s{4}-\s+(?:['\"]?/|https?://)")
    contradiction_answer = "Yes, a rabies titre test is required. Blood must be drawn"

    for path in sorted(CONTENT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        rel = path.relative_to(ROOT)
        if not fm:
            errors.append(f"{rel}: missing or unclosed YAML front matter")
            continue
        if path.name != "_index.md":
            if not scalar(fm, "title"):
                errors.append(f"{rel}: missing title")
            if not scalar(fm, "description"):
                errors.append(f"{rel}: missing description")

        author = scalar(fm, "author")
        if author:
            counts["pages_with_author"] += 1
            if author != COMPANY_AUTHOR:
                errors.append(f"{rel}: unverified named author '{author}'")

        if re.search(r"\bdays\s+days\b", text, re.I):
            errors.append(f"{rel}: contains duplicated phrase 'days days'")
        if path.parent == ROUTES and path.name != "_index.md":
            counts["routes"] += 1
            if re.search(r"the relevant government body|government-run facility|days minimum days", text, re.I):
                errors.append(f"{rel}: contains an unresolved generated-content placeholder")
            if not scalar(fm, "date") and not scalar(fm, "verified_at"):
                counts["routes_without_verification_date"] += 1
            block = invalid_sideways.search(fm)
            if block and string_item.search(block.group(0)):
                errors.append(f"{rel}: links.sideways must use url/text objects")

            titre = re.search(r"(?m)^\s{6}titre_test:\s*['\"]?(.+)$", fm)
            if titre and re.match(r"\s*(?:not required|no |required for:\s*not)", titre.group(1), re.I):
                if contradiction_answer.lower() in fm.lower():
                    errors.append(f"{rel}: titre-test source and FAQ contradict each other")

    freshness_partial = (ROOT / "site" / "layouts" / "partials" / "verified-date.html").read_text(encoding="utf-8")
    if re.search(r"\bnow\b", freshness_partial):
        errors.append("verified-date.html still substitutes the build time for a verification date")

    base_template = (ROOT / "site" / "layouts" / "_default" / "baseof.html").read_text(encoding="utf-8")
    if "routes_without_verification" not in base_template:
        warnings.append("base template does not contain the undated-route indexing guard marker")

    print(f"Source check: {counts['routes']} routes; {counts['routes_without_verification_date']} without a recorded verification date")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        print(f"ERROR: {len(errors)} source validation issue(s)", file=sys.stderr)
        for message in errors[:200]:
            print(f"  - {message}", file=sys.stderr)
        if len(errors) > 200:
            print(f"  ... {len(errors) - 200} more", file=sys.stderr)
        return 1
    print("Source validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
