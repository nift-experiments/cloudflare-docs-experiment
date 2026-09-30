<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 10, 2026</time><h2 id="post-title">Plain text output for Markdown Conversion</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>The <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service now supports a new <code>output</code> conversion option that controls the format of the converted content.</p>
<p>Set <code>output.format</code> to <code>text</code> to receive plain text with Markdown syntax removed. The default value is <code>markdown</code>, so existing conversions are unchanged.</p>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17819.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;output&quot;: {&quot;format&quot;: &quot;text&quot;}}&#x27;&#10;</code></pre>
<p>When you request text output, the <code>format</code> field of each result is set to <code>text</code>. For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#output">Conversion Options</a>.</p>
</div></article></div>
