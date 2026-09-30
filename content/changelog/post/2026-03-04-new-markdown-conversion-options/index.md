<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 4, 2026</time><h2 id="post-title">New conversion options for Markdown Conversion</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>You can now customize how the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service processes different file types by passing a <code>conversionOptions</code> object.</p>
<p>Available options:</p>
<ul>
<li><strong>Images</strong>: Set the language for AI-generated image descriptions</li>
<li><strong>HTML</strong>: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links</li>
<li><strong>PDF</strong>: Exclude metadata from the output</li>
</ul>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17817.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;html&quot;: {&quot;cssSelector&quot;: &quot;article.content&quot;}}&#x27;&#10;</code></pre>
<p>For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a>.</p>
</div></article></div>
