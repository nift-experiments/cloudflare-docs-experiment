---
cp9:
  canonical: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/
  description: Enable automatic mitigation of random prefix attacks in the Cloudflare dashboard or via the API.
  full_title: Protect against random prefix attacks · Cloudflare DNS docs
  head_html: <title>Protect against random prefix attacks · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable automatic mitigation of random prefix attacks in the Cloudflare dashboard or via the API."><link rel="canonical" href="https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/index.md"><meta property="og:title" content="Protect against random prefix attacks · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable automatic mitigation of random prefix attacks in the Cloudflare dashboard or via the API."><meta property="og:url" content="https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/#page","headline":"Protect against random prefix attacks \u00b7 Cloudflare DNS docs","description":"Enable automatic mitigation of random prefix attacks in the Cloudflare dashboard or via the API.","url":"https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dns-firewall/random-prefix-attacks/setup/
  schema: 1
---
<p>In order to enable automatic mitigation of <a href="/dns/dns-firewall/random-prefix-attacks/about/">random prefix attacks</a>:</p>
<ol>
<li>Set up <a href="/dns/dns-firewall/setup/">DNS Firewall</a>.</li>
<li>Enable attack mitigation on your DNS Firewall cluster.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7737.md")
</div></div>
<p>Once you turn on attack mitigation, Cloudflare returns a <code>REFUSED</code> response to queries that are part of a random prefix attack.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7734.md")
</aside>
