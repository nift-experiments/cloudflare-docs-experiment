<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 14, 2025</time><h2 id="post-title">Python Workers handlers now live in an entrypoint class</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as <code>on_fetch</code>, <code>on_scheduled</code>, etc. methods, but now they live in an entrypoint class.</p>
<p>Here's an example of how to now define a Worker with a fetch handler:</p>
<pre><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>To keep using the old-style handlers, you can specify the <code>disable_python_no_global_handlers</code> compatibility flag in your wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17785.md")</div>
<p>Consult the <a href="/workers/languages/python/">Python Workers documentation</a> for more details.</p>
</div></article></div>
