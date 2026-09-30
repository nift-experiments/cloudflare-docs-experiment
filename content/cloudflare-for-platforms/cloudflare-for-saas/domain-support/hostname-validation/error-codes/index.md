<p>When you <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">validate a custom hostname</a>, you might encounter the following error codes.</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zone does not have a fallback origin set.</td>
<td>Fallback is not active.</td>
</tr>
<tr>
<td>Fallback origin is in a status of <code>initializing</code>, <code>pending_deployment</code>, <code>pending_deletion</code>, or <code>deleted</code>.</td>
<td>Fallback is not active.</td>
</tr>
<tr>
<td>Custom hostname does not <code>CNAME</code> to this zone.</td>
<td>Zone does not have <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying entitlement</a> and custom hostname does not CNAME to zone.</td>
</tr>
<tr>
<td>None of the <code>A</code> or <code>AAAA</code> records are owned by this account and the pre-generated ownership validation token was not found.</td>
<td>Account has <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying enabled</a> but the custom hostname failed the hostname validation check on the <code>A</code> record.</td>
</tr>
<tr>
<td>This account and the pre-generated ownership validation token was not found.</td>
<td>Hostname does not <code>CNAME</code> to zone or none of the <code>A</code>/<code>AAAA</code> records match reserved IPs for zone.</td>
</tr>
</tbody>
</table>
