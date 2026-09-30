---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/
  description: Reference information for SharePoint (FedRAMP) in Zero Trust integrations.
  full_title: SharePoint (FedRAMP) · Cloudflare One docs
  head_html: <title>SharePoint (FedRAMP) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for SharePoint (FedRAMP) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/index.md"><meta property="og:title" content="SharePoint (FedRAMP) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for SharePoint (FedRAMP) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/#page","headline":"SharePoint (FedRAMP) \u00b7 Cloudflare One docs","description":"Reference information for SharePoint (FedRAMP) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/5101.md")
</aside>
<p>The SharePoint (FedRAMP) integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles">Global admin role</a> or equivalent permissions in Microsoft 365</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#integration-permissions">Microsoft 365 integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The SharePoint (FedRAMP) integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint-fedramp.mdx.atom">RSS feed</a>.</p>
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
