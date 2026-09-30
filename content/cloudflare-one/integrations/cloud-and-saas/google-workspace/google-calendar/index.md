<p>The Google Calendar integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions">Google Workspace integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Google Calendar integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar.mdx.atom">RSS feed</a>.</p>
<h3 id="calendar-sharing">Calendar sharing</h3>
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
<td>Google Workspace: Calendar is publicly accessible</td>
<td><code>ec68bf68-b0c0-47b3-ad48-fcb3d7eaf8b6</code></td>
<td>Medium</td>
<td>A user's Google Calendar is publicly accessible on the Internet that anyone can read.</td>
</tr>
</tbody>
</table>
