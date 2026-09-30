<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">AI Search UI snippets and MCP support</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.</p>
<p>Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance, and turn on **Public Endpoint** in **Settings**.
   For more details, refer to [Public endpoint configuration](/ai-search/configuration/retrieval/public-endpoint/).
<h4 id="ui-snippets">UI snippets</h4>
<p>UI snippets are pre-built search and chat components you can embed in your website. Visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a> to configure and preview components for your AI Search instance.</p>
<p><img src="/assets/upstream/images/ai-search/ui-snippet-search-modal.png" alt="Example of the search-modal-snippet component" /></p>
<p>To add a search modal to your page:</p>
<pre><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;search-modal-snippet&#10;	api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;	placeholder=&quot;Search...&quot;&#10;&gt;&#10;&lt;/search-modal-snippet&gt;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets documentation</a>.</p>
<h4 id="mcp">MCP</h4>
<p>The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:</p>
<pre><code class="language-txt">https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/mcp/">MCP documentation</a>.</p>
</div></article></div>
