---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/
  description: New updates and improvements at Cloudflare.
  full_title: New L4 transport telemetry fields in Workers · Changelog
  head_html: <title>New L4 transport telemetry fields in Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New L4 transport telemetry fields in Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/#page","headline":"New L4 transport telemetry fields in Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-01-l4-transport-telemetry-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 1, 2026</time><h2 id="post-title">New L4 transport telemetry fields in Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Three new properties are now available on <code>request.cf</code> in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.</p>
<p>Previously, this telemetry was only available via the <code>Server-Timing: cfL4</code> response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.</p>
<h4 id="new-properties">New properties</h4>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>clientTcpRtt</code></td>
<td>number | undefined</td>
<td>The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, <code>22</code>.</td>
</tr>
<tr>
<td><code>clientQuicRtt</code></td>
<td>number | undefined</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, <code>42</code>.</td>
</tr>
<tr>
<td><code>edgeL4</code></td>
<td>Object | undefined</td>
<td>Layer 4 transport statistics. Contains <code>deliveryRate</code> (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, <code>123456</code>.</td>
</tr>
</tbody>
</table>
<h4 id="example-log-connection-quality-metrics">Example: Log connection quality metrics</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const cf = request.cf;&#10;&#10;    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;&#10;    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;&#10;    const transport = cf.clientTcpRtt ? &quot;TCP&quot; : &quot;QUIC&quot;;&#10;&#10;    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;X-Client-RTT&quot;, String(rtt));&#10;    headers.set(&quot;X-Delivery-Rate&quot;, String(deliveryRate));&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/request/">Workers Runtime APIs: Request</a>.</p>
</div></article></div>
