<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 5, 2025</time><h2 id="post-title">Announcing Workers VPC Services (Beta)</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><strong>Workers VPC Services</strong> is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.</p>
<h4 id="what-s-new">What's new</h4>
<ul>
<li><strong>VPC Services</strong>: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax</li>
<li><strong>Multi-cloud Support</strong>: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels</li>
</ul>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Perform application logic in Workers here&#10;&#10;		// Sample call to an internal API running on ECS in AWS using the binding&#10;		const response = await env.AWS_VPC_ECS_API.fetch(&quot;https://internal-host.example.com&quot;);&#10;&#10;		// Additional application logic in Workers&#10;		return new Response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="getting-started">Getting started</h4>
<p>Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. <a href="/workers-vpc/">Refer to the documentation</a> to get started.</p>
</div></article></div>
