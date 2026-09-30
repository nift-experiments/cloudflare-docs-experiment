<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Use Browser Run Quick Actions directly from Workers</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>
</div></article></div>
