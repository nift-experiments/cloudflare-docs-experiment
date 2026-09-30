---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/
  description: Learn about restrict external connections in this guide.
  full_title: Restrict external connections · Cloudflare Learning Paths
  head_html: <title>Restrict external connections · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about restrict external connections in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/index.md"><meta property="og:title" content="Restrict external connections · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about restrict external connections in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="DDoS Protection,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/#page","headline":"Restrict external connections \u00b7 Cloudflare Learning Paths","description":"Learn about restrict external connections in this guide.","url":"https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/prevent-ddos-attacks/advanced/prevent-external-connections/
  schema: 1
---
<p>To fully secure your origin, you should limit or restrict external connections to your origin server. These suggestions vary in their level of completeness and complexity and depend on your application and origin setup.</p>
<h2 id="application-layer">Application layer</h2>
<details class="nb-details"><summary>Cloudflare Tunnel (HTTP / WebSockets)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9843.md")
</div></details>
<details class="nb-details"><summary>HTTP Header Validation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9844.md")
</div></details>
<details class="nb-details"><summary>JSON Web Tokens (JWT) Validation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9845.md")
</div></details>
<h2 id="transport-layer">Transport Layer</h2>
<details class="nb-details"><summary>Authenticated Origin Pulls</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9846.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Tunnel (SSH / RDP)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9847.md")
</div></details>
<h2 id="network-layer">Network Layer</h2>
<details class="nb-details"><summary>Allowlist Cloudflare IP addresses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9848.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Magic Transit</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9849.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Network Interconnect</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9850.md")
</div></details>
<details class="nb-details"><summary>Dedicated CDN Egress IPs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9853.md")
</div></details>
