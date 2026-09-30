---
cp9:
  canonical: https://developers.cloudflare.com/realtime/turn/
  description: Cloudflare Realtime TURN relays WebRTC traffic through NATs and firewalls on a global network.
  full_title: TURN Service · Cloudflare Realtime docs
  head_html: <title>TURN Service · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Realtime TURN relays WebRTC traffic through NATs and firewalls on a global network."><link rel="canonical" href="https://developers.cloudflare.com/realtime/turn/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/turn/index.md"><meta property="og:title" content="TURN Service · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Realtime TURN relays WebRTC traffic through NATs and firewalls on a global network."><meta property="og:url" content="https://developers.cloudflare.com/realtime/turn/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/turn/#page","headline":"TURN Service \u00b7 Cloudflare Realtime docs","description":"Cloudflare Realtime TURN relays WebRTC traffic through NATs and firewalls on a global network.","url":"https://developers.cloudflare.com/realtime/turn/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/turn/
  schema: 1
---
<p>Separately from the SFU, Realtime offers a managed TURN service. TURN acts as a relay point for traffic between WebRTC clients like the browser and SFUs, particularly in scenarios where direct communication is obstructed by NATs or firewalls. TURN maintains an allocation of public IP addresses and ports for each session, ensuring connectivity even in restrictive network environments.</p>
<p>Using Cloudflare Realtime TURN service is available free of charge when used together with the Realtime SFU. Otherwise, it costs $0.05/real-time GB outbound from Cloudflare to the TURN client.</p>
<h2 id="service-address-and-ports">Service address and ports</h2>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Primary address</th>
<th>Primary port</th>
<th>Alternate port</th>
</tr>
</thead>
<tbody>
<tr>
<td>STUN over UDP</td>
<td>stun.cloudflare.com</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over UDP</td>
<td>turn.cloudflare.com</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over TCP</td>
<td>turn.cloudflare.com</td>
<td>3478/tcp</td>
<td>80/tcp</td>
</tr>
<tr>
<td>TURN over TLS</td>
<td>turn.cloudflare.com</td>
<td>5349/tcp</td>
<td>443/tcp</td>
</tr>
</tbody>
</table>
<h2 id="regions">Regions</h2>
<p>Cloudflare Realtime TURN service runs on <a href="https://www.cloudflare.com/network">Cloudflare's global network</a> - a growing global network of thousands of machines distributed across hundreds of locations, with the notable exception of the Cloudflare's <a href="/china-network/">China Network</a>.</p>
<p>When a client tries to connect to <code>turn.cloudflare.com</code>, it <em>automatically</em> connects to the Cloudflare location closest to them. We achieve this using <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast routing</a>.</p>
<p>To learn more about the architecture that makes this possible, read this <a href="https://blog.cloudflare.com/cloudflare-calls-anycast-webrtc">technical deep-dive about Realtime</a>.</p>
<h2 id="protocols-and-ciphers-for-turn-over-tls">Protocols and Ciphers for TURN over TLS</h2>
<p>TLS versions supported include TLS 1.1, TLS 1.2, and TLS 1.3.</p>
<table>
<thead>
<tr>
<th>OpenSSL Name</th>
<th>TLS 1.1</th>
<th>TLS 1.2</th>
<th>TLS 1.3</th>
</tr>
</thead>
<tbody>
<tr>
<td>AEAD-AES128-GCM-SHA256</td>
<td>No</td>
<td>No</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-AES256-GCM-SHA384</td>
<td>No</td>
<td>No</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-CHACHA20-POLY1305-SHA256</td>
<td>No</td>
<td>No</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>No</td>
<td>✅</td>
<td>No</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>No</td>
<td>✅</td>
<td>No</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>No</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>No</td>
<td>✅</td>
<td>No</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>No</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>✅</td>
<td>✅</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="mtu">MTU</h2>
<p>There is no specific MTU limit for Cloudflare Realtime TURN service.</p>
<h2 id="limits">Limits</h2>
<p>Cloudflare Realtime TURN service places limits on:</p>
<ul>
<li>Unique IP address you can communicate with per relay allocation (&gt;5 new IP/sec)</li>
<li>Packet rate outbound and inbound to the relay allocation (&gt;5-10 kpps)</li>
<li>Data rate outbound and inbound to the relay allocation (&gt;50-100 Mbps)</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="limits-apply-to-each-turn-allocation-independently">Limits apply to each TURN allocation independently</h3>
@markup("md", "content/.markup/bodies/11566.md")
</aside>
<p>These limits are suitable for high-demand applications and also have burst rates higher than those documented above. Hitting these limits will result in packet drops.</p>
