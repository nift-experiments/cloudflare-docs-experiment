---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/
  description: New updates and improvements at Cloudflare.
  full_title: Improvements to Monitoring Using Zone Settings · Changelog
  head_html: <title>Improvements to Monitoring Using Zone Settings · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improvements to Monitoring Using Zone Settings · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/#page","headline":"Improvements to Monitoring Using Zone Settings \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-06-zone-monitoring-improvements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 6, 2025</time><h2 id="post-title">Improvements to Monitoring Using Zone Settings</h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.</p>
<p>All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.</p>
<h4 id="what-you-can-expect">What you can expect:</h4>
<ul>
<li>More reliable application of zone settings to monitoring requests, including
<ul>
<li>Authenticated Origin Pulls</li>
<li>Aegis Egress IP Pools</li>
<li>Argo Smart Routing</li>
<li>HTTP/2 to Origin</li>
</ul>
</li>
<li>Improved support and bug fixes for retries, redirects, and proxied origin resolution</li>
<li>Improved performance and reliability of monitoring requests within the Cloudflare network</li>
<li>Unrelated CDN or WAF configuration changes should have no risk of impact to pool health</li>
</ul>
</div></article></div>
