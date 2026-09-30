<p>The Atlassian Confluence integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Atlassian Confluence Cloud account that could leave you and your organization vulnerable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5097.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>
<p>A Confluence Cloud plan (Free, Standard, Premium, Enterprise)</p>
</li>
<li>
<p>Access to a Confluence Cloud account with Site admin and/or Organization admin permissions</p>
</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Confluence Cloud integration to function, Cloudflare CASB requires the following permissions via an OAuth 2.0 app:</p>
<ul>
<li><code>read:confluence-space.summary</code></li>
<li><code>read:confluence-props</code></li>
<li><code>read:confluence-content.all</code></li>
<li><code>read:confluence-content.summary</code></li>
<li><code>read:confluence-content.permission</code></li>
<li><code>read:confluence-user</code></li>
<li><code>read:confluence-groups</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/">Atlassian scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Atlassian Confluence integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/atlassian-confluence.mdx.atom">RSS feed</a>.</p>
<h3 id="access-security">Access security</h3>
<p>Flag user and third-party app access issues, including account misuse, sharing security, and users not following best practices.</p>
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
<td>Confluence: Unknown or anonymous user with edit access to content</td>
<td><code>d5ad6f5e-3e7a-4409-a9dc-9707caca047e</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Confluence: Unknown or anonymous user with edit access to space</td>
<td><code>a531c40f-76f5-404e-9c9b-3b21a6da7b98</code></td>
<td>High</td>
</tr>
<tr>
<td>Confluence: Third-party app with edit access to space</td>
<td><code>aac0ac18-25ad-442a-9a24-01ecd85b0b2b</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Confluence: Third-party app with edit access to content</td>
<td><code>8214431e-b708-49c9-b28b-3214f1b491d8</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Confluence: Unknown or anonymous user with access</td>
<td><code>a1d0d098-2602-4312-85a8-a62d3bc56aca</code></td>
<td>Low</td>
</tr>
<tr>
<td>Confluence: Third-party app with content access</td>
<td><code>5ccf7326-386d-4afb-867a-fbf25978c33a</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
