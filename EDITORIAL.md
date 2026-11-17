# Shiva Exim Market Insights

The owner requested two blog posts per month on 12 October 2026. As updated on 15 November 2026, prepare a review brief and concrete draft before publishing each new article; publish only after Savan explicitly approves that individual article. Earlier article approval never approves a new article. The monthly target does not override approval. October's two articles were published together at launch. Future runs publish one original article per occurrence, with at most two new posts in each calendar month in Asia/Kolkata. Preserve the public audience, company branding and the existing project identity.

## Editorial policy

- Alternate a sourced market update with a practical buyer guide. Prioritize cumin, fennel and sesame; include alfalfa in useful buyer guides.
- Market-origin coverage: sesame — India, Brazil, Pakistan; cumin — India, Egypt, China; fennel — India, Egypt. Do not imply these are the only origins globally.
- Retrieve current evidence before writing a market update. Prefer IMD, agriculture departments, DASD/Spices Board, customs statistics and direct industry-association reports. Supplier statements and industry projections require attribution. Older datasets retain their actual crop year; export volume is not production.
- Company view supplied 12 October 2026: weaker rainfall in Gujarat/Rajasthan may reduce 2027 cumin, fennel and sesame production. This is a provisional opinion, not a confirmed forecast or a fresh field observation. Reassess against district rainfall, irrigation, acreage, harvest and carryover evidence. Do not repeat the opinion as an established fact.
- Distinguish dated evidence, industry forecasts, company opinion and editorial inference. State data gaps honestly. Do not invent country crop tonnage, percentage changes, prices or documents.
- Any price must include its observation date, grade, origin/location, currency/unit and shipment/cost basis. User-supplied old offers are not live prices.
- Buyer guides use company-confirmed facts and the published product guides. The 99% Europe/Singapore cumin/fennel labels are commercial labels, not certification or blanket destination compliance. Confirm grade definitions and testing per lot. Do not turn specification enquiry questions into stock claims.
- Use a named organizational byline (Shiva Exim), publication date, sources and relevant product links. No invented author credentials. Preserve historical posts and dates; use a new unique slug for a new article. Use dateModified only for substantive revisions.
- End with a useful enquiry link. Avoid copied reports, keyword repetition and guaranteed price/ranking predictions. If current evidence is insufficient, publish an original useful buyer guide rather than a fabricated market update; disclose missing market data when relevant.

## Durable publishing route

Since 17 November 2026 the site is hosted on GitHub Pages from the repository `shivaexim12-2607/shivaexim-website` (custom domain shivaexim.com). ChatGPT Sites is no longer used for publishing. No browser session, WordPress login or secret is required.

1. Clone the repository. Inspect insights.py and the existing month/date coverage. If two articles for the target month already exist, do not create duplicates.
2. Append the new post to the END of POSTS in insights.py and add its three key points to ARTICLE_POINTS in review_content.py. render_insights handles the article, index, byline and BlogPosting metadata; build.py includes the paths in sitemap.xml. Do not replace, re-date or reorder prior posts.
3. Run `python build.py`. Validate internal links, canonical URLs, JSON-LD and that sitemap URLs match generated pages. Confirm `git diff --stat` touches only insights.py, review_content.py, the new article page, the insights index, sitemap.xml and pages that list recent articles. Preserve the logo plus SHIVA EXIM; do not restore the removed EXPORT & IMPORT subtitle.
4. Commit source and dist/ together on `main` with message `Market Insights: <title>` and push. The workflow `.github/workflows/deploy-pages.yml` rebuilds, checks dist/ matches the source and deploys to GitHub Pages.
5. Confirm the workflow run succeeded, then confirm https://shivaexim.com/insights/NEW-SLUG/ returns the article and the live sitemap lists it. Only then report publication.
6. If network access allows, run `python submit_indexnow.py https://shivaexim.com/insights/ https://shivaexim.com/insights/NEW-SLUG/`. Report submission failures separately; 200/202 do not guarantee indexing.
7. If source access, the deploy or verification fails, report the blocker; never claim the post is live. Store no private credentials in the repository. The IndexNow key is intentionally served as a public domain-verification file.

The monthly routine was chosen as the 1st and 15th, around 10:00 IST, starting November 2026 because October already has two posts. The linked cloud schedule is authoritative for execution timing.

Article presentation: include three or four accurate key points near the top. Maintain organizational authorship unless the named person has confirmed authorship; the business contact may be linked separately. Preserve original publication dates and the two-post monthly cadence.

15 November 2026: Savan explicitly approved publication of the reviewed buyer guide “From sample to shipment: approving cumin, fennel, sesame and alfalfa lots” after receiving its brief and full draft. This approval applies only to that article.
