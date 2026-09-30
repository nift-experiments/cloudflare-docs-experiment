---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/
  description: Layer 3 and 4 DDoS protection for TCP and UDP Spectrum applications.
  full_title: DDoS Protection for Spectrum · Cloudflare Spectrum docs
  head_html: <title>DDoS Protection for Spectrum · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Layer 3 and 4 DDoS protection for TCP and UDP Spectrum applications."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/index.md"><meta property="og:title" content="DDoS Protection for Spectrum · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Layer 3 and 4 DDoS protection for TCP and UDP Spectrum applications."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Spectrum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/#page","headline":"DDoS Protection for Spectrum \u00b7 Cloudflare Spectrum docs","description":"Layer 3 and 4 DDoS protection for TCP and UDP Spectrum applications.","url":"https://developers.cloudflare.com/spectrum/about/ddos-for-spectrum/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /spectrum/about/ddos-for-spectrum/
  schema: 1
---
<p>Spectrum provides DDoS Protection at layers 3-4 of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>, that is against TCP and UDP based DDoS attacks.</p>
<p>Spectrum works as a layer 4 reverse proxy, therefore a proper TCP connection must be first established before traffic is proxied to the origin. This moves any impact of SYN or SYN-ACK reflection attacks to the Cloudflare global network. Additionally, by using Spectrum in front of your application, your origin IP is concealed — preventing attackers from targeting your origin server directly. It is also recommended that you replace your origin IP address after moving to Cloudflare, and lock it down to only accept traffic from <a href="https://www.cloudflare.com/ips/">Cloudflare’s IP address range</a>.</p>
<p>Random or out-of-state TCP packets should not be passed to the origin if a legitimate TCP connection has not yet been established between the client and Cloudflare. Spectrum also <a href="https://blog.cloudflare.com/syn-packet-handling-in-the-wild/">leverages SYN cookie challenges as part of the Linux networking stack</a> to defend against floods.</p>
<p>Furthermore, if a flood of packets of an unspecified protocol target your application (for example, your Spectrum application is for TCP traffic, and a UDP flood targets your Spectrum application), the packets will be dropped. Similarly, if packets target a port or port range that you did not specify, they will also be dropped.</p>
<p>L3/4 DDoS attacks should be detected and mitigated by the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a> that is enabled by default. This ruleset detects and mitigates DDoS attacks by dynamically fingerprinting attacks based on packet header fields.</p>
<p>For protecting HTTP/S applications against L7 DDoS attacks and to benefit from caching and additional features, onboard your application to Cloudflare’s Web Application Firewall/Content Delivery Network service, which works in tandem with Cloudflare Spectrum.</p>
<p>Refer to <a href="/ddos-protection/">Cloudflare DDoS Protection</a> to learn more.</p>
<hr />
<h2 id="mitigation-reasons">Mitigation reasons</h2>
<p>The <strong>Mitigation reason</strong> field shown in the <strong>DDoS managed rules</strong> tab of <a href="/analytics/network-analytics/">Network Analytics</a> (<strong>Networking</strong> &gt; <strong>Insights</strong> &gt; <strong>Network Analytics</strong> in the dashboard) will contain more information on why a given packet was dropped by the Spectrum system.</p>
<p>The mitigation reasons are the following:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Blocked</strong></td>
<td>Packet dropped because it matched a DDoS protection rule.</td>
</tr>
<tr>
<td><strong>Rate limited</strong></td>
<td>Packet dropped because it exceeded rate limits.</td>
</tr>
<tr>
<td><strong>Connection limited</strong></td>
<td>Packet dropped because it exceeded connection limits.</td>
</tr>
<tr>
<td><strong>Unexpected</strong></td>
<td>Packet dropped because it was not expected given the current state of the connection it was associated with.</td>
</tr>
<tr>
<td><strong>Not found</strong></td>
<td>Packet dropped because it does not match any configured Spectrum application on the destination IP address and port.</td>
</tr>
</tbody>
</table>
