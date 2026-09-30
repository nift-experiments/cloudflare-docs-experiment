<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 19, 2025</time><h2 id="post-title">Easier debugging in Workers with improved Wrangler error screen</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler's error screen has received several improvements to enhance your debugging experience!</p>
<p>The error screen now features a refreshed design thanks to <a href="https://www.npmjs.com/package/youch">youch</a>, with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.</p>
<table>
<thead>
<tr>
<th>Before</th>
<th>After (Light)</th>
<th>After (Dark)</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="/assets/upstream/images/workers/changelog/old-error-screen.png" alt="Old error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-light.png" alt="New light theme error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-dark.png" alt="New dark theme error screen" /></td>
</tr>
</tbody>
</table>
<p>Try it out now with <code>npx wrangler@latest dev</code> in your Workers project.</p>
</div></article></div>
