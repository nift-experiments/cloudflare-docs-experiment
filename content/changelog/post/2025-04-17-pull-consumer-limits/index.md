<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 17, 2025</time><h2 id="post-title">Increased limits for Queues pull consumers</h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/configuration/pull-consumers/">Queues pull consumers</a> can now pull and acknowledge up to <strong>5,000 messages / second per queue</strong>. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.</p>
<p>Pull consumers allow you to consume messages over HTTP from any environment—including outside of <a href="/workers">Cloudflare Workers</a>. They’re also useful when you need fine-grained control over how quickly messages are consumed.</p>
<p>To setup a new queue with a pull based consumer using <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-sh">npx wrangler queues create my-queue&#10;npx wrangler queues consumer http add my-queue&#10;</code></pre>
<p>You can also configure a pull consumer using the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API</a> or the Queues dashboard.</p>
<p>Once configured, you can pull messages from the queue using any HTTP client. You'll need a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API Token</a> with <code>queues_read</code> and <code>queues_write</code> permissions. For example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${API_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the <a href="/queues/configuration/pull-consumers">pull consumer documentation</a>.</p>
<p>As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the <a href="/queues/platform/pricing">existing rate</a>, of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div></article></div>
