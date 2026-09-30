<p>The Gmail integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions">Google Workspace integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Gmail integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/gmail.mdx.atom">RSS feed</a>.</p>
<h3 id="gmail-administrator-settings">Gmail administrator settings</h3>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Workspace: Domain SPF record allows any IP address</td>
<td><code>f28dcc8d-1f0c-4b5a-b254-4169095c16e5</code></td>
<td>High</td>
<td>A Google Workspace Domain SPF record allows any email to be sent from any IP address on your behalf.</td>
</tr>
<tr>
<td>Google Workspace: Domain SPF record not present</td>
<td><code>2e13e5dd-88ed-4d65-8d0a-d3fdff9ee7bb</code></td>
<td>Medium</td>
<td>An SPF record does not exist for a Google Workspace Domain.</td>
</tr>
<tr>
<td>Google Workspace: Domain DMARC record not present</td>
<td><code>ec39eabf-3536-4005-940b-22d815c628ec</code></td>
<td>Medium</td>
<td>A DMARC record does not exist for a Google Workspace Domain.</td>
</tr>
<tr>
<td>Google Workspace: Domain DMARC not enforced</td>
<td><code>8971666d-c049-436d-b4d1-6816a70650ef</code></td>
<td>Medium</td>
<td>A DMARC record for a Google Workspace Domain is not enforced.</td>
</tr>
<tr>
<td>Google Workspace: Domain DMARC not enforced for subdomains</td>
<td><code>fe485f42-b158-4187-85fe-79acdd92055b</code></td>
<td>Medium</td>
<td>A DMARC record for a Google Workspace Subdomain is not configured to quarantine or reject messages that fail authentication.</td>
</tr>
<tr>
<td>Google Workspace: Domain DMARC only partially enforced</td>
<td><code>b682c603-9bc6-485e-be8c-a6e58a989407</code></td>
<td>Medium</td>
<td>A DMARC record for a Google Workspace Domain is not configured to quarantine or reject messages that fail authentication.</td>
</tr>
</tbody>
</table>
<h3 id="email-forwarding">Email forwarding</h3>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Workspace: User delegates email access</td>
<td><code>66897c22-29a5-4f55-b39a-1bfcdd3c12c5</code></td>
<td>High</td>
<td>A user has delegated access to their inbox to another party. Delegates can read, send, and delete messages on the user's behalf.</td>
</tr>
</tbody>
</table>
