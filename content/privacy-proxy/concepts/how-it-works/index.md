---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/
  description: Learn how Privacy Proxy uses MASQUE protocols to create encrypted tunnels that separate user identity from user activity.
  full_title: How Privacy Proxy works · Cloudflare Privacy Proxy docs
  head_html: <title>How Privacy Proxy works · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Privacy Proxy uses MASQUE protocols to create encrypted tunnels that separate user identity from user activity."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/index.md"><meta property="og:title" content="How Privacy Proxy works · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Privacy Proxy uses MASQUE protocols to create encrypted tunnels that separate user identity from user activity."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/#page","headline":"How Privacy Proxy works \u00b7 Cloudflare Privacy Proxy docs","description":"Learn how Privacy Proxy uses MASQUE protocols to create encrypted tunnels that separate user identity from user activity.","url":"https://developers.cloudflare.com/privacy-proxy/concepts/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/concepts/how-it-works/
  schema: 1
---
<p>Privacy Proxy uses the MASQUE protocol suite to create encrypted tunnels between clients and destination servers. This page explains the protocol mechanics and how privacy is preserved.</p>
<h2 id="traffic-flow">Traffic flow</h2>
<pre tabindex="0"><code>┌──────────┐      1. Connect + Auth      ┌──────────┐      4. Connect        ┌─────────────┐&#10;│          │ ──────────────────────────▶ │          │ ────────────────────▶  │             │&#10;│  Client  │      2. CONNECT request     │  Privacy │      (Egress IP)       │ Destination │&#10;│          │ ──────────────────────────▶ │  Proxy   │                        │   Server    │&#10;│          │                             │          │ ◀────────────────────  │             │&#10;│          │      3. 200 OK              │          │      5. Connected      │             │&#10;│          │ ◀────────────────────────── │          │                        │             │&#10;│          │                             │          │                        │             │&#10;│          │  ◀───── 6. Encrypted data tunnel ─────▶  ◀─────────────────────▶│             │&#10;└──────────┘                             └──────────┘                        └─────────────┘&#10;&#10;           │◀──── Client IP hidden ────▶│◀──── Cloudflare Egress IP visible ──────────▶│&#10;</code></pre>
<ol>
<li>The client establishes an HTTP/2 or HTTP/3 connection to Privacy Proxy and presents credentials (PSK or Privacy Pass token) in the <code>Proxy-Authorization</code> header.</li>
<li>The client sends a CONNECT request specifying the destination hostname and port.</li>
<li>The proxy responds with <code>200 OK</code> to confirm the tunnel is ready.</li>
<li>The proxy opens a connection to the destination using an egress IP address selected based on the client's geolocation.</li>
<li>The client sends encrypted data through the tunnel. The proxy forwards bytes without inspection.</li>
</ol>
<p>Throughout this process, the proxy learns the destination but not the content. The destination learns the egress IP address but not the client's real IP.</p>
<h2 id="masque-protocols">MASQUE protocols</h2>
<p><a href="https://datatracker.ietf.org/wg/masque/about/">MASQUE</a> (Multiplexed Application Substrate over QUIC Encryption) defines methods for proxying traffic over HTTP. Privacy Proxy supports two MASQUE methods:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Transport</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP CONNECT</td>
<td>TCP</td>
<td>Traditional HTTPS traffic</td>
</tr>
<tr>
<td>CONNECT-UDP</td>
<td>UDP</td>
<td>QUIC-based traffic, real-time applications</td>
</tr>
</tbody>
</table>
<p>Both methods create encrypted tunnels where the proxy forwards traffic without inspecting the content. The proxy sees only the destination hostname and port, not the actual requests, paths, or data exchanged.</p>
<p>Privacy Proxy accepts connections over HTTP/2 (TLS over TCP) and HTTP/3 (QUIC), selecting the appropriate protocol based on client capabilities.</p>
<p>For a technical deep dive into how these protocols work, refer to our <a href="https://blog.cloudflare.com/a-primer-on-proxies/">blog post</a>.</p>
<h2 id="privacy-separation">Privacy separation</h2>
<p>Privacy Proxy creates a privacy boundary between user identity and user activity:</p>
<table>
<thead>
<tr>
<th>Information</th>
<th>Who knows it</th>
</tr>
</thead>
<tbody>
<tr>
<td>User identity (IP address, account)</td>
<td>Authentication service, first-hop proxy (if using double-hop)</td>
</tr>
<tr>
<td>Destination server</td>
<td>Privacy Proxy, destination server</td>
</tr>
<tr>
<td>Request content</td>
<td>Client, destination server only</td>
</tr>
</tbody>
</table>
<p>The proxy authenticates users to verify they have permission to use the service, but authentication happens separately from proxying. Once authenticated, the proxy forwards traffic without linking individual requests to specific users.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/a-primer-on-proxies/">A Primer on Proxies</a> - Technical deep dive into HTTP CONNECT and MASQUE protocols.</li>
<li><a href="https://datatracker.ietf.org/wg/masque/about/">MASQUE Working Group</a> - IETF working group developing proxy protocol standards.</li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc9298">RFC 9298</a> - CONNECT-UDP specification for proxying UDP over HTTP.</li>
</ul>
