"""Add author attribution to all content files missing it."""
import os
import re

dirs = [
    "site/content/routes",
    "site/content/countries",
    "site/content/origins",
    "site/content/airlines",
    "site/content/breeds",
    "site/content/blog",
]

AUTHOR_LINE = 'author: "Gareth - Founder, PetTransportGlobal"\n'

fixed = 0
for d in dirs:
    for fname in os.listdir(d):
        if not fname.endswith(".md") or fname == "_index.md":
            continue
        path = os.path.join(d, fname)
        content = open(path, encoding="utf-8").read()
        if "author:" in content:
            continue
        new_content = re.sub(
            r'(layout: "single"\n)',
            r"\1" + AUTHOR_LINE,
            content,
            count=1,
        )
        if new_content == content:
            new_content = re.sub(
                r'(type: "[^"]+"\n)',
                r"\1" + AUTHOR_LINE,
                content,
                count=1,
            )
        if new_content != content:
            open(path, "w", encoding="utf-8").write(new_content)
            fixed += 1

print(f"Added author to {fixed} files")
