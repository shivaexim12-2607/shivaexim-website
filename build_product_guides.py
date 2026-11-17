"""Build three one-page guides from the same confirmed copy used by the website."""
from pathlib import Path
from html import escape
import json
from io import BytesIO
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from product_media import MEDIA

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
OUT = DIST / 'downloads'
OUT.mkdir(exist_ok=True)
GREEN = HexColor('#173c2f')
CREAM = HexColor('#f5f3e9')
INK = HexColor('#233b2f')
FONT_ROOT = Path('/usr/share/fonts/truetype/dejavu')
for name, filename in [('GuideSans','DejaVuSans.ttf'), ('GuideBold','DejaVuSans-Bold.ttf'), ('GuideSerif','DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_ROOT / filename)))
FONT_MAP = {'Helvetica':'GuideSans','Helvetica-Bold':'GuideBold','Times-Roman':'GuideSerif','Helvetica-Oblique':'GuideSans'}

def text(c, value, x, top, width, size=10, color=INK, font='Helvetica', leading=None):
    style = ParagraphStyle('copy', fontName=FONT_MAP[font], fontSize=size,
                           leading=leading or size * 1.35, textColor=color)
    p = Paragraph(value, style)
    _, h = p.wrap(width, 800)
    p.drawOn(c, x, top-h)
    return top-h

credits = {}
for slug, m in MEDIA.items():
    original = DIST / 'assets/products' / (slug+'.jpg')
    webp = original.with_suffix('.webp')
    if original.exists():
        image = Image.open(original).convert('RGB')
        original_size = image.size
        image.thumbnail((1600, 1200))
        image.save(webp, 'WEBP', quality=88, method=6)
    else:
        image = Image.open(webp).convert('RGB')
        original_size = image.size
    credits[slug] = {k: m[k] for k in ['name','author','source','license','license_url']}
    credits[slug].update(original_dimensions=original_size,
                         changes='Resized and converted to WebP; no colour or content edits.')
    c = canvas.Canvas(str(OUT/(slug+'-product-guide.pdf')), pagesize=(595.28,841.89))
    c.setTitle(m['name']+' - Product and Specification Guide | Shiva Exim')
    c.setAuthor('Shiva Exim')
    c.setFillColor(GREEN);c.rect(0,773,596,69,fill=1,stroke=0)
    c.drawImage(str(DIST/'assets/shiva-exim-logo-transparent.png'),42,791,28,28,mask='auto',preserveAspectRatio=True)
    text(c,'SHIVA EXIM',82,818,280,19,white,'Times-Roman')
    text(c,'MEHSANA, GUJARAT, INDIA',82,791,340,8,white)
    text(c,m['name'],42,746,510,30,font='Times-Roman')
    text(c,'PRODUCT &amp; SPECIFICATION GUIDE',42,706,510,9)
    pdf_image = image.copy()
    pdf_image.thumbnail((1100, 750))
    pdf_bytes = BytesIO()
    pdf_image.save(pdf_bytes, format='JPEG', quality=87, optimize=True)
    pdf_bytes.seek(0)
    c.drawImage(ImageReader(pdf_bytes),42,527,248,155,preserveAspectRatio=True,anchor='c')
    text(c,m['botanical'],319,677,225,12,font='Helvetica-Oblique')
    text(c,escape(m['intro']),319,649,225,10)
    text(c,'Representative photograph.<br/>Not the offered lot.',319,569,225,8)
    c.setFillColor(CREAM);c.roundRect(42,470,511,43,5,fill=1,stroke=0)
    text(c,'LISTED QUALITY OPTIONS',54,504,484,8)
    text(c,escape(m['options']),54,490,484,11,font='Helvetica-Bold')
    y=450
    for index,(label,value) in enumerate(m['rows']):
        if index%2==0:
            c.setFillColor(HexColor('#f7f8f4'));c.rect(42,y-39,511,39,fill=1,stroke=0)
        text(c,escape(label),51,y-8,162,9,font='Helvetica-Bold')
        text(c,escape(value),228,y-8,316,9)
        y-=39
    note = ('Commercial quality labels are not certification or blanket destination compliance.'
            if slug!='alfalfa-seeds' else
            'Single-year and multi-year are listed commercial options. Confirm variety and lot tests separately.')
    text(c,escape(note)+' Detailed limits and availability are agreed with each quotation.',42,201,510,8)
    c.setFillColor(GREEN);c.roundRect(42,113,511,54,5,fill=1,stroke=0)
    text(c,'REQUEST A QUOTATION',54,156,484,9,white,'Helvetica-Bold')
    text(c,'Quantity | Grade / variety | Packing | Destination | Shipment period',54,139,484,9,white)
    text(c,'info@shivaexim.com  |  +91 9099666604  |  shivaexim.com',42,96,511,9)
    c.linkURL('https://shivaexim.com/contact/?product='+slug+'&intent=buy',(42,113,553,167),relative=0)
    text(c,'Photo: '+escape(m['author'])+' | '+escape(m['license'])+' | Resized; image licence retained.',42,73,511,6.5)
    text(c,'Source: <link href="'+m['source']+'">'+m['source']+'</link>',42,60,511,6.5)
    text(c,'Licence: <link href="'+m['license_url']+'">'+m['license_url']+'</link>',42,47,511,6.5)
    text(c,'Prepared 26 October 2026 | This guide is not a certificate of analysis or a firm stock offer.',42,30,511,6.5)
    c.showPage();c.save()
    if original.exists(): original.unlink()
(DIST/'assets/products/credits.json').write_text(json.dumps(credits,indent=2)+'\n')
print('Built 3 product guides and optimized photographs.')
