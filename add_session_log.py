content = open(r"c:\Users\garet\Desktop\pet-transport\cascading-build-plan-pet=transport.html", encoding="utf-8").read()
idx = content.find("Block 27 / Task 2.8")
row_end = content.find("</tr>", idx) + 5
before = content[:row_end]
after = content[row_end:]
new_row = (
    "\n        <tr><td>2026-04-23</td>"
    "<td>Block 28 / Task 2.9 - Full QA + Regulatory Audit</td>"
    "<td>Wrote qa_audit_p2.py. Audited 518 pages. "
    "Fixed: 397 files em dashes, 35 routes banned word 'navigate', 15 US routes CDC FAQ added, "
    "11 route titles shortened (UAE), 4 breed + 1 blog title shortened, "
    "11 origin descriptions expanded (90-98 to 140-155 chars), 6 other desc fixes, "
    "NZ + Spain: 4th FAQ (breed bans), KLM links corrected to klm-royal-dutch-airlines (20 files), "
    "Air India broken links removed (20 files), Spain-UK broken sideways link removed. "
    "Final audit: 518/518 CLEAN. 0 errors, 0 warnings. 539 pages deployed.</td>"
    "<td>539</td>"
    '<td><span class="badge b-green">DONE 2026-04-23</span></td></tr>'
)
new_content = before + new_row + after
open(r"c:\Users\garet\Desktop\pet-transport\cascading-build-plan-pet=transport.html", "w", encoding="utf-8").write(new_content)
print("Session log row added")
