<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/5113.md")
</aside>
<p>The Google Admin (FedRAMP) integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan</li>
<li>A Google Workspace user with <a href="https://support.google.com/a/answer/2405986">Super Admin privileges</a> and <a href="https://cloud.google.com/iam/docs/understanding-roles">Owner permissions</a> in the Google Cloud Platform (GCP) project used</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions">Google Workspace integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Google Admin (FedRAMP) integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-admin-fedramp.mdx.atom">RSS feed</a>.</p>
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
