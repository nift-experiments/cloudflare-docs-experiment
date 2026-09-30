---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/
  description: New updates and improvements at Cloudflare.
  full_title: Search API tokens by name · Changelog
  head_html: <title>Search API tokens by name · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Search API tokens by name · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/#page","headline":"Search API tokens by name \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-25-api-token-search/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 25, 2026</time><h2 id="post-title">Search API tokens by name</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.</p>
<h4 id="what-s-new">What's new</h4>
<ul>
<li><strong>Dashboard search</strong>: Both <a href="https://dash.cloudflare.com/?to=/:account/account-api-tokens">account API tokens</a> and <a href="https://dash.cloudflare.com/profile/api-tokens">user API tokens</a> pages now include a search bar. Type a name to filter results.</li>
<li><strong>API search support</strong>: The <a href="/api/resources/user/subresources/tokens/methods/list/"><code>/user/tokens</code></a> and <a href="/api/resources/accounts/subresources/tokens/methods/list/"><code>/accounts/{account_id}/tokens</code></a> endpoints now accept a <code>name</code> query parameter to filter tokens by name.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/get-started/create-token/">Create an API token</a> and <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a>.</p>
</div></article></div>
