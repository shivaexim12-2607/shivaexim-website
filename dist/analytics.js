/* Business-interest events only: never send enquiry text or contact details. */
(() => {
  if (!['shivaexim.com', 'www.shivaexim.com'].includes(location.hostname)) return;
  if (navigator.globalPrivacyControl || navigator.doNotTrack === '1') return;
  const measurementId = 'G-JX66ZMLGPQ';
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  const pageLocation = location.origin + location.pathname;
  window.gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'
  });
  window.gtag('js', new Date());
  window.gtag('config', measurementId, {
    send_page_view: false,
    allow_google_signals: false,
    allow_ad_personalization_signals: false,
    page_location: pageLocation,
    page_referrer: document.referrer ? new URL(document.referrer).origin : ''
  });
  const track = (name, parameters = {}) => window.gtag('event', name, {
    send_to: measurementId, page_location: pageLocation, ...parameters
  });
  track('page_view', { page_title: document.title });
  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
  document.head.appendChild(tag);

  const placement = element => element.closest('.whatsapp-float') ? 'floating_whatsapp'
    : element.closest('header') ? 'header'
    : element.closest('footer') ? 'footer'
    : element.closest('.enquiry-panel') ? 'product_panel' : 'page';
  document.addEventListener('click', event => {
    const anchor = event.target.closest('a[href]');
    if (!anchor) return;
    const url = new URL(anchor.href, location.href);
    const parameters = { placement: placement(anchor) };
    if (url.protocol === 'mailto:') track('email_click', parameters);
    else if (url.hostname === 'wa.me') track('whatsapp_click', parameters);
    else if (['shivaexim.com', 'www.shivaexim.com'].includes(url.hostname) && url.pathname === '/contact/') {
      track('enquiry_click', parameters);
    } else if (['shivaexim.com', 'www.shivaexim.com'].includes(url.hostname) && /^\/downloads\/Shiva_Exim_(Export_Product|Import_Sourcing)_Catalogue\.pdf$/.test(url.pathname)) {
      track('catalogue_download', { ...parameters, catalogue: url.pathname.includes('_Export_') ? 'export' : 'import' });
    } else if (['shivaexim.com', 'www.shivaexim.com'].includes(url.hostname) && /^\/downloads\/(cumin-seeds|fennel-seeds|alfalfa-seeds)-product-guide\.pdf$/.test(url.pathname)) {
      track('product_guide_download', { ...parameters, guide: url.pathname.split('/').pop() });
    }
  }, true);
  document.addEventListener('submit', event => {
    if (event.target.id !== 'enquiry-form') return;
    // The browser dispatches submit only after native required-field validation.
    track(event.submitter?.value === 'whatsapp' ? 'whatsapp_click' : 'email_click', {
      placement: 'enquiry_form'
    });
  }, true);
  document.querySelector('#copy-enquiry')?.addEventListener('click', () => {
    if (document.querySelector('#enquiry-form')?.checkValidity()) {
      track('enquiry_copy', { placement: 'enquiry_form' });
    }
  });
})();
