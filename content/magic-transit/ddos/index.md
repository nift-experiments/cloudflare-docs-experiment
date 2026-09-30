---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/ddos/
  description: DDoS mitigation layers available to Magic Transit customers.
  full_title: Cloudflare DDoS protection · Cloudflare Magic Transit docs
  head_html: <title>Cloudflare DDoS protection · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="DDoS mitigation layers available to Magic Transit customers."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/ddos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/ddos/index.md"><meta property="og:title" content="Cloudflare DDoS protection · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DDoS mitigation layers available to Magic Transit customers."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/ddos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/magic-transit/ddos/#page","headline":"Cloudflare DDoS protection \u00b7 Cloudflare Magic Transit docs","description":"DDoS mitigation layers available to Magic Transit customers.","url":"https://developers.cloudflare.com/magic-transit/ddos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /magic-transit/ddos/
  schema: 1
---
<p>Cloudflare <a href="/ddos-protection/">DDoS protection</a> automatically detects and mitigates DDoS attacks using the <a href="/ddos-protection/about/components/#autonomous-edge">Autonomous Edge</a>. Magic Transit customers get multiple layers of protection, from always-on managed rulesets to advanced systems that you can configure for your specific traffic patterns.</p>
<h2 id="mitigation-layers">Mitigation layers</h2>
<h3 id="ddos-managed-rulesets">DDoS managed rulesets</h3>
<p>The <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS managed ruleset</a> provides pre-configured rules that detect and mitigate L3/L4 DDoS attacks. The ruleset is always enabled and cannot be turned off. Magic Transit and Spectrum Enterprise customers can <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">customize the ruleset behavior</a> by adjusting the action and sensitivity level for individual rules or groups of rules.</p>
<h3 id="advanced-tcp-protection">Advanced TCP Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> detects and mitigates SYN flood attacks and out-of-state TCP attacks. It uses <code>flowtrackd</code> to learn your normal TCP traffic patterns and identify anomalous flows. You can create rules scoped globally, by region, or by data center, and set each rule to monitoring or mitigation mode.</p>
<h3 id="advanced-dns-protection">Advanced DNS Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> detects and mitigates DNS-over-UDP DDoS attacks. Like Advanced TCP Protection, it uses <code>flowtrackd</code> to build a traffic profile and identify volumetric DNS anomalies. You can create rules with configurable burst, rate, and profile sensitivity levels.</p>
<h3 id="programmable-flow-protection">Programmable Flow Protection</h3>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> lets you write custom eBPF programs to inspect UDP payloads at the packet level. It is designed for custom or standardized L7 UDP-based protocols such as gaming, VoIP, financial services, and streaming. Programmable Flow Protection is available as an add-on for Magic Transit customers.</p>
<h3 id="network-firewall">Network Firewall</h3>
<p><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> lets you create custom packet-level firewall rules to filter traffic by protocol, port, IP address, packet length, and other attributes. Network Firewall is included with Magic Transit.</p>
<h2 id="automatic-activation">Automatic activation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/783.md")
</aside>
<p>After the initial monitoring period, review your traffic in <a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> to observe what would have been mitigated, then switch your rules from monitoring to mitigation mode. For more information, refer to <a href="/ddos-protection/advanced-ddos-systems/overview/">Advanced DDoS Systems general settings</a>.</p>
<h2 id="execution-order">Execution order</h2>
<p>When traffic enters the Cloudflare network, it passes through mitigation systems in the following order:</p>
<ol>
<li><a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a></li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a></li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a></li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a></li>
</ol>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> operates within the Advanced DDoS Protection layer for UDP-based protocols.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/magic-transit/how-to/verify-ddos-protection/">Verify your DDoS protection</a>: Confirm that your DDoS mitigation layers are active and correctly configured.</li>
<li><a href="/ddos-protection/">DDoS Protection overview</a>: Learn about Cloudflare DDoS Protection across all products.</li>
<li><a href="/ddos-protection/best-practices/proactive-defense/">Best practices for DDoS protection</a>: Review proactive defense recommendations, including steps specific to Magic Transit.</li>
</ul>
