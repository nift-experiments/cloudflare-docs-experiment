---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/
  description: Reference information for Anthropic in Zero Trust integrations.
  full_title: Anthropic · Cloudflare One docs
  head_html: <title>Anthropic · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Anthropic in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/index.md"><meta property="og:title" content="Anthropic · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Anthropic in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/#page","headline":"Anthropic \u00b7 Cloudflare One docs","description":"Reference information for Anthropic in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/anthropic/
  schema: 1
---
<p>The Anthropic integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Anthropic account that could leave you and your organization vulnerable.</p>
<p>This integration covers the following Anthropic products:</p>
<ul>
<li>Claude Console (organizations, workspaces/projects, users, invites)</li>
<li>Anthropic API Platform (organization and project API keys)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5098.md")
</aside>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>An Anthropic <a href="https://www.anthropic.com/pricing#team-&amp;-enterprise">Enterprise or Platform organization</a></li>
<li><a href="https://support.anthropic.com/articles/10186004-api-console-roles-and-permissions">Organization-level admin (or equivalent) privileges in Anthropic</a> to view organization metadata and manage API keys</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Anthropic integration to function, Cloudflare CASB requires authorization via <strong>API keys</strong>:</p>
<ul>
<li><code>Admin API key (organization-level)</code>: Grants read-only access to organization/workspace metadata, members and invites, key metadata, and compliance activities used for findings.</li>
<li>(Optional) <code>Project API key (project-level)</code>: Grants read-only access to project metadata and keys when you include project scopes in the scan.</li>
</ul>
<p>These credentials follow the principle of least privilege so that only the minimum required access is granted.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Anthropic integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/anthropic.mdx.atom">RSS feed</a>.</p>
<h3 id="api-key-hygiene">API key hygiene</h3>
<p>Detect API keys that may be unused or overdue for rotation.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anthropic: Unused API key</td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h3 id="access-security">Access security</h3>
<p>Flag organization access issues to help enforce best practices.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anthropic: High-privilege invite</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Stale pending invite</td>
<td>Low</td>
</tr>
<tr>
<td>Anthropic: Claude Project visible across organization</td>
<td>Low</td>
</tr>
<tr>
<td>Anthropic: Claude Cowork enabled for role</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Connector always allowed enabled for role</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude for Chrome enabled for role</td>
<td>High</td>
</tr>
</tbody>
</table>
<h3 id="data-loss-prevention-optional">Data Loss Prevention (optional)</h3>
<p>These findings will only appear if you <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">added DLP profiles</a> to your CASB integration.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anthropic: Downloadable File with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Chat User Prompt with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Chat Assistant Response with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Chat Uploaded File with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Chat Generated File with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Project File with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Project Document with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Chat Artifact with DLP Profile match</td>
<td>High</td>
</tr>
<tr>
<td>Anthropic: Claude Project Instructions with DLP Profile match</td>
<td>High</td>
</tr>
</tbody>
</table>
