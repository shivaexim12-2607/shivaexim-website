"""Original buyer guidance; parameters are requests, not offered-lot guarantees."""
from html import escape

IDENTITY={
 'cumin-seeds':('Jeera / Jira','Cuminum cyminum L.'),
 'fennel-seeds':('Saunf / Variari','Foeniculum vulgare Mill.'),
}

EXTRA_ROWS={
 'cumin-seeds':[
  ('Total ash & acid-insoluble ash','Buyer limits, reporting basis and test method','Adds composition and mineral-residue checks beyond physical purity.'),
  ('Microbiology','Required Salmonella, E. coli, total plate count and yeast / mould criteria','The test panel, sample size and acceptance limits must be agreed for the lot.'),
  ('Residues & contaminants','Required pesticide, heavy-metal and other relevant test panel','Destination and buyer requirements define the applicable scope.'),
 ],
 'fennel-seeds':[
  ('Total ash & acid-insoluble ash','Required limits and reporting basis','Supports comparison beyond seed colour and purity.'),
  ('Microbiology & residues','Required microbiological panel and residue tests','Agreed lot testing complements visual sample approval.'),
 ],
 'alfalfa-seeds':[
  ('Hard seed (%)','Reported hard-seed fraction and how it is included in the test result','Read normal germination and hard seed separately before comparing reports.'),
  ('Other crop & weed seeds','Reported other-seed content and any required species screening','A physical-purity percentage alone does not identify every unwanted seed.'),
  ('Coating / inoculation','Raw or coated preference; coating or inoculation declaration if applicable','Bag weight and seed-quality results should be interpreted on the declared basis.'),
  ('Lot identity & test date','Lot number, sample reference, laboratory and date of analysis','Connects the quality report to the material proposed for shipment.'),
 ],
 'onion-seeds':[
  ('Variety suitability','Growing region, planting season and required variety information','Choose the variety for the intended crop; no suitability is assumed from the product name.'),
  ('Lot identity & moisture','Lot number, moisture target and test date','Makes seed-quality reports traceable to the offered lot.'),
 ],
 'sesame-seeds':[
  ('Free fatty acids / FFA','Maximum target, test method and reporting basis, if required','Relevant when comparing lots for oil-related processing requirements.'),
  ('Hulling & defects','For hulled enquiries: residual hull and broken-seed limits','Defines the processing result beyond the word hulled.'),
  ('Microbiology & contaminants','Buyer-required test panel, sample size and acceptance limits','Discuss these separately from purity, colour and oil content.'),
 ],
 'fenugreek-seeds':[('Foreign seeds & cleaning','Other-seed limits and required cleaning preference','Separates physical cleanliness from the overall purity figure.')],
 'cumin-powder':[('Ash & microbiology','Required ash limits and microbiological test panel','Powder fineness and aroma do not establish lot test results.')],
 'coriander-powder':[('Ash & microbiology','Required ash limits and microbiological test panel','Adds analytical requirements to appearance and grinding preferences.')],
 'whole-chilli':[('Heat & colour reporting','Heat as SHU / capsaicin and colour as ASTA value, where required','These are different properties and need separate agreed methods.')],
 'chilli-powder':[('Heat & colour reporting','Heat as SHU / capsaicin and colour as ASTA value, where required','A colour value is not a pungency measurement.')],
 'turmeric':[('Sample & curcumin report','Representative sample and curcumin reporting basis','Connects the form and appearance to a measured composition requirement.')],
 'turmeric-powder':[('Ash & composition checks','Buyer-required ash and composition analysis','Agree analytical requirements in addition to curcumin and fineness.')],
 'dry-ginger':[('Foreign matter & cleaning','Required limits and cleaning preference','Clarifies the physical condition of dried pieces.')],
 'dill-seeds':[('Analytical requirements','Buyer-required ash, microbiological and residue test panel','Confirm the required limits and methods for the specific lot.')],
 'mustard-seeds':[('Sampling & test scope','Representative sample and any buyer-required analytical or residue tests','Colour and purity do not establish all processing or test characteristics.')],
 'maize':[('Lot identity & crop condition','Crop year, lot reference and any required inspection information','Links the grain description and quality reports to the proposed shipment.')],
 'wheat':[('Grain condition','Required damaged, shrivelled or sprouted-grain limits','Adds physical condition to protein and test weight.')],
 'foxtail-millet':[('Husk & processing','Required hull removal and residual-husk limits for processed enquiries','Whole grain and dehulled grain should not be compared as the same form.')],
 'green-millet':[('Sample identity','Photo, sample or crop identification supplied with the enquiry','The exact crop must be confirmed before applying species-specific limits.')],
 'olive-oil':[('Lot analysis & category','Category declaration and relevant analytical report for the offered lot','Country of origin alone does not define the oil category.')],
 'popcorn':[('Sample performance','Popping test conditions and sample reference','Performance comparisons require a consistent method.')],
 'sunflower-seeds':[('Hull & kernel defects','For kernels: residual shell and broken-kernel limits','Whole seeds and peeled kernels require different defect checks.')],
 'soybean':[('Traceability & declarations','Lot details and evidence for any requested GMO-status declaration','Declarations should be supported for the actual offer.')],
 'pumpkin-seeds':[('Processing & shell residue','For hulled kernels: shell residue and processing preference','Distinguishes the product form and cleanliness requirement.')],
 'chia-seeds':[('Test requirements','Required microbiological or contaminant panel, if relevant','Agree the panel and acceptance criteria for the intended market.')],
 'green-peas':[('Processing preference','Whole or split, with any dehulling or polishing requirements','Defines how the pulse should be supplied.')],
 'yellow-peas':[('Processing preference','Whole or split, with any dehulling or polishing requirements','Makes different processing forms explicit.')],
 'whole-lentils':[('Type & sample','Declared lentil type and representative sample','Colour names alone may not fully define the requested pulse.')],
 'split-lentils':[('Uniformity & polishing','Split-size distribution and polishing preference','Makes the agreed processing finish explicit.')],
 'black-gram':[('Processing finish','Whole, split with skin or dehulled; any polishing preference','Different forms should be quoted separately.')],
 'chickpeas':[('Sizing method','Sieve / diameter or count method behind the commercial grade','Grade numbers need a shared measurement basis.')],
}

