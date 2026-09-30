---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/
  description: Reference information for Atlassian Jira in Zero Trust integrations.
  full_title: Atlassian Jira · Cloudflare One docs
  head_html: <title>Atlassian Jira · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Atlassian Jira in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/index.md"><meta property="og:title" content="Atlassian Jira · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Atlassian Jira in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/#page","headline":"Atlassian Jira \u00b7 Cloudflare One docs","description":"Reference information for Atlassian Jira in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-jira/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/atlassian-jira/
  schema: 1
---
<p>The Atlassian Jira integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Atlassian Jira Cloud account that could leave you and your organization vulnerable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5096.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>
<p>A Jira Cloud plan (Free, Standard, Premium, Enterprise)</p>
</li>
<li>
<p>Access to a Jira Cloud account with Site admin and/or Organization admin permissions</p>
</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Jira Cloud integration to function, Cloudflare CASB requires the following permissions via an OAuth 2.0 app:</p>
<ul>
<li><code>read:jira-work</code></li>
<li><code>read:jira-user</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/">Atlassian scopes documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Jira Cloud integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/atlassian-jira.mdx.atom">RSS feed</a>.</p>
<h3 id="access-security">Access security</h3>
<p>Flag user and third-party app access issues, including account misuse and users not following best practices.</p>
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
<td>Jira: Active user with unknown account type</td>
<td><code>8dfd390d-911e-47bb-9ded-cb75fd91e793</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Active third-party app with access</td>
<td><code>01118135-a4ab-4b8f-887d-c814358da217</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Inactive third-party app with access</td>
<td><code>36f7de49-2938-4a54-b212-b4da74145a58</code></td>
<td>Low</td>
</tr>
<tr>
<td>Jira: Inactive user</td>
<td><code>1e1a085c-1ef3-4199-bea5-ff52ccbd6d2d</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="file-security">File security</h3>
<p>Identify files that could be potentially problematic and worth deeper investigation.</p>
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
<td>Jira: Issue attachment larger than 512 MB</td>
<td><code>1e5473b7-588e-4954-b97d-a5a20b4f8c5a</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
