<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 15, 2025</time><h2 id="post-title">Increased Workflows limits and improved instance queueing.</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> (beta) now allows you to define up to 1024 <a href="/workflows/build/workers-api/#workflowstep">steps</a>. <code>sleep</code> steps do not count against this limit.</p>
<p>We've also added:</p>
<ul>
<li><code>instanceId</code> as property to the <a href="/workflows/build/workers-api/#workflowevent"><code>WorkflowEvent</code></a> type, allowing you to retrieve the current instance ID from within a running Workflow instance</li>
<li>Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.</li>
<li>Support for <a href="/workflows/build/workers-api/#pause"><code>pause</code> and <code>resume</code></a> for Workflow instances in a queued state.</li>
</ul>
<p>We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new <code>waitForEvent</code> API over the coming weeks.</p>
</div></article></div>
