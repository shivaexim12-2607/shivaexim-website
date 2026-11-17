# Shiva Exim website

Buildless, responsive product catalogue. Run `python build.py` after changing product copy or templates. Public files are in `dist/`.

## Current launch state

- Public Sites deployment. Apex and www domain routing and SSL are active.
- 19 export and 12 import product entries, with a separate URL for every product.
- Priority home-page exports: cumin, fennel, alfalfa; onion seeds also featured.
- Email and WhatsApp enquiry drafts; no website submission database and no false submission success.
- No invented prices, stock, certifications, facilities, customers or performance statistics.
- Illustrative generated spice photograph, labelled as illustrative.
- Existing business address, telephone and email retained; UAE and Ghana offices omitted.
- The header and footer use the pink-purple SE symbol beside SHIVA EXIM. The owner requested removal of the EXPORT & IMPORT subtitle, completed on 11 October 2026.
- Brand proportions use a smaller SE symbol vertically centred beside a larger company name in the same Georgia serif family as page headings, with responsive sizing on mobile.
- Canonical URLs, structured data and sitemap use https://shivaexim.com. Search Console ownership and sitemap processing are verified by owner screenshots; indexing is not guaranteed. Security Issues and Manual Actions reported no issues on 12 October 2026.
- Market Insights is generated from insights.py. October begins with two source-backed articles; see EDITORIAL.md for the recurring content and publishing policy.
- A language selector on all pages submits the public canonical page URL to Google Translate in a new tab, using the buyer's selected language. English remains the original. It is an external automatic-translation view, not a set of human-reviewed localized URLs. Website translation availability depends on Google and region; live rendering through that service was not verified in the managed environment.
- The top-right email is 16 px on desktop and 14 px on mobile. The logo frame and SHIVA EXIM text have matching 40 px nominal sizing on desktop and 30 px on mobile, with aligned baselines/centering.

## Before public launch

1. Confirm the current address, approved company logo and real product photos.
2. Confirm grades, sample specifications, packing, documentation and product varieties. In particular, confirm what the commercial term “green millet” refers to.
3. Export and inspect the old site's URL list. Preserve useful paths or configure individual permanent redirects. Do not blanket-redirect unrelated spam pages.
4. Confirm the public hosting plan and custom-domain availability before moving DNS. Record and retain mail MX, SPF, DKIM and DMARC records so existing email continues working.
5. Complete GoDaddy routing: A @ 162.159.143.30 and A @ 172.66.3.26 replace the old A @ 82.112.229.76; CNAME www custom-domains.chatgpt.site replaces www shivaexim.com. Preserve all email and verification records. Prior website routing is recorded here for rollback.
6. Verify mobile layout, product filters, email and WhatsApp drafts in the deployed site. Browser QA was unavailable in the managed build environment.
7. Check HTTPS, domain routing, enquiry destinations and all public links; then submit the sitemap through the company's Search Console account.

## Content structure

Home; Exports; Imports; About; Contact; Privacy; 31 individual product pages; Market Insights and its articles.

17 October 2026: removed sliced ginger from the export catalogue and generated page, retaining whole dry ginger. Added mustard seeds, maize and dill seeds with original descriptions, specification enquiry parameters, applications and product FAQs. Updated the enquiry dropdown, About page and sitemap through the shared build. Home-page priorities use stable product slugs rather than positional indexes. The removed page remains recoverable from source history.

The owner then confirmed mustard types as bold and micro for human consumption and oil extraction; maize is for cattle feed; dill seeds are whole and splits, both machine clean. Cards, descriptions, confirmed-option labels, specification tables and FAQs reflect these details. No numeric size, moisture, purity, oil or feed-analysis guarantees were supplied.

Each product page has a fuller product description, common applications and a product-specific specification guide. Guide rows state the parameter, what the buyer or supplier should specify, and why it matters. Numeric stock specifications are not invented. Popcorn sourcing preferences reflect the user's supplied butterfly type, commercial sizes, 30 kg packing and origin preferences. Reference links point to Spices Board, ISTA, APEDA, IOC and USDA where relevant; none imply certification of the company or its stock.

Confirmed by the user on 10 October 2026: cumin and fennel have 99% Europe quality and 99% Singapore quality options; alfalfa has single-year and multi-year quality options. These are displayed as commercial quality labels. They do not imply a seed species classification, certification or blanket destination compliance.

The seed/enquiry requirements are questions to confirm, not claims that particular grades, certifications or documents are available.

22 October 2026: added a sourced sowing-quantity section to alfalfa and onion product pages. Lucerne fodder establishment uses the TNAU 20 kg/ha reference (8.1 kg/acre). Onion uses TNAU's 8–12 kg/ha of final transplanted field area (3.2–4.9 kg/acre) for nursery seedling production. Rates are conditional agronomic references, not lot specifications, universal export-market recommendations, yield guarantees or minimum order quantities. Variety, local conditions, sowing method, germination, purity, coating/treatment and alfalfa hard seeds must be confirmed. Cumin/fennel pages distinguish spice grade from planting suitability. Source URLs and review date appear on the pages; no competitor brand or agronomic performance claims were reused.

