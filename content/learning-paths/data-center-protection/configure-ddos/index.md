---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/
  description: Learn about configure ddos protection in this guide.
  full_title: Configure DDoS protection · Cloudflare Learning Paths
  head_html: <title>Configure DDoS protection · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about configure ddos protection in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/index.md"><meta property="og:title" content="Configure DDoS protection · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about configure ddos protection in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Magic Transit,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/#page","headline":"Configure DDoS protection \u00b7 Cloudflare Learning Paths","description":"Learn about configure ddos protection in this guide.","url":"https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/data-center-protection/configure-ddos/
  schema: 1
---
<p>Cloudflare DDoS protection automatically detects and mitigates Distributed Denial of Service (DDoS) attacks using its Autonomous Edge. Magic Transit customers have access to additional features, such as:</p>
<ul>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP protection</a> (disabled by default)</li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS protection (beta)</a></li>
</ul>
<h2 id="create-a-ddos-override">Create a DDoS override</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9622.md")
</div>
<h2 id="ddos-advanced-protection">DDoS advanced protection</h2>
<h3 id="advanced-tcp-protection">Advanced TCP Protection</h3>
<p>Cloudflare's Advanced TCP Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, is a stateful TCP inspection engine used to detect and mitigate sophisticated out-of-state TCP attacks such as randomized and spoofed ACK floods or SYN and SYN-ACK floods.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9618.md")
</aside>
<h4 id="setup">Setup</h4>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/#rules">Create a global configuration</a> to set up SYN Flood and Out-of-state TCP rules and filters for Advanced TCP Protection.</p>
<h3 id="advanced-dns-protection">Advanced DNS Protection</h3>
<p>Cloudflare's Advanced DNS Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, provides stateful protection against DNS-based DDoS attacks, specifically sophisticated and fully randomized DNS attacks such as <a href="/dns/dns-firewall/random-prefix-attacks/about/">random prefix attacks</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9617.md")
</aside>
<h4 id="setup-1">Setup</h4>
<p><a href="/ddos-protection/advanced-ddos-systems/how-to/create-rule/#create-an-advanced-dns-protection-rule">Create a rule</a> to enable Advanced DNS Protection.</p>
