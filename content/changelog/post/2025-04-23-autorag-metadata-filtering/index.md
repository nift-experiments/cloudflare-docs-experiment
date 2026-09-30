<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 23, 2025</time><h2 id="post-title">Metadata filtering and multitenancy support in AutoRAG</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now filter <a href="/ai-search/">AutoRAG</a> search results by <code>folder</code> and <code>timestamp</code> using <a href="/ai-search/configuration/indexing/metadata/">metadata filtering</a> to narrow down the scope of your query.</p>
<p>This makes it easy to build <a href="/ai-search/how-to/per-tenant-search/">multitenant experiences</a> where each user can only access their own data. By organizing your content into per-tenant folders and applying a <code>folder</code> filter at query time, you ensure that each tenant retrieves only their own documents.</p>
<p><strong>Example folder structure:</strong></p>
<pre><code class="language-bash">customer-a/logs/&#10;customer-a/contracts/&#10;customer-b/contracts/&#10;</code></pre>
<p><strong>Example query:</strong></p>
<pre><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;When did I sign my agreement contract?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/contracts/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select <strong>Sync index</strong>. Metadata filtering is available for all data indexed on or after <strong>April 21, 2025</strong>.</p>
<p>If you are new to AutoRAG, get started with the <a href="/ai-search/get-started/">Get started AutoRAG guide</a>.</p>
</div></article></div>
