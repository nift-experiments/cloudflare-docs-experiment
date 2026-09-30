<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 21, 2026</time><h2 id="post-title">Reach Cloudflare WAN destinations from Workers VPC</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>You can now use <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings with <code>network_id: &quot;cf1:network&quot;</code> to reach your full private network from Workers, including:</p>
<ul>
<li><a href="/mesh/">Cloudflare Mesh</a> nodes and client devices</li>
<li>Subnet routes and hostname routes announced through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or Cloudflare Mesh</li>
<li>Destinations connected through <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramps — GRE, IPsec, and CNI</li>
</ul>
<p>This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17824.md")</div>
<p>At runtime, the URL you pass to <code>fetch()</code> determines the destination:</p>
<pre><code class="language-js">// Reach a service behind a Cloudflare WAN IPsec on-ramp&#10;const response = await env.PRIVATE_NETWORK.fetch(&quot;http://10.50.0.100:8080/api&quot;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17823.md")</aside>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>.</p>
</div></article></div>
