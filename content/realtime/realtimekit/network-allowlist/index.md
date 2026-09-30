---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/
  description: Allow the domains and ports required for RealtimeKit connectivity.
  full_title: Network allowlist · Cloudflare Realtime docs
  head_html: <title>Network allowlist · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow the domains and ports required for RealtimeKit connectivity."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/index.md"><meta property="og:title" content="Network allowlist · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow the domains and ports required for RealtimeKit connectivity."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/#page","headline":"Network allowlist \u00b7 Cloudflare Realtime docs","description":"Allow the domains and ports required for RealtimeKit connectivity.","url":"https://developers.cloudflare.com/realtime/realtimekit/network-allowlist/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/network-allowlist/
  schema: 1
---
<p>If your network restricts outbound traffic, allow the following RealtimeKit domains and ports.</p>
<h2 id="allow-service-domains">Allow service domains</h2>
<p>Allow these domains for RealtimeKit SDKs:</p>
<table>
<thead>
<tr>
<th>Domain</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>api.realtime.cloudflare.com</code></td>
<td>Handles requests from RealtimeKit SDKs</td>
</tr>
<tr>
<td><code>api-silos.realtime.cloudflare.com</code></td>
<td>Collects SDK logs</td>
</tr>
<tr>
<td><code>da-collector.realtime.cloudflare.com</code></td>
<td>Collects call statistics</td>
</tr>
<tr>
<td><code>location.realtime.cloudflare.com</code></td>
<td>Determines the location in call statistics reports</td>
</tr>
<tr>
<td><code>r2.cloudflarestorage.com</code></td>
<td>Stores and retrieves chat messages</td>
</tr>
<tr>
<td><code>socket-edge.realtime.cloudflare.com</code></td>
<td>Establishes signaling connections between clients and RealtimeKit</td>
</tr>
</tbody>
</table>
<p>If your application uses RealtimeKit Web UI Kit, also allow these domains:</p>
<table>
<thead>
<tr>
<th>Domain</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rtk-assets.realtime.cloudflare.com</code></td>
<td>Serves Web UI Kit assets, including speaker-test audio</td>
</tr>
<tr>
<td><code>rtk-uploads.realtime.cloudflare.com</code></td>
<td>Serves notification sounds and other Web UI Kit assets</td>
</tr>
</tbody>
</table>
<p>Applications that use only RealtimeKit Core do not require the Web UI Kit asset domains.</p>
<h2 id="allow-media-traffic">Allow media traffic</h2>
<p>RealtimeKit uses the <a href="/realtime/sfu/">Cloudflare Realtime SFU</a> for media connections. Allow the following Session Traversal Utilities for NAT (STUN) and Traversal Using Relays around NAT (TURN) traffic:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Domain</th>
<th>Primary port</th>
<th>Alternate port</th>
</tr>
</thead>
<tbody>
<tr>
<td>STUN over UDP</td>
<td><code>stun.cloudflare.com</code></td>
<td><code>3478/udp</code></td>
<td><code>53/udp</code></td>
</tr>
<tr>
<td>TURN over UDP</td>
<td><code>turn.cloudflare.com</code></td>
<td><code>3478/udp</code></td>
<td><code>53/udp</code></td>
</tr>
<tr>
<td>TURN over TCP</td>
<td><code>turn.cloudflare.com</code></td>
<td><code>3478/tcp</code></td>
<td><code>80/tcp</code></td>
</tr>
<tr>
<td>TURN over TLS</td>
<td><code>turn.cloudflare.com</code></td>
<td><code>5349/tcp</code></td>
<td><code>443/tcp</code></td>
</tr>
</tbody>
</table>
<p>Allow the primary and alternate ports where possible. Do not rely only on <code>53/udp</code>, because Internet service providers and browsers can block this port.</p>
<p>For protocol details, refer to <a href="/realtime/turn/#service-address-and-ports">Service address and ports</a>.</p>
<h2 id="use-a-wildcard-domain">Use a wildcard domain</h2>
<p>If your network policy supports wildcard domains, you can use <code>*.realtime.cloudflare.com</code> instead of the listed <code>realtime.cloudflare.com</code> domains.</p>
<p>Individual domain rules are recommended because they restrict access to only the required services. If you use the wildcard domain, you must still allow <code>r2.cloudflarestorage.com</code>, <code>stun.cloudflare.com</code>, and <code>turn.cloudflare.com</code> separately, because the wildcard does not cover them.</p>
<h2 id="verify-connectivity">Verify connectivity</h2>
<p>Run the <a href="https://test.realtime.cloudflare.com/">RealtimeKit pre-call test</a> to verify your device can reach the required services.</p>
