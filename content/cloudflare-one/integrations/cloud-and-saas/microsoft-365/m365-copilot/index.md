---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/
  description: Reference information for Microsoft 365 Copilot in Zero Trust integrations.
  full_title: Microsoft 365 Copilot · Cloudflare One docs
  head_html: <title>Microsoft 365 Copilot · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Microsoft 365 Copilot in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/index.md"><meta property="og:title" content="Microsoft 365 Copilot · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Microsoft 365 Copilot in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft,AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/#page","headline":"Microsoft 365 Copilot \u00b7 Cloudflare One docs","description":"Reference information for Microsoft 365 Copilot in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft","AI"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/
  schema: 1
---
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
