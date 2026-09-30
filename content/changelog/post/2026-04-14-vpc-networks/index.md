<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">VPC Networks and Cloudflare Mesh support now in public beta</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> bindings, which scope each binding to a specific host and port.</p>
<p>You can bind to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> by <code>tunnel_id</code> to reach any service on the network where that tunnel is running, or bind to your <a href="/mesh/">Cloudflare Mesh</a> network using <code>cf1:network</code> to reach any Mesh node, client device, or subnet route in your account:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17822.md")</div>
<p>At runtime, <code>fetch()</code> routes through the network to reach the service at the IP and port you specify:</p>
<pre><code class="language-js">const response = await env.MESH.fetch(&quot;http://10.0.1.50:8080/api/data&quot;);&#10;</code></pre>
<p>For configuration options and examples, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a>.</p>
</div></article></div>
