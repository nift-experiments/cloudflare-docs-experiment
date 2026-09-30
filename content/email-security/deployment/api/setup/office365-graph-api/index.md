---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/office365-graph-api/
  description: Learn how to scan and protect Office 365 emails with Email security (formerly Area 1) via a Microsoft Graph API setup.
  full_title: Office 365 Graph API setup · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Office 365 Graph API setup · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to scan and protect Office 365 emails with Email security (formerly Area 1) via a Microsoft Graph API setup."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/office365-graph-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/office365-graph-api/index.md"><meta property="og:title" content="Office 365 Graph API setup · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to scan and protect Office 365 emails with Email security (formerly Area 1) via a Microsoft Graph API setup."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/office365-graph-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/office365-graph-api/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8514.md")
</aside>
<p>For customers using Microsoft Office 365, setting up Email security via Microsoft Graph API is quick and easy. The following email flow shows how this works:</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/ms-graph/ms-graph.png" alt="Email flow when setting up Email security with the Microsoft Graph API" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8513.md")
</aside>
<h2 id="user-roles">User roles</h2>
<p>Email security uses two roles for retraction and directory integration purposes:</p>
<ul>
<li><strong>Privileged authentication administrator</strong>: Users with this role can view the current authentication method information and set or reset non-password credentials for all users, including global administrators. Privileged authentication administrators can force users to re-register against existing non-password credentials (like MFA or FIDO) and revoke the <code>remember MFA on the device</code> message prompting for MFA on the next login of all users.</li>
<li><strong>Privileged role administrator</strong>: Users with this role can manage role assignments in Azure Active Directory, as well as within Privileged Identity Management. In addition, this role allows management of all aspects of Privileged Identity Management.</li>
</ul>
<p>Directory Integration requires the use of both roles mentioned above. Email retraction only requires the <strong>Privileged role administrator</strong>. Any Azure administrator with a membership in the required role can perform these authorizations. The authorization process grants the Email security dashboard access to the Azure environment. This access is performed with the least applicable privileges required to function, as shown in the <a href="#azure-applications">table below</a>.</p>
<p>The Enterprise Applications that Email security registers are not tied to any administrator account. Inside of the Azure Active Directory admin center you can review the permissions granted to each application in the Enterprise Application section. Refer to <a href="https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/">Application management documentation</a> for more information.</p>
<h2 id="set-up-microsoft-graph-api">Set up Microsoft Graph API</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>In <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>, select <strong>New Domain</strong>.</p>
</li>
<li>
<p>In <strong>Domain</strong>, enter the domain you want to onboard.</p>
</li>
<li>
<p>In <strong>Authorize Mail Access</strong>, select <strong>Authorize Access</strong>.</p>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/ms-graph/step5.png" alt="Select Authorize access to give the correct permissions to Email security" /></p>
</div>
<ol start="6">
<li>
<p>In the new tab that opens, choose an Office 365 account you want to authorize, or enter your credentials.</p>
</li>
<li>
<p>Read the permissions, and select <strong>Accept</strong> to continue. You will be directed back to the Email security dashboard.</p>
</li>
<li>
<p>In <strong>Directory Scanning</strong>, select <strong>Authorize Access</strong>.</p>
</li>
<li>
<p>In the new tab that opens, choose an Office 365 account you want to authorize, or enter your credentials.</p>
</li>
<li>
<p>Read the permissions, and select <strong>Accept</strong> to continue. You will be directed back to the Email security dashboard.</p>
</li>
<li>
<p>In <strong>Protection Scope</strong>, choose if Email security should scan only the inbox or all folders. Scanning all folders is useful for situations where the email is automatically routed to other folders that users still have access to:</p>
<ol>
<li><strong>Protect Inbox only</strong>: Email security will only scan the user's inbox.</li>
<li><strong>Protect all folders</strong>: Email security will scan all non-hidden email folders.</li>
</ol>
</li>
<li>
<p>Now that both types of authorizations have been complete, select <strong>Publish Domain</strong>.</p>
</li>
</ol>
<p>Your authorized domain will show up in <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>, with messages about the progress of directory syncing between Office 365 and Email security.</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/ms-graph/domain-sync-state.png" alt="Now that both authorizations are complete, select Publish domain" /></p>
<h2 id="azure-applications">Azure applications</h2>
<h3 id="directory-integration">Directory Integration</h3>
<p>The following table shows API permissions required for Directory Integration as it appears in Azure Enterprise applications.</p>
<table-wrap style="font-size:90%">
<table>
<thead>
<tr>
<th>API Name</th>
<th>Claim value</th>
<th>Permission</th>
<th>Type</th>
<th>Granted through</th>
<th>Granted by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>User.Read</code></td>
<td>Sign in and read user profile</td>
<td>Delegated</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Group.Read.All</code></td>
<td>Read all groups</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Directory.Read.All</code></td>
<td>Read directory data</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>User.Read.All</code></td>
<td>Read all users' full profiles</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>GroupMember.Read.All</code></td>
<td>Read all group memberships</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
</tbody>
</table>
</table-wrap>
<h3 id="retraction">Retraction</h3>
<p>The following table shows retractions as they appear in Azure Enterprise applications.</p>
<table-wrap style="font-size:90%">
<table>
<thead>
<tr>
<th>API Name</th>
<th>Claim value</th>
<th>Permission</th>
<th>Type</th>
<th>Granted through</th>
<th>Granted by</th>
</tr>
</thead>
<tbody>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Mail.ReadWrite</code></td>
<td>Read and write mail in all mailboxes</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Group.Read.All</code></td>
<td>Read all groups</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>User.Read.All</code></td>
<td>Read all users' full profiles</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Domain.Read.All</code></td>
<td>Read domains</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>GroupMember.Read.All</code></td>
<td>Read all group memberships</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
<tr>
<td>Microsoft <br /> Graph</td>
<td><code>Organization.Read.All</code></td>
<td>Read organization information</td>
<td>Application</td>
<td>Admin consent</td>
<td>An administrator</td>
</tr>
</tbody>
</table>
</table-wrap>
