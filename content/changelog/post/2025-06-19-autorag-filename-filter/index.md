<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 19, 2025</time><h2 id="post-title">Filter your AutoRAG search by file name</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AutoRAG</a>, you can now <a href="/ai-search/configuration/indexing/metadata/">filter</a> by an object's file name using the <code>filename</code> attribute, giving you more control over which files are searched for a given query.</p>
<p>This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.</p>
<p>For example, your search query may look like:</p>
<pre><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;what is the project deadline?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;filename&quot;,&#10;		value: &quot;project-alpha-roadmap.md&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div></article></div>
