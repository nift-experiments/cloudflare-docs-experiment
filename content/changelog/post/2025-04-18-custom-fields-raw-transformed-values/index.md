---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/
  description: New updates and improvements at Cloudflare.
  full_title: Custom fields raw and transformed values support · Changelog
  head_html: <title>Custom fields raw and transformed values support · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Custom fields raw and transformed values support · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/#page","headline":"Custom fields raw and transformed values support \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-18-custom-fields-raw-transformed-values/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-04-18-custom-fields-raw-transformed-values/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 18, 2025</time><h2 id="post-title">Custom fields raw and transformed values support</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Custom Fields now support logging both <strong>raw and transformed values</strong> for request and response headers in the HTTP requests dataset.</p>
<p>These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.</p>
<p>By default:</p>
<ul>
<li>Request headers are logged as raw values</li>
<li>Response headers are logged as transformed values</li>
</ul>
<p>These defaults can be overridden to suit your logging needs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17737.md")</aside>
<p>For more information refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> documentation</p>
</div></article></div>
