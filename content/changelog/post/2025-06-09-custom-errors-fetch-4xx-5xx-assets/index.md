<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 9, 2025</time><h2 id="post-title">More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>
</div></article></div>
