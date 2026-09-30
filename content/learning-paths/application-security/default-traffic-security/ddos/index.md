---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/
  description: Understand automatic DDoS attack mitigation.
  full_title: DDoS Protection · Cloudflare Learning Paths
  head_html: <title>DDoS Protection · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Understand automatic DDoS attack mitigation."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/index.md"><meta property="og:title" content="DDoS Protection · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand automatic DDoS attack mitigation."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="WAF,DDoS Protection,SSL/TLS,DNS,Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/#page","headline":"DDoS Protection \u00b7 Cloudflare Learning Paths","description":"Understand automatic DDoS attack mitigation.","url":"https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/application-security/default-traffic-security/ddos/
  schema: 1
---
<p>Cloudflare automatically detects and mitigates DDoS attacks using its <a href="/ddos-protection/about/components/#autonomous-edge">Autonomous Edge</a>, which is always-on. <code>Advanced</code> protections are reserved for Magic Transit customers.</p>
<table>
<thead>
<tr>
<th>OSI Layer</th>
<th>Ruleset / Feature</th>
<th>Example of covered DDoS attack vectors</th>
</tr>
</thead>
<tbody>
<tr>
<td>L3/4</td>
<td><a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection</a></td>
<td>ACK floods<br/>BitTorrent reflection attack<br/>Carpet Bombing attacks<br/>CHARGEN reflection attacks<br/>DNS amplification attack<br/>DNS Garbage Flood<br/>DNS NXDOMAIN flood<br/>DNS Query flood<br/>DTLS amplification attacks<br/>ESP flood<br/>GRE floods<br/><span class="nb-glossary-tooltip" title="ICMP">ICMP</span> flood attack<br/>Jenkins amplification attacks<br/>Lantronix reflection attacks<br/>mDNS DDoS attacks<br/>Memcached amplification attacks<br/>Mirai and Mirai-variant L3/4 attacks<br/>MSSQL reflection attacks<br/>NetBios DDoS attacks<br/>Out of state TCP attacks<br/>Protocol violation attacks<br/>QUIC flood attack<br/>Quote of the Day (QOTD) reflection attacks<br/>RST flood<br/>SIP attacks<br/>SNMP flood attack<br/>SPSS reflection attacks<br/>SSDP reflection attacks<br/>SYN floods<br/>SYN-ACK reflection attack<br/>TeamSpeak 3 floods<br/>Ubiquity reflection attacks<br/>UDP flood attack<br/>VxWorks DDoS attacks<br/><br/>For more DNS protection options, refer to <a href="/ddos-protection/about/attack-coverage/#getting-additional-dns-protection">Getting additional DNS protection</a>.</td>
</tr>
<tr>
<td>L3/4</td>
<td><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup></td>
<td>Fully randomized and spoofed ACK floods, SYN floods, SYN-ACK reflection attacks, and other sophisticated TCP-based DDoS attacks</td>
</tr>
<tr>
<td>L7 (DNS)</td>
<td><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup></td>
<td>Sophisticated and fully randomized DNS attacks, including Water Torture attacks, Random-prefix attacks, and DNS laundering attacks.</td>
</tr>
<tr>
<td>L7 (HTTP/S)</td>
<td><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a></td>
<td>Cache busting attacks<br/>Carpet Bombing attacks<br/>HTTP Continuation flood<br/>HTTP flood attack<br/>HTTP/2 MadeYouReset<br/>HTTP/2 Rapid Reset<br/>HULK attack<br/>Known DDoS botnets<br/>LOIC attack<br/>Mirai and Mirai-variant HTTP attacks<br/>Slowloris attack<br/>TLS/SSL exhaustion attacks<br/>TLS/SSL negotiation attacks<br/>WordPress pingback attack<br/></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-ddos-protection-ddos-attack-coverage-mdx-1">Available to Magic Transit customers.</li></ol></section>
<p>Refer to the learning path <a href="/learning-paths/prevent-ddos-attacks/concepts/">Prevent DDoS attacks</a>  to dive deeper into this subject.</p>
