<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 11, 2025</time><h2 id="post-title">Worker version rollback limit increased from 10 to 100</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The number of recent versions available for a Worker rollback has been increased from 10 to 100.</p>
<p>This allows you to:</p>
<ul>
<li>
<p>Promote any of the 100 most recent versions to be the active deployment.</p>
</li>
<li>
<p>Split traffic using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> between your latest code and any of the 100 most recent versions.</p>
</li>
</ul>
<p>You can do this through the Cloudflare dashboard or with <a href="/workers/wrangler/commands/general/#rollback">Wrangler's rollback command</a></p>
<p>Learn more about <a href="/workers/versions-and-deployments/">versioned deployments</a> and <a href="/workers/versions-and-deployments/rollbacks/">rollbacks</a>.</p>
</div></article></div>
