<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account. This page lists the actions that are logged for Secrets Store.</p>
<ul>
<li>Access</li>
<li>Create
<ul>
<li>Duplicating a secret is presented as a <code>create</code> log with a field <code>duplicated_from_id</code>.</li>
</ul>
</li>
<li>Update
<ul>
<li>A boolean <code>&quot;value_modified&quot;: true</code> is presented when the secret value is edited.</li>
</ul>
</li>
<li>Delete</li>
</ul>
<p>For information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Fundamentals</a>.</p>
