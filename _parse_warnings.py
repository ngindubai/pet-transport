import re, collections
report = open('qa-audit-report.html', encoding='utf-8').read()

issues = re.findall(r'class="issue">(.*?)</div>', report, re.DOTALL)
cleaned = []
for i in issues:
    text = re.sub(r'<[^>]+>', ' ', i).strip()
    text = re.sub(r'\s+', ' ', text)
    cleaned.append(text[:150])

counter = collections.Counter(cleaned)
print(f'Total issue instances: {len(cleaned)}')
print(f'Distinct messages: {len(counter)}')
print()
for msg, cnt in counter.most_common(30):
    print(f'  {cnt:>5}  {msg}')
