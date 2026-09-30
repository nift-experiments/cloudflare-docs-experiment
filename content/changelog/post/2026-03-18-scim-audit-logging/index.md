<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2026</time><h2 id="post-title">SCIM audit logging Support</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare dashboard SCIM provisioning operations are now captured in <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2</a>, giving you visibility into user and group changes made by your identity provider.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-03-18-scim-audit-logging.png" alt="SCIM audit logging" /></p>
<p><strong>Logged actions:</strong></p>
<table>
<thead>
<tr>
<th>Action Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Create SCIM User</td>
<td>User provisioned from IdP</td>
</tr>
<tr>
<td>Replace SCIM User</td>
<td>User fully replaced (PUT)</td>
</tr>
<tr>
<td>Update SCIM User</td>
<td>User attributes modified (PATCH)</td>
</tr>
<tr>
<td>Delete SCIM User</td>
<td>Member deprovisioned</td>
</tr>
<tr>
<td>Create SCIM Group</td>
<td>Group provisioned from IdP</td>
</tr>
<tr>
<td>Update SCIM Group</td>
<td>Group membership or attributes modified</td>
</tr>
<tr>
<td>Delete SCIM Group</td>
<td>Group deprovisioned</td>
</tr>
</tbody>
</table>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>
</div></article></div>
