<p>The Gemini for Google Workspace integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions">Google Workspace integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Gemini for Google Workspace integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/gemini.mdx.atom">RSS feed</a>.</p>
<h3 id="user-account-settings">User account settings</h3>
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
<td>Google Workspace: Admin user with Gemini license with two-factor authentication disabled</td>
<td><code>27a0a9a0-13c6-4d8f-a67c-b455dd213cb9</code></td>
<td>High</td>
<td>An administrator with a Gemini for Google Workspace license does not have two-factor authentication enabled.</td>
</tr>
<tr>
<td>Google Workspace: User with Gemini license with two-factor authentication disabled</td>
<td><code>c82024dc-b836-4b86-8c90-ab07971474e4</code></td>
<td>Medium</td>
<td>A user with a Gemini for Google Workspace license does not have two-factor authentication enabled.</td>
</tr>
</tbody>
</table>
<h3 id="inactive-or-suspended-users">Inactive or suspended users</h3>
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
<td>Google Workspace: Admin user suspended with AI Ultra license</td>
<td><code>ee7d4ed6-479f-404f-8dbd-f82dce2a0f66</code></td>
<td>Low</td>
<td>An administrator account with an AI Ultra (Gemini for Workspace) license is suspended.</td>
</tr>
<tr>
<td>Google Workspace: User suspended with AI Ultra license</td>
<td><code>cf20e808-29ad-4026-a8f9-6ec3e069376c</code></td>
<td>Low</td>
<td>A user account with an AI Ultra (Gemini for Workspace) license is suspended.</td>
</tr>
</tbody>
</table>
<h3 id="gemini-licensing">Gemini licensing</h3>
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
<td>Google Workspace: Admin user with AI Ultra license</td>
<td><code>62fa682a-c2b5-4d5a-a086-8e60bed804d3</code></td>
<td>Low</td>
<td>An administrator in Google Workspace is assigned an AI Ultra (Gemini for Workspace) license.</td>
</tr>
<tr>
<td>Google Workspace: User with AI Ultra license</td>
<td><code>5b847ed3-6c02-4963-a1ab-82a4aa2b6c64</code></td>
<td>Low</td>
<td>A user in Google Workspace is assigned an AI Ultra (Gemini for Workspace) license.</td>
</tr>
</tbody>
</table>
