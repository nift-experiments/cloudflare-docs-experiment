<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2025</time><h2 id="post-title">Workers AI now supports structured JSON outputs.</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI now supports structured JSON outputs with <a href="/workers-ai/features/json-mode/">JSON mode</a>, which allows you to request a structured output response when interacting with AI models.</p>
<p>This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.</p>
<p>JSON mode in Workers AI is compatible with the OpenAI SDK's <a href="https://platform.openai.com/docs/guides/structured-outputs">structured outputs</a> <code>response_format</code> API, which can be used directly in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17816.md")</div>
<p>To learn more about JSON mode and structured outputs, visit the <a href="/workers-ai/features/json-mode/">Workers AI documentation</a>.</p>
</div></article></div>
