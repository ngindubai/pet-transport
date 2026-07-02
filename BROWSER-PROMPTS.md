# Browser prompts for the manual work (Claude in Chrome)

These are the parts of the SEO plan I cannot do headless: they need Google Search
Console, the official authority sites, or the live site in a browser. Each block
below is a self-contained prompt. Open Claude in Chrome, paste one prompt, and let
it work. None of them change anything without telling you first.

Important: most of the site changes from this session are on the branch
`claude/pet-transport-seo-audit-4j2yot` and are NOT live until that branch is
merged to `main` (which triggers the automatic deploy). Prompt 4 only applies
after the merge and redeploy.

---

## Prompt 1: Set up Search Console and submit the sitemap

Do this first. Without it there is no ranking data, and prompts 2 and 4 need it.

```
Open Google Search Console at search.google.com/search-console. Check whether
pettransportglobal.com is added and verified as a property. If it is not, walk me
through verifying it with the HTML tag method and give me the exact meta
verification code, because I need to paste it into the site config
(params.googleSearchConsole in hugo.toml). Once the property is verified, submit
the sitemap at https://pettransportglobal.com/sitemap.xml. Then report: the
verification status, the total indexed page count, and any coverage or indexing
errors you see. Do not change any Search Console setting without telling me first.
```

---

## Prompt 2: Find the long-tail routes worth a better title (A10)

Run this after Prompt 1, once Search Console has a few weeks of data.

```
In Google Search Console for pettransportglobal.com, open Performance then Search
results. Set the date range to the last 3 months. Add a page filter for URLs
containing /pet-transport/ so we only see route pages. Sort by impressions,
highest first. Give me the top 40 route pages that have a lot of impressions but a
low click-through rate (under 2 percent) and an average position between 5 and 20.
For each one list: the page URL, its top query, impressions, CTR and average
position. These are the routes where a sharper title and meta description would
win clicks. Do not change anything. Just give me the list so I can hand-tune those
titles in the repo.
```

---

## Prompt 3: Quarterly regulatory re-check (A9)

First run `python3 refresh_audit.py --write` in the repo to get
`refresh-worklist.md`, then use its top rows to fill in the countries and source
URLs below. Repeat for each destination on the worklist.

```
I am doing a quarterly check of pet import rules for my website. For the country
[COUNTRY NAME], open the official source [AUTHORITY URL from the worklist, for
example gov.uk/bring-pet-to-great-britain]. Read the current rules for bringing a
dog and a cat into [COUNTRY NAME]. Then open the matching page on my site at
https://pettransportglobal.com/pet-transport/countries/[country-slug]/ and compare
the two. Go point by point and tell me, for each, whether they MATCH or DIFFER:
microchip rule, rabies vaccination, rabies titre test (required or not, and for
which origin countries), quarantine (none, or the number of days), health
certificate type and how many days it stays valid, and any breed restrictions or
bans. List only the points that DIFFER, showing the official value next to what my
site currently says. Do not change anything on the site. When you are done with
this country, tell me the country is checked so I can give you the next one.
```

Tip: give it the top three to five destinations from the worklist in one session,
one at a time. The stalest, highest-volume destinations are at the top of the list.

---

## Prompt 4: Verify this session's changes are live (after the merge)

Run this only after the branch `claude/pet-transport-seo-audit-4j2yot` is merged to
`main` and the site has redeployed.

```
Please verify some SEO changes are live and correct on pettransportglobal.com.

1. Search: open https://pettransportglobal.com/search/ , type "UK to Spain" and
   confirm relevant route results appear. Try "emirates" and "australia" as well.
   Then open the home page and confirm there is a working search box in the header.

2. Answer box: open https://pettransportglobal.com/pet-transport/germany-to-australia/
   and confirm that near the top there is an "In short" box that says about 10 days
   of quarantine and mentions the rabies titre test, and that there is a byline
   naming a specialist (Marcus Webb or similar), not "Gareth".

3. Quarantine accuracy: on that same Germany to Australia page, confirm the hero
   stat for quarantine shows a number of days (not "None"). Then open
   https://pettransportglobal.com/pet-transport/japan-to-united-kingdom/ and confirm
   its quarantine shows "None".

4. Structured data: paste the Germany to Australia URL into Google's Rich Results
   Test at search.google.com/test/rich-results. Confirm it detects FAQ and How-to,
   and that the question and answer text is clean with no stray backslashes or
   doubled quotation marks.

5. Duplicate content: open three different routes to the same country, for example
   https://pettransportglobal.com/pet-transport/armenia-to-austria/ ,
   https://pettransportglobal.com/pet-transport/oman-to-austria/ and
   https://pettransportglobal.com/pet-transport/georgia-to-austria/ . Confirm their
   overview and advice paragraphs read differently from each other.

6. llms.txt: open https://pettransportglobal.com/llms.txt and confirm it loads,
   names our specialists rather than Gareth, and that the links work.

Report what passed and anything that failed, with the URL for each failure.
```

---

## One extra, optional: fix the broken origin nav links

Not part of the SEO plan, but flagged during the work. The header menu links to
origin pages like
`/pet-transport/origins/pet-export-guide-shipping-from-united-kingdom/`, but the
real page is at `/pet-transport/origins/united-kingdom/`, so those menu links
likely 404.

```
Open https://pettransportglobal.com and hover the Routes menu. Click each "From the
UK / USA / Australia / UAE" link under "Browse by Region" and tell me which ones
load a real page and which ones 404. For any that 404, find the correct live URL by
opening https://pettransportglobal.com/pet-transport/origins/ and matching the
country. Give me the list of broken menu links and the correct URL for each, so I
can fix the header in the repo.
```