FAQ={
 'cumin-seeds':[
  ('How do I choose Europe or Singapore quality?','Both 99% Europe quality and 99% Singapore quality are listed. Tell us your application and buyer specification; agree the grade definition, foreign-matter limits, aroma, moisture and testing for the offered lot.'),
  ('Does 99% purity cover every quality test?','No. Physical purity is separate from moisture, volatile oil, ash, microbiology and residues. Share the required limits and test methods so the quotation can address them individually.'),
  ('Can I enquire about cleaned or colour-sorted material?','Yes. State the required cleaning or colour-sorting preference and a sample reference. The processing option and lot availability must be confirmed in the offer.'),
 ],
 'fennel-seeds':[
  ('Which fennel details should I compare?','Compare the same commercial quality label, colour reference, seed-size or sieve requirement, purity and aroma. Our listed options are 99% Europe quality and 99% Singapore quality; approve the detailed lot specification separately.'),
  ('Are colour and aroma the same quality measure?','No. A visual colour preference does not define aroma or volatile-oil results. Explain the intended application and agree both appearance and analytical requirements where needed.'),
 ],
 'alfalfa-seeds':[
  ('What do single-year and multi-year quality mean here?','These are the commercial quality labels confirmed by Shiva Exim. They are not a guarantee of stand life, yield or a named variety. Confirm the actual variety, growing region and lot-quality requirements separately.'),
  ('What should the seed report identify?','Request the actual lot number, laboratory, test date, physical purity, normal germination, hard seed, other seeds and moisture requirements. Confirm treatment, coating and certification needs with the specific offer.'),
  ('Can I assume a blue certificate or named variety is available?','No. If your destination or buyer needs an ISTA report, an OECD seed certificate or label, or a named variety, state the exact requirement. Availability and applicability must be verified before any commitment.'),
  ('Is this seed for sprouting or human consumption?','This listing is for agricultural planting to establish a fodder crop. It is not an offer of food-grade sprouting seed.'),
 ],
 'onion-seeds':[
  ('What variety information should I send?','State the intended growing region, planting season, variety preference and desired bulb colour, shape and market use. Variety suitability and lot availability require confirmation.'),
  ('Are onion seeds the same as kalonji?','No. This page concerns agricultural onion planting seed. It does not offer kalonji or a culinary black-seed product.'),
 ],
 'sesame-seeds':[
  ('Should I ask for natural or hulled sesame?','State whether the outer hull should remain or be removed, then specify colour, purity and intended use. The form and availability are confirmed on enquiry; they are not interchangeable quotation descriptions.'),
  ('Which tests matter for my application?','For food-ingredient enquiries, state your physical quality and required microbiological or contaminant tests. For oil-processing enquiries, also specify any oil-content and free-fatty-acid requirement.'),
 ],
 'fenugreek-seeds':[('What should a fenugreek enquiry include?','Specify whole seed, purity, colour reference, moisture and permitted damaged or other seeds. If you intend to grind it, explain the processing use and any required tests.')],
 'cumin-powder':[('How do I specify grinding fineness?','Provide the required sieve or mesh designation and test basis, alongside the aroma and moisture requirement. Do not rely on fine or coarse alone.')],
 'coriander-powder':[('What makes two coriander-powder offers comparable?','Match grinding fineness, aroma, colour reference, moisture and ingredient declaration, then compare the same packing and shipment basis.')],
 'whole-chilli':[('Why specify heat and colour separately?','Pungency and colour strength are different characteristics. State your required variety, stem preference, heat target and colour or sample reference separately.')],
 'chilli-powder':[('Does a redder powder mean a hotter powder?','Colour alone does not establish heat. Ask for separate pungency and colour requirements, along with mesh, moisture and the agreed ingredient declaration.')],
 'turmeric':[('What is needed to quote whole turmeric?','Specify fingers, bulbs or another required form, the variety if known, curcumin target and method, moisture and appearance. We confirm the lot details with the quotation.')],
 'turmeric-powder':[('What should I compare beyond curcumin?','Also compare grinding fineness, moisture, colour reference, ingredient declaration and required lot tests. Confirm that all offers use the same reporting basis.')],
 'dry-ginger':[('How do I distinguish different dry-ginger offers?','Specify piece size, peeled or unpeeled preference, appearance, moisture and aroma or volatile-oil requirements relevant to your application.')],
 'dill-seeds':[
  ('Are dill seeds the same as dill leaves?','No. This product page concerns dried dill seeds used as a spice. Fresh leaves and dried dill weed are different product forms and are not included in this listing.'),
  ('Which dill-seed forms are listed?','Whole and splits, both machine clean, are company-confirmed options. Select your required form and agree purity, moisture, aroma, split-size uniformity where relevant and any required lot tests.'),
 ],
 'mustard-seeds':[
  ('Which mustard types are listed?','Bold and micro are the confirmed commercial options for human consumption and oil extraction. Specify your preferred type, intended use and a grading or sample reference; exact size and lot requirements are agreed with the offer.'),
  ('Which specifications matter for mustard seeds?','Agree purity, moisture, seed condition and other-seed limits. For oil-processing enquiries, also state the oil-content target, method and any additional composition or test requirements.'),
 ],
 'maize':[
  ('What is this maize supplied for?','This listing is for cattle feed and cattle-feed processing. It is not a human-consumption maize or popcorn offer. Popcorn remains a separate import product.'),
  ('What should I include in a cattle-feed maize enquiry?','Specify moisture, broken kernels, foreign matter, damaged grain and any test-weight or feed-analysis requirements. Include required mycotoxin and other contaminant tests, quantity, packing, destination and shipment period.'),
  ('Is feed quality or non-GMO status guaranteed by the name?','No. Agree the cattle-feed specification and any GMO-status requirement with supporting lot evidence. A product name is not a lot test report or a blanket compliance guarantee.'),
 ],
 'wheat':[('Can I request a wheat export quotation immediately?','Send the intended use, variety, protein and moisture requirements, quantity and destination. Current export eligibility and the offered lot must be confirmed before a firm commitment.')],
 'foxtail-millet':[('Should I request whole or dehulled millet?','Describe the processing form your application needs, including hull removal and broken-grain requirements. Different forms should be assessed and quoted separately.')],
 'green-millet':[('Which crop does green millet mean?','The exact crop remains to be confirmed. Send its local or botanical name, intended use and a photo or sample if available so we can discuss the correct specification.')],
 'olive-oil':[('What should an olive-oil supplier offer include?','Declare the oil category, origin, lot details, relevant analysis, container type, net volume and date information. Extra virgin, virgin and refined categories should not be quoted as equivalent.')],
 'popcorn':[('What popcorn sourcing preferences are listed?','Our import enquiries focus on butterfly type, commercial sizes 38/40, 40/42 or 42/44, 30 kg bags, and Brazil, Argentina or South Africa. Confirm the size measurement basis and popping performance with your offer.')],
 'sunflower-seeds':[('Should I offer in-shell seeds or peeled kernels?','Declare the exact form and intended food or processing use. Include size, moisture and defect limits; peeled-kernel offers should address residual shell and broken kernels.')],
 'soybean':[('What details help assess a soybean offer?','State origin, crop year, intended use, moisture, foreign material, damage and any required protein, oil or GMO-status evidence. The buyer specification determines the necessary tests.')],
 'pumpkin-seeds':[('What form and sizing details should suppliers declare?','Specify in-shell seeds or hulled kernels, then provide colour, commercial size and measurement method, moisture and defect limits, including shell residue for kernel offers.')],
 'chia-seeds':[('How should suppliers describe chia seed quality?','Declare colour preference or mix, origin, crop year, purity, moisture, other-seed content and requested testing. Include lot traceability and packing details.')],
 'green-peas':[('Are these fresh, frozen or dried peas?','This portfolio concerns dried green peas. State whole or split form, any processing preference, crop year, origin and the required physical quality.')],
 'yellow-peas':[('What should a yellow-pea offer specify?','State dried whole or split form, origin, crop year, colour and size reference, moisture and defect limits, with any dehulling or polishing preference.')],
 'whole-lentils':[('How do I identify the required lentil type?','Provide the declared lentil type, colour and size or sample reference. Include origin, crop year and the intended application so incompatible types are not compared.')],
 'split-lentils':[('What processing details should I declare?','Identify the lentil type, whether it is dehulled, the polishing preference, split-size uniformity and permitted broken material, alongside origin and crop year.')],
 'black-gram':[('Which black-gram forms should be distinguished?','Declare whole black gram, split with skin or dehulled product. State any polishing preference, size, moisture and defect requirements for that exact form.')],
 'chickpeas':[('How should suppliers describe chickpea size?','Identify kabuli or desi, then declare the commercial size or count and its measurement method. Match that basis before comparing offers from different suppliers.')],
}


