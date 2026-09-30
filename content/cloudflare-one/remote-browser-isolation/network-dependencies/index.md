---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/
  description: Reference information for Browser Isolation with firewall in Browser Isolation.
  full_title: Browser Isolation with firewall · Cloudflare One docs
  head_html: <title>Browser Isolation with firewall · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Browser Isolation with firewall in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/index.md"><meta property="og:title" content="Browser Isolation with firewall · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Browser Isolation with firewall in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/#page","headline":"Browser Isolation with firewall \u00b7 Cloudflare One docs","description":"Reference information for Browser Isolation with firewall in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/network-dependencies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["UDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/network-dependencies/
  schema: 1
---
<p>If your organization uses a firewall or other policies to restrict Internet traffic, you may need to make a few changes to allow Browser Isolation to connect.</p>
<h2 id="remoting-client">Remoting client</h2>
<p>Isolated pages are served by the remoting client — the software component in the user's browser that loads, displays, and communicates with the remote browser session. This client communicates to Cloudflare's network via HTTPS and WebRTC.</p>
<h3 id="remoting-client-services">Remoting Client (Services)</h3>
<p>The remoting client provides static assets and API endpoints. For Browser Isolation to function, you must allow:</p>
<ul>
<li>HTTPS traffic to <code>*.browser.run</code> on port <code>443</code></li>
</ul>
<h4 id="clientless-web-isolation">Clientless Web Isolation</h4>
<p>Users connecting through Clientless Web Isolation also require connectivity to Cloudflare Access. For users to connect to Access, you must allow:</p>
<ul>
<li>HTTPS traffic to <code>https://&lt;team-name&gt;.cloudflareaccess.com</code> on port <code>443</code></li>
</ul>
<h3 id="webrtc-channel">WebRTC channel</h3>
<p>Browser Isolation uses WebRTC (a real-time communication protocol) for low-latency communication between the local browser and the remote browser. WebRTC uses UDP rather than TCP, which means this traffic does not flow through standard HTTP/HTTPS proxy settings. The connecting device must have direct UDP connectivity to the IP ranges listed below.</p>
<p>In order to pass WebRTC traffic, the remoting client must be able to connect to the following IP addresses:</p>
<table>
<thead>
<tr>
<th>IP range</th>
<th>Port range</th>
<th>Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4: <code>162.159.201.10 - 162.159.201.255</code> <br/> IPv4: <code>172.64.73.0 - 172.64.73.255</code> <br/> IPv6: <code>2606:4700:f2::/48</code></td>
<td>10000 - 59999</td>
<td>UDP</td>
</tr>
</tbody>
</table>
<p>Each remote browser instance is randomly assigned a port, and the port that a user is allocated to will change often and without notice.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4447.md")
</aside>
