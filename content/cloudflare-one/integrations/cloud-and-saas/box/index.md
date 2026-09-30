<p>The Box integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Box account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>
<p>A Box account on a Business plan (Business, Business Plus, Enterprise, Enterprise Plus)</p>
</li>
<li>
<p>Access to a Box Business account with Admin permission</p>
</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Box integration to function, Cloudflare CASB requires the following Box permissions via an OAuth 2.0 app:</p>
<ul>
<li><code>Read all files and folders stored in Box</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about the permission, refer to the <a href="https://developer.box.com/guides/api-calls/permissions-and-errors/scopes/#read-all-files-and-folders">Box Scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Box integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/box.mdx.atom">RSS feed</a>.</p>
<h3 id="file-sharing">File sharing</h3>
<p>Identify files and folders that have been shared in a potentially insecure fashion.</p>
<p>To access some file findings, you may need to review shared links. For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#view-shared-files">View shared files</a>.</p>
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
<td>Box: File publicly accessible with edit access</td>
<td><code>fa0532dd-9d13-4c21-8227-62b8bd8be275</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Box: File publicly accessible with high download count</td>
<td><code>97c0845a-754b-4269-b548-85026867da64</code></td>
<td>High</td>
</tr>
<tr>
<td>Box: Folder publicly accessible with edit access</td>
<td><code>154eabed-19a7-4a07-9dfd-d08f5e839aed</code></td>
<td>High</td>
</tr>
<tr>
<td>Box: File shared company-wide with edit access</td>
<td><code>8df801de-327b-4d71-9f36-fc6f3e2c18da</code></td>
<td>High</td>
</tr>
<tr>
<td>Box: File publicly accessible with view access</td>
<td><code>ecca7eeb-3c04-46b2-a509-40393ada32ec</code></td>
<td>High</td>
</tr>
<tr>
<td>Box: Folder shared company-wide with high download count</td>
<td><code>21bed8a9-b587-4a8b-b38f-8c9492b1d132</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: File publicly accessible with high view count</td>
<td><code>540ab1db-5a9e-4968-b669-100e2b97fa85</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: Folder that can be shared by anyone</td>
<td><code>c56757c6-72e4-456c-8cb9-a5b0fd6ceb4a</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: Folder shared company-wide with edit access</td>
<td><code>61082e41-3205-44a0-bb7e-34c02abd5137</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: File shared company-wide with view access</td>
<td><code>5afdbe74-0311-4da8-a64e-6f25c3d4a2b7</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: File shared company-wide with high download count</td>
<td><code>3cd0d8dd-d92b-4a46-b88f-076a17e11837</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: Folder publicly accessible with view access</td>
<td><code>2e9d5774-3a22-4d45-9307-bb24207af3d7</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: Folder shared company-wide with high view count</td>
<td><code>fd303606-a513-4bb5-9a87-b1c836f6e993</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: File larger than 2 GB</td>
<td><code>ef889ceb-4cad-4d25-8845-d350a599825e</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: Folder with external email upload access</td>
<td><code>90f9b277-0846-4918-aac2-2e63fed576b5</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: Folder shared company-wide with view access</td>
<td><code>1bb68e90-9c1d-44ef-91a9-2ed4eb2eb5b2</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: File shared company-wide with high view count</td>
<td><code>22bf3a7b-1fd1-4eb6-b8f5-1b2e772b3484</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>Severity</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Box: File Publicly Accessible Read and Write with DLP Profile match</td>
<td>Critical</td>
<td>A Box file contains sensitive data that anyone on the Internet can read or write.</td>
</tr>
<tr>
<td>Box: File Publicly Accessible Read Only with DLP Profile match</td>
<td>Critical</td>
<td>A Box file contains sensitive data that anyone on the Internet can read.</td>
</tr>
<tr>
<td>Box: File Shared Company Wide Read and Write with DLP Profile match</td>
<td>Medium</td>
<td>A Box file is shared with the entire company with read and write permissions.</td>
</tr>
<tr>
<td>Box: File Shared Company Wide Read Only with DLP Profile match</td>
<td>Medium</td>
<td>A Box file is shared with the entire company with read permissions.</td>
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
<td>Box: Admin not required to use two-factor authentication</td>
<td><code>40f33ef2-3eab-4855-b171-a71463f8fc96</code></td>
<td>High</td>
</tr>
<tr>
<td>Box: User not required to use two-factor authentication</td>
<td><code>a8f9e55a-cb7c-4e35-8dc0-fdf569919a97</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: Inactive admin user</td>
<td><code>e6b82aa9-7d0d-4c85-a582-a377684ace47</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Box: User with unconfirmed notification email</td>
<td><code>15b70c97-68f6-4ef0-afd1-891971162114</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: User with email alias configured</td>
<td><code>085164ed-c555-40ed-9374-358a892e49ef</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: User allowed to collaborate with external users</td>
<td><code>01ed4b90-c470-4ea1-961a-7e64c2fec525</code></td>
<td>Low</td>
</tr>
<tr>
<td>Box: Inactive user</td>
<td><code>d709ccb3-9b9d-4a3c-a3af-a1def54c9a2e</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="account-misconfigurations">Account misconfigurations</h3>
<p>Discover account and admin-level settings that have been configured in a potentially insecure way.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Box: Active Webhook</td>
<td>Low</td>
</tr>
</tbody>
</table>
