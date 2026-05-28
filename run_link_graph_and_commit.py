#!/usr/bin/env python3
"""
run_link_graph_and_commit.py
============================
One-time script to retroactively fix all origin hub and country guide files
with the complete internal link graph from the live route set.

Run from repo root:
    python run_link_graph_and_commit.py

This will:
  1. Run rebuild_link_graph_v3.py to update all source files
  2. Git add + commit + push the changes
  3. GitHub Actions will then deploy the updated site

Requires: git configured with push access to origin/main
"""

import subprocess, sys, os

def run(cmd, check=True):
    print(f"  $ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    if check and result.returncode != 0:
        print(f"ERROR: command failed with exit code {result.returncode}")
        sys.exit(1)
    return result

print("=" * 60)
print("Link graph rebuild + commit + push")
print("=" * 60)

# Step 1: Run the rebuild
print("\n[1/3] Running rebuild_link_graph_v3.py...")
run("python rebuild_link_graph_v3.py")

# Step 2: Check what changed
print("\n[2/3] Checking changes...")
result = run("git diff --stat site/content/origins/ site/content/countries/", check=False)
changed = result.stdout.strip()
if not changed:
    print("  No files changed — link graph is already up to date.")
    sys.exit(0)

# Step 3: Commit and push
print("\n[3/3] Committing and pushing...")
run("git add site/content/origins/ site/content/countries/")
run('git commit -m "chore: rebuild link graph — all origin hubs and country guides updated\n\nRetroactive fix: runs rebuild_link_graph_v3.py to update Popular routes\nsections in all 77 origin hub files and routes_incoming YAML in all\n75 country guides to reflect the complete set of 5,152 live route pages.\n\nFixes crawl budget issue causing ~1,873 pages to remain unindexed."')
run("git push origin main")

print("\n" + "=" * 60)
print("Done. GitHub Actions will now deploy the updated site.")
print("Monitor: https://github.com/ngindubai/pet-transport/actions")
print("=" * 60)
