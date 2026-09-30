---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/
  description: New updates and improvements at Cloudflare.
  full_title: Smart Tiered Cache Fallback to Generic · Changelog
  head_html: <title>Smart Tiered Cache Fallback to Generic · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Smart Tiered Cache Fallback to Generic · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/#page","headline":"Smart Tiered Cache Fallback to Generic \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 29, 2025</time><h2 id="post-title">Smart Tiered Cache Fallback to Generic</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p><a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a> now falls back to <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Tiered Cache</a> when the origin location cannot be determined, improving cache precision for your content.</p>
<p>Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.</p>
<h4 id="how-it-works">How it works</h4>
<p>When Smart Tiered Cache falls back to Generic Tiered Cache:</p>
<ol>
<li><strong>Multiple upper-tiers</strong>: Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.</li>
<li><strong>Distributed cache requests</strong>: Lower-tier data centers can query any available upper-tier for cached content.</li>
<li><strong>Improved global coverage</strong>: Provides better cache hit ratios across geographically distributed visitors.</li>
<li><strong>Automatic fallback</strong>: Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.</li>
</ol>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Preserves high performance during fallback</strong>: Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.</li>
<li><strong>Minimizes latency impact</strong>: Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.</li>
<li><strong>Seamless experience</strong>: No configuration changes or intervention required when fallback occurs.</li>
<li><strong>Improved resilience</strong>: Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>This improvement is automatically applied to all zones using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. No action is required on your part.</p>
</div></article></div>
