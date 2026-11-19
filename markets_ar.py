"""Arabic versions of the Gulf (GCC) buyer pages: /ar/markets/ and /ar/markets/<country>/.

Same confirmed facts as markets.py (no prices, stock or transit-time promises).
Pages are linked to their English versions with hreflang tags and a language switch.
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

WA_NUMBER = '919099666604'

PRODUCTS_AR = {
    'cumin-seeds': ('بذور الكمون', 'جودة 99% أوروبا و99% سنغافورة'),
    'fennel-seeds': ('بذور الشمر', 'جودة 99% أوروبا و99% سنغافورة'),
    'sesame-seeds': ('السمسم', 'للصناعات الغذائية والتجارة'),
    'coriander-powder': ('كزبرة مطحونة', 'لخلطات التوابل والتصنيع الغذائي'),
    'chilli-powder': ('فلفل أحمر مطحون', 'لخلطات التوابل والتصنيع الغذائي'),
    'turmeric-powder': ('كركم مطحون', 'للتوابل وتحضير الأغذية'),
    'fenugreek-seeds': ('الحلبة', 'حبوب كاملة'),
    'alfalfa-seeds': ('بذور البرسيم الحجازي', 'بذور للزراعة (أعلاف)'),
    'onion-seeds': ('بذور البصل', 'بذور للزراعة'),
    'dill-seeds': ('بذور الشبت', 'حبوب كاملة'),
}

COUNTRIES_AR = {
    'uae': dict(
        name='الإمارات', full='الإمارات العربية المتحدة',
        title='مورد كمون وشمر من الهند للمستوردين في الإمارات',
        desc='شيفا إكزيم، الهند: كمون وشمر وتوابل هندية للمستوردين وتجار الجملة وشركات التعبئة في دبي والشارقة وأبوظبي. الحد الأدنى 1 طن، عينات مجانية، تحويل بنكي أو خطاب اعتماد.',
        cities='دبي والشارقة وأبوظبي وعجمان',
        ports=['ميناء جبل علي (دبي)', 'ميناء خليفة (أبوظبي)', 'ميناء خالد (الشارقة)'],
        buyers='تجار التوابل وشركات التعبئة وتجار الجملة وشركات إعادة التصدير',
        note='يعيد كثير من المشترين في الإمارات تصدير البضائع إلى الأسواق المجاورة. أخبرونا إذا كانت شحنتكم تحتاج إلى تعبئة أو ملصقات أو مستندات خاصة لإعادة التصدير.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'coriander-powder', 'chilli-powder', 'turmeric-powder'],
    ),
    'saudi-arabia': dict(
        name='السعودية', full='المملكة العربية السعودية',
        title='مورد كمون وشمر من الهند للمستوردين في السعودية',
        desc='شيفا إكزيم، الهند: كمون وشمر وسمسم وتوابل هندية للمستوردين في الرياض وجدة والدمام. الحد الأدنى 1 طن، عينات مجانية، تحويل بنكي أو خطاب اعتماد.',
        cities='الرياض وجدة والدمام ومكة المكرمة',
        ports=['ميناء جدة الإسلامي', 'ميناء الملك عبدالعزيز (الدمام)'],
        buyers='مستوردي التوابل وتجار الجملة وشركات التعبئة ومصانع الأغذية',
        note='أخبرونا بالمستندات ومتطلبات الملصقات التي يطلبها المستورد أو الجهة المختصة في السعودية، وسنؤكد لكم ما يمكننا توفيره قبل الطلب.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'fenugreek-seeds', 'turmeric-powder', 'chilli-powder'],
    ),
    'oman': dict(
        name='عُمان', full='سلطنة عُمان',
        title='مورد كمون وشمر وبذور برسيم من الهند للمستوردين في عُمان',
        desc='شيفا إكزيم، الهند: كمون وشمر، وبذور البرسيم والبصل للزراعة، وتوابل هندية للمستوردين في مسقط وصحار وصلالة. عينات مجانية.',
        cities='مسقط وصحار وصلالة ونزوى',
        ports=['ميناء صحار', 'ميناء صلالة', 'ميناء الدقم'],
        buyers='تجار التوابل وتجار الجملة وموردي المستلزمات الزراعية وتجار البذور',
        note='قد تحتاج بذور البرسيم وبذور البصل المخصصة للزراعة إلى تصريح استيراد وشهادة صحة نباتية. أخبرونا بمتطلبات الوزارة قبل الطلب.',
        products=['cumin-seeds', 'fennel-seeds', 'alfalfa-seeds', 'onion-seeds', 'sesame-seeds', 'fenugreek-seeds'],
    ),
    'qatar': dict(
        name='قطر', full='دولة قطر',
        title='مورد كمون وشمر من الهند للمستوردين في قطر',
        desc='شيفا إكزيم، الهند: كمون وشمر وتوابل هندية للمستوردين وتجار الجملة وشركات التعبئة في الدوحة. الحد الأدنى 1 طن، عينات مجانية، تحويل بنكي أو خطاب اعتماد.',
        cities='الدوحة والوكرة',
        ports=['ميناء حمد'],
        buyers='مستوردي التوابل وتجار الجملة وشركات التعبئة وموردي خدمات الأغذية',
        note='أخبرونا بالمستندات ومتطلبات الملصقات التي يطلبها المستورد أو الجهة المختصة في قطر، وسنؤكد لكم ما يمكننا توفيره قبل الطلب.',
        products=['cumin-seeds', 'fennel-seeds', 'sesame-seeds', 'coriander-powder', 'turmeric-powder', 'dill-seeds'],
    ),
}

POINTS_AR = [
    ('من حزام الكمون والشمر', 'نحن في مهسانا، شمال ولاية كجرات، بالقرب من سوق أونجا للكمون والشمر.'),
    ('جودة 99% أوروبا و99% سنغافورة', 'الكمون والشمر بالدرجات التجارية التي يطلبها مشترو الخليج. تُؤكَّد المواصفات لكل دفعة.'),
    ('عينات مجانية', 'العينة مجانية، وتدفعون رسوم الشحن السريع فقط.'),
    ('ابتداءً من 1 طن', 'الحد الأدنى للطلب 1 طن متري، وحاويات كاملة 20 قدم و40 قدم للطلبات الأكبر.'),
    ('مُصدِّر مسجَّل', 'مسجلون لدى APEDA وهيئة التوابل الهندية وFSSAI وIOPEPC. نعمل منذ عام 2018.'),
    ('دفع سهل', 'تحويل بنكي (T/T) أو خطاب اعتماد (L/C) أو PayPal، حسب عرض السعر.'),
]

FAQ_AR = [
    ('ما الحد الأدنى للطلب؟', '1 طن متري لمعظم المنتجات.'),
    ('هل يمكنني الحصول على عينة؟', 'نعم. العينة مجانية، وتدفعون رسوم الشحن السريع فقط.'),
    ('ما طرق الدفع؟', 'تحويل بنكي (T/T) أو خطاب اعتماد (L/C) أو PayPal. يُتفق على جدول الدفع في عرض السعر.'),
    ('لماذا لا تعرضون الأسعار؟', 'نرسل عرض سعر مكتوبًا حسب الدرجة والكمية والتعبئة والميناء، لأن أسعار التوابل تتغير مع كل موسم.'),
]


def _points():
    return '<div class="market-points">' + ''.join(
        f'<div><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for a, b in POINTS_AR) + '</div>'


def _cta(country_name=None):
    msg = 'مرحبا شيفا إكزيم، أنا مشترٍ من ' + (country_name or 'الخليج') + '.'
    return ('<div class="hero-actions"><a class="button" href="/contact/?intent=buy">أرسلوا استفساركم ↖</a>'
            '<a class="button secondary" href="/contact/?intent=sample">اطلبوا عينة مجانية ↖</a>'
            f'<a class="text-link" href="https://wa.me/{WA_NUMBER}?text={quote(msg)}" target="_blank" rel="noopener">تواصلوا عبر واتساب ←</a></div>')


def _product_list(slugs):
    items = ''.join(
        f'<a class="ar-product" href="/products/{s}/"><h3>{escape(PRODUCTS_AR[s][0])}</h3>'
        f'<p>{escape(PRODUCTS_AR[s][1])}</p><span class="text-link">تفاصيل المنتج (بالإنجليزية) ←</span></a>'
        for s in slugs)
    return f'<div class="ar-products">{items}</div>'


def _switch(href):
    return f'<a class="lang-switch" href="{href}" hreflang="en" lang="en">English version →</a>'


def render_markets_ar(shell, base, out):
    paths = []

    tiles = ''.join(
        f'<a class="market-tile" href="/ar/markets/{s}/"><h3>{escape(c["name"])}</h3>'
        f'<p>الموانئ: {escape("، ".join(c["ports"]))}</p><span class="text-link">عرض الصفحة ←</span></a>'
        for s, c in COUNTRIES_AR.items())
    hub = ('<div class="rtl" lang="ar" dir="rtl">'
           + '<section class="page-intro wrap">' + _switch('/markets/')
           + '<span class="eyebrow">مشترو دول الخليج</span>'
           + '<h1>كمون وشمر وبذور من الهند<br>لمستوردي الخليج.</h1>'
           + '<p>شيفا إكزيم (Shiva Exim) شركة هندية لتصدير التوابل والبذور من مهسانا، كجرات. نورّد للمشترين في دول الخليج. اختاروا بلدكم، أو أرسلوا لنا طلبكم مباشرة.</p></section>'
           + f'<section class="wrap market-tiles">{tiles}</section>'
           + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">لماذا شيفا إكزيم</span><h2>ما يحصل عليه مشترو الخليج منا.</h2></div></div>'
           + _points() + '</section>'
           + '<section class="wrap market-section"><p>تشترون للكويت أو البحرين؟ يسعدنا استفساركم أيضًا. أخبرونا بالميناء والمتطلبات.</p>'
           + _cta() + '</section></div>')
    shell('ar/markets', 'توابل وبذور من الهند لمستوردي دول الخليج',
          'شيفا إكزيم، الهند: بذور الكمون والشمر والسمسم وبذور البرسيم والبصل وتوابل هندية للمستوردين في الإمارات والسعودية وعُمان وقطر والكويت والبحرين.',
          hub)
    paths.append('ar/markets')

    for slug, c in COUNTRIES_AR.items():
        others = ''.join(f'<a href="/ar/markets/{s}/">{escape(o["name"])}</a>' for s, o in COUNTRIES_AR.items() if s != slug)
        ports = ''.join(f'<li>{escape(p)}</li>' for p in c['ports'])
        faq = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in FAQ_AR)
        body = (
            '<div class="rtl" lang="ar" dir="rtl">'
            + f'<div class="wrap breadcrumb"><a href="/">الرئيسية</a><span>/</span><a href="/ar/markets/">مشترو الخليج</a><span>/</span><span>{escape(c["name"])}</span></div>'
            + '<section class="page-intro wrap">' + _switch(f'/markets/{slug}/')
            + f'<span class="eyebrow">للمستوردين في {escape(c["name"])}</span>'
            + f'<h1>كمون وشمر وتوابل هندية<br>إلى {escape(c["full"])}.</h1>'
            + f'<p>شيفا إكزيم (Shiva Exim) شركة لتصدير التوابل والبذور من مهسانا، ولاية كجرات، الهند. نورّد إلى {escape(c["buyers"])} في {escape(c["cities"])}، مع عينات مجانية وطلبات ابتداءً من 1 طن متري.</p>'
            + _cta(c['name']) + '</section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">الأكثر طلبًا</span><h2>منتجات للبداية.</h2></div><a class="text-link" href="/exports/">جميع منتجات التصدير (بالإنجليزية) ←</a></div>'
            + _product_list(c['products']) + '</section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">لماذا شيفا إكزيم</span><h2>لماذا تشترون منا.</h2></div></div>' + _points() + '</section>'
            + f'<section class="wrap market-section market-ship"><div><span class="eyebrow">الشحن إلى {escape(c["name"])}</span><h2>من كجرات إلى مينائكم.</h2>'
            + '<p>نشحن من الموانئ البحرية الهندية عبر الطريق البحري القصير إلى الخليج. تكون البضاعة جاهزة عادةً خلال 10–15 يومًا بعد تأكيد الطلب. أخبرونا بميناء الوصول وسنرسل لكم عرض السعر.</p>'
            + f'<h3>أهم الموانئ التي نقدم لها عروض الأسعار</h3><ul>{ports}</ul></div>'
            + '<div><h3>التعبئة</h3><p>أكياس 25 أو 30 أو 50 كجم (الحبوب 40 أو 50 كجم). علامتكم التجارية والبطانات والمنصات عند الطلب.</p>'
            + '<h3>دليل الحاويات</h3><p>الكمون والشمر حوالي 14 طنًا في حاوية 20 قدم، وحوالي 28 طنًا في حاوية 40 قدم. الكمية النهائية حسب التعبئة.</p>'
            + f'<h3>المستندات</h3><p>{escape(c["note"])}</p></div></section>'
            + '<section class="wrap market-section"><div class="section-heading"><div><span class="eyebrow">إجابات سريعة</span><h2>قبل أن تستفسروا.</h2></div></div>'
            + f'<div class="faq-list">{faq}</div></section>'
            + f'<section class="wrap market-section"><p class="other-markets">صفحات خليجية أخرى: {others}</p></section>'
            + '</div>'
        )
        shell('ar/markets/' + slug, c['title'], c['desc'], body)
        paths.append('ar/markets/' + slug)

    # Language attributes, hreflang pairs and an Arabic link on the English pages.
    pairs = [('markets', 'ar/markets')] + [(f'markets/{s}', f'ar/markets/{s}') for s in COUNTRIES_AR]
    for en, ar in pairs:
        en_url, ar_url = f'{base}/{en}/', f'{base}/{ar}/'
        links = (f'<link rel="alternate" hreflang="en" href="{en_url}">'
                 f'<link rel="alternate" hreflang="ar" href="{ar_url}">'
                 f'<link rel="alternate" hreflang="x-default" href="{en_url}">')
        ar_file = Path(out) / ar / 'index.html'
        t = ar_file.read_text()
        t = t.replace('<html lang="en">', '<html lang="ar">', 1).replace('</head>', links + '</head>', 1)
        ar_file.write_text(t)
        en_file = Path(out) / en / 'index.html'
        t = en_file.read_text()
        switch = f'<a class="lang-switch" href="{ar_url}" hreflang="ar" lang="ar" dir="rtl">اقرأ هذه الصفحة بالعربية ←</a>'
        t = t.replace('</head>', links + '</head>', 1)
        t = t.replace('<section class="page-intro wrap">', '<section class="page-intro wrap">' + switch, 1)
        en_file.write_text(t)
    return paths
