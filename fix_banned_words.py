"""
Fix banned vocabulary across all content files.
Run this as a one-off fix script.
"""
import os, re

fixes = 0

# ── Routes: "navigate" in boilerplate sentence ──────────────────────────────
routes_dir = r"c:\Users\garet\Desktop\pet-transport\site\content\routes"
for fn in os.listdir(routes_dir):
    if not fn.endswith(".md"):
        continue
    path = os.path.join(routes_dir, fn)
    content = open(path, encoding="utf-8").read()
    changed = False

    # "navigate each year" → "travel each year" 
    if re.search(r"\bnavigate\b", content, re.I):
        content = re.sub(
            r"\bnavigate\b",
            "complete",
            content,
            flags=re.I,
        )
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        fixes += 1

print(f"Routes fixed: {fixes}")

# ── Denmark: "crucial" → "important" ────────────────────────────────────────
denmark_path = r"c:\Users\garet\Desktop\pet-transport\site\content\countries\denmark.md"
content = open(denmark_path, encoding="utf-8").read()
content = re.sub(r"\bcrucial\b", "important", content, flags=re.I)
with open(denmark_path, "w", encoding="utf-8") as f:
    f.write(content)
print("denmark.md: 'crucial' fixed")

# ── Indonesia: "navigating" → "working through" ──────────────────────────────
indonesia_path = r"c:\Users\garet\Desktop\pet-transport\site\content\countries\indonesia.md"
content = open(indonesia_path, encoding="utf-8").read()
content = re.sub(r"\bnavigating\b", "working through", content, flags=re.I)
with open(indonesia_path, "w", encoding="utf-8") as f:
    f.write(content)
print("indonesia.md: 'navigating' fixed")

# ── Blog: "landscape" → "options" in airline blog post ───────────────────────
blog_path = r"c:\Users\garet\Desktop\pet-transport\site\content\blog\flying-with-a-french-bulldog-what-airlines-accept.md"
content = open(blog_path, encoding="utf-8").read()
# Replace "airline landscape" specifically
content = content.replace("airline landscape", "airline options")
# Also catch any other "landscape" usage
content = re.sub(r"\blandscape\b", "picture", content, flags=re.I)
with open(blog_path, "w", encoding="utf-8") as f:
    f.write(content)
print("flying-with-a-french-bulldog: 'landscape' fixed")

print("\nAll banned word fixes complete.")
