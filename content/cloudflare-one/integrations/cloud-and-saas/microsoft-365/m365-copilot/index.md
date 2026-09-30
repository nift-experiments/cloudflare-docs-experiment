<p>The Microsoft 365 Copilot integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles">Global admin role</a> or equivalent permissions in Microsoft 365</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#integration-permissions">Microsoft 365 integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Microsoft 365 Copilot integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/copilot.mdx.atom">RSS feed</a>.</p>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
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
