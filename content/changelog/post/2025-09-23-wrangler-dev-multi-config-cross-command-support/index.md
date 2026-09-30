<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 23, 2025</time><h2 id="post-title">Improved support for running multiple Workers with `wrangler dev`</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can run multiple Workers in a single dev command by passing multiple config files to <code>wrangler dev</code>:</p>
<pre><code class="language-sh">wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;</code></pre>
<p>Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use <a href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and <a href="https://developers.cloudflare.com/workers/observability/logs/tail-workers/">Tail Workers</a> in local development, when running separate wrangler dev sessions.</p>
<p>Now, the following works as expected:</p>
<pre><code class="language-sh">&#35; Terminal 1: Run your application that includes both Web and API workers&#10;wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;&#10;&#35; Terminal 2: Run your auth worker separately&#10;wrangler dev --config ./auth/wrangler.jsonc&#10;</code></pre>
<p>These Workers can now communicate with each other across separate dev commands, regardless of your development setup.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// This service binding call now works across dev commands&#10;		const authorized = await env.AUTH.isAuthorized(request);&#10;&#10;		if (!authorized) {&#10;			return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;		}&#10;&#10;		return new Response(&quot;Hello from API Worker!&quot;, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>
</div></article></div>
