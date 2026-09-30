---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/
  description: Submit abuse reports to Cloudflare via the dashboard, public form, or API, and view reports filed against your account.
  full_title: View and submit reports · Cloudflare Fundamentals docs
  head_html: <title>View and submit reports · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Submit abuse reports to Cloudflare via the dashboard, public form, or API, and view reports filed against your account."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/index.md"><meta property="og:title" content="View and submit reports · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submit abuse reports to Cloudflare via the dashboard, public form, or API, and view reports filed against your account."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/#page","headline":"View and submit reports \u00b7 Cloudflare Fundamentals docs","description":"Submit abuse reports to Cloudflare via the dashboard, public form, or API, and view reports filed against your account.","url":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/report-abuse/submit-report/
  schema: 1
---
<h2 id="submit-reports">Submit reports</h2>
<p>Cloudflare provides security, performance, and reliability services to millions of websites. When you report abuse involving a website that uses Cloudflare, Cloudflare's ability to respond depends on the Cloudflare service involved. Many reports involve websites using Cloudflare's pass-through CDN and security services, while others involve domains registered through Cloudflare Registrar or content hosted on Cloudflare's developer platform.</p>
<p>If you find abusive content on a website that uses Cloudflare, you can submit a report in one of three ways:</p>
<ul>
<li><strong>Public form</strong>: Use <a href="https://abuse.cloudflare.com/">Submit an abuse report</a> to report abuse to Cloudflare. This form is available to anyone on the Internet.</li>
<li><strong>Cloudflare dashboard</strong>: Entitled Cloudflare customers can submit abuse reports from the <strong>Abuse reports</strong> page. You must have the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li><strong>Cloudflare API</strong>: Entitled Cloudflare customers can submit abuse reports using the <a href="/api/resources/abuse_reports/">Abuse Reports API</a>. You must have the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role.</li>
</ul>
<h2 id="view-submitted-reports">View submitted reports</h2>
<p>Entitled Cloudflare customers with the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role can view abuse reports against content associated with their account.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Abuse reports</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Optionally, filter reports by date, report status, report type, or domain.</li>
</ol>
<p>If Cloudflare applied a mitigation to your website because of an abuse report, you may be able to request a review of that mitigation in the dashboard or using the <a href="/api/resources/abuse_reports/subresources/mitigations/">Abuse Report Mitigations API</a>. Cloudflare will review the request and may remove the mitigation.</p>
<h2 id="receive-notifications">Receive notifications</h2>
<p>You can enable abuse notifications for your account to configure email, webhook, or PagerDuty alerts about new abuse reports against your websites.</p>
<p>For help setting up alerts, refer to <a href="/notifications/get-started/">Configure Cloudflare notifications</a>.</p>
