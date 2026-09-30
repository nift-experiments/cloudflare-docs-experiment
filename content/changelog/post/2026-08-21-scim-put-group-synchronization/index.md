---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/
  description: New updates and improvements at Cloudflare.
  full_title: Improved SCIM 2.0 group synchronization · Changelog
  head_html: <title>Improved SCIM 2.0 group synchronization · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improved SCIM 2.0 group synchronization · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/#page","headline":"Improved SCIM 2.0 group synchronization \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-21-scim-put-group-synchronization/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Improved SCIM 2.0 group synchronization</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Dashboard SCIM now supports replacing groups using HTTP <code>PUT</code>, as defined by <a href="https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1">RFC 7644 section 3.5.1</a>. This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.</p>
<p><strong>What's New</strong></p>
<p><strong>Group replacement via <code>PUT</code></strong>: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17732.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
</ul>
</div></article></div>