26 October 2026: connected the existing GA4 web stream G-JX66ZMLGPQ. All 40 pages load dist/analytics.js. Events: page_view, enquiry_click (contact-page links), email_click, whatsapp_click (including validated enquiry-form draft buttons), and enquiry_copy (a valid form’s copy-button click). These actions are interest signals, not messages delivered, orders or confirmed leads. Custom events carry only page URL without query/fragment and fixed placement; no enquiry values or destination URL/body. Preview hosts, Global Privacy Control and Do Not Track are excluded. Google signals and advertising personalization are disabled; privacy copy is updated. The tag is served from tracked dist/analytics.js, which build.py preserves.

Search Console verified directly on 26 October: sitemap Success, last read 22 October, 40 discovered pages; no Security Issues or Manual Actions. Four existing temporary removal requests from 23 October include the poker URL (exact and prefix) and two old shop paths. A live homepage test succeeded and one old /items/ URL returned 404; this does not verify every historic spam URL.

26 October 2026: added representative product photographs and downloadable one-page guides to cumin, fennel and alfalfa. Product media and confirmed-copy metadata live in product_media.py. build_product_guides.py creates dist/downloads/*-product-guide.pdf and optimizes product photos. Numerical lot guarantees are deliberately not invented. Web photos and PDF attribution identify the author, source, licence and representative status. Cumin and fennel photos: Sanjay Acharya, CC BY-SA 3.0; alfalfa: Tracey Slotta / USDA-NRCS PLANTS Database, public domain. Optimized files and source credits are tracked in dist/assets/products; the photo scale is not an offered lot-size guarantee. Page layout and existing business content are preserved. PDF button clicks emit product_guide_download; this is a click, not proof the download completed.

26 October 2026: extended representative photography to all 31 listed products (19 export, 12 import), and added lightweight, lazy-loaded catalogue thumbnails. product_photos.json holds the additional 28 source/author/licence records; the three original photo-and-guide entries remain in product_media.py. Each product page displays its own photo credits, and /photo-credits/ lists all image licences. Product social-sharing images now use the matching photograph. The image assets are tracked, so the normal build has no live dependency on the image hosts. No new products, lot guarantees or PDF guides were added in this change. Green millet explicitly identifies the photograph as pearl millet and asks the buyer to confirm the crop/variety; mustard identifies the pictured black mustard. Maize is illustrated as kernels without a feed-quality claim. Existing enquiry forms, Analytics setup and the three PDF guides are preserved. Validation checked all 31 full photos and 31 thumbnails, local asset existence, image decoding, attribution, PDF link preservation, and catalogue filter/search behavior.

Header and footer branding: enlarged the existing symbol, balanced the wordmark size, and aligned both at their vertical centre, including mobile sizes. Removed repeated photo captions from catalogue cards; individual product attributions and the footer-linked photo credits page remain.

Catalogue completion: added castor seeds to exports; canary seeds, watermelon seeds for human consumption, oats, berseem planting seeds, red kidney beans, cashew kernels and saffron to imports. Added distinct import-sourcing pages for sesame and cattle-feed maize while preserving their export pages. Totals: 20 export listings, 21 import listings, 51 sitemap URLs. Every listing has a licensed representative photo, card thumbnail, specification guide, FAQ and product/intent-specific enquiry links. Berseem photography is explicitly labelled as the crop rather than a seed lot. Expanded the About portfolio and confirmed popcorn sourcing preferences (butterfly, 38/40, 40/42, 42/44; Brazil/Argentina/South Africa; 30 kg bags).
Validation: built 51 pages; checked every product page/photo/thumbnail, all root-relative page and asset links, sitemap count and correct enquiry direction. Browser checks covered search, Nuts category, cashew product detail and enquiry prefill. Analytics handlers tested for WhatsApp, email, enquiry navigation and copying, including exclusion of query strings and draft contents. Search Console was signed out in the browser, so current indexing, removals and sitemap processing could not be rechecked. No claims of current stock, fixed analysis or certification added.

Floating WhatsApp contact: persistent accessible link on all 51 pages, matching the green palette, with phone-safe bottom spacing and safe-area inset. Product pages prefill the product and buying/supplying direction. Uses a direct wa.me link (no external widget or new dependency); no message is sent by the website. Analytics records whatsapp_click with placement=floating_whatsapp and excludes the draft text. Validated all 51 links and export/import prefill, simulated the event handler, and visually checked the preview. Google Analytics report access currently has an email-communications preference dialog; report-level receipt of new events is pending the user's preference choice.

Full downloadable catalogues: build_catalogues.py generates a 23-page export PDF (20 products) and a 24-page import PDF (21 products) from the current product profiles and photo metadata. Both include a cover, linked index/bookmarks, one photo/specification page per product, product-specific enquiry links and photographer/licence credits. Priority exports lead the export PDF. Download panels added to both catalogue pages; footer links are available site-wide. Catalogue downloads use a separate catalogue_download analytics event with export/import parameter. Existing one-page product PDFs, contact flows and design retained.
Validation: visually reviewed all 47 PDF pages, inspected dense pages individually, checked text bounds, product coverage, bookmarks and enquiry destinations. Verified website placement in browser preview and tested both download event handlers.

3 November 2026 buyer journey improvements: common-name searches for jeera/jira (cumin seeds and powder), saunf/variari (fennel) and lucerne (alfalfa). Enquiry email is optional, and empty draft fields show Not specified. Product options now follow buying/export or supplying/import intent, with all products available for general enquiries; changing intent clears incompatible selections. Direct product-link prefill is retained. Browser-tested aliases, supplier prefill, 20/21/41 choice counts, incompatible selection reset and email-free enquiry copying without sending any message. No changes to product claims, photos, PDFs, branding, article dates or analytics configuration.
