"""SEO additions (Nov 2026, owner-approved):
- New export products the owner confirmed on 20 Nov 2026: all onion seed varieties
  (red, white, hybrid F1, Nasik Red N-53, desi, gavran), kalonji (nigella),
  jowar (sorghum) fodder seed and jowar for animal feed.
- Other names that buyers search for (Hindi / Gujarati / Arabic / trade names),
  shown once on each product page as 'Also known as'.
No prices, stock, germination or yield claims.
"""
from copy import deepcopy

ONION_VARIETIES = [
    ('red-onion-seeds', 'Red onion seeds', 'Red onion planting seed for bulb production in the main Indian red onion types.'),
    ('white-onion-seeds', 'White onion seeds', 'White onion planting seed for fresh-market and processing onion crops.'),
    ('hybrid-onion-seeds', 'Hybrid onion seeds (F1)', 'F1 hybrid onion planting seed for growers who want a uniform bulb crop.'),
    ('nasik-red-n53-onion-seeds', 'Nasik Red N-53 onion seeds', 'Nasik Red N-53, a well-known Indian red onion variety for kharif (monsoon-season) planting.'),
    ('desi-onion-seeds', 'Desi onion seeds', 'Traditional Indian (desi) red onion planting seed.'),
    ('gavran-onion-seeds', 'Gavran onion seeds', 'Gavran, a traditional local red onion variety from Maharashtra, India.'),
]

ONION_SPEC = 'Variety; bulb colour; germination requirement; treatment status; destination seed rules'

NEW_PRODUCTS = [
    (slug, name, 'export', 'Seeds', desc, 'Planting seeds', ONION_SPEC) for slug, name, desc in ONION_VARIETIES
] + [
    ('kalonji-seeds', 'Kalonji (nigella seeds)', 'export', 'Whole spices',
     'Kalonji, also called nigella or black seed, for spice trading, bakery and food processing.',
     'Whole seeds', 'Purity requirement; moisture; cleaning preference; packing'),
    ('jowar-fodder-seeds', 'Jowar (sorghum) fodder seeds', 'export', 'Seeds',
     'Sorghum (jowar) planting seed for green fodder crops for cattle and other livestock.',
     'Planting seeds', 'Variety; single-cut or multi-cut; germination requirement; treatment status; destination seed rules'),
    ('jowar-animal-feed', 'Jowar (sorghum) for animal feed', 'export', 'Grains & millets',
     'Sorghum (jowar) grain for animal feed and feed milling.',
     'Whole grain', 'Feed use; moisture; broken grain and foreign matter; packing'),
]

ONION_VARIETY_SLUGS = [s for s, _, _ in ONION_VARIETIES]

