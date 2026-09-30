<p>Budget alerts notify you by email when your account-wide usage-based spend crosses a dollar threshold you define. Use budget alerts to manage costs proactively instead of discovering unexpected charges at the end of a billing cycle.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3441.md")
</aside>
<h2 id="create-a-budget-alert">Create a budget alert</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3442.md")
</div>
<h2 id="view-and-manage-budget-alerts">View and manage budget alerts</h2>
<p>To view your existing budget alerts, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong> and select <strong>Budget alerts</strong>. The count next to the button shows how many alerts you have configured.</p>
<p>From there you can edit or delete existing alerts.</p>
<h2 id="how-budget-alerts-work">How budget alerts work</h2>
<ul>
<li>Budget alerts evaluate your cumulative usage-based spend for the current billing period.</li>
<li>When spend crosses the threshold, Cloudflare sends a single email notification to all configured recipients.</li>
<li>The alert resets at the start of each new billing period.</li>
<li>Budget alerts are informational only. They do not pause or cap usage. Your monthly invoice remains the authoritative source for billing.</li>
</ul>
<h2 id="budget-alerts-compared-to-usage-notifications">Budget alerts compared to usage notifications</h2>
<p>Cloudflare offers two types of spend monitoring:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Budget alerts</th>
<th>Usage notifications</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scope</strong></td>
<td>Account-wide, all usage-based products combined</td>
<td>Per-product (for example, Argo bytes or Workers requests)</td>
</tr>
<tr>
<td><strong>Threshold</strong></td>
<td>Dollar amount</td>
<td>Product-specific metric (bytes, requests, minutes)</td>
</tr>
<tr>
<td><strong>Setup location</strong></td>
<td><strong>Billing</strong> &gt; <strong>Billable Usage</strong></td>
<td><strong>Notifications</strong></td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Overall cost management</td>
<td>Monitoring a single product</td>
</tr>
</tbody>
</table>
<p>For per-product usage notifications, refer to <a href="/billing/understand/usage-based-billing/#usage-based-billing-notifications">Usage-based billing</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/billable-usage/">Monitor billable usage</a> — Track daily usage-based costs</li>
<li><a href="/billing/understand/usage-based-billing/">Usage-based billing</a> — Which products use metered billing</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
