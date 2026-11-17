"""Reference sowing rates, distinct from specifications of offered seed lots."""
from html import escape

GUIDANCE = {
    'alfalfa-seeds': {
        'rate': '20 kg/hectare (approximately 8.1 kg/acre)',
        'method': 'Lucerne grown for fodder; the cited Tamil Nadu Agricultural University guide describes line sowing at 25 cm row spacing.',
        'scope': 'An Indian extension reference for establishing a fodder stand. Confirm the rate for your variety, growing region, sowing method and seed treatment or coating. Single-year and multi-year commercial labels do not establish separate sowing rates.',
        'url': 'https://agritech.tnau.ac.in/agriculture/foragecrops_fodder_lucerne_crop%20production.html',
        'source': 'TNAU — Lucerne fodder crop production',
    },
    'onion-seeds': {
        'rate': '8–12 kg/hectare of final field area (approximately 3.2–4.9 kg/acre)',
        'method': 'Seed used to raise nursery seedlings for transplanting common big / Bellary onion. The rate is based on the final transplanted field area, not the nursery-bed area.',
        'scope': 'The cited TNAU seedling-production guidance applies to a nursery-and-transplanting system. It is not a universal direct-sowing rate. Variety, day-length adaptation, germination, nursery losses and local planting density affect the final requirement.',
        'url': 'https://agritech.tnau.ac.in/horticulture/horti_vegetables_bellaryonion.html',
        'source': 'TNAU — Bellary onion, quality seedling production',
    },
}

def sowing_guidance_html(slug):
    item = GUIDANCE.get(slug)
    if not item:
        return ''
    rows = [
        ('Reference seed quantity', item['rate']),
        ('Sowing system', item['method']),
        ('How to apply this reference', item['scope']),
    ]
    body = ''.join(f'<tr><th scope="row">{escape(label)}</th><td>{escape(value)}</td></tr>' for label, value in rows)
    return f'''<section class="product-information wrap" aria-label="Sowing quantity guidance"><div class="specification-heading"><span class="eyebrow">PLANTING ENQUIRIES</span><h2>How much seed is needed for sowing?</h2><p>Reference quantities for the stated growing system. Confirm a local recommendation before ordering planting seed.</p></div><div class="specification-table-wrap"><table class="specification-table"><caption>Sowing quantity — reference guidance</caption><thead><tr><th scope="col">Detail</th><th scope="col">Guidance</th></tr></thead><tbody>{body}</tbody></table></div><p>Request a current, lot-specific germination and physical-purity report, the test date, variety identity and treatment or coating status. For alfalfa, also confirm the reported hard-seed percentage. Physical purity alone does not establish planting suitability. Seed rate is a cultivation guideline, not a minimum order quantity or a yield guarantee.</p><p class="technical-source">Agronomic reference: <a href="{escape(item['url'], quote=True)}" target="_blank" rel="noopener">{escape(item['source'])} ↗</a>. Checked 22 October 2026. Acre figures are rounded conversions using 1 hectare ≈ 2.471 acres. These Indian reference rates are not destination-specific recommendations.</p><a class="text-link" href="/contact/?product={slug}&amp;intent=buy">Share your planting area, region and variety requirement →</a></section>'''
