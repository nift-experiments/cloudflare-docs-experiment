<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 29, 2026</time><h2 id="post-title">Hyperdrive support for private databases with Workers VPC</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now connect Hyperdrive to a private database through a <a href="/workers-vpc/">Workers VPC service</a>. This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.</p>
<p>When creating a Hyperdrive configuration in the Cloudflare dashboard, choose <strong>Connect to private database</strong> and then <strong>Workers VPC</strong>. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.</p>
<p>You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:</p>
<pre><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.</p>
<p>To get started, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect Hyperdrive to a private database using Workers VPC</a>.</p>
</div></article></div>
