---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/about/attack-coverage/
  description: DDoS attack types covered by Cloudflare managed rulesets at layers 3, 4, and 7.
  full_title: DDoS attack coverage · Cloudflare DDoS Protection docs
  head_html: <title>DDoS attack coverage · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="DDoS attack types covered by Cloudflare managed rulesets at layers 3, 4, and 7."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/about/attack-coverage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/about/attack-coverage/index.md"><meta property="og:title" content="DDoS attack coverage · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DDoS attack types covered by Cloudflare managed rulesets at layers 3, 4, and 7."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/about/attack-coverage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/about/attack-coverage/#page","headline":"DDoS attack coverage \u00b7 Cloudflare DDoS Protection docs","description":"DDoS attack types covered by Cloudflare managed rulesets at layers 3, 4, and 7.","url":"https://developers.cloudflare.com/ddos-protection/about/attack-coverage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/about/attack-coverage/
  schema: 1
---
<p>The <a href="/ddos-protection/managed-rulesets/">DDoS Attack Protection managed rulesets</a> provide protection against a variety of <span class="nb-glossary-tooltip" title="distributed denial-of-service (DDoS) attack">DDoS attacks</span> across L3/4 (layers 3/4) and L7 of the OSI model. Cloudflare constantly updates these managed rulesets to improve the attack coverage, increase the mitigation consistency, cover new and emerging threats, and ensure cost-efficient mitigations.</p>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>, <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>, and <a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> are available to Magic Transit customers. Advanced TCP Protection provides additional protection against sophisticated TCP-based DDoS attacks. Advanced DNS Protections protects against sophisticated and fully randomized DNS attacks. Programmable Flow Protection mitigates UDP-based attacks by executing a customer-defined program.</p>
<p>As a general guideline, various Cloudflare products operate on different open systems interconnection (OSI) layers and you are protected up to the layer on which your service operates. You can customize the DDoS settings on the layer in which you onboarded. For example, since the CDN/WAF service is a Layer 7 (HTTP/HTTPS) service, Cloudflare provides protection from DDoS attacks on L7 downwards, including L3/4 attacks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7477.md")
</aside>
<p>The following table includes a sample of covered attack vectors:</p>
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
<h2 id="getting-additional-dns-protection">Getting additional DNS protection</h2>
<p>The Network-layer DDoS Attack Protection managed ruleset provides protection against some types of DNS attacks.</p>
<p>Magic Transit customers have access to <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> <span class="nb-badge">Beta</span>. Other customers might consider the following options:</p>
<ul>
<li>Use Cloudflare as your authoritative DNS provider (<a href="/dns/zone-setups/full-setup/">primary DNS</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary DNS</a>).</li>
<li>If you are running your own <span class="nb-glossary-tooltip" title="nameserver">nameservers</span>, use <a href="/dns/dns-firewall/">DNS Firewall</a> to get additional protection against DNS attacks like random prefix attacks.</li>
</ul>
<h2 id="email-based-attacks">Email-based attacks</h2>
<p>DDoS Protection covers web and network protocols, including TCP, UDP, DNS, and HTTP/S. It does not cover email protocols such as SMTP, IMAP, or POP3.</p>
<p>For protection against email-borne threats such as phishing and malware, refer to <a href="/email-security/">Email Security</a>.</p>
