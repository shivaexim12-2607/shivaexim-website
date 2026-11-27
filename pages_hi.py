"""Hindi pages for Indian buyers (dealers and farmers) of berseem and alfalfa seed.

Each page is paired with its English product page through hreflang tags and a
language link. Facts and seed rates follow the same sources as the English pages.
"""
import json
from pathlib import Path
from urllib.parse import quote
from html import escape

PHONE = '919099666604'

PAGES = {
    'berseem-seed': {
        'en': 'products/berseem-seeds',
        'title': 'बरसीम बीज (आयातित) — भारत में थोक खरीदें, डीलर और किसान',
        'desc': 'शिवा एक्ज़िम, मेहसाणा (गुजरात) से आयातित बरसीम बीज खरीदें। प्रति एकड़ बीज दर, बुवाई का समय और डीलरों के लिए थोक सप्लाई। WhatsApp पर भाव पूछें।',
        'h1': 'बरसीम बीज (आयातित) — भारत में खरीदें',
        'lead': 'शिवा एक्ज़िम बरसीम (Egyptian clover) का चारा बीज आयात करता है और पूरे भारत में बीज डीलरों, वितरकों, डेयरी फार्मों और किसानों को बेचता है।',
        'wa': 'नमस्ते शिवा एक्ज़िम, मुझे बरसीम बीज खरीदना है। मात्रा: ___ किलो। स्थान: ___।',
        'rows': [
            ('बीज', 'आयातित बरसीम (Trifolium alexandrinum) चारा बीज'),
            ('किसे सप्लाई करते हैं', 'बीज डीलर, वितरक, डेयरी फार्म और किसान — पूरे भारत में'),
            ('प्रति एकड़ बीज', 'लगभग 8–10 किलो प्रति एकड़ (20–25 किलो प्रति हेक्टेयर) एक सामान्य संदर्भ है'),
            ('बुवाई का समय', 'सितंबर का आखिरी सप्ताह से अक्टूबर का पहला सप्ताह (उत्तर भारत का सामान्य संदर्भ)। अपने क्षेत्र की स्थानीय सलाह मानें।'),
            ('ऑर्डर कैसे करें', 'मात्रा और अपना शहर/राज्य WhatsApp पर भेजें। भाव और लॉट की जानकारी हर कोटेशन के साथ पक्की की जाती है।'),
        ],
        'faq': [
            ('बरसीम बीज प्रति एकड़ कितना लगता है?', 'सामान्य संदर्भ के अनुसार 20–25 किलो प्रति हेक्टेयर, यानी लगभग 8–10 किलो प्रति एकड़ बीज लगता है। लाइन में बुवाई 25 सेमी की दूरी पर की जाती है। अपने क्षेत्र के कृषि विशेषज्ञ की सलाह भी लें।'),
            ('बरसीम की बुवाई कब करें?', 'उत्तर भारत में सितंबर का आखिरी सप्ताह से अक्टूबर का पहला सप्ताह बुवाई का अच्छा समय माना जाता है। बरसीम सिंचित क्षेत्रों में सर्दियों की चारा फसल है।'),
            ('कौन-सी किस्म मिलती है?', 'हम आयातित बरसीम बीज बेचते हैं। किस्म, मूल देश, अंकुरण (germination) और पैकिंग हर लॉट के लिए खरीद से पहले बताई जाती है।'),
            ('भाव कैसे पता करें?', 'WhatsApp पर +91 9099666604 पर मात्रा और स्थान भेजें। हम उस समय के लॉट और भाव के साथ जवाब देंगे।'),
        ],
        'source': ('DAV University — Forage crops study material (बरसीम)', 'https://www.davuniversity.org/images/files/study-material/Forage%20crops.pdf'),
        'switch_en': 'हिंदी में पढ़ें: बरसीम बीज →',
    },
    'alfalfa-seed': {
        'en': 'products/alfalfa-seeds',
        'title': 'अल्फाल्फा (रिजका / लूसर्न) बीज — भारत में थोक खरीदें',
        'desc': 'शिवा एक्ज़िम, मेहसाणा (गुजरात) से अल्फाल्फा (रिजका / लूसर्न) चारा बीज खरीदें। प्रति एकड़ बीज दर, कटाई का समय और डीलरों के लिए थोक सप्लाई। WhatsApp पर भाव पूछें।',
        'h1': 'अल्फाल्फा (रिजका / लूसर्न) बीज — भारत में खरीदें',
        'lead': 'शिवा एक्ज़िम अल्फाल्फा (रिजका / लूसर्न) चारा बीज का निर्यात करता है और भारत में भी बीज डीलरों, वितरकों, डेयरी फार्मों और किसानों को बेचता है।',
        'wa': 'नमस्ते शिवा एक्ज़िम, मुझे अल्फाल्फा (रिजका) बीज खरीदना है। मात्रा: ___ किलो। स्थान: ___।',
        'rows': [
            ('बीज', 'अल्फाल्फा / रिजका / लूसर्न (Medicago sativa) चारा बीज — एक साल वाली और कई साल वाली किस्में'),
            ('किसे सप्लाई करते हैं', 'बीज डीलर, वितरक, डेयरी फार्म और किसान — पूरे भारत में; साथ ही यूरोप, पाकिस्तान और खाड़ी देशों में निर्यात'),
            ('प्रति एकड़ बीज', 'लगभग 8 किलो प्रति एकड़ (20 किलो प्रति हेक्टेयर), 25 सेमी लाइन में'),
            ('कटाई', 'पहली कटाई बुवाई के 60–65 दिन बाद, फिर हर 20–25 दिन में (TNAU संदर्भ)'),
            ('ऑर्डर कैसे करें', 'मात्रा और अपना शहर/राज्य WhatsApp पर भेजें। भाव और लॉट की जानकारी हर कोटेशन के साथ पक्की की जाती है।'),
        ],
        'faq': [
            ('रिजका (अल्फाल्फा) बीज प्रति एकड़ कितना लगता है?', 'तमिलनाडु कृषि विश्वविद्यालय (TNAU) के अनुसार 20 किलो प्रति हेक्टेयर, यानी लगभग 8 किलो प्रति एकड़ बीज, 25 सेमी की लाइन में। अपने क्षेत्र और किस्म के अनुसार स्थानीय सलाह भी लें।'),
            ('रिजका की कटाई कब और कितनी बार होती है?', 'TNAU के अनुसार पहली कटाई बुवाई के 60–65 दिन बाद होती है, फिर हर 20–25 दिन में। उनकी परिस्थितियों में साल में 12–14 कटाई और 90–130 टन प्रति हेक्टेयर हरा चारा मिलता है।'),
            ('एक साल वाली और कई साल वाली किस्म में क्या फर्क है?', 'एक साल वाली किस्म एक सीज़न के चारे के लिए है, कई साल वाली किस्म कई सालों तक कटाई देती है। अपनी ज़रूरत बताएं — हम उपलब्ध लॉट की किस्म, अंकुरण और पैकिंग पहले बताएंगे।'),
            ('भाव कैसे पता करें?', 'WhatsApp पर +91 9099666604 पर मात्रा और स्थान भेजें। हम उस समय के लॉट और भाव के साथ जवाब देंगे।'),
        ],
        'source': ('Tamil Nadu Agricultural University (TNAU) — Lucerne crop production', 'https://agritech.tnau.ac.in/agriculture/foragecrops_fodder_lucerne_crop%20production.html'),
        'switch_en': 'हिंदी में पढ़ें: रिजका (अल्फाल्फा) बीज →',
    },
}


