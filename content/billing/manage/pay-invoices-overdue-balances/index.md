---
cp9:
  canonical: https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/
  description: Resolve unpaid invoices and overdue balances.
  full_title: Pay an outstanding balance · Cloudflare Billing docs
  head_html: <title>Pay an outstanding balance · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve unpaid invoices and overdue balances."><link rel="canonical" href="https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/index.md"><meta property="og:title" content="Pay an outstanding balance · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve unpaid invoices and overdue balances."><meta property="og:url" content="https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/#page","headline":"Pay an outstanding balance \u00b7 Cloudflare Billing docs","description":"Resolve unpaid invoices and overdue balances.","url":"https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/manage/pay-invoices-overdue-balances/
  schema: 1
---
<p>If automatic payment retries fail and you do not pay manually, your account accrues an overdue balance. While the balance is unpaid, you cannot purchase products, upgrade subscriptions, or update your billing profile. Attempts to do so return an error:</p>
<p><strong>&quot;You cannot add or modify subscriptions or services until the outstanding balance is paid.&quot;</strong></p>
<p>To pay, select <strong>Pay Now</strong> from the <strong>Billing</strong> page in the Cloudflare dashboard. You can pay the entire balance in one transaction or <a href="#manually-pay-invoices">pay individual invoices</a> separately.</p>
<h2 id="understand-why-you-have-an-outstanding-balance">Understand why you have an outstanding balance</h2>
<p>When an outstanding balance is due, a new invoice is created in your account for that amount. The new invoice shows the original invoice number that the outstanding balance relates to. You can look up this original invoice to identify which products were not fully paid for.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3411.md")
</div>
<h2 id="pay-an-outstanding-balance">Pay an outstanding balance</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3410.md")
</aside>
<p>To pay the total outstanding balance:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3412.md")
</div>
<p>You will be redirected to our payment system to proceed.</p>
<h2 id="manually-pay-invoices">Manually pay invoices</h2>
<p>If an automatic subscription renewal payment fails, Cloudflare automatically retries the payment using your default payment method five times over five days. During this period, you can log in to the dashboard and attempt to manually pay the invoices.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3413.md")
</div>
<p>You will be redirected to our payment system to proceed.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a> — Fix errors when paying</li>
<li><a href="/billing/manage/invoices/">Invoices</a> — View and download invoices</li>
<li><a href="/billing/troubleshoot/error-reference/">Error reference</a> — Look up billing error messages</li>
</ul>
