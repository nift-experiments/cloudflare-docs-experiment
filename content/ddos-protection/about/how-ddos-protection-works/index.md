---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/
  description: How Cloudflare analyzes traffic and applies autonomous mitigation at the network edge.
  full_title: How DDoS protection works · Cloudflare DDoS Protection docs
  head_html: <title>How DDoS protection works · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cloudflare analyzes traffic and applies autonomous mitigation at the network edge."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/index.md"><meta property="og:title" content="How DDoS protection works · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cloudflare analyzes traffic and applies autonomous mitigation at the network edge."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/#page","headline":"How DDoS protection works \u00b7 Cloudflare DDoS Protection docs","description":"How Cloudflare analyzes traffic and applies autonomous mitigation at the network edge.","url":"https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/about/how-ddos-protection-works/
  schema: 1
---
<p>To detect and mitigate <span class="nb-glossary-tooltip" title="distributed denial-of-service (DDoS) attack">DDoS attacks</span>, Cloudflare's autonomous edge and centralized DDoS systems analyze traffic samples out of path, which allows Cloudflare to asynchronously detect DDoS attacks without causing latency or impacting performance.</p>
<p>The analyzed samples include:</p>
<ul>
<li><strong>Packet fields</strong> such as the source IP, source port, destination IP, destination port, protocol, TCP flags, sequence number, options, and packet rate.</li>
<li><strong>HTTP request metadata</strong> such as HTTP headers, user agent, query-string, path, host, HTTP method, HTTP version, TLS cipher version, and request rate.</li>
<li><strong>HTTP response metrics</strong> such as error codes returned by customers' origin servers and their rates.</li>
</ul>
<p>Cloudflare uses a set of dynamic rules that scan for attack patterns, known attack tools, suspicious patterns, protocol violations, requests causing large amounts of origin errors, excessive traffic hitting the origin or cache, and additional attack vectors. Each rule has a predefined sensitivity level and default action that varies based on the rule's confidence that the traffic is indeed part of an attack.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7474.md")
</aside>
<p>Once attack traffic matches a rule, Cloudflare's systems will track that traffic and generate a real-time signature to surgically match against the attack pattern and mitigate the attack without impacting legitimate traffic. The rules are able to generate different signatures based on various properties of the attacks and the signal strength of each attribute. For example, if the attack is distributed — that is, originating from many source IPs — then the source IP field will not serve as a strong indicator, and the rule will not choose the source IP field as part of the attack signature. Once generated, the fingerprint is propagated as a mitigation rule to the most optimal location on the Cloudflare global network for cost-efficient mitigation. These mitigation rules are ephemeral and will expire shortly after the attack has ended, which happens when no additional traffic has been matched to the rule.</p>
<table>
<thead>
<tr>
<th>Actions</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block</td>
<td>Matching requests are denied access to the site.</td>
</tr>
<tr>
<td>Managed Challenge</td>
<td>Depending on the characteristics of a request, Cloudflare will choose an appropriate type of challenge.</td>
</tr>
<tr>
<td>Interactive Challenge</td>
<td>The client that made the request must pass an interactive Challenge.</td>
</tr>
<tr>
<td>Log</td>
<td>Records matching requests in the Cloudflare Logs.</td>
</tr>
<tr>
<td>Use rule defaults</td>
<td>Uses the default action that is pre-defined for each rule.</td>
</tr>
</tbody>
</table>
<h2 id="thresholds">Thresholds</h2>
<p>Thresholds vary for each rule and there are different thresholds globally and per colocation. Within a rule, the traffic is fingerprinted and the thresholds are per fingerprint, and it is difficult to know ahead of time which rules, colocations, or fingerprints your traffic generates, so the threshold numbers are not necessarily valuable.</p>
<p>Instead, Cloudflare's DDoS Protection system provides the sensitivity adjustment. If you experience a false positive, you can decrease the sensitivity. You can also use the <code>Log</code> action to help find an appropriate sensitivity level. You can decrease the sensitivity while in <code>Log</code> mode until the rule no longer matches.</p>
<h2 id="time-to-mitigate">Time to mitigate</h2>
<ul>
<li>Immediate mitigation for Advanced TCP and DNS Protection systems.</li>
<li>Up to three seconds on average for the detection and mitigation of L3/4 DDoS attacks at the edge using the Network-layer DDoS Protection Managed rules.</li>
<li>Up to three seconds on average for the detection and mitigation of HTTP DDoS attacks at the edge using the HTTP DDoS Protection Managed rules.</li>
</ul>
<h2 id="data-localization">Data localization</h2>
<p>To learn more about how DDoS protection works with data localization, refer to the Data Localization Suite <a href="/data-localization/compatibility/">product compatibility</a>.</p>
