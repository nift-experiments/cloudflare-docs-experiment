<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 20, 2026</time><h2 id="post-title">Import SQL files as additional modules by default</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <code>.sql</code> file extension is now automatically configured to be importable in your Worker code when using <a href="/workers/wrangler/bundling/#including-non-javascript-modules">Wrangler</a> or the <a href="/workers/vite-plugin/reference/non-javascript-modules/">Cloudflare Vite plugin</a>.
This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using <a href="https://orm.drizzle.team/docs/connect-cloudflare-do">Drizzle</a>.</p>
<p>SQL files are imported as JavaScript strings:</p>
<pre><code class="language-ts">// `example` will be a JavaScript string&#10;import example from &quot;./example.sql&quot;;&#10;</code></pre>
</div></article></div>
