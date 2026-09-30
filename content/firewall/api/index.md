---
cp9:
  canonical: https://developers.cloudflare.com/firewall/api/
  description: Manage firewall rules programmatically via APIs.
  full_title: Manage firewall rules via the APIs · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Manage firewall rules via the APIs · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage firewall rules programmatically via APIs."><link rel="canonical" href="https://developers.cloudflare.com/firewall/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/api/index.md"><meta property="og:title" content="Manage firewall rules via the APIs · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage firewall rules programmatically via APIs."><meta property="og:url" content="https://developers.cloudflare.com/firewall/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/firewall/api/#page","headline":"Manage firewall rules via the APIs \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Manage firewall rules programmatically via APIs.","url":"https://developers.cloudflare.com/firewall/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/api/
  schema: 1
---
<p>Cloudflare offers APIs that work together to achieve the same effect as the UI-based <strong>Firewall rules</strong> feature under <strong>Security</strong> &gt; <strong>WAF</strong>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8700.md")
</aside>
<p>These APIs are the following:</p>
<ul>
<li><a href="/firewall/api/cf-firewall-rules/"><strong>Firewall Rules API</strong></a>: Manage firewall rules and their actions, based on criteria separately defined through filters.</li>
<li><a href="/firewall/api/cf-filters/"><strong>Filters API</strong></a>: Manage the filters that enable rule matching.</li>
<li><a href="/waf/tools/lists/lists-api/"><strong>Lists API</strong></a>: Manage named lists of items (such as IP addresses) that you can use in the rules of different Cloudflare products.</li>
</ul>
