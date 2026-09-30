<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 28, 2026</time><h2 id="post-title">Realtime backlog metrics now available for Queues</h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/">Queues</a>, Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:</p>
<ul>
<li><strong><code>backlog_count</code></strong> — the number of unacknowledged messages in the queue</li>
<li><strong><code>backlog_bytes</code></strong> — the total size of those messages in bytes</li>
<li><strong><code>oldest_message_timestamp_ms</code></strong> — the timestamp of the oldest unacknowledged message</li>
</ul>
<p>The following endpoints also now include a <code>metadata.metrics</code> object on the result field after successful message consumption:</p>
<ul>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/pull</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/batch</code></li>
</ul>
<h4 id="javascript-apis">Javascript APIs</h4>
<p>Call <code>env.QUEUE.metrics()</code> to get realtime backlog metrics:</p>
<pre><code class="language-ts">const {&#10;	backlogCount, // number&#10;	backlogBytes, // number&#10;	oldestMessageTimestamp, // Date | undefined&#10;} = await env.QUEUE.metrics();&#10;</code></pre>
<p><code>env.QUEUE.send()</code> and <code>env.QUEUE.sendBatch()</code> also now return a metrics object on the response.</p>
<p>You can also query these fields via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> or view realtime backlog on the <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">dashboard</a>.</p>
<p><img src="/assets/upstream/images/changelog/queues/2026-04-28-queues-metrics.png" alt="Queues realtime backlog" /></p>
<p>For more information, refer to <a href="/queues/observability/metrics/">Queues metrics</a>.</p>
</div></article></div>
