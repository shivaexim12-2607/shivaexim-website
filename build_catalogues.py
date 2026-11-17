"""Build the full, shareable catalogues from the current website product data."""
from pathlib import Path
from io import BytesIO
import ast, html, re, json
from urllib.parse import quote
from PIL import Image, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from product_details import DETAILS, QUALITY_OPTIONS, CROP
from product_media import PHOTOGRAPHS

ROOT=Path(__file__).parent
OUT=ROOT/'dist/downloads';OUT.mkdir(exist_ok=True)
PRODUCTS=ast.literal_eval(next(n.value for n in ast.parse((ROOT/'build.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PRODUCTS' for t in n.targets)))
GREEN=HexColor('#173c2f');GOLD=HexColor('#9b753c');CREAM=HexColor('#f6f3eb');INK=HexColor('#233b2f');MUTED=HexColor('#657368');LINE=HexColor('#d9ded2')
W,H=595.28,841.89;M=42;CW=W-2*M
for name,file in [('CatSans','DejaVuSans.ttf'),('CatBold','DejaVuSans-Bold.ttf'),('CatSerif','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('CatSans',normal='CatSans',bold='CatBold',italic='CatSans',boldItalic='CatBold')
logo=ImageReader(Image.open(ROOT/'dist/assets/shiva-exim-logo-transparent.png').crop((450,125,1075,775)))
images={}
def esc(s):return html.escape(str(s).replace('—','-').replace('–','-').replace('’',"'").replace('↗','').replace('↓',''))
def para(c,value,x,top,width,size=9,font='CatSans',color=INK,leading=None):
 st=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.4,textColor=color)
 p=Paragraph(value,st);_,height=p.wrap(width,800);p.drawOn(c,x,top-height);return top-height

def image(c,slug,x,y,w,h):
 if slug not in images:
  im=Image.open(ROOT/'dist/assets/products'/f'{slug}.webp').convert('RGB');im.thumbnail((1100,850));b=BytesIO();im.save(b,'JPEG',quality=86,optimize=True);images[slug]=ImageReader(b)
 c.setFillColor(white);c.roundRect(x,y,w,h,4,fill=1,stroke=0);c.drawImage(images[slug],x+7,y+7,w-14,h-14,preserveAspectRatio=True,anchor='c')

def base(c,trade,page,total):
 c.setFillColor(CREAM);c.rect(0,0,W,H,fill=1,stroke=0)
 c.drawImage(logo,M,H-85,42,44,mask='auto')
 para(c,'SHIVA EXIM',M+56,H-47,300,23,'CatSerif',GREEN,26)
 para(c,'MEHSANA, GUJARAT, INDIA',M+56,H-78,300,6.7,color=MUTED)
 para(c,trade.upper()+' CATALOGUE',W-M-135,H-57,135,8,'CatBold',GOLD)
 c.setStrokeColor(LINE);c.line(M,H-105,W-M,H-105)
 c.setStrokeColor(LINE);c.line(M,55,W-M,55)
 para(c,'<link href="mailto:info@shivaexim.com">info@shivaexim.com</link> | <link href="tel:+919099666604">+91 9099666604</link>',M,43,420,7.3,color=MUTED)
 para(c,'<link href="https://shivaexim.com">shivaexim.com</link> | Updated 26 October 2026',M,28,420,6.8,color=MUTED)
 para(c,f'{page:02d} / {total:02d}',W-M-48,32,48,7.2,'CatBold',GREEN)

def cover(c,trade,products,total):
 base(c,trade,1,total)
 title='Export product<br/>catalogue' if trade=='export' else 'Import sourcing<br/>catalogue'
 para(c,title,M,703,CW,42,'CatSerif',GREEN,48)
 sub='Indian spices, seeds and agricultural products.' if trade=='export' else 'Agricultural and food products for the Indian market.'
 para(c,sub,M,591,CW,12,color=MUTED)
 slugs=['cumin-seeds','fennel-seeds','alfalfa-seeds'] if trade=='export' else ['olive-oil','popcorn','sunflower-seeds']
 tile=(CW-22)/3
 for i,slug in enumerate(slugs):
  x=M+i*(tile+11);image(c,slug,x,383,tile,160)
  para(c,esc(PHOTOGRAPHS[slug]['name']),x,368,tile,9,'CatBold',GREEN)
 c.setFillColor(GREEN);c.roundRect(M,173,CW,151,5,fill=1,stroke=0)
 para(c,str(len(products))+' product listings',M+22,300,CW-44,23,'CatSerif',white)
 body='Priority exports: cumin, fennel and alfalfa seeds.' if trade=='export' else 'Supplier enquiries: declare origin, grade, packing and shipment terms.'
 para(c,body,M+22,263,CW-44,11,color=white)
 para(c,'Photos, specification parameters and direct enquiry links for every listing.',M+22,235,CW-44,9,color=HexColor('#d9e4db'))
 para(c,'<link href="https://shivaexim.com/'+trade+'s/">Explore the current online '+trade+' portfolio</link>',M+22,208,CW-44,9,'CatBold',white)
 para(c,'Product photographs are representative. This catalogue is an enquiry guide; it is not a stock offer, test report or certification. Detailed quality limits, availability, price and shipment terms are confirmed for each quotation.',M,145,CW,8.4,color=MUTED)
 c.showPage()

def index(c,trade,products,total):
 base(c,trade,2,total);para(c,'Find a product',M,706,CW,31,'CatSerif',GREEN)
 para(c,'Select a product name to jump to its page.',M,660,CW,9,color=MUTED)
 y=624
 for i,p in enumerate(products):
  if i%2==0:c.setFillColor(white);c.rect(M,y-23,CW,26,fill=1,stroke=0)
  para(c,f'<link href="#product-{p[0]}">{esc(p[1])}</link>',M+10,y-3,278,9.4,'CatBold')
  para(c,esc(p[3]),M+300,y-3,145,8,color=MUTED)
  para(c,str(i+3),W-M-35,y-3,25,9,'CatBold',GREEN)
  y-=26
 para(c,'Enquiries: product and grade | quantity | packing | origin / destination | shipment period',M,88,CW,7.7,color=MUTED)
 c.showPage()

def specs_table(rows):
 for size in [8.5,8.1,7.7]:
  st=ParagraphStyle('cell',fontName='CatSans',fontSize=size,leading=size*1.3,textColor=INK)
  hd=ParagraphStyle('hd',parent=st,fontName='CatBold',textColor=white)
  data=[[Paragraph('PARAMETER',hd),Paragraph('WHAT TO AGREE',hd)]]
  data += [[Paragraph('<b>'+esc(label)+'</b>',st),Paragraph(esc(value),st)] for label,value,*_ in rows]
  t=Table(data,colWidths=[150,CW-150]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#eeeee5')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-1),.35,LINE)]))
  _,h=t.wrap(CW,700)
  if h<=265:return t,h
 raise ValueError('Specification table is too tall: '+str(h))

def product_page(c,trade,p,index,total):
 slug,name,_,group,desc,form,spec=p;item=DETAILS[slug]
 base(c,trade,index+3,total);c.bookmarkPage('product-'+slug);c.addOutlineEntry(name,'product-'+slug,level=0,closed=False)
 para(c,esc(name),M,715,CW,31,'CatSerif',GREEN)
 para(c,esc(group.upper())+' | '+esc(form),M,671,CW,8.2,'CatBold',GOLD)
 image(c,slug,M,476,227,168)
 photo_note=PHOTOGRAPHS[slug].get('photo_note','Representative photograph; not the offered lot.')
 caption_bottom=para(c,esc(photo_note),M,468,227,6.7,color=MUTED,leading=8)
 assert caption_bottom>435,(slug,'photo caption')
 y=para(c,esc(item['description']),291,643,262,9,color=INK,leading=12.5)
 y=para(c,'COMMON APPLICATIONS',291,y-12,262,7,'CatBold',GOLD)
 y=para(c,esc(item['uses']),291,y-5,262,8.4,color=MUTED,leading=11.5)
 assert y>463,(slug,'description',y)
 para(c,'Specification guide',M,428,CW,14,'CatBold',GREEN)
 para(c,'Enquiry parameters - target values and lot results are agreed with the offer.',M,406,CW,7.6,color=MUTED)
 rows=list(item['rows'])
 if slug in QUALITY_OPTIONS and slug!='mustard-seeds':rows.insert(0,('Listed options','; '.join(QUALITY_OPTIONS[slug])))
 # Crop/origin and packing/testing are shared below, leaving the table focused on product parameters.
 t,h=specs_table(rows);t.drawOn(c,M,387-h);bottom=387-h
 note=item.get('note','')
 if note:
  b=para(c,esc(note),M,bottom-11,CW,7.4,color=MUTED,leading=9.6)
  assert b>=102,(slug,'note',b)
 else:
  b=para(c,'Confirm origin, crop year, quantity, packing, lot testing and required documents with the quotation.',M,bottom-12,CW,7.7,color=MUTED)
 # The full online table includes additional buyer-test parameters.
 link='https://shivaexim.com/contact/?product='+slug+'&intent='+('buy' if trade=='export' else 'supply')
 c.setFillColor(GREEN);c.roundRect(M,70,244,29,4,fill=1,stroke=0)
 para(c,'REQUEST A QUOTATION' if trade=='export' else 'SEND YOUR SUPPLIER OFFER',M+12,89,220,8,'CatBold',white)
 c.linkURL(link,(M,70,M+244,99),relative=0)
 para(c,'<link href="https://shivaexim.com/products/'+slug+'/">Full specification guide online</link>',M+266,88,CW-266,8,'CatBold',GREEN)
 c.showPage()

def credits(c,trade,products,total):
 base(c,trade,total,total);para(c,'Photo credits',M,711,CW,30,'CatSerif',GREEN)
 y=para(c,'Photos illustrate the product category, not a specific lot, grade or certification. Each photograph retains its stated licence. No photographer endorsement is implied.',M,666,CW,8.1,color=MUTED)-18
 for p in products:
  m=PHOTOGRAPHS[p[0]]
  value=f'<b>{esc(p[1])}</b> - {esc(m["author"])} | <link href="{html.escape(m["license_url"],quote=True)}">{esc(m["license"])}</link><br/><link href="{html.escape(m["source"],quote=True)}">Original photograph</link> | Resized and converted for this catalogue; image licence retained.'
  y=para(c,value,M,y,CW,7.1,color=INK,leading=9.3)-7
 assert y>65,('credits overflow',trade,y)
 c.showPage()

def build(trade):
 products=[p for p in PRODUCTS if p[2]==trade]
 if trade=='export':
  priority=['cumin-seeds','fennel-seeds','alfalfa-seeds'];products=sorted(products,key=lambda p:priority.index(p[0]) if p[0] in priority else 3+PRODUCTS.index(p))
 filename='Shiva_Exim_Export_Product_Catalogue.pdf' if trade=='export' else 'Shiva_Exim_Import_Sourcing_Catalogue.pdf'
 path=OUT/filename;total=len(products)+3;c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
 c.setTitle('Shiva Exim - '+('Export Product Catalogue' if trade=='export' else 'Import Sourcing Catalogue'))
 c.setAuthor('Shiva Exim');c.setSubject('Product photos, specification enquiry parameters and contact links. Updated 26 October 2026.')
 cover(c,trade,products,total);index(c,trade,products,total)
 for i,p in enumerate(products):product_page(c,trade,p,i,total)
 credits(c,trade,products,total);c.save();print(path.name,total,'pages',path.stat().st_size,'bytes')
if __name__=='__main__':
 build('export');build('import')
