<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 31, 2025</time><h2 id="post-title">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span><span>browser-run</span></div><div class="changelog-body"><p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>
</div></article></div>
