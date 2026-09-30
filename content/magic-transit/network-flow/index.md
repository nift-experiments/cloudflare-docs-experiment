---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/network-flow/
  description: Monitor Magic Transit traffic with Network Flow.
  full_title: Network Flow · Cloudflare Magic Transit docs
  head_html: <title>Network Flow · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor Magic Transit traffic with Network Flow."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/network-flow/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/network-flow/index.md"><meta property="og:title" content="Network Flow · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor Magic Transit traffic with Network Flow."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/network-flow/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/magic-transit/network-flow/#page","headline":"Network Flow \u00b7 Cloudflare Magic Transit docs","description":"Monitor Magic Transit traffic with Network Flow.","url":"https://developers.cloudflare.com/magic-transit/network-flow/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /magic-transit/network-flow/
  schema: 1
---
<p><a href="/magic-transit/on-demand/">Magic Transit On Demand</a> allows you to keep Magic Transit disabled during normal operations and activate it only when you need DDoS protection. Network Flow monitors your traffic while Magic Transit is off and detects attacks. When an attack is detected, you can enable Magic Transit automatically or manually.</p>
<p>You can create Network Flow rules that monitor specific IP <span class="nb-glossary-tooltip" title="prefix">prefixes</span> for DDoS attacks. When an attack is detected, Cloudflare notifies you by email, <a href="/notifications/get-started/configure-webhooks/">webhook</a>, or <a href="/notifications/get-started/configure-pagerduty/">PagerDuty</a>.</p>
<p>If you enable <a href="#activate-ip-auto-advertisement">auto-advertisement</a> on a rule, Magic Transit activates automatically to protect the targeted prefixes. You can enable auto-advertisement for individual Network Flow rules through the dashboard or API.</p>
<p>After Magic Transit activates and your traffic flows through Cloudflare, Cloudflare blocks malicious DDoS traffic. Your origin servers receive only clean traffic through IPsec or GRE tunnels.</p>
<p>The following diagrams illustrate this process:</p>
<div class="nb-width">
@markup("md", "content/.markup/bodies/757.md")
</div>
<div class="nb-width">
@markup("md", "content/.markup/bodies/758.md")
</div>
<div class="nb-width">
@markup("md", "content/.markup/bodies/759.md")
</div>
<h2 id="activate-ip-auto-advertisement">Activate IP auto-advertisement</h2>
<p>Before a rule can automatically activate Magic Transit, you must enable IP advertisement for the relevant prefixes. You can do this through the dashboard or the API.</p>
<h3 id="dashboard">Dashboard</h3>
<p>To activate IP advertisement through the Cloudflare dashboard, refer to <a href="/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement">Configure dynamic advertisement</a>.</p>
<h3 id="api">API</h3>
<p>To activate IP advertisement through the API, refer to the <a href="/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/">IP Address Management Dynamic Advertisement API</a>.</p>
<h2 id="network-flow-rules">Network Flow rules</h2>
<p>To create Network Flow rules with auto-advertisement, refer to <a href="/network-flow/rules/#rule-auto-advertisement">Rule Auto-Advertisement</a>.</p>
