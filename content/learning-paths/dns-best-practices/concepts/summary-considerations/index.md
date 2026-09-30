---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/
  description: Review DNS migration best practices summary.
  full_title: Key considerations and best practices summary · Cloudflare Learning Paths
  head_html: <title>Key considerations and best practices summary · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Review DNS migration best practices summary."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/index.md"><meta property="og:title" content="Key considerations and best practices summary · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review DNS migration best practices summary."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/#page","headline":"Key considerations and best practices summary \u00b7 Cloudflare Learning Paths","description":"Review DNS migration best practices summary.","url":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/dns-best-practices/concepts/summary-considerations/
  schema: 1
---
<ul>
<li>Plan meticulously: Do not rush the planning and preparation phases.</li>
<li>Communicate clearly: Keep stakeholders informed.</li>
<li>Lower TTLs in advance: This is crucial for a faster cutover.</li>
<li>Disable DNSSEC before NS change (safest): Remove DS records at the registrar well before changing nameservers, then re-enable DNSSEC via Cloudflare.</li>
<li>Verify, verify, verify: Double-check record imports and functionality at each stage.</li>
<li>Test thoroughly: From multiple locations and for all critical services.</li>
<li>Have a rollback plan: Know how to revert if necessary.</li>
<li>Migrate during low traffic: Minimize potential user impact.</li>
<li>Address BIND Views/ACLs: Understand how Cloudflare will handle or replace this functionality.</li>
<li>Take advantage of Cloudflare features: Once stable, explore and implement Cloudflare's security and performance enhancements.</li>
</ul>
<p>By following these best practices, you can significantly increase the likelihood of a smooth and successful migration from your on-prem BIND DNS to Cloudflare.</p>