FAQ.update({
 'castor-seeds':[('Is this an edible seed?','No. Castor seeds are listed for industrial oil extraction only. They are toxic and must not be used as food or animal feed. Share your industrial application and handling requirements with the enquiry.')],
 'canary-seeds':[('What is the intended application?','This listing is for bird-feed ingredient sourcing. Declare origin, crop year, purity, moisture, other-seed limits and the required feed-quality tests with your offer.')],
 'watermelon-seeds':[('Should suppliers offer in-shell seed or hulled kernels?','Declare the exact form, raw or processed status, size and food-quality evidence. This listing concerns human-consumption sourcing, not planting seed.')],
 'oats':[('What should an oat offer include?','State whole oats or groats, intended food or feed use, origin, crop year, moisture, test weight, defect limits and any processing or testing requirements.')],
 'berseem-seeds':[('How should berseem planting seed be described?','State variety, origin, intended growing region, germination, physical purity, other-seed limits, test date and treatment status. Provide the lot-specific reports and seed documents requested by the buyer.')],
 'red-kidney-beans':[('Which bean type and grade should I offer?','State light or dark red type, size or count and its measurement basis, origin, crop year, moisture and defect limits. Include any cooking-quality or processing requirements.')],
 'cashew':[('How should a kernel grade be quoted?','Declare whole kernels or pieces, grade, count and its units, colour, moisture, origin, packing and required food-quality analysis. Grade names alone do not establish lot quality.')],
 'saffron':[('What evidence helps assess a saffron offer?','Declare dried-thread form, origin and grade, with agreed authenticity evidence and laboratory results for required colour, aroma, flavour and moisture parameters. Provide traceable lot and packing details.')],
 'sesame-seeds-import':[('What should a sesame supplier offer include?','State natural or hulled form, colour, origin, crop year, purity, moisture, packing and the required food-quality tests. Share a sample or specification where available.')],
 'maize-import':[('What should a feed-maize supplier offer include?','State origin, crop year, grain type, moisture, broken kernels, foreign matter, damaged grain and the required feed-quality and mycotoxin analysis. Include any GMO-status declaration required by the buyer.')],
})

