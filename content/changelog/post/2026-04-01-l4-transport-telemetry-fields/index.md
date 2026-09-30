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
<pre><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const cf = request.cf;&#10;&#10;    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;&#10;    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;&#10;    const transport = cf.clientTcpRtt ? &quot;TCP&quot; : &quot;QUIC&quot;;&#10;&#10;    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;X-Client-RTT&quot;, String(rtt));&#10;    headers.set(&quot;X-Delivery-Rate&quot;, String(deliveryRate));&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/request/">Workers Runtime APIs: Request</a>.</p>
</div></article></div>
