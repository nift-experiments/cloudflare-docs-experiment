---
cp9:
  canonical: https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/
  description: Resolve common invoice discrepancies.
  full_title: Troubleshoot invoices · Cloudflare Billing docs
  head_html: <title>Troubleshoot invoices · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common invoice discrepancies."><link rel="canonical" href="https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/index.md"><meta property="og:title" content="Troubleshoot invoices · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common invoice discrepancies."><meta property="og:url" content="https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/#page","headline":"Troubleshoot invoices \u00b7 Cloudflare Billing docs","description":"Resolve common invoice discrepancies.","url":"https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-invoices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/troubleshoot/troubleshoot-invoices/
  schema: 1
---
<p>Use this page when invoice information is missing, invoice amounts differ from the Cloudflare dashboard, or company details do not appear as expected.</p>
<h2 id="change-in-billing-contact-information">Change in billing contact information</h2>
<h3 id="symptom">Symptom</h3>
<p>Invoices are sent to the wrong billing contact.</p>
<h3 id="fix">Fix</h3>
<p><a href="/billing/get-started/update-billing-info/#update-billing-email-address">Update your Cloudflare billing email address</a> as soon as possible.</p>
<h2 id="change-in-cloudflare-subscription-or-account">Change in Cloudflare subscription or account</h2>
<h3 id="symptom-1">Symptom</h3>
<p>An invoice appears after you change a plan, add a domain, or turn on an add-on service.</p>
<h3 id="cause">Cause</h3>
<p>The invoice data corresponds to the date your Cloudflare account changed. You are charged immediately for the plan, additional domain, or add-on service. An invoice is available in the Cloudflare dashboard within 24 hours of the account change.</p>
<p>Billing periods are 30 days. Payments for all recurring monthly costs are processed on the last day of the billing period. Invoices are generated the same day and will appear in the <strong>Billing</strong> section of the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> within 24 hours.</p>
<h2 id="cloudflare-invoice-without-company-name">Cloudflare invoice without company name</h2>
<h3 id="symptom-2">Symptom</h3>
<p>Your invoice does not include your company name, VAT ID, or Tax ID/EIN.</p>
<h3 id="fix-1">Fix</h3>
<p>To add your business or company name, VAT ID, or Tax ID/EIN on future invoices, <a href="/billing/get-started/update-billing-info/">update your billing information</a>.</p>
<h2 id="inconsistent-invoice-and-payment-amounts">Inconsistent invoice and payment amounts</h2>
<h3 id="symptom-3">Symptom</h3>
<p>The invoice amount does not match the amount shown in the Cloudflare dashboard.</p>
<h3 id="cause-1">Cause</h3>
<p>If your Cloudflare payment is past due and you order additional services, the past due amount is added to your invoice. This may cause inconsistencies between the invoice and what you see in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. After the account is current, the amounts in the Cloudflare dashboard update.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3383.md")
</aside>
<h2 id="still-stuck">Still stuck?</h2>
<p>If the invoice discrepancy remains after one billing period, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> with the invoice number and account ID.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/invoices/">Invoices</a> — Download and manage invoices</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — How to read your invoice</li>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> — Change your billing email</li>
</ul>
