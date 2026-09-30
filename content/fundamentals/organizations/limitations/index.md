---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/organizations/limitations/
  description: Review the current limitations of Cloudflare Organizations and troubleshoot common errors.
  full_title: Limitations and troubleshooting · Cloudflare Fundamentals docs
  head_html: <title>Limitations and troubleshooting · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Review the current limitations of Cloudflare Organizations and troubleshoot common errors."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/organizations/limitations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/organizations/limitations/index.md"><meta property="og:title" content="Limitations and troubleshooting · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review the current limitations of Cloudflare Organizations and troubleshoot common errors."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/organizations/limitations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/organizations/limitations/#page","headline":"Limitations and troubleshooting \u00b7 Cloudflare Fundamentals docs","description":"Review the current limitations of Cloudflare Organizations and troubleshoot common errors.","url":"https://developers.cloudflare.com/fundamentals/organizations/limitations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/organizations/limitations/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8812.md")
</aside>
<p>The following limitations currently apply to Cloudflare Organizations. For common errors and resolutions, refer to <a href="#troubleshooting">Troubleshooting</a>.</p>
<h2 id="account-and-zone-limits">Account and zone limits</h2>
<p>Each Organization supports a maximum of <strong>500 accounts</strong> and <strong>5,000 zones</strong>. This limit applies to both Enterprise and MSSP/Distributor Organizations. These limits may be adjusted as usage patterns are better understood during the beta.</p>
<h2 id="api-authentication">API authentication</h2>
<p>User API Tokens support some Organization operations. They cannot complete the full Terraform resource lifecycle. Full user API Token support for Organization operations is planned. To manage Organization resources with Terraform, configure the Cloudflare provider with a Global API key and the registered account email.</p>
<p>A user API Token may create an Organization. A later Terraform refresh or <code>terraform plan</code> may fail when reading the Organization. If the request returns HTTP <code>403</code> with error code <code>10000</code>, use a Global API key and the account email instead.</p>
<p>API Tokens remain the preferred authentication method for supported operations. A Global API key has full access to the user's Cloudflare resources. Refer to <a href="/fundamentals/api/get-started/keys/#limitations">Global API key limitations</a>.</p>
<h2 id="enterprise-organizations">Enterprise Organizations</h2>
<table>
<thead>
<tr>
<th>Limitation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Organization creation</td>
<td>You must be a Super Administrator of an Enterprise account to create an Organization.</td>
</tr>
<tr>
<td>Adding accounts</td>
<td>You can add accounts of any plan type (eg Enterprise, or Free) to your Organization. You must have Super Administrator access to the account, and it cannot already belong to another Organization.</td>
</tr>
<tr>
<td>Account creation</td>
<td>Organization Super Administrators can create up to five Free accounts within their Organization. API tokens and OAuth access tokens cannot create accounts within an Organization. Refer to <a href="/fundamentals/organizations/for-enterprise/#create-new-accounts">Create new accounts</a>.</td>
</tr>
<tr>
<td>Sub-Organizations</td>
<td>Not available. Enterprise Organizations use a flat, single-tier structure. Use tags to organize accounts by business unit, region, or environment.</td>
</tr>
<tr>
<td>Moving accounts</td>
<td>Accounts cannot be moved between Organizations.</td>
</tr>
<tr>
<td>Roles</td>
<td>Organization Super Administrator is the only role available. Additional roles (read-only, billing, audit log) will be available in a future release.</td>
</tr>
<tr>
<td>Organization deletion</td>
<td>To delete an Organization, use the <a href="/api/resources/organizations/methods/delete">API</a>. Dashboard support is not yet available.</td>
</tr>
<tr>
<td>Account removal</td>
<td>Self-service account removal is not yet available. To remove an account from your Organization, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</td>
</tr>
</tbody>
</table>
<h2 id="mssp-distributor-organizations">MSSP/Distributor Organizations</h2>
<table>
<thead>
<tr>
<th>Limitation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Organization creation</td>
<td>MSSP/Distributor Organizations are created by Cloudflare. Contact your account team to set up your Organization.</td>
</tr>
<tr>
<td>Adding existing accounts</td>
<td>Assigning existing accounts is not available for MSSP/Distributor Organizations. Use account creation to add new accounts.</td>
</tr>
<tr>
<td>Account creation</td>
<td>MSSP Organizations can self-serve create new customer accounts within their Organization.</td>
</tr>
<tr>
<td>Sub-Organizations</td>
<td>Distributors can create child MSSP Organizations. MSSP/Distributor Organizations support up to 5 levels of nested sub-organizations.</td>
</tr>
<tr>
<td>Moving accounts</td>
<td>Accounts can be moved between MSSP Organizations within the same Distributor Organization.</td>
</tr>
<tr>
<td>Roles</td>
<td>Organization Super Administrator is the only role available. Additional roles (read-only, billing, audit log) will be available in a future release.</td>
</tr>
<tr>
<td>Organization deletion</td>
<td>To delete an Organization, use the <a href="/api/resources/organizations/methods/delete">API</a>. Dashboard support is not yet available.</td>
</tr>
<tr>
<td>Account removal</td>
<td>Self-service account removal is not yet available. To remove an account from your Organization, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</td>
</tr>
<tr>
<td>Organization type conversion</td>
<td>Organization type (Enterprise vs MSSP/Distributor) is set at creation and cannot be changed. To switch types, a new Organization must be created.</td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>You may encounter the following errors when setting up or managing an Organization.</p>
<h3 id="organization-creation-errors">Organization creation errors</h3>
<table>
<thead>
<tr>
<th>Error</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Organization management is only available on the Enterprise plan at this time.</td>
<td>You are not a member of any Enterprise accounts. You must be a Super Administrator of at least one Enterprise account to create an Organization.</td>
</tr>
<tr>
<td>You need a super admin role on an enterprise account to create an Organization.</td>
<td>You are not a Super Administrator of an Enterprise account. Check your role under <strong>Manage Account</strong> &gt; <strong>Members</strong> on your Enterprise account.</td>
</tr>
<tr>
<td>One or more of your enterprise accounts is already part of an Organization.</td>
<td>Your accounts are already assigned to an Organization. Contact your company administrator to be invited to the existing Organization.</td>
</tr>
<tr>
<td>You have reached the maximum number of organizations.</td>
<td>Each user can only create one Organization. If you need to manage a second Organization, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</td>
</tr>
<tr>
<td>An Organization has already been created for accounts associated with your company. Please contact your company administrator.</td>
<td>Every company is limited to one Organization for all business units. Contact your company's Cloudflare administrator to be invited to the existing Organization.</td>
</tr>
<tr>
<td>You are not eligible to create an Organization because we think there's a problem. Please contact Cloudflare support and we will help you create it.</td>
<td>This rare error may indicate an issue with the internal metadata for one or more of your accounts. Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> with your account ID and the error message.</td>
</tr>
</tbody>
</table>
<h3 id="member-invitation-errors">Member invitation errors</h3>
<table>
<thead>
<tr>
<th>Error</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Invited member cannot accept the invitation.</td>
<td>The invited user must have <a href="/fundamentals/user-profiles/2fa/">two-factor authentication (2FA)</a> or <a href="/fundamentals/manage-members/dashboard-sso/">single sign-on (SSO)</a> enabled on their Cloudflare user account before they can accept an Organization invitation. This is a per-user requirement, not an account-level setting. Ask the user to enable 2FA or SSO, then resend the invitation.</td>
</tr>
<tr>
<td>Member does not have access to accounts after accepting.</td>
<td>Organization membership grants implicit access, which may take a few minutes to propagate. If access does not appear after 5 minutes, ask the member to log out and log back in.</td>
</tr>
</tbody>
</table>
<h3 id="account-assignment-errors">Account assignment errors</h3>
<table>
<thead>
<tr>
<th>Error</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account does not appear in the assignment list.</td>
<td>You must be a Super Administrator of the account. Verify your role under <strong>Manage Account</strong> &gt; <strong>Members</strong> on that account.</td>
</tr>
<tr>
<td>Account cannot be assigned.</td>
<td>The account may already belong to another Organization. Each account can only belong to one Organization. Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> if you believe this is incorrect.</td>
</tr>
</tbody>
</table>
