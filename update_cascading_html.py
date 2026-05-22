"""Update cascading-build-plan HTML: mark Tasks 2.10 and 2.11 DONE, add session log row."""
from pathlib import Path
from datetime import date

content = Path("cascading-build-plan-pet=transport.html").read_text(encoding="utf-8")

# Mark Task 2.10 DONE
content = content.replace(
    ">3.1</td><td>Country data for P3 countries",  # don't touch phase 3
    ">3.1</td><td>Country data for P3 countries"   # unchanged
)

# Mark 2.10 - find and update status badge
# The HTML has task rows; we mark 2.10 and 2.11 DONE
# Pattern: <td>2.10</td><td>Set up site health monitoring
old_2_10 = '<td>2.10</td><td>Set up site health monitoring'
new_2_10 = '<td>2.10 <span style="color:var(--green);font-size:0.8em;">&#10003; DONE 2026-04-23</span></td><td>Set up site health monitoring'

old_2_11 = '<td><strong>2.11</strong></td><td><strong>Phase 2 Gate Review'
new_2_11 = '<td><strong>2.11 <span style="color:var(--green);font-size:0.8em;">&#10003; DONE 2026-04-23</span></strong></td><td><strong>Phase 2 Gate Review'

if old_2_10 in content:
    content = content.replace(old_2_10, new_2_10)
    print("Marked 2.10 DONE")
else:
    print("WARNING: could not find 2.10 row — check HTML manually")

if old_2_11 in content:
    content = content.replace(old_2_11, new_2_11)
    print("Marked 2.11 DONE")
else:
    print("WARNING: could not find 2.11 row — check HTML manually")

# Add session log row
session_row = """
      <tr>
        <td>2026-04-23</td>
        <td>Block 29 + Task 2.10 + Task 2.11</td>
        <td>Site health monitor created (HEALTHY: P0=0, P1=0, P2=0). Fixed 393 broken origin hub links (short-slug → full-slug via fix_origin_links.py). Fixed schema on origins template + blog template. Phase 2 Gate Review PASS — Review #2 appended to google-deployment-strategy.html. Phase 2 complete. Phase 3 cleared.</td>
        <td>539</td>
        <td>Next: Phase 3 / Task 3.1 — P3 country data</td>
      </tr>"""

# Find session log table and insert before closing </tbody>
log_marker = "</tbody>\n    </table>\n  </section>"
if log_marker in content:
    content = content.replace(log_marker, session_row + "\n" + log_marker, 1)
    print("Session log row added")
else:
    # try alternate
    alt = "</tbody>\n</table>"
    if alt in content:
        content = content.replace(alt, session_row + "\n" + alt, 1)
        print("Session log row added (alt pattern)")
    else:
        print("WARNING: could not find session log table end")

Path("cascading-build-plan-pet=transport.html").write_text(content, encoding="utf-8")
print("Done.")
