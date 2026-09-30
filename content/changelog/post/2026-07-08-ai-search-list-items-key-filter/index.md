<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2026</time><h2 id="post-title">Filter AI Search list items by exact object key</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AI Search</a>, you can upload files to an instance, or connect a <a href="/ai-search/configuration/data-source/">data source</a> such as an R2 bucket, to make your content searchable with natural language. Each file becomes an <strong>item</strong> identified by an object <strong>key</strong> (its filename or path). The <a href="/ai-search/api/items/rest-api/">list items endpoint</a> returns the items in an instance.</p>
<p>That endpoint now accepts a <code>key</code> query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing <code>item_id</code> filter for when you know the key but not the ID.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
<p>For more information, refer to <a href="/ai-search/api/items/rest-api/">managing items</a>.</p>
</div></article></div>
