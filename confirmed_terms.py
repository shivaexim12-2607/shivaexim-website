"""Owner-supplied website details, received 9 November 2026.

Source: Shiva_Exim_Website_Information.numbers, completed 6 November 2026.
Only clear, public-approved product fields are included. Bag-count entries,
ambiguous experience/address entries and unavailable certificate numbers are omitted.
"""
import json
from pathlib import Path
from html import escape

PRODUCT_DATA=json.loads((Path(__file__).parent/'confirmed_product_data.json').read_text())

def specification_rows(record):
    rows=[]
    if record.get('origins'): rows.append(('Origin options', ' / '.join(record['origins'])))
    if record.get('crop'): rows.append(('Crop / harvest',record['crop']))
    if 'purity_min' in record: rows.append(('Minimum purity',f"{record['purity_min']:g}%"))
    if 'moisture_max' in record: rows.append(('Maximum moisture',f"{record['moisture_max']:g}%"))
    return rows

def commercial_rows(record):
    rows=[]
    if record.get('packing_kg'): rows.append(('Packing', ' / '.join(map(str,record['packing_kg']))+' kg bags'+(' · '+record['bag_material'].lower() if record.get('bag_material') else '')))
    if record.get('custom_packing'): rows.append(('Custom packing','Available by arrangement; confirm branding, liner and pallet requirements'))
    if 'moq_mt' in record: rows.append(('Minimum order',f"{record['moq_mt']:g} metric tonne"))
    for key,label in [('payload_20_mt','Indicative 20-ft loading'),('payload_40_mt','Indicative 40-ft loading')]:
        if key in record: rows.append((label,f"{record[key]:g} MT; final loading depends on packing, volume and carrier limits"))
    for key,label in [('port','Ports'),('lead_time','Preparation time'),('payments','Payment options'),('samples','Samples')]:
        if record.get(key): rows.append((label,record[key]))
    return rows

def confirmed_product_html(product):
    slug,name,trade,*_=product
    records=PRODUCT_DATA.get(slug,[])
    if not records:return ''
    intro='Origin and packing preferences for supplier offers to the Indian market.' if trade=='import' else 'Listed origin options, specifications and commercial terms for your enquiry.'
    def table(rows):
        return '<dl>'+''.join('<div><dt>'+escape(k)+'</dt><dd>'+escape(v)+'</dd></div>' for k,v in rows)+'</dl>'
    html='<section class="confirmed-product wrap" aria-label="'+escape(name)+' confirmed enquiry details"><div class="section-heading"><div><span class="eyebrow">PRODUCT &amp; TRADE DETAILS</span><h2>Plan your '+('supplier offer' if trade=='import' else 'order')+'.</h2></div><p>'+intro+'</p></div><div class="confirmed-grades">'
    for r in records:
        html+='<div class="confirmed-grade"><h3>'+escape(r['grade'])+'</h3>'+table(specification_rows(r))+'</div>'
    html+='</div><h3>Packing and shipment</h3>'+table(commercial_rows(records[0]))
    if any(r.get('payload_20_mt') or r.get('payload_40_mt') for r in records):
        html+='<p class="small muted">Container quantities are indicative planning figures, not guaranteed loading capacities. Confirm the final packing plan, applicable shipment requirements and freight booking.</p>'
    html+='<p class="small muted">Origin options do not imply current stock. The quotation identifies the offered origin, harvest year, lot specification and final commercial terms. Overseas-origin products are identified separately from the Indian shipment location.</p></section>'
    return html

def update_commercial_faq(faq):
    for slug in ['cumin-seeds','fennel-seeds','alfalfa-seeds','sesame-seeds']:
        answers={
          'What is the minimum order quantity?':'Our listed minimum order is 1 metric tonne. Confirm your grade, packing and destination with the quotation.',
          'Can I request a sample and lot report?':'Samples are available without a product charge; shipping costs apply. State the sample quantity and required tests. Lot reports and dispatch arrangements are confirmed for the proposed offer.',
          'Which loading port and shipment lead time apply?':'Indian loading ports can be arranged with the quotation. Usual preparation is 10–15 days after order confirmation; final dispatch depends on the agreed specification, documents and freight arrangements.',
          'Which payment terms are available?':'T/T, L/C and PayPal are listed payment options. The payment schedule, currency and method must be agreed in the quotation before an order is confirmed.',
        }
        faq[slug]=[(q,answers.get(q,a)) for q,a in faq[slug]]

def company_html(address, office_hours):
    return '''<section class="about-content wrap"><div><span class="eyebrow">ESTABLISHED IN 2018</span><h2>Agricultural trade with a clear point of contact.</h2><p>Shiva Exim is an agricultural export and import business established in 2018 and based in Mehsana, Gujarat, India. We bring together spices, seeds, grains and selected food ingredients for buyers, distributors, processors and agricultural suppliers.</p><p>Cumin and fennel are central to our spice portfolio, alongside sesame, mustard and other oilseeds, alfalfa and onion planting seeds, millets and feed grains. Our import sourcing covers agricultural and food products for the Indian market, with origin, quality and packing discussed for each requirement.</p><p>We work through a direct enquiry process: understand the intended use, identify the required grade, discuss samples and documentation, then agree the packing, payment and shipment terms. Each quotation states the proposed product and origin so buyers and suppliers can compare the same requirements.</p><h2 id="savan-patel">Your business contact: Savan Patel</h2><p>Speak with Savan Patel about export enquiries and agricultural import sourcing. Send your product, quantity, specification and destination by email or WhatsApp to begin.</p><h2>Markets we serve</h2><p>Our supplied markets include the Gulf, Europe, South Asia and Africa. We also welcome new enquiries from North America, South America, Russia and Australia as markets we aim to develop.</p><h2>Business registrations</h2><dl class="company-registrations"><div><dt>IEC</dt><dd>ADUFS1656H</dd></div><div><dt>GSTIN</dt><dd>24ADUFS1656H1ZO</dd></div></dl><p>Our company registration portfolio includes APEDA, Spices Board, FSSAI and IOPEPC. Contact us for the relevant registration details and documents for your transaction. Company registrations do not replace product-specific lot reports or destination requirements.</p><div class="hero-actions"><a class="button" href="/exports/">Our exports ↗</a><a class="text-link" href="/imports/">Our imports →</a></div></div><aside class="address-card"><span class="eyebrow">OUR OFFICE</span><h3>Mehsana, Gujarat</h3><p>'''+escape(address)+'''</p><p><strong>Customer visiting hours</strong><br>'''+escape(office_hours)+'''</p><a href="tel:+919099666604">+91 9099666604</a><a href="mailto:info@shivaexim.com">info@shivaexim.com</a></aside></section>'''
