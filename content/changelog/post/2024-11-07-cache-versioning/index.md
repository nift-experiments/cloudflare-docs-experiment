---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/
  description: New updates and improvements at Cloudflare.
  full_title: Stage and test cache configurations safely · Changelog
  head_html: <title>Stage and test cache configurations safely · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Stage and test cache configurations safely · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/#page","headline":"Stage and test cache configurations safely \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-11-07-cache-versioning/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 7, 2024</time><h2 id="post-title">Stage and test cache configurations safely</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.</p>
<h4 id="how-it-works">How it works</h4>
<p>With versioned environments, you can:</p>
<ol>
<li><strong>Create staging versions</strong> of your cache configuration.</li>
<li><strong>Test cache rules</strong> in a non-production environment.</li>
<li><strong>Purge staged content</strong> independently from production.</li>
<li><strong>Validate changes</strong> before promoting to production.</li>
</ol>
<p>This capability integrates with Cloudflare's broader <a href="/version-management/">versioning system</a>, allowing you to manage cache configurations alongside other zone settings.</p>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Risk-free testing</strong>: Validate configuration changes without impacting production.</li>
<li><strong>Independent purging</strong>: Clear staging cache without affecting live content.</li>
<li><strong>Deployment confidence</strong>: Catch issues before they reach end users.</li>
<li><strong>Team collaboration</strong>: Multiple team members can work on different versions.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/version-management/">version management documentation</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="important-limitation">Important limitation</h4>
@markup("md", "content/.markup/bodies/17701.md")</aside>
</div></article></div>
