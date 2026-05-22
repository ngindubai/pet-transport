"""
fix_long_titles.py
Fixes titles that are too long per Semrush audit.
Target: title + " | Pet Transport Global" (23 chars) <= 65 chars
So title field itself must be <= 42 chars.
"""
import re
import os
import csv

BRAND = " | Pet Transport Global"
BRAND_ALT = " | PetTransportGlobal"
MAX_TOTAL = 65
MAX_TITLE = MAX_TOTAL - len(BRAND)  # 42 chars

# Pages flagged from CSVs - collect unique slugs
FLAGGED_URLS = set()
csv_path = r"C:\Users\garet\Downloads\pettransportglobal.com_title_element_is_too_long_20260511.csv"
with open(csv_path, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        url = row["Page URL"].rstrip("/").replace("https://www.pettransportglobal.com","").replace("https://pettransportglobal.com","")
        FLAGGED_URLS.add(url)

CONTENT_BASE = r"c:\Users\garet\Desktop\pet-transport\site\content"

def shorten_title(title, max_len=MAX_TITLE):
    """Shorten title to max_len chars at a natural break point."""
    if len(title) <= max_len:
        return title
    # Remove brand suffix if present
    for suffix in [" | Pet Transport Global", " | PetTransportGlobal"]:
        if title.endswith(suffix):
            title = title[:-len(suffix)].rstrip()
    if len(title) <= max_len:
        return title
    # Try to cut at natural break points: colon, pipe, comma, dash
    candidates = []
    for sep in [":", "|", ",", " -", " –"]:
        pos = title.rfind(sep, 0, max_len + 1)
        if pos > 10:  # don't cut too early
            candidates.append(title[:pos].strip())
    if candidates:
        # Pick longest that's within max_len
        valid = [c for c in candidates if len(c) <= max_len]
        if valid:
            return max(valid, key=len)
    # Fallback: cut at last word boundary within max_len
    truncated = title[:max_len]
    last_space = truncated.rfind(" ")
    if last_space > 10:
        return truncated[:last_space].strip()
    return truncated.strip()

def url_to_file(url):
    """Convert URL path to content file path."""
    url = url.strip("/")
    parts = url.split("/")
    
    # blog/ -> content/blog/
    if parts[0] == "blog":
        slug = parts[1] if len(parts) > 1 else None
        if slug:
            return os.path.join(CONTENT_BASE, "blog", f"{slug}.md")
    
    # pet-transport/countries/X -> content/countries/X.md
    if len(parts) >= 3 and parts[0] == "pet-transport" and parts[1] == "countries":
        slug = parts[2]
        return os.path.join(CONTENT_BASE, "countries", f"{slug}.md")
    
    # pet-transport/airlines/X -> content/airlines/X.md
    if len(parts) >= 3 and parts[0] == "pet-transport" and parts[1] == "airlines":
        slug = parts[2]
        return os.path.join(CONTENT_BASE, "airlines", f"{slug}.md")
    
    # pet-transport/breeds/X -> content/breeds/X.md
    if len(parts) >= 3 and parts[0] == "pet-transport" and parts[1] == "breeds":
        slug = parts[2]
        return os.path.join(CONTENT_BASE, "breeds", f"{slug}.md")
    
    # contact/ -> content/contact.md or similar
    if parts[0] == "contact":
        return os.path.join(CONTENT_BASE, "contact", "_index.md")
    
    return None

def update_title_in_file(filepath, new_title):
    """Update the title: field in a markdown front matter file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match title: "..." in front matter (between --- delimiters)
    fm_match = re.match(r'^(---\n)(.*?)\n(---)', content, re.DOTALL)
    if not fm_match:
        return False, "No front matter found"
    
    fm = fm_match.group(2)
    # Update title field
    new_fm = re.sub(
        r'^(title:\s*)"[^"]*"',
        f'\\1"{new_title}"',
        fm,
        flags=re.MULTILINE
    )
    if new_fm == fm:
        return False, "Title field not found or unchanged"
    
    new_content = content.replace(fm_match.group(2), new_fm, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True, "Updated"

def update_seo_title_in_file(filepath, new_seo_title=None):
    """Remove or shorten seo.title in front matter."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "seo:" not in content and "seo.title" not in content:
        return False, "No seo section"
    
    if new_seo_title is None:
        # Remove the seo: block entirely (or just the title line)
        # Find and remove seo.title line
        new_content = re.sub(
            r'(\n  title:\s*"[^"]*")',
            '',
            content
        )
        # If seo: block is now empty, remove it
        new_content = re.sub(
            r'\nseo:\s*\n(?=\S)',
            '\n',
            new_content
        )
    else:
        new_content = re.sub(
            r'(seo:\s*\n\s*title:\s*)"[^"]*"',
            f'\\1"{new_seo_title}"',
            content
        )
    
    if new_content == content:
        return False, "No change"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True, "Updated"

# Process all flagged URLs
updated = 0
skipped = 0
not_found = 0
errors = []

# Also read the actual titles from the CSV for accurate processing
url_titles = {}
with open(csv_path, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        url = row["Page URL"].rstrip("/").replace("https://www.pettransportglobal.com","").replace("https://pettransportglobal.com","")
        url_titles[url] = row["Title"]

processed_files = set()

for url, full_title in url_titles.items():
    filepath = url_to_file(url)
    if not filepath:
        skipped += 1
        continue
    
    if not os.path.exists(filepath):
        not_found += 1
        errors.append(f"NOT FOUND: {filepath}")
        continue
    
    # Skip if already processed (www. duplicates)
    if filepath in processed_files:
        continue
    processed_files.add(filepath)
    
    # The full_title includes brand. Extract the base title part
    base_title = full_title
    for suffix in [" | Pet Transport Global", " | PetTransportGlobal"]:
        if base_title.endswith(suffix):
            base_title = base_title[:-len(suffix)].rstrip()
    
    total_len = len(base_title) + len(BRAND)
    if total_len <= MAX_TOTAL:
        skipped += 1
        continue
    
    # Shorten the base title
    short_title = shorten_title(base_title)
    
    # For blog/default pages: update title: field in front matter
    # For countries/airlines with seo.title: update seo.title
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    has_seo_title = re.search(r'^seo:\s*$', content, re.MULTILINE) and 'title:' in content[content.find('seo:'):]
    
    if has_seo_title:
        # Update the seo.title to shorter version + brand
        new_seo_title = short_title + BRAND
        ok, msg = update_seo_title_in_file(filepath, new_seo_title)
    else:
        # Update the main title: field
        ok, msg = update_title_in_file(filepath, short_title)
    
    if ok:
        print(f"UPDATED: {url}")
        print(f"  '{base_title}' ({len(base_title)} chars)")
        print(f"  -> '{short_title}' ({len(short_title)} chars)")
        updated += 1
    else:
        errors.append(f"FAILED {url}: {msg}")

print(f"\n=== SUMMARY ===")
print(f"Updated: {updated}")
print(f"Skipped (OK length or www. dup): {skipped}")
print(f"Not found: {not_found}")
print(f"Errors: {len(errors)}")
if errors:
    print("\nErrors:")
    for e in errors[:20]:
        print(f"  {e}")
