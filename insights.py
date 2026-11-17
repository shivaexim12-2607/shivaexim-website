"""Source-backed articles. Append new posts; retain historical dates and URLs."""
import json
from html import escape
from review_content import article_takeaways

POSTS = [
    {
        'slug': 'october-2026-cumin-fennel-sesame-crop-outlook',
        'title': 'Cumin, fennel and sesame: the October 2026 crop outlook',
        'category': 'MARKET UPDATE',
        'date': '2026-10-12',
        'display_date': '12 October 2026',
        'summary': 'Rainfall risk, planting decisions and competing origins: what buyers should watch before drawing conclusions about 2027 supply.',
        'body': '''
<p class="lead">A rainfall shortfall deserves attention, but it is not a complete crop forecast. For buyers of cumin, fennel and sesame, the useful question is how weather, planting decisions, existing stocks and competing origins combine to affect available supply.</p>
<h2>What the Indian evidence tells us</h2>
<p>IMD’s end-of-season assessment reports June–September 2026 rainfall for India at 87% of the long-period average. The national figure establishes a rainfall concern; it does not establish an identical deficit across Gujarat and Rajasthan or a uniform impact on their crop-growing districts. Regional distribution and the timing of rain matter.</p>
<p>The Directorate of Arecanut and Spices Development’s second advance estimates for 2025–26 report approximately 5% lower cumin production and 18% lower fennel production compared with 2024–25. The directorate attributes these declines mainly to reduced acreage in Gujarat following low prevailing prices and, for fennel, farmers moving to alternatives.</p>
<p>These production estimates concern the earlier crop year. They should not be presented as proof of the size of the crop harvested in 2027, or as a measured consequence of the 2026 monsoon.</p>
<h2>Shiva Exim’s view on the next crop</h2>
<blockquote><p>Shiva Exim sees a risk of lower Indian supply in 2027 if water constraints reduce planting or yields. This is a provisional market view, pending district rainfall, irrigation and acreage evidence.</p></blockquote>
<p>This outlook reflects the company’s concern about rainfall in Gujarat and Rajasthan. Before turning that concern into a production forecast, we want to see crop-specific planting progress and water availability in the relevant districts. A decline is a possibility, not an established outcome.</p>
<p>Fennel illustrates why irrigation needs to be considered alongside rainfall. ICAR–NRCSS guidance describes its main cool-season sowing window and highlights irrigation during flowering and seed formation. Water available to farmers during the growing season can change the outcome even after a weak monsoon.</p>
<h2>Sesame: India, Brazil and Pakistan</h2>
<p>For India, buyers should distinguish the crop season and region being discussed, and separate total seed output from the volume meeting their quality specification. A crop-size headline cannot tell a processor how much suitable material is available.</p>
<p>IBRAFE’s Brazilian sesame update for 2026 flags potentially tighter supply. We treat this as an industry outlook rather than a final production count. For Brazil and Pakistan, our comparison will track acreage, harvest progress, sample quality, carryover stocks and dated export offers. We have not verified comparable current-season national tonnage for Pakistan and will not substitute historical output or export shipments for a crop estimate.</p>
<h2>Cumin: India, Egypt and China</h2>
<p>Indian planting and output need to be assessed alongside stocks and demand. China belongs in the comparison both as a growing origin and as a buyer: changes in domestic availability may influence import requirements, but that relationship needs actual crop and trade evidence.</p>
<p>For Egypt, the useful comparison is exportable availability at the required specification and shipment timing. Comparable current-season production totals for Egypt and China remain unverified in this update. We are not assigning either origin an unsupported tonnage or percentage change.</p>
<h2>Fennel: India and Egypt</h2>
<p>Our India–Egypt comparison will cover crop-year availability, colour, seed size, purity, moisture and buyer-required testing. Supplier offers should identify the lot and quality basis; an origin name alone is not a specification. We have not verified a comparable current Egyptian national fennel crop estimate.</p>
<h2>What buyers can do now</h2>
<ul><li>Request the crop year, origin and specification with each offer.</li><li>Compare dated quotations on the same currency, packing and shipment basis.</li><li>Check samples and required test results before agreeing commercial terms.</li><li>Watch acreage, irrigation and carryover stocks as well as rainfall.</li></ul>
<p>A smaller harvest does not automatically produce a higher market price. Existing stocks, buyer demand and supply from other origins can offset a production decline. This article contains no firm price forecast or live quotation.</p>
<h2>Sources and scope</h2>
<ul class="article-sources"><li><a href="https://internal.imd.gov.in/press_release/20260930_pr_5358.pdf">IMD: end-of-season monsoon assessment, 30 September 2026</a></li><li><a href="https://dasd.kerala.gov.in/second-advance-estimates-for-2025-26/">DASD: second advance estimates for 2025–26</a></li><li><a href="https://www.nrcssajmer.org.in/Upload/637876998976459938.pdf">ICAR–NRCSS: Advance Production Technology of Fennel</a></li><li><a href="https://ibrafe.org/noticias/market-update-brazilian-sesame-2026">IBRAFE: Brazilian sesame market update 2026</a></li></ul>
<p class="small">Evidence checked on 12 October 2026. Government estimates, industry outlooks and Shiva Exim’s opinion are identified separately. Comparable crop figures are omitted where verification is incomplete. This is market commentary; product availability and commercial terms require a separate quotation.</p>
''',
    },
    {
        'slug': 'comparing-cumin-fennel-sesame-export-quotes',
        'title': 'How to compare cumin, fennel and sesame export quotations',
        'category': 'BUYER GUIDE',
        'date': '2026-10-12',
        'display_date': '12 October 2026',
        'summary': 'A practical checklist for comparing product quality, origin, packing and shipment terms before choosing a supplier.',
        'body': '''
<p class="lead">Two offers for the same named spice or seed can describe different products. Before comparing price, make sure the quality specification, packing and shipment basis match your requirement.</p>
<h2>Start with the product and its intended use</h2>
<p>State whether you need whole cumin, whole fennel, natural sesame or hulled sesame. Describe the application: distribution, spice blending, food processing or another use. A sample suitable for one application may not meet another buyer’s appearance or processing requirements.</p>
<h2>Cumin: clarify what the grade means</h2>
<p>Shiva Exim’s cumin portfolio includes commercial labels described as 99% Europe quality and 99% Singapore quality. When enquiring, specify what the purity figure measures and the agreed test method. These labels alone do not establish destination compliance, certification or the results of every required test.</p>
<p>Ask for the cleaning preference, foreign-matter limits, moisture requirement, crop year and sample reference. If buying cumin powder instead, agree the grinding requirement and packing as a separate product specification.</p>
<h2>Fennel: appearance and uniformity count</h2>
<p>Fennel enquiries should state seed-size preference, colour requirement, purity, moisture and cleaning preference. Discuss aroma or other quality requirements relevant to your application. Compare representative samples rather than relying only on a grade name.</p>
<p>The 99% Europe and 99% Singapore labels in Shiva Exim’s fennel portfolio are commercial quality descriptions. The destination’s requirements and the agreed lot tests still need to be checked individually.</p>
<h2>Sesame: compare the same form</h2>
<p>Specify natural or hulled sesame, the required colour and the intended application. Agree purity, moisture and permitted defects, with any buyer-required testing stated in the enquiry. Comparing different forms or colours on price alone can give a misleading result.</p>
<h2>Make the quotation basis explicit</h2>
<div class="specification-table-wrap"><table class="specification-table"><caption>Details to agree before comparing offers</caption><thead><tr><th scope="col">Detail</th><th scope="col">Ask the supplier</th><th scope="col">Why it matters</th></tr></thead><tbody>
<tr><th scope="row">Origin and crop year</th><td>Declare both for the offered lot.</td><td>Separates new-crop material from earlier stocks.</td></tr>
<tr><th scope="row">Price and validity</th><td>Currency, unit, quotation date and expiry.</td><td>Avoids comparing a current offer with an outdated indication.</td></tr>
<tr><th scope="row">Shipment basis</th><td>Agreed trade term, named port or place, and included costs.</td><td>Shows whether freight, local charges or other expenses are included.</td></tr>
<tr><th scope="row">Packing</th><td>Net bag weight, bag construction, liner and any pallet requirement.</td><td>Packing changes handling and total cost.</td></tr>
<tr><th scope="row">Quantity and timing</th><td>Net quantity and proposed shipment period.</td><td>Clarifies the actual offer rather than a general availability statement.</td></tr>
<tr><th scope="row">Quality evidence</th><td>Sample reference, test parameters, methods and agreed acceptance limits.</td><td>Connects the price to a defined quality requirement.</td></tr>
</tbody></table></div>
<h2>Send an enquiry that can become a useful quotation</h2>
<p>A useful first message includes the product, grade, quantity, packing, destination port, preferred shipment period and required documents or test reports. Include your company contact details and tell us whether you need a sample.</p>
<p>Shiva Exim confirms availability, testing, documentation and commercial terms for each enquiry. Product listings and this guide are not fixed offers, guarantees of stock or claims that every certification is available.</p>
<h2>Related product specifications</h2>
<ul><li><a href="/products/cumin-seeds/">Cumin seeds: product and specification guide</a></li><li><a href="/products/fennel-seeds/">Fennel seeds: product and specification guide</a></li><li><a href="/products/sesame-seeds/">Sesame seeds: product and specification guide</a></li></ul>
<p class="small">Prepared by Shiva Exim using its published product enquiry guides and company-confirmed commercial quality labels. This is a procurement checklist, not destination-specific regulatory advice or a live quotation.</p>
''',
    },
{'slug': 'november-2026-spice-watch-sowing-risk-sesame-supply',
 'title': 'November 2026 spice watch: sowing risk and sesame supply evidence',
 'category': 'MARKET UPDATE',
 'date': '2026-11-01',
 'display_date': '1 November 2026',
 'summary': 'IMD’s November outlook, a dated Brazilian sesame estimate and the evidence still needed before calling a '
            '2027 supply shortage.',
 'body': '\n'
         '<p class="lead">November starts with a new weather outlook, not a confirmed shortage. For cumin, fennel and '
         'sesame buyers, the useful distinction is between a forecast of growing conditions, an estimate of a '
         'particular crop year and the quantity a supplier can actually ship to an agreed specification.</p>\n'
         '<h2>The fresh weather signal: a forecast, not a harvest result</h2>\n'
         '<p>In its <a href="https://mausam.imd.gov.in/Forecast/marquee_data/Press_Release_NOV_31oct_2026.pdf">31 '
         'October 2026 monthly outlook</a>, the India Meteorological Department forecasts below-normal November '
         'rainfall for the country as a whole and above-normal maximum temperatures over most areas. Its regional '
         'picture is not uniform: some areas of central, northwest and northeast India have normal to above-normal '
         'rainfall probabilities. The outlook is probabilistic and applies to November 2026.</p>\n'
         '<p><strong>Our interpretation:</strong> this is a reason to monitor conditions during planting, not evidence '
         'that every cumin or fennel district in Gujarat and Rajasthan will face the same water constraint. A national '
         'rainfall category does not measure farm irrigation, planted area or the yield of the crop harvested in 2027. '
         'We have not verified a crop-district water balance or a complete current sowing series for this '
         'article.</p>\n'
         '<h2>Indian cumin and fennel: keep the crop-year labels attached</h2>\n'
         '<p>The <a href="https://dasd.kerala.gov.in/second-advance-estimates-for-2025-26/">DASD second advance '
         'estimates for 2025–26</a>, on a page marked updated 28 September 2026, describe lower cumin and fennel '
         'production compared with the preceding crop year. DASD links the reductions principally to lower acreage in '
         'Gujarat following weak prices, with fennel farmers moving to alternatives. These are government estimates '
         'for 2025–26, not measurements of the crop to be harvested in 2027.</p>\n'
         '<p>For the next crop, our watchlist is planted area, access to irrigation, subsequent weather and harvest '
         'evidence. Existing stocks also matter to shipment availability. A change in one of these factors should not '
         'be treated as a verified change in all of them.</p>\n'
         '<h2>Brazilian sesame: a dated estimate changes the evidence base</h2>\n'
         '<p>On <a '
         'href="https://www.sedec.mt.gov.br/-/mato-grosso-lidera-produ%C3%A7%C3%A3o-de-gr%C3%A3os-no-brasil-e-concentra-59-7-do-gergelim-nacional">6 '
         'October 2026, Mato Grosso’s economic development secretariat, SEDEC</a>, reported a Brazilian sesame '
         'production estimate of 356,300 tonnes, citing IBGE’s September agricultural survey. This is an estimate '
         'reported for 2026, not a final count of export-ready stock. SEDEC describes Mato Grosso as the leading '
         'producing state and sesame’s role as a crop grown after soybean.</p>\n'
         '<p>This provides a concrete checkpoint alongside the earlier industry outlook discussed in our <a '
         'href="/insights/october-2026-cumin-fennel-sesame-crop-outlook/">October article</a>. We are not treating '
         'different reports as a like-for-like revision series, or deriving a price forecast from the national '
         'estimate. Suppliers still need to establish crop year, form, quality, remaining stock and shipment timing '
         'for their own offer.</p>\n'
         '<h2>Origin watchlist: what is known and what still needs evidence</h2>\n'
         '<p>The origins below are Shiva Exim’s requested comparison set, not an exhaustive list of producing '
         'countries. We have not verified comparable current-season national crop estimates for Pakistan sesame, Egypt '
         'or China cumin, or Egypt fennel in this review. We therefore publish no tonnage, percentage change or supply '
         'ranking for those combinations.</p>\n'
         '<div class="specification-table-wrap"><table class="specification-table"><caption>Evidence checkpoints as of '
         '1 November 2026</caption><thead><tr><th scope="col">Product / origin</th><th scope="col">Evidence '
         'status</th><th scope="col">Next commercial check</th></tr></thead><tbody>\n'
         '<tr><th scope="row">Sesame / India</th><td>No verified current national crop total used '
         'here.</td><td>Identify the crop season, producing region, natural or hulled form and offered lot.</td></tr>\n'
         '<tr><th scope="row">Sesame / Brazil</th><td>SEDEC reports an IBGE-based 2026 production estimate; it is not '
         'exportable stock.</td><td>Match origin, crop year, processing form, sample and available shipment '
         'window.</td></tr>\n'
         '<tr><th scope="row">Sesame / Pakistan</th><td>Comparable current-season crop estimate not '
         'verified.</td><td>Request dated origin and crop-year evidence, lot analysis and shipment '
         'availability.</td></tr>\n'
         '<tr><th scope="row">Cumin / India</th><td>DASD’s 2025–26 estimates are historical context for the next '
         'planting decision.</td><td>Follow new acreage and water evidence separately from carryover '
         'offers.</td></tr>\n'
         '<tr><th scope="row">Cumin / Egypt</th><td>Comparable current-season crop estimate not '
         'verified.</td><td>Confirm crop year, actual stock, cleaning, moisture and aroma requirements.</td></tr>\n'
         '<tr><th scope="row">Cumin / China</th><td>Comparable current-season crop estimate not '
         'verified.</td><td>Verify the declared origin and lot specification rather than assuming availability from '
         'trade activity.</td></tr>\n'
         '<tr><th scope="row">Fennel / India</th><td>DASD describes acreage-related weakness in 2025–26; it does not '
         'establish 2027 output.</td><td>Monitor planting and irrigation, then compare seed size, colour and required '
         'tests.</td></tr>\n'
         '<tr><th scope="row">Fennel / Egypt</th><td>Comparable current-season crop estimate not '
         'verified.</td><td>Request the offered crop year, sample, size, colour and shipment period.</td></tr>\n'
         '</tbody></table></div>\n'
         '<h2>Shiva Exim’s provisional 2027 outlook</h2>\n'
         '<blockquote><p>Our company view, first supplied on 12 October 2026, is that weaker rainfall in Gujarat and '
         'Rajasthan may reduce 2027 cumin, fennel and sesame production. This remains a conditional opinion, not a '
         'confirmed production forecast or a new field observation.</p></blockquote>\n'
         '<p>The November outlook does not validate that hypothesis on its own. We would reassess it against district '
         'rainfall distribution, irrigation availability, actual crop acreage, harvest results and carryover stocks. '
         'Better water availability or larger acreage could weaken the lower-supply case; adverse conditions could '
         'strengthen it. No percentage production loss or guaranteed price direction is assigned.</p>\n'
         '<h2>What to request with an offer this month</h2>\n'
         '<p>Ask suppliers to separate new-crop expectations from stock available now. A useful offer states origin '
         'and crop year, quantity, lot or sample reference, packing, shipment period and the testing required by the '
         'buyer. Compare prices only when currency, unit, grade, quotation date and named shipment or cost basis are '
         'explicit.</p>\n'
         '<p>For <a href="/products/cumin-seeds/">cumin</a> and <a href="/products/fennel-seeds/">fennel</a>, Shiva '
         'Exim’s 99% Europe and 99% Singapore descriptions are commercial labels; they do not establish certification '
         'or blanket destination compliance. For <a href="/products/sesame-seeds/">sesame</a>, distinguish natural '
         'seed from hulled material before comparing offers. Our <a '
         'href="/insights/comparing-cumin-fennel-sesame-export-quotes/">quotation-comparison guide</a> explains the '
         'specification and shipment checks.</p>\n'
         '<p>This update contains no live price quotation. A production estimate, export shipment statistic and '
         'supplier stock declaration describe different things; none should silently substitute for the others.</p>\n'
         '<h2>Sources</h2>\n'
         '<ul class="article-sources">\n'
         '<li><a href="https://mausam.imd.gov.in/Forecast/marquee_data/Press_Release_NOV_31oct_2026.pdf">IMD: Monthly '
         'Outlook for Rainfall and Temperature for November 2026, issued 31 October 2026</a> — weather forecast.</li>\n'
         '<li><a href="https://dasd.kerala.gov.in/second-advance-estimates-for-2025-26/">DASD: Second Advance '
         'Estimates for 2025–26, page marked updated 28 September 2026</a> — government crop estimates and acreage '
         'explanation.</li>\n'
         '<li><a '
         'href="https://www.sedec.mt.gov.br/-/mato-grosso-lidera-produ%C3%A7%C3%A3o-de-gr%C3%A3os-no-brasil-e-concentra-59-7-do-gergelim-nacional">SEDEC-MT: '
         'Brazilian sesame production report, 6 October 2026</a> — state-government account citing IBGE’s September '
         'survey; not independently recast as a final harvest count.</li>\n'
         '</ul>\n'
         '<p class="small">Evidence checked on 1 November 2026. Market estimates may change. Shiva Exim’s 2027 outlook '
         'is provisional.</p>\n'},
{'slug': 'approving-spice-alfalfa-samples-test-reports-shipment-lots',
 'title': 'From sample to shipment: approving cumin, fennel, sesame and '
          'alfalfa lots',
 'category': 'BUYER GUIDE',
 'date': '2026-11-15',
 'display_date': '15 November 2026',
 'summary': 'Connect sample approval, test reports and shipment identity, with '
            'practical checks for spice buyers and alfalfa planting seed '
            'importers.',
 'body': '\n'
         '<p class="lead">A sample may look right while the shipment paperwork '
         'describes a different lot. Before loading cumin, fennel, sesame or '
         'alfalfa seed, make one final connection: does the material being '
         'packed match the sample, specification and evidence the buyer '
         'actually approved?</p>\n'
         '<h2>Key points</h2><ul><li>Record one consistent lot identity across '
         'samples, reports and shipment records.</li><li>Approve appearance '
         'and analytical results as separate decisions.</li><li>Check '
         'seed-test certificates by their scope, not just their '
         'colour.</li><li>Write down what is accepted and what still needs '
         'resolution before loading.</li></ul>\n'
         '<h2>1. Give the approval an identity</h2>\n'
         '<p>Our recommended first step is an approval record naming the '
         'product, intended use, declared origin, crop year, lot number, '
         'quantity and sample reference. Record who drew the sample, when it '
         'was drawn and which packed or bulk lot it represents. Ask the '
         'supplier to explain how that identity will appear on the bags and '
         'shipment documents.</p>\n'
         '<p>For example, approval of a fennel reference sample does not '
         'automatically approve a replacement lot. If the lot, processing '
         'stage or specification changes, ask which earlier tests and '
         'approvals still apply and what needs to be repeated. Keep a retained '
         'sample under agreed storage conditions for comparison if a question '
         'arises later.</p>\n'
         '<h2>2. Separate what you can see from what must be tested</h2>\n'
         '<p>Colour, seed size, visible foreign matter and aroma are useful '
         'sample checks. They do not establish every analytical result. '
         'Codex’s cumin standard, CXS 327-2017, amended in 2021 and 2022, '
         'addresses physical and chemical characteristics, hygiene and lot '
         'acceptance separately. It provides a technical reference for cumin; '
         'it should not be silently applied as a fennel or sesame '
         'standard.</p>\n'
         '<p>For <a '
         'href="https://shivaexim.com/products/cumin-seeds/">cumin</a> and <a '
         'href="https://shivaexim.com/products/fennel-seeds/">fennel</a>, '
         'Shiva Exim’s 99% Europe and 99% Singapore descriptions are '
         'commercial quality labels. Agree what purity measures, the test '
         'method and the other acceptance limits. Neither label is '
         'certification or blanket approval for a destination.</p>\n'
         '<p>For <a '
         'href="https://shivaexim.com/products/sesame-seeds/">sesame</a>, '
         'confirm natural or hulled form before assessing colour, defects and '
         'the relevant food-quality tests. A visibly clean sample does not '
         'replace microbiological or residue evidence.</p>\n'
         '<h2>3. Read the report against the order</h2>\n'
         '<p>As a procurement check, compare the laboratory name, report '
         'number, sample and lot references, sampling and test dates, methods, '
         'units, results and agreed limits. A certificate of analysis should '
         'be read for the parameters it actually covers. A generic statement '
         'such as “tested” does not tell the buyer which substances or '
         'organisms were examined, or at what reporting limits.</p>\n'
         '<p>Agree the required test panel and sampling arrangements before '
         'commissioning work. For EU-bound food, the European Commission’s '
         'pesticides database helps identify product-specific maximum residue '
         'levels; the Commission states that the database is informational and '
         'official legal information is published in the EU Official Journal. '
         'This guide sets no numerical residue limits and makes no destination '
         'compliance determination. The importer should confirm applicable '
         'requirements for the specific product and shipment.</p>\n'
         '<h2>4. Use the same questions across origins</h2>\n'
         '<p>Origin is part of traceability, not an automatic quality ranking. '
         'The following comparison set reflects Shiva Exim’s buying interests; '
         'it is not a claim that these are the only producing countries or '
         'that Shiva Exim currently offers every origin.</p>\n'
         '<div class="specification-table-wrap"><table '
         'class="specification-table"><thead><tr><th>Product and '
         'origins</th><th>Evidence to request for the offered '
         'lot</th></tr></thead><tbody>\n'
         '<tr><td>Sesame — India, Brazil, Pakistan</td><td>Declared origin and '
         'crop season; natural or hulled form; sample identity; agreed colour, '
         'purity and defect criteria; buyer-required microbiological and '
         'contaminant reports.</td></tr>\n'
         '<tr><td>Cumin — India, Egypt, China</td><td>Origin, crop year and '
         'lot; whole or other agreed form; cleaning and physical-quality '
         'limits; moisture and aroma-related requirements; required analytical '
         'panel.</td></tr>\n'
         '<tr><td>Fennel — India, Egypt</td><td>Origin, crop year and lot; '
         'agreed colour and size reference; purity and moisture criteria; '
         'aroma and buyer-required tests.</td></tr>\n'
         '</tbody></table></div>\n'
         '<p>Ask the same core questions when changing origin or supplier. Do '
         'not assume an earlier sample approval or test report transfers to '
         'the next consignment. This article supplies no new national crop '
         'estimate or available-stock figure for these origins.</p>\n'
         '<h2>5. Alfalfa planting seed needs a separate evidence check</h2>\n'
         '<p><a href="https://shivaexim.com/products/alfalfa-seeds/">Alfalfa '
         'seed</a> in Shiva Exim’s portfolio is for agricultural planting to '
         'establish a fodder crop. Specify the actual variety requirement, '
         'growing destination, treatment or coating status, physical purity, '
         'normal germination, hard-seed reporting, other-seed content and test '
         'date. The commercial single-year and multi-year labels are not '
         'guarantees of stand life or yield.</p>\n'
         '<p>ISTA’s official FAQ explains that a Blue International Seed '
         'Sample Certificate concerns the submitted sample at receipt; seed '
         'lot certificates concern the lot at sampling. Buyers should '
         'therefore check the scope of the certificate requested and supplied. '
         'ISTA’s current rules page identifies its 2026 edition, including '
         'certificate and sampling chapters.</p>\n'
         '<p>OECD Seed Schemes concern varietal certification under harmonised '
         'official procedures. That is a different purpose from reporting '
         'seed-test results. Specify the exact certificate, label and variety '
         'evidence your buyer requires, and confirm applicability and '
         'availability before committing. This guide does not claim that Shiva '
         'Exim holds an ISTA certificate or OECD certification for an offered '
         'lot.</p>\n'
         '<h2>6. Make the loading decision explicit</h2>\n'
         '<p>Our suggested release record has five fields: lot and quantity; '
         'approved sample reference; agreed specification; accepted '
         'report/document references; and the person and date authorising '
         'release. Record any exceptions separately. An unresolved identity '
         'mismatch or missing agreed test should be clarified before that lot '
         'is released.</p>\n'
         '<p>Before loading, compare the lot marks, packing list and actual '
         'packed material against that record. Agree how a proposed '
         'substitution or repacking will be handled. This is an operational '
         'recommendation, not a claim that testing eliminates all shipment '
         'risk.</p>\n'
         '<h2>Keep crop outlook separate from lot approval</h2>\n'
         '<p>Shiva Exim’s view, first supplied on 12 October 2026, is that '
         'weaker rainfall in Gujarat and Rajasthan may reduce Indian cumin, '
         'fennel and sesame production in 2027. That remains a provisional '
         'opinion, pending district rainfall, irrigation, acreage, harvest and '
         'carryover evidence. It does not establish the quality or '
         'availability of a particular lot, and this buyer guide does not '
         'update that forecast or predict prices.</p>\n'
         '<h2>Sources</h2><p class="small">Checked 15 November 2026. Dates '
         'below identify the standard or edition; undated pages are labelled '
         'as such.</p><ul>\n'
         '<li><a '
         'href="https://www.fao.org/fao-who-codexalimentarius/sh-proxy/ua/?lnk=1&amp;url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%2B327-2017%252FCXS_327e.pdf">FAO/WHO '
         'Codex: Standard for Cumin, CXS 327-2017</a> — adopted 2017; amended '
         '2021 and 2022. Technical reference for cumin characteristics and lot '
         'acceptance.</li>\n'
         '<li><a '
         'href="https://food.ec.europa.eu/plants/pesticides/eu-pesticides-database_en">European '
         'Commission: EU Pesticides Database</a> — undated live information '
         'page. Explains product/residue searches and the authority of '
         'Official Journal texts.</li>\n'
         '<li><a '
         'href="https://www.seedtest.org/en/accreditation/accreditation-faqs.html">ISTA: '
         'Accreditation FAQs, question 4</a> — undated. Explains '
         'sample-certificate and lot-certificate scope.</li>\n'
         '<li><a '
         'href="https://www.seedtest.org/en/publications/international-rules-seed-testing.html">ISTA: '
         'International Rules for Seed Testing</a> — 2026 edition listed. '
         'Sampling, testing and reporting framework.</li>\n'
         '<li><a '
         'href="https://www.oecd.org/en/topics/sub-issues/seeds.html">OECD: '
         'Seed Schemes</a> — undated overview; lists a varieties download '
         'updated July 2026. Explains varietal certification.</li>\n'
         '<li>Shiva Exim’s company-confirmed <a '
         'href="https://shivaexim.com/products/cumin-seeds/">cumin</a>, <a '
         'href="https://shivaexim.com/products/fennel-seeds/">fennel</a>, <a '
         'href="https://shivaexim.com/products/sesame-seeds/">sesame</a> and '
         '<a href="https://shivaexim.com/products/alfalfa-seeds/">alfalfa</a> '
         'product guides — reviewed in the linked Site’s current source on 15 '
         'November 2026.</li>\n'
         '</ul><p class="small">Lot availability, testing, documentation and '
         'terms require confirmation for each enquiry. Market estimates may '
         'change. Shiva Exim’s 2027 outlook is provisional.</p>\n'},
]