# Other names buyers search for. Arabic names help Gulf buyers.
OTHER_NAMES = {
    'cumin-seeds': 'Jeera (Hindi) · Jiru (Gujarati) · Kammoun / كمون (Arabic)',
    'fennel-seeds': 'Saunf (Hindi) · Variyali (Gujarati) · Shamar / شمر (Arabic)',
    'fenugreek-seeds': 'Methi (Hindi, Gujarati) · Hilba / حلبة (Arabic)',
    'dill-seeds': 'Suva / Sowa (Hindi, Gujarati) · Shibit / شبت (Arabic)',
    'cumin-powder': 'Jeera powder (Hindi) · Kammoun mathoun / كمون مطحون (Arabic)',
    'coriander-powder': 'Dhania powder (Hindi) · Kuzbara mathouna / كزبرة مطحونة (Arabic)',
    'whole-chilli': 'Lal mirch, dry red chilli (Hindi) · Filfil ahmar / فلفل أحمر (Arabic)',
    'chilli-powder': 'Lal mirch powder, red chilli powder (Hindi) · فلفل أحمر مطحون (Arabic)',
    'turmeric': 'Haldi (Hindi) · Turmeric finger · Kurkum / كركم (Arabic)',
    'turmeric-powder': 'Haldi powder (Hindi) · Kurkum mathoun / كركم مطحون (Arabic)',
    'dry-ginger': 'Sonth / Soonth (Hindi) · Dried ginger · زنجبيل مجفف (Arabic)',
    'alfalfa-seeds': 'Lucerne · Rajka / Rijka (Hindi, Gujarati) · Barseem hijazi / برسيم حجازي (Arabic)',
    'onion-seeds': 'Pyaz ke beej (Hindi) · Dungli na biya (Gujarati) · Kanda beej · بذور البصل (Arabic)',
    'sesame-seeds': 'Til (Hindi, Gujarati) · Simsim / سمسم (Arabic)',
    'mustard-seeds': 'Rai / Sarson (Hindi) · Khardal / خردل (Arabic)',
    'wheat': 'Gehun / Ghau (Hindi, Gujarati) · Qamh / قمح (Arabic)',
    'maize': 'Makka (Hindi) · Corn · Dhura safra / ذرة صفراء (Arabic)',
    'foxtail-millet': 'Kangni / Kang (Hindi) · Italian millet',
    'green-millet': 'Bajra (Hindi, Gujarati) · Pearl millet · Dukhn / دخن (Arabic)',
    'castor-seeds': 'Erandi / Arandi (Hindi) · Divela (Gujarati) · Khirwa / خروع (Arabic)',
    'kalonji-seeds': 'Nigella sativa · Black seed · Black cumin · Kalonji (Hindi) · Habbat al-barakah / حبة البركة (Arabic)',
    'jowar-fodder-seeds': 'Sorghum · Chari (fodder) · Jowar / Juwar (Hindi, Gujarati) · Dhura rafia / ذرة رفيعة (Arabic)',
    'jowar-animal-feed': 'Sorghum · Milo · Jowar (Hindi, Gujarati) · Dhura rafia / ذرة رفيعة (Arabic)',
    'red-onion-seeds': 'Lal pyaz ke beej (Hindi) · Red onion seed',
    'white-onion-seeds': 'Safed pyaz ke beej (Hindi) · White onion seed',
    'hybrid-onion-seeds': 'F1 hybrid onion seed',
    'nasik-red-n53-onion-seeds': 'N-53 · Nashik Red · Nasik N53 onion seed',
    'desi-onion-seeds': 'Local onion seed · Desi pyaz beej',
    'gavran-onion-seeds': 'Gavran kanda beej · Local Maharashtra onion seed',
    # Imports
    'oats': 'Jai (Hindi) · Oat grain · Shoufan / شوفان (Arabic)',
    'berseem-seeds': 'Egyptian clover · Barseem / برسيم (Arabic)',
    'chickpeas': 'Kabuli chana (Hindi)',
    'black-gram': 'Urad (Hindi)',
    'whole-lentils': 'Masoor (Hindi)',
    'split-lentils': 'Masoor dal (Hindi)',
    'green-peas': 'Hara matar (Hindi)',
    'yellow-peas': 'Peela matar (Hindi)',
    'red-kidney-beans': 'Rajma (Hindi)',
    'soybean': 'Soya (Hindi)',
    'sunflower-seeds': 'Surajmukhi beej (Hindi)',
    'pumpkin-seeds': 'Kaddu ke beej (Hindi)',
    'saffron': 'Kesar (Hindi)',
    'cashew': 'Kaju (Hindi)',
    'olive-oil': 'Jaitun tel (Hindi)',
}


def search_aliases():
    """Plain words for the catalogue search box."""
    import re
    return {k: re.sub(r'[^A-Za-z0-9 \-]', ' ', v).replace(' - ', ' ') for k, v in OTHER_NAMES.items()}


