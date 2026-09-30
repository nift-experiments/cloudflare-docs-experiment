---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/plans/
  description: Compare Network Firewall features by plan.
  full_title: Plans · Cloudflare Network Firewall docs
  head_html: <title>Plans · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Compare Network Firewall features by plan."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/plans/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/plans/index.md"><meta property="og:title" content="Plans · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Compare Network Firewall features by plan."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/plans/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/plans/#page","headline":"Plans \u00b7 Cloudflare Network Firewall docs","description":"Compare Network Firewall features by plan.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/plans/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/plans/
  schema: 1
---
<p>If you are a <a href="/magic-transit/">Magic Transit</a> or <a href="/cloudflare-wan/">Cloudflare WAN</a> user, you are automatically provided with a standard list of Cloudflare Network Firewall (formerly Magic Firewall) features. For additional features available for purchase, refer to the list of advanced features below.</p>
<h2 id="standard-features">Standard features</h2>
<ul>
<li>Filtering rules based on protocol, port, IP addresses, <span class="nb-glossary-tooltip" title="data packet">packet</span> length, and <span class="nb-glossary-tooltip" title="bit field matching">bit field match</span>.</li>
<li>Fast propagation of rule changes in less than a minute.</li>
<li>Single dashboard to manage <span class="nb-glossary-tooltip" title="firewall">firewall</span> and network configuration.</li>
<li>Programmable API for automated deployment and management — compatible with infrastructure-as-code platforms like <a href="/terraform/">Terraform</a>.</li>
<li>Traffic analytics per rule in the dashboard and using the <a href="/analytics/graphql-api/">GraphQL API</a>.</li>
<li>Integration with <a href="/cloudflare-wan/">Cloudflare WAN network-as-a-service</a>.</li>
<li>Included DDoS protection with <a href="/magic-transit/">Magic Transit</a>.</li>
</ul>
<h2 id="advanced-features">Advanced features</h2>
<p>All standard features are included with the purchase of the advanced features below:</p>
<ul>
<li>Customizable IP lists.</li>
<li>Managed threat intelligence IP lists (Anonymizer, Botnet, Malware, Open Proxies, VPNs).</li>
<li>Geoblocking based on user location by country.</li>
<li>Block or allow packets based on Autonomous System Number (ASN).</li>
<li>Packet captures on demand for network troubleshooting.</li>
<li><a href="/cloudflare-network-firewall/about/protocol-validation-rules/">Protocol validation rules</a> to inspect traffic validity and enforce a positive security model.</li>
<li><a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> filtering for outbound Internet traffic (network and HTTP policies). The Secure Web Gateway supports all TCP and UDP ports, as well as traffic sourced from RFC 1918 address space. Gateway will proxy BYOIP traffic to egress via the default Cloudflare IPs or your assigned <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>.</li>
<li>Intrusion Detection System (IDS).</li>
</ul>
