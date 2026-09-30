<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 17, 2025</time><h2 id="post-title">Control which routes invoke your Worker script for Single Page Applications</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>For those building <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">Single Page Applications (SPAs) on Workers</a>, you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code> config option</a> has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.</p>
<p><strong>Configuration example:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17776.md")</div>
<p>This new routing control was done in partnership with our community and customers who provided great feedback on <a href="https://github.com/cloudflare/workers-sdk/discussions/9143">our public proposal</a>. Thank you to everyone who brought forward use-cases and feedback on the design!</p>
<h4 id="prerequisites">Prerequisites</h4>
<p>To use advanced routing control with <code>run_worker_first</code>, you'll need:</p>
<ul>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> v4.20.0 and above</li>
<li><a href="/workers/vite-plugin/get-started/">Cloudflare Vite plugin</a> v1.7.0 and above</li>
</ul>
</div></article></div>
