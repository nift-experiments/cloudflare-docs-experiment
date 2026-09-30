<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">Announcing R2 SQL</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>Today, we're launching the <strong>open beta</strong> for <a href="/r2-sql/">R2 SQL</a>: A serverless, distributed query engine that can efficiently analyze petabytes of data in <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from <a href="/pipelines/">Pipelines</a>, or clickstream and user behavior data.</p>
<p>If you already have a table in R2 Data Catalog, running queries is as simple as:</p>
<pre><code class="language-bash">npx wrangler r2 sql query YOUR_WAREHOUSE &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    value&#10;FROM events.user_events&#10;WHERE event_type = &#x27;CHANGELOG&#x27; or event_type = &#x27;BLOG&#x27;&#10;  AND __ingest_ts &gt; &#x27;2025-09-24T00:00:00Z&#x27;&#10;ORDER BY __ingest_ts DESC&#10;LIMIT 100&quot;&#10;</code></pre>
<p>To get started with R2 SQL, check out our <a href="/r2-sql/get-started/">getting started guide</a> or learn more about supported features in the <a href="/r2-sql/sql-reference/">SQL reference</a>. For a technical deep dive into how we built R2 SQL, read our <a href="https://blog.cloudflare.com/r2-sql-deep-dive/">blog post</a>.</p>
</div></article></div>
