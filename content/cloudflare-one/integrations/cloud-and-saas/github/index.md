<p>The GitHub integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated GitHub Organization that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A GitHub account with a Free, Pro, or Enterprise plan</li>
<li>Membership to a GitHub Organization with Owner or GitHub App manager permissions</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the GitHub integration to function, Cloudflare CASB requires the following GitHub API permissions:</p>
<table>
<thead>
<tr>
<th>Permission</th>
<th>Access</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Administration</td>
<td><code>Read-only</code></td>
<td>View basic administrative information from the account.</td>
</tr>
<tr>
<td>Members</td>
<td><code>Read-only</code></td>
<td>View metadata on organization members</td>
</tr>
<tr>
<td>Metadata</td>
<td><code>Read-only</code></td>
<td>View metadata surrounding an organization's assets, excluding sensitive private repository information.</td>
</tr>
<tr>
<td>Organization administration</td>
<td><code>Read-only</code></td>
<td>View information on organization settings</td>
</tr>
</tbody>
</table>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://docs.github.com/en/rest/overview/permissions-required-for-github-apps">GitHub App permissions reference</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The GitHub integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/github.mdx.atom">RSS feed</a>.</p>
<h3 id="branches-and-merges">Branches and merges</h3>
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
<td>GitHub: Repository has no Default Branch Protection</td>
<td><code>5a0428fa-5c13-44b8-a028-9351c1d10a91</code></td>
<td>Medium</td>
<td>A repository's default branch does not have any branch protection rules enabled.</td>
</tr>
<tr>
<td>GitHub: Repository Default Branch Protection does not have PR Review Required</td>
<td><code>edd3f193-af01-421d-9a50-cb1d147bf3a6</code></td>
<td>Medium</td>
<td>A repository's default branch does not have a <strong>Require pull request reviews before merging</strong> rule.</td>
</tr>
<tr>
<td>GitHub: Repository Default Branch Protection does not have Force Pushes Disabled</td>
<td><code>efc3e582-ef39-4316-b1f3-d4717ef30867</code></td>
<td>Medium</td>
<td>A repository's default branch has enabled <strong>Allow force pushes</strong>.</td>
</tr>
<tr>
<td>GitHub: Repository Default Branch Protection does not have Stale PR Approvals Disabled</td>
<td><code>7dc170d7-b1ef-4138-95fb-403d16e7ed43</code></td>
<td>Medium</td>
<td>A repository's default branch does not have a <strong>Dismiss stale pull request approvals when new commits are pushed</strong> rule.</td>
</tr>
<tr>
<td>GitHub: Repository Default Branch Protection does not have Admin Restrictions</td>
<td><code>4e4aec5b-e763-41ac-9099-af874606959b</code></td>
<td>Medium</td>
<td>A repository's default branch does not have a <strong>Do not allow bypassing the above settings</strong> rule for administrators.</td>
</tr>
<tr>
<td>GitHub: Repository Default Branch Protection does not have Status Checks</td>
<td><code>1eba1aeb-9827-4a03-9c47-8290bd3a83d5</code></td>
<td>Medium</td>
<td>A repository's default branch does not have a <strong>Require status checks to pass before merging</strong> rule.</td>
</tr>
<tr>
<td>GitHub: Organization repository has default WRITE permission</td>
<td><code>fc074da0-1e1c-4982-8673-0852d70bf80c</code></td>
<td>Medium</td>
<td>A repository's default write protection settings were not changed.</td>
</tr>
<tr>
<td>GitHub: Repository not updated in 12+ months</td>
<td><code>68b6ef6d-7e00-4761-b3f1-fcf323dc9c26</code></td>
<td>Medium</td>
<td>No changes were made to a repository in at least a year.</td>
</tr>
</tbody>
</table>
<p>Learn more about <a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule">GitHub branch protection rules</a>.</p>
<h3 id="user-accounts">User accounts</h3>
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
<td>GitHub: Organization two-factor authentication disabled</td>
<td><code>47d01030-0ed8-496d-9484-f77899b21d59</code></td>
<td>High</td>
<td>An organization does not have its organization-wide two-factor authentication (2FA) requirement enabled.</td>
</tr>
<tr>
<td>GitHub: Organization user two-factor authentication disabled</td>
<td><code>dfed92b2-a45e-46ed-a86b-8c7e3db01f3c</code></td>
<td>High</td>
<td>A member of the organization does not have two-factor authentication (2FA) enabled.</td>
</tr>
</tbody>
</table>
