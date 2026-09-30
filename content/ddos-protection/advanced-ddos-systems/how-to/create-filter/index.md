---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/
  description: Create a filter to define traffic characteristics for Advanced TCP Protection rules.
  full_title: Create a filter for Advanced TCP Protection · Cloudflare DDoS Protection docs
  head_html: <title>Create a filter for Advanced TCP Protection · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a filter to define traffic characteristics for Advanced TCP Protection rules."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/index.md"><meta property="og:title" content="Create a filter for Advanced TCP Protection · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a filter to define traffic characteristics for Advanced TCP Protection rules."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/#page","headline":"Create a filter for Advanced TCP Protection \u00b7 Cloudflare DDoS Protection docs","description":"Create a filter to define traffic characteristics for Advanced TCP Protection rules.","url":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/advanced-ddos-systems/how-to/create-filter/
  schema: 1
---
<p>A filter modifies Advanced TCP Protection's <a href="/ddos-protection/advanced-ddos-systems/concepts/#mode">execution mode</a> — monitoring, mitigation (enabled), or disabled — for all incoming packets matching an expression.</p>
<p>Each protection system component (SYN flood protection or out-of-state TCP protection) should have at least one <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule">rule</a>, but filters are optional.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7504.md")
</aside>
<h2 id="procedure">Procedure</h2>
<p>To create a <a href="/ddos-protection/advanced-ddos-systems/concepts/#filter">filter</a> for one of the system components:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7506.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/7503.md")
</aside>