def render_insights(shell, intro, base):
    cards=''.join(f'<a class="product-card" href="/insights/{p["slug"]}/"><span class="category">{p["category"]}</span><p class="article-date">{p["display_date"]}</p><h3>{escape(p["title"])}</h3><p>{escape(p["summary"])}</p><span class="text-link">Read article →</span></a>' for p in sorted(POSTS,key=lambda p:p['date'],reverse=True))
    shell('insights','Market Insights & Buyer Guides','Crop outlooks and practical buyer guides from Shiva Exim, covering cumin, fennel, sesame and agricultural trade.',intro('SHIVA EXIM JOURNAL','Market insights.<br>Better buying decisions.','Dated market updates and practical guides, combining verified sources with clearly identified Shiva Exim commentary.')+'<section class="featured wrap"><div class="product-grid">'+cards+'</div></section>','Market Insights')
    paths=['insights']
    for p in POSTS:
        path='insights/'+p['slug']
        url=base+'/'+path+'/'
        schema={'@context':'https://schema.org','@type':'BlogPosting','headline':p['title'],'description':p['summary'],'datePublished':p['date'],'dateModified':p['date'],'author':{'@type':'Organization','name':'Shiva Exim','url':base+'/about/'},'publisher':{'@type':'Organization','name':'Shiva Exim','url':base},'mainEntityOfPage':url,'url':url}
        body=f'<div class="wrap breadcrumb"><a href="/">Home</a><span>/</span><a href="/insights/">Market Insights</a></div>'+intro(p['category'],escape(p['title']),p['summary'])+f'<article class="prose wrap insight-article"><p class="article-byline">By <a href="/about/">Shiva Exim</a> · Business contact: <a href="/about/#savan-patel">Savan Patel</a> · <time datetime="{p["date"]}">{p["display_date"]}</time></p>'+article_takeaways(p)+p['body']+'<div class="article-enquiry"><h2>Discuss your product requirement</h2><p>Share the product, quality, quantity and shipment details with Shiva Exim.</p><a class="button" href="/contact/">Send an enquiry ↗</a></div><a class="text-link" href="/insights/">All market insights →</a></article><script type="application/ld+json">'+json.dumps(schema)+'</script>'
        shell(path,p['title'],p['summary'],body,'Market Insights')
        paths.append(path)
    return paths
