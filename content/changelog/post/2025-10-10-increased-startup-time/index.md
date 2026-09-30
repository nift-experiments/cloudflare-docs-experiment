<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 10, 2025</time><h2 id="post-title">Worker startup time limit increased to 1 second</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.</p>
<p>This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.</p>
<p>For more information, see the documentation on <a href="/workers/platform/limits/#worker-startup-time">Workers startup limits</a>.</p>
</div></article></div>
