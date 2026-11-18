"""Gulf (GCC) buyer landing pages: /markets/ and one page per country.

Facts come from owner-confirmed terms (confirmed_product_data.json, confirmed_terms.py,
owner messages Nov 2026): Gulf is a supplied market; MOQ 1 MT; 10–15 days preparation;
T/T, L/C, PayPal; free samples (buyer pays courier); APEDA, Spices Board, FSSAI, IOPEPC.
Port names are public, stable facts. No prices, transit-time promises or stock claims.
"""
from html import escape

COUNTRIES = {
    'uae': dict(
        name='UAE', full='the United Arab Emirates', adj='UAE',
        title='Cumin & Fennel Seeds Supplier for UAE Importers',
        desc='Shiva Exim, India: cumin seeds, fennel seeds and Indian spices for importers, traders and packers in Dubai, Sharjah and Abu Dhabi. 1 MT minimum, free samples, T/T or L/C.',
        cities='Dubai, Sharjah, Abu Dhabi and Ajman',
        ports=['Jebel Ali (Dubai)', 'Khalifa Port (Abu Dhabi)', 'Khalid Port (Sharjah)'],
        buyers='spice traders, packers, wholesalers and re-exporters',
        note='Many UAE buyers re-export to nearby markets. Tell us if your shipment needs special packing, labels or documents for re-export.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'coriander-powder', 'chilli-powder', 'turmeric-powder'],
    ),
    'saudi-arabia': dict(
        name='Saudi Arabia', full='Saudi Arabia', adj='Saudi',
        title='Cumin & Fennel Seeds Supplier for Saudi Arabia Importers',
        desc='Shiva Exim, India: cumin seeds, fennel seeds, sesame and Indian spices for importers in Riyadh, Jeddah and Dammam. 1 MT minimum, free samples, T/T or L/C.',
        cities='Riyadh, Jeddah, Dammam and Makkah',
        ports=['Jeddah Islamic Port', 'King Abdulaziz Port (Dammam)'],
        buyers='spice importers, wholesalers, packers and food manufacturers',
        note='Tell us the documents and labelling your Saudi importer or authority asks for. We confirm what we can provide before you order.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'fenugreek-seeds', 'turmeric-powder', 'chilli-powder'],
    ),
    'oman': dict(
        name='Oman', full='Oman', adj='Omani',
        title='Cumin, Fennel & Alfalfa Seeds Supplier for Oman Importers',
        desc='Shiva Exim, India: cumin and fennel seeds, alfalfa seeds and onion seeds for planting, and Indian spices for importers in Muscat, Sohar and Salalah. Free samples.',
        cities='Muscat, Sohar, Salalah and Nizwa',
        ports=['Sohar Port', 'Port of Salalah', 'Port of Duqm'],
        buyers='spice traders, wholesalers, agricultural suppliers and seed dealers',
        note='Alfalfa and onion seeds for planting may need an import permit and a phytosanitary certificate. Tell us what your ministry requires before you order.',
        products=['cumin-seeds', 'fennel-seeds', 'alfalfa-seeds', 'onion-seeds', 'sesame-seeds', 'fenugreek-seeds'],
    ),
    'qatar': dict(
        name='Qatar', full='Qatar', adj='Qatari',
        title='Cumin & Fennel Seeds Supplier for Qatar Importers',
        desc='Shiva Exim, India: cumin seeds, fennel seeds and Indian spices for importers, wholesalers and packers in Doha. 1 MT minimum, free samples, T/T or L/C.',
        cities='Doha and Al Wakrah',
        ports=['Hamad Port'],
        buyers='spice importers, wholesalers, packers and food service suppliers',
        note='Tell us the documents and labelling your Qatari importer or authority asks for. We confirm what we can provide before you order.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'coriander-powder', 'turmeric-powder', 'dill-seeds'],
    ),
}


def gulf_strip():
    links = ''.join(f'<a href="/markets/{s}/">{escape(c["name"])} →</a>' for s, c in COUNTRIES.items())
    return ('<section class="gulf-strip wrap"><div><span class="eyebrow">FOR GULF BUYERS</span>'
            '<h2>Importing into the GCC?</h2><p>Pages for buyers in the UAE, Saudi Arabia, Oman and Qatar.</p></div>'
            f'<nav class="gulf-links" aria-label="Gulf country pages">{links}</nav></section>')


