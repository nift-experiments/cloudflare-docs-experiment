---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/
  description: New updates and improvements at Cloudflare.
  full_title: URL Scanner now supports geo-specific scanning · Changelog
  head_html: <title>URL Scanner now supports geo-specific scanning · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="URL Scanner now supports geo-specific scanning · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/#page","headline":"URL Scanner now supports geo-specific scanning \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-05-07-url-scanner-geoegress/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 8, 2025</time><h2 id="post-title">URL Scanner now supports geo-specific scanning</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Enterprise customers can now choose the geographic location from which a URL scan is performed — either via <a href="/security-center/investigate/">Security Center</a> in the Cloudflare dashboard or via the <a href="/api/resources/url_scanner/subresources/scans/methods/create/">URL Scanner API</a>.</p>
<p>This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>Location Picker: Select a location for the scan via <strong>Security Center → Investigate</strong> in the dashboard or through the API.</li>
<li>Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.</li>
<li>Default behavior: If no location is set, scans default to the user’s current geographic region.</li>
</ul>
<p>Learn more in the <a href="/security-center/">Security Center documentation</a>.</p>
</div></article></div>