def install(details, faq):
    """Add DETAILS and FAQ entries for the new products."""
    onion = details['onion-seeds']
    for slug, name, desc in ONION_VARIETIES:
        d = deepcopy(onion)
        d['description'] = desc + ' ' + onion['description']
        details[slug] = d
        faq[slug] = [
            ('What should I send for a ' + name.lower() + ' enquiry?',
             'Tell us the variety, quantity, packing, destination country and the germination, purity and treatment '
             'requirements of your country. We confirm the seed lot, documents and price in the quotation.'),
            ('Are onion seeds the same as kalonji?',
             'No. Onion seeds are planting seed for growing onions. Kalonji (nigella) is a spice that is sometimes '
             'sold as "black onion seed". We supply both; please say which one you need.'),
        ]
    details['kalonji-seeds'] = {
        'description': 'Kalonji (Nigella sativa), also called nigella or black seed, is a small black, angular spice seed used whole in breads, pickles and spice blends, and for black seed oil. It is sometimes called "black onion seed", but it is not onion planting seed.',
        'uses': 'Bakery and breads; pickles and spice blends; food processing; black seed oil pressing.',
        'rows': list(details['fenugreek-seeds']['rows']),
        'note': '',
    }
    faq['kalonji-seeds'] = [
        ('What should a kalonji enquiry include?',
         'Purity, moisture, cleaning (machine clean or sortex), packing, quantity and destination. Tell us any test '
         'reports your buyer or authority needs.'),
        ('Is kalonji the same as onion seed?',
         'No. Kalonji is the spice nigella, sometimes called "black onion seed" in trade. Onion seed for planting is a '
         'different product, which we also export.'),
    ]
    details['jowar-fodder-seeds'] = {
        'description': 'Jowar (sorghum) fodder seed is planting seed for green fodder crops for cattle, buffalo, camels and other livestock. Buyers should specify the variety type (single-cut or multi-cut), germination target, treatment and the seed rules of the destination country.',
        'uses': 'Green fodder and silage crops; livestock farms; fodder seed distribution.',
        'rows': list(onion['rows'][2:]) if len(onion['rows']) > 2 else list(onion['rows']),
        'note': 'For planting use. Confirm variety, growing conditions, treatment and destination seed documentation before ordering.',
    }
    faq['jowar-fodder-seeds'] = [
        ('What should a jowar fodder seed enquiry include?',
         'Variety type (single-cut or multi-cut), quantity, packing, destination and your germination, purity and '
         'treatment requirements. Seed documents for your country are confirmed before the order.'),
    ]
    details['jowar-animal-feed'] = deepcopy(details['maize'])
    details['jowar-animal-feed']['description'] = 'Shiva Exim lists sorghum (jowar) grain for animal feed. Buyers should provide the feed-grain specification, including moisture, broken grain, foreign matter, damaged grain and required contaminant testing.'
    details['jowar-animal-feed']['uses'] = 'Animal and poultry feed; feed milling and compound-feed processing.'
    details['jowar-animal-feed']['rows'] = [r for r in details['maize']['rows'] if 'GMO' not in r[0]]
    details['jowar-animal-feed']['rows'][0] = ('Intended use', 'Animal feed', 'This listing is for feed grain, not planting seed.')
    details['jowar-animal-feed']['note'] = 'This is a feed-grain enquiry, not planting seed. Feed-quality requirements and lot evidence are confirmed before an order.'
    faq['jowar-animal-feed'] = [
        ('What should a jowar animal-feed enquiry include?',
         'Moisture, broken grain and foreign matter limits, any feed analysis or mycotoxin tests, packing, quantity '
         'and destination.'),
    ]


def also_known(slug):
    from html import escape
    v = OTHER_NAMES.get(slug)
    return f'<p class="also-known"><span>Also known as:</span> {escape(v)}</p>' if v else ''


def onion_variety_block(current):
    from html import escape
    items = [('onion-seeds', 'All onion seeds')] + [(s, n) for s, n, _ in ONION_VARIETIES]
    links = ''.join(
        f'<a href="/products/{s}/"{" aria-current=\"page\"" if s == current else ""}>{escape(n)}</a>' for s, n in items)
    return ('<section class="onion-varieties wrap"><div><span class="eyebrow">ONION SEED VARIETIES</span>'
            '<h2>Onion seeds we export.</h2><p>Red, white, hybrid (F1), Nasik Red N-53, desi and gavran onion planting seed. '
            'Tell us the variety and quantity, and we quote with the seed lot details.</p></div>'
            f'<nav aria-label="Onion seed varieties">{links}</nav></section>')
