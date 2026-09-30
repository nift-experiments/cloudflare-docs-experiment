---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/
  description: Reference information for Admin Center (FedRAMP) in Zero Trust integrations.
  full_title: Admin Center (FedRAMP) · Cloudflare One docs
  head_html: <title>Admin Center (FedRAMP) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Admin Center (FedRAMP) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/index.md"><meta property="og:title" content="Admin Center (FedRAMP) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Admin Center (FedRAMP) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/#page","headline":"Admin Center (FedRAMP) \u00b7 Cloudflare One docs","description":"Reference information for Admin Center (FedRAMP) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/5109.md")
</aside>
<p>The Admin Center (FedRAMP) integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles">Global admin role</a> or equivalent permissions in Microsoft 365</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#integration-permissions">Microsoft 365 integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Admin Center (FedRAMP) integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp.mdx.atom">RSS feed</a>.</p>
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
<h3 id="third-party-apps">Third-party apps</h3>
<p>Identify and get alerted about the third-party apps that have access to at least one service in your Microsoft 365 domain. Additionally, receive information about which services are being accessed and by whom to get full visibility into <span class="nb-glossary-tooltip" title="shadow IT">shadow IT</span>.</p>
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
