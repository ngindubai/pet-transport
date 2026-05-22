content = open(r"cascading-build-plan-pet=transport.html", encoding="utf-8").read()
idx = content.find('id="phase-3"')
print(content[idx:idx+5000])
