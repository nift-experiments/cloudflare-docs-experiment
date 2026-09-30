<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 26, 2025</time><h2 id="post-title">Run Workers for up to 5 minutes of CPU-time</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now run a Worker for up to 5 minutes of CPU time for each request.</p>
<p>Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This
meant that some compute-intensive tasks were impossible to do with a Worker. For instance,
you might want to take the cryptographic hash of a large file from R2. If
this computation ran for over 30 seconds, the Worker request would have timed out.</p>
<p>By default, Workers are still limited to 30 seconds of CPU time. This protects developers
from incurring accidental cost due to buggy code.</p>
<p>By changing the <code>cpu_ms</code> value in your Wrangler configuration, you can opt in to
any value up to 300,000 (5 minutes).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17770.md")</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17769.md")</aside>
<p>For more information on the updates limits, see the documentation on <a href="/workers/wrangler/configuration/#limits">Wrangler configuration for <code>cpu_ms</code></a>
and on <a href="/workers/platform/limits/#cpu-time">Workers CPU time limits</a>.</p>
<p>For building long-running tasks on Cloudflare, we also recommend checking out <a href="/workflows/">Workflows</a> and <a href="/queues/">Queues</a>.</p>
</div></article></div>