# Buyer questions describe the quotation process, not unconfirmed standard terms.
IDENTITY['alfalfa-seeds'] = ('Lucerne', 'Medicago sativa L.')
for _slug in ['cumin-seeds', 'fennel-seeds', 'alfalfa-seeds', 'sesame-seeds']:
    _commercial = [
        ('What is the minimum order quantity?', 'Send your trial or commercial quantity with the required grade and packing. The minimum workable quantity is confirmed in the quotation; this page does not advertise a fixed MOQ.'),
        ('Can I request a sample and lot report?', 'Yes. Include the sample quantity, delivery country and tests you need. Sample availability, courier arrangements, costs and lot documents are confirmed before dispatch.'),
        ('Which loading port and shipment lead time apply?', 'State your destination port and required shipment window. The offer will name the Indian loading port and proposed dispatch period, subject to lot readiness, testing and freight arrangements.'),
        ('Which payment terms are available?', 'Ask for the proposed payment schedule with the quotation. Payment method, currency and any bank-document conditions must be agreed before an order is confirmed.'),
    ]
    FAQ[_slug] = (FAQ[_slug][:2] + _commercial)

from confirmed_terms import update_commercial_faq
update_commercial_faq(FAQ)

def identity_html(slug):
    names=IDENTITY.get(slug)
    return f'<p class="product-identity"><strong>Also known as:</strong> {escape(names[0])}<br><strong>Botanical name:</strong> <i>{escape(names[1])}</i></p>' if names else ''

