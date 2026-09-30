<p>The Salesforce integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Salesforce environment that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Salesforce environment (most editions are compatible)</li>
<li>Permissions to a Salesforce organization with either:
<ul>
<li>System Administrator permission</li>
<li>Permissions for View Setup and Configuration, Customize Applications, and Modify All Data</li>
</ul>
</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Salesforce integration to function, Cloudflare CASB requires the following Salesforce permissions via a Connected App:</p>
<ul>
<li><code>Manage user data via APIs (api)</code></li>
<li><code>Manage user data via Web browsers (web)</code></li>
<li><code>Perform requests at any time (refresh_token, offline_access)</code></li>
<li><code>Access unique user identifiers (openid)</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_tokens_scopes.htm">Salesforce OAuth Tokens and Scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Salesforce integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/salesforce.mdx.atom">RSS feed</a>.</p>
<h3 id="file-sharing">File sharing</h3>
<p>Identify uploaded content, files, and attachments that have been shared in a potentially insecure fashion.</p>
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
<td>Salesforce: Content Document publicly accessible without a password</td>
<td><code>4cde56ed-19db-4cdb-a6c6-3aede5e17785</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Salesforce: Content Document publicly accessible with weak password</td>
<td><code>68c43ab8-733d-4798-b25f-202f6fcf435f</code></td>
<td>High</td>
</tr>
<tr>
<td>Salesforce: Content Document publicly accessible and password protected</td>
<td><code>75194f6b-5a95-48fa-b485-37181d2d19c8</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Content Document shared and not viewed in 12+ months (stale permission)</td>
<td><code>7125e209-234a-4f10-89d2-1af0601c277f</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Content Document larger than 2 GB</td>
<td><code>3d21de13-4b9f-483c-921a-44cdef7a58c5</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h3 id="account-misconfigurations">Account misconfigurations</h3>
<p>Discover account and admin-level settings that have been configured in an insecure way.</p>
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
<td>Salesforce: Domain without HTTPS</td>
<td><code>20916e32-442e-4622-9e54-e1f37eb7d79f</code></td>
<td>High</td>
</tr>
<tr>
<td>Salesforce: Default Account record access allows edit</td>
<td><code>316f1d9a-447e-432c-add7-7adde67c4f19</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Default Case record access allows edit</td>
<td><code>a7c8eb3e-b5be-4bfc-969a-358186bf927a</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Default Contact record access allows edit</td>
<td><code>e7be14f0-24d6-4d6c-9e12-ca3f23d34ba9</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Default Lead record access allows edit</td>
<td><code>12fde974-45e8-4449-8bf4-dc319370d5ca</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Default Opportunity record access allows edit</td>
<td><code>2ab78d14-e804-4334-9d46-213d8798dd2a</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Organization with active compliance BCC email</td>
<td><code>43e5fd20-1cba-4f1d-aa39-90c7ce2e088a</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="user-access">User access</h3>
<p>Flag user access issues, including account misuse and users not following best practices.</p>
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
<td>Salesforce: User sending email with different email address</td>
<td><code>a2790c4f-03f5-449f-b209-5f4447f417af</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Salesforce: Inactive user</td>
<td><code>57e44995-c7ad-46fe-9c55-59706e663adf</code></td>
<td>Low</td>
</tr>
<tr>
<td>Salesforce: User has never logged in</td>
<td><code>a0bf74df-c796-4574-ac1c-0f239ea8c9ac</code></td>
<td>Low</td>
</tr>
<tr>
<td>Salesforce: User has not logged in for 90+ days</td>
<td><code>8395c824-bc44-4c12-b300-40f2477384d4</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
