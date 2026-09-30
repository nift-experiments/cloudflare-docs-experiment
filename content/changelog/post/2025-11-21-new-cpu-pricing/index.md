<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 21, 2025</time><h2 id="post-title">New CPU Pricing for Containers and Sandboxes</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> pricing for CPU time is now based on active usage only, instead of provisioned resources.</p>
<p>This means that you now pay less for Containers and Sandboxes.</p>
<h4 id="an-example-before-and-after">An Example Before and After</h4>
<p>Imagine running the <code>standard-2</code> instance type for one hour, which can use up to 1 vCPU,
but on average you use only 20% of your CPU capacity.</p>
<p>CPU-time is priced at <em>$0.00002 per vCPU-second</em>.</p>
<p>Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.</p>
<p>CPU cost would have been: <strong>$0.072</strong> — 1 vCPU * 3600 seconds * $0.00002</p>
<p>Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.</p>
<p>CPU cost is now: <strong>$0.0144</strong> — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization</p>
<p>This can significantly reduce costs for Containers and Sandboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17708.md")</aside>
<p>See the documentation to learn more about <a href="/containers/get-started/">Containers</a>, <a href="/sandbox/">Sandboxes</a>,
and <a href="/containers/platform/pricing">associated pricing</a>.</p>
</div></article></div>
