"""
assign_template_variants.py
---------------------------
Assigns template_variant front matter to non-US/non-UK route pages
in a deterministic round-robin rotation (A → B → C → D → E).

Rules:
- Routes FROM or TO united-states / united-kingdom → SKIP (stay legacy)
- Routes already containing template_variant → SKIP (idempotent)
- All other routes → assign variant by sorted position % 5
- Test routes (argentina-to-australia etc.) already assigned → SKIP

Usage:
    python assign_template_variants.py --batch 1          # process batch 1 (routes 1-50)
    python assign_template_variants.py --batch 2          # process batch 2 (routes 51-100)
    python assign_template_variants.py --batch 1 --size 50    # explicit size
    python assign_template_variants.py --dry-run --batch 1    # preview without writing
    python assign_template_variants.py --status               # show overall progress
"""

import os
import re
import argparse
import pathlib

ROUTES_DIR = pathlib.Path(__file__).parent / "site" / "content" / "routes"
VARIANTS = ["A", "B", "C", "D", "E"]
BATCH_SIZE_DEFAULT = 50
PROGRESS_FILE = pathlib.Path(__file__).parent / "assign_variants_progress.txt"


def read_progress() -> int:
    """Return last completed batch number (0 = none done)."""
    if PROGRESS_FILE.exists():
        try:
            return int(PROGRESS_FILE.read_text().strip())
        except ValueError:
            pass
    return 0


def write_progress(batch_num: int):
    PROGRESS_FILE.write_text(str(batch_num))

# Patterns for US/UK routes (origin OR destination)
US_UK_PATTERNS = re.compile(
    r"^(united-states-to-|united-kingdom-to-)|(-to-united-states\.md$|-to-united-kingdom\.md$)"
)

TEMPLATE_VARIANT_RE = re.compile(r"^template_variant\s*:", re.MULTILINE)


def get_eligible_routes():
    """Return sorted list of all eligible route paths (not US/UK, full path)."""
    all_files = sorted(ROUTES_DIR.glob("*.md"), key=lambda p: p.name)
    eligible = [
        f for f in all_files
        if not US_UK_PATTERNS.search(f.name)
        and not f.name.startswith("_")  # exclude _index.md and similar
    ]
    return eligible


def already_assigned(path: pathlib.Path) -> bool:
    """Check if file already has template_variant in front matter."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            # Only read the first 25 lines (front matter)
            head = "".join(f.readline() for _ in range(25))
        return bool(TEMPLATE_VARIANT_RE.search(head))
    except Exception:
        return False


def inject_variant(path: pathlib.Path, variant: str, dry_run: bool = False) -> bool:
    """
    Inject `template_variant: "X"` into the YAML front matter.
    Inserts after the opening `---` line.
    Returns True if file was modified.
    """
    if already_assigned(path):
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the opening --- and the second --- (end of front matter)
    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        print(f"  SKIP (no front matter): {path.name}")
        return False

    # Insert template_variant as the second line (after opening ---)
    lines.insert(1, f'template_variant: "{variant}"')
    new_content = "\n".join(lines)

    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True


def run_batch(batch_num: int, batch_size: int, dry_run: bool = False):
    eligible = get_eligible_routes()
    total_eligible = len(eligible)

    # Slice for this batch (0-indexed internally)
    start = (batch_num - 1) * batch_size
    end = start + batch_size
    batch = eligible[start:end]

    if not batch:
        print(f"Batch {batch_num} is empty — all routes have been processed!")
        return

    total_batches = (total_eligible + batch_size - 1) // batch_size
    print(f"\n{'DRY RUN — ' if dry_run else ''}Batch {batch_num}/{total_batches}")
    print(f"Routes {start + 1}–{min(end, total_eligible)} of {total_eligible} eligible")
    print(f"Routes dir: {ROUTES_DIR}")
    print("-" * 60)

    assigned_count = 0
    skipped_count = 0

    for i, path in enumerate(batch):
        global_position = start + i
        variant = VARIANTS[global_position % len(VARIANTS)]

        if already_assigned(path):
            skipped_count += 1
            print(f"  SKIP (has variant): {path.name}")
            continue

        modified = inject_variant(path, variant, dry_run=dry_run)
        if modified:
            assigned_count += 1
            action = "PREVIEW" if dry_run else "ASSIGNED"
            print(f"  {action} [{variant}]: {path.name}")

    print("-" * 60)
    print(f"  Assigned : {assigned_count}")
    print(f"  Skipped  : {skipped_count}")
    print(f"  Total    : {len(batch)}")

    if not dry_run and assigned_count > 0:
        write_progress(batch_num)
        next_batch = batch_num + 1
        next_start = end + 1
        if next_start <= total_eligible:
            print(f"\nNext: run batch {next_batch} (routes {end + 1}–{min(end + batch_size, total_eligible)})")
        else:
            print("\nAll batches complete!")
    elif dry_run:
        print("\nDry run complete — no files written.")


def show_status(batch_size: int):
    eligible = get_eligible_routes()
    total = len(eligible)
    done = sum(1 for p in eligible if already_assigned(p))
    remaining = total - done
    total_batches = (total + batch_size - 1) // batch_size
    last_completed = read_progress()
    next_batch = last_completed + 1

    print(f"\nTemplate Variant Assignment Status")
    print(f"{'=' * 40}")
    print(f"  Eligible routes    : {total}")
    print(f"  Already assigned   : {done}")
    print(f"  Remaining          : {remaining}")
    print(f"  Batch size         : {batch_size}")
    print(f"  Total batches      : {total_batches}")
    print(f"  Last batch done    : {last_completed if last_completed > 0 else 'none'}")
    print(f"  Next batch to run  : {next_batch}")
    print(f"  Progress           : {done/total*100:.1f}%")

    # Show variant distribution
    dist = {v: 0 for v in VARIANTS}
    for path in eligible:
        if already_assigned(path):
            with open(path, "r", encoding="utf-8") as f:
                head = "".join(f.readline() for _ in range(25))
            m = re.search(r'template_variant:\s*["\']?([A-E])["\']?', head)
            if m:
                dist[m.group(1)] += 1
    print(f"\n  Variant distribution:")
    for v, count in dist.items():
        print(f"    {v}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assign template variants to route pages")
    parser.add_argument("--batch", type=int, default=1, help="Batch number to process (1-based)")
    parser.add_argument("--size", type=int, default=BATCH_SIZE_DEFAULT, help="Routes per batch")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--status", action="store_true", help="Show overall progress and exit")
    args = parser.parse_args()

    if args.status:
        show_status(args.size)
    else:
        run_batch(args.batch, args.size, dry_run=args.dry_run)
