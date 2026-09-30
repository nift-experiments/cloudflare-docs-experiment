<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 30, 2025</time><h2 id="post-title">Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now <a href="https://developers.cloudflare.com/workers/observability/dev-tools/">debug, profile, view logs, and analyze memory usage for your Worker</a> using <a href="https://developer.chrome.com/docs/devtools">Chrome Devtools</a> when your Worker runs locally using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>Previously, this was only possible if your Worker ran locally using the <a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler CLI</a>, and now you can do all the same things if your Worker uses <a href="https://vite.dev/">Vite</a>.</p>
<p>When you run <code>vite</code>, you'll now see a debug URL in your console:</p>
<pre><code>  VITE v6.3.5  ready in 461 ms&#10;&#10;  ➜  Local:   http://localhost:5173/&#10;  ➜  Network: use --host to expose&#10;  ➜  Debug:   http://localhost:5173/__debug&#10;  ➜  press h + enter to show help&#10;</code></pre>
<p>Open the URL in Chrome, and an instance of Chrome Devtools will open and connect to your Worker running locally. You can then use Chrome Devtools to debug and introspect performance issues. For example, you can navigate to the Performance tab to understand where CPU time is spent in your Worker:</p>
<p><img src="/assets/upstream/images/workers/observability/profile.png" alt="CPU Profile" /></p>
<p>For more information on how to get the most out of Chrome Devtools, refer to the following docs:</p>
<ul>
<li><a href="/workers/observability/dev-tools/breakpoints/">Debug code by setting breakpoints</a></li>
<li><a href="/workers/observability/dev-tools/cpu-usage/">Profile CPU usage</a></li>
<li><a href="/workers/observability/dev-tools/memory-usage/">Observe memory usage and debug memory leaks</a></li>
</ul>
</div></article></div>
