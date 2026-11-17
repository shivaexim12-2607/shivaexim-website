"""Selected product photography and downloadable guides, without stock claims."""
from html import escape
import json
from pathlib import Path

MEDIA = {
    'cumin-seeds': {
        'name': 'Cumin seeds', 'botanical': 'Cuminum cyminum',
        'author': 'Sanjay Acharya',
        'source': 'https://commons.wikimedia.org/wiki/File:Sa_cumin.jpg',
        'license': 'CC BY-SA 3.0',
        'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/',
        'options': '99% Europe quality; 99% Singapore quality',
        'intro': 'Whole cumin for spice trading, grinding, seasoning blends and food processing.',
        'rows': [('Product form', 'Whole seeds'), ('Purity and foreign matter', 'Target limits and lot results confirmed with quotation'), ('Moisture', 'Maximum limit confirmed with quotation'), ('Cleaning and appearance', 'Cleaning level, colour and damaged-seed limits agreed'), ('Aroma / volatile oil', 'Required test and acceptance limit agreed'), ('Packing and quantity', 'Bag size, liner, net quantity and labelling agreed')],
    },
    'fennel-seeds': {
        'name': 'Fennel seeds', 'botanical': 'Foeniculum vulgare',
        'author': 'Sanjay Acharya',
        'source': 'https://commons.wikimedia.org/wiki/File:Fennel-seeds.jpg',
        'license': 'CC BY-SA 3.0',
        'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/',
        'options': '99% Europe quality; 99% Singapore quality',
        'intro': 'Aromatic whole fennel for seasoning, food ingredients, grinding and spice distribution.',
        'rows': [('Product form', 'Whole seeds'), ('Purity and foreign matter', 'Target limits and lot results confirmed with quotation'), ('Moisture', 'Maximum limit confirmed with quotation'), ('Seed size and colour', 'Sieve / size requirement and colour or sample agreed'), ('Aroma / volatile oil', 'Required test and acceptance limit agreed'), ('Packing and quantity', 'Bag size, liner, net quantity and labelling agreed')],
    },
    'alfalfa-seeds': {
        'name': 'Alfalfa seeds', 'botanical': 'Medicago sativa',
        'author': 'Tracey Slotta / USDA-NRCS PLANTS Database',
        'source': 'https://commons.wikimedia.org/wiki/File:Mesas_001_lhp.jpg',
        'license': 'Public domain (USDA)',
        'license_url': 'https://commons.wikimedia.org/wiki/File:Mesas_001_lhp.jpg#Licensing',
        'options': 'Single-year quality; Multi-year quality',
        'intro': 'Planting-seed enquiries for establishing a fodder crop. Confirm the variety and intended growing region.',
        'rows': [('Intended use', 'Fodder planting; not a food or sprouting-seed offer'), ('Variety and crop year', 'Identity, harvest year and growing-region suitability confirmed'), ('Germination and hard seeds', 'Lot test results, test date and acceptance limits agreed'), ('Physical purity and moisture', 'Lot results and limits for other seeds / inert matter agreed'), ('Treatment and documentation', 'Treatment declaration, tests and destination certificates confirmed'), ('Packing and quantity', 'Bag size, net quantity, labels and shipment terms agreed')],
    },
}

PHOTO_MANIFEST = Path(__file__).with_name('product_photos.json')
PHOTOGRAPHS = {**MEDIA, **(json.loads(PHOTO_MANIFEST.read_text()) if PHOTO_MANIFEST.exists() else {})}

def render_card_photo(slug):
    if slug not in PHOTOGRAPHS:
        return ''
    m = PHOTOGRAPHS[slug]
    subject = m.get('subject', m['name'].lower())
    return f'<figure class="card-photo"><img src="/assets/products/{slug}-thumb.webp" alt="Representative photograph of {escape(subject)}" width="500" height="330" loading="lazy"></figure>'

def needs_credit(m):
    """CC0 and public-domain photos need no attribution; CC BY / BY-SA photos do."""
    lic = m.get('license', '').lower()
    return not (lic.startswith('cc0') or lic.startswith('public domain'))

def credit_caption(m):
    note = m.get('photo_note', 'Representative photograph; not the offered lot.')
    if not needs_credit(m):
        return f'<figcaption>{escape(note)}</figcaption>'
    return f'''<figcaption>{escape(note)}<br>Photo: {escape(m['author'])} · <a href="{escape(m['source'])}" target="_blank" rel="noopener">Source</a> · <a href="{escape(m['license_url'])}" target="_blank" rel="noopener">{escape(m['license'])}</a> · resized and converted to WebP.</figcaption>'''

def render_photo_credits():
    items = []
    for slug, m in PHOTOGRAPHS.items():
        if not needs_credit(m):
            continue
        items.append(f'''<li><a href="/products/{slug}/">{escape(m['name'])}</a> — {escape(m['author'])}. <a href="{escape(m['source'])}">Original source</a> · <a href="{escape(m['license_url'])}">{escape(m['license'])}</a>. Resized and converted to WebP; the photograph retains its stated licence.</li>''')
    return '<section class="prose wrap"><p>Product photographs illustrate the product category and do not show a specific offered lot, grade, size, origin or certification. Photo credits and licences are also shown on each product page. No photographer endorsement is implied.</p><ul class="photo-credit-list">'+''.join(items)+'</ul></section>'

def render_media(slug, product=None):
    if slug not in MEDIA:
        if slug not in PHOTOGRAPHS:
            return ''
        m = PHOTOGRAPHS[slug]
        subject = m.get('subject', m['name'].lower())
        desc = product[4] if product else 'Discuss the product specification and shipment requirements with Shiva Exim.'
        form = product[5] if product else 'Confirmed with quotation'
        intent = 'supply' if product and product[2] == 'import' else 'buy'
        return f'''<section class="product-visual wrap" aria-label="{escape(m['name'])} product photograph"><figure><img src="/assets/products/{slug}.webp" alt="Representative photograph of {escape(subject)}" loading="lazy" width="900" height="600">{credit_caption(m)}</figure><div><span class="eyebrow">A CLOSER LOOK</span><h2>{escape(m['name'])}</h2><p>{escape(desc)}</p><p><strong>Product form:</strong> {escape(form)}</p><a class="button" href="/contact/?product={slug}&amp;intent={intent}">Discuss your specification ↗</a><p class="small muted">Confirm the exact form, grade, sample, packing and destination requirements with your quotation.</p></div></section>'''
    m = MEDIA[slug]
    return f'''<section class="product-visual wrap" aria-label="{escape(m['name'])} photograph and product guide"><figure><img src="/assets/products/{slug}.webp" alt="Representative photograph of {escape(m['name'].lower())} ({m['botanical']})" loading="lazy" width="900" height="600">{credit_caption(m)}</figure><div><span class="eyebrow">TAKE THE DETAILS WITH YOU</span><h2>A clear start to your enquiry.</h2><p>Download the product and specification guide for {escape(m['name'].lower())}. It includes listed quality options, the details to agree for each lot and our contact information.</p><a class="button" href="/downloads/{slug}-product-guide.pdf" download>Download product guide (PDF) ↓</a><p class="small muted">Detailed quality limits, packing, testing and documents are confirmed with the quotation. This guide is not a lot certificate or a stock offer.</p></div></section>'''
