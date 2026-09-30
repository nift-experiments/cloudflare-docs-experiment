---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/
  description: New updates and improvements at Cloudflare.
  full_title: Account Role API deprecated · Changelog
  head_html: <title>Account Role API deprecated · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Account Role API deprecated · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/#page","headline":"Account Role API deprecated \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-21-account-role-api-deprecated/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 21, 2026</time><h2 id="post-title">Account Role API deprecated</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> is deprecated and is being replaced by the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. An end of life date has not yet been established.</p>
<h4 id="what-you-need-to-do">What you need to do</h4>
<p>Review the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a> documentation; the response schema differs from the legacy Roles response.</p>
<h4 id="highlights">Highlights</h4>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div></article></div>
