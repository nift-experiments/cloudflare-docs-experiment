<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 15, 2026</time><h2 id="post-title">Stream Workflow instance events in your Worker or via the API with .subscribe()</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now stream Workflow instance events via <code>WorkflowInstance.subscribe()</code> and the <code>GET /subscribe</code> API endpoint. Workers and HTTP clients can react to <a href="/workflows/build/events-and-parameters/">workflow</a> and <a href="/workflows/build/step-context/#workflowstepcontext">step</a> events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.</p>
<p>A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use <code>filter</code> to receive only specific event types or <code>cursor</code> to start a subscription at a specific event.</p>
<p>Use <code>.subscribe()</code> to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17835.md")</div>
<p>For event types, available fields, and subscription options, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>
</div></article></div>
