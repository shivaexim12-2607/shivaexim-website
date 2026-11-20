"""Confirmed company facts and search metadata; no placeholder offer terms."""
import json
from html import escape
from product_buying_guides import FAQ

ALIASES = {'cumin-seeds': 'Cumin seeds (Jeera)', 'fennel-seeds': 'Fennel seeds (Saunf)', 'alfalfa-seeds': 'Alfalfa seeds (Lucerne)', 'onion-seeds': 'Onion seeds'}
PRIORITY = {'cumin-seeds', 'fennel-seeds', 'alfalfa-seeds', 'onion-seeds', 'sesame-seeds'}

def product_metadata(product):
    slug, name, trade, group, description, *_ = product
    label = ALIASES.get(slug, name)
    if trade == 'import':
        return f'{name} Import Sourcing for India', f'Supply {name.lower()} to Shiva Exim for the Indian market. Send origin, specification, crop year, packing, quantity and shipment terms for review.', label
    title = f'{label} Exporter from India'
    desc = f'{name} from Shiva Exim, an agricultural exporter in Mehsana, Gujarat, India. Discuss your specification, packing, quantity and destination.'
    if slug in {'cumin-seeds', 'fennel-seeds'}:
        word = 'Cumin' if slug == 'cumin-seeds' else 'Fennel'
        title = f'{label} Exporter from India — Gujarat'
        desc = f'{word} exporter in Mehsana, Gujarat, India: {label.lower()} in 99% Europe and 99% Singapore quality. Request a lot specification, sample and export quotation.'
    elif slug == 'alfalfa-seeds':
        title = 'Alfalfa Seeds (Lucerne) Exporter & Supplier from India'
        desc = 'Alfalfa (lucerne) seeds exporter and supplier from Gujarat, India: export-quality fodder planting seed, single-year and multi-year. Germination, purity and phytosanitary documents agreed per lot. Free samples, 1 MT minimum.'
    elif slug == 'onion-seeds':
        title = 'Onion Seeds Exporter & Supplier from India — Gujarat'
        desc = 'Onion seeds exporter and supplier from Gujarat, India: export-quality onion planting seed. Germination, purity and phytosanitary documents agreed per lot. Free samples, 1 MT minimum.'
    return title, desc, label

def product_opening(product):
    slug, name, trade, *_ = product
    if trade == 'import':
        return f'Shiva Exim sources {name.lower()} for the Indian market and welcomes supplier offers with origin, quality and shipment details.'
    if slug in {'cumin-seeds', 'fennel-seeds'}:
        label = ALIASES[slug].lower()
        return f'Shiva Exim is a {label} exporter based in Mehsana, Gujarat, India, with listed 99% Europe quality and 99% Singapore quality options.'
    if slug == 'alfalfa-seeds':
        return 'Shiva Exim is an alfalfa (lucerne) planting seed exporter based in Mehsana, Gujarat, India. Variety, germination and lot documentation are assessed for the buyer’s intended growing region.'
    if slug == 'onion-seeds':
        return 'Shiva Exim is an onion seed exporter based in Mehsana, Gujarat, India, supplying onion planting seed for crop production. Variety, germination and lot documentation are confirmed for the buyer’s growing region.'
    return f'Shiva Exim lists {name.lower()} in its export portfolio. Share the product specification, quantity and destination for a quotation.'

def regional_context():
    return '<div class="regional-context"><h3>Mehsana and the Unjha spice market</h3><p>Our business is based in Mehsana, North Gujarat, near Unjha’s established cumin and fennel trading market. Compare origin, crop year and a representative sample when assessing an offer.</p><p class="small">Market context: <a href="https://www.apmcunjha.com/index.php/market" target="_blank" rel="noopener">APMC Unjha describes its cumin and fennel trade ↗</a>.</p></div>'