def _body(slug, p):
    wa = f'https://wa.me/{PHONE}?text=' + quote(p['wa'])
    rows = ''.join(f'<tr><th scope="row">{escape(a)}</th><td>{escape(b)}</td></tr>' for a, b in p['rows'])
    faq = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in p['faq'])
    src_name, src_url = p['source']
    return (
        '<div lang="hi">'
        f'<section class="page-intro wrap"><a class="lang-switch" href="/{p["en"]}/" hreflang="en" lang="en">Read in English →</a>'
        f'<span class="eyebrow">डीलर और किसानों के लिए</span><h1>{escape(p["h1"])}</h1><p>{escape(p["lead"])}</p>'
        f'<p><a class="button" href="{wa}" target="_blank" rel="noopener">WhatsApp पर भाव पूछें ↗</a> '
        '<a class="button secondary" href="tel:+919099666604">कॉल करें: +91 9099666604</a></p></section>'
        '<section class="product-information wrap"><div class="specification-table-wrap"><table class="specification-table"><tbody>'
        f'{rows}</tbody></table></div>'
        f'<p class="technical-source">संदर्भ: <a href="{src_url}" target="_blank" rel="noopener">{escape(src_name)} ↗</a>। बीज दर खेती की एक सामान्य सलाह है, न्यूनतम ऑर्डर नहीं।</p></section>'
        f'<section class="buying-guide wrap"><div class="section-heading"><div><span class="eyebrow">आम सवाल</span><h2>किसानों और डीलरों के सवाल</h2></div></div>{faq}'
        f'<p><a class="button" href="{wa}" target="_blank" rel="noopener">WhatsApp पर ऑर्डर करें ↗</a></p></section>'
        '<section class="wrap"><p>शिवा एक्ज़िम · D-11, फर्स्ट फ्लोर, APMC, मेहसाणा 384001, गुजरात · APEDA, Spices Board, FSSAI पंजीकृत</p></section>'
        '</div>'
    )


def render_pages_hi(shell, base, out):
    paths = []
    for slug, p in PAGES.items():
        path = 'hi/' + slug
        shell(path, p['title'], p['desc'], _body(slug, p))
        paths.append(path)
        hi_url, en_url = f'{base}/{path}/', f'{base}/{p["en"]}/'
        links = (f'<link rel="alternate" hreflang="en" href="{en_url}">'
                 f'<link rel="alternate" hreflang="hi" href="{hi_url}">'
                 f'<link rel="alternate" hreflang="x-default" href="{en_url}">')
        faq_schema = {'@context': 'https://schema.org', '@type': 'FAQPage', 'inLanguage': 'hi',
                      'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]}
        hi_file = Path(out) / path / 'index.html'
        t = hi_file.read_text()
        t = t.replace('<html lang="en">', '<html lang="hi">', 1).replace(
            '</head>', links + f'<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script></head>', 1)
        hi_file.write_text(t)
        en_file = Path(out) / p['en'] / 'index.html'
        t = en_file.read_text()
        switch = f'<a class="lang-switch" href="{hi_url}" hreflang="hi" lang="hi">{p["switch_en"]}</a>'
        t = t.replace('</head>', links + '</head>', 1).replace('<h1>', switch + '<h1>', 1)
        en_file.write_text(t)
    return paths
