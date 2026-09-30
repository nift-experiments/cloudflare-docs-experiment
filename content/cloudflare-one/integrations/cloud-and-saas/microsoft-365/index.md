<p>The Microsoft 365 (M365) integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.</p>
<p>This integration covers the following Microsoft 365 products:</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center/">Admin Center</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/onedrive/">OneDrive</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/">Outlook</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint/">SharePoint</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/">Microsoft 365 Copilot</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/">Admin Center (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/onedrive-fedramp/">OneDrive (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook-fedramp/">Outlook (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/">SharePoint (FedRAMP)</a></li><li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot-fedramp/">Microsoft 365 Copilot (FedRAMP)</a></li></ul>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles">Global admin role</a> or equivalent permissions in Microsoft 365</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Microsoft 365 integration to function, Cloudflare CASB requires the following delegated Microsoft Graph API permissions:</p>
<ul>
<li><code>Application.Read.All</code></li>
<li><code>Calendars.Read</code></li>
<li><code>Domain.Read.All</code></li>
<li><code>Group.Read.All</code></li>
<li><code>InformationProtectionPolicy.Read.All</code></li>
<li><code>MailboxSettings.Read</code></li>
<li><code>offline_access</code></li>
<li><code>RoleManagement.Read.All</code></li>
<li><code>User.Read.All</code></li>
<li><code>UserAuthenticationMethod.Read.All</code></li>
<li><code>Files.Read.All</code></li>
<li><code>AuditLog.Read.All</code></li>
<li><code>AiEnterpriseInteraction.Read.All</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted.</p>
<p>Additionally, to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#remediate-findings">remediate findings</a>, CASB requires the following permissions:</p>
<ul>
<li><code>Application.ReadWrite.All</code></li>
<li><code>AuditLog.Read.All</code></li>
<li><code>AiEnterpriseInteraction.Read.All</code></li>
<li><code>Calendars.ReadWrite</code></li>
<li><code>Domain.ReadWrite.All</code></li>
<li><code>Files.ReadWrite.All</code></li>
<li><code>Group.ReadWrite.All</code></li>
<li><code>InformationProtectionPolicy.Read.All</code></li>
<li><code>MailboxSettings.ReadWrite</code></li>
<li><code>IdentityRiskyUser.ReadWrite.All</code></li>
<li><code>RoleManagement.ReadWrite.Directory</code></li>
<li><code>User.ReadWrite.All</code></li>
<li><code>UserAuthenticationMethod.ReadWrite.All</code></li>
<li><code>Directory.ReadWrite.All</code></li>
<li><code>GroupMember.ReadWrite.All</code></li>
<li><code>Organization.ReadWrite.All</code></li>
<li><code>Mail.ReadWrite</code></li>
</ul>
<p>To learn more about each permission, refer to the <a href="https://docs.microsoft.com/en-us/graph/permissions-reference">Microsoft Graph permissions documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Microsoft 365 integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365.mdx.atom">RSS feed</a>.</p>
<h3 id="user-account-settings">User account settings</h3>
<p>Keep user accounts safe by ensuring the following settings are maintained. Review password configurations and password strengths to ensure alignment to your organization's security policies and best practices.</p>
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
<td>Microsoft: FIDO2 authentication method unattested</td>
<td><code>5a9fd288-c04f-4f7a-8976-bfd5464c6cf1</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Provisioning error for on-prem user</td>
<td><code>3123d99e-a83c-4d9d-9a10-80da5af6dee5</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Password expiration disabled for user</td>
<td><code>ce8cc363-7cbb-445e-8385-79ae7348e430</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Password not changed for 90+ days</td>
<td><code>93be1fd1-b6c6-4b98-a04c-121d5ea66745</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Strong password disabled for user</td>
<td><code>aecfdcb2-ec1f-4571-be3c-4ae46c93125e</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Cloud sync disabled for on-prem user</td>
<td><code>8370628b-73f1-41a5-bbff-4d5adee7bf33</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Weak Windows Hello for Business key strength</td>
<td><code>6fae390f-07a3-4577-9821-034a7b29e18e</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: On-prem user not synced in 7+ days</td>
<td><code>1eefc5a1-e665-431a-b939-cfbb76a309f5</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: User is not a legal adult</td>
<td><code>329030a3-db43-4959-9d92-2616a42f1731</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: User configured proxy addresses</td>
<td><code>61406f68-feea-43c5-bda8-b7c4ef9b83cf</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: User account disabled</td>
<td><code>0a8bd094-9138-4e7f-8ce8-bebdf5c27c4e</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Reusable temporary access pass</td>
<td><code>98571e6b-c323-48bc-8c60-f0425c7f9342</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Long-lived temporary access pass</td>
<td><code>45cdbd9c-1594-488b-973e-7c62c6e7234e</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="file-sharing">File sharing</h3>
<p>Get alerted when files in your Microsoft 365 account have their permissions changed to a less secure setting. Additionally, you can automatically remediate certain finding types directly from CASB. For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#remediate-findings">Remediate findings</a>.</p>
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
<td>Microsoft: File publicly accessible with edit access</td>
<td><code>85241e6b-205f-4de6-a1d1-325656130995</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Microsoft: Folder publicly accessible with edit access</td>
<td><code>c9662c5c-c3d6-453b-9367-281e024f7e7a</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Microsoft: File publicly accessible with view access</td>
<td><code>a2b40dc9-b96a-4ace-b8f8-739c2be37dbd</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: Folder publicly accessible with view access</td>
<td><code>7c673785-8b70-41bc-b7d4-d0f346487ff6</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: File shared company-wide with edit access</td>
<td><code>a81a79c8-a0bf-4c60-aa46-7547b4d34266</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: File shared company-wide with view access</td>
<td><code>364c9c0e-684b-4a83-bf28-fdbb1430bb59</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Folder shared company-wide with edit access</td>
<td><code>80f73d47-7dcf-4997-8ed3-6564c8388bd1</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Folder shared company-wide with view access</td>
<td><code>f3fc8ae6-815e-4d5f-a57e-b00d5413f98c</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
<p>To access some file findings, you may need to review shared links. For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#view-shared-files">View shared files</a>.</p>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
<p>Additionally, you can automatically remediate certain finding types directly from CASB. For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#remediate-findings">Remediate findings</a>.</p>
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
<td>Microsoft: File publicly accessible with edit access with DLP Profile match</td>
<td><code>7b6ecb52-852f-4184-bf19-175fe59202b7</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Microsoft: File publicly accessible with view access with DLP Profile match</td>
<td><code>8150f237-576d-4b48-8839-0c257f612171</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: File shared company-wide with edit access with DLP Profile match</td>
<td><code>f838ec6b-7d7a-4c1c-9c61-958ac24c27fa</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: File shared company-wide with view access with DLP Profile match</td>
<td><code>0b882cf3-7e33-4c58-b425-0202206a2c10</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h3 id="microsoft-365-copilot-ai">Microsoft 365 Copilot / AI</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
<p>Detect DLP matches in content used and shared within Microsoft's artificial intelligence (AI) offering, Microsoft 365 Copilot.</p>
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
<td>Microsoft: Copilot Referenced File with DLP Profile match</td>
<td><code>fa7b06bd-cf63-41fc-9afa-a20598f7a52d</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: Copilot AI Response with DLP Profile match</td>
<td><code>176b9299-0cee-4bbb-9c59-b18611228454</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: Copilot User Prompt with DLP Profile match</td>
<td><code>1c5f1cdf-3e08-4a83-baf9-fc8e123877ab</code></td>
<td>High</td>
</tr>
</tbody>
</table>
<h3 id="third-party-apps">Third-party apps</h3>
<p>Identify and get alerted about the third-party apps that have access to at least one service in your Microsoft 365 domain. Additionally, receive information about which services are being accessed and by whom to get full visibility into <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5107.md")
</div>.
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
<td>Microsoft: App not certified by Microsoft</td>
<td><code>3f049bb1-3709-4d8f-8591-59dd034cf396</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: App not attested by publisher</td>
<td><code>d7390d6b-f466-4293-8528-6218e29b1179</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: App disabled by Microsoft</td>
<td><code>b5156b76-caaa-4ca8-bdb7-ea282da62356</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="calendar-sharing">Calendar sharing</h3>
<p>Get alerted when calendars in your Microsoft 365 account have their permissions changed to a less secure setting.</p>
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
<td>Microsoft: Calendar shared externally</td>
<td><code>7d2d9b00-3871-4abf-9e65-f29cf00c428b</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="email-administrator-settings">Email administrator settings</h3>
<p>Discover suspicious or insecure email configurations in your Microsoft domain. Missing SPF and DMARC records make it easier for bad actors to spoof email, while SPF records configured to another domain can be a potential warning sign of malicious activity.</p>
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
<td>Microsoft: Domain SPF record allows any IP address</td>
<td><code>27893e48-663e-43f9-83d4-c158c50259d0</code></td>
<td>High</td>
</tr>
<tr>
<td>Microsoft: Domain SPF record not present</td>
<td><code>009093d9-43df-45a2-bdc6-2f35fc3a0c71</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Domain DMARC record not present</td>
<td><code>bb3d3760-2c4e-4161-9164-cff92e809f9c</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Domain DMARC not enforced</td>
<td><code>a020d87d-332b-49d1-acc3-16c19d72fba4</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Domain DMARC not enforced for subdomains</td>
<td><code>1837a549-4d4e-4101-917c-e9a4036e0c08</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Domain DMARC only partially enforced</td>
<td><code>943414ed-7c79-4d17-a253-8d73f34dcc1d</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: Domain not verified</td>
<td><code>dd1e9aba-57ee-4cf1-a895-dd2f1fc166a7</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Microsoft: App certification expires within 90 Days</td>
<td><code>d5ede282-0339-4983-88f3-849ac59ba840</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="email-forwarding">Email forwarding</h3>
<p>Get alerted when users set their email to be forwarded externally. This can either be a sign of unauthorized activity, or an employee unknowingly sending potentially sensitive information to a personal email.</p>
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
<td>Microsoft: Active message rule forwards externally as attachment</td>
<td><code>9efca21a-aba2-452f-bb17-e66d34b58765</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Active message rule forwards externally</td>
<td><code>42fa3fe6-da72-4bf0-9bc9-5faa4a118ec4</code></td>
<td>Low</td>
</tr>
<tr>
<td>Microsoft: Active message rule redirects externally</td>
<td><code>b75ba81e-c98d-4b78-b5a1-47a2f54499e8</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h2 id="microsoft-information-protection-mip-sensitivity-labels">Microsoft Information Protection (MIP) sensitivity labels</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5106.md")
</aside>
<p>Microsoft provides <a href="https://learn.microsoft.com/en-us/microsoft-365/compliance/sensitivity-labels?view=o365-worldwide">MIP sensitivity labels</a> to classify and protect sensitive data. When you add the CASB Microsoft 365 integration, Cloudflare will automatically retrieve the labels from your Microsoft account and populate them in a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/">DLP Profile</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5105.md")
</aside>