def commercial_overview(product):
    slug, name, trade, *_ = product
    if slug not in PRIORITY:
        return ''
    quality = '99% Europe quality · 99% Singapore quality' if slug in {'cumin-seeds','fennel-seeds'} else 'Single-year quality · Multi-year quality; confirm variety and seed report' if slug == 'alfalfa-seeds' else 'Planting seed for onion crop production; confirm variety, germination and seed report' if slug == 'onion-seeds' else 'Natural or hulled; specify colour and intended use'
    return '<section class="commercial-overview wrap"><div class="section-heading"><div><span class="eyebrow">BUYER QUICK VIEW</span><h2>Your starting specification.</h2></div></div><dl><div><dt>Product / quality options</dt><dd>'+escape(quality)+'</dd></div><div><dt>Business location</dt><dd>Mehsana, Gujarat, India</dd></div><div><dt>Markets we supply</dt><dd>Gulf: <a href="/markets/uae/">UAE</a> · <a href="/markets/saudi-arabia/">Saudi Arabia</a> · <a href="/markets/oman/">Oman</a> · <a href="/markets/qatar/">Qatar</a>; also Europe, South Asia and Africa</dd></div><div><dt>For a useful quotation</dt><dd>Grade, target test limits, packing, quantity, destination and shipment window</dd></div></dl><p class="small">Commercial grade names identify enquiry options. The offered lot’s analysis and final contract determine its specification.</p></section>'

def product_schema(product, base, description):
    slug, name, trade, group, *_ = product
    url = f'{base}/products/{slug}/'
    label = ALIASES.get(slug, name)
    # These are enquiry pages without public prices, reviews or ratings.
    # Describe the page rather than claiming Product rich-result eligibility.
    graph = [{
        '@type':'WebPage', '@id':url+'#webpage', 'name':label,
        'description':description, 'url':url,
        'about':{'@type':'Thing','name':label},
        'primaryImageOfPage':{'@type':'ImageObject','url':f'{base}/assets/products/{slug}.webp'},
        'breadcrumb':{'@id':url+'#breadcrumb'},
        'publisher':{'@type':'Organization','name':'Shiva Exim','url':base},
    }, {
        '@type':'BreadcrumbList', '@id':url+'#breadcrumb',
        'itemListElement':[
            {'@type':'ListItem','position':1,'name':'Home','item':base+'/'},
            {'@type':'ListItem','position':2,'name':'Exports' if trade=='export' else 'Imports','item':f'{base}/{trade}s/'},
            {'@type':'ListItem','position':3,'name':label,'item':url},
        ],
    }]
    if FAQ.get(slug):
        graph.append({'@type':'FAQPage','@id':url+'#buyer-questions','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ[slug]]})
    return '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('</','<\\/')+'</script>'

ARTICLE_POINTS = {
 'october-2026-cumin-fennel-sesame-crop-outlook':[
    'Rainfall is one supply risk; acreage, irrigation and carryover also matter.',
    'Earlier crop-year estimates do not establish the size of the 2027 harvest.',
    'Shiva Exim’s 2027 outlook is provisional; several origin-level data gaps remain.',
 ],
 'comparing-cumin-fennel-sesame-export-quotes':[
    'Compare the same product form, origin, crop year and quality specification.',
    'Commercial grade names do not replace lot testing or destination requirements.',
    'Match currency, packing, shipment basis and quote validity before comparing prices.',
 ],
 'november-2026-spice-watch-sowing-risk-sesame-supply':[
    'IMD’s November outlook is a weather forecast, not a confirmed crop shortage.',
    'The Brazilian sesame figure discussed is an estimate, not a measure of export-ready stock.',
    'The 2027 company outlook remains provisional pending acreage, irrigation and harvest evidence.',
 ],
}

def article_takeaways(post):
    points = ARTICLE_POINTS.get(post['slug'])
    if not points:
        return ''
    return '<aside class="article-takeaways" aria-label="Article key points"><h2>Key points</h2><ul>'+''.join('<li>'+escape(p)+'</li>' for p in points)+'</ul></aside>'