def _points():
    pts = [
        ('From the cumin and fennel belt', 'We are in Mehsana, North Gujarat, near the Unjha market for cumin and fennel.'),
        ('99% Europe & Singapore quality', 'Cumin and fennel in the trade grades Gulf buyers ask for. The specification is confirmed for each lot.'),
        ('Free samples', 'The sample is free. You pay only the courier charge.'),
        ('From 1 MT', 'Minimum order 1 metric tonne. Full 20-ft and 40-ft containers for larger orders.'),
        ('Registered exporter', 'APEDA, Spices Board India, FSSAI and IOPEPC. In business since 2018.'),
        ('Simple payment', 'T/T, L/C or PayPal, agreed in the quotation.'),
    ]
    return '<div class="market-points">' + ''.join(f'<div><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for a, b in pts) + '</div>'


def _cta(label):
    return ('<div class="hero-actions"><a class="button" href="/contact/?intent=buy">Send your enquiry ↗</a>'
            '<a class="button secondary" href="/contact/?intent=sample">Request a sample ↗</a>'
            f'<a class="text-link" href="https://wa.me/919099666604?text={label}" target="_blank" rel="noopener">WhatsApp us →</a></div>')


def render_markets(shell, intro, card, product_by_slug, process):
    paths = []
    # Hub page
    tiles = ''.join(
        f'<a class="market-tile" href="/markets/{s}/"><span class="eyebrow">{escape(c["name"].upper())}</span>'
        f'<h3>{escape(c["name"])}</h3><p>Ports: {escape(", ".join(c["ports"]))}</p><span class="text-link">View page →</span></a>'
        for s, c in COUNTRIES.items())
    hub = (intro('GULF (GCC) BUYERS', 'Indian cumin, fennel and seeds<br>for Gulf importers.',
                 'Shiva Exim supplies spices and seeds to buyers in the Gulf from Mehsana, Gujarat, India. Choose your country, or send us your requirement directly.')
           + f'<section class="wrap market-tiles">{tiles}</section>'
           + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">WHY SHIVA EXIM</span><h2>What Gulf buyers get from us.</h2></div></div>'
           + _points() + '</section>'
           + '<section class="wrap market-section"><p>Buying for Kuwait or Bahrain? We welcome your enquiry too. Tell us your port and requirement.</p>'
           + _cta('Hello%20Shiva%20Exim%2C%20I%20am%20a%20buyer%20in%20the%20Gulf.') + '</section>'
           + process())
    shell('markets', 'Spices & Seeds Supplier for Gulf (GCC) Importers',
          'Shiva Exim, India: cumin seeds, fennel seeds, sesame, alfalfa and onion seeds and Indian spices for importers in the UAE, Saudi Arabia, Oman, Qatar, Kuwait and Bahrain.',
          hub)
    paths.append('markets')

    for slug, c in COUNTRIES.items():
        others = ''.join(f'<a href="/markets/{s}/">{escape(o["name"])}</a>' for s, o in COUNTRIES.items() if s != slug)
        ports = ''.join(f'<li>{escape(p)}</li>' for p in c['ports'])
        wa = f'Hello%20Shiva%20Exim%2C%20I%20am%20a%20buyer%20in%20{c["name"].replace(" ", "%20")}.'
        body = (
            f'<div class="wrap breadcrumb"><a href="/">Home</a><span>/</span><a href="/markets/">Gulf buyers</a><span>/</span><span>{escape(c["name"])}</span></div>'
            + f'<section class="page-intro wrap"><span class="eyebrow">FOR IMPORTERS IN {escape(c["name"].upper())}</span>'
            + f'<h1>Cumin, fennel and Indian spices<br>for {escape(c["full"])}.</h1>'
            + f'<p>Shiva Exim is a spices and seeds exporter from Mehsana, Gujarat, India. We supply {escape(c["buyers"])} in {escape(c["cities"])}, with free samples and orders from 1 metric tonne.</p>'
            + _cta(wa) + '</section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">POPULAR WITH ' + escape(c['adj'].upper()) + ' BUYERS</span><h2>Products to start with.</h2></div><a class="text-link" href="/exports/">All export products →</a></div>'
            + '<div class="product-grid">' + ''.join(card(product_by_slug[p]) for p in c['products']) + '</div></section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">WHY SHIVA EXIM</span><h2>Why buy from us.</h2></div></div>' + _points() + '</section>'
            + f'<section class="wrap market-section market-ship"><div><span class="eyebrow">SHIPPING TO {escape(c["name"].upper())}</span><h2>From Gujarat to your port.</h2>'
            + '<p>We ship from Indian sea ports on the short sea route to the Gulf. Goods are usually ready 10–15 days after you confirm the order. Tell us your port and we quote for it.</p>'
            + f'<h3>Main ports we can quote to</h3><ul>{ports}</ul></div>'
            + '<div><h3>Packing</h3><p>25, 30 or 50 kg bags (grains 40 or 50 kg). Your own brand, liners and pallets on request.</p>'
            + '<h3>Container guide</h3><p>Cumin and fennel about 14 MT in a 20-ft container; about 28 MT in a 40-ft. Final quantity depends on packing.</p>'
            + f'<h3>Documents</h3><p>{escape(c["note"])}</p></div></section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">QUICK ANSWERS</span><h2>Before you enquire.</h2></div><a class="text-link" href="/faq/">All buyer questions →</a></div>'
            + '<div class="faq-list">'
            + '<details><summary>What is the minimum order?</summary><p>1 metric tonne for most products.</p></details>'
            + '<details><summary>Can I get a sample?</summary><p>Yes. The sample is free; you pay only the courier charge.</p></details>'
            + '<details><summary>How can I pay?</summary><p>T/T (bank transfer), L/C or PayPal. The payment schedule is agreed in the quotation.</p></details>'
            + '<details><summary>Do you show prices?</summary><p>We send a written quotation for your grade, quantity, packing and port, because spice prices change with each crop.</p></details>'
            + '</div></section>'
            + f'<section class="wrap market-section"><p class="other-markets">Other Gulf pages: {others}</p></section>'
        )
        shell('markets/' + slug, c['title'], c['desc'], body)
        paths.append('markets/' + slug)
    return paths
