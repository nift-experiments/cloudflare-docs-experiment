<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 16, 2026</time><h2 id="post-title">TCP connections via connect() over VPC Networks</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now support the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via <code>fetch()</code>.</p>
<p>This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17828.md")</div>
<p>At runtime, use <code>connect()</code> on the binding to open a TCP socket to a private destination:</p>
<pre><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Open a TCP connection to a private Redis instance&#10;		const socket = await env.PRIVATE_NETWORK.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		// Write a Redis PING command&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17827.md")</aside>
<p>For more details, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and the <a href="/workers-vpc/api/">Workers Binding API</a>.</p>
</div></article></div>
