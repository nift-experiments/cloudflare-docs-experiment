---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/
  description: Access and review account audit logs.
  full_title: Review audit logs - v1 · Cloudflare Learning Paths
  head_html: <title>Review audit logs - v1 · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Access and review account audit logs."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/index.md"><meta property="og:title" content="Review audit logs - v1 · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access and review account audit logs."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,DDoS Protection,SSL/TLS,DNS,Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/#page","headline":"Review audit logs - v1 \u00b7 Cloudflare Learning Paths","description":"Access and review account audit logs.","url":"https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/application-security/account-security/review-audit-logs/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9635.md")
</aside>
<p>Audit logs summarize the history of changes made within your Cloudflare account. Audit logs include account level actions like login, as well as zone configuration changes.</p>
<p>Audit Logs are available on all plan types and are captured for both individual users and for multi-user organizations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9634.md")
</aside>
<p>Audit logs are available in the dashboard as well as the API.</p>
<h3 id="using-the-dashboard">Using the dashboard</h3>
<p>To access audit logs in the Cloudflare dashboard:</p>
<p>In the Cloudflare dashboard, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can search these audit logs by user email or domain and filter by date range. To download audit logs, click <strong>Download CSV</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9633.md")
</aside>
<h3 id="using-the-api">Using the API</h3>
<p>To get audit logs from the Cloudflare API, send a <a href="/api/resources/audit_logs/methods/list/">GET request</a>.</p>
<p>We recommending using the API for downloading historical audit log data.</p>
<p>To maintain Audit Logs query performance, the Audit Logs API was modified on 2019-06-30 to return records with a maximum age of 18 months.</p>
