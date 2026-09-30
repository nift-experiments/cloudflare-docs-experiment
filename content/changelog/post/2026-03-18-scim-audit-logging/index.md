---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/
  description: New updates and improvements at Cloudflare.
  full_title: SCIM audit logging Support · Changelog
  head_html: <title>SCIM audit logging Support · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="SCIM audit logging Support · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/#page","headline":"SCIM audit logging Support \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-18-scim-audit-logging/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2026</time><h2 id="post-title">SCIM audit logging Support</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare dashboard SCIM provisioning operations are now captured in <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2</a>, giving you visibility into user and group changes made by your identity provider.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-03-18-scim-audit-logging.png" alt="SCIM audit logging" /></p>
<p><strong>Logged actions:</strong></p>
<table>
<thead>
<tr>
<th>Action Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Create SCIM User</td>
<td>User provisioned from IdP</td>
</tr>
<tr>
<td>Replace SCIM User</td>
<td>User fully replaced (PUT)</td>
</tr>
<tr>
<td>Update SCIM User</td>
<td>User attributes modified (PATCH)</td>
</tr>
<tr>
<td>Delete SCIM User</td>
<td>Member deprovisioned</td>
</tr>
<tr>
<td>Create SCIM Group</td>
<td>Group provisioned from IdP</td>
</tr>
<tr>
<td>Update SCIM Group</td>
<td>Group membership or attributes modified</td>
</tr>
<tr>
<td>Delete SCIM Group</td>
<td>Group deprovisioned</td>
</tr>
</tbody>
</table>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>
</div></article></div>
