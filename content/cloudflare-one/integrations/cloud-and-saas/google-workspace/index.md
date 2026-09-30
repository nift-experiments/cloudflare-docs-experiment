<p>The Google Workspace integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<p>This integration covers the following Google Workspace products:</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/gmail/">Gmail</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-admin/">Google Admin</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar/">Google Calendar</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive/">Google Drive</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/gmail-fedramp/">Gmail (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-admin-fedramp/">Google Admin (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar-fedramp/">Google Calendar (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive-fedramp/">Google Drive (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/">Gemini for Google Workspace</a></li></ul>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Google Workspace integration to function, Cloudflare CASB requires the following Google API permissions:</p>
<ul>
<li><code>https://www.googleapis.com/auth/admin.directory.domain.readonly</code></li>
<li><code>https://www.googleapis.com/auth/admin.directory.user.readonly</code></li>
<li><code>https://www.googleapis.com/auth/admin.directory.user.security</code></li>
<li><code>https://www.googleapis.com/auth/calendar</code></li>
<li><code>https://www.googleapis.com/auth/cloud-platform.read-only</code></li>
<li><code>https://www.googleapis.com/auth/drive.readonly</code></li>
<li><code>https://www.googleapis.com/auth/gmail.settings.basic</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://developers.google.com/admin-sdk/directory/v1/guides/authorizing">Google Workspace Admin SDK Directory API</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Google Workspace integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace.mdx.atom">RSS feed</a>.</p>
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
<td>Google Workspace: Admin user with two-factor authentication disabled</td>
<td><code>5f7c1f62-0ac6-4422-b3d3-d0566dd4e3f2</code></td>
<td>Critical</td>
<td>An administrator in Google Workspace does not have two-factor authentication enabled.</td>
</tr>
<tr>
<td>Google Workspace: User with two-factor authentication disabled</td>
<td><code>739e1965-2ab4-4946-8a56-73fd75154efa</code></td>
<td>High</td>
<td>A user in Google Workspace does not have two-factor authentication enabled.</td>
</tr>
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
<tr>
<td>Google Workspace: User without recovery email</td>
<td><code>2e2383bb-51e8-47fc-8ba7-2dd255c2545f</code></td>
<td>Low</td>
<td>A user in Google Workspace does not have a recovery email set.</td>
</tr>
<tr>
<td>Google Workspace: User without recovery phone number</td>
<td><code>ec326c68-f331-4597-9ec4-43dc197c86f4</code></td>
<td>Low</td>
<td>A user in Google Workspace does not have a recovery phone number set.</td>
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
<td>Google Workspace: Inactive admin user</td>
<td><code>391ee66d-10e0-4b26-91b3-741a2a4c39d0</code></td>
<td>Medium</td>
<td>An administrator account in Google Workspace has not logged in for 30 days.</td>
</tr>
<tr>
<td>Google Workspace: Suspended admin user</td>
<td><code>31e02a11-aa3b-4278-97d3-9c0f7e8fd2c7</code></td>
<td>Medium</td>
<td>An administrator account in Google Workspace is suspended.</td>
</tr>
<tr>
<td>Google Workspace: Inactive user</td>
<td><code>7c098546-2e67-4f01-9fb7-bd48412bd178</code></td>
<td>Low</td>
<td>A user account in Google Workspace has not logged in for 30 days.</td>
</tr>
<tr>
<td>Google Workspace: Suspended user</td>
<td><code>84f514e3-f12d-49e5-bdfe-9073e336d89e</code></td>
<td>Low</td>
<td>A user account in Google Workspace is suspended.</td>
</tr>
<tr>
<td>Google Workspace: Admin user suspended with AI Ultra license</td>
<td><code>ee7d4ed6-479f-404f-8dbd-f82dce2a0f66</code></td>
<td>Low</td>
<td>An administrator account in Google Workspace with an AI Ultra (Gemini for Workspace) license is suspended.</td>
</tr>
<tr>
<td>Google Workspace: User suspended with AI Ultra license</td>
<td><code>cf20e808-29ad-4026-a8f9-6ec3e069376c</code></td>
<td>Low</td>
<td>A user account in Google Workspace with an AI Ultra (Gemini for Workspace) license is suspended.</td>
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
<h3 id="third-party-apps">Third-party apps</h3>
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
<td>Google Workspace: Installed 3rd-party app with Drive access</td>
<td><code>191f0751-7087-4588-9e99-93c5dd834b5b</code></td>
<td>High</td>
<td>A third-party application has been granted permissions to a user's Google Drive.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Gmail access</td>
<td><code>431aecad-20e5-4a20-80ba-4b66eaaa1be4</code></td>
<td>High</td>
<td>A third-party application has been granted permissions to a user's Gmail.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Google Docs access</td>
<td><code>fe41d53b-3bc3-45ef-95d2-75ba159ce60d</code></td>
<td>Medium</td>
<td>A third-party application has been granted permissions to a user's Google Documents.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Google Calendar access</td>
<td><code>80102f46-43d4-437e-b694-e8ee2c077ade</code></td>
<td>Medium</td>
<td>A third-party application has been granted permissions to a user's Google Calendar.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Google Slides access</td>
<td><code>d88e106c-1f2e-4b63-acae-5cee19ded9ec</code></td>
<td>Medium</td>
<td>A third-party application has been granted permissions to a user's Google Slides.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Google Sheets access</td>
<td><code>ece9a2fd-4248-4f11-bc45-8b4189eedb54</code></td>
<td>Medium</td>
<td>A third-party application has been granted permissions to a user's Google Sheets.</td>
</tr>
<tr>
<td>Google Workspace: Installed 3rd-party app with Google Sign In access</td>
<td><code>26b938ea-8d24-4ea5-8e81-2eae26830061</code></td>
<td>Low</td>
<td>A user has used their Google Workspace account to sign up for a third party service.</td>
</tr>
</tbody>
</table>
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
