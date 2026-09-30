<p>When you <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">validate a custom hostname</a>, that hostname can be in several different statuses.</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pending</td>
<td>Custom hostname is pending hostname validation.</td>
</tr>
<tr>
<td>Active</td>
<td>Custom hostname has completed hostname validation and is active.</td>
</tr>
<tr>
<td>Active re-deploying</td>
<td>Customer hostname is active and the changes have been processed.</td>
</tr>
<tr>
<td>Blocked</td>
<td>Custom hostname cannot be added to Cloudflare at this time. Custom hostname was likely associated with Cloudflare previously and flagged for abuse.<br/><br/>If you are an Enterprise customer, contact your account team. Otherwise, email <code>abusereply@cloudflare.com</code> with the name of the web property and a detailed explanation of your association with this web property.</td>
</tr>
<tr>
<td>Moved</td>
<td>Custom hostname is not active after <strong>Pending</strong> for the entirety of the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/">Validation Backoff Schedule</a> or it no longer points to the fallback origin.</td>
</tr>
<tr>
<td>Deleted</td>
<td>Custom hostname was deleted from the zone. Occurs when status is <strong>Moved</strong> for more than seven days.</td>
</tr>
</tbody>
</table>
<p>The custom hostname validation status is separate from the certificate status. In the <a href="/api/resources/custom_hostnames/methods/get/">Custom hostname details endpoint</a> response, <code>result.status</code> tracks hostname activation and <code>result.ssl.status</code> tracks certificate issuance and deployment.</p>
<p>A custom hostname is ready for production traffic when <code>result.status</code> is <code>active</code>, <code>result.ssl.status</code> is <code>active</code>, and DNS points to your SaaS target. If <code>result.status</code> is <code>active</code> but <code>result.ssl.status</code> is not <code>active</code>, Cloudflare has validated the hostname, but the certificate has not completed issuance and deployment.</p>
<h2 id="refresh-validation">Refresh validation</h2>
<p>To run the custom hostname validation check again, select <strong>Refresh</strong> on the dashboard or send a <code>PATCH</code> request to the <a href="/api/resources/custom_hostnames/methods/edit/">Edit custom hostname endpoint</a>. If using the API, make sure that the <code>--data</code> field contains an <code>ssl</code> object with the same <code>method</code> and <code>type</code> as the original request.</p>
<p>If the hostname is in a <strong>Moved</strong> or <strong>Deleted</strong> state, the refresh will set the custom hostname back to <strong>Pending validation</strong>.</p>
