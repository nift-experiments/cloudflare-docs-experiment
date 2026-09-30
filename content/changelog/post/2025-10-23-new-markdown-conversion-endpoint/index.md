<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 23, 2025</time><h2 id="post-title">Workers AI Markdown Conversion: New endpoint to list supported formats</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Developers can now programmatically retrieve a list of all file formats supported by the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a> in Workers AI.</p>
<p>You can use the <a href="/workers-ai/configuration/bindings/"><code>env.AI</code></a> binding:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown().supported()&#10;</code></pre>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<p>Both return a list of file formats that users can convert into Markdown:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;extension&quot;: &quot;.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;	},&#10;	{&#10;		&quot;extension&quot;: &quot;.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;	},&#10;	...&#10;]&#10;</code></pre>
<p>Learn more about our <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a>.</p>
</div></article></div>
