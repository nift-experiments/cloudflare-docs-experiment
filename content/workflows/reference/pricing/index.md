<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17491.md")
</aside>
<p>Workflows uses <a href="/workers/platform/pricing/#workers">Workers Standard pricing</a> for CPU time and requests. Workflows are billed on four dimensions:</p>
<ul>
<li><strong>CPU time</strong>: the total amount of compute (measured in milliseconds) consumed by a given Workflow.</li>
<li><strong>Requests</strong> (invocations): the number of Workflow invocations. <a href="/workers/platform/limits/#subrequests">Subrequests</a> made from a Workflow do not incur additional request costs.</li>
<li><strong>Storage</strong>: the total amount of storage (measured in GB) persisted by your Workflows.</li>
<li><strong>Steps</strong>: the number of steps executed by your Workflows.</li>
</ul>
<p>A Workflow that is waiting on a response to an API call, paused as a result of calling <code>step.sleep</code>, or otherwise idle, does not incur CPU time.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17490.md")
</aside>
<h3 id="workflows-pricing">Workflows pricing</h3>
<table>
<thead>
<tr>
<th>Unit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests (millions)</td>
<td>100,000 per day (<a href="/workers/platform/pricing/#workers">shared with Workers requests</a>)</td>
<td>10 million included per month + $0.30 per additional million</td>
</tr>
<tr>
<td>CPU time (ms)</td>
<td>10 milliseconds of CPU time per invocation</td>
<td>30 million CPU milliseconds included per month + $0.02 per additional million CPU milliseconds</td>
</tr>
<tr>
<td>Storage (GB-mo)</td>
<td>1 GB-month</td>
<td>1 GB-month included + $0.20/ GB-month</td>
</tr>
<tr>
<td>Steps</td>
<td>3,000 per day</td>
<td>500,000 included per month + $0.80/ additional 100,000 per month</td>
</tr>
</tbody>
</table>
<p>Cloudflare will not bill step and storage usage before the start date announced in the <a href="/changelog/post/2026-07-07-workflows-billing-updates/">Workflows billing changelog</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cpu-limits">CPU limits</h3>
@markup("md", "content/.markup/bodies/17489.md")
</aside>
<h3 id="storage-usage">Storage Usage</h3>
<p>Storage is billed using gigabyte-month (GB-month) as the billing metric, identical to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects SQL storage</a>. A GB-month is calculated by averaging the peak storage per day over a billing period (30 days).</p>
<ul>
<li>Storage is calculated across all instances, and includes running, errored, sleeping, and completed instances.</li>
<li>By default, instance state is retained for <a href="/workflows/reference/limits/">3 days on the Free plan</a> and <a href="/workflows/reference/limits/">30 days on the Paid plan</a>.</li>
<li>When creating a Workflow instance, you can set a shorter state retention period if you do not need to retain state for errored or completed Workflows. Refer to the <a href="/workflows/build/workers-api/#workflowinstancecreateoptions"><code>retention</code> option in <code>WorkflowInstanceCreateOptions</code></a> for more information.</li>
<li>Deleting instances via the <a href="/workflows/build/workers-api/">Workers API</a>, <a href="/workers/wrangler/commands/workflows/#workflows">Wrangler CLI</a>, REST API, or dashboard will free up storage. It may take a few minutes for storage limits to update.</li>
</ul>
<p>An instance that attempts to store state when you have reached the storage limit on the Free plan will throw an error.</p>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<p>Frequently asked questions related to Workflows pricing:</p>
<h3 id="are-there-additional-costs-for-workflows">Are there additional costs for Workflows?</h3>
<p>Yes. Workflows are priced based on the same compute (CPU time) and requests (invocations) as Workers, as well as storage (state from a Workflow) and steps.</p>
<h3 id="are-workflows-available-on-the-workers-free-workers-platform-pricing-workers-plan">Are Workflows available on the <a href="/workers/platform/pricing/#workers">Workers Free</a> plan?</h3>
<p>Yes.</p>
<h3 id="what-is-a-workflow-invocation">What is a Workflow invocation?</h3>
<p>A Workflow invocation is when you trigger a new Workflow instance: for example, via the <a href="/workflows/build/workers-api/">Workers API</a>, wrangler CLI, or REST API. Steps within a Workflow are not invocations.</p>
<h3 id="how-do-workflows-show-up-on-my-bill">How do Workflows show up on my bill?</h3>
<p>Workflows are billed as Workers, and share the same CPU time and request SKUs. Workflows billing also includes storage and step usage.</p>
<h3 id="are-there-any-limits-to-workflows">Are there any limits to Workflows?</h3>
<p>Refer to the published <a href="/workflows/reference/limits/">limits</a> documentation.</p>
