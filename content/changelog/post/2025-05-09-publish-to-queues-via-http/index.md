<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 9, 2025</time><h2 id="post-title">Publish messages to Queues directly via HTTP</h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p>You can now publish messages to <a href="/queues/">Cloudflare Queues</a> directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within <a href="/workers/">Cloudflare Workers</a>. You can already consume from queues via Workers or <a href="/queues/configuration/pull-consumers/">HTTP pull consumers</a>, and now publishing is just as flexible.</p>
<p>Publishing via HTTP requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>Queues Edit</code> permissions for authentication. Here's a simple example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/queues/&lt;queue_id&gt;/messages&quot; \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot;, &quot;timestamp&quot;:  &quot;2025-07-24T12:00:00Z&quot;} }&#x27;&#10;</code></pre>
<p>You can also use our <a href="/fundamentals/api/reference/sdks/">SDKs</a> for TypeScript, Python, and Go.</p>
<p>To get started with HTTP publishing, check out our <a href="/queues/examples/publish-to-a-queue-via-http/">step-by-step example</a> and the full API documentation in our <a href="/api/resources/queues/subresources/messages/methods/push/">API reference</a>.</p>
</div></article></div>
