<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 11, 2026</time><h2 id="post-title">Workers are no longer limited to 1000 subrequests</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more <code>fetch()</code> calls or requests
to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as
open websockets on <a href="/durable-objects">Durable Objects</a> or long-running <a href="/workflows">Workflows</a>, as these could often exceed this limit and error.</p>
<p>By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this
limit can be increased up to 10 million by setting the new <code>subrequests</code> limit in your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17797.md")</div>
<p>Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.</p>
<p>To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17798.md")</div>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#limits">Wrangler configuration documentation for limits</a> and <a href="/workers/platform/limits/#subrequests">subrequest limits</a>.</p>
</div></article></div>
