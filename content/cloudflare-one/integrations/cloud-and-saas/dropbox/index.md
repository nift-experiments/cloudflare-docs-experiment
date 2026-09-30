---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/
  description: Reference information for Dropbox in Zero Trust integrations.
  full_title: Dropbox · Cloudflare One docs
  head_html: <title>Dropbox · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Dropbox in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/index.md"><meta property="og:title" content="Dropbox · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Dropbox in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/#page","headline":"Dropbox \u00b7 Cloudflare One docs","description":"Reference information for Dropbox in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/dropbox/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/dropbox/
  schema: 1
---
<p>The Dropbox integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Dropbox account that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li>A Dropbox Business plan (Standard, Advanced, Enterprise, or Education)</li>
<li>Access to a Dropbox Business account with Team admin permissions</li>
</ul>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the Dropbox integration to function, Cloudflare CASB requires the following Dropbox permissions via an OAuth 2.0 app:</p>
<ul>
<li><code>account_info.read</code></li>
<li><code>files.metadata.read</code></li>
<li><code>files.content.read</code></li>
<li><code>sharing.read</code></li>
<li><code>team_info.read</code></li>
<li><code>team_data.member</code></li>
<li><code>team_data.governance.write</code></li>
<li><code>team_data.governance.read</code></li>
<li><code>files.team_metadata.read</code></li>
<li><code>members.read</code></li>
<li><code>groups.read</code></li>
<li><code>sessions.list</code></li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://developers.dropbox.com/oauth-guide#dropbox-api-permissions">Dropbox API Permissions documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The Dropbox integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/dropbox.mdx.atom">RSS feed</a>.</p>
<h3 id="file-and-folder-sharing">File and folder sharing</h3>
<p>Identify files and folders that have been shared in a potentially insecure fashion.</p>
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
<td>Dropbox: File publicly accessible with edit access</td>
<td><code>7fefad57-371b-4f27-b1f0-7d500c863bd0</code></td>
<td>Critical</td>
</tr>
<tr>
<td>Dropbox: File shared company-wide with edit access</td>
<td><code>265ed167-435c-4626-99ba-2fafd766c096</code></td>
<td>High</td>
</tr>
<tr>
<td>Dropbox: File publicly accessible with view access</td>
<td><code>e8c057e4-d6ce-431b-9d03-d9aadff610d4</code></td>
<td>High</td>
</tr>
<tr>
<td>Dropbox: Shared link create policy set to default 'Public'</td>
<td><code>0afabc9a-3a98-4a67-941a-d1f0ce0cfbfe</code></td>
<td>High</td>
</tr>
<tr>
<td>Dropbox: File shared company-wide with view access</td>
<td><code>02a14d67-27fa-4621-a280-1a25925d506f</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Folder shared company-wide with edit access</td>
<td><code>ac4da5b9-ddb0-4285-ba52-2ba4de43b530</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Shared folder policy set to default 'Anyone'</td>
<td><code>5d479ad5-d0f1-4c8f-b439-a39b399fe6c5</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Group creation policy set to 'Admins and Members'</td>
<td><code>6f54b5eb-6867-490e-b823-08e91878eb40</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Folder join policy set to 'Can join folders shared by Anyone'</td>
<td><code>e5ffaecc-f61a-4019-a54f-2e5ac882d3f3</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Folder member policy set to 'Can share folders with Anyone'</td>
<td><code>99d4a2af-12ec-43a1-9630-27ac4adf625c</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Shared link create policy set to default 'Team-wide'</td>
<td><code>a3d02f04-4372-4ae3-99f9-e2caccee6e76</code></td>
<td>Low</td>
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
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>File Publicly Accessible Read and Write with DLP Profile match</td>
<td>Critical</td>
<td>A Dropbox file contains sensitive data that anyone on the Internet can read or write.</td>
</tr>
<tr>
<td>File Publicly Accessible Read Only with DLP Profile match</td>
<td>Critical</td>
<td>A Dropbox file contains sensitive data that anyone on the Internet can read.</td>
</tr>
<tr>
<td>File Shared Company Wide Read and Write with DLP Profile match</td>
<td>Medium</td>
<td>A Dropbox file is shared with the entire company with read and write permissions.</td>
</tr>
<tr>
<td>File Shared Company Wide Read Only with DLP Profile match</td>
<td>Medium</td>
<td>A Dropbox file is shared with the entire company with read permissions.</td>
</tr>
</tbody>
</table>
<h3 id="suspicious-applications">Suspicious applications</h3>
<p>Detect when suspicious Dropbox applications are linked by members.</p>
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
<td>Dropbox: Suspicious application linked by member</td>
<td><code>8384c58c-1fc2-4caa-9836-c8ede7ca440d</code></td>
<td>High</td>
</tr>
</tbody>
</table>
<h3 id="user-access-and-account-misconfigurations">User access and account misconfigurations</h3>
<p>Flag user access issues, including users misusing accounts or not following best practices.</p>
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
<td>Dropbox: Admin user with unverified secondary email</td>
<td><code>cebb4104-1235-4049-a664-9fcd003ece71</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Admin user with restricted directory access</td>
<td><code>19378bb3-a3b7-4ee5-8ea7-39eec0a2ca7c</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: User with unverified email</td>
<td><code>2b5804f7-4888-4872-a85a-a64805d10654</code></td>
<td>Medium</td>
</tr>
<tr>
<td>Dropbox: Invited user</td>
<td><code>44d34aab-82fb-4a60-8e35-d7a75cfc789c</code></td>
<td>Low</td>
</tr>
<tr>
<td>Dropbox: Suspended user</td>
<td><code>e356cfe6-97e6-4e30-9cb9-4a42a387844e</code></td>
<td>Low</td>
</tr>
<tr>
<td>Dropbox: User with secondary email configured</td>
<td><code>4bbb795a-cd34-41ba-865d-9bf9de61a592</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
