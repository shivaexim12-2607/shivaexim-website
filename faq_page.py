"""Buyer FAQ page. Answers use only owner-confirmed terms (confirmed_product_data.json,
confirmed_terms.py and owner messages of November 2026). No prices, stock or delivery promises."""
import json
from html import escape

SECTIONS = [
    ('Samples', [
        ('Can I get a sample before I order?',
         'Yes. We send samples of our export products. The sample itself is free; you pay only the courier charge. '
         'Tell us the product, grade, sample quantity and your full courier address.'),
        ('How do I request a sample?',
         'Use the “Request a sample” button on any export product page, or choose “Request a sample” in the contact form. '
         'The form prepares an email or WhatsApp message that you send to us. You can also write to info@shivaexim.com '
         'or WhatsApp +91 9099666604.'),
        ('Can you send a lab report with the sample?',
         'Tell us which tests you need, for example purity, moisture or pesticide residue. Lot reports and testing are '
         'agreed for the specific offer before you confirm an order.'),
    ]),
    ('Ordering & price', [
        ('What is the minimum order quantity (MOQ)?',
         'Our minimum order is 1 metric tonne for most export products. Larger orders are usually shipped in 20-ft or 40-ft containers.'),
        ('Why are there no prices on the website?',
         'Spice and seed prices change with each crop and market. We send a written quotation for your grade, quantity, '
         'packing and destination, so the price you receive is the price for your order.'),
        ('What should I include in my enquiry?',
         'Product and grade, quantity, packing, destination country and port, preferred shipment month, and any documents '
         'or tests you need. With these details we can quote quickly and correctly.'),
        ('Do you supply 99% Europe and 99% Singapore quality cumin and fennel?',
         'Yes. Cumin and fennel are our main products, in 99% Europe and 99% Singapore quality (minimum 99% purity, '
         'maximum 7% moisture for cumin). These are trade quality names, not certificates; the specification is '
         'confirmed for each lot.'),
    ]),
    ('Packing & shipping', [
        ('What packing do you offer?',
         'Most products are packed in 25 kg, 30 kg or 50 kg bags; grains and millets in 40 kg or 50 kg bags. '
         'Custom packing, your own branding, liners and pallets can be arranged.'),
        ('How much fits in one container?',
         'As a guide: cumin and fennel about 14 MT in a 20-ft container; heavier products such as alfalfa, sesame, '
         'mustard, wheat or maize about 22–24 MT in a 20-ft; and about 28 MT in a 40-ft. The final quantity depends '
         'on packing and shipping-line limits.'),
        ('How long does it take to ship?',
         'Usually 10–15 days after the order is confirmed to prepare the goods. Transit time depends on your port '
         'and the shipping line.'),
        ('From which port do you ship?',
         'We ship from Indian sea ports. The loading port is agreed in the quotation.'),
        ('Which countries do you supply?',
         'We supply buyers in the Gulf (GCC), Europe, Pakistan, other South Asian markets and Africa. Our seeds, including alfalfa, go to Europe, Pakistan and the Gulf, and we welcome new buyers from other countries.'),
    ]),
    ('Payment', [
        ('Which payment terms do you accept?',
         'T/T (bank transfer), L/C (letter of credit) and PayPal. The payment schedule and currency are agreed in the '
         'quotation before you confirm the order.'),
    ]),
    ('Company & documents', [
        ('Is Shiva Exim a registered exporter?',
         'Yes. Shiva Exim was established in 2018 in Mehsana, Gujarat, India. We are registered with APEDA, '
         'Spices Board India, FSSAI and IOPEPC, and hold an Import Export Code (IEC). Registration details are '
         'shared for your transaction on request.'),
        ('Which export documents can you provide?',
         'Tell us the documents your country requires, for example a phytosanitary certificate, certificate of origin '
         'or lab analysis. We confirm what can be provided for your shipment before you place the order.'),
        ('Do you also import products into India?',
         'Yes. We also import seeds, pulses and agricultural products for the Indian market. Suppliers can send offers '
         'through the Imports section or the contact form.'),
    ]),
]


def faq_body(base):
    nav = ''.join(f'<a href="#faq-{i}">{escape(t)}</a>' for i, (t, _) in enumerate(SECTIONS))
    blocks = ''
    for i, (title, qs) in enumerate(SECTIONS):
        items = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in qs)
        blocks += f'<div class="faq-group" id="faq-{i}"><h2>{escape(title)}</h2>{items}</div>'
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for _, qs in SECTIONS for q, a in qs
        ],
    }
    intro = ('<section class="page-intro wrap"><span class="eyebrow">BUYER FAQ</span>'
             '<h1>Questions buyers ask us.</h1>'
             '<p>Samples, minimum order, packing, shipping and payment, in one place. '
             'Can’t find your answer? Send us a message.</p>'
             '<div class="hero-actions"><a class="button" href="/contact/?intent=sample">Request a sample ↗</a>'
             '<a class="text-link" href="/contact/">Ask a question →</a></div></section>')
    return (intro
            + f'<section class="faq-page wrap"><nav class="faq-nav" aria-label="FAQ topics">{nav}</nav>'
            + f'<div class="faq-list">{blocks}</div></section>'
            + f'<script type="application/ld+json">{json.dumps(schema)}</script>')
