<p>Artifacts pricing is billed on two dimensions:</p>
<ul>
<li><strong>Operations</strong>: the number of repo operations, such as <code>create</code>, <code>push</code>, <code>pull</code>, and <code>clone</code>.</li>
<li><strong>Storage</strong>: the total amount of stored data, measured in gigabyte-months (<code>GB-mo</code>).</li>
</ul>
<h2 id="artifacts-pricing">Artifacts pricing</h2>
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
<td>Operations (1,000 operations)</td>
<td>Unavailable</td>
<td>First 10,000 per month + $0.15 per additional 1,000 operations</td>
</tr>
<tr>
<td>Storage (GB-mo)</td>
<td>Unavailable</td>
<td>First 1 GB per month + $0.50 per additional GB-mo</td>
</tr>
</tbody>
</table>
<h2 id="storage-usage">Storage usage</h2>
<p>Storage is billed using gigabyte-month (<code>GB-mo</code>) as the billing metric, identical to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects SQL storage</a>. A <code>GB-mo</code> is calculated by averaging peak storage per day over a 30-day billing period.</p>
<ul>
<li>Storage is calculated across all repositories.</li>
<li>Replicas do not add storage charges. Storage is replicated by default, and you do not need to manage repository availability or uptime.</li>
<li>Repos remain stored until you explicitly delete them.</li>
</ul>
