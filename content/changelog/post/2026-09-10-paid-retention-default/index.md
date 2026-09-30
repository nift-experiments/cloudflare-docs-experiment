<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 10, 2026</time><h2 id="post-title">Default instance retention for new Workflows on Workers Paid is seven days</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention <a href="/workflows/reference/limits/">limit</a> remains 30 days.</p>
<p>The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.</p>
<p>To set the retention period for a Workflow instance, specify <code>successRetention</code>, <code>errorRetention</code>, or both:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17834.md")</div>
<p>You can also set the retention period per Workflow and per instance in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a>.</p>
<p>For retention details, refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> and the <a href="/workflows/build/workers-api/#workflowinstancecreateoptions"><code>WorkflowInstanceCreateOptions</code> API reference</a>.</p>
</div></article></div>
