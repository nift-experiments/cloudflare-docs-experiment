<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 16, 2026</time><h2 id="post-title">AI Search instances now include built-in storage and namespace Workers Bindings</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>New <a href="/ai-search/">AI Search</a> instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.</p>
<p>Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.</p>
<h4 id="built-in-storage-and-vector-index">Built-in storage and vector index</h4>
<p>All new instances now comes with built-in storage which allows you to upload files directly to it using the <a href="/ai-search/api/items/workers-binding/">Items API</a> or the dashboard. No R2 buckets to set up, no external data sources to connect first.</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;// upload and wait for indexing to complete&#10;const item = await instance.items.uploadAndPoll(&quot;faq.md&quot;, content);&#10;&#10;// search immediately after indexing&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;onboarding guide&quot; }],&#10;});&#10;</code></pre>
<h4 id="namespace-binding">Namespace binding</h4>
<p>The new <code>ai_search_namespaces</code> binding replaces the previous <code>env.AI.autorag()</code> API provided through the <code>AI</code> binding. It gives your Worker access to all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a> and lets you create, update, and delete instances at runtime without redeploying.</p>
<pre><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<pre><code class="language-ts">// create an instance at runtime&#10;const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;});&#10;</code></pre>
<p>For migration details, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>. For more on namespaces, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h4 id="cross-instance-search">Cross-instance search</h4>
<p>Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.</p>
<pre><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/api/search/workers-binding/#namespace-level">Namespace-level search</a> for details.</p>
</div></article></div>
