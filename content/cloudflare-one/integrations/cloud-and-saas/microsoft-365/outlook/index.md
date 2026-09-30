---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/
  description: Reference information for Outlook in Zero Trust integrations.
  full_title: Outlook · Cloudflare One docs
  head_html: <title>Outlook · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Outlook in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/index.md"><meta property="og:title" content="Outlook · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Outlook in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/#page","headline":"Outlook \u00b7 Cloudflare One docs","description":"Reference information for Outlook in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook/
  schema: 1
---
<p>The Outlook integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription</li>
<li><a href="https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles">Global admin role</a> or equivalent permissions in Microsoft 365</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#integration-permissions">Microsoft 365 integration permissions</a> for information on which API permissions to enable.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Outlook integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/outlook.mdx.atom">RSS feed</a>.</p>
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
