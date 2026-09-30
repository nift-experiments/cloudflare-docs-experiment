---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/
  description: Review Cloudflare Audit Logs v1 to track account activity through the dashboard or API.
  full_title: Review audit logs - v1 · Cloudflare Fundamentals docs
  head_html: <title>Review audit logs - v1 · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Review Cloudflare Audit Logs v1 to track account activity through the dashboard or API."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/index.md"><meta property="og:title" content="Review audit logs - v1 · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review Cloudflare Audit Logs v1 to track account activity through the dashboard or API."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,Audit Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/#page","headline":"Review audit logs - v1 \u00b7 Cloudflare Fundamentals docs","description":"Review Cloudflare Audit Logs v1 to track account activity through the dashboard or API.","url":"https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/account-security/review-audit-logs/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8943.md")
</aside>
<p>Audit logs summarize the history of changes made within your Cloudflare account. Audit logs include account level actions like login, as well as zone configuration changes.</p>
<p>Audit Logs are available on all plan types and are captured for both individual users and for multi-user organizations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8942.md")
</aside>
<h2 id="access-audit-logs">Access audit logs</h2>
<h3 id="using-the-dashboard">Using the dashboard</h3>
<p>To access audit logs in the Cloudflare dashboard:</p>
<p>In the Cloudflare dashboard, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can search these audit logs by user email or domain and filter by date range. To download audit logs, click <strong>Download CSV</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8941.md")
</aside>
<h3 id="using-the-api">Using the API</h3>
<p>To get audit logs from the Cloudflare API, send a <a href="/api/resources/audit_logs/methods/list/">GET request</a>.</p>
<p>We recommending using the API for downloading historical audit log data.</p>
<p>To maintain Audit Logs query performance, the Audit Logs API was modified on 2019-06-30 to return records with a maximum age of 18 months.</p>
<h2 id="retention">Retention</h2>
<p>Audit Logs are retained for 18 months before being deleted. Enterprise customers can use <a href="/logs/logpush/">Logpush</a> to store Audit Logs for longer periods of time.</p>
