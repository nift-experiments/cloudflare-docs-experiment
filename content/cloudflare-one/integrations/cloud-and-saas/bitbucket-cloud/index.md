<p>The Bitbucket Cloud integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Bitbucket Cloud Cloud account that could leave you and your organization vulnerable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5095.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Bitbucket Cloud plan (Free, Standard, Premium, Enterprise)</li>
<li>Access to a Bitbucket Cloud account with Site admin and/or Organization admin permissions</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Bitbucket Cloud integration to function, Cloudflare CASB requires the following permission scopes via an OAuth 2.0 app:</p>
<ul>
<li><code>account</code></li>
<li><code>email</code></li>
<li><code>issue</code></li>
<li><code>pipeline</code></li>
<li><code>project</code></li>
<li><code>project:admin</code></li>
<li><code>pullrequest</code></li>
<li><code>repository</code></li>
<li><code>repository:admin</code></li>
<li><code>runner</code></li>
<li><code>snippet</code></li>
<li><code>webhook</code></li>
<li><code>wiki</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission scope, refer to the <a href="https://developer.atlassian.com/cloud/bitbucket/rest/intro/#oauth-2-0">Atlassian scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Bitbucket Cloud integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/bitbucket-cloud.mdx.atom">RSS feed</a>.</p>
<h3 id="repository-security">Repository security</h3>
<p>Flag repository issues, including branch protection, access, and update frequency.</p>
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
<td>Bitbucket Cloud: Repository is publicly accessible</td>
<td><code>be273f0a-678e-49af-b9f8-8f3913acef97</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not have PR Review Required</td>
<td><code>6ad95c13-0d13-4595-bc76-bd86f4eba4b9</code></td>
<td>High</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository has no Default Branch Protection</td>
<td><code>324f2014-4d4b-4aa6-89a8-72a6c7da09d7</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository not updated in 12+ months</td>
<td><code>a1bd3076-a68d-492e-9947-a01e15a4d1b3</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not disable direct pushes for all users/groups</td>
<td><code>c60a7b00-1592-429a-8a32-d58101e4551f</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not have Stale PR Approvals Disabled</td>
<td><code>738c9839-5e1e-4048-85a3-7935ec4c647a</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not have Force Pushes Disabled</td>
<td><code>4c52f441-0c24-4dbd-8f5e-0e5b829ee8e2</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not require passing builds to merge</td>
<td><code>afe4a27e-ee01-4ebe-914c-d480ac49a5c2</code></td>
<td>Low</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection allows branch deletion</td>
<td><code>86411562-4b85-4677-b048-7887cc5b1567</code></td>
<td>Low</td>
</tr>
<tr>
<td>Bitbucket Cloud: Repository Default Branch Protection does not enforce merge checks</td>
<td><code>64440d40-91de-4d13-9280-d5afa418ccf0</code></td>
<td>Low</td>
</tr>
<tr>
<td>Bitbucket Cloud: Key is older than 180 days</td>
<td><code>0a135600-a109-434f-877c-1a6594dcd76d</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
