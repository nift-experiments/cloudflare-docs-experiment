<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 20, 2026</time><h2 id="post-title">View total SQLite storage for Durable Object namespaces</h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new <strong>Total storage</strong> chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-total-storage.png" alt="The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time." /></p>
<div class="nb-dash-button"></div>
<p>The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/#total-storage">Metrics and analytics</a>.</p>
</div></article></div>
