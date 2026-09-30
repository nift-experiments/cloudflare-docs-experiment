---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/
  description: Reference information for Slack in Zero Trust integrations.
  full_title: Slack · Cloudflare One docs
  head_html: <title>Slack · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Slack in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/index.md"><meta property="og:title" content="Slack · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Slack in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Slack"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/#page","headline":"Slack \u00b7 Cloudflare One docs","description":"Reference information for Slack in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Slack"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/slack/
  schema: 1
---
<p>The Slack integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Slack Workspace that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Slack user account</li>
<li>Membership in a Slack Workspace (Free, Pro, Business+, or Enterprise Grid)</li>
<li>If you are not the Workspace Owner and the <code>Require App Approval</code> setting is enabled for the Workspace, <a href="https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace">request permission</a> to install apps.</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Slack integration to function, Cloudflare CASB requires the following Slack API permissions:</p>
<ul>
<li><code>channels:read</code></li>
<li><code>files:read</code></li>
<li><code>groups:read</code></li>
<li><code>users:read</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://api.slack.com/scopes">Slack Permission scopes reference</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Slack integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/slack.mdx.atom">RSS feed</a>.</p>
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
<td>Slack: User with two-factor authentication disabled</td>
<td><code>d1cc8596-d22c-435c-9f94-3ba068f019cd</code></td>
<td>Critical</td>
<td>A user in the Slack Workspace does not have two-factor authentication (2FA) enabled for their account.</td>
</tr>
<tr>
<td>Slack: User with unverified email</td>
<td><code>9fa4ae7c-07f0-453a-b232-e734b0f8877c</code></td>
<td>High</td>
<td>A user in the Slack Workspace has not verified the email they use to sign in.</td>
</tr>
</tbody>
</table>
<h3 id="channel-sharing">Channel sharing</h3>
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
<td>Slack: Channel shared externally</td>
<td><code>d298ba64-f013-4e28-b68a-63f758380355</code></td>
<td>High</td>
<td>A channel in the Slack Workspace has been shared with users who are not members of the Workspace.</td>
</tr>
</tbody>
</table>
<h3 id="file-sharing">File sharing</h3>
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
<td>Slack: File publicly accessible with view access</td>
<td><code>9d96d3a2-696b-4802-98aa-c6c8572e806e</code></td>
<td>Medium</td>
<td>An external link has been created for a file uploaded to the Slack Workspace.</td>
</tr>
<tr>
<td>Slack: File larger than 2 GB</td>
<td><code>c16d64a8-9f78-4f24-99ff-de7fcdc6871b</code></td>
<td>Low</td>
<td>A file ≥ 2 GB has been uploaded to the Slack Workspace.</td>
</tr>
</tbody>
</table>
