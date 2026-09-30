<p>The Google Drive integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions">Google Workspace integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Google Drive integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive.mdx.atom">RSS feed</a>.</p>
<h3 id="file-sharing">File sharing</h3>
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
<td>Google Workspace: File publicly accessible with edit access</td>
<td><code>29b01269-025f-4249-b5c1-0b9ec39823e0</code></td>
<td>Critical</td>
<td>A Google Drive file is publicly accessible on the Internet that anyone can read or write.</td>
</tr>
<tr>
<td>Google Workspace: File publicly accessible with view access</td>
<td><code>d5132bc7-4c41-4824-b879-3918bf7f6ee7</code></td>
<td>High</td>
<td>A Google Drive file is publicly accessible on the Internet that anyone can read.</td>
</tr>
<tr>
<td>Google Workspace: File shared outside company with edit access</td>
<td><code>71ec135e-3d4c-4d35-a2b7-4fd1e5b65b99</code></td>
<td>High</td>
<td>A Google Drive file is shared with another organization or outside party with read and write permissions.</td>
</tr>
<tr>
<td>Google Workspace: File shared outside company with view access</td>
<td><code>d4b231ad-9a8c-40d3-8654-5bd5bb86bf1a</code></td>
<td>Medium</td>
<td>A Google Drive file is shared with another organization or outside party with read permissions.</td>
</tr>
<tr>
<td>Google Workspace: File shared company-wide with edit access</td>
<td><code>0ed79f27-32fd-415a-a919-ea4af3bd25fd</code></td>
<td>Medium</td>
<td>A Google Drive file is shared with the entire company with read and write permissions.</td>
</tr>
<tr>
<td>Google Workspace: File shared company-wide with view access</td>
<td><code>a34753f3-aec7-4134-a30b-2ebb1d7e47de</code></td>
<td>Medium</td>
<td>A Google Drive file is shared with the entire company with read permissions.</td>
</tr>
</tbody>
</table>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
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
<td>Google Workspace: File publicly accessible with edit access with DLP Profile match</td>
<td><code>868a21e9-62b2-4e4a-8150-92cf9eb0c2e3</code></td>
<td>Critical</td>
<td>A Google Drive file contains sensitive data that anyone on the Internet can read or write.</td>
</tr>
<tr>
<td>Google Workspace: File publicly accessible with view access with DLP Profile match</td>
<td><code>bfe54b22-5ee5-4ccc-b62b-ea822b34c164</code></td>
<td>High</td>
<td>A Google Drive file contains sensitive data that anyone on the Internet can read.</td>
</tr>
<tr>
<td>Google Workspace: File shared outside company with edit access with DLP Profile match</td>
<td><code>124cfac5-12c6-4b55-8691-9c11776b365a</code></td>
<td>High</td>
<td>A Google Drive file contains sensitive data that anyone the file is shared to can read.</td>
</tr>
<tr>
<td>Google Workspace: File shared company-wide with edit access with DLP Profile match</td>
<td><code>5b2ad0d2-f35f-47a3-96cb-6e8fbb1fcb36</code></td>
<td>Medium</td>
<td>A Google Drive file contains sensitive data that anyone in your organization can read or write.</td>
</tr>
<tr>
<td>Google Workspace: File shared company-wide with view access with DLP Profile match</td>
<td><code>b9fa5fef-c1d0-44da-8364-2c0887be0820</code></td>
<td>Medium</td>
<td>A Google Drive file contains sensitive data that anyone in your organization can read.</td>
</tr>
<tr>
<td>Google Workspace: File shared outside company with view access with DLP Profile match</td>
<td><code>aebdda6d-ab48-4408-9941-881683972d83</code></td>
<td>Medium</td>
<td>A Google Drive file contains sensitive data that anyone the file is shared to can read.</td>
</tr>
</tbody>
</table>
