#!/bin/bash
# SessionStart hook for PetTransportGlobal.
# Anti-drift guard: verifies build_state.json against the actual repo at the
# start of every session, so the count fields can never silently drift again.
# Read-only and fast (stdlib Python only). Always exits 0 so it never blocks
# the session; drift is surfaced loudly in the output instead.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

echo "PetTransportGlobal: verifying build_state.json against disk (verify_build_state.py)"
python3 verify_build_state.py || echo "NOTE: counts have drifted from disk. Reconcile with: python verify_build_state.py --write"

exit 0
