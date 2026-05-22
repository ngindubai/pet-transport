content = open("site-health-report.html", encoding="utf-8").read()
import re
rows = re.findall(r'<tr>\s*<td><span[^>]*>(P\d)</span></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>', content, re.DOTALL)
for sev, cat, msg, url in rows:
    print(f"[{sev}] {cat}: {msg.strip()} | {url.strip()[:80]}")
