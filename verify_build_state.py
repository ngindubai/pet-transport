#!/usr/bin/env python3
"""
verify_build_state.py - reconcile build_state.json against the actual repo.

Why this exists: the route count in build_state.json used to be a running tally
that was hand-incremented per build chunk and never recounted from disk. It
drifted from reality (claimed 5,544 when 5,172 route pages existed). This script
makes the filesystem the single source of truth.

Usage:
  python verify_build_state.py          Count from disk, compare to build_state.json,
                                         print a table, exit 1 on any mismatch.
  python verify_build_state.py --write   Recount from disk and rewrite the count
                                         fields in build_state.json. Use this to
                                         reconcile after a build. Never hand-edit counts.

Run this at the start of every session (a SessionStart hook does this automatically)
and after every build batch.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
CONTENT = REPO_ROOT / "site" / "content"
STATE_FILE = REPO_ROOT / "build_state.json"

# Total country-pair universe the route build is working towards.
# Source: CLAUDE.md ("~37,830 country pairs"). routes_remaining is derived from this.
TARGET_ROUTE_PAIRS = 37830

# Files in a route directory that are not themselves route pages.
NON_ROUTE_FILES = {"_index.md", "how-we-source-route-data.md"}


def count_md(directory: Path, exclude: set[str]) -> int:
    """Count .md files in a directory tree, excluding given filenames."""
    if not directory.is_dir():
        return 0
    return sum(
        1
        for p in directory.rglob("*.md")
        if p.name not in exclude
    )


def count_disk() -> dict:
    """Recompute every tracked count straight from site/content."""
    routes = count_md(CONTENT / "routes", {"_index.md"})
    pet_transport_routes = count_md(CONTENT / "pet-transport", NON_ROUTE_FILES)
    route_pairs = routes + pet_transport_routes

    blog = count_md(CONTENT / "blog", {"_index.md"})
    countries = count_md(CONTENT / "countries", {"_index.md"})
    origins = count_md(CONTENT / "origins", {"_index.md"})
    airlines = count_md(CONTENT / "airlines", {"_index.md"})
    breeds = count_md(CONTENT / "breeds", {"_index.md"})

    # Top-level static pages (home, about, contact, privacy, terms, thank-you).
    static_pages = sum(1 for p in CONTENT.glob("*.md"))

    total_markdown_files = sum(1 for p in CONTENT.rglob("*.md"))

    return {
        "route_pairs": route_pairs,
        "routes_in_routes_dir": routes,
        "routes_in_pet_transport_dir": pet_transport_routes,
        "blog": blog,
        "countries": countries,
        "origins": origins,
        "airlines": airlines,
        "breeds": breeds,
        "static_pages": static_pages,
        "total_markdown_files": total_markdown_files,
    }


def load_state() -> dict:
    with open(STATE_FILE, encoding="utf-8") as f:
        return json.load(f)


def apply_counts(state: dict, disk: dict) -> dict:
    """Write disk-derived counts into the state dict, preserving key order."""
    state["routes_built"] = disk["route_pairs"]
    state["routes_remaining"] = TARGET_ROUTE_PAIRS - disk["route_pairs"]
    state["blog_articles"] = disk["blog"]
    state["total_site_pages"] = disk["total_markdown_files"]
    state["counts"] = {
        "route_pairs": disk["route_pairs"],
        "blog": disk["blog"],
        "countries": disk["countries"],
        "origins": disk["origins"],
        "airlines": disk["airlines"],
        "breeds": disk["breeds"],
        "static_pages": disk["static_pages"],
        "total_markdown_files": disk["total_markdown_files"],
        "note": "total_site_pages counts content .md source files. The full deployed total (including Hugo taxonomy and list pages) is verified from sitemap.xml after a build.",
    }
    state["counts_method"] = "Reconciled from disk by verify_build_state.py. Never hand-edit count fields; run 'python verify_build_state.py --write' instead."
    return state


def check(state: dict, disk: dict) -> list[str]:
    """Return a list of human-readable mismatches between state and disk."""
    problems = []
    expected = {
        "routes_built": disk["route_pairs"],
        "blog_articles": disk["blog"],
        "total_site_pages": disk["total_markdown_files"],
    }
    for key, want in expected.items():
        have = state.get(key)
        if have != want:
            problems.append(f"  {key}: build_state.json says {have}, disk has {want}")
    return problems


def print_table(disk: dict) -> None:
    rows = [
        ("Route pairs", disk["route_pairs"]),
        ("  in routes/", disk["routes_in_routes_dir"]),
        ("  in pet-transport/", disk["routes_in_pet_transport_dir"]),
        ("Blog articles", disk["blog"]),
        ("Country guides", disk["countries"]),
        ("Origin hubs", disk["origins"]),
        ("Airline pages", disk["airlines"]),
        ("Breed guides", disk["breeds"]),
        ("Static pages", disk["static_pages"]),
        ("Total .md source files", disk["total_markdown_files"]),
    ]
    print("Repo content audit (counted from site/content):")
    for label, value in rows:
        print(f"  {label:<26} {value}")


def main() -> int:
    write = "--write" in sys.argv[1:]
    disk = count_disk()
    print_table(disk)

    state = load_state()

    if write:
        state = apply_counts(state, disk)
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print("\nbuild_state.json reconciled from disk.")
        return 0

    problems = check(state, disk)
    if problems:
        print("\nDRIFT DETECTED: build_state.json does not match disk:")
        print("\n".join(problems))
        print("\nFix with: python verify_build_state.py --write")
        return 1

    print("\nbuild_state.json matches disk. No drift.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
