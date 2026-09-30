<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 7, 2026</time><h2 id="post-title">Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.</h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.</p>
<h4 id="workflows-adds-step-billing">Workflows adds step billing</h4>
<p>A step is each unit of work executed by a Workflow, including step operations such as <a href="/workflows/build/sleeping-and-retrying/">sleeping</a> or <a href="/workflows/build/events-and-parameters/">waiting for events</a>.</p>
<p>You can query Workflows analytics, including <code>stepCount</code> for a Workflow instance, with the <a href="/workflows/observability/metrics-analytics/#query-via-the-graphql-api">GraphQL Analytics API</a>.</p>
<h4 id="steps-and-storage-billing-to-take-effect-august-10th-2026">Steps and storage billing to take effect August 10th, 2026</h4>
<p>Starting no earlier than August 10th, 2026, Cloudflare will begin billing for step and storage usage on Workers Paid plans.</p>
<p>Storage pricing has been published since Workflows became generally available and is not changing.  Storage is measured as persisted Workflow state in GB-months.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Steps</td>
<td>3,000 included per day</td>
<td>500,000 included per month, then $0.80 per additional 100,000 steps</td>
</tr>
<tr>
<td>Storage</td>
<td>1 GB-month included</td>
<td>1 GB-month included, then $0.20 per additional GB-month</td>
</tr>
</tbody>
</table>
<p>Developers on the Workers Free plan will not be charged for steps or storage beyond the included amounts.</p>
<p>Cloudflare will not bill step and storage usage before August 10, 2026.</p>
<p>You can review Workflows usage in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> before this change takes effect. To reduce costs, consider reducing the number of steps per Workflow or improving the memory efficiency of your stored state.</p>
<p>Refer to the <a href="/workflows/reference/pricing/">Workflows pricing</a> page for full details.</p>
</div></article></div>
