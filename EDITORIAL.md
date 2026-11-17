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

The source repository is the durable content store; articles are defined in insights.py. No browser session, WordPress login, Google sign-in or secret is required for this publication workflow.

1. Follow the current Sites skill. Read get_site for this linked project, acquire a new source repository write credential and open the repository using the official source helper. Credentials remain in memory and are passed only through hidden stdin.
2. Inspect insights.py and the existing month/date coverage. If two articles for the target month already exist, do not create duplicates. After a partial prior run, resume its saved version/deployment rather than publishing twice.
3. Append the new post to POSTS in insights.py. render_insights handles the article, index, byline and BlogPosting metadata. build.py includes the index and article paths in sitemap.xml. Do not replace prior posts.
4. Run python build.py. Validate internal links, canonical URLs, JSON-LD and that sitemap URLs match generated pages. Preserve the logo plus SHIVA EXIM; do not restore the removed EXPORT & IMPORT subtitle. Browser QA is unavailable unless the supported Sites browser control becomes available; follow the skill's preview boundary.
5. Package/push the exact checked source via the source helper, save the matching archive-backed version and deploy through the public Sites deployment operation. Native terminal success with the URL is required before reporting publication. Follow supported deployment status recovery for nonterminal or failed results.
6. After successful deployment, run `python submit_indexnow.py https://shivaexim.com/insights/ https://shivaexim.com/insights/NEW-SLUG/` with the actual new article URL. Submit only changed published pages, not the full sitemap on every run. Report submission failures separately from publication; HTTP 200 means received and 202 means key validation pending, neither guarantees indexing.
7. Read back the saved version/source metadata, and report the actual published article URL and substantive sources. If source access, publishing or verification fails, report the blocker; never claim the post is live. Store no private credentials in the repository. The IndexNow key is intentionally served as a public domain-verification file.

The monthly routine was chosen as the 1st and 15th, around 10:00 IST, starting November 2026 because October already has two posts. The linked cloud schedule is authoritative for execution timing.

Article presentation: include three or four accurate key points near the top. Maintain organizational authorship unless the named person has confirmed authorship; the business contact may be linked separately. Preserve original publication dates and the two-post monthly cadence.

15 November 2026: Savan explicitly approved publication of the reviewed buyer guide “From sample to shipment: approving cumin, fennel, sesame and alfalfa lots” after receiving its brief and full draft. This approval applies only to that article.
