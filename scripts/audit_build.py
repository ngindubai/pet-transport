#!/usr/bin/env python3
"""Audit critical properties of the rendered Hugo output."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "site" / "public"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.in_h1 = False
        self.in_jsonld = False
        self.title: list[str] = []
        self.h1: list[str] = []
        self.jsonld: list[str] = []
        self.jsonld_blocks: list[str] = []
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "script" and values.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.jsonld = []
        elif tag == "meta":
            if values.get("name") == "description":
                self.description = values.get("content") or ""
            if values.get("name") == "robots":
                self.robots = values.get("content") or ""
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href") or ""
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
        elif tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            self.jsonld_blocks.append("".join(self.jsonld).strip())

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title.append(data)
        if self.in_h1:
            self.h1.append(data)
        if self.in_jsonld:
            self.jsonld.append(data)


def target_path(url: str) -> Path | None:
    if url.startswith("#"):
        return None
    parsed = urlparse(url)
    if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
        return None
    if parsed.netloc and parsed.netloc not in {"pettransportglobal.com", "www.pettransportglobal.com"}:
        return None
    path = unquote(parsed.path)
    if not path or path == "/":
        return PUBLIC / "index.html"
    candidate = PUBLIC / path.lstrip("/")
    if path.endswith("/"):
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    return candidate / "index.html"


def main() -> int:
    if not PUBLIC.exists():
        print("ERROR: site/public does not exist", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    canonical_seen: dict[str, Path] = {}
    target_cache: dict[Path, bool] = {}
    broken_targets: dict[str, list[str]] = {}
    html_files = sorted(PUBLIC.rglob("*.html"))
    print(f"Auditing {len(html_files)} rendered HTML pages...", flush=True)

    for index, path in enumerate(html_files, 1):
        rel = path.relative_to(PUBLIC)
        if rel.parts and rel.parts[0] in {"fonts", "img", "images", "js", "css", "styles", "vendor", "videos"}:
            continue
        body = path.read_text(encoding="utf-8", errors="replace")
        parser = PageParser()
        parser.feed(body)
        title = " ".join("".join(parser.title).split())

        if re.search(r"http-equiv=(?:['\"])?refresh", body, re.I):
            continue

        if not title:
            errors.append(f"{rel}: missing title")
        elif len(title) > 70:
            warnings.append(f"{rel}: title is {len(title)} characters")
        if not parser.description:
            errors.append(f"{rel}: missing meta description")
        elif len(parser.description) > 165:
            warnings.append(f"{rel}: description is {len(parser.description)} characters")
        if not parser.canonical:
            errors.append(f"{rel}: missing canonical")
        elif parser.canonical in canonical_seen:
            errors.append(f"{rel}: duplicate canonical also used by {canonical_seen[parser.canonical].relative_to(PUBLIC)}")
        else:
            canonical_seen[parser.canonical] = path

        if not parser.h1 and "404" not in path.name:
            errors.append(f"{rel}: missing H1")
        if "days days" in body.lower():
            errors.append(f"{rel}: rendered duplicated phrase 'days days'")
        for block in parser.jsonld_blocks:
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD ({exc.msg})")

        for href in set(parser.links):
            target = target_path(href)
            if target is None or target.name == "submit.php":
                continue
            exists = target_cache.setdefault(target, target.exists())
            if not exists:
                samples = broken_targets.setdefault(href, [])
                if len(samples) < 3:
                    samples.append(str(rel))

        if index % 1000 == 0:
            print(f"  checked {index}/{len(html_files)}", flush=True)

    route_index = PUBLIC / "pet-transport" / "routes" / "index.html"
    if route_index.exists() and route_index.stat().st_size > 500_000:
        errors.append(f"route directory is still {route_index.stat().st_size / 1024:.0f} KiB (limit 488 KiB)")

    sitemap = PUBLIC / "sitemap.xml"
    try:
        root = ET.parse(sitemap).getroot()
        if not root.tag.endswith("sitemapindex"):
            errors.append("sitemap.xml is not a sitemap index")
    except (ET.ParseError, FileNotFoundError) as exc:
        errors.append(f"invalid sitemap.xml: {exc}")

    for href, samples in sorted(broken_targets.items()):
        errors.append(f"broken internal target {href} (seen on {', '.join(samples)})")

    print(f"Rendered audit: {len(html_files)} HTML pages; {len(warnings)} metadata warning(s)")
    for message in warnings[:30]:
        print(f"WARNING: {message}")
    if len(warnings) > 30:
        print(f"WARNING: ... {len(warnings) - 30} more metadata warnings")
    if errors:
        print(f"ERROR: {len(errors)} rendered-site issue(s)", file=sys.stderr)
        for message in errors[:200]:
            print(f"  - {message}", file=sys.stderr)
        if len(errors) > 200:
            print(f"  ... {len(errors) - 200} more", file=sys.stderr)
        return 1
    print("Rendered-site audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
