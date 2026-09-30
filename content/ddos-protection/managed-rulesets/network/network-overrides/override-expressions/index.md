---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/
  description: Expression fields and operators for scoping Network-layer DDoS overrides.
  full_title: Override expressions for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs
  head_html: <title>Override expressions for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Expression fields and operators for scoping Network-layer DDoS overrides."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/index.md"><meta property="og:title" content="Override expressions for Network-layer DDoS Attack Protection · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expression fields and operators for scoping Network-layer DDoS overrides."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="TCP,UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/#page","headline":"Override expressions for Network-layer DDoS Attack Protection \u00b7 Cloudflare DDoS Protection docs","description":"Expression fields and operators for scoping Network-layer DDoS overrides.","url":"https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TCP","UDP"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/managed-rulesets/network/network-overrides/override-expressions/
  schema: 1
---
<p>Set an override expression for the Network-layer DDoS Attack Protection managed ruleset to define a specific scope for <a href="/ddos-protection/managed-rulesets/network/override-parameters/#sensitivity-level">sensitivity level</a> or <a href="/ddos-protection/managed-rulesets/network/override-parameters/#action">action</a> adjustments.</p>
<p>When considering which, if any, expressions you should utilize, think of expressions as a tool to scope overrides to the specific service that the Network-layer DDoS Attack Protection managed ruleset is protecting. That is to say that most services are defined by their destination ports and IPs as opposed to source ports or IPs. Refer to <a href="/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/#important-remarks">Important remarks</a> for more information.</p>
<p>For example, you can set different sensitivity levels for different destination IP addresses or ports: a medium sensitivity level for destination IP address <code>A</code> and a low sensitivity level for destination IP address <code>B</code>.</p>
<h2 id="available-expression-fields">Available expression fields</h2>
<p>The following fields are made available for use in override expressions.</p>
<p>The list of fields we recommend using in expressions:</p>
<ul>
<li><code>ip.dst</code></li>
<li><code>ip.proto.num</code></li>
<li><code>tcp.dstport</code></li>
<li><code>tcp.flags</code></li>
<li><code>tcp.flags.ack</code></li>
<li><code>tcp.flags.fin</code></li>
<li><code>tcp.flags.push</code></li>
<li><code>tcp.flags.reset</code></li>
<li><code>tcp.flags.syn</code></li>
<li><code>tcp.flags.urg</code></li>
<li><code>udp.dstport</code></li>
</ul>
<p>The list of fields we do not recommend to be used in expressions:</p>
<ul>
<li><code>ip.src</code></li>
<li><code>ip.len</code></li>
<li><code>ip.ttl</code></li>
<li><code>tcp.srcport</code></li>
<li><code>udp.srcport</code></li>
</ul>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> in the Rules language documentation for more information.</p>
<h2 id="important-remarks">Important remarks</h2>
<h3 id="recommended-vs-non-recommended-fields">Recommended vs. non-recommended fields</h3>
<p>Override expressions are not allowlists. Overrides are applied to the detection, and are not applied to the resulting mitigation. This means an override only takes effect if the attack fingerprint, as generated by the DDoS managed rules, includes the same fields specified in your expression. Thus, it makes the use of source fields like <code>ip.src</code>, <code>ip.len</code>, <code>ip.ttl</code>, <code>tcp.srcport</code>, and <code>udp.srcport</code> unreliable.</p>
<p>The use of non-recommended fields in an expression may result in unexpected behavior. While you may be inclined to utilize source properties, the expressions are not allowlists and including source traffic properties may result in false positives.</p>
<p>For example, if you create an override with sensitivity set to <code>Essentially Off</code> for <code>ip.src eq 192.0.2.1</code>, it only applies if the fingerprint includes <code>ip.src</code>. However, because DDoS attacks are often distributed across many source IPs, the fingerprint may not include <code>ip.src</code> at all. In such cases, your override is not applied.</p>
<p>In a common scenario, an attack originating from thousands of IPs can target a single destination IP and port. The fingerprint would focus on the shared attributes, such as the destination IP, port, and additional packet fields that represent strong signals of the attack pattern. Even if your override matches a specific source IP, it will not apply if that field is not present in the fingerprint. As a result, the system will mitigate the attack using the default high sensitivity, and traffic from your specified IP could still be blocked. It is recommended to use more stable expressions such as protocol, destination IP, and destination port.</p>
<h3 id="character-limits">Character limits</h3>
<p>Each expression is limited to 4,000 characters, which means you can enter approximately a maximum of 200 IP addresses in a single expression. However, you can enter IP addresses in CIDR format, which allows you to include a larger number of IP addresses. For example, you can use <code>192.0.0.0/24</code> to match IP addresses from <code>192.0.0.0</code> to <code>192.0.0.255</code>.</p>
