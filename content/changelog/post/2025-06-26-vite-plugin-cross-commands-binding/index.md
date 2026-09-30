<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 26, 2025</time><h2 id="post-title">Run and connect Workers in separate dev commands with the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with <code>vite dev</code> or <code>wrangler dev</code>.</p>
<p>Simply start each Worker in its own terminal:</p>
<pre><code class="language-sh">&#35; Terminal 1&#10;vite dev&#10;&#10;&#35; Terminal 2&#10;wrangler dev&#10;</code></pre>
<p>This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.</p>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>
</div></article></div>
