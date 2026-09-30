<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 7, 2026</time><h2 id="post-title">New WebSocket Analytics Logpush dataset</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Enterprise customers can now push per-connection WebSocket analytics to any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a> using the new <code>websocket_analytics</code> dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.</p>
<p>Key fields include:</p>
<ul>
<li><strong><code>ConnectionCloseReason</code></strong> — why the connection ended: <code>peerReset</code>, <code>peerNoError</code>, <code>timedOut</code>, <code>upstreamReset</code>, <code>protocolViolation</code>, <code>unspecifiedError</code>, or <code>none</code>.</li>
<li><strong><code>ConnectionCloseSource</code></strong> — which side initiated the close: <code>upstream</code>, <code>downstream</code>, <code>me</code>, or <code>both</code>.</li>
<li><strong><code>ConnectionTransportCloseCode</code></strong> — the TLS alert code or TCP-level close code for additional precision.</li>
<li><strong><code>RayID</code></strong> — correlate WebSocket connection events with your existing HTTP Request logs.</li>
</ul>
<p>The dataset also includes directional byte counts (<code>BytesSentClient</code>, <code>BytesReceivedClient</code>, <code>BytesSentOrigin</code>, <code>BytesReceivedOrigin</code>), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.</p>
<p>This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (<code>ConnectionCloseReason == &quot;peerReset&quot;</code>) grouped by host and data center — directly in your existing log analysis tools.</p>
<p>For the full list of available fields, refer to <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics</a>.</p>
</div></article></div>
