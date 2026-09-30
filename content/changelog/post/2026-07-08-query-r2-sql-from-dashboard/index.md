<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2026</time><h2 id="post-title">Query R2 Data Catalog tables with R2 SQL from the dashboard</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>You can now query your <a href="/r2-data-catalog/">R2 Data Catalog</a> tables with <a href="/r2-sql/">R2 SQL</a> directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your <a href="https://iceberg.apache.org/">Apache Iceberg</a> data, validate queries, and inspect results in one place.</p>
<img src="/assets/upstream/images/r2-sql/r2-sql-studio.png" alt="R2 SQL Query Editor" />
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/data-catalog/overview">R2 Data Catalog</a> in the Cloudflare dashboard and select <strong>Query data</strong> to launch the built-in SQL editor. From there you can:</p>
<ul>
<li><strong>Write and run queries interactively</strong> — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.</li>
<li><strong>Explore your data</strong> — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.</li>
<li><strong>Understand results and performance</strong> — View result sets with per-query statistics, export them, and get helpful <code>EXPLAIN</code> outputs to see exactly how a query runs.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17743.md")</aside>
</div></article></div>
