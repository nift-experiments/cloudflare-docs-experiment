<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2025</time><h2 id="post-title">Faster indexing and new Jobs view in AutoRAG</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
<p>With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the <a href="/api/resources/ai-search/subresources/rags/">Sync API</a> or by clicking “Sync index” in the dashboard.</p>
<p>With the new jobs observability, you can now:</p>
<ul>
<li>View the status, job ID, source, start time, duration and last sync time for each indexing job</li>
<li>Inspect real-time logs of job events (e.g. <code>Starting indexing data source...</code>)</li>
<li>See a history of past indexing jobs under the Jobs tab of your AutoRAG</li>
</ul>
<p>This makes it easier to understand what’s happening behind the scenes.</p>
<p><strong>Coming soon:</strong> We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.</p>
<p>Try it out today on the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a>.</p>
</div></article></div>