def buying_guide_html(product):
    slug,name,trade,group,*_=product
    faqs=''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in FAQ[slug])
    seed=slug in ['alfalfa-seeds','onion-seeds','berseem-seeds']
    special='For planting seeds, confirm the test date and treatment or coating declaration; follow the offered lot’s handling instructions.' if seed else 'For food ingredients, agree the intended use, required testing and offered lot’s handling instructions.'
    if slug=='castor-seeds': special='Industrial use only. Confirm safe handling and packing for toxic castor seeds; never use them as food or feed.'
    elif slug in ['canary-seeds','maize','maize-import']: special='For feed products, agree the intended application, feed-quality testing and lot-specific storage and handling instructions.'
    elif slug=='oats': special='Confirm food or feed use, required testing and the offered lot’s storage and handling instructions.'
    return f'''<section class="buying-guide wrap" aria-label="{escape(name)} buyer questions"><div class="section-heading"><div><span class="eyebrow">PRACTICAL BUYING DETAILS</span><h2>Before you choose a lot.</h2></div><p>Match the product, specification and commercial terms.</p></div><div class="buyer-guide-grid"><div><h3>Product questions</h3>{faqs}</div><aside class="buyer-checklist"><h3>{'For your export enquiry' if trade=='export' else 'For your supplier offer'}</h3><ul><li>Product form, grade and intended use</li><li>Origin, crop year and lot or sample reference</li><li>Target quality values and required test methods</li><li>Net quantity, bag or container size and liner preference</li><li>Destination or origin port and shipment period</li><li>Required documents and any sample request</li></ul><h3>Packing, storage & shelf life</h3><p>Tell us the packing format and net weight you require. Bag construction, liner, labelling and pallet requirements are agreed with the offer. Confirm the lot’s storage conditions, shelf life or relevant dates rather than assuming a standard duration.</p><p>{escape(special)}</p><a class="text-link" href="/contact/?product={slug}&intent={'buy' if trade=='export' else 'supply'}">Send your requirement →</a></aside></div></section>'''

# Search-focused buyer questions (added 24 Nov 2026; sources noted in answers)
FAQ['cumin-seeds'] = [
 ('Where does Indian cumin (jeera) come from?', 'More than 90% of India’s cumin is grown in Gujarat and Rajasthan. Most of it is traded at Unjha APMC in Mehsana district, Gujarat, which is known as Asia’s largest cumin market. Shiva Exim is based in Mehsana, close to Unjha.'),
 ('When is new-crop cumin available for export?', 'In India, cumin is sown in October–November and harvested from February. Fresh arrivals at Unjha usually peak from February to April. Tell us your shipment month so we can plan the lot.'),
 ('What is the HS code for whole cumin seeds?', 'Whole cumin seeds (neither crushed nor ground) fall under HS 0909.31. Indian export shipping bills commonly use ITC-HS 09093129 or 09093121. Confirm the code your customs broker needs with the quotation.'),
 ('Which countries buy Indian cumin seeds?', 'India exports cumin mainly to the Gulf, the USA, Europe, China and Latin America. In Europe, the largest buyers of Indian cumin include importers in the UK, the Netherlands, Spain and Germany.'),
] + FAQ['cumin-seeds']
FAQ['alfalfa-seeds'] = [
 ('How much alfalfa (lucerne) seed is needed per acre?', 'Tamil Nadu Agricultural University gives a seed rate of 20 kg per hectare for fodder lucerne, about 8 kg per acre, sown in lines 25 cm apart. Confirm a local recommendation for your region and variety.'),
 ('How soon can alfalfa be cut for fodder, and how often?', 'Per the same TNAU guide, the first harvest is 60–65 days after sowing, then every 20–25 days, giving 12–14 harvests and 90–130 tonnes of green fodder per hectare per year under its conditions.'),
 ('Which markets does Shiva Exim supply alfalfa seed to?', 'Shiva Exim exports alfalfa (lucerne) planting seed from Gujarat, India to buyers in Europe, Pakistan and the Gulf. Import rules for planting seed differ by country; we confirm phytosanitary and seed documents for each destination.'),
] + FAQ['alfalfa-seeds']
