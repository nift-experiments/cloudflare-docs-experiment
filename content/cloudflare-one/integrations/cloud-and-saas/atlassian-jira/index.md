<p>The Atlassian Jira integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Atlassian Jira Cloud account that could leave you and your organization vulnerable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5096.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>
<p>A Jira Cloud plan (Free, Standard, Premium, Enterprise)</p>
</li>
<li>
<p>Access to a Jira Cloud account with Site admin and/or Organization admin permissions</p>
</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Jira Cloud integration to function, Cloudflare CASB requires the following permissions via an OAuth 2.0 app:</p>
<ul>
<li><code>read:jira-work</code></li>
<li><code>read:jira-user</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/">Atlassian scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Jira Cloud integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/atlassian-jira.mdx.atom">RSS feed</a>.</p>
<h3 id="access-security">Access security</h3>
<p>Flag user and third-party app access issues, including account misuse and users not following best practices.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Jira: Active user with unknown account type</td>
<td><code>8dfd390d-911e-47bb-9ded-cb75fd91e793</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Active third-party app with access</td>
<td><code>01118135-a4ab-4b8f-887d-c814358da217</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Inactive third-party app with access</td>
<td><code>36f7de49-2938-4a54-b212-b4da74145a58</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Inactive user</td>
<td><code>1e1a085c-1ef3-4199-bea5-ff52ccbd6d2d</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="file-security">File security</h3>
<p>Identify files that could be potentially problematic and worth deeper investigation.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Jira: Issue attachment larger than 512 MB</td>
<td><code>1e5473b7-588e-4954-b97d-a5a20b4f8c5a</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
