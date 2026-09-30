---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/
  description: New updates and improvements at Cloudflare.
  full_title: Audit Logs v2 — Resource History · Changelog
  head_html: <title>Audit Logs v2 — Resource History · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Audit Logs v2 — Resource History · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/#page","headline":"Audit Logs v2 \u2014 Resource History \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-27-audit-logs-v2-resource-history/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 27, 2026</time><h2 id="post-title">Audit Logs v2 — Resource History</h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 now includes <strong>Resource History</strong>. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_resource_history.png" alt="Resource History in Audit Logs v2" /></p>
<p><strong>Dashboard:</strong></p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for that resource.</li>
<li>Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p><strong>API:</strong></p>
<p>Use the History endpoint to retrieve the change history for any audit log entry:</p>
<pre tabindex="0"><code class="language-txt">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The endpoint is also available for organization-scoped audit logs at <code>/organizations/{organization_id}/logs/audit/{id}/history</code>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/#resource-history">Resource History documentation</a>.</p>
</div></article></div>
