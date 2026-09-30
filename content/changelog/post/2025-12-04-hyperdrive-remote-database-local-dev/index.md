<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 4, 2025</time><h2 id="post-title">Connect to remote databases during local development with wrangler dev</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now connect directly to remote databases and databases requiring TLS with <code>wrangler dev</code>.
This lets you run your Worker code locally while connecting to remote databases, without needing to use <code>wrangler dev --remote</code>.</p>
<p>The <code>localConnectionString</code> field and <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> environment variable can be used to configure the connection string used by <code>wrangler dev</code>.</p>
<pre><code class="language-jsonc">{&#10;  &quot;hyperdrive&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;      &quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;      &quot;localConnectionString&quot;: &quot;postgres://user:password@remote-host.example.com:5432/database?sslmode=require&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/local-development/">local development with Hyperdrive</a>.</p>
</div></article></div>
