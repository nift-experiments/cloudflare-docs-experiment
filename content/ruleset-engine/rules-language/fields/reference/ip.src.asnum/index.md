---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/
  description: The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.
  full_title: ip.src.asnum · Cloudflare Ruleset Engine docs
  head_html: <title>ip.src.asnum · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="ip.src.asnum · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/#page","headline":"ip.src.asnum \u00b7 Cloudflare Ruleset Engine docs","description":"The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/ip.src.asnum/
  schema: 1
---
<h1 id="ip-src-asnum">ip.src.asnum</h1>

**Data type:** Number

<p>The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.</p>

<p>This field has the same value as the <code>ip.geoip.asnum</code> field, which is deprecated. The <code>ip.geoip.asnum</code> field is still available for new and existing rules, but you should use the <code>ip.src.asnum</code> field instead.</p>
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>

<h2 id="categories">Categories</h2>

- Request
- Geolocation

**Keywords:** request, location, geolocation, asn, ip.geoip.asnum, client, visitor

