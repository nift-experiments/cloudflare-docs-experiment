---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/
  description: New updates and improvements at Cloudflare.
  full_title: Optional OAuth scopes · Changelog
  head_html: <title>Optional OAuth scopes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Optional OAuth scopes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/#page","headline":"Optional OAuth scopes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-20-oauth-optional-scopes/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 20, 2026</time><h2 id="post-title">Optional OAuth scopes</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>We're announcing the GA of Optional OAuth Scopes.</p>
<p>OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .</p>
<h4 id="what-s-new">What's New</h4>
<p><strong>Optional Scopes:</strong> OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.</p>
<p><strong>Scope Selection:</strong> On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.</p>
<p><strong>Templates:</strong> The consent screen now includes <strong>Read Only</strong> and <strong>Full Access</strong> templates to make scope selection faster and easier.</p>
<p><strong>Search:</strong> Users can now search scopes in the consent screen.</p>
<p>Learn how to <a href="/fundamentals/oauth/create-an-oauth-client/#select-scopes">select client scopes</a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">edit optional permissions</a>.</p>
</div></article></div>
